"""flow_adapter.py -- connects the live verbs to the flow ledger (P1b).

session_flow.py is pure (events in, frames out); emit.py is the only poster.
This module is the glue the live verbs call, so a real session is ledgered:

  start_ledger   session-open  -> `start` (compute only: session-open already
                                  posted the start card; the plan frame would be
                                  a second card)
  on_enter       exercise-enter -> `enter`  (table + entry card + first keyboard)
  on_set_added   set-add        -> `set_logged` (table -> card+keyboard; arms the
                                  rest worker through emit)
  tap            `flow tap <callback_data>` -> the owner's button, routed with no
                                  model turn; a rir / warm-up tap writes the DB
                                  through the real set-add, whose hook then logs
                                  the ledger and posts the frame

Every function is best-effort from the verb's side: a ledger failure must never
cost the logged set or the entry (callers wrap in try/except and fall back to the
old posters, which stand down only while a ledger exists).

The table the owner sees is set-table's render (ONE renderer). The ledger's own
render_table is the fallback when set-table cannot render.
"""
import importlib.machinery
import importlib.util
import json
import os
import re
import sqlite3
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import session_flow as F          # noqa: E402

_MODS = {}
PREP_SEQ_BASE = -100            # set-table.PREP_SEQ_BASE: set_seq <= this is a prep drill


