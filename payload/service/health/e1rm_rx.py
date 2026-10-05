#!/usr/bin/env python3
"""e1rm_rx.py -- e1RM-based prescription when the data is sufficient.

OWNER RULING 2026-09-30. This REPLACES the 2026-07-28 batch exclusion ("no
prescription or coaching logic is derived from e1RM"). The old rule made the
working load an estimate of an estimate: last prescription -> today's
prescription -> warm-up as a % of that. When the working load was set low
(B22: 21.25 kg prescribed, 27.25 kg x15 @RIR4+ actually done) the warm-up was
doubly low, and when the load did go up the rep target stayed pinned (B7).

    SUFFICIENT   working sets with weight+reps in >= min_sessions distinct
                 sessions -> the prescription comes from the observed e1RM:
                 working load back-solved from e1RM, target reps and target
                 RIR; the rep target is recomputed at the ROUNDED load; the
                 warm-up rungs are % of e1RM.
    INSUFFICIENT anything less -> rx-calc's last-load progression, unchanged.

Every tunable is in e1rm_rx_rules.json (same pattern as compose_rank_rules.json);
this file only carries the arithmetic. stdlib only, no rx-calc import (rx-calc
imports THIS), so the rounding functions are handed in by the caller.

Formula (per set):
    RIR known   e1rm = w * (1 + (reps + rir) / 30)    basis 'epley_rir'
    RIR absent  e1rm = w * (1 + reps / 30)            basis 'epley_reps'
The second is Epley on the reps actually done. It equals rir=0 numerically but
is NOT a claim that the set went to failure -- it is a lower bound, no default
RIR is imputed, and each estimate reports how many of its sessions were RIR-known.

OWNER RULING 2026-09-30 13:28 -- filter the history, then re-measure once.
Measured on the owner's history, median-of-3 put 12/24 lifts below the load
last lifted. The owner rejected "follow the newest peak" and ruled instead:
    1. bad-condition / early-stop sessions never feed the estimate
       (session_exclusion: a structured flag first, the note text as the
       legacy fallback -- keywords in rules, not code);
    2. a set that stopped AT the rep-range top is a LOWER BOUND, not a
       measurement: it counts toward sufficiency but can only raise the
       estimate (censored_statistic);
    3. the first e1RM-basis session opens with a CHECK SET (rx_basis.measure):
       the back-solved load, open reps to RIR 1-2. Its e1RM is the lift's
       ANCHOR and supersedes the older window from then on (find_anchor --
       derived from a dated cutover in rules, no schema change).

PER MACHINE (ticket 2026-09-30 per-machine cable lattice, kit 062). Two cable
machines with different pin stacks are two lifts as far as the estimate goes:
    * a CONFIRMED machine (chosen this session, or the machine of the newest
      logged set -- never a static ax_exercise binding) scopes the history to
      the sets logged on it (workout_sets.machine_ref). Unattributed history
      (machine_ref NULL, everything before 062) is never assigned to a machine;
    * the first trusted session on a machine is ITS anchor: that session's
      first working set was the check set;
    * a machine with no trusted session yet CALIBRATES: today's first working
      set is a check set (measure=true). The load it starts from is the pooled
      estimate of the other history, read as a seed only, and labelled so.
    machine_estimate() is that rule; estimate(machine=None) is unchanged.
"""

import json
import math
import os
import sqlite3
import statistics

HERE = os.path.dirname(os.path.abspath(__file__))
RULES_PATH = os.path.join(HERE, "e1rm_rx_rules.json")

BASIS_E1RM = "e1rm"                 # emitted rx_basis.basis on the e1RM path
BASIS_PROGRESSION = "progression"   # emitted rx_basis.basis on the fallback

_RULES = None


def load_rules(path=None):
    """The rules document (memoized for the default path)."""
    global _RULES
    if path is None and _RULES is not None:
        return _RULES
    with open(path or RULES_PATH, encoding="utf-8") as fh:
        rules = json.load(fh)
    if path is None:
        _RULES = rules
    return rules


# ---------------------------------------------------------------------------
# Per-set arithmetic
# ---------------------------------------------------------------------------
def set_e1rm(weight, reps, rir=None):
    """(e1rm, basis) for one set. See the module docstring for the two bases."""
    if rir is None:
        return weight * (1 + reps / 30.0), "epley_reps"
    return weight * (1 + (reps + rir) / 30.0), "epley_rir"


