---
# Authored 2026-09-02 (nutrition craft-lane opening, @meal-craft). KR-LOCALE.
# The evidence lane owns the protein TARGET (per-kg range, item 002; the Korean
# national reference standard, item 014). Neither says anything about hitting a
# target off a Korean plate, which is the only form the question ever actually
# arrives in. That is this item.
# It also carries the lane's one explicit CRAFT-CONTRADICTS-EVIDENCE statement:
# the per-meal even-distribution prescription that practitioners teach
# universally is not supported by this warehouse's evidence lane, and is kept
# here only on a different justification, stated out loud.
id: nutrition/kr-protein-exchange-counting-021
domain: nutrition
lane: "@meal-craft"
grade: D (professional-tool convention)
locale: KR
as_of: 2026
contested: no
sources:
  - "https://www.diabetes.or.kr/general/dietary/dietary_03.php"  # Korean Diabetes Association (대한당뇨병학회), 즐거운 식사계획 -- the 식품교환표 per-exchange nutrient content used for every number in this item, retrieved directly
  - "source:nutrition/protein-intake-002 -- the per-kilogram training target this item converts into countable units. That item owns the number; this one owns the arithmetic"
  - "source:nutrition/kr-reference-intakes-2025-014 -- the Korean national reference standard, a DIFFERENT construct that must not be substituted for the training target"
  - "source:nutrition/self-report-underreporting-007 -- protein is under-reported LESS than energy, which is half of why protein is the more trustworthy column"
  - "source:nutrition/kr-food-composition-accuracy-016 -- the Korean composition tables validated at 101% for protein, which is the other half, and which is a single contested 2003 study and must not be spoken as a guarantee"
  - "source:nutrition/protein-per-meal-ceiling-008 -- the de-escalated per-meal ceiling"
  - "source:nutrition/protein-distribution-thin-009 -- the thin distribution evidence that this item's per-meal practice deliberately does NOT lean on"
  - "source:nutrition/kr-mixed-dish-logging-unit-020 -- the unit convention this item counts in"
  - "framework:VC-E craft -- the exchange values are a published clinical-dietetics tool and are quoted exactly; the counting strategy built on them is a convention, and the ranking of protein as the log's most trustworthy column is a RELATIVE ordering among biased numbers, not an accuracy claim"
applicability:
  axes:
    - key: dietary_pattern
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
claim: >
  On a Korean plate, protein arrives through one door. In the exchange system
  used by Korean dietetic practice, a meat-and-fish exchange carries 8 g of
  protein regardless of its fat tier, and a milk exchange carries 6 g; a grain
  exchange carries 2 g and a vegetable exchange 2 g, and a fruit or fat exchange
  carries none. A conventional 밥 + 국 + 나물 반찬 built from two grain and two
  vegetable exchanges therefore delivers about 8 g of protein in total -- one
  meat-and-fish exchange's worth -- which means a training protein target is met
  almost entirely by the 반찬 side and essentially not at all by the 주식. The
  operational form: convert the daily target into meat-and-fish exchanges by
  dividing by 8, count exchanges rather than estimating grams, and treat the
  exchange as the smallest unit the instrument can honestly resolve. Ranking
  among unreliable columns: protein is the number in a Korean log most worth
  acting on, because it is under-reported less than energy and because the one
  chemical validation of the Korean composition tables put protein at 101
  percent of measured -- but that is a ranking among biased figures, not a claim
  that the protein number is right.
