# program edit lane -- volume audit, set-increase suppression, deload

Read BEFORE confirming any program.yaml slot change: R6 revision, safety-row reconcile,
focus-area edit, "add / drop / resize a slot", deload week. First build does not use
this file: program-plan `compose` runs the audit itself (sets held in [3, 5] per slot,
refuses E-VOLUME-FLOOR / E-VOLUME-CEILING, zero questions). Practice rows (roll-down,
bear crawl, get-up) never count in the band: the audit lists them under `practice`.
A LOADED functional move (kettlebell swing, a loaded get-up) counts half
(`muscle_credit`); `practice.<name>.muscle_sets_per_week` is what the band counts.

audit = arithmetic + statements, +0 questions. prompt-enforced, not tool-enforced
(DGN-316 grill r1): nothing stops an edit that skips it. do not skip it.

## volume-audit procedure (DGN-316 6.1/6.2 item 1)

1. DRAFT PATH: never edit the live card for an audit. write the proposal to
   `files/tmp/program-draft-<YYYY-MM-DD>.yaml` (files/tmp daily-clean owns it), audit it:
     service/health/rx-calc --volume-audit files/tmp/program-draft-<date>.yaml \
       <today> database/kit_life.db [<exclude_session_id>]
   live program.yaml changes only on owner confirm.
2. exclude_session_id: today has an OPEN placeholder workouts row (live session) -> pass
   its id (4th arg or stdin key "exclude_session_id"); else nothing. same for every run.
3. exit: 0 verdicts reliable; 1 fatal (fix inputs, no confirm); 3 unmapped lifts ->
   verdicts UNRELIABLE, that lift does not go forward. mapping = pack taxonomy
   (health_taxonomy_seed.sql), shipped as a reviewed seed row, never written at runtime
   (E9; muscle-fatigue ruling 2026-09-26 "종목 생성 시 근육맵 없으면 거부"). propose a
   mapped lift of the same pattern. `service/health/program-plan volume-say --draft
   <file>` names unmapped lifts, exit 2.
4. SET-INCREASE SUPPRESSION (DGN-316 5.2, safety invariant) -- two runs, identical
   <today> + exclude_session_id: CURRENT live program.yaml (no card -> every muscle 0)
   and DRAFT. muscle with draft proposed_weekly_sets > current AND fatigue_state !=
   fresh (loaded AND fatigued both suppress) -> needs explicit owner yes, stated in the
   ONE confirm the turn already has, e.g. "등이 지금 회복이 덜 된 상태인데 세트를 늘리는
   안이에요. 이대로 갈까요?". no extra question.
5. verdicts: floor / ceiling finding on a programmed muscle is FIXED in the draft or
   STATED -- statement = `program-plan volume-say --draft <file>` sentence verbatim
   (E8: verdict tokens + band acronyms are internal; user sees only e.g. "가슴 운동이
   일주일에 N세트라, 흔히 쓰는 최소 기준(M세트)보다 적어요"). quote exit-0 findings only.
   untrained = info, never a violation. non-empty unmapped_actual = history coverage
   hole (step 3). respect insufficient_data / ramp_guard_active (no floor claims on thin
   data).
6. pattern / focus advisory (C16, owner 2026-07-31): read `pattern_balance`.
   same_day_doubling -> note each day stacking >= 2 same compound push / pull slots as
   redundancy CONTEXT, not an auto-trim. hv_imbalance -> plane skew as a design note;
   prefer ADDING the under-trained plane over trimming. advisory, never a block.
7. on confirm: feed the SAME answers to `service/health/program-init write --answers
   @<file> --force` (incl. weekly_frequency, DGN-316 2.5). `--force` = confirmed
   REVISION (first build refuses to overwrite). session_type rows re-derived same call.
   changelog line -> `files/program/program-history.json` `changelog`; touched
   safety_note prose -> its `safety_notes` `<day>.<slot>.<name>` (DGN-773), never
   program.yaml.

source grade (volume bands): floor / target / ceiling (MEV / MAV / MRV) are grade C-D
practitioner anchors (RP landmark heuristics), not graded research; no validated
per-muscle numbers exist (volume-research 2026-07-18 MAJOR GAP; rx-calc GROUP_BANDS_4 /
GROUP_MUSCLE_BANDS comments say so). never "과학이 그렇다" / "연구가 이렇다"; honest
wording = practitioner heuristic, ungraded. the audit's decision procedure (in_band /
below_floor / above_ceiling) stays authoritative -- weak are the numbers, not the gate.

## edit-lane extras

- FOCUS-VS-INJURY RE-RUN (safety invariant): an edit that ADDS or CHANGES a focus area
  re-runs program-plan's `emphasis` stage and its sentence BEFORE volume emphasis. the
  audit is SAFETY-BLIND (no injury field in its schema). recommend protect; "protect"
  drops the emphasis for that area.
- FATIGUE-COST TRIM PRIORITY (C16): over-target -> rank trim candidates by
  per_slot[].fatigue_cost, trim HIGH before LOW (high-cost freeweight / spinal sets cost
  more systemic recovery). never trim a LOW slot on set-count redundancy alone.
- FOCUS-SLOT PROTECTION (C16): before any trim check `focus.focus_conflicts`:
  - `focus_slot_trim_risk` -> slot reinforces a declared focus muscle that carries a
    fatigue signal. pinned decision line: "이 슬롯(<name>)은 <muscle> 포커스 보강
    슬롯이라 트림 후보에서 빼고, 대신 고피로(fatigue_cost=high) 비포커스 슬롯을 먼저
    줄일게요." trim it only on explicit owner override.
  - `focus_above_ceiling` -> rebalance non-focus volume first.
  - a day's focus_slot whose primary muscle is not in focus.focus_muscles -> tell the
    owner the marker may point at the wrong slot.
  - rx-calc only EXPOSES focus_conflicts; the decision line is this skill's; writes stay
    owner-confirmed.
- module state (done@date) unchanged by edits; an edit is not a re-run and never makes
  an offer.
- set floor, micro-anchor lattice, rest: reference/program-rules.md.

## 디로드 / 주기화 (N2, owner 2026-07-28)

hybrid; this skill writes it.
- planned baseline: deload every N weeks; cut phase -> shorter (e.g. 4 weeks, tune by
  measured recovery). periodization axis = week cell (DGN-389), not session count /
  weekday.
- early summon: user self-reports fatigue ("이번 주 좀 빼자", "몸이 안 올라와") -> insert
  before plan.
- one cycle: volume -40-50 % OR lower intensity + wider RIR (pick per lift).
- confirmed instance (owner 2026-07-29): 「디로드 처방: 볼륨 60% 스케일, RIR +2」 --
  default anchor for the next deload week; not hard-coded, re-confirm once when program /
  phase changes.
- no e1RM auto trigger (knowledge mismatch): only plan + self-report.
- deload week edit goes through this audit like any structure change (a cut never trips
  suppression), one confirm.
- basis (PROVISIONAL / own-rule wording): volume-landmarks-015 (grade D),
  doseresponse-007 (B), deficit-volume-016 (D, contested). no "과학이 그렇다".
