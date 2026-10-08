---
# STUDY-CRAFT LANE OPENING. learning-habits had 13 items, all in the
# @behavioral evidence lane, and none of them says how to RUN a spacing
# schedule. This is the first item of the @study-craft lane (VC-E), modelled on
# exercise's @gym-craft: the basis is stated, its epistemic status is marked,
# and nothing ships merely because it is widely repeated.
#
# Primary read at source (the in-press manuscript PDF at files.eric.ed.gov,
# identical in the figures used here to the published Psychological Science
# article). Every number below was taken from that read, not from a summary --
# an earlier automated summary of the same PDF wrongly described the paper as a
# meta-analysis, which is exactly the failure mode this lane exists to avoid.
id: learning-habits/interval-from-retention-target-014
domain: learning-habits
grade: C (one large experiment + practitioner extrapolation)
lane: "@study-craft"
locale: universal
as_of: 2008
contested: yes
sources:
  - "https://doi.org/10.1111/j.1467-9280.2008.02209.x"
  - "Cepeda, N. J., Vul, E., Rohrer, D., Wixted, J. T., & Pashler, H. (2008). Spacing Effects in Learning: A Temporal Ridgeline of Optimal Retention. Psychological Science, 19(11), 1095-1102."
  - "https://files.eric.ed.gov/fulltext/ED505660.pdf"  # in-press manuscript, read directly at source for every figure quoted here
  - "learning-habits/spaced-retrieval-meta-012"  # within-warehouse cross-ref: the evidence lane establishes THAT spacing works; this item is the scheduling craft built on top of it
  - "framework:GRADE -- the measured core is ONE large web-panel experiment (1354 subjects, 26 gap-by-retention-interval conditions, 32 obscure trivia facts with single-word answers). The scheduling prescription built on top of it is practitioner extrapolation, not a tested protocol. No trial compares whole study SCHEDULES against each other."
claim: >
  A review interval is not a property of the material and cannot be set without
  first naming the date you want to still know it. The source paper's own
  words: "The optimally efficient gap between study sessions is not some
  absolute quantity that can be recommended, but a quantity that depends
  dramatically upon the retention interval." Measured optimal gaps were 1, 11,
  21 and 21 days for retention intervals of 7, 35, 70 and 350 days
  respectively (recall data), and the fitted surface puts the optimum for a
  350-day target at 23 days, "which is just 7% of the RI" -- so the
  gap-to-target RATIO FALLS as the target lengthens, and the widely circulated
  fixed "10-20% of the retention interval" rule misstates the very paper it
  cites. Critically for practice, the curve is ASYMMETRIC: "while there are
  costs to using a gap that is longer than the optimal value, these costs are
  much smaller than the costs of using too small a gap value." Practical
  consequence: pick the target date first, err LONG rather than short, and let
  a scheduler hold the intervals rather than hand-managing them.
reasoning: >
  Cepeda, Vul, Rohrer, Wixted & Pashler (2008) trained 1354 subjects from an
  internet memory-research panel to one perfect recall of 32 obscure-but-true
  trivia facts, ran a second study session after a prescribed gap, and tested
  after a further retention interval, across 26 gap-by-retention-interval
  combinations. Final performance rose with increasing gap and then fell, for
  every retention interval -- an interior optimum, not a monotone benefit. The
  optimum's ABSOLUTE size grew with the retention interval while its RATIO to
  the retention interval shrank; that combination is what kills any fixed
  percentage rule, and the paper reports that its own optimal-gap estimates
  "depart noticeably from the fixed ratio of retention interval suggested by
  some earlier researchers based on much shorter-term studies."
  .
  What is NOT established here, and must not be implied. The materials were 32
  trivia facts with 5-to-6-letter single-word answers; nothing in this
  experiment speaks to procedural skill, conceptual understanding, or
  productive language use (see learning-habits/surface-vs-deep-skew-013 for the
  warehouse's standing limiter on exactly this over-generalisation). It is one
  experiment, not a replicated protocol, and it compared GAPS between two study
  sessions, not multi-month schedules of the kind a spaced-repetition
  application actually runs. The step from "the optimal two-session gap depends
  on the target date" to "therefore run your schedule this way" is craft
  reasoning, and is marked contested for that reason -- the direction is well
  supported, the prescription is not a tested object.
---

# learning-habits/interval-from-retention-target-014

The evidence lane in this domain establishes that spacing works. It does not
say what interval to use, and that is the first thing anyone actually needs.

The most systematic long-interval experiment on the question trained 1354
people on a set of trivia facts, re-studied them after a gap, and tested them
after a further delay, crossing 26 combinations of gap and delay. Two results
matter for practice.

First, there is no universal interval. Performance rose with a wider gap and
then fell again, so there is a best gap -- but where it sits depends entirely
on how long you want to remember. The measured optima were roughly one day for
a one-week target, eleven days for a five-week target, and about three weeks
for both the ten-week and one-year targets. Notice what that does to the
percentage: three weeks is a large share of a ten-week target and about a
fourteenth of a one-year target. The ratio falls as the horizon lengthens. The
"space at ten to twenty percent of your retention interval" rule that
circulates as a takeaway from this literature is a fixed number stretched over
a relationship that is not fixed, and the paper explicitly says its own
estimates depart from that kind of fixed-ratio advice.

Second, and more useful day to day, the cost of being wrong is lopsided. The
paper states plainly that the penalty for a gap that is too LONG is much
smaller than the penalty for one that is too SHORT: accuracy climbs steeply as
the gap widens and then falls away only gradually. So when the interval is
uncertain -- which is always -- the cheap error is to wait longer, and the
expensive error is to review too soon. That single asymmetry is what makes an
imperfectly-kept schedule workable at all, and it is the load-bearing fact
behind this lane's item on lapses.

How to actually run it. Name the horizon before setting the interval: an exam
in six weeks, a language you intend to still speak in five years, and a fact
you need for one meeting are three different schedules for identical material.
Then let software hold the intervals. This is not a claim that any particular
scheduling algorithm is best -- see the refusals recorded for this lane in
GAPS.md, where a specific published improvement figure for one popular
algorithm was declined because the benchmark behind it is self-published by the
algorithm's own authors and the peer-reviewed version rests on the data of the
vendor that employed them. The defensible claim is narrower and enough:
interval arithmetic across hundreds of items is bookkeeping, humans do not do
bookkeeping reliably, and a scheduler is the thing that exists to replace it.

Honest limit. This is one experiment, on 32 trivia facts with one-word answers,
comparing the gap between two study sessions. It is a good experiment and it is
large, but it is not a tested schedule, and everything above the phrase "pick
the horizon first, err long" is reasoning rather than measurement.
