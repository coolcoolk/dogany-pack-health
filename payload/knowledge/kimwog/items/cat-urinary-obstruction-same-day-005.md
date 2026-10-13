---
# Collection sprint 2026-09-02, cat-domain opening. The "what warrants
# professional attention" row, and the one place where the scope boundary had to
# be enforced hardest. Urinary obstruction is the highest-stakes common feline
# emergency and it is also the one an owner is most likely to mistake for a
# litter-box behaviour problem. This item ships the SEVERITY PROFILE and the
# resulting posture (same-day, not watch-and-wait) and deliberately refuses to
# ship a presenting-sign checklist, because no source read in this sprint
# supplied one that could be verified.
# Rubric: cat @clinical-vet (VC-A, borrowed anchor -- read one band down).
id: cat/urinary-obstruction-same-day-005
domain: cat
grade: C (the severity profile: mortality, recurrence and cardiovascular-event frequencies as reported in the two cohorts); D (any presenting-sign checklist, any sex ratio, and anything at all about management)
lane: "@clinical-vet"
locale: universal
as_of: 2011-2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/21145768/"  # Segev G, Livne H, Ranen E, Lavy E. 2011, J Feline Med Surg 13(2):101-108, doi 10.1016/j.jfms.2010.10.006 -- 82 cats with urethral obstruction vs 82 sex- and time-matched controls; overall mortality 8.5 pct; recurrence 22 pct at 6 months and 24 pct at 2 years
  - "https://pubmed.ncbi.nlm.nih.gov/38164379/"  # Duperrier-Simond C, Pouzot-Nevoret C, Allaouchiche B, Nectoux A, Cadore JL, Krafft E. 2024, Can Vet J 65(1):67-74 -- 168 cats with acute urinary tract obstruction (56 upper, 112 lower); cardiovascular events in 61.9 pct, arrhythmia 33.6 pct, gallop rhythm 28.1 pct, heart murmur 15.3 pct. No DOI on the PubMed record; PMID 38164379 is the resolvable identifier
  - "https://pubmed.ncbi.nlm.nih.gov/24966283/"  # Carney HC, Sadek TP, Curtis TM, Halls V, Heath S, Hutchison P, Mundschenk K, Westropp JL. 2014, J Feline Med Surg 16(7):579-598, doi 10.1177/1098612X14539092 -- AAFP/ISFM house-soiling guidelines, written as a resource for veterinary practitioners, which is the routing fact this item uses
  - "cat/curator-checklist-001"  # the domain rule this item obeys, including the absolute scope boundary on diagnosis and management
refraction_notes:
  - note: >
      THE SEVERITY PROFILE, which is what licenses the posture. Segev 2011
      followed 82 cats presenting with urethral obstruction against 82 matched
      controls and reported overall mortality of 8.5 percent, with recurrence at
      22 percent within 6 months and 24 percent within 2 years. Duperrier-Simond
      2024 reviewed 168 cats with acute urinary tract obstruction, 56 upper and
      112 lower, and found cardiovascular events in 61.9 percent of them --
      arrhythmia 33.6 percent, gallop rhythm 28.1 percent, heart murmur 15.3
      percent -- with elevated potassium, pre-existing chronic kidney disease and
      renal pelvic dilation among the risk factors. Roughly one animal in twelve
      died and roughly six in ten had a cardiovascular complication. That is the
      whole basis for treating urinary difficulty as a same-day question.
    grade: C
  - note: >
      THESE ARE REFERRAL AND EMERGENCY POPULATIONS, so the percentages describe
      cats who arrived at a clinic already obstructed, not cats in general. A
      mortality figure from a hospital caseload is not a household risk. What
      transfers is the ORDER OF MAGNITUDE of the consequence once the condition
      is present, and that is all this item uses it for. Nothing here supports a
      statement about how likely any particular cat is to obstruct.
    grade: C
  - note: >
      THE OBSERVABLE EVENT MOST LIKELY TO BE MISREAD is a change in litter-box
      behaviour. The AAFP and ISFM published a full guideline document on
      diagnosing and solving house-soiling and wrote it as a resource for
      VETERINARY PRACTITIONERS, which is itself the routing fact: the
      professional bodies treat a cat that stops using its box as a clinical
      question first and a behavioural one second. For a household assistant the
      operational form is that a change in where or how a cat urinates routes to
      a veterinarian, not to a behaviour tip.
    grade: C
  - note: >
      DELIBERATELY NOT SHIPPED: a presenting-sign checklist. The obvious thing
      this item wants is a list -- repeated unproductive trips to the box,
      straining, vocalising, licking, a hard abdomen. That list is everywhere in
      pet media and in clinic handouts, and no source read in this sprint stated
      it in a form that could be quoted. Segev 2011's abstract, which was the
      record actually read, reports predisposing factors and outcomes rather than
      presenting signs. Rather than assemble a plausible list from memory and
      attach three real citations to it, the list is refused. If a later sprint
      wants it, it needs a guideline or a study that states it.
    grade: D
  - note: >
      ALSO NOT VERIFIED IN THIS PASS, and therefore not asserted: the sex ratio.
      It is very widely stated that urethral obstruction is overwhelmingly a
      problem of male cats, on anatomical grounds. That may well be true and the
      anatomy is not in dispute, but Segev 2011 used SEX-MATCHED controls, which
      means the design deliberately removed sex as a variable and the paper cannot
      be cited for it, and no other source read here quantified it. An agent must
      not state a sex ratio on the strength of these citations.
    grade: D
  - note: >
      THE SCOPE BOUNDARY, enforced. Nothing about catheterisation, fluid therapy,
      potassium management, diet after an episode, or when a cat can go home
      belongs in this warehouse, at any confidence level, and the sources here
      would support some of it. This item says that the condition is serious and
      that it routes to a professional promptly. It says nothing about what the
      professional should then do.
    grade: D
  - note: >
      THE ONE PREVENTION-SIDE LINK THAT IS SUPPORTED, kept narrow. Segev 2011
      found the proportion of cats eating ONLY dry food higher in the obstruction
      group than among matched controls, alongside lower mean age and higher mean
      body weight. That association is carried in full at
      cat/dietary-water-urinary-dilution-002 with its confounds. It is a
      case-control association, not a prevention protocol, and it does not belong
      in a sentence that starts "to prevent obstruction".
    grade: D
