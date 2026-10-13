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
# Build the BARBELL BACK SQUAT (high-bar) demo on the v4 per-finger rig, with the
# now-FIXED grip. INTEGRATION of three separately-solved pieces:
#
#  1) v4 per-finger closed grip (hand_sep_v4.pose_grip: 15 bones/hand, curl 70/70/70,
#     thumb 28/46/48 over the top) -- same grip source as e_back_squat_v4.py.
#  2) bar-collision / offset geometry fix (hand_v4_gripfix.py): the closed v4 grip
#     PENETRATED the bar (192 verts inside -> shards). Its offset function pushes every
#     vertex inside the bar cylinder radially OUT onto the bar surface
#     (target = r + eps; softplus feather, k=2000, smooth OFF). Verified 192 -> 0.
#     Reused HERE: because the grip is RIGID relative to the bar (constant finger +
#     hand local pose every frame -> the hand-to-bar relationship is FRAME-INVARIANT),
#     the correction is computed ONCE in the grip's reference frame and BAKED into the
#     REST mesh as a constant corrective. It then rides through the animation skinning
#     for free (no per-frame collision solve). Transfer is via the per-vertex
#     linear-blend-skin matrix under the reference grip pose: a posed-space radial push
#     is mapped back to rest space by M_skin^-1, so after skinning it reproduces the
#     gripfix offset -- and, being rigid, seats the fingers on the REAL bar every frame.
#  3) arm-orientation fix (e_back_squat_v3_fix.py): the elbow pole must point DOWN and
#     slightly BACK (+Y), not forward. e_back_squat_v4.py used the OLD forward pole
#     (-0.30 Y) which read as a REVERSED grip. Corrected here to f=(sc*0.28,+0.22,-1.0).
#     GRIP_ROLL re-tuned for the v4 hand (env ROLL).
#
# Also keeps e_back_squat_v4.py's arm-LOCATION fix (hand parented to the short
# forearm_twist bone needs the arm-bone LOCATION captured + keyframed, not just
# rotation) and the rigid grip transfer / feet-planted leg IK / high-bar shelf /
# torso lean / gaze / dark studio (unchanged from v3/v4 -- do NOT touch that machinery).
#
# Env BUILD_ONLY=1 -> build + print numbers, skip save.  ROLL / POLEY etc. tunable.
import bpy, sys, math, os
from mathutils import Vector, Matrix

SKILL = _SKILL_ROOT
WORK = _os.path.join(_WORK_ROOT, "back_squat_v4_grip")
sys.path.append(SKILL + "/scripts")
from prop_barbell import make_barbell
import hand_sep_v4 as H
import hand_v4_gripfix as G   # reuse the offset math (_softplus, INSIDE_MARGIN)

# ---------------------------------------------------------------- load v4 rig ---
RIG_GLB = os.environ.get("RIG_GLB",
                         SKILL + "/assets/rig/bodybuilder_rigged_v4_r8_lowpoly.glb")
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=RIG_GLB)
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
print("LOADED_RIG", RIG_GLB)

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

# --- HIGH-BAR tuning: hips drop mostly straight down; a touch of torso lean. ---
LEAN_SCALE = float(os.environ.get("LEAN", "1.40"))
SPINE_LEAN = (10.0 * LEAN_SCALE, 15.0 * LEAN_SCALE, 15.0 * LEAN_SCALE)
def torso(t):
    if t <= 0: return
    wrot("spine", 'X', SPINE_LEAN[0] * t)
    wrot("spine.001", 'X', SPINE_LEAN[1] * t)
    wrot("spine.002", 'X', SPINE_LEAN[2] * t)

GAZE = float(os.environ.get("GAZ", "-28.0"))
def gaze(t):
    if t <= 0: return
    wrot("neck", 'X', GAZE * t); wrot("head", 'X', GAZE * t)

def smooth(a, b, f):
    if f <= a: return 0.0
    if f >= b: return 1.0
    x = (f - a) / (b - a); return x * x * (3 - 2 * x)

# ============================================================ v4 GRIP (rigid) ===
BAR_Y, BAR_Z = 0.222, 0.566       # high-bar shelf below C7 (same as v3/v4)
GRIP_X = 0.315                     # grip just outside the shoulders
GRIP_ROLL = float(os.environ.get("ROLL", "8.0"))   # palm roll about bar axis (v4-tuned:
# swept 8/14/20 on hand crops -> 8 reads most natural, knuckles over the top of the bar)
SHAFT_R = 0.0137                   # match the v4 grip's fitted radius (fist seats on shaft)

