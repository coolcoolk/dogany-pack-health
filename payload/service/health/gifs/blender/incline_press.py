"""
Headless Blender prototype -- incline dumbbell press motion loop.
Run: blender --background --python incline_press.py -- <out_frames_dir>
Renders a side-view articulated figure doing an incline press, ping-pong loop.
Engine: Workbench (flat, fast, headless-safe, motion-graphic look).
Prototype scope: primitive kinematic figure (no skinned armature) to validate
the rig->animate->render pipeline. Character polish is a later step.
"""
import bpy
import sys
import math
from mathutils import Euler

# ---- args ----
argv = sys.argv
outdir = argv[argv.index("--") + 1] if "--" in argv else "/tmp/incline_frames"

# ---- clean scene ----
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)
for coll in (bpy.data.meshes, bpy.data.materials):
    for b in list(coll):
        coll.remove(b)

# ---- helpers ----
def mat(name, rgba):
    m = bpy.data.materials.new(name)
    m.use_nodes = False
    m.diffuse_color = rgba
    return m

SKIN = mat("skin", (0.85, 0.62, 0.45, 1))
SHIRT = mat("shirt", (0.20, 0.45, 0.85, 1))
DARK = mat("dark", (0.15, 0.16, 0.20, 1))
IRON = mat("iron", (0.10, 0.10, 0.12, 1))
BENCH = mat("bench", (0.30, 0.32, 0.38, 1))

def cyl(name, r, depth, mat_, parent=None, loc=(0,0,0), rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=depth, location=loc)
    o = bpy.context.active_object
    o.name = name
    o.rotation_euler = Euler(rot, 'XYZ')
    o.data.materials.append(mat_)
    if parent:
        o.parent = parent
    return o

def sphere(name, r, mat_, parent=None, loc=(0,0,0)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=loc)
    o = bpy.context.active_object
    o.name = name
    o.data.materials.append(mat_)
    if parent:
        o.parent = parent
    return o

def empty(name, loc=(0,0,0), parent=None):
    e = bpy.data.objects.new(name, None)
    e.location = loc
    bpy.context.collection.objects.link(e)
    if parent:
        e.parent = parent
    return e

# ---- incline bench (reclined ~30deg) + torso ----
INCLINE = math.radians(30)
# bench pad
cyl("bench_pad", 0.0, 0, BENCH)  # placeholder to keep names; replace below
bpy.data.objects.remove(bpy.data.objects["bench_pad"], do_unlink=True)
bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.55))
pad = bpy.context.active_object
pad.name = "bench_pad"
pad.scale = (0.55, 0.28, 0.06)
pad.rotation_euler = Euler((0, INCLINE, 0), 'XYZ')
pad.data.materials.append(BENCH)

# root at hip, torso reclined
root = empty("root", loc=(0, 0, 0.75))
torso = cyl("torso", 0.28, 1.1, SHIRT, parent=root, loc=(0, 0, 0.0),
            rot=(0, INCLINE, 0))
# offset torso so it lies along incline from hip upward
torso.location = (math.sin(INCLINE)*0.55, 0, math.cos(INCLINE)*0.55)
head = sphere("head", 0.20, SKIN, parent=root,
              loc=(math.sin(INCLINE)*1.15, 0, math.cos(INCLINE)*1.15))

# legs (static, context)
cyl("thigh_L", 0.13, 0.75, DARK, parent=root, loc=(-0.18, 0.16, -0.45),
    rot=(0, math.radians(75), 0))
cyl("thigh_R", 0.13, 0.75, DARK, parent=root, loc=(-0.18, -0.16, -0.45),
    rot=(0, math.radians(75), 0))
cyl("shin_L", 0.11, 0.75, DARK, parent=root, loc=(0.30, 0.16, -0.75))
cyl("shin_R", 0.11, 0.75, DARK, parent=root, loc=(0.30, -0.16, -0.75))

