---
# Authored 2026-09-02 (nutrition craft-lane opening, @meal-craft). Written to
# close the exact operational question the evidence lane leaves open: what does
# the consumer DO with a day that has no record. The lane already knows the log
# is biased; it had nothing on the gap.
# Filed as craft because the shipped content is an OPERATING RULE. Its empirical
# anchor is strong, but the transfer from questionnaire item non-response to a
# blank day in a conversational log is an inference, and it is graded as one.
id: nutrition/unlogged-day-not-zero-019
domain: nutrition
lane: "@meal-craft"
grade: C (operating rule, empirically anchored, transferred)
locale: universal
as_of: 2009-2015
contested: no
sources:
  - "https://doi.org/10.1097/EDE.0b013e31819642c4"  # Fraser GE, Yan R, Butler TL, Jaceldo-Siegl K, Beeson WL, Chan J. Missing data in a long food frequency questionnaire: are imputed zeroes correct? Epidemiology 2009;20(2):289-294. PMID 19177024 -- 20% of Adventist Health Study-2 participants with missing values re-contacted (n=2091), responses recovered for 92% of missing items
  - "https://doi.org/10.1093/ajcn/88.2.324"  # Moshfegh et al. Am J Clin Nutr 2008;88(2):324-332 -- cited here only for the instrument's design window: the multiple-pass recall collects the PREVIOUS day
  - "source:nutrition/self-report-underreporting-007 -- the within-day bias; this item covers the between-day hole"
  - "source:nutrition/log-reask-multiple-pass-017 -- what to do when the gap is still inside the reconstruction window"
  - "source:spending-saving/diary-attrition-zero-reporting-003 -- CROSS-DOMAIN corroboration of the MECHANISM only, from a different warehouse domain and a different instrument: a decaying diary fails by emitting zeros rather than smaller numbers. The rates do not transfer and are not imported"
claim: >
  An unlogged day is missing data. It is not zero intake, and it is not a small
  intake either. Fraser et al. re-contacted 2091 participants carrying missing
  values across 80 key dietary variables and recovered answers for 92 percent of
  the missing items. The recovered answers did contain a consistent excess of
  zeros relative to non-missing data, but for FREQUENTLY CONSUMED foods most
  missing values were not zeros, missingness was not at random (it concentrated
  in older and less-educated respondents), and the authors' stated conclusion is
  that automatic imputation of zeros for missing data will usually be incorrect,
  with acceptable bias only for infrequently consumed items. The operating rule
  that follows: mark the day unknown and carry it as unknown; never write zero;
  never let an unknown day enter a period average, a streak count or a trend
  line; reconstruct only inside the previous-day window the recall instrument is
  actually designed for, and only to named-food granularity; beyond that window
  leave it unknown rather than producing a plausible day.
reasoning: >
  The empirical anchor is strong -- a large re-contact study that actually
  recovered the missing values instead of modelling them, with a directly stated
  conclusion against zero imputation. It is held below the top band for the
  transfer, not for its own quality: it measures item non-response inside a
  questionnaire, whereas the case here is a whole day absent from a voluntary
  log. The mechanism is the same in shape and the direction of the error is the
  same, which is why the rule is shippable, but no study was located measuring
  the zero-versus-missing question for a consumer meal log specifically, so the
  strength is capped. The cross-domain corroboration is deliberately narrow: a
  spending diary is a different instrument in a different domain, and it is cited
  here ONLY because it independently establishes that a decaying self-kept record
  degrades by producing zeros rather than smaller numbers. That shape is exactly
  the failure mode this rule guards against. No rate from it is imported.
  The reconstruction window is not a guess either: it is the design window of the
  validated instrument. A multiple-pass recall collects the previous day, and no
  method with any validation behind it reaches further back. Reconstructing a
  three-day-old lunch is therefore not a weaker version of a good procedure, it
  is outside every procedure that has been tested, and this item declines to
  publish any accuracy expectation for it.
  ONE THING THIS ITEM DOES NOT LICENSE: it does not say a gap is meaningless. A
  gap is a real signal about the RECORDING, and item 017 uses it as one. It says
  only that a gap is not a measurement of what was eaten.
---

# nutrition/unlogged-day-not-zero-019

A day with nothing written down is a hole in the record, not a day without food.
The distinction sounds pedantic until it is spent: a zero written into a blank
day propagates into every average, every streak, every trend line downstream, and
it does so silently and in a known direction.

The question has been tested about as directly as it can be. Researchers went
back to two thousand people who had left dietary questionnaire items blank and
asked them again, recovering answers for ninety-two percent of the blanks. Blanks
were more likely than average to turn out to be zeros -- so the intuition is not
baseless -- but for foods people actually eat often, most blanks were not zeros
at all, and the blanks were not randomly distributed across people. The authors'
own conclusion is that filling missing data in with zeros will usually be wrong,
and that it is acceptable only for things people rarely eat anyway.

The same failure shape shows up in a completely different kind of record. When a
self-kept spending diary decays, it does not start reporting smaller amounts; it
starts reporting nothing, category by category and then day by day. A record that
is being abandoned looks exactly like a life that has gone quiet, and only one of
those is true.

So the handling is: mark the day unknown, and let unknown stay unknown. Do not
write a zero. Do not let the day into an average, a streak, or a trend. If the
gap is yesterday, it can be reconstructed, because that is the window the recall
instrument was actually built and validated for, and the re-ask has a shape worth
following. If the gap is older than that, it sits outside every method anyone has
tested, and the honest move is to leave it empty rather than to manufacture a
plausible day that will then be indistinguishable from a measured one.

None of this makes a gap uninteresting. A gap is a genuine signal about the
recording -- often the most informative thing in the week. It is simply not a
measurement of what was eaten, and the two must never be stored in the same
column.
