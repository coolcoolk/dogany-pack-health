---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory. The meta-analysis was read at full text (open
# access), including its results and publication-bias sections, not via any
# press write-up.
id: spending-saving/payment-method-effect-small-and-shrinking-012
domain: spending-saving
grade: B (with contested flag on the popular magnitude)
lane: "@household-behavioral"
locale: universal
as_of: 2024 (synthesising 40+ years of primary studies)
contested: yes
sources:
  - "Schomburgk, L., Belli, A. and Hoffmann, A. O. I. (2024). Less cash, more splash? A meta-analysis on the cashless effect. Journal of Retailing 100, 382-403. https://doi.org/10.1016/j.jretai.2024.05.003 (open access; full text read)"
  - "Prelec, D. and Simester, D. (2001). Always Leave Home Without It: A Further Investigation of the Credit-Card Effect on Willingness to Pay. Marketing Letters 12(1), 5-12. https://doi.org/10.1023/A:1008196717017 -- the small early experiment the popular version of this claim is usually traced to"
refraction_notes:
  - note: >
      Heterogeneity is very high (I-squared = 86.20 percent) and the distribution
      of effects spans g = -1.508 to g = 1.852. A pooled mean over a distribution
      that wide is a statement about the average study, not a prediction about
      any particular person or purchase. Do not use it to forecast an individual
      household's spending change.
    grade: B
  - note: >
      The trend term matters more than the level for anyone reasoning in 2026.
      The effect declines linearly over the study period and the authors find no
      quadratic term, so the most recent studies sit at the low end. In a market
      as far into cashless payment as Korea, the current effect should be
      expected at or below the pooled figure, not above it.
    grade: C
claim: >
  The "you spend more when you do not pay in cash" effect is REAL, SMALL, and
  SHRINKING -- all three, and the popular version keeps only the first. Across
  392 effect sizes from 71 papers, Schomburgk, Belli and Hoffmann report a grand
  mean of g = 0.135, 95 percent CI [0.068, 0.203]. The distribution behind that
  mean is extremely wide: individual effects range from g = -1.508 to g = 1.852
  (mean 0.078, median 0.077, SD 0.397) with I-squared = 86.20 percent. Several
  moderator results contradict the usual mechanism story. The features of the
  payment method that the "pain of paying" account rests on do NOT moderate the
  effect on their own: neither decoupled versus coupled payment
  (b = -0.024, p = 0.568) nor high versus low transparency (b = 0.073,
  p = 0.122) is significant. What does moderate it is the consumption
  situation -- the effect is stronger for conspicuous consumption
  (mean g 0.551 versus 0.218) and weaker for pro-social consumption
  (0.023 versus 0.253) -- and the business cycle, being stronger when GDP growth
  is rising. Finally, the effect has gotten weaker over time (b = -0.006,
  p = 0.025), with no quadratic term, indicating a gradual linear decline. The
  authors ran contour-enhanced funnel plots, Egger's regression test and
  trim-and-fill, and conclude that publication bias in the dataset is unlikely
  and that funnel asymmetry is more plausibly due to effect-size heterogeneity.
reasoning: >
  Graded at the strong empirical band as a meta-analysis with explicit
  publication-bias diagnostics, and flagged contested because the number in
  circulation is not the number in the literature. This is the same failure mode
  that the finance lane's one-sided market-timing item exists to catch, and the
  same one that
  relationships-communication/source-misattribution-rule-005 catches elsewhere in
  the warehouse: an early, small, striking experiment gets quoted forever while
  the accumulated synthesis moves the estimate down by an order of magnitude. The
  item is deliberately written to carry the moderator nulls as prominently as the
  main effect, because the nulls break the mechanism story that makes the popular
  version sound inevitable -- if the effect were about the pain of parting with
  physical money, decoupling and transparency should have moved it, and they did
  not. For an agent advising a Korean household in 2026, the honest reading is
  that switching to cash is a real but marginal lever, that it is most likely to
  matter on visible-status purchases, and that the effect is smallest in exactly
  the highly cashless environments where the advice gets given most confidently.
---

# spending-saving/payment-method-effect-small-and-shrinking-012

"Pay in cash and you will spend less" is true, and much less true than it
sounds.

Forty years of studies on the question were pooled: 392 effect sizes from 71
papers. The overall effect is positive and statistically solid, and it is small
-- a standardised effect of about 0.135. The individual studies behind that
average scatter enormously, from strongly negative to strongly positive, with
the great majority of the variation coming from real differences between studies
rather than from noise. So the average is a fact about the literature, not a
prediction about one person's next purchase.

Three findings puncture the usual story. First, the features of the payment
method that the explanation depends on -- whether the payment is separated in
time from the consumption, and how visible the outflow is -- did not
independently move the effect at all. If this were fundamentally about the sting
of handing over notes, those should have mattered, and they did not. Second,
what did matter was the situation: the effect roughly doubles for conspicuous,
status-visible purchases and essentially vanishes for charitable ones. Third,
and most relevant to anyone reading this now, the effect has been shrinking
steadily and linearly over the whole period, as non-cash payment became
ordinary.

The authors checked for the obvious objection -- that only flattering results
get published -- with three separate diagnostics, and concluded publication bias
was unlikely, attributing the funnel asymmetry to genuine heterogeneity instead.

So the defensible advice is narrow. Paying in cash is a real lever and a minor
one, it is most likely to bite on purchases made to be seen, and in a country
that is already deep into cashless payment the effect should be expected at the
low end of the range rather than the high end. Anyone quoting a large percentage
increase from card use is quoting an early, small, striking experiment rather
than the accumulated evidence.
