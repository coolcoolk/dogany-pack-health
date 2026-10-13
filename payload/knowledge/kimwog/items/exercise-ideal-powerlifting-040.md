---
# Body-ideal archetype sprint 2026-09-30. "힘센 몸 / 파워리프터" -- the
# maximal-strength ideal. Its measure (e1RM on three lifts) is the one this
# product reads best.
id: exercise/ideal-powerlifting-040
domain: exercise
grade: A (rule -- federation lift standards); B (injury epidemiology; heavy-load specificity for 1RM)
lane: "@performance-lit"
locale: universal
as_of: 2017-2026
contested: no
sources:
  - "https://www.powerlifting.sport/rules/codes/info/technical-rules"  # IPF Technical Rule Book (effective 1 Mar 2026, v3): squat (hip crease below top of knee), bench press (paused on chest, press command), deadlift (knees and hips locked); total of best lifts by body-weight class
  - "https://pubmed.ncbi.nlm.nih.gov/27707741/"  # Aasa U et al. Br J Sports Med 2017;51:211-219 -- powerlifting 1.0-4.4 injuries/1000 h, weightlifting 2.4-3.3; spine, shoulder, knee most common; similar to other non-contact strength sports
  - "https://pubmed.ncbi.nlm.nih.gov/27328853/"  # Keogh & Winwood 2017 -- weight-training sports low injury rates vs team sports
  - "https://pubmed.ncbi.nlm.nih.gov/28834797/"  # Schoenfeld BJ et al. -- low- vs high-load: hypertrophy similar, 1RM strength favours high load
  - "exercise/progression-modality-load-vs-reps-028"
  - "exercise/autoregulation-vs-percentage-prescription-030"
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE STRENGTH GOAL NEEDS HEAVY LOADS. Growth is similar across a wide load
      range, but one-rep-max strength favours heavy loading; a rep-progression
      program that drifts to light loads serves the physique strands, not this
      one (item 028).
    grade: B
  - note: >
      E1RM IS AN ESTIMATE, THE MEET IS THE MEASURE. The kit's e1rm_<lift> is
      an Epley estimate from logged top sets; it tracks direction well but is
      not a competition 1RM with standard depth, pause and lockout.
    grade: D
claim: >
  The powerlifting ideal is maximal strength in the squat, bench press and
  deadlift, performed to federation standards (squat below parallel, paused
  bench, locked-out deadlift) and scored as a total within a body-weight class.
  The body it produces is thick and strong through the hips, back and torso,
  often heavier and less lean than the physique ideals, because extra muscle
  and body mass help the total. Injury incidence is 1.0-4.4 per 1000 training
  hours, comparable to other non-contact strength sports, with spine, shoulder
  and knee the usual sites.
reasoning: >
  The lift standards are the IPF technical rules. Aasa 2017's systematic review
  supplies the incidence range and sites. The heavy-load requirement for 1RM
  strength is the Schoenfeld load meta-analysis already carried by item 028.
---

# exercise/ideal-powerlifting-040 -- 파워리프팅 / 최대근력

**한 줄 그림:** 스쿼트·벤치·데드리프트를 무겁게 드는 두껍고 단단한 몸 -- 보이는 것보다 드는 무게가 기준.

## Distinguishing features

Three lifts, maximal load, standard technique, body-weight class. Leanness is
irrelevant; relative-to-class strength matters.

## Measurable here (best-covered archetype)

- `e1rm_<squat>` / `e1rm_<bench>` / `e1rm_<deadlift>` -- registered prefix,
  needs a `goal_metric_source` row per lift; lead-compound slot only.
- `body_weight` -- class and relative strength.
- `skeletal_muscle_kg`, segmental lean -- secondary.
- Workout logs: top-set load, RIR, weekly sets per lift.

## Not measurable here

A competition-standard 1RM (depth, pause, lockout judged), a total, a
Wilks/DOTS score (no token; derivable from e1RMs + body weight but not
registered).

## Training emphasis and practice

Heavy low-rep work on the three lifts with periodised intensity,
autoregulated by RIR (item 030), accessory hypertrophy for weak points.
Program objective `functional` (strength phase) via the `e1rm_` prefix.
Practice picks are optional; `power` (speed sets) fits.

## Failure modes

Lower back from grinding deadlifts and technique breakdown; shoulder/pec from
bench volume; knee. Chronic heavy singles without recovery (harm boundary:
skipping recovery).

## Combines / conflicts

Conflicts with men's physique and calisthenics (body weight direction) and
with high endurance volume. Compatible with open bodybuilding (both want mass)
and with Pilates/mobility as supplementary work.
