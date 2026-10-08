---
# Collection sprint 2026-09-02. Closes the "timing of training relative to
# sleep" question in the direction almost nobody expects: the standard advice
# against evening exercise is not supported by the polysomnography evidence. The
# item deliberately carries the meta-analysis's own fragility disclosure (all
# significant moderator effects vanished when one study was removed), because
# that disclosure is what keeps this from being over-sold in the opposite
# direction. Rubric: sleep-recovery @clinical (VC-A).
# Source re-audit 2026-10-06: Stutz 2019 abstract re-read (PubMed 30374942),
# all numbers verified. Two later sources added as one note, nothing removed:
# Frimpong 2021 (trials, high intensity) and Leota 2025 (wearable cohort).
id: sleep-recovery/evening-training-sleep-effect-010
domain: sleep-recovery
grade: B (evening exercise does not harm sleep); C (the vigorous-within-one-hour caveat); D (all moderator effects)
lane: "@clinical"
locale: universal
as_of: 2019
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/30374942/"  # Stutz J, Eiholzer R, Spengler CM. 2019, Sports Med 49(2):269-287, doi 10.1007/s40279-018-1015-0 -- 11,717 references screened, 23 studies included, sleep measured against a no-exercise control
  - "https://pubmed.ncbi.nlm.nih.gov/24933083/"  # Buman MP, Phillips BA, Youngstedt SD, Kline CE, Hirshkowitz M. 2014, Sleep Med 15(7):755-761, doi 10.1016/j.sleep.2014.01.008 -- CORROBORATING ONLY and much weaker: cross-sectional self-report poll of 1000 US adults; evening moderate or vigorous exercisers did not differ from non-exercisers on any reported sleep metric
  - "https://pubmed.ncbi.nlm.nih.gov/34416428/"  # Frimpong E, Mograss M, Zvionow T, Dang-Vu TT. 2021, Sleep Med Rev 60:101535, doi 10.1016/j.smrv.2021.101535, PROSPERO CRD42020218299 -- 15 acute evening high-intensity studies, 194 participants, good sleepers aged 18-50
  - "https://pubmed.ncbi.nlm.nih.gov/40234380/"  # Leota J, Presby DM, Le F, Czeisler ME, Mascaro L, Capodilupo ER, Wiley JF, Drummond SPA, Rajaratnam SMW, Facer-Childs ER. 2025, Nat Commun 16(1):3297, doi 10.1038/s41467-025-58271-x -- OBSERVATIONAL, 14,689 wearable (WHOOP) users, 4,084,354 person-nights
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # the reverse direction: how sleep loss affects the session, versus how the session affects sleep
  - "framework:GRADE -- upgraded relative to most of this domain because the outcomes are polysomnographic sleep architecture measured against a no-exercise control condition, not self-report. Downgraded for indirectness (single acute exercise sessions in healthy adults, not a resistance-training programme) and, for the moderators specifically, for extreme fragility: the authors report that ALL significant moderating effects disappeared after removal of one study."
applicability:
  axes:
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The single most important sentence in the source is its fragility
      disclosure, and it applies to the moderators, not to the headline. The
      authors state that all significant moderating effects disappeared after
      removal of one study. That means the specific quantities attached to
      bedtime temperature, physical-stress level and running-versus-cycling
      should be treated as unreliable. What does NOT depend on that one study is
      the main comparison: evening exercise versus no evening exercise on sleep
      architecture.
    grade: D
  - note: >
      The one caveat the authors keep is a narrow and practically actionable
      window. Sleep-onset latency, total sleep time and sleep efficiency MIGHT be
      impaired after VIGOROUS exercise ending one hour or less before bedtime.
      Note the hedging in the source's own language and the tightness of the
      window -- the finding is about finishing hard work immediately before lying
      down, not about training in the evening in general.
    grade: C
  - note: >
      The measured direction is mildly favourable and the magnitudes are small.
      Compared with a no-exercise control, evening exercise increased REM latency
      by 7.7 minutes, increased slow-wave sleep by 1.3 percentage points, and
      decreased stage 1 sleep by 0.9 percentage points. Slow-wave sleep up and
      light sleep down is a favourable direction in conventional terms, but these
      are small architectural shifts, not a claim that evening training makes
      sleep better in any way anyone would notice.
    grade: B
  - note: >
      Design scope. The included studies evaluate sleep after a SINGLE session of
      evening physical exercise in healthy adults against a no-exercise control.
      Nothing here addresses a repeated resistance-training programme, and the
      exercise modalities discussed by the moderator analysis are running and
      cycling. Transfer to a four-times-weekly barbell schedule is an
      extrapolation and must be spoken as one.
    grade: C
  - note: >
      A second source points the same way but is much weaker and is carried as
      corroboration only. A cross-sectional poll of 1000 US adults found that,
      after adjustment for confounders, evening moderate or vigorous exercisers
      did not differ from non-exercisers on any reported sleep metric, and its
      authors concluded that sleep-hygiene recommendations should not discourage
      evening exercise. It is self-reported and cross-sectional, so it cannot
      carry the claim on its own; it matters only because it agrees with the
      polysomnography evidence rather than being the basis for it.
    grade: D
  - note: >
      Added at the 2026-10-06 re-audit: where the window sits. A 2021
      meta-analysis restricted to HIGH-intensity evening exercise (15 acute
      studies, 194 good sleepers aged 18 to 50) found that sessions ending 0.5
      to 4 hours before bed lowered REM sleep by 2.34 percent and changed
      nothing else, and that regular evening high-intensity training did not
      disrupt sleep; its authors conclude that a session ending 2 to 4 hours
      before bed does not disrupt sleep. A 2025 wearable cohort (14,689 people,
      about four million nights, observational) found later and harder
      sessions associated with later sleep onset, shorter and lower-quality
      sleep, higher night-time heart rate and lower heart-rate variability --
      and no association at all when the session ended 4 or more hours before
      sleep onset. The trials and the cohort agree that ending well before bed
      is safe; they disagree on how close is too close (trials: about one hour;
      cohort: associations from under four hours, larger with harder
      sessions). The cohort cannot separate the session from whatever makes
      someone train late, so it moves the near-bedtime caveat, not the
      headline.
    grade: C
  - note: >
      Direction of the question matters. This item is about how the SESSION
      affects the SLEEP. The reverse question -- how poor sleep affects the
      session -- is item 004, and it has both a stronger evidence base and a
      practical answer that points the other way (train earlier after a bad
      night). The two must not be merged into one statement about timing.
    grade: B
