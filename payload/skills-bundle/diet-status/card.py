#!/usr/bin/env python3
"""
diet-status card generator (dark theme).
Usage: python3 card.py '<json>'

Input JSON (all keys optional; if meals/intake_kcal are absent, the card reads
that date's meals+workouts straight from kit_life.db):
{
  "date": "2026-06-25",              // YYYY-MM-DD for kit_life.db lookup (default: today KST)
  "intake_kcal": {"current": 772},   // omit goal -> auto from body stats (config table)
  "protein":     {"current": 37.0},  // omit goal -> stats.protein_g fixed
  "carbs":       {"current": 72.5},  // omit goal -> auto from total target
  "fat":         {"current": 41.2},  // omit goal -> total x fat_ratio / 9 auto
  "burn_kcal":   {"current": 172, "detail": "..."},  // optional; hidden if absent
  "meals": [
    {"type": "아침", "name": "...", "kcal": 166, "protein": 14.7, "carbs": 26.2, "fat": 13.3}
  ],
  "output": "files/outbox/diet_card.png"   // optional, default: /tmp/diet_card.png
}

Concept:
  Visualizes "the more you exercise, the larger the recommended intake bar."
  Total track (= eff_goal) = [base_goal segment] + [exercise-added segment],
  with intake (coral) overlaid from left=0.

Output: prints the PNG path to stdout.

Rendering deps: matplotlib. This script is meant to be launched by a python that
has matplotlib installed. The SKILL.md documents resolving that interpreter via
RENDER_PYTHON (env) with fallbacks. If matplotlib is unavailable, this script
exits with a clear message so callers can gracefully skip the card.
"""

import sys
import json
import os
import re
import datetime

# matplotlib is needed to DRAW, not to count. The projection / shortlist
# modes (and suggest.py, which imports this module for the target) run on any
# python3, so the import failure is remembered here and the graceful-skip
# contract (stderr line + exit 3) fires only when a render is actually asked.
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import matplotlib.font_manager as fm
    _MPL_ERR = None
except ImportError as e:
    plt = fm = None
    _MPL_ERR = e


def _require_matplotlib():
    """Graceful skip contract: non-zero exit + a clear stderr message. Callers
    (SKILL.md flow) detect this and skip the card without failing the log."""
    if _MPL_ERR is not None:
        sys.stderr.write(
            "card.py: matplotlib not available in this interpreter -- skipping card "
            "render. Install matplotlib or point RENDER_PYTHON at a venv that has it. "
            f"({_MPL_ERR})\n")
        sys.exit(3)

# -- kit_life.py core (structured lane) as single source of truth --------------
# The skill lives at <PROJECT_ROOT>/.claude/skills/diet-status/, and kit_life lives
# at <PROJECT_ROOT>/database/. That is three levels up from this file's dir.
# PROJECT_ROOT-relative and path-independent (no absolute/parent-tree paths).
_DATA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', '..', '..', 'database'))
if _DATA_DIR not in sys.path:
    sys.path.insert(0, _DATA_DIR)
import kit_life as life

# -- Design tokens (single canon; DGN-376 T3) ---------------------------------
# design_tokens.py (and, from framework 2.6.0, card_blocks.py) live at
# <agent_root>/routines/lib/. This script is under .claude/skills-bundle/
# diet-status/, so walk up and import them by file path (no package install
# assumed). Loaded before fonts/colors, which consume them.
def _find_routines_lib():
    here = os.path.dirname(os.path.abspath(__file__))
    parent = here
    for _ in range(8):
        cand = os.path.join(parent, 'routines', 'lib')
        if os.path.isfile(os.path.join(cand, 'design_tokens.py')):
            return cand
        nxt = os.path.dirname(parent)
        if nxt == parent:
            break
        parent = nxt
    raise ImportError('design_tokens.py not found from %s' % here)


def _load_lib(lib_dir, fname, modname):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        modname, os.path.join(lib_dir, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_LIB_DIR = _find_routines_lib()
_tokens = _load_lib(_LIB_DIR, 'design_tokens.py', 'design_tokens')
_BRAND = _tokens.BRAND


def _card_palette():
    """DGN-768 S2: the framework's card_palette() -- card-light with the accent
    slot resolved from this agent's config/agent.conf (AGENT_ACCENT > crew >
    kit accent > teal). Returns None on a framework that predates it (< 2.6.0,
    i.e. 2.6.0-dev builds before .68) or when it cannot run; the card then
    degrades to the legacy card-dark theme below, pixel-identical to 0.26.0.
    Never raises: a colour lookup must not cost the owner the card."""
    try:
        cb = _load_lib(_LIB_DIR, 'card_blocks.py', 'card_blocks')
        fn = getattr(cb, 'card_palette', None)
        if not callable(fn):
            return None
        root = os.path.dirname(os.path.dirname(_LIB_DIR))
        pal = fn(conf_path=os.path.join(root, 'config', 'agent.conf'))
        need = ('bg', 'surface', 'border', 'text', 'muted', 'accent',
                'green', 'yellow', 'red')
        return pal if all(pal.get(k) for k in need) else None
    except Exception:            # noqa: BLE001 -- see docstring
        return None


_PAL = _card_palette()
PALETTE_SOURCE = 'card_palette' if _PAL is not None else 'card-dark'
_T = _tokens.theme('card-dark') if _PAL is None else None

# -- Fonts (path-independent, graceful) ---------------------------------------
# Preference order:
#   1) Bundled TTFs shipped with the skill (fonts/*.ttf) -- fully portable.
#   2) Extract from a system TTC found via a candidate list (env DIET_CARD_TTC
#      first, then common macOS locations) -- best effort only.
#   3) Fall back to matplotlib's default font (CJK may not render, but the card
#      still draws). Never hardcode an absolute font path as a hard dependency.
# Font filenames come from the token FONTS block (DGN-376 T3); this skill owns
# the physical fonts/ dir locally (plus a system-TTC extraction fallback).
FONT_DIR  = os.path.join(os.path.dirname(__file__), 'fonts')
FONT_MED  = os.path.join(FONT_DIR, _tokens.FONTS['medium'])
FONT_XBLD = os.path.join(FONT_DIR, _tokens.FONTS['extrabold'])

# Candidate system TTC files to source the fonts from if the bundled TTFs are
# missing. Env override wins; then common CJK-capable system fonts.
_TTC_CANDIDATES = [
    os.environ.get('DIET_CARD_TTC', ''),
    '/System/Library/Fonts/AppleSDGothicNeo.ttc',
]


def _try_extract_from_ttc():
    """Best-effort: extract Medium/ExtraBold faces from a system TTC into fonts/.
    Returns True on success. Silent no-op if no TTC/fontTools available."""
    ttc_path = next((p for p in _TTC_CANDIDATES if p and os.path.exists(p)), None)
    if not ttc_path:
        return False
    try:
        from fontTools.ttLib import TTCollection
    except ImportError:
        return False
    try:
        os.makedirs(FONT_DIR, exist_ok=True)
        ttc = TTCollection(ttc_path)
        # AppleSDGothicNeo.ttc: index 2 = Medium, 14 = ExtraBold.
        ttc.fonts[2].save(FONT_MED)
        ttc.fonts[14].save(FONT_XBLD)
        return True
    except Exception:
        return False


def _resolve_fonts():
    """Return (prop, bold_prop). Uses bundled TTFs if present, else tries to
    extract from a system TTC, else falls back to matplotlib defaults."""
    have = os.path.exists(FONT_MED) and os.path.exists(FONT_XBLD)
    if not have:
        have = _try_extract_from_ttc()
    if have:
        fm.fontManager.addfont(FONT_MED)
        fm.fontManager.addfont(FONT_XBLD)
        return fm.FontProperties(fname=FONT_MED), fm.FontProperties(fname=FONT_XBLD)
    # Fallback: default font (CJK glyphs may be missing but the card still draws).
    sys.stderr.write(
        "card.py: skill fonts not found and no usable system TTC -- falling back "
        "to matplotlib default font (CJK text may not render).\n")
    return fm.FontProperties(), fm.FontProperties(weight='bold')


prop, bold_prop = _resolve_fonts() if _MPL_ERR is None else (None, None)

# -- sibling carriers of this skill (imported by file path, carryover.py's
# idiom). Both are LOAD-BEARING for what the card is allowed to claim:
#   calorie_gate.py  the countable half of the G6 safety gate. The card's
#                    target is the number the owner eats to, so the floor has
#                    to bind HERE and not only in a consult transcript.
#   kitmode.py       declared kit shape vs installed kit shape. v0.1 printed
#                    its verdict to stdout and nothing read it, so 0.11.0 put
#                    it on the card. 0.36.0 took it OFF the card again: it is a
#                    maintenance signal with no owner action, so it goes to
#                    stderr as one KIT_SHAPE line the agent reads
#                    (report_kit_shape), never to the owner.
# Absent/broken sibling -> the card still renders, and the NOTICE says the
# check could not run. A card that silently drops its own guard is the defect
# this release is about.
def _sibling(name):
    import importlib.util
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), name + '.py')
    # NO BYTECODE. These modules live INSIDE the installed skill directory, and
    # a __pycache__ written there is packaging residue in the instance: it is
    # what compat-lint C4b refuses in a pack tree and what the installer's
    # content-drift guard would then report as live-only content. kit_life is
    # imported from database/ and has no such problem; these two do.
    _prev = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec = importlib.util.spec_from_file_location('dietstatus_' + name, path)
        if spec is None or spec.loader is None:
            return None
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    except Exception:            # noqa: BLE001 -- see NOTICE contract above
        return None
    finally:
        sys.dont_write_bytecode = _prev


