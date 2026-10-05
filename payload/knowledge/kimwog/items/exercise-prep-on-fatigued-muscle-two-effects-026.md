---
# Collection sprint 2026-08-22. THIS is the item that answers the originating
# owner question the warehouse could not answer (2026-08-21, logged in
# GAPS-instance.md): can mat-prep work performed on a muscle still fatigued
# from the previous session help? The owner himself split it into two effects
# and rejected the strong version -- "프렙에서 푼다고 피로도가 모두 회복되는건
# 아니야.. 그래도 당일 운동 혹은 근육의 회복속도 증진에 도움이 되겠지."
# This item grades those two effects SEPARATELY, because the evidence states
# for them are different. Rubric: exercise.rubric.md @clinical-physio.
id: exercise/prep-on-fatigued-muscle-two-effects-026
domain: exercise
grade: C (same-day performance effect, indirect); C (small reduction in LATER soreness from prior warm-up); D (recovery-rate acceleration -- unsupported, direction is negative)
lane: "@clinical-physio"
locale: universal
as_of: 2007-2021
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/17535144/"  # Law & Herbert 2007, Aust J Physiother 53(2):91-95, RCT n=52 factorial, warm-up vs cool-down on later DOMS
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC3588693/"  # Olsen/Sjohaug/van Beekvelt/Mork 2012, J Hum Kinet 35:59-68, RCT n=36, warm-up prevents soreness but NOT force loss
  - "https://pubmed.ncbi.nlm.nih.gov/29663142/"  # Van Hooren & Peake 2018, Sports Med 48(7):1575-1595, active cool-down ineffective for same-day and next-day performance
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC8133317/"  # Afonso et al. 2021, Front Physiol 12:677581, post-exercise stretching: no effect on strength recovery
  - "exercise/dynamic-warmup-same-day-performance-022"  # within-warehouse cross-ref: the same-day performance leg of this question
  - "exercise/acute-static-stretch-force-deficit-021"  # within-warehouse cross-ref: why a LONG static hold on an already-fatigued muscle is the one prep choice with a documented cost
  - "exercise/recovery-modality-soreness-vs-performance-024"  # within-warehouse cross-ref: the soreness-vs-performance split this item applies
  - "framework:GRADE -- the DIRECT question (prep performed on a muscle that is ALREADY fatigued from a previous session) has NO trial. Every source here is adjacent: warm-up before a damaging bout, or a recovery intervention after one. The item is therefore an explicitly assembled inference from adjacent evidence, and is graded and flagged as such rather than presented as a measured finding."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The honest headline: NO study tests the actual question. There is no
      trial of a warm-up or mobility routine performed on a muscle carrying
      residual fatigue from a previous session, measuring either that day's
      output or the rate at which the fatigue clears. Everything below is
      assembled from adjacent designs. Anyone presenting a confident answer to
      this question -- in either direction -- is extrapolating.
    grade: C
  - note: >
      The two effects the owner separated do NOT have the same evidence
      state, and this is the item's load-bearing point. (a) SAME-DAY OUTPUT:
      indirectly supported. A warm-up improves subsequent performance
      generally, and nothing in the literature suggests a fatigued muscle is
      an exception, but no trial has tested it in the fatigued condition.
      (b) RECOVERY-RATE ACCELERATION: unsupported, and the closest direct
      evidence points the other way. Olsen 2012 found that a 20-minute
      moderate aerobic warm-up before the damaging bout prevented soreness at
      the central muscle belly but did NOT prevent the 10-20% force loss on
      days 2-3. Movement helped how the muscle FELT and did nothing for what
      it could DO. That is the same dissociation catalogued in
      exercise/recovery-modality-soreness-vs-performance-024.
    grade: C
  - note: >
      Prior warm-up does buy a small, real reduction in LATER soreness, and
      the size is worth naming honestly. Law & Herbert 2007 (randomized,
      factorial, n=52, downhill-treadmill damage protocol) found a 10-minute
      warm-up before the bout reduced soreness at 48 h by 13 mm on a 100 mm
      visual analogue scale (95% CI 2 to 24 mm) -- the interval only just
      excludes zero and its lower bound is trivially small. The same trial
      found the cool-down AFTER the bout did nothing at all (0 mm, 95% CI -11
      to 11). So the timing asymmetry is real: prep before beats work after.
      But this is soreness, not capacity, and 13 mm on 100 is modest.
    grade: C
  - note: >
      One prep choice does carry a documented cost, and it is the one bearing
      on a live decision. Prolonged static stretching produces an acute force
      deficit (see exercise/acute-static-stretch-force-deficit-021, threshold
      around 60 s per muscle group). Applying a LONG static hold to a muscle
      that is already carrying residual fatigue stacks a stretch-induced
      deficit on top of an existing one. The interaction has not been directly
      tested, so this is a caution rather than a finding -- but it is the one
      direction where the evidence argues against the intuition that
      "loosening it up" helps. Short holds well under the threshold, embedded
      in a fuller warm-up, do not carry this cost.
    grade: C
  - note: >
      Why this failed as a warehouse query on 2026-08-21 and what it implies.
      The question was routed at the muscle/fatigue level and the warehouse
      had nothing at any grade on stretching, DOMS, or recovery -- and the
      miss was never logged to GAPS-instance.md, which is exactly the failure
      mode GAPS.md warns about (the rest-interval hole in item 017 was
      unlogged the same way). The miss is now recorded retrospectively.
    grade: D
