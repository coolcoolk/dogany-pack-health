"""hand_sep_v4.py -- true per-finger separation + a 15-bone-per-hand rig.

Problem (v2/v3): the 4 fingers are one fused paddle. v3 stopped at a smooth
GROUPED wrap because there was no per-finger geometry to skin. This script does
the modeling v3 declined to attempt: it carves the fused paddle into 5 distinct
digits, then builds a real per-finger skeleton (thumb + 4 fingers, 3 bones each
= 15 deform bones per hand) with clean, per-finger, non-bleeding weights.

Two coupled parts:
  1) MESH SURGERY (bmesh): add resolution to the finger paddle (bisect at the 3
     inter-finger gap planes + one subdivide pass), then DISPLACE geometry into
     4 separate finger tubes -- pinch deep V-grooves down the 3 gaps (top and
     bottom shells driven together so a real slot opens), inflate each finger's
     centerline into a rounded tube, taper the tips to per-finger lengths, and
     weld the pinched groove seams so adjacent fingers become geometrically
     distinct lobes joined only at the natural palm knuckle. The palm/wrist is
     left untouched so the rest of the body rig is preserved exactly.
  2) BONES + WEIGHTS: drop the grouped fingers_01/02/03, add per-finger chains
     index/middle/ring/pinky (3 each) and extend the thumb to 3 bones. Each
     finger vertex is skinned ONLY to its own chain + hand by inverse-distance
     falloff, so there is zero cross-finger bleed (the separated geometry makes
     this clean, unlike v3's necessarily-shared grouped weights).

Bone scheme (per side, .L/.R), all use_deform=True, chain rooted at hand<side>:
    thumb_01 -> thumb_02 -> thumb_03           (metacarpal / proximal / distal)
    index_01 -> index_02 -> index_03           (proximal / middle / distal)
    middle_01 -> middle_02 -> middle_03
    ring_01 -> ring_02 -> ring_03
    pinky_01 -> pinky_02 -> pinky_03
15 finger bones/hand; 54 deform bones total (34 v3 - 6 grouped-finger + 2 thumb_03
+ 24 new per-finger).

Usage (headless):
  blender --background --python hand_sep_v4.py -- \
      <in_v3.glb> <out_v4.glb> <out_v4_lowpoly.glb> \
      <check_open.png> <check_grip.png> <tag>

Coordinate frame (as imported from the glb): X = left(+)/right(-) along the arm,
Y = front(-)/back(+), Z = up. Local along-arm coord xs = x * side_sign.
"""
import bpy, sys, math, bmesh
from mathutils import Vector, Matrix

# ---- finger paddle layout (LEFT-hand / local coords; mirrored by side_sign) ----
X_KNUCK = 0.845          # knuckle base (fingers begin here)
X_TIP   = 0.930          # farthest fingertip (middle finger)
FY_MIN, FY_MAX = -0.028, 0.088   # Y span the 4 fingers occupy
MIDZ = 0.537             # paddle mid-thickness plane
# 4 equal finger lanes across [FY_MIN, FY_MAX]; index nearest the thumb (-Y).
_LANE = (FY_MAX - FY_MIN) / 4.0
CENTERS = {"index":  FY_MIN + 0.5 * _LANE,
           "middle": FY_MIN + 1.5 * _LANE,
           "ring":   FY_MIN + 2.5 * _LANE,
           "pinky":  FY_MIN + 3.5 * _LANE}
GAPS = [FY_MIN + 1 * _LANE, FY_MIN + 2 * _LANE, FY_MIN + 3 * _LANE]
# per-finger tip length (X). middle longest, pinky shortest -- realism + reads.
TIPLEN = {"index": 0.914, "middle": 0.930, "ring": 0.922, "pinky": 0.900}
FINGERS = ["index", "middle", "ring", "pinky"]

