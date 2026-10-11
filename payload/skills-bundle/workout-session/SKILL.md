---
name: workout-session
display_name: 운동 세션 진행
description: >
  Runs the LIVE WORKOUT SESSION -- the in-session experience DURING training,
  not logging a finished workout as one session record (the kit's
  workout-log) and not designing the program (workout-program). Drives SESSION_START step-through (full-body
  dynamic stretch as stage 0, then the session-start routine table), per-set
  rest timers (dynamic 30s-grid push stack, water cadence, selective
  encouragement/form tips), live progress tables (in-set, cross-set,
  exercise-transition overview), per-set rx display (weight + RIR + target
  reps), warmup/stretch sequential guidance, exercise substitution reference,
  and accessory-weight % suggestion DURING the session. Per-set results are
  written by this pack's set-add, and set-level corrections (set-add
  --correct / set-undo / exercise-drop / session-abort) live here;
  program.yaml structure stays with workout-program. Fires on live-session utterances: "세션 시작", "운동
  시작하자", "다음 세트", "쉬는 시간 재줘", "루틴 보여줘", "타이머 시작해줘",
  "start my session", "next set", "start the rest timer", "show my routine",
  "어깨 하자", "오늘 가슴이랑 삼두", "그냥 자유롭게 할게", "free session".
---

# workout-session

live in-session drive. owns moment-to-moment UX: session start, exercise entry, per-set
flow, rest / hold timers, progress tables, warmup / prep sequencing, substitution and
accessory-weight reference, set-level record + correction.
- NOT: session row (kit workout-log: kind, minutes, kcal, HR, note; never sets);
  program.yaml structure (workout-program).
- reads plan from program.yaml (workout-program owned); writes sets via this pack's
  `set-add`. engine = `$PROJECT_ROOT/service/health/`.
- no program.yaml, or the owner asks for an ad-hoc region / lifts -> offer a real free
  session via `session-open --free` (per-set storage and record-backed progression stay
  on). Read `reference/session-start.md` and workout-program `reference/one-off-serving.md`.
  A paused program consult is left untouched. Open parity, `--register`, mid-session
  lifts, intervals, close-out: read `reference/free-session.md`.

## hard rules (every turn)
- engine scripts (rx-calc, set-arm, set-table, set-add, exercise-enter, session-open,
  session-cursor, session-closeout, ...) are EXECUTE-ONLY. run, consume stdout. never
  read / cat them into context in a live session (rx-calc ~120KB, set-arm ~70KB = per-set
  latency, P0). "code: X" in these docs = authority lives in code, not "go read it".
  read source only when debugging / editing outside a live session.
- answer-and-advance: every turn does all three together. ADVANCE (log set / arm timer /
  cue next set, never paused for a question); ANSWER (any question / request / "왜·뭐·
  어떻게·~아냐" closed in the same turn; knowledge search gate first if unsure; no
  swallowing, no half answer); CUE (new exercise / drill -> setup / execution / key points
  / common mistakes before asked; never retracted). this skill text is the ONLY guard for
  question-close; no code gate exists (F16; the question-close hook was never wired, 2026-09-10).
- no batch-note edits during a live session; after it ends.
- live state: before inferring slot / set number or composing a set-add, run
  `service/health/session-cursor resolve <sid>`. the CURSOR block (slot / next_set_seq /
  done_working / planned) is the ONLY truth; keyboard taps log sets with no model turn,
  so chat history can be N sets stale (M4). FALLBACK -> follow its reason.
- stdout machine lines are for you, not the user. shape rule: `TOKEN k=v` -> suppress the
  whole line; `TOKEN: text` -> drop the token, relay the text verbatim; `[[...]]` -> bridge
  marker, never authored where code already delivered it. unknown -> suppress unless colon
  form. full census + binding instructions: read reference/stdout-tokens.md at session
  start and whenever an unlisted token appears.
- `AUTO_ADVANCE: <label>` = an order: do it now, same turn, no menu, no tap wait (H17).
  one candidate (후보가 정확히 하나) -> no menu. `[[OPTIONS]]` only for 2+ real candidates in
  the set path. `NEXT_ACTION_MISSING` -> no auto-advance; relay its sentence, get confirmation.
- tap lists you DO render (no engine keyboard: prep / warmup / mobility drill done, yes /
  no, single confirm, hold timer done) always carry an authored `[[OPTIONS]]` marker, even
  with ONE item: the bridge classifier only attaches buttons to 2+ numbered lines, so a
  one-item list without the marker leaves dead text. code-delivered affordance
  (`KEYBOARD_DELIVERED`, `HOLD_NEXT_ARMED`, `HOLD_*_BTN`, `AFFORDANCE`, `set-arm
  hold-chain`) -> never author one. marker = last line, alone.
- 자백 금지 -- admit a miss only on a real code signal: `SET_TABLE_MISSING`,
  `SET_CUE_MISSING` / `SET_CUE_MISSING_REASON`, `NEXT_ACTION_MISSING`, `GUARD_BLOCKED`, or a
  real non-zero exit. no signal = no miss. an empty-looking screen, "should I have
  posted?", a result that looks off after following the rules: not evidence. say what you
  are doing now ("표를 지금 올립니다", "이 순서가 맞습니다. 프렙 먼저, 표 다음"). a false
  confession makes real misses indistinguishable (H6, 2026-08-24: model apologised for a
  table it correctly did not post; `SET_TABLE_MISSING` fired 0 times).
