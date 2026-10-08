# stdout machine lines -- classification (read at session start and whenever an unlisted token appears)

stdout machine lines are a contract the MODEL reads, not text the user reads. never
echo, quote, summarise or translate a token. classify by LINE SHAPE, not by list, so a
new token already has an answer (D6, 2026-08-24).

| line shape | class | handling |
|---|---|---|
| `TOKEN k=v k=v ...` (no colon, space/tab fields) | **A. 통째 억제** | not one character reaches the reply. event notice / gate signal only. |
| `TOKEN: <sentence or value>` (colon + space) | **B. 접두 토큰만 제거, 내용은 그대로 전달** | the payload IS content; dropping it loses what the user must know. |
| `[[...]]` bare bracket | **C. bridge marker** | render instruction the bridge consumes. never prefix / wrap. never author one the code already delivered. |

A-shape exceptions -- relay ONE named field, suppress the rest:
`ANCHOR ... note="..."` -> `note=` value only. `PREP_ENTRY` / `PREP_IMMEDIATE` /
`COOLDOWN_ENTRY ... display="..."` -> `display=` value only. `EXERCISE_CARD` -> strip the
head line, show the card body lines below it. `PREP_TABLE kind=... done=n/N` -> strip the
head line, relay the fenced block right below it verbatim (table (0) / (0-E), already
rendered by code; reference/progress-tables.md).

unknown token -> default A; colon form (`TOKEN: ...`) -> B. user-facing reason text
comes pre-rendered in Korean inside the colon line (D4); raw reason codes ride `_REASON`
machine lines. an English reason code inside a user sentence = code regression: do not
relay it, report it.

## A. 통째 억제 (census 2026-08-24, re-census 2026-09-12)
- set-add: `SET_LOGGED` `SET_SEQ_NOOP` `SET_SEQ_OCCUPIED` `SET_SEQ_MISMATCH`
  `SET_TABLE_MISSING` `SET_TABLE_COMPLETE` `WEIGHT_MISSING` `RIR_FLOOR_BREACH`
  `SET_CUE_MISSING_REASON` `RX_VIOLATION` `RUNG_AT_WORKING` `SET_BLOCKS` `BLOCK_MISSING`
  `NEXT_TAP` `TRANSITION` `TRANSITION_WRAPUP` `SET_SEQ_KIND_MISMATCH` `KEYBOARD_RELAY`
  `TRANSITION_CANCELLED` (d3f31d7: undo cancelled the pending next-exercise transition)
- set-arm: `NEXT_HINT` `SET_CUE` `HOLD_NEXT_REQUIRED` `REST_ARMED` `ARMED` `DRY-RUN`
  `RUNG_LOGGED` `HOLD_CHAIN` `HOLD_CHAIN_BTN` `HOLD_CHAIN_DONE` `HOLD_SET` `HOLD_SET_BTN`
  `HOLD_SET_DONE` `HOLD_NEXT_ARMED` `IDRILL_ARM` `IDRILL_ARM_SEQ` `GUARD_BLOCKED`
  `LOAD_DECISION` `LOAD_DECISION_SAY` `AFFORDANCE` `AFFORDANCE_MISSING` `AFFORDANCE_NOTE`
  `AFFORDANCE_REFUSED` `RX_ISSUED` `RAMP_ABSENT_REASON` `RAMP_BASIS_REASON`
  `RAMP_BLOCKED_REASON` `RAMP_BASIS` `RAMP_BLOCKED` `PREP_TAP` `PREP_TAP_CMD`
  `PREP_TAP_NO_TARGET` `RUNG_SET_CMD` `RUNG_SET_CMD_RULE` `RUNG_REST`
  `EXERCISE_INCOMPLETE` (set-arm's tab-separated forms share names with set-add colon
  forms; shape decides, not name)
- live load (batch 3, reference/set-recording.md "live load"): set-add `WEIGHT_FROM_ARM`
  `SET_RECLASSIFIED` `LOAD_NEXT` `ADDON_UNKNOWN` `ADDON_FIX_CMD`; exercise-enter
  `VARIANT_ASK` `VARIANT_OPTION` `VARIANT_SESSION` `SETUP_CUE` `LOAD_ESTIMATE`
  `MACHINE_PHOTO` (reference/exercise-entry.md); exercise-variant `VARIANT_PICK`;
  machine-pick `MACHINE_PICK` `MACHINE_STACK` `MACHINE_ADDON`
