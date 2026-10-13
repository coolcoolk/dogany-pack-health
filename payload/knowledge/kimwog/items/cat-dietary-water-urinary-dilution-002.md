---
# Collection sprint 2026-09-02, cat-domain opening. The domain's highest-value
# actionable claim: dietary water content, urine dilution, and lower urinary
# tract disease. This is the one place in feline medicine where a household
# decision (what the food's moisture content is) connects to a measured
# physiological outcome through more than one study. It is also the domain's
# worked example of the funding-affiliation carry rule -- BOTH controlled
# studies here come from a pet-food manufacturer's research centre.
# Rubric: cat @clinical-vet (VC-A, borrowed anchor -- read one band down; see
# cat/curator-checklist-001).
# Source re-audit 2026-10-06: Buckley 2011 abstract -- only the 73.3 pct diet
# separated (SG vs <=53.2 pct, CaOx RSS vs dry); voluntary drinking fell as food
# moisture rose, so total fluid intake was flat below 73.3. 'Consistent across the
# ladder' narrowed to that step. Markwell 1999: 8 of 54 lost to follow-up.
id: cat/dietary-water-urinary-dilution-002
domain: cat
grade: C (that higher dietary water content produces more dilute urine and lower calcium oxalate relative supersaturation); D (any magnitude, any recurrence percentage, and any claim about drinking-water intake as opposed to food moisture)
lane: "@clinical-vet"
locale: universal
as_of: 1999-2011
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/22005408/"  # Buckley CMF, Hawthorne A, Colyer A, Stevenson AE. 2011, Br J Nutr 106 Suppl 1:S128-S130, doi 10.1017/S0007114511001875 -- 6 cats, dry food vs the same food hydrated to 25.4, 53.2 and 73.3 pct moisture. Waltham Centre for Pet Nutrition (Mars) affiliation
  - "https://pubmed.ncbi.nlm.nih.gov/10023397/"  # Markwell PJ, Buffington CA, Chew DJ, Kendall MS, Harte JG, DiBartola SP. 1999, J Am Vet Med Assoc 214(3):361-365 -- 54 cats with idiopathic cystitis; canned 16/18 (89 pct) vs dry 17/28 (61 pct) free of recurrent signs within 12 months, p<0.05. NO DOI: this is a pre-DOI JAVMA record; PMID 10023397 is the resolvable identifier. Waltham affiliation on the first author
  - "https://pubmed.ncbi.nlm.nih.gov/21145768/"  # Segev G, Livne H, Ranen E, Lavy E. 2011, J Feline Med Surg 13(2):101-108, doi 10.1016/j.jfms.2010.10.006 -- 82 cats with urethral obstruction vs 82 sex- and time-matched controls; proportion consuming only dry food was higher in the obstruction group
  - "cat/curator-checklist-001"  # the domain rule this item obeys: small-n animal studies support direction, never magnitude; manufacturer affiliation is carried on the item
