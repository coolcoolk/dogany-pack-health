# -*- coding: utf-8 -*-
"""live_load.py -- today's load for a lift nothing measured has a number for.

WHY (owner live 2026-10-08 session 1, 07:24-07:51, pack 0.35.1 -- the first
session after a program reset, so every lift had weight_kg null and no
history). The owner had to ask back eight times, and every one of them was a
number the CODE never produced, so the agent made one up in prose or asked:

  * "how many kg?" -- the entry carried no weight at all (no estimate);
  * "you may go one step up next set" + a next-set line `... x 15` --
    after a logged 5kg x 15 the next-set line still had no weight, because the
    arm read rx-calc (None) and nothing re-derived from the set just done;
  * "log it as a ramp-up and go to the next weight" -- 50kg x 15 @RIR4 on an 8-rep
    target was stored as working set 1, while 20kg x 10 @RIR3 on 12-15 was
    (correctly) working: that call was the agent's, and it got one of two wrong;
  * "you told me 5kg" / "you told me 20" -- the weight the agent had named was never
    armed, so a reps-only reply had nothing to record against.

THE RULES (data: live_load.json; this module is its one reader):
  calibrating(...)  a lift with no measured basis: program weight_kg null and
                    no working set with a weight in any OTHER session. Only
                    these lifts get the estimate / classification / next-weight
                    below; a lift with history keeps its rx prescription.
  classify(...)     first working set of a calibrating lift: implied reps at
                    the target RIR (reps + rir - rir_target) outside the
                    rep_range band -> a CALIBRATION rung (stored in the ramp
                    lane), inside -> working set 1.
  next_load(...)    the concrete next weight from a logged set's e1RM, on the
                    grid the set is actually done on (machine pins incl. a
                    known add-on block, else the slot lattice).
  estimate(...)     the labelled entry estimate from an anchor lift's e1RM.
  load_cue(...)     the pin / plate / dumbbell words for a weight.

The decided weight is ARMED, not narrated: it is written into the per-
(session, exercise) override (.set-arm-override/, the shared contract set-arm
and set-table already read), so the table, NEXT_HINT, the pre-log arm and
set-add's text-path default all carry the same number.

stdlib only; every public function is best-effort (a miss returns None and
the caller keeps its pre-existing behaviour).
"""
import json
import math
import os
import re
import sqlite3
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
             or os.path.join(HERE, "..", "..", "files", "program"))
RULES_PATH = os.path.join(HERE, "live_load.json")
# Shared with set-arm / set-table (OVERRIDE_DIR, _override_path): ONE file per
# (session, exercise) carries the served target and its sentence.
OVERRIDE_DIR = os.path.join(STATE_DIR, ".set-arm-override")
# A calibration rung closes the warm-up ladder for the lift (set-arm
# resolve_ramp_plan / set-table render read ladder_closed()).
CALIB_DIR = os.path.join(STATE_DIR, ".live-calibration")
# Optional add-on block per machine: {ulid: {"addon": kg | null | "unknown"}}.
ADDON_PATH = os.path.join(STATE_DIR, ".machine-addon.json")
# set_seq rows whose add-on block was unknown when logged, per session.
ADDON_PENDING_DIR = os.path.join(STATE_DIR, ".addon-pending")

DECISION_ESTIMATE = "estimate"
DECISION_NEXT = "live_load"
ADDON_UNKNOWN = "unknown"

try:
    sys.path.insert(0, HERE)
    try:
        from db_pool import connect as _db_connect
    finally:
        sys.path.remove(HERE)
except Exception:  # noqa: BLE001
    _db_connect = sqlite3.connect

_RULES = None


def rules():
    global _RULES
    if _RULES is None:
        with open(RULES_PATH, encoding="utf-8") as fh:
            _RULES = json.load(fh)
    return _RULES


def _e1():
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import e1rm_rx
        return e1rm_rx
    except Exception:  # noqa: BLE001
        return None


def set_e1rm(weight, reps, rir=None):
    """The pack's one per-set e1RM (e1rm_rx.set_e1rm), Epley fallback."""
    e1 = _e1()
    if e1 is not None:
        return e1.set_e1rm(float(weight), int(reps), rir)[0]
    return float(weight) * (1 + (int(reps) + (rir or 0)) / 30.0)


def kg_txt(v):
    """20.0 -> '20', 6.25 -> '6.25' (SKILL: weight decimals verbatim)."""
    if v is None:
        return "-"
    f = float(v)
    return str(int(f)) if f.is_integer() else ("%.2f" % f).rstrip("0").rstrip(".")


def _safe(name):
    return re.sub(r"[^A-Za-z0-9_.-]", "_", str(name or ""))


