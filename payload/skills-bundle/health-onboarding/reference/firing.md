# how the entry fires (0.17.2) -- three legs, none a Stop-block

Read when: debugging why the entry did or did not fire, or touching the onboarding
hooks. The model needs none of this to run the skill: every leg opens the same way --
step 1, goal-setting's first message with nothing added (no per-leg variant, owner 2026-09-27).

1. INLINE, same message as the identity close: manifest `post_mint_next` (framework
   POST-IDENTITY CONTINUATION CHECK, DGN-1632) runs
   `routines/bundle/domain-onboarding-check.py`; nonempty stdout -> step 1, as the tail of the close.
2. NEXT OWNER MESSAGE: `routines/bundle/domain-onboarding-prompt.py` (UserPromptSubmit).
   ONCE, only on OFFER reason `absent`, zero offers + zero declines, identity marker gone;
   records the offer itself -> step 1 (no "setup finished" line).
3. EVERY LATER SESSION: `routines/bundle/domain-onboarding-check.py` (SessionStart).

`routines/bundle/domain-onboarding-stop.py` stays LOG-ONLY (0.17.1): a Stop-block lands
after the owner saw the reply and duplicates the question.

All three are declared in pack-manifest.json `hooks[]` (pack_install.sh `_hooks_wire` ->
`.claude/settings.local.json`, since 0.16.x). The old "this pack cannot register a hook"
section predates that lane and was deleted (health-onboarding audit H1).
