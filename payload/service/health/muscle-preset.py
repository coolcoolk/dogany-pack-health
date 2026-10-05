#!/usr/bin/env python3
# muscle-preset.py -- DGN-385 (instance-local): movement + grip composable preset
# for exercise_muscle mapping. NOT a replacement for exercise_muscle /
# exercise_subregion (rx-calc reads those two tables unchanged). This script
# only DRAFTS a suggested primary/secondary muscle set for a new exercise from
# (movement, grip), so a new exercise-equipment-grip combo doesn't require
# guessing the mapping from scratch. Output is always "estimated" -- a human
# (the user or the agent) must review before it is written into exercise_muscle
# (same "no auto-confirm" philosophy as the rest of workout-log SKILL.md).
#
# Schema (additive, created by DGN-385 seeding):
#   movement_muscle_base(movement, muscle, role)   -- base mapping per movement pattern
#   grip_muscle_delta(grip, muscle, role, evidence) -- additive delta per grip label
#   exercise_movement_grip(exercise_name, movement, equipment, grip) -- per-exercise tags
#
# equipment is documentation-only here (does not affect the computed mapping --
# DGN-385 assumption: equipment changes stability/subregion, not primary/
# secondary muscle assignment. revisit if evidence says otherwise).
#
# Usage:
#   muscle-preset.py --validate <workouts_db>
#       For every exercise in exercise_movement_grip, recompute base+delta and
#       diff against the real exercise_muscle rows. Exit 0 = all tagged
#       exercises reconstruct byte-identical; exit 1 = mismatch found (printed);
#       exit 3 = the pack taxonomy seed never ran on this DB, so there was
#       nothing to check (2026-09-12 -- this used to be a silent exit-0 "pass").
#   muscle-preset.py --draft <movement> <grip_or_-> <workouts_db>
#       Print the suggested muscle rows (JSON) for a NEW exercise with this
#       movement + grip. grip_or_- = '-' means no grip (identity, base only).
#       Does NOT write anything.

import json
import os
import sys
import sqlite3

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# ax_engine carries this pack's taxonomy-state probe (stdlib-only at import).
import ax_engine as TX

# Exit code for "this pack's taxonomy seed never ran on this DB" -- the same
# code ax-project uses, and deliberately not 1. All three of this script's
# tables (movement_muscle_base / grip_muscle_delta / grip_vocab) and the
# exercise_movement_grip roster it walks are SEEDED tables, so on a fresh
# install every one of them is empty and the two modes used to lie in opposite
# directions: --validate reported `checked: 0, all_match: true` and exited 0
# (a pass that verified nothing), --draft blamed a missing ROW ("add rows to
# movement_muscle_base first") when the real repair is a seed that never ran.
RC_NOT_SEEDED = 3


def _refuse_unseeded(db_path, tables):
    """Exit 3 with the named root cause when the seed never ran. Returns
    normally when the DB can answer."""
    try:
        TX.require_taxonomy(db_path, *tables)
    except TX.TaxonomyNotSeeded as exc:
        print(json.dumps({'error': 'taxonomy_not_seeded',
                          'verdict': exc.report.get('verdict'),
                          'empty': exc.report.get('empty'),
                          'fix': TX.taxonomy_seed_command(exc.report)},
                         ensure_ascii=False, indent=2))
        print(TX.taxonomy_diagnostic(exc.report, ', '.join(tables)), file=sys.stderr)
        sys.exit(RC_NOT_SEEDED)


def get_base(conn, movement):
    rows = conn.execute(
        "SELECT muscle, role FROM movement_muscle_base WHERE movement = ?",
        (movement,),
    ).fetchall()
    return {(m, r) for m, r in rows}


def is_known_grip(conn, grip):
    """A grip is valid if it is the identity (no grip) or registered in
    grip_vocab. This is what makes the grip axis extensible without becoming
    a guessing game: a NEW exercise tagged with a grip that nobody registered
    is rejected up front, instead of silently producing a base-only draft that
    looks correct."""
    if not grip or grip == '-':
        return True
    return conn.execute(
        "SELECT 1 FROM grip_vocab WHERE grip = ?", (grip,)
    ).fetchone() is not None


