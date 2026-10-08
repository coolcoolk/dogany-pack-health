---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). Answers a question
# a meal-log consumer meets every day and normally answers by assumption: is the
# calorie number in the database the calorie number the body gets. For one food
# class it demonstrably is not, and the size of the gap depends on how the food
# was processed. Scope is deliberately held to what was actually measured.
id: nutrition/metabolizable-energy-atwater-015
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2012-2016
contested: no
sources:
  - "https://doi.org/10.3945/ajcn.112.035782"  # Novotny JA, Gebauer SK, Baer DJ. Am J Clin Nutr 2012;96(2):296-301. PMID 22760558, PMC3396444 -- n=18 crossover, 0/42/84 g almonds per day, full urine and faecal collection, bomb calorimetry
  - "https://doi.org/10.3945/jn.115.217372"  # Baer DJ, Gebauer SK, Novotny JA. J Nutr 2016;146(1):9-13. PMID 26581681 -- n=18 controlled feeding crossover, 42 g walnuts per day
  - "https://doi.org/10.1039/C6FO01076H"  # Gebauer SK, Novotny JA, Bornhorst GM, Baer DJ. Food Funct 2016;7(10):4231-4238. PMID 27713968 -- n=18, five-period crossover: whole natural vs roasted vs chopped vs almond butter
  - "source:nutrition/self-report-underreporting-007 -- the OTHER error in a logged calorie figure; these two are independent and stack"
refraction_notes:
  - note: >
      SCOPE IS TREE NUTS, AND THE BOUNDARY IS THE POINT. This was measured for
      almonds and walnuts by whole-diet feeding with complete excreta collection.
      It is NOT a general licence to discount database calories for other foods,
      and there is no measured figure here for any food outside that class.
      Generalising it into "database calories are wrong" would convert a precise
      finding into a vague excuse.
    grade: B
  - note: >
      FOOD STRUCTURE, NOT FOOD IDENTITY, drives the gap, which is what makes it
      more than a trivia item. In the same laboratory the discount shrank as the
      almond was broken down: whole natural 4.42, whole roasted 4.86, chopped
      5.04 and almond butter 6.53 kcal per gram, with almond butter matching its
      predicted value. The same food logged as butter and as whole nuts is
      genuinely different energy. Anything relying on a food name alone cannot see
      this.
    grade: B
  - note: >
      THIS ERROR IS INDEPENDENT OF SELF-REPORT ERROR AND POINTS THE OTHER WAY. A
      user under-reports what they ate, which understates intake, while the
      database over-states the energy of certain whole foods, which overstates it.
      They do not cancel in any known ratio and must never be netted off against
      each other as if they did.
    grade: C
claim: >
  The general Atwater factors used to assign calorie values overestimate the
  energy the body actually obtains from whole tree nuts. In controlled feeding
  with complete urine and faecal collection, almonds delivered 4.6 kcal per gram
  against a predicted 6.0-6.1, a 32 percent overestimate, equivalent to about 129
  rather than 168-170 kcal per 28 g serving. Walnuts delivered 146 rather than
  185 kcal per 28 g serving, about 21 percent less. The size of the discrepancy
  depends on food structure: grinding almonds into butter removed it almost
  entirely.
reasoning: >
  These are direct measurements of metabolisable energy by whole-diet feeding with
  complete excreta collection and bomb calorimetry, which is the reference method
  for this question rather than an inference from composition. Three independent
  studies from the same programme agree, the mechanism (intact cell walls limiting
  lipid release, abolished by grinding) is measured rather than assumed, and no
  contrary result was located, so it sits at the RCT-level pre-consensus band and
  is not flagged contested. The reason it is not at the top band is population and
  scope, not quality: each study is a controlled crossover with 18 participants,
  and the finding is established for two nuts, not for food in general. For a
  consumer reading a meal log the value is a bounded correction plus a general
  caution: a logged calorie total is a model output, not a measurement, and the
  model is known to be wrong in a specific measured direction for a specific food
  class. It is emphatically not a warrant to hand-adjust arbitrary foods.
---

# nutrition/metabolizable-energy-atwater-015

Calorie figures in any food database are calculated, not measured. They come from
general conversion factors applied to protein, fat and carbohydrate content, and
for most foods that works. For whole tree nuts it demonstrably does not. When
researchers fed almonds as part of a controlled diet and collected everything the
participants excreted, the energy actually obtained was about a third less than
the calculated value, roughly a hundred and thirty rather than a hundred and
seventy calories per serving. Walnuts came in about a fifth low.

The interesting part is why, because it stops the finding from being a piece of
trivia. The gap closes as the nut is broken down. Whole almonds gave the least
energy, roasted a little more, chopped more again, and almond butter matched its
predicted value exactly. Intact plant cell structure is physically withholding
fat from digestion, and grinding removes the effect. That means the same food,
under the same name, is genuinely different energy depending on its form, which
is something no name-matching food log can see.

Two guardrails belong with this. It has been measured for almonds and walnuts and
nothing else, so it is not a general permission to distrust database calories.
And it runs opposite to the self-report bias: users under-record what they eat
while the database over-values certain whole foods. The two errors are unrelated
and there is no known ratio in which they cancel, so treating one as an offset
against the other is a mistake dressed as sophistication.
