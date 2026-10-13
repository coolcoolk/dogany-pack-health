---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "스프린터 몸 / 운동선수 같은 몸" -- the lean, muscular, springy athletic
# look. Split from weightlifting / athletic power (041): the sprinter's power
# is horizontal and elastic (ground contact at speed), its signature injury is
# the hamstring, and it is measured by a clock, not a bar.
id: exercise/ideal-sprinter-athletic-048
domain: exercise
grade: B (meta-analysis -- strength gains transfer to sprint; championship injury surveillance); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2014-2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/25059334/"  # Seitz LB et al. Sports Med 2014 -- meta-analysis, 15 studies, 510 subjects: increases in back-squat strength transfer to sprint performance (r = -0.77 between strength and sprint changes)
  - "https://pubmed.ncbi.nlm.nih.gov/33632663/"  # Edouard P et al. J Sci Med Sport 2021 -- international championships, 12,233 athletes: hamstring is the most injured muscle group in sprints, hurdles, jumps and combined events (43-75% of lower-limb muscle injuries); hamstring burden rises with running velocity
  - "https://pubmed.ncbi.nlm.nih.gov/36078705/"  # Edouard P et al. Int J Environ Res Public Health 2022 -- 357 championship athletes: 48% reported a hamstring injury in their career; more core (lumbo-pelvic) stability training associated with lower in-championship hamstring injury (OR 0.49), observational
  - "https://pubmed.ncbi.nlm.nih.gov/38857522/"  # Maeo S et al. Med Sci Sports Exerc 2024 -- trained hip-extension-biased (lengthened) hamstring work grew biceps femoris long head more than Nordic curls; sprint and injury benefit inferred, not tested
  - "exercise/ideal-weightlifting-athletic-power-041"
  - "exercise/ideal-endurance-runner-triathlete-042"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      "운동선수 같은 몸" IS AMBIGUOUS -- ASK WHICH ATHLETE. The lean, muscular,
      springy look people call athletic is usually the sprinter (horizontal
      speed, hamstrings and glutes) or the weightlifter/jumper (vertical bar
      and jump power, 041). Name both pictures and let the user pick; the
      measures differ (a sprint clock vs a bar or jump).
    grade: D
  - note: >
      SPRINTING IS THE HAMSTRING'S HIGHEST-RISK TASK. Adding maximal sprints
      to a program needs a gradual build and hamstring strength work in both
      knee-flexion and hip-extension patterns; the lengthened-position growth
      finding is a hypertrophy result, its injury benefit is inferred.
    grade: B
claim: >
  The sprinter / athletic ideal is a lean, muscular, springy body built for
  top speed over short distances: powerful glutes, hamstrings and calves,
  strong hips and trunk, fast elastic ground contacts, low body fat, and only
  as much upper body as the arm drive needs. Gains in lower-body (squat)
  strength transfer to sprint speed, so heavy strength training belongs in the
  program, but the hamstring is the most injured muscle group in sprinting
  events and its injury burden rises with running velocity. It differs from
  weightlifting/athletic power by being horizontal and elastic and measured by
  a clock, and from endurance running by duration and muscle mass.
reasoning: >
  The strength-to-sprint transfer is a meta-analysis (Seitz 2014) of mostly
  non-elite trained subjects. Injury location is championship surveillance
  (Edouard 2021, 2022) -- large but observational, with the protective
  association of trunk work not causal. The hamstring hypertrophy finding is a
  single trial. The look (lean, muscular) is the craft picture of the event.
---

# exercise/ideal-sprinter-athletic-048 -- 스프린터 / 운동선수형

**한 줄 그림:** 군살 없이 단단하고, 엉덩이·햄스트링·종아리가 탄력 있게 발달한, 짧게 폭발적으로 달리는 몸.

## Distinguishing features

Horizontal, elastic power; posterior chain (glutes, hamstrings, calves)
dominance; lean; athletic upper body without bulk. The scoreboard is time over
a short distance.

## Measurable here

- `e1rm_<squat>`, `e1rm_<hip_thrust>` or `e1rm_<deadlift>` (strength that
  transfers).
- `body_fat_pct`, `skeletal_muscle_kg`, `body_weight`.
- Segmental `lean_leg_*_kg` (readable, not a strand token); track sessions as
  workouts `minutes`.

## Not measurable here

Sprint time, acceleration, jump height, hamstring strength. Proposed:
`sprint_s_<distance>`, `jump_cm`.

## Training emphasis and practice

Sprint technique and short maximal sprints with full recovery, built up
gradually; heavy lower-body strength 2x/week; plyometrics (bounds, hops);
hamstring work in both patterns (Nordic-type and hip-hinge/lengthened);
trunk stability. Picks: `power` primary, `conditioning` sparingly.

## Failure modes

Hamstring strain from sprint volume or speed jumps; turning sprint work into
long interval conditioning (a different quality); skipping strength.

## Combines / conflicts

Aligns with weightlifting/athletic power and with the classic X (legs judged);
combines with racket and team-sport ideals. Conflicts with endurance volume
(running economy vs top speed) and with open-bodybuilding mass.
