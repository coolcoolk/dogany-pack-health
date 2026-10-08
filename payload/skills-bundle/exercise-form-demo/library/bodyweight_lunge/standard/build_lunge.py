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
# Bodyweight lunge on the v3 rigged bodybuilder (3-segment fingers, smooth grip).
# Static split-stance forward lunge; both feet grounded every frame.
#   FRONT foot (.L) flat + planted, stepped forward (-Y);
#   REAR foot (.R) ball-down / heel-up, stepped back (+Y);
# Rep = descend into lunge (front knee ~90 over ankle, back knee toward floor,
# torso upright) -> hold -> stand. start pose == end pose (loop-friendly).
#
# v3 rig changes vs the original hands-on-hips build:
#  (a) AKIMBO hands-on-hips (natural orientation) using the v3 3-segment finger
#      curl -- BACK of the hand faces UP/out, PALM faces DOWN + IN on top of the
#      iliac crest (palm-on-hip); the four grouped FINGERS drape FORWARD over the
#      front of the hip; the THUMB hooks BACK (posterior) toward the glute/spine;
#      elbows flared out + slightly back. Posed on the LEFT arm only then X-mirrored
#      to the RIGHT (rig is X-symmetric) so both hands are artifact-free.
#      Full-res (symmetric) mesh is used so the grouped-finger deform stays clean
#      (the decimated lowpoly breaks left/right topology -> right-hand seams).
#  (b) feet raised so soles sit ON the floor (a few mm above the plane), no clip.
import bpy, sys, math
from mathutils import Vector, Matrix
GLB=_os.path.join(_SKILL_ROOT, "assets/rig/bodybuilder_rigged_v3.glb")
WORK=_os.path.join(_WORK_ROOT, "blender_work")
OUT=WORK+"/ex_build"

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB)
mesh=max([o for o in bpy.data.objects if o.type=='MESH'],key=lambda o:len(o.data.vertices))
for o in list(bpy.data.objects):
    if o.type=='MESH' and o is not mesh:
        bpy.data.objects.remove(o,do_unlink=True)   # drop stray helper meshes
rig=[o for o in bpy.data.objects if o.type=='ARMATURE'][0]
mesh.name="Body"; rig.name="Rig"

for pb in rig.pose.bones: pb.rotation_mode='QUATERNION'

def reset_bind():
    for pb in rig.pose.bones:
        pb.rotation_quaternion=(1,0,0,0); pb.location=(0,0,0); pb.scale=(1,1,1)
    bpy.context.view_layer.update()

def wrot(name,axis,deg):
    pb=rig.pose.bones[name]; M=pb.matrix.copy(); h=M.translation.copy()
    Rm=Matrix.Rotation(math.radians(deg),4,axis); T=Matrix.Translation(h)
    pb.matrix=T@Rm@T.inverted()@M; bpy.context.view_layer.update()

def wrot_axis(name,axis_vec,deg):
    pb=rig.pose.bones[name]; M=pb.matrix.copy(); h=M.translation.copy()
    Rm=Matrix.Rotation(math.radians(deg),4,Vector(axis_vec).normalized()); T=Matrix.Translation(h)
    pb.matrix=T@Rm@T.inverted()@M; bpy.context.view_layer.update()

def curl_localx(name,deg):
    # rotate a bone about its OWN local X axis (the knuckle/flex axis) through its head
    pb=rig.pose.bones[name]; M=pb.matrix
    axis=(M.to_3x3()@Vector((1,0,0))).normalized()
    wrot_axis(name,axis,deg)

def _curl_sign(name,palm_normal):
    # +1 or -1 so a positive curl flexes the fingertip toward the palm side
    # (opposite the palm normal). Probe with a small test rotation, then undo.
    pb=rig.pose.bones[name]
    tip0=(pb.matrix@Vector((0,pb.length,0)))
    axis=(pb.matrix.to_3x3()@Vector((1,0,0))).normalized()
    wrot_axis(name,axis,10.0)
    tip1=(pb.matrix@Vector((0,pb.length,0)))
    wrot_axis(name,axis,-10.0)   # undo
    moved=(tip1-tip0).dot(-Vector(palm_normal).normalized())
    return 1.0 if moved>0 else -1.0

