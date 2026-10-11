#!/usr/bin/env python3
# blocks.py -- hook block contract + publisher (SPEC A2.2, pack payload).
#
# A hook returns an ORDERED LIST OF BLOCKS, not prose. The publisher owns the
# ordering and the refusals; the caller (and the model behind it) owns neither.
# This is the point where "table first, words after" stops being a SKILL.md
# sentence and becomes a data structure -- the 8/22 owner directive that had
# recurred for three straight days (SPEC defect #7).
#
# Rules the publisher enforces AS CODE:
#   R-ORDER          blocks are emitted in slot order; caller order is discarded
#   R-KEYBOARD-PROSE a KEYBOARD present forbids operating instructions in PROSE
#                    -- the button IS the instruction (defect #9)
#   R-TABLE-REQUIRED a required TABLE that is missing/empty fails publication;
#                    prose may never stand in for a table (defect #8). Note the
#                    inverse is NOT a rule: most events must NOT emit a table at
#                    all -- see SLOT POLICY below.
#   R-KEYBOARD-EMPTY a KEYBOARD slot with no spec is a mislabeled prose block
#   R-KEYBOARD-SLOT  a keyboard spec may only ride in the KEYBOARD slot
#   R-TABLE-REPUBLISH a TABLE delivered as a NEW BUBBLE at an event that has no
#                    card to mint or close -- the owner's 06:48 ruling, made
#                    mechanical ("세션 진행표 채팅 재발행")
#   R-TARGET-NOT-ALLOWED a block delivered to a surface this event may not use
#   R-BUBBLE-BUDGET  more new bubbles inside one cadence scope than SPEC A5
#                    allows (per-set / per-exercise caps)
#
# Every refusal names the rule that fired and the block that violated it.
#
# i18n (SPEC Gate 3): all slot names and rule ids are English. The ONLY Korean
# in this module is INSTRUCTIONAL_PHRASES -- see the note on that constant.
#
# stdlib only.

from dataclasses import dataclass, field
from enum import Enum, IntEnum


# ---------------------------------------------------------------------------
# Slot ranking. The integer IS the emission order; there is no other ordering
# input. The model may write INTO the PROSE slot and nowhere else.
#
# SLOT POLICY -- TABLE is the exception, not the rule (owner ruling 2026-08-25
# 06:48): the session progress table has exactly ONE update path, an EDIT OF THE
# PINNED CARD. Republishing the table into the chat is itself a defect. So most
# events emit a CUE and no TABLE; a TABLE block is reserved for events that mint
# or close out a card. The ordering invariant is unconditional -- IF a TABLE is
# emitted it sorts first -- but "table first" must never be read as "table
# always". Defect #7 is about order WITHIN one publication; an event that
# publishes no table has no ordering hazard to guard.
# ---------------------------------------------------------------------------
class Slot(IntEnum):
    TABLE = 1      # set table / exercise card
    CUE = 2        # next instruction (load, reps, RIR, plate delta)
    KEYBOARD = 3   # inline keyboard
    PROSE = 4      # model sentences (optional)


# ---------------------------------------------------------------------------
# DELIVERY TARGET -- the second axis of a block. Slot answers "what is this and
# where does it sort"; Target answers "WHICH SURFACE does it land on".
#
# Without this axis Slot.TABLE means only "table content goes out", which cannot
# tell "edit the pinned card" apart from "post a new chat bubble" -- and those
# two are a RULING, not a rendering detail:
#
#   Owner ruling 2026-08-25 06:48 -- the session progress table has EXACTLY ONE
#   update path, an EDIT OF THE PINNED MESSAGE. Re-publishing the table into the
#   chat is itself the defect the owner complained about ("세션 진행표 채팅
#   재발행"). Before this enum that ruling lived only in comments; now it is a
#   value the publisher can refuse on.
#
# NOT AN IntEnum: there is no ranking between the two surfaces. Slot is an
# IntEnum because its integer IS the emission order; Target has no order to
# carry, so it is a str Enum like Event and SetKind (stable wire token).
#
# REQUIRED, NOT DEFAULTED -- Block.target has no default value on purpose:
#   1. No default is right. PIN_EDIT would silently swallow the three sanctioned
#      new-bubble points (SPEC A5: set start / rest complete / exercise close),
#      and NEW_BUBBLE would silently reproduce the exact defect the owner
#      complained about. The correct target differs per event, so any default is
#      wrong for roughly half the roster -- and wrong SILENTLY, which is the
#      failure mode this axis exists to end.
#   2. It is a ruling, not a convenience. Same reasoning as
#      set_kind.UnknownSetKindError: "a silent default is how `working`
#      semantics leaked onto prep rows in the first place." A caller that has
#      not decided which surface it is writing to has not finished thinking.
#   3. Omission is caught at construction time (TypeError from the dataclass),
#      the earliest and loudest point available -- not at publication, and not
#      in production as a duplicated table.
# ---------------------------------------------------------------------------
class Target(str, Enum):
    PIN_EDIT = "pin_edit"        # edit the pinned session/exercise card in place
    NEW_BUBBLE = "new_bubble"    # post a new message into the chat


