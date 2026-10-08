---
# Authored 2026-10-06 (cooking craft/holding re-audit sprint). @food-safety, universal.
# Fills the hole item 014 left open on purpose ("NO COOLING-RATE MEASUREMENT IS
# GIVEN on this page"). Korea sets no cooling rate (checked against the
# 2026-10-01 Food Code text, item 070), so this item carries two FOREIGN legal
# cooling standards as labelled references and ONE controlled foodservice
# measurement of what container depth and cooling method actually achieve.
# Locale is universal because the physics and the measurement are; every
# number below says which jurisdiction or study it came from.
id: cooking/batch-cooling-depth-071
domain: cooking
lane: "@food-safety"
grade: C (one controlled foodservice cooling study; the two-stage standard is foreign law, not Korean)
locale: universal
as_of: 2013
contested: no
sources:
  - "https://www.foodprotection.org/files/food-protection-trends/JanFeb-13-Sneed.pdf"  # Roberts KR, Olds DA, Shanklin C, Sauer K, Sneed J. Cooling of Foods in Retail Foodservice Operations. Food Protection Trends 2013;33(1):27-31. Peer-reviewed, Kansas State University child-nutrition food-safety centre, federally funded. Full PDF read 2026-10-06. Chili con carne and meatless tomato sauce, 5.1 cm and 7.6 cm depths in steel pans, walk-in refrigerator / walk-in freezer / ice bath in walk-in, plus 11.4 L in a stockpot with a frozen chill stick
  - "https://www.foodstandards.gov.au/business/food-safety/cooling-and-reheating-food"  # Food Standards Australia New Zealand, Cooling and reheating food, citing Standard 3.2.2 clause 7: 60C to 21C in two hours or less, then 21C to 5C in four hours or less. Read 2026-10-06. FOREIGN jurisdiction
  - "https://www.foodstandards.gov.au/business/food-safety/2-hour-4-hour-rule"  # FSANZ, 2-hour/4-hour rule: cumulative time between 5C and 60C; under 2 h use or refrigerate, 2-4 h use but do not refrigerate, over 4 h discard. Described by FSANZ as guidance. Read 2026-10-06. FOREIGN jurisdiction
  - "https://www.revisor.mn.gov/rules/4626.0385/"  # Minnesota Rules 4626.0385, adopting US FDA Food Code 3-501.14: cooked TCS food from 57C to 21C within 2 hours and to 5C within a total of 6 hours. Read 2026-10-06 as the legal text of the US model rule; the FDA's own Food Code PDF refused retrieval (bot block) in this pass. FOREIGN jurisdiction
  - "source:cooking/session-holding-fence-014 -- the Korean ministry instruction this item quantifies: 여러 용기로 나누어 담기, cold-water or iced sink and stir; the 43~47C C. perfringens band"
  - "source:cooking/kr-food-code-cooked-food-holding-070 -- the check that Korean law sets no cooling rate"
  - "source:cooking/reheating-not-a-reset-007 -- why a slow cool is not repaired by reheating"
cooling_rules:
  - rule: split-before-chilling
    action: divide a batch into containers no deeper than about 5 cm of food before it goes in the fridge or freezer
    basis: Roberts 2013 (only 5.1 cm depth met both stages, and only in a freezer); KR ministry 여러 용기로 나누어 담기 (item 014)
    basis_grade: C
  - rule: never-chill-the-stockpot
    action: do not put a full pot in the fridge and count it as cooling
    basis: Roberts 2013 (11.4 L stockpot with a passive chill stick: roughly 16 to 23 h to reach 5C; the paper's text and table disagree)
    basis_grade: C
  - rule: active-cooling-first
    action: ice or cold-water bath with stirring for the first stage, then shallow containers into the coldest compartment
    basis: Roberts 2013 (ice bath gave the fastest first stage, about 1 h to 21C at 5.1 cm, but alone did not finish the second stage); KR ministry iced-sink-and-stir instruction
    basis_grade: C
  - rule: foreign-two-stage-benchmark
    first_stage: 60C (AU) or 57C (US) to 21C within 2 h
    second_stage: to 5C within a further 4 h (AU) or 6 h total (US)
    locale: AU-NZ and US only; NOT a Korean standard
    basis_grade: A for what those codes say; no Korean equivalent exists
  - rule: reheat-does-not-repair
    action: a batch that cooled slowly is not made safe by reheating to 75C
    basis: item 007, item 014
    basis_grade: A
refraction_notes:
  - note: >
      DEPTH, NOT THE FRIDGE, DECIDES. In the one controlled study read, the only
      method that met both stages of the US cooling standard for both foods was
      5.1 cm of product in a walk-in FREEZER (chili about 1 h 47 min to 21C and
      3 h 10 min to 5C). The same 5.1 cm in a walk-in refrigerator took about
      3 h to 21C and over 9 h to 5C. At 7.6 cm in the refrigerator, over 14 h to
      5C. "I put it in the fridge" is not a cooling method for a deep container.
    grade: C
  - note: >
      THE STOCKPOT IS THE WORST CASE AND THE COMMONEST HABIT. 11.4 L (3 gallons)
      in a stockpot with a frozen chill stick left in place was the slowest
      method in the study. The chill stick sped the first hour, then, once its ice
      had melted, the added water slowed the rest; the table reports over 20 h to
      reach 5C. The paper's text and table disagree on the exact total (the text
      says 16.5 h for chili, the table 22 h 38 min), so quote "most of a day",
      not a number of hours.
    grade: C
  - note: >
      THESE ARE COMMERCIAL WALK-IN UNITS, NOT A HOME FRIDGE. A walk-in
      refrigerator or freezer has more cold air and more capacity than a
      household appliance, and in the study no more than four pans were loaded
      at once. A home fridge holding a hot pot, with the door being opened, is
      unlikely to do better. Use the direction (shallower, colder, actively
      stirred is faster), not the minutes, for a household.
    grade: C
  - note: >
      THE TWO-STAGE TIMES ARE FOREIGN LAW. SAY SO. Australia and New Zealand
      (60C to 21C in 2 h, then to 5C in 4 h) and the US model code (57C to 21C
      in 2 h, to 5C within 6 h total) both legislate this. Korea does not; its
      2026 Food Code says only 청결한 장소에서 식히거나 보관 (item 070). Quote the
      foreign numbers as "what other food codes require", never as a Korean rule.
    grade: A
  - note: >
      WHY THE FIRST STAGE IS THE STRICT ONE. Both foreign codes give the hot half
      of the descent the shorter window, and the Korean ministry names 43~47C as
      where C. perfringens grows best (item 014). That band sits inside the first
      stage. The mechanism is consistent with the codes; the warehouse did not
      read the codes' own derivation, so the link is stated as consistency, not
      as their stated rationale.
    grade: B
  - note: >
      THE AU 2-HOUR/4-HOUR RULE IS CUMULATIVE AND IS NOT A COOLING RULE. FSANZ
      counts every period between 5C and 60C, during prep, transport and display,
      and keeps it separate from cooling. It is guidance, not a Korean rule, and
      its 4-hour discard line has no Korean counterpart; do not import it as one.
    grade: B
