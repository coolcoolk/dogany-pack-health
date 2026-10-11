---
# Body-composition measurement sprint 2026-10-07 (dispatch task
# kw-bc-inbody-measure-noise). The evidence row under 029's measure_rules.
# Deliberately NOT a duplicate of nutrition/body-composition-measurement-floor-011:
# 011 bounds ACCURACY (device vs reference) and declines to publish a threshold;
# this row supplies the PRECISION side -- how far one person's readings move
# between days with nothing real changing, and what moves them (meal, water,
# standing, unstandardised presentation, weekday). 011's sub-gap 4 (no LSC for
# the UNCONTROLLED case) stays open: every figure here is from fasted,
# standardised laboratory visits and is therefore a floor for the gym case.
# Read and not used: Koch 2022 (Iowa Orthop J, InBody S10) -- same-day
# inter-rater MDC in 19 orthopaedic-trauma inpatients, not transportable to a
# standing consumer device in healthy adults.
id: nutrition/bia-day-to-day-noise-028
domain: nutrition
lane: "@obs-inferential"
grade: B (direction and magnitude band; the single detection-threshold figure is a conference abstract, see notes)
locale: universal
as_of: 2001-2024
contested: no
sources:
  - "https://doi.org/10.3389/fnut.2024.1491931"  # Looney DP, Schafer EA, Chapman CL, et al. Front Nutr 2024;11:1491931. PMC11649400 -- InBody 770, 14 adults, duplicate tests on 5 standardised visits over 19+/-6 days (0700, >10 h fast, >48 h no strenuous exercise); test-retest ICC >= 0.999 whole body; within-person range across the 10 tests: body mass 1.7+/-0.7 kg, fat mass 1.5+/-0.6 kg, fat-free mass 1.8+/-0.7 kg, skeletal muscle mass 1.0+/-0.4 kg; between-day body-mass differences 0.1-0.7 kg; %BF bias vs DXA -4.0+/-2.8
  - "https://digitalcommons.wku.edu/ijesab/vol2/iss13/18"  # Siedler MR, Harty PS, Stratton MT, ... Tinsley GM. Int J Exerc Sci Conf Proc 2021;2(13):18. CONFERENCE ABSTRACT -- InBody 770 and Omron, 17 adults, two visits within 48 h, >= 8 h food/fluid/caffeine/alcohol fast; InBody day-to-day precision error 1.0 %BF, 0.7 kg FM, 0.9 kg FFM; least significant change 2.8 %BF, 1.9 kg FM, 2.4 kg FFM
  - "https://doi.org/10.2478/joeb-2022-0004"  # Tinsley GM, Stratton MT, Harty PS, et al. J Electr Bioimpedance 2022;13(1):10-20 -- randomised crossover, 20 adults, InBody 770 after overnight fast; 11 mL/kg water: the added body mass was read exclusively as fat mass (~1.3 kg above baseline at 60 min); upright posture alone lowered TBW and lean mass ~0.5 kg over the hour in both conditions
  - "https://doi.org/10.1093/ajcn/74.4.474"  # Slinde F, Rossander-Hulthen L. Am J Clin Nutr 2001;74(4):474-478. PMID 11566645 -- 18 adults, 18 measurements over 24 h with 3 identical meals: impedance fell after each meal for 2-4 h, additively over the day; estimated %BF spanned 8.8 points (women) and 9.9 points (men) from highest to lowest reading
  - "https://doi.org/10.1017/S0007114517000551"  # Kerr A, Slater GJ, Byrne N. Br J Nutr 2017;117(4):591-601. PMID 28382898 -- 32 athletic males; non-standardised (afternoon, fed) and post-meal presentation produced substantially large changes in BIS fat mass and fat-free mass; biological error minimised only with standardised presentation
  - "https://doi.org/10.1123/ijsnem.2020-0061"  # Farley A, Slater GJ, Hind K. Int J Sport Nutr Exerc Metab 2021;31(1):55-65 -- 32 resistance-trained males; consecutive-day precision error for BIS fat mass 50 pct higher than same-day (3607 vs 2331 g); BIS not recommended for small changes
  - "https://doi.org/10.1123/ijsnem.2022-0219"  # Herberts T, Slater GJ, Farley A, et al. Int J Sport Nutr Exerc Metab 2023;33(4):222-229. PMID 37142404 -- InBody 720, 18 recreational athletes; replicating the prior 24 h of food, fluid and activity made between-day precision error not different from within-day
  - "https://doi.org/10.1371/journal.pone.0232152"  # Turicchi J, O'Driscoll R, Horgan G, et al. PLoS One 2020;15(4):e0232152. PMID 32353079 -- connected-scale weights, 1421 adults (weekly analysis): within-week fluctuation 0.35 pct, weekend gain and weekday loss; Christmas +1.35 pct not fully compensated
  - "https://doi.org/10.1159/000356147"  # Orsama AL, Mattila E, Ermes M, et al. Obes Facts 2014;7(1):36-47. PMID 24504358 -- 4657 daily weights, 80 adults: highest Sunday-Monday, falling through the week; weekend-weekday variation 'should be considered as normal instead of signs of weight gain'
  - "nutrition/body-composition-measurement-floor-011"  # accuracy side: reliability is not accuracy; never compare devices; visceral fat not spoken
