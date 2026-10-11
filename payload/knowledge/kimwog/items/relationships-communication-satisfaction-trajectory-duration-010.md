---
# Collection sprint 2026-09-02, relationships-communication lane expansion.
# "Does it get worse?" is the single most common question a life agent will meet
# in this domain, and until now the warehouse had nothing to answer it with. The
# useful property of this source is that it separates the AGE curve from the
# RELATIONSHIP-DURATION curve, which the popular retellings collapse into one --
# and the two curves have different shapes.
# Rubric: relationships-communication @dyadic (VC-C).
id: relationships-communication/satisfaction-trajectory-duration-010
domain: relationships-communication
grade: B (the aggregate trajectory shape by age and by relationship duration); D (any application of the mean curve to an individual couple)
lane: "@dyadic"
locale: universal
as_of: 2021
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/34928690/"  # Buhler JL, Krauss S, Orth U. 2021, Psychol Bull 147(10):1012-1053, doi 10.1037/bul0000342 -- systematic review and meta-analysis, 165 independent samples, 165,039 participants, POMP-scored
  - "relationships-communication/relationship-quality-predictors-joel-009"  # the companion constraint: the aggregate trajectory is describable, the individual trajectory is not predictable
  - "framework:GRADE -- graded at the trial-adjacent band, not the top. This is a large and carefully moderated meta-analysis of observational longitudinal samples: 165 samples, 165,039 participants, effect sizes converted to a percent-of-maximum-possible metric so heterogeneous instruments could be pooled. What it cannot deliver is causal structure, and what it must not be read as is an individual forecast -- the mean-change curve is an average over samples whose within-sample variance is not reported as a personal prediction interval. The bottom-band second grade exists specifically to block the individual reading."
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      Two different curves, routinely collapsed into one. Plotted against AGE,
      mean relationship satisfaction decreased from age 20 to 40, reached its low
      point at 40, increased until 65, then plateaued in late adulthood. Plotted
      against RELATIONSHIP DURATION, it decreased over the first 10 years,
      reached its low point at 10 years, increased until 20 years, and then
      decreased again. These are not the same shape -- the duration curve turns
      down again after year 20 and the age curve does not. Anyone quoting "it
      bottoms out and then recovers" is quoting whichever of the two happens to
      suit them. Say which metric is being used.
    grade: B
  - note: >
      The mean-change result is the one that answers the actual question. Within
      a given relationship, satisfaction DECREASED, with the largest declines in
      young adulthood and in the first years of a relationship. So the cross-
      sectional recovery after the low point is not primarily people getting
      happier inside the same relationship over time; the within-relationship
      direction is downward, steepest early. Reporting only the U-shaped
      cross-sectional curve, without the mean-change result, produces a
      systematically over-optimistic picture.
    grade: B
  - note: >
      What survived moderation, and what did not. The authors report that
      presence of children and the measure of relationship satisfaction explained
      variance in mean LEVEL. Apart from those two, the pattern of findings held
      across birth cohort, sample type, COUNTRY, ETHNICITY, gender, whether the
      household was shared with the partner, marital status, relationship
      transitions, and dyadic data. The country and ethnicity invariance is the
      only cross-cultural robustness signal this sprint located anywhere in the
      couples literature, and it is worth something -- but it is a moderator null
      inside a sample whose composition the abstract does not break down by
      region, so it is evidence of no DETECTED difference, not evidence of
      demonstrated transfer. Do not upgrade it into a claim that the curve has
      been verified in Korea.
    grade: C
  - note: >
      Instrument dependence is an explicitly reported moderator here, which is
      unusual and useful. The measure of relationship satisfaction explained
      variance in the mean level, meaning part of what looks like a difference
      between populations is a difference between questionnaires. This is the
      same tool-instability problem the warehouse records under
      nutrition/tool-instability-005 in a different domain, and it caps how
      precisely any absolute satisfaction number can be spoken.
    grade: B
  - note: >
      NOT established: any individual prediction. This item describes an average
      over 165 samples. It says nothing about whether a particular relationship
      will decline, and the companion row -- relationships-communication/
      relationship-quality-predictors-joel-009 -- shows directly that individual
      CHANGE was not predictable from self-report at all, with no analysis
      exceeding 5 percent of variance. The two must be spoken together: the
      population curve is knowable, the personal curve is not. Using the
      population curve as a personal forecast is the single most likely misuse of
      this item.
    grade: D
