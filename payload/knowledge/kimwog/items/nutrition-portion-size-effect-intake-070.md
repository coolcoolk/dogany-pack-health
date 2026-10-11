---
# Meal-prep / eating-out sprint 2026-10-06 (dispatch task kw-meal-prep). The
# evidence row under the two craft rows that follow it (071 meal prep, 072
# eating out, KR). It owns ONE finding: the amount served sets the amount
# eaten, and the body does not correct for it within the days measured. It does
# NOT own portion ESTIMATION (that is nutrition/portion-estimation-shape-
# ceiling-018) and it does not own logging units (020).
#
# meal_rules is structured data for a meal module (same posture as
# exercise/caution-severity-ladder-056 decision_ladder). Each rule names its
# own basis_grade and kind (evidence | convention); a convention is never
# spoken as a finding.
id: nutrition/portion-size-effect-intake-070
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2007-2015
contested: no
sources:
  - "https://doi.org/10.1002/14651858.CD011045.pub2"  # Hollands GJ, Shemilt I, Marteau TM, Jebb SA, Lewis HB, Wei Y, Higgins JPT, Ogilvie D. Portion, package or tableware size for changing selection and consumption of food, alcohol and tobacco. Cochrane Database Syst Rev 2015;(9):CD011045. 72 RCTs to July 2013; consumption SMD 0.38 (95% CI 0.29 to 0.46), moderate-quality evidence; read from the Cochrane summary page 2026-10-06
  - "https://doi.org/10.1509/jm.12.0303"  # Zlatevska N, Dubelaar C, Holden SS. Sizing up the effect of portion size on consumption: a meta-analytic review. J Marketing 2014;78(3):140-154. Doubling portion -> about 35 percent more eaten; curvilinear; weaker in women, overweight people, non-snack foods and attentive eating. Abstract read at the UTS repository record
  - "https://pubmed.ncbi.nlm.nih.gov/17557991/"  # Rolls BJ, Roe LS, Meengs JS. The effect of large portion sizes on energy intake is sustained for 11 days. Obesity 2007;15(6):1535-1543. +50 percent portions -> +423 kcal/day, no significant decline across 11 days. Abstract figures via index record; full text not read
  - "source:nutrition/portion-estimation-shape-ceiling-018 -- the other half: people cannot see the portion accurately, and this item says the portion steers intake anyway"
  - "source:nutrition/self-report-underreporting-007 -- why a larger-portion day is also a worse-logged day"
  - "framework:GRADE -- RCT base, rated moderate by Cochrane for study limitations; most trials are single-meal or few-day laboratory exposures, so the direction is firm and the magnitude in free living is not"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
meal_rules:
  - rule: serve-decides
    when: any planned meal in a fat-loss phase
    action: decide the portion before eating (plate it, pack it, or split it) instead of eating from a pot, a family-style dish or a large package
    basis: Hollands 2015; Zlatevska 2014
    basis_grade: B
    kind: evidence
  - rule: no-next-day-compensation
    when: a meal or day was served large
    action: do not assume the next meals self-correct; the excess persisted across 11 measured days
    basis: Rolls 2007
    basis_grade: B
    kind: evidence
  - rule: tableware-not-a-lever
    when: user asks whether smaller plates alone will do it
    action: do not promise it; tableware-only evidence is too thin to rely on, the served amount is the lever
    basis: Hollands 2015 (tableware evidence rated very low)
    basis_grade: C
    kind: evidence
  - rule: no-percent-promise
    when: speaking magnitude
    action: give the direction and the order (more served, more eaten, about a third more for a doubling in lab studies); never promise a kcal saving for this user
    basis: Zlatevska 2014 moderators; lab exposures
    basis_grade: C
    kind: evidence
refraction_notes:
  - axis: primary_goal
    note: >
      For a fat-loss goal this is the most actionable row in the domain: the
      served amount is set once, before appetite and estimation error get a
      vote. For a gain goal the same finding runs the other way -- serving more
      is a legitimate way to raise intake -- and the item should be read that
      way rather than as a warning.
    grade: B
  - note: >
      THE MAGNITUDE DOES NOT TRANSFER TO THIS USER. The 35 percent per doubling
      and the 423 kcal per day are laboratory and controlled-feeding figures;
      the effect is weaker in women, in overweight people, for main meals and
      when attention is on the food. Say the direction with confidence and the
      number only as the study's number.
    grade: C
