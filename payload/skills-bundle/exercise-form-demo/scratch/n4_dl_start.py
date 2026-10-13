"""N4 deadlift START position: bar on the floor at plate height (225mm) over the
midfoot; pelvis dropped + knees bent with feet planted (coordinate-descent leg
IK), torso hinged until the shoulders hang the straight arms onto the bar; the
proven N2/N3 wrap solver grips it.

Derived from n3_deadlift.py; same build / structures / wrap.
Usage: blender --background --python n4_dl_start.py
"""
import bpy, addon_utils, os, math
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))

BARR = float(os.environ.get("N2_BARR", "0.014"))

bpy.ops.wm.read_factory_settings(use_empty=True)
addon_utils.enable('bl_ext.user_default.mpfb', default_set=True, persistent=True)
from bl_ext.user_default.mpfb.services.humanservice import HumanService
from bl_ext.user_default.mpfb.services.targetservice import TargetService
from bl_ext.user_default.mpfb.services.locationservice import LocationService

# ===== 1 approved body =====
MACRO = {"gender": 1.0, "age": 0.45, "muscle": 1.0, "weight": 0.85,
         "proportions": 0.7, "height": 0.60, "cupsize": 0.5, "firmness": 0.9,
         "race": {"asian": 0.34, "caucasian": 0.33, "african": 0.33}}
body = HumanService.create_human(macro_detail_dict=MACRO)
TDIR = LocationService.get_mpfb_data("targets")
D = 1.0
for rel, w in [
    ("arms/l-upperarm-muscle-incr", D), ("arms/r-upperarm-muscle-incr", D),
    ("arms/l-lowerarm-muscle-incr", D * 0.8), ("arms/r-lowerarm-muscle-incr", D * 0.8),
    ("arms/l-upperarm-shoulder-muscle-incr", D), ("arms/r-upperarm-shoulder-muscle-incr", D),
    ("torso/torso-muscle-pectoral-incr", D), ("torso/torso-muscle-dorsi-incr", D),
    ("legs/l-upperleg-muscle-incr", D * 0.85), ("legs/r-upperleg-muscle-incr", D * 0.85),
    ("legs/l-lowerleg-muscle-incr", D * 0.8), ("legs/r-lowerleg-muscle-incr", D * 0.8),
    ("torso/torso-vshape-incr", 0.25), ("stomach/stomach-tone-incr", 1.0),
    ("torso/measure-shoulder-dist-incr", 0.2), ("torso/measure-waist-circ-decr", 0.1),
]:
    p = os.path.join(TDIR, rel + ".target.gz")
    TargetService.load_target(body, p, weight=w, name=os.path.basename(rel))
for p in body.data.polygons:
    p.use_smooth = True
sub = body.modifiers.new("sub", 'SUBSURF'); sub.levels = 1; sub.render_levels = 2
m = bpy.data.materials.new("skin"); m.use_nodes = True
b = m.node_tree.nodes["Principled BSDF"]
b.inputs["Base Color"].default_value = (0.60, 0.42, 0.32, 1)
b.inputs["Roughness"].default_value = 0.5
body.data.materials.clear(); body.data.materials.append(m)

# trunks (approved tailoring; hem lengthened to just above the knee -- in the
# deep hinge the old mid-thigh hem rode up and bared the whole thigh)
W_TOP, W_HEM = 1.06, 0.62
deps = bpy.context.evaluated_depsgraph_get()
me = bpy.data.meshes.new_from_object(body.evaluated_get(deps))
band = set(v.index for v in me.vertices if W_HEM <= v.co.z <= W_TOP and abs(v.co.x) < 0.28)
faces = [p for p in me.polygons if all(vi in band for vi in p.vertices)]
vmap = {}; sverts = []
for p in faces:
    for vi in p.vertices:
        if vi not in vmap:
            v = me.vertices[vi]
            vmap[vi] = len(sverts); sverts.append(v.co + v.normal * 0.006)
sfaces = [tuple(vmap[vi] for vi in p.vertices) for p in faces]
smesh = bpy.data.meshes.new("shorts")
smesh.from_pydata([tuple(c) for c in sverts], [], sfaces); smesh.update()

import bmesh as _bmesh
def leg_frame(sign):
    up = [v.co for v in me.vertices if 0.76 < v.co.z < 0.86 and 0.02 < sign * v.co.x < 0.28]
    lo = [v.co for v in me.vertices if 0.50 < v.co.z < 0.58 and 0.02 < sign * v.co.x < 0.28]
    cU = sum(up, Vector()) / len(up); cL = sum(lo, Vector()) / len(lo)
    ax = (cU - cL).normalized()
    return ax, cL + ax * ((W_HEM - cL.z) / ax.z)
FR = {1: leg_frame(1), -1: leg_frame(-1)}
bmm = _bmesh.new(); bmm.from_mesh(smesh)
zmid = (W_HEM + W_TOP) * 0.5
hemv = [v for v in bmm.verts if v.is_boundary and v.co.z < zmid]
topv = [v for v in bmm.verts if v.is_boundary and v.co.z >= zmid]
def project_hem():
    for v in hemv:
        ax, Q = FR[1] if v.co.x >= 0 else FR[-1]
        v.co -= ax * ((v.co - Q).dot(ax))
project_hem()
for _ in range(3):
    _bmesh.ops.smooth_vert(bmm, verts=hemv, factor=0.5, use_axis_x=True, use_axis_y=True, use_axis_z=True)
    project_hem()
