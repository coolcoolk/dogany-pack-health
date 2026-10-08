#!/usr/bin/env python3
"""undo_lib.py -- shared machinery for the workout DELETE verbs
(set-undo / exercise-drop / session-abort), landed 2026-08-25.

WHY THIS EXISTS
---------------
The workout-session module shipped half-CRUD. create/read/update existed for all
three entities (session / exercise-instance / set); DELETE existed for NONE of
them. The only real delete anywhere in the pipeline was kit_life.py's unguarded
`workout_del()`, which cascades an entire session's set rows and printed a single
`deleted workout {id}` line while doing it.

Two things looked like deletes and were not:
  * `session-cursor clear` removes the .active-session MARKER only -- the
    workouts row and every set survive, leaving a half-open session that
    `session-closeout --check` flags NEEDS_CLOSEOUT forever;
  * `set-add --correct` OVERWRITES in place -- the row count never changes, so a
    phantom row from a mis-tap (set_seq=4 on a 3-set exercise) is permanent and
    inflates every volume / e1RM aggregate.

WHY THE VERBS LIVE IN service/health AND NOT IN THE kit_life CLI
---------------------------------------------------------------
A workout delete is not a row delete. Removing a set has to invalidate the
DOMAIN RUNTIME STATE that was armed off that set's existence:
  .idrill-arm/<sha256(sid|ex|seq)[:8]>   the next set's in-place keyboard, whose
                                         baked `cmd` argv names the exact seq
  .telegram_bot/countdown/rest-*.json    a running rest countdown on the phone
  .set-table-published/<sid>.<ex>        the 표2 grid idempotency flag
  .exercise-entered/<sid>.<ex>           the entry-payload-delivered marker
  .set-arm-override/<sid>.<ex>.json      the F19/F21 target override
  .plate-cue/<sid>.<ex>                  the "last cued weight" memory
  .arm-gen/<sid>                         the push fencing token
  .active-session / .session-closed      the session lifecycle gate + tombstone
  dashboard.md `workout` pin section     the pinned 표3 종목카드
Every one of those is a files/program surface (STATE_DIR convention; set-arm is
sole writer of the arm dir; session-closeout owns the pin clear). database/
kit_life.py is SHARED kit code -- the main agent runs the same file and has no files/program
at all -- so putting the verbs there would either duplicate this knowledge into
an agent that must not have it, or ship deletes that leave the markers dangling,
which is exactly the defect being fixed. The verbs are instance-local; the SHARED
CLI's job was only to stop deleting silently (see kit_life.py workout_del guard).

RE-SEQUENCING DECISION: A REMOVED SET LEAVES A HOLE. Rationale in `hole_note()`.

stdlib only.
"""

import hashlib
import importlib.machinery
import importlib.util
import json
import os
import re
import sqlite3
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
# LIVE-SAFETY: runtime-state root -- identical contract to set-arm / set-add /
# session-closeout. Tests MUST export LIFEKIT_HEALTH_STATE_DIR=<temp dir>; unset means the
# owner's LIVE marker surface.
PROJECT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
# 2026-08-25: pinned to files/program independently of where this module
# lives -- bridge/bot.py:4239 reads .idrill-arm/ from that exact path.
STATE_DIR = (os.environ.get("LIFEKIT_HEALTH_STATE_DIR")
             or os.path.join(PROJECT_ROOT, "files", "program"))
DEFAULT_DB = os.path.join(HERE, "..", "..", "database", "kit_life.db")

ACTIVE_MARKER = os.path.join(STATE_DIR, ".active-session")
CLOSED_TOMBSTONE = os.path.join(STATE_DIR, ".session-closed")
ENTERED_DIR = os.path.join(STATE_DIR, ".exercise-entered")
PUBLISHED_DIR = os.path.join(STATE_DIR, ".set-table-published")
IDRILL_ARM_DIR = os.path.join(STATE_DIR, ".idrill-arm")
ARM_GEN_DIR = os.path.join(STATE_DIR, ".arm-gen")
OVERRIDE_DIR = os.path.join(STATE_DIR, ".set-arm-override")
PLATE_CUE_DIR = os.path.join(STATE_DIR, ".plate-cue")
# Same env hook set-arm honours, so a test never cancels the owner's live timer.
COUNTDOWN_DIR = os.environ.get(
    "WARG_COUNTDOWN_DIR",
    os.path.join(HERE, "..", "..", ".telegram_bot", "countdown"))
