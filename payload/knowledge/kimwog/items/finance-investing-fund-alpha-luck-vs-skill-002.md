---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/fund-alpha-luck-vs-skill-002.
id: finance-investing/fund-alpha-luck-vs-skill-002
domain: finance-investing
grade: C (contested)
lane: "@quant-market"
locale: universal
as_of: 2010 / 2022
contested: yes
sources:
  - "Fama, E. F. and French, K. R. (2010). Luck versus Skill in the Cross-Section of Mutual Fund Returns. The Journal of Finance 65(5), 1915-1947. Open copy: https://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S8C-FamaFrench-LuckvSkill-JF10.pdf"
  - "Harvey, C. R. and Liu, Y. (2022). Luck versus Skill in the Cross Section of Mutual Fund Returns: Reexamining the Evidence. The Journal of Finance 77(3), 1921-1966. https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.13123"
  - "Kosowski, R., Timmermann, A., Wermers, R. and White, H. (2006). Can Mutual Fund Stars Really Pick Stocks? The Journal of Finance 61(6), 2551-2595. Cited here as the opposite pole that Harvey and Liu (2022) reconcile against."
claim: >
  Whether any meaningful number of active fund managers have real skill after
  fees is UNSETTLED at the method level, and both poles are published in the
  same flagship journal. Fama and French (2010) bootstrap the cross-section
  of US equity fund alphas and conclude that the aggregate portfolio of
  actively managed US equity funds is close to the market portfolio while the
  high costs of active management show up intact as lower returns to
  investors, with few funds producing benchmark-adjusted returns sufficient
  to cover their costs. Harvey and Liu (2022) then reconcile that against
  Kosowski et al. (2006), which reached the opposite conclusion, and find the
  disagreement is a statistical-power artifact on BOTH sides: the Fama-French
  method suffers an undersampling problem that fails to reject a zero-alpha
  null even when some funds generate economically large risk-adjusted
  returns, while Kosowski et al. substantially over-reject the null even when
  all funds have zero alpha. Actionable residue that survives both sides:
  identifying a skilled manager IN ADVANCE is not demonstrated by either
  paper.
reasoning: >
  Held contested on purpose. The popular one-line version ("studies prove
  active managers have no skill") overstates Fama and French and ignores a
  same-journal methodological rebuttal that neither confirms nor refutes
  skill but shows the test was underpowered. The cost identity in
  finance-investing/active-arithmetic-cost-floor-001 is what actually carries
  the practical conclusion here; this item exists so that conclusion is not
  propped up on a contested skill result it does not need.
---

# finance-investing/fund-alpha-luck-vs-skill-002

The question "do active fund managers have skill?" is genuinely open in the
academic literature, and the honest answer is that the field is arguing about
statistical power, not about a settled fact.

The widely cited 2010 study found that the whole population of actively
managed US equity funds looks a lot like the market before costs, and that
the costs come straight out of investor returns, with very few funds clearing
their own fees. A 2022 paper in the same journal then took the two leading
studies that disagreed with each other and showed why: the 2010 method is
biased toward finding nothing (it can miss funds with economically large
risk-adjusted returns), while the earlier opposing method is biased toward
finding something (it flags skill even when nobody has any).

What survives regardless of which side wins: neither paper shows anyone can
pick the skilled manager ahead of time. So the practical guidance should rest
on the cost identity, which is not in dispute, rather than on a skill claim
that is. Speak about this as an unresolved methodological dispute, never as a
proven absence of skill.
