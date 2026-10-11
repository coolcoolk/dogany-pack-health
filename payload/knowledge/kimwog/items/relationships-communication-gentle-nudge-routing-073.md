---
# Relationship-contact sprint 2026-10-06 (dispatch task kw-relationship-contact).
# The engine-readable synthesis for the lifekit person module: which signals
# may produce a gentle reach-out suggestion, what the suggestion carries, and
# what is forbidden. It is a ROUTING rule, not a finding: every row names the
# graded item it rests on. It does not replace the craft rules already in force
# (018 three-state log, 019 trigger and render, 020 declared tiers, 021 caps,
# fade and snooze) -- it sits on top of them and adds the 070-072 evidence.
# Same posture as exercise/caution-severity-ladder-056.
#
# nudge_rules and forbidden are structured data. No field carries an interval,
# a day count or a target; the only numbers in force are 021's caps and the
# owner's own declared bands (020), both read from their own rows.
id: relationships-communication/gentle-nudge-routing-073
domain: relationships-communication
grade: D (synthesis routing rule over 013, 014, 018-021 and 070-072; each row's own basis grade is carried in the data)
lane: "@relational-craft"
locale: universal
as_of: 2026-10-06
contested: no
sources:
  - "relationships-communication/friendship-decay-kin-buffer-070"  # friends drift without contact, kin hold, transitions, dormant ties, own-pattern comparison
  - "relationships-communication/remembered-detail-follow-up-071"  # detail as a follow-up question; good news; birthdays as an occasion
  - "relationships-communication/communal-no-scorekeeping-072"  # no balance, no your-turn
  - "relationships-communication/reach-out-appreciation-gap-013"  # the reach-out is under-valued, most for distant ties; speak only into hesitation (019)
  - "relationships-communication/contact-cadence-no-evidence-014"  # no interval exists to be behind on
  - "relationships-communication/record-absence-not-neglect-018"  # unknown is not a lapse
  - "relationships-communication/reconnect-after-gap-craft-019"  # trigger = owner's declared tier overrun; render as name / last occasion / days since
  - "relationships-communication/declared-tiers-not-quota-020"  # bands are the owner's, a criterion not a target
  - "relationships-communication/roster-without-chore-list-021"  # caps in code; fade and snooze; owner directive P6 (no nagging, no guilt, no streaks)
  - "framework:GRADE -- bottom band by construction: a routing synthesis. The evidence behind individual rows runs from randomised (071 question-asking) through observational (070, 072) to design-only; that per-row strength is carried in basis_grade and must be spoken with the row, never lifted to the synthesis."
nudge_rules:
  - signal: declared-band-overrun
    when: the owner's own declared tier band for this person is overrun on RECORDED contact (020); unknown stretches excluded (018)
    offer: name, last shared occasion, days since (019), inside the 021 weekly batch
    tie_weight: friend full; kin softened (070) -- shown only if the owner set a band for that relative
    basis: relationships-communication/reconnect-after-gap-craft-019
    basis_grade: D
  - signal: friend-pattern-drop
    when: recorded contact with a friend has fallen against the owner's own past pattern with that person
    offer: may raise that person's rank inside the existing 021 batch; never adds a batch, never shown as "drifting"
    tie_weight: friend only
    basis: relationships-communication/friendship-decay-kin-buffer-070
    basis_grade: C
  - signal: life-transition
    when: the owner or the person is moving, starting a job or school, or the owner's network is filling with new people (owner-stated or recorded)
    offer: one line that old friends are worth a light touch around now; no list
    tie_weight: friend
    basis: relationships-communication/friendship-decay-kin-buffer-070
    basis_grade: D
  - signal: stored-detail-due
    when: a detail the person shared has a date or a natural follow-up point (exam day, move date, surgery, launch)
    offer: the detail plus a follow-up question stem; good news ranks above routine
    tie_weight: any
    basis: relationships-communication/remembered-detail-follow-up-071
    basis_grade: B
  - signal: birthday-or-date
    when: the day itself
    offer: one mention on the day; no advance chain; a skip is not recorded and never resurfaces
    tie_weight: any
    basis: relationships-communication/remembered-detail-follow-up-071
    basis_grade: D
  - signal: dormant-close-tie
    when: the owner marks someone as once close and long out of touch, or mentions them
    offer: the last shared context as an opener, explicitly without an apology for the gap (019)
    tie_weight: any
    basis: relationships-communication/friendship-decay-kin-buffer-070
    basis_grade: C
  - signal: owner-hesitates
    when: the owner says it has been too long, it would be strange, they would not want to hear from me
    offer: one line -- the welcome is usually underestimated, most of all for people you are less close to
    tie_weight: any
    basis: relationships-communication/reach-out-appreciation-gap-013
    basis_grade: B
forbidden:
  - item: any interval, day count, target or "should contact every N" -- the owner's own band is the only number, and it is spoken as theirs (014, 020)
  - item: who-contacted-whom balance, ratio, "your turn", "they reached out last" (072, 012)
  - item: streaks, missed counts, overdue lists, backlog, red or urgent styling (021, owner directive P6)
  - item: verdicts on a relationship -- drifting, one-sided, at risk, losing (012, 070)
  - item: treating an empty log as no contact (018)
  - item: a finished message drafted unasked; offer the detail and a question stem only (019, 071)
  - item: re-asking after a dismissal; nudging someone with an upcoming appointment (021)
refraction_notes:
  - note: >
      WHAT FIRES, WHAT RIDES ALONG. The only things that fire a reach-out
      suggestion on their own are the owner's own declared band (020), a
      dated detail the person shared (071), and the day of a birthday or
      date. Evidence-derived signals -- a friend's falling pattern, a life
      transition, a dormant close tie (070) -- change ORDER inside the
      existing capped batch or add one line; they never create a new
      reminder stream. This keeps 019's rule that evidence must not become
      the reason a schedule exists.
    grade: D
  - note: >
      WHAT A SUGGESTION CARRIES. A name, the last shared occasion, days
      since, and -- when there is one -- the stored detail as a question
      stem. Good news outranks routine news. Nothing about how long it
      "should" have been, and nothing about who owes whom.
    grade: D
  - note: >
      FAMILY IS QUIETER. Kin closeness held through the transition in the one
      prospective study, so a gap with a relative is a weak cue and is shown
      only when the owner set a band for that person. This is a reason to
      say less, never a claim that family needs no contact.
    grade: C
  - note: >
      SPEAK EACH ROW AT ITS OWN STRENGTH. The follow-up-question rule rests on
      randomised conversations (between strangers); the decay and
      scorekeeping rows rest on small observational or old lab studies; the
      routing itself is design. Never present the synthesis as "research
      says".
    grade: D
claim: >
  Routing rule for the lifekit person module's gentle nudges, built on the
  domain's graded rows and on the owner's standing no-nagging, no-guilt,
  no-streak directive. FIRING signals are only three: the owner's own declared
  tier band overrun on recorded contact (019, 020), a dated detail the person
  shared (071), and the day of a birthday or date (071, one mention, no chain,
  skip never recorded). EVIDENCE signals only reorder or annotate inside the
  existing caps (021): a friend's recorded contact falling against the owner's
  own past pattern with that person (070), a life transition (070), a dormant
  once-close tie (070), and -- only when the owner voices hesitation -- the line
  that the welcome is usually underestimated, most for less-close people (013).
  The suggestion carries name, last shared occasion, days since, and the stored
  detail as a follow-up question stem (071); good news outranks routine. Kin
  gaps are a weak cue (070). FORBIDDEN: any interval or target (014), any
  give/receive balance or "your turn" (072, 012), streaks, missed counts,
  overdue lists (021), verdicts on a relationship, treating an empty log as no
  contact (018), and unasked finished messages. Every row carries its own basis
  grade; the synthesis itself has no evidential strength of its own.
reasoning: >
  The module already enforces caps, fade, snooze and the three-state log
  (018-021), but the evidence lane had nothing on decay, message content or
  reciprocity, so the module had no graded basis for which signals deserve a
  nudge at all. 070-072 supply that, each with an honest ceiling. This row
  turns them into one table the code can read, and fixes the division of
  labour that keeps 014 and 019 intact: owner-declared and person-shared
  signals may fire; evidence-derived signals may only reorder within limits
  already in force. That split is the mechanical form of "no guilt, no
  streaks" -- if no evidence signal can create a reminder, no amount of
  evidence can grow the surface into a debt ledger. The forbidden list is in
  data so that a renderer can be tested against it. Bottom band by
  construction; not contested.
---

# relationships-communication/gentle-nudge-routing-073 -- 사람 모듈의 부드러운 연락 제안 규칙

**한 줄 그림:** 알림을 '켜는' 건 사용자가 정한 기준, 상대가 말해 준 일, 생일 당일뿐이다. 연구에서 나온 신호는
이미 있는 한도 안에서 순서만 바꾼다.

## What the engine reads from this row

| signal | fires on its own? | offer | basis strength |
|---|---|---|---|
| owner's declared band overrun (recorded contact) | yes | name / last occasion / days since, in the weekly batch | design |
| dated detail the person shared | yes | detail + follow-up question stem; good news first | randomised (strangers) |
| birthday or date | yes, on the day only | one mention; skip never recorded | no closeness evidence |
| friend's contact falling vs own past pattern | no, reorders only | higher in the batch, never labelled "drifting" | observational |
| life transition | no, one line | old friends are worth a light touch now | inference |
| dormant once-close tie | no, when owner raises it | last shared context, no apology | observational |
| owner voices hesitation | no, one line | welcome is usually underestimated | randomised |

Forbidden in any output: intervals or targets, give/receive balance or "your
turn", streaks or missed counts or overdue lists, relationship verdicts, empty
log read as no contact, unasked finished messages.

## 한국어 요약 (답변용)

- 연락 제안을 새로 띄울 수 있는 건 세 가지뿐이다. 사용자가 직접 정한 그 사람의 연락 기준을 기록상
  넘었을 때, 상대가 말해 준 일(시험, 이사, 수술 등)의 날짜가 됐을 때, 생일·기념일 당일.
- 연구에서 나온 신호는 이미 있는 주간 묶음 안에서 순서만 바꾸거나 한 줄을 덧붙인다. 친구와의 연락이
  그 사람과의 예전 패턴보다 줄었을 때, 이사·이직처럼 생활이 바뀔 때, 오래 끊긴 옛 가까운 사이를
  사용자가 떠올렸을 때가 여기 해당한다. 새 알림을 만들지는 않는다.
- 제안에는 이름, 마지막으로 함께한 일, 며칠 지났는지, 그리고 기억해 둔 일이 있으면 그에 대한 질문
  하나를 담는다. 좋은 소식이 일상적인 소식보다 앞선다.
- 가족과의 공백은 약한 신호로 본다. 사용자가 그 가족에게 기준을 정해 둔 경우에만 보여 준다.
- 사용자가 "너무 오래돼서 좀 그렇다"며 망설일 때만 "연락받는 쪽은 생각보다 반가워한다, 덜 가까운
  사이일수록 더 그렇다"는 말을 한 줄 한다.
- 하지 않는 것: 며칠마다 연락하라는 간격, 누가 더 연락했는지·누구 차례인지, 연속 기록·놓친 횟수·
  밀린 목록, "멀어지고 있다·일방적이다" 같은 판정, 기록이 없는 걸 연락 안 한 걸로 보기, 묻지 않았는데
  완성된 메시지 써 주기.
