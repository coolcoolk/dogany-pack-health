"""hand_regrip_v3.py -- fix the grouped-finger hand so a closed bar-grip deforms
CLEANLY instead of crushing into a shard blob.

Problem (v2): the hand is a grouped-finger rig -- the 4 fingers are one fused
paddle driven by two bones (fingers_01/02) with HARD-partitioned skin weights.
When curled to wrap a bar the two hard weight boundaries pinch and the mesh
collapses into a crushed blob with shards.

Fix (v3), two parts:
  1) BONES: rebuild the grouped fingers as THREE segments (fingers_01/02/03 =
     MCP + PIP + DIP curl joints) so the wrap curl distributes over 3 gentle
     bends instead of 2 hard ones (same idea as forearm_twist distributing roll).
  2) WEIGHTS: replace the hard-partitioned finger/thumb weights with smooth
     inverse-distance weights + Laplacian smoothing across the hand region, then
     cap to 4 influences and normalize. The crush was mainly a skinning problem;
     smooth normalized falloff removes the pinch. Palm/wrist verts are left
     untouched so the rest of the body rig is preserved exactly.

Per-finger articulation is NOT attempted (the mesh's 4 fingers are fused -- no
per-finger separation to skin). Target = a smooth GROUPED wrap (loose fist /
hook grip), which is the ceiling for this mesh.

Usage (headless):
  blender --background --python hand_regrip_v3.py -- <in_v2.glb> <out_v3.glb> <check.png> <tag>
The rig is exported in BIND pose (textures embedded). A zoomed grip-check crop
is rendered to <check.png> BEFORE reset so reviewers can see the closed grip.

Coordinate frame (as imported from the v2 glb): X = left(+)/right(-) along the
arm, Y = front(-)/back(+), Z = up. Local along-arm coord xs = x * side_sign.
"""
import bpy, sys, math
from mathutils import Vector, Matrix

# ---- finger 3-segment layout along the finger centerline (local coords) ----
FKNUCK, FTIP, FZ, FY = 0.845, 0.928, 0.535, 0.03


def _seg_bounds():
    a, b = FKNUCK, FTIP
    return [(a, a + (b - a) / 3.0), (a + (b - a) / 3.0, a + 2 * (b - a) / 3.0),
            (a + 2 * (b - a) / 3.0, b)]


def rebuild_finger_bones(arm):
    """Reposition fingers_01/02 into equal thirds and add fingers_03 so the
    grouped fingers curl at 3 joints. Per side; keeps chain hand->01->02->03."""
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='EDIT')
    eb = arm.data.edit_bones
    segs = _seg_bounds()
    for s, sc in ((".L", 1), (".R", -1)):
        def pt(x):
            return Vector((sc * x, FY, FZ))
        f1, f2 = eb.get("fingers_01" + s), eb.get("fingers_02" + s)
        f1.head, f1.tail = pt(segs[0][0]), pt(segs[0][1])
        f2.head, f2.tail = pt(segs[1][0]), pt(segs[1][1])
        f2.parent, f2.use_connect = f1, True
        f3 = eb.get("fingers_03" + s) or eb.new("fingers_03" + s)
        f3.head, f3.tail = pt(segs[2][0]), pt(segs[2][1])
        f3.parent, f3.use_connect, f3.use_deform = f2, True, True
    bpy.ops.object.mode_set(mode='OBJECT')


def _pt_seg_dist(p, a, b):
    ab = b - a
    d = ab.dot(ab)
    t = max(0.0, min(1.0, (p - a).dot(ab) / d)) if d > 1e-12 else 0.0
    return (p - (a + ab * t)).length


def _vg(mesh, name):
    return mesh.vertex_groups.get(name) or mesh.vertex_groups.new(name=name)


def reweight_hand(mesh, power=3.0, eps=0.006, smooth_iters=6, smooth_factor=0.55):
    """Smooth inverse-distance skin weights for the finger + thumb region, then
    Laplacian-smooth, cap to 4 influences, normalize. Removes the hard weight
    boundaries that made the fingers crush when curled."""
    segs = _seg_bounds()
    co = [v.co for v in mesh.data.vertices]
    for s, sc in ((".L", 1), (".R", -1)):
        def pt(x, y=FY, z=FZ):
            return Vector((sc * x, y, z))
        palm = (pt(0.80, 0.02, 0.53), pt(0.845, 0.02, 0.53))
        f1 = (pt(segs[0][0]), pt(segs[0][1]))
        f2 = (pt(segs[1][0]), pt(segs[1][1]))
        f3 = (pt(segs[2][0]), pt(segs[2][1]))
        th1 = (pt(0.76, -0.02, 0.53), pt(0.80, -0.05, 0.53))
        th2 = (pt(0.80, -0.05, 0.53), pt(0.842, -0.078, 0.53))
        finger_bones = [("hand" + s, palm), ("fingers_01" + s, f1),
                        ("fingers_02" + s, f2), ("fingers_03" + s, f3)]
        thumb_bones = [("hand" + s, palm), ("thumb_01" + s, th1),
                       ("thumb_02" + s, th2)]
        region = {}
        for vi, c in enumerate(co):
            xs = c.x * sc
            if xs < 0.79 or not (0.45 < c.z < 0.62):
                continue
            is_thumb = (c.y < -0.028 and 0.74 < xs < 0.865)
            is_finger = (xs > 0.836 and not is_thumb)
            if not (is_thumb or is_finger):
                continue
            bones = thumb_bones if is_thumb else finger_bones
            region[vi] = [(bn, 1.0 / ((_pt_seg_dist(c, a, b) + eps) ** power))
                          for bn, (a, b) in bones]
        if not region:
            continue
        for vi, ws in region.items():
            tot = sum(w for _, w in ws)
            region[vi] = [(bn, w / tot) for bn, w in ws]
        wd = {vi: {bn: w for bn, w in ws} for vi, ws in region.items()}
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
        clear_names = ["hand" + s, "fingers_01" + s, "fingers_02" + s,
                       "fingers_03" + s, "thumb_01" + s, "thumb_02" + s]
        clear_idx = {mesh.vertex_groups[n].index for n in clear_names
                     if mesh.vertex_groups.get(n)}
        groups = {n: _vg(mesh, n) for n in clear_names}
        for vi, w in wd.items():
            v = mesh.data.vertices[vi]
            for gi in list({g.group for g in v.groups} & clear_idx):
                mesh.vertex_groups[gi].remove([vi])
            items = sorted(w.items(), key=lambda kv: -kv[1])[:4]
            tot = sum(x for _, x in items) or 1.0
            for bn, ww in items:
                if ww / tot > 1e-4:
                    groups[bn].add([vi], ww / tot, 'REPLACE')


