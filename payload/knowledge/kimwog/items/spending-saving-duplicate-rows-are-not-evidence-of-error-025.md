---
id: spending-saving/duplicate-rows-are-not-evidence-of-error-025
domain: spending-saving
grade: D (practitioner rule; the duplicate census behind it is a measurement of one ledger)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: yes
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Exact-duplicate groups computed on the triple of date, amount and payee string; group composition tallied by payee class and by amount band; amount-roundness distribution tallied over all 1540 expense rows."
  - "instrument-schema: the absence of any audit table covering kit_life spend_entry, which makes a deletion unrecoverable and invisible; and spend_entry.amount, which is documented as permitting a negative offsetting row."
  - "source:spending-saving/self-report-spending-error-not-uniform-002 -- the finding that self-report error is instrument-dependent and not uniform, which is why recall quality is a function of how long ago the transaction was, and therefore why a re-ask queue has a deadline."
  - "source:spending-saving/stored-value-load-is-not-consumption-019 -- the payee class that dominates this ledger's duplicate groups, and the class in which same-day duplication is most ordinary."
refraction_notes:
  - note: >
      ONE LEDGER, AND THE COMPOSITION IS THE FINDING RATHER THAN THE RATE. That
      7 percent of rows sit in exact-duplicate groups is a property of this
      ledger. What transfers is the structure the census revealed: the duplicate
      rate is HIGHEST in the payee classes where duplication is most plausible,
      which is the opposite of what a duplicate-detection rule assumes.
    grade: C
  - note: >
      A REFUSED HEURISTIC, RECORDED SO IT IS NOT RE-ADOPTED. Round amounts as a
      signal of an estimated rather than an observed figure does not survive
      contact with this ledger: 89 percent of expense rows are multiples of ten
      and 46 percent are multiples of a hundred, because retail prices in this
      market are usually round. Roundness carries almost no discriminating
      information here and is not proposed as a trigger.
    grade: C
claim: >
  An exact duplicate in a spending ledger is not evidence of a duplicated
  record, and de-duplicating silently is a larger error than the duplicate it
  removes. Measured on the instance ledger: 52 groups of rows share an identical
  date, amount and payee, covering 112 rows, 7.0 percent of the ledger. The
  composition is what settles the question. 17 of the 52 groups are
  transit-operator rows, the payee class where two identical same-day
  transactions are entirely ordinary, and the remaining groups are dominated by
  convenience retail, food delivery and small recurring venues -- again the
  classes where genuine repetition is normal. By amount band, 9 groups fall
  below the smallest band, 32 in the low-to-middle band, 11 in the middle band,
  and NONE above it. So the duplicate rate is highest exactly where duplication
  is most plausible and lowest in the amounts where an error would matter, which
  is the reverse of what an automatic duplicate rule assumes. The asymmetry of
  consequences points the same way: a spurious duplicate inflates one month by
  one small amount and stays inspectable, whereas a wrong deletion removes a
  real purchase permanently, and with no audit trail on this table it is neither
  recoverable nor visible, and it changes a figure that may already have been
  reported. The operating rule: never de-duplicate automatically; where a
  duplicate is genuinely suspected, record the correction as a paired offsetting
  row rather than by deleting anything; and ration re-asking, which costs the
  user's attention and expires as recall decays. Re-ask only where duplication
  is IMPLAUSIBLE for that payee class AND the amount is large enough that the
  answer changes a decision. Applied to this ledger, that filter selects
  approximately none of the 52 groups, and the honest output of the duplicate
  check is to ask about nothing.
