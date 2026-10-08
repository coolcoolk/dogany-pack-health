---
# Collection sprint 2026-09-02. Naps were named in the GAPS.md sleep-recovery
# coverage list ("nap protocols"). Two meta-analyses of largely the same small
# literature give very different impressions, and the endpoint that matters for
# a lifter -- muscle force -- is the one with the clean null. The item is
# organised around that dissociation, deliberately mirroring
# exercise/recovery-modality-soreness-vs-performance-024, because it is the same
# perceived-versus-measured structure appearing inside the sleep domain.
# Rubric: sleep-recovery @clinical (VC-A).
# Source re-audit 2026-10-06: Mesas 2023 and Boukhris 2024 abstracts re-read
# (PubMed 36690376, 37700141). Mesas's 0.99 pool is itself the after-NORMAL-
# sleep pool, so the two reviews differ in granularity, not in restriction;
# note 2 now says so. Numbers and dose parameters verified unchanged.
id: sleep-recovery/nap-force-null-shuttle-signal-009
domain: sleep-recovery
grade: C (nap benefit on intermittent running and perceived fatigue); B (the null on muscle force); D (any transfer to strength training)
lane: "@clinical"
locale: universal
as_of: 2023-2024
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/36690376/"  # Mesas AE, Nunez de Arenas-Arroyo S, Martinez-Vizcaino V, Garrido-Miguel M, Fernandez-Rodriguez R, Bizzozero-Peroni B, Torres-Costoso AI. 2023, Br J Sports Med 57(7):417-426, doi 10.1136/bjsports-2022-106355, PROSPERO CRD42020212272 -- 22 RCTs, 291 male participants
  - "https://pubmed.ncbi.nlm.nih.gov/37700141/"  # Boukhris O, Trabelsi K, Suppiah H, Ammar A, Clark CCT, Jahrami H, Chtourou H, Driller M. 2024, Sports Med 54(2):323-345, doi 10.1007/s40279-023-01920-2, PMCID PMC10933197 -- 18 articles, napping after NORMAL night sleep
  - "exercise/recovery-modality-soreness-vs-performance-024"  # the same perceived-versus-measured dissociation, exercise domain
  - "exercise/small-n-culture-006"  # why a 291-participant literature spread over 22 trials is a structural warning, not a detail
  - "framework:GRADE -- downgraded for imprecision (291 participants across 22 trials, roughly 13 per trial), for inconsistency (I-squared 89.1 percent on the physical-performance pool), and for indirectness (the pooled physical-performance signal is dominated by one intermittent-running test, not by strength). The muscle-force NULL grades higher than the positive pool because it is the one endpoint where two independent syntheses agree and where the popular claim is loudest."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The endpoint split is the finding. The 2024 meta-analysis, restricted to
      napping after a NORMAL night of sleep, reports increases in highest
      distance (effect size 1.026) and total distance (0.737) and a decrease in
      fatigue index (0.839) on the 5-metre shuttle run test -- and NO effect on
      muscle force (effect size 0.175, p = 0.267). Alongside that: no effect in
      the one study measuring sprint performance, no effect in the two studies
      measuring the 30-second Wingate test, jump improved in two of three
      studies, repeated sprints in two of three, endurance in one of two. For
      someone whose training outcome is force production, the relevant endpoint is
      the one that came back null.
    grade: B
  - note: >
      Two meta-analyses, two very different impressions, largely one literature.
      The 2023 review reports a pooled physical-performance standardized mean
      difference of 0.99 (95 percent CI 0.67 to 1.31) -- a large effect, and
      that pool is itself for naps after a NORMAL night. The 2024 review, with
      the same normal-sleep restriction, concludes
      that no firm conclusions can be drawn about physical performance measures
      other than the shuttle run because of the limited number of studies. Both
      are competently executed. The difference is what got pooled: a single pooled
      number across heterogeneous tasks versus a task-by-task accounting. The
      task-by-task view is the honest one here, and it is far less impressive.
    grade: B
  - note: >
      Size and composition of the base. The 2023 meta-analysis covers 22 trials
      containing 291 participants in total -- roughly 13 per trial -- ALL MALE,
      aged 18 to 35, comprising 164 trained athletes and 127 physically active
      adults. Heterogeneity was I-squared 89.1 percent for physical performance
      and 89.5 percent for fatigue. This is precisely the small-n, high-scatter
      profile the exercise domain flags as a structural hazard, and it caps how
      much any pooled number here can be trusted.
    grade: B
  - note: >
      Independence caution, stated as fact rather than as accusation. The
      5-metre shuttle run test that carries the positive signal in the 2024
      meta-analysis is the outcome used in nap trials authored by members of the
      same research group who then authored that meta-analysis -- Boukhris and
      Chtourou appear both as primary-trial authors in this literature and as
      authors of the 2024 synthesis. That is a real concentration of a small
      field in one group and one test, and it should be weighed the way the
      exercise domain weighs funding and authorship concentration.
    grade: C
  - note: >
      The dose parameters, carried as reported and not independently verified.
      The 2023 review found benefits higher with nap durations between 30 and
      under 60 minutes and when more than one hour elapsed between waking from the
      nap and the test, with naps taken between 12:30 and 16:50 and 14:00 the most
      common time. The one-hour buffer matters practically: a nap ending shortly
      before a session may not have cleared sleep inertia.
    grade: C
  - note: >
      Where naps are on firmer ground is as partial compensation for a shortfall,
      not as an addition to adequate sleep. The 2023 review confirms the positive
      effects after PARTIAL SLEEP DEPRIVATION as well as after normal sleep, and
      that use case sits comfortably alongside item 004, which shows sleep loss to
      be the well-evidenced harm. A nap after a bad night is a different and
      better-supported proposition than a nap on top of a good one.
    grade: C
