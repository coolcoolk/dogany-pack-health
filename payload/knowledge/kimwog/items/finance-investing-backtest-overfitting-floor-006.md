---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/backtest-overfitting-floor-006.
id: finance-investing/backtest-overfitting-floor-006
domain: finance-investing
grade: A (field-methodology)
lane: "@quant-market"
locale: universal
as_of: 2014
contested: no
sources:
  - "Bailey, D. H., Borwein, J. M., Lopez de Prado, M. and Zhu, Q. J. (2014). Pseudo-Mathematics and Financial Charlatanism: The Effects of Backtest Overfitting on Out-of-Sample Performance. Notices of the American Mathematical Society 61(5), 458-471. https://www.ams.org/notices/201405/rnoti-p458.pdf"
  - "Harvey, C. R., Liu, Y. and Zhu, H. (2016). ... and the Cross-Section of Expected Returns. The Review of Financial Studies 29(1), 5-68. Cited here for the multiple-testing framing that the same problem produces in the published literature."
claim: >
  A high backtested performance figure carries almost no information unless
  the number of strategy configurations tried is also reported. Bailey,
  Borwein, Lopez de Prado and Zhu (2014) prove that high simulated
  performance is easily achievable after backtesting a relatively small
  number of alternative strategy configurations, so the maximum in-sample
  Sharpe ratio rises mechanically with the number of trials even when the
  true expected return is zero. The paper names this as a large part of the
  reason so many algorithmic or systematic funds fail to live up to the
  expectations their managers generated. Forced downgrade rule for this
  lane: a performance claim that does not disclose the number of variants
  tested, or that was selected AFTER seeing the data, cannot be graded above
  the practitioner band, no matter how strong the reported statistics are.
reasoning: >
  Top band as a FIELD-METHODOLOGY finding, mirroring how
  nutrition/observational-dominance-003 anchors its own lane: it is a
  mathematical result about what a selection process does to a test
  statistic, not an empirical regularity that could decay. It is the reason
  this lane treats an undisclosed-trial-count backtest as evidence of
  nothing rather than as weak evidence of something.
---

# finance-investing/backtest-overfitting-floor-006

If you try enough strategy variants on the same historical data, one of them
will look excellent by pure chance. That is a theorem, not a suspicion: the
best in-sample result climbs predictably as the number of variants tested
grows, even when none of the variants has any real edge. The 2014 paper that
formalizes this argues it is a large part of why systematic funds so often
fail to deliver what their marketing implied.

The operational rule that follows is blunt. A backtest is only interpretable
alongside the number of configurations that were tried to produce it. Almost
no backtest presented to a retail investor discloses that number. Absent that
disclosure, the correct treatment is that the backtest is uninformative --
not weak evidence, not suggestive evidence, uninformative.

This is the floor the rest of the lane rests on. It is why a strategy that
"worked historically" is not, by itself, ever a reason to act, and why
anything selected after looking at the data has to be spoken about at the
bottom of the confidence ladder.
