"""cue.py -- the ONE owner of how a lift's instructions reach a set card.

Cadence (owner 2026-10-12 07:52, the 08-28 design): the FULL cue is shown once
per lift per session, then ONE tip per set, rotating through the cue's parts
(steps in order, then the fault warning) with no repeat while another part
remains. A session that resumes (a new process, the same session id) does not
repeat the full cue: the ledger is on disk, keyed by (date, session id).

The wording stays in movement_cues.json / prep_cues.json (data); this module
only decides WHICH part is shown WHEN. It posts nothing.

Idempotent per set: asking again for the same (session, lift, set_seq) returns
the same answer and does not advance the rotation, so a re-arm of one set (an
owner correction, a stale-tap refresh) never burns a tip.
"""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
             or os.path.join(HERE, "..", "..", "files", "program"))

FULL = "full"
TIP = "tip"
NONE = "none"


def _dir():
    base = os.environ.get("LIFEKIT_HEALTH_STATE_DIR") or STATE_DIR
    return os.path.join(base, ".cue-shown")


def today_kst():
    import datetime
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).date().isoformat()


def _path(session_id, day=None):
    """The ledger is keyed by (date, session id): a session id the kit reuses on
    another day (a restored DB, a re-minted id) must show its full cue again."""
    return os.path.join(_dir(), "%s.%s.json" % (day or today_kst(), re.sub(
        r"[^A-Za-z0-9_.-]", "_", str(session_id))))


def _read(session_id, day=None):
    try:
        with open(_path(session_id, day), encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def _write(session_id, data, day=None):
    try:
        os.makedirs(_dir(), exist_ok=True)
        tmp = _path(session_id, day) + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False)
        os.rename(tmp, _path(session_id, day))
    except OSError:
        pass            # a lost ledger degrades to a repeated cue, never a crash


def parts(code, lang="ko", recorded=None):
    """The cue as an ordered list of tip-sized parts: each step, then the fault."""
    import movement_cues
    data = movement_cues.cue(code, lang)
    for key in ("steps", "fault"):
        if (recorded or {}).get(key):
            data[key] = recorded[key]
    steps = data.get("steps") or []
    if isinstance(steps, str):
        steps = [steps]
    out = ["%d. %s" % (i, s) for i, s in enumerate(steps, 1)]
    if data.get("fault"):
        out.append("\u26a0\ufe0f " + data["fault"])
    return out


def card(session_id, exercise, set_seq=None, lang="ko", recorded=None, day=None):
    """-> {"kind": full|tip|none, "lines": [...]} for this set's card.

    FULL on the lift's first card of the session; afterwards one tip, rotating,
    never repeating while another part remains."""
    body = parts(exercise, lang, recorded)
    if not body:
        return {"kind": NONE, "lines": []}
    ledger = _read(session_id, day)
    ent = ledger.get(exercise) or {}
    key = None if set_seq is None else str(set_seq)
    if key is not None and ent.get("last_key") == key and ent.get("last"):
        return dict(ent["last"])                    # same set again: same answer
    if not ent.get("full"):
        out = {"kind": FULL, "lines": body}
        ent = {"full": True, "tips": [0], "last_key": key, "last": out}   # tips start past step 1
    else:
        tips = [i for i in ent.get("tips", []) if i < len(body)]
        left = [i for i in range(len(body)) if i not in tips]
        if not left:                                # every part shown: start over
            tips, left = [], list(range(len(body)))
        pick = left[0]
        tips.append(pick)
        out = {"kind": TIP, "lines": [body[pick]]}
        ent = {"full": True, "tips": tips, "last_key": key, "last": out}
    ledger[exercise] = ent
    _write(session_id, ledger, day)
    return dict(out)
