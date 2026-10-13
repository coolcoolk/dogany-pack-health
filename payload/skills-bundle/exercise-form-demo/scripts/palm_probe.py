"""palm_probe.py -- measure the hand/palm geometry of the v4 rig so we can size
the palm-shortening. Prints bone head/tail X for hand + finger bases, the X-span
of hand-region verts per side, and the middle-finger length. Read-only.

Usage: blender --background --python palm_probe.py -- <glb>
"""
import bpy, sys, os
from mathutils import Vector

GLB = sys.argv[sys.argv.index("--") + 1]
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=GLB)
mesh = max([o for o in bpy.data.objects if o.type == 'MESH'], key=lambda o: len(o.data.vertices))
arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]

print("=== BONES (rest, armature-local head/tail) ===")
for s in (".L", ".R"):
    for bn in ["forearm_twist"+s, "hand"+s,
               "thumb_01"+s, "index_01"+s, "middle_01"+s, "ring_01"+s, "pinky_01"+s,
               "middle_02"+s, "middle_03"+s]:
        b = arm.data.bones.get(bn)
        if not b:
            print("  MISSING", bn); continue
        h = b.head_local; t = b.tail_local
        print("  %-14s head=(%.4f,%+.4f,%.4f) tail=(%.4f,%+.4f,%.4f) len=%.4f"
              % (bn, h.x, h.y, h.z, t.x, t.y, t.z, b.length))

# middle finger length in X (knuckle base -> tip)
for s in (".L", ".R"):
    m1 = arm.data.bones["middle_01"+s].head_local
    m3 = arm.data.bones["middle_03"+s].tail_local
    print("MIDDLE_FINGER_LEN%s = %.4f (x %.4f -> %.4f)" % (s, abs(m3.x-m1.x), m1.x, m3.x))

# vertex X-distribution of hand-region verts, per side. Use vertex groups to find
# verts weighted to hand/finger bones. Report histogram of local xs = x*sign.
gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}
FINGER_PREF = ("hand", "thumb", "index", "middle", "ring", "pinky")

def is_hand_vert(v, s):
    for g in v.groups:
        n = gi2name.get(g.group, "")
        if g.weight > 0.05 and n.endswith(s) and any(n.startswith(p) for p in FINGER_PREF):
            return True
    return False

for s, sign in ((".L", 1.0), (".R", -1.0)):
    xs_list = []
    palm_xs = []   # verts weighted mainly to hand bone (palm/metacarpal)
    for v in mesh.data.vertices:
        if not is_hand_vert(v, s):
            continue
        xs = v.co.x * sign
        xs_list.append(xs)
        # dominant group
        best = max(v.groups, key=lambda g: g.weight)
        if gi2name.get(best.group, "") == "hand"+s:
            palm_xs.append(xs)
    if not xs_list:
        print("no hand verts", s); continue
    xs_list.sort()
    print("HAND%s verts=%d xs range=[%.4f .. %.4f]" % (s, len(xs_list), xs_list[0], xs_list[-1]))
    # percentiles
    import statistics
    def pct(p):
        i = int(p*(len(xs_list)-1)); return xs_list[i]
    print("   xs pct: p05=%.4f p25=%.4f p50=%.4f p75=%.4f p95=%.4f"
          % (pct(.05), pct(.25), pct(.50), pct(.75), pct(.95)))
    if palm_xs:
        palm_xs.sort()
        print("   PALM (hand-bone-dominant) verts=%d xs=[%.4f .. %.4f]"
              % (len(palm_xs), palm_xs[0], palm_xs[-1]))
print("PROBE_DONE")