claim: >
  Urinary obstruction in cats carries consequences severe enough that difficulty
  or change in urination is a same-day veterinary question rather than something
  to observe for a few days. Segev et al. (2011, JFMS) followed 82 cats with
  urethral obstruction against 82 matched controls and reported overall mortality
  of 8.5 percent, with recurrence in 22 percent within 6 months and 24 percent
  within 2 years. Duperrier-Simond et al. (2024, Canadian Veterinary Journal)
  reviewed 168 cats with acute urinary tract obstruction and found cardiovascular
  events in 61.9 percent -- arrhythmia 33.6 percent, gallop rhythm 28.1 percent,
  heart murmur 15.3 percent. Both are clinic populations, so these describe the
  consequence once the condition is present, not a household's risk of it
  occurring. The observable event most likely to be misread is a change in
  litter-box behaviour: the AAFP and ISFM published their house-soiling guidance
  as a resource for veterinary practitioners, which is to say the professional
  bodies route a cat that stops using its box to a clinical work-up first.
  DELIBERATELY NOT SHIPPED: a presenting-sign checklist, because no source read
  in this sprint stated one in quotable form; and the sex ratio, because the
  case-control study used sex-matched controls and therefore cannot be cited for
  it. Nothing about management, treatment or dosing is in scope at any confidence
  level.
reasoning: >
  This row exists because "what warrants professional attention" is squarely in
  this warehouse's scope and "what to do about it" squarely is not, and urinary
  obstruction is where that line is both hardest to hold and most worth holding.
  The severity numbers are strong enough to license the only instruction the item
  gives: roughly one cat in twelve died in the case-control cohort, roughly one
  in four obstructed again within two years, and roughly six in ten had a
  cardiovascular complication in the emergency cohort. Those figures come from
  clinic populations and describe consequence rather than incidence, which the
  item says explicitly, but the order of magnitude is what makes waiting the wrong
  posture. The routing argument rests on a fact about the literature rather than
  a finding inside it: the feline professional bodies wrote their house-soiling
  document for veterinarians, meaning they treat a cat that stops using its box
  as a clinical question before a behavioural one, and that is exactly the
  household-observable event most likely to be misfiled. Two refusals are the
  part of this item most worth reading. A presenting-sign checklist is the
  obvious thing to include and it is not included, because the version everyone
  knows could not be sourced from the records actually read, and attaching three
  genuine citations to a list assembled from memory is the specific failure this
  warehouse exists to prevent. The sex ratio is refused for a sharper reason: the
  one case-control study here used sex-matched controls, so the design removed
  sex on purpose and the paper cannot support a statement about it, however
  confident the anatomy makes everyone. Not marked contested -- nothing in the
  sources disagrees; the uncertainty is absence, not dispute.
---

# cat/urinary-obstruction-same-day-005

Difficulty urinating in a cat is a same-day veterinary question. The reason is
the numbers.

A case-control study followed eighty-two cats presenting with urethral
obstruction. Overall mortality was around eight and a half percent. Roughly
twenty-two percent obstructed again within six months and about a quarter within
two years. A separate review of a hundred and sixty-eight cats with acute urinary
obstruction found cardiovascular complications in about six in ten of them --
arrhythmias in a third, gallop rhythms in nearly three in ten, murmurs in about
one in six.

Both of those are hospital caseloads, so the percentages describe what happens
once a cat is obstructed rather than how likely a given cat is to become
obstructed. That distinction matters and this item does not blur it. What carries
over is the scale of the consequence, and it is large enough that "wait and see
how he is tomorrow" is the wrong posture.

The event a household actually sees is usually a change in litter-box behaviour,
and that is exactly what is most likely to be filed as a behaviour problem. Worth
knowing how the profession itself treats it: the feline veterinary bodies
published their guidance on house-soiling as a document for veterinarians. A cat
that stops using its box is a clinical question first, and a behavioural one
after that has been excluded.

Two things are missing from this item on purpose.

There is no list of signs to watch for. The list everyone knows -- the repeated
unproductive trips, the straining, the vocalising -- is in every clinic handout
and pet article, and none of the records read for this item stated it in a form
that could be quoted. Writing it from memory and hanging three real citations off
it would be the exact failure this warehouse is built to avoid. If someone wants
that list here, it needs its own source.

And there is no sex ratio. It is very widely said that this is overwhelmingly a
male cat's problem, and the anatomy behind that claim is not disputed. But the
case-control study used sex-matched controls, which means it deliberately removed
sex from the comparison and cannot be cited about it, and nothing else read here
quantified it.

Nothing about what happens next -- catheters, fluids, potassium, diet afterwards
-- belongs here at all. This item says the thing is serious and goes to a
professional quickly. What the professional does is theirs.