claim: >
  The amount of food served sets the amount eaten. Across 72 randomised
  trials, larger portions, packages and individual units increased consumption
  with a small-to-moderate standardised effect (SMD 0.38), rated moderate-
  quality evidence by Cochrane; a separate meta-analysis puts a doubling of
  portion size at about 35 percent more eaten on average, with the effect
  flattening as portions grow and weaker in women, in overweight people, for
  non-snack foods and when attention is on the food. The effect is not
  compensated within the measured horizon: serving everything 50 percent
  larger raised intake by about 423 kcal a day and the increase did not fade
  over 11 days. Tableware size on its own is not a demonstrated lever. The
  operational reading for a fat-loss phase: the decision that matters is the
  serving decision, made before the meal, not a promise to stop early.
reasoning: >
  This is the strongest evidence base available for a meal-handling rule:
  randomised exposures, two independent syntheses (a Cochrane review and a
  marketing-science meta-analysis) agreeing on direction, and a multi-day
  feeding study closing the obvious objection that people compensate later.
  It stops short of the top band because the trials are mostly short
  laboratory or cafeteria exposures, Cochrane downgraded for study
  limitations, and no trial tests a free-living person deliberately
  pre-portioning for weeks. Not contested: nobody located disputes the
  direction. What is uncertain is magnitude, and that is carried in a graded
  note rather than in the letter. Note the interaction with the logging rows:
  a large portion is both eaten more of and estimated worse
  (nutrition/portion-estimation-shape-ceiling-018), so the large-portion day is
  the day the log is least trustworthy.
---

# nutrition/portion-size-effect-intake-070 -- the serving decides

**One line:** whatever is on the plate is roughly what gets eaten, and the next
day does not pay it back.

Seventy-two randomised trials, pooled by Cochrane, find that bigger portions,
packages and units make people eat more. A separate meta-analysis puts a
doubled portion at about a third more eaten. The effect gets smaller as
portions get huge, and it is weaker for women, for people already carrying
more weight, for main meals rather than snacks, and when people are paying
attention to what they eat.

The objection everyone raises -- "I'll just eat less tomorrow" -- was tested.
Serving every food half again as large for eleven days raised intake by a
little over four hundred kcal a day, and it did not fade.

What did not hold up: smaller plates and glasses on their own. The evidence
for tableware alone is too thin to promise anything. The lever is the amount
served.

| Rule | Action | Kind |
|---|---|---|
| serve-decides | portion before eating; no eating from the pot or shared platter unplated | evidence |
| no-next-day-compensation | do not plan on tomorrow correcting today | evidence |
| tableware-not-a-lever | do not sell small plates as the fix | evidence |
| no-percent-promise | direction yes, kcal saving for this user no | evidence |

## 한국어 요약 (답변용)

- 담긴 만큼 먹는다. 양을 크게 주면 더 먹는다는 건 무작위 시험 72건을 묶은 코크란 리뷰가 확인한
  방향이다. 양을 두 배로 하면 평균 3분의 1쯤 더 먹는다는 메타분석도 있다(실험실 수치라 개인에게
  그대로 옮기지 않는다).
- "내일 덜 먹으면 된다"는 기대는 시험됐다. 모든 음식을 1.5배로 준 11일 동안 하루 섭취가 약
  420 kcal 늘었고 줄어들지 않았다.
- 그래서 감량기에 중요한 건 먹다가 멈추는 의지가 아니라 먹기 전에 양을 정하는 일이다. 덜어서
  먹고, 냄비·큰 접시·대용량 봉지에서 바로 먹지 않는다.
- 작은 그릇만 바꾸는 방법은 근거가 너무 약해서 약속하지 않는다.
- 증량기라면 같은 결과를 반대로 쓴다. 많이 담는 것이 섭취를 올리는 정당한 방법이다.
