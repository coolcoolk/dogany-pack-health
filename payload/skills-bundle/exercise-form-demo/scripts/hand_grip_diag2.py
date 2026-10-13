"""hand_grip_diag2.py -- pinpoint the chevron flap verts + classify the cause.

For each fingertip-region vert (.L), compute the Laplacian magnitude = |co - mean(
edge-neighbours)| in the REST mesh and again in the GRIP-DEFORMED mesh.
  * spiky in BOTH rest & deformed  -> rest-geometry outlier (mesh sliver/flap).
  * smooth in rest, spiky deformed  -> skinning-induced protrusion (weights).
Prints the worst verts by deformed Laplacian, with rest Laplacian, weights, and
whether the vert is a rest outlier.

Usage:
  blender --background --python hand_grip_diag2.py -- <glb>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H


def build_adj(me):
    adj = {}
    for e in me.edges:
        a, b = e.vertices
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return adj


def lap(co_list, adj, idxs):
    out = {}
    for vi in idxs:
        nb = adj.get(vi, ())
        if not nb:
            out[vi] = 0.0
            continue
        m = Vector()
        for n in nb:
            m += co_list[n]
        m /= len(nb)
        out[vi] = (co_list[vi] - m).length
    return out


def main():
    glb = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    me = mesh.data
    mw = mesh.matrix_world
    adj = build_adj(me)
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}

    # fingertip region (.L): index/middle tips, x in [0.88,0.94], the curl zone
    rest_co = [mw @ v.co for v in me.vertices]
    idxs = [v.index for v in me.vertices
            if 0.875 < (mw @ v.co).x < 0.945
            and -0.020 < (mw @ v.co).y < 0.030
            and 0.505 < (mw @ v.co).z < 0.575]
    rest_lap = lap(rest_co, adj, idxs)

    # deform
    H.pose_grip(arm, ".L")
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    def_co = [mesh.matrix_world @ v.co for v in dm.vertices]
    def_lap = lap(def_co, adj, idxs)
    ev.to_mesh_clear()
    H.reset_pose(arm)

    rl = sorted(rest_lap.values())
    dl = sorted(def_lap.values())
    def pct(a, p):
        return a[int(p * (len(a) - 1))]
    print("region verts: %d" % len(idxs))
    print("REST  lap median=%.2e p90=%.2e p99=%.2e max=%.2e"
          % (pct(rl, .5), pct(rl, .9), pct(rl, .99), rl[-1]))
    print("DEFRM lap median=%.2e p90=%.2e p99=%.2e max=%.2e"
          % (pct(dl, .5), pct(dl, .9), pct(dl, .99), dl[-1]))
    rest_p95 = pct(rl, .95)

    rows = sorted(idxs, key=lambda vi: -def_lap[vi])[:30]
    print("\nworst 30 verts by DEFORMED laplacian:")
    print("  vert       rest_pos                 def_lap   rest_lap  rest_outlier?  weights")
    for vi in rows:
        v = me.vertices[vi]
        c = mw @ v.co
        ws = sorted(((gi2name.get(g.group, str(g.group)), g.weight)
                     for g in v.groups), key=lambda kv: -kv[1])[:3]
        wtxt = " ".join("%s=%.2f" % (n, w) for n, w in ws)
        outl = "REST-OUTLIER" if rest_lap[vi] > rest_p95 else "rest-smooth"
        print("  v%-7d (%.4f,%+.4f,%.4f)  d=%.2e r=%.2e  %-12s  %s"
              % (vi, c.x, c.y, c.z, def_lap[vi], rest_lap[vi], outl, wtxt))
    print("\nDIAG2_DONE")


if __name__ == "__main__":
    main()
