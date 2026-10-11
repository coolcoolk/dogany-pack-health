# calf-raise QA stills: lower-body 3/4 framing (thigh-down to feet) so the heel lift
# reads clearly. usage: blender -b --python calf_stills.py -- <blend> <outprefix>
import bpy, sys, math
from mathutils import Vector
argv=sys.argv[sys.argv.index("--")+1:]
blend=argv[0]; outp=argv[1]
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
az=math.radians(39.0)
out=Vector((math.sin(az),-math.cos(az),0.20)); out.normalize()
aim=Vector((0,-0.05,-0.66))          # lower body (hips-down to feet)
loc=aim+3.4*out
cam=bpy.data.cameras.new("cam"); ob=bpy.data.objects.new("cam",cam)
sc.collection.objects.link(ob); ob.location=loc
d=(aim-loc).normalized(); ob.rotation_euler=d.to_track_quat('-Z','Y').to_euler()
cam.lens=50; cam.sensor_fit='VERTICAL'; sc.camera=ob
for f,tag in ((0,"top"),(42,"mid"),(78,"bottom")):
    sc.frame_set(f)
    sc.render.filepath=outp+tag+".png"
    bpy.ops.render.render(write_still=True)
    print("RENDERED",tag,f)
