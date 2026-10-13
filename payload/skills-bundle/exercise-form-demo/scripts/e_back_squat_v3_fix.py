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
# Build the BARBELL BACK SQUAT (high-bar) demo on the v3 rig -- GRIP FIX pass.
#
# Same as e_back_squat_v3.py except the HAND/ARM ORIENTATION is corrected:
#  * solve_arm elbow pole vector is exposed via env (POLEX/POLEY/POLEZ). The v3
#    default pulled the elbow FORWARD (-Y), which reads as a reversed grip on a
#    back squat. A high-bar back squat wants the elbow DOWN + slightly BACK
#    (+Y) / tucked under the bar, so the default here flips Y to +Y.
#  * GRIP_ROLL (env ROLL) re-tuned so the closed fist wraps the bar from BEHIND
#    (fingers over the top, thumb over, back of hand up/out) instead of palm-out.
# The MESH (v3 rig + hand_regrip_v3 grip) is unchanged -- only orientation.
#
# Writes to the PREVIEW dir; does NOT touch library/. Env BUILD_ONLY=1 -> build +
# print balance/occlusion/foot numbers, skip save.
import bpy, sys, math, os
from mathutils import Vector, Matrix

SKILL = _SKILL_ROOT
WORK = _os.path.join(_WORK_ROOT, "back_squat_v3_fix")
sys.path.append(SKILL + "/scripts")
from prop_barbell import make_barbell
import hand_regrip_v3 as HR

# ---------------------------------------------------------------- load v3 rig ---
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=SKILL + "/assets/rig/bodybuilder_rigged_v3_lowpoly.glb")
# drop the junk icosphere the glb ships with; keep the body mesh + rig
mesh = max([o for o in bpy.data.objects if o.type == 'MESH'], key=lambda o: len(o.data.vertices))
mesh.name = "Body_low"
for o in list(bpy.data.objects):
    if o.type == 'MESH' and o is not mesh:
        bpy.data.objects.remove(o, do_unlink=True)
rig = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
rig.name = "Rig"
sc = bpy.context.scene
for pb in rig.pose.bones:
    pb.rotation_mode = 'QUATERNION'

# ------------------------------------------------------- s1 leg-IK machinery ---
def reset_bind():
    for pb in rig.pose.bones:
        pb.rotation_quaternion = (1, 0, 0, 0); pb.location = (0, 0, 0); pb.scale = (1, 1, 1)
    bpy.context.view_layer.update()

def wrot(name, axis, deg):
    pb = rig.pose.bones[name]; M = pb.matrix.copy(); h = M.translation.copy()
    Rm = Matrix.Rotation(math.radians(deg), 4, axis); T = Matrix.Translation(h)
    pb.matrix = T @ Rm @ T.inverted() @ M
    bpy.context.view_layer.update()

def hips_move(dy, dz):
    pb = rig.pose.bones['hips']; M = pb.matrix.copy()
    M.translation.y += dy; M.translation.z += dz; pb.matrix = M
    bpy.context.view_layer.update()

def aim_world(name, d):
    pb = rig.pose.bones[name]; head = pb.matrix.translation.copy()
    q = Vector(d).normalized().to_track_quat('Y', 'Z')
    pb.matrix = Matrix.Translation(head) @ q.to_matrix().to_4x4()
    bpy.context.view_layer.update()

def bpos(name, tail=False):
    pb = rig.pose.bones[name]
    return (pb.matrix @ Vector((0, pb.length, 0))) if tail else pb.matrix.translation.copy()

def bhead(name):
    return rig.pose.bones[name].matrix.translation.copy()

L1 = rig.pose.bones['thigh.L'].length
L2 = rig.pose.bones['shin.L'].length
KNEE_BIAS = 0.28
TOE_OUT = math.radians(12.0)
_HIPB = {}; _ANKB = {}; _FOOTB = {}

def capture_bind():
    reset_bind()
    for s in ('.L', '.R'):
        _HIPB[s] = rig.pose.bones['thigh' + s].matrix.translation.copy()
        _ANKB[s] = rig.pose.bones['foot' + s].matrix.translation.copy()
        _FOOTB[s] = rig.pose.bones['foot' + s].matrix.to_3x3().copy()

def set_seg(name, target):
    pb = rig.pose.bones[name]; m = pb.matrix; head = m.translation.copy(); cur = m.to_3x3()
    cdir = (cur @ Vector((0, 1, 0))).normalized()
    q = cdir.rotation_difference(Vector(target).normalized())
    pb.matrix = Matrix.Translation(head) @ (q.to_matrix() @ cur).to_4x4()
    bpy.context.view_layer.update()

