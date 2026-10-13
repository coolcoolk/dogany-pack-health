---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). Deliberate
# structural echo of sleep-recovery/tracker-accuracy-003 and
# exercise/increment-verification-floor-029: an instrument-limit item that bounds
# what any body-composition reading can confirm, filed in the domain whose
# consumer reads the instrument daily.
id: nutrition/body-composition-measurement-floor-011
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2012-2025
contested: no
sources:
  - "https://doi.org/10.1249/MSS.0b013e318228b60e"  # Nana A, Slater GJ, Hopkins WG, Burke LM. Med Sci Sports Exerc 2012;44(1):180-189. PMID 22179140 -- five scans over two days in 31 active adults; daily activity and a single breakfast substantially raised typical error and shifted mean lean mass
  - "https://doi.org/10.1123/ijsnem.2013-0228"  # Nana A, Slater GJ, Stewart AD, Burke LM. Int J Sport Nutr Exerc Metab 2015;25(2):198-215. PMID 25029265 -- best-practice standardisation: rested, overnight-fasted, minimal clothing, fixed positioning
  - "https://doi.org/10.1038/s41430-025-01664-4"  # Potter AW, Ward LC, Chapman CL, Tharion WJ, Looney DP, Friedl KE. Eur J Clin Nutr 2025;79:1235-1244. PMID 40957934, PMC12678178 -- multi-frequency bioimpedance (InBody 770) vs DXA in 1000 adults under real-world uncontrolled conditions
  - "source:sleep-recovery/tracker-accuracy-003 -- in-warehouse precedent for an instrument-limit item bounding a consumer device"
applicability:
  axes:
    - key: body_fat_pct
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      RELIABILITY IS NOT ACCURACY, and conflating them is the specific error a
      consumer device invites. In the 1000-adult comparison the bioimpedance
      device was highly repeatable (intraclass correlation 0.987 to 0.995) while
      simultaneously carrying a systematic offset against the reference method of
      about +3.4 kg fat-free mass and -4.2 percent body fat in men. A very
      consistent number can be a very consistently wrong number. Use the device
      for trend, never for an absolute figure, and never compare a reading from
      one device against a reading from another.
    grade: B
  - note: >
      VISCERAL FAT IS THE WEAKEST OUTPUT on the consumer device and should not be
      spoken as a quantity. In the same comparison it had the lowest agreement of
      any measure reported (concordance 0.68 in men and 0.34 in women).
    grade: B
  - note: >
      NO PUBLISHED LEAST-SIGNIFICANT-CHANGE FIGURE was adopted here for the
      consumer bioimpedance case under uncontrolled home or gym conditions. The
      precision estimates located are from standardised laboratory protocols. The
      transfer to an unstandardised gym measurement is an extrapolation of unknown
      size, so this item states the DIRECTION of the limit and declines to state a
      threshold number. Recorded as an open sub-gap rather than filled with a
      borrowed figure.
    grade: D
claim: >
  A single body-composition reading cannot resolve a short-interval change. Under
  a fully standardised protocol, repositioning alone contributes only trivial
  error to whole-body estimates, but ordinary daily activity and the consumption
  of one breakfast substantially increase measurement error and shift the mean
  estimate of total and regional lean mass. Consumer multi-frequency bioimpedance
  is highly repeatable yet systematically biased against reference methods
  (roughly +3.4 kg fat-free mass and -4.2 percent body fat in men, +2.0 kg and
  -2.8 percent in women, in 1000 adults measured without controlling hydration,
  meals, exercise or time of day), and its visceral-fat output agrees poorly. The
  usable signal is a trend measured on one device under one repeated protocol.
reasoning: >
  Two independent lines converge. The reference-method work shows that even a
  laboratory instrument's reading moves with what the person did that morning,
  which is why standardisation (rested, overnight-fasted, minimal clothing, fixed
  positioning) is the published precondition for longitudinal use. The 1000-adult
  field comparison shows what happens when that precondition is dropped: high
  retest reliability alongside a real systematic offset. Both are direct
  measurements against a stated reference rather than modelled inferences, which
  places the claim at the RCT-level pre-consensus band, and no source disputes the
  direction, so it is not flagged contested. The item deliberately stops short of
  publishing a numeric detection threshold for the uncontrolled consumer case,
  because the precision estimates available all come from standardised laboratory
  protocols and importing one would manufacture a false floor. For a consumer
  reading a scale or a gym impedance device against a daily meal log, the
  operational consequences are that same-device same-protocol trend is the only
  interpretable output, that cross-device comparison is meaningless, and that a
  single reading is never evidence a change occurred.
---

# nutrition/body-composition-measurement-floor-011

Body-composition numbers move for reasons that have nothing to do with body
composition. Reference-standard scanning of active adults over two days showed
that simply repositioning a person on the bed barely changes the whole-body
result, but going about a normal day, or eating one breakfast, measurably
increases the error and shifts the estimated lean mass. That is why the published
protocol for tracking anyone over time insists on rested, overnight-fasted,
minimally clothed and identically positioned measurement.

Consumer devices drop every one of those conditions, and a thousand-person
comparison against the reference method shows exactly what that costs. The device
was extremely repeatable, agreeing with itself to within a fraction of a percent
on retest, while at the same time reading fat-free mass several kilograms high
and body fat several percentage points low in men. Repeatability and correctness
are different properties, and a device can have the first while lacking the
second. Its visceral-fat output was the weakest number it produced and should not
be quoted at all.

This item deliberately does not publish a threshold for how large a change has to
be before it counts. Every precision figure available comes from standardised
laboratory conditions, and borrowing one for a gym measurement would invent a
floor rather than measure one. The direction is what is established: track the
trend on one device under one repeated routine, never mix devices, and never let
a single reading stand as evidence that anything changed.
