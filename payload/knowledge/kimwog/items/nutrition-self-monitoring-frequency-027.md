---
# Diet-adherence sprint 2026-10-07 (dispatch kw-nu-diet-adherence-structure).
# "Log every day, weigh every day" is the most consistent association in
# behavioural weight-loss research and also one of its weakest causal
# claims: the people who keep logging are the people who are succeeding.
# Filed so the engine can use frequency as a SIGNAL and a gentle default
# without speaking it as a dose that causes loss, and with the
# self-weighing harm literature next to it.
id: nutrition/self-monitoring-frequency-027
domain: nutrition
lane: "@obs-inferential"
grade: C (consistent association; one bundled RCT for daily weighing; no established dose)
locale: universal
as_of: 2011-2021
contested: no
sources:
  - "https://doi.org/10.1016/j.jada.2010.10.008"  # Burke LE, Wang J, Sevick MA. Self-monitoring in weight loss: a systematic review of the literature. J Am Diet Assoc 2011;111(1):92-102. PMID 21185970 -- 22 studies 1993-2009; association consistent, level of evidence weak (homogeneous samples, self-reported adherence); calls for studies establishing the required dose
  - "https://doi.org/10.1002/oby.23088"  # Patel ML, Wakayama LN, Bennett GG. Obesity 2021;29(3):478-499. PMID 33624440 -- 39 RCTs 2009-2019, 67 digital self-monitoring arms; greater self-monitoring linked to weight loss in 74 pct of occurrences; few arms reached engagement on 75 pct of days or more
  - "https://doi.org/10.1002/oby.22382"  # Harvey J, Krukowski R, Priest J, West D. Log often, lose more. Obesity 2019;27(3):380-384. PMID 30801989 -- n=142, 24-week online programme; 23.2 min/day logging in month 1, 14.6 in month 6; minutes did not separate success, log-ins per day did (2.4 vs 1.6 for >=5 pct loss)
  - "https://doi.org/10.1002/oby.20396"  # Steinberg DM, Tate DF, Bennett GG, Ennett S, Samuel-Hodge C, Ward DS. Obesity 2013;21(9):1789-1797. PMID 23512320 -- RCT n=91: daily self-weighing on a smart scale + weight graph + weekly tailored e-mail vs delayed control; -6.55 vs -0.35 pct at 6 months (ITT); weighed 6.1 days/week; daily weighing perceived positively
  - "https://doi.org/10.1002/oby.20946"  # Zheng Y, Klem ML, Sereika SM, Danford CA, Ewing LJ, Burke LE. Self-weighing in weight management: a systematic literature review. Obesity 2015;23(2):256-265. PMID 25521523 -- 17 longitudinal studies, treatment-seeking adults: regular self-weighing associated with more loss and not with depression or anxiety
  - "https://doi.org/10.1007/s13679-015-0142-2"  # Pacanowski CR, Linde JA, Neumark-Sztainer D. Self-weighing: helpful or harmful for psychological well-being? Curr Obes Rep 2015;4(1):65-72. PMID 26627092 -- 20 studies; negative associations concentrated in women and younger people, null or positive in overweight treatment-seeking adults
  - "source:nutrition/unlogged-day-not-zero-019 -- what to do with the gaps frequency leaves"
  - "source:nutrition/self-report-underreporting-007 -- more logging does not make the logged number true"
  - "source:nutrition/weekend-drift-073 -- why daily weights must be read as a weekly pattern, not day to day"
  - "source:nutrition/adherence-rules-074 -- the engine-readable rules that consume this item"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      FREQUENCY IS A SIGNAL BEFORE IT IS A LEVER. People who are losing keep
      logging and people who stall stop; the reviews cannot separate the two
      directions. Read falling logging frequency as an early warning in the
      weekly retro; do not tell the user that logging more will by itself
      make them lose more.
    grade: C
  - note: >
      HOW OFTEN, NOT HOW LONG. Harvey 2019 found success separated by
      log-ins per day, not minutes spent, and minutes fell from about 23 to
      15 per day over six months among successful loggers. Make logging
      fast and frequent (log at the meal), never long.
    grade: C
  - note: >
      DAILY WEIGHING HAS ONE RCT, AS A BUNDLE. Steinberg 2013 tested daily
      weighing together with a trend graph and weekly tailored feedback
      against no intervention. It shows the package works; it does not
      isolate daily over weekly weighing. Daily weighing is a reasonable
      default only when the result is shown as a trend, never as a verdict
      on today.
    grade: B
  - note: >
      NOT FOR EVERYONE. Adverse associations with self-weighing cluster in
      women and younger people and in non-treatment-seeking samples
      (Pacanowski 2015), while treatment-seeking adults with overweight show
      none (Zheng 2015). If the user reports distress at the scale, a history
      of disordered eating, or checking many times a day, drop the daily
      weighing default and do not push it back. There is no eating-disorder
      axis on the ledger yet (GAPS.md), so this is a conversational trigger,
      not a gate.
    grade: C
  - note: >
      NO DOSE IS ESTABLISHED. "Log at least N days a week" thresholds in
      circulation are study engagement cut-offs, not tested minimums. Burke
      2011 lists the dose as unknown and nothing since fixes it.
    grade: C
