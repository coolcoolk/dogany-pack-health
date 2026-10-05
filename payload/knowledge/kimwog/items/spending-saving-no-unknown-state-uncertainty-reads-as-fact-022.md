---
id: spending-saving/no-unknown-state-uncertainty-reads-as-fact-022
domain: spending-saving
grade: D (practitioner rule resting on a deterministic instrument fact)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: yes
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Null-category count, scope-value distribution and audit-table coverage tallied directly."
  - "instrument-schema: kit_life spend_entry.category_id, which is nullable; spend_entry.scope, which admits an explicit unknown value; and the database's only audit table, which records goal-lifecycle transitions and does not cover spend_entry at all."
  - "source:spending-saving/catch-all-partition-before-reclassify-020 -- the measured consequence. 28 rows in that catch-all have payee strings that identify no merchant, and they are stored as confident category assignments because the instrument offers no other shape."
  - "source:spending-saving/category-classification-malleable-004 -- the evidence-lane finding that classifying from a stable rule at entry time differs from classifying later when a convenient answer is available. An unmarked guess is what makes the later, convenient answer indistinguishable from the earlier, principled one."
refraction_notes:
  - note: >
      THE INSTRUMENT FACTS ARE DETERMINISTIC AND THE RULE IS NOT. That the
      category column is nullable and unused, that the scope column offers an
      unknown value and never carries it, and that no audit table covers this
      table are checkable properties of the database, not judgements. That
      leaving a row unclassified is BETTER than guessing into the catch-all is a
      practitioner rule with no measured outcome behind it, and it runs against
      what most budgeting products do.
    grade: D
  - note: >
      THE COST OF THE RULE IS REAL AND IS NOT ESTIMATED HERE. Unclassified rows
      make every category total incomplete by a visible amount, which is
      uncomfortable in a way that a confident wrong total is not. Whether users
      prefer an honestly incomplete report to a confidently wrong one was not
      measured and no evidence on it was located.
    grade: D
claim: >
  A ledger that cannot mark a row as uncertain stores every guess in exactly the
  same shape as every certainty, and the guesses become permanently
  indistinguishable from the facts. Three deterministic facts about the instance
  instrument, each checkable in one query. (1) The category column is NULLABLE,
  and 0 of 1603 rows are null: every row is classified, including the 28 whose
  payee string names only a payment intermediary and therefore identifies no
  purchase. (2) The scope column admits an explicit UNKNOWN value and 0 of 1603
  rows carry it: the one uncertainty marker the schema does provide is unused.
  (3) There is no audit trail on this table -- the database's only audit table
  covers goal lifecycle events -- so a category that is corrected later leaves no
  record that it was ever different, and any figure already reported under the
  old classification becomes irreproducible. The consequence is that uncertainty
  in this ledger is not lost, it is CONVERTED: it goes into the catch-all
  category dressed as a decision, which is a large part of why that category
  contains almost no actual miscellany. The operating rule proposed here, and it
  is a rule rather than a finding: prefer the states the schema already offers to
  a guess. Leave a row unclassified when the payee cannot be resolved, since the
  column permits it. Use the explicit unknown value where the question is scope.
  And record the provenance of a classification, so that a later correction is
  visible as a correction. Guessing into the catch-all is the one option that
  destroys the information about which rows were ever in doubt.
reasoning: >
  The instrument facts are not in dispute and take one query each to verify. What
  they add up to is that this ledger has no shape for the sentence "I do not know
  what this was." It has a shape for "this was miscellaneous," which is a
  different and stronger claim, and that is where the uncertainty goes. The
  damage is not the wrong category on any individual row -- it is that after the
  fact nobody can tell which rows were confident and which were shrugs, so a
  later pass cannot target the doubtful ones and has to either re-examine
  everything or trust everything. The absence of an audit trail compounds this in
  a specific way worth stating: if a category is silently corrected later, a
  monthly total already reported under the old classification can no longer be
  reproduced, and the ledger cannot even show that it changed. This is filed as a
  practitioner rule and flagged as contested on purpose. Forcing every row into a
  category is what nearly every budgeting product does, for a defensible reason:
  totals that do not add up look broken, and an unclassified bucket is an
  unfinished chore staring at the user. The counter-argument is that a
  confidently wrong total is also broken, just invisibly, and that the visible
  version is the one that can be repaired. No measured comparison of the two was
  located, and none is claimed. The related evidence-lane finding gives the rule a
  partial anchor rather than a proof: classification fixed in advance from a
  stable rule behaves differently from classification chosen afterwards when a
  convenient answer is available, and an unmarked guess is exactly what makes
  those two indistinguishable in the stored record.
---

# spending-saving/no-unknown-state-uncertainty-reads-as-fact-022

Three facts about this ledger, each one query away:

- The category column is nullable. Zero of 1603 rows are null.
- The scope column offers an explicit unknown value. Zero of 1603 rows use it.
- No audit table covers this table. A category corrected later leaves no trace
  that it was ever anything else.

Put together: the ledger has a way to say "this was miscellaneous" and no way to
say "I do not know what this was." Those are different sentences. The first is a
claim about the purchase. The second is a claim about the record. When only the
first is available, every instance of the second gets written as the first.

That is where the catch-all comes from. Twenty-eight rows in it carry payee
strings that name a payment gateway and identify no merchant. Nobody could have
known what those purchases were. They are stored in exactly the same shape as
the rows where the payee was obvious.

The damage is not the wrong category on any one row. It is that afterwards
nobody can separate the confident rows from the shrugs. A later pass that wants
to clean up the doubtful ones has no way to find them, so it either re-examines
everything or trusts everything, and in practice it trusts everything. The
missing audit trail makes this worse in a specific way: if a category is
corrected months later, a monthly figure already given to the user under the old
classification can no longer be reproduced, and the ledger cannot show that it
moved.

The rule proposed here is to use the states the instrument already has rather
than invent certainty:

- Leave a row unclassified when the payee cannot be resolved. The column allows
  it.
- Use the explicit unknown value where the open question is scope rather than
  category.
- Record where a classification came from, so a later correction reads as a
  correction rather than as the original answer.

This is a rule, not a finding, and it argues against what most budgeting
products do. Forcing a category on every row has a real justification: totals
that do not add up look broken, and a pile of unclassified rows is a chore
sitting in the user's face. The counter is that a confidently wrong total is
also broken, only invisibly, and that the visible kind is the kind that can be
fixed. Which of the two users actually prefer was not measured here and no
evidence on it was located, so the honest statement is that this rule buys
repairability at a cost in comfort, and the size of the cost is unknown.