def set_foot(side, sc_sign):
    pb = rig.pose.bones['foot' + side]; head = pb.matrix.translation.copy()
    rot = Matrix.Rotation(sc_sign * TOE_OUT, 4, 'Z').to_3x3() @ _FOOTB[side]
    pb.matrix = Matrix.Translation(head) @ rot.to_4x4()
    bpy.context.view_layer.update()

def solve_leg(side, sc_sign, dy, dz):
    Phip = _HIPB[side] + Vector((0, dy, dz))
    A = _ANKB[side]
    base = A - Phip; d = base.length; d = min(d, L1 + L2 - 1e-4)
    n = base.normalized()
    ca = max(-1.0, min(1.0, (L1 * L1 + d * d - L2 * L2) / (2 * L1 * d))); a1 = math.acos(ca)
    proj = L1 * math.cos(a1); h = L1 * math.sin(a1)
    f = Vector((sc_sign * KNEE_BIAS, -1, 0))
    perp = f - (f.dot(n)) * n
    if perp.length < 1e-5:
        perp = Vector((0, 0, -1)); perp = perp - (perp.dot(n)) * n
    perp.normalize()
    K = Phip + proj * n + h * perp
    set_seg("thigh" + side, K - Phip)
    set_seg("shin" + side, A - K)
    set_foot(side, sc_sign)

# --- HIGH-BAR tuning: hips drop mostly straight down; a touch of torso lean so the
#     trap-mounted bar tracks over the midfoot. ---
LEAN_SCALE = float(os.environ.get("LEAN", "1.40"))
SPINE_LEAN = (10.0 * LEAN_SCALE, 15.0 * LEAN_SCALE, 15.0 * LEAN_SCALE)
def torso(t):
    if t <= 0: return
    wrot("spine", 'X', SPINE_LEAN[0] * t)
    wrot("spine.001", 'X', SPINE_LEAN[1] * t)
    wrot("spine.002", 'X', SPINE_LEAN[2] * t)

GAZE = float(os.environ.get("GAZ", "-28.0"))   # head counter-rotates UP to clear bar + neutral gaze
def gaze(t):
    if t <= 0: return
    wrot("neck", 'X', GAZE * t); wrot("head", 'X', GAZE * t)

def smooth(a, b, f):
    if f <= a: return 0.0
    if f >= b: return 1.0
    x = (f - a) / (b - a); return x * x * (3 - 2 * x)

# ============================================================ v3 GRIP (rigid) ===
# high-bar shelf, raised: bar CENTER behind the neck (occluded from front camera).
BAR_Y, BAR_Z = 0.222, 0.566       # raised ~4.5cm from v2 (0.520) -> high-bar shelf below C7
GRIP_X = 0.315                     # grip just outside the shoulders
GRIP_ROLL = float(os.environ.get("ROLL", "11.0"))   # palm roll about bar axis: re-tuned
# from 18 -> 11 so the fingers drape cleanly OVER the top of the bar (wrap from
# behind) with the thumb over the top; 18 sat the fist low, >=35 rolled the palm out.
# grip was tuned zero-mesh-through-bar for a 16.6mm shaft -> use that radius so the
# closed fist seats ON the shaft surface (a thinner shaft lets the fingertips overshoot).
SHAFT_R = 0.0166

# elbow pole for solve_arm: v3 default was (sc*0.28, -0.30, -1.0) = down + FWD + out,
# which reads as a reversed back-squat grip. Flip Y to +Y so the elbow sits down +
# BACK / tucked under the bar. Exposed via env for tuning.
POLE_X = float(os.environ.get("POLEX", "0.28"))
POLE_Y = float(os.environ.get("POLEY", "0.22"))     # +Y = BACK (v3 had -0.30 = fwd)
POLE_Z = float(os.environ.get("POLEZ", "-1.0"))

ARM_BONES = []
for s in ('.L', '.R'):
    ARM_BONES += ["upper_arm" + s, "forearm" + s, "forearm_twist" + s, "hand" + s]
FING_BONES = []
for s in ('.L', '.R'):
    FING_BONES += ["fingers_01" + s, "fingers_02" + s, "fingers_03" + s,
                   "thumb_01" + s, "thumb_02" + s]