# ---------------------------------------------------------------------------
# slot / day
# ---------------------------------------------------------------------------
def session_code(db_path, session_id):
    try:
        c = _db_connect(db_path)
        try:
            row = c.execute(
                "SELECT st.code FROM workouts w JOIN session_type st "
                "ON st.id = w.session_type_id WHERE w.id = ?",
                (session_id,)).fetchone()
        finally:
            c.close()
        return row[0] if row else None
    except sqlite3.Error:
        return None


def find_slot(rx, program_path, db_path, session_id, exercise_name):
    """A COPY of the program slot for this lift (the session's own day first),
    or None."""
    try:
        program = rx.load_yaml(program_path) or {}
    except Exception:  # noqa: BLE001
        return None
    days = program.get("days") or {}
    code = session_code(db_path, session_id)
    order = ([code] if code in days else []) + [d for d in days if d != code]
    for d in order:
        for s in (days.get(d) or {}).get("exercises") or []:
            if isinstance(s, dict) and s.get("name") == exercise_name:
                return dict(s)
    return None


def _entry_setup():
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import entry_setup
        return entry_setup
    except Exception:  # noqa: BLE001
        return None


def view(rx, slot, db_path, session_id, exercise_name):
    """The slot as it is done TODAY: a copy carrying `_variant` (the
    implement the owner picked at entry) and that implement's class grid."""
    if not isinstance(slot, dict):
        return slot
    out = dict(slot)
    es = _entry_setup()
    v = es.picked(session_id, exercise_name) if es else None
    if v and v != exercise_name:
        out["_variant"] = v
        _mv, eq = _movement_equipment(db_path, v)
        try:
            cls = rx.CLASS_LATTICE_BY_EQUIPMENT.get(eq)
        except Exception:  # noqa: BLE001
            cls = None
        if cls:
            out["lattice"] = dict(cls)
    return out


def band(slot):
    """(lo, hi) of the slot rep_range, a one-number range widened."""
    rr = (slot or {}).get("rep_range")
    try:
        if isinstance(rr, (list, tuple)) and len(rr) >= 2:
            lo, hi = int(rr[0]), int(rr[1])
        elif isinstance(rr, (list, tuple)) and rr:
            lo = hi = int(rr[0])
        else:
            lo = hi = int(rr)
    except (TypeError, ValueError):
        return None
    if lo == hi:
        tol = int(rules()["band"]["single_target_tolerance"])
        lo, hi = lo - tol, hi + tol
    return lo, hi


def rir_target(rx, slot):
    try:
        b = rx.resolve_target_rir(slot)
        if b:
            return int(b[-1])
    except Exception:  # noqa: BLE001
        pass
    return int(rules()["band"]["rir_default"])


def _movement_equipment(db_path, exercise_name):
    try:
        c = _db_connect(db_path)
        try:
            row = c.execute(
                "SELECT movement, equipment FROM exercise_movement_grip "
                "WHERE exercise_name = ?", (exercise_name,)).fetchone()
        finally:
            c.close()
        return (row[0], row[1]) if row else (None, None)
    except sqlite3.Error:
        return None, None


def _is_hold(slot):
    unit = (slot or {}).get("rep_unit")
    return unit in ("sec", "seconds", "hold_sec") or bool(
        (slot or {}).get("hold_sec"))


def prior_session_working(db_path, session_id, exercise_name):
    """True when ANY other session logged a weighted working set of this lift."""
    try:
        c = _db_connect(db_path)
        try:
            row = c.execute(
                "SELECT 1 FROM workout_sets WHERE exercise_name = ? AND "
                "session_id != ? AND set_seq >= 1 AND weight_kg IS NOT NULL "
                "AND reps IS NOT NULL LIMIT 1",
                (exercise_name, session_id)).fetchone()
        finally:
            c.close()
        return bool(row)
    except sqlite3.Error:
        return False


def calibrating(db_path, session_id, exercise_name, slot):
    """No measured basis for today's load: program weight_kg null, no prior
    session's weighted working set, a rep-measured lift on loadable
    equipment (never a hold, bodyweight or assisted lift)."""
    if not isinstance(slot, dict) or _is_hold(slot):
        return False
    if slot.get("fixed_implement"):
        # a swing / slam: the bell IS the load and the reps are the dose
        # (owner 2026-10-10: 12kg x 40 x 3) -- nothing to calibrate.
        return False
    if slot.get("weight_kg") is not None or slot.get("assisted"):
        return False
    if band(slot) is None:
        return False
    _mv, eq = _movement_equipment(db_path, exercise_name)
    if eq in ("bodyweight", "bodyweight_assist", "medicine_ball"):
        return False
    return not prior_session_working(db_path, session_id, exercise_name)


def session_working(db_path, session_id, exercise_name):
    """[(set_seq, weight, reps, rir)] working rows of this lift today."""
    try:
        c = _db_connect(db_path)
        try:
            return [tuple(r) for r in c.execute(
                "SELECT set_seq, weight_kg, reps, rir FROM workout_sets WHERE "
                "session_id = ? AND exercise_name = ? AND set_seq >= 1 "
                "ORDER BY set_seq", (session_id, exercise_name))]
        finally:
            c.close()
    except sqlite3.Error:
        return []


