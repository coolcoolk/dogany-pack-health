#!/usr/bin/env python3
"""emit.py -- the ONLY poster of session surfaces (design R2-R5).

A Frame from session_flow is posted here and nowhere else: table, then ONE card
carrying its keyboard, in that order, synchronously. Posting a card retires the
previous card (edited to a stub with no keyboard), so exactly one keyboard is
live in the session (R5). Dedupe is by (session, frame version), never by
content (R3): a version posts once, a re-run of the same version does nothing.

No other module may call push.sh for a session surface when WARG_FLOW=1; this
module is the single caller. The agent never relays any of this: the receipt it
gets is `FRAME_POSTED v=<n> ...` plus `SAY_SLOT <kind>`.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

PROJECT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))


def flow_enabled():
    """On by default: the old posters (per-set table publish, the tap rail's
    followup table, the rest push text) stand down for a session that has a flow
    ledger. WARG_FLOW=0 is the kill switch back to the old posters."""
    return os.environ.get("WARG_FLOW", "1") != "0"


def flow_owns(sid):
    """True when WARG_FLOW=1 AND this session runs on a flow ledger: the old
    posters stand down for it. A session with no ledger keeps the old posters,
    so a migration step can never leave the owner without a screen."""
    if not flow_enabled() or sid in (None, ""):
        return False
    try:
        import session_flow
        return session_flow.load(sid) is not None
    except Exception:  # noqa: BLE001
        return False


def flow_owns_plan(sid):
    """flow_owns for a session whose ledger holds a PLAN (not a free session):
    the ledger knows the lifts' loads, so its card is the only set keyboard and
    the legacy code-posted keyboards / record message stand down. A free session
    (lifts and owner-named weights the ledger never planned) keeps them."""
    if not flow_owns(sid):
        return False
    try:
        import session_flow
        return not (session_flow.load(sid) or {}).get("free")
    except Exception:  # noqa: BLE001
        return False


def _state_dir():
    return (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
            or os.path.join(HERE, "..", "..", "files", "program"))


def _push_bin():
    return os.environ.get("WARG_PUSH") or os.path.join(PROJECT_ROOT, "routines", "push.sh")


def _t(key, **kw):
    try:
        import ui_labels
        return ui_labels.i18n(key, **kw)
    except Exception:  # noqa: BLE001
        return ""


def _emitted_path(sid):
    return os.path.join(_state_dir(), ".flow", "%s.emitted" % re.sub(r"[^A-Za-z0-9_.-]", "_", str(sid)))


def last_emitted(sid):
    try:
        with open(_emitted_path(sid)) as fh:
            return int(fh.read().strip() or 0)
    except (OSError, ValueError):
        return 0


def _mark(sid, version):
    os.makedirs(os.path.dirname(_emitted_path(sid)), exist_ok=True)
    with open(_emitted_path(sid), "w") as fh:
        fh.write(str(int(version)))


def post(frame, sid, push_bin=None, state_dir=None):
    """Post one frame. Returns the receipt:
    {"version", "posted": bool, "table": str, "card": str, "say_slot": kind}"""
    import inplace_delivery as D
    receipt = {"version": frame["version"], "table": "none", "card": "none",
               "say_slot": (frame.get("say_slot") or {}).get("kind", "none"),
               "posted": False}
    if not frame.get("table") and not frame.get("card"):
        return receipt
    if frame["version"] <= last_emitted(sid):
        receipt["table"] = receipt["card"] = "skipped:version"
        return receipt
    push_bin = push_bin or _push_bin()
    state_dir = state_dir or _state_dir()
    stub = _t("health.live.table_moved")
    # (a) the table, at the bottom of the chat
    if frame.get("table"):
        key = D.surface_key("table", sid, frame.get("lift"))
        ok, detail, _ = D.move_down(key, frame["table"], push_bin, state_dir, stub=stub)
        receipt["table"] = "ok" if ok else "failed:%s" % detail
    # (b) ONE card with its keyboard; the previous card (and keyboard) retires
    if frame.get("card"):
        key = D.surface_key("card", sid)
        ok, detail, _ = D.move_down(key, "\n".join(frame["card"]), push_bin, state_dir,
                                    stub=stub, buttons=frame.get("keyboard") or [])
        receipt["card"] = "ok" if ok else "failed:%s" % detail
    receipt["posted"] = "failed" not in receipt["table"] + receipt["card"]
    if receipt["posted"]:
        _mark(sid, frame["version"])
        if frame.get("timer"):
            spawn_rest_done(sid, frame["timer"])
    return receipt


def spawn_rest_done(sid, timer):
    """The ONE rest-done speaker: after the rest, a detached `flow step <sid>
    --event rest_done` carrying the LEDGER's own rest number (never set-arm's DB
    set_seq, whose count differs whenever a warm-up rung precedes the working
    sets). The ledger answers with the rest actually taken, or stays silent when
    the owner already started the next set. The bridge countdown message itself is
    set-arm's channel 1 (it is armed there, on every set-add, for flow sessions
    too); this worker is the only thing that SPEAKS at the end.
    WARG_FLOW_REST_SPAWN=0 disables it (suites fire the event themselves)."""
    if os.environ.get("WARG_FLOW_REST_SPAWN", "1") == "0":
        return False
    import json
    import subprocess
    cmd = ["sh", "-c", 'sleep %d; exec "$0" "$1" step "$2" --event rest_done '
           '--args-json "$3"' % int(timer["sec"]), sys.executable,
           os.path.join(HERE, "flow"), str(sid), json.dumps({"n": int(timer["n"])})]
    try:
        subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL, start_new_session=True)
        return True
    except OSError:
        return False


def stdout_lines(receipt, frame):
    """What the agent sees: a receipt and a slot, never frame content."""
    kind = (frame.get("say_slot") or {}).get("kind", "none")
    out = ["FRAME_POSTED v=%s table=%s card=%s" % (receipt["version"], receipt["table"], receipt["card"]),
           "SAY_SLOT %s" % (kind if kind != "none" else "NONE")]
    if kind != "none" and (frame["say_slot"].get("hint")):
        out[-1] += " hint=%s" % frame["say_slot"]["hint"]
    for f in frame.get("facts") or []:
        out.append("FLOW_FACT %s" % f)
    return out
