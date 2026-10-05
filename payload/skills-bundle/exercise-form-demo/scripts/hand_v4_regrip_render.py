"""hand_v4_regrip_render.py -- re-render the v4 grip QA stills + re-export the GLBs
after a pose_grip constant change, WITHOUT re-running the accepted mesh surgery.

Round 2 only changed GRIP_THUMB (a posing constant). The exported GLB is reset to
rest before export, so the mesh/rig is unchanged; the only thing that differs is
the closed-grip RENDER. This driver loads the already-separated + rigged v4 GLB,
applies the (updated) grip pose from hand_sep_v4, renders the full grip check and
the zoomed knuckle crop, and re-exports the GLBs -- so the accepted mesh/open pose
are never touched.

Usage:
  blender --background --python hand_v4_regrip_render.py -- \
      <in_v4.glb> <out_v4.glb> <out_v4_lowpoly.glb> <grip_check.png> <knuckle_crop.png>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H


def main():
    argv = sys.argv[sys.argv.index("--") + 1:]
    src, out, out_low, chk_grip, chk_crop = argv[:5]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=src)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

    # --- build the grip scene once (bar + pose + studio), render two framings ---
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

    H.pose_grip(arm, ".L")
    sc = bpy.context.scene
    H._studio(sc)

    # full grip check -- exact framing render_grip uses
    sc.render.resolution_x = sc.render.resolution_y = 1200
    H._cam((0.98, -0.40, 0.66), (0.845, 0.0, 0.512), lens=78)
    sc.render.filepath = chk_grip
    bpy.ops.render.render(write_still=True)
    print("CHECK_GRIP", chk_grip)

    # zoomed knuckle/thumb crop -- same view direction, longer lens onto the thumb
    sc.render.resolution_x = sc.render.resolution_y = 700
    H._cam((0.98, -0.40, 0.66), (0.828, -0.02, 0.520), lens=135)
    sc.render.filepath = chk_crop
    bpy.ops.render.render(write_still=True)
    print("CHECK_CROP", chk_crop)

    bpy.data.objects.remove(bar, do_unlink=True)

    # --- re-export (pose reset inside export_full; mesh/rig identical) ---
    H.export_full(out, arm, mesh)
    print("EXPORTED_FULL", out, os.path.getsize(out))
    H.export_lowpoly(out_low, arm, mesh)
    print("EXPORTED_LOW", out_low, os.path.getsize(out_low))


if __name__ == "__main__":
    main()
