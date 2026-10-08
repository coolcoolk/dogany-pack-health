---
# Collection sprint 2026-09-02 (mental-health lane expansion). The observational
# partner to item 008, deliberately kept SEPARATE from it. 008 is about treating
# a diagnosed condition in trials; this is about the association between habitual
# activity and later onset in cohorts. They answer different questions, carry
# different weaknesses, and are constantly merged into one sentence in popular
# retellings. Keeping them apart is the point of authoring two items.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/activity-incident-depression-observational-009
domain: mental-health
grade: "B (that habitual physical activity is inversely associated with later depression in prospective cohorts, with a curvilinear shape and diminishing returns); D (any causal reading, and any use of the preventable-fraction figure)"
lane: "@clinical"
locale: universal
as_of: 2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/35416941/"  # Pearce M, Garcia L, Abbas A, Strain T, Schuch FB, Golubic R, Kelly P, Khan S, Utukuri M, Laird Y, Mok A, Smith A, Tainio M, Brage S, Woodcock J. 2022, JAMA Psychiatry 79(6):550-559, doi 10.1001/jamapsychiatry.2022.0609, PMCID PMC9008579 -- systematic review and two-stage random-effects dose-response meta-analysis of 15 prospective cohorts, 191130 participants, 2110588 person-years <!-- estate-scrub:allow(author surname Smith, not an instance) -->
  - "mental-health/exercise-depression-trial-certainty-008"  # the TRIAL evidence on treating diagnosed depression; a different question with different weaknesses
  - "nutrition/observational-dominance-003"  # the warehouse's existing rule on what an observational literature can and cannot license
  - "framework:GRADE -- a prospective cohort literature starts below the trial band for causal claims regardless of how large it is. Size buys precision, not identification."
applicability:
  axes:
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The shape is the finding, not the endpoint numbers. The dose-response
      curve is inverse and CURVILINEAR, with the steepest gradient at the LOW
      end. Relative to adults reporting no activity, those accumulating half the
      recommended volume (4.4 marginal MET-hours per week) had 18 percent lower
      risk (95 percent CI 13 to 23); at the full recommended volume (8.8 marginal
      MET-hours per week) it was 25 percent lower (95 percent CI 18 to 32). Past
      that, additional benefit diminished and uncertainty widened. If any of this
      is to be acted on, the actionable part is that the first increment from
      nothing to something is where the association is steepest -- not that more
      is linearly better.
    grade: B
  - note: >
      Heterogeneity was large and significant (I-squared 74 percent, p less than
      0.001). That is not a footnote on a pooled curve; it means the cohorts
      disagree substantially with one another and the pooled gradient is an
      average over genuinely different populations, exposure instruments and
      outcome definitions.
    grade: A
  - note: >
      Reverse causation is the obvious and unresolved alternative explanation.
      Reduced activity is itself a feature of depression, often present before a
      diagnosis is recorded. A prospective design with three or more years of
      follow-up reduces this concern; it does not remove it. No cohort in this
      literature randomised anybody to activity, so nothing here identifies a
      causal effect.
    grade: A
  - note: >
      Exposure measurement. Physical activity in these cohorts is overwhelmingly
      self-reported, and the outcome mixes registry or interview-based major
      depressive disorder with elevated symptoms on a screening instrument. The
      warehouse already records what a screening instrument does to a prevalence
      figure (item 011); an outcome partly defined that way inherits that
      inflation.
    grade: A
  - note: >
      DO NOT carry the preventable-fraction figure. The review estimates that if
      less active adults had reached the recommended volume, 11.5 percent of
      depression cases could have been prevented (95 percent CI 7.7 to 15.4).
      That number is a population-attributable calculation built ON TOP of the
      causal assumption the design cannot support. It is legitimate as a
      public-health modelling exercise and illegitimate as a statement to an
      individual person about their own risk.
    grade: D
