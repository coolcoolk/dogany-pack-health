#!/usr/bin/env python3
# session_harness -- workout-session hook harness (SPEC 2026-08-25, pack).
#
# Four modules and a carrier package, five jobs:
#   events.py       the 11-event roster + the DELIVERY table + handler registry
#                   + coverage()
#   blocks.py       the block contract (slot x delivery target) and THE
#                   PUBLISHER (ordering + refusals)
#   set_kind.py     the prep/ramp/working/hold derivation table (data, not
#                   branches)
#   prescription.py the load<->rep prescription axis: plausibility-first
#                   verdicts (defect #12) + the A8 safety gate
#   hooks/          executable carriers for roster events (turn_pre.py). Each
#                   carrier is ALSO a standalone script, so it is not imported
#                   here -- importing the package only makes the namespace
#                   reachable, it does not pull a carrier into this process.
#
# Design proposition (SPEC): enumerate the points and the empty ones become
# visible; make the order a contract and it cannot be broken. The delivery
# target is the same move applied to the surface: make "pin edit vs new bubble"
# a value and the owner's 06:48 ruling stops being a comment.
#
# Status: pack-side build. hooks/turn_pre.py is declared (2026-09-30) through
# routines/bundle/session-progress-inject.py; the rest is not wired. No DB access, no SQL, no
# migration -- this pack is zero-schema by invariant (see repo README). The
# workout_sets set_kind/target_reps/hold_sec columns are a kit_life migration
# owned elsewhere; this module only names the tokens.
#
# stdlib only.

from . import hooks  # noqa: F401
from .blocks import (  # noqa: F401
    INSTRUCTIONAL_PHRASES,
    Block,
    BubbleBudgetError,
    BubbleLedger,
    BubbleScope,
    DeliveryPolicy,
    EmptyKeyboardError,
    HookResult,
    InstructionalProseError,
    InvalidBlockError,
    KeyboardSpec,
    MisplacedKeyboardError,
    MissingTableError,
    PublishError,
    Slot,
    TableRepublishError,
    Target,
    TargetNotAllowedError,
    bubble_count,
    enforce_delivery,
    find_instructional_phrases,
    publish,
)
from .events import (  # noqa: F401
    BUBBLE_BUDGET,
    CONTRACTS,
    DELIVERY,
    HANDLERS,
    MAX_NEW_BUBBLES_PER_EXERCISE,
    MAX_NEW_BUBBLES_PER_SESSION,
    MAX_NEW_BUBBLES_PER_SET,
    Coverage,
    Event,
    EventContract,
    MissingCueError,
    RequiredSlotMissingError,
    SlotNotPermittedError,
    UnknownEventError,
    contract,
    coverage,
    delivery,
    dispatch,
    emit,
    handler_for,
    is_stub,
    new_ledger,
    register,
)
from .prescription import (  # noqa: F401
    PCT_OF_1RM,
    PLAUSIBLE_BAND_SLACK,
    RULES,
    SAFETY_CAP_KEYS,
    SAFETY_RULES,
    TABLE_MAX_REPS,
    TABLE_MIN_REPS,
    AdjustDirection,
    Capacity,
    MissingSafetyCapError,
    Outcome,
    PlausibleRange,
    PrescriptionInputError,
    SafetyCaps,
    SafetyRuling,
    Verdict,
    evaluate,
    implied_e1rm,
    is_unsafe_prescription,
    no_verdict,
    pct_of_1rm,
    plausible_rep_target,
    reps_to_failure,
    safety_ruling,
    should_emit_summary,
)
from .set_kind import (  # noqa: F401
    CUE_EXERCISE_TARGET,
    CUE_HOLD_DURATION,
    CUE_LOAD_TARGET,
    CUE_LOAD_TARGET_RIR,
    DERIVATION_TABLE,
    KEYBOARD_REPS_DRILLDOWN,
    KEYBOARD_TIMER_DONE,
    DerivedSpec,
    MarkerContractPendingError,
    SetKind,
    UnknownSetKindError,
    coerce,
    counts_toward_volume,
    derive,
    keyboard_kind_for,
    kinds_with_keyboard,
    render_keyboard_marker,
)
