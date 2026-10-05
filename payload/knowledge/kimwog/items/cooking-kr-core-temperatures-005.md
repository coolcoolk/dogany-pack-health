---
# Authored 2026-09-02 (cooking-lane collection sprint). KR-LOCALE item, @food-safety.
# The single most-read item for a live cooking-session consumer: the per-food
# core-temperature table the OWNER'S OWN REGULATOR publishes, retrieved directly
# from the Ministry of Food and Drug Safety consumer portal rather than from a
# US chart or a recipe site. Deliberately carries the jurisdiction discipline
# established when a US-only rest-time equivalence was dropped from this lane
# earlier the same day: a US regulatory fact is not a Korean regulatory fact.
id: cooking/kr-core-temperatures-005
domain: cooking
lane: "@food-safety"
grade: A (jurisdictional-guidance)
locale: KR
as_of: 2026-09-02
contested: no
sources:
  - "https://www.foodsafetykorea.go.kr/portal/board/boardDetail.do?menu_no=3120&bbs_no=bbs001&ntctxt_no=21793&menu_grp=MENU_NEW01"  # Ministry of Food and Drug Safety (식품의약품안전처), 식품안전나라 portal, consumer guidance page 식중독 예방을 위한 권장 온도. Retrieved directly 2026-09-02; all figures below are quoted from it verbatim
  - "source:cooking/poultry-safe-temp-002 -- the poultry row of this table, already shipped as its own item after an independent US/KR cross-check"
  - "source:cooking/kr-cold-chain-band-006 -- the STORAGE side; note the 5C in this item is a food-poisoning recommendation, not the 0-10C legal cold-chain band"
refraction_notes:
  - note: >
      THIS IS CONSUMER GUIDANCE FROM THE REGULATOR, NOT A BINDING COOKING
      STANDARD. The Ministry of Food and Drug Safety publishes this table on its
      public food-safety portal to tell households what to do. It is the right
      thing to speak to a home cook under Korean jurisdiction and it is issued by
      the body that actually regulates food here, but it is not a statutory
      cooking specification and it should not be described as one.
    grade: A
  - note: >
      THE BEEF ROW IS A RANGE, AND NOTHING IS ATTACHED TO ITS LOWER END. The page
      lists 쇠고기 63~77C. That lower bound must NOT be converted into the US
      construct of a lower temperature made equivalent by a holding time. The
      Korean page publishes no rest-time equivalence, no holding-time table and
      no log-reduction schedule of any kind, and the Korean-language safety
      material does not treat 레스팅 as a safety step. A claim built on the US
      time-temperature equivalence was researched and DROPPED from this lane
      earlier on 2026-09-02 for exactly this reason. Read the range as a doneness
      band, speak the upper part of it when the question is safety, and never
      import a foreign holding-time rule to justify the bottom of it.
    grade: A
  - note: >
      ONE FIGURE ON THIS PAGE IS AN INSTRUCTION TO USE A THERMOMETER, NOT AN
      INSTRUCTION TO LOOK. The page pairs the numbers with visual cues for
      shellfish and shrimp because those have no practical core-temperature
      reading. For everything with a number, the number is the test. Colour and
      juice appearance are not, and the poultry item already carries that point.
    grade: A
  - note: >
      THE REFRIGERATED-STORAGE DURATIONS ARE COARSE. Raw meat and seafood 1-2
      days, cooked meat and seafood 3-5 days, eggs 3-5 weeks. These are
      household rules of thumb with no stated temperature assumption attached on
      the page itself, and Korea's legal refrigeration band runs up to 10C. Speak
      them as the regulator's rounded advice, not as a shelf-life calculation.
    grade: C
claim: >
  Korea's Ministry of Food and Drug Safety publishes a per-food core-temperature
  (중심부온도) table for household cooking on its 식품안전나라 portal. The values
  are: 닭고기 74C for 1분 이상; 돼지고기 70~77C; 쇠고기 63~77C; 다진고기 71C;
  달걀요리 71C; 생선요리 63C. Shellfish (대합, 조개) are judged by the shell
  opening completely and shrimp/lobster by the shell peeling easily with the
  flesh gone opaque. Leftovers being reheated (남은 음식 재가열) are given 74C.
  The same page states the microbial danger zone as 5~60C and the safe-holding
  rule as 5C 이하 또는 60C 이상. Its refrigerated-storage durations are: raw meat
  and seafood 1-2일, cooked meat and seafood 3-5일, eggs 3-5주.
reasoning: >
  A live cooking-session consumer needs one authoritative temperature table, and
  the only defensible choice of table is the one issued by the food-safety
  authority of the jurisdiction the user actually cooks in. This is that table,
  retrieved directly from the regulator's own portal rather than from a
  secondary write-up, so confidence about WHAT THE GUIDANCE SAYS is at the top
  band with a jurisdictional qualifier, in the same way a government document
  describing its own contents is definitive about its own contents. Confidence
  about whether each individual number is the microbiologically optimal figure
  is a separate and weaker question that this item does not claim to answer. The
  item exists mostly to close a specific failure mode: without it, a consumer
  asked for a safe temperature will reach for a US chart, and this lane has
  already had one US-only rule dropped for exactly that reason. The beef range
  is the sharp edge and is fenced off explicitly rather than left for a later
  pass to trip over.
---

# cooking/kr-core-temperatures-005

When a Korean home cook asks how hot something has to get, the answer should
come from the Korean regulator, and it exists. The Ministry of Food and Drug
Safety publishes a core-temperature table on its public food-safety portal:

- 닭고기 (chicken): 74C, held 1분 이상
- 돼지고기 (pork): 70~77C
- 쇠고기 (beef): 63~77C
- 다진고기 (ground meat): 71C
- 달걀요리 (egg dishes): 71C
- 생선요리 (fish): 63C
- 대합, 조개 (clams, shellfish): until the shell opens completely
- 새우, 바다가재 (shrimp, lobster): until the shell peels easily and the flesh
  turns opaque
- 남은 음식 재가열 (reheating leftovers): 74C

The same page gives the danger zone as 5~60C and the holding rule as at or below
5C, or at or above 60C. Its household refrigerated-storage durations are one to
two days for raw meat and seafood, three to five days for cooked meat and
seafood, and three to five weeks for eggs.

Two things about this table need saying out loud.

First, the beef row is a range, and the bottom of that range carries nothing
with it. In the United States a lower temperature can be made equivalent to a
higher one by holding the meat for a specified time, and that equivalence is
written into the US regulatory system. Korea publishes no such thing -- no
holding-time table, no log-reduction schedule, and no treatment of resting as a
safety step rather than a juiciness technique. So the 63C at the bottom of the
Korean beef range is not a Korean version of the American rule and must never be
spoken as one. Read it as a doneness band; when the question is safety, speak
the upper end.

Second, the numbers are an instruction to measure. The page falls back on visual
cues only for shellfish and shrimp, which have no practical core reading.
Everywhere a number appears, the number is the test, and appearance is not.

The storage durations are the softest part of the page. They are rounded
household advice with no stated fridge temperature behind them, and Korea's
legal refrigeration band is wider and warmer than most people assume -- which is
its own item.
