---
# Authored 2026-10-07 (dispatch kw-nu-kr-convenience-protein, @meal-craft).
# KR-LOCALE. The diet card's "뭐 먹지 / 대신 뭐 먹을까" path ranks by protein
# density (g per 100 kcal) but only over foods the owner has already logged.
# This item supplies the graded table a swap path would need for foods the
# owner has NOT logged: Korean convenience-store protein products and common
# 외식 dishes, every number read at source from the Ministry of Food and Drug
# Safety K-FIND database (식품영양성분 데이터베이스, last DB update 2026-09-07)
# on 2026-10-07. No figure is recalled from memory or copied from a blog.
#
# kr_protein_options and swap_rules are structured data for the diet code.
# The ratios are DATA (K-FIND values divided out); the tier cut-offs are
# PRODUCT CONSTANTS and are labelled as such. No program code changed.
id: nutrition/kr-convenience-protein-options-030
domain: nutrition
lane: "@meal-craft"
grade: C (official composition dataset read at source; label-declared and single-sample values; tier cut-offs are product constants)
locale: KR
as_of: 2012-2026
contested: no
sources:
  - "https://various.foodsafetykorea.go.kr/nutrient/"  # MFDS K-FIND 식품영양성분 데이터베이스, read 2026-10-07 through its own food search and per-food detail pages (general/food/listJson.do, general/food/detail.do). Every row below carries its K-FIND food code or is a median over the named category
  - "https://various.foodsafetykorea.go.kr/nutrient/intro/data/dataInfo.do"  # K-FIND source list, read 2026-10-07: 가공식품 DB 2026 (307,028 foods), 음식 DB 2026 (20,580), 국가표준식품성분표 10.4 (RDA, 3,313), 표준수산물성분표 2023; final DB update 2026-09-07
  - "K-FIND per-food detail pages -- the 1일 영양성분 기준치 percentages printed on them fix the label reference values used for the sodium tier: 110 kcal = 5.5% (2,000 kcal) and 230 mg sodium = 11.5% (2,000 mg); read on food P117-501050100-2870"
  - "source:nutrition/kr-protein-exchange-counting-021 -- the exchange arithmetic this table cross-checks: one meat-and-fish exchange is 8 g protein at 50-100 kcal, i.e. 8-16 g per 100 kcal, which brackets the mid/lean tier boundary"
  - "source:nutrition/kr-mixed-dish-logging-unit-020 -- the same ministry dish dataset used as a logging unit; this item uses it as a ranking input and does not change 020's rule"
  - "source:nutrition/kr-food-composition-accuracy-016 -- the only chemical validation of the Korean tables (protein 101 percent, one 2003 study); bounds how much any table row can be trusted"
  - "source:nutrition/kr-reference-intakes-2025-014 -- records that sodium outcome evidence was NOT researched; this item's sodium tier is a label-parity display rule, not a health threshold, and does not close that gap"
  - "source:nutrition/protein-intake-002 -- owns the daily protein target; this table only ranks ways to fill it"
  - "source:nutrition/meal-protein-nudge-rules-063 -- (v37; linked at the v38 merge) the per-meal nudge adds one dose to the poorest meal; this table is where a diet-card swap for that dose is picked"
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- (v37; linked at the v38 merge) the deficit-phase protein band the swaps help fill; this table does not set it"
  - "source:nutrition/kr-restaurant-dish-energy-ranking-022 -- (v37; linked at the v38 merge) the energy ranking of the same ministry dish dataset; this table ranks protein per 100 kcal and sodium"
  - "source:nutrition/kr-eating-out-fat-loss-072 -- (v37; linked at the v38 merge) eating-out rules in a cut; restaurant rows here are swap options, not those rules"
  - "framework:VC-E craft -- the values are a government dataset read directly; the choice of protein per 100 kcal as the ranking key, the tier cut-offs and the swap rules are conventions, labelled as such"
applicability:
  axes:
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: allergen_list
      type: categorical
      role: hard
      unknown_policy: hedge
    - key: renal_condition
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
swap_rules:
  - rule: rank_key
    value: protein_g_per_100kcal descending; ties broken by sodium_mg_per_g_protein ascending
    basis: same density term the diet engine already uses (docs/reports/2026-09-30-diet-engine.md)
    basis_grade: D
  - rule: protein_tier
    value: lean at 15 or more g per 100 kcal (60 percent or more of energy from protein); mid 8 to under 15; low under 8
    basis: product constant; 8 and 16 g per 100 kcal are the two ends of one meat-and-fish exchange (021)
    basis_grade: D
  - rule: sodium_tier
    value: low up to 100 mg per 100 kcal; mid over 100 up to 200; high over 200
    basis: 100 mg per 100 kcal is parity with the label reference values (2,000 mg over 2,000 kcal); the tier names a share of the label budget, not a health threshold
    basis_grade: D
  - rule: baseline_rows
    value: rows with role baseline are swap-FROM anchors only and are never suggested
    basis: convention
    basis_grade: D
  - rule: serving_numbers
    value: speak serving_kcal / serving_protein_g / serving_sodium_mg only when present; otherwise speak the per-100-kcal ratio and no serving figure
    basis: K-FIND gives no single serving for those rows (multi-unit packs, or a 100 g analysis basis)
    basis_grade: B
  - rule: shared_dish
    value: rows whose note says shared (shabu_beef, andong_jjimdak) carry whole-pot figures; never present them as one person's intake (020 shared-dish convention)
    basis: convention
    basis_grade: D
  - rule: allergen_exclude
    value: drop any row whose allergens intersect allergen_list; allergen tags are product-class defaults, so unknown or unusual products still need the pack read
    basis: allergens are curator tags from the food class, not read from each label
    basis_grade: D
  - rule: logged_foods_only_contract
    value: the shipped suggest.py names only foods the owner has logged; using this table for unlogged suggestions is a product decision this item does not make
    basis: payload/skills-bundle/diet-status/reference/card-render.md
    basis_grade: D
