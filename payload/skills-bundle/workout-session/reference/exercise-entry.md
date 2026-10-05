# exercise entry (read on every exercise entry)

## the call -- FIRST action of every entry
```bash
service/health/exercise-enter <session_id> <exercise_name>
```
- `session_id` from session-open; `exercise_name` snake_case (`lat_pulldown`).
- `--force` re-publish the table on a corrected re-entry; `--no-table` settings only.
- exit 0 = entry handled (sections best-effort, never blocks); 1 = argument error.
- before injury lookup, cues, warmup. no exception for compound entries (JIT machine
  registration, prep). safety net: a skipped entry is auto-fired by set-add on the
  first working set (table 2 publish, table 3 pin, settings, anchor), but then the
  payload lands late. call it at entry.
- idempotent per (session, exercise). `ENTERED_ALREADY` -> still echo CONFIRMED_SETTINGS /
  RECORD_PARAMS / ANCHOR (read-only, not re-asking); table not re-posted without `--force`.

## stdout handling
- `FATIGUE_SWAP <planned> <substitute>` (fatigue-brief swap chosen at start): entry ran as
  the substitute; record later sets under `<substitute>`. say `FATIGUE_SAY` as-is, render
  `FATIGUE_CHOICE` label (원래 종목으로) as a button. tapped ->
  `service/health/fatigue-brief revert --session <id> --exercise <planned>` then
  `exercise-enter <id> <planned>`.
