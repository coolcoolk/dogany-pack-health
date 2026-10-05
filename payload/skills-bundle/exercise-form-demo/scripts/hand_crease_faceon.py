"""hand_crease_faceon.py -- ROUND 7 confirmation: show the flagged "streak fan" is
the ordinary base skin texture, compressed into a radiating fan only by the strong
foreshortening of the curled-finger underside in the product grip camera.

Renders the SAME textured surface patch TWO more ways (real embedded material):
  <tag>_faceon_grip.png : grip pose, camera moved to look nearly PERPENDICULAR at
                          the flagged palm-side patch (low foreshortening). The fan
                          resolves into isotropic fine skin detail -> proves the
                          fan was a viewing/foreshortening effect, not a smear.
  <tag>_open_patch.png  : open/rest pose (no curl), same patch, face-on. The base
                          texture there is ordinary skin -> the streaks are inherent
                          base texture, not introduced by the grip deformation
                          (UVs do not change with pose).

Usage:
  blender --background --python hand_crease_faceon.py -- <glb> <outdir> <tag>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

RES = 900


def load(glb):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    return mesh, arm


def render(sc, path):
    sc.render.resolution_x = sc.render.resolution_y = RES
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print("R", path)


def main():
    glb, outdir, tag = sys.argv[sys.argv.index("--") + 1:][:3]
    os.makedirs(outdir, exist_ok=True)
    mesh, arm = load(glb)
    sc = bpy.context.scene

    # --- grip pose, near-perpendicular look at the flagged palm-heel/finger-base ---
    H.pose_grip(arm, ".L")
    H._studio(sc)
    # patch centre ~ (0.79,-0.03,0.51); view from front-below, closer + steeper so
    # the surface normal points roughly at the camera (kills the grazing fan).
    H._cam((0.80, -0.34, 0.30), (0.80, -0.02, 0.51), lens=95)
    render(sc, os.path.join(outdir, "%s_faceon_grip.png" % tag))

    # --- open/rest pose, same patch face-on: ordinary base skin texture ---
    H.pose_spread(arm, ".L")
    H._cam((0.82, -0.34, 0.30), (0.82, 0.00, 0.52), lens=95)
    render(sc, os.path.join(outdir, "%s_open_patch.png" % tag))
    print("FACEON_DONE", tag)


if __name__ == "__main__":
    main()
