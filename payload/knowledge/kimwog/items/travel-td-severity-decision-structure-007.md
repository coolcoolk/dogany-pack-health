---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The lane's decision-structure item: what a graded expert panel says the
# DECISION looks like, deliberately stripped of every drug choice and every
# dose. A life agent's job here is to help someone recognise which situation
# they are in and route accordingly, not to prescribe. The severity definitions
# are functional rather than clinical, which is exactly what makes them usable
# by a non-clinician.
# Source re-audit 2026-10-06: Riddle 2017 full text re-read from the author PDF
# at OpenBU; the definitions and the four quoted prophylaxis recommendations
# confirmed verbatim. Changed: (1) 'on prevention the panel is a qualified no'
# was true of ANTIMICROBIAL prophylaxis only -- recommendation 3, bismuth
# subsalicylate may be considered for any traveller (Strong, HIGH-quality
# evidence), was left out; (2) treatment now carries the severity ladder as
# graded -- antibiotics not recommended for mild (Strong, moderate), may be used
# for moderate (WEAK, moderate), should be used for severe (Strong, high) --
# instead of only the abstract's blanket 'strong evidence ... moderate to
# severe'; (3) the abstract's '20 graded recommendations' counts #20, which
# Table 1 itself marks ungraded; (4) consensus statement 23 quoted as written;
# (5) issue pages S63-S80 (PubMed lists S57-S74); (6) 'several of the agents
# are prescription-only in Korea' had no source in the item and is now stated as
# unsourced.
id: travel/td-severity-decision-structure-007
domain: travel
lane: "@travel-clinical"
grade: B (the severity framework and the graded prophylaxis position); C (the resistance-acquisition counterweight, which the panel itself issued ungraded)
locale: universal
as_of: 2017
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/28521004/"  # Riddle MS, Connor BA, Beeching NJ, DuPont HL, Hamer DH, Kozarsky P, Libman M, Steffen R, Taylor D, Tribble DR, Vila J, Zanger P, Ericsson CD. 2017, J Travel Med 24(suppl_1):S57-S74 (PubMed; the issue's own page range is S63-S80), doi 10.1093/jtm/tax026, PMCID PMC5731448 -- graded expert panel; the abstract counts 20 graded recommendations plus 3 non-graded consensus statements, while Table 1 numbers 23 items and marks #20 ungraded. Full text read at PMC 2026-09-02; re-read 2026-10-06 from the author PDF at OpenBU (https://hdl.handle.net/2144/31138) for Table 1, the definitions and the scope
  - "source:travel/food-water-precautions-not-preventive-006 -- the behavioural prevention side; this guideline never took it up (scope absence, not a verdict)"
  - "source:travel/kr-pretravel-decision-structure-009 -- who a Korean traveller actually asks, since this guideline is not a Korean document"
  - "source:mental-health/no-single-hierarchy-003 -- the warehouse's handling of a field whose authority is an expert panel rather than a regulator"
  - "framework:graded expert panel -- this is a consensus guideline developed with a formal grading and voting process, not a systematic review with pooled estimates. Recommendation STRENGTH and evidence QUALITY move independently in it, and the pattern below is the point: several STRONG recommendations rest on LOW or VERY LOW quality evidence. That combination is legitimate in guideline methodology and must not be reported as strong evidence."
