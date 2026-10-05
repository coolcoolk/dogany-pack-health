---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (leisure domain opening).
# The KR-locale row for 술. Most of the alcohol literature is Western; this is
# the part of it that is specifically NOT transferable, and it runs in the
# direction of the Korean case being different rather than merely unstudied.
# Lane: @drinking-epidemiology (VC-B).
id: leisure/kr-aldh2-flushing-010
domain: leisure
grade: "B (the ALDH2 rs671 genotype distribution in a large Korean sample, and that the inactive allele is common enough to be the default assumption rather than an exception); C (the acetaldehyde-exposure mechanism and its cancer relevance, which is carried from a review rather than a primary measurement); E (any numeric cancer risk multiplier for flushers, which this pass REFUSED to source)"
lane: "@drinking-epidemiology"
locale: KR
as_of: 2009-2023
contested: yes
sources:
  - "Kim, S. S., Park, S. and Jin, H. S. (2021). Interaction between ALDH2 rs671 and life habits affects the risk of hypertension in Koreans: A STROBE observational study. Medicine (Baltimore) 100(28), e26664. https://doi.org/10.1097/MD.0000000000026664"
  - "Brooks, P. J., Enoch, M. A., Goldman, D., Li, T. K. and Yokoyama, A. (2009). The alcohol flushing response: an unrecognized risk factor for esophageal cancer from alcohol consumption. PLoS Medicine 6(3), e50. https://doi.org/10.1371/journal.pmed.1000050"
  - "Zhang, B., Peng, Y. H., Luo, Y., Hong, C. Q., Lin, Y. W., Zhang, Y. L., Xu, Y. W., Su, X. F. and Wu, F. C. (2023). Relationship between esophageal squamous cell carcinoma risk and alcohol-related ALDH2 and ADH1B polymorphisms: Evidence from a meta-analysis and Mendelian randomization analysis. Cancer Medicine 12(20), 20437-20449. https://doi.org/10.1002/cam4.6610"
  - "leisure/alcohol-jcurve-collapse-009"
  - "relationships-communication/kr-weird-transfer-gate-016"
  - "framework:GRADE -- the genotype distribution comes from a large Korean case-control sample (8157 cases, 9550 controls) and is a direct measurement in the target population, hence the observational band. The mechanism is carried from a peer-reviewed review rather than a primary study and drops one band. The cancer magnitude is refused outright because the stratified and unstratified literatures point in opposite directions and this pass could not resolve them."
applicability:
  axes:
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
refraction_notes:
  - note: >
      The Korean numbers, stated exactly. In Korean Genome and Epidemiology
      Study data covering 8157 hypertensive cases and 9550 controls, the ALDH2
      rs671 genotype frequencies were 2.51 percent AA, 26.66 percent GA and
      70.83 percent GG. So roughly 29 percent of this Korean sample carried at
      least one copy of the inactive allele. Nearly three in ten is not a rare
      variant to be handled as an exception; it is a population feature.
    grade: B
  - note: >
      What the variant does. rs671 is specific to East Asia and impairs the
      enzyme that clears acetaldehyde, the first metabolite of ethanol.
      Carriers accumulate acetaldehyde after drinking, which is the flushing
      response -- the reddening, the racing heart, the nausea. The reason this
      matters beyond discomfort is that acetaldehyde, not ethanol, is the
      carcinogenic species in the upper digestive tract.
    grade: C
  - note: >
      REFUSED, and the refusal is the point. No numeric cancer-risk multiplier
      for flushing drinkers is carried. Two literatures point in opposite
      directions and this pass could not reconcile them from primary stratified
      data. Unstratified pooling (Zhang et al. 2023, 23 publications) reports
      rs671 as APPARENTLY PROTECTIVE against oesophageal squamous cell carcinoma
      (OR 0.60, 95 percent CI 0.50-0.73) -- because the allele stops people
      drinking in the first place -- and its own Mendelian randomisation found no
      causal effect of alcohol on oesophageal cancer. Drinker-stratified figures
      showing sharply ELEVATED risk in heterozygous drinkers circulate from a
      pooling published without a DOI in a low-tier journal, which this warehouse
      does not ship. Until a stratified primary with a resolvable citation is
      read, the magnitude stays unstated.
    grade: E
  - note: >
      What the two directions actually mean, because the contradiction is
      informative rather than merely confusing. The gene has two effects that
      run opposite ways: it raises risk PER DRINK, and it lowers the number of
      drinks. Pooled without stratifying by drinking, the second effect wins and
      the variant looks protective. That is not a finding about safety; it is a
      finding about behaviour. A carrier who drinks anyway has the exposure
      without the protection.
    grade: C
  - note: >
      Why the Western literature under-describes the Korean case. Most alcohol
      epidemiology is sampled from populations in which this variant is rare, so
      the average per-drink exposure in those cohorts is not the average
      per-drink exposure here. Note also the direction of the reinforcement in
      the neighbouring item: the strongest genetic evidence against the
      moderate-drinking benefit (Millwood et al. 2019) is itself an East Asian
      study using this same variant, so the anti-J-curve conclusion is if
      anything BETTER evidenced for this locale than for the West.
    grade: C
  - note: >
      What may be said to a person, and it is deliberately non-clinical. That
      flushing is a metabolic signal rather than a tolerance quirk is worth
      knowing and is well supported. That it is common in Korea is measured.
      Anything past that -- a risk figure, a threshold, a screening
      recommendation -- is not this warehouse's to give and belongs to a
      clinician.
    grade: B
