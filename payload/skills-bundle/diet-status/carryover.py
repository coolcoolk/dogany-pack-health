#!/usr/bin/env python3
"""
Calorie CARRY-OVER: what the days already lived owe to the day being planned.

WHY.  The owner stated the gap verbatim (2026-09-10 17:11): "주간으로 칼로리
단백질 계산도맞지먼 오늘 단백[질 부족]하면 내일 더채우거나 오늘 칼로리
초과면 내일 덜먹는다거나 이런 기전이 없어".  2.15.0 + migration 046 gave the
week a JUDGEMENT (v_criterion / kcal-week): it can now say the week ran over.
A judgement is delivered after the fact, and the owner's ask is for a number
he can steer by BEFORE the next meal.  This module turns the same rows the
judgement reads into that number.  It opens no store and mints no constant --
every input is either already in `measure` or already declared in the goal's
own detail JSON.

THE RULE, AND WHY IT IS ASYMMETRIC.  The two directions are not mirrors:

  ate MORE than the days allowed  ->  CARRIED.  Under a recomp a surplus does
      not merely miss a target, it CANCELS the declared deficit -- the food is
      already eaten and the only place the balance can be recovered is the days
      that remain.  This is the same argument 046 uses to call a past-ceiling
      week 'surplus' at any coverage.

  ate LESS than the days allowed  ->  ERASED.  Fat loss is a function of the
      CUMULATIVE deficit, so a day that under-shot is not a debt the next day
      is owed -- it is simply a smaller number in the sum.  Paying it back
      would mean raising tomorrow's target on the strength of yesterday's
      restraint, which turns an eating plan into a ledger of credits.  So the
      carry is floored at zero and this module can only ever LOWER a target.

  ran a LARGE deficit  ->  NOT ASSERTED.  The energy-availability threshold
      that would make "you are under-eating" a factual claim is graded C /
      contested in the knowledge warehouse (the IOC consensus says of itself
      that it is guidance, not a diagnosis).  So `floor_pressure` is reported
      as a flag with the numbers behind it and NEVER as a verdict; the wording
      rule lives in SKILL.md, on the llm lane, because it is a wording call.

WHICH DAYS COUNT.  Only days BEFORE today whose record is 'complete' under the
kit's own under-logging guard (>= 3 distinct meal slots, _KCAL_DAY_MIN_SLOTS).
A partial or unlogged day is dropped from BOTH sides of the comparison -- its
intake and its target leave together -- because an unlogged day is a missing
RECORD, not missing food (046).  Dropping it from one side only is how a busy
Saturday manufactures either a debt or a windfall.  The count of dropped days
is reported, never swallowed.

FAIL-CLOSED, everywhere the inputs run out: no declared week boundary, no
active calorie rule, or a rule whose detail is missing a field -> no carry-over
and no sentence.  Silence, never a half-derived number.

Usage:
  carryover.py [--date YYYY-MM-DD] [--json]
Exit 0 always when the query itself succeeded; `applicable: false` carries the
"nothing to say" case so a caller never has to read an exit code as data.
"""
import argparse
import datetime
import importlib.util
import json
import os
import sys

# Skill dir; PROJECT_ROOT is three levels up. Same derivation as lookup.py /
# mealstate.py -- one idiom for the whole unit.
_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
LIFEKIT_PATH = os.path.join(_PROJECT_ROOT, "database", "kit_life.py")

_LIFEKIT = None


def kit_life():
    """Import the sibling kit_life SDK once, by path (lookup.py's idiom)."""
    global _LIFEKIT
    if _LIFEKIT is None:
        spec = importlib.util.spec_from_file_location("kit_life", LIFEKIT_PATH)
        if spec is None or spec.loader is None:
            raise ImportError("kit_life SDK not found: %s" % LIFEKIT_PATH)
        mod = importlib.util.module_from_spec(spec)
        sys.modules.setdefault("kit_life", mod)
        spec.loader.exec_module(mod)
        _LIFEKIT = mod
    return _LIFEKIT


# =========================================================================
# MIGRATION POINT -- kit mode.
#
# Everything below reads the kit directly (connected mode).  A standalone
# module would read the same shapes out of its own sidecar and the derivation
# would not change by one line, because the derivation only ever touches
# `measure` rows and the goal's declared detail.  kitmode.py holds the mode
# decision and the declared mimic version; see the MIGRATION POINT marker
# there for what a standalone->connected pour has to do.  v0.1 implements the
# connected side only, ON PURPOSE (see kitmode.py).
# =========================================================================


