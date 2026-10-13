---
# Collection sprint 2026-09-02 (mental-health lane expansion). The item that
# governs every other item in this lane when it is applied to ONE person. Every
# effect size in this domain is a group average, and this is the measured reason
# a group average is not a prediction about an individual. Deliberately flagged
# contested: the paper drew four published commentaries in PNAS in 2019, and the
# strength of the ergodicity argument is genuinely disputed even where the
# empirical variance finding is not.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/group-to-individual-nongeneralizability-012
domain: mental-health
grade: "B (that within-person variance substantially exceeds between-person variance in psychological measures, and that group estimates therefore understate individual variability); C (the strong ergodicity framing, which is contested in published commentary)"
lane: "@clinical"
locale: universal
as_of: 2018
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/29915059/"  # Fisher AJ, Medaglia JD, Jeronimus BF. 2018, Proc Natl Acad Sci USA 115(27):E6106-E6115, doi 10.1073/pnas.1711978115, PMCID PMC6142277 -- six repeated-measures samples, 87 to 94 participants each with an equal number of assessments per participant
  - "https://doi.org/10.1073/pnas.1820221116"  # published commentary, PNAS 2019;116(14):6542-6543 -- one of four commentaries on the above
  - "https://doi.org/10.1073/pnas.1818675116"  # published commentary, PNAS 2019;116(14):6540-6541
  - "https://doi.org/10.1073/pnas.1820222116"  # published commentary, PNAS 2019;116(14):6546-6547
  - "https://doi.org/10.1073/pnas.1818033116"  # published commentary, PNAS 2019;116(14):6544-6545
  - "mental-health/pubbias-shrinkage-005"  # the domain's existing finding on what happens to group-level effect sizes under scrutiny; this item is the orthogonal problem
  - "framework:GRADE -- the empirical variance comparison is a direct within-study measurement and is graded at the trial band. The theoretical claim built on it (that psychological processes are non-ergodic and group inference is therefore invalid for individuals) attracted four published rebuttals and is graded lower and flagged contested."
refraction_notes:
  - note: >
      The measured result, which is the durable part. Across six repeated-measures
      samples (87 to 94 participants each, equal numbers of assessments per
      person), central tendency estimates showed some agreement between the group
      and the individual. But the VARIANCE around the expected value was TWO TO
      FOUR TIMES LARGER within individuals than within groups. The average of a
      population is a poor guide to how much any one person swings.
    grade: B
  - note: >
      What that does to every other number in this lane. An effect size, a
      correlation, a dose-response curve -- all of them are computed across people.
      If individual variability is two to four times what the group statistic
      implies, then a group-level estimate systematically understates the range a
      single person will actually experience, and the confidence with which it can
      be applied to that person is correspondingly lower than the confidence
      interval printed next to it.
    grade: B
  - note: >
      Contested, and honestly so. Four commentaries were published in PNAS in
      2019 responding to this paper. The dispute is not primarily about whether
      the variances differ -- they were measured -- but about how far the ergodicity
      argument licenses the conclusion that group-based research is invalid for
      individuals, and about whether the comparison as constructed is the right
      test. The empirical observation is carried at the trial band; the strong
      theoretical reading is carried lower and must not be spoken as settled.
    grade: C
  - note: >
      The correct operational response is NOT to abandon group evidence. It is to
      state group findings as what they are -- what happened on average across
      other people -- and to treat any individual application as a hypothesis about
      that person rather than a prediction. Where within-person repeated data
      exists, the comparison that carries information is that person against their
      own history, not that person against a population mean.
    grade: B
  - note: >
      Direct collision with the tracking case. A system holding one person's
      daily blocks, sleep and workload is holding within-person time-series data,
      and the temptation is to interpret it using population correlations -- "sleep
      and mood are correlated, therefore your bad mood is the short night". That
      inference is exactly the one this paper says does not follow, and the
      warehouse's separate finding on passive sensing (item 013) shows the
      individual-level version has not been established either.
    grade: B
