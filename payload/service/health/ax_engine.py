#!/usr/bin/env python3
# ax_engine.py -- AX/US engine core (DGN-782, pack payload).
#
# The projection engine, US render/delivery composition, and JIT-gate logic
# that run OVER the v20 tables (migration 020_ax_us_datamodel). This is the
# shared library; the three CLI entrypoints (ax-project / us-render / ax-jit)
# are thin argv wrappers around the functions here.
#
# BOUNDARY (DGN-782, framework-confirmed): the entire engine is pack code.
# The framework owns ONLY the countdown done-marker (C1 self-natural-end emit, still
# pending) plus reused primitives (push transport, countdown channel, migration
# runner). Every function here is pack payload -- no in-process framework API,
# interfaces are file / CLI / exit-code only. Runs as installed kit_core python
# (pack_install.sh 2e: payload/database/* -> instance/database/).
#
# Behaviour preserved from the interim instance-local carriers (rx-calc F17 needs_lattice
# + snap_to_lattice, lattice-set, set-arm F11 next_hint): the DB engine is the
# PRIMITIVE that supersedes those YAML-slot carriers while keeping their exact
# rounding + gate semantics. See snap_to_lattice() (ported verbatim from
# rx-calc) and jit_probe() (the F17 forcing-point moved to the tool level).
#
# stdlib only: sys, os, json, sqlite3, math, importlib.

import os
import sys
import re
import json
import math
import sqlite3
import importlib.util
import importlib.machinery

_ENGINE_DIR = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# kit_life core reuse (get connection helpers / ULID / pragmas). We do NOT rely
# on kit_life.DB_PATH (hardcoded to the install dir); the engine resolves its DB
# via --db / LIFEKIT_DB / kit_life default, so smoke tests run on a temp copy.
# ---------------------------------------------------------------------------
# PACK/LIVE PATH SEAM -- the SAME two-candidate probe set-table / set-add /
# set-arm carry for ax_engine.py itself, one level down. kit_life.py has ONE
# owner (kit_life, installed to <root>/database/) but this engine has had two
# homes:
#   live layout   database/ax_engine.py         <- kit_life.py is a SIBLING
#   pack layout   service/health/ax_engine.py   <- kit_life.py is ../../database
# The sibling path alone was correct only before the PROJECTION-ENGINE SEAM
# cutover (2026-08-25) moved this file out of database/. Post-cutover, on an
# INSTALLED instance, `_ENGINE_DIR/kit_life.py` is service/health/kit_life.py --
# which the pack does not ship and, with capabilities.db_lane=false, may not
# ship. So _lk() raised FileNotFoundError and took new_ulid() and
# resolve_db_path() down with it: `ax-jit` / `ax-project` died at line 1 unless
# --db or LIFEKIT_DB was supplied, and EVERY write path died unconditionally.
# It held on the live tree only because the engine still sat next to the facade
# there (audit 2026-09-12 2.2 -- this is an installed-instance break, not the
# repo-hygiene note the README used to call it).
# SIBLING IS TRIED FIRST so a live/pre-cutover tree behaves exactly as before.
_KIT_LIFE_CANDIDATES = (
    ("kit_life.py",),                          # live: database/ sibling
    ("..", "..", "database", "kit_life.py"),   # pack: <root>/database
)


# LIFEKIT_CORE_PY -- the facade half of the escape hatch LIFEKIT_DB already
# provides for the DB half, and the exact mirror of the LIFEKIT_SCHEMA_SQL the
# ax/us smoke test already uses for the kit's DDL.
#
# WHY IT EXISTS (2026-09-12). Neither candidate below can exist in a PACK
# CHECKOUT: `database/` is the kit's lane and capabilities.db_lane=false forbids
# this pack from writing it, so a checkout has no kit_life.py anywhere. That is
# correct as a packaging rule and fatal as a test rule -- it is why
# tests/test_ax_us_engine.py was red on `main`, dying on the raise below after
# it had already resolved the kit's schema.sql through LIFEKIT_SCHEMA_SQL. One
# env var makes the pack's own smoke test runnable against a kit sibling
# checkout without the pack ever carrying a copy of the facade.
#
# It is an OVERRIDE, not a candidate: it wins outright when set, and a value
# that points at nothing still loses to nothing -- the raise below names it
# alongside the two probed paths so a typo says so instead of looking like an
# install defect. The README listed this hatch as a genuine nice-to-have; it is
# now real.
_KIT_LIFE_ENV = "LIFEKIT_CORE_PY"


def kit_life_path():
    """Absolute path to the kit_life.py this tree should import, or the SIBLING
    candidate when neither exists (so the error names the historical path)."""
    env = os.environ.get(_KIT_LIFE_ENV)
    if env:
        return os.path.abspath(os.path.expanduser(env))
    for parts in _KIT_LIFE_CANDIDATES:
        cand = os.path.abspath(os.path.join(_ENGINE_DIR, *parts))
        if os.path.exists(cand):
            return cand
    return os.path.abspath(os.path.join(_ENGINE_DIR,
                                        *_KIT_LIFE_CANDIDATES[0]))


