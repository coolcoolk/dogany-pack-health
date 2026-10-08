---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Converted 2026-09-02 (SKU-knowledge-warehouse-ownership,
# gated-row resolution pass -- see
# worklog/2026-09-02-knowledge-warehouse-ownership.md). Previously blocked:
# locale field was the placeholder "KR-check-US-source", which fails this
# warehouse's locale grammar (lint.py LOCALE_RE) and was an open verification
# task, not a real value. Resolved by checking Korea's own food-safety
# authority (Ministry of Food and Drug Safety / foodsafetykorea.go.kr): its
# official poultry doneness guidance (74C, "meat turns from red to white")
# is functionally identical to the USDA/FDA standard (73.9C/165F) this item
# already cited -- the underlying claim holds under KR regulation, verified
# independently rather than assumed.
# Rubric: cooking.rubric.md @food-safety row cooking/poultry-safe-temp-002.
id: cooking/poultry-safe-temp-002
domain: cooking
grade: A
lane: "@food-safety"
locale: universal
as_of: 2026
contested: no
sources:
  - "https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/safe-temperature-chart"
  - "https://www.foodsafetykorea.go.kr/portal/board/boardDetail.do?menu_no=3120&bbs_no=bbs001&ntctxt_no=21793&menu_grp=MENU_NEW01"
claim: >
  Poultry safe-cooking is an A-grade codified standard: USDA/FDA set poultry
  to 165F/73.9C, verified by measured internal temperature since pathogens
  evade the senses. Korea's food-safety authority (Ministry of Food and Drug
  Safety, via foodsafetykorea.go.kr) independently publishes an equivalent
  guidance value for chicken (74C, "red meat turns white") -- the same
  practical temperature target holds under KR regulation, so this is not a
  US-only figure. Lethality is a species-specific continuum -- poultry
  requires 7.0 log10 reduction vs beef's 6.5, so a beef temperature table
  undercooks poultry by roughly 4 logs.
reasoning: >
  USDA FSIS safe-temperature chart (US federal standard) plus Korea's
  foodsafetykorea.go.kr / MFDS official cooking-temperature guidance,
  cross-checked directly on 2026-09-02: both set the poultry doneness
  threshold at essentially the same value (73.9C vs 74C -- a 0.1C difference,
  i.e. the same practical target reached via independent US/KR regulatory
  processes). The locale gate this item previously failed is resolved: this
  is not a US-only figure requiring a KR disclaimer, it is a value two
  independent food-safety authorities converge on. Hard-safety: assert with
  disclosure; do not use a beef table for poultry regardless of jurisdiction.
---

# cooking/poultry-safe-temp-002

Poultry needs to reach a measured internal temperature before it's safe to
eat -- looks and juice color are not reliable indicators, since the
pathogens of concern (Salmonella, Campylobacter) are killed by heat but not
visibly signaled by doneness cues. The USDA/FDA standard is 165F (73.9C).

This item was previously held back pending a Korea-jurisdiction check, since
the source was purely a US federal standard. That check is now done: Korea's
own Ministry of Food and Drug Safety (via the official foodsafetykorea.go.kr
portal) publishes essentially the same guidance for chicken -- done at 74C,
described as the point where the meat turns from red to white throughout.
The two figures (73.9C US, 74C KR) are the same practical cooking target
reached independently by two different countries' food-safety regulators, so
this claim is shipped as a universal standard rather than a US-locale-only
one.

One safety note carried over unchanged: poultry's target temperature is
higher than a general "meat" table because the pathogen-lethality math is
species-specific (poultry needs a larger log-reduction than beef) -- don't
substitute a beef doneness chart for poultry.
