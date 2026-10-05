#!/usr/bin/env python3
# events.py -- the 11-event hook roster (SPEC A2.1, pack payload).
#
# The point of this file is ENUMERATION. A call chain has no enumerated points,
# so a missing point is invisible and gets patched by cutting into the chain
# wherever the defect surfaced -- which is why the same defect class kept
# recurring (12 observed in 43 minutes on 2026-08-25, 9 of them "there is no
# hook there"). Enumerate the points and the empty ones become visible.
#
# Therefore: the roster is COMPLETE even where handlers are stubs. A stub that
# raises is a visible gap; an absent event is an invisible one. coverage()
# turns that gap into a number (SPEC A1 success metric 1: hook coverage).
#
# Self-declaration is forbidden (SPEC A5, DGN-071): a hook cannot invent a new
# event. register() refuses anything outside this roster.
#
# i18n (SPEC Gate 3): all event and slot tokens are English.
#
# stdlib only.

from dataclasses import dataclass
from enum import Enum

from .blocks import (
    Block,
    BubbleLedger,
    BubbleScope,
    DeliveryPolicy,
    PublishError,
    Slot,
    Target,
    publish,
)


class Event(str, Enum):
    """The complete hook roster. Names are the contract tokens from SPEC A2.1
    and are used verbatim in wiring (settings.json, marker payloads, logs)."""

    SessionOpen = "SessionOpen"
    ExerciseEnter = "ExerciseEnter"
    SetArm = "SetArm"
    SetLogged = "SetLogged"
    RestStart = "RestStart"
    RestTick = "RestTick"
    RestEnd = "RestEnd"
    ExerciseExit = "ExerciseExit"
    SessionClose = "SessionClose"
    TurnPre = "TurnPre"
    TurnPost = "TurnPost"


@dataclass(frozen=True)
class EventContract:
    """What one event is allowed and required to emit.

    may_emit:       slots this event is permitted to produce at all
    required:       slots that MUST be present for the event to publish
    table_required: whether a non-empty TABLE is mandatory (feeds publish())
    guarantee:      one-line statement of what the event guarantees (SPEC A2.1)
    """

    event: Event
    may_emit: frozenset
    required: frozenset
    table_required: bool
    guarantee: str


def _c(event, may_emit, required, table_required, guarantee):
    return EventContract(
        event=event,
        may_emit=frozenset(may_emit),
        required=frozenset(required),
        table_required=table_required,
        guarantee=guarantee,
    )


