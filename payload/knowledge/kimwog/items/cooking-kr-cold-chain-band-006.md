---
# Authored 2026-09-02 (cooking-lane collection sprint). KR-LOCALE item, @food-safety.
# Filed because a cooking-session consumer that quotes storage durations is
# implicitly assuming a fridge temperature, and the Korean legal assumption is
# NOT the 4C an English-language source would assume. The divergence is
# internal to Korean guidance itself: the legal band tops out at 10C while the
# regulator's own food-poisoning advice says 5C.
id: cooking/kr-cold-chain-band-006
domain: cooking
lane: "@food-safety"
grade: A (jurisdictional-standard)
locale: KR
as_of: 2026-09-02
contested: no
sources:
  - "https://www.korea.kr/multi/visualNewsView.do?newsId=148893687"  # Ministry of Food and Drug Safety (식품의약품안전처), 정책브리핑 (korea.kr, the Korean government's official policy portal), 2021-09-29: 꼭 알아야 할 식품별 보존 및 유통 온도. The ministry's own presentation of the Food Code preservation/distribution temperatures. Retrieved 2026-09-02
  - "https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2100000177958"  # 식품의 기준 및 규격 (Food Standards and Specifications), 식품의약품안전처고시, National Law Information Center record. The administrative rule that carries the 보존 및 유통기준 these temperatures come from. Verified as the correct instrument and issuing agency; the 별표 text itself was NOT read at this URL (see refraction note)
  - "https://www.foodnews.co.kr/news/articleView.html?idxno=71829"  # 식품음료신문 (Korean food-industry trade press), report of 조윤미, C&I소비자연구소, presenting at the 한국식품위생안전성학회 제34차 정기학술대회, Gyeongju, 2019-11-08, arguing the 10C legal refrigeration ceiling should be reconsidered. Cited ONLY as evidence that the adequacy debate is live and public, not as evidence for any microbiological figure
  - "source:cooking/kr-core-temperatures-005 -- the COOKING side, and the source of the 5C 이하 food-poisoning recommendation this item contrasts with"
refraction_notes:
  - note: >
      DO NOT ASSUME A 4C FRIDGE. Almost every English-language food-safety rule a
      model has absorbed is written against a refrigerator at or below about 4C.
      Korea's legal band for a refrigerated product with no separate standard is
      0~10C. Its upper end is six degrees warmer, and it is inside the range
      where psychrotrophic pathogens still grow. Any storage duration spoken to a
      Korean user is therefore being quoted against a potentially warmer chain
      than the rule was written for. Speak durations conservatively and, where it
      matters, tell the user to set the appliance colder rather than to trust the
      legal band.
    grade: A
  - note: >
      THE STANDARD IS NOT DISPUTED; ITS ADEQUACY IS. The numbers themselves are a
      matter of published record and are not contested. What is publicly argued
      in Korea is whether a 10C ceiling is protective enough, and that debate is
      cited here from trade press reporting a conference presentation -- which is
      enough to establish that the argument exists and NOT enough to establish
      any microbiological claim. No pathogen growth-rate figure is taken from
      that source, and none should be.
    grade: C
  - note: >
      PROVENANCE OF THE NUMBERS. The temperature table was read from the
      ministry's own publication on the government policy portal, which is the
      regulator presenting its own standard. The underlying administrative rule
      was confirmed to exist, to be issued by the Ministry of Food and Drug
      Safety and to be titled 식품의 기준 및 규격, but the 별표 text carrying the
      보존 및 유통기준 could not be rendered at the law portal in this pass. Treat
      the figures as the regulator's own statement of its standard rather than as
      a verbatim reading of the legal annex. The v13 nutrition lesson applies:
      a jurisdiction-bound item needs an EDITION check, not just a source check,
      and this one has not had one.
    grade: C
  - note: >
      TIGHTER BANDS EXIST AND THEY BEAT THE GENERAL ONE. Meat, packaged meat and
      meat products sit at -2~10C; ground meat and poultry at -2~5C; prepared
      salads, smoked salmon and liquid egg at 0~5C. Where a specific category has
      its own band, that band governs. Never quote the general 0~10C figure at a
      food that has a stricter one.
    grade: A