calorie_gate = _sibling('calorie_gate')
kitmode      = _sibling('kitmode')

# -- Body stats / targets model (kit_life.py core; no local reimplementation) --
load_body_stats     = life.load_body_stats
compute_targets     = life.compute_targets
compute_macro_goals = life.compute_macro_goals

# -- Effective-goal single source of truth (eff_goal double-count guard) -------
# eff_goal = the FINAL daily intake target = base_goal + today's workout burn.
# The burn must be folded in EXACTLY ONCE. This one function is the only place
# the card derives eff_goal; every consumer (formula line, bar, remaining) reads
# its result. It makes a burn re-add structurally impossible:
#   * `intake.goal` may be either the base goal (burn-exclusive) or the already-
#     effective goal (burn-inclusive). Callers historically inject the effective
#     goal (the body-state context line), so blindly adding burn double-counted.
#   * We disambiguate by an explicit `intake.goal_kind` in {'base','effective'};
#     when absent we AUTO-DETECT: a passed goal that already reaches the stats-
#     derived effective target (within EPS) is treated as effective, so burn is
#     NOT re-added.
#   * A hard post-condition then asserts eff_goal never exceeds base+burn. Any
#     path that re-adds burn to an already-effective value trips this and raises,
#     so the wrong number fails loudly in tests instead of shipping silently.
GOAL_EPS = 1.0  # kcal tolerance for rounding when comparing goals


def safety_notices(gate_report):
    """The lines the card must carry because a machine, not a reader, found
    them. Empty list = everything checked and everything cleared.

    G6 ONLY. The kit-shape check used to share this surface (0.11.0); since
    0.36.0 it does not -- see kit_shape_signal(). A shape mismatch is a
    maintenance signal with no owner action, so it never reaches the card or
    any owner-facing text. NOT fatal: a card that refuses to draw because of
    a note is worse than the note.
    """
    out = []

    # -- G6 (Part A) -------------------------------------------------------
    v = (gate_report or {}).get('verdict')
    hoist = (gate_report or {}).get('hoist') or 0
    if calorie_gate is None:
        out.append('안전 게이트 미탑재 -- calorie_gate.py 를 못 읽어 하한/상한 '
                   '확인을 못 했습니다.')
    elif v is None:
        out.append('안전 게이트 실행 실패 -- 이 목표는 하한/상한 확인이 안 된 '
                   '숫자입니다.')
    elif v.get('verdict') == 'unverifiable':
        miss = ', '.join(v.get('limits_missing') or []) or '입력'
        out.append('안전 하한/상한을 확인 못 했습니다 (%s) -- 이 목표는 안전 '
                   '확인이 안 된 숫자입니다.' % miss)
    elif v.get('verdict') == 'refuse':
        line = calorie_gate.why_line(v)
        if hoist:
            line = '%s (%+d kcal)' % (line, hoist)
        out.append('안전 게이트: %s' % line)

    return out


KIT_SHAPE_TAG = 'KIT_SHAPE'


def kit_shape_signal():
    """kitmode's verdict, for the AGENT, never for the owner (0.36.0, PM
    ruling after the 2026-10-08 live card showed "킷 모양 불일치: 선언 71 !=
    설치 72"). Returns None when there is nothing to report (linked /
    standalone / migratable, or the kitmode sibling is absent), else a dict
    {verdict, declared, installed} with verdict in mismatch / undeclared /
    error (resolve raised). kitmode's verdict logic and its mode/enforced
    fields are untouched; only the SURFACE moved."""
    if kitmode is None:
        return None
    try:
        km = kitmode.resolve()
    except Exception:            # noqa: BLE001 -- a broken check is a signal
        km = None
    if km is None:
        return {'verdict': 'error', 'declared': None, 'installed': None}
    if km.get('verdict') in ('mismatch', 'undeclared'):
        return {'verdict': km['verdict'],
                'declared': km.get('declared_schema'),
                'installed': km.get('installed_schema')}
    return None


