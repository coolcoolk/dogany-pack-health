---
# Meal-protein sprint 2026-10-06 (dispatch task kw-meal-protein). The
# engine-readable synthesis a meal module reads to decide WHETHER and HOW to
# nudge protein from a meal log. It is a routing rule, not a primary finding:
# each rule names the graded row it rests on, and every product constant (the
# logged-day minimum, the 7-day window, the 0.9 margin) is labelled as a
# constant. Same posture as exercise/caution-severity-ladder-056.
#
# target_bands and nudge_rules are structured data. Numbers in target_bands are
# g protein per kg body weight per day, copied from the graded items, for
# RESCALE against measured body weight -- never computed by the model. The
# YAML-subset reader returns scalars as strings; cast with float()/int().
id: nutrition/meal-protein-nudge-rules-063
domain: nutrition
lane: "@meal-craft"
grade: D (synthesis rule over 002, 008, 009, 019, 021, 062; each rule carries its own basis grade; every constant is product judgement)
locale: universal
as_of: 2026
contested: no
sources:
  - "nutrition/protein-intake-002"  # general daily range 1.4-2.0 g/kg; per-meal 0.25 g/kg or 20-40 g
  - "nutrition/protein-deficit-lean-mass-target-062"  # deficit band 1.6-2.4 g/kg; older-adult floor; CKD gate
  - "nutrition/protein-per-meal-ceiling-008"  # no basis for "above ~40 g is wasted"
  - "nutrition/protein-distribution-thin-009"  # even split not established; skew is not a defect
  - "nutrition/self-report-underreporting-007"  # logged intake is a floor
  - "nutrition/unlogged-day-not-zero-019"  # missing days are missing, not zero
  - "nutrition/kr-protein-exchange-counting-021"  # 8 g per meat-and-fish exchange; split justified by loggability, not physiology
  - "exercise/protein-anabolic-window-002"  # wide post-exercise window
  - "https://doi.org/10.1186/1550-2783-10-53"  # Schoenfeld BJ, Aragon AA, Krieger JW. J Int Soc Sports Nutr 2013;10:53. PMID 24299050 -- timing meta-regression: no timing effect once covariates are controlled; total protein the strongest predictor of hypertrophy effect size
  - "https://doi.org/10.1093/gerona/glu103"  # Moore DR, Churchward-Venne TA, Witard O, et al. J Gerontol A Biol Sci Med Sci 2015;70(1):57-62. PMID 25056502 -- retrospective pooled tracer data: per-meal MPS plateau at 0.40 vs 0.24 g/kg body mass in older vs younger men (p=.055), 0.60 vs 0.25 g/kg LBM (p<.01)
  - "https://doi.org/10.3945/jn.114.208371"  # Snijders T, Res PT, Smeets JS, et al. J Nutr 2015;145(6):1178-1184. PMID 25926415 -- RCT, n=44 young men, 12 wk RT: 27.5 g protein pre-sleep vs non-caloric placebo increased strength and quadriceps CSA (total daily protein not matched)
  - "https://doi.org/10.1016/j.jamda.2013.05.021"  # PROT-AGE 2013, PMID 23867520 -- timing and quality evidence "not yet sufficient to support specific recommendations" in older people
  - "owner request 2026-10-06 (dispatch task kw-meal-protein): rules a meal module can use to nudge"
  - "framework:GRADE -- the daily bands inherit their item grades (002 A, 062 B); the per-meal older-adult dose is a pooled retrospective tracer analysis (C); the pre-sleep option is one RCT without matched daily protein (C); the windows, margins and logged-day minimums are product constants with no direct evidence."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: ask
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: renal_condition
      type: categorical
      role: hard
      unknown_policy: hedge
      gate:
        allowed: [none, healthy]
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
target_bands:
  - context: general
    when: primary_goal not fat loss, age under 65, renal none or unknown
    low: 1.4
    high: 2.0
    basis: nutrition/protein-intake-002
    basis_grade: A
  - context: deficit
    when: primary_goal is fat loss or weight loss with resistance training, age under 65
    low: 1.6
    high: 2.4
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: B
  - context: older
    when: age 65 or over, not dieting
    low: 1.0
    high: none
    low_if_active: 1.2
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: B
  - context: older-deficit
    when: age 65 or over and losing weight
    low: 1.2
    high: none
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: B
  - context: renal
    when: renal_condition stated and not none or healthy
    low: none
    high: none
    action: withhold target; refer to clinician
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: A
per_meal_dose:
  - group: under-65
    g_per_kg: 0.25
    absolute_g: 20-40
    use: size of the protein add-on suggested for a protein-poor meal; NOT a cap
    basis: nutrition/protein-intake-002
    basis_grade: B
  - group: 65-plus
    g_per_kg: 0.4
    absolute_g: none
    use: same, older adults; body-mass difference vs young was borderline (p=.055)
    basis: Moore 2015 (PMID 25056502)
    basis_grade: C
