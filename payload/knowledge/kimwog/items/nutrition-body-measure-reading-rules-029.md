---
# Body-composition measurement sprint 2026-10-07 (dispatch task
# kw-bc-inbody-measure-noise). The engine-readable synthesis of 028 (precision:
# between-day noise, meal / water / standing, weekly weight rhythm) and 011
# (accuracy: device bias, no cross-device comparison, visceral fat unspoken).
# A routing rule for copy, not a primary finding: each rule names the graded
# row it rests on, and every product constant (bands, windows, cadence) is
# labelled as a constant. Same posture as exercise/caution-severity-ladder-056.
#
# noise_bands, measure_rules and cadence are structured data for the retro /
# brief copy (brief_lib body_line, goal_verdict) -- field guide:
# docs/kimwog-measure-rules-fields.md. Metric names follow metric_log
# (weight_kg, body_fat_pct); the other body-composition names are the ones an
# InBody import would carry. Values are THRESHOLDS FOR SPEAKING, never a claim
# about what the user's body did.
id: nutrition/body-measure-reading-rules-029
domain: nutrition
lane: "@obs-inferential"
grade: D (synthesis rule over 028 and 011; the direction is B-backed, every band and cadence is product judgement)
locale: universal
as_of: 2026
contested: no
sources:
  - "nutrition/bia-day-to-day-noise-028"  # between-day noise floors, meal / water / standing, weekly weight rhythm
  - "nutrition/body-composition-measurement-floor-011"  # reliability is not accuracy; one device only; visceral fat not spoken
  - "nutrition/weight-loss-rate-lean-mass-012"  # the rate rule is itself a convention; used only to size the cadence argument
  - "nutrition/weekend-drift-073"  # (parallel v38 sprint) the weekday weight rhythm behind weekday-not-diet, and the like-day comparison the weekly retro uses
  - "nutrition/self-monitoring-frequency-027"  # (parallel v38 sprint) its weighing-exit rule overrides the daily weight_kg cadence default here
  - "framework:GRADE -- that a single reading or a two-point difference cannot show a body-composition change is supported by direct repeat-measurement studies (028, 011); the specific speaking bands, the 7-day weight mean, the 3-reading confirmation and the 2-4 week body-composition cadence are product constants with no direct evidence."
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
noise_bands:
  - metric: weight_kg
    compare: 7-day mean against the previous 7-day mean, at least 3 readings in each week
    evidence_floor: none located for a mean-to-mean difference; single mornings 0.1-0.7 kg apart, 3-week span 1.7 kg, weekly swing about 0.35 pct
    speak_band: 0.5
    single_pair_band: 1.0
    unit: kg
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: D
  - metric: body_fat_pct
    compare: reading against the previous comparable reading on the same device
    evidence_floor: 2.8
    speak_band: 3.0
    unit: percentage points
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: C
  - metric: fat_mass_kg
    compare: reading against the previous comparable reading on the same device
    evidence_floor: 1.9
    speak_band: 2.0
    unit: kg
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: C
  - metric: fat_free_mass_kg
    compare: reading against the previous comparable reading on the same device
    evidence_floor: 2.4
    speak_band: 2.5
    unit: kg
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: C
  - metric: skeletal_muscle_kg
    compare: reading against the previous comparable reading on the same device
    evidence_floor: none located; 3-week span of an unchanged adult 1.0 +/- 0.4 kg
    speak_band: 1.5
    unit: kg
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: D
  - metric: visceral_fat
    compare: never
    evidence_floor: poorest agreement of any output
    speak_band: never
    unit: device score
    basis: nutrition/body-composition-measurement-floor-011
    basis_grade: B