def report_kit_shape(stream=None):
    """Print the one machine line to stderr when kitmode has something to say:
        KIT_SHAPE\t<verdict>\tdeclared=<n>\tinstalled=<n>
    (`-` for an unknown number). The agent reads it; it is never drawn on the
    card and never relayed to the owner (diet-status SKILL.md). Returns the
    line written, or None."""
    sig = kit_shape_signal()
    if sig is None:
        return None
    fmt = lambda v: '-' if v is None else str(v)
    line = '%s\t%s\tdeclared=%s\tinstalled=%s' % (
        KIT_SHAPE_TAG, sig['verdict'], fmt(sig['declared']),
        fmt(sig['installed']))
    try:
        (stream or sys.stderr).write(line + '\n')
    except Exception:            # noqa: BLE001 -- a signal never fails a card
        pass
    return line


def burn_unrecorded_line(workouts):
    """One line when a logged workout carries no burn (kit 064: kcal NULL =
    not entered, never 0). Owner ruling 2026-09-30: such a day keeps the BASE
    target -- no burn is guessed or restored from memos -- and the card says
    in one line that the workout is not counted. A day with no workout at all
    gets no line: nothing is missing there. None = nothing to say."""
    missing = [w for w in (workouts or []) if w.get('kcal') is None]
    if not missing:
        return None
    if len(missing) == len(workouts):
        return '운동 소모 칼로리가 기록되지 않아 목표에 넣지 않았어요.'
    return ('운동 %d건은 소모 칼로리가 기록되지 않아 목표에 넣지 않았어요.'
            % len(missing))


_GATE_AUTO = object()        # "run the gate" -- distinct from "gate says nothing"


def safety_verdict(targets, stats, base_goal):
    """The G6 countable limbs, run on the numbers this card is about to show.

    Returns the verdict dict, or None when the carrier is absent. The three
    inputs are the kit's own: `targets` came out of compute_targets and `stats`
    out of load_body_stats, so the gate judges the SAME arithmetic the card
    prints rather than a re-derivation of it."""
    if calorie_gate is None:
        return None
    try:
        return calorie_gate.evaluate(
            deficit_kcal=targets.get('deficit'),
            base_target_kcal=base_goal,
            bmr_kcal=targets.get('bmr'),
            sex=stats.get('sex'))
    except Exception:            # noqa: BLE001 -- a broken gate is a NOTICE
        return None


def resolve_goal(intake, burn_amt, targets, carry_kcal=0, stats=None,
                 gate=_GATE_AUTO, report=None):
    """Single source of truth for (base_goal, eff_goal).

    intake    : the card's intake_kcal dict (may carry 'goal' and 'goal_kind').
    burn_amt  : today's workout burn kcal (>= 0), counted at most once.
    targets   : compute_targets(stats, exercise_kcal=burn_amt) output; carries
                the stats-derived base_goal and eff_goal for this same burn.
    carry_kcal: kcal carried over from earlier days this week (>= 0). Comes
                from carryover.py, which only ever produces a non-negative
                number -- so this argument can only LOWER the target, never
                raise it. Applied to base AND effective together, so the
                burn-fold post-condition below still holds exactly.
    stats     : load_body_stats() output; the gate needs `sex` off it. None ->
                the sex-floor limb reports `unverifiable`, which is a verdict.
    gate      : the G6 verdict to apply. Default runs it. Pass an already-
                computed verdict to avoid a second database read; pass None
                ONLY to test the ungated arithmetic -- nothing in the render
                path does, because a gate a caller can switch off by omission
                is the prose gate this release replaced.
    report    : optional dict; filled with {'verdict', 'hoist'} so the caller
                can SAY what the gate did. An out-parameter rather than a
                third return value on purpose -- the (base, eff) contract is
                asserted by name in three suites, and a silent arity change is
                how a post-condition stops being checked.

    Returns (base_goal, eff_goal) as rounded ints. eff_goal = base_goal + burn,
    guaranteed by an assertion so no caller can double-count.

    WHY THE CARRY LANDS HERE and not at a call site: this function is already
    the single place the card's target is decided, and the bar, the remaining
    number and the macro goals all read its result. Moving the target anywhere
    else would move the line without moving the bar -- which is precisely the
    failure the carry-over is supposed to make visible.
    """
    burn = round(burn_amt or 0)
    stats_base = targets['base_goal']
    stats_eff = targets['eff_goal']  # == stats_base + burn by construction

    injected = intake.get('goal')
    if injected is None:
        # no override -> use stats model directly (already single-counted).
        base_goal, eff_goal = stats_base, stats_eff
    else:
        injected = round(injected)
        kind = (intake.get('goal_kind') or '').strip().lower()
        if kind == 'effective':
            is_effective = True
        elif kind == 'base':
            is_effective = False
        else:
            # auto-detect: an injected goal that already reaches the effective
            # target (within EPS) is burn-inclusive; do not add burn again.
            is_effective = burn > 0 and injected >= stats_eff - GOAL_EPS
        if is_effective:
            eff_goal = injected
            base_goal = injected - burn
        else:
            base_goal = injected
            eff_goal = injected + burn

    # The carry comes off both halves, so `eff_goal - base_goal` stays exactly
    # `burn` and the assertion below keeps testing what it was written to test.
    # Clamped at 0: a target below zero is not a smaller target, it is a broken
    # card, and carryover.py already floors its own output.
    carry = max(0, round(carry_kcal or 0))
    if carry:
        base_goal = max(0, base_goal - carry)
        eff_goal = max(burn, eff_goal - carry)

    # -- G6 floor, applied LAST and unconditionally (0.11.0) ----------------
    # The clamp above stops at zero, and zero is not the floor: the inviolable
    # `calorie_floor` row is. Until this release the only thing standing
    # between the carry and a target of nothing was that sentence in a file
    # the pack never delivered, so the floor binds here, in the one function
    # that decides the target. The hoist moves base AND effective by the same
    # amount, so `eff_goal - base_goal == burn` still holds exactly and the
    # post-condition below keeps testing what it was written to test.
    #
    # A verdict of `unverifiable` -- which is what a freshly minted instance
    # gets, because nothing seeds the two safety rows -- moves NOTHING. It
    # cannot: a floor that could not be read is not a floor to hoist to. The
    # card says so instead (safety_notices), which is the whole point.
    if gate is _GATE_AUTO:
        gate = safety_verdict(targets, stats or {}, base_goal)
    hoist = 0
    if gate is not None and calorie_gate is not None:
        permitted = calorie_gate.permitted_base(
            gate, base_goal, targets.get('deficit'))
        if permitted is not None and permitted > base_goal:
            hoist = permitted - base_goal
            eff_goal += hoist
            base_goal = permitted
    if report is not None:
        report['verdict'] = gate
        report['hoist'] = round(hoist)

    base_goal = round(base_goal)
    eff_goal = round(eff_goal)
    # structural post-condition: burn folded in exactly once. A re-add would push
    # eff_goal past base+burn and trip this -- loud failure, never a silent card.
    assert eff_goal <= base_goal + burn + GOAL_EPS, (
        "eff_goal double-count detected: eff_goal=%d exceeds base_goal=%d + "
        "burn=%d (a burn re-add slipped through)" % (eff_goal, base_goal, burn))
    return base_goal, eff_goal

