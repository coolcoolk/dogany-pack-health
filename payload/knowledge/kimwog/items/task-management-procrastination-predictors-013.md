---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# Read in full text. Every correlation below is quoted from the paper's own
# Tables 3-5 (mean observed r, not the corrected rho), with K and N attached.
id: task-management/procrastination-predictors-013
domain: task-management
grade: C (very large meta-analysis on an entirely correlational, self-report substrate; pre-replication-era)
lane: "@behavioral-productivity"
locale: universal
as_of: 2007
contested: no
sources:
  - "https://doi.org/10.1037/0033-2909.133.1.65"
  - "Steel, P. (2007). The nature of procrastination: A meta-analytic and theoretical review of quintessential self-regulatory failure. Psychological Bulletin, 133(1), 65-94."
refraction_notes:
  - note: >
      Every number here is a correlation between two SELF-REPORT scales, which
      is the measurement condition learning-habits/measurement-inflation-007
      says inflates effect sizes. Read the ordering as trustworthy and the
      magnitudes as upper bounds. Nothing here is causal: none of these
      variables was manipulated.
    grade: D
claim: >
  What predicts a task slipping is not what the popular account says. Across 691
  correlations, the strongest observed correlates of procrastination are
  conscientiousness r = -.62 (K = 20, N = 4,012), self-control r = -.58
  (K = 21), dilatory behaviour r = .52 (K = 16), distractibility r = .45
  (K = 13), impulsiveness r = .41 (K = 22, N = 4,005), self-efficacy r = -.38
  (K = 39, N = 6,994) and organisation r = -.36 (K = 25). The commonly assumed
  drivers are weak or absent: neuroticism r = .24 (K = 59), sensation seeking
  r = .17 (K = 11), and PERFECTIONISM r = -.03 (K = 24, N = 3,884) -- an
  essentially null result on a well-powered set. The single most operationally
  relevant number: INTENTION correlates r = -.03 with procrastination (K = 8),
  while the intention-action gap correlates r = .29 (K = 6).
reasoning: >
  Graded at the correlational band, not higher, and for once the reason is not
  sample size -- 691 correlations is enormous. It is that every variable on both
  sides of every correlation is a self-report scale, which is exactly the
  measurement condition this warehouse discounts, and the paper predates the
  replication-era corrections that learning-habits/replication-calibration-001
  imposes. Carried because the ORDERING is robust to those caveats and is
  directly actionable, and because two of its results are refutations that a
  task agent will otherwise get wrong: procrastination is not explained by
  perfectionism, and how strongly someone intends to do a task tells you
  essentially nothing about whether they will delay it.
---

# task-management/procrastination-predictors-013

The largest synthesis of why tasks slip puts the strongest correlates in a
clear order: conscientiousness and self-control at the top (both around 0.6 in
absolute terms), then distractibility and impulsiveness, then self-efficacy and
organisation, all in the 0.35-0.45 band.

Two results in it are more useful than the ranking, because they refute things
a task agent would otherwise assume.

The first is perfectionism. It is the standard folk explanation for delay, and
across 24 studies and nearly 4,000 people its correlation with procrastination
is essentially zero. Not weak -- absent. Treating a delayed task as evidence of
someone's high standards is not supported.

The second is intention. Across eight studies, how strongly someone intends to
do a task correlates about -0.03 with whether they procrastinate on it. The
gap between intention and action, however, correlates about 0.29. Intending
harder is not the mechanism; the mechanism sits between the intention and the
act.

That second finding is what makes
task-management/implementation-intentions-effect-shrinks-003 the right
intervention shape rather than a coincidence: the useful move is to attach the
task to a trigger, because that is where the failure is, not to strengthen the
commitment, because commitment is not where the failure is.

Read the sizes as upper bounds. Both sides of every correlation here are
self-report scales, which is the measurement condition that inflates effects,
and none of these variables was manipulated, so none of it is causal. The
ordering is what to trust.
