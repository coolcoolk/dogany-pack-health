---
# Collection sprint 2026-09-02 (mental-health lane expansion). The lane's
# boundary item, authored deliberately as a MEASUREMENT-LIMITATION finding and
# not as a screening instruction. It exists so that a self-report score -- from a
# questionnaire, a mood log, a daily check-in -- can never be converted into a
# statement about a person's state. It is also the item that makes the domain's
# refusal to do screening a sourced position rather than a policy preference.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/screening-score-is-not-a-diagnosis-011
domain: mental-health
grade: "A (that symptom-questionnaire cut-offs systematically over-identify relative to diagnostic interviews, and by how much)"
lane: "@clinical"
locale: universal
as_of: 2019
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/30967483/"  # Levis B, Benedetti A, Thombs BD, DEPRESsion Screening Data (DEPRESSD) Collaboration. 2019, BMJ 365:l1476, doi 10.1136/bmj.l1476, PMCID PMC6454318, PROSPERO CRD42014010673 -- individual participant data meta-analysis, 58 of 72 eligible studies, n=17357, 2312 major depression cases. Erratum BMJ 2019;365:l1781
  - "https://pubmed.ncbi.nlm.nih.gov/30894161/"  # Levis B, Yan XW, He C, Sun Y, Benedetti A, Thombs BD. 2019, BMC Med 17(1):65, doi 10.1186/s12916-019-1297-6, PMCID PMC6427845 -- meta-research review of 69 meta-analyses, 81 pooled prevalence estimates, 2094 primary studies
  - "mental-health/grade-clinical-meaningfulness-002"  # the domain's rule that a number's statistical behaviour is not the same as its meaning
  - "nutrition/self-report-underreporting-007"  # the warehouse's existing companion finding on what self-report instruments do to a measured quantity
  - "framework:GRADE -- an individual participant data meta-analysis of diagnostic accuracy against a semistructured reference standard is the strongest design available for this question, and the accompanying meta-research review measures the consequence of ignoring it. Both are graded at the top band."
refraction_notes:
  - note: >
      The accuracy numbers, stated exactly, because they are usually quoted
      without their reference standard. Against SEMISTRUCTURED diagnostic
      interviews, the PHQ-9 at a cut-off of 10 or above maximised combined
      accuracy with sensitivity 0.88 (95 percent CI 0.83 to 0.92) and specificity
      0.85 (0.82 to 0.88), across 29 studies and 6725 participants. Sensitivity
      was 5 to 22 percent LOWER when the reference standard was a fully
      structured interview and 2 to 15 percent lower against the MINI. So even
      the headline accuracy figure is conditional on which interview it was
      measured against -- a detail almost always dropped in retelling.
    grade: A
  - note: >
      The consequence, which is the load-bearing half. Across 69 meta-analyses
      reporting pooled depression prevalence, estimates based on SCREENING TOOLS
      OR RATING SCALES came out at 31 percent, combined-method estimates at 22
      percent, and estimates based on DIAGNOSTIC INTERVIEWS at 17 percent. Of
      2094 primary studies pooled, only 277 (13 percent) used a validated
      diagnostic interview while 1604 (77 percent) used a screening or rating
      tool. The method was accurately described in the abstract for only 17 of
      81 prevalence estimates (21 percent), and 52 of 73 questionnaire-based or
      mixed-method meta-analyses nonetheless described their result as the
      prevalence of "depression" or "depressive disorders".
    grade: A
  - note: >
      Why the inflation is arithmetic and not sloppiness. At specificity 0.85, a
      questionnaire misclassifies roughly 15 percent of people who do not have
      the condition as screening positive. When the true prevalence is low, those
      false positives outnumber the true positives, and a cut-off count therefore
      overestimates by construction. This is a property of the instrument, not a
      flaw in any particular study, and it does not go away with a larger sample.
    grade: A
  - note: >
      SCOPE, and it is the reason this item is authored at all. This is a fact
      about what a number means. It is NOT an instruction to administer a
      questionnaire, and no cut-off recorded here may be applied to anyone. The
      operative rule for an assistant is the negative one: a self-reported score,
      a mood log entry, a check-in rating, or any threshold crossed in tracked
      data is a measurement with known error and no diagnostic content, and must
      never be spoken as a claim about the person's state or condition.
    grade: A
  - note: >
      Generalises beyond the specific instrument. The mechanism -- a
      symptom-count threshold standing in for a structured clinical assessment --
      is identical for any brief self-report scale, including whatever ad hoc
      daily rating a tracking system happens to collect. An ad hoc rating is in
      fact worse off: it has no validation study behind it at all, so its
      sensitivity and specificity against any reference standard are simply
      unknown rather than merely imperfect.
    grade: A
