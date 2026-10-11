---
# Authored 2026-10-06 (dispatch kw-kr-dish-energy, @meal-craft). KR-LOCALE.
# Closes residual sub-gap 5 of the v21 craft-lane section: item 020 cited the
# Ministry of Food and Drug Safety (식약처) restaurant-dish dataset but could not
# read it (fetch size limit). This pass downloaded BOTH volumes in full and read
# every dish page: vol.1 (2012, 130 dishes, 134 pp.) and vol.2 (2013, 108
# dishes, 116 pp.) -- 238 measured dishes. Every number below is either copied
# from a dish page or is arithmetic over those pages (medians by the dataset's
# own 분류 field); nothing is recalled from memory.
#
# dish_class_table, logging_defaults and swap_rules are structured data for a
# meal-logging module. The YAML-subset reader returns numbers as strings; cast
# them. Values are 2011-13 RESTAURANT means, published without any spread, so a
# module may use them as defaults and orderings, never as the user's truth.
id: nutrition/kr-restaurant-dish-energy-ranking-022
domain: nutrition
lane: "@meal-craft"
grade: B (measured national restaurant-dish dataset read at source; class orderings computed over 238 dishes; single 2011-13 snapshot with no published spread; the logging defaults are convention and carry their own basis_grade)
locale: KR
as_of: 2012-2013
contested: no
sources:
  - "https://foodsafetykorea.go.kr/upload/mkisna/2012.pdf"  # 식품의약품안전청, 외식 영양성분 자료집 (2012.2), 130 dishes, 27 nutrients + fatty acids per 1인분 and per 100 g; dishes chosen from 국민건강영양조사 high-frequency foods, collected in 6 regions, each value a representative value over 72 samples, 20+ analysing institutions. READ IN FULL 2026-10-06
  - "https://foodsafetykorea.go.kr/upload/mkisna/2013.pdf"  # 식품의약품안전처, 외식 영양성분 자료집 제2권 (2013.3, 발간등록번호 11-1471000-000001-01), 108 dishes, 2010 국민건강영양조사 basis, 6 regions x 19 sub-areas x 3-4 random restaurants, mean of 72 samples per dish, 18 institutions under an analytical QC programme; values per 1회 제공량 (named 눈대중량 + grams) and per 100 g. READ IN FULL 2026-10-06
  - "https://www.diabetes.or.kr/general/dietary/dietary_03.php?con=2"  # Korean Diabetes Association 식품교환표: 밥 70 g (1/3공기) = one grain exchange; con=3 restates 밥류 70 g (1/3공기); dietary_03.php gives the grain exchange as 100 kcal / 23 g carbohydrate / 2 g protein. Retrieved directly 2026-10-06
  - "https://various.foodsafetykorea.go.kr/nutrient/"  # K-FIND, the ministry's live national food nutrition DB (states monthly updates). Reached 2026-10-06 as an EDITION CHECK only; its rows were not read (script-driven app), so no figure here comes from it
  - "source:nutrition/kr-mixed-dish-logging-unit-020 -- the log-by-name rule this item supplies the numbers for; the shared-dish convention there is unchanged"
  - "source:nutrition/kr-protein-exchange-counting-021 -- exchange arithmetic; the rice line below is three grain exchanges"
  - "source:nutrition/portion-estimation-shape-ceiling-018 -- why the dataset's named reference portion beats a gram guess on rice and broth"
  - "source:nutrition/kr-food-composition-accuracy-016 -- table-level error; restaurant means add between-restaurant spread on top, and that spread is not published"
  - "source:nutrition/self-report-underreporting-007 -- a default is still a floor-and-trend instrument, not an intake estimate"
  - "framework:VC-E craft -- the dataset is a government measurement and its orderings are computed, not judged; turning them into logging defaults and swaps is a convention, labelled per rule"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
