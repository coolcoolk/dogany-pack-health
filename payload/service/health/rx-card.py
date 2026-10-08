#!/usr/bin/env python3
"""
rx-card.py -- daily workout routine renderer (text table OR dark-navy image).

Renders the rx-calc JSON (today's prescription). Two output surfaces:

  --text  (DEFAULT morning-push surface): a Telegram-HTML <pre> code block in
          the workout-session "세션 시작 시 전체 루틴 표" (session-start routine
          table) format -- the same card-style lineup the agent shows at live-session
          start (mat-prep overview row, per-slot 2-line cards: slot + 종목, then
          "└ <n> sets  <weight>kg  <lo>-<hi> REPS", W prep rows). NO matplotlib;
          prints to stdout. Rest day / empty rx -> prints nothing (silent).

  (no flag): the legacy dark-navy table IMAGE (matplotlib). Title:
          "오늘 운동 루틴 | <split day>". Prints the PNG path to stdout.

Usage:
  python3 rx-card.py --text --file rx.json      # text table (default surface)
  python3 rx-card.py --text '<rx-calc-json>'    # text table from JSON arg
  cat rx.json | python3 rx-card.py --text        # text table from stdin
  python3 rx-card.py --file rx.json             # legacy PNG image
  python3 rx-card.py '<rx-calc-json>'           # legacy PNG image (stdin/arg)

Image output path via env RX_CARD_OUT (default: /tmp/rx_card.png).

Reads ONLY the rx-calc JSON. Weight numbers are copied verbatim (never
invented) -- calibration slots (weight_kg null) render weight-free, no
placeholder, no "무게 알려주세요" text (DGN-301 render rule).

Image path deps: matplotlib (loaded lazily, only for the image surface). If it
is unavailable the IMAGE path exits code 3 with a clear stderr message so
callers can fall back; the --text path never needs matplotlib.
"""

import sys
import os
import json
import html

# -- Fonts: reuse the diet-status skill's bundled TTFs (single font asset) -----
# This file lives at <PROJECT_ROOT>/service/health/. The diet-status fonts live
# at <PROJECT_ROOT>/.claude/skills/diet-status/fonts/ -- same pack, same truck
# since kit_life 2.19.0 moved the coaching half here. Path-independent.
_FONT_DIR = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', '..',
    '.claude', 'skills', 'diet-status', 'fonts'))
_FONT_MED = os.path.join(_FONT_DIR, 'ASDGN_Medium.ttf')
_FONT_XBLD = os.path.join(_FONT_DIR, 'ASDGN_ExtraBold.ttf')

_TTC_CANDIDATES = [
    os.environ.get('RX_CARD_TTC', ''),
    '/System/Library/Fonts/AppleSDGothicNeo.ttc',
]


def _try_extract_from_ttc():
    ttc_path = next((p for p in _TTC_CANDIDATES if p and os.path.exists(p)), None)
    if not ttc_path:
        return False
    try:
        from fontTools.ttLib import TTCollection
    except ImportError:
        return False
    try:
        os.makedirs(_FONT_DIR, exist_ok=True)
        ttc = TTCollection(ttc_path)
        ttc.fonts[2].save(_FONT_MED)   # Medium
        ttc.fonts[14].save(_FONT_XBLD)  # ExtraBold
        return True
    except Exception:
        return False


def _resolve_fonts():
    have = os.path.exists(_FONT_MED) and os.path.exists(_FONT_XBLD)
    if not have:
        have = _try_extract_from_ttc()
    if have:
        fm.fontManager.addfont(_FONT_MED)
        fm.fontManager.addfont(_FONT_XBLD)
        return fm.FontProperties(fname=_FONT_MED), fm.FontProperties(fname=_FONT_XBLD)
    sys.stderr.write(
        "rx-card.py: skill fonts not found and no usable system TTC -- falling "
        "back to matplotlib default font (CJK text may not render).\n")
    return fm.FontProperties(), fm.FontProperties(weight='bold')


