# -*- coding: utf-8 -*-
"""machine_capture.py -- which machine a set is done on (kit 062, 2026-09-30).

WHY. The gym has two cable machines with different pin stacks (one 25 kg, the
other 1.25 + 2.5k), and one exercise bound exactly one ax_machine, so a
tricep_pushdown_rope snapped to the wrong grid (25 -> 23.75). The owner cannot
say whether the stacks feel equal ("내가 어케 알아"): measure, never ask them
to recall. Owner ruling 2026-09-30: open the STRUCTURE only -- nothing is
seeded, nothing restored from archive_health_reset_ax_machine. The agent
captures machines in conversation.

THE FLOW (per session, per machine/cable exercise):
  1. the session already chose a machine for this exercise -> use it
     (MACHINE_SESSION). A choice is held per session in a small state file and
     by the rows themselves (workout_sets.machine_ref).
  2. else the remembered choice -- the machine of the newest logged set of this
     exercise (kit machine-last) -> ONE confirm button + 다른 기계.
  3. else the candidates (kit machine-list --for-exercise) as buttons +
     다른 기계; a new name registers the machine (kit machine-register).
  Every set of the exercise then carries set-add --machine (set-add fills it
  from the session choice when the caller did not).
  The pin grid is LEARNED from the loads logged on the machine (kit
  machine-grid / machine-snap; rx-calc resolve_lattice reads it), and the
  owner's stated stack goes to kit machine-upd (lattice-set --machine).

ONE HOME FOR THE LOGIC. Every read and the register call are the kit's own
functions (training_axis.py, kit 062), imported from the kit's database dir --
the pack never re-implements machine-last / machine-list / the grid. No kit
module reachable (a pre-062 kit, a sandbox tree) -> no lines, nothing asked:
the exercise runs exactly as before.

Machine tokens only on stdout; the owner-facing ask is one short Korean line.
"""
import hashlib
import importlib
import json
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
# Per-process connection reuse (db_pool.py): the kit schema is parsed once per
# process, not once per lookup. Import failure -> plain sqlite3.connect.
# sys.path is left exactly as found (sibling-import resolution must not move).
try:
    sys.path.insert(0, HERE)
    try:
        from db_pool import connect as _db_connect
    finally:
        sys.path.remove(HERE)
except Exception:              # noqa: BLE001 -- degrade to a new connection per call
    _db_connect = sqlite3.connect
STATE_DIR = (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
             or os.path.join(HERE, "..", "..", "files", "program"))

# load_type / equipment values that mean "a machine with its own grid".
MACHINE_LOAD_TYPES = ("machine", "cable", "stack")
MACHINE_EQUIPMENT = ("cable", "machine", "stack", "selectorized")

ASK_CONFIRM = "지난번 그 기계(%s)예요?"
ASK_PICK = "어느 기계예요?"
ASK_PICK_CABLE = "어느 케이블이에요?"
OTHER_LABEL = "다른 기계"
# live batch 2 item 5 (owner 2026-10-08: the cable pick question with no registered
# machine and nothing to press). Zero machines -> never a pick over an empty
# set: ONE ask for a photo of the weight stack (or its increments), then the
# machine is registered from it (machine-pick --new + lattice-set --machine).
ASK_PHOTO = ("이 %s 무게 스택 사진 한 장 보내주세요 (어려우면 한 칸에 몇 kg씩 "
             "올라가는지만). 그걸로 기계를 등록할게요.")


def kit_axis(db_path=None):
    """The kit's training_axis module (kit 062 verbs), or None. Looked for
    beside the DB first (the installed layout: database/), then in the kit
    checkout the suites point at (DOGANY_LIFEKIT_DIR), then the installed
    layout relative to this file."""
    dirs = []
    if db_path:
        dirs.append(os.path.dirname(os.path.abspath(db_path)))
    kit = os.environ.get("DOGANY_LIFEKIT_DIR")
    if kit:
        dirs.append(os.path.join(kit, "payload", "database"))
    dirs.append(os.path.normpath(os.path.join(HERE, "..", "..", "database")))
    for d in dirs:
        if os.path.exists(os.path.join(d, "training_axis.py")):
            if d not in sys.path:
                sys.path.insert(0, d)
            try:
                mod = importlib.import_module("training_axis")
            except Exception:  # noqa: BLE001
                return None
            return mod if hasattr(mod, "machine_last") else None
    return None


