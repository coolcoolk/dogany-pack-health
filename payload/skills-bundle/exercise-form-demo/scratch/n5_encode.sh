#!/bin/bash
# Encode n5f PNG sequence -> mp4 + gif, place into library/deadlift/conventional/.
set -e
# de-identified 2026-09-12 (pack carry-in): no absolute instance/home path in a
# shipped pack. This script lives at <skill>/scratch/, so the skill root is ..
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="${FORM_DEMO_SKILL_ROOT:-$(cd "$HERE/.." && pwd)}"
SCR="$ROOT/scratch"
SEQ="$SCR/n5f_frames"
OUT="$ROOT/library/deadlift/conventional"
mkdir -p "$OUT"
FF="${FFMPEG:-$(command -v ffmpeg || echo /opt/homebrew/bin/ffmpeg)}"
[ -x "$FF" ] || { echo "ffmpeg not found (set FFMPEG=<path>)"; exit 3; }

# mp4: H.264 yuv420p +faststart, 30fps, portrait 720x1280
$FF -y -framerate 30 -start_number 1 -i "$SEQ/f%04d.png" \
  -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart \
  -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" "$OUT/deadlift_conventional_rep.mp4"

# gif via palette
$FF -y -i "$OUT/deadlift_conventional_rep.mp4" \
  -vf "fps=25,scale=480:-1:flags=lanczos,palettegen" "$SCR/n5f_pal.png"
$FF -y -i "$OUT/deadlift_conventional_rep.mp4" -i "$SCR/n5f_pal.png" \
  -lavfi "fps=25,scale=480:-1:flags=lanczos[x];[x][1:v]paletteuse" \
  "$OUT/deadlift_conventional_rep.gif"

# stills
cp "$SCR/n5f_qa_setup.png"           "$OUT/deadlift_conventional_frame_setup.png"
cp "$SCR/n5f_qa_midpull.png"         "$OUT/deadlift_conventional_frame_midpull.png"
cp "$SCR/n5f_qa_lockout.png"         "$OUT/deadlift_conventional_frame_lockout.png"
cp "$SCR/n5f_diag_grip.png"          "$OUT/deadlift_conventional_diag_grip.png"
cp "$SCR/n5f_diag_barbreak_side.png" "$OUT/deadlift_conventional_diag_barbreak_side.png"
# source script
cp "$SCR/n5_build.py"                "$OUT/build_deadlift.py"

echo "=== OUTPUTS ==="
ls -la "$OUT"
echo "mp4 size: $(du -h "$OUT/deadlift_conventional_rep.mp4" | cut -f1)"
echo "gif size: $(du -h "$OUT/deadlift_conventional_rep.gif" | cut -f1)"
