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
import bpy, sys, os
sys.path.append(_os.path.join(_WORK_ROOT, "blender_work"))
import lib_rig2 as R

WORK = _os.path.join(_WORK_ROOT, "blender_work")
OUT = _os.path.join(_OUT_ROOT, "rigged")
os.makedirs(OUT, exist_ok=True)

bpy.ops.wm.open_mainfile(filepath=WORK + "/rig3.blend")
mesh = bpy.data.objects["Body"]
rig = bpy.data.objects["Rig"]

R.reset_pose(rig)
try: bpy.ops.file.pack_all()
except Exception as e: print("pack warn", e)

tris = sum(len(p.vertices) - 2 for p in mesh.data.polygons)
ndef = sum(1 for b in rig.data.bones if b.use_deform)
print("FULL_TRIS", tris, "VERTS", len(mesh.data.vertices), "DEFORM_BONES", ndef)

def export_glb(path, objs):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.export_scene.gltf(
        filepath=path, export_format='GLB', use_selection=True,
        export_apply=False, export_skins=True, export_yup=True,
        export_image_format='AUTO', export_texcoords=True, export_normals=True,
        export_materials='EXPORT')

full = OUT + "/bodybuilder_rigged_v2.glb"
export_glb(full, [rig, mesh])
print("EXPORTED_FULL", full, os.path.getsize(full))

# low-poly: decimate BEFORE armature so manual weights interpolate onto the reduced mesh
bpy.ops.object.select_all(action='DESELECT')
mesh.select_set(True); bpy.context.view_layer.objects.active = mesh
bpy.ops.object.duplicate()
low = bpy.context.view_layer.objects.active; low.name = "Body_low"
dec = low.modifiers.new("Decimate", 'DECIMATE'); dec.decimate_type = 'COLLAPSE'
dec.ratio = min(1.0, 50000.0 / float(tris))
while low.modifiers[0].name != "Decimate":
    bpy.ops.object.modifier_move_up(modifier="Decimate")
bpy.ops.object.modifier_apply(modifier="Decimate")
low_tris = sum(len(p.vertices) - 2 for p in low.data.polygons)
# report how many verts still carry finger/thumb weights after decimation
def carriers(obj, names):
    gi = {obj.vertex_groups[n].index for n in names if obj.vertex_groups.get(n)}
    return sum(1 for v in obj.data.vertices for g in v.groups if g.group in gi and g.weight > 0.05)
hn = ["thumb_01.L","thumb_02.L","fingers_01.L","fingers_02.L","thumb_01.R","thumb_02.R","fingers_01.R","fingers_02.R"]
print("LOW_TRIS", low_tris, "VERTS", len(low.data.vertices), "HAND_WEIGHT_CARRIERS", carriers(low, hn))

lowpath = OUT + "/bodybuilder_rigged_v2_lowpoly.glb"
export_glb(lowpath, [rig, low])
print("EXPORTED_LOW", lowpath, os.path.getsize(lowpath))