# Korean weekday (Mon=0 .. Sun=6)
_WDAY_KO = ['월', '화', '수', '목', '금', '토', '일']


def _resolve_date(date_in):
    """From input date build the kit_life.db lookup 'YYYY-MM-DD' and the display
    'YYYY.MM.DD <weekday>'. 'YYYY-MM-DD' -> that date; otherwise -> today."""
    iso = None
    if date_in:
        m = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', date_in.strip())
        if m:
            iso = date_in.strip()
    if iso is None:
        iso = datetime.date.today().isoformat()
    y, mo, da = iso.split('-')
    wd = datetime.date(int(y), int(mo), int(da)).weekday()
    display = f"{y}.{mo}.{da} {_WDAY_KO[wd]}"
    if date_in and not re.match(r'^\d{4}-\d{2}-\d{2}$', date_in.strip()):
        display = date_in
    return iso, display


def load_from_life_db(iso_date):
    """Read that date's meals+workouts as a card dict fragment (via kit_life).
    Net-carb opt-in ON -> each meal also gets its `fiber` (delta 3)."""
    res = life.load_card_data(iso_date)
    if _net_carb_config():
        _attach_fiber(iso_date, res.get('meals') or [])
    return res


# -- net carb (DGN-336/700 delta 3; framework D-C approved as-is) ------------------
# 탄 = total carb - fiber. OPT-IN: config `diet_net_carb` (kit_life.sh
# config-set diet_net_carb=1), default = TOTAL carbs (owner LOCKED -- no silent
# switch of what the printed number means). A read failure is OFF. When ON the
# header says 순탄수 so the meaning of the number is on the card. kcal does not
# move with the toggle: the kit's kcal is generated net of fiber either way.
_NET_ON = ('1', 'true', 'on', 'yes', 'y')


def _net_carb_config():
    try:
        v = life.get_config('diet_net_carb')
    except Exception:            # noqa: BLE001 -- read-fail = OFF
        return False
    return str(v).strip().lower() in _NET_ON if v is not None else False


def _attach_fiber(iso_date, meals):
    """Per-meal fiber, when the kit's load_card_data does not carry it yet
    (the core fold of fiber into load_card_data is the kit's lane). Read off
    the kit's own meal-measure expression, in load_card_data's row order;
    any mismatch or failure leaves the meals untouched -> net carb stays OFF."""
    if not meals or all('fiber' in m for m in meals):
        return
    try:
        conn = life.get_conn()
        try:
            rows = conn.execute(
                "SELECT " + (life._MEAL_M % 'fiber') + " FROM block b "
                "WHERE b.settled_by = 'meal-record' AND b.date = ? "
                "ORDER BY b.id;", (iso_date,)).fetchall()
        finally:
            conn.close()
    except Exception:            # noqa: BLE001 -- read-fail = OFF
        return
    if len(rows) != len(meals):
        return
    for m, (fib,) in zip(meals, rows):
        m.setdefault('fiber', float(fib or 0))


def net_carb_on(d, meals):
    """Net carb is shown only when opted in AND every food row carries its
    fiber -- a half-net table would be two meanings in one column."""
    if 'net_carb' in d:
        want = bool(d.get('net_carb'))
    else:
        want = _net_carb_config()
    food = [m for m in meals if m.get('type') != '운동']
    return bool(want and food and all('fiber' in m for m in food))


# -- Colors -- every value is a canonical slot, never a card-local hex --------
# Framework >= 2.6.0: card_palette() (DGN-768 S2). the framework's DGN-700 landing hold
# (YYDRDY34) was exactly the old block's theme('card-dark') hardcode plus the
# raw-hex table colours, so on a framework that has the resolver the card
# reads ONLY its slots; the few hues the 11-slot palette has no name for
# (burn orange, sugar) are DERIVED from BRAND through tune_accent against this
# palette's own surface -- the same derivation the palette itself is pinned to.
# Older framework: the legacy card-dark colours, exactly as 0.26.0 drew them.
def _tuned(brand_key, fallback):
    try:
        return _tokens.tune_accent(_BRAND[brand_key], _PAL['surface']) or fallback
    except Exception:            # noqa: BLE001
        return fallback


if _PAL is not None:
    BG          = _PAL['bg']
    INK         = _PAL['text']
    INK_SOFT    = _PAL['muted']
    INK_VALUE   = _PAL['text']
    TRACK_BASE  = _PAL['border']
    BAR_EXERCISE_SEG = _PAL['surface']
    INTAKE_FILL = _PAL['red']
    SEP_LINE    = _PAL['border']
    WARN        = _PAL['yellow']       # AA-checked warning amber
    BURN_ACCENT = _tuned('orange', _PAL['yellow'])
    # 당: its own hue so it never reads as the carb column (D-B). The ticket's
    # card-local #F0A868 is gone; coral tuned to this surface replaces it.
    SUGAR_COLOR = _tuned('coral', _PAL['red'])
    # text drawn ON the intake fill once the bar is full (the "초과" label)
    ON_FILL     = _PAL['bg']
    MACRO_COLORS = {'단백질': _PAL['accent'], '탄수화물': _PAL['yellow'],
                    '지방': _PAL['green']}
    MEAL_COLORS = {'아침': _PAL['red'], '점심': _PAL['accent'],
                   '저녁': _PAL['green'], '간식': _PAL['yellow'],
                   '운동': BURN_ACCENT}
    FALLBACK_INK = _PAL['muted']
else:
    # Values are pixel-identical to the former hardcoded block by construction
    # (Layer A / card-dark was canonicalized from this palette, DGN-376 T1).
    BG          = _T['bg']
    INK         = _T['text']
    INK_SOFT    = _T['muted']
    INK_VALUE   = _BRAND['ink-value']
    TRACK_BASE  = _BRAND['navy-track']
    BAR_EXERCISE_SEG = _BRAND['navy-seg']
    BURN_ACCENT = _T['orange']
    INTAKE_FILL = _T['red']
    SEP_LINE    = _BRAND['navy-line']
    # NOTICE band (0.11.0). Reuses the existing warn token rather than minting
    # a colour -- design_tokens.py is the canon and a card-local hex would be a
    # second one.
    WARN        = _T['orange']
    SUGAR_COLOR = None                 # legacy: sugar wears the carb colour
    ON_FILL     = INK_VALUE
    MACRO_COLORS = {
        '단백질':   _T['accent'],   # teal
        '탄수화물': _T['yellow'],   # amber
        '지방':     _BRAND['mint'],
    }
    MEAL_COLORS = {
        '아침': _T['red'],          # coral
        '점심': _T['accent'],       # teal
        '저녁': _BRAND['mint'],
        '간식': _T['yellow'],       # amber
        '운동': _T['orange'],
    }
    FALLBACK_INK = _T['muted']

