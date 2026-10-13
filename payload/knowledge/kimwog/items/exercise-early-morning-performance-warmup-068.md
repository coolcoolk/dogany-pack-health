---
# Early-morning training sprint 2026-10-07 (dispatch task
# kw-ex-early-morning-training). The owner trains in a 05:00-06:00 window and
# the morning brief goes out at 04:30 (program-plan BRIEF_LEAD_MIN). This item
# answers the performance half: how much weaker is a dawn session, what part of
# it a warm-up buys back, and whether the training TIME changes the long-run
# result. Companion to 069 (caffeine / food at dawn) and 073 (the
# engine-readable brief rules). Rubric: exercise.rubric.md @performance-lit.
#
# HONEST SCOPE NOTE. No source below tested 05:00. The "morning" arms sit at
# 06:00-10:00 (Taylor 08:00, Facer-Childs 08:00, Mora-Rodriguez 10:00; Knaier
# pools whatever times the included studies used). A 05:00 session is the
# early edge of that range, so the direction transfers and the magnitudes are
# a floor, not a fit.
# Renumbered at the v37 merge (provisional 070 -> 068). The sleep side of the
# same 05:00 session is sleep-recovery/early-morning-session-071.
id: exercise/early-morning-performance-warmup-068
domain: exercise
grade: B (maximal power, jump and grip are lower in the morning than late afternoon); B (morning vs evening training gives similar strength and hypertrophy gains); C (a longer, temperature-raising warm-up closes most of the morning power gap); C (chronotype / time-since-waking sets the size of the gap)
lane: "@performance-lit"
locale: universal
as_of: 2011-2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/34431827/"  # Knaier R, Qian J, Roth R, et al. 2022, Med Sci Sports Exerc 54(1):169-180, doi 10.1249/MSS.0000000000002773 -- 63 studies (tests at >= 3 times of day), 29 meta-analysed, 841 participants (78% male); ES favouring evening: Wingate 0.73, jump 0.79, grip 0.39, endurance 0.23; risk of bias moderately high
  - "https://doi.org/10.1080/07420528.2019.1567524"  # Grgic J, Lazinica B, Garofolini A, Schoenfeld BJ, Saner NJ, Mikulic P. 2019, Chronobiol Int 36(4):449-460 -- 11 training studies: morning- and evening-trained groups gain strength and muscle size similarly; morning training lifts MORNING-tested strength toward the evening level
  - "https://doi.org/10.1055/s-0030-1268437"  # Taylor K, Cronin JB, Gill N, Chapman DW, Sheppard JM. 2011, Int J Sports Med 32(3):185-189 -- n=8 recreationally trained men; afternoon jump/power 2-6% above morning after a standard warm-up; adding 20 min cycling (+0.3 C body temp) at 08:00 removed the substantial difference
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC6200828/"  # Facer-Childs ER, Boiling S, Balanos GM. 2018, Sports Med Open 4:47, doi 10.1186/s40798-018-0162-z, PMID 30357501 -- n=56 (25 early, 31 late chronotype; 33 F); at 08:00 early types 7.4% stronger on grip than late types; peak ~6.7 h after waking (early) vs ~12.6 h (late)
  - "exercise/dynamic-warmup-same-day-performance-022"  # the general warm-up evidence this item narrows to the morning case
  - "exercise/warmup-load-rampup-progression-018"  # the LOAD ramp, a separate lever from the general warm-up
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # the sleep half: early alarm vs late bedtime, AM vs PM
  - "framework:GRADE -- the morning deficit is a meta-analysed direction with moderately high risk of bias and a young male sample (B on direction, magnitudes not transported). The adaptation finding is a meta-analysis of 11 small training studies (B). The warm-up offset rests on one n=8 crossover plus mechanism (C). The chronotype modifier rests on one n=56 study plus the Knaier discussion (C)."
applicability:
  axes:
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      SPEAK THE GAP AS A DIRECTION, NOT A PERCENT. Knaier 2022 gives moderate
      to large standardised effects for power and jump (ES about 0.7-0.8) and
      small ones for grip and endurance, but these are between-time effect
      sizes in mostly young men across heterogeneous protocols. The single
      percent figure in this item (2-6% for jump/power, Taylor 2011) comes from
      n=8 at 08:00. A 05:00 lifter may sit at or beyond that; nothing measured
      it. Say "a bit weaker at dawn, most of it warm-up-recoverable", never
      "you are X% weaker".
    grade: C
  - note: >
      THE GAP IS MOSTLY TEMPERATURE, SO THE WARM-UP IS THE LEVER. In Taylor
      2011 a 20-minute general warm-up (+0.3 C whole-body temperature) at
      08:00 brought jump and power to the afternoon level. Mechanism and one
      small crossover agree, so a dawn session should get a LONGER general
      warm-up than an afternoon one before the load ramp (018). The exact
      extra minutes are not established: 20 min was the tested dose, not a
      dose-response finding.
    grade: C
  - note: >
      TIME OF TRAINING DOES NOT DECIDE THE LONG-RUN RESULT. Grgic 2019:
      morning-trained and evening-trained groups gained strength and muscle
      size similarly, and morning training raised morning-tested strength
      toward the evening level (a time-of-day specificity). So the dawn slot
      costs a little on the day, not on the programme; consistency of the slot
      matters more than its hour. Do not tell a dawn lifter to move to the
      evening for gains.
    grade: B
  - note: >
      CHRONOTYPE SETS THE SIZE. Facer-Childs 2018: at 08:00 late chronotypes
      were 7.4% weaker on grip than early chronotypes, and peak strength came
      ~6.7 h after waking for early types versus ~12.6 h for late types. A
      05:00 session is far from either peak, but it is much further for a late
      type forced up early. Chronotype unknown -> hedge to the intermediate
      baseline; do not ask just for this.
    grade: C
  - note: >
      POPULATION. Knaier: 78% male, mostly young adults, moderately high risk
      of bias. Facer-Childs is the only source here with a majority-female
      sample. Nothing here resolves age or sex effects on the morning gap.
    grade: C
