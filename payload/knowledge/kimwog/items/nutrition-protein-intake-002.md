---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119.
# Converted from batch1-exercise-nutrition.raw.json finding [9] (protein dose
# worked example, vote 3-0). Rubric: nutrition.rubric.md @obs-inferential row
# nutrition/protein-intake-002. This item OWNS the dose/absorption claim (v3 5
# single-ownership: protein-dose-absorption = nutrition evidence base). Its
# hypertrophy-timing sibling (the anabolic window) owns exercise/ -- see
# source:exercise/protein-anabolic-window-002 (two distinct claims, not a dual ID).
id: nutrition/protein-intake-002
domain: nutrition
grade: A
lane: "@obs-inferential"      # optional on a single-lane domain; kept for clarity.
locale: universal
as_of: 2017
contested: no
sources:
  - "https://www.tandfonline.com/doi/full/10.1186/s12970-017-0177-8"  # ISSN 2017 protein stand (batch1 3-0)
  - "ACSM/AND/DC joint position stand (~1.2-2.0 g/kg/day)"            # independent corroboration
  - "IOM Acceptable Macronutrient Distribution Range (protein)"       # independent corroboration
  - "MacNaughton 2016 -- per-meal MPS refinement inside the range"
  - "framework:GRADE spine -- converged multi-body corroboration, no credible dispute"
applicability:
  axes:
    - key: body_weight_kg     # kit_life-measured axis, used as a scaling input.
      type: numeric
      role: scale
      unknown_policy: ask
      rescale:                # per-unit range refract.py multiplies by the
        per_unit_low: 1.4     # user's measured weight (RESCALE op). The model
        per_unit_high: 2.0    # never computes this -- data drives the number.
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      Total daily protein scales with body weight (1.4-2.0 g/kg/day). RESCALE
      from the user's measured weight rather than quoting fixed grams. The
      higher 2.3-3.1 g/kg band applies only for hypocaloric lean-mass retention.
    grade: A
claim: >
  Total daily protein intake of ~1.4-2.0 g/kg/day is sufficient for most
  exercising adults; the per-meal muscle-protein-synthesis response is maximized
  at ~0.25 g/kg body weight, or an absolute 20-40 g, per meal.
reasoning: >
  The ISSN 2017 protein stand aligns with the joint ACSM/AND/DC position
  (~1.2-2.0 g/kg/day) and the IOM Acceptable Macronutrient Distribution Range;
  no credible body disputes the intake range, and MacNaughton 2016 refines the
  per-meal figure inside it. Convergence across independent institutional bodies
  with no dispute reaches the top confidence band on the GRADE spine. This is the
  dose/absorption claim (nutrition-owned); the timing/anabolic-window claim is a
  separate exercise-owned item.
---

# nutrition/protein-intake-002

The daily-intake range and the per-meal dose are the two load-bearing numbers.
Both are corroborated across independent institutional bodies with no credible
dispute, so the claim sits at the top of the confidence ladder.

The daily figure scales with the user's body weight; the answer path RESCALES
from a measured weight rather than reciting the fixed grams. The higher
2.3-3.1 g/kg band is a narrow carve-out for lean-mass retention during a caloric
deficit, not a general recommendation. Protein timing (the anabolic window) is a
separate, exercise-owned claim and is deliberately not decided here.