# ---------------------------------------------------------------------------
# CADENCE SCOPES (SPEC A5). A budget is a property of a SEQUENCE of
# publications, so it needs a bucket to accumulate in.
#
# Why a bubble is counted PER PUBLICATION and not per block: the blocks of one
# publication that carry NEW_BUBBLE coalesce into ONE outgoing message (the
# KEYBOARD attaches to it; a keyboard is not a message of its own). So one
# publication is 0 or 1 new bubbles, and A5's numbers -- 세트당 신규 버블 <= 2,
# 종목당 <= 1 -- only mean anything when counted across the events of a set or
# an exercise. That is what BubbleLedger does.
# ---------------------------------------------------------------------------
class BubbleScope(str, Enum):
    SET = "set"
    EXERCISE = "exercise"
    SESSION = "session"


# ---------------------------------------------------------------------------
# RUNTIME-OUTPUT MATCHING DATA -- Korean by necessity, not by style.
#
# These are literal user-facing strings the publisher looks for inside PROSE
# payloads. They are data, not code: extend/replace this list (or pass `phrases`
# to publish()) as new offenders are observed. They are Korean because the
# runtime output being matched is Korean; this is the one carve-out from the
# English-tokens rule in SPEC Gate 3.
#
# Seeded with the observed offenders from the 2026-08-25 session (defect #9:
# "버튼 있는데 '아래에서 입력해주세요' 안내문구").
#
# Matching is whitespace-insensitive on both sides, so "선택해 주세요" and
# "선택해주세요" are the same needle.
# ---------------------------------------------------------------------------
INSTRUCTIONAL_PHRASES = (
    "아래에서",
    "입력해주세요",
    "눌러주세요",
    "선택해주세요",
)


@dataclass(frozen=True)
class KeyboardSpec:
    """An inline keyboard, described symbolically.

    `kind` is a symbolic token from set_kind.py (reps_drilldown / timer_done),
    never a bridge marker string. Marker rendering lives behind
    set_kind.render_keyboard_marker() and is not wired yet (SPEC A2.6 seam).
    """

    kind: str
    arm_id: str = None
    options: tuple = field(default_factory=tuple)


@dataclass(frozen=True)
class Block:
    """One publishable unit.

    `slot` is WHAT it is (and therefore where it sorts); `target` is WHICH
    SURFACE it lands on. Both are required -- see the Target docstring for why
    the delivery target is deliberately not defaulted.
    """

    slot: Slot
    target: Target
    payload: str = ""
    keyboard: KeyboardSpec = None


@dataclass(frozen=True)
class DeliveryPolicy:
    """What one event may deliver, and where. DATA -- see events.DELIVERY.

    allowed:       Targets any block of this event may carry at all
    table_targets: Targets a TABLE block specifically may carry. Narrower than
                   `allowed` wherever the event is a sanctioned bubble point but
                   still has no card to mint (SetArm), which is precisely the
                   owner's 06:48 ruling.
    scope:         which A5 cadence budget this event's bubble is charged to
                   (None for the events that emit nothing at all)
    opens:         cadence scopes this event RESETS when it publishes -- a new
                   set clears the per-set bubble count, a new exercise clears
                   the per-exercise one
    """

    allowed: frozenset
    table_targets: frozenset
    scope: BubbleScope = None
    opens: frozenset = frozenset()


# HookResult is the return type of every hook handler: an ordered list of
# Blocks, as produced by publish(). Ordering is the publisher's, not the
# caller's -- see R-ORDER.
HookResult = list


# ---------------------------------------------------------------------------
# Refusals
# ---------------------------------------------------------------------------
class PublishError(Exception):
    """Base for every publication refusal. Carries the rule id and the
    offending block so the failure names itself."""

    rule = "R-PUBLISH"

    def __init__(self, message, block=None):
        self.block = block
        super().__init__("%s: %s" % (self.rule, message))


class InvalidBlockError(PublishError):
    rule = "R-BLOCK-TYPE"


class InstructionalProseError(PublishError):
    rule = "R-KEYBOARD-PROSE"


class MissingTableError(PublishError):
    rule = "R-TABLE-REQUIRED"


class EmptyKeyboardError(PublishError):
    rule = "R-KEYBOARD-EMPTY"


class MisplacedKeyboardError(PublishError):
    rule = "R-KEYBOARD-SLOT"


