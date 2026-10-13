"""Shared build/deform/pose/render helpers for the body_rig_v5 rebuild.

The body MESH is built exactly as scratch/n4_dl_start.py section 1 (approved look:
MPFB macro human + muscle targets + skin material + subsurf). This module ONLY
owns the deformation layer (rig choice, skin weights, corrective helpers) and a
simple FK pose/render harness for the acceptance battery.

Import from a headless Blender script:
    import importlib.util, os
    spec = importlib.util.spec_from_file_location("rigv5_lib", "<abs>/rigv5_lib.py")
    L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
"""
import bpy, addon_utils, os, math
from mathutils import Vector

HERE = os.path.dirname(os.path.abspath(__file__))

MACRO = {"gender": 1.0, "age": 0.45, "muscle": 1.0, "weight": 0.85,
         "proportions": 0.7, "height": 0.60, "cupsize": 0.5, "firmness": 0.9,
         "race": {"asian": 0.34, "caucasian": 0.33, "african": 0.33}}

TARGETS = [
    ("arms/l-upperarm-muscle-incr", 1.0), ("arms/r-upperarm-muscle-incr", 1.0),
    ("arms/l-lowerarm-muscle-incr", 0.8), ("arms/r-lowerarm-muscle-incr", 0.8),
    ("arms/l-upperarm-shoulder-muscle-incr", 1.0), ("arms/r-upperarm-shoulder-muscle-incr", 1.0),
    ("torso/torso-muscle-pectoral-incr", 1.0), ("torso/torso-muscle-dorsi-incr", 1.0),
    ("legs/l-upperleg-muscle-incr", 0.85), ("legs/r-upperleg-muscle-incr", 0.85),
    ("legs/l-lowerleg-muscle-incr", 0.8), ("legs/r-lowerleg-muscle-incr", 0.8),
    ("torso/torso-vshape-incr", 0.25), ("stomach/stomach-tone-incr", 1.0),
    ("torso/measure-shoulder-dist-incr", 0.2), ("torso/measure-waist-circ-decr", 0.1),
]


def enable_mpfb():
    addon_utils.enable('bl_ext.user_default.mpfb', default_set=True, persistent=True)


def build_body():
    """Approved MPFB body mesh (no rig). Returns the body object."""
    from bl_ext.user_default.mpfb.services.humanservice import HumanService
    from bl_ext.user_default.mpfb.services.targetservice import TargetService
    from bl_ext.user_default.mpfb.services.locationservice import LocationService
    body = HumanService.create_human(macro_detail_dict=MACRO)
    TDIR = LocationService.get_mpfb_data("targets")
    for rel, w in TARGETS:
        p = os.path.join(TDIR, rel + ".target.gz")
        TargetService.load_target(body, p, weight=w, name=os.path.basename(rel))
    for p in body.data.polygons:
        p.use_smooth = True
    sub = body.modifiers.new("sub", 'SUBSURF'); sub.levels = 1; sub.render_levels = 2
    m = bpy.data.materials.new("skin"); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (0.60, 0.42, 0.32, 1)
    b.inputs["Roughness"].default_value = 0.5
    body.data.materials.clear(); body.data.materials.append(m)
    return body


