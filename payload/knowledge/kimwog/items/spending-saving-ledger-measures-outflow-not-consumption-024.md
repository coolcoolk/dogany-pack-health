---
id: spending-saving/ledger-measures-outflow-not-consumption-024
domain: spending-saving
grade: C (deterministic instrument facts, census-verified on one instance ledger)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: no
sources:
  - "instrument-schema: kit_life spend_entry, which has no participant column and no share or split column, while the same database links people to calendar events through a persons table and an event-persons join; spend_entry.amount, documented in the schema as permitting negative values for refunds and cancellations; and the absence of any audit table covering spend_entry."
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Negative-amount rows: 0. Zero-amount rows: 0. Payment-instrument vocabulary: 8 entries, two credit cards, one debit card, five accounts or wallets, and no cash instrument."
  - "source:spending-saving/self-report-spending-error-not-uniform-002 -- the general finding that measurement error in this domain is not a uniform downward shift but varies by category. The shared-payment error described here is one concrete mechanism with exactly that property."
  - "source:spending-saving/declared-vs-applied-scheme-check-021 -- the measured consequence in this ledger: the category naming spending connected to other people holds 2 rows, because the instrument cannot record the thing the category names."
refraction_notes:
  - note: >
      THE MAGNITUDE IS NOT MEASURED, ONLY THE DIRECTION AND THE CONCENTRATION.
      How much of a typical household's spending is shared, reimbursed or paid
      by someone else is not measured here and no measurement of it was located
      in the evidence lane either. What is established is that the instrument
      cannot represent it and that the resulting error is concentrated in
      particular categories rather than spread evenly.
    grade: C
  - note: >
      THE PAIRED-ROW RULE IS DETERMINISTIC, NOT A PREFERENCE. Editing a past row
      changes a figure that may already have been reported, and with no audit
      table on this table the old value is unrecoverable and the change is
      invisible. A paired offsetting row leaves both the original and the
      correction inspectable. This follows from the instrument's structure and
      needs no outcome evidence.
    grade: C
claim: >
  A single-entry ledger records WHO PAID, not who consumed, and in the places
  where those diverge it does not approximate consumption -- it measures a
  different quantity. Three deterministic facts about the instance instrument.
  (1) There is no participant column and no share or split column on a spending
  row, although the same database links people to calendar events through a
  persons table and a join table, so the modelling capability exists and is
  simply not applied to spending. (2) The payment-instrument vocabulary holds 8
  entries, all cards or accounts, with no cash instrument, so a bill settled by
  somebody else produces no row at all rather than an unattributed one. (3) The
  amount column is documented as permitting negative values for refunds and
  cancellations, and 0 of 1603 rows are negative, so in this ledger no
  reimbursement has ever been recorded in the shape the schema provides for it.
  The two resulting errors run in opposite directions and DO NOT CANCEL. Paying
  for a group records the full amount as the payer's consumption, overstating
  it. Being paid for records nothing, understating it. Both are correct
  statements of outflow. Both are concentrated in the same categories -- meals,
  travel, gifts, occasions -- which are precisely the categories a spending
  review is most likely to discuss, so the error is largest exactly where the
  conversation goes. The operating rules follow. Report such a category as
  outflow through the connected instruments rather than as consumption, and say
  so rather than adding it as a footnote if challenged. And record a
  reimbursement as a paired offsetting row, never by editing the original
  amount down: the instrument permits the negative row, has no audit trail, and
  an edited row silently changes a month that may already have been reported.
reasoning: >
  It is easy to treat shared payments as noise that averages out, and the
  structure of the instrument shows why that is wrong. The two errors have
  opposite signs but they are not independent draws -- they cluster in the same
  categories and around the same kinds of occasion, so within any category the
  net is whatever the person's role in those occasions happened to be, not zero.
  A household where one person habitually settles the group bill has a food
  category that overstates their consumption systematically; the reverse case
  understates it just as systematically; and neither is visible in the row,
  because the row has no place to put it. The cleanest way to state what is
  actually being measured is to stop calling it consumption. The ledger sees
  money leaving the connected instruments. Who ate the meal is not in it. That
  reframing is not a hedge, it is the accurate description, and it is what makes
  the number usable rather than merely caveated: outflow is a real quantity, it
  is what budgets and cash flow are actually about, and it does not need
  defending the way a consumption claim does. The reimbursement rule is separate
  and stands on its own. With no audit trail on this table, editing a past row
  destroys the previous value and leaves no record that it changed, so any
  figure already given to the user for that month becomes irreproducible and
  quietly wrong. A paired negative row keeps both facts inspectable and is the
  shape the schema was written for. Graded at the observational band because the
  structural claims are certain for this instrument while the magnitude of
  shared and reimbursed spending in a household is not measured here and was not
  located in the evidence lane.
---

# spending-saving/ledger-measures-outflow-not-consumption-024

A spending row in this ledger has a date, an amount, a payee, a category and a
payment instrument. It has no field for who else was there, and no field for
what share was the payer's. The same database does link people to calendar
events, through a persons table and a join table, so this is not a limitation of
the technology. Spending simply was not modelled that way.

That single absence produces two errors running in opposite directions, and
they do not cancel:

- Pay for a group and the full amount lands as the payer's spending. Their
  consumption is overstated.
- Be paid for and nothing lands at all. Their consumption is understated, and
  there is not even an unattributed row to notice, because the payment
  instrument vocabulary here holds eight cards and accounts and no cash.

Both are perfectly correct statements about money leaving the connected
instruments. Neither is a statement about consumption.

The reason they do not average out is that they are not independent. They
cluster in the same categories -- meals, travel, gifts, occasions -- and around
the same kinds of event. A person who habitually settles the group bill has a
food category that overstates them month after month. A person usually treated
has one that understates them month after month. In both cases the error is
largest in the categories a spending review is most likely to open with.

The repair is not a correction factor, because no factor is measurable from
inside the ledger. It is to say what the number is. The ledger measures outflow
through the connected instruments. That is a real, useful quantity -- it is
what cash flow and budgets are actually about -- and stating it that way is more
accurate than stating a consumption figure and defending it afterwards.

Reimbursements are a separate rule and a firmer one. The amount column is
documented as accepting negative values for refunds and cancellations, and in
this ledger 0 of 1603 rows are negative, so the facility exists and has never
been used. When money comes back, record it as a paired offsetting row. Do not
edit the original amount down. There is no audit trail on this table: an edited
row destroys its previous value, leaves no record that it changed, and silently
alters a month that may already have been reported to the user. A paired row
leaves both the original outflow and the return visible and reproducible.

Limit worth stating: how much of a household's spending is actually shared,
reimbursed, or paid by someone else is not measured here, and no measurement of
it was located in the evidence lane either. What is established is that the
instrument cannot represent it, and that where it happens the error concentrates
rather than spreads.