- 사용자 대면 어휘: prep = 준비운동, warmup / ramp = 웜업, `bw` = 세팅; 폐기어 never to
  the user: 프라이머 -> 세팅, 워밍업 -> 웜업, 프렙 -> 준비운동, 램프 / 렁 -> 웜업, 슬롯 -> 종목.
  never "처방" (-> 오늘 플랜 / 오늘 무게). never internal names, English state keys, ticket
  IDs. never mention skill delegation. session label = rotation code (앞A ...). RIR text =
  what the tool prints, the RIR ask included. read reference/vocabulary.md at session start.
- tool values only: weights, rungs, reps, RIR, unilateral, plates, drill implements come
  from code / data lines. never mint, estimate or borrow a value where code printed none;
  relay the ask line instead (reference/set-gates.md).
- cue-as-data: movement instructions are data. Use the cue + fault already on the
  code-posted row keyboard; send no extra cue message, no improvised replacement prose.
  Delivery failed -> relay the complete numbered cue, fault and completion affordance once.
  Overview card unchanged. Run PREP_SET_CMD / PREP_TAP_CMD / RUNG_SET_CMD exactly as
  emitted: no output filtering, no positional-arg rearranging. Korean session -> all
  owner-facing text Korean; never relay internal English narration. Code-posted
  record / next-set line + keyboard -> no praise, no completion-request footer.
- code-post contract (no contradiction, input asks, OWNER_LINES, ov echo): read reference/code-post-contract.md at session start.

## session start (every SESSION_START)
read reference/session-start.md first. sequence:
1. `rx-calc` first + short ack (its `session_class` is the only regular / makeup authority).
2. `service/health/session-open` -> `session_id`; follow its START_CARD / CARE /
   INSTALL-GAP lines.
