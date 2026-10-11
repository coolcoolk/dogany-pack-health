#!/usr/bin/env python3
# us_render.py -- US render / delivery / scheduler (DGN-782 R1-R5, D1).
#
# Renders us_step rows into deliverable step content, composes the sequence,
# and auto-emits one step at a time (the scheduler). Pack payload code,
# running as installed kit_core. Interfaces are CLI / file / exit-code only.
#
# Render paths (F1 A+B):
#   R1 matrix_ref     -> verbatim lookup of display_key in the drill/stretch
#                        matrix (NO generation; the cue text is looked up).
#   R2 exercise_derived -> deterministic code-composed target line from the
#                        AX exercise attributes + the step's target/measure.
#   R3 next_hint      -> materialized from seq+1 (absorbs interim F11 next_hint).
#   R4 equipment_need -> flow ordering hint (bodyweight vs equipment).
#   R5 group_id       -> grouped-set (drop/super/giant) bundling.
#
# HOLD (E14): a hold-class us_step (step_type='hold', measure='hold_sec') drives
# per-set START/END + set separation via the sequence itself -- no new schema.
# The step's target carries the hold seconds; render emits a countdown request
# (START) and the sequence's next step is the END/separation. The timer-end ->
# next-step CHAINING depends on the framework's countdown done-marker (C1) -- that ONE
# seam is stubbed in scheduler_advance() (poll <bot_data_dir>/countdown/<id>.done)
# and is the ONLY framework-dependent point; everything else runs without it.
#
# Absorbs interim set-arm F11 (next_hint materialized).
#
# stdlib only.

import os
import sys
import json
import re

import ax_engine as AX


# ---------------------------------------------------------------------------
# Drill / stretch matrix lookup (R1). The matrix is a markdown table shipped in
# the workout skill bundle; the render path does a verbatim key lookup, never a
# generation. The matrix file is optional -- absent => the cue falls back to the
# display_key itself (tolerant, no hard fail on a missing matrix).
# ---------------------------------------------------------------------------
def _matrix_path():
    # payload/database/../skills-bundle/workout-log/stretch-matrix.md, if bundled.
    here = os.path.dirname(os.path.abspath(__file__))
    cand = os.path.normpath(os.path.join(
        here, "..", "skills-bundle", "workout-log", "stretch-matrix.md"))
    if os.path.isfile(cand):
        return cand
    env = os.environ.get("US_MATRIX_PATH")
    if env and os.path.isfile(env):
        return env
    return None


_MATRIX_CACHE = None


def _load_matrix():
    """Parse the drill/stretch matrix into {key: cue}. The matrix is a markdown
    doc; we index bolded/keyed rows of form `key | cue` or `**key**: cue`. Best
    effort, verbatim -- unknown format lines are skipped."""
    global _MATRIX_CACHE
    if _MATRIX_CACHE is not None:
        return _MATRIX_CACHE
    out = {}
    p = _matrix_path()
    if p:
        with open(p, "r", encoding="utf-8") as f:
            for line in f:
                # markdown table row: | key | cue | ...
                if line.count("|") >= 2:
                    cells = [c.strip() for c in line.strip().strip("|").split("|")]
                    if len(cells) >= 2 and cells[0] and cells[0].lower() not in (
                            "key", "name", "---", ":---") and not set(
                            cells[0]) <= set("-: "):
                        out.setdefault(cells[0], cells[1])
                # `**key**: cue`
                m = re.match(r"^\*\*(.+?)\*\*\s*[:\-]\s*(.+)$", line.strip())
                if m:
                    out.setdefault(m.group(1).strip(), m.group(2).strip())
    _MATRIX_CACHE = out
    return out


def render_matrix_ref(step):
    """R1: verbatim lookup of the step's display_key in the drill matrix."""
    key = step["display_key"]
    matrix = _load_matrix()
    cue = matrix.get(key)
    if cue is None:
        cue = key  # tolerant fallback: emit the key itself
    return {"render": "matrix_ref", "key": key, "cue": cue}


