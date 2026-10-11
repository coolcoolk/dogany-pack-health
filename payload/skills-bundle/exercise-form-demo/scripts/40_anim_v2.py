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
import bpy, sys, math, glob, os
sys.path.append(_os.path.join(_WORK_ROOT, "blender_work"))
import lib_render as L, lib_rig2 as R
from mathutils import Vector, Matrix

WORK = _os.path.join(_WORK_ROOT, "blender_work")
bpy.ops.wm.open_mainfile(filepath=WORK + "/rig3.blend")
mesh = bpy.data.objects["Body"]; rig = bpy.data.objects["Rig"]

# low-poly copy (same skeleton/weights) for fast render
bpy.ops.object.select_all(action='DESELECT')
mesh.select_set(True); bpy.context.view_layer.objects.active = mesh
bpy.ops.object.duplicate()
low = bpy.context.view_layer.objects.active; low.name = "Body_low"
tris = sum(len(p.vertices)-2 for p in mesh.data.polygons)
dec = low.modifiers.new("Decimate", 'DECIMATE'); dec.decimate_type='COLLAPSE'
dec.ratio = min(1.0, 60000.0/float(tris))
while low.modifiers[0].name != "Decimate":
    bpy.ops.object.modifier_move_up(modifier="Decimate")
bpy.ops.object.modifier_apply(modifier="Decimate")
bpy.data.objects.remove(mesh, do_unlink=True)
print("LOW_TRIS", sum(len(p.vertices)-2 for p in low.data.polygons))

for pb in rig.pose.bones:
    pb.rotation_mode = 'QUATERNION'

def reset_bind():
    for pb in rig.pose.bones:
        pb.rotation_quaternion = (1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
    bpy.context.view_layer.update()

def wrot(name, axis, deg):
    pb = rig.pose.bones[name]; M = pb.matrix.copy(); h = M.translation.copy()
    Rm = Matrix.Rotation(math.radians(deg),4,axis); T = Matrix.Translation(h)
    pb.matrix = T @ Rm @ T.inverted() @ M
    bpy.context.view_layer.update()

def hips_move(dz, dy):
    pb = rig.pose.bones['hips']; M = pb.matrix.copy()
    M.translation.z += dz; M.translation.y += dy; pb.matrix = M
    bpy.context.view_layer.update()

prefs = bpy.context.preferences.edit
prefs.keyframe_new_interpolation_type = 'BEZIER'
try: prefs.keyframe_new_handle_type = 'AUTO_CLAMPED'
except Exception as e: print("handle warn", e)

# ---- pose fragments (parent before child) ----
SQUAT = [('h',-0.28,-0.05),
         ('r','thigh.L','X',-48), ('r','shin.L','X',92), ('r','foot.L','X',-42),
         ('r','thigh.R','X',-48), ('r','shin.R','X',92), ('r','foot.R','X',-42)]
SUP1  = [('r','forearm_twist.L','X',90),  ('r','forearm_twist.R','X',-90)]   # palms roll one way
SUP2  = [('r','forearm_twist.L','X',-90), ('r','forearm_twist.R','X',90)]    # and the other way
FIST  = [('r','fingers_01.L','Y',85), ('r','fingers_02.L','Y',85), ('r','thumb_01.L','Z',45), ('r','thumb_02.L','Z',40),
         ('r','fingers_01.R','Y',-85),('r','fingers_02.R','Y',-85),('r','thumb_01.R','Z',-45),('r','thumb_02.R','Z',-40)]
CURL  = [('r','forearm.L','Y',-118), ('r','forearm.R','Y',118)]              # bicep curl (elbow)
FWD   = [('r','upper_arm.L','Z',-85), ('r','upper_arm.R','Z',85),            # reach forward
         ('r','forearm.L','Y',-25),  ('r','forearm.R','Y',25)]
OVER  = [('r','upper_arm.L','Y',-95), ('r','upper_arm.R','Y',95)]            # overhead raise

KEYS = [
    (0,   []),       # T-pose
    (25,  SQUAT),    # 1) corrected squat  -> knee crease
    (50,  []),
    (72,  SUP1),     # 2) forearm twist A (pronation/supination)
    (94,  SUP2),     #    forearm twist B
    (112, []),
    (132, FIST),     # 3) fist curl
    (152, []),       #    open
    (174, CURL),     # 4a) bicep curl
    (196, FWD),      # 4b) reach forward
    (220, OVER),     # 4c) overhead raise
    (244, []),       # back to T
    (262, []),
]
FSTART, FEND = 0, 262

for frame, ops in KEYS:
    bpy.context.scene.frame_set(frame)
    reset_bind()
    for op in ops:
        if op[0]=='r': wrot(op[1], op[2], op[3])
        elif op[0]=='h': hips_move(op[1], op[2])
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion', frame=frame)
    rig.pose.bones['hips'].keyframe_insert('location', frame=frame)

sc = bpy.context.scene
sc.frame_start = FSTART; sc.frame_end = FEND; sc.render.fps = 30

# camera + lights (3/4 front), frame the whole figure incl. arms
for o in list(bpy.data.objects):
    if o.type in ('CAMERA','LIGHT'): bpy.data.objects.remove(o, do_unlink=True)
L.setup_world(); L.add_lights()
sc.render.engine='BLENDER_EEVEE'
sc.render.resolution_x=800; sc.render.resolution_y=800
try: sc.eevee.taa_render_samples = 16
except Exception: pass
d = 5.2
cam = L.add_cam("cam3q", (d*0.55, -d*0.83, 0.30), Vector((0,0,0.02)))
cam.data.lens = 48
sc.camera = cam

fdir = WORK + "/frames2"
if os.path.exists(fdir):
    for f in glob.glob(fdir + "/*.png"): os.remove(f)
os.makedirs(fdir, exist_ok=True)
sc.render.image_settings.file_format = 'PNG'
sc.render.filepath = fdir + "/f_"
bpy.ops.render.render(animation=True)
frames = sorted(glob.glob(fdir + "/f_*.png"))
print("FRAMES", len(frames), "first", os.path.basename(frames[0]), "last", os.path.basename(frames[-1]))
