"""hand_hole_classify.py -- ROUND 6: is the thumb-base grip cavity a real HOLE or a
self-occluded POCKET?

Renders the SAME straight-underside macro view as hand_thumb_waterfall's under_rakeX,
in grip pose, three ways so the cause is unambiguous:
  <tag>_headlamp.png   studio + a strong point light AT the camera. A deep pocket
                       (hollow of the closed fist, just unlit) FILLS IN with lit skin;
                       a genuine tear/gap stays void.
  <tag>_cull.png       backface culling ON + a flat mid-grey world. Through a genuine
                       hole you then see the GREY WORLD BACKGROUND; a solid pocket
                       stays skin (front faces only).
  <tag>_normals.png    front faces green / back faces red-ish via a geometry-normal
                       emission shader: if the cavity shows BACK faces (red) pointing
                       at the camera, the surface is inverted/torn there.

Usage:
  blender --background --python hand_hole_classify.py -- <glb> <outdir> <tag>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

RES = 1100
LENS = 170
UNDER = (0.045, -0.150, -0.150)   # matches waterfall's straight-underside framing


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


def thumb_centroid(mesh, arm):
    tgi = {mesh.vertex_groups[n].index for n in
           ("thumb_01.L", "thumb_02.L", "thumb_03.L") if mesh.vertex_groups.get(n)}
    tvi = [v.index for v in mesh.data.vertices
           if any(g.group in tgi and g.weight > 0.3 for g in v.groups)]
    H.pose_grip(arm, ".L")
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    mw = mesh.matrix_world
    co = [mw @ dm.vertices[i].co for i in tvi]
    cen = sum(co, Vector()) / len(co)
    ev.to_mesh_clear()
    return cen


def cam_at(cen, offset=UNDER, lens=LENS):
    for o in list(bpy.data.objects):
        if o.type == 'CAMERA':
            bpy.data.objects.remove(o, do_unlink=True)
    loc = cen + Vector(offset)
    cam = bpy.data.cameras.new("c"); ob = bpy.data.objects.new("c", cam)
    bpy.context.collection.objects.link(ob); ob.location = loc
    ob.rotation_euler = (cen - loc).normalized().to_track_quat('-Z', 'Y').to_euler()
    cam.lens = lens
    bpy.context.scene.camera = ob
    return ob


def clear_lights():
    for o in list(bpy.data.objects):
        if o.type == 'LIGHT':
            bpy.data.objects.remove(o, do_unlink=True)


def base_setup(sc):
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x = sc.render.resolution_y = RES
    try: sc.eevee.taa_render_samples = 48
    except Exception: pass
    if sc.world is None:
        sc.world = bpy.data.worlds.new('W')
    sc.world.use_nodes = True


def render(path):
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print("R", path)


def main():
    glb, outdir, tag = sys.argv[sys.argv.index("--") + 1:][:3]
    os.makedirs(outdir, exist_ok=True)
    mesh, arm = load(glb)
    cen = thumb_centroid(mesh, arm)   # applies grip
    sc = bpy.context.scene
    base_setup(sc)

    # --- headlamp: studio + strong point light at the camera ---
    clear_lights()
    bg = sc.world.node_tree.nodes.get('Background')
    bg.inputs[0].default_value = (0.4, 0.4, 0.45, 1.0)
    bg.inputs[1].default_value = 0.4
    camob = cam_at(cen)
    lamp = bpy.data.lights.new("head", 'POINT'); lamp.energy = 60.0
    lo = bpy.data.objects.new("head", lamp); bpy.context.collection.objects.link(lo)
    lo.location = camob.location
    render(os.path.join(outdir, "%s_headlamp.png" % tag))

    # --- cull: backface culling ON, flat grey world (hole -> shows grey bg) ---
    clear_lights()
    bg.inputs[0].default_value = (0.55, 0.55, 0.6, 1.0)
    bg.inputs[1].default_value = 1.0
    for m in mesh.data.materials:
        if m:
            m.use_backface_culling = True
    camob = cam_at(cen)
    lamp = bpy.data.lights.new("head", 'POINT'); lamp.energy = 60.0
    lo = bpy.data.objects.new("head", lamp); bpy.context.collection.objects.link(lo)
    lo.location = camob.location
    render(os.path.join(outdir, "%s_cull.png" % tag))
    for m in mesh.data.materials:
        if m:
            m.use_backface_culling = False

    # --- normals: emission by facing (front=green, back=red) ---
    nm = bpy.data.materials.new("NRM"); nm.use_nodes = True
    nt = nm.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    emit = nt.nodes.new("ShaderNodeEmission")
    geo = nt.nodes.new("ShaderNodeNewGeometry")
    # backfacing -> mix red, front -> green
    mix = nt.nodes.new("ShaderNodeMixRGB")
    mix.inputs[1].default_value = (0.0, 1.0, 0.0, 1.0)   # front = green
    mix.inputs[2].default_value = (1.0, 0.0, 0.0, 1.0)   # back = red
    nt.links.new(geo.outputs["Backfacing"], mix.inputs[0])
    nt.links.new(mix.outputs[0], emit.inputs[0])
    nt.links.new(emit.outputs[0], out.inputs[0])
    orig_mats = [m for m in mesh.data.materials]
    for i in range(len(mesh.data.materials)):
        mesh.data.materials[i] = nm
    clear_lights()
    bg.inputs[0].default_value = (0.1, 0.1, 0.12, 1.0)
    bg.inputs[1].default_value = 1.0
    cam_at(cen)
    render(os.path.join(outdir, "%s_normals.png" % tag))
    for i, m in enumerate(orig_mats):
        mesh.data.materials[i] = m
    print("HOLE_CLASSIFY_DONE", tag)


if __name__ == "__main__":
    main()
