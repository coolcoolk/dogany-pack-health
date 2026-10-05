# goal revision (re-consult) -- DGN-317 v2.4

read when: consult_state=done and the user asks to change a goal, phase, target number
or habit; asks to redo goals wholesale; or engages a weekly-loop transition proposal.
consult_state does NOT change during or after a re-consult. reference/AGENT-CONSULT.md
"Global conduct rules" apply in full.
scope boundary: event-overlay asks with a deadline ("2주만 급하게 빼야 해요") -> overlay
machinery; overlays sit ON TOP of the ladder, a re-consult CHANGES it.
bare goal-setting ask outside a consult -> kit goal-setting SKILL
(reference/consult-goal-part.md "goal-setting entry").

## single-layer revision (default)

- R1: identify the target layer; restate its active row in one line. SoT divergence
  check (config vs ledger; ledger wins, repair + audit -- AGENT-CONSULT "Ledger
  one-writer + SoT").
- R2 cascade, top-down: long changed -> mid and short each re-affirmed (fast-confirm, one
  message each); mid changed -> nutrition constraints re-derived, short re-affirmed only
  if phase-dependent; short changed -> no cascade.
- R3: propose the replacement row (status proposed), citing inputs incl. latest
  measurements; current state stale -> a fresh measurement joins the proposal.
- R4 safety gate: mandatory whenever the mid layer's numbers or phase change. short-layer
  edits skip it ONLY within the frequency backstop (<= 7/week and < 2/day); beyond, the
  gate runs (AGENT-CONSULT "G6 -- Safety gate", G6-c). [SAFETY: frequency backstop = G6
  invariant.]
- R5 on approval (확정): supersede old row, activate new, config mirror per the ordered
  discipline, append ledger_audit kind='ladder_review' detail {"trigger":"user"}.
  CARRY-FORWARD (legacy installs only): a replacement LONG row carries
  `detail.focus_areas` verbatim. since 2026-09-26 focus areas live on the program card
  (`program.yaml focus_areas`); a goal revision does not touch it.
- R6 operationalization delta (consult_modules grammar): approved revision changes
  training days, split, focus areas, measurement cadence or frequency -> AFFECTED modules'
  artifacts re-adjusted INLINE as an EDIT in the same approval sequence (done-module edit
  lane): reconcile program.yaml / routines / guideline per the idempotency rule
  (reference/consult-modules.md), run the DGN-316 volume audit on any program change
  (reference/program-edit.md), keep done@<original-date> UNCHANGED (edit != re-run, never
  an offer). focus area ADDED or CHANGED -> re-run focus-vs-injury (program-plan
  `emphasis`) BEFORE the emphasis applies (volume audit is band arithmetic, safety-blind).
  affected module PENDING / DECLINED -> the revision is a program-need trigger of class (c)
  for it (one offer per bounds; declined diet / supp only if (c) is a new class; declined
  WORKOUT follows the 30-day cooldown, OQ-23(b)). consult_ops never touched.
  DGN-316: weekly review's attendance-drift flag, once the owner engages, enters here (R6
  re-key edits the program inline).

## full re-consult ("목표 처음부터 다시 잡자")

entry = the RESTART RULE batch confirm (reference/consult-conduct.md; OQ-29): ONE message
batch-confirms the whole captured state (ladder, body state, constraints / resources,
completed modules), ONE keep-or-change question; replaces the per-layer walk.
- step 0 = current-ladder snapshot + recent adherence numbers from own DB
  (kit_life-computed) instead of a digest; they ride the batch message.
- unchanged (not rejected) layers: covered, never re-asked. changed / rejected: full step
  at the owning step (priority pin) + reversal cascade. interview staging applies.
- focus / injury restate rides the batch (old S7 combined line subsumed). amendment to
  either half -> each on its own topic. batch covered the safety set -> G6 injuries SLOT
  counts 0; the gate still runs in full.
  confirmed / amended focus set -> program card via program-plan `focus` (proposes the
  areas already on the card first). = staleness loop for weak-point data.
- wrap supersedes all prior active rows, refreshes the config mirror; audit
  kind='ladder_review', detail {"trigger":"user","mode":"full"}. affected modules follow R6.

## system-initiated proposals (weekly loop)

transition proposals (short-success promotion, mid-death demotion, every-Nth
ladder_review) surface in the weekly coaching block; user engages -> single-layer revision
at R3 (proposal formed), R2 cascade still checked before R5. approval / activation rules
identical; why stays user-owned.
