---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# A DELIBERATE GATE ROW, same species as
# relationships-communication/contact-cadence-no-evidence-014. It ships no
# altitude number at all, because the full text of the current guideline could
# not be retrieved in this pass and the numbers that circulate are exactly the
# kind a model will supply from parametric memory with no edition attached. What
# it does ship is which document is authoritative, what edition is current, and
# an explicit instruction not to generate the rest.
# Source re-audit 2026-10-06: still a gate row, deliberately unchanged in
# content. The guideline's full text was re-attempted and refused again: the
# SAGE record (doi redirect) and the WEM site return 403 to both curl and
# WebFetch, ScienceDirect returns 403, and Europe PMC lists it as subscription
# required and not in PMC. The PubMed record was re-read and matches every
# statement here (2010 / 2014 / 2019 chain, ACCP grading, COVID-19 addition);
# no later WMS altitude edition was located. A search-result snippet quoting an
# ascent rate and a 'strong recommendation, moderate-quality evidence' label was
# seen and NOT taken: it is a retelling, not the text.
id: travel/altitude-edition-gate-010
domain: travel
lane: "@travel-clinical"
grade: B (which document is the current authoritative guideline, what it covers and how it grades); D (any ascent rate, altitude threshold or risk category -- none is shipped)
locale: universal
as_of: 2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/37833187/"  # Luks AM, Beidleman BA, Freer L, Grissom CK, Keyes LE, McIntosh SE, Rodway GW, Schoene RB, Zafren K, Hackett PH. 2024, Wilderness Environ Med 35(1_suppl):2S-19S, doi 10.1016/j.wem.2023.05.013. Abstract read verbatim 2026-09-02. FULL TEXT NOT RETRIEVED -- see the refraction note; no recommendation content is quoted anywhere in this item
  - "https://pubmed.ncbi.nlm.nih.gov/31248818/"  # Luks AM, Auerbach PS, Freer L, Grissom CK, Keyes LE, McIntosh SE, Rodway GW, Schoene RB, Zafren K, Hackett PH. 2019, Wilderness Environ Med 30(4S):S3-S18, doi 10.1016/j.wem.2019.04.006 -- the SUPERSEDED 2019 edition, recorded so that a later pass meeting it in a citation recognises it as stale rather than current
  - "source:finance-investing/kr-tax-regime-staleness-gate-016 -- the same gate pattern: name the current edition, refuse the remembered number"
  - "source:relationships-communication/contact-cadence-no-evidence-014 -- the warehouse's precedent for shipping a row whose content is a refusal"
  - "framework:ACCP grading -- the guideline states that its recommendations are graded on the quality of supporting evidence AND the balance between benefits and risks or burdens, according to criteria put forward by the American College of Chest Physicians. That is a THIRD grading ladder in this warehouse, alongside GRADE and the older AASM Standard/Guideline/Option scheme. Its labels are not interchangeable with either."
refraction_notes:
  - note: >
      THE CURRENT DOCUMENT AND ITS SUPERSESSION CHAIN. The authoritative clinical
      practice guideline for acute mountain sickness, high altitude cerebral oedema
      and high altitude pulmonary oedema is the Wilderness Medical Society's 2024
      Update (Wilderness Environ Med 35(1_suppl):2S-19S). Its own abstract records
      the chain: original consensus guidelines 2010, practice guidelines 2014, an
      update in 2019, and this 2024 update. So a citation to the 2019 edition --
      which is what a search will most often surface -- is a citation to a
      superseded document. The 2024 edition also adds recommendations on high
      altitude travel following COVID-19 infection, which by definition none of its
      predecessors contain.
    grade: B
  - note: >
      NO NUMBER IS SHIPPED, AND THAT IS THE POINT OF THE ROW. The guideline's full
      text was not retrievable in this pass: the publisher's page and the society's
      own summary both refused retrieval. Therefore NOTHING about ascent rates,
      sleeping-elevation limits, altitude thresholds, rest-day intervals or risk
      categories appears anywhere in this item. Secondary summaries of those figures
      were encountered during the search and were deliberately not taken, on the
      same rule this warehouse applied to the oyster seasonal-incidence multiplier:
      a figure that lives only in retellings does not ship.
    grade: A
  - note: >
      WHY THIS PARTICULAR ABSENCE NEEDED A ROW RATHER THAN SILENCE. Altitude advice
      is unusually easy to produce from parametric memory. Ascent-rate rules of
      thumb are widely circulated, they sound precise, they have changed across
      editions, and a model asked about them will almost certainly generate one with
      no edition attached and no way for the user to know which edition it came
      from. A silent gap invites exactly that. A row that says "the current document
      is the 2024 update, this warehouse holds none of its numbers, go and read it"
      is a forcing point; an empty domain is not.
    grade: A
  - note: >
      A THIRD GRADING LADDER, WHICH IS ITS OWN HAZARD. This guideline grades on
      American College of Chest Physicians criteria. This warehouse already carries
      documents graded on GRADE (STRONG / WEAK, with certainty stated separately)
      and on the older AASM ladder (Standard / Guideline / Option). Three ladders
      now appear across the lanes, and their labels do not translate. Any future
      pass that ships an altitude recommendation must carry its ACCP label as issued
      rather than paraphrase it into one of the other two vocabularies.
    grade: A
  - note: >
      RELEVANCE TO A KOREAN USER, STATED HONESTLY SO THE PRIORITY IS CLEAR. Nothing
      in Korea reaches an altitude where this guideline's subject matter arises;
      the exposure comes entirely from outbound travel -- Nepal, Tibet, the Andes,
      parts of western China, and high-altitude airports reached directly by air,
      which is the itinerary shape most likely to matter because it removes the
      gradual part of any ascent. This is a real but occasional need, which is why
      it is a gate row in the opening sprint rather than a full item, and why
      closing it properly is recorded as a want rather than as a defect.
    grade: C
  - note: >
      WHAT WOULD CLOSE THIS. A read of the 2024 guideline's own text for two things
      specifically: the risk-stratification categories, and the graded ascent
      recommendation with its ACCP strength and evidence-quality labels attached.
      Those two would make a real item. Anything short of reading them produces a
      plausible item, which in this domain is worse than none.
    grade: D