refraction_notes:
  - note: >
      WHAT WAS ACTUALLY MEASURED, and it is food moisture rather than drinking.
      Buckley 2011 fed SIX cats the same dry diet, plain and then hydrated to
      25.4, 53.2 and 73.3 percent moisture, and measured urine output, specific
      gravity and relative supersaturation for calcium oxalate and struvite.
      Only the 73.3 percent version separated: its urine specific gravity was
      significantly lower than on the 53.2-percent-or-lower diets, and its
      calcium oxalate supersaturation significantly lower than on the plain dry
      food; the struvite picture was not clear. Voluntary drinking FELL as food
      moisture rose, so total fluid intake stayed flat across the three lower
      levels and rose only at 73.3 percent. Six cats is six cats. The direction
      is physiologically unsurprising, which is why it is carried at all, but it
      is one step on six cats rather than a graded response, and no number from
      this study should ever be spoken as a magnitude.
    grade: C
  - note: >
      THE CLINICAL-OUTCOME STUDY IS OLDER, SMALLER AND ITS HEADLINE NUMBER IS NOT
      SHIPPABLE. Markwell 1999 followed 54 cats with idiopathic cystitis and
      reported that 16 of 18 on a canned formulation (89 percent) versus 17 of 28
      on the dry formulation (61 percent) were free of recurrent signs within
      twelve months, p below 0.05. Those denominators are 18 and 28 -- eight of
      the 54 were lost to follow-up, and the abstract says cats were assigned
      without saying the assignment was random. A difference
      of that size on samples that small, in an unblinded design with
      owner-reported recurrence, establishes at most that the direction is worth
      taking seriously. The 89-versus-61 pair must not be quoted as an effect
      size, and the study is also not a test of moisture alone: the two arms
      differed as products, not only in water content.
    grade: D
  - note: >
      A THIRD, INDEPENDENT AND NON-INDUSTRY LINE POINTS THE SAME WAY, which is
      why this item exists rather than being refused. Segev 2011 compared 82 cats
      presenting with urethral obstruction against 82 sex- and time-matched
      controls and found the proportion consuming ONLY dry food higher in the
      obstruction group, alongside lower mean age, higher mean body weight, and a
      lower proportion of indoor-outdoor cats. That is a case-control
      association with every confound a case-control design carries -- an
      exclusively-dry-fed cat is likely to differ in other ways too -- but it is
      not funded by a food manufacturer and it lands in the same direction as the
      two that are.
    grade: C
  - note: >
      CONTESTED, ON FUNDING, and stated rather than buried. Buckley 2011 comes
      from the Waltham Centre for Pet Nutrition and Markwell's affiliation is the
      same. Waltham is the research arm of a pet-food manufacturer, and the
      finding it supports is that a wet product is better for the cat's urinary
      tract than a dry one -- which is a finding about a product category that
      manufacturer sells. This is exactly the situation exercise/
      funding-coi-check-004 was written for. It does not make the physiology
      wrong; urine dilution follows water intake in any mammal. It does mean the
      two controlled studies and the commercial interest point the same way, and
      that an agent quoting them should say who ran them.
    grade: D
  - note: >
      NOT ESTABLISHED BY ANY SOURCE HERE: that giving a cat MORE DRINKING WATER
      does the same thing. Every source in this item manipulates or observes the
      water content of FOOD. None of them tests bowl water, bowl placement, bowl
      number, or encouragement to drink. The two studies that did test water
      presentation found nothing at the group level -- see
      cat/water-bowl-type-null-003. The honest form of the claim is about what the
      cat eats, not about how the water is offered.
    grade: D
  - note: >
      AND NOT ESTABLISHED: any threshold. There is no moisture percentage in this
      literature above which a cat is protected, no target urine specific gravity
      for a healthy household cat, and no ratio of wet to dry feeding with a study
      behind it. Buckley tested three moisture levels and saw a separation only
      at the highest, with drinking compensating below it; a step between 53.2
      and 73.3 percent on six cats locates no threshold. Converting that into "feed at least X percent wet" is an
      invention. An agent must not generate a numeric feeding target from this
      item.
    grade: D
claim: >
  Higher water content in a cat's FOOD produces more dilute urine and a lower
  relative supersaturation for calcium oxalate. Buckley et al. (2011, British
  Journal of Nutrition) fed six cats the same diet at 25.4, 53.2 and 73.3 percent
  moisture and saw that direction only at 73.3 percent, the one level where total
  fluid intake rose (voluntary drinking fell as food moisture rose); the struvite
  picture was not clear. Markwell et al. (1999, JAVMA) followed 54 cats with idiopathic
  cystitis and reported 16 of 18 on a canned formulation versus 17 of 28 on the
  dry formulation free of recurrent signs within twelve months (p<0.05) -- a
  direction on denominators of 18 and 28, unblinded, with owner-reported
  outcomes, and not a test of moisture alone since the arms differed as products.
  Segev et al. (2011, JFMS), an independent non-industry case-control of 82 cats
  with urethral obstruction against 82 matched controls, found the proportion
  eating only dry food higher in the obstruction group. Both controlled studies
  come from a pet-food manufacturer's research centre (Waltham) and support a
  conclusion favourable to a product category that manufacturer sells; the
  affiliation is carried, not dropped. NOT established by anything here: that
  offering more DRINKING water achieves the same thing (every source manipulates
  food moisture, not bowl water), and any threshold, target urine specific
  gravity, or wet-to-dry feeding ratio. No number in this item is a magnitude.