# Planned-meal rendering: a meal row that is not yet eaten is written for
# real but tagged in its name string. Everywhere this tag shows up (row text,
# intake bar, macro bars) gets rendered at reduced alpha so the user can tell
# planned vs actual at a glance -- no schema change, no separate "status"
# field. Any producer that writes planned meals uses this same tag contract.
PLANNED_TAG = '(예정)'
PLANNED_ALPHA = 0.42


def day_goals(d):
    """The day's target, derived ONCE: (burn, carry, gate, base/eff goal, macro
    goals). draw_card, projection() and suggest.py all read this, so the number
    the model speaks is the number the card draws -- same carry, same G6 floor.

    daily total target = BMR + NEAT - deficit. NO workout burn (owner
    2026-10-08 07:09): lifting 3-6x/week already sits inside the activity
    band, and watch kcal never sets or tops up the food target -- cardio watch
    kcal is reference only. The day's burn still rides the card as a
    reference label (`burn_amt`), never as a term of the target."""
    burn     = d.get('burn_kcal', None)
    intake   = d.get('intake_kcal', {})
    has_burn = bool(burn and burn.get('current', 0) > 0)
    burn_amt = burn['current'] if has_burn else 0
    stats    = load_body_stats()
    t        = compute_targets(stats, exercise_kcal=0)
    # CARRY-OVER (v0.1). The number is derived by carryover.py from the same
    # measure rows the weekly criterion is judged on; the card neither computes
    # it nor guesses one. Absent key -> 0 -> the card is byte-identical to its
    # pre-carry self, so a kit with no calorie rule sees no change at all.
    #
    # TOP-LEVEL key, and that placement is load-bearing: __main__ only
    # auto-aggregates from kit_life.db when BOTH 'meals' and 'intake_kcal' are
    # absent, so nesting the carry under 'intake_kcal' would silently suppress
    # the day's own meal load and render an empty card. Measured, not reasoned
    # -- the first wiring did exactly that.
    carry_kcal = max(0, round(d.get('carry_kcal') or 0))
    # single source of truth: burn is folded into eff_goal exactly once here,
    # and the G6 floor binds here too -- `gate_report` is how the card learns
    # what the gate did so it can print it instead of swallowing it.
    gate_report = {}
    base_goal, eff_goal = resolve_goal(intake, 0, t, carry_kcal, stats,
                                       report=gate_report)
    g = compute_macro_goals(eff_goal, stats)
    return {'has_burn': has_burn, 'burn_amt': burn_amt, 'stats': stats,
            'targets': t, 'carry_kcal': carry_kcal, 'base_goal': base_goal,
            'eff_goal': eff_goal, 'macro_goals': g, 'gate_report': gate_report}


def load_day(data):
    """The card's input dict with the kit auto-aggregate filled in -- the same
    rule __main__ applies before drawing (both 'meals' and 'intake_kcal'
    absent -> read that date from kit_life.db). Returns (data, iso_date)."""
    data = dict(data or {})
    iso_date, display_date = _resolve_date(data.get('date'))
    if 'meals' not in data and 'intake_kcal' not in data:
        for k, v in load_from_life_db(iso_date).items():
            data.setdefault(k, v)
        data['date'] = display_date
    return data, iso_date


def day_state(d):
    """Where the day stands, as numbers the model may speak verbatim:
    target / intake / remaining for kcal and protein. Same day_goals() the
    card draws from, so `remaining_kcal` here IS the card's 남은/초과 label."""
    dg = day_goals(d)
    report_kit_shape()           # agent-side only; never in the state below
    eff = dg['eff_goal']
    kcal = float((d.get('intake_kcal') or {}).get('current') or 0)
    prot = d.get('protein') or {}
    p_cur = float(prot.get('current') or 0)
    p_goal = float(prot.get('goal') or dg['macro_goals']['protein'])
    return {'eff_goal': eff, 'base_goal': dg['base_goal'],
            'carry_kcal': dg['carry_kcal'],
            'intake_kcal': round(kcal), 'remaining_kcal': round(eff - kcal),
            'protein_g': round(p_cur), 'protein_goal_g': round(p_goal),
            'remaining_protein_g': round(p_goal - p_cur),
            'fat_g': round(float((d.get('fat') or {}).get('current') or 0)),
            'carbs_g': round(float((d.get('carbs') or {}).get('current') or 0)),
            'safety_notices': safety_notices(dg['gate_report'])}


_NUTR = ('kcal', 'protein', 'fat', 'carbs')


def resolve_candidate(cand):
    """A food the owner is weighing -> its numbers, from a SOURCE, never from
    the model's head. Order: numbers passed in (the model already has them from
    a lookup this turn) > the kit's shared food cache scaled to `grams` (the
    lookup meal-capture itself uses) > the owner's own logged serving of that
    name (suggest.py history). Nothing found -> found False and no numbers:
    the trade-off line is then not spoken, never estimated."""
    cand = dict(cand or {})
    name = str(cand.get('name') or '').strip()
    grams = cand.get('grams')
    out = {'name': name, 'grams': grams, 'found': False, 'basis': None}
    if cand.get('kcal') is not None:
        out.update(found=True, basis='given')
        for k in _NUTR:
            out[k] = float(cand.get(k) or 0)
        return out
    if not name:
        return out
    try:
        fc = life.foodcache_lookup(name, grams=grams)
    except Exception:            # noqa: BLE001 -- cache lane down = not found
        fc = {'found': False}
    if fc.get('found') and fc.get('kcal') is not None:
        scaled = grams is None or bool(fc.get('base_grams'))
        out.update(found=True, basis='food_cache' if scaled else 'food_cache_unscaled',
                   grams=fc.get('grams'), kcal=float(fc.get('kcal') or 0),
                   protein=float(fc.get('protein') or 0),
                   fat=float(fc.get('fat') or 0),
                   carbs=float(fc.get('carb') or 0))
        return out
    try:
        sg = _sibling('suggest')
        h = sg.history_item(name) if sg is not None else None
    except Exception:            # noqa: BLE001
        h = None
    if h:
        out.update(found=True, basis='history', kcal=float(h['kcal']),
                   protein=float(h['protein']), fat=float(h['fat']),
                   carbs=float(h['carbs']))
    return out