# -- Design tokens (estate palette canon; DGN-376) ---------------------------
# Palette comes from the single design-token canon (routines/lib/design_tokens
# card-dark theme), not hardcoded, so all cards move together on a token change.
def _load_design_tokens():
    import importlib.util
    parent = os.path.dirname(os.path.abspath(__file__))
    for _ in range(6):
        cand = os.path.join(parent, 'routines', 'lib', 'design_tokens.py')
        if os.path.isfile(cand):
            spec = importlib.util.spec_from_file_location('design_tokens', cand)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return mod
        nxt = os.path.dirname(parent)
        if nxt == parent:
            break
        parent = nxt
    raise ImportError('design_tokens.py not found from %s' % __file__)


# matplotlib + fonts + palette are needed ONLY for the image render path. They
# are loaded lazily so the text-table path (below) has ZERO image dependency:
# on a box without matplotlib the text renderer still works. render() calls this
# once; it populates the module globals the image code references.
plt = None
fm = None
FancyBboxPatch = None
prop = None
bold_prop = None
BG = PANEL = ROW_ALT = INK = INK_SOFT = INK_DIM = None
ACCENT = WEIGHT = FOCUS = SAFETY = SEP_LINE = None


def _ensure_image_deps():
    """Load matplotlib/fonts/palette for the image path. Exits 3 (same contract
    as before) when matplotlib is unavailable so callers fall back to text."""
    global plt, fm, FancyBboxPatch, prop, bold_prop
    global BG, PANEL, ROW_ALT, INK, INK_SOFT, INK_DIM
    global ACCENT, WEIGHT, FOCUS, SAFETY, SEP_LINE
    if plt is not None:
        return
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as _plt
        import matplotlib.font_manager as _fm
        from matplotlib.patches import FancyBboxPatch as _FancyBboxPatch
    except ImportError as e:
        sys.stderr.write(
            "rx-card.py: matplotlib not available in this interpreter -- skipping "
            "card render. Point RENDER_PYTHON at a venv that has matplotlib. "
            f"({e})\n")
        sys.exit(3)
    plt, fm, FancyBboxPatch = _plt, _fm, _FancyBboxPatch
    prop, bold_prop = _resolve_fonts()
    _T = _load_design_tokens().theme('card-dark')
    # INK_DIM / ROW_ALT have no 11-slot token; documented card-local shades.
    BG        = _T['bg']       # deep navy page
    PANEL     = _T['surface']  # table panel
    ROW_ALT   = '#20204A'      # zebra row (card-local; no token slot)
    INK       = _T['text']
    INK_SOFT  = _T['muted']
    INK_DIM   = '#8A93C4'      # dim label (card-local; no token slot)
    ACCENT    = _T['accent']   # split-day accent
    WEIGHT    = _T['yellow']   # weight value
    FOCUS     = _T['orange']   # focus-slot tag
    SAFETY    = _T['red']      # safety note tint
    SEP_LINE  = _T['border']


def _load_input():
    """Return the rx-calc dict from argv/stdin/--file."""
    args = sys.argv[1:]
    if args and args[0] == '--file':
        with open(args[1], 'r', encoding='utf-8') as f:
            return json.load(f)
    if args and args[0].strip().startswith('{'):
        return json.loads(args[0])
    data = sys.stdin.read()
    if data.strip():
        return json.loads(data)
    raise SystemExit("rx-card.py: no JSON input (arg / --file / stdin)")


def _reps(ex):
    rr = ex.get('rep_range') or []
    if len(rr) == 2:
        return f"{rr[0]}-{rr[1]}회"
    if len(rr) == 1:
        return f"{rr[0]}회"
    return "-"


def _weight_label(ex):
    """Verbatim weight, or calibration mark. Never a placeholder request."""
    w = ex.get('weight_kg')
    if w is None:
        return None  # calibration -> weight column blank + '캘리브레이션' tag
    # keep decimals verbatim (21.25 stays 21.25; 115.0 -> 115)
    if isinstance(w, float) and w.is_integer():
        return f"{int(w)}kg"
    return f"{w}kg"


