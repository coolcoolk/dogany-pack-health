#!/usr/bin/env python3
"""Deterministic applicability-refraction engine (DGN-172, from DGN-119 design A).

WHAT THIS IS
------------
Refraction turns a general knowledge item ("~1.4-2.0 g/kg/day protein") into a
statement about THIS user ("for your measured 80 kg: ~112-160 g/day"). The split
that is the spine of the design (DGN-119): DETERMINISM lives here, JUDGEMENT
(phrasing, whether to ask) lives in the model. This file NEVER lets the model
compute a number. Every number in the output is either copied from item data or
produced by a deterministic op over item data + a resolved user axis value.

The model calls refract() and speaks the result. It does not do arithmetic.

AXIS RESOLUTION PRECEDENCE (DGN-119)
------------------------------------
measured (kit_life.db, via the LifekitAdapter interface) > stated (profile_axes
KV). Prose memory is NEVER machine-parsed here (if injected, the main agent
confirms then sets profile_axes -- out of scope for this engine).

OPERATIONS (exactly three, DGN-119)
-----------------------------------
  RESCALE      -- role=scale numeric axis: multiply/format a per-unit item
                  number by the user's measured/stated value (the ONLY place a
                  new number is produced, and it is pure arithmetic on data).
  REFRAME      -- role=soft mismatch: keep the number, attach a curated
                  refraction_note (each note carries its own grade) as a hedge.
  EXCLUDE_SWAP -- role=hard mismatch: withdraw the specific claim / route around
                  it. For a SAFETY hard axis that is unknown/refused this becomes
                  block_specifics (general info + mechanism stay, specific numbers
                  and any green-light are withheld -- NOT silence).

NEED PROTOCOL (DGN-119)
-----------------------
A missing axis does not block the answer. refract() reports needed-but-missing
axes with their data-sourced baseline_text; the answer path (DGN-175) speaks the
stated-baseline answer FIRST, then may ask per the question budget. Refused /
unknown rows are recorded (dedup: never re-ask a refused axis); volatile axes are
re-askable only after max_age_days.

DETERMINISM CONTRACT
--------------------
refract() takes ALL time-varying inputs as arguments (the caller passes `now`
and the resolved axis values). Given the same item + same axis values it returns
a byte-identical structure. No ambient clock, no network, no randomness.

Python 3 stdlib only. Shares the warehouse core (kimwog.py) for the YAML subset
parser and the axes ledger loader.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import kimwog  # noqa: E402  (warehouse core: parser, ledger loader)


# ==========================================================================
# Axes ledger view (framework-owned; refract.py is the resolution authority)
# ==========================================================================

class Ledger:
    """A resolved, queryable view over axes.yaml. Owns the tiering fields the
    engine needs at refraction time: source, type, volatility, safety flag,
    baseline_text, and alias redirection."""

    def __init__(self, axes_data):
        self._by_name = {}
        self.aliases = dict((axes_data.get("aliases") or {}).items())
        for tier in ("core", "pack"):
            for row in (axes_data.get(tier) or []):
                name = row.get("name")
                if name:
                    self._by_name[name] = dict(row)

    @classmethod
    def from_root(cls, root):
        return cls(kimwog.load_axes(root))

    def canonical(self, key):
        """Resolve an alias to its canonical axis name. Unknown keys pass
        through unchanged (the caller/lint decides they are off-ledger)."""
        seen = set()
        cur = key
        while cur in self.aliases and cur not in seen:
            seen.add(cur)
            cur = self.aliases[cur]
        return cur

    def spec(self, key):
        """Return the ledger row for an axis (alias-resolved), or None."""
        return self._by_name.get(self.canonical(key))

    def is_safety(self, key):
        spec = self.spec(key)
        return bool(spec and spec.get("safety") is True)

    def source(self, key):
        spec = self.spec(key)
        return spec.get("source") if spec else None

    def volatility(self, key):
        """Return 'stable' or an int max_age_days (None if unknown axis)."""
        spec = self.spec(key)
        if not spec:
            return None
        vol = spec.get("volatility")
        if vol == "stable":
            return "stable"
        try:
            return int(vol)
        except (TypeError, ValueError):
            return None

    def baseline_text(self, key):
        spec = self.spec(key)
        return spec.get("baseline_text") if spec else None


# ==========================================================================
# Lifekit adapter interface + fixture (DGN-174 wires the real db here)
# ==========================================================================

class LifekitAdapter:
    """Interface a measured-axis source must satisfy. DGN-174 provides the real
    implementation over the live kit_life.db (through database/kit_life.py, never
    a raw connection). refract.py depends ONLY on this contract.

    CONTRACT
    --------
    get(axis_name, now) -> AxisValue | None
        Return the most recent MEASURED value for `axis_name` as an AxisValue
        whose .measured_at is the ISO date the measurement was taken, or None if
        the source holds no measurement for that axis. `now` is passed in for
        determinism (the adapter must not read an ambient clock); an adapter may
        use it to bound "recent", but MUST NOT fabricate a value.

    The adapter answers ONLY kit_life-sourced axes (ledger source: kit_life).
    Stated axes (source: profile) are never routed here. An adapter that cannot
    answer an axis returns None -- refraction then treats it as missing and the
    Need protocol applies. The adapter NEVER computes a derived number; it
    returns a stored measurement. Any scaling arithmetic is refract()'s RESCALE.
    """

    def get(self, axis_name, now):  # pragma: no cover - interface
        raise NotImplementedError


class DictLifekitAdapter(LifekitAdapter):
    """A fixture adapter over an in-memory dict. Used by the tests and any
    caller that already has measured values in hand (no db). The dict maps
    axis_name -> {"value": <v>, "measured_at": "YYYY-MM-DD"}."""

    def __init__(self, table):
        self._table = dict(table or {})

    def get(self, axis_name, now):
        row = self._table.get(axis_name)
        if row is None:
            return None
        return AxisValue(
            value=row.get("value"),
            source="measured",
            measured_at=row.get("measured_at"),
        )


class SqliteLifekitAdapter(LifekitAdapter):
    """Fixture adapter over a sqlite db shaped like kit_life's metric_log table
    (date TEXT, metric TEXT, value REAL). Used ONLY against the sandbox FIXTURE
    db in tests -- it NEVER touches a live kit_life.db. DGN-174 will replace this
    with an adapter that goes through database/kit_life.py's official accessors
    (mapping axis names -> kit_life metrics / aggregates), not raw SQL.

    metric_axis_map lets a warehouse map ledger axis names onto kit_life metric
    rows (e.g. body_weight_kg -> metric 'weight'). Identity by default.
    """

    def __init__(self, db_path, metric_axis_map=None):
        import sqlite3
        self._sqlite3 = sqlite3
        self._db_path = db_path
        self._map = dict(metric_axis_map or {})

    def get(self, axis_name, now):
        metric = self._map.get(axis_name, axis_name)
        conn = self._sqlite3.connect(self._db_path)
        try:
            cur = conn.execute(
                "SELECT value, date FROM metric_log WHERE metric=? "
                "ORDER BY date DESC LIMIT 1;", (metric,))
            row = cur.fetchone()
        finally:
            conn.close()
        if row is None:
            return None
        return AxisValue(value=row[0], source="measured", measured_at=row[1])


class AxisValue:
    """A single resolved axis value with provenance."""
    __slots__ = ("value", "source", "measured_at", "as_of")

    def __init__(self, value, source, measured_at=None, as_of=None):
        self.value = value            # the axis value (number / string / bool)
        self.source = source          # "measured" | "stated"
        self.measured_at = measured_at  # ISO date for measured values
        self.as_of = as_of            # ISO date a stated value was set/confirmed

    def as_dict(self):
        return {"value": self.value, "source": self.source,
                "measured_at": self.measured_at, "as_of": self.as_of}


# ==========================================================================
# Axis resolution: measured (kit_life) > stated (profile_axes)
# ==========================================================================

def resolve_axis(key, ledger, adapter, profile_axes, now):
    """Resolve one axis to an AxisValue or None (missing), honoring precedence.

    profile_axes: dict axis_name -> {"value":..., "as_of":"YYYY-MM-DD",
                                      "status":"set|refused|unknown"}. A refused
    or unknown row resolves to None-value but its status is surfaced by the
    caller (need protocol) -- resolve_axis returns None for those so refraction
    treats the axis as unavailable; the Need layer reads profile_axes directly
    for the status.

    Precedence: if the ledger says the axis is kit_life-sourced, ask the adapter
    FIRST; only fall back to a stated value if the adapter has none.
    """
    canon = ledger.canonical(key)
    src = ledger.source(canon)
    # measured first when the ledger routes this axis to kit_life
    if src == "kit_life" and adapter is not None:
        measured = adapter.get(canon, now)
        if measured is not None and measured.value is not None:
            return measured
    # stated fallback (profile_axes)
    row = (profile_axes or {}).get(canon)
    if isinstance(row, dict) and row.get("status", "set") == "set" \
            and row.get("value") is not None:
        return AxisValue(value=row.get("value"), source="stated",
                         as_of=row.get("as_of"))
    return None


# ==========================================================================
# Deterministic ops
# ==========================================================================

def _fmt_num(x):
    """Format a number for output without floating cruft, deterministically."""
    if isinstance(x, bool):
        return str(x)
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float):
        if x == int(x):
            return str(int(x))
        # fixed, stable repr: strip trailing zeros but keep determinism
        s = ("%.6f" % x).rstrip("0").rstrip(".")
        return s
    return str(x)


def _as_float(x):
    """Coerce a value to float, or None. The YAML-subset parser yields numeric
    scalars as strings, so per-unit item numbers arrive as "1.4"; coerce here so
    the arithmetic is always numeric (and non-numbers never silently multiply)."""
    if x is None:
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def op_rescale(axis_key, per_unit_low, per_unit_high, user_value):
    """RESCALE: the only op that produces a new number, by pure arithmetic on
    data. Multiplies a per-unit item range by the user's measured/stated value.
    Returns a structured op record with the computed absolute range."""
    v = _as_float(user_value)
    if v is None:
        return None
    lo = _as_float(per_unit_low)
    hi = _as_float(per_unit_high)
    low = lo * v if lo is not None else None
    high = hi * v if hi is not None else None
    return {
        "op": "RESCALE",
        "axis": axis_key,
        "user_value": user_value,
        "per_unit_low": lo,
        "per_unit_high": hi,
        "result_low": low,
        "result_high": high,
        "result_text": _rescale_text(low, high),
    }


def _rescale_text(low, high):
    if low is None and high is None:
        return None
    if high is None:
        return _fmt_num(low)
    if low is None:
        return _fmt_num(high)
    return "%s-%s" % (_fmt_num(low), _fmt_num(high))


def op_reframe(axis_key, note_text, note_grade):
    """REFRAME: soft mismatch -> keep the number, attach a graded hedge note.
    The number does not change (DGN-119: no note -> hedge only, number fixed)."""
    return {
        "op": "REFRAME",
        "axis": axis_key,
        "note": note_text,
        "note_grade": note_grade,
    }


def op_exclude_swap(axis_key, reason):
    """EXCLUDE_SWAP: hard mismatch -> withdraw/route around the specific claim."""
    return {
        "op": "EXCLUDE_SWAP",
        "axis": axis_key,
        "reason": reason,
    }


# ==========================================================================
# refract(): the deterministic entry point
# ==========================================================================

class RefractionResult:
    """Structured output. Every number here traces to item data or a RESCALE
    over item data + a resolved axis value. The model reads this and speaks it;
    it computes nothing."""

    def __init__(self):
        self.item_id = None
        self.ops = []               # applied deterministic ops (RESCALE/REFRAME/EXCLUDE_SWAP)
        self.block_specifics = False  # true when a safety axis gate fired
        self.blocked_axes = []      # safety axes that fired block_specifics
        self.axes_used = []         # {key, source, value, measured_at/as_of}
        self.needed_missing = []    # {key, safety, baseline_text, volatility, reask_ok}
        self.notes = []             # curated refraction_notes surfaced (with grades)

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "block_specifics": self.block_specifics,
            "blocked_axes": list(self.blocked_axes),
            "ops": list(self.ops),
            "axes_used": list(self.axes_used),
            "needed_missing": list(self.needed_missing),
            "notes": list(self.notes),
        }


def _profile_status(profile_axes, canon):
    """Return the recorded status for an axis ('set'|'refused'|'unknown') or
    None if there is no row at all."""
    row = (profile_axes or {}).get(canon)
    if isinstance(row, dict):
        return row.get("status", "set")
    return None


def _reask_ok(ledger, canon, profile_axes, now):
    """Determine whether a missing/volatile axis may be re-asked.

    Dedup rule (DGN-119): a REFUSED axis is never re-asked. An UNKNOWN axis is
    re-askable. A stable axis previously answered is asked at most once. A
    volatile axis is re-askable only after max_age_days from its as_of.
    """
    status = _profile_status(profile_axes, canon)
    if status == "refused":
        return False
    vol = ledger.volatility(canon)
    if status == "set":
        # already known; only volatile axes become re-askable after aging
        if vol == "stable" or vol is None:
            return False
        row = profile_axes.get(canon) or {}
        as_of = row.get("as_of")
        return _older_than(as_of, vol, now)
    # unknown / no-row -> askable
    return True


def _older_than(as_of, max_age_days, now):
    """Deterministic date math: is `as_of` more than max_age_days before `now`?
    Both are ISO YYYY-MM-DD strings. Missing as_of counts as askable (True)."""
    import datetime
    if not as_of:
        return True
    try:
        d0 = datetime.date.fromisoformat(str(as_of))
        d1 = datetime.date.fromisoformat(str(now))
    except (TypeError, ValueError):
        return True
    return (d1 - d0).days > int(max_age_days)


def refract(item, ledger, adapter, profile_axes, now):
    """Refract one item against resolved user axis values. DETERMINISTIC.

    item: the F2 frontmatter dict (applicability.axes + refraction_notes + the
          optional `rescale` spec on a scale-role axis -- see below).
    ledger: a Ledger view over the axes.yaml (Ledger.from_root(root)).
    adapter: a LifekitAdapter for measured axes (may be None -> stated only).
    profile_axes: dict of stated axis rows (see resolve_axis).
    now: ISO YYYY-MM-DD string, passed IN (no ambient clock).

    Returns a RefractionResult. Raises nothing on missing axes -- missing is a
    first-class outcome (Need protocol).
    """
    res = RefractionResult()
    res.item_id = item.get("id")

    app = item.get("applicability") or {}
    axes = app.get("axes") or [] if isinstance(app, dict) else []

    # Curated refraction_notes are surfaced verbatim with their own grades. They
    # never change a number (DGN-119); REFRAME attaches the relevant one.
    notes_by_axis = {}
    for note in (item.get("refraction_notes") or []):
        # a note may name the axis it modifies via `axis:`, else it is general.
        notes_by_axis.setdefault(note.get("axis"), []).append(note)
        res.notes.append({"note": note.get("note"), "grade": note.get("grade"),
                          "axis": note.get("axis")})

    for ax in axes:
        key = ax.get("key")
        canon = ledger.canonical(key)
        role = ax.get("role")
        policy = ax.get("unknown_policy")
        is_safety = ledger.is_safety(canon)

        resolved = resolve_axis(key, ledger, adapter, profile_axes, now)

        if resolved is None:
            # MISSING axis. Two paths: safety gate vs Need.
            status = _profile_status(profile_axes, canon)
            refused_or_unknown = status in ("refused", "unknown") or status is None
            if is_safety and policy == "block_specifics":
                # block_specifics: withhold specific numbers + green-light, keep
                # general info + mechanism. NOT silence.
                res.block_specifics = True
                res.blocked_axes.append(canon)
                res.ops.append(op_exclude_swap(
                    canon,
                    "safety axis unknown/refused -> block_specifics (%s)"
                    % (status or "no-row")))
            # record the Need (baseline + re-ask eligibility) regardless of gate
            res.needed_missing.append({
                "key": canon,
                "safety": is_safety,
                "policy": policy,
                "status": status,
                "baseline_text": ledger.baseline_text(canon),
                "volatility": ledger.volatility(canon),
                "reask_ok": _reask_ok(ledger, canon, profile_axes, now),
            })
            continue

        # axis is present -> record provenance
        res.axes_used.append({
            "key": canon, "source": resolved.source, "value": resolved.value,
            "measured_at": resolved.measured_at, "as_of": resolved.as_of,
        })

        # role-driven op
        if role == "scale":
            spec = ax.get("rescale")  # {"per_unit_low":.., "per_unit_high":..}
            if isinstance(spec, dict):
                op = op_rescale(canon, spec.get("per_unit_low"),
                                spec.get("per_unit_high"), resolved.value)
                if op is not None:
                    res.ops.append(op)
        elif role == "soft":
            # REFRAME only when a curated note targets this axis (else the
            # present value simply stands; soft never withdraws).
            for note in notes_by_axis.get(canon, []):
                res.ops.append(op_reframe(canon, note.get("note"),
                                          note.get("grade")))
        elif role == "hard":
            # hard mismatch is decided by curated gate data on the axis entry:
            # `gate` = {"allowed": [...]} -> value must be in allowed, else swap.
            gate = ax.get("gate")
            if isinstance(gate, dict) and "allowed" in gate:
                allowed = gate.get("allowed") or []
                if resolved.value not in allowed:
                    res.ops.append(op_exclude_swap(
                        canon, "hard axis value %r not in allowed set"
                        % (resolved.value,)))
    return res


# ==========================================================================
# CLI (self-test / manual inspection)
# ==========================================================================

def _demo():
    import json
    root = kimwog.default_root()
    ledger = Ledger.from_root(root)
    item_path = os.path.join(root, "items", "nutrition-protein-intake-002.md")
    fm, _ = kimwog.read_frontmatter(item_path)
    # inject a rescale spec + gate for the demo (sample items carry notes only)
    for ax in (fm.get("applicability") or {}).get("axes", []):
        if ax.get("key") == "body_weight_kg":
            ax["rescale"] = {"per_unit_low": 1.4, "per_unit_high": 2.0}
    adapter = DictLifekitAdapter({
        "body_weight_kg": {"value": 80.0, "measured_at": "2026-07-05"}})
    profile = {"training_status": {"value": "trained", "as_of": "2026-07-01",
                                   "status": "set"}}
    res = refract(fm, ledger, adapter, profile, now="2026-07-06")
    print(json.dumps(res.to_dict(), indent=2, ensure_ascii=True, sort_keys=True))


if __name__ == "__main__":
    _demo()