def projection(state, item):
    """{kcal_after, protein_after, over_kcal, ...} for one resolved candidate
    on top of day_state(). Pure arithmetic on engine numbers -- this is the
    sum the model used to do in its head ("목살 220g이면 ..."). `line` is the
    one trade-off sentence, kcal then protein (the fixed order), with the
    "참고로" overshoot clause only when the item crosses the target."""
    if not item.get('found'):
        return {'available': False, 'name': item.get('name'),
                'line': None}
    kcal_after = round(state['intake_kcal'] + item['kcal'])
    protein_after = round(state['protein_g'] + item['protein'])
    over = max(0, kcal_after - state['eff_goal'])
    label = item['name']
    if item.get('grams'):
        label = '%s %gg' % (label, float(item['grams']))
    line = '%s이면 칼로리 %skcal, 단백질 %dg까지 올라가요.' % (
        label, format(kcal_after, ','), protein_after)
    if over:
        line += ' 참고로 목표보다 %skcal 넘어요.' % format(over, ',')
    return {'available': True, 'name': item['name'], 'grams': item.get('grams'),
            'basis': item['basis'],
            'item_kcal': round(item['kcal']), 'item_protein_g': round(item['protein']),
            'kcal_after': kcal_after, 'protein_after': protein_after,
            'over_kcal': over,
            'remaining_kcal_after': state['eff_goal'] - kcal_after,
            'remaining_protein_after': state['protein_goal_g'] - protein_after,
            'fat_after': round(state['fat_g'] + item.get('fat', 0)),
            'carbs_after': round(state['carbs_g'] + item.get('carbs', 0)),
            'line': line}


