# payload/service/health -- the workout engine

This directory IS the engine. As of pack 0.2.0 it carries the product copy of
every executable, library, test and reference asset the workout skills drive.

## What is here

- **Onboarding and activity**: `program-plan` builds the program and asks for
  the cardio preference, then offers the final HealthKit consent choice;
  `hk-ingest` imports only approved data; `cardio-record` writes completed
  cardio active kcal from the watch or a bodyweight MET estimate.
- **16 CLIs** (executable, no `.py` extension): `exercise-drop` `exercise-enter`
  `exercise-variant` `lattice-set` `machine-pick` `prep-migrate`
  `program-rebalance` `rx-calc` `session-abort` `session-closeout`
  `session-cursor` `session-open` `set-add` `set-arm` `set-table` `set-undo`.
- **Libraries**: `undo_lib.py` (the delete/correct verbs), `ui_labels.py` (the
  single resolver home for owner-facing labels), `machine_capture.py` (which
  machine a set is done on -- kit 062, through the kit's own verbs),
  `live_load.py` + `live_load.json` (today's load for a lift with no measured
  basis: entry estimate, first-set calibration, next weight, add-on blocks),
  `entry_setup.py` + `entry_setup.json` (the implement question and the
  attachment / grip cue at entry).
- **Render helpers**: `e1rm-card.py` `muscle-preset.py` `rx-card.py`.
- **Projection engine**: `ax_engine.py` `ax-jit` `ax-project` `us-render`
  `us_render.py` `us_reseed.py`.
- **Session harness**: `session_harness/` (blocks / events / prescription /
  set_kind / hooks).
- **Prose references** (shipped docs, not data): `README.txt` (program.yaml
  schema) `gifs/reference-angles.md`.
- **NOT shipped -- user data**: `program.yaml` `prep.yaml` `program-history.json`
  `gym-layout.md` `stretch-matrix.md`. A gym layout is per-person; shipping one
  would let `program-rebalance --order` optimise a route through a gym the user
  has never been in. `gym-layout.md` is read off `DATA_DIR`, not off the script
  dir, so it stays put when this engine is installed to `service/health/`.
  Starter templates ship at `service/health/sot/gym-layout.TEMPLATE.md`,
  `service/health/sot/prep.TEMPLATE.yaml` and
  `service/health/sot/stretch-matrix.TEMPLATE.md`. THE TEMPLATE SHIPS, THE DATA
  DOES NOT -- two different paths, and the distinction is the whole point.
  `cp -f` onto `service/health/sot/` overwrites only the pack's own previous
  template; nothing under `files/program/` is written by any install lane.
  Until 2026-09-12 these three sat at the REPO ROOT under `sot/`, outside
  `payload_root`, which no lane reads -- so a freshly minted instance received
  none of them while four shipped skill documents treated `prep.yaml` /
  `gym-layout.md` / `stretch-matrix.md` as canonical (audit 2026-09-12 2.4).
  Seeding stays MANUAL and per-file: `gym-layout.md` is safe to copy empty (an
  unmapped layout turns the route axis off rather than guessing), `prep.yaml`
  is NOT -- its example day would fire example drills as a real prescription,
  so it must be replaced with the user's real drills before it is used.

  `stretch-matrix.md` joined that list on 2026-09-11 and it is the same
  argument, one step later. The file reads as product prose -- drill setup,
  execution, common mistakes -- but its 부상 프로파일 연계 section carries the
  user's MEASURED injury profile: laterality, real session ids, the dates the
  drill rulings rest on. The pack shipped an EXAMPLE profile under that exact
  filename, and `payload/service/` is copied with `cp -f` on every apply, so an
  apply would replace the evidence a ruling cites with an example. The code
  agrees already: `rx-calc.cue_source_path` resolves it BESIDE `prep.yaml`
  (i.e. off `DATA_DIR`), never off `SCRIPT_DIR`, exactly like `gym-layout.md`.
  Shipping a second copy into `service/health/` only created a SHADOW the model
  could be pointed at while the code quoted the real one.
  `prep.TEMPLATE.yaml` is the prep/cooldown SCHEMA (blocks / drill catalog /
  day items, with the zone and requires axes worked through); the same
  `cp -f`-over-the-owner's-injuries argument that keeps `gym-layout.md` out of
  payload keeps `prep.yaml` out of it.
- **Data migrations** (`prep-migrate`, `health_taxonomy_seed.py`,
  `us_reseed.py`): how this pack changes data it does not own. Dry run by
  default, `--apply` to write. A `prep.yaml` restructuring ships as a
  migration, never as a packaged file -- `prep-migrate --list` names them.
- **Assets**: `gifs/` `refs/`.
- **Tests**: `tests/`, including `_state_isolation.py` -- the live-contamination
  tripwire every suite must call before touching a state dir. **Run them through
  `tests/run-suite.sh`.** Running the suite from inside `payload/` used to make
  the pack UNINSTALLABLE: python writes `__pycache__/` beside every module it
  imports and pytest writes `.pytest_cache/` at its rootdir, both land under
  `payload/`, compat-lint C4b refuses every one of them, and `pack_install.sh`
  refuses a pack that fails compat-lint. Measured twice -- 16 findings here, and
  75 for real on `pack_install --pack kit_life` against the live dogany-lifekit
  checkout. The close is three-layer and documented in `run-suite.sh`'s header:
  a one-line bytecode-off preamble in every suite, `conftest.py` + `pytest.ini`
  for the pytest-collected half, and the runner's own residue gate.
  `run-suite.sh --check-only` is the gate on its own -- run it before any
  `pack_install`.

## Code surface vs state surface -- they are NOT the same directory

This is the single most important thing to know about this tree.

| surface | lives at | contents |
|---|---|---|
| **code** (this dir) | `service/health/` | CLIs, libs, tests, shipped prose |
| **state / data** | `files/program/` | `.active-session` `.idrill-arm/` `.arm-gen/` and every other runtime marker; `program.yaml` `prep.yaml` `program-history.json` (owner data) |

Every CLI resolves `STATE_DIR` / `DATA_DIR` off `PROJECT_ROOT/files/program`,
**never** off its own `SCRIPT_DIR`. Two reasons, both load-bearing:

1. `bridge/bot.py` reads `.idrill-arm/` from that exact path
   (`bridge/IDRILL-ARM-CONTRACT.md` declares it the one pack<->bridge surface).
   Following `SCRIPT_DIR` would silently kill every inline button.
2. `program.yaml` / `prep.yaml` / `program-history.json` are the OWNER'S data --
   their slots, their loads, their rulings. They are deliberately **not shipped** in
   this pack, so an install can never `cp -f` a packaged copy over their real
   program.

So a `files/program` string in this tree is not automatically stale. If it names
a marker or one of the three owner-data files, it is correct and must stay.

## DB boundary

All code here goes through the kit_life facade (`kit_life.sh` / `kit_life.py` CLI)
for DB access. No direct SQL against the shared kit_life DB.

`owning_agent` is the column that tells two crew members apart on that shared
DB. This layer used to write a hard-coded legacy slug --
at four sites in `ax_engine.py` and nine rows of the taxonomy seed. It now goes
through `ax_engine.owning_agent_for(db)`, which answers two questions at once:
who this instance is (`.instance.conf` `DOGANY_AGENT_NAME`, overridable with
`LIFEKIT_OWNING_AGENT`) and what this DB will accept. A pre-049 kit schema still
constrains the column to the legacy three-value enum and would REFUSE a real slug, so
on that lineage the legacy value is used **and announced** -- one
`OWNING-AGENT-LEGACY` line per process, never a quiet mislabel. A read that
find-firsts before writing resolves through the same call, so it looks under the
identity its own insert would stamp.

## Taxonomy seed -- the one install-time step this pack needs

`health_taxonomy_seed.sql` + `health_taxonomy_seed.py` carry 386 rows of
muscle / exercise classification across 12 tables. 370 of them (11 tables) are
the rows the kit_life `schema.sql` used to INSERT at every fresh mint. The kit was shipping a trainer's product
knowledge to instances that will never train; the rows now live with the pack
that owns them.

The **tables** stay in the kit. They are FK targets, the kit owns their DDL, and
a table that does not exist cannot be seeded later. A kit_life-only mint is born
with them EMPTY, not missing.

**IT HAS A CALLER NOW (2026-09-14).** `routines/bundle/health-install-ensure.sh`
is this pack's install-completion lane: it probes with `--check`, runs `--apply`
only when needed, RE-CHECKS after the write so its verdict is measured rather
than inferred from an exit code, and never gates its caller.
`routines/bundle/session-ensure.sh` drives it BEFORE `session-open` -- so the
owner's first 「운동 시작」 seeds the taxonomy and then opens the session, in that
order. Ordering matters: `session-open` READS the taxonomy to decide whether to
print its install-incomplete banner.

To run it by hand, either of these:

```
routines/bundle/health-install-ensure.sh
python3 service/health/health_taxonomy_seed.py --db database/kit_life.db --apply
```

**THIS PARAGRAPH IS NOT THE GUARANTEE, AND UNTIL 2026-09-12 IT WAS THE ONLY ONE.**
A real fresh install was measured on 2026-09-12: the seed had not run, all eleven
tables held 0 rows, `ax-project rules` printed nothing and exited 0, and
`ax-project serve` returned the RAW rx-calc weight with an empty warmup array and
exit 0. No shipped SKILL mentioned the step, so the session agent had no way to
notice. A README is not a caller. What actually holds it now:

- `ax_engine.evaluate_rules` -- the one funnel every projection path goes
  through -- REFUSES an unseeded DB, so `ax-project project|serve|rules` exit **3**
  with the command above on stderr instead of answering.
- `session-open` probes the whole install at session BIRTH (the one code path a
  session cannot skip) and prints `taxonomy=` / `install=` keys plus an
  `INSTALL-GAP` block naming every unmet step.
- `workout-program/SKILL.md` 「설치 완결」 and `workout-session/SKILL.md`
  「전제조건」 carry the precondition and the exit-3 handling.
- `health_taxonomy_seed.py --check` checks the current seed against a read-only
  in-memory snapshot: exit 0 complete, 3 incomplete, 1 error. It uses the same
  INSERT OR IGNORE logic as dry-run, including conditional tag rows, and reports
  per-table missing counts. JSON retains the presence-probe fields and adds
  `missing_rows` and `total_missing`; `tables` still describes table presence.
  Existing identities and user edits count as present. `--seed` and
  `--owning-agent` are honored by check as well as apply.
  In-process `ax_engine.taxonomy_probe` remains the cheaper table-presence
  backstop; it does not detect catalog expansions in nonempty tables.
- `routines/bundle/health-install-ensure.sh`, above, is the CALLER. Two guards,
  independent: if the lane is skipped or the DB is replaced underneath it,
  `session-open` still names the gap at the moment it matters.
- `service/health/tests/run-suite.sh` is the suite entrypoint (see TESTS below).
  `tests/test-ax-exercise-seed.py` is the grill for all of the above.

Dry-run (no `--apply`) does the whole thing in a transaction and rolls back, so
the printed counts are real, not estimated.

- **Idempotent.** Eleven of the twelve tables have a natural primary key, so
  every statement is `INSERT OR IGNORE` and a re-run inserts 0 rows.
  `ax_exercise` is the exception -- its PK is a ULID, so `OR IGNORE` alone would
  let a seeded row sit beside a JIT-registered one for the same lift; those
  statements carry their own `WHERE NOT EXISTS ... exercise_name=` guard. Same
  promise, one more key. An existing row -- including one
  the user edited on top of the seed -- is left exactly as it is. Verified: a
  second and third `--apply` leave the DB dump byte-identical.
- **Existing installations need nothing.** They already hold these rows. There is
  no migration, no `EXPECTED_USER_VERSION` move, and no row is ever deleted or
  rewritten. Not running it on an already-populated instance is the correct
  no-op; running it there is a measured no-op too.
- **Parity.** kit mint (new `schema.sql`) + this seeder produces a DB whose
  `.dump` is byte-identical -- same SHA256 -- to today's fresh mint.

**Why it fires from a session gate and not from the installer, and the framework
gap behind that.** The framework's `kind=pack` install pipeline is file-copy +
ledger-write only: it has no post-install execution hook of any kind (the
manifest's `domain_seed` field is not a generic hook -- it is a hardcoded write
of `config.consult_state`), and the plist lane that could have carried one is
BLOCKED for `kind=pack` by DGN-1402. So the seeder cannot fire at install. The
earliest code this pack owns on a fresh instance is inside its own installed
tree, which is why the lane hangs off `session-ensure.sh`. A sanctioned pack
post-install hook is still the right home and is still a framework change
(the framework's lane), not a content one -- escalated 2026-09-14.

RE-VERIFIED 2026-09-12 against `scripts/pack/pack_install.sh` rather than
inherited: for `PACK_CLASS=pack` the steps are service_facade / skills-bundle /
routines-bundle / config-merge / i18n-json-merge / deps-provision /
units-engrave / DOGANY_PACKS upsert. The one step that DOES execute pack-shipped
code -- step 5, hook wiring -- fires only on `payload/routines/ledger-inject.py`,
which this pack cannot ship (compat-lint C4 refuses `routines/<non-bundle>`), and
it wires a UserPromptSubmit hook rather than running anything at install time.
The legacy `triggers` / `db_migrations` categories belong to the contract class
and `kind=pack` never dispatches to them. **There is no lane. This was checked,
not assumed.**

**The other post-install steps, and why they are announced together.** The
taxonomy seed is not the only one. `files/program/{program.yaml, prep.yaml,
stretch-matrix.md, gym-layout.md}` and the `session_type` rotation rows are all
in the same shape -- the pack ships the template or the schema, no lane places
the file, and the reader degrades instead of saying so. `prep.yaml` was the worst
of them: `rx-calc.load_prep` treats the file as "optional enrichment", so an
absent one produces a session card with NO 준비운동 and no warning at all.
`session-open.install_gaps()` probes the whole set at once. Two of the three SoT
templates are deliberately never auto-copied: `prep.TEMPLATE.yaml`'s example day
would be prescribed as real drills, and `stretch-matrix.TEMPLATE.md` carries an
EXAMPLE injury profile where the owner's measured one belongs.

**Direct-SQL exception to the DB boundary above.** This script opens `sqlite3`
directly rather than going through the kit_life facade, because the facade has no
generic statement-exec verb and adding one would be far worse than this
exception. The blast radius is fenced as code, not prose: `SQL_GUARD` parses the
seed file and refuses any statement that is not `INSERT OR IGNORE` into one of
the 12 declared tables (`ax_engine.SEED_TABLES`), in one of two INSERT-only
shapes -- `VALUES(` for the eleven natural-key tables, `SELECT ... WHERE NOT
EXISTS` for `ax_exercise`'s natural-key guard. CREATE / ALTER / PRAGMA / plain INSERT / INSERT OR
REPLACE / UPDATE / DELETE, and inserts into kit tables or user-data tables, are
all rejected before a connection is opened -- which is what keeps the pack inside
`capabilities.db_lane=false`: it inserts DATA into existing tables and never
touches schema. (`us_reseed.py` beside it takes the same direct-SQL route.)