# UNDO-OF-THE-UNDO. Every destroyed row is archived here as JSON before the
# DELETE commits, so a wrong undo is recoverable by hand instead of being gone.
# This is what makes these verbs safe to hand a model: the DB row leaves, the
# facts do not.
DISCARDED_DIR = os.path.join(STATE_DIR, ".discarded")

SET_COLS = ("id", "session_id", "exercise_name", "slot_num", "set_seq",
            "weight_kg", "reps", "rir", "raw_input", "recorded_at")

# Exit codes -- same contract the rest of service/health uses.
#   0 = done, 1 = usage / not-found error, 3 = REFUSED (nothing was written).
REFUSE_CODE = 3


def hole_note():
    """WHY A REMOVED SET LEAVES A HOLE INSTEAD OF RENUMBERING.

    Removing set_seq=2 of 3 leaves rows at 1 and 3. It does NOT renumber 3 -> 2.

    1. set_seq is CALLER-CHOSEN, not code-derived (see set-add
       `_refuse_occupied_seq`), and it carries a SIGN CONVENTION: seq <= 0 is the
       warm-up / ramp lane, seq >= 1 is the working lane (migration 034 backfills
       set_seq<=0 rows as set_kind='ramp'). A blind renumber can walk a row
       across that lane boundary and silently reclassify real data.
    2. THE OWNER ALREADY HEARD THE NUMBERS. They was told "3세트" when set 3 was
       logged. Renumbering makes the next thing they hear contradict the last
       thing they heard, for a row they never touched. A hole is visible and honest;
       a renumber is a silent rewrite of history they already saw.
    3. DOWNSTREAM STATE IS KEYED ON THE SEQ. .idrill-arm files are named
       sha256("<sid>|<ex>|<seq>")[:8] and their baked `cmd` argv contains the
       literal seq. Renumbering orphans or mis-binds every arm for the exercise
       -- the failure mode is a button that writes to the wrong row.
    4. UNIQUE(session_id, exercise_name, set_seq) makes a renumber an N-row
       ordered dance to dodge transient collisions. A hole is one DELETE.
    5. NOTHING NUMERIC CARES. Volume / e1RM / tonnage aggregate with SUM and MAX
       over ROWS, and every volume query already filters set_seq >= 1. A gap in
       the integers moves no figure.
    6. THE COMMON CASE SELF-HEALS ANYWAY. set-add computes next_free as
       MAX(seq>=1)+1, so undoing the LAST set immediately reuses the number. A
       hole is only ever visible for a mid-sequence undo -- precisely the case
       where preserving what the owner was told matters most.
    """
    return ("set_seq holes are intentional: seq is caller-chosen, carries the "
            "ramp/working sign convention, keys the .idrill-arm files, and the "
            "owner already heard the old numbers. Aggregates use SUM/MAX over "
            "rows, so a gap moves no figure.")


