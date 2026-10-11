---
# Collection sprint 2026-08-22 (owner-requested: warehouse returned ZERO coverage
# on stretching/recovery). Deep-research pass, 4 primary sources + adversarial
# verification. Fills GAPS gap-area 1 (acute static stretching -> subsequent
# strength/power). Rubric: exercise.rubric.md @performance-lit.
id: exercise/acute-static-stretch-force-deficit-021
domain: exercise
grade: B (duration threshold, isolated maximal strength); C (breadth across power/speed outcomes)
lane: "@performance-lit"
locale: universal
as_of: 2016-2024
contested: yes
sources:
  - "https://cdnsciencepub.com/doi/10.1139/apnm-2015-0235"  # Behm/Blazevich/Kay/McHugh 2016, Appl Physiol Nutr Metab 41(1):1-11, systematic review
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC11336295/"  # Warneke & Lohmann 2024, J Sport Health Sci 13(6):805-819, PMID 38735533, multilevel meta 83 studies/2012 participants/400+ ES
  - "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2019.01468/full"  # Chaabene/Behm/Negra/Granacher 2019, Front Physiol 10:1468, narrative synthesis with percentage bands
  - "https://pure.northampton.ac.uk/en/publications/no-effect-of-muscle-stretching-within-a-full-dynamic-warm-up-on-a/"  # Blazevich et al. 2018, Med Sci Sports Exerc 50(6):1258-1266, randomized crossover n=20, experimenter-blinded
  - "framework:GRADE -- two independent meta-level syntheses converge on the same duration threshold, but pooled methodological quality is LOW (mean PEDro 3.95/10 in Warneke 2024, authors self-rate certainty as low). Direction is well-supported; magnitude and outcome-breadth are not."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      Outcome-breadth caveat, and this is the load-bearing one. The popular
      framing is that static stretching before lifting blunts strength AND
      power. The 2024 multilevel meta separates the outcomes and only the
      first survives: isolated maximal strength ES -0.21 (p=0.003), but
      jump ES +0.15 (p=0.006, a trivial BENEFIT in adults), sprint/throwing
      ES +0.13 (p=0.20, not significant), and explosive strength / rate of
      force development ES -0.03 (p=0.86, nothing at all). So the deficit is
      demonstrated for slow maximal force tested in isolation, not for
      explosive or multi-joint whole-body tasks.
    grade: B
  - note: >
      Context caveat. Every meta-level percentage above is measured with
      stretching as an ISOLATED treatment immediately before an isolated
      test. When short static stretching is embedded inside a comprehensive
      warm-up that continues with dynamic and task-specific work, the effect
      disappears: Blazevich 2018 (randomized, crossover, experimenter-blinded,
      20 team-sport athletes, 9 body regions) found no effect of 5 s static,
      30 s static, or 5-repetition dynamic stretching on sprint, jump, or
      change-of-direction. Warneke 2024 concludes a rigorous prohibition on
      including stretching in a warm-up is without evidence.
    grade: B
  - note: >
      Population and quality limit. The pooled evidence is dominated by young
      adult males; the 2024 meta states outright that data in children and in
      females are insufficient and its results are not interpretable for those
      groups. Mean methodological quality is poor (PEDro 3.95/10) and the
      authors label the body of evidence low-certainty. The 480 s cumulative-
      volume threshold the same meta reports (ES -0.46, p=0.03) is described
      by its own authors as somewhat arbitrary. Treat the numbers as directional.
    grade: C
  - note: >
      Untested extrapolation, flagged so it is not silently assumed. No trial
      in this body of evidence tests what a multi-set heavy compound resistance
      SESSION does after stretching. All outcomes are single-effort tests
      (one maximal contraction, one jump, one sprint). Whether a pre-session
      static stretch changes reps-at-load across a working session is
      undetermined, not shown to be safe and not shown to be harmful.
    grade: D
claim: >
  Acute static stretching produces a DURATION-DEPENDENT force deficit, and the
  threshold is consistent across independent syntheses at roughly 60 seconds of
  accumulated stretch PER MUSCLE GROUP. Under 60 s per muscle group the effect
  is trivial and statistically indistinguishable from zero (approximately 1-2%
  performance change; pooled ES -0.13, p=0.20). At or over 60 s per muscle
  group the deficit becomes substantial (approximately 4-7.5%; pooled ES -0.84,
  p=0.004). Critically, the deficit is demonstrated for MAXIMAL STRENGTH TESTED
  IN ISOLATION and does NOT extend to jumping, sprinting, or rate of force
  development, which show trivial or null effects. When short-duration static
  stretching sits inside a full warm-up that continues with dynamic and
  task-specific work, no performance effect is detectable at all. Practical
  direction: a brief static hold (well under 60 s per muscle) placed inside a
  fuller warm-up carries no measurable performance cost; long static holds
  immediately before a maximal-strength effort do carry one and should be moved
  away from the pre-lift slot.
