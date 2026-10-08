"""N6 conventional deadlift -- rebuilt on the body_rig_v5 body + STRAIGHT-ARM fix.

Supersedes the N5 build. Two owner-mandated changes over the (structurally passed)
N5 rebuild:

  1. NEW BODY. The body is no longer built inline (n4 macro + custom LBS grip).
     We LOAD assets/rig/body_rig_v5.blend -- the re-rigged asset that passed its
     acceptance battery (MPFB 'default' 163-bone skeleton, preserve-volume dual-quat
     skinning + joint-masked corrective smooth, planted-feet deform). Bone names are
     identical to N5 (MPFB default), so the mocap retarget + leg/arm IK port as-is.
     HANDS are posed with the NATIVE per-finger armature (rigv5_lib.wrap_grip) around
     the bar shaft -- NOT the old pos_of-based manual-LBS grip that blobbed the hands.

  2. STRAIGHT-ARM bar Z. N5 drove bar Z from the mocap hip fraction; the shoulders
     descended at a different rate, so the elbows absorbed the mismatch (flail). Here
     the dependency is INVERTED: per frame the bar is placed at straight-arm reach
     BELOW the shoulders,   bar_z = shoulder_z - ARM_LEN_EFF   (ARM_LEN_EFF measured
     ONCE at lockout), clamped at the floor bar height. shoulder_z is monotonic to the
     bottom, so bar_z is monotonic + smooth (no oscillation), and the arm stays rope-
     straight every frame. The hinge DEPTH is capped so at the bottom the shoulders
     sit exactly ARM_LEN_EFF above the floored bar -> straight arms reach the floor bar
     (weld holds; no arm compression). Optional exact-distance mode (N6_ZMODE=exact)
     solves bar_z for |shoulder-grip| == reach directly (guarantees straight arms even
     if the horizontal shoulder gap drifts, at the cost of possible bar_z non-monotony).

Kept verbatim from the passed N5 structure: bar object rotation LOCKED (identity every
frame -> no tilt); root lateral X locked to 0 (no drift); ankles IK-pinned, feet flat
+ symmetric; mocap hinge timing (26_10.bvh retarget); anterior-clearance bar-Y path
(pre-calibrated, frozen); 96f loop lockout->eccentric->floor->pull->lockout; static
~39deg camera; dark studio. Render matches the v5 battery: Standard view transform,
exposure tuned to avoid blown highlights, EEVEE 384 spp stills / >=64 anim.

Env:
  N6_ZMODE      const (default; bar_z=shoulder_z-eff) | exact (|sh-grip|==reach)
  N6_GRIP=0     skip the finger-wrap solve (fast probe, straight fingers)
  N6_HIPZ_BOT   hip height at bottom (default 0.60)
  N6_HIPY_BK    hip back-shift at bottom (default 0.28)
  N6_GRIPX      grip half-width (default 0.28)
  N6_ANT        bar anterior ramp at lockout (default 0.06, <=0.08)
  N6_RES        render res short side (default 720 -> 720x1280); probe use 480
  N6_SUB        subsurf render level (default 2; probe 0/1)
  N6_SAMP       still TAA samples (default 384); N6_ASAMP anim samples (default 64)
  N6_EXPO       view exposure (default -1.8, Standard)
  N6_NORENDER=1 skip the animation PNG sequence (numeric checks + stills only)
  N6_STILLS_ONLY=1 same as NORENDER for the anim, still shoots QA stills
Usage: blender --background --python build_deadlift.py
"""
import bpy, addon_utils, os, math, importlib.util
from mathutils import Vector, Matrix
from mathutils import Quaternion as _Quat

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
BVH = os.path.join(SKILL_ROOT, "scratch", "mocap", "26_10.bvh")
ASSET = os.path.join(SKILL_ROOT, "assets", "rig", "body_rig_v5.blend")
SRC_STAND, SRC_BOTTOM, SRC_END = 64, 241, 445
STEP = 4
ZMODE = os.environ.get("N6_ZMODE", "const")
DO_GRIP = os.environ.get("N6_GRIP", "1") != "0"
HIPZ_BOT = float(os.environ.get("N6_HIPZ_BOT", "0.60"))
HIPY_BK = float(os.environ.get("N6_HIPY_BK", "0.28"))
RES = int(os.environ.get("N6_RES", "720"))
SUBL = int(os.environ.get("N6_SUB", "2"))
BARR = 0.014                      # bar shaft radius (28mm grip zone)
R = BARR
SIDES = ("L", "R")

# ===================== 1 load the v5 asset =====================
addon_utils.enable('bl_ext.user_default.mpfb', default_set=True, persistent=True)
bpy.ops.wm.open_mainfile(filepath=ASSET)
body = bpy.data.objects["body_v5"]
arm = bpy.data.objects["body_v5.rig"]
shorts = bpy.data.objects["shorts"]

# native finger-wrap grip helper (drives the per-finger armature; no custom LBS)
spec = importlib.util.spec_from_file_location(
    "rigv5_lib", os.path.join(SKILL_ROOT, "scratch", "rigv5_lib.py"))
LIB = importlib.util.module_from_spec(spec); spec.loader.exec_module(LIB)

# asset deform modifiers (already baked: preserve-vol armature + masked corrective
# smooth + subsurf on the body; solidify+subsurf+armature+shrinkwrap on the shorts).
# We only toggle the heavy non-armature ones off during pose/bake, on for render.
sub = next(m for m in body.modifiers if m.type == 'SUBSURF')
sub.render_levels = SUBL
csm = next((m for m in body.modifiers if m.type == 'CORRECTIVE_SMOOTH'), None)
mask_mod = next((m for m in body.modifiers if m.type == 'MASK'), None)
ssub = next((m for m in shorts.modifiers if m.type == 'SUBSURF'), None)
if ssub: ssub.render_levels = SUBL
sol = next((m for m in shorts.modifiers if m.type == 'SOLIDIFY'), None)
swr = next((m for m in shorts.modifiers if m.type == 'SHRINKWRAP'), None)

pb = arm.pose.bones
for pbone in pb: pbone.rotation_mode = 'XYZ'
mwa = arm.matrix_world
def ppos(n, tail=False):
    bb = pb[n]; return mwa @ (bb.tail if tail else bb.head)

# ===================== 2 rest coords + leg clip structures (v5 base mesh) =====================
name2idx = {vg.name: vg.index for vg in body.vertex_groups}
idx2name = {vg.index: vg.name for vg in body.vertex_groups}
visible = None
if mask_mod and mask_mod.vertex_group:
    mg = name2idx[mask_mod.vertex_group]; inv = mask_mod.invert_vertex_group
    visible = set()
    for v in body.data.vertices:
        inn = any(g.group == mg and g.weight > 0 for g in v.groups)
        if inn != inv: visible.add(v.index)
