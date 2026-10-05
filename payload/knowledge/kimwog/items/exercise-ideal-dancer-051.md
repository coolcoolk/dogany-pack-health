---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "무용수 몸" -- long, lean, extremely mobile and controlled, with jumps and
# turns. Filed next to Pilates (037, historically a dancers' method) and yoga
# (039) because it is the movement ideal that ALSO needs power (jumps) and
# conditioning, and because its population carries documented energy-
# deficiency and low-back risks.
id: exercise/ideal-dancer-051
domain: exercise
grade: B (systematic reviews -- low-back pain in dance, contemporary-dance fitness); C (small cohorts -- energy deficiency in professional dancers; feasibility trial); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2009-2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/30658051/"  # Swain CTV et al. J Orthop Sports Phys Ther 2019 -- systematic review, 50 studies: dancers' low-back pain median point prevalence 27%, 12-month 73%, lifetime 50%; lower back ~11% of time-loss injuries
  - "https://pubmed.ncbi.nlm.nih.gov/19301219/"  # Angioi M et al. Int J Sports Med 2009 -- systematic review, contemporary dance fitness: professionals have higher VO2max and muscular endurance than ballet dancers; only two studies of supplementary fitness training, preliminary benefit for performance
  - "https://pubmed.ncbi.nlm.nih.gov/29405782/"  # Staal S et al. Int J Sport Nutr Exerc Metab 2018 -- 40 professional ballet dancers: suppressed RMR in 25-100% depending on equation; 10% disordered eating; 50% of women underweight; dancers at risk of energy deficiency
  - "https://pubmed.ncbi.nlm.nih.gov/21358502/"  # Hoch AZ et al. Clin J Sport Med 2011 -- 22 professional women dancers: 77% low/negative energy availability, 32% disordered eating, 36% menstrual dysfunction, 23% low bone density
  - "https://pubmed.ncbi.nlm.nih.gov/35697491/"  # Kolokythas N et al. J Dance Med Sci 2022 -- feasibility RCT, pre-professional ballet: 11+ Dance neuromuscular programme; fear of muscle hypertrophy and fatigue reported as reasons for attrition
  - "exercise/ideal-pilates-controlled-movement-037"
  - "exercise/ideal-yoga-mobility-039"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE DANCER LOOK IS NOT A THINNESS TARGET. Professional dancer samples
      show high rates of low energy availability, disordered eating and
      menstrual dysfunction. When a user names "무용수 같은 몸", coach the
      movement qualities (range, control, balance, jump, posture) and a normal
      body-composition direction; never set a low body weight or body-fat
      number as the dancer goal.
    grade: C
  - note: >
      STRENGTH WORK DOES NOT MAKE A DANCER BULKY AT THESE DOSES. Fear of
      hypertrophy is a documented reason dancers drop out of strength and
      neuromuscular programmes. Supplementary fitness training is preliminary
      but favourable; the pack offers moderate-volume strength and power work
      as support for jumps, landings and the low back, not as a mass program.
    grade: D
claim: >
  The dancer ideal is a long, lean, upright body with extreme but controlled
  range of motion, fine balance, strong feet and ankles, springy jumps and the
  endurance to repeat choreography, with expression layered on top. It differs
  from Pilates (controlled movement, no jumps) and yoga (range and positions)
  by combining range with power, turns and intermittent conditioning. Its
  population carries a high low-back pain burden (about three in four dancers
  in a year) and documented energy-deficiency risk in professionals.
  Supplementary strength and fitness training is under-studied but
  preliminarily favourable, and fear of getting bulky is itself a barrier.
reasoning: >
  Low-back epidemiology is a systematic review of 50 studies with wide
  heterogeneity (Swain 2019). Fitness and supplementary-training evidence is a
  2009 systematic review with only two training studies (Angioi). Energy-
  deficiency figures are small professional cohorts (n=40, n=22) and depend on
  method, so they describe risk, not prevalence. The barrier finding is one
  feasibility trial. Picture and translation are craft.
---

# exercise/ideal-dancer-051 -- 무용수형

**한 줄 그림:** 길고 곧은 자세, 넓지만 통제된 가동범위, 가볍게 뛰어오르고 흔들림 없이 착지하는 몸.

## Distinguishing features

Range with control (active flexibility); balance and turns; foot and ankle
strength; jumps and landings; intermittent conditioning; posture and line.

## Measurable here

- `unilateral_share_sets` (single-leg balance and landing work -- partial).
- `max_reps_<calf_raise>` or `max_reps_<single_leg_squat>` (foot/leg
  endurance), `weekly_sessions`.
- Classes as workouts `minutes` (readable). InBody is context only.

## Not measurable here

Range of motion, balance time, jump height, turn quality, choreography
endurance. Proposed: `rom_<joint>_deg`, `balance_s_single_leg`, `jump_cm`.

## Training emphasis and practice

Class / practice first. Support work: moderate-volume strength for legs,
hips, trunk and feet; plyometric and landing work; controlled end-range
strength (Pilates-type) rather than passive stretching alone; aerobic
intervals matched to a piece. Picks: `mobility_flow`, `breath_trunk`,
`whole_body`, `power` (jumps).

## Failure modes

Low energy availability chasing a thinner line; low-back pain from repeated
extension; foot and ankle overuse; avoiding strength work for fear of bulk;
passive over-stretching without control.

## Combines / conflicts

Aligns with Pilates and yoga/mobility (natural partners) and with
calisthenics (body control). Conflicts with open bodybuilding and powerlifting
mass, and with any deep-cut phase.