def capture_ref_grip_quats():
    """Apply HR canonical closed-grip curl to the LEFT fingers/thumb in bind pose,
    capture the LOCAL (parent-relative) quats. Mirror them for the right side."""
    reset_bind()
    f1, f2, f3 = HR.GRIP_FINGERS
    HR.wrot(rig, "fingers_01.L", 'Y', f1)
    HR.wrot(rig, "fingers_02.L", 'Y', f2)
    HR.wrot(rig, "fingers_03.L", 'Y', f3)
    t1x, t1z, t2x, t2z = HR.GRIP_THUMB
    HR.wrot(rig, "thumb_01.L", 'X', t1x); HR.wrot(rig, "thumb_01.L", 'Z', t1z)
    HR.wrot(rig, "thumb_02.L", 'X', t2x); HR.wrot(rig, "thumb_02.L", 'Z', t2z)
    bpy.context.view_layer.update()
    qL = {}
    for b in ["fingers_01.L", "fingers_02.L", "fingers_03.L", "thumb_01.L", "thumb_02.L"]:
        qL[b] = rig.pose.bones[b].rotation_quaternion.copy()
    # mirror across YZ plane (x->-x): q=(w,x,y,z) -> (w,x,-y,-z)
    q = dict(qL)
    for b, v in qL.items():
        rb = b[:-2] + ".R"
        q[rb] = (v.w, v.x, -v.y, -v.z)
    reset_bind()
    return q

FING_LOCAL = capture_ref_grip_quats()

# reference (bind) geometry of the LEFT hand + the bar it wraps
capture_bind()   # leaves rig in bind
R0_L = rig.pose.bones["hand.L"].matrix.to_3x3().copy()
HAND_HEAD_REF_L = rig.pose.bones["hand.L"].matrix.translation.copy()
# HR.GRIP_BAR = (x, z, r); the tuned test bar sits at y=0 (see render_check)
PBAR_REF_L = Vector((HR.GRIP_BAR[0], 0.0, HR.GRIP_BAR[1]))
LOCAL_OFF_L = R0_L.transposed() @ (PBAR_REF_L - HAND_HEAD_REF_L)   # bar offset in hand-local

Rz = Matrix.Rotation(math.radians(-90.0), 3, 'Z')   # maps local-Y-axis(bar) -> world X
S = Matrix.Diagonal(Vector((-1.0, 1.0, 1.0)))       # YZ-plane mirror

def grip_targets(side):
    """Return (hand_world_rot 3x3, hand_head_world) that rigidly place the tuned
    wrapped hand so its bar coincides with the real barbell grip point on `side`."""
    Rt_L = Matrix.Rotation(math.radians(GRIP_ROLL), 3, 'X') @ Rz
    if side == ".L":
        Rt = Rt_L; R0 = R0_L; loff = LOCAL_OFF_L; Gt = Vector((GRIP_X, BAR_Y, BAR_Z))
    else:
        Rt = S @ Rt_L @ S; R0 = S @ R0_L @ S; loff = S @ LOCAL_OFF_L
        Gt = Vector((-GRIP_X, BAR_Y, BAR_Z))
    Rhand = Rt @ R0
    hand_head = Gt - Rhand @ loff
    return Rhand, hand_head

# 2-link arm IK: place the wrist (hand head) at `wrist`, elbow pole down+back+out.
def solve_arm(side, sc_sign, wrist):
    P0 = bhead("upper_arm" + side)
    base = wrist - P0; d = base.length
    l1 = rig.pose.bones['upper_arm' + side].length
    l2 = rig.pose.bones['forearm' + side].length
    d = min(d, l1 + l2 - 1e-4); n = base.normalized()
    ca = max(-1.0, min(1.0, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d))); a1 = math.acos(ca)
    proj = l1 * math.cos(a1); h = l1 * math.sin(a1)
    f = Vector((sc_sign * POLE_X, POLE_Y, POLE_Z))   # elbow down + BACK + out
    perp = f - (f.dot(n)) * n
    if perp.length < 1e-5:
        perp = Vector((0, 0, -1)); perp = perp - (perp.dot(n)) * n
    perp.normalize()
    K = P0 + proj * n + h * perp
    set_seg("upper_arm" + side, K - P0)
    set_seg("forearm" + side, wrist - K)
    aim_world("forearm_twist" + side, wrist - K)

def pose_grip_once():
    """Solve both arms + override both hands to the rigid wrapped grip, apply the
    finger curls, and capture ALL arm+finger LOCAL quats for constant re-use."""
    reset_bind()
    for side, sign in ((".L", 1.0), (".R", -1.0)):
        Rhand, hand_head = grip_targets(side)
        solve_arm(side, sign, hand_head)
        pb = rig.pose.bones["hand" + side]
        pb.matrix = Matrix.Translation(hand_head) @ Rhand.to_4x4()
        bpy.context.view_layer.update()
    for b, q in FING_LOCAL.items():
        rig.pose.bones[b].rotation_quaternion = q
    bpy.context.view_layer.update()
    grip = {b: rig.pose.bones[b].rotation_quaternion.copy() for b in ARM_BONES}
    grip.update({b: rig.pose.bones[b].rotation_quaternion.copy() for b in FING_BONES})
    return grip

