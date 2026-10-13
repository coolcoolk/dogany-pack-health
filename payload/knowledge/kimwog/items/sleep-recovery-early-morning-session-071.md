---
# Sleep-training sprint 2026-10-06 (dispatch kw-sleep-training-2). The owner
# trains at 05:00-06:00; this row answers what that time slot costs and what
# offsets it. Every source was read at PubMed (abstract) or PMC (full text)
# on 2026-10-06. The honest headline is a scope limit: NO located trial tests
# strength at 05:00-06:00. Morning arms in this literature run about
# 07:00-10:00, so every statement about a 05:00 session is a transfer and is
# graded as one.
#
# morning_session_rules is structured data for a health / brief module. Each
# rule names its input (planned session start, sleep_min from hk-ingest,
# stated chronotype), its action, and whether its number is a product
# constant. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/early-morning-session-071
domain: sleep-recovery
grade: B (strength is lower in the morning; morning training still builds strength and size like evening training; caffeine offsets the morning dip in trained men; a short night hurts AM tasks little); C (early sessions shorten sleep; late chronotypes are worse in the morning; sleep inertia); D (every transfer to a 05:00-06:00 start and every product time constant)
lane: "@clinical"
locale: universal
as_of: 2012-2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/30704301/"  # Grgic J, Lazinica B, Garofolini A, Schoenfeld BJ, Saner NJ, Mikulic P. 2019, Chronobiol Int 36(4):449-460, doi 10.1080/07420528.2019.1567524 -- 11 studies, morning vs evening resistance training, volume and frequency equated
  - "https://pubmed.ncbi.nlm.nih.gov/22496767/"  # Mora-Rodriguez R, Garcia Pallares J, Lopez-Samanes A, Ortega JF, Fernandez-Elias VE. 2012, PLoS One 7(4):e33807, doi 10.1371/journal.pone.0033807 -- 12 highly resistance-trained men, 3 mg/kg caffeine at 10:00 vs placebo at 10:00 and 18:00, double-blind crossover
  - "https://pubmed.ncbi.nlm.nih.gov/24816164/"  # Mora-Rodriguez R, Pallares JG, Lopez-Gullon JM, Lopez-Samanes A, Fernandez-Elias VE, Ortega JF. 2015, J Sci Med Sport 18(3):338-342, doi 10.1016/j.jsams.2014.04.010 -- 13 resistance-trained men, 6 mg/kg 60 min pre, AM and PM, double-blind crossover
  - "https://pubmed.ncbi.nlm.nih.gov/32528038/"  # Mirizio GG, Nunes RSM, Vargas DA, Foster C, Vieira E. 2020, Sci Rep 10(1):9485, doi 10.1038/s41598-020-66342-w -- narrative review, short maximal efforts peak 16:00-20:00; warm-up and time-specific training blunt the dip
  - "https://pubmed.ncbi.nlm.nih.gov/24444223/"  # Sargent C, Halson S, Roach GD. 2014, Eur J Sport Sci 14 Suppl 1:S310-S315, doi 10.1080/17461391.2012.696711 -- 7 elite swimmers, 06:00 sessions, actigraphy + diaries, 14 days
  - "https://pubmed.ncbi.nlm.nih.gov/30357501/"  # Facer-Childs ER, Boiling S, Balanos GM. 2018, Sports Med Open 4(1):47, doi 10.1186/s40798-018-0162-z -- 56 healthy adults, early vs late chronotypes, tested 14:00, 20:00 and 08:00
  - "https://pubmed.ncbi.nlm.nih.gov/31692489/"  # Hilditch CJ, McHill AW. 2019, Nat Sci Sleep 11:155-165, doi 10.2147/NSS.S188911, PMCID PMC6710480 -- sleep inertia review (cognitive endpoints only)
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # AM tasks largely unaffected by a short night; deficit grows with hours awake
  - "sleep-recovery/caffeine-bedtime-cutoff-070"  # why morning caffeine is outside the sleep window
  - "sleep-recovery/hour-target-is-a-threshold-consensus-013"  # the 7-hour threshold the bedtime anchor uses
  - "sleep-recovery/nap-force-null-shuttle-signal-009"  # the nap after a short night
  - "framework:GRADE -- the morning-dip, adaptation and caffeine findings come from controlled trials (Grgic pools 11; the caffeine trials are double-blind crossovers) but each trial is small, all-male and tested around 10:00, not 05:00: B for the finding, D for the 05:00 transfer. Sargent is 7 swimmers (C); Facer-Childs measured grip at 08:00 (C); the sleep inertia review covers cognition, not force (C for the window, D for training)."
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
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
morning_session_rules:
  - id: bedtime-anchor
    input: planned session start, usual wake-up before it
    action: target lights-out about 7.5 h before the wake-up time (7 h sleep + about 30 min to fall asleep and settle); say it as the plan's anchor; check it against sleep_min, since time in bed is not sleep
    product_constant: true
    basis: sleep-recovery/hour-target-is-a-threshold-consensus-013; Sargent 2014
    basis_grade: D
  - id: short-night-keep-session
    input: sleep_min below 360 the night before a morning session
    action: keep the session; do not move it later in the day; a nap later is the repayment (009); no maximal-effort test today
    product_constant: false
    basis: Craven 2022 via sleep-recovery/sleep-loss-performance-decrement-004
    basis_grade: B
  - id: chronic-short-sleep
    input: sleep_min below 360 on 3 or more of the last 7 nights before training days
    action: flag the schedule, not the session -- the early slot is cutting sleep; suggest an earlier bedtime or moving a session
    product_constant: true
    basis: Sargent 2014
    basis_grade: C
  - id: wake-to-first-heavy-set
    input: planned session start and usual wake-up
    action: allow at least 30 min awake before the first heavy set, and a longer, ramped warm-up than an evening session
    product_constant: true
    basis: Hilditch 2019 (cognitive recovery within about 30 min, fuller by 1 h); Mirizio 2020 (active warm-up blunts the morning dip)
    basis_grade: D
  - id: morning-caffeine-ok
    input: caffeine before a session starting 05:00-06:00
    action: about 3 mg/kg about 60 min before (or with the wake-up if the gap is shorter) is a legitimate offset for the morning dip and is outside the sleep cutoff; never above 6 mg/kg
    product_constant: false
    basis: Mora-Rodriguez 2012, 2015; sleep-recovery/caffeine-bedtime-cutoff-070
    basis_grade: B
  - id: morning-numbers-are-morning-numbers
    input: e1RM or top-set comparison across sessions at different times of day
    action: compare morning sessions with morning sessions; a lower morning top set is not a regression
    product_constant: false
    basis: Grgic 2019; Mora-Rodriguez 2012
    basis_grade: B
  - id: late-chronotype
    input: stated chronotype late
    action: expect a larger morning dip; hedge morning targets; do not pathologise it
    product_constant: false
    basis: Facer-Childs 2018
    basis_grade: C