for v in topv:
    v.co.z = W_TOP
for _ in range(3):
    _bmesh.ops.smooth_vert(bmm, verts=topv, factor=0.5, use_axis_x=True, use_axis_y=True, use_axis_z=False)
bmm.to_mesh(smesh); bmm.free(); smesh.update()
for p in smesh.polygons:
    p.use_smooth = True
shorts = bpy.data.objects.new("shorts", smesh)
bpy.context.scene.collection.objects.link(shorts)
sol = shorts.modifiers.new("sol", 'SOLIDIFY'); sol.thickness = 0.004
ssub = shorts.modifiers.new("sub", 'SUBSURF'); ssub.levels = 1; ssub.render_levels = 2
fm = bpy.data.materials.new("fabric"); fm.use_nodes = True
fb = fm.node_tree.nodes["Principled BSDF"]
fb.inputs["Base Color"].default_value = (0.015, 0.015, 0.018, 1)
fb.inputs["Roughness"].default_value = 0.9
smesh.materials.append(fm)

# ===== 2 rig =====
arm = HumanService.add_builtin_rig(body, "default", import_weights=True)
print("N3 rig=%s bones=%d" % (arm.name, len(arm.data.bones)))
bpy.context.view_layer.objects.active = body
shorts.select_set(True); body.select_set(True)
with bpy.context.temp_override(object=body, active_object=body,
                               selected_editable_objects=[body, shorts]):
    bpy.ops.object.data_transfer(data_type='VGROUP_WEIGHTS',
                                 vert_mapping='POLYINTERP_NEAREST',
                                 layers_select_src='ALL', layers_select_dst='NAME')
shorts.parent = arm
amod = shorts.modifiers.new("arm", 'ARMATURE'); amod.object = arm
# big joint rotations collapse the 6mm cloth offset (shorts z-fight into the
# thighs); shrinkwrap AFTER the armature keeps the cloth outside the skin
swr = shorts.modifiers.new("swr", 'SHRINKWRAP')
swr.target = body
swr.wrap_method = 'NEAREST_SURFACEPOINT'
swr.wrap_mode = 'OUTSIDE'
swr.offset = 0.005

pb = arm.pose.bones
mwa = arm.matrix_world
for pbone in arm.pose.bones:
    pbone.rotation_mode = 'XYZ'
def ppos(n, tail=False):
    b = pb[n]
    return mwa @ (b.tail if tail else b.head)

# ===== 3 morphed rest coords + hand structures =====
name2idx = {vg.name: vg.index for vg in body.vertex_groups}
idx2name = {vg.index: vg.name for vg in body.vertex_groups}
mask_mod = next((mm for mm in body.modifiers if mm.type == 'MASK'), None)
visible = None
if mask_mod and mask_mod.vertex_group:
    mg = name2idx[mask_mod.vertex_group]; inv = mask_mod.invert_vertex_group
    visible = set()
    for v in body.data.vertices:
        inn = any(g.group == mg and g.weight > 0 for g in v.groups)
        if inn != inv:
            visible.add(v.index)

body_mw = body.matrix_world
_mstates = [(mm, mm.show_viewport) for mm in body.modifiers]
for _m, _s in _mstates:
    _m.show_viewport = False
_deps = bpy.context.evaluated_depsgraph_get()
_rest_me = bpy.data.meshes.new_from_object(body.evaluated_get(_deps))
restco = [body_mw @ v.co for v in _rest_me.vertices]
bpy.data.meshes.remove(_rest_me)
for _m, _s in _mstates:
    _m.show_viewport = _s
assert len(restco) == len(body.data.vertices), "rest eval changed vertex count"

SIDES = ("L", "R")
seg_verts = {}
for side in SIDES:
    for fi in (1, 2, 3, 4, 5):
        for sg in (1, 2, 3):
            gid = name2idx.get("finger%d-%d.%s" % (fi, sg, side))
            s = set()
            if gid is not None:
                for v in body.data.vertices:
                    if visible is not None and v.index not in visible:
                        continue
                    for g in v.groups:
                        if g.group == gid and g.weight > 0.5:
                            s.add(v.index); break
            seg_verts[(fi, sg, side)] = s

K_rest = {}
hand_i = {}
allfg = {}
for side in SIDES:
    K_rest[side] = sum((ppos("finger%d-1.%s" % (f, side)) for f in (2, 3, 4, 5)),
                       Vector()) / 4
    hand_i[side] = [i for i in (visible or range(len(body.data.vertices)))
                    if (restco[i] - K_rest[side]).length < 0.12]
    allfg[side] = set().union(*[seg_verts[(fi, sg, side)]
                                for fi in (1, 2, 3, 4, 5) for sg in (1, 2, 3)])

# manual LBS over ALL hand verts (palm moves with the arm pose in n3)
arm_mw = arm.matrix_world; arm_inv = arm_mw.inverted()
bones = {bn.name for bn in arm.data.bones}
rest_inv = {bn.name: bn.matrix_local.inverted() for bn in arm.data.bones}
allsk = set(hand_i["L"]) | set(hand_i["R"])
skin = {}
for i in allsk:
    v = body.data.vertices[i]
    ws = [(idx2name[g.group], g.weight) for g in v.groups]
    ws = [(nm, w) for nm, w in ws if nm in bones and w > 0]
    tot = sum(w for _, w in ws) or 1.0
    skin[i] = (arm_inv @ restco[i], [(nm, w / tot) for nm, w in ws])