dish_class_table:
  - class: 튀김류
    slug: fried
    n: 11
    kcal_serving_median: 387
    kcal_serving_range: [251, 755]
    kcal_per_100g_median: 310
    protein_g_per_100kcal_median: 3.9
    carb_energy_pct_median: 30
    fat_energy_pct_median: 53
    sodium_mg_serving_median: 552
    rice_in_entry: no
  - class: 구이류
    slug: grilled
    n: 9
    kcal_serving_median: 481
    kcal_serving_range: [177, 941]
    kcal_per_100g_median: 267
    protein_g_per_100kcal_median: 7.1
    carb_energy_pct_median: 12
    fat_energy_pct_median: 58
    sodium_mg_serving_median: 950
    rice_in_entry: no
  - class: 전류
    slug: pan-fried-batter
    n: 9
    kcal_serving_median: 276
    kcal_serving_range: [208, 361]
    kcal_per_100g_median: 188
    protein_g_per_100kcal_median: 4.7
    carb_energy_pct_median: 31
    fat_energy_pct_median: 49
    sodium_mg_serving_median: 480
    rice_in_entry: no
  - class: 찜류
    slug: braised-steamed
    n: 7
    kcal_serving_median: 470
    kcal_serving_range: [203, 1206]
    kcal_per_100g_median: 181
    protein_g_per_100kcal_median: 10.1
    carb_energy_pct_median: 6
    fat_energy_pct_median: 43
    sodium_mg_serving_median: 645
    rice_in_entry: no
  - class: 볶음류
    slug: stir-fried
    n: 10
    kcal_serving_median: 199
    kcal_serving_range: [52, 351]
    kcal_per_100g_median: 164
    protein_g_per_100kcal_median: 6.9
    carb_energy_pct_median: 39
    fat_energy_pct_median: 28
    sodium_mg_serving_median: 862
    rice_in_entry: no
  - class: 밥류
    slug: rice-dish
    n: 45
    kcal_serving_median: 584
    kcal_serving_range: [161, 885]
    kcal_per_100g_median: 156
    protein_g_per_100kcal_median: 3.6
    carb_energy_pct_median: 65
    fat_energy_pct_median: 22
    sodium_mg_serving_median: 1203
    rice_in_entry: yes
    note: one-bowl rice meals only (덮밥, 비빔밥, 볶음밥, 카레, 오므라이스; n=23, sushi, rolls and 김밥 excluded) have median 700 kcal, IQR 672-755, protein median 26 g
  - class: 면류
    slug: noodle
    n: 30
    kcal_serving_median: 636
    kcal_serving_range: [204, 918]
    kcal_per_100g_median: 94
    protein_g_per_100kcal_median: 3.4
    carb_energy_pct_median: 69
    fat_energy_pct_median: 15
    sodium_mg_serving_median: 2193
    rice_in_entry: no
    note: noodles are in the entry; IQR 600-688 kcal; 16 of 30 entries are at or above 2000 mg sodium
  - class: 죽류
    slug: porridge
    n: 8
    kcal_serving_median: 572
    kcal_serving_range: [443, 874]
    kcal_per_100g_median: 74
    protein_g_per_100kcal_median: 2.9
    carb_energy_pct_median: 76
    fat_energy_pct_median: 13
    sodium_mg_serving_median: 1211
    rice_in_entry: yes
  - class: 탕류
    slug: hot-soup-tang
    n: 16
    kcal_serving_median: 456
    kcal_serving_range: [237, 960]
    kcal_per_100g_median: 70
    protein_g_per_100kcal_median: 12.7
    carb_energy_pct_median: 12
    fat_energy_pct_median: 37
    sodium_mg_serving_median: 1786
    rice_in_entry: no
    note: 15 of 16 entries under 30 g carbohydrate; the exception is 삼계탕 (40.9 g, glutinous rice inside the bird)
  - class: 국류
    slug: soup-guk
    n: 9
    kcal_serving_median: 434
    kcal_serving_range: [223, 711]
    kcal_per_100g_median: 62
    protein_g_per_100kcal_median: 7.3
    carb_energy_pct_median: 24
    fat_energy_pct_median: 36
    sodium_mg_serving_median: 1980
    rice_in_entry: depends
    note: 떡국, 떡만둣국, 만둣국 and 어묵국 carry their starch (34-147 g carbohydrate); 소머리국밥 (17.5 g), 순대국 (17.3 g) and the other low-carbohydrate entries carry no rice
  - class: 찌개류
    slug: stew-jjigae
    n: 7
    kcal_serving_median: 248
    kcal_serving_range: [145, 520]
    kcal_per_100g_median: 61
    protein_g_per_100kcal_median: 7.8
    carb_energy_pct_median: 20
    fat_energy_pct_median: 44
    sodium_mg_serving_median: 1962
    rice_in_entry: no
    note: 6 of 7 under 30 g carbohydrate; 부대찌개 (47.3 g) carries ramen noodle and processed meat
  - class: 김치류
    slug: kimchi
    n: 12
    kcal_serving_median: 19
    kcal_serving_range: [14, 56]
    kcal_per_100g_median: 38
    protein_g_per_100kcal_median: 5.6
    carb_energy_pct_median: 59
    fat_energy_pct_median: 15
    sodium_mg_serving_median: 339
    rice_in_entry: no
    note: reference portion is mostly 1/2작은접시 = 50 g
