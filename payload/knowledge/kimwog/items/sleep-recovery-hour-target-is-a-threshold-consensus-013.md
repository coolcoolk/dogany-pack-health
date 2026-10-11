---
# Collection sprint 2026-09-02. "You need 8 hours" is the most repeated number in
# this domain and almost nobody can say where it comes from. It comes from two
# different bodies using two different methods, producing two different SHAPES of
# recommendation (a threshold and a range), on a predominantly cross-sectional
# self-report evidence base. This item is deliberately built on the CONSENSUS
# PANEL'S OWN stated limitations, which are more candid than any secondary
# retelling. Note the domain-internal contrast this item creates with
# sleep-recovery/aasm-hierarchy-001: that item's whole point is that AASM
# systematic-review GUIDELINES are distinguished from expert-consensus
# documents -- and this is an expert-consensus document.
# Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/hour-target-is-a-threshold-consensus-013
domain: sleep-recovery
grade: B (that the recommendation is a consensus threshold, and what it says); D (that any specific hour count is an individual optimum)
lane: "@clinical"
locale: universal
as_of: 2015
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/26039963/"  # Watson NF et al (Consensus Conference Panel). 2015, Sleep 38(6):843-844, doi 10.5665/sleep.4716, PMCID PMC4434546 -- the AASM/SRS joint consensus recommendation
  - "https://pubmed.ncbi.nlm.nih.gov/26194576/"  # Watson NF et al (Consensus Conference Panel). 2015, Sleep 38(8):1161-1183, doi 10.5665/sleep.4886, PMCID PMC4507722 -- methodology and discussion, including the panel's own limitations section
  - "https://pubmed.ncbi.nlm.nih.gov/29073412/"  # Hirshkowitz M et al. 2015, Sleep Health 1(1):40-43, doi 10.1016/j.sleh.2014.12.010 -- National Sleep Foundation methodology and results summary; 18-member multidisciplinary panel (the separate body behind the 7-9 RANGE)
  - "https://pubmed.ncbi.nlm.nih.gov/29073398/"  # Hirshkowitz M et al. 2015, Sleep Health 1(4):233-243, doi 10.1016/j.sleh.2015.10.004 -- NSF updated recommendations, final report, recommendations for 9 age groups
  - "sleep-recovery/aasm-hierarchy-001"  # the distinction this item turns on: systematic-review guideline versus expert-consensus document
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # what IS demonstrated experimentally about short sleep
  - "sleep-recovery/regularity-vs-duration-014"  # the timing-consistency axis beside this duration floor; a second NSF consensus product (linked 2026-10-07)
  - "framework:GRADE -- this is not a GRADE guideline and must not be spoken as one. It is a modified RAND Appropriateness Method consensus over a systematic literature search, which is a legitimate but structurally different instrument: the output is panel appropriateness ratings, not certainty-of-evidence ratings with separated recommendation strength. The panel's own limitations section (predominantly cross-sectional designs, self-reported sleep with little psychometric validation, few experiments exceeding 7 days, unresolved reverse causation) is what caps any individual-optimum reading at the bottom of the ladder."
