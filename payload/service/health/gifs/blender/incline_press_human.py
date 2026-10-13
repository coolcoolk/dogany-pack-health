"""
Incline dumbbell press -- muscular human loop (GymVisual-style proof of concept).

Human + rig: MPFB2 (MakeHuman Plugin For Blender 2), created headless.
Body = gray, target muscle (pectoral / chest) = red highlight.
Motion: incline dumbbell press, bottom (elbows ~90 deg, dumbbells at chest)
        <-> top (arms extended overhead lockout), ping-pong loop.

Usage:
  Blender --background --python incline_press_human.py -- \
      --stage {calib|render} [--frames N] [--recline DEG]

All coordinates: Z up. Human faces -Y. Character LEFT arm = +X side.
"""
import bpy, sys, math, os, tempfile
from mathutils import Vector, Matrix, Quaternion

# ---------------- arg parse ----------------
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
def argval(flag, default):
    return argv[argv.index(flag) + 1] if flag in argv else default
STAGE   = argval("--stage", "render")
FRAMES  = int(argval("--frames", "24"))
RECLINE = float(argval("--recline", "52"))   # degrees reclined from vertical
WORK    = os.environ.get("BLENDER_WORK", os.path.join(tempfile.gettempdir(), "blender_work"))
FRAMEDIR= os.path.join(WORK, "frames")
# persistent MPFB human lives next to this script; tmp copy is a fallback
_HERE   = os.path.dirname(os.path.abspath(__file__))
HUMANBLEND = os.path.join(_HERE, "human.blend")
if not os.path.exists(HUMANBLEND):
    HUMANBLEND = os.path.join(WORK, "human.blend")

# ---------------- load base human ----------------
bpy.ops.wm.open_mainfile(filepath=HUMANBLEND)
sc = bpy.context.scene
human = bpy.data.objects.get("Human")
rig   = bpy.data.objects.get("Human.rig")

# ---------------- materials: gray body + red chest ----------------
def make_mat(name, rgb, rough=0.55):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*rgb, 1.0)
    bsdf.inputs["Roughness"].default_value = rough
    m.diffuse_color = (*rgb, 1.0)   # Workbench viewport color
    return m

gray = make_mat("BodyGray", (0.55, 0.56, 0.58))
red  = make_mat("ChestRed", (0.80, 0.09, 0.09), rough=0.5)
human.data.materials.clear()
human.data.materials.append(gray)   # index 0
human.data.materials.append(red)    # index 1

# assign red to pectoral region faces (front upper torso).
# chest band: z in [1.30,1.52], front (y<-0.02), within shoulder width, above sternum.
me = human.data
wm = human.matrix_world
red_count = 0
for poly in me.polygons:
    c = wm @ poly.center
    n = (wm.to_3x3() @ poly.normal)
    if (1.28 <= c.z <= 1.53 and c.y < -0.04 and abs(c.x) < 0.20 and n.y < -0.1):
        poly.material_index = 1
        red_count += 1
print("REDFACES", red_count)

# ---------------- pose helper: orient a pose bone in armature space ----------------
def point_bone(pbname, direction, up=Vector((0, 0, 1))):
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

# ---- press pose targets (armature space; body upright frame) ----
# BOTTOM: upper arm out to side + slightly forward, roughly level; elbow bent ~90 -> forearm up.
# TOP:    arm straight overhead (up, slight forward, slight inward).
def apply_pose(t):
    # t in [0,1]: 0 = bottom, 1 = top (lockout)
    def lerp(a, b): return Vector(a).lerp(Vector(b), t)
    # LEFT arm (+X side)
    ua_L = lerp((0.75, -0.28, 0.05), (0.16, -0.12, 0.98))   # upperarm dir
    fa_L = lerp((0.18, -0.30, 0.94), (0.14, -0.10, 0.99))   # forearm dir
    # RIGHT arm (-X side) mirror X
    ua_R = Vector((-ua_L.x, ua_L.y, ua_L.z))
    fa_R = Vector((-fa_L.x, fa_L.y, fa_L.z))
    point_bone("upperarm01.L", ua_L)
    point_bone("lowerarm01.L", fa_L)
    point_bone("upperarm01.R", ua_R)
    point_bone("lowerarm01.R", fa_R)

# ---------------- calibration: render bottom & top, no recline ----------------
def setup_render(res=400, engine='BLENDER_WORKBENCH'):
    sc.render.engine = engine
    sc.render.resolution_x = res
    sc.render.resolution_y = res
    if engine == 'BLENDER_WORKBENCH':
        sc.display.shading.light = 'STUDIO'
        sc.display.shading.show_shadows = True
        sc.display.shading.color_type = 'MATERIAL'
    w = bpy.data.worlds.get("W") or bpy.data.worlds.new("W")
    sc.world = w; w.use_nodes = False; w.color = (0.92, 0.92, 0.93)

def add_camera(loc, look, lens=55):
    cam = bpy.data.cameras.new("Cam"); ob = bpy.data.objects.new("Cam", cam)
    bpy.context.collection.objects.link(ob)
    ob.location = loc
    d = (Vector(look) - Vector(loc)).normalized()
    ob.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler()
    cam.lens = lens
    sc.camera = ob
    return ob

