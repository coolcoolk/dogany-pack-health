#!/usr/bin/env python3
"""Parse a BVH file: report joint hierarchy, frame count/rate, and
estimate hip/root vertical trajectory to sanity-check hinge motion."""
import sys
import re

def parse_bvh(path):
    with open(path) as f:
        text = f.read()

    hier_text, motion_text = text.split("MOTION", 1)

    # Parse joint order and channel counts in document order
    joints = []
    channel_counts = []
    for line in hier_text.splitlines():
        line = line.strip()
        m = re.match(r"(ROOT|JOINT)\s+(\S+)", line)
        if m:
            joints.append(m.group(2))
        m2 = re.match(r"CHANNELS\s+(\d+)\s+(.*)", line)
        if m2:
            channel_counts.append((int(m2.group(1)), m2.group(2).split()))

    # Parse motion section
    lines = motion_text.strip().splitlines()
    frames_line = [l for l in lines if l.startswith("Frames:")][0]
    frame_time_line = [l for l in lines if l.startswith("Frame Time:")][0]
    n_frames = int(frames_line.split(":")[1].strip())
    frame_time = float(frame_time_line.split(":")[1].strip())

    data_lines = [l for l in lines if l and not l.startswith("Frames") and not l.startswith("Frame Time")]
    frames = [list(map(float, l.split())) for l in data_lines]

    return {
        "joints": joints,
        "n_joints": len(joints),
        "channel_counts": channel_counts,
        "n_frames_header": n_frames,
        "n_frames_actual": len(frames),
        "frame_time": frame_time,
        "fps": round(1.0 / frame_time, 3) if frame_time else None,
        "duration_sec": round(n_frames * frame_time, 3),
        "frames": frames,
    }


def root_channel_indices(channel_counts):
    """Return the starting index of the root's channels within a frame vector."""
    return channel_counts[0][1]


def main(path):
    d = parse_bvh(path)
    print(f"file: {path}")
    print(f"  joints ({d['n_joints']}): {', '.join(d['joints'])}")
    print(f"  fps: {d['fps']}  frame_time: {d['frame_time']}")
    print(f"  frames(header): {d['n_frames_header']}  frames(actual): {d['n_frames_actual']}")
    print(f"  duration: {d['duration_sec']} s")

    root_chans = d["channel_counts"][0][1]
    print(f"  root channels: {root_chans}")

    # find Y position index within root channels (Xposition Yposition Zposition Xrotation ...)
    if "Yposition" in root_chans:
        y_idx = root_chans.index("Yposition")
        ys = [fr[y_idx] for fr in d["frames"] if len(fr) > y_idx]
        if ys:
            print(f"  root Y range: min={min(ys):.2f} max={max(ys):.2f} delta={max(ys)-min(ys):.2f}")
            # sample trajectory at 10 points across the clip
            n = len(ys)
            sample_idx = [int(i * (n - 1) / 9) for i in range(10)]
            traj = [round(ys[i], 1) for i in sample_idx]
            print(f"  root Y trajectory (10 samples): {traj}")
    else:
        print("  no Yposition channel found in root")
    print()


if __name__ == "__main__":
    for p in sys.argv[1:]:
        try:
            main(p)
        except Exception as e:
            print(f"file: {p}\n  ERROR parsing: {e}\n")