_GATE = None


def _gate_mod():
    """calorie_gate.py beside this file, imported once by path.

    Absent carrier -> None, and every caller treats that as "the check did not
    run", never as "the check passed". Same contract card.py uses."""
    global _GATE
    if _GATE is None:
        path = os.path.join(_HERE, "calorie_gate.py")
        # No bytecode: a __pycache__ inside the installed skill directory is
        # packaging residue (card.py's _sibling carries the full reason).
        _prev = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            spec = importlib.util.spec_from_file_location(
                "dietstatus_calorie_gate", path)
            if spec is None or spec.loader is None:
                return None
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            _GATE = mod
        except Exception:        # noqa: BLE001 -- reported, never swallowed
            return None
        finally:
            sys.dont_write_bytecode = _prev
    return _GATE


def _safety_gate(aim, rule, life):
    """(verdict, 0) for `aim` as today's base target.

    Every input is already in hand: the BMR and the declared deficit are fields
    of the owner's OWN rule detail (the same JSON 046 derives the weekly band
    from), and the sex is a config key. Nothing is invented and nothing is
    re-derived -- if a field is absent the matching limb reports `unverifiable`,
    which is the honest answer and not a pass."""
    mod = _gate_mod()
    if mod is None:
        return None, 0
    try:
        sex = life.get_config("sex")
    except Exception:            # noqa: BLE001
        sex = None
    try:
        deficit = life._num(life._detail_get(rule["detail"], "deficit_kcal"),
                            None)
    except Exception:            # noqa: BLE001
        deficit = None
    try:
        return mod.evaluate(deficit_kcal=deficit, base_target_kcal=aim,
                            bmr_kcal=(rule.get("bmr") or None), sex=sex), 0
    except Exception:            # noqa: BLE001
        return None, 0


def compute(conn, life, today_local=None):
    """The carry-over for `today_local` (default: today in the declared zone).

    Returns a dict.  `applicable` is False, with a `reason`, whenever any
    declared input is absent -- the caller renders nothing in that case."""
    anchor = life._kcal_week_anchor(conn)
    if anchor is None:
        return {"applicable": False,
                "reason": "no declared week boundary (period_anchor)"}
    off_min, week_start = anchor
    rule = life._kcal_week_rule(conn)
    if rule is None:
        return {"applicable": False,
                "reason": "no active calorie rule with a derivable weekly band"}

    if today_local is None:
        today_local = (datetime.datetime.now(datetime.timezone.utc)
                       + datetime.timedelta(minutes=off_min)).date()
    today_s = today_local.isoformat()
    monday = life._kcal_week_floor(today_local, week_start)
    bal = life._kcal_week_balance(conn, monday, off_min, rule, today_s)

    before = [d for d in bal["days"] if d["date"] < today_s]
    counted_days = [d for d in before if d["state"] == "complete"]
    dropped = [d for d in before if d["state"] != "complete"]
    counted = sum(d["intake"] for d in counted_days)
    planned = sum(d["target"] for d in counted_days)
    # Floored at zero: the erase half of the rule, in one operator.
    carry = max(0.0, counted - planned)

    remaining = [d for d in bal["days"] if d["date"] >= today_s]
    days_left = len(remaining)
    today_row = next((d for d in bal["days"] if d["date"] == today_s), None)
    if today_row is None or days_left == 0:
        # `today` is outside the week this module just built -- only reachable
        # if a caller hands in a date from another week. Refuse rather than
        # spread a carry across days it was not computed from.
        return {"applicable": False,
                "reason": "requested date is not inside the anchored week"}

    cut = int(round(carry / days_left))
    base_target = int(round(today_row["target"]))
    aim = max(0, base_target - cut)

    # -- G6 FLOOR (0.11.0) -------------------------------------------------
    # Zero was never the floor. This module can only LOWER a target and it had
    # exactly one guard on how far -- `max(0, ...)` -- while the number that
    # actually bounds it, the inviolable `calorie_floor` row, was named only in
    # a document the pack never delivered. A long enough surplus divided into a
    # short enough remainder produces an aim under the floor, and before this
    # release nothing anywhere refused it.
    #
    # The clamp is applied to the AIM, not to the carry: the carry is a measured
    # fact about days already eaten and must not be rewritten to make today's
    # number legal. What changes is how much of it today is asked to absorb --
    # `cut_kcal` reports what actually came off, which is already this module's
    # contract for the zero floor.
    gate, floor_applied = _safety_gate(aim, rule, life)
    if gate is not None and gate.get("verdict") == "refuse":
        permitted = _gate_mod().permitted_base(gate, aim)
        if permitted is not None and permitted > aim:
            floor_applied = permitted - aim
            aim = int(permitted)
    applied = base_target - aim          # what actually came off, after the floors

    # FLOOR PRESSURE -- reported, never asserted, and only computed when the
    # comparison is honest: the floor spans all seven days, so a week with a
    # dropped day has no seven-day sum to compare against it.
    projected = None
    floor_pressure = None
    if not dropped:
        projected = counted + sum(
            max(0, int(round(d["target"])) - cut) for d in remaining)
        floor_pressure = projected < bal["floor"]

    return {
        "applicable": True,
        "date": today_s,
        "week_start": bal["start"],
        "week_end": bal["end"],
        "training_today": bool(today_row["training"]),
        "base_target": base_target,
        "carry_kcal": int(round(carry)),
        "days_left": days_left,
        "cut_kcal": int(applied),
        "aim_kcal": aim,
        "safety_verdict": None if gate is None else gate.get("verdict"),
        "safety_floor_applied": int(floor_applied),
        "safety_missing": None if gate is None else (gate.get("limits_missing")
                                                     or []),
        "counted_days": len(counted_days),
        "dropped_days": len(dropped),
        "dropped_dates": [d["date"] for d in dropped],
        "counted_kcal": int(round(counted)),
        "planned_kcal": int(round(planned)),
        "week_ceiling": int(round(bal["ceiling"])),
        "week_floor": int(round(bal["floor"])),
        "projected_week": None if projected is None else int(round(projected)),
        "floor_pressure": floor_pressure,
        "band_why": rule["why"],
    }


