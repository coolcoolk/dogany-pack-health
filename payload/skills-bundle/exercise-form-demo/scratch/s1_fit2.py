"""S1 fit v3 -- FIX: donor carries 11 MPFB shape keys, so editing me.vertices.co
was ignored by the renderer (it used shape-key data at the old MakeHuman location
-> hand invisible at wrist). Here we FLATTEN shape keys (bake current mix into a
plain mesh) FIRST, then apply the same rigid+uniform-scale fit, then force a
bound_box refresh so the renderer no longer frustum-culls it."""
import bpy, os, math, bmesh
from mathutils import Vector, Matrix
HERE=os.path.dirname(os.path.abspath(__file__))
BODY=os.path.dirname(HERE)+"/assets/rig/bodybuilder_rigged_v4_r8_lowpoly.glb"

D_WRIST=Vector((0.431,-0.176,1.063)); D_ELBOW=Vector((0.313,-0.013,1.167))
D_ROOT={"index":Vector((0.450,-0.264,1.021)),"middle":Vector((0.461,-0.248,1.006)),
        "ring":Vector((0.470,-0.231,1.000)),"pinky":Vector((0.475,-0.212,0.994))}
D_THUMB=Vector((0.420,-0.213,1.048)); D_TIP_MID=Vector((0.478,-0.301,0.948))
d_fwd=(sum(D_ROOT.values(),Vector())/4.0-D_WRIST).normalized()
d_across=(D_ROOT["pinky"]-D_ROOT["index"]).normalized()
d_forearm_len=(D_WRIST-D_ELBOW).length
T_WRIST=Vector((0.7800,0.0200,0.5300)); T_FORE_HEAD=Vector((0.510,0.030,0.550))
T_ARMAXIS=Vector((0.9966,-0.0369,-0.0738)).normalized()
T_ACROSS=Vector((-0.0199,0.9993,-0.0319)).normalized(); T_FWD=T_ARMAXIS
t_forearm_len=(T_WRIST-T_FORE_HEAD).length
SCALE=t_forearm_len/d_forearm_len
print("SCALE=%.4f"%SCALE)
def ortho_basis(fwd,across):
    u1=fwd.normalized();u3=u1.cross(across).normalized();u2=u3.cross(u1).normalized()
    return Matrix((u1,u2,u3)).transposed()
Rmap=ortho_basis(T_FWD,T_ACROSS)@ortho_basis(d_fwd,d_across).transposed()
print("det(Rmap)=%.4f"%Rmap.determinant())
def xform(p): return T_WRIST+Rmap@(p-D_WRIST)*SCALE

bpy.ops.wm.open_mainfile(filepath=os.path.join(HERE,"donor_hand_L.blend"))
donor=max([o for o in bpy.data.objects if o.type=='MESH'],key=lambda o:len(o.data.vertices))
# --- FLATTEN shape keys: bake evaluated mesh (shape keys applied) into plain mesh ---
bpy.context.view_layer.objects.active=donor
dg=bpy.context.evaluated_depsgraph_get()
newme=bpy.data.meshes.new_from_object(donor.evaluated_get(dg))
old=donor.data; donor.data=newme
if old.users==0: bpy.data.meshes.remove(old)
print("flattened -> shape_keys:",donor.data.shape_keys, "verts:",len(donor.data.vertices))
# --- apply fit to real verts (now renderable) ---
mw=donor.matrix_world
for v in donor.data.vertices: v.co=xform(mw@v.co)
donor.matrix_world=Matrix.Identity(4); donor.data.update()
# --- force bound_box refresh (edit-toggle now works: no shape keys) ---
donor.select_set(True)
bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.object.mode_set(mode='OBJECT')
bpy.context.view_layer.update()
bb=donor.bound_box
print("bound_box now:",[round(bb[0][i],3) for i in range(3)],"->",[round(bb[6][i],3) for i in range(3)])
print("dims:",[round(x,3) for x in donor.dimensions])
# --- gate ---
mk=sum((xform(D_ROOT[f]) for f in D_ROOT),Vector())/4.0; mt=xform(D_THUMB); mtip=xform(D_TIP_MID)
ratio=(mtip-T_WRIST).length/t_forearm_len
print("=== GATE ===")
print("thumb y=%.4f vs knuckle y=%.4f -> %s"%(mt.y,mk.y,"PASS" if mt.y<mk.y else "FAIL"))
print("hand:forearm ratio=%.3f -> %s"%(ratio,"PASS" if 0.68<=ratio<=0.87 else "FAIL"))
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE,"donor_hand_L_fit.blend"))
bpy.ops.object.select_all(action='DESELECT'); donor.select_set(True)
bpy.context.view_layer.objects.active=donor
bpy.ops.export_scene.gltf(filepath=os.path.join(HERE,"donor_hand_L_fit.glb"),use_selection=True,export_format='GLB',export_yup=True)
print("SAVED")
