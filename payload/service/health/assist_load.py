#!/usr/bin/env python3
"""assist_load.py -- ONE home for the ASSIST-MACHINE load inversion.

WHY THIS FILE EXISTS
--------------------
On an assist machine (chin-up / pull-up assist stack) `workout_sets.weight_kg`
is not the load the owner moved -- it is the COUNTERWEIGHT the machine gave
back. The axis is INVERTED: a BIGGER number is an EASIER set, and progress is
the number going DOWN.

`rx-calc.apply_progression` already reads the slot's `assisted:` flag and flips
the progression direction. Nothing else did. So two families of derived numbers
were wrong for every assisted set ever logged:

  volume    `weight_kg * reps` made a genuine assist REDUCTION look like a
            volume CRASH -- which the strategy-B engine reads as a
            performance drop and answers with a hold or an early deload.
  top set   `MAX(weight_kg)` picked the set with the MOST assistance, i.e.
            the EASIEST set, and handed its rep count to the progression
            arithmetic as if it were the hardest.

Owner's rulings (2026-08-22 volume, 2026-09-01 recompute-history, and the
top-set direction derived from "less assist = progress"):

  volume of an assisted set = (bodyweight_at_the_time - counterweight) * reps
  top set of an assisted exercise = the set with the LOWEST counterweight
  the DISPLAYED number stays the raw stack weight (owner, 2026-08-22)

WHAT IS AN ASSISTED EXERCISE
----------------------------
Two declared sources, unioned. Neither is a hardcoded exercise name:

  1. `ax_machine.loading_method = 'assisted'` reached through
     `ax_exercise.machine_ref`. This is the DB-side truth and it is the only
     source that covers HISTORY -- exercises that have since left program.yaml
     (measured: `pullup`, 10 sets, same assist machine as `chinup`) still
     resolve here. `set-table._is_assist_loaded` already reads exactly this.
  2. program.yaml slots carrying `assisted: true`. This is the truth for the
     PRESCRIPTION side and is what rx-calc already reads.

BODYWEIGHT AT THE TIME
----------------------
`metric_log` rows with `metric = 'weight_kg'` (measured: 12 readings covering
2026-06-30..2026-09-01; every assisted set in the live DB has a reading within
7 days). Resolution is CARRY-FORWARD -- the last reading on or before the set's
session date -- so a past set's volume never moves when a NEW weigh-in lands.
A set that predates every reading falls back to the earliest one.

No bodyweight at all -> the assisted set is UNMEASURABLE, not zero. Python
returns None and the SQL expression yields NULL, so such a set drops out of a
SUM exactly like a NULL weight_kg row already does. Substituting a constant
would be inventing a number about the owner's body.

DEGRADATION
-----------
Every lookup is guarded. Missing `ax_machine` / `ax_exercise` / `metric_log`
(an instance without that history, a fresh DB) -> the assisted set is EMPTY -> every helper
here returns the pre-existing arithmetic byte-for-byte. Non-assisted exercises
never take a different code path.
"""

import sqlite3

__all__ = [
    "context",
    "reset_cache",
    "volume_sql",
    "AssistContext",
    "assisted_names",
    "bodyweight_at",
    "effective_load",
    "set_volume",
    "top_set_key",
    "pick_top_set",
    "effective_load_sql",
    "top_weight_sql",
]

# metric_log key for scale bodyweight. Same string health_metrics.py reads.
BODYWEIGHT_METRIC = "weight_kg"

# ax_machine.loading_method value that marks an assist stack. Same string
# set-table._is_assist_loaded gates on -- one vocabulary, one spelling.
ASSISTED_LOADING_METHOD = "assisted"


# ---------------------------------------------------------------------------
# declared sources
# ---------------------------------------------------------------------------

def assisted_names(db_path=None, program=None):
    """frozenset of exercise names whose load axis is INVERTED.

    Union of the two declared sources (see module docstring). Any read failure
    contributes nothing rather than raising -- a gate miss must never break a
    card, and an empty set restores the exact pre-fix behaviour."""
    names = set()
    if db_path:
        try:
            conn = sqlite3.connect(db_path)
            try:
                names.update(r[0] for r in conn.execute(
                    "SELECT e.exercise_name FROM ax_exercise e "
                    "JOIN ax_machine m ON m.ulid = e.machine_ref "
                    "WHERE e.status = 'active' AND m.loading_method = ?",
                    (ASSISTED_LOADING_METHOD,)) if r[0])
            finally:
                conn.close()
        except Exception:      # noqa: BLE001 -- degrade to the other source
            pass
    if isinstance(program, dict):
        for day_plan in (program.get("days") or {}).values():
            for ex in ((day_plan or {}).get("exercises") or []):
                if isinstance(ex, dict) and ex.get("assisted") and ex.get("name"):
                    names.add(ex["name"])
    return frozenset(names)


