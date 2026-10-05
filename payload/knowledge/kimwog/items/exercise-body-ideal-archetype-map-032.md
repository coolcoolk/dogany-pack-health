---
# Body-ideal archetype sprint 2026-09-30 (owner ask 19:53). The index row for
# items 033-045: which archetype a user's words name, how to tell neighbours
# apart, what each one can and cannot be measured by here, and how they combine
# when a user names several (the owner named three: classic physique X-taper,
# CrossFit function, Pilates connection). The machine-readable form of this
# row is payload/service/health/body_ideal_archetypes.json; this item is the
# graded source of truth that table points back to.
id: exercise/body-ideal-archetype-map-032
domain: exercise
grade: D (synthesis rule over the graded archetype rows)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/ideal-classic-physique-x-taper-033"
  - "exercise/ideal-mens-physique-v-taper-034"
  - "exercise/ideal-open-bodybuilding-035"
  - "exercise/ideal-crossfit-functional-036"
  - "exercise/ideal-pilates-controlled-movement-037"
  - "exercise/ideal-calisthenics-gymnast-038"
  - "exercise/ideal-yoga-mobility-039"
  - "exercise/ideal-powerlifting-040"
  - "exercise/ideal-weightlifting-athletic-power-041"
  - "exercise/ideal-endurance-runner-triathlete-042"
  - "exercise/ideal-swimmer-043"
  - "exercise/ideal-combat-fighter-044"
  - "exercise/ideal-healthy-lean-injury-free-045"
  - "exercise/ideal-climber-bouldering-046"
  - "exercise/ideal-grappler-ssireum-wrestler-047"
  - "exercise/ideal-sprinter-athletic-048"
  - "exercise/ideal-rower-049"
  - "exercise/ideal-cyclist-050"
  - "exercise/ideal-dancer-051"
  - "exercise/ideal-ski-snowboard-052"
  - "exercise/ideal-racket-sports-053"
  - "owner correction 2026-09-30 19:53 (goal consult): X-taper described as V-taper with legs missing; measured by body fat alone; Pilates treated as isometric holds"
  - "owner ask 2026-09-30 19:57/20:02 (pass 2): climber, 씨름/wrestler/grappler distinct from the striking-leaning combat row, sprinter/athletic, rower, cyclist, dancer, ski/snowboard, racket sports"
refraction_notes:
  - note: >
      ONE NAMED IDEAL = ITS OWN STRAND WITH ITS OWN MEASURE. Never collapse
      several ideals into one number. Shape ideals read body-composition and
      segmental lean mass; capability ideals read logged performance;
      movement-quality ideals (Pilates, yoga) read practice share and have no
      InBody signal at all. A strand whose measure is missing is carried as a
      direction with the gap named, never proxied by the nearest number.
    grade: D
  - note: >
      NAME THE NEIGHBOUR TO CHECK THE PICTURE. The fastest way to confirm a
      one-line picture is to say what it is not: X (legs judged) vs V (legs
      not judged); Pilates (controlled movement) vs core holds; CrossFit
      (breadth of output) vs balance/coordination; powerlifting (slow max
      force) vs weightlifting (speed); grappler (force, grip, isometric, may
      be heavy) vs striker (repeated bursts, lean at a class); sprinter
      (horizontal, clock) vs weightlifter (vertical, bar); cyclist (weight-
      supported, watts/kg, no bone loading) vs runner; dancer (range + jumps)
      vs Pilates (control, no jumps).
    grade: D
  - note: >
      THE HOLD TOKEN IS WRONG FOR ONE ROW AND PARTLY RIGHT FOR OTHERS.
      `zero_load_control_share_sets` counts timed isometric holds. That is
      the wrong proxy for Pilates (controlled movement) but a partial, honest
      measure where holding IS the work: climber hangs and lock-offs (046),
      grappler holds and carries (047), ski low-position holds (052). Name it
      as partial there; never as the Pilates measure.
    grade: D
  - note: >
      WEIGHT-SENSITIVE SPORTS SHARE ONE SAFETY STANCE. Striking combat (044),
      grappling / 씨름 (047), lightweight rowing (049), climbing (046, strength-
      to-weight), cycling (050, climbs) and dance (051, line) all carry a
      pressure toward a lower number; the sport categories and look are the
      user's goal, acute cuts and restriction are the caught route of
      exercise/harm-route-boundary-031, and the pack coaches the strength /
      skill side of the ratio.
    grade: D
