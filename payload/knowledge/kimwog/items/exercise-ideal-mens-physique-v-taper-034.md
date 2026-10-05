---
# Body-ideal archetype sprint 2026-09-30. Filed next to
# exercise/ideal-classic-physique-x-taper-033 on purpose: the V is the shape the
# agent wrongly gave for the X, so the two rows state their boundary against
# each other.
id: exercise/ideal-mens-physique-v-taper-034
domain: exercise
grade: A (rule -- federation judging criteria); D (training translation)
lane: "@gym-craft"
locale: universal
as_of: 2021-2026
contested: no
sources:
  - "https://ifbb.com/wp-content/uploads/2021/04/Mens-Physique-Rules-2021-.pdf"  # IFBB Rules Section 9, Men's Physique & Muscular Men's Physique -- 'less muscular, yet athletic and aesthetically pleasing physique'; Art. 6.1 opaque loose board shorts covering the whole upper leg to the patella; Art. 10.1 proper shape and body proportions, balanced muscularity, 'extreme muscularity and definition should be marked down'; quarter turns, no mandatory muscle poses
  - "https://www.ifbbpro.com/rules/"  # IFBB Pro League: men's physique judged in front/back quarter turns
  - "https://www.ifbbproleague.com.au/uploads/b/994ea660-d8aa-11ed-9014-378d597f6cc4/Judging%20Criteria%20-%20Mens%20Physique.pdf"  # IFBB Pro League Australia judging criteria: small waist + wide shoulders for the front V, wide lat spread for the back V, visible abs/obliques/serratus
  - "exercise/ideal-classic-physique-x-taper-033"
  - "source:nutrition/body-composition-measurement-floor-011"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE V STOPS AT THE HIPS BY RULE, NOT BY TASTE. Board shorts cover the
      whole upper leg, so legs are not scored in this division. That is a
      statement about the stage, not advice to skip legs: a user who says
      "men's physique body" still gets a full-body program for health and for
      the lower back; only the SHAPE target is upper-body.
    grade: A
  - note: >
      "LESS MUSCULAR" IS PART OF THE DEFINITION. Extreme muscularity and
      definition are marked down. A user chasing this picture has a ceiling on
      size that classic and open do not; past it, more mass moves them toward
      muscular men's physique or classic, not toward a better V.
    grade: A
claim: >
  Men's physique is an upper-body V: wide shoulders and a wide upper back
  (visible lat spread from behind) tapering to a small waist, with full but not
  extreme muscularity, visible abdominal definition, and overall athletic
  proportion, judged in quarter turns while wearing loose board shorts that
  cover the whole upper leg. Legs are not scored, extreme muscularity and
  definition are marked down, and there are no mandatory muscle poses.
reasoning: >
  IFBB rule text (Section 9, Art. 6.1 and 10.1) states both the attire and the
  mark-down, and the IFBB Pro League Australia judging-criteria sheet states the
  front and back V. The rule text is definitional, hence the rule grade; how to
  train for it is practitioner translation (shoulder and lat width priority,
  trunk leanness, arms in proportion), graded as craft.
---

# exercise/ideal-mens-physique-v-taper-034 -- 멘즈 피지크 (V-taper)

**한 줄 그림:** 넓은 어깨와 등이 잘록한 허리로 좁아지는 상체 V자, 선명한 복근, 과하지 않은 근육.
다리는 보드쇼츠에 가려 심사하지 않는다.

## Distinguishing features

- Upper-body V from the front (delts over a small waist) and from behind (lat
  spread). Abs, obliques, serratus visible.
- "Less muscular, yet athletic": extreme muscularity is marked down.
- Neighbour boundary: classic physique (033) adds the lower half of the X --
  legs scored, more mass allowed under a weight cap.

## Measurable here

- `body_fat_pct` -- the abs-visible conditioning strand; matters more here than
  in any other physique archetype because the midsection is the centre of the
  picture.
- `skeletal_muscle_kg` -- total muscle; beyond a point, more is not better here.
- Segmental `lean_arm_*_kg` / `lean_trunk_kg` vs `lean_leg_*_kg` -- upper-body
  share (readable via `body-segment`, not a strand token).
- Workout logs: weekly sets for side delts / lats / upper chest; e1RM of a lead
  press or pull.

## Not measurable here

Shoulder-to-waist ratio, waist circumference, lat width by eye. No token for any
of them. Do not stand body fat in for the V.

## Training emphasis and practice

Hypertrophy with an upper-body regional bias (lateral and rear delts, lats,
upper chest, arms in proportion), a lean phase to show the midsection. Legs are
trained for health, not for the stage. No practice pick is intrinsic to it.

## Failure modes

- Neglecting legs and posterior chain entirely (health and knee/back cost, and
  it closes the door on the X later).
- Over-cutting for abs (harm-route-boundary-031, extreme cut).
- Over-building the waist with heavy loaded oblique work is a stage concern
  only; there is no graded evidence that normal trunk training widens the waist.

## Combines / conflicts

Compatible with functional conditioning and Pilates. Conflicts with open
bodybuilding (mass ceiling) and with a powerlifting total goal (a lean V and a
heavy total pull body weight in opposite directions).
