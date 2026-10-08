---
# Sleep-regularity sprint 2026-10-07. The engine-readable synthesis for
# briefs of the WEEKLY, REGULARITY and APPETITE sleep statements: which of
# them a morning or training brief may make, from what data, at what
# strength. A routing rule, not a primary finding -- same posture as
# exercise/caution-severity-ladder-056. Each rule names the graded row it
# rests on; every minute boundary not taken from a source's exposure
# definition is labelled a product constant.
#
# v38 MERGE (2026-10-07, dispatch kw-consolidate-2): written in parallel with
# the v37 sleep-training sprint as provisional sleep-recovery/
# sleep-rules-brief-072. Its single-night performance rules (short-night,
# slightly-short-night, short-night-pm-session, early-wake-cut, nap-offer)
# restated rules v37 already ships in sleep-recovery/
# brief-sleep-training-rules-072 (short-night-morning, short-night-later,
# early-alarm-pattern, nap-repay) and exercise/
# early-morning-session-brief-rules-073. They were dropped here, not shipped
# twice; this row keeps only what neither v37 row says, and the slug was
# changed so the two rows do not read alike.
#
# sleep_rules is structured data for brief / fatigue code (field guide:
# docs/kimwog-sleep-rules-fields.md). It sits beside 072's brief_rules, and
# 072's guards (one sleep line per brief, never cancel on sleep alone,
# missing means no line) govern both blocks. DATA REALITY (2026-10-07):
# hk-ingest stores ONE number per night -- metric_log sleep_min, asleep
# minutes summed per WAKE day, naps on that day included. Onset and wake
# CLOCK TIMES are present in the transporter events but are NOT stored.
# Rules with needs: onset_wake_times cannot fire until they are; they are
# listed so the next build knows what to store, not so a brief guesses at
# them. The same holds for 072's early-alarm-pattern.
id: sleep-recovery/regularity-appetite-brief-rules-016
domain: sleep-recovery
grade: D (synthesis rule over 004, 013, 014 and 015; each rule's basis_grade is the strength of its own row, every product constant is product judgement)
lane: "@clinical"
locale: universal
as_of: 2026
contested: no
sources:
  - "sleep-recovery/brief-sleep-training-rules-072"  # the single-night rules (short night by session time, early alarm, nap) and the brief guards; this row adds the weekly, regularity and appetite rules beside them
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # <=6 h exposure definition; early-wake worse than late-bed
  - "sleep-recovery/hour-target-is-a-threshold-consensus-013"  # 7 h is a population floor, not a target, no upper bound
  - "sleep-recovery/regularity-vs-duration-014"  # timing consistency is a second axis; no measured cut-off; catch-up contested
  - "sleep-recovery/short-sleep-appetite-weight-015"  # intake up after short sleep; lean-mass share in a cut
  - "sleep-recovery/early-morning-session-071"  # repeated short nights before 05:00-06:00 sessions; the bedtime anchor
  - "sleep-recovery/tracker-accuracy-003"  # wearable sleep minutes are estimates
  - "sleep-recovery/adult-injury-risk-not-established-006"  # no injury claim from short sleep in adults
  - "nutrition/unlogged-day-not-zero-019"  # a missing night is missing, not zero
  - "https://pubmed.ncbi.nlm.nih.gov/25222347/"  # Sargent C, Lastella M, Halson SL, Roach GD. 2014, Chronobiol Int 31(10):1160-1168, doi 10.3109/07420528.2014.957306 -- 70 nationally ranked athletes, 7 sports, 2 weeks actigraphy: average 6.5 h asleep in 8.3 h in bed; nights before training days shorter with earlier onset AND offset; shorter sleep -> higher pre-training fatigue; early starts named as the cause. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/24444223/"  # Sargent C, Halson S, Roach GD. 2014, Eur J Sport Sci 14 Suppl 1:S310-S315, doi 10.1080/17461391.2012.696711 -- elite swimmers, 06:00 sessions: 5.4 h asleep before training days (bed 22:05, up 05:48) vs 7.1 h before rest days (bed 00:32, up 09:47). Abstract read.
  - "framework:GRADE -- each rule inherits its basis row's grade (short-night appetite B; cut-phase lean-mass C; weekly floor B as a population floor; regularity C). Early-start schedules cutting sleep is observational in elite athletes (two cohorts, one group). The 7- and 14-day windows, the 5-night minimum, the 60-minute wake-time spread, the 120-minute lie-in and the 3-of-7 count are product constants."
applicability:
  axes:
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
sleep_rules:
  - rule: evening-appetite
    needs: [sleep_min]
    when: last night's sleep_min is below 360 (the line 072's short-night rules use), or 2 of the last 3 nights are below 360
    threshold_min: 360
    threshold_kind: source exposure definition (004, 015 studies used 4-5.5 h opportunities)
    brief_action: expect more evening hunger today; plan dinner and an after-dinner option rather than rely on willpower
    never_say: a kcal number for this user; that the user lacks discipline
    basis: sleep-recovery/short-sleep-appetite-weight-015
    basis_grade: B
  - rule: cut-phase-sleep
    needs: [sleep_min, primary_goal]
    when: primary_goal is fat loss and the 7-night mean of sleep_min is below 420 with at least 5 nights recorded
    threshold_min: 420
    threshold_kind: population floor (013); 7-night window and 5-night minimum are product constants
    brief_action: say that in a calorie deficit short sleep shifted loss toward lean mass in trials, so sleep is part of protecting muscle this phase
    never_say: how much muscle the user is losing; a weekly weight figure caused by sleep
    basis: sleep-recovery/short-sleep-appetite-weight-015
    basis_grade: C
  - rule: weekly-floor
    needs: [sleep_min]
    when: 7-night mean of sleep_min is below 420 with at least 5 nights recorded
    threshold_min: 420
    threshold_kind: population floor (013); window is a product constant
    brief_action: one line, at most once a week, that the week ran under the commonly cited 7 h floor
    never_say: a score; a target to hit; an upper limit
    basis: sleep-recovery/hour-target-is-a-threshold-consensus-013
    basis_grade: B
  - rule: missing-night
    needs: [sleep_min]
    when: no sleep_min row for the wake day
    threshold_min: none
    threshold_kind: data rule
    brief_action: say nothing about last night (072 guard); count the night as missing, not short, in every window of this block
    never_say: that the user slept badly or did not sleep
    basis: nutrition/unlogged-day-not-zero-019
    basis_grade: D
  - rule: early-start-schedule
    needs: [onset_wake_times]
    when: the user has a fixed early start (training or work) on 3 or more of the last 7 days and sleep_min on those nights averages 60 or more minutes below other nights
    threshold_min: 60
    threshold_kind: product constant; the pattern itself is observational (Sargent 2014)
    brief_action: name the pattern (early starts shorten the night before); the lever is an earlier bedtime on the nights before early starts, not a longer lie-in afterwards
    never_say: that the early start must be dropped; a required bedtime
    basis: https://pubmed.ncbi.nlm.nih.gov/25222347/
    basis_grade: C
  - rule: irregular-week
    needs: [onset_wake_times]
    when: SD of wake time across the last 7 nights is above 60 minutes with at least 5 nights recorded
    threshold_min: 60
    threshold_kind: product constant (no measured cut-off exists, 014)
    brief_action: at most once a week; suggest anchoring the wake time, including days off
    never_say: a mortality or heart-risk figure; that irregular sleep is costing muscle
    basis: sleep-recovery/regularity-vs-duration-014
    basis_grade: C
  - rule: late-lie-in
    needs: [onset_wake_times]
    when: a day-off wake time is 120 or more minutes later than the 14-day median wake time
    threshold_min: 120
    threshold_kind: product constant
    brief_action: if the week was short, the extra sleep is fine; suggest getting it by an earlier bedtime or a nap next time, keeping wake time near usual
    never_say: that catch-up sleep is harmful
    basis: sleep-recovery/regularity-vs-duration-014
    basis_grade: C
