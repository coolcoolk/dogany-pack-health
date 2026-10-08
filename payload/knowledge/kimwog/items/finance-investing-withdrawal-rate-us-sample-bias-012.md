---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/withdrawal-rate-us-sample-bias-012.
id: finance-investing/withdrawal-rate-us-sample-bias-012
domain: finance-investing
grade: C (contested)
lane: "@quant-market"
locale: universal
as_of: 1994 (original) / 2025 (broad-sample rebuttal)
contested: yes
sources:
  - "Bengen, W. P. (1994). Determining Withdrawal Rates Using Historical Data. Journal of Financial Planning 7(4), 171-180. Publisher copy: https://www.financialplanningassociation.org/sites/default/files/2021-04/MAR04%20Determining%20Withdrawal%20Rates%20Using%20Historical%20Data.pdf"
  - "Anarkulova, A., Cederburg, S., O'Doherty, M. S. and Sias, R. W. (2025). The safe withdrawal rate: evidence from a broad sample of developed markets. Journal of Pension Economics and Finance 24(3), 464-500. https://doi.org/10.2139/ssrn.4227132"
claim: >
  The widely repeated 4 percent retirement withdrawal rule is a US-only,
  20th-century result, and it does not survive being tested on a broader
  sample of developed markets. Bengen (1994) derived it from US stock and
  intermediate Treasury returns over rolling periods beginning in 1926, for a
  30-year horizon. Anarkulova, Cederburg, O'Doherty and Sias (2025), using a
  dataset of asset-class returns across 38 developed countries, report that a
  65-year-old couple willing to accept a 5 percent chance of financial ruin
  can withdraw only about 2.26 percent per year -- materially below
  conventional advice. The gap is not a modelling quibble: it is the
  difference between calibrating on the single most successful equity market
  of the 20th century and calibrating on the full cross-section of developed
  markets, i.e. survivorship at the level of the COUNTRY, not the fund.
  Directly load-bearing for any non-US investor.
reasoning: >
  Contested is the honest state: both numbers are published, both are
  defensible given their samples, and the disagreement is entirely about
  which sample is the right reference class. Held at the observational band
  because a withdrawal rate is a simulation output conditional on an assumed
  return distribution, not a measured effect -- neither figure is a fact
  about the future. Flagged for a Korean user in particular: US-derived
  retirement heuristics inherit US equity outperformance as an assumption,
  and Korea is not in the sample that produced the 4 percent figure.
---

# finance-investing/withdrawal-rate-us-sample-bias-012

The 4 percent rule -- withdraw 4 percent of the initial portfolio in year one
and adjust for inflation thereafter -- comes from a 1994 study of US stock
and Treasury returns over rolling periods starting in 1926, for a 30-year
retirement.

A 2025 study rebuilt the same question on a dataset covering 38 developed
countries and reached a very different answer: a 65-year-old couple accepting
a 5 percent chance of running out of money could withdraw only about 2.26
percent a year.

The difference is not a technical disagreement about method. It is about
which history counts as the reference case. The US equity market of the 20th
century was an outlier among developed markets, and calibrating a lifetime
spending rule on the single most successful market is survivorship bias
applied at the level of a country rather than a fund.

Neither figure should be spoken as the answer. What should be spoken is the
structure: any retirement withdrawal heuristic inherits the return
distribution of the market it was fitted on, and a rule derived from US
history is a bet that the future resembles that specific history. For an
investor outside the US that assumption is doing a great deal of unexamined
work.