def _script(name):
    """Import an extensionless engine script (rx-calc, set-table) as a module."""
    if name not in _MODS:
        path = os.path.join(HERE, name)
        mod_name = name.replace("-", "_")
        spec = importlib.util.spec_from_loader(
            mod_name, importlib.machinery.SourceFileLoader(mod_name, path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        _MODS[name] = mod
    return _MODS[name]


def _session_date(db_path, sid):
    try:
        conn = sqlite3.connect(db_path)
        try:
            row = conn.execute("SELECT date FROM workouts WHERE id = ?", (int(sid),)).fetchone()
        finally:
            conn.close()
        return row[0] if row else None
    except Exception:  # noqa: BLE001
        return None


# ---------------------------------------------------------------------------
# the plan
# ---------------------------------------------------------------------------
def _ramp_warmups(db_path, ex, kg):
    """Warm-up rows for a lift as the ledger wants them: {kg, reps, seq}. seq is
    the DB set_seq set-add writes (empty-bar primer 0, ramp N = -N)."""
    try:
        st = _script("set-table")
        rows = st.planned_ramp_rows(db_path, ex["name"], kg, slot=ex)
    except Exception:  # noqa: BLE001
        return []
    out = []
    for i, r in enumerate(rows or []):
        label = str(r.get("label") or "")
        m = re.match(r"r(\d+)$", label)
        seq = 0 if label == "bw" else (-int(m.group(1)) if m else -(i + 1))
        out.append({"kg": float(r["weight_kg"]), "reps": int(r.get("reps") or 5), "seq": seq})
    return out


_FIRST_KG = {"barbell": 20.0, "dumbbell": 4.0, "stack": 10.0}


def _prescribe(db_path, sid, rx, ex, kind):
    """A conservative start weight for a lift with none on file: the engine
    proposes, it never asks (owner 2026-10-12). Estimate from related lifts,
    else the load's natural zero, else a per-implement floor. (kg, True)."""
    try:
        import live_load as LL
        name = ex["name"]
        view = LL.view(rx, ex, db_path, sid, name)
        est = LL.estimate(rx, view, db_path, sid, name, variant=view.get("_variant"))
        if est and est.get("kg"):
            return float(est["kg"])
        zero, _k = LL.natural_zero(rx, view, db_path, sid, name)
        if zero:
            return float(zero)
    except Exception:  # noqa: BLE001
        pass
    return _FIRST_KG.get(kind, 0.0)


def lift_entry(db_path, program, ex, rx=None, sid=None, program_dict=None):
    """One ledger plan entry from an rx-calc exercise dict."""
    import implement
    rx = rx or _script("rx-calc")
    name = ex["name"]
    kind = implement.kind_of(db_path, name, ex)
    rr = ex.get("rep_range") or []
    try:
        reps = int(rr[-1]) if rr else 8
    except (TypeError, ValueError):
        reps = 8
    kg = ex.get("weight_kg")
    rest = None
    try:
        prog = program_dict if program_dict is not None else rx.load_yaml(program)
        rest = int(rx.resolve_rest_sec(ex, prog, rx.get_fatigue_cost_map(db_path),
                                       rx.get_pattern_map(db_path))[0])
    except Exception:  # noqa: BLE001
        rest = None
    step = None
    try:
        step = rx._lattice_step(rx.resolve_lattice(ex, db_path, sid))
    except Exception:  # noqa: BLE001
        step = None
    ent = {"name": name, "display": ex.get("display") or name, "kind": kind,
           "slot": ex.get("slot"), "sets": int(ex.get("sets") or 3), "reps": reps,
           "kg": float(kg) if kg else 0.0, "rest_sec": rest or F.DEFAULT_REST_SEC}
    if step:
        ent["step"] = float(step)
    if not kg and kind in _FIRST_KG:
        first = _prescribe(db_path, sid, rx, ex, kind)
        if first:
            ent["kg"], ent["est"] = first, True
    if kg and kind in (implement.BARBELL, implement.DUMBBELL, implement.STACK):
        ent["warmups"] = _ramp_warmups(db_path, ex, float(kg))
    return ent


def build_plan(sid, db_path, program, split=None, free=False):
    """{split, free, lifts:[entry]} from rx-calc + the program. A free session
    starts with no lifts: each is added when it is entered."""
    plan = {"split": split, "free": bool(free), "lifts": []}
    if free:
        return plan
    rx = _script("rx-calc")
    date = _session_date(db_path, sid)
    from free_session import effective_path
    eff = effective_path(program, db_path, int(sid))     # the frozen day snapshot
    try:
        result = rx.calc_rx(eff, date, db_path, int(sid), hydrate=False, split=split)
    except SystemExit:                  # SplitRefused et al.: plan by the queue answer
        result = rx.calc_rx(eff, date, db_path, int(sid), hydrate=False)
    program = eff
    prog = rx.load_yaml(program)
    plan["split"] = result.get("rotation_day") or split
    for ex in result.get("exercises") or []:
        plan["lifts"].append(lift_entry(db_path, program, ex, rx, sid, prog))
    return plan


def start_ledger(sid, db_path, program, split=None, free=False):
    """Start the session's ledger (compute only, no post). Returns True when a
    ledger exists afterwards. A session that already has one is left alone."""
    if F.load(sid) is not None:
        return True
    plan = build_plan(sid, db_path, program, split=split, free=free)
    plan["env"] = {"db": os.path.abspath(db_path), "program": os.path.abspath(program)}
    F.locked_step(sid, "start", plan)
    return True


def ensure_lift(sid, name, db_path, program):
    """Make sure the ledger plan holds `name` (free session, late addition)."""
    st = F.load(sid)
    if st is None or name in st["plan"]:
        return
    ent = None
    try:
        rx = _script("rx-calc")
        from free_session import effective_path
        eff = effective_path(program, db_path, int(sid))
        result = rx.calc_rx(eff, _session_date(db_path, sid), db_path, int(sid), hydrate=False)
        for ex in result.get("exercises") or []:
            if ex["name"] == name:
                ent = lift_entry(db_path, eff, ex, rx, sid)
    except Exception:  # noqa: BLE001
        ent = None
    if ent is None:
        import implement
        ent = {"name": name, "display": name, "kind": implement.kind_of(db_path, name),
               "sets": 3, "reps": 8, "kg": 0.0, "rest_sec": F.DEFAULT_REST_SEC}
    F.add_lifts(sid, [ent])


# ---------------------------------------------------------------------------
# posting
# ---------------------------------------------------------------------------
def _table_from_set_table(sid, name, db_path, program, est_kg=None):
    """The ONE renderer: set-table's owner-surface table for this lift."""
    try:
        argv = [os.path.join(HERE, "set-table"), str(sid), name, "--db", db_path,
                "--program", program, "--surface", "owner"]
        if est_kg:
            argv += ["--est-weight", repr(float(est_kg))]
        p = subprocess.run([sys.executable] + argv, capture_output=True, text=True, timeout=60)
        out = (p.stdout or "").strip()
        return out if p.returncode == 0 and out else None
    except Exception:  # noqa: BLE001
        return None


def post(sid, frame, db_path=None, program=None, quiet=True):
    """Swap in set-table's table (when it renders), then emit.post. Returns the
    receipt. Receipt lines go to stderr when `quiet` (the verbs' stdout contracts
    are not ours to extend)."""
    import emit
    env = (F.load(sid) or {}).get("env") or {}
    db_path = db_path or env.get("db")
    program = program or env.get("program")
    if frame.get("table") and frame.get("lift") and db_path and program:
        ent = ((F.load(sid) or {}).get("plan") or {}).get(frame["lift"]) or {}
        est_kg = ent.get("kg") if ent.get("est") else None
        t = _table_from_set_table(sid, frame["lift"], db_path, program, est_kg)
        if t:
            frame = dict(frame)
            frame["table"] = t
    receipt = emit.post(frame, sid)
    lines = emit.stdout_lines(receipt, frame)
    print("\n".join(lines), file=sys.stderr if quiet else sys.stdout)
    return receipt


def _step_and_post(sid, event, args, db_path=None, program=None, post_it=True):
    frame = F.locked_step(sid, event, args)
    if post_it:
        post(sid, frame, db_path, program)
    return frame


# ---------------------------------------------------------------------------
# verb hooks
# ---------------------------------------------------------------------------
def post_prep_card(sid, name, table, card, argv, seq, button, near, db_path, program):
    """One prep drill's card on the ledger: the prep table, then the drill (title
    outside, the cue quoted) with its done button; the button's tap runs `argv`
    (the drill's literal set-add) with no model turn. Returns the receipt."""
    if F.load(sid) is None:
        return None
    frame = F.locked_step(sid, "prep", {"lift": name, "argv": list(argv), "seq": seq,
                                        "table": table, "card": list(card),
                                        "button": button, "near": list(near or [])})
    return post(sid, frame, db_path, program)


def prep_owed_card(sid, name, db_path, program):
    """Post the lift's first owed ENTRY prep drill as a ledger card. True when a
    card went out (the lift's entry waits for the drills); False when no entry
    prep is owed. The one place that decides it is set-arm's prep gate."""
    try:
        argv = [sys.executable, os.path.join(HERE, "set-arm"), "prep-card", str(sid), name,
                "--db", db_path, "--program", program]
        p = subprocess.run(argv, capture_output=True, text=True, timeout=120)
        return "PREP_TAP_POSTED" in (p.stdout or "")
    except Exception:  # noqa: BLE001
        return False


def on_enter(sid, name, db_path, program, post_it=True):
    """exercise-enter: the lift's entry screen. A lift already entered (ledger
    lift == name) is not re-entered: re-running exercise-enter posts nothing."""
    st = F.load(sid)
    if st is None:
        return None
    env = st.get("env") or {}
    db_path = db_path or env.get("db")
    program = program or env.get("program")
    ensure_lift(sid, name, db_path, program)
    st = F.load(sid)
    if st.get("lift") == name or name in st["closed"]:
        return None
    return _step_and_post(sid, "enter", {"lift": name}, db_path, program, post_it)


def on_set_added(sid, name, set_seq, reps, weight, rir, db_path, program):
    """set-add: the set is committed; log it on the ledger and post the next
    screen. Rows that are not a lift's set (session-level prep, drills) are
    ignored by the caller."""
    st = F.load(sid)
    if st is None or int(set_seq) <= PREP_SEQ_BASE:     # a prep drill is the prep card's, not a lift's set
        return None
    ensure_lift(sid, name, db_path, program)
    st = F.load(sid)
    if name in st["closed"]:
        return None
    if st.get("lift") != name or st["state"] in (F.S1, F.S2, F.S6, F.S7):
        # set-add on a lift the owner never "entered" through the ledger (the
        # agent logged a set directly): enter silently -- the set's own frame is
        # the screen, an entry card after the fact would only be noise.
        F.locked_step(sid, "enter", {"lift": name})
        st = F.load(sid)
    kind = "working" if int(set_seq) >= 1 else "warmup"
    args = {"lift": name, "kind": kind, "seq": int(set_seq), "reps": reps}
    if weight is not None:
        args["kg"] = float(weight)
    if rir is not None:
        args["rir"] = int(rir)
    return _step_and_post(sid, "set_logged", args, db_path, program)


def on_set_removed(sid, name, set_seq, db_path=None, program=None):
    """set-undo: the DB row is gone -- drop it from the ledger and post the
    current screen (table -> card -> the one live keyboard). Returns True when
    the ledger took over the screen (the old undo keyboard stands down)."""
    st = F.load(sid)
    if st is None or name not in st["plan"]:
        return False
    frame = F.locked_step(sid, "undo", {"lift": name, "seq": int(set_seq)})
    if frame.get("card"):
        post(sid, frame, db_path, program)
        return True
    return False


# ---------------------------------------------------------------------------
# taps
# ---------------------------------------------------------------------------
def parse_callback(data):
    parts = str(data).split("|", 4)
    if len(parts) < 4 or parts[0] != "flow":
        return None
    return {"sid": parts[1], "ver": int(parts[2]), "event": parts[3],
            "arg": parts[4] if len(parts) > 4 else ""}


def _run_set_add(sid, st, name, seq, reps, kg, rir):
    ent = (st["plan"].get(name) or {})
    env = st.get("env") or {}
    argv = [sys.executable, os.path.join(HERE, "set-add"), str(sid), name,
            str(ent.get("slot") if ent.get("slot") is not None else "session"),
            str(seq), str(reps)]
    if kg:
        argv += ["--weight", str(kg)]
    if rir is not None:
        argv += ["--rir", str(rir)]
    if env.get("db"):
        argv += ["--db", env["db"]]
    if env.get("program"):
        argv += ["--program", env["program"]]
    return subprocess.run(argv, capture_output=True, text=True, timeout=180)


def _run_prep(sid, st, arg):
    """The prep done button: run the drill's stored set-add argv. A nearby-weight
    tap (`arg` = kg) records that weight instead of the prescribed one."""
    prep = st["prep"]
    argv = list(prep["argv"])
    if arg:
        if "--weight" in argv:
            i = argv.index("--weight")
            argv[i + 1] = str(arg)
        else:
            argv += ["--weight", str(arg)]
    env = st.get("env") or {}
    cmd = [sys.executable, os.path.join(HERE, "set-add")] + argv
    if env.get("db"):
        cmd += ["--db", env["db"]]
    if env.get("program"):
        cmd += ["--program", env["program"]]
    return subprocess.run(cmd, capture_output=True, text=True, timeout=180)


def tap(data):
    """Route one flow button. Returns a process exit code (0 ok, 2 refused)."""
    cb = parse_callback(data)
    if cb is None:
        print("FLOW_REFUSED code=bad_callback detail=%s" % data)
        return 2
    sid = cb["sid"]
    st = F.load(sid)
    if st is None:
        print("FLOW_REFUSED code=no_session detail=%s" % sid)
        return 2
    env = st.get("env") or {}
    try:
        if cb["event"] == "prep" and cb["ver"] == st["version"] and st.get("prep"):
            p = _run_prep(sid, st, cb["arg"])
            if p.returncode != 0:
                print("FLOW_REFUSED code=set_add_failed detail=%s" % (p.stderr or p.stdout)[-200:])
                return 2
            print("FLOW_TAP_LOGGED prep seq=%s" % st["prep"]["seq"])
            return 0
        if (cb["ver"] == st["version"] and cb["event"] in ("enter", "next_lift")
                and (cb["arg"] or None) and env.get("db") and env.get("program")
                and prep_owed_card(sid, cb["arg"], env["db"], env["program"])):
            print("FLOW_TAP_PREP lift=%s" % cb["arg"])
            return 0
        if cb["ver"] == st["version"] and cb["event"] == "rir" and st.get("pending"):
            name = st["lift"]
            nxt = F.decide(st, name)
            reps = st["pending"]["reps"]
            seq = nxt["seq"] if nxt["kind"] == "working" else -nxt["seq"]
            p = _run_set_add(sid, st, name, seq, reps, nxt["kg"], int(cb["arg"]))
            if p.returncode != 0:
                print("FLOW_REFUSED code=set_add_failed detail=%s" % (p.stderr or p.stdout)[-200:])
                return 2
            print("FLOW_TAP_LOGGED lift=%s seq=%s" % (name, seq))
            return 0
        if cb["ver"] == st["version"] and cb["event"] == "set_logged" and cb["arg"].startswith("w:"):
            name = st["lift"]
            nxt = F.decide(st, name)
            _w, kg, reps = cb["arg"].split(":")
            ent = st["plan"][name]
            seqs = [w.get("seq") for w in ent.get("warmups") or []]
            idx = nxt["seq"] - 1
            seq = seqs[idx] if idx < len(seqs) and seqs[idx] is not None else -nxt["seq"]
            p = _run_set_add(sid, st, name, seq, int(reps), float(kg), None)
            if p.returncode != 0:
                print("FLOW_REFUSED code=set_add_failed detail=%s" % (p.stderr or p.stdout)[-200:])
                return 2
            print("FLOW_TAP_LOGGED lift=%s seq=%s" % (name, seq))
            return 0
        frame = F.locked_step(sid, "tap", {"ver": cb["ver"], "event": cb["event"], "arg": cb["arg"]})
    except F.FlowError as exc:
        print("FLOW_REFUSED code=%s detail=%s" % (exc.code, exc.detail))
        return 2
    import emit
    receipt = post(sid, frame, env.get("db"), env.get("program"), quiet=False)
    return 0 if receipt else 0