applicability:
  axes:
    - key: body_fat_pct
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE DETECTION FLOOR UNDER IDEAL CONDITIONS. On an InBody 770, two fasted
      morning laboratory readings taken within 48 hours have to differ by at
      least about 2.8 percentage points of body fat, 1.9 kg of fat mass or 2.4
      kg of fat-free mass before the difference is more likely real than
      between-day error. The figure is from a conference abstract in 17
      adults, which is why it carries the observational band rather than the
      row's letter. It is a FLOOR: a gym reading taken at a different hour,
      fed, or after training sits on top of it by an unknown amount (011
      sub-gap 4 is still open).
    grade: C
  - note: >
      THE SAME PERSON SPANS KILOGRAMS WITH NOTHING CHANGING. Under the
      strictest protocol located (same 07:00 slot, overnight fast, two days
      without strenuous exercise), ten readings over about three weeks in
      healthy adults spanned on average 1.5 kg of fat mass, 1.8 kg of
      fat-free mass, 1.0 kg of skeletal muscle mass and 1.7 kg of body
      weight per person. That span includes real day-to-day biology, which is
      exactly the point: a user who never changed still sees numbers move by
      this much.
    grade: B
  - note: >
      FOOD, WATER AND STANDING PUSH THE READING IN DIRECTIONS THAT DO NOT
      CANCEL. Meals lower impedance for two to four hours and stack across
      the day, which lowers estimated body fat; a large glass of water on the
      InBody 770 was booked entirely as fat mass (about 1.3 kg after 11 mL/kg);
      an hour upright drifted lean mass down about 0.5 kg. Because the signs
      differ, no correction can be applied to a non-standard reading. It is
      either comparable or it is not.
    grade: B
  - note: >
      BODY WEIGHT HAS A WEEKLY RHYTHM. In free-living daily weighers, weight
      runs highest after the weekend and falls through the week, with an
      average within-week swing of about 0.35 percent of body weight
      (roughly 0.25 kg at 70 kg) and individual swings larger. A Monday
      reading compared with a Friday reading measures the weekday, not the
      diet.
    grade: B
  - note: >
      STANDARDISING THE DAY BEFORE HELPS. Replicating the previous 24 hours of
      food, fluid and activity brought between-day error on an InBody 720 down
      to within-day error in recreational athletes. This is the strongest
      located evidence that the measurement routine, not only the morning
      conditions, decides whether two readings can be compared. Single small
      sample, no number adopted from it.
    grade: C
claim: >
  On a consumer multi-frequency bioimpedance device (InBody class), the same
  person's readings move between days by amounts that are as large as the
  changes a few weeks of training or dieting can produce. Even fasted, rested,
  same-hour laboratory readings need a difference of roughly 2.8 points of body
  fat, 1.9 kg of fat mass or 2.4 kg of fat-free mass to exceed between-day
  error, and ten standardised readings of an unchanged adult over three weeks
  span about 1.5 kg of fat mass and 1.8 kg of fat-free mass. Meals, water,
  time upright and an unstandardised day before each shift the reading, in
  directions that do not cancel. Scale weight carries its own weekly rhythm
  (heaviest after the weekend). A single reading, or a difference between two
  readings, is therefore not evidence of a change in body composition; a
  repeated same-device, same-routine trend is.
