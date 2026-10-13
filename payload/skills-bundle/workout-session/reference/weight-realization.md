# weight realization, loading units, plate cues, stack learning
read before showing a working-set weight, when a weight is (잠정), when ax-project exits
non-zero, or when the user says a weight does not exist on a machine.

## realized working weight (code: `service/health/ax-project serve`)
never show rx-calc's slot weight directly; realize it first:
```
service/health/ax-project serve --session <rotation_day> --slot <slot_num> \
    --target <rx_weight_kg> --json
```
- `<rotation_day>` from rx-calc (앞A / 앞B / 뒷A / 뒷B).
- `<slot_num>` = 1-based position after rx-calc sorts by program.yaml `priority`
  (== program.yaml slot == us_step seq). find by exercise name, never hard-code (a
  reorder changes numbers). rule home: workout-program "슬롯 우선순위".
  the us_step rows serve reads are derived from the card by program-init (same call
  as the card write) and re-synced at every session-open (`us_step=` on the OPENED
  line). exit 1 "no working us_step" for a slot = that lift has no catalog row yet
  (`USSTEP unresolved`); run `service/health/program-init sync` after it is registered.
- `<rx_weight_kg>` = rx-calc's slot weight.

exit codes:
| code | meaning | do |
|---|---|---|
| 0 | realized | use `realized_value` |
| 2 | JIT gate (machine unregistered / incomplete) | "stack learning" below |
| 3 | install incomplete: pack taxonomy seed never ran on this DB | below |
| 1 | other (args / no exercise / DB) | read the message, judge |

