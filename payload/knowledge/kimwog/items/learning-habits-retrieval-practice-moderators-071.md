---
# Learning-retention sprint 2026-10-06 (dispatch kw-learning-retention). 012
# carries the testing effect's size from ONE meta-analysis (Donoghue & Hattie,
# d=0.74, built on Dunlosky's reference list). This item adds two independent
# meta-analyses read at source in full text -- Rowland 2014 (lab, vs restudy)
# and Yang et al. 2021 (classroom, 222 studies, bias-corrected) -- and turns
# their moderator results into rules a learning module can apply. Adesope et
# al. 2017 is quoted ONLY as reported inside Yang 2021 and Latimier 2021
# (publisher full text not reached); it is marked secondary where used.
#
# session_rules is structured data: each rule names its basis and the grade of
# that basis. Effect sizes are copied from the papers, never derived.
id: learning-habits/retrieval-practice-moderators-071
domain: learning-habits
grade: A (direction and size, three independent meta-analyses converge near g=0.5 against restudy; individual moderators B to C)
lane: "@behavioral"
locale: universal
as_of: 2021
contested: no
sources:
  - "https://doi.org/10.1037/a0037559"
  - "Rowland, C. A. (2014). The effect of testing versus restudy on retention: A meta-analytic review of the testing effect. Psychological Bulletin, 140(6), 1432-1463."
  - "https://courseware.epfl.ch/assets/courseware/v1/fdde2f0aa590bf3b1324077a6bf1540c/asset-v1%3AEPFL%2BDEMO%2B2020%2Btype%40asset%2Bblock/Rowland2014-meta-analysis.pdf"  # author-uploaded copy of the online-first article, read at source
  - "https://doi.org/10.1037/bul0000309"
  - "Yang, C., Luo, L., Vadillo, M. A., Yu, R., & Shanks, D. R. (2021). Testing (quizzing) boosts classroom learning: A systematic and meta-analytic review. Psychological Bulletin, 147(4), 399-435."
  - "https://gwern.net/doc/psychology/spaced-repetition/2021-yang.pdf"  # online-first article PDF, read at source
  - "https://doi.org/10.3102/0034654316689306"  # Adesope, Trevisan & Sundararajan (2017), Review of Educational Research 87(3) -- figures quoted SECONDARY, as reported in Yang 2021 and Latimier 2021
  - "learning-habits/spaced-retrieval-meta-012"  # within-warehouse cross-ref: the single-meta anchor this item corroborates
  - "learning-habits/rep-is-attempt-then-check-016"  # within-warehouse cross-ref: the craft rep this evidence underwrites
  - "framework:GRADE -- three meta-analyses with different study pools (Rowland lab k=159; Yang classroom 573 effects, 48,478 students; Adesope 118 articles) agree on a medium effect against restudy; Yang's PEESE correction barely moves it (0.499 -> 0.475). Moderators are between-study comparisons and some disagree across metas (feedback, number of tests)."
session_rules:
  - rule: attempt recall before showing the answer
    effect: testing beats restudy, g 0.50 [0.42, 0.58] (Rowland, k 159); classroom quizzing g 0.499 [0.442, 0.557], PEESE-corrected 0.475 (Yang)
    basis: Rowland 2014; Yang 2021
    basis_grade: A
  - rule: show the correct answer after every attempt
    effect: with feedback g 0.73 vs without 0.39 (Rowland); classroom 0.537 vs 0.374 (Yang); Adesope found no difference (0.63 vs 0.60, secondary)
    basis: Rowland 2014; Yang 2021
    basis_grade: B
  - rule: without feedback, only test items the learner can mostly get right
    effect: no-feedback studies with initial success at or below 50 percent showed no benefit (g 0.03, n.s.); 51-75 percent g 0.29; above 75 percent g 0.56 (Rowland)
    basis: Rowland 2014
    basis_grade: B
  - rule: prefer producing the answer (cued recall, short answer) over recognising it
    effect: lab, matched exposure - cued recall 0.72 and free recall 0.81 vs recognition 0.36 (Rowland high-exposure set); classroom formats all positive, multiple choice 0.567 (Yang)
    basis: Rowland 2014; Yang 2021
    basis_grade: C
  - rule: quiz the same content on more than one occasion
    effect: more classroom test repetitions, larger gains (Yang meta-regression); Adesope found one test 0.70 vs more than one 0.51 (secondary) -- direction unsettled
    basis: Yang 2021
    basis_grade: C
  - rule: expect the benefit to show at delays of a day or more, not minutes
    effect: retention interval of at least 1 day g 0.69 vs under 1 day 0.41 (Rowland)
    basis: Rowland 2014
    basis_grade: B
  - rule: retrieval practice mainly helps the tested material
    effect: classroom, untested-but-related material g 0.321 vs tested 0.512 (Yang); Pan & Rickard 2018 found little effect on untested material (0.16, CI crosses zero, as reported in Yang)
    basis: Yang 2021
    basis_grade: B