- `ENTERED ...` -> session_id / exercise_name / first_entry for the flow.
- `CONFIRMED_SETTINGS ...` -> grip / loading / setup_cue used verbatim in warmup + cues.
  never infer grip / loading_side / setup_cue. `none=no_record` -> nothing stored, do not
  re-ask. grip includes WIDTH (#44): give kind + width up front; width missing -> confirm
  once, store, auto-apply after.
- resource facts are CAPTURED, not asked. user mentions gear ("스트랩 쓰고있어", "벨트는
  없어") -> hold it as fact that turn, never re-ask it this session. do not announce the
  capture, no confirmation question. a needed ownership fact not in the conversation ->
  workout-program "자원 ASK-GATE" first; UNKNOWN is not "not used". never infer gear from
  performance ("무게가 뛰었으니 스트랩"). carrier today = the model's memory only; nothing
  persists it (`ledger_resource` has no writer; the capture hooks were never shipped,
  correction 2026-09-15).
- `JIT_CALIBRATION need=yes ask="..."` (#12) -> un-calibrated machine / stack. `ask` is the
  final user wording (tell the stack marks, or send one photo); use verbatim. never build
  base / step questions by hand. `need=no` -> never ask for marks / photo.
  procedure: reference/weight-realization.md "stack learning".
- `RECORD_PARAMS ...` -> AUTO-LOAD; never re-ask anything on this line (#28).
  - `unilateral=<mode>` from program.yaml `unilateral.mode` only (no prose keyword
    inference; that caused #24/#25). `mode=both_one_record`: both sides, one result input,
    no weak/strong split, no rest between sides; rest timer after both
    (reference/hold-unilateral.md).
  - `weak_side_first=yes` -> weak side first, strong side matches its reps.
  - `weak_side=<left|right>` -> auto-load, never ask "약한 쪽 어디에요?".
  - `confirm_side=yes` -> only here ask the weak side ONCE, store it.
  - per-side LOADING ("한쪽당") is a weight unit, not unilateral execution.
- `ANCHOR ...` (#43) -> `prior=` last measured working weight, `today=` from the single
  resolver `set-table.resolve_today_weights` (same source as table WT, SET_CUE, rest-over
  push). put `note="직전 N kg -> 오늘 M kg"` beside the cue verbatim.
  - today's weight comes from ANCHOR `today=` / `note=` ONLY. never program.yaml slot
    weight, last session, or a number from chat (2026-08-24 D1: 140.0 vs 135 in one
    message from a second derivation).
  - no `today=` -> no plan weight (bodyweight / un-calibrated stack / not derived). never
    make one up; cue without weight. table WT is blank / `?` for the same reason.
  - ANCHOR today != table WT (working rows) -> state neither as fact: "표시된 무게가
    갈립니다. 확인 전까지 원판 끼우지 마세요." fix before continuing. equal is normal;
    different is a regression.
  - `first=yes` (prior=none) -> say in one line it is the first record.
- `PREP_PLAN` block (#10/#11/#26) from prep.yaml. every drill is a set (A3 D1):
  `PREP_SET` + `PREP_SET_CMD` per drill, row + `pN` table line + target each.
  user word = 준비운동. detail: reference/set-kinds.md.
  - `PREP_ENTRY` (phase mat_prep / equipment_prep): one by one right after entry (after
    injury lookup, before warmup / cue). text = `display` verbatim; full prose per
    stretch-matrix.md K-code glossary. mat prep arrives on slot 1's entry.
  - `PREP_IMMEDIATE` (phase immediate_primer, `defer=first_working_set`): NOT at entry.
    after cue + table + warmup / ramp, right before working set 1; `hold_sec` timer via
    set-arm countdown press-start then, never armed at entry. first occurrence this
    session: no "한 번 더" / "다시" / "또"; a drill done twice ("x2" in display) says
    "한 번 더" only on round 2 (owner 2026-08-20).
  - order (F2 3-bucket, code: exercise-enter): mat_prep -> equipment_prep -> [entry] ->
    immediate_primer.
  - zone (2026-09-11, owner: 「랫풀다운은 매트프렙이아닌데 구분이 전혀안돼있네」): never
    flatten to 준비운동 1 / 2 / 3. `PREP_ENTRY ... zone=mat|equipment requires=<>` read as
    is; `PREP_PLAN ... zones=mat:4,equipment:2` -> say the split first in the overview;
    `PREP_ZONE_MOVE ... say="..."` -> announce the move BEFORE that drill (say= text or
    same meaning). `requires=` gear not owned -> offer skip beside the done button.
  - `PREP_CUE code=<> setup="..." sensation="..."` (W3) -> verbatim. never assemble,
    rephrase, or invent a cue for a drill that has none.
- `SET_TABLE ...` -> receipt that code delivered table 2 (`delivered=yes by=code`); the
  table is not on stdout. only `SET_TABLE delivered=no` + `fallback=defenced` -> relay the
  rows below it verbatim. placement: 프렙 gate-close 다음 (F14).

## delivery order at entry (all before the user asks)
- (a) HARD GATE injury history lookup for this lift (F10: prompt-level advice failed
  under live pressure). no cue / set talk before it.
- (b) HARD CHECK cue (G3): setup + execution cue (first time) or reminder cue
  (reference/exercise-cues.md). never move to (c) without it. a cue names ONE action for
  today's plan: no "또는 ~" / "~ 없으면 ~로" alternatives in live cues (owner 2026-08-17);
  alternatives live in stretch-matrix.md / exercise-prefs.md, pulled only on request.
- (c) warmup sets with concrete weight; (d) ramp-up if the jump is big.
- (e) working-set target: weight + expected rep RANGE for that set + RIR (reference/
  vocabulary.md "rep range"), weight as ANCHOR "직전 -> 오늘". full exercise name, not a
  bare weight (#43).
- (f) table: code delivers (never relayed, never typed). order =
  **프렙 gate-close -> table (code) -> warmup / first set (model)**. a table after prep is
  on spec; never narrate it as late or missing (자백 금지). "entry" = first message with
  warmup guidance, not "just before the first working set" (F28).
- `SET_TABLE_MISSING` fires only if even set-add's auto-enter could not publish; only then
  run set-table yourself.

## F14 prep before working delivery (owner 2026-08-14; code-enforced 2026-09-11)
prep drills (step_type=prep) in front of a lift go first, one by one with done
confirmation, then the lift's table + working cue.
- table gate `exercise-enter.entry_table_gate_open`: entry-phase prep band (mat_prep +
  equipment_prep) open -> table held: `F14_GATE table=held` + `SET_TABLE
  held=prep_incomplete entry_prep=<logged>/<planned>`. zero prep or unreadable prep.yaml ->
  fail-open.
- arm gate `set-arm.prep_lane_open`: open prep band closes ramp / working arms, incl. an
  explicit `set-arm reps-entry <sid> <ex> 1`. re-arm / correction after a logged working
  set is not blocked.
- held table is not `SET_TABLE_MISSING` and not a failure (자백 금지).
- `PREP_IMMEDIATE` is the deliberate exception (deferred to before working set 1).
- tests: `service/health/tests/test-prep-order-gate-f14.py` (incl. gate-removed mutant).

## knee-flag bodyweight primer (C12, owner 2026-07-31)
slots with `injury_knee` in program.yaml safety_note ONLY: one bodyweight (or empty-bar)
primer set before (c). runs beside the K2 band knee-out primer, does not replace it.
independent of the ax-project warmup array (G7): empty array still means do C12.

## empty-bar primer (F15 / F18)
all barbell compounds (deadlift / barbell row / incline barbell press): empty bar (20kg)
primer = first warmup step, REPLACES the light warmup (not added). big jump to working ->
bar -> middle weight -> working. never reorder.

## drill reference links (F5, on demand)
drills without exercise-form-demo coverage may get a YouTube link (shorts first,
timestamp if possible), added when the drill actually appears. no bulk pre-research.

## pulled on demand
first-time cues -> reference/exercise-cues.md · saved preference / substitute slots ->
reference/exercise-prefs.md · accessory slot null weight + parent calibration ->
reference/accessory-weight.md · calc_rx `needs_lattice` -> reference/lattice-jit.md
