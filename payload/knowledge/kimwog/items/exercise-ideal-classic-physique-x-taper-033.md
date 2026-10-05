---
# Body-ideal archetype sprint 2026-09-30 (owner ask 19:53). The owner named
# "클래식 피지크 X-taper" as one of three ideals in his goal consult and the
# agent described it as a V-taper (legs missing) measured by body fat alone
# (skeletal muscle and segmental lean mass missing). This row is the
# correction: what the division actually judges, which of it this product can
# read, and which it cannot. Map + combination rules live in
# exercise/body-ideal-archetype-map-032; the machine table is
# payload/service/health/body_ideal_archetypes.json.
id: exercise/ideal-classic-physique-x-taper-033
domain: exercise
grade: A (rule -- federation judging criteria); D (training translation)
lane: "@gym-craft"
locale: universal
as_of: 2023-2026
contested: no
sources:
  - "https://ifbb.com/wp-content/uploads/2023/02/Mens-Classic-Physique-2023.pdf"  # IFBB Rules, Men's Classic Physique 2023 -- Art. 3 height-weight caps (Max kg = height cm - 100 + 4..17 by class); Art. 10.1 downward survey incl. thighs, legs, calves, glutes, hamstrings; Art. 10.2 'harmonious, classical physique', broad shoulders, limbs and trunk in good proportion
  - "https://www.ifbbpro.com/rules/"  # IFBB Pro League rules: Classic Physique mandatory poses (front double biceps, side chest, back double biceps, abdominals and thighs, favourite classic pose -- no most muscular), height/weight caps, judging 100%
  - "https://anbfnatural.com/classic-physique-guidelines/"  # ANBF (natural federation) classic physique guidelines: the classic X frame -- broad shoulders, small waist, quadriceps sweep, hamstring definition
  - "https://www.naturalbodybuilding.com/categories/male-categories/"  # natural federation category text: men's physique board shorts 'cut the X in half'; classic judges legs
  - "source:nutrition/body-composition-measurement-floor-011 -- InBody is a trend instrument, not an absolute figure"
  - "exercise/volume-doseresponse-007"
  - "exercise/regional-hypertrophy-exists-010"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      X IS NOT V. The distinguishing feature against men's physique is the LOWER
      half of the X: the thighs flare out again below a small waist (quad sweep,
      hamstring and glute detail, calves), and the legs are scored. A picture
      that says only "wide shoulders, narrow waist" has described men's physique.
      Never let the one-line picture drop the legs.
    grade: A
  - note: >
      BODY FAT ALONE CANNOT TRACK AN X. Leanness is one of the division's
      criteria (conditioning), but the X is built from muscle placed in specific
      regions. The measurable proxies here are skeletal_muscle_kg for total
      muscle and the InBody segmental lean readings (lean_leg_l/r_kg vs
      lean_arm_l/r_kg vs lean_trunk_kg) for where it sits; body_fat_pct is the
      conditioning strand, not the shape strand. A segmental reading is lean
      tissue, not shape: it cannot see the waist width, the shoulder width or
      the sweep of a quad.
    grade: D
  - note: >
      THE WEIGHT CAP IS A DESIGN FACT OF THE DIVISION, not a health target. The
      federation caps stage weight by height (roughly height-in-cm minus 100
      plus a class allowance). It exists to keep the division from becoming open
      bodybuilding. Do not turn it into a user's body-weight goal; quote it only
      when the user asks what the division allows.
    grade: A
claim: >
  Classic physique is judged on the whole body as an X: broad shoulders and
  upper back, a small waist, and thighs that flare out again below it, with the
  legs (quadriceps sweep, hamstrings, glutes, calves) scored alongside the upper
  body, in a harmonious proportion where no single part dominates, at stage
  leanness, under a height-indexed body-weight cap that keeps total mass below
  open bodybuilding. It differs from men's physique (upper-body V judged in
  board shorts, legs not judged, extreme muscularity marked down) by the legs
  and by accepting more muscle, and from open bodybuilding by the weight cap and
  the priority of proportion over maximal mass.
