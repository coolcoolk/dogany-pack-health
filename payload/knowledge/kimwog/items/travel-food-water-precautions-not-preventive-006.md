---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The domain's biggest folklore, refuted, with a deliberately narrow refutation.
# "Boil it, cook it, peel it, or forget it" is the single most repeated sentence
# in travel health and it does not have the evidence people assume. The item
# ships the refutation of the INCIDENCE claim and explicitly refuses to convert
# it into permission, which is the reverse error and the easier one to make.
# Source re-audit 2026-10-06: Shlim 2005 abstract re-read (confirmed); Riddle
# 2017 full text re-read from the author PDF at OpenBU. Changed: (1) the
# guideline's silence is a SCOPE absence -- its five key questions never ask
# about food or water precautions -- so the 'corroboration' note is withdrawn;
# (2) Kozicki 1985, the study the rule is named for, found incidence
# proportionate to the number of dietary mistakes in 688 charter passengers,
# the opposite of Shlim's count; Shlim's full text is closed-access, so the two
# abstracts stay in unresolved tension: B -> C and 'refuted' -> 'not
# demonstrated, record mixed'; (3) the Korean authority wording this item said it
# lacked is now quoted verbatim from the KDCA 해외여행전 page; (4) the
# guideline's issue pages are S63-S80 (PubMed lists S57-S74).
id: travel/food-water-precautions-not-preventive-006
domain: travel
lane: "@travel-clinical"
grade: C (food-selection precautions have not been demonstrated to reduce travellers' diarrhoea incidence; the observational record is mixed); C (the underlying restaurant-hygiene explanation); D (any quantified protective effect in either direction)
locale: universal
as_of: 2005-2017
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/16267714/"  # Shlim DR. 2005, Clin Infect Dis 41(Suppl 8):S531-S535, doi 10.1086/432947 -- the review that collected the studies. Abstract read verbatim 2026-09-02
  - "https://pubmed.ncbi.nlm.nih.gov/28521004/"  # Riddle MS, Connor BA, Beeching NJ, DuPont HL, Hamer DH, Kozarsky P, Libman M, Steffen R, Taylor D, Tribble DR, Vila J, Zanger P, Ericsson CD. 2017, J Travel Med 24(suppl_1):S57-S74, doi 10.1093/jtm/tax026, PMCID PMC5731448 -- the graded expert-panel guideline. Full text read at PMC 2026-09-02, and read SPECIFICALLY to check whether it issues a graded food-and-water-precaution recommendation. It does not. Re-read 2026-10-06 from the author PDF at OpenBU (https://hdl.handle.net/2144/31138; the issue's own page range is S63-S80): its five key questions never ask about food or water precautions, so the absence is scope, not a verdict
  - "https://pubmed.ncbi.nlm.nih.gov/3988431/"  # Kozicki M, Steffen R, Schär M. 1985, Int J Epidemiol 14(1):169-172, doi 10.1093/ije/14.1.169 -- 688 of 2240 air-charter passengers to Kenya, West Africa, Sri Lanka/Maldives followed for diarrhoea against dietary mistakes. Abstract read verbatim 2026-10-06
  - "https://pubmed.ncbi.nlm.nih.gov/29718436/"  # Evans DP. 2018, J Travel Med 25(suppl_1):S38-S45, doi 10.1093/jtm/tay013 -- loosely searched review of non-pharmacological TD interventions (Google Scholar, QxMD, ReadCube); weak corroboration only. Abstract read verbatim 2026-10-06
  - "https://www.kdca.go.kr/kdca/4916/subview.do"  # 질병관리청 해외여행전 page. Read 2026-10-06 for the Korean authority's food-and-water wording, quoted verbatim in the refraction notes. The page's vaccine block still names the 외교통상부 (the ministry's pre-2013 name), so it is long unrevised
  - "source:travel/td-severity-decision-structure-007 -- what the same guideline DOES recommend, which is a treatment structure rather than a prevention rule"
  - "source:travel/kr-pretravel-decision-structure-009 -- the Korean pre-travel route; note the two-level handling described below"
  - "source:cooking/craft-testing-ceiling-001 -- the adjacent question of what food-handling claims can be tested at all"
  - "framework:absence-of-evidence -- the main source is a narrative review counting studies, not a meta-analysis, and no pooled estimate exists; a second observational study (Kozicki 1985) points the other way. No randomised trial of food selection is cited. The guideline contributes nothing either way: its questions never covered food or water precautions, so its silence is a scope absence, not evidence."
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
      WHAT CUTS THE OTHER WAY: KOZICKI 1985, THE STUDY THE RULE IS NAMED FOR. The
      abstract reports that 688 of 2240 air-charter passengers to Kenya, West
      Africa and Sri Lanka/Maldives volunteered for a follow-up of food and
      beverage items; within the first three days abroad 98 percent accepted
      items whose avoidance is traditionally recommended; the incidence of
      diarrhoea, 19.5 percent, "was proportionate to the number of dietary
      mistakes committed"; and "the most dangerous items were those whose
      avoidance was traditionally recommended". That is the opposite of the
      7-of-8 count above. Whether Kozicki was among Shlim's eight, and why it
      would have been set aside, could not be checked (Shlim's full text is
      closed-access). Two observational readings disagree and no randomised trial
      of food selection is cited, so the honest statement is that the effect has
      not been demonstrated and the record is mixed -- not that it was refuted.
      A loosely searched 2018 review reaches the null reading (advice and
      consumption of higher-risk foods did not track reported TD) and adds that
      the evidence on water purification is mixed too; weak support only.
    grade: C
  - note: >
      THE GUIDELINE'S SILENCE IS A SCOPE ABSENCE, NOT CORROBORATION. The 2017
      graded expert-panel guideline has no recommendation on food and water
      precautions, and the full text, re-read 2026-10-06, shows why: its five key
      questions are antibiotic prophylaxis and traveller characteristics,
      diagnostics, MDR colonisation and how to direct travellers on expectant
      management, OTC agents, antibiotics and seeking care, how to convey risk and
      benefit, and the microbiome. Behavioural precautions were never a question,
      and its stated aim is practical guidance on antibiotic and non-antibiotic
      therapies. The earlier reading of the silence as a panel declining to grade
      the field's most famous advice is withdrawn; the absence carries no
      evidential weight either way.
    grade: D
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
      THE KOREAN AUTHORITY'S WORDING, QUOTED. The 질병관리청 해외여행전 page (read
      2026-10-06), under 해외여행 전 주의사항, says: 길거리에서 파는 음식은 피하고,
      음식은 되도록 익혀 드세요. / 손을 자주 깨끗하게 씻고, 사람이 많이 모여있는 실내
      공간에서는 마스크를 착용하세요. / 물은 생수를 사 먹거나, 끓여 드세요. Its
      vaccine block adds, for 콜레라: 예방은 철저한 개인위생과 안전한 음식섭취로
      충분하며. That block still names the 외교통상부, the ministry's pre-2013 name,
      so the page is long unrevised; treat it as what the authority publishes, not
      as a current clinical schedule. The two-level handling stands: report what
      the authority instructs as what the authority instructs, and report
      separately that the evidence for reduced incidence has not been demonstrated
      and is mixed. Do not use this item to contradict a public-health instruction
      to a user.
    grade: A
  - note: >
      WHAT WOULD ACTUALLY CLOSE THIS. A prospective study randomising or at least
      systematically measuring food-selection behaviour against laboratory-confirmed
      travellers' diarrhoea, with water source measured separately, plus a reading
      of Shlim's eight studies against Kozicki's. Nothing of that design was
      located in this pass. Until then the honest statement is that the most
      confidently repeated rule in travel medicine rests on plausibility, and that
      the studies which looked for its effect disagree.
    grade: D