kr_protein_options:
  - key: chicken_breast_rte
    name: "닭가슴살 (즉석·훈제·수비드 포장육)"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 79
    protein_g_per_100kcal: 20.0
    protein_g_per_100kcal_iqr: [16.8, 21.1]
    sodium_mg_per_100kcal: 296
    sodium_mg_per_100kcal_iqr: [200, 388]
    sodium_mg_per_g_protein: 17.2
    protein_tier: lean
    sodium_tier: high
    serving_basis: "median package (n=58)"
    serving_kcal: 120
    serving_protein_g: 25.0
    serving_sodium_mg: 379
    allergens: [chicken]
    dietary: omnivore
    data_year: "2019..2026"
    note: "sodium spread is wide (40 to about 690 mg per 100 g in the sample); the lowest entries were plain smoked or unseasoned lines, so read the pack"
  - key: rtd_protein_drink
    name: "고단백 음료 (우유단백 RTD, 250 mL 내외)"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 61
    protein_g_per_100kcal: 18.2
    protein_g_per_100kcal_iqr: [15.4, 20.8]
    sodium_mg_per_100kcal: 94
    sodium_mg_per_100kcal_iqr: [48, 153]
    sodium_mg_per_g_protein: 7.5
    protein_tier: lean
    sodium_tier: low
    serving_basis: "median package (n=60)"
    serving_kcal: 110
    serving_protein_g: 20.0
    serving_sodium_mg: 130
    allergens: [milk]
    dietary: vegetarian
    data_year: "2021..2026"
    note: "brand family sample: 더단백 / 테이크핏 맥스 / 닥터유 프로 / 이지프로틴 / 하이뮨 액티브 / 셀렉스; sweetened balance-type drinks sit lower (7-15)"
  - key: tuna_can
    name: "참치 통조림"
    setting: convenience
    role: option
    db: standard-table
    kfind_code: "R211-059070128-0000"
    n: 1
    protein_g_per_100kcal: 11.7
    sodium_mg_per_100kcal: 111
    sodium_mg_per_g_protein: 9.5
    protein_tier: mid
    sodium_tier: mid
    serving_basis: "per 100 g only"
    allergens: [fish]
    dietary: pescatarian
    data_year: "2026 (table 10.4)"
    note: "oil-packed default; draining changes kcal, not measured here"
  - key: chicken_sausage
    name: "닭가슴살 소시지"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 59
    protein_g_per_100kcal: 10.9
    protein_g_per_100kcal_iqr: [8.3, 13.9]
    sodium_mg_per_100kcal: 257
    sodium_mg_per_100kcal_iqr: [188, 326]
    sodium_mg_per_g_protein: 26.7
    protein_tier: mid
    sodium_tier: high
    serving_basis: "median package (n=52)"
    serving_kcal: 168
    serving_protein_g: 18.0
    serving_sodium_mg: 446
    allergens: [chicken]
    dietary: omnivore
    data_year: "2020..2026"
  - key: egg_roasted
    name: "구운란·훈제란 (포장)"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 60
    protein_g_per_100kcal: 10.0
    protein_g_per_100kcal_iqr: [9.6, 10.9]
    sodium_mg_per_100kcal: 120
    sodium_mg_per_100kcal_iqr: [101, 131]
    sodium_mg_per_g_protein: 11.6
    protein_tier: mid
    sodium_tier: mid
    serving_basis: "median package (n=30)"
    serving_kcal: 132
    serving_protein_g: 11.5
    serving_sodium_mg: 155
    allergens: [egg]
    dietary: vegetarian
    data_year: "2022..2026"
  - key: tofu_pack
    name: "두부 (포장 제품)"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 80
    protein_g_per_100kcal: 9.5
    protein_g_per_100kcal_iqr: [8.4, 10.6]
    sodium_mg_per_100kcal: 12
    sodium_mg_per_100kcal_iqr: [4, 73]
    sodium_mg_per_g_protein: 1.4
    protein_tier: mid
    sodium_tier: low
    serving_basis: "median package (n=44)"
    serving_kcal: 252
    serving_protein_g: 23.3
    serving_sodium_mg: 23
    allergens: [soy]
    dietary: vegan
    data_year: "2014..2026"
  - key: egg_boiled
    name: "삶은 달걀"
    setting: convenience
    role: option
    db: standard-table
    kfind_code: "R110-003000046-0000"
    n: 1
    protein_g_per_100kcal: 9.3
    sodium_mg_per_100kcal: 88
    sodium_mg_per_g_protein: 9.5
    protein_tier: mid
    sodium_tier: low
    serving_basis: "per 100 g only"
    allergens: [egg]
    dietary: vegetarian
    data_year: "2026 (table 10.4)"
  - key: string_cheese
    name: "스트링치즈"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 60
    protein_g_per_100kcal: 7.7
    protein_g_per_100kcal_iqr: [7.3, 8.5]
    sodium_mg_per_100kcal: 162
    sodium_mg_per_100kcal_iqr: [132, 241]
    sodium_mg_per_g_protein: 20.9
    protein_tier: low
    sodium_tier: mid
    serving_basis: "multi-unit packs; per 100 kcal only"
    allergens: [milk]
    dietary: vegetarian
    data_year: "2022..2026"
  - key: milk_lowfat
    name: "저지방 우유"
    setting: convenience
    role: option
    db: standard-table
    kfind_code: "R121-026090000-0000"
    n: 1
    protein_g_per_100kcal: 7.1
    sodium_mg_per_100kcal: 87
    sodium_mg_per_g_protein: 12.3
    protein_tier: low
    sodium_tier: low
    serving_basis: "per 100 g only"
    allergens: [milk]
    dietary: vegetarian
    data_year: "2026 (table 10.4)"
  - key: protein_bar
    name: "단백질바"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 60
    protein_g_per_100kcal: 7.1
    protein_g_per_100kcal_iqr: [4.5, 8.1]
    sodium_mg_per_100kcal: 78
    sodium_mg_per_100kcal_iqr: [38, 109]
    sodium_mg_per_g_protein: 11.0
    protein_tier: low
    sodium_tier: low
    serving_basis: "median package (n=46)"
    serving_kcal: 174
    serving_protein_g: 14.5
    serving_sodium_mg: 195
    allergens: [milk, soy, wheat]
    dietary: vegetarian
    data_year: "2021..2026"
    note: "allergen set varies by product; read the pack"
  - key: greek_yogurt
    name: "그릭요거트"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 60
    protein_g_per_100kcal: 6.0
    protein_g_per_100kcal_iqr: [5.2, 7.2]
    sodium_mg_per_100kcal: 22
    sodium_mg_per_100kcal_iqr: [13, 35]
    sodium_mg_per_g_protein: 3.2
    protein_tier: low
    sodium_tier: low
    serving_basis: "median package (n=46)"
    serving_kcal: 181
    serving_protein_g: 11.0
    serving_sodium_mg: 35
    allergens: [milk]
    dietary: vegetarian
    data_year: "2021..2026"
    note: "plain-labelled subset (n=11) also at median 6.0; sweetening is not what holds it down"
  - key: soy_milk
    name: "두유"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 80
    protein_g_per_100kcal: 5.6
    protein_g_per_100kcal_iqr: [4.0, 8.2]
    sodium_mg_per_100kcal: 110
    sodium_mg_per_100kcal_iqr: [62, 146]
    sodium_mg_per_g_protein: 18.5
    protein_tier: low
    sodium_tier: mid
    serving_basis: "median package (n=55)"
    serving_kcal: 95
    serving_protein_g: 6.0
    serving_sodium_mg: 120
    allergens: [soy]
    dietary: vegan
    data_year: "2019..2026"
  - key: sliced_cheese
    name: "슬라이스치즈"
    setting: convenience
    role: option
    db: processed-label
    kfind_code: "category median"
    n: 50
    protein_g_per_100kcal: 5.3
    protein_g_per_100kcal_iqr: [4.8, 6.2]
    sodium_mg_per_100kcal: 299
    sodium_mg_per_100kcal_iqr: [193, 341]
    sodium_mg_per_g_protein: 55.5
    protein_tier: low
    sodium_tier: high
    serving_basis: "multi-unit packs; per 100 kcal only"
    allergens: [milk]
    dietary: vegetarian
    data_year: "2022..2026"
  - key: milk_whole
    name: "우유"
    setting: convenience
    role: option
    db: standard-table
    kfind_code: "R113-009000000-0000"
    n: 1
    protein_g_per_100kcal: 4.6
    sodium_mg_per_100kcal: 60
    sodium_mg_per_g_protein: 12.9
    protein_tier: low
    sodium_tier: low
    serving_basis: "per 100 g only"
    allergens: [milk]
    dietary: vegetarian
    data_year: "2026 (table 10.4)"
  - key: triangle_kimbap
    name: "삼각김밥 (reference: the item a swap replaces)"
    setting: convenience
    role: baseline
    db: processed-label
    kfind_code: "category median"
    n: 60
    protein_g_per_100kcal: 2.6
    protein_g_per_100kcal_iqr: [2.2, 3.0]
    sodium_mg_per_100kcal: 218
    sodium_mg_per_100kcal_iqr: [182, 265]
    sodium_mg_per_g_protein: 82.0
    protein_tier: low
    sodium_tier: high
    serving_basis: "median package (n=60)"
    serving_kcal: 190
    serving_protein_g: 5.0
    serving_sodium_mg: 444
    allergens: [wheat, soy]
    dietary: omnivore
    data_year: "2020..2026"
    note: "baseline row, not a protein option"
  - key: cup_ramyeon
    name: "컵라면 (reference: the item a swap replaces)"
    setting: convenience
    role: baseline
    db: processed-label
    kfind_code: "category median"
    n: 40
    protein_g_per_100kcal: 2.0
    protein_g_per_100kcal_iqr: [1.8, 2.2]
    sodium_mg_per_100kcal: 465
    sodium_mg_per_100kcal_iqr: [374, 565]
    sodium_mg_per_g_protein: 223.6
    protein_tier: low
    sodium_tier: high
    serving_basis: "median package (n=34)"
    serving_kcal: 326
    serving_protein_g: 7.0
    serving_sodium_mg: 1460
    allergens: [wheat, soy]
    dietary: omnivore
    data_year: "2021..2026"
    note: "baseline row, not a protein option"
  - key: seolleongtang
    name: "설렁탕"
    setting: eating-out
    role: option
    db: dish-home-measured
    kfind_code: "D105-231000000-0001"
    n: 1
    protein_g_per_100kcal: 17.8
    sodium_mg_per_100kcal: 92
    sodium_mg_per_g_protein: 5.2
    protein_tier: lean
    sodium_tier: low
    serving_basis: "500g"
    serving_kcal: 120
    serving_protein_g: 21.3
    serving_sodium_mg: 110
    allergens: [beef]
    dietary: omnivore
    data_year: "2018"
    note: "analysed unsalted; table salt is added by the eater and is not in this sodium figure. Home-recipe analysis: for a RESTAURANT bowl quote the 2012-13 restaurant volume read for nutrition/kr-restaurant-dish-energy-ranking-022 (420 kcal, 60 g protein per serving), which K-FIND does not carry (v38 merge)"
  - key: seonji_haejangguk
    name: "선지해장국"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D305-256230000-0001"
    n: 1
    protein_g_per_100kcal: 15.9
    sodium_mg_per_100kcal: 990
    sodium_mg_per_g_protein: 62.3
    protein_tier: lean
    sodium_tier: high
    serving_basis: "1000g"
    serving_kcal: 310
    serving_protein_g: 49.3
    serving_sodium_mg: 3070
    allergens: [beef]
    dietary: omnivore
    data_year: "2017"
  - key: hwangtae_haejangguk
    name: "황태해장국"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D305-258000000-0001"
    n: 1
    protein_g_per_100kcal: 13.6
    sodium_mg_per_100kcal: 853
    sodium_mg_per_g_protein: 62.7
    protein_tier: mid
    sodium_tier: high
    serving_basis: "600g"
    serving_kcal: 180
    serving_protein_g: 24.5
    serving_sodium_mg: 1536
    allergens: [fish, egg]
    dietary: pescatarian
    data_year: "2016"
  - key: shabu_beef
    name: "소고기 샤브샤브"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D306-287180000-0001"
    n: 1
    protein_g_per_100kcal: 11.0
    sodium_mg_per_100kcal: 425
    sodium_mg_per_g_protein: 38.6
    protein_tier: mid
    sodium_tier: high
    serving_basis: "600g"
    serving_kcal: 264
    serving_protein_g: 29.1
    serving_sodium_mg: 1122
    allergens: [beef, wheat, soy]
    dietary: omnivore
    data_year: "2016"
    note: "shared pot; serving is the analysed pot, not one person"
  - key: gomtang
    name: "곰탕"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D305-203000000-0001"
    n: 1
    protein_g_per_100kcal: 10.6
    sodium_mg_per_100kcal: 392
    sodium_mg_per_g_protein: 36.9
    protein_tier: mid
    sodium_tier: high
    serving_basis: "300g"
    serving_kcal: 183
    serving_protein_g: 19.4
    serving_sodium_mg: 717
    allergens: [beef]
    dietary: omnivore
    data_year: "2016"
    note: "salted as served; rice not included"
  - key: salmon_grilled
    name: "연어구이"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D308-388000000-0001"
    n: 1
    protein_g_per_100kcal: 10.6
    sodium_mg_per_100kcal: 68
    sodium_mg_per_g_protein: 6.4
    protein_tier: mid
    sodium_tier: low
    serving_basis: "per 100 g only"
    allergens: [fish]
    dietary: pescatarian
    data_year: "2022"
  - key: samgyetang
    name: "삼계탕"
    setting: eating-out
    role: option
    db: dish-home-measured
    kfind_code: "D105-228000000-0001"
    n: 1
    protein_g_per_100kcal: 10.6
    sodium_mg_per_100kcal: 81
    sodium_mg_per_g_protein: 7.7
    protein_tier: mid
    sodium_tier: low
    serving_basis: "900g"
    serving_kcal: 909
    serving_protein_g: 96.1
    serving_sodium_mg: 738
    allergens: [chicken]
    dietary: omnivore
    data_year: "2018"
    note: "home-recipe analysis; no restaurant-analysed entry in K-FIND. The 2012-13 restaurant volume read for nutrition/kr-restaurant-dish-energy-ranking-022 carries a restaurant 삼계탕 (glutinous rice inside the bird); use 022 for a restaurant serving (v38 merge)"
  - key: chodang_sundubu
    name: "초당순두부 (백순두부)"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D305-252000000-0001"
    n: 1
    protein_g_per_100kcal: 9.4
    sodium_mg_per_100kcal: 231
    sodium_mg_per_g_protein: 24.5
    protein_tier: mid
    sodium_tier: high
    serving_basis: "900g"
    serving_kcal: 522
    serving_protein_g: 49.1
    serving_sodium_mg: 1206
    allergens: [soy]
    dietary: vegetarian
    data_year: "2016"
  - key: ojingeo_bokkeum
    name: "오징어볶음"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D310-488000000-0001"
    n: 1
    protein_g_per_100kcal: 8.6
    sodium_mg_per_100kcal: 336
    sodium_mg_per_g_protein: 39.2
    protein_tier: mid
    sodium_tier: high
    serving_basis: "per 100 g only"
    allergens: [mollusc, soy, wheat]
    dietary: pescatarian
    data_year: "2022"
  - key: fried_chicken
    name: "후라이드치킨 (프랜차이즈 신고값)"
    setting: eating-out
    role: option
    db: dish-franchise-label
    kfind_code: "category median"
    n: 8
    protein_g_per_100kcal: 8.6
    protein_g_per_100kcal_iqr: [7.4, 9.0]
    sodium_mg_per_100kcal: 109
    sodium_mg_per_100kcal_iqr: [82, 139]
    sodium_mg_per_g_protein: 12.6
    protein_tier: mid
    sodium_tier: mid
    serving_basis: "multi-unit packs; per 100 kcal only"
    allergens: [chicken, wheat]
    dietary: omnivore
    data_year: "2023..2023"
    note: "franchise-submitted values per 100 g; 2023 collection"
  - key: andong_jjimdak
    name: "안동찜닭"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D307-318140000-0001"
    n: 1
    protein_g_per_100kcal: 8.4
    sodium_mg_per_100kcal: 400
    sodium_mg_per_g_protein: 47.8
    protein_tier: mid
    sodium_tier: high
    serving_basis: "1500g"
    serving_kcal: 1365
    serving_protein_g: 114.2
    serving_sodium_mg: 5460
    allergens: [chicken, soy, wheat]
    dietary: omnivore
    data_year: "2016"
    note: "1.5 kg analysed dish is a shared platter"
  - key: godeungeo_jjigae
    name: "고등어찌개"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D306-262000000-0001"
    n: 1
    protein_g_per_100kcal: 8.2
    sodium_mg_per_100kcal: 431
    sodium_mg_per_g_protein: 52.9
    protein_tier: mid
    sodium_tier: high
    serving_basis: "600g"
    serving_kcal: 600
    serving_protein_g: 48.9
    serving_sodium_mg: 2586
    allergens: [fish, soy]
    dietary: pescatarian
    data_year: "2016"
  - key: sundaeguk
    name: "순대국"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D305-234000000-0001"
    n: 1
    protein_g_per_100kcal: 8.0
    sodium_mg_per_100kcal: 276
    sodium_mg_per_g_protein: 34.6
    protein_tier: mid
    sodium_tier: high
    serving_basis: "800g"
    serving_kcal: 544
    serving_protein_g: 43.5
    serving_sodium_mg: 1504
    allergens: [pork, wheat]
    dietary: omnivore
    data_year: "2012"
    note: "rice served separately is not included"
  - key: dakgalbi
    name: "닭갈비 (닭볶음)"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D310-462000000-0004"
    n: 1
    protein_g_per_100kcal: 7.7
    sodium_mg_per_100kcal: 258
    sodium_mg_per_g_protein: 33.4
    protein_tier: low
    sodium_tier: high
    serving_basis: "400g"
    serving_kcal: 596
    serving_protein_g: 45.9
    serving_sodium_mg: 1536
    allergens: [chicken, soy, wheat]
    dietary: omnivore
    data_year: "2016"
  - key: sogogi_gukbap
    name: "소고기국밥"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D301-004280000-0001"
    n: 1
    protein_g_per_100kcal: 6.6
    sodium_mg_per_100kcal: 543
    sodium_mg_per_g_protein: 82.0
    protein_tier: low
    sodium_tier: high
    serving_basis: "700g"
    serving_kcal: 329
    serving_protein_g: 21.8
    serving_sodium_mg: 1785
    allergens: [beef]
    dietary: omnivore
    data_year: "2016"
    note: "rice included"
  - key: kimchi_jjigae
    name: "김치찌개"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D306-266000000-0001"
    n: 1
    protein_g_per_100kcal: 6.2
    sodium_mg_per_100kcal: 805
    sodium_mg_per_g_protein: 130.2
    protein_tier: low
    sodium_tier: high
    serving_basis: "400g"
    serving_kcal: 244
    serving_protein_g: 15.1
    serving_sodium_mg: 1964
    allergens: [pork, soy, fish]
    dietary: omnivore
    data_year: "2012"
  - key: modum_chobap
    name: "모듬초밥"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D301-042200000-0001"
    n: 1
    protein_g_per_100kcal: 5.5
    sodium_mg_per_100kcal: 210
    sodium_mg_per_g_protein: 38.1
    protein_tier: low
    sodium_tier: high
    serving_basis: "300g"
    serving_kcal: 462
    serving_protein_g: 25.4
    serving_sodium_mg: 969
    allergens: [fish, soy, wheat]
    dietary: pescatarian
    data_year: "2012"
  - key: donkkaseu
    name: "돈가스"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D312-550000000-0002"
    n: 1
    protein_g_per_100kcal: 4.9
    sodium_mg_per_100kcal: 123
    sodium_mg_per_g_protein: 24.8
    protein_tier: low
    sodium_tier: mid
    serving_basis: "per 100 g only"
    allergens: [pork, wheat, egg, milk]
    dietary: omnivore
    data_year: "2022"
  - key: pho
    name: "쌀국수"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D303-162000000-0001"
    n: 1
    protein_g_per_100kcal: 4.9
    sodium_mg_per_100kcal: 519
    sodium_mg_per_g_protein: 105.8
    protein_tier: low
    sodium_tier: high
    serving_basis: "600g"
    serving_kcal: 318
    serving_protein_g: 15.6
    serving_sodium_mg: 1650
    allergens: [beef, fish]
    dietary: omnivore
    data_year: "2016"
  - key: budae_jjigae
    name: "부대찌개"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D306-284000000-0004"
    n: 1
    protein_g_per_100kcal: 4.6
    sodium_mg_per_100kcal: 578
    sodium_mg_per_g_protein: 126.1
    protein_tier: low
    sodium_tier: high
    serving_basis: "600g"
    serving_kcal: 402
    serving_protein_g: 18.4
    serving_sodium_mg: 2322
    allergens: [pork, wheat, milk, soy]
    dietary: omnivore
    data_year: "2016"
  - key: kongguksu
    name: "콩국수"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D303-175000000-0001"
    n: 1
    protein_g_per_100kcal: 4.6
    sodium_mg_per_100kcal: 97
    sodium_mg_per_g_protein: 21.0
    protein_tier: low
    sodium_tier: low
    serving_basis: "per 100 g only"
    allergens: [soy, wheat]
    dietary: vegetarian
    data_year: "2022"
  - key: hoedeopbap
    name: "회덮밥"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D301-051000000-0001"
    n: 1
    protein_g_per_100kcal: 4.4
    sodium_mg_per_100kcal: 109
    sodium_mg_per_g_protein: 24.7
    protein_tier: low
    sodium_tier: mid
    serving_basis: "500g"
    serving_kcal: 685
    serving_protein_g: 30.2
    serving_sodium_mg: 745
    allergens: [fish, soy, wheat]
    dietary: pescatarian
    data_year: "2012"
  - key: bibimbap
    name: "비빔밥"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D301-018000000-0002"
    n: 1
    protein_g_per_100kcal: 3.1
    sodium_mg_per_100kcal: 223
    sodium_mg_per_g_protein: 70.9
    protein_tier: low
    sodium_tier: high
    serving_basis: "per 100 g only"
    allergens: [egg, soy, wheat]
    dietary: omnivore
    data_year: "2022"
  - key: mul_naengmyeon
    name: "물냉면"
    setting: eating-out
    role: option
    db: dish-restaurant-measured
    kfind_code: "D303-144180000-0001"
    n: 1
    protein_g_per_100kcal: 3.0
    sodium_mg_per_100kcal: 526
    sodium_mg_per_g_protein: 174.4
    protein_tier: low
    sodium_tier: high
    serving_basis: "per 100 g only"
    allergens: [buckwheat, wheat, beef, egg]
    dietary: omnivore
    data_year: "2022"
  - key: kimchi_ramyeon
    name: "김치라면 (분식점)"
    setting: eating-out
    role: baseline
    db: dish-restaurant-measured
    kfind_code: "D303-148050000-0001"
    n: 1
    protein_g_per_100kcal: 2.5
    sodium_mg_per_100kcal: 458
    sodium_mg_per_g_protein: 183.5
    protein_tier: low
    sodium_tier: high
    serving_basis: "650g"
    serving_kcal: 552
    serving_protein_g: 13.8
    serving_sodium_mg: 2528
    allergens: [wheat, soy]
    dietary: omnivore
    data_year: "2015"
    note: "baseline row, not a protein option"
