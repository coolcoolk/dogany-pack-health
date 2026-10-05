---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
id: spending-saving/flat-rate-usage-overestimation-010
domain: spending-saving
grade: B (administrative usage records matched to contract choice)
lane: "@household-behavioral"
locale: US
as_of: 2006
contested: no
sources:
  - "DellaVigna, S. and Malmendier, U. (2006). Paying Not to Go to the Gym. American Economic Review 96(3), 694-719. https://doi.org/10.1257/aer.96.3.694"
  - "source:spending-saving/subscription-cancellation-friction-009 -- the renewal-side error; this item is the sign-up-side error"
  - "source:spending-saving/spending-self-prediction-bias-005 -- the same self-prediction failure, measured on spending rather than on usage"
refraction_notes:
  - note: >
      Three US health clubs in one metropolitan area, contracts and attendance
      records from the late 1990s and early 2000s, with dollar prices from that
      period. The prices are historical and must never be quoted as current. The
      structural finding -- people pay a per-use price far above the a-la-carte
      option because they overestimate their own future usage -- is what carries.
    grade: C
claim: >
  When people choose a recurring plan, they systematically buy for a version of
  themselves that does not show up. DellaVigna and Malmendier matched health-club
  members' contract choices to their actual attendance records. Members who chose
  a monthly contract costing over USD 70 per month attended on average 4.3 times
  per month, which works out to a price of more than USD 17 per expected visit,
  while the same clubs offered a ten-visit pass at about USD 10 per visit. Over
  the life of the membership these members forwent on average about USD 600. The
  authors attribute the pattern to overconfidence about future self-control:
  members misestimated both how often they would attend and how likely they were
  to cancel. Note the second half, which is usually dropped: the error was not
  only about usage. It was also about CANCELLATION -- people expected to stop
  paying sooner than they did, which is the same inertia measured from the
  seller side in item 009.
reasoning: >
  Graded at the strong empirical band because the outcome is an administrative
  usage record matched to an actual contract and an actual price, not a survey
  response or a stated intention -- the person's forecast is compared against
  what they demonstrably did. It stays below the top band because it is three
  clubs in one US metropolitan area in one period, and because the interpretation
  (overconfidence rather than, say, option value or convenience) is an inference
  from the pattern. It ships because it supplies the half of the recurring-cost
  story that item 009 does not: 009 explains why a subscription survives, this
  one explains why it was bought. For an agent holding a spending log the
  consequence is concrete and computable, and it is the rare case where the
  ledger contains everything needed to check the claim: a recurring charge can be
  divided by the number of times it was actually used, and the resulting per-use
  price compared against what the same thing costs one at a time. That
  calculation is the item's whole operational content, and it does not depend on
  the historical dollar figures at all.
---

# spending-saving/flat-rate-usage-overestimation-010

People do not buy subscriptions for who they are. They buy them for who they
plan to be, and the plan is measurably wrong.

Researchers matched gym members' contract choices against the turnstile records
of how often those members actually came. People on monthly contracts of over
seventy dollars showed up 4.3 times a month. That is more than seventeen dollars
a visit, at clubs that were selling ten-visit passes at about ten dollars a
visit. Over the life of a membership the average member left roughly six hundred
dollars on the table by picking the plan that felt like the committed choice.

The mistake had two parts, and the second is usually left out of the retelling.
Members overestimated how often they would attend, and they also overestimated
how quickly they would cancel once they were not attending. They were wrong
about the usage and wrong about the exit, and the two errors compounded in the
same direction.

That makes this the sign-up half of the recurring-cost problem, with the
renewal half measured separately from payment-network data. One explains why the
subscription was bought; the other explains why it never ended.

The operational content survives the age of the study completely, because it is
an arithmetic instruction rather than a number: take a recurring charge, divide
it by the number of times the thing was actually used in the period, and compare
the result to what one use costs on its own. A log of dated entries already
contains both sides of that division. If the per-use price is worse than the
a-la-carte price, the plan is being bought for a hypothetical person.

The dollar figures themselves are from three US clubs around the turn of the
century and are historical. They are not to be quoted as current prices, and the
result is not evidence about Korean recurring-service pricing.