# groove/inflate tuning
X_GROOVE_START = 0.860   # grooves begin just past the knuckle (natural palm web)
X_GROOVE_FULL  = 0.884   # grooves at full depth from here to the tips
GROOVE_HALF    = 0.013   # Y half-width of a groove influence band
PINCH          = 0.98    # fraction of half-thickness pulled to MIDZ at groove core
#   PINCH~1.0 makes the top and bottom groove shells actually MEET at the seam so
#   remove_doubles welds them into one clean valley -- the old 0.72 left the shells
#   apart, so the weld could not close them and thin sliver webs survived (the
#   "firework" flap the reviewer/owner flagged between the fingers).
NARROW         = 0.14    # gentle off-seam pull; high values TEAR the seam into slivers
INFLATE        = 0.52    # centerline tube inflation (fraction of half-thickness)


def clamp(v, a=0.0, b=1.0):
    return max(a, min(b, v))


def _finger_of(y):
    """Nearest finger lane for a Y (LEFT/local frame)."""
    return min(FINGERS, key=lambda f: abs(y - CENTERS[f]))


# ============================ 1) MESH SURGERY ================================
def separate_fingers(mesh):
    """Carve the fused paddle into 4 distinct finger tubes + rounded tips.
    Operates per side in local coords; welds pinched groove seams at the end."""
    bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.mode_set(mode='OBJECT')
    bm = bmesh.new()
    bm.from_mesh(mesh.data)
    bm.verts.layers.deform.verify()   # keep skin weights on new/old verts

    for sc in (1, -1):
        _add_resolution(bm, sc)
    bm.normal_update()

    for sc in (1, -1):
        _displace(bm, sc)

    # --- groove cleanup (kills the sliver "firework" webs at the groove roots) ---
    # The pinched grooves leave near-coincident top/bottom shell verts plus thin
    # bridging faces across each opening slot. A global weld at 0.0009 was too weak
    # to close them. Here we weld + dissolve DEGENERATE geometry region-locally at a
    # threshold sized to the web thickness (~0.0026), so the thin sheets collapse
    # into the seam without touching the rest of the body mesh.
    # cleanup region is WIDER than the displace region: it reaches back to the
    # knuckle base (x>=0.842) so the natural inter-finger WEB at the finger roots
    # is welded too -- otherwise the fan-spread open pose tears that un-welded base
    # webbing into thin jagged sheets (the residual "firework" near the knuckles).
    def _clean_faces(sc):
        out = []
        for f in bm.faces:
            c = f.calc_center_median()
            if c.x * sc > 0.842 and c.y > -0.030 and 0.50 < c.z < 0.575:
                out.append(f)
        return out

    # A gentle weld (0.0016) plus a slightly larger degenerate-dissolve (0.0024):
    # welding hard merges tube verts and makes the fingertips lumpy, so we lean on
    # dissolve_degenerate (which only collapses the thin SHORT-edge sliver faces,
    # leaving the healthy tube quads intact) for the sliver kill.
    for sc in (1, -1):
        cf = _clean_faces(sc)
        rverts = list({v for f in cf for v in f.verts})
        bmesh.ops.remove_doubles(bm, verts=rverts, dist=0.0026)
        redges = list({e for f in _clean_faces(sc) for e in f.edges})
        bmesh.ops.dissolve_degenerate(bm, dist=0.0028, edges=redges)

    # Laplacian smooth of the finger region to clean groove/tip jaggies + tip lumps
    for sc in (1, -1):
        rv = list({v for f in _clean_faces(sc) for v in f.verts})
        for _ in range(4):
            bmesh.ops.smooth_vert(bm, verts=rv, factor=0.5,
                                  use_axis_x=True, use_axis_y=True, use_axis_z=True)

    bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
    bm.normal_update()
    bm.to_mesh(mesh.data)
    bm.free()
    # final global pass: catch any remaining coincident verts + fix normals
    _weld(mesh, 0.0009)
    mesh.data.update()


def _region_faces(bm, sc):
    """Finger-paddle faces for one side (exclude thumb + palm)."""
    out = []
    for f in bm.faces:
        c = f.calc_center_median()
        xs = c.x * sc
        if xs > (X_GROOVE_START - 0.004) and c.y > -0.030 and 0.505 < c.z < 0.57:
            out.append(f)
    return out


