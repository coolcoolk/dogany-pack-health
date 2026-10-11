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
# Build the BARBELL BACK SQUAT (high-bar) demo. FIRST equipment-integrated demo.
#
# It re-drives the same feet-planted analytic leg-IK + COM balance machinery as the
# reference bodyweight squat (scripts/s1_squat.py), but tuned for a HIGH-BAR loaded
# squat: the hips drop more vertically (less rearward travel) with a touch more
# torso lean, so the barbell -- which rests on the traps BEHIND the neck -- tracks
# roughly straight up/down OVER THE MIDFOOT instead of drifting behind the heels.
#
# The parametric barbell prop (scripts/prop_barbell.py) rests on the rear-trap shelf
# and is BONE-PARENTED to spine.002 so it rides with the torso through the whole rep.
# The arms are re-gripped into a back-squat hold (hands just outside the shoulders,
# forearms up/back to the bar, hands draped over the top of the bar) and baked as a
# constant torso-local pose so hands+bar stay locked to the torso.
#
# Env BUILD_ONLY=1 -> just build + print the balance/occlusion numbers, skip save.
import bpy, sys, math, os
from mathutils import Vector, Matrix

SKILL = _SKILL_ROOT
WORK = _os.path.join(_WORK_ROOT, "back_squat_work")
sys.path.append(SKILL + "/scripts")
from prop_barbell import make_barbell

bpy.ops.wm.open_mainfile(filepath=SKILL + "/assets/rig/squat.blend")
sc = bpy.context.scene
rig = bpy.data.objects["Rig"]
for pb in rig.pose.bones:
    pb.rotation_mode = 'QUATERNION'

# wipe the reference squat action -> re-drive from scratch on the same rig/scene
if rig.animation_data and rig.animation_data.action:
    rig.animation_data.action = None

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

# --- HIGH-BAR tuning: hips drop mostly straight down (small rearward travel) so the
#     loaded COM / bar stay over the midfoot; a touch more torso lean than the
#     bodyweight rep helps the trap-mounted bar track forward over the foot. ---
SPINE_LEAN = (10.0, 15.0, 15.0)   # spine / spine.001 / spine.002 forward deg at bottom
def torso(t):
    if t <= 0: return
    wrot("spine", 'X', SPINE_LEAN[0] * t)
    wrot("spine.001", 'X', SPINE_LEAN[1] * t)
    wrot("spine.002", 'X', SPINE_LEAN[2] * t)

GAZE = -19.0                      # counter-rotate head UP so the jaw clears the bar
def gaze(t):
    if t <= 0: return
    wrot("neck", 'X', GAZE * t); wrot("head", 'X', GAZE * t)

def smooth(a, b, f):
    if f <= a: return 0.0
    if f >= b: return 1.0
    x = (f - a) / (b - a); return x * x * (3 - 2 * x)

# ------------------------------------------------------------ arm back-squat grip
# bar rests BEHIND the traps: mesh back surface at this height ~ y=0.199, so the bar
# CENTER must sit behind it (body fully in front -> central span occluded on camera).
BAR_Y, BAR_Z = 0.214, 0.520       # just behind the trap shelf, below C7 (high-bar)
GRIP_X = 0.305                     # hands just outside the shoulders
ARM_BONES = []
for s in ('.L', '.R'):
    ARM_BONES += ["upper_arm" + s, "forearm" + s, "forearm_twist" + s, "hand" + s]

def solve_arm(side, sc_sign):
    P0 = bhead("upper_arm" + side)
    G = Vector((sc_sign * GRIP_X, BAR_Y - 0.004, BAR_Z + 0.010))   # wrist on top of bar
    base = G - P0; d = base.length; d = min(d, 0.35 + 0.271 - 1e-4)
    n = base.normalized()
    l1 = rig.pose.bones['upper_arm' + side].length
    l2 = rig.pose.bones['forearm' + side].length
    ca = max(-1.0, min(1.0, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d))); a1 = math.acos(ca)
    proj = l1 * math.cos(a1); h = l1 * math.sin(a1)
    f = Vector((sc_sign * 0.22, -0.45, -1.0))   # elbow down + slightly fwd + out
    perp = f - (f.dot(n)) * n
    if perp.length < 1e-5:
        perp = Vector((0, 0, -1)); perp = perp - (perp.dot(n)) * n
    perp.normalize()
    K = P0 + proj * n + h * perp
    set_seg("upper_arm" + side, K - P0)
    set_seg("forearm" + side, G - K)
    aim_world("hand" + side, (-sc_sign * 0.15, -0.72, -0.68))   # drape over top of bar