refraction_notes:
  - note: >
      Strength is lower in the morning, and morning training fixes most of
      that for morning testing. Across 11 studies, baseline strength was
      greater in the evening; training in the morning raised morning strength
      to evening levels; and strength and muscle-size gains were similar
      whichever time people trained. In one trial of trained men the evening
      advantage on bar velocity and power was 3.0-7.5 percent (10:00 vs
      18:00). For a 05:00 trainer this means two things: the schedule does
      not cost long-term results, and morning numbers should be compared with
      morning numbers.
    grade: B
  - note: >
      Caffeine offsets the morning dip in trained men. 3 mg/kg at 10:00 raised
      strength and power 4.6-5.7 percent above morning placebo, to the
      afternoon level; 6 mg/kg 60 minutes before raised squat velocity 5.4-8.1
      percent in the morning, gave no velocity gain in the afternoon, and side
      effects were twice as common in the afternoon (26 vs 13 percent). Both
      trials are 12-13 men tested around 10:00. Whether the size of the offset
      holds at 05:00, closer to the body-temperature low, is untested.
    grade: B
  - note: >
      A short night before a morning session is cheaper than it looks. In the
      sleep-loss meta-analysis, morning tasks were largely unaffected while
      afternoon tasks were consistently impaired, and the loss grew with hours
      awake (004). A 05:00 session after a short night is near the low end of
      hours awake. The cost of the short night shows up later in the day and
      across the week, which is why the nap and the next bedtime are the
      repair, not cancelling the session.
    grade: B
  - note: >
      Early sessions take sleep. Seven elite swimmers training at 06:00 went
      to bed at about 22:05, got up at about 05:48 and slept 5.4 hours before
      training days, against 7.1 hours before rest days. That is about 7.7
      hours in bed yielding 5.4 hours of measured sleep: an earlier bedtime
      alone did not deliver the sleep. Seven athletes in one squad is thin,
      but two things generalise: a 05:00 start means a 04:15-04:30 wake-up,
      so 7 hours of sleep needs lights-out near 21:00; and time in bed is not
      sleep, so the anchor must be checked against measured sleep_min, not
      assumed to work.
    grade: C
  - note: >
      Waking straight into heavy work. Sleep inertia -- the grogginess after
      waking -- impairs cognitive performance, mostly recovering within about
      30 minutes and more fully by an hour; it is worse after sleep loss and
      when waking near the circadian low, which is where a 04:30 alarm falls
      for most people. The review measures attention and reaction, not force,
      so the 30-minute buffer is a product rule for technique-heavy work, not
      a measured strength threshold.
    grade: C
  - note: >
      Chronotype. Late chronotypes (by questionnaire, phase markers and
      actigraphy) were significantly worse than early chronotypes on every
      measure in the morning, including grip strength, in a study of 56
      people tested at 08:00. Expect a late type at 05:00 to show the largest
      dip; that is a reason to hedge the day's targets, not a diagnosis.
    grade: C
