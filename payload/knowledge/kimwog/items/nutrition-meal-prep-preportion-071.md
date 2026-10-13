---
# Meal-prep / eating-out sprint 2026-10-06 (dispatch task kw-meal-prep). Craft
# row. The question a meal module actually gets: "should I meal-prep for a
# cut, and how". The evidence for meal prep AS SUCH is cross-sectional and the
# item says so; the one randomised piece is about pre-portioned meals, not
# about cooking. The handling rules on top (portion at pack time, weigh the
# batch once, food-safety routing to the cooking domain) are conventions and
# are labelled kind: convention.
id: nutrition/meal-prep-preportion-071
domain: nutrition
lane: "@meal-craft"
grade: C
locale: universal
as_of: 2004-2017
contested: yes
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC5288891/"  # Ducrot P, Méjean C, Aroumougame V, Ibanez G, Allès B, Kesse-Guyot E, Hercberg S, Péneau S. Meal planning is associated with food variety, diet quality and body weight status in a large sample of French adults. Int J Behav Nutr Phys Act 2017;14:12. NutriNet-Santé, n=40,554, cross-sectional. Planning = 'to plan ahead the foods that will be eaten for the next few days'. Obesity OR 0.79 (women), 0.81 (men); overweight OR 0.92 (women only). Authors: no causality, reverse causation not excluded. Full text read 2026-10-06
  - "https://doi.org/10.1186/s12966-017-0567-y"  # Mills S, Brown H, Wrieden W, White M, Adams J. Frequency of eating home cooked meals and potential benefits for diet and health: cross-sectional analysis of a population-based cohort study. Int J Behav Nutr Phys Act 2017;14:109. Fenland, n=11,396, age 29-64. >5 vs <3 home-cooked main meals/week -> +62.3 g fruit, +97.8 g veg/day; 28 percent less likely overweight BMI, 24 percent less likely excess body fat; HbA1c, cholesterol, hypertension not significant. Authors: direction of cause cannot be established. Full text (PMC5561571) read 2026-10-06
  - "Hannum SM, Carson L, Evans EM, et al. Use of portion-controlled entrees enhances weight loss in women. Obes Res 2004;12(3):538-546"  # 8-week RCT, 60 women BMI 26-40, both arms 1365 kcal plan; two portion-controlled entrees/day lost 5.6 vs 3.6 kg, fat mass 3.6 vs 2.3 kg. Industry-relevant (frozen entrees), small, short. Figures from the abstract via an index record; full text not read
  - "source:nutrition/portion-size-effect-intake-070 -- why the portion decision is the one that matters"
  - "source:nutrition/portion-estimation-shape-ceiling-018 -- why a portion fixed by weight at pack time beats one eyeballed at eat time"
  - "source:nutrition/kr-mixed-dish-logging-unit-020 -- a home-made 반찬/찌개 batch is still logged as a named dish or in exchanges, not itemised"
  - "source:cooking/reheating-not-a-reset-007 -- cooked rice and batch food: the control is how fast it gets cold, reheating does not undo storage"
  - "source:cooking/kr-cold-chain-band-006 -- Korean refrigeration bands; the ministry's 5C holding advice is stricter than the legal 10C ceiling"
  - "framework:VC-E craft -- two large cross-sectional cohorts (direction only, confounded, reverse causation open) plus one small RCT of pre-portioned meals. The pack-time portion and batch-weighing rules are conventions argued from 070 and 018, not tested"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
meal_rules:
  - rule: plan-ahead
    when: user asks how to make a fat-loss diet easier to run
    action: suggest deciding the next few days' meals in advance; speak it as associated with better diet quality and lower obesity odds, not as proven to cause weight loss
    basis: Ducrot 2017; Mills 2017
    basis_grade: C
    kind: evidence
  - rule: portion-at-pack-time
    when: cooking a batch for several meals
    action: split into single-meal containers when cooking, so the portion is decided once and not at the fridge or the pot
    basis: nutrition/portion-size-effect-intake-070; Hannum 2004 (pre-portioned meals beat self-selected at equal kcal plan)
    basis_grade: C
    kind: convention
  - rule: weigh-the-batch-once
    when: user has a kitchen scale and wants to log a batch
    action: weigh the cooked batch, divide by the number of equal containers, log each container as one named portion; never re-estimate per meal
    basis: arithmetic over nutrition/portion-estimation-shape-ceiling-018; no accuracy study of this practice
    basis_grade: D
    kind: convention
  - rule: no-scale-batch
    when: no kitchen scale
    action: still split into equal containers at cook time and log by dish name or exchanges per container; do not invent grams
    basis: nutrition/kr-mixed-dish-logging-unit-020
    basis_grade: D
    kind: convention
  - rule: cool-fast-store-cold
    when: any cooked batch, especially rice
    action: route storage questions to cooking/reheating-not-a-reset-007 and cooking/kr-cold-chain-band-006; never say reheating makes old food safe
    basis: cooking domain food-safety rows (007 carries B, 006 carries a jurisdictional-standard A)
    basis_grade: B
    kind: evidence
  - rule: no-cooking-cure-claim
    when: user expects meal prep itself to cause fat loss
    action: say the cohort link is confounded; the controllable part is the fixed portion and the planned kcal, not the act of cooking
    basis: Ducrot 2017 and Mills 2017 authors' own limitations
    basis_grade: C
    kind: evidence
