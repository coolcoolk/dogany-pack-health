#!/usr/bin/env python3
# prescription.py -- the load<->rep prescription axis (SPEC A2.4 / A6 / A8,
# pack payload).
#
# WHAT THIS FIXES (SPEC defect #12, observed live 2026-08-25 06:57):
#   The deadlift target was 5 reps. The load went 135 -> 140kg. `target_reps`
#   stayed pinned at 5. The owner hit 3 reps at RIR 2, twice. The system scored
#   that as 목표 미달 (missed target) and the model then invented a CONDITION
#   cause for it -- "오늘 140kg이 좀 빡빡한 것 같습니다".
#
#   That diagnosis is wrong. At e1RM 163kg, 140kg is ~86% of 1RM: about a 5-rep
#   maximum. A 5-rep TARGET at that load, under the slot's RIR floor of 2, would
#   require a 7-rep capacity at 86% -- which does not exist. The prescription was
#   impossible, the performance was fine. Blaming the user's condition for a bad
#   prescription is the exact failure mode this module exists to delete.
#
# THE RULE (SPEC A2.4): a shortfall verdict is NOT `actual_reps < target_reps`.
# It FIRST asks whether `target_reps` was plausible for that load against that
# e1RM. If it was not, the verdict is PRESCRIPTION_ADJUST (처방 조정), never
# UNDERPERFORMED. Only a target that WAS plausible can be underperformed.
#
# WHERE THE PINNED CONSTANT LIVES (upstream, live instance -- not edited here):
#   files/program/program.yaml carries a static per-slot `rep_range` and
#   rx-calc's apply_progression() moves `weight_kg` while never touching
#   `rep_range`. Load progresses; the rep target cannot follow it. That is the
#   structural source of #12.
#   (2026-09-30, owner ruling: rx-calc now emits `target_reps` beside
#   `weight_kg` -- recomputed from e1RM at the rounded load once an exercise
#   has >= 3 sessions of data, the rep_range bottom right after a progression
#   'up' otherwise -- and set-table / set-arm read it. See e1rm_rx.py.)
#
# A6 -- NO FREE TEXT. Verdict exposes ONLY computed judgment. There is
# deliberately no `reason` / `note` / `comment` field, and Verdict is a frozen
# dataclass so a model-facing caller cannot bolt one on at runtime. Downstream
# prose is GENERATED FROM these fields; it never adds a cause that is not in
# them. When no verdict can be computed the outcome is NO_VERDICT and the
# summary block is OMITTED (see should_emit_summary) -- never guessed.
#
# A8 -- SAFETY. Raising load while holding the rep target constant walks the
# user toward failure reps, which on a loaded compound is an injury path.
# is_unsafe_prescription() is a TOOL-LAYER GATE: the caller hard-gates on the
# boolean before a cue is ever published. It is never a prompt rule and never
# prose. Cap VALUES are not in this file -- per SPEC A8 they live in store rows
# (workout_program cap rows) and arrive as a caller-supplied config mapping.
#
# i18n (SPEC Gate 3): every token in this module is English. No Korean.
#
# stdlib only.

from dataclasses import dataclass
from enum import Enum


# ---------------------------------------------------------------------------
# THE REP-MAX TABLE -- the load<->rep relationship AS DATA.
#
# Source: the standard rep-max percentage chart from Baechle & Earle,
# "Essentials of Strength Training and Conditioning" (NSCA), the chart every
# %1RM prescription in the field is cut from. It agrees with the Epley estimate
# (1RM = w * (1 + reps/30)) to within ~1-2 percentage points across 1-10 reps.
#
# Read as: PCT_OF_1RM[n] = the percentage of 1RM a trainee can lift for exactly
# n reps to failure. It is a lookup table on purpose -- an if/elif ladder is how
# a rep target ends up pinned to a constant in the first place.
#
# The chart is only meaningful in the strength/hypertrophy band. Below
# PCT_OF_1RM[TABLE_MAX_REPS] the rep relation degrades into work capacity, so
# capacity is clamped at TABLE_MAX_REPS and the clamp is reported, not hidden.
# ---------------------------------------------------------------------------
PCT_OF_1RM = {
    1: 100.0,
    2: 95.0,
    3: 93.0,
    4: 90.0,
    5: 87.0,
    6: 85.0,
    7: 83.0,
    8: 80.0,
    9: 77.0,
    10: 75.0,
    11: 72.0,
    12: 70.0,
}