def _add_resolution(bm, sc):
    # bisect at each inter-finger gap plane (crisp groove loops), region only
    for g in GAPS:
        faces = _region_faces(bm, sc)
        edges = {e for f in faces for e in f.edges}
        geom = list(faces) + list(edges) + list({v for f in faces for v in f.verts})
        bmesh.ops.bisect_plane(bm, geom=geom, dist=1e-5,
                               plane_co=Vector((0, g, 0)),
                               plane_no=Vector((0, 1, 0)), clear_inner=False,
                               clear_outer=False)
    # one uniform subdivide of the region for smooth grooves/tubes
    faces = _region_faces(bm, sc)
    edges = list({e for f in faces for e in f.edges})
    bmesh.ops.subdivide_edges(bm, edges=edges, cuts=1, use_grid_fill=True)


def _displace(bm, sc):
    dfl = bm.verts.layers.deform.verify()  # noqa: F841 (keep layer alive)
    for v in bm.verts:
        c = v.co
        xs = c.x * sc
        if xs <= (X_GROOVE_START - 0.006) or c.y <= -0.030 or not (0.505 < c.z < 0.57):
            continue
        if c.y < FY_MIN - 0.006 or c.y > FY_MAX + 0.006:
            continue
        finger = _finger_of(c.y)
        cen = CENTERS[finger]
        ramp = clamp((xs - X_GROOVE_START) / (X_GROOVE_FULL - X_GROOVE_START))
        # nearest inter-finger gap
        dg = min(abs(c.y - g) for g in GAPS)
        gap_f = clamp(1.0 - dg / GROOVE_HALF)          # 1 at seam -> 0 at band edge
        near_gap = min((g for g in GAPS), key=lambda g: abs(c.y - g))

        new = c.copy()
        # (a) PINCH the groove: drive top & bottom shells toward MIDZ
        pinch = ramp * gap_f * PINCH
        new.z = c.z + (MIDZ - c.z) * pinch
        # (b) NARROW: pull groove verts off the seam toward their finger center
        if gap_f > 0.0:
            new.y = c.y + (cen - c.y) * (gap_f * ramp * NARROW)
        # (c) INFLATE the finger centerline into a rounded tube
        dc = abs(c.y - cen)
        core = clamp(1.0 - dc / (0.5 * _LANE))         # 1 at center -> 0 at lane edge
        infl = ramp * core * (1.0 - gap_f) * INFLATE
        halfz = 0.017
        new.z = new.z + math.copysign(halfz * infl, c.z - MIDZ)
        # (d) TIP taper: compress past this finger's tip length, round the end.
        # Kept GENTLE (0.45, not 0.7): a hard compression jams many verts into the
        # tip, and the later weld turns that pileup into sliver/lump geometry -- a
        # softer taper leaves an evenly-sampled rounded tip.
        tl = TIPLEN[finger]
        if xs > tl - 0.02:
            over = clamp((xs - (tl - 0.02)) / 0.05)
            target = tl - 0.02 + (xs - (tl - 0.02)) * (1.0 - 0.45 * over)
            new.x = sc * min(xs, target) if sc > 0 else -min(xs, target)
            # round the tip: pull toward centerline as we approach it
            new.y = new.y + (cen - new.y) * 0.22 * over
            new.z = MIDZ + (new.z - MIDZ) * (1.0 - 0.30 * over)
        v.co = new


def _weld(mesh, dist):
    bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=dist)
    bpy.ops.mesh.dissolve_degenerate(threshold=2.0e-4)  # kill zero-area sliver flaps
    # Delete INTERIOR faces: the residual sliver "firework" sheets are thin faces
    # buried inside the welded finger volume (both their sides face solid mesh).
    # select_interior_faces finds exactly those; deleting them leaves the outer
    # skin intact and removes the flaps that survived the degenerate dissolve.
    bpy.ops.mesh.select_all(action='DESELECT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_interior_faces()
    bpy.ops.mesh.delete(type='FACE')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode='OBJECT')


# ============================ 2) BONES ======================================
def _thirds(a, b):
    d = (b - a) / 3.0
    return [(a, a + d), (a + d, a + 2 * d), (a + 2 * d, b)]