applicability:
  axes:
    - key: medication_list
      type: categorical
      role: soft
      unknown_policy: block_specifics
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: allergen_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
refraction_notes:
  - note: >
      THE SEVERITY DEFINITIONS ARE FUNCTIONAL, NOT CLINICAL, AND THAT IS WHY THEY
      ARE USABLE. Mild: diarrhoea that is tolerable, is not distressing, and does
      not interfere with planned activities. Moderate: diarrhoea that is
      distressing or interferes with planned activities. Severe: diarrhoea that is
      incapacitating or completely prevents planned activities, with dysentery
      counted as severe. Persistent: diarrhoea lasting two weeks or more. Note
      what is absent -- no stool count per day, no duration threshold for the
      acute categories. The panel replaced a frequency-based definition with an
      impact-based one, and an impact-based definition is one a traveller can
      apply to themselves.
    grade: A
  - note: >
      THE ANTIMICROBIAL PROPHYLAXIS POSITION IS A NO WITH A NARROW EXCEPTION, AND
      MOST OF IT IS STRONG RECOMMENDATIONS ON WEAK EVIDENCE. Antimicrobial
      prophylaxis should not be used routinely in travellers -- strong
      recommendation, low or very low quality evidence. Prophylaxis should be
      considered for travellers at high risk of health-related complications --
      strong recommendation, low or very low quality evidence. Fluoroquinolones
      are not recommended for prophylaxis -- strong recommendation, low or very low
      quality evidence. When prophylaxis IS indicated, rifaximin is recommended --
      strong recommendation, moderate quality evidence. Report these as guideline
      positions, never as demonstrated effects. The same section also holds a
      non-antibiotic yes that the first pass left out: bismuth subsalicylate may
      be considered for any traveller to prevent travellers' diarrhoea -- strong
      recommendation, HIGH level of evidence (the text cites three randomised
      trials against placebo). It is the one prevention recommendation in the set
      with high-quality evidence behind it, and it is a drug choice: carried here
      as a pointer, with no dose, no product and no contraindication list, which
      belong to a clinician or pharmacist.
    grade: B
  - note: >
      THE COUNTERWEIGHT THE PANEL ISSUED WITHOUT A GRADE. Consensus statement 23,
      ungraded, as written: there is an incrementally increasing association
      between travel, travellers' diarrhoea, and antibiotic use with the
      acquisition of multidrug-resistant bacteria, and pretravel counselling should
      include information about this risk, balanced against the benefits of
      antibiotic use. The panel put this in its non-graded
      consensus tier, which is where it belongs and also where it is easiest to
      overlook. It is the reason the default is NOT to medicate: the cost of
      treating is not zero and it is partly borne by people who are not the
      traveller.
    grade: C
  - note: >
      WHAT THE GUIDELINE SAYS ABOUT TREATING, AT THE STRUCTURAL LEVEL ONLY. The
      abstract's conclusion: strong evidence supports the effectiveness of
      antimicrobial therapy in most cases of MODERATE to SEVERE travellers'
      diarrhoea, while either increasing fluid intake alone, or loperamide, or
      bismuth subsalicylate may suffice for most cases of MILD diarrhoea. The graded
      recommendations split that sentence by severity. Mild: antibiotic treatment
      is not recommended (strong, moderate-quality evidence); loperamide or
      bismuth subsalicylate may be considered (strong, moderate). Moderate:
      antibiotics MAY be used (WEAK recommendation, moderate-quality evidence).
      Severe: antibiotics SHOULD be used (strong, high-quality evidence); all
      dysentery, meaning grossly bloody stools, counts as severe. So the abstract's
      "moderate to severe" folds a weak recommendation and a strong one together.
      That is the whole of what this warehouse carries. No agent selection beyond
      what is named above, no dose, no duration, no paediatric variation, and
      nothing about pregnancy -- those are prescribing decisions and this is a
      warehouse.
    grade: B
  - note: >
      JURISDICTION. This is an international expert-panel guideline published in a
      travel-medicine journal, not a Korean document and not a regulatory
      instrument anywhere. It describes what an expert panel recommends to
      clinicians. Where a Korean traveller needs an actual decision -- what to
      carry, whether they qualify as high risk -- the route is the Korean one.
      Whether the agents named above are available over the counter or only on
      prescription in Korea is not sourced here and may differ from the countries
      the panel writes for. Do not present an international guideline as a Korean
      instruction; that
      substitution is the specific error the cooking lane was corrected for.
    grade: A
  - note: >
      NOT COVERED HERE. Diagnostics and their utility, follow-up of persistent
      diarrhoea, microbiome effects, the paediatric literature, rehydration
      formulation, and everything about self-treatment kits. The guideline
      addresses several of these; this item carries only the severity framework,
      the prophylaxis position and the resistance counterweight, because those are
      the three things a non-clinical assistant can use without crossing into
      prescribing.
    grade: D
claim: >
  The 2017 graded expert-panel guideline on travellers' diarrhoea reframes the
  problem around functional severity rather than stool frequency. Mild is diarrhoea
  that is tolerable, is not distressing, and does not interfere with planned
  activities; moderate is diarrhoea that is distressing or interferes with planned
  activities; severe is diarrhoea that is incapacitating or completely prevents
  planned activities, with dysentery classed as severe; persistent is diarrhoea
  lasting two weeks or more. On antimicrobial prevention the panel is a qualified
  no: antimicrobial prophylaxis should not be used routinely in travellers (strong
  recommendation, low or very low quality evidence), should be considered for
  travellers at high risk of health-related complications (strong recommendation,
  low or very low quality evidence), fluoroquinolones are not recommended for
  prophylaxis (strong recommendation, low or very low quality evidence), and where
  prophylaxis is indicated rifaximin is recommended (strong recommendation,
  moderate quality evidence). Separately, bismuth subsalicylate may be considered
  for any traveller to prevent travellers' diarrhoea (strong recommendation, high
  level of evidence). At the structural level of treatment, the abstract says
  strong evidence supports antimicrobial therapy in most cases of moderate to
  severe disease, while increased fluid intake alone, loperamide, or bismuth
  subsalicylate may suffice for most mild cases; the graded recommendations split
  this by severity: antibiotic treatment is not recommended for mild disease
  (strong, moderate), may be used for moderate (weak, moderate) and should be used
  for severe (strong, high). The panel additionally issued an ungraded consensus
  statement that there is an incrementally increasing association between travel,
  travellers' diarrhoea, and antibiotic use with the acquisition of
  multidrug-resistant bacteria and that pretravel counselling should include
  information about this risk, balanced against the benefits of antibiotic use. This is an
  international expert-panel document, not a Korean one, and it carries no
  authority as a Korean instruction.
