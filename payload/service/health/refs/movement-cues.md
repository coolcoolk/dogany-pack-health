# Movement instructions and optional activation

`movement_cues.json` holds explicit ko/en steps, repetition definitions and one common fault for lifts and remaining catalog movements. `prep_cues.json` remains the source for the existing drills (including warehouse 741's count units). `movement_cues.cue()` reads both; an absent translation is absent, not silently replaced with Korean. The i18n bundles remain string-only for kit compatibility; ordered steps stay in these structured data files.

Main-lift instructions were adapted from warehouse `exercise/main-lift-cues-746` (knowledge commit `7fa78c4`, published in `af8515f`). Cue wording is grade D; `basis_grade` preserves the source row's supporting evidence grade without presenting coaching wording as a tested intervention. Variant instructions are explicit product adaptations of those families and `movement_catalog` technique references. They are not injury-prevention claims. Warehouse 741's existing drill definitions are unchanged.

The execution prompt carries the steps and fault inside the keyboard message. Prep sends the item number, name/dose and completion button together. The overview card remains compact. Cooldown start/done prompts use the same data. User-recorded prep/cooldown steps and fault override pack defaults.

## Activation configuration

Activation defaults OFF. To record a preference, include this in the input to `program-init write` (the writer preserves and validates these fields):

```yaml
activation_primers: true
activation_drills:
  horizontal_push: [plate_pullover, dumbbell_fly_pattern]
```

A slot can override `activation_primers` and carry its own `activation_drills` list of one or two codes or drill objects. Objects can retain `load_kg`, `implement`, `steps`, `fault`, `target_reps`, `target_unit` and `hold_sec`. Do not invent a load. `caution_prep: true` on a slot selects shoulder/knee preparation when no recorded menu replaces it. Existing slot-bound drills (including K4) replace defaults. `skip_optional_prep: true` omits generated optional drills.

The mechanism shares G19's free-weight equipment and compound-pattern definitions. Recorded machine primers remain valid user data. Generated drills are one light set, at least five reps in reserve, before the lift's ramp; a repeated pattern does not generate another primer. Legacy immediate primers are projected into this same before-ramp sequence, retaining their recorded dose. `activation_rules.json` names warehouse 731, the menu and dose limits. These are product rules, not measured effectiveness claims.

The historical 0.5-bodyweight proposal is stored as `owner_confirmed: false`, `enforced: false`. Preference/caution is the final owner-approved switch; load alone never enables extra preparation. Do not turn the historical proposal into a gate without resolving that decision.

## Record/undo contract

Setup/ramp rows use the emitted `RUNG_SET_CMD`; prep rows use the emitted `PREP_SET_CMD`/`PREP_TAP_CMD`. Do not reconstruct the positional arguments. `set-add` already checks sequence/kind consistency and planned working completion. Delayed transition delivery now checks completion again after waiting.

`set-undo` keeps the user's load override, cancels obsolete arms, posts a correction, and refreshes the progress surfaces. Prep/setup/ramp storage sequences and null completion taps are rendered as owner labels, never `None`, negative set numbers or “no weight”. Surface delivery errors remain explicit and do not falsify the committed record operation.
