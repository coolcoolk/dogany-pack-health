"""Acceptance battery for body_rig_v5. Builds the approved body (drawers ON) once,
applies the deform recipe (armature preserve-volume + JOINT-MASKED corrective
smooth + subsurf), then poses it into 5 static poses and renders full-body + zoom
crops of knee/hand/elbow/hip. Dark studio, Standard view transform, high samples.

Feet are actually PLANTED for the leg poses (squat/hinge): ankles pinned hip-width
at standing floor height with built-in leg IK, hips dropped by translating the
ROOT BONE (not the whole armature -- that was the round-1 float/converge bug),
soles re-levelled flat.

blender --background --python rigv5_battery.py -- [pose1 ...] [asset]
  poses: squat hinge grip curl stand   (default: all)
  asset: load the saved canonical blend (drawers already on) instead of building
"""
import bpy, os, sys, math, importlib.util
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("rigv5_lib", os.path.join(HERE, "rigv5_lib.py"))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

ALL = ["squat", "hinge", "grip", "curl", "stand"]
args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
ASSET = "asset" in args
poses = [a for a in args if a in ALL] or ALL[:]
OUT = os.path.join(HERE, "rigv5_battery" + ("_asset" if ASSET else ""))
os.makedirs(OUT, exist_ok=True)

# ---------- build once (or load the canonical asset) ----------
if ASSET:
    L.enable_mpfb()
    bpy.ops.wm.open_mainfile(filepath=os.path.join(
        os.path.dirname(HERE), "assets", "rig", "body_rig_v5.blend"))
    body = bpy.data.objects["body_v5"]
    arm = bpy.data.objects["body_v5.rig"]
    for pbm in arm.pose.bones:
        pbm.rotation_mode = 'XYZ'
else:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    L.enable_mpfb()
    body = L.build_body()
    shorts = L.build_shorts(body)
    arm = L.add_rig(body, "default")
    L.attach_shorts(shorts, arm, body)
    L.clean_weights(body, limit=4, normalize=True, smooth_iters=0)
    mask = L.build_joint_mask(body, arm)
    L.configure_deform(body, preserve_volume=True, corrective=True,
                       cs_factor=0.6, cs_iters=12, cs_vgroup=mask)

pb = arm.pose.bones
mwa = arm.matrix_world
fy = L.faceY(arm)
D = math.radians
SIDES = ("L", "R")


def H(n):
    return mwa @ pb[n].head


def T(n):
    return mwa @ pb[n].tail


# ---------- measured signs ----------
KS = L.flex_sign(arm, "lowerleg01.L", "foot.L", "pelvis.L")
HS = L.flex_sign(arm, "upperleg01.L", "lowerleg01.L", "spine01")
ELS = L.flex_sign(arm, "lowerarm01.L", "wrist.L", "shoulder01.L")
ELSR = L.flex_sign(arm, "lowerarm01.R", "wrist.R", "shoulder01.R")
e = pb["upperarm01.L"].rotation_euler; o = e[0]
e[0] = o + D(20); bpy.context.view_layer.update(); yp = H("wrist.L").y
e[0] = o; bpy.context.view_layer.update()
SHF = 1.0 if (yp - H("wrist.L").y) * fy > 0 else -1.0
e = pb["spine05"].rotation_euler; o = e[0]
e[0] = o + D(10); bpy.context.view_layer.update(); yp = H("head").y
e[0] = o; bpy.context.view_layer.update()
TF = 1.0 if (yp - H("head").y) * fy > 0 else -1.0
# root-pitch sign that carries the shoulders toward the face (hip hinge)
c0 = ((H("shoulder01.L") + H("shoulder01.R")) / 2).y
pb["root"].rotation_euler = (D(10), 0, 0); bpy.context.view_layer.update()
RS = 1.0 if (((H("shoulder01.L") + H("shoulder01.R")) / 2).y - c0) * fy > 0 else -1.0
pb["root"].rotation_euler = (0, 0, 0); bpy.context.view_layer.update()
print("SIGNS KS=%+.0f HS=%+.0f EL=%+.0f SHF=%+.0f TF=%+.0f RS=%+.0f fy=%+.0f"
      % (KS, HS, ELS, SHF, TF, RS, fy))