reasoning: >
  A life agent cannot and must not prescribe, but it can help someone see which
  situation they are in, and this guideline happens to define the situations in a
  way a non-clinician can apply. That is the reason this item exists in this shape.
  Riddle et al. 2017 (J Travel Med 24(suppl_1):S57-S74) replaced the old
  frequency-based severity definitions with functional ones -- tolerable, versus
  distressing or interfering, versus incapacitating -- and the change is more
  consequential than it looks: counting stools is a clinical act performed poorly
  by patients, whereas "is this stopping you doing what you came here to do" is a
  question a traveller can answer honestly at three in the morning. Graded in the
  solid band rather than the top band throughout, and the reason is written into
  the framework note: this is a consensus panel using a formal grading process,
  and several of its STRONG recommendations rest on LOW or VERY LOW quality
  evidence. That combination is entirely legitimate in guideline methodology -- a
  panel can be confident about the right action while the underlying trials are
  poor -- but reporting a strong recommendation as strong evidence is precisely
  the collapse this warehouse's grading discipline exists to prevent, and it is the
  same distinction the sleep domain records for the AASM. The ungraded resistance
  statement is deliberately foregrounded despite being the panel's weakest tier,
  because it is the piece that explains the default. Without it, "prophylaxis is
  not routinely recommended" sounds like a shrug about efficacy; with it, the
  reason is visible and it is partly an externality argument. What this item
  refuses to carry is everything downstream of the decision: agent choice beyond
  the names the guideline itself puts in its summary, doses, durations, paediatric
  and pregnancy variation. Those are prescribing, and an assistant that produces
  them has stopped being an assistant. The jurisdiction note is not boilerplate:
  this warehouse dropped a US-only cooking rule earlier the same day for exactly
  the sin of presenting one country's authority as another's, and an international
  panel guideline is not a Korean instruction either.
---

# travel/td-severity-decision-structure-007

The useful thing the travellers' diarrhoea guideline did was stop counting.

Older definitions of severity were built on stool frequency, which is a number
nobody tracks accurately while ill in a hotel room. The 2017 expert panel replaced
it with a functional scale:

- **Mild** -- tolerable, not distressing, does not interfere with what you had
  planned.
- **Moderate** -- distressing, or it interferes with what you had planned.
- **Severe** -- incapacitating, or it completely prevents what you had planned.
  Dysentery counts as severe regardless.
- **Persistent** -- lasting two weeks or more.

That is a scale a traveller can apply to themselves at four in the morning, which
is when the question actually gets asked.

On preventing it with antibiotics, the panel's position is a no with a door in it.
Antibiotic prophylaxis should not be used routinely. It should be considered for
travellers at high risk of health-related complications. Fluoroquinolones are not
recommended for prophylaxis. Where prophylaxis is indicated, rifaximin is the
recommended agent.

Three of those four are strong recommendations built on low or very low quality
evidence, which is worth pausing on. In guideline language, a strong
recommendation says the panel is confident about the right action; it does not say
the trials behind it are good. Repeating "strongly recommended" as "well proven"
is a quiet upgrade and this warehouse does not permit it.

The same section also holds a yes the first version of this entry left out: the
panel says bismuth subsalicylate may be considered for any traveller to prevent
travellers' diarrhoea, and that is a strong recommendation with high-quality
evidence behind it -- the only prevention recommendation in the set that can say
so. It is a drug choice, so it is carried as a pointer, not as a dose or a product.

The reason the default is *not* to medicate with antibiotics sits in the panel's
weakest tier, an ungraded consensus statement: travel, travellers' diarrhoea and
antibiotic use show an incrementally increasing association with picking up
resistant bacteria, and pretravel counselling should include that risk, balanced
against the benefit of antibiotics. Some of the cost of a precautionary course of
antibiotics is paid by people who never went anywhere.

On treatment, only the shape is carried here, and the shape is graded by severity.
For mild diarrhoea, antibiotics are not recommended, and more fluids alone, or
loperamide, or bismuth subsalicylate may be enough. For moderate, antibiotics may
be used -- a weak recommendation. For severe, antibiotics should be used -- a
strong one. The abstract's "most moderate-to-severe cases" folds the last two
together; the graded list does not. What is deliberately absent is everything after
that -- which drug for whom, how much, for how long, what changes in pregnancy or
for a child. Those are prescriptions, and nothing here is one.

One last thing that is easy to miss. This is an international expert-panel
guideline published in a travel-medicine journal. It is not Korean law, Korean
guidance, or a Korean prescribing framework, and whether the drugs it names need
a prescription in Korea is not something this entry has sourced. Someone deciding
what to actually carry in a wash bag needs the Korean route, which has its own
entry here.
