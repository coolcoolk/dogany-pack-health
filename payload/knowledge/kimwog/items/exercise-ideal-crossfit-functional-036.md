---
# Body-ideal archetype sprint 2026-09-30. The owner's second named ideal
# ("크로스핏 기능성"). The kit already reads it as work capacity (intervals,
# power, mixed-modal circuits) after the owner's 2026-09-29 13:09 correction;
# this row supplies the source for that reading and the measurement map.
id: exercise/ideal-crossfit-functional-036
domain: exercise
grade: A (rule -- the method's own definition); B (injury epidemiology); C (performance determinants)
lane: "@performance-lit"
locale: universal
as_of: 2002-2023
contested: no
sources:
  - "https://journal.crossfit.com/article/what-is-fitness"  # Glassman G. What Is Fitness? CrossFit Journal, Oct 2002 -- fitness = increased work capacity across broad time and modal domains; ten general physical skills (cardiorespiratory endurance, stamina, strength, flexibility, power, speed, coordination, agility, balance, accuracy)
  - "https://www.crossfit.com/what-is-crossfit"  # current definition: constantly varied functional movements performed at relative intensity
  - "https://pubmed.ncbi.nlm.nih.gov/33322981/"  # Angel Rodriguez M et al. Phys Sportsmed 2022;50:3-10 -- 25 studies, 12,079 practitioners, prevalence 35.3%, incidence 0.2-18.9/1000 h; shoulder 26%, spine 24%, knee 18%; risk: previous injury, no coach supervision, competition; 'similar to weightlifting and powerlifting'
  - "https://pubmed.ncbi.nlm.nih.gov/32223862/"  # Gean RP et al. J Surg Orthop Adv 2020 -- incidence similar to common recreational sports; shoulder, back, knee
  - "https://pubmed.ncbi.nlm.nih.gov/29484512/"  # Claudino JG et al. Sports Med Open 2018 -- 31 articles, only two high-level low-bias; no significant pooled training effects
  - "https://pubmed.ncbi.nlm.nih.gov/32698335/"  # Mangine GT et al. Sports 2020 -- CrossFit Open performance predicted by body composition/muscle CSA, respiratory compensation threshold, rate of force development (n=16)
  - "exercise/ideal-endurance-runner-triathlete-042"
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      FUNCTIONAL HERE MEANS WORK CAPACITY, NOT BALANCE OR COORDINATION. The
      method's own definition is output across broad time and modal domains:
      short and long efforts, lifting, gymnastics and monostructural cardio.
      One-side balance and body linking belong to the connection side (Pilates,
      exercise/ideal-pilates-controlled-movement-037); offering them as "기능성" was the error the owner
      corrected on 2026-09-29.
    grade: A
  - note: >
      THE RISK IS SUPERVISION AND FATIGUE, NOT THE BRAND. Pooled incidence sits
      with weightlifting and powerlifting; the reported risk factors are prior
      injury, lack of coach supervision and competition. Shoulder work under
      fatigue (kipping, ring muscle-ups, overhead lifts) is where the shoulder
      share comes from.
    grade: B
  - note: >
      THE OUTCOME LITERATURE IS THIN. The one systematic review with a
      meta-analysis found few low-bias studies and no significant pooled
      effects; do not promise the method outperforms ordinary concurrent
      training.
    grade: C
claim: >
  CrossFit-type functional fitness defines the goal as work capacity across
  broad time and modal domains: being good at many things at once -- strength,
  power, stamina, cardiorespiratory endurance, gymnastic bodyweight skill,
  speed, agility, balance, coordination, accuracy, flexibility -- trained by
  constantly varied mixed-modal workouts at high relative intensity. The body
  it produces is a lean, muscular, all-round one whose defining feature is what
  it can DO, measured by times, loads, reps and rounds, not by a shape. Its
  injury incidence is similar to weightlifting and powerlifting, concentrated
  in shoulder, spine and knee, with prior injury, lack of supervision and
  competition as the named risk factors.
reasoning: >
  The definition is the method's own foundational text, so it carries the rule
  grade as a definition of the ideal (not as a claim that the method works).
  The injury picture comes from two systematic reviews that agree on the site
  distribution and on comparability with other strength sports. Performance
  determinants (muscle size, a high aerobic threshold, rate of force
  development) come from a small observational study and are graded
  accordingly.
---

# exercise/ideal-crossfit-functional-036 -- 크로스핏 / 기능성 체력

**한 줄 그림:** 무겁게 들고, 빨리 움직이고, 숨이 차도 오래 버티는 -- 무엇이든 잘 해내는 다재다능한
몸. 모양보다 "해내는 능력"이 기준.

## Distinguishing features

- Breadth, not a peak: the target is no big gap across strength, power,
  conditioning and bodyweight skill.
- Mixed-modal and time-bound: work is scored as time, rounds, reps or load.
- Neighbours: powerlifting / weightlifting = one peak (max load, max power);
  endurance = one long-duration peak; Pilates/yoga = control and range, not
  output.

## Measurable here

- `e1rm_<lift>` for a squat/hinge/press (strength leg of the triangle).
- `max_reps_<lift>` for a bodyweight skill (pull-up, push-up) -- the gymnastics
  leg.
- `weekly_sessions`; workouts `minutes` / `kcal` / `avg_hr` for conditioning
  sessions (readable, not a strand token).
- `body_fat_pct`, `skeletal_muscle_kg` -- secondary (they predict performance,
  they are not the goal).
- Practice picks the program acts on: `power`, `mixed_circuit`, `conditioning`.

## Not measurable here

Benchmark workout times (e.g. a named WOD), row/run/bike pace or distance,
jump height, rounds completed in a circuit, VO2max. None has a token; the
workouts table stores minutes and kcal only. A logged benchmark time would need
a new metric (proposed `benchmark_time_s_<name>`).

## Training emphasis and practice

Concurrent strength + conditioning + skill: a lead strength lift, short
interval work, a mixed circuit 1-2x/week, low-dose power. Supervision and
technique before load under fatigue.

## Failure modes

Shoulder overload from high-rep overhead/kipping work under fatigue; spine
under fatigued lifting; returning with a previous injury; competition
intensity without coaching.

## Combines / conflicts

- With classic physique: compatible at moderate conditioning doses; heavy
  running volume costs a little fibre growth (042). Body composition helps
  performance, so the strands mostly pull together.
- With Pilates: complementary -- Pilates brings controlled range and trunk
  control that high-intensity work under fatigue tends to erode.
- With powerlifting: overlapping but diluted -- breadth caps the peak.