claim: >
  Daytime naps improve perceived fatigue and some intermittent-running measures,
  but the endpoint most relevant to strength training -- muscle force -- shows no
  effect, and the two meta-analyses of this literature give sharply different
  impressions of the same small evidence base. The 2023 systematic review of 22
  randomized trials reports a large pooled effect on physical performance
  (standardized mean difference 0.99, 95 percent CI 0.67 to 1.31, I-squared 89.1
  percent), on cognitive performance (0.69) and on perceived fatigue (-0.76), with
  benefits larger for naps of 30 to under 60 minutes and when more than an hour
  passed between waking and testing; its entire base is 291 MALE participants aged
  18 to 35 across those 22 trials, roughly 13 per trial. The 2024 meta-analysis,
  restricted to napping after a normal night of sleep, disaggregates by task and
  finds the benefit concentrated in the 5-metre shuttle run test (highest distance
  effect size 1.026, total distance 0.737, fatigue index 0.839) with NO effect on
  muscle force (0.175, p = 0.267), no effect on sprint performance in the single
  study measuring it, and no effect on the 30-second Wingate test in the two
  studies measuring it; its authors state that no firm conclusions can be drawn
  about physical performance measures beyond the shuttle run. Napping also has
  support as partial compensation after PARTIAL SLEEP DEPRIVATION, which is a
  better-founded use than adding a nap to already-adequate sleep. The operative
  rule: a nap reliably makes an athlete feel less tired and helps repeated-effort
  running; it has not been shown to increase force production, and for a lifter
  that is the endpoint in question.