# ---------------------------------------------------------------------------
# implied reps / classification
# ---------------------------------------------------------------------------
def implied_reps(reps, rir, rir_t):
    if reps is None:
        return None
    return float(reps) + (float(rir) if rir is not None else 0.0) - rir_t


def classify(weight, reps, rir, lohi, rir_t):
    """('calibration'|'working', implied). ABOVE the band only: a set that
    light was a ramp-up (owner: "log it as a ramp-up, next weight"). A set BELOW
    the band is a real working set the owner fought for -- live batch 2 item
    1 (bench 70kg x5 @RIR2 on 7-8) steps the NEXT set down from it instead.
    No RIR -> the implied count is a lower bound, which still decides
    "above"."""
    imp = implied_reps(reps, rir, rir_t)
    if weight is None or imp is None or lohi is None:
        return "working", imp
    margin = float((rules().get("calibration") or {}).get("margin_reps", 0))
    if imp > lohi[1] + margin + 1e-9:
        return "calibration", imp
    return "working", imp


# ---------------------------------------------------------------------------
# the grid the set is done on
# ---------------------------------------------------------------------------
def _machine_capture():
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import machine_capture
        return machine_capture
    except Exception:  # noqa: BLE001
        return None


def session_machine(db_path, session_id, exercise_name):
    mc = _machine_capture()
    if mc is None:
        return None
    try:
        hit = mc.session_machine(db_path, session_id, exercise_name)
        return hit[0] if hit else None
    except Exception:  # noqa: BLE001
        return None


def machine_stack(db_path, ulid):
    """(stated pin points, lattice (base, step) | None) of a machine."""
    try:
        c = _db_connect(db_path)
        try:
            row = c.execute(
                "SELECT available_plates, lattice_base, lattice_step FROM "
                "ax_machine WHERE ulid = ?", (ulid,)).fetchone()
        finally:
            c.close()
    except sqlite3.Error:
        return [], None
    if not row:
        return [], None
    pts = []
    try:
        pts = sorted(set(float(x) for x in json.loads(row[0] or "[]")))
    except (TypeError, ValueError):
        pts = []
    lat = ((float(row[1]), float(row[2]))
           if row[1] is not None and row[2] is not None else None)
    return pts, lat


def grid_points(rx, slot, db_path, session_id, exercise_name, center):
    """Loadable weights around `center`: the slot's resolved grid (machine
    pins first -- rx-calc resolve_lattice), else the default increment."""
    lo_kg = max(0.0, center * float(rules()["next"]["search_low"]))
    hi_kg = max(center * float(rules()["next"]["search_high"]), center + 5)
    ex = dict(slot or {})
    ex.setdefault("name", exercise_name)
    lat = None
    if ex.get("_variant"):
        # The owner picked another implement (entry_setup): the slot's own
        # grid is the wrong one. This session's machine for the lift (a
        # cable/machine variant), else the variant equipment's class grid.
        ulid = session_machine(db_path, session_id, exercise_name)
        try:
            lat = rx.machine_lattice(db_path, ulid) if ulid else None
        except Exception:  # noqa: BLE001
            lat = None
        lat = lat or ex.get("lattice")
    else:
        try:
            lat, _src = rx.resolve_lattice(ex, db_path, session_id)
        except Exception:  # noqa: BLE001
            lat = ex.get("lattice")
    pts = []
    try:
        pts = list(rx._lattice_points(lat))
    except Exception:  # noqa: BLE001
        pts = []
    if not pts:
        step = None
        try:
            step = rx._lattice_step(lat)
        except Exception:  # noqa: BLE001
            step = None
        if step is None:
            try:
                inc = float(rx.default_inc(exercise_name))
            except Exception:  # noqa: BLE001
                inc = 2.5
            step = (0.0, inc)
        base, st = step
        k0 = max(0, int(math.floor((lo_kg - base) / st)))
        k1 = int(math.ceil((hi_kg - base) / st)) + 1
        pts = [round(base + k * st, 4) for k in range(k0, k1 + 1)
               if base + k * st > 0]
    pts = sorted(set(p for p in pts if p > 0))
    near = [p for p in pts if lo_kg - 1e-9 <= p <= hi_kg + 1e-9]
    return near or pts


def choose(e1rm, lohi, rir_t, points):
    """(kg, implied) on `points`: in band and closest to the band middle,
    else closest to the band; ties -> lighter."""
    if not points or not e1rm or lohi is None:
        return None, None
    lo, hi = lohi
    mid = (lo + hi) / 2.0

    def imp(p):
        return 30.0 * (e1rm / p - 1.0) - rir_t

    def score(p):
        r = imp(p)
        if lo - 1e-9 <= r <= hi + 1e-9:
            return (0, abs(r - mid), p)
        return (1, min(abs(r - lo), abs(r - hi)), p)
    best = min(points, key=score)
    return best, imp(best)