# ---------------------------------------------------------------------------
# small shared helpers
# ---------------------------------------------------------------------------
def load_sibling(name, filename):
    """Import an extension-less sibling script as a module (same convention
    session-open / session-cursor / exercise-enter use)."""
    path = os.path.join(HERE, filename)
    spec = importlib.util.spec_from_loader(
        name, importlib.machinery.SourceFileLoader(name, path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def safe_token(exercise_name):
    """exercise-enter / set-add / set-table marker token convention, verbatim."""
    return re.sub(r"[^A-Za-z0-9_.-]", "_", str(exercise_name or ""))


def arm_id(session_id, exercise_name, set_seq):
    """set-arm.compute_arm_id, duplicated (one literal beats importing the whole
    209KB set-arm module, which pulls program.yaml + rx-calc, to hash a string).
    Keep in sync with set-arm.compute_arm_id."""
    key = "%s|%s|%s" % (session_id, exercise_name, set_seq)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:8]


def marker_read(path):
    try:
        with open(path) as fh:
            txt = fh.read().strip()
        return int(txt) if txt else None
    except (OSError, ValueError):
        return None


def _rm(path):
    try:
        os.remove(path)
        return True
    except OSError:
        return False


def lane_of(set_seq):
    """'working' (seq >= 1) or 'ramp' (seq <= 0). The two lanes are numbered
    independently (working ascends from 1, ramp descends from -1, 0 is the
    bodyweight primer), so "is this the last set" is a per-lane question."""
    return "working" if int(set_seq) >= 1 else "ramp"


# ---------------------------------------------------------------------------
# DB reads
# ---------------------------------------------------------------------------
def session_row(conn, session_id):
    """(date, note, session_type_code) or None."""
    return conn.execute(
        "SELECT w.date, w.note, st.code FROM workouts w "
        "LEFT JOIN session_type st ON st.id = w.session_type_id "
        "WHERE w.id=?;", (int(session_id),)).fetchone()


def newest_session_id(conn):
    row = conn.execute(
        "SELECT id FROM workouts ORDER BY date DESC, created_at DESC, id DESC "
        "LIMIT 1;").fetchone()
    return int(row[0]) if row else None


def sets_of(conn, session_id, exercise_name=None):
    """Full rows (SET_COLS order) for a session, optionally one exercise."""
    sql = ("SELECT id, session_id, exercise_name, slot_num, set_seq, "
           "weight_kg, reps, rir, raw_input, recorded_at FROM workout_sets "
           "WHERE session_id=?")
    args = [int(session_id)]
    if exercise_name is not None:
        sql += " AND exercise_name=?"
        args.append(exercise_name)
    sql += " ORDER BY slot_num, exercise_name, set_seq;"
    return conn.execute(sql, args).fetchall()


def exercises_of(conn, session_id):
    """[(exercise_name, n_sets, 'seq,seq,...')] in program slot order."""
    return [(r[0], int(r[1]), r[2]) for r in conn.execute(
        "SELECT exercise_name, COUNT(*), group_concat(set_seq) "
        "FROM workout_sets WHERE session_id=? GROUP BY exercise_name "
        "ORDER BY MIN(slot_num), exercise_name;", (int(session_id),)).fetchall()]


def referencing_records(conn, session_id):
    """`record` rows whose polymorphic pointer targets this workouts row.

    These do NOT cascade -- record has no FK to workouts (source_table /
    source_id is a text+int pointer) -- so deleting the session leaves them
    DANGLING, and a later rowid reuse silently re-binds them to a different
    session (kit_life.py GUARD #3b). Returns [(record_id, ulid_or_'')].
    """
    try:
        return [(int(r[0]), r[1] or "") for r in conn.execute(
            "SELECT id, COALESCE(ulid,'') FROM record "
            "WHERE source_table='workouts' AND source_id=?;",
            (int(session_id),)).fetchall()]
    except sqlite3.OperationalError:
        return []


def classification_count(conn, session_id):
    try:
        return int(conn.execute(
            "SELECT COUNT(*) FROM workout_classifications WHERE workout_id=?;",
            (int(session_id),)).fetchone()[0])
    except sqlite3.OperationalError:
        return 0


# ---------------------------------------------------------------------------
# archive (undo-of-the-undo)
# ---------------------------------------------------------------------------
def archive(kind, payload, dry_run=False):
    """Dump the rows about to be destroyed to .discarded/<ts>-<kind>.json.
    Best-effort by policy but LOUD on failure: the caller prints the path, and a
    None return tells it to say so."""
    if dry_run:
        return None
    try:
        os.makedirs(DISCARDED_DIR, exist_ok=True)
        path = os.path.join(
            DISCARDED_DIR, "%s-%s.json" % (time.strftime("%Y%m%d-%H%M%S"), kind))
        tmp = "%s.tmp.%d" % (path, os.getpid())
        with open(tmp, "w") as fh:
            json.dump(payload, fh, ensure_ascii=False, indent=1)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, path)
        return path
    except OSError:
        return None