def _conn(db_path):
    return _db_connect(db_path)


def has_machine_col(db_path):
    try:
        c = _conn(db_path)
        try:
            return any(r[1] == "machine_ref" for r in
                       c.execute("PRAGMA table_info(workout_sets)"))
        finally:
            c.close()
    except sqlite3.Error:
        return False


def is_machine_exercise(db_path, exercise):
    """True when the taxonomy says this lift runs on a machine grid:
    ax_exercise.load_type machine/cable/stack, or its equipment is one."""
    try:
        c = _conn(db_path)
    except sqlite3.Error:
        return False
    try:
        for sql in ("SELECT load_type FROM ax_exercise WHERE exercise_name=? "
                    "ORDER BY status='active' DESC LIMIT 1",
                    "SELECT equipment FROM exercise_movement_grip "
                    "WHERE exercise_name=?"):
            try:
                row = c.execute(sql, (exercise,)).fetchone()
            except sqlite3.Error:
                continue
            if row and row[0] and (row[0] in MACHINE_LOAD_TYPES
                                   or row[0] in MACHINE_EQUIPMENT):
                return True
        return False
    finally:
        c.close()


def _is_cable(db_path, exercise):
    try:
        c = _conn(db_path)
        try:
            row = c.execute("SELECT equipment FROM exercise_movement_grip "
                            "WHERE exercise_name=?", (exercise,)).fetchone()
        finally:
            c.close()
        return bool(row and row[0] == "cable") or "cable" in exercise
    except sqlite3.Error:
        return "cable" in exercise


# ---------------------------------------------------------------------------
# the session's choice
# ---------------------------------------------------------------------------

def pick_path(db_path, session_id):
    key = hashlib.sha256(os.path.realpath(db_path).encode()).hexdigest()[:16]
    return os.path.join(STATE_DIR, ".machine-pick",
                        "%s-%s.json" % (key, int(session_id)))


def _read_picks(db_path, session_id):
    try:
        with open(pick_path(db_path, session_id), encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def record_pick(db_path, session_id, exercise, ulid):
    """Hold `ulid` as this session's machine for `exercise`."""
    path = pick_path(db_path, session_id)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    data = _read_picks(db_path, session_id)
    data[exercise] = ulid
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, sort_keys=True)
    os.replace(tmp, path)


def session_machine(db_path, session_id, exercise):
    """(ulid, basis) this session already chose for `exercise`, or None.
    basis: pick (the choice file) | logged (a set of this session names it)."""
    if session_id is None:
        return None
    u = _read_picks(db_path, session_id).get(exercise)
    if u:
        return u, "pick"
    if not has_machine_col(db_path):
        return None
    try:
        c = _conn(db_path)
        try:
            row = c.execute(
                "SELECT machine_ref FROM workout_sets WHERE session_id=? AND "
                "exercise_name=? AND machine_ref IS NOT NULL "
                "ORDER BY id DESC LIMIT 1", (session_id, exercise)).fetchone()
        finally:
            c.close()
    except sqlite3.Error:
        return None
    return (row[0], "logged") if row else None


def machine_for(db_path, session_id, exercise):
    """(ulid, basis) the prescription should use: this session's choice, else
    the remembered one (kit machine-last: logged, then bound), else None."""
    hit = session_machine(db_path, session_id, exercise)
    if hit:
        return hit
    ta = kit_axis(db_path)
    if ta is None:
        return None
    try:
        c = _conn(db_path)
        try:
            last = ta.machine_last(c, exercise)
        finally:
            c.close()
    except Exception:  # noqa: BLE001
        return None
    return (last[0], last[1]) if last else None


