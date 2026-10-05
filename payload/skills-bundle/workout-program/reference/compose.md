# THE COMPOSE STEP (model lane)

Read when: program-plan returns a `compose` move (or `sessions` sent changed
sessions back). No user message; answer with `program-plan answer --stage
compose` in the move's `answer` payload shape.

## engine-first

The tool builds a deterministic draft from a data rulebook, not the model:
- order: main -> compounds -> isolations -> core (region blocks, never
  revisit a region).
- main slot guaranteed per session (a compound in the session's main
  pattern).
- region integrity: every lift stays inside the session's assigned regions.
- one in-region unilateral compound when a practice slot is required
  (min 1, cap 1).
- goal practice picks (kit `handoff.practice`; rules as data in
  compose_rank_rules.json `practice_effects`), each one per session:
  - `unilateral`: the practice slot above (`E-UNILATERAL`).
  - `core`: a loaded core lift (`E-CORE-PRACTICE`; a breath/whole-body row
    does not count).
  - `breath_trunk`: slot `breath_trunk` -- a controlled movement, the
    roll-down (`E-BREATH-TRUNK`, exactly one). Pilates is slow controlled
    movement, not a hold: hollow hold does not fill this slot and no other
    slot offers it (`withheld_names`).
  - `whole_body`: slot `whole_body` -- bear crawl, or a light Turkish
    get-up when an open floor is on record; the pick is the get-up's
    technical opt-in; light dose from `practice_dose` (`E-WHOLE-BODY`,
    exactly one).
  - `mobility_flow`: the tool opens every session with a 5-minute flow of
    three drills (world's greatest stretch, cat-cow, ...) before the prep,
    none repeating the prep; drills reaching a caution site go first --
    a warm-up moves the site, never skips it (`E-MOBILITY-FLOW`).
  - `conditioning`: the tool ends every session with a 7-minute interval
    finisher (30 s hard / 30 s easy x 7: bike or rower at a gym, a
    bodyweight interval at home, none loading a caution site), before the
    cardio and cooldown (`E-CONDITIONING`).
  - `power`: right after the prep, before the first lift, one explosive
    move, low dose (3 x 3-5, full rest): box jump at a gym; kettlebell swing
    when a knee/ankle/foot caution rules out landing; med-ball slam only
    with its ball + throwing space on record; squat jump at home without a
    kettlebell. hinge moves avoid back/lower-back/hip cautions; no allowed
    move -> light speed sets (3 x 3, as fast as possible) of the session's
    first lift, which compose already screened; no lift at all ->
    `E-POWER`. the pick is the
    swing/slam's technical opt-in for this block only; the lift pool is
    unchanged.
  - `mixed_circuit`: a 10-minute no-rest circuit after the last lift, light
    load, 40 s per station x rounds (row/bike, kettlebell, bodyweight; home
    and caution fallbacks; never a lift of that session), on 1-2 sessions a
    week (`circuit_sessions`: floor(2 x rotation length / weekly days), at
    least one, spread evenly; `E-MIXED-CIRCUIT`).
  - `conditioning` + `mixed_circuit` (two picks): never stacked -- the
    circuit replaces the interval finisher on its sessions, every other
    session keeps the finisher (`E-END-STACK`); the budget reserves the
    longer one (10 min), not both.
  - legacy `unilateral` / `core` (the kit no longer offers them; a stored
    answer still composes as before).
  breath/whole-body rows appear ONLY in their own slot; flow, power,
  finisher and circuit minutes come out of the lift budget (a short window
  can fail the volume floor: fewer lifts fit). the model never sends these
  blocks -- the tool composes them.
- set cap 4 per lift.
- session lift budget from the time window (compound 12 min / isolation 8
  min + 2 min setup, minus prep/cooldown/cardio; hard cap 7 lifts).
- prep: mobility + activation drills, at most 4 total / 2 per category.
- common-gym lifts only by default; a limited-equipment lift needs the
  matching facility on record.
- the tool doses, holds the weekly volume floor, and refuses what breaks a
  rule -- each refusal is one `E-*<TAB>path<TAB>why` line; fix and resend.

## answer

- default: accept the draft in one step -- `{"accept": true}`. no extra file
  reading, no recomputation.
- edit: pick ONLY from the move's shortlists (validated, mapped lifts usable
  at the recorded place). a name outside a session's shortlist ->
  `E-NOT-A-CANDIDATE`; never map on the spot (mapping = pack taxonomy,
  reviewed seed row, E9). every changed lift needs a short Korean `why`.
- no `candidates` / flat list, no `titles` -- the tool derives session
  titles later (sessions stage) from primary-muscle working sets.
- no numbers (`E-NUMBER-FROM-MODEL`).
- a caution site PREPARES, it does not swap (owner 2026-09-27, restated
  2026-10-04 11:44): keep the lift -- the tool puts the site's prep drills
  (compose_rank_rules `caution_policy.site_prep`) in every session holding a
  lift that uses the site. the ONLY swaps are `caution_policy.substitutions`
  (owner-approved rows; knee: walking lunge -> reverse lunge): the draft
  already carries them (`replaces` + `replaces_display` + `for_site` + `why`);
  any other `replaces` -> `E-SWAP-TABLE`. range/load modifiers (leg press to
  90 degrees, leg extension light 15 reps) are notes the tool attaches, not
  swaps. kept but changed for a site: `for_site` + `why`. extra lift for a
  focus area: `focus`.
- ORDER (owner 17:31, 09-11 rule): execution order, one body region finished
  before the next, never returning inside a session
  (`E-ORDER-BACK-AND-FORTH`).

## per session also send (on edit)

- `prep.<session>`: mat-prep drill keys from `drills` (slot `prep`).
  ACTIVATION CORE (dead bug, pallof press, bird dog, side plank) lives HERE;
  in the lift list -> `E-ACTIVATION-IN-WORK`. loaded core (cable crunch, leg
  raise) stays a lift. each safety site needs a drill preparing it
  (`E-PREP-SITE`).
- `cooldown.<session>`: stretch keys (slot `cooldown`) for what the session
  worked.
- session titles are derived by the tool from primary-muscle working sets;
  never send `titles`.

## names

every name the user reads is a display name. drill names come from the
display layer (ui_labels.PLAN_DRILL_KO), never an internal term ("내전근
프라이머" -> "허벅지 안쪽 깨우기").