claim: >
  Under the Korean Food Code (식품의 기준 및 규격, a Ministry of Food and Drug
  Safety notice), the preservation and distribution temperature bands for a food
  with no separately defined standard are: 온장 60C 이상, 실온 1~35C, 냉장 0~10C,
  냉동 -18C 이하. Stricter category bands override the general one: 식육
  (excluding ground and poultry), 포장육 and 식육가공품 at -2~10C or frozen at
  -18C 이하; 분쇄육, 가금육 and 분쇄가공육제품 at -2~5C or frozen; 샐러드, 훈제연어
  and 액란제품 at 0~5C or frozen; 원유, 우유류, 두부, 묵류 and 달걀 at 0~10C. The
  legal refrigeration ceiling of 10C is therefore WARMER than the 5C 이하 that the
  same ministry's food-poisoning prevention guidance recommends for holding food,
  and warmer than the roughly 4C assumed by most English-language storage advice.
reasoning: >
  Confidence here is about what the Korean standard says, and on that question
  the issuing ministry's own publication of its own figures is authoritative, so
  the item sits at the top band with a jurisdictional qualifier. It earns its
  place not by being interesting but by being a silent premise: every storage
  duration a cooking consumer speaks -- three to five days for cooked meat, seven
  days for oily fish -- assumes a refrigerator temperature, and the assumption
  imported with English-language advice is about six degrees colder than what
  Korean law permits. That gap is exactly the class of error this lane already
  paid for once, when a US-only rule was nearly shipped as a Korean one. Two
  limits are carried openly. The legal annex text was not read directly, only the
  regulator's own presentation of it, and no edition check was performed, so the
  figures are recorded as current-as-presented rather than as verified against
  the standard in force. And the live Korean argument that 10C is too warm is
  cited only to show the argument exists; no microbiological number is taken from
  a trade-press report of a conference talk.
---

# cooking/kr-cold-chain-band-006

Every storage rule hides a fridge temperature inside it. "Cooked meat keeps
three to five days" is only true against some assumed cold-chain, and the
assumption baked into most English-language food-safety writing is a
refrigerator at or below about four degrees.

Korea's legal band is not that. Under the Korean Food Code, a refrigerated
product with no separate standard of its own may sit anywhere in 0~10C. Frozen
is -18C or below, room temperature is 1~35C, and hot-holding is 60C or above.
The refrigerated ceiling is six degrees warmer than the assumption, and it is
warmer than the 5C the same ministry recommends in its own food-poisoning
guidance -- an internal divergence between what the law permits and what the
regulator advises.

Some categories are held tighter, and where they are, the tighter band wins:

- 식육 (other than ground), 포장육, 식육가공품: -2~10C, or frozen at -18C or below
- 분쇄육, 가금육, 분쇄가공육제품: -2~5C, or frozen
- 샐러드, 훈제연어, 액란제품: 0~5C, or frozen
- 원유, 우유류, 두부, 묵류, 달걀: 0~10C

The practical consequence for a cooking session is small and concrete. Do not
recite a storage duration as if the fridge were at four degrees. If the duration
matters -- leftovers being kept for a second meal, banchan being made ahead,
oily fish waiting to be cooked -- the safer instruction is to set the appliance
colder than the legal band requires rather than to trust the band.

Two honesty notes. The figures here were read from the ministry's own
publication of its standard rather than from the legal annex itself, which could
not be rendered in this pass, and no check was made against the edition
currently in force. And there is a live public argument in Korea that a
ten-degree ceiling is not protective enough; that argument is recorded here as
existing, and nothing microbiological is taken from it.
