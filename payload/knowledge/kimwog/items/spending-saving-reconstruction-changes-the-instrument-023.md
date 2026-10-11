---
id: spending-saving/reconstruction-changes-the-instrument-023
domain: spending-saving
grade: D (practitioner rule resting on a deterministic instrument fact and an evidence-lane boundary)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: yes
sources:
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Day coverage computed against the full calendar span: 353 of 366 days carry at least one row, the 13 absent days are scattered singles and two adjacent pairs, and every row carries the bulk-import provenance value."
  - "instrument-schema: kit_life spend_entry.source, whose documented value set distinguishes how a row ARRIVED (conversational entry, bulk import, and adapter-added values such as import and receipt) but carries no value distinguishing a row entered at the time from a row reconstructed from memory afterwards. The schema comment records that the value set is deliberately extensible without a table rebuild."
  - "source:spending-saving/self-report-spending-error-not-uniform-002 -- specifically its refraction note that a personal ledger is a DIARY instrument and not a recall survey, that this is the relevant comparison class, and that recall-survey error rates must not be imported onto a daily log. A reconstructed day is a recall-survey observation."
  - "source:spending-saving/diary-attrition-zero-reporting-003 -- the finding that a diary fails by producing zeros, which is why an empty day cannot be read as a zero-spending day without knowing the provenance."
refraction_notes:
  - note: >
      THE DIRECTION OF RECONSTRUCTION ERROR IS NOT ESTABLISHED AND IS NOT
      ASSERTED HERE. The evidence lane establishes that self-report error is
      instrument-dependent and NOT uniform across categories. It does not
      establish what a person reconstructing one personal day systematically
      omits or inflates. It is tempting to assume small purchases drop out; that
      is a plausible guess, it was not measured, and it is not claimed. The
      practical consequence is stronger than if the direction were known: an
      error whose direction is unknown cannot be corrected for afterwards.
    grade: D
  - note: >
      AN ABSENT DAY MEANS DIFFERENT THINGS IN THE TWO PROVENANCES. In a
      feed-derived ledger an absent day is a day with no posting on the connected
      rails, which is informative about those rails and silent about cash. In a
      hand-kept ledger it is a day nobody wrote in, which is silent about
      everything. The 13 absent days measured here are of the first kind, so this
      ledger has no reconstruction problem to solve -- the item is about what to
      do when a ledger does.
    grade: C
claim: >
  Reconstructing a missed day from memory does not fill a gap in a ledger; it
  inserts a row from a DIFFERENT INSTRUMENT into the same table, and in an
  instrument that cannot mark it as such the mixing is irreversible. The
  evidence lane draws this boundary explicitly: a personal ledger is a diary
  instrument, that is the comparison class its error properties come from, and
  recall-survey error must not be imported onto a daily log. A day written from
  memory a week later is a recall observation by definition. The instance
  instrument's provenance column records how a row ARRIVED -- entered in
  conversation, bulk imported, and adapter values beyond that -- and has no
  value distinguishing recorded-at-the-time from reconstructed-afterwards, though
  its schema notes the value set is deliberately extensible. So today a
  reconstructed row is indistinguishable from a contemporaneous one, and after
  even one reconstruction pass every completeness and coverage statistic in the
  ledger is computed over a table whose rows no longer share an error model. The
  operating rule: reconstruct only if the reconstructed row can be MARKED as
  reconstructed; if the instrument cannot mark it, mark the day unknown instead
  and leave it empty. This is the same ruling as the general one -- a missing
  record is not evidence of absence -- applied in the direction people usually
  get backwards: the error is not that the empty day gets read as a zero, it is
  that filling it in makes the day look measured. And read the provenance before
  deciding there is a gap at all: in the measured ledger the 13 absent days are
  days with no posting on the connected payment rails, which is a fact about the
  rails and not a recording failure, and reconstructing them would fabricate a
  problem as well as a solution.
reasoning: >
  Two options are usually offered for a missed day, filling it in or leaving it
  blank, and they are usually compared on completeness, where filling it in
  obviously wins. That is the wrong axis. The comparison that matters is what
  each option does to the table's error model. Leaving the day blank leaves one
  instrument with one known and documented failure mode, the one the evidence
  lane characterises. Filling it in creates a table containing two instruments
  with different error properties and no column that separates them, and every
  aggregate computed afterwards silently averages across both. The asymmetry is
  what settles it: a blank day can be reconstructed later, but a table that has
  been mixed cannot be unmixed, because the information that would separate the
  rows was never written down. This item is a practitioner rule and is flagged
  contested for the same reason as its sibling on unknown states -- prompting a
  user to fill in yesterday is ordinary and defensible product behaviour, the
  user does often remember, and a ledger with holes is less useful than one
  without. The rule does not forbid reconstruction; it makes it conditional on
  marking, which the instrument's own extensible provenance vocabulary can
  support. Nothing here is a measured outcome and none is claimed: no study was
  located comparing a marked-reconstruction ledger against an unmarked one, and
  the direction of reconstruction error is deliberately left unstated because it
  was not measured. That last point strengthens rather than weakens the rule --
  an error of unknown direction cannot be adjusted for after the fact, so the
  only available control is knowing which rows carry it.
---

# spending-saving/reconstruction-changes-the-instrument-023

A day with no rows in it is a common situation and the usual reaction is to ask
the person what they spent. That reaction is worth slowing down, because filling
the day in is not the same operation as recording it was.

The evidence lane draws the line explicitly. A personal ledger is a diary
instrument; that is the class its error properties come from; and recall-survey
error must not be imported onto a daily log. A day written from memory a week
later is a recall observation. It is a different instrument. Putting it in the
same table as contemporaneous rows means the table now holds two instruments,
and every completeness figure computed afterwards averages across both without
saying so.

In this instrument that mixing cannot currently be undone. The provenance column
records how a row arrived -- typed in conversation, bulk imported, and further
values that adapters may add -- and has no value that separates
recorded-at-the-time from reconstructed-afterwards. The schema notes that the
value set is deliberately open, so the marker is buildable. It just does not
exist yet, and until it does, a reconstructed row is stored exactly like a
contemporaneous one.

That asymmetry decides the rule. A blank day can be reconstructed at any point
later. A mixed table can never be unmixed, because the information that would
separate the rows was never written down.

So: reconstruct only if the reconstructed row can be marked as reconstructed.
If it cannot be marked, mark the day unknown and leave it empty.

This is the same ruling as the general one -- a missing record is not evidence
of absence -- applied in the direction people usually get backwards. The danger
people expect is that an empty day gets read as a day of no spending. The
danger that actually bites is the opposite: filling the day in makes it look
measured, and from then on nothing distinguishes it from a day that was.

One more check before any of this applies. Read the provenance before deciding
there is a gap. In the ledger measured here, 353 of 366 days carry rows and the
13 that do not are scattered singles and two adjacent pairs, in a ledger where
every row arrived from a card or bank feed. An absent day in that ledger is a
day with no posting on the connected rails. That is a fact about the rails, not
a recording failure, and it is silent about cash either way. Reconstructing
those days would invent the problem as well as the solution.

Honest limits. Nothing here is a measured outcome: no comparison of a
marked-reconstruction ledger against an unmarked one was located, and none is
claimed. The direction of reconstruction error is left unstated because it was
not measured -- it is tempting to assume the small purchases are the ones that
drop out, and that assumption is not made here. That absence makes the rule
stronger rather than weaker. An error whose direction is unknown cannot be
adjusted for afterwards, so the only control available is knowing which rows
carry it.
