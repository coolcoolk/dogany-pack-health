# --- de-identified 2026-09-12 (pack carry-in): a shipped pack carries no
# --- absolute instance/home path. Roots resolve at runtime; override with
# --- FORM_DEMO_SKILL_ROOT / FORM_DEMO_WORK_ROOT / FORM_DEMO_OUT_ROOT.
import os as _os
_SKILL_ROOT = _os.environ.get("FORM_DEMO_SKILL_ROOT") or _os.path.abspath(
    _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), ".."))
_PROJECT_ROOT = _os.environ.get("PROJECT_ROOT") or _os.getcwd()
_WORK_ROOT = _os.environ.get("FORM_DEMO_WORK_ROOT") or _os.path.join(
    _PROJECT_ROOT, "files", "tmp")
_OUT_ROOT = _os.environ.get("FORM_DEMO_OUT_ROOT") or _os.path.join(
    _PROJECT_ROOT, "files", "outbox")
# --- end de-identification preamble ---
import bpy, sys, math
sys.path.append(_os.path.join(_WORK_ROOT, "blender_work"))
import lib_render as L, lib_rig2 as R
from mathutils import Vector

WORK = _os.path.join(_WORK_ROOT, "blender_work")
bpy.ops.wm.read_factory_settings(use_empty=True)

# 1) import + weld shells (same fix as v1)
mesh = L.import_model(); mesh.name = "Body"
R.merge_by_distance(mesh, 0.001)
print("ISLANDS_AFTER_MERGE", R.count_islands(mesh), "verts", len(mesh.data.vertices))

# 2) base armature (22 deform bones, KNEE corrected)
rig = R.build_armature(mesh)

# 3) automatic bone-heat weights on the base skeleton (clean body + hand-block weights)
bpy.ops.object.select_all(action='DESELECT')
mesh.select_set(True); rig.select_set(True)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.parent_set(type='ARMATURE_AUTO')
print("PARENTED base")

bpy.context.view_layer.objects.active = mesh
bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
bpy.ops.object.vertex_group_limit_total(limit=4)
bpy.ops.object.vertex_group_smooth(group_select_mode='ALL', factor=0.5, repeat=3)
bpy.ops.object.vertex_group_limit_total(limit=4)
bpy.ops.object.vertex_group_normalize_all(lock_active=False)
bpy.ops.object.mode_set(mode='OBJECT')
print("BASE_WEIGHTS_CLEANED")

# 4) add new DOF bones + reparent hand under twist
R.add_dof_bones(rig)
print("DOF_BONES_ADDED total_deform", sum(1 for b in rig.data.bones if b.use_deform))

# 5) graded forearm-twist weight split
R.redistribute_forearm_twist(mesh)
# 6) carve hand block into thumb + combined fingers (manual, no bleed)
stats = R.assign_hand_bones(mesh)
print("HAND_CARVE (thumb,fingers) L", stats.get(".L"), "R", stats.get(".R"))
# 7) final cap + normalize
R.normalize_and_cap(mesh)
print("FINAL_WEIGHTS_DONE")

bpy.ops.wm.save_as_mainfile(filepath=WORK + "/rig3.blend")
print("SAVED rig3.blend")

# ---------- verification renders ----------
def clear_cl():
    for o in list(bpy.data.objects):
        if o.type in ('CAMERA','LIGHT'): bpy.data.objects.remove(o, do_unlink=True)

def cams():
    L.setup_world(); L.add_lights()
    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x = 800; sc.render.resolution_y = 800
    try: sc.eevee.taa_render_samples = 16
    except Exception: pass
    d = 4.7
    cf = L.add_cam("cf", (d*0.55, -d*0.83, 0.35), Vector((0,0,0.05))); cf.data.lens=50
    cs = L.add_cam("cs", (d*0.95, -d*0.15, -0.35), Vector((0.16,0,-0.5))); cs.data.lens=60
    return cf, cs

def render(cam, path):
    sc = bpy.context.scene; sc.camera = cam; sc.render.filepath = path
    bpy.ops.render.render(write_still=True)

R.reset_pose(rig)
cf, cs = cams()
render(cf, WORK + "/v2_00_bind_front.png")

# squat (corrected knee): check crease sits at the real knee
R.reset_pose(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode='POSE')
# lower hips + bend thigh/shin/foot
hp = rig.pose.bones['hips']; M = hp.matrix.copy(); M.translation.z -= 0.28; M.translation.y -= 0.05; hp.matrix = M
bpy.context.view_layer.update()
for s in (".L", ".R"):
    R.wrot(rig, "thigh"+s, 'X', -48)
    R.wrot(rig, "shin"+s,  'X', 92)
    R.wrot(rig, "foot"+s,  'X', -42)
bpy.ops.object.mode_set(mode='OBJECT')
render(cs, WORK + "/v2_01_squat_side.png")
render(cf, WORK + "/v2_01_squat_front.png")

# forearm twist: supinate L (+X about arm axis), pronate R
R.reset_pose(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode='POSE')
R.wrot(rig, "forearm_twist.L", 'X', 90)
R.wrot(rig, "forearm_twist.R", 'X', -90)
bpy.ops.object.mode_set(mode='OBJECT')
render(cf, WORK + "/v2_02_twist_front.png")

# fist curl (fingers + thumb) on both hands
R.reset_pose(rig)
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode='POSE')
for s, sc in ((".L",1), (".R",-1)):
    R.wrot(rig, "fingers_01"+s, 'Y', sc*80)
    R.wrot(rig, "fingers_02"+s, 'Y', sc*80)
    R.wrot(rig, "thumb_01"+s, 'Z', sc*40)
    R.wrot(rig, "thumb_02"+s, 'Z', sc*40)
bpy.ops.object.mode_set(mode='OBJECT')
render(cf, WORK + "/v2_03_fist_front.png")
render(cs, WORK + "/v2_03_fist_side.png")
print("VERIFY_RENDERS_DONE")
