#!/usr/bin/env python3
"""implement.py -- the ONE home of "which implement is this lift, and what do
its weights look like on the owner's screen".

Before this module the answer was spread over rx-calc (venue dumbbell grid),
ax_engine (a hand-kept mirror of it), set-arm / live_load / ax_engine / set-table
(plate and empty-bar text that never checked the implement), and a bodyweight
patch (bw-lift2, folded here). The 2026-10-12 session broke on exactly that:
"empty bar" on a dumbbell, 22.5 kg dumbbells, a chin-up shown as plain bodyweight.

What lives here (design section 4.1):
  kind_of()           barbell | dumbbell | stack | assisted | bodyweight | band
  display(kind, kg)   the owner-facing weight: 60kg + plates per side, per-hand dumbbell,
                      pin for a stack, assist -NNkg, bodyweight, bodyweight +Nkg
  venue grid          DUMBBELL_DEFAULT_*, venue_grid_gaps, venue_dumbbell_points
                      (learned set > learned step > default, minus gaps) --
                      rx-calc and ax_engine re-export these, they own no copy
  bodyweight / assisted  classify, wt_cell/wt_text, assist_estimate, next_target,
                      first_window, last_top_set (folded from bw-lift2)

Table HEADINGS are not here: they stay English (R-T9). Owner copy is by i18n
key. Every function degrades (None / '' / the input) rather than raising: a
display helper must never stop an entry or a table.
"""
import json
import os
import sqlite3
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))

BARBELL = "barbell"
DUMBBELL = "dumbbell"
STACK = "stack"
ASSISTED = "assisted"
BODYWEIGHT = "bodyweight"
BAND = "band"

BAR_KG = 20.0

ASSIST_EQUIPMENT = "bodyweight_assist"
BODYWEIGHT_EQUIPMENT = "bodyweight"
_BARBELL_EQUIPMENT = ("barbell", "ez_bar", "t_bar", "trap_bar", "smith_machine")
_DUMBBELL_EQUIPMENT = ("dumbbell", "kettlebell")
_STACK_EQUIPMENT = ("cable", "machine", "selectorized")


def _t(key, **kw):
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import ui_labels
        return ui_labels.i18n(key, **kw)
    except Exception:  # noqa: BLE001
        return ""


def fmt(v):
    """12.0 -> '12', 12.5 -> '12.5'."""
    try:
        return ("%.2f" % float(v)).rstrip("0").rstrip(".")
    except (TypeError, ValueError):
        return ""


def _disp_w(s):
    return sum(2 if unicodedata.east_asian_width(c) in ("W", "F") else 1
               for c in str(s))


# ---------------------------------------------------------------------------
# the venue's dumbbell rack: ONE source (rx-calc and ax_engine re-export it)
# ---------------------------------------------------------------------------
# The owner's gym is 2 kg steps (14 / 16 / 24; no 15 / 22.5 / 25), so the
# default rack is 2 kg all the way. A venue with a different rack is LEARNED
# (.venue-dumbbells.json / .venue-grid-gaps.json), never by editing this.
DUMBBELL_DEFAULT_GRID = ((2.0, 100.0, 2.0),)
VENUE_DUMBBELL_FILE = ".venue-dumbbells.json"


def _build_default_dumbbell_points():
    pts = []
    for lo, hi, st in DUMBBELL_DEFAULT_GRID:
        k = 0
        while lo + k * st <= hi + 1e-9:
            v = round(lo + k * st, 4)
            if v not in pts:
                pts.append(v)
            k += 1
    return tuple(sorted(pts))


DUMBBELL_DEFAULT_POINTS = _build_default_dumbbell_points()


def _state_dir():
    return (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
            or os.path.join(HERE, "..", "..", "files", "program"))


def _venue_gap_path():
    return os.path.join(_state_dir(), ".venue-grid-gaps.json")


def venue_grid_gaps(implement="dumbbell"):
    """Set of kg this venue's `implement` grid lacks (empty when none learned)."""
    try:
        with open(_venue_gap_path(), encoding="utf-8") as fh:
            data = json.load(fh)
        return set(round(float(x), 4) for x in (data or {}).get(implement) or [])
    except (OSError, ValueError, TypeError, AttributeError):
        return set()


def _venue_learned_dumbbells():
    try:
        with open(os.path.join(_state_dir(), VENUE_DUMBBELL_FILE),
                  encoding="utf-8") as fh:
            data = json.load(fh)
        pts = sorted(set(float(x) for x in (data or {}).get("points") or []
                         if float(x) > 0))
        return pts or None
    except (OSError, ValueError, TypeError, AttributeError):
        return None


