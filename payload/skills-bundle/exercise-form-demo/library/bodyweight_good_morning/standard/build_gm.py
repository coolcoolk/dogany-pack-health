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
# Bodyweight good morning (standing hip hinge) on the v3 rigged bodybuilder
# (3-segment grouped fingers). Feet flat + planted (hip width) every frame; soft
# constant knee bend; hips travel BACK to counterbalance while a RIGID NEUTRAL spine
# hinges forward to ~parallel (a hip hinge, NOT a squat); neutral gaze (head in line
# with spine). ready-stance start == end (loop-friendly).
#
# v3 changes vs the crushed v2 cut:
#  (a) ARM POSE posed on the LEFT arm/hand only, then X-mirrored to the RIGHT (rig is
#      X-symmetric) so both hands are artifact-free; full-res symmetric mesh used so
#      the grouped-finger deform stays seam-free. Two selectable poses:
#        - "behind_head": laced hands cupping the base of the skull, elbows flared, estate-scrub:allow(anatomical skull)
#          gentle 3-segment finger curl (v3 rig) -- no crush blob.
#        - "akimbo": hands-on-hips, natural orientation (back-of-hand UP, palm
#          down+in on the crest, four fingers draping FORWARD over the front of the
#          hip, thumb hooking BACK) -- fallback if behind-head still crushes.
#  (b) FOOT FIX: sole min-z measured across all frames; ground plane placed 4mm below
#      the lowest sole so soles sit ~4mm ON the floor -- no z-fight clip, flat/planted.
import bpy, sys, os, math
from mathutils import Vector, Matrix

ARM_POSE=os.environ.get("GM_ARM","behind_head")   # "behind_head" | "akimbo"

GLB=_os.path.join(_SKILL_ROOT, "assets/rig/bodybuilder_rigged_v3.glb")
WORK=_os.path.join(_WORK_ROOT, "blender_work")
OUT=WORK+"/ex_build"

bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB)
mesh=max([o for o in bpy.data.objects if o.type=='MESH'],key=lambda o:len(o.data.vertices))
for o in list(bpy.data.objects):
    if o.type=='MESH' and o is not mesh:
        bpy.data.objects.remove(o,do_unlink=True)
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
    # +1/-1 so a positive curl flexes the fingertip toward the palm side
    pb=rig.pose.bones[name]
    tip0=(pb.matrix@Vector((0,pb.length,0)))
    axis=(pb.matrix.to_3x3()@Vector((1,0,0))).normalized()
    wrot_axis(name,axis,10.0)
    tip1=(pb.matrix@Vector((0,pb.length,0)))
    wrot_axis(name,axis,-10.0)
    moved=(tip1-tip0).dot(-Vector(palm_normal).normalized())
    return 1.0 if moved>0 else -1.0

def set_frame_x(name,ydir,xdir):
    # world orientation: local Y along ydir, local X toward xdir (knuckle/roll axis --
    # ~horizontal, well-conditioned vs the ~vertical bone length -> no candy-wrapper).
    pb=rig.pose.bones[name]; head=pb.matrix.translation.copy()
    y=Vector(ydir).normalized()
    x=Vector(xdir); x=(x-x.dot(y)*y).normalized()
    z=x.cross(y).normalized(); x=y.cross(z).normalized()
    M3=Matrix((x,y,z)).transposed()
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
    # analytic 2-link IK: hip driven, ankle pinned, knee via pole.
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

def flat_foot(side):
    # re-align foot to bind (flat) + toe-out ~10deg, so soles stay parallel to floor.
    pb=rig.pose.bones['foot'+side]; head=pb.matrix.translation.copy()
    rot=Matrix.Rotation(math.radians(10.0)*(1 if side=='.L' else -1),4,'Z').to_3x3()@_FOOTB[side]
    pb.matrix=Matrix.Translation(head)@rot.to_4x4(); bpy.context.view_layer.update()

def hinge(t):
    # rigid straight-back hip hinge: lean ONLY 'spine' -> whole torso chain tips as one
    # neutral unit. small neck+head counter keeps gaze in line with the spine (no chin
    # tuck, no over-lift): head stays roughly in line with the torso.
    if t<=0: return
    wrot("spine",'X',80*t)
    wrot("neck",'X',-10*t); wrot("head",'X',-10*t)