reasoning: >
  Two independent meta-level syntheses converge on the same duration threshold
  from different methods. Behm et al. 2016 (Appl Physiol Nutr Metab 41(1):1-11),
  the field's most-cited systematic review, reports a percent-change dose
  response of -1.1% under 60 s versus -4.6% at or above 60 s per muscle group
  (static stretching overall -3.7%, dynamic +1.3%, PNF -4.4%). Chaabene et al.
  2019 (Front Physiol 10:1468) restates the same split as 1-2% versus 4.0-7.5%.
  Warneke & Lohmann 2024 (J Sport Health Sci 13(6):805-819, PMID 38735533)
  re-derives it with a multilevel meta-analysis over 83 controlled pre-post
  studies, 2012 participants and more than 400 effect sizes, and lands on
  ES -0.13 (n.s.) under 60 s versus ES -0.84 (p=0.004) at or above 60 s.
  Agreement across a vote-counting review and a modern multilevel meta on the
  same threshold is what carries the confidence here. What the 2024 meta ALSO
  does is break the effect out by outcome, and that is where the popular version
  of this claim fails: jump performance shows a trivial positive effect
  (ES +0.15, p=0.006), sprint and throwing are null, and rate of force
  development is flatly null (ES -0.03, p=0.86). The deficit is therefore
  specific to slow maximal force production tested in isolation. Blazevich
  et al. 2018 (Med Sci Sports Exerc 50(6):1258-1266) supplies the ecological
  test: with 20 male team-sport athletes in a randomized, experimenter-blinded
  crossover across nine body regions, neither 5 s nor 30 s of static stretching
  nor 5 repetitions of dynamic stretching changed sprint, jump, or change-of-
  direction performance when performed inside a comprehensive warm-up. The
  contested flag is on OUTCOME BREADTH and MAGNITUDE, not on the duration
  direction: coaching practice widely asserts a general pre-lift power penalty
  that the outcome-stratified evidence does not support, and the underlying
  study quality is low (mean PEDro 3.95/10, authors' own certainty rating low).
---

# exercise/acute-static-stretch-force-deficit-021

Holding a static stretch before training does reduce force, but only under
conditions much narrower than the gym-floor version of the rule suggests. Two
things decide it: how long the hold is, and what you measure afterwards.

Duration is the clean part. Under about 60 seconds of total stretching per
muscle group, the measured effect is roughly one to two percent and is
statistically indistinguishable from no effect at all. At or beyond 60 seconds
per muscle group it becomes real -- roughly four to seven and a half percent,
a large pooled effect. Two independent syntheses built with different methods,
a widely cited 2016 systematic review and a 2024 multilevel meta-analysis over
83 studies and more than 2,000 participants, land on the same 60-second line.
That convergence is the strongest thing in this literature.

What you measure afterwards is where the popular version breaks. The 2024
meta-analysis splits the outcomes apart, and the deficit only appears in one of
them: maximal strength tested in isolation, one slow maximal contraction. Jump
performance actually came out marginally BETTER after stretching. Sprinting and
throwing showed nothing. Rate of force development -- explosive force, the exact
quality the popular claim says stretching destroys -- showed nothing whatsoever.
So "static stretching kills your power" is not what the pooled evidence says.

And the context matters as much as the dose. When short static holds are placed
inside a complete warm-up that then continues with dynamic movement and
task-specific work, the effect vanishes entirely: a randomized, blinded
crossover on 20 athletes across nine body regions found no difference at all
between 5 seconds of static stretching, 30 seconds of static stretching,
dynamic stretching, and no stretching.

Honest limits. The underlying study quality is poor -- mean methodological score
under 4 out of 10, and the meta's own authors call the certainty low. The
subject pool is overwhelmingly young adult men, and the 2024 authors state
explicitly that their results should not be read across to women or children.
And nobody has tested the thing an actual lifter cares about: whether a
pre-session stretch changes reps-at-load across a multi-set heavy compound
session. Every measured outcome here is a single effort, not a session.

## Applicability check (2026-08-22) -- NOT adopted, implication only

Checked against the owner's `files/program/prep.yaml` and `program.yaml`. **No
change was made to either file, and none is proposed here.** A program-design
consult is pending; what follows is what this item WOULD imply, for the owner
to decide on.

Current state: his `mat_prep` block is entirely dynamic/activation work (ankle
dorsiflexion primer, band knee-out, dynamic adductor sequence, pull/hinge prep)
with zero static holds. The one isometric in the prep chain (K4, 15 s x2) is an
adductor activation hold, not a stretch. So today there is nothing in the prep
chain that this item flags.

The live decision it bears on: **H1 (스탠딩 햄스트링 정적 스트레칭)** is defined
in the `drills` glossary with `default_phase: mat_prep`, is marked not
trim-eligible, and is queued for wave-2 restoration to the day blocks -- but it
currently renders on no day and it carries **no `hold_sec`**. This item says the
cost of a static hold is a function of total accumulated hold time per muscle
group, with a threshold around 60 seconds, and that below that threshold inside
a fuller warm-up the effect is not detectable. Implications, in the owner's
hands:

1. If H1 lands in `mat_prep`, its per-leg hold duration is the variable that
   decides whether it is free or costly. A short hold is in the no-detectable-
   effect zone; an accumulated hold approaching a minute per hamstring is not.
   `prep.yaml`'s own rule is that a `hold_sec` must come from the owner and must
   never be invented, so this is a decision to make, not a value to derive.
2. Placement helps here. `mat_prep` is the FIRST block, followed by
   `equipment_prep` and then the load ramp-up -- which is exactly the
   "embedded inside a comprehensive warm-up" condition under which the blinded
   crossover found no effect at all. Prep-block placement is more favourable
   than a hold taken immediately before a working set would be.
3. The day that matters most is 뒷B, where the RDL makes the hamstrings the
   working muscle rather than a bystander. If a duration cap is ever wanted, that
   is the day to argue it on. 앞A and 앞B (squat-dominant) are the weaker case.
4. What the item does NOT support: banning H1 from the prep on "static
   stretching kills your power" grounds. That framing did not survive
   verification -- the deficit is confined to isolated maximal strength and does
   not appear for jump, sprint or explosive force.