def rows_as_dicts(rows):
    return [dict(zip(SET_COLS, r)) for r in rows]


# ---------------------------------------------------------------------------
# runtime-state invalidation
# ---------------------------------------------------------------------------
def arm_files_for(session_id, exercise_name=None):
    """Every .idrill-arm payload belonging to this (session[, exercise]).

    Arm ids are a hash, so attribution is by READING each payload's session_id /
    exercise_name -- never by filename. Returns [(path, payload_dict)]."""
    out = []
    try:
        sid = int(session_id)
        for entry in sorted(os.listdir(IDRILL_ARM_DIR)):
            p = os.path.join(IDRILL_ARM_DIR, entry)
            try:
                with open(p) as fh:
                    payload = json.load(fh)
            except (OSError, ValueError):
                continue
            if not isinstance(payload, dict):
                continue
            if int(payload.get("session_id", -1) or -1) != sid:
                continue
            if (exercise_name is not None
                    and payload.get("exercise_name") != exercise_name):
                continue
            out.append((p, payload))
    except (OSError, ValueError):
        pass
    return out


def invalidate_arms(session_id, exercise_name=None, dry_run=False):
    """Remove the armed in-place keyboards for this (session[, exercise]).

    ALL arms of the exercise go, not just the deleted set's: an arm bakes a
    literal set_seq into its `cmd` argv and its confirm copy, so once a row
    vanishes every armed continuation of that exercise is prescribing against a
    count that no longer holds -- including the NEXT set's arm, which is the one
    the owner is about to tap. Re-arming is free and deterministic (set-arm
    rewrites the same arm id), so removing too many is cheap and leaving one is
    a wrong write."""
    removed = []
    for path, _payload in arm_files_for(session_id, exercise_name):
        if dry_run or _rm(path):
            removed.append(path)
    return removed


def clear_row_keyboards(session_id, exercise_name=None, dry_run=False):
    """CODE-POSTED KEYBOARDS (2026-10-08): edit the buttons off every live
    set keyboard of this (session[, exercise]) -- the arm files they fire are
    removed above, so a tap would land on nothing -- and release the rows the
    delete removed, so their keyboards can be posted again. Returns
    ["<exercise>:<seq>:<what>"]. Best-effort; a missing module is a no-op."""
    try:
        if HERE not in sys.path:
            sys.path.insert(0, HERE)
        import row_keyboard
    except Exception:  # noqa: BLE001
        return []
    if dry_run:
        return ["%s:%s:would_clear" % (st.get("exercise_name"),
                                       st.get("set_seq"))
                for st in row_keyboard.rows_of(STATE_DIR, session_id)
                if st.get("state") in row_keyboard.OPEN_STATES
                and (not exercise_name
                     or st.get("exercise_name") == exercise_name)]
    out = ["%s:%s:cleared" % (ex, seq) for ex, seq, _prev in
           row_keyboard.clear_rows(STATE_DIR, session_id, exercise_name,
                                   why="undo")]
    out += ["%s:%s:released" % (ex, seq) for ex, seq in
            row_keyboard.release_unlogged(STATE_DIR, session_id,
                                          exercise_name)]
    return out


def cancel_countdown(dry_run=False):
    """Delete the live rest-countdown control file(s). The bridge
    CountdownDriver treats an early file removal as CANCEL, which is exactly the
    semantics wanted: the timer counting down to a set that no longer exists must
    stop on the owner's phone. `.done` files are spent receipts, not live
    controls -- they are left alone."""
    removed = []
    try:
        for entry in sorted(os.listdir(COUNTDOWN_DIR)):
            if entry.startswith("rest-") and entry.endswith(".json"):
                p = os.path.join(COUNTDOWN_DIR, entry)
                if dry_run or _rm(p):
                    removed.append(p)
    except OSError:
        pass
    return removed