def backsolve_load(e1rm, reps, rir):
    """The load that leaves `rir` in reserve after `reps` at this e1RM."""
    return e1rm / (1 + (reps + rir) / 30.0)


def reps_at(load, e1rm, rir):
    """Whole reps doable at `load` while keeping `rir` in reserve (>= 0)."""
    if not load or load <= 0:
        return 0
    return max(0, int(math.floor(30.0 * (e1rm / load - 1.0) - rir + 1e-9)))


# ---------------------------------------------------------------------------
# Observation read
# ---------------------------------------------------------------------------
def _has_set_kind(conn):
    return "set_kind" in {r[1] for r in
                          conn.execute("PRAGMA table_info(workout_sets)")}


def _has_machine_col(conn):
    return "machine_ref" in {r[1] for r in
                             conn.execute("PRAGMA table_info(workout_sets)")}


def _workout_cols(conn):
    return {r[1] for r in conn.execute("PRAGMA table_info(workouts)")}


# ---------------------------------------------------------------------------
# History filter 1 -- untrustworthy SESSIONS (owner ruling 2026-09-30 13:28)
# ---------------------------------------------------------------------------
def session_exclusion(session, rules=None):
    """THE predicate: why this session must not feed the estimate, or None.

    `session` is {"note": str|None, "flag": value|None}. `flag` is the value of
    the structured column rules condition.flag_column names (None when the kit
    has no such column yet, or the row left it NULL).

      1. flag present -> it is AUTHORITATIVE: excluded iff the value is in
         condition.flag_excluded ('flag:<value>'); the note is not read.
      2. flag absent  -> LEGACY fallback: workouts.note free text matched
         against condition.note_keywords ('note:<keyword>').

    The keyword list lives in e1rm_rx_rules.json, never here. When the kit
    lands the column, every newly written row carries a flag and the note
    match silently becomes the fallback for the pre-column history only."""
    rules = rules or load_rules()
    cond = rules.get("condition") or {}
    flag = (session or {}).get("flag")
    if flag is not None and str(flag).strip() != "":
        flag = str(flag).strip()
        return ("flag:%s" % flag
                if flag in set(cond.get("flag_excluded") or []) else None)
    note = (session or {}).get("note") or ""
    squashed = "".join(note.split())
    for kw in cond.get("note_keywords") or []:
        # whitespace-insensitive: '조기 종료' and '조기종료' are one keyword
        if kw and "".join(kw.split()) in squashed:
            return "note:%s" % kw
    return None


# ---------------------------------------------------------------------------
# History filter 2 -- sets that stopped AT the rep ceiling are LOWER BOUNDS
# ---------------------------------------------------------------------------
def rep_ceiling(rep_range, rules=None):
    """The rep count at/above which a set is a lower bound (censored), or None
    when the slot has no usable range or censoring is off."""
    rules = rules or load_rules()
    cen = rules.get("censor") or {}
    if cen.get("treatment", "none") == "none":
        return None
    if not (isinstance(rep_range, (list, tuple)) and len(rep_range) == 2):
        return None
    try:
        return int(rep_range[1])
    except (TypeError, ValueError):
        return None


def _stat(vals, stat):
    if stat == "median":
        return statistics.median(vals)
    if stat == "max":
        return max(vals)
    if stat == "mean":
        return sum(vals) / len(vals)
    raise ValueError("e1rm_rx_rules: unknown estimate.statistic %r" % stat)


def censored_statistic(points, stat, rules=None):
    """The window statistic with censored points treated as lower bounds.

    treatment 'raise_only' (see rules censor._why): the statistic runs over the
    MEASURED (uncensored) points; a censored point can only RAISE the result --
    it replaces it when it is higher (capacity is at least that), and is simply
    dropped when it is lower (a lower bound below the measurements says
    nothing). A window of censored points only -> the highest lower bound.
    treatment 'none' -> the plain statistic over every point (7dbaff1)."""
    rules = rules or load_rules()
    treat = (rules.get("censor") or {}).get("treatment", "none")
    vals = [p["e1rm"] for p in points]
    if treat == "none":
        return _stat(vals, stat)
    if treat != "raise_only":
        raise ValueError("e1rm_rx_rules: unknown censor.treatment %r" % treat)
    meas = [p["e1rm"] for p in points if not p.get("censored")]
    lows = [p["e1rm"] for p in points if p.get("censored")]
    if not meas:
        return max(lows)
    return max([_stat(meas, stat)] + lows)