# ---------- ARM POSE A: laced hands behind the head (v3 3-segment curl) ----------
FCURL_BH=(24.0,30.0,26.0)     # per-segment MCP/PIP/DIP flex -> fingers curl to cup
THB_BH=(-18.0,-10.0)          # thumb adduct/tuck along the skull estate-scrub:allow(anatomical skull)
def arms_behind_head():
    up_t=(bpos('head',True)-bpos('head')).normalized()          # crown direction
    side_t=(bpos('shoulder.L')-bpos('shoulder.R')).normalized() # +X = left
    front_t=side_t.cross(up_t)
    if front_t.y>0: front_t=-front_t                             # -Y front
    back_t=-front_t
    skull_c=bpos('head')+up_t*0.085                             # skull center approx estate-scrub:allow(anatomical skull)
    R=0.105
    s='.L'; sgn=1.0
    sh=bpos('upper_arm'+s)
    # wrist behind + lateral of the skull, at surface + small gap estate-scrub:allow(anatomical skull)
    wrist_t=skull_c + back_t*(R*0.55) + side_t*(0.085*sgn) + up_t*(-0.015)
    # elbow flared WIDE: out + up + a touch forward
    elbow_t=sh + side_t*(0.32*sgn) + up_t*0.14 + front_t*0.12
    set_seg('upper_arm'+s, elbow_t-sh)
    kx=side_t*sgn                                               # knuckle/roll axis
    set_frame_x('forearm'+s, wrist_t-bpos('forearm'+s), kx)
    ft_dir=(wrist_t-bpos('forearm_twist'+s)).normalized()
    set_frame_x('forearm_twist'+s, ft_dir, kx)
    # HAND length axis points up + inward (toward crown/center) so the palm cups the
    # back of the skull; slight back so fingers wrap onto the occiput, not the crown. estate-scrub:allow(anatomical skull)
    hy=(up_t*0.66 + (-side_t*sgn)*0.50 + back_t*0.10).normalized()
    set_frame_x('hand'+s, hy, kx)
    pz=(rig.pose.bones['hand'+s].matrix.to_3x3()@Vector((0,0,1))).normalized()
    csgn=_curl_sign('fingers_01'+s, pz)
    curl_localx('fingers_01'+s, FCURL_BH[0]*csgn)
    curl_localx('fingers_02'+s, FCURL_BH[1]*csgn)
    curl_localx('fingers_03'+s, FCURL_BH[2]*csgn)
    wrot('thumb_01'+s,'Z',THB_BH[0]); wrot('thumb_02'+s,'Z',THB_BH[1])
    _mirror_arm_LtoR()

# ---------- ARM POSE B: akimbo hands on hips (natural orientation) ----------
# back-of-hand UP/out, palm DOWN + IN on top of the iliac crest (palm-on-hip); four
# fingers drape FORWARD over the front of the hip; thumb hooks BACK (posterior)
# toward the glute/spine; elbows flared out + slightly back. LEFT posed, X-mirrored.
FCURL_AK=(14.0,18.0,14.0)
def arms_akimbo():
    pelvis=bpos('hips')
    up_t=(bpos('neck')-bpos('spine.001')).normalized()
    side_t=(bpos('shoulder.L')-bpos('shoulder.R')).normalized()   # +X toward LEFT
    front_t=side_t.cross(up_t)
    if front_t.y>0: front_t=-front_t          # -Y anterior
    back_t=-front_t                            # +Y posterior
    s='.L'; sgn=1.0
    out=side_t*sgn; inw=-out
    sh=bpos('upper_arm'+s)
    # wrist seated HIGH at the iliac crest / waist notch, just ABOVE the waistband
    # (raised ~6cm vs the old low-on-shorts spot; lateral pulled in a touch so the
    # hand stays in contact with the narrower waist)
    wrist_t=pelvis + side_t*(0.150*sgn) + up_t*0.175 + front_t*(0.00)
    elbow_t=sh + side_t*(0.24*sgn) - up_t*0.27 - front_t*0.12
    set_seg('upper_arm'+s, elbow_t-sh)
    kxf=side_t*sgn
    set_frame_x('forearm'+s, wrist_t-bpos('forearm'+s), kxf)
    ft_dir=(wrist_t-bpos('forearm_twist'+s)).normalized()
    set_frame_x('forearm_twist'+s, ft_dir, kxf)
    # fingers point ANTERIOR (-Y front) + slight down + inward; back-of-hand (local
    # +Z) forced UP/out so palm (local -Z) faces DOWN + IN on top of the crest. The
    # four fingers drape/curl down over the FRONT of the hip.
    y_fing=(front_t*1.0 + (-up_t)*0.18 + inw*0.10).normalized()
    # back-of-hand rolled ~13deg further OUT (out 0.35 -> 0.58) so the palm cups the
    # SIDE of the waist (faces more medial/inward), back-of-hand more up-and-OUT.
    # kxh (knuckle axis) stays the roll ref -> no wrist candy-wrapper.
    back_norm=(up_t*0.80 + out*0.58).normalized()
    kxh=y_fing.cross(back_norm)
    set_frame_x('hand'+s, y_fing, kxh)
    pz=(rig.pose.bones['hand'+s].matrix.to_3x3()@Vector((0,0,1))).normalized()
    csgn=_curl_sign('fingers_01'+s, pz)
    curl_localx('fingers_01'+s, FCURL_AK[0]*csgn)
    curl_localx('fingers_02'+s, FCURL_AK[1]*csgn)
    curl_localx('fingers_03'+s, FCURL_AK[2]*csgn)
    # thumb hooks POSTERIORLY (toward the BACK / glute / spine), tip curled to body.
    set_seg('thumb_01'+s, (back_t*1.0 + (-up_t)*0.12 + out*0.12).normalized())
    set_seg('thumb_02'+s, (back_t*0.90 + (-up_t)*0.35 + inw*0.05).normalized())
    _mirror_arm_LtoR()

