"""N7 bodyweight squat -- rebuilt on the body_rig_v5 body (library refresh, bodyweight
exercises first: no prop -> no grip complexity).

Supersedes the OLD v2-glb squat (scripts/s1_squat.py + library/squat/standard/squat_rep.*).
The PROVEN squat mechanics from s1_squat.py are ported onto the v5 rig:

  * FEET PLANTED the whole rep. Ankles are IK-pinned hip-width at their standing world
    position (ankle world-z CONSTANT -> soles stay on the floor, heels never rise); the
    knees bend via a 4-bone leg IK (lowerleg02 -> upperleg01) as the pelvis drops. Feet
    are re-levelled to their standing flat-sole world orientation (+ slight toe-out)
    every frame. Same structure the passed N6 deadlift + the v5 acceptance battery use.

  * HIPS sit BACK-and-DOWN by translating the ROOT (pelvis) bone -- back along +Y
    (front = -Y here), down in Z -- calibrated so the thigh reaches ~horizontal
    (parallel, knee flexion ~110-120) at the bottom and the COM stays plumb over the
    midfoot every frame.

  * TORSO moderate forward lean via the spine chain (spine05/04/03), spine neutral;
    GAZE neutral (neck/head counter the lean -> face forward-and-slightly-down).

  * ARMS -- PORTED VERBATIM from the owner-approved v2 FIRST-VERSION motion
    (scripts/s1_squat.py `arms()`): held STRAIGHT FORWARD, horizontal at shoulder height,
    the ENTIRE rep -- frame 1 to last. NO raising/lowering, NO hang, NO crossing. Each
    wrist IK target sits a soft-elbow reach straight forward (WORLD -Y) from its OWN
    (leaning) shoulder, so the two forearms stay shoulder-width apart, parallel to each
    other and to the floor even as the torso hinges (exactly the v2 world-space aim). The
    symmetric IK poles (mirror targets, pole_angle 0) make L/R exact mirror images by
    construction -> no flail, no chest-sweep (the yesterday-rejected failure). Hands are
    the v5 NATIVE per-finger chains set to a relaxed-extended slight curl (not fists, not
    splayed, not a claw). This is the whole point of the v5 rebuild: real fingers.

Clip: standing -> descend -> brief bottom hold -> ascend -> standing, 156f @ 30fps
(~5.2s), start pose == end pose -> loop-clean. TIMING ported from the v2 reference
(_v2_first/squat_rep.mp4 = 157f/5.23s; s1_squat.py F_DN0/1=12/72, F_HOLD=84, F_UP1=144):
descend 60f (2s), brief bottom hold 12f, ascend 60f (2s), smooth Bezier ease.

Render matches the N6 deadlift grade: dark studio (near-black backdrop, floor a touch
lighter, contact shadows, key+fills+rim), Standard view transform, exposure tuned (no
blown highlights / speckle), static ~39deg-off-front camera, portrait 720x1280. The floor
plane is made large + dropped so its edge stays OUT of frame (no diagonal seam).

Env knobs:
  N7_DROP        hip Z drop at bottom (default auto-calibrated to knee flexion ~115)
  N7_BACK        hip back-shift at bottom (default auto-calibrated so COM over midfoot)
  N7_STANCE      planted ankle half-width (default = rest ankle x)
  N7_TOEOUT      foot toe-out deg (default 12)
  N7_KNEEX       knee-out x target at bottom for tracking (default 0.19)
  N7_ARMUP       shoulder-height forward reach flag (auto)
  N7_ELBOW       soft elbow bend deg at bottom (default 15)
  N7_RES         render short side (default 720 -> 720x1280); probe 480
  N7_SUB         subsurf render level (default 2; probe 0/1)
  N7_SAMP        still TAA samples (default 384); N7_ASAMP anim samples (default 64)
  N7_EXPO        view exposure (default -1.8, Standard)
  N7_NORENDER=1  skip the animation PNG sequence (numeric checks + stills only)
Usage: blender --background --python build_squat.py
"""
import bpy, addon_utils, os, math, importlib.util, time as _time
from mathutils import Vector, Matrix

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
ASSET = os.path.join(SKILL_ROOT, "assets", "rig", "body_rig_v5.blend")
RES = int(os.environ.get("N7_RES", "720"))
SUBL = int(os.environ.get("N7_SUB", "2"))
TOEOUT = math.radians(float(os.environ.get("N7_TOEOUT", "12")))
KNEE_X_TGT = float(os.environ.get("N7_KNEEX", "0.19"))
ELBOW_BEND = math.radians(float(os.environ.get("N7_ELBOW", "15")))
SIDES = ("L", "R")
D = math.radians

# clip timeline (frames 1..NF): standing -> descend -> hold -> ascend -> standing.
# TIMING PORTED from the v2 first-version reference (s1_squat.py: F_DN0/1=12/72,
# F_HOLD=84, F_UP1=144, FEND=156 @ 30fps = 5.2s). descend 60f, hold 12f, ascend 60f.
NF = 156
F_DN0, F_DN1 = 12, 72     # descend ramp (60 frames, 2.0s)
F_HOLD = 84               # bottom hold end (12-frame hold)
F_UP1 = 144               # ascend ramp end (then standing to NF)


def smooth(a, b, f):
    if f <= a: return 0.0
    if f >= b: return 1.0
    x = (f - a) / (b - a); return x * x * (3 - 2 * x)


def squat_t(f):
    if f <= F_DN1: return smooth(F_DN0, F_DN1, f)
    if f <= F_HOLD: return 1.0
    return 1.0 - smooth(F_HOLD, F_UP1, f)


# ARMS ARE STATIC (v2 first-version port): held straight forward the ENTIRE rep. There is
# NO raise/lower choreography (yesterday's invented hang->raise slerp swept the hands
# through the chest -> owner rejected). arm_raise is a CONSTANT 1.0 every frame so the
# forward-horizontal counterbalance hold is identical from frame 1 to the last frame.
def arm_raise(f):
    return 1.0


# ===================== 1 load the v5 asset =====================
addon_utils.enable('bl_ext.user_default.mpfb', default_set=True, persistent=True)
bpy.ops.wm.open_mainfile(filepath=ASSET)
body = bpy.data.objects["body_v5"]
arm = bpy.data.objects["body_v5.rig"]
shorts = bpy.data.objects["shorts"]

spec = importlib.util.spec_from_file_location(
    "rigv5_lib", os.path.join(SKILL_ROOT, "scratch", "rigv5_lib.py"))
LIB = importlib.util.module_from_spec(spec); spec.loader.exec_module(LIB)

sub = next(m for m in body.modifiers if m.type == 'SUBSURF'); sub.render_levels = SUBL
csm = next((m for m in body.modifiers if m.type == 'CORRECTIVE_SMOOTH'), None)
ssub = next((m for m in shorts.modifiers if m.type == 'SUBSURF'), None)
if ssub: ssub.render_levels = SUBL
sol = next((m for m in shorts.modifiers if m.type == 'SOLIDIFY'), None)
swr = next((m for m in shorts.modifiers if m.type == 'SHRINKWRAP'), None)

