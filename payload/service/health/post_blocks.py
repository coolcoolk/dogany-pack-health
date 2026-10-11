#!/usr/bin/env python3
"""post_blocks.py -- the post-lift blocks, run by the tool in program order.

WHY (0.36.0 item 2, live session 1 of 2026-10-08). After the last lift the
agent offered "finisher or cardio?" as an either/or, then wrote the cooldown
as prose (a "do a few stretches and wrap up" line), and the close-out ran with
neither block recorded. The program already says what follows the lifts --
program-plan's session text is "... finisher -> cardio -> cooldown" -- so
the blocks are the PROGRAM's, not a menu:

  source   .program-plan.json beside program.yaml (the consult's state):
             practice_blocks.<code>.finisher | .circuit   (one end block)
             cardio {pick, display, minutes}               (pick != none)
             cooldown.<code> [drill key, ...]
           a cooldown drill's hold comes from prep.yaml days.<code>.cooldown
           (rx-calc cooldown_day_items: hold_sec) else the movement
           catalog's dose ("<per side> 20<sec>").
  order    finisher/circuit -> cardio -> cooldown. One block at a time,
           never offered as a choice.
  state    <state>/.post-blocks/<sid>.json -- per block pending | active |
           done | skipped, per cooldown row the same plus started_at /
           ended_at. NOT a runtime marker: close-out does not sweep it, the
           card reads it, and "let's stretch" after close-out reopens it.
  gate     open_keys() -> every block not done and not explicitly skipped.
           session-closeout refuses while any is open.

Copy lives in the i18n bundles (health.post.*). stdlib only. ASCII only.
"""

import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

ORDER = ("finisher", "circuit", "cardio", "cooldown")
ST_PENDING, ST_ACTIVE, ST_DONE, ST_SKIPPED = ("pending", "active", "done",
                                              "skipped")
FINAL = (ST_DONE, ST_SKIPPED)
FMT = "%Y-%m-%d %H:%M:%S"
# "per side" / "sec" words of a catalog dose, spelled as escapes (ASCII code)
_PER_SIDE = "\uc88c\uc6b0"
_SEC_RE = re.compile("(\\d+)\\s*\ucd08")
DEFAULT_HOLD_SEC = 30


def state_dir():
    return (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
            or os.path.join(PROJECT_ROOT, "files", "program"))


def data_dir():
    return (os.environ.get("WARG_DATA_DIR")
            or os.path.join(PROJECT_ROOT, "files", "program"))


def now_local():
    return datetime.datetime.now().strftime(FMT)


def t(key, **kw):
    try:
        import ui_labels
        return ui_labels.i18n(key, **kw)
    except Exception:  # noqa: BLE001 -- copy missing never breaks the run
        return ""


# ---------------------------------------------------------------------------
# the plan
# ---------------------------------------------------------------------------
def plan_state(program_path=None):
    base = (os.path.dirname(os.path.abspath(program_path)) if program_path
            else data_dir())
    try:
        with open(os.path.join(base, ".program-plan.json"),
                  encoding="utf-8") as fh:
            got = json.load(fh)
        return got if isinstance(got, dict) else {}
    except (OSError, ValueError):
        return {}


def _prep_cooldown(program_path, code):
    """{drill code: prep.yaml cooldown item} for the day, {} on any miss."""
    try:
        import importlib.machinery
        import importlib.util
        path = os.path.join(HERE, "rx-calc")
        loader = importlib.machinery.SourceFileLoader("_post_rx", path)
        spec = importlib.util.spec_from_loader("_post_rx", loader)
        rx = importlib.util.module_from_spec(spec)
        loader.exec_module(rx)
        prep = rx.load_prep(program_path
                            or os.path.join(data_dir(), "program.yaml"))
        return {d.get("code"): d for d in rx.cooldown_day_items(prep, code)
                if d.get("code")}
    except Exception:  # noqa: BLE001 -- the catalog dose stands
        return {}


def _catalog(key):
    try:
        import movement_catalog as MC
        return MC.MOVEMENTS.get(key) or {}
    except Exception:  # noqa: BLE001
        return {}


def _display(key):
    m = _catalog(key)
    if m.get("ko"):
        return m["ko"]
    try:
        import ui_labels
        return ui_labels.plan_drill_ko(key)
    except Exception:  # noqa: BLE001
        return key


