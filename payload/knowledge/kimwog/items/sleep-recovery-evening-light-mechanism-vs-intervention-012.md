---
# Collection sprint 2026-09-02. The blue-light claim is the cleanest example in
# this domain of a real laboratory mechanism being sold as a consumer product
# effect. Both halves are carried: the mechanism study (rigorous, tiny, extreme
# dose) and the Cochrane review of the intervention people actually buy
# (indeterminate at very low certainty). Contested is set because the two halves
# are routinely spoken as one. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/evening-light-mechanism-vs-intervention-012
domain: sleep-recovery
grade: C (the laboratory mechanism); D (any consumer-scale magnitude); B (blue-blocking lenses have not been shown to improve sleep)
lane: "@clinical"
locale: universal
as_of: 2015-2023
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/25535358/"  # Chang AM, Aeschbach D, Duffy JF, Czeisler CA. 2015, Proc Natl Acad Sci U S A 112(4):1232-1237, doi 10.1073/pnas.1418490112, PMCID PMC4313820 -- the mechanism study; inpatient, light-emitting eReader versus printed book
  - "https://pubmed.ncbi.nlm.nih.gov/37593770/"  # Singh S, Keller PR, Busija L, McMillan P, Makrai E, Lawrenson JG, Hull CC, Downie LE. 2023, Cochrane Database Syst Rev 8(8):CD013244, doi 10.1002/14651858.CD013244.pub2, PMCID PMC10436683 -- 17 RCTs of blue-light filtering spectacle lenses
  - "sleep-recovery/grade-aasm-anchor-002"  # certainty versus action-strength; a mechanism demonstration is not an intervention result
  - "framework:GRADE -- the Cochrane review is the highest-certainty document in this item and its sleep-quality verdict is VERY LOW certainty with no meta-analysis possible, which is itself the finding. The mechanism study is a rigorous inpatient protocol but n=12 with an exposure dose far above ordinary use, so it is graded for what it demonstrates (the pathway exists) and not for what it is usually quoted as (a consumer-scale effect size)."
applicability:
  axes:
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The mechanism study is real and its conditions are extreme. Participants
      read a light-emitting eReader for four hours before bed, on consecutive
      evenings, in an inpatient laboratory whose background lighting was
      controlled to be dim. Against reading a printed book under those
      conditions, they took longer to fall asleep, had suppressed evening
      melatonin, showed a later circadian phase, felt less sleepy in the evening
      and were less alert the next morning. Every one of those effects is
      credible. None of them was produced by the exposure most people actually
      have -- a phone, at arm's length, for a few minutes, in a normally lit
      room.
    grade: C
  - note: >
      Sample size. n=12. This is a mechanistic demonstration in a highly
      controlled environment, which is the right design for showing that a
      pathway exists and the wrong design for estimating how much anything moves
      in ordinary life. Quoting its numbers as a personal expectation is the
      standard failure mode for this study.
    grade: C
  - note: >
      The consumer intervention has been reviewed and it does not deliver. The
      Cochrane review of blue-light filtering spectacle lenses included 17
      randomized trials with samples from 5 to 156 participants and follow-up
      from under one day to five weeks. NO meta-analysis was possible for ANY
      outcome, owing to lack of available quantitative data, heterogeneous
      populations and differing follow-up periods. On sleep quality specifically,
      six trials with 148 participants between them split three positive and
      three null, and the review's verdict is very low certainty -- it does not
      know whether the lenses help. On eye strain, there may be no difference; on
      visual acuity, probably little or none.
    grade: B
  - note: >
      An absence worth stating: NONE of the 17 trials in the Cochrane review
      measured serum melatonin. So the intervention that is sold on the melatonin
      mechanism has never been tested against the melatonin mechanism in that
      review's evidence base. That is a gap in the product's own case, not a
      finding against it.
    grade: B
  - note: >
      Study quality in the Cochrane review is poor across the board. None of the
      17 trials had low risk of bias across all seven assessed domains; 65 percent
      were at high risk of detection bias because outcome assessors were not
      masked, and 59 percent at high risk of performance bias because participants
      and personnel were not masked; only 35 percent were pre-registered. This is
      an unblindable-intervention literature with subjective endpoints, the same
      structural weakness this warehouse documents for recovery modalities.
    grade: B
  - note: >
      NOT covered. Screen-use restriction as a behaviour, screen dimming, device
      night modes, and ambient evening light management were NOT the intervention
      tested by either source and no defensible evidence on them was located in
      this sprint. Nothing here endorses or refutes them. Also note that the
      relevant behavioural claim -- put the phone down -- is a sleep-hygiene
      element, and this domain separately records that sleep hygiene as a
      standalone treatment is not endorsed by the AASM guideline.
    grade: D
