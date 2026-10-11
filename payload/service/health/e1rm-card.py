#!/usr/bin/env python3
"""
e1rm-card.py -- per-exercise strength-trend card (e1RM line + volume bars).

DRAFT (2026-07-28): session-end telemetry card for one exercise. Plots the
cross-session e1RM trend (line, left axis) over the recent N sessions plus the
per-session training volume (bars, right axis). This CARD is display-only: it
renders the numbers it is handed and computes nothing.

The 2026-07-28 batch exclusion ("no prescription derived from e1RM") is
REPLACED by the owner ruling of 2026-09-30: when an exercise has working sets
with weight+reps in >= 3 distinct sessions, rx-calc prescribes the working load,
rep target and warm-up rungs FROM e1RM (service/health/e1rm_rx.py, rules in
e1rm_rx_rules.json); with less data the last-load progression stands unchanged.
The prescription computes its own estimate there -- nothing here feeds it.

e1RM formula (top set of the session):
    e1rm = weight_kg * (1 + (reps + rir) / 30)
Volume (per exercise, per session):
    volume = sum(weight_kg * reps) over that exercise's working sets.
    ASSISTED exercises (assist stack -- weight_kg is the COUNTERWEIGHT) use
    sum((bodyweight_at_the_time - weight_kg) * reps) instead; this card only
    PLOTS the points, set-table.session_history computes them and owns that
    branch (see service/health/assist_load.py).

Input JSON (arg / --file / stdin):
  {
    "exercise": "데드리프트",              # display name (program.yaml display)
    "points": [                            # oldest -> newest, "오늘" is last label
      {"label": "7/14", "e1rm": 122, "vol": 2.0},
      ...
    ],
    "unit": "t",                           # volume unit label (t = tonnes, or kg)
    "output": "files/outbox/e1rm_card.png" # optional; default /tmp/e1rm_card.png
  }

Reads ONLY the JSON handed to it. Numbers are copied verbatim -- the caller
computes e1RM/volume (session-held set data or program.yaml last/changelog);
this script never invents a value. Missing matplotlib -> exit 3 (caller falls
back to the ASCII live-track only).

Output: prints the PNG path to stdout.
"""

import sys
import os
import json

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
except ImportError:
    sys.stderr.write(
        "e1rm-card.py: matplotlib not available -- skipping card render. "
        "Point RENDER_PYTHON at a venv that has matplotlib.\n")
    raise SystemExit(3)

HERE = os.path.dirname(os.path.abspath(__file__))
# font dir shared with the diet/rx cards (dark-navy DS tone)
FDIR = os.path.abspath(os.path.join(HERE, '..', '..', '.claude', 'skills-bundle', 'diet-status', 'fonts'))
MED = os.path.join(FDIR, 'ASDGN_Medium.ttf')
XBD = os.path.join(FDIR, 'ASDGN_ExtraBold.ttf')
for f in (MED, XBD):
    if os.path.exists(f):
        fm.fontManager.addfont(f)
PROP_MED = fm.FontProperties(fname=MED) if os.path.exists(MED) else None
PROP_BLD = fm.FontProperties(fname=XBD) if os.path.exists(XBD) else None


# -- Design tokens (estate palette canon; DGN-376) ---------------------------
# This card previously used an off-brand github-dark palette; it now joins the
# brand navy surfaces by sourcing the card-dark token theme, so it moves with
# every other card on a token change.
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

_T = _load_design_tokens().theme('card-dark')

# card-dark theme palette. e1RM trend = primary series -> accent (teal);
# volume bars = secondary series -> purple (muted, alpha at draw time).
BG = _T['bg']
CARD = _T['surface']
GRID = _T['border']
TXT = _T['text']
SUB = _T['muted']
ACC = _T['accent']    # e1RM line (primary accent, teal)
BAR = _T['purple']    # volume bars (secondary, lavender)


def load():
    args = sys.argv[1:]
    if args and args[0] == '--file':
        with open(args[1]) as f:
            return json.load(f)
    if args:
        return json.loads(args[0])
    data = sys.stdin.read()
    if data.strip():
        return json.loads(data)
    raise SystemExit("e1rm-card.py: no JSON input (arg / --file / stdin)")