def _clear_prefixed(directory, session_id, exercise_name=None, suffix="",
                    dry_run=False):
    """Remove `<sid>.<safe_exercise><suffix>` (or every `<sid>.*` when no
    exercise is given) from a per-session marker dir. Session-scoped by
    construction -- another session's markers are never touched."""
    removed = []
    try:
        if exercise_name is not None:
            names = ["%s.%s%s" % (session_id, safe_token(exercise_name), suffix)]
        else:
            prefix = "%s." % session_id
            names = [n for n in sorted(os.listdir(directory))
                     if n.startswith(prefix)]
        for n in names:
            p = os.path.join(directory, n)
            if os.path.exists(p) and (dry_run or _rm(p)):
                removed.append(p)
    except OSError:
        pass
    return removed


def clear_published(session_id, exercise_name=None, dry_run=False):
    """Drop the 표2 published flag so the corrected table is re-rendered."""
    return _clear_prefixed(PUBLISHED_DIR, session_id, exercise_name,
                           dry_run=dry_run)


def clear_entered(session_id, exercise_name=None, dry_run=False):
    """Drop the entry marker. ONLY exercise-drop / session-abort do this: for a
    single set-undo the exercise WAS still entered, and removing the marker
    would trip set-add's auto-enter recovery and re-publish the whole entry
    payload mid-exercise."""
    return _clear_prefixed(ENTERED_DIR, session_id, exercise_name,
                           dry_run=dry_run)


def clear_override(session_id, exercise_name=None, dry_run=False):
    return _clear_prefixed(OVERRIDE_DIR, session_id, exercise_name,
                           suffix=".json", dry_run=dry_run)


def clear_plate_cue(session_id, exercise_name=None, dry_run=False):
    """The plate cue remembers the LAST CUED WEIGHT to render deltas ('양쪽에
    5kg씩 더'). After a set is removed that memory is a wrong baseline."""
    return _clear_prefixed(PLATE_CUE_DIR, session_id, exercise_name,
                           dry_run=dry_run)


def clear_arm_gen(session_id, dry_run=False):
    removed = []
    p = os.path.join(ARM_GEN_DIR, str(session_id))
    if os.path.exists(p) and (dry_run or _rm(p)):
        removed.append(p)
    return removed


def clear_active_marker(session_id, dry_run=False):
    """Remove .active-session ONLY when it points at THIS session. Clearing
    another session's gate marker would be the `session-cursor clear` defect in
    reverse."""
    if marker_read(ACTIVE_MARKER) != int(session_id):
        return []
    if dry_run or _rm(ACTIVE_MARKER):
        return [ACTIVE_MARKER]
    return []


def stamp_tombstone(session_id, dry_run=False):
    """Stamp .session-closed with the discarded sid (atomic tmp+rename, the
    session-closeout convention).

    THIS IS THE ABORT STATE. See `abort_state_note()`."""
    if dry_run:
        return CLOSED_TOMBSTONE
    try:
        tmp = "%s.tmp.%d" % (CLOSED_TOMBSTONE, os.getpid())
        with open(tmp, "w") as fh:
            fh.write("%d" % int(session_id))
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, CLOSED_TOMBSTONE)
        return CLOSED_TOMBSTONE
    except OSError:
        return None


