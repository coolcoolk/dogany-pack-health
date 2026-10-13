# session start detail (read on every SESSION_START)

## order of calls (F1 speed: no dead air)
Free session: `session-open --free ...` is the whole open -- it runs the install lane
(`INSTALL_ENSURE ...`), writes the 표3 pin, posts the lineup card (`START_CARD
delivered=yes`) and prints CARE. Do not run session-ensure.sh after it; if it runs anyway,
it prints `FREE<TAB><id>` and does nothing.

1. `service/health/rx-calc` FIRST + short ack. `session_class` in its output is the ONLY
   authority: `regular` -> serve `rotation_day` slots; `makeup` -> do not serve rotation
   slots as a regular session, hand off to workout-program "주말 보충세션 규칙". never
   re-judge regular / makeup from weekday or inference. never infer / serve rotation slots
   before rx-calc runs.
2. `service/health/session-open` -- row birth via workout-add (DGN-231 dedupe kept),
   birth tag (`session_type_id` from rx-calc; regular = rotation code, makeup = 보충,
   provisional -> NULL, closeout tags later), active marker. idempotent, best-effort.
   never raw `kit_life.sh workout-add`. take `session_id` from `OPENED session_id=<id> ...`.
   its other stdout:
   - `START_CARD delivered=yes` -> lineup table is already on screen ABOVE your reply.
     never re-render the lineup in chat; prose below it, `[[OPTIONS]]` last.
   - `CARE <n> line(s)` + indented lines -> say them verbatim this turn, below the lineup,
     above the buttons.
   - `INSTALL-GAP` block / `taxonomy=` `install=` keys -> install incomplete. handle now,
     not at the first working set (reference/weight-realization.md "exit 3").
   - `NOTE <text>` -> read; relay only if it concerns the user.
3. `bash routines/bundle/session-ensure.sh` -- creates today's "헬스 - <next_split>" task if
   missing, no-op otherwise. do not wait for it.