logging_defaults:
  - rule: log-by-name
    when: a dish matches a dataset entry by name
    then: log the entry at its 1회 제공량 (named 눈대중량 and grams); let the user scale in halves, never in grams
    basis: nutrition/kr-mixed-dish-logging-unit-020
    basis_grade: D
  - rule: rice-line
    when: a 찌개, 탕 or 국 entry has carbohydrate under 30 g
    then: add a separate 공기밥 line, default one 공기 = 210 g = 3 grain exchanges = 300 kcal, 69 g carbohydrate, 6 g protein; adjust in 1/3-공기 steps (one exchange each)
    basis: dataset carbohydrate values (26 of 32 soup and stew entries under 30 g, less than half of one 공기; the six above carry their own starch -- 떡, 만두, 어묵, 찹쌀, 라면) and the KDA exchange (밥 70 g = 1/3공기 = 100 kcal)
    basis_grade: B
    default_grade: D
  - rule: no-rice-line
    when: the entry is a 덮밥, 비빔밥, 볶음밥, 카레라이스, 오므라이스, 죽, 김밥, 초밥 or any noodle dish, or any entry with carbohydrate of 50 g or more
    then: do not add rice; the starch is already inside the entry
    basis: dataset carbohydrate values
    basis_grade: B
  - rule: name-does-not-decide
    when: the dish name contains 국밥 or 탕 and the matched entry is under 30 g carbohydrate
    then: apply rice-line anyway; in this dataset even 소머리국밥 is measured without its rice
    basis: dataset carbohydrate values
    basis_grade: B
  - rule: class-median-fallback
    when: a restaurant dish has no matching entry but its class is known
    then: log the class kcal_serving_median and mark the line estimated; one-bowl rice meals use 700 kcal, noodle dishes 640 kcal, a 찌개 250 kcal plus the rice line, a 탕 460 kcal plus the rice line
    basis: dish_class_table
    basis_grade: D
  - rule: banchan-weight
    when: banchan are logged
    then: kimchi and 나물 or 무침 banchan default to their small published portions (kimchi 50 g about 20 kcal; 무침 median 46 kcal); oil-cooked banchan (전, 볶음, 조림 with meat or nuts) get their own line; shared banchan follow item 020 (present but uncounted)
    basis: dish_class_table and nutrition/kr-mixed-dish-logging-unit-020
    basis_grade: D
  - rule: sodium-flag
    when: the meal holds a 면, 국, 탕 or 찌개 entry
    then: flag that one serving is near the dataset's own 2000 mg daily reference value; give NO credit for leaving broth, because the dataset does not split broth from solids
    basis: dish_class_table sodium column
    basis_grade: B