class TargetNotAllowedError(PublishError):
    """A block delivered to a surface this event's policy does not permit."""

    rule = "R-TARGET-NOT-ALLOWED"


class TableRepublishError(TargetNotAllowedError):
    """A TABLE block delivered as a NEW BUBBLE where no card is minted or closed.

    Named separately from the generic target refusal -- and catchable as one,
    the same way MissingCueError is catchable as RequiredSlotMissingError --
    because it is the load-bearing one: this is the owner's 2026-08-25 06:48
    ruling made mechanical. The progress table has exactly ONE update path, an
    edit of the pinned message; a second copy of it in the chat is the defect
    the owner reported, not a formatting preference.
    """

    rule = "R-TABLE-REPUBLISH"


class BubbleBudgetError(PublishError):
    """More new bubbles inside one cadence scope than SPEC A5 allows."""

    rule = "R-BUBBLE-BUDGET"


# ---------------------------------------------------------------------------
# Publisher
# ---------------------------------------------------------------------------
def _squeeze(text):
    """Drop all whitespace so phrase matching survives spacing variants."""
    return "".join(str(text).split())


def _describe(block):
    """Short, quotable identification of a block for a refusal message."""
    if not isinstance(block, Block):
        return repr(block)
    head = block.payload if len(block.payload) <= 60 else block.payload[:57] + "..."
    return "%s block %r" % (block.slot.name, head)


def find_instructional_phrases(text, phrases=INSTRUCTIONAL_PHRASES):
    """Return the phrases from `phrases` present in `text` (whitespace-insensitive)."""
    hay = _squeeze(text)
    return tuple(p for p in phrases if _squeeze(p) in hay)


# ---------------------------------------------------------------------------
# Delivery enforcement
# ---------------------------------------------------------------------------
def bubble_count(blocks):
    """New bubbles ONE publication produces: 0 or 1.

    Not a block count. Every NEW_BUBBLE block of a single publication coalesces
    into one outgoing message -- see the BubbleScope note.
    """
    return 1 if any(b.target is Target.NEW_BUBBLE for b in blocks) else 0


def enforce_delivery(blocks, policy):
    """Apply the per-event delivery rules. Raises; returns None.

    Rule order is deliberate. R-TABLE-REPUBLISH runs FIRST so the owner's ruling
    names itself: at an event that permits no bubble at all, a bubbled TABLE
    violates both that rule and the generic target rule, and the useful refusal
    is the specific one. Same precedence pattern as events.MissingCueError
    firing ahead of the generic missing-slot refusal.
    """
    # R-TABLE-REPUBLISH
    for b in blocks:
        if b.slot is not Slot.TABLE:
            continue
        if b.target in policy.table_targets:
            continue
        if b.target is Target.NEW_BUBBLE:
            raise TableRepublishError(
                "%s is delivered as a NEW_BUBBLE, but this event mints no card "
                "and closes none: the session progress table has exactly one "
                "update path, an edit of the pinned message (owner ruling "
                "2026-08-25 06:48). Republishing the table into the chat is "
                "itself the defect. Permitted TABLE target(s) here: %s"
                % (_describe(b),
                   ", ".join(sorted(t.name for t in policy.table_targets))
                   or "none -- this event may emit no TABLE at all"),
                block=b)
        raise TargetNotAllowedError(
            "%s may not be delivered to %s; permitted TABLE target(s): %s"
            % (_describe(b), b.target.name,
               ", ".join(sorted(t.name for t in policy.table_targets)) or "none"),
            block=b)

    # R-TARGET-NOT-ALLOWED
    for b in blocks:
        if b.target not in policy.allowed:
            raise TargetNotAllowedError(
                "%s is delivered to %s, which this event may not use; "
                "permitted target(s): %s"
                % (_describe(b), b.target.name,
                   ", ".join(sorted(t.name for t in policy.allowed))
                   or "none -- this event emits no user-visible blocks"),
                block=b)


class BubbleLedger:
    """Running new-bubble count per cadence scope (SPEC A5 budget).

    Deliberately NOT a frozen dataclass: this is the one accumulator in the
    harness, and its whole job is to carry a count across publications. It is
    driven entirely by DeliveryPolicy data -- `opens` says what a publication
    resets, `scope` says what it charges -- so no event is special-cased here.

    A refused publication never charges the budget: the running total is
    checked before it is written.
    """

    def __init__(self, budget):
        self.budget = dict(budget)
        self.counts = {scope: 0 for scope in self.budget}

    def spent(self, scope):
        return self.counts.get(scope, 0)

    def spend(self, policy, bubbles):
        """Reset the scopes this publication opens, then charge its bubbles."""
        for scope in policy.opens:
            self.counts[scope] = 0
        if not bubbles:
            return
        scope = policy.scope
        if scope is None:
            raise BubbleBudgetError(
                "a publication produced %d new bubble(s) but its event is "
                "charged to no cadence scope; such an event emits nothing"
                % bubbles, block=None)
        cap = self.budget.get(scope)
        total = self.counts.get(scope, 0) + bubbles
        if cap is not None and total > cap:
            raise BubbleBudgetError(
                "this publication would make %d new bubble(s) in the current "
                "%s, and SPEC A5 caps it at %d; adjacent hooks must be absorbed "
                "into the pinned-card edit instead"
                % (total, scope.value, cap), block=None)
        self.counts[scope] = total