TABLE_MIN_REPS = min(PCT_OF_1RM)
TABLE_MAX_REPS = max(PCT_OF_1RM)

# How far BELOW the RIR-adjusted ceiling a target may sit and still count as a
# sane prescription rather than a load/target mismatch. This is a MODELLING band
# width, NOT a safety cap -- safety cap values live in store rows (SPEC A8) and
# are never written in this file. Widening it only makes the plausibility test
# more permissive in the "load is too light" direction; it can never permit an
# over-heavy prescription, which is the direction that hurts people.
PLAUSIBLE_BAND_SLACK = 2


# ---------------------------------------------------------------------------
# Outcomes and the closed rule vocabulary.
#
# `rule` on a Verdict is drawn from RULES and nowhere else: it names WHICH
# BRANCH FIRED, so downstream prose is traceable to a computation instead of to
# a model's guess.
# ---------------------------------------------------------------------------
class Outcome(str, Enum):
    PRESCRIPTION_ADJUST = "PRESCRIPTION_ADJUST"   # the target was wrong, not the effort
    UNDERPERFORMED = "UNDERPERFORMED"             # target was plausible and was missed
    ON_TARGET = "ON_TARGET"
    OVERPERFORMED = "OVERPERFORMED"               # signal: the load is too light
    NO_VERDICT = "NO_VERDICT"                     # A6: omit the summary block


class AdjustDirection(str, Enum):
    TARGET_TOO_HIGH = "TARGET_TOO_HIGH"   # target exceeds what the load allows
    TARGET_TOO_LOW = "TARGET_TOO_LOW"     # load is too light for that target


RULES = {
    "R-RX-NO-VERDICT":
        "an input required for judgment is absent; A6 omits the summary block",
    "R-RX-LOAD-ABOVE-1RM":
        "the load meets or exceeds the estimated 1RM, so no rep target exists",
    "R-RX-NO-PLAUSIBLE-TARGET":
        "the RIR reserve leaves no reps at this load; no target can be plausible",
    "R-RX-TARGET-ABOVE-CAPACITY":
        "the target exceeds the reps the load allows at that RIR reserve "
        "(SPEC defect #12 -- prescription, not performance)",
    "R-RX-TARGET-BELOW-BAND":
        "the target sits below the band the load supports; the load is too light",
    "R-RX-SHORT":
        "the target was plausible and the achieved reps fell short of it",
    "R-RX-MET":
        "the target was plausible and was met",
    "R-RX-EXCEEDED":
        "the target was plausible and was beaten; the load is a candidate to rise",
}


# ---------------------------------------------------------------------------
# Refusals. Unknown or nonsensical inputs raise -- they are never defaulted.
# A silent default is what pins a rep target to a constant.
# ---------------------------------------------------------------------------
class PrescriptionInputError(ValueError):
    """Raised for an input that cannot be interpreted as a prescription value.

    Carries the rule id and the offending field so the failure names itself,
    matching the refusal style of blocks.py / set_kind.py.
    """

    rule = "R-RX-INPUT"

    def __init__(self, field, given, expected):
        self.field = field
        self.given = given
        super().__init__(
            "%s: %s=%r is not usable (%s); no default is applied"
            % (self.rule, field, given, expected)
        )


class MissingSafetyCapError(KeyError):
    """Raised when the caller-supplied safety config omits a required cap key.

    SPEC A8 puts cap VALUES in store rows, so this module cannot invent one. A
    missing cap must be loud, because the quiet alternative is a permissive
    gate -- exactly the instance-local anti-pattern (DGN-318) the spec forbids repeating.
    """

    rule = "R-RX-CAP-MISSING"

    def __init__(self, missing):
        self.missing = tuple(missing)
        super().__init__(
            "%s: safety config is missing cap key(s) %s; cap values live in "
            "store rows (SPEC A8) and are never defaulted in code"
            % (self.rule, ", ".join(repr(m) for m in self.missing))
        )