applicability:
  axes:
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The number is a FLOOR, not a target, and the shape matters more than the
      digit. The AASM and Sleep Research Society joint consensus states that
      adults should sleep 7 or more hours per night on a regular basis to promote
      optimal health. The methodology paper is explicit that the panel used a
      THRESHOLD model rather than a RANGE model, and deliberately set no upper
      limit -- the panel recorded consensus that the appropriateness of 9 or more
      hours could not be ascertained with certainty, and could not establish
      biological plausibility for harm from longer sleep. Anyone reporting an
      upper bound from this document is reporting something it does not contain.
    grade: B
  - note: >
      The familiar "7 to 9 hours" range is a DIFFERENT body's product. It comes
      from the National Sleep Foundation, which ran its own panel and published
      its own recommendations in Sleep Health, and which does express adult sleep
      need as a range. Two organisations, two methods, two shapes of answer,
      routinely quoted interchangeably. When precision matters, name which one is
      being cited.
    grade: B
  - note: >
      What the consensus rests on, in the panel's own words. Their limitations
      section names: predominantly cross-sectional observational designs that
      preclude causal claims, with concurrently measured sleep duration a poor
      predictor of conditions that develop over years; self-reported sleep subject
      to recall error, inconsistent measurement across studies, and mostly lacking
      formal psychometric validation; experimental studies few of which exceeded
      seven days, with small and unrepresentative samples and weak agreement
      between objective and self-reported sleep; and unresolved confounding as to
      whether short sleep causes ill health or reflects underlying disease. This
      is not an outside critique. It is the panel describing its own evidence.
    grade: B
  - note: >
      Individual variation is stated in the recommendation itself, not smuggled
      in afterwards. The consensus statement acknowledges that individual
      variability in sleep need is influenced by genetic, behavioural, medical and
      environmental factors, and that sleeping more than 9 hours regularly may be
      appropriate for young adults, for people recovering from sleep debt, and for
      people who are ill. A population floor is not a personal prescription, and
      the panel says so.
    grade: B
  - note: >
      Do not let this item be used to soften item 004. Nothing here weakens the
      experimental finding that sleep of 6 hours or less in 24 hours measurably
      degrades physical performance -- that comes from controlled experiments with
      objective endpoints, not from this epidemiology. The correct division: the
      hour TARGET is a soft population consensus on weak observational evidence;
      the performance COST of a real deficit is demonstrated experimentally. Being
      sceptical of the first is not licence to be sceptical of the second.
    grade: B
  - note: >
      NOT established anywhere in this item: any athlete-specific or
      lifter-specific hour requirement. The recommendation is a general adult
      health recommendation for ages 18 to 60. Claims that athletes need 9 or 10
      hours were not supported by any defensible source located in this sprint --
      see also item 005, where the sleep-extension literature that such claims
      lean on turns out to be seven small studies with two nulls.
    grade: D
claim: >
  The sleep-hours number everyone quotes is a population-level expert-consensus
  FLOOR built on predominantly cross-sectional self-report evidence, not an
  experimentally derived individual optimum, and the two commonly cited versions
  come from different organisations with different methods. The American Academy
  of Sleep Medicine and Sleep Research Society joint consensus states that adults
  should sleep 7 or more hours per night on a regular basis to promote optimal
  health. It was produced by a 15-member panel over three voting rounds using a
  modified RAND Appropriateness Method, from a systematic literature search that
  screened 5,314 publications down to a final evidence base of 311 across nine
  health categories. Crucially, the panel used a THRESHOLD rather than a RANGE
  model and set NO upper limit, recording that the appropriateness of 9 or more
  hours could not be ascertained with certainty. The widely quoted "7 to 9 hours"
  RANGE is a separate product of the National Sleep Foundation's own panel. The
  consensus panel's own stated limitations are the load-bearing part:
  predominantly cross-sectional designs that preclude causal inference,
  self-reported sleep measures mostly without formal psychometric validation, few
  experimental studies exceeding seven days, small and unrepresentative
  experimental samples, weak agreement between objective and self-reported sleep,
  and unresolved confounding as to whether short sleep causes ill health or
  reflects it. The statement itself acknowledges that individual sleep need varies
  with genetic, behavioural, medical and environmental factors. The operative rule:
  treat 7 hours as a soft population floor with a candid evidence base, never as a
  personal optimum or a scored target, and never quote an upper bound from a
  document that deliberately declined to set one.