def why_line(r):
    """ONE line, in the user's language, for the morning brief.

    Returns "" when there is nothing to say.  No carry means no line: a
    touchpoint that speaks every morning whether or not anything changed is
    how a signal becomes wallpaper."""
    if not r.get("applicable") or r.get("cut_kcal", 0) <= 0:
        return ""
    line = ("어제까지 계획보다 %s kcal 더 먹었습니다 -- 남은 %d일에 나눠 "
            "오늘 목표는 %s 대신 %s 입니다."
            % (format(r["carry_kcal"], ","), r["days_left"],
               format(r["base_target"], ","), format(r["aim_kcal"], ",")))
    # A target the safety floor moved must say the floor moved it, or the owner
    # reads a cut that silently stopped short as a cut that was applied in full.
    if r.get("safety_floor_applied"):
        line += " 안전 하한에 걸려 %s kcal 만 내렸습니다." % format(
            r["cut_kcal"], ",")
    return line


def main(argv):
    ap = argparse.ArgumentParser(prog="carryover.py", add_help=True)
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    day = None
    if args.date:
        try:
            day = datetime.date.fromisoformat(args.date)
        except ValueError:
            print(json.dumps({"applicable": False,
                              "reason": "bad --date %r" % args.date}))
            return 2

    life = kit_life()
    conn = life.get_conn()
    try:
        r = compute(conn, life, day)
    finally:
        conn.close()

    if args.json:
        print(json.dumps(r, ensure_ascii=False))
        return 0
    if not r["applicable"]:
        print("carry-over: not applicable (%s)" % r["reason"])
        return 0
    print("date=%s" % r["date"])
    print("base_target=%d" % r["base_target"])
    print("carry_kcal=%d" % r["carry_kcal"])
    print("days_left=%d" % r["days_left"])
    print("cut_kcal=%d" % r["cut_kcal"])
    print("aim_kcal=%d" % r["aim_kcal"])
    print("counted_days=%d" % r["counted_days"])
    print("dropped_days=%d" % r["dropped_days"])
    if r["dropped_days"]:
        print("dropped_dates=%s" % ",".join(r["dropped_dates"]))
    print("projected_week=%s" % ("" if r["projected_week"] is None
                                 else r["projected_week"]))
    print("week_floor=%d" % r["week_floor"])
    print("week_ceiling=%d" % r["week_ceiling"])
    print("floor_pressure=%s" % ("" if r["floor_pressure"] is None
                                 else int(bool(r["floor_pressure"]))))
    print("safety_verdict=%s" % (r.get("safety_verdict") or ""))
    print("safety_floor_applied=%d" % (r.get("safety_floor_applied") or 0))
    if r.get("safety_missing"):
        print("safety_missing=%s" % ",".join(r["safety_missing"]))
    line = why_line(r)
    if line:
        print("why_line=%s" % line)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
