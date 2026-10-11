#!/usr/bin/env python3
"""row_keyboard.py -- the set keyboard, posted BY CODE, one per owed row.

WHY (owner live 2026-10-08). Everything the engine posted itself reached the
owner (rest countdown + its buttons, the set table "delivered=yes by=code").
Everything that waited on the agent relaying a marker line went missing for a
whole session: the reps drilldown on working rows and the completion tap on
prep / setup / ramp rows. The owner's ruling: buttons must not depend on the
agent. This module is the keyboard layer that makes that true.

THE CONTRACT
  * ONE keyboard per owed row, keyed (session, exercise, set_seq). The row's
    kind decides the keyboard, never the caller's prose:
        working              reps drilldown -> RIR, swapped IN PLACE by the
                             bridge (2026-08-21 drilldown contract) -- rail
                             `idrill`, no model turn per tap
        setup / ramp rung    one completion tap -- rail `idrill` (step_final 1)
        prep drill           one completion tap -- rail `opt`: the tap reaches
                             the agent as a user message, exactly as the
                             model-authored single button did before
        hold                 NOT here: the timer keeps its own buttons
  * POSTED BY CODE through push.sh --strict --buttons-json, so the message id
    comes back and is recorded (inplace_delivery, key row-kb:<sid>:<ex>:<seq>).
    The buttons carry the SAME callback grammar the bridge renders for an
    `[[IDRILL:<arm>]]` marker (idrill:<arm>:<step>:<value>), so a tap is handled
    by the existing bridge handler with no bridge change.
  * IDEMPOTENT. A second post of the same row with the same content is a
    no-op; with different content it EDITS the row's own message. Posting a
    row CLEARS (edits away the buttons of) every other still-live row keyboard
    of the session, so two live keyboards never coexist. A logged row is done:
    when it was TAPPED the bridge already edited its message; when it was
    TYPED, the stale buttons are cleared. Undo clears. A tagged keyboard on
    the same row (the RIR ask) is closed by on_logged too.

  Detached like every other channel-2 push: schedule() writes the row state
  under a session lock and spawns `row_keyboard.py run <state> <token>` after
  the caller's delay; the worker re-checks token, generation fence and the DB
  (a row logged in the meantime is not owed any more) before it sends.
  WARG_ROW_KB_SYNC=1 runs the worker inline with no sleep (suites, probes).

Never raises to a caller. stdlib only. ASCII only (copy is passed in).
"""

import fcntl
import hashlib
import json
import os
import re
import sqlite3
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))

KIND_REPS = "reps_drilldown"
KIND_TAP = "completion_tap"
RAIL_IDRILL = "idrill"
RAIL_OPT = "opt"

ST_PENDING = "pending"     # scheduled, worker has not sent yet
ST_LIVE = "live"           # on screen, buttons live, message id recorded
ST_LEGACY = "live_legacy"  # on screen via the non-strict marker push (no id)
ST_DONE = "done"           # the row was logged -- owes nothing any more
ST_CLEARED = "cleared"     # superseded / undone: buttons edited away
ST_DROPPED = "dropped"     # worker woke to a superseded / not-owed row
OPEN_STATES = (ST_PENDING, ST_LIVE, ST_LEGACY)

SYNC_ENV = "WARG_ROW_KB_SYNC"
CALLBACK_DATA_MAX_BYTES = 64
SEND_TIMEOUT_SEC = 25
_KEY_SAFE = re.compile(r"[^A-Za-z0-9_.-]")


# --------------------------------------------------------------------------
# paths / small helpers
# --------------------------------------------------------------------------
def _safe(s):
    return _KEY_SAFE.sub("_", str(s))


def session_dir(state_dir, session_id):
    return os.path.join(state_dir, ".row-kb", _safe(session_id))


def row_path(state_dir, session_id, exercise_name, set_seq, tag=None):
    """`tag` names a second keyboard on the same row (r2 2026-10-10: the RIR
    ask on a logged warm-up rung) -- its own state file and message."""
    return os.path.join(session_dir(state_dir, session_id),
                        "%s.%s%s.json" % (_safe(exercise_name), int(set_seq),
                                          ("." + _safe(tag)) if tag else ""))


def surface_key(session_id, exercise_name, set_seq, tag=None):
    return "row-kb:%s:%s:%s%s" % (session_id, exercise_name, int(set_seq),
                                  (":" + tag) if tag else "")


