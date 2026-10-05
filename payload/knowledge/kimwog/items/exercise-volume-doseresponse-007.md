---
# Converted from files/inbox/volume-research-2026-07-18.md finding [2] (dose-
# response meta-regression, vote 3-0 across four converging claims). Rubric:
# exercise.rubric.md @performance-lit row exercise/volume-doseresponse-007.
id: exercise/volume-doseresponse-007
domain: exercise
grade: B (dose-response)
lane: "@performance-lit"
locale: universal
as_of: 2025
contested: no
sources:
  - "https://link.springer.com/article/10.1007/s40279-025-02344-w"  # Pelland et al. 2025, Sports Medicine, 67 studies/2058 participants
  - "https://pubmed.ncbi.nlm.nih.gov/41343037/"
  - "https://sportrxiv.org/index.php/server/preprint/view/460"
  - "framework:GRADE -- Bayesian meta-regression, current state-of-art, not yet independently replicated"
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The study did not identify a growth plateau or reversal point within the
      tested volume range -- the slope stayed positive throughout. Treating MRV
      as an absolute hard ceiling is therefore an inference beyond the data, not
      a directly observed plateau; phrase MRV guidance as a recoverability limit,
      not a growth-stops-here line.
    grade: B
claim: >
  Muscle hypertrophy increases monotonically with weekly set volume (100%
  posterior probability the slope exceeds zero) with diminishing returns as
  volume rises, though the diminishing-returns curve is less pronounced for
  hypertrophy than for strength. This empirically justifies MAV/MRV ceilings as
  the point where added sets yield progressively less growth.
reasoning: >
  Pelland et al. 2025 (Sports Medicine, DOI 10.1007/s40279-025-02344-w, PMID
  41343037) ran a Bayesian meta-regression across 67 studies and 2058
  participants and reports the marginal volume slope exceeded zero with 100%
  posterior probability for both hypertrophy and strength, with both best-fit
  models showing diminishing returns and strength's plateau considerably more
  pronounced. This is the current state-of-art dose-response estimate and sits
  at the RCT-level pre-consensus band: strong single meta-regression, not yet
  independently replicated. Caveat carried forward: no plateau or reversal was
  observed within the tested range, so an absolute MRV ceiling is an inference,
  not a direct finding.
---

# exercise/volume-doseresponse-007

More weekly sets keeps producing more hypertrophy across the tested range, with
very high confidence that the trend is real -- but each added set buys less
growth than the one before it, and the tapering-off is milder than it is for
strength gains. That diminishing-returns shape is exactly why capping volume at
a maximum-adaptive/maximum-recoverable range makes sense: past a point, the
extra sets barely move the needle even before recovery becomes the limiting
factor.

One caveat worth carrying: within the volumes actually tested, the curve never
turned down or flattened to zero. So an absolute set-count ceiling is a
reasonable inferred boundary (recovery capacity, session length, life)
rather than something the data directly showed as a growth stop-point.
