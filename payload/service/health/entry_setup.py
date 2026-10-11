# -*- coding: utf-8 -*-
"""entry_setup.py -- what the owner needs to know BEFORE the first rep, from
data: which implement (one question, the lift's real variants) and how to set
it up (attachment, grip, orientation).

WHY (owner live 2026-10-08 session 1, pack 0.35.1):
  * curl was entered as "dumbbell, cable or bar?" and the bar type was never
    asked -- owner: "ask barbell or EZ bar from the start". The variants are in the
    taxonomy (exercise_movement_grip: bicep_curl/barbell, ez_bar_curl,
    dumbbell_curl, cable_curl); the entry now lists them as ONE question
    before any weight is named, and the pick re-keys the estimate and the grid.
  * "which grip?" on close-grip pulldown, then a photo of the handle and
    "which way does it go?" answered "hard to say". The entry cue now
    states attachment + grip + orientation (entry_setup.json), concretely.

State: the session's pick (.implement-pick/<sid>.json) and the last pick per
lift (.implement-last.json), both under STATE_DIR. Data: entry_setup.json.
"""
import json
import os
import sqlite3
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
             or os.path.join(HERE, "..", "..", "files", "program"))
DATA_PATH = os.path.join(HERE, "entry_setup.json")
PICK_DIR = os.path.join(STATE_DIR, ".implement-pick")
LAST_PATH = os.path.join(STATE_DIR, ".implement-last.json")
VARIANT_CMD = os.path.join(HERE, "exercise-variant")

_DATA = None


def data():
    global _DATA
    if _DATA is None:
        with open(DATA_PATH, encoding="utf-8") as fh:
            _DATA = json.load(fh)
    return _DATA


def _conn(db_path):
    try:
        sys.path.insert(0, HERE)
        try:
            from db_pool import connect
        finally:
            sys.path.remove(HERE)
        return connect(db_path)
    except Exception:  # noqa: BLE001
        return sqlite3.connect(db_path)


def _ko(name):
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import ui_labels
        return ui_labels.exercise_ko(name)
    except Exception:  # noqa: BLE001
        return name


def movement_row(db_path, exercise_name):
    """(movement, equipment, grip) or (None, None, None)."""
    try:
        c = _conn(db_path)
        try:
            row = c.execute(
                "SELECT movement, equipment, grip FROM exercise_movement_grip "
                "WHERE exercise_name = ?", (exercise_name,)).fetchone()
        finally:
            c.close()
        return tuple(row) if row else (None, None, None)
    except sqlite3.Error:
        return None, None, None


def _tokens(name):
    return set(str(name or "").split("_"))


def _has_token(name, tokens):
    toks = _tokens(name)
    joined = "_%s_" % name
    for t in tokens:
        if t in toks or ("_%s_" % t) in joined:
            return True
    return False


def variants(db_path, exercise_name):
    """[(variant_exercise, equipment, label)] when this lift's implement is
    open at entry (open movement, a name that names no implement, >= 2
    implements in the taxonomy); else []."""
    cfg = data()["variants"]
    mv, eq, grip = movement_row(db_path, exercise_name)
    if mv is None or mv not in cfg["open_movements"]:
        return []
    if _has_token(exercise_name, cfg["equipment_tokens"]):
        return []
    try:
        c = _conn(db_path)
        try:
            rows = c.execute(
                "SELECT exercise_name, equipment FROM exercise_movement_grip "
                "WHERE movement = ? AND grip IS ?", (mv, grip)).fetchall()
        finally:
            c.close()
    except sqlite3.Error:
        return []
    best = {}
    for name, equip in rows:
        if not equip or equip in ("bodyweight", "bodyweight_assist"):
            continue
        if name != exercise_name and _has_token(name, cfg["exclude_tokens"]):
            continue
        cur = best.get(equip)
        if (cur is None or name == exercise_name
                or (cur != exercise_name and len(name) < len(cur))):
            best[equip] = name
    if len(best) < 2:
        return []
    order = cfg["equipment_order"]
    labels = cfg["equipment_labels"]
    keys = sorted(best, key=lambda e: (order.index(e) if e in order
                                       else len(order), e))
    return [(best[e], e, labels.get(e, e)) for e in keys]


def _pick_path(session_id):
    return os.path.join(PICK_DIR, "%s.json" % int(session_id))


def _read(path):
    try:
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        return d if isinstance(d, dict) else {}
    except (OSError, ValueError):
        return {}


