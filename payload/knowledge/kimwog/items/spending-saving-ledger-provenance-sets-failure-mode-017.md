---
id: spending-saving/ledger-provenance-sets-failure-mode-017
domain: spending-saving
grade: C (census of one instance ledger, plus a deterministic instrument fact)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: no
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Every count below is reproducible by re-running the stated aggregation."
  - "instrument-schema: kit_life spend_entry.source and spend_entry.method columns and the pay_method table, read at source in the same database."
  - "source:spending-saving/diary-attrition-zero-reporting-003 -- the diary failure mode this item bounds. That item establishes that diary instruments fail by producing zeros; this one establishes that the test it implies does not detect the failure mode of a feed-derived ledger."
  - "invitation: GAPS.md spending-saving section, v18 gap ANY MEASURED CONSEQUENCE OF LOG COMPLETENESS, which records that log-coverage decay may be measurable from the instance's own data rather than from literature."
refraction_notes:
  - note: >
      ONE LEDGER, NOT A SAMPLE. This is a census of a single personal ledger.
      The proportions are properties of that ledger and are not offered as
      population values. What transfers is the mechanism and the diagnostic,
      not the numbers.
    grade: C
  - note: >
      THE TWO PROVENANCES MIX IN PRACTICE. A real ledger is often part feed and
      part hand-entered. Coverage statistics are then dominated by whichever
      part is larger, so a mostly-feed ledger with a decaying hand-entered
      remainder will pass the coverage check while the hand-entered part rots.
      The provenance column has to be read per row, not per ledger.
    grade: C
claim: >
  A spending ledger has a provenance, and the provenance decides which failure
  mode it has. The instance ledger measured here is entirely feed-derived: all
  1603 rows carry the bulk-import provenance value and none carry the
  conversational one, and 1587 of 1603 rows resolve to a named payment
  instrument. The instrument vocabulary in the same database contains eight
  entries -- two credit cards, one debit card and five bank or wallet accounts
  -- and NO cash instrument at all. Coverage is 353 of the 366 days in the
  window, the 13 absent days are scattered singles and pairs with no clustering
  toward the end, and monthly entry counts show no downward trend across
  thirteen months. So the coverage-and-attrition diagnostic implied by
  spending-saving/diary-attrition-zero-reporting-003 returns a completely clean
  result on this ledger, AND the ledger is nonetheless blind to every purchase
  made off the payment rails, permanently and silently. The two failure modes
  are different in kind: a hand-kept diary loses rows through decaying
  recording effort, which coverage statistics detect; a feed-derived ledger
  loses whole PAYMENT CHANNELS, which coverage statistics cannot detect,
  because within the channels it does see the record is close to complete. The
  operating rule follows: establish provenance before running any completeness
  test, run attrition tests on hand-entered rows and scope tests on
  feed-derived ones, and never state a category or period total without naming
  the payment channels it covers.
reasoning: >
  The evidence lane's sharpest operational finding is that a diary degrades by
  producing zeros rather than smaller numbers, and the diagnostic it prescribes
  is to treat coverage as a first-class number: before saying a category fell,
  check whether entries fell. That diagnostic is correct and it is also
  insufficient, and the insufficiency is visible directly in the artefact the
  agent already holds. On this ledger the coverage numbers are close to ideal
  and the ledger still cannot see a single cash purchase, because no cash
  instrument exists in its instrument vocabulary and every row arrived through a
  card or account feed. Cash spending here is not under-reported; it is
  structurally unrepresented, and no amount of entry-count checking will surface
  it, because the missing rows never existed to decay. This is a craft item and
  not an evidence item because no study is being cited for the general claim:
  what is cited is a census of one instrument plus a fact about how that
  instrument is constructed. The honest scope is therefore narrow. What is
  solid is that these are two distinct failure modes with two distinct tests,
  that the test for one is blind to the other, and that provenance is recorded
  per row in the instrument and can be read before either test is chosen. What
  is not established is any rate: how much household outflow typically escapes
  a payment feed is not measured here and is not measured in the evidence lane
  either.
---

# spending-saving/ledger-provenance-sets-failure-mode-017

Before running any test on a spending ledger, find out where its rows came
from. The answer changes which test is worth running.

Two provenances produce two different objects. A ledger a person types into is
a diary, and the evidence lane already says precisely how a diary fails: not by
reporting smaller amounts but by reporting nothing, one quiet category at a
time, until a month of not-logging renders as a month of thrift. The
prescribed defence is to treat coverage as a number in its own right -- check
whether entries fell before concluding that spending fell.

A ledger assembled from card and bank feeds is a different instrument, and the
same defence does not protect it.

Measured on the instance ledger, one year, 1603 rows: every row carries the
bulk-import provenance value, 1587 of them resolve to a named payment
instrument, and the instrument list in the same database holds eight entries --
two credit cards, one debit card, five accounts or wallets. There is no cash
instrument in the list. Coverage is 353 days out of 366. The thirteen absent
days are scattered singles and one or two adjacent pairs, not a tail. Monthly
entry counts across thirteen months move within a normal band and trend
nowhere.

Run the coverage diagnostic on that and it reports excellent health. It is
right, and it is answering a question the ledger was never at risk on. Whatever
was paid for in cash is not a decayed row, a late row or a thin row. It is not
a row. It never entered the instrument, so there is nothing for a completeness
check to find missing.

That is the distinction worth carrying:

- A hand-entered ledger loses ROWS, gradually, as recording effort decays.
  Coverage statistics detect this, which is exactly what the diary finding
  tells you to watch.
- A feed-derived ledger loses CHANNELS, completely and from the first day.
  Coverage statistics cannot detect this, because inside the channels it does
  carry, the record is close to complete.

So the order of operations is: read the provenance first, then choose the test.
For hand-entered rows, watch entry counts and per-category quiet periods. For
feed-derived rows, inventory the instruments instead and ask what is missing
from the list -- cash, another person's card, an account that was never
connected, a payment app that does not export. Then say the total with its
boundary attached. "Spending in this category was X" is a claim the ledger
cannot support. "X went through these cards and accounts" is one it can.

Two limits, stated plainly. This is a census of one ledger, so the proportions
belong to that ledger and only the mechanism travels. And most real ledgers are
mixtures -- part feed, part typed -- in which case the coverage statistics are
dominated by the feed portion and will look healthy while the typed portion
decays underneath. The provenance column is per row. Read it per row.
