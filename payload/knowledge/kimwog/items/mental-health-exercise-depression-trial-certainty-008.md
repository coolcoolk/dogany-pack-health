---
# Collection sprint 2026-09-02 (mental-health lane expansion). The single most
# repeated mental-health claim a life agent will ever be tempted to make --
# "exercise helps depression" -- and the one whose evidence base is most
# routinely overstated. The largest network meta-analysis in the area found
# real effects AND reported that exactly one of its 218 trials met the Cochrane
# low-risk-of-bias criteria. This item exists so the effect and its certainty
# are never separated. Sits on the domain's existing grading anchors 002 and
# 003 (clinical meaningfulness, and no single hierarchy) and is a worked
# example of the downgrade trigger recorded on 007.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/exercise-depression-trial-certainty-008
domain: mental-health
grade: "B (that structured exercise reduces depressive symptoms relative to active controls in trial populations); D (any specific effect size, any ranking between exercise modalities, any comparison against other treatments)"
lane: "@clinical"
locale: universal
as_of: 2024
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/38355154/"  # Noetel M, Sanders T, Gallardo-Gomez D, Taylor P, Del Pozo Cruz B, van den Hoek D, Smith JJ, Mahoney J, Spathis J, Moresi M, Pagano R, Pagano L, Vasconcellos R, Arnott H, Varley B, Parker P, Biddle S, Lonsdale C. 2024, BMJ 384:e075847, doi 10.1136/bmj-2023-075847, PMCID PMC10870815 -- systematic review and network meta-analysis, 218 unique studies, 495 arms, 14170 participants, PROSPERO CRD42018118040 <!-- estate-scrub:allow(author surname Smith, not an instance) -->
  - "https://doi.org/10.1136/bmj.q1024"  # published correction to the above, BMJ 2024;385:q1024, 28 May 2024 -- the effect-size standardisation was changed to use the baseline standard deviation; the authors state this did not lead to material changes in the findings
  - "mental-health/grade-clinical-meaningfulness-002"  # the rule this item is a worked example of -- statistical significance is not sufficient for a top band
  - "mental-health/curator-checklist-007"  # the downgrade triggers applied here
  - "framework:CINeMA -- the review graded confidence with the Confidence In Network Meta-Analysis tool rather than asserting certainty. That grading, not the point estimate, is the load-bearing part of this item."
applicability:
  axes:
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The effects, stated exactly. Compared with ACTIVE controls (usual care, a
      placebo tablet), Hedges' g was -0.62 for walking or jogging (n=1210,
      51 studies), -0.55 for yoga (n=1047, 33 studies), -0.49 for strength
      training (n=643, 22 studies), -0.43 for mixed aerobic exercise (n=1286,
      51 studies) and -0.42 for tai chi or qigong (n=343, 12 studies). Effects
      were proportional to prescribed intensity. Yoga and strength training were
      the best tolerated. Results appeared robust to publication bias.
    grade: B
  - note: >
      The sentence that governs every use of those numbers, from the review's
      own results section: ONLY ONE STUDY out of 218 met the Cochrane criteria
      for low risk of bias. Confidence under CINeMA was accordingly LOW for
      walking or jogging and VERY LOW for every other modality. A point estimate
      carried at very low confidence is a direction, not a magnitude, and must
      never be spoken as a number.
    grade: A
  - note: >
      Population gate, and it is the one most often ignored. Every included
      trial recruited participants meeting CLINICAL CUT-OFFS FOR MAJOR
      DEPRESSION. This is not evidence about a flat day, a bad week, or ordinary
      low mood, and transferring it there is a category error of exactly the
      kind the sleep domain flags on its own clinical-guideline item.
    grade: A
  - note: >
      Blinding, which is where the contested flag comes from. Participants in an
      exercise trial know they are exercising and know the control group is not.
      The review's own authors name this and recommend that future studies try to
      blind participants and staff to mitigate expectancy effects. In a
      literature where the outcome is a self-reported symptom score and the
      participant cannot be blinded, an unblinded effect of this size is
      compatible with a substantial expectancy component. This is the same
      structural limit the domain's no-single-hierarchy item records for
      psychological interventions generally.
    grade: A
  - note: >
      DO NOT carry any head-to-head ranking out of this review. The network
      included psychotherapy and antidepressant arms, and it is tempting to read
      off a league table. At LOW-to-VERY-LOW confidence across a network with one
      low-risk-of-bias trial in it, any statement of the form "exercise is as
      good as X" is not supported at usable certainty and must not be spoken.
      Comparative treatment claims are also outside what this warehouse is for.
    grade: D
  - note: >
      A published correction exists (BMJ 2024;385:q1024, 28 May 2024): the
      standardisation of effect sizes was changed to use the baseline standard
      deviation, with the authors stating the change did not materially alter
      the findings. Recorded so a later sprint meeting the correction does not
      mistake it for a retraction, and so the corrected version is the one cited.
    grade: A
