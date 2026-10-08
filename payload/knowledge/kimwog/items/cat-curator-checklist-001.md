---
# Collection sprint 2026-09-02, cat-domain opening. FIRST item in a new domain.
# The owner filed this area under his RELATIONSHIPS domain, not under pets or
# household maintenance, and that filing is a content instruction: the cat is a
# member of the household with whom there is a relationship, not an object of
# upkeep. Every item in this domain is authored to that framing.
# This row is the domain's grading rule. It exists first because the ceiling of
# veterinary evidence is LOWER than the ceiling of the human-medicine lanes this
# warehouse already carries, and a curator who imports the sleep-recovery or
# mental-health grading anchor unchanged will over-grade almost everything here.
# Rubric: cat @clinical-vet (VC-A, borrowed anchor -- see the notes).
id: cat/curator-checklist-001
domain: cat
grade: D (synthesis rule, not a primary finding)
lane: "@clinical-vet"
locale: universal
as_of: 2026
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/30375948/"  # Halls V. 2018, J Feline Med Surg 20(11):1005-1014, doi 10.1177/1098612X18806757, PMCID PMC11343342 -- states that some recommendations in it rest on the author's 20 years of referral practice rather than on research
  - "https://pubmed.ncbi.nlm.nih.gov/24966283/"  # Carney HC, Sadek TP, Curtis TM, Halls V, Heath S, Hutchison P, Mundschenk K, Westropp JL. 2014, J Feline Med Surg 16(7):579-598, doi 10.1177/1098612X14539092 -- AAFP/ISFM house-soiling guidelines; states they use scientifically documented information where available and the authors' accumulated clinical experience where it is not
  - "https://pubmed.ncbi.nlm.nih.gov/23422366/"  # Ellis SLH, Rodan I, Carney HC, Heath S, Rochlitz I, Shearburn LD, Sundahl E, Westropp JL. 2013, J Feline Med Surg 15(3):219-230, doi 10.1177/1098612X13477537 -- AAFP/ISFM environmental needs guidelines, the domain's anchor consensus document
  - "synthesis: cat/dietary-water-urinary-dilution-002 through cat/kr-registration-gate-013 (checklist derived from this sprint's worked examples, not an independent primary finding)"
refraction_notes:
  - note: >
      THE CEILING IS LOWER HERE, and that is the single most important thing to
      carry out of this row. This warehouse's other clinical lanes are anchored on
      literatures with large randomised trials, formal evidence-grading bodies and
      meta-analytic syntheses. Feline medicine has almost none of that. The
      largest study in this sprint is a UK life-table analysis of 7,936 deaths;
      the intervention studies are 6, 9, 16, 28, 46 and 54 animals. A finding that
      would sit mid-ladder in the sleep or nutrition lanes sits one band lower
      here for the same design, because the replication culture that would confirm
      it does not exist. Do not import the human-medicine anchor unchanged.
    grade: D
  - note: >
      THE PROFESSIONAL BODIES SAY SO THEMSELVES, which is why their guidelines are
      usable rather than suspect. The AAFP/ISFM house-soiling guidelines state
      that they draw on scientifically documented information where it is
      available and on the authors' accumulated clinical experience where it is
      not. The JFMS behaviour-management review that enumerates the environmental
      framework says outright that some of its recommendations come from the
      author's twenty years of referral practice. This is honest authorship and it
      is also a grading instruction: a recommendation carried in a veterinary
      guideline is a consensus artefact by default, and only rises above that
      when a specific study is cited for it.
    grade: D
  - note: >
      THE LADDER FOR THIS DOMAIN. Top band: a jurisdictional legal or regulatory
      fact, read from the statute or the regulator -- verifiable by reading, not
      by trial. Second band: a large observational veterinary dataset (life
      tables, primary-practice records, multi-thousand-animal cohorts) reporting
      DIRECTION, or a validated measurement instrument reporting its own
      reliability. Third band: a small controlled or crossover animal study
      (single digits to low tens), reporting direction only, never magnitude.
      Fourth band: professional-body consensus, and any recommendation a guideline
      itself attributes to clinical experience. Bottom band: pet media, breed
      lore, trainer lore, and any manufacturer statement about a category the
      manufacturer sells into.
    grade: D
  - note: >
      AUTO-REFUSAL TRIGGERS specific to this domain, all of which fired at least
      once in this sprint. A pet-food or pet-product brand cited as evidence for
      its own product category. A number with no study behind it that everybody
      repeats (the folklore in this area is unusually confident). A human-medicine
      finding transplanted to a cat without a feline study. A guideline
      recommendation quoted as though it were a trial result. An effect size taken
      from a study with fewer than about twenty animals. And the specific trap of
      this domain: an authority-shaped source that turns out to be a veterinary
      MARKETING channel rather than a veterinary professional body.
    grade: D
  - note: >
      FUNDING IS NOT INCIDENTAL HERE. Several of the strongest hydration and
      nutrition findings in feline medicine were produced by research centres owned
      by pet-food manufacturers. That does not invalidate them -- they are often
      the only controlled data that exists -- but the affiliation must be carried
      on the item rather than dropped, exactly as the exercise lane does with
      supplement-industry funding at exercise/funding-coi-check-004. Item 002
      carries the worked example.
    grade: D
  - note: >
      THE BOUNDARY, which is a scope rule rather than a grading rule and is
      absolute. This is a warehouse for a life agent, not a veterinary clinic.
      What the evidence says, and what warrants professional attention, are in
      scope. Diagnosis, dosing and treatment protocols are not, at any confidence
      level and no matter how well sourced. An item that would let an agent
      substitute for a veterinarian must not be written even if the source
      supports it.
    grade: D
