---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# Deliberate counterweight to item 006. Automation is not uniformly good.
id: spending-saving/automation-removes-salience-008
domain: spending-saving
grade: C (single quasi-experiment, one utility, one country)
lane: "@household-behavioral"
locale: US
as_of: 2015 (programme introduced 2005)
contested: no
sources:
  - "Sexton, S. (2015). Automatic Bill Payment and Salience Effects: Evidence from Electricity Consumption. The Review of Economics and Statistics 97(2), 229-241. https://doi.org/10.1162/REST_a_00465"
  - "source:spending-saving/automation-defaults-dominate-intention-006 -- the item this one bounds"
  - "source:spending-saving/subscription-cancellation-friction-009 -- the same inattention mechanism observed on the seller side"
refraction_notes:
  - note: >
      One utility's customers, one country, one commodity, and a
      quasi-experimental design over programme enrolment rather than random
      assignment. Self-selection into automatic payment is the obvious threat
      and the reason this item does not sit higher. The MECHANISM -- removing
      the moment where a recurring cost is looked at raises the cost -- is what
      transfers; the percentages are one setting's.
    grade: D
claim: >
  Automating a PAYMENT is not the same as automating a SAVING, and the evidence
  says they run in opposite directions. Sexton (2015) studies the introduction
  of automatic bill payment, which eliminates the need for a consumer to view a
  recurring bill: if enrolled consumers stop inspecting the bill, price salience
  falls, the price perceived by a boundedly rational agent falls, and
  consumption rises. The estimates are that enrolment in automatic bill payment
  increases residential electricity consumption by about 4.0 percent and
  commercial consumption by as much as 8.1 percent, and that enrolment in
  programmes designed to smooth seasonal variation in monthly utility bills for
  low-income customers results in about 6.7 percent greater electricity use.
  The finding generalises as a mechanism rather than as a number: a recurring
  cost that no longer produces a moment of attention becomes a larger recurring
  cost.
reasoning: >
  Graded at the observational band. It is a single quasi-experiment at one
  utility, enrolment is voluntary rather than randomly assigned, and the outcome
  is one commodity in one country -- all of which are exactly the conditions
  this lane's checklist says force a downgrade. It ships anyway because it is
  the only located evidence that bounds this lane's strongest positive item, and
  an automation recommendation that carries only the upside is a one-sided
  claim of the kind item 016 flags. The design rule it supports is specific:
  automate the leg where the desired behaviour is INACTION, and keep visible the
  leg where the desired behaviour is a decision. A standing transfer into
  savings is the first kind -- nothing needs to be noticed for it to work. A
  standing charge for a service is the second kind -- it only stays right if
  somebody looks at it, and this is the measurement of what happens when nobody
  does. The same mechanism appears from the seller's side in item 009, where
  cancellations spike precisely in the months a payment card has to be
  re-entered.
---

# spending-saving/automation-removes-salience-008

Automation gets recommended as a single idea. It is two ideas, and one of them
costs money.

When a US utility introduced automatic bill payment, the bill stopped being
something customers looked at. Electricity use went up: about 4 percent for
residential customers, and as much as 8 percent for commercial ones. A separate
programme that smoothed low-income customers' bills across the seasons -- also
removing the monthly signal -- was associated with about 7 percent higher use.
Nothing about the price changed. What changed was whether anyone saw it.

Set that beside the finding that automatic saving works enormously well, and the
distinction becomes clear. Automation helps when the behaviour you want is for
nothing to happen. A standing transfer into savings succeeds precisely because
it needs no attention. Automation hurts when the behaviour you want is a
periodic decision. A standing charge for a service only stays correct if someone
occasionally asks whether it should still exist, and taking away the moment
where they would ask is what this study measured.

The practical form: automate the inflow to savings, and deliberately
de-automate attention on the outflow. A recurring charge that nobody has looked
at in a year is not a settled decision, it is an unexamined one.

Keep the confidence low on the specific numbers. This is one utility, one
country, one commodity, and customers chose whether to enrol rather than being
randomly assigned, so selection is a live alternative explanation. The
mechanism, not the percentage, is the part to carry.
