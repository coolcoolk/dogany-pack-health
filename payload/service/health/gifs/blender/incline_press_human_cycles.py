"""
Incline dumbbell press -- muscular human loop, CYCLES quality pass.

Upgrade of incline_press_human.py (original preserved). Same motion, framing,
and concept (gray sculpted body + red target pectoral). ONLY the render engine,
materials, and lighting change:
  - Engine: Workbench -> Cycles (CPU), samples + denoising.
  - Body: neutral gray skin, weak subsurface (flesh feel), mild spec.
  - Chest: vivid red base + light emission so it pops against the gray.
  - Lighting: studio 3-point soft area lights (key / fill / rim) + bright
    neutral world + floor shadow.

Usage:
  Blender --background --python incline_press_human_cycles.py -- \
      --stage {still|render} [--frames N] [--recline DEG] [--t T] [--samples S]

  still  : build the full reclined scene, render ONE frame at pose --t
           (default 1.0 = top lockout) to files/tmp/cycles_still.png -- for
           fast material/lighting tuning.
  render : full FRAMES ping-pong loop into files/tmp/blender_frames_cycles.

All coordinates: Z up. Human faces -Y. Character LEFT arm = +X side.
"""
import bpy, sys, math, os, tempfile
from mathutils import Vector, Matrix

# ---------------- arg parse ----------------
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def argval(flag, default):
    return argv[argv.index(flag) + 1] if flag in argv else default
STAGE    = argval("--stage", "render")
FRAMES   = int(argval("--frames", "24"))
RECLINE  = float(argval("--recline", "52"))   # degrees reclined from vertical
T_STILL  = float(argval("--t", "1.0"))        # pose for the still tuning frame
SAMPLES  = int(argval("--samples", "96"))
WORK     = os.environ.get("BLENDER_WORK", os.path.join(tempfile.gettempdir(), "blender_work"))
FRAMEDIR = os.path.join(WORK, "frames_cycles")
STILLOUT = os.path.join(WORK, "cycles_still.png")
_HERE    = os.path.dirname(os.path.abspath(__file__))
HUMANBLEND = os.path.join(_HERE, "human.blend")
if not os.path.exists(HUMANBLEND):
    HUMANBLEND = os.path.join(WORK, "human.blend")

# ---------------- load base human ----------------
bpy.ops.wm.open_mainfile(filepath=HUMANBLEND)
sc = bpy.context.scene
human = bpy.data.objects.get("Human")
rig   = bpy.data.objects.get("Human.rig")

# ---------------- material helpers ----------------
def set_in(bsdf, name, val):
    """Set a Principled input only if that socket exists (version-robust)."""
    if name in bsdf.inputs:
        bsdf.inputs[name].default_value = val
        return True
    return False

def skin_gray(name, rgb):
    """Neutral gray skin: weak subsurface for flesh, mild spec, matte-ish."""
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    set_in(b, "Base Color", (*rgb, 1.0))
    set_in(b, "Roughness", 0.52)
    # subsurface -- flesh translucency; keep tint neutral so body stays gray
    set_in(b, "Subsurface Weight", 0.18)
    set_in(b, "Subsurface", 0.18)          # pre-4.0 socket fallback
    set_in(b, "Subsurface Radius", (0.30, 0.20, 0.16))
    set_in(b, "Subsurface Scale", 0.045)
    set_in(b, "Subsurface Color", (rgb[0] * 0.9, rgb[1] * 0.72, rgb[2] * 0.66, 1.0))
    # gentle specular for volume without plastic sheen
    set_in(b, "Specular IOR Level", 0.32)
    set_in(b, "Specular", 0.32)            # pre-4.0 socket fallback
    m.diffuse_color = (*rgb, 1.0)
    return m

def muscle_red(name, rgb):
    """Vivid target-muscle red: saturated base + light self-emission to pop."""
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    set_in(b, "Base Color", (*rgb, 1.0))
    set_in(b, "Roughness", 0.46)
    set_in(b, "Subsurface Weight", 0.12)
    set_in(b, "Subsurface", 0.12)
    set_in(b, "Subsurface Radius", (0.36, 0.12, 0.10))
    set_in(b, "Subsurface Scale", 0.04)
    set_in(b, "Specular IOR Level", 0.35)
    set_in(b, "Specular", 0.35)
    # light emission so the pec reads clearly against the gray body
    set_in(b, "Emission Color", (0.85, 0.05, 0.05, 1.0))
    set_in(b, "Emission", (0.85, 0.05, 0.05, 1.0))   # pre-4.0 socket
    set_in(b, "Emission Strength", 0.45)
    m.diffuse_color = (*rgb, 1.0)
    return m

def plain_mat(name, rgb, rough=0.55, metal=0.0):  # estate-scrub:allow(metal material, 3D render)
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    set_in(b, "Base Color", (*rgb, 1.0))
    set_in(b, "Roughness", rough)
    set_in(b, "Metallic", metal)  # estate-scrub:allow(metal material, 3D render)
    m.diffuse_color = (*rgb, 1.0)
    return m

