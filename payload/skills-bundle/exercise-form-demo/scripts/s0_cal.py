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
import bpy, sys
sys.path.append(_os.path.join(_WORK_ROOT, "blender_work"))
from mathutils import Vector
WORK=_os.path.join(_WORK_ROOT, "blender_work")
bpy.ops.wm.open_mainfile(filepath=WORK+"/rig3.blend")
mesh=bpy.data.objects["Body"]; rig=bpy.data.objects["Rig"]
# mesh world bbox
dg=bpy.context.evaluated_depsgraph_get(); ev=mesh.evaluated_get(dg)
mn=Vector((1e18,)*3); mx=Vector((-1e18,)*3)
for v in ev.data.vertices:
    w=ev.matrix_world@v.co
    for i in range(3):
        mn[i]=min(mn[i],w[i]); mx[i]=max(mx[i],w[i])
print("MESH_BBOX min",[round(x,3) for x in mn],"max",[round(x,3) for x in mx])
# bone head/tail world (rig at identity presumably)
print("RIG matrix_world translation", [round(x,3) for x in rig.matrix_world.translation])
for bn in ["hips","thigh.L","shin.L","foot.L","toe.L","spine","spine.002"]:
    b=rig.data.bones[bn]
    h=rig.matrix_world@b.head_local; t=rig.matrix_world@b.tail_local
    print(bn,"head",[round(x,3) for x in h],"tail",[round(x,3) for x in t])
