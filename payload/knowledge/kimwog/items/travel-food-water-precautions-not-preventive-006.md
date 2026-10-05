---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The domain's biggest folklore, refuted, with a deliberately narrow refutation.
# "Boil it, cook it, peel it, or forget it" is the single most repeated sentence
# in travel health and it does not have the evidence people assume. The item
# ships the refutation of the INCIDENCE claim and explicitly refuses to convert
# it into permission, which is the reverse error and the easier one to make.
id: travel/food-water-precautions-not-preventive-006
domain: travel
lane: "@travel-clinical"
grade: B (food-selection precautions have not been shown to reduce travellers' diarrhoea incidence); C (the underlying restaurant-hygiene explanation); D (any quantified protective effect in either direction)
locale: universal
as_of: 2005-2017
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/16267714/"  # Shlim DR. 2005, Clin Infect Dis 41(Suppl 8):S531-S535, doi 10.1086/432947 -- the review that collected the studies. Abstract read verbatim 2026-09-02
  - "https://pubmed.ncbi.nlm.nih.gov/28521004/"  # Riddle MS, Connor BA, Beeching NJ, DuPont HL, Hamer DH, Kozarsky P, Libman M, Steffen R, Taylor D, Tribble DR, Vila J, Zanger P, Ericsson CD. 2017, J Travel Med 24(suppl_1):S57-S74, doi 10.1093/jtm/tax026, PMCID PMC5731448 -- the graded expert-panel guideline. Full text read at PMC 2026-09-02, and read SPECIFICALLY to check whether it issues a graded food-and-water-precaution recommendation. It does not
  - "source:travel/td-severity-decision-structure-007 -- what the same guideline DOES recommend, which is a treatment structure rather than a prevention rule"
  - "source:travel/kr-pretravel-decision-structure-009 -- the Korean pre-travel route; note the two-level handling described below"
  - "source:cooking/craft-testing-ceiling-001 -- the adjacent question of what food-handling claims can be tested at all"
  - "framework:absence-of-evidence -- the primary source is a narrative review counting studies, not a meta-analysis, and no pooled estimate exists. The guideline contribution is a STRUCTURAL absence: a 20-recommendation graded panel that issues no graded recommendation on food and water precautions. An absence in a guideline is weaker evidence than a negative recommendation and is reported as such."
applicability:
  axes:
    - key: medication_list
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      WHAT WAS ACTUALLY FOUND. Reviewing the literature on whether personal
      hygiene precautions prevent travellers' diarrhoea, 7 of 8 studies that
      specifically addressed the question showed NO correlation between the types
      of food selected and the risk of acquiring travellers' diarrhoea. The eighth
      showed a correlation between a few dietary mistakes and a DECREASED risk,
      and a further increase in the number of dietary mistakes did not continue to
      increase risk -- which is a dose-response running the wrong way and is itself
      an argument against a causal reading.
    grade: B
  - note: >
      THE EXPLANATION THE SOURCE OFFERS, AND WHY IT MATTERS MORE THAN THE
      REFUTATION. The review's own account is that precautions CAN prevent
      travellers' diarrhoea when performed under the direct supervision of an
      expatriate running his or her own kitchen, but that poor restaurant hygiene
      in most developing countries continues to create an insurmountable risk. So
      the claim being refuted is not "hygiene is irrelevant." It is "the choices
      available to a traveller at someone else's table are the ones that matter."
      The failure is one of control, not of biology.
    grade: C
  - note: >
      THE GUIDELINE'S SILENCE IS CORROBORATION, AND IT IS ONLY THAT. The 2017
      graded expert-panel guideline developed 20 graded recommendations plus three
      non-graded consensus statements covering prophylaxis, diagnosis, therapy and
      follow-up. Its full text was read for this item specifically to see whether
      food and water precautions appear as a graded recommendation. They do not.
      A panel that grades this much and declines to grade the most famous advice in
      the field is telling you something -- but an absence is weaker than an
      explicit negative recommendation, and it is graded here as corroboration
      rather than as a second refutation.
    grade: C
  - note: >
      THE REVERSE ERROR IS THE DANGEROUS ONE. This item does NOT say eat anything,
      drink the tap water, or ignore public-health advice. What has not been shown
      is that a traveller's food SELECTION at restaurants reduces incidence. Water
      source, hand hygiene, and the specific high-risk exposures that other lanes
      of this warehouse cover were not the variable in these studies. Anyone
      turning this entry into permission has inverted it, and an assistant
      repeating it must say the narrow version or say nothing.
    grade: A
  - note: >
      NO KOREAN AUTHORITY WORDING IS QUOTED HERE, DELIBERATELY. Pre-travel advice
      from health authorities, including Korea's, generally does issue food-and-
      water precautions, and no verbatim Korean regulator wording on this point was
      captured in this pass, so none is quoted or attributed. The two-level
      handling this warehouse uses stands regardless: report what the authority
      instructs as what the authority instructs, and report separately that the
      controlled evidence for reduced incidence is absent. Do not use this item to
      contradict a public-health instruction to a user. Closing the Korean wording
      is recorded as a gap.
    grade: C
  - note: >
      WHAT WOULD ACTUALLY CLOSE THIS. A prospective study randomising or at least
      systematically measuring food-selection behaviour against laboratory-confirmed
      travellers' diarrhoea, with water source measured separately. Nothing of that
      design was located in this pass. Until then the honest statement is that the
      most confidently repeated rule in travel medicine rests on plausibility, and
      that the studies which looked for its effect did not find one.
    grade: D
claim: >
  The rule summarised as "boil it, cook it, peel it, or forget it" is not supported
  as a way of reducing the incidence of travellers' diarrhoea. Reviewing the
  literature that specifically addressed the question, 7 of 8 studies showed no
  correlation between the types of food selected and the risk of acquiring
  travellers' diarrhoea; the eighth found a correlation between a few dietary
  mistakes and a DECREASED risk, with further mistakes not increasing risk further.
  The review's own explanation is that precautions can work when carried out under
  the direct supervision of someone running their own kitchen, but that poor
  restaurant hygiene in most developing countries creates an insurmountable risk
  that a diner's menu choices cannot route around. Corroborating this structurally
  rather than directly: the 2017 graded expert-panel guideline on travellers'
  diarrhoea produced 20 graded recommendations plus three non-graded consensus
  statements on prophylaxis, diagnosis, therapy and follow-up, and issues no graded
  recommendation on food and water precautions at all. What is NOT claimed: that
  hygiene is irrelevant, that water source does not matter, or that a traveller
  should stop taking sensible precautions. The refuted claim is specifically that
  food SELECTION in restaurants measurably lowers incidence.
reasoning: >
  This is the domain's equivalent of the cooking lane's salted-pasta-water entry:
  a rule everybody repeats, stated with total confidence, resting on plausibility
  rather than measurement. Shlim 2005 (Clin Infect Dis 41 Suppl 8:S531-S535) is a
  narrative review rather than a meta-analysis and that caps how high this can be
  graded, but the thing it does is exactly the thing needed -- it goes and counts
  the studies that actually asked the question, and reports that seven of eight
  found nothing. The eighth result is worth more than a footnote, because it does
  not point the other way in a clean fashion either: a few dietary mistakes
  associated with LOWER risk and additional mistakes not raising it is a shape
  incompatible with a simple exposure-response story, and reporting it honestly is
  more useful than reporting seven-of-eight and stopping. The corroboration from
  Riddle et al. 2017 (J Travel Med 24(suppl_1):S57-S74) is structural and is
  deliberately weighted as such: the full text was read for this specific purpose,
  a panel that graded twenty recommendations across the whole clinical course does
  not grade the field's most famous piece of advice, and that is informative
  without being a negative recommendation. Contested is set for the reason this
  warehouse sets it -- the gap between how confidently a claim is spoken and what
  supports it is at its widest here. The part of this item that took the most care
  is the boundary, because the inversion is genuinely harmful and is the
  predictable way an assistant would misuse it. The claim being refuted is narrow:
  food selection at restaurants, measured against incidence. Water source was not
  the variable. Hand hygiene was not the variable. And the review's own
  explanation -- that hygiene works where you control the kitchen and fails where
  you do not -- means the correct summary is about the limits of a diner's
  control, not about the irrelevance of contamination. No Korean authority wording
  is quoted here because none was captured verbatim in this pass, and inventing
  or paraphrasing a regulator's instruction to set up a contrast would be worse
  than leaving the contrast general.
---

# travel/food-water-precautions-not-preventive-006

"Boil it, cook it, peel it, or forget it" is the most confidently repeated
sentence in travel health, and the studies that went looking for its effect did
not find one.

Someone reviewed the literature on whether personal hygiene precautions prevent
travellers' diarrhoea and counted. Eight studies had specifically addressed the
question. Seven found no correlation between the types of food a traveller
selected and whether they got sick.

The eighth is more interesting than a simple null. It found that making a few
dietary mistakes was associated with a *lower* risk, and that making more mistakes
did not push risk back up. Whatever that pattern is, it is not the dose-response
you would expect if menu choices were driving infection.

The review's explanation is the part worth carrying, because it says something
more useful than "the rule is wrong."

Precautions do work when you control the kitchen. The review's own example is an
expatriate supervising their own household cooking. What fails is the
traveller-at-a-restaurant version, because restaurant hygiene in most developing
countries creates a risk that no amount of choosing between the salad and the
soup can route around. The problem is not that contamination doesn't matter. It is
that a diner does not have the lever people think they have.

There is a second, quieter piece of evidence. The 2017 expert-panel guideline for
travellers' diarrhoea produced twenty graded recommendations and three consensus
statements covering prevention, diagnosis, treatment and follow-up. It does not
issue a graded recommendation on food and water precautions. A panel that grades
that much and declines to grade the field's most famous advice is not saying
nothing. It is also not saying the advice is wrong, which is why this counts as
corroboration rather than as a second refutation.

Now the important part, because this entry is easy to invert and the inversion is
worse than the original folklore.

This does not say eat anything. It does not say drink the tap water. It does not
say ignore what a health authority tells you before a trip. Water source was not
the variable in these studies. Hand hygiene was not the variable. The specific
claim that failed is that a traveller's *food selection in restaurants* measurably
lowers how often they get sick.

So the honest position holds two things at once. Public-health bodies issue
food-and-water advice and a traveller should follow the advice they are given. And
the belief that following it reliably prevents travellers' diarrhoea is not
something anyone has managed to demonstrate. Someone who gets ill after being
careful was not careless. They were in a restaurant.
