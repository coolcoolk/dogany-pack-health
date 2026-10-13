---
# Collection sprint 2026-08-22. Fills GAPS gap-area 2 (dynamic stretching /
# mobility work -> same-day performance). Companion to
# exercise/acute-static-stretch-force-deficit-021 (the static side of the same
# question) and exercise/warmup-load-rampup-progression-018 (the LOAD ramp,
# which is a different lever from the movement prep covered here).
# Rubric: exercise.rubric.md @performance-lit.
id: exercise/dynamic-warmup-same-day-performance-022
domain: exercise
grade: B (general warm-up raises subsequent performance); C (independent increment attributable to the stretching component)
lane: "@performance-lit"
locale: universal
as_of: 2010-2024
contested: yes
sources:
  - "https://research.monash.edu/en/publications/effects-of-warming-up-on-physical-performance-a-systematic-review/"  # Fradkin/Zazryn/Smoliga 2010, J Strength Cond Res 24(1):140-148, DOI 10.1519/JSC.0b013e3181c643a0, 32 high-quality studies
  - "https://pubmed.ncbi.nlm.nih.gov/29063454/"  # Opplert & Babault 2018, Sports Med 48(2):299-325, systematic analysis of dynamic-stretching literature
  - "https://cdnsciencepub.com/doi/10.1139/apnm-2015-0235"  # Behm/Blazevich/Kay/McHugh 2016, Appl Physiol Nutr Metab 41(1):1-11, dynamic stretching +1.3%
  - "https://pure.northampton.ac.uk/en/publications/no-effect-of-muscle-stretching-within-a-full-dynamic-warm-up-on-a/"  # Blazevich et al. 2018, Med Sci Sports Exerc 50(6):1258-1266, the null within-full-warm-up crossover
  - "exercise/acute-static-stretch-force-deficit-021"  # within-warehouse cross-ref: the static counterpart, same evidence base, same context caveat
  - "framework:GRADE -- the warm-up-improves-performance direction rests on a VOTE-COUNTING review (proportion of criteria improved), not a pooled effect size, and its own authors flag a shortage of well-conducted RCTs. The dynamic-stretch-specific increment rests on a narrative synthesis plus a small percent-change figure, and is contradicted by the one blinded crossover that isolated it."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The headline warm-up statistic is weaker than it reads. Fradkin 2010 is
      cited as showing warm-up improved performance in 79% of the criteria
      examined across 32 studies. That is a VOTE COUNT of significant results,
      not a pooled effect size with a confidence interval, and the authors
      themselves note there were few well-conducted randomized controlled
      trials. Vote-counting is biased toward positive findings. The direction
      is safe; a specific magnitude is not available from this source.
    grade: C
  - note: >
      The dynamic-stretch increment does NOT survive isolation. Behm 2016
      reports dynamic stretching at +1.3% and Opplert & Babault 2018 report
      broadly positive effects on ROM, force, power, sprint and jump -- but
      both bodies compare dynamic stretching against a passive or minimal
      control. When Blazevich 2018 held the rest of the warm-up constant and
      varied only the stretching component in a blinded crossover, dynamic
      stretching produced no measurable benefit over no stretching. The most
      defensible reading is that most of the benefit belongs to the warm-up
      as a whole (temperature, blood flow, task rehearsal), and the stretching
      modality label is a small and possibly null part of it.
    grade: C
  - note: >
      Mechanism is under-tested. The physiological attribution usually offered
      (raised muscle temperature, faster cross-bridge kinetics, post-activation
      potentiation, task rehearsal) is plausible and consistent with the data
      but is not what the performance trials measured. Do not present the
      mechanism as an established finding.
    grade: D
claim: >
  A warm-up that raises muscle temperature and rehearses the coming movement
  improves subsequent performance -- this is the well-supported direction and
  there is little evidence any adequate warm-up is detrimental. The specific
  contribution of the STRETCHING component within that warm-up is small and
  contested: dynamic stretching outperforms static stretching in head-to-head
  syntheses (roughly +1.3% versus -3.7% in the largest systematic review) and
  is broadly reported to improve ROM, force, power, sprint and jump when
  compared against passive control, BUT when the rest of the warm-up is held
  constant and only the stretching modality is varied in a blinded crossover,
  neither dynamic nor short static stretching changes sprint, jump, or
  change-of-direction performance. The defensible practical position: the
  warm-up as a whole earns its place; the choice between dynamic and short
  static within it is a preference and ROM decision, not a performance lever.
  Only LONG static holds carry a documented performance cost (see item 021).
