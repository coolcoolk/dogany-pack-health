"""Today's regular split, picked by the owner (live failure 2026-10-12 05:54).

The owner, at the gym: Saturday's legs were a FREE session (deadlift only),
so the queue still said the lower split was next, and they wanted upper body.
The agent offered [free upper session | change the order], the owner picked
the order change, and no tool could run it: `session-open --subtype` only
relabelled the row while the queue day's lifts loaded. Two defects -- an
offered option with no executable path, and no way to run another regular
split today.

This module is the ONE answer to "which regular split may run today, and
which one should":
  * state()    -- queue day + open splits of the KIT's pass (rotation-current
                  next_split / pass_remaining; never re-derived here);
  * refusal()  -- any split of the program's cycle is choosable; only an
                  unknown code is refused (a plain token);
  * build()    -- the choice block: recent free-session load (72 h) on a
                  split's primary regions, the suggested split that avoids
                  it, and the fork the agent may offer (every entry has a
                  runnable path: `session-open --split <code>` or
                  `session-open --free`).

Past rows are never rewritten: a free session stays a free session; it is
shown as recent load and steers the suggestion, nothing more.
Copy lives in i18n/<lang>.json (health.split_choice.*); this file is ASCII.
"""
import datetime
import os
import sqlite3

# Muscle -> body region. Mirrors program-plan MUSCLE_REGION (+ abs -> core),
# the vocabulary of exercise_muscle.muscle.
REGION_OF = {
    "chest": "chest", "back": "back", "shoulders": "shoulders",
    "quads": "legs", "glutes": "legs", "hamstrings": "legs",
    "adductors": "legs", "calves": "calves", "biceps": "arms",
    "triceps": "arms", "forearms": "arms", "abs": "core",
}
REGION_ORDER = ("legs", "back", "chest", "shoulders", "arms", "calves", "core")
# 72 h, as calendar days back from today (Saturday counts on Monday).
CREDIT_DAYS = 3
# A region is one of a split's PRIMARY regions when at least this share of the
# split's mapped slots carries a primary muscle there (a lone calf raise on a
# leg day, or one lateral raise among six upper lifts, still counts at 1/6).
PRIMARY_SHARE = 0.15
from free_session import CODE as FREE_CODE   # session_type.code token
REFUSE_UNKNOWN = "SPLIT_UNKNOWN"
REFUSE_LIVE = "SPLIT_LIVE"


def _labels():
    import ui_labels
    return ui_labels


def _copy(key, **kw):
    return _labels().i18n("health.split_choice." + key, "ko", **kw)


def region_ko(region):
    return _copy("region." + region) or region


def lift_ko(name):
    try:
        found = _labels().exercise_ko(name)
    except Exception:  # noqa: BLE001 -- a label miss never blocks the choice
        found = None
    if found and found != _labels().i18n("health.split_choice.lift_unknown",
                                         "ko"):
        return found
    return name


def _regions_of(names, muscle_map):
    out = set()
    for name in names:
        for muscle, role in muscle_map.get(name, ()):
            if role == "primary":
                out.add(REGION_OF.get(muscle, muscle))
    return out


def _ordered(regions):
    return [r for r in REGION_ORDER if r in regions] + sorted(
        r for r in regions if r not in REGION_ORDER)


def split_regions(program, code, muscle_map):
    """The split's PRIMARY regions (see PRIMARY_SHARE)."""
    day = ((program.get("days") or {}).get(code) or {})
    slots = [ex.get("name") for ex in (day.get("exercises") or [])
             if isinstance(ex, dict) and ex.get("name")]
    per_slot = [_regions_of([n], muscle_map) for n in slots]
    per_slot = [r for r in per_slot if r]
    if not per_slot:
        return set()
    counts = {}
    for regs in per_slot:
        for r in regs:
            counts[r] = counts.get(r, 0) + 1
    return {r for r, n in counts.items()
            if float(n) / len(per_slot) >= PRIMARY_SHARE}


def state(rx, program, db_path, today, exclude_session_id=None):
    """Queue day + the splits still open in the kit's current pass, ALL read
    from the kit (rx.kit_rotation = `kit_life.sh rotation-current`): the
    queue day is the kit's next_split (the cycle successor of the latest split
    done), `remaining` the whole cycle from it. The pack holds no rotation
    rule of its own."""
    rotation = list(program.get("rotation") or [])
    kit = rx.kit_rotation(db_path, today, exclude_session_id)
    queue_day = kit["next_split"] if kit["next_split"] in rotation else None
    week = rx.week_regular_status(program, db_path, today,
                                  exclude_session_id=exclude_session_id)
    remaining = [c for c in kit["pass_remaining"] if c in rotation]
    return {"rotation": rotation, "queue_day": queue_day,
            "provisional": queue_day is None,
            "done": list(week.get("done_codes") or []),
            "week_sessions": week.get("week_sessions", 0),
            "remaining": remaining}


def refusal(code, st, program):
    """None when `code` may run as today's regular split, else a token. Every
    split of the cycle is choosable (the owner may defer the next one; the
    cycle continues after what was done); only an unknown code is refused."""
    days = program.get("days") or {}
    if code not in st["rotation"] or code not in days:
        return REFUSE_UNKNOWN
    return None


