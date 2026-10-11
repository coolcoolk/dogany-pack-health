"""hand_thumb_fit.py -- thumb-wrap diagnostic + sweep for the v4 per-finger hand.

The 4 fingers were arc-fit to the bar in round 1; the thumb was left folding into
the palm on the SAME side as the fingers (a thumbless/monkey grip). This harness
scores thumb configs quantitatively so the thumb can be brought AROUND to the far
side of the bar to oppose the fingers (a real closed thumb-wrap grip).

For each thumb config it poses the hand (fingers fixed at the accepted round-1
grip curl), then prints:
  * thumb joint world positions (thumb_01/02/03 head + thumb_03 tail = TIP), each
    as (dx,dz) offset from the bar axis so we can see which side of the bar the
    thumb sits on. Fingertips wrap to dx<0 (the -X side); a real wrap needs the
    thumb TIP on the OPPOSITE side (dx>0) and curled toward/below centre.
  * thumb-mesh penetration: thumb-weighted verts that end up inside the bar
    (deepest dist + a DEEP count for gross pass-through), same standard as fingers.
  * thumb-tip -> nearest index-finger-mesh distance (checks the tip actually meets
    the index finger, not floating in space).

Usage:
  blender --background --python hand_thumb_fit.py -- <glb> '<configs-json>'
  configs-json = [{"label":..,"bar":[x,z,r],"curl":{..},"thumb":[t1x,t1z,t2x,t2z,t3x]}, ..]
    thumb axes match pose_grip: thumb_01 X then Z, thumb_02 X then Z, thumb_03 X.
"""
import bpy, sys, math, json
from mathutils import Vector, Matrix

FINGERS = ["index", "middle", "ring", "pinky"]


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


