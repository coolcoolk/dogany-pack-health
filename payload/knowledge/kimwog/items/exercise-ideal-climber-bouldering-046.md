---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "클라이머 몸" -- the owner's own example: strength-to-weight, back /
# forearm / finger, lean. Filed because it is the one archetype where the
# hold-counting kit token is a PARTIAL fit (hangs are isometric), which is the
# opposite of Pilates (037), and because leanness in this sport carries a
# documented low-energy-availability pressure.
id: exercise/ideal-climber-bouldering-046
domain: exercise
grade: B (systematic reviews -- performance determinants and injury epidemiology); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2019-2025
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/31193395/"  # Saul D et al. J Exerc Sci Fit 2019 -- systematic review, determinants for success in climbing: low skinfold/body fat and large forearm volume in successful climbers; hand-grip strength and endurance, long finger and bent-arm hang times in elites; fingerboard and eccentric-concentric training push red-point grade
  - "https://pubmed.ncbi.nlm.nih.gov/41562737/"  # Zielinski J et al. J Funct Morphol Kinesiol 2025 -- systematic review, 7 studies, >4000 lead/bouldering climbers: overuse injuries (fingers, shoulders) exceed acute in adults; risk-factor evidence inconclusive and contradictory
  - "https://pubmed.ncbi.nlm.nih.gov/38939753/"  # Slagel N et al. Front Sports Act Living 2024 -- 324 recreational climbers: 78.7% rate strength-to-weight as important; body-type ideals and social media predict weight-loss and food-tracking behaviour; climbers flagged at risk of disordered eating / low energy availability
  - "exercise/ideal-calisthenics-gymnast-038"
  - "exercise/ideal-pilates-controlled-movement-037"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      STRENGTH-TO-WEIGHT HAS TWO SIDES; COACH THE STRENGTH SIDE. Lower body fat
      separates better climbers from worse ones in cross-sectional data, and
      recreational climbers already chase weight loss for it, with disordered
      eating and low energy availability named as a risk in this population.
      Build finger, forearm and pulling strength and let body weight follow a
      normal lean phase; never make a lower number on the scale the climbing
      goal, and route any restriction-to-make-a-grade talk to the pack's
      harm-route boundary (exercise/harm-route-boundary-031).
    grade: B
  - note: >
      HANGS ARE HOLDS. Unlike Pilates, the climber's key gym work (dead hangs,
      fingerboard hangs, lock-offs, front-lever holds) really is timed
      isometric holding, so `zero_load_control_share_sets` is a partial, honest
      measure here. It still does not measure finger strength (load on a given
      edge) or climbing grade.
    grade: D
claim: >
  The climber / bouldering ideal is a light, lean body that is very strong for
  its weight in the fingers, forearms, back and shoulders, with a strong trunk
  that keeps the feet on the wall. Successful climbers show low body fat, large
  forearm volume, high grip and finger strength relative to body mass and long
  finger and bent-arm hang times, and fingerboard plus eccentric-concentric
  training raises the hardest route they can send. Its injuries are mostly
  overuse of the fingers (pulleys) and shoulders, and specific risk factors are
  not established. It differs from calisthenics by the finger/grip limiter and
  the wall skill, and from men's physique by being judged on what it can hang
  from, not on size.
reasoning: >
  Determinants are a systematic review (Saul 2019), mostly cross-sectional
  comparisons of better vs worse climbers, so they describe the profile rather
  than prove what training causes it. The injury pattern is a 2025 systematic
  review whose own conclusion is that risk factors remain inconclusive. The
  leanness pressure is a single survey of recreational climbers (not pooled),
  carried as a caution, not a prevalence. The gym translation is craft.
---

# exercise/ideal-climber-bouldering-046 -- 클라이머 / 볼더링형

**한 줄 그림:** 가볍고 군살 없는 몸에 손가락·전완·등이 체중 대비 아주 강한, 벽에 오래 매달리는 몸.

## Distinguishing features

Strength-to-weight in the fingers, forearms and back; bent-arm and
straight-arm hanging; trunk tension that holds the feet on; low body fat;
modest leg size. The limiter is usually the fingers, not the lats.

## Measurable here

- `body_weight`, `body_fat_pct` (context only, never the goal).
- `max_reps_<pull_up>` and `e1rm_<weighted_pull_up>` for the pulling side.
- `zero_load_control_share_sets` -- a partial fit: dead hangs, lock-offs and
  lever holds are timed holds.
- Segmental `lean_arm_*_kg` (readable, not a strand token); gym and wall
  sessions as workouts `minutes`.

## Not measurable here

Finger strength on an edge, maximum hang time, grip strength, climbing grade.
Proposed: `hang_s_<edge>`, `grip_kg`, `climb_grade_<discipline>`.

## Training emphasis and practice

On the wall: climbing volume and technique first. Off the wall: fingerboard
work only after a base of climbing (progressive, submaximal first), weighted
pulling, antagonist pushing and rotator cuff for the shoulder, trunk tension
(leg raises, lever progressions). Picks: `power` (pulling), `whole_body`,
`mobility_flow` for hips (high steps, drop-knees).

## Failure modes

Finger pulley overload from jumping fingerboard load or crimping volume;
shoulder overuse; cutting weight to climb harder (see the refraction note);
pulling-only gym work.

## Combines / conflicts

Aligns with calisthenics (bodyweight strength) and yoga/mobility (hip range);
compatible with men's physique if upper-body mass stays moderate. Conflicts with
open bodybuilding and powerlifting mass (strength-to-weight falls).
