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
import os
import re

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


# ---------------------------------------------------------------------------
# the day-end settlement and the weekly signals (owner 2026-10-11 12:06;
# evidence kimwog nutrition 750 steps_to_kcal + 751 neat_rules)
# ---------------------------------------------------------------------------
# The daytime target stays the morning number. At day end the real step
# count re-reads today's NEAT against the steps the band was built on, with
# 750's per-step arithmetic (NET kcal per kg body weight per 1000 steps,
# 0.3-0.6, grade D: the middle is used and the line says "about"). Watch
# active kcal is never read (no brand is accurate, Apple pooled error about
# 28 percent, the sign flips by device / activity / body fat) and no brand
# factor is applied: there is none that is defensible.
STEPS_KCAL_PER_KG = (0.3, 0.6)      # per 1000 steps, 750 steps_to_kcal
DEFAULT_BASE_STEPS = 7000           # the band's step basis when never answered
KCAL_PER_KG = 7700                  # convention (751 recalibrate-from-trend)
NEAT_DROP = 0.20                    # 751 neat-drop-signal: 20 percent
RECAL_DAYS = 14                     # 751: the trend window opens at day 14
RECAL_LOGGED_DAYS = 10
SETTLE_ROUND = 10

_KNOWLEDGE_750 = "nutrition-neat-estimation-watch-steps-evidence-750.md"


def _knowledge_dirs():
    env = os.environ.get("HEALTH_KNOWLEDGE_DIR")
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(os.path.dirname(here))
    out = [env] if env else []
    out.append(os.path.join(root, "knowledge", "kimwog", "items"))
    return out


def steps_rule():
    """(low, high) NET kcal per kg per 1000 steps: the warehouse item 750's
    steps_to_kcal block when it is installed, else the same numbers."""
    for d in _knowledge_dirs():
        p = os.path.join(d, _KNOWLEDGE_750)
        if not os.path.isfile(p):
            continue
        try:
            text = open(p, encoding="utf-8").read()
        except OSError:
            continue
        m = re.search(r"^steps_to_kcal:\s*\n((?:[ \t]+.*\n)+)", text, re.M)
        if not m:
            continue
        lo = re.search(r"^\s+low:\s*([0-9.]+)", m.group(1), re.M)
        hi = re.search(r"^\s+high:\s*([0-9.]+)", m.group(1), re.M)
        try:
            pair = (float(lo.group(1)), float(hi.group(1)))
        except (AttributeError, ValueError):
            continue
        if 0 < pair[0] <= pair[1]:
            return pair
    return STEPS_KCAL_PER_KG


def steps_kcal(steps, weight_kg):
    """NET kcal for a step count at the rule's middle (derived arithmetic)."""
    lo, hi = steps_rule()
    return float(steps) / 1000.0 * float(weight_kg) * (lo + hi) / 2.0


def cardio_kcal(met, weight_kg, minutes):
    """A cardio session's NET kcal, the exercise 094 / 095 rule the
    cardio-record verb already uses: (MET - 1) x kg x h. Lifting sits inside
    the band (751 lifting-inside-the-band) and is never added."""
    if not met or met <= 1 or not weight_kg or not minutes or minutes <= 0:
        return 0
    return int(round((float(met) - 1.0) * float(weight_kg) * minutes / 60.0))


def day_settlement(maint_middle, weight_kg, eaten_kcal, steps=None,
                   base_steps=None, cardio=0):
    """The day-end estimate. {burn, eaten, diff, steps, base_steps, basis}:
    basis = 'steps' when today's real step count re-read the NEAT, 'default'
    when there was none (the band's own activity stands, said as such)."""
    base = int(base_steps or DEFAULT_BASE_STEPS)
    burn = float(maint_middle)
    basis = "default"
    if steps is not None and steps > 0 and weight_kg:
        burn += steps_kcal(steps - base, weight_kg)
        basis = "steps"
    burn += float(cardio or 0)
    burn = _round(burn, SETTLE_ROUND)
    eaten = int(round(eaten_kcal or 0))
    return {"burn": burn, "eaten": eaten, "diff": eaten - burn,
            "steps": int(steps) if basis == "steps" else None,
            "base_steps": base, "basis": basis}


def weekly_change_kg(delta_kcal):
    """A daily deficit (-) / surplus (+) as kg a week, 0.1 kg steps."""
    return round(float(delta_kcal) * 7.0 / KCAL_PER_KG, 1)


def protein_per_kg(protein_g, weight_kg):
    if not protein_g or not weight_kg:
        return None
    return round(float(protein_g) / float(weight_kg), 1)


def age_from(birth, today):
    """Age in whole years from a birth year ('1995') or a birth date
    ('1995-03-02'); None when unreadable."""
    s = str(birth or "").strip()
    m = re.match(r"^(\d{4})(?:[-./](\d{1,2})[-./](\d{1,2}))?$", s)
    if not m:
        return None
    y = int(m.group(1))
    if not 1900 <= y <= today.year:
        return None
    age = today.year - y
    if m.group(2):
        try:
            if (today.month, today.day) < (int(m.group(2)), int(m.group(3))):
                age -= 1
        except ValueError:
            return None
    return age


def neat_drop(ref_mean, week_mean, prev_week_mean=None):
    """751 neat-drop-signal, said ONCE: True only the first week the weekly
    step mean sits NEAT_DROP or more under the cut's first two weeks (the
    week before was still above the line, or unknown)."""
    if not ref_mean or not week_mean or ref_mean <= 0:
        return False
    line = ref_mean * (1.0 - NEAT_DROP)
    if week_mean > line:
        return False
    return prev_week_mean is None or prev_week_mean > line


def logged_maintenance(day_kcals, weight_change_kg_week):
    """751 recalibrate-from-trend: mean logged kcal over complete logged
    days minus the confirmed weekly weight change in kcal a day -- in the
    user's own logged units. None below the logged-day floor."""
    days = [float(k) for k in day_kcals if k]
    if len(days) < RECAL_LOGGED_DAYS or weight_change_kg_week is None:
        return None
    mean = sum(days) / len(days)
    return _round(mean - weight_change_kg_week * KCAL_PER_KG / 7.0, ROUND)