def main():
    d = load()
    exercise = d.get('exercise', '종목')
    pts = d.get('points', [])
    unit = d.get('unit', 't')
    out = d.get('output') or os.environ.get('E1RM_CARD_OUT') or '/tmp/e1rm_card.png'

    if len(pts) < 2:
        sys.stderr.write("e1rm-card.py: need >=2 points to draw a trend.\n")
        raise SystemExit(2)

    labels = [p.get('label', '') for p in pts]
    e1rm = [float(p['e1rm']) for p in pts]
    vol = [float(p.get('vol', 0)) for p in pts]

    fig, ax1 = plt.subplots(figsize=(6.4, 4.0), dpi=200)
    fig.patch.set_facecolor(BG)
    ax1.set_facecolor(CARD)
    x = range(len(labels))

    # volume bars (right axis)
    ax2 = ax1.twinx()
    # ax1.patch is hidden below (so the line draws over the bars); the visible
    # plot interior is therefore ax2's patch -- paint it the card surface so the
    # interior stays navy instead of matplotlib's default white.
    ax2.set_facecolor(CARD)
    bars = ax2.bar(x, vol, width=0.5, color=BAR, alpha=0.55, zorder=1)
    ax2.set_ylim(0, (max(vol) if max(vol) > 0 else 1) * 1.6)
    ax2.tick_params(axis='y', colors=SUB, labelsize=9)
    for lb in ax2.get_yticklabels():
        if PROP_MED:
            lb.set_fontproperties(PROP_MED)
    ax2.set_ylabel(f'볼륨 ({unit})', color=SUB, fontproperties=PROP_MED, fontsize=10)

    # e1RM line (left axis)
    line, = ax1.plot(x, e1rm, color=ACC, lw=2.6, marker='o', ms=7,
                     mfc=ACC, mec=BG, mew=1.5, zorder=3)
    ax1.set_ylim(min(e1rm) - 8, max(e1rm) + 8)
    for xi, yi in zip(x, e1rm):
        txt = f'{yi:g}'
        ax1.annotate(txt, (xi, yi), textcoords='offset points', xytext=(0, 10),
                     ha='center', color=TXT, fontproperties=PROP_BLD, fontsize=10)

    ax1.set_zorder(ax2.get_zorder() + 1)
    ax1.patch.set_visible(False)
    ax1.tick_params(axis='y', colors=ACC, labelsize=9)
    ax1.tick_params(axis='x', colors=TXT, labelsize=10)
    ax1.set_xticks(list(x))
    ax1.set_xticklabels(labels)
    for lb in ax1.get_xticklabels():
        if PROP_MED:
            lb.set_fontproperties(PROP_MED)
    for lb in ax1.get_yticklabels():
        if PROP_MED:
            lb.set_fontproperties(PROP_MED)
    ax1.set_ylabel('e1RM (kg)', color=ACC, fontproperties=PROP_MED, fontsize=10)
    ax1.grid(axis='y', color=GRID, lw=0.7, alpha=0.5)
    for sp in ax1.spines.values():
        sp.set_color(GRID)
    for sp in ax2.spines.values():
        sp.set_color(GRID)

    # title + delta caption
    fig.text(0.11, 0.94, f'{exercise} — 최근 추세', color=TXT,
             fontproperties=PROP_BLD, fontsize=15)
    delta = e1rm[-1] - e1rm[0]
    pct = (delta / e1rm[0] * 100) if e1rm[0] else 0
    fig.text(0.11, 0.885, f'e1RM {delta:+g}kg ({pct:+.1f}%) · {len(pts)}세션',
             color=SUB, fontproperties=PROP_MED, fontsize=9.5)

    leg = ax1.legend([line, bars], ['e1RM (kg)', f'볼륨 ({unit})'],
                     loc='lower right', frameon=False, fontsize=9,
                     labelcolor=TXT, prop=PROP_MED)

    plt.subplots_adjust(left=0.11, right=0.89, top=0.83, bottom=0.11)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    fig.savefig(out, facecolor=BG)
    print(os.path.abspath(out))


if __name__ == '__main__':
    main()
