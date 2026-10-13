#!/usr/bin/env python3
"""card_lib.py -- the session cards' shared helpers, owned by this pack.

WHY THIS EXISTS (owner ruling 2026-10-02). The session cards were written to
REUSE three instance libraries -- routines/lib/muscle_taxonomy.py,
health_dashboard.py and health_metrics.py -- and none of them is installed on a
new instance (progress-tables.md 2026-09-15 correction; compat-lint C4 forbids
this pack from shipping routines/<non-bundle>). Every importer degraded
silently:

  * the card taxonomy (CARD_MUSCLE_KO & co.) came back EMPTY, so the per-row
    muscle annotation printed English keys. The 2026-09-27 patch papered over
    that by reading ui_labels.MUSCLE_PLAIN_KO (the PROGRAM card's plain-word
    register) on the session cards -- the regression this module ends;
  * the cumulative-volume block never rendered (no sparkline, no arrow, no names).

This module carries the parts the cards use, read-only and stdlib-only, so the
cards stop depending on files nobody installs. It is the ONE copy: the session
cards import it instead of the instance libraries, never alongside them.

  taxonomy   Taxonomy / load / bind: muscle_node + muscle_label read side
             (from the retired muscle_taxonomy.py, unchanged in behaviour).
             bind() returns the compat proxies CARD_MUSCLE_KO (short anatomy
             register), MUSCLE_KO (long register), GROUP_KO, ...
  metrics    DB, MUSCLE_KO, MUSCLE_GROUP, GROUP_KO, GROUP_ORDER, coarse_group,
             VOLUME_TREND_SESSIONS, _recent_coded_sessions (health_metrics).
  glyphs     _sparkline, _dir_arrow, _disp_width (health_dashboard).
  markers    MARK_DONE / MARK_CURRENT / MARK_PASSED / MARK_PENDING -- the one marker set of
             every session table (owner 2026-10-02: the set-table style).
  prep       render_prep_table -- tables (0) mat prep and (0-E) machine prep.

DB BINDING. Callers rebind `card_lib.DB` (exercise-enter does it on every
hand-out) or pass their own resolver to bind(); the taxonomy read is cached per
db path, so the hot card path costs a dict lookup.

DEGRADE. A missing/unreadable db, or one predating the taxonomy tables, gives
an EMPTY taxonomy and an empty history -- never an exception.

ASCII-only source: every non-ASCII glyph is a \\u escape.
"""

import os
import sqlite3
import unicodedata
from collections import abc

ROOT = os.environ.get(
    "WARG_ROOT",
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
)
DB = os.path.join(ROOT, "database", "kit_life.db")


# ===========================================================================
# taxonomy (muscle_node / muscle_label read side)
# ===========================================================================
class Taxonomy(object):
    """An immutable, fully-materialised read of muscle_node + muscle_label."""

    __slots__ = ("nodes", "labels", "group_order", "group_ko", "muscle_group",
                 "muscle_ko_long", "muscle_ko_short", "subregion_parent",
                 "subregion_ko", "muscle_children", "subregion_group",
                 "subregion_vocab")

    def __init__(self, rows=(), labels=(), subregion_vocab=()):
        self.nodes = {r[0]: {"parent": r[1], "kind": r[2], "sort": r[3],
                             "band_unit": r[4]} for r in rows}
        self.labels = {(l[0], l[1], l[2]): l[3] for l in labels}
        self.subregion_vocab = set(subregion_vocab)

        n = self.nodes
        self.group_order = [k for k in sorted(
            (x for x in n if n[x]["parent"] is None),
            key=lambda x: (n[x]["sort"] or 0, x))]
        self.group_ko = {g: self.label(g, "long") for g in self.group_order
                         if self.label(g, "long") is not None}
        muscles = [k for k in sorted(n, key=lambda x: (n[x]["sort"] or 0, x))
                   if n[k]["kind"] == "muscle"]
        self.muscle_group = {m: self.root_of(m) for m in muscles}
        self.muscle_ko_long = {m: self.label(m, "long") for m in muscles
                               if self.label(m, "long") is not None}
        self.muscle_ko_short = {m: self.label(m, "short") for m in muscles
                                if self.label(m, "short") is not None}
        # subregion vocabulary -> its MUSCLE-level parent (a vocabulary entry
        # that is itself a muscle answers with itself). A child of a pure
        # aggregate (adductors -> legs) has no muscle-level parent: excluded.
        sp = {}
        for sr in sorted(self.subregion_vocab):
            p = self.muscle_parent(sr)
            if p is not None and n.get(p, {}).get("kind") == "muscle":
                sp[sr] = p
        self.subregion_parent = sp
        self.subregion_ko = {sr: self.label(sr, "short") for sr in sp
                             if self.label(sr, "short") is not None}
        kids = {}
        for sr, pa in sp.items():
            kids.setdefault(pa, set()).add(sr)
        self.muscle_children = kids
        self.subregion_group = {
            sr: (n[sr].get("band_unit") or sr)
            for sr in sorted(self.subregion_vocab) if sr in n}

    def label(self, node, form, lang="ko"):
        return self.labels.get((node, lang, form))

    def root_of(self, node):
        """Walk to the root (the coarse group). Cycle-safe."""
        seen = set()
        cur = node
        while cur in self.nodes and self.nodes[cur]["parent"] is not None:
            if cur in seen:
                return cur
            seen.add(cur)
            cur = self.nodes[cur]["parent"]
        return cur

    def muscle_parent(self, node):
        info = self.nodes.get(node)
        if info is None:
            return None
        return node if info["kind"] == "muscle" else info["parent"]


