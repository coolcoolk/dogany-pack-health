---
# Early-morning training sprint 2026-10-07 (dispatch task
# kw-ex-early-morning-training). The engine-readable synthesis of 068
# (performance / warm-up), 069 (caffeine / food) and
# sleep-recovery/sleep-loss-performance-decrement-004 (sleep loss) for the
# 04:30 morning brief (health-brief, sent BRIEF_LEAD_MIN = 30 before the
# earliest 05:00 start) and the session prep block. It is a routing rule, not
# a primary finding: each rule names the graded row it rests on, and every
# product constant (the 07:00 dawn boundary, the 360-minute short-night
# line, the 90-minute short-vs-usual delta, the extra warm-up minutes) is
# labelled as a constant. Same posture as 056.
#
# session_rules is structured data for the brief / prep code. Inputs are
# things the engine already has or can be told: the session start time
# (training windows), last night's asleep minutes (hk-ingest -> metric_log
# sleep_min, keyed by WAKE day), the sleep_baseline_hours axis, body_weight_kg,
# the user's stated caffeine habit and usual bedtime. A rule whose input is
# missing does not fire and is not asked for just to fire it.
# Renumbered at the v37 merge (provisional 072 -> 073). A sibling brief rule
# set from the sleep lane, sleep-recovery/brief-sleep-training-rules-072,
# shipped in the same release; the brief code reads both (GAPS.md).
id: exercise/early-morning-session-brief-rules-073
domain: exercise
grade: D (synthesis rule over 068, 069 and 004; each rule carries its own basis_grade; every threshold is product judgement)
lane: "@performance-lit"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/early-morning-performance-warmup-068"  # dawn power gap, warm-up offset, similar long-run adaptation, chronotype
  - "exercise/early-morning-caffeine-food-069"  # caffeine dose / timing / sleep cutoff, fasted vs fed
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # early alarm worse than late bed; AM sessions largely spared; keep the session
  - "exercise/warmup-load-rampup-progression-018"  # the load ramp the extended general warm-up goes in front of
  - "exercise/autoregulation-vs-percentage-prescription-030"  # day-to-day load adjustment after the warm-up, not before
  - "dispatch task kw-ex-early-morning-training (2026-10-07): engine-readable rules for the session brief / prep of a 05:00-06:00 trainee"
  - "framework:GRADE -- the directions are borrowed from the cited rows at their own grades; the thresholds (dawn boundary, short-night line, delta, warm-up minutes, no-test-day) are product constants with no direct evidence."
applicability:
  axes:
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [none]
constants:
  dawn_start_before: "07:00"        # product: a session starting before this is a dawn session
  short_night_min: 360              # product, borrowed from 004's exposure definition (6 h or less in 24 h)
  short_vs_usual_delta_min: 90      # product: last night this much under the user's own baseline also counts as short
  extra_general_warmup_min: [5, 10] # product; the one tested dose was 20 min (068) -- not a dose-response
  caffeine_cutoff_coffee_h: 8.8     # 069, Gardiner 2023 model estimate, ~107 mg
  caffeine_cutoff_preworkout_h: 13.2  # 069, Gardiner 2023 model estimate, ~217.5 mg
  caffeine_single_dose_ceiling_mg: 200  # 069, EFSA 2015 safety ceiling, not an ergogenic target
  short_session_max_min: 60         # 069, Aird 2018 split prolonged vs shorter aerobic