def next_load(rx, slot, db_path, session_id, exercise_name, weight, reps,
              rir):
    """The next set's weight from one logged set. dict(kg, implied, e1rm,
    move up|hold|down) or None."""
    if weight is None or reps is None or not slot:
        return None
    lohi = band(slot)
    if lohi is None:
        return None
    rt = rir_target(rx, slot)
    e1 = set_e1rm(weight, reps, rir)
    pts = grid_points(rx, slot, db_path, session_id, exercise_name,
                      float(weight))
    if float(weight) not in pts:
        pts = sorted(set(pts + [float(weight)]))
    kg, imp = choose(e1, lohi, rt, pts)
    if kg is None:
        return None
    move = ("hold" if abs(kg - float(weight)) < 1e-6
            else ("up" if kg > float(weight) else "down"))
    return {"kg": kg, "implied": imp, "e1rm": e1, "move": move,
            "band": lohi, "rir_target": rt}


# ---------------------------------------------------------------------------
# the entry estimate
# ---------------------------------------------------------------------------
def _best_e1rm(db_path, exercise_name, session_id=None, exclude=None):
    """(e1rm, date) of the best working set: in `session_id`, else in the
    newest session (not `exclude`) that logged this lift."""
    try:
        c = _db_connect(db_path)
        try:
            if session_id is not None:
                rows = c.execute(
                    "SELECT s.weight_kg, s.reps, s.rir, w.date FROM "
                    "workout_sets s JOIN workouts w ON w.id = s.session_id "
                    "WHERE s.session_id = ? AND s.exercise_name = ? AND "
                    "s.set_seq >= 1 AND s.weight_kg IS NOT NULL AND "
                    "s.reps IS NOT NULL", (session_id, exercise_name)
                ).fetchall()
            else:
                last = c.execute(
                    "SELECT s.session_id FROM workout_sets s JOIN workouts w "
                    "ON w.id = s.session_id WHERE s.exercise_name = ? AND "
                    "s.session_id != ? AND s.set_seq >= 1 AND s.weight_kg IS "
                    "NOT NULL AND s.reps IS NOT NULL ORDER BY w.date DESC, "
                    "s.session_id DESC LIMIT 1",
                    (exercise_name, exclude if exclude is not None else -1)
                ).fetchone()
                if not last:
                    return None
                rows = c.execute(
                    "SELECT s.weight_kg, s.reps, s.rir, w.date FROM "
                    "workout_sets s JOIN workouts w ON w.id = s.session_id "
                    "WHERE s.session_id = ? AND s.exercise_name = ? AND "
                    "s.set_seq >= 1 AND s.weight_kg IS NOT NULL AND "
                    "s.reps IS NOT NULL", (last[0], exercise_name)).fetchall()
        finally:
            c.close()
    except sqlite3.Error:
        return None
    best = None
    for w, r, rir, d in rows:
        try:
            v = set_e1rm(w, r, rir)
        except (TypeError, ValueError):
            continue
        if best is None or v > best[0]:
            best = (v, d)
    return best


def anchor(db_path, session_id, region):
    """dict(e1rm=<anchor-equivalent>, exercise, raw, when) or None. Today's
    session first (the freshest evidence), else the newest logged session."""
    anchors = (rules()["estimate"]["anchors"] or {}).get(region) or []
    for scope in ("today", "history"):
        best = None
        for a in anchors:
            hit = (_best_e1rm(db_path, a["exercise"], session_id=session_id)
                   if scope == "today"
                   else _best_e1rm(db_path, a["exercise"], exclude=session_id))
            if hit is None:
                continue
            eq = hit[0] * float(a.get("scale", 1.0))
            if best is None or eq > best["e1rm"]:
                best = {"e1rm": eq, "exercise": a["exercise"],
                        "raw": hit[0], "when": scope, "date": hit[1]}
        if best is not None:
            return best
    return None


def estimate(rx, slot, db_path, session_id, exercise_name, variant=None):
    """The labelled starting weight for a calibrating lift, or None.
    `variant` = the implement-variant exercise the owner picked (its
    movement/equipment keys the ratio; the slot keeps its own band/grid)."""
    mv, eq = _movement_equipment(db_path, variant or exercise_name)
    if mv is None:
        return None
    r = (rules()["estimate"]["ratios"] or {}).get("%s/%s" % (mv, eq))
    if not r:
        return None
    a = anchor(db_path, session_id, r["region"])
    if a is None:
        return None
    lohi = band(slot)
    if lohi is None:
        return None
    rt = rir_target(rx, slot)
    target = a["e1rm"] * float(r["ratio"]) * float(
        rules()["estimate"]["conservative"])
    raw = target / (1 + (lohi[0] + rt) / 30.0)
    pts = grid_points(rx, slot, db_path, session_id, exercise_name, raw)
    under = [p for p in pts if p <= raw + 1e-9]
    kg = max(under) if under else (min(pts) if pts else None)
    if kg is None:
        return None
    try:
        import ui_labels
        anchor_disp = ui_labels.exercise_ko(a["exercise"])
    except Exception:  # noqa: BLE001
        anchor_disp = a["exercise"]
    return {"kg": kg, "raw": raw, "ratio": float(r["ratio"]),
            "anchor": a["exercise"], "anchor_e1rm": a["raw"],
            "anchor_disp": anchor_disp,
            "anchor_when": a["when"], "anchor_date": a["date"],
            "key": "%s/%s" % (mv, eq), "band": lohi, "rir_target": rt}


