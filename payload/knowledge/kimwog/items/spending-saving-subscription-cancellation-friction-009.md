---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
id: spending-saving/subscription-cancellation-friction-009
domain: spending-saving
grade: B (comprehensive payment-network data, structural estimation)
lane: "@household-behavioral"
locale: US
as_of: 2025 (published), payment-card network panel
contested: no
sources:
  - "Einav, L., Klopack, B. and Mahoney, N. (2025). Selling Subscriptions. American Economic Review 115(5), 1650-1671. https://doi.org/10.1257/aer.20231612 (abstract read verbatim at the journal record; earlier circulation as NBER WP 31547, https://doi.org/10.3386/w31547)"
  - "source:spending-saving/automation-removes-salience-008 -- the same inattention mechanism measured from the consumer side"
  - "source:spending-saving/flat-rate-usage-overestimation-010 -- the complementary error made at sign-up rather than at renewal"
refraction_notes:
  - note: >
      The headline magnitude is a MODEL estimate, not a directly observed
      quantity. The authors estimate the revenue effect using two stylised
      models of consumer inertia (inattention and switching costs); the directly
      observed fact is the cancellation spike in card-replacement months. Quote
      the observation with more confidence than the estimate.
    grade: B
  - note: >
      A US payment-card network panel. Korean recurring-payment practice differs
      in ways that plausibly change the size of the effect -- card reissue
      cycles, 자동이체 through bank accounts rather than cards, and carrier
      billing all alter how often a subscription is forced back into view. No
      Korean equivalent measurement was located.
    grade: C
claim: >
  A large share of subscription revenue comes from customers who are no longer
  choosing to subscribe. Einav, Klopack and Mahoney use comprehensive data from
  a large payment card network to study one benefit to firms of selling
  subscriptions: the prospect that consumers will continue to pay for
  subscriptions they no longer value. Their central observed fact is that months
  during which cards are REPLACED -- when active renewal is required, because the
  charge fails until the customer re-enters details -- are associated with much
  higher rates of cancellation. Using two stylised models of consumer inertia,
  driven by inattention or by switching costs, they estimate that these
  cancellation frictions roughly DOUBLE seller revenues on average, holding
  fixed the initial number of subscribers. The identifying logic is worth
  keeping in mind because it is what an agent can imitate: the card replacement
  is an exogenous event that forces a decision, and the size of the cancellation
  response measures how many of the ongoing payments were decisions at all.
reasoning: >
  Graded at the strong empirical band. It is comprehensive transaction data
  rather than survey or laboratory evidence, published in a flagship journal,
  and the core empirical fact -- the cancellation spike when renewal is forced --
  is a direct observation rather than an inference. It is held below the top
  band because the headline "roughly double" figure comes out of structural
  models of inertia rather than out of the data directly, and because it is one
  country's payment infrastructure. The operational consequence is unusually
  clean for this lane, because it does not require changing anyone's
  preferences. The measured intervention is simply forcing the decision back
  into view. An agent reading a ledger can identify recurring charges from the
  entries themselves and can manufacture the equivalent of a card-replacement
  moment on purpose. Note what this item does NOT license: it gives no basis for
  a claim about how much any particular household is wasting on subscriptions,
  and no Korean measurement of the same effect was found.
---

# spending-saving/subscription-cancellation-friction-009

The evidence for the subscription problem is better than the folklore about it,
and it is a different claim.

Researchers with access to a large payment card network's full transaction data
looked at what happens in the months a customer's card gets replaced. A
replacement breaks every recurring charge attached to it: the payment fails, and
the customer has to actively re-enter the card to continue. In those months,
cancellations jump sharply. Nothing about the services changed. The only thing
that changed is that continuing became a decision instead of a default.

That gap -- between what people pay when continuing is automatic and what they
pay when continuing requires an action -- is the quantity of interest. Modelling
it two ways, as inattention and as switching costs, the authors estimate that
these frictions roughly double sellers' revenue relative to a world where
customers re-decided each period.

What makes this useful rather than merely interesting is that the effective
intervention is already identified and requires no persuasion. It is not
budgeting advice or willpower. It is putting the recurring charge back in front
of the person and making continuation an explicit choice. An agent holding a
ledger can find recurring charges from the entries themselves and stage that
moment deliberately, on a schedule, instead of waiting for a card to expire.

Two limits. The doubling figure comes from structural models, while the
cancellation spike is directly observed -- so lean on the second. And this is US
payment infrastructure; Korean recurring payments run through different rails,
including bank-account transfers and carrier billing that may never force a
re-entry at all, and no equivalent Korean measurement was located. That last
point cuts toward the intervention being more necessary here, not less, but it
is an argument rather than a measurement.