def venue_dumbbell_points(default=None):
    """ONE answer for "which dumbbells does this venue have". Order: the learned
    set, else a learned step ("14 or 16" says 2 kg), else `default`; learned
    gaps are removed from whichever applies."""
    default = list(default if default is not None else DUMBBELL_DEFAULT_POINTS)
    gaps = venue_grid_gaps("dumbbell")
    learned = _venue_learned_dumbbells()
    if learned:
        pts = learned
    else:
        try:
            with open(_venue_gap_path(), encoding="utf-8") as fh:
                step = float((json.load(fh) or {}).get("dumbbell_step") or 0)
        except (OSError, ValueError, TypeError, AttributeError):
            step = 0.0
        pts = ([round(step * k, 4) for k in range(1, int(60 // step) + 1)]
               if step > 0 else default)
    return [p for p in pts if p not in gaps] or default


def mark_gap(implement, kg, alts=None):
    """The owner said this venue lacks `kg` ("no 15, use 14 or 16"). Delegates to the
    one learner (live_load.mark_grid_gap) so there is one gap file."""
    if HERE not in sys.path:
        sys.path.insert(0, HERE)
    import live_load
    return live_load.mark_grid_gap(implement, kg, alts)


# ---------------------------------------------------------------------------
# classification
# ---------------------------------------------------------------------------
def _rows(db_path, sql, args=()):
    try:
        conn = sqlite3.connect(db_path)
        try:
            return conn.execute(sql, args).fetchall()
        finally:
            conn.close()
    except Exception:  # noqa: BLE001
        return []


def taxonomy_equipment(db_path, name):
    """exercise_movement_grip.equipment for a lift, else None. The movement
    table is the class fact; ax_exercise.equipment is a seed shortcut that
    classes the chin-up as plain bodyweight, so it is only the fallback."""
    if not db_path or not name:
        return None
    rows = _rows(db_path, "SELECT equipment FROM exercise_movement_grip "
                 "WHERE exercise_name = ?", (name,))
    if rows and rows[0][0]:
        return rows[0][0]
    rows = _rows(db_path, "SELECT equipment FROM ax_exercise "
                 "WHERE exercise_name = ? AND status = 'active'", (name,))
    return rows[0][0] if rows and rows[0][0] else None


def _is_hold(slot):
    if not isinstance(slot, dict):
        return False
    if slot.get("isometric") or slot.get("progression") == "hold":
        return True
    return slot.get("rep_unit") in ("sec", "seconds", "s")


def classify(db_path, name, slot=None):
    """'assisted' / 'bodyweight' / None. Program equipment `bodyweight_assist`
    resolves to assisted -- the root of the 10-12 chin-up break."""
    slot = slot if isinstance(slot, dict) else {}
    if _is_hold(slot):
        return None
    if slot.get("assisted"):
        return ASSISTED
    eq = taxonomy_equipment(db_path, name)
    if eq == ASSIST_EQUIPMENT:
        return ASSISTED
    if eq == BODYWEIGHT_EQUIPMENT:
        return BODYWEIGHT           # a loaded slot's weight_kg is the ADDED load
    return None


def kind_of(db_path, name, slot=None, equipment=None):
    """The implement kind of a lift, or None when unknown (then NO implement
    wording is invented: no plates, no pin, no hand)."""
    cls = classify(db_path, name, slot)
    if cls:
        return cls
    eq = equipment or taxonomy_equipment(db_path, name)
    if eq in _BARBELL_EQUIPMENT:
        return BARBELL
    if eq in _DUMBBELL_EQUIPMENT:
        return DUMBBELL
    if eq in _STACK_EQUIPMENT:
        return STACK
    if eq == "band":
        return BAND
    return None


def has_history(db_path, name, exclude_session_id=None):
    sql = "SELECT 1 FROM workout_sets WHERE exercise_name = ? AND set_seq >= 1"
    args = [name]
    if exclude_session_id is not None:
        sql += " AND session_id != ?"
        args.append(exclude_session_id)
    return bool(_rows(db_path, sql + " LIMIT 1", args))


# ---------------------------------------------------------------------------
# display: the owner-facing weight, by kind
# ---------------------------------------------------------------------------
def display_name(disp, cls):
    """An assisted lift is NAMED as such (an 'assisted' prefix on the display name). Idempotent."""
    disp = str(disp or "")
    if cls != ASSISTED:
        return disp
    prefix = _t("health.impl.assist_prefix")
    if not prefix or disp.startswith(prefix):
        return disp
    return "%s %s" % (prefix, disp)


def wt_text(cls, weight_kg):
    """Bodyweight / bodyweight +Nkg / assist -Nkg phrase. Never '?'."""
    if cls == ASSISTED:
        if weight_kg is None:
            return _t("health.impl.wt.assist_tbd")
        return _t("health.impl.wt.assist", kg=fmt(weight_kg))
    if weight_kg is None or float(weight_kg) <= 0:
        return _t("health.impl.wt.bodyweight")
    return _t("health.impl.wt.bodyweight_plus", kg=fmt(weight_kg))


def wt_cell(cls, weight_kg):
    """WT-column cell (the column is 9 display columns wide): '-25kg' under the
    Assist head, the bodyweight word, or '+12.5kg' when the phrase does not fit."""
    if cls == ASSISTED:
        if weight_kg is None:
            return _t("health.impl.wt.assist_tbd")
        return "-%skg" % fmt(weight_kg)
    if weight_kg is None or float(weight_kg) <= 0:
        return _t("health.impl.wt.bodyweight")
    full = wt_text(cls, weight_kg)
    return full if _disp_w(full) <= 9 else "+%skg" % fmt(weight_kg)


def head_wt(cls):
    """The WT heading of an assisted table. English, like every table head."""
    return "Assist" if cls == ASSISTED else ""


def display(kind, kg=None):
    """The weight as the owner reads it, per implement. A dumbbell is per hand
    and never has a bar; a stack is a pin; only a barbell names plates."""
    if kind in (ASSISTED, BODYWEIGHT):
        return wt_text(kind, kg)
    if kg is None:
        return ""
    if kind == BARBELL:
        side = (float(kg) - BAR_KG) / 2.0
        if side < 0:                                   # lighter than the bar
            return "%skg" % fmt(kg)
        if side == 0:
            return _t("health.impl.display.barbell_bare", kg=fmt(kg))
        return _t("health.impl.display.barbell", kg=fmt(kg), side=fmt(side))
    if kind == DUMBBELL:
        return _t("health.impl.display.dumbbell", kg=fmt(kg))
    if kind == STACK:
        return _t("health.impl.display.stack", kg=fmt(kg))
    return "%skg" % fmt(kg)


def plate_text_allowed(kind):
    """Plate / empty-bar wording is for a barbell and nothing else."""
    return kind == BARBELL


# ---------------------------------------------------------------------------
# first-time assist estimate, progression (reps first, then less assist / load)
# ---------------------------------------------------------------------------
DEFAULT_STEP_KG = 2.5
BW_REP_RANGE = (6, 10)
FIRST_WINDOW = tuple(range(1, 16))
TARGET_REPS_FRACTION = 0.75
MAX_ASSIST_FRACTION = 0.8
NO_PULL_HISTORY_FRACTION = 0.5
DEFAULT_ASSIST_KG = 30.0        # no body weight on file: a stated default, never a question


def body_weight_kg(db_path):
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import assist_load
        series = assist_load.bodyweight_series(db_path)
        return series[-1][1] if series else None
    except Exception:  # noqa: BLE001
        return None


def pull_capacity_kg(db_path, name=None):
    """Best Epley e1RM over the owner's logged pull work on a loaded implement."""
    rows = _rows(
        db_path,
        "SELECT s.weight_kg, s.reps FROM workout_sets s "
        "JOIN exercise_movement_grip g ON g.exercise_name = s.exercise_name "
        "WHERE s.set_seq >= 1 AND s.weight_kg > 0 AND s.reps > 0 "
        "AND g.movement IN ('vertical_pull', 'horizontal_pull', "
        "'pull_compound') "
        "AND COALESCE(g.equipment, '') NOT IN (?, ?) "
        "AND s.exercise_name != ?",
        (ASSIST_EQUIPMENT, BODYWEIGHT_EQUIPMENT, name or ""))
    best = None
    for kg, reps in rows:
        e1 = float(kg) * (1.0 + float(reps) / 30.0)
        best = e1 if best is None or e1 > best else best
    return best


def lattice_step(slot):
    lat = (slot or {}).get("lattice") if isinstance(slot, dict) else None
    try:
        st = float((lat or {}).get("step"))
        return st if st > 0 else None
    except (TypeError, ValueError, AttributeError):
        return None


def assist_estimate(db_path, name, slot=None, step=None):
    """First-time assist for an assisted lift: {'kg', 'source', ...}. ALWAYS
    answers (R-E3: the engine proposes, the owner corrects): body weight x
    pull strength when known, half body weight with no pull history, and a
    stated default with no body weight at all."""
    step = step or lattice_step(slot) or DEFAULT_STEP_KG
    bw = body_weight_kg(db_path)
    if not bw:
        return {"kg": round(round(DEFAULT_ASSIST_KG / step) * step, 4),
                "source": "default", "bodyweight": None, "capacity": None}
    cap = pull_capacity_kg(db_path, name)
    if cap:
        raw, source = bw - TARGET_REPS_FRACTION * cap, "pull_strength"
    else:
        raw, source = NO_PULL_HISTORY_FRACTION * bw, "bodyweight_only"
    raw = max(0.0, min(raw, MAX_ASSIST_FRACTION * bw))
    return {"kg": round(round(raw / step) * step, 4), "source": source,
            "bodyweight": bw, "capacity": cap}


def rep_bounds(slot):
    rr = (slot or {}).get("rep_range") if isinstance(slot, dict) else None
    try:
        lo, hi = int(rr[0]), int(rr[1])
        if 0 < lo <= hi:
            return lo, hi
    except (TypeError, ValueError, IndexError, KeyError):
        pass
    return BW_REP_RANGE


def next_target(cls, last_weight, last_reps, slot=None):
    """Reps first; at the range top: assisted -> one step LESS assist,
    bodyweight -> one step of added load, reps restart at the bottom."""
    lo, hi = rep_bounds(slot)
    step = lattice_step(slot) or DEFAULT_STEP_KG
    w = None if last_weight is None else float(last_weight)
    try:
        reps = int(last_reps)
    except (TypeError, ValueError):
        return {"weight_kg": w, "reps": hi, "move": "repeat"}
    if reps < hi:
        return {"weight_kg": w, "reps": min(max(reps + 1, lo), hi),
                "move": "reps"}
    if cls == ASSISTED:
        return {"weight_kg": max((0.0 if w is None else w) - step, 0.0),
                "reps": lo, "move": "less_assist"}
    return {"weight_kg": (w or 0.0) + step, "reps": lo, "move": "add_load"}


def last_top_set(db_path, name, cls, exclude_session_id=None):
    """(weight_kg, reps) of the hardest working set of the latest session that
    logged this lift: lowest assist for assisted, else the heaviest load."""
    sql = ("SELECT session_id, weight_kg, reps FROM workout_sets "
           "WHERE exercise_name = ? AND set_seq >= 1 AND reps IS NOT NULL")
    args = [name]
    if exclude_session_id is not None:
        sql += " AND session_id != ?"
        args.append(exclude_session_id)
    rows = _rows(db_path, sql + " ORDER BY session_id DESC, id ASC", args)
    if not rows:
        return None
    sid = rows[0][0]
    sets = [(w, r) for s, w, r in rows if s == sid]
    if cls == ASSISTED:
        def key(s):
            return (-(s[0] if s[0] is not None else 1e9), s[1])
    else:
        def key(s):
            return (s[0] or 0.0, s[1])
    return max(sets, key=key)


def first_window(db_path, name, slot=None, exclude_session_id=None):
    """The reps keyboard of a first-ever bodyweight / assisted set: 1..15."""
    if classify(db_path, name, slot) is None:
        return []
    if has_history(db_path, name, exclude_session_id):
        return []
    return list(FIRST_WINDOW)


def prescription(db_path, session_id, name, slot, weight_kg=None, disp=None):
    """The engine-owned prescription of a bodyweight / assisted entry:
    {'class', 'name', 'weight_kg', 'wt', 'reps', 'move', 'say', 'source',
    'window'} or None for a lift this module does not own. The say line states
    a number and never asks one (R-E3, R-X3)."""
    cls = classify(db_path, name, slot)
    if cls is None:
        return None
    name_disp = display_name(disp or (slot or {}).get("display") or name, cls)
    lo, hi = rep_bounds(slot)
    if has_history(db_path, name, session_id):
        last = last_top_set(db_path, name, cls, session_id)
        nxt = next_target(cls, last[0] if last else None,
                          last[1] if last else None, slot)
        wt, reps, move = nxt["weight_kg"], nxt["reps"], nxt["move"]
        say = _t("health.impl.say.progress.%s" % move, name=name_disp,
                 wt=wt_text(cls, wt), reps=reps)
        source, window = "history:%s" % move, "target"
    else:
        wt, reps, move, window = weight_kg, hi, "first", "1-15"
        if cls == ASSISTED:
            if wt is None:
                wt = assist_estimate(db_path, name, slot)["kg"]
            say = _t("health.impl.say.assist_first", name=name_disp,
                     wt=wt_text(cls, wt))
            source = "estimate"
        else:
            say = _t("health.impl.say.first", name=name_disp)
            source = "first_set"
    return {"class": cls, "name": name_disp, "weight_kg": wt,
            "wt": wt_text(cls, wt), "reps": reps, "move": move, "say": say,
            "source": source, "window": window}
