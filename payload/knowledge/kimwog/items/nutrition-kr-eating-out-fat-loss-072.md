---
# Meal-prep / eating-out sprint 2026-10-06 (dispatch task kw-meal-prep).
# KR-LOCALE craft row: 외식 during a fat-loss phase. It owns three things the
# warehouse did not have: (1) eating out raises intake (direction, from
# reviews + one KNHANES analysis), (2) a restaurant plate is large and
# variable and its STATED value is right on average but wrong per item, (3)
# a restaurant main dish is the food type people under-estimate most. It
# routes the logging UNIT to nutrition/kr-mixed-dish-logging-unit-020 and the
# portion mechanism to nutrition/portion-size-effect-intake-070; it does not
# restate them.
#
# NO KOREAN DISH RANKING SHIPS HERE. A "choose X over Y" list for 한식 would
# need the ministry's measured dish values (외식 영양성분 자료집), which this
# warehouse still has not read (see GAPS). The dish rules below are
# structural (decide the 밥 portion, leave the 국물, count named pieces), not
# a ranking.
id: nutrition/kr-eating-out-fat-loss-072
domain: nutrition
lane: "@meal-craft"
grade: C
locale: KR
as_of: 2011-2014
contested: yes
sources:
  - "https://doi.org/10.1111/j.1467-789X.2011.00953.x"  # Lachat C, Nago E, Verstraeten R, Roberfroid D, Van Camp J, Kolsteren P. Eating out of home and its association with dietary intake: a systematic review of the evidence. Obes Rev 2012;13(4):329-346. 29 studies; eating out associated with higher total energy and fat share, lower micronutrients. Abstract read via the ITG/UAC repository records
  - "https://doi.org/10.1080/10408398.2011.627095"  # Nago ES, Lachat CK, Dossa RAM, Kolsteren PW. Association of out-of-home eating with anthropometric changes; a systematic review of prospective studies. Crit Rev Food Sci Nutr 2014;54(9):1103-1116. 15 prospective studies; frequent out-of-home eating positively associated with becoming overweight/obese and weight change; fast food worse than restaurants. Abstract read at the ITG repository record
  - "https://doi.org/10.3746/jkfn.2013.42.5.705"  # Koo S, Park K. 성인의 외식 빈도와 관련된 식습관 및 생활습관 요인 분석 (Dietary behaviors and lifestyle characteristics related to frequent eating out among Korean adults). J Korean Soc Food Sci Nutr 2013;42(5):705-. KNHANES 2007-2009, n=10,223 adults 30-64, 24-h recall; more frequent eating out -> higher intake of most nutrients (not carbohydrate or fibre) and lower dietary-guideline adherence score. Abstract read at KoreaScience
  - "https://doi.org/10.1001/jamainternmed.2013.6163"  # Urban LE, Lichtenstein AH, Gary CE, et al. The energy content of restaurant foods without stated calorie information. JAMA Intern Med 2013;173(14):1292-1299. 157 meals, 33 Boston independent/small-chain restaurants, bomb calorimetry; mean 1327 kcal per meal, 7.6 percent above a full day's requirement, within-meal SD about 271 kcal. Abstract read at the publisher
  - "https://doi.org/10.1001/jama.2011.993"  # Urban LE, McCrory MA, Dallal GE, et al. Accuracy of stated energy contents of restaurant foods. JAMA 2011;306(3):287-293. 269 foods, 42 US restaurants; stated vs measured not different overall (about 10 kcal/portion), but 19 percent of items at least 100 kcal over stated, worst in sit-down items stated under 600 kcal. Abstract via index records; full text not read
  - "https://doi.org/10.1016/j.appet.2013.07.012"  # Almiron-Roig E, Solis-Trapala I, Dodd J, Jebb SA. Estimating food portions. Influence of unit number, meal type and energy density. Appetite 2013;71:95-103. n=32 healthy-weight UK adults, 33 foods; low/medium energy-density foods under-estimated by 30-46 percent, single-unit foods and items classed as meals estimated worse than multi-unit snacks, men worse than women. Full text (PMC3857597) read 2026-10-06
  - "source:nutrition/kr-mixed-dish-logging-unit-020 -- the logging unit for a Korean restaurant dish (named measured entry or exchanges) and the shared-dish convention"
  - "source:nutrition/portion-size-effect-intake-070 -- why the portion decision before eating is the lever"
  - "source:nutrition/portion-estimation-shape-ceiling-018 -- rice and protein pieces are where estimation fails"
  - "source:nutrition/self-report-underreporting-007 -- the eating-out day is under-reported on top of all this; no flat correction"
  - "framework:VC-E craft -- direction from two systematic reviews and one KNHANES analysis (observational), restaurant energy from bomb-calorimetry samples in the US (no Korean equivalent read), estimation bias from one small UK laboratory study. The table-side rules are conventions argued from 070 and 020"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