def pos_of(i):
    rest_co, ws = skin[i]
    co = Vector((0, 0, 0))
    for nm, w in ws:
        co += w * ((pb[nm].matrix @ rest_inv[nm]) @ rest_co)
    return arm_mw @ co

# solve fast: viewport modifiers off during the update-heavy loops
sub.show_viewport = False; ssub.show_viewport = False; sol.show_viewport = False

# ===== 4 ARM POSE (measurement-driven, no axis assumptions) =====
# body facing along Y: ankle -> toe BONE direction (both vertex-cloud heuristics
# guessed wrong; the foot bone cannot -- toes point where the body faces)
faceY = 1.0 if (ppos("toe2-1.L") - ppos("foot.L")).y > 0 else -1.0
print("N3 faceY=%+.0f (body faces %sY, via foot bone)"
      % (faceY, "-" if faceY < 0 else "+"))

def descend(bone, score, comps=(0, 1, 2), steps=(math.radians(10), math.radians(4)),
            rounds=25):
    # generic coordinate descent on one bone's euler; score() smaller = better
    for st in steps:
        for _ in range(rounds):
            improved = False
            for c in comps:
                for d in (st, -st):
                    e = pb[bone].rotation_euler
                    old = e[c]
                    e[c] = old + d
                    bpy.context.view_layer.update()
                    s1 = score()
                    if s1 < descend.best - 1e-9:
                        descend.best = s1
                        improved = True
                    else:
                        e[c] = old
                        bpy.context.view_layer.update()
            if not improved:
                break

# --- heavy-lockout posture (owner: "does not look like he is holding weight") ---
# stance: the rest pose feet are WIDE; conventional DL stance is hip width
for side in SIDES:
    sgn = 1.0 if ppos("upperleg01.%s" % side).x >= 0 else -1.0
    a0 = ppos("foot.%s" % side)
    tgt = Vector((sgn * 0.10, a0.y, a0.z))
    def scost():
        return (ppos("foot.%s" % side) - tgt).length
    descend.best = scost()
    descend("upperleg01.%s" % side, scost)
    print("N3 %s stance ankle x=%.3f (res=%.3f)"
          % (side, ppos("foot.%s" % side).x, descend.best))

# spine FORWARD-hinge sign, measured via head nudge (forward = facing side)
h0 = ppos("head").y
pb["spine03"].rotation_euler = (math.radians(5), 0, 0)
bpy.context.view_layer.update()
fsgn = 1.0 if (ppos("head").y - h0) * faceY > 0 else -1.0
pb["spine03"].rotation_euler = (0, 0, 0)
bpy.context.view_layer.update()

# scapular depression: heavy load pulls the shoulder girdle DOWN ~15mm
for side in SIDES:
    t = ppos("shoulder01.%s" % side) + Vector((0, 0, -0.015))
    def ccost():
        return (ppos("shoulder01.%s" % side) - t).length
    descend.best = ccost()
    descend("clavicle.%s" % side, ccost, steps=(math.radians(6), math.radians(2)))
    print("N3 %s clavicle depressed (res=%.3f)" % (side, descend.best))

# --- START-POSE bar target: plate radius above the floor, over the midfoot ---
sole_z = min(q.z for q in restco)
BAR_TZ = sole_z + 0.225
# 2cm toward the toes off pure midfoot: at exact midfoot the bar sat inside the
# shin flesh (ankles visually skewered)
BAR_TY = (ppos("foot.L").y + ppos("toe2-1.L").y
          + ppos("foot.R").y + ppos("toe2-1.R").y) / 4 + faceY * 0.02
print("N4 bar target y=%.3f z=%.3f (midfoot, plate height)" % (BAR_TY, BAR_TZ))

def descend_multi(dofs, score, rounds=40):
    # coordinate descent over mixed DOFs: (posebone, attr, index, (coarse, fine))
    best = score()
    for phase in (0, 1):
        for _ in range(rounds):
            improved = False
            for ob, attr, idx, steps in dofs:
                st = steps[phase]
                for d in (st, -st):
                    vec = getattr(ob, attr)
                    old = vec[idx]
                    vec[idx] = old + d
                    bpy.context.view_layer.update()
                    s1 = score()
                    if s1 < best - 1e-9:
                        best = s1
                        improved = True
                    else:
                        vec[idx] = old
                        bpy.context.view_layer.update()
            if not improved:
                break
    return best

# --- pelvis drop + knee bend with feet PLANTED (leg IK by descent) ---
feetT = {s: ppos("foot.%s" % s).copy() for s in SIDES}
toesT = {s: ppos("toe2-1.%s" % s).copy() for s in SIDES}
hipy0 = ppos("root").y
# --- ANALYTIC 2-link leg IK, solved joint by joint. Every search-based attempt
#     either froze (coupled valley) or diverged (alternating objectives); this
#     is plain geometry: hips translate to the DL-start target, each knee goes
#     to its 2-link circle point (picked toward the face), shin closes on the
#     planted ankle, foot levels the toes. ---
def feeterr():
    s = 0.0
    for sd in SIDES:
        s += (ppos("foot.%s" % sd) - feetT[sd]).length
        s += (ppos("toe2-1.%s" % sd) - toesT[sd]).length
    return s

