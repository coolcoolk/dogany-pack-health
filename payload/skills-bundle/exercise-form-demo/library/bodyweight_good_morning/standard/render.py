# Generic PNG-sequence render. Usage:
#  blender -b --python render.py -- <blend> <framedir> <fend> [az]
import bpy, sys, math, glob, os
from mathutils import Vector
argv=sys.argv[sys.argv.index("--")+1:]
blend=argv[0]; fdir=argv[1]; fend=int(argv[2])
az_deg=float(argv[3]) if len(argv)>3 else 39.0
bpy.ops.wm.open_mainfile(filepath=blend)
sc=bpy.context.scene
sc.render.engine='BLENDER_EEVEE'
try: sc.eevee.taa_render_samples=96
except Exception: pass
try: sc.eevee.use_shadows=True
except Exception: pass
sc.render.resolution_x=720; sc.render.resolution_y=1280
sc.render.film_transparent=False; sc.render.fps=30
for o in list(bpy.data.objects):
    if o.type=='CAMERA': bpy.data.objects.remove(o,do_unlink=True)
az=math.radians(az_deg)
out=Vector((math.sin(az),-math.cos(az),0.14)); out.normalize()
aim=Vector((0,0,-0.30)); loc=aim+5.9*out
cam=bpy.data.cameras.new("cam"); ob=bpy.data.objects.new("cam",cam)
sc.collection.objects.link(ob); ob.location=loc
d=(aim-loc).normalized(); ob.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
cam.lens=50; cam.sensor_fit='VERTICAL'; sc.camera=ob
if os.path.exists(fdir):
    for f in glob.glob(fdir+"/*.png"): os.remove(f)
os.makedirs(fdir,exist_ok=True)
sc.frame_start=0; sc.frame_end=fend
sc.render.image_settings.file_format='PNG'
sc.render.filepath=fdir+"/f_"
bpy.ops.render.render(animation=True)
print("FRAMES",len(glob.glob(fdir+"/f_*.png")))