_EMPTY = Taxonomy()
_CACHE = {}


def load(db_path=None):
    """Cached Taxonomy for `db_path`. Never raises; degrades to empty."""
    path = os.path.abspath(db_path or DB)
    hit = _CACHE.get(path)
    if hit is not None:
        return hit
    try:
        conn = sqlite3.connect("file:%s?mode=ro" % path, uri=True)
        try:
            rows = conn.execute(
                "SELECT node, parent, kind, sort, band_unit "
                "FROM muscle_node").fetchall()
            labels = conn.execute(
                "SELECT node, lang, form, text FROM muscle_label").fetchall()
            vocab = [r[0] for r in conn.execute(
                "SELECT DISTINCT subregion FROM exercise_subregion")]
        finally:
            conn.close()
        tax = Taxonomy(rows, labels, vocab)
    except Exception:  # noqa: BLE001 -- no taxonomy tables -> caller degrades
        tax = _EMPTY
    _CACHE[path] = tax
    return tax


def reset_cache():
    """Drop the per-path cache (tests that mutate a db between assertions)."""
    _CACHE.clear()


class _LazyMap(abc.Mapping):
    """Mapping view over one Taxonomy attribute, resolved on every touch."""

    __slots__ = ("_db", "_attr")

    def __init__(self, get_db, attr):
        self._db = get_db
        self._attr = attr

    def _d(self):
        return getattr(load(self._db()), self._attr)

    def __getitem__(self, k):
        return self._d()[k]

    def __iter__(self):
        return iter(self._d())

    def __len__(self):
        return len(self._d())

    def __repr__(self):
        return repr(self._d())


class _LazySeq(abc.Sequence):
    """Sequence view (GROUP_ORDER)."""

    __slots__ = ("_db", "_attr")

    def __init__(self, get_db, attr):
        self._db = get_db
        self._attr = attr

    def _l(self):
        return getattr(load(self._db()), self._attr)

    def __getitem__(self, i):
        return self._l()[i]

    def __len__(self):
        return len(self._l())

    def __eq__(self, other):
        return list(self._l()) == list(other) if isinstance(
            other, (list, tuple, _LazySeq)) else NotImplemented

    def __ne__(self, other):
        eq = self.__eq__(other)
        return eq if eq is NotImplemented else not eq

    def __repr__(self):
        return repr(self._l())


def bind(get_db):
    """All compat proxies, bound to a db resolver (callable or plain path)."""
    if not callable(get_db):
        _fixed = get_db

        def get_db():  # noqa: E306 -- accept a plain path too
            return _fixed
    return {
        "MUSCLE_GROUP":          _LazyMap(get_db, "muscle_group"),
        "GROUP_KO":              _LazyMap(get_db, "group_ko"),
        "GROUP_ORDER":           _LazySeq(get_db, "group_order"),
        "MUSCLE_KO":             _LazyMap(get_db, "muscle_ko_long"),
        "CARD_MUSCLE_KO":        _LazyMap(get_db, "muscle_ko_short"),
        "CARD_SUBREGION_PARENT": _LazyMap(get_db, "subregion_parent"),
        "CARD_SUBREGION_KO":     _LazyMap(get_db, "subregion_ko"),
        "CARD_MUSCLE_CHILDREN":  _LazyMap(get_db, "muscle_children"),
        "SUBREGION_GROUP":       _LazyMap(get_db, "subregion_group"),
    }