def clear_leg_ik():
    for s in SIDES:
        for c in list(pb["lowerleg02.%s" % s].constraints):
            pb["lowerleg02.%s" % s].constraints.remove(c)
    for o in [o for o in bpy.data.objects if o.name.startswith(("ankT.", "polT."))]:
        bpy.data.objects.remove(o, do_unlink=True)
    arm.location = (0, 0, 0)


def reset():
    clear_leg_ik()
    L.pose_reset(arm)
    bpy.context.view_layer.update()


def mkempty(name, loc):
    e = bpy.data.objects.new(name, None)
    bpy.context.scene.collection.objects.link(e)
    e.location = loc
    return e


def knee_angle(s):
    thigh = (H("lowerleg01.%s" % s) - H("upperleg01.%s" % s)).normalized()
    shin = (H("foot.%s" % s) - H("lowerleg01.%s" % s)).normalized()
    return math.degrees(math.acos(max(-1, min(1, thigh.dot(shin)))))


def descend(setget, score, steps, rounds=30):
    """Generic 1-D-per-DOF coordinate descent. setget = list of (get, set) for
    each DOF; score smaller = better."""
    best = score()
    for st in steps:
        for _ in range(rounds):
            improved = False
            for get, setv in setget:
                for d in (st, -st):
                    old = get()
                    setv(old + d); bpy.context.view_layer.update()
                    s1 = score()
                    if s1 < best - 1e-9:
                        best = s1; improved = True
                    else:
                        setv(old); bpy.context.view_layer.update()
            if not improved:
                break
    return best


def plant_legs(drop_z, back=0.0, stance=0.11, kneeout=0.07):
    """Feet stay planted where they stand (hip-width), hips drop to world z=drop_z
    (+back along -face) by translating the ROOT bone; built-in leg IK bends the
    knees; then each foot is restored to its STANDING world orientation (a flat
    sole) about the IK-pinned ankle -- not toe-height matching, which has a
    tiptoe second solution the descent used to fall into."""
    # capture the standing (flat-sole) foot world matrices before any posing
    foot_rest = {s: pb["foot.%s" % s].matrix.copy() for s in SIDES}
    feetT = {}
    for s in SIDES:
        a = H("foot.%s" % s)
        sgn = 1.0 if a.x >= 0 else -1.0
        feetT[s] = Vector((sgn * stance, a.y, a.z))
    for s in SIDES:
        ank = mkempty("ankT.%s" % s, feetT[s])
        knee0 = H("lowerleg01.%s" % s)
        sgn = 1.0 if knee0.x >= 0 else -1.0
        pol = mkempty("polT.%s" % s,
                      Vector((knee0.x + sgn * kneeout, knee0.y + fy * 0.8, knee0.z)))
        con = pb["lowerleg02.%s" % s].constraints.new('IK')
        con.target = ank; con.pole_target = pol; con.chain_count = 4
        best = None
        for pa in range(-180, 180, 10):
            con.pole_angle = D(pa); bpy.context.view_layer.update()
            dev = (H("lowerleg01.%s" % s) - knee0).length
            if best is None or dev < best[0]:
                best = (dev, pa)
        con.pole_angle = D(best[1]); bpy.context.view_layer.update()
    # drop the pelvis: translate root.location (world target for the hip centroid)
    hy = (H("upperleg01.L").y + H("upperleg01.R").y) / 2
    HSTAR = Vector((0, hy + fy * back, drop_z))

    def hscore():
        c = (H("upperleg01.L") + H("upperleg01.R")) / 2
        return (c - HSTAR).length
    rb = pb["root"]
    dofs = [((lambda i=i: rb.location[i]),
             (lambda v, i=i: rb.location.__setitem__(i, v))) for i in (0, 1, 2)]
    descend(dofs, hscore, steps=(0.04, 0.008), rounds=40)
    # flat sole: give each foot back its standing world ROTATION about the
    # current (IK-pinned) ankle head -- reproduces the planted-foot geometry
    # exactly, no tiptoe ambiguity.
    for s in SIDES:
        fb = pb["foot.%s" % s]
        m = foot_rest[s].copy()
        m.translation = fb.matrix.translation
        fb.matrix = m
        bpy.context.view_layer.update()
    bpy.context.view_layer.update()


