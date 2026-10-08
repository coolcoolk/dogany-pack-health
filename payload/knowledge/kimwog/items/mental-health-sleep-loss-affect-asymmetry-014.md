---
# Collection sprint 2026-09-02 (mental-health lane expansion). The lane's
# strongest experimental item and its cleanest cross-domain bridge: this is
# controlled EXPERIMENTAL evidence, not correlation, on a variable a life agent
# already observes. The finding that makes it worth authoring is an ASYMMETRY --
# sleep loss reliably removes the good, and its effect on the bad is mixed --
# which is the opposite of how the relationship is usually stated. Pairs with
# sleep-recovery/sleep-loss-performance-decrement-004, which is the same
# asymmetry discipline applied to physical output.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/sleep-loss-affect-asymmetry-014
domain: mental-health
grade: "A (that experimentally induced sleep loss reduces positive affect, increases anxiety symptoms and blunts emotional arousal); C (any effect on negative affect or depressive symptoms, which were mixed and depended on the type of sleep loss)"
lane: "@clinical"
locale: universal
as_of: 2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/38127505/"  # Palmer CA, Bower JL, Cho KW, Clementi MA, Lau S, Oosterhoff B, Alfano CA. 2024, Psychol Bull 150(4):440-463, doi 10.1037/bul0000410 -- preregistered systematic review and meta-analysis, 1338 effect sizes across 154 studies, N=5717, participant age range 7 to 79
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # the physical-output partner; the same directional asymmetry between sleep LOSS and sleep EXTENSION
  - "sleep-recovery/hour-target-is-a-threshold-consensus-013"  # why no specific hour count may be attached to this finding as an individual optimum
  - "mental-health/group-to-individual-nongeneralizability-012"  # the governor when this pooled effect is applied to one person's night
  - "framework:GRADE -- experimental manipulation in healthy participants with preregistration, across five decades of studies. This is the highest-quality design available anywhere in this lane: the exposure was induced rather than observed, so confounding and reverse causation do not apply. The split grade reflects that the review's own results were consistent for some outcomes and mixed for others."
applicability:
  axes:
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The asymmetry is the finding. All forms of sleep loss reduced POSITIVE
      AFFECT (standardized mean difference -0.27 to -1.14), increased ANXIETY
      symptoms (0.57 to 0.63), and blunted AROUSAL in response to emotional
      stimuli (-0.20 to -0.53). Findings for NEGATIVE AFFECT, for reported
      emotional valence in response to stimuli, and for DEPRESSIVE SYMPTOMS were
      MIXED and depended on which form of sleep loss was studied. The robust
      casualty of a short night is the good stuff, not the bad stuff.
    grade: A
  - note: >
      Why that asymmetry matters more than it sounds. The popular version of this
      relationship is that poor sleep makes people irritable, low, negative --
      that it ADDS something unpleasant. The measured version is that it
      SUBTRACTS: enjoyment, enthusiasm, engagement, responsiveness. Someone who
      slept badly is more likely to report that nothing much landed than to
      report that everything was awful, and those two states call for different
      responses and are easily confused.
    grade: A
  - note: >
      The design is what earns the top band. This is EXPERIMENTAL: total sleep
      deprivation, partial sleep restriction or sleep fragmentation was IMPOSED on
      healthy participants. The exposure was manipulated rather than observed, so
      unlike almost everything else in this lane the finding is not vulnerable to
      confounding or reverse causation. It is also preregistered, and it spans 154
      studies, 1338 effect sizes and 5717 participants across five decades.
    grade: A
  - note: >
      Effects were NONLINEAR in the amount of sleep lost, and differed by which
      sleep stage was restricted (rapid eye movement versus slow-wave). So the
      relationship is not a straight line from hours to mood, and no per-hour
      conversion may be constructed from these numbers.
    grade: A
  - note: >
      Boundary against the hour-count trap. This establishes what happens when
      sleep is REDUCED FROM A PERSON'S OWN BASELINE under experimental conditions.
      It says nothing about what any individual's optimal duration is, and it must
      not be joined to a target number. The sleep domain's own consensus-threshold
      item records why any specific hour figure is a population threshold rather
      than an individual optimum.
    grade: A
  - note: >
      Boundary against the reverse inference. The experiment ran one way: impose
      sleep loss, measure affect. It does not license reading backwards from
      someone's mood to a conclusion about their sleep, and it does not license
      reading forward from an observed short night to a claim about how they feel
      today -- that is a within-person prediction, which item 012 addresses and
      item 013 shows has not been established from tracked data.
    grade: A
