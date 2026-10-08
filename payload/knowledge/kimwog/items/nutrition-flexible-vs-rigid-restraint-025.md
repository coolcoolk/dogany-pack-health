---
# Diet-adherence sprint 2026-10-07 (dispatch kw-nu-diet-adherence-structure).
# "Flexible dieting beats rigid dieting" is repeated in coaching as if it were
# a trial result. It is mostly a questionnaire correlation, and the one
# randomised test found no difference in weight loss. Filed with that split
# visible: the correlational direction is kept, the causal sentence is not.
id: nutrition/flexible-vs-rigid-restraint-025
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 1999-2021
contested: no
sources:
  - "https://doi.org/10.1002/(SICI)1098-108X(199907)26:1<53::AID-EAT7>3.0.CO;2-N"  # Westenhoefer J, Stunkard AJ, Pudel V. Int J Eat Disord 1999;26(1):53-64. PMID 10349584 -- scale development: 7-day diary + questionnaire n=54,517 in a weight-reduction programme, population survey n=1,838; rigid control with more disinhibition, higher BMI, more binge episodes; flexible control the reverse and a higher probability of 1-year weight reduction
  - "https://doi.org/10.1006/appe.2001.0445"  # Stewart TM, Williamson DA, White MA. Appetite 2002;38(1):39-44. PMID 11883916 -- n=188 nonobese women, cross-sectional; rigid dieting with eating-disorder symptoms, mood disturbance, shape concern; flexible not highly associated; authors state causality cannot be addressed
  - "https://doi.org/10.1016/j.eatbeh.2017.01.008"  # Linardon J, Mitchell S. Eat Behav 2017;26:16-22. PMID 28131005 -- n=372 community; flexible control predicted LOWER disordered eating but HIGHER body-image concern, and only once rigid control was accounted for
  - "https://doi.org/10.1038/sj.ijo.0802530"  # Westenhoefer J, von Falck B, Stellfeldt A, Fintelmann S. Int J Obes 2004;28(2):334-335. PMID 14647175 -- Lean Habits Study, prospective, 1,247 of 6,857 with complete 3-year data; improved flexible control among the behaviours whose maintenance at 1 year went with 3-year success
  - "https://doi.org/10.1186/s12970-021-00452-2"  # Conlin LA, Aguilar DT, Rogers GE, Campbell BI. J Int Soc Sports Nutr 2021;18:52. PMID 34187492 -- the only randomised test located: n=23 completers, resistance-trained, ~20 percent deficit for 10 weeks, flexible (non-specific foods) vs rigid (specific foods); no between-group difference on any variable during the diet
  - "source:nutrition/adherence-rules-074 -- the engine-readable rules that consume this item"
  - "source:nutrition/unlogged-day-not-zero-019 -- a missed or off-plan day is data, the counterpart of 'not a failure'"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      CORRELATION, NOT A TRIAL RESULT. Every flexible-is-better finding located
      is a questionnaire correlation (cross-sectional, or a programme cohort
      where flexible control rose alongside other behaviours). The one
      randomised comparison (Conlin 2021, n=23) found the two styles equally
      effective for loss. Do not say "flexible dieting makes you lose more".
    grade: C
  - note: >
      WHAT IS SAFE TO SAY is the shape: an all-or-nothing rule set ("never X",
      "a slip ruins the day") travels with more disinhibition, binge episodes
      and shape concern, so the plan should not be phrased as one. That is a
      wording choice the evidence supports in direction, not a cure.
    grade: C
  - note: >
      FLEXIBLE IS NOT FREE OF COST. Linardon 2017 found flexible control tied to
      higher body-image concern once rigid control was held constant. Flexible
      control is still dietary control; it is not intuitive eating and not a
      prevention measure for disordered eating.
    grade: C
  - note: >
      THE TRIAL'S POST-DIET FAT-FREE-MASS GAP IS NOT A FINDING TO SPEAK. Conlin
      2021 reported more fat-free mass in the flexible arm after the diet, and
      the authors themselves say there is no clear physiological rationale for
      it (no difference in training time, protein or energy). Do not quote it.
    grade: D