# elbow pole: DOWN + slightly BACK (+Y). e_back_squat_v4 used -0.30 (forward) = the
# reversed-grip bug; e_back_squat_v3_fix landed +0.22. Exposed via env for tuning.
POLE_X = float(os.environ.get("POLEX", "0.28"))
POLE_Y = float(os.environ.get("POLEY", "0.22"))
POLE_Z = float(os.environ.get("POLEZ", "-1.0"))

ARM_BONES = []
for s in ('.L', '.R'):
    ARM_BONES += ["upper_arm" + s, "forearm" + s, "forearm_twist" + s, "hand" + s]
FINGER_NAMES = ("thumb", "index", "middle", "ring", "pinky")
FING_BONES = []
for s in ('.L', '.R'):
    for fn in FINGER_NAMES:
        for i in (1, 2, 3):
            FING_BONES.append("%s_%02d%s" % (fn, i, s))

def capture_ref_grip_quats():
    """Apply hand_sep_v4's canonical per-finger closed-grip curl to the LEFT
    fingers/thumb in bind pose, capture the LOCAL quats, mirror for the right."""
    reset_bind()
    for finger in H.FINGERS:
        a, b, c = H.GRIP_CURL[finger]
        H.wrot(rig, "%s_01.L" % finger, 'Y', a)
        H.wrot(rig, "%s_02.L" % finger, 'Y', b)
        H.wrot(rig, "%s_03.L" % finger, 'Y', c)
    tz, t2y, t3y = H.GRIP_THUMB
    H.wrot(rig, "thumb_01.L", 'Z', tz)
    H.wrot(rig, "thumb_02.L", 'Y', t2y)
    H.wrot(rig, "thumb_03.L", 'Y', t3y)
    bpy.context.view_layer.update()
    left_bones = ["%s_%02d.L" % (fn, i) for fn in FINGER_NAMES for i in (1, 2, 3)]
    qL = {b: rig.pose.bones[b].rotation_quaternion.copy() for b in left_bones}
    q = dict(qL)
    for b, v in qL.items():
        rb = b[:-2] + ".R"
        q[rb] = (v.w, v.x, -v.y, -v.z)
    reset_bind()
    return q

FING_LOCAL = capture_ref_grip_quats()

# ==================== GRIP-FIX: bake the collision offset into the REST mesh =====
# hand_v4_gripfix's verified final params (eps/k), smooth OFF (smoothing exploded the
# low-poly fingertips). The offset math (radial softplus push onto the bar surface) is
# reused verbatim; only the transfer differs: computed in the actual frame-0 grip pose
# and mapped to REST space per vertex via the linear-blend-skin matrix.
GF_EPS, GF_K = 0.0008, 2000.0
GF_XZ_R = 0.06                 # only touch verts within 6cm of the bar axis radially
ARM_MW = rig.matrix_world.copy()
MESH_MW = mesh.matrix_world.copy()
HAND_VERTS = set()   # collected hand-region vert indices, reused for pen. checks

def _bones_of_side(side):
    s = {"hand" + side}
    for fn in FINGER_NAMES:
        for i in (1, 2, 3):
            s.add("%s_%02d%s" % (fn, i, side))
    return s

def _skin_matrix_world(vi):
    """Per-vertex linear-blend-skin matrix mapping MESH-LOCAL rest co -> WORLD posed
    co, under the currently-posed rig. Uses ALL of the vertex's weighted deform bones
    (NOT just the hand subset): wrist verts bleed weight onto forearm/forearm_twist,
    so a hand-only normalization is wrong there and tears the rest edit into shards.
    In the reference grip pose the non-finger bones sit at bind (~identity), so the
    full-weight matrix exactly matches Blender's evaluated deform (mean err ~1e-6)."""
    v = mesh.data.vertices[vi]
    M = None; tot = 0.0
    for g in v.groups:
        gname = mesh.vertex_groups[g.group].name
        pb = rig.pose.bones.get(gname)
        if pb is None:
            continue
        w = g.weight
        if w <= 0.0:
            continue
        rest = rig.data.bones[gname].matrix_local
        Mi = pb.matrix @ rest.inverted()          # armature-space skin transform
        contrib = Mi * w
        M = contrib if M is None else (M + contrib)
        tot += w
    if M is None or tot < 1e-8:
        return None
    M = M * (1.0 / tot)
    return ARM_MW @ M @ ARM_MW.inverted() @ MESH_MW

def _is_hand_vert(vi, bones):
    """A region vert counts as a HAND vert if it carries real weight on a hand/finger
    bone (used to gate the correction + penetration check to the fist)."""
    for g in mesh.data.vertices[vi].groups:
        if g.weight > 0.02 and mesh.vertex_groups[g.group].name in bones:
            return True
    return False