refraction_notes:
  - note: >
      THIS ROW ADDS NO SINGLE-NIGHT PERFORMANCE FLAG. The short-night,
      early-alarm and nap lines live in 072 (and the dawn-session lines in
      exercise 073). What a short night adds here is the evening-hunger
      line. Between 6 and 7 hours no line in either row speaks about
      performance; that band is under a population floor, not inside the
      experimental exposure.
    grade: B
  - note: >
      EARLY STARTS ARE WHERE THE EARLY ALARM COMES FROM. With the same lost
      hours, being woken early carried the consistent performance decrement
      and going to bed late did not (004, 072 early-alarm-pattern).
      Early-start schedules produce exactly this pattern in elite athletes
      (5.4 h before 06:00 swims vs 7.1 h before rest days). So the lever on
      an early-start schedule is the bedtime the night before, not a longer
      lie-in afterwards.
    grade: B
  - note: >
      NUMBERS IN THESE RULES ARE OF THREE KINDS. 360 minutes is a source
      exposure definition; 420 minutes is a consensus population floor; 60
      minutes of wake-time spread, the 120-minute lie-in, the 7- and 14-day
      windows, the 5-night minimum and the 3-of-7 count are product
      constants. A brief speaks the first as "the line studies used", the
      second as "the commonly cited floor", and the third as "this plan's
      rule".
    grade: D
  - note: >
      THE TIMING RULES ARE NOT LIVE YET. early-start-schedule, irregular-week
      and late-lie-in need onset and wake clock times, which the current
      ingest drops after summing minutes -- and so does 072's
      early-alarm-pattern. Until they are stored, a brief must not infer
      wake time from anything else.
    grade: D
  - note: >
      EVERY SLEEP NUMBER IS A WEARABLE ESTIMATE, AND NAPS ARE INSIDE IT.
      sleep_min sums every asleep span ending on the wake day, so a nap
      raises it. Speak minutes as "your tracker recorded", never as measured
      sleep.
    grade: B
