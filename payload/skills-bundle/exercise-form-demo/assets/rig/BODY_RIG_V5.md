# body_rig_v5 — rebuilt deformation layer

Canonical rigged bodybuilder body for the exercise form-demo pipeline. The MESH
(proportions, muscle targets, skin material, mid-thigh drawers) is the approved
`n4_dl_start.py` look, unchanged. What was REBUILT is the deformation layer:
skeleton, skin weights, skinning method, corrective helpers — to fix the deep-pose
failures the owner flagged (knee folding wrongly, hands collapsing into blobs).

## Files
- `assets/rig/body_rig_v5.blend` — the ready-to-pose scene (body + drawers + rig).
- `scripts/32_build_v5.py` — headless rebuild from scratch → the .blend above.
- `scratch/rigv5_lib.py` — shared build / deform / pose / render helpers.
- `scratch/rigv5_battery.py` — acceptance-battery poser + renderer.
- `scratch/rigv5_battery/` — battery renders (nude, to expose joint deformation).
- `scratch/rigv5_battery_asset/` — spot-check renders posed FROM the saved .blend
  (drawers on) to prove the asset is valid and poseable.

  NOTE (pack carry-in 2026-09-12): the two render dirs above and the A/B dirs
  cited below (`scratch/rigv5_ab/`) are BUILD OUTPUT and did not ship with the
  pack -- see SKILL.md "what did NOT ship". The battery SCRIPTS did ship; run
  `rigv5_battery.py` / `rigv5_detail_ab.py` (commands at the bottom of this file)
  to regenerate the images before citing them as evidence.

## Objects in the .blend
- `body_v5`         — the skin mesh (19,158 verts), armature-parented.
- `body_v5.rig`     — the armature (MPFB "default" rig, 163 bones).
- `shorts`          — mid-thigh drawers; weight-transferred from the body, parented
                      to the rig, ARMATURE + SHRINKWRAP(OUTSIDE, 5mm) so cloth stays
                      outside the skin under big joint rotations.

## Rig = MPFB "default" (MakeHuman) skeleton
Full deform skeleton incl. per-finger chains + metacarpals (the hands are driven by
the NATIVE armature, not the old custom manual-LBS grip solver that blobbed).
Up = +Z, front = −Y, arms along the body sides in bind (A-pose), `.L` = +X.
Rotation mode is set to XYZ Euler on every pose bone.

Key deform bones (per side, `.L` / `.R`):
- leg:   `upperleg01`, `upperleg02`, `lowerleg01`, `lowerleg02`, `foot`, `toe{1..5}-{1..3}`
- spine: `root` (pelvis), `spine01..05`, `neck01..03`, `head`
- arm:   `clavicle`, `shoulder01`, `upperarm01`, `upperarm02`, `lowerarm01`, `lowerarm02`, `wrist`
- hand:  `metacarpal{1..5}`, `finger{1..5}-{1..3}` (finger1 = thumb)
- (also a full face rig — unused by the pipeline.)

Joint-angle conventions are measured at runtime, never assumed (see
`rigv5_lib.flex_sign` / `curl_sign` / `faceY`): the sign that FLEXES a joint is
detected by probing ±20° and keeping the direction that reduces the relevant
head-to-head distance. This keeps posing robust to MakeHuman's bind orientation.

## Deformation recipe (this is the fix)
Modifier stack on `body_v5`, top → bottom:
1. `ARMATURE`  with **`use_deform_preserve_volume = True`** (dual-quaternion
   skinning). This is the single biggest win: it stops the linear-blend collapse
   at the knee and elbow — the kneecap/joint keeps volume in deep flexion instead
   of creasing inward.
2. `CORRECTIVE_SMOOTH`  (rest_source = `ORCO`, `LENGTH_WEIGHTED`, factor 0.6,
   12 iters) **MASKED to a joint-ring vertex group** (`cs_joint_mask`). Relaxes
   the residual linear-blend pinch at deep folds (knee / elbow / shoulder / hip /
   wrist / finger creases) while leaving muscle BELLIES untouched. An UNMASKED
   whole-body corrective smooth was the round-1 "smooth mannequin" regression;
   masking it restores full n4 muscle separation (A/B: `scratch/rigv5_ab/
   detail_ab_v5.png` vs `detail_ab_n4.png` — indistinguishable). ORCO =
   pre-deform coords as rest, so no bind step.
3. `SUBSURF`  (levels 1 / render 2) — the approved smoothing, unchanged.

