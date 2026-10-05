---
# Collection sprint 2026-09-02, cat-domain opening. The counterweight to the
# single most defeatist piece of cat folklore -- "cats hide pain, you can't
# tell". A validated observational instrument exists, it is built entirely from
# facial features a person can see, and it reports its own reliability. This is
# the closest thing the domain has to a measurement tool a household can use,
# and it is also the item where the diagnosis boundary is easiest to trip over:
# an observation score is not a diagnosis and the item says so repeatedly.
# Rubric: cat @clinical-vet (VC-A, borrowed anchor -- read one band down).
id: cat/pain-observable-grimace-scale-006
domain: cat
grade: B (that a validated facial-expression instrument for acute feline pain exists and reports the stated reliability figures); D (any use of its cut-off score as a household decision rule, and any application outside acute pain)
lane: "@clinical-vet"
locale: universal
as_of: 2019
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/31836868/"  # Evangelista MC, Watanabe R, Leung VSY, Monteiro BP, O'Toole E, Pang DSJ, Steagall PV. 2019, Sci Rep 9(1):19128, doi 10.1038/s41598-019-55693-8 -- Feline Grimace Scale development and validation; 35 client-owned painful cats and 20 controls; five action units; rho = 0.86 against an established instrument; inter-rater ICC 0.89 (95 pct CI 0.85-0.92); intra-rater above 0.91; internal consistency 0.89; cut-off total score above 0.39 out of 1.0
  - "cat/curator-checklist-001"  # domain rule: a validated instrument reporting its own reliability sits above consensus, and below a large dataset
  - "cat/urinary-obstruction-same-day-005"  # the neighbouring row on what warrants professional attention; this one supplies the observation side, not a threshold for acting
refraction_notes:
  - note: >
      WHAT THE INSTRUMENT IS. The Feline Grimace Scale scores five facial action
      units -- ear position, orbital tightening, muzzle tension, whiskers change,
      and head position -- each of which is a visible feature rather than a
      physiological measurement. It was developed and validated on 35 client-owned
      cats presenting in pain against 20 controls. It correlated very strongly
      with an established pain instrument (rho = 0.86, p below 0.001), with
      inter-rater reliability ICC 0.89 (95 percent CI 0.85-0.92), intra-rater
      reliability above 0.91, internal consistency 0.89, and a reported cut-off of
      a total score above 0.39 out of 1.0.
    grade: B
  - note: >
      WHY THIS MATTERS MORE THAN THE NUMBERS DO. The folklore version of this
      subject is that cats conceal pain as an evolutionary reflex and that an
      owner therefore cannot know. That framing is defeatist and it is now false
      at least for acute pain: the observable signal was found to be reliable
      enough that different raters agree on it to an ICC of 0.89. The correct
      replacement for "you can't tell" is "the signal is in the face, it is
      learnable, and trained raters agree on it".
    grade: B
  - note: >
      THE CUT-OFF IS NOT A HOUSEHOLD DECISION RULE and must never be spoken as
      one. The 0.39-out-of-1.0 threshold was derived on 35 painful cats and 20
      controls in a clinical setting by trained raters, as a decision point about
      ANALGESIC INTERVENTION. Reproducing it as "score your cat and if it is above
      0.39 do X" would convert an observational instrument into a treatment trigger
      and would cross this domain's scope boundary in one step. The item carries
      the number because the paper reports it, and refuses the operationalisation.
    grade: D
  - note: >
      SCOPE OF VALIDATION IS ACUTE PAIN. The development sample was cats
      presenting acutely in a clinical context. Nothing in this source validates
      the instrument for chronic pain, for degenerative joint disease, for
      long-term monitoring at home, or for cats whose facial anatomy differs
      markedly by breed. An agent that used a grimace score to conclude a cat's
      long-term arthritis was or was not being managed would be reading the
      instrument outside everything it was tested on.
    grade: D
  - note: >
      OBSERVATION IS NOT DIAGNOSIS, and this is the row where that distinction is
      easiest to lose. A high score says a person can see something. It does not
      say what is wrong, where it is, or what should happen. The correct
      operational chain is observe, then route -- exactly as at
      cat/urinary-obstruction-same-day-005. This warehouse supplies the observing
      half and stops there.
    grade: D
  - note: >
      NOT ESTABLISHED HERE: whether an untrained owner can apply it. The
      reliability figures come from raters in a validation study, not from cat
      owners scoring their own animals at home, and no source read in this sprint
      tested lay-observer performance. The instrument's existence proves the
      signal is real and legible; it does not prove that any given person reads it
      correctly. Treat the finding as "there is something visible here worth
      learning to see", not as "you now have a home test".
    grade: D