nudge_rules:
  - rule: window
    trigger: always
    action: judge protein on the mean of LOGGED days in the last 7 days; need at least 4 logged days, else no nudge and at most one note that the log is too thin to judge
    never: judge a single meal or a single day; count an unlogged day as zero
    constants: [7-day window, 4 logged days]
    basis: nutrition/unlogged-day-not-zero-019
    basis_grade: D
  - rule: below-floor
    trigger: 7-day logged mean below 0.9 x band low (x body weight)
    action: one nudge naming the gap in grams per day (and in meat-and-fish exchanges on a KR log, gap / 8), suggesting an add-on of one per-meal dose to the lowest-protein meal
    never: more than one protein nudge per day; frame the gap as muscle loss already happening
    constants: [0.9 margin, one nudge per day]
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: B
  - rule: logged-is-floor
    trigger: a below-floor nudge is about to be sent
    action: phrase it as "your log shows", since true intake is likely higher than logged
    never: apply a correction factor to the logged number
    constants: []
    basis: nutrition/self-report-underreporting-007
    basis_grade: A
  - rule: in-band
    trigger: 7-day logged mean at or above band low
    action: no nudge; a confirmation is allowed when the user asks
    never: push toward the band top; suggest more protein "for safety"
    constants: []
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: B
  - rule: above-band
    trigger: 7-day logged mean above band high
    action: no nudge in either direction for a healthy adult
    never: warn of kidney harm without a stated renal condition; call the excess wasted
    constants: []
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: B
  - rule: large-meal
    trigger: a single meal above 40 g protein
    action: none
    never: say protein above 20-40 g in one meal is wasted or oxidised
    constants: []
    basis: nutrition/protein-per-meal-ceiling-008
    basis_grade: B
  - rule: skewed-day
    trigger: most of the day's protein in one meal (e.g. dinner)
    action: none when the daily mean is in band; when below floor, the add-on goes to the lowest meal because a per-meal count is easier to hit and to log
    never: present an even split as physiologically required; trade the daily total for evenness
    constants: []
    basis: nutrition/protein-distribution-thin-009
    basis_grade: C
  - rule: training-timing
    trigger: protein not eaten near a workout
    action: none
    never: invoke a 30-60 minute anabolic window
    constants: []
    basis: exercise/protein-anabolic-window-002
    basis_grade: B
  - rule: pre-sleep-option
    trigger: below floor AND the evening has no protein-containing meal
    action: may offer a pre-sleep protein snack (about 30-40 g) as ONE way to close the gap
    never: present pre-sleep protein as better than the same protein earlier in the day
    constants: []
    basis: Snijders 2015 (PMID 25926415)
    basis_grade: C
  - rule: renal-gate
    trigger: renal_condition stated and not none or healthy
    action: no target, no below-floor nudge; route to clinician
    never: quote a g/kg target
    constants: []
    basis: nutrition/protein-deficit-lean-mass-target-062
    basis_grade: A
refraction_notes:
  - note: >
      THE BANDS ARE THE EVIDENCE; THE WINDOW AND MARGIN ARE NOT. The daily
      bands are copied from 002 and 062. The 7-day window, the four-logged-day
      minimum, the 0.9 margin and the one-nudge-per-day cap are product
      constants chosen to keep nudges off log noise. Speak them as the app's
      rule, never as a threshold from research.
    grade: D
  - note: >
      NUDGE THE TOTAL, NOT THE PATTERN. Every rule that fires acts on the daily
      total. Skewed distribution, large single meals and distance from a
      workout never trigger a nudge on their own, because the evidence for
      correcting them is thin (009), refuted (008) or wide (exercise 002). A
      per-meal add-on is suggested only as the easiest place to close a daily
      gap, and that reason is stated.
    grade: B
  - note: >
      OLDER USERS GET A BIGGER ADD-ON, NOT A DIFFERENT RULE. The per-meal dose
      at 65+ is 0.4 g/kg rather than 0.25 g/kg, from one pooled retrospective
      tracer analysis in men whose body-mass difference was borderline. PROT-AGE
      itself calls timing evidence insufficient for a specific recommendation.
      Use the larger figure to size an add-on, never to grade a meal as failed.
    grade: C
  - note: >
      BODY WEIGHT MISSING -> ASK ONCE, THEN SPEAK IN EXCHANGES OR SKIP. Without
      a measured or stated weight, no g/kg band can be rescaled. Ask per the
      budget. Until then, do not invent a reference weight, and do not send the
      below-floor nudge.
    grade: D
