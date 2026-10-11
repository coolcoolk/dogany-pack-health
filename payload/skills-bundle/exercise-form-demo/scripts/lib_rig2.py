import bpy, math, bmesh
from mathutils import Vector, Matrix

# Coordinate frame (same as v1): X = left(+)/right(-), Y = front(-)/back(+), Z = up.
# Mesh is normalized to z in [-1, 1] (height 2.0 units).

# ---- Base 22 deform bones, KNEE CORRECTED (thigh tail / shin head raised to z=-0.455) ----
def bone_table():
    B = []
    def add(n, h, t, p=None, c=False):
        B.append((n, Vector(h), Vector(t), p, c))
    add("hips",     (0, 0.02, -0.05), (0, 0.02, 0.05))
    add("spine",    (0, 0.02, 0.05),  (0, 0.02, 0.22),  "hips", True)
    add("spine.001",(0, 0.02, 0.22),  (0, 0.03, 0.42),  "spine", True)
    add("spine.002",(0, 0.03, 0.42),  (0, 0.03, 0.60),  "spine.001", True)
    add("neck",     (0, 0.04, 0.60),  (0, 0.03, 0.75),  "spine.002", True)
    add("head",     (0, 0.03, 0.75),  (0, 0.02, 0.97),  "neck", True)
    def arm(s, sc):
        add("shoulder"+s,  (sc*0.04,0.02,0.56), (sc*0.16,0.03,0.57), "spine.002", False)
        add("upper_arm"+s, (sc*0.16,0.03,0.57), (sc*0.51,0.03,0.55), "shoulder"+s, True)
        add("forearm"+s,   (sc*0.51,0.03,0.55), (sc*0.78,0.02,0.53), "upper_arm"+s, True)
        add("hand"+s,      (sc*0.78,0.02,0.53), (sc*0.90,0.02,0.53), "forearm"+s, True)
    def leg(s, sc):
        # KNEE raised from -0.52 to -0.455 (equal thigh/shin split, at the real crease)
        add("thigh"+s, (sc*0.11,0.02,-0.05), (sc*0.165,0.02,-0.455), "hips", False)
        add("shin"+s,  (sc*0.165,0.02,-0.455),(sc*0.185,0.03,-0.86), "thigh"+s, True)
        add("foot"+s,  (sc*0.185,0.03,-0.86),(sc*0.185,-0.13,-0.96),"shin"+s, True)
        add("toe"+s,   (sc*0.185,-0.13,-0.96),(sc*0.185,-0.20,-0.965),"foot"+s, True)
    arm(".L",1); arm(".R",-1); leg(".L",1); leg(".R",-1)
    return B


def build_armature(mesh):
    B = bone_table()
    ad = bpy.data.armatures.new("Rig")
    rig = bpy.data.objects.new("Rig", ad)
    bpy.context.collection.objects.link(rig)
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.mode_set(mode='EDIT')
    eb = ad.edit_bones
    for n,h,t,p,c in B:
        b = eb.new(n); b.head=h; b.tail=t; b.use_deform=True
    for n,h,t,p,c in B:
        if p: eb[n].parent=eb[p]; eb[n].use_connect=c
    bpy.ops.object.mode_set(mode='OBJECT')
    return rig


# ---- NEW: extra DOF bones (forearm twist + thumb x2 + combined-fingers x2), per side ----
def add_dof_bones(rig):
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.mode_set(mode='EDIT')
    eb = rig.data.edit_bones
    def add(n, h, t, p, c=False):
        b = eb.new(n); b.head=Vector(h); b.tail=Vector(t); b.use_deform=True
        b.parent = eb[p]; b.use_connect = c
        return b
    for s, sc in ((".L",1), (".R",-1)):
        # forearm twist: collinear with forearm (elbow->wrist), rolls about arm long axis (world X)
        add("forearm_twist"+s, (sc*0.51,0.03,0.55), (sc*0.78,0.02,0.53), "forearm"+s, False)
        # reparent hand under the twist bone so wrist twist carries the hand
        eb["hand"+s].parent = eb["forearm_twist"+s]; eb["hand"+s].use_connect = True
        # thumb (2 bones) along the -Y protrusion
        add("thumb_01"+s, (sc*0.76,-0.02,0.53), (sc*0.80,-0.05,0.53), "hand"+s, False)
        add("thumb_02"+s, (sc*0.80,-0.05,0.53), (sc*0.83,-0.07,0.53), "thumb_01"+s, True)
        # combined fingers (2 bones, proximal + distal) covering the 4-finger paddle
        add("fingers_01"+s, (sc*0.845,0.03,0.535), (sc*0.885,0.03,0.535), "hand"+s, False)
        add("fingers_02"+s, (sc*0.885,0.03,0.535), (sc*0.925,0.03,0.535), "fingers_01"+s, True)
    bpy.ops.object.mode_set(mode='OBJECT')


