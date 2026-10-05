---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/factor-replication-contested-004.
id: finance-investing/factor-replication-contested-004
domain: finance-investing
grade: C (contested)
lane: "@quant-market"
locale: universal
as_of: 2016-2023
contested: yes
sources:
  - "Harvey, C. R., Liu, Y. and Zhu, H. (2016). ... and the Cross-Section of Expected Returns. The Review of Financial Studies 29(1), 5-68. https://academic.oup.com/rfs/article/29/1/5/1843824"
  - "Hou, K., Xue, C. and Zhang, L. (2020). Replicating Anomalies. The Review of Financial Studies 33(5), 2019-2133. https://academic.oup.com/rfs/article-abstract/33/5/2019/5236964"
  - "Jensen, T. I., Kelly, B. T. and Pedersen, L. H. (2023). Is There a Replication Crisis in Finance? The Journal of Finance 78(5), 2465-2518. https://onlinelibrary.wiley.com/doi/full/10.1111/jofi.13249"
claim: >
  How much of the published factor and anomaly literature is real is an
  ACTIVE dispute, and the answer depends on the statistical framework chosen,
  not on new data. Harvey, Liu and Zhu (2016) argue that after accounting for
  the sheer number of factors tested, a newly proposed factor should have to
  clear a t-statistic above 3.0, and that most claimed findings in financial
  economics are therefore likely false. Hou, Xue and Zhang (2020) rebuild 452
  anomalies with microcaps controlled via NYSE breakpoints and value-weighted
  returns and report that 65 percent fail even the single-test hurdle of
  absolute t of 1.96, rising to 82 percent under a multiple-test hurdle of
  2.78. Jensen, Kelly and Pedersen (2023) build a Bayesian replication model
  over 153 characteristics and reach the opposite conclusion, that most of
  the literature replicates in-sample and out-of-sample and across 93
  countries, with a replication rate above 50 percent in 11 of 13 themes.
  The disagreement is a methodology disagreement about multiple-testing
  correction and hierarchical shrinkage.
reasoning: >
  Contested is the correct state, and the item is written to keep it that
  way. This is the single easiest place in the lane for one-sided framing:
  a factor product will cite the 2023 optimistic result and a passive-only
  argument will cite the 2020 pessimistic result, and both are real papers
  in top journals. Practical downgrade rule this item anchors: any claim
  that rests on a published factor or anomaly inherits this dispute plus the
  decay documented in finance-investing/post-publication-alpha-decay-005,
  and cannot be spoken at the top of the ladder.
---

# finance-investing/factor-replication-contested-004

Whether the published catalogue of return factors is mostly real or mostly
noise is unresolved, and both answers are defended in the field's leading
journals.

One line of work says the literature has tested so many candidate factors
that the usual significance bar is meaningless, that a new factor should have
to clear a t-statistic above 3.0, and that most published findings are
therefore probably false. A large 2020 replication effort rebuilt 452
anomalies while controlling for tiny-company effects and found that 65
percent could not clear even the ordinary bar, and 82 percent could not clear
a multiple-testing bar.

A 2023 paper reaches the opposite conclusion using a Bayesian model over 153
characteristics, reporting that most of the literature does replicate,
including out-of-sample and across 93 countries.

The two camps are not looking at different data. They are choosing different
ways to correct for the fact that thousands of factors were tested. Treat any
factor-based claim as inheriting this dispute: it should be spoken as
suggestive, with the disagreement named, never as an established effect.
