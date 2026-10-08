---
# Habit-formation sprint 2026-10-06 (dispatch kw-habit-formation-2). The
# newer-data sequel to 003 (21-day myth) and 004 (weak meta base): what the
# post-2010 field data add to Lally's 66 days. Every figure was read at the
# primary's abstract or open full text on 2026-10-06; Lally 2010 at its
# abstract (publisher full text was not reachable this pass).
#
# expectation_bands is structured data for the lifekit routine module (see
# docs/kimwog-routine-habit-fields.md). The bands are ORDERINGS with their
# sources' own numbers attached; they are never a completion date.
id: learning-habits/habit-time-is-a-distribution-022
domain: learning-habits
grade: C (direction consistent across a daily-diary study, a weak-base meta-analysis, a nutrition RCT and two large field datasets; every day-count is bound to how its study measured habit)
lane: "@behavioral"
locale: universal
as_of: 2010-2024
contested: no
sources:
  - "https://doi.org/10.1002/ejsp.674"  # Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W., & Wardle, J. (2010). How are habits formed. European Journal of Social Psychology, 40(6), 998-1009 -- read at the abstract
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC11641623/"  # Singh, B., Murphy, A., Maher, C., & Smith, A. E. (2024). Time to form a habit: a systematic review and meta-analysis of health behaviour habit formation and its determinants. Healthcare, 12(23), 2488 estate-scrub:allow(cited author surname)
  - "https://doi.org/10.1073/pnas.2216115120"  # Buyalskaya, A., Ho, H., Milkman, K. L., Li, X., Duckworth, A. L., & Camerer, C. (2023). What can machine learning teach us about habit formation? Evidence from exercise and hygiene. PNAS, 120(17), e2216115120 -- read in full at PMC10151500
  - "https://doi.org/10.1111/bjhp.12504"  # Keller, J., Kwasnicka, D., Klaiber, P., Sichert, L., Lally, P., & Fleig, L. (2021). Habit formation following routine-based versus time-based cue planning: A randomized controlled trial. British Journal of Health Psychology (2021) -- read at the abstract
  - "learning-habits/21-day-myth-refuted-003"  # the myth refutation this item extends
  - "learning-habits/habit-meta-weak-base-004"  # the measurement caveat every number here inherits
  - "framework:GRADE -- Lally and Keller measure self-reported automaticity; Buyalskaya measures context-predictability in behavioural logs with no automaticity measure. Agreement on DIRECTION across those two kinds of measurement is the evidence; no single day-count is."
expectation_bands:
  - behaviour: simple-anchored
    examples: wash hands on leaving a room, a single act fired by a fixed event at work
    typical_range: weeks
    source_numbers: handwashing median 9-10 shifts (about two weeks)
    basis: Buyalskaya 2023
    basis_grade: C
  - behaviour: daily-health-behaviour
    examples: a chosen eating, drinking or activity behaviour done daily in the same context
    typical_range: about two months to plateau, very wide spread
    source_numbers: Lally median 66 days to 95% of plateau (39 of 96 good fits), individual 18-254; meta median 59-66, mean 106-154, range 4-335; Keller nutrition RCT median 59 days among habit formers
    basis: Lally 2010; Singh 2024; Keller 2021
    basis_grade: C
  - behaviour: effortful-exercise
    examples: gym attendance, a training session
    typical_range: months
    source_numbers: gym median 122-226 days to 95% of predictability asymptote (N 30110)
    basis: Buyalskaya 2023
    basis_grade: C
refraction_notes:
  - note: >
      NEVER A COMPLETION DATE. The routine module must not announce that a
      habit "is formed" on any day count (21, 66 or any other). Every
      number above is a median of a wide distribution, measured as a
      plateau, not a threshold, and in the gym data the median alone spans
      four to seven months. Speak the band (weeks / about two months /
      months) and the spread, never a day.
    grade: C
  - note: >
      HARDER BEHAVIOURS TAKE LONGER. The one ordering the data agree on:
      a small act tied to a fixed event (washing on exit) settles in weeks,
      a daily health behaviour in about two months with a long tail, and
      going to the gym in months. When a user expects a training routine
      to feel automatic in three weeks, that expectation is the problem,
      not the user.
    grade: C
  - note: >
      THE TWO KINDS OF "HABIT" DIFFER. Diary studies ask people how
      automatic it feels; the field data infer habit from how predictable
      behaviour is from context. The Buyalskaya authors say plainly that
      other, non-automatic mechanisms could produce the same predictability.
      Do not add their months to Lally's days as if they measured one thing.
    grade: D