body_mw = body.matrix_world
_mstates = [(mm, mm.show_viewport) for mm in body.modifiers]
for _mm, _s in _mstates: _mm.show_viewport = False
_deps = bpy.context.evaluated_depsgraph_get()
_rest_me = bpy.data.meshes.new_from_object(body.evaluated_get(_deps))
restco = [body_mw @ v.co for v in _rest_me.vertices]
bpy.data.meshes.remove(_rest_me)
for _mm, _s in _mstates: _mm.show_viewport = _s
arm_mw = arm.matrix_world; arm_inv = arm_mw.inverted()
bones = {bn.name for bn in arm.data.bones}
rest_inv = {bn.name: bn.matrix_local.inverted() for bn in arm.data.bones}
LEGB = set(name2idx[vg.name] for vg in body.vertex_groups
           if vg.name.startswith(("upperleg", "lowerleg")))
leg_all = [v.index for v in body.data.vertices
           if (visible is None or v.index in visible)
           and any(g.group in LEGB and g.weight > 0.6 for g in v.groups)]
leg_front_i = leg_all[::2]                      # halve the per-frame cost
skin = {}
for i in leg_front_i:
    v = body.data.vertices[i]
    ws = [(idx2name[g.group], g.weight) for g in v.groups]
    ws = [(nm, w) for nm, w in ws if nm in bones and w > 0]
    tot = sum(w for _, w in ws) or 1.0
    skin[i] = (arm_inv @ restco[i], [(nm, w/tot) for nm, w in ws])
def pos_of(i):
    rest_co, ws = skin[i]; co = Vector((0, 0, 0))
    for nm, w in ws: co += w * ((pb[nm].matrix @ rest_inv[nm]) @ rest_co)
    return arm_mw @ co
def front_leg_y(z, band=0.055, x0=0.0, x1=0.17):
    ys = [q.y for i in leg_front_i for q in (pos_of(i),)
          if abs(q.z - z) < band and x0 <= abs(q.x) < x1]
    return min(ys) if ys else None
for _m in (sub, csm, ssub, sol, swr):
    if _m: _m.show_viewport = False

faceY = 1.0 if (ppos("toe2-1.L") - ppos("foot.L")).y > 0 else -1.0
sole_z = min(q.z for q in restco)
print("N6 faceY=%+.0f sole_z=%.3f bones=%d zmode=%s" % (faceY, sole_z, len(arm.data.bones), ZMODE))

def descend(bone, score, comps=(0, 1, 2), steps=(math.radians(10), math.radians(4)), rounds=25):
    for st in steps:
        for _ in range(rounds):
            improved = False
            for c in comps:
                for d in (st, -st):
                    e = pb[bone].rotation_euler; old = e[c]; e[c] = old + d
                    bpy.context.view_layer.update()
                    if score() < descend.best - 1e-9: descend.best = score(); improved = True
                    else: e[c] = old; bpy.context.view_layer.update()
            if not improved: break

# ===================== 3 source retarget (torso) =====================
pre = set(bpy.data.objects)
bpy.ops.import_anim.bvh(filepath=BVH, axis_forward='-Z', axis_up='Y', rotate_mode='NATIVE',
                        global_scale=1.0, use_fps_scale=False, update_scene_fps=False,
                        update_scene_duration=True)
src = [o for o in bpy.data.objects if o not in pre][0]
src.rotation_euler = (0, 0, math.pi if faceY < 0 else 0.0); bpy.context.view_layer.update()
sp = src.pose.bones; src_mw = src.matrix_world
scn = bpy.context.scene
def swpos(n): return src_mw @ sp[n].matrix.translation
def src_pose3(c): return src_mw.to_3x3() @ sp[c].matrix.to_3x3()
TMAP = [("LowerBack", "spine05"), ("Spine", "spine04"), ("Spine1", "spine03"),
        ("Neck", "neck01"), ("Neck1", "neck02"), ("Head", "head")]
TORDER = [t for _, t in TMAP]; t2c = {t: c for c, t in TMAP}
Rt_rest = {t: pb[t].bone.matrix_local.to_3x3() for _, t in TMAP}
scn.frame_set(SRC_STAND)
hv = swpos("LeftUpLeg") - swpos("RightUpLeg")
yaw_err = math.atan2(hv.y, hv.x)
src.rotation_euler.z -= yaw_err
bpy.context.view_layer.update()
src_mw = src.matrix_world
print("N6 src yaw-aligned by %+.1f deg" % math.degrees(-yaw_err), flush=True)
Rs_ref_inv = {c: src_pose3(c).inverted() for c, _ in TMAP}
Rroot_rest = pb["root"].bone.matrix_local.to_3x3()
Rs_root_ref_inv = (src_mw.to_3x3() @ sp["Hips"].matrix.to_3x3()).inverted()
hipz_src_stand = swpos("Hips").z
scn.frame_set(SRC_BOTTOM)
hipz_src_bot = swpos("Hips").z

src_frames = list(range(SRC_STAND, SRC_END+1, STEP))
NF = len(src_frames)
bottom_of = round((SRC_BOTTOM - SRC_STAND)/STEP) + 1
print("N6 %d frames, bottom out-frame=%d" % (NF, bottom_of))

SPINE_K = {"spine05": 1.0, "spine04": 0.9, "spine03": 0.55,
           "neck01": 0.5, "neck02": 0.45, "head": 0.42}
def twistX(M3):
    q = M3.to_quaternion()
    t = _Quat((q.w, q.x, 0.0, 0.0))
    if t.magnitude < 1e-8: return Matrix.Identity(3)
    return t.normalized().to_matrix()
EXTRA_PITCH = 0.0   # closed-loop depth cap (scaled by u)
def apply_torso(sf):
    scn.frame_set(sf)
    u = max(0.0, min(1.0, (hipz_src_stand - swpos("Hips").z)/(hipz_src_stand - hipz_src_bot)))
    Mx = Matrix.Rotation(EXTRA_PITCH * u, 3, 'X')
    Droot = Mx @ twistX(src_pose3("Hips") @ Rs_root_ref_inv)
    hz = (1-u)*0.957 + u*HIPZ_BOT
    hy = math.sqrt(u)*HIPY_BK*(-faceY)
    des_r = (Droot @ Rroot_rest).to_quaternion().to_matrix().to_4x4()
    des_r.translation = Vector((0, 0.062 + hy, hz))   # X LOCKED to 0 (no lateral slide)
    pb["root"].rotation_mode = 'QUATERNION'
    pb["root"].matrix = des_r
    bpy.context.view_layer.update()
    for t in TORDER:
        c = t2c[t]
        D3 = Mx @ twistX(src_pose3(c) @ Rs_ref_inv[c])
        mocap_q = (D3 @ Rt_rest[t]).to_quaternion()
        rest_q = Rt_rest[t].to_quaternion()
        k = SPINE_K.get(t, 1.0)
        des = rest_q.slerp(mocap_q, (1 - u) * 1.0 + u * k)
        pbn = pb[t]; pbn.rotation_mode = 'QUATERNION'
        loc = pbn.matrix.translation.copy()
        nm2 = des.to_matrix().to_4x4(); nm2.translation = loc
        pbn.matrix = nm2; bpy.context.view_layer.update()
    return u