claim: >
  Acute pain in cats is visible in the face, reliably enough to be measured. The
  Feline Grimace Scale (Evangelista et al., 2019, Scientific Reports) was
  developed and validated on 35 client-owned cats presenting in pain against 20
  controls, scoring five action units -- ear position, orbital tightening, muzzle
  tension, whiskers change, and head position. It correlated with an established
  pain instrument at rho = 0.86 (p < 0.001), with inter-rater reliability ICC
  0.89 (95 percent CI 0.85-0.92), intra-rater reliability above 0.91, internal
  consistency 0.89, and a reported cut-off of a total score above 0.39 out of
  1.0. This directly contradicts the common framing that cats conceal pain so
  completely that an owner cannot know: the signal is in the face, and trained
  raters agree on it. Three boundaries hold. The cut-off is a clinical decision
  point about analgesic intervention and is NOT a household decision rule. The
  validation covers ACUTE pain in a clinical setting -- not chronic pain, not
  degenerative joint disease, not long-term home monitoring. And lay-observer
  performance was not tested by this source, so the finding is that the signal is
  real and learnable, not that any given person reads it correctly. Observation
  is not diagnosis; the chain is observe, then route.
reasoning: >
  Most of what this domain has to say about pain is either folklore or clinical
  practice, so a properly validated instrument that reports its own reliability
  coefficients is unusually strong material and is graded accordingly -- not on
  the strength of the sample, which is 35 and 20, but on the fact that
  reliability is the thing being measured and it was measured well. The item
  ships mainly for what it displaces. "Cats hide pain, you can't tell" is one of
  the most confidently repeated lines in cat keeping and it is also the most
  disabling, because it tells an owner that attention is pointless. An
  inter-rater ICC of 0.89 on five facial features says the opposite: the signal
  is there, it is legible, and agreement on it is high. That is a better thing to
  give a household than any behavioural tip. The three boundaries are all places
  where a well-meaning agent would otherwise overreach. The cut-off number is the
  most dangerous, because it is concrete, it is in the paper, and turning it into
  "if the score exceeds this, do something" converts an observation scale into a
  treatment trigger in a single sentence -- which is exactly the line the domain
  checklist declares absolute. The acute-versus-chronic scope limit matters
  because the most common real-world use case in an older cat is joint pain, and
  the instrument was not tested there. And the lay-observer gap is stated because
  it is the difference between "there is something worth learning to see" and
  "you have a home test", and only the first is supported.
---

# cat/pain-observable-grimace-scale-006

The most repeated line about cats and pain is that they hide it so well you
cannot tell. For acute pain, that is no longer true.

A validated instrument scores five things in a cat's face: ear position, how
tight the area around the eyes is, tension in the muzzle, the position of the
whiskers, and the position of the head. All five are visible features, not
measurements. It was developed and validated on thirty-five cats presenting in
pain against twenty controls, and it correlated very strongly with an established
pain instrument. More importantly for the folklore it displaces, different raters
agreed with each other at a high level, and the same rater agreed with themselves
at a higher one.

So the honest replacement for "you can't tell" is: the signal is in the face,
it is learnable, and people who learn it agree about what they are seeing.

Three limits, all of which matter.

The scale has a published cut-off, and that cut-off is not a rule for a
household. It was derived in a clinical setting by trained raters as a decision
point about whether to give pain relief. Turning it into "score your cat, and
above this number do something" would convert an observation tool into a
treatment trigger, which is precisely the line this warehouse does not cross.

It was validated on acute pain in a clinical context. Not on chronic pain, not on
the joint disease that is the commonest real problem in an older cat, not on
long-term monitoring at home. Reading a grimace score as evidence about a cat's
arthritis is using the instrument outside everything it was tested on.

And the reliability figures come from raters in a validation study, not from
owners scoring their own cats at their own kitchen table. Nothing here tested
whether an untrained person reads it correctly. What the study proves is that the
signal exists and is legible. It does not hand anyone a home test.

The chain this supports is the same one that runs through the rest of this
domain: observe, then route. Seeing something is not knowing what it is.