def confirmed_machine(db_path, session_id, exercise):
    """The machine whose OWN history this lift's load reads today, or None.

    Confirmed = chosen this session, or the machine of the newest logged set.
    A static ax_exercise binding (machine_last basis 'bound') is not: nobody
    said the sets were done there, so the history stays pooled as before.
    None too for a free-weight lift or a DB without workout_sets.machine_ref."""
    if not (db_path and exercise and has_machine_col(db_path)
            and is_machine_exercise(db_path, exercise)):
        return None
    hit = machine_for(db_path, session_id, exercise)
    if not hit or hit[1] == "bound":
        return None
    return hit[0]


# ---------------------------------------------------------------------------
# the ask
# ---------------------------------------------------------------------------

def _label(db_path, ulid):
    try:
        c = _conn(db_path)
        try:
            row = c.execute("SELECT label FROM ax_machine WHERE ulid=?",
                            (ulid,)).fetchone()
        finally:
            c.close()
        return row[0] if row else ulid
    except sqlite3.Error:
        return ulid


def _q(text):
    return '"%s"' % str(text).replace('"', "'")


def ask_spec(db_path, session_id, exercise, pick_cmd=None):
    """The machine question for this entry as data, or None (not a machine
    lift / no kit 062 / DB predates 062). A session that already chose a
    machine yields {"session": (ulid, basis)} and no question. Otherwise:
    {"kind": confirm|pick, "ask", "last", "options": [(ulid, label)],
    "base": the machine-pick argv prefix}. entry_lines prints it for the
    model; ask_arm_payload turns the same data into the owner's keyboard."""
    if not (db_path and exercise and is_machine_exercise(db_path, exercise)):
        return None
    if not has_machine_col(db_path):
        return None
    ta = kit_axis(db_path)
    if ta is None:
        return None
    pick_cmd = pick_cmd or os.path.join(HERE, "machine-pick")
    hit = session_machine(db_path, session_id, exercise)
    if hit:
        return {"session": hit}
    c = _conn(db_path)
    try:
        last = ta.machine_last(c, exercise)
        cands = ta.machine_list(c, None, exercise)
    finally:
        c.close()
    options = []
    if last:
        options.append((last[0], _label(db_path, last[0])))
    for m, _why in cands:
        if all(m["ulid"] != u for u, _l in options):
            options.append((m["ulid"], m["label"]))
    if last:
        kind, ask = "confirm", ASK_CONFIRM % _label(db_path, last[0])
    elif not options:
        kind = "photo"
        ask = ASK_PHOTO % ("케이블" if _is_cable(db_path, exercise) else "기계")
    else:
        kind = "pick"
        ask = ASK_PICK_CABLE if _is_cable(db_path, exercise) else ASK_PICK
    return {"kind": kind, "ask": ask, "last": last, "options": options,
            "base": [pick_cmd, str(session_id), exercise]}


def _photo_line(exercise, base):
    """live batch 3 (2026-10-08 07:28): a photo of the stack ANSWERS the
    machine question -- one command registers the machine with the pins read
    off it (label derived from the stack) and holds it for the session."""
    return ("MACHINE_PHOTO exercise=%s cmd=%s -- a photo of the weight stack "
            "ANSWERS the machine question: run it with the lightest and "
            "heaviest plate read off the photo (add --addon <kg>|unknown when "
            "a block sits on the stack). Never ask which machine after a "
            "stack photo." % (exercise, " ".join(base + ["--stack",
                                                       "<min>-<max>"])))


