#!/usr/bin/env python3
# us_reseed.py -- reseed us_step from program.yaml (SoT for rotation roster/order).
#
# The us_step rows are a projection of the workout program: for each rotation
# day (session_ref), the ordered exercise roster with per-step delivery
# metadata. program.yaml (files/program/program.yaml) is the source of truth
# for WHICH exercises appear in WHICH order per day. This script re-derives the
# us_step rows so seq / exercise_ref / step_type match program.yaml, preserving
# the established step semantics and re-materializing next_hint via the engine's
# own logic (us_render.materialize_next_hint) -- no divergent hand-rolled hint.
#
# Deterministic + idempotent: each row's ULID is a fixed function of
# (rotation-day index, seq), so re-running upserts the same rows. Rows beyond a
# day's program.yaml slot count are removed (handles roster shrink).
#
# Derivation rules (matching the existing seed conventions, verified against the
# live rows before reseed):
#   step_type      = 'hold' when the exercise measures hold_sec, else 'working'.
#   measure        = ax_exercise.measure ('reps' | 'hold_sec').
#   target         = "{lo}-{hi}"   for reps  (from program.yaml rep_range)
#                    "{lo}-{hi}s"  for hold  (rep_range = hold-seconds window)
#   rest_sec       = 150 if ax_exercise.movement=='compound' else 90.
#   equipment_need = 'bodyweight' if load_type=='bodyweight' else 'equipment'.
#   display_source = 'exercise_derived' ; display_key = NULL ; group_id = NULL.
#   suppress_alert = 0.
#   next_hint      = (re)materialized by us_render.materialize_next_hint.
#
# Only OWNER-owned us_step rows are touched. No other table is written.
#
# Usage: us_reseed.py --db <path> [--apply] [--json]
#   default is dry-run (report only); --apply performs the write.
#
# stdlib + sqlite3 only.

import os
import sys
import json
import argparse
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import us_render as US  # engine next_hint materialization (reuse, no divergence)

# Rotation-day -> stable 1-based index for the ULID scheme
# (matches existing seed: 01KZST0000000000000000<dayN><seq2>, e.g. 앞A seq7 =
# 01KZST000000000000000107). Order per program.yaml `rotation`.
DAY_INDEX = {"앞A": 1, "뒷A": 2, "앞B": 3, "뒷B": 4}
ULID_STEM = "01KZST0000000000000000"  # 22 chars; + dayN(1) + seq(2) = 26
CREATED_AT = "2026-08-10T00:00:00Z"   # preserve original seed timestamp (stable)

OWNER = "warg"  # estate-scrub:allow(legacy DB slug value, a data contract kept for pre-049 DBs)


def _ulid(day, seq):
    """Deterministic us_step ULID for (rotation-day, seq). Fixed => idempotent."""
    return "%s%d%02d" % (ULID_STEM, DAY_INDEX[day], seq)


# ---------------------------------------------------------------------------
# Minimal program.yaml reader. We only need, per day, the ordered list of
# exercise names + rep_range. The file is large and richly commented; a full
# YAML lib is not a stdlib dependency, so we parse the narrow structure we own
# (days: -> <day>: -> exercises: -> - slot/name/rep_range). Values we read are
# simple scalars / 2-int lists. STOP-and-fail on any structural surprise rather
# than guess.
# ---------------------------------------------------------------------------
def parse_program(path):
    """Return ordered dict {day: [ {slot, name, rep_range:[lo,hi]} ... ]}.
    Whitespace-indentation driven, scoped to the `days:` block only."""
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    days = {}
    in_days = False
    cur_day = None
    cur_ex = None  # current exercise dict being filled

    def _flush(ex, day):
        if ex is not None and day is not None:
            days[day].append(ex)

    for raw in lines:
        # strip trailing comment (only outside quotes; our scalars here are
        # unquoted names / lists / ints, so a naive split on ' #' is safe for
        # the fields we consume -- name, slot, rep_range).
        line = raw.rstrip("\n")
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip(" "))

        # top-level key: `days:` opens the block; any other 0-indent key after
        # closes it (e.g. `changelog:`).
        if indent == 0:
            if stripped.startswith("days:"):
                in_days = True
                cur_day = None
                cur_ex = None
                continue
            else:
                if in_days:
                    _flush(cur_ex, cur_day)
                    cur_ex = None
                in_days = False
                continue
        if not in_days:
            continue

        # day header: `  <day>:` at indent 2 (value empty / trailing comment)
        if indent == 2 and stripped.endswith(":") is False and ":" in stripped:
            # form `앞A:  # ...` -> key before colon
            key = stripped.split(":", 1)[0].strip()
            _flush(cur_ex, cur_day)
            cur_ex = None
            cur_day = key
            days[cur_day] = []
            continue
        if indent == 2 and stripped.endswith(":"):
            key = stripped[:-1].strip()
            _flush(cur_ex, cur_day)
            cur_ex = None
            cur_day = key
            days[cur_day] = []
            continue

        if cur_day is None:
            continue

        # exercise list item start: `      - slot: N`
        if stripped.startswith("- slot:"):
            _flush(cur_ex, cur_day)
            cur_ex = {"slot": _int(stripped.split(":", 1)[1]),
                      "name": None, "rep_range": None}
            continue
        if cur_ex is None:
            continue

        # field lines within an exercise
        if stripped.startswith("name:"):
            cur_ex["name"] = _scalar(stripped.split(":", 1)[1])
        elif stripped.startswith("rep_range:"):
            cur_ex["rep_range"] = _int_list(stripped.split(":", 1)[1])
        # other fields ignored (weight_kg, sets, safety_note, etc.)

    # final flush
    if in_days:
        _flush(cur_ex, cur_day)

    # keep only real day blocks (guard against focus_slot etc. leaking as keys)
    return {d: exs for d, exs in days.items() if d in DAY_INDEX}


