---
# Collection sprint 2026-09-02. First SUBSTANTIVE claim ever authored in this
# domain -- the gap GAPS.md has carried open since v2 ("There are ZERO
# substantive sleep/recovery claims"). Anchored to a single large meta-analysis
# of controlled experiments, which is the strongest design available on this
# question. Rubric: sleep-recovery @clinical (VC-A). The whole item is built
# around the MODERATORS, not the headline number, because the headline number
# carries an I-squared of 98.1 percent and is therefore not the finding.
# Source re-audit 2026-10-06: Craven 2022 abstract re-read (PubMed 35708888);
# the ~0.4 percent-per-hour-awake slope is reported for deprivation and
# late-restriction protocols only -- claim and note 3 now say so. Rest verified.
id: sleep-recovery/sleep-loss-performance-decrement-004
domain: sleep-recovery
grade: B (direction and moderator structure); D (the pooled -7.56 percent point estimate)
lane: "@clinical"
locale: universal
as_of: 2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/35708888/"  # Craven J, McCartney D, Desbrow B, Sabapathy S, Bellinger P, Roberts L, Irwin C. 2022, Sports Med 52(11):2669-2690, doi 10.1007/s40279-022-01706-y, PMCID PMC9584849 -- 69 publications, 227 outcome measures
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC9584849/"  # same paper, open-access full text
  - "sleep-recovery/regularity-appetite-brief-rules-016"  # weekly, regularity and appetite brief rules that share this item's 6 h exposure line; the single-night rules are in 072 (linked 2026-10-07, v38)
  - "framework:GRADE -- the pooled effect is downgraded hard for inconsistency (I-squared 98.1 percent). What survives that downgrade is the DIRECTION (negative, significant in every exercise category) and the two moderators the authors tested prospectively: sleep-loss PATTERN and TIME OF DAY. The item grades those separately from the number."
applicability:
  axes:
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      Do NOT speak the -7.56 percent figure as a personal expectation. Its
      confidence interval is -11.9 to -3.13 and its heterogeneity is I-squared
      98.1 percent, which means the included studies are not estimating one
      common effect. The number is a summary of a very scattered literature,
      not a prediction for one lifter on one night.
    grade: D
  - note: >
      The single most actionable result is the PATTERN split, and it is
      counterintuitive. Consistent negative effects appeared only under total
      deprivation and under LATE restriction -- being woken earlier than
      normal. EARLY restriction, meaning a delayed bedtime with a normal wake
      time, did not show the consistent negative effect. So a late night is not
      equivalent to an early alarm, and the early alarm is the worse one for a
      training session.
    grade: B
  - note: >
      Time of day moderates the whole thing. Tasks performed in the PM were
      consistently impaired; tasks performed in the AM were largely unaffected.
      The authors' own practical advice is to move the session EARLIER after a
      bad night, not to cancel it. This is mechanistically coherent with the
      dose relationship they found -- roughly 0.4 percent performance decrement
      per additional hour awake before the task, reported for the deprivation
      and late-restriction protocols -- so the damage accumulates
      across the waking day rather than being fixed at wake-up.
    grade: B
  - note: >
      Population limit: 959 of the participants, about 89 percent, were male.
      Sex-conditioned effects were not resolvable. Also note the exposure
      definition -- "sleep loss" here is 6 hours or less in any 24-hour period,
      which is a real deficit, not a slightly short night.
    grade: C
  - note: >
      This item covers ACUTE sleep loss only. Whether accumulated deficit across
      a training week behaves the same way, and whether extra sleep afterwards
      undoes it, are NOT answered by this source and were not established by any
      source found in this sprint. See the sleep-debt gap in GAPS.md.
    grade: D
