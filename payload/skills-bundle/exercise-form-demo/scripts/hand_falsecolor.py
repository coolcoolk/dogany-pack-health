"""hand_falsecolor.py -- pinpoint the chevron verts by false-coloring the DEFORMED
grip mesh: red = high deformed-Laplacian (jagged), and a second render tinting by
dominant vertex group so the driving bone of the flap is visible.

Prints the rest positions + weights of the verts inside a screen-space box the
caller can read off the render.

Usage: blender --background --python hand_falsecolor.py -- <glb> <outdir>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

GROUP_TINT = {
    "index": (1, 0.15, 0.15), "middle": (0.15, 1, 0.15),
    "ring": (0.15, 0.4, 1), "pinky": (1, 1, 0.15), "thumb": (1, 0.15, 1),
    "hand": (0.5, 0.5, 0.5),
}


def dom_finger(name):
    for k in GROUP_TINT:
        if name.startswith(k):
            return k
    return "hand"


def colorize(mesh, colors):
    me = mesh.data
    if me.color_attributes:
        for ca in list(me.color_attributes):
            me.color_attributes.remove(ca)
    ca = me.color_attributes.new(name="diag", type='FLOAT_COLOR', domain='POINT')
    for i, c in enumerate(colors):
        ca.data[i].color = (c[0], c[1], c[2], 1.0)
    mat = bpy.data.materials.get("diagmat")
    if mat is None:
        mat = bpy.data.materials.new("diagmat"); mat.use_nodes = True
        nt = mat.node_tree
        for n in list(nt.nodes):
            nt.nodes.remove(n)
        out = nt.nodes.new("ShaderNodeOutputMaterial")
        emi = nt.nodes.new("ShaderNodeEmission")
        vc = nt.nodes.new("ShaderNodeVertexColor"); vc.layer_name = "diag"
        nt.links.new(vc.outputs["Color"], emi.inputs["Color"])
        nt.links.new(emi.outputs["Emission"], out.inputs["Surface"])
    me.materials.clear(); me.materials.append(mat)


def render(mesh, arm, path):
    sc = bpy.context.scene
    sc.render.engine = 'BLENDER_EEVEE'
    sc.render.resolution_x = sc.render.resolution_y = 800
    if sc.world is None:
        sc.world = bpy.data.worlds.new('W')
    sc.world.use_nodes = True
    sc.world.node_tree.nodes.get('Background').inputs[1].default_value = 0.0
    H._cam((0.98, -0.40, 0.66), (0.828, -0.02, 0.520), lens=135)
    sc.render.filepath = path
    bpy.ops.render.render(write_still=True)


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
    me = mesh.data
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}

    adj = {}
    for e in me.edges:
        a, b = e.vertices
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)

    # deformed laplacian
    H.pose_grip(arm, ".L")
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    dco = [mesh.matrix_world @ v.co for v in dm.vertices]
    lap = [0.0] * len(dco)
    for vi in range(len(dco)):
        nb = adj.get(vi, ())
        if nb:
            m = sum((dco[n] for n in nb), Vector()) / len(nb)
            lap[vi] = (dco[vi] - m).length
    ev.to_mesh_clear()

    # render 1: laplacian heat (red=jagged), only finger region lit
    hi = 8.0e-3
    cols = []
    for vi in range(len(me.vertices)):
        c = mesh.matrix_world @ me.vertices[vi].co
        if 0.83 < c.x < 0.95 and -0.03 < c.y < 0.11 and 0.50 < c.z < 0.58:
            t = min(1.0, lap[vi] / hi)
            cols.append((t, 0.1 * (1 - t), (1 - t) * 0.3))
        else:
            cols.append((0.06, 0.06, 0.07))
    colorize(mesh, cols)
    render(mesh, arm, os.path.join(outdir, "fc_lap.png"))
    print("FC_LAP", os.path.join(outdir, "fc_lap.png"))

    # render 2: dominant-group tint
    cols = []
    for vi in range(len(me.vertices)):
        v = me.vertices[vi]
        gg = sorted(((gi2name.get(g.group, ""), g.weight) for g in v.groups),
                    key=lambda kv: -kv[1])
        if gg:
            cols.append(GROUP_TINT[dom_finger(gg[0][0])])
        else:
            cols.append((0.06, 0.06, 0.07))
    colorize(mesh, cols)
    render(mesh, arm, os.path.join(outdir, "fc_group.png"))
    print("FC_GROUP", os.path.join(outdir, "fc_group.png"))
    print("FALSECOLOR_DONE")


if __name__ == "__main__":
    main()