# ===========================================================================
# metrics (the health_metrics subset the cards read)
# ===========================================================================
_TAX = bind(lambda: DB)
MUSCLE_KO = _TAX["MUSCLE_KO"]
MUSCLE_GROUP = _TAX["MUSCLE_GROUP"]
GROUP_KO = _TAX["GROUP_KO"]
GROUP_ORDER = _TAX["GROUP_ORDER"]

# How many most-recent CODED sessions define the volume trend window.
VOLUME_TREND_SESSIONS = 6


def coarse_group(muscle):
    """Coarse group key for a fine muscle; the muscle itself when unknown."""
    return MUSCLE_GROUP.get(muscle, muscle)


def _recent_coded_sessions(limit=None, since_days=None):
    """Sessions that carry a split code AND >=1 logged set, oldest->newest.

    [{"id", "date", "code"}]. The retired health_metrics copy also filtered
    owning_agent on the retired agent's literal slug; a new instance writes its
    own slug (ax_engine.resolve_owning_agent), so that filter would leave every
    trend empty. The session_type join is what scopes this to training
    sessions."""
    where = ["st.code IS NOT NULL",
             "EXISTS (SELECT 1 FROM workout_sets ws WHERE ws.session_id=w.id)"]
    params = []
    if since_days is not None:
        where.append("w.date >= date('now', ?)")
        params.append("-%d day" % since_days)
    sql = ("SELECT w.id, w.date, st.code FROM workouts w "
           "JOIN session_type st ON w.session_type_id = st.id "
           "WHERE " + " AND ".join(where) +
           " ORDER BY w.date DESC, w.id DESC")
    if limit is not None:
        sql += " LIMIT ?"
        params.append(limit)
    try:
        conn = sqlite3.connect(DB)
        try:
            rows = conn.execute(sql, params).fetchall()
        finally:
            conn.close()
    except Exception:  # noqa: BLE001 -- no history is an empty trend
        return []
    out = [{"id": r[0], "date": r[1], "code": r[2]} for r in rows]
    out.reverse()
    return out


# ===========================================================================
# glyphs (the health_dashboard subset the cards read)
# ===========================================================================
_SPARK_BLOCKS = u"\u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588"
ARROW_UP, ARROW_FLAT, ARROW_DOWN = u"\u2191", u"\u2192", u"\u2193"


def _disp_width(s):
    """Display width: East Asian W, F and A glyphs count two cells."""
    return sum(2 if unicodedata.east_asian_width(ch) in ("W", "F", "A") else 1
               for ch in str(s))


