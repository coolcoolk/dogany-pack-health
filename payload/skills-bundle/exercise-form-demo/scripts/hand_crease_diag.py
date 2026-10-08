"""hand_crease_diag.py -- ROUND 7: classify the radiating "streak fan" the owner
circled at the palm-side base crease of the curled fingers on the FAR side from the
thumb (image-space x:20-260 y:460-760 of the 1200 product grip-check).

Three independent discriminators, all in the SAME product grip camera
(eye (0.98,-0.40,0.66) target (0.845,0.0,0.512) lens 78, 1200x1200), plus a 3x
zoom crop of the flagged box for each:

  <tag>_tex.png    real embedded material (product look) -- the streaks as flagged.
  <tag>_flat.png   material swapped for a plain matte grey Principled BSDF, NO
                   texture, SAME lighting/camera/pose. If the streaks are a TEXTURE
                   (albedo/bump UV-stretch), they VANISH here. If they REMAIN, the
                   streaks are GEOMETRY (real folded creasing / shading of the
                   deformed surface), not texture.
  <tag>_uvfc.png   false-color by per-vertex UV texel-density anomaly (red = the
                   UV is stretched/collapsed vs the mesh median at that vert). A
                   UV seam/pole shows up as a red band exactly where the streaks are.

Also prints, for the deformed verts that fall inside the flagged screen box:
  - UV seam spread (max pairwise UV distance among a vert's loops; a seam vert has
    >1 divergent UV),
  - per-vert texel-density ratio vs mesh median (stretch factor),
  - rest vs deformed Laplacian (geom outlier vs skinning fold),
  - dominant vertex group (which finger).

Usage:
  blender --background --python hand_crease_diag.py -- <glb> <outdir> <tag>
"""
import bpy, sys, math, os
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hand_sep_v4 as H

RES = 1200
# flagged image box (of RES) -> camera NDC. NDC origin = bottom-left, y up.
BOX_PX = (20, 260, 460, 760)   # x0, x1, y0(top), y1(top)


def load(glb):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    mesh = max([o for o in bpy.data.objects if o.type == 'MESH'],
               key=lambda o: len(o.data.vertices))
    for o in list(bpy.data.objects):
        if o.type == 'MESH' and o is not mesh:
            bpy.data.objects.remove(o, do_unlink=True)
    arm = [o for o in bpy.data.objects if o.type == 'ARMATURE'][0]
    return mesh, arm


def in_box(ndc):
    x0, x1, y0, y1 = BOX_PX
    px = ndc.x * RES
    py = (1.0 - ndc.y) * RES   # NDC y-up -> image y-down
    return (x0 <= px <= x1) and (y0 <= py <= y1) and ndc.z > 0


def build_adj(me):
    adj = {}
    for e in me.edges:
        a, b = e.vertices
        adj.setdefault(a, set()).add(b)
        adj.setdefault(b, set()).add(a)
    return adj


def lap(co, adj, idxs):
    out = {}
    for vi in idxs:
        nb = adj.get(vi, ())
        if not nb:
            out[vi] = 0.0
            continue
        m = Vector()
        for n in nb:
            m += co[n]
        m /= len(nb)
        out[vi] = (co[vi] - m).length
    return out


def per_vert_uv(me):
    """Return {vert: [uv Vectors across its loops]} for the active UV layer."""
    uvl = me.uv_layers.active
    if uvl is None:
        return {}
    out = {}
    for poly in me.polygons:
        for li in poly.loop_indices:
            vi = me.loops[li].vertex_index
            out.setdefault(vi, []).append(uvl.data[li].uv.copy())
    return out


