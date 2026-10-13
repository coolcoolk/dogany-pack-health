"""hand_grip_diag_render.py -- localize the contact chevron: render the grip pose
zoomed on the contact line, WITH the bar and WITHOUT it, from two angles.

Discriminator:
  * chevron persists with bar HIDDEN  -> mesh/skinning defect on the finger.
  * chevron GONE with bar hidden      -> bar<->finger intersection silhouette.

Usage:
  blender --background --python hand_grip_diag_render.py -- <glb> <outdir>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H


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
    glb, outdir = sys.argv[sys.argv.index("--") + 1:][:2]
    os.makedirs(outdir, exist_ok=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    H.pose_grip(arm, ".L")
    sc = bpy.context.scene
    H._studio(sc)
    sc.render.resolution_x = sc.render.resolution_y = 900

    # tight crops onto the contact line between index/middle at the bar top
    views = {
        "A": ((0.98, -0.40, 0.66), (0.845, 0.0, 0.520), 240),   # QA angle, deep zoom
        "B": ((0.90, -0.36, 0.70), (0.845, 0.0, 0.522), 240),   # higher / more top-down
    }
    for name, (loc, tgt, lens) in views.items():
        for tag, withbar in (("bar", True), ("nobar", False)):
            bar = add_bar() if withbar else None
            H._cam(loc, tgt, lens)
            path = os.path.join(outdir, "chev_%s_%s.png" % (name, tag))
            sc.render.filepath = path
            bpy.ops.render.render(write_still=True)
            print("RENDER", path)
            if bar:
                bpy.data.objects.remove(bar, do_unlink=True)
    print("DIAG_RENDER_DONE")


if __name__ == "__main__":
    main()