claim: >
  Training at 05:00-06:00 costs some same-day strength, not long-term
  progress, and the cost can be offset. Strength is greater in the evening at
  baseline, but across 11 studies morning training raised morning strength to
  evening levels and produced similar strength and muscle-size gains to evening
  training. In trained men caffeine taken before a morning session (3-6 mg/kg,
  about 60 minutes before) raised strength and bar velocity to afternoon levels,
  and morning caffeine sits outside every sleep cutoff (070). After a short
  night, a morning session loses less than an afternoon one, because the
  sleep-loss decrement grows with hours awake (004). The real cost of the slot
  is sleep: seven elite swimmers with 06:00 sessions slept 5.4 hours before
  training days despite about 7.7 hours in bed. Operative rules for
  a brief: anchor lights-out about 7.5 hours before the wake-up; keep the
  session after a short night and repay with a nap and an earlier bedtime; flag
  the schedule when short nights repeat; allow at least 30 minutes awake and a
  longer warm-up before the first heavy set; compare morning numbers with
  morning numbers; expect a larger dip in late chronotypes. No trial located
  tests 05:00-06:00 directly, so these are transfers from 07:00-10:00 data.
reasoning: >
  The finding a 05:00 trainer needs most is the adaptation result: Grgic et
  al. 2019 pooled 11 time-of-day-specific training studies with volume and
  frequency equated and found similar strength and hypertrophy gains for
  morning and evening training, with morning trainees closing the morning
  strength gap. That removes the fear that the slot itself limits progress.
  The two Mora-Rodriguez crossovers are small, all-male, double-blind and
  consistent with each other, which is enough for the direction (caffeine
  offsets the morning dip) at B and not for the size at 05:00. Craven 2022,
  already in this warehouse as item 004, supplies the counter-intuitive short
  night rule from its own pre-specified AM/PM subgroup. Sargent 2014 is the
  only located measurement of what early sessions do to sleep in athletes, and
  is carried at C for its size. The sleep inertia review and the chronotype
  study measure cognition and grip, not training loads, so they shape hedges
  and buffers, not numbers. Every time constant in morning_session_rules (7.5
  h anchor, 30 min buffer, 360-minute short-night line, 3-of-7 pattern) is a
  product constant and labelled so; the 360 minutes mirrors 004's exposure
  definition (6 h or less). Not contested: no located source argues that
  morning training limits long-term adaptation.