- exercise-enter: `ENTERED` `PINNED_CARD` `CONFIRMED_SETTINGS` `RECORD_PARAMS`
  `JIT_CALIBRATION` `SET_TABLE` `PREP_PLAN` `COOLDOWN_PLAN` `IDRILL_ARM` `F14_GATE`
  `PREP_SET` `PREP_SET_CMD` `PREP_TARGET_MISSING` `PREP_DONE_TAP` `PREP_UNIT_UNDECLARED`
  `PREP_ZONE_MOVE` `PREP_CUE` `PREP_NOW` `PREP_SWAP` `FATIGUE_SWAP` `FATIGUE_CHOICE` `MACHINE_ASK`
  `MACHINE_OPTION` `MACHINE_OTHER` `MACHINE_SESSION`
- set-table / exercise-enter: `RAMP_DECISION` `PREP_PLANNED` `WT_UNKNOWN` `DAY_SOURCE`
  `SESSION_UNTAGGED`
- `KEYBOARD_DELIVERED` (set-add / set-arm / exercise-enter), `PREP_TAP_POSTED`,
  `KEYBOARD_RAIL` (set keyboards are code-posted; any `... posted=code` line too)
- live batch 2: `NEXT_SET_LINE` (set-arm) `WT_ESTIMATE` `MACHINE_REGISTER` `MACHINE_GRID`
  (exercise-enter) -- `MACHINE_ASK ... kind=photo`: no machine registered; ask the `ask=`
  text once, no buttons; from the photo / stated increments run MACHINE_REGISTER (name)
  then MACHINE_GRID (base/step) -- or the one-command `MACHINE_PHOTO` cmd (batch 3) with
  the lightest-heaviest plate read off the photo (`--stack 2.5-47.5`).
- 0.36.0: set-add `REST_MEASURED` `REGISTER` `ADDON_SOLVE`; machine-pick `ADDON_SOURCE`;
  session-post `POST_BLOCK` `POST_ROW` `POST_KEYBOARD` `POST_TAP_CMD` `POST_COUNTDOWN`
  `POST_RECORDED` `POST_SKIPPED` `POST_DONE` `POST_GATE` `POST_REOPENED` `POST_NONE`
  `CARDIO_RECORD_CMD` `CARDIO_RECORDED`; session-closeout `CLOSEOUT_REFUSED post_blocks`
  `POST_NEXT_CMD` `POST_SKIP_CMD` `CARD_POSTED` (stderr). colon forms (B, relay verbatim):
  `RECORD_LINE:` `POST_SAY:` `CLOSE_SAY:` `ASK_WATCH_KCAL:` (reference/pacing.md
  "session end").

suppressed does NOT mean ignored. these carry binding instructions:
- `RUNG_SET_CMD` / `KEYBOARD_RELAY` / `RUNG_REST` / `EXERCISE_INCOMPLETE`: warm-up record
  argv, keyboard relay, warm-up pause, not-done verdict -- read set-recording.md "warm-up rows".
- `KEYBOARD_DELIVERED` / `HOLD_NEXT_ARMED` / `AFFORDANCE` / `HOLD_*_BTN`: code already
  sent the keyboard / button / timer. do not author `[[OPTIONS]]`; two keyboards otherwise.
- `TRANSITION`: code carried finished table, wrap line, next table, keyboard. do not
  redraw, do not add buttons. `TRANSITION_WRAPUP delivered=yes` -> wrap line already on
  screen; `delivered=no` -> say the text after the colon verbatim, go to next exercise.
- `SET_BLOCKS` / `BLOCK_MISSING` / `PREP_*` / `F14_GATE` / `RAMP_DECISION` / `WT_UNKNOWN`:
  reference/set-kinds.md. `PREP_SET_CMD` / `PREP_TAP_CMD` = argv to RUN as-is, never compose.
- `PREP_NOW` (exercise-enter) / a prep row's `SET_CUE:` (set-add): the drill owed now
  and HOW -- name + dose, `1회 = ...` (the one count definition), ordered steps, one
  `⚠️` mistake line, from data (service/health/prep_cues.json). Relay that block
  verbatim; never explain a drill or its count in your own words, never offer a second
  way to count. `SET_BLOCKS ... table=prep_table` = the turn's table is the
  `PREP_TABLE` fence, not the pin.
- `PREP_TARGET_MISSING`: no target for that drill. do not ask mid-session, no plausible
  default; run the drill without a count, park the gap for after the session.
