---
id: spending-saving/review-cadence-no-measured-optimum-026
domain: spending-saving
grade: D (a recorded search absence, plus two deterministic consequences)
lane: "@ledger-craft"
locale: universal
as_of: 2025-2026 (ledger window 2025-08-20 to 2026-08-20, measured 2026-09-02)
contested: no
sources:
  - "absence-record: GAPS.md spending-saving section, v18 gap OPTIMAL REVIEW CADENCE -- nothing at any tier was located on how often a spending review should happen, and no frequency comparison was located at all. This item does not repeat that search; it records what follows from the absence."
  - "source:spending-saving/tracking-monitoring-transfer-limit-001 -- the monitoring meta-analysis whose moderators are directly actionable (effects larger when outcomes are physically recorded, and when reported or made public) and which reports NOTHING about frequency."
  - "instance-measurement: kit_life spend_entry census on the live instance ledger, 1603 rows spanning 2025-08-20 to 2026-08-20, read read-only 2026-09-02. Mean rows per covered day 4.5 across 353 covered days; the final day of the import window carries 1 row."
  - "source:spending-saving/ledger-provenance-sets-failure-mode-017 -- and its siblings 018 through 024, which are the errors this item shows a cadence cannot reach."
refraction_notes:
  - note: >
      THIS IS AN ABSENCE, NOT A NULL RESULT. No study was located finding that
      cadence does not matter. What was located is nothing at all, in either
      direction. The difference matters: a later sprint that finds a frequency
      comparison is adding evidence where there was none, not overturning a
      finding.
    grade: D
  - note: >
      THE BOUNDARY-DAY OBSERVATION IS ONE DAY AND ITS CAUSE IS NOT ESTABLISHED.
      The final day of the window carries 1 row against a mean of 4.5. Whether
      that reflects settlement lag at the feed boundary or simply a quiet day
      cannot be told from one ledger, and no lag figure is claimed. What survives
      either way is that the newest end of a feed-derived ledger is of unknown
      completeness, which is enough for the consequence drawn.
    grade: D
claim: >
  There is no measured optimum for how often a spending review should happen,
  in either direction, and this lane records the absence rather than filling it.
  The monitoring meta-analysis that underwrites the whole premise of a tracking
  product reports moderators that ARE actionable -- effects on goal attainment
  were larger when the information was physically recorded, and larger when
  outcomes were reported or made public -- and reports nothing whatever about
  frequency. Two consequences do follow deterministically and are worth more
  than a cadence number. FIRST, WHAT CADENCE ACTUALLY TRADES: the only thing a
  shorter interval reliably buys is fresher recall, because the questions a
  review must put to the user -- what was this unresolvable payee, was this
  duplicate real, was this meal shared -- degrade with time, and that deadline
  is set outside the review. Against that it spends the user's attention, which
  is finite. Nothing else about the interval is established. SECOND, WHAT NO
  CADENCE CAN CATCH: every dominant error found in the measured ledger is
  cadence-insensitive. A payment channel the ledger cannot see stays invisible
  at any frequency. A category boundary set by which platform processed the
  payment is equally wrong weekly and annually. A stored-value load is not a
  purchase on any schedule. Non-consumption sitting in the catch-all does not
  sort itself out faster when looked at more often. A scheme that diverges from
  its own declarations diverges at every interval. Shared payments the
  instrument cannot represent are unrepresentable every week. Reviewing more
  often does not make an unrepresentable thing representable. THIRD, a shorter
  window is MORE exposed to the one completeness problem a feed has: the newest
  end of a feed-derived ledger is of unknown completeness -- the final day of
  this window carries 1 row against a mean of 4.5 -- and the shorter the review
  window, the larger the fraction of its days that sit in that uncertain zone.
  A month-to-date figure compared against a completed month is comparing an
  incomplete period with a complete one.
reasoning: >
  The question of how often to review is the one a product most wants answered
  and it is the one this domain has least to say about, so the temptation to
  supply a confident number is high and there is nothing behind any number that
  could be supplied. The lane's own gap record already states that no frequency
  evidence was located at any tier, and this item exists to make that absence do
  useful work rather than to leave it as a hole. What it can do is redraw the
  question. A cadence is usually argued about as though it were the main lever
  on whether a ledger tells the truth, and the census behind this lane says it
  is a small lever: six separate error mechanisms were measured directly in a
  real ledger, and not one of them is sensitive to how often somebody looks. The
  errors are structural -- what the instrument can see, what its payee strings
  mean, what its categories can represent -- and structural errors are fixed at
  the instrument, not at the review. What a cadence genuinely governs is
  narrower and is a real trade: the questions that require the user's memory
  have an expiry, and a longer interval means more of them arrive past it, while
  a shorter interval spends more of a finite attention budget. That trade is
  worth stating to a user honestly, including the part where no evidence sets
  its optimum. The third consequence is the one most likely to be got backwards
  in practice: shortening the review window increases rather than decreases
  exposure to feed incompleteness at the newest end, because a smaller window
  has proportionally more of its days in the zone whose completeness is unknown.
  Graded at the bottom of the usable band and shipped anyway, because the
  alternative to shipping a recorded absence with its consequences is that
  someone fills the silence with a rule of thumb, which is the failure mode this
  lane's checklist has a trigger for.
---

# spending-saving/review-cadence-no-measured-optimum-026

How often should a spending review happen? Nobody knows, and this lane is not
going to guess.

The gap record for this domain already states it: nothing was located at any
tier on review frequency, and no frequency comparison was found at all. The
meta-analysis that underwrites the entire premise of a tracking product is
informative on two things that ARE actionable -- monitoring works better when
the information is physically recorded, and better when outcomes are reported or
made public -- and says nothing about how often. That is an absence, not a null
result. Nobody found that frequency does not matter; nobody looked.

Three things do follow, and they are worth more than a number would be.

**What a cadence actually trades.** The only thing a shorter interval reliably
buys is fresher recall. The questions a review has to put to a person -- what
was this payee that only names a payment gateway, was this identical pair a real
pair, was this meal shared -- all depend on memory, and memory has a deadline
that is set outside the review. Against that, every review spends attention,
which is finite and which the person would rather spend elsewhere. That is the
whole trade. Nothing else about the interval is established.

**What no cadence can catch.** Every dominant error measured in this ledger is
insensitive to how often somebody looks at it:

- A payment channel the ledger cannot see is invisible weekly and invisible
  annually.
- A category boundary set by which platform processed the payment is equally
  wrong at any interval.
- A stored-value load is not a purchase on any schedule.
- Money that is not consumption sitting in the catch-all does not sort itself
  faster under more frequent inspection.
- A classification scheme that disagrees with its own declarations disagrees
  every week.
- Shared payments the instrument cannot represent stay unrepresentable.

None of those are review problems. They are instrument problems, and they are
fixed at the instrument. A review cadence is a much smaller lever than the
attention it usually gets.

**The one way a shorter cadence is worse.** The newest end of a feed-derived
ledger is of unknown completeness. The final day of the measured window carries
one row against a mean of 4.5 across covered days -- whether that is settlement
lag or simply a quiet day cannot be told from one ledger, and no lag figure is
claimed here. But the consequence holds either way: the shorter the review
window, the larger the fraction of its days that sit in the zone whose
completeness is unknown. A month-to-date figure held up against a completed
month is comparing an incomplete period with a complete one, and the comparison
gets worse, not better, as the window shrinks.

So the honest thing to tell a user asking how often to review is: no evidence
sets the frequency, here is what changing it actually costs and buys, and here
is the larger point -- most of what is wrong with these numbers will not be
fixed by looking at them more often.