def set_frame_x(name,ydir,xdir):
    # set a bone's world orientation: local Y along ydir, local X toward xdir
    # (the knuckle/flex axis -- used as the well-conditioned roll reference,
    # since it is ~horizontal while the bone length is ~vertical). head fixed.
    pb=rig.pose.bones[name]; head=pb.matrix.translation.copy()
    y=Vector(ydir).normalized()
    x=Vector(xdir); x=(x-x.dot(y)*y).normalized()
    z=x.cross(y).normalized(); x=y.cross(z).normalized()
    M3=Matrix((x,y,z)).transposed()   # columns x,y,z (right-handed)
    pb.matrix=Matrix.Translation(head)@M3.to_4x4(); bpy.context.view_layer.update()

def hips_move(dy,dz):
    pb=rig.pose.bones['hips']; M=pb.matrix.copy()
    M.translation.y+=dy; M.translation.z+=dz; pb.matrix=M
    bpy.context.view_layer.update()

def bpos(name,tail=False):
    pb=rig.pose.bones[name]
    return (pb.matrix@Vector((0,pb.length,0))) if tail else pb.matrix.translation.copy()

def set_seg(name,target):
    pb=rig.pose.bones[name]; m=pb.matrix; head=m.translation.copy(); cur=m.to_3x3()
    cdir=(cur@Vector((0,1,0))).normalized()
    q=cdir.rotation_difference(Vector(target).normalized())
    pb.matrix=Matrix.Translation(head)@(q.to_matrix()@cur).to_4x4()
    bpy.context.view_layer.update()

L1=rig.pose.bones['thigh.L'].length
L2=rig.pose.bones['shin.L'].length

_HIPB={}; _ANKB={}; _FOOTB={}
def capture_bind():
    reset_bind()
    for s in ('.L','.R'):
        _HIPB[s]=rig.pose.bones['thigh'+s].matrix.translation.copy()
        _ANKB[s]=rig.pose.bones['foot'+s].matrix.translation.copy()
        _FOOTB[s]=rig.pose.bones['foot'+s].matrix.to_3x3().copy()

def solve_leg(side,ankle_target,hip_off,pole):
    # analytic 2-link IK: hip driven, ankle pinned at ankle_target, knee via pole.
    Phip=_HIPB[side]+Vector(hip_off)
    A=Vector(ankle_target)
    base=A-Phip; d=base.length; d=min(d,L1+L2-1e-4)
    n=base.normalized()
    ca=max(-1.0,min(1.0,(L1*L1+d*d-L2*L2)/(2*L1*d))); a1=math.acos(ca)
    proj=L1*math.cos(a1); h=L1*math.sin(a1)
    f=Vector(pole); perp=f-(f.dot(n))*n
    if perp.length<1e-5:
        perp=Vector((0,0,-1)); perp=perp-(perp.dot(n))*n
    perp.normalize()
    K=Phip+proj*n+h*perp
    set_seg("thigh"+side, K-Phip)
    set_seg("shin"+side, A-K)
    return K

def flat_foot(side,sc):
    pb=rig.pose.bones['foot'+side]; head=pb.matrix.translation.copy()
    TOE_OUT=math.radians(10.0)
    rot=Matrix.Rotation(sc*TOE_OUT,4,'Z').to_3x3()@_FOOTB[side]
    pb.matrix=Matrix.Translation(head)@rot.to_4x4(); bpy.context.view_layer.update()

def aim_foot(side,ball_target):
    set_seg('foot'+side, Vector(ball_target)-bpos('foot'+side))
def aim_toe(side,ground):
    set_seg('toe'+side, Vector(ground)-bpos('toe'+side))

def torso(t):
    if t<=0: return
    wrot("spine",'X',3*t); wrot("spine.001",'X',5*t); wrot("spine.002",'X',5*t)
def gaze(t):
    if t<=0: return
    wrot("neck",'X',-4*t); wrot("head",'X',-4*t)

# tunables for the akimbo hand pose (corrected orientation)
FCURL=(14.0,18.0,14.0)   # per-segment (MCP,PIP,DIP) finger flex -- relaxed natural curl