- `DAY_SOURCE source=session_type` = read; `rotation_queue` / `file_order` = inferred.
  `SESSION_UNTAGGED` = split / title / plan are inferred: say so or fix the tag, never
  speak as if read. fix = `service/health/program-init check` (verdict), `program-init
  sync` (rows from the card), `program-init next` (first question when no card). never
  hand-INSERT a rotation code.
- `SET_SEQ_NOOP` / `SET_SEQ_OCCUPIED` / `SET_SEQ_MISMATCH` / `WEIGHT_MISSING`:
  reference/set-gates.md.
- `FATIGUE_SWAP` / `FATIGUE_CHOICE`: reference/exercise-entry.md.
- `MACHINE_ASK delivered=yes` / `delivered=already`: code already sent the machine
  question with its buttons. do not ask it again, do not author buttons. a machine name
  the user types after the 다른 기계 button -> run the `MACHINE_OTHER` cmd with that name.
  `MACHINE_ASK ... ask="..."` (no `delivered=`) -> ask the `ask=` text verbatim, one
  button per `MACHINE_OPTION` (its `cmd` = argv to run) plus 다른 기계.
  `MACHINE_SESSION` -> this session's machine is known; ask nothing.
- `RX_ISSUED` / `RAMP_*_REASON` / `RX_VIOLATION` / `RUNG_AT_WORKING` are D4 machine lines;
  the user sentence for the same event arrives as a colon line (below). never lift a raw
  reason code into speech.

## B. 접두만 떼고 페이로드 전달 (삭제 금지)
- `SET_CUE: <text>` -> block 2 cue, verbatim.
- `SET_CUE_MISSING: <한국어>` -> cue failed; relay as-is.
- `NEXT_HINT: <spec>` -> next-set line verbatim (only when no `NEXT_SET` block).
- `NEXT_SET (...)` head line -> drop it; relay the `> ` lines right below it verbatim.
- `WT_ESTIMATE_SAY: <한국어>` -> the labelled starting estimate of a new lift. relay.
- `NEXT_ACTION_MISSING: <한국어>` -> relay + do NOT auto-advance.
- `RIR_FLOOR_NOTE: <한국어>` -> safety cap notice, relay whole (reference/coaching.md).
- `REST_ARMED: <초>초 (...)` -> rest between hold sets, relay.
- `SEQ_ASK: <한국어>` / `WEIGHT_ASK: <한국어>` -> the question to ask, relay.
- `HOLD_NEXT: <label>` -> NAME of the next action (다음 세트 / 다음(진행) / 완료).
- `AUTO_ADVANCE: <label>` -> the one exception: not read aloud, an ORDER. do it now.
- `LOAD_DECISION: <한국어 한 문장>` -> today's load decision + reason. relay verbatim;
  never summarise, rewrite or turn into options (reference/load-decision.md).
- `RX_ASK: <한국어>` -> the plan axis code could not resolve. relay; never fill a number.
- `RX_DIVERGED: <한국어>` -> recorded value differs from code's. relay.
- `RUNG_REFUSED: <한국어>` -> rung at/over working weight not recorded. relay + offer the
  two branches it names (record as working / planned warmup weight).
- `RAMP_ABSENT: <한국어>` -> WHY there is no warmup. relay; never shorten to "없습니다".
- `EXEC_MODE: <한국어>` -> bilateral / unilateral + its source. relay.
- `FATIGUE_SAY` line -> say as-is (reference/exercise-entry.md).
- `LOAD_NEXT_SAY:` / `CALIBRATION_SAY:` / `LOAD_ESTIMATE_SAY:` / `VARIANT_SAY:` /
  `SETUP_SAY:` / `ADDON_ASK:` / `ADDON_SAY:` -> code-decided weight / implement / setup /
  block sentences. relay verbatim; never add a second number or a choice of your own.

## C. bridge markers
- `[[IDRILL:<arm_id>]]` = script-to-script signal. NEVER put it in a reply (code delivers
  the keyboard; reference/set-recording.md). never invent one.
- `[[OPTIONS]]` / `[[OPTIONS: a | b]]` = authored by the model only where no code
  affordance line says the keyboard is already out. marker = last line, alone.

ticket IDs (`(DGN-388)`) and parenthesised English expansions (`(Reps In Reserve)`) are
leaks too, including in folded reasoning blocks.