def _inplace():
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import inplace_delivery
        return inplace_delivery
    except Exception:  # noqa: BLE001 -- no module -> the caller's old rail
        return None


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            st = json.load(fh)
        return st if isinstance(st, dict) else None
    except (OSError, ValueError):
        return None


def _write(path, st):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(st, fh, ensure_ascii=False)
        os.replace(tmp, path)
        return True
    except OSError:
        return False


class _Lock(object):
    """flock on the session dir: one writer of row state at a time, so two
    concurrent set-arm runs cannot both decide they own a row's first send."""

    def __init__(self, state_dir, session_id):
        self.path = os.path.join(session_dir(state_dir, session_id), ".lock")
        self.fh = None

    def __enter__(self):
        try:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            self.fh = open(self.path, "a")
            fcntl.flock(self.fh.fileno(), fcntl.LOCK_EX)
        except OSError:
            self.fh = None
        return self

    def __exit__(self, *exc):
        if self.fh is not None:
            try:
                fcntl.flock(self.fh.fileno(), fcntl.LOCK_UN)
                self.fh.close()
            except OSError:
                pass
        return False


def _log(ch2_log, fields):
    """One CH2_KB line in the channel-2 diagnostic log (best-effort)."""
    if not ch2_log:
        return
    try:
        ts = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
        with open(ch2_log, "a") as fh:
            fh.write(ts + "\t" + "\t".join(
                str(f).replace("\t", " ").replace("\n", " ")
                for f in fields) + "\n")
    except Exception:  # noqa: BLE001 -- logging never costs a keyboard
        pass


def _sha(text, rows):
    blob = (text or "") + "\n\0" + json.dumps(rows or [], ensure_ascii=False,
                                              sort_keys=True)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


# --------------------------------------------------------------------------
# capability: strict send + edit, probed once per push binary
# --------------------------------------------------------------------------
def usable(push_bin, state_dir):
    """True when push.sh declares both `strict` (message id back, real
    buttons) and `edit` (in-place update / clear). Cached on disk per binary
    (path + mtime + size), so the probe runs once per install, not per set.
    False -> the caller keeps its pre-existing rail, byte for byte."""
    try:
        st = os.stat(push_bin)
    except (OSError, TypeError):
        return False
    tag = "%s|%s|%s" % (os.path.realpath(push_bin), int(st.st_mtime),
                        st.st_size)
    cache = os.path.join(state_dir, ".row-kb", "caps.json")
    rec = _read(cache) or {}
    if tag in rec:
        return bool(rec[tag])
    ok = False
    try:
        # A binary whose source never mentions the flag cannot answer it, so
        # it is not RUN: a recorder / neutralised shim must see no call at all
        # (a probe would read as a push in its log).
        with open(push_bin, "rb") as fh:
            declares = b"--capabilities" in fh.read(1 << 20)
        if not declares:
            raise OSError("no --capabilities in %s" % push_bin)
        p = subprocess.run([push_bin, "--capabilities"], capture_output=True,
                           text=True, timeout=5)
        words = set(re.findall(r"[a-z-]+", p.stdout or ""))
        ok = p.returncode == 0 and "strict" in words and "edit" in words
    except Exception:  # noqa: BLE001 -- no capability, never a crash
        ok = False
    rec[tag] = ok
    _write(cache, rec)
    return ok


# --------------------------------------------------------------------------
# button rows
# --------------------------------------------------------------------------
def _is_pair(e):
    return (isinstance(e, (list, tuple)) and len(e) == 2
            and all(isinstance(x, str) for x in e))