# ---- AKIMBO hands on hips (v3): back-of-hand UP, palm DOWN + IN on the crest, ----
# ---- FOUR FINGERS drape FORWARD over the front of the hip, THUMB hooks BACK. -----
def arms_akimbo():
    pelvis=bpos('hips')
    up_t=(bpos('neck')-bpos('spine.001')).normalized()
    side_t=(bpos('shoulder.L')-bpos('shoulder.R')).normalized()   # +X toward LEFT
    front_t=side_t.cross(up_t)
    if front_t.y>0: front_t=-front_t          # front_t points -Y (anterior, face side)
    back_t=-front_t                            # +Y (posterior, toward glute)
    # pose the LEFT arm/hand only (reference), then X-mirror to the RIGHT.
    s='.L'; sgn=1.0
    out=side_t*sgn                             # lateral (away from body center)
    inw=-out                                   # medial (toward body center / hip)
    sh=bpos('upper_arm'+s)
    # wrist ON the side of the waist, seated HIGH at the iliac crest / waist notch,
    # just ABOVE the shorts waistband (raised ~6cm vs the old low-on-shorts spot;
    # lateral pulled in a touch so the hand stays in contact with the narrower waist)
    wrist_t=pelvis + side_t*(0.150*sgn) + up_t*0.175 + front_t*(0.00)
    # elbow flared OUT + slightly BACK + down (confident akimbo flare, raised to match)
    elbow_t=sh + side_t*(0.24*sgn) - up_t*0.27 - front_t*0.12
    set_seg('upper_arm'+s, elbow_t-sh)
    # forearm roll reference = lateral knuckle axis (well-conditioned vs the ~vertical
    # bone length) -> NO wrist candy-wrapper twist. shared forearm -> twist.
    kxf=side_t*sgn
    set_frame_x('forearm'+s, wrist_t-bpos('forearm'+s), kxf)
    ft_dir=(wrist_t-bpos('forearm_twist'+s)).normalized()
    set_frame_x('forearm_twist'+s, ft_dir, kxf)
    # HAND: length axis (fingers) points ANTERIOR (-Y front) + slight down + slight
    # inward, so the four fingers drape/curl down over the FRONT of the hip. The
    # hand's local +Z is forced to the BACK-OF-HAND normal (UP + slightly out) so the
    # PALM (local -Z) faces DOWN + IN, resting on top of the iliac crest -- back-of-
    # hand up, palm-on-hip (roll UNCHANGED). xdir = y x z_back reproduces that +Z
    # under set_frame_x (z = x x y).
    y_fing=(front_t*1.0 + (-up_t)*0.18 + inw*0.10).normalized()
    # local +Z = back of hand. Rolled ~13deg further OUT about the finger/wrist axis
    # (out 0.35 -> 0.58) so the back-of-hand faces more up-and-OUTWARD and the PALM
    # (local -Z) cups the SIDE of the waist -- faces more medial/inward toward the
    # torso (not straight-down). kxh (knuckle axis) stays the roll ref -> no twist.
    back_norm=(up_t*0.80 + out*0.58).normalized()
    kxh=y_fing.cross(back_norm)
    set_frame_x('hand'+s, y_fing, kxh)
    pz=(rig.pose.bones['hand'+s].matrix.to_3x3()@Vector((0,0,1))).normalized()  # +Z=back
    # fingers: relaxed natural curl toward the palm side (down/in) -> drape down over
    # the FRONT of the hip. -pz is the palm side, so positive FCURL curls that way.
    csgn=_curl_sign('fingers_01'+s, pz)
    curl_localx('fingers_01'+s, FCURL[0]*csgn)
    curl_localx('fingers_02'+s, FCURL[1]*csgn)
    curl_localx('fingers_03'+s, FCURL[2]*csgn)
    # thumb: hooks POSTERIORLY (toward the BACK / glute / spine), tip curled toward
    # the body.
    set_seg('thumb_01'+s, (back_t*1.0 + (-up_t)*0.12 + out*0.12).normalized())
    set_seg('thumb_02'+s, (back_t*0.90 + (-up_t)*0.35 + inw*0.05).normalized())
    # X-mirror the LEFT arm chain onto the RIGHT (quat (w,x,y,z)->(w,x,-y,-z))
    ARMB=('upper_arm','forearm','forearm_twist','hand',
          'fingers_01','fingers_02','fingers_03','thumb_01','thumb_02')
    for b in ARMB:
        q=rig.pose.bones[b+'.L'].rotation_quaternion
        rig.pose.bones[b+'.R'].rotation_quaternion=(q.w,q.x,-q.y,-q.z)
    bpy.context.view_layer.update()