def bodyweight_series(db_path):
    """[(date, kg)] ascending by date, or [] when unavailable."""
    try:
        conn = sqlite3.connect(db_path)
        try:
            return [(r[0], float(r[1])) for r in conn.execute(
                "SELECT date, value FROM metric_log WHERE metric = ? "
                "AND value IS NOT NULL ORDER BY date ASC",
                (BODYWEIGHT_METRIC,)) if r[0] is not None]
        finally:
            conn.close()
    except Exception:          # noqa: BLE001 -- no series -> unmeasurable
        return []


def bodyweight_at(series, date):
    """Carry-forward bodyweight for `date`: the last reading on or before it,
    else the earliest reading. None when there is no reading at all."""
    if not series:
        return None
    if not date:
        return series[-1][1]
    prior = [kg for d, kg in series if d <= date]
    return prior[-1] if prior else series[0][1]


# ---------------------------------------------------------------------------
# context -- resolve the declared sources ONCE per run, not per set
# ---------------------------------------------------------------------------

class AssistContext(object):
    """Cached assisted-name set + bodyweight series + session-date lookup.

    Build one per command run and hand it down; every helper below accepts
    None and then behaves like "nothing is assisted", which is the pre-fix
    arithmetic."""

    def __init__(self, db_path=None, program=None):
        self.db_path = db_path
        self.names = assisted_names(db_path, program)
        self.series = bodyweight_series(db_path) if self.names else []
        self._session_date = {}

    def is_assisted(self, exercise_name):
        return exercise_name in self.names

    def session_date(self, session_id):
        """`workouts.date` for a session id, cached. None on any miss."""
        if session_id in self._session_date:
            return self._session_date[session_id]
        date = None
        if self.db_path is not None and session_id is not None:
            try:
                conn = sqlite3.connect(self.db_path)
                try:
                    row = conn.execute(
                        "SELECT date FROM workouts WHERE id = ?",
                        (session_id,)).fetchone()
                finally:
                    conn.close()
                date = row[0] if row else None
            except Exception:  # noqa: BLE001
                date = None
        self._session_date[session_id] = date
        return date

    def bodyweight(self, date):
        return bodyweight_at(self.series, date)


# ---------------------------------------------------------------------------
# the arithmetic
# ---------------------------------------------------------------------------

def effective_load(ctx, exercise_name, weight_kg, date=None):
    """The load the owner ACTUALLY moved, in kg.

    Non-assisted -> `weight_kg` unchanged (identity; this is the regression
    guarantee). Assisted -> bodyweight_at(date) - counterweight, floored at 0.
    None when the value is unmeasurable (no weight logged, or an assisted set
    with no bodyweight reading anywhere) -- callers treat None the way they
    already treat a NULL weight_kg: skip the set, never substitute 0."""
    if weight_kg is None:
        return None
    if ctx is None or not ctx.is_assisted(exercise_name):
        return float(weight_kg)
    bw = ctx.bodyweight(date)
    if bw is None:
        return None
    return max(float(bw) - float(weight_kg), 0.0)


def set_volume(ctx, exercise_name, weight_kg, reps, date=None):
    """Volume load of ONE set. None = unmeasurable (see effective_load)."""
    load = effective_load(ctx, exercise_name, weight_kg, date)
    if load is None or reps is None:
        return None
    return load * float(reps)


def top_set_key(ctx, exercise_name):
    """key= function selecting the HARDEST set from an iterable of rows.

    Works on anything exposing (weight, reps) -- pass an accessor pair. The
    assisted branch orders on the NEGATED counterweight, which is the same
    ordering as effective load (bodyweight is a constant within a session) and
    needs no bodyweight reading to be correct."""
    invert = ctx is not None and ctx.is_assisted(exercise_name)

    def key(weight, reps):
        w = 0.0 if weight is None else float(weight)
        return (-w if invert else w, reps or 0)
    return key


def pick_top_set(ctx, exercise_name, rows, weight_of, reps_of):
    """The hardest set in `rows`, or None when `rows` is empty."""
    rows = list(rows)
    if not rows:
        return None
    key = top_set_key(ctx, exercise_name)
    return max(rows, key=lambda r: key(weight_of(r), reps_of(r)))


# ---------------------------------------------------------------------------
# SQL -- for the consumers that aggregate inside the DB
# ---------------------------------------------------------------------------
# Built as expression STRINGS so a caller can drop them into an existing
# SELECT without restructuring the query. They are self-contained: they need
# only the workout_sets alias, and they resolve the session date themselves
# (not every caller joins `workouts`).

