---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (spending-tracking sprint, dispatch
# kw-spending-tracking). Every source below was resolved and read during
# authoring; no citation is reconstructed from memory. The working paper was
# read at full text (abstract, sections III-V, Tables 3-5 and the conclusion);
# the published Management Science version was read at the record only.
#
# nudge_rules is structured data for a ledger module's weekly review / nudge
# code. Values are DIRECTIONS; no rule carries a measured optimum frequency.
id: spending-saving/reminder-names-the-goal-070
domain: spending-saving
grade: C (three randomised field experiments, pooled effect marginal, self-selected new savers in developing economies)
lane: "@household-behavioral"
locale: universal  # three-country pooled (BO, PE, PH); population limit carried in refraction_notes
as_of: 2010 (working paper), 2016 (published)
contested: no
sources:
  - "Karlan, D., McConnell, M., Mullainathan, S. and Zinman, J. (2016). Getting to the Top of Mind: How Reminders Increase Saving. Management Science 62(12), 3393-3411. https://doi.org/10.1287/mnsc.2015.2296 (published record read; full text read at the NBER working paper version, w16205, July 2010, https://www.nber.org/system/files/working_papers/w16205/w16205.pdf)"
  - "source:spending-saving/commitment-savings-rct-007 -- the commitment-account population these reminders were sent to, and the effect size the authors compare against"
  - "source:spending-saving/earmarking-partitioning-field-experiment-011 -- the other located field result where making the specific goal concrete moved saving"
  - "source:spending-saving/nudge-attention-reallocation-071 -- why a reminder's gain on its target account is not a household-level gain"
nudge_rules:
  - rule: name-the-goal
    direction: a saving reminder names the user's own stated goal (the specific future expense), not saving in general
    basis: Peru arm -- goal-naming reminders +16 percent saved vs none; reminders not naming it had no effect; difference significant
    basis_grade: C
  - rule: point-at-the-next-action
    direction: the reminder lands before the next planned deposit and names that deposit; a goal image given once at sign-up is not a substitute
    basis: Peru photo and puzzle gifts had no effect and were significantly weaker than goal-naming reminders sent before the deposit
    basis_grade: C
  - rule: frame-is-free
    direction: gain versus loss wording is not a lever; pick the wording that reads naturally
    basis: no strong evidence of differential effects of loss vs gain framing
    basis_grade: C
  - rule: no-extra-late-nag
    direction: an extra reminder after a missed deposit is not expected to add anything over the regular one
    basis: no strong evidence of differential effects of late vs regular reminders
    basis_grade: C
  - rule: regular-not-optimal
    direction: a regular (monthly in the trials) cadence is what was tested; no frequency comparison exists, so the cadence is a product constant
    basis: absence; see spending-saving/review-cadence-no-measured-optimum-026
    basis_grade: D
refraction_notes:
  - note: >
      THE POOLED EFFECT IS SMALL AND ONLY MARGINALLY SIGNIFICANT. Monthly
      reminders raised balances in the reminding bank by about 6 percent
      (p = 0.079 without covariates, 0.065 with) and goal attainment by about 3
      percentage points. The goal-naming contrast is the stronger finding, but it
      comes from one site (Peru) and moved amount saved, not goal attainment.
      Speak the direction; do not promise a percentage.
    grade: C
  - note: >
      THE TARGET ACCOUNT IS NOT THE HOUSEHOLD. The outcome is the balance in the
      bank that sent the reminder. The authors state they cannot say whether or
      how much reminders increased TOTAL savings, and name crowd-out of other
      savings and offsetting borrowing as possible perverse effects. Item 071 is
      a measured case of exactly that kind of side effect.
    grade: C
  - note: >
      POPULATION. New commitment-savings account holders in Bolivia, Peru and
      the Philippines who had chosen to save of their own volition, mostly low
      balances (about 100 US dollars or less). Checklist trigger (8) applies to a
      middle-income Korean household; the authors themselves say the result does
      not answer whether non-savers respond the same way. The direction is
      plausible to transfer, the size is not.
    grade: C
claim: >
  A reminder to save works better when it names the person's own goal than
  when it does not. Karlan, McConnell, Mullainathan and Zinman randomised
  monthly reminders (text message in Bolivia and the Philippines, letter in
  Peru) to people who had just opened goal-oriented savings accounts at three
  banks. Pooled, reminded clients saved about 6 percent more in the reminding
  bank (p about 0.07) and were about 3 percentage points more likely to reach
  their savings goal. The sharper result is the content contrast: in Peru,
  the one site where clients had labelled the account with a specific future
  expense, reminders that mentioned that expense raised savings by an
  estimated 16 percent relative to no reminder, while reminders that did not
  mention it had no effect, and the difference was significant. A goal photo
  or puzzle piece handed over at account opening or after a deposit did
  nothing. Gain versus loss wording, and an extra reminder after a missed
  deposit, showed no strong differential effect. In Bolivia, where the bank
  rather than the client labelled the goal, only reminders that mentioned the
  financial incentive moved saving.
reasoning: >
  Graded at the observational band although the design is randomised, for
  three reasons stated on the lane checklist: the pooled main effect is only
  marginally significant, the population is self-selected new savers in
  developing economies with small balances (trigger 8), and the outcome is one
  account's balance rather than household saving. It ships because it is the
  only located field evidence on the CONTENT of a saving prompt, which is
  exactly what a ledger module writes every week, and because its useful
  findings are about what does not matter as much as what does. The authors'
  model is limited attention to lumpy future expenses -- people attend to
  everyday consumption but forget the school fee or the car registration
  coming -- so the operative content is the specific expense, held up just
  before the action that serves it. That matches item 011 (a concrete goal
  image helped there too, though in a physical-envelope design) and is
  consistent with item 007. Note what it does not license: no cadence (only
  monthly was tested), no claim about total saving, and no reason to think a
  generic "remember to save" message does anything.
---

# spending-saving/reminder-names-the-goal-070 -- 저축 알림은 '무엇을 위해'를 말해야 한다

**한 줄 그림:** 저축하라는 알림은 막연한 "저축하세요"가 아니라, 사용자가 직접 정한 목표 지출을
입금 직전에 짚어 줄 때만 효과가 보였다.

Three banks, three countries, people who had just opened savings accounts with
a goal attached. Some were randomly sent a monthly reminder; the rest were not.

Pooled, the reminder did a little: about 6 percent more money in that bank and
about 3 percentage points more people reaching their goal, with the pooled
result only marginally significant. The interesting part is in Peru, where
each client had labelled the account with the specific thing they were saving
for. Reminders that mentioned that thing raised savings by an estimated 16
percent. Reminders that did not mention it did nothing. A photo of the goal
given at sign-up did nothing either. The difference is timing and target: the
working reminder arrived just before the next deposit and pointed at both the
goal and the deposit.

Two things that did not matter are as useful as the one that did. Wording a
message as a gain or as a loss made no clear difference, and sending an extra
nag after a missed deposit added nothing over the regular message.

The limits are real. These were new, self-selected savers with small balances
in Bolivia, Peru and the Philippines. The outcome was the balance in the bank
that sent the message, and the authors say plainly they cannot tell whether
the household saved more overall or simply moved money. Item 071 is a measured
example of that kind of side effect.

## Engine-readable rules

| Rule | Direction | Basis |
|---|---|---|
| name-the-goal | name the user's own stated goal, not saving in general | Peru: +16 pct vs none; generic reminder no effect |
| point-at-the-next-action | send before the next planned transfer and name it | goal gifts at sign-up had no effect |
| frame-is-free | gain vs loss wording is not a lever | no differential effect found |
| no-extra-late-nag | no extra reminder after a miss | late vs regular, no differential effect |
| regular-not-optimal | regular cadence is a product constant | only monthly was tested; see 026 |

## 한국어 요약 (답변용)

- 저축 알림은 사용자가 정한 목표를 이름으로 불러야 한다. "여행 자금", "자동차 보험료"처럼 구체적인
  지출을 짚은 알림은 효과가 있었고, 목표를 말하지 않은 알림은 효과가 없었다(페루 은행 실험).
- 알림은 다음 입금·이체 직전에 보내고 그 행동을 함께 말한다. 가입할 때 한 번 준 목표 사진 같은 건
  효과가 없었다.
- "놓치면 손해"식 표현과 "하면 이득"식 표현 사이에 뚜렷한 차이는 없었다. 자연스러운 쪽을 고르면 된다.
- 입금을 놓쳤다고 추가 독촉을 보내도 정기 알림 이상의 효과는 없었다.
- 효과 크기는 작다. 세 나라를 합치면 저축액 약 6% 증가, 목표 달성 약 3%p 증가였고 통계적으로도
  간신히 걸쳤다. 숫자를 약속하지 말고 방향만 말한다.
- 이 실험은 볼리비아·페루·필리핀에서 스스로 저축 계좌를 연 저소득 사용자들이 대상이었고, 알림을 보낸
  은행 계좌 잔액만 쟀다. 가구 전체 저축이 늘었는지는 모른다.
- 알림 주기는 매달만 시험됐다. 주간 리뷰 주기는 제품이 정한 규칙이지 연구로 정해진 값이 아니다.
