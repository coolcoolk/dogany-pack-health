# Generic QA stills. Usage:
#  blender -b --python stills.py -- <blend> <outprefix> <ftop> <fmid> <fbot> [az]
import bpy, sys, math
from mathutils import Vector
argv=sys.argv[sys.argv.index("--")+1:]
blend=argv[0]; outp=argv[1]
ftop,fmid,fbot=int(argv[2]),int(argv[3]),int(argv[4])
az_deg=float(argv[5]) if len(argv)>5 else 39.0
bpy.ops.wm.open_mainfile(filepath=blend)
sc=bpy.context.scene
sc.render.engine='BLENDER_EEVEE'
try: sc.eevee.taa_render_samples=96
except Exception: pass
try: sc.eevee.use_shadows=True
except Exception: pass
sc.render.resolution_x=720; sc.render.resolution_y=1280
sc.render.film_transparent=False
for o in list(bpy.data.objects):
    if o.type=='CAMERA': bpy.data.objects.remove(o,do_unlink=True)
az=math.radians(az_deg)
out=Vector((math.sin(az),-math.cos(az),0.14)); out.normalize()
aim=Vector((0,0,-0.30)); loc=aim+5.9*out
cam=bpy.data.cameras.new("cam"); ob=bpy.data.objects.new("cam",cam)
sc.collection.objects.link(ob); ob.location=loc
d=(aim-loc).normalized(); ob.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
cam.lens=50; cam.sensor_fit='VERTICAL'; sc.camera=ob
for f,tag in ((ftop,"top"),(fmid,"mid"),(fbot,"bottom")):
    sc.frame_set(f)
    sc.render.filepath=outp+tag+".png"
    bpy.ops.render.render(write_still=True)
    print("RENDERED",tag,f)