# ---------------------------------------------------------------------------
# Input coercion
# ---------------------------------------------------------------------------
def _number(field, value, minimum, allow_none=False):
    if value is None:
        if allow_none:
            return None
        raise PrescriptionInputError(field, value, "a number is required")
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise PrescriptionInputError(field, value, "expected int or float")
    if value != value or value in (float("inf"), float("-inf")):
        raise PrescriptionInputError(field, value, "expected a finite number")
    if value < minimum:
        raise PrescriptionInputError(field, value, "must be >= %s" % minimum)
    return float(value)


def _count(field, value, minimum, allow_none=False):
    if value is None:
        if allow_none:
            return None
        raise PrescriptionInputError(field, value, "a rep count is required")
    if isinstance(value, bool) or not isinstance(value, int):
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        else:
            raise PrescriptionInputError(field, value, "expected a whole rep count")
    if value < minimum:
        raise PrescriptionInputError(field, value, "must be >= %d" % minimum)
    return int(value)


# ---------------------------------------------------------------------------
# The two directions of the table
# ---------------------------------------------------------------------------
def pct_of_1rm(load, e1rm):
    """Load as a percentage of the estimated 1RM."""
    load = _number("load", load, minimum=0.0)
    e1rm = _number("e1rm", e1rm, minimum=0.0)
    if load <= 0:
        raise PrescriptionInputError("load", load, "must be > 0")
    if e1rm <= 0:
        raise PrescriptionInputError("e1rm", e1rm, "must be > 0")
    return 100.0 * load / e1rm


@dataclass(frozen=True)
class Capacity:
    """How many reps the TABLE says this load allows, to failure.

    reps == 0 means the load is at or above the estimated 1RM.
    clamped is True when the load is lighter than the table's last row, i.e. the
    real answer is "more than TABLE_MAX_REPS" and the chart no longer speaks.
    """

    reps: int
    pct_1rm: float
    clamped: bool


def reps_to_failure(load, e1rm):
    """(load, e1RM) -> table capacity in reps. Lookup, never a branch ladder.

    The answer is the largest n whose chart percentage still covers this load.
    140kg against e1RM 163kg is 85.9%: PCT_OF_1RM[5] = 87 covers it,
    PCT_OF_1RM[6] = 85 does not, so the capacity is 5 reps.
    """
    pct = pct_of_1rm(load, e1rm)
    if pct > PCT_OF_1RM[TABLE_MIN_REPS]:
        return Capacity(reps=0, pct_1rm=pct, clamped=False)
    covering = [n for n in sorted(PCT_OF_1RM) if PCT_OF_1RM[n] >= pct]
    reps = max(covering)
    return Capacity(reps=reps, pct_1rm=pct, clamped=(reps == TABLE_MAX_REPS))


def implied_e1rm(load, achieved_reps, rir):
    """(load, achieved reps, RIR) -> the e1RM that performance implies.

    achieved + RIR is the reps-to-failure that set demonstrated; the table turns
    that into a percentage and the percentage back into a 1RM. The live case:
    140kg x 3 @ RIR 2 is a 5-rep capacity, 140 / 0.87 = 160.9kg -- which lines up
    with the recorded e1RM of 163kg. The performance was never the problem.
    """
    load = _number("load", load, minimum=0.0)
    if load <= 0:
        raise PrescriptionInputError("load", load, "must be > 0")
    achieved_reps = _count("achieved_reps", achieved_reps, minimum=1)
    rir = _count("rir", rir, minimum=0)
    total = achieved_reps + rir
    if total > TABLE_MAX_REPS:
        total = TABLE_MAX_REPS
    return load / (PCT_OF_1RM[total] / 100.0)


