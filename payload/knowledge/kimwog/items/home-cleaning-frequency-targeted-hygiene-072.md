---
# Home routines sprint 2026-10-06 (dispatch task kw-home-routines). The
# question a routine module asks first -- how often should each cleaning task
# recur -- has almost no health evidence behind any answer. This row records
# that absence honestly, carries the three things that ARE measured nearby,
# and hands the module the one defensible scheduling principle (clean at the
# risk moments, not on a calendar). It refuses the familiar weekly-sheets /
# daily-wipe cadence tables as health rules. Product efficacy (antibacterial,
# DIY disinfectant) is items 010 and 012 and is not repeated here; food-contact
# hygiene is the cooking domain's.
id: home/cleaning-frequency-targeted-hygiene-072
domain: home
lane: "@household-labor"
grade: B (antibacterial versus plain cleaning products made no difference to household infection symptoms in a blinded trial); C (mite-reduction measures did not improve asthma, flagged review); D (targeted hygiene as the scheduling principle; any specific cleaning cadence)
locale: universal
as_of: 2004-2016
contested: no
sources:
  - "https://doi.org/10.7326/0003-4819-140-5-200403020-00007"  # Larson EL, Lin SX, Gomez-Pichardo C, Della-Latta P. Effect of antibacterial home cleaning and handwashing products on infectious disease symptoms: a randomized, double-blind trial. Ann Intern Med 2004;140(5):321-329. PMID 14996673. 238 households (1178 persons), 48 weeks, Northern Manhattan. Abstract read via Europe PMC 2026-10-06
  - "https://doi.org/10.1002/14651858.CD001187.pub2"  # Gøtzsche PC, Johansen HK. House dust mite control measures for asthma. Cochrane Database Syst Rev 2008 (searches to Nov 2007). PMID 18425868. 54 trials, 3002 patients. Abstract read via Europe PMC 2026-10-06, which carries Cochrane's editorial note: the review "predates current reporting standards and methodological expectations for Cochrane Reviews. It should not be used for clinical decision-making."
  - "https://doi.org/10.1177/1757913916650225"  # Bloomfield SF, Rook GA, Scott EA, Shanahan F, Stanwell-Smith R, Turner P. Time to abandon the hygiene hypothesis ... the role of targeted hygiene. Perspectives in Public Health 2016;136(4):213-224. PMID 27354505, PMC4966430. Delphi-style judgement of six experts. Full text read at Europe PMC 2026-10-06. COI: the authors received an honorarium from the International Scientific Forum on Home Hygiene (IFH) for preparing the manuscript; IFH's own site carries no funding disclosure on its targeted-hygiene page estate-scrub:allow(cited author surname)
  - "https://www.ukcpi.org/the-nine-moments-for-hygiene-when-cleanliness-really-matters/"  # The nine IFH hygiene moments, listed verbatim on a page of the UK Cleaning Products Industry Association (trade body), 2019-12-03. Read 2026-10-06. Used ONLY for the enumerated list, which IFH's own site did not show in readable form; the publisher sells the products the list is about, which is one more reason the list is carried as a consensus checklist and not as evidence
  - "home/antibacterial-wash-not-grase-010"  # within-warehouse: regulator adjudication of antibacterial washes
  - "home/diy-disinfectant-efficacy-012"  # within-warehouse: vinegar / baking soda are not disinfectants
  - "home/dampness-mould-respiratory-001"  # within-warehouse: the one home exposure with strong harm evidence -- damp is a moisture problem, not a cleaning-cadence one
  - "home/cleaning-agents-lung-function-009"  # within-warehouse: more cleaning-product exposure is not free
  - "framework:GRADE -- one double-blind household RCT (product type, not frequency); one large pooled review of RCTs that Cochrane itself now flags as outdated; one expert-consensus paper with an industry-adjacent honorarium. A targeted search for any trial or cohort that compares cleaning FREQUENCIES (sheets, bathrooms, floors, kitchens) against a health outcome returned only consumer recommendations and habit surveys. The cadence question is unstudied, not answered."