session_rules:
  - rule: dawn-extend-warmup
    trigger: session start before dawn_start_before
    action: put extra_general_warmup_min of easy general work (bike, rower, brisk walk) before the usual prep and load ramp
    brief: true
    prep: true
    basis: exercise/early-morning-performance-warmup-068
    basis_grade: C
  - rule: dawn-first-sets-feel-heavy
    trigger: session start before dawn_start_before
    action: read load and RIR from the first work set after the ramp, not from how the empty bar or first ramp set feels; no load cut on warm-up feel alone
    brief: false
    prep: true
    basis: exercise/autoregulation-vs-percentage-prescription-030
    basis_grade: D
  - rule: keep-slot-no-evening-move
    trigger: user asks whether to move training to the evening for better gains
    action: answer that morning and evening training give similar strength and size gains and the body adapts to its training hour; consistency of the slot matters more than the hour
    brief: false
    prep: false
    basis: exercise/early-morning-performance-warmup-068
    basis_grade: B
  - rule: short-night-keep-session
    trigger: last night sleep_min at or under short_night_min, or under the sleep_baseline_hours baseline by short_vs_usual_delta_min or more
    action: keep the session at its dawn slot (do not cancel, do not postpone to later in the day); apply dawn-extend-warmup; one brief line saying so
    brief: true
    prep: true
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - rule: short-night-no-test
    trigger: short-night-keep-session fired and the plan has a rep-max or new top-set test today
    action: run the planned work but move the test to the next normal-sleep session
    brief: true
    prep: false
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: D
  - rule: no-earlier-alarm
    trigger: any brief or prep advice that would need waking earlier than the user's current wake time (to eat, to warm up longer, to take caffeine earlier)
    action: never advise it; fit the advice inside the existing window instead
    brief: true
    prep: true
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - rule: dawn-caffeine-if-user
    trigger: user has said they take caffeine before training
    action: on waking (about 60 min before is the common protocol; gum or a fast source if later); dose from the 069 rescale band, default the low end; never above caffeine_single_dose_ceiling_mg as a routine line; never suggest caffeine to a non-user; pregnancy or a cardiovascular condition withholds the dose number
    brief: true
    prep: false
    basis: exercise/early-morning-caffeine-food-069
    basis_grade: B
  - rule: afternoon-caffeine-cutoff
    trigger: user's usual bedtime is known and they mention afternoon coffee or a pre-workout
    action: last coffee no later than bedtime minus caffeine_cutoff_coffee_h; last pre-workout serve no later than bedtime minus caffeine_cutoff_preworkout_h; speak as a rule of thumb
    brief: false
    prep: false
    basis: exercise/early-morning-caffeine-food-069
    basis_grade: C
  - rule: food-short-session
    trigger: strength session or any session up to short_session_max_min
    action: fasted is fine; optional small easily digested carbohydrate snack 30-60 min before by habit and gut tolerance; a proper meal after; habitual breakfast eaters training sets to failure are the ones who most likely lose reps fasted
    brief: true
    prep: false
    basis: exercise/early-morning-caffeine-food-069
    basis_grade: C
  - rule: food-long-endurance
    trigger: continuous aerobic session longer than short_session_max_min
    action: carbohydrate during the session; the 1-4 h pre-meal window does not fit a dawn start
    brief: true
    prep: false
    basis: exercise/early-morning-caffeine-food-069
    basis_grade: D
refraction_notes:
  - note: >
      THE DIRECTIONS ARE EVIDENCE, THE THRESHOLDS ARE NOT. Keep a dawn session
      after a short night (004), warm up longer at dawn (068), fasted is fine
      for an hour of lifting (069): each has a graded row. The 07:00 dawn
      line, the 360-minute and 90-minute short-night lines, the 5-10 extra
      warm-up minutes and the no-test-after-a-short-night rule are product
      constants. Speak them as the plan's rule, never as a measured cut-off.
    grade: D
  - note: >
      SHORT NIGHT AT DAWN: KEEP IT, DO NOT SHIFT IT LATER. 004's own advice is
      to prioritise morning exercise after sleep loss, because the decrement
      grows by roughly 0.4% per hour awake. Postponing a dawn session to the
      evening after a bad night is the one move the evidence argues against.
      Note the pooled AM effect in that meta-analysis was still negative
      (-5.4%, CI -9.7 to -1.2) even though the authors describe AM tasks as
      largely unaffected -- so "keep it" is right, "it costs nothing" is not.
    grade: B
  - note: >
      THE TYPICAL DAWN LIFTER'S SLEEP LOSS IS THE HARMFUL KIND. A fixed 05:00
      start with a late bedtime is late restriction (woken earlier than the
      body would wake), the pattern 004 found consistently harmful. The
      session itself is spared by being early; what the brief can actually
      protect is the bedtime. Any brief line about sleep should point at the
      evening, not the morning.
    grade: B
  - note: >
      ONE SLEEP LINE, NOT A SCORE. The tracker's asleep minutes are an
      estimate (sleep-recovery/tracker-accuracy-003), so the rules use one
      coarse line and the user's own baseline rather than a graded readiness
      score; no rule cuts load on the sleep number alone.
    grade: D
claim: >
  For a 05:00-06:00 trainee the morning brief and prep follow ten rules:
  extend the general warm-up before the usual prep and ramp at a dawn start;
  read the day's load from the first work set, not from how the bar feels
  cold; never advise moving to the evening for gains; after a short night keep
  the session at its dawn slot and warm up longer, but move any max test to a
  normal-sleep day; never advise waking earlier to eat, warm up or dose
  caffeine; for caffeine users, dose on waking at the low end of the band and
  stop afternoon coffee about 8.8 h (pre-workout about 13.2 h) before
  bedtime; train fasted or with a small carbohydrate snack for sessions up to
  an hour and eat properly after; take carbohydrate during long dawn
  endurance work. The directions carry the grades of 068, 069 and 004; the
  boundaries are product constants.
