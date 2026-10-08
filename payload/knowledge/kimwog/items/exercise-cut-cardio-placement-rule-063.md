---
# Cardio-in-a-cut sprint 2026-10-06 (dispatch task kw-cardio-cut). The
# engine-readable synthesis of 062 for a program engine that has to place
# cardio in a lifting week during a fat-loss phase. It is a routing rule, not a
# primary finding: each rule names the graded row it rests on and its basis
# grade, and every product constant (minute bands, the 6 h gap, the step-up
# size) is labelled as a constant. Same posture as 056.
#
# placement_rules, mode_preference and dose_bands are structured data for the
# program engine. Minute values are PRODUCT DEFAULTS, never a measured
# threshold; the kcal ceiling is a meta-regression estimate (062), spoken as
# an approximate ceiling, never as this user's number.
#
# v38 MERGE (2026-10-07, dispatch kw-consolidate-2): the parallel
# kw-ex-cardio-interference-cut sprint's provisional row
# ("concurrent-cardio-interference-fat-loss", provisional 070, never released) is
# folded in. Carried: incline walking moved from mode rank 1 to rank 2
# (Gergley 2009 via 062); catalog_key on each mode, matching CARDIO_CATALOG
# in payload/service/health/movement_catalog.py; the caution-site-mode
# placement rule. NOT carried: its 60 / 30 / 300-minute ramp and 2-HIIT cap
# -- this row's dose_bands and step_up already own those constants, and two
# competing sets of product constants for the same decision would contradict.
id: exercise/cut-cardio-placement-rule-063
domain: exercise
grade: D (synthesis rule over 062; the ordering of priorities is B/C-backed, every minute band and gap length is product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/concurrent-cardio-interference-cut-062"  # the evidence row: average interference ~0; same-session, trained, mode, dose and deficit modifiers
  - "nutrition/weight-loss-rate-lean-mass-012"  # rate of loss; the weekly target the deficit serves
  - "nutrition/energy-availability-threshold-010"  # the floor that a large cardio dose can push a user under
  - "exercise/deficit-volume-guidance-016"  # lifting volume in a deficit, theory-only; unchanged here
  - "exercise/caution-severity-ladder-056"  # a caution site at the knee, hip, ankle or foot can veto a cardio mode
  - "exercise/tendon-fascia-load-management-055"  # stepmill and incline walking load the calf / Achilles and plantar fascia; the 055 pain ceiling applies at a caution site
  - "exercise/knee-pain-symptom-guided-loading-057"  # stepmill and incline walking load the knee; the 057 knee ceiling applies at a knee caution site
  - "https://pubmed.ncbi.nlm.nih.gov/19127177/"  # Donnelly JE et al. 2009, ACSM Position Stand -- 150-250 min/week moderate activity gives modest loss with moderate diet restriction; >250 min/week for clinically significant loss and regain prevention
  - "https://pubmed.ncbi.nlm.nih.gov/24998610/"  # Helms ER et al. 2015, J Sports Med Phys Fitness 55(3):164-178 -- lowest cardio frequency and duration that achieves the fat loss; cycling or full-body modes may reduce interference
  - "dispatch task kw-cardio-cut 2026-10-06: how a program engine should place cardio (mode, placement, dose) during a fat-loss phase without costing strength or muscle"
  - "framework:GRADE -- keep-lifting and diet-first are supported by randomised diet-plus-modality trials (Villareal 2017, Willis 2012 via 062); lift-first and separate-session placement by meta-analyses in trained or mixed samples (062); the mode preference is contested; stepmill / incline walking have no interference data; minute bands, the 6 h gap and the step-up size are product constants. No trial tested any of these rules inside a deficit in trained lifters."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: ask
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
placement_rules:
  - rule: keep-lifting
    when: always in a fat-loss phase
    do: lifting sessions are fixed first; cardio is added around them and never replaces a lifting session
    basis: exercise/concurrent-cardio-interference-cut-062
    basis_grade: B
  - rule: separate-first
    when: training_status is trained, or the user's goal names strength or leg performance
    do: put cardio on a non-lifting day, or at least 6 h away from lifting (product constant; 3 h is the minimum the pooled analysis separated)
    basis: exercise/concurrent-cardio-interference-cut-062
    basis_grade: C
  - rule: lift-first-if-same-session
    when: cardio must share a session with lifting
    do: lifting first, cardio after; never cardio as a long pre-lift block (a 5-10 min warm-up is not this rule)
    basis: exercise/concurrent-cardio-interference-cut-062
    basis_grade: B
  - rule: guard-leg-day
    when: the cardio is HIIT, a hard stepmill / stair session, or any session the user rates hard
    do: count it as lower-body fatigue; do not place it on the day before or the same session as the heaviest lower-body day; upper-body or rest days first
    basis: exercise/concurrent-cardio-interference-cut-062
    basis_grade: D
  - rule: beginner-relaxed
    when: training_status is untrained or novice
    do: placement is a preference, not a constraint; same-session cardio after lifting is acceptable if it is the only way the user trains
    basis: exercise/concurrent-cardio-interference-cut-062
    basis_grade: C
  - rule: caution-site-mode
    when: 056 places a lower-limb site (knee, ankle, Achilles, plantar fascia, hip) at history-recent or above
    do: drop running first; prefer cycling or rowing; treat stepmill and incline walking as loaded exposure of the calf / Achilles and the knee, monitored with the 055 / 057 pain ceilings
    basis: exercise/caution-severity-ladder-056
    basis_grade: D
  - rule: diet-before-cardio
    when: fat loss stalls on the multi-week trend (012)
    do: before adding cardio minutes, check that the total deficit (diet gap plus cardio cost) is not already near the ceiling; if it is, do not add cardio, hold
    basis: exercise/concurrent-cardio-interference-cut-062
    basis_grade: C
mode_preference:
  - mode: cycling
    catalog_key: bike
    rank: 1
    note: low impact, concentric-dominant; favoured in two of four pooled analyses, worse only as a non-significant HIIT trend
    basis_grade: C
  - mode: incline-walk
    catalog_key: incline_walk
    rank: 2
    note: low impact, low intensity; the one trial (Gergley 2009, n=30 untrained, via 062) found it cost MORE leg-press gain than cycling, so it sits below cycling, never level with it; ranked above running for impact, not for less interference
    basis_grade: C
  - mode: stepmill
    catalog_key: stepmill
    rank: 2
    note: low impact but a leg-dominant load at hard effort; no interference data; counts as leg fatigue when hard
    basis_grade: D
  - mode: rower-or-elliptical
    catalog_key: row
    rank: 2
    note: low impact, whole-body; no interference data in this row
    basis_grade: D
  - mode: running
    catalog_key: run
    rank: 3
    note: not excluded; worse in one older pool and at type I fibres, no difference in the newest pool; prefer when the user enjoys it over not doing cardio at all
    basis_grade: C
dose_bands:
  - band: start
    minutes_per_week: [0, 90]
    intensity: easy to moderate
    use: default first block of a cut; the diet carries most of the deficit
    basis_grade: D
  - band: standard
    minutes_per_week: [90, 150]
    intensity: easy to moderate, at most 1 hard session
    use: after a multi-week stall when the deficit ceiling still has room
    basis_grade: D
  - band: high
    minutes_per_week: [150, 250]
    intensity: mostly easy
    use: only with an explicit user preference for more activity over less food, and with the deficit ceiling checked; matches the ACSM moderate-activity range for weight loss
    basis_grade: C
deficit_budget:
  total_deficit_ceiling_kcal_per_day: 500
  counts: diet gap plus estimated cardio energy cost
  meaning: approximate ceiling above which pooled trials saw lean-mass gain stop; strength gains were kept
  basis_grade: C
step_up:
  minutes_per_step: 30
  min_weeks_between_steps: 2
  basis_grade: D
refraction_notes:
  - note: >
      THE ORDER IS THE EVIDENCE, THE NUMBERS ARE NOT. Keep lifting, then
      watch the total deficit, then separate or sequence cardio, then pick a
      mode: that ordering follows the size and certainty of the effects in
      062. The minute bands, the 6 h gap, the 30-minute step and the 2-week
      wait are product constants. Speak them as the plan's rule.
    grade: D
  - note: >
      THE CEILING IS A TOTAL, NOT A CARDIO BUDGET. The ~500 kcal a day
      figure is the whole deficit, diet plus cardio. An engine that raises
      cardio minutes without lowering the diet gap is raising the deficit.
      The figure is a pooled estimate from mixed populations; with a measured
      trend (012) the trend wins.
    grade: C
  - note: >
      MODE IS A TIE-BREAK, NOT A GATE. Cycling ranks first because it costs
      the least and the evidence leans its way; incline walking, stepmill and
      rowing come next (the one incline-walking trial found it worse than
      cycling, and stepmill has no data), but the mode evidence is split.
      Never tell a user that stepmill or incline walking does not interfere. A user who will run and will not cycle should
      run. A caution site at the knee, ankle or foot (056) moves impact modes
      down for that user regardless of this ranking.
    grade: C
  - note: >
      BEGINNERS CAN STACK. In untrained and moderately trained people adding
      cardio did not cost leg strength even in the same session. The
      separation rules protect trained lifters; do not make a beginner's week
      harder to follow to satisfy them.
    grade: C
  - note: >
      CARDIOVASCULAR CONDITION GATES SPECIFICS. With a heart condition
      unknown or reported, no hard-intensity session and no minute target is
      prescribed; general activity information only, and the medical route
      applies.
    grade: D
claim: >
  To place cardio in a fat-loss phase without costing strength or muscle, a
  program engine should apply five rules in order. First, keep every lifting
  session; cardio is added around lifting, never swapped in for it. Second,
  treat the total deficit (diet gap plus cardio energy cost) as the main
  risk to muscle and keep it near or under about 500 kcal a day; when fat
  loss stalls, check that total before adding minutes. Third, for trained
  lifters put cardio on a non-lifting day or several hours away from lifting
  (product default 6 h); if it must share a session, lift first. Fourth,
  treat hard intervals and hard stepmill work as leg fatigue and keep them
  off the day before or the session of the heaviest lower-body day. Fifth,
  prefer low-impact modes (cycling first, then incline walking, stepmill
  or rowing) as a tie-break, not a rule; at a lower-limb caution site drop
  running first. Start low (0-90 min a week), step up by about 30 minutes no more
  often than every two weeks, and reserve 150-250 minutes for users who
  prefer moving more over eating less. Beginners can stack cardio after
  lifting without measurable cost.
reasoning: >
  The rules are ordered by effect size and certainty in 062. Swapping lifting
  for cardio during a diet costs the most lean mass and strength in
  randomised trials, so keep-lifting is first. The deficit ceiling comes next
  because it is the one quantified effect on lean mass in a deficit, and
  cardio feeds it directly. Session separation and lift-first ordering rest
  on consistent meta-analytic subgroups in trained samples and are worth a
  few kilograms of leg 1RM, which matters to a lifter on a cut and not to a
  beginner. Mode is last because the pooled analyses disagree. The dose
  bands borrow the ACSM 150-250 minute range for the upper band and the
  practitioner advice to use the least cardio that achieves the loss for the
  lower ones; none of the band edges has been tested as a boundary.
---

# exercise/cut-cardio-placement-rule-063 -- 감량기 유산소 배치 규칙

**한 줄 그림:** 웨이트는 그대로 두고, 전체 적자를 먼저 보고, 유산소는 다른 날이나 웨이트 뒤에, 종목은 마지막에
고른다.

## The rules (engine order)

| # | Rule | When | Do | Basis |
|---|---|---|---|---|
| 1 | keep-lifting | always | cardio is added, never swapped for a lifting session | 062, RCTs |
| 2 | deficit total | stall, or adding minutes | diet gap + cardio cost near or under ~500 kcal/day | 062, meta-regression |
| 3 | separate / lift-first | trained, or strength goal | other day or >=6 h apart (product); same session: lift first | 062, meta-analyses |
| 4 | guard leg day | HIIT, hard stepmill | count as leg fatigue; not before or with heaviest leg day | product |
| 5 | mode tie-break | choosing | cycling > incline walk, stepmill, rower, elliptical > running | contested |
| -- | caution-site-mode | lower-limb site at history-recent or above (056) | drop running first; cycling / rowing; stepmill and incline walk monitored as loaded exposure | product |

| Dose band | Minutes / week (product) | Use |
|---|---:|---|
| start | 0-90 | first block; diet does most of the deficit |
| standard | 90-150 | after a multi-week stall with room under the ceiling |
| high | 150-250 | user prefers moving more over eating less; ceiling checked |

Step up by about 30 minutes, no more often than every 2 weeks (product).

## 한국어 요약 (답변용)

- 감량기라도 웨이트 세션은 그대로 둔다. 유산소는 웨이트에 더하는 것이지 대신하는 것이 아니다.
- 근육을 지키는 데 제일 중요한 건 전체 적자다. 식단으로 만든 적자에 유산소로 태운 열량을 더한 값이
  하루 약 500kcal 근처를 넘지 않게 본다. 정체가 오면 유산소를 늘리기 전에 이 합계부터 확인한다. 500은
  연구를 모은 추정치이고, 실제 체중 추세가 있으면 추세를 따른다.
- 운동 경력이 있는 사람은 유산소를 웨이트 없는 날이나 웨이트와 몇 시간(제품 기준 6시간) 떨어뜨려 한다.
  꼭 같은 세션이면 웨이트 먼저, 유산소 나중.
- 인터벌이나 힘든 스텝밀은 하체 피로로 친다. 가장 무거운 하체 날 전날이나 같은 세션에는 넣지 않는다.
- 종목은 마지막에 고른다. 자전거를 먼저 권하고 경사 걷기·스텝밀·로잉이 그다음이다. 경사 걷기를
  직접 비교한 연구 하나에서는 자전거보다 다리 근력 손해가 컸으니 "간섭 없는 유산소"라고 하지 않는다. 근거가
  엇갈리니 달리기를 좋아하면 달리기를 해도 된다. 무릎·발목·발에 주의 부위가 있으면 달리기부터 빼고
  자전거·로잉을 권하며, 스텝밀과 경사 걷기도 다리에 부하가 가는 운동으로 보고 통증 기준을 적용한다.
- 양은 적게 시작한다(주 0~90분). 2주 이상 정체일 때 30분씩 올리고, 150~250분은 덜 먹기보다 더 움직이길
  원하는 사람에게만 쓴다. 분 단위 구간과 6시간 간격은 제품이 정한 규칙이다.
- 운동을 막 시작한 사람은 웨이트 뒤에 바로 유산소를 붙여도 손해가 거의 없다.
- 심장 질환이 있거나 여부를 모르면 고강도 세션과 분 목표는 정하지 않고, 일반 정보만 주고 진료를 권한다.