# ===================== 4 leg IK (feet planted) =====================
apply_torso(SRC_STAND)
STANCE_X = 0.15
feetT = {}; toesT = {}
for sd in SIDES:
    a0 = ppos("foot.%s" % sd); sgn = 1.0 if a0.x >= 0 else -1.0
    feetT[sd] = Vector((sgn*STANCE_X, a0.y, ppos("foot.%s" % sd).z))
    toesT[sd] = ppos("toe2-1.%s" % sd).copy()
def mkempty(name, loc):
    e = bpy.data.objects.new(name, None); bpy.context.scene.collection.objects.link(e); e.location = loc; return e
cons = {}
for sd in SIDES:
    ankle = mkempty("ankT.%s" % sd, feetT[sd])
    knee0 = ppos("lowerleg01.%s" % sd).copy(); sgn = 1.0 if knee0.x >= 0 else -1.0
    pole = mkempty("polT.%s" % sd, Vector((knee0.x + sgn*0.06, knee0.y + faceY*0.8, knee0.z)))
    con = pb["lowerleg02.%s" % sd].constraints.new('IK')
    con.target = ankle; con.pole_target = pole; con.chain_count = 4
    cons[sd] = con
    best_pa = None
    for pa in range(-180, 180, 10):
        con.pole_angle = math.radians(pa); bpy.context.view_layer.update()
        dev = (ppos("lowerleg01.%s" % sd) - knee0).length
        if best_pa is None or dev < best_pa[0]: best_pa = (dev, pa)
    con.pole_angle = math.radians(best_pa[1]); bpy.context.view_layer.update()
KNEE_X_TGT = float(os.environ.get("N6_KNEEX", "0.18"))
apply_torso(SRC_BOTTOM)
for sd in SIDES:
    sgn = 1.0 if feetT[sd].x >= 0 else -1.0
    best = None
    for pa in range(-180, 180, 2):
        cons[sd].pole_angle = math.radians(pa)
        bpy.context.view_layer.update()
        k = ppos("lowerleg01.%s" % sd)
        cost = abs(k.x - sgn*KNEE_X_TGT) + 1.0*max(0.0, -faceY*(k.y - feetT[sd].y))
        if best is None or cost < best[0]: best = (cost, pa, k.copy())
    cons[sd].pole_angle = math.radians(best[1])
    bpy.context.view_layer.update()
    print("N6 %s deep pole=%d knee=%s" % (sd, best[1], tuple(round(v, 3) for v in best[2])), flush=True)
kL = ppos("lowerleg01.L"); kR = ppos("lowerleg01.R")
print("N6 knee mirror asym=%.3f m" % (abs(kR.x + kL.x) + abs(kR.y - kL.y) + abs(kR.z - kL.z)), flush=True)
FOOT_REST3 = {sd: pb["foot.%s" % sd].bone.matrix_local.to_3x3() for sd in SIDES}
def level_feet():
    for sd in SIDES:
        pbn = pb["foot.%s" % sd]; loc = pbn.matrix.translation.copy()
        nm2 = FOOT_REST3[sd].to_4x4(); nm2.translation = loc
        pbn.matrix = nm2
    bpy.context.view_layer.update()

# ===================== 5 bar path geometry constants =====================
BAR_FLOOR_Z = sole_z + 0.225                  # bar axis 225mm off floor (plate rests on floor)
GRIPX = float(os.environ.get("N6_GRIPX", "0.28"))
BAR_ANT = float(os.environ.get("N6_ANT", "0.06"))
BAR_ANT_MID = float(os.environ.get("N6_ANT_MID", "0.055"))
BAR_TY = (feetT["L"].y + toesT["L"].y + feetT["R"].y + toesT["R"].y)/4 + faceY*0.02  # midfoot
ARMREACH = sum(pb["%s.L" % b].bone.length for b in
               ("upperarm01", "upperarm02", "lowerarm01", "lowerarm02"))

# ===================== 6 reference grip solve (ONCE, standing, native finger wrap) =====================
# Hang each arm near-vertical via IK (wrist above where the bar will sit), pronate the
# wrist to a double-overhand orientation, define the bar center in the grip, then curl
# fingers 2..5 + thumb around the shaft with the NATIVE per-finger armature (wrap_grip).
# Capture: the finger euler angles (rigid fist, re-keyed constant), the wrist->bar_center
# offset, and the pronated wrist world orientation. Reused at every bar height.
def pronate_wrist(side):
    wr = "wrist.%s" % side
    xhat = Vector((1, 0, 0)); rear = Vector((0, -faceY, 0))
    def _kl_ds():
        kl = (ppos("finger5-1.%s" % side) - ppos("finger2-1.%s" % side)).normalized()
        ds = (ppos("finger3-2.%s" % side) - ppos("finger3-1.%s" % side)).normalized()
        ds = (ds - kl*ds.dot(kl)).normalized(); return kl, ds
    tip0 = ppos("finger3-3.%s" % side, tail=True)
    pb["finger3-2.%s" % side].rotation_euler = (math.radians(40), 0, 0); bpy.context.view_layer.update()
    pdir0 = (ppos("finger3-3.%s" % side, tail=True) - tip0).normalized()
    pb["finger3-2.%s" % side].rotation_euler = (0, 0, 0); bpy.context.view_layer.update()
    kl0, ds0 = _kl_ds(); chir = 1.0 if kl0.cross(ds0).dot(pdir0) >= 0 else -1.0
    def wcost():
        kl, ds = _kl_ds(); n = kl.cross(ds)*chir
        return (1-abs(kl.dot(xhat)))*2.0 + (1-n.dot(rear))
    descend.best = wcost(); descend(wr, wcost, steps=(math.radians(8), math.radians(3)), rounds=16)

apply_torso(SRC_STAND); level_feet()
SH_LOCK_Z = 0.5*(ppos("upperarm01.L").z + ppos("upperarm01.R").z)
_tmp_ik = []
for side in SIDES:
    sh = ppos("upperarm01.%s" % side); sgn = 1.0 if sh.x >= 0 else -1.0
    # hang the wrist joint at a STRAIGHT-arm distance (0.997*ARMREACH) from the
    # shoulder, at grip x / midfoot y -> the reference arm is truly straight, so the
    # captured grip reach == arm chain and the animated elbow starts from 180.
    gx = sgn*GRIPX; gy = BAR_TY
    dx = gx - sh.x; dy = gy - sh.y
    vert = math.sqrt(max((0.997*ARMREACH)**2 - dx*dx - dy*dy, 0.01))
    hangpt = Vector((gx, gy, sh.z - vert))
    tge = mkempty("tmpG.%s" % side, hangpt)
    tpe = mkempty("tmpP.%s" % side, Vector((sh.x + sgn*0.30, sh.y + faceY*0.20, sh.z - 0.12)))
    con = pb["lowerarm02.%s" % side].constraints.new('IK')
    con.target = tge; con.pole_target = tpe; con.chain_count = 4
    ref_el = Vector((sh.x + sgn*0.05, sh.y, sh.z - 0.20))
    best = None
    for pa in range(-180, 180, 10):
        con.pole_angle = math.radians(pa); bpy.context.view_layer.update()
        dev = (ppos("lowerarm01.%s" % side) - ref_el).length
        if best is None or dev < best[0]: best = (dev, pa)
    con.pole_angle = math.radians(best[1]); bpy.context.view_layer.update()
    pronate_wrist(side)
    _tmp_ik.append((side, con))
