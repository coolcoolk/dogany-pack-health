#!/usr/bin/env python3
"""calorie_band -- the goal consult's calorie step: the activity band, the
maintenance RANGE and the target from its middle. Rules only; no I/O.

Product decisions (2026-10-08; supersedes 2026-09-27
"watch linked -> NEAT from watch kcal" and 2026-09-28 "7,000 steps, no watch
mention"; evidence kimwog nutrition 750/751 NEAT + watch accuracy, 755-757
maintenance calibration, deficit dynamics, goal_calorie_rules):

  * the activity band comes from ONE job question (mostly seated / on feet /
    physical) and the weekly mean steps. Maintenance is shown as a RANGE
    (a starting estimate), the target is taken from its MIDDLE, and the
    weight trend corrects it at the weekly reviews.
  * lifting 3-6x a week sits INSIDE the band: no exercise add-on.
  * a smartwatch link imports steps and heart rate only. Watch kcal never
    sets or tops up the food target (cardio: a reference on the record;
    lifting: recorded only). No watch: the steps estimate / job band only.
  * no step count is ever assumed: an unknown count leaves the job band
    alone (the old silent 7,000 / 8,000-step defaults are gone).

The band is a physical activity level (PAL) range applied to the BMR the
kit's calculator computes (Katch-McArdle, `kit_life.sh body-state`). When
the job and the steps land in different tiers the range runs from the
lower tier's middle to the higher tier's middle -- the honest width of a
starting estimate, never a guess at which one is right.
"""

import math

JOBS = ("seated", "feet", "physical")

# PAL range per tier: (low, high). Resistance training 3-6x/week included.
PAL_BANDS = {
    "seated": (1.35, 1.55),
    "feet": (1.55, 1.75),
    "physical": (1.75, 1.95),
}

# weekly mean steps -> tier (the upper bound is exclusive)
STEP_TIERS = ((5000, "seated"), (10000, "feet"), (None, "physical"))

# the step buttons: a representative count per range (the user's own number,
# when said, is kept as said)
STEP_PICKS = {"under5k": 4000, "5to10k": 7500, "over10k": 11000}

# energy balance off the middle, by phase. cut = deficit, grow = surplus
# (lean bulk), recomp / maintain = small or none. Every number still clears
# the G6 gate (calorie_gate.py) before it is spoken.
PHASE_SHIFT = {"cut": -0.20, "recomp": -0.10, "grow": 0.10, "maintain": 0.0}

ROUND = 50          # range ends and the deficit are said in 50s
ROUND_TARGET = 10   # the middle / target in 10s

# the kinds a linked watch imports (hk-ingest consent kinds). Never
# active_energy: watch kcal does not feed the food target.
WATCH_IMPORT_KINDS = ("steps", "heart_rate", "resting_heart_rate")


def _round(x, step):
    """Half-up to the step (never banker's rounding: 2,725 -> 2,730)."""
    return int(step * math.floor(float(x) / step + 0.5))


def steps_tier(steps):
    """The tier a weekly mean step count reads as, or None when unknown."""
    if steps is None:
        return None
    try:
        n = float(steps)
    except (TypeError, ValueError):
        return None
    if n <= 0:
        return None
    for top, tier in STEP_TIERS:
        if top is None or n < top:
            return tier
    return None


def pal_range(job, steps=None):
    """(low, high, basis): the PAL range from the job tier and the steps
    tier. basis = 'job' | 'agree' | 'between'."""
    if job not in PAL_BANDS:
        raise ValueError("job must be one of %s" % ", ".join(JOBS))
    st = steps_tier(steps)
    if st is None:
        lo, hi = PAL_BANDS[job]
        return lo, hi, "job"
    if st == job:
        lo, hi = PAL_BANDS[job]
        return lo, hi, "agree"
    mids = sorted(sum(PAL_BANDS[t]) / 2.0 for t in (job, st))
    return mids[0], mids[1], "between"


def maintenance(bmr, job, steps=None):
    """{low, high, middle, basis}: the maintenance range in kcal a day."""
    lo, hi, basis = pal_range(job, steps)
    low = _round(bmr * lo, ROUND)
    high = _round(bmr * hi, ROUND)
    return {"low": low, "high": high,
            "middle": _round((low + high) / 2.0, ROUND_TARGET),
            "basis": basis}


def target(maint, phase):
    """{target, deficit, surplus}: the starting target off the middle.
    Never adds exercise or watch kcal."""
    shift = PHASE_SHIFT.get(phase or "maintain", 0.0)
    delta = _round(abs(maint["middle"] * shift), ROUND)
    if shift < 0:
        return {"target": maint["middle"] - delta, "deficit": delta,
                "surplus": 0}
    if shift > 0:
        return {"target": maint["middle"] + delta, "deficit": 0,
                "surplus": delta}
    return {"target": maint["middle"], "deficit": 0, "surplus": 0}


def kit_neat(maint, bmr):
    """The kit computes base = BMR - deficit + NEAT from avg_steps and
    other_neat_kcal. The band already holds every activity, so the kit is
    given avg_steps=0 and the middle's activity as other_neat_kcal: its base
    then equals middle - deficit, with no step count added on top."""
    return {"avg_steps": 0,
            "other_neat_kcal": max(0, int(maint["middle"] - round(bmr)))}


def parse_steps(value):
    """A said step count ('6500', '6,500', '6 cheon 5 baek' in Hangul
    units, '8 cheon') -> int, or None."""
    if value is None:
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return int(value) if value > 0 else None
    s = str(value).replace(",", "").replace(" ", "").replace("\ubcf4", "")
    s = s.replace("\uac78\uc74c", "").replace("\uc815\ub3c4", "").replace("\ucbe4", "")
    try:
        n = float(s)
        return int(n) if n > 0 else None
    except ValueError:
        pass
    total, num = 0.0, ""
    units = {"\ub9cc": 10000, "\ucc9c": 1000, "\ubc31": 100}
    for ch in s:
        if ch.isdigit() or ch == ".":
            num += ch
        elif ch in units:
            total += (float(num) if num else 1.0) * units[ch]
            num = ""
        else:
            return None
    if num:
        total += float(num)
    return int(total) if total > 0 else None