def _rest_label(ex):
    """Designated rest in Korean minutes and optional seconds (from rx-calc).
    None when absent/invalid -> row renders rest-free (backward compatible)."""
    r = ex.get('rest_sec')
    if not isinstance(r, (int, float)) or isinstance(r, bool) or r <= 0:
        return None
    r = int(r)
    minutes, seconds = divmod(r, 60)
    return f"휴식 {minutes}분" + (f" {seconds}초" if seconds else "")


# ============================================================================
# Session-start routine table renderer (default morning-push surface).
#
# Mirrors the EXACT format of the workout-session skill's "(1) 세션 시작 시
# 전체 루틴 표" (SKILL.md, owner-confirmed 2026-07-18/07-29/08-06): the same
# card-style code block the agent gives when a live session starts. This morning
# push is the day's exercise lineup in that identical visual style -- so the
# pre-session view and the in-session view read the same.
#
# Format (SKILL spec, verbatim):
#   - NO column header row. Exercises are continuous (no blank line between).
#   - Code block; the morning surface renders it inside a Telegram-HTML <pre>.
#   - Mat-prep overview row at the top (above slot 1), when warmup.mat_prep is
#     present:
#         0 매트 준비운동 (세션 시작 · 하나씩 순차)
#            └ <drill 1>
#            └ <drill 2>
#         one drill per └ line (mirrors the per-slot cards; owner req 2026-08-10).
#   - Per exercise = 2 lines:
#         <slot> <display name>
#            └ <n> sets  <weight>kg  <lo>-<hi> REPS   (2 spaces between tokens)
#     Calibration (weight_kg null): omit the <weight>kg token, append
#     "  (첫 세션)" after REPS. Never a weight placeholder (DGN-301 render rule).
#   - Pre-slot-prep W row: for a slot whose rx-calc pre_slot_prep is non-null,
#     add one line "W <pre_slot_prep>" directly ABOVE that slot's line 1.
#   - Marker MUST be "└" (U+2514), never the Hangul jamo "ㄴ" (width drifts).
#
# The morning view shows the LINEUP only -- setup/execution cues, rest, RIR,
# per-set targets belong to the LIVE in-session surface (rest-timer pushes,
# per-set rx display), NOT this at-a-glance card. Evidence: the SKILL defines
# (1) as the "세션 시작 1회" whole-routine overview (종목/세트/목표반복), while
# RIR / rest / setup-execution cues live in the per-set rx display and the
# rest-timer stack (SKILL "dynamic 30s-grid", "per-set rx display") -- separate
# in-session tables. So this card carries slot / 종목 / n sets / weight / rep
# range + the prep overview rows, matching (1) exactly, and no more.
#
# NO matplotlib. User-facing wording only (no rx-calc/처방/파일 jargon).
# ============================================================================

_TREE = "└"  # └  (U+2514) -- fixed monospace width 1; never Hangul "ㄴ"


def _reps_token(ex):
    """Rep token for the TEXT card -- delegates to _reps (the PNG formatter).

    This used to render '<lo>-<hi> REPS' while _reps, 70 lines up in this SAME
    file, rendered '<lo>-<hi>회' for the PNG of the SAME card. One card, two
    languages, decided by which surface you happened to look at -- and the text
    path is the DEFAULT one pushed every morning, so English was the version the
    user actually read. 표(3) already moved REPS -> 회; this finishes that sweep.
    표(1) is explicitly exempt from the ASCII column-width rule
    (progress-tables.md), so no alignment reason kept the English.
    Absent range -> '-' (same as the PNG): never invent a range."""
    return _reps(ex)