def _write(path, d):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, sort_keys=True)
    os.replace(tmp, path)


def picked(session_id, exercise_name):
    """The variant the owner picked for this lift THIS session, or None."""
    if session_id is None:
        return None
    return _read(_pick_path(session_id)).get(exercise_name)


def remembered(exercise_name):
    return _read(LAST_PATH).get(exercise_name)


def record_pick(session_id, exercise_name, variant):
    d = _read(_pick_path(session_id))
    d[exercise_name] = variant
    _write(_pick_path(session_id), d)
    last = _read(LAST_PATH)
    last[exercise_name] = variant
    _write(LAST_PATH, last)


def effective(session_id, exercise_name):
    """The exercise the owner is actually doing for this slot (the picked
    variant, else the slot itself)."""
    return picked(session_id, exercise_name) or exercise_name


def _t(key, **kw):
    """Owner copy from the i18n bundle (code stays ASCII; ui_labels.i18n)."""
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import ui_labels
        return ui_labels.i18n(key, **kw)
    except Exception:  # noqa: BLE001
        return ""


def _q(text):
    return '"%s"' % str(text).replace('"', "'")


def variant_lines(db_path, session_id, exercise_name, display=None):
    """VARIANT_* lines for the entry. ask_pending=True when the owner still
    has to answer (the caller then names no weight yet)."""
    opts = variants(db_path, exercise_name)
    if not opts:
        return [], False
    disp = display or _ko(exercise_name)
    pick = picked(session_id, exercise_name)
    if pick:
        lab = next((o[2] for o in opts if o[0] == pick), pick)
        return (["VARIANT_SESSION exercise=%s variant=%s label=%s"
                 % (exercise_name, pick, _q(lab))], False)
    last = remembered(exercise_name)
    if last and any(o[0] == last for o in opts):
        opts = ([o for o in opts if o[0] == last]
                + [o for o in opts if o[0] != last])
    labels = " / ".join(o[2] for o in opts)
    if last and opts[0][0] == last:
        ask = _t("health.setup.variant.confirm", last=opts[0][2],
                 labels=labels)
        kind = "confirm"
    else:
        ask = _t("health.setup.variant.pick", name=disp, labels=labels)
        kind = "pick"
    lines = ["VARIANT_ASK exercise=%s kind=%s n=%d -- ONE question, before "
             "any weight; relay VARIANT_SAY with one button per option"
             % (exercise_name, kind, len(opts))]
    for v, e, lab in opts:
        lines.append("VARIANT_OPTION exercise=%s variant=%s equipment=%s "
                     "label=%s cmd=%s %s %s %s"
                     % (exercise_name, v, e, _q(lab), VARIANT_CMD,
                        session_id, exercise_name, v))
    lines.append("VARIANT_SAY: %s" % ask)
    lines.append("[[OPTIONS: %s]]" % " | ".join(o[2] for o in opts))
    return lines, True


def setup_spec(db_path, exercise_name):
    """dict(attachment, grip, orient) for a lift (data first, the taxonomy
    grip as fallback), or {}."""
    spec = dict((data().get("setup") or {}).get(exercise_name) or {})
    if not spec.get("grip"):
        _mv, _eq, grip = movement_row(db_path, exercise_name)
        fb = (data().get("grip_fallback") or {}).get(grip or "")
        if fb:
            spec["grip"] = fb
    return spec


def setup_lines(db_path, exercise_name, display=None):
    spec = setup_spec(db_path, exercise_name)
    if not spec:
        return []
    disp = display or _ko(exercise_name)
    parts = []
    if spec.get("attachment"):
        parts.append(_t("health.setup.attach",
                        attachment=spec["attachment"]))
    if spec.get("grip"):
        parts.append(spec["grip"])
    say = (_t("health.setup.say", name=disp, body=", ".join(parts))
           if parts else "")
    if spec.get("orient"):
        say = (_t("health.setup.and_orient", say=say, orient=spec["orient"])
               if say else _t("health.setup.say_orient", name=disp,
                              orient=spec["orient"]))
    return ["SETUP_CUE exercise=%s attachment=%s grip=%s orient=%s"
            % (exercise_name, _q(spec.get("attachment") or "-"),
               _q(spec.get("grip") or "-"),
               "yes" if spec.get("orient") else "no"),
            "SETUP_SAY: %s" % say]


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S")
