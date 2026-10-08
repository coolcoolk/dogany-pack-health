---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# Two independent research programmes converge here, which is why this sits a
# band above the single-programme laboratory items.
id: spending-saving/spending-self-prediction-bias-005
domain: spending-saving
grade: B (converging experimental programmes, self-report outcomes)
lane: "@household-behavioral"
locale: universal
as_of: 2009-2016
contested: no
sources:
  - "Peetz, J. and Buehler, R. (2009). Is There a Budget Fallacy? The Role of Savings Goals in the Prediction of Personal Spending. Personality and Social Psychology Bulletin 35(12), 1579-1591. https://doi.org/10.1177/0146167209345160 (PMID 19713568, record read at PubMed)"
  - "Berman, J. Z., Tran, A. T. K., Lynch, J. G. Jr. and Zauberman, G. (2016). Expense Neglect in Forecasting Personal Finances. Journal of Marketing Research 53(4), 535-550. https://doi.org/10.1509/jmr.15.0101 (author-reported file-drawer meta-analysis read at https://doi.org/10.2139/ssrn.2542805)"
refraction_notes:
  - note: >
      Both programmes measure PREDICTIONS against self-reported or recalled
      spending, not against an external record. The direction is robust across
      two independent labs, four studies in one and a 25-study internal
      meta-analysis in the other; the exact magnitude of the shortfall is not
      something to quote, because the comparison standard is itself a
      self-report subject to item 002.
    grade: B
claim: >
  People systematically expect to spend less than they will, and the error has
  two distinct and separately measured sources. (1) SAVINGS-GOAL CONTAMINATION.
  Peetz and Buehler (2009) ran four studies on prediction of personal spending
  and found participants underestimated their future spending, predicting they
  would spend substantially less in the coming week than they actually spent, or
  than they remembered spending in the previous week. The bias stemmed from
  savings goals -- the general desire to save money or minimise future spending
  -- held at the time of prediction: participants who reported (Studies 2 and 3)
  or were experimentally INDUCED to experience (Study 4) a stronger savings goal
  predicted they would spend less. Critically, those savings goals were NOT
  related to actual spending. The goal moved the forecast and left the behaviour
  alone. (2) EXPENSE NEGLECT. Berman, Tran, Lynch and Zauberman (2016) show that
  when consumers forecast their future spare money, they under-weigh how much
  their own expected expense growth will consume it, even though they expect
  both income and expenses to rise. Their meta-analysis of their entire file
  drawer (25 studies, 7,214 participants) finds participants place about 2.7
  times as much weight on income change as on expense change when forecasting
  financial slack, with the neglect stronger for the distant than the near
  future. They rule out measurement error, low confidence in estimating expenses,
  belief in greater flexibility of future expenses, and general optimism bias as
  explanations.
reasoning: >
  Graded at the strong band, above the single-laboratory items in this lane,
  because two independent research programmes with different designs and
  different outcome measures converge on the same direction, and because the
  second one explicitly published its file drawer and ruled out the obvious
  alternative explanations rather than leaving them open. The reason it is not
  at the top band is that both benchmark forecasts against self-reported
  spending, so item 002 applies to the comparison standard as well as to the
  forecast. The consequence for a ledger agent is a hard design rule, and it is
  a rule against a very natural product behaviour: do NOT build a plan from what
  the user says they will spend, and be especially wary of a plan the user makes
  while feeling motivated to save, because the motivation demonstrably moves the
  prediction without moving the outcome. A user with 1,600 logged entries has
  supplied a better forecast of their own next month than any budget they would
  state. The second finding adds the sharper version: when someone reasons about
  future headroom, the income side is vivid and the expense side is not, so an
  agent that projects only earnings or only a savings target is amplifying the
  exact bias the literature measures.
---

# spending-saving/spending-self-prediction-bias-005

Ask someone what they will spend next week and they will tell you a number
below what they will actually spend, and below what they themselves remember
spending last week. That is the plain finding from four studies on personal
spending forecasts.

The mechanism is worse than simple optimism, and it is the part with a direct
product consequence. The underestimate is driven by the desire to save. People
who wanted to spend less predicted they would spend less -- including people who
were experimentally made to want it, which rules out the reverse explanation.
And that desire had no relationship at all to what they went on to spend. The
goal moved the forecast and left the behaviour untouched. So the moment a person
is most motivated to budget is precisely the moment their budget is least
accurate.

A separate line of research found the second half. When people estimate how much
spare money they will have later, they know their income will grow and they know
their expenses will grow, and they still weight the income side roughly two and
a half times more heavily. Across the authors' entire file drawer -- 25 studies
and over 7,000 participants, published including the null results -- the neglect
held, got worse the further out the forecast went, and survived every obvious
alternative explanation they tested.

The rule that follows is uncomfortable but clear. A person's own spending
history is a better forecast of their spending than the plan they would write
down, and a plan written in a moment of motivation is the least reliable version
of it. An agent holding a long log should quote the log back, not ask for a
target. Where the log itself is the comparison standard, remember that it is a
self-report too, so treat the direction as established and leave the size of the
gap alone.