claim: >
  Split the question, because the two halves have different evidence states.
  (a) DOES PREP HELP THAT DAY'S SESSION on a muscle still fatigued from the
  previous one? Probably yes, but only indirectly supported: warming up improves
  subsequent performance in general and there is no reason or evidence to think
  a fatigued muscle is exempt -- however, no trial has tested a warm-up on an
  already-fatigued muscle, so this is inference, not measurement. (b) DOES PREP
  SPEED UP THE MUSCLE'S RECOVERY? Not supported, and the nearest direct evidence
  points against it. A 20-minute moderate aerobic warm-up performed BEFORE a
  damaging bout prevented soreness at the central muscle belly but did NOT
  prevent the 10-20% force loss measured on days 2-3; movement changed the
  sensation and not the capacity. A separate randomized trial found a 10-minute
  warm-up before a damaging bout reduced 48 h soreness by 13 mm on a 100 mm
  scale (95% CI 2 to 24), while a cool-down after the bout did nothing (0 mm,
  95% CI -11 to 11). No recovery modality studied -- including movement,
  stretching and active cool-down -- has been shown to accelerate the return of
  force. One caution runs the other way: prolonged static stretching produces
  its own acute force deficit, so a long static hold applied to an
  already-fatigued muscle is the single prep choice with a plausible cost
  rather than a benefit. Net: prep is worth doing for the session in front of
  you and for a modest reduction in later soreness. It is not a recovery
  accelerator, and the owner's own framing -- that prep does not restore
  accumulated fatigue -- is the correct half of his split.
reasoning: >
  The direct question has no trial, so this item is explicitly assembled from
  adjacent designs and graded down accordingly. On the same-day leg, the support
  is the general warm-up literature carried in
  exercise/dynamic-warmup-same-day-performance-022 (Fradkin 2010: warm-up
  improved performance in 79% of criteria across 32 studies), which never tested
  a pre-fatigued muscle -- the inference is that the mechanisms usually invoked
  (temperature, blood flow, movement rehearsal) are not obviously abolished by
  residual fatigue, but that is reasoning, not data. On the recovery leg the
  evidence is better and more negative. Olsen et al. 2012 (J Hum Kinet 35:59-68,
  n=36 randomized to warm-up, cool-down or control around a front-lunge damage
  protocol) is the cleanest single result: 20 minutes of moderate cycling before
  the bout raised pressure-pain thresholds at the central muscle belly on days
  2-3 relative to control, but every group lost roughly 10-20% of force on those
  same days and neither warm-up nor cool-down prevented it. Law & Herbert 2007
  (Aust J Physiother 53(2):91-95, randomized factorial, n=52, backwards downhill
  treadmill walking) independently reproduces the sensation-only pattern and adds
  the timing asymmetry: warm-up before the bout reduced 48 h soreness by 13 mm
  on a 100 mm VAS (95% CI 2 to 24 mm), cool-down after produced 0 mm (95% CI -11
  to 11). Both effects are on soreness. Neither trial shows a capacity effect.
  That is the same dissociation established at meta-analytic scale in
  exercise/recovery-modality-soreness-vs-performance-024, where an active
  cool-down is largely ineffective for same-day and next-day performance
  (Van Hooren & Peake 2018) and post-exercise stretching has no effect on
  strength recovery (Afonso 2021). The one asymmetric caution comes from
  exercise/acute-static-stretch-force-deficit-021: prolonged static stretching
  causes its own acute force deficit, so of all prep choices the long static
  hold is the one with a documented downside when the muscle is already
  compromised -- untested in combination, hence a caution, not a finding.
  Contested flag is set because the practitioner intuition that mobility work
  "flushes out" or "speeds up" recovery is widespread and the two directly
  relevant randomized trials both fail to find any capacity effect.
---

# exercise/prep-on-fatigued-muscle-two-effects-026

