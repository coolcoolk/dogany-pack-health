# Deadlift mocap acquisition — sources, license, technical assessment

Task: find commercial-safe mocap for retargeting a barbell deadlift onto the
exercise-form-demo rig. CMU Graphics Lab Motion Capture Database has no
motion literally tagged "deadlift" (it predates gym-culture terminology), so
the pick is the best real floor-lift/hip-hinge motion in the catalog. No
login-walled or non-commercial source was used.

## License — CMU Graphics Lab Motion Capture Database

- Source: http://mocap.cs.cmu.edu/faqs.php
- Operative line, quoted verbatim from the FAQ ("How can I use this data?"):
  > "The motion capture data may be copied, modified, or redistributed
  > without permission."
- No fee, no attribution requirement, no non-commercial clause. Widely relied
  on by shipped commercial games/products for exactly this reason. This is
  the least-restrictive license of any source checked (see rejected sources
  below) — safe for a paid/product deliverable.
- Files here are BVH conversions of the original ASF/AMC data. Conversion
  itself carries no additional restriction (cgspeed/B. Hahne conversions are
  explicitly released with "no additional restrictions" beyond CMU's own
  terms). Files were fetched from a GitHub mirror of that same public BVH
  conversion set: https://github.com/omni360/cmu.action (raw files under
  `cmuconvert-mb2-*` directories, unmodified from the original conversion).

## Rejected sources (checked, not used)

- **SFU Motion Capture Database** (mocap.cs.sfu.ca) — explicitly research-only,
  "cannot be used for commercial products or resale." Rejected.
- **Bandai Namco Research motion dataset** (github bandainamco-mirai) —
  CC BY-NC-ND (non-commercial, no-derivatives). Rejected — retargeting is a
  derivative work and the license forbids both NC use and derivatives.
- **AMASS** — aggregates MoCap under research-only redistribution terms.
  Rejected outright per task brief.
- **Mixamo** — no deadlift/weightlifting animation found in its catalog by
  name in any case; also login-walled (Adobe account), so out of scope even
  if one existed. Not used; nothing to hand off here (see "Mixamo" section
  below for what a manual check would need if the owner wants to look).
- **ACCAD (OSU)** — general-purpose research mocap library, browsed but no
  weightlifting/lifting content indexed; not pursued further once CMU
  candidates were confirmed usable.
- **Truebones / mocapdata.com free tier** — free packs are marketing samples
  for a paid library; license terms on the free files are inconsistent/unclear
  per-file and not worth the risk versus CMU's unambiguous clearance. Not used.

## Skeleton / format (all 3 files, identical convention)

- Format: BVH (Biovision Hierarchy), text, loads natively in Blender's
  built-in "Import BVH" (no plugins/conversion needed).
- Skeleton: standard CMU 31-joint hierarchy — `Hips` root, `LHipJoint/
  LeftUpLeg/LeftLeg/LeftFoot/LeftToeBase` and mirrored right leg, `LowerBack/
  Spine/Spine1/Neck/Neck1/Head`, `LeftShoulder/LeftArm/LeftForeArm/LeftHand/
  LeftFingerBase/LeftHandIndex1/LThumb` and mirrored right arm.
- Frame rate: 120 fps (frame time 0.0083333s) for all three files — matches
  CMU's Vicon capture rate (12-camera MX-40 system, per CMU FAQ). Will need
  resampling to the render pipeline's fps in Blender (standard NLA/action
  resample, not a data problem).
- Validated by parsing (see `analyze_bvh.py` in this dir): all three parse
  cleanly, header `Frames:` matches actual data row count, joint/channel
  hierarchy is well-formed. No corruption.

## Per-file assessment

### 26_10.bvh — PRIMARY RECOMMENDATION
- CMU Subject #26 ("nursery rhymes, basketball, bending"), motion 10, listed
  in the CMU index as **"bend, lift"**.
- Duration: 5.817s, 698 frames @ 120fps.
- Root (Hips) trajectory: stands (Y≈18.5) → smooth descent to a deep crouch
  (Y≈11.4, a 7.2-unit drop, the largest of any candidate checked) → brief
  hold at the bottom (~5 frames, i.e. a grip/load pause) → smooth ascent back
  to standing lockout, held to end of clip.
- Root X/Z stay within a ~1-2 unit box for the whole clip — the subject is
  stationary in place, not walking up to an object. This matters: it means
  the capture is directly usable as an in-place lift without needing to
  strip out translation, which a barbell deadlift needs (feet planted).
  Verified via `analyze_bvh.py` root-position min/max.
- Joint angles at the bottom of the dip (parsed from rotation channels):
  LowerBack.Xrotation ≈ 52° (forward torso flex), LeftUpLeg.Xrotation ≈ 119°
  (deep hip flexion), LeftLeg.Xrotation ≈ 110° (deep knee flexion). This is a
  genuine floor-reach with hip AND knee both loaded — closer to a squat-style
  object pickup than a stiff-leg conventional deadlift (conventional form
  usually has less knee flexion, more hip-dominant hinge). It is real,
  in-place, floor-to-standing motion capture, which is what the task needs as
  a retarget base; the knee-flexion ratio is a starting point a Blender pass
  can dial down toward a more hip-dominant hinge if the final demo wants
  strict conventional-deadlift knee angle.
- Confidence this is a real, usable floor-lift motion: HIGH. Confidence it
  is literally "conventional barbell deadlift form" out of the box: MEDIUM —
  expect the retarget agent to adjust knee-flexion/hip-hinge ratio.

