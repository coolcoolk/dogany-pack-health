---
# Authored 2026-09-02 (nutrition craft-lane opening, @meal-craft). KR-LOCALE.
# Source re-audit 2026-10-06: the 2013 dataset PDF, unread here before, was read in full; it confirms the 108-dish / 33-nutrient description; source note updated, claim unchanged; figures now in item 022.
# THE ITEM THIS LANE WAS OPENED FOR. The evidence lane searched the Korean
# mixed-dish logging error and REFUSED to publish a number, correctly: no
# primary source quantifies portion or nutrient error for 찌개 / 국 / 비빔밥 /
# 반찬 as logged by a consumer, and item 016 cannot supply it because its design
# removed exactly that error. This item does NOT fill that hole. It ships the
# HANDLING instead, and it names the handling as a convention with a known error
# SIGN rather than as an accuracy claim.
id: nutrition/kr-mixed-dish-logging-unit-020
domain: nutrition
lane: "@meal-craft"
grade: D (professional-tool convention)
locale: KR
as_of: 2013-2026
contested: no
sources:
  - "https://www.diabetes.or.kr/general/dietary/dietary_03.php"  # Korean Diabetes Association (대한당뇨병학회), 즐거운 식사계획 -- the 식품교환표 six-group exchange system with per-exchange nutrient content, retrieved directly
  - "https://www.gwanak.go.kr/site/educare/ex/bbs/View.do?cbIdx=256&bcIdx=41940"  # notice of the Ministry of Food and Drug Safety (식품의약품안전처) 외식 영양성분 자료집 vol.2: 108 of the most frequently eaten Korean restaurant dishes, 33 nutrients plus 26 fatty acids and 17 amino acids, built on 2010 국민영양조사 consumption data. PROVENANCE CAVEAT: read from a municipal repost of the ministry notice; the ministry's own copy of this notice was not retrieved in this pass
  - "https://foodsafetykorea.go.kr/upload/mkisna/2013.pdf"  # the 외식 영양성분 자료집 제2권 itself (식품의약품안전처, 2013.3). Read in full 2026-10-06: 108 dishes, 27 nutrients + 6 added nutrients, 26 fatty acids, 17 amino acids, per 1회 제공량 and per 100 g, each a mean of 72 samples, on 2010 국민건강영양조사 data -- the description above holds. Its numbers, with vol.1 (2012, 130 dishes), live in nutrition/kr-restaurant-dish-energy-ranking-022
  - "https://various.foodsafetykorea.go.kr/nutrient/"  # 식품안전나라 / K-FIND, the ministry-operated national food nutrition database that carries these values as a queryable store
  - "source:nutrition/kr-food-composition-accuracy-016 -- the evidence-lane item that measured the TABLE and explicitly refused the mixed-dish question"
  - "source:nutrition/portion-estimation-shape-ceiling-018 -- why itemising a composite dish cannot work: the portion step alone fails on exactly the amorphous components a 찌개 is made of"
  - "framework:VC-E craft -- two published professional tools (a clinical-dietetics exchange system and a government measured-dish dataset) define coarser units than grams. Their EXISTENCE and their unit definitions are checkable facts; the rule to log in them rather than in grams is a design convention, and is labelled as one"
claim: >
  For Korean composite dishes there is no defensible way to log in grams, and
  there are two published units coarser than grams to log in instead. The first
  is the clinical exchange system (식품교환표) used in Korean dietetic practice,
  which quantises food into six groups with fixed per-exchange content -- grain
  100 kcal / 23 g carbohydrate / 2 g protein; meat-and-fish 8 g protein per
  exchange at 50, 75 or 100 kcal depending on the fat tier; vegetable 20 kcal /
  3 g carbohydrate / 2 g protein; fat 45 kcal / 5 g fat; milk 6 g protein at 80
  or 125 kcal; fruit 50 kcal / 12 g carbohydrate. The second is the Ministry of
  Food and Drug Safety's measured restaurant-dish dataset (외식 영양성분
  자료집), which publishes whole-dish values for the most frequently eaten
  Korean 외식 dishes -- 108 of them in volume 2 alone, with 33 nutrients plus
  fatty-acid and amino-acid detail, on a defined per-serving basis. The craft
  rule: log a composite dish by its NAME against a measured whole-dish entry,
  or in exchange units, and do not itemise it into grams of each ingredient.
  For a genuinely shared dish, record only what can be named and counted -- the
  pieces of meat or fish actually taken -- and mark the shared broth or shared
  banchan as present-but-uncounted rather than apportioning it by a fraction
  nobody measured.
