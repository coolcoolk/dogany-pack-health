"""hand_base_diag.py -- inspect the index/middle GROOVE-BASE web (the real chevron
location: rest x~0.842, y~0, z~0.546). Renders the QA-crop framing nobar, and
prints rest geometry + weights at the base web so rest-defect vs skinning-fold can
be told apart there.

Usage: blender --background --python hand_base_diag.py -- <glb> <nobar_png>
"""
import bpy, sys, math, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H


def main():
    glb, nobar = sys.argv[sys.argv.index("--") + 1:][:2]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    me = mesh.data
    mw = mesh.matrix_world
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}

    # weights + rest lap at the index/middle base web (x 0.828..0.862, |y|<0.012, top)
    adj = {}
    for e in me.edges:
        a, b = e.vertices
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)
    co = [mw @ v.co for v in me.vertices]
    sel = []
    for v in me.vertices:
        c = co[v.index]
        if not (0.826 < c.x < 0.864 and -0.013 < c.y < 0.013 and 0.538 < c.z < 0.560):
            continue
        nb = adj.get(v.index, ())
        lp = (c - sum((co[n] for n in nb), Vector()) / len(nb)).length if nb else 0.0
        ws = sorted(((gi2name.get(g.group, str(g.group)), g.weight)
                     for g in v.groups), key=lambda kv: -kv[1])[:3]
        sel.append((v.index, c, lp, ws))
    sel.sort(key=lambda t: (round(t[1].x, 3), t[1].y))
    print("=== index/middle BASE WEB (top surface) rest geom + weights ===")
    print("verts: %d" % len(sel))
    for vi, c, lp, ws in sel:
        wtxt = " ".join("%s=%.2f" % (n, w) for n, w in ws)
        print("  v%-7d (%.4f,%+.4f,%.4f) lap=%.2e  %s" % (vi, c.x, c.y, c.z, lp, wtxt))

    # render nobar at the QA-crop framing so the artifact is seen without the bar
    H.pose_grip(arm, ".L")
    sc = bpy.context.scene
    H._studio(sc)
    sc.render.resolution_x = sc.render.resolution_y = 700
    H._cam((0.98, -0.40, 0.66), (0.828, -0.02, 0.520), lens=135)
    sc.render.filepath = nobar
    bpy.ops.render.render(write_still=True)
    print("NOBAR", nobar)
    print("BASE_DIAG_DONE")


if __name__ == "__main__":
    main()
