---
# Collection sprint 2026-09-02 (mental-health lane expansion). "Burnout" is the
# word a life agent that watches workload will reach for most often, and it is
# the one whose numbers are least usable. A systematic review of 182 studies
# found at least 142 distinct definitions and a prevalence range spanning 0 to
# 80.5 percent -- so wide that the reviewers abandoned a planned meta-analysis.
# Alongside that, the WHO's ICD-11 entry constrains the word itself. Same
# handling as the domain's zombie-stat discipline: the number is not corrected,
# it is refused.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/burnout-definition-bound-015
domain: mental-health
grade: "A (that burnout prevalence figures are not comparable across studies, and that ICD-11 scopes the term to the occupational context and does not classify it as a medical condition); E (any specific burnout prevalence figure, which is refused outright rather than graded)"
lane: "@clinical"
locale: universal
as_of: 2018-2019
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/30326495/"  # Rotenstein LS, Torre M, Ramos MA, Rosales RC, Guille C, Sen S, Mata DA. 2018, JAMA 320(11):1131-1150, doi 10.1001/jama.2018.12777, PMCID PMC6233645 -- systematic review, 182 studies, 109628 individuals, 45 countries, published 1991 to 2018
  - "https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases"  # World Health Organization, 28 May 2019 -- the ICD-11 entry for burn-out, its three dimensions, its occupational-context restriction, and the explicit statement that it is not classified as a medical condition
  - "relationships-communication/zombie-stat-retraction-rule-002"  # the warehouse's existing handling for a widely circulating number that cannot be repaired
  - "mental-health/screening-score-is-not-a-diagnosis-011"  # the same instrument-threshold problem in the depression literature, with the inflation quantified
  - "framework:GRADE -- the reviewers PLANNED a meta-analytic pooling and abandoned it, judging quantitative pooling inappropriate given the variation in designs, ascertainment methods and statistical heterogeneity. A systematic review that declines to pool is stronger evidence about the state of a field than one that pools anyway."
refraction_notes:
  - note: >
      The scale of the definitional problem, stated exactly. Across 182 studies
      covering 109628 individuals in 45 countries, at least 142 UNIQUE DEFINITIONS
      were used for meeting overall burnout or burnout subscale criteria. Among
      studies using instruments based on the Maslach Burnout Inventory alone there
      were at least 47 distinct definitions of overall burnout prevalence. Reported
      overall burnout prevalence ranged from 0 percent to 80.5 percent.
    grade: A
  - note: >
      The reviewers' own response is the most informative part. Meta-analytic
      pooling was PLANNED and then judged inappropriate, because variation in study
      designs and burnout ascertainment methods, together with statistical
      heterogeneity, made it meaningless. They also report that because of these
      inconsistencies, associations between burnout and sex, age, geography, time,
      specialty and depressive symptoms COULD NOT BE RELIABLY DETERMINED. So it is
      not only the prevalence figure that fails; the correlates fail with it.
    grade: A
  - note: >
      Why this is a refusal rather than a range. A range from 0 to 80.5 percent is
      not an imprecise estimate that a larger study would tighten. It is the
      signature of a construct measured by different instruments at different
      thresholds, where the threshold choice determines the answer. No number can
      be quoted, no average of the range can be computed, and pointing at the range
      itself is the only honest use of this literature.
    grade: A
  - note: >
      What ICD-11 actually says, since it is routinely overstated in both
      directions. Burn-out is defined as "a syndrome conceptualized as resulting
      from chronic workplace stress that has not been successfully managed", with
      three dimensions: feelings of energy depletion or exhaustion; increased mental
      distance from one's job, or feelings of negativism or cynicism related to
      one's job; and reduced professional efficacy. It is listed under factors
      influencing health status or contact with health services. It is explicitly
      NOT classified as a medical condition.
    grade: A
  - note: >
      The scope restriction is the operationally useful sentence and it is usually
      dropped: burn-out "refers specifically to phenomena in the occupational
      context and should not be applied to describe experiences in other areas of
      life". Exhaustion from parenting, caregiving, study or life in general is
      not burnout under this definition, whatever it is called colloquially.
      Neither is "I am tired this week".
    grade: A
  - note: >
      The population caveat on the prevalence review specifically: it studied
      PRACTICING PHYSICIANS, excluding physicians in training. Its definitional
      finding generalises -- the instrument-and-threshold problem is a property of
      how burnout is measured, not of doctors -- but the studies counted were not a
      general working population, and no figure from it applies to one.
    grade: A
