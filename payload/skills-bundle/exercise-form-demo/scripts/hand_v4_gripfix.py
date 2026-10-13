"""hand_v4_gripfix.py -- bar-collision / offset geometry pass for the v4 closed grip.

The v4 per-finger closed grip (H.pose_grip) penetrates the test bar: curled fingers
pass THROUGH the metal, throwing mesh shards + cracking the back of the hand. The  # estate-scrub:allow(metal material, 3D render)
three prior repair rounds all re-weighted the skin and hit a cap. This script uses a
DIFFERENT lever: it bakes the posed hand mesh, then runs a radial COLLISION/OFFSET
pass that seats every penetrating vertex ON the bar surface (project to bar radius +
skin epsilon), so the fingers wrap ON the metal instead of through it.  # estate-scrub:allow(metal material, 3D render)

Offset math (per vertex, bar axis along world-Y at (bx,bz)):
  d       = hypot(co.x-bx, co.z-bz)          # radial distance from bar axis
  target  = r + skin_eps                     # bar surface + thin skin gap
  new_d   = softmax(d, target, k)            # SMOOTH max -> feathers to 0 as d grows
          = target + softplus(d-target)/k,  softplus(x)=log(1+exp(k*x))
  co.x,co.z pushed radially so radial dist becomes new_d; co.y untouched.
The softmax (not a hard clamp) is the anti-shard trick: verts just outside the bar
get only a vanishing nudge and the pushed band blends C1-smoothly into the un-pushed
mesh, so no crease/spike forms at the contact boundary. Deeply-penetrating verts are
lifted fully onto the surface (kills the pass-through), shallow ones feather out.

Measurement reuses the hand_thumb_fit standard: a vertex is INSIDE the bar when its
radial dist < r - 0.0015. We report that count before and after the pass (target 0),
across ALL grip verts (5 fingers + thumb + palm), not just the thumb.

Usage:
  blender --background --python hand_v4_gripfix.py -- \
      <in_v4.glb> <out_dir> [<out_gripfix.glb>] \
      [--eps E] [--k K] [--smooth N] [--curl C] [--thumb t1,t2,t3] [--r R] \
      [--measure-only]
"""
import bpy, sys, math, os
from mathutils import Vector

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

INSIDE_MARGIN = 0.0015   # hand_thumb_fit "inside" standard: d < r - this


# ------------------------------------------------------------------ helpers
def _args():
    argv = sys.argv[sys.argv.index("--") + 1:]
    pos = [a for a in argv if not a.startswith("--") and "=" not in a.split(" ")[0][:0]]
    # simple flag parse
    d = {"eps": 0.0008, "k": 650.0, "smooth": 2, "curl": None,
         "thumb": None, "r": None, "barx": None, "measure_only": False}
    plain = []
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--eps": d["eps"] = float(argv[i + 1]); i += 2
        elif a == "--k": d["k"] = float(argv[i + 1]); i += 2
        elif a == "--smooth": d["smooth"] = int(argv[i + 1]); i += 2
        elif a == "--curl":
            # single value -> all 3 joints; comma list -> per joint (j1,j2,j3)
            vals = [float(x) for x in argv[i + 1].split(",")]
            d["curl"] = vals if len(vals) == 3 else [vals[0]] * 3
            i += 2
        elif a == "--thumb": d["thumb"] = [float(x) for x in argv[i + 1].split(",")]; i += 2
        elif a == "--r": d["r"] = float(argv[i + 1]); i += 2
        elif a == "--barx": d["barx"] = float(argv[i + 1]); i += 2
        elif a == "--measure-only": d["measure_only"] = True; i += 1
        else: plain.append(a); i += 1
    return plain, d


def _load(glb):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    return mesh, arm