def idrill_rows(arm_id, payload, step="1"):
    """(rows, text) for an arm's step -- the SAME rows the bridge renders
    from an `[[IDRILL:<arm>]]` marker (bridge/artifacts.py
    build_step_keyboard_spec): flat [[label, value], ...] = one row, a list of
    such lists = a grid; callback `idrill:<arm>:<step>:<value>`; a button
    whose callback overflows 64 bytes is dropped. ([], "") when nothing would
    render -- the caller then keeps its old rail."""
    if not isinstance(payload, dict):
        return [], ""
    entries = (payload.get("step_buttons") or {}).get(step)
    text = ((payload.get("step_text") or {}).get(step) or "").strip()
    if not isinstance(entries, list) or not entries:
        return [], text
    if all(_is_pair(e) for e in entries):
        decl = [list(entries)]
    else:
        decl = []
        for e in entries:
            if isinstance(e, list) and e and all(_is_pair(b) for b in e):
                decl.append(e)
            elif _is_pair(e):
                decl.append([e])
    selected, marker = set(), ""
    if isinstance(payload.get("step_slots"), dict) and payload["step_slots"]:
        selected, marker, text = _initial_slots(payload, step, text)
    rows = []
    for row in decl:
        out = []
        for label, value in row:
            cb = "idrill:%s:%s:%s" % (arm_id, step, value)
            if len(cb.encode("utf-8")) > CALLBACK_DATA_MAX_BYTES:
                continue
            if value in selected:
                label = marker + label
            out.append({"text": label, "callback_data": cb})
        if out:
            rows.append(out)
    return rows, text


SLOT_TOKEN_RE = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*)\}")


def _initial_slots(payload, step, text):
    """DGN-1955 slot arm, INITIAL render (no taps yet): the bridge's
    build_step_keyboard_spec marks each slot's slot_default value on its step
    and fills {slot} in the step text (unset -> `?`; undeclared stays
    verbatim). Mirrored here so the code-posted keyboard is the bridge's.
    Returns (selected values on `step`, marker, filled text)."""
    names, display, owner = set(), {}, {}
    for st, per in payload["step_slots"].items():
        for slot, values in (per.items() if isinstance(per, dict) else ()):
            pairs = (values.items() if isinstance(values, dict)
                     else [(v, v) for v in values or ()])
            names.add(slot)
            for value, disp in pairs:
                owner.setdefault((st, value), (slot, disp))
    selected = set()
    for slot, value in (payload.get("slot_default") or {}).items():
        for (st, v), (s, disp) in owner.items():
            if v == value and s == slot:
                display[slot] = disp
                if st == step:
                    selected.add(v)
                break
    marker = payload.get("selected_marker") or "\u25cf "
    text = SLOT_TOKEN_RE.sub(
        lambda m: (display.get(m.group(1), "?") if m.group(1) in names
                   else m.group(0)), text)
    return selected, marker, text


def opt_rows(label):
    """ONE `opt:` button: the tap is sent to the agent as a user message (the
    bridge recovers the full label from the button text when the callback had
    to fall back to the number form)."""
    cb = "opt:%s" % label
    if len(cb.encode("utf-8")) > CALLBACK_DATA_MAX_BYTES:
        cb = "opt:1"
    return [[{"text": label, "callback_data": cb}]]


# --------------------------------------------------------------------------
# the DB question: is this row logged?
# --------------------------------------------------------------------------
def row_logged(db_path, session_id, exercise_name, set_seq):
    if not db_path or not os.path.exists(db_path):
        return False
    try:
        conn = sqlite3.connect("file:%s?mode=ro" % db_path, uri=True,
                               timeout=5)
        try:
            r = conn.execute(
                "SELECT 1 FROM workout_sets WHERE session_id=? AND "
                "exercise_name=? AND set_seq=? LIMIT 1",
                (int(session_id), exercise_name, int(set_seq))).fetchone()
        finally:
            conn.close()
        return r is not None
    except Exception:  # noqa: BLE001 -- unknown -> treat as owed
        return False