claim: >
  About three in ten Koreans carry a gene variant that changes what a drink does
  to them, which makes the Korean case structurally different from the Western
  cohorts most alcohol research is drawn from. In Korean Genome and Epidemiology
  Study data (Kim, Park and Jin, 2021; 8157 hypertensive cases and 9550
  controls), ALDH2 rs671 genotype frequencies were 2.51 percent AA, 26.66 percent
  GA and 70.83 percent GG -- roughly 29 percent carrying at least one inactive
  allele. The variant is East-Asia-specific and impairs clearance of
  acetaldehyde, the first metabolite of ethanol, producing the flushing response
  and leaving carriers with higher acetaldehyde exposure per drink; acetaldehyde
  rather than ethanol is the carcinogenic species in the upper digestive tract
  (Brooks et al., 2009). This item deliberately ships NO numeric cancer risk
  multiplier for flushing drinkers. Unstratified meta-analysis reports rs671 as
  apparently protective against oesophageal squamous cell carcinoma (Zhang et
  al., 2023; OR 0.60, 95 percent CI 0.50-0.73) because the allele suppresses
  drinking, while drinker-stratified figures showing sharply elevated risk
  circulate only from a pooling published without a resolvable DOI in a low-tier
  journal. The contradiction is explicable -- the variant raises risk per drink
  and lowers drinks per person, and pooling without stratification lets the
  second effect dominate -- but explicable is not the same as quantified, so the
  magnitude stays unstated until a stratified primary is read. Two consequences
  for locale handling: flushing is a metabolic signal rather than a tolerance
  quirk, and the strongest genetic evidence against the moderate-drinking benefit
  is itself an East Asian study using this same variant, so that conclusion
  transfers to this locale better than most of the literature does.
reasoning: >
  The instruction governing this domain was to check the Korean case rather than
  assume the Western one, and here that check returns something sharper than a
  missing local study: a measured population difference in how alcohol is
  metabolised, in a Korean sample, with a resolvable citation. That is the
  strongest form a locale item can take and it is why the genotype distribution
  rather than any outcome is the anchor. The refusal is the other half of the
  item and is written as prominently as the finding. The famous version of this
  claim -- flushers who drink face a large multiple of oesophageal cancer risk --
  is probably directionally right and could not be shipped, because the
  best-indexed recent pooling reports the opposite sign for the unstratified
  comparison and the stratified figures trace to a journal this warehouse will
  not cite. Shipping the intuitive answer while the one retrievable meta-analysis
  says the reverse would have been the domain's worst available failure, so the
  contradiction is carried openly along with the reason it exists. The reason it
  exists is itself useful: a gene that reduces exposure by reducing consumption
  will look protective in any analysis that does not condition on consumption,
  and a carrier who drinks anyway gets the harm without the protection. Flagged
  contested on that unresolved sign. The item is also kept deliberately
  non-clinical: it states what is measured and stops, because risk figures,
  thresholds and screening advice are a clinician's to give and not a life
  agent's.
---

# leisure/kr-aldh2-flushing-010

Roughly three Koreans in ten carry a gene variant that changes what alcohol does
inside them. That is not a footnote to the Western research; it is the reason the
Western research does not fully describe this place.

The measurement is Korean. In genome and epidemiology study data covering more
than seventeen thousand Korean adults, about 2.5 percent carried two copies of
the inactive ALDH2 variant and about 27 percent carried one. Nearly thirty
percent of the sample. That is not a rare condition to be handled as an
exception. It is a feature of the population.

What the variant does is slow the clearance of acetaldehyde, the substance
ethanol turns into first. Carriers accumulate it after a drink, which is what
the flushing is -- the red face, the fast heart, the queasiness. The reason this
is worth more than a note about tolerance is that acetaldehyde, not the alcohol
itself, is the carcinogenic agent in the mouth, throat and oesophagus. Flushing
is a metabolic readout, not a quirk of constitution.

Here is where this item stops, and the stopping is deliberate.

No number is given for how much cancer risk a flushing drinker carries. The
famous version of that claim is probably pointed in the right direction and it
cannot be shipped from what was located. The most recent well-indexed pooling of
twenty-three studies reports the variant as apparently *protective* against
oesophageal cancer -- odds ratio 0.60 -- and its own genetic analysis found no
causal effect of alcohol on that cancer at all. The stratified figures that show
sharply raised risk among carriers who drink come from a pooling published
without a resolvable citation in a journal this warehouse will not cite.

The contradiction is explicable, and the explanation is the useful part. The
variant does two opposite things at once. It raises the harm per drink, and it
cuts the number of drinks, because drinking is unpleasant. Pool everyone together
without asking who actually drinks and the second effect swamps the first, and
the gene looks like a shield. It isn't one. It is a deterrent, and a deterrent
only protects the people who heed it. A carrier who drinks through the flush gets
the exposure without the discount.

Explicable is not quantified, so the magnitude stays blank until someone reads a
stratified primary with a citation that resolves.

One direction of reinforcement worth carrying. The strongest genetic evidence
against the whole moderate-drinking-is-good story comes from a study of half a
million adults in China using this very variant as its instrument. So unusually
for this warehouse, that conclusion is better evidenced for this part of the
world than for the West -- the transfer problem runs the other way for once.
