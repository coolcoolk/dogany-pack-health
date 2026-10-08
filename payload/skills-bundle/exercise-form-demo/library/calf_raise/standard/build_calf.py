# --- de-identified 2026-09-12 (pack carry-in): a shipped pack carries no
# --- absolute instance/home path. Roots resolve at runtime; override with
# --- FORM_DEMO_SKILL_ROOT / FORM_DEMO_WORK_ROOT / FORM_DEMO_OUT_ROOT.
import os as _os
_SKILL_ROOT = _os.environ.get("FORM_DEMO_SKILL_ROOT") or _os.path.abspath(
    _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", ".."))
_PROJECT_ROOT = _os.environ.get("PROJECT_ROOT") or _os.getcwd()
_WORK_ROOT = _os.environ.get("FORM_DEMO_WORK_ROOT") or _os.path.join(
    _PROJECT_ROOT, "files", "tmp")
_OUT_ROOT = _os.environ.get("FORM_DEMO_OUT_ROOT") or _os.path.join(
    _PROJECT_ROOT, "files", "outbox")
# --- end de-identification preamble ---
# Standing calf raise on the rigged bodybuilder.
# INVERTS the heels-down rule (correctly, per the movement): the BALL of each foot
# stays pinned on the floor, the heel + ankle RISE. Foot pivots about the ball; the
# body translates straight up with legs kept straight. flat -> rise onto balls (heels
# up) -> hold -> lower. start pose == end pose. no floating, no clipping.
import bpy, sys, math
from mathutils import Vector, Matrix
WORK=_os.path.join(_WORK_ROOT, "blender_work")
OUT=WORK+"/ex_build"
bpy.ops.wm.open_mainfile(filepath=WORK+"/rig3.blend")
mesh=bpy.data.objects["Body"]; rig=bpy.data.objects["Rig"]

bpy.ops.object.select_all(action='DESELECT')
mesh.select_set(True); bpy.context.view_layer.objects.active=mesh
bpy.ops.object.duplicate()
low=bpy.context.view_layer.objects.active; low.name="Body_low"
tris=sum(len(p.vertices)-2 for p in mesh.data.polygons)
dec=low.modifiers.new("Decimate",'DECIMATE'); dec.decimate_type='COLLAPSE'
dec.ratio=min(1.0,60000.0/float(tris))
while low.modifiers[0].name!="Decimate":
    bpy.ops.object.modifier_move_up(modifier="Decimate")
bpy.ops.object.modifier_apply(modifier="Decimate")
bpy.data.objects.remove(mesh,do_unlink=True)

for pb in rig.pose.bones: pb.rotation_mode='QUATERNION'
def reset_bind():
    for pb in rig.pose.bones:
        pb.rotation_quaternion=(1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
    bpy.context.view_layer.update()
def wrot(name,axis,deg):
    pb=rig.pose.bones[name]; M=pb.matrix.copy(); h=M.translation.copy()
    Rm=Matrix.Rotation(math.radians(deg),4,axis); T=Matrix.Translation(h)
    pb.matrix=T@Rm@T.inverted()@M; bpy.context.view_layer.update()
def hips_move(dy,dz):
    pb=rig.pose.bones['hips']; M=pb.matrix.copy()
    M.translation.y+=dy; M.translation.z+=dz; pb.matrix=M
    bpy.context.view_layer.update()
def bpos(name,tail=False):
    pb=rig.pose.bones[name]
    return (pb.matrix@Vector((0,pb.length,0))) if tail else pb.matrix.translation.copy()
def aim_world(name,d):
    pb=rig.pose.bones[name]; head=pb.matrix.translation.copy()
    q=Vector(d).normalized().to_track_quat('Y','Z')
    pb.matrix=Matrix.Translation(head)@q.to_matrix().to_4x4(); bpy.context.view_layer.update()
def set_seg(name,target):
    pb=rig.pose.bones[name]; m=pb.matrix; head=m.translation.copy(); cur=m.to_3x3()
    cdir=(cur@Vector((0,1,0))).normalized()
    q=cdir.rotation_difference(Vector(target).normalized())
    pb.matrix=Matrix.Translation(head)@(q.to_matrix()@cur).to_4x4(); bpy.context.view_layer.update()

L1=rig.pose.bones['thigh.L'].length; L2=rig.pose.bones['shin.L'].length
_HIPB={}; _ANKB={}; _BALL={}
def capture_bind():
    reset_bind()
    for s in ('.L','.R'):
        _HIPB[s]=rig.pose.bones['thigh'+s].matrix.translation.copy()
        _ANKB[s]=rig.pose.bones['foot'+s].matrix.translation.copy()
        _BALL[s]=(rig.pose.bones['toe'+s].matrix.translation.copy())  # toe head = ball, on floor

def solve_leg(side,ankle_target,hip_off,pole):
    Phip=_HIPB[side]+Vector(hip_off); A=Vector(ankle_target)
    base=A-Phip; d=base.length; d=min(d,L1+L2-1e-4); n=base.normalized()
    ca=max(-1.0,min(1.0,(L1*L1+d*d-L2*L2)/(2*L1*d))); a1=math.acos(ca)
    proj=L1*math.cos(a1); h=L1*math.sin(a1)
    f=Vector(pole); perp=f-(f.dot(n))*n
    if perp.length<1e-5:
        perp=Vector((0,0,-1)); perp=perp-(perp.dot(n))*n
    perp.normalize()
    K=Phip+proj*n+h*perp
    set_seg("thigh"+side, K-Phip); set_seg("shin"+side, A-K); return K

def arms_side():
    for s in ('.L','.R'):
        sgn=1.0 if s=='.L' else -1.0
        d=Vector((sgn*0.24,-0.16,-1.0))
        for bn in ("upper_arm"+s,"forearm"+s,"forearm_twist"+s,"hand"+s):
            aim_world(bn,d)

def smooth(a,b,f):
    if f<=a: return 0.0
    if f>=b: return 1.0
    x=(f-a)/(b-a); return x*x*(3-2*x)

F_UP0,F_UP1=12,72; F_HOLD=84; F_DN1=144; FEND=156
PHI_MAX=math.radians(54.0)   # rise HIGH onto the balls/toes (full plantarflexion)
def raise_t(f):
    if f<=F_UP1: return smooth(F_UP0,F_UP1,f)
    if f<=F_HOLD: return 1.0
    return 1.0-smooth(F_HOLD,F_DN1,f)

def ankle_for(side,phi):
    B=_BALL[side]; rel=_ANKB[side]-B
    y,z=rel.y,rel.z
    yp=y*math.cos(phi)-z*math.sin(phi); zp=y*math.sin(phi)+z*math.cos(phi)
    return B+Vector((0.0,yp,zp))

prefs=bpy.context.preferences.edit
prefs.keyframe_new_interpolation_type='BEZIER'
try: prefs.keyframe_new_handle_type='AUTO_CLAMPED'
except Exception as e: print("handle warn",e)

capture_bind()
for f in range(0,FEND+1):
    bpy.context.scene.frame_set(f)
    reset_bind()
    st=raise_t(f); phi=PHI_MAX*st
    # body rise = ankle delta (legs stay straight, translate up with body)
    dl=ankle_for(".L",phi)-_ANKB[".L"]; dr=ankle_for(".R",phi)-_ANKB[".R"]
    delta=0.5*(dl+dr)
    hips_move(delta.y,delta.z)
    for s in ('.L','.R'):
        A=ankle_for(s,phi)
        solve_leg(s,A,(0,delta.y,delta.z),(0.08 if s=='.L' else -0.08,-1,0.0))
        set_seg('foot'+s, _BALL[s]-bpos('foot'+s))          # heel up, ball planted
        set_seg('toe'+s, Vector((_BALL[s].x,_BALL[s].y-0.06,-0.985))-bpos('toe'+s))
    arms_side()
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion',frame=f)
    rig.pose.bones['hips'].keyframe_insert('location',frame=f)
    if f in (0,42,78,156):
        ball=bpos("toe.L"); ank=bpos("foot.L"); heel=ank+(ank-bpos("shin.L")).normalized()*0.0
        # heel-ground clearance proxy: ankle z rise
        knee=bpos("shin.L"); kneeang=math.degrees((bpos("thigh.L")-knee).angle(ank-knee))
        print("F%03d st=%.2f phi=%.1fdeg | ballZ=%.3f ballY=%.3f (planted) ankZ=%.3f (rise=%.3f) "
              "hipZ=%.3f kneeAng=%.1f"%(f,st,math.degrees(phi),ball.z,ball.y,ank.z,ank.z-(-0.860),
              bpos("hips").z,kneeang))

sc=bpy.context.scene
sc.frame_start=0; sc.frame_end=FEND; sc.render.fps=30
bpy.ops.mesh.primitive_plane_add(size=14.0, location=(0,0,-1.001))
plane=bpy.context.active_object; plane.name="Ground"
gmat=bpy.data.materials.new("GroundMat"); gmat.use_nodes=True
bsdf=gmat.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value=(0.030,0.030,0.038,1.0); bsdf.inputs["Roughness"].default_value=0.7
plane.data.materials.append(gmat)
if sc.world is None: sc.world=bpy.data.worlds.new('W')
sc.world.use_nodes=True
bg=sc.world.node_tree.nodes.get('Background')
bg.inputs[0].default_value=(0.012,0.012,0.018,1.0); bg.inputs[1].default_value=1.0
try:
    sc.view_settings.view_transform='Standard'; sc.view_settings.look='None'
except Exception as e: print("vt warn",e)
LIGHTS=(((66,0,10),2.8,6.0),((72,0,0),1.1,16.0),((46,0,-34),0.7,14.0),((115,0,190),3.6,4.0))
for ang,en,sa in LIGHTS:
    lt=bpy.data.lights.new("sun",'SUN'); lt.energy=en
    try: lt.angle=math.radians(sa)
    except Exception: pass
    lo=bpy.data.objects.new("sun",lt); bpy.context.collection.objects.link(lo)
    lo.rotation_euler=(math.radians(ang[0]),math.radians(ang[1]),math.radians(ang[2]))
bpy.ops.wm.save_as_mainfile(filepath=OUT+"/calf_raise.blend")
print("SAVED calf_raise.blend")
