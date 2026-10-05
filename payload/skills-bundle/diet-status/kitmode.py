#!/usr/bin/env python3
"""
Which kit shape is this module writing into, and does it match what it copied?

WHY A MODULE DECLARES THE KIT IT MIMICS.  A diet module is useful at three
different depths (owner, 2026-09-10): a dictionary is a calculator and not a
module at all; a module with its OWN record is a diet app but never touches the
rest of a life; a module writing into the KIT is the one that can say "this week
you are 476 over the plan".  The middle depth is the one that lets a module run
"like a plugin" -- the owner's phrase -- and the estate already has a precedent
for it, the relationship module keeping its own sidecar and reading the kit
read-only.

The owner's own proposal is what makes the middle depth cheap: copy the kit's
SHAPE for the few tables actually needed, so a later move into the kit is a
POUR, not a conversion.  `block.ulid TEXT NOT NULL UNIQUE` is what makes the
pour safe -- rows are written with a ULID in the sidecar, and on pour the
integer id is reassigned while the ULID does the de-duplication, with the
attached tables re-keyed by joining on it.

AND THAT IS WHY THE VERSION MUST BE DECLARED.  A copied shape is a copy of ONE
version of that shape.  The kit is at 47; a module that copied 35 and never
said so cannot be poured at all, because nothing knows which shape its rows are
in and by then the rows exist.  The declaration is cheap now and impossible
later -- the same failure mode this estate keeps paying for.

REQUIRE vs DECLARE.  `requires_kit` means "this kit must be present" and fails
closed.  `mimics_kit` means "this is the shape I copied", which is a statement
about the module, not a demand on the host: a missing kit is not an error, it
is just standalone mode.  So the gate table loses two of its three BLOCK rows:

    kit absent            PASS    standalone -- write to the sidecar
    kit present, matches  PASS    linked -- write to the kit directly
    kit present, differs  BLOCK   pouring into a different shape breaks it
    standalone -> kit installed   MIGRATE  <- see MIGRATION POINT below

WHAT THIS DOES, STATED PLAINLY SO THE DECLARATION IS NOT READ AS ENFORCEMENT:
this script REPORTS the verdict; it does not refuse anything.  The install-time
gate lives in the framework's pack_install.sh and the manifest schema, which are
not this lane's to change; the shape this module needs from them is exactly the
`mimics_kit` block in product.yaml beside this file.  Until that lands, a BLOCK
verdict here is a report, not a refusal, and this file says so on every run
rather than letting a reader assume otherwise.

WHO READS THE VERDICT (0.11.0).  In v0.1 the answer was NOBODY, and that was
measured on the live instance on day one of kit_life 2.19.0:

    verdict=mismatch declared_schema=46 installed_schema=47 enforced=False

A warning that only appears when a human happens to run the script by hand is
not a surface.  The verdict now has two readers, neither of them fatal:
  * `card.py` -- a non-`linked` verdict prints a NOTICE line on the diet status
    card.  The card is where this pack's coaching actually reaches the owner,
    so it is where "this card is built on a shape the pack says it does not
    match" has to become visible.  It never stops the card from rendering: a
    pack that refuses to run over a version note is worse than the note.
  * the shipped suite -- claim M2 in `service/health/tests/test-diet-coaching.py`
    re-runs the declaration check against the kit checkout on every run, so the
    next kit bump turns a suite RED with the re-verification instruction rather
    than printing a verdict into a void.
`enforced` stays False and keeps saying so.  Being READ and being ENFORCED are
different claims and this file will not blur them.

Usage:  kitmode.py [--json]
Exit 0 on linked/standalone, 1 on mismatch (so a future caller CAN gate on it
without this file having to change).
"""
import argparse
import json
import os
import re
import sqlite3
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
PRODUCT_YAML = os.path.join(_HERE, "product.yaml")
KIT_DB = os.path.join(_PROJECT_ROOT, "database", "kit_life.db")

# =========================================================================
# ***  MIGRATION POINT  ***  standalone -> linked pour.
#
# NOT IMPLEMENTED IN v0.1, ON PURPOSE: there is no sidecar to pour from yet
# (v0.1 ships linked-only), and writing the pour before the thing it pours
# would be building on an unmeasured shape -- the exact habit this module's
# design session spent its day undoing.  The MARKER is what v0.1 owes: a
# named, findable place, because a seam nobody wrote down is a seam nobody
# can add later.
#
# When it is written, it does this and nothing else:
#   1. refuse unless verdict == 'migratable' (declared schema_version equals
#      the installed kit's user_version).  A pour into a different shape is
#      the one BLOCK row of the gate table above.
#   2. for each sidecar `block`: INSERT into the kit's block, letting the kit
#      assign a fresh integer id, with the sidecar's ULID carried over
#      verbatim.  ON CONFLICT(ulid) DO NOTHING -- the ULID is what makes a
#      re-run idempotent and a partial pour resumable.  Name the columns;
#      never `INSERT ... SELECT *` -- the kit's block has columns the sidecar
#      does not (052 `retro_line`, measured 2026-09-26), and they take the
#      kit's own NULL.
#   3. re-key every attached row (block_attr / measure / block_delta) by
#      joining sidecar.block_id -> ULID -> kit block.id.  Never by position,
#      never by date+name.
#   4. leave the sidecar in place, read-only, until the pour is verified.
#      029 did exactly this with the per-instance food_cache.json and it is
#      why that cutover was reversible.
#   5. flip mode: linked in product.yaml LAST, so a crash mid-pour re-runs
#      instead of stranding the module in a mode its data does not match.
#
# The tables and vocabulary the pour has to cover are DECLARED, not inferred:
# see `mimics_kit.tables` / `mimics_kit.vocab` in product.yaml. `excluded`
# lists what was measured as genuinely unused (place / place_link / entity:
# 0 of 6,331 meal measures reference an entity) -- if that stops being true,
# the declaration is the thing that changes, not this comment.
# =========================================================================
_MIGRATION_POINT = "kitmode.py: standalone -> linked pour (v0.1: marker only)"


