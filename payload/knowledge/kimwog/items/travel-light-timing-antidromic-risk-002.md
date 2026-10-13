---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The one genuinely actionable circadian item in the lane, and the one with the
# sharpest failure mode: the direction rule is easy to get BACKWARDS, and getting
# it backwards does not produce no effect, it produces the wrong effect. Built
# from the primary phase-response-curve study for the mechanism and the
# travel-specific review for the field consequence, with the difference in tier
# between those two sources carried explicitly rather than smoothed over.
# Source re-audit 2026-10-06: Eastman and Burgess 2009 re-read at PMC full text,
# Khalsa 2003 abstract re-read. (1) 'one day per time zone' was pinned on the
# westward rate; about an hour a day is the EASTWARD figure (57 min), westward
# is 92 min, so the comparison was reversed. (2) 2.4 and 1.6 h/day come from a
# laboratory 12 h abrupt-shift study, not from travellers; the review's own
# planning figures are 1.5 and 2 h/day. (3) 'follows from the period' -> the
# review says explained at least in part. (4) antidromic re-entrainment is
# observed in two small samples and the light route is the review's PRC-based
# explanation, not a measured cause: B -> C on that point. (5) the missing dead
# zone is protocol-dependent.
id: travel/light-timing-antidromic-risk-002
domain: travel
lane: "@travel-clinical"
grade: B (the direction rule under laboratory conditions); C (the existence of wrong-direction re-entrainment after eastward flights, from small samples; the re-entrainment rates in minutes per day); D (any consumer-scale magnitude for ordinary outdoor light)
locale: universal
as_of: 2003-2009
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/12717008/"  # Khalsa SB, Jewett ME, Cajochen C, Czeisler CA. 2003, J Physiol 549(Pt 3):945-952, doi 10.1113/jphysiol.2003.040477, PMCID PMC2342968 -- the primary human phase response curve. n=21, inpatient constant-routine protocol
  - "https://pubmed.ncbi.nlm.nih.gov/20204161/"  # Eastman CI, Burgess HJ. 2009, Sleep Med Clin 4(2):241-255, doi 10.1016/j.jsmc.2009.02.006, PMCID PMC2829880 -- the travel-specific review. Full text read at PMC 2026-09-02 for the re-entrainment rates, the eastward-asymmetry explanation and the antidromic-re-entrainment passage; re-read at full text 2026-10-06 (which figures are traveller estimates and which laboratory, the antidromic examples, the planning figures)
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
      WRONG-TIMED LIGHT CAN SHIFT THE WRONG WAY: WHAT IS OBSERVED AND WHAT IS
      EXPLAINED ARE DIFFERENT TIERS. The review names antidromic re-entrainment,
      the clock re-entraining in the direction opposite to the one the traveller
      needs, and reports that it is common following eastward travel, especially
      when eight or more time zones are crossed. Observed, in the studies it
      cites: of 8 people flown 11 zones east, 7 re-entrained by delaying; of 6
      flown 8 zones east, 4 advanced, 1 delayed and 1 did not shift at all.
      Those are small samples, and the review does not attribute them to light
      exposure. Explained: the review uses the light curve to show how it could
      happen (more bright light before the temperature minimum than after could
      push the clock to delay even while the sleep schedule advances) and notes
      that advancing and delaying forces can cancel into no shift. So the
      warning that mistimed light could make the trip worse is
      mechanism-supported, not a measured field effect.
    grade: C
  - note: >
      WHY EASTWARD IS HARDER, MECHANISTICALLY. The human free-running period is
      slightly longer than 24 hours, and the review states plainly that it is
      much more difficult to phase advance the human circadian clock than to
      phase delay it. Eastward travel requires an advance. This is not only a
      folk observation about jet lag feeling worse going east; the review says
      it can be explained, at least in part, by the period of the oscillator.
    grade: B
  - note: >
      THE RATES ARE REVIEW-CITED, NOT MEASURED HERE, AND ARE GRADED DOWN. The
      review gives two different kinds of figure. From real jet travellers, which
      it calls early estimates: the clock delays about 92 minutes per day after
      westward flights and advances about 57 minutes per day after eastward
      flights. From a laboratory study with an abrupt 12 hour shift of the sleep
      schedule and appropriately timed bright light: delays of 2.4 hours per day
      and advances of 1.6 hours per day, averaged over the first 4 days. The
      second pair is a laboratory best case, not a travel rate; the review's own
      planning assumption after landing, with timed bright light, is 1.5 hours
      per day of advance and 2 hours per day of delay. Treat all of these as the
      review's reported figures: the right order of magnitude for planning, NOT a
      personal prediction. And the popular "one day per time zone" rule of thumb,
      about an hour a day, matches the EASTWARD traveller figure (57 minutes per
      day), not the westward one; applied westward it overstates the time needed
      (at 92 minutes per day, nine zones is about six days, not nine). The review
      does not mention the rule of thumb; that comparison is the curator's
      arithmetic.
    grade: C
  - note: >
      THE LABORATORY DOSE IS NOT A TRIP. The phase response curve was derived
      from 21 subjects given a 6.7 hour bright-light stimulus under a controlled
      inpatient constant routine with dim background lighting, and the resulting
      curve had a peak-to-trough amplitude of about 5 hours. That establishes the
      shape of the response and the location of the critical phase. It does not
      establish how far a given traveller moves from an hour on a sunny street,
      and this warehouse has already recorded exactly this mechanism-versus-
      intervention gap for evening light in the sleep domain. The missing dead
      zone belongs to this protocol: the review draws the midday region of its
      own curve without data and cites other human light curves with minimal
      midday shifts. Carry the SHAPE forward; do not carry the amplitude
      forward.
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
  asymmetric: eastward travel needs a phase advance, and the review states that
  it is much more difficult to phase advance the clock than to phase delay it,
  explained at least in part by a free-running period slightly longer than 24
  hours. The travel-specific review gives early estimates from real jet
  travellers of roughly 92 minutes per day of delay after westward flights and
  roughly 57 minutes per day of advance after eastward flights, and cites a
  laboratory study of an abrupt 12 hour schedule shift in which appropriately
  timed bright light gave roughly 2.4 hours per day of delay and 1.6 hours per
  day of advance over the first four days. The review also names antidromic
  re-entrainment -- the clock shifting in the direction OPPOSITE to the one
  needed -- and reports it as common after eastward travel, especially across
  eight or more time zones (small samples: 7 of 8 people flown 11 zones east;
  4 of 6 advanced after 8 zones east). It offers the light curve as one way
  mistimed light could produce this; it does not report light as the measured
  cause.
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
  the review's figures, not as measurements made here. The part of the review that
  matters most for advice is the antidromic passage, and its two halves carry
  different weight. That wrong-direction re-entrainment happens is observed, but
  in two small samples (7 of 8 after 11 zones east; 4 of 6 advancing after 8
  zones east), so it sits in the observational band. That mistimed light is a
  route to it is the review's explanation from the phase response curve -- if the
  curve has a delay region and an advance region, then light on the wrong side of
  the critical phase must push the wrong way -- and the review does not report
  light exposure as the measured cause in those subjects. That is still the
  item's real payload: it moves light timing from an optimisation with no
  downside to an intervention that could make the trip worse, which is a
  different kind of advice, and it should be said in those terms, as
  mechanism-supported and not measured in travellers.
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
someone's clock currently sits. And when the guess is wrong, the result need not
be a null. The travel review that studies this names the failure -- the clock
re-entrains in the direction opposite to the one the traveller needs -- and
reports that it is common after eastward travel, particularly when eight or more
time zones have been crossed. Its examples are small: seven of eight people flown
eleven zones east re-entrained backwards, and four of six flown eight zones east
moved the right way. The review does not say light caused those cases; it shows,
from the light curve, how wrong-timed light could. That is one candidate
explanation for the trip where someone never seems to adjust at all. For some of
them the clock was moving, backwards.

There is also a built-in asymmetry, and it is not psychological. The human clock
free-runs a little slower than 24 hours, so delaying it is downhill and advancing
it is uphill. Eastward travel is the uphill one; the review says the period
explains this at least in part. Unaided, it reports early estimates from real
travellers of roughly an hour and a half of delay per day going west against
roughly an hour of advance per day going east. Laboratory figures with timed
bright light are higher (about two and a half hours of delay and one and a half
of advance), but they come from a different design and are not a travel rate.
Which means the familiar "one day per time zone" rule, about an hour a day,
matches the eastward figure; applied going west it overstates how long the
adjustment takes.

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