reasoning: >
  Duplicate detection is standard in ledger products and it is usually built on
  the assumption that identical rows are suspicious. Running the check on a real
  ledger inverts the assumption. The classes that generate the most exact
  duplicates are the classes where a person genuinely does the same thing twice
  in a day -- topping up a transit card, buying at the same convenience store,
  ordering delivery twice -- so the detector fires hardest where it is most
  likely to be wrong. And the amounts are small: no duplicate group in this
  ledger exceeds the middle amount band, which means that even when a duplicate
  IS spurious, resolving it changes no figure anyone would act on. Put those
  together with the cost structure and the rule writes itself. Removing a row is
  irreversible in this instrument and invisible afterwards; leaving it is
  neither. Asking the user is not free either, and unlike the row itself the
  question has an expiry date, because recall of a specific small transaction
  degrades and a queue of unresolved rows is worth less every week it waits.
  That gives a two-condition filter rather than a threshold, and on this ledger
  the filter returns an empty set, which is the useful result: a check whose
  correct output is often no action is still worth running, provided it is
  allowed to output no action. Flagged as contested because this argues against
  what most budgeting products do, and because nothing here measures outcomes --
  no comparison of an auto-de-duplicating ledger against a permissive one was
  located, and the two-condition filter is a proposal calibrated on a single
  duplicate census. The refused roundness heuristic is recorded inside the item
  rather than dropped, because it is the obvious next trigger to reach for and
  it does not work: in a market where retail prices are usually round, almost
  every row is round, and the signal is not there.
---

# spending-saving/duplicate-rows-are-not-evidence-of-error-025

Two rows in this ledger with the same date, the same amount and the same payee
are not evidence of anything. That sounds like a hedge until the check is
actually run.

Measured over one year, 1603 rows: 52 groups share an identical date, amount and
payee, covering 112 rows -- 7.0 percent of the ledger. Then look at what those
groups are. Seventeen of the fifty-two are transit-operator rows: topping up a
card twice in a day is a completely ordinary thing to do. The rest are dominated
by convenience retail, food delivery and small recurring venues, which are again
the places where doing the same thing twice in one day is normal.

So the duplicate detector fires hardest in exactly the classes where it is most
likely to be wrong. That is not a tuning problem, it is the shape of the data:
repetition and duplication look identical in a row that carries no transaction
identifier.

The amounts settle it further. Of the 52 groups, 9 fall below the smallest
amount band, 32 in the low-to-middle band, 11 in the middle band, and none above
it. Even where a duplicate genuinely is spurious, removing it changes no figure
anybody would act on.

Now the consequences, which are not symmetric:

- Leave a spurious duplicate: one month is inflated by one small amount, the row
  stays visible, and it can be corrected at any time.
- Delete a real row: the purchase is gone. This table has no audit trail, so the
  deletion is unrecoverable and leaves no trace, and any figure already reported
  for that month silently changes.

Hence the rule. Never de-duplicate automatically. Where a duplicate is genuinely
suspected and confirmed, record the correction as a paired offsetting row rather
than by deleting anything -- the amount column is documented to accept it, and
it keeps both facts inspectable.

Re-asking the user is the other option and it is not free. It costs attention,
and unlike the row, the question expires: recall of one small transaction
degrades, so a queue of unresolved rows is worth less every week it sits. Ration
it with two conditions, both of which must hold: duplication is implausible for
that payee class, and the amount is large enough that the answer changes a
decision.

Applied to this ledger, that filter selects approximately none of the 52 groups.
That is the useful output, not a failure of the check. A diagnostic whose
correct answer is often "do nothing" is worth running only if it is permitted to
say so.

One heuristic refused and recorded so it is not reached for next. Round amounts
as a marker of an estimated rather than an observed figure does not work here:
89 percent of expense rows are multiples of ten and 46 percent are multiples of
a hundred, because retail prices in this market are usually round. There is no
signal in it.

Limits: this is one ledger, so the 7 percent rate is its own. What transfers is
the structure -- duplicates concentrate where duplication is plausible -- and
the asymmetry between a visible wrong row and an invisible wrong deletion. No
outcome comparison between an auto-de-duplicating ledger and a permissive one
was located, and the two-condition filter is a proposal calibrated on a single
census.