reasoning: >
  Every source measures repeat readings against themselves or against a
  controlled perturbation, so the direction is direct measurement rather than
  modelled inference, and no source disputes it; that supports the
  pre-consensus band for the direction and the magnitude band (about one to
  two kilograms, two to three points). The samples are small (14 to 32 for the
  device studies), mostly young, healthy and in laboratories, and the one
  study that states an InBody least-significant-change figure is a conference
  abstract; the specific threshold is therefore carried as an observational
  note, not as the row's letter, and is explicitly a floor. The BIS studies
  (Kerr, Farley) are a different impedance technology and are used only for the
  direction (non-standardised presentation and consecutive days enlarge error),
  not for any number. The weekly weight rhythm comes from two large free-living
  connected-scale datasets and transfers directly to a user weighing at home.
  What this row cannot say is how large the error is for an unstandardised
  gym or home reading; that stays an open gap on 011 and in GAPS.md.
---

# nutrition/bia-day-to-day-noise-028 -- 인바디 숫자는 하루하루 얼마나 흔들리나

**한 줄 그림:** 인바디는 같은 사람을 재도 날마다 1-2kg, 체지방률 2-3%p 정도는 그냥 흔들린다.
한 번 잰 숫자, 두 번 사이의 차이로는 몸이 바뀌었다고 말할 수 없다.

## What the engine reads from this row

| Quantity (InBody 770 class) | Noise between days, nothing changing | Strength of the evidence |
|---|---|---|
| body fat % | must differ by >= ~2.8 points (fasted lab floor) | conference abstract, n=17 |
| fat mass | >= ~1.9 kg (floor); 1.5 kg span over 3 weeks | abstract; small lab study |
| fat-free mass | >= ~2.4 kg (floor); 1.8 kg span over 3 weeks | abstract; small lab study |
| skeletal muscle mass | no threshold located; 1.0 kg span over 3 weeks | small lab study |
| body weight (scale) | 0.1-0.7 kg between mornings; ~0.35 % weekly swing, heaviest after the weekend | lab study; two large free-living datasets |
| meal before the reading | lowers impedance 2-4 h, stacks over the day | small trial |
| water before the reading | booked as fat mass (~1.3 kg after a large glass) | randomised crossover |
| different gym hour / fed / after training | adds error of unknown size on top of the floor | direction only |

The thresholds are floors measured under ideal conditions. Accuracy against a
reference method and cross-device comparison are the separate row 011.

## 한국어 요약 (답변용)

- 인바디는 같은 기계로 같은 사람을 재도 날마다 숫자가 흔들린다. 아침 공복, 같은 시간, 운동 안 한
  상태로 맞춰 재도 체지방률은 약 2.8%p, 체지방량은 약 1.9kg, 제지방량은 약 2.4kg 넘게 달라야 진짜
  변화일 가능성이 높다. 이 기준은 17명 대상 학회 초록에서 나온 값이고, 실험실 조건에서 잰 최소치다.
- 헬스장에서 시간 아무 때나, 밥 먹고, 운동 끝나고 재면 흔들림은 더 커진다. 얼마나 커지는지 잰
  연구는 아직 찾지 못했다.
- 조건을 최대한 맞춰 3주 동안 10번 잰 실험에서도, 한 사람의 체지방량은 평균 1.5kg, 제지방량은
  1.8kg, 골격근량은 1.0kg, 체중은 1.7kg 범위 안에서 오르내렸다.
- 밥은 수치를 낮추는 쪽으로, 물 한 컵은 체지방이 늘어난 것처럼 보이게 하는 쪽으로 움직인다.
  방향이 서로 달라서 "밥 먹고 쟀으니 몇 kg 빼면 된다" 식의 보정은 할 수 없다. 조건이 같으면 비교하고,
  다르면 비교하지 않는다.
- 체중도 요일을 탄다. 주말 지나 월요일이 가장 무겁고 주중에 내려간다. 평균 흔들림은 체중의 0.35%
  정도다. 월요일 체중과 금요일 체중을 비교하면 식단이 아니라 요일을 비교하게 된다.
- 결론: 한 번 잰 숫자나 두 번 사이 차이로 "늘었다/줄었다"고 말하지 않는다. 같은 기계, 같은 조건으로
  여러 번 잰 흐름을 본다. 기계 간 비교와 정확도 문제는 011을 따른다.