### 26_11.bvh — SECONDARY / hip-hinge reference
- Same subject #26, motion 11, also indexed as **"bend, lift"**.
- Duration: 4.583s, 550 frames @ 120fps.
- Root Y drop is shallower (18.5 → 16.7, only 1.9 units) — does not reach
  floor level, implying a higher/lighter object.
- BUT joint angles are more hip-dominant than 26_10: LowerBack.Xrotation ≈ 37°,
  LeftUpLeg.Xrotation ≈ 110° (deep hip flexion, similar to 26_10), LeftLeg.
  Xrotation ≈ 36° (much shallower knee flexion than 26_10's 110°). This is a
  genuinely more hip-hinge-dominant pattern — closer to a Romanian-deadlift-
  style hinge (hips move back, knees stay fairly soft) than 26_10's deeper
  squat-like pickup.
- Root X/Z also stationary (tight box, no walking).
- Use case: if the retarget agent finds 26_10's knee bend too deep for
  "conventional deadlift" look, 26_11 is a same-subject, same-rig alternate
  take with a more hip-dominant angle ratio, at the cost of not reaching full
  floor depth. Could also be blended/referenced alongside 26_10.
- Confidence this is a real floor-hinge-style lift: HIGH. Confidence it
  reaches full deadlift floor depth: LOW (shallower dip than 26_10).

### 74_08.bvh — THIRD / fallback only, has caveats
- CMU Subject #74 ("kicks and walking on slopes"), motion 8, indexed as
  **"lifting up"**.
- Duration: only 1.408s, 169 frames @ 120fps — very short clip.
- Root Y starts at the deepest crouch of any file checked (Y≈8.3, lower than
  26_10's 11.4) and rises smoothly to standing (Y≈17.3), i.e. it looks like
  it captures only the ascending/lift-off half of a rep — no descent phase
  is present in this clip.
- Caveat: Root X/Z drift ~1.5 units X and ~6.8 units Z over the clip — the
  subject is translating forward significantly while rising, consistent with
  "carry after lifting" or a walk-into-lift sequence, not a stationary
  in-place barbell pull. Would need root-motion stripping/re-centering before
  retargeting onto a fixed-stance deadlift rig.
- Confidence this is a real lift-off motion: MEDIUM-HIGH (very deep starting
  crouch, clean rise). Confidence it's usable without editing: LOW (missing
  descent phase, has translation drift). Kept only as a third option / for
  cross-reference on lift-off posture, not the first pick.

## Rejected CMU motions (checked, not downloaded/kept)

- `79_93` "weight lifting" (Subject #79, actor everyday-activities reel):
  root Y range only 16.9–18.2 (1.3-unit delta) — barely leaves standing
  height. Rotation channels confirm shallow flexion (hip ≈37°, torso ≈8° at
  sampled frame). This is a standing mime (curls/press-style), not a floor
  lift. Rejected for deadlift use.
- `79_25` "moving heavy box" (same subject): root Y delta only 0.8 — no
  meaningful bend at all, a standing carry/push. Rejected.
- `74_07` "lifting up" (Subject #74, sibling clip to 74_08): similar
  translation-drift issue as 74_08 but a less clean floor start (starts
  mid-crouch at Y≈12 rather than a full standing-to-floor cycle). 74_08 was
  judged the better of the pair and kept; this one was dropped to stay within
  the 1-3 file budget.

## Mixamo (not used — for reference only, do not fetch)

Checked Mixamo's catalog by name; it has no "deadlift" or barbell-lift
animation. It does have generic "Lifting" / box-carry animations under
non-gym names, but nothing hip-hinge/barbell-specific, and every asset
requires an Adobe login to export (FBX). Per task bounds, no login was
attempted and nothing was downloaded from Mixamo. Not recommended as a
fallback here since CMU already supplies a directly-fetchable, unambiguously
licensed, better-matching motion (26_10). Only revisit Mixamo if the Blender
retarget agent finds CMU's knee-flexion angle unfixable and specifically
wants a cleaner conventional-form reference — in that case the owner would
need to log into mixamo.com, search "lifting" or "picking up", and export as
FBX binary, with skin, 30fps.

## Ranked recommendation

1. **26_10.bvh — use this as the primary retarget source.** Real, in-place,
   full standing→floor→standing motion capture at 120fps on the standard
   CMU 31-joint skeleton, unambiguous commercial-safe license (CMU: "may be
   copied, modified, or redistributed without permission"). Caveat: knee
   flexion is deeper than strict conventional-deadlift form (squat-style
   pickup) — the retarget/animation pass should judge whether to soften knee
   bend or keep it (it still reads as a heavy floor lift either way).
2. **26_11.bvh — secondary reference**, same subject/rig, more hip-dominant
   angle ratio (less knee bend, similarly deep hip flexion) but shallower
   floor reach. Use if 26_10's knee angle needs a hip-hinge-heavier
   comparison point, or blend the two.
3. **74_08.bvh — fallback only.** Deepest crouch start-point of the three but
   missing the descent phase and carrying ~1.5-6.8 units of translation drift
   that would need to be stripped/re-centered before retargeting onto a
   stationary rig. Use only if both subject-26 clips prove unworkable.

No non-commercial-safe source was needed as a last resort — CMU cleared all
three picks. If, after the Blender pass, none of the three read convincingly
as a "deadlift" (vs. generic floor pickup), the documented Mixamo path above
is the next thing to try, but it requires the owner's own Adobe login.