def session_points(db_path, exercise_name, exclude_session_id=None,
                   rep_range=None, rules=None, keep_excluded=False,
                   machine=None):
    """One point per session that has a usable WORKING set for this exercise,
    newest first: {session_id, date, weight_kg, reps, rir, e1rm, basis,
    censored, excluded, first}.

    Usable working set = set_seq >= 1 (ramps/prep sit at <= 0), set_kind
    'working' where the column exists, weight_kg > 0 and reps > 0. The point is
    the session TOP SET (heaviest, then most reps, then an RIR-known set, then
    the larger RIR) -- the same top-set rule as the set-table trend, with the
    ties it left to row order broken deterministically.

    2026-09-30 13:28 additions (all additive):
      excluded  session_exclusion() reason or None. Excluded sessions are
                DROPPED unless keep_excluded (the estimate wants them only to
                report what it skipped).
      censored  the top set's reps reached the rep ceiling (rep_range top):
                a lower bound, see censored_statistic().
      first     the session's FIRST working set {set_seq, weight_kg, reps, rir,
                e1rm, basis} -- the re-measure set when this is the anchor.

    `machine` (kit 062): only the sets logged on that ax_machine ulid. A DB
    without workout_sets.machine_ref has no set on any machine -> []."""
    rules = rules or load_rules()
    ceiling = rep_ceiling(rep_range, rules)
    flag_col = (rules.get("condition") or {}).get("flag_column")
    try:
        conn = sqlite3.connect(db_path)
    except sqlite3.Error:
        return []
    try:
        where = ["ws.exercise_name = ?", "ws.set_seq >= 1",
                 "ws.weight_kg IS NOT NULL", "ws.weight_kg > 0",
                 "ws.reps > 0"]
        params = [exercise_name]
        if _has_set_kind(conn):
            where.append("ws.set_kind = 'working'")
        if machine is not None:
            if not _has_machine_col(conn):
                return []
            where.append("ws.machine_ref = ?")
            params.append(machine)
        if exclude_session_id is not None:
            where.append("ws.session_id != ?")
            params.append(exclude_session_id)
        cols = _workout_cols(conn)
        note_sql = "w.note" if "note" in cols else "NULL"
        flag_sql = ("w.%s" % flag_col
                    if flag_col and flag_col.isidentifier()
                    and flag_col in cols else "NULL")
        rows = conn.execute(
            "SELECT ws.session_id, w.date, w.created_at, ws.weight_kg, "
            "ws.reps, ws.rir, ws.set_seq, " + note_sql + ", " + flag_sql +
            " FROM workout_sets ws "
            "JOIN workouts w ON w.id = ws.session_id WHERE "
            + " AND ".join(where), params).fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()
    by_session = {}
    firsts = {}
    for sid, date, created, w, reps, rir, seq, note, flag in rows:
        key = (w, reps, rir is not None, rir if rir is not None else 0)
        cur = by_session.get(sid)
        if cur is None or key > cur[0]:
            by_session[sid] = (key, date, created, w, reps, rir, note, flag)
        if sid not in firsts or seq < firsts[sid][0]:
            firsts[sid] = (seq, w, reps, rir)
    points = []
    for sid, (_k, date, created, w, reps, rir, note, flag) in by_session.items():
        why = session_exclusion({"note": note, "flag": flag}, rules)
        if why is not None and not keep_excluded:
            continue
        e, basis = set_e1rm(float(w), int(reps), rir)
        fseq, fw, freps, frir = firsts[sid]
        fe, fbasis = set_e1rm(float(fw), int(freps), frir)
        points.append({"session_id": sid, "date": date, "created_at": created,
                       "weight_kg": float(w), "reps": int(reps), "rir": rir,
                       "e1rm": e, "basis": basis,
                       "censored": bool(ceiling is not None
                                        and int(reps) >= ceiling),
                       "excluded": why,
                       "first": {"set_seq": fseq, "weight_kg": float(fw),
                                 "reps": int(freps), "rir": frir,
                                 "e1rm": fe, "basis": fbasis}})
    points.sort(key=lambda p: (p["date"] or "", p["created_at"] or "",
                               p["session_id"]), reverse=True)
    return points


