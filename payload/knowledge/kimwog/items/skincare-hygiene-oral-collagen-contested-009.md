---
# Source re-audit 2026-10-06: de Miranda 2021 abstract re-read (holds; full
# text still not retrieved). The funding gap this item named is now partly
# closed by Myung and Park 2025 (Am J Med, PMID 40324552): 23 RCTs pooled
# positive, but trials without company funding and high-quality trials showed
# no effect. One note, the claim tail, reasoning and prose updated; the "no
# claim about sponsorship" lines narrowed to what that abstract shows.
id: skincare-hygiene/oral-collagen-contested-009
domain: skincare-hygiene
lane: "@clinical-derm"
grade: C
locale: universal
as_of: 2025-09
contested: yes
sources:
  - "de Miranda RB, Weimer P, Rossi RC. Effects of hydrolyzed collagen supplementation on skin aging: a systematic review and meta-analysis. Int J Dermatol 2021 Dec;60(12):1449-1461. DOI 10.1111/ijd.15518. PMID 33742704. 19 randomised double-blind controlled trials, 1,125 participants aged 20 to 70, 95 percent women; outcomes skin wrinkles, hydration, elasticity, firmness."
  - "Myung SK, Park Y. Effects of Collagen Supplements on Skin Aging: A Systematic Review and Meta-Analysis of Randomized Controlled Trials. Am J Med 2025 Sep;138(9):1264-1277. DOI 10.1016/j.amjmed.2025.04.034. PMID 40324552. 23 RCTs, 1,474 participants, searched to 2024-06-14; subgroup analysis by funding source and study quality. Abstract read; full text not retrieved."
  - "Pu SY, Huang YL, Pu CM, Kang YN, Hoang KD, Chen KH, Chen C. Effects of Oral Collagen for Skin Anti-Aging: A Systematic Review and Meta-Analysis. Nutrients 2023 Apr 26;15(9):2080. DOI 10.3390/nu15092080. PMID 37432180. 26 RCTs, 1,721 participants; favourable pooled hydration and elasticity, several biases identified in the included trials, no funding stratification in the abstract."
  - "source:skincare-hygiene/self-assessed-outcome-floor-008 -- the placebo-response floor that instrument and self-report endpoints in this literature sit on top of"
  - "source:skincare-hygiene/sunscreen-rct-what-was-shown-001 -- the same warehouse's worked example of an oral supplement for the skin (beta-carotene) randomised against placebo and failing"
  - "source:skincare-hygiene/curator-checklist-015 -- the commercial-capture rule this item is the primary test case for"
