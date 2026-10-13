---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "조정 선수 몸" -- tall, big-framed, a strong back and legs with a very large
# engine. Filed as its own row because it is the one endurance ideal where
# more lean mass helps rather than hurts, and because its two signature
# injuries (low back, ribs) are specific.
id: exercise/ideal-rower-049
domain: exercise
grade: B (rule values read second-hand -- lightweight class limits); B (systematic reviews -- low-back pain and rib stress fracture); C (single studies -- 2,000 m ergometer predictors); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 1999-2025
contested: no
sources:
  - "https://www.nbcolympics.com/news/rowing-101-olympic-rules"  # NBC Olympics rowing rules explainer (World Rowing lightweight limits, fetched 2026-09-30): lightweight men crew average 70 kg, no rower over 72.5 kg; women crew average 57 kg, no rower over 59 kg
  - "https://pubmed.ncbi.nlm.nih.gov/10585164/"  # Cosgrove MJ et al. J Sports Sci 1999 -- 13 club oarsmen: VO2max and lean body mass showed the highest correlations with 2,000 m ergometer performance
  - "https://pubmed.ncbi.nlm.nih.gov/40605029/"  # Ze X et al. BMC Sports Sci Med Rehabil 2025 -- meta-analysis, 10 studies, N=2,082 rowers: previous LBP (OR 2.65) the only significant risk factor; age, sex, BMI, level, training volume, boat type not significant
  - "https://pubmed.ncbi.nlm.nih.gov/26173790/"  # D'Ailly PN et al. J Sports Med Phys Fitness 2016 -- systematic review: rib stress fractures in 8-16% of elite rowers over a career; 4-6 weeks lost; risk factors insufficient or conflicting
  - "https://pubmed.ncbi.nlm.nih.gov/12392443/"  # Warden SJ et al. Sports Med 2002 -- rib stress fracture aetiology in rowers (6.1-12%), rib cage loaded as a unit by muscle forces
  - "exercise/ideal-endurance-runner-triathlete-042"
  - "exercise/ideal-swimmer-043"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      HEIGHT IS SELECTION, THE ENGINE AND BACK ARE TRAINABLE. Open-weight
      rowers are selected tall with long levers; training does not change
      that. A user naming this look is asking for a big back and legs, a
      strong trunk and a large aerobic engine -- offer that.
    grade: D
  - note: >
      THE ONE ENDURANCE IDEAL WHERE LEAN MASS HELPS. In the ergometer data
      lean body mass tracks performance alongside VO2max, so a rower strand
      can own `skeletal_muscle_kg` alongside its conditioning measure without
      contradiction -- unlike the runner (042), where extra mass costs. The
      lightweight class is a sport category; making it by acute weight loss
      is the caught route of exercise/harm-route-boundary-031.
    grade: C
claim: >
  The rower ideal is a tall, strong, big-backed body with powerful legs and
  hips, a stiff trunk and a very large aerobic engine: a stroke is a
  leg-driven hinge finished by the back and arms, repeated for about six to
  seven minutes over 2,000 m. Aerobic capacity and lean body mass both track
  2,000 m ergometer performance, so it is the endurance ideal in which muscle
  mass helps. Low-back pain is common and the only established risk factor is
  having had it before; rib stress fractures affect roughly one in ten elite
  rowers over a career. Lightweight rowing is a defined class (crew average
  70 kg men / 57 kg women). It differs from running endurance by the whole-
  body, weight-supported stroke and the size it rewards, and from the swimmer
  by the leg drive.
reasoning: >
  The class limits are World Rowing rule values as reported by an Olympic
  broadcaster's rules explainer (a definition, but read second-hand -- the
  World Rowing rulebook itself was not fetched). The ergometer predictor is a single
  small study, graded low. The low-back meta-analysis (2025) and the rib
  stress-fracture systematic review (2016) both conclude risk factors beyond
  previous injury are unclear. Picture and translation are craft.
---

# exercise/ideal-rower-049 -- 조정 선수형

**한 줄 그림:** 크고 길쭉한 체격에 넓은 등과 강한 다리·엉덩이, 몸통은 단단하고 심폐는 아주 큰 몸.

## Distinguishing features

Leg-driven, whole-body pulling; large back and posterior chain; stiff trunk
through a hinge; high aerobic power with muscle mass, not despite it.

## Measurable here

- `skeletal_muscle_kg`, `body_weight`, `body_fat_pct`.
- `e1rm_<deadlift>`, `e1rm_<squat>`, `e1rm_<row>` (strength base).
- `weekly_sessions`; erg / water sessions as workouts `minutes`, `avg_hr`
  (readable, not strand tokens).

## Not measurable here

2,000 m time, split per 500 m, weekly rowing distance, erg power. Proposed:
`race_time_s_<distance>` (e.g. `race_time_s_2000`), `row_m_week`,
`cardio_minutes_week`.

## Training emphasis and practice

Mostly low-intensity aerobic volume on the erg or water plus some hard
intervals; 2-3 strength sessions (hinge, squat, rows, trunk), with technique
(hip hinge, not a rounded low back); build erg volume gradually. Picks:
`conditioning` primary, `power`, `breath_trunk` for trunk control.

## Failure modes

Low-back pain (history is the risk marker -- keep it in mind when volume
rises); rib stress from sudden volume jumps; an erg-only week with no
strength work; acute weight cutting for the lightweight class.

## Combines / conflicts

Aligns with the classic X and men's V back development and with CrossFit-type
work capacity (the erg is shared); compatible with the swimmer. Conflicts
with climbing (mass) and with maximal-speed ideals only in scheduling.
