"""hand_thumb_wave.py -- ROUND 4 diagnostic: isolate the "wave under the thumb".

Owner flagged a wave/ripple (파도) UNDER the thumb in the grip render (the round-3
knuckle hairline is separately accepted). This harness renders the thumb region so
we can decide REST-geometry waviness vs POSE-deformation skinning artifact:

  1) grip pose,  standard 3/4 cam, tight thumb crop      -> thumb_grip_std.png
  2) grip pose,  UNDERSIDE cam (below the bar looking up) -> thumb_grip_under.png
  3) REST pose,  same underside cam                       -> thumb_rest_under.png
  4) REST pose,  standard cam, tight thumb crop           -> thumb_rest_std.png
  5) grip pose,  deformed-Laplacian false-color (thumb)   -> thumb_lap.png
        red = high per-vert deformed Laplacian (jagged skinning); if the wave is
        red it is a skinning artifact, if the wave shows in rest renders it is
        baked-in geometry.

Also prints, for the thumb-weighted verts, the REST-pose Laplacian (geometry
waviness independent of pose) vs DEFORMED Laplacian (pose skinning), so we get a
number for each hypothesis.

Usage: blender --background --python hand_thumb_wave.py -- <glb> <outdir>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

# thumb-crop cameras (bar axis along Y at x=0.831 z=0.517)
CAM_STD   = ((0.98, -0.40, 0.66), (0.828, -0.02, 0.520), 150)   # tight 3/4 on thumb
CAM_UNDER = ((0.95, -0.28, 0.30), (0.836, -0.02, 0.520), 120)   # from BELOW, looking up


def thumb_vi(mesh, side=".L"):
    gi = {mesh.vertex_groups[n].index for n in
          ("thumb_01" + side, "thumb_02" + side, "thumb_03" + side)
          if mesh.vertex_groups.get(n)}
    out = []
    for v in mesh.data.vertices:
        for g in v.groups:
            if g.group in gi and g.weight > 0.3:
                out.append(v.index); break
    return out


def add_bar():
    bx, bz, r = H.GRIP_BAR
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


def lap_of(mesh, adj, deformed):
    if deformed:
        dg = bpy.context.evaluated_depsgraph_get()
        ev = mesh.evaluated_get(dg)
        dm = ev.to_mesh()
        co = [mesh.matrix_world @ v.co for v in dm.vertices]
    else:
        co = [mesh.matrix_world @ v.co for v in mesh.data.vertices]
    lap = [0.0] * len(co)
    for vi in range(len(co)):
        nb = adj.get(vi, ())
        if nb:
            m = sum((co[n] for n in nb), Vector()) / len(nb)
            lap[vi] = (co[vi] - m).length
    if deformed:
        ev.to_mesh_clear()
    return lap


def render(path, res=760):
    sc = bpy.context.scene
    sc.render.resolution_x = sc.render.resolution_y = res
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print("R", path)


def main():
    glb, outdir = sys.argv[sys.argv.index("--") + 1:][:2]
    os.makedirs(outdir, exist_ok=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

    adj = {}
    for e in mesh.data.edges:
        a, b = e.vertices
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    tvi = thumb_vi(mesh)

    sc = bpy.context.scene
    H._studio(sc)
    bar = add_bar()

    # 1) grip std
    H.pose_grip(arm, ".L")
    H._cam(*CAM_STD); render(os.path.join(outdir, "thumb_grip_std.png"))
    # 2) grip underside
    H._cam(*CAM_UNDER); render(os.path.join(outdir, "thumb_grip_under.png"))

    # deformed laplacian (grip pose still applied)
    lap_def = lap_of(mesh, adj, deformed=True)

    # 4) rest std / 3) rest under
    H.reset_pose(arm)
    H._cam(*CAM_STD); render(os.path.join(outdir, "thumb_rest_std.png"))
    H._cam(*CAM_UNDER); render(os.path.join(outdir, "thumb_rest_under.png"))
    lap_rest = lap_of(mesh, adj, deformed=False)

    # numbers on the thumb verts
    def stats(lap, idx):
        vals = sorted(lap[i] for i in idx)
        n = len(vals)
        return (sum(vals) / n, vals[int(0.5 * n)], vals[int(0.9 * n)], vals[-1])
    mr = stats(lap_rest, tvi); md = stats(lap_def, tvi)
    print("THUMB_LAP REST  mean=%.5f med=%.5f p90=%.5f max=%.5f" % mr)
    print("THUMB_LAP DEFORM mean=%.5f med=%.5f p90=%.5f max=%.5f" % md)
    print("RATIO deform/rest mean=%.2f p90=%.2f" % (md[0]/mr[0], md[2]/mr[2]))

    # 5) false-color deformed laplacian on the thumb, grip pose
    H.pose_grip(arm, ".L")
    hi = 6.0e-3
    me = mesh.data
    if me.color_attributes:
        for ca in list(me.color_attributes):
            me.color_attributes.remove(ca)
    ca = me.color_attributes.new(name="diag", type='FLOAT_COLOR', domain='POINT')
    tset = set(tvi)
    for vi in range(len(me.vertices)):
        if vi in tset:
            t = min(1.0, lap_def[vi] / hi)
            ca.data[vi].color = (t, 0.12 * (1 - t), (1 - t) * 0.35, 1)
        else:
            ca.data[vi].color = (0.05, 0.05, 0.06, 1)
    mat = bpy.data.materials.new("dm"); mat.use_nodes = True
    nt = mat.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    emi = nt.nodes.new("ShaderNodeEmission")
    vc = nt.nodes.new("ShaderNodeVertexColor"); vc.layer_name = "diag"
    nt.links.new(vc.outputs["Color"], emi.inputs["Color"])
    nt.links.new(emi.outputs["Emission"], out.inputs["Surface"])
    me.materials.clear(); me.materials.append(mat)
    sc.world.node_tree.nodes.get('Background').inputs[1].default_value = 0.0
    bpy.data.objects.remove(bar, do_unlink=True)
    H._cam(*CAM_STD); render(os.path.join(outdir, "thumb_lap.png"))
    print("THUMB_WAVE_DONE")


if __name__ == "__main__":
    main()