def entry_lines(db_path, session_id, exercise, pick_cmd=None):
    """exercise-enter's machine lines. [] when the lift is not a machine
    lift, the kit has no 062 verbs, or the DB predates 062."""
    spec = ask_spec(db_path, session_id, exercise, pick_cmd)
    if not spec:
        return []
    if spec.get("session"):
        hit = spec["session"]
        return ["MACHINE_SESSION exercise=%s machine=%s label=%s basis=%s"
                % (exercise, hit[0], _q(_label(db_path, hit[0])), hit[1])]
    lines = []
    base, options, last = spec["base"], spec["options"], spec["last"]
    if spec["kind"] == "photo":
        lines.append("MACHINE_ASK exercise=%s kind=photo n=0 ask=%s -- no "
                     "machine is registered for this lift: ask this ONE "
                     "question (no buttons, never a pick). From the photo or "
                     "the stated increments run MACHINE_REGISTER, then "
                     "MACHINE_GRID with the stack's base/step."
                     % (exercise, _q(spec["ask"])))
        lines.append("MACHINE_REGISTER exercise=%s cmd=%s"
                     % (exercise, " ".join(base + ["--new", "<이름>"])))
        lines.append("MACHINE_GRID exercise=%s cmd=%s"
                     % (exercise, " ".join(
                         [os.path.join(HERE, "lattice-set"), exercise,
                          "--machine", "<ulid>", "--type", "stack",
                          "--base", "<kg>", "--step", "<kg>"])))
        lines.append(_photo_line(exercise, base))
        return lines
    if spec["kind"] == "confirm":
        lines.append("MACHINE_ASK exercise=%s kind=confirm last=%s basis=%s "
                     "ask=%s -- ONE confirm button for the remembered machine "
                     "plus %s; never ask them to compare stacks."
                     % (exercise, last[0], last[1], _q(spec["ask"]),
                        OTHER_LABEL))
    else:
        lines.append("MACHINE_ASK exercise=%s kind=pick n=%d ask=%s -- one "
                     "button per machine below plus %s. A new name registers "
                     "it; nothing is ever pre-filled."
                     % (exercise, len(options), _q(spec["ask"]), OTHER_LABEL))
    for u, lab in options:
        lines.append("MACHINE_OPTION exercise=%s machine=%s label=%s cmd=%s"
                     % (exercise, u, _q(lab), " ".join(base + [u])))
    lines.append(_photo_line(exercise, base))
    lines.append("MACHINE_OTHER exercise=%s label=%s cmd=%s"
                 % (exercise, _q(OTHER_LABEL),
                    " ".join(base + ["--new", "<이름>"])))
    return lines


# ---------------------------------------------------------------------------
# the ask, as the owner's keyboard (2026-10-03)
# ---------------------------------------------------------------------------
# On the inline-button rail no model turn runs, so MACHINE_ASK on stdout reached
# nobody (files/session-render.md, step 2). The same question, the same
# wording, the same options, as an idrill arm (bridge IDRILL-ARM-CONTRACT):
# one button per machine (value = its ulid -> machine-pick), plus OTHER_LABEL
# with the bridge's reserved `other` value (free-text prompt; the typed name is
# registered by machine-pick --new). Built here, delivered by set-arm
# machine-ask (the file that owns arm delivery and its once-only ledger).
ASK_DONE_KEY = "health.machine.ask.done"
_ULID_RE = "[0-9A-Z]{26}"


def ask_arm_id(session_id, exercise):
    """Deterministic 8-hex arm id per (session, exercise): a re-entry
    re-arms the same file and the delivery ledger refuses a second push."""
    key = "%s|%s|machine-ask" % (session_id, exercise)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:8]


def _done_text():
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import ui_labels
        return ui_labels.i18n(ASK_DONE_KEY) or "OK"
    except Exception:  # noqa: BLE001
        return "OK"


def ask_arm_payload(spec, session_id, exercise, db_path):
    """The idrill arm for `spec` (ask_spec), or None when there is nothing to
    ask. Single step, fires on the tap: machine-pick <sid> <ex> <ulid>."""
    if not spec or spec.get("session") or not spec.get("options"):
        return None
    rows = [[[lab, u]] for u, lab in spec["options"]]
    rows.append([[OTHER_LABEL, "other"]])
    return {
        "session_id": session_id,
        "exercise_name": exercise,
        "step_buttons": {"1": rows},
        "step_text": {"1": spec["ask"]},
        "step_validate": {"1": "^%s$" % _ULID_RE},
        "step_final": "1",
        "cmd": list(spec["base"]) + ["{1}", "--db",
                                     os.path.abspath(db_path)],
        "confirm_fmt": _done_text(),
    }


# ---------------------------------------------------------------------------
# register + choose
# ---------------------------------------------------------------------------

_CROCKFORD = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"