# ---------------------------------------------------------------------------
# THE ROSTER (SPEC A2.1). Flow shape:
#
#   SessionOpen
#     ExerciseEnter                (exercise 1..N)
#       SetArm / SetLogged         (set 1..M -- prep, ramp, working, hold alike)
#       RestStart / RestTick / RestEnd
#     ExerciseExit
#   SessionClose
#
#   TurnPre / TurnPost             (orthogonal -- every model turn)
#
# TurnPre and TurnPost emit NO user-visible blocks: TurnPre injects live cursor
# state into context (read-only, never blocks, no-op when no session is active)
# and TurnPost verifies the ordering contract and logs violations. Their
# may_emit is deliberately empty.
#
# TABLE POLICY ACROSS THE ROSTER (owner ruling 2026-08-25 06:48 -- the progress
# table has ONE update path, the pinned-card edit; chat republication is itself a
# defect). table_required is therefore a narrow exception:
#   SessionOpen     True  -- mints the pinned card; there must be one to pin
#   ExerciseEnter   True  -- card content delivered as a PIN EDIT, not a bubble
#                            (ExerciseEnter is not a sanctioned bubble point, A5)
#   SetLogged       True  -- post-commit table render, also a PIN EDIT; this is
#                            the one place prose-instead-of-table was the defect
#                            being fixed (#8)
#   ExerciseExit    True  -- close-out CARD, a distinct artifact the owner asked
#                            for (#1), not a progress-table update
#   SessionClose    True  -- same, session close-out card
#   SetArm          False -- sanctioned new bubble; a table here IS the rejected
#                            republication
#   everything else False
# The pin-edit readings above are no longer assumptions: the DELIVERY table
# below carries the pin-edit / new-bubble axis as data and the publisher refuses
# on it (blocks.Target, R-TABLE-REPUBLISH).
# ---------------------------------------------------------------------------
CONTRACTS = {
    Event.SessionOpen: _c(
        Event.SessionOpen,
        may_emit={Slot.TABLE, Slot.CUE, Slot.PROSE},
        required={Slot.TABLE},
        table_required=True,
        guarantee="Publish the session card; fix the exercise roster.",
    ),
    Event.ExerciseEnter: _c(
        Event.ExerciseEnter,
        may_emit={Slot.TABLE, Slot.CUE, Slot.PROSE},
        required={Slot.TABLE, Slot.CUE},
        table_required=True,
        guarantee=(
            "Exercise card + ramp/prep set rows created + first cue "
            "(defects #2 #3 #10)."
        ),
    ),
    Event.SetArm: _c(
        Event.SetArm,
        may_emit={Slot.TABLE, Slot.CUE, Slot.KEYBOARD, Slot.PROSE},
        # NO TABLE REQUIREMENT (owner ruling 2026-08-25 06:48). SetArm is one of
        # the three sanctioned new-bubble points (A5), so a mandatory TABLE here
        # would republish the progress table into the chat on EVERY set -- the
        # exact behaviour the owner rejected. The table's only update path is the
        # pinned-card edit. TABLE stays PERMITTED (a caller with a legitimate
        # card to mint may emit one, and it still sorts first) but is never
        # forced. What a set-start MUST carry is a concrete cue: a set-start with
        # no load/reps is defect #3 ("오버헤드 슈러그로 진행해주세요").
        required={Slot.CUE, Slot.KEYBOARD},
        table_required=False,
        guarantee=(
            "Set-start block: a concrete cue plus the set_kind-derived keyboard "
            "(defects #3 #5 #6 #9 #11). No table republication."
        ),
    ),
    Event.SetLogged: _c(
        Event.SetLogged,
        may_emit={Slot.TABLE, Slot.CUE, Slot.PROSE},
        required={Slot.TABLE},
        table_required=True,
        guarantee=(
            "Render the table AFTER the commit lands, then the next cue "
            "(defects #7 #8)."
        ),
    ),
    Event.RestStart: _c(
        Event.RestStart,
        may_emit={Slot.CUE, Slot.KEYBOARD},
        required={Slot.CUE},
        table_required=False,
        guarantee="Open the rest window from a single deadline source.",
    ),
    Event.RestTick: _c(
        Event.RestTick,
        # Counter edit only -- a tick must never grow a new bubble or prose
        # (SPEC A5 bubble budget).
        may_emit={Slot.CUE},
        required={Slot.CUE},
        table_required=False,
        guarantee="Edit the rest counter; derive milestones from that deadline.",
    ),
    Event.RestEnd: _c(
        Event.RestEnd,
        may_emit={Slot.CUE, Slot.KEYBOARD, Slot.PROSE},
        required={Slot.CUE},
        table_required=False,
        guarantee="Rest complete; hand off to the next set.",
    ),
    Event.ExerciseExit: _c(
        Event.ExerciseExit,
        may_emit={Slot.TABLE, Slot.CUE, Slot.PROSE},
        required={Slot.TABLE},
        table_required=True,
        guarantee=(
            "Exercise close-out card: final table plus the exercise verdict "
            "(defect #1). PROSE is omitted when no verdict is supplied."
        ),
    ),
    Event.SessionClose: _c(
        Event.SessionClose,
        may_emit={Slot.TABLE, Slot.CUE, Slot.PROSE},
        required={Slot.TABLE},
        table_required=True,
        guarantee="Session close-out card.",
    ),
    Event.TurnPre: _c(
        Event.TurnPre,
        may_emit=frozenset(),
        required=frozenset(),
        table_required=False,
        guarantee=(
            "Inject live cursor state into context (defect #4). Read-only, "
            "never blocks, no-op when no session is active."
        ),
    ),
    Event.TurnPost: _c(
        Event.TurnPost,
        may_emit=frozenset(),
        required=frozenset(),
        table_required=False,
        guarantee="Verify the ordering contract; log violations (defect #7).",
    ),
}


