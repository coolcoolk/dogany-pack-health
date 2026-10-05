---
# Collection sprint 2026-09-02, cat-domain opening. The provenance row for the
# single most-repeated number in cat keeping: one litter box per cat plus one.
# The number is real advice from real clinicians in a peer-reviewed journal, and
# the same article says where it comes from -- twenty years of referral practice,
# not a study. That is worth having explicitly, because "n+1" is quoted with the
# confidence of a measured result and an agent that repeats it should know which
# kind of thing it is.
# Rubric: cat @companion-ethology (VC-C).
id: cat/litter-provisioning-evidence-012
domain: cat
grade: C (that the n+1 recommendation is published clinical-practice advice whose own source describes it as experience-based, and that no overall covered-versus-uncovered preference was detected in the one controlled test); D (that n+1 produces any measured outcome, and any other litter-box specification)
lane: "@companion-ethology"
locale: universal
as_of: 2013-2018
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/30375948/"  # Halls V. 2018, J Feline Med Surg 20(11):1005-1014, doi 10.1177/1098612X18806757, PMCID PMC11343342 -- states the n+1 formula ("one per cat plus one extra located out of sight of each other") and attributes its good outcomes to the author's referral-practice experience rather than to research
  - "https://pubmed.ncbi.nlm.nih.gov/23103684/"  # Grigg EK, Pick L, Nibblett B. 2013, J Feline Med Surg 15(4):280-284, doi 10.1177/1098612X12465606 -- 28 cats offered simultaneous covered and uncovered boxes; no significant overall preference; 8 cats showed individual preferences, four for each type
  - "https://pubmed.ncbi.nlm.nih.gov/24966283/"  # Carney HC, Sadek TP, Curtis TM, Halls V, Heath S, Hutchison P, Mundschenk K, Westropp JL. 2014, J Feline Med Surg 16(7):579-598, doi 10.1177/1098612X14539092 -- AAFP/ISFM house-soiling guidelines; states they use documented science where available and the authors' accumulated clinical experience where research is limited
  - "cat/curator-checklist-001"  # domain rule: a guideline recommendation is consensus until a specific study is named for it
  - "cat/urinary-obstruction-same-day-005"  # the medical-routing row that must fire BEFORE any litter-box provisioning advice
refraction_notes:
  - note: >
      THE PROVENANCE OF n+1, which is the point of this row. The formula -- one
      box per cat plus one extra, located out of sight of each other -- appears in
      a peer-reviewed JFMS behaviour review, and the same article reports that
      this approach achieves a consistently good outcome in the author's
      experience. That is an honest attribution of a clinical heuristic, and it is
      also the answer to "is there a study": there is not one cited, and the
      article does not claim one. The number is good practice from experienced
      clinicians. It is not a measurement.
    grade: C
  - note: >
      THE PROFESSIONAL BODIES SAY THE SAME THING ABOUT THEMSELVES. The AAFP and
      ISFM house-soiling guidelines state that they draw on scientifically
      documented information where it is available and on the authors' accumulated
      clinical experience where research is limited. So the honest description of
      the whole litter-box advice corpus is: a consensus built by people who have
      seen a great many cases, with thin measurement underneath it.
    grade: C
  - note: >
      THE ONE CONTROLLED TEST THAT EXISTS FOUND NOTHING AT THE GROUP LEVEL. Grigg,
      Pick and Nibblett 2013 gave 28 cats simultaneous access to covered and
      uncovered boxes and measured daily waste. There was no significant overall
      preference. Eight of the 28 showed an individual preference, split four and
      four. The authors suggest that if boxes are cleaned at least once daily most
      cats will not prefer either type, and recommend offering both to identify a
      particular cat's preference. That is the same shape as the water-bowl result
      at cat/water-bowl-type-null-003: no group effect, real individual variation,
      and the actionable move is observation rather than a rule.
    grade: C
  - note: >
      THE CLEANLINESS CONDITION IS DOING WORK IN THAT RESULT and should not be
      dropped. The 2013 finding is conditional on daily cleaning -- that is the
      authors' own framing of why no preference emerged. A covered-versus-uncovered
      null under daily cleaning is not a statement about a box that is cleaned
      weekly, and nothing here tests cleaning frequency itself.
    grade: D
  - note: >
      THE ORDER OF OPERATIONS MATTERS MORE THAN THE PROVISIONING ADVICE. A cat
      that stops using its box is a clinical question before it is a furniture
      question -- see cat/urinary-obstruction-same-day-005, where the severity
      numbers are, and note that the feline professional bodies published their
      house-soiling document as a resource for veterinarians. Adding a litter box
      to a cat that has a urinary problem is a delay, not an intervention. Any
      provisioning advice must fire AFTER the medical routing, never instead of it.
    grade: C
  - note: >
      NOT ESTABLISHED BY ANY SOURCE HERE, and all of it circulates confidently:
      box size, litter substrate and depth, liner use, cleaning frequency, box
      placement relative to food and water, and whether the n+1 count should
      include boxes on different floors. A targeted search in this sprint located
      no controlled feline test of any of them that could be cited. The one
      published test of one variable found nothing at the group level. Treat every
      other specification as clinical practice at best.
    grade: D
