---
# Home routines sprint 2026-10-06 (dispatch task kw-home-routines). Two
# levers a household routine surface actually has besides "do more chores":
# how the split is PERCEIVED by the people in it, and whether some of the load
# is bought off. Both are carried with their observational limits, because
# this is the area where newspaper retellings run furthest ahead of the
# papers ("money CAN buy happiness"). Companion rows: 070 (cognitive labour),
# 013 (time cost), 073 (routine rules).
id: home/chore-fairness-and-buying-time-071
domain: home
lane: "@household-labor"
grade: C (perceived unfairness of the split to oneself goes with lower relationship satisfaction; time-saving spending goes with higher life satisfaction); D (any specific split or spending amount as a target)
locale: universal
as_of: 2008-2017
contested: no
sources:
  - "https://doi.org/10.1371/journal.pone.0214204"  # Gillespie BJ, Peterson G, Lever J. Gendered perceptions of fairness in housework and shared expenses: implications for relationship satisfaction and sex frequency. PLoS ONE 2019;14(3):e0214204. 10,236 US respondents in different-gender cohabiting or married couples, online NBCNews.com survey 2008, cross-sectional, non-probability. Full text read at PMC (PMC6426245) 2026-10-06
  - "https://doi.org/10.1073/pnas.1706541114"  # Whillans AV, Dunn EW, Smeets P, Bekkers R, Norton MI. Buying time promotes happiness. PNAS 2017;114(32):8523-8527. PMID 28739889. Surveys n = 6,271 across US, Canada, Denmark, Netherlands plus a field experiment. Abstract read via Europe PMC 2026-10-06; publisher full text returned 403. The field experiment's size and design (reported in secondary coverage as 60 working adults in Vancouver, within-subjects, two weekends, 40 dollars each) were NOT read at source
  - "home/cognitive-labour-mental-load-070"  # within-warehouse: what a "fair split" leaves out if it counts only execution
  - "home/kr-household-labour-time-013"  # within-warehouse: the hours actually at stake in a Korean dual-income household
  - "relationships-communication/roster-without-chore-list-021"  # within-warehouse: no debt ledger, no streaks on shortfall surfaces
  - "framework:GRADE -- both findings are associations in large non-probability or multi-country surveys; the only causal design (a small within-subject field experiment) was not read at source. Observational band. No study located sets a fair split or a spending amount as a target, so any such number is bottom band."
refraction_notes:
  - note: >
      THE FELT SPLIT, NOT THE COUNTED SPLIT, IS WHAT WAS MEASURED. The survey
      asked whether the division was fair, not how many hours each person
      did. Unfairness to oneself (I do more than my fair share) predicted
      lower relationship satisfaction more consistently than unfairness to
      one's partner. A routine surface cannot compute fairness from a task
      log; it can only ask, and only the person can answer.
    grade: C
  - note: >
      MONEY FAIRNESS MATTERED MORE THAN CHORE FAIRNESS in the same sample:
      perceived unfairness to oneself in shared expenses had the strongest
      negative association with relationship satisfaction (housework
      self-unfairness was still significant, beta about -0.18). Housework is one
      fairness domain among several, not the master variable. About a
      quarter of respondents reported the housework split as unfair to
      themselves.
    grade: C
  - note: >
      FAIR IS NOT 50/50. No source located defines a fair split by
      proportion; the 2019 survey measured whether the split felt fair, not
      whether it was equal. Do not propose an equal split as the target or
      score a household against one. The household's own stated agreement is
      the target.
    grade: D
  - note: >
      BUYING TIME, READ AT ITS REAL STRENGTH. Across four countries, people
      who spent money on time-saving services reported greater life
      satisfaction, and a field experiment found working adults happier
      after a time-saving purchase than a material one. The survey half is
      cross-sectional (people who outsource may differ in other ways); the
      experimental half is small and was not read at source here. Carry it
      as "outsourcing a disliked chore is a legitimate lever when money is
      less scarce than time", not as a guaranteed happiness return.
    grade: C
  - note: >
      THE ROUTINE-SURFACE CONSEQUENCE. When a household's chore load is over
      its own stated capacity, the options are, in order: drop or lower the
      standard of a task (070, 072: many cleaning cadences have no health
      basis), redistribute it with whole-task ownership (070), or buy it
      off. Offer outsourcing as one option among these, never as advice to
      spend, and never on a surface that also shows spending shortfalls
      without the owner having asked.
    grade: D
  - note: >
      NO LEDGER. A running tally of who did more is exactly the debt ledger
      the owner's standing directive forbids (021), and the fairness finding
      gives no reason to build one: what predicted satisfaction was a
      perception, which a tally does not measure and can easily inflame.
    grade: D
  - note: >
      POPULATION. The fairness data are US, 2008, an online convenience
      sample with higher income and education than average; the authors flag
      their age. No Korean measurement of perceived housework fairness and
      relationship outcomes was located (GAPS.md).
    grade: D
