"""Build body_rig_v5: the approved MPFB bodybuilder body (exact n4_dl_start.py
look) with a REBUILT deformation layer, saved as a ready-to-pose canonical asset.

What is NEW vs the old pipeline (this is the rebuild):
  * skinning method: armature modifier runs with use_deform_preserve_volume=True
    (dual-quaternion) -- fixes the knee/elbow collapse ("무릎이 이상하게 접혀").
  * corrective-smooth modifier (ORCO rest, light) after the armature -- relaxes
    the residual linear-blend pinch at deep folds without washing muscle detail.
  * weights: MPFB "default" MakeHuman weights, normalized + limited to 4 bones.
  * the hands are driven by the NATIVE per-finger armature (metacarpals included),
    NOT the old custom manual-LBS grip solver that produced the blob fists.

The mesh itself (proportions, muscle targets, skin material, mid-thigh drawers)
is unchanged from the approved n4_dl_start.py look.

Usage:  blender --background --python scripts/32_build_v5.py
Output: assets/rig/body_rig_v5.blend
"""
import bpy, os, sys, importlib.util

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(SKILL, "scratch", "rigv5_lib.py")
spec = importlib.util.spec_from_file_location("rigv5_lib", LIB)
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

OUT = os.path.join(SKILL, "assets", "rig", "body_rig_v5.blend")

bpy.ops.wm.read_factory_settings(use_empty=True)
L.enable_mpfb()

# 1) approved body mesh + drawers (unchanged look)
body = L.build_body()
shorts = L.build_shorts(body)

# 2) rebuilt deformation layer
arm = L.add_rig(body, "default")
L.attach_shorts(shorts, arm, body)
L.clean_weights(body, limit=4, normalize=True, smooth_iters=0)
# corrective smooth is MASKED to joint rings only (knee/elbow/shoulder/hip/
# wrist/finger creases) -- muscle bellies keep full n4 detail (fixes the
# round-1 "smooth mannequin" wash). Stronger, since it is now localized.
mask = L.build_joint_mask(body, arm)
L.configure_deform(body, preserve_volume=True, corrective=True,
                   cs_factor=0.6, cs_iters=12, cs_vgroup=mask)

body.name = "body_v5"
arm.name = arm.data.name = "body_v5.rig"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("V5_BUILD_DONE", OUT, "bones=%d verts=%d" % (len(arm.data.bones), len(body.data.vertices)))