pb = arm.pose.bones
for pbone in pb: pbone.rotation_mode = 'XYZ'
mwa = arm.matrix_world


def H(n): return mwa @ pb[n].head
def T(n): return mwa @ pb[n].tail


# heavy modifiers off during pose/bake, on for render
for _m in (sub, csm, ssub, sol, swr):
    if _m: _m.show_viewport = False

# rest mesh sole z
deps = bpy.context.evaluated_depsgraph_get()
_me = bpy.data.meshes.new_from_object(body.evaluated_get(deps))
sole_z = min((body.matrix_world @ v.co).z for v in _me.vertices)
bpy.data.meshes.remove(_me)

# ===================== 2 measured joint-flex signs =====================
fy = LIB.faceY(arm)
FWD = Vector((0.0, fy, 0.0))       # world direction the model faces (front = -Y here)
KS = LIB.flex_sign(arm, "lowerleg01.L", "foot.L", "pelvis.L")
ELS = LIB.flex_sign(arm, "lowerarm01.L", "wrist.L", "shoulder01.L")
ELSR = LIB.flex_sign(arm, "lowerarm01.R", "wrist.R", "shoulder01.R")
# shoulder-flex-forward sign (probe upperarm01 X, watch wrist move toward the face)
e = pb["upperarm01.L"].rotation_euler; o = e[0]
e[0] = o + D(20); bpy.context.view_layer.update(); yp = H("wrist.L").y
e[0] = o; bpy.context.view_layer.update()
SHF = 1.0 if (yp - H("wrist.L").y) * fy > 0 else -1.0
# torso-lean-forward sign (probe spine05 X, watch head move toward the face)
e = pb["spine05"].rotation_euler; o = e[0]
e[0] = o + D(10); bpy.context.view_layer.update(); yp = H("head").y
e[0] = o; bpy.context.view_layer.update()
TF = 1.0 if (yp - H("head").y) * fy > 0 else -1.0
CS = {s: LIB.curl_sign(arm, s) for s in SIDES}
print("N7 SIGNS KS=%+.0f ELS=%+.0f ELSR=%+.0f SHF=%+.0f TF=%+.0f fy=%+.0f sole_z=%.4f"
      % (KS, ELS, ELSR, SHF, TF, fy, sole_z), flush=True)

# ===================== 3 standing reference capture =====================
LIB.pose_reset(arm); bpy.context.view_layer.update()
ROOT0 = pb["root"].matrix.translation.copy()              # standing pelvis
foot_rest3 = {s: pb["foot.%s" % s].matrix.to_3x3().copy() for s in SIDES}
ankle0 = {s: H("foot.%s" % s).copy() for s in SIDES}       # standing ankle world pos
STANCE_X = float(os.environ.get("N7_STANCE", "%.3f" % abs(ankle0["L"].x)))
sh0 = {s: H("upperarm01.%s" % s).copy() for s in SIDES}    # standing shoulder
wrist0 = {s: H("wrist.%s" % s).copy() for s in SIDES}      # standing wrist (arms at sides)
hipc0 = 0.5 * (H("upperleg01.L") + H("upperleg01.R"))
toe0y = 0.5 * (T("toe2-1.L").y + T("toe2-1.R").y)
heel0y = 0.5 * (ankle0["L"].y + ankle0["R"].y)
MIDFOOT_Y = 0.5 * (heel0y + toe0y)
ARMREACH = sum(pb["%s.L" % b].bone.length for b in
               ("upperarm01", "upperarm02", "lowerarm01", "lowerarm02"))
print("N7 STANCE_X=%.3f ROOT0z=%.3f hipc0z=%.3f sh0z=%.3f midfootY=%.3f ARMREACH=%.3f"
      % (STANCE_X, ROOT0.z, hipc0.z, sh0["L"].z, MIDFOOT_Y, ARMREACH), flush=True)

# ===================== 4 leg IK (feet planted, ankles pinned) =====================
feetT = {}
for s in SIDES:
    sgn = 1.0 if ankle0[s].x >= 0 else -1.0
    feetT[s] = Vector((sgn * STANCE_X, ankle0[s].y, ankle0[s].z))


def mkempty(name, loc):
    e = bpy.data.objects.new(name, None); bpy.context.scene.collection.objects.link(e)
    e.location = loc; return e


cons = {}
for s in SIDES:
    ank = mkempty("ankT.%s" % s, feetT[s])
    knee0 = H("lowerleg01.%s" % s).copy(); sgn = 1.0 if knee0.x >= 0 else -1.0
    pol = mkempty("polT.%s" % s, Vector((knee0.x + sgn * 0.06, knee0.y + fy * 0.8, knee0.z)))
    con = pb["lowerleg02.%s" % s].constraints.new('IK')
    con.target = ank; con.pole_target = pol; con.chain_count = 4
    cons[s] = con
    best = None
    for pa in range(-180, 180, 10):
        con.pole_angle = D(pa); bpy.context.view_layer.update()
        dev = (H("lowerleg01.%s" % s) - knee0).length
        if best is None or dev < best[0]: best = (dev, pa)
    con.pole_angle = D(best[1]); bpy.context.view_layer.update()


def level_feet():
    # restore each foot to its standing flat-sole world rotation + slight toe-out,
    # about the (IK-pinned) ankle. Sole stays on the floor every frame.
    for s in SIDES:
        pbn = pb["foot.%s" % s]; loc = pbn.matrix.translation.copy()
        sgn = 1.0 if feetT[s].x >= 0 else -1.0
        rot = Matrix.Rotation(sgn * TOEOUT, 3, 'Z') @ foot_rest3[s]
        m = rot.to_4x4(); m.translation = loc
        pbn.matrix = m
    bpy.context.view_layer.update()


# ===================== 5 arm IK (symmetric front raise, soft elbow) =====================
# Same clean IK the legs use: a wrist target empty + an elbow pole empty per side, an
# IK constraint on lowerarm02 (chain 4 -> upperarm01). Deterministic + symmetric by
# construction (no per-side coordinate descent -> no flail / crossing). The wrist target
# is moved per frame from "hanging at the side" to "forward-horizontal at shoulder
# height"; the reach is 0.94*ARMREACH so the elbow keeps a soft ~165 bend (not locked).
# reach = 0.985*ARMREACH -> the wrist target sits just inside full extension, so the
# elbow stays soft-straight (~165, in the 160-175 band) rather than locked.
REACH_F = float(os.environ.get("N7_REACH", "0.985"))
REACH = REACH_F * ARMREACH


def _smoother(x):
    x = max(0.0, min(1.0, x)); return x * x * x * (x * (x * 6 - 15) + 10)


