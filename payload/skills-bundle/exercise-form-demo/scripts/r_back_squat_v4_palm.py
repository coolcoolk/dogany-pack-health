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
# Render driver for the v4-WRIST back squat preview. Adds, on top of the v4_grip
# driver: 3 full-body stills (top/mid/bottom) + a SIDE/PROFILE crop of the
# forearm->wrist->hand (camera looking along the bar axis) at top and bottom so the
# wrist bend is judgeable, plus the usual tight near/far per-hand crops. PREVIEW dir.
import bpy, sys, math, glob, os
from mathutils import Vector

WORK = _os.path.join(_WORK_ROOT, "back_squat_v4_palm")
bpy.ops.wm.open_mainfile(filepath=WORK + "/back_squat_v4_palm.blend")
sc = bpy.context.scene
sc.render.engine = 'BLENDER_EEVEE'
try: sc.eevee.taa_render_samples = 96
except Exception: pass
try: sc.eevee.use_shadows = True
except Exception: pass
sc.render.resolution_x = 720; sc.render.resolution_y = 1280
sc.render.film_transparent = False
sc.render.fps = 30
sc.render.image_settings.file_format = 'PNG'

rig = bpy.data.objects["Rig"]

def wrist_world(side, frame):
    sc.frame_set(frame); bpy.context.view_layer.update()
    return rig.pose.bones["hand" + side].matrix.translation.copy()

def elbow_world(side, frame):
    sc.frame_set(frame); bpy.context.view_layer.update()
    return rig.pose.bones["forearm" + side].matrix.translation.copy()

# ---------------- main full-body camera: 39 deg off straight front -------------
def main_cam():
    for o in list(bpy.data.objects):
        if o.type == 'CAMERA': bpy.data.objects.remove(o, do_unlink=True)
    az = math.radians(39)
    out = Vector((math.sin(az), -math.cos(az), 0.14)); out.normalize()
    aim = Vector((0, 0, -0.22)); loc = aim + 5.8 * out
    cam = bpy.data.cameras.new("cam"); ob = bpy.data.objects.new("cam", cam)
    sc.collection.objects.link(ob); ob.location = loc
    d = (aim - loc).normalized(); ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.lens = 52; cam.sensor_fit = 'VERTICAL'; sc.camera = ob
    return ob

# ---------------- tight per-hand crop camera (locked to hand-local frame) -------
def _hand_rot(side, frame):
    sc.frame_set(frame); bpy.context.view_layer.update()
    return rig.pose.bones["hand" + side].matrix.to_3x3().copy()

_REF = {}
for _s in (".L", ".R"):
    _sx = 1.0 if _s == ".L" else -1.0
    _az = math.radians(34)
    _d0 = Vector((_sx * math.sin(_az), -math.cos(_az), 0.16)).normalized()
    _REF[_s] = _hand_rot(_s, 0).transposed() @ _d0

def hand_cam(side, frame, dist=0.52, lens=110):
    for o in list(bpy.data.objects):
        if o.type == 'CAMERA': bpy.data.objects.remove(o, do_unlink=True)
    aim = wrist_world(side, frame)
    dirw = (_hand_rot(side, frame) @ _REF[side]).normalized()
    loc = aim + dist * dirw
    cam = bpy.data.cameras.new("hc"); ob = bpy.data.objects.new("hc", cam)
    sc.collection.objects.link(ob); ob.location = loc
    d = (aim - loc).normalized(); ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.lens = lens; cam.sensor_fit = 'AUTO'; sc.camera = ob
    return ob

# ---------------- SIDE / PROFILE crop: look ALONG the bar axis (world X) at the
# wrist so the forearm->wrist->hand bend shows in profile (Y-Z plane). Aim between
# wrist and elbow to frame the whole lower arm; camera slightly off the pure axis so
# the near fingers don't fully occlude the wrist line. -------------------------
def wrist_side_cam(side, frame, dist=0.42, lens=95):
    for o in list(bpy.data.objects):
        if o.type == 'CAMERA': bpy.data.objects.remove(o, do_unlink=True)
    w = wrist_world(side, frame); e = elbow_world(side, frame)
    aim = 0.55 * w + 0.45 * e
    sx = 1.0 if side == ".L" else -1.0
    # view from OUTSIDE the arm, mostly along the bar axis (+/-X), tipped a little to
    # the front (-Y) and up (+Z) so the wrist crease is not edge-on.
    dirw = Vector((sx * 1.0, -0.42, 0.28)).normalized()
    loc = aim + dist * dirw
    cam = bpy.data.cameras.new("wc"); ob = bpy.data.objects.new("wc", cam)
    sc.collection.objects.link(ob); ob.location = loc
    d = (aim - loc).normalized(); ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.lens = lens; cam.sensor_fit = 'AUTO'; sc.camera = ob
    return ob

mode = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "all"

if mode in ("all", "anim"):
    main_cam()
    fdir = WORK + "/frames"
    if os.path.exists(fdir):
        for f in glob.glob(fdir + "/*.png"): os.remove(f)
    os.makedirs(fdir, exist_ok=True)
    sc.render.resolution_x = 720; sc.render.resolution_y = 1280
    sc.render.filepath = fdir + "/f_"
    bpy.ops.render.render(animation=True)
    print("FRAMES", len(glob.glob(fdir + "/f_*.png")))

if mode in ("all", "stills"):
    sdir = WORK + "/stills"
    os.makedirs(sdir, exist_ok=True)
    main_cam()
    sc.render.resolution_x = 720; sc.render.resolution_y = 1280
    for tag, frame in (("top", 0), ("mid", 40), ("bottom", 78)):
        sc.frame_set(frame)
        sc.render.filepath = sdir + "/body_%s.png" % tag
        bpy.ops.render.render(write_still=True)
        print("STILL", tag)

if mode in ("all", "crops"):
    cdir = WORK + "/crops"
    os.makedirs(cdir, exist_ok=True)
    sc.render.resolution_x = 900; sc.render.resolution_y = 900
    for tag, frame in (("top", 0), ("mid", 40), ("bot", 78)):
        for side, sl in ((".L", "L"), (".R", "R")):
            hand_cam(side, frame)
            sc.render.filepath = cdir + "/hand_%s_%s.png" % (tag, sl)
            bpy.ops.render.render(write_still=True)
            print("CROP", tag, sl)
            wrist_side_cam(side, frame)
            sc.render.filepath = cdir + "/wristside_%s_%s.png" % (tag, sl)
            bpy.ops.render.render(write_still=True)
            print("WRISTSIDE", tag, sl)