claim: >
  The rule summarised as "boil it, cook it, peel it, or forget it" has not been
  demonstrated to reduce the incidence of travellers' diarrhoea, and the
  observational record is mixed. A 2005 narrative review counting the studies that
  specifically addressed the question found 7 of 8 showing no correlation between
  the types of food selected and the risk of acquiring travellers' diarrhoea; the
  eighth found a correlation between a few dietary mistakes and a DECREASED risk,
  with further mistakes not increasing risk further. The 1985 study the rule is
  named for (688 charter passengers) found the opposite: incidence proportionate
  to the number of dietary mistakes, the traditionally avoided items being the most
  dangerous. No randomised trial of food selection is cited. The 2005 review's own
  explanation is that precautions can work when carried out under the direct
  supervision of someone running their own kitchen, but that poor restaurant
  hygiene in most developing countries creates an insurmountable risk that a
  diner's menu choices cannot route around. The 2017 graded expert-panel guideline
  on travellers' diarrhoea has no recommendation on food and water precautions, but
  its key questions never covered them, so its silence is not evidence either way.
  The Korean authority's published instruction is quoted verbatim in the notes. What
  is NOT claimed: that hygiene is irrelevant, that water source does not matter, or
  that a traveller should stop taking sensible precautions. The claim in question is
  specifically that food SELECTION in restaurants measurably lowers incidence.
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
  more useful than reporting seven-of-eight and stopping. The re-audit found two
  things the first pass did not weigh. Kozicki et al. 1985 (Int J Epidemiol
  14(1):169-172), the study the rule's name comes from, reports the opposite
  pattern in 688 travellers, and Shlim's full text is closed-access, so the
  disagreement could not be resolved; with observational evidence in conflict and
  no trial, the letter is C and the claim is "not demonstrated", not "refuted". And
  Riddle et al. 2017 (J Travel Med 24(suppl_1), PubMed S57-S74, issue pages
  S63-S80) is not corroboration at all: its key questions never asked about food or
  water, so a panel that grades twenty recommendations and does not grade this
  advice was not declining to grade it. Contested is set for the reason this
  warehouse sets it -- the gap between how confidently a claim is spoken and what
  supports it is at its widest here. The part of this item that took the most care
  is the boundary, because the inversion is genuinely harmful and is the
  predictable way an assistant would misuse it. The claim in question is narrow:
  food selection at restaurants, measured against incidence. Water source was not
  the variable. Hand hygiene was not the variable. And the review's own
  explanation -- that hygiene works where you control the kitchen and fails where
  you do not -- means the correct summary is about the limits of a diner's
  control, not about the irrelevance of contamination. The Korean authority's own
  wording is now quoted verbatim from its 해외여행전 page, so the two-level handling
  is complete: the authority instructs this; the evidence that it lowers
  incidence is mixed.
