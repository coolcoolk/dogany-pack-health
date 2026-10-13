"""Muscle-detail A/B: does the v5 deform stack (armature preserve-volume +
JOINT-MASKED corrective smooth + subsurf) preserve the approved n4 muscle
separation at standing rest?

  detail_ab_n4.png  -- the approved-look body mesh (build_body: targets+subsurf),
                       NO rig, NO corrective smooth. This is the reference.
  detail_ab_v5.png  -- the SAME mesh + rig + masked corrective smooth + subsurf,
                       posed at standing rest.

Same camera, same approved dramatic lighting (AgX punchy). If muscle definition
matches, the corrective-smooth mask worked. Renders to scratch/rigv5_ab/.

blender --background --python rigv5_detail_ab.py -- [n4|v5]
"""
import bpy, os, sys, importlib.util
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rigv5_lib", os.path.join(HERE, "rigv5_lib.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

which = "v5"
for a in (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []):
    if a in ("n4", "v5"):
        which = a
OUT = os.path.join(HERE, "rigv5_ab")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.read_factory_settings(use_empty=True)
L.enable_mpfb()
body = L.build_body()
if which == "v5":
    arm = L.add_rig(body, "default")
    L.clean_weights(body, limit=4, normalize=True, smooth_iters=0)
    mask = L.build_joint_mask(body, arm)
    L.configure_deform(body, preserve_volume=True, corrective=True,
                       cs_factor=0.6, cs_iters=12, cs_vgroup=mask)

scn = bpy.context.scene
L.studio(scn, view_transform='AgX')      # the approved dramatic grade
# frame + light the torso the same for both
deps = bpy.context.evaluated_depsgraph_get()
me = bpy.data.meshes.new_from_object(body.evaluated_get(deps))
co = [body.matrix_world @ v.co for v in me.vertices]
lo = Vector((min(p.x for p in co), min(p.y for p in co), min(p.z for p in co)))
hi = Vector((max(p.x for p in co), max(p.y for p in co), max(p.z for p in co)))
bpy.data.meshes.remove(me)
fy = -1.0    # body faces -Y (front)
L.add_lights(scn, Vector((0, 0, 1.05)), fy)
L.add_floor(scn, lo.z - 0.02)
cam = L.make_cam(scn)
# torso-and-thighs crop, front 3/4 -- where pec/ab/quad separation reads
ctr = Vector((0, (lo.y + hi.y) / 2, 1.02))
L.shoot(scn, cam, os.path.join(OUT, "detail_ab_%s.png" % which),
        ctr, 1.35, Vector((0.45, fy, 0.06)), 900, 1100)
print("AB_DONE", which)
