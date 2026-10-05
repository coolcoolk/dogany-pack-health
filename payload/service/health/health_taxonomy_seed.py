#!/usr/bin/env python3
# health_taxonomy_seed.py -- install the pack_health taxonomy rows into the
# kit_life DB. Idempotent. Never clobbers. Dry-run by default.
#
# WHY THIS EXISTS
#   dogany-lifekit's payload/database/schema.sql used to INSERT 370 rows of
#   muscle / exercise classification at every fresh mint. That made the kit ship
#   a trainer's product knowledge to instances that will never train -- the
#   owner's objection, and correctly a SEEDING defect, not a storage one.
#
#   The TABLES stay in the kit: they are FK targets, kit_life's schema owns their
#   DDL, and a table that does not exist cannot be seeded later. Only the ROWS
#   moved here, into the pack that actually owns them as product knowledge.
#
# LEGALITY UNDER THE PACK CONTRACT (kind=pack, capabilities.db_lane=false)
#   This script inserts DATA into tables the KIT already created. It issues no
#   CREATE, no ALTER, no DROP, and never touches PRAGMA user_version -- so it is
#   not a schema change and does not enter the DB lane, which is kit-exclusive
#   (compat-lint C3/C4, pack_install.sh db_lane gate). Refusal to run any
#   statement outside the allowlist below is enforced as code (SQL_GUARD), not
#   promised in prose: the seed file is parsed and every statement must be an
#   INSERT OR IGNORE into one of the 12 declared tables (ax_engine.SEED_TABLES).
#
#   WHAT IS NOT LEGAL, AND IS NOT ATTEMPTED: firing automatically at pack
#   install. The framework's kind=pack install pipeline is file-copy + ledger
#   write only -- it has no post-install execution hook of any kind (measured:
#   pack_install.sh steps for PACK_CLASS=pack are service_facade / skills-bundle
#   / routines-bundle / config-merge / deps-provision / units-engrave /
#   DOGANY_PACKS upsert; manifest 'domain_seed' is NOT a generic hook, it is a
#   hardcoded write of config.consult_state). Until such an affordance exists,
#   this script is invoked explicitly by the deploy owner right after the pack
#   install, exactly like us_reseed.py in this same directory.
#
# IDEMPOTENCY
#   Eleven of the twelve target tables carry a NATURAL primary key -- there is
#   no implicit-rowid table in the set (verified against the kit schema). A PK
#   collision is therefore an exact identity match, and INSERT OR IGNORE means
#   an existing row is left byte-identical, INCLUDING a user's own edits on top
#   of a seeded row. Re-running inserts 0 rows and changes nothing.
#
#   ax_exercise is the twelfth and the exception: its PK is a ULID, so OR IGNORE
#   alone would let a seeded row land BESIDE a JIT-registered row for the same
#   lift. Those statements carry their own natural-key guard
#   (WHERE NOT EXISTS ... exercise_name=...) and the SQL guard below allows that
#   one extra statement shape. Same promise, one more key.
#
# EXISTING INSTALLATIONS
#   Catalog expansions are topped up without deleting or rewriting existing rows.
#
# Usage: health_taxonomy_seed.py [--db PATH] [--apply | --check] [--json]
#                                [--owning-agent SLUG]
#   default is dry-run: the work is done inside a transaction and rolled back.
#   --check runs the same seed on an in-memory snapshot, leaving the source DB
#   read-only. It checks completeness against the current seed, not just whether
#   the seed ever ran. ax_engine.taxonomy_probe stays a presence check (cheap,
#   per call); ax_engine.taxonomy_probe_complete is this same check in-process
#   (~0.2s on a 10MB DB -- once per session, not per set).
#
# Exit: 0 ok, 1 error (nothing written -- the transaction is rolled back),
#       3 the taxonomy is NOT seeded on this DB (--check only). 3 is a distinct
#         code on purpose: "this install is incomplete" is not the same fact as
#         "the command failed", and the two get told apart by the caller.
#
# stdlib + sqlite3 only.

import os
import re
import sys
import json
import argparse
import sqlite3
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
# ax_engine is this directory's shared library and is stdlib-only at import
# time (its kit_life/DB access is all lazy), so a seed run pays nothing for it.
# The taxonomy-state probe lives there rather than in a module of its own --
# see the TAXONOMY SEED STATE section there for why (26 suites copy a named
# subset of this directory and every one of those lists carries ax_engine.py).
import ax_engine as TX                                       # noqa: E402

# Same derivation every other entrypoint in this directory uses
# (set-add / set-table / session-open / rx-calc: ../../database/kit_life.db).
DEFAULT_DB = os.path.join(HERE, "..", "..", "database", "kit_life.db")
DEFAULT_SEED = os.path.join(HERE, "health_taxonomy_seed.sql")