reasoning: >
  Fradkin, Zazryn & Smoliga 2010 (J Strength Cond Res 24(1):140-148) reviewed 32
  studies of uniformly high methodological quality (mean 7.6/10) and found
  warm-up improved performance in 79% of the criteria examined, with little
  evidence of harm. That establishes the direction, but it is a vote count of
  significant results rather than a pooled estimate, and the authors flag the
  shortage of well-conducted RCTs -- which is why this does not sit at the top
  of the ladder despite being near-universally accepted practice. For the
  stretching component specifically, Behm et al. 2016 (Appl Physiol Nutr Metab
  41(1):1-11) reports dynamic stretching at +1.3% against static stretching at
  -3.7%, and Opplert & Babault 2018 (Sports Med 48(2):299-325) find substantial
  evidence for positive dynamic-stretching effects on ROM and on subsequent
  force, power, sprint and jump. Both, however, compare against passive or
  minimal control. The decisive test is Blazevich et al. 2018 (Med Sci Sports
  Exerc 50(6):1258-1266): a randomized, experimenter-blinded crossover in 20
  team-sport athletes that held a comprehensive warm-up constant and varied ONLY
  the stretch condition (5 s static, 30 s static, 5-repetition dynamic, or none)
  across nine body regions -- and found no effect of stretch condition on any
  test. Read together, the honest synthesis is that the warm-up carries the
  benefit and the stretching modality inside it is close to interchangeable at
  short durations. Contested flag is set because the practitioner consensus
  ("dynamic stretching primes the muscle and improves output") is stated far
  more strongly than the isolated evidence supports.
---

# exercise/dynamic-warmup-same-day-performance-022

Two questions get collapsed into one here, and they have different answers.

Does warming up help? Yes, and that is not seriously in dispute. A review of 32
high-quality studies found performance improved in roughly four out of five of
the criteria examined, with essentially no signal that an adequate warm-up hurts
anything. The caveat is that this is a count of how many studies found a
significant improvement, not a pooled effect size -- so "warming up helps" is
well-directed but does not come with a trustworthy number attached, and the
review's own authors point out how few properly randomized trials existed.

Does the stretching part of the warm-up help, on top of the warm-up itself?
That is much shakier. Compared head-to-head against static stretching, dynamic
stretching looks clearly better -- about +1.3% versus -3.7% in the largest
systematic review -- and the dynamic-stretching literature broadly reports gains
in range of motion, force, power, sprint and jump. But almost all of those
comparisons are against doing nothing. The one study that held the whole warm-up
constant and changed only the stretch condition, blinded, across nine body
regions in 20 athletes, found no difference between dynamic stretching, short
static stretching, and no stretching at all.

The practical read: keep the warm-up, and treat the choice of stretch style
inside it as a range-of-motion and preference decision rather than a performance
lever. The one thing that does have a documented cost is long static holds
immediately before a maximal strength effort, and that is covered separately.

Honest limit: the usual mechanistic story -- warmer muscle, faster cross-bridge
cycling, potentiation, movement rehearsal -- is plausible and consistent, but the
performance trials did not measure it. It is an explanation offered for the
result, not itself a finding.

## Applicability check (2026-08-22) -- NOT adopted, implication only

Checked against `files/program/prep.yaml`. **Nothing was changed and nothing is
proposed.** Implication only, for the owner's pending program-design consult.

Current state: the `mat_prep` block on every day is dynamic/activation work
already (K6 ankle dorsiflexion and foot-alignment primer, K2 band knee-out, K5
dynamic adductor sequence of cossack squat plus lateral lunge, U2 pull/hinge
prep), followed by `equipment_prep` light-load specific primers and then the
load ramp-up. That is structurally a comprehensive warm-up, which is the exact
condition under which this item's evidence applies.

What it would imply:

1. The prep block earns its slot as a warm-up. That part is well supported and
   nothing here argues for cutting it.
2. It does NOT support the argument "these drills are dynamic, therefore they
   are priming output." The measured increment attributable to the stretching
   modality specifically is small and vanishes when the rest of the warm-up is
   held constant. If a rationale document anywhere in the program claims a
   performance benefit from the drills being dynamic, that rationale is stronger
   than the evidence.
3. Symmetrically, it removes the performance argument for keeping H1 (static)
   out of `mat_prep` on the grounds that dynamic is better. At short durations
   the two are close to interchangeable for performance. The case for or against
   H1 should be argued on range-of-motion goals and on the prep block's time
   budget -- not on a performance-lever claim in either direction.
4. Trim decisions (`prep.yaml` marks some drills trim-eligible) therefore have
   no evidence-based ordering from this item. It cannot tell the owner which
   drill to cut first.