def _measure_point(p):
    """The anchor session's point: its FIRST working set (the re-measure set,
    open reps to RIR 1-2), never censored -- the reps were not capped."""
    f = p["first"]
    return {"session_id": p["session_id"], "date": p["date"],
            "created_at": p["created_at"], "weight_kg": f["weight_kg"],
            "reps": f["reps"], "rir": f["rir"], "e1rm": f["e1rm"],
            "basis": f["basis"], "censored": False, "excluded": None,
            "measure": True}


def find_anchor(trusted_oldest_first, need, rules=None):
    """The re-measure ANCHOR session among trusted points, or None.

    DERIVED FROM DATA, no stored flag: the first trusted session dated on/after
    rules remeasure.cutover that had >= `need` trusted sessions before it. From
    the cutover on, every eligible lift with >= `need` trusted sessions is
    prescribed on the e1RM basis with measure=true, so that session is by
    construction the one whose first working set was the check set. A session
    later marked bad/early-stop is not trusted, so the NEXT session becomes the
    measurement -- the flag re-fires until a trusted one exists."""
    rules = rules or load_rules()
    rm = rules.get("remeasure") or {}
    if not rm.get("enabled"):
        return None
    cut = rm.get("cutover") or ""
    for i, p in enumerate(trusted_oldest_first):
        if (p["date"] or "") >= cut and i >= need:
            return p
    return None


def estimate(db_path, exercise_name, exclude_session_id=None, rules=None,
             rep_range=None, today=None, machine=None):
    """The exercise's e1RM estimate and whether it is SUFFICIENT.

    {sufficient, sessions, e1rm (None when insufficient), statistic,
     window: [{date, weight_kg, reps, rir, e1rm, basis, censored}], rir_known,
     excluded: [{date, reason}], censored, measure, anchor}

    Owner ruling 2026-09-30 13:28, on top of 7dbaff1:
      * sessions session_exclusion() flags never count (sufficiency or window)
      * censored points (reps at the rep ceiling) count toward sufficiency but
        can only raise the statistic (censored_statistic)
      * RE-MEASURE: no anchor yet + sufficient -> measure=True (today's first
        working set is a check set). An anchor (find_anchor) supersedes the
        older window: the estimate is then the anchor's measure set plus the
        trusted sessions after it. With rules remeasure.same_session, a check
        set already logged in the OPEN session (exclude_session_id) is today's
        anchor, so the remaining sets follow the fresh measurement.

    `machine` (kit 062): the history is the sets logged on that machine only,
    and the anchor is the machine's FIRST trusted session (the calibration
    check set, see machine_estimate) -- no cutover, no min_sessions before it.
    With no trusted session on it the result is insufficient (sessions 0)."""
    rules = rules or load_rules()
    need = int(rules["sufficiency"]["min_sessions"])
    n_win = int(rules["estimate"]["window_sessions"])
    stat = rules["estimate"]["statistic"]
    rm = rules.get("remeasure") or {}
    every = session_points(db_path, exercise_name, None, rep_range, rules,
                           keep_excluded=True, machine=machine)
    open_pt = None
    if exclude_session_id is not None:
        for p in every:
            if p["session_id"] == exclude_session_id:
                open_pt = p
        every = [p for p in every if p["session_id"] != exclude_session_id]
    pts = [p for p in every if p["excluded"] is None]
    out = {"sufficient": len(pts) >= need, "sessions": len(pts),
           "min_sessions": need, "e1rm": None, "statistic": stat,
           "window": [], "rir_known": 0, "excluded": [], "censored": 0,
           "measure": False, "anchor": None}
    if machine is not None:
        anchor = pts[-1] if pts else None
    else:
        anchor = find_anchor(list(reversed(pts)), need, rules)
    if anchor is not None:
        win = [p for p in pts if p is not anchor and
               (p["date"], p["created_at"] or "", p["session_id"])
               > (anchor["date"], anchor["created_at"] or "",
                  anchor["session_id"])]
        win = (win + [_measure_point(anchor)])[:n_win]
        out["sufficient"] = True
        out["anchor"] = {"date": anchor["date"], "source": "history"}
    elif (machine is not None and rm.get("same_session")
          and open_pt is not None and open_pt["excluded"] is None):
        # the machine's calibration check set is already logged today: the
        # rest of today's sets follow it.
        win = [_measure_point(open_pt)]
        out["sufficient"] = True
        out["anchor"] = {"date": open_pt["date"], "source": "open_session"}
    elif machine is not None:
        return out
    elif (out["sufficient"] and rm.get("enabled") and rm.get("same_session")
          and open_pt is not None and open_pt["excluded"] is None
          and (open_pt["date"] or "") >= (rm.get("cutover") or "")):
        win = [_measure_point(open_pt)]
        out["anchor"] = {"date": open_pt["date"], "source": "open_session"}
    elif not out["sufficient"]:
        return out
    else:
        win = pts[:n_win]
        out["measure"] = bool(rm.get("enabled")
                              and (today is None
                                   or today >= (rm.get("cutover") or "")))
    value = censored_statistic(win, stat, rules)
    oldest = min((p["date"] or "") for p in win)
    lifted_by = None
    if (rules.get("condition") or {}).get("treatment", "drop") == "raise_only":
        # An excluded (bad-condition / early-stop) session inside the window
        # span is a LOWER BOUND: it can raise the estimate, never lower it.
        for p in every:
            if (p["excluded"] is not None and (p["date"] or "") >= oldest
                    and p["e1rm"] > value):
                value, lifted_by = p["e1rm"], p["date"]
    out["condition_raised_by"] = lifted_by
    out["e1rm"] = round(value, 2)
    out["window"] = [{k: p[k] for k in ("date", "weight_kg", "reps", "rir",
                                        "basis", "censored")}
                     | {"e1rm": round(p["e1rm"], 2)}
                     | ({"measure": True} if p.get("measure") else {})
                     for p in win]
    out["rir_known"] = sum(1 for p in win if p["rir"] is not None)
    out["censored"] = sum(1 for p in win if p["censored"])
    out["excluded"] = [{"date": p["date"], "reason": p["excluded"]}
                       for p in every
                       if p["excluded"] is not None
                       and (p["date"] or "") >= oldest]
    return out