bpy.context.view_layer.update()

# grip center per side = midpoint(wrist head, middle-finger mid-joint tail) -- where a
# held bar sits in the curled hand (same anchor the v5 battery grip used).
gc_side = {}
for side in SIDES:
    gc_side[side] = 0.5*(ppos("wrist.%s" % side) + ppos("finger3-2.%s" % side, tail=True))
BAR_Y = 0.5*(gc_side["L"].y + gc_side["R"].y)
BAR_Z = 0.5*(gc_side["L"].z + gc_side["R"].z)
BAR_LOCK_Z = BAR_Z
ARM_LEN_EFF = SH_LOCK_Z - BAR_LOCK_Z          # constant straight-arm vertical drop
print("N6 ref grip: BAR_Y=%.3f lockout BAR_Z=%.3f shoulder_z=%.3f -> ARM_LEN_EFF=%.3f"
      % (BAR_Y, BAR_LOCK_Z, SH_LOCK_Z, ARM_LEN_EFF), flush=True)

# curl the fingers around the bar shaft with the native armature
FINGER_ANG = {"L": {}, "R": {}}
if DO_GRIP:
    for side in SIDES:
        LIB.wrap_grip(arm, side, Vector((gc_side[side].x, BAR_Y, BAR_Z)),
                      Vector((1, 0, 0)), R, flesh=0.010)
        for fi in (1, 2, 3, 4, 5):
            for sg in (1, 2, 3):
                bn = "finger%d-%d.%s" % (fi, sg, side)
                FINGER_ANG[side][(fi, sg)] = tuple(pb[bn].rotation_euler)
        print("N6 %s grip wrapped (native fingers)" % side, flush=True)
def set_fingers():
    for side in SIDES:
        for (fi, sg), e in FINGER_ANG[side].items():
            pb["finger%d-%d.%s" % (fi, sg, side)].rotation_euler = e
set_fingers(); bpy.context.view_layer.update()

# capture the rigid fist: wrist-joint OFFSET from the (symmetric) bar center + pronated
# wrist world orientation. Offset is pure hand geometry -> valid at every bar height.
GRIP = {}
for side in SIDES:
    Mw = mwa @ pb["wrist.%s" % side].matrix
    cx = gc_side[side].x
    FIST_OFF = Mw.translation - Vector((cx, BAR_Y, BAR_Z))
    GRIP[side] = (FIST_OFF.copy(), Mw.to_quaternion(), cx)
    print("N6 %s fist offset from bar center=%s" % (side, tuple(round(x, 3) for x in FIST_OFF)), flush=True)
for side, con in _tmp_ik:
    pb["lowerarm02.%s" % side].constraints.remove(con)

# ===================== 7 build bar (rotation identity -> never tilts) =====================
BAR_Y_BOT, BAR_Z_BOT = BAR_TY, BAR_FLOOR_Z     # bottom = floor over midfoot
def build_bar():
    bpy.ops.mesh.primitive_cylinder_add(radius=R, depth=2.2, location=(0, 0, 0), vertices=32)
    bar = bpy.context.active_object; bar.name = "barbell"
    bar.rotation_euler = Vector((1, 0, 0)).to_track_quat('Z', 'Y').to_euler()
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    bm2 = bpy.data.materials.new("steel"); bm2.use_nodes = True
    sb = bm2.node_tree.nodes["Principled BSDF"]
    sb.inputs["Base Color"].default_value = (0.35, 0.36, 0.38, 1); sb.inputs["Metallic"].default_value = 1.0
    sb.inputs["Roughness"].default_value = 0.35; bar.data.materials.append(bm2)
    SLEEVE_R = 0.025; PLATE_R = 0.225; PLATE_T = 0.055; COLLAR_X = 0.60
    smat = bpy.data.materials.new("sleeve"); smat.use_nodes = True
    smat.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value = (0.30, 0.31, 0.33, 1)
    smat.node_tree.nodes["Principled BSDF"].inputs["Metallic"].default_value = 1.0
    pmat = bpy.data.materials.new("plate"); pmat.use_nodes = True
    pB = pmat.node_tree.nodes["Principled BSDF"]
    pB.inputs["Base Color"].default_value = (0.05, 0.05, 0.055, 1); pB.inputs["Roughness"].default_value = 0.55
    kids = []
    for sx in (1, -1):
        bpy.ops.mesh.primitive_cylinder_add(radius=SLEEVE_R, depth=0.30, location=(sx*(COLLAR_X+0.15), 0, 0), vertices=24)
        sl = bpy.context.active_object; sl.name = "sleeve.%d" % sx
        sl.rotation_euler = Vector((1, 0, 0)).to_track_quat('Z', 'Y').to_euler(); sl.data.materials.append(smat); kids.append(sl)
        for k in range(2):
            bpy.ops.mesh.primitive_cylinder_add(radius=PLATE_R, depth=PLATE_T,
                location=(sx*(COLLAR_X + PLATE_T*0.5 + k*PLATE_T), 0, 0), vertices=48)
            pl = bpy.context.active_object; pl.name = "plate.%d.%d" % (sx, k)
            pl.rotation_euler = Vector((1, 0, 0)).to_track_quat('Z', 'Y').to_euler(); pl.data.materials.append(pmat); kids.append(pl)
    bar.location = (0.0, BAR_Y_BOT, BAR_Z_BOT); bpy.context.view_layer.update()
    for k in kids:
        k.location = (k.location.x, BAR_Y_BOT, BAR_Z_BOT)
        k.parent = bar; k.matrix_parent_inverse = bar.matrix_world.inverted()
    return bar
bar = build_bar()
bpy.context.view_layer.update()

# ===================== 8 grip empties (welded to bar) + arm IK + wrist copy-rot =====================
grip_empty = {}
for side in SIDES:
    FIST_OFF, Rw, cx = GRIP[side]
    wj = Vector((cx, BAR_Y_BOT, BAR_Z_BOT)) + FIST_OFF
    e = bpy.data.objects.new("gripT.%s" % side, None)
    bpy.context.scene.collection.objects.link(e); e.empty_display_size = 0.05
    M = Rw.to_matrix().to_4x4(); M.translation = wj
    e.matrix_world = M
    e.parent = bar; e.matrix_parent_inverse = bar.matrix_world.inverted()
    grip_empty[side] = e
