# calorie safety gate (G6 countable half) -- read when calling it or explaining a refusal

```bash
python3 .claude/skills/diet-status/calorie_gate.py \
    --deficit <N> --base-target <N> --bmr <N> [--sex male|female] \
    [--weekly-freq <N>] [--per-session-burn <N>]
# exit 0 pass · 1 refuse · 2 unverifiable
```
(activation path absent -> same file under `.claude/skills-bundle/diet-status/`.)

- conversational half (injuries ask, refusal wording, medical-supervision referral) =
  workout-program reference/AGENT-CONSULT.md "G6 -- Safety gate". one home.
- numbers are NOT in this pack. gate reads two inviolable kit `ledger_constraint` rows
  by key (`max_deficit_cap`, `calorie_floor`), read-only, and checks three limbs: cap,
  BMR-relative floor, sex floor on weekly average effective intake. never copy those
  values anywhere in this repo.
- binds without being asked: card.py `resolve_goal` applies it LAST, after the carry
  (a hoist moves base AND effective target together, burn post-condition holds);
  carryover.py clamps its `aim` the same way and reports `safety_verdict` /
  `safety_floor_applied`.
- `unverifiable` != `pass`. missing row, unreadable DB or uncollected input ->
  unverifiable -> card prints NOTICE, consult refuses to 확정 a calorie number that turn.
- reachable on a fresh instance: both rows are `source='seed'` and nothing in kit_life
  plants them. seeding is the kit's job; this pack refuses to paper over the absence.