def cooldown_rows(keys, program_path, code):
    prep = _prep_cooldown(program_path, code)
    rows = []
    for k in keys or ():
        item = prep.get(k) or {}
        dose = str(_catalog(k).get("dose") or "")
        sec = item.get("hold_sec")
        if not sec:
            m = _SEC_RE.search(dose)
            sec = int(m.group(1)) if m else DEFAULT_HOLD_SEC
        rows.append({"code": k,
                     "display": item.get("display") or _display(k),
                     "sec": int(sec),
                     "per_side": _PER_SIDE in dose
                     or item.get("target_unit") == "per_side",
                     "status": ST_PENDING,
                     **{key: item[key] for key in ("steps", "fault")
                        if item.get(key)}})
    return rows


def plan(program_path, code):
    """The session's post-lift blocks in program order: [{key, ...}]."""
    st = plan_state(program_path)
    try:
        from free_session import CODE as FREE_CODE
    except Exception:  # noqa: BLE001
        FREE_CODE = None
    # a session outside the program's rotation (a one-off) has no post-lift
    # blocks: the program's cardio / cooldown are its days'
    rot = (st.get("structure") or {}).get("rotation")
    if rot and code not in rot and code != FREE_CODE:
        return []
    if code == FREE_CODE:
        # owner 2026-10-10: a free session gets the cooldown stretch a planned
        # session gets -- the free day's composed cooldown (free_session
        # prep_day, read through rx-calc load_prep like any prep.yaml day).
        # No finisher / cardio: those are the program's.
        rows = cooldown_rows(list(_prep_cooldown(program_path, code)),
                             program_path, code)
        return ([{"key": "cooldown", "name": t("health.post.cooldown_name")
                  or "cooldown", "rows": rows, "status": ST_PENDING}]
                if rows else [])
    pb = ((st.get("practice_blocks") or {}).get(code) or {})
    out = []
    fin = pb.get("finisher") or {}
    if fin.get("key") and fin.get("minutes"):
        out.append({"key": "finisher", "name": fin.get("display")
                    or _display(fin["key"]), "minutes": fin["minutes"],
                    "work_sec": fin.get("work_sec"),
                    "rest_sec": fin.get("rest_sec"),
                    "rounds": fin.get("rounds")})
    circ = pb.get("circuit") or {}
    if circ.get("keys") and circ.get("minutes"):
        out.append({"key": "circuit", "name": " -> ".join(
            circ.get("display") or circ["keys"]),
            "minutes": circ["minutes"], "work_sec": circ.get("work_sec"),
            "rest_sec": circ.get("rest_sec") or 0,
            "rounds": circ.get("rounds")})
    cardio = st.get("cardio") or {}
    if cardio.get("pick") and cardio.get("pick") != "none" \
            and (cardio.get("minutes") or 0) > 0:
        out.append({"key": "cardio", "name": cardio.get("display")
                    or cardio["pick"], "pick": cardio["pick"],
                    "minutes": cardio["minutes"]})
    keys = (st.get("cooldown") or {}).get(code) or []
    rows = cooldown_rows(keys, program_path, code)
    if rows:
        out.append({"key": "cooldown", "name": t("health.post.cooldown_name")
                    or "cooldown", "rows": rows})
    for b in out:
        b["status"] = ST_PENDING
    return out


# ---------------------------------------------------------------------------
# state
# ---------------------------------------------------------------------------
def _path(session_id, sd=None):
    return os.path.join(sd or state_dir(), ".post-blocks",
                        "%d.json" % int(session_id))


def read(session_id, sd=None):
    try:
        with open(_path(session_id, sd), encoding="utf-8") as fh:
            got = json.load(fh)
        return got if isinstance(got, dict) else None
    except (OSError, ValueError):
        return None


def write(state, sd=None):
    path = _path(state["session_id"], sd)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def ensure(session_id, code, program_path, sd=None):
    """The session's post-block state, created from the plan on first use."""
    st = read(session_id, sd)
    if st is not None:
        return st
    st = {"session_id": int(session_id), "code": code,
          "created_at": now_local(), "blocks": plan(program_path, code)}
    if st["blocks"]:
        write(st, sd)
    return st


def block(st, key):
    return next((b for b in (st or {}).get("blocks") or ()
                 if b.get("key") == key), None)


def open_keys(st):
    return [b["key"] for b in (st or {}).get("blocks") or ()
            if b.get("status") not in FINAL]


def current(st):
    """(block, row index or None) of the next thing to run, or (None, None)."""
    for b in (st or {}).get("blocks") or ():
        if b.get("status") in FINAL:
            continue
        if b["key"] == "cooldown":
            for i, r in enumerate(b.get("rows") or ()):
                if r.get("status") not in FINAL:
                    return b, i
            return b, None
        return b, None
    return None, None


def ended_stamps(st):
    """Every ended_at of the session's post-block work (session_clock)."""
    out = []
    for b in (st or {}).get("blocks") or ():
        if b.get("ended_at"):
            out.append(b["ended_at"])
        for r in b.get("rows") or ():
            if r.get("ended_at"):
                out.append(r["ended_at"])
    return out


