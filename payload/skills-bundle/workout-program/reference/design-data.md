# design data -- files/program/, install completion, ownership

Read when: session-open printed `install=incomplete:N` / an `INSTALL-GAP` block, a
`files/program/` file is missing, or the edit touches prep / gym-layout /
program-history. Audit: docs/skill-compaction/workout-program.md.

## 설치 완결 -- fresh mint is not finished (2026-09-12)

Installer copies files + writes the ledger only (`kind=pack` has no post-install
hook). The five items below are filled by nobody else, and missing them raises no
error. session-open checks all at session birth: prints `install=complete` or
`install=incomplete:N` + one `INSTALL-GAP` block per item (what / silent damage /
how to fill). Seen it -> do NOT cover with an invented prescription; tell user in
one sentence setup has one step left, fill the items with them.

| missing | silent damage | who fills |
|---|---|---|
| pack taxonomy seed (11 tables) | weights leave the lattice, empty-bar ramp vanishes; `ax-project` now refuses exit 3 | `python3 service/health/health_taxonomy_seed.py --db database/kit_life.db --apply` (idempotent). `--check` alone: exit 0 done / 3 not |
| `files/program/program.yaml` | no session opens (session-open exit 1) | program-plan (next move + sentence) + program-init (write). model carries sentences + answers; CLI writes. contract: reference/program-init.md |
| `files/program/prep.yaml` | prep + cooldown vanish whole (rx-calc prep block is optional enrichment) | first build: program-plan `done` writes it from the sessions' mat-prep / cooldown slots when none exists. later edits: this skill, schema = `service/health/sot/prep.TEMPLATE.yaml` (schema ONLY -- copying it ships the example drills as a real prescription). verify `rx-calc --validate-prep` |
| `files/program/stretch-matrix.md` | drill cues have no source; a drill declaring a cue closes `--validate-prep` with PREP-CUE-SOURCE-MISSING | this skill, from `sot/stretch-matrix.TEMPLATE.md`. injury-profile part = user's measurements, ask |
| `files/program/gym-layout.md` | route axis off (`program-rebalance --order` cannot measure zone hops; prints WARN) | this skill, placement consult. `cp service/health/sot/gym-layout.TEMPLATE.md files/program/gym-layout.md` is safe (empty = axis OFF, no guessing) |
| `session_type` rotation rows | birth tag fails (`tag=failed`), session labelled by muscle not rotation code | program-init, SAME call that writes program.yaml, derived from its `rotation:`. card present + rows empty -> `program-init sync` |

## missing file = not built yet, never "error"

No install lane writes `files/program/` -- boundary, not defect (never `cp -f` someone
else's prescription over the user's program). Templates ship in
`service/health/sot/` (pack-owned, read-only); data never ships. Do not mix the two.

| file | off when absent | do |
|---|---|---|
| program.yaml | whole prescription | build via program-plan (reference/build-flow.md). no template, ever |
| prep.yaml | prep / cooldown (morning card + live) | see table above. never copy the template as data |
| gym-layout.md | route axis only | copy empty template, ask the user for zones |
| stretch-matrix.md | prose rationale only (code never reads it) | start from template; injury profile only from user ledger |
| program-history.json | rationale sidecar | created on first change |

## 프렙 ownership (C4 2026-07-31; SoT 2026-08-21)

- `files/program/prep.yaml` = THE prep SoT: which drill on which day / slot / phase,
  `display` text (verbatim contract), hold seconds. morning card (rx-calc -> rx-card.py)
  and live session (exercise-enter) both read only this file.
- `files/program/stretch-matrix.md` = prose "why" (setup, execution, common faults,
  evidence grade, time budget, placement rationale). no data status since 2026-08-21;
  code does not read it. disagrees with prep.yaml -> prep.yaml wins.
- retired sources: program.yaml `prep_drills`, `warmup.yaml`. any doc reading them as
  prep source = stale.
- structural / content change (add / drop / retarget drill, session-type prep block,
  K2 / injury model, U3 % basis) = workout-program change. value -> prep.yaml; why ->
  the stretch-matrix.md section.
- workout-session consumes both for delivery only (one drill at a time, buttons,
  timers, cues); does not own prep design.
- both files live in `files/program/` (user data: stretch-matrix carries measured
  injury info). code agrees: `rx-calc.cue_source_path` looks beside prep.yaml. ownership
  statement, not a move instruction.

## files/program/gym-layout.md -- zones + route (user-filled)

Holds zones A-G (owner-dictated), zone adjacency, zone hop matrix, drill / working slot
-> zone map. owner: workout-program. absent -> route axis OFF: every lift reported
UNMAPPED, left out of route cost, order proposals run on fatigue axis only. normal,
no guessing. ordering rules that use it: reference/placement.md.

## files/program/program-history.json -- rationale sidecar (DGN-773)

on-demand sidecar ("why is my program this shape"); split out of program.yaml so
set-arm / set-table do not parse prose per set. rx-calc / exercise-enter hydrate on
demand. holds:
- `safety_notes` -- per-slot safety / design prose, key `<day>.<slot>.<name>`: why this
  lift, why this weight / depth cap, why a primer, dated corrections.
- `changelog` -- program change history, each `date | what | how | why`.

READ FIRST (mandatory) on: "왜 이 종목이 여기 있어", "왜 이 무게야", "이거 언제 바뀌었어",
"왜 바꿨어", and right before dropping / swapping / moving a slot. never rebuild the
reason from memory or prior chat.

EDIT RULE: safety_note prose + changelog lines go ONLY here (moved 2026-08-19); never
back inline into program.yaml. structure change -> same turn update the matching
`safety_notes` key + a `changelog` entry.
