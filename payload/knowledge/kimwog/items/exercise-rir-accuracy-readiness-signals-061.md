---
# Fatigue-management sprint 2026-10-06 (dispatch kw-deload), second of two
# rows for the next-version adaptive daily program. This row owns the DAY: how good the
# RIR instrument is, how today's load is picked with it, and which readiness
# signals may move today's session. The WEEK (deloads) lives on
# exercise/deload-planned-vs-reactive-060. The method comparison
# (autoregulated vs percentage) and the RIR-resolution argument already live
# on exercise/autoregulation-vs-percentage-prescription-030 and are linked,
# not restated.
#
# v38 (2026-10-07, dispatch kw-consolidate-2): the set-level companion
# exercise/rir-set-log-accuracy-077 (kw-ex-rir-accuracy sprint) landed. The
# practice line below is scoped to the one study that tested it, matching the
# 030 re-audit; the rules and numbers are unchanged.
#
# rir_rules and readiness_signals are structured data for the adaptive daily
# layer. Values are directions plus product constants; each entry carries
# its own basis_grade. The YAML-subset reader returns numbers as strings.
id: exercise/rir-accuracy-readiness-signals-061
domain: exercise
grade: B (people misjudge reps-to-failure by about one rep, much worse in sets over 12 reps; subjective wellness tracks training load better than objective markers; sleep loss lowers performance); C (today's anchor-set performance as the primary readiness signal; RIR dose-response by goal; readiness-chosen session order); D (every threshold and adjustment size)
lane: "@performance-lit"
locale: universal
as_of: 2010-2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/34542869/"  # Halperin I, Malleron T, Har-Nir I, Androulakis-Korakakis P, Wolf M, Fisher J, Steele J 2022, Sports Med 52(2):377-390, doi 10.1007/s40279-021-01559-x -- scoping review + exploratory meta-analysis, 12 studies, n=414: reps-to-failure UNDER-predicted by 0.95 reps (95% CI 0.17-1.73), I2 97.9%; slightly more accurate closer to failure (beta -0.025) and in later sets (beta -0.07); sets of 12 reps or fewer beta 0.06 vs over 12 reps beta 0.47; training status no effect (beta -0.006); upper vs lower body no clear difference. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/38970765/"  # Robinson ZP, Pelland JC, Remmert JF, Refalo MC, Jukic I, Steele J, Zourdos MC 2024, Sports Med 54(9):2209-2231, doi 10.1007/s40279-024-02069-2 -- meta-regressions on ESTIMATED RIR: strength gains flat across a wide RIR range; hypertrophy increases as sets end closer to failure. Abstract read
  - "https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2018.00247/pdf"  # Helms ER et al. 2018, Front Physiol 9:247 -- RCT n=21 trained men, 8 weeks DUP: RPE-chosen vs %1RM loads, no significant 1RM difference (squat +17.05 vs +13.91 kg; bench +10.70 vs +9.64 kg); a "small squat advantage" comes from magnitude-based inference only
  - "https://pubmed.ncbi.nlm.nih.gov/28129275/"  # Colquhoun RJ et al. 2017, J Strength Cond Res 31(2):283-291, doi 10.1519/JSC.0000000000001500 -- RCT n=25 trained men, 9 weeks: lifters choosing the ORDER of the week's hypertrophy/power/strength sessions vs fixed order; no difference in 1RMs, total, FFM, motivation, session RPE or satisfaction
  - "https://pubmed.ncbi.nlm.nih.gov/20042923/"  # McNamara JM, Stearne DJ 2010, J Strength Cond Res 24(1):17-22, doi 10.1519/JSC.0b013e3181bc177b -- RCT n=16 beginners, 12 weeks: choosing which of the 10/15/20RM workouts to do each day by readiness; leg press +62 vs +16 kg, no difference in chest press or long jump
  - "https://pubmed.ncbi.nlm.nih.gov/26049792/"  # Zourdos MC et al. 2016, J Strength Cond Res 30(1):267-275 -- RIR-based RPE scale; RPE strongly and inversely related to bar velocity in experienced and novice squatters; experienced lifters rated a true 1RM closer to RPE 10
  - "https://sportgeneeskunde.com/wp-content/uploads/Meeusen-et-al-2013-Overtraining-Consensus-ECSS-ACSM.pdf"  # Meeusen R et al. 2013, Eur J Sport Sci 13(1):1-24 -- performance decrement is the defining feature of overreaching; no single physiological or psychological marker suffices. Cited from the record
  - "exercise/autoregulation-vs-percentage-prescription-030"  # within-warehouse: autoregulated ~ percentage for strength; RIR error 0.65-1.0 reps near failure, no improvement over 6 weeks in one study (Remmert 2023, n=9; re-audited v38); one rep ~3-4% of 1RM near 85%
  - "exercise/rir-set-log-accuracy-077"  # within-warehouse (v38): the SET-level companion -- how far a logged RIR can be trusted by set position, rep count and exercise type; refines read-near-the-target and experience-does-not-calibrate by rule name
  - "exercise/deload-planned-vs-reactive-060"  # within-warehouse partner: the week-level response to a repeated drop
  - "exercise/recovery-kinetics-session-spacing-025"  # within-warehouse: proximity to failure drives recovery cost
  - "exercise/doms-timeline-mechanism-023"  # within-warehouse: soreness is not a training instrument
  - "exercise/recovery-modality-soreness-vs-performance-024"  # within-warehouse: feeling and doing must be reported separately
  - "exercise/caution-severity-ladder-056"  # within-warehouse: pain goes to the caution ladder
  - "source:sleep-recovery/sleep-loss-performance-decrement-004"  # cross-domain: sleep loss lowers strength; early waking and PM sessions worst
  - "source:sleep-recovery/subjective-monitoring-vs-objective-markers-011"  # cross-domain: self-reported wellbeing tracks load better than objective markers; HRV and device readiness scores not validated for RT
  - "framework:GRADE -- the RIR-accuracy figure is a meta-analysis of small accuracy studies with very high heterogeneity, so the direction (about one rep, conservative on average) is firmer than the number. The readiness-signal ranking is assembled from a consensus definition (performance), a 56-study review (subjective wellbeing, via 011), a sleep meta-analysis (via 004) and the soreness rows (023/024); no trial tests a readiness-signal-driven daily program against a fixed one in lifters except the two small flexible-order RCTs. All thresholds are product constants."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
rir_rules:
  - rule: reported-rir-is-conservative
    value: on average lifters have about 1 more rep in them than they report
    engine: read reported RIR as-is; do not add a safety buffer on top; do not treat a single reported RIR as exact
    basis: Halperin 2022
    basis_grade: B
  - rule: high-rep-sets-unreliable
    value: rep-to-failure guesses are much worse in sets over 12 reps
    engine: anchor load decisions on sets of 12 reps or fewer; for sets over 12 reps progress by reps at a fixed load instead of by RIR
    basis: Halperin 2022
    basis_grade: B
  - rule: read-near-the-target
    value: guesses improve closer to failure and in later sets
    engine: take the readiness read at the end of the first working set of the anchor lift with a target RIR of 1-3, not from a warm-up or a set ended far from failure
    basis: Halperin 2022
    basis_grade: C
  - rule: experience-does-not-calibrate
    value: training status did not change accuracy; six weeks of practice did not improve it in one small study (Remmert 2023, n=9), while two studies with failure feedback found improvement (077)
    engine: apply the same error assumptions to experienced and new users; no calibration phase that promises better accuracy
    basis: Halperin 2022; 030 (Remmert 2023)
    basis_grade: B
  - rule: resolution
    value: about 1 rep of error, and one rep is about 3-4% of 1RM near 85%
    engine: change today's load only when the anchor set is 2 or more reps off target; a 1-rep miss is within the instrument's error (threshold is a product constant)
    basis: 030
    basis_grade: C
  - rule: adjustment-size
    value: about one load step (roughly 2.5-5% of the working load) per rep off target, at most two steps in one session
    engine: easier than target by 2 or more -> up one step for the remaining sets; harder by 2 or more -> down one step, or keep load and cut 1-2 back-off sets; never chase a missed rep with more sets (all product constants)
    basis: 030; Helms 2018
    basis_grade: D
  - rule: target-rir-by-goal
    value: strength gains are flat across a wide RIR range; hypertrophy rises as sets end closer to failure; failure work costs more recovery
    engine: defaults compound lifts RIR 1-3, isolation RIR 0-2, deload week RIR 3 or more; strength-focused users need not go near failure (product constants)
    basis: Robinson 2024; 025
    basis_grade: C
  - rule: method-is-not-a-dividend
    value: RPE/RIR-chosen loads and percentage loads give similar strength gains
    engine: use RIR to absorb day-to-day readiness, not as a promise of faster progress
    basis: 030; Helms 2018
    basis_grade: B
readiness_signals:
  - signal: anchor-set-performance
    role: primary
    read: first working set of the day's main lift at the planned load -- reps achieved and reported RIR, against target and the last comparable exposure
    low: 2 or more reps short of target, or RIR 2 or more below target
    action_low: down one load step or cut 1-2 back-off sets today; if repeated at the next exposure, hand to 060 performance-drop
    action_high: up one step for the remaining sets, within the plan's weekly progression cap
    basis_grade: C
  - signal: self-reported-wellness
    role: secondary
    read: one short daily check (fatigue, sleep quality, motivation, general muscle feel), scored against the user's own recent average
    low: clearly below the user's own recent average
    action_low: keep the session, cap effort at RIR 2 or more, drop the last set of each exercise, no max attempts; persistent low plus a performance drop goes to 060
    action_high: no change; good mood alone does not raise load
    basis_grade: B
  - signal: sleep-last-night
    role: secondary
    read: hours slept (measured if available) and whether the user woke earlier than usual
    low: 6 hours or less, worse if woken early or if the session is in the afternoon or evening
    action_low: no 1RM tests or heavy singles today; let the anchor set decide load; do not cancel the session for sleep alone
    action_high: no change
    basis_grade: B
  - signal: muscle-soreness
    role: none-for-load
    read: user words
    low: any level
    action_low: does not change load, sets or the deload clock; keep exercise selection familiar if a very sore muscle is trained again soon
    action_high: no change
    basis_grade: B
  - signal: joint-or-tendon-pain
    role: route
    read: user words naming a site
    low: any pain at a site
    action_low: hand the site to the caution ladder (056); the rest of the session runs on the other signals
    action_high: no change
    basis_grade: D
  - signal: device-readiness-score
    role: none
    read: wearable HRV or proprietary readiness number
    low: any value
    action_low: may be shown, never moves load; not validated against next-day lifting performance
    action_high: no change
    basis_grade: D
  - signal: session-order-swap
    role: option
    read: low wellness or sleep on a day that holds the week's heaviest session
    low: low readiness on a heavy day
    action_low: offer to swap today's session with a lighter one later in the same week, keeping the week's total unchanged
    action_high: no change
    basis_grade: C
refraction_notes:
  - note: >
      THE INSTRUMENT IS ABOUT ONE REP WIDE, AND IT ERRS ON THE SAFE SIDE.
      Across 12 studies and 414 people, lifters predicted about one fewer rep
      than they could actually do, with large spread between studies. So a
      reported "2 in the tank" usually means 2 to 3. The engine reads it
      as-is, does not pad it, and does not act on a one-rep difference.
    grade: B
  - note: >
      HIGH-REP SETS ARE WHERE THE GUESS BREAKS. Prediction error rose sharply
      in sets over 12 reps. For those sets, progress the reps at a fixed
      load; set today's load from a heavier anchor set.
    grade: B
  - note: >
      PERFORMANCE IS THE READINESS SIGNAL, THE REST ARE MODIFIERS. Only a
      performance drop defines overreaching (Meeusen 2013). Self-reported
      wellbeing is the best supporting signal (it tracks load better than
      blood or heart-rate markers, 011), short or early-ended sleep lowers
      strength (004), soreness tracks neither damage nor stimulus (023), and
      device readiness scores are unvalidated for lifting (011). The daily
      layer moves load on the anchor set; the other signals shape effort caps
      and set counts, never the load on their own.
    grade: C
  - note: >
      HOW CLOSE TO FAILURE DEPENDS ON THE GOAL. Strength gains looked flat
      across a wide RIR range, while muscle growth rose as sets ended closer
      to failure; the RIR in those analyses was estimated from study
      descriptions, so the shape is suggestive rather than precise. Failure
      work also costs more recovery (025). A strength-goal user loses little
      by stopping 2-3 reps short; a hypertrophy-goal user benefits from
      finishing isolation work near failure.
    grade: C
  - note: >
      LETTING THE DAY PICK THE SESSION IS SAFE, NOT A BOOSTER. Trained men
      who chose the order of their weekly sessions gained the same as a fixed
      order; beginners choosing their workout by readiness gained more on the
      leg press only. Swapping a heavy and a light day within the week is a
      reasonable low-readiness option, not a proven gain.
    grade: C
  - note: >
      EXPERIENCE DOES NOT FIX THE GAUGE. Training status did not change
      prediction accuracy. Practice is open: six weeks did not improve it in
      one small study (030), and two studies with failure feedback found
      improvement (077), so no calibration phase is promised. With
      training_status unknown, the same rules apply; there is no separate
      novice table.
    grade: B
claim: >
  The daily layer can pick today's load from repetitions in reserve, but it
  must respect the instrument's width. Lifters misjudge reps-to-failure by
  about one rep on average -- and on the conservative side, predicting
  fewer than they can do -- with accuracy improving near failure and in
  later sets, collapsing in sets over 12 reps, and not improving with
  training experience (practice is open: one null, two positive studies).
  RIR- or RPE-chosen loads give similar
  strength gains to percentage loads, so autoregulation absorbs day-to-day
  variation rather than speeding progress. Among readiness signals, only
  performance defines overreaching, so the anchor lift's first working set
  (reps and RIR at the planned load) is the primary signal; self-reported
  wellbeing and last night's sleep are supporting modifiers that cap effort
  and trim sets; soreness and device readiness scores do not move load; pain
  goes to the caution ladder. How close to failure to train depends on the
  goal: strength gains look flat across a wide RIR range while hypertrophy
  rises nearer failure. Letting a low-readiness day swap sessions within the
  week is safe but unproven as a gain. Every threshold (2-rep trigger, one
  load step per rep, the 12-rep cut-off as an engine rule, default RIR
  bands) is a product constant.
reasoning: >
  Halperin 2022 is the only pooled estimate of RIR accuracy; its very high
  heterogeneity is why the direction and the moderators carry more weight
  than the 0.95 figure. Its moderators map directly onto engine choices:
  read near the target, read on a set of 12 reps or fewer, expect no
  calibration from experience (which also matches Remmert 2023 on 030). The
  2-rep action threshold follows from an instrument about one rep wide. The
  outcome side of autoregulation is already graded on 030 (similar strength
  to percentage loading) and Helms 2018 adds a small trained RCT in the
  same direction; its small squat advantage comes from magnitude-based
  inference and is not carried. Robinson 2024 supplies the goal split for
  RIR targets, held at C because the RIR values were estimated. The
  readiness ranking puts performance first because the consensus definition
  of overreaching is a performance decrement (Meeusen 2013) and because it
  is the thing the session is trying to protect; the supporting signals are
  graded on their own rows (011, 004, 023, 024). Colquhoun 2017 and
  McNamara 2010 are the only trials of letting readiness choose the session,
  small and mixed, hence C and an offer rather than a rule. Sleep and
  training status are soft hedges: neither changes the rules, only the
  wording and the sleep modifier.
---

# exercise/rir-accuracy-readiness-signals-061 -- 오늘 무게는 어떻게 정하나: RIR의 정확도와 컨디션 신호

**한 줄 그림:** "몇 개 더 할 수 있었나(RIR)"는 한 개쯤 틀리는 눈금이다. 오늘 무게는 주 운동 첫 세트가
목표보다 2개 이상 쉽거나 힘들 때만 바꾸고, 잠·피로감은 세트 수와 강도 상한만 조절한다. 근육통과
스마트워치 준비도 점수로는 무게를 바꾸지 않는다.

## RIR rules (engine-readable)

| Rule | Engine |
|---|---|
| reported RIR runs about 1 rep conservative | read as-is, no extra buffer, no action on a 1-rep miss |
| sets over 12 reps | progress by reps at fixed load; anchor load on 12 reps or fewer |
| read near target | end of first working set of the anchor lift, target RIR 1-3 |
| experience | same error assumptions for everyone |
| adjust | 2+ reps off target -> one load step (about 2.5-5%), max two steps a session |
| target RIR | compounds 1-3, isolation 0-2, deload week 3+ |

## Readiness signals

| Signal | Role | When low |
|---|---|---|
| anchor-set performance | primary | down one step or cut 1-2 back-off sets; repeated -> 060 |
| self-reported wellness | secondary | effort cap RIR 2+, drop last set per exercise, no max attempts |
| sleep last night (6 h or less, early wake) | secondary | no max tests; anchor set decides load; don't cancel |
| muscle soreness | none for load | no change (023) |
| joint or tendon pain | route | caution ladder (056) |
| device readiness / HRV | none | show only |
| low readiness on the week's heavy day | option | offer to swap with a lighter day this week |

Thresholds and step sizes are the plan's rules, not measured cut-offs.

## 한국어 요약 (답변용)

- 사람들은 "몇 개 더 할 수 있었나"를 평균 한 개 정도 틀리고, 대개 실제보다 적게 말한다(12개 연구,
  414명). 그래서 "2개 남았다"는 보통 2~3개다. 이 숫자에 안전 여유를 더 얹지 않고, 한 개 차이로는
  무게를 바꾸지 않는다.
- 12회가 넘는 고반복 세트에서는 이 추정이 크게 틀린다. 고반복 세트는 같은 무게로 반복 수를 늘려 가고,
  오늘 무게는 12회 이하인 주 운동 세트로 정한다.
- 경력이 길다고 이 눈금이 정확해지지 않았다. 연습 효과는 갈린다(6주 연습이 효과 없던 작은 연구 하나, 실패 지점
  피드백으로 나아진 연구 둘). 초보와 경력자에게 같은 규칙을 쓴다.
- 오늘 무게 조정: 주 운동 첫 세트가 목표보다 2개 이상 쉬우면 남은 세트를 한 단계 올리고, 2개 이상
  힘들면 한 단계 내리거나 무게는 두고 마지막 1~2세트를 뺀다. 한 단계는 대략 무게의 2.5~5%이고, 한
  번에 두 단계까지. 이 숫자들은 제품이 정한 규칙이다.
- 컨디션 신호의 순서: 기록(첫 세트)이 가장 중요하다. 과훈련 전 단계를 정의하는 것도 기록 하락이다.
  스스로 느끼는 피로·의욕·수면의 질은 그다음이고, 낮으면 세트를 줄이고 실패 2회 전에서 멈추며
  최대 무게 시도는 하지 않는다. 6시간 이하로 잤거나 평소보다 일찍 깼으면 최대 무게 테스트만
  미루고, 운동 자체는 취소하지 않는다.
- 근육통은 무게나 디로드 판단에 쓰지 않는다. 근육통은 손상이나 자극의 크기를 잘 반영하지 않는다.
  스마트워치 준비도·HRV 점수는 보여 줄 수는 있지만 근력운동에서 검증되지 않아 무게를 바꾸지 않는다.
  관절·힘줄 통증은 부상 주의 단계(056)로 보낸다.
- 실패에 얼마나 가까이 갈지는 목표에 따라 다르다. 근력은 실패 몇 회 전에서 멈춰도 비슷하게 늘었고,
  근육 크기는 실패에 가까울수록 더 늘었다. 기본값은 다관절 운동 실패 1~3회 전, 단관절 운동 0~2회
  전이다.
- 컨디션이 안 좋은 날 그 주의 가장 무거운 운동이 잡혀 있으면, 같은 주 가벼운 날과 바꾸자고 제안할 수
  있다. 손해는 없었지만 더 좋아진다는 근거는 약하다.
- RIR이나 체감 강도로 무게를 고르는 방식은 퍼센트 방식과 근력 증가가 비슷했다. 그날 컨디션 차이를
  흡수하는 도구이지, 더 빨리 늘게 해 주는 방법은 아니다.
