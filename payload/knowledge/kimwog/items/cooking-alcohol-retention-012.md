---
# Authored 2026-09-02 (cooking-lane collection sprint). @test-kitchen, universal.
# A named folklore correction with a hard reference table behind it. The USDA
# retention values were extracted from the primary PDF itself (retention codes
# 5001-5010, ethyl alcohol column), not copied from a secondary write-up.
id: cooking/alcohol-retention-012
domain: cooking
lane: "@test-kitchen"
grade: B
locale: universal
as_of: 2007
contested: no
sources:
  - "https://www.ars.usda.gov/ARSUserFiles/80400530/pdf/retn06.pdf"  # USDA Table of Nutrient Retention Factors, Release 6. US Department of Agriculture, Agricultural Research Service, Nutrient Data Laboratory, 2007. Retention codes 5001-5010 (ALC BEV rows), 'Alcohol, ethyl' column. Values below were read out of this document directly
refraction_notes:
  - note: >
      THIS IS A COMPILATION TABLE, NOT A MEASUREMENT SERIES. USDA publishes
      retention factors as a reference for nutrient calculation. The document does
      not carry per-row experimental provenance, and the values are rounded to the
      nearest 5 percent. The underlying published measurements were NOT located in
      this pass. Use these as orders of magnitude for a class of preparation, never
      as a prediction of the alcohol content of one specific dish.
    grade: C
  - note: >
      THE VALUES ARE RETENTION OF WHAT WAS ADDED, NOT A CONCENTRATION. A 25
      percent retention after an hour of simmering means a quarter of the alcohol
      that went in is still there. It says nothing about how strong the finished
      dish is, which depends on how much went in and how much liquid was lost. Do
      not convert these figures into a drink-equivalent without doing that
      arithmetic explicitly.
    grade: A
  - note: >
      THE COUNTERINTUITIVE ROW IS THE FLAMED ONE. Setting a dish alight retains
      about 75 percent -- more than a fifteen-minute simmer, which retains about
      40. The visible drama of the flame is the opposite of a reliable signal, and
      that inversion is the single most useful thing in the table.
    grade: B
  - note: >
      NO KOREAN-DISH DATA. Cooking wine, 청주 and soju appear constantly in
      Korean cooking, and nothing in this table was measured on a Korean
      preparation. Mapping a 찌개 or a 조림 onto the "stirred, baked or simmered"
      rows is a judgement about cooking method, not a measured result, and should
      be spoken as such.
    grade: D
claim: >
  Alcohol added to food does not cook off at any ordinary cooking duration. USDA
  retention factors for ethyl alcohol, by preparation: stirred into a hot liquid,
  85 percent retained; flamed, 75 percent; added with no heat and stored
  overnight, 70 percent; baked 25 minutes without being stirred in, 45 percent;
  stirred in and baked or simmered for 15 minutes, 40 percent; 30 minutes, 35
  percent; 1 hour, 25 percent; 1.5 hours, 20 percent; 2 hours, 10 percent; 2.5
  hours, 5 percent. Substantial alcohol therefore survives every short
  preparation, flambeing removes less than a brief simmer does, and even two and a
  half hours of simmering leaves a residue rather than nothing.
reasoning: >
  The claim being corrected -- that alcohol burns off in cooking -- is stated as
  fact in kitchens constantly and is the kind of claim a live cooking consumer
  will be asked to confirm, sometimes by someone with a real reason to avoid
  alcohol. The correction rests on a US federal reference table read out of the
  primary document rather than from a write-up, so the figures themselves are not
  in doubt. What holds the item below the top band is the nature of the source:
  retention factors are a compiled reference intended for nutrient bookkeeping,
  the values are rounded to five percent, and the document does not expose the
  experiments underneath them, which were not located in this pass. That is enough
  for orders of magnitude and not enough for a specific dish. The single most
  useful line is also the least intuitive one: flaming retains more than simmering
  briefly does, so the most visually convincing way of burning off alcohol is
  among the least effective. The item states retention of what was added, and
  deliberately refuses to convert that into a strength or a drink equivalent,
  because doing so requires inputs the table does not contain.
---

# cooking/alcohol-retention-012

"The alcohol cooks off" is one of the most repeated statements in a kitchen and
it is not true at any duration a normal recipe uses. The USDA publishes retention
factors for ethyl alcohol by preparation method:

- stirred into a hot liquid: 85 percent retained
- flamed: 75 percent
- added with no heat, stored overnight: 70 percent
- baked 25 minutes, not stirred in: 45 percent
- stirred in, baked or simmered 15 minutes: 40 percent
- 30 minutes: 35 percent
- 1 hour: 25 percent
- 1.5 hours: 20 percent
- 2 hours: 10 percent
- 2.5 hours: 5 percent

Read the top of that list carefully. Splashing wine into a hot pan leaves most of
it. Setting a dish alight -- the gesture that most looks like burning off alcohol
-- retains about three quarters, which is worse than simply letting it simmer for
fifteen minutes. The visible drama is anti-correlated with the effect.

Getting genuinely low takes hours, and even two and a half hours of simmering
leaves a residue rather than zero.

Three limits on how to use these numbers. They are retention of what was added,
not a concentration: a quarter remaining after an hour tells you nothing about how
strong the finished dish is until you also account for how much went in and how
much liquid boiled away. They come from a compiled reference table rounded to the
nearest five percent, with no per-row experimental provenance in the document, so
they are good for the shape of the answer and not for a specific pot. And nothing
in the table was measured on a Korean dish; placing a 찌개 or a 조림 into the
"stirred in and simmered" rows is a judgement about method, not a measurement.

The practical use is narrow and real. If someone at the table is avoiding alcohol
-- pregnancy, medication, recovery, religious observance -- a dish made with
cooking wine or soju is not alcohol-free, and no amount of flaming makes it so.