def wrot(arm, pbname, axis, deg):
    pb = arm.pose.bones[pbname]
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


# ---- reference grip pose (LEFT hand wrapping a ~29mm bar) ----
# tuned against a penetration sweep: fingers wrap ~220 deg, tips reach underside,
# zero mesh-through-bar. Reuse these angles as the canonical closed-grip.
GRIP_BAR = (0.862, 0.478, 0.0166)   # x, z, radius (bar axis along Y)
GRIP_FINGERS = (70, 78, 72)
GRIP_THUMB = (-48, 34, -30, 22)     # thumb_01 X,Z ; thumb_02 X,Z


def pose_grip(arm, side=".L"):
    reset_pose(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    f1, f2, f3 = GRIP_FINGERS
    wrot(arm, "fingers_01" + side, 'Y', f1)
    wrot(arm, "fingers_02" + side, 'Y', f2)
    wrot(arm, "fingers_03" + side, 'Y', f3)
    t1x, t1z, t2x, t2z = GRIP_THUMB
    wrot(arm, "thumb_01" + side, 'X', t1x); wrot(arm, "thumb_01" + side, 'Z', t1z)
    wrot(arm, "thumb_02" + side, 'X', t2x); wrot(arm, "thumb_02" + side, 'Z', t2z)
    bpy.ops.object.mode_set(mode='OBJECT')


def render_check(mesh, arm, path):
    """Pose the left hand into the closed bar-grip around a test cylinder and
    render a tight zoomed 3/4 crop for review."""
    bx, bz, r = GRIP_BAR
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=0.30, vertices=32,
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
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x = sc.render.resolution_y = 1000
    try: sc.eevee.taa_render_samples = 32
    except Exception: pass
    if sc.world is None:
        sc.world = bpy.data.worlds.new('W')
    sc.world.use_nodes = True
    bg = sc.world.node_tree.nodes.get('Background')
    bg.inputs[0].default_value = (0.6, 0.6, 0.63, 1.0); bg.inputs[1].default_value = 1.0
    for ang, en in (((55, 0, 20), 3.2), ((60, 0, 160), 1.6), ((30, 0, -90), 1.4)):
        lt = bpy.data.lights.new("sun", 'SUN'); lt.energy = en
        lo = bpy.data.objects.new("sun", lt); bpy.context.collection.objects.link(lo)
        lo.rotation_euler = (math.radians(ang[0]), math.radians(ang[1]), math.radians(ang[2]))
    cam = bpy.data.cameras.new("c"); ob = bpy.data.objects.new("c", cam)
    bpy.context.collection.objects.link(ob); ob.location = (0.97, -0.34, 0.70)
    tgt = Vector((0.865, 0.0, 0.486))
    ob.rotation_euler = (tgt - ob.location).normalized().to_track_quat('-Z', 'Y').to_euler()
    cam.lens = 100
    sc.camera = ob; sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(bar, do_unlink=True)


def export_glb(path, rig, mesh):
    reset_pose(rig)
    try: bpy.ops.file.pack_all()
    except Exception as e: print("pack warn", e)
    bpy.ops.object.select_all(action='DESELECT')
    rig.select_set(True); mesh.select_set(True)
    bpy.context.view_layer.objects.active = rig
    bpy.ops.export_scene.gltf(
        filepath=path, export_format='GLB', use_selection=True,
        export_apply=False, export_skins=True, export_yup=True,
        export_image_format='AUTO', export_texcoords=True, export_normals=True,
        export_materials='EXPORT')


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    src, out, check, tag = argv[0], argv[1], argv[2], argv[3]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    rebuild_finger_bones(arm)
    reweight_hand(mesh)
    ndef = sum(1 for b in arm.data.bones if b.use_deform)
    print("REGRIP %s verts=%d deform_bones=%d" % (tag, len(mesh.data.vertices), ndef))
    render_check(mesh, arm, check)
    print("CHECK_RENDER", check)
    export_glb(out, arm, mesh)
    import os
    print("EXPORTED", out, os.path.getsize(out))


if __name__ == "__main__":
    main()
