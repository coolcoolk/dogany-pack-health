# form-demo quality invariants -- Blender subagent prompt block

Paste this whole block into the Opus Blender subagent prompt for EVERY render.
These are the non-negotiable look + biomechanics rules the whole library shares.
Values in {curly} are per-job params the skill fills from the request.

## environment
- Blender `/opt/homebrew/bin/blender` (v5.2 LTS). Headless:
  `blender --background --python <script.py>`.
- Blender build has NO ffmpeg output -> render PNG sequence, then encode with
  system `ffmpeg` (H.264, yuv420p, +faststart).
- work in a tmp scratch dir; write final outputs to the paths the skill gives.

## rig (do not rebuild unless asked)
- import the render rig the job names ({rig}; authority = `library/registry.yaml`
  `rig:` block). bodyweight: `assets/rig/bodybuilder_rigged_v2_lowpoly.glb` (50k
  tris, 32 deform bones, textures embedded) OR open `assets/rig/squat.blend` (rig +
  reference squat anim to copy timing from). grip / equipment:
  `assets/rig/bodybuilder_rigged_v3_lowpoly.glb` (34 bones, same axes/scale).
- axes: up=+Z, front=-Y, arms along X in bind. .L = +X. names: hips, spine,
  spine.001/002, neck, head; per side shoulder, upper_arm, forearm,
  forearm_twist, hand, thumb_01/02, fingers_01/02; per side thigh, shin, foot,
  toe.
- hands: v2 = grouped fingers, no equipment grip. v3 = grouped fingers in 3
  segments (fingers_01/02/03); closed bar grip via `scripts/hand_regrip_v3.py`.
  no per-finger on either. no IK control bones -> pose via FK + analytic leg IK
  (below).

## feet planted (hard rule, every frame)
- add a ground plane at foot level. pin each ankle to a fixed world z on the
  floor. solve leg as 2-joint analytic IK so thigh+shin reach the pinned ankle.
- re-align foot bones to bind (flat) each frame so soles stay parallel to floor.
- heels stay DOWN. feet never float, tilt, or clip through floor. verify ankle
  world-z constant across all frames (print + check).

## balance (hard rule)
- center of mass sits over the MIDFOOT, never behind the heel. at the deepest
  frame, drop a vertical plumb from hips/chest -> must land ~over midfoot.
- shins incline forward so knees travel over/just past toes; torso hinges
  forward to match; hips go back only as much as balance allows.
- NOTE: at parallel depth the hip joint cannot sit directly over the ankle
  (that needs ATG). balance target = COM line over midfoot, not hip-over-ankle.

## biomechanics (correct form, coaching-grade)
- knees track OUT over the 2nd-3rd toe (foot toe-out ~10-15deg). no valgus
  (knees caving in). check knee x vs foot x sign at bottom.
- spine neutral, no rounding, no butt-wink at bottom.
- gaze/head NEUTRAL: forward-and-slightly-down a couple meters ahead, head in
  line with spine. no chin-to-chest tuck at bottom.
- movement-specific hinge/track per exercise; get the real lift mechanics right.

## clip structure (rep kind)
- START in the READY STANCE already set (no T-pose visible, ever). arms in the
  movement's counterbalance/hold position from frame 1.
- sequence: ready -> descend -> brief bottom hold -> ascend -> ready.
  start pose == end pose (loop-friendly).
- ~30fps, smooth Bezier ease in/out (controlled, not bouncy).

## camera + look
- camera: front-dominant 3/4, default {camera_deg_off_front=39} degrees off
  straight FRONT. frames full body head-to-feet. (25=more front, 52=more side.)
- dark studio: near-black charcoal backdrop, dark floor a touch lighter so the
  horizon/ground reads, contact shadow under feet. view transform = Standard so
  dark stays dark while light skin stays bright.
- lighting: key + front fill + side fill + rim so muscle detail reads and the
  model separates from the dark bg (no muddy shadows).

## encode + outputs
- MP4: H.264 yuv420p +faststart, portrait 720x1280 (or square if it frames the
  move better). UNDER 10 MB (short clips are ~0.5 MB, plenty of headroom).
- gif fallback optional.
- ALWAYS emit 3 QA stills (top/ready, mid/descent, bottom/deepest) as PNG so the
  coordinator can check form before the clip is finalized/sent.

## rom variants
- parallel: standard full depth (thigh ~horizontal).
- knee_90: rehab partial -> cap knee flexion ~90deg (stop above parallel, like
  sitting to a chair), then ascend. shorter ROM.
- custom: per request.

## no clipping / interpenetration (HARD rule -- check every keyframe)
- NO mesh passes through mesh. specifically watch:
  - hands / forearms into the TORSO (crossed-arms and hands-on-chest poses sink
    into the pec/rib volume -> BANNED. keep a real air gap, or pick a pose that
    clears the body: hands on hips, arms extended forward with clearance, or
    hands behind head with elbows out).
  - any prop (bar/plate/dumbbell) through the body, head, or the other arm.
  - limb into limb, heel/toe through floor.
- process (mandatory): after rendering, OPEN the 3 QA stills and LOOK. confirm
  no interpenetration at top / mid / bottom. numeric joint checks are NOT enough
  -- a pose can pass every angle/distance check and still have a hand buried in
  the chest. if any clip is visible, fix the pose and RE-RENDER. do not report
  "clean" until the stills are visually clear.

## honesty
- if the mesh/rig cannot hit a pose cleanly (deep hip-crease pinch, equipment
  grip, per-finger action), SAY SO in the report -- do not fake it. report the
  bottom-frame numeric checks (ankle z, COM vs midfoot, knee vs toe, depth).