# The only tables this script may write. A statement naming anything else is a
# hard error -- the pack contract boundary is checked, not trusted.
#
# The declaration lives in ax_engine.SEED_TABLES because the SAME list is
# what every reader probes to answer "did this seed ever run" (2026-09-12). It
# is still a HAND-WRITTEN declaration there, never derived from the seed file --
# a guard that read its allowlist out of the file it is guarding would check the
# seed against itself and prove nothing.
# Plus the two tag tables (2026-09-26, kit_life 056 D4 parity): stabilizer /
# laterality tags are DATA the kit read model consumes, seeded row-for-row the
# same as the migration writes them. They are allowed here but deliberately NOT
# in SEED_TABLES: that tuple is also the "did the seed run" probe, and a DB with
# no tagged exercise registered legitimately holds zero tag rows.
TAG_TABLES = ("ax_tag", "ax_exercise_tag")
ALLOWED_TABLES = TX.SEED_TABLES + TAG_TABLES

# Every seed statement must match this. Anything else (CREATE/ALTER/DROP/PRAGMA,
# a bare INSERT that could clobber, an UPDATE) is refused before a connection is
# even opened.
#
# TWO SHAPES, both INSERT-ONLY (2026-09-14). `VALUES(` is the eleven
# natural-key tables. `SELECT ` is ax_exercise, whose PK is a ULID rather than
# its natural key -- there the statement carries its own
# `WHERE NOT EXISTS (SELECT 1 FROM ax_exercise WHERE exercise_name=...)` guard so
# a JIT-registered row is never doubled. Widening the guard by one alternative
# keeps what the guard is FOR: no CREATE/ALTER/DROP/PRAGMA, no UPDATE, no
# clobbering INSERT, and no table outside ALLOWED_TABLES. A SELECT source is
# still a read; it cannot leave the db_lane=false boundary.
SQL_GUARD = re.compile(
    r"^INSERT OR IGNORE INTO (%s) (?:VALUES\(|SELECT )" % "|".join(ALLOWED_TABLES)
)

# The one substitution token in the seed file. See the header block in
# health_taxonomy_seed.sql for why owning_agent cannot be a literal.
OWNING_AGENT_TOKEN = "@@OWNING_AGENT@@"


def _sql_quote(value):
    """A single-quoted SQL literal. The value is already normalised to
    [A-Za-z0-9_-] by ax_engine.normalize_owning_agent, so the doubling below is
    belt-and-braces rather than the only thing standing between this file and an
    injection -- but the seed is the one place a config-derived string reaches
    SQL text, so it is spelled out rather than assumed."""
    return "'%s'" % str(value).replace("'", "''")


def resolve_seed_owning_agent(db, explicit=None):
    """The slug this seed stamps on ax_projection_rule / ax_exercise rows.

    SCHEMA PREFLIGHT, not just config: on a pre-049 kit DB the column still
    carries the legacy three-value CHECK on owning_agent, and a resolved slug
    outside that set does not mislabel the rows -- it makes every one of these
    386 statements raise IntegrityError and the seed insert nothing. So the DB
    is asked what it accepts, and a forced degrade to the legacy slug is
    announced on stderr rather than performed quietly.

    Returns (slug, degraded_bool)."""
    if explicit:
        slug = TX.normalize_owning_agent(explicit)
        if not slug:
            raise ValueError(
                "--owning-agent %r is not a usable instance slug "
                "(expected [A-Za-z0-9_-], 1-64 chars)" % explicit)
    else:
        slug = TX.resolve_owning_agent()
    if slug in TX.LEGACY_OWNING_AGENT_ENUM:
        return slug, False
    if TX.owning_agent_grammar_open(db):
        return slug, False
    print("WARNING: this DB still carries the pre-049 closed enumeration %s, "
          "so the taxonomy is being seeded as %r, NOT as this instance (%r). "
          "Apply kit_life migration 049_owning_agent_identity.sql and re-run "
          "to re-stamp -- until then a second health agent on this crew DB "
          "would collide with these rows."
          % (TX.LEGACY_OWNING_AGENT_CHECK, TX.LEGACY_OWNING_AGENT, slug),
          file=sys.stderr)
    return TX.LEGACY_OWNING_AGENT, True


