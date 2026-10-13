#!/usr/bin/env python3
"""session_flow.py -- THE ledger of a live workout session (design sections 2-5).

ONE entry (`step`), ONE place that computes the next screen, ONE frame out. The
poster (emit.py) shows frames; nothing else posts a session surface. Every piece
this module calls (cue, rest, implement, live_load) is a pure owner that posts
nothing.

States (design 3.1)
  S1 PLAN  S2 PREP  S3 ENTRY  S4 SET_READY  S5 RESTING  S6 LIFT_DONE
  S7 POST  S8 CLOSED          (S0 IDLE = no flow file)

Events
  flow events   start, enter, set_logged, rest_done, next_lift, undo, tap
  owner intents (accepted in EVERY state S1-S7, design 3.2):
                split_choose, claim, skip_lift, swap_lift, reorder, weight,
                missing, minutes, warmup_reclass, pain, stop, question,
                stack_unknown, stack_photo, stack_pick, correct
  An unknown event is refused with a NAMED code (FlowError.code), never ignored.

Frame (what `step` returns)
  {version, state, lift, table, card:[lines], keyboard:[rows], say_slot:{kind,..},
   timer:{sec,n}|None, facts:[...], repost}
  table -> card -> keyboard is the only order (emit.py). The agent says one line
  at most, and only when say_slot.kind is not "none"; it never restates the table,
  card, weight, cue or next set.

Memory of stated facts (R-T6/R-T7): a weight the owner named sticks for the lift,
a weight the gym lacks never comes back (it is also taught to the venue profile),
the start-weight line is said once per lift and never after the lift's first set.
"""
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

S1, S2, S3, S4, S5, S6, S7, S8 = ("PLAN", "PREP", "ENTRY", "SET_READY",
                                  "RESTING", "LIFT_DONE", "POST", "CLOSED")
ACTIVE = (S1, S2, S3, S4, S5, S6, S7)

FLOW_EVENTS = ("start", "enter", "set_logged", "rest_done", "next_lift",
               "undo", "tap", "prep")
INTENTS = ("split_choose", "claim", "skip_lift", "swap_lift", "reorder",
           "weight", "missing", "minutes", "warmup_reclass", "pain", "stop",
           "question", "stack_unknown", "stack_photo", "stack_pick", "correct")

SAY_NONE, SAY_ANSWER, SAY_LEAD, SAY_NOTICE = "none", "answer", "lead", "notice"
ABANDON_SEC = 12 * 3600
DEFAULT_REST_SEC = 120
RIR_CHOICES = (0, 1, 2, 3, 4)


class FlowError(Exception):
    def __init__(self, code, detail=""):
        Exception.__init__(self, "%s %s" % (code, detail))
        self.code, self.detail = code, detail


# ---------------------------------------------------------------------------
# copy + state file
# ---------------------------------------------------------------------------
def _t(key, **kw):
    try:
        import ui_labels
        return ui_labels.i18n(key, **kw)
    except Exception:  # noqa: BLE001
        return ""


def _fmt(v):
    import implement
    return implement.fmt(v)


def flow_dir():
    base = (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
            or os.path.join(HERE, "..", "..", "files", "program"))
    return os.path.join(base, ".flow")


def _path(sid):
    return os.path.join(flow_dir(), "%s.json" % re.sub(r"[^A-Za-z0-9_.-]", "_", str(sid)))


def load(sid, now=None):
    """The session's flow state, or None (S0). A state untouched for 12 h is
    abandoned: dropped, so a new session starts clean."""
    try:
        with open(_path(sid), encoding="utf-8") as fh:
            st = json.load(fh)
    except (OSError, ValueError):
        return None
    if (now or time.time()) - float(st.get("touched", 0)) > ABANDON_SEC:
        try:
            os.remove(_path(sid))
        except OSError:
            pass
        return None
    return st


def save(sid, st, now=None):
    st["touched"] = now or time.time()
    os.makedirs(flow_dir(), exist_ok=True)
    tmp = _path(sid) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(st, fh, ensure_ascii=False)
    os.replace(tmp, _path(sid))


def lift_closed(sid, lift):
    """True once the lift is finished or skipped in this session's ledger."""
    st = load(sid)
    return bool(st) and lift in st.get("closed", [])


# ---------------------------------------------------------------------------
# plan access
# ---------------------------------------------------------------------------
def _lift(st, name=None):
    name = name or st.get("lift")
    return (st.get("plan") or {}).get(name) or {}


def _disp(st, name):
    import implement
    ent = _lift(st, name)
    return implement.display_name(ent.get("display") or name,
                                  ent.get("kind") if ent.get("kind") == "assisted" else None)


def _day(st):
    """The session's date (KST) -- half of the cue memory's key."""
    import datetime
    return (datetime.datetime.utcfromtimestamp(float(st.get("created") or time.time()))
            + datetime.timedelta(hours=9)).date().isoformat()


