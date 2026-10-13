---
# Collection sprint 2026-09-02 (mental-health lane expansion). The most directly
# operational item in the lane for this consumer: a life agent sees sleep,
# activity, location and phone-use data, which is exactly the feature set the
# digital-phenotyping literature uses to try to infer mood. This item records
# what that literature has and has not established. The authors' own verdict --
# "purely as a starting point for hypothesis generation" -- is the ceiling, and
# it is quoted rather than paraphrased upward. Partner to sleep-recovery's
# tracker-accuracy item and to mental-health item 012.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/passive-sensing-hypothesis-generating-013
domain: mental-health
grade: "C (that sleep, physical activity, location and phone-use features show consistent bivariate associations with depression across studies); D (any claim that passively sensed data detects, tracks or predicts an individual's mood state)"
lane: "@clinical"
locale: universal
as_of: 2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/35017634/"  # De Angel V, Lewis S, White K, Oetzmann C, Leightley D, Oprea E, Lavelle G, Matcham F, Pace A, Mohr DC, Dobson R, Hotopf M. 2022, NPJ Digit Med 5(1):3, doi 10.1038/s41746-021-00548-8, PMCID PMC8752685 -- systematic review of methods, 51 studies, databases searched January 2007 to November 2019
  - "sleep-recovery/tracker-accuracy-003"  # the same warehouse's finding on device measurement ACCURACY; this item is about what can be INFERRED from those measurements
  - "sleep-recovery/subjective-monitoring-vs-objective-markers-011"  # the physical-recovery analogue -- the cheap subjective question outperformed the expensive sensor there too
  - "mental-health/group-to-individual-nongeneralizability-012"  # why a population-level association between a sensor feature and mood does not license an individual-level inference
  - "framework:GRADE -- a systematic review of METHODS rather than of effects. It cannot support a pooled estimate and explicitly does not attempt one; the reviewers state that small samples, short follow-up and variable reporting limit the interpretability of pooled results. Graded accordingly, and the reviewers' own ceiling on interpretation is adopted verbatim rather than softened."
refraction_notes:
  - note: >
      What was actually found, stated at the reviewers' own level. Across 51
      studies linking depression to objective behavioural data from smartphone
      and wearable sensors, bivariate analyses showed CONSISTENCY in
      statistically significant associations between depression and digital
      features drawn from sleep, physical activity, location and phone-use data.
      Machine-learning models found predictive value in aggregated features. That
      is the positive result and it is real.
    grade: C
  - note: >
      The ceiling the reviewers put on their own result, and it is quoted rather
      than paraphrased: "Given the pitfalls in the combined literature, these
      results should be taken purely as a starting point for hypothesis
      generation." A systematic review that declines to license its own findings
      as more than hypothesis generation has stated the maximum, and no downstream
      user may exceed it.
    grade: A
  - note: >
      The pitfalls, named. The reviewers found threats to reproducibility and
      transparency arising from failure to describe recruitment strategies, sample
      information, feature construction, and the determination and handling of
      missing data. The literature is characterised by SMALL SAMPLE SIZES, SHORT
      FOLLOW-UP, and great variability in reporting quality, which together limit
      the interpretability of any pooled result. Missing-data handling matters
      unusually much here: sensor data goes missing for reasons that are
      themselves behavioural, so the gaps are not random.
    grade: A
  - note: >
      Feature multiplicity is the specific statistical hazard. These studies
      construct large numbers of candidate features from a continuous data stream
      and test them, and the reviewers explicitly recommend reporting potential
      bias in studies with numerous features. A "consistent significant
      association" found across a literature that tests many features per study
      without correction is weaker than the same phrase would imply elsewhere.
    grade: A
  - note: >
      The direction of the association is not established as a direction of
      inference. That someone's sleep and movement change when they are depressed
      is not in serious doubt and is close to definitional. That an observed
      change in sleep and movement therefore indicates a mood state is the
      converse, and it is the inference a tracking system will be tempted to make.
      Nothing in this literature supports the converse for an individual, and item
      012 gives the reason a population-level association would not license it
      even if the association were strong.
    grade: D
  - note: >
      Practical translation, which is a refusal rather than a technique: observed
      behavioural data may be used to ASK, never to CONCLUDE. Noting out loud that
      the calendar has been heavy and sleep short, and asking how the person is
      finding it, is supported. Telling them what their data implies about their
      mood is not, at any confidence.
    grade: C
