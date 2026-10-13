"""rest.py -- the ONE speaker for "rest done" (R-R1..R-R3, design section 4).

Before: two messages announced the end of a rest (the bridge countdown and a
detached push from set-arm), the push quoted the PLANNED seconds, and a rest
that ended after the next set was already logged still spoke. Now the flow
ledger holds one record per rest and `fire` answers once:

  arm(rest, n, planned_sec, now)   write the rest record for working set n
  fire(rest, n, now)               -> the rest-done text, or None when it must
                                      stay silent (a later set already started,
                                      or this rest already spoke)

The text states the rest actually taken; a set started early reads
"<elapsed> (<planned> planned)" (ko copy in i18n). Posting is emit.py's job, not this module's.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EARLY_SLACK_SEC = 3          # a fire this far short of the plan is still on time


def fmt_sec(sec):
    sec = max(int(round(sec)), 0)
    return "%d:%02d" % (sec // 60, sec % 60)


def _t(key, **kw):
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import ui_labels
        return ui_labels.i18n(key, **kw)
    except Exception:  # noqa: BLE001
        return ""


def done_text(elapsed_sec, planned_sec):
    """Rest done with the elapsed time, or elapsed vs planned for an early start."""
    if planned_sec and elapsed_sec < planned_sec - EARLY_SLACK_SEC:
        return _t("health.rest.done_early", elapsed=fmt_sec(elapsed_sec),
                  planned=fmt_sec(planned_sec))
    return _t("health.rest.done", elapsed=fmt_sec(elapsed_sec))


def arm(n, planned_sec, now):
    """The record of the rest that follows working set `n`."""
    return {"n": int(n), "planned": int(planned_sec), "started": float(now),
            "spoke": False}


def fire(rest, n, now):
    """The rest-done text for rest `n`, once. None = stay silent: no such rest,
    it already spoke, or the owner is past it (R-R3). Marks the record spoken."""
    if not rest or int(rest.get("n", -1)) != int(n) or rest.get("spoke"):
        return None
    rest["spoke"] = True
    return done_text(float(now) - float(rest["started"]), rest.get("planned"))
