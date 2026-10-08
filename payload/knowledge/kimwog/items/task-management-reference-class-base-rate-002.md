---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# The per-project-type escalation figures below were read out of the paper's
# own results table (author's accepted manuscript, arXiv:1303.6604), not from
# any secondary retelling of Flyvbjerg.
id: task-management/reference-class-base-rate-002
domain: task-management
grade: B (large systematic sample with objective outcome data; observational, non-personal domain)
lane: "@behavioral-productivity"
locale: universal
as_of: 2002
contested: no
sources:
  - "https://doi.org/10.1080/01944360208976273"
  - "Flyvbjerg, B., Holm, M. S., & Buhl, S. (2002). Underestimating costs in public works projects: Error or lie? Journal of the American Planning Association, 68(3), 279-295. (author's accepted manuscript read at arXiv:1303.6604)"
refraction_notes:
  - note: >
      This is TRANSPORT INFRASTRUCTURE, not personal tasks, and the outcome is
      COST, not time. It is carried here for one structural reason only: it is
      the largest body of objectively measured forecast-versus-outcome data
      that exists, and it establishes that the error is systematic, one-signed,
      and does not decay with experience. Do not quote 44.7% at a personal task.
    grade: D
claim: >
  Forecast error in planning is systematic and one-signed, and experience does
  not remove it. Across 258 transport infrastructure projects worth about
  US$90 billion, actual costs exceeded estimated costs in 9 of 10 cases; for a
  randomly selected project the probability of overrun is 86%. Average cost
  escalation by type: rail 44.7% (n = 58, SD 38.4), fixed links 33.8% (n = 33,
  SD 62.4), roads 20.4% (n = 167, SD 29.9), all differences from zero at
  p <= 0.004. The finding that makes this load-bearing rather than merely
  colourful: underestimation has NOT decreased over the 70-year period the data
  covers -- it is the same order of magnitude as it was 10, 30 and 70 years
  ago. The authors conclude the pattern cannot be explained by error and is
  best explained by strategic misrepresentation.
reasoning: >
  Graded high for its class -- very large sample, objective recorded outcomes at
  both ends, statistically overwhelming -- and held one band down because it is
  observational, it is a different domain from personal task management, and its
  headline causal claim (deception rather than optimism) is an interpretation
  the data constrains but does not prove. It is carried in this lane as the
  OUTSIDE-VIEW anchor for task-management/planning-fallacy-own-estimates-001:
  001 shows the individual estimate is biased, 002 shows what a stack of past
  outcomes looks like when someone finally counts them, and that counting them
  is the only thing that has ever been shown to help. The "no learning over 70
  years" result is the operationally important half and is the half that gets
  dropped in retelling.
---

# task-management/reference-class-base-rate-002

The largest body of measured forecast-versus-outcome data anywhere is the
transport-infrastructure cost literature, and it says three things that a
planning agent should carry.

First, the error is one-signed. Costs were underestimated in 9 out of 10
projects; for a randomly picked project the chance that actual exceeds
estimated is 86%. This is not noise around a correct central estimate. It is a
distribution with almost nothing on the pessimistic side.

Second, the magnitude is large and varies by kind of work: rail averaged 44.7%
over budget, fixed links 33.8%, roads 20.4%. The spread within each type is
wide (standard deviations of 38, 62 and 30 percentage points respectively), so
the average is a shift, not a precision correction.

Third -- and this is the part that gets dropped when the study is retold -- the
underestimation has not shrunk over the seventy years the dataset spans. It is
the same size now as it was ten, thirty and seventy years ago. Repeated
exposure to one's own overruns did not, at the level of an entire industry,
produce learning.

For a task agent the transfer is structural, not numerical. Do not apply 44.7%
to anything. What transfers is the method: when you want to know how long
something will take, the useful input is the distribution of how long
comparable past things actually took, not a fresh estimate of this one. That is
the same correction that worked in
task-management/planning-fallacy-own-estimates-001, arrived at from a
completely different direction. And the seventy-year null on learning is the
warning that having the history is not the same as using it -- the reference
class only helps if it is put in front of the estimate at the moment the
estimate is made.
