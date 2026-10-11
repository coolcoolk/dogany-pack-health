# set recording -- keyboards, text fallback, target reload (read before the first working set of a session)

## in-place drilldown (IDRILL, DGN-918/939)
default working-set path: one message, reps tap -> same message swaps to RIR keyboard ->
RIR tap records. zero model turns. the old two-message `[[OPTIONS]]` narration (ask reps,
"N회 확인, 이제 RIR", ask RIR) is retired.

**키보드 배달은 전부 코드가 한다. 모델은 이 경로에 관여하지 않는다.**
keyboards are code-posted (2026-10-08, service/health/row_keyboard.py): one per owed row
(working = reps -> RIR, setup / ramp / prep = one done tap), each its own code-sent message;
a repost edits it in place, a superseded / typed-over / undone row loses its buttons.
(code: service/health/set-arm, routines/push.sh; contract bridge/IDRILL-ARM-CONTRACT.md)
A1-KEYBOARD (2026-08-25, session 10092): when the model had to echo the marker, 3 of 40
minted arms rendered and the user typed 30+ results by hand. delivery moved to code at
all three mint points:
1. working-set entry (`exercise-enter` -> `set-arm reps-entry`): keyboard as its own
   message right after the table (`marker=arm-entry`).
2. set-start / rest-over push (`set-arm` main path): carries the arm of the set it cues.
3. warmup rung (`set-arm` rung branch): next ladder step's keyboard in its own message
   (`marker=arm-rung-next`).
set records only when the callback fires the arm's declared argv
(`set-add ... {1} --rir {2}`). button windows (reps R-2..R+2, RIR 0..4+/skip), labels and
regex live in the arm file; the bridge knows no values.
post-log correction arm: after a set records, set-arm re-arms the same seq (declares
`--correct`) and does NOT push it. re-tap = overwrite. pre-log arms never carry `--correct`
(that would disarm the collision gate).

rules:
- `[[IDRILL:<arm_id>]]` is an A-class line: 절대 응답에 싣지 않는다. no echo, quote,
  mention, invention. code already sent it; a second copy = two keyboards.
- keyboard-bearing turn carries NO operating instructions (owner 06:48 2026-08-25;
  measured redundant 4/4). the button + the arm's `step_text` are the whole message.
- never ask reps in prose: "몇 개 하셨어요?", "몇 개 하셨는지", "몇 회 하셨", "반복수
  알려주세요", "몇 개예요", and any synonym, also when pointing at the keyboard ("몇 개
  하셨는지 아래에서 탭해 주세요" is banned too).
- never rebuild reps / RIR as a numbered `[[OPTIONS]]` list; no "N회 확인. 이제 RIR
  알려주세요" narration.
- text stays open as ADDITIVE fallback: "15" or "15-1" -> record via text path at once.
  out-of-window values come as text. both converge on set-add.
- RIR label = whatever the tool prints (ui_labels knob). never invent an alias.

scope:
- 2-step (reps -> RIR) = working sets (`set_seq >= 1`) only.
- warmup rung (`set_seq <= 0`: `bw` 세팅, `r1..rN`) = 1-step arm: reps tap records, no RIR
  asked; arm declares `step_final: "1"`, argv has no `--rir`, `workout_sets.rir` stays NULL.
  rungs are prescribed RIR 4+; never write the prescription into the measured column.
  button window = the rung's own taper target; keyboard text names the rung (starts
  `웜업 빈 봉` for the empty bar), so a 20kg rung never reads like a 100kg working set.
- empty-bar first set = `set_seq 0` rung; weight-free, `--weight` may be omitted.
- hold / isometric (seconds): arm skips the reps step (step1 empty), starts at RIR; hold
  END flow separate (reference/timers.md, hold-unilateral.md).
- open-weight set (weight undecided): weight-reps-RIR text path.

## RIR default fill (owner 2026-07-29)
result reported without RIR -> slot target RIR met; completed row's RIR cell = slot
target. RIR cell only; reps cell is always the measured value.

## target reload mid-session (F19/F21, code: service/health/set-arm)
user changes the target -> ride it through set-add, never "표 무시하세요" in prose.
- substitution (e.g. 케이블 플라이 -> 펙덱): record on the original slot with
  `--ov-display "<대체 종목명>" --ov-weight <kg> --ov-reps <reps> --ov-rir <rir>`.