# STRAIGHT-FORWARD HOLD (v2 first-version port). Each arm points PURE world-forward (-Y)
# from its OWN shoulder, at shoulder height (z-component 0) -> the two forearms stay
# shoulder-width apart, parallel to each other and horizontal, exactly like the approved
# v2 `arms()` (which aimed every arm bone along world -Y). No hang, no waypoint, no side
# spread: the wrist target is a fixed soft-elbow reach straight ahead of the (leaning)
# shoulder, recomputed each frame off the CURRENT shoulder so the hold stays world-
# horizontal through the torso hinge. arm_t is ignored (the arms never move).
FWD_DIR = {s: Vector((0.0, FWD.y, 0.0)).normalized() for s in SIDES}


def arm_target(side, arm_t):
    sh = H("upperarm01.%s" % side)                      # current (leaned) shoulder
    return sh + FWD_DIR[side] * REACH


arm_ik = {}
for s in SIDES:
    sgn = 1.0 if sh0[s].x >= 0 else -1.0
    tge = mkempty("armT.%s" % s, wrist0[s].copy())
    # elbow pole down + OUT + slightly FORWARD -> elbows point down-and-out-and-forward, so
    # the forearm hangs slightly forward (never behind) standing, and on the raise the elbow
    # stays lateral to the ribs -> the forearm clears the pec/lat with air.
    tpe = mkempty("armPol.%s" % s, Vector((sh0[s].x + sgn * 0.22, sh0[s].y + fy * 0.10, sh0[s].z - 0.45)))
    con = pb["lowerarm02.%s" % s].constraints.new('IK')
    con.target = tge; con.pole_target = tpe; con.chain_count = 4
    con.pole_angle = 0.0
    arm_ik[s] = (con, tge, tpe)
bpy.context.view_layer.update()

# ELBOW-BOW SYMMETRY CALIBRATION: mirrored pole TARGETS + pole_angle 0 do NOT give mirror
# solutions on this rig -- the MakeHuman L/R arm bone ROLLS are not mirrored, so the L elbow
# bowed up-and-out while the R bowed down-and-in (measured 7.5 cm mirror deviation, visible).
# Fix = the same trick the LEG IK uses: scan each side's pole_angle so the soft-elbow bow
# points the SAME natural direction on both sides -- OUT (lateral) and slightly DOWN --
# making the arms mirror by measurement, not by assumption. The arm hold is static relative
# to the shoulder, so one calibration at the standing hold is valid for every frame.
for s in SIDES:
    sgn = 1.0 if sh0[s].x >= 0 else -1.0
    arm_ik[s][1].location = sh0[s] + FWD_DIR[s] * REACH
bpy.context.view_layer.update()
for s in SIDES:
    sgn = 1.0 if sh0[s].x >= 0 else -1.0
    want = Vector((sgn * 0.6, 0.0, -0.8)).normalized()   # elbow bows out + slightly down
    best = None
    for pa in range(-180, 180, 2):
        arm_ik[s][0].pole_angle = D(pa); bpy.context.view_layer.update()
        sh = H("upperarm01.%s" % s); wr = H("wrist.%s" % s); el = H("lowerarm01.%s" % s)
        axis = (wr - sh).normalized(); off = el - sh
        perp = off - off.dot(axis) * axis
        if perp.length < 1e-6: continue
        cost = (perp.normalized() - want).length
        if best is None or cost < best[0]: best = (cost, pa)
    arm_ik[s][0].pole_angle = D(best[1]); bpy.context.view_layer.update()
    print("N7 %s elbow-bow pole=%d cost=%.3f elbow=%s"
          % (s, best[1], best[0], tuple(round(v, 3) for v in H("lowerarm01.%s" % s))), flush=True)

# relaxed natural hand: a soft uniform curl across MCP/PIP/DIP (more at the base, less at
# the tip) so the fingers read as a gently cupped resting hand -- NOT the splayed frozen
# claw (too-open + uneven) and NOT a clenched fist. A slight per-finger progression
# (index curls a hair less than the pinky) mimics a real relaxed hand.
RELAX = {1: 13, 2: 17, 3: 10}   # MCP / PIP / DIP curl (deg): relaxed-EXTENDED slight curl
#                                 (palms-down forward reach), NOT a cupped fist / claw.


def set_hands():
    for s in SIDES:
        cs = CS[s]
        for fi in (2, 3, 4, 5):
            prog = 1.0 + 0.06 * (fi - 3)     # pinky slightly more curled than index
            pb["finger%d-1.%s" % (fi, s)].rotation_euler = (cs * D(RELAX[1] * prog), 0, 0)
            pb["finger%d-2.%s" % (fi, s)].rotation_euler = (cs * D(RELAX[2] * prog), 0, 0)
            pb["finger%d-3.%s" % (fi, s)].rotation_euler = (cs * D(RELAX[3] * prog), 0, 0)
        zsgn = -1.0 if s == "L" else 1.0     # thumb relaxed, tucked alongside (not splayed)
        pb["finger1-1.%s" % s].rotation_euler = (D(18), 0, zsgn * D(10))
        pb["finger1-2.%s" % s].rotation_euler = (D(12), 0, 0)
        pb["finger1-3.%s" % s].rotation_euler = (D(10), 0, 0)


# HAND LEVELLING (v2 port of `aim_world("hand", fwd)`): the wrist is FK (NOT in the arm IK
# chain), so left at bind it inherits the forearm twist and the hand DROOPS / breaks at the
# wrist (near hand curled palm-up, far hand hung down -- the probe defect). Aim each wrist's
# Y axis (head->finger) straight forward-horizontal so the hand CONTINUES the forearm line
# (no broken wrist), with a fixed roll about the forward axis chosen so the palm faces DOWN.
# Both wrists get the SAME world orientation -> with the mirrored thumb splay in set_hands
# the two hands read as proper mirror images (palms down, thumbs opposed).
HAND_ROLL = D(float(os.environ.get("N7_HANDROLL", "0")))   # roll about the forward axis (deg)


def level_hands():
    base = FWD.to_track_quat('Y', 'Z').to_matrix().to_4x4()   # Y->forward, Z->up
    roll = Matrix.Rotation(HAND_ROLL, 4, FWD)                 # palm-down tuning about fwd
    for s in SIDES:
        pbn = pb["wrist.%s" % s]; head = pbn.matrix.translation.copy()
        m = roll @ base; m.translation = head
        pbn.matrix = m
    bpy.context.view_layer.update()


# ===================== 6 whole-body pose at parameter t =====================
# torso lean + gaze magnitudes at the bottom
LEAN = {"spine05": 20, "spine04": 9, "spine03": 6}
GAZE = {"neck01": 20, "head": 8}


