---
# Sleep-training sprint 2026-10-06 (dispatch kw-sleep-training-2). The
# engine-readable synthesis of 004, 009, 010, 070 and 071 for a health /
# brief module, in the same posture as exercise/caution-severity-ladder-056:
# a routing rule, not a primary finding. Each rule names the graded row it
# rests on and labels every time / minute constant as a product constant.
#
# brief_rules is structured data. Inputs are things the product already has
# or can ask once: sleep_min (hk-ingest, asleep minutes, keyed to the wake
# day), planned session start and end, stated usual bedtime, stated last
# caffeine time and dose. Output is a level (none / note / hedge / flag) and a
# copy key -- never a readiness score and never a cancelled session.
# Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/brief-sleep-training-rules-072
domain: sleep-recovery
grade: D (synthesis rule over 004, 009, 010, 070, 071; each rule's direction carries its own basis grade, every threshold is product judgement)
lane: "@clinical"
locale: universal
as_of: 2026
contested: no
sources:
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # short night: AM tasks little affected, loss grows with hours awake; early alarm worse than late bedtime
  - "sleep-recovery/nap-force-null-shuttle-signal-009"  # nap 30 to under 60 min, more than 1 h before the effort; repays a short night; force does not move
  - "sleep-recovery/evening-training-sleep-effect-010"  # evening training is not a sleep problem; the window before bed is the caveat
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # dose x hours-before-bed table
  - "sleep-recovery/early-morning-session-071"  # 05:00-06:00 rules: bedtime anchor, wake buffer, morning numbers
  - "sleep-recovery/subjective-monitoring-vs-objective-markers-011"  # why the brief does not speak a composite readiness score
  - "sleep-recovery/tracker-accuracy-003"  # sleep_min is a wearable estimate, not polysomnography
  - "sleep-recovery/hour-target-is-a-threshold-consensus-013"  # 7 h is a threshold consensus, not a personal target
  - "sleep-recovery/regularity-appetite-brief-rules-016"  # (v38) the weekly, regularity and appetite brief rules beside this row's single-night rules; the brief_guards here govern its sleep_rules block too
  - "framework:GRADE -- the DIRECTIONS (keep the morning session after a short night, nap to repay, caffeine against bedtime, hard work well before bed) rest on B and C rows. The thresholds (360 and 420 minutes, 3 of 7 nights, 1 h and 4 h windows, nap end time) are product constants with no direct evidence for these exact numbers."
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
brief_rules:
  - id: short-night-morning
    when: sleep_min < 360 and the next session starts before 10:00
    level: note
    say: keep the session; skip any max test or new top single today; repay with a nap and an earlier bedtime
    product_constant: true
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - id: short-night-later
    when: sleep_min < 360 and the next session starts at 10:00 or later
    level: hedge
    say: if the day allows, train earlier rather than later; hedge targets; do not cancel on sleep alone
    product_constant: true
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - id: early-alarm-pattern
    when: wake-up was earlier than the user's usual by 60 min or more and sleep_min < 360
    level: note
    say: an early alarm costs more than a late bedtime; protect tomorrow's wake time
    product_constant: true
    basis: sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - id: repeated-short-nights
    when: sleep_min < 360 on 3 or more of the last 7 nights
    level: flag
    say: the schedule is cutting sleep; move lights-out earlier (about 7.5 h before wake-up) or move a session; not a single-night problem
    product_constant: true
    basis: sleep-recovery/early-morning-session-071
    basis_grade: C
  - id: nap-repay
    when: sleep_min < 360 and the day allows a nap
    level: note
    say: a 30 to under 60 min nap in the early afternoon helps feel less tired; wake from it more than 1 h before training or driving; it will not raise strength
    product_constant: true
    basis: sleep-recovery/nap-force-null-shuttle-signal-009
    basis_grade: C
  - id: nap-not-a-strength-tool
    when: user asks whether a nap will make the lift stronger
    level: note
    say: naps reduce fatigue and help repeated running; muscle force did not change in the trials
    product_constant: false
    basis: sleep-recovery/nap-force-null-shuttle-signal-009
    basis_grade: B
  - id: caffeine-late
    when: stated last caffeine is inside the caffeine_cutoff product_hours of 070 for its dose (unknown dose = about 200 mg row)
    level: hedge
    say: this dose this close to bed is likely to cost sleep even if it does not feel that way
    product_constant: false
    basis: sleep-recovery/caffeine-bedtime-cutoff-070
    basis_grade: B
  - id: caffeine-morning-session
    when: session starts 05:00-06:00 and the user asks about pre-workout caffeine
    level: none
    say: about 3 mg/kg about 60 min before is a reasonable offset for the morning dip and does not reach tonight's sleep; never above 6 mg/kg
    product_constant: false
    basis: sleep-recovery/early-morning-session-071
    basis_grade: B
  - id: evening-hard-close-to-bed
    when: a hard session ends 60 min or less before the usual bedtime
    level: hedge
    say: finishing hard work right before bed may delay sleep; finish earlier or keep the last part light
    product_constant: true
    basis: sleep-recovery/evening-training-sleep-effect-010
    basis_grade: C
  - id: evening-hard-1-to-4h
    when: a hard session ends 1 to 4 h before the usual bedtime
    level: note
    say: trials find little effect; a large wearable study links this window with later, shorter sleep; watch sleep_min, no change needed by default
    product_constant: true
    basis: sleep-recovery/evening-training-sleep-effect-010
    basis_grade: C
  - id: evening-ends-4h-plus
    when: session ends 4 h or more before the usual bedtime
    level: none
    say: no sleep note
    product_constant: true
    basis: sleep-recovery/evening-training-sleep-effect-010
    basis_grade: B
  - id: wake-buffer
    when: planned first heavy set is less than 30 min after the usual wake-up
    level: note
    say: allow at least 30 min awake and a longer warm-up before the first heavy set
    product_constant: true
    basis: sleep-recovery/early-morning-session-071
    basis_grade: D
  - id: morning-vs-evening-numbers
    when: comparing top sets or e1RM across sessions at different times of day
    level: note
    say: compare morning with morning; a lower morning number is the clock, not a regression
    product_constant: false
    basis: sleep-recovery/early-morning-session-071
    basis_grade: B
brief_guards:
  - guard: never cancel or shorten a session on sleep_min alone; the levels above hedge, they do not block
    basis_grade: D
  - guard: one sleep line per brief at most; pick the highest level that fires (flag > hedge > note)
    basis_grade: D
  - guard: sleep_min is a wearable estimate; speak it in hours rounded to 0.5 and never as a diagnosis
    basis_grade: C
  - guard: no composite readiness or recovery score is computed or spoken from these rules
    basis_grade: C
  - guard: missing sleep_min means no sleep line, not a question every morning
    basis_grade: D
  - guard: persistent short sleep with daytime sleepiness, snoring or gasping, or insomnia complaints routes out of the brief -- insomnia to sleep-recovery/cbti-strong-sleep-hygiene-weak-007, breathing signs to a clinician -- not into training advice
    basis_grade: B
refraction_notes:
  - note: >
      THE DIRECTIONS ARE GRADED, THE THRESHOLDS ARE NOT. Keeping a morning
      session after a short night, napping to repay it, timing caffeine against
      bedtime and finishing hard work well before bed each rest on a graded row.
      The 360-minute line (mirroring 004's 6 h exposure definition), the 3-of-7
      pattern, the 1 h and 4 h windows and the 30 min wake buffer are the
      plan's rules. Speak them as the plan's rules.
    grade: D
  - note: >
      HEDGE, NEVER BLOCK. Nothing in the sleep evidence supports cancelling a
      session because of one short night; the best-supported advice is to
      train earlier, and a 05:00 session already is early. The brief lowers
      ambition (no max test) rather than removing training.
    grade: B
  - note: >
      THE 1-TO-4-HOUR WINDOW IS WHERE THE SOURCES DISAGREE. Trials put the risk
      at hard work ending within about an hour of bed; a large observational
      wearable study sees associations out to four hours. The rule therefore
      notes and watches in that window instead of advising a change.
    grade: C
  - note: >
      ONE MEASUREMENT, ONE SENTENCE. sleep_min comes from a wrist device, so
      it is good for patterns across nights and weak for one night's exact
      minutes. That is why the strongest level (flag) is reserved for a
      repeated pattern, not a single night.
    grade: C
claim: >
  A health brief can use five graded directions about sleep and training, each
  with product thresholds: after a short night (under 6 hours) keep a morning
  session, skip max attempts, and repay with a 30 to under 60 minute early-afternoon
  nap ending more than an hour before training and an earlier bedtime; if
  the session is later in the day, move it earlier if possible rather than
  cancelling; flag the schedule, not the night, when short nights repeat (3 of
  the last 7); time the last caffeine against bedtime by dose (070), which
  leaves pre-workout caffeine before a 05:00-06:00 session free and puts the
  same dose before an evening session in question; and finish hard sessions
  more than an hour before bed, with a watch-only note for 1 to 4 hours
  because trials and a large wearable cohort disagree there. The brief hedges
  and never cancels, speaks one sleep line at most, never computes a
  readiness score, and routes persistent insomnia or sleep-disorder signs out
  of training advice. The directions are evidence-backed; every threshold is a
  product constant.
reasoning: >
  Each rule is lifted from a graded row and keeps that row's grade as
  basis_grade, so the module can choose how strongly to phrase it. 004 gives
  the short-night and early-alarm rules from Craven 2022's pre-specified
  subgroups; 009 gives the nap parameters (Mesas 2023: 30 to under 60
  minutes, more than an hour from waking to the test) and the force null; no
  shorter nap is offered because the trials do not support one; 010 now carries both the trial window and the 2025 wearable
  association, which is why 1 to 4 hours is a note and not a hedge; 070 and
  071 supply the caffeine and morning rules. The guards come from the
  warehouse's own measurement items: 011 (subjective and objective markers
  diverge; no composite readiness score validated against performance) and
  003 (wearable sleep estimates are approximate). The axes are soft because
  nothing here withholds information. Not contested: this row adds no
  primary claim of its own.
---

# sleep-recovery/brief-sleep-training-rules-072 -- 브리프용 수면·운동 규칙 묶음

**한 줄 그림:** 브리프는 잠 때문에 운동을 취소하지 않는다. 기대치를 낮추고, 낮잠·취침 시각·카페인
시각으로 메우며, 반복되는 패턴만 강하게 짚는다.

## The rule set

| Rule | When | Level | Basis |
|---|---|---|---|
| short-night-morning | under 6 h, session before 10:00 | note | 004 |
| short-night-later | under 6 h, session 10:00 or later | hedge | 004 |
| early-alarm-pattern | woke 60+ min early and under 6 h | note | 004 |
| repeated-short-nights | under 6 h on 3 of last 7 | flag | 071 |
| nap-repay | under 6 h, nap possible | note | 009 |
| caffeine-late | last caffeine inside 070's hours | hedge | 070 |
| caffeine-morning-session | 05:00-06:00 start | none | 071 |
| evening-hard-close-to-bed | hard work ends within 1 h of bed | hedge | 010 |
| evening-hard-1-to-4h | ends 1-4 h before bed | note | 010 |
| wake-buffer | first heavy set under 30 min after waking | note | 071 |
| morning-vs-evening-numbers | cross-time comparison | note | 071 |

Guards: hedge, never block; one sleep line per brief; no readiness score; no
sleep_min, no line; sleep-disorder signs route to the clinical items.

## 한국어 요약 (답변용)

- 6시간 못 잔 다음 날 아침 운동은 그대로 한다. 최대 중량 시도만 미루고, 이른 오후 30분~1시간 미만 낮잠(깬 뒤
  1시간 넘게 지나서 운동)과 일찍 자는 것으로 갚는다.
- 운동이 오후·저녁이면 가능할 때 일찍 당긴다. 잠 하나 때문에 취소하지는 않는다.
- 평소보다 일찍 깨서 짧게 잔 날이 늦게 자서 짧게 잔 날보다 손해가 크다. 다음 날 기상 시각을 지킨다.
- 최근 7일 중 3일 이상 6시간 미만이면 하루 문제가 아니라 일정 문제로 짚는다(취침을 기상 7.5시간
  전으로 당기거나 운동 시간을 옮긴다).
- 낮잠은 피로감을 줄이지만 근력을 올리지는 않는다.
- 마지막 카페인은 잠자리 시각과 양으로 판단한다(070). 새벽 운동 전 카페인은 괜찮고, 같은 양을 저녁
  운동 전에 먹으면 밤잠에 걸린다.
- 힘든 운동이 잠자기 1시간 안에 끝나면 늦게 잠들 수 있다고 알린다. 1~4시간 전이면 연구 결과가 엇갈리니
  수면 기록만 지켜본다. 4시간 이상이면 말하지 않는다.
- 숫자 기준(6시간, 7일 중 3일, 1·4시간, 30분)은 제품이 정한 규칙이다. 방향은 연구로 뒷받침된다.
- 수면 점수·회복 점수는 만들지 않는다. 잠 얘기는 브리프에 한 줄까지만. 수면 기록이 없으면 말하지 않는다.
- 불면이 오래가거나 낮 졸림·코골이·숨 멎음이 있으면 운동 조언이 아니라 수면 진료 쪽으로 안내한다.