### The joint mask (`rigv5_lib.build_joint_mask`)
Weight per vertex = "jointness": for each true anatomical joint (a child deform
bone + its ACTUAL armature parent — hip `upperleg01/pelvis`, knee `lowerleg01/
upperleg02`, ankle, shoulder `upperarm01/shoulder01`, elbow `lowerarm01/
upperarm02`, wrist, and every finger MCP/PIP/DIP) the crease ring is exactly the
verts that straddle BOTH bones, so `min(w_child, w_parent)` marks it. Max over
all joints, ×2 and clamped to 1. Mid-limb segment bones (`upperleg02`,
`upperarm02`, …) are deliberately EXCLUDED so thigh / bicep / chest / ab bellies
stay at weight 0 → full detail.

Weights: MPFB "default" MakeHuman weights, `normalize_all` + `limit_total(4)`
(≤4 bone influences per vert). No hand weight-painting was needed — the stock
per-finger weights deform cleanly once preserve-volume is on.

### What was tried and rejected
- Plain linear-blend skinning (the old default): knee collapses to a sharp pinch
  in deep flexion. REJECTED — this is the reported bug (A/B: `scratch/rigv5_ab/`).
- Aggressive weight-smoothing / per-vertex hand repair: unnecessary. The blob
  hands were NOT a weight problem; they came from the old pipeline's custom
  manual-LBS grip solver (`pos_of`, which ignored the metacarpals). Driving the
  hands with the native armature fixes it with zero weight work.
- Rigify / other standard rigs: not needed; the default rig deforms well once the
  skinning method + corrective smooth are set. Not adopted (added complexity, no
  measured benefit for these poses).

## Posing the asset
Open the .blend, grab `body_v5.rig`, set `pose.bones[...].rotation_euler`. For a
readable planted-feet squat/hinge use IK feet-pinning (see `rigv5_battery.py`:
`setup_leg_ik` + drop the armature object's Z + `level_feet`). Deformation quality
depends only on the joint ANGLES, so FK-at-the-target-angles already exercises the
deform; feet-planting is purely presentational (and is the motion pipeline's job).

Grip: `rigv5_lib.wrap_grip(arm, side, axis_pt, axis_dir, R)` curls fingers 2–5
around a cylinder until each segment's tail reaches the surface (R + ~9mm flesh),
then sets an opposed thumb. Validated on a Ø28 mm (R = 0.014) bar.

## Known limits (honest)
- Full elbow flexion is now CAPPED at ~135° in the battery pose (a muscular arm
  physically cannot close further — bicep meets forearm). Combined with the masked
  corrective smooth, the antecubital fold now reads as compressed flesh (a soft
  dimple), not the round-1 knife-edge V-notch + spike. Still the softest joint; a
  JCM-style corrective shape key could tighten it further if ever wanted.
- The DRAWERS tear / speckle at the deep hip fold (squat & hinge `hip_crease`
  crops): the cloth SHRINKWRAP self-intersects at the sharp glute/inseam fold,
  opening a small jagged slit. This is a CLOTH artifact, out of the deformation-
  layer scope — the body hip-crease deform underneath is sound. A proper cloth-sim
  pass (motion pipeline) would resolve it.
- Face is featureless MPFB base (no eyes/brows) — same as the approved look. Note:
  the round-1 dark "oval" on the forehead was a highlight-clip artifact of an
  over-bright exposure, fixed by dialing exposure to −2.2 under Standard.

## Fixed since round 1
- Muscle-detail wash → masked corrective smooth (belly detail preserved; A/B proven).
- Elbow knife-notch → masked CS + 135° cap → soft compressed-flesh crease.
- Lumpy finger joints → masked CS on finger rings; per-finger fist wrap kept.
- Floating / converging / plantar-flexed feet in squat & hinge → PLANTED: ankles
  IK-pinned hip-width at floor height, hips dropped via the ROOT BONE (not the
  whole armature), soles restored to their standing world orientation (flat).
- Battery now: dark studio + Standard view transform, drawers ON, feet planted,
  EEVEE 384 samples (no speckle), both from-script and from-asset variants.

## Regenerate
    blender --background --python scripts/32_build_v5.py
    # → assets/rig/body_rig_v5.blend

## Re-run the acceptance battery
    # from-script (drawers on, planted feet, dark studio, Standard, 384 spp):
    blender --background --python scratch/rigv5_battery.py -- squat hinge grip curl stand
    # from the saved asset (spot-check the asset is valid + poseable):
    blender --background --python scratch/rigv5_battery.py -- asset squat grip curl
    # muscle-detail A/B (v5 masked-CS body vs approved n4 body, same cam+lights):
    blender --background --python scratch/rigv5_detail_ab.py -- n4
    blender --background --python scratch/rigv5_detail_ab.py -- v5
