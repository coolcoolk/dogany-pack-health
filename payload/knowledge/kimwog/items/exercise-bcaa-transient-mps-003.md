---
# Converted from batch1-exercise-nutrition.raw.json finding [11] (BCAA worked
# example, vote 2-1 -> confidence reflects the split). Rubric: exercise.rubric.md
# @clinical-physio row exercise/bcaa-transient-mps-003.
id: exercise/bcaa-transient-mps-003
domain: exercise
grade: B (negative)
lane: "@clinical-physio"
locale: universal
as_of: 2023
contested: no
sources:
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10561576/"  # BCAA/EAA kinetics (batch1 2-1)
  - "framework:GRADE -- B tier; split 2-1 vote holds confidence at medium, not A"
applicability:
  axes:
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
claim: >
  BCAAs or leucine taken alone give only a transient (~1-2 h) muscle-protein-
  synthesis stimulus and cannot sustain synthesis the way a complete protein does
  (~3-5 h), because a complete protein keeps delivering all essential amino acids
  as it is digested and absorbed. BCAA-alone supplementation has low practical value.
reasoning: >
  This is a negative claim graded at the RCT-level band: BCAA-alone is
  demonstrably inferior to complete protein for sustaining synthesis. The source
  set split 2-1 in verification, so confidence is held at medium (B) rather than
  pushed higher -- when torn, grade down. The practical implication is that
  complete protein sources dominate; free-form BCAA products add little for
  someone already meeting protein intake.
---

# exercise/bcaa-transient-mps-003

Free-form BCAAs or leucine spike synthesis briefly but cannot hold it, because
they lack the other essential amino acids that a complete protein keeps
supplying during digestion. For anyone already hitting their daily protein
target, BCAA-alone products offer little practical benefit.

This is a negative finding held at the RCT-level band, deliberately not upgraded:
the underlying sources split on the exact magnitude, so the confidence reflects
that split rather than overstating certainty.
