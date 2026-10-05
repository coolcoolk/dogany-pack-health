---
# Body-ideal archetype sprint 2026-09-30. "운동선수 같은 몸 / 역도 / 폭발력"
# -- the power ideal. Grouped: Olympic weightlifting as the sport and
# "athletic power" as the goal people name, because they share the defining
# feature (rate of force development) and the measurement gap.
id: exercise/ideal-weightlifting-athletic-power-041
domain: exercise
grade: A (rule -- federation lift definitions); B (injury epidemiology); C (weightlifting vs plyometric transfer)
lane: "@performance-lit"
locale: universal
as_of: 2017-2025
contested: no
sources:
  - "https://iwf.sport/wp-content/uploads/downloads/2020/01/IWF_TCRR_2020.pdf"  # IWF Technical and Competition Rules & Regulations: two lifts, snatch and clean & jerk, two hands, three attempts each, total by body-weight category (2025 edition on iwf.sport)
  - "https://pubmed.ncbi.nlm.nih.gov/27707741/"  # Aasa U et al. Br J Sports Med 2017 -- weightlifting 2.4-3.3 injuries/1000 h; spine, shoulder, knee
  - "https://pubmed.ncbi.nlm.nih.gov/41409563/"  # Wang S et al. Front Physiol 2025 -- network meta-analysis, 17 studies: weightlifting training ranked best for sprint, plyometrics for countermovement jump, traditional training for max strength (no significant pairwise differences)
  - "https://pubmed.ncbi.nlm.nih.gov/32698335/"  # Mangine 2020 -- rate of force development among predictors of mixed-modal performance
  - "https://pubmed.ncbi.nlm.nih.gov/34757594/"  # Schumann M et al. Sports Med 2022 -- 43 studies: concurrent aerobic + strength training does not blunt hypertrophy (SMD -0.01) or max strength (-0.06) but attenuates explosive strength (-0.28), more so in the same session
  - "exercise/ideal-crossfit-functional-036"
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      POWER IS SPEED UNDER LOAD, AND THIS PRODUCT CANNOT SEE SPEED. There is
      no bar-velocity, jump-height or sprint-time token. The kit's e1RM of a
      clean or snatch tracks strength in the lift, not power. Say so, and
      offer the `power` practice pick as the training lever rather than a
      number the product cannot read.
    grade: D
  - note: >
      THE FULL LIFTS ARE TECHNICAL; THE DERIVATIVES ARE THE USUAL ROUTE. For a
      non-competitor who wants athletic power, jumps, kettlebell swings, med
      ball throws and pulls from the hang deliver the stimulus with less
      technical demand. Ranking among weightlifting, plyometric and strength
      training for jump/sprint is uncertain (no significant pairwise
      differences).
    grade: C
claim: >
  The weightlifting / athletic-power ideal is the ability to produce force
  fast: the snatch and clean & jerk in sport, and jumping, sprinting and
  explosive change of direction as the everyday "athletic" version. The body
  is compact and muscular through legs, hips and back, typically not very
  lean-focused, with high mobility in the ankles, hips and overhead position.
  It is distinguished from powerlifting by speed (maximal power rather than
  maximal slow force) and from CrossFit by specialisation. Injury incidence is
  2.4-3.3 per 1000 training hours.
reasoning: >
  The sport definition is the IWF's. Incidence from Aasa 2017. The transfer
  evidence (weightlifting best for sprint, plyometrics for jump, no significant
  pairwise differences) is a single recent network meta-analysis of small
  trials, graded C.
---

# exercise/ideal-weightlifting-athletic-power-041 -- 역도 / 운동선수형 폭발력

**한 줄 그림:** 바닥에서 머리 위까지 한 번에 폭발하듯 들어올리고, 높이 뛰고 빠르게 튀어나가는
탄력 있는 몸.

## Distinguishing features

Rate of force development; speed-strength; technical full-body lifts; overhead
and deep-squat mobility.

## Measurable here

- `e1rm_<power_clean>` / `e1rm_<snatch>` if logged as lead lift (strength in
  the lift, not power).
- `e1rm_<squat>` -- base strength.
- `body_weight`, `skeletal_muscle_kg` -- secondary.
- Practice pick `power` (3 x 3-5 explosive, full rest) -- the program lever.

## Not measurable here

Bar velocity, jump height, sprint time, reactive strength. Proposed tokens:
`jump_cm`, `sprint_s_<distance>`. None exists.

## Training emphasis and practice

Low-rep explosive work with full rest, heavy squats and pulls, jump and throw
derivatives, mobility for overhead/deep-squat positions. `power` pick fits
directly; keep it before fatiguing work.

## Failure modes

Lumbar and knee from poor catch positions; wrist/elbow in the rack or overhead;
landing load on cautioned knees/ankles (the kit already swaps to swings then).

## Combines / conflicts

Combines with powerlifting and CrossFit; conflicts mildly with endurance volume
(explosive strength is the one capacity concurrent training measurably blunts,
SMD -0.28, worse when both share a session -- Schumann 2022) and
with a very lean physique cut (power drops with energy deficit).
