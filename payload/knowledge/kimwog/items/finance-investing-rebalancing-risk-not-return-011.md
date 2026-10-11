---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/rebalancing-risk-not-return-011.
id: finance-investing/rebalancing-risk-not-return-011
domain: finance-investing
grade: B
lane: "@quant-market"
locale: universal
as_of: 1988 / 2011
contested: no
sources:
  - "Perold, A. F. and Sharpe, W. F. (1988). Dynamic Strategies for Asset Allocation. Financial Analysts Journal 44(1), 16-27. https://www.tandfonline.com/doi/abs/10.2469/faj.v44.n1.16"
  - "Willenbrock, S. (2011). Diversification Return, Portfolio Rebalancing, and the Commodity Return Puzzle. Financial Analysts Journal 67(4), 42-49. Open copy: https://arxiv.org/abs/1109.1256"
claim: >
  Rebalancing is a risk-control decision with a known payoff shape, not a
  return-generating strategy. Perold and Sharpe (1988) classify a constant-mix
  policy (holding a fixed fraction in stocks, therefore buying as the market
  falls and selling as it rises) as a CONCAVE strategy: it outperforms in
  oscillating markets and underperforms buy-and-hold in sustained trends, and
  it is the buy-and-hold portfolio, not the rebalanced one, whose payoff is
  linear in the market. Willenbrock (2011) resolves the common confusion
  about the so-called rebalancing bonus: the diversification return of a
  rebalanced portfolio is not created by variance reduction, it comes from
  the forced selling of relatively appreciated assets and buying of
  relatively depreciated ones, and the buy-and-hold alternative earns its own
  incremental return from the opposite mechanism (winners becoming a larger
  share of the portfolio). Operational consequence: choose a rebalancing
  policy to hold the risk profile you intended, and treat any claimed return
  premium from rebalancing frequency as unproven.
reasoning: >
  Two peer-reviewed primaries in the same practitioner-facing journal, one
  giving the payoff taxonomy and one correcting the most common
  misattribution, with no live dispute between them -- hence the strong
  empirical band. Deliberately NOT graded at the top: neither paper
  establishes an optimal rebalancing frequency, and the lane holds no
  defensible evidence that any particular calendar or threshold rule beats
  another. That absence is recorded in GAPS.md rather than filled with a
  plausible-sounding number.
---

# finance-investing/rebalancing-risk-not-return-011

Rebalancing back to target weights is a way of keeping the risk you chose,
not a way of earning extra return. Holding a constant mix means buying as
markets fall and selling as they rise, which is a concave payoff: it does
well when markets oscillate and it lags a simple buy-and-hold portfolio when
markets trend in one direction for a long time. The linear, do-nothing payoff
belongs to buy-and-hold, not to the rebalanced portfolio.

The frequently cited "rebalancing bonus" is also widely misunderstood. It
does not come from reducing variance. It comes from the mechanical act of
selling what has gone up in relative terms and buying what has gone down --
and the buy-and-hold portfolio earns its own incremental return from exactly
the opposite mechanism, letting winners grow into a larger share. Neither is
free money.

The usable conclusion is narrow: pick a rebalancing policy because it keeps
the portfolio at the risk level you intended, and be sceptical of anyone
claiming a specific rebalancing frequency raises returns. This lane holds no
evidence that any particular schedule is optimal, and does not pretend to.
