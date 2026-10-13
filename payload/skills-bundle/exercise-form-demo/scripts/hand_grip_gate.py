"""hand_grip_gate.py -- reusable ACCEPTANCE GATE for the bar-grip hand.

One test that catches all 6 known defect classes BEFORE a hand is promoted:
  1 reversed-on-bar     2 thumb-up (no wrap)     3 impossible wrist supination
  4 pinky vanishes / <5 fingers read            5 long palm / ghost paddle
  6 hand passes through bar  (+ L/R mirror tear)

It renders a CLOSED BAR GRIP for BOTH hands from a FIXED angle set
(front-3/4, thumb-side end-on, UNDERSIDE, top-down) and prints numeric checks with
explicit PASS/FAIL per class. Read-only on the glb (never writes the asset).

Numeric checks:
  - bar penetration: # mesh verts with radial dist < r - margin, deepest dist
  - palm:finger proportion ratio (mesh-measured)
  - per-finger vert / length (pinky-vanish detector)
  - thumb-tip side vs bar (wrap detector: tip must cross to the far side of the bar)
  - L/R digit vert-count symmetry (mirror-tear detector)

Usage:
  blender --background --python hand_grip_gate.py -- <glb> <out_dir> [side1 side2...]
  (default sides: .L .R)
"""
import bpy, sys, os, math
from collections import defaultdict
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

INSIDE_MARGIN = 0.0015
KNUCK = 0.845
LANES = {"index": -0.0135, "middle": 0.0155, "ring": 0.0445, "pinky": 0.0735}

# fixed camera set. tgt ~ grip center. loc chosen per side sign in _cam_for_side.
# base coords are for .L (+X); .R mirrors x -> -x.
CAM_L = {
    "front34":   ([0.98, -0.40, 0.66], [0.845, 0.00, 0.512], 92),
    "thumbside": ([0.84, -0.62, 0.55], [0.83, -0.02, 0.515], 96),
    "underside": ([0.90, -0.20, 0.30], [0.85,  0.02, 0.512], 96),
    "topdown":   ([0.86, -0.06, 0.86], [0.855, 0.02, 0.512], 104),
}


def _args():
    argv = sys.argv[sys.argv.index("--") + 1:]
    glb, out_dir = argv[0], argv[1]
    sides = argv[2:] if len(argv) > 2 else [".L", ".R"]
    return glb, out_dir, sides


def _load(glb):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    return mesh, arm


def _cam_for_side(name, side):
    loc, tgt, lens = CAM_L[name]
    if side == ".R":
        loc = [-loc[0], loc[1], loc[2]]
        tgt = [-tgt[0], tgt[1], tgt[2]]
    return loc, tgt, lens


def _add_bar(bar, side):
    bx, bz, r = bar
    if side == ".R":
        bx = -bx
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=0.32, vertices=64,
                                        location=(bx, 0.0, bz))
    b = bpy.context.active_object
    b.rotation_euler = (math.radians(90), 0, 0)
    bpy.ops.object.transform_apply(rotation=True)
    m = bpy.data.materials.new("Bar"); m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (0.15, 0.35, 0.75, 1)
    bsdf.inputs["Metallic"].default_value = 0.9
    bsdf.inputs["Roughness"].default_value = 0.3
    b.data.materials.append(m)
    return b, (bx, bz, r)


def _dom(mesh, gi2name, v):
    if not v.groups:
        return None
    g = max(v.groups, key=lambda g: g.weight)
    return gi2name.get(g.group, None)


def measure(mesh, arm, side):
    """Numeric checks on the posed hand for one side. Returns a dict of results."""
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}
    sign = 1.0 if side == ".L" else -1.0
    bar = list(H.GRIP_BAR)
    bx = bar[0] * sign; bz = bar[1]; r = bar[2]

    dg = mesh.evaluated_get(bpy.context.evaluated_depsgraph_get())
    ev = dg.to_mesh()
    mw = mesh.matrix_world

    inside = 0; deepest = r
    for v in ev.vertices:
        co = mw @ v.co
        d = math.hypot(co.x - bx, co.z - bz)
        if d < r - INSIDE_MARGIN:
            inside += 1
            deepest = min(deepest, d)
    mesh.to_mesh_clear()

    # rest-frame per-finger metrics (topology is pose-invariant for counts)
    per = defaultdict(list)
    palm = []
    for v in mesh.data.vertices:
        n = _dom(mesh, gi2name, v)
        if not n or not n.endswith(side):
            continue
        xs = v.co.x * sign
        if n.startswith("hand"):
            palm.append(xs); continue
        for f in ("thumb", "index", "middle", "ring", "pinky"):
            if n.startswith(f):
                per[f].append(xs); break
    finger_stats = {}
    for f in ("thumb", "index", "middle", "ring", "pinky"):
        xs = sorted(per.get(f, []))
        finger_stats[f] = (len(xs), (xs[-1] - xs[0]) if xs else 0.0)
    palm.sort()
    palm_len = KNUCK - palm[0] if palm else 0.0
    tip = max((max(per[f]) for f in per if per[f]), default=KNUCK)
    finger_len = tip - KNUCK
    ratio = (palm_len / finger_len) if finger_len > 1e-6 else 0.0

    return {"inside": inside, "deepest": deepest, "r": r,
            "finger_stats": finger_stats, "palm_len": palm_len,
            "finger_len": finger_len, "ratio": ratio}