# ---------------------------------------------------------------------------
# A5 BUBBLE BUDGET -- the numbers, once, as named constants.
#
# SPEC A5 (신규 리스크 mitigation): "인접 훅의 블록은 가능한 한 핀 카드 edit로
# 흡수하고 신규 버블은 (a) 세트 시작, (b) 휴식 완료, (c) 종목 마감 세 지점으로
# 제한한다 ... 세트당 신규 버블 <= 2, 종목당 <= 1."
#
# Per-set 2 is exactly SetArm (set start) + RestEnd (rest complete). Per-exercise
# 1 is exactly ExerciseExit (exercise close). The two sanctioned-point lists and
# the two numbers are the same statement counted two ways, which is why the
# budget can be enforced without naming any event here.
#
# SESSION is an extension of the same principle, not a quote from A5: A5 counts
# per set and per exercise only. A session has exactly two card moments -- the
# SessionOpen mint and the SessionClose card -- and neither recurs, so neither
# can drive the noise A5 is about. Declared as a constant rather than left
# unbounded so no future event can quietly add a third session-level bubble.
# ---------------------------------------------------------------------------
MAX_NEW_BUBBLES_PER_SET = 2
MAX_NEW_BUBBLES_PER_EXERCISE = 1
MAX_NEW_BUBBLES_PER_SESSION = 2

BUBBLE_BUDGET = {
    BubbleScope.SET: MAX_NEW_BUBBLES_PER_SET,
    BubbleScope.EXERCISE: MAX_NEW_BUBBLES_PER_EXERCISE,
    BubbleScope.SESSION: MAX_NEW_BUBBLES_PER_SESSION,
}


def _d(allowed, table_targets, scope, opens=()):
    return DeliveryPolicy(
        allowed=frozenset(allowed),
        table_targets=frozenset(table_targets),
        scope=scope,
        opens=frozenset(opens),
    )


# ---------------------------------------------------------------------------
# THE DELIVERY TABLE -- per event, WHICH SURFACE its blocks may land on.
# Data, exactly like CONTRACTS; read it, do not branch on it.
#
# Derived from two rulings and nothing else:
#
#   (1) Owner ruling 2026-08-25 06:48 -- the session progress table has EXACTLY
#       ONE update path: an edit of the PINNED message. A second copy of it in
#       the chat is the reported defect ("세션 진행표 채팅 재발행"). => TABLE is
#       PIN_EDIT everywhere EXCEPT where a card is genuinely MINTED or CLOSED.
#   (2) SPEC A5 -- new bubbles are limited to three sanctioned points:
#       (a) set start, (b) rest complete, (c) exercise close. => NEW_BUBBLE is
#       permitted at SetArm / RestEnd / ExerciseExit and nowhere else in the
#       set-and-exercise loop.
#
#   event         | allowed targets       | TABLE may be | why
#   --------------|-----------------------|--------------|--------------------
#   SessionOpen   | NEW_BUBBLE            | NEW_BUBBLE   | MINTS the pin
#   ExerciseEnter | PIN_EDIT              | PIN_EDIT     | not a bubble point
#   SetArm        | NEW_BUBBLE, PIN_EDIT  | PIN_EDIT     | bubble point (a)
#   SetLogged     | PIN_EDIT              | PIN_EDIT     | not a bubble point
#   RestStart     | PIN_EDIT              | (no TABLE)   | absorbed into the pin
#   RestTick      | PIN_EDIT              | (no TABLE)   | counter edit only
#   RestEnd       | NEW_BUBBLE, PIN_EDIT  | (no TABLE)   | bubble point (b)
#   ExerciseExit  | NEW_BUBBLE, PIN_EDIT  | both         | bubble point (c)
#   SessionClose  | NEW_BUBBLE, PIN_EDIT  | both         | close-out card
#   TurnPre       | none                  | none         | emits nothing
#   TurnPost      | none                  | none         | emits nothing
#
# Two entries deserve their justification spelled out, because both look like
# exceptions to ruling (1) and neither is:
#
#   SessionOpen mints the pin. A PIN_EDIT is impossible before a pinned message
#   exists, so the mint MUST be a new bubble -- and a mint is not a
#   republication, because there is nothing yet to republish. PIN_EDIT is
#   therefore NOT allowed at SessionOpen: it would be an edit of nothing.
#
#   ExerciseExit / SessionClose emit a CLOSE-OUT CARD, a distinct artifact the
#   owner asked for (defect #1) -- final table plus verdict, one per exercise or
#   session. It is not an update of the progress table, so shipping it as a new
#   bubble does not touch ruling (1)'s single update path.
#
# SetArm is the sharp one: it IS a sanctioned bubble point, so NEW_BUBBLE is
# allowed for its cue and keyboard -- but its table_targets stay PIN_EDIT-only.
# A bubbled TABLE at a per-set event is the republication itself, and the fact
# that the event may bubble does not license the table to ride along.
# ---------------------------------------------------------------------------
DELIVERY = {
    Event.SessionOpen: _d(
        allowed={Target.NEW_BUBBLE},
        table_targets={Target.NEW_BUBBLE},
        scope=BubbleScope.SESSION,
        # A session start resets everything downstream of it.
        opens={BubbleScope.SESSION, BubbleScope.EXERCISE, BubbleScope.SET},
    ),
    Event.ExerciseEnter: _d(
        allowed={Target.PIN_EDIT},
        table_targets={Target.PIN_EDIT},
        scope=BubbleScope.EXERCISE,
        opens={BubbleScope.EXERCISE, BubbleScope.SET},
    ),
    Event.SetArm: _d(
        allowed={Target.NEW_BUBBLE, Target.PIN_EDIT},
        table_targets={Target.PIN_EDIT},
        scope=BubbleScope.SET,
        opens={BubbleScope.SET},
    ),
    Event.SetLogged: _d(
        allowed={Target.PIN_EDIT},
        table_targets={Target.PIN_EDIT},
        scope=BubbleScope.SET,
    ),
    Event.RestStart: _d(
        allowed={Target.PIN_EDIT},
        table_targets=frozenset(),
        scope=BubbleScope.SET,
    ),
    Event.RestTick: _d(
        allowed={Target.PIN_EDIT},
        table_targets=frozenset(),
        scope=BubbleScope.SET,
    ),
    Event.RestEnd: _d(
        allowed={Target.NEW_BUBBLE, Target.PIN_EDIT},
        table_targets=frozenset(),
        scope=BubbleScope.SET,
    ),
    Event.ExerciseExit: _d(
        allowed={Target.NEW_BUBBLE, Target.PIN_EDIT},
        table_targets={Target.NEW_BUBBLE, Target.PIN_EDIT},
        scope=BubbleScope.EXERCISE,
    ),
    Event.SessionClose: _d(
        allowed={Target.NEW_BUBBLE, Target.PIN_EDIT},
        table_targets={Target.NEW_BUBBLE, Target.PIN_EDIT},
        scope=BubbleScope.SESSION,
    ),
    Event.TurnPre: _d(
        allowed=frozenset(), table_targets=frozenset(), scope=None),
    Event.TurnPost: _d(
        allowed=frozenset(), table_targets=frozenset(), scope=None),
}