refraction_notes:
  - axis: primary_goal
    note: >
      For a fat-loss goal the useful core is the fixed portion, decided at
      pack time. For maintenance or gain, planning still helps diet variety in
      the cohort data but the portion rule is a choice, not a lever to push.
    grade: C
  - note: >
      THE COHORT NUMBERS ARE ASSOCIATIONS. Odds ratios of about 0.8 for
      obesity in planners, and roughly a quarter lower odds of overweight in
      frequent home cooks, come from cross-sectional data whose own authors
      say people who already eat well may simply be the ones who plan and
      cook. Never quote them as what meal prep will do for this user.
    grade: C
  - note: >
      THE ONE TRIAL IS ABOUT PORTIONS, NOT KITCHENS. The randomised result
      that pre-portioned meals lost more weight at the same planned kcal is
      eight weeks, sixty women, and used bought frozen entrees. It supports
      fixing the portion; it says nothing about cooking at home versus buying.
    grade: C
claim: >
  Planning meals ahead and eating home-cooked meals are both associated with
  better diet quality and lower odds of excess weight in large cohorts:
  among 40,554 French adults, people who planned the next few days' meals had
  about 20 percent lower odds of obesity, and among 11,396 English adults,
  those eating home-cooked main meals more than five times a week ate more
  fruit and vegetables and had about a quarter lower odds of overweight and
  excess body fat than those eating them under three times. Both studies are
  cross-sectional and both sets of authors say causality cannot be inferred.
  The one randomised piece is about the portion, not the kitchen: at the same
  planned energy, women given two pre-portioned entrees a day lost more weight
  and fat over eight weeks than women selecting their own portions. The
  usable rule for a fat-loss phase is therefore to fix the portion at the
  moment of cooking -- split a batch into single-meal containers -- and to
  route storage to the cooking domain's cold-chain rows.
reasoning: >
  The observational band is the honest ceiling. Ducrot and Mills are large and
  measured diet with repeated records or a long FFQ, and Mills measured body
  composition rather than taking it from self-report, but neither can separate
  meal prep from the kind of person who meal-preps; reverse causation is named
  by the authors. Contested here means under-evidenced, not disputed: no trial
  of meal planning or batch cooking itself against a weight endpoint was
  located. Hannum 2004 gives a randomised, if small and short, anchor for the
  portion mechanism, and it lines up with the portion-size effect in
  nutrition/portion-size-effect-intake-070. The pack-time and batch-weighing
  rules are conventions built on that mechanism and on the estimation ceiling
  in nutrition/portion-estimation-shape-ceiling-018: weighing once at the batch
  replaces many failing eyeball estimates with one division. No study of that
  practice's accuracy or adherence exists, so it is labelled a convention. The
  food-safety rule carries the cooking domain's grade, not this item's.
---

# nutrition/meal-prep-preportion-071 -- meal prep: fix the portion when you cook

**One line:** the cohorts say planners and home cooks are leaner; the trial says
fixed portions lose more; the rule is to portion at the pot, not at the plate.

Two big studies -- forty thousand French adults, eleven thousand English ones --
found that people who plan the next few days' meals, and people who eat
home-cooked meals most days, eat better and are less often overweight. Both
sets of authors say plainly that this could run backwards: people who already
eat well are the ones who plan and cook.

The one randomised result points at the mechanism a meal module can use. At the
same planned calories, women eating two pre-portioned meals a day lost about two
kilograms more over eight weeks than women serving themselves. That is a
portion result, and it agrees with the portion-size row (070).

| Rule | Action | Kind |
|---|---|---|
| plan-ahead | plan the next few days; associated, not proven | evidence |
| portion-at-pack-time | split the batch into single-meal containers when cooking | convention |
| weigh-the-batch-once | with a scale: weigh batch, divide by containers, log per container | convention |
| no-scale-batch | without a scale: equal containers, log by dish name or exchanges | convention |
| cool-fast-store-cold | storage goes to the cooking food-safety rows | evidence |
| no-cooking-cure-claim | cooking itself is not the lever; the fixed portion is | evidence |

## 한국어 요약 (답변용)

- 며칠 치 식사를 미리 정하는 사람, 집밥을 자주 먹는 사람이 식단 질이 좋고 비만 비율이 낮다는
  대규모 조사가 있다. 다만 둘 다 단면 연구라서, 원래 잘 먹는 사람이 계획하고 요리하는 것일 수
  있다고 저자들이 직접 말한다. "밀프렙하면 빠진다"고 말하지 않는다.
- 무작위 시험에서 확인된 건 요리가 아니라 양이다. 같은 칼로리 계획에서 미리 1인분으로 나뉜
  식사를 먹은 쪽이 8주 동안 더 많이 뺐다(여성 60명, 작은 시험).
- 그래서 규칙은 하나다. 만들 때 한 끼 용기에 나눠 담는다. 냉장고나 냄비 앞에서 양을 정하지 않는다.
- 저울이 있으면 완성된 한 솥을 한 번 재고 용기 수로 나눠 용기 하나를 한 단위로 기록한다. 저울이
  없으면 똑같이 나눠 담고 음식 이름이나 교환단위로 기록한다. 그램을 지어내지 않는다.
- 보관은 요리 도메인의 식품안전 항목을 따른다. 특히 밥은 빨리 식혀 냉장하고, 다시 데운다고 오래된
  음식이 안전해지지 않는다.