gray = skin_gray("BodyGray", (0.40, 0.41, 0.43))
red  = muscle_red("ChestRed", (0.82, 0.04, 0.04))
human.data.materials.clear()
human.data.materials.append(gray)   # index 0
human.data.materials.append(red)    # index 1

# assign red to pectoral region faces (front upper torso).
me = human.data
wm = human.matrix_world
red_count = 0
for poly in me.polygons:
    c = wm @ poly.center
    n = (wm.to_3x3() @ poly.normal)
    if (1.35 <= c.z <= 1.53 and c.y < -0.04 and abs(c.x) < 0.19 and n.y < -0.12):
        poly.material_index = 1
        red_count += 1
print("REDFACES", red_count)

# ---------------- pose helper ----------------
def point_bone(pbname, direction):
    pb = rig.pose.bones[pbname]
    d = Vector(direction).normalized()
    quat = d.to_track_quat('Y', 'Z')
    loc = pb.matrix.to_translation()
    m = quat.to_matrix().to_4x4()
    m.translation = loc
    pb.matrix = m
    bpy.context.view_layer.update()

bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode='POSE')

def apply_pose(t):
    def lerp(a, b): return Vector(a).lerp(Vector(b), t)
    ua_L = lerp((0.75, -0.28, 0.05), (0.16, -0.12, 0.98))
    fa_L = lerp((0.18, -0.30, 0.94), (0.14, -0.10, 0.99))
    ua_R = Vector((-ua_L.x, ua_L.y, ua_L.z))
    fa_R = Vector((-fa_L.x, fa_L.y, fa_L.z))
    point_bone("upperarm01.L", ua_L)
    point_bone("lowerarm01.L", fa_L)
    point_bone("upperarm01.R", ua_R)
    point_bone("lowerarm01.R", fa_R)

# ---------------- render setup: CYCLES + studio lighting ----------------
def setup_render(res=512):
    sc.render.engine = 'CYCLES'
    sc.cycles.device = 'CPU'
    sc.cycles.samples = SAMPLES
    sc.cycles.use_denoising = True
    sc.render.resolution_x = res
    sc.render.resolution_y = res
    sc.render.film_transparent = False
    sc.view_settings.view_transform = 'Standard'  # keep neutral grays true
    # bright neutral world
    w = bpy.data.worlds.get("W") or bpy.data.worlds.new("W")
    sc.world = w
    w.use_nodes = True
    bg = w.node_tree.nodes.get("Background")
    if bg:
        bg.inputs[0].default_value = (0.95, 0.95, 0.97, 1.0)
        bg.inputs[1].default_value = 0.72

def add_camera(loc, look, lens=45):
    cam = bpy.data.cameras.new("Cam"); ob = bpy.data.objects.new("Cam", cam)
    bpy.context.collection.objects.link(ob)
    ob.location = loc
    d = (Vector(look) - Vector(loc)).normalized()
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.lens = lens
    sc.camera = ob
    return ob

def add_area(name, loc, look, energy, size):
    lt = bpy.data.lights.new(name, 'AREA')
    lt.energy = energy
    lt.size = size
    lo = bpy.data.objects.new(name, lt)
    bpy.context.collection.objects.link(lo)
    lo.location = loc
    d = (Vector(look) - Vector(loc)).normalized()
    lo.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    return lo

def studio_lights(ctr):
    # camera sits at +X; subject front faces -Y. soft 3-point.
    add_area("Key",  (ctr.x + 2.6, ctr.y - 2.4, ctr.z + 2.6), ctr, 260, 2.6)
    add_area("Fill", (ctr.x - 3.0, ctr.y - 1.6, ctr.z + 1.2), ctr, 55, 4.0)
    add_area("Rim",  (ctr.x - 0.4, ctr.y + 2.6, ctr.z + 2.8), ctr, 150, 2.2)

# ---------------- scene build (recline + bench + dumbbells) ----------------
def add_box(name, dims, loc, rot=(0, 0, 0), rgb=(0.2, 0.2, 0.22)):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc)
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = (dims[0] / 2, dims[1] / 2, dims[2] / 2)
    ob.rotation_euler = rot
    ob.data.materials.append(plain_mat("mat_" + name, rgb))
    return ob

def add_dumbbell(name, rgb=(0.05, 0.05, 0.06)):
    bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.26,
                                         rotation=(0, math.radians(90), 0),
                                         location=(0, 0, 0))
    handle = bpy.context.active_object; handle.name = name
    mm = plain_mat("mat_" + name, rgb, rough=0.35, metal=0.7)  # estate-scrub:allow(metal material, 3D render)
    handle.data.materials.append(mm)
    for sx in (-0.10, 0.10):
        bpy.ops.mesh.primitive_cylinder_add(radius=0.075, depth=0.09,
                                             rotation=(0, math.radians(90), 0),
                                             location=(sx, 0, 0))
        w = bpy.context.active_object
        w.data.materials.append(mm)
        w.parent = handle
        w.matrix_parent_inverse = handle.matrix_world.inverted()
    return handle