- weight only: `--ov-weight <kg>`. back to plan: `--ov-clear`.
- fallback weight: `--ov-alt-weight <kg>` (weight row on the keyboard; dropped when the load changes).
- effect: re-fired set-start push, set-table remaining rows and NEXT_HINT follow the new
  target; stale push / timer auto-cancel. `--ov-*` is NOT a correction signal (see
  set-gates.md `--correct`). load differs from engine -> reference/load-decision.md.

## early stop -- `set-add --no-next` (C12-B, 2026-08-24)
code already refuses to arm after the last prescribed set (F14 set count) and without a
fresh real set write (`rest_bound`). the one gap: sets remain but the user stops early.
triggers (match targets): "그만할게", "여기까지 할게", moving to another exercise with sets
left, ending the session. -> attach `--no-next` to the LAST set-add of that exercise
(kills countdown, before-markers, set-start push). not on a normal transition after the
prescribed sets.

## warm-up rows: tool-issued record command, keyboard relay, rest (hotfix 0.34.x, live 2026-10-08)
- tool output is relayed WHOLE. never pipe `set-add` / `set-arm` / `exercise-enter` output
  through `grep` / `head` / `sed` / `tail` -- the keyboard line (`KEYBOARD_DELIVERED`,
  bare `[[IDRILL:...]]`, `KEYBOARD_RELAY` + its `[[OPTIONS: ...]]` line) is easy to filter
  away, and then the owner hears "웜업 세트는 버튼이 안 떠요" for buttons that existed.
- `RUNG_SET_CMD <label> set-add ...` = the literal argv that records the next 세팅/웜업 row.
  owner reports that row by text -> run it VERBATIM (change only the reps number when the
  count differs). never assemble set-add arguments yourself: the positional order is
  `<sid> <exercise> <slot> <seq> [reps]`, warm-up seqs are <= 0, and a hand-built
  `... 0 10 --set-kind ramp` is now refused (`SET_SEQ_KIND_MISMATCH` + `SEQ_ASK:`).
- `KEYBOARD_RELAY` (only when the warm-up keyboard did not land by code): put the next
  line, `[[OPTIONS: N회 완료 | 다른 횟수]]`, verbatim as the last line of the reply.
- `RUNG_REST <sec>` is the warm-up pause (60s between rungs, 90s before working set 1).
  no timer runs for a warm-up; never quote the working rest (`휴식: ...` in the table) for it.
- every recorded 세팅/웜업 row republishes the set table by code (`SET_TABLE delivered=yes`),
  same as a working set. no prose-only "기록했어요 ... 다음 세트" turn.
- `EXERCISE_INCOMPLETE` = planned working sets remain: no wrap-up, no next exercise.
- every user-visible line is Korean, including progress narration between tool calls
  ("명령 인자를 잘못 넣었어요", "확인하고 바로 기록할게요"). no English sentence ever
  reaches the owner ("Command argument mistake on my side", "Dry-run works, so ..." were
  live leaks).

## live batch 2 (owner 2026-10-08)
- reps(+RIR) reply on a rung/set the tool prescribed -> run set-add WITHOUT asking the weight
  (rung: RUNG_SET_CMD; working: no `--weight`). code records the prescribed weight. ask the
  weight only when the owner says it differed ("16kg 아니고 14kg") -- then pass `--weight`.
  never "몇 kg짜리 덤벨로 하셨어요?" for a weight the tool itself prescribed.
- probe rung (estimated working weight): the rung keyboard asks RIR too. a text reply carries
  it: RUNG_SET_CMD + `--rir N` (4+ -> `--rir 4`). `LOAD_DECISION:` after a rung = the probe
  verdict (one more heavier rung, or the working weight set from the probe) -- relay verbatim.
- `LOAD_DECISION:` after a working set on a calibration lift = the in-session step-down
  (set short of the rep floor). relay verbatim; the next set's numbers already follow it.
- `TRANSITION deferred=Ns`: the exercise is done; reply with the record line only. code
  posts the wrap-up, the next table, the machine ask and the keyboard AFTER the reply.