swap_rules:
  - goal: less energy, same slot
    from: cream-sauce pasta (크림소스 838 kcal, 해물크림소스 918 kcal)
    to: tomato-sauce pasta (토마토소스 643 kcal, 해물토마토소스 584 kcal)
    delta_kcal: [-195, -334]
    basis_grade: B
  - goal: less energy, same slot
    from: fried cutlet plate (돈가스 624-755 kcal, 생선까스 653 kcal)
    to: lean grilled white fish (갈치구이 481 kcal with 62 g protein, against 24-42 g in the cutlets)
    delta_kcal: [-143, -274]
    caveat: 대구매운탕 with the rice line (662 kcal) is about the same energy as a cutlet with twice the protein; 고등어구이 (668 kcal) and 훈제오리 (797 kcal) are grilled and NOT lighter; the fish or cut decides, not the word 구이
    basis_grade: B
  - goal: less energy, same slot
    from: one-bowl rice meal to another (볶음밥 773 to 비빔밥 707 or 회덮밥 683)
    to: same dish, leave 1/3 공기 of rice
    delta_kcal: [-66, -100]
    caveat: swaps inside 밥류 move energy about 10 percent; the rice amount is the bigger lever
    basis_grade: C
  - goal: more protein per kcal
    from: one-bowl rice or noodle meal (median 26 g or 21 g protein for 640-700 kcal)
    to: a white-fish or beef-bone 탕 with one 공기 (설렁탕 420 kcal, 60 g protein; 대구매운탕 362 kcal, 57 g; plus 300 kcal of rice)
    delta_kcal: [-38, 20]
    caveat: 감자탕 (960 kcal), 곰탕 and 꼬리곰탕 carry 30-52 g fat; the protein advantage holds, the energy advantage does not
    basis_grade: B
  - goal: less sodium
    from: 짬뽕 (4000 mg), 우동(중식) (3396 mg), 열무냉면 (3152 mg)
    to: 콩국수 (945 mg), 비빔밥 (1337 mg), 회덮밥 (744 mg)
    caveat: no figure for leaving the broth exists in this dataset
    basis_grade: B
refraction_notes:
  - note: >
      THE SNAPSHOT AND THE SETTING BOTH BOUND THIS. Restaurant dishes, sampled
      for 2012 and 2013 books built on 2010 consumption data. Every value is a
      mean or representative value over 72 samples and no standard deviation or
      range is published, so how far one restaurant's bowl sits from the mean is
      unknown. The orderings across classes are wide and survive that; a single
      dish value is a default, not a measurement of the user's bowl. One entry
      shows why: 소불고기 is printed at 177 kcal per 200 g (88 kcal per 100 g),
      well below what its recipe suggests and below every other grilled meat.
      It was checked on the page and is reproduced as printed; treat outliers as
      outliers.
    grade: B
  - note: >
      HOME COOKING IS NOT COVERED. Both volumes are 외식. A home 김치찌개 or a
      home 국 may differ in oil, meat cut and serving size, and no measured home
      dataset was read in this pass. Use the restaurant entry for a home dish
      only as a labelled fallback.
    grade: D
  - note: >
      THE RICE LINE IS AN INFERENCE FROM CARBOHYDRATE, NOT A STATEMENT IN THE
      BOOK. Neither volume says whether rice was served or excluded. The
      inference is arithmetic: a soup entry with under 30 g of carbohydrate
      cannot contain a 210 g 공기 at 69 g. The default of exactly one 공기 is a
      convention; no source on how much rice Korean diners actually eat with a
      찌개 was read.
    grade: C
  - note: >
      PER-100-G AND PER-SERVING RANKINGS POINT OPPOSITE WAYS. 찌개, 국 and 탕 are
      the least energy-dense classes (61-70 kcal per 100 g) and fried food the
      most (310). Per serving the order flips, because a soup or noodle serving
      weighs 400-1000 g. A swap rule that reads only energy density will steer a
      user from a 624 kcal 돈가스 to a 960 kcal 감자탕.
    grade: B