def _new_ulid():
    """26-char Crockford ULID (48-bit ms time + 80 random bits), the same
    shape kit_life.new_ulid mints."""
    import secrets
    import time
    n = (int(time.time() * 1000) << 80) | secrets.randbits(80)
    out = []
    for _ in range(26):
        out.append(_CROCKFORD[n & 31])
        n >>= 5
    return "".join(reversed(out))


def _owning_agent():
    try:
        sys.path.insert(0, HERE)
        import ax_engine
        return ax_engine.resolve_owning_agent()
    except Exception:  # noqa: BLE001
        return os.environ.get("LIFEKIT_OWNING_AGENT") or "warg"  # estate-scrub:allow(legacy DB slug value, a data contract kept for pre-049 DBs)


def pick(db_path, session_id, exercise, ulid=None, new_label=None, gym=None):
    """-> (kind, ulid): kind SAME|NEW|PICK. Registers `new_label` through the
    kit (find-first on the label), then holds the choice for the session."""
    ta = kit_axis(db_path)
    if ta is None:
        raise RuntimeError("kit 062 verbs are not reachable")
    kind = "PICK"
    c = _conn(db_path)
    try:
        if new_label:
            kind, ulid = ta.machine_register(c, _owning_agent(), _new_ulid,
                                             new_label, gym)
            c.commit()
        elif not c.execute("SELECT 1 FROM ax_machine WHERE ulid=? AND "
                           "status='active'", (ulid,)).fetchone():
            raise ValueError("no active machine %s" % ulid)
    finally:
        c.close()
    record_pick(db_path, session_id, exercise, ulid)
    return kind, ulid


# ---------------------------------------------------------------------------
# the stack, read off a photo (owner live 2026-10-08 07:28)
# ---------------------------------------------------------------------------
# The owner sent a photo of the weight stack (2.5 .. 47.5kg). The agent read
# it ("plates from 2.5kg to 47.5kg") and still asked "which machine" and registered
# nothing, so nothing snapped and no next weight could name a pin. A stack
# photo IS the answer to the machine question: machine-pick --stack registers
# the machine (label derived from the stack when none is given -- the same
# stack at the same gym is the same machine) with the read pins as its STATED
# grid, and holds it for the session.

def stack_points(spec, step=None):
    """'2.5-47.5' (or '2.5-47.5:2.5', '5,10,15') -> sorted pin kg list.
    Step defaults to the lightest plate (a stack is labelled from its first
    plate: 2.5, 5.0, 7.5 ...)."""
    spec = str(spec or "").strip()
    if not spec:
        raise ValueError("empty stack")
    if "," in spec or " " in spec:
        return sorted(set(float(x) for x in spec.replace(",", " ").split()))
    if ":" in spec:
        spec, st = spec.split(":", 1)
        step = float(st)
    lo, hi = (float(x) for x in spec.split("-", 1))
    if hi < lo:
        lo, hi = hi, lo
    step = float(step) if step else lo
    if step <= 0:
        raise ValueError("stack step must be > 0")
    out, k = [], 0
    while lo + k * step <= hi + 1e-9 and k < 400:
        out.append(round(lo + k * step, 4))
        k += 1
    return out


def _fmt(v):
    f = float(v)
    return str(int(f)) if f.is_integer() else ("%.2f" % f).rstrip("0").rstrip(".")


def stack_label(db_path, exercise, points):
    import live_load
    return live_load.stack_label(_is_cable(db_path, exercise), points[0],
                                 points[-1])


def set_plates(db_path, ulid, points):
    """The machine's STATED grid = `points` (kit machine-upd --plates)."""
    ta = kit_axis(db_path)
    if ta is None:
        raise RuntimeError("kit 062 verbs are not reachable")

    class _Refused(Exception):
        pass

    def _err(msg):
        raise _Refused(msg)

    ctx = ta.Ctx(lambda: sqlite3.connect(db_path), _err, _new_ulid,
                 _owning_agent)
    import io
    import contextlib
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            ta.cli_machine_upd(ctx, [ulid, "--plates",
                                     " ".join(_fmt(p) for p in points)])
    except _Refused as e:
        raise RuntimeError(str(e))

