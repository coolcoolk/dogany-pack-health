#!/usr/bin/env python3
"""fatigue_heatmap.py -- per-muscle fatigue -> front+back body photo (< 1 s).

The session-start briefing's picture (owner 2026-09-26 11:37 / 13:05). Style
is the owner-approved round 5 of the heatmap spike (compose5): fatigue is
OPACITY of one red over the pre-rendered body, never a colour ramp -- no
fatigue = bare skin, more fatigue = deeper red. Shading-preserving albedo
swap in linear light, so the muscle relief of the base render survives.

WHAT IS DATA HERE (the parallel region-subdivision loop drops its output in
without a code change):
  <assets>/meta.json        res, views, group{region: [muscle masks]}, skin_lin
  <assets>/masks.npz        "<view>/G:<region>" region fields + "<view>/<muscle>"
  <assets>/base_<view>.png  the pre-rendered body per view
  <assets>/region_map.json  region -> which kit muscle nodes paint it:
      {"<region>": {"nodes": [kit node, ...], "fallback": [kit node, ...]}}
      value(region) = the highest ratio among `nodes` present in the reading;
      when none is present, the highest among `fallback` (a set-less session
      declares "back" as a whole and never loads back_lats itself).
  A region in the masks with no region_map row is never painted; a kit node
  no region lists is simply not drawn (it still appears in the text lines).

NUMBERS. The picture carries NO number of its own. The side panel lists the
same display items the text lines carry (label + the kit's own pct), so the
photo and the message can never disagree. Ratios (residual / dose) come from
kit_life muscle-state; this file only maps them to opacity.

Deps: numpy + Pillow (the heatmap is optional -- the caller degrades to text
when either is missing; see available()). Everything else is stdlib.
"""
import sys as _sys; _sys.dont_write_bytecode = True   # never leave __pycache__ in the pack or kit tree (compat-lint C4b)
import json
import os
import time

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ASSETS = os.path.join(HERE, "assets", "fatigue-heatmap")
FONT_CANDIDATES = ("/System/Library/Fonts/AppleSDGothicNeo.ttc",
                   "/usr/share/fonts/truetype/nanum/NanumGothic.ttf",
                   "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")

AMAX = 0.92                 # opacity at the top of the scale
RED = (205, 20, 25)         # the one colour (round 5)
SKIN8 = (196, 150, 124)     # legend swatch base
SEAM = 0.40                 # region outline darkening (multiplicative)
MIN_RATIO = 0.05            # below this a region stays bare skin

# region_map used when the assets directory carries none (the compose5 set).
DEFAULT_REGION_MAP = {
    "chest": {"nodes": ["chest", "chest_upper", "chest_mid", "chest_lower"]},
    "shoulders": {"nodes": ["shoulders", "front_delt", "side_delt",
                            "rear_delt", "rotator_cuff"]},
    "biceps": {"nodes": ["biceps", "biceps_distal", "biceps_prox",
                         "brachialis"]},
    "triceps": {"nodes": ["triceps", "triceps_long", "triceps_lat_med"]},
    "forearms": {"nodes": ["forearms", "brachioradialis"]},
    "abs": {"nodes": ["abs", "abs_lower", "obliques"]},
    "back_upper": {"nodes": ["back_upper"], "fallback": ["back"]},
    "back_lats": {"nodes": ["back_lats"], "fallback": ["back"]},
    "back_erectors": {"nodes": ["back_erectors"], "fallback": ["back"]},
    "glutes": {"nodes": ["glutes", "glute_max", "glute_med"]},
    "quads": {"nodes": ["quads"]},
    "hamstrings": {"nodes": ["hamstrings"]},
    "calves": {"nodes": ["calves", "calf_gastroc", "calf_soleus",
                         "tibialis_anterior"]},
}


def available():
    """(ok, why) -- can this interpreter draw the photo?"""
    try:
        import numpy  # noqa: F401
        from PIL import Image  # noqa: F401
    except Exception as exc:  # noqa: BLE001 -- any import failure = no photo
        return False, "%s: %s" % (exc.__class__.__name__, exc)
    return True, None


def s_of(ratio):
    """Compressed scale 0..1: log2(1 + ratio) / 2 (ratio 3 -> 1)."""
    import math
    return min(max(math.log2(1 + max(ratio, 0.0)) / 2.0, 0.0), 1.0)