# ---------- pose builders ----------
def pose_squat():
    reset()
    plant_legs(drop_z=0.55, back=0.02, stance=0.12, kneeout=0.08)
    pb["spine05"].rotation_euler = (TF * D(22), 0, 0)
    pb["spine04"].rotation_euler = (TF * D(8), 0, 0)
    pb["neck01"].rotation_euler = (-TF * D(20), 0, 0)
    for s in SIDES:
        pb["upperarm01.%s" % s].rotation_euler = (SHF * D(80), 0, 0)
        pb["lowerarm01.%s" % s].rotation_euler = (ELS * D(18), 0, 0)
    bpy.context.view_layer.update()
    print("SQUAT knee L=%.0f R=%.0f deg" % (knee_angle("L"), knee_angle("R")))


def pose_hinge():
    reset()
    plant_legs(drop_z=0.74, back=0.02, stance=0.11, kneeout=0.05)
    pb["root"].rotation_euler = (RS * D(42), 0, 0)   # hip hinge (legs IK-pinned)
    pb["spine05"].rotation_euler = (TF * D(10), 0, 0)
    pb["neck01"].rotation_euler = (-TF * D(34), 0, 0)
    for s in SIDES:
        pb["upperarm01.%s" % s].rotation_euler = (SHF * D(6), 0, 0)
    bpy.context.view_layer.update()
    print("HINGE knee L=%.0f R=%.0f deg" % (knee_angle("L"), knee_angle("R")))


def aim_wrist(side, target):
    ua = "upperarm01.%s" % side
    best = (H("wrist.%s" % side) - target).length
    for st in (D(12), D(4)):
        for _ in range(30):
            improved = False
            for c in (0, 1, 2):
                for d in (st, -st):
                    e = pb[ua].rotation_euler; old = e[c]
                    e[c] = old + d; bpy.context.view_layer.update()
                    s1 = (H("wrist.%s" % side) - target).length
                    if s1 < best - 1e-6:
                        best = s1; improved = True
                    else:
                        e[c] = old; bpy.context.view_layer.update()
            if not improved:
                break


def pose_grip():
    reset()
    hipz = H("upperleg01.L").z - 0.04
    for s, el in (("L", ELS), ("R", ELSR)):
        sgn = 1.0 if H("upperleg01.%s" % s).x >= 0 else -1.0
        aim_wrist(s, Vector((sgn * 0.16, fy * 0.15, hipz)))
        pb["lowerarm01.%s" % s].rotation_euler = (el * D(8), 0, 0)
    bpy.context.view_layer.update()
    cL = 0.5 * (H("wrist.L") + T("finger3-2.L"))
    cR = 0.5 * (H("wrist.R") + T("finger3-2.R"))
    bar_z = (cL.z + cR.z) / 2; bar_y = (cL.y + cR.y) / 2
    R = 0.014
    axis_pt = Vector((0, bar_y, bar_z)); axis_dir = Vector((1, 0, 0))
    bpy.ops.mesh.primitive_cylinder_add(radius=R, depth=1.4, location=axis_pt)
    bar = bpy.context.active_object; bar.name = "gripbar"
    bar.rotation_euler = Vector((1, 0, 0)).to_track_quat('Z', 'Y').to_euler()
    bm = bpy.data.materials.new("steel"); bm.use_nodes = True
    sb = bm.node_tree.nodes["Principled BSDF"]
    sb.inputs["Base Color"].default_value = (0.35, 0.36, 0.38, 1)
    sb.inputs["Metallic"].default_value = 1.0; sb.inputs["Roughness"].default_value = 0.35
    bar.data.materials.append(bm)
    L.wrap_grip(arm, "L", axis_pt, axis_dir, R)
    L.wrap_grip(arm, "R", axis_pt, axis_dir, R)
    bpy.context.view_layer.update()
    return bar