claim: >
  The Ministry of Food and Drug Safety measured 238 frequently eaten Korean
  restaurant dishes (130 in 2012, 108 in 2013), each a mean over 72 samples from
  six regions, per named serving and per 100 g. Computed over those pages:
  energy density ranks fried (median 310 kcal/100 g) above grilled (267),
  batter-fried 전 (188), braised 찜 (181), stir-fried (164), rice dishes (156),
  noodles (94), porridge (74), 탕 (70), 국 (62) and 찌개 (61). Per serving the
  order changes because broth dishes are heavy: a noodle serving is median
  636 kcal, a one-bowl rice meal 700 kcal, a 탕 456 kcal, a fried dish 387 kcal,
  a 찌개 248 kcal. 26 of 32 찌개, 탕 and 국 entries hold under 30 g
  carbohydrate, so they are measured without rice (the other six carry their own 떡, 만두, 어묵, 찹쌀 or 라면); one 공기 (210 g, three grain
  exchanges, 300 kcal) makes up a median 55 percent of a 찌개 meal's energy
  and 41 percent of a 탕 meal's. Protein per 100 kcal is highest in 탕 (12.7 g)
  and 찜 (10.1 g) and lowest in rice (3.6 g), noodle (3.4 g) and 떡 (1.7 g)
  dishes. The ingredient outranks the cooking method: boiled pork 수육 is the
  densest main (402 kcal/100 g, 1206 kcal per serving), and grilled mackerel
  (668 kcal) matches a pork cutlet (624). Noodle, 국, 탕 and 찌개 servings carry
  a median 1786-2193 mg sodium, near the dataset's own 2000 mg daily reference
  in one bowl. Logging rules: log by name at the published serving; add a
  separate rice line to any soup or stew entry under 30 g carbohydrate; fall
  back to the class median when the dish is missing; swap the fish, cut or
  sauce before the cooking method; never credit leaving the broth.
reasoning: >
  This is the dataset item 020 could only point at. Both volumes were
  downloaded and parsed page by page; dish counts match the books' own
  contents pages (130 and 108), and spot values (갈치구이 481 kcal, 소불고기
  177 kcal, 설렁탕 420 kcal) were checked against the rendered page. The class
  is the dataset's own 분류 field; medians are used because the classes are
  small and skewed (찜 runs 203-1206 kcal). Why B and not higher: it is one
  government snapshot, a decade old, restaurant only, with no published spread,
  and no independent replication of these dish values was read. Why not lower:
  these are chemical analyses of real servings, and the cross-class orderings
  this item leans on are several-fold apart, far wider than any plausible
  between-restaurant variation. The logging defaults sit lower than the data,
  and each says so in its own basis_grade. The rice line is the most useful
  thing here and also the easiest to get wrong. Without it, a 찌개 meal logs at
  about 250 kcal when the plate is about 550, and an energy-density swap rule
  sends a dieter toward the heaviest bowls in the book. What the dataset cannot
  answer: how much of a soup's energy and sodium sits in the broth, how the
  values have drifted since 2013, and how home versions differ. All three are
  recorded in GAPS.md and none is filled here by inference.
---

# nutrition/kr-restaurant-dish-energy-ranking-022

식약처 외식 영양성분 자료집은 그동안 이름만 인용되던 자료다. 이번에 1권(2012,
130종)과 2권(2013, 108종)을 통째로 내려받아 음식 페이지를 전부 읽었다. 메뉴마다
전국 6개 권역에서 모은 시료 72개의 평균을 1인분과 100 g 기준으로 실은 정부
실측치다. 아래 숫자는 모두 그 페이지에서 옮겨 적었거나, 자료집의 분류별로
중앙값을 낸 것이다.

