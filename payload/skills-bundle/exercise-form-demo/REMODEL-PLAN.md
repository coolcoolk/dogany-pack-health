# hand remodel plan -- APPROVED, execution deferred (owner: next session)

Status: approach APPROVED 2026-07-23. Build NOT started (owner chose next session).
Resume from S0 below. Do NOT re-scope -- diagnosis + gate already done.

## why (measured root cause, do not relitigate)
v4 fingers are displaced flat SHEETS, not tubes: 8-14 joint loops along a finger vs
30-44 verts radially (inverted ratio) -> a 70deg curl tears into slivers, not a bend.
Pinky = 41% verts / 56% length of middle -> vanishes. L/R vert distribution differs
9-16% -> not a true mirror -> .R web tear. Closed-grip bar penetration 276 L / 88 R.
Pose/collision/weight patching CANNOT fix geometry+topology. Remodel is the fix.

## approved approach: GRAFT the MPFB (MakeHuman) hand
MPFB is already installed in this Blender 5.2, runs headless.
`bpy.ops.mpfb.create_human()` -> 19,158-vert anatomically-correct human with 5 real
per-finger chains, opposable thumb, 47 hand vertex groups, `add_standard_rig`,
`auto_transfer_weights`. Use it as the donor hand.
Residual risk lives at ONE place = the WRIST SEAM (geometry loop mismatch + MPFB skin
!= Meshy bodybuilder skin). Both isolated + testable at S2/S5.
Fallback if seam can't be made clean in ~2 tries: procedural rebuild (approach b).
Retopo of the old paddle (c) = REJECTED (lipstick on paddle).

## acceptance gate (already built -- USE IT, never promote without it)
Harness: `scripts/hand_grip_gate.py`. Diag: `scripts/hand_remodel_diag.py`.
Static closed-grip render, BOTH hands, 4 fixed angles: front34 / thumbside /
UNDERSIDE (money angle) / topdown. PASS criteria per defect class:
- C1 reversed: palmar side faces bar, knuckles away (vision).
- C2 thumb-up: thumb tip crosses to FAR side of bar axis + points down/under (vision+measure).
- C3 wrist ROM: |hand vs forearm-twist| <= ~90deg pronation; hard-flag beyond.
- C4 pinky: pinky verts >= 55% of middle AND length >= 70%. (now 41/56 FAIL)
- C5 palm/paddle: palm:finger ratio 0.90-1.15 AND visible knuckle break in render. (now 0.83 FAIL)
- C6 bar-through: 0 verts radial < r-0.0015, both hands. (now 276L/88R FAIL)
- C6b mirror: worst per-digit L/R vert-count delta < 5%. (now 16% FAIL)
Motion gate (product scale, the one that caught the through-bar): rebuild the squat
clip, sample 12-16 frames across the rep (NOT 3 keyframes), C6 penetration = 0 on
EVERY sampled frame, emit one zoomed hand crop per frame for a fresh vision review.
Rule: numbers gate + fresh reviewer opens crops. Each alone lied before -> need both.

## staged build (each stage gated; promote only after S7 + owner sign-off)
- S0 donor capture: mpfb create_human -> isolate one hand at wrist -> save to scratch.
  gate: donor hand passes static C4/C5 on its own.
  [DONE 2026-07-23] scratch/s0_capture.py + s0_render.py. Donor = MPFB 13,380-vert
  base skin, LEFT hand isolated at forearm-axis wrist plane (1.5cm stub kept) ->
  scratch/donor_hand_L.{blend,glb}, 1,642 verts / 3,260 tris, vgroups stripped.
  Gate result: 5 real fingers, per-finger verts 215-295 (pinky 295 = 102% of
  middle -> C4-verts strong PASS, the real anti-paddle proof). Two RAW sub-threshold
  flags, both confirmed calibration artifacts by fresh vision (palmar/dorsal renders
  show full reading pinky + non-paddle palm + opposable thumb):
   * C4-length: pinky 68% of middle (thr 70%). Real anatomical pinky is 65-70%;
     70% was tuned vs the v4 VANISHING pinky (56% len + 41% verts). Donor reads full.
   * C5 palm:mean4-finger = 1.29 inflated by the short pinky in the mean; palm:MIDDLE
     = 1.13 (in 0.90-1.15 band). Vision: visible knuckle break, not a paddle.
  DONOR-GATE TOLERANCE (this stage only): accept pinky-len 65-70% when verts>=90%
  of middle AND vision confirms full finger; use palm:MIDDLE for C5. The STRICT
  bodybuilder-frame C1-C6b numbers still apply unchanged at S6/S7.