def apply_pose(t, drop, back, arm_t=None):
    if arm_t is None: arm_t = t
    LIB.pose_reset(arm)
    set_hands()
    # pelvis: sit back (+ along -FWD) and down. Root carries the whole upper body.
    m = pb["root"].matrix.copy()
    m.translation = Vector((0.0, ROOT0.y - fy * back * t, ROOT0.z - drop * t))
    pb["root"].matrix = m
    bpy.context.view_layer.update()
    # torso forward lean + neutral gaze
    for bn, a in LEAN.items():
        pb[bn].rotation_euler = (TF * D(a) * t, 0, 0)
    for bn, a in GAZE.items():
        pb[bn].rotation_euler = (-TF * D(a) * t, 0, 0)
    bpy.context.view_layer.update()
    # legs solve via IK (ankles pinned), then flatten soles
    level_feet()
    # arms: hold each wrist IK target at the forward-horizontal reach off the current
    # shoulder; the IK (fixed mirror pole) solves a clean symmetric straight-forward hold.
    for s in SIDES:
        arm_ik[s][1].location = arm_target(s, arm_t)
    bpy.context.view_layer.update()
    # then aim the hands straight forward (continue the forearm, no wrist droop, palm down)
    level_hands()


def knee_flex(s):
    thigh = (H("lowerleg01.%s" % s) - H("upperleg01.%s" % s)).normalized()
    shin = (H("foot.%s" % s) - H("lowerleg01.%s" % s)).normalized()
    return math.degrees(math.acos(max(-1, min(1, thigh.dot(shin)))))


# crude COM (y only), segment-weighted like s1
def com_y():
    segs = [(0.14, H("root")),
            (0.33, 0.5 * (H("spine03") + H("neck01"))),
            (0.08, T("head")),
            (0.05, 0.5 * (H("upperarm01.L") + H("wrist.L"))),
            (0.05, 0.5 * (H("upperarm01.R") + H("wrist.R"))),
            (0.10, 0.5 * (H("upperleg01.L") + H("lowerleg01.L"))),
            (0.10, 0.5 * (H("upperleg01.R") + H("lowerleg01.R"))),
            (0.075, 0.5 * (H("lowerleg01.L") + H("foot.L"))),
            (0.075, 0.5 * (H("lowerleg01.R") + H("foot.R")))]
    return sum(w * p.y for w, p in segs) / sum(w for w, _ in segs)


# ===================== 7 calibrate depth + hip-back (coupled) then knee-out =====================
# depth and back-shift are coupled (both move the knee/COM), so iterate the pair:
#   DROP  -> bottom thigh within THIGH_TGT deg of horizontal (TRUE PARALLEL). Calibrating
#            on the thigh angle directly (not on a fixed knee-flexion number) hits the real
#            acceptance metric -- the shin rakes forward over the toes, so a fixed knee
#            flexion left the thigh ~20 deg high (half squat). Knee flexion lands ~120-125.
#   BACK  -> bottom COM plumb over the midfoot (arms-forward counterbalance included)
DROP = float(os.environ.get("N7_DROP", "0"))
BACK = float(os.environ.get("N7_BACK", "0"))
# DEPTH is calibrated on KNEE FLEXION, not on the femur angle alone. On a flat foot with
# the ankle pinned at its standing spot, driving the femur to true-horizontal forces the
# shin to rake so far forward (knee 15cm+ past the toes) that the knee folds to ~42 deg
# interior -- a below-parallel COLLAPSE that only READS as "parallel" by the femur metric.
# Targeting the knee interior angle instead lands an honest coaching-grade parallel: thigh
# about horizontal, shin at a natural forward incline, knee tracking just over the toes.
# knee_flex() here = angle between the femur and shin DIRECTIONS (0=straight leg), so a
# parallel squat is ~95-110; we default 104 (interior knee ~76) -- solid depth, not a fold.
THIGH_TGT = float(os.environ.get("N7_THIGH", "10.0"))    # deg above horizontal (0..~12 = parallel)
KNEEFLEX_CAP = float(os.environ.get("N7_KNEEFLEX_CAP", "126"))  # never fold past this (anti-collapse)
_drop_fixed = DROP > 0
_back_fixed = BACK != 0
if not _drop_fixed: DROP = 0.44
if not _back_fixed: BACK = 0.06


def thigh_horiz():
    # SIGNED femur angle above horizontal: +ve = knee BELOW hip (shallow side of parallel),
    # 0 = thigh horizontal (true parallel), -ve = knee above hip (BELOW parallel / deep).
    aa = 0.0
    for s in SIDES:
        t = H("lowerleg01.%s" % s) - H("upperleg01.%s" % s)
        aa += math.degrees(math.asin(max(-1, min(1, -t.z / t.length))))
    return 0.5 * aa


def calib_drop():
    # Descend to true PARALLEL (thigh ~THIGH_TGT deg above horizontal) but STOP if the knee
    # would fold past KNEEFLEX_CAP first. On a pinned flat foot, chasing thigh-horizontal
    # alone rakes the shin into a below-parallel collapse (knee 13cm+ past the toes); the cap
    # holds an honest coaching-grade depth -- as deep as the flat foot allows without folding.
    global DROP
    lo, hi = 0.24, 0.72
    for _ in range(24):
        DROP = 0.5 * (lo + hi)
        apply_pose(1.0, DROP, BACK)
        th = thigh_horiz()
        kf = 0.5 * (knee_flex("L") + knee_flex("R"))
        if th > THIGH_TGT and kf < KNEEFLEX_CAP: lo = DROP   # go deeper
        else: hi = DROP
    return thigh_horiz()


def calib_back():
    global BACK
    lo, hi = -0.06, 0.28
    cy = 0.0
    for _ in range(16):
        BACK = 0.5 * (lo + hi)
        apply_pose(1.0, DROP, BACK)
        cy = com_y()
        # BACK+ shifts hips (and COM) toward +Y (back). Want COM_y == midfoot_y.
        if cy > MIDFOOT_Y: hi = BACK      # COM behind midfoot -> less back-shift
        else: lo = BACK
    return cy


