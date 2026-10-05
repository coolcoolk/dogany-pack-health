"""hand_pose_probe.py -- fast pose iteration harness for the v4 per-finger hand.

Loads an existing rigged glb (no mesh surgery), applies a grip or open pose with
angle sets passed on the command line as JSON, renders a small check image, and
-- for grip mode -- prints quantitative diagnostics:
  * per-finger tip (finger_03 tail) distance-to-bar-axis and (dx,dz) offset
  * mesh penetration: how many finger verts sit inside the bar (dist_to_axis < r)
    and the deepest penetration.
This lets grip curl be tuned to "tips wrap past centre, zero mesh-through-bar"
without paying the full-surgery cost each iteration.

Usage:
  blender --background --python hand_pose_probe.py -- <glb> <mode> <out.png> '<json>'
  mode = grip | open
  json (grip) = {"bar":[x,z,r],"curl":{"index":[a,b,c],...},"thumb":[...]}
  json (open) = {"fan":{"index":d,...},"curl2":d,"curl3":d,"thumb":[z1,z2],"cam":[...]}
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


def pose_grip(arm, cfg, side=".L"):
    reset_pose(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    for finger in FINGERS:
        a, b, c = cfg["curl"][finger]
        wrot(arm, "%s_01%s" % (finger, side), 'Y', a)
        wrot(arm, "%s_02%s" % (finger, side), 'Y', b)
        wrot(arm, "%s_03%s" % (finger, side), 'Y', c)
    t = cfg["thumb"]
    wrot(arm, "thumb_01" + side, 'X', t[0]); wrot(arm, "thumb_01" + side, 'Z', t[1])
    wrot(arm, "thumb_02" + side, 'X', t[2]); wrot(arm, "thumb_02" + side, 'Z', t[3])
    wrot(arm, "thumb_03" + side, 'X', t[4])
    bpy.ops.object.mode_set(mode='OBJECT')


def pose_open(arm, cfg, side=".L"):
    reset_pose(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    fan = cfg["fan"]; c2 = cfg.get("curl2", 0); c3 = cfg.get("curl3", 0)
    for finger in FINGERS:
        wrot(arm, "%s_01%s" % (finger, side), 'Z', fan[finger])
        if c2:
            wrot(arm, "%s_02%s" % (finger, side), 'Y', c2)
        if c3:
            wrot(arm, "%s_03%s" % (finger, side), 'Y', c3)
    th = cfg.get("thumb", [22, 12])
    wrot(arm, "thumb_01" + side, 'Z', th[0])
    wrot(arm, "thumb_02" + side, 'Z', th[1])
    bpy.ops.object.mode_set(mode='OBJECT')


def studio(sc, res=700):
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


def cam(loc, tgt, lens=95):
    c = bpy.data.cameras.new("c"); ob = bpy.data.objects.new("c", c)
    bpy.context.collection.objects.link(ob); ob.location = Vector(loc)
    ob.rotation_euler = (Vector(tgt) - ob.location).normalized().to_track_quat('-Z', 'Y').to_euler()
    c.lens = lens
    bpy.context.scene.camera = ob


def tip_world(arm, finger, side=".L"):
    pb = arm.pose.bones.get("%s_03%s" % (finger, side))
    return arm.matrix_world @ pb.tail


def diagnostics(mesh, arm, bar, side=".L"):
    """Report per-finger tip wrap + mesh penetration against the bar cylinder."""
    bx, bz, r = bar
    # tip reach per finger
    print("--- TIP REACH (dist_to_axis vs r=%.4f; dz<0 = below centre) ---" % r)
    for finger in FINGERS:
        w = tip_world(arm, finger, side)
        d = math.hypot(w.x - bx, w.z - bz)
        print("  %-6s tip x=%.4f z=%.4f  dist=%.4f (%.3f*r)  dz=%+.4f dx=%+.4f"
              % (finger, w.x, w.z, d, d / r, w.z - bz, w.x - bx))
    # mesh penetration: finger-region verts inside the bar
    dg = mesh.evaluated_get(bpy.context.evaluated_depsgraph_get())
    me = dg.to_mesh()
    mw = mesh.matrix_world
    inside = 0; mind = 1e9; near = 0
    sc_sign = 1 if side == ".L" else -1
    for v in me.data.vertices if hasattr(me, "data") else me.vertices:
        co = mw @ v.co
        xs = co.x * sc_sign
        if xs < 0.83 or not (0.40 < co.z < 0.60):
            continue
        d = math.hypot(co.x - bx, co.z - bz)
        if d < r - 0.0005:
            inside += 1
            mind = min(mind, d)
        elif d < r + 0.004:
            near += 1
    dg_ok = mind if inside else float('nan')
    print("--- PENETRATION: %d verts inside bar (deepest dist=%.4f, r=%.4f), %d verts hugging surface ---"
          % (inside, dg_ok, r, near))
    mesh.to_mesh_clear()


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    glb, mode, out, cfg_json = argv[:4]
    cfg = json.loads(cfg_json)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    sc = bpy.context.scene

    if mode == "grip":
        bx, bz, r = cfg["bar"]
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
        pose_grip(arm, cfg, ".L")
        studio(sc)
        c = cfg.get("cam", [[0.95, -0.31, 0.60], [0.868, 0.0, 0.50], 92])
        cam(c[0], c[1], c[2])
        sc.render.filepath = out
        bpy.ops.render.render(write_still=True)
        diagnostics(mesh, arm, cfg["bar"], ".L")
    else:
        pose_open(arm, cfg, ".L")
        studio(sc)
        c = cfg.get("cam", [[0.86, -0.30, 0.86], [0.855, 0.01, 0.535], 80])
        cam(c[0], c[1], c[2])
        sc.render.filepath = out
        bpy.ops.render.render(write_still=True)
    print("PROBE_DONE", out)


if __name__ == "__main__":
    main()
