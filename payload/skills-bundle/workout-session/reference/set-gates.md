# set-add / set-arm gates (read when set-add exits 1, or a WEIGHT_ASK / SEQ_ASK / RX_ASK / RX_DIVERGED / RUNG_REFUSED / RAMP_ABSENT / EXEC_MODE line appears, or a correction / delete / defer of today's split is asked)

every gate below is STRUCTURALLY ENFORCED in code. the model's job: relay the colon
line, re-fire the call correctly once. never treat a refusal as a failure to skip, never
retry the same call unchanged, never re-ask values preserved on the refused line.

## weight missing (code: service/health/set-add; incident 2026-08-20)
- `--weight` omitted on a working set (`set_seq >= 1`) -> set-add restores it from the live
  arm (.idrill-arm). button and text paths converge. add `--weight` only for a weight the
  user said (explicit always wins); never guess one.
- still unknown on a bar + plate lift -> not recorded, exit 1:
  `WEIGHT_MISSING exercise=<> set_seq=<n> armed=none` + `WEIGHT_ASK: <한국어>`.
  relay the ask; on answer re-fire the same call with `--weight <kg>` only.
- bodyweight, machine / stack, cable, fixed dumbbell, unmapped lifts and `set_seq <= 0`
  rungs are not gated.

## plan-value source (code: service/health/rx_source.py; incidents 2026-09-11)
ruling: set-start plan values (weight / unilateral / reps / RIR) come ONLY from code. the
model may explain a value, never mint one. (2026-09-11: a `weight_kg: null` slot showed
`? / ? / ?`; speech filled 115kg incl. warmups, a value no code path produced; same
morning speech claimed a unilateral switch no slot declared.)
- no silent axis: every arm prints all four axes with source:
  `RX_ISSUED exercise=<> seq=<n> weight=115:override exec=bilateral:default reps=20:rx rir=1:rx`.
  unresolved = `weight=unknown:none`, a value, not a blank.
- unresolved -> `RX_ASK: <한국어>` follows. relay it.
- recording is verified: value differs from code's -> `RX_VIOLATION ...` +
  `RX_DIVERGED: <한국어>`. working set still records; mismatch shows in the same message.
  user-stated weight is not a violation (P2).
- unilateral comes only from declaration: `set-table.resolve_unilateral`. none declared ->
  bilateral (`RECORD_PARAMS exec_mode=bilateral exec_mode_source=default`). safety_note
  prose ("싱글레그") is only a hint (`exec_mode_hint=`) -> `EXEC_MODE: <한국어>` says
  "선언이 없어 양측으로 갑니다"; relay. promote to unilateral = user edits program.yaml.

## warmup ladder ceiling (code: service/health/set-table `gate_rung_ceiling`)
- rung weight < working weight, checked at publish (`ramp_decision`), arm re-plan and
  record (set-add). cannot build -> no ramp, and it says why. unknown ceiling -> fail OPEN.
- rung at/over working weight is refused as `set_seq <= 0`: exit 1 + `RUNG_AT_WORKING` +
  `RUNG_REFUSED: <한국어>` (a working-weight rung would poison `last_logged` and next
  week's ladder). relay + the two branches.
- no warmup -> `RAMP_ABSENT: <한국어>` with the reason (isolation / assist load / at or
  below bar / no rung below working), only while no working set is logged. relay.

## set-slot collision (code: service/health/set-add; incidents 2026-08-21, 2026-09-01)
`set_seq` is chosen by the model; a miscount used to overwrite a real row silently.
- identical value at the same slot (button re-fire) -> passes, exit 0, plus
  `SET_SEQ_NOOP ... next_free=<n>`. if the user just did a NEW set, re-fire with
  `set_seq=<next_free>`; otherwise the set count stays silently wrong.
- different value at an occupied slot without `--correct` -> not recorded, exit 1:
  `SET_SEQ_OCCUPIED exercise=<> set_seq=<n> existing=<> incoming=<> next_free=<m>` +
  `SEQ_ASK: <한국어>`. existing row untouched. decide intent, re-fire ONCE:
  new set -> same call with `set_seq=<next_free>` (never count yourself);
  correction of a logged set -> same call + `--correct`.
  only when truly undecidable -> relay `SEQ_ASK`.
- `--correct` = the only "write THIS slot" signal. two meanings, both enforced:
  (1) overwrite an occupied slot; (2) write a slot the ladder already passed, even empty
  (`SET_SEQ_MISMATCH` without it). typical (2): filling a warmup rung after working sets
  were logged. `--ov-*` never opens overwrite.
- rungs are protected the same. next_free per lane: working MAX(seq>=1)+1, ramp
  MIN(seq<=-1)-1; empty-bar `set_seq 0` is single-row -> `next_free=none` (so `--correct`
  or a ramp seq).
- button re-tap correction is open: post-log arm declares `--correct` (reference/set-recording.md).

## corrections / deletes (set-level; moved from kit workout-log 0.17.0)
kit workout-log owns the SESSION row only (`workout-upd`: minutes / kcal / HR / note).
everything below it is here, engine in `$PROJECT_ROOT/service/health/`.
1. pick the verb by SCOPE:
   - one wrong value -> `set-add --correct` (in-place, row count unchanged)
   - one set that should not exist -> `set-undo <session_id> <exercise_name> <set_seq>`
   - whole exercise by mistake -> `exercise-drop <session_id> <exercise_name>`
   - session opened by mistake -> `session-abort <session_id>`
   they also clean arm files (incl. next set's), running countdown,
   .set-table-published / .exercise-entered / .set-arm-override / .plate-cue markers and
   the pinned 표3 card, and archive destroyed rows to files/program/.discarded/ first.
2. first call REFUSES (exit 3) and prints what it would destroy. exercise-drop /
   session-abort then need `--confirm-sets <n>` echoing that count; set-undo needs
   `--allow-hole` mid-sequence. relay the Korean `*_ASK:` line, wait for the answer, re-run.
   never invent or assume the count.
3. removed `set_seq` leaves a HOLE; later sets never renumber. that is why a number is missing.
4. DANGER: `kit_life.sh workout-del <id>` and `kit_life.sh experience-delete-source
   workouts <id>` cascade-delete EVERY set of the session (`ON DELETE CASCADE`), only
   REPORT dangling markers, never clear the pinned card. guarded (`--confirm-destroy-sets
   <n>`), but the guard stops accidents, it does not make them right. whole session ->
   `session-abort`; `workout-del` only for a set-less (cardio) row.

## defer today's split (in-session: session-defer; no session yet: kit_life.sh workout-defer)
"미룰래" / "내일로" about today's split, mid-session or before it starts.
Verb: a session row exists today -> `session-defer`; none yet (schedule-log only) -> `kit_life.sh workout-defer`.
Same args for both.
1. ask: `session-defer [--from <day>] [--to <date>] [--at HH:MM] [--with <title>]...`
   -> relay DEFER_ASK's question + its options line, nothing else.
2. on [옮기기] / yes: same args + `--apply` -> relay the DEFER_CARD text verbatim
   (DEFER_CARD is last; SESSION_NOT_STARTED lines before it are silent bookkeeping).
3. DEFER_REFUSED -> say what it names; never claim a move.
   `SESSION_TRAINED` = the split already holds performed sets: say it was trained, nothing moved;
   closeout (`session-closeout`) is the path, not a move.
4. `SESSION_LINGERS` (exit 2) = moved, but the session row could not be discarded: say the move
   stands and the session is still open; never claim it is cleared.
Never session-abort, never a [정리|그대로] menu, never say "미뤘어요" without the DEFER_CARD.
