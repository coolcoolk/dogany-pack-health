---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# Read in full text (Konstanz KOPS open-access copy of the published article).
# Every figure below is quoted from the paper's own results section, including
# the publication-bias analysis, which is the half that does not survive
# retelling.
id: task-management/implementation-intentions-effect-shrinks-003
domain: task-management
grade: B (very large meta-analysis with explicit bias correction; effect direction robust, magnitude heavily corrected)
lane: "@behavioral-productivity"
locale: universal
as_of: 2024
contested: yes
sources:
  - "https://doi.org/10.1080/10463283.2024.2334563"
  - "Sheeran, P., Listrom, O., & Gollwitzer, P. M. (2025). The when and how of planning: Meta-analysis of the scope and components of implementation intentions in 642 tests. European Review of Social Psychology, 36(1), 162-194."
  - "https://doi.org/10.1016/S0065-2601(06)38002-1"
  - "Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. Advances in Experimental Social Psychology, 38, 69-119. (the source of the widely quoted d = .65)"
claim: >
  If-then plans ("when situation X arises, I will do Y") work, but the famous
  number is roughly four times the corrected one, and the correction comes from
  the original authors. Gollwitzer and Sheeran (2006) reported d = .65 across 94
  independent tests and that figure is what circulates. The same authors'
  2024/2025 meta-analysis of 642 independent tests reports a sample-weighted
  average of d = .36 (95% CI [.33, .40]), finds Egger's regression at b = 1.06
  -- meeting the published threshold for "substantial" publication bias -- and
  reports a Robust Bayesian model-averaged estimate of d = .15 (95% CI
  [.08, .22]) with extreme evidence FOR an effect (BF_10 = 319.3) and extreme
  evidence for publication bias (BF_pb > 161.5) and for heterogeneity
  (tau = 0.27). Their own conclusion: the effect is robust but "small according
  to conventional guidelines" and "highly heterogenous", and "caution is
  warranted in interpreting findings from the present review". Moderators that
  raised effects: contingent if-then FORMAT, high motivation to pursue the goal,
  and rehearsal of the plan.
reasoning: >
  Flagged contested on the MAGNITUDE, not the direction. The existence of the
  effect is about as well evidenced as anything in this lane gets (642 tests,
  extreme Bayes factor in favour). What is contested is which number to speak,
  and the honest answer is that the two credible estimates differ by a factor of
  more than two (d = .36 raw vs d = .15 bias-corrected) and the popular one
  (d = .65) is superseded by its own authors. Graded one band down from the top
  for exactly the reason the authors themselves give: substantial publication
  bias plus extreme heterogeneity means the pooled number is a weak summary of a
  very mixed literature. This is also this lane's first zombie-stat catch, and
  an unusually clean one -- the correction was published by the same
  researchers who produced the original figure, so there is no dispute to
  adjudicate, only a citation to stop repeating.
---

# task-management/implementation-intentions-effect-shrinks-003

Forming a specific if-then plan -- "when I sit down after dinner, I will open
the tax file" -- does help, and it is one of the few things in this domain with
a serious evidence base behind it. But the effect size everyone quotes is not
the current one.

The 2006 meta-analysis that made the technique famous reported a
medium-to-large effect across 94 tests. The same authors' 2024 meta-analysis,
covering 642 tests including unpublished ones, reports a raw pooled effect
roughly half that size, and then reports that the literature carries
substantial publication bias by the standard test. When they apply a Robust
Bayesian model-averaging correction, the estimate falls again -- to a small
effect, with a confidence interval that stays clear of zero but sits well below
the popular figure.

Two things to hold at once, because dropping either one gets it wrong:

- The effect is real. The Bayesian analysis found extreme evidence in favour of
  an effect existing. This is not a debunking.
- The effect is small and very heterogeneous, and the authors themselves write
  that caution is warranted in interpreting their own review.

What the same paper found does raise the effect: making the plan genuinely
contingent (an if-then structure, not a to-do line), the person actually being
motivated to pursue the goal, and rehearsing the plan. So the operational
advice survives in a narrowed form -- attaching a task to a specific
trigger beats leaving it unattached -- while any promise about how much it will
help does not.

For an agent that converts a goal into scheduled work: propose the trigger, and
do not promise the size of the gain.
