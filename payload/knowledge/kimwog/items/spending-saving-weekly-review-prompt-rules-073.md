---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (spending-tracking sprint, dispatch
# kw-spending-tracking). Synthesis row, same posture as
# exercise/caution-severity-ladder-056: a routing rule over graded rows, not a
# primary finding. Each step names the row it rests on and that row's grade;
# every product constant (weekly cadence, the 30-day recurring look-back, the
# one-prompt-per-topic cap) is labelled as a constant.
#
# review_steps, nudge_rules and refused_methods are structured data for a
# ledger module's weekly review. Values are ORDERINGS and DIRECTIONS; no field
# carries a target amount, a ratio, or a measured optimum frequency.
id: spending-saving/weekly-review-prompt-rules-073
domain: spending-saving
grade: D (synthesis rule; step order and directions rest on B and C rows, every constant is product judgement)
lane: "@household-behavioral"
locale: universal
as_of: 2026
contested: no
sources:
  - "spending-saving/tracking-monitoring-transfer-limit-001"  # monitoring works when physically recorded and reported (B, domain-general)
  - "spending-saving/diary-attrition-zero-reporting-003"  # a missing log renders as a zero (B)
  - "spending-saving/category-classification-malleable-004"  # categories move to fit spending; fix the account before the expense (C)
  - "spending-saving/spending-self-prediction-bias-005"  # forecasts of own spending run low (B)
  - "spending-saving/automation-defaults-dominate-intention-006"  # automatic saving dominates intended saving (B)
  - "spending-saving/automation-removes-salience-008"  # auto-paid costs drift up (C)
  - "spending-saving/subscription-cancellation-friction-009"  # forced re-decision cancels subscriptions (B)
  - "spending-saving/flat-rate-usage-overestimation-010"  # people buy plans for a self that does not show up (B)
  - "spending-saving/earmarking-partitioning-field-experiment-011"  # partition beats label; higher target without partition backfired (C)
  - "spending-saving/budget-app-rct-knowledge-not-saving-014"  # a recording app moved knowledge, not saving (B)
  - "spending-saving/review-cadence-no-measured-optimum-026"  # no cadence evidence; newest days are of unknown completeness (D)
  - "spending-saving/reminder-names-the-goal-070"  # reminders work when they name the goal (C)
  - "spending-saving/nudge-attention-reallocation-071"  # a nudge can move the shortfall to the neighbour account (B)
  - "spending-saving/fresh-start-framing-small-absolute-072"  # landmark-start offers, small effect (C)
  - "Heath, C. and Soll, J. B. (1996). Mental Budgeting and Consumer Decisions. Journal of Consumer Research 23(1), 40-52. https://doi.org/10.1086/209465 (abstract read verbatim at the journal record via OpenAlex: budgets that earmark too little lead to UNDERconsumption in the category, and typical purchases block other typical items)"
  - "Iyer, G. R., Blut, M., Xiao, S. H. and Grewal, D. (2020). Impulse buying: a meta-analytic review. Journal of the Academy of Marketing Science 48, 384-404. https://doi.org/10.1007/s11747-019-00670-w (abstract read verbatim via OpenAlex: 231 samples, more than 75,000 consumers; traits, motives, resources and marketing stimuli as triggers; self-control and mood as mediators; strongly context-dependent)"
  - "framework:GRADE -- the order of the steps (coverage before totals, recurring re-decision before category talk, nudge check before new nudge) follows from B rows (003, 009, 071) and C rows (004, 070); the weekly cadence, the 30-day look-back and the prompt caps are product constants with no direct evidence (026)."
review_steps:
  - step: 1
    name: coverage-check
    action: before any total, check which days and channels have rows; mark the newest days and any silent channel as incomplete, never as zero spending
    basis: spending-saving/diary-attrition-zero-reporting-003
    basis_grade: B
  - step: 2
    name: previous-nudge-follow-up
    action: if last week's review nudged a bill or a transfer, check the neighbour accounts (checking balance, minus-account, revolving, cash advance) before reporting success
    basis: spending-saving/nudge-attention-reallocation-071
    basis_grade: B
  - step: 3
    name: recurring-re-decision
    action: list recurring charges seen in the last 30 days (product constant) and ask keep-or-cancel for at most a few, oldest-unreviewed first; continuation becomes an explicit choice
    basis: spending-saving/subscription-cancellation-friction-009
    basis_grade: B
  - step: 4
    name: usage-vs-plan
    action: for a flat-rate plan, compare recorded use with the price per use only when use is actually recorded; never infer non-use from absence of rows
    basis: spending-saving/flat-rate-usage-overestimation-010
    basis_grade: B
  - step: 5
    name: category-stability
    action: before speaking a category total, check the category scheme did not move to fit the spending (reclassified rows, ambiguous rows); classify by a fixed rule at logging time
    basis: spending-saving/category-classification-malleable-004
    basis_grade: C
  - step: 6
    name: goal-prompt
    action: one saving prompt that names the user's own stated goal and the next scheduled transfer; if no goal is stated, ask for one instead of sending a generic save message
    basis: spending-saving/reminder-names-the-goal-070
    basis_grade: C
  - step: 7
    name: change-offer
    action: if a change is proposed, offer a scheduled automatic change, with a labelled landmark start (next month's first day, the user's birthday) alongside now
    basis: spending-saving/fresh-start-framing-small-absolute-072
    basis_grade: C
nudge_rules:
  - rule: one-topic-one-prompt
    direction: at most one prompt per topic per review (product constant); attention is the scarce input and a moved nudge has side effects
    basis: spending-saving/nudge-attention-reallocation-071
    basis_grade: D
  - rule: user-history-first
    direction: users whose ledger shows recent minus-account, revolving or cash-advance use get the side-effect check before any payment nudge
    basis: spending-saving/nudge-attention-reallocation-071
    basis_grade: B
  - rule: no-generic-save-message
    direction: a prompt that does not name a specific goal or action is not sent
    basis: spending-saving/reminder-names-the-goal-070
    basis_grade: C
  - rule: no-forecast-trust
    direction: when the user predicts next week's spending, record the forecast but expect it to run low; never use it as the budget
    basis: spending-saving/spending-self-prediction-bias-005
    basis_grade: B
  - rule: partition-not-label
    direction: if the user wants money set aside, suggest a separate account or scheduled transfer; a label on the same balance is not the tested object
    basis: spending-saving/earmarking-partitioning-field-experiment-011
    basis_grade: C
  - rule: no-target-raise-alone
    direction: do not raise a saving target without also adding structure (a separate account, an automatic transfer)
    basis: spending-saving/earmarking-partitioning-field-experiment-011
    basis_grade: C
  - rule: under-is-not-success
    direction: a category far under its own budget is not automatically good news; mental budgets can cause underconsumption, so a deep underspend is a question, not a prize
    basis: Heath and Soll 1996
    basis_grade: C
  - rule: impulse-is-not-a-row-field
    direction: never label a ledger row as an impulse purchase from amount, time or merchant; impulse is a state the user reports, and its triggers are context-dependent
    basis: Iyer et al. 2020 (abstract)
    basis_grade: C
  - rule: tracking-is-not-saving
    direction: do not tell the user that keeping the ledger will by itself raise saving; the located money RCT moved knowledge, not saving
    basis: spending-saving/budget-app-rct-knowledge-not-saving-014
    basis_grade: B
refused_methods:
  - method: fixed-ratio budgets (50/30/20, 70/20/10, 80/20)
    status: refused
    reason: no study derives, tests or validates any split (GAPS.md v18)
  - method: envelope budgeting effect sizes
    status: refused as stated; the partition direction survives as item 011
    reason: one field experiment in a cash economy with physical envelopes
  - method: zero-based budgeting (every unit assigned a job)
    status: refused, no item
    reason: no household-level test of the method was located at any tier in this pass (GAPS.md, 2026-10-06)
  - method: tracking saves N percent
    status: refused
    reason: domain-transfer error from 001; 014 found no saving effect
  - method: latte factor
    status: refused
    reason: GAPS.md v18
  - method: wait-N-hours impulse rule
    status: not shipped
    reason: the located study could not be read at source; reported outcomes were urge and intent, and a short lab delay did not reduce purchases (GAPS.md, 2026-10-06)
refraction_notes:
  - note: >
      THE ORDER IS THE EVIDENCE, THE CONSTANTS ARE NOT. Coverage before totals,
      checking last week's nudge before sending a new one, and recurring
      re-decision before category talk follow from graded rows. Weekly
      cadence, the 30-day recurring look-back and one prompt per topic are
      product constants. Speak them as the review's rule, never as a measured
      optimum.
    grade: D
  - note: >
      NO TARGET NUMBER. Nothing in this row gives an amount, a percentage of
      income or a category split. If the user asks what share of income to save
      or spend on a category, say plainly that no budget ratio has been
      measured against outcomes, then work from the user's own stated goal.
    grade: C
  - note: >
      NOT A SAVING GUARANTEE. The steps are built to keep the review honest
      (coverage, side effects, category drift) and to word prompts the way the
      located field experiments found worked. None of them, alone or together,
      has been tested as a weekly review, and the nearest test of a recording
      tool did not raise saving.
    grade: B
claim: >
  A weekly spending review runs in a fixed order: (1) check coverage first and
  mark missing days or channels as incomplete, never as zero; (2) if last week
  nudged a bill or transfer, check the neighbour accounts for a moved
  shortfall before calling it a success; (3) put a few recurring charges back
  in front of the user as an explicit keep-or-cancel choice; (4) compare a
  flat-rate plan with recorded use only where use is actually recorded;
  (5) check the category scheme held still before speaking category totals;
  (6) send at most one saving prompt, naming the user's own goal and next
  transfer; (7) offer any change as a scheduled automatic change with a
  labelled landmark start alongside now. Nudges never use a generic save
  message, never trust the user's own spending forecast as a budget, prefer a
  separate account over a label, never raise a target without structure,
  treat a deep underspend as a question, never tag a row as impulse, and never
  promise that tracking itself saves money. Fixed-ratio, zero-based and
  envelope effect-size claims are refused.
reasoning: >
  Each step is the operational form of one graded row, and the ordering
  follows from which errors would invalidate the later steps. Coverage comes
  first because a missing log renders as a zero and a zero renders as thrift
  (003, checklist trigger 10): every later statement is about totals. The
  nudge follow-up comes second because 071 shows the nudge's own success
  metric can hide a cost on the neighbour account, concentrated on users
  already using overdraft. Recurring re-decision comes before category talk
  because it is the one intervention in this lane with a strong, directly
  observed effect that needs no persuasion (009) and because auto-paid costs
  drift up out of sight (008). Category totals come after a stability check
  because categories bend to fit spending (004). The prompt and change-offer
  steps carry the two C-band findings about prompt content (070) and timing
  (072), and the change is always automatic because automatic saving
  dominates intended saving (006). Two additions come from sources read at
  abstract only: mental budgets can cause underconsumption as well as
  overspending (Heath and Soll), and impulse buying is a context-dependent
  state rather than a property visible in a row (Iyer et al.). The refused
  list is part of the rule, so that a later build cannot reach for a
  50/30/20 split or a zero-based template because the review step looked
  empty without one.
---

# spending-saving/weekly-review-prompt-rules-073 -- 주간 가계부 리뷰 순서와 알림 규칙

**한 줄 그림:** 주간 리뷰는 "기록이 빠진 곳 확인 → 지난주 알림의 부작용 확인 → 정기결제 다시 고르기 →
카테고리 확인 → 목표를 이름으로 부르는 알림 하나 → 바꿀 게 있으면 날짜 정해 자동이체로" 순서로 한다.

## Review order (engine-readable)

| Step | Name | Action | Basis (grade) |
|---:|---|---|---|
| 1 | coverage-check | mark missing days / channels incomplete, never zero | 003 (B) |
| 2 | previous-nudge-follow-up | check neighbour accounts after last week's nudge | 071 (B) |
| 3 | recurring-re-decision | a few recurring charges as explicit keep-or-cancel | 009 (B) |
| 4 | usage-vs-plan | price per use only where use is recorded | 010 (B) |
| 5 | category-stability | check the scheme held still before category totals | 004 (C) |
| 6 | goal-prompt | one prompt naming the user's goal and next transfer | 070 (C) |
| 7 | change-offer | scheduled automatic change, landmark start alongside now | 072 (C) |

Product constants, not evidence: weekly cadence, 30-day recurring look-back,
one prompt per topic.

## Refused

Fixed-ratio budgets (50/30/20 and the rest), zero-based budgeting as an
evidenced method, envelope effect sizes, "tracking saves N percent", the latte
factor, and a wait-N-hours impulse rule. See GAPS.md.

## 한국어 요약 (답변용)

- 합계를 말하기 전에 기록이 빠진 날짜와 결제 수단부터 확인한다. 빠진 곳은 "안 썼다"가 아니라 "기록 없음"으로
  표시한다. 가장 최근 며칠은 아직 다 안 들어왔을 수 있다.
- 지난주에 카드값이나 저축 이체를 챙기라고 했다면, 이번 주에는 그 돈이 어디서 나왔는지 본다. 입출금 통장
  잔액, 마이너스통장, 리볼빙, 현금서비스. 원래 마이너스를 쓰던 사람은 특히 먼저 본다.
- 최근 30일 정기결제 중 몇 개만 골라 "계속할까요, 해지할까요?"를 묻는다. 그냥 두면 계속 나가는 게
  기본값이라서, 다시 고르게 하는 것 자체가 효과가 있다.
- 헬스장·구독처럼 정액제는 실제 이용 기록이 있을 때만 1회당 가격을 계산한다. 기록이 없다고 안 갔다고
  단정하지 않는다.
- 카테고리별 합계를 말하기 전에 분류가 바뀌지 않았는지 본다. 애매한 지출은 쓰기 편한 쪽으로 옮겨 가기
  쉽다. 기록할 때 정해진 규칙으로 분류한다.
- 저축 알림은 리뷰당 하나만, 사용자가 정한 목표("여름 여행", "자동차 보험 갱신")와 다음 이체를 이름으로
  짚어서 보낸다. 목표가 없으면 막연한 "저축하세요" 대신 목표부터 묻는다.
- 바꾸자고 할 때는 "아껴 쓰자"가 아니라 날짜가 정해진 자동이체로 제안하고, "지금부터"와 함께 "다음 달
  1일부터"·"생일부터" 같은 새 출발 날짜도 제시한다.
- 다음 주 지출 예상은 듣되 예산으로 쓰지 않는다. 사람들은 자기 지출을 낮게 예상한다.
- 돈을 따로 떼어 두고 싶어 하면 이름표만 붙이지 말고 별도 계좌나 자동이체를 권한다. 구조 없이 목표 금액만
  올리면 오히려 덜 모였다.
- 예산보다 훨씬 덜 쓴 카테고리는 무조건 칭찬하지 않는다. 꼭 필요한 데 못 쓰고 있는 건 아닌지 묻는다.
- 금액·시간·가게만 보고 "충동구매"라고 붙이지 않는다. 충동구매는 사용자가 말해 주는 상태다.
- 가계부를 쓰는 것만으로 저축이 늘어난다고 말하지 않는다. 지금까지 찾은 실험에서는 지식은 늘었지만 저축은
  그대로였다.
- 50/30/20 같은 비율 예산, 제로 베이스 예산, 봉투 예산의 효과 수치는 근거가 없거나 매우 좁다. 비율을
  물으면 "검증된 비율은 없다"고 말하고 사용자의 목표에서 출발한다.
- 리뷰를 매주 한다, 30일을 본다, 주제당 알림 하나 같은 숫자는 제품 규칙이지 연구로 정해진 값이 아니다.
