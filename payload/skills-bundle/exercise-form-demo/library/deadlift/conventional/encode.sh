#!/bin/bash
# Encode the deadlift PNG sequence -> mp4 + gif into this library folder.
# build_deadlift.py renders the sequence to scratch/dlrb_frames/ and the QA stills
# directly here with their final names; this only does the video encode.
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
SKILL_ROOT="$(cd "$HERE/../../.." && pwd)"
SEQ="$SKILL_ROOT/scratch/dlrb_frames"
FF="${FFMPEG:-$(command -v ffmpeg || echo /opt/homebrew/bin/ffmpeg)}"
[ -x "$FF" ] || { echo "ffmpeg not found (set FFMPEG=<path>)"; exit 3; }

# mp4: H.264 yuv420p +faststart, 30fps, portrait 720x1280
$FF -y -framerate 30 -start_number 1 -i "$SEQ/f%04d.png" \
  -c:v libx264 -pix_fmt yuv420p -crf 19 -movflags +faststart \
  -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" "$HERE/deadlift_conventional_rep.mp4"

# gif via palette (loops)
$FF -y -i "$HERE/deadlift_conventional_rep.mp4" \
  -vf "fps=25,scale=420:-1:flags=lanczos,palettegen=stats_mode=diff" "$SEQ/_pal.png"
$FF -y -i "$HERE/deadlift_conventional_rep.mp4" -i "$SEQ/_pal.png" \
  -lavfi "fps=25,scale=420:-1:flags=lanczos[x];[x][1:v]paletteuse=dither=bayer" \
  "$HERE/deadlift_conventional_rep.gif"

echo "=== OUTPUTS ==="
echo "mp4: $(du -h "$HERE/deadlift_conventional_rep.mp4" | cut -f1)  gif: $(du -h "$HERE/deadlift_conventional_rep.gif" | cut -f1)"
