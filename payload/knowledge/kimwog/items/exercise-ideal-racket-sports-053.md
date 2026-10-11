---
# Body-ideal archetype sprint, pass 2 (owner ask 2026-09-30 19:57/20:02).
# "테니스 / 배드민턴 / 스쿼시 치는 몸" -- quick, agile, a strong shoulder and
# trunk rotation, the legs to change direction for an hour. One row for the
# three racket sports: they share the movement profile (repeated short
# sprints, lunges, rotation, overhead strokes); they differ in load on the
# shoulder (tennis serve) and in landing (badminton jump smash).
id: exercise/ideal-racket-sports-053
domain: exercise
grade: B (large cohort -- mortality association; systematic reviews -- tennis injuries, overhead shoulder, ACL mechanisms); C (narrative review -- badminton; single study -- arm asymmetry); D (archetype picture and gym translation)
lane: "@performance-lit"
locale: universal
as_of: 2004-2025
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/27895075/"  # Oja P et al. Br J Sports Med 2017 -- 80,306 adults: racquet sports associated with lower all-cause (HR 0.53) and CVD (HR 0.44) mortality, the largest association among the sports studied; observational
  - "https://pubmed.ncbi.nlm.nih.gov/16632572/"  # Pluim BM et al. Br J Sports Med 2006 -- systematic review of tennis injuries: incidence varies widely; most injuries in the lower extremities, then upper extremities, then trunk; very few cohort studies of risk factors; no prevention RCTs
  - "https://pubmed.ncbi.nlm.nih.gov/32758080/"  # Tooth C et al. Sports Health 2020 -- systematic review, overhead athletes: previous injury, ROM deficit or excess, rotator cuff weakness and training load raise shoulder-injury risk
  - "https://pubmed.ncbi.nlm.nih.gov/40690162/"  # Sundberg A et al. Sports Med 2025 -- landing causes 57-82% of ACL injuries in overhead sports such as volleyball and badminton
  - "https://pubmed.ncbi.nlm.nih.gov/32399141/"  # Pardiwala DN et al. Indian J Orthop 2020 -- review of elite badminton: fastest racquet sport; overuse plus non-contact joint and muscle-tendon injuries from sudden direction changes
  - "https://pubmed.ncbi.nlm.nih.gov/15207895/"  # Sanchis-Moysi J et al. Maturitas 2004 -- postmenopausal tennis players: 8% more bone mineral content in the dominant arm, scaling with years played; arm muscle mass not different
  - "exercise/ideal-sprinter-athletic-048"
  - "exercise/ideal-healthy-lean-injury-free-045"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE RACKET SPORT IS ALSO A HEALTH CHOICE. In a large cohort, playing
      racquet sports carried the lowest all-cause and cardiovascular
      mortality hazard of the sports studied. It is observational (players
      differ from non-players), but it means a user whose ideal is "keep
      playing tennis into old age" is aligned with the healthy-lean default
      (045), and the strand's job is keeping them on court: shoulder, knee
      and ankle robustness plus conditioning.
    grade: B
  - note: >
      ONE-SIDED SPORT, TWO-SIDED GYM. The dominant arm gains bone with years
      played; the shoulder's modifiable risks are range (too little or too
      much), rotator cuff weakness and load. Gym work balances the sides and
      strengthens the cuff; it does not copy the stroke with weights.
    grade: B
claim: >
  The racket-sports ideal is a quick, agile, well-conditioned body: legs that
  accelerate, lunge and change direction repeatedly for an hour or more, a
  strong trunk that transfers rotation, and a robust hitting shoulder. Most
  tennis injuries are in the lower limbs, overhead shoulder injuries track
  range-of-motion faults, rotator cuff weakness and load, and in badminton
  landing is the dominant ACL mechanism. Racquet-sport players in a large
  cohort had markedly lower all-cause and cardiovascular mortality. It
  differs from the sprinter by repeated multi-directional efforts and the
  one-sided upper body, and from endurance by the intermittent,
  reaction-driven profile.
reasoning: >
  The mortality association is a large pooled population cohort (not causal).
  Tennis injury distribution is a 2006 systematic review whose own authors
  note weak risk-factor evidence; the shoulder risk factors come from a 2020
  systematic review of overhead athletes (tennis among them). Badminton
  evidence is a narrative review plus the 2025 ACL mechanism review. Squash
  has no dedicated source here (GAPS). Picture and translation are craft.
---

# exercise/ideal-racket-sports-053 -- 라켓 스포츠형 (테니스 / 배드민턴 / 스쿼시)

**한 줄 그림:** 가볍게 튀어나가고 방향을 바꾸는 다리, 회전을 싣는 몸통, 오래 휘둘러도 탈 없는 어깨 -- 한 시간을 뛰고도 지치지 않는 몸.

## Distinguishing features

Repeated short multi-directional sprints and lunges; rotational power; a
robust dominant shoulder; intermittent conditioning; reaction and footwork.

## Measurable here

- `unilateral_share_sets` (lunges, single-leg landing -- a real fit).
- `e1rm_<split_squat>` / `e1rm_<squat>`; `weekly_sessions`.
- Segmental `lean_arm_l_kg` vs `lean_arm_r_kg` (readable; side balance, not a
  strand token); matches as workouts `minutes`, `avg_hr`.

## Not measurable here

Agility / change-of-direction time, sprint time, shoulder rotation range,
rotator cuff strength, match play time. Proposed: `agility_s_<test>`,
`sprint_s_<distance>`, `rom_<joint>_deg`.

## Training emphasis and practice

Court time first. Support: lower-body strength and single-leg work, landing
and deceleration drills, rotator cuff and scapular strength, shoulder range
kept (not lost to one-sided play), rotational trunk power (med-ball throws),
intervals mirroring rallies. Picks: `power`, `conditioning`, `whole_body`.

## Failure modes

Shoulder overuse from serve/smash volume without cuff work; ankle sprains and
knee (landing) injuries; tennis-elbow-type overuse; playing through fatigue
with no strength work.

## Combines / conflicts

Aligns with healthy-lean (045), the sprinter and CrossFit-type fitness;
Pilates and yoga complement (trunk, range). Conflicts with open
bodybuilding and powerlifting mass only through agility and time.