def rebuild_finger_bones(arm):
    """Remove grouped fingers_01/02/03; add per-finger chains + thumb_03."""
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='EDIT')
    eb = arm.data.edit_bones
    for s, sc in ((".L", 1), (".R", -1)):
        # drop grouped finger bones
        for n in ("fingers_01", "fingers_02", "fingers_03"):
            b = eb.get(n + s)
            if b:
                eb.remove(b)
        hand = eb.get("hand" + s)

        def V(x, y, z=MIDZ):
            return Vector((sc * x, y, z))

        # ---- 4 fingers, 3 bones each, along X at each lane center ----
        for finger in FINGERS:
            cen = CENTERS[finger]
            tl = TIPLEN[finger]
            segs = _thirds(X_KNUCK, tl)
            prev = hand
            connect = False
            for i, (a, b) in enumerate(segs, start=1):
                bn = "%s_%02d%s" % (finger, i, s)
                nb = eb.get(bn) or eb.new(bn)
                nb.head, nb.tail = V(a, cen), V(b, cen)
                nb.parent, nb.use_connect, nb.use_deform = prev, connect, True
                prev, connect = nb, True

        # ---- thumb: 3 bones down the -Y diagonal protrusion ----
        thumb_pts = [V(0.760, -0.020), V(0.792, -0.042), V(0.820, -0.062), V(0.845, -0.078)]
        prev, connect = hand, False
        for i in range(3):
            bn = "thumb_%02d%s" % (i + 1, s)
            nb = eb.get(bn) or eb.new(bn)
            nb.head, nb.tail = thumb_pts[i], thumb_pts[i + 1]
            nb.parent, nb.use_connect, nb.use_deform = prev, connect, True
            prev, connect = nb, True
    bpy.ops.object.mode_set(mode='OBJECT')


# ============================ 3) WEIGHTS ====================================
def _pt_seg_dist(p, a, b):
    ab = b - a
    d = ab.dot(ab)
    t = clamp((p - a).dot(ab) / d) if d > 1e-12 else 0.0
    return (p - (a + ab * t)).length


def _vg(mesh, name):
    return mesh.vertex_groups.get(name) or mesh.vertex_groups.new(name=name)


