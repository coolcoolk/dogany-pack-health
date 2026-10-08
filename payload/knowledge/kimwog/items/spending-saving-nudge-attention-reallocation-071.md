---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (spending-tracking sprint, dispatch
# kw-spending-tracking). Every source below was resolved and read during
# authoring; no citation is reconstructed from memory. Medina 2021 and Stango
# and Zinman 2014 were read at the abstract (journal record via OpenAlex) and,
# for Medina, at the AEA RCT registry entry; neither was read at full text.
#
# nudge_rules is structured data for a ledger module's nudge code. It says
# what a nudge must CHECK, not how often to send one.
id: spending-saving/nudge-attention-reallocation-071
domain: spending-saving
grade: B (randomised field experiment n = 26,069 on a personal-finance platform, plus a large-panel quasi-experiment); C (the attention-stock duration, one survey panel)
lane: "@household-behavioral"
locale: universal
as_of: 2014-2021
contested: no
sources:
  - "Medina, P. C. (2021). Side Effects of Nudging: Evidence from a Randomized Intervention in the Credit Card Market. The Review of Financial Studies 34(5), 2580-2607. https://doi.org/10.1093/rfs/hhaa108 (abstract read verbatim at the journal record)"
  - "AEA RCT Registry AEARCTR-0003034, Selective Attention in Consumer Finance: Evidence from a Randomized Intervention in the Credit Card Market. https://www.socialscienceregistry.org/trials/3034 (read: 26,069 users of a Brazilian personal-finance platform randomised to planning-plus-due-date messages, due-date messages only, placebo messages, or none; intervention 2015-09-25 to 2015-12-13; registered 2018-06-05, i.e. after the intervention)"
  - "Stango, V. and Zinman, J. (2014). Limited and Varying Consumer Attention: Evidence from Shocks to the Salience of Bank Overdraft Fees. The Review of Financial Studies 27(4), 990-1030. https://doi.org/10.1093/rfs/hhu008 (abstract read verbatim at the journal record)"
  - "source:spending-saving/reminder-names-the-goal-070 -- the reminder result whose own authors flag crowd-out and offsetting borrowing as possible perverse effects"
  - "source:spending-saving/budget-app-rct-knowledge-not-saving-014 -- the other located case of a money tool moving one account in the wrong direction (credit use rose)"
nudge_rules:
  - rule: watch-the-neighbour-account
    direction: after nudging one obligation (a card bill, a saving transfer), the next review checks the accounts the money could come from -- checking balance, overdraft, revolving credit -- not only the target
    basis: card-payment reminders cut late fees 14 percent and raised checking overdraft fees 9 percent
    basis_grade: B
  - rule: history-splits-the-effect
    direction: a user whose own ledger shows recent overdraft or minus-account use is the group where a payment nudge can net out negative; do not send the same nudge to everyone and report the average
    basis: side effect concentrated in users with overdraft history (net +5 percent total fees) while the rest saved 15 percent
    basis_grade: B
  - rule: salience-is-a-stock
    direction: repeated, topic-specific attention to a fee builds and persists; a one-off mention is not the whole effect, and a topic dropped from the review is expected to fade only slowly
    basis: multiple overdraft-themed surveys reduced overdrafts for up to two years
    basis_grade: C
  - rule: say-the-mechanism-actions
    direction: the behaviours that actually avoided fees were fewer low-balance debit transactions and cancelling automatic recurring withdrawals; a nudge can name those two concrete actions
    basis: Stango and Zinman abstract
    basis_grade: C
refraction_notes:
  - note: >
      READ AT ABSTRACT AND REGISTRY LEVEL. The percentages above are the
      abstract's; the registry describes the design. Neither paper was read at
      full text in this pass, so subgroup definitions, standard errors and the
      exact construction of "history of overdraft use" are not carried. The
      registry entry was filed after the intervention ran, so it documents the
      design but is not a pre-registration in the strict sense.
    grade: B
  - note: >
      BRAZIL AND THE US, NOT KOREA. The side effect needs a cheap way to move
      the shortfall -- a checking overdraft. The Korean analogue is the
      마이너스통장 (overdraft line) or a card's 리볼빙 / 현금서비스, which
      exist but are not the same product and are not measured here. The
      direction (money for the nudged bill comes from somewhere) is general
      arithmetic; the size is not transferable.
    grade: C
  - note: >
      THE ATTENTION-STOCK FINDING IS FROM SURVEY CONTENT AS THE SHOCK, among
      people who selected into a survey panel. It shows attention to a fee can
      be built and persist; it does not tell a module how many prompts build it
      or how long a weekly prompt's effect lasts. No cadence number follows.
    grade: C
claim: >
  A nudge moves attention, and attention moved to one account can be taken
  from another. Medina ran a field experiment with 26,069 users of a
  Brazilian personal-finance management platform: reminders about upcoming
  credit card payments reduced credit card late-payment fees by 14 percent but
  increased overdraft fees in checking accounts by 9 percent. The unintended
  effect was concentrated in users with a history of overdraft use, who
  experienced a net increase of 5 percent in total fees, while the rest saved
  15 percent. Stango and Zinman, using survey questions about overdrafts as
  shocks to the salience of overdraft fees, found that people asked about
  overdrafts were less likely to incur a fee that month, that taking several
  such surveys built a stock of attention that reduced overdrafts for up to
  two years, that the effects were significant among consumers with lower
  education and financial literacy, and that people avoided fees by making
  fewer low-balance debit transactions and cancelling automatic recurring
  withdrawals.
reasoning: >
  Graded at the strong empirical band for the side-effect result: a large
  randomised field experiment on a real financial-management platform with
  administrative fee outcomes, published in a flagship finance journal, and
  directly about the object a ledger module is -- a money app that sends
  reminders. It is held below the top band by the lane's ceiling rule (no
  behavioural finding goes there) and by having been read at abstract and
  registry level only. The attention-stock half is a quasi-experiment on a
  survey panel and stays at the observational band. The two papers together
  make one structural point that changes how a weekly review should be built:
  the unit of evaluation for a nudge is the household's whole set of
  accounts, not the account the nudge names. A module that reminds about a
  card bill and then reports "no late fee this month" has measured the
  target and missed the side effect, and the side effect lands on exactly the
  users -- those already using overdraft -- for whom it is most costly. The
  same logic covers item 070, whose authors flag that a reminder's gain in one
  bank could be crowd-out from another. What this item does NOT license: any
  rule about how often to nudge, and any Korean magnitude.
