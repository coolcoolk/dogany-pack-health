---
# Habit-formation sprint 2026-10-06 (dispatch kw-habit-formation-2). Cue and
# routine design for the lifekit routine module. The if-then plan's EFFECT
# SIZE is not restated here: task-management/implementation-intentions-
# effect-shrinks-003 owns it (d .65 superseded; .36 raw, .15 bias-corrected)
# and this item links it. What this item adds is which cue, how rigid, and
# what predicts the habit actually forming. Read at the abstracts / open
# full text on 2026-10-06.
#
# cue_rules is structured data for the routine module (see
# docs/kimwog-routine-habit-fields.md).
id: learning-habits/cue-design-repetition-over-rigidity-023
domain: learning-habits
grade: C (one RCT plus a weak-base review on cue type; one field experiment on rigidity; the repetition predictor is consistent but correlational)
lane: "@behavioral"
locale: universal
as_of: 2021-2025
contested: no
sources:
  - "task-management/implementation-intentions-effect-shrinks-003"  # if-then plans help; small, heterogeneous; contingent format, motivation and rehearsal raise the effect
  - "https://doi.org/10.1111/bjhp.12504"  # Keller et al. (2021), BJHP: routine-based vs time-based cue planning RCT, N 192, read at the abstract
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC11641623/"  # Singh et al. (2024), Healthcare 12(23):2488: cue type no difference; self-selected > assigned; morning stretching faster
  - "https://doi.org/10.1287/mnsc.2020.3706"  # Beshears, J., Lee, H. N., Milkman, K. L., Mislavsky, R., & Wisdom, J. (2021). Creating exercise habits using incentives: The trade-off between flexibility and routinization. Management Science, 67(7), 4139-4171 -- read at the abstract
  - "https://doi.org/10.1073/pnas.2216115120"  # Buyalskaya et al. (2023), PNAS: days since last visit the strongest (negative) gym predictor; day-of-week streak positive
  - "learning-habits/habit-time-is-a-distribution-022"
  - "framework:GRADE -- cue-type equivalence rests on one nutrition RCT (no between-condition difference) and the review's narrative synthesis; the flexibility result is one gym field experiment with incentives; transport to unpaid routines is inference."
cue_rules:
  - rule: cue-required
    action: every routine carries one concrete cue the user names, as an if-then (after or at X, do Y)
    basis: task-management/implementation-intentions-effect-shrinks-003
    basis_grade: B
  - rule: cue-type-either
    action: offer both an existing-routine anchor and a clock time; neither is the default on evidence
    basis: Keller 2021; Singh 2024
    basis_grade: C
  - rule: user-picks-behaviour
    action: the user chooses or edits the behaviour; the module does not assign it
    basis: Singh 2024 (self-selected more successful than assigned)
    basis_grade: C
  - rule: no-narrow-window
    action: do not require a tight time window for a routine to count; a done-on-the-day counts
    basis: Beshears 2021
    basis_grade: C
  - rule: repetition-is-the-lever
    action: success metric is repeated enactment on the cue, not perfection of timing
    basis: Keller 2021; Buyalskaya 2023
    basis_grade: C
refraction_notes:
  - note: >
      ANCHOR OR CLOCK, USER'S CHOICE. "After I brush my teeth" and "at 7 am"
      produced the same automaticity and plan enactment in the one RCT that
      compared them head to head, and the 2024 review found no difference
      either. A module that insists on one cue style is enforcing a
      preference, not a finding.
    grade: C
  - note: >
      RIGID WINDOWS BACKFIRED IN THE ONE TEST. Paying gym members only for
      visits inside a planned daily two-hour window produced FEWER visits
      than paying for any visit, during the programme and after it ended,
      and a larger post-programme drop at matched attendance. So a routine
      done at a different time still counts, and the module should never
      mark it missed for being outside a window.
    grade: C
  - note: >
      REPETITION, NOT THE PLAN, BUILDS THE HABIT. In the cue RCT the
      predictor of automaticity was repeatedly carrying out the plan on the
      cue; in the gym logs the strongest single predictor of attendance was
      days since the last visit. Both say the same practical thing: the
      next repetition matters more than the plan's wording.
    grade: C
  - note: >
      MORNING IS A SINGLE-STUDY HINT. The review reports one study in which
      stretching practised in the morning became habitual faster than in the
      evening. Mention it as an option for exercise-type routines; never
      as a rule.
    grade: D