def per_vert_texdensity(me, rest_co):
    """Per-vertex texel density = mean over incident faces of (uv_area/geo_area).
    A stretched/collapsed UV (pole/seam smear) gives a density far from the median.
    Returns {vert: density} and the global median."""
    uvl = me.uv_layers.active
    acc, cnt = {}, {}
    dens_all = []
    for poly in me.polygons:
        lis = list(poly.loop_indices)
        vids = [me.loops[li].vertex_index for li in lis]
        # triangulate fan for area
        p3 = [rest_co[v] for v in vids]
        uv = [uvl.data[li].uv for li in lis]
        a3 = a_uv = 0.0
        for k in range(1, len(vids) - 1):
            a3 += (p3[k] - p3[0]).cross(p3[k + 1] - p3[0]).length * 0.5
            e1 = uv[k] - uv[0]; e2 = uv[k + 1] - uv[0]
            a_uv += abs(e1.x * e2.y - e1.y * e2.x) * 0.5
        if a3 <= 1e-12:
            continue
        d = a_uv / a3
        dens_all.append(d)
        for v in vids:
            acc[v] = acc.get(v, 0.0) + d
            cnt[v] = cnt.get(v, 0) + 1
    dens = {v: acc[v] / cnt[v] for v in acc}
    dens_all.sort()
    med = dens_all[len(dens_all) // 2] if dens_all else 0.0
    return dens, med


def colorize_emit(mesh, colors):
    me = mesh.data
    for ca in list(me.color_attributes):
        me.color_attributes.remove(ca)
    ca = me.color_attributes.new(name="diag", type='FLOAT_COLOR', domain='POINT')
    for i, c in enumerate(colors):
        ca.data[i].color = (c[0], c[1], c[2], 1.0)
    mat = bpy.data.materials.new("diagmat"); mat.use_nodes = True
    nt = mat.node_tree
    for n in list(nt.nodes):
        nt.nodes.remove(n)
    out = nt.nodes.new("ShaderNodeOutputMaterial")
    emi = nt.nodes.new("ShaderNodeEmission")
    vc = nt.nodes.new("ShaderNodeVertexColor"); vc.layer_name = "diag"
    nt.links.new(vc.outputs["Color"], emi.inputs["Color"])
    nt.links.new(emi.outputs["Emission"], out.inputs["Surface"])
    me.materials.clear(); me.materials.append(mat)


def flat_material(mesh):
    m = bpy.data.materials.new("flat"); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (0.72, 0.66, 0.60, 1.0)
    b.inputs["Roughness"].default_value = 0.55
    try: b.inputs["Specular IOR Level"].default_value = 0.3
    except Exception: pass
    mesh.data.materials.clear(); mesh.data.materials.append(m)


def add_bar():
    bx, bz, r = H.GRIP_BAR
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=0.32, vertices=48,
                                        location=(bx, 0.0, bz))
    bar = bpy.context.active_object
    bar.rotation_euler = (math.radians(90), 0, 0)
    bpy.ops.object.transform_apply(rotation=True)
    m = bpy.data.materials.new("Bar"); m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (0.15, 0.35, 0.75, 1)
    bsdf.inputs["Metallic"].default_value = 0.9
    bsdf.inputs["Roughness"].default_value = 0.3
    bar.data.materials.append(m)
    return bar


def product_cam(sc):
    sc.render.resolution_x = sc.render.resolution_y = RES
    return H._cam((0.98, -0.40, 0.66), (0.845, 0.0, 0.512), lens=78)


def render(path):
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
    print("R", path)


def crop3x(src, dst):
    """3x-upscale crop of the flagged box using ffmpeg (matches diag_round7 crop)."""
    x0, x1, y0, y1 = BOX_PX
    w, h = x1 - x0, y1 - y0
    os.system("ffmpeg -y -loglevel error -i '%s' -vf "
              "\"crop=%d:%d:%d:%d,scale=%d:%d:flags=neighbor\" '%s'"
              % (src, w, h, x0, y0, w * 3, h * 3, dst))
    print("CROP", dst)