def build_shorts(body):
    """Approved mid-thigh drawers, built exactly as n4_dl_start.py (from the
    evaluated body band; hem projected onto each leg frame). Returns shorts obj.
    Call after build_body(), BEFORE add_rig()."""
    import bmesh as _bmesh
    W_TOP, W_HEM = 1.06, 0.62
    deps = bpy.context.evaluated_depsgraph_get()
    me = bpy.data.meshes.new_from_object(body.evaluated_get(deps))
    band = set(v.index for v in me.vertices if W_HEM <= v.co.z <= W_TOP and abs(v.co.x) < 0.28)
    faces = [p for p in me.polygons if all(vi in band for vi in p.vertices)]
    vmap = {}; sverts = []
    for p in faces:
        for vi in p.vertices:
            if vi not in vmap:
                v = me.vertices[vi]
                vmap[vi] = len(sverts); sverts.append(v.co + v.normal * 0.006)
    sfaces = [tuple(vmap[vi] for vi in p.vertices) for p in faces]
    smesh = bpy.data.meshes.new("shorts")
    smesh.from_pydata([tuple(c) for c in sverts], [], sfaces); smesh.update()

    def leg_frame(sign):
        up = [v.co for v in me.vertices if 0.76 < v.co.z < 0.86 and 0.02 < sign * v.co.x < 0.28]
        lo = [v.co for v in me.vertices if 0.50 < v.co.z < 0.58 and 0.02 < sign * v.co.x < 0.28]
        cU = sum(up, Vector()) / len(up); cL = sum(lo, Vector()) / len(lo)
        ax = (cU - cL).normalized()
        return ax, cL + ax * ((W_HEM - cL.z) / ax.z)
    FR = {1: leg_frame(1), -1: leg_frame(-1)}
    bmm = _bmesh.new(); bmm.from_mesh(smesh)
    zmid = (W_HEM + W_TOP) * 0.5
    hemv = [v for v in bmm.verts if v.is_boundary and v.co.z < zmid]
    topv = [v for v in bmm.verts if v.is_boundary and v.co.z >= zmid]

    def project_hem():
        for v in hemv:
            ax, Q = FR[1] if v.co.x >= 0 else FR[-1]
            v.co -= ax * ((v.co - Q).dot(ax))
    project_hem()
    for _ in range(3):
        _bmesh.ops.smooth_vert(bmm, verts=hemv, factor=0.5, use_axis_x=True, use_axis_y=True, use_axis_z=True)
        project_hem()
    for v in topv:
        v.co.z = W_TOP
    for _ in range(3):
        _bmesh.ops.smooth_vert(bmm, verts=topv, factor=0.5, use_axis_x=True, use_axis_y=True, use_axis_z=False)
    bmm.to_mesh(smesh); bmm.free(); smesh.update()
    for p in smesh.polygons:
        p.use_smooth = True
    shorts = bpy.data.objects.new("shorts", smesh)
    bpy.context.scene.collection.objects.link(shorts)
    sol = shorts.modifiers.new("sol", 'SOLIDIFY'); sol.thickness = 0.004
    ssub = shorts.modifiers.new("sub", 'SUBSURF'); ssub.levels = 1; ssub.render_levels = 2
    fm = bpy.data.materials.new("fabric"); fm.use_nodes = True
    fb = fm.node_tree.nodes["Principled BSDF"]
    fb.inputs["Base Color"].default_value = (0.015, 0.015, 0.018, 1)
    fb.inputs["Roughness"].default_value = 0.9
    smesh.materials.append(fm)
    bpy.data.meshes.remove(me)
    return shorts


def attach_shorts(shorts, arm, body):
    """Transfer body weights to shorts, parent to rig, armature + shrinkwrap.
    Exactly as n4_dl_start.py section 2. Call after add_rig()."""
    bpy.context.view_layer.objects.active = body
    shorts.select_set(True); body.select_set(True)
    with bpy.context.temp_override(object=body, active_object=body,
                                   selected_editable_objects=[body, shorts]):
        bpy.ops.object.data_transfer(data_type='VGROUP_WEIGHTS',
                                     vert_mapping='POLYINTERP_NEAREST',
                                     layers_select_src='ALL', layers_select_dst='NAME')
    shorts.parent = arm
    amod = shorts.modifiers.new("arm", 'ARMATURE'); amod.object = arm
    swr = shorts.modifiers.new("swr", 'SHRINKWRAP')
    swr.target = body
    swr.wrap_method = 'NEAREST_SURFACEPOINT'
    swr.wrap_mode = 'OUTSIDE'
    swr.offset = 0.005


def add_rig(body, rig_name="default"):
    from bl_ext.user_default.mpfb.services.humanservice import HumanService
    arm = HumanService.add_builtin_rig(body, rig_name, import_weights=True)
    for pbone in arm.pose.bones:
        pbone.rotation_mode = 'XYZ'
    return arm


# explicit-per-side child bones whose junction WITH THEIR PARENT is a true
# flexing joint (a crease that linear-blend pinches). Mid-limb segment bones
# (upperleg02/upperarm02/...) are deliberately EXCLUDED so muscle BELLIES stay
# untouched by the corrective smooth -- only these joint rings get relaxed.
JOINT_CHILDREN = (
    ["upperleg01", "lowerleg01", "foot",            # hip / knee / ankle
     "upperarm01", "lowerarm01", "wrist"]           # shoulder / elbow / wrist
    + ["finger%d-%d" % (fi, sg) for fi in (1, 2, 3, 4, 5) for sg in (1, 2, 3)]
)