# Blender's BUILT-IN IK does the legs (every hand-rolled solver froze, diverged
# or knock-kneed): ankle empties pin the feet where they stood, pole empties
# keep the knees bowing toward the face, and the root just drags the pelvis to
# the DL-start target while the engine solves the chains.
hipc0 = (ppos("upperleg01.L") + ppos("upperleg01.R")) / 2
# hip target DERIVED from torso length, not guessed: shoulders are pinned at
# bar+reach, and placing the hips closer to them than the torso is long forced
# the spine to fold and shoved the belly through the thighs (owner caught it).
TORSO = ((ppos("shoulder01.L") + ppos("shoulder01.R")) / 2 - hipc0).length
# straight-arm reach measured HERE (the shoulder height estimate needs it)
for bn in ("upperarm01.L", "lowerarm01.L", "wrist.L"):
    pb[bn].rotation_euler = (0, 0, 0)
bpy.context.view_layer.update()
_shL = ppos("upperarm01.L")
def _straightL():
    return -(ppos("finger3-1.L") - _shL).length
descend.best = _straightL()
descend("lowerarm01.L", _straightL, steps=(math.radians(6), math.radians(2)))
reach0 = (ppos("finger3-1.L") - ppos("upperarm01.L")).length
sh_z_est = BAR_TZ + reach0 * 0.98
HIPZ_T = 0.68
_dy = math.sqrt(max(TORSO * TORSO - (sh_z_est - HIPZ_T) ** 2, 0.01))
HSTAR = Vector((0, (BAR_TY + faceY * 0.02) + (-faceY) * _dy * 0.90, HIPZ_T))
print("N4 torso=%.3f reach=%.3f -> hip target y=%.3f z=%.3f"
      % (TORSO, reach0, HSTAR.y, HSTAR.z))
loc_dofs = [(pb["root"], "location", i, (0.03, 0.006)) for i in (0, 1, 2)]

def mkempty(name, loc):
    e = bpy.data.objects.new(name, None)
    bpy.context.scene.collection.objects.link(e)
    e.location = loc
    return e

# stance a touch wider + knees tracking OUT: gives the torso a corridor between
# the thighs (hips-back only made the measured overlap worse)
for sd in SIDES:
    sgn = 1.0 if feetT[sd].x >= 0 else -1.0
    feetT[sd].x = sgn * 0.14
    toesT[sd].x = sgn * 0.155                         # slight toe-out
for sd in SIDES:
    ankle = mkempty("ankT.%s" % sd, feetT[sd])
    knee0 = ppos("lowerleg01.%s" % sd).copy()
    sgn = 1.0 if knee0.x >= 0 else -1.0
    pole = mkempty("polT.%s" % sd,
                   Vector((knee0.x + sgn * 0.06, knee0.y + faceY * 0.8, knee0.z)))
    con = pb["lowerleg02.%s" % sd].constraints.new('IK')
    con.target = ankle
    con.pole_target = pole
    con.chain_count = 4                               # lowerleg02..upperleg01
    # calibrate pole_angle: the wrong value twists the whole leg; pick the one
    # that leaves the (currently straight) leg where it stands
    best_pa = None
    for pa in range(-180, 180, 10):                   # 30-deg grid left L/R asymmetric
        con.pole_angle = math.radians(pa)             # (-120 vs -60) and the knees
        bpy.context.view_layer.update()               # crossed at deep flexion
        dev = (ppos("lowerleg01.%s" % sd) - knee0).length
        if best_pa is None or dev < best_pa[0]:
            best_pa = (dev, pa)
    con.pole_angle = math.radians(best_pa[1])
    bpy.context.view_layer.update()
    print("N4 %s IK pole_angle=%d (dev=%.3f)" % (sd, best_pa[1], best_pa[0]))

def hscore():
    c = (ppos("upperleg01.L") + ppos("upperleg01.R")) / 2
    return (c - HSTAR).length
descend_multi(loc_dofs, hscore, rounds=30)
for sd in SIDES:                                      # level the toes back down
    def tscore():
        return (ppos("toe2-1.%s" % sd) - toesT[sd]).length
    descend.best = tscore()
    descend("foot.%s" % sd, tscore)
print("N4 legs IK: hip z=%.3f y=%.3f feet-err=%.3f knee L y=%.3f z=%.3f"
      % (ppos("upperleg01.L").z, ppos("upperleg01.L").y, feeterr(),
         ppos("lowerleg01.L").y, ppos("lowerleg01.L").z))

# pelvis-pitch sign: rotating the root must carry the shoulders toward the face
_c0 = ((ppos("shoulder01.L") + ppos("shoulder01.R")) / 2).y
pb["root"].rotation_euler = (math.radians(10), 0, 0)
bpy.context.view_layer.update()
rsgn = 1.0 if (((ppos("shoulder01.L") + ppos("shoulder01.R")) / 2).y - _c0) * faceY > 0 else -1.0
pb["root"].rotation_euler = (0, 0, 0)
bpy.context.view_layer.update()

