---
# Body-ideal archetype sprint 2026-09-30. "체조선수 같은 몸 / 맨몸운동" -- a
# commonly named ideal adjacent to both men's physique (the look) and
# CrossFit (the gymnastics leg of work capacity).
id: exercise/ideal-calisthenics-gymnast-038
domain: exercise
grade: B (bodyweight progression builds strength -- small RCTs); D (archetype definition and skill ladder)
lane: "@gym-craft"
locale: universal
as_of: 2015-2026
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/29466268/"  # Kotarsky CJ et al. J Strength Cond Res 2018;32:651-659 -- progressive calisthenic push-up variations vs bench press, 4 wk, similar 1RM gains in moderately trained men
  - "https://pubmed.ncbi.nlm.nih.gov/24983847/"  # Calatayud J et al. J Strength Cond Res 2015;29:246-53 -- 6RM elastic-band push-up and 6RM bench press at matched EMG gave similar 1RM/6RM gains (n=30 trained)
  - "https://pubmed.ncbi.nlm.nih.gov/36622555/"  # Alizadeh S et al. Sports Med 2023 -- resistance training improves ROM, EXCEPT bodyweight-only programs showed no significant ROM gain
  - "https://pubmed.ncbi.nlm.nih.gov/42012154/"  # Li D et al. J Sports Med Phys Fitness 2026 -- competitive gymnasts: injury prevalence significant; higher competitive level = higher risk
  - "https://pubmed.ncbi.nlm.nih.gov/33322981/"  # CrossFit review: shoulder injuries associated with gymnastic ring dips, muscle-ups, kipping
  - "exercise/progression-modality-load-vs-reps-028"
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      BODYWEIGHT IS A LOAD THAT PROGRESSES BY LEVERAGE, NOT PLATES. Harder
      variations (incline -> floor -> decline -> archer -> one-arm push-up;
      band-assisted -> strict -> weighted pull-up) are the increment. The
      trials show strength gains similar to the barbell equivalent when the
      variation keeps the set hard; adding reps without changing the variation
      drifts into endurance (item 028).
    grade: B
  - note: >
      THE STRAIGHT-ARM AND RING SKILLS ARE THE INJURY END. Planche, front
      lever, ring muscle-up and kipping load the elbow, wrist and shoulder in
      ways a straight-arm novice is not adapted to; progress them slowly and
      separately from the bent-arm strength base.
    grade: D
claim: >
  The calisthenics / gymnast ideal is a lean, relatively light body with high
  strength relative to body weight, visible upper-body and trunk muscularity,
  and control of the body in space: strict pull-ups and dips, push-up and
  pistol-squat variants, and progressively the skills (L-sit, handstand,
  muscle-up, levers, planche). Its distinguishing feature against the physique
  ideals is that the scoreboard is body-weight-relative skill and reps, not
  size; against CrossFit, it is a single modality (bodyweight) pushed to skill
  rather than breadth. Progressive bodyweight training builds strength
  comparably to matched free-weight training in short trials.
reasoning: >
  Two small randomised trials (Calatayud 2015, Kotarsky 2018) show push-up
  progressions matching bench press strength gains when difficulty is kept
  comparable. The archetype definition and skill ladder are practitioner
  convention (street-workout and gymnastics coaching), graded as craft.
  Alizadeh 2023's subgroup finding that bodyweight-only resistance work did not
  improve ROM is a caution against assuming calisthenics delivers the
  gymnast's flexibility by itself.
---

# exercise/ideal-calisthenics-gymnast-038 -- 맨몸운동 / 체조선수형

**한 줄 그림:** 가볍고 탄탄하며 자기 몸을 자유자재로 다루는 몸 -- 턱걸이·딥스·물구나무·머슬업을 해내는
체중 대비 힘.

## Distinguishing features

Relative strength (strength per kg body weight) and skill; lean, light, with
upper-body/trunk definition. Size is a by-product and extra body weight is a
cost.

## Measurable here

- `max_reps_<lift>` (pull-up, dip, push-up) -- the core strand; registered prefix.
- `e1rm_<lift>` for weighted pull-up / dip if loaded.
- `body_weight`, `body_fat_pct` -- relative-strength denominator.
- `skeletal_muscle_kg`, segmental `lean_arm_*` / `lean_trunk_kg` -- secondary.

## Not measurable here

Skill attainment (holds a handstand for N s, first muscle-up), progression level
on a skill ladder, hold durations for levers (a hold_sec log exists per set but
no strand token), wrist/shoulder mobility. A proposed token family
`skill_level_<skill>` would be needed.

## Training emphasis and practice

Progressive variations for push, pull, legs (pistol/shrimp), trunk
(L-sit/hollow body as a skill element), plus handstand practice; mobility
added separately because bodyweight work alone did not raise ROM.
Practice picks: `whole_body` (bear crawl) and `mobility_flow` fit; `power` for
explosive pull/push.

## Failure modes

Elbow/wrist tendon overload from straight-arm skills progressed fast; shoulder
from ring/kipping volume; plateaus from adding reps instead of harder
variations.

## Combines / conflicts

Aligns with men's physique (lean upper-body V) and with CrossFit's gymnastics
leg. Conflicts with open bodybuilding and powerlifting (extra mass costs
relative strength). Pilates complements it (trunk control, articulation).