claim: >
  Experimentally imposed sleep loss reliably takes away positive feeling and only
  unreliably adds negative feeling. Palmer et al. 2024 (Psychological Bulletin), a
  preregistered systematic review and meta-analysis of 1338 effect sizes across
  154 studies (N=5717, ages 7 to 79) that experimentally reduced sleep in healthy
  participants via total deprivation, partial restriction or fragmentation, found
  that ALL forms of sleep loss reduced positive affect (standardized mean
  difference -0.27 to -1.14), increased anxiety symptoms (0.57 to 0.63) and blunted
  arousal in response to emotional stimuli (-0.20 to -0.53), while findings for
  negative affect, for reported emotional valence, and for depressive symptoms
  were MIXED and depended on the type of sleep loss. Effects were nonlinear in the
  amount of sleep lost and differed by which sleep stage was restricted. The
  design is the reason this sits at the top of the lane: the exposure was
  manipulated rather than observed, so neither confounding nor reverse causation
  applies. Three boundaries. The popular framing has the direction wrong -- short
  sleep subtracts enjoyment and engagement more reliably than it adds misery, and
  those two states look different and call for different responses. No hour
  target may be attached: this measures reduction from a person's own baseline,
  not an individual optimum. And the experiment ran one way only, so it licenses
  neither reading backwards from mood to sleep nor forward from one observed short
  night to a claim about how a specific person feels today.
reasoning: >
  This is the best-designed evidence in the lane and it lands on a variable the
  consumer already holds, which makes it the highest-value item in the sprint.
  Nearly everything else here is observational or is a trial that could not blind
  its participants; this is an experimental manipulation in healthy people,
  preregistered, pooled across five decades and 154 studies. Confounding and
  reverse causation -- the two objections that limit items 009 and 013 -- simply do
  not apply, which is why the top band is available here and rarely elsewhere in
  this domain. It was authored around the ASYMMETRY rather than around a headline
  effect size because the asymmetry is where the popular version of this claim is
  actually wrong: the reliable consequence of a short night is a flattening, not a
  souring, and the review's own results are consistent for positive affect,
  anxiety and blunted arousal while explicitly mixed for negative affect and
  depressive symptoms. Grading is split to keep those apart, since collapsing them
  into one letter would launder the mixed half into the robust half. Three
  boundary notes are carried at the top band because each blocks a specific misuse
  that a tracking system would otherwise commit: attaching an hour target,
  inferring sleep from mood, and predicting today's feeling from last night's
  duration for one individual. The sleep domain's own items are cited as
  dependencies rather than restated, since the threshold-versus-optimum argument
  and the loss-versus-extension asymmetry are already established there. Not
  flagged contested: no source located disputes the review, and its mixed findings
  are reported as mixed by the authors rather than being a dispute between sources.
---

# mental-health/sleep-loss-affect-asymmetry-014

Almost everything else in this lane is people being observed. This is people
being experimented on, which is why it is the sturdiest thing here.

Across 154 studies spanning five decades, researchers deliberately shortened,
fragmented or eliminated the sleep of healthy volunteers and then measured how
they felt. More than thirteen hundred effect sizes, nearly six thousand
participants, ages seven to seventy-nine, and the whole synthesis preregistered.

Because the sleep loss was imposed rather than observed, the usual escape routes
close. There is no question of whether low mood caused the bad sleep, and no
question of some third factor causing both. The experimenters caused it.

And the result is not quite the one everybody repeats.

What sleep loss reliably did was remove positive feeling. Every form of sleep
loss studied reduced positive affect. It also raised anxiety symptoms and blunted
how strongly people responded to emotional material at all.

What it did NOT do reliably was increase negative feeling. Effects on negative
affect, on how people rated emotional material, and on depressive symptoms came
out mixed, and depended on which kind of sleep loss was involved.

So the shape is subtraction, not addition. A person who slept badly is more
likely to report that the day did not land -- that nothing was especially good,
that things felt muted -- than to report that everything was terrible. Those two
descriptions get treated as the same complaint and they are not, and confusing
them leads to responding to a flatness problem as though it were a distress
problem.

Two more details from the data that block tidy conversions. The effects were
nonlinear in how much sleep was lost, and they differed depending on which stage
of sleep was cut. So there is no per-hour exchange rate to be constructed here,
however much a system tracking hours might want one.

And three limits on what may be done with it.

No hour target attaches to this. The experiments reduced sleep relative to a
person's own baseline. They say nothing about what any individual's right
duration is, and the sleep domain separately records why a headline hour figure
is a population threshold rather than a personal optimum.

The experiment ran in one direction only. It does not license reading backwards
-- inferring from someone's mood that they must have slept badly.

And it does not license reading forwards for one specific person on one specific
day. That is a within-person prediction from a between-person average, which is
the move the warehouse's group-to-individual item exists to stop, and which the
tracking literature has not managed to establish either.

The usable version is short and it is worth getting the direction right: cutting
sleep predictably costs enjoyment and responsiveness before it costs anything
else, and it does so in a way that has been demonstrated by experiment rather
than inferred from correlation.