claim: >
  A meal module should judge protein on the daily total, averaged over logged
  days, and nudge only when that total falls below the floor for the user's
  context. The floors are 1.4 g/kg body weight in general training, 1.6 g/kg in
  a deficit with resistance training, 1.0-1.2 g/kg for adults 65 and over, and
  1.2 g/kg for older adults who are losing weight. With a stated kidney
  condition there is no target and the user is routed to a clinician. When a
  nudge fires, it names the daily gap and suggests one per-meal dose added to
  the lowest-protein meal: about 0.25 g/kg (20-40 g) under 65, about 0.4 g/kg
  at 65 and over. Large meals, dinner-heavy days and protein eaten far from a
  workout never trigger a nudge by themselves, and nothing is ever called
  wasted.
reasoning: >
  This item turns graded rows into a decision table. It decides nothing that
  those rows do not already support. The bands carry their source grades:
  general from 002, deficit, older-adult and renal from 062. The pattern rules
  are deliberately null actions, because the evidence base for even
  distribution (009) and against large boluses (008) does not support
  correction, and the timing meta-regression found total intake, not timing,
  to be the predictor. The only place distribution re-enters is as craft (021):
  adding one dose to the poorest meal is the most loggable way to close a daily
  gap, and the rule says so. Log-handling rules come from the measurement items.
  The logged figure is a floor (007) and a missing day is not zero (019), which
  is why the window averages logged days only and requires a minimum count. The
  window length, the minimum count and the margin have no evidence behind them
  and are labelled as product constants, which keeps the whole item at the
  practitioner band.
---

# nutrition/meal-protein-nudge-rules-063 -- 식단 모듈의 단백질 넛지 규칙

**한 줄 그림:** 끼니가 아니라 하루 총량을 본다. 기록된 날들의 평균이 맥락별 하한보다 낮을 때만 한 번
권하고, 그 외에는 아무 말도 하지 않는다.

## Target bands (g per kg body weight per day)

| Context | Floor | Upper | Basis |
|---|---:|---:|---|
| general (under 65) | 1.4 | 2.0 | 002 |
| deficit + resistance training (under 65) | 1.6 | 2.4 | 062 |
| 65+, not dieting | 1.0 (1.2 if active) | -- | 062 |
| 65+, losing weight | 1.2 | -- | 062 |
| stated kidney condition | -- | -- | withhold, refer (062) |

## Nudge table

| Situation | Action |
|---|---|
| fewer than 4 logged days in 7 | no nudge |
| 7-day logged mean < 0.9 x floor | one nudge: gap in g/day (KR: gap / 8 exchanges), add one per-meal dose to the lowest meal |
| in band or above | none |
| one meal > 40 g | none, never "wasted" |
| dinner-heavy day | none on its own |
| no protein near workout | none, no 30-60 minute window |
| short and no evening protein | may offer about 30-40 g before sleep as one option |

The 7-day window, the 4-day minimum, the 0.9 margin and the one-per-day cap are
product constants.

## 한국어 요약 (답변용)

- 단백질은 끼니 하나, 하루 하나로 판단하지 않는다. 최근 7일 중 **기록된 날**의 평균으로 본다. 기록된
  날이 4일보다 적으면 권하지 않는다. 기록 안 된 날을 0으로 세지 않는다.
- 하한(일반 1.4, 감량 중 근력 운동 1.6, 65세 이상 1.0~1.2, 감량 중 고령 1.2 g/kg)의 90% 밑일 때만
  하루 한 번 권한다. 부족분을 하루 그램으로 말하고, 한국 식단이면 8로 나눠 어육류 교환 수로 말한다.
- 권할 때는 "기록상"이라고 말한다. 실제 섭취는 기록보다 많을 가능성이 높다.
- 보충은 단백질이 가장 적은 끼니에 한 번 분량(65세 미만 약 0.25 g/kg, 20~40 g / 65세 이상 약
  0.4 g/kg)을 더하는 방식으로 제안한다. 이유는 생리학이 아니라 지키기 쉽고 기록하기 쉬워서다.
- 한 끼에 40 g을 넘게 먹어도 "낭비"라고 하지 않는다. 저녁에 몰아 먹는 것도, 운동 직후에 안 먹는
  것도 그 자체로는 권할 이유가 아니다.
- 하루가 부족하고 저녁에 단백질이 없으면 자기 전 30~40 g 간식을 여러 방법 중 하나로 제안할 수 있다.
  다른 시간에 먹는 것보다 낫다고 말하지 않는다.
- 콩팥 질환이 있다고 밝힌 사람에게는 목표치도 권유도 주지 않고 담당 의료진에게 연결한다.
- 7일, 4일, 90%, 하루 한 번은 앱이 정한 규칙이다. 연구에서 나온 기준처럼 말하지 않는다.
