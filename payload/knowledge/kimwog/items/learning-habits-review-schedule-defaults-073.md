---
# Learning-retention sprint 2026-10-06 (dispatch kw-learning-retention). The
# engine-readable synthesis of 014 (gap from horizon), 070 (interleaving by
# material), 071 (retrieval moderators) and 072 (schedule shape), plus the
# craft rows 015 / 016 / 018 it must not contradict. Same posture as
# exercise/caution-severity-ladder-056: a routing rule, not a primary finding.
# Every row names the graded item it rests on; every product constant is
# labelled as a constant.
#
# horizon_gaps, review_steps and material_order are structured data for a
# learning module. Day values in horizon_gaps are COPIED from Cepeda et al.
# 2008 via 014 (measured optima, one experiment, trivia facts); they are a
# starting point, not a tested schedule. No program code is shipped.
id: learning-habits/review-schedule-defaults-073
domain: learning-habits
grade: D (synthesis rule over 014, 070, 071, 072; each row's basis keeps its own grade, the assembled schedule is untested)
lane: "@study-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "learning-habits/interval-from-retention-target-014"  # horizon -> gap, err long (Cepeda 2008)
  - "learning-habits/interleaving-similarity-bounded-070"  # mix by material
  - "learning-habits/retrieval-practice-moderators-071"  # attempt, then feedback
  - "learning-habits/spacing-schedule-shape-072"  # always space; equal gaps acceptable
  - "learning-habits/lapse-is-not-a-reset-015"  # late review is cheap
  - "learning-habits/rep-is-attempt-then-check-016"  # what counts as a rep
  - "learning-habits/reformulate-do-not-grind-017"  # repeated failure -> rebuild the item
  - "learning-habits/review-load-follows-intake-018"  # intake sets the load
  - "framework:GRADE -- each ingredient is graded in its own item (A to C). Nobody has tested the assembled practice a person runs (GAPS.md, @study-craft: ANY TRIAL OF ANY PRACTICE PROTOCOL). The gap table is one experiment's measured optima for two study sessions; the step rule for later reviews and the failure rule are product constants."
horizon_gaps:
  - horizon_days: 7
    first_gap_days: 1
    basis: learning-habits/interval-from-retention-target-014
    basis_grade: C
  - horizon_days: 35
    first_gap_days: 11
    basis: learning-habits/interval-from-retention-target-014
    basis_grade: C
  - horizon_days: 70
    first_gap_days: 21
    basis: learning-habits/interval-from-retention-target-014
    basis_grade: C
  - horizon_days: 350
    first_gap_days: 21
    basis: learning-habits/interval-from-retention-target-014
    basis_grade: C
review_steps:
  - step: every review is an attempt before the answer is shown
    value: required
    basis: learning-habits/retrieval-practice-moderators-071
    basis_grade: A
  - step: show the correct answer after every attempt
    value: required
    basis: learning-habits/retrieval-practice-moderators-071
    basis_grade: B
  - step: no two reviews of the same item in one sitting after it is first learned
    value: required
    basis: learning-habits/spacing-schedule-shape-072
    basis_grade: A
  - step: horizon unknown
    value: use the 35-day row and say it is an assumption; ask once
    basis: product constant
    basis_grade: D
  - step: horizon between rows
    value: use the next LONGER row (err long)
    basis: learning-habits/interval-from-retention-target-014
    basis_grade: C
  - step: later gaps after a successful review
    value: equal to the first gap is acceptable; growing gaps are a product choice, not an evidence requirement
    basis: learning-habits/spacing-schedule-shape-072
    basis_grade: B
  - step: failed review
    value: show the answer, re-test once later in the same session, restart that item's gap from the first gap
    basis: product constant (016 for the rep; no trial of failure handling)
    basis_grade: D
  - step: item fails repeatedly across sessions
    value: flag it for rewriting (split into one-retrieval items) instead of drilling; the lapse count that triggers the flag is a product constant
    basis: learning-habits/reformulate-do-not-grind-017
    basis_grade: D
  - step: missed review day
    value: review when next possible, most-overdue relative to its gap first; do not reset learned items; pause new intake until the queue clears
    basis: learning-habits/lapse-is-not-a-reset-015; learning-habits/review-load-follows-intake-018
    basis_grade: D
material_order:
  - material: categories that look alike (images, problem types)
    order: block the first encounter, then interleave in reviews
    basis: learning-habits/interleaving-similarity-bounded-070
    basis_grade: B
  - material: word and vocabulary lists
    order: do not interleave by category
    basis: learning-habits/interleaving-similarity-bounded-070
    basis_grade: C
  - material: expository text and everything else
    order: no ordering rule; spacing and retrieval still apply
    basis: learning-habits/interleaving-similarity-bounded-070
    basis_grade: C
refraction_notes:
  - note: >
      THE INGREDIENTS ARE EVIDENCE, THE RECIPE IS NOT. Attempt-before-answer,
      feedback and spacing are backed by meta-analyses. The day numbers come
      from one experiment on trivia facts, and the failure and missed-day
      rules are product constants. Speak them as the plan's defaults, never
      as a measured optimum for this learner.
    grade: D
  - note: >
      NAME THE HORIZON. The same material on a one-week horizon and a
      one-year horizon gets different gaps. If the user has not said when
      they need it, the module states the assumption it is using and asks
      once.
    grade: C
  - note: >
      SURFACE OUTCOMES ONLY. Every row here was measured on recall,
      classification or problem-type choice. None of it is evidence that a
      schedule produces speaking fluency, writing skill or deep understanding
      (013, 019). The module should not promise those.
    grade: C
claim: >
  A learning module can run a defensible default review schedule from four
  graded ingredients: (1) every review is a recall attempt before the answer
  is shown, and the answer is always shown afterwards (071); (2) the same item
  is never reviewed twice in one sitting after first learning, and the first
  gap is sized from the retention horizon -- about 1 day for a 1-week horizon,
  11 days for 5 weeks, 21 days for 10 weeks to a year, taking the longer row
  when in doubt (014); (3) later gaps may stay equal, because growing gaps
  were not shown to beat equal ones (072); (4) look-alike categories are
  introduced in a block and then mixed in review, while word lists are not
  mixed (070). The failure rule, the missed-day rule and the default horizon
  are product constants with no trial behind them.
reasoning: >
  Each structured row copies a value or direction from a graded item and
  carries that item's grade. horizon_gaps reproduces the measured optimal
  gaps that 014 reads from Cepeda et al. 2008 (1, 11, 21, 21 days for 7, 35,
  70, 350-day retention intervals, recall data; the same paper's
  recognition optima were shorter, 1, 7, 7 and 21 days, so a module that
  tests by recognition should not lengthen these); 014 records why those are the measured
  points rather than the fitted surface, and why erring long is cheaper. The
  attempt-then-feedback steps come from 071, where three meta-analyses put
  retrieval near g 0.5 over restudy and feedback raises it in two of three.
  "Equal later gaps are acceptable" comes from 072 (expanding vs uniform
  g 0.032, CI crossing zero). material_order comes from 070's per-material
  table. The failed-review and missed-day rows are written to agree with the
  craft rows already shipped: a rep is an attempt then a check (016), a lapse
  is not a reset (015), and an overloaded queue is fixed by cutting intake
  (018). The default horizon of 35 days is a product choice: it sits in the
  middle of the measured rows and errs long for short-horizon users, which is
  the cheaper direction.
---

# learning-habits/review-schedule-defaults-073 -- 학습 모듈용 복습 일정 기본값

**한 줄 그림:** 먼저 떠올리게 하고, 정답을 보여 주고, 기억해야 할 기간에 맞춰 날을 띄운다. 간격을 꼭 늘릴
필요는 없다.

## The defaults

| Field | Default | Rests on |
|---|---|---|
| Review form | recall attempt, then the answer | 071 |
| Same item twice in a sitting | no (after first learning) | 072 |
| First gap, 1-week horizon | 1 day | 014 |
| First gap, 5-week horizon | 11 days | 014 |
| First gap, 10-week to 1-year horizon | 21 days | 014 |
| Horizon between rows | take the longer row | 014 |
| Horizon unknown | 35-day row, stated as an assumption, ask once | product |
| Later gaps | equal is fine; growing is optional | 072 |
| Failed review | show answer, re-test later that session, restart the item's gap | product |
| Item keeps failing | rewrite it, do not drill it | 017 |
| Missed day | catch up, no reset, pause new items | 015, 018 |
| Look-alike categories | block first, then mix | 070 |
| Word lists | do not mix by category | 070 |

The ingredients are evidence-backed. The assembled schedule is not a tested
object. Nobody has run a trial of a whole practice protocol (see GAPS.md).

## 한국어 요약 (답변용)

- 복습은 항상 먼저 떠올려 보게 한 다음 정답을 보여 준다. 맞혔든 틀렸든 정답을 보여 준다.
- 처음 익힌 뒤에는 같은 항목을 한자리에서 두 번 복습하지 않는다.
- 첫 복습 간격은 언제까지 기억해야 하는지로 정한다. 1주 뒤면 1일, 5주 뒤면 11일, 10주에서 1년이면 21일
  정도다. 애매하면 긴 쪽을 고른다. 이 숫자는 잡학 퀴즈로 한 실험 하나에서 나온 값이라 출발점일 뿐이다.
- 기간을 모르면 5주 기준으로 하고, 그렇게 가정했다고 말한 뒤 한 번만 묻는다.
- 그다음 간격은 같게 두어도 된다. 간격을 점점 늘리는 방식이 더 낫다는 근거는 약하다.
- 틀린 항목은 정답을 보여 주고 같은 세션 뒤쪽에서 한 번 더 묻고, 그 항목의 간격은 처음부터 다시
  시작한다. 이것은 제품 규칙이다.
- 여러 번 계속 틀리는 항목은 더 반복하지 말고 하나만 떠올리면 되도록 쪼개서 다시 만든다.
- 하루 빠졌다고 처음부터 다시 하지 않는다. 밀린 복습을 하고, 밀린 게 정리될 때까지 새 항목을 줄인다.
- 비슷해서 헷갈리는 종류는 처음에는 따로 익히고 복습 때 섞는다. 단어 목록은 범주별로 섞지 않는다.
- 이 일정은 기억과 구분 능력을 기준으로 한 것이다. 말하기 실력이나 깊은 이해까지 보장한다고 말하지
  않는다.