reasoning: >
  Both tools are real, published and checkable: the exchange system is the
  standard teaching instrument of Korean clinical dietetics and its per-exchange
  content was read from the Korean Diabetes Association's own page, and the
  restaurant dataset is a ministry publication carried in the national food
  nutrition database. What is NOT evidence is the rule built on top of them, and
  that distinction is the whole item. No study was located comparing itemised
  against whole-dish logging of a Korean composite dish for accuracy. The rule is
  argued, not measured: itemising a 찌개 requires a portion judgment for each
  component, and the portion step is measured elsewhere in this lane as a
  plus-or-minus-25-percent instrument at best and a failing one for amorphous
  foods, so an itemised 찌개 multiplies several failing estimates and then
  presents the product to four significant figures. A whole-dish entry makes one
  error instead of six and makes it a NAMED error attached to a published
  reference portion.
  THE SHARED-DISH CONVENTION IS THE WEAKEST THING HERE AND IS LABELLED AS SUCH.
  No published method for apportioning a shared Korean serving was located. The
  convention is not chosen because it is accurate; it is chosen because its error
  has a KNOWN SIGN. Counting only what you can name undercounts, which is the
  same direction as every other error in a food record
  (nutrition/self-report-underreporting-007), so it keeps the whole record a
  consistent floor. An invented apportionment fraction would have an unknown
  sign and would destroy that property. Say the undercount out loud when the
  record is used; never present a shared-dish day as a complete one.
  WHAT THIS ITEM REFUSES: any figure for how wrong a Korean mixed-dish log is.
  The evidence lane searched for one and found nothing, and item 016 cannot be
  extrapolated into one because its design fed correctly identified duplicate
  portions through the tables, removing precisely the portion and identification
  error this question is about. Craft does not get to fill an evidence hole by
  being confident.
---

# nutrition/kr-mixed-dish-logging-unit-020

김치찌개 한 그릇을 그램 단위로 기록하는 방법은 없다. 있는 것처럼 적는 순간
그 기록은 측정이 아니라 창작이 된다. 이 항목은 그 구멍을 숫자로 메우지
않는다 -- 대신 그램보다 거친, 실제로 출판되어 있는 두 개의 단위를 쓴다.

첫째는 식품교환표다. 한국 임상영양 실무의 표준 도구이고, 음식을 여섯 군으로
묶어 1교환단위의 영양소 함량을 고정한다. 곡류군 100 kcal에 탄수화물 23 g,
단백질 2 g. 어육류군은 지방 함량에 따라 50 / 75 / 100 kcal이지만 단백질은
어느 쪽이든 8 g으로 같다. 채소군 20 kcal에 탄수화물 3 g, 단백질 2 g. 지방군
45 kcal에 지방 5 g. 우유군 단백질 6 g. 과일군 50 kcal에 탄수화물 12 g. 이
체계의 미덕은 정밀함이 아니라 의도적으로 거친 눈금이다 -- 애초에 잴 수 없는
것을 재는 척하지 않는다.

둘째는 식약처의 외식 영양성분 자료집이다. 국민이 실제로 자주 먹는 외식
메뉴를 1인분 기준으로 실측해 놓은 정부 자료로, 제2권만 해도 108종에 영양성분
33종과 지방산·아미노산 정보가 붙어 있고, 같은 값들이 국가 식품영양성분
데이터베이스에 들어 있다. 김치찌개를 재료별로 쪼개지 말고 "김치찌개"라는
이름으로 기록하라는 말이다.

왜 쪼개면 안 되는가. 찌개를 재료 단위로 적으려면 각 재료마다 양을 눈대중해야
하는데, 이 레인의 다른 항목이 그 눈대중이 잘해야 ±25% 도구이고 밥처럼 형태가
없는 음식에서는 아예 실패한다는 걸 측정치로 보여준다. 여섯 번 실패한 추정을
곱한 값에 소수점을 붙여 내놓는 것보다, 한 번의 오차를 이름 붙은 기준 1인분에
붙여두는 편이 정직하다.

여럿이 먹는 상은 이 항목에서 가장 약한 부분이고, 약하다고 명시한다. 공유
찌개나 공유 반찬을 몇 분의 몇 먹었는지 배분하는 검증된 방법은 찾지 못했다.
그래서 규칙은 정확해서가 아니라 오차의 부호가 알려져 있어서 고른다: 셀 수
있는 것(내가 실제로 집은 고기·생선 조각)만 세고, 공유된 국물과 반찬은
"있었지만 세지 않음"으로 표시한다. 이러면 과소 기록이 되는데, 식사 기록의
다른 모든 오차와 방향이 같아서 기록 전체가 일관된 하한선으로 남는다. 지어낸
배분 비율은 부호를 알 수 없게 만들어 그 성질을 깨뜨린다. 대신 그 날의 기록을
쓸 때는 과소 기록이라는 사실을 반드시 같이 말할 것.

마지막으로, 이 항목이 하지 않는 것. 한국식 혼합 음식 기록이 얼마나 틀리는지에
대한 수치는 여기 없다. 근거 레인이 직접 찾아보고 없다고 기록했고, 조리 전
식품을 정확히 식별해 실험실에서 분석한 연구(이 도메인의 한국 성분표 검증
항목)로는 메울 수 없다 -- 그 설계는 지금 문제 삼는 바로 그 오차를 제거한
설계이기 때문이다. 실무 지식이라는 이유로 근거의 빈칸을 자신 있게 채우는 건
이 레인에서 허용되지 않는다.