def parse_seed(path, owning_agent=None):
    """Read the seed file, strip comments/blanks, validate every statement.

    Returns [(table, statement), ...] in file order. Order is load-bearing:
    muscle_label.node and muscle_node.parent are FKs into muscle_node.

    `owning_agent` substitutes OWNING_AGENT_TOKEN. Substitution happens BEFORE
    the guard match on purpose: the statement that is validated is the exact
    statement that will execute, so a guard failure can never be read against a
    line the DB never sees. A token left unsubstituted (owning_agent None, the
    parse-only path) is reported by its own error rather than handed to sqlite.
    """
    stmts = []
    with open(path, encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, 1):
            line = raw.strip()
            if not line or line.startswith("--"):
                continue
            if owning_agent is not None:
                line = line.replace(OWNING_AGENT_TOKEN,
                                    _sql_quote(owning_agent))
            if OWNING_AGENT_TOKEN in line:
                raise ValueError(
                    "%s:%d: %s was not substituted -- this statement would be "
                    "handed to sqlite verbatim: %s"
                    % (path, lineno, OWNING_AGENT_TOKEN, line[:80])
                )
            if not line.endswith(";"):
                raise ValueError(
                    "%s:%d: statement does not terminate on its own line "
                    "(multi-line statements are not supported by this runner): "
                    "%s" % (path, lineno, line[:80])
                )
            m = SQL_GUARD.match(line)
            if not m:
                raise ValueError(
                    "%s:%d: refused -- not an INSERT OR IGNORE into an allowed "
                    "health taxonomy table (db_lane=false pack may insert DATA "
                    "only): %s" % (path, lineno, line[:80])
                )
            stmts.append((m.group(1), line))
    if not stmts:
        raise ValueError("%s: no seed statements found" % path)
    return stmts


def seed(conn, stmts, apply_changes):
    """Apply the seed inside one transaction. Returns a per-table report."""
    tables = []
    for t, _ in stmts:
        if t not in tables:
            tables.append(t)

    report = {
        "applied": bool(apply_changes),
        "tables": {},
        "total_statements": len(stmts),
        "total_inserted": 0,
        "total_skipped": 0,
        "missing_tables": [],
        "fk_violations": [],
    }

    # Missing table = the kit schema is older than this pack expects. Report it
    # as a blocker rather than half-seeding.
    have = {
        r[0]
        for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
    }
    missing = [t for t in tables if t not in have]
    if missing:
        report["missing_tables"] = missing
        report["applied"] = False   # blocked before any statement ran
        return report

    cur = conn.cursor()
    try:
        cur.execute("BEGIN")
        before = {
            t: conn.execute("SELECT COUNT(*) FROM %s" % t).fetchone()[0]
            for t in tables
        }
        for _, stmt in stmts:
            cur.execute(stmt)
        after = {
            t: conn.execute("SELECT COUNT(*) FROM %s" % t).fetchone()[0]
            for t in tables
        }
        planned = {t: 0 for t in tables}
        for t, _ in stmts:
            planned[t] += 1
        for t in tables:
            ins = after[t] - before[t]
            report["tables"][t] = {
                "rows_before": before[t],
                "rows_after": after[t],
                "statements": planned[t],
                "inserted": ins,
                "skipped_existing": planned[t] - ins,
            }
            report["total_inserted"] += ins
            report["total_skipped"] += planned[t] - ins

        # FK integrity, scoped to the tables actually touched -- a whole-DB
        # check would surface pre-existing violations this script did not cause.
        for t in tables:
            for row in conn.execute("PRAGMA foreign_key_check(%s)" % t):
                report["fk_violations"].append({"table": t, "row": list(row)})
        if report["fk_violations"]:
            conn.rollback()
            report["applied"] = False
            return report

        if apply_changes:
            conn.commit()
        else:
            conn.rollback()
    except Exception:
        conn.rollback()
        raise
    return report


def check_report(db, seed_path=DEFAULT_SEED, owning_agent=None):
    """Measure missing rows with the exact dry-run logic on a read-only snapshot.

    Keep the presence-probe JSON fields for existing consumers; missing_rows
    and total_missing describe the current seed, including conditional tag rows.
    A snapshot avoids taking a write lock or creating a journal on the source.
    Never prints, never raises on a DB/seed problem (verdict UNKNOWN + error);
    ax_engine.taxonomy_probe_complete is the in-process reader of this.
    """
    report = TX.taxonomy_probe(db)
    report.update(missing_rows={}, total_missing=0)
    try:
        agent, degraded = resolve_seed_owning_agent(db, owning_agent)
        stmts = parse_seed(seed_path, owning_agent=agent)
        source = sqlite3.connect(Path(db).as_uri() + "?mode=ro", uri=True)
        snapshot = sqlite3.connect(":memory:")
        try:
            source.backup(snapshot)
            # Both reports must describe the same snapshot.
            report = TX.taxonomy_probe(snapshot)
            report.update(db=db, missing_rows={}, total_missing=0,
                          owning_agent=agent, owning_agent_degraded=degraded)
            snapshot.execute("PRAGMA foreign_keys=ON")
            planned = seed(snapshot, stmts, False)
        finally:
            snapshot.close()
            source.close()
        report["missing_rows"] = {
            t: info["inserted"] for t, info in planned["tables"].items()
        }
        report["total_missing"] = planned["total_inserted"]
        report["fk_violations"] = planned["fk_violations"]
        for t in planned["missing_tables"]:
            if t not in report["missing"]:
                report["missing"].append(t)
            report["tables"][t] = "missing"
        if planned["fk_violations"]:
            report.update(verdict=TX.UNKNOWN,
                          error="foreign-key violations in seed dry-run")
        elif report["missing"]:
            report["verdict"] = TX.SCHEMA_MISSING
        elif report["total_missing"] and report["verdict"] == TX.SEEDED:
            report["verdict"] = TX.PARTIAL
    except (OSError, ValueError, sqlite3.Error) as exc:
        report.update(verdict=TX.UNKNOWN, error=str(exc))
    return report