# ---------------------------------------------------------------------------
# Contract refusals. They subclass PublishError so a caller catches one family.
# ---------------------------------------------------------------------------
class SlotNotPermittedError(PublishError):
    rule = "R-SLOT-NOT-PERMITTED"


class RequiredSlotMissingError(PublishError):
    rule = "R-SLOT-REQUIRED"


class MissingCueError(RequiredSlotMissingError):
    """A required CUE that is absent or empty.

    Named separately from the generic missing-slot refusal because it is the
    load-bearing one now that most events emit no table: with the progress table
    updated only by pin edit, the CUE is what a set-start actually delivers. A
    cue-less set-start is defect #3 -- "오버헤드 슈러그로 진행해주세요" with no
    load and no reps. An empty CUE payload is the same defect wearing a block.
    """

    rule = "R-CUE-REQUIRED"


class UnknownEventError(KeyError):
    """Raised when an event outside the roster is used. Hooks may not
    self-declare events (SPEC A5, DGN-071)."""

    def __init__(self, given):
        self.given = given
        super().__init__(
            "R-EVENT-UNKNOWN: %r is not on the hook roster; hooks may not "
            "self-declare events. Roster: %s"
            % (given, ", ".join(e.value for e in Event))
        )


def contract(event):
    """Event (or its token) -> EventContract. Raises outside the roster."""
    if not isinstance(event, Event):
        try:
            event = Event(event)
        except ValueError:
            raise UnknownEventError(event) from None
    return CONTRACTS[event]


def delivery(event):
    """Event (or its token) -> DeliveryPolicy. Raises outside the roster."""
    return DELIVERY[contract(event).event]


def new_ledger():
    """A fresh A5 bubble ledger, wired to BUBBLE_BUDGET. One per session."""
    return BubbleLedger(BUBBLE_BUDGET)