claim: >
  How fast a batch of cooked food passes down through the danger zone is decided
  mostly by the depth of food in the container and how cold and how actively it
  is cooled, not by whether it is "in the fridge". In a controlled foodservice
  study (Roberts et al. 2013), chili and tomato sauce cooled at 5.1 cm depth in a
  walk-in freezer were the only treatments to meet the US model cooling standard
  (57C to 21C within 2 h, to 5C within 6 h); the same depth in a walk-in
  refrigerator took roughly 3 h to 21C and 9 h or more to 5C, 7.6 cm took over
  14 h to 5C, and an 11.4 L stockpot with a passive chill stick took most of a
  day. An ice bath gave the fastest first stage but alone did not finish the
  second. Australia/New Zealand (60C to 21C in 2 h, then to 5C in 4 h) and the
  US model code legislate two-stage cooling; Korea legislates no cooling rate,
  and its ministry's household instruction is to divide into several containers
  and cool in a cold-water or iced sink with stirring.
reasoning: >
  This sits in the observational band because the quantitative core is one
  controlled study in commercial walk-in equipment with two foods; it is a
  measurement, not a trial with an outcome in people, and it has not been
  replicated here. The foreign cooling standards are certain as statements of
  what those codes say and carry no weight as Korean rules, which is why the
  locale is universal and every number is labelled with its jurisdiction. The
  item earns its place because it turns item 014's qualitative instruction
  (나누어 담기, 급냉) into something a cooking-session flow can act on: split to
  shallow containers before chilling, cool actively first, and never treat a
  full pot in the fridge as cooled. The household fridge was not measured, and
  the study's own authors question whether the US standard is the right one; the
  direction of the result is what transfers, not its minutes.
---

# cooking/batch-cooling-depth-071

Cooking a big pot is the easy part of batch cooking. Cooling it is where the
risk is, and the thing that decides how long it takes is mostly the depth of
food in the container.

The best measurement located is a 2013 study from Kansas State University. It
cooled chili and a tomato sauce in steel pans at two depths, 5 cm and 7.5 cm,
in a walk-in fridge, a walk-in freezer and an ice bath, and cooled a three-gallon
stockpot with a frozen "chill stick" in it. The yardstick was the US cooling
rule: down to 21 degrees within two hours, and to 5 within six.

Only one method passed both stages for both foods: 5 cm of food in the freezer.
The same 5 cm in the fridge took about three hours to reach 21 and over nine to
reach 5. At 7.5 cm, over fourteen hours. The stockpot was the slowest of all --
most of a day -- because once the chill stick's ice had melted it was just
adding water to the pot. An ice bath was the fastest way through the hot first
stage, but on its own it did not finish the job.

So the useful rules for a home kitchen are about shape, not appliance:

- split the batch into shallow containers, about 5 cm of food or less
- cool actively first -- a sink of cold water or ice, and stir
- then the coldest part of the fridge, or the freezer, uncrowded
- never put a full pot in the fridge and count it as cooled

That is the same instruction Korea's food-safety ministry gives (divide into
several containers, cold or iced sink, stir); this study shows how much it
matters.

Two honest limits. Those were commercial walk-in units, colder and bigger than a
home fridge, so the minutes do not transfer -- the direction does. And the
two-stage times are other countries' law. Australia and New Zealand require 60
to 21 in two hours and then to 5 in four more; the US model code is similar.
Korea sets no cooling rate at all, which was checked against its 2026 Food Code.
A cooling time spoken to a Korean user is "what other food codes require", not a
Korean rule. And a batch that cooled too slowly is not repaired by boiling it
again.