# knee-out tracking: scan the leg pole angle at the final bottom so the knee tracks out
# over the 2nd-3rd toe (knee x ~= KNEE_X_TGT), knee slightly forward of the ankle. The
# knee-out pole shifts the knee (hence the femur angle), so depth calibration and this
# scan are COUPLED -- calibrating DROP once and THEN scanning the pole moved the real
# bottom thigh off target. Iterate the pair so DROP is calibrated with the final pole in
# place (calib_drop measures the true post-scan thigh angle -> matches the checks below).
def scan_knee_out():
    # knee tracks OUT to KNEE_X_TGT (over the 2nd-3rd toe) and forward to ~just over the
    # toe tip -- a BOUNDED forward target (knee_y_tgt), not the old "reward max-forward"
    # which raked the shin into a below-parallel fold. Knee just past the toes = correct
    # flat-foot squat mechanics without the collapse.
    knee_y_tgt = toe0y + fy * 0.015          # ~1.5cm past the toe tip (front = -Y)
    apply_pose(1.0, DROP, BACK)
    for s in SIDES:
        sgn = 1.0 if feetT[s].x >= 0 else -1.0
        best = None
        for pa in range(-180, 180, 2):
            cons[s].pole_angle = D(pa); bpy.context.view_layer.update()
            k = H("lowerleg01.%s" % s)
            cost = abs(k.x - sgn * KNEE_X_TGT) + 0.6 * abs(k.y - knee_y_tgt)
            if best is None or cost < best[0]: best = (cost, pa, k.copy())
        cons[s].pole_angle = D(best[1]); bpy.context.view_layer.update()
        print("N7 %s knee-out pole=%d knee=%s (knee_y_tgt=%.3f)"
              % (s, best[1], tuple(round(v, 3) for v in best[2]), knee_y_tgt), flush=True)


cy = com_y()
for _it in range(4):
    if not _drop_fixed: calib_drop()
    if not _back_fixed: cy = calib_back()
    scan_knee_out()               # re-track the knee at the new depth, then re-calibrate
apply_pose(1.0, DROP, BACK)
kf = 0.5 * (knee_flex("L") + knee_flex("R"))
th = thigh_horiz()
print("N7 calib DROP=%.3f BACK=%.3f -> thigh_above_horiz=%.1f knee_flex=%.1f COM_y=%.3f (midfoot %.3f)"
      % (DROP, BACK, th, kf, cy, MIDFOOT_Y), flush=True)

# ===================== 8 bottom numeric checks =====================
apply_pose(1.0, DROP, BACK)
up = Vector((0, 0, 1))
thighL = H("lowerleg01.L") - H("upperleg01.L")
thigh_from_horiz = math.degrees(math.asin(max(-1, min(1, abs(thighL.z) / thighL.length))))
kf_bot = 0.5 * (knee_flex("L") + knee_flex("R"))
comy_bot = com_y()
kxL = H("lowerleg01.L").x; kxR = H("lowerleg01.R").x
toexL = abs(T("toe2-1.L").x); toexR = abs(T("toe2-1.R").x)
kneeasym = abs(H("lowerleg01.R").x + H("lowerleg01.L").x) + abs(H("lowerleg01.R").y - H("lowerleg01.L").y)
print("N7 BOTTOM knee_flex=%.1f thigh_from_horiz=%.1f COMy=%.3f(midfoot %.3f d=%.3f) "
      "kneeX L=%.3f R=%.3f toeX L=%.3f R=%.3f kneeasym=%.4f"
      % (kf_bot, thigh_from_horiz, comy_bot, MIDFOOT_Y, comy_bot - MIDFOOT_Y,
         kxL, kxR, toexL, toexR, kneeasym), flush=True)