def build_joint_mask(body, arm, *, name="cs_joint_mask", boost=2.0):
    """Paint a vertex group whose weight = 'jointness': for each anatomical
    joint (a child deform bone + its actual armature parent) the crease ring is
    exactly the verts that straddle BOTH bones, so min(w_child, w_parent) marks
    it. Take the max over all joints, boost + clamp to [0,1]. Muscle bellies get
    0 -> the masked corrective smooth leaves them at full n4 detail. Returns the
    vertex-group name (feed it to configure_deform(cs_vgroup=...))."""
    pairs = []
    for side in ("L", "R"):
        for base in JOINT_CHILDREN:
            child = "%s.%s" % (base, side)
            b = arm.data.bones.get(child)
            if b is None or b.parent is None:
                continue
            pairs.append((child, b.parent.name))
    name2idx = {vg.name: vg.index for vg in body.vertex_groups}
    needed = {g for pr in pairs for g in pr if g in name2idx}
    need_idx2name = {name2idx[g]: g for g in needed}
    wv = {g: {} for g in needed}
    for v in body.data.vertices:
        for gr in v.groups:
            gn = need_idx2name.get(gr.group)
            if gn is not None and gr.weight > 0.0:
                wv[gn][v.index] = gr.weight
    vg = body.vertex_groups.get(name) or body.vertex_groups.new(name=name)
    pairs = [(a, b) for a, b in pairs if a in wv and b in wv]
    for v in body.data.vertices:
        vi = v.index
        m = 0.0
        for a, b in pairs:
            mm = min(wv[a].get(vi, 0.0), wv[b].get(vi, 0.0))
            if mm > m:
                m = mm
        if m > 0.0:
            vg.add([vi], min(1.0, m * boost), 'REPLACE')
    return name


def configure_deform(body, *, preserve_volume=True, corrective=True,
                     cs_factor=0.45, cs_iters=8, cs_type='LENGTH_WEIGHTED',
                     cs_rest_from_bind=False, cs_vgroup=None):
    """Set the deformation stack on the body. Order in the modifier stack:
    ARMATURE -> (CORRECTIVE_SMOOTH) -> SUBSURF. Returns the corrective mod or None.
    cs_vgroup: if given, the corrective smooth is MASKED to that vertex group
    (joint rings only) so muscle bellies keep full detail.
    """
    am = next(m for m in body.modifiers if m.type == 'ARMATURE')
    am.use_deform_preserve_volume = bool(preserve_volume)
    # drop any prior corrective smooth
    for mm in list(body.modifiers):
        if mm.type == 'CORRECTIVE_SMOOTH':
            body.modifiers.remove(mm)
    cs = None
    if corrective:
        cs = body.modifiers.new("csmooth", 'CORRECTIVE_SMOOTH')
        cs.factor = cs_factor
        cs.iterations = cs_iters
        cs.smooth_type = cs_type            # 'SIMPLE' or 'LENGTH_WEIGHTED'
        cs.use_only_smooth = False
        cs.use_pin_boundary = False
        if cs_vgroup:
            cs.vertex_group = cs_vgroup     # mask to joint rings only
        # ORCO = pre-deform original (bind) coords as rest; no bind op needed
        cs.rest_source = 'BIND' if cs_rest_from_bind else 'ORCO'
    # keep subsurf last
    sub = next((m for m in body.modifiers if m.type == 'SUBSURF'), None)
    # reorder: armature, corrective, subsurf
    order = [am]
    if cs is not None:
        order.append(cs)
    if sub is not None:
        order.append(sub)
    names = [m.name for m in order]
    # move each to bottom in order
    for nm in names:
        with bpy.context.temp_override(object=body):
            idx = body.modifiers.find(nm)
            bpy.ops.object.modifier_move_to_index(modifier=nm, index=len(body.modifiers) - 1)
    return cs


def bind_corrective(body):
    """Bind corrective-smooth rest to the current (bind/rest) mesh state."""
    cs = next((m for m in body.modifiers if m.type == 'CORRECTIVE_SMOOTH'), None)
    if cs is None:
        return
    cs.rest_source = 'BIND'
    with bpy.context.temp_override(object=body, active_object=body):
        try:
            bpy.ops.object.correctivesmooth_bind(modifier=cs.name)
        except Exception as e:
            print("BIND corrective failed:", e)


