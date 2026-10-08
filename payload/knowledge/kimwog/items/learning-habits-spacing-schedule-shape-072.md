---
# Learning-retention sprint 2026-10-06 (dispatch kw-learning-retention).
# Partly closes the GAPS.md @study-craft entry "OPTIMAL SCHEDULES, AS OPPOSED
# TO OPTIMAL GAPS": 014 rests on one two-session gap experiment; this item
# adds the two syntheses that speak to MULTI-review schedules. Read at source:
# Cepeda et al. 2006 full article (evullab.org author copy: abstract, Table 1,
# expanding-vs-fixed section, General Discussion); Latimier, Peyre & Ramus,
# the PsyArXiv preprint kzy7u (Word file, read in full -- the publisher text is
# closed). The preprint gives expanding-vs-uniform g = 0.032; summaries of the
# published abstract give 0.034. The preprint figure and CI are used and the
# discrepancy is recorded here rather than resolved.
id: learning-habits/spacing-schedule-shape-072
domain: learning-habits
grade: B (two meta-analyses; spaced > massed is robust, expanding = uniform rests on 16 mostly-lab studies of word pairs)
lane: "@behavioral"
locale: universal
as_of: 2021
contested: yes
sources:
  - "https://doi.org/10.1037/0033-2909.132.3.354"
  - "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. Psychological Bulletin, 132(3), 354-380."
  - "https://www.evullab.org/pdf/CepedaPashlerVulWixtedRohrer-PB-2006.pdf"  # author-lab copy, read at source
  - "https://doi.org/10.1007/s10648-020-09572-8"
  - "Latimier, A., Peyre, H., & Ramus, F. (2021). A meta-analytic review of the benefit of spacing out retrieval practice episodes on retention. Educational Psychology Review, 33, 959-987."
  - "https://psyarxiv.com/kzy7u/"  # preprint, read in full at source; publisher version closed access
  - "learning-habits/interval-from-retention-target-014"  # within-warehouse cross-ref: the size of the gap depends on the retention horizon (Cepeda 2008)
  - "learning-habits/retrieval-practice-moderators-071"  # within-warehouse cross-ref: feedback after each attempt
  - "learning-habits/lapse-is-not-a-reset-015"  # within-warehouse cross-ref: late is cheaper than early
  - "framework:GRADE -- spaced-over-massed is replicated across 317 experiments (Cepeda 2006) and holds after trim-and-fill in spaced retrieval (Latimier 1.02 -> 0.74). The schedule-shape question rests on 16 studies / 54 effects, mostly lab, mostly word pairs, with the first retrieval often timed differently between arms. No trial compares whole multi-month scheduler algorithms against a plain uniform schedule on a learning outcome."
schedule_rules:
  - rule: separate repeated study of the same item by time; never repeat it back-to-back
    effect: final recall 47.3 vs 36.7 percent, spaced vs massed, all retention intervals pooled (Cepeda 2006, Table 1); spaced vs massed retrieval g 1.02, 0.74 after trim-and-fill (Latimier)
    basis: Cepeda 2006; Latimier 2021
    basis_grade: A
  - rule: size the gap from the retention horizon, longer horizon longer gap
    effect: the gap producing maximal retention increased as the retention interval increased (Cepeda 2006 abstract); specific gap values in 014
    basis: Cepeda 2006; learning-habits/interval-from-retention-target-014
    basis_grade: B
  - rule: uniform (equal) gaps are an acceptable default; expanding gaps are not required
    effect: expanding vs uniform g 0.032 [-0.10, 0.17], 54 effects, 16 studies, no heterogeneity (Latimier)
    basis: Latimier 2021
    basis_grade: B
  - rule: when an item has more than four exposures, expanding may help slightly
    effect: more than 4 exposures g 0.20 [-0.07, 0.46] vs 4 or fewer -0.04 (moderator p = .09, tentative per the authors)
    basis: Latimier 2021
    basis_grade: C
  - rule: when no answer is shown after a failed attempt, make the first review early
    effect: proposed by Cepeda 2006 as the likely reason expanding sometimes helps (it minimises forgetting before the first retrieval when feedback is withheld); not tested as a moderator
    basis: Cepeda 2006
    basis_grade: D
refraction_notes:
  - note: >
      THE GAP MATTERS, THE CURVE OF GAPS MUCH LESS. Whether reviews are spread
      out at all, and roughly how far relative to the date the material must
      still be known, are the evidence-backed levers. Whether each gap is
      longer than the last showed no average difference. A learning module
      does not need an elaborate algorithm to get most of the benefit, and
      should not tell users that expanding intervals are proven superior.
    grade: B
  - note: >
      CRAMMING IS NOT MASSING. Cepeda 2006 notes that a few hours of
      pre-exam cramming is usually repeated non-contiguous study, not literal
      massing, and that the real comparison people mean is studying just
      before the exam versus days or weeks before. That comparison is the gap
      question (014), not the spaced-versus-massed one.
    grade: B
  - note: >
      ADAPTIVE SCHEDULERS ARE NOT REFUTED BY THIS. Latimier et al. note that
      per-learner, per-item adaptive schedules make the uniform-versus-
      expanding comparison less relevant. Nothing here tests one against a
      fixed schedule; this item supports "uniform is good enough", not
      "adaptive is useless".
    grade: C