bpy.context.view_layer.update()

arm_ik = {}
for side in SIDES:
    sh = ppos("upperarm01.%s" % side); el = ppos("lowerarm01.%s" % side)
    sgn = 1.0 if sh.x >= 0 else -1.0
    pole = mkempty("armPol.%s" % side, Vector((el.x + sgn*0.30, el.y + faceY*0.20, el.z + 0.02)))
    con = pb["lowerarm02.%s" % side].constraints.new('IK')
    con.target = grip_empty[side]; con.pole_target = pole; con.chain_count = 4
    arm_ik[side] = (con, pole, el.copy())
for side in SIDES:
    for bn in ("upperarm01", "upperarm02", "lowerarm01", "lowerarm02"):
        pb["%s.%s" % (bn, side)].rotation_euler = (0, 0, 0)
bpy.context.view_layer.update()
for side in SIDES:
    con, pole, el_ref = arm_ik[side]
    best = None
    for pa in range(-180, 180, 10):
        con.pole_angle = math.radians(pa); bpy.context.view_layer.update()
        dev = (ppos("lowerarm01.%s" % side) - el_ref).length
        if best is None or dev < best[0]: best = (dev, pa)
    con.pole_angle = math.radians(best[1]); bpy.context.view_layer.update()
    print("N6 %s arm IK pole=%d (elbow dev %.3f)" % (side, best[1], best[0]), flush=True)
for side in SIDES:
    wc = pb["wrist.%s" % side].constraints.new('COPY_ROTATION')
    wc.target = grip_empty[side]; wc.mix_mode = 'REPLACE'
    wc.owner_space = 'WORLD'; wc.target_space = 'WORLD'
bpy.context.view_layer.update()

def emp_pos(side):
    return grip_empty[side].matrix_world.translation.copy()

# ===================== 9 straight-arm bar Z + depth cap =====================
# bar_z tracks the shoulders (const-offset, default) or solves |shoulder-grip|==reach
# (exact). Both clamp at the floor. apply_torso(sf) MUST be called first.
FIST_OFF_Z = 0.5*(GRIP["L"][0].z + GRIP["R"][0].z)
GRIP_REACH = None   # set below after we know a straight-arm distance
def shoulder_z_now():
    return 0.5*(ppos("upperarm01.L").z + ppos("upperarm01.R").z)
def bar_nom_y(u):
    return BAR_TY + faceY*(BAR_ANT*(1.0-u) + BAR_ANT_MID*math.sin(math.pi*u))
def bar_z_raw(u):
    # UNCLAMPED straight-arm bar height (apply_torso(sf) already applied).
    #  const: bar hangs a fixed vertical drop below the shoulders (guaranteed
    #         monotonic with shoulder_z, but the arm bends as the horizontal
    #         shoulder->grip offset drifts through the hinge).
    #  exact: bar_z solved so mean |shoulder - grip| == straight-arm reach ->
    #         arms stay rope-straight every frame (the owner-mandated result).
    if ZMODE != "exact":
        return shoulder_z_now() - ARM_LEN_EFF
    by = bar_nom_y(u); z = 0.0; n = 0
    for sd in SIDES:
        sh = ppos("upperarm01.%s" % sd); FIST_OFF, _Rw, cx = GRIP[sd]
        gx = cx + FIST_OFF.x; gy = by + FIST_OFF.y
        dx = sh.x - gx; dy = sh.y - gy
        rad2 = GRIP_REACH*GRIP_REACH - dx*dx - dy*dy
        if rad2 < 1e-6: rad2 = 1e-6
        z += sh.z - FIST_OFF.z - math.sqrt(rad2); n += 1
    return z/n
def bar_z_for(u):
    return max(bar_z_raw(u), BAR_FLOOR_Z)

# measure the straight-arm shoulder->grip reach at lockout (for exact mode + reporting)
apply_torso(SRC_STAND); level_feet()
bar.location = (0.0, BAR_Y, BAR_LOCK_Z); bpy.context.view_layer.update()
GRIP_REACH = 0.5*sum((ppos("upperarm01.%s" % sd) - emp_pos(sd)).length for sd in SIDES)
print("N6 straight-arm reach (shoulder->grip at lockout)=%.4f  ARMREACH=%.4f" % (GRIP_REACH, ARMREACH), flush=True)

# DEPTH CAP: cap the hinge so the LOWEST *unclamped* straight-arm bar height over the
# WHOLE rep equals the floor bar height -> the bar just kisses the floor at the deepest
# frame and never gets clamped BELOW straight-arm reach anywhere else. Without this, the
# mocap's bottom dwell drives the straight-arm bar below the floor for a run of frames;
# clamping there forces the arms to bend (the N5 flail). Mode-aware via bar_z_raw.
# Fast: find the argmin frame once, Newton on it, re-find, one correction if it moved.
def scan_min_barz():
    m = 1e9; mf = 0
    for of2, sf in enumerate(src_frames, 1):
        u = apply_torso(sf)
        z = bar_z_raw(u)
        if z < m: m = z; mf = of2
    return m, mf
def barz_raw_at(sf):
    u = apply_torso(sf); level_feet()
    return bar_z_raw(u)
_, _mf = scan_min_barz()
for _pass in range(3):
    DEEP_SF = src_frames[_mf-1]
    for _it in range(12):
        z0 = barz_raw_at(DEEP_SF); err = z0 - BAR_FLOOR_Z
        if abs(err) < 0.002: break
        _d = 0.05; EXTRA_PITCH += _d; z1 = barz_raw_at(DEEP_SF); EXTRA_PITCH -= _d
        grad = (z1 - z0)/_d
        if abs(grad) < 1e-4: break
        EXTRA_PITCH -= max(min(err/grad, 0.4), -0.4)
    _mz, _mf2 = scan_min_barz()
    print("N6 depth cap pass%d EXTRA_PITCH=%+.1f min_barz_raw=%.3f@f%d (deep f%d)" % (
        _pass, math.degrees(EXTRA_PITCH), _mz, _mf2, DEEP_SF), flush=True)
    if _mf2 == _mf: break
    _mf = _mf2
print("N6 depth cap final EXTRA_PITCH=%+.1f deg" % math.degrees(EXTRA_PITCH), flush=True)