def _strip_comment(v):
    # remove an inline ` # ...` comment; safe for our unquoted scalar fields
    idx = v.find(" #")
    if idx >= 0:
        v = v[:idx]
    return v.strip()


def _scalar(v):
    v = _strip_comment(v)
    if v.startswith('"') and v.endswith('"') and len(v) >= 2:
        v = v[1:-1]
    return v


def _int(v):
    return int(_strip_comment(v))


def _int_list(v):
    v = _strip_comment(v)
    v = v.strip().strip("[]")
    return [int(x.strip()) for x in v.split(",") if x.strip()]


# ---------------------------------------------------------------------------
# ax_exercise resolution + row derivation
# ---------------------------------------------------------------------------
def load_exercises(conn):
    rows = conn.execute(
        "SELECT ulid, exercise_name, movement, measure, load_type "
        "FROM ax_exercise WHERE owning_agent=?;", (OWNER,)).fetchall()
    return {r["exercise_name"]: r for r in rows}


def derive_row(day, ex_entry, ax):
    """Build the full us_step column set for one program.yaml exercise entry.
    ax = matched ax_exercise row. seq = program.yaml slot (contiguous 1..N)."""
    seq = ex_entry["slot"]
    measure = ax["measure"]
    step_type = "hold" if measure == "hold_sec" else "working"
    lo, hi = ex_entry["rep_range"]
    if measure == "hold_sec":
        target = "%d-%ds" % (lo, hi)
    else:
        target = "%d-%d" % (lo, hi)
    rest_sec = 150 if ax["movement"] == "compound" else 90
    equip = "bodyweight" if ax["load_type"] == "bodyweight" else "equipment"
    return {
        "ulid": _ulid(day, seq),
        "owning_agent": OWNER,
        "session_ref": day,
        "seq": seq,
        "exercise_ref": ax["ulid"],
        "step_type": step_type,
        "group_id": None,
        "display_source": "exercise_derived",
        "display_key": None,
        "equipment_need": equip,
        "measure": measure,
        "target": target,
        "rest_sec": rest_sec,
        "suppress_alert": 0,
        "next_hint": None,   # materialized after all rows are in place
        "created_at": CREATED_AT,
    }


UPSERT_SQL = (
    "INSERT INTO us_step (ulid, owning_agent, session_ref, seq, exercise_ref, "
    "step_type, group_id, display_source, display_key, equipment_need, "
    "measure, target, rest_sec, suppress_alert, next_hint, created_at) "
    "VALUES (:ulid, :owning_agent, :session_ref, :seq, :exercise_ref, "
    ":step_type, :group_id, :display_source, :display_key, :equipment_need, "
    ":measure, :target, :rest_sec, :suppress_alert, :next_hint, :created_at) "
    "ON CONFLICT(ulid) DO UPDATE SET "
    "session_ref=excluded.session_ref, seq=excluded.seq, "
    "exercise_ref=excluded.exercise_ref, step_type=excluded.step_type, "
    "group_id=excluded.group_id, display_source=excluded.display_source, "
    "display_key=excluded.display_key, equipment_need=excluded.equipment_need, "
    "measure=excluded.measure, target=excluded.target, "
    "rest_sec=excluded.rest_sec, suppress_alert=excluded.suppress_alert, "
    "created_at=excluded.created_at;"
)