@dataclass(frozen=True)
class PlausibleRange:
    """The rep targets this load can actually support at a given RIR reserve.

    high = capacity - reserve_rir. A target above `high` demands reps that do
    not exist at that load, which is what pins a user into failure attempts.
    low  = high - PLAUSIBLE_BAND_SLACK, floored at 1. A target below `low` is
    not dangerous, it just means the load is too light for the target.
    """

    low: int
    high: int
    capacity: int
    reserve_rir: int
    pct_1rm: float
    clamped: bool

    def contains(self, target_reps):
        return self.low <= target_reps <= self.high


def plausible_rep_target(load, e1rm, reserve_rir, slack=PLAUSIBLE_BAND_SLACK):
    """(load, e1RM, RIR reserve) -> the plausible rep-target band.

    This is the function the pinned constant should have been all along: move
    the load and the band moves with it.
    """
    reserve_rir = _count("reserve_rir", reserve_rir, minimum=0)
    slack = _count("slack", slack, minimum=0)
    cap = reps_to_failure(load, e1rm)
    high = cap.reps - reserve_rir
    low = max(1, high - slack)
    return PlausibleRange(
        low=low,
        high=high,
        capacity=cap.reps,
        reserve_rir=reserve_rir,
        pct_1rm=cap.pct_1rm,
        clamped=cap.clamped,
    )


# ---------------------------------------------------------------------------
# The Verdict
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Verdict:
    """A computed judgment and the evidence that produced it. Nothing else.

    A6 CONTRACT: there is no free-text field on this object -- no `reason`, no
    `note`, no `summary`. The model receives a Verdict and RENDERS it; it may
    not add a cause the computation did not produce. The dataclass is frozen so
    a free-text field cannot be attached at runtime either. `rule` is a key of
    RULES, so every sentence downstream traces back to one named branch.

    Evidence carried:
      plausible          the rep band the load supports (None when uncomputable)
      capacity           table reps-to-failure at this load
      pct_1rm            the load as %1RM
      implied_e1rm       the e1RM the achieved set demonstrates
      suggested_target   the target the load actually supports
      adjust_direction   which way the prescription is wrong
      missing            input names absent when outcome is NO_VERDICT
    """

    outcome: Outcome
    rule: str
    load: float = None
    e1rm: float = None
    target_reps: int = None
    actual_reps: int = None
    rir: int = None
    pct_1rm: float = None
    capacity: int = None
    plausible: PlausibleRange = None
    implied_e1rm: float = None
    suggested_target_reps: int = None
    adjust_direction: AdjustDirection = None
    missing: tuple = ()

    @property
    def target_was_plausible(self):
        """None when the question could not be asked at all."""
        if self.plausible is None or self.target_reps is None:
            return None
        return self.plausible.contains(self.target_reps)

    def __post_init__(self):
        if self.rule not in RULES:
            raise PrescriptionInputError(
                "rule", self.rule,
                "must be one of the closed vocabulary %s" % ", ".join(sorted(RULES)))


def no_verdict(missing):
    """A6: judgment could not be computed, so the summary block is OMITTED.

    This is a value, not an exception, because "say nothing" is a legitimate
    outcome the publisher must be able to route. It is emphatically not a
    placeholder for the model to fill in.
    """
    return Verdict(
        outcome=Outcome.NO_VERDICT,
        rule="R-RX-NO-VERDICT",
        missing=tuple(missing),
    )


def should_emit_summary(verdict):
    """Tool-layer predicate for SPEC A6: emit the summary block, or omit it."""
    return verdict.outcome is not Outcome.NO_VERDICT


