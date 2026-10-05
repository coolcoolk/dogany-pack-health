# kit mode (mimics_kit) -- maintainer; read before touching the declaration

```bash
python3 .claude/skills/diet-status/kitmode.py            # verdict
```
- module DECLARES the kit shape it copied (`mimics_kit` in product.yaml) instead of
  REQUIRING a kit. missing kit = standalone, not error. verdicts: linked / standalone /
  mismatch / migratable.
- REPORTS only. nothing refuses on it; install gate is framework pack_install.sh, not
  this module. never describe the declaration as blocking.
- two readers (0.11.0), neither fatal: the card (non-linked -> NOTICE line, card still
  renders) and the suite (test-diet-coaching.py claim M2 re-runs the check against the
  kit checkout, so the next kit bump turns a suite red instead of printing into a void).
- declared `schema_version` = what was COPIED, not what is installed. mismatch -> never
  edit the number to silence it. re-measure the mimic surface (4 tables + 6 vocab tables,
  DDL + seeded rows) against the new kit schema first; bump only after it passes;
  `mimics_kit.verified_against` records which kit. (46 -> 47 was re-verified byte-identical;
  migration 047 touched nothing mimicked.)
- standalone -> linked pour NOT implemented; seam marked in kitmode.py `MIGRATION POINT`.
- carried-in tension: manifest says `requires_kit: kit_life`, so on this delivery path
  `standalone` has no live population. belongs to the `requires_module` grammar question
  (DGN-783), a separate decision.