refraction_notes:
  - note: >
      THE PUBLICATION EXISTS AND IS POSITIVE. THAT IS NOT THE SAME AS THE CLAIM
      BEING SUPPORTED. A retrievable systematic review with a resolvable DOI in
      a society journal reports favourable pooled results across 19 double-blind
      randomised trials. An assistant must not pretend this literature does not
      exist. It must also not report the conclusion without the four limits
      below.
    grade: A
  - note: >
      WHAT COULD NOT BE VERIFIED IN THIS PASS, STATED AS A GAP RATHER THAN
      GUESSED AT. The full text was not retrievable, so the funding sources of
      the 19 included trials, their individual risk-of-bias assessments, and any
      publication-bias or funnel analysis were NOT read. No claim is made here
      about industry sponsorship of THOSE 19 pooled trials, because that would
      be an assertion without a source. It is recorded as unverified.
    grade: D
  - note: >
      WHEN THE TRIALS ARE SPLIT BY WHO PAID, THE EFFECT GOES AWAY. A 2025
      meta-analysis of 23 randomised trials (1,474 participants) found the
      same favourable pooled result, then split it: trials without funding
      from pharmaceutical companies (the abstract's term) showed no effect on hydration, elasticity or wrinkles,
      trials with company funding did, and high-quality trials showed no
      significant effect in any outcome. Its authors conclude there is
      currently no clinical evidence to support collagen supplements for skin
      aging. Read at abstract level only: the per-subgroup trial counts and
      magnitudes were not seen, and a subgroup split is weaker evidence than
      the pooled randomisation. Speak it as the pattern, not as a number.
    grade: C
  - note: >
      THE OUTCOMES ARE INSTRUMENT AND APPEARANCE MEASURES, WHICH IS WHERE THE
      PLACEBO FLOOR BITES HARDEST. Hydration, elasticity, firmness and wrinkle
      appearance are exactly the endpoint class that moves under placebo and
      under a background routine. This is not a lesion count and not a
      histological endpoint.
    grade: B
  - note: >
      NO SPECIFIC EFFECT SIZE IS CARRIED, DELIBERATELY. The abstract reports
      direction (favourable for hydration, elasticity and wrinkles) without
      pooled magnitudes, and the full text was not read. Quoting a number here
      would be manufacturing precision. Any specific figure a consumer brings
      from a brand page must be treated as unsourced until it is traced to this
      paper or another primary.
    grade: A
  - note: >
      THE SURROUNDING LITERATURE IS THE WARNING. Searches in this pass returned
      predominantly narrative reviews and single-product trials named after the
      branded ingredient being tested. That is the shape of a commercially
      originated evidence base, and it is the reason this item ships as
      contested rather than as a finding.
    grade: C
engine_rules:
  - when: user asks whether a collagen supplement improves skin
    say: contested; pooled trials look positive but the effect sits in company-funded and lower-quality trials, trials without company funding and high-quality trials show no significant effect
    never: say collagen works, or quote an effect size or a dose as proven
    basis: Myung and Park 2025, de Miranda 2021
    basis_grade: C
claim: >
  Oral collagen for skin is contested, and both halves of that have to be spoken.
  A systematic review and meta-analysis published in a dermatology society
  journal searched Medline, Embase, Cochrane, LILACS and the Journal of Negative
  Results in BioMedicine, included 19 randomised double-blind controlled trials
  totalling 1,125 participants aged 20 to 70 (95 percent women), and reported
  favourable pooled results for hydrolyzed collagen supplementation versus
  placebo on skin hydration, elasticity and wrinkles, with hydration and
  elasticity confirmed in subgroup analysis; the authors conclude that ingestion
  for 90 days is effective in reducing skin aging. What could NOT be verified in
  this pass, because the full text was not retrievable, is the funding structure
  of the 19 included trials, their individual risk-of-bias ratings, and whether
  any publication-bias analysis was performed. The endpoints are instrumental and
  appearance measures of the class most affected by placebo response and by the
  background routine imposed on both arms. A later and larger meta-analysis (23
  randomised trials, 1,474 participants) reproduced the favourable pooled result
  but found, in subgroup analysis, no effect in trials without company funding
  and no significant effect in high-quality trials, and concluded there is
  currently no clinical evidence to support collagen supplements for skin aging.
  No pooled effect magnitude is carried in this item.
reasoning: >
  This is the domain's hardest case and the one that decides whether the lane is
  honest. Refusing it outright would be wrong: a real systematic review with a
  resolvable identifier, a stated search strategy across five databases including
  a negative-results database, and 19 double-blind randomised trials is not
  nothing, and an assistant that pretends the literature is empty will be caught
  and rightly distrusted. Reporting its conclusion at face value would also be
  wrong: the endpoints are the instrument and appearance measures most vulnerable
  to the placebo floor documented elsewhere in this lane, the surrounding
  literature located in the same searches consists of narrative reviews and trials
  named after the branded ingredient under test, and the funding and
  risk-of-bias structure underneath the 2021 pooled estimate could not be read.
  The 2025 funding-stratified analysis is the first sourced look underneath a
  pooled estimate in this literature, and it points the way the commercial-
  capture rule predicts: the effect sits in the company-funded and lower-quality
  trials. It is a subgroup analysis read at abstract level, which is why the
  item tilts toward "not supported" without leaving the contested band. The
  resolution is to ship it as contested with the gap named as a gap rather than
  filled by assumption. The warehouse already holds the relevant control case: in
  a randomised trial in this same domain, an oral supplement marketed for the
  skin -- beta-carotene at 30 mg per day -- was tested against placebo alongside a
  topical measure and showed no overall effect, while the topical measure moved the outcome.
  That is the prior an assistant should carry into any oral-supplement skin claim.
---

# skincare-hygiene/oral-collagen-contested-009

Collagen supplements are the most commercially loaded question in this domain and
the answer has to carry both halves or it is dishonest.

The literature is not empty. A systematic review and meta-analysis in a
dermatology society journal searched Medline, Embase, Cochrane, LILACS and the
Journal of Negative Results in BioMedicine -- including a negative-results
database, which is more than most reviews in this space bother with. It included
19 randomised, double-blind, controlled trials, 1,125 participants aged 20 to 70,
95 percent of them women. Pooled, it reported favourable results for hydrolyzed
collagen against placebo on hydration, elasticity and wrinkles, with hydration
and elasticity holding up in subgroup analysis. The authors conclude that ninety
days of supplementation is effective against skin aging.

Now what is missing, said as missing rather than assumed.

The full text was not retrievable in this pass. So the funding sources of the 19
pooled trials were not read, their individual risk-of-bias ratings were not read,
and whether any publication-bias analysis was done is unknown. This item makes no
claim about who funded those 19 trials, because asserting one without having read
it would be the same offence as the marketing it is meant to guard against.

A later review did look. A 2025 meta-analysis of 23 randomised trials, 1,474
participants, got the same favourable result when everything was pooled. Then it
split the trials by funding. The ones without company money showed no effect on
hydration, elasticity or wrinkles; the company-funded ones did. The high-quality
trials showed no significant effect on anything. The authors' conclusion is that
there is currently no clinical evidence to support collagen supplements for skin
aging. Only the abstract was read, so the size of each subgroup is not known, and
a subgroup split is a weaker kind of evidence than the trials themselves. But it
is a sourced look under the pooled number, and it points one way.

The endpoints are the vulnerable kind. Hydration, elasticity, firmness, wrinkle
appearance -- instrument readings and appearance judgements, not lesion counts and
not histology. This lane already documents what placebo alone does to endpoints
of that class, and it is a lot.

And the searches that found this review also returned, in the same breath,
narrative reviews and trials named after the branded ingredient they were
testing. That is the signature of a literature that grew out of a market rather
than a question.

No number is quoted here on purpose. The abstract reports direction without
pooled magnitudes and the full text was not read, so any specific figure would be
invented. If a specific effect size arrives from a brand page, it is unsourced
until traced.

The warehouse holds the right prior for this. In the Queensland sunscreen trial,
an oral supplement sold for the skin -- beta-carotene, 30 mg a day -- was
randomised against placebo alongside a topical intervention. The topical
intervention moved the outcome. The supplement showed no effect on skin cancer
and no overall effect on skin aging. That is what an oral skin supplement looks like when
somebody with no stake in selling it runs the trial.