def main():
    glb, outdir, tag = sys.argv[sys.argv.index("--") + 1:][:3]
    os.makedirs(outdir, exist_ok=True)
    mesh, arm = load(glb)
    me = mesh.data
    mw = mesh.matrix_world
    gi2name = {vg.index: vg.name for vg in mesh.vertex_groups}
    adj = build_adj(me)
    rest_co = [mw @ v.co for v in me.vertices]
    vuv = per_vert_uv(me)
    dens, med = per_vert_texdensity(me, rest_co)

    # ---- render 1: real texture, product camera + crop ----
    orig_mats = [m for m in me.materials]
    bar = add_bar()
    H.pose_grip(arm, ".L")
    sc = bpy.context.scene
    H._studio(sc)
    camob = product_cam(sc)
    render(os.path.join(outdir, "%s_tex.png" % tag))
    crop3x(os.path.join(outdir, "%s_tex.png" % tag),
           os.path.join(outdir, "%s_tex_crop.png" % tag))

    # which deformed verts fall in the flagged screen box (grip pose active) ----
    dg = bpy.context.evaluated_depsgraph_get()
    ev = mesh.evaluated_get(dg)
    dm = ev.to_mesh()
    def_co = [mw @ v.co for v in dm.vertices]
    ev.to_mesh_clear()
    box_verts = []
    for vi in range(len(def_co)):
        ndc = world_to_camera_view(sc, camob, def_co[vi])
        if in_box(ndc):
            box_verts.append(vi)
    print("BOX_VERTS", len(box_verts))

    # ---- render 2: flat matte (texture removed), same pose/lights/cam + crop ----
    flat_material(mesh)
    render(os.path.join(outdir, "%s_flat.png" % tag))
    crop3x(os.path.join(outdir, "%s_flat.png" % tag),
           os.path.join(outdir, "%s_flat_crop.png" % tag))

    # ---- render 3: UV texel-density anomaly false color + crop ----
    # red = |log2(density/median)| large (stretched or collapsed UV); grey = normal.
    cols = []
    box_set = set(box_verts)
    for vi in range(len(me.vertices)):
        d = dens.get(vi)
        if d is None or med <= 0:
            cols.append((0.06, 0.06, 0.07)); continue
        r = abs(math.log2(max(d, 1e-9) / med))
        t = min(1.0, r / 3.0)   # 3 stops = full red
        cols.append((0.06 + 0.94 * t, 0.06 * (1 - t) + 0.06, 0.07 * (1 - t)))
    colorize_emit(mesh, cols)
    # emit shader ignores lights; keep world dark so only the mesh reads
    sc.world.node_tree.nodes.get('Background').inputs[1].default_value = 0.0
    render(os.path.join(outdir, "%s_uvfc.png" % tag))
    crop3x(os.path.join(outdir, "%s_uvfc.png" % tag),
           os.path.join(outdir, "%s_uvfc_crop.png" % tag))

    # restore materials so nothing downstream is polluted
    me.materials.clear()
    for m in orig_mats:
        me.materials.append(m)
    bpy.data.objects.remove(bar, do_unlink=True)

    # ---- numeric report over the box verts ----
    rest_lap = lap(rest_co, adj, box_verts)
    def_lap = lap(def_co, adj, box_verts)
    print("\n=== flagged-box deformed verts: UV / density / laplacian ===")
    print("mesh median texel-density = %.4g" % med)
    print("  vert      rest_pos                  uv_spread  dens/med  def_lap   rest_lap  finger")
    rows = sorted(box_verts, key=lambda vi: -abs(math.log2(max(dens.get(vi, med), 1e-9) / med))
                  if med > 0 else 0)[:40]
    seam_ct = stretch_ct = 0
    for vi in rows:
        uvs = vuv.get(vi, [])
        spread = 0.0
        for i in range(len(uvs)):
            for j in range(i + 1, len(uvs)):
                spread = max(spread, (uvs[i] - uvs[j]).length)
        d = dens.get(vi, med)
        ratio = d / med if med > 0 else 1.0
        if spread > 0.02:
            seam_ct += 1
        if ratio < 0.4 or ratio > 2.5:
            stretch_ct += 1
        v = me.vertices[vi]
        ws = sorted(((gi2name.get(g.group, str(g.group)), g.weight)
                     for g in v.groups), key=lambda kv: -kv[1])[:1]
        fng = ws[0][0] if ws else "?"
        c = rest_co[vi]
        print("  v%-7d (%.4f,%+.4f,%.4f)  %.4f     %6.2f   %.2e  %.2e  %s"
              % (vi, c.x, c.y, c.z, spread, ratio, def_lap[vi], rest_lap[vi], fng))
    print("\nSEAM_VERTS(spread>0.02): %d / %d   STRETCH_VERTS(dens<0.4 or >2.5x): %d / %d"
          % (seam_ct, len(rows), stretch_ct, len(rows)))
    print("CREASE_DIAG_DONE", tag)


if __name__ == "__main__":
    main()