claim: >
  The blue-light story has a solid mechanism and an unsupported product, and the
  two get spoken as one. On the mechanism: an inpatient study in which 12
  participants read a light-emitting eReader for FOUR HOURS before bed under
  controlled dim laboratory lighting, compared against reading a printed book,
  found longer time to fall asleep, suppressed evening melatonin, a later
  circadian phase, reduced evening sleepiness and reduced next-morning alertness.
  That establishes the pathway is real at that dose in that setting; it does not
  establish a magnitude for ordinary phone use, and n=12 with a four-hour exposure
  under dim background light is not ordinary phone use. On the product: the
  Cochrane review of blue-light filtering spectacle lenses included 17 randomized
  trials and could perform NO meta-analysis for any outcome; on sleep quality it
  reports very low certainty with six trials totalling 148 participants splitting
  three positive and three null; on eye strain there may be no difference; on
  visual acuity probably little or none. None of the 17 trials measured serum
  melatonin, so the mechanism the product is sold on was not tested. Trial quality
  was poor throughout: no trial was at low risk of bias across all seven domains,
  65 percent were at high risk of detection bias and 59 percent of performance
  bias, and only 35 percent were pre-registered. The operative rule: short-
  wavelength light at high dose measurably delays the clock and suppresses
  melatonin; the glasses sold on that basis have not been shown to improve sleep,
  and the magnitude for normal evening screen use is unestablished in both
  directions.
reasoning: >
  This is the domain's clearest case of the pattern the sourcing discipline for
  this sprint was written to catch: a real, rigorously demonstrated laboratory
  mechanism, and a consumer layer built on top of it that has not been shown to
  work. Chang et al. 2015 (PNAS 112(4):1232-1237) is a genuinely good study of
  what it studied -- an inpatient protocol from the Brigham and Women's sleep
  division with controlled background lighting, comparing an identical reading
  task on a light-emitting device against print, and reporting effects across
  sleep-onset latency, melatonin secretion, circadian phase and next-morning
  alertness. Its limits are equally plain: twelve participants and a four-hour
  pre-bed exposure in a dim room, which is a deliberately maximised dose chosen to
  make the pathway visible. Graded for the demonstration, not for the magnitude.
  Singh et al. 2023 (Cochrane CD013244.pub2) is the higher-certainty document and
  it tests the thing people buy. Its most informative result is structural: across
  17 randomized trials it could not pool a single outcome, because the
  quantitative data were not available, the populations were heterogeneous and the
  follow-up periods differed. Its sleep-quality conclusion is explicit uncertainty
  at very low certainty, with the six relevant trials splitting evenly. The
  finding that no included trial measured serum melatonin is worth recording on its
  own, because it means the product's advertised mechanism is untested within its
  own evidence base. The risk-of-bias profile is the same unblindable-intervention
  problem this warehouse documents for recovery modalities in
  exercise/recovery-modality-soreness-vs-performance-024: participants know
  whether they are wearing tinted lenses, outcome assessors mostly were not
  masked, and the primary endpoint is a subjective rating. Contested is set
  because the mechanism result and the intervention result are routinely merged
  into a single confident consumer claim, and because within the Cochrane sleep
  evidence the individual trials genuinely disagree three to three. What this item
  deliberately does NOT do is convert an absence into a negative: no defensible
  evidence was located on screen-time restriction, device night modes or ambient
  light management as behaviours, so no claim is made about them in either
  direction.
---

# sleep-recovery/evening-light-mechanism-vs-intervention-012

There are two blue-light claims and only one of them has support.

The first is about the pathway. Researchers had people read on a light-emitting
device for four hours before bed, on consecutive evenings, inside a laboratory
where the background lighting was kept deliberately dim, and compared it against
the same people reading a printed book under the same conditions. On the device
they took longer to fall asleep, their evening melatonin was suppressed, their
body clock shifted later, they felt less sleepy at night and less alert the next
morning. Those results are credible and the study was carefully run.

Now notice the conditions. Twelve people. Four hours. A dim room chosen so that
the screen would be the dominant light source. That is a dose designed to make an
effect visible, not a description of someone checking a phone in a lit living room
for ten minutes. The study shows the pathway exists. It does not tell you how much
your evening looks like that.

The second claim is the product. Blue-light filtering glasses are sold on exactly
this mechanism, and they have been reviewed properly. Seventeen randomized trials.
The reviewers could not pool a single outcome -- not one -- because the numbers
were not reported usably, the populations differed and the follow-up periods
ranged from less than a day to five weeks. On sleep quality, six trials covering
148 people between them split three finding a benefit and three finding none, and
the review's stated position is that it does not know. On eye strain, likely no
difference. On visual acuity, probably nothing.

One detail deserves to be pulled out. Not a single one of those seventeen trials
measured melatonin. The mechanism the glasses are sold on was not tested anywhere
in the evidence base for the glasses.

The trial quality is also the familiar problem. Nobody can be blinded to whether
they are wearing tinted lenses. Two thirds of these trials did not even mask the
people assessing the outcomes, and most were not pre-registered. Unblindable
intervention, subjective endpoint, mixed results -- this warehouse has a whole
item elsewhere about what that combination usually means.

So the honest position holds both halves without letting either one borrow the
other's credibility. High-dose short-wavelength light before bed really does
suppress melatonin and shift the clock. The glasses built on that fact have not
been shown to improve sleep. And how much a normal evening of screen use matters
is genuinely unestablished -- not demonstrated to be large, and not demonstrated
to be nothing.

What about simply putting the phone away? No defensible evidence on that behaviour
was found in this sprint, so nothing here supports or opposes it. It is worth
noting only that it belongs to the sleep-hygiene family, and this domain
separately records that the sleep field's own guideline declined to endorse sleep
hygiene as a standalone treatment.
