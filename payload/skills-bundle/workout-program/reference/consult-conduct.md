# consult conduct -- restart / resume, question budget, record-first fields, planning inputs

read when: restart / redo / resume / full re-consult; before mining a field for a
fast-confirm; auditing the question count; any meal / workout PLAN or DESIGN branch.
hard rules (pacing, one topic, consume-ahead, record-first, intent carve-out) stay in
reference/AGENT-CONSULT.md "Global conduct rules". this file = their long bodies.

## restart rule (NORMATIVE -- DGN-317 section 6; OQ-29 owner-confirmed)

applies to: (a) user-requested restart / redo of consult or onboarding, mid-flight or
after completion; (b) interview resume after interruption; (c) full re-consult entry.

CAPTURED = everything persisted in own stores from prior consult / module elicitation:
staged (proposed, source='interview') + active ledger_goal rows incl. detail keys (split;
legacy focus_areas / tradeoff_priority on old installs); user's strands + order pick
(metric_axis origin='user', phase_order); program.yaml focus_areas; program-plan state
(files/program/.program-plan.json); ledger_constraint rows (safety, nutrition, time);
ledger_resource + ledger_preference rows; config profile + mirror keys; program.yaml;
module done states. answer never written = not captured.

PROCEDURE: open with ONE summary message batch-fast-confirming ALL captured answers --
compact grouped restatement (goal ladder: 3 lines; body state: profile + injuries + focus
areas; constraints / resources: schedule, venue, supplements; completed modules), target
<= ~12 lines -- ending with ONE question: keep everything, or name items to change.
pinned exemplar closing line (OQ-26):
  "여기까지가 지금 잡혀 있는 내용이에요. 이대로 갈까요, 아니면 바꿀
  항목만 짚어주세요."
counts 1 decision question.

PRIORITY PIN: items the owner REJECTS (incl. full-batch reject) re-open in FULL step form
at the owning step -- may be an open ask -- with reversal cascade on dependents (top-down
re-affirm). "re-asking a captured answer as an open question = spec violation" applies
ONLY to fields NOT rejected. record-first still applies inside a rejected re-run where
the captured value plausibly survives. not-rejected items: never re-asked. G6 runs in
full on every restart path.
FULL RE-INTERVIEW FORBIDDEN: even explicit "from scratch" routes through the batch
confirm first; wholesale redo only if the owner rejects the whole batch -- then the
spine re-runs under the priority pin.

resume specifics (interrupted interview): reference/AGENT-CONSULT.md "Pre-flight" resume.

## spine question budget (DGN-317 section 7; OQ-27 owner-confirmed 2026-07-15)

supersedes the TWO-BAND 12/15+3 pin.
budget: typical <= ~7 decision questions / HARD CAP 11.
ledger: G0 consent 0-1 / G1-pre XOR G3 stats 0-1 / G1 1 / G2 1 / G2 explicit-confirm
restore 0-1 / G3 1 / G3 measure-first 0-1 / G4 1 / G5 1 / G6 1 / G7 1.

measurables walk -- OUTSIDE this band (owner correction 2026-08-23: the
problem is not the number of questions but asking several at once; the
session runs linearly). G2/G3/G4 goal-interview walk paid in its own band, not
counted against the spine cap: constraint = one question per turn, not COUNT. band:
<= 4 asks per staged layer (verb cannot emit more); an ask landing as CONFIRM off a record
counts 1. never drop a measurable question to protect the budget (dropped question = the
NULL-column defect back).

counting: every user-decision ask counts; fast-confirm 1; statements / echoes / mining 0.
restart batch confirm = 1, own unit row; restart audit SUMS it with re-run slots against
the SPINE cap (full-batch-reject worst = 11 = cap; audited restart > 11 = spec
deviation). module questions paid in the MODULE's own band (reference/consult-modules.md);
bands never pool.

## record-first derivable fields (DGN-317 section 5)

mining order: (1) records -- meals, workouts, workout_sets, metric_log, food_cache;
(2) ledger quadrant rows (all four); (3) config keys; (4) files -- program.yaml,
guideline, stored reports; (5) prior confirmed answers (staged / active interview rows).
mining reads cost 0; the fast-confirm counts 1.
enumerated: training venue (equipment / machine names in history imply a gym); training
window + days (logged timestamps / notes + ledger_constraint class='time'); weekly
frequency (sessions per week in history); meal repertoire (meals 30-60d at N>=3); body
stats + profile (config, metric_log, InBody reports); supplement stack
(supplement-classified meals + ledger_resource kind='supplement'); goal / phase on
re-entry (active ledger rows + config mirror) -- FACT fields only; intent is never mined.
general: any field with a queryable home = record-first by default. record-first governs
HOW a needed question is asked, never WHETHER (scope wall + accrual-only preference rule
untouched). fields REJECTED in a restart batch re-open in full step form (priority pin).

## consume-ahead classes

pre-answered later step (weekly frequency, injury, weak body part during G1):
- QUADRANT facts (resource / constraint / preference) -> write now to their quadrant.
- MEASUREMENT facts (stated or report-extracted body values) -> current-state, write now
  (kit `inbody-capture` / config-set).
- GOAL-LAYER facts (phase wishes, targets, habit frequency) -> held in conversation;
  staged only at that layer's 확정.
- focus areas -> held like goal-layer facts; land on the program card at program-plan's
  `focus` stage (fast-confirmed, not re-asked).
- injuries -> quadrant facts (safety rows, written now); fast-confirmed at G6.
strict step ORDER unchanged; only redundant re-asking is removed.

## planning inputs (A1) + resource pre-check wall (A6)

plan sound only on: goal ladder + measured current state + resources / constraints = the
four ledger quadrants (ledger_goal / ledger_constraint / ledger_resource /
ledger_preference).
- current state = baseline profile + recent records (what pre-flight queries find) + a
  current measurement. segmental InBody on file = part of it (refines as-is,
  reference/consult-phase-numbers.md A8). no recent measurement -> scheduling the
  start-point measurement is part of the plan; numbers before it = provisional, say so.
- resources / constraints: "자원·취향은 안 물어요" = GOAL INTERVIEW ONLY. ask only what the
  CURRENT layer needs, one topic each: venue / equipment before a split (program-plan
  `place`); physique focus at program-plan `focus`; injuries at G6 before the gate. focus
  + injuries = the two BODY-STATE asks, each at its consumer's doorstep, never fused.
  venue = RESOURCE ask (ledger_resource kind='env'). injuries double duty: G6 input AND
  program design (substitution at compose, marked in the sessions list); served once from
  the G6 slot. any surfaced resource / constraint -> record to its quadrant immediately.
- plans cite inputs: mid / short layers or routines name the current-state numbers and
  resources / constraints they rest on (focus areas + injury substitutions included).
- A6 wall: any meal / workout PLAN or DESIGN branch REQUIRES resource pre-check: mine own
  records first (repeated foods ~30-60 days = repertoire; food_cache; workout history for
  practiced splits / lifts); build from those. item with no history is NOT prescribable as
  default -> ONE compact availability question, or offer it as optional beside a
  history-grounded default. fresh path, mining empty for a class -> the ONE availability
  question is the default; answers accrue to ledger_resource. gear / venue look-up order:
  workout-program reference/resource-ask-gate.md.
