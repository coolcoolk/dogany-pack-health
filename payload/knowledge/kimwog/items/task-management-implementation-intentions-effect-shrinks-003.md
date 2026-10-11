---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# Read in full text (Konstanz KOPS open-access copy of the published article).
# Every figure below is quoted from the paper's own results section, including
# the publication-bias analysis, which is the half that does not survive
# retelling.
# Source re-audit 2026-10-07: Sheeran et al. 2025 full text (KOPS copy) and the
# 2006 chapter's abstract re-read. d=.36 pools four outcome families (behaviour
# change alone d=.27, k=301); trim-and-fill leaves .35 and only the Robust
# Bayesian model gives .15, so the correction is method-dependent, not 'heavy';
# the authors say estimating the population effect was not their aim and call
# the findings corroborating, so 'superseded by its own authors' is withdrawn.
# Plan-format moderator added (contingent .43 vs schedule .29).
id: task-management/implementation-intentions-effect-shrinks-003
domain: task-management
grade: B (very large meta-analysis with bias diagnostics reported; effect direction robust, magnitude depends on the correction method)
lane: "@behavioral-productivity"
locale: universal
as_of: 2024
contested: yes
sources:
  - "https://doi.org/10.1080/10463283.2024.2334563"
  - "Sheeran, P., Listrom, O., & Gollwitzer, P. M. (2025). The when and how of planning: Meta-analysis of the scope and components of implementation intentions in 642 tests. European Review of Social Psychology, 36(1), 162-194."
  - "https://doi.org/10.1016/S0065-2601(06)38002-1"
  - "Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. Advances in Experimental Social Psychology, 38, 69-119. (the source of the widely quoted d = .65; its abstract, p.69: 94 independent tests, d = .65 on goal attainment)"
claim: >
  If-then plans ("when situation X arises, I will do Y") work, but the famous
  number is well above the same authors' later estimates, and those estimates
  do not all mean the same thing. Gollwitzer and Sheeran (2006) reported
  d = .65 on goal attainment across 94 independent tests and that figure is
  what circulates. The same authors' 2024/2025 meta-analysis of 642 independent
  tests reports a sample-weighted average of d = .36 (95% CI [.33, .40]) pooled
  over four outcome families: behaviour change alone is d = .27 (k = 301, 86%
  of them health behaviours), cognitive performance .47, affect regulation .66,
  social judgement .52. It finds Egger's regression at b = 1.06 -- meeting the
  published threshold for "substantial" publication bias -- and then two
  corrections that disagree: trim-and-fill leaves d = .35 (95% CI [.31, .38]),
  while a Robust Bayesian model-averaged estimate is d = .15 (95% CI
  [.08, .22]), with extreme evidence FOR an effect (BF_10 = 319.3) and extreme
  evidence for publication bias (BF_pb > 161.5) and for heterogeneity
  (tau = 0.27). The authors write that estimating the population effect size
  was not the goal of the review, and describe their findings as corroborating
  the earlier conclusion that planning promotes behaviour change. Their own
  conclusion: the effect is robust but "small according to conventional
  guidelines" and "highly heterogenous", and "caution is warranted in
  interpreting findings from the present review". Moderators that raised
  effects (comparisons across tests, not randomised within studies): contingent
  if-then FORMAT (d = .43, k = 373) over a SCHEDULE format that lists when,
  where and what without a cue-response link (d = .29, k = 269), high
  motivation to pursue the goal, and rehearsal of the plan.
reasoning: >
  Flagged contested on the MAGNITUDE, not the direction. The existence of the
  effect is about as well evidenced as anything in this lane gets (642 tests,
  extreme Bayes factor in favour). What is contested is which number to speak,
  and the honest answer is that the credible estimates differ by a factor of
  more than two depending on the correction (d = .36 raw, .35 after
  trim-and-fill, .15 Robust Bayesian) and on the outcome (d = .27 for behaviour
  alone), while the popular one (d = .65, 94 goal-attainment tests) predates the
  larger review. The review does not retract it, but its larger and more
  complete evidence base gives smaller pooled numbers and shows substantial
  publication bias, so .65 should not be quoted as the size of a behavioural
  effect. Graded one band down from the top for exactly the reason the authors
  themselves give: substantial publication bias plus extreme heterogeneity
  means the pooled number is a weak summary of a very mixed literature. This is
  the lane's first catch of an older, larger number still circulating after a
  bigger review by the same authors, but a less clean one than first read: the
  two reviews differ in scope (94 tests of goal attainment against 642 tests
  across behaviour, cognition, affect and social judgement), so the rule is 'do
  not quote .65 as the size of the gain', not 'the authors withdrew it'.
---

# task-management/implementation-intentions-effect-shrinks-003

Forming a specific if-then plan -- "when I sit down after dinner, I will open
the tax file" -- does help, and it is one of the few things in this domain with
a serious evidence base behind it. But the effect size everyone quotes is not
the current one.

The 2006 meta-analysis that made the technique famous reported a
medium-to-large effect across 94 tests of goal attainment. The same authors'
2024 meta-analysis, covering 642 tests including unpublished ones and outcomes
beyond behaviour, reports a raw pooled effect roughly half that size (for
behaviour change alone smaller still, about d = .27), and then reports that the
literature carries substantial publication bias by the standard test. The usual
trim-and-fill correction barely moves the number; a Robust Bayesian
model-averaging analysis drops it to a small effect, with a confidence interval
that stays clear of zero but sits well below the popular figure. The two
corrections disagree, which is why the size stays contested. The authors do not
present the new figures as a replacement for the old one.

Two things to hold at once, because dropping either one gets it wrong:

- The effect is real. The Bayesian analysis found extreme evidence in favour of
  an effect existing. This is not a debunking.
- The effect is small and very heterogeneous, and the authors themselves write
  that caution is warranted in interpreting their own review.

What the same paper found does raise the effect: making the plan genuinely
contingent (an if-then structure, not a to-do line: contingent plans averaged
d = .43, plans that merely list when, where and what averaged d = .29), the
person actually being motivated to pursue the goal, and rehearsing the plan.
These are comparisons across studies, not tests within one. So the operational
advice survives in a narrowed form -- attaching a task to a specific
trigger beats leaving it unattached -- while any promise about how much it will
help does not. A calendar slot on its own is the schedule format, the weaker of
the two; the review's if-then plans linked a cue (a time and place, an event, a
point in a task) to the action.

For an agent that converts a goal into scheduled work: propose the trigger, and
do not promise the size of the gain.