The question was posed correctly in the first place: prep does not undo
accumulated fatigue, but might it still help that day's session, or help the
muscle recover faster? Those are two separate claims, and the evidence treats
them very differently.

Start with the part nobody has actually studied. There is no trial of a warm-up
or mobility routine performed on a muscle that is already carrying fatigue from
a previous session, measuring either that day's output or the speed at which the
fatigue clears. Everything below is assembled from studies that are adjacent to
the question, not on it. Anyone answering this confidently in either direction is
extrapolating, including this item.

**Same-day output: probably yes, indirectly.** Warming up improves subsequent
performance in general, and there is no mechanism or finding suggesting a tired
muscle is an exception to that. But the inference is doing the work here, not a
measurement.

**Recovery rate: no, and the closest evidence points the other way.** In a
randomized trial, 20 minutes of moderate cycling before a damaging leg session
did make the muscle less tender in the days after -- and did nothing at all about
the force loss. Every group, warmed up or not, lost roughly 10 to 20 percent of
their force on days two and three. A second randomized trial found the same
shape: a 10-minute warm-up beforehand cut soreness at 48 hours by 13 millimetres
on a 100-millimetre scale, with a confidence interval running from 2 to 24 --
real, but the lower end is trivially small -- while a cool-down afterwards moved
it by exactly nothing. Movement changed how the muscle felt. It did not change
what the muscle could do.

There is a useful timing asymmetry buried in that: doing the work BEFORE beats
doing it after. The cool-down result is a flat zero in both trials.

And one caution runs opposite to intuition. Long static holds cause their own
acute drop in force output. Applying a long static stretch to a muscle that is
already carrying residual fatigue means stacking one deficit on another. That
specific combination has not been tested, so treat it as a caution rather than a
result -- but it is the one prep choice where the evidence argues against the
instinct to "loosen it up" before working it. Short holds, well under the
threshold and embedded in a fuller warm-up, do not carry that cost.

The net, and it matches the framing the question arrived with: do the prep for
the session in front of you, and accept a modest reduction in later soreness as
a bonus. Do not expect it to make the muscle recover faster. Nothing measured so
far does that.

## Applicability check (2026-08-22) -- NOT adopted, implication only

This is the item that answers the question the warehouse could not answer.
Checked against `files/program/prep.yaml` and `program.yaml`. **Neither file was
touched, and no change is proposed.** A program-design consult is pending; the
decision is the owner's.

Current state: `mat_prep` runs first on every day and is all dynamic/activation
work; `equipment_prep` follows with light-load specific primers; K4 (adductor
isometric, 15 s x2) is the only timed hold and is an activation primer, not a
stretch; the `cooldown` block holds one item, HP1, with no duration. H1
(스탠딩 햄스트링 정적 스트레칭) is defined with `default_phase: mat_prep`, marked
not trim-eligible, queued for wave-2 restoration to the day blocks, and renders
on no day today.

What this item would imply for the mat-prep design:

1. **The prep block is justified -- for the session in front of him.** Warming a
   muscle that still carries fatigue from the previous session should still help
   that day's output. That is inference from the general warm-up literature
   rather than a measurement of the fatigued case, but nothing argues against it.
2. **It should not be justified as a recovery accelerator.** If any rationale in
   the program presents mat-prep as helping the muscle recover faster, or as
   "flushing out" accumulated fatigue, that claim is unsupported and the nearest
   randomized evidence points the other way: a warm-up before a damaging session
   left the day-2 and day-3 force loss completely unchanged while making the
   muscle feel less tender. His own framing -- prep does not restore accumulated
   fatigue -- is the half of the split the evidence backs.
3. **A modest soreness benefit is a legitimate secondary reason to keep it,**
   stated at its real size: about 13 mm on a 100 mm scale at 48 hours, from a
   warm-up done BEFORE the bout, with a confidence interval whose lower end is
   near-trivial. Not nothing, not much.
4. **Timing asymmetry favours prep over cooldown.** In both randomized trials the
   work done before the session moved soreness and the work done after moved
   nothing at all. If prep time and cooldown time ever compete for the same
   minutes, that is the direction the evidence leans -- though it says nothing
   about HP1's mobility rationale, which stands separately.
5. **The one caution attaches to H1.** A long static hold on a hamstring that is
   already fatigued stacks a stretch-induced force deficit on an existing one.
   The combination is untested, so this is a caution and not a finding, and it
   only bites at long hold durations -- see
   exercise/acute-static-stretch-force-deficit-021 for the threshold and for why
   short holds inside a full warm-up are in the no-detectable-effect zone. The
   day where it would matter most is 뒷B, where the RDL makes the hamstrings the
   working muscle.
