"""hand_thumb_probe.py -- ROUND 4: quantify the thumb-base wave mechanism.

Prints, for the thumb-region verts, rest position (xs,y,z) + weight split across
hand / thumb_01 / thumb_02 / thumb_03, sorted by DEFORMED grip Laplacian, so we
can see whether a hand<->thumb_01 weight CLIFF (like the round-3 knuckle) drives
the ripple, and read off the rest-coordinate band to confine any reweight to.

Usage: blender --background --python hand_thumb_probe.py -- <glb>
"""
import bpy, sys, os
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H


def main():
    glb = sys.argv[sys.argv.index("--") + 1]
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

    def wmap(vi):
        return {gi2name[g.group]: g.weight for g in me.vertices[vi].groups}

    # thumb-region verts (weight>0.2 on any thumb bone), side .L
    tset = []
    tgi = {mesh.vertex_groups[n].index for n in
           ("thumb_01.L", "thumb_02.L", "thumb_03.L") if mesh.vertex_groups.get(n)}
    for v in me.vertices:
        for g in v.groups:
            if g.group in tgi and g.weight > 0.15:
                tset.append(v.index); break

    adj = {}
    for e in me.edges:
        a, b = e.vertices
        adj.setdefault(a, set()).add(b); adj.setdefault(b, set()).add(a)

    def lap(deformed):
        if deformed:
            H.pose_grip(arm, ".L")
            dg = bpy.context.evaluated_depsgraph_get()
            ev = mesh.evaluated_get(dg)
            dm = ev.to_mesh()
            co = [mesh.matrix_world @ v.co for v in dm.vertices]
        else:
            H.reset_pose(arm)
            co = [mesh.matrix_world @ v.co for v in me.vertices]
        L = {}
        for vi in tset:
            nb = adj.get(vi, ())
            if nb:
                m = sum((co[n] for n in nb), Vector()) / len(nb)
                L[vi] = (co[vi] - m).length
        if deformed:
            ev.to_mesh_clear()
        return L

    Ld = lap(True); Lr = lap(False)
    ranked = sorted(tset, key=lambda vi: -Ld.get(vi, 0))
    print("thumb-region verts=%d" % len(tset))
    print("worst-30 by deformed laplacian (rest coords, weights):")
    print("  xs      y       z     | lapD    lapR  ratio | hand thmb1 thmb2 thmb3")
    for vi in ranked[:30]:
        c = me.vertices[vi].co
        w = wmap(vi)
        h = w.get("hand.L", 0); t1 = w.get("thumb_01.L", 0)
        t2 = w.get("thumb_02.L", 0); t3 = w.get("thumb_03.L", 0)
        ld = Ld.get(vi, 0); lr = Lr.get(vi, 0)
        print("  %.4f %+.4f %.4f | %.5f %.5f %4.1f | %.2f %.2f %.2f %.2f"
              % (abs(c.x), c.y, c.z, ld, lr, (ld/lr if lr else 0), h, t1, t2, t3))

    # weight-cliff scan: bucket thumb-region verts by rest xs along the thumb axis,
    # print mean hand-weight per bucket to see where the hand->thumb handoff is sharp
    print("\nhand-weight vs thumb axis (xs bucket -> mean hand.L weight, n):")
    import collections
    buck = collections.defaultdict(list)
    for vi in tset:
        c = me.vertices[vi].co
        w = wmap(vi)
        buck[round(abs(c.x) * 100)].append(w.get("hand.L", 0))
    for k in sorted(buck):
        vals = buck[k]
        print("  xs~%.2f  meanHand=%.2f  n=%d" % (k/100.0, sum(vals)/len(vals), len(vals)))


if __name__ == "__main__":
    main()
