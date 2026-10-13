# program.yaml generation -- program-init contract (DGN-301 5.1; writer since 2026-09-14)

Read when: writing or repairing program.yaml outside the program-plan build (revision
`--force`, `validate` / `sync` / `check`), program-init printed an `E-*` / `W-*` line,
or asked what the card contains.

writer = `service/health/program-init`, never this skill, never Write / heredoc (D2).
2026-09-13: the old text said "generate program.yaml", no generator existed, the owner
hit `session-open exit=1` on the first "운동 시작". a model asked to write a file
sometimes does not, and nobody notices -> write moved to a deterministic carrier.

lanes (D10): asking, hearing, Korean -> fields = LLM. schema, validation, derivation,
write, `session_type` rows, verdicts = CLI. seam = `answer`.

## calls (same result)

```bash
# build: program-plan walks the stages; its `done` stage calls program-init write.
# lower-level contract (repair / tooling), stage by stage -- last answer IS the write:
service/health/program-init next
service/health/program-init answer --stage rotation --json '{"rotation":[...]}'
service/health/program-init answer --stage 'day:<코드>' --json '{"exercises":[...]}'
# one shot, whole draft (revision confirm):
service/health/program-init write --answers @files/tmp/program-answers.json [--force]
```

`program-init schema` = whole answer contract (fields, ranges, required) as JSON. read
it first; never invent a field not in it.

## refuses (at write time, loudly; any error -> nothing written)

rotation code duplicate / reserved (`보충`) / YAML punctuation, rotation day without a
plan (= unfinished consult), empty day, same lift twice a day, sets / rep_range /
weight_kg out of range, missing `weight_kg` KEY (null != "not asked"). each error one
line `E-*<TAB>path<TAB>why`.

## derives (only unanswered fields; owner answer wins)

`slot` / `priority` (slot*10) / `role` (ax_exercise.movement) / `progression`
(ax_exercise.measure) / `lattice` (equipment class); marked `# DERIVED:` in the file.
never machine / cable base / step (gym-specific; F17 JIT lane `lattice-set`).
never `rir_floor` (G19 home = reference/rir-floor.md): checks coverage, prints
`W-G19-UNSET` per G19-class slot without one.

## content contract (first build via program-plan `done`, revision via `--force`)

- slots = lifts named in compose + confirmed in the sessions message; safety swaps
  (compose `replaces` / `for_site` / `why`) encoded as the slot safety_note; sets from
  RX_RULES + silent volume fit.
- `focus_areas` minus areas the emphasis decision protects; focus lifts named in
  compose (`focus`).
- `weight_kg: null` all slots (calibration pending). exception: workouts.note history
  has a kg for that lift -> seed it as estimate (`last.source='note_extract'`).
- `inc_override: null` (rx-calc picks the step, program-rules 증량 폭) unless owner sets one.
- `weekly_frequency` per DGN-316 2.5.
- idempotency: card exists -> reconcile (update touched slots, carry miss_streak +
  last values), never blind overwrite. `write` REFUSES an existing card without
  `--force`: first build and confirmed revision are different acts.
- `session_type`: same call, one row per `rotation:` code (+ 보충 at out-of-cycle sort
  99), reconcile-first. hand-authored card or replaced DB -> `program-init sync`;
  `program-init check` = verdict (0 done / 3 not yet); health-install-ensure.sh runs it at
  every session birth. `invalid` card -> `program-init validate` names every error.
- no trailing invites on the confirm (2026-09-26): weights come from the ramp-up; a
  first program starts at its first day. volunteered weight -> session lane.

## W5 -- the `done` stage outputs (calendar registration)

same call: `program-init write` (card + session_type rows); `files/program/prep.yaml`
from the sessions' mat-prep + cooldown slots when none exists (existing one = user data,
never touched); `config-set consult_modules` (workout -> done@<date>, others kept); one
`kit_life.sh routine add 운동 W:<days> [time=HH:MM duration=<min>]` per time window of the
운동일시 answer (2nd+ with `--new`). no time said -> all-day routine; the tool never picks
an hour (E13). kit duplicate gate answers EXISTS on a re-run. extra (보충) days are not
scheduled (makeup by weekly quota: rotation-current / makeup gate).

plan state `files/program/.program-plan.json` keeps answers with no kit verb yet
(safety items, place); `files/kit-side-followups.md` in the pack repo names the kit verbs
that retire it.
