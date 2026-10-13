---
# Injury-caution sprint (directive: caution depends on the injury's severity,
# site and type). The engine-readable synthesis of 054
# (history, recency, tissue) and 055 (present tendon / fascia pain). It is a
# routing rule, not a primary finding: each rung names the graded row it rests
# on, and every product constant (score weights, the 12-month boundary) is
# labelled as a constant. Same posture as 031 and 032.
#
# decision_ladder and tissue_modifiers are structured data for the split /
# caution code (see docs/kimwog-caution-ladder-fields.md). Values are
# DIRECTIONS and ORDERINGS; the numeric site_weight is a product score weight,
# never a load in kilograms and never a risk figure.
id: exercise/caution-severity-ladder-056
domain: exercise
grade: D (synthesis rule over 054 and 055; the ordering is C-backed, every constant is product judgement)
lane: "@clinical-physio"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/injury-history-reinjury-risk-054"  # history > none, recent > old, never zero; tissue shapes the time course
  - "exercise/tendon-fascia-load-management-055"  # present tendon / fascia pain: monitored loading, pain ceiling, spacing
  - "exercise/harm-route-boundary-031"  # red-flag pain is routed, not coached through
  - "exercise/ideal-healthy-lean-injury-free-045"  # strength training as the injury lever
  - "exercise/knee-pain-symptom-guided-loading-057"  # knee joint / patellofemoral pain: the joint-cartilage exception (added v37)
  - "owner directive 2026-10-06 17:50 (dispatch task kimwog-injury-caution): caution weight must depend on severity, site and tissue, grounded in graded knowledge"
  - "framework:GRADE -- the ORDER of the rungs (none < mild < old history < recent history < current pain) is supported by observational cohorts (054); the tendon/fascia exception to avoid-on-current-pain is supported by small RCTs (055); the specific weights, the 12-month boundary and the exposure-day caps are product constants with no direct evidence."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
decision_ladder:
  - level: mild
    words: occasional stiffness or tightness, managed, no pain that limits training, no named past injury
    site_weight: 0
    prep: true
    spread_load: false
    exposure_days: unchanged
    exclude_grades: []
    route: none
    basis: exercise/ideal-healthy-lean-injury-free-045
    basis_grade: D
  - level: history-old
    words: a named past injury at the site, recovered, more than the product window ago
    site_weight: 1
    prep: true
    spread_load: false
    exposure_days: unchanged
    exclude_grades: []
    route: none
    basis: exercise/injury-history-reinjury-risk-054
    basis_grade: C
  - level: history-recent
    words: a named past injury at the site within the product window (12 months, a convention)
    site_weight: 2
    prep: true
    spread_load: true
    exposure_days: unchanged
    exclude_grades: [high]
    route: none
    basis: exercise/injury-history-reinjury-risk-054
    basis_grade: C
  - level: history-unknown
    words: a named past injury, timing not given after one ask
    site_weight: 2
    prep: true
    spread_load: true
    exposure_days: unchanged
    exclude_grades: [high]
    route: none
    basis: exercise/injury-history-reinjury-risk-054
    basis_grade: D
  - level: current-load-pain
    words: present, familiar, activity-related ache at a tendon or the plantar fascia; no red flag; pain-triage has not flagged it
    site_weight: 2
    prep: true
    spread_load: true
    exposure_days: no consecutive heavy days at the site
    exclude_grades: [high]
    route: pain-monitoring rule (055)
    basis: exercise/tendon-fascia-load-management-055
    basis_grade: B
  - level: current-other
    words: present pain at a joint, ligament or muscle, or any pain whose tissue is unknown
    site_weight: 2
    prep: false
    spread_load: false
    exposure_days: reduce until triaged
    exclude_grades: [low, medium, high]
    route: pain-triage before split selection
    basis: exercise/harm-route-boundary-031
    basis_grade: D
  - level: red-flag
    words: new trauma, swelling, locking, giving way, night pain, numbness or weakness, sharp or rising pain
    site_weight: 2
    prep: false
    spread_load: false
    exposure_days: none at the site
    exclude_grades: [low, medium, high]
    route: pain-triage; refer
    basis: exercise/harm-route-boundary-031
    basis_grade: D
tissue_modifiers:
  - tissue: tendon
    effect: present familiar ache moves current-other to current-load-pain when pain-triage has not flagged it; space heavy site days by at least one day
    basis_grade: B
  - tissue: fascia
    effect: same as tendon (plantar fascia); heavy slow heel raises are the loading, not a hazard
    basis_grade: B
  - tissue: muscle
    effect: recurrence risk concentrated after return in the same season; recent history weighs as history-recent; a new strain is current-other
    basis_grade: C
  - tissue: ligament
    effect: reconstructed or repeatedly sprained ligament keeps history weight longer; add balance and strength work at the site; instability or giving way is red-flag
    basis_grade: C
  - tissue: joint-cartilage
    effect: stiffness without pain is mild; present joint pain is current-other, EXCEPT the knee when the user's words fit the patellofemoral picture or a clinician has named knee osteoarthritis -> knee variant of current-load-pain under the 057 ceiling (2/10 during, after and next day) with 058 range and variant swaps; other joints have no graded loading row yet (GAPS.md)
    basis_grade: C
