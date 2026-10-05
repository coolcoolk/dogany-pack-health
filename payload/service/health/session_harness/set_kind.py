#!/usr/bin/env python3
# set_kind.py -- set_kind derivation table (SPEC A2.3, pack payload).
#
# Every unit of work in a workout session is a `workout_sets` row. prep / ramp /
# working / hold are NOT separate concepts -- they are values of one column, and
# everything that differs between them is DERIVED FROM A TABLE, never from an
# if/elif chain. That table is DERIVATION_TABLE below; it is the whole module.
#
# Why a table and not branches: spec defects #2 #3 #6 #10 all came from prep
# being a second-class citizen living OUTSIDE the set pipeline, and from the
# timer keyboard leaking onto working sets. With a total table there is no
# outside, and a `timer_done` keyboard is structurally underivable for any kind
# other than `hold` -- there is no row that produces it.
#
# SEAM (NOT resolved here): the concrete bridge marker payload that carries a
# keyboard to Telegram. keyboard_kind is a SYMBOLIC token only. See
# render_keyboard_marker() at the bottom.
#
# i18n (SPEC Gate 3): every token in this module is English. No Korean.
#
# stdlib only.

from dataclasses import dataclass
from enum import Enum


# ---------------------------------------------------------------------------
# Tokens. DB-level values -- English, lowercase, stable. `set_kind` column of
# workout_sets is constrained to exactly these four.
# ---------------------------------------------------------------------------
class SetKind(str, Enum):
    PREP = "prep"
    RAMP = "ramp"
    WORKING = "working"
    HOLD = "hold"


# Symbolic keyboard tokens. These are NOT bridge markers -- see the seam note.
KEYBOARD_REPS_DRILLDOWN = "reps_drilldown"
KEYBOARD_TIMER_DONE = "timer_done"

# Symbolic cue shapes (what fields the CUE block must carry, not the prose).
CUE_EXERCISE_TARGET = "exercise_target"        # exercise name + target
CUE_LOAD_TARGET = "load_target"                # load + target
CUE_LOAD_TARGET_RIR = "load_target_rir"        # load + target + RIR
CUE_HOLD_DURATION = "hold_duration"            # duration


class UnknownSetKindError(ValueError):
    """Raised for a set_kind that has no row in DERIVATION_TABLE.

    There is deliberately no fallback: a silent default is how `working`
    semantics leaked onto prep rows in the first place.
    """

    def __init__(self, given):
        self.given = given
        super().__init__(
            "R-SETKIND-UNKNOWN: no derivation row for set_kind %r; known kinds "
            "are %s (no default is applied -- a set_kind must be declared)"
            % (given, ", ".join(k.value for k in SetKind))
        )


@dataclass(frozen=True)
class DerivedSpec:
    """One row of the SPEC A2.3 derivation table."""

    set_kind: SetKind
    in_table: bool
    keyboard_kind: str
    counts_toward_volume: bool
    cue_shape: str


# ---------------------------------------------------------------------------
# THE TABLE (SPEC A2.3). Read it; do not branch on it.
#
#   set_kind | in_table | keyboard        | volume | cue shape
#   ---------|----------|-----------------|--------|-------------------------
#   prep     | yes      | reps drilldown  | no     | exercise name + target
#   ramp     | yes      | reps drilldown  | no     | load + target
#   working  | yes      | reps drilldown  | yes    | load + target + RIR
#   hold     | yes      | timer (done)    | yes    | duration
# ---------------------------------------------------------------------------
DERIVATION_TABLE = {
    SetKind.PREP: DerivedSpec(
        set_kind=SetKind.PREP,
        in_table=True,
        keyboard_kind=KEYBOARD_REPS_DRILLDOWN,
        counts_toward_volume=False,
        cue_shape=CUE_EXERCISE_TARGET,
    ),
    SetKind.RAMP: DerivedSpec(
        set_kind=SetKind.RAMP,
        in_table=True,
        keyboard_kind=KEYBOARD_REPS_DRILLDOWN,
        counts_toward_volume=False,
        cue_shape=CUE_LOAD_TARGET,
    ),
    SetKind.WORKING: DerivedSpec(
        set_kind=SetKind.WORKING,
        in_table=True,
        keyboard_kind=KEYBOARD_REPS_DRILLDOWN,
        counts_toward_volume=True,
        cue_shape=CUE_LOAD_TARGET_RIR,
    ),
    SetKind.HOLD: DerivedSpec(
        set_kind=SetKind.HOLD,
        in_table=True,
        keyboard_kind=KEYBOARD_TIMER_DONE,
        counts_toward_volume=True,
        cue_shape=CUE_HOLD_DURATION,
    ),
}


def coerce(set_kind):
    """Normalize a str / SetKind into a SetKind. Raises on anything else."""
    if isinstance(set_kind, SetKind):
        return set_kind
    if isinstance(set_kind, str):
        try:
            return SetKind(set_kind)
        except ValueError:
            raise UnknownSetKindError(set_kind) from None
    raise UnknownSetKindError(set_kind)


def derive(set_kind):
    """set_kind -> DerivedSpec. Table lookup, never a branch, never a default."""
    kind = coerce(set_kind)
    try:
        return DERIVATION_TABLE[kind]
    except KeyError:
        # Only reachable if SetKind gains a member without a table row -- that
        # is a build-time defect and must be loud, not defaulted.
        raise UnknownSetKindError(kind.value) from None


def keyboard_kind_for(set_kind):
    """Symbolic keyboard token for a kind. `timer_done` is derivable ONLY from
    `hold` (SPEC defect #6): no other row carries that token."""
    return derive(set_kind).keyboard_kind


def counts_toward_volume(set_kind):
    return derive(set_kind).counts_toward_volume


def kinds_with_keyboard(keyboard_kind):
    """Inverse index over the table -- which kinds can produce this keyboard.
    Used to assert defect #6 structurally rather than by inspection."""
    return tuple(
        k for k, row in DERIVATION_TABLE.items()
        if row.keyboard_kind == keyboard_kind
    )


# ---------------------------------------------------------------------------
# BRIDGE MARKER SEAM -- deliberately unimplemented.
#
# TODO(seam): the wire format that hands a KeyboardSpec to the bridge (the
# `[[IDRILL:<arm_id>]]`-class marker contract, SPEC A2.6 "seam -- 합의 필요")
# is still being characterized against IDRILL-ARM-CONTRACT.md by the bridge/
# marker agent. The bridge idrill engine and actual keyboard attachment are
# the framework's lane. Until that contract is pinned, this module refuses to guess a
# marker format -- keyboard_kind stays symbolic and rendering raises.
# ---------------------------------------------------------------------------
class MarkerContractPendingError(NotImplementedError):
    pass


def render_keyboard_marker(keyboard_kind, arm_id=None):
    """Symbolic keyboard token -> bridge marker string. NOT IMPLEMENTED."""
    raise MarkerContractPendingError(
        "keyboard marker rendering is not yet wired: the hook->bridge marker "
        "contract (IDRILL-ARM-CONTRACT extension, SPEC A2.6) is still being "
        "characterized. Refusing to guess a marker format for "
        "keyboard_kind=%r arm_id=%r." % (keyboard_kind, arm_id)
    )
