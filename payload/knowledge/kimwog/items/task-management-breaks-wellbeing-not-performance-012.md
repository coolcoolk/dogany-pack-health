---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# Both sources read: the meta-analysis in full text (PLOS ONE open access), and
# the Biwer trial's full abstract and citation from the publishing university's
# research record. Note the detail that decides the Pomodoro question: even the
# condition Biwer et al. LABEL 'Pomodoro technique' ran 24 minutes of work and
# 6 of break, not 25 and 5.
id: task-management/breaks-wellbeing-not-performance-012
domain: task-management
grade: B (meta-analysis plus a randomised comparison; small performance effect with detected bias, single-day trial)
lane: "@behavioral-productivity"
locale: universal
as_of: 2023
contested: no
sources:
  - "https://doi.org/10.1371/journal.pone.0272460"
  - "Albulescu, P., Macsinga, I., Rusu, A., Sulea, C., Bodnaru, A., & Tulbure, B. T. (2022). 'Give me a break!' A systematic review and meta-analysis on the efficacy of micro-breaks for increasing well-being and performance. PLOS ONE, 17(8), e0272460."
  - "https://doi.org/10.1111/bjep.12593"
  - "Biwer, F., Wiradhany, W., Egbrink, M. G. A. O., & de Bruin, A. B. H. (2023). Understanding effort regulation: Comparing 'Pomodoro' breaks and self-regulated breaks. British Journal of Educational Psychology, 93(S2), 353-367."
claim: >
  Breaks help how work feels, barely help what work produces, and no interval
  has been established. Meta-analysis of 22 samples (N = 2,335) of micro-breaks
  (defined as under 10 minutes): vigour d = 0.36 (95% CI .16-.55, k = 9),
  fatigue d = 0.35 (95% CI .19-.50, k = 9), but PERFORMANCE d = 0.16 (95% CI
  -.04 to .37, k = 15) -- not significant, with substantial heterogeneity
  (I-squared 59.45%), Egger's test indicating possible publication bias for
  performance, and trim-and-fill giving d = 0.22. Break duration moderated
  performance (b = .07, p = .006): longer breaks did better, the opposite of the
  short-interval prescription. The authors state there is no established
  standard for break length. Separately, Biwer et al. randomised 87 university
  students across one day of real self-study into self-regulated breaks
  (n = 35), 24-minutes-work / 6-minutes-break (n = 25) and 12/3 (n = 27):
  systematic-break students reported more concentration and motivation and less
  fatigue and distractedness, but there was NO difference between groups in
  invested mental effort or in task completion.
reasoning: >
  Two independent sources agreeing on the same asymmetry -- breaks move
  subjective state reliably and objective output weakly or not at all -- which
  is the same perceived-versus-measured split this warehouse records in
  exercise/recovery-modality-soreness-vs-performance-024 and in the nap
  literature under sleep-recovery. Held one band below the top because the
  performance effect is null with detected publication bias in the meta-analysis
  and because Biwer is a single-day trial at n = 87. Carried as the item that
  refuses the 25-minute interval: the duration moderator points the OTHER WAY
  from short fixed blocks, no source establishes any specific interval, and the
  one trial that compared a Pomodoro-style schedule against self-chosen breaks
  did not even use 25 minutes.
---

# task-management/breaks-wellbeing-not-performance-012

Two separate lines of evidence agree on the same split.

The meta-analysis of short breaks finds clear effects on how work feels --
vigour up, fatigue down, both around d = 0.35 -- and no significant effect on
performance. The performance estimate is small, its confidence interval crosses
zero, its heterogeneity is high, and there is a sign of publication bias in it
specifically.

The randomised comparison finds the same shape in a real study day. Students on
a fixed work/break schedule reported more concentration and motivation and less
fatigue and distractedness than students choosing their own break timing. On
invested mental effort and on task completion there was no difference between
the groups. The authors do note an apparent efficiency benefit -- similar
completion in shorter total time -- because the self-regulating students took
longer sessions and longer breaks.

So a fixed break schedule is defensible on the grounds that it makes the work
feel better and stops sessions and breaks from drifting long. It is not
defensible on the grounds that it makes you get more done.

On the interval itself, three facts:

- No source establishes any particular work-block length. The meta-analysis
  authors say explicitly there is no established standard for break length.
- The one duration moderator that reached significance points AGAINST short
  blocks: longer breaks were associated with better performance, not worse.
- The trial usually cited for the 25-minute technique did not test 25 minutes.
  Its own condition ran 24 minutes of work and 6 of break, and its comparison
  was against self-chosen breaks rather than against another interval.

The 25-minute number itself has no primary study behind it. See GAPS.md and
task-management/no-block-length-or-task-count-evidence-015.