GRIP_LOCAL = pose_grip_once()
for s in ('.L', '.R'):
    w = bhead("hand" + s)
    print("GRIP%s wrist=(%.3f,%.3f,%.3f)" % (s, w.x, w.y, w.z))

# ---------------------------------------------------------------- timeline -----
F_DN0, F_DN1 = 12, 72
F_HOLD = 84
F_UP1 = 144
FEND = 156
DZ = float(os.environ.get("DZ", "-0.51"))
DY = float(os.environ.get("DY", "0.07"))

def squat_t(f):
    if f <= F_DN1: return smooth(F_DN0, F_DN1, f)
    if f <= F_HOLD: return 1.0
    return 1.0 - smooth(F_HOLD, F_UP1, f)

prefs = bpy.context.preferences.edit
prefs.keyframe_new_interpolation_type = 'BEZIER'
try: prefs.keyframe_new_handle_type = 'AUTO_CLAMPED'
except Exception as e: print("handle warn", e)

capture_bind()
for f in range(0, FEND + 1):
    sc.frame_set(f)
    reset_bind()
    st = squat_t(f)
    dy = DY * st; dz = DZ * st
    hips_move(dy, dz)
    torso(st); gaze(st)
    solve_leg(".L", 1.0, dy, dz); solve_leg(".R", -1.0, dy, dz)
    for b in ARM_BONES + FING_BONES:            # constant torso-local grip every frame
        rig.pose.bones[b].rotation_quaternion = GRIP_LOCAL[b]
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion', frame=f)
    rig.pose.bones['hips'].keyframe_insert('location', frame=f)

sc.frame_start = 0; sc.frame_end = FEND; sc.render.fps = 30

# ------------------------------------------------------- barbell prop + parent -
bar = make_barbell(plates_per_side=2, shaft_radius=SHAFT_R)
sc.frame_set(0); bpy.context.view_layer.update()
pb = rig.pose.bones["spine.002"]
bone_tail_m = rig.matrix_world @ pb.matrix @ Matrix.Translation((0, pb.length, 0))
bar.parent = rig
bar.parent_type = 'BONE'
bar.parent_bone = "spine.002"
bar.matrix_parent_inverse = bone_tail_m.inverted()
bar.matrix_basis = Matrix.Translation((0.0, BAR_Y, BAR_Z))
bpy.context.view_layer.update()

# =============================================== DARK studio (from s1_squat) ====
def build_studio():
    # measure planted-sole min z across the whole clip, drop ground just below it
    dg = bpy.context.evaluated_depsgraph_get()
    sole_min = 1e9
    for f in (0, 40, 78, 156):
        sc.frame_set(f); bpy.context.view_layer.update()
        ev = mesh.evaluated_get(dg); me = ev.to_mesh(); mw = mesh.matrix_world
        zmin = min((mw @ v.co).z for v in me.vertices)
        sole_min = min(sole_min, zmin); ev.to_mesh_clear()
    EPS = 0.004
    ground_z = sole_min - EPS
    print("SOLE_MIN over clip=%.5f  GROUND_Z=%.5f  gap=%.4f" % (sole_min, ground_z, EPS))
    bpy.ops.mesh.primitive_plane_add(size=14.0, location=(0, 0, ground_z))
    plane = bpy.context.active_object; plane.name = "Ground"
    gm = bpy.data.materials.new("GroundMat"); gm.use_nodes = True
    bsdf = gm.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (0.030, 0.030, 0.038, 1.0)
    bsdf.inputs["Roughness"].default_value = 0.7
    plane.data.materials.append(gm)
    if sc.world is None: sc.world = bpy.data.worlds.new('W')
    sc.world.use_nodes = True
    bg = sc.world.node_tree.nodes.get('Background')
    bg.inputs[0].default_value = (0.012, 0.012, 0.018, 1.0); bg.inputs[1].default_value = 1.0
    try:
        sc.view_settings.view_transform = 'Standard'; sc.view_settings.look = 'None'
    except Exception as e: print("vt warn", e)
    LIGHTS = (((66, 0, 10), 2.8, 6.0), ((72, 0, 0), 1.1, 16.0),
              ((46, 0, -34), 0.7, 14.0), ((115, 0, 190), 3.6, 4.0))
    for ang, en, sa in LIGHTS:
        lt = bpy.data.lights.new("sun", 'SUN'); lt.energy = en
        try: lt.angle = math.radians(sa)
        except Exception: pass
        lo = bpy.data.objects.new("sun", lt); bpy.context.collection.objects.link(lo)
        lo.rotation_euler = (math.radians(ang[0]), math.radians(ang[1]), math.radians(ang[2]))
    return ground_z