# ===================== 10 bar path Y calibration (anterior leg clearance; frozen) =====================
SHAFT_PAD = R + 0.008
FIST_PAD = 0.030
u_list = []; z_list = []; y_req = []
for sf in src_frames:
    u = apply_torso(sf); level_feet()
    bz = bar_z_for(u)
    y_nom = bar_nom_y(u)
    fl_shaft = front_leg_y(bz, band=0.055, x0=0.0, x1=0.34)
    fl_fist = front_leg_y(bz, band=0.055, x0=GRIPX-0.06, x1=GRIPX+0.07)
    ys = [y_nom]
    if fl_shaft is not None: ys.append(fl_shaft - SHAFT_PAD)
    if fl_fist is not None: ys.append(fl_fist - FIST_PAD)
    u_list.append(u); z_list.append(bz); y_req.append(min(ys))
def _smooth(vals, w):
    n = len(vals); out = []
    for i in range(n):
        a = max(0, i-w); b = min(n, i+w+1)
        out.append(sum(vals[a:b])/(b-a))
    return out
def _pava(y, inc=True):
    # isotonic regression (pool-adjacent-violators): least-squares monotone fit.
    # inc=True -> non-decreasing, inc=False -> non-increasing. Minimal deviation
    # from y, so forcing the bar path monotone costs the least arm-straightness.
    lvl = []
    for yi in y:
        lvl.append([float(yi), 1.0])
        while len(lvl) >= 2 and ((lvl[-2][0] > lvl[-1][0]) if inc else (lvl[-2][0] < lvl[-1][0])):
            a = lvl.pop(); b = lvl.pop()
            lvl.append([(a[0]*a[1] + b[0]*b[1])/(a[1]+b[1]), a[1]+b[1]])
    out = []
    for m, w in lvl: out += [m]*int(round(w))
    return out[:len(y)]
YPATH = list(y_req)
for w in (4, 2, 1):
    YPATH = _smooth(YPATH, w)
    YPATH = [min(s, r) for s, r in zip(YPATH, y_req)]
print("N6 bar path calibrated: y %.3f..%.3f (midfoot %.3f, max anterior %.3f)"
      % (min(YPATH), max(YPATH), BAR_TY, max(abs(y - BAR_TY) for y in YPATH)), flush=True)
# bar Z path: the per-frame straight-arm z, lightly de-noised then made a strict
# monotone VALLEY (descend to floor, ascend) via isotonic regression on each side --
# the least-squares monotone fit, so the single-turnaround guarantee costs the least
# possible arm-straightness. Floor contact pinned at the deepest frame.
_z0 = _smooth(list(z_list), 1)
_mi = min(range(NF), key=lambda i: _z0[i])
_desc = _pava(_z0[:_mi+1], inc=False)          # non-increasing to the bottom
_asc = _pava(_z0[_mi:], inc=True)              # non-decreasing back up
BZPATH = _desc[:-1] + _asc
BZPATH = [max(z, BAR_FLOOR_Z) for z in BZPATH]
_mi = min(range(NF), key=lambda i: BZPATH[i])
BZPATH[_mi] = BAR_FLOOR_Z
print("N6 bar Z path: %.3f..%.3f valley@f%d (straight-arm z, isotonic monotone)"
      % (min(BZPATH), max(BZPATH), _mi+1), flush=True)

# ===================== 11 keyframe bake =====================
DR = ["root", "spine05", "spine04", "spine03", "neck01", "neck02", "head",
      "upperleg01.L", "upperleg02.L", "lowerleg01.L", "lowerleg02.L", "foot.L",
      "upperleg01.R", "upperleg02.R", "lowerleg01.R", "lowerleg02.R", "foot.R"]
FINGERS = [bn for bn in bones if bn.startswith("finger")]
QUATB = set(["root"] + TORDER)
for bn in DR + FINGERS:
    pb[bn].rotation_mode = 'QUATERNION' if bn in QUATB else 'XYZ'

scn.frame_start = 1; scn.frame_end = NF
bpy.context.preferences.edit.keyframe_new_interpolation_type = 'BEZIER'
bar_track = []
import time as _time; _t0 = _time.time()
set_fingers()
for of, sf in enumerate(src_frames, 1):
    if of % 16 == 1: print("N6 bake frame %d/%d (%.0fs)" % (of, NF, _time.time()-_t0), flush=True)
    u = apply_torso(sf); level_feet()
    bz = BZPATH[of-1]                         # smoothed monotone straight-arm Z
    by = YPATH[of-1]
    bar.location = (0.0, by, bz)
    set_fingers()
    bpy.context.view_layer.update()          # empties follow bar; arm IK + wrist copyrot re-solve
    bar_track.append((of, by, bz))
    for bn in DR:
        pb[bn].keyframe_insert("rotation_quaternion" if bn in QUATB else "rotation_euler", frame=of)
    pb["root"].keyframe_insert("location", frame=of)
    for bn in FINGERS: pb[bn].keyframe_insert("rotation_euler", frame=of)
    bar.keyframe_insert("location", frame=of)   # ONLY location; rotation stays identity
print("N6 baked in %.0fs. bar z %.3f..%.3f" % (_time.time()-_t0,
      min(z for _, _, z in bar_track), max(z for _, _, z in bar_track)), flush=True)
# the visual bottom of the rep = the deepest bar frame (bar on the floor), which the
# min-barz depth cap places just after the mocap hip-bottom -- use it for the bottom
# still + the bottom-geometry analysis (leg IK already used SRC_BOTTOM for knee tracking).
bottom_of = min(range(1, NF+1), key=lambda of: bar_track[of-1][2])
print("N6 deepest-bar (visual bottom) out-frame=%d" % bottom_of, flush=True)

# ===================== 12 numeric checks (fcurve replay = what renders) =====================
def ang(a, b):
    return math.degrees(a.angle(b))
ankz_L = []; ankz_R = []; bary = []; barrot = []; rootx = []
ankdev = {"L": [], "R": []}; fistrad = {"L": [], "R": []}
ikerr = {"L": [], "R": []}; elbow = {"L": [], "R": []}
kneeasym = []; sh_ahead = []; shaftclr = []; fistclr = []; barz = []
FIST_RAD = 0.050
SHAFTCLR_NEED = R + 0.004
for of in range(1, NF+1):
    scn.frame_set(of)
    ankz_L.append(ppos("foot.L").z); ankz_R.append(ppos("foot.R").z)
    _, _by, _bz = bar_track[of-1]
    bary.append(_by); barz.append(_bz)
    _shaft = (bar.matrix_world.to_3x3() @ Vector((1, 0, 0))).normalized()
    barrot.append(abs(math.degrees(math.asin(max(-1.0, min(1.0, _shaft.z))))))
    rootx.append((mwa @ pb["root"].matrix.translation).x)
    for sd in SIDES:
        ankdev[sd].append((ppos("foot.%s" % sd) - feetT[sd]).length)
        knu = ppos("finger3-1.%s" % sd)
        fistrad[sd].append(math.hypot(knu.y - _by, knu.z - _bz))
        ep = emp_pos(sd)
        ikerr[sd].append((ppos("wrist.%s" % sd) - ep).length)
        # true elbow flexion = angle at the elbow joint (shoulder->elbow, elbow->wrist)
        upper = ppos("lowerarm01.%s" % sd) - ppos("upperarm01.%s" % sd)
        fore = ppos("wrist.%s" % sd) - ppos("lowerarm01.%s" % sd)
        elbow[sd].append(180 - ang(upper, fore))
    shy = (ppos("upperarm01.L").y + ppos("upperarm01.R").y)/2
    sh_ahead.append(faceY*(shy - _by))
    _kL = ppos("lowerleg01.L"); _kR = ppos("lowerleg01.R")
    kneeasym.append(abs(_kR.x + _kL.x) + abs(_kR.y - _kL.y) + abs(_kR.z - _kL.z))
    _minax = 9.9; _minfist = 9.9; _wax = None; _wfi = None
    for i in leg_front_i:
        q = pos_of(i)
        if abs(q.x) < 0.60:
            _d = math.hypot(q.y - _by, q.z - _bz)
            if _d < _minax: _minax = _d; _wax = q.copy()
        for gx in (GRIPX, -GRIPX):
            _df = (q - Vector((gx, _by, _bz))).length
            if _df < _minfist: _minfist = _df; _wfi = q.copy()
    shaftclr.append((of, _minax, _wax))
    fistclr.append((of, _minfist, _wfi))
