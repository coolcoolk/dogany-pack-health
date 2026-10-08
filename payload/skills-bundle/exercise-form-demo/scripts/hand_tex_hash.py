"""hand_tex_hash.py -- print name, resolution and a pixel hash for every embedded
image in a GLB, so the base skin texture can be proven identical across rig
versions (v3 pre-surgery vs v4 post-surgery). Same texture hash => the finger-
separation surgery did NOT introduce the flagged palm/thenar skin detail.

Usage: blender --background --python hand_tex_hash.py -- <glb>
"""
import bpy, sys, hashlib


def main():
    glb = sys.argv[sys.argv.index("--") + 1]
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=glb)
    print("GLB", glb)
    for img in bpy.data.images:
        if img.name == "Render Result" or img.size[0] == 0:
            continue
        px = img.pixels[:]
        h = hashlib.md5(bytes(int(p * 255) & 0xFF for p in px[::17])).hexdigest()
        print("  IMG %-24s %dx%d  chans=%d  hash=%s"
              % (img.name, img.size[0], img.size[1], img.channels, h))
    print("TEXHASH_DONE")


if __name__ == "__main__":
    main()