def hinge_to(sz, sy):
    # torso hinge: put the shoulder-pair centroid at (sy, sz); reset each call.
    # The PELVIS pitches forward (root rotation -- legs stay planted, they are
    # IK-pinned) and carries a near-neutral spine; the spine joints only refine.
    # Spine-only hinging folded the model into a round-backed crunch.
    for bn in ("spine05", "spine04", "spine03", "spine02", "neck01"):
        pb[bn].rotation_euler = (0, 0, 0)
    pb["root"].rotation_euler = (rsgn * math.radians(35), 0, 0)
    pb["spine05"].rotation_euler = (fsgn * math.radians(15), 0, 0)
    bpy.context.view_layer.update()
    def hs():
        c = (ppos("shoulder01.L") + ppos("shoulder01.R")) / 2
        return abs(c.z - sz) + abs(c.y - sy)
    # root + spine05 + a whisper of spine04 ONLY: upper-spine flexing pooched
    # the belly down INTO the thighs and rounded the back
    r = descend_multi(
        [(pb["root"], "rotation_euler", 0, (math.radians(8), math.radians(2))),
         (pb["spine05"], "rotation_euler", 0, (math.radians(6), math.radians(2))),
         (pb["spine04"], "rotation_euler", 0, (math.radians(3), math.radians(1)))], hs)
    # neck counters the measured torso pitch: gaze ahead-down, not at the floor
    tv = ppos("neck01") - ppos("spine05")
    pitch = math.atan2(math.hypot(tv.x, tv.y), max(tv.z, 1e-6))
    pb["neck01"].rotation_euler = (-fsgn * pitch * 0.55, 0, 0)
    bpy.context.view_layer.update()
    return r

PEN = float(os.environ.get("N2_PEN", "0.005"))
BARV = float(os.environ.get("N2_BARV", "-0.005"))
R = BARR

def pose_arm(side, ty):
    ua = "upperarm01.%s" % side
    la = "lowerarm01.%s" % side
    # RESET first: descending from the previous pass's pose let the arm drift
    # into a bent-forward local minimum it could never leave (bar at the waist)
    for bn in (ua, la, "wrist.%s" % side):
        pb[bn].rotation_euler = (0, 0, 0)
    bpy.context.view_layer.update()
    sh = ppos(ua)
    # heavy load = arm hangs like a rope, FULLY stretched: extend the elbow by
    # maximizing shoulder->hand distance (owner: bent elbows kill the weight feel)
    def straight():
        return -(ppos("finger3-1.%s" % side) - sh).length
    descend.best = straight()
    descend(la, straight, steps=(math.radians(6), math.radians(2)))
    reach = (ppos("finger3-1.%s" % side) - sh).length
    # grip a touch wider than the shoulders (owner: shoulder-drop grip too narrow)
    sgn = 1.0 if sh.x >= 0 else -1.0
    dy = abs(ty - sh.y)
    dz = math.sqrt(max((reach * 0.995) ** 2 - dy ** 2, 0.01))   # taut straight-line hang
    target = Vector((sh.x + sgn * 0.05, ty, sh.z - dz))
    def aim():
        return (ppos("finger3-1.%s" % side) - target).length
    descend.best = aim()
    descend(ua, aim)
    # wrist align: knuckle line -> world X, palm normal -> body rear (SIGNED).
    # Hand chirality is pose-invariant: fix the palmar sign of kl x ds once with
    # the curl-nudge probe, then the cost can demand the palm truly faces rear.
    wr = "wrist.%s" % side
    xhat = Vector((1, 0, 0))
    rear = Vector((0, -faceY, 0))
    def _kl_ds():
        kl = (ppos("finger5-1.%s" % side) - ppos("finger2-1.%s" % side)).normalized()
        ds = (ppos("finger3-2.%s" % side) - ppos("finger3-1.%s" % side)).normalized()
        ds = (ds - kl * ds.dot(kl)).normalized()
        return kl, ds
    tip0 = ppos("finger3-3.%s" % side, tail=True)
    pb["finger3-2.%s" % side].rotation_euler = (math.radians(40), 0, 0)
    bpy.context.view_layer.update()
    pdir0 = (ppos("finger3-3.%s" % side, tail=True) - tip0).normalized()
    pb["finger3-2.%s" % side].rotation_euler = (0, 0, 0)
    bpy.context.view_layer.update()
    kl0, ds0 = _kl_ds()
    chir = 1.0 if kl0.cross(ds0).dot(pdir0) >= 0 else -1.0
    def wcost():
        kl, ds = _kl_ds()
        n = kl.cross(ds) * chir                       # true palmar normal
        return (1 - abs(kl.dot(xhat))) * 2.0 + (1 - n.dot(rear))
    descend.best = wcost()
    descend(wr, wcost)

def hand_frame(side):
    K = sum((ppos("finger%d-1.%s" % (f, side)) for f in (2, 3, 4, 5)), Vector()) / 4
    klm = (ppos("finger5-1.%s" % side) - ppos("finger2-1.%s" % side)).normalized()
    Zc = Vector((1, 0, 0)) if klm.x >= 0 else Vector((-1, 0, 0))   # snap to world X
    tip0 = ppos("finger3-3.%s" % side, tail=True)
    pb["finger3-2.%s" % side].rotation_euler = (math.radians(40), 0, 0)
    bpy.context.view_layer.update()
    palmardir = (ppos("finger3-3.%s" % side, tail=True) - tip0).normalized()
    pb["finger3-2.%s" % side].rotation_euler = (0, 0, 0)
    bpy.context.view_layer.update()
    dstl = (ppos("finger3-2.%s" % side) - ppos("finger3-1.%s" % side)).normalized()
    dstl = (dstl - Zc * dstl.dot(Zc)).normalized()
    e1 = Zc.cross(dstl).normalized()
    if e1.dot(palmardir) < 0:
        e1 = -e1
    return {"K": K, "Zc": Zc, "e1": e1, "e2": dstl}