GROUND_Z = build_studio()

# ------------------------------------------------- balance + occlusion report --
def bar_center(fr):
    sc.frame_set(fr); bpy.context.view_layer.update()
    return bar.matrix_world.translation.copy()

c0 = bar_center(0); cb = bar_center(78)
sc.frame_set(78); bpy.context.view_layer.update()
ank = bhead("foot.L"); toe = bpos("toe.L", True)
heel_y = ank.y; toe_y = toe.y; mid_y = 0.5 * (heel_y + toe_y)
hip_bot = bhead("hips")
print("BAR_TOP  center=(%.3f,%.3f,%.3f)" % (c0.x, c0.y, c0.z))
print("BAR_BOT  center=(%.3f,%.3f,%.3f)" % (cb.x, cb.y, cb.z))
print("MIDFOOT_Y=%.3f heelY=%.3f toeY=%.3f  barBOT_y=%.3f  d(bar-mid)=%+.3f (>0=behind mid)"
      % (mid_y, heel_y, toe_y, cb.y, cb.y - mid_y))
print("  bar vs heel: %+.3f (>0 = behind heel = BAD)" % (cb.y - heel_y))
print("BAR_VERT_TRAVEL dz=%.3f  horiz_drift_y=%.3f" % (cb.z - c0.z, cb.y - c0.y))
# occlusion: mesh back-surface y at bar height, top + bottom frames
def mesh_back_y(fr, zc):
    sc.frame_set(fr); bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get(); ev = mesh.evaluated_get(dg)
    me = ev.to_mesh(); mw = mesh.matrix_world
    ys = [(mw @ v.co).y for v in me.vertices
          if abs((mw @ v.co).z - zc) < 0.03 and abs((mw @ v.co).x) < 0.12]
    r = max(ys) if ys else None; ev.to_mesh_clear(); return r
mb0 = mesh_back_y(0, c0.z); mbb = mesh_back_y(78, cb.z)
# bar central span sits BEHIND the body back surface (front camera at -Y) => the body
# occludes it. gap = bar_front_edge - mesh_back : >=0 occluded (no skewer poking front),
# and small (<~0.03) = resting near the skin, not floating far behind.
print("OCC top: bar_front_edge_y=%.3f  mesh_back_y=%.3f  gap=%+.3f (>=0 occluded)"
      % (c0.y - SHAFT_R, mb0, (c0.y - SHAFT_R) - mb0))
print("OCC bot: bar_front_edge_y=%.3f  mesh_back_y=%.3f  gap=%+.3f (>=0 occluded)"
      % (cb.y - SHAFT_R, mbb, (cb.y - SHAFT_R) - mbb))
# depth + head-vs-bar clearance at the bottom
sc.frame_set(78); bpy.context.view_layer.update()
knee_bot = bhead("shin.L")
print("DEPTH hip-knee=%+.3f (0=parallel,<0 below)" % (hip_bot.z - knee_bot.z))
head_z = bhead("head").z
dg = bpy.context.evaluated_depsgraph_get(); ev = mesh.evaluated_get(dg)
me = ev.to_mesh(); mw = mesh.matrix_world
hv = [mw @ v.co for v in me.vertices if (mw @ v.co).z > head_z - 0.02 and abs((mw @ v.co).x) < 0.13]
if hv:
    dmin = min(math.hypot(v.y - cb.y, v.z - cb.z) for v in hv)
    ylo = min(v.y for v in hv)
    print("HEAD-BAR min dist head->bar axis=%.3f (>%.3f shaft = clears)  head_frontY=%.3f barY=%.3f"
          % (dmin, SHAFT_R, ylo, cb.y))
ev.to_mesh_clear()

if os.environ.get("BUILD_ONLY") != "1":
    sc.frame_set(0)
    bpy.ops.wm.save_as_mainfile(filepath=WORK + "/back_squat_v3_fix.blend")
    print("SAVED back_squat_v3_fix.blend")
print("DONE ROLL=%.1f POLE=(%.2f,%.2f,%.2f) BAR=(%.3f,%.3f) GRIP_X=%.3f"
      % (GRIP_ROLL, POLE_X, POLE_Y, POLE_Z, BAR_Y, BAR_Z, GRIP_X))
