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
# Build a bodyweight squat rep on the rigged bodybuilder.
# Legs use a per-frame analytic 2-link IK: hip joint is driven (hinge back+down),
# ankle is pinned (planted), thigh+shin solve to reach it, foot is re-flattened to
# bind orientation every frame -> soles stay flat on the floor at every frame.
import bpy, sys, math, glob, os
sys.path.append(_os.path.join(_WORK_ROOT, "blender_work"))
from mathutils import Vector, Matrix

WORK=_os.path.join(_WORK_ROOT, "blender_work")
bpy.ops.wm.open_mainfile(filepath=WORK+"/rig3.blend")
mesh=bpy.data.objects["Body"]; rig=bpy.data.objects["Rig"]

# ---- low-poly copy (same skeleton/weights) for fast render ----
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
print("LOW_TRIS",sum(len(p.vertices)-2 for p in low.data.polygons))

for pb in rig.pose.bones:
    pb.rotation_mode='QUATERNION'

def reset_bind():
    for pb in rig.pose.bones:
        pb.rotation_quaternion=(1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
    bpy.context.view_layer.update()

def wrot(name,axis,deg):
    pb=rig.pose.bones[name]; M=pb.matrix.copy(); h=M.translation.copy()
    Rm=Matrix.Rotation(math.radians(deg),4,axis); T=Matrix.Translation(h)
    pb.matrix=T@Rm@T.inverted()@M
    bpy.context.view_layer.update()

def hips_move(dy,dz):
    pb=rig.pose.bones['hips']; M=pb.matrix.copy()
    M.translation.y+=dy; M.translation.z+=dz; pb.matrix=M
    bpy.context.view_layer.update()

def cur_dir_yz(name):
    # world head->tail direction of a pose bone, projected to (y,z)
    d=rig.pose.bones[name].matrix.to_3x3()@Vector((0,1,0))
    return Vector((d.y,d.z))

def head_yz(name):
    t=rig.pose.bones[name].matrix.translation
    return Vector((t.y,t.z))

def signed_x(u,v):
    # signed angle (deg) about +X taking dir u -> dir v, u,v are (y,z)
    cross=u.x*v.y-u.y*v.x; dot=u.x*v.x+u.y*v.y
    return math.degrees(math.atan2(cross,dot))

def align(name,target_yz):
    wrot(name,'X',signed_x(cur_dir_yz(name),target_yz))

def aim_world(name,d):
    # point a bone's Y axis (head->tail) along world direction d, keep head fixed.
    pb=rig.pose.bones[name]; head=pb.matrix.translation.copy()
    q=Vector(d).normalized().to_track_quat('Y','Z')
    pb.matrix=Matrix.Translation(head)@q.to_matrix().to_4x4()
    bpy.context.view_layer.update()

def bpos(name,tail=False):
    pb=rig.pose.bones[name]
    return (pb.matrix@Vector((0,pb.length,0))) if tail else pb.matrix.translation.copy()

# ---- 3D leg IK: hip driven, ankle pinned on the floor, knee tracked OUT over the
#      toes by rotating the IK pole around the hip->ankle axis (feet stay planted).
#      Actual bone lengths so the shin tail lands exactly on the pinned ankle. ----
L1=rig.pose.bones['thigh.L'].length   # thigh
L2=rig.pose.bones['shin.L'].length    # shin
KNEE_BIAS=0.28   # forward+OUT pole bias -> knee tracks out over the 2nd-3rd toe
TOE_OUT=math.radians(12.0)  # feet turned slightly out (sole stays flat = Z yaw)

# bind (identity-pose) references captured once
_HIPB={}; _ANKB={}; _FOOTB={}
def capture_bind():
    reset_bind()
    for s in ('.L','.R'):
        _HIPB[s]=rig.pose.bones['thigh'+s].matrix.translation.copy()
        _ANKB[s]=rig.pose.bones['foot'+s].matrix.translation.copy()
        _FOOTB[s]=rig.pose.bones['foot'+s].matrix.to_3x3().copy()

def set_seg(name,target):
    # rotate a bone's current orientation by the MINIMAL rotation that points its
    # Y axis at `target` (twist-free -> keeps bind roll). Head stays fixed.
    pb=rig.pose.bones[name]; m=pb.matrix; head=m.translation.copy(); cur=m.to_3x3()
    cdir=(cur@Vector((0,1,0))).normalized()
    q=cdir.rotation_difference(Vector(target).normalized())
    pb.matrix=Matrix.Translation(head)@(q.to_matrix()@cur).to_4x4()
    bpy.context.view_layer.update()

def set_foot(side,sc):
    # force bind-flat sole (sole stays on the floor) + slight toe-out yaw about world Z
    pb=rig.pose.bones['foot'+side]; head=pb.matrix.translation.copy()
    rot=Matrix.Rotation(sc*TOE_OUT,4,'Z').to_3x3()@_FOOTB[side]
    pb.matrix=Matrix.Translation(head)@rot.to_4x4()
    bpy.context.view_layer.update()

def solve_leg(side,sc,dy,dz):
    Phip=_HIPB[side]+Vector((0,dy,dz))
    A=_ANKB[side]                       # pinned on the floor
    base=A-Phip; d=base.length; d=min(d,L1+L2-1e-4)
    n=base.normalized()
    ca=max(-1.0,min(1.0,(L1*L1+d*d-L2*L2)/(2*L1*d))); a1=math.acos(ca)
    proj=L1*math.cos(a1); h=L1*math.sin(a1)
    f=Vector((sc*KNEE_BIAS,-1,0))       # forward + OUTward -> knee bows out over toes
    perp=f-(f.dot(n))*n
    if perp.length<1e-5:
        perp=Vector((0,0,-1)); perp=perp-(perp.dot(n))*n
    perp.normalize()
    K=Phip+proj*n+h*perp
    set_seg("thigh"+side, K-Phip)
    set_seg("shin"+side, A-K)
    set_foot(side,sc)

# ---- arms: T-pose -> extended forward (counterbalance) ----
def arms(t):
    # Straight-forward, PARALLEL front-raise hold: both arms point world -Y
    # (forward, horizontal), each from its own shoulder -> shoulder-width apart,
    # forearms parallel to the floor and to each other, hands NOT touching.
    # World-space aim so they stay horizontal even as the torso leans.
    fwd=Vector((0,-1,0))
    for s in ('.L','.R'):
        for bn in ("upper_arm"+s,"forearm"+s,"forearm_twist"+s,"hand"+s):
            aim_world(bn,fwd)

def torso(t):
    # Forward torso lean (hip hinge). Slightly more upright than before for a clean
    # high-bar look; COM kept over midfoot by knees/shins traveling a bit more forward.
    if t<=0: return
    wrot("spine",'X',8*t); wrot("spine.001",'X',12*t); wrot("spine.002",'X',12*t)

def gaze(t):
    # Neutral gaze: counter the torso lean at the neck/head so the face looks
    # forward-and-slightly-down (no chin-to-chest tuck) through the whole rep.
    if t<=0: return
    wrot("neck",'X',-9*t); wrot("head",'X',-9*t)

def smooth(a,b,f):
    if f<=a: return 0.0
    if f>=b: return 1.0
    x=(f-a)/(b-a); return x*x*(3-2*x)

# ---- timeline (30 fps): NO T-pose intro. Frame 0 is already the ready stance
#      (arms forward the whole time). ready -> descend -> hold -> ascend -> ready.
#      start pose == end pose -> loop-friendly.
F_DN0,F_DN1=12,72
F_HOLD=84
F_UP1=144
FEND=156
DZ,DY=-0.55,0.09

def squat_t(f):
    if f<=F_DN1: return smooth(F_DN0,F_DN1,f)
    if f<=F_HOLD: return 1.0
    return 1.0-smooth(F_HOLD,F_UP1,f)

prefs=bpy.context.preferences.edit
prefs.keyframe_new_interpolation_type='BEZIER'
try: prefs.keyframe_new_handle_type='AUTO_CLAMPED'
except Exception as e: print("handle warn",e)

capture_bind()
for f in range(0,FEND+1):
    bpy.context.scene.frame_set(f)
    reset_bind()
    at=1.0; st=squat_t(f)   # arms already in ready position at every frame
    dy=DY*st; dz=DZ*st
    hips_move(dy,dz)
    torso(st); gaze(st); arms(at)
    solve_leg(".L",1.0,dy,dz); solve_leg(".R",-1.0,dy,dz)
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion',frame=f)
    rig.pose.bones['hips'].keyframe_insert('location',frame=f)
    if f in (0,42,78,156):
        hip=bpos("thigh.L"); knee=bpos("shin.L"); ank=bpos("foot.L")
        toe=bpos("toe.L",True)
        midfoot=0.5*(0.09+toe.y)  # heel~+0.09 .. toe tip
        shin_ang=math.degrees(math.atan2(abs(ank.y-knee.y),abs(ank.z-knee.z)))
        # crude COM (upper body + limbs), y only, at this frame
        segs=[(0.14,bpos("hips")),
              (0.33,(bpos("spine")+bpos("neck"))/2),
              (0.08,bpos("head",True)),
              (0.05,(bpos("shoulder.L")+bpos("hand.L"))/2),
              (0.05,(bpos("shoulder.R")+bpos("hand.R"))/2),
              (0.10,(bpos("thigh.L")+bpos("shin.L"))/2),
              (0.10,(bpos("thigh.R")+bpos("shin.R"))/2),
              (0.075,(bpos("shin.L")+bpos("foot.L"))/2),
              (0.075,(bpos("shin.R")+bpos("foot.R"))/2)]
        comy=sum(w*p.y for w,p in segs)/sum(w for w,_ in segs)
        footx=bpos("foot.L").x; toex=bpos("toe.L",True).x  # knees-out check vs foot
        print("F%03d st=%.2f hipY=%.3f kneeY=%.3f kneeX=%.3f footX=%.3f toeX=%.3f "
              "ankleZ=%.3f midfootY=%.3f shin=%.1fdeg COMy=%.3f par=%.3f"%(
              f,st,hip.y,knee.y,knee.x,footx,toex,ank.z,midfoot,shin_ang,comy,hip.z-knee.z))

sc=bpy.context.scene
sc.frame_start=0; sc.frame_end=FEND; sc.render.fps=30

# ---- DARK studio: near-black backdrop, dark floor (a touch lighter so it reads),
#      key + fill + rim so the light-skin model pops and stays defined. ----
bpy.ops.mesh.primitive_plane_add(size=14.0, location=(0,0,-1.001))
plane=bpy.context.active_object; plane.name="Ground"
gm=bpy.data.materials.new("GroundMat"); gm.use_nodes=True
bsdf=gm.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value=(0.030,0.030,0.038,1.0)  # dark, > backdrop
bsdf.inputs["Roughness"].default_value=0.7
plane.data.materials.append(gm)

if sc.world is None: sc.world=bpy.data.worlds.new('W')
sc.world.use_nodes=True
bg=sc.world.node_tree.nodes.get('Background')
bg.inputs[0].default_value=(0.012,0.012,0.018,1.0)  # near-black charcoal
bg.inputs[1].default_value=1.0

# Standard view transform: the dark floor stays genuinely dark while the high-albedo
# skin still reads bright -> strong contrast without AgX lifting the floor to grey.
try:
    sc.view_settings.view_transform='Standard'; sc.view_settings.look='None'
except Exception as e: print("vt warn",e)
print("VIEW_TRANSFORM", sc.view_settings.view_transform)
print("GROUND_MAT", plane.data.materials[0].name if plane.data.materials else "NONE")

# suns: (rot_euler_deg, energy, soft_angle_deg). key front-high (even chest light);
# broad frontal fill washes the arm-cast torso shadow; side fill shapes; rim behind-top
# gives a bright edge that separates the model from the near-black backdrop.
LIGHTS=(
    ((66,  0,  10), 2.8,  6.0),  # key  (front, high, gently soft)
    ((72,  0,   0), 1.1, 16.0),  # frontal fill (broad -> lifts torso shadow)
    ((46,  0, -34), 0.7, 14.0),  # side fill (front-right, subtle shaping)
    ((115, 0, 190), 3.6,  4.0),  # rim  (behind + above -> bright edge)
)
for ang,en,sa in LIGHTS:
    lt=bpy.data.lights.new("sun",'SUN'); lt.energy=en
    try: lt.angle=math.radians(sa)
    except Exception: pass
    lo=bpy.data.objects.new("sun",lt); bpy.context.collection.objects.link(lo)
    lo.rotation_euler=(math.radians(ang[0]),math.radians(ang[1]),math.radians(ang[2]))

bpy.ops.wm.save_as_mainfile(filepath=WORK+"/squat.blend")
print("SAVED squat.blend  L1=%.3f L2=%.3f"%(L1,L2))