---

# sleep-recovery/early-morning-session-071 -- 새벽 5~6시 운동: 무엇을 잃고 무엇으로 메우나

**한 줄 그림:** 새벽 운동은 그날 힘이 조금 덜 나올 뿐 장기 성과를 깎지 않는다. 진짜 비용은 잠이고,
잠은 취침 시각으로 지킨다.

## Rules a brief can use

| Rule | Input | Action | Constant? |
|---|---|---|---|
| bedtime-anchor | session start, wake-up | lights-out about 7.5 h before wake-up | product |
| short-night-keep-session | sleep under 6 h before a morning session | keep it, no max test, nap + earlier bed later | evidence |
| chronic-short-sleep | under 6 h on 3 of 7 training nights | flag the schedule | product |
| wake-to-first-heavy-set | wake-up, start | 30+ min awake, longer warm-up | product |
| morning-caffeine-ok | caffeine before 05:00-06:00 | about 3 mg/kg, about 60 min before; max 6 mg/kg | evidence |
| morning-numbers | cross-session comparison | morning vs morning only | evidence |
| late-chronotype | stated late type | hedge morning targets | evidence |

Example: wake 04:30 for a 05:00 start -> lights-out about 21:00.

## 한국어 요약 (답변용)

- 아침에는 저녁보다 힘이 덜 나온다(10시와 18시 비교에서 3~7.5%). 하지만 아침에 꾸준히 운동하면
  아침 힘이 저녁 수준까지 올라오고, 근력·근육 증가는 운동 시간대와 상관없이 비슷했다(11편 종합).
- 그래서 기록 비교는 아침 기록끼리 한다. 아침 탑세트가 저녁보다 낮은 건 퇴보가 아니다.
- 운동 약 60분 전 카페인(체중 1kg당 약 3mg)은 훈련된 남성에서 아침 저하를 오후 수준까지 메웠다.
  새벽 운동 전 카페인은 밤잠 기준(070) 밖이다. 1kg당 6mg을 넘기지 않는다.
- 잠을 적게 잔 날도 새벽 운동은 그대로 한다. 짧은 잠의 손해는 깨어 있는 시간이 길어질수록 커지므로
  아침이 가장 덜하다. 다만 그날은 최대 기록 측정은 하지 않고, 낮잠과 이른 취침으로 갚는다.
- 새벽 운동의 진짜 비용은 수면이다. 6시 훈련 수영 선수들은 훈련 전날 약 7.7시간 누워 있었지만
  실제 잠은 5.4시간이었다. 4시 30분에 일어나려면 9시 전후에 불을 꺼야 7시간을 잔다(제품 기준: 기상
  7.5시간 전). 누워 있는 시간과 잔 시간은 다르므로, 실제 수면 기록으로 확인한다.
- 일어나서 바로 무거운 세트에 들어가지 않는다. 깬 뒤 최소 30분, 워밍업은 저녁보다 길게(제품 기준).
- 저녁형인 사람은 아침 저하가 더 크다. 목표를 조금 낮춰 잡되 문제로 다루지 않는다.
- 새벽 5~6시를 직접 시험한 연구는 없다. 대부분 아침 7~10시 자료를 옮겨 쓴 것이다.
