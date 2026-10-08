# set kinds -- prep / warmup / working / hold are one pipeline (A3, 2026-08-25)
read when a prep drill, warmup rung or hold is on screen, or a table cell looks wrong.

every unit of work in a session = ONE `workout_sets` row. prep / ramp / working / hold are
four values of one column; everything that differs between them is READ FROM THE TABLE,
not branched.

| set_kind | on table | keyboard | volume | cue shape |
|---|---|---|---|---|
| `prep` | yes | **single done tap** (`completion_tap`) | **no** | drill name + target |
| `ramp` | yes | reps drilldown | **no** | weight + target |
| `working` | yes | reps drilldown | yes | weight + target + RIR |
| `hold` | yes | timer (done) | yes | duration |

code: `service/health/set-table` `SET_KIND_DERIVATION` / `derive_set_kind`.
`prep` keyboard = `completion_tap` by owner ruling 2026-08-27 (the table was changed;
the old footnote that overrode it was removed: when footnote and table disagree, the
table decides). canonical `session_harness/set_kind.py` still differs in that one cell on
purpose; `tests/test-a3-set-kind.py` allows exactly that divergence.

bands (code: set-table `PREP_SEQ_BASE` / `set_kind_for_seq` / `seq_label`):
| band | `set_seq` | label | kind |
|---|---|---|---|
| working | `>= 1` | `1` `2` `3` | working |
| warmup / setting | `-99 .. 0` | `bw` `r1` `r2` | ramp |
| prep | `<= -100` | `p1` `p2` | prep |
the volume filter `set_seq >= 1` drops rungs and prep alike (prep.yaml `volume: false`).

## warmup turns carry the 3 blocks too (D2)
observed: rung turns after the first had no table and no keyboard though set-add stdout
already carried them. set-add now prints `SET_BLOCKS kind=... table=pin_edit cue=...
keyboard=...` each set = what this reply owes. line suppressed, demand binding:
- table: code updates pin (table 3) and delivers table 2 as a new message. never re-post
  a table in the reply (owner 06:48).
- cue: `SET_CUE:` verbatim, else relay `SET_CUE_MISSING`.
- keyboard: code-posted (row_keyboard, one per row: working = reps -> RIR, setup / ramp /
  prep = one done tap). never author or echo one. `BLOCK_MISSING` (legacy rail only) ->
  say so plainly; never substitute a numbered menu or "아래에 입력해주세요".
no prose-only warmup turn. a ramp is a set.

## prep drill = set (D1)
(2026-08-25: mat 5 + pull 2 + shoulder 3 drills took 21 minutes and left 0 rows, 0 table
lines, 0 targets.)
- per drill exercise-enter prints:
  `PREP_SET p1 seq=-100 kind=prep target=<v> unit=<u> keyboard=completion_tap
  cue=exercise_target volume=no` (target is a unit-bearing token: `20` / `10/side` /
  `1round` / `2x15s` / `?`), `PREP_DONE_TAP p1 keyboard=completion_tap posted=code` (the
  done button is posted by code when the drill is up; no rep question, no candidate
  numbers), `PREP_SET_CMD p1 set-add <sid> <ex> <slot> <seq> <v> --set-kind prep
  --target-reps <v> [--hold-sec <s>]` -> RUN as printed, never compose.
- the done button (`✅ 완료 (pN)`) is code-posted: the first open drill at entry, the next
  one as each lands (`PREP_TAP_POSTED`, set-arm `PREP_TAP pN ... posted=code` +
  `PREP_TAP_CMD pN <argv>`, set-add `NEXT_TAP ... posted=code`). its tap arrives as a user
  message -> run that drill's `PREP_TAP_CMD` / `PREP_SET_CMD`. never render the button.
  legacy rail only (a line WITHOUT `posted=code`): render ONE done button as the line says.
  `PREP_TAP_NO_TARGET` -> guide without a count, take the done tap.
- done wording never says "기록" (2026-08-27: "1번, 20회로 기록했어요" read as a logged
  working set). say done, move to the next drill.