def smooth(a,b,f):
    if f<=a: return 0.0
    if f>=b: return 1.0
    x=(f-a)/(b-a); return x*x*(3-2*x)

# timeline 30fps
F_DN0,F_DN1=12,72; F_HOLD=84; F_UP1=144; FEND=156
DZ_TOP=-0.16; DZ_BOT=-0.42
STEP=0.42
def lunge_t(f):
    if f<=F_DN1: return smooth(F_DN0,F_DN1,f)
    if f<=F_HOLD: return 1.0
    return 1.0-smooth(F_HOLD,F_UP1,f)

prefs=bpy.context.preferences.edit
prefs.keyframe_new_interpolation_type='BEZIER'
try: prefs.keyframe_new_handle_type='AUTO_CLAMPED'
except Exception as e: print("handle warn",e)

capture_bind()
FRONT='.L'; REAR='.R'
frontA0=_ANKB[FRONT].copy(); rearA0=_ANKB[REAR].copy()
# foot ground contact -- raised so soles sit ON the floor (a few mm above plane)
GROUND_Z=-1.001
FOOT_LIFT=0.006
front_ank=Vector((frontA0.x, frontA0.y-STEP, frontA0.z+FOOT_LIFT))            # flat, forward
rear_ank =Vector((rearA0.x,  rearA0.y+STEP+0.03, -0.80+FOOT_LIFT))            # raised (heel up)
rear_ball=Vector((rearA0.x,  rearA0.y+STEP+0.03-0.10, -0.955+FOOT_LIFT))      # ball on floor

# foot-vertex sets (for penetration measurement), classified by x sign
FRONT_VI=[i for i,v in enumerate(mesh.data.vertices) if v.co.x>0.03]
REAR_VI =[i for i,v in enumerate(mesh.data.vertices) if v.co.x<-0.03]
dg=bpy.context.evaluated_depsgraph_get()
def foot_minz(vis):
    me=mesh.evaluated_get(dg); mw=mesh.matrix_world
    return min((mw@me.data.vertices[i].co).z for i in vis)

for f in range(0,FEND+1):
    bpy.context.scene.frame_set(f)
    reset_bind()
    st=lunge_t(f)
    dz=DZ_TOP+(DZ_BOT-DZ_TOP)*st
    hips_move(0.0,dz)
    torso(st); gaze(st)
    # FRONT leg: flat foot, knee tracks forward over toe
    solve_leg(FRONT, front_ank, (0,0,dz), (0.06,-1,0.02))
    flat_foot(FRONT,1.0)
    # REAR leg: ball-down, knee drops forward-down
    solve_leg(REAR, rear_ank, (0,0,dz), (-0.04,-0.7,-0.5))
    aim_foot(REAR, rear_ball)
    aim_toe(REAR, Vector((rear_ball.x, rear_ball.y-0.06, -0.955+FOOT_LIFT-0.015)))
    arms_akimbo()
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion',frame=f)
    rig.pose.bones['hips'].keyframe_insert('location',frame=f)
    if f in (0,42,78,156):
        bpy.context.view_layer.update()
        fz=foot_minz(FRONT_VI); rz=foot_minz(REAR_VI)
        print("F%03d st=%.2f | FRONT sole minZ=%.4f %s | REAR sole minZ=%.4f %s | ground=%.3f"%(
              f,st,fz,"CLIP" if fz<GROUND_Z else "ok",
              rz,"CLIP" if rz<GROUND_Z else "ok",GROUND_Z))

sc=bpy.context.scene
sc.frame_start=0; sc.frame_end=FEND; sc.render.fps=30

# DARK studio (same look as the squat template)
bpy.ops.mesh.primitive_plane_add(size=14.0, location=(0,0,GROUND_Z))
plane=bpy.context.active_object; plane.name="Ground"
gm=bpy.data.materials.new("GroundMat"); gm.use_nodes=True
bsdf=gm.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value=(0.030,0.030,0.038,1.0)
bsdf.inputs["Roughness"].default_value=0.7
plane.data.materials.append(gm)
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

bpy.ops.wm.save_as_mainfile(filepath=OUT+"/lunge.blend")
print("SAVED lunge.blend  L1=%.3f L2=%.3f"%(L1,L2))