claim: >
  Give each routine one concrete cue the user names, as an if-then plan
  (small but real effect; magnitude in task-management/003). The cue can be
  an existing routine ("after breakfast") or a clock time: a 192-person RCT
  (Keller et al. 2021) found no difference in automaticity or enactment, the
  2024 review agrees, and repeated enactment on the cue predicted
  automaticity. Let the user pick the behaviour (self-selected habits did
  better than assigned ones in the review). Do not make a narrow time window
  a condition: in a gym field experiment (Beshears et al. 2021) rewarding
  only visits inside a planned two-hour window gave fewer visits than
  rewarding any visit, during and after the programme. The lever the module
  controls is the next repetition, not the plan's precision.
reasoning: >
  Each rule rests on a different single source, which is why the item sits
  at the observational band despite including an RCT: cue-type equivalence is
  one nutrition trial plus a review of weak primaries (004); the flexibility
  result is one incentive experiment, and applying it to unpaid app routines
  is an inference labelled as such; the repetition predictor is
  correlational within trials and in field logs. The if-then plan rule
  inherits task-management/003's grade and is not re-derived here, to avoid
  two items carrying the same effect size.
---

# learning-habits/cue-design-repetition-over-rigidity-023 -- 신호는 구체적으로, 시간은 유연하게

**한 줄 그림:** "언제 할지"를 하나 정하되, 정해 둔 시간을 놓쳤다고 실패로 치지 않는다. 습관을 만드는
건 계획의 정밀함이 아니라 다음 한 번이다.

Tying a routine to a specific trigger helps; how much is owned by the
task-management item on if-then plans, which records that the famous effect
size was cut by its own authors. This item covers the design questions that
follow.

Which cue. An existing routine ("after I make coffee") and a clock time ("at
7:30") did equally well in the one trial that compared them directly, and the
2024 review found the same. Offer both and let the user choose.

Whose behaviour. Habits people chose themselves did better than assigned
ones in the review. The module proposes; the user picks.

How strict. In a large gym field experiment, rewarding visits only within a
planned two-hour window produced fewer visits than rewarding any visit, and
the routine group fell off more once the rewards stopped. Rigidity cost
attendance. Done at a different time is done.

What actually builds it. Repeating the behaviour on its cue predicted
automaticity in the cue trial; days since the last visit was the strongest
predictor of gym attendance in the field logs. Both point at the next
repetition. That is what the lapse rules in 024 protect.

## 한국어 요약 (답변용)

- 루틴마다 사용자가 직접 정한 신호 하나를 "~하면 ~한다" 형태로 붙인다. 효과는 있지만 작다(크기는
  task-management/003 참고).
- 신호는 "아침 먹고 나서" 같은 기존 일과에 붙여도, "7시 30분" 같은 시각으로 정해도 된다. 둘을
  직접 비교한 연구에서 차이가 없었다. 사용자가 고르게 한다.
- 무엇을 습관으로 할지는 사용자가 정한다. 스스로 고른 습관이 정해 준 습관보다 잘 됐다.
- 시간 창을 좁게 못 박지 않는다. 정한 두 시간 안에 간 것만 보상한 쪽이 아무 때나 간 것을
  보상한 쪽보다 덜 갔고, 끝난 뒤에도 더 많이 떨어졌다. 다른 시간에 했어도 한 것으로 친다.
- 습관을 만드는 건 반복이다. 계획 문구를 다듬는 것보다 다음 한 번을 하는 게 중요하다.
- 아침에 하면 더 빨리 붙는다는 결과는 연구 하나뿐이다. 선택지로만 말한다.