claim: >
  The n+1 litter box rule is published clinical-practice advice and its own source
  says so. Halls (2018, JFMS) states the formula -- one box per cat plus one extra,
  located out of sight of each other -- and attributes its consistently good
  outcomes to the author's referral-practice experience rather than to research; no
  study is cited for it and none is claimed. The AAFP/ISFM house-soiling
  guidelines (Carney et al., 2014, JFMS) describe themselves the same way: documented
  science where available, the authors' accumulated clinical experience where
  research is limited. The one controlled test of a litter-box variable found
  nothing at the group level: Grigg, Pick and Nibblett (2013, JFMS) offered 28 cats
  simultaneous covered and uncovered boxes and detected no significant overall
  preference, with 8 cats showing individual preferences split four and four; the
  authors note this holds where boxes are cleaned at least once daily, and
  recommend offering both types to identify a given cat's preference. ORDER OF
  OPERATIONS: a cat that stops using its box is a clinical question first -- adding
  a box to a cat with a urinary problem is a delay, not an intervention. NOT
  established by anything read here: box size, substrate, depth, liners, cleaning
  frequency, placement relative to food and water, or whether boxes on different
  floors count.
reasoning: >
  This row exists for its provenance rather than its content. The n+1 formula is
  probably the single most-repeated number in cat keeping and it is quoted with
  the confidence of a measured result, so knowing which kind of claim it is
  changes how an agent should speak it. The answer turns out to be unusually clean:
  the peer-reviewed article that states the formula also states where it comes
  from, which is twenty years of clinical referral work, and the professional
  bodies' house-soiling guidelines describe their own evidence base the same way.
  That is honest authorship and it is exactly the situation the domain checklist
  was written for -- consensus by default, elevated only when a study is named.
  Nothing here argues against the advice; experienced clinicians converging on a
  heuristic is worth something, and it is being reported as what it is. The single
  controlled test of a litter-box variable is included because its result rhymes
  with the water-bowl finding in a way that looks like a pattern in this domain:
  no group-level effect, real variation between individuals, and the useful move
  being observation of the particular animal rather than a universal rule. Its
  daily-cleaning condition is preserved because dropping it would turn a
  conditional null into an unconditional one. The order-of-operations note is the
  most consequential line in the row and is placed accordingly: provisioning
  advice given to a cat with a medical problem is a delay dressed as help, and the
  routing row that must fire first is cross-referenced directly. Everything else
  in the litter-box advice corpus is refused for the simplest reason available --
  a targeted search found no controlled feline test of any of it.
---

# cat/litter-provisioning-evidence-012

One litter box per cat, plus one spare, out of sight of each other. It is
probably the most-repeated number in cat keeping, and it is worth knowing what
kind of claim it is.

It comes from a peer-reviewed behaviour review in a veterinary journal, which
also says where it comes from: twenty years of referral practice, in which that
arrangement consistently produced good outcomes. No study is cited for it and the
article does not claim one. The feline professional bodies describe their own
house-soiling guidance the same way -- documented science where it exists, and
accumulated clinical experience where it does not.

That is honest authorship, and it is not an argument against the advice.
Experienced clinicians converging on a heuristic is worth something. It is just a
different kind of thing from a result, and an agent repeating it should know
which one it is holding.

The one variable anyone has actually tested came back empty at the group level.
Twenty-eight cats were given covered and uncovered boxes at the same time. No
overall preference. Eight of them had an individual preference, evenly split
between the two types. The authors' reading is that where boxes are cleaned at
least once a day, most cats will not care, and that the useful move is to offer
both and see what this cat does. That is the same shape as the water-bowl result
elsewhere in this domain: nothing at the group level, real variation between
individuals, and observation beating any rule.

Keep the cleaning condition attached to that finding. It is the authors' own
explanation for why no preference showed up, and a null under daily cleaning says
nothing about a box that gets cleaned once a week.

The most important thing in this row is not about boxes at all. A cat that stops
using its box is a medical question before it is a furniture question. The
severity numbers live elsewhere in this domain, and the professional bodies
published their house-soiling document for veterinarians. Adding a litter box to
a cat with a urinary problem is a delay wearing the costume of an intervention.
Provisioning advice comes after the medical routing, never instead of it.

Everything else that circulates -- box size, what litter, how deep, liners, how
often to clean, how far from the food, whether a box upstairs counts -- has no
controlled feline test behind it that could be found. The one thing anyone tested
found nothing.
