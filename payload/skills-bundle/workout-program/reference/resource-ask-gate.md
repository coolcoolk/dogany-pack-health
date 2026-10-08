# 자원 ASK-GATE -- look up before asking; never re-ask a known value (2026-08-24)

Read when: about to ask the user about something they own / carry / have access to
(gear, straps, belt, venue equipment). rule 2026-08-22 + correction 2026-08-24:
re-asking a value already on record is a defect, not data collection.

## rule (no exceptions)

check the two stores below BEFORE asking:
- KNOWN -> do not ask; use it. `possession='has_not'` is KNOWN ("asked, does not have"
  != "never asked"; re-asking it was the original incident).
- UNKNOWN -> not "no", not "unused". never paper over with a default (silent default =
  assumes "does not use").
- trace only in memory prose -> not a value (search noise is real: homonyms). need it ->
  ask a CONFIRM question, not an open one, and record the answer on the spot.
- no code reads the value today -> do not ask (e.g. knee sleeve / lifting shoes: zero
  code paths change a number). user volunteers it -> record only.

## carrier -- honest state

- LOOKUP half has a carrier: `carry-list` (kit table `carry_item`, migration 053,
  kit_life 2.24.0). read / write `carry-list` / `carry-add` / `carry-upd`. containment
  via `parent_id`; container rows `item_kind='container'`. possession 3-state
  `has|has_not|unknown`.
- BLOCK half has NO carrier: no hook or gate script checks outgoing messages. the
  scripts the old text named do not exist (measured 2026-09-15; test-carrier-claims.py
  pins them as absent). this skill text is the only guard. building them = behaviour
  change, separate decision.
- fixed venue equipment = `ax_machine` (boundary unchanged). venue itself
  (`ledger_resource kind='env'`) still has NO CLI verb -- do not imply the venue half is
  solved.
- usage policy (which lift uses a strap) stays module-side (G19 / program.yaml slots),
  not kit. design basis: design notes 2026-08-24 owner-resource-inventory-DESIGN (its
  `detail` JSON model has no column in `carry_item`).
