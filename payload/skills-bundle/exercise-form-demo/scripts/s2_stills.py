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
from mathutils import Vector
WORK=_os.path.join(_WORK_ROOT, "blender_work")
bpy.ops.wm.open_mainfile(filepath=WORK+"/squat.blend")
sc=bpy.context.scene
sc.render.engine='BLENDER_EEVEE'
try: sc.eevee.taa_render_samples=96
except Exception: pass
try: sc.eevee.use_shadows=True
except Exception: pass
sc.render.resolution_x=720; sc.render.resolution_y=1280
sc.render.film_transparent=False

# 3/4 front-side camera: az from front(-Y) toward +X (character's left) ~55deg
def make_cam(dist,az_deg,lens,aim,hz):
    for o in list(bpy.data.objects):
        if o.type=='CAMERA': bpy.data.objects.remove(o,do_unlink=True)
    az=math.radians(az_deg)
    out=Vector((math.sin(az),-math.cos(az),hz)); out.normalize()
    loc=Vector(aim)+dist*out
    cam=bpy.data.cameras.new("cam"); ob=bpy.data.objects.new("cam",cam)
    sc.collection.objects.link(ob); ob.location=loc
    d=(Vector(aim)-loc).normalized()
    ob.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
    cam.lens=lens; cam.sensor_fit='VERTICAL'
    sc.camera=ob; return ob

make_cam(dist=5.8, az_deg=39, lens=52, aim=(0,0,-0.22), hz=0.14)
for f,tag in ((0,"stand0"),(42,"mid"),(78,"bottom"),(156,"stand1")):
    sc.frame_set(f)
    sc.render.filepath=WORK+"/qa_%s.png"%tag
    bpy.ops.render.render(write_still=True)
    print("RENDERED",tag)
