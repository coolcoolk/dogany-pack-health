"""hand_grip_diag.py -- diagnose the chevron/notch artifact at the bar contact.

Loads the accepted v4 glb (no mesh surgery), then reports THREE things so the
root cause (rest-mesh sliver vs skinning pinch) can be told apart with evidence:

  A) REST-POSE sliver/degenerate scan in the finger region: per-face area, min
     edge, aspect ratio; flags thin/degenerate faces + prints their world center.
  B) GRIP-POSE deformation stretch: applies pose_grip, evaluates the deformed
     mesh, and for finger faces near the bar-contact TOP region reports the ratio
     deformed_area / rest_area (a skinning pinch/tear shows as extreme stretch or
     near-zero collapse ONLY when posed, with a clean rest face).
  C) WEIGHTS across the index/middle boundary at the fingertips: dominant bone +
     weight per vert, so a sharp weight discontinuity across the seam is visible.

Usage:
  blender --background --python hand_grip_diag.py -- <glb>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

FINGERS = ["index", "middle", "ring", "pinky"]


def load(glb):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    return mesh, arm


def face_metrics(verts):
    """area, min_edge, max_edge for a polygon given world-space vert coords."""
    n = len(verts)
    # area via fan triangulation
    area = 0.0
    for i in range(1, n - 1):
        area += (verts[i] - verts[0]).cross(verts[i + 1] - verts[0]).length * 0.5
    edges = [(verts[i] - verts[(i + 1) % n]).length for i in range(n)]
    return area, min(edges), max(edges)


def in_finger_region(c, sc=1):
    xs = c.x * sc
    return xs > 0.842 and c.y > -0.030 and 0.50 < c.z < 0.575


def scan_rest(mesh):
    print("\n=== A) REST-POSE SLIVER / DEGENERATE SCAN (finger region, .L) ===")
    me = mesh.data
    mw = mesh.matrix_world
    flagged = []
    nfaces = 0
    for p in me.polygons:
        vs = [mw @ me.vertices[i].co for i in p.vertices]
        c = sum(vs, Vector()) / len(vs)
        if not in_finger_region(c, 1):
            continue
        nfaces += 1
        area, mn, mx = face_metrics(vs)
        aspect = (mx / mn) if mn > 1e-9 else 9e9
        # sliver: extreme aspect OR tiny area OR near-zero min edge
        if aspect > 8.0 or area < 2.0e-6 or mn < 6.0e-4:
            flagged.append((p.index, c, area, mn, mx, aspect,
                            [i for i in p.vertices]))
    print("finger-region faces scanned: %d" % nfaces)
    print("flagged (aspect>8 or area<2e-6 or min_edge<6e-4): %d" % len(flagged))
    flagged.sort(key=lambda t: -t[5])
    for (pi, c, area, mn, mx, asp, vids) in flagged[:25]:
        print("  face %6d  c=(%.4f,%+.4f,%.4f) area=%.2e minE=%.2e maxE=%.2e asp=%6.1f verts=%s"
              % (pi, c.x, c.y, c.z, area, mn, mx, asp, vids))
    return flagged


def scan_grip_stretch(mesh, arm):
    print("\n=== B) GRIP-POSE DEFORMATION STRETCH (finger region near bar top) ===")
    bx, bz, r = H.GRIP_BAR
    # rest areas keyed by poly index
    me = mesh.data
    mw = mesh.matrix_world
    rest_area = {}
    for p in me.polygons:
        vs = [mw @ me.vertices[i].co for i in p.vertices]
        c = sum(vs, Vector()) / len(vs)
        if in_finger_region(c, 1):
            a, _, _ = face_metrics(vs)
            rest_area[p.index] = (a, c)
    # pose grip and evaluate
    H.pose_grip(arm, ".L")
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    mwe = mesh.matrix_world
    rows = []
    for p in dm.polygons:
        if p.index not in rest_area:
            continue
        vs = [mwe @ dm.vertices[i].co for i in p.vertices]
        c = sum(vs, Vector()) / len(vs)
        # near the bar surface AND at/above bar centre (the contact top region)
        d_axis = math.hypot(c.x - bx, c.z - bz)
        if d_axis > r + 0.020 or c.z < bz - 0.004:
            continue
        da, _, _ = face_metrics(vs)
        ra, rc = rest_area[p.index]
        ratio = (da / ra) if ra > 1e-9 else 9e9
        rows.append((p.index, ratio, ra, da, c, rc, d_axis))
    ev.to_mesh_clear()
    # worst stretches / collapses
    rows.sort(key=lambda t: -abs(math.log(max(t[1], 1e-6))))
    print("faces near bar-top contact: %d" % len(rows))
    print("worst 25 by |log(area ratio)| (ratio>>1 stretch, <<1 collapse/pinch):")
    for (pi, ratio, ra, da, c, rc, dax) in rows[:25]:
        print("  face %6d ratio=%7.2f restA=%.2e defA=%.2e  world=(%.4f,%+.4f,%.4f) rest=(%.4f,%+.4f,%.4f) dax=%.4f"
              % (pi, ratio, ra, da, c.x, c.y, c.z, rc.x, rc.y, rc.z, dax))
    H.reset_pose(arm)
    return rows


def scan_weights(mesh):
    print("\n=== C) WEIGHTS across index/middle boundary at fingertips (.L) ===")
    # index/middle gap y:
    _LANE = H._LANE
    gap_im = H.FY_MIN + 1 * _LANE
    print("index center=%.4f middle center=%.4f gap=%.4f"
          % (H.CENTERS['index'], H.CENTERS['middle'], gap_im))
    me = mesh.data
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}
    # collect verts near the gap, across a range of X (proximal -> tip)
    sel = []
    for v in me.vertices:
        c = v.co
        xs = c.x  # .L side sc=1
        if xs < 0.86 or not (0.50 < c.z < 0.575):
            continue
        if abs(c.y - gap_im) > 0.010:
            continue
        ws = sorted(((gi2name.get(g.group, str(g.group)), g.weight)
                     for g in v.groups), key=lambda kv: -kv[1])
        sel.append((v.index, c.copy(), ws[:3]))
    sel.sort(key=lambda t: (round(t[1].x, 3), t[1].y))
    print("verts within 10mm of index/middle seam, xs>=0.86: %d" % len(sel))
    for (vi, c, ws) in sel:
        wtxt = "  ".join("%s=%.2f" % (n, w) for n, w in ws)
        print("  v%6d (%.4f,%+.4f,%.4f)  %s" % (vi, c.x, c.y, c.z, wtxt))


def main():
    glb = sys.argv[sys.argv.index("--") + 1]
    mesh, arm = load(glb)
    scan_rest(mesh)
    scan_weights(mesh)
    scan_grip_stretch(mesh, arm)
    print("\nDIAG_DONE")


if __name__ == "__main__":
    main()
