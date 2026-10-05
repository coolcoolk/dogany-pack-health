---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The one genuinely actionable circadian item in the lane, and the one with the
# sharpest failure mode: the direction rule is easy to get BACKWARDS, and getting
# it backwards does not produce no effect, it produces the wrong effect. Built
# from the primary phase-response-curve study for the mechanism and the
# travel-specific review for the field consequence, with the difference in tier
# between those two sources carried explicitly rather than smoothed over.
id: travel/light-timing-antidromic-risk-002
domain: travel
lane: "@travel-clinical"
grade: B (the direction rule and the existence of wrong-direction shifting); C (the re-entrainment rates in minutes per day); D (any consumer-scale magnitude for ordinary outdoor light)
locale: universal
as_of: 2003-2009
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/12717008/"  # Khalsa SB, Jewett ME, Cajochen C, Czeisler CA. 2003, J Physiol 549(Pt 3):945-952, doi 10.1113/jphysiol.2003.040477, PMCID PMC2342968 -- the primary human phase response curve. n=21, inpatient constant-routine protocol
  - "https://pubmed.ncbi.nlm.nih.gov/20204161/"  # Eastman CI, Burgess HJ. 2009, Sleep Med Clin 4(2):241-255, doi 10.1016/j.jsmc.2009.02.006, PMCID PMC2829880 -- the travel-specific review. Full text read at PMC 2026-09-02 for the re-entrainment rates, the eastward-asymmetry explanation and the antidromic-re-entrainment passage
  - "source:travel/jet-lag-guideline-standing-001 -- the guideline places timed light at the Option tier for jet lag; this item is the mechanism underneath that, not an upgrade of it"
  - "source:sleep-recovery/evening-light-mechanism-vs-intervention-012 -- the same mechanism-versus-consumer-dose split, in the sleep domain. Read the two together: a laboratory light dose is not a hotel window"
  - "framework:phase response curve -- the primary source is a controlled inpatient protocol using a 6.7 h bright-light stimulus at roughly 10000 lx fixed-gaze and 5000-9000 lx free-gaze, with plasma melatonin as the phase marker. It is graded for the SHAPE it establishes, not for a magnitude anyone will reproduce on a trip. The review is a review and its cited rates inherit that tier."
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
      THE DIRECTION RULE, AND THE REFERENCE POINT IT HANGS ON. Light landing
      BEFORE the core body temperature minimum delays the clock; light landing
      AFTER it advances the clock; at the critical phase itself there is no
      shift. The temperature minimum sits in the late part of the sleep episode,
      not at midnight and not at wake time, and the whole rule is useless without
      it. Any version of this advice that omits the reference point -- "get
      morning light to fix jet lag" -- is a coin flip dressed as a rule, because
      whether a given hour counts as before or after the minimum depends on where
      the traveller's clock currently is, not on what the destination's clocks
      say.
    grade: A
  - note: >
      WRONG-TIMED LIGHT DOES NOT DO NOTHING, IT SHIFTS THE WRONG WAY. The review
      names this: antidromic re-entrainment, the clock re-entraining in the
      direction opposite to the one the traveller needs, and it reports that this
      is common following eastward travel, especially when eight or more time
      zones are crossed. This is the single most useful thing in the item. It
      converts light timing from a nice-to-have optimisation into something with
      a downside, and it explains why the eight-to-twelve-zone trip is the one
      people describe as never adjusting.
    grade: B
  - note: >
      WHY EASTWARD IS HARDER, MECHANISTICALLY. The human free-running period is
      slightly longer than 24 hours, and the review states plainly that it is
      much more difficult to phase advance the human circadian clock than to
      phase delay it. Eastward travel requires an advance. This is not a folk
      observation about jet lag feeling worse going east; it follows from the
      period of the oscillator.
    grade: B
  - note: >
      THE RATES ARE REVIEW-CITED, NOT MEASURED HERE, AND ARE GRADED DOWN. The
      review reports phase delays of about 92 minutes per day after westward
      flights and phase advances of about 57 minutes per day after eastward
      flights, and with bright-light intervention delays of about 2.4 hours per
      day and advances of about 1.6 hours per day. Treat these as the review's
      reported figures. They are the right order of magnitude for planning and
      they are NOT a personal prediction, and the popular "one day per time zone"
      rule of thumb is a rounding of the westward number applied in both
      directions, which the asymmetry above says it should not be.
    grade: C
  - note: >
      THE LABORATORY DOSE IS NOT A TRIP. The phase response curve was derived
      from 21 subjects given a 6.7 hour bright-light stimulus under a controlled
      inpatient constant routine with dim background lighting, and the resulting
      curve had a peak-to-trough amplitude of about 5 hours. That establishes the
      shape of the response and the location of the critical phase. It does not
      establish how far a given traveller moves from an hour on a sunny street,
      and this warehouse has already recorded exactly this mechanism-versus-
      intervention gap for evening light in the sleep domain. Carry the SHAPE
      forward; do not carry the amplitude forward.
    grade: C
  - note: >
      NOT COVERED BY EITHER SOURCE. No light box product, no wavelength or
      intensity specification for consumer devices, no melatonin dose or timing
      table, no validated pre-flight shifting schedule that was tested against a
      real itinerary in this pass, and nothing about children, shift workers or
      anyone with a diagnosed circadian disorder. Do not manufacture a schedule
      from this item. It supports a direction and a warning, not a plan.
    grade: D