measure_rules:
  - rule: one-reading-no-direction
    when: only one reading in the window, or the previous reading is outside the freshness window
    then: show the value and its date; no direction word, no arrow, no verdict of progress
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: B
  - rule: inside-band-is-steady
    when: the difference to the comparison value is smaller than the metric's speak_band (single_pair_band for two single weights)
    then: say steady / within the normal day-to-day range; never gained, lost, up or down
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: D
  - rule: outside-band-once-is-possible
    when: one comparison exceeds speak_band and no earlier comparison agrees in direction
    then: say possible change, the next reading will tell; do not attribute it to diet or training
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: D
  - rule: confirmed-trend
    when: at least 3 comparable readings, and the last two comparisons both move the same way, with the first-to-last difference beyond speak_band
    then: the change may be spoken as a trend over the dates, with the first and last values
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: D
  - rule: comparable-or-not
    when: either reading lacks the standard conditions (same device, on waking, after the toilet, before food, drink and training) or the conditions are unknown
    then: treat as not comparable for body-composition outputs; show the value only; body weight may still enter a 7-day mean
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: B
  - rule: no-correction
    when: a reading is known to be fed, after water, after training or at another hour
    then: never adjust the number by an estimated offset; meal and water push in different directions
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: B
  - rule: one-device-only
    when: the two readings come from different devices or device models
    then: no comparison at all; restart the trend on the new device
    basis: nutrition/body-composition-measurement-floor-011
    basis_grade: B
  - rule: weekday-not-diet
    when: comparing two single body weights taken on different weekdays
    then: prefer the 7-day mean; if only singles exist, do not read a Monday-high or Friday-low as a diet effect
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: B
  - rule: goal-near-not-reached
    when: a single reading crosses a goal target, or sits inside speak_band of it
    then: say near the target, confirm with the next reading; reached only under confirmed-trend; a hold goal without its own noise_sd uses speak_band
    basis: nutrition/bia-day-to-day-noise-028
    basis_grade: D
cadence:
  - metric: weight_kg
    how_often: daily or at least 3 mornings a week
    condition: on waking, after the toilet, before food and drink, same scale
    read_as: 7-day mean
    basis_grade: D
  - metric: body_composition
    how_often: every 2 to 4 weeks, not more than weekly
    condition: same device, morning, fasted, before training, and a similar day before
    read_as: trend across at least 3 readings
    basis_grade: D
refraction_notes:
  - note: >
      THE DIRECTION IS THE EVIDENCE, THE BANDS ARE NOT. That one reading, or the
      gap between two, cannot show a body-composition change is measured (028,
      011). The speak bands round the fasted laboratory floors upward and are
      product constants; the weight bands and the skeletal-muscle band have no
      published floor at all. Speak them as the plan's reading rule, never as a
      measured threshold.
    grade: D
  - note: >
      A REAL GYM READING IS NOISIER THAN THE BAND. Every evidence floor comes
      from fasted, rested, same-hour visits. A gym or home reading without
      those conditions carries more error of unknown size, which is why the
      comparable-or-not rule withholds a body-composition difference rather
      than widening the band to a guessed number.
    grade: C
  - note: >
      WHY NOT WEEKLY BODY-COMPOSITION SCANS. At a body-weight loss of 0.5 to 1
      percent a week (itself a convention, 012), a fat-mass change takes about
      three to four weeks to clear a 2 kg band, and a lean-mass gain usually
      takes longer. Scanning more often than every two weeks mostly reports
      noise and invites over-reading. The 2-4 week cadence is product
      judgement built on that arithmetic, not a trial.
    grade: D
  - note: >
      SILENCE IS NOT THE ANSWER. Inside the band the copy still shows the
      numbers and says steady; it does not hide the reading. The rule removes
      the verdict, not the data.
    grade: D
claim: >
  Body-weight and bioimpedance readings are spoken by these rules: a single
  reading gets a value and a date, never a direction; a difference smaller than
  the metric's band (weight 0.5 kg between 7-day means or 1.0 kg between two
  single mornings; body fat 3 points; fat mass 2 kg; fat-free mass 2.5 kg;
  skeletal muscle 1.5 kg) is called steady; a single difference beyond the band
  is a possible change awaiting the next reading; only three or more comparable
  readings moving the same way are spoken as a trend. Readings are comparable
  only on one device under the same morning, fasted, pre-training routine;
  unknown conditions mean not comparable, and no reading is corrected by an
  estimated offset. Visceral-fat scores are not spoken. Weigh most mornings
  and read the weekly mean; scan body composition every two to four weeks. The
  direction of every rule is evidence-backed; the bands, windows and cadence are
  product constants.
