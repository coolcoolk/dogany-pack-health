"""hand_reweight_thumb.py -- ROUND 4 WEIGHT-ONLY fix for the "wave under the thumb".

Diagnosis (hand_thumb_probe.py): the ripple under the thumb is a POSE-DEFORMATION
skinning artifact at the thumb's inter-phalangeal joints, NOT rest geometry. The
worst verts sit on the thumb UNDERSIDE (rest z~0.495-0.527, below MIDZ) at the
thumb_01<->thumb_02 / 02<->03 joints with ~50/50 weight splits: rest Laplacian is
tiny (0.0003-0.0027) but deformed Laplacian is 4-33x higher. Two compounding
causes:
  (a) sharp inverse-distance joint bands (power=3): verts straddling two thumb
      bones at ~50/50 fold into a crease when the joint curls 46/48 deg; and
  (b) a WEIGHTING-SCHEME SEAM at reweight_hand's is_thumb y<-0.030 cutoff -- verts
      just above the cutoff kept their ORIGINAL (pre-surgery) weights while the
      ones below were rewritten, so the two schemes meet in a ridge on the thumb
      underside.

Fix (analogous to round-3's knuckle reweight, but for the thumb chain): select
ALL thumb-DOMINATED verts by weight (unifies both sides of the seam), recompute
their weights with the SAME inverse-distance field reweight_hand uses (so the
overall bone mass -- and thus the accepted round-2 tip position -- is preserved),
then apply HEAVIER same-thumb Laplacian smoothing so each joint transition spreads
over several rings instead of folding into a ripple. Writes ONLY thumb-dominated
verts; fingers, palm, and the round-3 knuckle band are byte-identical. Does NOT
touch bones, GRIP_CURL, GRIP_THUMB, or pose_spread.

Usage:
  blender --background --python hand_reweight_thumb.py -- \
     <in_glb> <out_glb> <out_low_glb> <grip_png> <crop_png> <export:0|1> [iters]
Prints QA: thumb deformed-Laplacian p90/max, bar penetration (inside/deep verts),
and thumb-tip -> index-mesh gap, so round-2 closure is re-verified numerically.
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

THUMB_DOM = 0.35   # a vert is "thumb" if sum(thumb_01..03 weight) exceeds this


def _thumb_segs(sc, side):
    def V(x, y, z=H.MIDZ):
        return Vector((sc * x, y, z))
    pts = [V(0.760, -0.020), V(0.792, -0.042), V(0.820, -0.062), V(0.845, -0.078)]
    return (V(0.80, 0.02, 0.535), V(H.X_KNUCK, 0.02, 0.535)), \
           [(pts[i], pts[i + 1]) for i in range(3)]


def reweight_thumb(mesh, power=3.0, eps=0.006, smooth_iters=16, smooth_factor=0.5):
    co = [v.co for v in mesh.data.vertices]
    for s, sc in ((".L", 1), (".R", -1)):
        tnames = ["thumb_01" + s, "thumb_02" + s, "thumb_03" + s]
        tgi = {mesh.vertex_groups[n].index for n in tnames if mesh.vertex_groups.get(n)}
        # thumb-dominated verts (by current weight): both sides of the is_thumb seam
        region = {}
        for vi, v in enumerate(mesh.data.vertices):
            tw = sum(g.weight for g in v.groups if g.group in tgi)
            if tw <= THUMB_DOM:
                continue
            region[vi] = True
        if not region:
            continue
        palm_seg, tsegs = _thumb_segs(sc, s)
        bones = [("hand" + s, palm_seg),
                 ("thumb_01" + s, tsegs[0]),
                 ("thumb_02" + s, tsegs[1]),
                 ("thumb_03" + s, tsegs[2])]
        wd = {}
        for vi in region:
            c = co[vi]
            ws = [(bn, 1.0 / ((H._pt_seg_dist(c, a, b) + eps) ** power))
                  for bn, (a, b) in bones]
            tot = sum(w for _, w in ws) or 1.0
            wd[vi] = {bn: w / tot for bn, w in ws}
        # same-region adjacency; heavy Laplacian smoothing spreads the joint bands
        adj = {vi: set() for vi in wd}
        for e in mesh.data.edges:
            a, b = e.vertices
            if a in wd and b in wd:
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

        names = ["hand" + s] + tnames
        clear_idx = {mesh.vertex_groups[n].index for n in names
                     if mesh.vertex_groups.get(n)}
        groups = {n: H._vg(mesh, n) for n in names}
        written = 0
        for vi, w in wd.items():
            v = mesh.data.vertices[vi]
            for gi in list({g.group for g in v.groups} & clear_idx):
                mesh.vertex_groups[gi].remove([vi])
            items = sorted(w.items(), key=lambda kv: -kv[1])[:4]
            tot = sum(x for _, x in items) or 1.0
            for bn, ww in items:
                if ww / tot > 1e-4:
                    groups[bn].add([vi], ww / tot, 'REPLACE')
            written += 1
        print("  side %s thumb-verts rewritten=%d" % (s, written))
    print("REWEIGHT_THUMB_DONE iters=%d power=%.1f" % (smooth_iters, power))


# ---- QA: thumb deformed-laplacian + bar penetration + tip->index gap ----
def qa(mesh, arm):
    me = mesh.data
    tgi = {mesh.vertex_groups[n].index for n in
           ("thumb_01.L", "thumb_02.L", "thumb_03.L") if mesh.vertex_groups.get(n)}
    igi = {mesh.vertex_groups[n].index for n in
           ("index_01.L", "index_02.L", "index_03.L") if mesh.vertex_groups.get(n)}
    tvi = [v.index for v in me.vertices
           if any(g.group in tgi and g.weight > 0.3 for g in v.groups)]
    ivi = [v.index for v in me.vertices
           if any(g.group in igi and g.weight > 0.3 for g in v.groups)]
    adj = {}
    for e in me.edges:
        a, b = e.vertices
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    H.pose_grip(arm, ".L")
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    mw = mesh.matrix_world
    co = [mw @ v.co for v in dm.vertices]
    lap = []
    for vi in tvi:
        nb = adj.get(vi, ())
        if nb:
            m = sum((co[n] for n in nb), Vector()) / len(nb)
            lap.append((co[vi] - m).length)
    lap.sort()
    n = len(lap)
    p90 = lap[int(0.9 * n)]; mx = lap[-1]; mean = sum(lap) / n
    bx, bz, r = H.GRIP_BAR
    inside = deep = 0; mind = 1e9
    tpts = []
    for vi in tvi:
        c = co[vi]; tpts.append(c)
        d = math.hypot(c.x - bx, c.z - bz)
        if d < r - 0.0015:
            inside += 1
            if d < 0.45 * r:
                deep += 1
            mind = min(mind, d)
    tipbone = mw @ arm.pose.bones["thumb_03.L"].tail
    tipcluster = [p for p in tpts if (p - tipbone).length < 0.025]
    ipts = [co[vi] for vi in ivi]
    best = 1e9
    for tp in (tipcluster or tpts):
        for ip in ipts:
            best = min(best, (tp - ip).length)
    ev.to_mesh_clear()
    print("QA thumb-lap mean=%.5f p90=%.5f max=%.5f | PEN inside=%d deep=%d "
          "deepest=%.4f(r=%.4f) | tip->index=%.4f (%.1fmm)"
          % (mean, p90, mx, inside, deep, mind if inside else r, r, best, best * 1060))


def add_bar():
    bx, bz, r = H.GRIP_BAR
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
    return bar


def main():
    a = sys.argv[sys.argv.index("--") + 1:]
    src, out, out_low, chk_grip, chk_crop = a[:5]
    do_export = a[5] == "1"
    iters = int(a[6]) if len(a) > 6 else 16

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

    print("--- BEFORE ---"); qa(mesh, arm)
    reweight_thumb(mesh, smooth_iters=iters)
    print("--- AFTER ---"); qa(mesh, arm)

    bar = add_bar()
    H.pose_grip(arm, ".L")
    sc = bpy.context.scene
    H._studio(sc)
    sc.render.resolution_x = sc.render.resolution_y = 1200
    H._cam((0.98, -0.40, 0.66), (0.845, 0.0, 0.512), lens=78)
    sc.render.filepath = chk_grip
    bpy.ops.render.render(write_still=True)
    print("CHECK_GRIP", chk_grip)
    sc.render.resolution_x = sc.render.resolution_y = 700
    H._cam((0.98, -0.40, 0.66), (0.828, -0.02, 0.520), lens=135)
    sc.render.filepath = chk_crop
    bpy.ops.render.render(write_still=True)
    print("CHECK_CROP", chk_crop)
    bpy.data.objects.remove(bar, do_unlink=True)

    if do_export:
        H.export_full(out, arm, mesh)
        print("EXPORTED_FULL", out, os.path.getsize(out))
        H.export_lowpoly(out_low, arm, mesh)
        print("EXPORTED_LOW", out_low, os.path.getsize(out_low))
    print("REWEIGHT_THUMB_MAIN_DONE")


if __name__ == "__main__":
    main()
