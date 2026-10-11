---
# Collection sprint 2026-08-22. Fills GAPS gap-area 3 (DOMS -- mechanism,
# timeline, modifiers). Routed to the exercise domain rather than sleep-recovery
# on purpose: sleep-recovery's single lane is @clinical (VC-A) anchored to the
# AASM/sleep-medicine authority hierarchy, which is the wrong verification
# culture for exercise-induced muscle nociception. Rubric: exercise.rubric.md
# @clinical-physio.
id: exercise/doms-timeline-mechanism-023
domain: exercise
grade: B (timeline and repeated-bout protection); C (causal mechanism)
lane: "@clinical-physio"
locale: universal
as_of: 2002-2024
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/12453160/"  # Nosaka/Newton/Sacco 2002, Scand J Med Sci Sports 12(6):337-346, n=110, DOMS vs damage-marker correlations
  - "https://link.springer.com/article/10.1007/s12576-015-0397-0"  # Mizumura & Taguchi 2016, J Physiol Sci 66(1):43-52, neurotrophic-factor mechanism review
  - "https://www.jneurosci.org/content/30/10/3752"  # Murase et al. 2010, J Neurosci 30(10):3752-3761, bradykinin/NGF causal pathway in rat
  - "https://pubmed.ncbi.nlm.nih.gov/27782911/"  # Hyldahl/Chen/Nosaka 2017, Exerc Sport Sci Rev 45(1):24-33, repeated-bout effect mechanisms review
  - "framework:GRADE -- the ONSET/PEAK/RESOLUTION timeline is the most-replicated observation in this literature (hundreds of controlled eccentric-bout studies converge) and sits high. The MECHANISM is genuinely contested: the causal nociception work is rodent, and the classical damage-inflammation account and the neurotrophic account are both live. Certainty of evidence and strength of the practical recommendation are separate axes here -- the practical instruction (do not steer training off soreness) is strong even where the mechanism is low-certainty."
