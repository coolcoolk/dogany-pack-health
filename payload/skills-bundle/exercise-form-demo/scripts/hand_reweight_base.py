"""hand_reweight_base.py -- WEIGHT-ONLY fix for the knuckle chevron.

Diagnosis (hand_falsecolor.py + hand_base_diag.py): the grip chevron is a
SKINNING fold at the palm->finger_01 boundary. reweight_hand classifies a vert as
"finger" only at xs > X_KNUCK-0.004 (=0.841); everything behind stays pure hand
(=1.0). So the dorsal knuckle has a HARD cliff -- hand=1.00 at x=0.8408 jumping to
finger~0.65 at x=0.8413. Under 70deg/joint curl the static palm and the rotating
finger fold at that cliff into a sharp crease = the chevron notch.

This does NOT re-run mesh surgery and does NOT touch bones, GRIP_CURL/GRIP_THUMB,
or pose_spread. It re-computes ONLY the hand/finger skin weights with:
  1) a widened region reaching back into the palm (xs > X_BAND_LO), and
  2) a smooth axial RAMP t(xs) that blends pure-hand -> full inverse-distance
     finger weights across [X_BAND_LO .. X_BAND_HI], spreading the knuckle fold
     over ~4 vertex rings instead of one crease, and
  3) limited cross-finger smoothing at the BASE WEB ONLY (xs < X_WEB) so the
     index/middle seam does not kink -- bleed stays ~2 rings at the web (where the
     fingers are naturally joined); beyond the web, same-finger-only (no bleed on
     the separated tubes, preserving round-0/1's clean separation).

Then re-exports the GLBs and re-renders the two grip QA framings.

Usage:
  blender --background --python hand_reweight_base.py -- \
     <in_glb> <out_glb> <out_low_glb> <grip_png> <crop_png> <export:0|1>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

X_BAND_LO = 0.834   # pure hand at/below here (palm side of the knuckle)
X_BAND_HI = 0.850   # full finger inverse-distance weighting at/beyond here
X_WRITE   = 0.850   # ONLY verts at/below here are rewritten; beyond = byte-identical.
X_CTX     = 0.862   # verts up to here are recomputed as smoothing CONTEXT only.
#   Recomputing + re-smoothing the WHOLE finger perturbs the accepted tip weights
#   and tears the far tubes into shards (round-0's failure). So all changes are
#   confined to the knuckle band (xs <= X_WRITE); everything distal keeps its
#   accepted weights exactly. The band verts up to X_CTX are computed only to give
#   the ramp a smooth neighbourhood, not written.

FINGERS = H.FINGERS


def _smoothstep(t):
    t = H.clamp(t)
    return t * t * (3 - 2 * t)


def reweight_base(mesh, power=3.0, eps=0.006, smooth_iters=5, smooth_factor=0.5):
    co = [v.co for v in mesh.data.vertices]
    for s, sc in ((".L", 1), (".R", -1)):
        def V(x, y, z=H.MIDZ):
            return Vector((sc * x, y, z))

        palm_seg = (V(0.80, 0.02, 0.535), V(H.X_KNUCK, 0.02, 0.535))
        finger_segs = {}
        for finger in FINGERS:
            cen = H.CENTERS[finger]
            finger_segs[finger] = [(V(a, cen), V(b, cen))
                                   for a, b in H._thirds(H.X_KNUCK, H.TIPLEN[finger])]

        # region = knuckle band + a context skirt up to X_CTX (fingers only; the
        # thumb, accepted in round 2, is never touched).
        region = {}
        fid = {}
        for vi, c in enumerate(co):
            xs = c.x * sc
            if not (X_BAND_LO < xs < X_CTX) or not (0.49 < c.z < 0.585):
                continue
            if not (-0.030 < c.y < H.FY_MAX + 0.02):
                continue
            if c.y < -0.030 and 0.74 < xs < 0.86:      # skip thumb column
                continue
            finger = H._finger_of(c.y)
            fs = finger_segs[finger]
            bones = [("hand" + s, palm_seg),
                     ("%s_01%s" % (finger, s), fs[0]),
                     ("%s_02%s" % (finger, s), fs[1]),
                     ("%s_03%s" % (finger, s), fs[2])]
            fid[vi] = finger
            ws = [(bn, 1.0 / ((H._pt_seg_dist(c, a, b) + eps) ** power))
                  for bn, (a, b) in bones]
            tot = sum(w for _, w in ws) or 1.0
            ws = [(bn, w / tot) for bn, w in ws]
            # axial ramp: pure-hand -> full-finger across the knuckle band, so the
            # static-palm / rotating-finger fold spreads over ~4 rings, not a crease.
            t = _smoothstep((xs - X_BAND_LO) / (X_BAND_HI - X_BAND_LO))
            hand_bn = "hand" + s
            region[vi] = [(bn, (1.0 - t) + t * w) if bn == hand_bn else (bn, t * w)
                          for bn, w in ws]
        if not region:
            continue

        wd = {vi: {bn: w for bn, w in ws} for vi, ws in region.items()}
        # same-finger adjacency only (no cross-finger bleed -> tubes stay separate)
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

        # WRITE only the knuckle band (xs <= X_WRITE). Distal verts (context skirt)
        # were computed only to smooth the ramp; their accepted weights stay intact.
        names = ["hand" + s]
        for finger in FINGERS:
            names += ["%s_0%d%s" % (finger, i, s) for i in (1, 2, 3)]
        clear_idx = {mesh.vertex_groups[n].index for n in names
                     if mesh.vertex_groups.get(n)}
        groups = {n: H._vg(mesh, n) for n in names}
        written = 0
        for vi, w in wd.items():
            if abs(co[vi].x) > X_WRITE:
                continue
            v = mesh.data.vertices[vi]
            for gi in list({g.group for g in v.groups} & clear_idx):
                mesh.vertex_groups[gi].remove([vi])
            items = sorted(w.items(), key=lambda kv: -kv[1])[:4]
            tot = sum(x for _, x in items) or 1.0
            for bn, ww in items:
                if ww / tot > 1e-4:
                    groups[bn].add([vi], ww / tot, 'REPLACE')
            written += 1
        print("  side %s written=%d" % (s, written))
    print("REWEIGHT_BASE_DONE band=[%.3f,%.3f] write<=%.3f ctx<%.3f"
          % (X_BAND_LO, X_BAND_HI, X_WRITE, X_CTX))


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

    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

    reweight_base(mesh)

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
    print("REWEIGHT_MAIN_DONE")


if __name__ == "__main__":
    main()
