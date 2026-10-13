---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (spending-tracking sprint, dispatch
# kw-spending-tracking). Every source below was resolved and read during
# authoring; no citation is reconstructed from memory. Beshears et al. 2021
# read at full text (PMC8341022: results, Tables 4-5, limitations); Dai et al.
# 2014 read at the abstract on the authors' posted article PDF.
#
# The temporal-landmark item. Answers "WHEN should the weekly review offer a
# new saving or spending plan" -- not "how often to review" (026 holds that).
id: spending-saving/fresh-start-framing-small-absolute-072
domain: spending-saving
grade: C (one randomised field experiment inside an employer retirement plan, small absolute effect, plus archival correlational studies)
lane: "@household-behavioral"
locale: US
as_of: 2013-2014 (field data), 2021 (published)
contested: no
sources:
  - "Beshears, J., Dai, H., Milkman, K. L. and Benartzi, S. (2021). Using Fresh Starts to Nudge Increased Retirement Savings. Organizational Behavior and Human Decision Processes 167, 72-87. https://doi.org/10.1016/j.obhdp.2021.06.005 (full text read at https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8341022/)"
  - "Dai, H., Milkman, K. L. and Riis, J. (2014). The Fresh Start Effect: Temporal Landmarks Motivate Aspirational Behavior. Management Science 60(10), 2563-2582. https://doi.org/10.1287/mnsc.2014.1901 (abstract read at the authors' posted copy, https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)"
  - "source:spending-saving/automation-defaults-dominate-intention-006 -- why the offer should be to SCHEDULE an automatic change, not to try harder from the landmark on"
  - "source:learning-habits/lapse-is-not-a-reset-015 -- the opposite hazard: a landmark used to wipe a record rather than to start a plan"
nudge_rules:
  - rule: offer-at-a-landmark
    direction: when the review proposes a new saving or spending plan, offer to start it at a named landmark (start of month, start of a season, the user's birthday) rather than only "from now"
    basis: fresh-start-framed delayed option take-up +1.4 pp on a 2.6 percent base, without lowering immediate take-up
    basis_grade: C
  - rule: label-it-as-a-start
    direction: the landmark must be framed as a new beginning; naming an ordinary date or an unrelated holiday is not the same treatment
    basis: placebo-holiday framing did not produce the effect; fresh start vs placebo +1.7 to 1.8 pp
    basis_grade: C
  - rule: schedule-not-resolve
    direction: the thing offered at the landmark is a scheduled, automatic change (a transfer that starts on that date), not a resolution to behave differently
    basis: the tested object was a pre-committed future contribution increase; see 006
    basis_grade: C
  - rule: never-reset-the-ledger
    direction: a landmark starts a plan; it never deletes, zeroes or "forgives" past ledger rows or past-period totals
    basis: the record is the instrument (027); learning-habits/lapse-is-not-a-reset-015
    basis_grade: D
  - rule: new-year-not-special
    direction: do not treat 1 January as the strongest landmark; in the field experiment New Year framing did not produce a noticeable increase
    basis: Beshears et al. limitations section
    basis_grade: C
refraction_notes:
  - note: >
      THE ABSOLUTE EFFECT IS TINY. Take-up of the delayed option went from 2.6
      percent to about 4 percent of employees (+1.3 to 1.4 percentage points).
      The headline "50 percent increase" is relative to a very small base. The
      average contribution rate over November to June rose by about 0.17 to 0.19
      percentage points of pay. Quote the absolute numbers or none.
    grade: C
  - note: >
      EMPLOYER-PLAN ARCHITECTURE. The experiment ran inside US university
      retirement plans, where a mailed offer changes a payroll contribution with
      one action. Checklist trigger (7) applies to a self-directed Korean
      account. The direction (a labelled landmark makes a scheduled start
      slightly more attractive) is plausible to transfer; the size is not.
    grade: C
  - note: >
      THE 2014 FRESH START EFFECT IS ARCHIVAL AND CORRELATIONAL. Diet searches,
      gym visits and goal commitments rise after landmarks; that shows when
      people already act, not that prompting at a landmark causes anything. The
      2021 field experiment is the only causal test located for money.
    grade: C
claim: >
  Offering a future saving increase as starting at a "fresh start" date makes
  a small number of extra people take it, without taking anyone away from
  starting now. Beshears, Dai, Milkman and Benartzi mailed 6,082 university
  employees an offer to raise their retirement contributions either
  immediately or at a future date two to six months out. Describing that future
  date as a fresh start (the recipient's birthday, the first day of spring)
  rather than simply as a number of months away increased take-up of the
  delayed option by 1.3 to 1.4 percentage points over 2.6 percent in the
  control framing, and did not reduce take-up of the immediate option. Against
  a placebo framing that named a holiday that is not a fresh start, the effect
  was 1.7 to 1.8 percentage points. Average contributions over the following
  eight months rose by about 0.17 to 0.19 percentage points of pay. New Year
  framing, which the authors expected to be strongest, did not produce a
  noticeable increase. The motivating archival work (Dai, Milkman and Riis
  2014) found that diet searches, gym visits and goal commitments rise after
  temporal landmarks such as the start of a week, month, year, semester, a
  birthday or a holiday, which the authors interpret as landmarks opening new
  mental accounting periods.
reasoning: >
  Graded at the observational band. The 2021 study is randomised and well
  reported, but it is one field experiment, the absolute effect is about one
  percentage point, it runs inside employer-plan architecture (trigger 7), and
  the archival evidence underneath it is correlational. It ships because a
  weekly review module constantly faces a timing choice -- when to propose a
  new plan -- and this is the only located money evidence on that choice. Two
  readings are worth separating. The useful one: when the review proposes a
  change, offering a labelled landmark start alongside "now" costs nothing
  measurable and gains a little, and the offer should be to schedule an
  automatic change because that is what was tested and because item 006 shows
  automatic saving dominates intended saving. The harmful one, explicitly
  refused here: using a landmark to declare the past period "doesn't count."
  The mental-accounting-period mechanism the authors propose works by
  relegating past imperfections to a previous period; for a ledger, that
  relegation must happen in the user's head, never in the data. Past rows are
  the instrument (027) and resetting them would destroy the only record the
  next review has.
---

# spending-saving/fresh-start-framing-small-absolute-072 -- 새 계획은 '새 출발' 날짜에 맞춰 제안한다

**한 줄 그림:** 저축을 늘리자는 제안을 "다음 달 1일부터", "생일부터"처럼 새 출발 날짜에 맞춰 하면 받아들이는
사람이 조금 늘었다. 다만 그 '조금'은 1%p 정도다.

University employees were mailed an offer: raise your retirement contribution
now, or schedule the raise for a date a few months away. For some, the future
date was described as a fresh start -- your birthday, the first day of spring.
For others it was just "in N months."

The fresh-start wording made more people schedule the future raise: about 4
percent of employees instead of 2.6 percent. Nobody was pulled away from
raising contributions immediately. Naming an ordinary holiday instead of a
fresh start did not work, so it is the "new beginning" label that matters, not
merely having a date. Oddly, New Year's Day, the most obvious fresh start, did
not produce a noticeable effect.

Keep the size in view. A 50 percent relative increase on a 2.6 percent base is
about one more person in seventy. And this was a US employer retirement plan,
where accepting the offer is one action that changes a payroll deduction.

For a weekly review this answers a timing question, not a frequency question.
When the review is about to propose a new plan, it can offer a labelled start
date -- the first of next month, a new season, the user's birthday -- alongside
"starting now," and the thing offered should be a scheduled automatic change.
What a landmark must never do is wipe the slate in the ledger itself. The past
rows are the record the next review needs.

## Engine-readable rules

| Rule | Direction | Basis |
|---|---|---|
| offer-at-a-landmark | offer a labelled landmark start alongside "now" | +1.4 pp on 2.6 pct base, immediate take-up not reduced |
| label-it-as-a-start | frame the date as a new beginning; an ordinary date is not the treatment | placebo holiday framing did not work |
| schedule-not-resolve | the offer is a scheduled automatic change | tested object; see 006 |
| never-reset-the-ledger | a landmark never zeroes or hides past rows or totals | 027; learning-habits/015 |
| new-year-not-special | 1 January is not privileged | New Year framing no noticeable effect |

## 한국어 요약 (답변용)

- 저축액을 늘리거나 새 지출 계획을 제안할 때 "지금부터"만 말하지 말고 "다음 달 1일부터", "봄 시작부터",
  "생일부터"처럼 새 출발로 느껴지는 날짜를 함께 제안한다. 미국 대학 직원 6,082명 실험에서 이렇게 하면
  미래 시점 저축 증액을 고르는 사람이 2.6%에서 약 4%로 늘었고, 지금 바로 늘리는 사람은 줄지 않았다.
- 날짜에 '새 출발'이라는 의미를 붙여야 한다. 그냥 "3개월 뒤"나 아무 휴일 이름은 같은 효과가 없었다.
- 제안하는 것은 "그날부터 아껴 쓰겠다"는 다짐이 아니라 그날 시작되는 자동이체 예약이다.
- 1월 1일이 특별히 더 잘 먹히지는 않았다.
- 효과는 작다. 늘어난 건 1%p 남짓이다. "50% 증가" 같은 상대 수치로 말하지 않는다.
- 새 출발 날짜를 핑계로 지난 기록을 지우거나 "이번 달은 없던 걸로" 하지 않는다. 과거 기록은 다음
  리뷰가 쓸 유일한 자료다.
- 미국 직장 퇴직연금 안에서 한 실험이라, 한국에서 스스로 관리하는 통장에 그대로 같은 크기로 통한다고
  보지 않는다.