# ---------------------------------------------------------------- timeline -----
F_DN0, F_DN1 = 12, 72
F_HOLD = 84
F_UP1 = 144
FEND = 156
DZ, DY = -0.44, -0.03    # high-bar: mostly vertical drop to ~parallel, tiny FWD shift

def squat_t(f):
    if f <= F_DN1: return smooth(F_DN0, F_DN1, f)
    if f <= F_HOLD: return 1.0
    return 1.0 - smooth(F_HOLD, F_UP1, f)

prefs = bpy.context.preferences.edit
prefs.keyframe_new_interpolation_type = 'BEZIER'
try: prefs.keyframe_new_handle_type = 'AUTO_CLAMPED'
except Exception as e: print("handle warn", e)

capture_bind()

# solve the grip ONCE at the standing pose, capture constant torso-local arm quats
sc.frame_set(0); reset_bind()
solve_arm(".L", 1.0); solve_arm(".R", -1.0)
GRIP_LOCAL = {b: rig.pose.bones[b].rotation_quaternion.copy() for b in ARM_BONES}
for s in ('.L', '.R'):
    w = bhead("hand" + s)
    print("GRIP%s wrist=(%.3f,%.3f,%.3f)" % (s, w.x, w.y, w.z))

for f in range(0, FEND + 1):
    sc.frame_set(f)
    reset_bind()
    st = squat_t(f)
    dy = DY * st; dz = DZ * st
    hips_move(dy, dz)
    torso(st); gaze(st)
    solve_leg(".L", 1.0, dy, dz); solve_leg(".R", -1.0, dy, dz)
    for b in ARM_BONES:                       # constant back-squat grip every frame
        rig.pose.bones[b].rotation_quaternion = GRIP_LOCAL[b]
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion', frame=f)
    rig.pose.bones['hips'].keyframe_insert('location', frame=f)

sc.frame_start = 0; sc.frame_end = FEND; sc.render.fps = 30

# ------------------------------------------------------- barbell prop + parent -
bar = make_barbell(plates_per_side=2)
sc.frame_set(0); bpy.context.view_layer.update()
pb = rig.pose.bones["spine.002"]
bone_tail_m = rig.matrix_world @ pb.matrix @ Matrix.Translation((0, pb.length, 0))
bar.parent = rig
bar.parent_type = 'BONE'
bar.parent_bone = "spine.002"
bar.matrix_parent_inverse = bone_tail_m.inverted()
bar.matrix_basis = Matrix.Translation((0.0, BAR_Y, BAR_Z))
bpy.context.view_layer.update()

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
# occlusion sanity: mesh back surface at bar height (frame0), bar front edge behind it
print("OCC top: bar_front_edge_y=%.3f (needs > mesh_back ~0.199)" % (BAR_Y - 0.0145))
# depth (thigh angle) + head-vs-bar clearance at the bottom
knee_bot = bhead("shin.L")
print("DEPTH hip-knee=%+.3f (0=parallel,<0 below)" % (hip_bot.z - knee_bot.z))
_body = bpy.data.objects["Body_low"]; _dg = bpy.context.evaluated_depsgraph_get()
_ev = _body.evaluated_get(_dg); _me = _ev.to_mesh(); _mw = _body.matrix_world
_hv = [_mw @ v.co for v in _me.vertices if (_mw @ v.co).z > 0.08 and -0.6 < (_mw @ v.co).y < -0.15]
if _hv:
    _lowz = min(v.z for v in _hv)
    print("HEAD-BAR gap (headLowZ - barTopZ)=%+.3f (>0 = head clears bar)" % (_lowz - (cb.z + 0.0145)))
_ev.to_mesh_clear()

if os.environ.get("BUILD_ONLY") != "1":
    sc.frame_set(0)
    bpy.ops.wm.save_as_mainfile(filepath=WORK + "/back_squat.blend")
    print("SAVED back_squat.blend")
print("DONE DY=%.3f LEAN=%s" % (DY, SPINE_LEAN))