def reweight_hand(mesh, power=3.0, eps=0.006, smooth_iters=5, smooth_factor=0.5):
    """Per-finger inverse-distance skin weights. Each finger vertex is skinned
    ONLY to its own chain + hand (no neighbouring finger bone in the pool), so
    there is zero cross-finger bleed. Smoothing is restricted to same-finger
    neighbours. Palm/wrist verts are left on their original groups."""
    co = [v.co for v in mesh.data.vertices]
    for s, sc in ((".L", 1), (".R", -1)):
        def V(x, y, z=MIDZ):
            return Vector((sc * x, y, z))

        palm_seg = (V(0.80, 0.02, 0.535), V(X_KNUCK, 0.02, 0.535))

        # segment endpoints per finger + thumb
        finger_segs = {}
        for finger in FINGERS:
            cen = CENTERS[finger]
            finger_segs[finger] = [(V(a, cen), V(b, cen))
                                   for a, b in _thirds(X_KNUCK, TIPLEN[finger])]
        thumb_pts = [V(0.760, -0.020), V(0.792, -0.042), V(0.820, -0.062), V(0.845, -0.078)]
        thumb_segs = [(thumb_pts[i], thumb_pts[i + 1]) for i in range(3)]

        # classify region verts
        region = {}      # vi -> (kind, finger_or_None, weight-list)
        fid = {}         # vi -> finger id ("thumb" for thumb) for smoothing groups
        for vi, c in enumerate(co):
            xs = c.x * sc
            if xs < 0.74 or not (0.49 < c.z < 0.585):
                continue
            is_thumb = (c.y < -0.030 and 0.74 < xs < 0.86)
            is_finger = (xs > X_KNUCK - 0.004 and -0.030 < c.y < FY_MAX + 0.02
                         and not is_thumb)
            if not (is_thumb or is_finger):
                continue
            if is_thumb:
                bones = [("hand" + s, palm_seg),
                         ("thumb_01" + s, thumb_segs[0]),
                         ("thumb_02" + s, thumb_segs[1]),
                         ("thumb_03" + s, thumb_segs[2])]
                fid[vi] = "thumb"
            else:
                finger = _finger_of(c.y)
                fs = finger_segs[finger]
                bones = [("hand" + s, palm_seg),
                         ("%s_01%s" % (finger, s), fs[0]),
                         ("%s_02%s" % (finger, s), fs[1]),
                         ("%s_03%s" % (finger, s), fs[2])]
                fid[vi] = finger
            ws = [(bn, 1.0 / ((_pt_seg_dist(c, a, b) + eps) ** power))
                  for bn, (a, b) in bones]
            tot = sum(w for _, w in ws) or 1.0
            region[vi] = [(bn, w / tot) for bn, w in ws]
        if not region:
            continue

        wd = {vi: {bn: w for bn, w in ws} for vi, ws in region.items()}
        # same-finger adjacency only (prevents cross-finger smoothing bleed)
        adj = {vi: set() for vi in wd}
        for e in mesh.data.edges:
            a, b = e.vertices
            if a in wd and b in wd and fid.get(a) == fid.get(b):
                adj[a].add(b); adj[b].add(a)
        for _ in range(smooth_iters):
            nxt = {}
            for vi, w in wd.items():
                nb = adj[vi]
                if nb:
                    keys = set(w)
                    for n in nb:
                        keys |= set(wd[n])
                    acc = {k: w.get(k, 0.0) * (1 - smooth_factor)
                           + sum(wd[n].get(k, 0.0) for n in nb) / len(nb) * smooth_factor
                           for k in keys}
                else:
                    acc = dict(w)
                tot = sum(acc.values()) or 1.0
                nxt[vi] = {k: v / tot for k, v in acc.items()}
            wd = nxt

        names = ["hand" + s, "thumb_01" + s, "thumb_02" + s, "thumb_03" + s]
        for finger in FINGERS:
            names += ["%s_0%d%s" % (finger, i, s) for i in (1, 2, 3)]
        clear_idx = {mesh.vertex_groups[n].index for n in names
                     if mesh.vertex_groups.get(n)}
        groups = {n: _vg(mesh, n) for n in names}
        for vi, w in wd.items():
            v = mesh.data.vertices[vi]
            for gi in list({g.group for g in v.groups} & clear_idx):
                mesh.vertex_groups[gi].remove([vi])
            items = sorted(w.items(), key=lambda kv: -kv[1])[:4]
            tot = sum(x for _, x in items) or 1.0
            for bn, ww in items:
                if ww / tot > 1e-4:
                    groups[bn].add([vi], ww / tot, 'REPLACE')


# ============================ POSING / RENDER ===============================
def wrot(arm, pbname, axis, deg):
    pb = arm.pose.bones.get(pbname)
    if pb is None:
        return
    M = pb.matrix.copy(); head = M.translation.copy()
    R = Matrix.Rotation(math.radians(deg), 4, axis)
    pb.matrix = Matrix.Translation(head) @ R @ Matrix.Translation(head).inverted() @ M
    bpy.context.view_layer.update()


def reset_pose(arm):
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.transforms_clear()
    bpy.ops.object.mode_set(mode='OBJECT')


# reference grip pose (LEFT hand wrapping a ~27mm bar = realistic Olympic bar at
# this hand scale, 1 unit ~= 1060mm). Tuned by fitting the finger's curled joint
# arc to a circle and placing the bar at that arc's centre of curvature with
# radius = arc_radius - finger_half_thickness, so each finger CONFORMS to the bar
# (mesh hugs the surface, zero gross pass-through). The fingers close into a real
# fist AROUND the bar and the bar exits both sides of the grip -- a genuine grip,
# not the v4-round-0 claw that hovered in front of the bar.
GRIP_BAR = (0.8308, 0.5168, 0.0137)  # x, z, radius (bar axis along Y)
# uniform 70 deg/joint -> the joints lie on the arc the bar radius was fitted to.
GRIP_CURL = {"index": (70, 70, 70), "middle": (70, 70, 70),
             "ring": (70, 70, 70), "pinky": (70, 70, 70)}
