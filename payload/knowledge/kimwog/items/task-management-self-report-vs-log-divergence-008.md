---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# Read in full text. Every figure below is quoted from the paper's own results
# section, including the 6.12% accuracy figure, which is the number that
# matters here and is the one that never appears in secondary coverage.
id: task-management/self-report-vs-log-divergence-008
domain: task-management
grade: B (pre-registered meta-analysis with objective comparator; media-use domain, transfer to task time is by analogy)
lane: "@behavioral-productivity"
locale: universal
as_of: 2021
contested: no
sources:
  - "https://doi.org/10.1038/s41562-021-01117-5"
  - "Parry, D. A., Davidson, B. I., Sewall, C. J. R., Fisher, J. T., Mieczkowski, H., & Quintana, D. S. (2021). A systematic review and meta-analysis of discrepancies between logged and self-reported digital media use. Nature Human Behaviour, 5, 1535-1547."
refraction_notes:
  - note: >
      The measured behaviour is DIGITAL MEDIA USE, not task time. It is carried
      here because it is the only large, pre-registered, objectively
      benchmarked estimate of how far a person's estimate of their own recent
      time use sits from a machine record of it. The mechanism -- frequent,
      unremarkable, hard-to-individuate episodes are estimated badly -- applies
      directly to time spent on work. The magnitude is not asserted for task
      time.
    grade: C
claim: >
  When a person estimates their own time use and a machine logs it, the two
  agree only moderately, and the estimate is almost never right. Across 106
  effect sizes from 47 records, self-reported and logged media use correlate
  r = 0.38 (95% CI 0.33-0.42). The decisive figure is the accuracy analysis: of
  49 included comparisons, only three (6.12%) had a mean self-reported estimate
  falling within 5% of the logged mean. The direction of error is NOT
  consistent -- 46.94% of comparisons over-reported and 46.94% under-reported,
  and the pooled ratio (R = 1.21, 95% CI 0.94-1.54) cannot rule out accuracy in
  either direction. Egger's tests showed no evidence of small-study bias in any
  of the three analyses; heterogeneity was extreme (I-squared 92% for the
  correlation, 99.5% for accuracy).
reasoning: >
  Graded strong for design -- pre-registered, an objective comparator on one
  side of every comparison, no detected publication bias -- and held one band
  down because the behaviour measured is media use rather than work, so its
  application here is by analogy. Carried as the MEASUREMENT FLOOR for this
  whole lane. Every other item in it that touches a person's report of their own
  time inherits this. The specific reason it is worth an item rather than a
  footnote: the naive correction ("people overestimate, so discount") is
  refuted by the paper's own data -- the errors go both ways in almost equal
  proportion, so there is no adjustment factor to apply, only an uncertainty to
  respect.
---

# task-management/self-report-vs-log-divergence-008

If a person tells you how long they spent on something and a machine also
recorded it, the two numbers are only loosely related. Across the largest
synthesis of paired self-report and log data, the correlation is about 0.38 --
positive, real, and well below what would be needed to treat one as a stand-in
for the other.

The number that actually settles the question is not the correlation. Of 49
comparisons where an average self-report could be checked against an average
log, only three -- about 6% -- landed within 5% of the logged value. People are
rarely accurate about their own recent time use.

The second finding is the one that kills the obvious fix. Roughly 47% of
comparisons over-reported and roughly 47% under-reported. There is no reliable
direction to the error, and the pooled ratio's confidence interval spans
under-reporting, accuracy and over-reporting. So "people exaggerate, apply a
discount" is not supported. What is supported is that a self-reported duration
carries wide, two-sided uncertainty.

For a system holding both kinds of data at once, three rules follow:

- Do not treat a remembered duration and a logged duration as the same
  quantity. They correlate moderately and measure differently.
- Do not apply a correction factor to self-reports. The error has no consistent
  sign.
- Where a log exists, the log is the better measure of what happened -- but see
  task-management/record-is-not-behaviour-009, because a log kept BY THE PERSON
  is not a machine log and fails in its own specific way.
