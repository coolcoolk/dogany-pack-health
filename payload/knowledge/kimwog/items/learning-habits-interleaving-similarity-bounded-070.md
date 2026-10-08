---
# Learning-retention sprint 2026-10-06 (dispatch kw-learning-retention). Closes
# the GAPS.md @study-craft entry "INTERLEAVING. Not shipped ... Evidence-lane
# work, for @behavioral." Both primaries read at source as full text:
# Brunmair & Richter, accepted manuscript at the University of Wuerzburg
# repository (every figure below from its abstract, Table 2 and the
# moderator / publication-bias sections); Rohrer, Dedrick, Hartwig & Cheung,
# full article PDF (abstract, Caveats 1-4, Discussion).
#
# material_rules is structured data for a learning module: one row per
# material class, with the pooled effect, its direction and the action. It is
# a reading of the meta-analysis's own table, not a product constant, except
# where a row says so.
id: learning-habits/interleaving-similarity-bounded-070
domain: learning-habits
grade: B (one large multilevel meta-analysis + one preregistered cluster RCT in maths; direction depends on material)
lane: "@behavioral"
locale: universal
as_of: 2020
contested: yes
sources:
  - "https://doi.org/10.1037/bul0000209"
  - "Brunmair, M., & Richter, T. (2019). Similarity matters: A meta-analysis of interleaved learning and its moderators. Psychological Bulletin, 145(11), 1029-1052."
  - "https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf"  # accepted manuscript, read at source for every figure quoted
  - "https://doi.org/10.1037/edu0000367"
  - "Rohrer, D., Dedrick, R. F., Hartwig, M. K., & Cheung, C.-N. (2020). A randomized controlled trial of interleaved mathematics practice. Journal of Educational Psychology, 112(1), 40-52."
  - "https://www.gwern.net/doc/psychology/spaced-repetition/2019-rohrer.pdf"  # mirror of the published article, read at source
  - "learning-habits/learning-techniques-high-utility-010"  # within-warehouse cross-ref: Dunlosky 2013 rates interleaving MODERATE, not high -- 'benefits have just begun to be systematically explored'
  - "learning-habits/surface-vs-deep-skew-013"  # within-warehouse cross-ref: standing limiter on over-generalising technique effects
  - "framework:GRADE -- the pooled effect is moderate (g=0.42, 238 effects, 59 studies) but heterogeneous by material, mostly university students in laboratory sessions, and trim-and-fill on the full set lowers it to 0.29. The one large classroom trial (maths, d=0.83) is preregistered and randomised by class, but interleaving there also delivers spacing and retrieval, did not measure time on task, and was not run on any other material."
material_rules:
  - material: paintings and complex naturalistic images (art styles, species, medical images)
    pooled_g: 0.67
    k: 70
    direction: interleave
    action: mix categories within a session once each category has been seen
    basis_grade: B
  - material: naturalistic photographs
    pooled_g: 0.35
    k: 19
    direction: interleave
    action: mix categories within a session
    basis_grade: B
  - material: artificial pictures and diagrams
    pooled_g: 0.31
    k: 63
    direction: interleave, weakly
    action: mix when categories are similar; trim-and-fill lowers this class to 0.17
    basis_grade: C
  - material: mathematical problem types
    pooled_g: 0.34
    k: 45
    direction: interleave after a short blocked introduction
    action: block a new skill first, then mix it with earlier problem types; give worked solutions or corrective feedback; expect it to take longer per problem
    basis_grade: B
  - material: expository text
    pooled_g: 0.21
    k: 25
    direction: no default
    action: keep the order the material was written in; the pooled effect is not significant (CI -0.06 to 0.47)
    basis_grade: C
  - material: words and vocabulary lists
    pooled_g: -0.39
    k: 13
    direction: block
    action: do not interleave by category; 13 effects only, cause may be task rather than material
    basis_grade: C