refraction_notes:
  - note: >
      THE SIZE IS MEDIUM, NOT LARGE. Three independent pools put retrieval
      against restudy near g 0.5. The larger figures that circulate (0.74 in
      012, 0.93 against doing nothing in Adesope) come from different
      comparisons or a narrower pool. Quote "about half a standard deviation
      better than rereading" and keep the comparison named.
    grade: A
  - note: >
      FEEDBACK DECIDES WHETHER A HARD QUIZ HELPS. A test the learner mostly
      fails, with no answer shown afterwards, produced no measurable benefit
      in Rowland's split. A learning module that quizzes before teaching or
      quizzes at high difficulty must show the answer after each attempt.
    grade: B
  - note: >
      FACTS AND CONCEPTS, NOT EVERYTHING. Classroom effects held for facts
      (0.524), concepts (0.644) and application (0.453), and from middle
      school through university. Continuing (adult) education is unresolved:
      6 effects, CI crosses zero. Do not tell an adult learner the effect is
      established for their setting; say it is established for students.
    grade: B
claim: >
  Trying to recall material before seeing it again beats seeing it again by
  about half a standard deviation, and the figure is stable across independent
  pools: Hedges' g 0.50 [0.42, 0.58] against restudy in 159 laboratory effects
  (Rowland 2014) and g 0.499 [0.442, 0.557] for classroom quizzing across 573
  effects and 48,478 students, 0.475 after publication-bias correction (Yang
  et al. 2021). What changes the size: corrective feedback after the attempt
  (Rowland 0.73 with vs 0.39 without; Yang 0.537 vs 0.374); without feedback,
  initial success (no benefit at or below 50 percent correct, 0.56 above 75
  percent); producing rather than recognising the answer; and a final test a
  day or more later (0.69 vs 0.41 under a day). The benefit is mostly for the
  material that was tested (0.512) rather than related untested material
  (0.321). Practical rule: attempt, then show the answer, every time; keep
  no-feedback quizzes easy enough to mostly succeed; quiz again on a later
  day.
reasoning: >
  Rowland (2014): random-effects meta-analysis of 61 studies, 159 effect sizes,
  testing versus restudy only (so the control had equal exposure), published
  and unpublished. Overall g 0.50, heterogeneity high (I-squared 84). Feedback
  0.73 [0.61, 0.86] vs none 0.39 [0.29, 0.49]. Among no-feedback studies,
  initial test performance at or below 50 percent g 0.03 [-0.21, 0.27];
  51-75 percent 0.29; above 75 percent 0.56. Retention interval of at least a
  day 0.69 vs under a day 0.41. Initial test type in the full set: cued recall
  0.61, free recall 0.29, recognition 0.29 -- but Rowland flags that cued
  recall was confounded with more feedback and higher initial success, and in
  the high-exposure set (feedback or above 75 percent success) cued 0.72 and
  free 0.81 both exceed recognition 0.36. Unpublished studies gave smaller
  effects, which Rowland traces to their lacking feedback (89 percent) and
  lower initial success. A delayed-feedback advantage (1.38, k 6) is reported
  but flagged by Rowland as confounded with retention interval; it is not
  carried as a rule here.
  .
  Yang, Luo, Vadillo, Yu & Shanks (2021): 222 independent classroom studies,
  573 effects, 48,478 students. Overall 0.499; PEESE-corrected 0.475 [0.329,
  0.620]; funnel not significantly asymmetric; published 0.510 vs unpublished
  0.449, not significantly different. Feedback 0.537 vs 0.374; consistent
  quiz and final-test formats 0.531 vs inconsistent 0.399; tested 0.512 vs
  untested 0.321; more test repetitions associated with larger gains;
  elementary 0.328, middle 0.597, high school 0.655, university 0.486,
  continuing education 0.314 (k 6, n.s.). Against other elaborative
  strategies the advantage shrinks to 0.095, so the comparison condition must
  always be named.
  .
  Where the metas disagree, the rule is graded down rather than averaged:
  Adesope et al. (2017), as reported by Yang, found no feedback moderation
  (0.63 vs 0.60) and a larger effect for one test than for several (0.70 vs
  0.51). Hence feedback is B (two of three agree, mechanism clear) and
  repetition is C.