reasoning: >
  Every quantity above is quoted from the published exchange system rather than
  derived, and the arithmetic on top of it is arithmetic, not a finding. Grading
  stays at the practitioner-tool band because the CHOICE to count in exchanges is
  a convention: no study was located comparing exchange-unit counting against
  gram estimation for accuracy or for adherence in any population. It is argued
  from the measurement position the lane already holds -- the portion step is a
  plus-or-minus-25-percent instrument at best and fails outright on the amorphous
  staples a Korean plate is built from -- so a unit finer than the exchange is a
  unit the instrument cannot resolve.
  WHERE CRAFT AND EVIDENCE DISAGREE, STATED RATHER THAN RESOLVED QUIETLY. Coaching
  practice near-universally prescribes an even per-meal protein split, typically
  four meals of roughly 30-40 g. This warehouse's evidence lane does not support
  that prescription: nutrition/protein-distribution-thin-009 traces the
  even-distribution concept to an n=8 acute crossover with two later randomised
  trials returning null at real outcomes, and nutrition/protein-per-meal-ceiling-008
  removed the basis for warning anyone that protein above roughly 40 g in one
  sitting is wasted. A per-meal split is therefore still a reasonable thing for
  this lane to suggest, but ONLY on the ground it can actually defend -- an
  exchange count spread across meals is easier to hit and easier to log than a
  single daily total reconciled at midnight -- and never on the physiological
  ground practitioners usually give for it. Anyone stating the split must state
  which justification they are using.
  A SECOND BOUNDARY, carried from item 014: the Korean national reference intake
  is a population adequacy standard expressed per day and as an energy
  percentage. It is not the per-kilogram training range, the two answer different
  questions, and neither may be shown as a correction to the other.
---

# nutrition/kr-protein-exchange-counting-021

한국 식단에서 단백질은 문이 하나다. 식품교환표 기준으로 어육류군 1교환은
지방 등급과 무관하게 단백질 8 g이고, 우유군 1교환이 6 g이다. 곡류군은 1교환에
2 g, 채소군도 2 g, 과일군과 지방군은 0이다.

이 숫자를 실제 상에 대보면 결론이 바로 나온다. 밥 두 교환에 나물 반찬 두
교환으로 차린 밥+국+반찬 한 끼의 단백질은 다 합쳐 8 g 남짓, 어육류군 한
교환어치다. 즉 훈련하는 사람의 단백질 목표는 주식이 아니라 반찬 쪽에서
거의 전부 나온다. 목표치를 8로 나누면 필요한 어육류군 교환 수가 그대로
나오고, 그 수가 하루 상차림에서 눈으로 셀 수 있는 유일한 단위다.

그램 대신 교환을 세는 이유는 정밀해서가 아니라 그 반대다. 이 레인의 다른
항목이 보여주듯 눈대중 양 추정은 잘해야 ±25%이고, 밥이나 생선 토막처럼
한국 상에서 정작 중요한 형태에서는 그마저 무너진다. 도구가 분해하지 못하는
눈금을 기록에 적는 건 정밀함이 아니라 허구다.

그럼에도 단백질은 이 기록에서 가장 믿고 움직일 만한 칸이다. 자기보고에서
단백질은 열량보다 덜 누락되고, 한국 식품성분표를 화학 분석과 맞춰본 유일한
연구에서 단백질은 실측 대비 101%로 나왔다. 다만 그 연구는 2003년 제주
여성 66명짜리 단일 연구이고 이 창고에서 논쟁 표시가 붙어 있다. 그러니
"가장 믿을 만하다"는 건 틀린 숫자들 사이의 순위지, 맞는 숫자라는 뜻이 아니다.

실무와 근거가 갈리는 지점은 숨기지 않고 적는다. 코칭 현장은 거의 예외 없이
끼니당 30-40 g씩 네 번으로 고르게 나누라고 가르친다. 이 창고의 근거 레인은
그 처방을 받쳐주지 않는다 -- 균등 분배 개념의 양성 결과는 n=8 급성 교차설계
하나이고 실제 결과 지표를 본 무작위 시험 둘은 무효로 나왔으며, 한 끼 40 g
넘는 단백질이 낭비된다고 경고할 근거도 이미 철회됐다. 그래서 끼니 분배는
여전히 권할 만하지만, 권하는 이유가 달라진다: 생리학이 아니라 기록
가능성이다. 하루 총량을 자정에 몰아서 맞추는 것보다 끼니마다 교환 수를 세는
쪽이 실제로 지켜지고 실제로 기록된다. 이 이유로 권하는 것과 근육 합성
논리로 권하는 것은 다른 주장이고, 말할 때 어느 쪽인지 밝혀야 한다.

마지막 경계 하나. 한국인 영양소 섭취기준의 단백질 수치는 인구집단 적정
섭취 기준이며 하루 그램과 에너지 비율로 표현된다. 체중 킬로그램당으로
표현되는 훈련 목표와는 서로 다른 질문에 대한 답이고, 한쪽을 다른 쪽의
교정값처럼 보여주면 안 된다.