100 g당 열량은 예상대로 나온다. 튀김 310 kcal, 구이 267, 전 188, 찜 181,
볶음 164, 밥류 156, 면류 94, 죽 74, 탕 70, 국 62, 찌개 61 순이다. 그런데 1인분으로
바꾸면 순위가 뒤집힌다. 국물 음식은 한 그릇이 400~1000 g이라 면 한 그릇이
중앙값 636 kcal, 덮밥·비빔밥 같은 한 그릇 밥이 700 kcal, 탕이 456 kcal인
반면 튀김 1인분은 387 kcal, 찌개는 248 kcal다. 밀도만 보고 바꾸라고 하면
624 kcal짜리 돈가스를 960 kcal짜리 감자탕으로 바꾸게 된다.

기록에서 가장 중요한 건 공기밥이다. 찌개·탕·국 32종 가운데 26종은 탄수화물이
30 g도 안 된다. 공기밥 한 그릇(210 g)에는 69 g이 들어 있으니 이 값에는 밥이
빠져 있다는 뜻이다. 소머리국밥조차 17.5 g이라, 이름에 '국밥'이 붙어도 밥은
따로 계산해야 한다. 그래서 규칙은 이렇다. 국물 음식의 탄수화물이 30 g
미만이면 공기밥을 별도 줄로 넣고, 기본값은 한 공기(곡류군 3교환, 300 kcal)로
한다. 이렇게 하면 밥이 찌개 한 끼 열량의 절반 남짓(중앙값 55%), 탕 한 끼의
41%를 차지한다. 밥을 빼먹으면 550 kcal짜리 상이 250 kcal로 기록된다. 다만
자료집 어디에도 밥을 뺐다고 적혀 있지는 않다. 탄수화물 값에서 계산으로
끌어낸 결론이고, '한 공기'라는 기본값도 실제 섭취량을 잰 근거가 없는
관례라는 점을 밝혀 둔다.

조리법보다 재료가 먼저다. 삶은 돼지고기 수육이 주요리 가운데 가장 열량이
높고(100 g당 402 kcal, 1인분 1206 kcal), 고등어구이(668 kcal)는 등심돈가스(624)와
비슷하다. 구이라는 이름만으로 가볍다고 볼 수 없다. 열량을 줄이려면 생선의
종류, 고기 부위, 소스(크림을 토마토로 바꾸면 195~334 kcal가 준다)를 먼저
바꿔야 한다. 같은 한 그릇 밥끼리 바꿔 봐야 10% 안팎이고, 밥 1/3공기를 남기는
편(100 kcal)이 낫다. 단백질이 목표라면 탕이 유리하다. 100 kcal당 단백질이
탕 12.7 g, 찜 10.1 g으로, 밥류 3.6 g이나 면류 3.4 g보다 훨씬 많다. 설렁탕이나
대구매운탕에 공기밥 하나를 더해도 열량은 덮밥 한 그릇과 비슷하고 단백질은
두 배가 넘는다.

나트륨은 국물 음식 한 그릇이 중앙값 1800~2200 mg으로, 자료집이 쓰는 하루
기준치 2000 mg에 한 끼 만에 닿는다. 짬뽕은 4000 mg이다. 그런데 이 자료는
국물과 건더기를 나눠 재지 않았으니, 국물을 남기면 얼마나 줄어드는지는
알 수 없다. 그 몫을 공제해 주지 않는다.

한계도 분명하다. 2012~2013년 외식 시료이고, 평균만 있고 편차는 없으며,
집밥은 다루지 않는다. 소불고기처럼 200 g에 177 kcal로 이상하게 낮은 값도
페이지에 찍힌 그대로 옮겼다. 그러니 개별 값은 기본값으로만 쓰고, 분류 사이의
큰 차이를 믿고 쓸 것.
