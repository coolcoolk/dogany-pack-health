---
# Early-morning training sprint 2026-10-07 (dispatch task
# kw-ex-early-morning-training). The fuel half of a 05:00-06:00 session:
# caffeine (does it help at dawn, when to take it, what it costs that night)
# and food (fasted vs fed when the session starts minutes after waking).
# Companion to 068 (performance / warm-up) and 073 (brief rules). Also the
# first caffeine row in the warehouse -- GAPS.md (exercise) has listed caffeine
# as a missing AIS Group A ergogenic since batch1, and GAPS.md
# (sleep-recovery) lists "caffeine timing versus sleep" as untouched. This item
# covers both ONLY as far as a dawn lifter needs; it is not the general
# caffeine item. Rubric: exercise.rubric.md @clinical-physio.
# Renumbered at the v37 merge (provisional 071 -> 069). The same release adds
# sleep-recovery/caffeine-bedtime-cutoff-070, which owns the caffeine-vs-sleep
# cutoff; the cutoff figures quoted here are the same Gardiner 2023 estimates
# and follow that row if it is re-graded.
#
# HONEST SCOPE NOTE. As in 068, no source tested 05:00. The caffeine-at-dawn
# trial ran at 10:00; the breakfast trial fed 2 h before the session, which a
# 05:00 lifter can only copy by waking at 03:00.
id: exercise/early-morning-caffeine-food-069
domain: exercise
grade: B (caffeine at 3-6 mg/kg is ergogenic for strength, power and endurance); C (morning caffeine offsets most of the morning neuromuscular deficit); B (caffeine shortens and lightens that night's sleep); C (the 8.8 h / 13.2 h bedtime cutoffs); B (pre-exercise food helps prolonged aerobic work, not short sessions); C (omitting a habitual breakfast cuts reps to failure); D (the small-snack compromise at dawn)
lane: "@clinical-physio"
locale: universal
as_of: 2012-2023
contested: no
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC7777221/"  # Guest NS, VanDusseldorp TA, Nelson MT, et al. 2021, J Int Soc Sports Nutr 18(1):1, doi 10.1186/s12970-020-00383-4, PMID 33388079 -- ISSN position stand: 3-6 mg/kg consistently ergogenic, minimum effective dose may be ~2 mg/kg, 60 min pre-exercise the most common timing (gum faster), 9 mg/kg high side-effect incidence, large inter-individual variation; caffeine lengthens sleep onset and reduces deep sleep and sleep efficiency
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC3319538/"  # Mora-Rodriguez R, Garcia Pallares J, Lopez-Samanes A, Ortega JF, Fernandez-Elias VE. 2012, PLoS One 7(4):e33807, doi 10.1371/journal.pone.0033807 -- n=12 highly resistance-trained men, double-blind crossover: 18:00 placebo 3.0-7.5% above 10:00 placebo on squat/bench velocity; 3 mg/kg caffeine at 10:00 raised morning values above morning placebo, to about afternoon level (except bench at the 1 m/s load)
  - "https://doi.org/10.1016/j.smrv.2023.101764"  # Gardiner C, Weakley J, Burke LM, Roach GD, Sargent C, et al. 2023, Sleep Med Rev 69:101764, PMID 36870101 -- 24 studies: total sleep -45 min, efficiency -7%, onset latency +9 min, WASO +12 min, deep sleep down; to avoid losing total sleep, coffee (107 mg) >= 8.8 h and a pre-workout serve (217.5 mg) >= 13.2 h before bedtime
  - "https://www.efsa.europa.eu/en/efsajournal/pub/4102"  # EFSA NDA Panel 2015, EFSA Journal 13(5):4102 -- single doses up to 200 mg raise no safety concern, including < 2 h before intense exercise under normal conditions; habitual up to 400 mg/day (non-pregnant adults); up to 200 mg/day in pregnancy
  - "https://www.ncbi.nlm.nih.gov/pubmed/29315892"  # Aird TP, Davies RW, Carson BP. 2018, Scand J Med Sci Sports 28(5):1476-1493 -- 46 studies: pre-exercise feeding improved PROLONGED aerobic performance (p = 0.012), not shorter aerobic (p = 0.687); resistance exercise not meta-analysed
  - "https://doi.org/10.1519/JSC.0000000000003054"  # Bin Naharudin MN, Yusof A, Shaw H, Stockton M, Clayton DJ, James LJ. 2019, J Strength Cond Res -- n=16 resistance-trained HABITUAL breakfast-eating men; 1.5 g/kg carbohydrate breakfast vs water 2 h before 4 sets to failure at 90% 10RM: squat 68 vs 58 reps, bench 40 vs 38 reps; not blinded (water vs a meal)
  - "https://pubmed.ncbi.nlm.nih.gov/26920240/"  # Thomas DT, Erdman KA, Burke LM. 2016, J Acad Nutr Diet 116(3):501-528 (co-published Med Sci Sports Exerc 48(3):543-568) -- AND/DC/ACSM joint position: 1-4 g/kg carbohydrate 1-4 h before exercise lasting > 60 min; nothing specific for short dawn strength sessions
  - "exercise/early-morning-performance-warmup-068"  # the morning deficit caffeine is offsetting
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # why waking at 03:00 to eat is the wrong trade
  - "sleep-recovery/evening-training-sleep-effect-010"  # the timing-vs-sleep sibling (exercise, not caffeine)
  - "framework:GRADE -- caffeine's ergogenic direction is a position stand over many meta-analysed RCTs (B). The dawn-specific offset is one n=12 crossover at 10:00 (C). Sleep harm is a meta-analysis of 24 studies (B); the cutoff hours are model-derived from those studies (C). Fed vs fasted is a 46-study meta-analysis that did not pool resistance work (B for the aerobic split); the resistance breakfast trial is one unblinded n=16 study in habitual eaters (C). The dawn snack is practitioner compromise (D)."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: hedge
      rescale:
        per_unit_low: 3       # mg caffeine per kg body weight (ISSN 2021 ergogenic range)
        per_unit_high: 6
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
refraction_notes:
  - note: >
      THE DAWN DOSE COSTS ALMOST NOTHING AT NIGHT; THE AFTERNOON ONE DOES. A
      dose at about 04:00-04:30 sits roughly 17 h before a 21:30-22:00
      bedtime, beyond even the 13.2 h cutoff Gardiner 2023 derived for a
      217.5 mg pre-workout serve. The sleep risk for a dawn lifter is the
      SECOND coffee: because an early riser also goes to bed early, the
      cutoff moves forward -- bedtime minus 8.8 h for a 107 mg coffee (about
      13:00 for a 21:45 bedtime), minus 13.2 h for a ~220 mg serve. The hours
      are regression estimates from 24 mostly small studies; speak them as a
      rule of thumb, not a threshold.
    grade: C
  - note: >
      CAFFEINE BUYS BACK SOME OF THE MORNING GAP. Mora-Rodriguez 2012: 3 mg/kg
      at 10:00 brought squat and bench bar velocity in trained men up to about
      the 18:00 placebo level. One n=12 crossover, later than 05:00, so it
      supports "caffeine helps more in the morning" without a number.
    grade: C
  - note: >
      DOSE AND SAFETY. 3-6 mg/kg is the ISSN ergogenic range; ~2 mg/kg may
      already work. EFSA puts single doses up to 200 mg as no safety concern
      even within 2 h of intense exercise, and up to 400 mg/day habitual.
      For a heavier lifter 3 mg/kg is already above 200 mg, so the low end of
      the ISSN range is the default and the upper end is not routine advice.
      9 mg/kg carries a high side-effect rate. Pregnancy (200 mg/day cap) or a
      cardiovascular condition withholds the specific dose.
    grade: B
  - note: >
      TIMING AT DAWN. 60 min before is the commonest protocol, so coffee on
      waking for a 05:00 start is the straightforward version; a brief that
      arrives 30 min before the session is late for a first coffee but on time
      for gum or a fast-absorbed source (ISSN: gums need a shorter wait).
      Exact onset differences at dawn are not tested.
    grade: D
  - note: >
      FOOD: DURATION DECIDES. Aird 2018: eating before exercise helped
      PROLONGED aerobic work and made no detectable difference to shorter
      aerobic work. A typical 05:00 lifting session of about an hour is in the
      "short" band, so fasted training is a legitimate choice. The caveat is
      Naharudin 2019: habitual breakfast eaters who skipped a 1.5 g/kg
      carbohydrate breakfast did fewer reps to failure 2 h later (squat 58 vs
      68). One unblinded trial, sets to failure, habitual eaters only.
    grade: C
  - note: >
      DO NOT TRADE SLEEP FOR A MEAL. The 2-hour pre-session meal from the
      trial would mean a 03:00 alarm, which is the late-restriction pattern
      004 grades as the harmful kind of sleep loss. The defensible compromise
      is a small, easily digested carbohydrate snack 30-60 min before, or
      nothing, chosen by gut tolerance and habit, and a proper meal after.
      This compromise is practitioner reasoning; no trial tested it at dawn.
    grade: D
  - note: >
      LONG ENDURANCE AT DAWN IS THE EXCEPTION. For a session over about 60 min
      of continuous aerobic work, the joint position (1-4 g/kg carbohydrate,
      1-4 h before) and Aird's prolonged-aerobic result apply; at 05:00 the
      practical route is carbohydrate during the session, since the pre-meal
      window does not fit.
    grade: D
claim: >
  For a 05:00-06:00 strength session: caffeine at 3-6 mg/kg is a
  well-supported ergogenic aid, and in the morning it also offsets part of
  the morning neuromuscular deficit (one small trial). Taken around waking,
  the dawn dose is far enough from bedtime that it should not cost sleep; the
  sleep risk for an early riser is a second dose in the afternoon, which
  should come at least ~8.8 h (coffee) or ~13.2 h (pre-workout serve) before
  bedtime. Single doses up to 200 mg raise no safety concern even close to
  intense exercise; pregnancy and cardiovascular conditions withhold dose
  specifics. On food: pre-exercise eating improves prolonged aerobic work but
  not short sessions, so training fasted for an hour of lifting is
  legitimate; habitual breakfast eaters may lose some reps to failure when
  they skip it. Waking two hours early to eat is the wrong trade -- a small
  carbohydrate snack 30-60 min before, or nothing, then a real meal after.
reasoning: >
  Guest et al. 2021 (J Int Soc Sports Nutr 18:1) consolidates the caffeine
  RCT and meta-analysis base: 3-6 mg/kg consistently improves performance,
  benefits span strength, power, sprint and endurance, 60 min pre-exercise is
  the commonest timing, and response varies between people. That is enough
  for the direction and the dose band. The dawn-specific claim is narrower:
  Mora-Rodriguez et al. 2012 (PLoS One 7(4):e33807), a double-blind crossover
  in 12 highly trained men, found 3 mg/kg at 10:00 restored velocity toward
  the 18:00 level -- graded down for n and for the 10:00 test time. Gardiner
  et al. 2023 (Sleep Med Rev 69:101764) pooled 24 studies to show caffeine
  cuts about 45 min of total sleep and lightens it, and derived the 8.8 h and
  13.2 h cutoffs from dose-timing data; the harm is graded higher than the
  cutoff hours. EFSA 2015 (EFSA Journal 13(5):4102) supplies the safety
  ceiling, which matters because 3 mg/kg for a 75-85 kg lifter is already
  225-255 mg. Aird et al. 2018 (Scand J Med Sci Sports 28(5):1476-1493)
  splits fed vs fasted by duration and did not pool resistance work; Bin
  Naharudin et al. 2019 (J Strength Cond Res, doi 10.1519/JSC.0000000000003054)
  is the one resistance trial, unblinded (a meal against water), in habitual
  eaters, with sets to failure -- so it moves "fasted is fine" to "fasted is
  fine unless you usually eat and you are going to failure", not further.
  Thomas et al. 2016 is cited for the endurance exception only. Not
  contested: none of these sources oppose each other; the caveats narrow the
  claim.
---

# exercise/early-morning-caffeine-food-069 -- 새벽 운동 전 카페인과 음식

**One line:** coffee on waking helps a dawn session and will not cost tonight's
sleep; the afternoon coffee is the one to watch. Fasted is fine for an hour of
lifting; do not set a 03:00 alarm to eat.

## Caffeine

| Question | Answer | Strength |
|---|---|---|
| Does it help? | yes, 3-6 mg/kg; maybe from ~2 mg/kg | strong direction |
| More so in the morning? | it brought morning bar speed up to about evening level in one small trial | moderate |
| When? | about 60 min before is the common protocol; gum works faster | timing at dawn untested |
| Safe single dose? | up to 200 mg is no safety concern, even close to hard training | regulator ceiling |
| Tonight's sleep? | the dawn dose is ~17 h before bed and should not matter; a second dose should stop ~8.8 h (coffee) or ~13.2 h (pre-workout) before bed | rule of thumb |

## Food

- Session of about an hour of lifting: fasted is a legitimate choice. Eating
  before helps long aerobic work, not short sessions.
- If you normally eat breakfast and you train sets to failure, skipping food
  may cost some reps (one trial).
- Do not wake two hours early to eat; the sleep you lose costs more. A small,
  easy carbohydrate snack 30-60 min before, or nothing, and a real meal after.
- Over about an hour of continuous endurance work: take carbohydrate during
  the session.

## 한국어 요약 (답변용)

- 카페인은 체중 1kg당 3~6mg에서 근력·파워·지구력 모두에 효과가 있다. 2mg 정도부터 듣는 사람도
  있다. 아침에는 효과가 더 쓸모 있다. 오전 10시에 3mg/kg를 먹었더니 스쿼트·벤치 바 속도가 저녁
  수준 가까이 올라왔다(12명 연구). 새벽 5시를 직접 시험한 연구는 없다.
- 한 번에 200mg까지는 고강도 운동 2시간 안이라도 안전 문제가 없다고 본다. 하루 400mg까지가 일반
  성인 기준이다. 체중이 75kg만 넘어도 3mg/kg가 200mg을 넘으니 기본은 범위의 아래쪽이다. 임신 중이거나
  심혈관 질환이 있으면 구체적인 양을 말하지 않는다.
- 보통 운동 60분 전에 먹는 방식이 많다. 5시 운동이면 일어나자마자 커피를 마시면 된다. 4시 반 알림
  시점이면 첫 커피로는 조금 늦고, 껌 형태처럼 빨리 흡수되는 건 괜찮다.
- 새벽 커피는 밤잠을 거의 해치지 않는다. 잠들기 17시간쯤 전이기 때문이다. 문제는 오후 커피다.
  일찍 자는 사람은 커피(약 107mg)는 취침 8.8시간 전, 프리워크아웃(약 220mg)은 13.2시간 전까지만
  마신다. 예를 들어 21시 45분에 자면 커피는 오후 1시 전까지다. 이 시간은 연구를 모아 계산한 대략의
  기준이다.
- 음식: 한 시간 안팎의 근력운동이면 공복으로 해도 된다. 운동 전 식사는 긴 유산소에서만 효과가
  확인됐다. 다만 평소 아침을 먹는 사람이 실패 지점까지 세트를 하면 굶었을 때 반복 수가 줄 수 있다
  (스쿼트 68회→58회, 16명 연구).
- 먹으려고 새벽 3시에 일어나지 않는다. 일찍 깨서 잠이 줄어드는 쪽이 더 손해다. 운동 30~60분 전에
  소화가 쉬운 탄수화물 간식을 조금 먹거나 아무것도 안 먹고, 운동 후에 제대로 먹는다. 이 절충안은
  실천 경험에서 나온 판단이고 새벽에 시험한 연구는 없다.
- 한 시간 넘게 쉬지 않는 지구력 운동이면 운동 중에 탄수화물을 먹는다.