refraction_notes:
  - note: >
      NO CLEANING CADENCE HAS A HEALTH BASIS. No trial or cohort was located
      that compares how often a household cleans (weekly versus fortnightly
      sheets, daily versus weekly bathroom, and so on) against an infection,
      allergy or other health outcome. The cadence tables in circulation are
      recommendations and habit surveys. A routine module may schedule by
      the household's own standard, but must not present any interval as
      what health requires.
    grade: D
  - note: >
      PRODUCT STRENGTH DID NOT MATTER IN THE ONE BLINDED TRIAL. Households
      randomised to antibacterial versus plain products for general
      cleaning, laundry and handwashing over 48 weeks showed no difference
      in any infectious symptom (overall incidence density ratio 0.96, 95%
      CI 0.82 to 1.12). The symptoms were mostly respiratory and viral; the
      authors leave room for bacterial illness. Ordinary products are enough
      for a routine; stronger ones buy nothing measured (and see 009, 010).
    grade: B
  - note: >
      MORE ALLERGEN-REDUCTION WORK DID NOT HELP MITE-SENSITIVE ASTHMA in the
      pooled trials: 54 trials, mostly mattress encasings and acaricides,
      morning peak flow difference 0.00 (95% CI -0.10 to 0.10), and no
      difference in symptoms or medication. Cochrane now flags this review as
      outdated and not for clinical decisions, so it cannot carry a clinical
      rule. It does mean the common "clean more often for your allergies"
      advice has no trial support behind it here. Allergy management belongs
      to the user's clinician.
    grade: C
  - note: >
      SCHEDULE BY RISK MOMENT, NOT BY CALENDAR. The targeted-hygiene
      position is that hygiene means acting at the times and places where
      harmful microbes spread -- food handling, eating with fingers, toilet
      use and nappy changing, coughing and sneezing, frequently touched surfaces, dirty
      laundry, pets, refuse, caring for an ill household member -- and that
      hygiene is not the same as general cleanliness. That is an expert
      consensus with an industry-adjacent honorarium, not a trial result.
      For a routine module it means: event-triggered tasks (someone is ill,
      raw meat was handled) carry the hygiene weight; calendar tasks carry
      the household's comfort standard.
    grade: D
  - note: >
      CLEANLINESS AND HEALTH ARE DIFFERENT GOALS, AND BOTH ARE LEGITIMATE.
      The same paper finds no confirmed evidence that home cleanliness
      raises allergy risk, so the reverse folklore ("a too-clean home causes
      allergies") is not supported either. A household that wants a tidier
      home is choosing a comfort standard, which is its own business; the
      module should label it as that and not dress it as hygiene.
    grade: D
  - note: >
      DAMP IS THE EXCEPTION THAT HAS EVIDENCE. The strongest harm evidence in
      this domain is dampness and mould (001), and its lever is moisture and
      ventilation (004), not wiping frequency. A routine that keeps surfaces
      spotless in a damp flat is optimising the wrong variable.
    grade: B
claim: >
  How often a household cleans has, as far as could be found, never been
  tested against a health outcome: no trial or cohort compares cleaning
  cadences, and the familiar weekly-sheets, daily-wipe tables are
  recommendations and habit surveys. What is measured nearby points the same
  way. In a blinded 48-week trial in 238 households, antibacterial versus
  plain cleaning, laundry and handwashing products made no difference to
  infection symptoms. Pooled trials of mite-allergen reduction found no
  benefit for mite-sensitive asthma, though Cochrane now flags that review as
  outdated. The defensible scheduling principle is targeted hygiene, an
  expert-consensus position: put hygiene effort at the moments microbes
  spread (food handling, eating with fingers, toilet use, illness in the home, frequently touched
  surfaces, dirty laundry, pets, refuse) and treat calendar cleaning as the
  household's own comfort standard rather than a health requirement. For a
  routine module: event-triggered hygiene tasks, household-set cadences for
  everything else, and no interval presented as medically required.
reasoning: >
  The grade is split because the parts differ sharply. Larson 2004 is a
  randomised, double-blind household trial with a year of follow-up and
  blinded commercial products, and it answers a product question cleanly;
  it is not a frequency trial and is not stretched into one. The mite review
  pools 54 RCTs and finds a precise null, but Cochrane's own editorial note
  withdraws it from clinical use, so it is carried at the observational band
  and only to refuse the allergy-cadence claim. Targeted hygiene comes from a
  six-expert Delphi exercise whose authors were paid an honorarium by the
  forum that promotes the approach; it is consistent with the trial evidence
  and with regulator positions elsewhere in this domain, but it is opinion,
  and it is graded as such. The absence of cadence evidence is a search
  result recorded in GAPS.md, not a finding that cadence never matters.
---

# home/cleaning-frequency-targeted-hygiene-072 -- 청소는 얼마나 자주? 달력보다 "위험한 순간"

**한 줄 그림:** 청소 주기를 건강과 비교한 연구는 찾지 못했다. 위생은 날짜가 아니라 위험한 순간에
맞추고, 나머지 청소 주기는 그 집이 정하는 깔끔함의 기준이다.

## What the engine reads from this row

| Question | Answer | Strength |
|---|---|---|
| a health-required interval for any cleaning task | none located | search absence |
| antibacterial vs plain products, infection symptoms | no difference (IDR 0.96, 0.82-1.12) | blinded household RCT |
| more mite-allergen control for mite-sensitive asthma | no benefit in pooled trials; review flagged outdated | pooled RCTs, flagged |
| scheduling principle | hygiene at risk moments; calendar tasks = comfort standard | expert consensus, COI noted |
| "too clean causes allergies" | not supported | expert review |
| damp / mould | moisture and ventilation, not wiping frequency | see 001, 004 |

Risk moments (event triggers, the IFH list of nine): food handling; eating
with fingers; toilet use and nappy changing;
coughing and sneezing; frequently touched surfaces; handling and laundering
dirty clothing and linen; caring for pets; handling refuse; caring for an ill
household member.

## 한국어 요약 (답변용)

- 침대 시트는 매주, 욕실은 매일 같은 청소 주기표가 건강에 필요하다는 연구는 찾지 못했다. 주기를
  건강 결과와 비교한 연구 자체가 없다. 그래서 주기는 "건강상 필요"라고 말하지 않고, 그 집이 원하는
  깔끔함의 기준으로 다룬다.
- 일반 세제와 항균 세제를 몰래 바꿔 1년 가까이 쓴 238가구 실험에서 감염 증상은 차이가 없었다.
  평범한 세제로 충분하다.
- 진드기 알레르기 천식에 매트리스 커버·살진드기제 같은 조치를 더해도 좋아지지 않았다는 종합 분석이
  있다. 다만 이 리뷰는 오래돼서 진료 판단에는 쓰지 말라는 표시가 붙어 있다. "알레르기 있으면 청소를
  더 자주"는 근거가 없다는 정도로만 말하고, 치료는 의료진에게 넘긴다.
- 위생은 위험한 순간에 맞춘다. 음식 손질, 손으로 먹을 때, 화장실·기저귀, 기침·재채기, 자주 만지는 곳, 더러운
  빨래, 반려동물, 쓰레기, 아픈 가족 돌보기. 이건 전문가 합의이고, 저자들이 관련 단체에서 사례비를
  받았다는 점도 밝힌다.
- "너무 깨끗하면 알레르기 생긴다"도 근거가 없다. 깔끔하게 살고 싶으면 그건 취향이고, 위생이라고
  포장하지 않으면 된다.
- 근거가 강한 건 습기와 곰팡이 쪽이다(001). 해결책은 자주 닦기가 아니라 습기와 환기다(004).