reasoning: >
  The definition is the federation's own rule text (IFBB Men's Classic Physique
  rules Art. 10.1-10.2 and Art. 3; IFBB Pro League rules), which is why the
  definitional half carries the rule grade: it is what the division is, not a
  finding about it. The downward survey in Art. 10.1 explicitly includes thighs,
  legs, calves, glutes and the hamstring group, and the mandatory poses include
  "abdominals and thighs" and back poses that show the legs; the board-shorts
  attire of men's physique covers the whole upper leg (IFBB Men's Physique Art.
  6.1), which is the structural reason the X exists only in classic. The
  training translation (regional volume across shoulders, back width, and legs;
  waist kept small by not over-building the obliques; measure by segmental lean
  mass) is practitioner craft built on the regional-hypertrophy and volume items
  already in this warehouse, hence its lower grade.
---

# exercise/ideal-classic-physique-x-taper-033 -- 클래식 피지크 (X-taper)

**한 줄 그림:** 넓은 어깨·등 → 잘록한 허리 → 다시 벌어지는 허벅지(대퇴 스윕)까지, 위아래가
균형 잡힌 X자 몸. 다리도 심사한다.

## What it is (and what it is not)

- The X has two halves. Upper: shoulder width (side delts), back width (lats),
  a high full chest. Lower: the thighs sweep outward again below the waist, with
  hamstring/glute detail and calves. The waist is the crossing point and is kept
  small.
- Legs are judged. The mandatory poses include "abdominals and thighs", and the
  judge's downward survey includes thighs, calves, glutes and hamstrings.
- Proportion over size: "harmonious, classical physique", limbs and trunk in good
  proportion. More muscle than men's physique is welcome; open-class mass is
  capped out by a height-indexed weight limit.
- Neighbours: men's physique = the upper half of this X only (board shorts hide
  the legs, extreme muscularity is marked down). Open bodybuilding = no weight
  cap, maximal mass and conditioning, "most muscular" pose allowed.

## What this product can measure

- `skeletal_muscle_kg` (InBody) -- total muscle; the "is the frame filling out"
  strand. Registered kit token.
- Segmental lean mass `lean_arm_l_kg` / `lean_arm_r_kg` / `lean_trunk_kg` /
  `lean_leg_l_kg` / `lean_leg_r_kg` (+ the sheet's `lean_<seg>_pct` of standard)
  -- the one reading that sees *where* the muscle is, including the legs the
  V-taper framing forgot. Readable via `body-segment`; NOT yet a goal token a
  strand can own.
- `body_fat_pct` -- conditioning only. Needed, never sufficient.
- `body_weight` -- relevant only against the division cap if the user competes.
- Workout logs: weekly sets per region (shoulders/back/legs balance), e1RM of a
  lead leg compound (`e1rm_<lift>`), unilateral share.

## What it cannot measure here

Waist circumference, shoulder width, thigh girth, shoulder-to-waist ratio, the
visual sweep of a quad, symmetry left vs right by eye -- none has a token. Girths
could be logged by hand if the kit grew `waist_cm` / `thigh_cm` / `shoulder_cm`
tokens; photos are outside the instrument. Say this plainly rather than proxy it
with body fat.

## Training emphasis and practice

Hypertrophy programming with a regional distribution: side/rear delts and lats
for the upper X, quads (incl. sweep-biased work), hamstrings, glutes and calves
for the lower X, trunk trained for function without over-building the waist.
Program-engine fit: the objective is `band_center` (growth) during building,
`functional` during a cut; the regional balance is the design input. Fits the
practice menu weakly -- this is a volume-distribution goal, not a practice pick.

## Failure modes and risks

- Upper-body-only programming (the V mistake) -- leaves the X half-built.
- Chasing the stage look with extreme cuts, dehydration or drugs -- caught by
  exercise/harm-route-boundary-031.
- Reading a single InBody number as progress toward a shape (see
  nutrition/body-composition-measurement-floor-011: trend, not absolute).

## Combines / conflicts

- With functional (CrossFit-type) work: compatible if conditioning is dosed; a
  large running volume carries a small interference cost on muscle growth
  (exercise/ideal-endurance-runner-triathlete-042).
- With Pilates: complementary -- Pilates supplies controlled full-range movement
  and trunk control, not muscle size; it does not compete for the growth strand.
- With men's physique: a subset. With open bodybuilding: diverges at the cap.