def _apply_pose(arm, curl=None, thumb=None):
    """Pose the closed grip. curl overrides the per-joint angle; thumb overrides
    the 3-tuple GRIP_THUMB. Falls back to hand_sep_v4 constants."""
    if curl is not None:
        for f in H.FINGERS:
            H.GRIP_CURL[f] = (curl[0], curl[1], curl[2])
    if thumb is not None:
        H.GRIP_THUMB = tuple(thumb)
    H.pose_grip(arm, ".L")


def _bake_pose_to_mesh(mesh):
    """Apply the Armature modifier so the current pose is frozen into mesh verts."""
    bpy.ops.object.select_all(action='DESELECT')
    mesh.select_set(True)
    bpy.context.view_layer.objects.active = mesh
    for mod in list(mesh.modifiers):
        if mod.type == 'ARMATURE':
            bpy.ops.object.modifier_apply(modifier=mod.name)


def _radial(co, bx, bz):
    return math.hypot(co.x - bx, co.z - bz)


def _count_inside(mesh, bar):
    """Count mesh verts whose radial dist to the bar axis < r - INSIDE_MARGIN,
    plus deepest penetration. Uses evaluated mesh (post-pose, post-offset)."""
    bx, bz, r = bar
    dg = mesh.evaluated_get(bpy.context.evaluated_depsgraph_get())
    me = dg.to_mesh()
    mw = mesh.matrix_world
    inside = 0; mind = 1e9
    for v in me.vertices:
        co = mw @ v.co
        d = _radial(co, bx, bz)
        if d < r - INSIDE_MARGIN:
            inside += 1
            mind = min(mind, d)
    mesh.to_mesh_clear()
    return inside, (mind if inside else r)


def _softplus(x, k):
    # numerically stable log(1+exp(k*x))/k
    kx = k * x
    if kx > 30.0:
        return x
    if kx < -30.0:
        return 0.0
    return math.log1p(math.exp(kx)) / k


def collision_offset(mesh, bar, eps, k, smooth_iters):
    """Radial softmax collision pass on the BAKED (posed) mesh. Returns #verts moved.
    Only touches verts within a bounding box around the bar so the rest of the body
    is untouched. Optional light Laplacian smooth of the moved band tidies any
    residual jaggies WITHOUT re-penetrating (re-projected after)."""
    bx, bz, r = bar
    target = r + eps
    # region of interest: near the bar in X-Z, along the hand's Y span
    XZ_R = 0.06          # only verts within 6cm of the bar axis radially
    Y_LO, Y_HI = -0.14, 0.20
    me = mesh.data
    moved = []
    for v in me.vertices:
        co = v.co
        if not (Y_LO < co.y < Y_HI):
            continue
        dx = co.x - bx; dz = co.z - bz
        d = math.hypot(dx, dz)
        if d > XZ_R or d < 1e-6:
            continue
        new_d = target + _softplus(d - target, k)
        if new_d - d > 1e-6:
            s = new_d / d
            v.co = Vector((bx + dx * s, co.y, bz + dz * s))
            moved.append(v.index)
    me.update()

    if smooth_iters and moved:
        import bmesh
        bm = bmesh.new(); bm.from_mesh(me)
        bm.verts.ensure_lookup_table()
        mset = set(moved)
        # include one ring of neighbours so the blend feathers, then re-project
        band = set(moved)
        for vi in moved:
            for e in bm.verts[vi].link_edges:
                band.add(e.other_vert(bm.verts[vi]).index)
        bverts = [bm.verts[i] for i in band]
        for _ in range(smooth_iters):
            bmesh.ops.smooth_vert(bm, verts=bverts, factor=0.5,
                                  use_axis_x=True, use_axis_y=True, use_axis_z=True)
            # re-project any vert that smoothing pushed back inside the bar
            for vv in bverts:
                dx = vv.co.x - bx; dz = vv.co.z - bz
                d = math.hypot(dx, dz)
                if 1e-6 < d < target:
                    s = target / d
                    vv.co = Vector((bx + dx * s, vv.co.y, bz + dz * s))
        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.to_mesh(me); bm.free()
        me.update()
    return len(moved)


