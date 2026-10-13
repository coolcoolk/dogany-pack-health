# Reusable PARAMETRIC BARBELL prop for the exercise-form-demo library.
# Built procedurally in Blender (no download). Olympic-bar proportions:
#   straight shaft ~2.2 m, ~29 mm shaft, thicker sleeves + collars at each end,
#   and PARAMETRIC plates mounted on the sleeves.
# Shared prop: other barbell lifts (bench, deadlift, OHP, row...) import make_barbell().
#
# usage from another Blender script:
#   import sys; sys.path.append("<skill>/scripts")
#   from prop_barbell import make_barbell
#   bar = make_barbell(plates_per_side=2)          # -> returns an Empty (the parent)
#   bar.location = (0, 0.09, 0.56)                 # place / parent it as one unit
#
# The whole assembly is parented to a single Empty at the bar's CENTER, shaft
# running along world X. Move / rotate / bone-parent that Empty to move the bar.
import bpy, math
from mathutils import Vector


def _mat(name, rgb, metallic, rough):
    m = bpy.data.materials.get(name)
    if m is None:
        m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (rgb[0], rgb[1], rgb[2], 1.0)
    b.inputs["Metallic"].default_value = metallic
    b.inputs["Roughness"].default_value = rough
    return m


def _cyl(radius, depth, x_center, verts=48):
    # cylinder whose axis runs along world X, centered at (x_center,0,0).
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=depth,
                                        vertices=verts, location=(x_center, 0, 0))
    o = bpy.context.active_object
    o.rotation_euler = (0, math.radians(90), 0)   # Z-axis cylinder -> X-axis
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
    return o


def make_barbell(plates_per_side=2,
                 plate_diameter=0.45,      # 20 kg olympic plate ~450 mm
                 plate_thickness=0.030,    # per-plate width on the sleeve
                 shaft_length=2.20,        # straight-bar length
                 shaft_radius=0.0145,      # ~29 mm shaft diameter
                 sleeve_radius=0.025,      # ~50 mm loadable sleeve
                 sleeve_length=0.36,       # loadable length each end
                 name="Barbell"):
    """Build a parametric olympic barbell. Returns the parent Empty (bar center at
    origin, shaft along +/-X). plates_per_side / plate_diameter / plate_thickness
    are the load parameters other lifts vary. Metal-grey shaft, darker plates."""  # estate-scrub:allow(metal material, 3D render)
    metal = _mat("BarMetal", (0.55, 0.56, 0.585), 1.0, 0.34)  # estate-scrub:allow(metal material, 3D render)
    plate_m = _mat("BarPlate", (0.045, 0.047, 0.055), 0.25, 0.62)
    collar_m = _mat("BarCollar", (0.30, 0.31, 0.33), 1.0, 0.42)

    half = shaft_length / 2.0
    metal_parts = []
    plate_parts = []

    # straight shaft (full length, thin)
    metal_parts.append(_cyl(shaft_radius, shaft_length, 0.0))

    # thicker loadable sleeve at each end
    sleeve_inner = half - sleeve_length
    sleeve_cx = half - sleeve_length / 2.0
    for s in (+1, -1):
        sl = _cyl(sleeve_radius, sleeve_length, s * sleeve_cx)
        sl.data.materials.append(bpy.data.materials["BarMetal"])
        metal_parts.append(sl)
        # inner collar (shoulder) that the plates butt against
        col = _cyl(sleeve_radius * 1.55, 0.028, s * (sleeve_inner + 0.014))
        col.data.materials.clear()
        col.data.materials.append(collar_m)
        plate_parts_collar = col
        # keep collars in the metal group visually but give collar mat estate-scrub:allow(metal material, 3D render)
        col_group = col
        metal_parts.append(col_group)
        # remove default mat so only collar_m shows
        # (append above already set it)

        # PARAMETRIC plates stacked outward from the collar
        x0 = s * (sleeve_inner + 0.028)
        for i in range(plates_per_side):
            cx = x0 + s * (plate_thickness / 2.0 + i * (plate_thickness + 0.004))
            p = _cyl(plate_diameter / 2.0, plate_thickness, cx, verts=64)
            p.data.materials.clear()
            p.data.materials.append(plate_m)
            plate_parts.append(p)

    # first shaft has no mat yet -> metal estate-scrub:allow(metal material, 3D render)
    if not metal_parts[0].data.materials:
        metal_parts[0].data.materials.append(metal)  # estate-scrub:allow(metal material, 3D render)

    def _join(objs, out_name):
        bpy.ops.object.select_all(action='DESELECT')
        for o in objs:
            o.select_set(True)
        bpy.context.view_layer.objects.active = objs[0]
        bpy.ops.object.join()
        j = bpy.context.active_object
        j.name = out_name
        return j

    # separate collar objects keep their own material after join (per-face mats
    # survive join), so we can join everything metal-ish into one object. estate-scrub:allow(metal material, 3D render)
    metal_obj = _join(metal_parts, name + "_bar")
    plate_obj = _join(plate_parts, name + "_plates") if plate_parts else None

    # parent everything to a single Empty at the bar center
    empty = bpy.data.objects.new(name, None)
    empty.empty_display_type = 'PLAIN_AXES'
    empty.empty_display_size = 0.15
    bpy.context.collection.objects.link(empty)
    for o in (metal_obj, plate_obj):
        if o is None:
            continue
        o.parent = empty
        o.matrix_parent_inverse = empty.matrix_world.inverted()
    return empty


if __name__ == "__main__":
    # standalone smoke test: build a 2-plate bar in an empty scene
    bar = make_barbell(plates_per_side=2)
    print("BARBELL_BUILT", bar.name, "children",
          [c.name for c in bar.children])