refraction_notes:
  - note: >
      THE ORDER IS THE EVIDENCE, THE NUMBERS ARE NOT. That a recent injury
      weighs more than an old one, and an old one more than none, is
      supported by cohorts (054). The site weights 0 / 1 / 2, the 12-month
      window and the "no consecutive heavy days" cap are product constants.
      Speak them as the plan's rule, never as a measured threshold.
    grade: D
  - note: >
      CURRENT PAIN IS TWO RUNGS, NOT ONE. A familiar tendon or plantar-fascia
      ache that triage has not flagged keeps loading under the 055 ceiling
      (pain up to about 5/10, settled by next morning, not rising week to
      week). Only joint / ligament / muscle pain, unknown-tissue pain, or a
      red flag closes the site's loading pending triage. Collapsing both into
      avoid-everything throws away the loading that treats the tendon.
    grade: B
  - note: >
      SPREAD BEFORE YOU CUT. For a recent history or a loaded tendon, the
      first lever is how the site's work is distributed (spread across the
      week, no heavy back-to-back days) and prepared; removing exposure days
      is reserved for the rungs that go to triage. Spreading is supported by
      tendon turnover timing and protocol design, not by a head-to-head trial
      in lifters (GAPS.md).
    grade: D
  - note: >
      ADD, DON'T ONLY SUBTRACT. Every rung below current-other adds prep and
      site-specific strengthening, because residual deficit is the proposed
      mechanism for re-injury and strength training cuts injury.
    grade: C
  - note: >
      SIDE AND SITE COME FROM THE USER'S WORDS. The ladder decides how much a
      site weighs; it never invents which site, which side, the tissue, or a
      date. Tissue unknown -> treat present pain as current-other until the
      user or triage names it.
    grade: D
claim: >
  How much a caution site should weigh in a split follows a ladder of seven
  rungs: mild (stiffness, managed) -> prep only, no score weight; old history
  -> prep plus a small weight; recent or undated history -> prep, higher
  weight, spread the site's load, drop the highest-load variants; present
  familiar tendon or plantar-fascia ache without red flags -> keep loading
  under the pain-monitoring ceiling, spread the site's heavy days, drop the
  highest-load variants; present joint, ligament, muscle or unknown-tissue
  pain -> close the site's loading and route to pain-triage before choosing a
  split; red flags -> triage and refer. Tissue shifts the rung (tendon and
  fascia stay loadable when present pain is familiar; ligament instability is
  a red flag; muscle recurrence clusters after return). The ordering of the
  rungs is evidence-backed; the weights, window and day caps are product
  constants.
reasoning: >
  The rungs come straight from the two graded rows. 054 supplies the history
  ordering (none < old < recent) and the never-zero rule, which is why the old
  history rung keeps a weight, while mild stiffness without a named injury
  carries prep only. 055 supplies the split of present pain: tendon and plantar
  fascia are treated by monitored loading, so for them "current" means keep
  loading with a ceiling, while every other present pain keeps today's
  avoid-and-triage behaviour under 031. The spread-before-cut note uses 055's
  spacing rationale. The axis is hard with block_specifics: without the user's
  words on severity and tissue, the specific rung is not asserted and the one
  merged ask applies.
---

# exercise/caution-severity-ladder-056 -- 부상 정도·시기·조직에 따른 주의 단계

**한 줄 그림:** 부상은 하나로 뭉뚱그리지 않는다. 가벼운 뻣뻣함, 오래된 부상, 최근 부상, 지금 아픈
힘줄, 지금 아픈 관절, 위험 신호를 각각 다르게 다룬다.

## The ladder

| Rung | Site weight (product) | Prep | Spread site load | Drop variants | Route |
|---|---:|---|---|---|---|
| mild | 0 | yes | no | none | -- |
| history-old | 1 | yes | no | none | -- |
| history-recent | 2 | yes | yes | high | -- |
| history-unknown | 2 | yes | yes | high | -- |
| current-load-pain (tendon / fascia, no red flag) | 2 | yes | yes, no heavy back-to-back days | high | 055 pain ceiling |
| current-other (joint / ligament / muscle / unknown) | 2 | no | -- | all | pain-triage first |
| red-flag | 2 | no | -- | all | pain-triage; refer |

The order is evidence-backed (054, 055). The weights, the 12-month window and
the day cap are product constants.

## 한국어 요약 (답변용)

- 가끔 뻣뻣한 정도로 관리되고 있으면 준비 운동만 더하고 분할 점수에는 반영하지 않는다.
- 예전에 다쳤다가 나은 부위(제품 기준 12개월 이전)는 준비 운동과 함께 작은 가중치를 둔다. 오래돼도
  0으로 치지 않는다.
- 최근(12개월 안) 다쳤거나 언제 다쳤는지 모르면 가중치를 높이고, 그 부위 운동을 주 안에 나누고,
  가장 무거운 변형은 뺀다.
- 지금 아픈데 그게 힘줄이나 족저근막의 익숙한 통증이고 위험 신호가 없으면, 쉬지 않고 통증 기준(운동
  중·후 10점 중 5점까지, 다음 날 아침 회복, 주마다 늘지 않음)을 지키며 계속 부하를 준다. 무거운 날은
  이어 붙이지 않는다.
- 지금 아픈 곳이 관절·인대·근육이거나 어디가 아픈지 모르면, 그 부위 부하를 닫고 분할을 고르기 전에
  통증 확인으로 보낸다.
- 새로 다침, 붓기, 잠김, 빠지는 느낌, 밤 통증, 저림·힘 빠짐, 날카롭거나 심해지는 통증은 위험
  신호다. 통증 확인 후 진료를 권한다.
- 단계의 순서는 연구로 뒷받침되지만, 가중치 숫자·12개월 경계·연속일 제한은 제품이 정한 규칙이다.
  답할 때도 그렇게 말한다.