claim: >
  Aggregate relationship satisfaction follows a describable trajectory, and it
  is TWO trajectories, not one. In the largest synthesis available (Buhler,
  Krauss and Orth 2021, Psychological Bulletin; 165 independent samples,
  165,039 participants), satisfaction plotted against AGE decreased from 20 to
  40, bottomed at 40, rose until 65 and plateaued; plotted against RELATIONSHIP
  DURATION it decreased over the first 10 years, bottomed at 10 years, rose
  until 20 and then declined again. The mean-CHANGE result is the corrective:
  within a given relationship, satisfaction decreased, with the largest declines
  in young adulthood and in the first years of the relationship. Only two
  moderators explained variance in mean level -- presence of children, and which
  satisfaction questionnaire was used. The pattern otherwise held across birth
  cohort, sample type, country, ethnicity, gender, cohabitation, marital status,
  relationship transitions and dyadic data; treat that country/ethnicity
  invariance as no DETECTED difference rather than as demonstrated transfer to
  any specific non-Western population. None of this predicts an individual
  couple: the companion finding in Joel et al. 2020 is that individual change is
  not predictable from self-report at all.
reasoning: >
  The domain needed a row that answers "does it get worse over time" with
  something other than folklore, and this is the only source located in this
  sprint with the scale to do it -- 165 samples and 165,039 participants, with
  scores converted to a percent-of-maximum-possible metric so that incompatible
  questionnaires could be pooled honestly. Graded at the trial-adjacent band
  rather than the top because it is a meta-analysis of observational
  longitudinal data with no causal identification and no experimental arm; that
  is the ceiling for a developmental question of this kind, and the analysis
  hits it. The second, bottom-band grade is doing real work and is not a
  formality: the most probable misuse of this item is to read a mean curve over
  165 samples as a forecast for one person's relationship, and the warehouse
  already holds the direct refutation of that move in
  relationships-communication/relationship-quality-predictors-joel-009, where
  individual change proved unpredictable across 43 datasets. The two rows are
  written to be spoken together. The moderator result is handled carefully on
  purpose: a null on country and ethnicity is genuinely the best cross-cultural
  signal this sprint found in the couples literature, and it is also exactly the
  kind of finding that gets laundered into "this has been shown to hold in
  Korea", which it has not. It is recorded a band lower than the main trajectory
  claim for that reason. Not marked contested: the trajectory shape is not in
  dispute in the literature, and the disagreement the authors set out to resolve
  -- that previous research had reached no agreement on the normative
  trajectory -- is precisely what this synthesis was built to settle.
---

# relationships-communication/satisfaction-trajectory-duration-010

"Does it get worse?" has an answer, and the answer depends on which clock you
measure against.

Against AGE, average relationship satisfaction falls from twenty to forty, hits
its low point around forty, rises again until sixty-five, and then flattens.
Against RELATIONSHIP DURATION, it falls across the first ten years, bottoms at
ten, rises until twenty, and then turns down again. Those are different shapes,
and the popular version of this finding picks whichever one sounds better and
quietly drops the other.

The more honest number is the within-relationship one. Inside a given
relationship, satisfaction goes down, and the steepest decline is early -- in
young adulthood and in the first years together. The cheerful upswing in the
cross-sectional curve is largely not the same couples recovering.

What is unusual about this synthesis is how much it tested and failed to find.
Only two things explained variation in the average level: whether there were
children, and which questionnaire was used. The pattern otherwise held across
birth cohort, sample type, country, ethnicity, gender, whether the couple lived
together, marital status, and relationship transitions. That country and
ethnicity result is the closest thing to a cross-cultural robustness signal
anywhere in this literature -- but a moderator that failed to reach significance
is not the same as a curve demonstrated in a specific population. It means no
difference was detected, not that transfer was shown.

The questionnaire moderator deserves a note of its own. Part of what looks like
a real difference between groups is a difference between instruments. That caps
how precisely any absolute satisfaction figure can be stated.

And the limit that matters most in practice: this is an average over a hundred
and sixty-five samples. It does not forecast one couple. The companion finding
in this domain is that individual change could not be predicted from self-report
at all, across forty-three datasets, with nothing explaining more than five
percent of the variance. The population curve is knowable. The personal curve is
not. Saying the first while implying the second is the main way this item can be
misused.
