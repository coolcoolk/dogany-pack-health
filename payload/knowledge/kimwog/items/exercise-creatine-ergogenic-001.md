---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Converted from batch1-exercise-nutrition.raw.json finding
# [8] (creatine worked example, vote 3-0). Rubric: exercise.rubric.md
# @clinical-physio row exercise/creatine-ergogenic-001.
id: exercise/creatine-ergogenic-001   # domain/slug-NNN. domain-scoped, lane NEVER in ID.
domain: exercise                      # M5 cross-domain field. MUST equal the ID prefix.
grade: A                              # letter grade = confidence ladder (A..E).
lane: "@clinical-physio"              # non-ID field. REQUIRED: exercise is multi-lane (3).
locale: universal                     # ISO code (e.g. KR) or "universal". non-ID field.
as_of: 2017-2025                      # as-of date / range of the underlying evidence.
contested: no                         # orthogonal to the letter grade.
sources:
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5469049/"  # ISSN 2017 creatine position stand (batch1 3-0)
  - "AIS Sports Supplement Framework -- Group A"             # independent corroboration
  - "IOC 2018 consensus statement on dietary supplements"    # independent corroboration
  - "framework:GRADE (Balshem 2011; Cochrane Handbook Ch.14) -- A via converging reviews + independent corroboration"
applicability:
  axes:
    - key: age_years          # core ledger axis
      type: numeric
      role: soft              # hard(gate) | soft(modifier) | scale(math input)
      unknown_policy: hedge   # hedge | ask | block_specifics
    - key: renal_condition    # safety axis -> block_specifics when unknown/refused
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:                   # hard gate: value must be in `allowed`, else the
        allowed: [none, healthy]   # specific dose claim is EXCLUDE_SWAP'd.
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The +10-20% performance figure is an upper-bound generalization drawn
      from high-intensity/repetitive tasks; scale it down for pure-endurance
      athletes, where the ergogenic effect is small to negligible.
    grade: C   # each refraction note carries its own grade (DGN-119).
claim: >
  Creatine monohydrate is the most effective ergogenic aid for
  high-intensity/repetitive exercise (performance improvement on the order of
  +10-20% after a loading phase) and for lean-mass gain; it is safe at up to
  30 g/day for 5 years in healthy adults with no pre-existing renal disease.
reasoning: >
  The ISSN 2017 position stand carries a disclosed supplement-industry conflict,
  but independent bodies neutralize it: the Australian Institute of Sport rates
  creatine Group A (strongest evidence) and the IOC 2018 consensus corroborates
  efficacy and safety. Because converging systematic reviews plus independent
  institutional corroboration is exactly what the GRADE spine treats as
  high-certainty, this reaches the top confidence band. Safety derives from
  monitoring and long-term observational follow-up. Safety-critical: disclose
  the confidence band, the as-of range, and applicability up front, and withhold
  a specific dose green-light when renal status is unknown or refused.
---

# exercise/creatine-ergogenic-001

Creatine monohydrate is the best-evidenced ergogenic aid in the strength and
power space. The efficacy signal (short-duration, high-intensity, repeated-bout
work and lean-mass accrual) is corroborated across independent institutional
bodies, which is what lifts it above a single society stand that would otherwise
be discounted for industry conflict.

The safety envelope (up to 30 g/day for five years in healthy adults) applies to
people without pre-existing renal disease. When renal status is unknown or the
user declines to share it, the answer path gives the general mechanism and the
population-level finding but withholds a specific dose recommendation -- it does
not go silent. Endurance-only athletes should discount the performance figure.
