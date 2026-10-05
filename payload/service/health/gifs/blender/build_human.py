import bpy, importlib, os, tempfile

# Scratch dir for this prototype. Override with BLENDER_WORK.
WORK = os.environ.get("BLENDER_WORK", os.path.join(tempfile.gettempdir(), "blender_work"))
os.makedirs(WORK, exist_ok=True)
HS = importlib.import_module("bl_ext.user_default.mpfb.services.humanservice").HumanService
# clean scene
bpy.ops.wm.read_factory_settings(use_empty=True)
macro = {"gender":1.0,"age":0.5,"muscle":0.92,"weight":0.55,"proportions":0.5,
         "height":0.6,"cupsize":0.5,"firmness":0.5,
         "race":{"asian":0.0,"caucasian":1.0,"african":0.0}}
basemesh = HS.create_human(macro_detail_dict=macro)
print("BASEMESH", basemesh.name, "verts", len(basemesh.data.vertices))
# add default rig
try:
    HS.add_builtin_rig(basemesh, "default")
    print("RIG default OK")
except Exception as e:
    print("RIG default FAIL", e)
# find armature
arm = None
for o in bpy.data.objects:
    if o.type=='ARMATURE':
        arm=o; break
print("ARMATURE", arm.name if arm else None)
if arm:
    names=[b.name for b in arm.data.bones]
    print("NBONES", len(names))
    # print arm/shoulder related
    for n in names:
        low=n.lower()
        if any(k in low for k in ("clav","shoulder","upperarm","lowerarm","hand","spine","chest","pect","breast")):
            print("BONE", n)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(WORK, "human.blend"))
print("SAVED")
