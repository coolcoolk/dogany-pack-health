"""hand_remodel_diag.py -- read-only topology/proportion audit of the v4 hand.

Purpose: produce NUMBERS for the remodel-scope diagnosis. For each hand (.L/.R):
  - hand-region vert / tri counts
  - per-finger: vert count, cross-section (edge-loop) count along the finger X
    axis, and radial resolution (verts per loop) -- i.e. can it bend + read?
  - palm proportion: wrist-crease -> knuckle (palm) vs knuckle -> tip (fingers)
    measured from the MESH, not the bones
  - pinky isolation: how many verts actually belong to the pinky lane
  - L/R mirror symmetry: vert-count delta + thenar-web (thumb base) vert delta

Everything is measured in the imported glb frame: X = along-arm (L=+, R=-),
Y = front(-)/back(+), Z = up. Local xs = x * side_sign.

Usage: blender --background --python hand_remodel_diag.py -- <glb>
"""
import bpy, sys, os
from collections import defaultdict

GLB = sys.argv[sys.argv.index("--") + 1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB)
mesh = max([o for o in bpy.data.objects if o.type == 'MESH'], key=lambda o: len(o.data.vertices))
arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
me = mesh.data
gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}

# finger lane centers (from hand_sep_v4): index -Y .. pinky +Y, knuckle at x=0.845
LANES = {"index": -0.0135, "middle": 0.0155, "ring": 0.0445, "pinky": 0.0735}
KNUCK = 0.845
LANE_HALF = 0.0145   # half the inter-finger spacing (0.029)

print("=== GLB:", os.path.basename(GLB))
print("=== total mesh verts=%d tris=%d" %
      (len(me.vertices), sum(len(p.vertices) - 2 for p in me.polygons)))


def dom_group(v):
    if not v.groups:
        return None
    g = max(v.groups, key=lambda g: g.weight)
    return gi2name.get(g.group, None)


def finger_of_vert(v, s):
    """Return finger name if this vert is dominantly weighted to a finger bone of side s."""
    n = dom_group(v)
    if not n or not n.endswith(s):
        return None
    for f in ("thumb", "index", "middle", "ring", "pinky"):
        if n.startswith(f):
            return f
    return None


for s, sign in ((".L", 1.0), (".R", -1.0)):
    print("\n########## HAND%s ##########" % s)
    # collect verts per finger by DOMINANT bone weight (robust to lane overlap)
    per_finger = defaultdict(list)
    palm_verts = []
    for v in me.vertices:
        n = dom_group(v)
        if not n or not n.endswith(s):
            continue
        xs = v.co.x * sign
        if n.startswith("hand"):
            palm_verts.append(xs)
            continue
        f = finger_of_vert(v, s)
        if f:
            per_finger[f].append(v.co)

    # --- per finger: loop count (distinct X cross-sections) + radial resolution ---
    print("  per-finger topology (dominant-weight verts):")
    for f in ("thumb", "index", "middle", "ring", "pinky"):
        vs = per_finger.get(f, [])
        if not vs:
            print("    %-7s verts=0  << NONE" % f)
            continue
        xs = sorted(c.x * sign for c in vs)
        # quantize X to 3mm bins (~loop spacing) to count cross-sections
        bins = defaultdict(int)
        for x in xs:
            bins[round(x / 0.006)] += 1   # 6mm bins
        loops = len(bins)
        med_radial = sorted(bins.values())[len(bins) // 2]
        print("    %-7s verts=%3d  xloops(6mm)=%2d  radial/loop(med)=%2d  xspan=%.4f..%.4f (%.4f)"
              % (f, len(vs), loops, med_radial, xs[0], xs[-1], xs[-1] - xs[0]))

    # --- palm proportion from mesh ---
    if palm_verts:
        palm_verts.sort()
        palm_lo, palm_hi = palm_verts[0], palm_verts[-1]
        # finger tip = max x across all fingers
        alltip = max((c.x * sign for vs in per_finger.values() for c in vs), default=palm_hi)
        palm_len = KNUCK - palm_lo      # wrist-ish -> knuckle
        finger_len = alltip - KNUCK     # knuckle -> tip
        print("  palm span xs=[%.4f..%.4f]  (palm_len wrist->knuckle=%.4f)"
              % (palm_lo, palm_hi, palm_len))
        print("  finger reach: knuckle=%.4f -> tip=%.4f  (finger_len=%.4f)"
              % (KNUCK, alltip, finger_len))
        if finger_len > 0:
            print("  >> PALM:FINGER ratio = %.2f  (human norm ~0.95-1.10)"
                  % (palm_len / finger_len))

# --- L/R mirror symmetry ---
print("\n########## MIRROR SYMMETRY ##########")
cnt = {".L": defaultdict(int), ".R": defaultdict(int)}
for v in me.vertices:
    n = dom_group(v)
    if not n:
        continue
    for s in (".L", ".R"):
        if n.endswith(s):
            for f in ("hand", "thumb", "index", "middle", "ring", "pinky"):
                if n.startswith(f):
                    cnt[s][f] += 1
for f in ("hand", "thumb", "index", "middle", "ring", "pinky"):
    l, r = cnt[".L"][f], cnt[".R"][f]
    flag = "  << ASYMMETRIC" if abs(l - r) > max(2, 0.08 * max(l, r, 1)) else ""
    print("  %-7s  L=%4d  R=%4d  delta=%+d%s" % (f, l, r, r - l, flag))
print("DIAG_DONE")