def apply_grip_correction():
    """Bake the gripfix radial offset into the REST mesh (both hands), computed in
    the ACTUAL frame-0 grip pose against the REAL barbell shaft. The rig must already
    be posed at the frame-0 grip (pose_grip_once left it there). Because the grip is
    rigid, targeting the real bar directly (rather than the isolated reference bar via
    a rigid-transfer hop) removes the transfer residual and zeroes real-frame
    penetration. Reuses G._softplus + G.INSIDE_MARGIN. The radial push is about the
    bar axis (world-X at frame 0, through world Y=BAR_Y, Z=BAR_Z) so it is
    roll-invariant. Returns (before_inside, moved)."""
    by, bz = BAR_Y, BAR_Z
    r = SHAFT_R; target = r + GF_EPS
    total_before = 0; total_moved = 0
    for side, sign in ((".L", 1.0), (".R", -1.0)):
        bones = _bones_of_side(side)
        for vi, v in enumerate(mesh.data.vertices):
            xs = v.co.x * sign
            if xs < 0.55 or not (0.44 < v.co.z < 0.63):
                continue
            if not _is_hand_vert(vi, bones):
                continue
            M = _skin_matrix_world(vi)
            if M is None:
                continue
            HAND_VERTS.add(vi)
            posed = M @ v.co
            dy = posed.y - by; dz = posed.z - bz
            d = math.hypot(dy, dz)
            if d > GF_XZ_R or d < 1e-6:
                continue
            if d < r - G.INSIDE_MARGIN:
                total_before += 1
            new_d = target + G._softplus(d - target, GF_K)
            if new_d - d > 1e-6:
                s = new_d / d
                tgt_world = Vector((posed.x, by + dy * s, bz + dz * s))
                v.co = M.inverted() @ tgt_world
                total_moved += 1
        mesh.data.update()
    return total_before, total_moved

# reference (bind) geometry of the LEFT hand + the bar it wraps (post-correction)
capture_bind()   # leaves rig in bind
R0_L = rig.pose.bones["hand.L"].matrix.to_3x3().copy()
HAND_HEAD_REF_L = rig.pose.bones["hand.L"].matrix.translation.copy()
PBAR_REF_L = Vector((H.GRIP_BAR[0], 0.0, H.GRIP_BAR[1]))
LOCAL_OFF_L = R0_L.transposed() @ (PBAR_REF_L - HAND_HEAD_REF_L)

Rz = Matrix.Rotation(math.radians(-90.0), 3, 'Z')   # local-Y(bar) -> world X
S = Matrix.Diagonal(Vector((-1.0, 1.0, 1.0)))       # YZ-plane mirror

def grip_targets(side):
    Rt_L = Matrix.Rotation(math.radians(GRIP_ROLL), 3, 'X') @ Rz
    if side == ".L":
        Rt = Rt_L; R0 = R0_L; loff = LOCAL_OFF_L; Gt = Vector((GRIP_X, BAR_Y, BAR_Z))
    else:
        Rt = S @ Rt_L @ S; R0 = S @ R0_L @ S; loff = S @ LOCAL_OFF_L
        Gt = Vector((-GRIP_X, BAR_Y, BAR_Z))
    Rhand = Rt @ R0
    hand_head = Gt - Rhand @ loff
    return Rhand, hand_head

# 2-link arm IK: place the wrist (hand head) at `wrist`, elbow pole DOWN + BACK + out.
def solve_arm(side, sc_sign, wrist):
    P0 = bhead("upper_arm" + side)
    base = wrist - P0; d = base.length
    l1 = rig.pose.bones['upper_arm' + side].length
    l2 = rig.pose.bones['forearm' + side].length
    d = min(d, l1 + l2 - 1e-4); n = base.normalized()
    ca = max(-1.0, min(1.0, (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d))); a1 = math.acos(ca)
    proj = l1 * math.cos(a1); h = l1 * math.sin(a1)
    f = Vector((sc_sign * POLE_X, POLE_Y, POLE_Z))   # elbow DOWN + BACK + out (fixed)
    perp = f - (f.dot(n)) * n
    if perp.length < 1e-5:
        perp = Vector((0, 0, -1)); perp = perp - (perp.dot(n)) * n
    perp.normalize()
    K = P0 + proj * n + h * perp
    set_seg("upper_arm" + side, K - P0)
    set_seg("forearm" + side, wrist - K)
    aim_world("forearm_twist" + side, wrist - K)

def pose_grip_once():
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
    # arm-LOCATION fix: hand<side> parented to the SHORT forearm_twist bone -> the
    # matrix override that seats the wrist at hand_head yields a non-zero hand
    # LOCATION; reset_bind zeroes locations each frame, so re-apply it or the fist
    # drops off the bar (the v4 fix).
    loc = {b: rig.pose.bones[b].location.copy() for b in ARM_BONES}
    return grip, loc

