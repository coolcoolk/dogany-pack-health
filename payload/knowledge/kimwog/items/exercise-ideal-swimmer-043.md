---
# Body-ideal archetype sprint 2026-09-30. "수영선수 몸" -- a frequently named
# look (broad shoulders, long lats, lean) whose training is a sport the
# product barely records.
id: exercise/ideal-swimmer-043
domain: exercise
grade: B (swim volume and shoulder pain, adolescent level-II evidence); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2020-2023
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/31935141/"  # Feijen S et al. J Athl Train 2020 -- 12 studies, 1460 swimmers: swim-training volume associated with shoulder pain in adolescents; supraspinatus thickening with volume
  - "https://pubmed.ncbi.nlm.nih.gov/37515375/"  # McKenzie A et al. Scand J Med Sci Sports 2023 -- systematic review of shoulder pain/injury risk factors in competitive swimmers
  - "exercise/ideal-mens-physique-v-taper-034"
  - "exercise/ideal-endurance-runner-triathlete-042"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE SWIMMER'S BODY IS PARTLY SELECTION. Elite swimmers are selected for
      long limbs, a long torso and large hands and feet; training does not make
      a person taller or longer-armed. A user naming this look is usually
      asking for broad shoulders, long lats and leanness, which is the men's
      physique V without the stage leanness -- offer that picture. Marked
      contested because the selection-vs-training split is not quantified by a
      source here.
    grade: D
claim: >
  The swimmer ideal is a long, lean, broad-shouldered body with wide lats and a
  V-shaped upper body, supple shoulders and a strong trunk, built by high
  volumes of water-supported, full-range pulling at aerobic and anaerobic
  intensities. Its signature risk is the shoulder: training volume is
  associated with shoulder pain and supraspinatus tendon thickening, at least in
  adolescent competitors. It shares the upper-body V with men's physique and
  the aerobic engine with endurance athletes; part of the look is selection
  (limb length), not trainable.
reasoning: >
  The shoulder-volume association is a systematic review (Feijen 2020, level-II
  conclusion for adolescents) with a later risk-factor review (McKenzie 2023).
  The picture and the gym translation (pull-dominant upper-body volume, rotator
  cuff and scapular work, aerobic volume in the pool) are practitioner
  convention, and the selection point is the item's own reasoning, not a sourced
  number.
---

# exercise/ideal-swimmer-043 -- 수영선수형

**한 줄 그림:** 길고 군살 없는 상체에 넓은 어깨와 등이 펼쳐진 몸, 부드러운 어깨와 강한 몸통.

## Distinguishing features

Upper-body V (like men's physique) but leaner-by-volume rather than by diet, less
bulk, long lats, shoulder mobility; aerobic engine. Leg development modest.

## Measurable here

- Swim sessions as workouts `minutes` / `kcal` (no distance/stroke data).
- Segmental `lean_arm_*` / `lean_trunk_kg` share; `body_fat_pct`.
- Gym side: `max_reps_<pull_up>`, weekly pull sets.

## Not measurable here

Swim distance, pace per 100 m, stroke count, shoulder range. Proposed:
`swim_m_week`.

## Training emphasis and practice

In the pool: aerobic volume and technique. In the gym: pulling volume (lats,
rear delts), rotator cuff and scapular control (see
exercise/serratus-anterior-integration-019), trunk; `mobility_flow` fits.

## Failure modes

Shoulder overuse from volume jumps; pressing-dominant gym work adding to an
already overloaded shoulder.

## Combines / conflicts

Aligns with men's physique and endurance; conflicts with open bodybuilding mass.
Pilates complements (trunk, shoulder control).