# ---------------------------------------------------------------------------
# words: the pin / plate / dumbbell for a weight
# ---------------------------------------------------------------------------
def _addon_data():
    try:
        with open(ADDON_PATH, encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def addon_record(ulid):
    """{"addon": kg|None|'unknown', "stack": [pin kg]} or {} (never stated)."""
    rec = _addon_data().get(ulid)
    return rec if isinstance(rec, dict) else {}


def addon_of(ulid):
    """kg (float) | None (no block / never stated) | 'unknown'."""
    v = addon_record(ulid).get("addon")
    if v == ADDON_UNKNOWN:
        return ADDON_UNKNOWN
    try:
        return float(v) if v is not None else None
    except (TypeError, ValueError):
        return None


def addon_stated(ulid):
    return "addon" in addon_record(ulid)


def set_stack(ulid, stack):
    """Remember the bare pin stack of a machine (the add-on is stated apart)."""
    data = _addon_data()
    rec = dict(data.get(ulid) or {})
    rec["stack"] = sorted(set(float(x) for x in stack))
    rec["at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    data[ulid] = rec
    _write_addon_data(data)


def _write_addon_data(data):
    os.makedirs(os.path.dirname(ADDON_PATH), exist_ok=True)
    tmp = ADDON_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, sort_keys=True)
    os.replace(tmp, ADDON_PATH)


def set_addon(ulid, value, stack=None, source=None, confidence=None):
    """Persist a machine's add-on block (float kg, None = none, 'unknown')
    and, when known, the bare pin stack it sits on. `source` / `confidence`
    (0.36.0 item 6) say where a kg came from -- a looked-up page or the
    owner -- so a number is never stored without its provenance."""
    data = _addon_data()
    rec = dict(data.get(ulid) or {})
    rec["addon"] = value
    if source:
        rec["source"] = str(source)
        rec["confidence"] = str(confidence or "")
    if stack:
        rec["stack"] = sorted(set(float(x) for x in stack))
    rec["at"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    data[ulid] = rec
    _write_addon_data(data)


def _ax():
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import ax_engine
        return ax_engine
    except Exception:  # noqa: BLE001
        return None


def load_cue(db_path, session_id, exercise_name, slot, kg):
    """How to SET this weight, in the owner's words, or ""."""
    if kg is None:
        return ""
    ulid = session_machine(db_path, session_id, exercise_name)
    if ulid:
        add = addon_of(ulid)
        if isinstance(add, float) and add > 0:
            stack = addon_record(ulid).get("stack") or []
            if not stack:
                pins, lat = machine_stack(db_path, ulid)
                stack = ([round(lat[0] + k * lat[1], 4) for k in range(200)]
                         if lat is not None else [])
            base = round(kg - add, 4)
            if stack and kg not in stack and base in stack:
                return t("health.live.cue.pin_block", kg=kg_txt(base),
                         add=kg_txt(add))
        return t("health.live.cue.pin", kg=kg_txt(kg))
    ax = _ax()
    kind_ex = (slot or {}).get("_variant") or exercise_name
    lat_type = ((slot or {}).get("lattice") or {}).get("type") \
        if isinstance((slot or {}).get("lattice"), dict) else None
    _mv, eq = _movement_equipment(db_path, kind_ex)
    try:
        if eq == "barbell" or (ax is not None and not (slot or {}).get(
                "_variant") and ax.is_plate_loaded(db_path, exercise_name,
                                                   lat_type)):
            note = ax.plate_breakdown(kg) if ax is not None else ""
            return note or t("health.live.cue.empty_bar", kg=kg_txt(kg))
    except Exception:  # noqa: BLE001
        pass
    if eq == "ez_bar":
        return t("health.live.cue.ez_bar", kg=kg_txt(kg))
    if eq == "dumbbell" or lat_type == "even":
        return t("health.live.cue.dumbbell", kg=kg_txt(kg))
    if eq in ("cable", "machine") or lat_type == "stack":
        return t("health.live.cue.pin", kg=kg_txt(kg))
    return ""


# ---------------------------------------------------------------------------
# the armed target (shared override file) + the calibration marker
# ---------------------------------------------------------------------------
def override_path(session_id, exercise_name):
    return os.path.join(OVERRIDE_DIR, "%s.%s.json"
                        % (session_id, _safe(exercise_name)))


def read_override(session_id, exercise_name):
    try:
        with open(override_path(session_id, exercise_name)) as fh:
            data = json.load(fh)
        return data if isinstance(data, dict) else {}
    except (OSError, ValueError):
        return {}


def arm_weight(session_id, exercise_name, kg, decision, reason, say,
               from_seq=None):
    """Serve `kg` for this (session, exercise): MERGED into the shared
    override (display / reps / rir a caller set survive). by=coach -- the
    code's call; the owner naming a number still wins (set-arm --ov-by
    owner rewrites the file). `from_seq` = the logged row this decision was
    derived from, so set-undo can take the decision away with its row."""
    ov = read_override(session_id, exercise_name)
    if ov.get("weight_kg") != float(kg):
        # a fallback weight (design 2) belongs to the load it was named for
        ov.pop("alt_weight_kg", None)
    ov.update({"weight_kg": float(kg), "by": "coach", "decision": decision,
               "reason": reason, "reason_source": "code", "say": say,
               "source": "live_load",
               "at": time.strftime("%Y-%m-%dT%H:%M:%S")})
    if from_seq is None:
        ov.pop("from_seq", None)
    else:
        ov["from_seq"] = int(from_seq)
    os.makedirs(OVERRIDE_DIR, exist_ok=True)
    path = override_path(session_id, exercise_name)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(ov, fh, ensure_ascii=False)
    os.rename(tmp, path)
    return ov


# ---------------------------------------------------------------------------
# the calibration ramp (owner 2026-10-10 12:47-12:50, free session deadlift)
# ---------------------------------------------------------------------------
# The owner ramped 20 -> 60 -> 100 -> 130 on a lift with no history. Three
# defects, one rule each:
#   * a coach-armed target sat BELOW a rung already lifted (50kg after 60x5,
#     kept after the undo): a coach target on a calibrating lift is never at or
#     below today's heaviest completed rung -- it is re-derived from that rung;
#   * a short first set with no RIR stepped the load DOWN on reps alone: with
#     no RIR the set says nothing about effort, so it is a rung and RIR is asked;
#   * a rung above a stale coach target was refused: only an OWNER-named
#     working weight is a ceiling for rungs while the lift is calibrating.
# An owner-named weight (by=owner) is never replaced by any of this.
RAMP_SEQ_FLOOR = -100          # set-add PREP_SEQ_BASE: prep rows sit at/below


def ramp_rungs_today(db_path, session_id, exercise_name):
    """[(set_seq, weight, reps, rir)] loaded ramp rows of this lift today,
    heaviest first."""
    try:
        c = _db_connect(db_path)
        try:
            return [tuple(r) for r in c.execute(
                "SELECT set_seq, weight_kg, reps, rir FROM workout_sets WHERE "
                "session_id = ? AND exercise_name = ? AND set_seq <= 0 AND "
                "set_seq > ? AND weight_kg IS NOT NULL "
                "ORDER BY weight_kg DESC, set_seq ASC",
                (session_id, exercise_name, RAMP_SEQ_FLOOR))]
        finally:
            c.close()
    except sqlite3.Error:
        return []


def owner_named(ov):
    return (ov or {}).get("by") == "owner" and (ov or {}).get(
        "weight_kg") is not None


def coach_target(ov):
    """The coach-armed working weight (kg) or None. Owner-named -> None."""
    if not ov or owner_named(ov) or ov.get("weight_kg") is None:
        return None
    try:
        return float(ov["weight_kg"])
    except (TypeError, ValueError):
        return None


def rung_rir(rir):
    """The RIR a rung is read at: the stated one, else the warm-up reserve
    (a warm-up is by definition far from failure -- never 0, which is what
    an e1RM with no RIR assumes and what stepped 60x5 down to 50)."""
    if rir is not None:
        return float(rir)
    return float((rules().get("calibration") or {}).get("rung_rir_assumed",
                                                         4))


def above_rungs(rx, slot, db_path, session_id, exercise_name, kg,
                strict=False):
    """`kg` lifted to today's heaviest completed warm-up rung when it sits
    below it (owner 2026-10-10: a working target never sits below a warm-up
    already lifted). `strict` -> the first settable weight ABOVE the rung
    (the calibration ramp's own target: a working weight equal to the last
    warm-up is no step at all). No rung / kg None -> kg unchanged."""
    if kg is None:
        return kg
    # Only a WARM-UP rung is a floor: no RIR, or the warm-up reserve (4+).
    # A rung with a stated RIR under that is a measurement, and its e1RM
    # decides the working weight even below it (live batch 2 probe rule:
    # 17.5kg x 8 @RIR2 makes 10 reps @RIR1 lighter than 17.5).
    rungs = [r for r in ramp_rungs_today(db_path, session_id, exercise_name)
             if r[3] is None or float(r[3]) >= rung_rir(None)]
    if not rungs:
        return kg
    top = float(rungs[0][1])
    if float(kg) > top + 1e-9 or (not strict and float(kg) >= top - 1e-9):
        return kg
    if not strict:
        return top
    pts = grid_points(rx, slot, db_path, session_id, exercise_name, top)
    above = sorted(p for p in pts if p > top + 1e-9)
    return above[0] if above else kg


def ramp_target(rx, slot, db_path, session_id, exercise_name):
    """Re-derive a calibrating lift's coach target from today's rungs.

    Returns dict(kg, prev, rung, reason) after re-arming, or None when there
    is nothing to change: the lift is not calibrating, a working set is
    logged (LOAD_NEXT owns the next weight), the owner named the weight, no
    loaded rung is logged, or the current target is already above the
    heaviest rung and no rung carries a stated RIR newer than it.

    The new target: the heaviest rung's e1RM (stated RIR, else the warm-up
    reserve) back-solved into the band, then never at or below a WARM-UP rung
    (no RIR / 4+) -- the next loadable weight above it is the floor. A rung
    with a stated RIR under 4 is a measurement: its e1RM decides."""
    if not calibrating(db_path, session_id, exercise_name, slot):
        return None
    if session_working(db_path, session_id, exercise_name):
        return None
    ov = read_override(session_id, exercise_name)
    if owner_named(ov):
        return None
    rungs = ramp_rungs_today(db_path, session_id, exercise_name)
    if not rungs:
        return None
    seq, w, reps, rir = rungs[0]
    w = float(w)
    cur = coach_target(ov)
    informative = rir is not None and float(rir) < rung_rir(None)
    if cur is None and not informative:
        return None        # no target yet and the rung says nothing: ramp on
    if cur is not None and cur > w + 1e-9 and not informative:
        return None
    nxt = next_load(rx, slot, db_path, session_id, exercise_name, w,
                    int(reps or 1), rung_rir(rir))
    kg = above_rungs(rx, slot, db_path, session_id, exercise_name,
                     nxt["kg"] if nxt else w, strict=True)
    if kg is None or (not informative and kg <= w + 1e-9):
        return None
    if cur is not None and abs(kg - cur) < 1e-6:
        return None
    reason = ("ramp rung %skg x %s RIR %s%s -> target above it"
              % (kg_txt(w), reps, kg_txt(rung_rir(rir)),
                 "" if informative else " (assumed warm-up reserve)"))
    arm_weight(session_id, exercise_name, kg, DECISION_NEXT, reason, None,
               from_seq=seq)
    return {"kg": kg, "prev": cur, "rung": w, "rung_seq": seq,
            "reason": reason}


EMPTY_BAR_KG = 20.0


def natural_zero(rx, slot, db_path, session_id, exercise_name):
    """(kg, kind) where a no-history ramp starts, or (None, None).

    owner 2026-10-10 12:47: with no load history the ramp starts from the
    load's natural zero -- the empty bar on a barbell lift (the venue records
    no bar weight today, so the standard 20kg), the lightest settable weight
    on a dumbbell / kettlebell / machine grid -- and the agent prescribes the
    climb; it never asks the owner to "pick a comfortable weight"."""
    _mv, eq = _movement_equipment(db_path, exercise_name)
    if eq in ("bodyweight", "bodyweight_assist", "medicine_ball"):
        return None, None
    lat = (slot or {}).get("lattice")
    lat_type = lat.get("type") if isinstance(lat, dict) else None
    plate = eq in ("barbell", "smith_machine")
    if not plate and eq is None:
        ax = _ax()
        try:
            plate = bool(ax and ax.is_plate_loaded(db_path, exercise_name,
                                                   lat_type))
        except Exception:  # noqa: BLE001
            plate = False
    if plate:
        return EMPTY_BAR_KG, "bar"
    try:
        pts = grid_points(rx, slot, db_path, session_id, exercise_name, 1.0)
    except Exception:  # noqa: BLE001
        pts = []
    return (min(pts), "lightest") if pts else (None, None)


def calibration_open(rx, slot, db_path, session_id, exercise_name):
    """The calibration ramp in progress, as a dict, or None.

    rehearsal S2 (2026-10-10): exercise-enter announces "no record -> climb
    from the bar" (CALIBRATION_RAMP); set-arm's ramp gate then found no target
    weight and CLOSED, asking the owner for today's weight -- so the owner's
    next "60-5" read as a target. While a calibrating lift has no working set
    and no named weight, the climb itself IS the plan: the next owner-reported
    set is a rung (set-add classifies it). Returns
    dict(rungs, top=(kg, reps) | None, start=(kg, kind) | None); `rungs` = 0
    means the climb has not started (start = the natural zero)."""
    if not calibrating(db_path, session_id, exercise_name, slot):
        return None
    if session_working(db_path, session_id, exercise_name):
        return None
    if owner_named(read_override(session_id, exercise_name)):
        return None
    rungs = ramp_rungs_today(db_path, session_id, exercise_name)
    if rungs:
        return {"rungs": len(rungs), "top": (float(rungs[0][1]), rungs[0][2]),
                "start": None}
    zero_kg, zero_kind = natural_zero(rx, slot, db_path, session_id,
                                      exercise_name)
    if zero_kg is None:
        return None
    return {"rungs": 0, "top": None, "start": (zero_kg, zero_kind)}


def calibration_next_say(display, state):
    """The ONE owner sentence while the climb has no target: ask for the next
    rung in plain words (no jargon, no "pick a weight")."""
    if state.get("start") is not None:
        kg, kind = state["start"]
        return t("health.live.calib_first_say", name=display,
                 start=t("health.live.ramp_start." + kind, kg=kg_txt(kg)),
                 example=t("health.live.calib_first_example"))
    return t("health.live.calib_next_say", name=display)


def calib_path(session_id, exercise_name):
    return os.path.join(CALIB_DIR, "%s.%s.json"
                        % (session_id, _safe(exercise_name)))


def mark_calibration(session_id, exercise_name, info):
    os.makedirs(CALIB_DIR, exist_ok=True)
    path = calib_path(session_id, exercise_name)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(info, fh, ensure_ascii=False)
    os.rename(tmp, path)


def ladder_closed(session_id, exercise_name):
    """True once a calibration rung was logged for this lift today: the
    warm-up ladder is behind it, the next step is working set 1."""
    return os.path.exists(calib_path(session_id, exercise_name))


# ---------------------------------------------------------------------------
# owner sentences (relayed verbatim: `TOKEN: <sentence>` lines)
# ---------------------------------------------------------------------------
def t(key, **kw):
    """Owner copy from the i18n bundle (code stays ASCII; ui_labels.i18n)."""
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import ui_labels
        return ui_labels.i18n(key, **kw)
    except Exception:  # noqa: BLE001
        return ""


def _cue(cue, key="health.live.cue_paren"):
    return t(key, cue=cue) if cue else ""


def estimate_say(display, est, cue):
    anchor = t("health.live.anchor.today" if est["anchor_when"] == "today"
               else "health.live.anchor.last", name=est["anchor_disp"])
    return t("health.live.estimate_say", name=display, kg=kg_txt(est["kg"]),
             cue=_cue(cue, "health.live.cue_dot"), anchor=anchor,
             e1rm=kg_txt(round(est["anchor_e1rm"])))


def next_say(display, kg, prev_kg, move, cue, lohi, rt):
    """ONE sentence: the change and how to set it. The NEXT_SET blockquote
    (live batch 2 item 8) carries the full prescription; this is the
    register's weight-note bullet, so it does not restate reps / rest."""
    head = t("health.live.next.%s" % move, prev=kg_txt(prev_kg),
             kg=kg_txt(kg))
    return t("health.live.next_say", head=head, cue=_cue(cue), lo=lohi[0],
             hi=lohi[1], rir=rt)


def calibration_say(display, weight, reps, rir, nxt_kg, cue, lohi, rt):
    return t("health.live.calibration_say", name=display, kg=kg_txt(weight),
             reps=int(reps),
             rir_clause=(t("health.live.rir_clause", rir=rir)
                         if rir is not None else ""),
             lo=lohi[0], hi=lohi[1], rir=rt, next=kg_txt(nxt_kg),
             cue=_cue(cue))


def stack_label(is_cable, lo, hi):
    return t("health.live.stack_label.%s" % ("cable" if is_cable
                                             else "machine"),
             lo=kg_txt(lo), hi=kg_txt(hi))


# ---------------------------------------------------------------------------
# add-on blocks logged before their weight was known
# ---------------------------------------------------------------------------
def pending_path(session_id):
    return os.path.join(ADDON_PENDING_DIR, "%s.json" % int(session_id))


def read_pending(session_id):
    try:
        with open(pending_path(session_id), encoding="utf-8") as fh:
            data = json.load(fh)
        return data if isinstance(data, list) else []
    except (OSError, ValueError):
        return []


def add_pending(session_id, row):
    data = [r for r in read_pending(session_id)
            if not (r.get("exercise") == row.get("exercise")
                    and r.get("set_seq") == row.get("set_seq"))]
    data.append(row)
    os.makedirs(ADDON_PENDING_DIR, exist_ok=True)
    tmp = pending_path(session_id) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False)
    os.replace(tmp, pending_path(session_id))


def clear_pending(session_id, machine):
    keep = [r for r in read_pending(session_id) if r.get("machine") != machine]
    os.makedirs(ADDON_PENDING_DIR, exist_ok=True)
    tmp = pending_path(session_id) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(keep, fh, ensure_ascii=False)
    os.replace(tmp, pending_path(session_id))