claim: >
  Passively sensed behavioural data does not tell you how someone feels, and the
  most systematic review of the field says so in its own words. De Angel et al.
  2022 (npj Digital Medicine, 51 studies, searched January 2007 to November 2019)
  synthesised the methods of studies linking depression to objective behavioural
  data from smartphone and wearable sensors. Bivariate analyses showed consistency
  in statistically significant associations between depression and digital
  features derived from sleep, physical activity, location and phone-use data, and
  machine-learning models found predictive value in aggregated features. But the
  reviewers found threats to reproducibility and transparency arising from failure
  to report recruitment, sample information, feature construction and missing-data
  handling; characterised the literature as having small samples, short follow-up
  and highly variable reporting quality that limits the interpretability of pooled
  results; and concluded that the results "should be taken purely as a starting
  point for hypothesis generation". Two further cautions: the studies construct
  and test many candidate features from a continuous data stream, so a
  "consistent significant association" is weaker than it sounds; and sensor data
  goes missing for behavioural reasons, so the gaps are not random. The direction
  that is nearly definitional -- that sleep and movement change during a
  depressive episode -- does not license the converse inference that observed
  changes in sleep and movement indicate a mood state, which is precisely the
  inference a tracking system will reach for. Operative rule: observed behavioural
  data may be used to ASK, never to CONCLUDE.
reasoning: >
  This is the item with the shortest distance between the literature and the
  consumer. A generalist life agent holds sleep, movement, location and calendar
  data on one person, which is very close to the exact feature set this
  literature builds mood inferences from, so the question "can this data tell me
  how they are doing" is not hypothetical here -- it is the default temptation.
  De Angel et al. 2022 was selected because it is a review of METHODS rather than
  of effects, which makes it the right instrument for this question: the useful
  answer is not a pooled effect size but an assessment of whether the field's
  designs and reporting can support any inference at all, and the reviewers'
  verdict is that they support hypothesis generation and nothing beyond it. That
  verdict is adopted as the ceiling verbatim rather than softened, on the same
  discipline the sleep domain applied when it declined to convert a
  searched-and-unfound readiness-score validation into either a positive or a
  negative claim. Graded at the observational band for the existence of the
  bivariate associations, which are consistent across studies and are the
  literature's genuine positive finding, and at the practitioner floor for any
  detection, tracking or prediction claim about an individual. Item 012 is cited
  as a dependency because it supplies the independent reason a population-level
  association would not transfer to one person even if this literature were
  methodologically sound. Not flagged contested: no source located disputes the
  review, and its limitations are its own stated assessment of its field rather
  than an external critique.
---

# mental-health/passive-sensing-hypothesis-generating-013

A system that can see someone's sleep, their movement, where they went and how
much they used their phone is holding almost exactly the feature set that
researchers use to try to infer mood from sensors. So it is worth knowing what
that research has actually produced.

The most systematic look at the field covered 51 studies. The positive finding is
real: across those studies, features built from sleep, physical activity, location
and phone use were consistently and significantly associated with depression, and
models built on aggregated features had some predictive value.

Then the reviewers say what they think that is worth. Their words: the results
should be taken purely as a starting point for hypothesis generation.

That is a systematic review declining to let its own field's findings be used for
anything. It is the ceiling, and nothing downstream is entitled to exceed it.

The reasons are specific. Studies routinely failed to describe how they recruited,
who was in the sample, how features were constructed, and how missing data was
determined and handled. Samples are small. Follow-up is short. Reporting quality
varies enormously. That combination makes pooling uninterpretable, which is why
the review reports methods rather than a pooled effect.

Two of those problems bite harder here than they would elsewhere.

Missing data in sensor studies is not random. A phone stops reporting because it
was off, or flat, or left at home, or because the person stopped carrying it --
and every one of those is itself a behaviour that may be related to the thing
being measured. Dropping the gaps quietly is not a neutral choice.

And feature multiplicity. A continuous data stream can be sliced into an
essentially unlimited number of candidate features, and studies test many of them.
The reviewers specifically recommend reporting potential bias in studies with
numerous features. A phrase like "consistently significantly associated" carries
less weight in a literature built that way than the same phrase carries in a
literature testing one prespecified hypothesis.

The deepest problem is not statistical, though. It is directional.

That someone sleeps differently and moves less during a depressive episode is
barely a finding; it is close to part of the description. What a tracking system
wants is the reverse: this person slept badly and went out less, therefore
something is wrong. That converse is not established by anything in this
literature, and the warehouse's separate item on group-to-individual transfer
gives the reason it would not follow even if the population association were
strong.

Which leaves one honest use, and it is a small one. Behavioural data can be a
reason to ask. Noticing out loud that the week has been heavy and sleep has been
short, and then asking how it is landing, is supported and useful. Telling
somebody what their data says about their mood is not supported at any level of
confidence, and the sensors do not become more entitled to that conclusion by
getting more numerous.
