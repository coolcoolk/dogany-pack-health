---
# Authored 2026-09-02 (cooking-session craft sprint). KR-LOCALE item, @food-safety.
# LANE CHOICE STATED UP FRONT, because this sprint is otherwise a craft sprint:
# this item is a regulator's own instruction plus a named organism, which is the
# VC-F culture, not the VC-E craft one. Lane follows the verification culture,
# never the sprint theme. It is filed first in this batch on purpose -- every
# craft item that follows defers to it by ID rather than by hand-waving at
# "safety".
id: cooking/session-holding-fence-014
domain: cooking
lane: "@food-safety"
grade: A (jurisdictional-guidance)
locale: KR
as_of: 2024-10-11
contested: no
sources:
  - "https://www.korea.kr/news/healthView.do?newsId=148934234"  # 식품의약품안전처 (Ministry of Food and Drug Safety), 정책브리핑 (korea.kr, official Korean government policy portal), 2024-09-23, 대량 조리음식 식중독 예방요령. The five-step holding and cooling instruction. Page HTML retrieved and the Korean text read directly 2026-09-02
  - "https://www.korea.kr/news/policyNewsView.do?newsId=148934964"  # 식품의약품안전처, 정책브리핑, 2024-10-11, 가을철 식중독 주의 -- 끓인 음식도 실온에 오래두면 위험. Source for the 43~47C growth optimum, the spore statement, the five-year outbreak counts and the 259-case incident. Page HTML retrieved and read directly 2026-09-02
  - "source:cooking/reheating-not-a-reset-007 -- the mechanism item this one gives a Korean-authority statement to, and a DIFFERENT organism (see notes)"
  - "source:cooking/kr-core-temperatures-005 -- the household core-temperature table whose numbers this page diverges from by scope"
  - "source:cooking/kr-cold-chain-band-006 -- the storage side, once a dish leaves the session"
refraction_notes:
  - note: >
      THE 60C FLOOR IS THE ONLY THING THAT MAKES HOLDING FREE. The ministry's
      instruction is 따뜻한 음식은 60C 이상, 차가운 음식은 5C 이하로 보관. Above
      that floor, a finished dish waiting on the stove is being held. Below it,
      the same dish is not absorbing schedule slack, it is incubating, and the
      2시간 clock the same page states is already running. Any craft rule about a
      dish tolerating delay is conditional on this line, and where the two
      conflict this line wins.
    grade: A
  - note: >
      THIS PAGE'S COOKING NUMBERS ARE HIGHER THAN THE HOUSEHOLD TABLE, AND THE
      DIFFERENCE IS SCOPE, NOT A CORRECTION. Item 005 carries the consumer table
      (닭고기 74C, 돼지고기 70~77C, 쇠고기 63~77C, 생선요리 63C, 재가열 74C). This
      page, scoped to 대량 조리, says 육류 등은 중심온도 75C, 어패류는 85C, 1분 이상,
      and 재가열 75C 이상. Do not overwrite 005 with these and do not average the
      two. When a session is deliberately cooking in bulk in order to hold or to
      store, this is the page whose scope actually matches, and it is the more
      conservative of the two.
    grade: B
  - note: >
      43~47C IS THE MOST OPERATIONALLY USEFUL NUMBER HERE. The ministry states
      퍼프린젠스 grows well without oxygen at 43~47C. That sits inside the
      5~60C danger zone and it is precisely the band a large covered pot passes
      through slowly on its way down, which is why the instruction is 소분 plus
      급냉 (여러 용기로 나누어 담기, 차가운 물이나 얼음을 채운 싱크대에 올려놓고 젓기)
      rather than simply letting it cool. NO COOLING-RATE MEASUREMENT IS GIVEN on
      this page, so no time-to-cool figure may be quoted from it in either
      direction.
    grade: B
  - note: >
      THIS PARTLY CLOSES ITEM 007'S KOREAN GAP AND ONLY PARTLY. Item 007 reached
      the reheated-stew habit by mechanism from a study of cooked rice, and
      GAPS.md records the missing Korean-dish evidence as the lane's highest-value
      hole. Here the Korean regulator says in its own words that 충분히 끓여 조리한
      음식이라도 실온에 오래 보관하면 this poisoning can occur, and that the organism
      다른 식중독균과 달리 끓인 음식에서도 다시 증식할 수 있다. That is an authority
      statement about the right food class in the right jurisdiction. It is still
      NOT a measurement in 국 or 찌개, and the outbreak counts behind it are
      surveillance of restaurants and mass catering, not of households.
    grade: C
  - note: >
      THE ORGANISM IS NOT THE ONE IN ITEM 007. This page is about Clostridium
      perfringens. Item 007 is about Bacillus cereus and its heat-stable emetic
      toxin. The two share the shape that matters for a session -- spores survive
      the boil, and growth happens during the descent rather than during the
      cooking -- and they are different hazards with different biology. State the
      shape; do not merge the organisms.
    grade: A
  - note: >
      THE SURVEILLANCE FIGURES ARE COUNTS, NOT RATES. 62 outbreaks over the five
      years from 2019, with autumn (9월~11월) the highest season at 21, and
      음식점 the most common location at 33. There is no denominator on this page,
      so nothing about per-meal risk follows. Speak the seasonality and the
      setting; do not convert either into a probability.
    grade: C
