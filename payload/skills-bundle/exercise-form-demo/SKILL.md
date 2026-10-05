---
name: exercise-form-demo
display_name: 운동 폼 3D 데모
description: Build/render/refine/list a curated library of 3D exercise form-demo media (rigged bodybuilder model, coaching-grade form) -- one-rep animation videos + still poses, for product use (shown before trainee's first set of a new exercise, setup/form guidance). Covers generating a NEW demo (video or still) for an exercise, adding to the demo library (batch build for productization), re-rendering/refining an EXISTING demo (camera angle, depth/ROM, background, form fix), and listing/looking up which demos already exist. Korean triggers: "스쿼트 폼 영상 만들어줘", "데드리프트 자세 3D로 시연", "이 종목 폼 데모 렌더", "폼 데모 라이브러리에 추가", "무릎 90도 재활 버전으로", "카메라 각도 바꿔서 다시", "이 운동 데모 있어?". Output: renders to skill's own library/ folder (mp4 + gif + 3 QA stills), updates library/registry.yaml catalog, emits QA stills for review before finalize/send.
---

# exercise-form-demo

asset-production pipeline, not a live gimmick. curated, reproducible, catalogued LIBRARY
of 3D form demos (one-rep video + stills) shipped as product content. heavy Blender work
= opus subagent.

## hard rules
- REVIEW GATE every build AND every refine (procedure-enforced, no hook). demo is done
  only when it PASSES review, not when it renders. owner final look outranks the gate:
  gate PASS has been owner-rejected twice (registry `squat` row).
- rig choice = `library/registry.yaml` `rig:` block, never guessed from a filename.
- INVARIANTS.md pasted VERBATIM into every Blender subagent prompt.
- no absolute paths in scripts; resolve at runtime (env overrides in reference/layout.md).
- library = curated 3D model only. never add user-supplied media.
- this folder ships in `pack_health`: a change here is a pack change (release discipline).
- new mocap: read `scratch/mocap/SOURCES.md` first (CMU only cleared for redistribution).

## when
make / render a demo (pose or rep), batch-build for the library, refine an existing one
(angle / ROM / bg / form fix), list or look up what exists (`library/registry.yaml`).

## build (procedure)
1. pick exercise + variant + kind (rep|pose) + rom (parallel|knee_90|custom) + options
   (camera_deg_off_front default 39, background dark) + rig (registry).
2. dispatch opus subagent. prompt MUST carry: (a) INVARIANTS.md verbatim; (b) this lift's
   mechanics (start stance, joint angles, hinge, bar path / COM); (c) rig + template
   script (`scripts/s1_squat.py` = rep reference); (d) outputs into
   `library/<exercise>/<variant>/`.
3. subagent renders mp4 + gif + 3 QA stills, reports bottom-frame numeric checks (ankle z
   constant, COM vs midfoot, knee vs toe, depth).
4. REVIEW GATE per REVIEW.md: reviewer separate from builder (fresh vision subagent or
   coordinator; self-cert never counts); reviewer OPENS the stills (numbers miss
   clipping); PASS or FAIL + per-still defect list; FAIL -> fix -> re-render -> re-review,
   cap 3 rounds, then STOP and tell owner what limits it.
5. PASS -> update registry row (kind, rom, status, rig_version, camera, fps, duration,
   built date, output paths, source_scripts). coordinator final look, present to owner,
   one-line worklog note.
read reference/layout.md when picking a rig, template script or build input, or when
a script / sheet / encode step finds its input dir missing.

## refine
reuse the exercise's scripts / scene, change only the requested param, re-render to SAME
library paths, re-run REVIEW GATE (not exempt), bump registry row.

## equipment scope
barbell grip demos are supported on the v3 rig (`back_squat`) and the MPFB body
(`deadlift`). per-finger grip, dumbbell / machine / cable props are not built yet: say
so if asked, do not fake it. hand remodel plan (paused): REMODEL-PLAN.md.

## model routing
Blender render / rig = opus subagent. registry bookkeeping = main agent. reviewer =
fresh vision subagent or coordinator, never the builder.