# ---- arms: shoulder pivot -> upper arm -> elbow pivot -> forearm+dumbbell ----
# shoulder near top of torso
shoulder_z = math.cos(INCLINE)*1.0
shoulder_x = math.sin(INCLINE)*1.0
UPPER_LEN = 0.42
FORE_LEN = 0.40

def build_arm(side, y):
    sh = empty(f"shoulder_{side}", loc=(shoulder_x, y, shoulder_z), parent=root)
    ua = cyl(f"upperarm_{side}", 0.075, UPPER_LEN, SKIN, parent=sh,
             loc=(0, 0, -UPPER_LEN/2))
    el = empty(f"elbow_{side}", loc=(0, 0, -UPPER_LEN), parent=sh)
    fa = cyl(f"forearm_{side}", 0.065, FORE_LEN, SKIN, parent=el,
             loc=(0, 0, -FORE_LEN/2))
    # dumbbell at hand
    hand = empty(f"hand_{side}", loc=(0, 0, -FORE_LEN), parent=el)
    cyl(f"db_bar_{side}", 0.03, 0.22, IRON, parent=hand, loc=(0, 0, 0),
        rot=(math.radians(90), 0, 0))
    sphere(f"db_p1_{side}", 0.09, IRON, parent=hand, loc=(0, 0.11, 0))
    sphere(f"db_p2_{side}", 0.09, IRON, parent=hand, loc=(0, -0.11, 0))
    return sh, el

sh_L, el_L = build_arm("L", 0.22)
sh_R, el_R = build_arm("R", -0.22)

# ---- keyframe poses (ping-pong loop) ----
# START (bottom): upper arm out to side/down, elbow bent ~90 (dumbbell at chest)
# END   (top):    upper arm up along incline, elbow straight (press lockout)
scene = bpy.context.scene
scene.frame_start = 1
scene.frame_end = 24
MID = 12

def key_arm(sh, el, frame, sh_rot, el_rot):
    sh.rotation_euler = Euler(sh_rot, 'XYZ')
    el.rotation_euler = Euler(el_rot, 'XYZ')
    sh.keyframe_insert("rotation_euler", frame=frame)
    el.keyframe_insert("rotation_euler", frame=frame)

# rotations about Y (side-view plane)
START_SH = (0, math.radians(105), 0)   # upper arm out/down
START_EL = (0, math.radians(-95), 0)   # forearm bent up toward chest
END_SH   = (0, math.radians(10), 0)    # upper arm up
END_EL   = (0, math.radians(0), 0)     # straight

for sh, el, y in ((sh_L, el_L, 1), (sh_R, el_R, -1)):
    key_arm(sh, el, 1,   START_SH, START_EL)
    key_arm(sh, el, MID, END_SH,   END_EL)
    key_arm(sh, el, 24,  START_SH, START_EL)

# ---- camera + light ----
bpy.ops.object.camera_add(location=(3.6, -3.2, 1.4))
cam = bpy.context.active_object
cam.rotation_euler = Euler((math.radians(80), 0, math.radians(48)), 'XYZ')
scene.camera = cam

bpy.ops.object.light_add(type='SUN', location=(4, -4, 6))
sun = bpy.context.active_object
sun.data.energy = 3.0

# world bg light grey
world = bpy.data.worlds.new("W") if not bpy.data.worlds else bpy.data.worlds[0]
scene.world = world
world.use_nodes = False
world.color = (0.93, 0.94, 0.96)

# ---- render settings (Workbench, flat, fast, headless-safe) ----
scene.render.engine = 'BLENDER_WORKBENCH'
scene.render.image_settings.file_format = 'PNG'
scene.render.resolution_x = 480
scene.render.resolution_y = 480
scene.render.film_transparent = False
scene.render.filepath = outdir.rstrip("/") + "/f_"
try:
    scene.display.shading.light = 'STUDIO'
    scene.display.shading.color_type = 'MATERIAL'
except Exception as e:
    print("shading cfg skip:", e)

bpy.ops.render.render(animation=True)
print("RENDER_DONE frames ->", outdir)
