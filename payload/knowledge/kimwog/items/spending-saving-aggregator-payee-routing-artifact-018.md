---
id: spending-saving/aggregator-payee-routing-artifact-018
domain: spending-saving
grade: C (census of one instance ledger)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: no
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Payee-string frequencies and per-payee category distributions computed from the name and category_id columns."
  - "source:spending-saving/category-classification-malleable-004 -- the behavioural mechanism this item is deliberately distinguished from. That item is about a person moving an ambiguous expense to the account with room; this one is about a machine assigning an opaque payee to one category once, with no choice involved."
refraction_notes:
  - note: >
      ONE LEDGER, NOT A SAMPLE. The concentration figures are properties of this
      ledger and of the retail market it sits in. The mechanism -- a payee string
      that names a payment channel rather than a purchase, mapped once to one
      category and never revisited -- is general to any feed-derived ledger.
    grade: C
  - note: >
      THE DIAGNOSTIC IS THE TRANSFERABLE PART, NOT THE NUMBER. What travels is
      the check: compute each category total's concentration on its single
      largest payee string, and ask whether that string names a merchant or a
      channel. The threshold at which concentration becomes disqualifying is not
      measured and is not proposed here.
    grade: D
claim: >
  In a feed-derived ledger the payee string is often the name of a payment
  channel rather than of a purchase, and when that string is mapped to a
  category the resulting category boundary is an artefact of routing rather than
  a fact about consumption. Measured on the instance ledger: a single
  general-purpose retail payment wallet accounts for 216 rows, 13.5 percent of
  the whole ledger, and 216 of 216 sit in ONE category -- 62.6 percent of that
  category's 345 rows. A sibling platform name from the same operator, its food
  delivery service, accounts for 163 rows, 100 percent of them in a DIFFERENT
  category, 28.0 percent of that category's 583 rows. Together the two strings
  carry 379 rows, 23.6 percent of the ledger. The operator behind the first
  string sells groceries, household goods, books and electronics through one
  checkout, so the wallet name carries no information about what was bought.
  The consequence is exact: the boundary between the ledger's two largest
  categories is set by WHICH PLATFORM PRODUCT the payment passed through, not by
  the contents of the purchase, for roughly a quarter of all rows. A further
  class of payee strings is worse -- payment gateway and card-acquirer company
  names, which identify neither the merchant nor the category, and which are
  the only payee strings in this ledger that appear under more than one
  category. The operating rule: before reporting any per-category figure,
  compute what share of that category is carried by its single largest payee
  string, and check whether that string names a merchant or a channel. Where it
  names a channel, the category is a routing artefact and must be reported as
  one.
reasoning: >
  The evidence lane already carries a category-instability finding, and it is
  important that this item is not read as a second helping of it. That finding
  is behavioural: a person facing an expense that could honestly belong to two
  categories files it wherever there is still room, and the repair is to fix the
  categories before the expense is met. Nothing of that kind is happening here.
  Nobody chose. An importer mapped an opaque string to a category once, and 216
  identical strings inherited the mapping. The behavioural item predicts that
  ambiguous expenses drift toward the category with slack; this one predicts
  that a large block of rows sits rigidly in one category regardless of content.
  Those are opposite dynamics with opposite symptoms, and an agent that
  attributes a routing artefact to mental accounting will look for the drift in
  the wrong place and will propose the wrong repair -- fixing categories in
  advance does nothing about a wallet name. Graded at the observational band and
  no higher: this is a census of one instrument in one retail market, and while
  aggregator checkouts and payment intermediaries are not specific to that
  market, no measurement of how common the pattern is elsewhere was made or
  located. The concentration diagnostic itself is a proposal, not a validated
  procedure; it is cheap, it runs on data already held, and its output is a
  reason to hedge a number rather than a correction to apply to it.
---

# spending-saving/aggregator-payee-routing-artifact-018

A per-category total is only as meaningful as the payee strings underneath it.
In a ledger built from card and bank feeds, a large share of those strings name
the way the money moved rather than the thing that was bought.

Measured on the instance ledger, one year, 1603 rows. One string -- the general
checkout wallet of a large retail platform -- appears 216 times, 13.5 percent
of everything in the ledger, and all 216 rows sit in a single category, where
they make up 62.6 percent of its 345 rows. The same operator's food delivery
service appears under a separate string, 163 times, all 163 in a different
category, 28.0 percent of that category's 583 rows. Between them the two
strings carry 379 rows: just under a quarter of the ledger.

The retailer behind the first string sells groceries, cleaning supplies,
electronics, books and clothing through one checkout. The wallet name says
nothing about which of those was purchased. So the split between the two
largest categories in this ledger is not a measurement of how the household
divides its spending between food and household goods. It is a record of which
of the platform's two products the payment went through. Order groceries
through the main site and it lands in one category; order a meal through the
delivery app and it lands in the other. That is a routing fact wearing the
clothes of a consumption fact.

There is a worse class of string in the same ledger: payment gateway and
card-acquirer company names. These identify neither the merchant nor the
purchase, only the intermediary that processed the charge. They are also, in
this ledger, the only payee strings that appear under more than one category at
all -- exactly two strings, twelve rows -- which is telling in itself. The
strings nobody can interpret are the strings whose classification wanders.

Note what this is NOT. The evidence lane carries a real finding that people
move ambiguous expenses to whichever category still has room, and that setting
categories in advance removes the flexibility. That finding describes a person
making a choice. Nothing here involves a choice. An import mapped one string to
one category once, and every subsequent row with that string inherited it. The
two mechanisms produce opposite symptoms -- one makes a boundary drift, the
other makes it rigid and wrong -- and the repair for one does nothing for the
other. Fixing categories in advance has no effect on a wallet name.

The check to run before quoting any category number is short and uses data
already in hand: for each category, what fraction of its rows come from its
single largest payee string, and does that string name a merchant or a channel?
When the answer is a channel, the number is a routing artefact. Say so when
reporting it, rather than reporting a clean figure and adding the caveat if
asked.

Two honest limits. This is one ledger in one retail market, so the
concentration figures are its own; what travels is the mechanism and the check.
And no threshold is proposed at which concentration becomes disqualifying,
because none was measured -- the output of the check is a reason to hedge a
number, not a correction to apply to it.
