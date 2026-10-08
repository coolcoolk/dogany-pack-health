---
# Converted from batch1-exercise-nutrition.raw.json finding [3] (tool instability,
# vote 3-0). Rubric: nutrition.rubric.md @obs-inferential row
# nutrition/tool-instability-005. Anchors the GRADE-vs-NutriGrade disclosure rule.
id: nutrition/tool-instability-005
domain: nutrition
grade: A (field-methodology)
lane: "@obs-inferential"
locale: universal
as_of: 2021-2023
contested: no
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC8168365/"  # GRADE vs NutriGrade ~53% agreement (batch1 3-0)
  - "framework:GRADE and NutriGrade -- the two tools whose disagreement this item quantifies"
claim: >
  The choice of grading tool materially changes the verdict for the same
  nutrition evidence: NutriGrade rated red/processed-meat observational evidence
  moderate/high where GRADE rated it very low, and the two tools agree on
  certainty in only ~53% of outcomes. Method-agnostic grading is therefore
  unstable -- a nutrition rubric must fix a tool and disclose it.
reasoning: >
  PMC8168365 confirms both parts (the red/processed-meat divergence and the ~53%
  agreement). Nuance carried from the raw: the 53% figure derives from a
  low-carb/T2D study, not the red-meat data, but is an accurate general statement
  about the two tools. Graded A as a field-methodology finding. It anchors this
  lane's rule: default to the GRADE spine, run NutriGrade in parallel on
  observational-inherent claims, and attach CONTESTED when they disagree >=1 band.
---

# nutrition/tool-instability-005

Two mainstream grading tools can reach opposite verdicts on the same nutrition
evidence, agreeing on certainty barely half the time. That means a grade is not a
property of the evidence alone -- it depends on which tool you picked. A honest
nutrition rubric fixes one tool as its default and discloses it.

Operationally this lane runs the GRADE spine by default, checks it against
NutriGrade on observational-inherent claims, and flags the claim as contested
whenever the two tools disagree by a band or more.