def seat_of(side, F):
    palm_pos = {i: pos_of(i) for i in hand_i[side] if i not in allfg[side]}
    pband = []
    for i, q in palm_pos.items():
        d = q - F["K"]
        if abs(d.dot(F["e2"])) <= 0.015 and abs(d.dot(F["Zc"])) <= 0.05 \
                and 0.0 < d.dot(F["e1"]) <= 0.05:
            pband.append(d.dot(F["e1"]))
    s_crease = max(pband)
    Cs = F["K"] + F["e1"] * (s_crease + R - PEN) + F["e2"] * BARV
    F["palm_pos"] = palm_pos
    return Cs

# ===== 5 hinge + arms with 2-D bar feedback (y AND z): every pass resets, so
#       each attempt is deterministic; errors feed the next targets =====
frames = {}
BAR_Y = BAR_Z = 0.0

def solve_pose():
    global BAR_Y, BAR_Z
    ty = BAR_TY
    sz = BAR_TZ + reach0 * 0.99
    sy = BAR_TY + faceY * 0.02
    for attempt in range(7):
        hinge_to(sz, sy)
        for side in SIDES:
            pose_arm(side, ty)
        cys = []; czs = []
        for side in SIDES:
            frames[side] = hand_frame(side)
            Cs = seat_of(side, frames[side])
            cys.append(Cs.y); czs.append(Cs.z)
        BAR_Y = sum(cys) / 2; BAR_Z = sum(czs) / 2
        errY = BAR_TY - BAR_Y; errZ = BAR_TZ - BAR_Z
        print("N4 pose pass %d: bar y=%.3f z=%.3f (err %+.3f / %+.3f)"
              % (attempt + 1, BAR_Y, BAR_Z, errY, errZ))
        if abs(errY) < 0.006 and abs(errZ) < 0.006:
            break
        ty += errY * 0.7                              # damped: undamped ping-ponged
        sy += errY * 0.35
        sz = min(max(sz + errZ * 0.7, BAR_TZ + 0.40), BAR_TZ + reach0)

# --- MEASURED torso-thigh interpenetration (owner: stop eyeballing). Deformed
#     body with only the armature modifier on (indices stay aligned); thigh
#     faces become a BVH; torso verts inside it are penetration, depth in m. ---
from mathutils.bvhtree import BVHTree
def dom_bone(v):
    bg = [(idx2name[g.group], g.weight) for g in v.groups
          if idx2name[g.group] in bones and g.weight > 0]
    return max(bg, key=lambda t: t[1])[0] if bg else ""
_thigh_i = set(); _torso_i = set()
for v in body.data.vertices:
    if visible is not None and v.index not in visible:
        continue
    nm = dom_bone(v)
    if nm.startswith("upperleg") or nm.startswith("lowerleg"):
        _thigh_i.add(v.index)
    elif nm.startswith("spine") or nm.startswith("pelvis"):
        _torso_i.add(v.index)

def torso_thigh_pen():
    states = [(mm, mm.show_viewport) for mm in body.modifiers]
    for mm, _s in states:
        if mm.type != 'ARMATURE':
            mm.show_viewport = False
    dg = bpy.context.evaluated_depsgraph_get()
    me2 = bpy.data.meshes.new_from_object(body.evaluated_get(dg))
    co = [body_mw @ v.co for v in me2.vertices]
    faces = [tuple(p.vertices) for p in me2.polygons
             if all(vi in _thigh_i for vi in p.vertices)]
    bvh = BVHTree.FromPolygons([tuple(c) for c in co], faces)
    worst = 0.0; cnt = 0
    for i in _torso_i:
        hit = bvh.find_nearest(co[i], 0.08)
        if hit and hit[0] is not None:
            loc, nrm, _idx, dist = hit
            if nrm.dot(co[i] - loc) < 0:              # inside the thigh volume
                cnt += 1
                if dist > worst:
                    worst = dist
    bpy.data.meshes.remove(me2)
    for mm, s in states:
        mm.show_viewport = s
    bpy.context.view_layer.update()
    return worst, cnt

solve_pose()
for fix in range(3):
    depth, npen = torso_thigh_pen()
    print("N4 torso-thigh penetration: depth=%.3f m verts=%d" % (depth, npen))
    if depth < 0.008:
        break
    # widen the corridor: ankles out 2cm, knees out 5cm more per round
    for sd in SIDES:
        sgn = 1.0 if feetT[sd].x >= 0 else -1.0
        bpy.data.objects["ankT.%s" % sd].location.x += sgn * 0.02
        bpy.data.objects["polT.%s" % sd].location.x += sgn * 0.05
    bpy.context.view_layer.update()
    solve_pose()
print("N4 bar line y=%.3f z=%.3f" % (BAR_Y, BAR_Z))

def rad(q):
    return math.hypot(q.y - BAR_Y, q.z - BAR_Z)

# ===== 6 wrap per hand (N2 solver, side-threaded) =====
STEPW = math.radians(float(os.environ.get("N2_STEP", "2")))
MAXA = {1: math.radians(95), 2: math.radians(100), 3: math.radians(70)}
TMAX = {1: math.radians(55), 2: math.radians(65), 3: math.radians(80)}
SPREAD = math.radians(float(os.environ.get("N2_SPREAD", "8")))
TPEN = float(os.environ.get("N2_TPEN", "0.003"))
TFLEX2 = math.radians(float(os.environ.get("N2_TF2", "35")))
TFLEX3 = math.radians(float(os.environ.get("N2_TF3", "40")))
ZTGT = float(os.environ.get("N2_TZ", "-0.030"))
THTGT = math.radians(float(os.environ.get("N2_TTH", "-30")))

