# pain.py verbs + store (read when composing a call or reading audit output)

## verbs
```
pain.py add --exercise <slot> --pain <0-10> [--side L|R|both|NA] [--load <kg>]
    [--set-no <n>] [--rir <n>] [--rom setup|descent|bottom|ascent|lockout|other]
    [--fault valgus|knee_forward|shift|twist|round|buttwink|impingement|unknown]
    [--action load_drop|substitute|stop|continue|form_cue] [--session "<split>"]
    [--note "<>"] [--ts "YYYY-MM-DD HH:MM"]
pain.py list [--exercise <slot>] [--days n] [--open]
pain.py recent [--days n]          # open events; no --days = every open event
pain.py show --id <n>
pain.py resolve --id <n> [--guardrail "<>"] [--note "<>"] [--program-change "<>"] [--reopen]
pain.py audit [--window-days 30] [--threshold 3]
```
- only `--exercise` + `--pain` required on add. fill what you know, skip rest.
- `--fault` accepts free text; the listed values are the grouping vocabulary. prefer them.
- `list --exercise` = substring match; `audit` groups by EXACT string. hence slot names only.

## audit output lines
- `FLAG recurring-fault: <ex> x <fault> -> N hits, avg pain X => PROGRAM REVIEW`
  (same exercise x fault >= threshold in window)
- `FLAG recurring-side: <ex> on <side> -> N hits => check L/R imbalance`
- `FLAG rising-pain: <ex> a -> b over N events => PROGRAM REVIEW`
  (>= 3 events, last pain > first pain)
- `NO_FLAGS` / `NO_EVENTS in window` = nothing to raise.
- no recovery flag exists (see program-review.md).

## store
- `data/pain_events.db` (SQLite) beside pain.py, created on first `add`. pack ships
  schema (inside pain.py), never a database. fresh instance = zero events.
- kept out of kit_life.db by design (B-plan). migrate later only if join-with-sets
  analysis is needed (port table + repoint pain.py).
- one row per event: ts, session, exercise, load_kg, set_no, rir, side, pain,
  rom_phase, fault, action, note, guardrail, program_change, status(open|resolved).