def swatch(ratio):
    a = s_of(ratio) * AMAX
    return tuple(int(round(k + (r - k) * a)) for k, r in zip(SKIN8, RED))


def load_region_map(assets):
    path = os.path.join(assets, "region_map.json")
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            return {k: v for k, v in json.load(fh).items()
                    if not k.startswith("_")}
    return dict(DEFAULT_REGION_MAP)


def region_values(node_ratio, region_map):
    """{region: ratio} from {kit node: ratio} through the region table."""
    out = {}
    for reg, spec in region_map.items():
        vals = [node_ratio[n] for n in spec.get("nodes", ())
                if n in node_ratio]
        if not vals:
            vals = [node_ratio[n] for n in spec.get("fallback", ())
                    if n in node_ratio]
        if vals and max(vals) >= MIN_RATIO:
            out[reg] = max(vals)
    return out


_CACHE = {}


def _load(assets):
    import numpy as np
    from PIL import Image
    key = os.path.realpath(assets)
    if key in _CACHE:
        return _CACHE[key]
    with open(os.path.join(assets, "meta.json"), encoding="utf-8") as fh:
        meta = json.load(fh)
    masks = np.load(os.path.join(assets, "masks.npz"))
    views = {}
    for v in meta["views"]:
        base = np.asarray(Image.open(
            os.path.join(assets, "base_%s.png" % v)).convert("RGB"))
        mm = {}
        for k in masks.files:
            if k.startswith(v + "/"):
                mm[k.split("/", 1)[1]] = masks[k]
        views[v] = (base, mm)
    _CACHE[key] = (meta, views)
    return meta, views


def _luts():
    import numpy as np
    lut = ((np.arange(256) / 255.0 + 0.055) / 1.055) ** 2.4
    lut[:11] = np.arange(11) / 255.0 / 12.92
    x = np.arange(256) / 255.0
    t = np.clip((x - 0.38) / 0.24, 0, 1)
    cover = (t * t * (3 - 2 * t)).astype(np.float32)
    line = np.clip(1 - np.abs(x - 0.5) / 0.075, 0, 1).astype(np.float32) ** 1.5
    return lut.astype(np.float32), cover, line


def _to_srgb8(x):
    import numpy as np
    x = np.clip(x, 0, 1)
    y = np.where(x <= 0.0031308, 12.92 * x,
                 1.055 * np.power(x, 1 / 2.4) - 0.055)
    return (y * 255 + 0.5).astype(np.uint8)


def _bbox(m):
    import numpy as np
    rows = np.flatnonzero(m.any(axis=1))
    if rows.size == 0:
        return None
    cols = np.flatnonzero(m[rows[0]:rows[-1] + 1].any(axis=0))
    return (slice(int(rows[0]), int(rows[-1]) + 1),
            slice(int(cols[0]), int(cols[-1]) + 1))


def tint(base8, mm, group, ratio):
    """One view: every fatigued region painted by opacity of one red.
    Work is done inside each region's bounding box (the frame is mostly
    background), which is what keeps the whole photo under a second."""
    import numpy as np
    lut, cover, line = _luts()
    skin = np.array(_META_SKIN[0], np.float32)
    red_lin = lut[np.array(RED)]
    k = red_lin / skin
    lin = lut[base8]
    h, w = lin.shape[:2]
    seam = np.zeros((h, w), np.float32)
    alpha = np.zeros((h, w), np.float32)
    for reg, mus in group.items():
        if reg not in ratio:
            continue
        gm = mm.get("G:" + reg)
        if gm is None:
            continue
        bb = _bbox(gm)
        if bb is None:
            continue
        g = gm[bb]
        cw = cover[g]
        np.maximum(seam[bb], line[g], out=seam[bb])
        inner = cw * (g > 200)
        for m in mus:
            mk = mm.get(m)
            if mk is not None:
                np.maximum(seam[bb], line[mk[bb]] * inner * 0.7, out=seam[bb])
        al = s_of(ratio[reg]) * AMAX
        np.maximum(alpha[bb], cw * al, out=alpha[bb])
    tinted = lin * k                            # one hue everywhere (round 5)
    over = np.clip(tinted.max(-1, keepdims=True) - 1, 0, None)
    tinted = np.clip(tinted, 0, 1) + over * 0.5
    a = alpha[..., None]
    sm = (SEAM * seam * np.clip(alpha / AMAX * 1.5, 0, 1))[..., None]
    return _to_srgb8((lin * (1 - a) + tinted * a) * (1 - sm))