# bar_z monotonicity: sign changes of the per-frame delta (want exactly 1, at turnaround)
dz = [barz[i+1]-barz[i] for i in range(len(barz)-1)]
sign_changes = 0; prev = 0
_turn = min(range(len(barz)), key=lambda i: barz[i])   # the valley (real turnaround)
max_rev = 0.0
for i, d in enumerate(dz):
    s = 1 if d > 1e-5 else (-1 if d < -1e-5 else 0)
    if s != 0:
        if prev != 0 and s != prev: sign_changes += 1
        prev = s
    # a "reversal" = a delta pointing the wrong way for its side of the valley
    wrong = (d > 0 and i < _turn) or (d < 0 and i >= _turn)
    if wrong: max_rev = max(max_rev, abs(d))
min_elbow = min(min(elbow["L"]), min(elbow["R"]))
elbow_bot = min(elbow["L"][bottom_of-1], elbow["R"][bottom_of-1])
# DEBUG: locate the worst-elbow frame + its geometry
_wf_el = min(range(NF), key=lambda i: min(elbow["L"][i], elbow["R"][i]))
scn.frame_set(_wf_el+1)
_shL = ppos("upperarm01.L"); _epL = emp_pos("L")
print("N6 DBG worst-elbow f%d elbowL=%.1f elbowR=%.1f bar_z=%.3f bar_y=%.3f | shL=(%.3f,%.3f,%.3f) gripL=(%.3f,%.3f,%.3f) |sh-grip|=%.4f reach=%.4f weldL=%.4f" % (
    _wf_el+1, elbow["L"][_wf_el], elbow["R"][_wf_el], barz[_wf_el], bary[_wf_el],
    _shL.x, _shL.y, _shL.z, _epL.x, _epL.y, _epL.z, (_shL-_epL).length, ARMREACH, ikerr["L"][_wf_el]), flush=True)
print("N6 DBG elbowL by frame:", " ".join("%.0f" % e for e in elbow["L"]), flush=True)
scn.frame_set(bottom_of)
up = Vector((0, 0, 1))
thigh = ppos("lowerleg01.L") - ppos("upperleg01.L")
shin = ppos("foot.L") - ppos("lowerleg01.L")
torso = ppos("neck01") - ppos("root")
knee_ang = ang(thigh, shin); hip_ang = ang(thigh, torso)
torso_from_horiz = 90 - ang(torso, up); shin_from_vert = 180 - ang(shin, up)
bot_by, bot_bz = bar_track[bottom_of-1][1], bar_track[bottom_of-1][2]
plate = next(o for o in bpy.data.objects if o.name.startswith("plate."))
pd = plate.evaluated_get(bpy.context.evaluated_depsgraph_get())
plate_bot_z = min((plate.matrix_world @ v.co).z for v in pd.data.vertices)
scn.frame_set(NF)
_ue = ppos("lowerarm01.L") - ppos("upperarm01.L")
_fe = ppos("wrist.L") - ppos("lowerarm01.L")
elbow_lockout = 180 - ang(_ue, _fe)
plate_axis = (plate.matrix_world.to_3x3() @ Vector((0, 0, 1))).normalized()
bar_axis = (bar.matrix_world.to_3x3() @ Vector((1, 0, 0))).normalized()
plate_coax = ang(plate_axis, bar_axis)
print("N6 CHECKS:", flush=True)
print("  *** ELBOW *** min over ALL frames=%.1f deg (L min=%.1f R min=%.1f) at-bottom=%.1f lockout=%.1f (>=~168 = straight)" % (
    min_elbow, min(elbow["L"]), min(elbow["R"]), elbow_bot, elbow_lockout), flush=True)
print("  *** BARZ *** range=%.3f..%.3f delta sign-changes=%d max-reversal=%.5fm (want 1 change, ~0 reversal)" % (
    min(barz), max(barz), sign_changes, max_rev), flush=True)
print("  *** WELD *** IK reach err (wrist->grip empty): L max=%.5f  R max=%.5f (0=hand ON bar)" % (
    max(ikerr["L"]), max(ikerr["R"])), flush=True)
print("  fist->bar radial (knuckle): L %.3f..%.3f  R %.3f..%.3f (const=welded)" % (
    min(fistrad["L"]), max(fistrad["L"]), min(fistrad["R"]), max(fistrad["R"])), flush=True)
print("  *** TILT *** bar axis vs horizontal: max=%.4f deg (0=horizontal)" % max(barrot), flush=True)
print("  *** DRIFT *** root world-X: range=%.5f (%.5f..%.5f)" % (
    max(rootx)-min(rootx), min(rootx), max(rootx)), flush=True)
print("  ankle z L range=%.4f  R range=%.4f  3D dev from pinned L max=%.4f R max=%.4f" % (
    max(ankz_L)-min(ankz_L), max(ankz_R)-min(ankz_R), max(ankdev["L"]), max(ankdev["R"])), flush=True)
print("  bar y range=%.4f  shoulders-ahead-of-bar min=%.3f at-bottom=%.3f" % (
    max(bary)-min(bary), min(sh_ahead), sh_ahead[bottom_of-1]), flush=True)
_ws = min(shaftclr, key=lambda t: t[1]); _wf = min(fistclr, key=lambda t: t[1])
print("  *** CLIP *** leg-skin dist to bar AXIS min=%.3f at f%d (need >=%.3f)" % (
    _ws[1], _ws[0], SHAFTCLR_NEED), flush=True)
print("  *** CLIP *** leg-skin dist to GRIP CENTER min=%.3f at f%d (need >=%.3f)" % (
    _wf[1], _wf[0], FIST_RAD), flush=True)