for side in SIDES:
    F = frames[side]
    K, Zc, e1, e2 = F["K"], F["Zc"], F["e1"], F["e2"]

    def set_joint(fi, sg, ang, z=0.0):
        pb["finger%d-%d.%s" % (fi, sg, side)].rotation_euler = (ang, 0, z)

    def wrap_joint(fi, sg, z, amax, setter=None, test=None, start=0.0, pen=None):
        p = PEN if pen is None else pen
        moving = set().union(*[seg_verts[(fi, s, side)]
                               for s in (test or (1, 2, 3)) if s >= (0 if test else sg)])
        setf = setter or (lambda a: set_joint(fi, sg, a, z))
        setf(start)
        bpy.context.view_layer.update()
        live = [i for i in moving if rad(pos_of(i)) >= R - p + 0.001]
        ang = start
        while ang + STEPW <= amax + 1e-6:
            trial = ang + STEPW
            setf(trial)
            bpy.context.view_layer.update()
            if any(rad(pos_of(i)) < R - p for i in live):
                setf(ang)
                bpy.context.view_layer.update()
                break
            ang = trial
        return ang

    # splay close first (extended fingers), sign measured per finger
    zadd = {}
    for fi, refi in ((2, 3), (4, 3), (5, 4)):
        ref = ppos("finger%d-3.%s" % (refi, side), tail=True)
        d0 = (ppos("finger%d-3.%s" % (fi, side), tail=True) - ref).length
        set_joint(fi, 1, 0.0, math.radians(5))
        bpy.context.view_layer.update()
        d1 = (ppos("finger%d-3.%s" % (fi, side), tail=True) - ref).length
        zadd[fi] = (1.0 if d1 < d0 else -1.0) * SPREAD
        set_joint(fi, 1, 0.0, zadd[fi])
        bpy.context.view_layer.update()

    angles = {}
    for fi in (2, 3, 4, 5):
        for sg in (1, 2, 3):
            tst = (2, 3) if (fi == 2 and sg == 1) else None
            angles[(fi, sg)] = wrap_joint(
                fi, sg, zadd.get(fi, 0.0) if sg == 1 else 0.0, MAXA[sg], test=tst)

    # thumb: bent chain + CMC grid with flesh guard
    set_joint(1, 2, TFLEX2); set_joint(1, 3, TFLEX3)
    tverts = list(seg_verts[(1, 2, side)] | seg_verts[(1, 3, side)])
    best = None; best_any = None
    for xd in range(-20, 61, 5):
        for zd in range(0, 71, 5):
            zsgn = -1.0 if side == "L" else 1.0       # mirrored adduction sense
            set_joint(1, 1, math.radians(xd), zsgn * math.radians(zd))
            bpy.context.view_layer.update()
            q = ppos("finger1-3.%s" % side, tail=True)
            dp = q - Vector((q.x, BAR_Y, BAR_Z))
            axq = (q - K).dot(Zc)
            th = math.atan2((dp).dot(e2), (dp).dot(e1)) if dp.length > 1e-9 else 0.0
            cost = (abs(axq - ZTGT) + abs(rad(q) - (R + 0.002)) * 2.0
                    + abs(th - THTGT) * 0.01)
            if best_any is None or cost < best_any[0]:
                best_any = (cost, xd, zd)
            ok = True
            for nm, tl in (("finger1-2.%s" % side, False),
                           ("finger1-2.%s" % side, True),
                           ("finger1-3.%s" % side, True)):
                if rad(ppos(nm, tail=tl)) < R - 0.002:
                    ok = False; break
            if ok:
                for i in tverts:
                    if rad(pos_of(i)) < R - TPEN:
                        ok = False; break
            if ok and (best is None or cost < best[0]):
                best = (cost, xd, zd)
    if best is None:
        best = best_any
        print("N3 WARN %s thumb grid: no clear pose, using best-any" % side)
    _, txd, tzd = best
    zsgn = -1.0 if side == "L" else 1.0
    set_joint(1, 1, math.radians(txd), zsgn * math.radians(tzd))
    angles[(1, 1)] = math.radians(txd)
    angles[(1, 2)] = wrap_joint(1, 2, 0.0, TMAX[2], start=TFLEX2, test=(2, 3), pen=TPEN)
    angles[(1, 3)] = wrap_joint(1, 3, 0.0, TMAX[3], start=TFLEX3, test=(3,), pen=TPEN)
    print("N3 %s thumb CMC flex=%d add=%d" % (side, txd, tzd))
    for fi in (2, 3, 4, 5, 1):
        print("N3 %s wrap f%d = %s deg" % (side, fi,
              "/".join(str(round(math.degrees(angles[(fi, s)]))) for s in (1, 2, 3))))

    # verify: clearance + sectors
    bpy.context.view_layer.update()
    OBS = [pos_of(i) for i in allfg[side]] + [pos_of(i) for i in F["palm_pos"]]
    NSEC = 8; RMAXS = 0.06
    sect = [False] * NSEC
    cl = 1e9
    for Q in OBS:
        r = rad(Q)
        if r < cl:
            cl = r
        if r < RMAXS:
            a = math.atan2((Q - Vector((Q.x, BAR_Y, BAR_Z))).dot(e2),
                           (Q - Vector((Q.x, BAR_Y, BAR_Z))).dot(e1))
            sect[int((a + math.pi) / (2 * math.pi) * NSEC) % NSEC] = True
    print("N3 %s seat clearance=%.4f (floor=%.4f) sectors=%d/8"
          % (side, cl, R - PEN, sum(sect)))