def abort_state_note():
    """WHY session-abort USES THE .session-closed MARKER AND NOT A NEW
    `workouts.status` COLUMN (i.e. why there is no migration 035).

    1. THERE IS NO ROW LEFT TO HOLD A STATUS. Abort means DISCARD: the workouts
       row is deleted. `status='aborted'` is only meaningful for keep-but-mark,
       which is the wrong semantics for "opened by mistake" -- a mistaken empty
       session left in `workouts` still pollutes workout-find, the day's session
       count, agg_day, and session-closeout's latest-weight-candidate scan. A
       column would be dead weight on a row that no longer exists.
    2. DIRECT IN-CODE PRECEDENT, SAME LIFECYCLE. session-closeout F1 (DGN-801)
       already states it: "workouts has NO status/ended_at column, so 'this
       session is closed' is carried by a marker instead of a schema change
       (ladder rule -- avoid a migration)". Adding a column for `aborted` while
       `closed` stays a marker would give ONE lifecycle TWO representations --
       worse than either choice made consistently.
    3. THE MARKER IS ALREADY A FULL LIFECYCLE CITIZEN, and it carries exactly
       the protection abort needs. set-add's `_mark_active` refuses to revive
       .active-session for a tombstoned sid (the F1 phantom-logging guard), and
       session-open clears the tombstone when it legitimately reuses a session.
       Stamping the aborted sid reuses a proven mechanism for zero new surface.
    4. LOCKSTEP COST IS REAL RIGHT NOW. The live DB is at user_version 33 while
       EXPECTED_USER_VERSION is 34 (034_set_kind staged, not yet applied). A 035
       would widen an already-open landing gap -- to add a column that point 1
       shows is unnecessary.

    The audit trail that a status column would have provided is preserved
    better: session-abort archives the full destroyed rows to
    .discarded/<ts>-session-abort-<sid>.json, so the discard is inspectable AND
    reversible by hand, which `status='aborted'` never was.
    """
    return ("abort = discard: the row is deleted, so there is nothing to hold a "
            "status. The .session-closed tombstone (F1/DGN-801 precedent) "
            "carries the state, and .discarded/ carries the audit trail. No "
            "migration 035.")


def clear_pin_card(dry_run=False):
    """Retire the 표3 종목카드 from the shared dashboard pin by delegating to
    session-closeout.clear_pin_card -- the SoT for that call. Best-effort: a pin
    that will not clear must never fail a delete."""
    if dry_run:
        return False
    try:
        co = load_sibling("session_closeout_for_undo", "session-closeout")
        return bool(co.clear_pin_card())
    except Exception:  # noqa: BLE001 -- cosmetic surface, never blocks a delete
        return False


def invalidate_session_scoped(session_id, exercise_name=None, clear_pin=True,
                              drop_entry=False, dry_run=False, preserve_override=False):
    """One call that invalidates every downstream surface a delete outdates.
    Returns an ordered [(kind, path)] list so the caller can PRINT what it did --
    an invisible cleanup is how the dangling-marker defect happened in the first
    place."""
    done = []
    for p in invalidate_arms(session_id, exercise_name, dry_run):
        done.append(("idrill-arm", p))
    for p in clear_row_keyboards(session_id, exercise_name, dry_run):
        done.append(("row-keyboard", p))
    for p in cancel_countdown(dry_run):
        done.append(("countdown", p))
    for p in clear_published(session_id, exercise_name, dry_run):
        done.append(("set-table-published", p))
    for p in clear_plate_cue(session_id, exercise_name, dry_run):
        done.append(("plate-cue", p))
    if not preserve_override:
        for p in clear_override(session_id, exercise_name, dry_run):
            done.append(("set-arm-override", p))
    if drop_entry:
        for p in clear_entered(session_id, exercise_name, dry_run):
            done.append(("exercise-entered", p))
    if clear_pin:
        done.append(("pin-card", "cleared=%s"
                     % ("yes" if clear_pin_card(dry_run) else "no")))
    return done


# ---------------------------------------------------------------------------
# refusal rendering -- ONE protocol, copied from set-add `_refuse_occupied_seq`
# ---------------------------------------------------------------------------
def fmt_set(row):
    """One stored set as a machine field string."""
    d = dict(zip(SET_COLS, row))
    w = "null" if d["weight_kg"] is None else "%g" % float(d["weight_kg"])
    return ("set_seq=%s,slot=%s,weight=%s,reps=%s,rir=%s"
            % (d["set_seq"], d["slot_num"], w, d["reps"],
               "null" if d["rir"] is None else d["rir"]))


