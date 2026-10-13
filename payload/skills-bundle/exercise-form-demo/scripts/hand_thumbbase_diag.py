"""hand_thumbbase_diag.py -- ROUND 6 DIAGNOSTIC: classify the thumb-base grip hole.

Owner/orchestrator flagged a black jagged cavity that opens at the BASE of the
thumb ONLY under the grip pose (v4-rest has no hole, round5 waterfall renders).
This harness classifies WHY, reusing the Laplacian rest-vs-deformed method from
hand_grip_diag2.py / hand_thumb_probe.py, and adds two things those lacked for a
"hole": a TOPOLOGY check (are the cavity-boundary edges genuinely open/unwelded in
the REST mesh, or is the mesh closed and the hole only appears under deform?) and a
per-FACE stretch metric (which faces blow up in area under the grip -> the tearing
faces), so the fix region is pinned exactly.

Region = the thumb-base WEB spanning BOTH sides of the reweight_hand is_thumb
seam (y = -0.030): xs in [0.72,0.87], y in [-0.085,+0.055], z in [0.475,0.590].

Outputs:
  * boundary-edge count in region (REST) -> >0 means a real topology hole.
  * worst faces by deformed/rest area ratio, with the vert weights on them.
  * hand-weight vs y buckets across the seam -> shows the cliff sharpness.

Usage: blender --background --python hand_thumbbase_diag.py -- <glb>
"""
import bpy, sys, os, collections
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H


def in_region(c, sc):
    xs = c.x * sc
    return (0.72 < xs < 0.87 and -0.085 < c.y < 0.055 and 0.475 < c.z < 0.590)


def main():
    glb = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    me = mesh.data
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}

    def wmap(vi):
        return {gi2name[g.group]: g.weight for g in me.vertices[vi].groups}

    # region verts (.L side, sc=1)
    region = set(v.index for v in me.vertices if in_region(v.co, 1))
    print("region verts=%d" % len(region))

    # ---- topology: boundary edges (1 incident face) inside the region (REST) ----
    face_count = collections.Counter()
    for p in me.polygons:
        vs = list(p.vertices)
        for i in range(len(vs)):
            a, b = vs[i], vs[(i + 1) % len(vs)]
            face_count[frozenset((a, b))] += 1
    region_boundary = 0
    for e, n in face_count.items():
        a, b = tuple(e)
        if n == 1 and a in region and b in region:
            region_boundary += 1
    print("REST boundary edges in region (open-seam / real hole indicator) = %d"
          % region_boundary)

    # ---- per-face stretch: rest area vs grip-deformed area ----
    rest_co = [mesh.matrix_world @ v.co for v in me.vertices]
    H.pose_grip(arm, ".L")
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    def_co = [mesh.matrix_world @ v.co for v in dm.vertices]

    def poly_area(co, vs):
        # fan triangulation area
        a = 0.0
        o = co[vs[0]]
        for i in range(1, len(vs) - 1):
            a += ((co[vs[i]] - o).cross(co[vs[i + 1]] - o)).length * 0.5
        return a

    rows = []
    for p in me.polygons:
        vs = list(p.vertices)
        if not any(vi in region for vi in vs):
            continue
        ra = poly_area(rest_co, vs)
        da = poly_area(def_co, vs)
        ratio = da / ra if ra > 1e-9 else 0.0
        rows.append((ratio, p.index, vs, ra, da))
    ev.to_mesh_clear()
    rows.sort(reverse=True)

    print("\nworst 20 faces by grip stretch (def_area/rest_area):")
    print("  ratio  rest->def area          face vert weights (hand/th1/th2/th3/idx1)")
    for ratio, pi, vs, ra, da in rows[:20]:
        c = sum((rest_co[vi] for vi in vs), Vector()) / len(vs)
        wsum = collections.defaultdict(float)
        for vi in vs:
            for k, w in wmap(vi).items():
                wsum[k] += w / len(vs)
        def g(k):
            return wsum.get(k, 0.0)
        print("  %5.1f  %.2e->%.2e  @(%.3f,%+.3f,%.3f) h=%.2f t1=%.2f t2=%.2f t3=%.2f i1=%.2f"
              % (ratio, ra, da, c.x, c.y, c.z,
                 g("hand.L"), g("thumb_01.L"), g("thumb_02.L"), g("thumb_03.L"),
                 g("index_01.L")))

    # ---- hand-weight vs y across the seam (thumb-base column xs in [0.76,0.83]) ----
    print("\nhand.L weight vs y (seam at y=-0.030), xs in [0.76,0.83]:")
    buck = collections.defaultdict(list)
    for vi in region:
        c = me.vertices[vi].co
        if 0.76 < c.x < 0.83:
            buck[round(c.y * 100)].append(wmap(vi).get("hand.L", 0.0))
    for k in sorted(buck):
        vals = buck[k]
        print("  y~%+.2f  meanHand=%.2f  n=%d" % (k / 100.0, sum(vals) / len(vals), len(vals)))
    print("\nTHUMBBASE_DIAG_DONE")


if __name__ == "__main__":
    main()