def machine_rules(rules=None):
    rules = rules or load_rules()
    return rules.get("machine") or {}


def machine_estimate(db_path, exercise_name, exclude_session_id=None,
                     machine=None, rules=None, rep_range=None, today=None):
    """estimate() for the machine this lift runs on today.

    machine None (a free-weight lift, an unconfirmed machine, a pre-062 DB) or
    rules machine.enabled false -> estimate() exactly as before.
    Otherwise the result carries `machine` {ulid, state, seed_sessions}:
      state 'own'        the machine's own history (or today's check set on
                         it) answers; see estimate(machine=...).
      state 'calibrate'  nothing trusted on this machine yet. The pooled
                         estimate of the rest of the history is the SEED
                         (sufficient or not, exactly as estimate() reads it),
                         measure is forced on and the anchor cleared: today's
                         first working set is this machine's check set."""
    rules = rules or load_rules()
    if machine is None or not machine_rules(rules).get("enabled"):
        return estimate(db_path, exercise_name, exclude_session_id, rules,
                        rep_range=rep_range, today=today)
    own = estimate(db_path, exercise_name, exclude_session_id, rules,
                   rep_range=rep_range, today=today, machine=machine)
    if own["sufficient"]:
        own["machine"] = {"ulid": machine, "state": "own",
                          "seed_sessions": None}
        return own
    seed = estimate(db_path, exercise_name, exclude_session_id, rules,
                    rep_range=rep_range, today=today)
    seed["measure"] = bool(seed["sufficient"])
    seed["anchor"] = None
    seed["machine"] = {"ulid": machine, "state": "calibrate",
                       "seed_sessions": seed["sessions"]}
    return seed