- prep is not a challenge set: prescription = record. never ask how many. owner: a drill
  set up to fail is a prescription defect; never hide it in volume trends.
  - state the prescription in the drill's declared unit (`target_unit`): `reps` total /
    `per_side` (total = 2x) / `rounds` / `hold_sets` (duration `hold_sec`). never lump as
    "반복수" (that stored 1 round as `reps=1`). no value -> no prescription wording, done tap.
  - user did not reach it -> no lower number logged; acknowledge plainly, next drill, park
    a prescription review for after the session.
  - exception: rehab drills or genuinely hard positions may be challenge sets.
- never end a drill with nothing to tap. engine lines present -> single done tap. absent
  -> author a single-item `[[OPTIONS]]` done button (H17 does not apply: no AUTO_ADVANCE
  outside the set path; 2026-08-27 misapplied it, no button, user had to type).
- in sequence, a drill's completion goes ONLY to the next drill. a stray working-slot arm
  already sent -> retract in text ("방금 뜬 세팅 안내는 무시해 주세요, 제때 다시
  안내할게요").
- mat prep enters live on slot 1 (`set-table.MAT_PREP_LIVE_SLOT`).
- target only from prep.yaml `target_reps`. none -> `?` in table + `PREP_TARGET_MISSING`;
  never ask mid-session (2026-08-27 stopped the session to ask), no plausible default.
- `PREP_UNIT_UNDECLARED` -> prep.yaml has a value but no unit; read as total reps; session
  continues; park for after.

## ramp or not is a value (D3)
(user challenged a missing warmup; model defended "엔진이 별도 램프 세트를 산출하지
않았어요", folded 20s later; engine had `[50.0, 60.0]` computed.)
- set-table / exercise-enter print every render, outside the code fence:
  `RAMP_DECISION exercise=<> decision=ramp|none reason=<code> rungs=<n> target_weight=<kg>`.
- reasons: `barbell_ladder` / `machine_ladder` (ramped) · `no_target_weight` /
  `not_ramp_class` / `assist_loaded` / `at_or_below_bar` / `no_rung_below_working` (not).
- never judge ramp yourself; answer from this line. never declare "웜업 없이 갑니다"
  without its reason.
- cable stack (face pull) = machine / stack: pinned stack ramps
  (`set-table._MACHINE_RAMP_LOAD_TYPES`). machine ladder = light rungs in the machine's
  load unit up to just under working, RIR 4+, no plate line (F6-ext #9).

## table columns -- prescribed vs measured (D4)
(deadlift entry `|  bw |  20.0kg |   6  |  4+ | [ ] |`: the 6 was a target, indistinguishable
from a logged 6; logging blanked RIR, so a logged row held LESS than an unlogged one.)
- `REPS`: target before logging; measured after; `실측/목표` (`8/10`) when they differ.
- `RIR` never blanks on logging; rungs keep the prescribed `4+`.
- invariant: a logged row always carries more than an unlogged row.
- `ST` has three states (A2): `[v]` done · `[-]` exercise closed, not done · `[ ]` pending.
  `session-closeout --exercise-exit` turns every unlogged row of that exercise `[-]`,
  persistently (`set-table.exercise_is_closed`).
- no 6th column: phone code-block width (36 -> 43+ soft-wraps every row).

## `WT` 칸은 비지 않는다 -- 산문으로 표를 변명하지 않는다 (D5)
observed excuse: "(표 WT칸은 방금 등록 반영 전 스냅샷이라 비어 보이지만, 실제 적용 무게는
위에 안내한 값입니다.)" -- a wrong table papered over with prose; later it recurred silently.
- blank never means two things: `bw` = nothing to load, `?` = could not resolve.
- a known weight is never rendered blank.
- set-table prints `WT_UNKNOWN exercise=... rows=...` -> a `?` is to FIX, not narrate. fix
  the value; the next publish carries the fixed table (pin edit for table 3; changed
  content passes the delivery ledger). never add "표는 틀렸지만 실제로는 N kg입니다".
