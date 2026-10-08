"""hand_grip_sweep.py -- load the rigged glb ONCE and score many grip configs.

No rendering: for each (bar, curl) combo it poses the hand, measures per-finger
tip wrap and mesh penetration against the bar, and prints a score so the closed
grip can be tuned to "tips reach the underside, minimal mesh-through-bar" fast.
Score = sum over fingers of |tip_dist - r| (want tip on surface) with a bonus for
tips that have wrapped below centre (dz<0), PLUS a penetration penalty.
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
    if thumb:
        wrot(arm, "thumb_01" + side, 'X', thumb[0]); wrot(arm, "thumb_01" + side, 'Z', thumb[1])
        wrot(arm, "thumb_02" + side, 'X', thumb[2]); wrot(arm, "thumb_02" + side, 'Z', thumb[3])
        wrot(arm, "thumb_03" + side, 'X', thumb[4])
    bpy.ops.object.mode_set(mode='OBJECT')


def evaluate(mesh, arm, bar, side=".L"):
    bx, bz, r = bar
    sc_sign = 1 if side == ".L" else -1
    tips = {}
    for finger in FINGERS:
        pb = arm.pose.bones.get("%s_03%s" % (finger, side))
        w = arm.matrix_world @ pb.tail
        d = math.hypot(w.x - bx, w.z - bz)
        tips[finger] = (d, w.z - bz, w.x - bx)
    dg = mesh.evaluated_get(bpy.context.evaluated_depsgraph_get())
    me = dg.to_mesh()
    mw = mesh.matrix_world
    inside = 0; deep = 0; mind = 1e9
    maxx = -1e9; minz = 1e9; maxx_z = 0.0
    deep_at = (0, 0)
    verts = me.vertices
    for v in verts:
        co = mw @ v.co
        xs = co.x * sc_sign
        if xs < 0.83 or not (0.40 < co.z < 0.60):
            continue
        d = math.hypot(co.x - bx, co.z - bz)
        if d < r - 0.0015:
            inside += 1
            if d < 0.45 * r:          # deep = gross pass-through (not surface contact)
                deep += 1
            if d < mind:
                mind = d; deep_at = (co.x, co.z)
        if xs > maxx:
            maxx = xs; maxx_z = co.z
        minz = min(minz, co.z)
    mesh.to_mesh_clear()
    return tips, inside, deep, (mind if inside else r), (maxx, maxx_z, minz), deep_at


def score(tips, inside, deep, r):
    # bone tail is the finger CENTERLINE; mesh surface sits ~0.010 outward (toward
    # the bar). So mesh hugs the surface when the bone tail is ~1.6r from the axis.
    # DEEP pass-through is the real defect; shallow contact is fine/invisible.
    target = 1.6 * r
    s = 0.0
    for f in FINGERS:
        d, dz, dx = tips[f]
        s += abs(d - target) * 120.0
        if dz > 0.008:                    # tip still well above centre -> not wrapped
            s += dz * 250.0
    s += deep * 0.6 + inside * 0.008
    return s


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    glb = argv[0]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

    # configs to try: list of (label, bar, curl, thumb)
    configs = json.loads(argv[1])
    best = None
    for cfg in configs:
        bar = cfg["bar"]; curl = cfg["curl"]; thumb = cfg.get("thumb")
        pose_grip(arm, curl, thumb)
        tips, inside, deep, mind, bounds, deep_at = evaluate(mesh, arm, bar)
        sc = score(tips, inside, deep, bar[2])
        tipstr = " ".join("%s:%.2fr/dz%+.3f" % (f[:2], tips[f][0] / bar[2], tips[f][1])
                          for f in FINGERS)
        print("CFG %-16s score=%6.1f pen=%4d deep=%4d deepAt=(%.3f,%.3f) | %s"
              % (cfg.get("label", "?"), sc, inside, deep, deep_at[0], deep_at[1], tipstr))
        if best is None or sc < best[1]:
            best = (cfg.get("label", "?"), sc)
    print("BEST", best)


if __name__ == "__main__":
    main()
