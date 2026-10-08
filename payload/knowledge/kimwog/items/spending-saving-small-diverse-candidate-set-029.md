---
# Shopping / decision sprint 2026-10-07 (dispatch task kw-sh-product-choice-overload).
# Sources read 2026-10-07 at the publisher / repository abstract; the UMUAI
# journal version (Springer) was paywalled and only its indexed abstract text
# was read. The "3-4" count is a product constant, labelled as such.
id: spending-saving/small-diverse-candidate-set-029
domain: spending-saving
grade: C (recommender user studies and lab experiments; the specific count is product judgement)
lane: "@household-behavioral"
locale: universal
as_of: 2005-2016
contested: no
sources:
  - "Willemsen, M. C., Graus, M. P. and Knijnenburg, B. P. (2016). Understanding the role of latent feature diversification on choice difficulty and satisfaction. User Modeling and User-Adapted Interaction 26(4), 347-389. https://doi.org/10.1007/s11257-016-9178-6 -- diversifying a recommendation set on latent features, holding overall quality constant, raised perceived diversity and attractiveness, lowered perceived choice difficulty, and could raise satisfaction with the chosen item, especially from SMALL, diverse sets (indexed abstract read; full text paywalled)."
  - "Willemsen, M. C., Knijnenburg, B. P., Graus, M. P., Velter-Bremmers, L. C. M. and Fu, K. (2011). Using latent features diversification to reduce choice difficulty in recommendation lists. RecSys 2011 Workshop on Human Decision Making in Recommender Systems (Decisions@RecSys'11), CEUR-WS Vol-811 -- the workshop precursor; diversity at constant attractiveness reduced trade-off and choice difficulty (abstract read at research.tue.nl)."
  - "Gourville, J. T. and Soman, D. (2005). Overchoice and Assortment Type: When and Why Variety Backfires. Marketing Science 24(3), 382-395. https://doi.org/10.1287/mksc.1040.0109 -- non-alignable variety raises effort and anticipated regret; simplifying presentation and reducing regret potential moderate it (abstract read)."
  - "spending-saving/choice-overload-conditional-028 -- the moderators this item operationalises"
  - "framework:product-constant -- the presented count of 3 to 4 is a design choice inside the range where small diverse sets were studied; no study compared 3 against 4 against 5 for this purpose (GAPS.md spending-saving v37)."
refraction_notes:
  - note: >
      DIVERSE MEANS DIFFERENT ON WHAT THE USER CARES ABOUT. The studies
      diversified on latent taste features while holding quality flat. A set of
      four near-duplicates with different colours is not diverse in that sense,
      and a set that spans quality levels is not what was tested either. Keep
      each candidate plausible; vary the trade-off it represents.
    grade: C
  - note: >
      VISUALLY DISTINCT IS A PRESENTATION RULE, NOT A FINDING. No study
      located tested visual distinctness of product cards as such. The rule
      follows from the alignability evidence (make the difference easy to see)
      and is carried at the practitioner band.
    grade: D
  - note: >
      THREE TO FOUR IS THE PLAN'S NUMBER. It sits inside the small-set range
      the diversification studies used and leaves room for one contrast per
      main trade-off. No head-to-head of 3 vs 4 vs 5 exists; speak it as the
      skill's rule.
    grade: D
claim: >
  When an agent shows candidates, a small set whose members differ in the
  trade-off they represent is easier to choose from, and no less satisfying,
  than a longer list of the top-scoring items. In recommender user studies,
  diversifying a set on the features that drive taste, while holding overall
  quality constant, raised perceived diversity and attractiveness, lowered
  perceived choice difficulty, and could raise satisfaction with the chosen
  item, with the benefit clearest for small sets. The way to show such a set
  follows from the alignability evidence: put candidates on the same one or two
  axes the user named, and make each one's distinguishing trade-off visible at
  a glance. The skill shows 3 to 4 candidates; that count is a product
  constant chosen inside the studied range, not a measured optimum.
reasoning: >
  The diversification work is the closest evidence to the exact act of a
  find-things skill -- a system choosing which few items to put in front of a
  person -- and it measures the outcomes that matter (difficulty, satisfaction
  with the pick). It stays at the observational/user-study band because the
  studies are user studies of recommendation lists whose outcomes are
  self-report scales rather than purchases, and the product domain and sample
  could not be read past the abstract. The count is
  carried as a constant for the same reason the caution ladder carries its
  weights as constants: the direction (small and diverse beats long and
  similar) has evidence, the number does not. A top-N list of near-identical
  best-scorers is the failure the item exists to prevent: it maximises the
  score of each slot and minimises the information the set gives the user.
---

# spending-saving/small-diverse-candidate-set-029 -- 후보는 적게, 서로 다르게

**한 줄 그림:** 점수 1~10등을 줄 세우지 말고, 서로 다른 장단점을 대표하는 후보 3~4개를 같은 기준
위에 나란히 보여 준다.

A recommender's instinct is to show the ten highest-scoring items. Those ten
tend to be near-copies of each other, so the list is long and tells the person
very little.

User studies on recommendation lists tested the alternative: keep quality
level the same, but pick items that differ on the features that drive taste.
The diverse sets looked more varied and more attractive, felt easier to choose
from, and the person was at least as happy with what they picked -- most
clearly when the set was small.

Two presentation rules follow from the overload evidence. Line candidates up
on the same one or two axes the user said they care about, because options that
differ on unrelated dimensions are the hardest to compare. And make each
candidate's distinguishing trade-off obvious -- "the cheapest", "the lightest",
"the longest warranty" -- so the difference is seen, not read.

## Presentation rule

| Rule | Basis | Band |
|---|---|---|
| show 3-4 candidates | product constant inside studied small-set range | constant |
| each candidate represents a different trade-off, all plausible | diversification at constant quality (Willemsen 2016) | C |
| same 1-2 user-named axes for every candidate | alignability (Gourville and Soman 2005), 028 | C |
| each card leads with its one distinguishing label | follows from the above; not tested as such | D |
| no near-duplicates (same model, other colour) as separate slots | diversity definition | D |

## 한국어 요약 (답변용)

- 점수 높은 순으로 10개를 늘어놓으면 서로 비슷한 것끼리 길어지기만 하고 정보는 적다.
- 품질 수준은 비슷하게 두고 취향을 가르는 특징이 서로 다른 후보로 묶으면, 더 다양하고 매력적으로
  보이고 고르기 쉬워지며 고른 것에 대한 만족도 떨어지지 않는다. 후보 수가 적을 때 효과가 가장 분명했다.
- 모든 후보를 사용자가 말한 기준 한두 개 위에 나란히 놓는다. 서로 다른 축에서 다른 후보가 가장 비교하기
  어렵다.
- 후보마다 "가장 쌈", "가장 가벼움"처럼 차이 하나를 맨 앞에 보여 준다.
- 3~4개라는 숫자는 제품이 정한 규칙이다. 3개와 5개를 직접 비교한 연구는 없다.