def _log(st, name):
    return st["logs"].setdefault(name, [])


def _working(st, name):
    return [s for s in _log(st, name) if s["kind"] == "working"]


def _warm(st, name):
    return [s for s in _log(st, name) if s["kind"] == "warmup"]


def _remaining_order(st):
    return [n for n in st["order"] if n not in st["closed"]]


def _next_lift_name(st):
    rest = [n for n in _remaining_order(st) if n != st.get("lift")]
    return rest[0] if rest else None


# ---------------------------------------------------------------------------
# the load: ONE decider (facts + grid + guard)
# ---------------------------------------------------------------------------
def _grid(st, name):
    """Settable weights for the lift: the dumbbell rack is the venue's (learned
    set > learned step > default, minus gaps -- implement.venue_dumbbell_points);
    other implements step by the lift's own step, minus learned gaps."""
    import implement
    ent = _lift(st, name)
    kind = ent.get("kind")
    gaps = set(st["facts"]["gaps"].get(name, []))
    if kind == implement.DUMBBELL:
        pts = implement.venue_dumbbell_points()
    else:
        step = float(ent.get("step") or 2.5)
        base = float(ent.get("kg") or 0)
        top = max(base * 2, 100.0)
        pts = [round(step * k, 4) for k in range(1, int(top // step) + 1)]
    return [p for p in pts if p not in gaps] or pts


def _snap(st, name, kg, prefer="up"):
    pts = _grid(st, name)
    if prefer == "down":
        return min(pts, key=lambda p: (abs(p - kg), p))
    return min(pts, key=lambda p: (abs(p - kg), -p))


def decide(st, name):
    """The next set of `name`: {kind, kg, reps, display, seq} or None when the
    lift has ended -- no load line is ever composed after that (R-E9/R-L1)."""
    import implement
    if name in st["closed"]:
        return None
    ent = _lift(st, name)
    kind = ent.get("kind")
    warm_done = len(_warm(st, name))
    warms = ent.get("warmups") or []
    if warm_done < len(warms) and not _working(st, name):
        w = warms[warm_done]
        kg, reps, sk = float(w["kg"]), int(w.get("reps") or 5), "warmup"
        seq = warm_done + 1
    else:
        sk, seq = "working", len(_working(st, name)) + 1
        stated = st["facts"]["weights"].get(name)
        kg = float(stated if stated is not None else ent.get("kg") or 0)
        reps = int(ent.get("reps") or 8)
        if (stated is None and kg
                and kind not in (implement.ASSISTED, implement.BODYWEIGHT)):
            kg = _snap(st, name, kg, "down")        # the prescription lands on THIS gym's grid
    if kind in (implement.ASSISTED, implement.BODYWEIGHT):
        shown = implement.wt_text(kind, kg if kg else None)
    elif kg:
        shown = implement.display(kind, kg)
    else:
        shown = _t("health.flow.wt_open")       # no weight on file: never a made-up "0kg"
    return {"kind": sk, "kg": kg, "reps": reps, "display": shown, "seq": seq,
            "wt_plain": _t("health.flow.btn.weight", kg=_fmt(kg)) if kg else shown}


def _rest_sec(st, name):
    return int(_lift(st, name).get("rest_sec") or DEFAULT_REST_SEC)


# ---------------------------------------------------------------------------
# rendering: table, keyboard, cards
# ---------------------------------------------------------------------------
def _cb(sid, st, event, arg=""):
    data = "flow|%s|%s|%s|%s" % (sid, st["version"] + 1, event, arg)
    return data[:64]


def _quote(lines):
    """A cue's lines as ONE blockquote under the card's title line (owner
    2026-10-13 06:44): every line, so the quote reads as a single block."""
    return ["> %s" % ln for ln in lines if ln]


def _btn(text, data):
    return {"text": text, "callback_data": data}


def render_table(st, name):
    """The lift's set table: English heads (R-T9), warm-ups included (R-E11),
    done rows checked, the next row marked. A pure render of the ledger."""
    import implement
    ent = _lift(st, name)
    kind = ent.get("kind")
    cls = kind if kind in (implement.ASSISTED, implement.BODYWEIGHT) else None
    head_wt = implement.head_wt(cls) or "WT"
    cols = ("SET", head_wt, "REPS", "RIR", "ST")
    widths = (5, 9, 6, 5, 5)
    border = "+" + "+".join("-" * w for w in widths) + "+"

    def row(*cells):
        out = []
        for c, w in zip(cells, widths):
            pad = w - implement._disp_w(c)
            out.append(" " * (pad // 2) + str(c) + " " * (pad - pad // 2))
        return "|" + "|".join(out) + "|"

    def wt(kg):
        if cls:
            return implement.wt_cell(cls, kg if kg else None)
        return "%skg" % _fmt(kg) if kg else "?"

    lines = [border, row(*cols), border]
    for i, s in enumerate(_warm(st, name), 1):
        lines.append(row("w%d" % i, wt(s["kg"]), s["reps"], "-", "[v]"))
    for i, s in enumerate(_working(st, name), 1):
        lines.append(row(i, wt(s["kg"]), s["reps"],
                         "-" if s.get("rir") is None else s["rir"], "[v]"))
    nxt = decide(st, name)
    owed = int(ent.get("sets") or 0) - len(_working(st, name))
    if nxt and nxt["kind"] == "working":
        for i in range(owed):
            n = len(_working(st, name)) + i + 1
            lines.append(row(n, wt(nxt["kg"]), nxt["reps"], "", "[>]" if i == 0 else "[ ]"))
    elif nxt:
        lines.append(row("w%d" % nxt["seq"], wt(nxt["kg"]), nxt["reps"], "", "[>]"))
    lines.append(border)
    return _t("health.flow.table_head", lift=_disp(st, name), grid="\n".join(lines))


def _weight_row(sid, st, name, nxt):
    """Q1 (owner 2026-10-09): the weight the engine chose, circled, among its
    neighbours on this gym's grid. One tap overrides it (event `weight`)."""
    if not nxt or not nxt["kg"] or _lift(st, name).get("kind") in ("assisted", "bodyweight"):
        return []
    pts = _grid(st, name)
    kg = nxt["kg"]
    if kg not in pts:
        pts = sorted(pts + [kg])
    i = pts.index(kg)
    near = pts[max(i - 1, 0):i + 2]
    return [[_btn(_t("health.flow.btn.weight_on" if p == kg else "health.flow.btn.weight", kg=_fmt(p)),
                  _cb(sid, st, "weight", _fmt(p))) for p in near]]


def _set_keyboard(sid, st, name, nxt):
    if not nxt:
        return []
    if nxt["kind"] == "warmup":
        return [[_btn(_t("health.flow.btn.done"), _cb(sid, st, "set_logged",
                                                      "w:%s:%d" % (_fmt(nxt["kg"]), nxt["reps"])))]]
    reps = nxt["reps"]
    window = sorted(set(max(r, 1) for r in range(reps - 2, reps + 3)))
    rows = _weight_row(sid, st, name, nxt)
    rows.append([_btn(_t("health.flow.btn.reps", n=r), _cb(sid, st, "reps", str(r)))
                 for r in window])
    return rows


def _rir_keyboard(sid, st):
    return [[_btn(_t("health.flow.btn.rir", n=n), _cb(sid, st, "rir", str(n)))
             for n in RIR_CHOICES]]


def _next_line(st, name, rest=True):
    nxt = decide(st, name)
    if not nxt or nxt["kind"] != "working":
        return None
    from rest import fmt_sec
    tail = _t("health.flow.next_rest", rest=fmt_sec(_rest_sec(st, name))) if rest else ""
    return _t("health.flow.next", lift=_disp(st, name), wt=nxt["display"],
              reps=nxt["reps"], rest=tail)


def _record_line(st, name, s, seq):
    import implement
    ent = _lift(st, name)
    kind = ent.get("kind")
    shown = (implement.wt_text(kind, s["kg"] if s["kg"] else None)
             if kind in ("assisted", "bodyweight") else
             implement.display(kind, s["kg"]) if s["kg"] else _t("health.flow.wt_open"))
    if s["kind"] == "warmup":
        return _t("health.flow.record_warmup", lift=_disp(st, name), wt=shown, reps=s["reps"])
    return _t("health.flow.record", lift=_disp(st, name), set=seq, wt=shown,
              reps=s["reps"], rir="-" if s.get("rir") is None else s["rir"])


# ---------------------------------------------------------------------------
# frame assembly
# ---------------------------------------------------------------------------
def _frame(sid, st, card, keyboard=None, say=None, timer=None, table_for=None,
           facts=None, repost=False):
    """Bump the version and build the frame. The ledger is saved by the caller
    (step) after this returns, so a frame is never emitted for an unsaved state."""
    st["version"] += 1
    name = table_for if table_for is not None else st.get("lift")
    table = render_table(st, name) if (table_for is not None and name in st["plan"]) else None
    return {"version": st["version"], "state": st["state"], "lift": st.get("lift"),
            "table": table, "card": [c for c in card if c],
            "keyboard": keyboard or [],
            "say_slot": say or {"kind": SAY_NONE},
            "timer": timer, "facts": facts or [], "repost": repost}


def _current_frame(sid, st, lead=None):
    """Re-render the current screen (stale tap, correct, weight change)."""
    name = st.get("lift")
    nxt = decide(st, name) if name else None
    card = [lead, _t("health.flow.entry_head", lift=_disp(st, name)) if name else None]
    if nxt:
        what = (_t("health.flow.do_warmup", wt=nxt["display"], reps=nxt["reps"])
                if nxt["kind"] == "warmup" else
                _t("health.flow.do_working", set=nxt["seq"], wt=nxt["display"], reps=nxt["reps"]))
        if nxt["kind"] == "working" and _lift(st, name).get("est") and not _working(st, name):
            what += _t("health.flow.first_light")       # a proposed first weight, said as light
        card.append(_t("health.flow.do_now", what=what))
    return _frame(sid, st, card, _set_keyboard(sid, st, name, nxt) if st["state"] in (S3, S4, S5) else [],
                  table_for=name, repost=True)


def _new_state(sid, args, now):
    plan = {}
    order = []
    for ent in args.get("lifts") or []:
        ent = dict(ent)
        plan[ent["name"]] = ent
        order.append(ent["name"])
    return {"sid": sid, "version": 0, "state": S1, "lift": None, "plan": plan,
            "order": order, "closed": [], "logs": {}, "rest": None,
            "pending": None, "split": args.get("split"), "free": bool(args.get("free")),
            "claim": None, "minutes": None, "created": now,
            "env": dict(args.get("env") or {}),
            "said": {"start_weight": [], "pain": []},
            "facts": {"weights": {}, "gaps": {}, "stacks": {}, "pain": [], "questions": 0}}


# ---------------------------------------------------------------------------
# step: the one entry
# ---------------------------------------------------------------------------
def step(sid, event, args=None, now=None):
    """Apply one event to the session ledger and return the Frame to show.
    Raises FlowError with a named code for an unknown event or a violated gate."""
    args = args or {}
    now = now or time.time()
    if event not in FLOW_EVENTS and event not in INTENTS:
        raise FlowError("unknown_event", event)
    st = load(sid, now)
    if st is None:
        if event != "start":
            raise FlowError("no_session", "send event=start first")
        st = _new_state(sid, args, now)
    elif event == "start":
        raise FlowError("already_started", str(sid))
    if st["state"] == S8 and event != "claim":
        raise FlowError("session_closed", str(sid))
    handler = globals().get("_on_" + event)
    frame = handler(sid, st, args, now)
    save(sid, st, now)
    return frame


class _Lock(object):
    """One writer at a time per session: a tap, a set-add hook and the detached
    rest-done worker can all call `step` in the same second."""
    def __init__(self, sid):
        self.sid = sid
        self.fh = None

    def __enter__(self):
        import fcntl
        os.makedirs(flow_dir(), exist_ok=True)
        self.fh = open(_path(self.sid) + ".lock", "a")
        fcntl.flock(self.fh, fcntl.LOCK_EX)
        return self

    def __exit__(self, *exc):
        import fcntl
        try:
            fcntl.flock(self.fh, fcntl.LOCK_UN)
        finally:
            self.fh.close()


def locked_step(sid, event, args=None, now=None):
    """`step` under the session lock -- the entry every live caller uses."""
    with _Lock(sid):
        return step(sid, event, args, now)


def add_lifts(sid, entries, env=None, now=None):
    """Register plan entries the ledger does not hold yet (a free session's
    lift, a lift added mid-session). Not an owner event: no frame, no version.
    Returns the names added."""
    with _Lock(sid):
        st = load(sid, now)
        if st is None:
            raise FlowError("no_session", "send event=start first")
        added = []
        for ent in entries:
            ent = dict(ent)
            if ent["name"] in st["plan"]:
                continue
            st["plan"][ent["name"]] = ent
            st["order"].append(ent["name"])
            added.append(ent["name"])
        if env:
            st.setdefault("env", {}).update(env)
        save(sid, st, now)
        return added


def show(sid):
    st = load(sid)
    if st is None:
        return None
    return {"state": st["state"], "version": st["version"], "lift": st.get("lift"),
            "closed": st["closed"], "order": st["order"], "facts": st["facts"],
            "rest": st["rest"], "logs": st["logs"]}


# ---- flow events ----------------------------------------------------------
def _on_start(sid, st, args, now):
    st["state"] = S1
    n = len(st["order"])
    card = [_t("health.flow.plan", split=args.get("split") or "", n=n)]
    kb = [[_btn(_t("health.flow.btn.start_lift", lift=_disp(st, st["order"][0])),
                _cb(sid, st, "enter", st["order"][0]))]] if n else []
    return _frame(sid, st, card, kb, say={"kind": SAY_LEAD, "hint": "plan"})


def _begin_lift(sid, st, name, now):
    """S3 ENTRY: table + FULL cue (once) + the start-weight line (once) + what
    to do now + the first set's keyboard."""
    import cue
    st["lift"], st["state"] = name, S3
    st["rest"] = None
    st["prep"] = None
    nxt = decide(st, name)
    c = cue.card(sid, name, 0, day=_day(st))
    card = [_t("health.flow.entry_head", lift=_disp(st, name))] + _quote(c["lines"])
    # the "now" line below carries the weight: one weight per instruction (R-T5)
    if nxt:
        what = (_t("health.flow.do_warmup", wt=nxt["display"], reps=nxt["reps"])
                if nxt["kind"] == "warmup" else
                _t("health.flow.do_working", set=nxt["seq"], wt=nxt["display"], reps=nxt["reps"]))
        if nxt["kind"] == "working" and _lift(st, name).get("est") and not _working(st, name):
            what += _t("health.flow.first_light")       # a proposed first weight, said as light
        card.append(_t("health.flow.do_now", what=what))
    return _frame(sid, st, card, _set_keyboard(sid, st, name, nxt), table_for=name)


def _prep_frame(sid, st, lead=None):
    """S2 PREP: the stored prep drill as a frame -- the prep table, then ONE card
    (title outside, the cue quoted) with its done button (+ the nearby-weight row
    of a loaded drill). Built from `st["prep"]`, so a stale tap re-renders it."""
    p = st["prep"]
    rows = [[_btn(p["button"], _cb(sid, st, "prep", ""))]]
    if p.get("near"):
        rows.append([_btn(_t("health.flow.btn.weight", kg=_fmt(w)), _cb(sid, st, "prep", _fmt(w)))
                     for w in p["near"]])
    fr = _frame(sid, st, ([lead] if lead else []) + list(p["card"]), rows, repost=bool(lead))
    fr["table"] = p.get("table") or None
    fr["lift"] = None                  # the table is the prep table: never swapped for a lift's
    return fr


def _on_prep(sid, st, args, now):
    """One prep drill's card (R-PR3/R-PR4/R-PR5). The drill's literal set-add
    argv rides the ledger, so its done button is code-routed (no model turn):
    tap -> set-add prep row -> the next drill's card."""
    if (st["state"] == S2 and (st.get("prep") or {}).get("seq") == int(args["seq"])
            and (st["prep"].get("lift") == args.get("lift"))):
        return _silent(st, "prep_refire")          # the same drill's card is already live
    st["state"] = S2
    st["rest"] = None
    st["prep"] = {"argv": [str(a) for a in args["argv"]], "seq": int(args["seq"]),
                  "lift": args.get("lift"), "table": args.get("table"),
                  "card": list(args["card"]), "button": args["button"],
                  "near": [float(w) for w in args.get("near") or []]}
    return _prep_frame(sid, st)


def _on_enter(sid, st, args, now):
    name = args.get("lift") or (_remaining_order(st) or [None])[0]
    if name not in st["plan"]:
        raise FlowError("unknown_lift", str(name))
    if name in st["closed"]:
        raise FlowError("lift_closed", name)
    return _begin_lift(sid, st, name, now)


def _on_next_lift(sid, st, args, now):
    nxt = args.get("lift") or _next_lift_name(st)
    if nxt is None:
        return _post_lifts(sid, st, st.get("lift"), [])
    return _begin_lift(sid, st, nxt, now)


def _lift_finished(sid, st, name, now, record):
    """S6: the lift ends. From here `decide` answers None for it, so no load
    line, start weight or closer can be composed about it again."""
    st["closed"].append(name)
    st["state"] = S6
    st["rest"] = None
    nxt = _next_lift_name(st)
    if nxt is None:
        return _post_lifts(sid, st, name, [record])
    card = [record, _t("health.flow.lift_done", lift=_disp(st, name), next=_disp(st, nxt))]
    kb = [[_btn(_t("health.flow.btn.start_lift", lift=_disp(st, nxt)), _cb(sid, st, "next_lift", nxt))]]
    return _frame(sid, st, card, kb, table_for=name)


def _post_lifts(sid, st, name, lead):
    """S7 POST: every lift is done or skipped. The cooldown / cardio cards are
    session-post's; this frame only says the sets are over and offers the close."""
    st["state"] = S7
    st["rest"] = None
    card = list(lead) + [_t("health.flow.all_done")]
    return _frame(sid, st, card, [[_btn(_t("health.flow.btn.done"), _cb(sid, st, "stop"))]],
                  table_for=name)


def _on_set_logged(sid, st, args, now):
    import cue
    import rest as R
    name = args.get("lift") or st.get("lift")
    if st["state"] in (S1, S2, S6, S7) or not name or name in st["closed"]:
        raise FlowError("no_open_lift", str(st["state"]))
    nxt = decide(st, name)
    kind = args.get("kind") or nxt["kind"]
    seq_in = args.get("seq")
    if seq_in is not None:
        # The DB row's set_seq (set-add's key). A re-fire of the same row, or a
        # correction of it, rewrites the ledger row in place -- never a second row.
        for row in _log(st, name):
            if row["kind"] == kind and row.get("seq") == int(seq_in):
                changed = False
                for key, cast in (("kg", float), ("reps", int), ("rir", int)):
                    if args.get(key) is not None and row.get(key) != cast(args[key]):
                        row[key] = cast(args[key])
                        changed = True
                return _current_frame(sid, st) if changed else _silent(st, "set_refire")
    if st["rest"]:
        st["rest"]["spoke"] = True          # the owner is past this rest (R-R3)
    kg = float(args["kg"]) if args.get("kg") is not None else nxt["kg"]
    s = {"kind": kind, "kg": kg, "reps": int(args.get("reps") or nxt["reps"]),
         "rir": args.get("rir"), "at": now}
    if seq_in is not None:
        s["seq"] = int(seq_in)
    if (kind == "working" and args.get("kg") is not None
            and nxt["kind"] == "working" and abs(kg - nxt["kg"]) > 1e-6):
        st["facts"]["weights"][name] = kg   # the weight the owner used stays (R-T6)
    _log(st, name).append(s)
    st["pending"] = None
    seq = len(_working(st, name)) if kind == "working" else len(_warm(st, name))
    record = _record_line(st, name, s, seq)
    if kind == "working" and len(_working(st, name)) >= int(_lift(st, name).get("sets") or 0):
        return _lift_finished(sid, st, name, now, record)
    nxt2 = decide(st, name)
    tip = cue.card(sid, name, ("w" if nxt2["kind"] == "warmup" else "s") + str(nxt2["seq"]),
                   day=_day(st))
    card = [record] + (_quote(tip["lines"][:1])) + [_next_line(st, name, rest=kind == "working")]
    timer = None
    if kind == "working":                      # a warm-up never arms a rest (R-E12)
        sec = _rest_sec(st, name)
        st["rest"] = R.arm(len(_working(st, name)), sec, now)
        st["state"], timer = S5, {"sec": sec, "n": len(_working(st, name))}
    else:
        st["state"] = S4
    return _frame(sid, st, card, _set_keyboard(sid, st, name, nxt2), timer=timer, table_for=name)


def _silent(st, fact):
    """A frame that posts nothing (a re-fired write, a stale rest-done)."""
    return {"version": st["version"], "state": st["state"], "lift": st.get("lift"),
            "table": None, "card": [], "keyboard": [], "say_slot": {"kind": SAY_NONE},
            "timer": None, "facts": [fact], "repost": False}


def _on_rest_done(sid, st, args, now):
    import rest as R
    # n comes from the ledger's own timer (emit spawns the worker with it), never
    # from set-arm's DB set_seq: the two counts differ whenever a warm-up rung or
    # a prep row precedes the working sets, which used to silence rest-done.
    n = int((st["rest"] or {}).get("n", -1)) if args.get("n") is None else int(args["n"])
    text = R.fire(st["rest"], n, now) if st["state"] == S5 else None
    if text is None:                           # stale or already spoken: silence
        return _silent(st, "rest_done_suppressed")
    st["state"] = S4
    name = st["lift"]
    nxt = decide(st, name)
    card = [text, _next_line(st, name, rest=False)]
    # No table: nothing was logged since the last one, so the owner's latest table
    # is still the newest; re-posting it would be a duplicate message (R-T1 is
    # "after each logged row").
    return _frame(sid, st, card, _set_keyboard(sid, st, name, nxt))


def _on_tap(sid, st, args, now):
    """A keyboard tap. A tap on an old keyboard says so and shows the current
    card (R-T7); a live one is routed as its event."""
    ver = int(args.get("ver", st["version"]))
    ev, arg = args.get("event"), args.get("arg", "")
    if ver != st["version"]:
        if st["state"] == S2 and st.get("prep"):
            return _prep_frame(sid, st, lead=_t("health.flow.moved"))
        return _current_frame(sid, st, lead=_t("health.flow.moved"))
    if ev == "reps":
        st["pending"] = {"reps": int(arg)}
        card = [_t("health.flow.rir_prompt", reps=int(arg))]
        return _frame(sid, st, card, _rir_keyboard(sid, st), table_for=None, repost=True)
    if ev == "rir":
        if not st.get("pending"):
            return _current_frame(sid, st, lead=_t("health.flow.moved"))
        return _on_set_logged(sid, st, {"reps": st["pending"]["reps"], "rir": int(arg)}, now)
    if ev == "set_logged" and str(arg).startswith("w:"):
        _w, kg, reps = arg.split(":")
        return _on_set_logged(sid, st, {"kg": float(kg), "reps": int(reps), "kind": "warmup"}, now)
    if ev == "enter" or ev == "next_lift":
        return _on_next_lift(sid, st, {"lift": arg or None}, now) if ev == "next_lift" \
            else _on_enter(sid, st, {"lift": arg}, now)
    if ev == "weight":
        return _on_weight(sid, st, {"kg": float(arg)}, now)
    if ev == "stop":
        return _on_stop(sid, st, {}, now)
    raise FlowError("unknown_tap", str(ev))


def _on_undo(sid, st, args, now):
    """Remove a logged set. With `seq` (set-undo's DB set_seq: >=1 working, <=0
    warm-up) the matching ledger row goes; without it, the lift's last row. A
    seq the ledger never held is a silent no-op (the row was not a ledger set)."""
    name = args.get("lift") or st.get("lift")
    log = _log(st, name) if name else []
    if args.get("seq") is not None:
        kind = "working" if int(args["seq"]) >= 1 else "warmup"
        hit = [r for r in log if r["kind"] == kind and r.get("seq") == int(args["seq"])]
        if not hit:
            return _silent(st, "undo_unknown_row")
        log.remove(hit[0])
    elif log:
        log.pop()
    else:
        raise FlowError("nothing_to_undo", str(name))
    if name in st["closed"]:
        st["closed"].remove(name)
    st["lift"] = name
    st["state"] = S4
    st["rest"] = None
    return _current_frame(sid, st)


# ---- owner intents (every state) -------------------------------------------
def _on_weight(sid, st, args, now):
    """Owner says a weight ("use 20"): the owner's number becomes the lift's weight and STAYS it
    (R-T6) until the owner changes it. No arguing back."""
    name = args.get("lift") or st.get("lift")
    kg = float(args["kg"])
    st["facts"]["weights"][name] = kg
    return _current_frame(sid, st)


def _on_missing(sid, st, args, now):
    """Owner says "no 15, 14 or 16": the gym lacks it. Learn it, re-decide the SAME set at
    the nearest available weight, and give a fresh keyboard now (R-T7)."""
    import implement
    name = args.get("lift") or st.get("lift")
    kg = float(args["kg"])
    ent = _lift(st, name)
    gaps = st["facts"]["gaps"].setdefault(name, [])
    if kg not in gaps:
        gaps.append(kg)
    alts = args.get("alts")
    if ent.get("kind") == implement.DUMBBELL:
        try:
            implement.mark_gap("dumbbell", kg, alts)
        except Exception:  # noqa: BLE001 -- the ledger already holds the gap
            pass
    if args.get("pick") is not None:
        new = float(args["pick"])
    else:
        new = _snap(st, name, kg, "down")
    st["facts"]["weights"][name] = new
    lead = _t("health.flow.gap", kg=_fmt(kg), new=_t("health.flow.btn.weight", kg=_fmt(new)))
    fr = _current_frame(sid, st, lead=lead)
    fr["facts"] = ["gap:%s" % _fmt(kg)]
    return fr


def _on_warmup_reclass(sid, st, args, now):
    """Owner says the last set was a warm-up: re-file the last working set as a warm-up; the next
    set goes to the next weight."""
    name = st.get("lift")
    work = _working(st, name)
    if not work:
        raise FlowError("nothing_to_reclass", str(name))
    last = work[-1]
    last["kind"] = "warmup"
    ent = _lift(st, name)
    if last["kg"] >= float(ent.get("kg") or 0):
        pts = _grid(st, name)
        higher = [p for p in pts if p > last["kg"]]
        if higher:
            st["facts"]["weights"][name] = higher[0]
    st["state"] = S4
    st["rest"] = None
    return _current_frame(sid, st)


def _on_skip_lift(sid, st, args, now):
    name = args.get("lift") or st.get("lift")
    if name not in st["plan"]:
        raise FlowError("unknown_lift", str(name))
    if name not in st["closed"]:
        st["closed"].append(name)
    nxt = _next_lift_name(st)
    if nxt is None:
        return _post_lifts(sid, st, name, [])
    fr = _begin_lift(sid, st, nxt, now)
    fr["card"].insert(0, _t("health.flow.skipped", lift=_disp(st, name), next=_disp(st, nxt)))
    return fr


def _on_swap_lift(sid, st, args, now):
    """The new lift is its OWN exercise on the slot (F4), remaining sets carried
    over; never a display-only rename."""
    old = st.get("lift")
    new = args["new"]
    ent = dict(_lift(st, old))
    ent.update(args.get("plan") or {})
    ent["name"] = new
    done = len(_working(st, old))
    ent["sets"] = max(int(_lift(st, old).get("sets") or 0) - done, 1)
    ent["display"] = args.get("display") or new
    st["plan"][new] = ent
    st["order"][st["order"].index(old)] = new
    if old not in st["closed"] and not done:
        st["closed"].append(old)
    fr = _begin_lift(sid, st, new, now)
    fr["card"].insert(0, _t("health.flow.swapped", old=_disp(st, old), new=_disp(st, new)))
    return fr


def _on_reorder(sid, st, args, now):
    name = args["lift"]
    if name not in st["order"]:
        raise FlowError("unknown_lift", name)
    st["order"].remove(name)
    cur = st.get("lift")
    idx = st["order"].index(cur) + 1 if cur in st["order"] else 0
    st["order"].insert(idx, name)
    return _begin_lift(sid, st, name, now) if args.get("now", True) else _current_frame(sid, st)


def _on_minutes(sid, st, args, now):
    """Owner says only 40 minutes are left: re-trim the REMAINING lineup to the window."""
    minutes = float(args["minutes"])
    st["minutes"] = minutes
    keep, used = [], 0.0
    for n in _remaining_order(st):
        ent = _lift(st, n)
        cost = int(ent.get("sets") or 3) * (_rest_sec(st, n) / 60.0 + 1.0)
        if keep and used + cost > minutes:
            continue
        keep.append(n)
        used += cost
    for n in _remaining_order(st):
        if n not in keep and n != st.get("lift"):
            st["closed"].append(n)
    return _current_frame(sid, st, lead=_t("health.flow.minutes", minutes=_fmt(minutes), n=len(keep)))


def _on_pain(sid, st, args, now):
    """D5 gate: a lift that loads the hurting site stops, with the substitute
    offered; otherwise the site is noted and the session continues."""
    site = args["site"]
    st["facts"]["pain"].append(site)
    name = st.get("lift")
    ent = _lift(st, name)
    if name and site in (ent.get("loads") or []):
        alt = ent.get("substitute")
        if name not in st["closed"]:
            st["closed"].append(name)
        card = [_t("health.flow.pain_stop", lift=_disp(st, name), alt=alt or "-")]
        kb = [[_btn(_t("health.flow.btn.alt", lift=alt), _cb(sid, st, "swap_lift", alt))]] if alt else []
        return _frame(sid, st, card, kb, say={"kind": SAY_NOTICE, "hint": "pain_stop"}, table_for=name)
    fr = _current_frame(sid, st, lead=_t("health.flow.pain_note", site=site))
    fr["say_slot"] = {"kind": SAY_NOTICE, "hint": "pain_note"}
    return fr


def _finish(sid, st, now):
    st["state"] = S8
    sets = sum(len(_working(st, n)) for n in st["logs"])
    lifts = sum(1 for n in st["logs"] if _working(st, n))
    card = [_t("health.flow.stop_summary", sets=sets, lifts=lifts)]
    return _frame(sid, st, card, [], repost=True)


def _on_stop(sid, st, args, now):
    """Owner says go home: skips everything left and closes with the summary, never a
    blocked close."""
    for n in st["order"]:
        if n not in st["closed"]:
            st["closed"].append(n)
    return _finish(sid, st, now)


def _on_question(sid, st, args, now):
    """State unchanged; the agent answers in ONE line; nothing is re-posted."""
    st["facts"]["questions"] += 1
    return {"version": st["version"], "state": st["state"], "lift": st.get("lift"),
            "table": None, "card": [], "keyboard": [], "timer": None, "facts": [],
            "say_slot": {"kind": SAY_ANSWER, "hint": args.get("text", "")}, "repost": False}


def _on_split_choose(sid, st, args, now):
    st["split"], st["free"] = args["code"], False
    return _current_frame(sid, st)


def _on_claim(sid, st, args, now):
    st["claim"] = args["code"]
    st["split"] = args["code"]
    return {"version": st["version"], "state": st["state"], "lift": st.get("lift"),
            "table": None, "card": [], "keyboard": [], "timer": None, "facts": ["claim:%s" % args["code"]],
            "say_slot": {"kind": SAY_NONE}, "repost": False}


def _on_stack_unknown(sid, st, args, now):
    st["facts"]["stacks"][st.get("lift")] = {"state": "unknown"}
    return _current_frame(sid, st)


def _on_stack_photo(sid, st, args, now):
    st["facts"]["stacks"][st.get("lift")] = {"points": args.get("points"), "addon": args.get("addon")}
    return _current_frame(sid, st)


def _on_stack_pick(sid, st, args, now):
    st["facts"]["stacks"][st.get("lift")] = {"id": args.get("id")}
    return _current_frame(sid, st)


def _on_correct(sid, st, args, now):
    """Correct the last logged set in place (D3: find first, write once)."""
    name = args.get("lift") or st.get("lift")
    log = _log(st, name)
    if not log:
        raise FlowError("nothing_to_correct", str(name))
    for key in ("kg", "reps", "rir"):
        if args.get(key) is not None:
            log[-1][key] = float(args[key]) if key == "kg" else int(args[key])
    return _current_frame(sid, st)