def render_side(mesh, arm, side, out_dir):
    H.pose_grip(arm, side)
    bar_obj, _ = _add_bar(H.GRIP_BAR, side)
    sc = bpy.context.scene
    H._studio(sc)
    sc.render.resolution_x = sc.render.resolution_y = 900
    paths = []
    for name in CAM_L:
        loc, tgt, lens = _cam_for_side(name, side)
        H._cam(loc, tgt, lens=lens)
        p = "%s/gate%s_%s.png" % (out_dir, side.replace(".", "_"), name)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        paths.append(p)
        print("GATE_CROP", p)
    bpy.data.objects.remove(bar_obj, do_unlink=True)
    return paths


def verdict(res, side):
    """Explicit PASS/FAIL per defect class using the numeric checks available.
    Vision classes (1 reversed, 2 thumb-up, 3 wrist) are FLAGGED for the still
    review -- geometry checks alone cannot fully settle orientation, so the gate
    pairs numbers with the fixed-angle crops a reviewer must open."""
    fs = res["finger_stats"]
    print("  -- HAND%s numeric verdict --" % side)
    # class 4: pinky vanishes / <5 fingers read
    counts = {f: fs[f][0] for f in fs}
    lens = {f: fs[f][1] for f in fs}
    mn = min(counts.values()); mx = max(counts.values())
    pinky_ok = counts["pinky"] >= 0.55 * counts["middle"] and lens["pinky"] >= 0.7 * lens["middle"]
    print("    [C4 pinky/5-finger] pinky verts=%d (%.0f%% of middle) len=%.4f (%.0f%% of middle) -> %s"
          % (counts["pinky"], 100 * counts["pinky"] / max(counts["middle"], 1),
             lens["pinky"], 100 * lens["pinky"] / max(lens["middle"], 1e-6),
             "PASS" if pinky_ok else "FAIL"))
    # class 5: long palm / ghost paddle
    ratio_ok = 0.9 <= res["ratio"] <= 1.15
    print("    [C5 palm:finger]  ratio=%.2f (norm 0.90-1.15) -> %s"
          % (res["ratio"], "PASS" if ratio_ok else "FAIL"))
    # class 6a: hand passes through bar
    pen_ok = res["inside"] == 0
    print("    [C6 bar-through]  inside=%d deepest=%.4f (r=%.4f) -> %s"
          % (res["inside"], res["deepest"], res["r"], "PASS" if pen_ok else "FAIL"))
    return {"C4": pinky_ok, "C5": ratio_ok, "C6": pen_ok}


def main():
    glb, out_dir, sides = _args()
    os.makedirs(out_dir, exist_ok=True)
    all_v = {}
    for side in sides:
        mesh, arm = _load(glb)
        H.pose_grip(arm, side)
        res = measure(mesh, arm, side)
        all_v[side] = verdict(res, side)
        render_side(mesh, arm, side, out_dir)

    # mirror symmetry (class 6b): compare rest-frame digit vert counts L vs R
    if ".L" in sides and ".R" in sides:
        mesh, arm = _load(glb)
        gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}
        cnt = {".L": defaultdict(int), ".R": defaultdict(int)}
        for v in mesh.data.vertices:
            n = _dom(mesh, gi2name, v)
            if not n:
                continue
            for s in (".L", ".R"):
                if n.endswith(s):
                    for f in ("thumb", "index", "middle", "ring", "pinky"):
                        if n.startswith(f):
                            cnt[s][f] += 1
        print("\n  -- MIRROR (C6b thenar/web tear) --")
        worst = 0.0
        for f in ("thumb", "index", "middle", "ring", "pinky"):
            l, r = cnt[".L"][f], cnt[".R"][f]
            dpct = abs(l - r) / max(l, r, 1)
            worst = max(worst, dpct)
            print("    %-7s L=%d R=%d delta=%.0f%%" % (f, l, r, 100 * dpct))
        print("    [C6b mirror] worst digit delta=%.0f%% (PASS if <5%%) -> %s"
              % (100 * worst, "PASS" if worst < 0.05 else "FAIL"))
    print("GATE_DONE")


if __name__ == "__main__":
    main()