claim: >
  A symptom questionnaire score is a measurement with known error, not a
  statement about whether someone has a condition, and treating it as the latter
  inflates counts by roughly a factor of two. Two linked sources establish this.
  On accuracy: an individual participant data meta-analysis (Levis, Benedetti,
  Thombs and the DEPRESSD Collaboration 2019, BMJ, 58 studies, n=17357, 2312
  cases) found the PHQ-9 at a cut-off of 10 or above maximised combined accuracy
  at sensitivity 0.88 (95 percent CI 0.83 to 0.92) and specificity 0.85 (0.82 to
  0.88) against semistructured diagnostic interviews, with sensitivity 5 to 22
  percent lower when measured against fully structured interviews. On
  consequence: a meta-research review by the same group (Levis et al. 2019, BMC
  Medicine, 69 meta-analyses, 81 pooled estimates, 2094 primary studies) found
  pooled prevalence of 31 percent when primary studies used screening or rating
  tools, 22 percent for mixed methods, and 17 percent when diagnostic interviews
  were used; 77 percent of pooled primary studies used a questionnaire rather
  than an interview, the method was accurately stated in only 21 percent of
  abstracts, and 52 of 73 questionnaire-based reviews still called their result
  the prevalence of "depression". The inflation is arithmetic: at 85 percent
  specificity, false positives outnumber true positives whenever true prevalence
  is low. The operative rule for an assistant is entirely negative -- no
  self-reported score, tracked threshold or check-in rating may be converted
  into a claim about a person's state, and an unvalidated ad hoc daily rating is
  worse off than a validated instrument, not better, because its error is
  unknown rather than merely quantified.
reasoning: >
  This lane sits inside an assistant that will routinely hold self-reported
  numbers about how someone says they are doing, and the single most damaging
  thing it could do with them is read them as evidence of a condition. This item
  makes that refusal a sourced position instead of a house rule. The two Levis
  papers were selected together deliberately: the BMJ paper establishes the
  instrument's error rate under the strongest available design, and the BMC
  Medicine paper measures what happens downstream when that error rate is
  ignored, which is a published, quantified, factor-of-roughly-two inflation in
  the literature itself. Having both means the item can state not only that a
  score is not a diagnosis but by how much the field gets this wrong in print.
  Graded at the top band: an individual participant data meta-analysis against a
  semistructured reference standard is the ceiling of design quality for
  diagnostic accuracy, and the meta-research review is a census rather than an
  estimate. Not flagged contested; no source located disputes either finding, and
  the direction of the error is a mathematical property of specificity rather
  than an empirical claim that could be overturned. Authored strictly as a
  measurement-limitation item with the scope note graded at the top band, so that
  no part of it can be read as an instruction to screen anybody. The generalising
  note is included because the practical case in this warehouse is not a clinician
  administering a validated scale; it is a tracking system collecting an ad hoc
  daily number, which has no validation behind it at all.
---

# mental-health/screening-score-is-not-a-diagnosis-011

A questionnaire score is a measurement. It has error, the error has been
measured, and when the error is ignored the resulting counts come out roughly
twice as large as they should.

The accuracy first, with the detail that usually goes missing. Pooled across 58
studies and more than seventeen thousand participants, the most widely used
depression questionnaire at its standard threshold catches about 88 percent of
people who would be identified by a careful clinical interview, and correctly
clears about 85 percent of those who would not. Those figures are conditional on
which kind of interview was used as the yardstick -- against a briefer, fully
structured interview the sensitivity drops by up to 22 percentage points. The
number and its reference standard are one object, and quoting the number alone is
already an error.

Now the part that matters more.

The same group went looking at what happens when the field forgets this. Across
69 meta-analyses that reported a pooled prevalence of depression: reviews built
on questionnaires reported 31 percent, reviews built on mixed methods 22 percent,
and reviews built on actual diagnostic interviews 17 percent. Of the two thousand
or so primary studies inside those pooled estimates, only 13 percent had used a
diagnostic interview. Around three quarters had used a questionnaire.

And the reporting: only about one in five of those pooled estimates accurately
described in its own abstract what had been pooled. Most of the reviews built on
questionnaires nevertheless called the result the prevalence of "depression" or
"depressive disorders" -- of disorders that had never been assessed.

The inflation is not carelessness in the individual studies. It is arithmetic.
At 85 percent specificity, fifteen out of every hundred people who do not have
the condition still cross the threshold. When the condition is uncommon, those
false positives outnumber the true ones, and a threshold count therefore
overshoots by construction. A bigger sample makes the overshoot more precise, not
smaller.

What this means here is narrow and entirely negative, and it should be read that
way.

This item is not a reason to hand anyone a questionnaire. No threshold recorded
here is to be applied to a person. What it establishes is the opposite: any
self-reported number -- a score, a mood log, a daily check-in, a threshold crossed
in tracked data -- is a measurement with error and no diagnostic content, and
cannot be converted into a statement about what someone has or is.

And the case that actually arises in a system like this one is worse than the
case studied. The instrument above at least has fifty-eight validation studies
behind it. A rating a tracking system invents for itself has none, so its
sensitivity and specificity against anything are not merely imperfect -- they are
unknown. Fewer validation studies never means more license.
