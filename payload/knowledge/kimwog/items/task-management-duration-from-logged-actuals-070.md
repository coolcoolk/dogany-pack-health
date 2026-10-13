---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (schedule/task-time sprint, dispatch
# kw-schedule-time). The CORRECTION half of the planning-fallacy pair: 001
# says own estimates run short, 002 says the base rate is the fix at project
# scale; this row says where the fix comes from for one person's tasks -- a
# measured duration, not a remembered one and not a multiplier.
# What was read: Roy, Mitten & Christenfeld 2008 and Roy, Christenfeld &
# McKenzie 2005 -- ABSTRACTS only (Europe PMC, 2026-10-06); no figure from
# either full text is quoted. Halkjelsvik & Jorgensen 2012 -- abstract only,
# as in cooking/duration-estimate-asymmetry-018. Buehler 1994 Study 4 is
# carried from item 001, which read it in full text.
id: task-management/duration-from-logged-actuals-070
domain: task-management
grade: B (three randomised experiments plus a narrative review pointing the same way; abstracts read, effect sizes not retrieved; single lab)
lane: "@behavioral-productivity"
locale: universal
as_of: 1994-2012
contested: no
sources:
  - "https://doi.org/10.1037/1076-898X.14.3.266"  # Roy MM, Mitten ST, Christenfeld NJS. Correcting memory improves accuracy of predicted task duration. Journal of Experimental Psychology: Applied 2008;14(3):266-275. Abstract read 2026-10-06: three experiments (paper counting, essay writing, a field sample at fast-food restaurants and arcades); supplying ACTUAL duration -- own previous or others' average -- before predicting increased predictive accuracy in all three
  - "https://doi.org/10.1037/0033-2909.131.5.738"  # Roy MM, Christenfeld NJS, McKenzie CRM. Underestimating the duration of future events: memory incorrectly used or memory bias? Psychological Bulletin 2005;131(5):738-756. Abstract read 2026-10-06: people base predictions on memories of past duration, and those memories are themselves systematic underestimates
  - "https://doi.org/10.1037/a0025996"  # Halkjelsvik T, Jorgensen M. From origami to software development: a review of studies on judgment-based predictions of performance time. Psychological Bulletin 2012;138(2):238-271. Abstract read 2026-10-06: underestimation dominant in engineering/management studies, NOT in psychology studies; performance-time vs completion-time predictions often conflated
  - "task-management/planning-fallacy-own-estimates-001"  # Buehler 1994: own estimates short; pessimism instruction does not fix accuracy; Study 4 past-experience linking removed the bias
  - "task-management/reference-class-base-rate-002"  # the outside view at project scale
  - "task-management/self-report-vs-log-divergence-008"  # why the record must be a log, not a recollection
  - "source:cooking/duration-estimate-asymmetry-018 -- the no-blanket-multiplier rule for performance-time estimates, same 2012 review"
estimate_rules:
  - rule: source-order
    value: logged actuals of the same task class (owner) > logged actuals of others for the same task class > owner's stated estimate
    basis: Roy 2008 (own or others' actual duration both improved accuracy)
    basis_grade: B
  - rule: remembered-is-not-logged
    value: a duration the owner recalls ("it took about an hour last time") is a STATED estimate, not a logged actual
    basis: Roy 2005 (memories of past duration are themselves underestimates)
    basis_grade: C
  - rule: capture-actual
    value: when a timed task closes, store actual_start, actual_end and the task class beside the original estimate
    basis: the correction needs a measured duration to exist; product rule
    basis_grade: D
  - rule: show-before-estimate
    value: when the owner states a new estimate for a class with logged actuals, show the logged figure first, then accept whatever the owner sets
    basis: Roy 2008 (feedback supplied BEFORE predicting); Buehler 1994 Study 4
    basis_grade: B
  - rule: no-blanket-multiplier
    value: never rescale the owner's estimate by a fixed factor; no measured conversion factor exists
    basis: Halkjelsvik 2012 (direction is field-dependent); 001 note; cooking 018
    basis_grade: B
  - rule: min-history
    value: speak a logged figure as "your last N" with N stated; with N below the product floor (3, a convention) show the individual values, not a mean
    basis: product constant
    basis_grade: D
refraction_notes:
  - note: >
      THE FIX IS A CHANGE OF INFORMATION SOURCE, NOT A NUMBER. All three Roy
      2008 experiments improved accuracy by putting a measured duration in
      front of the person before they predicted. Nothing in the abstracts
      read supports a percentage to add. A module that pads by 1.5x is using
      the finding's popularity, not its content.
    grade: B
  - note: >
      MEMORY IS THE CONTAMINATED INPUT. Roy 2005 argues that predictions
      inherit the bias of remembered durations. So "how long did it take
      last time?" asked of the owner returns another estimate. Only a
      timestamp pair counts as an actual. This is the same rule as
      task-management/self-report-vs-log-divergence-008 applied to task time.
    grade: C
  - note: >
      PERFORMANCE TIME VERSUS COMPLETION TIME. "How many hours of work" and
      "when will it be done" are different predictions (Halkjelsvik 2012).
      Logged actuals correct the first directly. A completion date also
      absorbs waiting, interruption and competing tasks (see
      task-management/interruption-resumption-measured-004), so a logged
      work-time is a floor for a due date, not the due date.
    grade: B
  - note: >
      NO KOREAN OR WORKPLACE-LOG STUDY. The experiments are US laboratory
      and field samples on short tasks. The direction is carried; transfer
      to a Korean adult's calendar is untested, not shown to fail (GAPS.md,
      task-management).
    grade: C
claim: >
  The workable correction for a person's optimistic task-duration estimates is
  to put a MEASURED past duration in front of them before they estimate, not
  to pad the estimate. Roy, Mitten and Christenfeld (2008) ran three
  experiments -- counting paper, writing an essay, and a field sample recruited
  at fast-food restaurants and arcades -- and in all three, supplying the
  actual duration of the person's own previous similar task, or the average
  actual duration for other people, increased predictive accuracy. Roy,
  Christenfeld and McKenzie (2005) give the mechanism: people predict from
  memories of how long similar tasks took, and those memories are themselves
  underestimates, so a recollected "last time" carries the same bias as the
  prediction. Buehler, Griffin and Ross (1994, item 001) found the bias
  removed when people were made to connect the prediction to past experience,
  and that a pessimism instruction did not improve accuracy. Halkjelsvik and
  Jorgensen (2012) limit the scope: underestimation dominates in engineering
  and management studies but not in psychology studies, and work-time
  predictions are often conflated with delivery-date predictions. So no
  fixed padding factor is licensed; a logged actual for the same kind of task
  is.
reasoning: >
  Graded in the second band under task-management/curator-checklist-016: the
  core result is experimental (feedback manipulated before prediction,
  accuracy measured against timed actuals) and replicated across three
  samples, one of them outside a university. Held below the top band because
  only the abstracts were read this pass, no effect size was retrieved, the
  work comes from one group, and the tasks are minutes-to-hours long rather
  than the days-to-weeks horizon of item 001. The memory-bias mechanism is
  carried one band lower because 2005 is a review argument whose own
  evidence was not re-read. The structured estimate_rules are for the
  lifekit schedule/task module: source order and no-multiplier rest on the
  graded rows; capture-actual and the history floor are product rules and
  are labelled D.
---

# task-management/duration-from-logged-actuals-070

When someone says a task will take an hour, the useful correction is to put
what similar tasks actually took in front of them before they decide. Padding
the number does not do this job.

Three experiments by Roy, Mitten and Christenfeld (2008) did exactly that. They
showed people the measured duration of their own previous similar task, or the
average for other people, before asking for a prediction. Accuracy went up in
all three, including a field sample recruited outside a university. The earlier
review by Roy, Christenfeld and McKenzie (2005) explains why it works. People
predict from memory, and memory of how long things took is already short. A
remembered "last time" is therefore another estimate, not a correction.

This fits the rest of the lane:

- task-management/planning-fallacy-own-estimates-001: own estimates run short,
  asking for a worst case does not fix accuracy, and anchoring on past
  experience removed the bias.
- task-management/reference-class-base-rate-002: the outside view at project
  scale.
- task-management/self-report-vs-log-divergence-008: a recollection is not a
  log.

What it does NOT license is a multiplier. The 2012 review by Halkjelsvik and
Jorgensen finds the underestimation pattern depends on the field, and it
separates "how many hours of work" from "when will it be done". A logged
work-time corrects the first. A due date also has to absorb waiting and
interruptions, so the logged figure is its floor.

## Rules for the schedule/task module (frontmatter `estimate_rules`)

| Rule | What the module does | Basis |
|---|---|---|
| source-order | owner's logged actuals > others' logged actuals > owner's stated estimate | Roy 2008 |
| remembered-is-not-logged | a recalled duration is stored as a stated estimate | Roy 2005 |
| capture-actual | on close, store start, end and task class beside the estimate | product rule |
| show-before-estimate | show the logged figure first; the owner still sets the number | Roy 2008, 001 |
| no-blanket-multiplier | never rescale an estimate by a fixed factor | Halkjelsvik 2012, cooking 018 |
| min-history | fewer than 3 logged actuals: show the values, not a mean | product constant |

## 한국어 요약 (답변용)

- 사용자가 말한 소요 시간이 짧게 잡히는 경향은 있지만, 고치는 방법은 숫자를 부풀리는 것이 아니다.
  비슷한 일에 실제로 걸린 시간(기록된 시작·종료 시각)을 예측하기 전에 보여 주는 것이다.
- "지난번엔 한 시간쯤 걸렸어"처럼 기억으로 말한 시간은 기록이 아니라 또 하나의 추정치다. 기억
  자체가 짧게 남는다.
- 1.5배처럼 정해진 배수를 곱하지 않는다. 그런 환산 계수를 측정한 연구는 없다.
- 작업 시간(몇 시간 일하나)과 완료 날짜(언제 끝나나)는 다르다. 기록된 작업 시간은 마감일의
  하한일 뿐이다.
- 기록이 3건(제품이 정한 기준) 미만이면 평균 대신 각 기록을 그대로 보여 준다.
- 근거는 미국 실험 연구이고 한국 성인 데이터는 없다. 방향은 가져오되 수치는 옮기지 않는다.
