---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# HONEST SOURCING NOTE, stated here rather than buried: for Bevan and Hood the
# published abstract and full citation were retrieved and read; the full text
# was NOT retrieved in this pass (the repository entry carries no full text and
# the publisher refused automated retrieval). Campbell's citation was resolved
# to the publisher record but its text was likewise not read. The grade below
# reflects that, and no figure from either paper is quoted.
id: task-management/target-corruption-completion-metrics-010
domain: task-management
grade: D (conceptual and case-analysis literature; no effect estimate, and full texts not retrieved in this pass)
lane: "@behavioral-productivity"
locale: universal
as_of: 2006
contested: no
sources:
  - "https://doi.org/10.1111/j.1467-9299.2006.00600.x"
  - "Bevan, G., & Hood, C. (2006). What's measured is what matters: targets and gaming in the English public health care system. Public Administration, 84(3), 517-538."
  - "https://doi.org/10.1016/0149-7189(79)90048-X"
  - "Campbell, D. T. (1979). Assessing the impact of planned social change. Evaluation and Program Planning, 2(1), 67-90."
claim: >
  Once a count of completed work becomes the thing being optimised, it stops
  being a good measure of the work. Bevan and Hood analyse a governance regime
  built on targets in the English health service and argue that its two
  underlying assumptions -- that the measured part can stand for the whole
  (synecdoche), and that problems of measurement and gaming do not matter -- do
  not hold, examining reported successes against measurement problems and
  gaming. Campbell states the general form: the more any quantitative social
  indicator is used for social decision-making, the more subject it will be to
  corruption pressures and the more apt it will be to distort and corrupt the
  social processes it is intended to monitor. Neither source provides an effect
  size, and this item asserts none.
reasoning: >
  Graded at the bottom of the ladder DELIBERATELY and stated plainly: these are
  a policy analysis and a methodological essay, not measurements, and in this
  pass neither full text was retrieved -- only the abstract, the citation and
  the widely reproduced statement of Campbell's principle. This item exists
  anyway for a forcing-point reason, not an evidential one: a task agent
  computing a completion rate will produce a number the owner then optimises,
  and the failure mode has a name and a literature even though it has no
  effect size. It is carried at a low band so that it can never be spoken as
  though it were measured. Its empirical partner, which IS measured, is
  task-management/record-is-not-behaviour-009: gaming is not needed to corrupt a
  completion count -- ordinary recording failure already does it.
---

# task-management/target-corruption-completion-metrics-010

A completion rate is a description of a task store. The moment it becomes a
target, it starts describing the target instead.

Campbell's formulation is the general one: the more a quantitative indicator is
used to make decisions, the more it comes under corruption pressure, and the
more it distorts the process it was meant to monitor. Bevan and Hood examine a
real governance regime built on targets and argue that it rests on two
assumptions that do not survive contact with practice -- that the measured
slice can stand in for the whole, and that measurement problems and gaming can
be treated as second-order.

Neither source measures anything, and this item claims no magnitude. It is here
as a named hazard, not as a finding, and it is graded at the bottom of this
lane's ladder for that reason.

The concrete forms it takes in a personal task system:

- Small, easily-closed items get created and closed because they move the
  number; large or ill-defined work does not get created at all, so it cannot
  be counted as incomplete.
- Items get closed to clear a view rather than because the work finished.
- Work that never entered the store is invisible to the rate, so a week of
  heavy unplanned work reads as a bad week.

None of that requires anyone to be dishonest, which is the important part. And
the ordinary case is worse still: recording simply lapses, and the lapse looks
identical to failure -- see task-management/record-is-not-behaviour-009, which
does have a measurement behind it.

The operational consequence is to keep a completion count as an internal
diagnostic and never as a score reported back to the person as an assessment of
them. If it is reported, it must be reported alongside how much entered the
store, because a rate whose denominator the person controls is not a
measurement of anything.