sub.show_viewport = True; ssub.show_viewport = True; sol.show_viewport = True
bpy.context.view_layer.update()

# ===== 7 bar + plates + floor + renders + save =====
bpy.ops.mesh.primitive_cylinder_add(radius=R, depth=2.2, location=(0, BAR_Y, BAR_Z))
bar = bpy.context.active_object
bar.rotation_euler = Vector((1, 0, 0)).to_track_quat('Z', 'Y').to_euler()
bm2 = bpy.data.materials.new("steel"); bm2.use_nodes = True
sb = bm2.node_tree.nodes["Principled BSDF"]
sb.inputs["Base Color"].default_value = (0.35, 0.36, 0.38, 1)
sb.inputs["Metallic"].default_value = 1.0
sb.inputs["Roughness"].default_value = 0.35
bar.data.materials.append(bm2)

# 450mm plates: their radius (0.225) is what DEFINES the bar height off the floor
# in the start position (owner-confirmed ordering: plates first, then hinge)
PLATE_R = 0.225; PLATE_T = 0.045; PLATE_X = 0.66     # IPF-ish inner face spacing
pmat = bpy.data.materials.new("plate"); pmat.use_nodes = True
pB = pmat.node_tree.nodes["Principled BSDF"]
pB.inputs["Base Color"].default_value = (0.06, 0.06, 0.065, 1)
pB.inputs["Roughness"].default_value = 0.6
for sx in (1, -1):
    bpy.ops.mesh.primitive_cylinder_add(
        radius=PLATE_R, depth=PLATE_T,
        location=(sx * (PLATE_X + PLATE_T / 2), BAR_Y, BAR_Z))
    pl = bpy.context.active_object
    pl.rotation_euler = Vector((1, 0, 0)).to_track_quat('Z', 'Y').to_euler()
    pl.data.materials.append(pmat)

# floor at the actual sole height so the plates read against a ground plane
sole_z = min(q.z for q in restco)
bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, sole_z))
floor = bpy.context.active_object
fmat = bpy.data.materials.new("floor"); fmat.use_nodes = True
fB = fmat.node_tree.nodes["Principled BSDF"]
fB.inputs["Base Color"].default_value = (0.05, 0.05, 0.055, 1)
fB.inputs["Roughness"].default_value = 0.95
floor.data.materials.append(fmat)

scn = bpy.context.scene
try:
    scn.render.engine = 'BLENDER_EEVEE'
except TypeError:
    scn.render.engine = 'BLENDER_EEVEE_NEXT'
scn.render.resolution_x = scn.render.resolution_y = 1000
scn.view_settings.exposure = -0.4
try:
    scn.view_settings.view_transform = 'AgX'
    scn.view_settings.look = 'AgX - Punchy'
except TypeError:
    pass
world = bpy.data.worlds.new("W"); scn.world = world; world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.035, 0.035, 0.04, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 0.35

allp = restco
lo = Vector((min(p.x for p in allp), min(p.y for p in allp), min(p.z for p in allp)))
hi = Vector((max(p.x for p in allp), max(p.y for p in allp), max(p.z for p in allp)))
body_c = Vector((0, (lo.y + hi.y) / 2, 0.95))
for kx, ky, kz, e, s in ((0.8, faceY * 1.2, 1.9, 120, 0.8), (-0.9, faceY * 0.8, 1.2, 60, 1.2),
                         (0.2, -faceY * 1.2, 1.6, 80, 0.9), (0.1, faceY * 0.5, 0.2, 40, 0.8)):
    L = bpy.data.lights.new("k", 'AREA'); L.energy = e; L.size = s
    o = bpy.data.objects.new("k", L); scn.collection.objects.link(o)
    o.location = body_c + Vector((kx, ky, kz))
    o.rotation_euler = (body_c - o.location).normalized().to_track_quat('-Z', 'Y').to_euler()

camd = bpy.data.cameras.new("C"); cam = bpy.data.objects.new("C", camd)
scn.collection.objects.link(cam); scn.camera = cam; camd.lens = 65
fov = 2 * math.atan(18.0 / camd.lens)

def shoot(name, center, size, d):
    dist = (size * 0.6) / math.tan(fov / 2) * 1.15
    loc = center + d.normalized() * dist
    cam.location = loc
    cam.rotation_euler = (center - loc).normalized().to_track_quat('-Z', 'Y').to_euler()
    scn.render.filepath = os.path.join(HERE, "n4_%s.png" % name)
    bpy.ops.render.render(write_still=True)
    print("R", name)

full_c = Vector((0, 0, 0.75))                          # crouched pose sits low
hand_L = ppos("finger3-2.L")
shoot("dl_front", full_c, (hi - lo).length, Vector((0.15, faceY, 0.05)))
shoot("dl_side", full_c, (hi - lo).length, Vector((1.0, faceY * 0.12, 0.05)))
shoot("dl_grip_L", hand_L, 0.30, Vector((0.3, faceY, -0.25)))
shoot("dl_grip_wide", Vector((0, BAR_Y, BAR_Z)), 0.75, Vector((0.05, faceY, -0.2)))

bpy.ops.wm.save_as_mainfile(filepath=os.path.join(HERE, "n4_dl_start.blend"))
print("N4_DONE")