claim: >
  Burnout prevalence figures are not comparable to each other and should not be
  quoted, and the word itself is narrower than its everyday use. Rotenstein et al.
  2018 (JAMA), a systematic review of 182 studies covering 109628 individuals in
  45 countries, found at least 142 unique definitions for meeting burnout or
  burnout-subscale criteria -- at least 47 distinct definitions of overall burnout
  prevalence among studies using Maslach Burnout Inventory-based instruments alone
  -- and reported overall burnout prevalence ranging from 0 percent to 80.5
  percent. The reviewers planned a meta-analysis and abandoned it, judging
  quantitative pooling inappropriate, and reported that associations between
  burnout and sex, age, geography, time, specialty and depressive symptoms could
  not be reliably determined because of the same inconsistencies. A 0-to-80.5
  percent range is not an imprecise estimate awaiting a bigger study; it is the
  signature of a construct where the choice of threshold determines the answer, so
  the correct handling is refusal rather than a range. Separately, the World
  Health Organization's ICD-11 entry defines burn-out as "a syndrome conceptualized
  as resulting from chronic workplace stress that has not been successfully
  managed", with three dimensions (energy depletion or exhaustion; increased mental
  distance from one's job, or negativism or cynicism about it; reduced professional
  efficacy), classifies it under factors influencing health status rather than as
  a medical condition, and states that it "refers specifically to phenomena in the
  occupational context and should not be applied to describe experiences in other
  areas of life". The population caveat: the prevalence review studied practicing
  physicians, so its definitional finding generalises but none of its figures do.
reasoning: >
  A generalist assistant that watches someone's workload will reach for the word
  burnout constantly, and both of the things it will want to do with it are
  unsupported: quote a prevalence, and apply the label outside work. This item
  blocks both from primary sources. Rotenstein et al. 2018 was selected because
  its finding is definitional rather than empirical, which makes it durable in a
  way a prevalence estimate never could be: the discovery that 182 studies used
  at least 142 different definitions and produced a range from zero to eighty
  percent will not be superseded by a bigger survey, because the problem is not
  sample size. The reviewers' decision to abandon a planned pooling is treated
  here as the strongest part of the evidence, on the same logic the warehouse
  applies elsewhere when a source declines to overstate itself -- a systematic
  review that refuses to pool has said something more reliable about its field
  than one that pools regardless. The ICD-11 entry is included as a second,
  independent source because it constrains the WORD rather than the number, and
  the occupational-context restriction is the sentence most often dropped in
  circulation, which makes it exactly the kind of scope loss this warehouse
  exists to catch. Graded at the top band for both the non-comparability finding
  and the ICD-11 definition, and at the bottom of the ladder for any specific
  figure, which is refused outright rather than hedged -- the same handling the
  warehouse gives a zombie statistic that cannot be repaired. Not flagged
  contested: no source located disputes either the review or the WHO entry, and
  the review's finding is a census of the literature rather than an estimate that
  could be argued with.
---

# mental-health/burnout-definition-bound-015

Two things about burnout, and both of them are refusals.

The first. A systematic review pulled together 182 studies covering more than a
hundred thousand people across 45 countries and asked a simple question: how
common is burnout? What it found was that the studies had used at least 142
different definitions of what counts as being burned out. Among just the studies
using instruments derived from the field's standard questionnaire, there were at
least 47 different definitions of overall prevalence.

The reported prevalence ranged from zero percent to eighty and a half percent.

The reviewers had planned to pool these into a single estimate. They did not,
judging that the variation in designs and ascertainment methods made pooling
inappropriate. They also reported that they could not reliably determine whether
burnout is associated with sex, age, geography, time period, specialty, or
depressive symptoms -- because the same definitional chaos wrecks those analyses
too.

A range from nothing to four fifths of the population is not a fuzzy estimate
that a larger study would sharpen. It is what you get when the answer depends on
where somebody drew a line on a questionnaire. So there is no figure to quote, no
midpoint to take, and no honest way to say what fraction of anybody is burned
out. The only defensible use of that literature is to point at the range and
explain why it exists.

The second refusal is about the word.

The World Health Organization's classification defines burn-out as a syndrome
conceptualised as resulting from chronic workplace stress that has not been
successfully managed, with three components: feeling depleted or exhausted;
becoming mentally distant from the job, or cynical and negative about it; and
reduced effectiveness at work. It is filed under factors influencing health
status rather than as an illness, and the WHO says explicitly that it is not
classified as a medical condition.

Then the sentence that almost never travels with the definition: burn-out refers
specifically to phenomena in the occupational context and should not be applied
to describe experiences in other areas of life.

That rules out most of how the word gets used. Exhaustion from caregiving, from
studying, from a hard stretch of life generally -- none of that is burnout under
the definition, whatever it feels like. And a tired week is not burnout either,
under any of the 142 definitions.

One caveat on the prevalence review itself: it studied practicing doctors, not a
general working population. The definitional finding travels, because the
problem is in how burnout is measured rather than in who was measured. The
numbers do not travel at all, and there were never any usable ones to begin with.

The practical upshot for anything watching someone's workload: describe what is
observable -- long hours, no recovery, the same complaint three weeks running --
and do not reach for a diagnosis-shaped word that the field cannot even count.