def render_exercise_derived(conn, step):
    """R2: deterministic code-composed target line from AX attributes + target.
    No LLM: name + measure + target string, plus tempo/hold when carried."""
    ex = conn.execute("SELECT * FROM ax_exercise WHERE ulid=?;",
                      (step["exercise_ref"],)).fetchone()
    # The owner-facing name: the card's `display` (Korean), which program-init
    # stamps into display_key when it derives the row. Rows seeded without one
    # (legacy us_reseed) fall back to the catalog key -- display-name rule B4.
    key_name = ex["exercise_name"] if ex is not None else "?"
    name = step["display_key"] or key_name
    measure = step["measure"]
    target = step["target"]
    parts = [name]
    if measure == "reps" and target:
        parts.append("x%s reps" % target)
    elif measure == "hold_sec" and target:
        # hold targets are stored "20-45s" already; never print "20-45ss".
        parts.append("hold %s" % (target if str(target).endswith("s")
                                  else "%ss" % target))
    elif measure == "tempo" and target:
        parts.append("tempo %s" % target)
    elif target:
        parts.append(str(target))
    if ex is not None and ex["tempo"] and measure != "tempo":
        parts.append("(tempo %s)" % ex["tempo"])
    return {"render": "exercise_derived", "line": " ".join(parts),
            "name": name, "exercise_name": key_name, "measure": measure,
            "target": target}


def render_step(conn, step):
    """R1/R2 dispatch on display_source. Returns the deliverable content dict
    plus R4 equipment flag and R5 group bundling."""
    if step["display_source"] == "matrix_ref":
        body = render_matrix_ref(step)
    else:
        body = render_exercise_derived(conn, step)
    body.update({
        "ulid": step["ulid"],
        "seq": step["seq"],
        "step_type": step["step_type"],
        "equipment_need": step["equipment_need"],   # R4 flow order
        "group_id": step["group_id"],               # R5 grouped set
        "rest_sec": step["rest_sec"],
        "suppress_alert": step["suppress_alert"],
        "next_hint": step["next_hint"],             # R3 materialized
        "is_hold": step["step_type"] == "hold",     # E14 hold class
        "hold_sec": step["target"] if step["step_type"] == "hold" else None,
    })
    return body


# ---------------------------------------------------------------------------
# R3: next_hint materialization. Absorbs interim set-arm F11: the hint is the
# seq+1 step in the same session, derived at sequence-build (self-refreshes on
# re-sequence). This writes next_hint on every step of a session.
# ---------------------------------------------------------------------------
def materialize_next_hint(conn, session_ref, write=True):
    """R3/F11: fill each step's next_hint from the seq+1 step's rendered short
    label. Returns the ordered list of (ulid, next_hint). Deterministic, no LLM.
    Self-refresh: recomputes from the current sequence every call."""
    steps = conn.execute(
        "SELECT * FROM us_step WHERE session_ref=? ORDER BY seq ASC;",
        (session_ref,)).fetchall()
    hints = []
    for i, step in enumerate(steps):
        if i + 1 < len(steps):
            nxt = steps[i + 1]
            rendered = render_step(conn, nxt)
            label = rendered.get("line") or rendered.get("cue") or (
                "seq %d" % nxt["seq"])
            hint = "NEXT: %s" % label
        else:
            hint = "NEXT: (session end)"
        hints.append((step["ulid"], hint))
        if write:
            conn.execute("UPDATE us_step SET next_hint=? WHERE ulid=?;",
                         (hint, step["ulid"]))
    if write:
        conn.commit()
    return hints


# ---------------------------------------------------------------------------
# Sequence composition + scheduler (D1). The scheduler auto-emits ONE step at a
# time in seq order. Emission = render the current step + (for hold/rest steps)
# arm the countdown; the NEXT emission is gated on the timer-end done-marker.
# ---------------------------------------------------------------------------
def compose_sequence(conn, session_ref):
    """D1: render the whole session sequence in seq order (composition view).
    Also (re)materializes next_hint so R3 is consistent with the sequence."""
    materialize_next_hint(conn, session_ref, write=True)
    steps = conn.execute(
        "SELECT * FROM us_step WHERE session_ref=? ORDER BY seq ASC;",
        (session_ref,)).fetchall()
    return [render_step(conn, s) for s in steps]


def _cursor_path(session_ref, state_dir=None):
    """Scheduler cursor file: which seq was last emitted for a session. File-
    based state (no schema) so the scheduler survives across process calls."""
    d = state_dir or os.environ.get(
        "US_STATE_DIR", os.path.join(os.path.expanduser("~"), ".dogany",
                                     "us-sched"))
    os.makedirs(d, exist_ok=True)
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", str(session_ref))
    return os.path.join(d, "cursor-%s.json" % safe)


def _read_cursor(session_ref, state_dir=None):
    p = _cursor_path(session_ref, state_dir)
    if os.path.isfile(p):
        try:
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {"last_seq": None}
    return {"last_seq": None}


def _write_cursor(session_ref, cur, state_dir=None):
    p = _cursor_path(session_ref, state_dir)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(cur, f)


