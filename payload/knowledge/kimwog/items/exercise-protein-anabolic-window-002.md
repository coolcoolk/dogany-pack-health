---
# Converted from batch1-exercise-nutrition.raw.json finding [10] (protein timing
# worked example, vote 3-0). Rubric: exercise.rubric.md @clinical-physio row
# exercise/protein-anabolic-window-002. Owns the hypertrophy-TIMING claim under
# v3 5 single-ownership; the dose/absorption sibling owns nutrition/ (see alias).
id: exercise/protein-anabolic-window-002
domain: exercise
grade: B
lane: "@clinical-physio"
locale: universal
as_of: 2017
contested: no
sources:
  - "https://www.tandfonline.com/doi/full/10.1186/s12970-017-0177-8"  # ISSN 2017 nutrient-timing stand (batch1 3-0)
  - "Aragon & Schoenfeld nutrient-timing consensus"
  - "framework:GRADE -- RCT-level but scoped, not yet full consensus -> B"
  - "alias:nutrition/protein-intake-002 -- the sibling dose/absorption claim (cross-domain visibility)"
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
claim: >
  The post-exercise anabolic window is WIDE, not narrow: the anabolic effect of
  training lasts at least ~24 hours (muscle stays sensitized to protein), is most
  pronounced in the first 4-6 hours and diminishes thereafter. This refutes the
  older 30-60 minute anabolic-window myth.
reasoning: >
  RCT-level nutrient-timing evidence plus the companion ISSN nutrient-timing
  stand support a wide window; this is the current Aragon/Schoenfeld consensus
  but remains scoped to resistance-trained adults, so it sits at the RCT-level
  pre-consensus band rather than full converged consensus. Total daily protein is
  the stronger hypertrophy predictor -- the window matters far less than the myth
  implied. Cross-domain visibility: the dose/absorption sibling is nutrition-owned
  (alias:nutrition/protein-intake-002); this is the v3 "two distinct claims"
  resolution, not a co-located dual ID.
---

# exercise/protein-anabolic-window-002

The practical takeaway is that missing a narrow post-workout feeding window does
not sacrifice adaptation. Muscle stays sensitized to protein for roughly a day,
with the strongest response in the first few hours. Total daily protein is the
dominant hypertrophy lever, so this claim mostly serves to retire the 30-60
minute myth rather than to prescribe precise timing.

The confidence band is one step below the top: the evidence is RCT-level and the
consensus is current, but it is scoped to trained adults and not yet fully
converged. The dose/absorption side of protein is a separate nutrition-owned
item, cross-referenced here for visibility only.