def reseed(conn, program_path, apply_changes):
    """Reseed the legacy-owner us_step from program.yaml. Returns a report dict.
    In dry-run (apply_changes=False) the transaction is rolled back."""
    program = parse_program(program_path)
    exmap = load_exercises(conn)

    report = {"days": {}, "missing_exercises": [], "applied": apply_changes,
              "skipped_days": []}

    planned = {}    # day -> list of derived rows (only resolvable ones)
    for day in [d for d in DAY_INDEX if d in program]:
        entries = program[day]
        # slots must be a dense 1..N sequence -- seq is derived from slot and
        # the unique index (session_ref, seq) requires no gaps/dupes. STOP on
        # a structural surprise rather than silently seed a broken sequence.
        slots = [e["slot"] for e in entries]
        if slots != list(range(1, len(slots) + 1)):
            raise ValueError(
                "program.yaml day %s has non-contiguous slots %s" % (day, slots))
        for e in entries:
            if e.get("name") is None or e.get("rep_range") is None:
                raise ValueError(
                    "program.yaml day %s slot %s missing name/rep_range"
                    % (day, e.get("slot")))
        rows = []
        day_missing = []
        for e in entries:
            if e["name"] not in exmap:
                report["missing_exercises"].append(
                    {"day": day, "slot": e["slot"], "name": e["name"]})
                day_missing.append(e)
                continue
            rows.append(derive_row(day, e, exmap[e["name"]]))
        planned[day] = rows
        report["days"][day] = {
            "program_slots": [e["name"] for e in entries],
            "seeded_rows": [(r["seq"], r["exercise_ref"]) for r in rows],
            "missing": [(e["slot"], e["name"]) for e in day_missing],
        }
        if day_missing:
            # A gap means we cannot faithfully seed this day's full sequence
            # (a hole in seq order). Skip the WHOLE day's write to avoid a
            # sequence with a missing slot; flag for a decision.
            report["skipped_days"].append(day)

    conn.execute("BEGIN;")
    try:
        for day, rows in planned.items():
            if day in report["skipped_days"]:
                continue
            # Clear this day's OWNER rows first, then insert the fresh roster.
            # Delete-then-insert (vs in-place upsert) sidesteps transient
            # UNIQUE(session_ref, seq) collisions during a roster reorder, and
            # is still idempotent because every row's ULID is deterministic.
            # Scoped strictly to this session_ref + owning_agent=OWNER.
            conn.execute(
                "DELETE FROM us_step WHERE owning_agent=? AND session_ref=?;",
                (OWNER, day))
            for r in rows:
                conn.execute(UPSERT_SQL, r)
            # re-materialize next_hint via the engine (R3), consistent path
            US.materialize_next_hint(conn, day, write=True)
        if apply_changes:
            conn.commit()
        else:
            conn.rollback()
    except Exception:
        conn.rollback()
        raise
    return report


def main():
    ap = argparse.ArgumentParser(description="Reseed the legacy-owner us_step from program.yaml")
    ap.add_argument("--db", required=True, help="path to kit_life.db")
    ap.add_argument("--program", default=os.path.join(
        os.path.expanduser("~"), ".dogany", "agents", "Warg", "files",  # estate-scrub:allow(legacy default workspace path, kept for the retired manual script)
        "program", "program.yaml"), help="path to program.yaml")
    ap.add_argument("--apply", action="store_true",
                    help="perform the write (default: dry-run, rolled back)")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    args = ap.parse_args()

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    try:
        report = reseed(conn, args.program, args.apply)
    finally:
        conn.close()

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("reseed %s (%s)" % (
            "APPLIED" if args.apply else "DRY-RUN", args.db))
        for day, info in report["days"].items():
            flag = "  [SKIPPED: missing exercise]" if day in report[
                "skipped_days"] else ""
            print("  %s: %d rows%s" % (day, len(info["seeded_rows"]), flag))
        if report["missing_exercises"]:
            print("BLOCKERS (exercise not in ax_exercise):")
            for m in report["missing_exercises"]:
                print("  %s slot%s: %s" % (m["day"], m["slot"], m["name"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
