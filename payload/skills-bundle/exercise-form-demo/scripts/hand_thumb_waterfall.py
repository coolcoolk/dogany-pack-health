"""hand_thumb_waterfall.py -- ROUND 5 DIAGNOSTIC (render-only, no mesh writes).

Owner still sees a "waterfall" (폭포) under the thumb after round 4. This harness
renders TIGHT macro crops of the thumb UNDERSIDE (ventral surface) from several
angles + a RAKING (grazing) light that exaggerates fine ridge/ripple geometry,
for a given GLB in a given pose, so we can classify the pattern:
  (a) base-mesh micro-texture (cottage-cheese bump noise present body-wide),
  (b) mesh-topology ridges baked by the finger/thumb surgery (pose-independent),
  (c) a skinning fold that only appears under the grip deformation.

It auto-aims every camera at the deformed thumb centroid (so rest vs grip vs v3
frame the same physical patch), renders bar-free (nothing occludes the surface),
and emits:
  <tag>_under_studio.png   straight-on underside, flat studio light
  <tag>_34_studio.png      3/4 underside, flat studio light
  <tag>_under_rakeX.png    straight-on underside, raking light skimming along +x
  <tag>_under_rakeY.png    straight-on underside, raking light skimming along +y
  <tag>_34_rakeX.png       3/4 underside, raking light skimming along +x

Usage:
  blender --background --python hand_thumb_waterfall.py -- <glb> <grip|rest> <outdir> <tag>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

RES = 1100
LENS = 170  # long lens -> hard macro zoom on the thumb


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


def thumb_centroid(mesh, arm, pose):
    tgi = {mesh.vertex_groups[n].index for n in
           ("thumb_01.L", "thumb_02.L", "thumb_03.L") if mesh.vertex_groups.get(n)}
    tvi = [v.index for v in mesh.data.vertices
           if any(g.group in tgi and g.weight > 0.3 for g in v.groups)]
    if pose == "grip":
        try:
            H.pose_grip(arm, ".L")
        except Exception as e:
            print("POSE_WARN", e)
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    mw = mesh.matrix_world
    co = [mw @ dm.vertices[i].co for i in tvi]
    cen = sum(co, Vector()) / len(co)
    ev.to_mesh_clear()
    return cen


def clear_lights():
    for o in list(bpy.data.objects):
        if o.type == 'LIGHT':
            bpy.data.objects.remove(o, do_unlink=True)


def studio_light(sc):
    clear_lights()
    if sc.world is None:
        sc.world = bpy.data.worlds.new('W')
    sc.world.use_nodes = True
    bg = sc.world.node_tree.nodes.get('Background')
    bg.inputs[0].default_value = (0.62, 0.62, 0.65, 1.0)
    bg.inputs[1].default_value = 1.0
    for ang, en in (((55, 0, 20), 3.2), ((60, 0, 160), 1.6), ((30, 0, -90), 1.4)):
        lt = bpy.data.lights.new("sun", 'SUN'); lt.energy = en
        lo = bpy.data.objects.new("sun", lt); bpy.context.collection.objects.link(lo)
        lo.rotation_euler = (math.radians(ang[0]), math.radians(ang[1]),
                             math.radians(ang[2]))


def raking_light(sc, azimuth_deg):
    """Single strong sun skimming the thumb underside at a shallow grazing angle.
    The underside normal points roughly -Z; a near-horizontal ray casts long micro
    shadows off any ridge that runs across the light, making ripples pop.
    azimuth chooses which way the light skims so ridges of either orientation show."""
    clear_lights()
    sc.world.use_nodes = True
    bg = sc.world.node_tree.nodes.get('Background')
    bg.inputs[0].default_value = (0.5, 0.5, 0.55, 1.0)
    bg.inputs[1].default_value = 0.08   # very dim fill so shadows survive
    lt = bpy.data.lights.new("rake", 'SUN'); lt.energy = 6.0
    lt.angle = math.radians(0.4)        # crisp shadows
    lo = bpy.data.objects.new("rake", lt); bpy.context.collection.objects.link(lo)
    # elevation 12 deg above the (downward-facing) underside plane -> ray nearly
    # parallel to the surface. Pitch ~ 90-12 from vertical, lit from BELOW.
    lo.rotation_euler = (math.radians(180 - 12), 0.0, math.radians(azimuth_deg))
    # a faint top fill to keep the shape readable, but weak enough not to wash ridges
    f = bpy.data.lights.new("fill", 'SUN'); f.energy = 0.5
    fo = bpy.data.objects.new("fill", f); bpy.context.collection.objects.link(fo)
    fo.rotation_euler = (math.radians(40), 0, math.radians(30))


def cam_at(cen, offset, lens=LENS):
    for o in list(bpy.data.objects):
        if o.type == 'CAMERA':
            bpy.data.objects.remove(o, do_unlink=True)
    loc = cen + Vector(offset)
    cam = bpy.data.cameras.new("c"); ob = bpy.data.objects.new("c", cam)
    bpy.context.collection.objects.link(ob); ob.location = loc
    ob.rotation_euler = (cen - loc).normalized().to_track_quat('-Z', 'Y').to_euler()
    cam.lens = lens
    bpy.context.scene.camera = ob


def render(path):
    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x = sc.render.resolution_y = RES
    try: sc.eevee.taa_render_samples = 48
    except Exception: pass
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print("R", path)


# camera offsets from the thumb centroid (world units; ~1u = 1060mm)
UNDER = (0.045, -0.150, -0.150)   # below + front, looking up at the ventral pad
Q34   = (0.175, -0.115, -0.070)   # 3/4 from the outer side, slightly below


def main():
    glb, pose, outdir, tag = sys.argv[sys.argv.index("--") + 1:][:4]
    os.makedirs(outdir, exist_ok=True)
    mesh, arm = load(glb)
    cen = thumb_centroid(mesh, arm, pose)   # also applies grip pose if requested
    print("CENTROID", tag, "%.4f %.4f %.4f" % (cen.x, cen.y, cen.z))
    sc = bpy.context.scene

    studio_light(sc)
    cam_at(cen, UNDER); render(os.path.join(outdir, "%s_under_studio.png" % tag))
    cam_at(cen, Q34);   render(os.path.join(outdir, "%s_34_studio.png" % tag))

    raking_light(sc, 0);   cam_at(cen, UNDER)
    render(os.path.join(outdir, "%s_under_rakeX.png" % tag))
    raking_light(sc, 90);  cam_at(cen, UNDER)
    render(os.path.join(outdir, "%s_under_rakeY.png" % tag))
    raking_light(sc, 0);   cam_at(cen, Q34)
    render(os.path.join(outdir, "%s_34_rakeX.png" % tag))
    print("WATERFALL_DONE", tag)


if __name__ == "__main__":
    main()
