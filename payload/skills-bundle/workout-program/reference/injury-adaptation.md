# injury-driven program adaptation 라이프사이클 (any site, C-new2 2026-08-02)

Read when: pain-triage raised an escalation flag or a recovery-candidate, a single
pain event hit a loaded joint during working sets, an injury was re-diagnosed, or a
program change touches an injury-flagged slot. Detect / judge / propose = pain-triage
(pain-triage reference/program-review.md); this file = the action catalog + program.yaml apply.

## steps

1. onset (new / worse): trigger = pain-triage escalation flag (recurring-fault /
   recurring-side / rising-pain). find lifts loading the site -> adjustment
   {substitute | load-cap | ROM-cap | tempo} + primer-prep drill -> safety_note tag ->
   anchor in injury / safety ledger.
1a. first-occurrence review: all three flags need recurrence, so a mild one-off pain
   raises nothing. trigger = ONE pain event on a loaded joint axis; no recurrence, no
   intensity floor (2/10 fires), reported during a working set of a lift loading that
   joint. output = CANDIDATE, never auto-apply: propose at POST_SESSION, only approved
   goes into program.yaml. approved -> same as onset. rejected -> ledger "관찰됨, 조치
   없음" (never ask twice for one event). silence is not an option.
1b. pattern-spread candidates (2026-08-23): once a lift is confirmed pain-loading (1 or
   1a), raise program.yaml slots sharing its `exercise_pattern` (closed vocab: squat /
   hinge / horizontal_push / vertical_push / horizontal_pull / vertical_pull / core /
   isolation). then narrow by joint axis + mechanism: same pattern, different axis ->
   not a candidate (pattern match = eligibility, not evidence). propose weakest form
   first: primer-prep > tempo / cue > ROM-cap > load-cap > substitute. never open with
   substitute on a not-yet-painful lift. one-axis one-step: never apply candidates
   together.
2. reassess (site / mechanism corrected): re-check existing adjustments against the new
   mechanism -> fix primer direction / cues only, not a redesign. a decision built on the
   old mechanism flips with it.
3. recovery (ACTIVE roll-back): pain-triage flags recovery-candidate -> propose at
   POST_SESSION only -> on approval apply ONE-AXIS ONE-STEP probe {load up | ROM-cap up |
   primer reduce} -> workout-session verifies in-session -> pain-free: step stays;
   pain back: revert same session.

## discipline

- recovery indicator = pain-triage's (primary pain-absence streak pain<=2, default K=3
  sessions or N weeks, no down / stop action; secondary load tolerance up +
  primer-dependence down). self-report + log PROXY, never tissue recovery: gradual,
  conditional, no overselling.
- rules: one-axis one-step, revert-on-recurrence, approval-required (one writer),
  injury / safety ledger = SoT (safety_note = mirror), exposed ONLY at POST_SESSION
  (no push, no morning brief).
- 1a / 1b = proposal only (NON-NEGOTIABLE). no silent apply path; nothing written to
  program.yaml / prep.yaml without approval.
- candidate rhythm = linear, workout-session reference/pacing.md (F23 is the single
  home): 3+ candidates -> one overview list, then ONE per turn; 1-2 -> one by one, no
  list. never 2+ decision questions in one message (2026-08-23). never drop candidates
  to cut questions -- cut questions per message, not candidates.

## worked example -- 1a + 1b path (schematic)

one-off mild medial pain mid-set on a unilateral knee-flexion lift <LIFT_A>; no flag
fires (old output: silence). 1a -> <LIFT_A> becomes a candidate. 1b -> same pattern
`squat` slots <LIFT_B> / <LIFT_C>, narrowed to the medial knee-flexion axis; both
already carry the primer -> spread reads backwards: <LIFT_A> was the hole. owner
approves primer on <LIFT_A> (one candidate -> no overview). apply weakest form only:
declare in prep.yaml `days.<DAY>` beside the existing primer declarations (binding =
lift, not slot number; no engine special case). it took 7 days and a human reading
notes to surface; 1a exists to remove that gap.

## injury_knee rehab prep principles + source grade (C-new, 2026-08-02)

worked example of ONE site; keep, reference only.
- knee-flexion session prep layers along the load path: ankle (K6 dorsiflexion) ->
  hip adduction / abduction (K2 / K4 / K5) -> knee-flexion compound. model: ankle
  mobility limit is an upstream cause of medial knee collapse (2018 Phys Ther Sport
  meta-analysis, video citation).
- leg-extension family managed by knee angle band: 0-45 deg first (less pain), recline
  the backrest for upper quad, align knee axis. (a leg press would own 45-90 deg; not in
  the current program, V-squat / BSS cover it.)
- ground feel: thin-sole / barefoot style for squat-pattern slots (keeps load off the
  knee). gear tip, not structure.
- source grade (important): (a) owner live feedback = own-rule, (b) the coaching videos
  = mechanically coherent model, NOT medical fact, (c) warehouse-graded evidence --
  keep apart. never "과학이 그렇다" in program / coaching text.
- source videos: 03clUJqwkW8, h0NmtiByMEo (2026-07-22, applied 2026-08-02). concrete
  drills / placement live in prep.yaml; their prose (K6, common setup, leg-ext cues) in
  files/program/stretch-matrix.md.

## 부상 부위 x 워밍업 매트릭스

primer call for a slot with an injured site. three branches, opposite directions --
never merge.

    무릎 재활 슬롯               맨몸 프라이머를 무게 워밍업 전에 반드시 먼저
    단관절 머신 + 부상부위        맨몸 프라이머 스킵, 가벼운 워밍업 무게로 바로 시작하되
                                 부상 부위 반응 체크
    다관절 프리웨이트 + 부상부위  맨몸 프라이머 필수

workout-session reference/warmup-stretch.md states bw-first for compounds in general;
these three are narrower (injury axis present). no carrier: read at design time and
encode into the slot.
