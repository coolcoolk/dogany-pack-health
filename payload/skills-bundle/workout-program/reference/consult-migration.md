# consult migration path -- digest, pre-ready, mis-seed, G0 lead, G1-pre

read when: pre-flight sets `entry_path = migration` (reference/AGENT-CONSULT.md "Entry
paths + state machine"), or consult_state is pending_data / digesting. fresh path
(health-onboarding, new instance) never reads this file.

## state + mis-seed

- migration path states: `pending_data -> digesting -> ready -> done`.
- mis-seed self-heal: consult_state=pending_data with ZERO migration traces AND
  config/agent.conf HANDOFF_PEER_AG unset -> config-set consult_state=ready, proceed as
  fresh. HANDOFF_PEER_AG set -> pending_data with zero traces is a legitimate
  pre-migration state: keep the deferral ("정리 끝나면 상담 제안
  드릴게요.").
- pre-ready (pending_data / digesting): normal logging / query service only; defer
  ladder / program talk with one line. digest job sets ready -> ONE proactive consult
  offer push (V3-registered trigger, 1/day budget).

## digest read (pre-flight, migration only)

- READ the latest files/consult/digest-YYYY-MM-DD.md AND ledger_goal WHERE
  status='proposed' (source='migration-digest').
- staleness: digest older than 7 days OR records added after it -> re-verify each finding
  against own DB; drop or restate any falsified finding.
- consult_state=ready but NO digest: say so plainly, offer to analyze records now.
  accepted -> run the analysis inline (kit_life-computed numbers only), treat its output as
  the digest, continue on the MIGRATION branch.
- digest content contract: every derived number from kit_life CLI; daily calorie verdicts
  use per-day effective target = base target + that day's burn
  (`kit_life.sh targets --burn <that day's burn kcal>`). never repeat the fixed-base
  comparison error even if a stale digest carries it.

## G0 migration lead

lead with the strongest digest findings: at most 2, one line each, numbers included,
staleness-verified. consent slot rules: reference/consult-goal-part.md "G0 consent slot".

## G1-pre -- baseline profile completeness (A8; migration only)

present what EXISTS as a compact one-line snapshot to confirm (e.g.
"키 OOO / 체중 OO.O / 체지방 OO.O% InBody M/D") -- carried-over data confirmed, never
silently assumed. corrected value -> config-set immediately. sex or birth_year missing ->
ask ONLY the missing fields in ONE compact question:
  database/kit_life.sh config-set sex=<male|female> birth_year=<YYYY>
why: BMR math is lean-mass-based and runs without them, but coaching judgment (protein
/kg, deficit margins, expectations) uses both -- collect regardless.
fresh path: skipped; body state comes through the move loop (`ask_baseline`: InBody photo
or height + weight).

## G3 migration numbers

migrated config (goal_mode / deficit_kcal / protein_g) = mid-layer evidence only:
presented at G3 as carried-over starting values (reference/consult-phase-numbers.md),
never the consult's purpose or opening agenda, never as already-current commitments.