reasoning: >
  The rules are read directly off the three graded rows. 068 supplies the
  warm-up extension (C, one small crossover plus mechanism) and the
  keep-the-slot answer (B, training-study meta-analysis). 004 supplies the
  keep-the-session-after-a-short-night rule (B, the authors' own conclusion)
  and the no-earlier-alarm rule (B, late restriction is the harmful
  pattern). 069 supplies caffeine dose, timing and afternoon cutoff (B
  direction, C cutoffs) and the fasted-is-fine-for-short-sessions rule (B on
  the aerobic split, C on the one resistance trial). The no-test-after-a-short
  night and first-set-not-bar-feel rules are product judgement (D): no trial
  tested rep-max testing after short sleep at dawn, and the autoregulation
  row (030) supports adjusting from work-set performance but not a specific
  rule. The safety axes are hard with block_specifics because the caffeine
  rule names a dose band.
---

# exercise/early-morning-session-brief-rules-073 -- 새벽 운동 브리핑·준비 규칙

**한 줄 그림:** 새벽엔 워밍업을 늘리고, 잠을 못 잤어도 그 시간에 하고, 먹거나 커피 마시려고 더 일찍
일어나지 않는다.

## The rules

| Rule | Fires when | Does | Basis row |
|---|---|---|---|
| dawn-extend-warmup | start before 07:00 (product) | +5-10 min easy general work before prep and ramp | 068 |
| dawn-first-sets-feel-heavy | start before 07:00 | judge load from the first work set, not the cold bar | 030 |
| keep-slot-no-evening-move | user asks about moving to evening | similar gains either way; keep the slot | 068 |
| short-night-keep-session | slept <= 6 h, or >= 90 min under own baseline (product) | keep the dawn session, warm up longer | 004 |
| short-night-no-test | short night + a max test today | do the work, move the test | 004 |
| no-earlier-alarm | any advice needing an earlier wake | never | 004 |
| dawn-caffeine-if-user | user takes caffeine | on waking, low end of 3-6 mg/kg, no routine dose over 200 mg | 069 |
| afternoon-caffeine-cutoff | bedtime known + afternoon caffeine | coffee by bedtime - 8.8 h, pre-workout by bedtime - 13.2 h | 069 |
| food-short-session | session up to about 60 min | fasted fine, or a small carb snack 30-60 min before; eat after | 069 |
| food-long-endurance | continuous aerobic over about 60 min | carbohydrate during | 069 |

The directions carry the grades of their basis rows; the times and minute counts are product
constants.

## 한국어 요약 (답변용)

- 7시 전에 시작하는 운동이면 평소 준비 운동과 무게 올리기 전에 가벼운 전신 운동(실내자전거, 로잉,
  빠르게 걷기)을 5~10분 더한다. 5~10분은 제품이 정한 값이고, 연구에서 시험한 건 20분이었다.
- 새벽엔 빈 봉이나 첫 워밍업 세트가 무겁게 느껴지는 게 정상이다. 오늘 무게는 첫 본세트를 보고 정한다.
- 근육을 더 키우려고 저녁으로 옮길 필요는 없다. 아침이든 저녁이든 근력·근육 증가는 비슷하다.
  시간대를 일정하게 지키는 게 낫다.
- 어젯밤 6시간 이하로 잤거나 평소보다 1시간 반 넘게 덜 잤으면, 운동은 빼지 말고 그 시간에 그대로
  하고 워밍업을 늘린다. 저녁으로 미루는 게 오히려 손해다. 깨어 있는 시간이 길수록 수행력이 더
  떨어지기 때문이다. 다만 그날 최대 무게 테스트는 잠을 제대로 잔 날로 옮긴다.
- 먹거나 워밍업을 늘리거나 커피를 마시려고 더 일찍 일어나라고 하지 않는다. 일찍 깨서 줄어든 잠이 가장
  해롭다. 잠 이야기는 아침이 아니라 저녁 취침 시각 쪽으로 한다.
- 카페인을 원래 먹는 사람에게만: 일어나자마자, 체중당 3~6mg 범위의 아래쪽으로. 한 번에 200mg을
  넘는 양을 기본으로 권하지 않는다. 안 먹는 사람에게 권하지 않는다. 임신 중이거나 심혈관 질환이 있으면
  양을 말하지 않는다.
- 오후 커피는 취침 8.8시간 전, 프리워크아웃은 13.2시간 전까지. 대략의 기준으로 말한다.
- 한 시간 안팎의 근력운동은 공복도 괜찮다. 먹는다면 30~60분 전에 소화 쉬운 탄수화물을 조금. 운동 후엔
  제대로 먹는다. 한 시간 넘게 이어지는 지구력 운동이면 운동 중에 탄수화물을 먹는다.