def clean_weights(body, *, limit=4, normalize=True, smooth_iters=0, smooth_factor=0.5):
    """Limit total influences, normalize, optional smooth. Body must be selectable."""
    bpy.context.view_layer.objects.active = body
    body.select_set(True)
    with bpy.context.temp_override(object=body, active_object=body,
                                   selected_editable_objects=[body], selected_objects=[body]):
        if limit:
            bpy.ops.object.vertex_group_limit_total(group_select_mode='BONE_DEFORM', limit=limit)
        if normalize:
            bpy.ops.object.vertex_group_normalize_all(group_select_mode='BONE_DEFORM', lock_active=False)
    if smooth_iters:
        # smooth needs weight-paint context; use bmesh-free op via edit mode
        bpy.context.view_layer.objects.active = body
        bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
        with bpy.context.temp_override(object=body, active_object=body):
            for _ in range(smooth_iters):
                bpy.ops.object.vertex_group_smooth(group_select_mode='BONE_DEFORM',
                                                   factor=smooth_factor)
        bpy.ops.object.mode_set(mode='OBJECT')


# ------------------------------------------------------------------ posing
def pose_reset(arm):
    for pb in arm.pose.bones:
        pb.rotation_euler = (0, 0, 0)
        pb.location = (0, 0, 0)


def setb(arm, name, x=0.0, y=0.0, z=0.0):
    arm.pose.bones[name].rotation_euler = (x, y, z)


def faceY(arm):
    pb = arm.pose.bones
    mwa = arm.matrix_world
    return 1.0 if (mwa @ pb["toe2-1.L"].tail - mwa @ pb["foot.L"].head).y > 0 else -1.0


def flex_sign(arm, bone, ref_head, target_head, axis=0, probe=20.0):
    """Return +1/-1: the X-rot sign that FLEXES (brings ref toward target)."""
    pb = arm.pose.bones; mwa = arm.matrix_world
    def d():
        return (mwa @ pb[ref_head].head - mwa @ pb[target_head].head).length
    e = pb[bone].rotation_euler; old = e[axis]
    e[axis] = old + math.radians(probe); bpy.context.view_layer.update(); dp = d()
    e[axis] = old - math.radians(probe); bpy.context.view_layer.update(); dm = d()
    e[axis] = old; bpy.context.view_layer.update()
    return 1.0 if dp < dm else -1.0


def curl_sign(arm, side):
    """Return +1/-1 X-rot sign that curls the fingers of a hand toward the palm."""
    pb = arm.pose.bones; mwa = arm.matrix_world
    tip = "finger3-3.%s" % side; ref = "wrist.%s" % side
    d0 = (mwa @ pb[tip].tail - mwa @ pb[ref].head).length
    e = pb["finger3-1.%s" % side].rotation_euler; o = e[0]
    e[0] = o + math.radians(20); bpy.context.view_layer.update()
    dp = (mwa @ pb[tip].tail - mwa @ pb[ref].head).length
    e[0] = o; bpy.context.view_layer.update()
    return 1.0 if dp < d0 else -1.0


def wrap_grip(arm, side, axis_pt, axis_dir, R, *, flesh=0.009,
              caps=(70, 95, 75), thumb=(35, 40, 40)):
    """Curl fingers 2..5 of `side` around a cylinder (axis_pt,axis_dir,radius R)
    until each segment's tail reaches the cylinder surface (R+flesh). Thumb set
    to a fixed opposed wrap. Measured via bone-tail radial distance (fast, no
    mesh eval). Returns dict of final per-joint angles (deg)."""
    pb = arm.pose.bones; mwa = arm.matrix_world
    ad = Vector(axis_dir).normalized(); ap = Vector(axis_pt)
    cs = curl_sign(arm, side)

    def radial(name, tail=True):
        p = mwa @ (pb[name].tail if tail else pb[name].head)
        v = p - ap
        return (v - ad * v.dot(ad)).length

    out = {}
    for fi in (2, 3, 4, 5):
        for sg in (1, 2, 3):
            bn = "finger%d-%d.%s" % (fi, sg, side)
            cap = math.radians(caps[sg - 1])
            step = math.radians(4)
            ang = 0.0
            while ang + step <= cap:
                pb[bn].rotation_euler = (cs * (ang + step), 0, 0)
                bpy.context.view_layer.update()
                if radial(bn, tail=True) <= R + flesh:
                    break
                ang += step
            pb[bn].rotation_euler = (cs * ang, 0, 0)
            out[bn] = math.degrees(cs * ang)
    bpy.context.view_layer.update()
    # thumb: opposed wrap (fixed, mirrored adduction handled by CMC sign)
    zsgn = -1.0 if side == "L" else 1.0
    pb["finger1-1.%s" % side].rotation_euler = (math.radians(thumb[0]), 0,
                                                zsgn * math.radians(35))
    pb["finger1-2.%s" % side].rotation_euler = (math.radians(thumb[1]), 0, 0)
    pb["finger1-3.%s" % side].rotation_euler = (math.radians(thumb[2]), 0, 0)
    bpy.context.view_layer.update()
    return out


