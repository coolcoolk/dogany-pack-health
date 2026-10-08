---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "사이클 선수 몸" -- split from the endurance row (042), which is written
# runner-first. Cycling is weight-supported: little impact injury, but no
# bone-loading, and the power-to-weight scoreboard is watts per kg. The track
# sprinter (huge quads) is a different picture from the road rider.
id: exercise/ideal-cyclist-050
domain: exercise
grade: B (systematic reviews -- bone health, overuse risk factors, road injury; narrative review of concurrent strength); B (large cohort -- mortality association); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2012-2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/23256921/"  # Olmedillas H et al. BMC Med 2012 -- systematic review, 31 studies: adult road cyclists in regular training have low BMD in key regions (e.g. lumbar spine); road cycling confers no significant osteogenic benefit; mountain biking or mixing sports may offset
  - "https://pubmed.ncbi.nlm.nih.gov/22164312/"  # Nagle KB, Brooks MA. Sports Health 2011 -- systematic review, 13 studies: concern that weight-supported cycling does not benefit bone
  - "https://pubmed.ncbi.nlm.nih.gov/23914932/"  # Ronnestad BR, Mujika I. Scand J Med Sci Sports 2014 -- review: heavy strength training added to endurance training improves cycling economy and performance (most compelling additive evidence for heavy, not explosive, strength in cycling)
  - "https://pubmed.ncbi.nlm.nih.gov/35151569/"  # Visentini PJ et al. J Sci Med Sport 2022 -- systematic review, 18 studies: moderate evidence that load relates to overuse symptoms; moderate evidence of NO relationship with many bike-fit measures; no strong evidence for any bike/body/load factor
  - "https://pubmed.ncbi.nlm.nih.gov/34422283/"  # Rooney D et al. BMJ Open Sport Exerc Med 2020 -- systematic review of road cycling: abrasions/lacerations 40-60% of injuries, fractures 6-15% (clavicle most common), head injury 5-15%; patellofemoral pain the top overuse diagnosis
  - "https://pubmed.ncbi.nlm.nih.gov/27895075/"  # Oja P et al. Br J Sports Med 2017 -- 80,306 adults: cycling participation associated with lower all-cause mortality (HR 0.85), no significant CVD association
  - "exercise/ideal-endurance-runner-triathlete-042"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      ASK ROAD OR TRACK. The road / climbing rider is light and lean with a
      slim upper body (power-to-weight); the track sprinter carries very large
      quadriceps and glutes (peak power). Most users mean the road rider; the
      measures differ (sustained watts per kg vs peak power).
    grade: D
  - note: >
      CYCLING DOES NOT LOAD BONE. Road cyclists in regular training show low
      bone density in the lumbar spine. A cyclist strand keeps heavy strength
      work and some impact (jumps, running, hiking) in the week -- for bone,
      and because heavy strength improves cycling economy.
    grade: B
claim: >
  The cyclist ideal is a lean, light body with strong quadriceps, glutes and
  calves, a trunk that holds a forward position for hours and a very large
  aerobic engine, judged by sustained power relative to body weight. Because
  cycling is weight-supported it spares the joints but does not build bone:
  road cyclists who train regularly have low bone density in key regions.
  Heavy strength training added to cycling improves economy and performance,
  and overuse symptoms follow load while most bike-fit measures show no link.
  Road injuries are mostly abrasions and upper-limb fractures from crashes. It
  differs from the runner (042) by the weight support, the bone risk and the
  watts-per-kg scoreboard, and from the rower by the lighter upper body.
reasoning: >
  Bone findings are two systematic reviews of mostly cross-sectional studies
  (Olmedillas 2012, Nagle 2011). The strength-for-cycling claim is a
  narrative review of trials (Ronnestad & Mujika 2014). Overuse risk factors
  and road-injury patterns are systematic reviews whose own authors call the
  evidence limited. The mortality association is a large observational cohort,
  not causal. The picture is craft.
---

# exercise/ideal-cyclist-050 -- 사이클 선수형

**한 줄 그림:** 가볍고 군살 없는 몸에 허벅지와 엉덩이가 단단한, 몇 시간을 일정한 힘으로 밟는 몸.

## Distinguishing features

Sustained power per kg; quadriceps/glute dominance; slim upper body (road);
trunk endurance in a flexed position; very large aerobic engine. Track
sprinters are a separate, heavier picture.

## Measurable here

- `body_weight`, `body_fat_pct` (power-to-weight context).
- `e1rm_<squat>` or `e1rm_<leg_press>` (heavy strength for economy and bone).
- `weekly_sessions`; rides as workouts `minutes`, `avg_hr` (readable, not
  strand tokens).

## Not measurable here

Power output (FTP, watts per kg), ride distance, time-trial times, bone
density. Proposed: `ftp_w_per_kg`, `ride_km_week`, `cardio_minutes_week`.

## Training emphasis and practice

Mostly easy aerobic riding with some threshold and interval work, 2 heavy
low-rep lower-body strength sessions a week, some impact (jumps, running,
hiking) for bone, trunk and hip-flexor/thoracic mobility against the riding
posture. Picks: `conditioning` primary, `power`, `mobility_flow`.

## Failure modes

Low bone density from riding-only training; knee (patellofemoral) pain with
sudden load jumps; crash injuries; dropping strength work; chasing a lower
body weight for climbing.

## Combines / conflicts

Aligns with the runner/triathlete and healthy-lean rows; compatible with the
classic X legs (cycling costs less muscle growth than running -- see 042).
Conflicts with open bodybuilding and powerlifting mass on climbs, and with
climbing only in shared lightness pressure.