exit 3 (setup defect, not the user's):
1. never invent weight / grid / warmup ramp; never pass rx-calc's raw value off as
   realized (the silent pre-fix behaviour). continue; weight undecided; record what the
   user actually lifts.
2. one line, no internal words (ax-project / ax_projection_rule / 시드 / exit 3):
   "설치가 한 단계 덜 끝나 있어요. 무게 반올림/램프 규칙 데이터가 아직 안 들어가서, 지금은
   제가 무게를 확정해 드릴 수 없어요."
3. with consent run the command stderr printed:
   `python3 service/health/health_taxonomy_seed.py --db database/kit_life.db --apply`
   (idempotent; a second run inserts 0 rows).
4. verify `... --check` exit 0, then re-run the same `serve`.
`session-open` reports the same state at birth (`taxonomy=` / `install=` / `INSTALL-GAP`,
also prep.yaml / stretch-matrix.md / gym-layout.md / session_type rows; full table in
workout-program "설치 완결"). seen there -> do step 3 now.

JSON: `realized_value` (show this) · `provisional` 0|1 · `gate_needs` · `exercise_name` ·
`warmup` ordered steps (empty = none) · `equipment` (internal, never shown) · `tempo`
(machine / SAFE lifts only: `{raw, concentric_s, pause_top_s, eccentric_s, pause_bottom_s}`).

rules:
- shown working weight = `realized_value` always (registered machine: same as rx-calc).
- `provisional == 1` -> "(잠정)" after the weight + one line under it: estimate until the
  machine is fully known, go with the real weight, tell me if you used another. never
  block or wait. "(잠정)" is the only visible signal.
- `warmup` empty (stack / cable) -> straight to working, and do not announce "no warmup".
- `warmup` items -> one step at a time before the working weight (reference/
  warmup-stretch.md). keyboards for rungs come from code (reference/set-recording.md);
  author a single done `[[OPTIONS]]` only for a step no code keyboard covers.
  `provisional` does not suppress warmup; "(잠정)" only on the working weight.
- render per item, from its fields only (never compute / round / % estimate):
  `render == "ramp_set"`: `rung == "empty_bar"` -> "빈 봉" (empty bar / smith bar); else
  weight = `weight_kg`. cue = weight + target reps + RIR (#9): "40kg x8 (RIR 4+)",
  "빈 봉 x8 (RIR 4+)". reps = item `reps`, RIR = item `rir` (always present on ramp sets,
  same taper as the table; reps fall as weight rises). other seeded prep / warmup items ->
  `line` (else `cue`) verbatim.
- tempo (F18, machine SAFE lifts): field present -> add a tempo instruction to the
  working cue; absent -> never invent one. 4 digits = 당김 / 유지 / 신장 / 정지 seconds:
  "2140 템포: 당김 2초, 유지 1초, 신장 4초 천천히" (0s phases may drop). non-4-digit raw ->
  show raw only. tempo is an alternative lever to weight on machines.
- field names (warmup / render / rung / weight_kg / tempo / concentric_s ...) and CLI
  names never reach the user.

## stack learning / machine designation (F20, on demand)
weight comes out (잠정) (stack unknown) or the user says the weight does not exist on the
machine -> learn the stack there. never block.
1. only if the lift has 2+ physical machines: confirm which.
2. ask in plain words (#12): no base / step / "시작 무게" / "한 칸 간격". two options:
   stack marks ("5, 10, 15 ...") or one photo (read the marks yourself). `JIT_CALIBRATION
   ask=` present -> use it verbatim. non-uniform stack -> only the band in use.
3. register: `service/health/ax-jit register-machine --label <label> --lattice-base <b>
   --lattice-step <s>` (cable lifts: `--cable-lines single|dual` too, else stays provisional).
4. re-run the same `ax-project serve`.
known gap (engine): no per-session machine switch when a lift has two machines; serve
reads only the DB-bound machine. work around by hand, log as improvement.

## loading unit (#27)
read rx-calc `loading` (or `ax_machine.loading_side`, the SoT) and state the unit up front:
- `per_side` -> "한쪽당 {N}kg", never converted to total. `total` / `single` -> total.
  `stack` -> pin weight.
- warmups / ramps in the same unit. no tag or provisional machine -> never guess; confirm
  per-side vs total once, store (JIT), auto after.
- set-table header labels are deterministic from the tag (`(한쪽당)` / `(총)` / `(스택)`, none
  when untagged); trust them.
- weights verbatim with decimals (21.25kg, 34.38kg) in push and chat. never round.

## plate cue (G10, #39-B)
placement: plate guidance lives in the SET CUE, not the table. the `[원판] 양쪽당 껴야 하는
무게` block under the table is 폐기·제거됨; never re-add a plate line to the table.
format -- kg per side, never plate counts (a wrong count is worse than honest kg). the
code prints only three shapes, all prefixed `[원판] `:
- absolute (first cued set of the lift): `[원판] 바 20kg + 양쪽 55kg`
- add: `[원판] 양쪽에 2.5kg씩 더` · remove: `[원판] 양쪽에서 2.5kg씩 빼기`
frequency (owner 2026-08-21 15:32): 변경시만, 델타. same weight as the last cued set -> no
line at all (no "same weight" line either). changed -> per-side delta. first cued set ->
absolute. line absent also when: not bar + plate, weight undecided, at or below the bar.
bar-less lifts (machine / stack / cable / bodyweight / fixed dumbbell `lattice.type: even`)
never get one. set-start push (set-arm) attaches it; model never recomputes or retypes it,
only supplements in the same format if needed.

원장 (ledger) rule (A3 D6, 2026-08-25): the last cued weight is remembered per (session,
lift) in the `.plate-cue` ledger, and rungs count. before D6 rungs never entered the
ledger, so every first working set degraded to an absolute load right after the user had
ramped up. now:
- only the ladder's first rung is absolute; rung -> rung and rung -> first working set are
  deltas; working -> working at the same weight is silent.
- rung deltas come precomputed in `set-table.planned_ramp_rows` `plate_delta` (carried
  with `plate_prev_kg` through `set-arm.resolve_ramp_ladder` -> `due_rung` ->
  `derive_next_spec` -> `plate_cue_line`). the plan is used only when `plate_prev_kg`
  equals the ledger; otherwise the ledger (what is really on the bar) wins.
- working sets have no `plate_delta`; only there `plate_cue_line` computes its own.
- ledger updates only when a line actually went out; an unsent cue never counts. missing
  record -> next cue degrades to absolute (duplicate, never wrong).
code: `service/health/set-arm` (`plate_cue_line`, `PLATE_CUE_FMT` / `PLATE_CUE_ADD_FMT` /
`PLATE_CUE_DROP_FMT`), `service/health/ax_engine.py` (`plate_breakdown`: per side =
(total - bar) / 2). open owner decision: kg per side vs plate counts (code = kg per side);
if reversed, edit this section and the formats together.
