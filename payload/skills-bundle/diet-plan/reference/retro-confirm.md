# step B -- retro confirm (read when a planned row is being resolved)

## pending rows
```bash
$PROJECT_ROOT/database/kit_life.sh meal-planned-list "<YYYY-MM-DD>"
```
TSV: id / 끼니 / 이름 (marker stripped) / kcal / protein. zero pending -> prints
nothing, exit 0. this is the ONLY source of which rows are pending. `task-find` /
`task-done` only close the matching `회고:` task per row.
several rows -> resolve each separately. "먹었어" / "안 먹었어" covers only the row it
was said about; ask the rest, never assume.

## the question
one short plain line: ate exactly what was planned? no framing. banned: "계획과 다르게
드셨네요", "아쉽네요", anything that reads a difference as a lapse. a difference is a
correction to log.

## three outcomes (each resolves the row; no planned row survives retro)

ate exactly as planned:
```bash
$PROJECT_ROOT/database/kit_life.sh meal-planned-confirm <id>
$PROJECT_ROOT/database/kit_life.sh task-done <id_of_retro_task>
```

ate something different (food or amount):
```bash
$PROJECT_ROOT/database/kit_life.sh meal-planned-confirm <id>
$PROJECT_ROOT/database/kit_life.sh meal-upd <id> name="<corrected name>" carb=<v> protein=<v> fat=<v> fiber=<v> sugar=<v> alt_sugar=<v> grams=<v>
$PROJECT_ROOT/database/kit_life.sh task-done <id_of_retro_task>
```
- confirm FIRST (strips marker), then meal-upd.
- `name=` only when the food changed; never re-type ` (예정)`.
- macro fields only for what changed. food changed -> resolve nutrition via lookup.py
  as in step A.

did not eat:
```bash
$PROJECT_ROOT/database/kit_life.sh meal-planned-drop <id>
```
bare call prints census (date / meal / name / kcal / protein / day_rows_before /
day_kcal_before) and refuses, exit 3. re-run echoing the printed kcal:
```bash
$PROJECT_ROOT/database/kit_life.sh meal-planned-drop <id> --confirm-kcal <n>
$PROJECT_ROOT/database/kit_life.sh task-done <id_of_retro_task>
```

## other refusals (exit 3)
- `NOT_PLANNED` -> row has no marker (already confirmed, or never planned). do not
  retry; meal-del is a different verb and not this skill's.
- `REFERENCED ... notion_id=` (drop) -> external mirror holds a pair; mirror first.

## after every verb
re-render + send card (diet-status reference/card-render.md). confirm and drop print
`pending_remaining <n>`; today's sweep is done at 0, all `회고:` tasks closed.