def _mirror_arm_LtoR():
    ARMB=('upper_arm','forearm','forearm_twist','hand',
          'fingers_01','fingers_02','fingers_03','thumb_01','thumb_02')
    for b in ARMB:
        q=rig.pose.bones[b+'.L'].rotation_quaternion
        rig.pose.bones[b+'.R'].rotation_quaternion=(q.w,q.x,-q.y,-q.z)
    bpy.context.view_layer.update()

arms=arms_behind_head if ARM_POSE=="behind_head" else arms_akimbo

def smooth(a,b,f):
    if f<=a: return 0.0
    if f>=b: return 1.0
    x=(f-a)/(b-a); return x*x*(3-2*x)

# timeline 30fps
F_DN0,F_DN1=12,72; F_HOLD=84; F_UP1=144; FEND=156
DY_BACK=0.24; DZ=-0.10
def gm_t(f):
    if f<=F_DN1: return smooth(F_DN0,F_DN1,f)
    if f<=F_HOLD: return 1.0
    return 1.0-smooth(F_HOLD,F_UP1,f)

prefs=bpy.context.preferences.edit
prefs.keyframe_new_interpolation_type='BEZIER'
try: prefs.keyframe_new_handle_type='AUTO_CLAMPED'
except Exception as e: print("handle warn",e)

capture_bind()
# foot vertices (feet region only) for sole-clip measurement
FOOT_VI=[i for i,v in enumerate(mesh.data.vertices) if v.co.z<-0.70]
dg=bpy.context.evaluated_depsgraph_get()
def foot_minz():
    me=mesh.evaluated_get(dg); mw=mesh.matrix_world
    return min((mw@me.data.vertices[i].co).z for i in FOOT_VI)

sole_min=1e9
for f in range(0,FEND+1):
    bpy.context.scene.frame_set(f)
    reset_bind()
    st=gm_t(f); dy=DY_BACK*st; dz=DZ*st
    hips_move(dy,dz)
    hinge(st)
    solve_leg(".L",_ANKB['.L'],(0,dy,dz),(0.10,-1,0.0)); flat_foot(".L")
    solve_leg(".R",_ANKB['.R'],(0,dy,dz),(-0.10,-1,0.0)); flat_foot(".R")
    arms()
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion',frame=f)
    rig.pose.bones['hips'].keyframe_insert('location',frame=f)
    bpy.context.view_layer.update()
    fz=foot_minz(); sole_min=min(sole_min,fz)
    if f in (0,42,78,156):
        hipp=bpos("hips"); neck=bpos("neck")
        tv=(neck-hipp); torso_from_vert=math.degrees(math.atan2(abs(tv.y),tv.z))
        ankL=bpos("foot.L")
        segs=[(0.14,bpos("hips")),(0.33,(bpos("spine")+bpos("neck"))/2),
              (0.08,bpos("head",True)),(0.10,(bpos("shoulder.L")+bpos("hand.L"))/2),
              (0.20,(bpos("thigh.L")+bpos("shin.L")+bpos("thigh.R")+bpos("shin.R"))/4),
              (0.15,(bpos("shin.L")+bpos("foot.L")+bpos("shin.R")+bpos("foot.R"))/4)]
        comy=sum(w*p.y for w,p in segs)/sum(w for w,_ in segs)
        heelY=0.09; toeY=bpos("toe.L",True).y; midY=0.5*(heelY+toeY)
        print("F%03d st=%.2f torsoLean=%.1fdeg(vert) ankZ=%.3f soleZ=%.4f COMy=%.3f midfootY=%.3f"%(
              f,st,torso_from_vert,ankL.z,fz,comy,midY))

# FOOT FIX: place ground 4mm below the lowest sole -> soles ~4mm ON the floor, no clip
GROUND_Z=sole_min-0.004
print("SOLE_MIN=%.4f GROUND_Z=%.4f (gap=%.1fmm)"%(sole_min,GROUND_Z,(sole_min-GROUND_Z)*1000))

sc=bpy.context.scene
sc.frame_start=0; sc.frame_end=FEND; sc.render.fps=30

bpy.ops.mesh.primitive_plane_add(size=14.0, location=(0,0,GROUND_Z))
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
bpy.ops.wm.save_as_mainfile(filepath=OUT+"/good_morning.blend")
print("SAVED good_morning.blend ARM_POSE=%s"%ARM_POSE)
