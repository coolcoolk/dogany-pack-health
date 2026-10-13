---
# Collection sprint 2026-09-02. The highest-certainty actionable item in this
# domain, and the one that most directly inverts common advice: the AASM's own
# systematic-review guideline issues a STRONG recommendation FOR multicomponent
# CBT-I and a recommendation AGAINST sleep hygiene used on its own. Sits
# directly on the lane's authority anchor (sleep-recovery/aasm-hierarchy-001)
# and its grading anchor (sleep-recovery/grade-aasm-anchor-002), which is
# exactly the path those two items were authored to enable.
# Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/cbti-strong-sleep-hygiene-weak-007
domain: sleep-recovery
grade: A
lane: "@clinical"
locale: universal
as_of: 2021
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/33164742/"  # Edinger JD, Arnedt JT, Bertisch SM, Carney CE, Harrington JJ, Lichstein KL, Sateia MJ, Troxel WM, Zhou ES, Kazmi U, Heald JL, Martin JL. 2021, J Clin Sleep Med 17(2):255-262, doi 10.5664/jcsm.8986, PMCID PMC7853203 -- the AASM clinical practice guideline
  - "https://pubmed.ncbi.nlm.nih.gov/33164741/"  # same task force, 2021, J Clin Sleep Med 17(2):263-298, doi 10.5664/jcsm.8988 -- the accompanying systematic review, meta-analysis and GRADE assessment that the guideline rests on
  - "sleep-recovery/aasm-hierarchy-001"  # why an AASM systematic-review guideline is a real top-tier anchor in this domain
  - "sleep-recovery/grade-aasm-anchor-002"  # the certainty-versus-strength separation this item depends on
  - "framework:GRADE -- this is the archetype the domain's anchor items describe: a task force, a systematic review with meta-analysis, explicit GRADE certainty ratings, and recommendation strengths assigned separately from certainty. The CBT-I recommendation is STRONG; every other recommendation in the guideline including the negative one on sleep hygiene is CONDITIONAL. The letter grade here reports certainty in the guideline's finding, not the strength of any single recommendation."
refraction_notes:
  - note: >
      The negative recommendation is the surprising half and it is easy to
      overstate. The guideline suggests clinicians NOT use sleep hygiene as a
      SINGLE-COMPONENT therapy for chronic insomnia disorder, and that
      recommendation is CONDITIONAL, not strong. It does not say sleep-hygiene
      advice is worthless or harmful, and it does not address sleep hygiene as
      one element inside a multicomponent programme -- which is where it
      normally lives. What it rules out is sleep hygiene ALONE as the treatment.
    grade: A
  - note: >
      Scope gate. This guideline is about CHRONIC INSOMNIA DISORDER, a clinical
      diagnosis, not about a healthy trainee who wants better sleep. Applying a
      strong clinical recommendation to a non-clinical goal is a category error.
      What transfers cleanly is the negative finding, because "give the person a
      list of sleep-hygiene tips" is precisely the intervention a general
      wellness context reaches for by default, and it is the one component the
      task force declined to endorse on its own.
    grade: B
  - note: >
      Stimulus control and sleep restriction therapy are separately endorsed as
      single-component therapies, both CONDITIONAL. Sleep restriction therapy in
      this clinical sense means deliberately compressing time in bed to
      consolidate sleep; it is NOT sleep deprivation and must never be conflated
      with the sleep-loss exposure in item 004, which is a harm. Same words,
      opposite intent.
    grade: A
  - note: >
      Do not read the CBT-I strength as a claim about effect size. Per the
      domain's grading anchor, GRADE separates certainty of evidence from
      strength of recommendation on purpose. STRONG here means clinicians should
      follow it under most circumstances; it is not a statement about how many
      minutes of sleep anyone gains.
    grade: A