def emit(event, blocks, ledger=None):
    """Validate `blocks` against the event contract, then publish them.

    This is the only sanctioned way to produce a HookResult: slot permission and
    required-slot checks run first, then blocks.publish() applies the ordering
    and refusal rules with this event's table requirement AND its delivery
    policy.

    `ledger` is an optional BubbleLedger (see new_ledger()). Pass the same one
    through a whole session to have the A5 per-set / per-exercise bubble budget
    accounted; a single publication cannot exceed it on its own.
    """
    spec = contract(event)
    blocks = list(blocks)

    for b in blocks:
        if not isinstance(b, Block):
            raise SlotNotPermittedError(
                "%s received a non-Block value %r" % (spec.event.value, b),
                block=b)
        if b.slot not in spec.may_emit:
            raise SlotNotPermittedError(
                "%s may not emit the %s slot (permitted: %s)"
                % (spec.event.value, b.slot.name,
                   ", ".join(sorted(s.name for s in spec.may_emit)) or "none"),
                block=b)

    present = {b.slot for b in blocks}
    missing = spec.required - present

    # R-CUE-REQUIRED fires ahead of the generic refusal: an absent cue is a
    # different failure from an absent card, and it is the one that reaches the
    # owner as "what am I supposed to lift?".
    if Slot.CUE in missing:
        raise MissingCueError(
            "%s requires a CUE block and none was supplied; a publication with "
            "no cue tells the user to proceed without a load or a rep target"
            % spec.event.value, block=None)
    if Slot.CUE in spec.required:
        cues = [b for b in blocks if b.slot is Slot.CUE]
        if not any(b.payload and b.payload.strip() for b in cues):
            raise MissingCueError(
                "%s requires a non-empty CUE block but every CUE block is empty"
                % spec.event.value, block=cues[0])

    if missing:
        raise RequiredSlotMissingError(
            "%s requires the %s slot(s) and they are absent"
            % (spec.event.value, ", ".join(sorted(s.name for s in missing))),
            block=None)

    return publish(blocks, require_table=spec.table_required,
                   delivery=DELIVERY[spec.event], ledger=ledger)


# ---------------------------------------------------------------------------
# Handler registry. Every event has an entry; unwired events carry a stub that
# raises. A stub is a VISIBLE gap -- that is the design, not an oversight.
# ---------------------------------------------------------------------------
def _stub(event):
    def handler(ctx=None):
        raise NotImplementedError(
            "%s handler is not yet wired (SPEC A2.1 roster entry exists, "
            "implementation pending -- Phase 1). Register a real handler with "
            "session_harness.events.register(Event.%s, fn)."
            % (event.value, event.name)
        )

    handler.__name__ = "stub_%s" % event.value
    handler.__qualname__ = handler.__name__
    handler.is_stub = True
    handler.event = event
    return handler


HANDLERS = {event: _stub(event) for event in Event}


def register(event, fn):
    """Bind a real handler to a roster event. Refuses unknown events."""
    spec = contract(event)
    if not callable(fn):
        raise TypeError(
            "R-HANDLER-TYPE: handler for %s must be callable, got %r"
            % (spec.event.value, fn))
    HANDLERS[spec.event] = fn
    return fn


def handler_for(event):
    return HANDLERS[contract(event).event]


def is_stub(event):
    return getattr(handler_for(event), "is_stub", False) is True


def dispatch(event, ctx=None):
    """Run an event's handler. A stub raises NotImplementedError by design."""
    return handler_for(event)(ctx)


@dataclass(frozen=True)
class Coverage:
    """SPEC A1 success metric 1: hook coverage = wired / enumerated."""

    total: int
    implemented: int
    stub: int
    ratio: float
    stub_events: tuple

    def __str__(self):
        return "hook coverage %d/%d (%.0f%%); stubs: %s" % (
            self.implemented, self.total, self.ratio * 100,
            ", ".join(self.stub_events) or "none")


def coverage():
    """Report implemented vs stub handlers over the full roster."""
    stubs = tuple(e.value for e in Event if is_stub(e))
    total = len(Event)
    stub_n = len(stubs)
    implemented = total - stub_n
    return Coverage(
        total=total,
        implemented=implemented,
        stub=stub_n,
        ratio=(implemented / total) if total else 0.0,
        stub_events=stubs,
    )
