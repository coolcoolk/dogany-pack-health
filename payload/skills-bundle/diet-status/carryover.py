#!/usr/bin/env python3
"""
Calorie CARRY-OVER: what YESTERDAY owes to today, and nothing older.

WHY.  The owner stated the gap (2026-09-10 17:11): there was no mechanism by
which eating over today means eating less tomorrow.  v0.1 answered it with a
weekly ledger -- a surplus spread over the days left in the declared week.
The owner then narrowed it (2026-10-11 21:03): "if you eat a lot you have to
absorb it; health comes first".  Overeating is absorbed, not paid back across
the week.  So the window is ONE day and the payback is bounded.

THE RULE.
  window   yesterday only.  No week boundary, no spread over days_left.
           Yesterday's record must be 'complete' under the kit's own
           under-logging guard (>= 3 distinct meal slots,
           _KCAL_DAY_MIN_SLOTS); a partial or unlogged yesterday carries
           nothing and is reported in `dropped_days` / `dropped_dates`.
           An unlogged day is a missing RECORD, not missing food (046).
  surplus  yesterday's intake minus yesterday's EFFECTIVE target (the
           consult-settled config target when one is set -- the number the
           card drew -- else the rule's rest/training day target).
  carry    min(surplus, cap).  The remainder (`absorbed_kcal`) is DROPPED,
           never carried to tomorrow or anywhere else.
  floor 0  an undershoot is erased: fat loss follows the cumulative deficit,
           so a day under the target is a smaller number in the sum, not a
           credit.  This module can only ever LOWER a target.
  G6       the safety gate (calorie_gate.py) still binds LAST, on the aim.

THE CAP.  CARRY_CAP_KCAL = 300, a PRODUCT constant, not a graded threshold.
The knowledge warehouse (kimwog items, searched 2026-10-11: diet breaks 026,
flexible vs rigid restraint 025, weekend drift 073, adherence rules 074,
energy availability 010, deficit/lean mass 062) carries no per-day reduction
bound for a one-off compensation day.  The nearest number -- a sustained
deficit of ~500 kcal/day stopped lean-mass gain (Murphy & Koehler 2022,
meta-regression, in 062) -- bounds the standing deficit, not a single day's
cut, so it is not borrowed.  The owner-named default of 300 applies.  The
existing kit config store overrides it (key `carry_cap_kcal`, read through
the same life.get_config this module already reads `sex` with); no new store.

  ran a LARGE deficit  ->  NOT ASSERTED.  `floor_pressure` is reported as a
      flag with the numbers behind it and NEVER as a verdict (EA threshold
      graded C / contested); the wording rule lives in SKILL.md.

FAIL-CLOSED, everywhere the inputs run out: no declared week anchor (it holds
the declared UTC offset that defines a local day), no active calorie rule, or
a rule whose detail is missing a field -> no carry-over and no sentence.

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


# The per-day bound on what yesterday may take off today (owner 2026-10-11
# 21:03: "absorb it; health comes first"). Product constant -- see THE CAP in
# the module docstring for why no warehouse number replaces it.
CARRY_CAP_KCAL = 300
# Existing kit config store (life.get_config); absent / unreadable -> default.
CARRY_CAP_CONFIG_KEY = "carry_cap_kcal"


def _config_num(life, key):
    """A config value as a float, or None when absent or not a number."""
    try:
        v = life.get_config(key)
        return None if v in (None, "") else float(v)
    except Exception:            # noqa: BLE001 -- unreadable = not set
        return None


def carry_cap(life):
    """(cap_kcal, source). source is 'config' or 'default'."""
    v = _config_num(life, CARRY_CAP_CONFIG_KEY)
    if v is not None and v >= 0:
        return int(round(v)), "config"
    return CARRY_CAP_KCAL, "default"


def _settled(life):
    """The consult-settled daily target (config calorie_target_kcal, written
    with its maintenance_mid), or None -- card.py settled_target's rule, so
    the surplus is measured against the number the card actually drew."""
    tgt = _config_num(life, "calorie_target_kcal")
    if tgt and _config_num(life, "maintenance_mid"):
        return int(round(tgt))
    return None


def _day_row(conn, life, day, off_min, week_start, rule, today_s):
    """(week balance, the row for `day`) from the kit's own week readout."""
    bal = life._kcal_week_balance(
        conn, life._kcal_week_floor(day, week_start), off_min, rule, today_s)
    iso = day.isoformat()
    return bal, next(d for d in bal["days"] if d["date"] == iso)


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
    yday = today_local - datetime.timedelta(days=1)
    bal, today_row = _day_row(conn, life, today_local, off_min, week_start,
                              rule, today_s)
    # Yesterday may sit in the previous declared week; the week is only the
    # kit's readout shape here, never a boundary the carry respects.
    _, y_row = _day_row(conn, life, yday, off_min, week_start, rule, today_s)

    settled = _settled(life)

    def target(row):
        return settled if settled else int(round(row["target"]))

    base_target = target(today_row)
    y_target = target(y_row)
    complete = y_row["state"] == "complete"
    # Floored at zero: the erase half of the rule, in one operator. An
    # incomplete yesterday carries nothing -- a gap is not food eaten.
    surplus = max(0.0, y_row["intake"] - y_target) if complete else 0.0
    cap, cap_source = carry_cap(life)
    carry = min(int(round(surplus)), cap)
    absorbed = int(round(surplus)) - carry     # dropped, never carried further
    aim = max(0, base_target - carry)

    # -- G6 FLOOR (0.11.0), applied LAST --------------------------------------
    # The clamp is applied to the AIM, not to the carry: the carry is a fact
    # about yesterday and must not be rewritten to make today's number legal.
    # `cut_kcal` reports what actually came off.
    gate, floor_applied = _safety_gate(aim, rule, life)
    if gate is not None and gate.get("verdict") == "refuse":
        permitted = _gate_mod().permitted_base(gate, aim)
        if permitted is not None and permitted > aim:
            floor_applied = permitted - aim
            aim = int(permitted)
    applied = base_target - aim          # what actually came off, after the floors

    # FLOOR PRESSURE -- reported, never asserted, and only computed when the
    # comparison is honest: the floor spans all seven days of the declared
    # week, so a week with a gap before today has no seven-day sum.
    before = [d for d in bal["days"] if d["date"] < today_s]
    after = [d for d in bal["days"] if d["date"] > today_s]
    projected = None
    floor_pressure = None
    if all(d["state"] == "complete" for d in before):
        projected = (sum(d["intake"] for d in before) + aim
                     + sum(target(d) for d in after))
        floor_pressure = projected < bal["floor"]

    return {
        "applicable": True,
        "date": today_s,
        "yesterday": y_row["date"],
        "yesterday_state": y_row["state"],
        "week_start": bal["start"],
        "week_end": bal["end"],
        "training_today": bool(today_row["training"]),
        "base_target": base_target,
        "surplus_kcal": int(round(surplus)),
        "carry_cap_kcal": cap,
        "carry_cap_source": cap_source,
        # what today is asked to absorb (min(surplus, cap)); the card's
        # top-level `carry_kcal` input takes exactly this number.
        "carry_kcal": carry,
        "absorbed_kcal": absorbed,
        "days_left": 1,                  # the carry lands on today only
        "cut_kcal": int(applied),
        "aim_kcal": aim,
        "safety_verdict": None if gate is None else gate.get("verdict"),
        "safety_floor_applied": int(floor_applied),
        "safety_missing": None if gate is None else (gate.get("limits_missing")
                                                     or []),
        "counted_days": 1 if complete else 0,
        "dropped_days": 0 if complete else 1,
        "dropped_dates": [] if complete else [y_row["date"]],
        "counted_kcal": int(round(y_row["intake"])) if complete else 0,
        "planned_kcal": y_target if complete else 0,
        "week_ceiling": int(round(bal["ceiling"])),
        "week_floor": int(round(bal["floor"])),
        "projected_week": None if projected is None else int(round(projected)),
        "floor_pressure": floor_pressure,
        "band_why": rule["why"],
    }