reasoning: >
  This is the most useful claim available in the domain and it needed the most
  careful handling in the sprint. It is useful because it links a decision a
  household actually makes to a measured physiological outcome, and because
  lower urinary tract disease is one of the highest-frequency serious problems in
  companion cats. It needed care for two independent reasons. First, the sample
  sizes are six and fifty-four, split eighteen against twenty-eight, which is
  the size at which a percentage difference means direction and nothing else --
  quoting 89 versus 61 as an effect size would be precisely the small-sample
  precision the domain checklist flags. Second, and less commonly noticed, both
  controlled studies were produced by the research arm of a pet-food
  manufacturer, and their conclusion favours a product category that
  manufacturer sells. Carrying that affiliation is not a rhetorical hedge; it is
  the same discipline the exercise lane applies to supplement-industry trials,
  and the reason the claim is graded at the small-controlled-study band rather
  than higher despite having three sources. What rescues it from a refusal is the
  third source: an independent Israeli case-control with no food-industry
  funding, landing in the same direction on a harder clinical endpoint. Two
  boundaries are held explicitly. The literature is about food moisture and says
  nothing whatsoever about drinking-water provision, which is a separate question
  answered separately and negatively at item 003; conflating them is the most
  likely misuse. And no threshold exists anywhere in the set, so any numeric
  feeding target generated from this item would be manufactured at answer time.
  Marked contested on the funding structure rather than on a scientific dispute.
---

# cat/dietary-water-urinary-dilution-002

The water in a cat's food changes its urine. That much is supported from three
directions, and it is the closest thing this domain has to an actionable
finding.

A controlled feeding study took six cats and fed them the same diet plain and
then hydrated to roughly a quarter, a half and three-quarters moisture. Only
the three-quarters version made a difference: the cats drank less from the bowl
as the food got wetter, so their total water intake barely moved until the top
level, where urine became more dilute and the supersaturation associated with
calcium oxalate stone formation fell. The struvite side was not clear. Six cats is a direction, not a number.

An older clinical study followed fifty-four cats with idiopathic cystitis and
compared a canned against a dry formulation over twelve months. Substantially
more of the canned group stayed free of recurrent signs. The denominators were
eighteen and twenty-eight, the design was unblinded, and the outcome was
reported by owners. It is also not a clean test of water content, because the two
arms differed as whole products and not only in moisture. The percentages that
get quoted from this study should not be quoted.

The third line matters most, because it is the one nobody paid for. An
independent case-control compared eighty-two cats presenting with urethral
obstruction against eighty-two matched controls, and found exclusively dry-fed
cats over-represented in the obstruction group, along with lower age, higher body
weight and less indoor-outdoor access. Case-control designs carry every confound
you would expect, and a cat fed only dry food probably differs in other ways too.
But it lands in the same place as the feeding studies without a commercial
interest attached.

Which brings up the thing that belongs on the record. Both controlled studies
came out of a pet-food manufacturer's research centre, and what they support is
that wet food is better for a cat's urinary tract than dry food -- a conclusion
about a product category that manufacturer sells. That does not make the
physiology wrong. Urine dilutes when water intake rises, in any mammal. It does
mean the two controlled studies and the commercial interest point the same
direction, and anyone repeating them should say who ran them.

Two things this evidence does not support, both of which are easy to slide into.

It is not about the water bowl. Every study here manipulates or observes the
moisture content of food. None of them tests bowl water, bowl type, bowl
placement or encouragement to drink. That question has been tested separately,
and the answer was nothing.

And there is no threshold anywhere in it. No protective moisture percentage, no
target urine concentration for a healthy household cat, no wet-to-dry ratio with
a study behind it. A specific feeding target derived from this item would be
invented at the moment of answering.