def _parse_hold_seconds(target):
    """Parse a hold-step target into integer seconds for the countdown timer.
    Accepts plain seconds ("45", "45s") or a range ("20-45s"). For a range we
    arm the UPPER bound so the timer covers the full hold window (the user can
    end early via the done signal). Returns 0 if unparseable."""
    if target is None:
        return 0
    s = str(target).strip().lower().rstrip("s").strip()
    if not s:
        return 0
    if "-" in s:
        nums = []
        for part in s.split("-"):
            part = part.strip()
            try:
                nums.append(float(part))
            except ValueError:
                pass
        return int(max(nums)) if nums else 0
    try:
        return int(float(s))
    except ValueError:
        return 0


def scheduler_emit_next(conn, session_ref, state_dir=None):
    """D1: emit the NEXT step after the cursor (one step at a time). Returns the
    rendered step dict, or {"done": True} at end of sequence. Advances the
    cursor. A hold/rest step's emission includes a countdown-arm request
    (countdown_request) that the delivery layer writes to the bridge channel."""
    cur = _read_cursor(session_ref, state_dir)
    last = cur.get("last_seq")
    if last is None:
        row = conn.execute(
            "SELECT * FROM us_step WHERE session_ref=? ORDER BY seq ASC "
            "LIMIT 1;", (session_ref,)).fetchone()
    else:
        row = conn.execute(
            "SELECT * FROM us_step WHERE session_ref=? AND seq>? "
            "ORDER BY seq ASC LIMIT 1;", (session_ref, last)).fetchone()
    if row is None:
        return {"done": True, "session_ref": session_ref}
    rendered = render_step(conn, row)
    # E14 hold: emit a countdown-arm request for hold seconds; the set END is
    # the sequence's next step (set separation via the sequence, no new schema).
    countdown_req = None
    if row["step_type"] == "hold" and row["target"]:
        hold_s = _parse_hold_seconds(row["target"])
        if hold_s > 0:
            countdown_req = {
                "id": "%s-seq%d" % (session_ref, row["seq"]),
                "seconds": hold_s,
                "label": rendered.get("line") or rendered.get("cue") or "hold",
                "cadence": "hold",
            }
    elif row["rest_sec"]:
        countdown_req = {
            "id": "%s-seq%d-rest" % (session_ref, row["seq"]),
            "seconds": int(row["rest_sec"]),
            "label": "rest",
            "cadence": "rest",
        }
    cur["last_seq"] = row["seq"]
    _write_cursor(session_ref, cur, state_dir)
    return {
        "done": False,
        "session_ref": session_ref,
        "step": rendered,
        "suppress_alert": bool(row["suppress_alert"]),   # F8: prep steps mute
        "countdown_request": countdown_req,              # D3 timer display arm
    }


# ---------------------------------------------------------------------------
# FRAMEWORK DONE-MARKER SEAM (C1 / D4) -- the ONLY framework-dependent point.
# The bridge (framework) will emit <bot_data_dir>/countdown/<id>.done on natural
# timer end (distinct from cancel = file delete). Until that lands, this poll is
# STUBBED and clearly isolated: scheduler_advance() consumes the marker if it
# exists (real chaining), else reports "waiting" so the caller degrades to the
# interim polling path. NOTHING else in the engine depends on this.
# ---------------------------------------------------------------------------
def _countdown_dir():
    return os.environ.get(
        "COUNTDOWN_DIR",
        os.path.join(os.path.expanduser("~"), ".dogany", "countdown"))


def done_marker_path(countdown_id):
    return os.path.join(_countdown_dir(), "%s.done" % countdown_id)


def check_done_marker(countdown_id):
    """STUB SEAM (framework C1 pending): return True iff the bridge has written the
    natural-end marker <id>.done. Returns False when the marker is absent
    (timer still running OR marker feature not yet shipped). This is the single
    process-boundary consume point; the bridge emit is the framework's."""
    return os.path.isfile(done_marker_path(countdown_id))


def consume_done_marker(countdown_id):
    """After chaining on a done marker, delete it (contract C1: pack consumes
    then deletes). No-op if absent."""
    p = done_marker_path(countdown_id)
    try:
        if os.path.isfile(p):
            os.remove(p)
            return True
    except OSError:
        pass
    return False


def scheduler_advance(conn, session_ref, countdown_id, state_dir=None):
    """D4 chaining: advance to the next step ONLY when the timer's done marker
    is present (framework C1). If the marker is absent, return {"waiting": True}
    (the caller/interim path may re-poll). This isolates the one framework seam:
    remove this gate and the scheduler still emits on explicit next calls."""
    if not check_done_marker(countdown_id):
        return {"waiting": True, "countdown_id": countdown_id,
                "note": "done-marker absent (framework C1 pending or timer live)"}
    consume_done_marker(countdown_id)
    return scheduler_emit_next(conn, session_ref, state_dir)