# --------------------------------------------------------------------------
# schedule (caller side)
# --------------------------------------------------------------------------
def schedule(state_dir, push_bin, session_id, exercise_name, set_seq, kind,
             rail, text, rows, arm_id=None, db_path=None, delay=0, gen=None,
             gen_file=None, ch2_log=None, legacy_text=None, channel="row-kb",
             dry_run=False, out=None, tag=None, owed_logged=False):
    """Put row (session, exercise, set_seq)'s keyboard on its way. Returns:
        "scheduled"  a send (or an in-place edit of this row's own message)
                     is on its way
        "already"    this exact keyboard is already live / on its way
        "not_owed"   the row is logged -- it owes no keyboard
        "invalid"    nothing renderable was given (caller keeps its rail)"""
    if not rows or not (text or "").strip():
        return "invalid"
    path = row_path(state_dir, session_id, exercise_name, set_seq, tag)
    sha = _sha(text, rows)
    if dry_run:
        if out is not None:
            out.append("[row-kb +%ds] seq=%s kind=%s rail=%s arm=%s"
                       % (int(delay or 0), set_seq, kind, rail, arm_id or "-"))
        return "scheduled"
    with _Lock(state_dir, session_id):
        cur = _read(path) or {}
        if cur.get("state") == ST_DONE:
            return "not_owed"
        if cur.get("state") in OPEN_STATES and cur.get("sha") == sha:
            return "already"
        token = "%d.%d" % (time.time() * 1e6, os.getpid())
        st = {
            "session_id": session_id, "exercise_name": exercise_name,
            "set_seq": int(set_seq), "kind": kind, "rail": rail,
            "arm_id": arm_id, "text": text, "rows": rows, "sha": sha,
            "token": token, "state": ST_PENDING, "db": db_path,
            "push": push_bin, "state_dir": state_dir, "ch2_log": ch2_log,
            "delay": int(delay or 0), "gen": gen, "gen_file": gen_file,
            "legacy_text": legacy_text, "channel": channel,
            "scheduled_at": time.time(), "tag": tag,
            "owed_logged": bool(owed_logged),
        }
        _write(path, st)
    _log(ch2_log, ["CH2_INTENT", session_id, channel,
                   "delay=%ds" % int(delay or 0),
                   "row=%s:%s" % (exercise_name, set_seq),
                   "kind=%s" % kind, "rail=%s" % rail])
    _spawn(["run", path, token])
    return "scheduled"


def _spawn(argv):
    if os.environ.get(SYNC_ENV) == "1":
        run_row(argv[1], argv[2], sleep=False)
        return
    try:
        subprocess.Popen(
            [sys.executable, os.path.abspath(__file__)] + argv,
            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL, start_new_session=True)
    except Exception:  # noqa: BLE001 -- a lost keyboard never costs a set
        pass


# --------------------------------------------------------------------------
# the worker
# --------------------------------------------------------------------------
def _gen_current(st):
    gf, gen = st.get("gen_file"), st.get("gen")
    if not gf or not gen:
        return True
    if not os.path.exists(gf):
        return False           # the session was aborted / closed (spawn())
    try:
        with open(gf) as fh:
            cur = fh.read().strip()
    except OSError:
        return True            # fail-open, like spawn()'s guard
    return not cur or cur == str(gen)


def _clear_one(st, why):
    """Edit the row's message so it keeps its text and loses its buttons.
    Only a row with a recorded message id can be cleared; a legacy-rail row
    has none and is merely marked."""
    mod = _inplace()
    push = st.get("push")
    sd = st.get("state_dir")
    key = surface_key(st["session_id"], st["exercise_name"], st["set_seq"],
                      st.get("tag"))
    outcome = "no_message"
    if st.get("state") == ST_LIVE and mod is not None and push and sd \
            and mod.read_record(sd, key) is not None:
        if mod.can_edit(push):
            ok, detail, _mid = mod.deliver(key, st.get("text") or "", push,
                                           sd, timeout=SEND_TIMEOUT_SEC,
                                           buttons=[])
            outcome = detail if ok else "failed:%s" % detail
        else:
            outcome = "no_edit_capability"
        # A cleared row that is posted again starts a NEW message at the
        # bottom of the chat; editing one scrolled far up would be invisible.
        mod.drop_record(sd, key)
    _log(st.get("ch2_log"), ["CH2_KB", st["session_id"], "row-kb-clear",
                             "row=%s:%s" % (st["exercise_name"],
                                            st["set_seq"]),
                             "why=%s" % why, outcome])
    return outcome


def _supersede(st):
    """Clear every OTHER open row keyboard of this session (lock held)."""
    sdir = session_dir(st["state_dir"], st["session_id"])
    try:
        names = sorted(os.listdir(sdir))
    except OSError:
        return
    me = row_path(st["state_dir"], st["session_id"], st["exercise_name"],
                  st["set_seq"], st.get("tag"))
    for name in names:
        if not name.endswith(".json"):
            continue
        p = os.path.join(sdir, name)
        if os.path.abspath(p) == os.path.abspath(me):
            continue
        other = _read(p)
        if not other or other.get("state") not in OPEN_STATES:
            continue
        if other.get("state") == ST_PENDING:
            other["state"] = ST_DROPPED      # its worker will see the token
            other["token"] = "superseded"
        else:
            _clear_one(other, "superseded")
            other["state"] = ST_CLEARED
        other["closed_at"] = time.time()
        _write(p, other)


