---
id: spending-saving/declared-vs-applied-scheme-check-021
domain: spending-saving
grade: C (census of one instance ledger, cross-checked against the same database's own declarations)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: no
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Per-category row counts, per-payee category distributions, and the is_fixed column tallied across all rows."
  - "instrument-schema: kit_life fixed_cost table in the same database, which declares 18 recurring commitments each with an explicit category assignment, compared row by row against the categories the matching ledger rows actually carry; and spend_entry, which has no participant column while the same database's event tables do link to a persons table."
  - "source:spending-saving/diary-attrition-zero-reporting-003 -- the rule this item operationalises for the per-category case. A quiet category is a hypothesis about recording before it is a conclusion about behaviour; here the hypothesis is testable without asking the user anything."
refraction_notes:
  - note: >
      ONE LEDGER, AND A SMALL NUMBER OF CHECKABLE PAIRS. Only the recurring
      commitments that are separately declared can be checked this way, which in
      this ledger is 18 declarations against 1603 rows. The check therefore
      proves that the scheme diverges from its own declaration; it does not
      measure how far, and it says nothing about one-off purchases.
    grade: C
  - note: >
      A MATCH DOES NOT CLEAR THE SCHEME. Agreement between a declaration and the
      applied category means only that the two agree. Both can be wrong together,
      and where no declaration exists there is nothing to compare against. This
      is a cheap falsifier, not an audit.
    grade: D
claim: >
  An unusually small category is a hypothesis about the classification scheme
  before it is a fact about the person, and in a ledger that also stores
  DECLARED categories the hypothesis can be tested without spending any of the
  user's attention. Measured on the instance ledger: the two smallest categories
  hold 2 rows each against 583 in the largest. The learning category's 2 rows are
  two different vendors' digital subscriptions. Meanwhile 15 rows for one
  vendor's assistant subscription sit in the hobby-and-content category -- while
  the same database's own declared-commitment table assigns that exact
  subscription to LEARNING. A second declaration, a retail membership fee, is
  declared against household goods while its 12 matching ledger rows sit under
  hobby-and-content. So the small category is not a measurement of how little
  the person spends on learning; it is the residue left after
  functionally identical purchases were routed elsewhere. A third signal points
  the same way: the instrument provides a fixed-cost flag on every row and 18
  recurring commitments are declared, yet 0 of 1603 rows carry the flag -- a
  declared distinction that the applied data does not implement anywhere. The
  smallest category is a different failure again: its 2 rows are two entries on
  a single date for one clothing retailer, and the instrument has no participant
  column at all, so spending WITH someone is structurally unrepresentable and
  necessarily sits inside the food and travel categories instead. The operating
  rule: when a category is conspicuously small, run the declared-versus-applied
  comparison before reporting the number or asking the user about it, and check
  whether the category names something the schema can actually record.
reasoning: >
  Faced with 2 rows in one category and 583 in another, an agent has two
  hypotheses and no obvious way to choose: the person genuinely does not spend
  there, or the category is one nobody files into. The evidence lane says which
  way to lean -- a quiet category is a hypothesis about recording before it is a
  conclusion about behaviour -- but does not say how to test it, because in a
  survey instrument there is nothing to test against. In a ledger that also
  carries declared recurring commitments there is. The declaration states where
  the household intends a given commitment to sit; the ledger states where its
  rows actually sit; disagreement is a scheme defect and is visible immediately.
  Here the disagreement is exactly on the item that would have populated the
  near-empty category. It is not a subtle case: an assistant subscription from
  one vendor was declared as learning and filed as hobby content, while a
  near-identical subscription from a competing vendor is one of the only two
  rows that reached learning at all. The same comparison catches a second
  mismatch and a third, coarser signal -- a fixed-cost flag that is declared 18
  times and set 0 times. The smallest category fails for a different and more
  structural reason worth separating: a category can only be populated if the
  instrument can record what it names, and this one names a relational fact
  about a purchase while the row model has no participant field, although the
  same database does link people to events. Graded at the observational band: it
  is one ledger and only the separately declared commitments are checkable, so
  the check proves divergence without measuring its extent. Its value is that it
  costs no user attention, which matters because the alternative -- asking the
  user why they never spend on learning -- both spends attention and asks a
  question premised on an artefact.
---

# spending-saving/declared-vs-applied-scheme-check-021

Two categories in this ledger hold 2 rows each. The largest holds 583. The
question is whether that is a fact about the person or a fact about the
categories, and it is answerable from data already in hand.

Take the learning category first. Its 2 rows are digital subscriptions from two
different vendors. Elsewhere in the ledger, 15 rows for one vendor's assistant
subscription sit under hobby and content. And in the same database, the
household's own declared recurring commitments assign that exact subscription to
LEARNING.

That is a direct contradiction between what the scheme says and what the scheme
does, on precisely the item that would have filled the empty category. A second
declared commitment, a retail membership, is declared against household goods
while its 12 matching rows sit under hobby and content. And there is a blunter
version of the same signal: every row has a fixed-cost flag available to it,
18 recurring commitments are declared, and 0 of 1603 rows have the flag set.
A distinction that exists in the declaration and nowhere in the data.

So the answer for that category is: not real. The number is the residue left
after functionally identical purchases were routed somewhere else. Reporting it
as a fact about the person's spending on learning would be wrong, and asking
the person why they spend so little on learning would be worse -- it spends
their attention on a question premised on an artefact.

The other small category fails differently, and the difference is worth keeping
separate. Its 2 rows are two entries on a single date for one clothing
retailer. The category names spending connected to other people, and the row
model has no participant column at all -- although the same database does link
people to calendar events. A category can only be populated if the instrument
can record the thing it names. This one cannot, so spending with other people
is not under-recorded, it is unrepresentable, and it necessarily sits inside the
food and travel categories with no marker.

The check that separates these two cases is cheap and runs without asking
anything:

- For every separately declared recurring commitment, compare the declared
  category against the category its matching rows actually carry. Disagreement
  is a scheme defect and locates itself.
- For a conspicuously small category, ask whether the instrument has a field
  that could record what the category names. If it does not, the emptiness is
  structural and no amount of classification discipline will fill it.

Two limits. Only separately declared commitments can be checked this way -- 18
declarations against 1603 rows -- so the comparison proves that the scheme
diverges from itself without measuring how far, and it says nothing about
one-off purchases. And a match clears nothing: agreement between a declaration
and an applied category means only that the two agree, and both can be wrong
together. This is a cheap falsifier, not an audit.