def get_delta(conn, grip):
    if not grip or grip == '-':
        return set()
    rows = conn.execute(
        "SELECT muscle, role FROM grip_muscle_delta WHERE grip = ?",
        (grip,),
    ).fetchall()
    return {(m, r) for m, r in rows}


def compute_draft(conn, movement, grip):
    """Union of base(movement) and delta(grip). Delta ADDS rows only -- never
    removes/overrides a base role (DGN-385 spec: additive-only, no
    contradiction resolution needed while the delta table only holds one
    evidenced entry)."""
    combined = get_base(conn, movement) | get_delta(conn, grip)
    return sorted(combined)


def cmd_validate(db_path):
    # An empty roster is not a clean bill of health. Refuse before walking it.
    _refuse_unseeded(db_path, ("exercise_movement_grip", "movement_muscle_base",
                               "grip_vocab", "grip_muscle_delta"))
    conn = sqlite3.connect(db_path)
    try:
        tagged = conn.execute(
            "SELECT exercise_name, movement, grip FROM exercise_movement_grip"
        ).fetchall()
        mismatches = []
        checked = 0
        unknown_grips = []
        for exercise_name, movement, grip in tagged:
            if not is_known_grip(conn, grip):
                unknown_grips.append({'exercise_name': exercise_name, 'grip': grip})
                continue
            draft = set(compute_draft(conn, movement, grip))
            actual = set(
                conn.execute(
                    "SELECT muscle, role FROM exercise_muscle WHERE exercise_name = ?",
                    (exercise_name,),
                ).fetchall()
            )
            checked += 1
            if draft != actual:
                mismatches.append({
                    'exercise_name': exercise_name,
                    'movement': movement,
                    'grip': grip,
                    'draft':  sorted(draft),
                    'actual': sorted(actual),
                })
        result = {
            'checked': checked,
            'mismatches': mismatches,
            'unknown_grips': unknown_grips,
            'all_match': len(mismatches) == 0 and len(unknown_grips) == 0,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        sys.exit(0 if result['all_match'] else 1)
    finally:
        conn.close()


def cmd_draft(movement, grip, db_path):
    _refuse_unseeded(db_path, ("movement_muscle_base", "grip_vocab",
                               "grip_muscle_delta"))
    conn = sqlite3.connect(db_path)
    try:
        base = sorted(get_base(conn, movement))
        if not base:
            print(json.dumps({
                'error': f'unknown movement {movement!r} -- add rows to '
                         f'movement_muscle_base first (no invented mapping).',
            }, ensure_ascii=False))
            sys.exit(1)
        if not is_known_grip(conn, grip):
            known = [g for (g,) in conn.execute(
                "SELECT grip FROM grip_vocab ORDER BY grip").fetchall()]
            print(json.dumps({
                'error': f'unknown grip {grip!r} -- register it in grip_vocab '
                         f'first (no invented grip). known: {known}',
            }, ensure_ascii=False))
            sys.exit(1)
        draft = compute_draft(conn, movement, grip)
        print(json.dumps({
            'movement': movement,
            'grip': grip,
            'suggested_muscle_rows': [
                {'muscle': m, 'role': r, 'estimated': True} for m, r in draft
            ],
            'note': '초안입니다 -- exercise_muscle에 넣기 전에 확인 필요 (자동 확정 없음).',
        }, ensure_ascii=False, indent=2))
        sys.exit(0)
    finally:
        conn.close()


def main():
    argv = sys.argv[1:]
    if not argv:
        print(
            'Usage: muscle-preset.py --validate <workouts_db>\n'
            '   or: muscle-preset.py --draft <movement> <grip_or_-> <workouts_db>',
            file=sys.stderr,
        )
        sys.exit(1)

    if argv[0] == '--validate':
        if len(argv) < 2:
            print('Usage: muscle-preset.py --validate <workouts_db>', file=sys.stderr)
            sys.exit(1)
        cmd_validate(argv[1])
    elif argv[0] == '--draft':
        if len(argv) < 4:
            print('Usage: muscle-preset.py --draft <movement> <grip_or_-> <workouts_db>',
                  file=sys.stderr)
            sys.exit(1)
        cmd_draft(argv[1], argv[2], argv[3])
    else:
        print(f'Unknown mode: {argv[0]}', file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