def _detail_line(ex):
    """The '   └ <n>세트  <weight>kg  <lo>-<hi>회' line (SKILL (1) spec).

    Calibration (weight_kg null) -> omit the weight token, append '  (첫 세션)'
    after the rep token. Weight kept verbatim (21.25kg stays 21.25kg;
    135.0 -> 135kg). per_side loading -> weight token marked '(한쪽)'.
    'sets' -> '세트' with REPS -> 회 (same leak, same card); the tree line is not
    a padded column, so widening a token cannot break alignment here."""
    sets = ex.get('sets', '?')
    reps = _reps_token(ex)
    w = ex.get('weight_kg')
    if w is None:
        # first-session calibration: no weight token, rep token then (첫 세션)
        return f"   {_TREE} {sets}세트  {reps}  (첫 세션)"
    # Weight verbatim, MATCHING the SKILL (1) session-start example which keeps
    # the one-decimal form for whole floats (40.0kg / 100.0kg / 20.0kg). Only an
    # int input (no decimal in the source) renders bare (e.g. 135 -> 135kg);
    # non-whole decimals stay exact (28.125 / 16.25). Never invent a number.
    if isinstance(w, float):
        wtok = f"{w:g}kg" if (w != int(w)) else f"{w:.1f}kg"
    else:
        wtok = f"{w}kg"
    if ex.get('loading') == 'per_side':
        wtok += " (한쪽)"
    return f"   {_TREE} {sets}세트  {wtok}  {reps}"


def _cooldown_session_items(rx):
    """Session-level cooldown drills from rx['cooldown']['session'], or [].

    Defensive in the same style as the warmup block: any shape other than a
    list of strings degrades to empty, so a bad prep.yaml edit cannot break the
    morning push. rx dicts produced before 2026-08-22 have no 'cooldown' key
    at all -> [] -> the card renders exactly as it did then."""
    cd = rx.get('cooldown') or {}
    if not isinstance(cd, dict):
        return []
    items = cd.get('session') or []
    if not isinstance(items, list):
        return []
    return [str(d) for d in items if d]


def _cooldown_lines(rx):
    """The card's bottom cooldown block, or [] when there is none.

    Deliberate mirror of the "0 매트 준비운동" block at the top: same header +
    "   └ <drill>" per-line shape, at the opposite end of the card because
    cooldown is performed after the last slot. The block is a PEER of the prep
    block and the slot list, not a footnote on one of them (owner ruling
    2026-08-21) -- but it is NOT training volume: no set count, no weight, no
    rep range on these rows, and rx-calc never lets a cooldown item into an
    aggregate (see rx-calc NON_VOLUME_KINDS / day_work_items)."""
    items = _cooldown_session_items(rx)
    if not items:
        return []
    out = ["C 쿨다운 (세션 마무리 · 하나씩 순차)"]
    for d in items:
        out.append("   %s %s" % (_TREE, d))
    return out


def render_text(rx):
    """Render today's routine as the session-start routine table, wrapped in a
    Telegram-HTML <pre> code block (the morning-push surface).

    Returns "" when there is nothing to show (rest day / empty rx) so the caller
    stays silent -- matching existing rest-day behavior (rx-gen emits nothing).
    """
    exercises = rx.get('exercises', []) or []
    if not exercises:
        return ""  # rest day / empty -> silent (caller sends nothing)

    split = rx.get('rotation_day', '?')
    lines = []

    # ---- mat-prep overview row (top, above slot 1), when present ----
    warmup = rx.get('warmup') or {}
    mat_prep = warmup.get('mat_prep') or []
    if not isinstance(mat_prep, list):
        mat_prep = []
    if mat_prep:
        lines.append("0 매트 준비운동 (세션 시작 · 하나씩 순차)")
        # One drill per line under the header (each its own └ row), mirroring the
        # per-slot exercise cards -- easier to scan / check off one at a time than
        # the old single " · "-joined line (owner request 2026-08-10).
        for d in mat_prep:
            lines.append("   %s %s" % (_TREE, str(d)))

    # ---- equipment-prep overview row (needs equipment but NOT bound to one
    # slot -- e.g. an optional knee drill on a day with no knee-dominant
    # compound). Distinct from mat_prep (bodyweight/band, no equipment) --
    # never folded into the "매트 준비운동" block. ----
    equipment_prep = warmup.get('equipment_prep') or []
    if not isinstance(equipment_prep, list):
        equipment_prep = []
    if equipment_prep:
        lines.append("E 장비 준비운동 (슬롯 무관 · 필요 시)")
        for d in equipment_prep:
            lines.append("   %s %s" % (_TREE, str(d)))

    # ---- per-exercise cards (2 lines each; optional W prep row above,
    # optional C cooldown row below) ----
    for i, ex in enumerate(exercises):
        psp = ex.get('pre_slot_prep')
        if psp:
            lines.append("W %s" % str(psp))  # W row: column 0, no └ (no collision)
        slot = ex.get('slot', i + 1)
        name = ex.get('display', ex.get('name', '-'))
        lines.append(f"{slot} {name}")
        lines.append(_detail_line(ex))
        # C row: a cooldown drill pinned to THIS slot renders directly BELOW it
        # (mirror of the W row above). Empty today -- no cooldown item carries a
        # card_slot -- so this adds nothing to the current render.
        psc = ex.get('post_slot_cooldown')
        if psc:
            lines.append("C %s" % str(psc))

    # ---- cooldown block (bottom, after the last slot) ----
    lines.extend(_cooldown_lines(rx))

    body = "\n".join(html.escape(l, quote=False) for l in lines)
    pre = "<pre>" + body + "</pre>"

    # Title outside the code block; user-facing wording (no internal jargon).
    title = f"오늘의 운동 루틴 | {html.escape(str(split), quote=False)}"
    return "\n".join([title, pre])


