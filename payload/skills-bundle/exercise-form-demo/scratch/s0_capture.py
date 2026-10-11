"""S0 donor capture -- APPROVED remodel plan, stage 0.

Build the MPFB donor human, delete helper geometry, isolate the LEFT hand at the
wrist plane (perpendicular to the forearm axis, keeping a ~1.5 cm forearm stub for
the S2 seam bridge), and save the isolated donor hand to scratch (.blend + .glb).

Then run the DONOR gate (C4 pinky / C5 palm:finger) on the isolated mesh, measured
from the mesh itself, and render 4 fixed angles for a fresh vision review.

Usage: blender --background --python s0_capture.py
Outputs (scratch/):
  donor_hand_L.blend, donor_hand_L.glb, donor_gate_*.png
"""
import bpy, addon_utils, os, math, bmesh
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = HERE  # scratch dir

# ---------------------------------------------------------------- build donor
bpy.ops.wm.read_factory_settings(use_empty=True)
addon_utils.enable('bl_ext.user_default.mpfb', default_set=True, persistent=True)
bpy.ops.mpfb.create_human()
mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
           key=lambda o: len(o.data.vertices))
me = mesh.data
name2i = {vg.name: vg.index for vg in mesh.vertex_groups}


def centroid(gname):
    gi = name2i.get(gname)
    if gi is None:
        return None
    acc = Vector((0, 0, 0)); n = 0
    for v in me.vertices:
        for g in v.groups:
            if g.group == gi and g.weight > 0.5:
                acc += v.co; n += 1
                break
    return (acc / n) if n else None


# capture joints BEFORE deleting helpers
FING = {1: "thumb", 2: "index", 3: "middle", 4: "ring", 5: "pinky"}
joints = {}
for fi in range(1, 6):
    joints[fi] = [centroid("joint-l-finger-%d-%d" % (fi, ji)) for ji in range(1, 5)]
wrist = centroid("joint-l-hand")
elbow = centroid("joint-l-elbow")
axis = (wrist - elbow).normalized()          # forearm direction elbow->wrist
cut_pt = wrist - axis * 0.015                 # keep ~1.5cm forearm stub

# ---------------------------------------------------------------- delete helpers
bpy.ops.mpfb.delete_helpers()
me = mesh.data
print("clean skin verts=%d" % len(me.vertices))

# ---------------------------------------------------------------- isolate hand
# hand = local cluster past the wrist plane, within 0.20 of the wrist
keep = set()
for v in me.vertices:
    d_plane = (v.co - cut_pt).dot(axis)       # >0 = toward fingers
    d_wrist = (v.co - wrist).length
    if d_plane > 0.0 and d_wrist < 0.20:
        keep.add(v.index)
print("hand verts selected=%d" % len(keep))

# delete everything else via bmesh
bm = bmesh.new(); bm.from_mesh(me)
bm.verts.ensure_lookup_table()
todel = [v for v in bm.verts if v.index not in keep]
bmesh.ops.delete(bm, geom=todel, context='VERTS')
bm.to_mesh(me); bm.free()
mesh.name = "DonorHandL"
me.update()
# strip vertex groups (donor rig is throwaway; S3 reskins to body skeleton)
for vg in list(mesh.vertex_groups):
    mesh.vertex_groups.remove(vg)
print("isolated DonorHandL verts=%d tris=%d" %
      (len(me.vertices), sum(len(p.vertices) - 2 for p in me.polygons)))

# ---------------------------------------------------------------- save
bpy.ops.object.select_all(action='DESELECT')
mesh.select_set(True)
bpy.context.view_layer.objects.active = mesh
blend_path = os.path.join(OUT, "donor_hand_L.blend")
bpy.ops.wm.save_as_mainfile(filepath=blend_path)
glb_path = os.path.join(OUT, "donor_hand_L.glb")
bpy.ops.export_scene.gltf(filepath=glb_path, use_selection=True,
                          export_format='GLB', export_yup=True)
print("SAVED", blend_path, glb_path)

# ---------------------------------------------------------------- DONOR gate
# per-finger vert assignment by nearest finger segment; palm vs finger split by
# projection past the knuckle (j1). lengths measured from mesh.
def seg_dist(p, a, b):
    ab = b - a; t = (p - a).dot(ab) / max(ab.length_squared, 1e-9)
    t = max(0.0, min(1.0, t)); return (p - (a + ab * t)).length


def past_knuckle(p, fi):
    j1, j4 = joints[fi][0], joints[fi][3]
    ax = (j4 - j1)
    return (p - j1).dot(ax) / max(ax.length_squared, 1e-9)  # >0 = past knuckle