claim: >
  Losing sleep measurably degrades physical performance, and unlike most of the
  recovery literature this one holds up on OBJECTIVE endpoints rather than on
  perceived readiness. A meta-analysis pooling 227 outcome measures from 69
  publications, comparing exercise under normal sleep (more than 6 h in 24 h)
  against sleep loss (6 h or less in 24 h), found a negative effect on
  performance that was significant in every exercise category tested: anaerobic
  power, speed and power endurance, high-intensity interval work, STRENGTH,
  endurance, strength-endurance and skill. The pooled figure was a mean change
  of -7.56 percent (95 percent CI -11.9 to -3.13), but heterogeneity was
  I-squared 98.1 percent, so that number should be treated as an order of
  magnitude and nothing more. The durable findings are the two moderators. FIRST,
  the pattern matters: consistent negative effects appeared only with total
  deprivation and with LATE restriction (waking earlier than normal), not with
  early restriction (going to bed later than normal with the usual wake time).
  SECOND, time of day matters: PM sessions were consistently impaired while AM
  sessions were largely unaffected, and under deprivation and late restriction
  performance fell by roughly 0.4 percent for every additional hour awake before
  the task. The operative consequence for
  a training decision is therefore not "skip the session" but "an early alarm
  costs more than a late bedtime, and the cost grows across the day."
reasoning: >
  Craven et al. 2022 (Sports Med 52(11):2669-2690) is the strongest available
  design on this question because the underlying studies are controlled
  experiments in which the same participants are tested under a normal-sleep
  control and a sleep-loss intervention, so the comparison is not observational.
  That is what lets this claim reach a higher confidence band than most of the
  recovery literature, where the intervention cannot be blinded and the outcome
  is a rating. Here the outcomes are power, force and time. The reason the item
  nonetheless refuses to grade the pooled number highly is I-squared 98.1
  percent: at that level of inconsistency the studies are demonstrably not
  measuring one common effect, and reporting -7.56 percent as if it were a
  personal expectation would be exactly the effect-inflation failure that
  learning-habits/effect-inflation-screening-008 exists to catch. What the
  authors did do properly is pre-specify subgroup analyses, and those results are
  both internally coherent and mechanistically sensible. The pattern split
  (deprivation and late restriction harmful, early restriction not consistently
  so) and the time-awake dose relationship (about -0.4 percent per hour awake)
  point at the same underlying variable, namely hours of continuous wakefulness
  before the task rather than hours of sleep lost in the abstract. The AM/PM
  asymmetry falls out of the same mechanism. Not flagged contested: no source
  found in this sprint disputes the direction, and the field-authority anchor
  (sleep-recovery/aasm-hierarchy-001) is not in tension with it. The limitations
  are carried as refraction notes rather than as a contested flag because they
  narrow the claim rather than opposing it.
---

# sleep-recovery/sleep-loss-performance-decrement-004

Sleep is the one item in the recovery cupboard that survives the hard test.
Almost everything else marketed as recovery moves how sore or how fresh someone
FEELS and stops working the moment you measure what the muscle can do. Sleep loss
does not behave that way: it shows up in power output, in force, in time on the
clock, across a meta-analysis of 227 outcome measures drawn from 69 papers, and
it shows up in every exercise category including strength.

The headline number from that analysis is about a 7.5 percent drop. Do not carry
that number around. The studies behind it disagree with each other about as much
as studies can disagree -- the inconsistency statistic is 98 percent, which means
they are not all measuring the same thing. The direction is solid. The magnitude
is a smear.

What is worth carrying is the shape of it, and the shape is not what most people
assume.

First, how you lose the sleep matters more than how much you lose. Going to bed
late and waking at the usual time did not produce a consistent decrement. Being
woken earlier than usual did. So a late night and an early alarm are not the same
injury, and the early alarm is the worse one.

Second, when you train matters. Sessions run in the afternoon or evening after
sleep loss were consistently impaired. Sessions run in the morning were largely
unaffected. This is not mysterious: the same analysis found performance falling
by roughly 0.4 percent for every extra hour spent awake before the task. The
deficit is a function of how long you have been up, so it is smallest right after
you get out of bed and worst late in the day.

Put those together and the practical move after a short night is to shift the
session earlier rather than to cancel it. That is the authors' own conclusion,
not an extrapolation.

Two boundaries. The exposure studied is 6 hours or less in a 24-hour period --
a genuine deficit, not a mildly short night, so nothing here licenses treating
7 hours instead of 8 as a performance emergency. And about 89 percent of
participants were male, so nothing here resolves sex-conditioned effects.

Finally, what this does NOT cover: accumulated deficit across a week, and whether
sleeping extra afterwards repays it. Neither question was answerable from any
defensible source in this sprint, and both are logged as open gaps rather than
guessed at.
