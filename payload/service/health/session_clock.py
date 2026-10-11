#!/usr/bin/env python3
"""session_clock.py -- session minutes and rest, measured from timestamps.

WHY (0.36.0 item 4, live session 1 of 2026-10-08). The close-out asked the
owner how long the session took. The engine already holds the answer: the
session opened at a known moment and every set row carries recorded_at. The
owner is asked for ONE number only -- the watch kcal -- and that number is
recorded on the session row, never used to set a food target.

  minutes   = (last record or close-out) - session open, rounded
  open      = .session-clock/<sid>.json (stamped by session-open), else the
              session's first row
  last      = the latest of: any workout_sets.recorded_at of the session, a
              post-lift block row's ended_at (post_blocks.py)
  rest      = RETROACTIVE: the rest before a set is its record time minus
              the previous set's record time (a set is recorded when it
              ends). The clarifying back-and-forth between two sets is part
              of that gap and counts as rest -- nothing is subtracted.

Times are local wall-clock strings ('YYYY-MM-DD HH:MM:SS'), the shape
set-add writes (datetime('now','localtime')). Never raises to a caller.
stdlib only. ASCII only.
"""

import datetime
import json
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
FMT = "%Y-%m-%d %H:%M:%S"


def state_dir():
    return (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
            or os.path.join(PROJECT_ROOT, "files", "program"))


def _path(session_id, sd=None):
    return os.path.join(sd or state_dir(), ".session-clock",
                        "%d.json" % int(session_id))


def now_local():
    return datetime.datetime.now().strftime(FMT)


def parse(ts):
    if not ts:
        return None
    s = str(ts).strip().replace("T", " ")[:19]
    try:
        return datetime.datetime.strptime(s, FMT)
    except ValueError:
        return None


def stamp_open(session_id, now=None, sd=None):
    """Record the session's open moment once (a resume keeps the first)."""
    path = _path(session_id, sd)
    try:
        if os.path.exists(path):
            return False
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump({"opened_at": now or now_local()}, fh)
        os.replace(tmp, path)
        return True
    except OSError:
        return False


# A close request this long after the last record is a session left open
# (closed the next morning), not training time: the last record stands.
CLOSE_GAP_MAX_MIN = 90


def stamp_close_request(session_id, now=None, sd=None):
    """Record the FIRST close-out request (owner 2026-10-10: "go home" at 14:07;
    the kcal ask and the photo came later). The session ran until the owner
    ended it, not until its last recorded set (22 min vs ~100 min, only the
    deadlift was recorded). A retry keeps the first stamp."""
    path = _path(session_id, sd)
    try:
        data = {}
        if os.path.exists(path):
            with open(path) as fh:
                data = json.load(fh) or {}
        if data.get("close_requested_at"):
            return False
        data["close_requested_at"] = now or now_local()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w") as fh:
            json.dump(data, fh)
        os.replace(tmp, path)
        return True
    except (OSError, ValueError, AttributeError):
        return False


def close_requested_at(session_id, sd=None):
    try:
        with open(_path(session_id, sd)) as fh:
            return parse((json.load(fh) or {}).get("close_requested_at"))
    except (OSError, ValueError, AttributeError):
        return None


def _stamped_open(session_id, sd=None):
    try:
        with open(_path(session_id, sd)) as fh:
            return (json.load(fh) or {}).get("opened_at")
    except (OSError, ValueError, AttributeError):
        return None


def _rows(db_path, session_id):
    """[(exercise, set_seq, recorded_at)] in record order."""
    try:
        conn = sqlite3.connect("file:%s?mode=ro" % os.path.abspath(db_path),
                               uri=True, timeout=5)
        try:
            return conn.execute(
                "SELECT exercise_name, set_seq, recorded_at FROM workout_sets "
                "WHERE session_id = ? AND recorded_at IS NOT NULL "
                "ORDER BY recorded_at, rowid", (int(session_id),)).fetchall()
        finally:
            conn.close()
    except Exception:  # noqa: BLE001 -- no table / no column -> no rows
        return []


def opened_at(db_path, session_id, sd=None):
    t = parse(_stamped_open(session_id, sd))
    if t is not None:
        return t
    rows = _rows(db_path, session_id)
    return parse(rows[0][2]) if rows else None


def last_record_at(db_path, session_id, extra=(), sd=None):
    """The latest record of the session: set rows plus `extra` timestamps
    (the post-lift block rows' ended_at)."""
    cands = [parse(r[2]) for r in _rows(db_path, session_id)]
    cands += [parse(x) for x in (extra or ())]
    cands = [c for c in cands if c is not None]
    return max(cands) if cands else None


def session_minutes(db_path, session_id, extra=(), now=None, sd=None):
    """(minutes, opened, ended) or (None, opened, ended) when the open is
    unknown. `ended` = the later of the last record and the owner's first
    close-out request (open -> close); with neither, the close-out moment
    (`now`)."""
    opened = opened_at(db_path, session_id, sd)
    ended = last_record_at(db_path, session_id, extra, sd)
    closed = close_requested_at(session_id, sd)
    if closed is not None and (
            ended is None
            or ended < closed <= ended + datetime.timedelta(
                minutes=CLOSE_GAP_MAX_MIN)):
        ended = closed
    if ended is None:
        ended = parse(now) if now else datetime.datetime.now()
    if opened is None or ended < opened:
        return None, opened, ended
    return int(round((ended - opened).total_seconds() / 60.0)), opened, ended


def rest_before(db_path, session_id, exercise_name, set_seq):
    """Seconds of rest before (exercise, set_seq), measured retroactively:
    its record time minus the PREVIOUS row's record time in the session (the
    previous set ended when it was recorded). None for the session's first
    row or an unknown time."""
    rows = _rows(db_path, session_id)
    prev = None
    for ex, seq, ts in rows:
        if ex == exercise_name and int(seq) == int(set_seq):
            t, p = parse(ts), parse(prev)
            if t is None or p is None:
                return None
            return max(0, int((t - p).total_seconds()))
        prev = ts
    return None