claim: >
  Flexible restraint (graded, permissive control with room for adjustment) is
  associated with lower body mass index, less disinhibition and fewer binge
  episodes, and rigid restraint (all-or-nothing rules) with the reverse and
  with eating-disorder symptoms and shape concern, across a 54,517-person
  programme sample, a 1,838-person population survey and a 188-woman
  community sample. These are correlations. The only randomised comparison
  located, 23 resistance-trained adults on a 20 percent deficit for 10 weeks,
  found flexible and rigid food plans equally effective for weight and fat
  loss. The usable conclusion is about phrasing: do not build a plan as an
  all-or-nothing rule set; do not promise that flexibility itself causes
  more loss.
reasoning: >
  The flexible-versus-rigid distinction comes from a validated split of the
  Three-Factor Eating Questionnaire restraint scale, and its correlates have
  replicated across independent samples, which is why the direction ships at
  the observational band rather than lower. Causality is not established:
  Stewart et al. say so in their own abstract, the Lean Habits cohort reports
  flexible control as one of several behaviours that moved together, and a
  person who binges may report rigid rules because of the binge rather than
  the other way round. The only trial tested food-list flexibility, not the
  restraint style the questionnaire measures, and was small and short; its
  null on weight loss is consistent with adherence, not food choice, being
  what drives loss (see 074). The Linardon result is carried because it is
  the honest counterweight: flexible control is not harmless in every
  respect. Not contested -- no source located argues rigid control is
  better; the dispute is only about how much the correlation means.
---

# nutrition/flexible-vs-rigid-restraint-025 -- 유연한 절제 vs 경직된 절제

"유연하게 다이어트하면 더 잘 빠진다"는 말은 연구 결과처럼 돌아다니지만, 실제
근거는 대부분 설문 상관관계다. 경직된 규칙("절대 안 먹는다", "한 번 어기면 그날은
끝")을 쓰는 사람일수록 폭식·탈억제·체형 걱정이 많고 체질량지수가 높으며, 유연한
조절을 쓰는 사람은 그 반대였다. 이 방향은 독일 대규모 프로그램 자료, 인구 조사,
미국 여성 표본에서 반복해서 나왔다.

그런데 이를 직접 무작위로 비교한 연구는 하나뿐이고, 결과는 무승부였다. 근력
운동을 하는 23명을 10주 동안 20% 적자로 두고 정해진 음식만 먹는 쪽과 아무
음식이나 칼로리 안에서 먹는 쪽으로 나눴을 때, 감량에는 차이가 없었다. 그 뒤
'유연한 쪽 제지방 증가'는 저자들 스스로 설명이 안 된다고 했으므로 전하지 않는다.

그러니 이 항목이 허락하는 말은 하나다. 식단을 "전부 아니면 전무" 규칙으로
짜지 말 것. 유연함 자체가 더 많이 빠지게 한다고 약속하지는 말 것. 그리고
유연한 조절도 조절이다. 체형 걱정과 함께 갈 수 있다는 결과도 있다.

## 한국어 요약 (답변용)

- 식단 카드 문구는 "절대", "실패", "망쳤다" 같은 전부-아니면-전무 표현을 쓰지 않는다.
  한 끼를 벗어나도 다음 끼니부터 이어 가는 구조로 말한다.
- "유연하게 하면 더 빠진다"고 약속하지 않는다. 무작위 비교에서는 감량 차이가 없었다.
- 유연한 방식이 더 오래 버티기 쉬운 사람이 많다는 건 상관관계 수준의 이야기다. 사용자가
  정해진 메뉴 방식이 편하다고 하면 그것도 똑같이 유효한 선택이다.
- 폭식이나 체형 걱정이 대화에 보이면 식단 규칙을 조이는 쪽으로 가지 않는다.
