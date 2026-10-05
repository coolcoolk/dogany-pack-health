---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The domain's anchor row, and the one that had to be written first: the sleep
# lane already carries a melatonin item built on the AASM's 2015 circadian
# guideline, and a session reading that item will assume it covers jet lag. It
# does not. The 2015 guideline states in its own text that jet lag is out of
# scope. The standing AASM position on jet lag is a 2007 practice parameter on
# a different grading ladder, and knowing that is the difference between citing
# a guideline and inventing one.
id: travel/jet-lag-guideline-standing-001
domain: travel
lane: "@travel-clinical"
grade: B (what the standing guideline recommends and at what tier); C (whether those recommendations still reflect the 2026 evidence base)
locale: universal
as_of: 2007
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/18041479/"  # Morgenthaler TI, Lee-Chiong T, Alessi C, Friedman L, Aurora RN, Boehlecke B, Brown T, Chesson AL Jr, Kapur V, Maganti R, Owens J, Pancer J, Swick TJ, Zak R; Standards of Practice Committee of the AASM. 2007, Sleep 30(11):1445-1459, doi 10.1093/sleep/30.11.1445, PMCID PMC2082098 -- the standing AASM practice parameter covering jet lag disorder. Abstract read verbatim 2026-09-02
  - "https://pubmed.ncbi.nlm.nih.gov/26414986/"  # Auger RR, Burgess HJ, Emens JS, Deriy LV, Thomas SM, Sharkey KM. 2015, J Clin Sleep Med 11(10):1199-1236, doi 10.5664/jcsm.5100, PMCID PMC4582061 -- the 2015 AASM circadian guideline. Full text read at PMC 2026-09-02 for the SCOPE statement, which is the load-bearing part here
  - "source:sleep-recovery/melatonin-chronobiotic-not-hypnotic-008 -- the sleep lane's melatonin item. It is built on the 2015 guideline and is therefore NOT about jet lag; this item is the fence between them"
  - "source:sleep-recovery/grade-aasm-anchor-002 -- certainty versus recommendation strength. Note that the 2007 parameter uses a DIFFERENT ladder from the one that item describes"
  - "framework:AASM Standard/Guideline/Option (Eddy) -- the 2007 practice parameter grades on the older three-tier ladder, where Standard is the highest tier and Option the lowest. The 2015 and 2017 AASM documents that this warehouse otherwise cites use GRADE. The two ladders are NOT interchangeable and a Standard on the 2007 ladder must never be spoken as a STRONG GRADE recommendation."
applicability:
  axes:
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE 2015 GUIDELINE EXCLUDES JET LAG IN ITS OWN WORDS. Its text states that
      the extrinsic or predominantly environmentally influenced circadian rhythm
      sleep-wake disorders, namely shift work and jet lag disorder, are not
      addressed in that paper. So the sleep lane's melatonin item -- which rests
      on the 2015 document -- carries NOTHING about jet lag, and must not be
      quoted as if it did. This was checked at full text specifically because a
      cross-domain misread was the likely failure.
    grade: A
  - note: >
      THE LADDER IS NOT THE ONE THIS WAREHOUSE USUALLY USES. The 2007 parameter
      grades recommendations Standard / Guideline / Option, the older AASM
      ladder. Every other AASM document cited in this warehouse uses GRADE, where
      the words are STRONG and WEAK and they mean something different. A Standard
      on the 2007 ladder is the top tier of that ladder; it is not a GRADE STRONG
      recommendation and should not be reported as one.
    grade: A
  - note: >
      WHAT THE 2007 PARAMETER ACTUALLY SAYS ABOUT JET LAG, quoted rather than
      paraphrased. Timed melatonin administration is indicated for jet lag
      disorder (Standard). Planned or prescribed sleep schedules are indicated in
      jet lag disorder (Option). Specifically dosed and timed light exposure is
      indicated for each of the circadian disorders with variable success
      (Option). Hypnotic medications may be indicated to treat jet lag-induced
      insomnia (Option). Stimulants may be indicated to improve alertness in jet
      lag disorder (Option) but may have risks that must be weighed prior to use.
      Note the ordering that falls out of this: the intervention with the
      strongest guideline backing is the timed one.
    grade: A
  - note: >
      THE DOCUMENT IS FROM 2007 AND HAS NOT BEEN SUPERSEDED FOR JET LAG. That is
      a finding, not an oversight to paper over. Nineteen years is a long time to
      leave a recommendation standing, and the 2015 update deliberately declined
      to revisit it. Speak the recommendations as what the field's standard-setting
      body has on the books, not as a current reading of the 2026 evidence. The
      same edition discipline the finance and cooking lanes were built on applies
      here: a jurisdiction-bound or body-bound statement needs an edition check.
    grade: B
  - note: >
      NO DOSE, NO SCHEDULE, NO PRODUCT. The 2007 parameter's melatonin
      recommendation is for TIMED administration, and this warehouse deliberately
      carries neither the timing table nor any milligram figure. Deciding what a
      specific traveller takes and when is a clinical act; recording that the
      guideline endorses timed melatonin for this indication is not. Everything
      downstream of "the guideline endorses it" belongs to a clinician, and the
      chronobiology item in this lane carries the direction logic without any
      drug attached.
    grade: A