4. fatigue brief (before the condition question):
   ```bash
   service/health/fatigue-brief open --session <session_id> --day <rotation_day> --json
   ```
   - `photo` -> send it first (send_file), then `lines` (max 4) -> `say` verbatim. no edits,
     no added numbers / lifts / times.
   - `choices` present (중간 / 많이 level) -> those labels as buttons; that is THIS turn's
     only decision; condition question comes next turn. answer ->
     `fatigue-brief pick --session <id> --pick <pick>`, say output verbatim
     (`expand` = full list + same buttons again; `keep` = today's regular plan).
   - A cardio / small-muscle / mobility pick returns `activity` and `regular_day_next`.
     Follow that activity for this session. The pick records the decision and tags
     this session `보충`, outside the rotation; use `보충` for closeout too. The
     regular day named by `regular_day_next` stays next. Do not serve the regular
     lifts after an alternative pick. A `small_muscle` or `mobility` activity
     starts a short user-directed selection of movements; no lifts are invented.
   - Optional owner setting: `cardio_preference` at the top level of
     `files/program/program.yaml`, using `stairs`, `run`, `incline_walk`, `bike`,
     or `row` (Korean display names also accepted). With no setting, the open
     offers all five methods. This key can be populated by a preference flow;
     fatigue-brief only reads it.
   - no `choices` (조금 / 없음) -> no question; append the `expand` label (전체 근육 피로 보기)
     at the END of the condition button row. one button row. 조금 level warm-up boost =
     one extra prep set for `proposal.nodes` regions (the sentence already says so).
   - never lead with rest / skip / "오늘은 가볍게 쉬어가자"; the tool has no such level.
5. condition check C6 (owner 2026-07-31; buttons 2026-08-22, landed 2026-09-01): one-line
   question + one line per option + marker alone on the last line:
   `1. 통증 있음` -> pain-triage now; `2. 피로함` -> propose lower sets / more RIR today;
   `3. 이상 없음` -> stage 0 in order.
   `[[OPTIONS: 통증 있음 | 피로함 | 이상 없음]]`
   body numbering = marker labels, same order, same words. text answers take the same
   branch (buttons are affordance, not gate). no interview / checklist expansion.
6. stage 0 (mat prep) one by one. NO working-slot arm before mat prep closes (2026-08-27:
   "이상 없음" armed a working slot at once, keyboard and all). missing drill targets do not
   stop the session (`PREP_TARGET_MISSING`, reference/set-kinds.md).

## another body part today -- split choice (owner 2026-10-12)
The owner wants a different body part than `rotation_day` ("오늘 상체해야겠는데"). rx-calc's
`split_choice` block is the whole answer; never offer an option the tools cannot run.
- `split_choice.recent_load[].line` -> say it verbatim, one line each ("토요일 자유 세션에
  하체(데드리프트)를 했어요"). A free session is recent load only; never rewrite its row.
- the fork is `split_choice.fork`, in order: `[[OPTIONS: <swap> 정규로 | 자유 세션]]`
  (e.g. `[[OPTIONS: 상체B 정규로 | 자유 세션]]`). `fork_paths` is what each entry runs:
  `<swap> 정규로` -> `rx-calc --split <swap>` then `session-open --split <swap>` (that
  split's lineup, prescription, progression and week tally; the queue day stays in this
  week's remaining splits; step 3 becomes `session-ensure.sh "" <swap>`); `자유 세션` -> `session-open --free --regions ...`. no `swap`
  (no other split remains) -> the fork is `자유 세션` alone.
- never offer "순번 변경" / "순서 바꾸기" or any option without a command behind it. unsure
  whether a path runs -> dry-run it first (`session-open --split <code> --dry-run` ->
  `SPLIT_OK`), then offer it. `session-open --dry-run` prints the same block
  (`SPLIT_CHOICE` / `RECENT_LOAD` / `SPLIT_FORK`).
- `SPLIT_REFUSED <SPLIT_UNKNOWN|SPLIT_LIVE> ... remaining=<csv>` (exit 4) ->
  nothing was created; offer only a `remaining` split or the free session. `--subtype` is a
  row label, never a split change.

## start-turn block order (owner 2026-09-11: 「표-평문-버튼 이게 기본이라고 왜 표가 제일
아래에나와」)
applies to the start turn and every turn that shows a table:
```
1  표     (top, if any; at session start the code-delivered START_CARD)
2  평문   (question / explanation / cue)
3  버튼   (`[[OPTIONS: ...]]` always the last line, alone)
```
- buttons never above the body; a table never below prose.
- the pinned card is a bridge-managed separate message; its position is not yours. never
  confess "the table came out at the bottom" over the pin (자백 금지, SKILL.md).
- F14 holding the table (`SET_TABLE held=prep_incomplete`) -> no row 1 that turn; go 2 -> 3.
- this order has no code gate except START_CARD delivery and the set-arm countdown defer.

## session label (batch #19)
label / caption / wrap / summary / retro name the session by rotation CODE
(`session_type.code`: 앞A / 뒷A / 앞B / 뒷B / 보충). muscle display names ("가슴+쿼드") only
as a parenthetical after the code.

## `files/program/` empty (fresh instance)
`prep.yaml` / `stretch-matrix.md` / `gym-layout.md` / `program.yaml` = USER data; no
install lane writes there. empty = boundary, not defect. this skill consumes prep data:
- no `prep.yaml` -> prep / cooldown blocks stay empty. never invent drills, never grep
  stretch-matrix prose to rebuild them. tell the user once, quietly, that prep is not
  designed yet; route to workout-program.
- no `stretch-matrix.md` -> no drill prose (setup / execution / mistakes). `display`
  verbatim only; never invent cues.
- templates ship at `service/health/sot/prep.TEMPLATE.yaml` and
  `service/health/sot/stretch-matrix.TEMPLATE.md`. never copy the template to
  `files/program/prep.yaml` (example drills would fire as a real plan).
- prep design (add / move / delete drills, session-type blocks) = workout-program.

## hip constraint in the user ledger (F20)
- mat prep: hip drill volume high every session (reference/warmup-stretch.md hip step).
- cooldown is data: `files/program/prep.yaml` `days.<세션>.cooldown` (peer of `.prep`).
  hip stretch = drill code HP1 in all four sessions, rendered as the morning card's
  "C 쿨다운(세션 마무리 · 하나씩 순차)" block. wording owned by prep.yaml, verbatim. not a
  set; not in volume.
- active hip pain event in the ledger -> treat response to that volume as observation data
  for the event. side / event number / symptoms come from the ledger only.

## Free-session routing (owner override, 2026-09-28)

"어깨 하자", "오늘 가슴이랑 삼두", and "그냥 자유롭게 할게" route to a real
free session, even without program.yaml or during a paused consult. Read
`workout-program/reference/one-off-serving.md` for the proposal, safety, calibration,
and trailing-offer rules. Use `session-open --free --regions shoulders` (recorded
venue) or add `--venue gym` only when confirmed. Lifts the owner named go in
`--exercises` in their words, every one (`--exercises 데드리프트,클린`; the open
registers an uncatalogued one). Normal per-set tools select the
session-local prescription from the session id. Close with `session-closeout <id>`;
never write a planned rotation code onto this session. Leave the consult resumable.