claim: >
  Group-level psychological findings do not transfer cleanly to individuals, and
  the size of the gap has been measured. Fisher, Medaglia and Jeronimus 2018
  (PNAS) compared interindividual with intraindividual variation across six
  repeated-measures samples of 87 to 94 participants each, with an equal number
  of assessments per participant. Central tendency estimates showed some
  agreement between group and individual, but the VARIANCE around the expected
  value was two to four times larger WITHIN individuals than within groups. The
  authors argue that only ergodic processes permit group-to-individual
  generalisation, that human psychological processes are individually variable
  and time-varying and therefore unlikely to be ergodic, and that literatures in
  the social and medical sciences may consequently overestimate the accuracy of
  aggregated statistical estimates. The empirical variance comparison is the
  durable part; the strong ergodicity conclusion drew four published commentaries
  in PNAS in 2019 and is genuinely disputed. The operative consequence for this
  lane: every effect size it holds is an average over other people, a group
  average systematically understates how much one person swings, and applying a
  population correlation to a specific person's tracked data is an inference the
  data does not support. The correct response is not to discard group evidence
  but to speak it as what happened on average elsewhere, and to treat any
  individual application as a hypothesis to be checked against that person's own
  history rather than as a prediction.
reasoning: >
  This item is the governor on the rest of the lane. Everything else here is a
  pooled estimate over a population, and the consumer is an assistant looking at
  exactly one person's data. Fisher et al. 2018 is the cleanest available
  measurement of the gap between those two things: six independent samples, a
  symmetric comparison of between-person and within-person variation, and a
  result -- two to four times the variance within individuals -- that is a
  measurement rather than an argument. It was chosen over the broader
  methodological literature on ergodicity because it reports a number, and a
  number is what makes the caution operational rather than rhetorical. The item
  is flagged contested on purpose and the grade is split, because the paper's
  empirical finding and its theoretical conclusion have very different standing:
  the variance comparison was measured, while the claim that group-based
  inference is therefore invalid for individuals attracted four published
  commentaries in the same journal within a year. Laundering the contested half
  into the measured half would be exactly the failure mode this warehouse exists
  to prevent, so both are carried with separate grades. The practical note about
  tracking data is included because that is the live case: this warehouse's
  consumer holds one person's time series and will be tempted to read it through
  population correlations, and this item plus item 013 together say why that
  specific move fails.
---

# mental-health/group-to-individual-nongeneralizability-012

Every effect size in this lane is an average over other people. This item is
about what that does and does not tell you about one person.

Researchers took six datasets in which the same individuals were measured
repeatedly, dozens of times each, and did something unusual: they compared how
much the measure varied between people with how much it varied within a single
person over time. Same construct, same data, two different kinds of spread.

The averages agreed reasonably well. The spread did not. The variance around the
expected value was two to four times larger inside individuals than across the
group.

That is the whole finding and it is enough to change how the rest of this lane
should be spoken. A group statistic is built from between-person variation. If a
single person actually swings two to four times more than that statistic implies,
then the confidence interval printed next to a population estimate is not the
uncertainty that applies to any particular person. It is narrower. Sometimes much
narrower.

The authors go further than the measurement. They argue that group results only
transfer to individuals when the process is ergodic, that psychological processes
are individually variable and time-varying and therefore almost certainly are
not, and that large parts of social and medical science may be overstating how
accurate their aggregate estimates are.

That second part is contested, and it should be said so. Four separate
commentaries were published in the same journal within a year, disagreeing about
how far the ergodicity argument can be pushed and about whether the comparison
was set up correctly. The variance measurement is not what is in dispute; the
sweeping conclusion built on it is. Both are kept here, on different footings.

The wrong lesson would be to throw out group evidence. There is nothing better,
and a well-run trial still contains real information. The right lesson is a
change in voice: a group finding is a statement about what happened on average to
other people, and applying it to one person is a hypothesis about that person,
not a prediction of what they will do.

Which lands directly on the case this warehouse actually faces. A system that
holds one person's sleep, workload and daily blocks holds within-person
time-series data, and the obvious move is to explain that data using population
correlations -- short night, and the literature says sleep and mood move together,
so the flat afternoon is the short night. This paper is the reason that
inference does not follow. The warehouse's neighbouring item on passive sensing
is the reason the individual-level version has not been demonstrated either.

Where there is real repeated data on one person, the comparison that carries
information is that person against their own history. Not against a mean built
from strangers.