claim: >
  Beside the single-night rules 072 already ships, a brief may make a small
  number of weekly, regularity and appetite statements, each tied to a graded
  row and to data the system actually holds. From nightly asleep minutes
  alone: after a night under 6 hours, or two of three, expect more evening
  hunger; in a fat-loss phase, a week averaging under 7 hours earns a
  lean-mass protection note; a week under 7 hours otherwise earns one weekly
  floor line; a missing night is missing, never short. With onset and wake
  times (not stored today): early-start schedules systematically shorten the
  night before, so the lever is an earlier bedtime then; a wide wake-time
  spread earns a once-weekly anchor-your-wake-time suggestion; a long lie-in
  is acceptable repayment but an earlier bedtime or nap is preferred. Every
  minute boundary not copied from a source is a product constant and is
  spoken as one.
reasoning: >
  The rules are the operational shadow of four graded rows, chosen so that
  each statement a brief can make is no stronger than its row. 013 supplies
  the 7-hour line as a population floor, which is why it gates weekly notes
  only; 015 supplies the appetite and cut-phase statements; 014 supplies the
  regularity statements and their lack of a cut-off; 004 supplies the 6-hour
  exposure line the appetite rule shares with 072. The early-start rule rests
  directly on Sargent 2014's two actigraphy cohorts, which show the mechanism
  (earlier onset and offset, shorter sleep, more pre-training fatigue) but no
  performance outcome; it is graded at the observational band and its advice
  is limited to bedtime timing. The data split is deliberate: hk-ingest keeps
  only summed minutes per wake day, so rules needing clock times are declared
  but marked as not firing, rather than letting a brief guess wake time.
  Frequency caps (once a week for floor and regularity lines) and 072's
  one-sleep-line guard keep a sleep note from becoming a daily nag,
  consistent with the record-is-not-behaviour and observation-without-
  surveillance rows in other domains.
---

# sleep-recovery/regularity-appetite-brief-rules-016 -- 브리핑용 수면 규칙 (주간·규칙성·식욕)

**한 줄 그림:** 하룻밤 기준 운동 경고는 072가 맡는다. 이 규칙은 주간 평균, 감량기, 기상 시각의 규칙성,
짧게 잔 날의 식욕을 맡고, 근거 없는 분 단위 숫자는 제품 규칙이라고 밝힌다.

## The rules

| Rule | Needs | Fires when | Line kind | Basis |
|---|---|---|---|---|
| evening-appetite | sleep_min | last night under 360, or 2 of last 3 | source definition | 015 |
| cut-phase-sleep | + primary_goal | fat loss, 7-night mean under 420 | floor + product window | 015 |
| weekly-floor | sleep_min | 7-night mean under 420 | floor + product window | 013 |
| missing-night | sleep_min | no row | data rule | nutrition 019 |
| early-start-schedule | wake times | 3 of 7 early starts, nights 60+ min shorter | product | Sargent 2014 |
| irregular-week | wake times | wake SD over 60 min | product | 014 |
| late-lie-in | wake times | day-off wake 120+ min late | product | 014 |

Single-night rules (short night by session time, early alarm, nap) are in
sleep-recovery/brief-sleep-training-rules-072; its guards cover this block too.
Rules needing wake times do not fire until onset and wake times are stored.

## 한국어 요약 (답변용)

- 하룻밤만 보고 하는 운동 경고(6시간 미만, 일찍 깬 날, 낮잠)는 072 규칙이 맡는다. 6~7시간은 어느 쪽에서도
  성능 경고를 하지 않는다. 7시간은 인구 기준의 최저선이지 목표 점수가 아니다.
- 짧게 잔 날은 저녁에 배가 더 고플 수 있다고 미리 알려주고, 저녁 식사 계획을 세우게 돕는다.
  개인 칼로리 숫자는 말하지 않는다.
- 감량 중인데 한 주 평균이 7시간 미만이면, 연구에서 잠을 줄이면 지방보다 근육 쪽이 더 빠졌다는
  점을 한 줄로 알려준다.
- 새벽 운동·출근이 있는 날 전날은 잠이 짧아지기 쉽다. 늦잠으로 메우기보다 전날 일찍 자는 쪽을 권한다.
- 기상 시각이 매일 크게 다르면 주 1회만, 쉬는 날에도 비슷한 시각에 일어나자고 제안한다. 몇 분
  기준은 제품 규칙이다.
- 기록이 없는 밤은 "못 잤다"가 아니라 "기록 없음"이다. 수면 분은 웨어러블 추정치이고 낮잠도
  포함돼 있다고 말한다.