def _sparkline(series):
    """Numeric series -> block sparkline scaled to the series' own range.
    A flat series renders mid-height; empty -> ''. None -> a blank cell."""
    vals = [v for v in (series or []) if v is not None]
    if not vals:
        return ""
    lo, hi = min(vals), max(vals)
    if hi == lo:
        return _SPARK_BLOCKS[len(_SPARK_BLOCKS) // 2] * len(vals)
    span = hi - lo
    out = []
    for v in series or []:
        if v is None:
            out.append(" ")
            continue
        idx = int(round((v - lo) / span * (len(_SPARK_BLOCKS) - 1)))
        out.append(_SPARK_BLOCKS[max(0, min(len(_SPARK_BLOCKS) - 1, idx))])
    return "".join(out)


def _dir_arrow(series):
    """First vs last present value: up / down / flat. Never a diagonal."""
    vals = [v for v in (series or []) if v is not None]
    if len(vals) < 2:
        return ARROW_FLAT
    delta = vals[-1] - vals[0]
    if delta > 0:
        return ARROW_UP
    if delta < 0:
        return ARROW_DOWN
    return ARROW_FLAT


# ===========================================================================
# markers -- ONE set across every session table (owner 2026-10-02)
# ===========================================================================
# The set-table style, ASCII: done, in progress, pending. The lineup pin card,
# the closeout card and the two prep tables all draw from these.
# MARK_PASSED (owner review 2026-10-02 09:15: prep and the row were both
# shown in progress): an item the session moved past while unfinished -- left, not
# in progress. Only the item currently entered is MARK_CURRENT, so a card has
# at most one [>] row.
# RETIRED from the cards (owner 2026-10-02 10:12 / 11:06): mid-session a
# passed item reads MARK_DONE, on the closeout card a lift ended short reads
# MARK_CURRENT. Kept only as a name for older callers.
MARK_DONE = "[v]"
MARK_CURRENT = "[>]"
MARK_PASSED = "[-]"
MARK_PENDING = "[ ]"


# ===========================================================================
# prep tables (0) and (0-E)
# ===========================================================================
PREP_MAT_EMOJI = u"\U0001F9D8"       # table (0) title glyph
PREP_EQUIP_EMOJI = u"\U0001F527"     # table (0-E) title glyph
PREP_MAT_TITLE = u"\ub9e4\ud2b8 \uc900\ube44\uc6b4\ub3d9"         # mat prep
# (0-E) is the prep FOR one lift (owner 2026-10-02 11:10): titled
# "<lift> + PREP_SLOT_TITLE"; PREP_EQUIP_TITLE when the lift is unknown.
PREP_EQUIP_TITLE = u"\uc7a5\ube44 \uc900\ube44\uc6b4\ub3d9"       # fallback title
PREP_SLOT_TITLE = u"\uc900\ube44\uc6b4\ub3d9"                      # "<lift> " + this
# The header count reads done/total with the word saying so ("1/3 \uc644\ub8cc"):
# owner 2026-10-12 06:27 saw a bare "1/3" above one [v] row and could not
# tell "done" from "drill 1 of 3 is up".
PREP_COUNT_FMT = u"%d/%d \uc644\ub8cc"                                # "<done>/<total> done"
SEP = u" \u00b7 "


# Dose words for a prep row (owner 2026-10-02 11:13: show the rep count).
# Read from set-table.prep_target_spec(drill) -- the owner-stated prescription;
# nothing is invented when the drill states none.
_DOSE_TIMES = u"\ud68c"            # reps suffix
_DOSE_SIDES = u"\uc88c\uc6b0"      # per-side prefix
_DOSE_SEC = u"\ucd08"              # seconds suffix


def prep_dose_text(spec, words=None):
    """'' | 'N<times>' | '<sides> N<times>' | 'S<sec> x N' | 'S<sec>'.
    `words` ({unit: '%d' format}, the drill's prep_cues.json `dose`) lets a
    drill with its own count word say it: bear crawl counts steps per side,
    halo / arm circles per direction (kimwog exercise 741)."""
    spec = spec if isinstance(spec, dict) else {}
    value, unit, hold = spec.get("value"), spec.get("unit"), spec.get("hold_sec")
    if value is None:
        return ("%s%s" % (hold, _DOSE_SEC)) if hold is not None else ""
    word = words.get(unit or "reps") if isinstance(words, dict) else None
    if hold is None and word:
        return word % int(value)
    if unit == "per_side":
        return "%s %d%s" % (_DOSE_SIDES, value, _DOSE_TIMES)
    if unit == "hold_sets":
        return ("%s%s x %d" % (hold, _DOSE_SEC, value)) if hold is not None \
            else "%d%s" % (value, _DOSE_TIMES)
    return "%d%s" % (value, _DOSE_TIMES)


def render_prep_table(kind, rows, exercise_ko=None):
    """Lines of table (0) (kind='mat') or (0-E) (kind='equipment').

    rows = [(drill display name, done bool[, dose text])] in performance order. Shape
    (owner 2026-10-02): a header line, ONE blank line, then one marker row per
    drill. Returns [] when there are no rows -- no empty table, ever."""
    norm = []
    for r in rows or []:
        n, d = r[0], r[1]
        dose = r[2] if len(r) > 2 else ""
        if n:
            norm.append((str(n), bool(d), str(dose or "")))
    rows = norm
    if not rows:
        return []
    done = sum(1 for _n, d, _x in rows if d)
    count = PREP_COUNT_FMT % (done, len(rows))
    if kind == "equipment":
        title = ("%s %s" % (exercise_ko, PREP_SLOT_TITLE) if exercise_ko
                 else PREP_EQUIP_TITLE)
        parts = [PREP_EQUIP_EMOJI + " " + title, count]
    else:
        parts = [PREP_MAT_EMOJI + " " + PREP_MAT_TITLE, count]
    lines = [SEP.join(parts), ""]
    for name, d, dose in rows:
        label = name + (SEP + dose if dose else "")
        lines.append("%s %s" % (MARK_DONE if d else MARK_PENDING, label))
    return lines
