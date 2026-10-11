---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/post-publication-alpha-decay-005.
# Source re-audit 2026-10-06: published JF abstract re-read -- the authors call
# the 26 pct out-of-sample decline an UPPER BOUND on data-mining bias, not an
# estimate of it; wording scoped. The HEC 'open copy' is the 2012 working
# paper (82 characteristics, ~10 / ~35 pct), relabelled so its numbers are
# not mistaken for the published ones.
id: finance-investing/post-publication-alpha-decay-005
domain: finance-investing
grade: B
lane: "@quant-market"
locale: universal
as_of: 2016
contested: no
sources:
  - "McLean, R. D. and Pontiff, J. (2016). Does Academic Research Destroy Stock Return Predictability? The Journal of Finance 71(1), 5-32. https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365"
  - "Earlier working-paper draft (2012; 82 characteristics, ~10 pct out-of-sample / ~35 pct post-publication -- NOT the published figures): https://www.hec.ca/finance/Fichier/McLean.pdf"
claim: >
  A published return-predictability result systematically shrinks after the
  period it was discovered in. Across 97 variables shown to predict
  cross-sectional stock returns, portfolio returns are 26 percent lower
  out-of-sample and 58 percent lower post-publication. The authors treat
  the 26 percent out-of-sample decline as an UPPER BOUND on statistical
  (data-mining) bias -- the in-sample advantage of having selected the
  variable on that sample -- and estimate a further 32 percent (58 minus
  26) lower return attributable to publication-informed trading. Direct
  operational consequence: any strategy presented with a backtest has
  already spent its most flattering period, and the expected forward return
  is materially below the figure being shown. This is a base rate to apply
  to EVERY historical performance number, not a criticism of any one
  strategy.
reasoning: >
  Single flagship-journal study with a large variable set and a clean
  identification of the publication date as the event, so it sits at the
  strong empirical band rather than the top band -- it is one paper, not a
  replicated multi-lab consensus, and it is US-sample. Paired deliberately
  with finance-investing/backtest-overfitting-floor-006: overfitting
  explains why the in-sample number was too high to begin with, decay
  explains why even an honest number falls after it is known.
---

# finance-investing/post-publication-alpha-decay-005

Return-predictability findings fade. Looking at 97 published predictors of
stock returns, the same strategies delivered 26 percent lower returns
out-of-sample, and 58 percent lower after the paper was published. The gap
between those two numbers -- about 32 percent -- is the part attributable to
other investors reading the paper and trading on it. The first 26 percent is
at most the ordinary penalty for having chosen the variable because it worked
on that particular sample; the authors present it as an upper bound.

The practical use of this is as a discount rate on every historical
performance figure. Whenever a strategy is presented with a backtest, the
forward-looking expectation is not the backtested number. It is meaningfully
below it, and the better known the strategy is, the further below it sits.

This is the reason a plausible-sounding, historically excellent strategy is
still not a reason to act. The history is the part that is guaranteed to look
good; that is how it got selected.