GRIP_LOCAL, GRIP_LOCAL_LOC = pose_grip_once()
for s in ('.L', '.R'):
    w = bhead("hand" + s)
    print("GRIP%s wrist=(%.3f,%.3f,%.3f)" % (s, w.x, w.y, w.z))

# pose_grip_once left the rig posed at the frame-0 grip -> bake the collision offset
# into the rest mesh now (targets the REAL bar). Constant corrective; rides the anim.
GF_BEFORE, GF_MOVED = apply_grip_correction()
print("GRIPFIX rest-bake: hand_verts=%d inside_before=%d moved=%d (eps=%.4f k=%.0f shaft_r=%.4f)"
      % (len(HAND_VERTS), GF_BEFORE, GF_MOVED, GF_EPS, GF_K, SHAFT_R))

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
    for b in ARM_BONES + FING_BONES:
        rig.pose.bones[b].rotation_quaternion = GRIP_LOCAL[b]
    for b in ARM_BONES:
        rig.pose.bones[b].location = GRIP_LOCAL_LOC[b]
    for pb in rig.pose.bones:
        pb.keyframe_insert('rotation_quaternion', frame=f)
    for b in ARM_BONES:
        rig.pose.bones[b].keyframe_insert('location', frame=f)
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
def mesh_back_y(fr, zc):
    sc.frame_set(fr); bpy.context.view_layer.update()
    dg = bpy.context.evaluated_depsgraph_get(); ev = mesh.evaluated_get(dg)
    me = ev.to_mesh(); mw = mesh.matrix_world
    ys = [(mw @ v.co).y for v in me.vertices
          if abs((mw @ v.co).z - zc) < 0.03 and abs((mw @ v.co).x) < 0.12]
    r = max(ys) if ys else None; ev.to_mesh_clear(); return r
mb0 = mesh_back_y(0, c0.z); mbb = mesh_back_y(78, cb.z)
print("OCC top: bar_front_edge_y=%.3f  mesh_back_y=%.3f  gap=%+.3f (>=0 occluded)"
      % (c0.y - SHAFT_R, mb0, (c0.y - SHAFT_R) - mb0))
print("OCC bot: bar_front_edge_y=%.3f  mesh_back_y=%.3f  gap=%+.3f (>=0 occluded)"
      % (cb.y - SHAFT_R, mbb, (cb.y - SHAFT_R) - mbb))
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

# ---- REAL-FRAME grip penetration check: hand verts vs the actual barbell shaft ----
# The bar axis runs along the bar-local X; measure radial dist of each HAND vert to
# that axis line and count verts inside SHAFT_R - INSIDE_MARGIN. Rigid grip => should
# be ~0 at every frame (verify top / mid / bottom to be safe).
def grip_penetration(fr):
    sc.frame_set(fr); bpy.context.view_layer.update()
    Cb = bar.matrix_world.translation.copy()
    axis = (bar.matrix_world.to_3x3() @ Vector((1.0, 0.0, 0.0))).normalized()
    dg = bpy.context.evaluated_depsgraph_get(); ev = mesh.evaluated_get(dg)
    me = ev.to_mesh(); mw = mesh.matrix_world
    inside = 0; mind = 1e9
    for vi in HAND_VERTS:
        P = mw @ me.vertices[vi].co
        rel = P - Cb
        radial = (rel - rel.dot(axis) * axis).length
        # only near the shaft span (skip verts far along the axis / off the bar)
        along = abs(rel.dot(axis))
        if along > 0.55:
            continue
        if radial < SHAFT_R - G.INSIDE_MARGIN:
            inside += 1
            mind = min(mind, radial)
    ev.to_mesh_clear()
    return inside, (mind if inside else SHAFT_R)

for label, fr in (("top", 0), ("mid", 40), ("bottom", 78)):
    pin, pmin = grip_penetration(fr)
    print("GRIP_PEN %-6s frame=%3d inside=%d deepest=%.4f (shaft_r=%.4f)"
          % (label, fr, pin, pmin, SHAFT_R))

if os.environ.get("BUILD_ONLY") != "1":
    os.makedirs(WORK, exist_ok=True)
    sc.frame_set(0)
    bpy.ops.wm.save_as_mainfile(filepath=WORK + "/back_squat_v4_grip.blend")
    print("SAVED back_squat_v4_grip.blend")
print("DONE ROLL=%.1f POLE=(%.2f,%.2f,%.2f) BAR=(%.3f,%.3f) GRIP_X=%.3f SHAFT_R=%.4f"
      % (GRIP_ROLL, POLE_X, POLE_Y, POLE_Z, BAR_Y, BAR_Z, GRIP_X, SHAFT_R))