claim: >
  In prospective cohorts, habitually more active adults develop depression less
  often than inactive adults, and the relationship is curvilinear with the
  steepest gradient at the bottom of the activity range. Pearce et al. 2022
  (JAMA Psychiatry, 15 cohorts, 191130 participants, 2110588 person-years)
  report that relative to adults reporting no activity, those at half the
  recommended volume (4.4 marginal MET-hours per week) had 18 percent lower risk
  (95 percent CI 13 to 23) and those at the full recommended volume (8.8 marginal
  MET-hours per week) had 25 percent lower risk (95 percent CI 18 to 32), with
  diminishing additional benefit and widening uncertainty beyond that.
  Heterogeneity was large and significant (I-squared 74 percent). This is an
  ASSOCIATION with incident depression in observational data, not a treatment
  effect and not a causal estimate: nobody was randomised, activity is
  self-reported, the outcome mixes diagnosed disorder with screening-instrument
  symptom cut-offs, and reduced activity is itself an early feature of the
  condition being predicted. The review's population-attributable estimate that
  11.5 percent of cases could have been prevented rests on the causal assumption
  the design cannot supply and must not be repeated to an individual. The one
  robust and usable shape: the first move from nothing to something is where the
  association is steepest, and more beyond the recommended volume buys
  progressively less with progressively more uncertainty.
reasoning: >
  This item exists because item 008 does. The two are constantly fused into a
  single sentence -- "exercise treats and prevents depression" -- and they are
  different claims resting on different designs with different failure modes.
  008 is randomised evidence about treating people who already meet a clinical
  threshold, and its weakness is risk of bias and unblindable expectancy. This
  item is observational evidence about who later develops the condition, and its
  weakness is confounding and reverse causation. Neither weakness fixes the
  other, and a reader who merges them ends up with a claim that appears to have
  both randomisation and long-run population reach when in fact no single body
  of evidence has both. Pearce et al. 2022 was chosen because it is the
  dose-response synthesis rather than a binary active-versus-inactive comparison,
  which is what makes its shape usable: the curve is steepest at the low end,
  which is the opposite of the "more is better" reading that a metrics-driven
  system defaults to. Graded at the trial band for the existence and shape of
  the association, because 15 prospective cohorts over two million person-years
  establish that much robustly, and at the practitioner floor for causal
  language and for the preventable-fraction figure, which is a modelling output
  and not an individual-level fact. Not flagged contested: no source located
  disputes the association, and the limits recorded here are the review's own
  design limits rather than a live scientific dispute.
---

# mental-health/activity-incident-depression-observational-009

There are two different "exercise and depression" literatures and they get
merged into one sentence constantly. This item is the second one.

The first is trials: take people who are already depressed, prescribe exercise,
measure symptoms. That evidence lives on the neighbouring item and its problem
is that hardly any of those trials are well controlled.

This one is cohorts: follow a large number of people who are not depressed,
record how active they are, and see who develops depression years later. Fifteen
such cohorts, 191130 people, over two million person-years of follow-up.

The result has a shape worth knowing. The relationship is inverse and curved,
and the curve is steepest at the bottom. Going from doing nothing to doing about
half of what the guidelines recommend is associated with roughly 18 percent lower
risk. Getting to the full recommended volume is associated with roughly 25 percent
lower. Past that, the line flattens and the uncertainty widens.

So the interesting part is not "more is better." It is that most of the
association is bought in the first increment, and the return on further volume
falls away. For anyone deciding where to spend effort, the difference between
zero and something is where this literature says the signal is.

Now the limits, which are large and which are structural rather than fixable by
sample size.

Nobody randomised anybody. This is who chose to be active, compared with who did
not, and the people in those two groups differ in a hundred ways that were not
measured. Activity was overwhelmingly self-reported. The outcome is a mixture of
diagnosed disorder and symptom-questionnaire cut-offs, and this warehouse
separately records what those cut-offs do to a count.

And the alternative explanation that never fully goes away: becoming less active
is one of the earliest things that happens when someone is heading into a
depressive episode. A three-year lag reduces that concern. It does not delete it.
Some unknown share of "inactive people get depressed more" is "people getting
depressed stop moving."

One number in that paper should never be repeated to a person. The authors
estimate that if less active adults had hit the guidelines, 11.5 percent of
depression cases could have been prevented. That is a population-attributable
calculation stacked on a causal assumption the study design cannot deliver. As
public-health modelling it is a legitimate exercise. Said to one individual about
their own odds, it is a fabrication wearing a confidence interval.

The honest summary is short. More active people get depressed less often, the
relationship is real and well measured, the first step off zero is where most of
it sits, and none of it establishes that moving more will change what happens to
any particular person.