---

# travel/food-water-precautions-not-preventive-006

"Boil it, cook it, peel it, or forget it" is the most confidently repeated
sentence in travel health, and the studies that went looking for its effect have
not demonstrated one -- and do not agree with each other.

A 2005 review of the literature on whether personal hygiene precautions prevent
travellers' diarrhoea counted. Eight studies had specifically addressed the
question. Seven found no correlation between the types of food a traveller
selected and whether they got sick.

The eighth is more interesting than a simple null. It found that making a few
dietary mistakes was associated with a *lower* risk, and that making more mistakes
did not push risk back up. Whatever that pattern is, it is not the dose-response
you would expect if menu choices were driving infection.

And there is a study that points the other way. The one the rule is named for,
from 1985, followed 688 charter passengers to Kenya, West Africa and Sri
Lanka/Maldives and reported that diarrhoea was proportionate to the number of
dietary mistakes, with the traditionally avoided items the most dangerous. The two
accounts cannot both be taken at face value, and the full text of the review was
not readable, so whether it counted that study is unknown. No trial settles it.

The review's explanation is the part worth carrying, because it says something
more useful than "the rule is wrong."

Precautions do work when you control the kitchen. The review's own example is an
expatriate supervising their own household cooking. What fails is the
traveller-at-a-restaurant version, because restaurant hygiene in most developing
countries creates a risk that no amount of choosing between the salad and the
soup can route around. The problem is not that contamination doesn't matter. It is
that a diner does not have the lever people think they have.

One thing that is not evidence: the 2017 expert-panel guideline for travellers'
diarrhoea says nothing about food and water precautions. That is easy to read as a
panel declining to grade the field's most famous advice, and it is not that. The
guideline's own list of questions is about antibiotics, tests, resistance and the
gut microbiome; behaviour was never on it. Its silence counts for nothing either
way.

Now the important part, because this entry is easy to invert and the inversion is
worse than the original folklore.

This does not say eat anything. It does not say drink the tap water. It does not
say ignore what a health authority tells you before a trip. Water source was not
the variable in these studies. Hand hygiene was not the variable. The specific
claim that has not been shown is that a traveller's *food selection in
restaurants* measurably lowers how often they get sick.

So the honest position holds two things at once. Public-health bodies issue
food-and-water advice and a traveller should follow the advice they are given. The
Korean disease-control authority's page says it plainly: 길거리에서 파는 음식은
피하고, 음식은 되도록 익혀 드세요; 물은 생수를 사 먹거나, 끓여 드세요; 손을 자주
깨끗하게 씻고. And the belief that following it reliably prevents travellers'
diarrhoea is not something anyone has managed to demonstrate. Someone who gets ill
after being careful was not necessarily careless. They may simply have been in a
restaurant.