claim: >
  Spreading repeated study of the same material over time is reliably better
  than massing it: in the spaced-versus-massed comparisons of a synthesis of
  839 assessments in 317 experiments, final recall averaged 47.3 percent after
  spaced and 36.7 percent after massed study (Cepeda et al. 2006), and spaced over massed retrieval practice gave
  g = 1.02, still 0.74 after trim-and-fill correction for publication bias
  (Latimier et al. 2021). The best gap grows with how long the material must
  be retained (Cepeda 2006; sizes in 014). The shape of the schedule matters
  much less: expanding gaps (each longer than the last) did not beat equal
  gaps on average, g = 0.032 [-0.10, 0.17] across 54 effects in 16 studies,
  with only a tentative advantage when items get more than four exposures.
  Practical rule: always space, size the gaps to the retention horizon, and
  treat equal gaps as a sound default; do not present expanding intervals as
  established.
reasoning: >
  Cepeda, Pashler, Vul, Wixted & Rohrer (2006) synthesised 839 assessments of
  distributed practice in 317 experiments from 184 articles on verbal recall.
  Their spacing-versus-lag distinction matters: spaced (lag of 1 s or more)
  beat massed at every retention interval tested, from under a minute to over
  a month, with no sign that retention interval modulates the spacing effect
  proper. Lengthening an already non-zero gap helped up to a point that grew
  with the retention interval. On expanding versus fixed gaps they had only 22
  accuracy comparisons and 8 effect sizes; expanding was ahead overall but
  with large standard errors, and three long-interval researchers found three
  different answers (expanding better, fixed better, no difference). They
  suggest expanding may help when feedback is withheld because it reduces
  forgetting before the first retrieval.
  .
  Latimier, Peyre & Ramus (2021) restricted the question to spaced RETRIEVAL
  practice and used robust variance estimation. Subset 1 (11 studies, 39
  effects): spaced over massed g 1.02 [0.68, 1.36]; Egger's test showed funnel
  asymmetry; trim-and-fill lowered it to 0.74 [0.55, 0.92]. Subset 2 (16
  studies, 54 effects): expanding over uniform g 0.032 [-0.10, 0.17], p .62,
  I-squared 0; 55 percent of effects favoured expanding and 43 percent
  uniform. The only moderator near significance was exposures per item
  (more than four: 0.20, CI crossing zero; four or fewer: -0.04; p .09).
  Retention interval did not moderate it. Typical study: adults in a lab,
  word pairs, cued recall, often no feedback, and in 34 of 54 comparisons the
  first retrieval came immediately in the expanding arm but later in the
  uniform arm -- coded as a moderator, not significant at alpha .1.
  .
  Contested because the expanding-interval belief is widespread in study
  advice and built into popular tools, and because the null result rests on a
  narrow material base. The direction of this item is "not shown to matter",
  not "shown not to matter".
---

# learning-habits/spacing-schedule-shape-072 -- 간격 반복: 간격을 두는 것은 확실, 간격을 점점 늘리는 것은 미확인

**한 줄 그림:** 반복은 반드시 날을 띄워서 하고, 간격 크기는 언제까지 기억해야 하는지로 정한다. 간격을 매번
늘리느냐 같게 두느냐는 평균적으로 차이가 없었다.

## Three separate questions

People ask "what is the best spacing schedule?" as if it were one question.
The literature answers three separate ones, with different strength.

| Question | Answer | Strength |
|---|---|---|
| Space at all, or repeat back-to-back? | Space. Recall 47 vs 37 percent; retrieval g 0.74 after bias correction | very strong |
| How big a gap? | Bigger as the retention horizon lengthens; erring long is cheaper (014) | strong direction, few long experiments |
| Equal gaps or growing gaps? | No average difference (g 0.03) | moderate, narrow material base |

The third answer surprises people, because growing intervals are built into
most flashcard tools and repeated in most study advice. In the one synthesis
that isolates it, 54 comparisons split almost evenly, and the overall
difference was indistinguishable from zero. There is a weak hint that growing
gaps help once an item has been reviewed more than four times. The authors
call that tentative.

## How a learning module should use it

- Never schedule two reviews of the same item back-to-back in one sitting.
- Ask, or assume and state, how long the material needs to last, then size
  the gaps from that (014 has the numbers).
- Equal gaps are a sound and explainable default. If the module grows the
  gaps, that is a product choice. Do not present it as a proven improvement.
- If the module shows the answer after a failed attempt (071), the timing of
  the first review matters less. If it does not, bring the first review
  earlier.
- A late review costs little and a skipped review is not a reset (015). The
  main failure is not spacing at all.

## 한국어 요약 (답변용)

- 같은 내용을 연달아 반복하지 말고 시간 간격을 두고 반복한다. 317개 실험을 종합한 연구의 간격 대 몰아 하기 비교에서 간격을 둔 쪽의 회상률이
  47%, 몰아서 한 쪽이 37%였다. 떠올리기 연습만 따로 보아도 효과 크기가 0.74(출판 편향 보정 후)로 크다.
- 간격의 크기는 언제까지 기억해야 하는지에 따라 정한다. 오래 기억해야 할수록 간격을 넓힌다. 구체적인
  숫자는 014 항목을 쓴다.
- 간격을 점점 늘리는 방식이 같은 간격보다 낫다는 믿음은 근거가 약하다. 16개 연구, 54개 비교에서 평균
  차이가 없었다(효과 크기 0.03). 한 항목을 다섯 번 이상 반복할 때 늘리는 방식이 조금 나을 수 있다는
  약한 신호만 있다.
- 따라서 같은 간격도 충분히 좋은 기본값이다. 간격을 늘리는 것은 제품 선택일 뿐 입증된 개선이라고
  말하지 않는다.
- 시험 직전 몇 시간 벼락치기는 엄밀한 의미의 몰아 하기와 다르다. 진짜 질문은 '시험 직전에 하느냐,
  며칠·몇 주 전부터 하느냐'이고, 이는 간격 크기의 문제다.
