---
# Diet-adherence sprint 2026-10-07 (dispatch kw-nu-diet-adherence-structure).
# Two things travel together and must be kept apart: weekend EATING drift
# (real, measured, modest) and the weekend WEIGHT bump (real, small, and
# largely reversed by midweek in people who are losing). The weekly retro
# needs both: the first is a lever, the second is noise it must not
# misread. Grade held at the observational band; no Korean data.
id: nutrition/weekend-drift-073
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 2003-2020
contested: no
sources:
  - "https://doi.org/10.1038/oby.2008.320"  # Racette SB, Weiss EP, Schechtman KB, Steger-May K, Villareal DT, Obert KA, Holloszy JO. Influence of weekend lifestyle patterns on body weight. Obesity 2008;16(8):1826-1830. PMID 18551108 -- within a 1-year RCT (caloric restriction vs exercise), n=48 aged 50-60, 7 consecutive morning weights for 165 baseline and 437 intervention weeks; baseline weekend gain +0.06 kg/day (Fri-Mon), none on weekdays; during restriction weight loss stopped at weekends; Saturday intake higher, Sunday activity lower; diary and accelerometer checked against doubly labelled water
  - "https://doi.org/10.1038/oby.2003.130"  # Haines PS, Hama MY, Guilkey DK, Popkin BM. Weekend eating in the United States is linked with greater energy, fat, and alcohol intake. Obes Res 2003;11(8):945-949. PMID 12917498 -- CSFII 1994-1996, two recalls: +82 kcal per weekend day (Fri-Sun) vs Mon-Thu, +115 kcal at ages 19-50, higher share from fat and alcohol
  - "https://doi.org/10.1159/000356147"  # Orsama AL, Mattila E, Ermes M, van Gils M, Wansink B, Korhonen I. Weight rhythms. Obes Facts 2014;7(1):36-47. PMID 24504358 -- retrospective, n=80, 4,657 daily weights: highest Sunday-Monday, falling to Friday; compensation strongest in those who lost or maintained, weakest in slow gainers. (Co-author Wansink later had multiple papers retracted; Europe PMC lists no retraction, correction or expression of concern on this paper as of 2026-10-07, and the pattern is independently reproduced by Turicchi 2020)
  - "https://doi.org/10.1371/journal.pone.0232152"  # Turicchi J, O'Driscoll R, Horgan G, et al. PLoS One 2020;15(4):e0232152. PMID 32353079 -- NoHoW weight-loss-maintenance trial, smart-scale data, n=1,421 weekly analysis: within-week fluctuation 0.35 pct, weekend gain and weekday reduction; Christmas +1.35 pct not fully compensated in following months
  - "source:nutrition/self-monitoring-frequency-027 -- daily weights only mean something as a weekly pattern"
  - "source:nutrition/unlogged-day-not-zero-019 -- an unlogged weekend is missing data, not a light weekend"
  - "source:nutrition/adherence-rules-074 -- the weekly-retro rules that consume this item"
  - "source:nutrition/body-measure-reading-rules-029 -- (parallel v38 sprint) the noise bands and weekday-not-diet rule for the same Monday bump, on the body-line surface"
  - "source:nutrition/alcohol-training-recovery-dose-031 -- (parallel v38 sprint) weekend drinking as part of the weekend energy gap; dose bands and retro copy"
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      COMPARE LIKE DAYS. Body weight runs about 0.35 percent higher at the
      start of the week than at its end in large smart-scale data. A retro
      that compares Friday to Monday reads that swing as a gain. Compare the
      same weekday week to week, or weekly means.
    grade: C
  - note: >
      A MONDAY BUMP IS NOT A VERDICT. In people who are losing or maintaining,
      the weekend rise is largely reversed by midweek (Orsama 2014, Turicchi
      2020). Do not comment on Monday's weight alone.
    grade: C
  - note: >
      THE EATING DRIFT IS MODEST AND REAL. US national recalls show about 80
      kcal more per weekend day (about 115 at ages 19-50), and in a
      year-long restriction trial weight loss stopped on weekends. A
      deficit that holds Monday to Thursday and disappears Friday to Sunday
      is a plausible reason a plan stalls; it is a lever to look at, not a
      character flaw.
    grade: C
  - note: >
      THE NUMBERS ARE AMERICAN AND EUROPEAN. Size of drift, which days it
      falls on (Friday counts as weekend in the US data), and the role of
      alcohol are culture-bound. No Korean data was located (GAPS.md). Use
      the user's own logged weekday-weekend gap, not these figures.
    grade: D
  - note: >
      HOLIDAYS ARE THE BIGGER PROBLEM. The one large dataset that measured
      both found the Christmas rise (1.35 percent) larger than the weekly
      swing and not fully reversed months later. Korean holiday equivalents
      (명절) are untested.
    grade: C