def mesh_bbox_world():
    dg = bpy.context.evaluated_depsgraph_get()
    he = human.evaluated_get(dg)
    mn = Vector((1e9,) * 3); mx = Vector((-1e9,) * 3)
    for v in he.data.vertices:
        w = he.matrix_world @ v.co
        for k in range(3):
            mn[k] = min(mn[k], w[k]); mx[k] = max(mx[k], w[k])
    return mn, mx

def build_scene():
    HIP = Vector((0.0, -0.11, 0.90))
    DROP = 0.30
    empty = bpy.data.objects.new("Pivot", None)
    bpy.context.collection.objects.link(empty)
    empty.location = HIP
    rig.parent = empty
    rig.matrix_parent_inverse = empty.matrix_world.inverted()
    empty.rotation_euler = (math.radians(-RECLINE), 0, 0)
    empty.location = HIP + Vector((0, 0, -DROP))
    bpy.context.view_layer.update()

    def bone_head_world(name):
        pb = rig.pose.bones[name]
        return rig.matrix_world @ pb.head
    p_low = bone_head_world("spine01")
    p_high = bone_head_world("spine04")
    axis = (p_high - p_low).normalized()
    back_dir = (empty.matrix_world.to_3x3() @ Vector((0, 1, 0))).normalized()
    normal = back_dir
    length_axis = axis
    side_axis = length_axis.cross(normal).normalized()
    basis = Matrix((side_axis, length_axis, normal)).transposed()
    center = (p_low + p_high) / 2 + back_dir * 0.09 - Vector((0, 0, 0.02))
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=center)
    bench = bpy.context.active_object; bench.name = "Bench"
    bench.matrix_world = Matrix.Translation(center) @ basis.to_4x4() @ Matrix.Diagonal(
        (0.50, 1.05, 0.09)).to_4x4()
    bench.data.materials.append(plain_mat("mat_bench", (0.12, 0.12, 0.14)))
    floor_z = -0.61
    add_box("Post", (0.16, 0.30, center.z - floor_z),
            (center.x, center.y, (center.z + floor_z) / 2),
            rgb=(0.09, 0.09, 0.11))
    add_box("Floor", (10, 10, 0.02), (0, 0, -0.62), rgb=(0.88, 0.88, 0.90))

    db_L = add_dumbbell("DumbbellL")
    db_L.parent = rig; db_L.parent_type = 'BONE'; db_L.parent_bone = "wrist.L"
    db_R = add_dumbbell("DumbbellR")
    db_R.parent = rig; db_R.parent_type = 'BONE'; db_R.parent_bone = "wrist.R"

    # auto-frame side camera across the whole press range
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.mode_set(mode='POSE')
    apply_pose(0.0); mn0, mx0 = mesh_bbox_world()
    apply_pose(1.0); mn1, mx1 = mesh_bbox_world()
    bpy.ops.object.mode_set(mode='OBJECT')
    mn = Vector((min(mn0[k], mn1[k]) for k in range(3)))
    mx = Vector((max(mx0[k], mx1[k]) for k in range(3)))
    ctr = (mn + mx) / 2
    span = max(mx.y - mn.y, mx.z - mn.z)
    dist = span * 1.55 + 1.2
    add_camera((ctr.x + dist, ctr.y, ctr.z), (ctr.x, ctr.y, ctr.z), lens=45)
    return ctr

# ---------------- STILL: single tuning frame ----------------
if STAGE == "still":
    ctr = build_scene()
    setup_render(res=512)
    studio_lights(ctr)
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.mode_set(mode='POSE')
    apply_pose(T_STILL)
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.update()
    sc.render.filepath = STILLOUT
    bpy.ops.render.render(write_still=True)
    print("STILL DONE t=", T_STILL, "->", STILLOUT)
    sys.exit(0)

# ---------------- RENDER: full ping-pong loop ----------------
if STAGE == "render":
    ctr = build_scene()
    setup_render(res=512)
    studio_lights(ctr)
    os.makedirs(FRAMEDIR, exist_ok=True)
    for f in os.listdir(FRAMEDIR):
        if f.startswith("frame_"):
            os.remove(os.path.join(FRAMEDIR, f))
    for i in range(FRAMES):
        phase = i / FRAMES
        t = 1.0 - abs(1.0 - 2.0 * phase)   # triangle 0->1->0
        t = t * t * (3 - 2 * t)             # ease in/out
        bpy.context.view_layer.objects.active = rig
        bpy.ops.object.mode_set(mode='POSE')
        apply_pose(t)
        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.update()
        sc.render.filepath = os.path.join(FRAMEDIR, f"frame_{i:03d}.png")
        bpy.ops.render.render(write_still=True)
    print("RENDER DONE frames=", FRAMES)
    sys.exit(0)

print("SCRIPT LOADED stage=", STAGE)
