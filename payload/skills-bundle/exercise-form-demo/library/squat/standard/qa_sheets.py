#!/usr/bin/env python3
"""Build QA contact sheets: every 4th rendered frame tiled into 4x4 grids.
Reads scratch/n7_frames/, writes squat_standard_sheet_N.png here.
Each tile is a downscaled full frame so EVERY in-between frame can be eyeballed
for planted feet / valgus / depth / arm symmetry / clipping / drift.
"""
import os, glob
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
SEQ = os.path.join(SKILL_ROOT, "scratch", "n7_frames")

frames = sorted(glob.glob(os.path.join(SEQ, "f[0-9][0-9][0-9][0-9].png")))
pick = frames[::4]                       # every 4th frame
if not pick:
    raise SystemExit("no frames in %s" % SEQ)

COLS, ROWS = 4, 4                        # <=16 tiles per sheet
TW = 300                                 # tile width px (readable)
per = COLS * ROWS
sheets = [pick[i:i + per] for i in range(0, len(pick), per)]
for si, grp in enumerate(sheets, 1):
    im0 = Image.open(grp[0]); ar = im0.height / im0.width
    th = int(TW * ar)
    sheet = Image.new("RGB", (COLS * TW, ROWS * th), (20, 20, 22))
    dr = ImageDraw.Draw(sheet)
    for k, fp in enumerate(grp):
        r, c = divmod(k, COLS)
        t = Image.open(fp).resize((TW, th), Image.LANCZOS)
        sheet.paste(t, (c * TW, r * th))
        n = os.path.basename(fp)[1:5]
        dr.text((c * TW + 5, r * th + 4), "f" + n, fill=(255, 235, 120))
    out = os.path.join(HERE, "squat_standard_sheet_%d.png" % si)
    sheet.save(out)
    print("SHEET", out, "tiles=%d" % len(grp))
print("sheets=%d frames_tiled=%d" % (len(sheets), len(pick)))