refraction_notes:
  - note: >
      Do NOT treat soreness as a readout of muscle damage, of training
      stimulus, or of recovery status. Nosaka/Newton/Sacco 2002 had 110 men
      perform 12, 24 or 60 maximal eccentric elbow-flexor actions and tracked
      soreness alongside maximal isometric force, joint angles, arm
      circumference and plasma creatine kinase for four days. Correlations
      between soreness and every other damage indicator were generally poor,
      and the authors concluded soreness is a poor reflector of damage and
      inflammation. This is the single most load-bearing consequence of the
      whole item.
    grade: B
  - note: >
      Mechanism is contested and the popular account is the weaker one. The
      standard story (micro-tears cause inflammation which causes pain) is
      undermined by rodent work in which mechanical hyperalgesia appeared
      1-3 days after lengthening contractions with no detectable microscopic
      damage and no signs of inflammation. Murase 2010 traces a different
      pathway: exercise releases bradykinin, which induces nerve growth
      factor, which sensitizes muscle nociceptors. This is causal, blockable
      evidence -- but it is animal evidence, and its transfer to human DOMS
      is inference. Both accounts are live; neither should be spoken as settled.
    grade: C
  - note: >
      Zombie stat, flagged rather than carried. Fitness-media sources
      circulate precise repeated-bout numbers ("a single bout reduces soreness
      from the next identical session by 60-80% for 6-8 weeks, protection
      lasting 6-9 months"). No peer-reviewed source in this sprint's search
      produced those figures. The repeated-bout effect itself is well
      established and reviewed in Hyldahl 2017, but the specific percentages
      and durations above are UNSOURCED and were deliberately excluded from
      the claim. Do not speak them.
    grade: D
  - note: >
      Lactic acid does not cause DOMS. This is not merely weakly supported --
      it is refuted and still in wide circulation. Lactate clears within
      roughly an hour of exercise, long before soreness onset. Same
      zombie-stat handling as the shrinkage figure on
      exercise/replication-power-crisis-005.
    grade: B
claim: >
  Delayed-onset muscle soreness follows a highly reproducible time course after
  unaccustomed or eccentrically biased work: onset around 12-24 h, peak around
  24-72 h, largely resolved by roughly 5-7 days. It is provoked mainly by
  eccentric (lengthening) and by NOVEL loading, not by effort or by lactate. A
  single prior bout confers substantial protection against soreness and damage
  markers from a subsequent similar bout -- the repeated-bout effect -- attributed
  to a combination of neural adaptation, altered muscle mechanical properties,
  extracellular-matrix remodelling and biochemical signalling. Two things the
  claim deliberately does NOT assert: (1) that soreness magnitude indicates
  how much damage, stimulus or adaptation occurred -- it correlates poorly with
  every objective damage marker; (2) that the micro-damage-then-inflammation
  chain is the established cause -- an alternative pathway (bradykinin inducing
  nerve growth factor, which sensitizes muscle nociceptors) has direct causal
  support in animal models, including hyperalgesia with no detectable damage
  and no signs of inflammation. The
  operative consequence: soreness is a sensation, not a training instrument.
  Steering load, volume or session spacing off how sore something feels is
  steering off a signal that does not track the thing being managed.
reasoning: >
  The timeline is the most-replicated observation in this literature and is
  consistent across hundreds of controlled eccentric-bout protocols; it carries
  the higher grade. The repeated-bout effect is likewise well established and is
  reviewed mechanistically by Hyldahl, Chen & Nosaka 2017 (Exerc Sport Sci Rev
  45(1):24-33), who propose that neural adaptations, changes to muscle mechanical
  properties, structural remodelling of the extracellular matrix and biochemical
  signalling act together; they are explicit that the mechanism is not resolved.
  The soreness-is-not-damage finding comes from Nosaka, Newton & Sacco 2002
  (Scand J Med Sci Sports 12(6):337-346, PMID 12453160), a 110-participant dose
  study across 12, 24 and 60 maximal eccentric elbow-flexor actions that tracked
  soreness against isometric force, relaxed and flexed joint angles, upper-arm
  circumference and plasma creatine kinase for four days and reported generally
  poor correlations throughout. The mechanism is where the field is genuinely
  split. Mizumura & Taguchi 2016 (J Physiol Sci 66(1):43-52) review evidence that
  nerve growth factor and GDNF mediate the mechanical hyperalgesia, and note the
  awkward observation that rats develop it 1-3 days after lengthening
  contractions without apparent microscopic damage or signs of inflammation.
  Murase et al. 2010 (J Neurosci 30(10):3752-3761) supply the causal chain --
  exercise-released bradykinin induces NGF, which sensitizes muscle nociceptors.
  That is stronger evidence than the classical account has, but it is rodent
  evidence, so the mechanism sits a rung lower than the timeline. Contested flag
  is set on the mechanism, not the timeline. Note the grading discipline
  inherited from sleep-recovery/grade-aasm-anchor-002: certainty of evidence and
  strength of recommendation are separate axes. The mechanism here is
  low-certainty, yet the practical instruction it supports -- do not use soreness
  as a training gauge -- rests on the SEPARATE, better-evidenced Nosaka
  correlation finding and is stated strongly on that basis, not on the mechanism.
---

# exercise/doms-timeline-mechanism-023

Muscle soreness after unfamiliar or eccentric-heavy work runs on a clock that
barely varies: it starts somewhere around 12 to 24 hours after the session,
peaks between 24 and 72 hours, and has mostly cleared by day five to seven. It
is provoked by lengthening contractions and by novelty, not by how hard the
session felt and not by lactate -- lactate is gone within about an hour, long
before the soreness arrives. Do one bout of the offending work and the next
similar bout hurts markedly less; that protective adaptation is real and
well documented, though the mechanism behind it is still argued over and the
precise "how much protection, for how long" numbers that circulate online are
not traceable to peer-reviewed sources and are not repeated here.

The part worth actually internalizing is what soreness is NOT. In a study of 110
men doing graded eccentric work, soreness correlated poorly with every objective
marker of muscle damage that was measured alongside it: force loss, swelling,
joint-angle changes, creatine kinase. You can be badly sore with little damage,
or substantially damaged with little soreness. Soreness is therefore not a
gauge of stimulus, not a gauge of damage, and not a gauge of readiness.

The cause is genuinely unsettled. The gym-floor story -- micro-tears, then
inflammation, then pain -- has an awkward problem: in animal experiments, muscles
become mechanically hyperalgesic one to three days after lengthening
contractions with no visible damage and no signs of inflammation. The competing
account traces a specific chemical chain instead: exercise releases bradykinin,
which induces nerve growth factor, which sensitizes the pain nerves in the
muscle. That chain has been demonstrated causally and can be blocked -- but in
rats, so carrying it over to human soreness is inference, not observation. Both
stories are live. Neither should be spoken as settled.

Practical consequence, and this one is stated firmly even though the mechanism
underneath is not: do not steer training off soreness. Choosing loads, cutting
volume, or re-spacing sessions because something still feels sore is steering
off a signal that has been directly measured not to track the state being
managed. What to steer off instead is covered in the recovery-kinetics item.

## Applicability check (2026-08-22) -- NOT adopted, implication only

Checked against `files/program/program.yaml`, `prep.yaml` and the owner's
session records. **No file was changed.** This item has no `prep.yaml`
implication at all -- it is not a drill-level finding. Its implication is for
how session FEEDBACK is interpreted, which is a behaviour question for the
owner's consult, not a data edit:

1. Soreness reports should not, on this evidence, drive load, volume or session
   spacing decisions. Soreness has been directly measured to correlate poorly
   with force loss, swelling and creatine kinase -- it is not a readout of the
   state being managed. If a soreness report ever gets treated as a fatigue
   signal in the retro or fast-path, that is a conflation this item argues
   against.
2. The rotation 앞A - 뒷A - 앞B - 뒷B means quad-dominant days (앞A, 앞B) and
   back days (뒷A, 뒷B) each recur with one session between them. Whether that
   spacing is adequate is a recovery-kinetics question, handled on
   exercise/recovery-kinetics-session-spacing-025, and it should be argued from
   proximity-to-failure and volume rather than from how sore anything feels.
3. Novelty is the DOMS driver, not effort. A newly introduced or newly
   re-weighted exercise should be expected to produce soreness once and much
   less thereafter, and that first-time soreness should not be read as the
   exercise being too much.
