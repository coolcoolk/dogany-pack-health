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
sc.render.fps=30

az=math.radians(39)
out=Vector((math.sin(az),-math.cos(az),0.14)); out.normalize()
aim=Vector((0,0,-0.22)); loc=aim+5.8*out
cam=bpy.data.cameras.new("cam"); ob=bpy.data.objects.new("cam",cam)
sc.collection.objects.link(ob); ob.location=loc
d=(aim-loc).normalized(); ob.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
cam.lens=52; cam.sensor_fit='VERTICAL'; sc.camera=ob

fdir=WORK+"/frames_sq"
if os.path.exists(fdir):
    for f in glob.glob(fdir+"/*.png"): os.remove(f)
os.makedirs(fdir,exist_ok=True)
sc.render.image_settings.file_format='PNG'
sc.render.filepath=fdir+"/f_"
bpy.ops.render.render(animation=True)
n=len(glob.glob(fdir+"/f_*.png"))
print("FRAMES",n)
