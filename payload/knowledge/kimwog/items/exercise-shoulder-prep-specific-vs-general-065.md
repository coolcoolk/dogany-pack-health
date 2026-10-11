---
# Shoulder sprint 2026-10-06 (dispatch kw-shoulder-warmup). The prep half of
# the shoulder question, companion to 064 (selection + cuff work). The health
# pack is moving toward a MACHINE-FIRST prep policy: prep for a pressing day is
# light ramp sets on the first machine, plus a short cuff / scapular primer
# (cable or band external rotation, halo, face pull) only where the shoulder
# carries a caution rung. This row says what the evidence supports for each
# piece and what is product judgement. It extends 022 (general warm-up and
# same-day performance) and 018 (load ramp-up) to the shoulder.
#
# prep_policy is structured data for the prep code, same posture as 056's
# decision_ladder: each component names its rung trigger, its basis and its own
# grade. Doses marked "product constant" are not measured thresholds.
id: exercise/shoulder-prep-specific-vs-general-065
domain: exercise
grade: B (upper-body warm-up raises same-day strength and power; specific, near-load warm-up sets carry most of the resistance-exercise effect); C (shoulder-specific prep programmes cut shoulder problems -- shown in overhead-throwing handball players only, indirect for lifters); D (any specific activation drill -- band or cable external rotation, halo, face pull, machine activation -- before pressing, for injury or performance; no trial located)
lane: "@performance-lit"
locale: universal
as_of: 2015-2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/25694615/"  # McCrary JM, Ackermann BJ, Halaki M 2015, Br J Sports Med 49(14):935 -- systematic review, 31 RCTs (21 good quality, PEDro): strong evidence that high-load dynamic warm-ups enhance upper-body strength and power; short static stretching no effect on power; passive heating largely ineffective; NO study of upper-body warm-up on injury prevention found
  - "https://revistas.rcaap.pt/motricidade/article/view/21143"  # Ribeiro B, Pereira A, Neves P, Marinho D, Marques M, Neiva HP 2021, Motricidade 17(1), doi 10.6063/motricidade.21143 -- systematic review, 11 studies: maximal strength and repetitions benefit when a specific warm-up is done at loads close to the working load; adding a general component before it is not consistently better
  - "https://bjsm.bmj.com/content/51/14/1073"  # Andersson SH, Bahr R, Clarsen B, Myklebust G 2017, Br J Sports Med 51(14):1073 -- cluster RCT, 45 elite handball teams, 660 players, one season: OSTRC shoulder programme (internal-rotation ROM, external-rotation and scapular strength with elastic bands, kinetic chain, thoracic mobility) as part of warm-up 3x/week; average shoulder-problem prevalence 17% (95% CI 16 to 19) vs 23% (21 to 26)
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC9283550/"  # Asker M, Hägglund M, Waldén M, Källberg H, Skillgate E 2022, Sports Med Open 8, doi 10.1186/s40798-022-00478-z -- three-armed cluster RCT, 627 adolescent elite handball players: Shoulder Control (five exercises, four levels, 10-15 min, used as warm-up) HR 0.44 (95% CI 0.29 to 0.68) for shoulder injury, NNT 9, despite mean use 1.3x/week against a prescribed 3x
  - "https://pubmed.ncbi.nlm.nih.gov/24077379/"  # Kolber MJ et al. 2014, J Strength Cond Res 28(4):1081-1089 -- recreational weight trainers: external-rotator strengthening inversely associated with impingement signs (cross-sectional, read at abstract; also in 064)
  - "exercise/dynamic-warmup-same-day-performance-022"  # within-warehouse: the whole warm-up carries the effect; stretching modality inside it is close to interchangeable
  - "exercise/warmup-load-rampup-progression-018"  # within-warehouse: the load ramp that IS the specific warm-up
  - "exercise/prep-on-fatigued-muscle-two-effects-026"  # within-warehouse: prep helps the session, does not speed recovery
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: "activation" measured by EMG is not an outcome
  - "exercise/serratus-anterior-integration-019"  # within-warehouse: scapular drills as a pre-set cue (practitioner)
  - "exercise/shoulder-pressing-selection-cuff-work-064"  # within-warehouse: the cuff STRENGTH dose belongs in the work block
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the rung that switches the shoulder primer on
  - "framework:GRADE -- the performance effect of upper-body warm-up rests on a systematic review of RCTs with mostly good-quality trials; the specific-near-load point on a small review of 11 acute studies. The injury effect of shoulder prep rests on two cluster RCTs in handball, consistent in direction, but in overhead throwers with a throwing load lifters do not have, and with multi-component programmes that cannot isolate any single drill. No trial of any isolated activation drill before pressing, in lifters, for injury or performance was located."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