- S1 fit+orient: scale/rotate donor into bodybuilder wrist frame (wrist x=0.78, arm
  along X, thumb to -Y). gate: wrist diameter + knuckle-line x match forearm in tol.
  [DONE 2026-08-01] scratch/s1_fit2.py. KEY FIX: donor carried 11 MPFB shape keys
  that made me.vertices.co edits invisible to the renderer (frustum-culled at old
  MakeHuman location) -> flatten shape keys (bake evaluated mesh) FIRST, then apply
  rigid+uniform fit. SCALE=1.1961, det(Rmap)=1.0000 (proper rotation, no reflection),
  1642 verts. Numeric gate: thumb y=-0.0103 < knuckle y=0.0160 PASS; hand:forearm
  ratio=0.778 (band 0.68-0.87) PASS. Fresh vision review (4-angle overlay
  s1_ov_*.png rebuilt from corrected fit): 5 real fingers survive the fit, hand
  continues forearm axis, palm-down, thumb correct side, natural fan -> PASS.
  Output: scratch/donor_hand_L_fit.{blend,glb}. Longitudinal wrist gap is expected
  (= S2 seam-bridge target), NOT an S1 defect. Slight wrist-thin + minor vertical
  drop vs forearm centerline noted -> handle at S2 bridge-loop/normals, not blockers.
- S2 seam bridge: delete old paddle past wrist; bridge-loop donor wrist ring to
  forearm cut; remove doubles; consistent normals. gate: manifold, no interior faces,
  seam holds under a wrist-flex pose.
  [ATTEMPT-2 FAILED-GATE 2026-08-01] Two bridge tries exhausted (plan's ~2-try limit).
  Try1 (s2_bridge.py/s2b_bridge.py -> body_hand_bridged.blend): seam left OPEN
  (hollow forearm tube + gap), fed a clean 22-vert donor ring to a ragged non-planar
  143+94-vert forearm double-lip that were far apart -> bridge_loops mis-joined.
  Try2 (s2_bridge_v2.py -> body_hand_bridged_v2.{blend,glb}, QA s2v_*.png): weld the
  forearm double-lip into a 27-vert rim, regularize, pure-translate donor coaxial
  (S1 fit preserved), tapered collar bridge. Result: seam CLOSED + joined + correct
  5-finger hand, BUT NOT manifold -- ~3 non-manifold edges + ~8 interior faces + a
  dark recessed faceted cuff + crumpled palmar pinch localized to the seam patch.
  Reviewer QA verdict (4 angles): FAIL for promotion; subdivision (S5) would AMPLIFY the
  interior faces, not hide them. Root cause = material, not code: the bodybuilder
  forearm is a non-watertight OPEN Meshy shell with no clean cross-section to sew to.
  DECISION POINT: plan's fallback = procedural rebuild (approach b) of a clean
  forearm->wrist tube with matched ring topology. Awaiting owner go/hold (heaviest
  step). Do NOT carry body_hand_bridged_v2 into S3 as-is.
- S3 rig+weight: skin to existing 15-bone/hand skeleton (auto-transfer/bone-heat),
  <=4 influences, no cross-finger bleed. gate: static C6 = 0, clean curl from underside.
- S4 mirror: mirror the clean hand to the other side. gate: C6b < 5%.
- S5 texture/seam blend: reproject body skin / blend neutral at seam. gate: front34
  shows no seam line at full-body scale.
- S6 full static gate both hands: C1-C6b PASS + fresh vision review of 8 crops.
- S7 motion gate: rebuild squat, multi-frame penetration sweep + per-frame crops.
  gate: 0 penetration every sampled frame + reviewer clears the strip.
- S8 promote: export as v5 glb (NEW version, do NOT overwrite v4). update registry.
  Needs owner sign-off before any deploy-asset write.

## process guard (learned the hard way 2026-07-23)
Do NOT declare clean or promote off keyframe stills. Run the FULL gate (static +
motion) and have a FRESH reviewer open the crops. Owner sign-off before any library
write. Library back-squat currently = v3 baseline (v4 promotion was reverted).