refraction_notes:
  - note: >
      PRODUCT ROWS ARE LABEL DECLARATIONS, NOT ANALYSES. Every 가공식품 entry
      read for this table is marked 데이터 생성 방법 수집 (collected from the
      manufacturer's declaration). Some entries contradict each other: the
      same yogurt line appears as 188 kcal / 23 g protein per 100 mL
      (P119-202040200-0635) and as 86 kcal / 10.95 g (P119-202040200-1559),
      which reads like a per-pack value filed as per-100. The category
      medians and interquartile ranges blunt such errors; a single named
      product does not. Quote the median, never one product as typical.
    grade: B
  - note: >
      DISH ROWS ARE ONE ANALYSED SERVING, MOSTLY OLD. Each 외식 row is one
      analysed dish from 2012-2022 with no spread across restaurants, and the
      database's own sub-sources disagree: 순대국 analysed as a home recipe
      gives 2.8 g protein per 100 kcal (D105-234000000-0001) against 8.0 for
      the restaurant analysis used here (D305-234000000-0001). The ORDER of
      dishes far apart in the table (a 해장국 against a 냉면) is safe to say;
      a gap of one or two units between neighbours is within that noise.
    grade: C
  - note: >
      CALCULATED DISH ROWS WERE EXCLUDED, AND WHY. K-FIND also carries
      2022-2024 외식 rows built by calculation (데이터 생성 방법 산출, flagged
      on the page "참고치로 활용"). Their sodium is not usable for ranking: the
      calculated 라면 row gives 58 mg per 100 mL (D403-148000000-0001), while
      the analysed 김치라면 gives 389 mg per 100 g (D303-148050000-0001) and
      the median cup-ramyeon label in this table carries 1,460 mg per pack.
      Only analysed (분석) restaurant rows are used; two rows with no restaurant
      analysis (삼계탕, 설렁탕) use the home-recipe analysis and are flagged.
    grade: B
  - note: >
      THE SODIUM TIER IS A LABEL-BUDGET SHARE, NOT A HEALTH LIMIT. It says how
      much of the 2,000 mg label reference a food spends per 100 kcal. Whether
      and how far an individual should cut sodium is not settled here; this
      warehouse has not researched sodium outcomes (014). With a stated
      cardiovascular or renal condition, a clinician's sodium and protein
      limits override this table: speak the sodium column first and do not
      call any row safe.
    axis: cardiovascular_condition
    grade: D
  - note: >
      RENAL CONDITION. Every swap in this table moves intake toward more
      protein. Where a renal condition is stated, the protein target itself is
      a clinical question (002 does not apply), so present the table as
      composition data only and suggest no swap that raises protein.
    axis: renal_condition
    grade: D
  - note: >
      DIETARY PATTERN. Filter on the dietary field (vegan, vegetarian,
      pescatarian, omnivore, each admitting the ones before it). For a vegan
      pattern the lean tier is empty in this table; the best rows are packaged
      tofu (median 9.5 g per 100 kcal, sodium near zero) and soy milk (5.6),
      and the honest line is that no vegan convenience row reaches the lean
      tier here.
    axis: dietary_pattern
    grade: C
claim: >
  Per 100 kcal, the Korean convenience store's strongest protein rows are
  ready-to-eat chicken breast (median 20.0 g protein per 100 kcal across 79
  labelled products, interquartile 16.8-21.1) and milk-protein ready-to-drink
  beverages (median 18.2, n=61); these are the only two convenience
  categories at or above 15 g per 100 kcal. Next come canned tuna (11.7),
  chicken-breast sausage (10.9), roasted or smoked eggs (10.0) and packaged
  tofu (9.5). String cheese, protein bars, Greek yogurt, soy milk, milk and
  sliced cheese all sit below 8 g per 100 kcal: they add protein but barely
  raise a meal's protein share. The two usual items a swap replaces,
  triangle kimbap (2.6) and cup ramyeon (2.0), sit at the bottom. Sodium
  splits the leaders: RTD protein drinks run 94 mg per 100 kcal (under
  label parity), chicken breast 296 mg (about three times its calorie share
  of the label sodium budget, about 380 mg in a median pack, interquartile
  200-388 mg per 100 kcal), tofu near zero. Eating out, the protein-dense dishes
  are almost all soups and stews -- 선지해장국 15.9, 황태해장국 13.6, beef
  shabu-shabu 11.0, 곰탕 10.6 -- and the two 해장국 carry the highest
  sodium per 100 kcal of any row in the table (990 and 853 mg); one
  analysed 선지해장국 bowl holds 49 g protein and 3,070 mg sodium. 삼계탕
  (10.6, 81 mg per 100 kcal, home-recipe analysis) and grilled salmon (10.6,
  68 mg) are the dishes that are both protein-dense and low in sodium.
  Rice- and noodle-based single dishes -- 비빔밥, 회덮밥, 콩국수, 쌀국수,
  물냉면, 초밥 -- sit under 6.
reasoning: >
  Every number is a K-FIND value read on 2026-10-07 and divided out. Protein
  per 100 kcal is the ranking key because it is serving-independent and is
  the density term the shipped diet engine already uses. Sodium is carried
  both per 100 kcal (the label-budget view) and per gram of protein (the
  swap view: what each gram of protein costs in sodium). Category rows are
  medians with interquartile ranges over the labelled products the database
  returns for the category, because single-product values vary widely and
  some are mis-filed. Dish rows are single restaurant analyses, which is why
  the dish ranking is spoken only between rows that sit far apart.
  WHY THE GRADE IS NOT HIGHER. The values are official, but processed rows
  are what the manufacturer declared, dish rows are one serving analysed up
  to fourteen years ago, and the only chemical check of the Korean tables is
  a single 2003 study (016). Label declarations also carry legal tolerances
  that were not read in this pass. The ranking holds where gaps are large
  (20 against 2.6 g per 100 kcal), not between neighbours a unit apart.
  WHAT THIS ITEM REFUSES. It names product CATEGORIES, not brands, as the
  options; brand names appear only in the RTD sample note so the median can
  be traced, because brand lines change faster than the database. It gives
  no per-serving figure where the database gives no serving. It makes no
  health claim for any sodium tier. And it does not decide whether the diet
  card may suggest foods the owner has never logged: the shipped contract
  says it may not, and changing that is a product decision.
---

# nutrition/kr-convenience-protein-options-030

편의점에서 단백질을 채우려 할 때 기준은 "단백질이 몇 그램 들었나"가 아니라
"100 kcal당 단백질이 몇 그램인가"다. 앞의 것은 포장 크기에 따라 달라지고,
뒤의 것은 그 음식이 끼니의 단백질 비율을 끌어올리는지 아닌지를 바로
보여준다. 이 항목의 모든 숫자는 식약처 식품영양성분 데이터베이스(K-FIND)에서
2026-10-07에 직접 읽은 값이다.

편의점 쪽 결론은 짧다. 100 kcal당 15 g을 넘는 건 즉석 닭가슴살(중앙값 20 g,
79개 제품)과 우유단백 고단백 음료(18 g, 61개 제품) 두 범주뿐이다. 그다음이
참치캔, 닭가슴살 소시지, 구운란, 두부로 10 g 안팎이다. 스트링치즈, 단백질바,
그릭요거트, 두유, 우유, 슬라이스치즈는 모두 8 g 아래다. 단백질을 더하긴
하지만 끼니의 단백질 비율은 크게 바꾸지 못한다. 바꾸려는 대상인 삼각김밥과
컵라면은 2-3 g으로 맨 아래에 있다.

나트륨은 상위권을 둘로 가른다. 고단백 음료는 100 kcal당 94 mg으로 표시
기준치(2,000 kcal에 2,000 mg)의 열량 몫보다 낮다. 닭가슴살은 296 mg으로 그
몫의 약 세 배를 쓰고, 제품마다 편차가 크다. 두부는 거의 0이다.

외식에서 단백질 밀도가 높은 건 대부분 국물 요리다. 선지해장국, 황태해장국,
소고기 샤브샤브, 곰탕이 그렇다. 그런데 두 해장국은 100 kcal당 나트륨이 표 전체에서
가장 높다. 분석된 선지해장국 한 그릇에는 단백질 49 g과 함께 나트륨
3,070 mg이 들어 있다. 단백질도 높고 나트륨도 낮은 외식 메뉴는 삼계탕과
연어구이 정도다. 비빔밥, 회덮밥, 콩국수, 쌀국수, 물냉면, 초밥처럼 밥이나 면이
중심인 단품은 100 kcal당 6 g이 안 된다.

이 숫자를 얼마나 믿어도 되는지도 같이 말해야 한다. 가공식품 값은 업체가
신고한 값이라 분석값이 아니다. 같은 제품이 한 번은 100 mL당 188 kcal로, 한
번은 86 kcal로 올라가 있는 경우도 있어서 제품 하나가 아니라 범주의 중앙값을
쓴다. 외식 값은 식당 한 곳의 한 그릇을 2012-2022년에 분석한 것이고, 같은
순대국이라도 출처에 따라 100 kcal당 2.8 g과 8.0 g으로 갈린다. 그래서 순위는
멀리 떨어진 항목 사이에서만 말한다. 해장국이 냉면보다 단백질 밀도가 높다는
말은 해도 되지만, 한두 칸 차이인 이웃끼리 순서를 매기는 건 잡음 안의 일이다.
계산으로 만든 외식 값(산출)은 쓰지 않았다. 계산된 라면 행은 나트륨이 100 mL당
58 mg인데, 분석된 김치라면은 100 g당 389 mg이고 컵라면 표시값 중앙값은 한 개에
1,460 mg이다.

나트륨 등급은 표시 기준치 대비 몫일 뿐 건강 기준이 아니다. 이 창고는 나트륨과
건강 결과의 관계를 아직 조사하지 않았다. 심혈관이나 신장 질환이 있다고 했다면
의료진이 정한 나트륨·단백질 한도가 이 표보다 우선하고, 단백질을 늘리는 쪽의
대체안은 내지 않는다.

마지막 경계. 지금 식단 카드의 "뭐 먹지"는 사용자가 기록한 적 있는 음식만
이름으로 말하도록 되어 있다. 이 표를 써서 처음 보는 음식을 권할지는 제품
결정이고, 이 항목이 내리는 결정이 아니다.
