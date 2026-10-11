---
# Set-floor sprint 2026-10-07 (dispatch kw-ex-set-floor-experience). The
# MAINTENANCE half: how little training keeps muscle you already have, and
# what a calorie deficit changes about the growth-vs-keep choice. The
# composer's cut mode (compose_rank_rules trainer_fit.cut_keep) narrows
# hypertrophy scope when minutes do not fit; this row says which floor the
# narrowed muscles may fall to. Companion rows: 070 (growth floors by
# experience), 072 (the set_floor rule). Does NOT restate 016: the claim
# that HIGH or RISING volume in a deficit best spares lean mass was tested
# and refuted there and stays refuted here.
id: exercise/maintenance-vs-growth-volume-cut-071
domain: exercise
grade: B (an energy deficit blunts lean-mass gain while strength gains hold); C (about a third of a growth week, with load kept, held muscle size in young adults for 32 weeks -- one RCT, thigh only, plus a narrative review; older adults needed more); D (which weekly volume best spares muscle during a cut, and the cut-phase floor split)
lane: "@performance-lit"
locale: universal
as_of: 2011-2026
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/21131862/"  # Bickel CS, Cross JM, Bamman MM 2011, Med Sci Sports Exerc 43(7):1177-1187 -- n=70, 16 wk of 3 d/wk (knee extension, leg press, squat, 3 x 8-12RM) then 32 wk of detraining, one-third dose (same 3 sets, 1 d/wk = 9 weekly sets) or one-ninth dose (1 set, 1 d/wk = 3 weekly sets), intensity kept: both doses preserved hypertrophy in the young (20-35 y), not in the old (60-75 y); the one-third dose added myofiber hypertrophy in the young; strength largely retained even with detraining
  - "https://pubmed.ncbi.nlm.nih.gov/33629972/"  # Spiering BA, Mujika I, Sharp MA, Foulis SA 2021, J Strength Cond Res 35(5):1449-1458 -- narrative review: strength and muscle size (younger) maintained up to 32 wk with 1 session/wk and 1 set per exercise if relative load is kept; older adults may need up to 2 sessions/wk and 2-3 sets per exercise; intensity is the key variable
  - "https://pubmed.ncbi.nlm.nih.gov/34623696/"  # Murphy C, Koehler K 2022, Scand J Med Sci Sports 32(1):125-137 -- meta-analysis/meta-regression of RCTs, resistance training in an energy deficit >=3 wk: lean-mass gain impaired vs no deficit (ES -0.57, p=0.02), strength gain comparable (ES -0.31, p=0.28); a deficit of ~500 kcal/day prevented lean-mass gain
  - "https://pubmed.ncbi.nlm.nih.gov/41843416/"  # ACSM 2026 Position Stand (Currier et al.), Med Sci Sports Exerc 58(4):851-872 -- >=10 sets/wk enhances hypertrophy; >=80% 1RM, 2-3 sets enhances strength
  - "exercise/deficit-volume-guidance-016"  # within-warehouse: deficit volume guidance is theory-only, the high-volume-spares-muscle claims were refuted
  - "exercise/set-floor-by-experience-070"  # within-warehouse: the growth floors this row's maintenance floor is measured against
  - "exercise/volume-landmarks-heuristic-015"  # within-warehouse: MV (maintenance volume) as a practitioner landmark
  - "framework:GRADE -- the deficit effect on lean-mass gain is a meta-analysis of RCTs (B). The maintenance dose rests on one RCT with about ten young people per arm and lower-body exercises only, plus a narrative review that leans on it (C). No trial tests maintenance volumes DURING an energy deficit, so carrying the energy-balanced maintenance dose into a cut is an extrapolation (D)."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      KEEPING IS CHEAP IF THE LOAD STAYS. In young adults, one session a
      week at the same 8-12RM loads, either 3 sets or 1 set per exercise,
      held the muscle gained over 16 weeks for the next 32 weeks. Volume
      and frequency can fall a long way; the load per set is what must not
      fall. Cut sets before cutting load, never the reverse.
    grade: C
  - note: >
      OLDER ADULTS NEED MORE TO KEEP. At 60-75 years neither the one-third
      nor the one-ninth dose kept the size gained, though strength held.
      For an older user, the maintenance floor is about two sessions a week
      and 2-3 sets per exercise, not one session; the age boundary in code
      is a product constant (the trial compared 20-35 with 60-75 only).
    grade: C
  - note: >
      A DEFICIT MOVES THE GOAL FROM GAIN TO KEEP, NOT THE VOLUME UP. In a
      deficit lean-mass gain is blunted and, near 500 kcal a day or more,
      absent on average, while strength still rises. So a cut is the phase
      where most muscles can sit at a maintenance floor; it is not evidence
      that more sets protect muscle (016 refuted that), and not evidence
      that fewer sets do either. Which volume spares the most muscle in a
      deficit is untested.
    grade: B
  - note: >
      PRIORITY MUSCLES KEEP THE GROWTH FLOOR WHEN MINUTES ALLOW. Splitting a
      cut week into priority muscles at the growth floor and the rest at a
      maintenance floor is a product rule built from the two findings above
      (keep needs little; a deficit blunts gain). It is not tested as a
      package.
    grade: D
  - note: >
      THE TRIAL WAS THE THIGH. Every maintenance number comes from knee
      extension, leg press and squat. Applying it to the chest, back, arms
      or calves is an extrapolation; the direction is plausible, the
      fractions are not measured there.
    grade: C