reasoning: >
  The rules come straight from the two graded rows. 028 supplies the size of
  between-day noise under ideal conditions (about 2.8 points, 1.9 kg and 2.4 kg
  on an InBody 770, and kilogram-scale spans in unchanged adults), the fact that
  meal, water and standing move the reading in directions that do not cancel
  (hence no-correction and comparable-or-not), and the weekly weight rhythm
  (hence the 7-day mean and weekday-not-diet). 011 supplies one-device-only and
  the visceral-fat silence. The three-reading confirmation is the simplest rule
  that a single noisy reading cannot satisfy on its own. The bands are rounded
  upward from the floors because a gym reading is never cleaner than the
  laboratory one. The axes are soft with hedge: without a reading the copy shows
  nothing and asks nothing; with one, these rules decide only the words around it.
---

# nutrition/body-measure-reading-rules-029 -- 체중·인바디 숫자를 말하는 규칙

**한 줄 그림:** 숫자는 보여 주되, 한 번 잰 값이나 두 번 사이 차이로 "늘었다/줄었다"고 판정하지
않는다. 같은 조건으로 여러 번 잰 흐름만 변화로 말한다.

## The bands (product constants over 028's floors)

| Metric | Compare | Evidence floor | Speak band |
|---|---|---:|---:|
| body weight | 7-day mean vs previous 7-day mean (>= 3 readings each) | none located | 0.5 kg |
| body weight, two single mornings | single vs single | none located | 1.0 kg |
| body fat % | comparable reading vs previous, same device | 2.8 points | 3 points |
| fat mass | same | 1.9 kg | 2 kg |
| fat-free mass | same | 2.4 kg | 2.5 kg |
| skeletal muscle mass | same | none located | 1.5 kg |
| visceral fat | never | -- | never spoken |

## The verdict ladder

| Situation | Copy says |
|---|---|
| one reading | value + date, no direction |
| difference inside the band | steady, within the day-to-day range |
| one difference beyond the band | possible change; next reading will tell |
| >= 3 comparable readings, last two moves agree, total beyond the band | trend, with first and last values and dates |
| unknown or non-standard conditions (body composition) | value only, not compared |
| different devices | not compared; trend restarts |

## 한국어 요약 (답변용)

- 한 번 잰 숫자는 날짜와 함께 보여 주기만 한다. 늘었다, 줄었다는 말을 붙이지 않는다.
- 두 번 사이 차이가 흔들림 범위 안이면 "유지, 평소 흔들림 범위 안"이라고 말한다. 범위는 체중 주간
  평균끼리 0.5kg, 아침 체중 두 번끼리 1.0kg, 체지방률 3%p, 체지방량 2kg, 제지방량 2.5kg, 골격근량
  1.5kg이다. 이 숫자들은 연구에서 잰 최소치(028)를 올려 잡아 제품이 정한 규칙이다.
- 범위를 한 번 넘으면 "변화일 수 있다, 다음 측정에서 확인하자"까지만 말한다. 식단이나 운동 덕이라고
  단정하지 않는다.
- 같은 조건으로 세 번 이상 쟀고 최근 두 번이 같은 방향이며, 처음과 마지막 차이가 범위를 넘을 때만
  "흐름이 이렇다"고 말한다.
- 같은 기계로, 아침에 일어나 화장실 다녀온 뒤, 먹고 마시기 전, 운동 전에 잰 값끼리만 비교한다. 조건을
  모르면 인바디 수치는 비교하지 않고 값만 보여 준다. 밥 먹고 쟀다고 몇 kg 빼 주는 식의 보정은 하지
  않는다.
- 다른 기계로 잰 값은 비교하지 않는다. 내장지방 점수는 숫자로 말하지 않는다(011).
- 측정 주기 권장: 체중은 거의 매일 또는 주 3회 이상 아침에 재고 주간 평균으로 본다. 인바디는 2-4주에
  한 번, 같은 조건으로 잰다. 매주 재면 대부분 흔들림만 보게 된다. 이 주기도 연구가 정한 값이 아니라
  제품의 규칙이다.
- 목표 체중·체지방에 한 번 닿았으면 "거의 다 왔다, 다음 측정으로 확인"이라고 말하고, 흐름으로
  확인됐을 때 "달성"이라고 말한다.