claim: >
  The American Academy of Sleep Medicine's standing position on jet lag disorder
  is its 2007 practice parameter, not its 2015 circadian guideline. The 2015
  document states in its own text that shift work and jet lag disorder, being the
  extrinsic circadian rhythm sleep-wake disorders, are not addressed in it. The
  2007 parameter, graded on the older Standard / Guideline / Option ladder, says:
  timed melatonin administration is indicated for jet lag disorder (Standard);
  planned or prescribed sleep schedules are indicated in jet lag disorder
  (Option); specifically dosed and timed light exposure is indicated for each of
  the circadian disorders with variable success (Option); hypnotic medications may
  be indicated to treat jet lag-induced insomnia (Option); and stimulants may be
  indicated to improve alertness in jet lag disorder (Option) but may have risks
  that must be weighed prior to use. Two consequences follow. The strongest
  guideline-backed jet lag intervention is a TIMED one, which is the same
  chronobiotic-not-hypnotic logic the sleep lane records for melatonin generally.
  And the recommendation set is nineteen years old and was passed over rather than
  refreshed, so it should be spoken as what is on the books and not as a current
  reading of the evidence.
reasoning: >
  This item exists because of a specific cross-domain trap that this warehouse was
  already exposed to. The sleep lane carries a well-built melatonin item resting
  on the AASM's 2015 circadian guideline, and any reasonable reader would assume
  a guideline about circadian rhythm sleep-wake disorders covers the most common
  circadian complaint there is. It does not, and the 2015 text was read at full
  text specifically to confirm the exclusion rather than infer it from an absence
  in the abstract. Confidence about what the standing parameter recommends sits in
  the solid band because the recommendations were read verbatim from the source
  record and are unambiguous. Confidence about whether those recommendations still
  represent the evidence is graded a band lower on purpose: the document is from
  2007, the body that owns it has since published two circadian-adjacent
  guidelines without revisiting jet lag, and no serious reader should treat a
  nineteen-year-old recommendation as a current verdict. The grading-ladder note
  is not pedantry. This warehouse's other AASM items describe GRADE, where STRONG
  and WEAK carry defined meanings about certainty; the 2007 parameter uses the
  older three-tier Eddy ladder, and collapsing "Standard" into "strong evidence"
  is exactly the kind of quiet upgrade the warehouse's grading discipline exists
  to stop. What this item deliberately does not do is convert a guideline
  endorsement into an instruction. It records that timed melatonin has the
  strongest backing of the listed options and stops there, because the next step
  -- how much, when, for whom -- is a clinical decision and this is a warehouse,
  not a clinic.
---

# travel/jet-lag-guideline-standing-001

There is a guideline on jet lag, and it is not the one you would reach for.

The American Academy of Sleep Medicine published a clinical practice guideline on
circadian rhythm sleep-wake disorders in 2015, and the sleep domain of this
warehouse leans on it for melatonin. That document says, in its own introduction,
that the extrinsic circadian disorders -- shift work and jet lag -- are not
addressed in it. Whatever it concludes about melatonin, it concludes about
delayed sleep phase and free-running rhythm and the like. Not about flying to
Frankfurt.

The standing position on jet lag is a practice parameter from 2007. It grades on
the academy's older ladder, where the tiers are Standard, Guideline and Option,
Standard being the top. On jet lag disorder it says:

- Timed melatonin administration is indicated (Standard).
- Planned or prescribed sleep schedules are indicated (Option).
- Specifically dosed and timed light exposure is indicated for each of the
  circadian disorders with variable success (Option).
- Hypnotic medications may be indicated to treat jet lag-induced insomnia
  (Option).
- Stimulants may be indicated to improve alertness (Option), but may have risks
  that must be weighed before use.

Two things are worth pulling out of that list.

The first is the shape of it. The item at the top tier is a timed one. That is
the same finding the sleep domain records about melatonin in general -- it works
as a clock signal, not as a sedative -- arriving here from a completely different
document. The intervention with the strongest backing is the one where the
timing is the active ingredient.

The second is the date. This is a 2007 document, and it is still the standing
recommendation because the 2015 update looked at circadian disorders and decided
jet lag was out of scope. That is not a scandal, but it is a fact that has to
travel with the recommendations. Nineteen years is long enough that "the
guideline says" and "the evidence shows" have come apart, and only the first of
those two claims is safe here.

One boundary, stated plainly because this is the point where a travel question
turns into a medical one. This warehouse carries the fact that timed melatonin is
the endorsed jet-lag intervention. It carries no dose, no schedule and no
product. The word doing all the work in the recommendation is "timed," and
deciding a specific person's timing and amount is a clinician's job. The
chronobiology item in this lane carries the direction logic -- which way the
clock needs to move and what moves it -- without any drug attached to it, and
that is as far as an assistant should go on its own.