# ---------------------------------------------------------------------------
# evaluate -- SPEC A2.4's core rule
# ---------------------------------------------------------------------------
def evaluate(load, e1rm, target_reps, actual_reps, rir,
             prescribed_rir=None, slack=PLAUSIBLE_BAND_SLACK):
    """Judge one set. Plausibility of the TARGET is tested BEFORE performance.

    Args:
        load:           kg actually loaded. Required, > 0.
        e1rm:           estimated 1RM. None -> NO_VERDICT.
        target_reps:    the prescribed rep target. None -> NO_VERDICT.
        actual_reps:    reps achieved. None -> NO_VERDICT.
        rir:            reps in reserve at the end of the set. None -> NO_VERDICT.
        prescribed_rir: the RIR the prescription asked for (e.g. a slot's
                        rir_floor). Defaults to the observed `rir` -- the
                        reserve the set was actually run with.
        slack:          plausibility band width (see PLAUSIBLE_BAND_SLACK).

    Returns:
        Verdict. Never prose, never a guess.

    Raises:
        PrescriptionInputError on garbage input. Absent inputs are NO_VERDICT;
        malformed inputs raise. The two are not the same thing.
    """
    missing = []
    if e1rm is None:
        missing.append("e1rm")
    if target_reps is None:
        missing.append("target_reps")
    if actual_reps is None:
        missing.append("actual_reps")
    if rir is None and prescribed_rir is None:
        missing.append("rir")
    if missing:
        # Still validate what WAS supplied -- garbage must raise even when
        # something else is absent, or a typo hides behind a silence.
        _number("load", load, minimum=0.0, allow_none=True)
        _number("e1rm", e1rm, minimum=0.0, allow_none=True)
        _count("target_reps", target_reps, minimum=1, allow_none=True)
        _count("actual_reps", actual_reps, minimum=0, allow_none=True)
        _count("rir", rir, minimum=0, allow_none=True)
        return no_verdict(missing)

    load = _number("load", load, minimum=0.0)
    if load <= 0:
        raise PrescriptionInputError("load", load, "must be > 0")
    e1rm = _number("e1rm", e1rm, minimum=0.0)
    if e1rm <= 0:
        raise PrescriptionInputError("e1rm", e1rm, "must be > 0")
    target_reps = _count("target_reps", target_reps, minimum=1)
    actual_reps = _count("actual_reps", actual_reps, minimum=0)
    rir = _count("rir", rir, minimum=0, allow_none=True)
    reserve = _count("prescribed_rir", prescribed_rir, minimum=0, allow_none=True)
    if reserve is None:
        reserve = rir

    band = plausible_rep_target(load, e1rm, reserve, slack=slack)
    # The implied e1RM needs an OBSERVED reserve; a prescribed one says nothing
    # about what the set demonstrated. No observation -> no implied value.
    implied = (implied_e1rm(load, actual_reps, rir)
               if (rir is not None and actual_reps >= 1) else None)

    common = dict(
        load=load,
        e1rm=e1rm,
        target_reps=target_reps,
        actual_reps=actual_reps,
        rir=rir,
        pct_1rm=band.pct_1rm,
        capacity=band.capacity,
        plausible=band,
        implied_e1rm=implied,
    )

    # ---- GATE 1: was the target plausible for this load? (SPEC A2.4) --------
    # This runs BEFORE any comparison of actual against target. Everything
    # below this gate is downstream of a target that survived it.
    if band.capacity == 0:
        return Verdict(
            outcome=Outcome.PRESCRIPTION_ADJUST,
            rule="R-RX-LOAD-ABOVE-1RM",
            adjust_direction=AdjustDirection.TARGET_TOO_HIGH,
            suggested_target_reps=None,
            **common)

    if band.high < 1:
        return Verdict(
            outcome=Outcome.PRESCRIPTION_ADJUST,
            rule="R-RX-NO-PLAUSIBLE-TARGET",
            adjust_direction=AdjustDirection.TARGET_TOO_HIGH,
            suggested_target_reps=None,
            **common)

    if target_reps > band.high:
        # The 2026-08-25 deadlift case lands here: load rose, target did not
        # follow it down. The shortfall is the prescription's, not the user's.
        return Verdict(
            outcome=Outcome.PRESCRIPTION_ADJUST,
            rule="R-RX-TARGET-ABOVE-CAPACITY",
            adjust_direction=AdjustDirection.TARGET_TOO_HIGH,
            suggested_target_reps=band.high,
            **common)

    if target_reps < band.low:
        return Verdict(
            outcome=Outcome.PRESCRIPTION_ADJUST,
            rule="R-RX-TARGET-BELOW-BAND",
            adjust_direction=AdjustDirection.TARGET_TOO_LOW,
            suggested_target_reps=band.high,
            **common)

    # ---- GATE 2: the target was plausible; now the performance may be read --
    if actual_reps < target_reps:
        return Verdict(
            outcome=Outcome.UNDERPERFORMED,
            rule="R-RX-SHORT",
            suggested_target_reps=band.high,
            **common)

    if actual_reps > target_reps:
        return Verdict(
            outcome=Outcome.OVERPERFORMED,
            rule="R-RX-EXCEEDED",
            suggested_target_reps=band.high,
            **common)

    return Verdict(
        outcome=Outcome.ON_TARGET,
        rule="R-RX-MET",
        suggested_target_reps=band.high,
        **common)