def _send_legacy(st):
    """The pre-existing marker push (non-strict): still code-posted, just not
    editable. Used only when the strict send could not land."""
    text = st.get("legacy_text")
    push = st.get("push")
    if not text or not push:
        return False
    try:
        p = subprocess.run([push, "--text", text], capture_output=True,
                           text=True, timeout=SEND_TIMEOUT_SEC)
        return p.returncode == 0
    except Exception:  # noqa: BLE001
        return False


def run_row(path, token, sleep=True):
    st = _read(path)
    if not st or st.get("token") != token:
        return "superseded"
    if sleep and st.get("delay"):
        time.sleep(int(st["delay"]))
    sid, sd = st["session_id"], st["state_dir"]
    with _Lock(sd, sid):
        st = _read(path)
        row = "%s:%s" % ((st or {}).get("exercise_name"),
                         (st or {}).get("set_seq"))
        if not st or st.get("token") != token \
                or st.get("state") != ST_PENDING:
            return "superseded"
        log = st.get("ch2_log")
        if not _gen_current(st):
            st["state"] = ST_DROPPED
            _write(path, st)
            _log(log, ["CH2_KB", sid, st.get("channel"), "row=%s" % row,
                       "SUPPRESSED-gen"])
            return "suppressed"
        if not st.get("owed_logged") and row_logged(
                st.get("db"), sid, st["exercise_name"], st["set_seq"]):
            st["state"] = ST_DONE
            _write(path, st)
            _log(log, ["CH2_KB", sid, st.get("channel"), "row=%s" % row,
                       "NOT_OWED (row already logged)"])
            return "not_owed"
        _supersede(st)
        mod = _inplace()
        push = st.get("push")
        key = surface_key(sid, st["exercise_name"], st["set_seq"],
                          st.get("tag"))
        ok, detail, mid = False, "no_inplace_module", None
        if mod is not None:
            ok, detail, mid = mod.deliver(key, st["text"], push, sd,
                                          timeout=SEND_TIMEOUT_SEC,
                                          buttons=st["rows"])
        if ok:
            st["state"] = ST_LIVE
            st["message_id"] = mid
            st["sent_at"] = time.time()
            _write(path, st)
            _log(log, ["CH2_KB", sid, st.get("channel"), "row=%s" % row,
                       "kind=%s" % st.get("kind"),
                       "SENT by=code %s mid=%s" % (detail, mid)])
            return "sent"
        if detail in ("edit_uncertain", "send_rc=6"):
            # The edit / send may be on screen already; another send would be
            # the duplicate keyboard. An uncertain NEW send has no id to edit,
            # so it is kept like a legacy-rail row (marked, never re-sent).
            st["state"] = ST_LIVE if detail == "edit_uncertain" else ST_LEGACY
            _write(path, st)
            _log(log, ["CH2_KB", sid, st.get("channel"), "row=%s" % row,
                       "UNCERTAIN (not re-sent)"])
            return "uncertain"
        if st.get("rail") == RAIL_IDRILL and _send_legacy(st):
            st["state"] = ST_LEGACY
            st["sent_at"] = time.time()
            _write(path, st)
            _log(log, ["CH2_KB", sid, st.get("channel"), "row=%s" % row,
                       "SENT by=code legacy-marker strict=%s" % detail])
            return "sent_legacy"
        st["state"] = ST_DROPPED
        _write(path, st)
        _log(log, ["CH2_KB", sid, st.get("channel"), "row=%s" % row,
                   "FAILED %s" % detail])
        return "failed"