claim: >
  More frequent dietary self-monitoring and regular self-weighing are
  consistently associated with greater weight loss in behavioural programmes
  (22-study review, 39 digital-RCT review with the association in 74 percent
  of occurrences, 17 longitudinal self-weighing studies). The association is
  with frequency of entries, not time spent: in a 142-person programme,
  people who lost at least 5 percent logged in more often per day while their
  minutes logging did not differ, and logging time fell from about 23 to 15
  minutes a day over six months. A daily self-weighing package (smart scale,
  trend graph, weekly feedback) beat no intervention in one 91-person RCT.
  Causality is not established and no minimum dose is known. Self-weighing is
  not associated with harm in treatment-seeking adults with overweight but
  is in some women and younger people.
reasoning: >
  The association has replicated across reviews spanning two decades and
  paper to app, which earns the observational band. It stays there because
  adherence to self-monitoring is itself a marker of engagement: Burke et al.
  rate the evidence weak, and none of the reviewed designs randomise
  frequency while holding everything else fixed. The Steinberg trial is the
  only randomised piece and it randomised a bundle against nothing, so its
  trial-level strength attaches only to the note about the bundle. Harvey's
  log-ins-not-minutes finding is the most actionable result for a product
  because it says the cost to keep low is friction per entry, but it is a
  single observational cohort, 91 percent women. The harm side is carried
  because a daily-weighing default ships to everyone: the treatment-seeking
  samples show no harm, the broader samples show some, and the engine needs
  an exit rather than a stronger push. No Korean data was located.
---

# nutrition/self-monitoring-frequency-027 -- 기록·체중 측정 빈도

기록을 자주 하는 사람이 더 많이 뺀다. 이건 행동 체중 관리 연구에서 가장 꾸준히 나오는
관계다. 종이 일지 시절 리뷰(22편)에서도, 앱과 웹을 쓴 무작위 시험 39편을 모은 리뷰에서도
같은 방향이었다. 다만 원인과 결과가 어느 쪽인지는 모른다. 잘 빠지고 있는 사람이 기록을
계속하는 것일 수도 있다.

쓸모 있는 세부 결과가 하나 있다. 24주 온라인 프로그램에서 성공한 사람과 아닌 사람은
기록에 쓴 시간이 아니라 하루에 기록을 연 횟수에서 갈렸다. 기록 시간은 첫 달 하루 23분에서
여섯째 달 15분으로 줄었다. 오래 붙잡고 있을 필요는 없고 자주, 바로 적으면 된다.

매일 체중을 재는 방식은 무작위 시험이 하나 있다. 스마트 체중계, 추세 그래프, 주간 피드백을
묶은 프로그램이 아무것도 안 한 대조군보다 6개월에 훨씬 많이 뺐다. 묶음 전체의 효과라서
'매일'이 '매주'보다 낫다는 증명은 아니다. 체중을 재는 게 해로운지에 대해서는, 감량을
원해서 찾아온 과체중 성인에서는 해가 보이지 않았지만 여성과 젊은 층 일부에서는 기분·자존감
악화와 함께 나타났다.

## 한국어 요약 (답변용)

- 기록은 길게보다 자주가 낫다. 끼니 직후 한 줄로 적게 하고, 한 번에 몰아서 정리하게 하지 않는다.
- 주간 회고에서 기록 빈도가 떨어지는 것은 경고 신호로 읽는다. 다만 "더 자주 기록하면 더
  빠진다"고 약속하지 않는다.
- 매일 체중을 재는 것을 기본값으로 둘 수 있지만, 결과는 항상 추세로 보여 준다. 오늘 숫자 하나로
  평가하지 않는다.
- 체중계 때문에 괴롭다, 하루에 여러 번 잰다, 섭식 문제 이력이 있다는 말이 나오면 매일 측정
  기본값을 끄고 다시 권하지 않는다.
- "주 며칠 이상 기록해야 한다"는 기준 숫자는 연구로 정해진 적이 없다. 그런 숫자를 말하지 않는다.
