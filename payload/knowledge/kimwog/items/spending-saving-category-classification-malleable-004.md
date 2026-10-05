---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# The category-drift item. Directly relevant to any per-category budget.
id: spending-saving/category-classification-malleable-004
domain: spending-saving
grade: C (laboratory studies, single research programme)
lane: "@household-behavioral"
locale: universal
as_of: 2006
contested: no
sources:
  - "Cheema, A. and Soman, D. (2006). Malleable Mental Accounting: The Effect of Flexibility on the Justification of Attractive Spending and Consumption Decisions. Journal of Consumer Psychology 16(1), 33-44. https://doi.org/10.1207/s15327663jcp1601_6 (full text read at https://www-2.rotman.utoronto.ca/facbios/file/mma.pdf)"
  - "Heath, C. and Soll, J. B. (1996). Mental Budgeting and Consumer Decisions. Journal of Consumer Research 23(1), 40-52. https://doi.org/10.1086/209465 -- the prior work establishing that consumers set category budgets and track expenses against them"
  - "Thaler, R. H. (1999). Mental accounting matters. Journal of Behavioral Decision Making 12(3), 183-206. https://doi.org/10.1002/(SICI)1099-0771(199909)12:3<183::AID-BDM318>3.0.CO;2-F -- the framework these studies test, including the explicit claim that mental accounting evolved to economise on thinking costs and so carries imprecision"
refraction_notes:
  - note: >
      These are hypothetical-scenario laboratory studies with student-population
      samples and stated willingness-to-spend as the outcome, not observed
      transactions. Consumer-psychology findings of this vintage and design are
      exactly the class that the replication literature treats with suspicion,
      and no replication of this specific effect was located in this pass. The
      DIRECTION is consistent with the classification behaviour visible in any
      real category-tagged ledger; the effect size should not be quoted.
    grade: D
claim: >
  Category budgets are not a fixed partition that spending is sorted into; the
  sorting itself moves to accommodate the spending. Cheema and Soman (2006)
  state it directly: mental accounts are often characterised as self-control
  devices consumers use to prevent excess spending, but under conditions of
  ambiguity the mental accounting process is MALLEABLE, and consumers have
  flexibility in assigning expenses to different accounts. Their central result
  is that an AMBIGUOUS expense -- one that can plausibly be assigned to more
  than one account -- is more likely to be incurred than an unambiguous expense
  that is constrained either by an existing budget or by a previously
  constructed account. In one study (n = 218, three expense types crossed with
  whether accounts were constructed before or after the expense was considered)
  the ambiguous item was a restaurant dinner, assignable to food or to
  entertainment, and participants assigned it to whichever account still had
  room. Unambiguous items (a food delivery, a movie) could not be reassigned and
  the budget constraint held. Constructing the accounts BEFORE encountering the
  expense removed the flexibility and reduced spending.
reasoning: >
  Graded at the observational band and no higher: hypothetical scenarios,
  stated intentions rather than transactions, one research programme, no located
  replication. It is shipped anyway because the mechanism is verifiable directly
  against the artefact the agent already holds -- a category-tagged spending log
  -- and because it predicts a specific, checkable pattern rather than a vague
  tendency. Two consequences for a ledger agent, both structural. First, a
  per-category budget is weaker than it looks, and it is weakest exactly where
  categories overlap; the observable symptom is a category boundary that moves
  rather than a limit that is breached. Second, and this is the actionable half:
  the studies found that fixing the account BEFORE the expense removed the
  effect. An agent that classifies at logging time, from a stable rule, is doing
  something different from an agent that lets the user classify after the fact
  when the answer is convenient. The failure this item guards against is
  reporting a clean per-category result without checking whether the categories
  themselves held still.
---

# spending-saving/category-classification-malleable-004

A category budget assumes the categories stay put. They do not.

The finding is that when an expense could honestly belong to more than one
category, people file it wherever there is still room, and that this makes them
more likely to spend it at all. A restaurant dinner can be food or it can be
entertainment. If the food budget is spent and the entertainment budget is not,
it becomes entertainment, and the dinner happens. An expense with only one
plausible home -- a food delivery, a cinema ticket -- has nowhere to go, so the
budget actually binds and the spending does not happen.

The experiments also found the repair, which is more useful than the problem.
When people set up their categories BEFORE they encountered the expense, the
flexibility disappeared and the constraint held. When they set the categories up
afterwards, they built the categories that justified what they wanted.

For a ledger, this changes what per-category numbers mean. If a category looks
disciplined, check the neighbouring one: the discipline may be a relabelling.
Overlapping pairs are where this shows up -- eating out against groceries,
hobby against everyday goods, transport against travel. And it argues for
classifying at the moment of entry from a stable rule rather than letting the
tag be chosen later, because later is exactly when the convenient answer is
available.

Hold the confidence low. These are hypothetical-choice laboratory studies with
stated spending intentions, from one research programme, with no replication
found. The direction is checkable against a real log; the magnitude is not
something to quote.