claim: >
  Two findings give a household routine surface levers besides doing more.
  First, in a cross-sectional US survey of over 10,000 partnered adults,
  feeling that the housework split was unfair to oneself went with lower
  relationship satisfaction, and unfairness over shared expenses went with it
  more strongly; what was measured was the perception of fairness, not the
  counted hours. Second, across samples from four countries totalling 6,271
  people, spending money on time-saving services went with greater life
  satisfaction, and a field experiment found working adults happier after a
  time-saving purchase than after a material one. Neither finding supplies a
  target: no source defines a fair split by proportion or a right amount to
  spend. For a routine or task surface the consequences are to ask about
  fairness rather than compute it, to treat the household's own agreement as
  the target, and to offer dropping, reassigning or buying off a task as
  options when the load exceeds what the household says it can carry.
reasoning: >
  Gillespie and colleagues is large but a non-probability web sample from
  2008, cross-sectional, and the authors themselves list those limits; it
  supports an association and an ordering (self-unfairness over
  partner-unfairness, expenses over housework), not a dose. Whillans and
  colleagues pairs multi-country surveys with an experiment, which is why the
  claim is stated in the paper as causal; here it is carried at the
  observational band because only the abstract was read at source and the
  experimental arm is small. The routine-surface consequences are design
  reasoning on top of the two findings and of item 070, and are graded at the
  bottom band accordingly.
---

# home/chore-fairness-and-buying-time-071 -- 집안일 분담: 공평하다고 느끼는가, 시간을 살 수 있는가

**한 줄 그림:** 관계 만족도와 함께 간 건 몇 시간씩 나눴느냐가 아니라 내가 손해 본다고 느끼느냐였다.
그리고 시간을 아껴 주는 데 돈을 쓰는 사람들이 삶의 만족도가 더 높았다.

## What the engine reads from this row

| Input | Direction | Strength |
|---|---|---|
| feels the chore split is unfair to self | lower relationship satisfaction | large cross-sectional survey, US 2008 |
| feels shared expenses are unfair to self | stronger negative association than chores | same survey |
| equal split as a target | no source | none -- do not use |
| spends money on time-saving services | higher life satisfaction | multi-country surveys + small experiment |
| response when load > stated capacity | drop or lower standard -> reassign whole task -> buy off | design reasoning |
| tally of who did more | do not build | owner directive (021) |

## 한국어 요약 (답변용)

- 관계 만족도와 함께 움직인 건 집안일을 몇 시간씩 했느냐가 아니라 "내가 더 손해 본다"고 느끼느냐였다.
  미국 성인 1만여 명 설문에서 그랬다. 그래서 공평한지는 기록으로 계산하지 않고 당사자에게 묻는다.
- 같은 조사에서 생활비를 나누는 게 불공평하다는 느낌이 집안일보다 관계 만족도와 더 강하게 엮여
  있었다. 집안일은 공평함을 느끼는 여러 영역 중 하나일 뿐이다.
- 반반이 정답은 아니다. 공평한 비율을 정한 연구는 없다. 그 집이 스스로 합의한 방식이 기준이다.
- 청소 대행처럼 시간을 사는 데 돈을 쓰는 사람들은 삶의 만족도가 더 높았고, 작은 실험에서도 물건을
  산 주말보다 시간을 산 주말에 더 행복하다고 답했다. 다만 설문은 한 시점 비교이고 실험은 작다.
  "돈보다 시간이 더 부족하면 쓸 만한 선택지" 정도로 말한다.
- 집안일이 감당할 수 있는 양을 넘으면 순서대로 제안한다. 기준을 낮추거나 빼기, 일을 통째로 한
  사람에게 맡기기, 돈 주고 맡기기. 돈 쓰라는 조언으로 말하지 않는다.
- 누가 더 했는지 점수판은 만들지 않는다. 불만은 느낌에서 나오는데, 점수판은 그 느낌을 재지도
  못하고 오히려 키울 수 있다.