3. `bash routines/bundle/session-ensure.sh` (today's task, idempotent).
4. `fatigue-brief open` -> photo + lines verbatim; its buttons are this turn's only decision.
5. condition check C6: `[[OPTIONS: 통증 있음 | 피로함 | 이상 없음]]` (통증 -> pain-triage).
6. stage 0 prep one by one; no working-slot arm before mat prep closes.
turn layout: table (code-delivered) -> prose -> buttons last.

## exercise entry (every exercise)
read reference/exercise-entry.md first. `service/health/exercise-enter <sid> <exercise>`
is the FIRST action, then: (a) injury history lookup (hard gate) -> (b) cue (hard check;
first time full setup + execution, else reminder; one action, no alternatives) -> (c)
warmup with weights -> (d) ramp if big jump -> (e) working target: weight as ANCHOR
"직전 -> 오늘" + expected rep range + RIR -> (f) table = code, after 프렙 gate-close.
prep drills / rungs / holds follow the set-kind table: read reference/set-kinds.md when
any prep drill, warmup rung or hold is on screen.
working-set weight -> read reference/weight-realization.md before the first working set
of each lift (realized value, (잠정), loading unit, plate cue).

## per-set turn
1. set records by keyboard tap (code, zero turns) or text fallback ("15", "15-1") ->
   set-add. read reference/set-recording.md before the first working set of a session.
   never ask reps in prose; never echo `[[IDRILL:...]]`.
2. reply = blocks in fixed order, each on its own line / paragraph, never merged into one
   sentence (F12, G5). register (owner 2026-10-08): record line `✅ <n>세트 · <kg> × <reps>
   · RIR <r>`, then at most 3 short bullets (cue / LOAD_DECISION / note), then the next-set
   blockquote; ONE weight per prescription in text; a load fallback goes to code via
   set-arm --ov-alt-weight <kg>, never into prose (reference/set-recording.md "in-session register"):
   - block 1 table: code delivers (set-add -> `exercise-enter --publish-table`, deduped by
     the delivery ledger). only `SET_TABLE ... fallback=defenced` -> relay those rows verbatim,
     whole ([추세] + [세트] + prev / next tails), never edited, cut or re-typed (F17).
   - block 2 cue: `SET_CUE:` text verbatim (H11). `SET_CUE_MISSING:` -> relay. neither
     (session end) -> no cue, no apology. never skipped on later sets (G5-ext): first
     working set = full setup + execution cue (reference/exercise-cues.md); later sets =
     SET_CUE + short weight / target / RIR / ANCHOR note, nothing newly composed.
   - block 3 rest line: the two `> ` lines under `NEXT_SET`, verbatim (code-emitted,
     `> ▸ 다음 세트: <lift>` / `> <kg> × <reps> (RIR ..) · 휴식 m:ss`). no NEXT_SET ->
     `다음 세트: <NEXT_HINT spec> 휴식 <Z>초`. `NEXT_HINT: (세션 종료)` -> drop the line.
     nothing after the rest line (no "타이머 설정 완료", F12). never narrate pushes, water
     pushes or internal timing.
3. bare-number result ("14") -> answer in a full short sentence: confirm the value + next
   instruction. never a bare number back.
4. weights verbatim with decimals; unit from the loading tag (per_side = "한쪽당 N kg").
5. water: >15 min since the last water line -> one natural, varied full sentence in the
   next reply (reference/timers.md).
6. any `WEIGHT_ASK` / `SEQ_ASK` / `RX_ASK` / `RX_DIVERGED` / `RUNG_REFUSED` / `RAMP_ABSENT`
   / `EXEC_MODE` line, or set-add exit 1 -> read reference/set-gates.md. relay, re-fire once.
7. `LOAD_DECISION:` line, or your weight will differ from the engine -> read
   reference/load-decision.md. agent owns the load; never throw the choice back.
8. `RIR_FLOOR_NOTE:` -> relay the whole sentence (safety cap). intensity / RIR scale:
   reference/coaching.md.
9. user stops an exercise early ("그만할게", "여기까지 할게", next lift with sets left, end)
   -> `--no-next` on that exercise's last set-add (reference/set-recording.md).
10. `SET_TABLE_COMPLETE` = exercise done; its table is already delivered. a re-run
    set-table printing nothing is normal (withheld as already delivered). hold / isometric
    lifts have their own END flow.
11. target change mid-session (substitute / weight) -> `--ov-*` reload, never "표 무시하세요".

## hold / timers
hold or press-start countdown -> read reference/timers.md (start trigger required, done
affordance, `HOLD_NEXT`, hold-chain). hold / unilateral input rules ->
reference/hold-unilateral.md.

## pacing
3+ items -> overview then one by one; one decision per message; "next" stays inside the
bundle; compound steps split. read reference/pacing.md when a list of 3+ items or an
approval bundle is coming.

## session end
0. post-lift blocks (finisher / cardio / cooldown) are the TOOL's, in program order:
   `session-post next <sid>` after the last lift, then its POST_TAP_CMD per tap. never an
   either/or, never a prose cooldown. close-out refuses (exit 6) until each is done or
   explicitly skipped (`session-post skip`). "스트레칭 하자" after close-out ->
   `session-post reopen <sid> cooldown`.
1. `pain.py recent` (pain-triage skill folder) -> open events -> pain-triage phase 2 before
   the wrap. this step is the carrier of pain-triage's must-happen raise.
2. `session-closeout`: minutes come from timestamps; `ASK_WATCH_KCAL:` = the ONE ask
   (kcal only) -> re-run with `--watch-kcal N`. the card is posted by code
   (`CARD_POSTED by=code`: do not re-post); `by=none` -> relay the stdout card as-is.
3. wrap + calorie card posted without being asked, also on early end.
read reference/pacing.md "session end" for the wrap details.

## corrections / deletes
wrong value -> `set-add --correct`; extra set -> `set-undo`; wrong exercise ->
`exercise-drop`; wrong session -> `session-abort`. first call refuses with a count to
echo. never `kit_life.sh workout-del` for a session with sets. read
reference/set-gates.md "corrections / deletes" before running any of them.

## pointer index
| trigger | read |
|---|---|
| session start / C6 / fatigue brief / empty files/program / hip constraint | reference/session-start.md |
| every stdout token, binding A-line instructions | reference/stdout-tokens.md |
| user-facing words, layers, retired words, RIR display / ask / wording pref, rep range | reference/vocabulary.md |
| exercise entry lines, entry order, F14, C12, empty-bar primer | reference/exercise-entry.md |
| prep drills, rungs, set-kind table, ramp decision, table columns, WT `?` | reference/set-kinds.md |
| keyboards, text fallback, rung arm, `--ov-*`, `--no-next`, RIR default | reference/set-recording.md |
| weight / seq / plan-value / rung gates, corrections, deletes | reference/set-gates.md |
| engine vs agent load, LOAD_DECISION | reference/load-decision.md |
| realized weight, (잠정), install gap, stack learning, loading unit, plate cue | reference/weight-realization.md |
| rest / hold / start gate / water / push log | reference/timers.md |
| RIR scale + floor, performance drop, reorder, variant switch, cardio | reference/coaching.md |
| overview lists, one decision per message, compound split, session end + wrap card | reference/pacing.md |
| tip ride, form-callout carve-out, dash format, 75s / 150s schematics | reference/rest-timer.md |
| hold / isometric / unilateral, input mode, weight re-ask, injury axis != weak axis | reference/hold-unilateral.md |
| table 0 mat prep / table 1 start card / table 3 transition, trend, effective volume | reference/progress-tables.md |
| warmup / stretch sequence, warmup %, plate rounding, shoulder mobility, drill gear | reference/warmup-stretch.md |
| first-time cues + gif | reference/exercise-cues.md |
| saved preference / substitute slots, angled smith | reference/exercise-prefs.md |
| accessory null weight + parent calibration | reference/accessory-weight.md |
| calc_rx `needs_lattice` | reference/lattice-jit.md |
| cardio HR zone | reference/cardio-hr-zone.md |