prep_policy:
  - component: specific-ramp-on-first-press
    applies_at: [all]
    action: 2-3 light-to-moderate ramp sets on the first pressing exercise (machine or bar), climbing toward the working load, well short of failure
    dose_status: ramp shape from 018 (practitioner); set count is a product constant
    basis: McCrary 2015; Ribeiro 2021; exercise/warmup-load-rampup-progression-018
    basis_grade: B
  - component: general-pulse-raiser
    applies_at: [all]
    action: optional few minutes of general movement; keep if the user likes it or the room is cold, never at the expense of the specific ramp
    dose_status: product constant
    basis: Ribeiro 2021; exercise/dynamic-warmup-same-day-performance-022
    basis_grade: C
  - component: shoulder-primer
    applies_at: [history-old, history-recent, history-unknown, current-load-pain]
    action: 1-2 light sets of external rotation (cable, band or machine -- interchangeable) and one scapular drill (face pull, band pull-apart or serratus wall slide), sub-fatiguing
    dose_status: product constant; drill choice is preference, no drill is evidenced over another
    basis: Andersson 2017; Asker 2022 (handball, multi-component, indirect)
    basis_grade: C
  - component: shoulder-primer-default-off
    applies_at: [no-rung, mild]
    action: no dedicated cuff primer for a shoulder with no caution rung; the ramp sets are the shoulder prep
    dose_status: product judgement
    basis: McCrary 2015 (no injury data for upper-body warm-up); no lifter trial
    basis_grade: D
  - component: cuff-strength-not-in-prep
    applies_at: [history-old, history-recent, history-unknown, current-load-pain]
    action: progressive external-rotation strengthening lives in the work block (064); the prep primer is not a substitute for it
    dose_status: direction only
    basis: exercise/shoulder-pressing-selection-cuff-work-064
    basis_grade: B
  - component: no-cuff-fatigue-before-pressing
    applies_at: [all]
    action: do not take cuff or scapular drills near failure before heavy pressing; hard cuff sets go after the pressing or on another day
    dose_status: product judgement, untested
    basis: no trial; exercise/prep-on-fatigued-muscle-two-effects-026
    basis_grade: D
refraction_notes:
  - note: >
      THE WARM-UP THAT IS PROVEN IS THE LIFT ITSELF, LIGHTER. Across trials,
      high-load dynamic warm-ups raised upper-body strength and power, and in
      resistance exercise the gain came from specific sets at loads close to
      the working load; a general component added in front was not
      consistently better. For a machine-first plan this means the first
      press machine's ramp sets are the core of shoulder prep for everyone.
    grade: B
  - note: >
      SHOULDER PREP PROGRAMMES PREVENT PROBLEMS -- IN THROWERS. Two cluster
      trials in handball found that a 10-15 minute shoulder programme used
      as the warm-up (external-rotation and scapular strengthening with
      bands, internal-rotation range, thoracic and kinetic-chain work)
      lowered shoulder problems (17% vs 23% prevalence; injury hazard less
      than half), even when done about once a week. These are overhead
      throwers, and the programmes are packages, so the result transfers to a
      pressing lifter as a direction only. It supports switching a short
      cuff / scapular primer ON for a shoulder that carries a caution rung.
    grade: C
  - note: >
      NO SINGLE ACTIVATION DRILL HAS EVIDENCE. No trial was located that
      tests band or cable external rotation, halo, face pull or machine
      "activation" before pressing, for injury or for performance, in
      lifters. "It activates the cuff" is an EMG statement, and EMG
      recruitment is not an outcome (013). The drills are interchangeable
      choices inside a primer; pick by equipment and preference, and never
      present one as protective.
    grade: D
  - note: >
      PRIMER, NOT STRENGTH WORK; SUB-FATIGUING. The handball programmes were
      progressive strength work three times a week. A two-set light primer
      is not that dose. The strengthening that showed effect in shoulder pain
      (064) belongs in the work block and progresses; the primer stays light
      so it does not tire the stabilisers before heavy pressing. The
      fatigue caution is reasoning, not a measured effect.
    grade: D
claim: >
  For a pressing lifter, the best-supported shoulder prep is specific: a few
  ramp sets of the first pressing exercise climbing toward the working load.
  Upper-body warm-ups of this kind raise strength and power across randomised
  trials, and in resistance exercise the benefit comes from specific sets near
  the working load; adding a general warm-up in front is not consistently
  better. No study of upper-body warm-up has measured injury in lifters. In
  overhead-throwing athletes, a 10-15 minute shoulder programme used as the
  warm-up (external-rotation and scapular strengthening, rotation range,
  thoracic work) reduced shoulder problems in two cluster trials, so a short
  cuff / scapular primer is a reasonable addition when the shoulder carries a
  caution rung -- a direction transferred from throwers, not a lifter finding.
  No individual drill (band or cable external rotation, halo, face pull, machine
  activation) has been tested before pressing; they are interchangeable
  choices. Keep the primer light and sub-fatiguing, and put the progressive
  cuff strengthening that treats shoulder pain in the work block (064).