def _add_bar(bar):
    bx, bz, r = bar
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=0.32, vertices=64,
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


CAMS = {
    "front34": ([0.98, -0.40, 0.66], [0.845, 0.0, 0.512], 92),
    "thumbside": ([0.82, -0.60, 0.60], [0.83, -0.02, 0.515], 96),
    "knuckle": ([0.98, -0.40, 0.66], [0.828, -0.02, 0.520], 150),
    "topdown": ([0.86, -0.10, 0.82], [0.855, 0.02, 0.512], 110),
}


def render_crops(mesh, bar, out_dir, tag):
    b = _add_bar(bar)
    sc = bpy.context.scene
    H._studio(sc)
    sc.render.resolution_x = sc.render.resolution_y = 900
    paths = []
    for name, (loc, tgt, lens) in CAMS.items():
        H._cam(loc, tgt, lens=lens)
        p = "%s/%s_%s.png" % (out_dir, tag, name)
        sc.render.filepath = p
        bpy.ops.render.render(write_still=True)
        paths.append(p)
        print("CROP", p)
    bpy.data.objects.remove(b, do_unlink=True)
    return paths


def _export(path, mesh):
    bpy.ops.object.select_all(action='DESELECT')
    mesh.select_set(True)
    bpy.context.view_layer.objects.active = mesh
    try: bpy.ops.file.pack_all()
    except Exception as e: print("pack warn", e)
    bpy.ops.export_scene.gltf(
        filepath=path, export_format='GLB', use_selection=True,
        export_apply=False, export_yup=True, export_image_format='AUTO',
        export_texcoords=True, export_normals=True, export_materials='EXPORT')


def main():
    plain, d = _args()
    glb = plain[0]
    out_dir = plain[1]
    out_glb = plain[2] if len(plain) > 2 else None
    os.makedirs(out_dir, exist_ok=True)

    bar = list(H.GRIP_BAR)
    if d["r"] is not None:
        bar[2] = d["r"]
    if d["barx"] is not None:
        bar[0] = d["barx"]
    tag = "e%.4f_k%.0f_s%d" % (d["eps"], d["k"], d["smooth"])
    if d["curl"] is not None: tag += "_c%s" % "-".join("%.0f" % x for x in d["curl"])
    if d["thumb"] is not None: tag += "_t%s" % "-".join("%.0f" % x for x in d["thumb"])
    if d["barx"] is not None: tag += "_bx%.3f" % d["barx"]
    if d["r"] is not None: tag += "_r%.4f" % d["r"]

    mesh, arm = _load(glb)
    _apply_pose(arm, curl=d["curl"], thumb=d["thumb"])

    before, before_min = _count_inside(mesh, bar)
    print("BAR", bar)
    print("PEN_BEFORE inside=%d deepest=%.4f (r=%.4f)" % (before, before_min, bar[2]))

    if d["measure_only"]:
        render_crops(mesh, bar, out_dir, "before")
        return

    _bake_pose_to_mesh(mesh)
    # re-measure after bake (should match before; sanity that bake == pose)
    baked_in, _ = _count_inside(mesh, bar)
    print("PEN_BAKED inside=%d" % baked_in)

    nmoved = collision_offset(mesh, bar, d["eps"], d["k"], d["smooth"])
    after, after_min = _count_inside(mesh, bar)
    print("MOVED verts=%d" % nmoved)
    print("PEN_AFTER inside=%d deepest=%.4f (r=%.4f)" % (after, after_min, bar[2]))

    paths = render_crops(mesh, bar, out_dir, tag)
    print("RESULT tag=%s before=%d after=%d moved=%d" % (tag, before, after, nmoved))

    if out_glb:
        _export(out_glb, mesh)
        print("EXPORTED", out_glb, os.path.getsize(out_glb))


if __name__ == "__main__":
    main()