# ---------------------------------------------------------------------------
# SPEC A8 -- TOOL-LAYER SAFETY GATE
#
# Everything below is a GATE, not prose. The caller hard-gates on the boolean
# before a cue is published; a prompt-only cap is forbidden by SPEC A8, which
# names the instance-local anti-pattern (deficit cap + calorie floor living only in a
# prompt, DGN-318 key mismatch, verification never firing) as the thing not to
# repeat.
#
# Cap VALUES are NOT in this file. They arrive from store rows (workout_program
# cap rows) through SafetyCaps.from_config(). A cap key that is absent raises;
# a cap explicitly set to None is a recorded caller decision to leave that one
# rule unconfigured, and shows up in the ruling rather than passing silently.
# ---------------------------------------------------------------------------
SAFETY_CAP_KEYS = (
    "session_load_increase_cap_kg",
    "session_load_increase_cap_pct",
    "pct_1rm_cap",
    "rir_floor",
)

SAFETY_RULES = {
    "R-SAFE-TARGET-HELD-ON-LOAD-UP":
        "the load rose while the rep target was held or raised -- SPEC A8: this "
        "walks the user toward failure reps (the 2026-08-25 deadlift path)",
    "R-SAFE-TARGET-ABOVE-CAPACITY":
        "the target exceeds what the load supports at the slot's RIR floor",
    "R-SAFE-LOAD-JUMP-KG":
        "the session-over-session load increase exceeds the absolute kg cap",
    "R-SAFE-LOAD-JUMP-PCT":
        "the session-over-session load increase exceeds the percentage cap",
    "R-SAFE-PCT-1RM":
        "the prescribed load exceeds the %1RM cap",
}


@dataclass(frozen=True)
class SafetyCaps:
    """Cap values read from store rows. Never authored in code (SPEC A8)."""

    session_load_increase_cap_kg: float = None
    session_load_increase_cap_pct: float = None
    pct_1rm_cap: float = None
    rir_floor: int = None

    @classmethod
    def from_config(cls, config):
        """Build from a caller-supplied mapping (a store row rendered as dict).

        Every key in SAFETY_CAP_KEYS must be PRESENT. A present value of None
        means "this cap is not configured" and disables exactly that rule, which
        the ruling then reports in `unconfigured`.
        """
        if not hasattr(config, "get") or not hasattr(config, "__contains__"):
            raise PrescriptionInputError(
                "config", config, "expected a mapping of cap keys to values")
        absent = [k for k in SAFETY_CAP_KEYS if k not in config]
        if absent:
            raise MissingSafetyCapError(absent)
        return cls(
            session_load_increase_cap_kg=_number(
                "session_load_increase_cap_kg",
                config["session_load_increase_cap_kg"], 0.0, allow_none=True),
            session_load_increase_cap_pct=_number(
                "session_load_increase_cap_pct",
                config["session_load_increase_cap_pct"], 0.0, allow_none=True),
            pct_1rm_cap=_number(
                "pct_1rm_cap", config["pct_1rm_cap"], 0.0, allow_none=True),
            rir_floor=_count(
                "rir_floor", config["rir_floor"], 0, allow_none=True),
        )