claim: >
  Time to form a habit is a wide, behaviour-dependent distribution, not a
  date. Lally et al. (2010) put the median at 66 days to reach 95% of a fitted
  automaticity plateau (39 of 96 volunteers with good curve fit, individual
  18-254 days), the 2024 meta-analysis gives medians of 59-66 days and means
  of 106-154 across only four studies that measured duration, and a nutrition
  RCT found a median of 59 days among those who formed the habit. Large field
  logs separate behaviours sharply: in Buyalskaya et al. (2023), hospital
  handwashing became predictable from context in a median of 9-10 shifts,
  while gym attendance in 30,110 members took a median of 122-226 days. Speak
  a band (weeks for small anchored acts, about two months for a daily health
  behaviour, months for exercise) with its spread; never a completion day.
reasoning: >
  Four independent sources agree on two things: no fixed number, and harder
  or less cue-bound behaviours take longer. They disagree on how habit is
  measured -- self-reported automaticity in Lally and Keller, context
  predictability in Buyalskaya -- so the numbers are not interchangeable and
  are carried separately in expectation_bands. Grade held at the
  observational band: the meta-analysis underneath is weak (004), Lally is a
  single 84-day student-volunteer study with values beyond day 84
  extrapolated, and the field datasets have no automaticity measure. The
  ordering simple < daily health behaviour < gym is the most stable part and
  is what the routine module should use.
---

# learning-habits/habit-time-is-a-distribution-022 -- 습관이 자리 잡는 시간은 날짜가 아니라 분포

**한 줄 그림:** 손 씻기 같은 작은 행동은 몇 주, 매일 하는 건강 행동은 두 달 남짓, 헬스장 가기는
몇 달. 그리고 사람마다 차이가 아주 크다.

The 21-day figure is gone (003). The replacement is not "66 days". Lally's 66
is the median point where automaticity stopped climbing, among the people
whose curves could be fitted at all, in a 12-week study. The 2024 review that
gathered everything since found only four studies that measured duration
directly, and a weak base under them (004).

What the newer data add is the shape across behaviours. A small act tied to a
fixed moment -- washing hands on leaving a patient room -- became predictable
from context in about two weeks of shifts. Going to the gym, across thirty
thousand members over four years, took four to seven months by the same
method. A randomised nutrition study, where people tied a food behaviour to a
routine or a clock time, landed at a median of 59 days for those who got
there.

These studies do not all measure the same thing. The diary studies ask how
automatic the behaviour feels; the field studies infer habit from how well
context predicts the behaviour, and their authors say other mechanisms could
produce that. The direction agrees; the day counts are not one ruler.

| Behaviour | Typical band | Numbers as the sources report them |
|---|---|---|
| Small act on a fixed cue | weeks | handwashing 9-10 shifts |
| Daily health behaviour | about two months, long tail | 66 (18-254); meta 59-66 median, 106-154 mean; nutrition RCT 59 |
| Exercise / gym | months | 122-226 days median |

## 한국어 요약 (답변용)

- "21일이면 습관이 된다"는 근거가 없다. 그렇다고 "66일"이 정답인 것도 아니다. 66일은 한 연구에서
  자동성이 더 오르지 않게 된 시점의 중앙값이고, 사람에 따라 18일에서 254일까지 퍼져 있었다.
- 행동마다 다르다. 정해진 순간에 붙인 작은 행동은 몇 주, 매일 하는 건강 행동은 두 달 남짓, 헬스장
  출석은 몇 달(중앙값 약 4~7개월)이 걸렸다.
- 루틴 화면이나 답변에서 "오늘로 습관 완성" 같은 날짜를 선언하지 않는다. 구간과 개인차를 함께
  말한다.
- 운동 루틴이 3주 만에 자동으로 느껴지지 않는다고 실패한 게 아니다. 원래 몇 달 걸리는 쪽이다.
- 숫자는 연구마다 재는 방식이 달라(스스로 느끼는 자동성 vs 기록으로 본 예측 가능성) 서로 더하거나
  비교하지 않는다.