reasoning: >
  This item exists because the domain's own authority anchor makes the
  distinction that the popular version of this claim erases.
  sleep-recovery/aasm-hierarchy-001 states that what lifts this field to a real
  top confidence tier is that AASM clinical practice GUIDELINES are grounded in
  systematic reviews with explicit benefit-harm weighing and are DISTINGUISHED
  from expert-consensus and position documents. The sleep-duration recommendation
  is an expert-consensus document. It is a good one -- a systematic literature
  search of 5,314 publications reduced to 311, a 15-member panel, three structured
  voting rounds under a modified RAND Appropriateness Method, and an unusually
  candid limitations discussion -- but the instrument produces panel
  appropriateness ratings, not GRADE certainty ratings with separately assigned
  recommendation strength, and it therefore does not inherit the standing of a
  guideline like Edinger et al. 2021. Graded at the trial band for the factual
  content (what the recommendation says, its threshold shape, its provenance),
  and at the bottom of the ladder for any reading of it as an individual optimum,
  because the panel itself reports that the underlying literature is predominantly
  cross-sectional, self-reported, short in experimental duration, and unresolved
  on reverse causation. Contested is set for two independent reasons. First, the
  two most-quoted versions of the number are structurally different objects -- an
  open-ended threshold from one body, a bounded range from another -- and they are
  used interchangeably in practice. Second, the popular framing inverts the
  document: a floor stated with explicit acknowledgement of individual variation
  is routinely retold as a precise universal requirement, and sometimes as a
  higher athlete-specific requirement for which no source located in this sprint
  provides support. The item deliberately fences itself off from
  sleep-recovery/sleep-loss-performance-decrement-004, because scepticism about a
  soft epidemiological target must not be allowed to leak into scepticism about a
  demonstrated experimental harm; those rest on entirely different evidence and
  deserve entirely different confidence.
---

# sleep-recovery/hour-target-is-a-threshold-consensus-013

Ask where "you need eight hours" comes from and the answer is more interesting
than the number.

The sleep field's two main American bodies issued a joint consensus statement in
2015 saying that adults should sleep seven or more hours per night on a regular
basis to promote optimal health. Note the shape of that sentence. Seven or more.
It is a floor with nothing above it, and the panel chose that shape deliberately
-- their methodology paper says they used a threshold model rather than a range,
and they explicitly declined to set an upper limit because they could not
establish that sleeping longer was harmful and could not settle whether nine or
more hours was appropriate.

So the version most people carry around -- "seven to nine hours" -- is not that
statement. It is a separate recommendation from the National Sleep Foundation,
produced by a different panel with a different method, which does express adult
sleep need as a range. Two organisations, two answers of different shapes, quoted
as if they were one.

Now the part that decides how much weight the number can carry. The consensus
panel wrote an unusually honest limitations section, and it says the evidence
underneath is predominantly cross-sectional -- snapshots that cannot establish
which way causation runs. Sleep was mostly self-reported, using measures that in
most studies were never formally validated. The experimental studies, the ones
that could establish causation, were few and rarely ran longer than a week, on
small and unrepresentative samples. And objective and self-reported sleep agree
with each other only weakly. The panel also flagged the confound that will not go
away: short sleep may cause ill health, or ill health may cause short sleep.

That is the panel describing its own evidence base, not a critic attacking it.

The recommendation itself also concedes what the retellings drop: individual sleep
need varies with genetics, behaviour, medical conditions and environment, and
regularly sleeping more than nine hours may be entirely appropriate for young
adults, for someone repaying a deficit, or for someone who is ill.

Which leaves a sensible way to hold the number. Seven hours is a soft population
floor, arrived at by a careful panel reading a weak literature honestly. It is not
a personal optimum, it is not a score to hit, and it has no ceiling attached to it.

One thing this must not be used to do. It does not soften the finding that real
sleep loss measurably costs performance. That result comes from controlled
experiments with objective endpoints, and it belongs to a different and much
stronger evidence base than the epidemiology behind the hour target. Doubting a
population number is not permission to doubt a measured effect.

And nothing here supports the frequent claim that athletes specifically need nine
or ten hours. This recommendation is a general adult health floor for ages
eighteen to sixty. The athlete-specific version leans on the sleep-extension
literature, which this domain documents separately as seven small studies, three
of them at high risk of bias, with two outright nulls in the set.