claim: >
  Korea's Ministry of Food and Drug Safety publishes a holding rule for cooked
  food that governs what a live cooking session may do with a finished dish:
  따뜻한 음식은 60C 이상, 차가운 음식은 5C 이하로 보관; 조리한 음식은 가급적 2시간
  이내 섭취; 보관된 음식을 다시 섭취할 경우 75C 이상으로 재가열. For food cooked in
  bulk the same guidance gives 육류 등은 중심온도 75C, 어패류는 85C, 1분 이상, then
  가열 조리 후 신속히 냉각 with 여러 용기로 나누어 담기 and a cold-water or iced sink
  to speed the cooling, and 조리된 상태로 상온에 방치되지 않도록 조리 후 즉시 제공.
  The organism named is Clostridium perfringens, which the ministry describes as
  an anaerobe that grows well at 43~47C and which forms a heat-resistant 아포 so
  that, unlike other foodborne pathogens, it can grow again in food that has been
  boiled. Reported Korean surveillance: 62 outbreaks in the five years from 2019,
  most in autumn (21 of 62), most often in restaurants (33 of 62), predominantly
  from cooked chicken and pork dishes.
reasoning: >
  Confidence here is about what the Korean regulator instructs, and the ministry
  publishing its own guidance through the government policy portal is definitive
  on that question, so the item sits at the top band with a jurisdictional
  qualifier. It earns its slot because it is the hard boundary of an entire
  product design. A live cooking-session module that back-calculates a timeline
  will inevitably want to park a finished dish and pick it up later, and the
  question of whether that is free has a published Korean answer with a number in
  it: it is free above 60C and it is a two-hour clock below. Without this item the
  craft rules in the rest of this batch would be free to say "a stew tolerates
  waiting", which is true about the pot and false about the food. Two limits are
  carried openly. The page's cooking temperatures are higher than the household
  table already shipped as item 005 and the difference is one of scope rather than
  a correction, so neither page is allowed to overwrite the other. And the
  outbreak figures are counts without a denominator, so the seasonality is
  reportable and no risk per meal is.
---

# cooking/session-holding-fence-014

A cooking session that plans backwards from a serving time will always, sooner
or later, want to finish something early and let it sit. Korea's food-safety
regulator has published the boundary on that, and it is a number rather than a
feeling.

Hot food is held at 60C or above. Cold food at 5C or below. Cooked food should
be eaten within about two hours. Food that has been stored and is being eaten
again is reheated to 75C or above.

Everything a live session does with a waiting dish sits on that first line. Above
60C, waiting is holding. Below it, waiting is not schedule slack at all -- the
dish is in the 5~60C zone and the two-hour clock has started.

The organism the ministry names for this is Clostridium perfringens, and its
biology explains why the descent matters more than the cooking. It is an
anaerobe. It grows well at 43 to 47 degrees. And when conditions turn against it,
it forms a heat-resistant spore, which is why the ministry says plainly that
unlike other foodborne pathogens it can grow again in food that has already been
boiled. A big covered pot cooling slowly on a stove spends a long time in exactly
the band where that organism is happiest.

That is why the ministry's cooling instruction is not "let it cool". It is:
divide it into several containers, and stand them in a sink of cold water or ice
and stir. Splitting a large volume is the intervention; it is what changes how
long the food spends in the band.

For food cooked in bulk the same guidance sets the cooking targets higher than
the household table does -- 75C at the centre for meat, 85C for fish and
shellfish, held a minute or more, then served immediately. Those are not a
correction to the household numbers. They are a different scope, aimed at the
large batch, and where a session is deliberately cooking a big pot to hold or to
store, they are the numbers whose scope fits.

The Korean surveillance behind the advisory: 62 outbreaks across the five years
from 2019, most of them in autumn, most often in restaurants, mostly from cooked
chicken and pork. Those are counts with no denominator attached, so they place
the season and the setting and they do not give a risk per meal.

One honest note about what this does and does not settle. This warehouse already
carries the finding that reheating does not reset a food's safety state, but it
reached the Korean stew habit by mechanism, from a study of cooked rice. This
page is the Korean authority saying, about boiled food, in Korea, that leaving it
out is where the problem happens. That is a real step up from an inference. It is
still not a measurement taken in a pot of 국, and the outbreaks counted here
happened in restaurants and canteens rather than in kitchens.