meal_rules:
  - rule: frequency-is-the-lever
    when: planning a fat-loss week
    action: count 외식 meals per week as the controllable quantity; one restaurant meal is not the problem, a high weekly count is the association
    basis: Lachat 2012; Nago 2014; Koo and Park 2013
    basis_grade: C
    kind: evidence
  - rule: decide-before-eating
    when: a restaurant meal
    action: decide the portion before the first bite -- leave part of the 공기밥 or order a half portion, take 반찬 and shared dishes onto your own plate once, do not eat from the shared pot
    basis: nutrition/portion-size-effect-intake-070
    basis_grade: B
    kind: convention
  - rule: leave-the-broth
    when: 국, 탕, 찌개, 국수 or 냉면
    action: eat the named solid pieces, leave most of the 국물; log the dish by name and mark broth as not counted
    basis: nutrition/kr-mixed-dish-logging-unit-020 (named-piece convention)
    basis_grade: D
    kind: convention
  - rule: log-as-whole-dish
    when: logging a restaurant meal
    action: log by dish name against a measured whole-dish entry or in exchange units; never itemise into grams; never shave the entry down because you think you ate less
    basis: nutrition/kr-mixed-dish-logging-unit-020; Almiron-Roig 2013 (meals estimated low)
    basis_grade: C
    kind: convention
  - rule: stated-kcal-is-average-not-item
    when: a menu or app shows a kcal figure
    action: use it, but say it is right on average and can be 100 kcal or more low per item, especially for items stated as light
    basis: Urban 2011
    basis_grade: C
    kind: evidence
  - rule: no-restaurant-multiplier
    when: anyone wants a "restaurant serving is N times normal" factor
    action: refuse; no sourced multiplier exists for Korean dishes, use the named measured entry instead
    basis: GAPS.md nutrition craft lane (refused v21, still unsourced)
    basis_grade: D
    kind: convention
  - rule: day-is-floor
    when: summarising a day with 외식 or a shared table
    action: mark the day's total as a floor (under-counted), not a complete figure; never average it into a trend as if complete
    basis: nutrition/self-report-underreporting-007; nutrition/kr-mixed-dish-logging-unit-020
    basis_grade: C
    kind: convention
refraction_notes:
  - axis: primary_goal
    note: >
      For fat loss, the weekly 외식 count and the decide-before-eating step
      carry the item. For maintenance, the same rules are optional; do not
      turn a social meal into a logging exercise for a user who is not
      cutting.
    grade: D
  - note: >
      THE RESTAURANT NUMBERS ARE AMERICAN. 1327 kcal per meal and the
      per-item label error come from bomb-calorimetry samples of US
      restaurants. They establish that restaurant meals are large and
      variable; they are NOT the size of a Korean 정식 or 국밥 and must not be
      quoted as one. The Korean evidence read here is about frequency and
      intake, not plate energy.
    grade: C
  - note: >
      THE ESTIMATION BIAS IS DIRECTIONAL, NOT A CORRECTION. Meals and
      single-unit foods were under-estimated in a small lean UK sample; that
      tells the module which way a guessed restaurant portion leans. It does
      not license adding a percentage to the user's log (refused on
      nutrition/self-report-underreporting-007).
    grade: C
claim: >
  Eating out is associated with eating more. Two systematic reviews find
  out-of-home eating linked to higher total energy and fat intake and, in
  prospective studies, to weight gain and becoming overweight, with fast food
  worse than restaurants; in Korean adults (KNHANES 2007-2009, n=10,223) more
  frequent eating out went with higher intake of most nutrients and lower
  adherence to dietary guidelines. Restaurant plates are large and variable:
  measured US independent-restaurant meals averaged about 1,330 kcal with a
  within-meal spread of about 270 kcal, and stated menu values, accurate on
  average, were at least 100 kcal low for about one item in five, worst for
  sit-down items advertised as lighter. And the restaurant main dish is the
  kind of food people under-estimate: in a small laboratory study,
  single-unit foods and foods classed as meals were estimated worse than
  multi-unit snacks, with low- and medium-energy-density foods under-counted
  by roughly a third or more. For a fat-loss phase in a Korean setting the
  usable rules are structural: treat the weekly count of 외식 meals as the
  lever, decide the 밥 and shared-dish portion before eating, leave most of
  the 국물, log the dish whole by name, and mark the day as a floor.