claim: >
  The authoritative clinical practice guideline for acute altitude illness -- acute
  mountain sickness, high altitude cerebral oedema and high altitude pulmonary
  oedema -- is the Wilderness Medical Society's 2024 Update (Wilderness Environ Med
  35(1_suppl):2S-19S). Its own abstract records that it supersedes the society's
  original consensus guidelines of 2010 and the subsequently updated practice
  guidelines of 2014 and 2019, and that it adds recommendations on high altitude
  travel following COVID-19 infection. It grades its recommendations on both the
  quality of supporting evidence and the balance between benefits and risks or
  burdens, according to criteria put forward by the American College of Chest
  Physicians -- a different ladder from the GRADE and AASM schemes used elsewhere
  in this warehouse, whose labels do not translate. THIS WAREHOUSE HOLDS NONE OF
  THAT GUIDELINE'S CONTENT. Its full text was not retrievable in this pass, so no
  ascent rate, sleeping-elevation limit, altitude threshold, rest-day interval or
  risk category is recorded here, and none should be produced from memory. The
  correct response to an altitude question is to read the current edition, not to
  recall a number.
reasoning: >
  This row exists because of a specific and predictable failure, not because the
  domain is unimportant. Altitude guidance consists largely of numbers -- metres
  per day, sleeping elevation, thresholds at which risk begins -- that are widely
  circulated, sound authoritative, have moved across four editions of the same
  guideline, and are exactly what a language model will supply on request without
  any edition attached. An empty spot in the warehouse does not prevent that; it
  invites it, because the answer-path then falls back on parametric memory with
  nothing to check it against. A row that names the current document and explicitly
  refuses its contents is a forcing point, and this warehouse has shipped that
  shape before, most directly in the relationships domain's deliberate absence row
  on contact cadence. What can be established here was established from the
  PubMed record read verbatim: which body owns the guideline, what conditions it
  covers, that the 2024 edition supersedes 2010, 2014 and 2019, and that it grades
  on ACCP criteria. That is a real and useful piece of knowledge on its own,
  because the 2019 edition is what a casual search most often returns and it is
  now stale. The grading-ladder observation earns its place too: with this
  document the warehouse now spans three incompatible recommendation vocabularies,
  and a later pass that paraphrases an ACCP-graded recommendation into GRADE
  language would be committing the same collapse this warehouse polices elsewhere.
  What is deliberately not here is any figure. Secondary summaries carrying ascent
  rates and risk categories were encountered while searching for the full text and
  were not taken, on the standing rule that a number living only in retellings does
  not ship. Reading the guideline itself would produce a genuinely good item, and
  that is recorded as a want rather than quietly filled with something plausible.
---

# travel/altitude-edition-gate-010

This warehouse does not hold altitude numbers. That is on purpose, and this entry
exists to say so out loud rather than leave a gap that gets filled from memory.

The authoritative document for acute mountain sickness, high altitude cerebral
oedema and high altitude pulmonary oedema is the Wilderness Medical Society's
clinical practice guideline, 2024 update. Its own abstract sets out the lineage:
consensus guidelines in 2010, practice guidelines in 2014, an update in 2019, and
this one. The 2024 edition also adds guidance on going to altitude after a
COVID-19 infection, which none of the earlier versions could contain.

That lineage is the practical part. A search for these guidelines will very often
surface the 2019 edition, and the 2019 edition is superseded.

The guideline grades its recommendations on the quality of the evidence and the
balance of benefits against risks and burdens, using American College of Chest
Physicians criteria. That is worth flagging because it is a third grading system
in this warehouse. Elsewhere there are documents graded on GRADE, where the words
are strong and weak and certainty is stated separately, and a sleep-medicine
document graded Standard / Guideline / Option. These vocabularies look similar and
mean different things, and translating between them silently is a mistake this
warehouse takes seriously.

Now the refusal.

The full text of the 2024 guideline could not be retrieved in this pass -- the
publisher's page and the society's own summary both declined. So this warehouse
holds none of its recommendations. There is no ascent rate here. No sleeping
elevation limit, no altitude at which anything is said to begin, no rest-day
interval, no risk categories. Summaries of those figures were encountered while
looking for the paper and were deliberately not taken, on the same rule this
warehouse applies to any number that exists only in retellings.

The reason this is a row rather than a silence is that altitude advice is unusually
easy to fabricate convincingly. The numbers are memorable, they sound precise,
they have shifted across four editions, and an assistant asked for one will produce
it without knowing which edition it came from. A gap invites that. A row saying
"the current document is the 2024 update and this warehouse holds none of its
contents" does not.

For a Korean traveller this is a real but occasional need. Nothing in Korea is high
enough for any of it; the exposure comes from trips to Nepal, Tibet, the Andes and
parts of western China -- and particularly from flying directly into a
high-altitude airport, which is the itinerary that removes whatever gradualness an
ascent would otherwise have had.

What would fix this properly is small and specific: read the 2024 guideline for
its risk-stratification categories and its graded ascent recommendation, and carry
both with their strength and evidence labels attached as issued. Until someone
does that, the honest answer to an altitude question is to go and read it.