def render(rx, out_path):
    _ensure_image_deps()  # lazy: loads matplotlib/fonts/palette (exit 3 if absent)
    split = rx.get('rotation_day', '?')
    exercises = rx.get('exercises', []) or []
    provisional = bool(rx.get('provisional_tag'))

    # recovery (fatigue-trim) note: at most one line, names copied from JSON
    trimmed = [ex for ex in exercises if ex.get('fatigue_trim')]

    n = len(exercises)
    total_sets = sum(int(ex.get('sets') or 0) for ex in exercises)
    est_min = int(round(total_sets * 3))  # ~3 min/set incl rest (footer estimate)

    # warmup / mat-prep block (session mobility prep; mirror of
    # stretch-matrix.md). Absent 'warmup'/'mat_prep' -> zero height, nothing
    # drawn (old JSON without this key renders exactly as before).
    warmup = rx.get('warmup') or {}
    mat_prep = warmup.get('mat_prep') or []
    if not isinstance(mat_prep, list):
        mat_prep = []
    equipment_prep = warmup.get('equipment_prep') or []
    if not isinstance(equipment_prep, list):
        equipment_prep = []
    warmup_line_h = 0.26
    warmup_h = (0.34 + warmup_line_h * len(mat_prep)) if mat_prep else 0.0
    warmup_h += (0.34 + warmup_line_h * len(equipment_prep)) if equipment_prep else 0.0

    # cooldown block (NEW 2026-08-22): peer of the prep block, drawn at the
    # BOTTOM (below the slot table, above the footer) because it is performed
    # after the last slot. Absent 'cooldown' -> zero height, nothing drawn, so
    # an rx dict from before this block renders exactly as it did.
    cooldown_items = _cooldown_session_items(rx)
    cooldown_h = ((0.34 + warmup_line_h * len(cooldown_items))
                  if cooldown_items else 0.0)

    # -- geometry (inches) --
    W = 8.0
    header_h = 1.35
    row_h = 0.92
    foot_h = 0.95
    note_h = 0.5 if (trimmed or provisional) else 0.0
    H = (header_h + row_h * n + foot_h + note_h + warmup_h + cooldown_h + 0.5)

    fig = plt.figure(figsize=(W, H), facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis('off')
    fig.patch.set_facecolor(BG)

    y = H - 0.55

    # -- title: 오늘 운동 루틴 | <split> --
    ax.text(0.55, y, "오늘 운동 루틴", fontsize=25, color=INK,
            fontproperties=bold_prop, va='center', ha='left')
    # measure-ish: place the split tag after a separator
    ax.text(0.55 + 3.05, y, "|", fontsize=22, color=INK_DIM,
            fontproperties=prop, va='center', ha='left')
    ax.text(0.55 + 3.35, y, split, fontsize=25, color=ACCENT,
            fontproperties=bold_prop, va='center', ha='left')

    y -= 0.62
    basis = rx.get('rotation_basis', '')
    if basis:
        ax.text(0.57, y, basis, fontsize=10.5, color=INK_DIM,
                fontproperties=prop, va='center', ha='left')

    # -- warmup / mat-prep block (drawn only when present; height already
    # folded into warmup_h so the table never clips) --
    if mat_prep:
        y -= 0.34
        ax.text(0.57, y, "웜업 · 매트 준비운동", fontsize=10.5, color=INK_SOFT,
                fontproperties=bold_prop, va='center', ha='left')
        for item in mat_prep:
            y -= warmup_line_h
            ax.text(0.72, y, "· " + str(item), fontsize=9.5, color=INK_DIM,
                    fontproperties=prop, va='center', ha='left')

    # -- equipment-prep block (needs equipment, not bound to one slot;
    # kept visually distinct from the mat-prep block above) --
    if equipment_prep:
        y -= 0.34
        ax.text(0.57, y, "웜업 · 장비 준비운동 (슬롯 무관)", fontsize=10.5, color=INK_SOFT,
                fontproperties=bold_prop, va='center', ha='left')
        for item in equipment_prep:
            y -= warmup_line_h
            ax.text(0.72, y, "· " + str(item), fontsize=9.5, color=INK_DIM,
                    fontproperties=prop, va='center', ha='left')

    # -- table panel --
    top = y - 0.3
    panel_top = top
    panel_bottom = foot_h + note_h + cooldown_h + 0.1
    panel = FancyBboxPatch(
        (0.4, panel_bottom), W - 0.8, panel_top - panel_bottom,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        linewidth=0, facecolor=PANEL, zorder=1)
    ax.add_patch(panel)

    # column x positions
    x_num = 0.75
    x_name = 1.25
    x_weight = W - 2.75
    x_reps = W - 1.35

    ry = panel_top - 0.15
    for i, ex in enumerate(exercises):
        rc = ry - row_h
        if i % 2 == 1:
            zb = FancyBboxPatch(
                (0.5, rc + 0.06), W - 1.0, row_h - 0.12,
                boxstyle="round,pad=0.0,rounding_size=0.06",
                linewidth=0, facecolor=ROW_ALT, zorder=2)
            ax.add_patch(zb)

        mid = rc + row_h / 2

        # stacked sub-tags under the exercise name (focus / slot-prep /
        # safety), each a dim one-liner in the same visual family but a
        # distinct color+marker. Lift the name so the stack stays centered.
        subs = []
        if ex.get('focus_slot'):
            subs.append(("◆ 포커스", FOCUS))
        psp = ex.get('pre_slot_prep')
        if psp:
            subs.append(("▶ " + str(psp), ACCENT))
        psc = ex.get('post_slot_cooldown')
        if psc:
            # slot-pinned cooldown, mirror of the ▶ prep sub-tag. Empty today.
            subs.append(("◀ " + str(psc), ACCENT))
        sn = ex.get('safety_note')
        if sn:
            note = sn.split('--')[-1].strip() if '--' in sn else sn
            note = note.split('.')[0].strip()
            if len(note) > 46:
                note = note[:45] + "…"
            subs.append(("● " + note, SAFETY))

        sub_step = 0.24
        name_mid = mid + (sub_step / 2) * len(subs)

        # slot number
        ax.text(x_num, name_mid, str(ex.get('slot', i + 1)), fontsize=15,
                color=INK_DIM, fontproperties=bold_prop, va='center',
                ha='center', zorder=3)
        # exercise name
        disp = ex.get('display', ex.get('name', '-'))
        ax.text(x_name, name_mid, disp, fontsize=15, color=INK,
                fontproperties=bold_prop, va='center', ha='left', zorder=3)

        # sub-tags, stacked downward from the name
        sy = name_mid
        for text, color in subs:
            sy -= sub_step
            ax.text(x_name, sy, text, fontsize=9.5, color=color,
                    fontproperties=prop, va='center', ha='left', zorder=3)

        # weight
        wl = _weight_label(ex)
        if wl is None:
            ax.text(x_weight, mid, "캘리브레이션", fontsize=10.5, color=INK_DIM,
                    fontproperties=prop, va='center', ha='center', zorder=3)
        else:
            ax.text(x_weight, mid, wl, fontsize=16, color=WEIGHT,
                    fontproperties=bold_prop, va='center', ha='center', zorder=3)

        # sets x reps (+ designated rest line, DGN-388)
        sr = f"{ex.get('sets', '?')}세트\n{_reps(ex)}"
        rest_lbl = _rest_label(ex)
        ax.text(x_reps, mid + (0.14 if rest_lbl else 0.0), sr, fontsize=12.5,
                color=INK_SOFT, fontproperties=prop, va='center', ha='center',
                linespacing=1.25, zorder=3)
        if rest_lbl:
            ax.text(x_reps, mid - 0.30, rest_lbl, fontsize=10, color=INK_DIM,
                    fontproperties=prop, va='center', ha='center', zorder=3)

        # (focus / slot-prep / safety sub-tags already drawn above via subs)

        # row separator
        if i < n - 1:
            ax.plot([0.6, W - 0.6], [rc + 0.03, rc + 0.03],
                    color=SEP_LINE, linewidth=0.8, zorder=2)
        ry = rc

    # -- cooldown block (below the slot panel, above the note/footer; height
    # already folded into cooldown_h + panel_bottom so nothing clips) --
    if cooldown_items:
        cy = foot_h + note_h + cooldown_h - 0.10
        ax.text(0.57, cy, "쿨다운 · 세션 마무리", fontsize=10.5, color=INK_SOFT,
                fontproperties=bold_prop, va='center', ha='left')
        for item in cooldown_items:
            cy -= warmup_line_h
            ax.text(0.72, cy, "· " + str(item), fontsize=9.5, color=INK_DIM,
                    fontproperties=prop, va='center', ha='left')

    # -- recovery / provisional note --
    ny = foot_h + note_h - 0.1
    if trimmed:
        parts = trimmed[0].get('muscle_state', {}) or {}
        body = parts.get('body_part') or parts.get('muscle') or "해당 부위"
        names = ", ".join(ex.get('display', '') for ex in trimmed)
        ax.text(0.55, ny, f"• 오늘은 {body} 회복을 봐서 {names} 세트를 덜 갑니다",
                fontsize=11, color=ACCENT, fontproperties=prop,
                va='center', ha='left')
        ny -= 0.32
    if provisional:
        ax.text(0.55, ny, "* 로테이션 위치 미확정 -- 세션 완료 후 스플릿 일 확인 부탁드려요",
                fontsize=10, color=INK_DIM, fontproperties=prop,
                va='center', ha='left')

    # -- footer: totals --
    ax.plot([0.4, W - 0.4], [foot_h - 0.05, foot_h - 0.05],
            color=SEP_LINE, linewidth=1.0)
    fy = foot_h / 2 - 0.05
    ax.text(0.55, fy, f"{n}종목 · {total_sets}세트", fontsize=13,
            color=INK, fontproperties=bold_prop, va='center', ha='left')
    ax.text(W - 0.55, fy, f"예상 약 {est_min}분", fontsize=13,
            color=INK_SOFT, fontproperties=prop, va='center', ha='right')

    fig.savefig(out_path, facecolor=BG, dpi=200,
                bbox_inches='tight', pad_inches=0.15)
    plt.close(fig)
    return out_path


def main():
    # --text mode (default morning-push surface): print the <pre> text table to
    # stdout, no image. Strip the flag so _load_input still sees --file/{json}/stdin.
    text_mode = False
    if len(sys.argv) > 1 and sys.argv[1] == '--text':
        text_mode = True
        del sys.argv[1]

    rx = _load_input()

    if text_mode:
        out = render_text(rx)  # "" on rest day / empty -> print nothing (silent)
        if out:
            print(out)
        return

    out = os.environ.get('RX_CARD_OUT', '/tmp/rx_card.png')
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    path = render(rx, out)
    print(path)


if __name__ == '__main__':
    main()
