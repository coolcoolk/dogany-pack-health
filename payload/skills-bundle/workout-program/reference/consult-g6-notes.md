# G6 notes -- open gaps, provenance (maintainer)

read when: changing the G6 gate, or asked why a cap / floor behaves as it does. the gate
itself (rules the agent runs) = reference/AGENT-CONSULT.md "G6 -- Safety gate"; the
countable limbs (cap / bmr_floor / sex_floor math, conservative per_session_burn=0
branch, `assumed` output) = diet-status calorie_gate.py docstring +
diet-status reference/safety-gate.md. not restated here.

## reconstruction gaps, named rather than filled

- cap is a FIXED ceiling; the row's own note says "not a verified optimum". an
  archetype-dependent cap (lean-mass-preserving vs pace-first) is a candidate with no
  sourcing. until a row says otherwise, one cap for every goal mode.
- `per_session_burn` mining: sources say "history average or kit_life", name no window or
  estimator. pack does not query kit workout history for it; caller passes it when held,
  tool declares the conservative branch otherwise.

## provenance

G6 + ledger one-writer text reconstructed from the framework legacy fragment
`packs/health-trainer/<instance>/AGENT.md.add` (DGN-287-CONSULT-FRAGMENT v2.4) and the instance
copy in force until retirement (`identity/hot.custom.agent.md`, 2026-09-11); they agree
on every rule carried. gaps above = where both were silent; nothing invented.
why the home is AGENT-CONSULT, not AGENT.md (0.11.0): the pack declares no
`agent_md_fragment` / `agent_md_marker` and ships no `AGENT.md.add`, so the old "run the
AGENT.md G6 section verbatim" pointed at nothing (measured on 0.10.0: `grep -rE
'max_deficit_cap|calorie_floor' payload/` -> 0). CHANGELOG 0.11.0,
docs/reports/2026-09-12-g6-gate-home-and-read-mismatch.md.