claim: >
  Light shifts the circadian clock in a direction that depends on WHEN it lands
  relative to the core body temperature minimum, which falls in the late part of
  the sleep episode. Light before that point delays the clock; light after it
  advances the clock; at the critical phase itself no shift occurs. The primary
  human phase response curve establishing this was derived in 21 subjects under an
  inpatient constant-routine protocol using a 6.7 hour bright-light stimulus, and
  had a peak-to-trough amplitude of about 5 hours, with no prolonged dead zone of
  photic insensitivity during the subjective day. The travel consequence is
  asymmetric: eastward travel needs a phase advance, and because the human
  free-running period is slightly longer than 24 hours it is much more difficult
  to phase advance the clock than to phase delay it. The travel-specific review
  reports unaided re-entrainment of roughly 92 minutes per day of delay after
  westward flights and roughly 57 minutes per day of advance after eastward
  flights, rising to roughly 2.4 hours and 1.6 hours per day respectively with
  bright light. Critically, mistimed light does not merely fail: the review names
  antidromic re-entrainment -- the clock shifting in the direction OPPOSITE to the
  one needed -- and reports it as common after eastward travel, especially across
  eight or more time zones.
reasoning: >
  This is the item a life agent can actually act on, and it is also the item most
  likely to be got backwards, which is why it is built with the reference point
  in the first sentence rather than the conclusion. The mechanism rests on a
  primary source of unusually good design for the question: Khalsa et al. 2003 (J
  Physiol 549(Pt 3):945-952) ran pre- and post-stimulus constant routines in dim
  light with plasma melatonin as the phase marker, in 21 entrained subjects, which
  is a large sample by phase-response-curve standards and an explicit improvement
  on the small and imprecisely phased curves that preceded it. It is graded in the
  solid band for the shape it establishes -- the direction rule, the location of
  the critical phase, the absence of a long insensitive daytime window -- and a
  band lower for anything numeric, because a 6.7 hour laboratory light stimulus
  under controlled dim background lighting is a deliberately maximised dose and
  this warehouse already carries a sleep-domain item about exactly what happens
  when a laboratory light magnitude gets quoted as a consumer expectation. The
  field consequences come from Eastman and Burgess 2009 (Sleep Med Clin
  4(2):241-255), which is a review rather than a primary study, and its
  contribution is graded accordingly: the rates in minutes per day are reported as
  the review's figures, not as measurements made here. The one part of the review
  that carries more weight than its tier would suggest is the antidromic passage,
  because it is a qualitative mechanism claim that follows directly from the phase
  response curve rather than from any single cited number -- if the curve has a
  delay region and an advance region, then light on the wrong side of the critical
  phase must push the wrong way, and the review reports that this is what commonly
  happens after long eastward flights. That is the item's real payload. It changes
  light timing from an optimisation with no downside into an intervention that can
  make the trip worse, which is a different kind of advice and deserves to be said
  in those terms.
---

# travel/light-timing-antidromic-risk-002

Light moves the body clock. Which way it moves depends entirely on when it
arrives, and the reference point is not the local clock on the wall.

The pivot is the core body temperature minimum, which falls late in the sleep
episode. Light landing before that point delays the clock. Light landing after it
advances the clock. Right at the critical phase, nothing happens. This shape
comes from a controlled inpatient study in which 21 people received a long bright
light exposure at different points across the circadian cycle, with blood
melatonin used to measure where their clock had actually moved to.

Everything useful and everything dangerous about jet-lag light advice follows
from that one sentence.

Useful, because the direction a traveller needs is knowable. Flying east requires
the clock to advance. Flying west requires it to delay. So east wants light after
the temperature minimum and west wants light before it.

Dangerous, because the popular version of this advice drops the reference point.
"Get morning light when you land" is not a rule; it is a guess about where
someone's clock currently sits. And when the guess is wrong, the result is not a
null. The travel review that studies this names the failure -- the clock
re-entrains in the direction opposite to the one the traveller needs -- and
reports that it is common after eastward travel, particularly when eight or more
time zones have been crossed. That is a real explanation for the trip where
someone never seems to adjust at all. They were adjusting. Backwards.

There is also a built-in asymmetry, and it is not psychological. The human clock
free-runs a little slower than 24 hours, so delaying it is downhill and advancing
it is uphill. Eastward travel is the uphill one. Unaided, the review reports
roughly an hour and a half of delay per day going west against roughly an hour of
advance per day going east, with bright light raising both but not equalising
them. Which means the familiar "one day per time zone" rule is roughly the
westward number applied in both directions, and the asymmetry says it should not
be.

Two limits, both deliberate.

The numbers here are borrowed. The phase response curve is a primary measurement;
the re-entrainment rates in minutes per day are figures a review reports. They
are good enough to plan around and they are not a prediction about any particular
person.

And the laboratory dose is not a trip. That curve was produced by nearly seven
hours of bright light in a dim room. It tells you the shape of the response, not
how far an afternoon outdoors will move you. This warehouse already carries the
same distinction on the sleep side, where a real laboratory light mechanism gets
sold as a consumer product effect it has never demonstrated. The same caution
applies in the other direction here.

What this item supports is a direction and a warning. It does not support a
schedule, a device, or a drug, and none of those should be generated from it.