def copy(key, **values):
    import ui_labels
    return ui_labels.i18n(key, **values)


def exercise_label(name):
    return copy("movement." + name) or name.replace("_", " ")


def fmt_set_ko(row):
    """Render the storage bands and null completion taps as owner language."""
    d = dict(zip(SET_COLS, row))
    seq = int(d["set_seq"])
    if seq <= -100:
        label = copy("health.undo.prep", n=-100 - seq + 1)
    elif seq < 0:
        label = copy("health.undo.ramp", n=-seq)
    elif seq == 0:
        label = copy("health.undo.setup")
    else:
        label = copy("health.undo.working", n=seq)
    parts = [label]
    if d["weight_kg"] is not None:
        parts.append("%gkg" % float(d["weight_kg"]))
    parts.append(copy("health.undo.reps", n=d["reps"]) if d["reps"] is not None
                 else copy("health.undo.completed"))
    return " ".join(parts)


def undo_say(exercise_name, target, remaining):
    return copy("health.undo.say", name=exercise_label(exercise_name),
                row=fmt_set_ko(target), remaining=", ".join(
                    fmt_set_ko(r) for r in remaining) or copy("health.undo.empty"))


def correct_surfaces(db_path, session_id, exercise_name, skip_pin=False):
    """Post a correction for invalidated bubbles and refresh from the DB.

    The old messages may already have reached the user; clearing local flags
    cannot retract that claim. Use the existing code delivery, never a relay.
    """
    correction = copy("health.undo.correction", name=exercise_label(exercise_name))
    delivered = False
    try:
        st = load_sibling("set_table_undo", "set-table")
        delivered, _detail = st.deliver_table(correction, session_id, None)
        sa = load_sibling("set_add_undo", "set-add")
        if not skip_pin:
            sa._refresh_card(db_path, session_id, exercise_name)
        sa._publish_table(db_path, sa.DEFAULT_PROGRAM, session_id, exercise_name)
    except Exception as exc:
        print("WARN undo surface refresh failed: %s" % exc, file=sys.stderr)
    print("UNDO_CORRECTION delivered=%s" % ("yes" if delivered else "no"))
    if not delivered:
        print("UNDO_CORRECTION_SAY: " + correction)


def refuse(token, machine_fields, dep_lines, ko_line, why, rerun):
    """THE REFUSAL. NOTHING is written and every stored row is untouched -- that
    is the whole point, and it is stated in the message so a reader never has to
    infer it.

    STDOUT (the channel the model relays, same contract as SET_SEQ_OCCUPIED):
        <TOKEN> k=v k=v ...
          DEP <kind>\t<detail>          -- one line per REFERENCING entity, named
        <TOKEN>_ASK: <one Korean line, verbatim to the owner>
    STDERR (audit / operator, same `ERROR: ` prefix every set-add refusal uses):
        ERROR: <why> ... <the exact re-run>
    Exit 3 (REFUSE_CODE) -- "resolve first", never "it failed".
    """
    print("%s %s" % (token, machine_fields))
    for kind, detail in dep_lines:
        print("  DEP %s\t%s" % (kind, detail))
    print("%s_ASK: %s" % (token, ko_line))
    print("ERROR: %s NOTHING was deleted and every stored row is untouched. "
          "Re-run: %s" % (why, rerun), file=sys.stderr)
    sys.exit(REFUSE_CODE)


def open_db(db_path):
    """Connection with foreign_keys ON (matches kit_life.py's get_conn), so an
    explicit child-then-parent delete and a cascade can never disagree."""
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def resolve_db(arg_db):
    p = os.path.abspath(arg_db or DEFAULT_DB)
    if not os.path.exists(p):
        print("ERROR: db not found: %s" % p, file=sys.stderr)
        sys.exit(1)
    return p