## in-session register (owner amendment 2026-10-08, after batch 2)
`OWNER_LINES posted=code` (code rail, 0.36.0): the record line, the LOAD_* / CALIBRATION
sentence and the NEXT_SET lines are ALREADY on the owner's screen as one code-posted message
(`REGISTER ... reply=none_owed`). Do NOT repeat them; answer only what the owner asked.
A piped call (`set-add ... | grep`) is refused by the pack's PreToolUse gate -- run it bare.
Without that receipt (code rail off / post failed) the reply carries them itself:
the reply to a recorded working set is exactly, in this order:
1. the record line: `✅ <n>세트 · <kg> × <reps> · RIR <r>` (weight verbatim with decimals;
   a weight-free set drops `<kg> × `; no RIR logged drops ` · RIR <r>`). code prints it:
   `RECORD_LINE: <line>` (set-add, every working set) -- relay it verbatim, never recompose.
2. at most 3 short bullets (`- `): the `SET_CUE:` text, a `LOAD_DECISION:` /
   `RIR_FLOOR_NOTE:` sentence when one is printed (verbatim, they take priority), a
   one-clause weight / target note. nothing else; fewer is fine.
3. the next-set blockquote (`NEXT_SET` lines, verbatim).
never: a praise sentence ("좋아요!", "잘하셨어요", "깔끔합니다" ...), a restated table,
or a "끝나면 ... 말씀해 주세요" / "끝나면 알려주세요" footer when a keyboard is on the row
(`KEYBOARD_RAIL code`, `KEYBOARD_DELIVERED`, `... posted=code`) -- the keyboard IS the ask.
the footer is allowed only on a row with no keyboard (text fallback). set-add prints
`REGISTER footer=none ...` whenever a keyboard is on the row -- that line is the gate.
an estimate in a bullet (e1RM, a starting weight, a rest, a kcal) cites the kimwog item it
comes from (`kimwog <lane>/<item-id>`) or says `추정`; a number with neither is not said.

## one weight per prescription (owner amendment 2026-10-08)
a next-set / rung / working prescription names ONE weight: the one code printed. never
a fallback in the same line ("20kg, 플레이트 없으면 15kg", "16 또는 14kg", "~ 없으면 ~로").
if the owner's gym may not load it (e.g. no 1.25 plate), keep the line to the one weight and
run `set-arm <sid> <ex> <seq> --ov-alt-weight <kg>`: the next set's keyboard offers both
weights (prescribed preselected) and records the tapped one. On a bridge without that
support the keyboard keeps the one weight; the owner says if it differed (`--weight`).

## live load -- weights come from the tool, every set (live 2026-10-08 batch 3)
code: service/health/live_load.py (+ live_load.json), on top of batch 2's prescribed-weight
default, probe rungs and step-down. every point where the owner had to ask back was a
number the code did not produce; it produces them now.
- `WEIGHT_FROM_ARM` = set-add recorded the row at the weight the tool prescribed for it (no
  `--weight` passed). state it in the record line; never ask "몇 kg으로 하셨어요".
- `LOAD_NEXT_SAY:` (after a set of a lift with no measured basis) -> the next weight change
  with the pin / plates, already armed (NEXT_SET, table, keyboard carry it). it is the
  register's weight-note bullet, verbatim; never "한 칸 올려도 좋아요" without the number,
  never a second suggestion of your own. (a step DOWN on a short set stays batch 2's
  `LOAD_DECISION:`; one author per set.)
- `SET_RECLASSIFIED ... kind=ramp` + `CALIBRATION_SAY:` -> the tool classified the first set
  of an unknown weight as a calibration rung (implied reps at the target RIR ABOVE the
  band -- it was a ramp-up -- and the grid has a better weight) and re-prescribed working
  set 1. relay; never move rows yourself. a first set inside or below the band stays working
  set 1 (below -> batch 2's step-down).
- add-on block on a stack: a block sits on the pin and its weight is unknown ->
  `set-add ... --weight <pin> --addon unknown`. the row is stored at the pin weight (flagged,
  never a guessed 1.25). SOLVE FIRST (0.36.0): `ADDON_SOLVE machine=.. label=".." query=".."`
  -> name the machine from the stack photo's label, web-search the query for that machine's
  add-on increment, and on a hit run `ADDON_FIX_CMD` with `--addon <kg> --addon-source <url>
  --addon-confidence high|medium|low`; the reply states the source and the confidence
  (`ADDON_SAY:` carries both). no source found -> relay `ADDON_ASK:` (once, verbatim) and run
  the fix with `--addon-source owner` when the owner answers. never a number with no source.
  the fix corrects every flagged row and adds pin+block weights to the machine's grid. a
  known block -> `--addon <kg>` (stored pin + block). never name an object in a photo with confidence
  (grip handle / strap rack / weight block): unsure -> ask once what it is.