reasoning: >
  The direction is consistent across two reviews and a Korean national
  survey, but all of it is observational, and people who eat out often plausibly differ
  in age, sex, income and schedule (not quantified in the Korean abstract
  read this pass), so the observational band is the ceiling and the
  contested flag means under-evidenced. The restaurant-energy and label
  figures are clean measurements by bomb calorimetry but from the US; they
  are carried as evidence that a restaurant plate is large and that a stated
  figure is an average, not as a Korean plate size. The estimation result is
  one study of 32 lean adults against reference portions and transfers only
  as a direction. Everything at the table -- half the 공기밥, plate the shared
  dish once, leave the broth, whole-dish logging -- is a convention resting on
  the portion-size mechanism (nutrition/portion-size-effect-intake-070) and
  the logging-unit convention (nutrition/kr-mixed-dish-logging-unit-020). The
  broth rule is the weakest: it is chosen because the solid pieces are what
  can be named and counted, not from a measurement of where a 찌개's energy
  sits; no Korean dish breakdown was read this pass. No dish ranking ships
  for the same reason.
---

# nutrition/kr-eating-out-fat-loss-072 -- 외식 in a fat-loss phase

**One line:** how often you eat out matters more than any single order; decide
the portion before eating, log the dish whole, call the day a floor.

Reviews of dozens of studies agree that eating out goes with eating more, and
the prospective ones link frequent eating out with gaining weight. A Korean
national survey of ten thousand adults finds the same direction: the more
often people ate out, the more of most nutrients they took in and the worse
they matched the dietary guidelines. None of this is a trial; people who eat
out a lot differ from people who do not in many other ways.

What a restaurant plate is, measured in the US: about thirteen hundred kcal on
average, with a spread of a couple of hundred within the same dish. Printed
calorie figures were right on average but one item in five was at least a
hundred kcal heavier than stated, mostly the dishes sold as lighter. Those are
American plates; the point that transfers is "large and variable", not the
number.

And the main dish is the hardest thing to guess. In a small study, single
plated meals were estimated worse than countable snacks, and everyday foods
were under-counted by a third or more. A guessed restaurant portion leans low.

| Rule | Action | Kind |
|---|---|---|
| frequency-is-the-lever | count 외식 per week | evidence |
| decide-before-eating | half the 공기밥 / half portion; plate shared dishes once | convention |
| leave-the-broth | eat named solids, leave most 국물, mark broth uncounted | convention |
| log-as-whole-dish | named measured entry or exchanges; never shave it down | convention |
| stated-kcal-is-average-not-item | use menu kcal, say it can run 100+ low per item | evidence |
| no-restaurant-multiplier | no N-times factor exists; refuse | convention |
| day-is-floor | an 외식 day is a lower bound, not a complete total | convention |

## 한국어 요약 (답변용)

- 외식이 잦을수록 더 먹는다는 방향은 체계적 문헌고찰 두 편과 국민건강영양조사 분석(성인
  1만여 명)이 같은 쪽을 가리킨다. 다만 모두 관찰 연구다. 한 번의 외식보다 주당 외식 횟수가
  조절할 수 있는 지점이다.
- 식당 한 끼는 크고 들쭉날쭉하다. 미국 식당을 실측한 결과 한 끼 평균 약 1,300 kcal였고, 메뉴에
  적힌 칼로리는 평균은 맞지만 다섯 개 중 하나꼴로 100 kcal 이상 더 나왔다. 미국 수치이므로 한식
  한 상의 크기로 말하지 않는다.
- 먹기 전에 양을 정한다. 공기밥은 처음부터 일부를 덜어 두거나 반 공기로, 공유 반찬과 찌개는 내
  접시에 한 번 덜고, 냄비에서 바로 계속 떠먹지 않는다.
- 국·탕·찌개·면 요리는 건더기 위주로 먹고 국물은 대부분 남긴다. 기록은 음식 이름으로 하고 국물은
  "세지 않음"으로 표시한다. 이 규칙은 측정이 아니라 셀 수 있는 것만 세는 관례다.
- 식당 음식은 요리 이름 그대로(실측 1인분 값이나 교환단위로) 기록한다. 덜 먹은 것 같다고 임의로
  깎지 않는다. 눈대중은 식사류에서 적게 잡히는 쪽으로 기운다.
- "식당 1인분은 보통의 몇 배" 같은 배수는 근거가 없어 쓰지 않는다.
- 외식이나 여럿이 먹은 날의 합계는 하한선이다. 완전한 하루처럼 평균이나 추세에 넣지 않는다.
- 어떤 한식 메뉴가 더 가벼운지 순위는 이 항목에 없다. 식약처 실측 외식 자료를 아직 읽지 못했기
  때문이다.
