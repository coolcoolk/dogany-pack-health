"""hand_reweight_thumbbase.py -- ROUND 6 WEIGHT-ONLY fix for the thumb-base grip hole.

Diagnosis (hand_thumbbase_diag.py): under the grip pose a black jagged cavity opens
at the BASE of the thumb (v4-rest has none). Cause is a SKINNING weight cliff, NOT a
topology hole -- the faces bridging the seam exist and stretch 3.4-6.6x in area, so
the mesh is connected; there is no open boundary to bridge. The cliff is
reweight_hand's hard `is_thumb: y < -0.030` cutoff: verts below it were skinned to
the thumb chain, verts above it kept their ORIGINAL palm weights with ~zero thumb
weight. Mean hand.L weight jumps 0.17 (y=-0.03) -> 0.69 (y=-0.02) across one row.
Under the thumb's grip adduction+curl the thumb-side verts follow the thumb while the
palm-side verts stay put, so the bridge faces over-stretch into thin/back-facing
slivers and the dark interior shows through = the "hole".

Round 4 (hand_reweight_thumb) rewrote only thumb-DOMINATED verts (tw>=0.35), so the
palm side of the seam was never fixed. This round closes the cliff from the palm
side: for the palm-side web verts along the seam it blends in thumb_01..03 weight
with a smooth ramp (pure original palm deep in the hand -> full inverse-distance
hand/thumb gradient at the seam), using the SAME inverse-distance-to-bone-segment
field the rig was skinned with. So the palm verts partially follow the thumb and the
bridge faces no longer tear.

Surgical discipline (mirrors round-3 hand_reweight_base):
  * touches ONLY palm-side web verts near the seam (thumb_total < THUMB_DOM so the
    accepted round-4 thumb verts are byte-identical; finger_total < FINGER_MAX so the
    round-3 knuckle / finger paddle is untouched).
  * REDISTRIBUTES only the hand+thumb portion of each vert's weight; every non-
    hand/thumb group (forearm etc.) is preserved exactly, and the total stays 1.
  * a proximity ramp keeps deep-palm verts at their ORIGINAL weights (byte-identical),
    so only the seam band changes.
  * does NOT re-run mesh surgery and does NOT touch bones, GRIP_CURL/GRIP_THUMB, or
    pose_spread.

Usage:
  blender --background --python hand_reweight_thumbbase.py -- \
     <in_glb> <out_glb> <out_low_glb> <grip_png> <crop_png> <export:0|1> [ramp_hi_y]
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

THUMB_DOM  = 0.35    # tw>=this -> accepted round-4 thumb vert, left untouched
FINGER_MAX = 0.15    # finger_total>=this -> finger paddle vert, left untouched
# palm-side seam band (local coords). x/z bound the thumb-base web; y spans from the
# seam (-0.033) up into the palm. The ramp fades the fix to zero by RAMP_HI_Y so the
# deep palm keeps its original weights (byte-identical outside the seam).
X_LO, X_HI = 0.730, 0.855
Y_SEAM     = -0.033
Y_RAMP_HI  = 0.028   # default; overridable arg. ramp=1 at seam -> 0 here (deep palm)
Z_LO, Z_HI = 0.478, 0.588

THUMB_BONES  = ("thumb_01", "thumb_02", "thumb_03")
FINGER_STEMS = ("index", "middle", "ring", "pinky")


def _smoothstep(t):
    t = H.clamp(t)
    return t * t * (3 - 2 * t)


def reweight_thumbbase(mesh, ramp_hi_y=Y_RAMP_HI, power=3.0, eps=0.006,
                       smooth_iters=6, smooth_factor=0.5):
    co = [v.co for v in mesh.data.vertices]
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}
    for s, sc in ((".L", 1), (".R", -1)):
        def V(x, y, z=H.MIDZ):
            return Vector((sc * x, y, z))

        palm_seg = (V(0.80, 0.02, 0.535), V(H.X_KNUCK, 0.02, 0.535))
        tpts = [V(0.760, -0.020), V(0.792, -0.042), V(0.820, -0.062), V(0.845, -0.078)]
        tsegs = [(tpts[i], tpts[i + 1]) for i in range(3)]
        hand_bn = "hand" + s
        tnames = [b + s for b in THUMB_BONES]
        ht_names = [hand_bn] + tnames
        bones = [(hand_bn, palm_seg),
                 (tnames[0], tsegs[0]), (tnames[1], tsegs[1]), (tnames[2], tsegs[2])]
        tgi = {mesh.vertex_groups[n].index for n in tnames if mesh.vertex_groups.get(n)}
        fgi = {mesh.vertex_groups["%s_0%d%s" % (stem, i, s)].index
               for stem in FINGER_STEMS for i in (1, 2, 3)
               if mesh.vertex_groups.get("%s_0%d%s" % (stem, i, s))}
        ht_gi = {mesh.vertex_groups[n].index for n in ht_names if mesh.vertex_groups.get(n)}

        # ---- select palm-side seam verts to blend ----
        region = {}          # vi -> (cap, orig_ht_fracs, ramp)
        for vi, v in enumerate(mesh.data.vertices):
            c = co[vi]
            xs = c.x * sc
            if not (X_LO < xs < X_HI and Y_SEAM < c.y < ramp_hi_y and Z_LO < c.z < Z_HI):
                continue
            gw = {g.group: g.weight for g in v.groups}
            tw = sum(w for gi, w in gw.items() if gi in tgi)
            fw = sum(w for gi, w in gw.items() if gi in fgi)
            if tw >= THUMB_DOM or fw >= FINGER_MAX:
                continue                       # keep round-4 thumb / round-3 fingers
            other = sum(w for gi, w in gw.items() if gi not in ht_gi)
            cap = H.clamp(1.0 - other, 0.0, 1.0)
            if cap <= 1e-4:
                continue
            orig = {n: gw.get(mesh.vertex_groups[n].index, 0.0)
                    for n in ht_names if mesh.vertex_groups.get(n)}
            otot = sum(orig.values()) or 1.0
            orig_frac = {n: w / otot for n, w in orig.items()}   # fractions of the ht mass
            ramp = _smoothstep((ramp_hi_y - c.y) / (ramp_hi_y - Y_SEAM))
            region[vi] = (cap, orig_frac, ramp)
        if not region:
            continue

        # recomputed inverse-distance hand/thumb split (same field the rig uses)
        wd = {}
        for vi, (cap, orig_frac, ramp) in region.items():
            c = co[vi]
            ws = [(bn, 1.0 / ((H._pt_seg_dist(c, a, b) + eps) ** power))
                  for bn, (a, b) in bones]
            tot = sum(w for _, w in ws) or 1.0
            rec = {bn: w / tot for bn, w in ws}
            blend = {n: (1.0 - ramp) * orig_frac.get(n, 0.0) + ramp * rec.get(n, 0.0)
                     for n in ht_names}
            btot = sum(blend.values()) or 1.0
            wd[vi] = {n: v / btot for n, v in blend.items()}    # fractions, sum 1

        # same-region Laplacian smoothing on the ht fractions (no cross-bleed out)
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

        # ---- write: replace ONLY hand+thumb groups, scaled to cap; keep others ----
        groups = {n: H._vg(mesh, n) for n in ht_names}
        written = 0
        for vi, frac in wd.items():
            cap = region[vi][0]
            v = mesh.data.vertices[vi]
            for gi in list({g.group for g in v.groups} & ht_gi):
                mesh.vertex_groups[gi].remove([vi])
            items = sorted(frac.items(), key=lambda kv: -kv[1])[:4]
            tot = sum(x for _, x in items) or 1.0
            for bn, ww in items:
                w = cap * ww / tot
                if w > 1e-4:
                    groups[bn].add([vi], w, 'REPLACE')
            written += 1
        print("  side %s thumb-base verts rewritten=%d" % (s, written))
    print("REWEIGHT_THUMBBASE_DONE band x[%.3f,%.3f] y(%.3f,%.3f] z[%.3f,%.3f] iters=%d"
          % (X_LO, X_HI, Y_SEAM, ramp_hi_y, Z_LO, Z_HI, smooth_iters))


# ---- QA: thumb-base seam face stretch + bar penetration + tip->index gap ----
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
    # seam-band faces (the ones that tore)
    def in_band(c):
        return (0.73 < c.x < 0.86 and -0.033 < c.y < 0.03 and 0.478 < c.z < 0.588)
    band_faces = [p for p in me.polygons
                  if any(in_band(me.vertices[vi].co) for vi in p.vertices)]

    rest_co = [mesh.matrix_world @ v.co for v in me.vertices]
    H.pose_grip(arm, ".L")
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    def_co = [mesh.matrix_world @ v.co for v in dm.vertices]

    def area(cc, vs):
        a = 0.0; o = cc[vs[0]]
        for i in range(1, len(vs) - 1):
            a += ((cc[vs[i]] - o).cross(cc[vs[i + 1]] - o)).length * 0.5
        return a
    ratios = []
    for p in band_faces:
        vs = list(p.vertices)
        ra = area(rest_co, vs); da = area(def_co, vs)
        if ra > 1e-9:
            ratios.append(da / ra)
    ratios.sort()
    n = len(ratios)
    p50 = ratios[n // 2]; p90 = ratios[int(0.9 * n)]; mx = ratios[-1]

    # bar penetration + tip->index (round-2 closure re-verify)
    co = def_co
    bx, bz, r = H.GRIP_BAR
    inside = deep = 0; mind = 1e9
    for vi in tvi:
        c = co[vi]
        d = math.hypot(c.x - bx, c.z - bz)
        if d < r - 0.0015:
            inside += 1
            if d < 0.45 * r:
                deep += 1
            mind = min(mind, d)
    tipbone = mesh.matrix_world @ arm.pose.bones["thumb_03.L"].tail
    tpts = [co[vi] for vi in tvi]
    tipcluster = [p for p in tpts if (p - tipbone).length < 0.025]
    ipts = [co[vi] for vi in ivi]
    best = 1e9
    for tp in (tipcluster or tpts):
        for ip in ipts:
            best = min(best, (tp - ip).length)
    ev.to_mesh_clear()
    print("QA seam-stretch faces=%d p50=%.2f p90=%.2f max=%.2f | PEN inside=%d deep=%d "
          "deepest=%.4f(r=%.4f) | tip->index=%.4f (%.1fmm)"
          % (n, p50, p90, mx, inside, deep, mind if inside else r, r, best, best * 1060))


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
    ramp_hi = float(a[6]) if len(a) > 6 else Y_RAMP_HI

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

    print("--- BEFORE ---"); qa(mesh, arm); H.reset_pose(arm)
    reweight_thumbbase(mesh, ramp_hi_y=ramp_hi)
    print("--- AFTER ---"); qa(mesh, arm); H.reset_pose(arm)

    bar = add_bar()
    H.pose_grip(arm, ".L")
    sc = bpy.context.scene
    H._studio(sc)
    sc.render.resolution_x = sc.render.resolution_y = 1200
    H._cam((0.98, -0.40, 0.66), (0.845, 0.0, 0.512), lens=78)
    sc.render.filepath = chk_grip
    bpy.ops.render.render(write_still=True)
    print("CHECK_GRIP", chk_grip)
    sc.render.resolution_x = sc.render.resolution_y = 900
    H._cam((0.98, -0.40, 0.66), (0.822, -0.03, 0.505), lens=150)
    sc.render.filepath = chk_crop
    bpy.ops.render.render(write_still=True)
    print("CHECK_CROP", chk_crop)
    bpy.data.objects.remove(bar, do_unlink=True)

    if do_export:
        H.export_full(out, arm, mesh)
        print("EXPORTED_FULL", out, os.path.getsize(out))
        H.export_lowpoly(out_low, arm, mesh)
        print("EXPORTED_LOW", out_low, os.path.getsize(out_low))
    print("REWEIGHT_THUMBBASE_MAIN_DONE")


if __name__ == "__main__":
    main()