@dataclass(frozen=True)
class SafetyRuling:
    """Which gate rules fired, and which could not be evaluated.

    Like Verdict, this carries no free text: `fired` holds SAFETY_RULES keys.
    """

    unsafe: bool
    fired: tuple = ()
    unconfigured: tuple = ()
    plausible: PlausibleRange = None
    load_delta_kg: float = None
    load_delta_pct: float = None
    pct_1rm: float = None


def safety_ruling(load, target_reps, caps,
                  e1rm=None, prev_load=None, prev_target_reps=None):
    """Evaluate the A8 gate rules for a prescription about to be published.

    Args:
        load, target_reps: the prescription under test.
        caps:              SafetyCaps, or a mapping accepted by from_config().
                           The session-over-session load-increase cap is read
                           from here, never hardcoded (SPEC A8).
        e1rm:              needed for the %1RM cap and the capacity rule.
        prev_load, prev_target_reps: the previous session's prescription, needed
                           for the load-up/target-held rule.
    """
    if not isinstance(caps, SafetyCaps):
        caps = SafetyCaps.from_config(caps)

    load = _number("load", load, minimum=0.0)
    if load <= 0:
        raise PrescriptionInputError("load", load, "must be > 0")
    target_reps = _count("target_reps", target_reps, minimum=1)
    e1rm = _number("e1rm", e1rm, minimum=0.0, allow_none=True)
    prev_load = _number("prev_load", prev_load, minimum=0.0, allow_none=True)
    prev_target_reps = _count(
        "prev_target_reps", prev_target_reps, minimum=1, allow_none=True)

    fired = []
    unconfigured = []
    band = None
    delta_kg = None
    delta_pct = None
    pct = None

    # Rule 1 -- the defect's own shape. Load up, target held or raised.
    if prev_load is not None and prev_target_reps is not None:
        if load > prev_load and target_reps >= prev_target_reps:
            fired.append("R-SAFE-TARGET-HELD-ON-LOAD-UP")

    # Rules 2 and 3 -- the session-over-session load-increase caps.
    if prev_load is not None and prev_load > 0:
        delta_kg = load - prev_load
        delta_pct = 100.0 * delta_kg / prev_load
        if caps.session_load_increase_cap_kg is None:
            unconfigured.append("R-SAFE-LOAD-JUMP-KG")
        elif delta_kg > caps.session_load_increase_cap_kg:
            fired.append("R-SAFE-LOAD-JUMP-KG")
        if caps.session_load_increase_cap_pct is None:
            unconfigured.append("R-SAFE-LOAD-JUMP-PCT")
        elif delta_pct > caps.session_load_increase_cap_pct:
            fired.append("R-SAFE-LOAD-JUMP-PCT")

    # Rules 4 and 5 -- intensity ceiling and capacity, both need an e1RM.
    if e1rm is not None and e1rm > 0:
        pct = pct_of_1rm(load, e1rm)
        if caps.pct_1rm_cap is None:
            unconfigured.append("R-SAFE-PCT-1RM")
        elif pct > caps.pct_1rm_cap:
            fired.append("R-SAFE-PCT-1RM")
        if caps.rir_floor is None:
            unconfigured.append("R-SAFE-TARGET-ABOVE-CAPACITY")
        else:
            band = plausible_rep_target(load, e1rm, caps.rir_floor)
            if target_reps > band.high:
                fired.append("R-SAFE-TARGET-ABOVE-CAPACITY")

    return SafetyRuling(
        unsafe=bool(fired),
        fired=tuple(fired),
        unconfigured=tuple(unconfigured),
        plausible=band,
        load_delta_kg=delta_kg,
        load_delta_pct=delta_pct,
        pct_1rm=pct,
    )


def is_unsafe_prescription(load, target_reps, caps,
                           e1rm=None, prev_load=None, prev_target_reps=None):
    """TOOL-LAYER GATE (SPEC A8). True = this prescription must not publish.

    The caller hard-gates on this boolean. It is never rendered as prose and
    never delegated to a prompt rule. Use safety_ruling() when the caller needs
    to know WHICH rule fired.
    """
    return safety_ruling(
        load, target_reps, caps,
        e1rm=e1rm, prev_load=prev_load, prev_target_reps=prev_target_reps,
    ).unsafe
