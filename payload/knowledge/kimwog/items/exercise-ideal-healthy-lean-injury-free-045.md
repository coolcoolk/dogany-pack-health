---
# Body-ideal archetype sprint 2026-09-30. "건강하고 탄탄한 몸 / 안 다치는 몸"
# -- the most common answer and the default when a user names no sport. It is
# the only archetype with public-health guideline anchors, so it is graded on
# them and filed in the clinical lane.
id: exercise/ideal-healthy-lean-injury-free-045
domain: exercise
grade: A (WHO 2020 activity guideline); B (strength training reduces sports injury)
lane: "@clinical-physio"
locale: universal
as_of: 2018-2020
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/33239350/"  # Bull FC et al. Br J Sports Med 2020;54:1451-1462 -- WHO 2020: adults 150-300 min moderate or 75-150 min vigorous aerobic activity/week, muscle-strengthening activity on 2+ days, reduce sedentary time
  - "https://pubmed.ncbi.nlm.nih.gov/30131332/"  # Lauersen JB et al. Br J Sports Med 2018;52:1557-1563 -- strength training reduced acute and overuse sports injuries (RR 0.338), dose-dependent: +10% strength-training volume cut risk by >4 percentage points
  - "https://pubmed.ncbi.nlm.nih.gov/36622555/"  # Alizadeh 2023 -- full-range resistance training improves ROM
  - "source:nutrition/body-composition-measurement-floor-011"
  - "exercise/harm-route-boundary-031"
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: activity_level
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      "INJURY-FREE" HAS A TRAINABLE LEVER. Strength training cut sports
      injuries to about a third in pooled trials, dose-dependently. The
      injury-free strand is served by lifting, not by avoiding it.
    grade: B
  - note: >
      THIS IS THE DEFAULT PICTURE, NOT A LESSER ONE. When a user names no
      sport or look, this archetype is the frame; a named archetype refines
      it rather than replacing it (the guideline minimums still apply under
      every other row).
    grade: D
claim: >
  The healthy-lean / injury-free ideal is a body with a healthy body-fat range,
  enough muscle and strength for daily life and ageing, good aerobic fitness,
  comfortable range of motion, and few injuries -- a body that keeps training
  for decades. Its anchors are the WHO 2020 guideline (150-300 minutes of
  moderate or 75-150 of vigorous aerobic activity a week plus muscle
  strengthening on two or more days) and the finding that strength training
  reduces acute and overuse injuries to about a third, dose-dependently. It is
  distinguished from the physique ideals by having no stage look and from the
  sport ideals by having no single peak.
reasoning: >
  WHO 2020 is the global public-health guideline (Bull 2020), hence the top
  grade for the dose. Lauersen 2018 pooled six well-executed trials (7,738
  participants) with a robust RR of 0.338 and a dose-response. ROM via
  full-range lifting (Alizadeh 2023) supports "comfortable range" without a
  separate stretching program.
---

# exercise/ideal-healthy-lean-injury-free-045 -- 건강하고 탄탄한 몸 (안 다치는 몸)

**한 줄 그림:** 적당히 군살 없고, 일상과 나이 듦을 버틸 근력과 체력이 있으며, 오래 다치지 않고
운동을 이어가는 몸.

## Distinguishing features

No peak, no stage: health ranges, balance across strength / aerobic / mobility,
longevity of training. The default frame under every other archetype.

## Measurable here

- `weekly_sessions` -- the habit strand.
- `body_fat_pct`, `skeletal_muscle_kg`, `body_weight` (trend, per the
  measurement-floor item).
- Workouts `minutes` for aerobic minutes against the 150-300 min/week band
  (readable; no strand token -- proposed `cardio_minutes_week`).
- `e1rm_<lift>` / `max_reps_<lift>` -- strength maintenance.
- Pain-event log (pain-triage) as the injury signal.

## Not measurable here

Blood pressure, lipids, glucose, VO2max, sleep quality here (other domains /
devices), mobility tests.

## Training emphasis and practice

Two or more full-body strength sessions, aerobic minutes to the guideline band,
a mobility flow; progression conservative. Picks: `mobility_flow`,
`conditioning`.

## Failure modes

Doing only cardio (drops the injury-reducing lever); all-or-nothing volume jumps;
reading one InBody number as a verdict.

## Combines / conflicts

Combines with everything; it is the floor the others stand on.