refraction_notes:
  - note: >
      INTERLEAVING IS FOR TELLING THINGS APART. The benefit is largest when
      categories look alike across the boundary and differ inside it
      (meta-regression: stronger for higher between-category similarity, lower
      within-category similarity, more complex material). If the learner's
      problem is discriminating which kind of thing they are looking at, mix.
      If it is memorising a list, interleaving has no claim here.
    grade: B
  - note: >
      IT WILL FEEL WORSE AND TAKE LONGER. Learners mostly believe blocking is
      more effective (Kornell & Bjork 2008; McCabe 2011, both as reported in
      Rohrer 2020), and every teacher in the maths trial reported the
      interleaved assignments took more time. A learning module should say so
      in advance rather than treat the extra difficulty as a failure signal.
    grade: B
  - note: >
      DO NOT INTERLEAVE BY SEPARATING ITEMS IN TIME. In the 17 effects that
      varied it, interleaving helped when exemplars followed each other
      directly (g=0.73) and not when they were spaced apart (g=0.22, CI
      crosses zero). Interleaving and spacing are different tools; this item
      does not license replacing one with the other.
    grade: C
claim: >
  Mixing categories within practice (ABCABC) instead of blocking them (AAABBB)
  improves later classification and problem-type choice by a moderate amount
  overall -- Hedges' g = 0.42 [0.34, 0.50] across 238 effects in 59 studies
  (Brunmair & Richter 2019), 0.29 after trim-and-fill -- but the sign and size
  depend on the material: paintings 0.67, maths 0.34, expository text 0.21
  (not significant), words -0.39 (blocking better). In the one large classroom
  trial, a preregistered cluster RCT of 54 seventh-grade maths classes
  (787 students), interleaved practice over four months raised an unannounced
  test one month later from 38 to 61 percent, d = 0.83 (Rohrer et al. 2020).
  Practical rule: interleave when the skill is choosing between similar
  categories or problem types, after a short blocked introduction to each and
  with corrective feedback; do not interleave word lists; expect it to feel
  harder and take longer.
reasoning: >
  Brunmair & Richter ran a multilevel random-effects meta-analysis on 59
  studies, 238 effect sizes nested in 158 samples. Overall g = 0.42 with high
  between-study heterogeneity (I-squared 77.3 percent), which is the reason the
  material breakdown, not the headline, is the usable output. Their Table 2:
  paintings g 0.67 (k 70), naturalistic photographs 0.35 (k 19), artificial
  pictures 0.31 (k 63), expository texts 0.21 (k 25, p .119), mathematical
  tasks 0.34 (k 45, p .005), words -0.39 (k 13, p .005), tastes 0.57 (k 3,
  n.s.). Meta-regression: stronger effects for material more similar between
  categories, less similar within, and more complex. Retention interval did
  not moderate the effect in their regression. Publication bias: trim-and-fill
  on independent effects gave g = 0.29 [0.20, 0.38] with 23 studies imputed,
  but per-material analyses found bias only for artificial pictures. Their own
  discussion is more cautious than the maths row suggests: they say they are
  "reluctant to recommend interleaving for learning materials such as
  mathematical tasks, expository texts, grammar rules, foreign languages or
  words", and that most studies used university students and visual material.
  .
  Rohrer, Dedrick, Hartwig & Cheung (2020) is the strongest single test for
  maths and partly answers that reluctance: preregistered, cluster randomised
  by class, 54 classes, 787 students, a positive effect for each of the 15 teachers,
  61 versus 38 percent on an unannounced test one month after an interleaved
  review, d = 0.83. Their own caveats bound it: (1) interleaved practice took
  more time and was not measured per unit time; (2) the benefit may be smaller
  at short test delays; (3) it may need a small amount of blocked practice
  first; (4) every interleaved-maths study gave corrective feedback, which may
  be a necessary ingredient. Interleaving also guarantees spacing of each skill
  across assignments and forces retrieval of which method to use, so the trial
  measures the package, not interleaving in isolation.
  .
  Why contested: the meta-analysis authors and the classroom trial point in
  different directions for maths, and the words result runs against the
  general advice to "mix it up". The direction is material-conditional, and
  any learning module that applies interleaving as a universal default is
  outside what the evidence supports.