claim: >
  Muscle already gained can be held with far less training than it took to
  build, provided the load per set is kept: in young adults one weekly
  session at the same 8-12RM loads, at a third or even a ninth of the
  growth volume, preserved thigh muscle for 32 weeks, while adults aged
  60-75 lost the size at those doses and need about two sessions a week
  with 2-3 sets per exercise. An energy deficit blunts lean-mass gain (a
  deficit near 500 kcal a day prevents it on average) while strength still
  improves, so during a cut the realistic aim for most muscles is to keep,
  not to grow. A maintenance floor is therefore an acceptable cut-phase
  dose for lower-priority muscles; which volume best spares muscle in a
  deficit is untested, and the claim that high volume protects it stays
  refuted (016).
reasoning: >
  Bickel 2011 is the randomised maintenance-dose trial located in this
  sprint that measured muscle size (DXA, biopsy) over a long maintenance
  phase: the
  one-third arm kept three sets per exercise and cut frequency from three
  days to one; the one-ninth arm also cut to one set. Both held lean mass
  in the young; neither did in the old. Spiering 2021 summarises the same
  literature into the 1 session / 1 set (young) and 2 sessions / 2-3 sets
  (older) rule and names intensity as the key variable. Murphy and Koehler
  2022 pool RCTs of training in a deficit and find lean-mass gain impaired
  but strength preserved, with a ~500 kcal/day point at which gain stops.
  None of these trials put a maintenance dose inside a deficit; the cut
  split (priority at growth, rest at maintenance) is a product rule that
  combines them, and 016 already records that the high-volume-protects
  claims failed verification.
---

# exercise/maintenance-vs-growth-volume-cut-071 -- 감량 중엔 유지 볼륨이면 되나

**한 줄 그림:** 이미 만든 근육은 무게만 지키면 훨씬 적은 세트로 유지된다. 감량 중엔 대부분의
근육을 유지 목표로 두고, 우선 근육만 성장 최소선을 지킨다.

## What the engine reads from this row

| Situation | Floor the evidence allows | Basis |
|---|---|---|
| Young adult, keeping a muscle | one session a week; 1-3 sets per exercise; same load | one RCT (thigh) + review |
| Older adult (about 60+), keeping | about two sessions a week; 2-3 sets per exercise; same load | same RCT (60-75 lost size at lower doses) + review |
| Cut, priority muscle | growth floor (070) if minutes allow | product rule |
| Cut, other muscles | maintenance floor | product rule over the two findings |
| Any phase, what to cut first | sets and days before load | intensity is the variable that keeps |

## 한국어 요약 (답변용)

- 이미 키운 근육은 지키기가 키우기보다 훨씬 쉽다. 젊은 성인은 주 1회, 종목당 3세트나 1세트만 해도
  무게(8~12회 겨우 드는 무게)를 그대로 지키면 32주 동안 허벅지 근육이 유지됐다.
- 줄일 때는 세트와 횟수(빈도)를 먼저 줄이고 무게는 지킨다. 반대로 하면 안 된다.
- 60~75세는 같은 양으로 근육 크기가 유지되지 않았다(힘은 유지됐다). 나이가 있으면 주 2회,
  종목당 2~3세트를 유지선으로 본다. 몇 살부터 이 기준을 쓸지는 제품이 정한 경계다.
- 칼로리를 덜 먹는 동안에는 근육이 잘 늘지 않는다. 하루 500kcal 정도 모자라면 평균적으로 근육
  증가가 멈췄다. 그래도 힘은 계속 늘었다. 그래서 감량기에는 대부분의 근육을 "유지"에 두는 게
  현실적이다.
- 감량 중에 세트를 늘리면 근육이 더 지켜진다는 주장은 검증에서 떨어졌다. 세트를 줄이면 더 지켜진다는
  근거도 없다. 감량 중 어떤 볼륨이 근육을 가장 잘 지키는지는 아직 연구되지 않았다.
- 감량기에 우선 근육(하체·등·가슴 같은 큰 근육)은 시간이 되면 성장 최소선을 지키고, 나머지는
  유지선까지 내려도 된다는 건 위 두 결과를 묶은 제품 규칙이다.
- 유지 연구는 허벅지 운동만 다뤘다. 가슴·등·팔에 같은 비율을 쓰는 건 추론이다.