def count_islands(mesh):
    bm = bmesh.new(); bm.from_mesh(mesh.data)
    seen=set(); n=0
    for v in bm.verts:
        if v.index in seen: continue
        n+=1; stack=[v]
        while stack:
            cur=stack.pop()
            if cur.index in seen: continue
            seen.add(cur.index)
            for e in cur.link_edges:
                o=e.other_vert(cur)
                if o.index not in seen: stack.append(o)
    bm.free()
    return n


def merge_by_distance(mesh, dist):
    bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.remove_doubles(threshold=dist)
    bpy.ops.mesh.normals_make_consistent(inside=False)
    bpy.ops.object.mode_set(mode='OBJECT')


def clamp(v, a=0.0, b=1.0):
    return max(a, min(b, v))


# ---- Manual weight post-process for the new DOF bones ----
def _vg(mesh, name):
    return mesh.vertex_groups.get(name) or mesh.vertex_groups.new(name=name)


def redistribute_forearm_twist(mesh):
    """Split forearm-group weight into a graded blend forearm(hinge) -> forearm_twist(roll):
    near-zero twist at elbow, full twist at wrist."""
    for s, sc in ((".L",1), (".R",-1)):
        fa = mesh.vertex_groups.get("forearm"+s)
        if fa is None: continue
        tw = _vg(mesh, "forearm_twist"+s)
        fa_i = fa.index
        elbow_x, wrist_x = sc*0.51, sc*0.78
        for v in mesh.data.vertices:
            w = None
            for g in v.groups:
                if g.group == fa_i: w = g.weight; break
            if w is None or w <= 0.0: continue
            x = v.co.x
            t = clamp((x - elbow_x) / (wrist_x - elbow_x))  # 0 at elbow, 1 at wrist
            t = t * t  # ease so the twist ramps up toward the wrist
            fa.add([v.index], w * (1.0 - t), 'REPLACE')
            tw.add([v.index], w * t, 'ADD')


def assign_hand_bones(mesh):
    """Carve the hand block into thumb (2) + combined fingers (2), keeping palm on 'hand'.
    Manual proximity assignment (no bone-heat) so there is zero cross-bleed."""
    stats = {}
    for s, sc in ((".L",1), (".R",-1)):
        hand = _vg(mesh, "hand"+s)
        t01 = _vg(mesh, "thumb_01"+s);  t02 = _vg(mesh, "thumb_02"+s)
        f01 = _vg(mesh, "fingers_01"+s); f02 = _vg(mesh, "fingers_02"+s)
        nt = nf = 0
        for v in mesh.data.vertices:
            co = v.co
            x = co.x; xs = x * sc          # local along-arm coord (positive outward)
            if xs < 0.72: continue          # not in hand region
            if not (0.48 < co.z < 0.58): continue
            y = co.y
            # THUMB: -Y protrusion, x in [0.75,0.845]
            if y < -0.028 and 0.74 < xs < 0.845:
                hw = clamp((0.775 - xs) / 0.03) * 0.5
                tt = 1.0 - hw
                a = clamp((0.815 - xs) / 0.03)     # proximal fraction
                _clear_hand_groups(v, mesh)
                if hw > 0: hand.add([v.index], hw, 'REPLACE')
                t01.add([v.index], tt * a, 'REPLACE')
                t02.add([v.index], tt * (1.0 - a), 'REPLACE')
                nt += 1
                continue
            # FINGERS: paddle beyond the knuckle
            if xs > 0.845 and y > -0.03:
                hw = clamp((0.87 - xs) / 0.025) * 0.6
                ft = 1.0 - hw
                a = clamp((0.895 - xs) / 0.02)     # proximal fraction
                _clear_hand_groups(v, mesh)
                if hw > 0: hand.add([v.index], hw, 'REPLACE')
                f01.add([v.index], ft * a, 'REPLACE')
                f02.add([v.index], ft * (1.0 - a), 'REPLACE')
                nf += 1
                continue
        stats[s] = (nt, nf)
    return stats


def _clear_hand_groups(v, mesh):
    """Remove a vert from every group so the manual assignment fully owns it."""
    idxs = [g.group for g in v.groups]
    for gi in idxs:
        mesh.vertex_groups[gi].remove([v.index])


def normalize_and_cap(mesh):
    bpy.context.view_layer.objects.active = mesh
    bpy.ops.object.mode_set(mode='WEIGHT_PAINT')
    bpy.ops.object.vertex_group_limit_total(limit=4)
    bpy.ops.object.vertex_group_normalize_all(lock_active=False)
    bpy.ops.object.mode_set(mode='OBJECT')


def wrot(rig, pbname, axis, deg):
    pb = rig.pose.bones[pbname]
    M = pb.matrix.copy(); head=M.translation.copy()
    R = Matrix.Rotation(math.radians(deg),4,axis); T=Matrix.Translation(head)
    pb.matrix = T @ R @ T.inverted() @ M
    bpy.context.view_layer.update()


def reset_pose(rig):
    bpy.context.view_layer.objects.active = rig
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='SELECT')
    bpy.ops.pose.transforms_clear()
    bpy.ops.object.mode_set(mode='OBJECT')