claim: >
  Twenty-one body ideals cover what users usually name as "the body I want":
  three physique divisions (classic X, men's V, open), nine capability ideals
  (CrossFit-type work capacity, powerlifting, weightlifting/athletic power,
  endurance running, combat/striking, grappling/씨름, sprinter, rower,
  cyclist), four movement ideals (Pilates, yoga/mobility, calisthenics/
  gymnast, dancer), four sport-look ideals (swimmer, climber, ski/snowboard,
  racket sports) and the default healthy-lean / injury-free frame. Each is defined by the features that
  separate it from its neighbours, measured only by what this product can
  actually read, and combined with the others by explicit rules: shape strands
  share hypertrophy volume and a body-fat phase; capability strands add their
  own logged measure; movement strands add practice share and never compete
  for growth volume; energy direction (surplus vs deficit) and body-weight
  direction are where ideals genuinely pull apart.
reasoning: >
  A routing and synthesis row: every factual claim it relies on is carried by a
  graded archetype row (033-053; 046-053 added in pass 2). It exists because the failure the owner
  caught was not a missing fact about any one ideal but a flattening across
  them -- an X spoken as a V, a shape measured by one number, a movement
  practice measured as a hold.
---

# exercise/body-ideal-archetype-map-032 -- 몸의 지향(아키타입) 지도

## The archetypes, by family

| Family | Archetype (row) | One-line picture | Neighbour it is NOT |
|---|---|---|---|
| Shape | classic physique X (033) | 어깨-허리-허벅지 X자, 다리까지 심사 | V (legs not judged) |
| Shape | men's physique V (034) | 상체 V자, 과하지 않은 근육, 선명한 복근 | X; open |
| Shape | open bodybuilding (035) | 상한 없는 최대 근육 + 극도의 선명도 | classic (weight cap) |
| Capability | CrossFit / functional (036) | 무엇이든 해내는 다재다능한 체력 | balance/coordination ("연결") |
| Capability | powerlifting (040) | 3대 운동을 무겁게 드는 두꺼운 몸 | weightlifting (speed) |
| Capability | weightlifting / athletic power (041) | 폭발적으로 들고 뛰는 탄력 | powerlifting (slow force) |
| Capability | endurance (042) | 가볍고 숨이 오래가는 몸 | CrossFit (breadth) |
| Capability | combat / fighter (044) | 체급 안에서 폭발+지구력 반복 | CrossFit (no weight class) |
| Movement | Pilates (037) | 호흡에 맞춘 느리고 정확한 전 가동범위 움직임 | isometric core holds |
| Movement | yoga / mobility (039) | 넓고 편한 가동범위, 차분한 호흡 | Pilates (control from trunk) |
| Movement | calisthenics / gymnast (038) | 체중 대비 힘, 맨몸 기술 | physique (size) |
| Look+sport | swimmer (043) | 길고 넓은 어깨·등, 군살 없음 | men's physique (stage leanness) |
| Capability | grappler / 씨름 / wrestler (047) | 굵은 몸통·목, 악력, 들어 돌리는 엉덩이 힘 | combat/striking 044 (bursts, lean) |
| Capability | sprinter / athletic (048) | 탄력 있는 후면 사슬, 짧고 빠른 질주 | weightlifting 041 (vertical, bar) |
| Capability | rower (049) | 큰 체격, 넓은 등과 강한 다리, 큰 심폐 | endurance runner 042 (mass costs) |
| Capability | cyclist (050) | 가볍고 단단한 허벅지, 체중당 파워 | runner 042 (impact, bone) |
| Movement | dancer (051) | 통제된 넓은 가동범위 + 점프·회전 | Pilates 037 (no jumps) |
| Look+sport | climber / bouldering (046) | 체중 대비 강한 손가락·전완·등, 군살 없음 | calisthenics 038 (finger limiter, wall) |
| Look+sport | ski / snowboard (052) | 낮은 자세를 버티는 다리, 균형, 튼튼한 무릎 | sprinter 048 (eccentric, long effort) |
| Look+sport | racket sports (053) | 방향 전환하는 다리, 회전하는 몸통, 튼튼한 어깨 | sprinter 048 (multi-directional, one-sided) |
| Default | healthy-lean / injury-free (045) | 오래 다치지 않고 운동하는 탄탄한 몸 | -- (floor under all) |

## Measurement families (what this product reads)

- InBody: `body_fat_pct`, `skeletal_muscle_kg`, `body_weight` (registered
  strand tokens); segmental `lean_<arm_l|arm_r|trunk|leg_l|leg_r>_kg` and
  `_pct` (readable via `body-segment`, NOT strand tokens).
- Logs: `e1rm_<lift>`, `max_reps_<lift>` (registered prefixes, lead-compound
  slot), `weekly_sessions`, `unilateral_share_sets`,
  `zero_load_control_share_sets` (counts timed holds only), workouts
  `minutes` / `kcal` / `avg_hr` (readable, no strand token).
- Missing everywhere: girths (waist/shoulder/thigh/neck), ROM, pace/distance
  (run, swim, row, ride), jump/sprint/velocity/agility, skill level and
  climbing grade, controlled-tempo share, benchmark times, grip and finger
  strength (`grip_kg`, `hang_s_<edge>`), cycling power (`ftp_w_per_kg`),
  balance time, loaded carries.

## Combination rules

1. Shape + shape (X, V, open): one hypertrophy program; the regional
   distribution differs (V = upper bias, X = upper + legs, open = everything).
   The weight cap / "less muscular" ceiling are stage facts, not health targets.
2. Shape + capability: compatible at moderate conditioning doses. Concurrent
   training does not blunt whole-muscle growth or max strength; it blunts
   explosive strength (separate sessions) and running costs a little fibre
   growth (prefer cycling/rowing) -- item 042.
3. Anything + movement (Pilates / yoga): complementary; movement practice uses
   its own slot/block and its own measure and never takes growth volume.
   Controlled tempo within 0.5-8 s per rep costs no hypertrophy (item 037).
4. Real conflicts: energy direction (bulk vs cut vs endurance fuel), body
   weight direction (powerlifting/open/heavy-class 씨름 up; men's physique/
   calisthenics/endurance/combat/climbing/cycling down), and time budget.
   These go to the ORDER choice, not to a blended target.
5. Sport + gym (pass 2 rows 046-053): the sport itself (wall, mat, track,
   water, road, studio, slope, court) is the primary practice and its skill
   is not the gym's to teach; the gym strand supports it with strength where
   it transfers (squat to sprint, heavy strength to cycling economy), the
   injury-specific work each row names (finger, neck, hamstring, low back and
   ribs, bone, low back and energy, knee and wrist, shoulder and landing) and
   side balance for one-sided sports. Seasonal sports (ski/snowboard) enter
   as a pre-season block on top of the main ideal, not as a year-round body.
6. Rows that share a gym program: grappler + powerlifting + weightlifting
   (max force, hips); sprinter + weightlifting + classic X legs; rower +
   classic X / men's V back; climber + calisthenics; dancer + Pilates + yoga;
   racket + sprinter + healthy-lean. Rows whose shared program still has one
   real conflict: climber vs any mass ideal (strength-to-weight), cyclist /
   runner vs mass on climbs, grappler heavy class vs any leanness ideal.

## The owner's three together (classic X + CrossFit function + Pilates connection)

- X: hypertrophy with shoulders/lats AND legs; measured by
  `skeletal_muscle_kg` + segmental lean (legs vs arms vs trunk) + `body_fat_pct`
  for conditioning. Missing: waist/shoulder/thigh girths.
- Function: a lead strength lift (`e1rm_`), a bodyweight skill (`max_reps_`),
  and the `conditioning` / `mixed_circuit` / `power` picks. Missing: benchmark
  times, pace.
- Connection: controlled full-range movement with breath each session
  (roll-down / articulation, not hollow hold), `mobility_flow`; measured by a
  controlled-tempo share that does not exist yet. The existing
  `zero_load_control_share_sets` counts holds and is the wrong proxy.
- Pull-apart: only the energy phase (X building wants a surplus or recomp,
  conditioning volume raises the energy cost). Order it; do not average it.
