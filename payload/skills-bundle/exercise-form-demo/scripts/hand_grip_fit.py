"""hand_grip_fit.py -- derive the bar that the curled finger arc naturally wraps.

Uniform curl per joint makes the finger joints lie on a circular arc. Fit that
circle (in X-Z) from the middle-finger joint world positions, then the bar that
the finger hugs cleanly is: centre = arc centre, radius = arc_radius - finger
half-thickness. Prints, for several uniform curl angles, the fitted bar + the
resulting penetration so the closed grip can be placed with zero pass-through.
"""
import bpy, sys, math
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


def pose_uniform(arm, ang, side=".L"):
    reset_pose(arm)
    bpy.context.view_layer.objects.active = arm
    bpy.ops.object.mode_set(mode='POSE')
    for finger in FINGERS:
        for j in (1, 2, 3):
            wrot(arm, "%s_0%d%s" % (finger, j, side), 'Y', ang)
    bpy.ops.object.mode_set(mode='OBJECT')


def fit_circle_xz(pts):
    """Least-squares circle in the X-Z plane. pts = list of (x,z)."""
    import numpy as np
    A = []; b = []
    for x, z in pts:
        A.append([2 * x, 2 * z, 1]); b.append(x * x + z * z)
    A = np.array(A); b = np.array(b)
    c, *_ = np.linalg.lstsq(A, b, rcond=None)
    cx, cz, cc = c
    R = math.sqrt(cc + cx * cx + cz * cz)
    return cx, cz, R


def finger_joints(arm, finger, side=".L"):
    mw = arm.matrix_world
    b1 = arm.pose.bones["%s_01%s" % (finger, side)]
    b2 = arm.pose.bones["%s_02%s" % (finger, side)]
    b3 = arm.pose.bones["%s_03%s" % (finger, side)]
    pts = [mw @ b1.head, mw @ b2.head, mw @ b3.head, mw @ b3.tail]
    return [(p.x, p.z) for p in pts]


def penetration(mesh, arm, bx, bz, r, side=".L"):
    dg = mesh.evaluated_get(bpy.context.evaluated_depsgraph_get())
    me = dg.to_mesh()
    mw = mesh.matrix_world
    inside = 0; deep = 0; mind = 1e9
    for v in me.vertices:
        co = mw @ v.co
        xs = co.x * (1 if side == ".L" else -1)
        if xs < 0.83 or not (0.40 < co.z < 0.60):
            continue
        d = math.hypot(co.x - bx, co.z - bz)
        if d < r - 0.0015:
            inside += 1
            if d < 0.45 * r:
                deep += 1
            mind = min(mind, d)
    mesh.to_mesh_clear()
    return inside, deep, (mind if inside else r)


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    glb = argv[0]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    HALF = 0.011   # finger half-thickness (centerline -> surface)
    for ang in [58, 62, 66, 70, 74, 78]:
        pose_uniform(arm, ang)
        pts = finger_joints(arm, "middle")
        cx, cz, R = fit_circle_xz(pts)
        r_bar = R - HALF
        if r_bar <= 0.006:
            print("ang=%d  R=%.4f  bar_r=%.4f TOO TIGHT" % (ang, R, r_bar))
            continue
        inn, deep, mind = penetration(mesh, arm, cx, cz, r_bar)
        print("ang=%2d  arc R=%.4f  bar=(%.4f,%.4f) r=%.4f (%.1fmm dia) | pen=%d deep=%d mind=%.4f"
              % (ang, R, cx, cz, r_bar, r_bar * 2 * 1058, inn, deep, mind))


if __name__ == "__main__":
    main()