def _settle_block(b):
    """A cooldown whose rows are all final is final itself (done if any row
    was done, else skipped)."""
    rows = b.get("rows") or []
    if b["key"] == "cooldown" and rows and all(
            r.get("status") in FINAL for r in rows):
        b["status"] = (ST_DONE if any(r.get("status") == ST_DONE
                                      for r in rows) else ST_SKIPPED)
        b["ended_at"] = b.get("ended_at") or now_local()


def mark(st, key, status, row=None, now=None):
    """Move block `key` (or its cooldown row) to `status`. Returns the moved
    object, or None when it does not exist."""
    b = block(st, key)
    if b is None:
        return None
    now = now or now_local()
    target = b
    if row is not None:
        rows = b.get("rows") or []
        if not 0 <= row < len(rows):
            return None
        target = rows[row]
    target["status"] = status
    if status == ST_ACTIVE:
        target["started_at"] = now
        if target is not b:
            b["status"] = ST_ACTIVE
            b.setdefault("started_at", now)
    elif status in FINAL:
        target["ended_at"] = now
        if target is not b:
            _settle_block(b)
    return target


def reopen_cooldown(st, now=None):
    """'let's stretch' after close-out: the session's cooldown block runs
    again (its rows back to pending; the earlier run kept under `runs`)."""
    b = block(st, "cooldown")
    if b is None:
        return None
    b.setdefault("runs", []).append({
        "status": b.get("status"), "ended_at": b.get("ended_at"),
        "rows": [dict(r) for r in b.get("rows") or ()]})
    for r in b.get("rows") or ():
        for k in ("started_at", "ended_at"):
            r.pop(k, None)
        r["status"] = ST_PENDING
    b["status"] = ST_PENDING
    b.pop("ended_at", None)
    b["reopened_at"] = now or now_local()
    return b


# ---------------------------------------------------------------------------
# words
# ---------------------------------------------------------------------------
def row_dose(r):
    key = "health.post.dose_side" if r.get("per_side") else "health.post.dose"
    return t(key, sec=r.get("sec"))


def row_seconds(r):
    return int(r.get("sec") or 0) * (2 if r.get("per_side") else 1)


def block_seconds(b):
    if b["key"] in ("finisher", "circuit"):
        rounds = int(b.get("rounds") or 0)
        per = int(b.get("work_sec") or 0) + int(b.get("rest_sec") or 0)
        if rounds and per:
            return rounds * per
    return int(b.get("minutes") or 0) * 60


def block_say(b):
    if b["key"] in ("finisher", "circuit"):
        return t("health.post.say.%s" % b["key"], name=b["name"],
                 work=b.get("work_sec"), rest=b.get("rest_sec"),
                 rounds=b.get("rounds"), minutes=b.get("minutes"))
    if b["key"] == "cardio":
        return t("health.post.say.cardio", name=b["name"],
                 minutes=b.get("minutes"))
    rows = b.get("rows") or []
    return t("health.post.say.cooldown", n=len(rows),
             names=", ".join(r["display"] for r in rows))


def row_say(b, i):
    r = b["rows"][i]
    return t("health.post.say.row", i=i + 1, n=len(b["rows"]),
             name=r["display"], dose=row_dose(r))


def card_rows(st, marks):
    """[(marker, name, value)] for the close-out card, one per block.
    marks = (done, current, pending) -- the card's own [v] / [>] / [ ]."""
    done_m, cur_m, pend_m = marks
    out = []
    for b in (st or {}).get("blocks") or ():
        name = (t("health.post.card.%s" % b["key"], name=b.get("name"))
                or b.get("name"))
        rows = b.get("rows") or []
        if b["key"] == "cooldown" and rows:
            n = sum(1 for r in rows if r.get("status") == ST_DONE)
            value = t("health.post.card.rows", n=n, total=len(rows))
            if b.get("status") == ST_DONE and n >= len(rows):
                out.append((done_m, name, value))
            elif n:
                out.append((cur_m, name, value))
            else:
                out.append((pend_m, name, t("health.post.card.skipped")
                            if b.get("status") == ST_SKIPPED else ""))
            continue
        if b.get("status") == ST_DONE:
            out.append((done_m, name, t("health.post.card.minutes",
                                        minutes=b.get("minutes"))))
        elif b.get("status") == ST_SKIPPED:
            out.append((pend_m, name, t("health.post.card.skipped")))
        elif b.get("status") == ST_ACTIVE:
            out.append((cur_m, name, ""))
        else:
            out.append((pend_m, name, ""))
    return out