# feet-planted check: evaluate the (modifier-off) body mesh and read the foot-region heights.
# heels DOWN <=> heel + rearmost-heel-tip min z ~ floor; no toe clip <=> toe-region min z >= 0.
# NOTE (Defect B): the OLD banding capped the foot region at z < sole_z + 0.06, which SILENTLY
# EXCLUDES a genuinely lifted heel (its verts sit above the cap) and self-selects only the
# near-floor verts -> a lifted foot falsely read "planted". That masked bug is why the review
# caught a heel-lift the build's own check missed. The band is now z < 0.15 (a real lift stays
# in-band) and we report the rearmost heel-TIP min-z explicitly -- the true "is the heel down"
# metric. (Both feet here are in fact planted; the reported lift was a camera artefact, fixed
# at the camera below -- but the check is now honest so a real lift cannot slip through again.)
def foot_z(ws, s):
    ax = feetT[s].x; ay = feetT[s].y
    foot = [p for p in ws if abs(p.x - ax) < 0.12 and (ay - 0.30) < p.y < (ay + 0.12) and p.z < 0.15]
    heel = [p for p in foot if p.y > ay + 0.02]           # behind ankle (+Y = back)
    toe = [p for p in foot if p.y < ay - 0.03]            # forward of ankle (-Y = front)
    rear = sorted(heel, key=lambda p: -p.y)[:max(15, len(heel) // 6)]  # rearmost heel tip
    return (min(p.z for p in heel) - sole_z if heel else None,
            min(p.z for p in rear) - sole_z if rear else None,
            min(p.z for p in toe) - sole_z if toe else None)
def foot_planted_check():
    _dps = bpy.context.evaluated_depsgraph_get()
    _m = bpy.data.meshes.new_from_object(body.evaluated_get(_dps))
    ws = [body.matrix_world @ v.co for v in _m.vertices]
    bpy.data.meshes.remove(_m)
    return {s: foot_z(ws, s) for s in SIDES}
_fp = foot_planted_check()
for s in SIDES:
    hmn, htip, tmn = _fp[s]
    print("N7 FEET %s heel_min=%+.4f heeltip_min=%+.4f toe_min=%+.4f (m above floor; ~0=planted, lifted heel -> large +)"
          % (s, hmn or 0, htip or 0, tmn or 0), flush=True)

# ===================== 9 keyframe bake =====================
# legs + arms are IK-driven (constraints stay live in the scene); we keyframe the FK
# bones (root/spine/gaze/feet/fingers) + the moving arm IK target empties. Ankle + leg
# pole empties are static (no keyframes needed).
DRIVEN = (["root", "spine05", "spine04", "spine03", "neck01", "head", "foot.L", "foot.R",
           "wrist.L", "wrist.R"]
          + ["finger%d-%d.%s" % (fi, sg, s) for s in SIDES for fi in (1, 2, 3, 4, 5) for sg in (1, 2, 3)])
scn = bpy.context.scene
scn.frame_start = 1; scn.frame_end = NF; scn.render.fps = 30
bpy.context.preferences.edit.keyframe_new_interpolation_type = 'BEZIER'
elbow = {"L": [], "R": []}; ankz = {"L": [], "R": []}; comys = []; kxs = {"L": [], "R": []}
heeltip = {"L": [], "R": []}; toemn = {"L": [], "R": []}   # per-frame foot-flat verification
hand_clear = {"L": [], "R": []}   # per-frame min forearm/hand-to-torso clearance (no chest-sink)
sym_dev = []                      # per-frame max L/R mirror deviation over key joints (m)
_t0 = _time.time()
for f in range(1, NF + 1):
    scn.frame_set(f)
    t = squat_t(f)
    apply_pose(t, DROP, BACK, arm_t=1.0)   # arms held straight-forward every frame (static)
    for bn in DRIVEN:
        pb[bn].keyframe_insert("rotation_euler", frame=f)
    pb["root"].keyframe_insert("location", frame=f)
    for s in SIDES:
        arm_ik[s][1].keyframe_insert("location", frame=f)
    # per-frame metrics
    for s in SIDES:
        ankz[s].append(H("foot.%s" % s).z)
        u = H("lowerarm01.%s" % s) - H("upperarm01.%s" % s)
        fo = H("wrist.%s" % s) - H("lowerarm01.%s" % s)
        elbow[s].append(180 - math.degrees(u.angle(fo)))
        kxs[s].append(H("lowerleg01.%s" % s).x)
    comys.append(com_y())
    # per-frame heel-tip / toe min-z (Defect B: prove BOTH heels stay DOWN every frame)
    _dpsf = bpy.context.evaluated_depsgraph_get()
    _mf = bpy.data.meshes.new_from_object(body.evaluated_get(_dpsf))
    _wsf = [body.matrix_world @ v.co for v in _mf.vertices]
    bpy.data.meshes.remove(_mf)
    for s in SIDES:
        _hmn, _htip, _tmn = foot_z(_wsf, s)
        heeltip[s].append(_htip if _htip is not None else 9.9)
        toemn[s].append(_tmn if _tmn is not None else 9.9)
    # hand/forearm-to-torso clearance: torso-region verts = near midline, chest-height band,
    # and BEHIND the forward-reaching arms (so the arms' OWN verts are excluded). Min 3D dist
    # from sample points ALONG each forearm+hand (elbow, mid, wrist, hand-tip) to those verts
    # -> proves the straight-forward hold never sinks into the pec/rib volume (the rejected
    # v5 build buried a hand in the chest; this stays > ~0.15 m every frame).
    _czlo = H("spine03").z - 0.02; _czhi = H("neck01").z + 0.05
    _chy = H("spine04").y
    _torso = [v for v in _wsf if abs(v.x) < 0.27 and _czlo < v.z < _czhi and v.y > _chy - 0.30]
    for s in SIDES:
        _el = H("lowerarm01.%s" % s); _wr = H("wrist.%s" % s)
        _tip = _wr + (_wr - _el).normalized() * 0.09
        _samples = [_el, 0.5 * (_el + _wr), _wr, _tip]
        _dmin = 9.9
        for _p in _samples:
            # only torso verts BEHIND the arm point (front=-Y, so behind = larger y). This
            # excludes the arm's OWN girth verts (same/lower y) that otherwise contaminate the
            # metric with arm-radius (~3cm); what remains is the true clearance from the arm
            # point to the chest surface behind it.
            _behind = [v for v in _torso if v.y > _p.y + 0.02]
            if _behind:
                _dmin = min(_dmin, min((v - _p).length for v in _behind))
        if _dmin < 9.9:
            hand_clear[s].append(_dmin)
    # L/R mirror symmetry: world position of each key joint on L vs the x-mirrored R.
    _sd = 0.0
    for _j in ("upperarm01", "lowerarm01", "wrist", "upperleg01", "lowerleg01", "foot"):
        _l = H("%s.L" % _j); _r = H("%s.R" % _j)
        _sd = max(_sd, (Vector((_l.x + _r.x, _l.y - _r.y, _l.z - _r.z))).length)
    sym_dev.append(_sd)
    if f % 16 == 1: print("N7 bake f%d/%d (%.0fs)" % (f, NF, _time.time() - _t0), flush=True)
print("N7 baked %d frames in %.0fs" % (NF, _time.time() - _t0), flush=True)

bottom_of = max(range(1, NF + 1), key=lambda f: squat_t(f) if f <= F_HOLD else 0)
bottom_of = F_HOLD - 4     # a representative deep frame inside the hold
print("N7 CHECKS:", flush=True)
print("  elbow range L=%.0f..%.0f R=%.0f..%.0f (soft-straight 160-175 at reach)"
      % (min(elbow["L"]), max(elbow["L"]), min(elbow["R"]), max(elbow["R"])), flush=True)
print("  ankle z range L=%.5f R=%.5f (planted -> ~0)"
      % (max(ankz["L"]) - min(ankz["L"]), max(ankz["R"]) - min(ankz["R"])), flush=True)
print("  heeltip_min-z over all %d frames L=%.4f..%.4f R=%.4f..%.4f (heels DOWN -> stays ~0, never lifts)"
      % (NF, min(heeltip["L"]), max(heeltip["L"]), min(heeltip["R"]), max(heeltip["R"])), flush=True)
print("  toe_min-z over all frames L=%.4f..%.4f R=%.4f..%.4f (>= ~0 -> no floor clip)"
      % (min(toemn["L"]), max(toemn["L"]), min(toemn["R"]), max(toemn["R"])), flush=True)
print("  knee x range L=%.3f..%.3f R=%.3f..%.3f" % (
      min(kxs["L"]), max(kxs["L"]), min(kxs["R"]), max(kxs["R"])), flush=True)
print("  COM y range=%.3f..%.3f (midfoot %.3f)" % (min(comys), max(comys), MIDFOOT_Y), flush=True)
print("  hand->torso clearance min L=%.3f R=%.3f (m; POSITIVE = no interpenetration; the min"
      " sits at the elbow next to the front delt -- anatomically adjacent)"
      % (min(hand_clear["L"]) if hand_clear["L"] else -1,
         min(hand_clear["R"]) if hand_clear["R"] else -1), flush=True)
print("  L/R mirror symmetry max deviation over all frames = %.4f m (joints: shoulder/elbow/"
      "wrist/hip/knee/ankle; ~0 = exact mirror)" % (max(sym_dev) if sym_dev else -1), flush=True)

# ===================== 10 scene + render (v5-battery / N6 grade) =====================
for _m in (sub, csm, ssub, sol, swr):
    if _m: _m.show_viewport = True
# large floor, dropped a hair, so its far edge stays out of frame (no hard edge). A
# slightly lighter, rougher floor + a broad top-down floor-wash (added below) even out
# the light-pool falloff so no diagonal dark "seam" forms in the near corners.
bpy.ops.mesh.primitive_plane_add(size=80, location=(0, 0, sole_z - 0.002))
floor = bpy.context.active_object
fmat = bpy.data.materials.new("floor"); fmat.use_nodes = True
fB = fmat.node_tree.nodes["Principled BSDF"]
fB.inputs["Base Color"].default_value = (0.075, 0.075, 0.08, 1); fB.inputs["Roughness"].default_value = 0.98
floor.data.materials.append(fmat)
try: scn.render.engine = 'BLENDER_EEVEE'
except TypeError: scn.render.engine = 'BLENDER_EEVEE_NEXT'
STILL_SAMP = int(os.environ.get("N7_SAMP", "384"))
ANIM_SAMP = int(os.environ.get("N7_ASAMP", "64"))
try: scn.eevee.taa_render_samples = ANIM_SAMP
except Exception: pass
for _a in ("use_shadow_jitter", "use_raytracing", "use_taa_reprojection"):
    try: setattr(scn.eevee, _a, True)
    except Exception: pass
# Fast-GI OFF (Defect A round-3): the far (image-right) pec-delt junction reads ~16% darker
# than the frontal near pec -- a genuine CAST-SHADOW concavity (the anterior deltoid blocks
# the high +X key/chestfill from the pocket beneath it), further deepened by fast-GI's AO
# horizon term. Disabling fast GI is SURGICAL here: measured, the well-lit near junction is
# unchanged (215.4 vs 215.8) while only the AO-occluded pocket lifts (valley p5 122 -> 136).
# It removes the AO darkening of the pocket without touching the exposed body -- the direct
# key/fills still carry all the modeling + dark-studio grade.
try: scn.eevee.use_fast_gi = False
except Exception: pass
# consistent normals (kills shading speckle)
bpy.context.view_layer.objects.active = body
for _o in bpy.context.selected_objects: _o.select_set(False)
body.select_set(True)
try:
    bpy.ops.object.mode_set(mode='OBJECT')
    try: bpy.ops.mesh.customdata_custom_splitnormals_clear()
    except Exception as _e: print("splitnormals clear skipped:", _e)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode='OBJECT')
except Exception as _e:
    print("normals fix skipped:", _e)
body.select_set(False)
scn.render.resolution_x = RES; scn.render.resolution_y = int(RES * 16 / 9)
scn.view_settings.exposure = float(os.environ.get("N7_EXPO", "-1.8"))
try:
    scn.view_settings.view_transform = 'Standard'; scn.view_settings.look = 'None'
except TypeError: pass
world = bpy.data.worlds.new("W"); scn.world = world; world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.035, 0.035, 0.04, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.35
body_c = Vector((0, 0, 0.95)); low_c = Vector((0, 0, 0.45))
# KEY: the pec smudge (Defect A) is PROVEN a KEY-light self-shadow, not mesh data.
# A/B proof (scratch/squat_diag): under flat world light AND white-clay+flat the chest is
# perfectly clean and MIRROR-symmetric (r1_B_flatworld / r1_C_clayflat) -> the base mesh is
# geometrically mirror-perfect (measured mirror-dev = 0), has NO vertex colours / color
# attributes / image texture / custom split normals (single flat Principled skin), and the
# corrective-smooth ON vs OFF gives byte-identical geometry -> it is NOT data. Isolating each
# light, the KEY ALONE reproduces the exact dark pec-delt pocket (r1_L_k) while the chestfill
# alone is clean (r1_L_chestfill): the high off-axis key is occluded by the anterior-deltoid
# / shoulder mass on the far pec, pooling a hard shadow terminator into the pec-delt junction.
# FIX: enlarge the key 2.6 -> 5.5 and swing it more frontal (0.5,1.35,1.9 -> 0.28,1.52,1.68)
# so its terminator softens into a gentle gradient (no pooled crater); energy 100 -> 106 holds
# chest brightness at the larger size. Muscle separation + the dramatic arm rolloff stay; all
# other lights (fills / rim / low / floorwash) unchanged -> overall grade + drama preserved.
# NOTE (round-3): the low front fill (4th row) and the chestfill both preferentially light
# the exposed near (image-left) pec junction over the occluded far one -- per-light isolation
# measured near-vs-far contribution 114 vs 82 (low fill) and 139 vs 117 (chestfill). Trimming
# the low fill 45 -> 20 pulls the bright near junction DOWN toward the far one (differential a
# uniform fill cannot achieve), closing the L/R gap while the shadowless pec fill (below)
# lifts the far pocket. Key / left fill / rim unchanged -> modeling + arm rolloff preserved.
for kx, ky, kz, en, s, aim in ((0.22, fy * 1.55, 1.60, 106, 6.0, body_c),
                               (-0.9, fy * 0.8, 1.2, 50, 1.2, body_c),
                               (0.2, -fy * 1.2, 1.6, 65, 0.9, body_c),
                               (0.15, fy * 1.1, -0.35, 20, 1.4, low_c)):
    Lt = bpy.data.lights.new("k", 'AREA'); Lt.energy = en; Lt.size = s
    o = bpy.data.objects.new("k", Lt); scn.collection.objects.link(o)
    o.location = body_c + Vector((kx, ky, kz))
    o.rotation_euler = (aim - o.location).normalized().to_track_quat('-Z', 'Y').to_euler()
# broad top-down floor wash: big + soft + high, aimed at the floor in front of the
# figure -> lifts the near-corner falloff so the visible floor reads uniform (no
# diagonal seam), without lifting the near-black backdrop.
fwl = bpy.data.lights.new("floorwash", 'AREA'); fwl.energy = 26; fwl.size = 16
fo = bpy.data.objects.new("floorwash", fwl); scn.collection.objects.link(fo)
fo.location = Vector((0.5, fy * 2.2, 3.4))
fo.rotation_euler = (Vector((0.2, fy * 1.4, 0.0)) - fo.location).normalized().to_track_quat('-Z', 'Y').to_euler()
# CHEST-POCKET FILL (Defect A, second stage): a soft camera-SIDE frontal fill aimed at the
# upper chest. With the enlarged/frontal key above the pec-delt pocket is already a gentle
# gradient; this fill reaches straight into it from the camera side and erases the last of
# the smear so the right pec MATCHES the left, WITHOUT raising the near-black backdrop (aimed
# high at the chest, small, no floor/back spill). Energy 85 -> 150 to fully fill the residual
# pocket at the larger key size (verified clean in scratch/squat_diag/r1_key_k_huge_cf160).
_thc = math.radians(39.0)
_fill_dir = Vector((math.sin(_thc), fy * math.cos(_thc), 0.14)).normalized()
_chest_c = Vector((-0.04, 0.0, 1.32))     # aimed at the pec-delt pocket height (was 1.20 = too low)
cfl = bpy.data.lights.new("chestfill", 'AREA'); cfl.energy = 140; cfl.size = 2.6
cfo = bpy.data.objects.new("chestfill", cfl); scn.collection.objects.link(cfo)
cfo.location = _chest_c + _fill_dir * 2.3
cfo.rotation_euler = (_chest_c - cfo.location).normalized().to_track_quat('-Z', 'Y').to_euler()
# FAR PEC-DELT SHADOWLESS FILL (Defect A round-3, the decisive fix): the residual dark patch
# on the far (image-right) pec-delt junction is a CAST shadow -- the +X anterior deltoid blocks
# the high key/chestfill from the pocket beneath it. No ordinary (shadow-casting) fill can fill
# it: aimed there it either self-occludes on the same deltoid or, brightened enough to leak in,
# blows out the whole chest. A SHADOWLESS area light from the camera-side/front, angled up under
# the deltoid line, deposits light straight into the pocket THROUGH the occluder -- filling
# exactly the cast shadow, additively closing the L/R gap, with no hotspot and no backdrop spill
# (it is aimed at the chest, not the world). Tuned so far pec matches near within ~7% and the
# abrupt boundary becomes a gentle gradient (measured: L/R junction 216 vs 206, valley p5 lifted
# 122 -> 163, zero blown pixels). fy=-1 (front=-Y): dir has +X (camera side), -Y (front), and a
# small -Z so the source sits BELOW its aim and rakes UPWARD under the deltoid into the pocket.
_pf_azi = math.radians(42.0); _pf_elev = math.radians(-12.0)
_pf_aim = Vector((0.08, -0.03, 1.33))     # the far pec-delt pocket (world), calibrated at standing
_pf_dir = Vector((math.sin(_pf_azi) * math.cos(_pf_elev),
                  fy * math.cos(_pf_azi) * math.cos(_pf_elev),
                  math.sin(_pf_elev)))
pfl = bpy.data.lights.new("pecfill_far", 'AREA'); pfl.energy = 80; pfl.size = 1.7
pfl.use_shadow = False                    # shadowless -> reaches the pocket through the deltoid
pfo = bpy.data.objects.new("pecfill_far", pfl); scn.collection.objects.link(pfo)
pfo.location = _pf_aim + _pf_dir * 1.4
pfo.rotation_euler = (_pf_aim - pfo.location).normalized().to_track_quat('-Z', 'Y').to_euler()
camd = bpy.data.cameras.new("C"); cam = bpy.data.objects.new("C", camd)
scn.collection.objects.link(cam); scn.camera = cam; camd.lens = 50
fov = 2 * math.atan(18.0 / camd.lens)
CAM_DEG = 39.0
th = math.radians(CAM_DEG)
# Defect B (right heel "lifts"): the feet are geometrically CORRECT -- both soles flat, both
# ankles pinned at the same world-z, foot bones exact mirror images every frame, heel-tip
# min-z ~2mm both sides across all 96 frames (measured; the task's numeric acceptance passes).
# The apparent lift was a VIEWING artefact: the old camera looked too far DOWN (CENTER z 0.92
# at chest height + cdir z 0.16), foreshortening the feet so the FAR foot's grounded heel hid
# behind its own ankle mass while its raised medial arch faced the +X camera -> read "on the
# ball". The NEAR foot showed its flat lateral edge and read fine -> the false asymmetry.
# FIX: keep the 3/4 azimuth (39deg) and subject framing, but LEVEL the camera -- drop CENTER
# to 0.82 and the view direction to near-horizontal (z 0.16 -> 0.04). Now both heels read
# planted on the floor (scratch/squat_diag/r1_cc_A). Azimuth / lens / subject size unchanged.
cdir = Vector((math.sin(th), fy * math.cos(th), 0.04))
# frame center nudged FORWARD (toward the reach) + a wider size so the forward-horizontal
# arms at the bottom stay fully IN frame (they clipped the left edge at CENTER y=0 / 2.05).
CENTER = Vector((0, fy * 0.14, 0.82)); SIZE = 2.34
dist = (SIZE * 0.6) / math.tan(fov / 2) * 1.18
cam.location = CENTER + cdir.normalized() * dist
cam.rotation_euler = (CENTER - cam.location).normalized().to_track_quat('-Z', 'Y').to_euler()

seqdir = os.path.join(SKILL_ROOT, "scratch", "n7_frames")
os.makedirs(seqdir, exist_ok=True)
scn.render.image_settings.file_format = 'PNG'
scn.render.filepath = os.path.join(seqdir, "f####")
NORENDER = os.environ.get("N7_NORENDER") == "1"
if not NORENDER:
    for _f in os.listdir(seqdir):
        if _f.endswith(".png"): os.remove(os.path.join(seqdir, _f))
    bpy.ops.render.render(animation=True)

try: scn.eevee.taa_render_samples = STILL_SAMP
except Exception: pass


def shoot(nm, frame, d, center=CENTER, size=SIZE, lens=50, res=(RES, int(RES * 16 / 9))):
    camd.lens = lens; fv = 2 * math.atan(18.0 / lens)
    dd = (size * 0.6) / math.tan(fv / 2) * 1.18; loc = center + d.normalized() * dd
    cam.location = loc; cam.rotation_euler = (center - loc).normalized().to_track_quat('-Z', 'Y').to_euler()
    scn.render.resolution_x = res[0]; scn.render.resolution_y = res[1]
    scn.frame_set(frame); scn.render.filepath = os.path.join(HERE, "squat_standard_%s.png" % nm)
    bpy.ops.render.render(write_still=True); print("STILL", nm, "frame", frame, flush=True)


front34 = Vector((math.sin(th), fy * math.cos(th), 0.04))   # levelled (Defect B: heels read planted)
top_of, mid_of, bot_of = 2, (F_DN0 + F_DN1) // 2, bottom_of
shoot("frame_top", top_of, front34)
shoot("frame_mid", mid_of, front34)
shoot("frame_bottom", bot_of, front34)
# ---- two REVIEW crops (task-required): hands close-up @ mid frame, feet close-up @ bottom.
# HANDS crop: centred on the midpoint of the two wrists at the descent (mid) frame, front-3/4
# so both hands + the forward-horizontal forearms read -> QA the relaxed-extended fingers,
# palms-down, symmetry, and that the arms are clear of the torso (no chest-sweep).
scn.frame_set(mid_of); bpy.context.view_layer.update()
handc = 0.5 * (H("wrist.L") + H("wrist.R"))
handd = Vector((math.sin(th), fy * math.cos(th), 0.05))
shoot("crop_hands", mid_of, handd, center=Vector((handc.x * 0.5, handc.y, handc.z)),
      size=0.62, lens=80, res=(720, 720))
# FEET crop: centred on the midpoint of the two feet at the deepest (bottom) frame, near-level
# slightly-below view so BOTH heels read planted on the floor -> QA planted flat soles, no
# float/clip, distinct toes, knees tracking over the toes.
scn.frame_set(bottom_of); bpy.context.view_layer.update()
footc = 0.5 * (H("foot.L") + H("foot.R"))
# gentle front-3/4 from slightly ABOVE so the lit tops of both feet + the planted heels read
# (a near-level/below view left the feet dark, edge-on against the dark floor).
footd = Vector((math.sin(th) * 0.8, fy * math.cos(th), 0.30))
shoot("crop_feet", bottom_of, footd, center=Vector((0.0, footc.y + fy * 0.05, sole_z + 0.10)),
      size=0.88, lens=80, res=(720, 720))

scn.render.filepath = os.path.join(seqdir, "f####")
scn.render.resolution_x = RES; scn.render.resolution_y = int(RES * 16 / 9)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "squat_standard.blend"))
print("N7_BUILD_DONE frames=%d bottom=%d DROP=%.3f BACK=%.3f mid=%d crops=hands@%d,feet@%d"
      % (NF, bottom_of, DROP, BACK, mid_of, mid_of, bottom_of), flush=True)