def pose_grip(arm, curl, thumb, side=".L"):
    reset_pose(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    for finger in FINGERS:
        a, b, c = curl[finger]
        wrot(arm, "%s_01%s" % (finger, side), 'Y', a)
        wrot(arm, "%s_02%s" % (finger, side), 'Y', b)
        wrot(arm, "%s_03%s" % (finger, side), 'Y', c)
    # thumb: either the legacy 5-tuple [t1x,t1z,t2x,t2z,t3x] (X/Z folds), OR a list
    # of explicit ops [["thumb_01","Y",30],["thumb_02","Y",40],...] for free axis
    # experimentation (applied in the given order about WORLD axes at each head).
    if thumb and isinstance(thumb[0], (list, tuple)):
        for bn, ax, dg in thumb:
            wrot(arm, bn + side, ax, dg)
    else:
        t = thumb
        wrot(arm, "thumb_01" + side, 'X', t[0]); wrot(arm, "thumb_01" + side, 'Z', t[1])
        wrot(arm, "thumb_02" + side, 'X', t[2]); wrot(arm, "thumb_02" + side, 'Z', t[3])
        wrot(arm, "thumb_03" + side, 'X', t[4])
    bpy.ops.object.mode_set(mode='OBJECT')


def _thumb_vert_indices(mesh, side=".L"):
    """Vertices weighted to any thumb bone (rest-independent classification)."""
    gi = {mesh.vertex_groups[n].index for n in
          ("thumb_01" + side, "thumb_02" + side, "thumb_03" + side)
          if mesh.vertex_groups.get(n)}
    out = []
    for v in mesh.data.vertices:
        for g in v.groups:
            if g.group in gi and g.weight > 0.3:
                out.append(v.index); break
    return out


def _index_vert_indices(mesh, side=".L"):
    gi = {mesh.vertex_groups[n].index for n in
          ("index_01" + side, "index_02" + side, "index_03" + side)
          if mesh.vertex_groups.get(n)}
    out = []
    for v in mesh.data.vertices:
        for g in v.groups:
            if g.group in gi and g.weight > 0.3:
                out.append(v.index); break
    return out


def evaluate(mesh, arm, bar, thumb_vi, index_vi, side=".L"):
    bx, bz, r = bar
    mw = arm.matrix_world
    # thumb joint chain world positions
    joints = []
    for bn in ("thumb_01", "thumb_02", "thumb_03"):
        pb = arm.pose.bones["%s%s" % (bn, side)]
        joints.append(("%s.head" % bn, mw @ pb.head))
    tip = mw @ arm.pose.bones["thumb_03" + side].tail
    joints.append(("thumb_03.tail", tip))

    # thumb-mesh penetration + world positions of thumb / index verts
    dg = mesh.evaluated_get(bpy.context.evaluated_depsgraph_get())
    me = dg.to_mesh()
    mmw = mesh.matrix_world
    tset = set(thumb_vi); iset = set(index_vi)
    inside = 0; deep = 0; mind = 1e9
    thumb_pts = []; index_pts = []
    for v in me.vertices:
        co = mmw @ v.co
        if v.index in tset:
            thumb_pts.append(co)
            d = math.hypot(co.x - bx, co.z - bz)
            if d < r - 0.0015:
                inside += 1
                if d < 0.45 * r:
                    deep += 1
                mind = min(mind, d)
        if v.index in iset:
            index_pts.append(co)
    # nearest thumb-mesh-tip -> index-mesh distance (use thumb verts near the tip)
    # tip cluster = thumb verts within 0.02 of the bone tip
    tipco = tip
    tipcluster = [p for p in thumb_pts if (p - tipco).length < 0.025]
    best = 1e9
    for tp in (tipcluster or thumb_pts):
        for ip in index_pts:
            best = min(best, (tp - ip).length)
    mesh.to_mesh_clear()
    return joints, tip, (inside, deep, mind if inside else r), best


def studio(sc, res=760):
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x = sc.render.resolution_y = res
    try: sc.eevee.taa_render_samples = 24
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


def cam(loc, tgt, lens=78):
    c = bpy.data.cameras.new("c"); ob = bpy.data.objects.new("c", c)
    bpy.context.collection.objects.link(ob); ob.location = Vector(loc)
    ob.rotation_euler = (Vector(tgt) - ob.location).normalized().to_track_quat('-Z', 'Y').to_euler()
    c.lens = lens
    bpy.context.scene.camera = ob


def add_bar(bar):
    bx, bz, r = bar
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=0.32, vertices=48,
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
    return b


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    glb = argv[0]
    render_dir = argv[2] if len(argv) > 2 else None
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    thumb_vi = _thumb_vert_indices(mesh)
    index_vi = _index_vert_indices(mesh)
    print("thumb_verts=%d index_verts=%d" % (len(thumb_vi), len(index_vi)))

    configs = json.loads(argv[1])
    bar_obj = None
    if render_dir:
        bar_obj = add_bar(configs[0]["bar"])
        studio(bpy.context.scene)
    for cfg in configs:
        bar = cfg["bar"]; curl = cfg["curl"]; thumb = cfg["thumb"]
        bx, bz, r = bar
        pose_grip(arm, curl, thumb)
        joints, tip, (inside, deep, mind), best = evaluate(
            mesh, arm, bar, thumb_vi, index_vi)
        print("=== %s  thumb=%s ===" % (cfg.get("label", "?"), thumb))
        for name, p in joints:
            print("  %-14s x=%.4f z=%.4f  dx=%+.4f dz=%+.4f  dist=%.4f (%.2fr)"
                  % (name, p.x, p.z, p.x - bx, p.z - bz,
                     math.hypot(p.x - bx, p.z - bz),
                     math.hypot(p.x - bx, p.z - bz) / r))
        print("  PEN thumb-mesh: inside=%d deep=%d deepest_dist=%.4f (r=%.4f) | tip->index_mesh=%.4f"
              % (inside, deep, mind, r, best))
        if render_dir:
            c = cfg.get("cam", [[0.98, -0.40, 0.66], [0.845, 0.0, 0.512], 78])
            cam(c[0], c[1], c[2])
            bpy.context.scene.render.filepath = "%s/%s.png" % (render_dir, cfg.get("label", "x"))
            bpy.ops.render.render(write_still=True)
            print("  RENDER %s/%s.png" % (render_dir, cfg.get("label", "x")))


if __name__ == "__main__":
    main()
