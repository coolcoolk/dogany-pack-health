---
# Body-ideal archetype sprint 2026-09-30. "유연한 몸 / 요가" -- the range-of-
# motion ideal. Filed separately from Pilates because the two are routinely
# merged in conversation and they have different defining features.
id: exercise/ideal-yoga-mobility-039
domain: exercise
grade: B (ROM responds to stretching and to full-range resistance training); C (yoga fitness effects, older adults); D (archetype definition)
lane: "@performance-lit"
locale: universal
as_of: 2021-2025
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/37301370/"  # Konrad A et al. J Sport Health Sci 2024 -- chronic stretching increases ROM (ES ~1.0 vs control); PNF and static > ballistic/dynamic; volume/intensity/frequency not significant moderators
  - "https://pubmed.ncbi.nlm.nih.gov/36622555/"  # Alizadeh S et al. Sports Med 2023 -- full-range resistance training increases ROM (ES 0.73), no different from stretching; bodyweight-only showed no significant gain
  - "https://pubmed.ncbi.nlm.nih.gov/34770176/"  # Shin S. IJERPH 2021 -- 12 studies, older adults: yoga moderately improves strength, balance, mobility, lower-body flexibility; no cardiorespiratory effect
  - "exercise/acute-static-stretch-force-deficit-021"
  - "exercise/ideal-pilates-controlled-movement-037"
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      RANGE IS TRAINABLE TWO WAYS. Stretching raises range of motion, and
      full-range resistance training raises it about as much. A user who wants
      both muscle and flexibility does not need a separate long stretching
      block to get range; loaded lifts through full range already build it.
    grade: B
  - note: >
      YOGA IS NOT A CARDIO SUBSTITUTE. In older adults it improved strength,
      balance and lower-body flexibility but not cardiorespiratory endurance.
    grade: C
claim: >
  The yoga / mobility ideal is a body that moves through large, comfortable
  ranges of motion -- hips, hamstrings, thoracic spine, shoulders -- with the
  balance and strength to own those positions, and the calm breath yoga pairs
  with them. It is distinguished from Pilates by its emphasis on range and
  positions (held or flowed) rather than precise trunk-organised control, and
  from calisthenics by range rather than relative strength. Range of motion
  responds to chronic stretching (PNF and static more than dynamic) and equally
  to full-range resistance training.
reasoning: >
  Two meta-analyses (Konrad 2024, Alizadeh 2023) establish the ROM response and
  its equivalence between stretching and full-range lifting. Yoga-specific
  fitness evidence here is a meta-analysis in older adults, graded lower for
  population transfer. The archetype picture is a convention of how users name
  the goal.
---

# exercise/ideal-yoga-mobility-039 -- 요가 / 유연성·가동성

**한 줄 그림:** 고관절·햄스트링·흉추·어깨가 넓고 편하게 움직이고, 그 자세를 균형 있게 버티며
숨이 차분한 몸.

## Distinguishing features

Range of motion first, with balance and positional strength; breath and calm.
Vs Pilates: range/positions vs precise controlled movement from the trunk.

## Measurable here

- Practice pick `mobility_flow` (5-minute flow each session) -- an adherence
  signal, not a range measure.
- `weekly_sessions` / workouts `minutes` for logged yoga classes.
- `zero_load_control_share_sets` partially (held poses logged with hold_sec).

## Not measurable here

Range of motion itself (sit-and-reach, hip rotation, shoulder flexion angles),
balance tests. No ROM token exists; proposed `rom_<joint>_deg` or a simple
`sit_reach_cm`. Say "we can track that you practise it, not how far you reach".

## Training emphasis and practice

Regular stretching or yoga (PNF/static for range), full-range loaded lifts,
mobility flows before sessions; static stretching placed after lifting or on
separate days where acute force matters (item 021).

## Failure modes

Forcing end range in hypermobile joints; long static holds right before heavy
or explosive work (acute force deficit); expecting fitness gains yoga did not
show (cardio).

## Combines / conflicts

Combines with every archetype; conflicts only in time budget. Overlaps with
Pilates on breath and mind-body focus.