def publish(blocks, require_table=False, phrases=INSTRUCTIONAL_PHRASES,
            delivery=None, ledger=None):
    """THE PUBLISHER. Validate, refuse, and order.

    Args:
        blocks: iterable of Block. Caller order is irrelevant.
        require_table: True when the event's contract makes a TABLE mandatory.
        phrases: instructional-phrase detection data (see INSTRUCTIONAL_PHRASES).
        delivery: DeliveryPolicy for the publishing event. Omitted here means
            "no event context", so the delivery rules cannot be evaluated --
            they are per-event by construction. events.emit() ALWAYS supplies
            one, and emit() is the only sanctioned way to produce a HookResult;
            a bare publish() is the low-level slot-contract API.
        ledger: BubbleLedger accumulating the A5 cadence budget across
            publications. Omitted means the budget is not accounted -- a single
            publication is 0 or 1 bubbles and so can never exceed it alone.

    Returns:
        list[Block] sorted by slot number (stable within a slot).

    Raises:
        PublishError subclass, naming the rule and the offending block.
    """
    blocks = list(blocks)

    for b in blocks:
        if not isinstance(b, Block):
            raise InvalidBlockError(
                "not a Block instance: %s" % _describe(b), block=b)
        if not isinstance(b.slot, Slot):
            raise InvalidBlockError(
                "block carries slot %r which is not a Slot member" % (b.slot,),
                block=b)
        if not isinstance(b.target, Target):
            raise InvalidBlockError(
                "block carries target %r which is not a Target member; the "
                "delivery surface is required and is never inferred"
                % (b.target,), block=b)

    # Delivery rules run BEFORE the slot-content rules: a block aimed at the
    # wrong surface is malformed regardless of what it carries. In particular a
    # republished table is refused as a republication, not as an empty table.
    if delivery is not None:
        enforce_delivery(blocks, delivery)

    # R-KEYBOARD-SLOT / R-KEYBOARD-EMPTY -- keyboards live in exactly one slot,
    # and that slot must actually carry one.
    for b in blocks:
        if b.slot is Slot.KEYBOARD and b.keyboard is None:
            raise EmptyKeyboardError(
                "%s declares the KEYBOARD slot but carries no keyboard spec; a "
                "keyboardless KEYBOARD block is prose in disguise"
                % _describe(b), block=b)
        if b.slot is not Slot.KEYBOARD and b.keyboard is not None:
            raise MisplacedKeyboardError(
                "%s carries a keyboard spec; keyboards may only ride in the "
                "KEYBOARD slot" % _describe(b), block=b)

    # R-TABLE-REQUIRED -- prose can never substitute for a table (defect #8).
    if require_table:
        tables = [b for b in blocks if b.slot is Slot.TABLE]
        if not tables:
            raise MissingTableError(
                "this event requires a TABLE block and none was supplied; "
                "publication fails rather than emitting prose in its place",
                block=None)
        if not any(b.payload and b.payload.strip() for b in tables):
            empty = tables[0]
            raise MissingTableError(
                "this event requires a non-empty TABLE block but every TABLE "
                "block is empty (%s); publication fails rather than emitting "
                "prose in its place" % _describe(empty), block=empty)

    # R-KEYBOARD-PROSE -- if a button exists, the button is the instruction
    # (defect #9). Operating instructions in PROSE are refused.
    if any(b.slot is Slot.KEYBOARD for b in blocks):
        for b in blocks:
            if b.slot is not Slot.PROSE:
                continue
            hits = find_instructional_phrases(b.payload, phrases)
            if hits:
                raise InstructionalProseError(
                    "a KEYBOARD block is present, so %s may not carry operating "
                    "instructions; matched phrase(s): %s -- the button is the "
                    "instruction" % (_describe(b), ", ".join(repr(h) for h in hits)),
                    block=b)

    # R-BUBBLE-BUDGET -- charged LAST, and only once everything else has passed:
    # a refused publication never went out, so it must not spend the budget.
    if ledger is not None and delivery is not None:
        ledger.spend(delivery, bubble_count(blocks))

    # R-ORDER -- the publisher orders. Stable, so intra-slot caller order holds.
    return sorted(blocks, key=lambda b: int(b.slot))