# Thumb wrap (round 2). The round-0/1 thumb only folded X/Z into the palm on the
# SAME side as the fingers, so it never crossed the bar -> read as a thumbless
# (monkey) grip. This scheme wraps it like a real closed grip, verified against the
# bar in hand_thumb_fit.py (thumb-mesh: 0 verts inside bar; tip -> index_mesh
# ~14mm; thumb tip curls to dz=-0.038 below the bar centre, tucked toward the
# index):
#   thumb_01 Z = adduct the thumb ACROSS toward the fingers, bringing the tip off
#     the far -Y side in toward the index (kept <=28 deg: >=35 deg tears the
#     thumb-base skin weights into a shard).
#   thumb_02 / thumb_03 Y = curl the thumb DOWN over the bar and tuck the tip
#     under, about world-Y (the bar axis) -- the SAME axis the 4 fingers wrap on,
#     so the thumb conforms to the bar instead of folding onto the hand's back.
GRIP_THUMB = (28, 46, 48)  # thumb_01 Z-adduct, thumb_02 Y-curl, thumb_03 Y-curl


def pose_grip(arm, side=".L"):
    reset_pose(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    for finger in FINGERS:
        a, b, c = GRIP_CURL[finger]
        wrot(arm, "%s_01%s" % (finger, side), 'Y', a)
        wrot(arm, "%s_02%s" % (finger, side), 'Y', b)
        wrot(arm, "%s_03%s" % (finger, side), 'Y', c)
    tz, t2y, t3y = GRIP_THUMB
    wrot(arm, "thumb_01" + side, 'Z', tz)   # adduct across toward the fingers
    wrot(arm, "thumb_02" + side, 'Y', t2y)  # curl down over the bar (bar-axis)
    wrot(arm, "thumb_03" + side, 'Y', t3y)  # tuck the tip under toward the index
    bpy.ops.object.mode_set(mode='OBJECT')


def pose_spread(arm, side=".L"):
    """Open relaxed hand, fingers fanned apart about Z so the 5 separated digits
    read clearly. Kept nearly FLAT (tiny straightening, no curl) -- the round-0
    open_check curled into a half-fist which hid the separation; the rest geometry
    already splits the 4 fingers, so a gentle fan + slight straighten shows it."""
    reset_pose(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    fan = {"index": -11, "middle": -4, "ring": 5, "pinky": 13}
    for finger in FINGERS:
        wrot(arm, "%s_01%s" % (finger, side), 'Z', fan[finger])
        wrot(arm, "%s_02%s" % (finger, side), 'Y', -3)   # slight straighten
        wrot(arm, "%s_03%s" % (finger, side), 'Y', -2)
    wrot(arm, "thumb_01" + side, 'Z', 26)
    wrot(arm, "thumb_02" + side, 'Z', 14)
    bpy.ops.object.mode_set(mode='OBJECT')


def _studio(sc):
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x = sc.render.resolution_y = 1200
    try: sc.eevee.taa_render_samples = 32
    except Exception: pass
    if sc.world is None:
        sc.world = bpy.data.worlds.new('W')
    sc.world.use_nodes = True
    bg = sc.world.node_tree.nodes.get('Background')
    bg.inputs[0].default_value = (0.62, 0.62, 0.65, 1.0)
    bg.inputs[1].default_value = 1.0
    for ang, en in (((55, 0, 20), 3.2), ((60, 0, 160), 1.6), ((30, 0, -90), 1.4)):
        lt = bpy.data.lights.new("sun", 'SUN'); lt.energy = en
        lo = bpy.data.objects.new("sun", lt); bpy.context.collection.objects.link(lo)
        lo.rotation_euler = (math.radians(ang[0]), math.radians(ang[1]), math.radians(ang[2]))


def _cam(loc, tgt, lens=105):
    cam = bpy.data.cameras.new("c"); ob = bpy.data.objects.new("c", cam)
    bpy.context.collection.objects.link(ob); ob.location = Vector(loc)
    ob.rotation_euler = (Vector(tgt) - ob.location).normalized().to_track_quat('-Z', 'Y').to_euler()
    cam.lens = lens
    bpy.context.scene.camera = ob
    return ob


def render_open(mesh, arm, path):
    """Open, fanned hand seen from front-above so the 5 digits + grooves read."""
    pose_spread(arm, ".L")
    sc = bpy.context.scene
    _studio(sc)
    _cam((0.90, -0.34, 0.72), (0.875, 0.02, 0.520), lens=86)
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)


def render_grip(mesh, arm, path):
    """Closed per-finger bar-grip around a test cylinder, tight 3/4 crop."""
    bx, bz, r = GRIP_BAR
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=0.32, vertices=48,
                                        location=(bx, 0.0, bz))
    bar = bpy.context.active_object
    bar.rotation_euler = (math.radians(90), 0, 0)
    bpy.ops.object.transform_apply(rotation=True)
    m = bpy.data.materials.new("Bar"); m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (0.15, 0.35, 0.75, 1)
    bsdf.inputs["Metallic"].default_value = 0.9
    bsdf.inputs["Roughness"].default_value = 0.3
    bar.data.materials.append(m)
    pose_grip(arm, ".L")
    sc = bpy.context.scene
    _studio(sc)
    _cam((0.98, -0.40, 0.66), (0.845, 0.0, 0.512), lens=78)
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(bar, do_unlink=True)