# --------------------------------------------------------------------------
# lifecycle hooks (set-add, set-undo)
# --------------------------------------------------------------------------
def on_logged(state_dir, session_id, exercise_name, set_seq, tapped):
    """The row was just written. It owes nothing any more. TAPPED (the bridge
    consumed the arm before firing set-add) -> the bridge already edited the
    message; leave it. TYPED -> its buttons are stale: clear them. Returns the
    row's previous state, or None when no keyboard was ever posted for it."""
    for tagged in _tagged_paths(state_dir, session_id, exercise_name,
                                set_seq):
        with _Lock(state_dir, session_id):
            st = _read(tagged)
            if st and st.get("state") in OPEN_STATES:
                if st.get("state") != ST_PENDING:
                    _clear_one(st, "answered")
                st["state"] = ST_DONE
                st["token"] = "done"
                st["closed_at"] = time.time()
                _write(tagged, st)
    path = row_path(state_dir, session_id, exercise_name, set_seq)
    if not os.path.exists(path):
        return None
    with _Lock(state_dir, session_id):
        st = _read(path)
        if not st:
            return None
        prev = st.get("state")
        if prev in OPEN_STATES and not tapped and prev != ST_PENDING:
            _clear_one(st, "logged_by_text")
        else:
            # Tapped: the bridge edited this message already. Forget it, so a
            # re-post after an undo is a NEW message at the bottom of the chat.
            mod = _inplace()
            if mod is not None:
                mod.drop_record(state_dir, surface_key(
                    session_id, exercise_name, set_seq))
        st["state"] = ST_DONE
        st["token"] = "done"
        st["closed_at"] = time.time()
        _write(path, st)
    return prev


def _tagged_paths(state_dir, session_id, exercise_name, set_seq):
    head = "%s.%s." % (_safe(exercise_name), int(set_seq))
    sdir = session_dir(state_dir, session_id)
    try:
        names = sorted(os.listdir(sdir))
    except OSError:
        return []
    return [os.path.join(sdir, n) for n in names
            if n.startswith(head) and n.endswith(".json")
            and n != head + "json"]


def clear_rows(state_dir, session_id, exercise_name=None, why="undo"):
    """Clear every open row keyboard of the session (or of one exercise).
    Returns [(exercise, seq, previous_state)]."""
    sdir = session_dir(state_dir, session_id)
    cleared = []
    try:
        names = sorted(os.listdir(sdir))
    except OSError:
        return cleared
    with _Lock(state_dir, session_id):
        for name in names:
            if not name.endswith(".json"):
                continue
            p = os.path.join(sdir, name)
            st = _read(p)
            if not st or st.get("state") not in OPEN_STATES:
                continue
            if exercise_name and st.get("exercise_name") != exercise_name:
                continue
            prev = st.get("state")
            if prev != ST_PENDING:
                _clear_one(st, why)
            st["state"] = ST_CLEARED
            st["token"] = "cleared"
            st["closed_at"] = time.time()
            _write(p, st)
            cleared.append((st.get("exercise_name"), st.get("set_seq"), prev))
    return cleared


def release_unlogged(state_dir, session_id, exercise_name=None):
    """After a delete: every DONE row whose DB row is gone is owed again, so
    its DONE mark is dropped (a later post of its keyboard is not refused as
    not_owed). Returns [(exercise, seq)]."""
    out = []
    for st in rows_of(state_dir, session_id):
        if st.get("state") != ST_DONE:
            continue
        if exercise_name and st.get("exercise_name") != exercise_name:
            continue
        if not row_logged(st.get("db"), session_id, st.get("exercise_name"),
                          st.get("set_seq")):
            if reopen_row(state_dir, session_id, st.get("exercise_name"),
                          st.get("set_seq")):
                out.append((st.get("exercise_name"), st.get("set_seq")))
    return out


def reopen_row(state_dir, session_id, exercise_name, set_seq):
    """An undone row is owed again: drop its DONE mark so the next post of
    its keyboard is not refused as not_owed."""
    path = row_path(state_dir, session_id, exercise_name, set_seq)
    with _Lock(state_dir, session_id):
        st = _read(path)
        if st and st.get("state") == ST_DONE:
            st["state"] = ST_CLEARED
            st["token"] = "reopened"
            _write(path, st)
            return True
    return False


def rows_of(state_dir, session_id):
    """Every row state of a session (diagnostics, suites)."""
    sdir = session_dir(state_dir, session_id)
    out = []
    try:
        names = sorted(os.listdir(sdir))
    except OSError:
        return out
    for name in names:
        if name.endswith(".json"):
            st = _read(os.path.join(sdir, name))
            if st:
                out.append(st)
    return out


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    sleep = "--no-sleep" not in argv
    argv = [a for a in argv if a != "--no-sleep"]
    if len(argv) == 3 and argv[0] == "run":
        print(run_row(argv[1], argv[2], sleep=sleep))
        return 0
    print("usage: row_keyboard.py run <row-state.json> <token> [--no-sleep]",
          file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