def pose_curl():
    reset()
    # L arm bicep-curl TOP. A muscular arm cannot fully close the elbow -- bicep
    # and forearm flesh collide well before 180; ~135 is a realistic hard end.
    pb["upperarm01.L"].rotation_euler = (SHF * D(26), 0, 0)
    pb["lowerarm01.L"].rotation_euler = (ELS * D(135), 0, 0)
    # R arm overhead raise -- aim the wrist straight up, elbow straight
    sgn = 1.0 if H("upperleg01.R").x >= 0 else -1.0
    hz = H("head").z + 0.32
    aim_wrist("R", Vector((sgn * 0.14, fy * 0.02, hz)))
    bpy.context.view_layer.update()


def pose_stand():
    reset()


BUILDERS = {"squat": pose_squat, "hinge": pose_hinge, "grip": pose_grip,
            "curl": pose_curl, "stand": pose_stand}

# ---------- scene ----------
scn = bpy.context.scene
L.studio(scn, view_transform='Standard', exposure=-2.2, samples=384)
deps = bpy.context.evaluated_depsgraph_get()
me = bpy.data.meshes.new_from_object(body.evaluated_get(deps))
sole_z = min((body.matrix_world @ v.co).z for v in me.vertices)
bpy.data.meshes.remove(me)
cam = L.make_cam(scn)
L.add_lights(scn, Vector((0, 0, 0.9)), fy)
floor = L.add_floor(scn, sole_z - 0.005)


def body_bounds():
    dg = bpy.context.evaluated_depsgraph_get()
    m2 = bpy.data.meshes.new_from_object(body.evaluated_get(dg))
    co = [body.matrix_world @ v.co for v in m2.vertices]
    lo = Vector((min(p.x for p in co), min(p.y for p in co), min(p.z for p in co)))
    hi = Vector((max(p.x for p in co), max(p.y for p in co), max(p.z for p in co)))
    bpy.data.meshes.remove(m2)
    return lo, hi


def crops_for(pose):
    kneeL = H("lowerleg01.L")
    hipL = H("upperleg01.L")
    elbowL = H("lowerarm01.L"); elbowR = H("lowerarm01.R")
    handL = 0.5 * (H("wrist.L") + T("finger3-2.L"))
    handR = 0.5 * (H("wrist.R") + T("finger3-2.R"))
    shR = H("shoulder01.R")
    c = []
    if pose in ("squat", "hinge"):
        c += [("knee_side", kneeL, 0.42, Vector((1.0, -fy * 0.1, 0.1))),
              ("knee_front", kneeL, 0.44, Vector((0.15, -fy, 0.05))),
              ("hip_crease", hipL, 0.42, Vector((0.5, -fy * 0.9, 0.1)))]
    if pose == "grip":
        c += [("hand_L", handL, 0.24, Vector((0.25, fy, -0.3))),
              ("hand_R", handR, 0.24, Vector((-0.25, fy, -0.3))),
              ("hand_front", handL, 0.30, Vector((0.0, fy, -0.05)))]
    if pose == "curl":
        c += [("elbow_L", elbowL, 0.34, Vector((-0.4, fy, 0.05))),
              ("hand_L", handL, 0.26, Vector((-0.3, fy, 0.0))),
              ("shoulder_R", shR, 0.42, Vector((0.3, fy, 0.15)))]
    if pose == "stand":
        c += [("knee_side", kneeL, 0.4, Vector((1.0, -fy * 0.1, 0.1))),
              ("elbow_L", elbowL, 0.34, Vector((1.0, fy * 0.2, 0.05))),
              ("torso", Vector((0, 0, 1.1)), 0.9, Vector((0.4, fy, 0.05)))]
    return c


for pose in poses:
    extra = BUILDERS[pose]()
    lo, hi = body_bounds()
    ctr = Vector((0, (lo.y + hi.y) / 2, (lo.z + hi.z) / 2))
    size = (hi - lo).length
    L.shoot(scn, cam, os.path.join(OUT, "%s_full.png" % pose), ctr, size,
            Vector((0.6, fy, 0.05)), 720, 1280)
    for nm, c0, sz, d in crops_for(pose):
        L.shoot(scn, cam, os.path.join(OUT, "%s_%s.png" % (pose, nm)), c0, sz, d, 720, 720)
    if extra is not None:
        bpy.data.objects.remove(extra, do_unlink=True)
    print("POSE_DONE", pose)

print("BATTERY_DONE poses=%s asset=%s" % (",".join(poses), ASSET))