claim: >
  The standard advice against exercising in the evening is not supported by the
  polysomnography evidence. A systematic review and meta-analysis screening 11,717
  references and including 23 studies, each comparing sleep after a single evening
  exercise session against a no-exercise control in healthy adults, concluded that
  the studies reviewed do not support the hypothesis that evening exercise
  negatively affects sleep -- and if anything point the other way. Measured against
  control, evening exercise increased rapid-eye-movement latency by 7.7 minutes,
  increased slow-wave sleep by 1.3 percentage points, and decreased stage 1 sleep
  by 0.9 percentage points: small shifts, in the conventionally favourable
  direction. The authors retain one narrow caveat -- sleep-onset latency, total
  sleep time and sleep efficiency MIGHT be impaired after VIGOROUS exercise ending
  one hour or less before bedtime. Every moderator result in the analysis (bedtime
  temperature, relative physical stress, running versus cycling) must be discarded
  as unreliable, because the authors report that all significant moderating
  effects disappeared after removal of a single study. Scope limit: these are
  single acute sessions in healthy adults, predominantly running and cycling, not
  a repeated resistance-training programme. The operative rule: training in the
  evening is not a sleep problem; finishing hard work immediately before lying
  down might be.
reasoning: >
  Stutz et al. 2019 (Sports Med 49(2):269-287) is unusually well positioned to
  answer this question because its outcomes are polysomnographic sleep
  architecture measured against a no-exercise control condition rather than
  self-reported sleep quality, which removes the expectation-effect problem that
  dominates most recovery literature and that
  exercise/recovery-modality-soreness-vs-performance-024 documents at length. That
  is why the main finding is graded at the trial band while most of this domain
  sits lower. The search was large (11,717 references screened to 23 inclusions)
  and the analyses were random-effects throughout. The main result is a negative
  finding against a widely held recommendation, and the authors state it plainly:
  the reviewed studies do not support the hypothesis that evening exercise
  negatively affects sleep, in fact rather the opposite. The reason this item
  nonetheless refuses to grade the details highly is the authors' own disclosure
  that all significant moderating effects disappeared after removal of one study
  -- a fragility statement that would normally be buried and here is printed in
  the abstract. Taken seriously, it means the moderator numbers are one-study
  artefacts and must not be repeated as findings, while the primary comparison,
  which does not rest on that study, stands. The retained caveat about vigorous
  exercise ending within an hour of bedtime is carried at a lower band because
  the source's own language is conditional. Not flagged contested: no source
  located in this sprint argues the opposite, and the common recommendation this
  overturns is a practitioner convention rather than a competing evidence base.
  The real risk with this item is over-application, not dispute, so the scope
  limits are carried as refraction notes -- acute single sessions, healthy adults,
  running and cycling, not a barbell programme.
---

# sleep-recovery/evening-training-sleep-effect-010

"Do not train late, it will wreck your sleep" is one of those rules that everyone
repeats and the measurements do not back.

A systematic review screened nearly twelve thousand papers and kept twenty-three,
all of which measured sleep in a laboratory after a single evening exercise
session and compared it against the same people not exercising. The conclusion was
that the evidence does not support the idea that evening exercise harms sleep, and
that if anything it points the other way.

The measured changes are small and mildly favourable: slightly more deep sleep,
slightly less light sleep, a somewhat later first REM period. Nothing dramatic.
The useful part is not that evening training improves sleep -- it is that the
feared harm did not appear.

One caveat survives, and it is worth keeping because it is specific. The authors
allow that time to fall asleep, total sleep and sleep efficiency might be impaired
after vigorous exercise finishing within an hour of bedtime. That is a narrow
window, and note the hedge in their own wording. The problem, if there is one, is
finishing hard work and immediately lying down, not training in the evening.

Now the part that most summaries of this paper omit. The review also looked at
what might modify the effect -- body temperature at bedtime, how hard the session
was relative to the person's normal activity, running compared with cycling -- and
reported numbers for each. Then it disclosed that every one of those significant
moderator effects vanished when a single study was removed from the analysis.
That is an honest thing to publish and a decisive thing to act on: those numbers
are one-study artefacts and should not be quoted. The main comparison does not
depend on that study, so it stands.

Boundaries. These were single sessions, in healthy adults, mostly running and
cycling. Nobody in this dataset was four sessions deep into a barbell week.
Applying it to that is a reasonable inference and should be stated as an
inference.

And one distinction that must never blur. This item answers how the session
affects the sleep. The opposite question -- how bad sleep affects the session --
is answered separately in this domain, on stronger evidence, and its practical
advice runs the other way: after a short night, move the session earlier in the
day, because the deficit grows the longer you have been awake.
