---
id: spending-saving/stored-value-load-is-not-consumption-019
domain: spending-saving
grade: C (census of one instance ledger, on top of a deterministic accounting identity)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: no
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Per-payee row counts and amount distributions computed from the name, amount, date and category_id columns."
  - "identity: a load into a stored-value instrument moves money between two holdings of the same owner. It is a transfer, not an expense, and the expense occurs later at an amount and date the loading record does not contain. This half of the item is deterministic and does not rest on the measurement."
  - "source:spending-saving/diary-attrition-zero-reporting-003 -- the coverage discipline this item extends. A load-dominated category can have perfect coverage and still be a record of loading rather than of spending."
refraction_notes:
  - note: >
      TWO HALVES WITH DIFFERENT STANDING. That a load is not a purchase is an
      accounting identity and needs no evidence. That 78 percent of one
      category's rows are loads is a measurement of one ledger and is offered
      only as a demonstration that the identity has large practical consequences
      in a real artefact.
    grade: C
  - note: >
      THE ERROR HAS A DIRECTION AND IT IS NOT SYMMETRIC. Over a long enough
      window loads and consumption converge in TOTAL, because money loaded is
      eventually spent. They never converge in COUNT, in DATE, or in
      per-transaction AMOUNT. So a period total over a full year may be roughly
      right while every per-day, per-trip and per-event figure derived from the
      same rows is wrong. An agent that validates the annual total and then
      trusts the daily series has checked the one thing that was not broken.
    grade: C
claim: >
  A load into a stored-value instrument is a transfer between two holdings of
  the same person, not an act of consumption, and a ledger that records it as an
  expense misstates the count, the date and the amount of the spending it stands
  for. Measured on the instance ledger: 108 of the 138 rows in the transport
  category -- 78.3 percent -- carry the name of the transit-card operator or of
  its prepaid load product, and 59 of those 108 sit at exactly two round
  denominations, which are load sizes rather than fares. The remaining rows in
  that category are individually plausible travel events. Two further rows
  elsewhere in the ledger are wallet top-ups filed in the catch-all category.
  The consequences are separable and all three are wrong in different ways.
  COUNT: the category holds roughly four times fewer travel events than its row
  count suggests, because one load covers many journeys. DATE: each row is
  dated when the instrument was funded, not when the travel happened, so the
  spending is displaced backwards by an unknown and variable lag. AMOUNT: the
  values are denominations chosen by the payer, so the series is quantised into
  round steps and carries no information about fare levels. Nothing downstream
  repairs this, because the instrument never reports the consumption side back
  to the ledger at all. The operating rule: identify load-type payees at
  classification time and mark them as funding rather than consumption; never
  derive a per-event, per-day or per-trip figure from a category whose rows are
  loads; and when reporting such a category, say that it measures funding.
reasoning: >
  The identity half of this needs no defence and is stated first for that
  reason: money moved from a bank account into a transit card or a payment
  wallet has not been spent, it has been relocated, and the purchase it will
  eventually pay for has its own date and its own amount which the loading row
  does not contain. The measurement half exists to show that this is not a
  pedantic distinction but the dominant fact about one of the ledger's
  categories. Nearly four in five rows in the transport category are loads or
  operator settlements, and more than half of those sit at two round values,
  which is the signature of a payer choosing a top-up size rather than a fare
  being charged. A monthly transport figure computed from these rows is a record
  of when the card was funded. It will show a spike in a month with two top-ups
  and a trough in a month with none, and neither will correspond to travelling
  more or less. This item is filed as craft rather than as evidence because
  nothing here is a research finding: it is an identity plus a census. It is
  graded at the observational band because the load share is a property of one
  ledger in one transit market, and because the four-fold count inflation is an
  approximation from row structure rather than a validated ratio -- the actual
  number of journeys is not recoverable from this ledger at all, which is the
  point. What should not be softened is the direction: this error cannot be
  corrected after the fact from the ledger's own contents, only avoided at
  classification time or disclosed at reporting time.
---

# spending-saving/stored-value-load-is-not-consumption-019

Putting money onto a transit card is not spending it. The money has moved from
one place you own to another place you own. The spending happens later, in
amounts and on dates that the loading record does not contain and never will.

This matters more than it sounds, because in a feed-derived ledger the load is
the only event the feed can see. The card charges the bank when it is funded.
Every journey afterwards is invisible.

Measured on the instance ledger, one year. The transport category holds 138
rows. 108 of them -- 78.3 percent -- carry the name of the transit-card
operator or of its prepaid loading product. Of those 108, 59 sit at exactly two
round denominations. Those are top-up sizes, not fares. The thirty or so
remaining rows in the category look like individual travel events: an
intercity coach, a taxi, a rail ticket, a car share. Two more top-up rows, for
payment wallets rather than transit, sit in the catch-all category.

So three separate things are wrong with any number computed from that category,
and they are wrong in different directions:

- The COUNT is inflated. One load stands for many journeys, so the category
  contains roughly four times fewer travel events than it contains rows. How
  many fewer is not recoverable from this ledger at all.
- The DATE is displaced. Each row is dated when the card was funded. The travel
  it paid for happened afterwards, over a stretch of days that the ledger
  cannot see, and the lag varies with how heavily the card was used.
- The AMOUNT is quantised. The values are denominations the payer chose, so the
  series steps in round increments and says nothing about what any journey cost.

A monthly transport figure built on this is a record of top-up timing. A month
with two loads reads as a heavy travel month; a month that ran down an existing
balance reads as a light one. Neither has anything to do with how much the
person travelled.

There is one thing that does survive. Over a long enough window, money loaded
is money eventually spent, so an annual total is approximately right. Every
finer cut of the same rows is not. That asymmetry is a trap: an agent that
sanity-checks the annual figure, finds it plausible, and then trusts the daily
or per-trip series has verified the only quantity that was not broken.

Nothing downstream fixes this, because the stored-value instrument never
reports the consumption side back. The repair has to happen at one of two
moments. At classification time, mark load-type payees as funding rather than
consumption and keep them out of consumption totals. At reporting time, if that
was not done, say what the category actually measures. What is not available is
a correction computed afterwards from the ledger's own contents.