def _read_mimics(path=None):
    """Parse the `mimics_kit:` block out of product.yaml.

    Deliberately a small hand parser and not a YAML dependency: every other
    consumer of these unit manifests (publish.sh's flat parser, lane-lint.py)
    is one too, and adding a third grammar that reads the file differently is
    how a manifest starts meaning two things at once."""
    p = path or PRODUCT_YAML
    try:
        with open(p, "r", encoding="utf-8") as fh:
            lines = fh.read().splitlines()
    except (IOError, OSError):
        return None
    out, inside = {}, False
    cur_list = None
    for ln in lines:
        if re.match(r"^mimics_kit:\s*(#.*)?$", ln):
            inside = True
            continue
        if not inside:
            continue
        if re.match(r"^[A-Za-z_]", ln):        # next top-level key ends it
            break
        if not ln.strip() or ln.lstrip().startswith("#"):
            continue
        body = ln.strip()
        if body.startswith("-"):
            if cur_list is not None:
                out[cur_list].append(body[1:].strip().strip("\"'"))
            continue
        if ":" not in body:
            continue
        k, v = body.split(":", 1)
        k, v = k.strip(), v.strip().strip("\"'")
        if v:
            out[k] = v
            cur_list = None
        else:
            out[k] = []
            cur_list = k
    return out or None


def kit_user_version(db_path=None):
    """The installed kit's schema version, or None when no kit is installed.

    Read-only and never creates the file -- a missing kit is standalone mode,
    not an error, so this must not be the thing that mints an empty DB.

    TWO READS, and the second one is not belt-and-braces.  The live kit runs in
    WAL mode, and opening a WAL database even with mode=ro needs write access to
    its DIRECTORY (sqlite has to be able to create/attach -shm).  Measured: a
    caller without that access gets `unable to open database file` from the
    PRAGMA, not from connect() -- so a try around connect() alone still raises.
    `user_version` is a fixed 4-byte big-endian field at offset 60 of the file
    header, so the fallback reads it straight out of the file with no
    connection, no lock and no WAL involvement at all.

    Stated cost: the header can lag an un-checkpointed WAL.  It is the FALLBACK,
    only reached when the real read already failed, and reporting a slightly
    stale version beats crashing a mode check -- which is the one thing this
    function must never do.
    """
    p = db_path or KIT_DB
    if not os.path.isfile(p):
        return None
    try:
        conn = sqlite3.connect("file:%s?mode=ro" % p, uri=True)
        try:
            return int(conn.execute("PRAGMA user_version;").fetchone()[0])
        finally:
            conn.close()
    except (sqlite3.Error, TypeError, ValueError, IndexError):
        pass
    try:
        with open(p, "rb") as fh:
            head = fh.read(64)
        if len(head) < 64 or head[:16] != b"SQLite format 3\x00":
            return None
        return int.from_bytes(head[60:64], "big")
    except (IOError, OSError):
        return None


def resolve(product_path=None, db_path=None):
    mim = _read_mimics(product_path)
    if not mim:
        return {"verdict": "undeclared", "mode": None, "enforced": False,
                "why": "no mimics_kit block in product.yaml -- this module "
                       "does not declare a kit shape, so nothing can be "
                       "poured later"}
    declared = mim.get("schema_version")
    try:
        declared = int(declared)
    except (TypeError, ValueError):
        return {"verdict": "undeclared", "mode": mim.get("mode"),
                "enforced": False,
                "why": "mimics_kit.schema_version is missing or not an "
                       "integer -- an undeclared version cannot be compared"}
    installed = kit_user_version(db_path)
    base = {"kit": mim.get("kit"), "declared_schema": declared,
            "installed_schema": installed, "declared_mode": mim.get("mode"),
            "tables": mim.get("tables") or [], "vocab": mim.get("vocab") or [],
            "excluded": mim.get("excluded") or [],
            "migration_point": _MIGRATION_POINT, "enforced": False}
    if installed is None:
        base.update(verdict="standalone", mode="standalone",
                    why="no kit installed -- write to the sidecar; the "
                        "declaration is not a requirement")
    elif installed == declared:
        base.update(verdict="linked", mode="linked",
                    why="installed kit matches the declared shape")
    else:
        base.update(verdict="mismatch", mode=mim.get("mode"),
                    why="declared shape %d != installed kit %d -- rows "
                        "written now would not pour cleanly"
                        % (declared, installed))
    if base["verdict"] == "linked" and mim.get("mode") == "standalone":
        base["verdict"] = "migratable"
        base["why"] = ("declared standalone but a matching kit IS installed "
                       "-- this is the pour case; see the MIGRATION POINT in "
                       "kitmode.py (not implemented in v0.1)")
    return base


def main(argv):
    ap = argparse.ArgumentParser(prog="kitmode.py", add_help=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    r = resolve()
    if args.json:
        print(json.dumps(r, ensure_ascii=False))
    else:
        for k in ("verdict", "mode", "kit", "declared_schema",
                  "installed_schema", "why", "enforced", "migration_point"):
            if k in r:
                print("%s=%s" % (k, r[k]))
        # Claim discipline: the verdict is a report. Say it every run rather
        # than letting a declaration read as a gate that does not exist.
        print("note=v0.1 REPORTS this verdict; nothing gates on it. The "
              "install-time gate is pack_install.sh + the manifest schema, "
              "which this lane does not own.")
    return 1 if r["verdict"] == "mismatch" else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
