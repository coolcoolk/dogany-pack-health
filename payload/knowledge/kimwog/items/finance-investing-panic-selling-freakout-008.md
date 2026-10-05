---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/panic-selling-freakout-008.
id: finance-investing/panic-selling-freakout-008
domain: finance-investing
grade: C
lane: "@quant-market"
locale: US
as_of: 2003-2015 (sample) / 2022 (publication)
contested: no
sources:
  - "Elkind, D., Kaminski, K., Lo, A. W., Siah, K. W. and Wong, C. H. (2022). When Do Investors Freak Out? Machine Learning Predictions of Panic Selling. The Journal of Financial Data Science 4(1), 11-39. Working-paper copy: https://ssrn.com/abstract=3898940"
claim: >
  The damaging part of panic selling is the failure to return, not the sale
  itself. Using 653,455 individual brokerage accounts across 298,556
  households, and defining a panic sale as a decline of 90 percent of a
  household account equity position within one month of which at least half
  is due to trades, the authors report that panic sales are rare in normal
  times (about 0.1 percent of investors at any point) but occur at up to
  three times the baseline frequency around large market movements. Of the
  investors who panic sell, 30.9 percent never returned to risky assets at
  all within the sample; of those who did return, more than 58.5 percent
  re-entered within half a year. The authors conclude that while freaking
  out does protect investors during a crisis, such investors often wait too
  long to reinvest and miss significant gains when markets rebound.
  Counter-intuitive demographic finding, reported as-is: investors who are
  male, over 45, married, with more dependents, or who self-identify as
  having excellent investment experience or knowledge, panic MORE often.
reasoning: >
  Observational band. It is a single proprietary brokerage dataset from one
  country, self-reported demographics, and a mechanical definition of panic
  selling that will both miss slower capitulation and catch some legitimate
  liquidations, so the percentages are descriptive of this dataset rather
  than a population constant. Kept because the shape of the finding -- the
  cost is the exit becoming permanent -- is the single most decision-relevant
  behavioural fact for a personal investing agent, and because the
  self-assessed-expertise result directly undercuts the assumption that a
  confident user is a safe user.
---

# finance-investing/panic-selling-freakout-008

In a dataset of over 650,000 individual brokerage accounts, selling out
almost entirely during a sharp downturn was rare in ordinary times and up to
three times more common right after big market moves. The important number is
what happened next: 30.9 percent of the investors who did it never went back
into risky assets at all during the sample period. Among those who did return,
most were back within six months.

The authors are careful about this: getting out does protect you during the
crisis itself. The damage comes from waiting too long to get back in and
missing the rebound. So the risk being managed is not the sale, it is the
exit becoming permanent.

One finding deserves to be carried in full because it inverts the usual
assumption. The investors who panicked more often were male, over 45,
married, had more dependents, and self-identified as having excellent
investment experience or knowledge. Confidence and experience were not
protective here.

Scope: one US brokerage, one sample window, and a mechanical definition of
what counts as panic selling. Use the shape of the finding, not the exact
percentages.