# ------------------------------------------------------------------ render
def studio(scn, *, view_transform='Standard', exposure=None, samples=256):
    """Dark-studio look. view_transform 'Standard' (default -- reviewer-requested,
    faithful geometry, no tone-map wash) or 'AgX'/'AgX-Punchy' (the n4 dramatic
    grade, used for the approved-look A/B). Exposure auto-picks per transform so
    the key light does not clip to white under Standard."""
    try:
        scn.render.engine = 'BLENDER_EEVEE'
    except TypeError:
        scn.render.engine = 'BLENDER_EEVEE_NEXT'
    if exposure is None:
        exposure = -1.6 if view_transform == 'Standard' else -0.4
    scn.view_settings.exposure = exposure
    try:
        if view_transform.startswith('AgX'):
            scn.view_settings.view_transform = 'AgX'
            scn.view_settings.look = 'AgX - Punchy'
        else:
            scn.view_settings.view_transform = 'Standard'
            scn.view_settings.look = 'None'
    except TypeError:
        pass
    world = bpy.data.worlds.new("W"); scn.world = world; world.use_nodes = True
    world.node_tree.nodes["Background"].inputs[0].default_value = (0.035, 0.035, 0.04, 1)
    world.node_tree.nodes["Background"].inputs[1].default_value = 0.35
    try:
        scn.eevee.taa_render_samples = samples
    except Exception:
        pass
    for attr in ("use_shadow_jitter", "use_raytracing"):
        try:
            setattr(scn.eevee, attr, True)
        except Exception:
            pass
    # denoise the EEVEE-Next raytraced result -> kills the skin speckle
    try:
        scn.eevee.use_taa_reprojection = True
    except Exception:
        pass
    try:
        vl = scn.view_layers[0]
        vl.use_pass_combined = True
        vl.cycles.use_denoising = True
    except Exception:
        pass


def add_lights(scn, body_c, fy):
    for kx, ky, kz, e, s in ((0.8, fy * 1.2, 1.9, 120, 0.8), (-0.9, fy * 0.8, 1.2, 60, 1.2),
                             (0.2, -fy * 1.2, 1.6, 80, 0.9), (0.1, fy * 0.5, 0.2, 40, 0.8)):
        L = bpy.data.lights.new("k", 'AREA'); L.energy = e; L.size = s
        o = bpy.data.objects.new("k", L); scn.collection.objects.link(o)
        o.location = body_c + Vector((kx, ky, kz))
        o.rotation_euler = (body_c - o.location).normalized().to_track_quat('-Z', 'Y').to_euler()


def add_floor(scn, sole_z):
    bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, sole_z))
    floor = bpy.context.active_object
    fmat = bpy.data.materials.new("floor"); fmat.use_nodes = True
    fB = fmat.node_tree.nodes["Principled BSDF"]
    fB.inputs["Base Color"].default_value = (0.05, 0.05, 0.055, 1)
    fB.inputs["Roughness"].default_value = 0.95
    floor.data.materials.append(fmat)
    return floor


def make_cam(scn, lens=65):
    camd = bpy.data.cameras.new("C"); cam = bpy.data.objects.new("C", camd)
    scn.collection.objects.link(cam); scn.camera = cam; camd.lens = lens
    return cam


def shoot(scn, cam, path, center, size, d, res_x=720, res_y=1280):
    fov = 2 * math.atan(18.0 / cam.data.lens)
    dist = (size * 0.6) / math.tan(fov / 2) * 1.15
    loc = center + Vector(d).normalized() * dist
    cam.location = loc
    cam.rotation_euler = (center - loc).normalized().to_track_quat('-Z', 'Y').to_euler()
    scn.render.resolution_x = res_x; scn.render.resolution_y = res_y
    scn.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print("R", os.path.basename(path))
