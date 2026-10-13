---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "스키 / 스노보드 잘 타는 몸" -- strong, eccentric-tough legs and hips, balance
# and a knee that survives a season. A seasonal, gear-bound sport: the gym
# ideal is mostly preparation and injury protection, and the injury pattern
# differs between skis (knee) and a board (wrist / upper limb).
id: exercise/ideal-ski-snowboard-052
domain: exercise
grade: B (systematic reviews -- ACL mechanisms by sport, snowboard wrist guards; review of balance training); C (narrative reviews -- ski racing and winter-sport knee injury); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2011-2025
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/40690162/"  # Sundberg A et al. Sports Med 2025 -- systematic review, 62 articles, 20 sports, 5,612 ACL injury situations: gear-induced ACL injuries in alpine skiing and board sports come from the long lever attached to the feet ('valgus-external rotation', 'slip and catch', 'tail landing')
  - "https://pubmed.ncbi.nlm.nih.gov/30689522/"  # Tarka MC et al. Sports Health 2019 -- alpine ski racing: high injury rate, knee most common, ACL the largest time loss; mechanisms slip-catch, dynamic snowplow, back-weighted landing; injury rate has not fallen despite proposed prevention
  - "https://pubmed.ncbi.nlm.nih.gov/36239771/"  # Rauch A et al. Orthopadie 2022 -- knee the most affected region in alpine skiing and snowboarding; prevention via targeted training and equipment adjustment; ~80% return to sport after ACL surgery
  - "https://pubmed.ncbi.nlm.nih.gov/22035394/"  # Kim S, Lee SK. Bull NYU Hosp Jt Dis 2011 -- systematic review (2 RCTs, 1 meta-analysis, 8 case-control): wrist injuries among the most common in snowboarding; wrist guards may protect
  - "https://pubmed.ncbi.nlm.nih.gov/21395364/"  # Hrysomallis C. Sports Med 2011 -- review: balance training improved downhill slalom skiing among other motor skills in prospective studies of non-elite subjects; resistance training beat balance training for jump and sprint
  - "exercise/ideal-sprinter-athletic-048"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE KNEE IS THE SKIER'S RISK, THE WRIST THE BOARDER'S. Pre-season work
      for skiers aims at the knee (strong quads and hamstrings, landing and
      single-leg control, not skiing back-weighted); for snowboarders it adds
      falling technique and wrist guards. Equipment (binding setup) is part of
      prevention and outside the gym.
    grade: B
  - note: >
      SEASONAL IDEAL = A PREP BLOCK, NOT A YEAR-ROUND PHYSIQUE. Most users
      naming this want to ski or ride better and not get hurt; offer a 6-8
      week pre-season block (leg strength, eccentric and isometric endurance,
      balance, conditioning) on top of their main ideal rather than a
      separate body target.
    grade: D
claim: >
  The ski / snowboard ideal is a body with strong, fatigue-resistant legs and
  hips that can absorb load eccentrically and hold low positions, fine balance
  and trunk control on an unstable surface, and a knee that stays out of bad
  positions. The knee is the most injured region in both sports and ACL
  injuries in skiing are gear-induced by the long lever on the foot; wrist
  injuries are among the most common in snowboarding and wrist guards may
  protect. Balance training can improve slalom skiing in non-elite athletes
  but does not replace strength training. It differs from the sprinter by the
  eccentric, low-position, long-effort demand, and from yoga/Pilates by the
  load and speed.
reasoning: >
  Mechanisms come from a large 2025 systematic review across sports; the
  racing and winter-knee pictures are narrative reviews. The wrist-guard
  finding is a 2011 systematic review whose own conclusion is cautious. The
  balance claim is a review of mostly non-elite prospective studies. The
  pre-season framing is craft.
---

# exercise/ideal-ski-snowboard-052 -- 스키 / 스노보드형

**한 줄 그림:** 낮은 자세를 오래 버티는 단단한 허벅지·엉덩이, 흔들려도 무너지지 않는 균형, 한 시즌을 다치지 않고 타는 무릎.

## Distinguishing features

Eccentric and isometric leg endurance in a flexed stance; balance on an
unstable surface; trunk and hip control; seasonal; knee (ski) vs wrist
(board) risk.

## Measurable here

- `e1rm_<squat>`, `e1rm_<split_squat>` (leg strength).
- `unilateral_share_sets` (single-leg control -- a real fit here).
- `zero_load_control_share_sets` -- partial: wall sits and low holds are
  timed holds.
- Ski days as workouts `minutes` (readable).

## Not measurable here

Balance time, jump/landing quality, leg endurance to failure in a squat
hold, ski/ride days per season. Proposed: `balance_s_single_leg`, `jump_cm`.

## Training emphasis and practice

A 6-8 week pre-season block: squats and single-leg work, eccentric
emphasis, wall-sit / low-position holds, lateral bounds and landing drills,
balance work, hamstring strength, intervals matched to a run. Snowboarders
add falling practice and wrist protection. Picks: `power`, `conditioning`,
`whole_body`.

## Failure modes

Arriving at the season untrained; skiing back-weighted when fatigued late in
the day; ignoring binding setup; wrist fractures on falls without guards.

## Combines / conflicts

Layers onto almost any ideal as a seasonal block; aligns with the classic X
legs, the sprinter and CrossFit-type work capacity. No real conflict except
time and a deep cut in-season.
