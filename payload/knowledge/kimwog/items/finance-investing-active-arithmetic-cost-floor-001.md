---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/active-arithmetic-cost-floor-001.
id: finance-investing/active-arithmetic-cost-floor-001
domain: finance-investing
grade: A (field-methodology)
lane: "@quant-market"
locale: universal
as_of: 1991 / 2008 (cost estimate window 1980-2006)
contested: no
sources:
  - "Sharpe, W. F. (1991). The Arithmetic of Active Management. Financial Analysts Journal 47(1), 7-9. Author copy: https://web.stanford.edu/~wfsharpe/art/active/active.htm"
  - "French, K. R. (2008). Presidential Address: The Cost of Active Investing. The Journal of Finance 63(4), 1537-1573. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-6261.2008.01368.x"
  - "Pedersen, L. H. (2018). Sharpening the Arithmetic of Active Management. Financial Analysts Journal 74(1), 21-36. https://www.tandfonline.com/doi/full/10.2469/faj.v74.n1.4"
claim: >
  Cost drag is the one finance result that cannot fail out-of-sample, because
  it is an accounting identity rather than an empirical regularity. Sharpe
  (1991) states it exactly: before costs the return on the average actively
  managed dollar equals the return on the average passively managed dollar,
  and after costs the return on the average actively managed dollar is LESS
  than the return on the average passively managed dollar. French (2008)
  puts a number on the aggregate bill for the US market: averaging over
  1980-2006, investors spent 0.67 percent of the aggregate value of the
  market each year searching for superior returns, so the typical investor
  would have raised his average annual return by 67 basis points by holding
  the passive market portfolio. Boundary condition, not a refutation:
  Pedersen (2018) shows the identity assumes a literally static passive
  portfolio, and that real index funds must trade on index changes, new
  issues and delistings, so the passive side is not costless either. The
  DIRECTION of the identity survives that correction; only its exactness
  softens.
reasoning: >
  This is the lane anchor because it is the only kind of finance claim with
  no regime-dependence and no out-of-sample decay: it is arithmetic over the
  full market, true by construction in every period and every country. The
  French estimate is an empirical measurement layered on top and is
  US-specific and window-specific, so it is quoted with its window attached.
  Pedersen is cited deliberately as the strongest published objection, so
  the item does not have to be re-litigated the first time someone raises it.
---

# finance-investing/active-arithmetic-cost-floor-001

Costs are the only part of an investment outcome that is knowable in advance,
and the arithmetic behind that is not a study that might fail to replicate --
it is an identity. All investors together hold the market. So before costs,
the money managed actively earns exactly what the money managed passively
earns, and after costs it earns less, by the amount of the extra costs. This
is true every year, in every country, regardless of what markets do.

The size of the bill was measured for the US market: over 1980-2006, the
search for superior returns cost investors about 0.67 percent of the market
value each year, meaning the typical investor could have added roughly 67
basis points a year simply by holding the market.

The honest caveat, which is worth stating before someone else does: the
identity assumes a passive portfolio that never trades. Real index funds do
trade -- index reconstitutions, new listings, delistings -- so the passive
side has costs too. That narrows the gap; it does not reverse it. The rule
this item supports is narrow and durable: prefer the lower-cost way of taking
the same exposure, and treat any fee difference as the most reliable
predictable component of a long-run outcome.