reasoning: >
  McCrary 2015 is a systematic review of randomised trials with mostly
  good-quality studies and is the direct evidence for upper-body warm-up and
  performance; its explicit finding of no injury-prevention studies is why the
  default-off rule for a caution-free shoulder is D rather than "prep protects".
  Ribeiro 2021 is smaller and narrative but consistent with 018 and 022: the
  specific near-load ramp carries the effect. Andersson 2017 and Asker 2022 are
  well-run cluster trials pointing the same way, but in handball, with a
  throwing load and multi-component packages; they ground the shoulder primer
  as a C-level direction for caution rungs and cannot rank drills. Kolber 2014
  adds the cross-sectional lifter association with external-rotator training.
  Nothing located isolates any activation drill, so drill choice and doses are
  product constants. injury_history is soft with hedge here (unlike 064): the
  specific ramp applies to everyone, and the axis only switches the primer on,
  which is low-cost if the rung is wrong.
---

# exercise/shoulder-prep-specific-vs-general-065 -- 프레스 전 어깨 준비운동: 특정 드릴 vs 일반 워밍업

**한 줄 그림:** 어깨 준비의 핵심은 첫 프레스 종목을 가볍게 몇 세트 올려 가는 것이다. 어깨에 주의
단계가 있을 때만 가벼운 외회전·견갑 드릴을 더한다. 어떤 드릴이 낫다는 근거는 없다.

## Prep policy (engine-readable)

| Component | Fires at rung (056) | Action | Basis |
|---|---|---|---|
| specific-ramp-on-first-press | all | 2-3 ramp sets toward working load on the first press | McCrary 2015, Ribeiro 2021, 018 |
| general-pulse-raiser | all | optional, never instead of the ramp | Ribeiro 2021, 022 |
| shoulder-primer | history-old .. current-load-pain | 1-2 light sets ER (cable / band / machine) + one scapular drill | Andersson 2017, Asker 2022 (indirect) |
| shoulder-primer-default-off | no rung, mild | ramp sets are the shoulder prep | no injury data |
| cuff-strength-not-in-prep | history-old .. current-load-pain | progressive ER lives in the work block | 064 |
| no-cuff-fatigue-before-pressing | all | cuff drills sub-fatiguing before heavy pressing | reasoning only |

Set counts and the primer dose are product constants, not measured thresholds.

## 한국어 요약 (답변용)

- 근거가 가장 탄탄한 어깨 준비운동은 그날 할 미는 종목 자체를 가볍게 하는 것이다. 첫 프레스
  머신(또는 바벨)으로 2-3세트, 본 무게 쪽으로 올려 가되 지칠 때까지 하지 않는다. 상체 워밍업은
  근력·파워를 올렸고, 근력 운동에서는 본 무게에 가까운 특정 워밍업 세트가 효과를 냈다. 앞에 일반
  워밍업을 붙인다고 항상 더 나아지지는 않았다.
- 상체 워밍업이 부상을 줄이는지 본 연구는 없었다. 그래서 어깨에 문제가 없는 사람에게는 따로
  회전근개 드릴을 넣지 않고, 워밍업 세트가 곧 어깨 준비다.
- 핸드볼 선수 연구 두 건에서 10-15분짜리 어깨 프로그램(밴드 외회전·견갑 근력, 회전 가동범위,
  흉추 운동)을 워밍업으로 하니 어깨 문제가 줄었다. 던지는 선수 대상이고 여러 운동을 묶은
  프로그램이라, 헬스 하는 사람에게는 방향만 가져온다. 다친 적이 있거나 지금 익숙한 통증이 있는 어깨면
  가벼운 외회전 1-2세트와 견갑 드릴 하나를 더한다.
- 밴드·케이블 외회전, 헤일로, 페이스풀, 머신 "활성화" 중 어떤 게 더 낫다는 연구는 없다. 근전도로
  "많이 쓰인다"는 건 효과의 증거가 아니다. 있는 장비와 취향으로 고른다.
- 준비 드릴은 가볍게만 한다. 어깨 통증에 효과를 보인 건 무게를 올려 가는 외회전 근력 운동이고,
  그건 본운동 안에 넣는다. 무거운 프레스 전에 회전근개를 지치게 하지 않는다. 이건 연구 결과가
  아니라 추론이다.