def _check(db, as_json, seed_path=DEFAULT_SEED, owning_agent=None):
    """--check: check_report, printed; exit code per the header."""
    report = check_report(db, seed_path, owning_agent)
    if as_json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("health taxonomy CHECK %s (%s)" % (report["verdict"].upper(), db))
        for t in dict.fromkeys((*report["tables"], *report["missing_rows"])):
            n = report["counts"].get(t)
            missing = report["missing_rows"].get(t)
            print("  %-24s %s; missing=%s" % (
                t, report["tables"].get(t, "seed-only") if n is None
                else "%d rows" % n,
                "unknown" if missing is None else missing))
        print("  TOTAL missing=%d" % report["total_missing"])
        if report["error"]:
            print("ERROR: %s" % report["error"])
        elif report["missing"]:
            print(TX.taxonomy_diagnostic(report))
        elif report["verdict"] != TX.SEEDED:
            print("Seed incomplete; top up with: %s" % TX.taxonomy_seed_command(report))
    if report["verdict"] == TX.SEEDED:
        return 0
    if report["verdict"] == TX.UNKNOWN:
        return 1
    return 3


def main():
    ap = argparse.ArgumentParser(
        description="Seed pack_health taxonomy rows into the kit_life DB "
                    "(idempotent, never clobbers)"
    )
    ap.add_argument("--db", default=DEFAULT_DB, help="path to kit_life.db")
    ap.add_argument("--seed", default=DEFAULT_SEED,
                    help="path to health_taxonomy_seed.sql")
    ap.add_argument("--apply", action="store_true",
                    help="perform the write (default: dry-run, rolled back)")
    ap.add_argument("--check", action="store_true",
                    help="write nothing; report whether this DB is seeded "
                         "(exit 0 seeded / 3 not seeded / 1 error)")
    ap.add_argument("--json", action="store_true", help="emit JSON report")
    ap.add_argument("--owning-agent", default=None,
                    help="slug to stamp on ax_projection_rule / ax_exercise "
                         "rows (default: this instance, from .instance.conf "
                         "DOGANY_AGENT_NAME)")
    args = ap.parse_args()

    db = os.path.abspath(args.db)
    if not os.path.exists(db):
        print("ERROR: db not found: %s" % db, file=sys.stderr)
        return 1

    if args.check:
        if args.apply:
            print("ERROR: --check and --apply are mutually exclusive",
                  file=sys.stderr)
            return 1
        return _check(db, args.json, args.seed, args.owning_agent)

    try:
        agent, degraded = resolve_seed_owning_agent(db, args.owning_agent)
        stmts = parse_seed(args.seed, owning_agent=agent)
    except (OSError, ValueError) as exc:
        print("ERROR: %s" % exc, file=sys.stderr)
        return 1

    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        report = seed(conn, stmts, args.apply)
    finally:
        conn.close()

    report["owning_agent"] = agent
    report["owning_agent_degraded"] = degraded

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("health taxonomy seed %s (%s)" % (
            "APPLIED" if report["applied"] else "DRY-RUN", db))
        print("  owning_agent: %s%s" % (
            agent, "  [DEGRADED -- pre-049 schema]" if degraded else ""))
        if report["missing_tables"]:
            print("BLOCKED: kit schema is missing table(s): %s"
                  % ", ".join(report["missing_tables"]))
            print("  the kit owns this DDL -- install/upgrade kit_life first")
            return 1
        for t, info in report["tables"].items():
            print("  %-24s +%-4d (%d already present)"
                  % (t, info["inserted"], info["skipped_existing"]))
        print("  %-24s +%-4d (%d already present) / %d statements"
              % ("TOTAL", report["total_inserted"], report["total_skipped"],
                 report["total_statements"]))
        if report["fk_violations"]:
            print("BLOCKED: foreign-key violations -- rolled back, nothing "
                  "written:")
            for v in report["fk_violations"]:
                print("  %s: %s" % (v["table"], v["row"]))
            return 1

    if report["missing_tables"] or report["fk_violations"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