per = {fi: [] for fi in range(1, 6)}
palm = []
for v in me.vertices:
    p = v.co
    # nearest finger by min distance to that finger's polyline (j1..j4)
    best, bfi = 1e9, None
    for fi in range(1, 6):
        js = joints[fi]
        dmin = min(seg_dist(p, js[k], js[k + 1]) for k in range(3))
        if dmin < best:
            best, bfi = dmin, fi
    if past_knuckle(p, bfi) > 0.0:
        per[bfi].append(p)
    else:
        palm.append(p)

print("\n=== DONOR GATE (isolated left hand) ===")
counts = {}; lengths = {}
for fi in range(1, 6):
    ps = per[fi]
    counts[fi] = len(ps)
    if ps:
        # finger length = span along j1->j4 axis of assigned verts
        j1, j4 = joints[fi][0], joints[fi][3]
        ax = (j4 - j1).normalized()
        proj = [ (p - j1).dot(ax) for p in ps ]
        lengths[fi] = max(proj) - min(0.0, min(proj))
    else:
        lengths[fi] = 0.0
    print("  %-7s verts=%3d  meshlen=%.4f" % (FING[fi], counts[fi], lengths[fi]))
print("  palm verts=%d" % len(palm))

mid_c, pk_c = counts[3], counts[5]
mid_l, pk_l = lengths[3], lengths[5]
c4_verts = pk_c >= 0.55 * mid_c
c4_len = pk_l >= 0.70 * mid_l
print("\n[C4 pinky] verts %d = %.0f%% of middle (need >=55%%) -> %s"
      % (pk_c, 100 * pk_c / max(mid_c, 1), "PASS" if c4_verts else "FAIL"))
print("[C4 pinky] len %.4f = %.0f%% of middle (need >=70%%) -> %s"
      % (pk_l, 100 * pk_l / max(mid_l, 1e-9), "PASS" if c4_len else "FAIL"))

# palm:finger ratio -- palm length (wrist->knuckle line) vs mean finger length
knuckle_c = sum((joints[fi][0] for fi in range(2, 6)), Vector()) / 4.0
palm_len = (knuckle_c - wrist).length
finger_len = sum(lengths[fi] for fi in range(2, 6)) / 4.0
ratio = palm_len / max(finger_len, 1e-9)
c5 = 0.90 <= ratio <= 1.15
print("[C5 palm:finger] palm_len=%.4f finger_len(mean4)=%.4f ratio=%.2f (norm 0.90-1.15) -> %s"
      % (palm_len, finger_len, ratio, "PASS" if c5 else "FAIL"))
# also vs MIDDLE finger (dominant-finger reference, matches gate intent)
ratio_mid = palm_len / max(mid_l, 1e-9)
print("[C5 palm:middle] ratio=%.2f (norm 0.90-1.15) -> %s"
      % (ratio_mid, "PASS" if 0.90 <= ratio_mid <= 1.15 else "FAIL"))

# ---------------------------------------------------------------- render 4 views
scn = bpy.context.scene
scn.render.engine = 'BLENDER_EEVEE'
scn.render.resolution_x = scn.render.resolution_y = 900
world = bpy.data.worlds.new("W"); scn.world = world
world.use_nodes = True
world.node_tree.nodes["Background"].inputs[0].default_value = (0.05, 0.05, 0.06, 1)
world.node_tree.nodes["Background"].inputs[1].default_value = 1.0
# key light
lamp = bpy.data.lights.new("key", 'AREA'); lamp.energy = 200; lamp.size = 0.5
lo = bpy.data.objects.new("key", lamp); scn.collection.objects.link(lo)
lo.location = (0.6, -0.6, 1.4)

ctr = wrist * 0.4 + knuckle_c * 0.6            # grip center-ish
rad = 0.16
cam_d = bpy.data.cameras.new("C"); cam = bpy.data.objects.new("C", cam_d)
scn.collection.objects.link(cam); scn.camera = cam
cam_d.lens = 70

VIEWS = {
    "front34":   Vector((ctr.x + 0.10, ctr.y - rad, ctr.z + 0.06)),
    "thumbside": Vector((ctr.x - rad, ctr.y - 0.02, ctr.z + 0.02)),
    "underside": Vector((ctr.x + 0.02, ctr.y - 0.04, ctr.z - rad)),
    "topdown":   Vector((ctr.x + 0.02, ctr.y - 0.02, ctr.z + rad)),
}
for name, loc in VIEWS.items():
    cam.location = loc
    d = (ctr - loc).normalized()
    cam.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    p = os.path.join(OUT, "donor_gate_%s.png" % name)
    scn.render.filepath = p
    bpy.ops.render.render(write_still=True)
    print("DONOR_CROP", p)

print("S0_CAPTURE_DONE")