def refusal_line(token, code, st):
    return ("SPLIT_REFUSED %s split=%s remaining=%s -- run only a remaining "
            "split (session-open --split <code>) or a free session "
            "(session-open --free); never offer the refused one"
            % (token, code, ",".join(st["remaining"]) or "none"))


def recent_free_load(db_path, today, muscle_map, exclude_session_id=None):
    """Free sessions in the last CREDIT_DAYS days that logged working sets:
    [{session_id, date, regions, lifts}], newest first. Read-only."""
    d0 = (datetime.date.fromisoformat(today)
          - datetime.timedelta(days=CREDIT_DAYS)).isoformat()
    try:
        cx = sqlite3.connect("file:%s?mode=ro" % os.path.abspath(db_path),
                             uri=True)
    except sqlite3.Error:
        return []
    try:
        rows = cx.execute(
            "SELECT w.id, w.date, ws.exercise_name FROM workouts w "
            "JOIN session_type st ON st.id = w.session_type_id "
            "JOIN workout_sets ws ON ws.session_id = w.id "
            "WHERE st.code = ? AND w.date >= ? AND w.date <= ? "
            "AND COALESCE(ws.set_kind, 'working') IN ('working', 'hold') "
            "AND w.id != ? "
            "ORDER BY w.date DESC, w.id DESC, ws.id",
            (FREE_CODE, d0, today,
             -1 if exclude_session_id is None else exclude_session_id)
        ).fetchall()
    except sqlite3.Error:
        rows = []
    finally:
        cx.close()
    out, by_id = [], {}
    for sid, date, name in rows:
        if sid not in by_id:
            by_id[sid] = {"session_id": sid, "date": date, "lifts": []}
            out.append(by_id[sid])
        if name not in by_id[sid]["lifts"]:
            by_id[sid]["lifts"].append(name)
    for entry in out:
        entry["regions"] = _ordered(_regions_of(entry["lifts"], muscle_map))
    return [e for e in out if e["regions"]]


def _has_batchim(word):
    ch = (word or " ")[-1]
    o = ord(ch) - 0xAC00
    return 0 <= o < 11172 and o % 28 != 0


def credit_line(entry, today, muscle_map):
    """One line: '<weekday> free session did <region>(<lift>)'."""
    labels = _labels()
    d = datetime.date.fromisoformat(entry["date"])
    if entry["date"] == today:
        when = _copy("today")
    else:
        when = labels.WEEKDAY_FULL_KO[labels.WEEKDAY_ORDER[d.weekday()]]
    parts, last = [], ""
    for region in entry["regions"]:
        lifts = [lift_ko(n) for n in entry["lifts"]
                 if region in _regions_of([n], muscle_map)]
        last = region_ko(region)
        parts.append("%s(%s)" % (last, ", ".join(lifts)) if lifts else last)
    key = "recent_free_batchim" if _has_batchim(last) else "recent_free"
    return _copy(key, when=when, what=" \u00b7 ".join(parts))


def build(rx, program, db_path, today, exclude_session_id=None,
          muscle_map=None):
    """The choice block (rx-calc `split_choice`, session-open --dry-run)."""
    st = state(rx, program, db_path, today, exclude_session_id)
    mm = muscle_map if muscle_map is not None else rx.get_muscle_map(db_path)
    recent = recent_free_load(db_path, today, mm, exclude_session_id)
    loaded = set()
    for entry in recent:
        loaded.update(entry["regions"])
    regions = {c: split_regions(program, c, mm) for c in st["rotation"]}
    order = st["remaining"]   # cycle order from the queue day
    clear = [c for c in order if not (regions.get(c, set()) & loaded)]
    suggested = clear[0] if clear else (order[0] if order else None)
    # A different body part than the queue day, still clear of recent load.
    others = [c for c in order if c != st["queue_day"]]
    qreg = regions.get(st["queue_day"], set())
    swap = next((c for c in others
                 if not (regions.get(c, set()) & (loaded | qreg))), None)
    swap = swap or next((c for c in others if c in clear), None)
    swap = swap or (others[0] if others else None)
    fork = ([_copy("fork_regular", split=swap, queue=st["queue_day"])] if swap else []) + [
        _copy("fork_free")]
    return {
        "queue_day": st["queue_day"],
        "done": st["done"],
        "remaining": st["remaining"],
        "split_regions": {c: _ordered(r) for c, r in regions.items()},
        "recent_load": [dict(e, line=credit_line(e, today, mm))
                        for e in recent],
        "recent_regions": _ordered(loaded),
        "suggested": suggested,
        "swap": swap,
        "fork": fork,
        "fork_paths": ((["session-open --split %s" % swap] if swap else [])
                       + ["session-open --free"]),
    }


def emit_lines(block):
    """session-open --dry-run surface: machine line + say lines + fork."""
    out = ["SPLIT_CHOICE queue=%s remaining=%s suggested=%s swap=%s "
           "recent_regions=%s" % (
               block["queue_day"] or "NONE",
               ",".join(block["remaining"]) or "none",
               block["suggested"] or "NONE", block["swap"] or "NONE",
               ",".join(block["recent_regions"]) or "none")]
    for entry in block["recent_load"]:
        out.append("RECENT_LOAD %s" % entry["line"])
    out.append("SPLIT_FORK [[OPTIONS: %s]]" % " | ".join(block["fork"]))
    return out