def why_line(r):
    """ONE line, in the user's language, for the morning brief.

    Returns "" when there is nothing to say.  No cut means no line: a
    touchpoint that speaks every morning whether or not anything changed is
    how a signal becomes wallpaper."""
    if not r.get("applicable") or r.get("cut_kcal", 0) <= 0:
        return ""
    # "Yesterday you ate N kcal more, so today's target is lowered by C kcal.
    # Today's target is A kcal."
    line = (u"\uc5b4\uc81c %skcal \ub354 \ub4dc\uc154\uc11c \uc624\ub298 "
            u"\ubaa9\ud45c\ub97c %skcal \ub0ae\ucdc4\uc5b4\uc694. "
            u"\uc624\ub298 \ubaa9\ud45c\ub294 %skcal\uc608\uc694."
            % (format(r["surplus_kcal"], ","), format(r["cut_kcal"], ","),
               format(r["aim_kcal"], ",")))
    # A target the safety floor moved must say the floor moved it, or the owner
    # reads a cut that stopped short as a cut that was applied in full.
    # "Because of the safety floor it was not lowered further."
    if r.get("safety_floor_applied"):
        line += (u" \uc548\uc804 \ud558\ud55c \ub54c\ubb38\uc5d0 \ub354 "
                 u"\ub0ae\ucd94\uc9c0\ub294 \uc54a\uc558\uc5b4\uc694.")
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
    print("yesterday=%s" % r["yesterday"])
    print("yesterday_state=%s" % r["yesterday_state"])
    print("base_target=%d" % r["base_target"])
    print("surplus_kcal=%d" % r["surplus_kcal"])
    print("carry_cap_kcal=%d" % r["carry_cap_kcal"])
    print("carry_cap_source=%s" % r["carry_cap_source"])
    print("carry_kcal=%d" % r["carry_kcal"])
    print("absorbed_kcal=%d" % r["absorbed_kcal"])
    print("cut_kcal=%d" % r["cut_kcal"])
    print("aim_kcal=%d" % r["aim_kcal"])
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