reasoning: >
  Two syntheses published a year apart, drawing on largely the same trials, are
  the material here, and the discrepancy between them is instructive rather than
  disqualifying. Mesas et al. 2023 (Br J Sports Med 57(7):417-426, PROSPERO
  CRD42020212272) pooled 22 randomized controlled trials and reported a large
  standardized mean difference of 0.99 on physical performance. Boukhris et al.
  2024 (Sports Med 54(2):323-345) restricted to napping after a normal 7-9 hour
  night, assessed methodological quality with QualSyst (15 of 18 studies strong,
  3 moderate), and reported task by task -- at which point the large pooled effect
  resolves into a strong signal on one intermittent-running test and a null on
  muscle force. Both cannot be summarised as "naps improve performance" without
  losing the only distinction a strength trainee needs. The base is small and
  narrow: 291 participants, all male, 18 to 35, with heterogeneity near I-squared
  90 percent, which is the exact profile exercise/small-n-culture-006 and
  exercise/replication-power-crisis-005 were authored to make visible. There is
  also a genuine concentration issue worth recording without overstating it: the
  5-metre shuttle run trials that carry the positive signal come substantially
  from one research group whose members also authored the 2024 synthesis, so the
  positive endpoint and the analysts of that endpoint are not fully independent.
  Contested is set because the two meta-analyses genuinely diverge in the
  impression they leave, because the popular version of the claim asserts a
  performance benefit that the force endpoint does not support, and because this
  is the same perceived-versus-measured dissociation catalogued in
  exercise/recovery-modality-soreness-vs-performance-024 -- perceived fatigue
  moves by -0.76 while muscle force does not move at all. The one use that grades
  more comfortably is the nap as partial repayment after a short night, which is
  consistent with item 004 and does not require the extension literature's weaker
  premise.
---

# sleep-recovery/nap-force-null-shuttle-signal-009

Two research teams pooled essentially the same nap studies and came away sounding
like they were describing different worlds.

The first reported a large overall benefit to physical performance, a solid
benefit to cognitive performance, and a clear drop in perceived fatigue. Read that
summary and you would conclude that napping is one of the better-supported things
an athlete can do.

The second took the same territory, restricted itself to naps taken after a normal
night's sleep, and reported the results test by test instead of as one pooled
number. What emerges is much narrower. The benefit is concentrated in one specific
test -- a five-metre shuttle run, where distance covered improves substantially
and the fatigue index drops. Muscle force did not move at all. Sprint performance
did not move in the one study that measured it. The thirty-second Wingate did not
move in either of the two studies that measured it. Jump improved in two of three
studies, repeated sprints in two of three. Those authors state directly that no
firm conclusions can be drawn about physical performance measures beyond the
shuttle run.

Both analyses are competent. The difference is granularity, and the granular view
is the one that answers a lifter's question, because the endpoint a lifter cares
about is force, and force is the one that came back null.

It is worth knowing how small the underlying literature is. Twenty-two trials
sound like a lot until you notice they contain 291 people between them -- about
thirteen per study -- all male, all aged eighteen to thirty-five, with scatter
between studies running near ninety percent. This warehouse already carries items
explaining why a base shaped like that produces effect sizes that do not survive
contact with larger samples.

There is also a concentration worth naming plainly, without treating it as
misconduct. The shuttle-run trials that generate the positive signal come largely
from one research group, and members of that group also wrote the meta-analysis
that reports the signal. Small field, one favoured test, overlapping authorship.
That is a reason to hold the result loosely, in exactly the way this warehouse
holds funding and authorship concentration elsewhere.

If a nap is going to be used, the reported parameters are thirty to sixty minutes,
early afternoon, with at least an hour between waking up and doing anything that
matters -- that last one because waking straight into a session leaves you
climbing out of grogginess rather than benefiting from the nap.

And there is one use of napping that stands on firmer ground than any of the
above: napping to partially offset a short night, rather than napping on top of a
good one. That version lines up with the well-supported finding that losing sleep
carries a measured performance cost, and it does not depend on the shakier premise
that extra sleep buys extra performance.

The shape underneath all of this should look familiar. Perceived fatigue falls
substantially. Force production does not change. That is the same split this
warehouse documents across the recovery-modality literature, and it deserves the
same treatment here: report both, and never let the feeling stand in for the
measurement.