def draw_card(d: dict, out_path: str):
    date    = d.get('date', '')
    intake  = d.get('intake_kcal', {})
    protein = d.get('protein', {})
    carbs   = d.get('carbs', {})
    fat     = d.get('fat', {})
    burn     = d.get('burn_kcal', None)
    workouts = d.get('workouts', [])
    meals    = d.get('meals', [])
    # prepend workout rows (type='운동') at top of meal list for display
    if workouts:
        wo_entries = []
        for w in workouts:
            wtype = w.get('type', '')
            wname = w.get('name', '')
            label = f"{wtype} ({wname})" if wtype and wname else (wtype or wname or '운동')
            wkcal = w.get('kcal')
            entry = {'type': '운동', 'name': label}
            if wkcal:
                entry['kcal'] = -float(wkcal)  # burn shown as a negative row (owner-confirmed 2026-07-30)
            wo_entries.append(entry)
        meals = wo_entries + meals

    # -- net carb (delta 3): opt-in, default = total carbs (owner LOCKED).
    # Display only: kcal is net of fiber in the kit either way (generated).
    net_carb = net_carb_on(d, meals)
    if net_carb:
        fib = sum(float(m.get('fiber') or 0) for m in meals)
        carbs = dict(carbs, current=max(0.0, float(carbs.get('current') or 0) - fib))

    # -- daily total target: day_goals() is the one derivation, shared with
    # the projection mode and suggest.py so a spoken number can never drift
    # from the number drawn on the card.
    dg = day_goals(d)
    has_burn, burn_amt = dg['has_burn'], dg['burn_amt']
    t, carry_kcal = dg['targets'], dg['carry_kcal']
    base_goal, eff_goal, g = dg['base_goal'], dg['eff_goal'], dg['macro_goals']
    notices = safety_notices(dg['gate_report'])
    report_kit_shape()           # kit shape: stderr for the agent, not the band
    # (text, colour) rows for the bottom band: safety first, then the plain
    # "burn not counted" fact, which is information, not a warning.
    band = [('[주의] ' + n, WARN) for n in notices]
    # The "burn not entered, not counted" line is gone with the burn term
    # itself (owner 2026-10-08 07:09): no burn ever enters the target, so a
    # missing one changes nothing and saying so would read as if it should.

    current_intake = intake.get('current', 0)

    # -- diet-plan: split the not-yet-eaten (예정) portion out of today's
    # totals, so the intake bar and macro bars can render it dimmed. --
    def _is_planned(m):
        return str(m.get('name', '')).rstrip().endswith(PLANNED_TAG)
    planned_kcal    = sum(float(m.get('kcal') or 0) for m in meals if _is_planned(m))
    planned_protein = sum(float(m.get('protein') or 0) for m in meals if _is_planned(m))
    def _carb(m):
        c = float(m.get('carbs') or 0)
        return max(0.0, c - float(m.get('fiber') or 0)) if net_carb else c
    planned_carbs   = sum(_carb(m) for m in meals if _is_planned(m))
    planned_fat     = sum(float(m.get('fat') or 0) for m in meals if _is_planned(m))

    # The carry rides the formula line as its own term. It is the RESULT half
    # of the touchpoint pair: the brief says WHY the number moved, the card
    # shows THAT it moved and the bar follows it. Naming the term is what keeps
    # a shrunken target from reading as an error.
    formula = (f"기초 {t['bmr']} + 활동 {t['neat']} - 적자 {t['deficit']}"
               + (f" - 이월 {carry_kcal}" if carry_kcal else ''))

    # -- figure (height sized to content) --
    n_meals     = len(meals)
    fig_w       = 13.0

    _bar_top_in  = 2.05
    _bar_h_in    = 0.62
    _macro_top   = _bar_top_in + _bar_h_in + 1.25
    _mbar_top    = _macro_top + 0.55
    _mbar_h_in   = 0.22
    _sep_top_in  = _mbar_top + _mbar_h_in + 1.05
    _meals_start = _sep_top_in + 0.78
    _meal_row_in = 0.85
    _last_row_in = _meals_start + (max(n_meals, 1) - 1) * _meal_row_in if n_meals else _sep_top_in
    BOTTOM_PAD_IN = 0.55
    # NOTICE band. Grown at the BOTTOM and nowhere else: every other element is
    # positioned in absolute inches from the top and converted through y() at
    # draw time, so a taller figure moves none of them by a pixel. That is what
    # makes this addition safe to make on a card whose layout is pinned by
    # measured tests -- a notice cannot push the bar off the number it belongs
    # to.
    NOTICE_ROW_IN = 0.40
    # 0.62 of clearance before the first notice: a meal row is 0.85in tall and
    # _last_row_in is its CENTRE, so anything under ~0.45 overprints the row.
    NOTICE_GAP_IN = 0.62
    notice_in = ((NOTICE_ROW_IN * (len(band) - 1) + NOTICE_GAP_IN + 0.25)
                 if band else 0.0)
    fig_h = _last_row_in + notice_in + BOTTOM_PAD_IN
    fig = plt.figure(figsize=(fig_w, fig_h), facecolor=BG)
    fig.patch.set_facecolor(BG)

    L, R = 0.045, 0.955
    H = fig_h

    def y(px_from_top):
        return 1.0 - (px_from_top / H)

    # -- header: title + date --
    fig.text(L, y(0.55), '오늘 식단 현황', color=INK,
             fontsize=30, fontproperties=bold_prop, va='center', ha='left')
    if date:
        fig.text(0.34, y(0.55), date, color=INK_SOFT,
                 fontsize=23, fontproperties=bold_prop, va='center', ha='left')

    # -- recommended intake formula line --
    fig.text(L, y(1.55),
             f"권장 섭취 칼로리: {eff_goal}kcal = {formula}",
             color=INK, fontsize=18, fontproperties=prop, va='center', ha='left')

    # -- intake bar (exercise segment split) --
    bar_left   = L
    bar_right  = R
    bar_width  = bar_right - bar_left
    bar_top_in = 2.05
    bar_h_in   = 0.62
    bar_y0 = y(bar_top_in + bar_h_in)
    bar_h  = bar_h_in / H

    eff = max(eff_goal, 1)
    base_frac = min(base_goal / eff, 1.0)
    burn_frac = max(0.0, 1.0 - base_frac)
    intake_frac = min(current_intake / eff, 1.0)

    fig.patches.append(plt.Rectangle(
        (bar_left, bar_y0), bar_width * base_frac, bar_h,
        transform=fig.transFigure, facecolor=TRACK_BASE, edgecolor='none', zorder=1))
    if burn_frac > 0:
        fig.patches.append(plt.Rectangle(
            (bar_left + bar_width * base_frac, bar_y0), bar_width * burn_frac, bar_h,
            transform=fig.transFigure, facecolor=BAR_EXERCISE_SEG,
            edgecolor=TRACK_BASE if _PAL is not None else 'none', zorder=1))
    actual_intake = max(0.0, current_intake - planned_kcal)
    actual_frac = min(actual_intake / eff, 1.0)
    fig.patches.append(plt.Rectangle(
        (bar_left, bar_y0), bar_width * actual_frac, bar_h,
        transform=fig.transFigure, facecolor=INTAKE_FILL, edgecolor='none', zorder=2))
    if intake_frac > actual_frac:
        fig.patches.append(plt.Rectangle(
            (bar_left + bar_width * actual_frac, bar_y0),
            bar_width * (intake_frac - actual_frac), bar_h,
            transform=fig.transFigure, facecolor=INTAKE_FILL, alpha=PLANNED_ALPHA,
            edgecolor='none', zorder=2))

    # -- remaining / over label --
    remaining = eff_goal - current_intake
    if remaining > 0:
        remain_txt = f"남은 {remaining:,.0f} kcal"
    else:
        remain_txt = f"초과 {abs(remaining):,.0f} kcal"
    remain_start = bar_left + bar_width * intake_frac
    label_x = (remain_start + bar_right) / 2
    label_x = min(max(label_x, bar_left + 0.03), bar_right - 0.03)
    label_ha = 'center'
    # A short remainder (or none) used to centre the label on the bar's last
    # sliver and push "초과 842 kcal" past the right edge. Right-anchor it
    # inside the bar instead once the centred text would not fit (~0.16 of
    # the width at this size).
    if bar_right - remain_start < 0.16:
        label_x, label_ha = bar_right - 0.012, 'right'
    remain_y = bar_y0 + bar_h / 2
    fig.text(label_x, remain_y, remain_txt,
             color=ON_FILL if intake_frac >= 1.0 else INK_VALUE, fontsize=18,
             fontproperties=bold_prop, va='center', ha=label_ha, zorder=3)

    # -- labels under bar: intake (left), burn (right) --
    label_y = y(bar_top_in + bar_h_in + 0.45)
    fig.text(bar_left, label_y, f"섭취 {current_intake:.0f}", color=INK,
             fontsize=22, fontproperties=bold_prop, va='center', ha='left')
    if has_burn:
        detail = burn.get('detail') or '운동'
        # reference only: the burn is not in the target (owner 2026-10-08)
        fig.text(bar_right, label_y, f"{detail} 소모 {round(burn_amt)} (참고)",
                 color=BURN_ACCENT, fontsize=20, fontproperties=bold_prop,
                 va='center', ha='right')

    # -- macro 3 columns --
    macro_top_in = bar_top_in + bar_h_in + 1.25
    macros = [
        ('단백질',   protein.get('current', 0), protein.get('goal') or g['protein'], None, planned_protein),
        ('순탄수' if net_carb else '탄수화물', carbs.get('current', 0),
         carbs.get('goal') or g['carb'], carbs.get('sugar'), planned_carbs),
        ('지방',     fat.get('current', 0),     fat.get('goal')     or g['fat'], None, planned_fat),
    ]
    col_w = (R - L) / 3
    centers = [L + col_w * (i + 0.5) for i in range(3)]
    col_bar_w = col_w * 0.72

    name_y = y(macro_top_in)
    mbar_top_in = macro_top_in + 0.55
    mbar_h_in   = 0.22
    mbar_y0 = y(mbar_top_in + mbar_h_in)
    mbar_h  = mbar_h_in / H
    mval_y  = y(mbar_top_in + mbar_h_in + 0.55)
    msug_y  = y(mbar_top_in + mbar_h_in + 0.85)

    for cx, (mname, mcur, mgoal, msugar, mplanned) in zip(centers, macros):
        mcolor = MACRO_COLORS.get('탄수화물' if mname == '순탄수' else mname,
                                  FALLBACK_INK)
        fig.text(cx, name_y, mname, color=INK, fontsize=22,
                 fontproperties=bold_prop, va='center', ha='center')
        mb_left = cx - col_bar_w / 2
        frac = min(mcur / mgoal, 1.0) if mgoal else 0.0
        actual_mval = max(0.0, mcur - mplanned)
        actual_mfrac = min(actual_mval / mgoal, 1.0) if mgoal else 0.0
        fig.patches.append(plt.Rectangle(
            (mb_left, mbar_y0), col_bar_w, mbar_h,
            transform=fig.transFigure, facecolor=TRACK_BASE, edgecolor='none', zorder=1))
        fig.patches.append(plt.Rectangle(
            (mb_left, mbar_y0), col_bar_w * actual_mfrac, mbar_h,
            transform=fig.transFigure, facecolor=mcolor, edgecolor='none', zorder=2))
        if frac > actual_mfrac:
            fig.patches.append(plt.Rectangle(
                (mb_left + col_bar_w * actual_mfrac, mbar_y0),
                col_bar_w * (frac - actual_mfrac), mbar_h,
                transform=fig.transFigure, facecolor=mcolor, alpha=PLANNED_ALPHA,
                edgecolor='none', zorder=2))
        fig.text(cx, mval_y, f"{mcur:.0f} / {mgoal:.0f} g", color=INK_VALUE,
                 fontsize=21, fontproperties=bold_prop, va='center', ha='center')
        if msugar is not None:
            fig.text(cx, msug_y, f"당 {msugar:.0f}g", color=SUGAR_COLOR or mcolor,
                     fontsize=16, fontproperties=bold_prop, va='center', ha='center')

    # -- separator --
    sep_top_in = mbar_top_in + mbar_h_in + 1.05
    sep_y = y(sep_top_in)
    fig.add_artist(plt.Line2D([L, R], [sep_y, sep_y],
                   color=SEP_LINE, linewidth=1.5, transform=fig.transFigure))

    # -- meal table (DGN-336/700 delta 1, framework-approved D-A 2026-08-06) --
    # 메뉴 | kcal | 탄수 | 당류 | 단백 | 지방. Fixed per-column x anchors so the
    # same value type lands in the same column on every row (owner-confirmed
    # 2026-08-21 -- a single joined, right-aligned string drifted column-to-
    # column depending on digit count). Order/positions per the 2026-07-30
    # design note: 칼로리 · 탄 · 당 · 단 · 지, 0.075 equal spacing, KCAL=0.655.
    # Names truncate before the kcal column (the framework's narrowest-width stress
    # render: zero overlap). Macro values wear their macro colour; a workout
    # row shows its burn as a minus in the burn colour and dashes elsewhere.
    COL_X = {'kcal': 0.655, 'carb': 0.730, 'sugar': 0.805, 'protein': 0.880, 'fat': R}
    COL_HEAD = {'kcal': 'kcal', 'carb': '순탄수' if net_carb else '탄수',
                'sugar': '당류', 'protein': '단백', 'fat': '지방'}
    COL_INK = {'kcal': INK_VALUE, 'carb': MACRO_COLORS['탄수화물'],
               'sugar': SUGAR_COLOR or MACRO_COLORS['탄수화물'],
               'protein': MACRO_COLORS['단백질'], 'fat': MACRO_COLORS['지방']}
    NAME_X = L + 0.075
    name_limit_x = COL_X['kcal'] - 0.060

    def _fit_name(txt, fontsize=21):
        """Truncate to the width before the kcal column. Full-width (CJK)
        chars count 1.0 em, others ~0.55 em."""
        em = fontsize / (72.0 * fig_w)          # one em as a figure fraction
        budget = (name_limit_x - NAME_X) / em
        out, used = [], 0.0
        for ch in txt:
            w = 1.0 if ord(ch) > 0x2500 else 0.55
            if used + w > budget - 1.0:
                out.append('…')
                break
            out.append(ch)
            used += w
        return ''.join(out)

    meal_row_in = 0.85
    head_y = y(sep_top_in + 0.32)
    fig.text(NAME_X, head_y, '메뉴', color=INK_SOFT, fontsize=17,
             fontproperties=bold_prop, va='center', ha='left')
    for key, hx in COL_X.items():
        fig.text(hx, head_y, COL_HEAD[key], color=INK_SOFT, fontsize=17,
                 fontproperties=bold_prop, va='center', ha='right')

    cur_in = sep_top_in + 0.78
    for m in meals:
        mtype = m.get('type', '')
        mname = m.get('name', '')
        mcolor = MEAL_COLORS.get(mtype, FALLBACK_INK)
        ry = y(cur_in)
        is_planned = mname.rstrip().endswith(PLANNED_TAG)
        row_alpha = PLANNED_ALPHA if is_planned else 1.0

        fig.text(L, ry, mtype, color=mcolor, fontsize=21,
                 fontproperties=bold_prop, va='center', ha='left',
                 alpha=row_alpha)
        fig.text(NAME_X, ry, _fit_name(mname), color=INK, fontsize=21,
                 fontproperties=prop, va='center', ha='left',
                 alpha=row_alpha)

        kc = m.get('kcal')
        if mtype == '운동':
            if kc:
                fig.text(COL_X['kcal'], ry, f"{kc:.0f}", color=BURN_ACCENT,
                         fontsize=18, fontproperties=bold_prop, va='center',
                         ha='right')
            for key in ('carb', 'sugar', 'protein', 'fat'):
                fig.text(COL_X[key], ry, '-', color=FALLBACK_INK, fontsize=18,
                         fontproperties=prop, va='center', ha='right')
            cur_in += meal_row_in
            continue
        p = m.get('protein')
        c = m.get('carbs')
        if c is not None and net_carb:
            c = max(c - float(m.get('fiber') or 0), 0.0)
        f_ = m.get('fat')
        s = m.get('sugar')
        cell_vals = {
            'kcal': f"{kc:.0f}" if kc is not None else None,
            'carb': f"{c:.0f}" if c is not None else None,
            'sugar': f"{s:.0f}" if s is not None and s > 0 else None,
            'protein': f"{p:.0f}" if p is not None else None,
            'fat': f"{f_:.0f}" if f_ is not None else None,
        }
        for key, txt in cell_vals.items():
            if txt is not None:
                fig.text(COL_X[key], ry, txt, color=COL_INK[key], fontsize=18,
                         fontproperties=bold_prop, va='center', ha='right',
                         alpha=row_alpha)

        cur_in += meal_row_in

    # -- NOTICE band (0.11.0). Drawn last, at the bottom, in the warn colour.
    # Never suppressed by a short card and never truncated: the whole reason
    # this band exists is that the previous home for these two facts was
    # stdout of a script nobody runs.
    if band:
        n_y = _last_row_in + NOTICE_GAP_IN
        for line, colour in band:
            # Korean marker, not a dingbat: the shipped font is picked for CJK
            # and a glyph it lacks renders as a tofu box -- which is exactly
            # how a warning stops being read.
            fig.text(L, y(n_y), line, color=colour,
                     fontsize=15, fontproperties=prop, va='center', ha='left')
            n_y += NOTICE_ROW_IN

    plt.savefig(out_path, dpi=150, facecolor=BG, edgecolor='none')
    plt.close()


