# folder layout, paths, carry-in gaps (read when picking inputs or an input dir is missing)

## layout (self-contained under the skill folder)
- `assets/rig/` rig lineage. authority = `library/registry.yaml` `rig:` block.
  - `bodybuilder_rigged_v2.glb` (244k) + `_v2_lowpoly.glb` (50k): 32 bones, grouped
    fingers. bodyweight baseline.
  - `bodybuilder_rigged_v3.glb` + `_v3_lowpoly.glb`: 34 bones, fingers in 3 segments.
    grip / equipment demos. grip ref `scripts/hand_regrip_v3.py`.
  - `_v4*.glb` / `_v4_r8*.glb`: hand-remodel rounds. v4 promotion REVERTED
    (REMODEL-PLAN.md). lineage to resume from, NOT a build default.
  - `squat.blend` (master: rig + reference squat anim), `body_rig_v5.blend` (per-finger
    v5 body for v5-era builds), `BODY_RIG_V5.md`.
- `scripts/` Blender templates: `s1_squat.py` squat build reference (biomechanics,
  feet-planted IK, balance) · `s2_stills.py` QA stills · `s3_render.py` render + encode ·
  `s0_cal.py` landmark calibration · `lib_rig2.py` / `30_build_v2.py` / `31_export_v2.py`
  / `40_anim_v2.py` / `32_build_v5.py` = rig build (touch only for a rig rebuild) ·
  `hand_*.py` = hand-remodel diagnostics; `hand_grip_gate.py` is the acceptance harness,
  never promote a hand change without it.
- `library/<exercise>/<variant>/` mp4 + gif + 3 QA stills (+ per-exercise build / render
  / stills / qa_sheets / encode scripts). `library/registry.yaml` = catalog, one row per
  exercise/variant; statuses in use: done | planned | owner_rejected.
- `scratch/` = BUILD INPUTS the v5-era builds import by path (not throwaway):
  `rigv5_lib.py` (imported by build_squat.py, build_squat_v6.py, build_deadlift.py) ·
  `n4_dl_start.py` (approved MPFB body + measured finger-wrap grip solver) ·
  `n5_encode.sh` (PNG seq -> mp4 + gif) · `mocap/26_10.bvh` + `SOURCES.md` +
  `analyze_bvh.py` (deadlift motion + license provenance) · `s0_capture.py` /
  `s1_fit2.py` (REMODEL-PLAN S0 / S1, kept so the plan can resume).
- `INVARIANTS.md` quality-bar prompt block. `REVIEW.md` review checklist + protocol.

## runtime paths (no absolute paths)
- `FORM_DEMO_SKILL_ROOT` skill folder (default from `__file__`)
- `PROJECT_ROOT` instance root (default CWD)
- `FORM_DEMO_WORK_ROOT` Blender work dir (default `$PROJECT_ROOT/files/tmp`)
- `FORM_DEMO_OUT_ROOT` export dir (default `$PROJECT_ROOT/files/outbox`)
- `FFMPEG` ffmpeg binary (default first on PATH)

## what did NOT ship (carry-in 2026-09-12 from a retired instance)
~1.37 GB regenerable dev output stayed behind: diagnostic PNGs, intermediate `.blend`
files, frame dirs (`scratch/n7_frames/`, `scratch/dlrb_frames/`, `scratch/squat_diag/`,
`scratch/donor_*`), `assets/rig/diag_round5..8/`, `_*_bak/` rig snapshots.
- `library/*/*/qa_sheets.py` and `encode.sh` READ those frame dirs: re-run the matching
  `build_*.py` first, then sheet / encode.
- REMODEL-PLAN.md cites `scratch/donor_hand_L*` (S0/S1 outputs) and `diag_round*`
  evidence: reasoning + gate (C1-C6b) intact, artifacts not. re-run `scratch/s0_capture.py`
  then `scratch/s1_fit2.py` before resuming at S2.
- rendered demos in `library/` are complete (mp4 / gif / stills shipped).