---

# learning-habits/retrieval-practice-moderators-071 -- 떠올려 보기 연습: 얼마나, 어떤 조건에서

**한 줄 그림:** 다시 읽는 것보다 먼저 떠올려 보는 쪽이 반 표준편차쯤 낫고, 정답 확인이 붙으면 더 낫다.

## The size, from three independent pools

| Source | Setting | Comparison | Effect |
|---|---|---|---|
| Rowland 2014 | lab, 159 effects | test vs restudy | g 0.50 |
| Yang et al. 2021 | classroom, 573 effects, 48,478 students | quizzing vs other conditions | g 0.499 (0.475 bias-corrected) |
| Adesope et al. 2017 (secondary) | 118 articles | testing vs all controls | g 0.61 |

The three syntheses use different study pools and land close together. This
is the most stable number in the learning-technique literature. It is a
medium effect, not a large one.

## What changes it

- **Feedback.** Showing the answer after the attempt raised the effect in two
  of the three syntheses (0.73 vs 0.39 in the lab; 0.537 vs 0.374 in
  classrooms). The third found no difference.
- **Success without feedback.** If no answer is shown and the learner gets
  half or fewer right, the lab data show no benefit at all. Above three
  quarters right, the effect is solid.
- **Producing over recognising.** Recalling or writing the answer beat
  picking it from options in the lab when exposure was matched. In classrooms
  every format helped, multiple choice included.
- **Delay.** The advantage is larger on tests a day or more later. On a test
  minutes later, rereading can look almost as good. That is why it feels as
  though rereading works.
- **What gets better.** Mostly the material that was tested. Related material
  that was not tested improves less.

## How a learning module should use it

1. Ask before showing: every review starts with an attempt.
2. Show the correct answer after every attempt, right or wrong.
3. If a mode does not show answers, keep it to items the learner usually gets
   right.
4. Prefer typed or spoken answers to choosing from options when the interface
   allows.
5. Quiz the same content again on a later day. Spacing is covered in
   learning-habits/spacing-schedule-shape-072.

## 한국어 요약 (답변용)

- 다시 읽기보다 먼저 떠올려 보기(셀프 테스트)가 효과 크기 약 0.5만큼 낫다. 실험실 연구 159건과 교실 연구
  573건(학생 4만 8천여 명)이 따로 보아도 비슷하게 나오고, 출판 편향을 보정해도 거의 줄지 않는다.
- 정답 확인이 붙으면 효과가 커진다(실험실 0.73 대 0.39, 교실 0.54 대 0.37). 한 종합 연구에서는 차이가
  없었다.
- 정답을 보여 주지 않는 퀴즈는 절반 이상 틀리면 효과가 사라진다. 정답 없이 할 거라면 대부분 맞힐
  수 있는 문제로 한다.
- 고르기보다 직접 떠올려 쓰기가 낫다. 다만 교실에서는 객관식도 효과가 있었다.
- 효과는 하루 이상 지난 시험에서 더 크게 보인다. 몇 분 뒤 시험에서는 다시 읽기도 비슷해 보여서,
  다시 읽기가 잘 된다는 착각이 생긴다.
- 주로 시험 본 내용이 남는다. 관련됐지만 퀴즈에 안 나온 내용은 덜 좋아진다.
- 성인 평생교육에서의 효과는 아직 연구가 적어 확정되지 않았다(6건). 학생 대상으로는 확립된 결과라고
  말한다.