_ASSISTED_PRED = (
    "EXISTS (SELECT 1 FROM ax_exercise _ae "
    "        JOIN ax_machine _am ON _am.ulid = _ae.machine_ref "
    "        WHERE _ae.exercise_name = {a}.exercise_name "
    "          AND _ae.status = 'active' "
    "          AND _am.loading_method = '%s')" % ASSISTED_LOADING_METHOD
)

# Carry-forward bodyweight for the set's session date, else the earliest
# reading. NULL when metric_log holds no bodyweight at all -- and NULL then
# propagates through the subtraction so SUM() skips the set, which is exactly
# the Python side's None.
_BODYWEIGHT_AT = (
    "COALESCE("
    " (SELECT _ml.value FROM metric_log _ml "
    "   WHERE _ml.metric = '%(m)s' AND _ml.value IS NOT NULL "
    "     AND _ml.date <= (SELECT _w.date FROM workouts _w "
    "                       WHERE _w.id = {a}.session_id) "
    "   ORDER BY _ml.date DESC LIMIT 1),"
    " (SELECT _ml.value FROM metric_log _ml "
    "   WHERE _ml.metric = '%(m)s' AND _ml.value IS NOT NULL "
    "   ORDER BY _ml.date ASC LIMIT 1))" % {"m": BODYWEIGHT_METRIC}
)


def _tables_present(db_path, tables):
    """True iff every named table exists. A missing table means this DB cannot
    express the inversion, so the caller must keep the plain formula."""
    try:
        conn = sqlite3.connect(db_path)
        try:
            have = {r[0] for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type IN ('table','view')")}
        finally:
            conn.close()
    except Exception:          # noqa: BLE001
        return False
    return all(t in have for t in tables)


def effective_load_sql(db_path, alias="ws"):
    """SQL scalar expression for one row's effective load.

    Degrades to the plain `COALESCE(alias.weight_kg, 0)` when this DB has no
    assist taxonomy or no bodyweight series -- byte-identical to the pre-fix
    query text in that case."""
    if not _tables_present(db_path, ("ax_exercise", "ax_machine",
                                     "metric_log", "workouts")):
        return "COALESCE({a}.weight_kg, 0)".format(a=alias)
    return (
        "CASE WHEN " + _ASSISTED_PRED + " "
        "THEN MAX(" + _BODYWEIGHT_AT + " - COALESCE({a}.weight_kg, 0), 0) "
        "ELSE COALESCE({a}.weight_kg, 0) END"
    ).format(a=alias)


def volume_sql(db_path, alias="ws"):
    """SQL scalar expression for one row's volume load (effective x reps)."""
    return "(%s) * %s.reps" % (effective_load_sql(db_path, alias), alias)


def top_weight_sql(db_path, alias="ws", assisted=None):
    """Aggregate expression picking the HARDEST set's RAW STACK weight.

    The value stays the raw stack number (owner: display keeps stack weight);
    only WHICH set wins changes. `assisted` may be passed when the caller has
    already resolved it (query grouped on one exercise); otherwise the
    per-group predicate decides.

    No COALESCE: MIN/MAX both skip NULLs and both return NULL when every row
    is NULL, which is the calibration signal callers already branch on. Adding
    a 0 default here would turn "no weight logged" into "0 kg"."""
    if assisted is True:
        return "MIN({a}.weight_kg)".format(a=alias)
    if assisted is False or not _tables_present(db_path, ("ax_exercise",
                                                          "ax_machine")):
        return "MAX({a}.weight_kg)".format(a=alias)
    return ("CASE WHEN " + _ASSISTED_PRED + " "
            "THEN MIN({a}.weight_kg) "
            "ELSE MAX({a}.weight_kg) END").format(a=alias)


# ---------------------------------------------------------------------------
# per-run cache -- the declared sources are read once, not once per set
# ---------------------------------------------------------------------------

_CTX_CACHE = {}


def context(db_path=None, program=None):
    """Cached AssistContext for `db_path`.

    Callers that also hold the parsed program.yaml may pass it; its
    `assisted: true` slots are merged into the cached name set. Every consumer
    in this tree runs as a short-lived command, so a process-lifetime cache is
    the whole lifetime of one answer."""
    ctx = _CTX_CACHE.get(db_path)
    if ctx is None:
        ctx = AssistContext(db_path, program)
        _CTX_CACHE[db_path] = ctx
        return ctx
    if program is not None:
        extra = assisted_names(None, program) - ctx.names
        if extra:
            ctx.names = frozenset(ctx.names | extra)
            if not ctx.series:
                ctx.series = bodyweight_series(db_path)
    return ctx


def reset_cache():
    """Drop the cache. Tests that rebuild a DB between cases need this."""
    _CTX_CACHE.clear()