claim: >
  Maximal power, jump height and grip strength are reliably lower in the
  morning than in the late afternoon / early evening (peak window roughly
  13:00-20:00; Knaier 2022 meta-analysis, effect sizes about 0.7-0.8 for
  Wingate power and jump, about 0.4 for grip, about 0.2 for endurance). A
  05:00-06:00 session sits at the low end of that curve. Two things limit how
  much this matters. First, most of the short-term gap tracks body
  temperature, and a longer general warm-up that raises it (20 min of easy
  cycling in the one controlled test) brought morning jump and power level
  with the afternoon. Second, over a training block the hour does not decide
  the result: morning- and evening-trained groups gain strength and muscle
  similarly, and morning training raises morning-tested strength (time-of-day
  specificity). The size of the dawn gap depends on chronotype and time since
  waking: late types are weaker early and peak much later after waking. No
  source tested 05:00 itself; the direction transfers, the magnitudes do not.
reasoning: >
  Knaier et al. 2022 (Med Sci Sports Exerc 54(1):169-180) is the anchor: a
  PROSPERO-registered review of 63 studies with tests at three or more times
  of day, 29 meta-analysed, all four outcome classes favouring the evening and
  strong evidence that anaerobic power and jump peak in the afternoon. Its own
  limits (moderately high risk of bias, 78% male, young adults) keep the
  magnitudes from being spoken as personal expectations, but the direction is
  consistent. Grgic et al. 2019 (Chronobiol Int 36(4):449-460) answers the
  question that matters more for a habitual dawn lifter: across 11 training
  studies, morning and evening training produce similar strength and
  hypertrophy, and the morning deficit itself shrinks in morning-trained
  people when tested in the morning. Taylor et al. 2011 (Int J Sports Med
  32(3):185-189) supplies the lever: with a standard dynamic warm-up the
  afternoon was 2-6% better, but an extra 20-minute bike warm-up at 08:00 that
  raised whole-body temperature by about 0.3 C removed the substantial
  difference. That is n=8 men, so it is graded as supportive rather than
  established, and it tested jump/power, not multi-set heavy lifting.
  Facer-Childs et al. 2018 (Sports Med Open 4:47) shows that the clock hour is a
  proxy for time since waking and circadian phase: early types out-gripped late
  types by 7.4% at 08:00, and peak performance followed waking by ~6.7 h versus
  ~12.6 h. Not contested: no source located disputes the morning deficit or
  the similar-adaptation finding.
---

# exercise/early-morning-performance-warmup-068 -- 새벽 운동: 시간대에 따른 수행력과 워밍업

**One line:** at 05:00 you are a little weaker than you would be at 17:00,
most of that is a cold body that a longer warm-up fixes, and over months the
hour makes no difference to gains.

What the research shows, plainly:

- Power, jump and grip are lower in the morning than in the late afternoon.
  That holds across a 63-study review. The size varies a lot by study, and
  nobody has measured 05:00 specifically; the "morning" arms are mostly 06:00
  to 10:00.
- The gap looks mostly like body temperature. In one small crossover, 20
  minutes of easy cycling before the usual warm-up at 08:00 brought jump and
  power up to the afternoon level.
- Across training studies, people who train in the morning gain strength and
  size about as much as people who train in the evening. Their morning
  strength also catches up, because the body adapts to the hour it trains at.
- Chronotype matters. Natural late risers are weaker early in the day and peak
  much later after waking than early risers.

Practical read for a 05:00 lifter: make the general warm-up longer than you
would in the afternoon, then do the usual load ramp. Keep the slot consistent.
Do not read a slightly heavier-feeling first set at dawn as lost fitness.

## 한국어 요약 (답변용)

- 근력·순발력·점프·악력은 아침이 늦은 오후(대략 13시~20시)보다 낮다. 63편을 모은 메타분석에서
  일관된 방향이다. 다만 새벽 5시를 직접 잰 연구는 없고, 연구 속 "아침"은 대개 6시~10시다. 그래서
  "몇 % 약하다"고 말하지 않고 "새벽엔 조금 약하다"고만 말한다.
- 차이의 상당 부분은 체온이다. 8시에 실내자전거 20분을 더 해서 체온을 올렸더니 점프·파워가 오후
  수준으로 올라왔다(8명 연구). 새벽 운동은 오후보다 일반 워밍업을 길게 하고, 그다음 무게를 단계적으로
  올린다. 몇 분이 최적인지는 밝혀지지 않았다.
- 몇 달 단위로 보면 아침에 운동하든 저녁에 운동하든 근력·근육 증가는 비슷하다. 아침에 꾸준히 운동하면
  아침 근력 자체가 따라 올라온다. 근성장을 위해 저녁으로 옮길 이유는 없고, 시간대를 일정하게 지키는
  게 더 중요하다.
- 아침형인지 저녁형인지에 따라 차이 크기가 달라진다. 저녁형은 아침에 더 약하고 정점도 기상 후 훨씬
  늦게 온다. 모르면 중간형으로 보고, 이것 때문에 따로 묻지 않는다.
- 연구 참가자는 대부분 젊은 남성이다. 나이·성별에 따른 차이는 아직 모른다.