def add_light():
    lt = bpy.data.lights.new("Sun", 'SUN'); lo = bpy.data.objects.new("Sun", lt)
    bpy.context.collection.objects.link(lo)
    lo.rotation_euler = (math.radians(55), 0, math.radians(35)); lt.energy = 3.5

if STAGE == "calib":
    bpy.ops.object.mode_set(mode='POSE')
    setup_render()
    add_light()
    add_camera((0.0, -3.2, 1.2), (0.0, 0.0, 1.1))   # front (-Y look)
    frontcam = sc.camera
    sidecam = add_camera((3.2, -0.1, 1.2), (0.0, -0.1, 1.1))  # side (+X look)
    for label, tval in (("bottom", 0.0), ("top", 1.0)):
        bpy.ops.object.mode_set(mode='POSE')
        apply_pose(tval)
        for cam, tag in ((frontcam, "front"), (sidecam, "side")):
            sc.camera = cam
            sc.render.filepath = os.path.join(WORK, f"calib_{label}_{tag}.png")
            bpy.ops.render.render(write_still=True)
    print("CALIB DONE")
    sys.exit(0)

# ---------------- render stage: reclined incline press ----------------
def add_box(name, dims, loc, rot=(0, 0, 0), rgb=(0.2, 0.2, 0.22)):
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=loc)
    ob = bpy.context.active_object
    ob.name = name
    ob.scale = (dims[0] / 2, dims[1] / 2, dims[2] / 2)
    ob.rotation_euler = rot
    m = make_mat("mat_" + name, rgb)
    ob.data.materials.append(m)
    return ob

def add_dumbbell(name, rgb=(0.06, 0.06, 0.07)):
    # handle (thin cylinder along local X) + two weight cylinders
    bpy.ops.mesh.primitive_cylinder_add(radius=0.02, depth=0.26,
                                         rotation=(0, math.radians(90), 0),
                                         location=(0, 0, 0))
    handle = bpy.context.active_object; handle.name = name
    mm = make_mat("mat_" + name, rgb)
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

if STAGE == "render":
    # recline the whole character about the hip pivot, then drop it onto the bench
    HIP = Vector((0.0, -0.11, 0.90))
    DROP = 0.30
    empty = bpy.data.objects.new("Pivot", None)
    bpy.context.collection.objects.link(empty)
    empty.location = HIP
    rig.parent = empty
    rig.matrix_parent_inverse = empty.matrix_world.inverted()   # human follows rig (already child)
    empty.rotation_euler = (math.radians(-RECLINE), 0, 0)
    empty.location = HIP + Vector((0, 0, -DROP))
    bpy.context.view_layer.update()

    # --- bench placed along the reclined torso, from the body's own geometry ---
    def bone_head_world(name):
        pb = rig.pose.bones[name]
        return rig.matrix_world @ pb.head
    p_low = bone_head_world("spine01")      # near hips
    p_high = bone_head_world("spine04")     # upper back
    axis = (p_high - p_low).normalized()    # torso long axis (world)
    back_dir = (empty.matrix_world.to_3x3() @ Vector((0, 1, 0))).normalized()  # body back
    side = Vector((1, 0, 0))                # left-right
    normal = back_dir                       # pad thickness dir (points into back)
    length_axis = axis
    side_axis = length_axis.cross(normal).normalized()
    # orthonormal basis for the board
    basis = Matrix((side_axis, length_axis, normal)).transposed()
    center = (p_low + p_high) / 2 + back_dir * 0.09 - Vector((0, 0, 0.02))
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=center)
    bench = bpy.context.active_object; bench.name = "Bench"
    bench.matrix_world = Matrix.Translation(center) @ basis.to_4x4() @ Matrix.Diagonal(
        (0.50, 1.05, 0.09)).to_4x4()
    bmat = make_mat("mat_bench", (0.13, 0.13, 0.15)); bench.data.materials.append(bmat)
    # upright support post from bench underside down to floor
    floor_z = -0.61
    post_h = center.z - floor_z
    post = add_box("Post", (0.16, 0.30, post_h),
                   (center.x, center.y, (center.z + floor_z) / 2),
                   rgb=(0.10, 0.10, 0.12))
    # ground plane
    add_box("Floor", (8, 8, 0.02), (0, 0, -0.62), rgb=(0.86, 0.86, 0.88))

    # dumbbells bone-parented to wrists (follow the hands each frame)
    db_L = add_dumbbell("DumbbellL")
    db_L.parent = rig; db_L.parent_type = 'BONE'; db_L.parent_bone = "wrist.L"
    db_R = add_dumbbell("DumbbellR")
    db_R.parent = rig; db_R.parent_type = 'BONE'; db_R.parent_bone = "wrist.R"

    setup_render(res=512)
    add_light()

    # auto-frame a side camera along +X across the whole press range (bottom+top)
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
    cam = add_camera((ctr.x + dist, ctr.y, ctr.z), (ctr.x, ctr.y, ctr.z), lens=45)

    os.makedirs(FRAMEDIR, exist_ok=True)
    for f in os.listdir(FRAMEDIR):
        if f.startswith("frame_"):
            os.remove(os.path.join(FRAMEDIR, f))

    # ping-pong: bottom -> top -> bottom over FRAMES frames (seamless loop)
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