def _load_kit_life():
    """Import kit_life.py (its __main__ guard makes import side-effect free).
    Reused for new_ulid + _apply_pragmas -- climb-the-ladder: do not
    re-implement primitives the core already carries. Located via
    kit_life_path(); see the seam note above for why there are two candidates.

    LOUD BY DESIGN, unlike the ax_engine loaders above: there is no degraded
    answer for "mint an id" or "which DB". A caller that cannot get a ULID must
    not invent one, so this raises and the CLI exits -- and it raises with BOTH
    probed paths named, rather than the bare FileNotFoundError that said only
    the one path that was never going to exist."""
    path = kit_life_path()
    if not os.path.isfile(path):
        probed = [os.path.abspath(os.path.join(_ENGINE_DIR, *p))
                  for p in _KIT_LIFE_CANDIDATES]
        env = os.environ.get(_KIT_LIFE_ENV)
        if env:
            probed.insert(0, "%s=%s" % (_KIT_LIFE_ENV, env))
        raise FileNotFoundError(
            "kit_life.py not found -- probed: %s" % ", ".join(probed))
    spec = importlib.util.spec_from_file_location("kit_life", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_LK = None


def _lk():
    global _LK
    if _LK is None:
        _LK = _load_kit_life()
    return _LK


def new_ulid():
    return _lk().new_ulid()


def now_iso():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ")


def resolve_db_path(explicit=None):
    """DB path resolution order: explicit --db > LIFEKIT_DB env > kit_life
    default (install dir). Lets the engine run against a temp copy for tests
    without touching the installed DB."""
    if explicit:
        return explicit
    env = os.environ.get("LIFEKIT_DB")
    if env:
        return env
    return _lk().DB_PATH


# ===========================================================================
# OWNING AGENT -- WHO THIS INSTANCE IS, ON A CREW-SHARED DB.
#
# WHY THIS EXISTS (2026-09-14). `owning_agent` is the column that tells two
# crew members apart on ~/.dogany/crews/kit_life/kit_life.db. Every writer in
# this file used to stamp a hard-coded legacy slug. That
# was latent for the health lane only because nothing ever wrote ax_exercise;
# the moment the taxonomy seed fills it (the fix landing alongside this one), a
# freshly minted health agent's catalog lands under a retired instance's
# identity, and a SECOND health agent collides with the first on
# idx_ax_tag_uni(owning_agent, tag_group, value).
#
# THE TWO LINEAGES, AND WHY THE PROBE IS NOT OPTIONAL
#   pre-049  the kit schema constrains the column with a CLOSED enumeration,
#            CHECK on owning_agent (the legacy three-value enum). A resolved slug that
#            is not one of those three is REFUSED -- IntegrityError, on every
#            insert, including the seed's. Writing the resolved slug there does
#            not fix an identity bug, it breaks the install.
#   049+     the enumeration is replaced by a slug GRAMMAR and the instance can
#            write under its own name.
# So the value is not chosen from config alone: it is chosen from config AND
# from what this DB can actually accept, measured once per connection. On a
# pre-049 DB the legacy slug is used AND SAID OUT LOUD (one stderr line per
# process) -- a mislabel that announces itself, never a silent one. This pack
# declares requires_kit >=2.19.0 and must keep working on 2.20.0; a hard
# dependency on an uncut kit is not a fix.
#
# NOT A FALLBACK THAT HIDES ANYTHING: the probe answers "does this schema
# accept a slug", which is a fact about the DB, not a guess about the answer.
# ===========================================================================
OWNING_AGENT_ENV = "LIFEKIT_OWNING_AGENT"

# The legacy closed enumeration, verbatim as the pre-049 kit schema writes it.
# Matched as TEXT against sqlite_master because that is where the constraint
# lives; there is no PRAGMA that reports a CHECK.
LEGACY_OWNING_AGENT_ENUM = ("ag", "warg", "user")  # estate-scrub:allow(legacy DB slug value, a data contract kept for pre-049 DBs)
LEGACY_OWNING_AGENT_CHECK = "CHECK (owning_agent IN ('ag','warg','user'))"  # estate-scrub:allow(legacy DB slug value, a data contract kept for pre-049 DBs)

# The slug this pack stamps when it must write to a pre-049 DB. The legacy slug is the
# historical value every existing row on such a DB already carries, so a
# pre-049 write joins the rows already there instead of orphaning itself.
LEGACY_OWNING_AGENT = "warg"  # estate-scrub:allow(legacy DB slug value, a data contract kept for pre-049 DBs)

# Instance-slug grammar. Deliberately WIDER than [a-z0-9_]: mint.sh enforces no
# grammar at all on DOGANY_AGENT_NAME (measured 2026-09-14, scripts/mint.sh:189
# -- it defaults the name to `basename $PROJECT_ROOT` and validates nothing), so
# a real slug can carry a hyphen or an upper-case letter. What is refused is
# what would make the column stop discriminating: empty, whitespace, quotes,
# path fragments, CJK display labels.
_OWNING_AGENT_OK = re.compile(r"^[A-Za-z0-9_-]{1,64}$")
_OWNING_AGENT_STRIP = re.compile(r"[^A-Za-z0-9_-]+")

# Instance-root probe: this file installs to <root>/service/health/ax_engine.py
# (pack layout) or <root>/database/ax_engine.py (live/pre-cutover layout). Both
# are covered by walking up and stopping at the .instance.conf mint.sh writes.
_INSTANCE_CONF = ".instance.conf"


def _instance_conf_value(key, start=None):
    """`key=value` from the nearest .instance.conf at or above `start`, or None.

    mint.sh writes that manifest for EVERY instance (scripts/mint.sh:537), so on
    an installed tree this resolves; in a pack checkout or a test fixture there
    is no instance and it correctly answers None."""
    here = os.path.abspath(start or _ENGINE_DIR)
    for _ in range(6):
        cand = os.path.join(here, _INSTANCE_CONF)
        if os.path.isfile(cand):
            try:
                with open(cand, encoding="utf-8") as fh:
                    for line in fh:
                        line = line.strip()
                        if line.startswith(key + "="):
                            return line.split("=", 1)[1].strip()
            except OSError:
                return None
            return None
        nxt = os.path.dirname(here)
        if nxt == here:
            break
        here = nxt
    return None


def normalize_owning_agent(raw):
    """A candidate slug reduced to the grammar above, or None if nothing is
    left. Never raises. Normalising rather than refusing is what keeps a
    directory named `health-bot 2` from turning into an IntegrityError at the
    first write -- the DB gets `health-bot_2`, which still discriminates."""
    if raw is None:
        return None
    s = str(raw).strip().strip("'\"")
    if not s:
        return None
    if not _OWNING_AGENT_OK.match(s):
        s = _OWNING_AGENT_STRIP.sub("_", s).strip("_")[:64]
    return s if s and _OWNING_AGENT_OK.match(s) else None


def resolve_owning_agent(default=LEGACY_OWNING_AGENT):
    """THIS INSTANCE'S slug, independent of what any DB will accept.

    Order, first hit wins:
      1. LIFEKIT_OWNING_AGENT   explicit operator/test override
      2. .instance.conf DOGANY_AGENT_NAME   the mint manifest (the real answer
         on every installed tree)
      3. DOGANY_AGENT_NAME env  the same fact, when a caller exports it
      4. `default`              no instance to read: a pack checkout or a test
         fixture, where any legal slug is equally true."""
    for cand in (os.environ.get(OWNING_AGENT_ENV),
                 _instance_conf_value("DOGANY_AGENT_NAME"),
                 os.environ.get("DOGANY_AGENT_NAME")):
        slug = normalize_owning_agent(cand)
        if slug:
            return slug
    return default


def owning_agent_grammar_open(target):
    """True iff this DB has migration 049 -- i.e. it accepts an arbitrary slug.

    Measured off sqlite_master, the only place a CHECK is readable. Accepts an
    open connection or a path. Any read failure answers False (fail-closed: an
    unreadable schema is not permission to write a slug it may refuse)."""
    try:
        conn, close_it = _tax_open(target)
    except Exception:      # noqa: BLE001
        return False
    try:
        n = conn.execute(
            "SELECT COUNT(*) FROM sqlite_master WHERE type='table' "
            "AND instr(sql, ?) > 0;", (LEGACY_OWNING_AGENT_CHECK,)).fetchone()
        return (n is not None and n[0] == 0)
    except Exception:      # noqa: BLE001
        return False
    finally:
        if close_it:
            conn.close()


_LEGACY_SLUG_ANNOUNCED = set()


def _announce_legacy_slug_once(key, resolved):
    """ONE stderr line per process per DB when this pack writes under the
    retired slug because the schema still refuses the real one. Same shape as
    AX-ENGINE-MISSING: a structural absence gets named, not swallowed."""
    if key in _LEGACY_SLUG_ANNOUNCED:
        return
    _LEGACY_SLUG_ANNOUNCED.add(key)
    sys.stderr.write(
        "[ax_engine] OWNING-AGENT-LEGACY: this DB still carries the pre-049 "
        "closed enumeration %s, so rows are being written as %r, NOT as this "
        "instance (%r). Two health agents on this crew DB would collide. Fix: "
        "apply kit_life migration 049_owning_agent_identity.sql.\n"
        % (LEGACY_OWNING_AGENT_CHECK, LEGACY_OWNING_AGENT, resolved))


def owning_agent_for(target):
    """The slug to STAMP on a row in this DB: resolve_owning_agent(), degraded
    to the legacy slug (loudly) when this DB's schema would refuse it.

    Every writer in this module calls this instead of carrying a literal. Reads
    that find-or-create call it too, so the read and the write it guards look
    for the same identity -- otherwise a find-first would miss its own row and
    grow a duplicate under idx_ax_tag_uni."""
    resolved = resolve_owning_agent()
    if resolved in LEGACY_OWNING_AGENT_ENUM:
        return resolved
    if owning_agent_grammar_open(target):
        return resolved
    try:
        key = os.path.abspath(str(target)) if not isinstance(
            target, sqlite3.Connection) else "conn:%d" % id(target)
    except Exception:      # noqa: BLE001
        key = "conn"
    _announce_legacy_slug_once(key, resolved)
    return LEGACY_OWNING_AGENT


def connect(db_path, read_only=False):
    """Open a kit_life-hardened connection at db_path. read_only opens the file
    with SQLite ?mode=ro (used by the render/JIT read paths; live DBs are
    READ-ONLY per the task constraint unless a write verb is invoked)."""
    if not os.path.isfile(db_path):
        raise FileNotFoundError("kit_life.db not found: %s" % db_path)
    if read_only:
        conn = sqlite3.connect("file:%s?mode=ro" % db_path, uri=True)
    else:
        conn = sqlite3.connect(db_path)
        # apply the same hardening PRAGMAs kit_life uses for writers.
        try:
            _lk()._apply_pragmas(conn)
        except Exception:
            conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn


# ===========================================================================
# ROUNDING PRIMITIVES (weight-training domain)
# Ported verbatim from the interim rx-calc.snap_to_lattice so the pack engine
# reproduces the exact discrete-load snap the live carrier does. Tie resolves
# UP (next harder load); floor = base; malformed profile -> value unchanged.
# ===========================================================================
DUMBBELL_DEFAULT_POINTS = tuple([2.0, 4.0, 6.0, 8.0, 10.0]
                                + [10.0 + 2.5 * k for k in range(1, 37)])


def snap_to_lattice(value, lattice):
    """Snap a computed weight onto the nearest achievable value of a lattice
    profile. lattice = {type, base, step} or None.
      type 'even'     -> even-kg only          (base default 0.0, step 2.0)
      type 'stack'    -> pin stack base+k*step (base and step required)
      type 'standard' -> free 2.5 kg grid      (base 0.0, step 2.5)
    None / non-dict / unknown type / malformed -> value unchanged.
    Nearest achievable value; ties resolve UP. Floor = base.
    (verbatim from rx-calc F17 carrier; behaviour preserved.)"""
    if value is None or not isinstance(lattice, dict):
        return value
    ltype = lattice.get('type', 'standard')
    # live batch 2 item 3: a bare {type: even} is the DEFAULT dumbbell rack --
    # 2kg steps to 10kg, then 2.5kg (mirrors rx-calc DUMBBELL_DEFAULT_POINTS).
    # An even profile with its own base/step is a recorded gym grid.
    if (ltype == 'even' and lattice.get('step') is None
            and lattice.get('base') is None):
        return round(min(DUMBBELL_DEFAULT_POINTS,
                         key=lambda p: (abs(p - value), -p)), 4)
    if ltype == 'even':
        base = lattice.get('base', 0.0)
        step = lattice.get('step', 2.0)
    elif ltype == 'stack':
        base = lattice.get('base')
        step = lattice.get('step')
        if base is None or step is None:
            return value   # malformed stack profile: do not guess
    elif ltype == 'standard':
        base = lattice.get('base', 0.0)
        step = lattice.get('step', 2.5)
    else:
        return value       # unknown type: leave the value alone
    if step is None or step <= 0:
        return value
    if value <= base:
        return round(base, 4)
    k = (value - base) / step
    lo_v = base + math.floor(k) * step
    hi_v = lo_v + step
    chosen = lo_v if (value - lo_v) < (hi_v - value) else hi_v
    return round(chosen, 4)


def project_plates(target, available_plates, loading_side="per_side", bar_kg=20.0):
    """Round target weight onto a realizable plate combination from a gym-
    scoped available_plates list (JSON kg array). Returns (realized, detail).

    loading_side:
      'per_side' -> plates go on both ends; per-end load = (target - bar)/2,
                    realized = bar + 2 * (chosen per-end).
      'single' / 'total' / 'stack' -> plates count once (machine/total load).
    Greedy descending fill (standard barbell math); realized never exceeds
    target's nearest achievable stack (best-effort under the plate set)."""
    plates = sorted([float(p) for p in (available_plates or [])], reverse=True)
    if target is None:
        return None, None
    if not plates:
        # no plate data -> cannot project; hand target back unrounded.
        return round(float(target), 4), {"note": "no_plates", "target": target}
    per_side = str(loading_side) == "per_side"
    if per_side:
        want = max(0.0, (float(target) - bar_kg) / 2.0)
    else:
        want = max(0.0, float(target))
    used = []
    remaining = want
    for p in plates:
        while remaining + 1e-9 >= p:
            used.append(p)
            remaining -= p
    side_load = sum(used)
    if per_side:
        realized = bar_kg + 2.0 * side_load
    else:
        realized = side_load
    detail = {
        "loading_side": loading_side,
        "bar_kg": bar_kg if per_side else None,
        "plates_per_side" if per_side else "plates": sorted(used, reverse=True),
        "target": float(target),
    }
    return round(realized, 4), detail


# ===========================================================================
# JIT GATE (J1-J4) -- provisional / unregistered machine forcing-point.
# Absorbs the interim rx-calc F17 needs_lattice predicate at the TOOL level:
# projection off an incomplete machine is BLOCKED, the missing fields are asked
# (structured needs-fields signal), stored to the registry, then auto-reused.
# ===========================================================================
# Which fields a machine must carry to be projectable, keyed by load_type.
# A machine missing any required field for its load_type is "incomplete".
_JIT_REQUIRED = {
    "machine": ["lattice_base", "lattice_step"],   # discrete-load grid (F17)
    "cable":   ["cable_lines"],                     # which line(s)
    "freeweight": [],                               # bar math needs no registry
    "bodyweight": [],
}


def machine_row(conn, machine_ulid):
    r = conn.execute("SELECT * FROM ax_machine WHERE ulid=?;",
                     (machine_ulid,)).fetchone()
    return r


def jit_probe(conn, machine_ulid, load_type):
    """J1/J2: detect an unregistered/incomplete machine and return a structured
    gate result. Returns dict:
      {"ok": True}                              -> projectable, proceed
      {"ok": False, "reason": "unregistered",   -> machine_ulid has no row
       "machine_ref": <ulid>, "needs": [...] }
      {"ok": False, "reason": "provisional"|"incomplete",
       "machine_ref": <ulid>, "needs": [<field>, ...]}
    'needs' lists exactly the missing registry fields to ask for (J3). This is
    the F17 forcing-point moved to the tool level: no estimated prescription is
    emitted off an incomplete machine."""
    lt = str(load_type)
    required = _JIT_REQUIRED.get(lt, [])
    if machine_ulid is None:
        if not required:
            return {"ok": True}   # freeweight/bodyweight: no machine needed
        return {"ok": False, "reason": "unregistered", "machine_ref": None,
                "needs": ["label", "gym_id"] + required}
    row = machine_row(conn, machine_ulid)
    if row is None:
        return {"ok": False, "reason": "unregistered",
                "machine_ref": machine_ulid,
                "needs": ["label", "gym_id"] + required}
    keys = row.keys()
    missing = []
    for f in required:
        if f not in keys or row[f] is None:
            missing.append(f)
    # provisional=1 machines are JIT-registered but flagged incomplete.
    prov = ("provisional" in keys and row["provisional"] == 1)
    if missing:
        return {"ok": False, "reason": "provisional" if prov else "incomplete",
                "machine_ref": machine_ulid, "needs": missing}
    if prov:
        # provisional but all required fields present -> clear the flag on
        # first successful projection (auto-reuse: caller may promote).
        return {"ok": True, "was_provisional": True, "machine_ref": machine_ulid}
    return {"ok": True, "machine_ref": machine_ulid}


def jit_register_machine(conn, fields):
    """J3/J4 upsert: find-first by (gym_id, label); if absent INSERT a machine
    row, else UPDATE the supplied fields. provisional is auto-set: 1 if any
    required-for-load field is still missing, else 0. Returns the ulid."""
    label = fields.get("label")
    gym_id = fields.get("gym_id")
    if not label:
        raise ValueError("jit_register_machine requires 'label'")
    row = conn.execute(
        "SELECT ulid FROM ax_machine WHERE label=? AND "
        "(gym_id IS ? OR gym_id=?);",
        (label, gym_id, gym_id)).fetchone()
    cols = ["gym_id", "label", "brand", "loading_method", "loading_side",
            "smith_type", "cable_lines", "available_plates",
            "lattice_base", "lattice_step"]
    # completeness for provisional flag: a machine with a lattice pair or a
    # cable_lines value (per its declared loading) is complete enough.
    lb = fields.get("lattice_base")
    ls = fields.get("lattice_step")
    has_lattice = (lb is not None and ls is not None)
    has_cable = fields.get("cable_lines") is not None
    provisional = 0 if (has_lattice or has_cable) else 1
    ts = now_iso()
    if row is None:
        ulid = new_ulid()
        vals = [fields.get(c) for c in cols]
        conn.execute(
            "INSERT INTO ax_machine (ulid, owning_agent, %s, provisional, "
            "status, created_at, updated_at) VALUES (?, ?, %s, ?, "
            "'active', ?, ?);" % (
                ", ".join(cols), ", ".join(["?"] * len(cols))),
            [ulid, owning_agent_for(conn)] + vals + [provisional, ts, ts])
    else:
        ulid = row["ulid"]
        sets = []
        vals = []
        for c in cols:
            if c in fields and fields[c] is not None:
                sets.append("%s=?" % c)
                vals.append(fields[c])
        sets.append("provisional=?")
        vals.append(provisional)
        sets.append("updated_at=?")
        vals.append(ts)
        conn.execute("UPDATE ax_machine SET %s WHERE ulid=?;" % ", ".join(sets),
                     vals + [ulid])
    conn.commit()
    return ulid


def jit_register_tag(conn, tag_group, value, note=None):
    """J4: unregistered open-tag (grip/muscle/injury/equipment/...) -> add to
    ax_tag on first sight (open-tag growth). find-first upsert; returns ulid."""
    # ONE resolution for the read AND the write (see owning_agent_for): the
    # find-first must look under the identity the insert would stamp, or it
    # misses its own row and grows a duplicate under the UNIQUE index
    # idx_ax_tag_uni(owning_agent, tag_group, value).
    agent = owning_agent_for(conn)
    row = conn.execute(
        "SELECT ulid FROM ax_tag WHERE owning_agent=? AND tag_group=? "
        "AND value=?;", (agent, tag_group, value)).fetchone()
    if row is not None:
        return row["ulid"]
    ulid = new_ulid()
    conn.execute(
        "INSERT INTO ax_tag (ulid, owning_agent, tag_group, value, note, "
        "status, created_at) VALUES (?, ?, ?, ?, ?, 'active', ?);",
        (ulid, agent, tag_group, value, note, now_iso()))
    conn.commit()
    return ulid


# ===========================================================================
# PROJECTION ENGINE (P1-P4)
# Evaluate ax_projection_rule rows against an (exercise, machine) pair in
# priority order, run the matched action(s), and write ax_projection_slot.
# ===========================================================================
def _exercise_row(conn, exercise_ulid):
    return conn.execute("SELECT * FROM ax_exercise WHERE ulid=?;",
                        (exercise_ulid,)).fetchone()


def _exercise_tags(conn, exercise_ulid):
    """Return {tag_group: set(values)} for an exercise (P1 tag-join match)."""
    rows = conn.execute(
        "SELECT t.tag_group, t.value FROM ax_exercise_tag j "
        "JOIN ax_tag t ON t.ulid = j.tag_ref WHERE j.exercise_ref=?;",
        (exercise_ulid,)).fetchall()
    out = {}
    for r in rows:
        out.setdefault(r["tag_group"], set()).add(r["value"])
    return out


def _rule_matches(rule, ex, mac, tags):
    """P1 match predicate: NULL match_* columns are wildcards. injury match
    and tag-group match are resolved by reading the exercise's tags."""
    def wc(col, val):
        rv = rule[col]
        return rv is None or rv == val
    if not wc("match_movement", ex["movement"]):
        return False
    if not wc("match_load_type", ex["load_type"]):
        return False
    if not wc("match_measure", ex["measure"]):
        return False
    # machine-derived predicates (loading method / cable lines)
    if rule["match_loading"] is not None:
        mloading = mac["loading_method"] if mac is not None else None
        if mloading != rule["match_loading"]:
            return False
    if rule["match_cable_lines"] is not None:
        mcl = mac["cable_lines"] if mac is not None else None
        if mcl != rule["match_cable_lines"]:
            return False
    # injury predicate: fires only when the exercise carries an injury tag.
    if rule["match_has_injury"] == 1:
        if not tags.get("injury"):
            return False
    return True


def evaluate_rules(conn, exercise_ulid, machine_ulid=None):
    """P1: fetch active rules priority-ascending, return the ordered list of
    matched rules for (exercise, machine). FIRST match per dimension wins is
    applied by the action layer (each action_kind is one dimension).

    REFUSES an unseeded DB (2026-09-12). ax_projection_rule is seeded by this
    pack's MANUAL post-install step, and an unseeded table used to produce a
    perfectly quiet wrong answer: no rule matches, apply_actions hands back the
    RAW target unrounded, fired_rules is [], _f6_fired is False, and serve()
    therefore drops the empty-bar ramp -- exit 0, no error, an unsnapped weight
    and no warmup on the owner's card. Zero rows is not "no rule applies"; it is
    "this install cannot answer". The two are told apart HERE, at the one funnel
    every projection path goes through, rather than at each of its callers."""
    require_taxonomy(conn, "ax_projection_rule")
    ex = _exercise_row(conn, exercise_ulid)
    if ex is None:
        raise ValueError("ax_exercise not found: %s" % exercise_ulid)
    mac = machine_row(conn, machine_ulid) if machine_ulid else None
    tags = _exercise_tags(conn, exercise_ulid)
    rules = conn.execute(
        "SELECT * FROM ax_projection_rule WHERE status='active' "
        "ORDER BY priority ASC, code ASC;").fetchall()
    matched = [r for r in rules if _rule_matches(r, ex, mac, tags)]
    return ex, mac, tags, matched


def _lattice_from_machine(mac):
    """Build a snap_to_lattice profile dict from an ax_machine row's
    lattice_base/step. loading_method/smith influence type; default 'stack'
    when an explicit base+step pair is present (a measured discrete grid)."""
    if mac is None:
        return None
    lb = mac["lattice_base"]
    ls = mac["lattice_step"]
    if lb is None or ls is None:
        return None
    return {"type": "stack", "base": float(lb), "step": float(ls)}


def _freeweight_lattice(param, exercise_name, step_type):
    """Build a snap_to_lattice profile for a freeweight (no-machine) barbell/
    dumbbell exercise from a lattice_round rule's action_param 'freeweight_grid'
    map (owner-supplied plate model, not invented). The map keys each exercise
    NAME to a grid entry:
      {"type": "standard"|"even", "base": <kg>, "coarse_step": <kg>,
       "working_step": <kg>}
    coarse_step is the public-plate grid used on warmup/ramp sets (per-side
    public plate). working_step is the finer grid the owner's personal light
    plates allow, permitted ONLY on working sets of the main lift; warmup/ramp
    fall back to coarse_step. When working_step is absent the grid has no micro
    (coarse-only, e.g. deadlift/squat step 5.0). Returns a {type,base,step} dict
    for snap_to_lattice, or None when the exercise has no grid entry (then the
    value is left unchanged -- same 'trust the raw math' default as rx-calc for
    a lattice-less freeweight slot such as bicep_curl)."""
    grids = param.get("freeweight_grid") if isinstance(param, dict) else None
    if not isinstance(grids, dict):
        return None
    g = grids.get(exercise_name)
    if not isinstance(g, dict):
        return None
    ltype = g.get("type", "standard")
    base = g.get("base", 0.0)
    coarse = g.get("coarse_step")
    working = g.get("working_step")
    # working-set micro grid (owner rule): personal light plates only on the
    # main lift's WORKING sets. warmup/ramp/prep use the coarse public grid.
    if working is not None and step_type == "working":
        step = working
    else:
        step = coarse
    if step is None:
        return None
    return {"type": ltype, "base": float(base), "step": float(step)}


def apply_actions(conn, ex, mac, tags, matched, target_raw, step_type=None):
    """P2: run the matched actions. Returns (realized_value, realized_detail,
    fired_codes, rule_ref). Weight-rounding actions (lattice/plate) resolve the
    realized load; non-load actions (ramp/injury/order/tut/cable) annotate the
    detail (they shape the sequence, not the single realized number).
    step_type (us_step.step_type: prep/warmup/ramp/working/hold) gates the
    freeweight working-set micro grid; None = coarse grid only."""
    detail = {"actions": []}
    realized = target_raw
    rule_ref = None
    fired = []
    for r in matched:
        kind = r["action_kind"]
        fired.append(r["code"])
        if rule_ref is None:
            rule_ref = r["ulid"]
        param = {}
        if r["action_param"]:
            try:
                param = json.loads(r["action_param"])
            except Exception:
                param = {"raw": r["action_param"]}
        entry = {"code": r["code"], "kind": kind}
        if kind == "lattice_round":
            # Machine-derived lattice (cable pin stack / discrete machine grid)
            # takes precedence; freeweight (no machine) falls back to the rule's
            # owner-supplied freeweight_grid keyed by exercise + step_type.
            lat = _lattice_from_machine(mac)
            if lat is None:
                lat = _freeweight_lattice(param, ex["exercise_name"], step_type)
                if lat is not None:
                    entry["step_type"] = step_type or "coarse"
            if lat is not None and target_raw is not None:
                realized = snap_to_lattice(realized, lat)
                entry["lattice"] = lat
                entry["realized"] = realized
            else:
                entry["note"] = "no_lattice_on_machine"
        elif kind == "plate_projection":
            plates = None
            if mac is not None and mac["available_plates"]:
                try:
                    plates = json.loads(mac["available_plates"])
                except Exception:
                    plates = None
            side = (mac["loading_side"] if mac is not None else None) or "per_side"
            rv, pd = project_plates(realized, plates, loading_side=side)
            if rv is not None:
                realized = rv
                entry["plate_detail"] = pd
                entry["realized"] = realized
        elif kind == "cable_line_specify":
            entry["require"] = param.get("require", "which_line")
            entry["cable_lines"] = (mac["cable_lines"] if mac is not None
                                    else None)
        elif kind == "empty_bar_ramp":
            entry["prepend"] = param
        elif kind == "injury_drill_include":
            entry["injury_tags"] = sorted(tags.get("injury", []))
        elif kind == "order_defer":
            grp = param.get("when_tag_group", "muscle")
            want = set(param.get("tag_in", []))
            entry["defer"] = bool(tags.get(grp, set()) & want)
        elif kind == "tut_progression":
            entry["prefer_measure"] = param.get("prefer_measure", [])
        else:
            entry["note"] = "unknown_action_kind"
        detail["actions"].append(entry)
    return realized, detail, fired, rule_ref


def _step_type_for(conn, step_ref, step_type):
    """Resolve the effective step_type for the freeweight working-set gate.
    An explicit step_type wins (standalone/dry-run projection). Otherwise, when
    a us_step ulid is supplied, read its step_type from the row. None when
    neither is available (coarse grid)."""
    if step_type:
        return step_type
    if step_ref:
        row = conn.execute(
            "SELECT step_type FROM us_step WHERE ulid=?;", (step_ref,)
        ).fetchone()
        if row is not None:
            return row["step_type"]
    return None


def project(conn, exercise_ulid, machine_ulid, target_raw, step_ref=None,
            write=True, step_type=None):
    """P1-P4 top level. Evaluate rules, gate the machine (JIT), apply actions,
    and (P3) write an ax_projection_slot row. Returns a result dict. When the
    JIT gate blocks, no slot is written and the block is returned for the caller
    (the CLI turns it into an exit-2 needs-fields signal).
    step_type overrides the us_step-derived set class (prep/warmup/ramp/working/
    hold) for the freeweight micro-grid gate; used for standalone/dry-run calls
    that have no us_step row yet."""
    ex, mac, tags, matched = evaluate_rules(conn, exercise_ulid, machine_ulid)
    # P4 / J1: JIT gate before prescribing.
    gate = jit_probe(conn, machine_ulid, ex["load_type"])
    if not gate.get("ok"):
        return {"blocked": True, "gate": gate, "exercise_ref": exercise_ulid}
    eff_step_type = _step_type_for(conn, step_ref, step_type)
    realized, detail, fired, rule_ref = apply_actions(
        conn, ex, mac, tags, matched, target_raw, step_type=eff_step_type)
    provisional = 1 if (mac is not None and mac["provisional"] == 1) else 0
    result = {
        "blocked": False,
        "exercise_ref": exercise_ulid,
        "machine_ref": machine_ulid,
        "target_raw": target_raw,
        "realized_value": realized,
        "realized_detail": detail,
        "fired_rules": fired,
        "rule_ref": rule_ref,
        "provisional": provisional,
    }
    # ax_projection_slot.step_ref is NOT NULL: a realized slot exists only FOR
    # a us_step. Standalone projection (no step) computes the value without
    # persisting -- the CLI reports it, and the slot is written when a step is
    # supplied (the render/delivery layer links them). No step -> no write.
    if write and step_ref:
        slot_ulid = new_ulid()
        conn.execute(
            "INSERT INTO ax_projection_slot (ulid, owning_agent, step_ref, "
            "exercise_ref, machine_ref, target_raw, realized_value, "
            "realized_detail, provisional, rule_ref, created_at) VALUES "
            "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
            (slot_ulid, owning_agent_for(conn), step_ref, exercise_ulid,
             machine_ulid, target_raw,
             realized, json.dumps(detail, ensure_ascii=True), provisional,
             rule_ref, now_iso()))
        conn.commit()
        result["slot_ulid"] = slot_ulid
    return result


# ===========================================================================
# SERVE (S1) -- session/slot last-mile bridge.
# The live workout skill speaks (session_ref=rotation_day, slot=seq); the
# projection primitive speaks (exercise_ulid, machine_ulid, us_step_ref).
# serve() is the THIN orchestration seam between them: resolve the working
# us_step for (session, slot) -> its exercise + machine -> run project() WITH
# the step link so ax_projection_slot MATERIALIZES -> compose the skill-facing
# response (realized_value / provisional / gate_needs / exercise_name /
# warmup / equipment). No new projection or warmup logic -- reuse only.
# ===========================================================================
def _working_step(conn, session_ref, slot_num):
    """S1: the 'working' us_step for (session_ref, seq=slot_num). seq IS the
    slot number (one working step per slot in the rotation-day sequence).
    Returns the row or None."""
    return conn.execute(
        "SELECT * FROM us_step WHERE session_ref=? AND seq=? AND "
        "step_type='working';", (session_ref, slot_num)).fetchone()


def _warmup_steps(conn, session_ref, slot_seq):
    """S1: the ordered prep/warmup/ramp us_step rows that PRECEDE this slot's
    working set (seq < slot_seq, in the same session). These are the pre-working
    steps the skill lists as 'warmup'. Rendered via us_render so cue/line text
    is composed the same way the delivery path does (climb-the-ladder: reuse the
    render composition, do not re-derive it). Sessions with no prep/warmup/ramp
    steps yield an empty list."""
    import us_render as US
    rows = conn.execute(
        "SELECT * FROM us_step WHERE session_ref=? AND seq<? AND "
        "step_type IN ('prep', 'warmup', 'ramp') ORDER BY seq ASC;",
        (session_ref, slot_seq)).fetchall()
    return [US.render_step(conn, r) for r in rows]


# Empty-bar weight for the F6 ramp start (standard olympic bar). Matches the
# project_plates default bar_kg -- the ramp begins with just the bar.
_EMPTY_BAR_KG = 20.0
# ---------------------------------------------------------------------------
# SINGLE-PLATE-PER-SIDE ramp ladder (owner spec, warmup-stretch.md B7/F6, 스냅
# 우선 재확정 2026-08-15 + batch G11). Root fix 2026-08-16: replaces the old
# %-based fractional ramp (_RAMP_FRACTIONS 0.4/0.6/0.8 then grid-snap), which
# produced awkward grid-snapped values (60 -> 24/36/48; 75 -> 30/45-type 2-plate
# combos) the owner corrected every session.
#
# Algorithm (top-down from the working weight):
#   - Pick ONE per-side step-plate size and add that same plate one-per-side per
#     rung from the empty bar: rung = bar + 2*plate*k (k=1,2,...). NEVER mix
#     plate sizes -> no 2-plate combos (30/45/24/36).
#   - Choose the LARGEST step-plate that yields ~2-4 clean rungs (target 2
#     intermediate rungs between the empty bar and the working weight).
#   - The 20% single-jump cap is a SOFT background guide, not the primary gate:
#     awkward in-between values are dropped even if a jump is bigger (fine for
#     RIR 4+ light ramp sets).
#   - Empty bar (20kg) is the default first rung; no step between the bar and
#     the first weight.
#   - Only the FINAL-APPROACH jump stays tight (<=15%) for heavy/technical/
#     injury-sensitive lifts (OHP class), by CHOOSING a smaller uniform step
#     when one lands the final tight -- never by inserting an off-cadence rung.
#   - No micro plates (1.25/0.75) on ramp step rungs.
# Plate denominations are a physical inventory constant (per-side, descending):
# reference rack = per-side 1.25/2.5/5/10/15/20/25; micro 1.25 excluded from
# stepping, 25 excluded (never needed for a 2-4 rung ramp -- 20 is the largest
# step the examples reach). Rungs are additionally gated to the exercise's coarse
# grid via _freeweight_lattice, so a lift with a coarser grid still snaps clean.
# ---------------------------------------------------------------------------
_RAMP_STEP_PLATES = (20.0, 15.0, 10.0, 5.0, 2.5)   # per-side, descending
_RAMP_TARGET_INTERMEDIATES = 2                     # bar + 2 + working = sweet spot
_RAMP_MIN_INTERMEDIATES = 1
_RAMP_MAX_INTERMEDIATES = 3
_RAMP_FINAL_TIGHT_FRAC = 0.15                      # heavy final-approach cap (<=15%)


def _f6_fired(realized_detail):
    """True iff project() emitted the F6 empty_bar_ramp directive for this slot
    (a freeweight working set whose realized_detail carries the ramp action)."""
    if not isinstance(realized_detail, dict):
        return False
    for a in realized_detail.get("actions", []):
        if a.get("kind") == "empty_bar_ramp":
            return True
    return False


def _ramp_intermediates(working_weight, step_plate):
    """Intermediate rung weights strictly between the empty bar and the working
    weight for ONE per-side step plate: bar + 2*step_plate*k for k=1,2,...,
    while < working. Single-plate-per-side => every rung is bar + k uniform
    plates per side (no plate-size mixing). Ascending list."""
    out = []
    k = 1
    while True:
        w = _EMPTY_BAR_KG + 2.0 * step_plate * k
        if w >= working_weight - 1e-9:
            break
        out.append(round(w, 4))
        k += 1
    return out


def _ramp_pick_step(working_weight, heavy=False):
    """Pick the single per-side step-plate for the ladder. Every candidate keeps
    UNIFORM plate cadence (one denomination, no 2-plate combos) with an
    intermediate-rung count in [MIN, MAX]. Primary ranking: count closest to
    _RAMP_TARGET_INTERMEDIATES (2), ties to the LARGER plate. For a HEAVY/
    technical/injury-sensitive lift, final-approach tightness (top intermediate
    -> working <=15%) leads -- so among clean options the one landing tight wins
    (OHP 42.5: step 5 -> 40 -> 42.5 = 5.9%), keeping the final tight by CHOOSING
    a step, never inserting an off-cadence rung (no 30/45/115-type combo, ladder
    stays <= MAX rungs). When no clean step lands the final tight (heavy compound
    with a large plate-quantized final gap), the % cap softens (owner: cap is a
    soft guide, single-plate is the primary driver) and count alone decides --
    matching the doc's un-tightened squat 80 -> 100. Returns (step_plate,
    intermediates) or (None, []) when no plate gives a clean in-range count."""
    cands = []
    for p in _RAMP_STEP_PLATES:
        ints = _ramp_intermediates(working_weight, p)
        n = len(ints)
        if _RAMP_MIN_INTERMEDIATES <= n <= _RAMP_MAX_INTERMEDIATES:
            final_tight = 0 if (working_weight and
                                (working_weight - ints[-1]) <=
                                working_weight * _RAMP_FINAL_TIGHT_FRAC + 1e-9) \
                else 1
            count_dist = abs(n - _RAMP_TARGET_INTERMEDIATES)
            key = (final_tight, count_dist) if heavy else (count_dist,)
            cands.append((key, p, ints))
    if not cands:
        return None, []
    best = min(range(len(cands)), key=lambda i: cands[i][0])
    return cands[best][1], cands[best][2]


# ---------------------------------------------------------------------------
# SHARED ramp-rep taper + ramp RIR -- SINGLE SOURCE OF TRUTH (5.6 SoT unify,
# 2026-08-21). Both consumers read THIS module:
#   * the SPOKEN warmup cue      -- _f6_ramp_sets() below stamps reps/rir onto
#                                   every serve.warmup ramp_set item, so the
#                                   model echoes a code-provided number instead
#                                   of inferring one (doctrine D2: deterministic
#                                   mechanism > agent discretion).
#   * the RENDERED set table (표2) -- files/program/set-table imports
#                                   ramp_taper_reps + RAMP_RIR from here
#                                   (lazy importlib, mirroring its load_rx_calc
#                                   and this module's own _load_kit_life).
# Dependency direction is deliberate: ax_engine.py is installed PACK code
# (pack_install.sh 2e), files/program/* is instance-local program tooling, so
# the instance depends on the pack and never the reverse.
#
# Ramp RIR is a fixed intensity anchor, not a computed value (workout-session
# SKILL.md "ramp-up 세트: RIR 4+", warmup-stretch.md). It is emitted verbatim so
# the cue "40kg x8 (RIR 4+)" needs no model-side fill-in.
RAMP_RIR = "4+"

# ---------------------------------------------------------------------------
# SHARED plate math -- SINGLE SOURCE OF TRUTH (#39-B, owner 2026-08-21).
# The per-side plate breakdown used to live ONLY in files/program/set-table,
# where it fed a static "[원판]" block at the bottom of the set table. The owner
# retired that block ("원판은 바로 세트표에 넣는게 아니라, 세트 하나하나 설명할때
# 설명해줘야해") -- the breakdown now rides the DETERMINISTIC per-set cue
# (set-arm's set-start push), for THE ONE weight being cued. Two consumers, so
# the math moves here exactly like ramp_taper_reps did:
#   * set-table  -> planned_ramp_rows' per-rung `plate_note` (delegation)
#   * set-arm    -> the one-line plate cue on the set-start push
# Import direction is unchanged: instance program tooling -> installed pack code.
EMPTY_BAR_KG = 20.0     # standard olympic bar (the ONLY bar the reference rack stocks)


def _fmt_kg_token(v):
    """20.0 -> '20', 26.25 -> '26.25'. Drops a trailing .0 only when whole so a
    micro-plate load keeps its decimal."""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return str(v)
    return str(int(f)) if f.is_integer() else str(round(f, 4))


def plate_breakdown(total_weight, bar_kg=EMPTY_BAR_KG):
    """The per-side plate load the owner actually has to put on for a TOTAL barbell
    weight -- '바 20kg + 양쪽 N kg' (N = (total - bar) / 2).

    Returns a user-facing note string, or "" when there is nothing to load
    (empty bar or below) / the input is unusable. NEVER raises -- a plate-math
    miss must never break a set table or a set-start push.

    Vocabulary is fixed by the existing loading-unit rules (set-table
    _LOADING_LABELS: 총 / 한쪽당 / 양쪽당): the bar+per-side composition is the
    '양쪽당' form, so the string reads '양쪽 Nkg' verbatim. Do NOT invent a new
    unit phrase here -- both consumers render this string as-is."""
    try:
        per_side = (float(total_weight) - float(bar_kg)) / 2.0
    except (TypeError, ValueError):
        return ""
    if per_side <= 1e-9:
        return ""   # empty bar (or below): no plates to load
    return "바 %skg + 양쪽 %skg" % (_fmt_kg_token(bar_kg),
                                    _fmt_kg_token(per_side))


# exercise_movement_grip.equipment values whose ax_exercise row the pack CAN
# ship. The boundary is the kit's own DDL, not a preference:
#     CHECK (load_type NOT IN ('machine','cable') OR machine_ref IS NOT NULL)
# so machine / smith_machine / v_squat_machine / cable lifts cannot have a row
# without an ax_machine row, and an ax_machine row is one gym's one machine
# (ax_machine.gym_id -> place) -- instance data, registered by ax-jit at the
# machine. This tuple is the same rule health_taxonomy_seed.sql's ax_exercise
# block derives its rows from, stated here because this is the other reader of
# it. Keep the two in step; the seed file's block comment says so too.
# 'bodyweight' (push-up, lunge) joined with the 2026-09-26 catalog expansion.
SEEDABLE_EQUIPMENT = ("barbell", "dumbbell", "ez_bar", "t_bar",
                      "bodyweight_assist", "bodyweight", "kettlebell",
                      "trap_bar", "medicine_ball")

# exercise_movement_grip.movement values that are HOLDS (seconds). Their
# ax_exercise row would need a hold_sec nobody measured, so the seed skips
# them and a missing row is not a defect. Mirrors
# exercise_catalog.HOLD_MOVEMENTS (tested equal).
HOLD_MOVEMENTS = ("plank", "wall_sit")

_CLASS_MISS_ANNOUNCED = set()


def _announce_class_miss_once(db_path, exercise_name, conn):
    """ONE stderr line per (db, exercise) when ax_exercise cannot classify a
    lift THE SHIPPED TAXONOMY ALREADY KNOWS.

    WHY THIS IS A MARKER AND NOT A FALLBACK (2026-09-14, the decision behind
    the ax_exercise seed). The alternative repair on the table was: let this
    function fall back to exercise_movement_grip (equipment='barbell' ->
    compound/freeweight) and never seed ax_exercise at all. That reads the
    right answer off the wrong table -- movement_grip carries movement+grip
    and nothing else, so a derived row can answer 2 of ax_exercise's 12
    columns and none of `measure`, `tempo`, `hold_sec`, `machine_ref` or
    `status`. Worse, it would make an empty catalog INVISIBLE forever, which
    is the exact defect class the 2026-09-12 audit exists about: nine gaps
    that were silent while every file was present.

    So the catalog is seeded, and a miss says so. The gate is deliberately
    NARROW -- two conditions, both required:

      1. exercise_movement_grip HAS the name. An unknown lift (the owner's own,
         not in any shipped table) is not a defect and stays silent.
      2. its equipment is one the SEED COULD HAVE COVERED (SEEDABLE_EQUIPMENT).
         A machine or cable lift has no ax_exercise row BY DESIGN until ax-jit
         registers the machine it hangs off -- the kit's own CHECK forbids the
         row without a machine_ref, and the machine is a specific machine in a
         specific gym. Crying "unclassified" once per machine lift per session
         would train the reader to ignore the line that matters.

    Condition 2 is what keeps this a defect marker instead of a status report.
    Measured: without it, a fully and correctly seeded fresh instance still
    printed this line for leg_curl and lat_pulldown."""
    try:
        key = (os.path.abspath(str(db_path)), exercise_name)
        if key in _CLASS_MISS_ANNOUNCED:
            return
        _CLASS_MISS_ANNOUNCED.add(key)
        known = conn.execute(
            "SELECT equipment, movement FROM exercise_movement_grip WHERE "
            "exercise_name=? LIMIT 1;",
            (exercise_name,)).fetchone()
        if known is None or known[0] not in SEEDABLE_EQUIPMENT or \
                known[1] in HOLD_MOVEMENTS:
            return
        sys.stderr.write(
            "[ax_engine] AX-EXERCISE-UNCLASSIFIED: %r has a shipped taxonomy "
            "row (exercise_movement_grip) but NO ax_exercise row, so its "
            "movement/load class is unknown -- the empty-bar rung, the ramp "
            "taper and the plate cue are all silently off for this lift. "
            "Fix: %s\n"
            % (exercise_name, taxonomy_seed_command(db=db_path)))
    except Exception:      # noqa: BLE001 -- a diagnostic never breaks the read
        return


def exercise_class(db_path, exercise_name):
    """(movement, load_type) for an ACTIVE ax_exercise row, else (None, None).

    Best-effort: any DB error -> (None, None). Deliberately a bare sqlite3 read
    (not connect()) so it never needs the kit_life substrate and can be called
    from instance program tooling that only has a db path.

    A MISS IS NAMED, NOT SWALLOWED (2026-09-14): when the row is absent but the
    pack's own exercise_movement_grip knows the lift, one stderr line says so --
    see _announce_class_miss_once for why that is a marker rather than a
    fallback."""
    try:
        conn = sqlite3.connect(db_path)
        try:
            row = conn.execute(
                "SELECT movement, load_type FROM ax_exercise "
                "WHERE exercise_name=? AND status='active' LIMIT 1;",
                (exercise_name,)
            ).fetchone()
            if row is not None:
                return (row[0], row[1])
            _announce_class_miss_once(db_path, exercise_name, conn)
            return (None, None)
        finally:
            conn.close()
    except Exception:      # noqa: BLE001 -- a class miss must never break a cue
        return None, None


def is_free_weight_compound(db_path, exercise_name):
    """The RAMP-KIND gate: True iff the exercise is compound + freeweight in
    ax_exercise. This is the historical F6 barbell-ramp predicate, moved here
    verbatim from files/program/set-table._is_ramp_exercise so the ramp branch
    and the plate cue read one definition. Best-effort: any error -> False."""
    movement, load_type = exercise_class(db_path, exercise_name)
    return movement == "compound" and load_type == "freeweight"


# program.yaml `lattice.type` values that mean "this load is NOT a bar you put
# plates on". DGN-387: `even` = 고정덤벨 짝수kg만 (fixed dumbbells), `stack` = a
# stack pin. `standard` (총 2.5/5kg 그리드) IS the bar+plate grid.
NON_PLATE_LATTICE_TYPES = ("even", "stack")


def is_plate_loaded(db_path, exercise_name, lattice_type=None):
    """True iff this lift is loaded with a BAR + PLATES -- the only class for
    which plate_breakdown() means anything. Machines, stacks, cables, bodyweight
    AND FIXED DUMBBELLS are all False: their number is read off a pin or stamped
    on the bell, so a '바 20kg + 양쪽 N kg' line would be nonsense.

    Two signals, both data-backed (never a prose keyword scan -- that was the
    #24/#25 false-positive class):
      1. ax_exercise says compound + freeweight (is_free_weight_compound), and
      2. the program.yaml slot's `lattice.type` is not a NON_PLATE one.

    WHY (2) EXISTS -- pre-existing live bug, found 2026-08-21: signal (1) alone
    calls incline_dumbbell_press "barbell" (it IS compound + freeweight), so the
    retired set-table [원판] block really did print '28.0kg (워킹) = 바 20kg +
    양쪽 4kg' for a DUMBBELL press. Removing the block retired that surface; this
    gate is what stops the same nonsense reappearing on the per-set cue, which
    would show it once per SET instead of once per table.

    `lattice_type` is optional so a caller with no slot in hand degrades to
    signal (1) -- the historical behavior, never stricter than before."""
    if not is_free_weight_compound(db_path, exercise_name):
        return False
    if lattice_type is not None and \
            str(lattice_type).strip().lower() in NON_PLATE_LATTICE_TYPES:
        return False
    return True


# PLATE-LOADED MACHINES (owner ruling 2026-10-03). A leg press / hack squat /
# plate-loaded shoulder press is loaded with plates too, but there is no bar:
# is_plate_loaded() above is False for it by design, and plate_breakdown()'s
# "(total - 20) / 2" is meaningless for it. What the owner needs is what the
# number MEANS -- one side's load or the whole load -- so this answers that and
# nothing else (no plate inventory, no decomposition into plate counts).
#
# Data-backed, two signals:
#   1. the machine is ax_machine.loading_method = 'plate_loaded' -- the machine
#      the session chose (machine_ulid, from machine_capture) when known, else
#      the exercise's bound ax_exercise.machine_ref;
#   2. the meaning of the number: the program.yaml slot `loading` when it says
#      (per_side | total | single), else the machine's own loading_side.
# A stack / cable / assist machine, a free weight, or any DB miss -> None.
PLATE_MACHINE_METHOD = "plate_loaded"
_PLATE_MACHINE_LOADING = {"per_side": "per_side", "total": "total",
                          "single": "total"}


def plate_machine_loading(db_path, exercise_name, slot_loading=None,
                          machine_ulid=None):
    """'per_side' | 'total' for a PLATE-LOADED MACHINE, else None. Never
    raises."""
    try:
        conn = sqlite3.connect(db_path)
        try:
            row = None
            if machine_ulid:
                row = conn.execute(
                    "SELECT loading_method, loading_side FROM ax_machine "
                    "WHERE ulid=? LIMIT 1;", (machine_ulid,)).fetchone()
            if row is None:
                row = conn.execute(
                    "SELECT m.loading_method, m.loading_side FROM ax_exercise e "
                    "JOIN ax_machine m ON m.ulid = e.machine_ref "
                    "WHERE e.exercise_name=? AND e.status='active' LIMIT 1;",
                    (exercise_name,)).fetchone()
        finally:
            conn.close()
    except Exception:      # noqa: BLE001 -- a gate miss must never break a cue
        return None
    if not row or row[0] != PLATE_MACHINE_METHOD:
        return None
    declared = _PLATE_MACHINE_LOADING.get(str(slot_loading or "").strip())
    if declared:
        return declared
    return _PLATE_MACHINE_LOADING.get(str(row[1] or "").strip(), "total")


def _ramp_row_is_empty_bar(row):
    """True iff a ramp row is the empty-bar rung, across BOTH row shapes that
    reach ramp_taper_reps: the engine payload keys it `rung == 'empty_bar'`
    (_f6_ramp_sets), the set-table planned row keys it `label == 'bw'`
    (planned_ramp_rows). Keyed on the tag, never on the weight alone -- a
    machine rung can legitimately BE 20.0kg without any bar existing."""
    if not isinstance(row, dict):
        return False
    return row.get("label") == "bw" or row.get("rung") == "empty_bar"


# Ramp reps as a FRACTION OF THE WORKING REP TARGET, by load band (owner
# 2026-08-24 live: "3회는 너무적은데.. 10회씩함" on a 25kg x 15 x 3 lift whose ramp
# was prescribed 15kg x 3).
#
# The grid below used to be ABSOLUTE rep counts (8/5/3/2) authored against a
# 5-8 rep barbell working set, and `working_top_rep` was accepted and DISCARDED.
# On a 15-rep isolation lift that produced a 3-rep "warm-up", which primes
# nothing. The rep target is not missing data -- it is passed in by BOTH call
# sites (set-table target_top_rep, set-arm working_reps); the grid just never
# read it.
#
# The multipliers are measured, not invented: fitted against the owner's OWN
# logged ramp rungs (workout_sets set_seq <= 0 joined to that session's working
# sets, n=61). Mean observed ramp_reps/working_reps per load band was
# 1.25 / 1.01 / 0.87 / 0.69, and the ratio holds across low-rep and high-rep
# working sets alike (it is the ratio that is stable, not the count -- band-D
# absolute reps were 4.4 on <=8-rep lifts vs 8.4 on >8-rep lifts). Against those
# 61 rungs this model scores MAE 2.00 vs 4.28 for the absolute grid, and drops
# gross misses (|err| >= 5 reps) from 25/61 to 6/61.
RAMP_REP_RATIO_BY_BAND = (1.2, 1.0, 0.85, 0.7)
# Degrade grid: the historical absolute counts, used ONLY when no working rep
# target is available (so a caller that passes none is byte-identical to before).
RAMP_REPS_NO_TARGET = (8, 5, 3, 2)
# Never below 2 (a 1-rep "warm-up" is not one) and never above the highest ramp
# rep count in the owner's own log (20, on a 20-rep face pull).
RAMP_REPS_MIN = 2
RAMP_REPS_MAX = 20


def _ramp_load_band(f):
    """Load-fraction (row weight / working weight) -> band index 0..3. Band
    boundaries are the long-standing declared ones; only what each band YIELDS
    changed (absolute count -> fraction of the working rep target)."""
    if f < 0.35:
        return 0
    if f < 0.55:
        return 1
    if f < 0.72:
        return 2
    return 3


def _working_rep_target(working_top_rep):
    """The working set's rep target as a positive int, or None when it is
    absent/unparseable. Accepts the int both call sites normally pass and the
    string form an F19 owner override can carry ('12', '8-10' -> top of range).
    Never guesses a number: unusable input -> None -> the degrade grid."""
    if isinstance(working_top_rep, bool):
        return None
    if isinstance(working_top_rep, (int, float)):
        v = int(working_top_rep)
        return v if v > 0 else None
    if isinstance(working_top_rep, str):
        nums = re.findall(r"\d+", working_top_rep)
        if nums:
            v = int(nums[-1])          # '8-10' -> the TOP of the range
            return v if v > 0 else None
    return None


def ramp_taper_reps(planned_ramp, working_weight, working_top_rep=None):
    """Reps for each planned ramp row, TAPERING as load climbs (5.6, owner
    2026-08-20: 'ramp reps 5 고정' bug). A warmup ramp primes the pattern with
    HIGH reps on the light bar and DROPS the reps as the plate climbs toward the
    working weight -- never a constant 5. Returns a list of ints, one per row in
    `planned_ramp`, monotonically non-increasing.

    Row shape is duck-typed so the SAME grid serves the engine payload
    ({'rung','weight_kg'}) and the set-table planned row ({'label','weight_kg'})
    -- see _ramp_row_is_empty_bar.

    Two inputs, both required for a correct number:
      * WHERE on the ramp this rung sits -- the load fraction
        f = row_weight / working_weight, banded by _ramp_load_band.
      * WHAT rep band the lift is trained in -- `working_top_rep`. A ramp rung is
        a fraction of the working rep target (RAMP_REP_RATIO_BY_BAND), never a
        fixed count: 3 reps is a real warm-up under a 5-rep deadlift and no
        warm-up at all under a 15-rep leg extension. See the block above for the
        measured fit.
    A warmup rung legitimately does FEWER reps than the working set as the load
    nears the working weight, so the taper is NOT floored at the working rep
    count -- only at RAMP_REPS_MIN. Empty-bar rows always take the top band.
    When the working weight is unknown the fraction cannot be computed, so the
    band falls back to row POSITION; when the working rep target is unknown the
    historical absolute grid (RAMP_REPS_NO_TARGET) stands."""
    n = len(planned_ramp)
    if n == 0:
        return []
    reps = []
    have_working = isinstance(working_weight, (int, float)) and working_weight > 0
    target = _working_rep_target(working_top_rep)
    for idx, pr in enumerate(planned_ramp):
        if _ramp_row_is_empty_bar(pr):
            band = 0
        elif have_working:
            w = pr.get("weight_kg")
            if not isinstance(w, (int, float)) or w <= 0:
                band = 1
            else:
                band = _ramp_load_band(float(w) / float(working_weight))
        else:
            # Position taper when load fraction is not computable.
            band = idx if idx < 4 else 3
        if target is None:
            base = RAMP_REPS_NO_TARGET[band]
        else:
            base = int(round(target * RAMP_REP_RATIO_BY_BAND[band]))
            base = max(RAMP_REPS_MIN, min(RAMP_REPS_MAX, base))
        reps.append(base)
    # Enforce monotonic non-increasing (guard against grid non-monotonicity from
    # an irregular rung spacing): each row is at most the previous row's reps.
    for i in range(1, len(reps)):
        if reps[i] > reps[i - 1]:
            reps[i] = reps[i - 1]
    # Never below 2.
    reps = [max(2, r) for r in reps]
    return reps


def _f6_ramp_sets(param, exercise_name, working_weight, heavy=False,
                  working_reps=None):
    """Expand the F6 empty_bar_ramp directive into CONCRETE warmup ramp sets via
    the SINGLE-PLATE-PER-SIDE ladder (owner spec; see the module block above).
    empty bar (20 kg) then uniform single-plate rungs climbing to -- but not
    reaching -- the realized working weight. Every rung is additionally gated to
    the exercise's COARSE public-plate grid (warmup/ramp use coarse, never the
    working micro grid) via _freeweight_lattice + snap_to_lattice, so a lift with
    a coarser grid still snaps clean and no rung is unloadable. `heavy` keeps the
    final approach tight for OHP-class lifts. Returns an ordered list of ramp-set
    dicts (render='ramp_set'). Empty when working is at/below the empty bar.

    Each rung additionally carries `reps` (ramp_taper_reps -- the SAME taper the
    set table renders) and `rir` (RAMP_RIR), because the SKILL warmup-cue
    contract is 무게 + 목표 횟수 + RIR ("40kg x8 (RIR 4+)"). Without these
    fields the spoken rep count was a model inference while the table tapered --
    the exact prompt-layer dependency doctrine D2 forbids for a MUST-happen
    behaviour."""
    if working_weight is None or working_weight <= _EMPTY_BAR_KG:
        return []
    # coarse grid for this exercise (warmup/ramp public-plate grid). step_type
    # 'ramp' forces the coarse branch of _freeweight_lattice.
    lat = _freeweight_lattice(param, exercise_name, "ramp")

    _step, intermediates = _ramp_pick_step(working_weight, heavy=heavy)

    sets = []
    last_w = [None]   # last accepted rung weight (strictly-ascending guard)

    def _add(weight, tag):
        # Gate every rung to the exercise coarse grid (loadability), preserving
        # the pre-fix snap discipline. The single-plate ladder already lands on
        # the grid; snap is a defensive no-op there but protects a coarser grid.
        w = snap_to_lattice(weight, lat) if lat is not None else round(weight, 4)
        # ramp invariants (safety, unchanged): every rung must be
        #   - at/above the empty bar (never lighter than the bar),
        #   - strictly ABOVE the previous rung (a ramp only climbs), and
        #   - strictly BELOW the working weight (the working set is separate).
        if w is None or w < _EMPTY_BAR_KG or w >= working_weight:
            return
        if last_w[0] is not None and w <= last_w[0]:
            return
        last_w[0] = w
        sets.append({"render": "ramp_set", "step_type": "ramp",
                     "weight_kg": w, "rung": tag})

    # rung 0: empty bar (always first when it is below the working weight; the
    # single-plate intermediates all sit above the bar -- no gap step inserted).
    _add(_EMPTY_BAR_KG, "empty_bar")
    for idx, w in enumerate(intermediates, start=1):
        _add(w, "ramp_%d" % idx)
    # Stamp the tapered rep target + ramp RIR onto every rung. Computed AFTER the
    # invariant filtering above so the taper keys on the rungs that actually
    # survive (a dropped rung must not shift the ladder's rep positions).
    for row, r in zip(sets, ramp_taper_reps(sets, working_weight,
                                            working_reps)):
        row["reps"] = r
        row["rir"] = RAMP_RIR
    return sets


def _freeweight_grid_param(conn):
    """Fetch the owner's freeweight_grid map (the action_param carrying the
    coarse/working plate grids per exercise). It lives on the active lattice_round
    rule -- the same param apply_actions reads. Returns the parsed dict or {}.
    Reused by the F6 ramp expansion so warmup rungs snap to the SAME coarse grid
    the working-set projection uses (no second source of truth)."""
    rows = conn.execute(
        "SELECT action_param FROM ax_projection_rule WHERE status='active' AND "
        "action_kind='lattice_round';").fetchall()
    for r in rows:
        if not r["action_param"]:
            continue
        try:
            p = json.loads(r["action_param"])
        except Exception:
            continue
        if isinstance(p, dict) and isinstance(p.get("freeweight_grid"), dict):
            return p
    return {}


def _ramp_heavy(conn, exercise_ulid):
    """Deterministic heavy/technical/injury-sensitive flag for the ramp final-
    approach gate: True iff the exercise carries an ACTIVE injury tag (ax_tag
    tag_group='injury' via ax_exercise_tag). Owner spec (warmup-stretch.md F6):
    only heavy/technical/injury-sensitive lifts keep the FINAL approach tight
    (e.g. OHP for a shoulder injury tag). Reading the injury tag makes the flag data-driven (no
    hardcoded exercise list). Harmless for heavy compounds (squat/deadlift carry
    injury_knee): _ramp_pick_step softens the % cap when no clean tight step
    lands, so those keep their big single-plate final jump. Any DB error -> False
    (soft ramp), never a crash. NOTE (owner decision pending): if a lift should
    be tight-final WITHOUT an injury tag, a dedicated tag_group (e.g.
    'ramp':'tight_final') would be the clean source -- see report."""
    try:
        row = conn.execute(
            "SELECT 1 FROM ax_exercise_tag et "
            "JOIN ax_tag t ON t.ulid = et.tag_ref "
            "WHERE et.exercise_ref = ? AND t.tag_group = 'injury' "
            "AND t.status = 'active' LIMIT 1;",
            (exercise_ulid,)).fetchone()
        return row is not None
    except Exception:
        return False


def _equipment_of(conn, ex, mac, working_step):
    """S1: equipment classification for the slot. Prefer the machine label when
    a registered machine backs the exercise; else fall back to the exercise's
    load_type, annotated with the us_step's equipment_need flow flag."""
    machine_label = mac["label"] if mac is not None else None
    return {
        "load_type": ex["load_type"],
        "machine_ref": ex["machine_ref"],
        "machine_label": machine_label,
        "equipment_need": working_step["equipment_need"],
    }


def serve(conn, session_ref, slot_num, target_raw, write=True):
    """S1 top level: bridge (session_ref, slot_num) -> materialized projection
    + skill-facing response. Resolves the working us_step, links project() to it
    (so ax_projection_slot is written unless write=False), and composes the
    exact fields the workout-session skill consumes. When the JIT gate blocks
    (unregistered/incomplete machine), no slot is written and gate_needs carries
    the fields to ask -- the same forcing-point project()/ax-jit expose, surfaced
    at the serve layer."""
    step = _working_step(conn, session_ref, slot_num)
    if step is None:
        raise ValueError(
            "no working us_step for session=%s slot=%s" % (session_ref,
                                                           slot_num))
    exercise_ulid = step["exercise_ref"]
    ex = _exercise_row(conn, exercise_ulid)
    if ex is None:
        raise ValueError("ax_exercise not found: %s" % exercise_ulid)
    machine_ulid = ex["machine_ref"]
    mac = machine_row(conn, machine_ulid) if machine_ulid else None

    proj = project(conn, exercise_ulid, machine_ulid, target_raw,
                   step_ref=step["ulid"], write=write)

    # Seeded prep/warmup/ramp us_step rows (if any) come first in the sequence.
    seeded_warmup = _warmup_steps(conn, session_ref, step["seq"])
    resp = {
        "session_ref": session_ref,
        "slot": slot_num,
        "step_ref": step["ulid"],
        "exercise_name": ex["exercise_name"],
        "warmup": seeded_warmup,
        "equipment": _equipment_of(conn, ex, mac, step),
    }
    if proj.get("blocked"):
        # JIT gate blocked: no slot written; surface the needs-fields as
        # gate_needs so the skill can drive registration, then retry serve.
        gate = proj["gate"]
        resp.update({
            "realized_value": None,
            "provisional": 1,
            "gate_needs": gate.get("needs", []),
            "blocked": True,
            "gate_reason": gate.get("reason"),
        })
        return resp
    # SAFETY (F6): when the projection fires empty_bar_ramp for this working
    # slot, expand it into concrete ramp-UP-to-working-weight sets and PREPEND
    # them ahead of any seeded warmup. Without this the serve path drops the
    # ramp the interim rx-calc showed -- a warmup regression (owner: no warmup =
    # injury). Non-freeweight / no-F6 slots keep warmup as the seeded rows only.
    if _f6_fired(proj["realized_detail"]):
        grid_param = _freeweight_grid_param(conn)
        heavy = _ramp_heavy(conn, exercise_ulid)
        ramp = _f6_ramp_sets(grid_param, ex["exercise_name"],
                             proj["realized_value"], heavy=heavy,
                             working_reps=step["target"])
        resp["warmup"] = ramp + seeded_warmup
    resp.update({
        "realized_value": proj["realized_value"],
        "provisional": proj["provisional"],
        "gate_needs": [],
        "blocked": False,
        "realized_detail": proj["realized_detail"],
        "fired_rules": proj["fired_rules"],
    })
    if "slot_ulid" in proj:
        resp["slot_ulid"] = proj["slot_ulid"]
    return resp


# ===========================================================================
# TAXONOMY SEED STATE -- "did this pack's install-time seed ever run here?"
#
# WHY THIS LIVES IN ax_engine.py AND NOT IN ITS OWN MODULE (2026-09-12).
#   It was its own module for one afternoon. 26 shipped suites build a
#   throwaway tree by copying a NAMED SUBSET of this directory into it, and
#   every one of those lists carries `ax_engine.py` -- so a new sibling module
#   that ax_engine imports is absent in all 26 copied trees, `import ax_engine`
#   raises ModuleNotFoundError there, and set-add / set-arm / set-table swallow
#   that in their `except Exception` loaders. Measured: one suite went red and
#   25 kept reporting green against an engine that no longer loaded. That is
#   the SAME silent-degradation shape this section exists to close, so the
#   dependency is not created: the probe lives in the file every copy list
#   already names.
#
# WHY IT EXISTS AT ALL.
#   `health_taxonomy_seed.py --apply` is a MANUAL post-install step (the
#   framework's kind=pack pipeline is file-copy + ledger-write and has no
#   post-install execution hook of any kind), and the only place it was written
#   down was service/health/README.md -- which is not a caller. Measured on a
#   real fresh install of pack_health onto a kit_life 2.17.0 instance: all
#   ELEVEN seeded tables hold 0 rows, and nothing anywhere said so.
#
#   What that silence bought, on that same install:
#     * `ax-project rules`  -> printed NOTHING, exit 0.
#     * `ax-project serve`  -> evaluate_rules matched nothing, apply_actions
#       returned the RAW target unrounded, fired_rules was [], _f6_fired was
#       False, so serve() dropped the empty-bar ramp. Exit 0. An unsnapped
#       weight and no warmup on the owner's card, with no error anywhere.
#       ("no warmup = injury" is the owner's own ruling.)
#
#   An empty result set is an answer only when a non-empty one was possible. A
#   never-seeded table could not produce one, so it is told apart here.
#
# WHAT THIS IS NOT. Not a migration, not a writer, not a fallback. It never
# inserts a row and never invents a default rule -- a guessed projection rule
# would put a made-up number on a barbell.
# ===========================================================================
SEED_SCRIPT = os.path.join(_ENGINE_DIR, "health_taxonomy_seed.py")

# THE DECLARATION of what this pack seeds. Hand-written on purpose: it is also
# health_taxonomy_seed.SQL_GUARD's allowlist, i.e. the db_lane=false contract
# boundary ("the pack contract boundary is checked, not trusted"). Deriving it
# from health_taxonomy_seed.sql would make that guard check the seed file
# against itself and prove nothing. One declaration, two readers.
SEED_TABLES = (
    "muscle_node",
    "muscle_label",
    "exercise_muscle_map",
    "exercise_subregion_map",
    "exercise_pattern",
    "exercise_fatigue_cost",
    "exercise_movement_grip",
    "movement_muscle_base",
    "grip_vocab",
    "grip_muscle_delta",
    "ax_projection_rule",
    # ax_exercise (2026-09-14). The 12th table, and the one that was MISSING
    # from this declaration -- which is why the 2026-09-13 fresh-mint
    # simulation found it holding 0 rows with no writer anywhere while every
    # sibling held its rows and every probe said "seeded". Declaring it here is
    # what makes an unseeded catalog answer PARTIAL instead of SEEDED.
    # Only the freeweight/bodyweight half of the catalog is seedable -- see the
    # ax_exercise block in health_taxonomy_seed.sql for the CHECK that decides
    # that and why the machine/cable half is JIT-registered, not shipped.
    "ax_exercise",
)

# Verdicts. Ordered worst-first for reporting.
SCHEMA_MISSING = "schema_missing"   # the KIT's DDL is older than this pack
UNSEEDED = "unseeded"               # every seeded table is empty: never ran
PARTIAL = "partial"                 # some seeded, some empty: a ROW was removed
SEEDED = "seeded"                   # every seeded table holds rows
UNKNOWN = "unknown"                 # the DB could not be read at all

# Verdicts that mean "this DB cannot answer a taxonomy question truthfully".
BAD_VERDICTS = (SCHEMA_MISSING, UNSEEDED, PARTIAL)


class TaxonomyNotSeeded(RuntimeError):
    """The pack_health taxonomy seed has not run on this DB.

    A CONFIG DEFECT, deliberately not a subclass of ValueError: the ax-project
    CLI maps ValueError to exit 1 ("bad args / missing exercise"), and this is
    neither. It gets its own exit code so a caller can tell "you asked about a
    row that does not exist" apart from "this install is incomplete"."""

    def __init__(self, report, tables=()):
        self.report = report
        self.tables = tuple(tables)
        RuntimeError.__init__(self, taxonomy_one_line(report, tables))


def _tax_open(target):
    """Accept an open connection or a db path. Returns (conn, close_it)."""
    if isinstance(target, sqlite3.Connection):
        return target, False
    if not os.path.isfile(str(target)):
        raise FileNotFoundError("kit_life.db not found: %s" % target)
    return sqlite3.connect("file:%s?mode=ro" % target, uri=True), True


def taxonomy_probe(target, tables=SEED_TABLES):
    """Per-table state for the pack-seeded tables on this DB.

    Returns {"verdict": <str>, "db": <path or None>, "tables": {name: state},
             "counts": {name: int}, "missing": [...], "empty": [...],
             "seeded": [...], "error": <str or None>}
    where state is one of "missing" / "empty" / "seeded".

    Never raises on a DB-level problem: an unreadable DB is verdict UNKNOWN with
    the reason in ["error"]. A caller that wants a refusal calls require()."""
    report = {"verdict": UNKNOWN, "db": None, "tables": {}, "counts": {},
              "missing": [], "empty": [], "seeded": [], "error": None}
    close_it = False
    conn = None
    try:
        conn, close_it = _tax_open(target)
        try:
            report["db"] = conn.execute(
                "PRAGMA database_list;").fetchone()[2] or None
        except Exception:                                    # noqa: BLE001
            pass
        have = {r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table';")}
        for t in tables:
            if t not in have:
                report["tables"][t] = "missing"
                report["missing"].append(t)
                continue
            n = conn.execute("SELECT COUNT(*) FROM %s;" % t).fetchone()[0]
            report["counts"][t] = n
            if n == 0:
                report["tables"][t] = "empty"
                report["empty"].append(t)
            else:
                report["tables"][t] = "seeded"
                report["seeded"].append(t)
    except Exception as exc:                                 # noqa: BLE001
        report["error"] = "%s: %s" % (type(exc).__name__, exc)
        return report
    finally:
        if conn is not None and close_it:
            conn.close()

    if report["missing"]:
        report["verdict"] = SCHEMA_MISSING
    elif not report["seeded"]:
        report["verdict"] = UNSEEDED
    elif report["empty"]:
        report["verdict"] = PARTIAL
    else:
        report["verdict"] = SEEDED
    return report


def taxonomy_probe_complete(target, owning_agent=None):
    """ROW-complete taxonomy state: taxonomy_probe's report plus
    missing_rows / total_missing from the seed's own dry run on an in-memory
    snapshot (health_taxonomy_seed.check_report -- the exact --check logic).

    taxonomy_probe answers "does every seeded table hold rows"; a catalog
    top-up that never ran (e.g. the 2026-09-26 catalog block on an install
    seeded before it) still answers SEEDED there. Here it answers PARTIAL with
    the per-table count of rows the seed would add (overnight follow-ups
    2026-09-27 item 7). Costs one snapshot + one rolled-back seed pass, so
    call it once per session, never per set. Never raises: no seed script ->
    the presence report with error set; target must be a db PATH (the
    snapshot is taken read-only from it)."""
    if isinstance(target, sqlite3.Connection):
        rep = taxonomy_probe(target)
        rep["error"] = rep.get("error") or "row-complete probe needs a db path"
        return rep
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "health_taxonomy_seed_probe", SEED_SCRIPT)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod.check_report(str(target), owning_agent=owning_agent)
    except Exception as exc:                                 # noqa: BLE001
        rep = taxonomy_probe(target)
        rep["error"] = "row-complete probe unavailable: %s: %s" % (
            type(exc).__name__, exc)
        return rep


def taxonomy_seed_command(report=None, db=None):
    """The EXACT command that closes this, rendered absolute so it works from
    any cwd. Never a relative crib the reader has to re-anchor."""
    db_path = db or (report or {}).get("db") or os.path.join(
        _ENGINE_DIR, "..", "..", "database", "kit_life.db")
    return "python3 %s --db %s --apply" % (
        os.path.abspath(SEED_SCRIPT), os.path.abspath(db_path))


def taxonomy_one_line(report, tables=()):
    """One ascii line naming the defect. Used as the exception message."""
    named = ", ".join(tables) if tables else ""
    where = " (needed: %s)" % named if named else ""
    v = report.get("verdict")
    if v == SCHEMA_MISSING:
        return ("kit schema is missing %s -- the KIT owns this DDL; "
                "install/upgrade kit_life first"
                % ", ".join(report.get("missing", [])))
    if v == UNSEEDED:
        return ("pack_health taxonomy seed has NEVER run on this DB: all %d "
                "seeded tables hold 0 rows%s -- CONFIG DEFECT, not an empty "
                "answer. Fix: %s"
                % (len(report.get("empty", [])), where, taxonomy_seed_command(report)))
    if v == PARTIAL and not report.get("empty") and report.get("total_missing"):
        short = ", ".join("%s=%d" % (t, n) for t, n in
                          sorted((report.get("missing_rows") or {}).items()) if n)
        return ("pack_health taxonomy is INCOMPLETE: every table holds rows "
                "but the current seed would add %d (%s)%s -- a catalog top-up "
                "has not run on this DB. Fix: %s"
                % (report["total_missing"], short, where,
                   taxonomy_seed_command(report)))
    if v == PARTIAL:
        return ("pack_health taxonomy is PARTIALLY seeded: %s hold 0 rows%s "
                "-- rows were removed after seeding, or the seed was "
                "interrupted. Fix: %s"
                % (", ".join(report.get("empty", [])), where,
                   taxonomy_seed_command(report)))
    if v == UNKNOWN:
        return ("pack_health taxonomy state UNKNOWN -- the DB could not be "
                "read: %s" % report.get("error"))
    return "pack_health taxonomy is seeded"


def taxonomy_diagnostic(report, subject=None):
    """The multi-line operator/agent block. Named, actionable, no euphemism."""
    lines = []
    head = "[taxonomy] %s" % taxonomy_one_line(report)
    lines.append(head)
    if subject:
        lines.append("[taxonomy] asked for: %s" % subject)
    if report.get("verdict") in (UNSEEDED, PARTIAL):
        lines.append("[taxonomy] until it is seeded this install cannot snap a "
                     "weight to a real grid and cannot plan an empty-bar ramp; "
                     "any number it prints would be the raw arithmetic, "
                     "unrounded.")
        lines.append("[taxonomy] confirm with: python3 %s --db %s --check"
                     % (os.path.abspath(SEED_SCRIPT),
                        os.path.abspath(report.get("db") or "database/kit_life.db")))
    return "\n".join(lines)


def require_taxonomy(target, *tables):
    """Probe and REFUSE when the named tables cannot answer.

    tables defaults to the full seeded set. Raises TaxonomyNotSeeded on
    schema_missing / unseeded, and on partial WHEN one of the named tables is
    the empty one -- a partial seed elsewhere is not this caller's problem.
    Returns the report on success (verdict SEEDED, PARTIAL-but-not-mine, or
    UNKNOWN -- an unreadable DB is the caller's own error to raise, not ours)."""
    want = tables or SEED_TABLES
    report = taxonomy_probe(target)
    v = report["verdict"]
    if v == UNKNOWN or v == SEEDED:
        return report
    bad = [t for t in want if report["tables"].get(t) in ("empty", "missing")]
    if bad:
        raise TaxonomyNotSeeded(report, bad)
    return report