print("  knee mirror asym max=%.4f m" % max(kneeasym), flush=True)
print("  bottom: knee=%.0f hip=%.0f torso_from_horiz=%.0f shin_from_vert=%.0f" % (
    knee_ang, hip_ang, torso_from_horiz, shin_from_vert), flush=True)
print("  bottom clip: plate_bottom_z=%.4f (floor=%.4f gap=%.4f)  bar_z=%.3f" % (
    plate_bot_z, sole_z, plate_bot_z - sole_z, bot_bz), flush=True)
print("  plate/bar coaxial=%.1f deg (0=coaxial)" % plate_coax, flush=True)
scn.frame_set(1)

# ===================== 13 scene + render (v5-battery look: Standard, dark studio) =====================
for _m in (sub, csm, ssub, sol, swr):
    if _m: _m.show_viewport = True
bpy.data.objects.remove(src, do_unlink=True)
bpy.ops.mesh.primitive_plane_add(size=14, location=(0, 0, sole_z))
floor = bpy.context.active_object
fmat = bpy.data.materials.new("floor"); fmat.use_nodes = True
fB = fmat.node_tree.nodes["Principled BSDF"]
fB.inputs["Base Color"].default_value = (0.055, 0.055, 0.06, 1); fB.inputs["Roughness"].default_value = 0.95
floor.data.materials.append(fmat)
try: scn.render.engine = 'BLENDER_EEVEE'
except TypeError: scn.render.engine = 'BLENDER_EEVEE_NEXT'
STILL_SAMP = int(os.environ.get("N6_SAMP", "384"))
ANIM_SAMP = int(os.environ.get("N6_ASAMP", "64"))
try: scn.eevee.taa_render_samples = ANIM_SAMP
except Exception: pass
for _attr in ("use_shadow_jitter", "use_raytracing", "use_taa_reprojection"):
    try: setattr(scn.eevee, _attr, True)
    except Exception: pass
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
scn.render.resolution_x = RES; scn.render.resolution_y = int(RES*16/9)
scn.render.fps = 30
# v5-battery grade: Standard view transform, exposure tuned so the key doesn't blow out
scn.view_settings.exposure = float(os.environ.get("N6_EXPO", "-1.8"))
try:
    scn.view_settings.view_transform = 'Standard'; scn.view_settings.look = 'None'
except TypeError: pass
world = bpy.data.worlds.new("W"); scn.world = world; world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.035, 0.035, 0.04, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.35
body_c = Vector((0, 0, 0.95)); low_c = Vector((0, 0, 0.50))
# energies trimmed vs the N5 AgX rig so Standard (no tone-map roll-off) doesn't clip
for kx, ky, kz, e, s, aim in ((0.8, faceY*1.2, 1.9, 90, 0.8, body_c),
                              (-0.9, faceY*0.8, 1.2, 50, 1.2, body_c),
                              (0.2, -faceY*1.2, 1.6, 65, 0.9, body_c),
                              (0.15, faceY*1.1, -0.45, 45, 1.4, low_c)):
    Lt = bpy.data.lights.new("k", 'AREA'); Lt.energy = e; Lt.size = s
    o = bpy.data.objects.new("k", Lt); scn.collection.objects.link(o)
    o.location = body_c + Vector((kx, ky, kz))
    o.rotation_euler = (aim - o.location).normalized().to_track_quat('-Z', 'Y').to_euler()
camd = bpy.data.cameras.new("C"); cam = bpy.data.objects.new("C", camd)
scn.collection.objects.link(cam); scn.camera = cam; camd.lens = 50
fov = 2*math.atan(18.0/camd.lens)
CAM_DEG = 39.0
th = math.radians(CAM_DEG)
cdir = Vector((math.sin(th), faceY*math.cos(th), 0.10))
center = Vector((0, 0, 0.62)); size = 2.0
dist = (size*0.6)/math.tan(fov/2)*1.18
cam.location = center + cdir.normalized()*dist
cam.rotation_euler = (center - cam.location).normalized().to_track_quat('-Z', 'Y').to_euler()

seqdir = os.path.join(SKILL_ROOT, "scratch", "dlrb_frames")
os.makedirs(seqdir, exist_ok=True)
scn.render.image_settings.file_format = 'PNG'
scn.render.filepath = os.path.join(seqdir, "f####")
NORENDER = os.environ.get("N6_NORENDER") == "1" or os.environ.get("N6_STILLS_ONLY") == "1"
if not NORENDER:
    for _f in os.listdir(seqdir):
        if _f.endswith(".png"): os.remove(os.path.join(seqdir, _f))
    bpy.ops.render.render(animation=True)

try: scn.eevee.taa_render_samples = STILL_SAMP
except Exception: pass
def shoot(nm, frame, d, center=Vector((0, 0, 0.62)), size=2.0, lens=50):
    camd.lens = lens; fv = 2*math.atan(18.0/lens)
    dd = (size*0.6)/math.tan(fv/2)*1.18; loc = center + d.normalized()*dd
    cam.location = loc; cam.rotation_euler = (center-loc).normalized().to_track_quat('-Z', 'Y').to_euler()
    scn.frame_set(frame); scn.render.filepath = os.path.join(HERE, "deadlift_conventional_%s.png" % nm)
    bpy.ops.render.render(write_still=True); print("STILL", nm, "frame", frame)
front34 = Vector((math.sin(th), faceY*math.cos(th), 0.10))
sidev = Vector((1.0, faceY*0.12, 0.06))
midpull_of = bottom_of + (NF-bottom_of)//3
shoot("frame_setup", bottom_of, front34)
shoot("frame_midpull", midpull_of, front34)
shoot("frame_lockout", NF, front34)
shoot("diag_barbreak_side", bottom_of, sidev)
scn.frame_set(NF); bpy.context.view_layer.update()
gripd = Vector((0.35, faceY*0.9, -0.18))
shoot("diag_grip", NF, gripd, center=ppos("finger3-2.L"), size=0.24, lens=80)
# 3x zoom crops framing BOTH fists on the bar at 5 frames spread across the WHOLE clip
# (early descent, mid descent, floor/bottom, mid pull, near lockout)
crop_frames = sorted(set([10, max(1, bottom_of//2), bottom_of,
                          bottom_of + (NF-bottom_of)//2, NF-2]))
for cf in crop_frames:
    scn.frame_set(cf); bpy.context.view_layer.update()
    _, cby, cbz = bar_track[cf-1]
    cropd = Vector((0.30, faceY*0.95, -0.10))
    shoot("crop_f%02d" % cf, cf, cropd, center=Vector((0.0, cby, cbz)), size=0.62, lens=80)

scn.render.filepath = os.path.join(seqdir, "f####")
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "deadlift_conventional.blend"))
print("N6_BUILD_DONE frames=%d bottom=%d crops=%s min_elbow=%.1f barz_signchanges=%d" % (
    NF, bottom_of, crop_frames, min_elbow, sign_changes))
