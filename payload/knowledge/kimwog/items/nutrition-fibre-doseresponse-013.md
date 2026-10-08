---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). Partially fills the
# standing GAPS request for substantive diet claims graded THROUGH this lane's
# rules. Fibre was chosen over the other candidates named there (omega-3,
# vitamin D, added sugar, Mediterranean pattern) because it is the one with both
# a large prospective base AND a randomised arm, so the lane's observational
# discount can be applied against something rather than to everything.
# The jurisdiction-specific reference number is a SEPARATE item (locale KR).
id: nutrition/fibre-doseresponse-013
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 2019
contested: no
sources:
  - "https://doi.org/10.1016/S0140-6736(18)31809-9"  # Reynolds A, Mann J, Cummings J, Winter N, Mete E, Te Morenga L. Lancet 2019;393(10170):434-445. PMID 30638909 -- 185 prospective studies (just under 135 million person-years) plus 58 randomised trials (4635 participants)
  - "source:nutrition/observational-dominance-003 -- the lane rule applied to cap this claim"
  - "source:nutrition/grade-inadequate-position-006 -- the live dispute about how to certainty-rate exactly this class of evidence"
  - "framework:GRADE -- the source authors themselves graded the fibre evidence as moderate certainty, so the tool and its verdict are disclosed rather than re-derived"
applicability:
  axes:
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE SPLIT BETWEEN WHAT IS RANDOMISED AND WHAT IS NOT is the whole content of
      this item's grade. The disease and mortality outcomes are OBSERVATIONAL. The
      randomised arm covers intermediate markers only, showing lower body weight,
      systolic blood pressure and total cholesterol at higher intakes. Never speak
      the mortality figures with the causal confidence the trial arm earns.
    grade: C
  - note: >
      THIS CLAIM IS NOT CAPPED BY THE TINY-EFFECT RULE, and the reason should be
      stated rather than assumed. This lane caps relative risks around 0.95 to
      1.05 at the observational band for being indistinguishable from residual
      confounding. Reductions of 15 to 30 percent are an order of magnitude
      larger, sit on a monotonic dose-response, and are corroborated by a
      randomised arm on mechanistically adjacent markers. It stays at the
      observational band because it is observational, not because the effect is
      small.
    grade: C
  - note: >
      THE 25-29 g OPTIMUM IS A POPULATION FIGURE derived from where risk reduction
      across critical outcomes was greatest, and the dose-response curves suggest
      higher intakes may confer further benefit rather than plateauing there. It
      is not an individual requirement and not a ceiling. A jurisdiction-specific
      reference intake is a separate matter and is carried by the KR-locale item.
    grade: C
claim: >
  Higher dietary fibre intake is associated with substantially lower risk across
  several major outcomes, with risk reduction greatest at daily intakes between
  25 g and 29 g. Pooling 185 prospective studies covering just under 135 million
  person-years, comparing the highest fibre consumers with the lowest gives a 15
  to 30 percent lower rate of all-cause and cardiovascular mortality, coronary
  heart disease, stroke incidence and mortality, type 2 diabetes and colorectal
  cancer. In 58 randomised trials with 4635 participants, higher fibre intake
  produced significantly lower body weight, systolic blood pressure and total
  cholesterol. The source authors graded the certainty of the fibre evidence as
  moderate. Dose-response curves did not plateau at 25-29 g.
reasoning: >
  This is the strongest substantive diet claim available for this lane and it
  still lands at the observational band, which is the point of filing it. The
  effect sizes are far too large to fall under this lane's tiny-effect cap, the
  dose-response is monotonic and pre-specified, and there is a randomised arm.
  But the outcomes that matter, mortality and disease incidence, are all
  observational, and nutrition/observational-dominance-003 forbids letting
  concordant observational volume substitute for randomisation no matter how much
  of it there is. The randomised evidence covers intermediate markers only. The
  grading tool is disclosed rather than re-derived, per this lane's disclosure
  rule, and the source authors' own moderate-certainty verdict is carried
  forward. Not flagged contested: no competing body disputes the direction, and
  the methodology dispute about how to certainty-rate this class of evidence is
  already owned by nutrition/grade-inadequate-position-006 and is not re-fought
  here.
---

# nutrition/fibre-doseresponse-013

Fibre is the rare nutrition claim where both halves of the evidence exist. On the
observational side, 185 prospective studies covering close to 135 million
person-years show the highest fibre consumers running fifteen to thirty percent
below the lowest on all-cause mortality, cardiovascular death, coronary heart
disease, stroke, type 2 diabetes and colorectal cancer. On the randomised side,
58 trials show that raising fibre intake lowers body weight, systolic blood
pressure and total cholesterol. Risk reduction was greatest between twenty-five
and twenty-nine grams a day, and the curves did not flatten there.

The confidence band still sits at the observational level, and the reasoning
matters more than the placement. This lane caps very small relative risks because
they cannot be distinguished from leftover confounding. That is not the situation
here: the effects are large, they scale with dose, and a randomised arm points the
same way on related markers. What holds the claim down is simply that the
outcomes anyone actually cares about, dying and getting ill, were never
randomised. The trials measured markers, not endpoints.

Two boundaries to carry. The twenty-five to twenty-nine gram figure is a
population optimum, not a personal requirement and not a ceiling, and the data
hint that more may still be better. And a national reference intake is a
different kind of statement from an epidemiological optimum; the Korean figure is
held in its own jurisdiction-scoped item rather than blended in here.