---

# learning-habits/interleaving-similarity-bounded-070 -- 섞어서 연습하기(인터리빙): 재료에 따라 갈린다

**한 줄 그림:** 비슷해서 헷갈리는 종류를 구분하는 연습이면 섞어서 하고, 단어 목록이면 섞지 않는다.

## What the evidence says

Interleaving means practising several categories or problem types in a mixed
order instead of finishing one before starting the next. It is the third
technique next to spacing and retrieval practice, and the one with the most
conditional evidence.

The largest synthesis pools 238 effects from 59 studies and finds a moderate
average benefit. The average hides the real result: the benefit depends on
what is being learned.

| Material | Pooled g | Effects | Use |
|---|---:|---:|---|
| Paintings, complex natural images | 0.67 | 70 | interleave |
| Natural photographs | 0.35 | 19 | interleave |
| Artificial pictures, diagrams | 0.31 | 63 | interleave if categories are similar |
| Maths problem types | 0.34 | 45 | interleave after a short blocked start, with feedback |
| Expository text | 0.21 (n.s.) | 25 | no default |
| Words | -0.39 | 13 | block |

The common thread is discrimination. Mixing helps most when categories
resemble each other and the learner has to learn what separates them. It also
helps most when the mixed examples follow each other directly rather than
being spread out in time.

For maths, a preregistered trial in 54 school classes found a large benefit on
a test given a month later (61 versus 38 percent). The authors list the
limits themselves: interleaved work takes longer, the students had probably
seen each skill in a blocked lesson first, everyone got corrective feedback,
and mixing problem types also spaces each skill out and makes students recall
which method fits. The trial shows the package works in a real classroom. It
does not isolate mixing as the cause.

## How a learning module should use it

- Introduce a new category or problem type in a block, then mix it with the
  earlier ones in later practice.
- Mix when the learner's task is "which kind is this?" (art styles, species,
  problem types). The meta-analysis authors advise caution for grammar rules,
  foreign-language material and words.
- Give the answer or a worked solution after each mixed item.
- Do not mix vocabulary lists by category.
- Warn the learner that mixed practice feels harder and slower. That is
  expected, and is not a sign it is failing.

## 한국어 요약 (답변용)

- 인터리빙은 한 종류를 다 끝내고 다음으로 넘어가지 않고, 여러 종류를 섞어서 연습하는 방법이다.
- 59개 연구, 효과 크기 238개를 종합하면 평균적으로 중간 정도의 효과가 있다. 다만 재료에 따라 크게 갈린다.
  그림·사진처럼 서로 비슷해서 헷갈리는 범주는 효과가 크고, 수학 문제 유형은 작게나마 효과가 있다.
  설명문은 효과가 확인되지 않았고, 단어 목록은 오히려 묶어서 하는 편이 낫다.
- 핵심은 구분하기다. 비슷한 것들 사이의 차이를 익혀야 할 때 섞는다. 목록을 외울 때는 섞을 이유가 없다.
- 수학에서는 54개 학급을 무작위로 나눈 실험에서 한 달 뒤 시험 점수가 38%에서 61%로 올랐다. 다만
  새 유형은 먼저 따로 배운 뒤 섞었고, 매번 풀이를 확인했으며, 시간도 더 걸렸다.
- 섞어서 하면 더 어렵고 느리게 느껴진다. 실패 신호가 아니라 원래 그런 것이라고 미리 알려 준다.
- 섞을 때는 예시를 연달아 붙여서 보여 준다. 시간 간격을 두고 띄우는 것은 간격 반복이 할 일이지
  인터리빙의 몫이 아니다.