def refresh_health_pin(iso_date, root=None):
    """After a meal log the card-followup order runs this card; today's
    health pin carries the day's meals too (owner 2026-10-02 12:41-13:00),
    so refresh it here -- the pack's own hop, no kit change. The pin's one
    writer is <root>/service/health/workbench.py (no args = refresh today).
    Today only; inert when the health service is not installed beside this
    skill. Best-effort: never fails, never prints."""
    if iso_date != datetime.date.today().isoformat():
        return False
    root = root or os.path.dirname(_DATA_DIR)
    wb = os.path.join(root, 'service', 'health', 'workbench.py')
    if not os.path.isfile(wb):
        return False
    try:
        import subprocess
        return subprocess.run([sys.executable, wb], capture_output=True,
                              timeout=30, check=False).returncode == 0
    except Exception:            # noqa: BLE001 -- a pin miss never fails a card
        return False


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: card.py \'<json>\'', file=sys.stderr)
        sys.exit(1)

    data     = json.loads(sys.argv[1])
    out_path = data.get('output', '/tmp/diet_card.png')

    # PROJECTION mode (no render, no matplotlib): {"candidate": {"name": "목살",
    # "grams": 220}} or a list under "candidates". Prints one JSON object --
    # the day state plus one projection per candidate -- and draws nothing.
    if 'candidate' in data or 'candidates' in data:
        cands = data.get('candidates') or [data.get('candidate')]
        day = {k: v for k, v in data.items()
               if k not in ('candidate', 'candidates', 'output')}
        day, _iso = load_day(day)
        st = day_state(day)
        print(json.dumps({'state': st, 'projections': [
            projection(st, resolve_candidate(c)) for c in cands]},
            ensure_ascii=False))
        sys.exit(0)

    _require_matplotlib()
    # Data source: if meals/intake absent, auto-aggregate from kit_life.db.
    data, _iso = load_day(data)

    draw_card(data, out_path)
    print(out_path)
    refresh_health_pin(_iso)