claim: >
  For chronic insomnia disorder in adults, the American Academy of Sleep Medicine
  issues its only STRONG recommendation for multicomponent cognitive behavioural
  therapy for insomnia (CBT-I), and issues a recommendation AGAINST using sleep
  hygiene as a single-component therapy. Both statements come from the 2021 AASM
  clinical practice guideline, developed by a commissioned task force from a
  systematic review with meta-analysis and explicit GRADE assessment, with
  recommendation strengths assigned separately from evidence certainty. The full
  set: multicomponent CBT-I (STRONG for); multicomponent brief therapies
  (conditional for); stimulus control as a single component (conditional for);
  sleep restriction therapy as a single component (conditional for); relaxation
  therapy as a single component (conditional for); sleep hygiene as a single
  component (conditional AGAINST). The load-bearing consequence is that the
  single most commonly dispensed piece of sleep advice -- a list of hygiene tips
  -- is the one component this guideline declines to endorse on its own, while
  the structured behavioural programme that is rarely offered first is the one
  that carries the strong recommendation. Two boundaries: the guideline addresses
  a clinical diagnosis, not general sleep optimisation in a healthy trainee; and
  "sleep restriction therapy" here means deliberately compressing time in bed to
  consolidate sleep, which is a treatment, not the sleep-loss exposure that
  degrades performance.
reasoning: >
  This item is the payoff for the two methodology items this domain already
  carried. sleep-recovery/aasm-hierarchy-001 established that AASM clinical
  practice guidelines are grounded in systematic reviews with explicit
  benefit-harm weighing rather than expert opinion, which is what makes a real
  top confidence band available in this field at all;
  sleep-recovery/grade-aasm-anchor-002 established that the AASM adopted GRADE
  wholesale in 2016 and that certainty of evidence must never be conflated with
  strength of recommendation. Edinger et al. 2021 is the instance those two items
  predict: a commissioned task force, a companion systematic review with
  meta-analysis and GRADE assessment published alongside the guideline in the
  same issue (J Clin Sleep Med 17(2):263-298), explicit consideration of
  clinically relevant benefits and harms, patient values and resource use, and
  board approval. Graded at the top band accordingly -- the certainty concerns
  the guideline's findings, which are exactly what the anchor items say can be
  trusted here. The negative recommendation on sleep hygiene deserves the same
  discipline the domain applies elsewhere: it is CONDITIONAL, it is scoped to
  single-component use, and it is scoped to chronic insomnia disorder. Stated
  carefully it is still the most useful line in the guideline for a general
  consumer, because a hygiene checklist is the default intervention that anyone
  asking about sleep receives, and the task force reviewed it and declined to
  recommend it standing alone. Not flagged contested: no source located in this
  sprint disputes the guideline, and the AASM position is itself the field's
  authority. The genuine risks are misapplication rather than dispute, so they
  are carried as refraction notes -- the clinical-versus-general scope gate, and
  the collision between the clinical term "sleep restriction therapy" and the
  sleep-loss harm described in item 004.
---

# sleep-recovery/cbti-strong-sleep-hygiene-weak-007

The sleep field has an authoritative body, that body writes guidelines from
systematic reviews rather than from opinion, and on the treatment of chronic
insomnia it says two things that are worth putting side by side.

The strongest recommendation in the whole guideline is for multicomponent
cognitive behavioural therapy for insomnia. It is the only one the task force
marked strong, meaning clinicians should follow it under most circumstances.

And the one component the task force declined to endorse on its own is sleep
hygiene -- the list of tips. Cool dark room, no screens, no late coffee,
consistent bedtime. As a standalone treatment for chronic insomnia the guideline
suggests clinicians do not use it.

That is close to an exact inversion of what most people are handed. The tips are
what everyone gets first; the structured programme is what almost nobody is
offered.

Some care is needed with both halves. The negative recommendation is conditional,
not strong, and it is aimed specifically at sleep hygiene used ALONE. It does not
say the advice is useless, and it says nothing against hygiene elements sitting
inside a larger programme, which is where they normally sit. The guideline is also
about a clinical diagnosis. Someone who sleeps fine and simply wants to sleep
better is not the population this was written for.

Even with those fences up, the useful signal survives, because "here is a list of
sleep hygiene tips" is exactly the reflex answer a general wellness context
produces, and it is exactly the intervention that was reviewed and not endorsed
on its own.

One naming trap worth flagging permanently. The guideline conditionally endorses
"sleep restriction therapy" as a single-component treatment. That means
deliberately shrinking time in bed so that sleep consolidates -- a technique with
a clinical purpose. It is not the same thing as short sleep, which has a measured
performance cost documented elsewhere in this domain. Identical words, opposite
intent, and the two must never be allowed to collide in an answer.

Finally, a discipline point this domain already carries: strong here describes
how confidently a clinician should act, not how big the effect is. The framework
keeps those on separate axes deliberately, and a strong recommendation is not a
promise about minutes of sleep gained.