# ---------------------------------------------------------------------------
# Eligibility and prescription
# ---------------------------------------------------------------------------
def eligible(ex):
    """Slots the e1RM path may prescribe. Everything else keeps the fallback:
      * progression 'hold' (rehab/maintenance -- the slot weight is inviolable)
      * assisted slots (weight_kg is a counterweight; Epley does not apply)
      * no 2-element numeric rep_range (holds in seconds, malformed ranges)"""
    if not isinstance(ex, dict):
        return False
    if ex.get("progression", "double") == "hold" or ex.get("assisted"):
        return False
    rr = ex.get("rep_range")
    if not (isinstance(rr, (list, tuple)) and len(rr) == 2):
        return False
    try:
        lo, hi = int(rr[0]), int(rr[1])
    except (TypeError, ValueError):
        return False
    return 0 < lo <= hi


def backsolve_rir(target_rir, rules=None):
    """R for the back-solve: the band end rules backsolve.rir names (band_low:
    the floor-respecting low end; band_high: the more-reserve end), or rules
    rir_default when the slot has no band."""
    rules = rules or load_rules()
    bs = rules["backsolve"]
    if isinstance(target_rir, (list, tuple)) and len(target_rir) == 2:
        return int(target_rir[1] if bs["rir"] == "band_high"
                   else target_rir[0])
    return int(bs["rir_default"])


def prescribe(ex, est, target_rir, round_fn, step_down_fn, rules=None):
    """(weight_kg, target_reps, detail) from a SUFFICIENT estimate, or None.

    round_fn(v)     -> v on the slot's available increments (rx-calc snap)
    step_down_fn(v) -> the next lower available load, or None at the floor
    None means "the e1RM path cannot answer" and the caller falls back."""
    rules = rules or load_rules()
    if not est or not est.get("sufficient") or not est.get("e1rm"):
        return None
    lo, hi = int(ex["rep_range"][0]), int(ex["rep_range"][1])
    t_reps = hi if rules["backsolve"]["reps"] == "range_top" else lo
    r = backsolve_rir(target_rir, rules)
    e = float(est["e1rm"])
    raw = backsolve_load(e, t_reps, r)
    load = round_fn(raw)
    if load is None or load <= 0:
        return None
    while reps_at(load, e, r) < lo:
        nxt = step_down_fn(load)
        if nxt is None or nxt <= 0 or nxt >= load:
            break
        load = nxt
    reps = min(hi, max(lo, reps_at(load, e, r)))
    detail = {"basis": BASIS_E1RM, "e1rm": est["e1rm"],
              "sessions": est["sessions"], "statistic": est["statistic"],
              "window": est["window"], "rir_known": est["rir_known"],
              "backsolve_reps": t_reps, "backsolve_rir": r,
              "raw_load": round(raw, 2),
              # 2026-09-30 13:28: the history filter and the re-measure.
              "censored": est.get("censored", 0),
              "excluded": est.get("excluded", []),
              "condition_raised_by": est.get("condition_raised_by"),
              "anchor": est.get("anchor"),
              "measure": bool(est.get("measure"))}
    if est.get("machine"):
        detail["machine"] = dict(est["machine"])
    if detail["measure"]:
        # today's FIRST working set is a check set at this load: open reps,
        # stop with this many reps left (rules remeasure.rir).
        detail["measure_rir"] = list(rules["remeasure"]["rir"])
    return round(load, 4), reps, detail


def ramp_loads(e1rm, rules=None):
    """Warm-up rung loads as % of e1RM, ascending, unsnapped."""
    rules = rules or load_rules()
    return [e1rm * float(p) for p in sorted(rules["ramp"]["pct_of_e1rm"])]


def ramp_e1rm(db_path, exercise_name, slot, exclude_session_id=None,
              rules=None, machine=None):
    """The e1RM a warm-up ladder should be cut from, or None (fallback ladder).
    Same eligibility + sufficiency gate as the working prescription, so the
    ladder switches exactly when the working load does."""
    if not eligible(slot or {}):
        return None
    try:
        est = machine_estimate(db_path, exercise_name, exclude_session_id,
                               machine, rules,
                               rep_range=(slot or {}).get("rep_range"))
    except Exception:  # noqa: BLE001 -- a ladder never breaks on the estimate
        return None
    return est["e1rm"] if est["sufficient"] else None
