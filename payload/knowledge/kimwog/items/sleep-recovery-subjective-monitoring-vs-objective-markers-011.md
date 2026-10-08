---
# Collection sprint 2026-09-02. Answers the "which recovery markers are actually
# predictive versus merely correlated" question, and extends
# sleep-recovery/tracker-accuracy-003 from device ACCURACY to device
# USEFULNESS. The headline is uncomfortable for a data-driven agent: the cheap
# subjective question outperforms the expensive number. The proprietary
# readiness-score question was searched and NOT closed -- see the refraction
# note and GAPS.md. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/subjective-monitoring-vs-objective-markers-011
domain: sleep-recovery
grade: B (subjective measures track training load better than objective markers); C (HRV-guided training's small endurance benefit); D (any resistance-training application of HRV guidance)
lane: "@clinical"
locale: universal
as_of: 2016-2021
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/26423706/"  # Saw AE, Main LC, Gastin PB. 2016, Br J Sports Med 50(5):281-291, doi 10.1136/bjsports-2015-094758, PMCID PMC4789708 -- systematic review, 56 original studies reporting concurrent subjective and objective measures
  - "https://pubmed.ncbi.nlm.nih.gov/34639599/"  # Manresa-Rocamora A, Sarabia JM, Javaloyes A, Flatt AA, Moya-Ramon M. 2021, Int J Environ Res Public Health 18(19):10299, doi 10.3390/ijerph181910299, PMCID PMC8507742 -- methodological systematic review with meta-analysis of HRV-guided training
  - "sleep-recovery/tracker-accuracy-003"  # device ACCURACY against polysomnography; this item is the USEFULNESS partner
  - "framework:GRADE -- the subjective-versus-objective finding rests on a large systematic review with explicit study-quality and evidence-level grading, and is graded at the trial band for direction. The HRV-guided training result is graded lower because the performance outcomes were all non-significant, the entire literature is endurance training, and the authors themselves state that best methodological practices for HRV index selection, recording position and baseline referencing require further study."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The core result is a dissociation, and it is the opposite of what a
      metrics-driven system wants to hear. Across 56 studies reporting BOTH kinds
      of measure on the same athletes, subjective and objective measures of
      wellbeing generally DID NOT CORRELATE. Subjective measures reflected acute
      and chronic training loads with superior sensitivity and consistency.
      Subjective wellbeing worsened with an acute increase in load and with
      chronic training, and improved with an acute decrease in load. So the
      question "how do you feel" is not a soft substitute for the blood marker or
      the resting heart rate; on this evidence it is the better instrument.
    grade: B
  - note: >
      What HRV-guided training actually bought, stated precisely. Compared with
      predefined training, HRV-guided training was superior for enhancing
      vagal-related HRV indices (standardized mean difference 0.50, 95 percent CI
      0.09 to 0.91) -- that is, it improved the metric it was guided by. It was
      NOT superior for resting heart rate (0.04, CI -0.34 to 0.43). For outcomes
      anyone actually trains for, all effects were small and NON-significant:
      maximal aerobic capacity 0.20 (CI -0.07 to 0.47), aerobic capacity at the
      second ventilatory threshold 0.26 (CI -0.05 to 0.57), endurance performance
      0.20 (CI -0.09 to 0.48). The authors' own summary is that if HRV-guided
      training is superior at all for fitness and performance, current data suggest
      it is only by a small margin.
    grade: C
  - note: >
      Domain limit, and it is a hard one. The entire HRV-guided training
      literature in that meta-analysis is ENDURANCE training with aerobic and
      endurance-performance outcomes. No resistance-training equivalent was located
      in this sprint. Any statement that HRV should govern whether to squat heavy
      today is an extrapolation from cycling and running studies with
      non-significant performance results, and must be spoken as such.
    grade: D
  - note: >
      The one thing HRV guidance did reliably do is worth keeping, because it is
      not nothing: the authors note it may be more effective than predefined
      training for maintaining and improving vagal-mediated HRV with LESS
      LIKELIHOOD OF NEGATIVE RESPONSES. Fewer people going backwards is a
      different and more modest claim than a group-average performance gain, and it
      is the claim the data actually support.
    grade: C
  - note: >
      SEARCHED AND NOT FOUND, recorded so the absence is not read as an
      all-clear. No peer-reviewed validation of a PROPRIETARY consumer readiness
      or recovery score -- the composite number a wrist or ring device shows each
      morning -- against measured next-day physical performance was located in
      this sprint. What was found instead is observational work correlating such
      scores with training load and sleep duration, which establishes that the
      score moves with inputs, not that it predicts what the athlete can do. Until
      such a validation is located, treat a proprietary readiness score as an
      unvalidated composite: the device's underlying sleep staging is already
      known to vary widely in accuracy per tracker-accuracy-003, and the algorithm
      that turns it into a score is not published. This is a GAP, not a finding
      against the scores.
    grade: D
  - note: >
      Practical translation that follows from the evidence rather than from
      preference: a short, consistent, self-reported wellbeing check is the
      best-supported monitoring instrument in this literature, and it is also the
      cheapest. Consistency of the instrument matters more than which one, and the
      value comes from tracking change within a person over time rather than from
      comparing the number to anyone else.
    grade: C
claim: >
  Among recovery markers, the cheap subjective one outperforms the expensive
  objective ones. A systematic review of 56 studies that measured BOTH subjective
  and objective indicators of athlete wellbeing on the same athletes found that
  the two generally did NOT correlate, and that subjective measures reflected
  acute and chronic training load with superior sensitivity and consistency:
  subjective wellbeing was impaired by an acute increase in training load and by
  chronic training, and improved by an acute decrease in load. Objective markers
  taken at rest (blood markers, heart rate) and during exercise (oxygen
  consumption, heart-rate response) did not track training response as reliably.
  On the most popular objective instrument specifically, a meta-analysis of
  heart-rate-variability-guided training found it superior to predefined training
  for improving vagal-related HRV indices (standardized mean difference 0.50, 95
  percent CI 0.09 to 0.91) but NOT for resting heart rate (0.04), and produced only
  small NON-significant differences for maximal aerobic capacity (0.20, CI -0.07
  to 0.47), aerobic capacity at the second ventilatory threshold (0.26) and
  endurance performance (0.20, CI -0.09 to 0.48); the authors conclude that any
  superiority for fitness and performance is only by a small margin, while noting a
  reduced likelihood of negative responders. That entire literature is ENDURANCE
  training -- no resistance-training equivalent was located. Separately, no
  peer-reviewed validation of a proprietary consumer readiness or recovery score
  against measured next-day performance was located in this sprint. The operative
  rule: a consistent self-reported wellbeing check is the best-evidenced recovery
  monitor available; HRV guidance has a small, endurance-only, mostly
  non-significant performance case; and a device's morning readiness number is an
  unvalidated composite until shown otherwise.
reasoning: >
  This item extends the domain's existing device item from ACCURACY to
  USEFULNESS. sleep-recovery/tracker-accuracy-003 already establishes that
  consumer trackers vary widely against polysomnography and that their numbers
  must not be treated as high-certainty measurements. The natural follow-on
  question -- given imperfect numbers, which recovery marker should actually drive
  a training decision -- is answered by Saw, Main and Gastin 2016 (Br J Sports
  Med 50(5):281-291), which systematically compared concurrent subjective and
  objective measures across 56 studies, evaluated study quality and strength of
  findings to assign overall evidence levels, and found the two families generally
  uncorrelated with subjective measures the more sensitive and consistent
  reflection of training load. That result is graded at the trial band for
  direction: the review is large, the comparison is within-study, and the finding
  is a dissociation rather than a magnitude, so it does not depend on a fragile
  point estimate. Manresa-Rocamora et al. 2021 (Int J Environ Res Public Health
  18(19):10299) supplies the specific test of the most popular objective
  alternative and is notable for how carefully it reports a mostly negative
  result: HRV-guided training improves the HRV metric it optimises, does not
  improve resting heart rate, and produces small non-significant differences on
  every fitness and performance outcome measured, with the authors stating that
  best methodological practice for HRV index selection, recording position and
  baseline referencing still requires study. Graded lower accordingly, and graded
  lower again for any resistance-training application, since every included study
  is endurance training. Not flagged contested: the two sources are consistent
  with each other and with the existing tracker item, and no source located
  disputes them. The proprietary readiness-score question is deliberately recorded
  as a searched-and-unfound gap on a refraction note rather than converted into a
  negative claim, because a failure to locate a validation is not the same as a
  demonstration of invalidity, and this warehouse distinguishes the two.
---

# sleep-recovery/subjective-monitoring-vs-objective-markers-011

The uncomfortable finding first: when researchers put subjective and objective
recovery measures on the same athletes and compared them, the two mostly did not
agree with each other -- and the subjective one was the better instrument.

Fifty-six studies, each measuring both. Blood markers, resting heart rate, oxygen
consumption, heart-rate response during exercise on one side; how the athlete
reported feeling on the other. They generally did not correlate. And the
self-reported measures tracked training load with better sensitivity and better
consistency: wellbeing dropped when load spiked, stayed depressed under sustained
training, and recovered when load came down. The objective markers did not follow
training response as reliably.

That is a genuinely awkward result for anyone building a data-driven system,
because it says the two-second question beats the sensor.

The most popular sensor-based alternative has been tested directly. Training
guided day-to-day by heart rate variability was compared against training planned
in advance. It reliably improved one thing: heart rate variability, the number it
was optimising. It did not improve resting heart rate. And on the outcomes people
actually train for -- maximal aerobic capacity, threshold capacity, endurance
performance -- every difference was small and none reached significance. The
researchers' own summary is that if it is better at all, it is better by a small
margin.

There is one real benefit in there that deserves not to be lost in the debunking:
guided training appeared to reduce the number of people who respond badly. Fewer
negative responders is a modest and useful claim, and it is the claim the data
support. It is not the same as everyone getting fitter.

A hard boundary on all of it: every one of those studies is endurance training.
Cyclists and runners, aerobic outcomes. There is no resistance-training
equivalent. So using a morning heart-rate-variability reading to decide whether to
squat heavy is an extrapolation from a literature that was not about lifting and
that mostly failed to find performance effects even in its own domain.

Then the thing this warehouse will not do, which is invent a verdict on the
readiness score. Rings and watches display a composite number each morning -- a
recovery score, a readiness score. This sprint searched for a peer-reviewed study
validating any of them against measured next-day physical performance and did not
find one. What exists is observational work showing the score moves when training
load and sleep move, which demonstrates that the score responds to its inputs, not
that it predicts what someone can do. Combined with what this domain already
records about how much sleep-staging accuracy varies between devices, the honest
status is unvalidated composite. Unvalidated is not the same as wrong, and this is
logged as a hole in the evidence rather than as a finding against the devices.

What falls out of all this is unglamorous. The best-evidenced recovery monitor is a
short, consistent, self-reported check-in, tracked within one person over time.
Not because subjective data is philosophically preferable, but because when the
two were measured side by side, that is the one that moved with the training.