---

# spending-saving/nudge-attention-reallocation-071 -- 한 곳을 챙기라고 하면 다른 곳이 빈다

**한 줄 그림:** 카드값 알림은 카드 연체료를 줄였지만 통장 마이너스 수수료를 늘렸다. 알림의 효과는
알림 받은 계좌 하나가 아니라 가구 전체 계좌로 봐야 한다.

A Brazilian personal-finance app randomly sent some of its 26,069 users
reminders before their credit card due dates. Late fees on the card fell by 14
percent. Overdraft fees in their checking accounts rose by 9 percent. The money
to pay the card on time had to come from somewhere, and for some users it came
from the overdraft.

Who those users were matters. The extra overdraft cost landed on people who
already had a history of overdraft use; for them, total fees went UP about 5
percent. Everyone else saved about 15 percent. An average across both groups
hides that the nudge helped most people and hurt a specific, identifiable few.

A second study, in the US, used surveys that happened to ask about overdraft
fees as a shock to attention. People asked about overdrafts were less likely to
incur one that month, and several such surveys built up attention that kept
overdrafts down for up to two years. The behaviours that did the work were
concrete: fewer debit purchases on a low balance, and cancelling automatic
recurring withdrawals.

For a ledger, the lesson is about what to look at after a nudge, not how often
to send one. Check the neighbouring accounts. Treat a user who already uses
overdraft or a minus account as a different case. And the two actions that
actually avoided fees are things a review can name.

## Engine-readable rules

| Rule | Check / action | Basis |
|---|---|---|
| watch-the-neighbour-account | after a bill or saving nudge, review checking, overdraft and revolving credit too | card late fees -14 pct, overdraft fees +9 pct |
| history-splits-the-effect | users with recent overdraft / minus-account use get the side-effect check first | net +5 pct fees for that group, -15 pct for the rest |
| salience-is-a-stock | repeated topic-specific attention persists; a single mention is not the full effect | reduced overdrafts up to two years |
| say-the-mechanism-actions | name: avoid card/debit spending on a low balance; cancel unneeded automatic withdrawals | the actions that avoided fees |

## 한국어 요약 (답변용)

- 카드 결제일 알림을 받은 사람들은 카드 연체료가 14% 줄었지만, 그 돈을 맞추느라 통장 마이너스
  수수료가 9% 늘었다(브라질 가계부 앱 실험, 26,069명).
- 손해는 원래 마이너스를 자주 쓰던 사람에게 몰렸다. 이들은 전체 수수료가 오히려 5% 늘었고, 나머지는
  15% 아꼈다. 평균만 보면 이 차이가 안 보인다.
- 그래서 주간 리뷰에서 특정 청구서나 저축 이체를 챙기라고 했다면, 다음 리뷰 때 그 계좌만 보지 말고
  돈이 빠져나왔을 만한 곳(입출금 통장 잔액, 마이너스통장, 리볼빙·현금서비스)도 같이 본다.
- 마이너스통장이나 리볼빙을 최근에 쓴 기록이 있는 사용자에게는 같은 알림을 보내더라도 부작용 확인을
  먼저 한다.
- 수수료 이야기를 반복해서 꺼내면 주의가 쌓이고 오래간다(미국 연구에서 최대 2년). 실제로 수수료를
  피한 행동은 잔액이 적을 때 체크카드 결제를 줄인 것과 필요 없는 자동이체를 해지한 것이었다.
- 한국의 마이너스통장·리볼빙은 브라질·미국의 당좌 초과인출과 같은 상품이 아니다. "알림 받은 곳을
  채우면 다른 곳이 빈다"는 방향만 가져오고, 몇 %인지는 가져오지 않는다.
- 알림을 얼마나 자주 보내야 하는지는 이 연구들이 말해 주지 않는다.