claim: >
  Structured exercise reduces depressive symptoms in people who meet clinical
  cut-offs for major depression, and the size of that reduction is not knowable
  from the current literature. The largest synthesis available (Noetel et al.
  2024, BMJ, 218 unique studies, 495 arms, 14170 participants) reports moderate
  reductions against ACTIVE controls for walking or jogging (Hedges' g -0.62,
  95 percent credible interval -0.80 to -0.45), yoga (-0.55), strength training
  (-0.49), mixed aerobic exercise (-0.43) and tai chi or qigong (-0.42), with
  effects proportional to prescribed intensity and yoga and strength training
  best tolerated. The same review reports that exactly ONE of its 218 studies
  met the Cochrane criteria for low risk of bias, and that confidence assessed
  with CINeMA was LOW for walking or jogging and VERY LOW for every other
  modality. Participants in exercise trials cannot be blinded and the outcome is
  a self-reported symptom score, so an expectancy component cannot be separated
  out; the authors themselves recommend future blinding. The operative
  consequence: the DIRECTION of the finding is usable and the MAGNITUDE is not,
  no modality ranking may be read off the network, no comparison against other
  treatments may be carried out of it, and none of it transfers to ordinary low
  mood in someone who does not meet a clinical threshold.
reasoning: >
  This is the claim a generalist life agent is most likely to make and most
  likely to overstate, so it is authored as a certainty item rather than as an
  effect-size item. The source is the field's largest and most recent network
  meta-analysis, identified through PubMed and read at abstract and results
  level, with its published correction resolved separately. Two things in it
  point in opposite directions and both are true: the pooled effects are real
  and moderate in size, and the evidence supporting them is graded low to very
  low confidence by the authors' own formal assessment, resting on a literature
  in which a single trial out of 218 reached low risk of bias. The domain's
  existing rule item 002 already states that statistical significance is
  explicitly insufficient for a top band and that RCT evidence is downgraded for
  limitations, inconsistency, indirectness, imprecision and reporting bias; this
  is that rule meeting its most popular test case. The domain's item 003 already
  records that blinding is often impossible for psychological interventions,
  which is the mechanism by which an unblinded exercise trial inflates a
  self-reported outcome. Flagged contested because the gap between how
  confidently this finding is repeated in public and how confidently its own
  authors graded it is the largest in this lane. Graded at the trial band for
  direction and at the practitioner floor for any number, ranking or
  cross-treatment comparison, so that the answer path can say the useful true
  thing without reciting a figure the literature cannot support. The
  observational partner to this item is 009, which answers a different question
  and must not be merged with it.
---

# mental-health/exercise-depression-trial-certainty-008

The claim that exercise helps depression is true in direction and unknown in
size, and almost everyone who repeats it collapses those two facts into one.

The largest synthesis to date pooled 218 trials, 495 treatment arms and 14170
participants. Against active controls -- usual care, a placebo tablet -- it found
moderate reductions in depressive symptoms for walking or jogging, yoga, strength
training, mixed aerobic exercise, and tai chi or qigong, in roughly that order,
with bigger effects at higher prescribed intensity. Yoga and strength training
were the ones people stayed with.

Then the same paper says the thing that governs all of it. Of those 218 studies,
one met the Cochrane criteria for low risk of bias. One. The authors' own formal
confidence assessment came out low for walking or jogging and very low for
everything else.

That is not a footnote. It is the finding. A number carried at very low
confidence is a direction with a decimal point attached, and repeating the
decimal point is the error.

There is a structural reason the numbers are soft here, and it is not
carelessness. Nobody can be blinded to whether they have been exercising. The
outcome is a symptom questionnaire the participant fills in themselves. Someone
who has just completed twelve weeks of a programme they believe is helping is
being asked to rate whether they feel better. The review's authors say so
directly and recommend that future trials try to blind participants and staff.
Until that happens, an unblinded effect of this size is fully compatible with a
large expectancy component sitting inside it.

Two boundaries that must travel with the finding.

The first is population. Every one of these trials recruited people who met
clinical cut-offs for major depression. This is treatment evidence about a
diagnosed condition. It is not evidence about a flat Tuesday, and stretching it
to cover one is the same category error the sleep domain records when a chronic
insomnia guideline gets applied to someone who simply wants to sleep better.

The second is comparison. The network contained psychotherapy and medication
arms, and the temptation to read off a league table is strong. Do not. At this
confidence level, across a network with a single low-risk trial in it, no
statement of the form "as effective as" survives contact with the certainty
rating -- and treatment-versus-treatment questions are not what this warehouse
is for in the first place.

What is left after all that is still worth having, and it is worth having stated
plainly rather than dressed up: in people being treated for depression, moving
consistently is associated with feeling better in trials, more so when the
movement is more intense, and the strength of that evidence is weak enough that
nobody should be quoting a percentage.