# ============================ EXPORT ========================================
def _export(path, rig, mesh):
    bpy.ops.object.select_all(action='DESELECT')
    rig.select_set(True); mesh.select_set(True)
    bpy.context.view_layer.objects.active = rig
    bpy.ops.export_scene.gltf(
        filepath=path, export_format='GLB', use_selection=True,
        export_apply=False, export_skins=True, export_yup=True,
        export_image_format='AUTO', export_texcoords=True, export_normals=True,
        export_materials='EXPORT')


def export_full(path, rig, mesh):
    reset_pose(rig)
    try: bpy.ops.file.pack_all()
    except Exception as e: print("pack warn", e)
    _export(path, rig, mesh)


def export_lowpoly(path, rig, mesh):
    """Same decimate-then-export approach used for v2/v3 lowpoly (target 50k tris)."""
    tris = sum(len(p.vertices) - 2 for p in mesh.data.polygons)
    bpy.ops.object.select_all(action='DESELECT')
    mesh.select_set(True); bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.duplicate()
    low = bpy.context.view_layer.objects.active; low.name = "Body_low"
    dec = low.modifiers.new("Decimate", 'DECIMATE'); dec.decimate_type = 'COLLAPSE'
    dec.ratio = min(1.0, 50000.0 / float(tris))
    while low.modifiers[0].name != "Decimate":
        bpy.ops.object.modifier_move_up(modifier="Decimate")
    bpy.ops.object.modifier_apply(modifier="Decimate")
    low_tris = sum(len(p.vertices) - 2 for p in low.data.polygons)
    print("LOW_TRIS", low_tris, "VERTS", len(low.data.vertices))
    _export(path, rig, low)
    bpy.data.objects.remove(low, do_unlink=True)


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    src, out, out_low, chk_open, chk_grip, tag = argv[:6]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

    separate_fingers(mesh)
    rebuild_finger_bones(arm)
    reweight_hand(mesh)

    ndef = sum(1 for b in arm.data.bones if b.use_deform)
    perhand = sum(1 for b in arm.data.bones if b.use_deform and b.name.endswith(".L")
                  and any(b.name.startswith(p) for p in
                          ("thumb", "index", "middle", "ring", "pinky")))
    print("SEP %s verts=%d tris=%d deform_bones=%d per_hand_finger_bones=%d" %
          (tag, len(mesh.data.vertices),
           sum(len(p.vertices) - 2 for p in mesh.data.polygons), ndef, perhand))

    render_open(mesh, arm, chk_open)
    print("CHECK_OPEN", chk_open)
    render_grip(mesh, arm, chk_grip)
    print("CHECK_GRIP", chk_grip)

    export_full(out, arm, mesh)
    import os
    print("EXPORTED_FULL", out, os.path.getsize(out))
    export_lowpoly(out_low, arm, mesh)
    print("EXPORTED_LOW", out_low, os.path.getsize(out_low))


if __name__ == "__main__":
    main()