claim: >
  Two weekly effects exist and must be read separately. Eating: adults eat
  more at weekends -- about 82 kcal more per weekend day in US national
  recall data, 115 kcal at ages 19 to 50 -- and in a year-long trial adults
  on caloric restriction lost weight on weekdays but stopped losing at
  weekends. Weight: daily scale readings rise from Saturday to Monday and
  fall through the week, a swing of about 0.35 percent of body weight in
  1,421 people with smart-scale data, and the rise is largely compensated by
  midweek in people who are losing or maintaining. Holiday rises are larger
  and less fully reversed. A weekly review must therefore compare like days
  or weekly means, and may use a measured weekday-weekend intake gap in the
  user's own log as a lever.
reasoning: >
  Four independent datasets (national recall, a trial with daily weights and
  doubly-labelled-water-checked intake, a retrospective scale cohort, and a
  large multi-country smart-scale trial) agree in direction, which earns the
  observational band. It stays there because none randomises anything about
  the weekend, the samples are American and European, and the trial with the
  clearest mechanism had 48 people aged 50 to 60. Orsama 2014 lists a
  co-author whose other work was retracted for research misconduct; the
  paper is kept because its finding is reproduced at scale by Turicchi 2020,
  and the figure quoted (0.35 percent) is Turicchi's, not Orsama's. The
  split between eating drift and weight bump is the engine-relevant point:
  the bump is partly water and gut content from the eating drift and is
  self-reversing in people on track, so it must never trigger feedback by
  itself; the eating drift is the thing the user can change, and it should
  be read from the user's own log rather than assumed from US averages.
---

# nutrition/weekend-drift-073 -- 주말 드리프트

주말에는 더 먹는다. 미국 전국 식사 조사에서 금~일요일 하루 섭취가 평일보다 평균 82 kcal
많았고, 19~50세에서는 115 kcal였다. 1년짜리 감량 시험에서는 평일에는 빠지던 체중이 주말에는
멈췄다. 토요일에 더 먹고 일요일에 덜 움직인 탓이었다.

체중계 숫자도 주간 리듬을 탄다. 스마트 체중계 자료 1,421명을 분석한 결과 주말에 오르고 평일에
내려가는 폭이 체중의 약 0.35%였다. 감량하거나 유지하는 사람에게서는 그 상승분이 주 중반이면
대부분 되돌아갔다. 그러니 월요일 아침 체중 하나로 "지난주 망했다"고 읽으면 안 된다.

둘은 따로 읽어야 한다. 월요일 체중이 튀는 건 대체로 노이즈이고, 평일과 주말의 섭취 차이는
사용자가 바꿀 수 있는 지점이다. 단, 이 숫자들은 미국과 유럽 자료다. 한국 자료는 찾지 못했다.
그래서 평균값 대신 사용자 본인 기록에 나타난 평일-주말 차이를 쓴다. 명절처럼 긴 연휴는 주말보다
영향이 크고 잘 회복되지 않았다(서양 자료의 크리스마스 기준).

## 한국어 요약 (답변용)

- 주간 회고에서 체중은 같은 요일끼리(월요일 vs 지난 월요일) 비교하거나 주 평균으로 비교한다.
  금요일과 월요일을 비교하지 않는다.
- 월요일 체중이 오른 것만으로 피드백하지 않는다. 주말에 0.3~0.4% 정도 오르는 건 흔하고,
  잘 가고 있는 사람은 주 중반에 대부분 돌아온다.
- 기록에 평일과 주말 섭취 차이가 실제로 보이면 그것을 주간 회고의 조정 포인트로 짚는다. 기록이
  없는 주말은 '적게 먹은 주말'이 아니라 '모르는 주말'이다.
- 미국 평균(주말 하루 +80 kcal)을 사용자에게 그대로 적용하지 않는다. 본인 기록 숫자를 쓴다.
- 명절 같은 연휴는 주말보다 체중 영향이 크고 오래 남을 수 있다. 연휴 전후로 미리 짚어 준다.
