---
id: spending-saving/catch-all-partition-before-reclassify-020
domain: spending-saving
grade: C (census of one instance ledger)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: no
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. The catch-all category decomposed by payee string and by the kind column; monthly catch-all share computed across all thirteen calendar months in the window."
  - "instrument-schema: kit_life spend_entry.kind, which carries exactly two values in this instrument and therefore cannot express a transfer; and the fixed_cost table in the same database, whose declared category assignments were compared against the ledger's."
  - "source:spending-saving/category-classification-malleable-004 -- the behavioural category-drift finding, which this item does NOT invoke, because the decomposition below shows the catch-all is not filled by drift."
refraction_notes:
  - note: >
      ONE LEDGER, NOT A SAMPLE. The decomposition is a census of one catch-all.
      A different household with cash habits or an itemising importer would have
      a differently composed one. What transfers is the instruction to decompose
      before acting, and the three-class partition the decomposition revealed.
    grade: C
  - note: >
      THE GROWTH ASSUMPTION WAS FALSE HERE, WHICH IS THE REASON TO CHECK IT.
      Across thirteen months the catch-all share ranged from 4.0 to 13.7 percent
      with no trend in either direction. This is one ledger and does not
      establish that catch-alls do not grow. It establishes that the growth must
      be measured before it is acted on, because the intuition that a catch-all
      accumulates was wrong about the first real one examined.
    grade: C
claim: >
  A growing catch-all category and a catch-all full of the wrong KIND of thing
  are different problems, and the second is far more likely and is not fixed by
  reclassification. Measured on the instance ledger, the catch-all holds 126
  rows, the fifth largest of eleven categories. Decomposed, it is: 63 rows that
  are income, which is every income row in the entire ledger; 33 expense rows
  that are balance-sheet transfers -- 19 loan principal-and-interest payments,
  12 pension-savings contributions, 2 wallet top-ups; 28 expense rows whose
  payee string names a payment gateway or card acquirer and therefore identifies
  no merchant at all; and 2 remaining rows. Genuine miscellaneous CONSUMPTION is
  approximately zero. Two further facts settle what this is. First, the catch-all
  is NOT growing: across thirteen months its share of rows ranged from 4.0 to
  13.7 percent with no trend. Second, the owner's own declared recurring
  commitments in the same database assign salary, loan repayment, pension saving
  and a savings deposit to the catch-all deliberately, so this is a designed
  destination and not accumulated sloppiness. The underlying cause is structural:
  the instrument's kind column carries exactly two values, income and expense,
  and cannot express a transfer, so everything that is neither a purchase nor
  income has nowhere to go and lands in the category of last resort. The
  operating rule: never reclassify a catch-all before decomposing it, and
  decompose it into three classes with three different treatments -- (i)
  not-consumption (income, transfers, saving, debt principal), which must leave
  the consumption report entirely and for which reclassification into a spending
  category is the error rather than the fix; (ii) unresolvable payee, which only
  the user can resolve and only while it is still recallable, making it a queue
  with a deadline rather than a backlog; (iii) true miscellany, the only class
  reclassification helps, and in this ledger nearly empty.
reasoning: >
  The obvious reading of a large catch-all is that classification has been lazy
  and the repair is to sort the pile. Decomposing a real one says otherwise.
  Half of this catch-all is income, which is not a spending category problem at
  all. A quarter is money moving between the household's own holdings -- loan
  principal, retirement contributions, wallet funding -- which is not consumption
  and must not appear in a consumption total in ANY category, so moving those
  rows into a better-named spending category would make the report worse, not
  better. Another fifth is rows whose payee is a payment intermediary, which no
  amount of thinking will resolve because the information is not in the ledger;
  only the person who made the purchase can say what it was, and their ability
  to say so decays, which makes this a queue against a clock rather than a
  backlog to be worked through eventually. What remains, the actual miscellany
  the category is named for, is a residue. The structural cause is visible one
  layer down in the instrument: the kind column admits income and expense and
  nothing else, so a transfer has no representation and falls through to the
  catch-all. That is why this is a craft item and not a behavioural one -- the
  evidence lane's category-malleability finding describes a person relabelling an
  ambiguous expense to free up a budget, and none of these rows were relabelled
  by anyone. Graded at the observational band: it is a census of one catch-all,
  and a household with substantial cash spending or a more granular importer
  would show a different composition. The transferable content is the
  instruction to decompose first and the three-class partition, not the
  proportions. The stale-assumption catch is recorded deliberately: the belief
  that a catch-all grows was checked against thirteen months of data and was
  false, which is the whole argument for checking rather than assuming.
---

# spending-saving/catch-all-partition-before-reclassify-020

The catch-all category in this ledger is the fifth largest of eleven, with 126
rows. The natural reaction is to reclassify it. That would be the wrong move,
and the decomposition shows why in one pass.

Of the 126 rows:

- 63 are income. That is every income row in the ledger -- all of it lands
  here.
- 33 are transfers between the household's own holdings: 19 loan
  principal-and-interest payments, 12 retirement-savings contributions, 2
  payment-wallet top-ups.
- 28 have a payee string naming a payment gateway or card acquirer, which
  identifies no merchant and no purchase.
- 2 are left over.

Actual miscellaneous consumption, the thing the category is named for, is
approximately nothing.

So this is not a pile of badly-sorted purchases. It is the place where
everything that is not a purchase ends up, and one layer down the instrument
explains itself: the column that records what a row IS admits exactly two
values, income and expense. A loan repayment is neither. A savings contribution
is neither. With no third value available they are stored as expenses, and the
category of last resort is where they settle. The owner's own declared recurring
commitments in the same database do this deliberately -- salary, loan
repayment, pension saving and a savings deposit are all declared against the
catch-all. Nobody was being careless. The model has a missing dimension and the
catch-all is where it surfaces.

That gives three classes, and they need three different things done to them:

1. NOT CONSUMPTION -- income, transfers, saving, debt principal. These must
   leave the consumption report altogether. Moving them into a
   better-named spending category is the error, not the fix: it would put
   loan principal into a housing total and retirement saving into a savings
   total that is then read as expenditure. What they need is a second axis, not
   a better label.
2. UNRESOLVABLE PAYEE -- rows whose payee is an intermediary. Nothing in the
   ledger will ever resolve these. Only the person who made the purchase can,
   and their ability to do so decays from the day of the transaction. This is a
   queue with a deadline, not a backlog. Rows that sit in it long enough become
   permanently unresolvable, and at that point the honest move is to mark them
   so rather than to guess.
3. TRUE MISCELLANY -- the only class reclassification helps, and here almost
   empty.

One more thing worth reporting because it contradicts the assumption that
prompted the check. The catch-all is not growing. Across thirteen months its
share of rows moved between 4.0 and 13.7 percent with no trend in either
direction. One ledger does not establish that catch-alls never grow. It does
establish that the growth is a measurement, not a given, and the intuition was
wrong about the first real one looked at. Measure the trend before acting on
it; the check costs one aggregation over data already held.

Limit: this is a census of a single catch-all, in a ledger with no cash rows
and a coarse importer. A different household would decompose differently. What
travels is the instruction to decompose before acting, and the three-class
partition to decompose into.
