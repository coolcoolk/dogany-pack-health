# set recording -- keyboards, text fallback, target reload (read before the first working set of a session)

## in-place drilldown (IDRILL, DGN-918/939)
default working-set path: one message, reps tap -> same message swaps to RIR keyboard ->
RIR tap records. zero model turns. the old two-message `[[OPTIONS]]` narration (ask reps,
"N회 확인, 이제 RIR", ask RIR) is retired.

**키보드 배달은 전부 코드가 한다. 모델은 이 경로에 관여하지 않는다.**
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
