---
name: diet-plan
display_name: 식단 예정 기록
description: >
  Handles logging a meal/snack 사용자 has NOT eaten yet as PLANNED (예정), so it
  shows on today's calorie card immediately, plus the evening retro that
  confirms or corrects it. Log-planned triggers: "간식 예정으로 넣어줘", "저녁
  예정으로 등록해줘", "저녁 예정으로 넣어줘", "이따 <음식> 먹을 예정이야",
  "이따 먹을 거야", "<끼니> 예정으로 넣어줘",
  "미리 기록해줘 아직 안 먹었지만", "카드에도 예정으로 보이게 해줘", "log this
  as planned", "add as upcoming meal", "show it as planned on the card".
  Retro/confirm triggers: 사용자 answering a retro-check question about a planned
  item -- "어 먹었어", "아니 다르게 먹었어", "안 먹었어", or any end-of-day
  review moment with an open 회고-tagged task. Do NOT use for a normal
  already-eaten log with no planned framing -- that stays meal-capture's job
  (the kit's capture lane). Do NOT use for a status/remaining-calorie question
  either -- that is diet-status, in this pack.
  Output: writes a real row into the meals table now (tagged "(예정)" at the end
  of the name field; card.py detects that tag and draws the row dimmed),
  auto-fires the existing card-followup hook so the card renders + sends same
  turn, and opens a task-add retro-check marker for tonight. Retro step
  resolves that row via meal-planned-confirm or meal-planned-drop, marks the
  회고 task done, and manually re-renders + sends the card (those verbs do
  not auto-fire the hook).
---

# diet-plan

log not-yet-eaten food as a REAL meals row tagged ` (예정)`, card shows it now,
retro confirms / corrects / drops it tonight. prose only: every executable is someone
else's. no new script, table, column, status concept.

## depends on (check before trusting a step)
- `kit_life.sh` meal-add / meal-upd / meal-planned-list / meal-planned-confirm /
  meal-planned-drop / task-add / task-find / task-done -- KIT (`requires_kit`).
- meal-capture `lookup.py` -- KIT skill folder. probe
  `.claude/skills/meal-capture/lookup.py` then `.claude/skills-bundle/meal-capture/lookup.py`.
  neither -> kit capture skill not installed. say so, stop. never reimplement lookup.
- diet-status `card.py` -- THIS pack. neither activation nor bundle path -> this pack is
  half-installed. say which is missing; never blame the kit for our own sibling.
- `card-followup` PostToolUse hook -- FRAMEWORK, fires only if the instance registered it.
- `retro-emit.sh` -- INSTANCE-provided, shipped by nobody here (see tier).

## hard rules
- never touch DB schema, never create a table, never bump `EXPECTED_USER_VERSION`
  (kit_life = sole migration author; zero-migration invariant).
- plain "just ate X" -> meal-capture (kit). status / remaining kcal -> diet-status.
- planned-ness = exact TRAILING ` (예정)` suffix on `name` + one open `회고:` task.
  match anchored at end of name only, never as substring.
- coaching voice (no gatekeeping, no lecture, banned vocabulary, trade-off order) =
  diet-status "coaching voice". one trade-off line after the write, if anything.

## tier
- step A = BEST-EFFORT (description match; a miss costs a repeat or a normal log).
- step B = deterministic only where the instance runs `retro-emit.sh` (injects
  `meal-planned-list` rows into the evening retro; zero rows -> silent). there, only
  route the answer to a verb; do not re-surface the ask.
- no emitter (fresh instance) -> step B is BEST-EFFORT and yours: on any daily retro /
  evening review, run `meal-planned-list` yourself and surface open `회고:` tasks.
- either way: user answers a retro-check directly -> step B.

## step A -- log now, tag planned
user stating a plan ("이따 목살 구워먹을 거야") = decision notice, not permission ask. log it.
1. resolve nutrition via meal-capture `lookup.py`, same doors as meal-capture. lookup
   the EXACT string passed to meal-add, ` (예정)` suffix included (lookup-receipt rule,
   else write refused). refused / clearly wrong -> one plain line, no tool / door /
   cache names.
2. write:
   ```bash
   $PROJECT_ROOT/database/kit_life.sh meal-add \
     "<YYYY-MM-DD>" "<아침|점심|저녁|간식|운동>" "<식품명> (<그램수>g) (예정)" \
     <carb> <protein> <fat> <fiber> <sugar> <alt_sugar> <grams> [alcohol]
   ```
   2nd+ item same date + slot -> append `--new` (meal-capture convention).
3. name MUST end with ` (예정)`. card.py keys the dimmed render on it.
4. card-followup hook fires after meal-add -> render + send card this turn.
5. open retro marker:
   ```bash
   $PROJECT_ROOT/database/kit_life.sh task-add \
     "회고: <끼니>(<식품명>) 예정대로 드셨는지 확인" "<YYYY-MM-DD>"
   ```

## step B -- retro confirm
read reference/retro-confirm.md when step B fires (the three outcomes + verb
sequences). short form:
1. pending rows = `meal-planned-list <date>` ONLY (task-find is a reminder, not SoT).
2. one plain question per row. one answer covers only the row it was about.
3. ate as planned -> confirm. ate different -> confirm then meal-upd. did not eat ->
   drop (census, then `--confirm-kcal`). close the matching `회고:` task each time.
4. re-render + send card after EVERY confirm / upd / drop (verbs do not fire the hook).
   done when `pending_remaining 0`.
card render snippet = diet-status reference/card-render.md.
