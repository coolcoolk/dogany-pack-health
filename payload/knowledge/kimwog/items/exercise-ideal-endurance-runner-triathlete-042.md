---
# Body-ideal archetype sprint 2026-09-30. "러너 / 철인 같은 몸" -- the
# endurance ideal, and the carrier of the concurrent-training evidence the
# other archetype rows cite when they combine with cardio.
id: exercise/ideal-endurance-runner-triathlete-042
domain: exercise
grade: B (concurrent-training interference; strength training improves running economy; running-injury incidence); D (archetype definition)
lane: "@performance-lit"
locale: universal
as_of: 2015-2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/34757594/"  # Schumann M et al. Sports Med 2022 -- 43 studies: concurrent training does not compromise hypertrophy or max strength; explosive strength attenuated (SMD -0.28), esp. same session
  - "https://pubmed.ncbi.nlm.nih.gov/35476184/"  # Lundberg TR et al. Sports Med 2022 -- small negative effect on muscle FIBRE hypertrophy (SMD -0.23); type I fibre interference with running, not cycling
  - "https://pubmed.ncbi.nlm.nih.gov/22002517/"  # Wilson JM et al. J Strength Cond Res 2012 -- interference scales with modality, frequency and duration of endurance work; running worse than cycling
  - "https://pubmed.ncbi.nlm.nih.gov/38165636/"  # Llanos-Lagos C et al. Sports Med 2024 -- high-load and combined strength training improve running economy (small-moderate), plyometrics at slower speeds
  - "https://pubmed.ncbi.nlm.nih.gov/25951917/"  # Videbaek S et al. Sports Med 2015 -- running-related injuries 17.8/1000 h novice vs 7.7/1000 h recreational runners
  - "https://pubmed.ncbi.nlm.nih.gov/33239350/"  # Bull FC et al. Br J Sports Med 2020 -- WHO 2020: 150-300 min moderate or 75-150 min vigorous aerobic activity per week
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      ADDING CARDIO TO A PHYSIQUE GOAL COSTS LESS THAN FEARED. Whole-muscle
      hypertrophy and maximal strength are not measurably compromised by
      concurrent aerobic training; explosive strength is, and fibre-level
      growth shows a small cost that is larger with running than cycling.
      Practical routing: cycling or rowing over running when growth matters,
      and separate the sessions by several hours when power matters.
    grade: B
  - note: >
      NOVICE RUNNERS GET HURT AT MORE THAN TWICE THE RATE. A user starting to
      run from zero toward a race goal is in the 17.8 per 1000 h group; build
      volume gradually, and treat pain off the soreness time course as a
      caught route (ignoring pain).
    grade: B
  - note: >
      LIFTING HELPS RUNNERS. Heavy strength training improves running economy;
      an endurance ideal is not a reason to drop the lifts.
    grade: B
claim: >
  The endurance ideal (runner, cyclist, triathlete) is a light, lean body with
  high aerobic capacity and economy: it can sustain a pace for a long time, its
  limbs carry little excess mass, and its muscles are fatigue-resistant rather
  than large. It is distinguished from CrossFit-type fitness by specialising in
  long-duration efforts, and it pulls against the size ideals mainly through
  energy availability and running volume. Concurrent aerobic and strength
  training does not blunt whole-muscle hypertrophy or maximal strength but does
  blunt explosive strength; heavy strength training improves running economy;
  novice runners are injured at 17.8 per 1000 h versus 7.7 for recreational
  runners.
reasoning: >
  Schumann 2022 (43 studies) is the most recent and largest concurrent-training
  meta-analysis; Lundberg 2022 adds the fibre-level small cost and the
  running-versus-cycling moderator; Wilson 2012 is the older meta that first
  located interference in modality, frequency and duration. The running-economy
  benefit of strength work is Llanos-Lagos 2024. Injury incidence by runner type
  is Videbaek 2015. The archetype picture is convention.
---

# exercise/ideal-endurance-runner-triathlete-042 -- 지구력 (러너 / 철인)

**한 줄 그림:** 가볍고 군살 없는, 숨이 오래가는 몸 -- 크기보다 오래, 효율적으로 움직이는 능력.

## Distinguishing features

Long-duration aerobic output, economy, low body mass for the effort; muscle is
fatigue-resistant rather than large.

## Measurable here

- Workouts `minutes`, `kcal`, `avg_hr` for cardio sessions (readable; no strand
  token -- proposed `cardio_minutes_week`).
- `weekly_sessions`.
- `body_weight`, `body_fat_pct` -- relevant, secondary.
- `e1rm_<squat>` -- the strength support that improves economy.

## Not measurable here

Distance, pace, race time, VO2max, lactate threshold, heart-rate zones time.
The kit's `hk-ingest` activity map may bring distance in from HealthKit, but no
goal token reads it. Proposed: `run_km_week`, `race_time_s_<distance>`.

## Training emphasis and practice

Mostly easy aerobic volume with some hard intervals, gradual volume build,
2 strength sessions/week (heavy, low volume), plyometrics. Practice pick
`conditioning` is a small dose of the same quality; it is not endurance
training on its own.

## Failure modes

Overuse injuries from fast volume increases (novices especially); low energy
availability in lean-chasing runners (nutrition/energy-availability-threshold-010);
dropping strength work.

## Combines / conflicts

- With physique ideals: modest interference; prefer cycling/rowing, keep
  running volume moderate, separate sessions from power work.
  Placement rules (order, hours apart, modality, dose) for cardio inside a
  lifting week: exercise/concurrent-cardio-interference-cut-062 (evidence) and
  exercise/cut-cardio-placement-rule-063 (rules).
- With CrossFit: overlapping (conditioning), different duration focus.
- With Pilates/yoga: complementary.

Cycling-first and rowing-first ideals have their own rows
(exercise/ideal-cyclist-050, exercise/ideal-rower-049): weight-supported,
with different bone and body-mass trade-offs from running.
