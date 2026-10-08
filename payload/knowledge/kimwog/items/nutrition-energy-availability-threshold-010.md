---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). A consumer holding
# both a meal log and a training log can compute energy availability, so it will.
# This item exists to stop it treating the computed number as a diagnosis. The
# governing body that popularised the threshold has itself walked it back in
# print, and that walk-back is quoted from the primary consensus document.
id: nutrition/energy-availability-threshold-010
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 2003-2026
contested: yes
sources:
  - "https://doi.org/10.1136/bjsports-2023-106994"  # Mountjoy M, Ackerman KE, Bailey DM, Burke LM, Constantini N, Hackney AC, Heikura IA, et al. 2023 IOC consensus statement on Relative Energy Deficiency in Sport (REDs). Br J Sports Med 2023;57:1073-1097. PMID 37752011
  - "https://doi.org/10.1210/jc.2002-020369"  # Loucks AB, Thuma JR. J Clin Endocrinol Metab 2003;88(1):297-311. PMID 12519869 -- the ORIGIN trial: n=29 sedentary regularly menstruating young women, 5 days per condition
  - "https://doi.org/10.1123/ijsnem.2018-0142"  # Burke LM, Lundy B, Fahrenholtz IL, Melin AK. Int J Sport Nutr Exerc Metab 2018;28(4):350-363. PMID 30029584 -- pitfalls of estimating energy availability in free-living athletes
  - "https://doi.org/10.1007/s40279-026-02526-0"  # Walker AE, McKay AKA, Rogers MA, Kuikman MA, Ackerman KE, Stellingwerff T, Burke LM. Sports Med 2026. PMID 42645681 -- standardised audit of 203 publications
  - "source:nutrition/self-report-underreporting-007 -- the error in the energy-intake term of the equation"
applicability:
  axes:
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      QUOTE-LEVEL PROVENANCE, because this is the load-bearing part. The 2023 IOC
      consensus statement describes the threshold as based on "elegant but
      short-term laboratory studies" in "a small sample of sedentary females",
      states the concept "was intended as a guide, rather than a diagnostic
      end-point", and concludes there "are risks in setting a definitive clinical
      threshold of EA due to many moderating factors". The body that owns the
      construct has withdrawn the cut-off reading in print.
    grade: B
  - note: >
      THE INPUTS ARE WORSE THAN THE THRESHOLD. Energy availability is intake minus
      exercise expenditure, divided by fat-free mass, and every one of the three
      terms is estimated with substantial error in free-living conditions. In the
      audited literature, 82 percent of observational energy-availability studies
      obtained intake from food records and 40 percent obtained exercise
      expenditure from metabolic-equivalent scores. A number assembled from a
      consumer meal log plus an activity estimate plus a bioimpedance fat-free
      mass carries all three errors at once and is not comparable to a laboratory
      value.
    grade: B
  - note: >
      SEX ASYMMETRY. The threshold originates entirely in female physiology. The
      consensus statement reports that the corresponding range for males is less
      understood and appears LOWER, around 9 to 25 kcal per kg fat-free mass per
      day, and that most males sustain a lower level before disturbance appears.
      Speaking the female-derived number to a male user is a category error.
    grade: C
claim: >
  The widely used low-energy-availability threshold of 30 kcal per kg fat-free
  mass per day is not a diagnostic cut-off. It originates in short-term
  laboratory work in a small sample of sedentary young women, where luteinizing
  hormone pulsatility was disrupted below that level over 5-day exposures
  (n=29). The 2023 IOC consensus statement that governs the construct states the
  concept was intended as a guide rather than a diagnostic end-point and that
  there are risks in setting a definitive clinical threshold, and it treats low
  energy availability as a spectrum from adaptable to problematic. The
  corresponding range for males is less understood and appears lower. Separately,
  every input to the energy-availability equation is estimated with large error
  in free-living conditions.
reasoning: >
  Two independent failure modes stack here, which is why the claim sits at the
  observational band with a contested flag despite resting on a governing-body
  consensus document. First, the threshold's provenance is thin relative to how
  it is used: a 5-day laboratory manipulation in 29 sedentary women, generalised
  to free-living athletes of both sexes and all training states. Second, and
  more decisive for a consumer application, the measurement is not achievable
  outside a laboratory: the intake term inherits the full self-report bias
  documented in nutrition/self-report-underreporting-007, the expenditure term
  is usually a metabolic-equivalent estimate, and the fat-free-mass denominator
  is device-dependent. The consensus statement itself names the errors in intake,
  exercise expenditure, fat-free mass and resting metabolic rate as an open
  methodological problem. The operational rule that follows is narrow and firm:
  energy availability computed from a consumer log may be used as a direction and
  a prompt to ask, never as a threshold crossing and never as a diagnosis.
---

# nutrition/energy-availability-threshold-010

Thirty kilocalories per kilogram of fat-free mass per day is the number everyone
quotes as the line below which a person is under-fuelling. It comes from a
laboratory experiment in which twenty-nine sedentary young women spent five days
at each of several controlled intake levels and their reproductive hormone
pulsing was disrupted below that point. That is careful work, and it is a very
long way from a diagnostic threshold for a free-living adult of either sex.

The organisation that popularised the number has said so itself. Its 2023
consensus statement describes the underlying studies as elegant but short-term
and conducted in a small sample of sedentary females, says the concept was meant
as a guide and not an end-point, and warns of the risks of setting a definitive
clinical threshold. It also reports that the equivalent range for men appears
lower, roughly nine to twenty-five, and is much less well understood. Low
availability is now framed as a spectrum running from adaptable to problematic
rather than as a line to be crossed.

For anything computing this from a phone, the deeper problem is not the threshold
but the arithmetic feeding it. The calculation needs energy intake, exercise
energy expenditure and fat-free mass. In a consumer setting the first comes from
a meal log that systematically understates intake, the second from an activity
estimate, and the third from a body-composition device with its own bias. Three
estimates with three errors produce a figure that cannot be compared against a
laboratory-derived cut-off. The number is usable as a direction of travel and as
a reason to ask a question. It is not usable as a verdict.