_META_SKIN = [None]


def _font(size):
    from PIL import ImageFont
    for path in FONT_CANDIDATES:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def render(node_ratio, rows, out_path, title=None, legend=None,
           assets=DEFAULT_ASSETS):
    """Draw the photo.

    node_ratio  {kit node: ratio}   -- paints the body (through region_map)
    rows        [(label, pct, ratio)] -- the side panel, in message order;
                the SAME items and numbers the text lines carry
    title       one line above the bodies (user copy, from the caller)
    legend      {"front", "back", "scale_low", "scale_high", "empty"} labels
                (user copy, from the caller -- this file owns no sentence)
    Returns {"path", "ms", "size"}."""
    import numpy as np
    from PIL import Image, ImageDraw
    t0 = time.perf_counter()
    legend = legend or {}
    meta, views = _load(assets)
    _META_SKIN[0] = meta["skin_lin"]
    ratio = region_values(node_ratio, load_region_map(assets))
    W, H = meta["res"]
    x0, x1, y0 = 20, W - 20, 40
    imgs = {v: tint(b, mm, meta["group"], ratio)
            for v, (b, mm) in views.items()}
    bw, bh = x1 - x0, H - y0
    panel, top = 380, 64
    bg = tuple(int(x) for x in views[meta["views"][0]][0][5, 5])
    out = Image.new("RGB", (len(meta["views"]) * bw + panel, top + bh), bg)
    for i, v in enumerate(meta["views"]):
        out.paste(Image.fromarray(imgs[v][y0:, x0:x1]), (i * bw, top))
    d = ImageDraw.Draw(out)
    ink, mut = (238, 238, 238), (160, 160, 168)
    if title:
        d.text((18, 14), title, font=_font(34), fill=ink)
    for i, v in enumerate(meta["views"]):
        lab = legend.get(v)
        if lab:
            d.text((i * bw + 18, top + 8), lab, font=_font(26), fill=mut)
    px, y = len(meta["views"]) * bw + 24, top + 10
    f24, f18 = _font(24), _font(18)
    if not rows and legend.get("empty"):
        d.text((px, y), legend["empty"], font=f24, fill=ink)
        y += 44
    for label, pct, r in rows:
        d.rounded_rectangle((px, y + 4, px + 26, y + 30), 5, fill=swatch(r))
        d.text((px + 38, y), label, font=f24, fill=ink)
        d.text((px + 250, y), "%d%%" % pct, font=f24, fill=ink)
        y += 40
    y += 16
    bx, by, bwid, bhgt = px, y, 26, 200
    for i in range(bhgt):
        d.line([(bx, by + i), (bx + bwid, by + i)],
               fill=swatch(_inv_s(1 - i / float(bhgt - 1))))
    if legend.get("scale_high"):
        d.text((bx + bwid + 12, by - 4), legend["scale_high"], font=f18,
               fill=mut)
    if legend.get("scale_low"):
        d.text((bx + bwid + 12, by + bhgt - 22), legend["scale_low"],
               font=f18, fill=mut)
    t1 = time.perf_counter()
    ext = os.path.splitext(out_path)[1].lower()
    if ext in (".jpg", ".jpeg"):
        out.save(out_path, quality=88)
    else:
        out.save(out_path, compress_level=1)
    t2 = time.perf_counter()
    return {"path": out_path, "ms": int(round((t2 - t0) * 1000)),
            "compose_ms": int(round((t1 - t0) * 1000)),
            "size": list(out.size)}


def _inv_s(s):
    """ratio whose s_of() is s (legend bar)."""
    return 2 ** (2 * s) - 1


def main():
    """Subprocess entry (a render interpreter other than the caller's):
    one JSON payload on stdin -> the render result JSON on stdout."""
    import sys
    payload = json.load(sys.stdin)
    res = render(payload["node_ratio"], payload.get("rows") or [],
                 payload["out"], title=payload.get("title"),
                 legend=payload.get("legend"),
                 assets=payload.get("assets") or DEFAULT_ASSETS)
    print(json.dumps(res))


if __name__ == "__main__":
    main()