claim: >
  Grading rule for this domain, synthesized from this sprint's worked examples
  rather than measured independently. The evidence ceiling in feline medicine is
  materially lower than in the human-medicine lanes this warehouse already
  carries: the largest study used in this sprint is a life-table analysis of
  7,936 UK cat deaths, and the intervention studies run 6, 9, 16, 28, 46 and 54
  animals. Ladder: jurisdictional legal fact read from the statute at the top;
  then large observational veterinary datasets reporting direction, and validated
  instruments reporting their own reliability; then small controlled or crossover
  animal studies, direction only and never magnitude; then professional-body
  consensus, including any guideline recommendation the guideline itself
  attributes to clinical experience; pet media, breed lore and manufacturer
  claims about their own product categories at the bottom, which is to say not
  shipped. Auto-refusal triggers: a brand cited for its own category, a
  confidently repeated number with no study behind it, a human finding
  transplanted without a feline study, a guideline recommendation quoted as a
  trial result, an effect size from fewer than roughly twenty animals, and an
  authority-shaped source that is a marketing channel. Manufacturer funding is
  carried on the item, not dropped. Absolute scope boundary: what the evidence
  says and what warrants professional attention are in scope; diagnosis, dosing
  and treatment protocols are not, at any confidence level.
reasoning: >
  This row is written first because the failure mode it prevents is the most
  likely one. A curator arriving from the sleep-recovery or mental-health lanes
  has an internalised sense of what a given study design is worth, and that sense
  is calibrated to a literature with large randomised trials and formal grading
  bodies behind it. Feline medicine does not have those. Applying the same
  instinct produces systematic over-grading, and over-grading in a domain that
  touches a living animal in the owner's household is worse than over-grading a
  training-volume claim. The ladder above is deliberately shaped so that the
  strongest available band is a legal fact rather than a clinical one, because
  that is honestly where the certainty is: what Korean law requires can be read
  off the statute, whereas what a cat needs environmentally rests on a consensus
  document that says in its own text that parts of it are clinical experience.
  Two of the entries are direct imports of discipline this warehouse already
  practises in other lanes -- the funding-affiliation carry from the exercise
  lane, and the refusal-with-a-stated-reason habit from the
  relationships-communication lane -- because both apply here without
  modification and this domain would otherwise have to rediscover them. The scope
  boundary is stated as absolute rather than graded on purpose. It is not an
  evidential judgement and cannot be overridden by a better source.
---

# cat/curator-checklist-001

This domain's evidence has a lower ceiling than the human-medicine lanes next to
it, and every grading decision here has to start from that.

The warehouse's sleep and nutrition lanes sit on literatures with large
randomised trials, formal evidence-grading bodies and meta-analytic syntheses
behind them. Feline medicine has almost none of that infrastructure. The largest
study used anywhere in this sprint is a life-table analysis of just under eight
thousand recorded deaths. The intervention studies run six, nine, sixteen,
twenty-eight, forty-six and fifty-four animals. A design that would earn a solid
place on the ladder in a human lane earns one band less here, because the
replication culture that would confirm it does not exist.

The professional bodies are honest about this, which is what makes their
guidelines usable rather than suspect. The feline house-soiling guidelines state
in their own text that they draw on documented science where it exists and on
the authors' accumulated clinical experience where it does not. The behaviour
review that enumerates the environmental framework says plainly that some of its
recommendations come from twenty years of referral practice. Read that as a
grading instruction: a guideline recommendation is consensus until a specific
study is named for it.

The ladder for this domain, top to bottom. A jurisdictional legal or regulatory
fact, read off the statute -- verifiable by reading rather than by trial, and
therefore the most certain thing available here. Then a large observational
veterinary dataset reporting a direction, or a measurement instrument reporting
its own validated reliability. Then a small controlled or crossover animal study,
which can support a direction and never a magnitude. Then professional-body
consensus. At the bottom, and not shipped: pet media, breed lore, trainer lore,
and any manufacturer claim about a category that manufacturer sells into.

Things that trigger a refusal on sight. A pet-food or pet-product brand offered
as evidence for its own product category. A number everybody repeats that has no
study behind it, which in this area is unusually common. A human-medicine finding
transplanted onto a cat with no feline study. A guideline recommendation quoted
as though it were a trial result. An effect size taken from fewer than about
twenty animals. And the specific trap here, an authority-shaped source that turns
out to be a marketing channel rather than a professional body.

Funding gets carried, not dropped. Some of the best controlled hydration and
nutrition data in feline medicine was produced by research centres owned by
pet-food manufacturers. That does not make it wrong, and it is frequently the
only controlled data in existence, but the affiliation belongs on the item.

One rule is not a grading rule at all and cannot be overridden by a better
source. This is a warehouse for a household assistant, not a clinic. What the
evidence says, and what warrants a professional's attention, are in scope.
Diagnosis, dosing and treatment protocols are not.
