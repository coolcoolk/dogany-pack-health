---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# The closest located randomised test of the exact product class this lane
# serves. It is a partial null and is shipped as one.
id: spending-saving/budget-app-rct-knowledge-not-saving-014
domain: spending-saving
grade: B (randomised controlled trial, single population)
lane: "@household-behavioral"
locale: PE
as_of: 2023
contested: no
sources:
  - "Frisancho, V., Herrera, A. and Prina, S. (2023). Can a mobile-app-based behavioral intervention teach financial skills to youth? Experimental evidence from a financial diaries study. Journal of Economic Behavior & Organization 214, 595-614. https://doi.org/10.1016/j.jebo.2023.08.014 (working-paper text at https://doi.org/10.2139/ssrn.4509719)"
  - "source:spending-saving/tracking-monitoring-transfer-limit-001 -- the domain-general monitoring effect this trial fails to reproduce in the money domain"
  - "source:spending-saving/advice-effect-ceiling-contested-013 -- the dispute this trial lands on the pessimistic side of"
refraction_notes:
  - note: >
      The treatment is a BUNDLE -- the recording app plus regular enumerator
      visits plus SMS over 27 weeks -- so the trial cannot attribute any effect
      to the app alone. That cuts both ways: the knowledge gain may be the
      enumerators, and the savings null is a null for the whole bundle, which is
      considerably more support than an app on its own would have.
    grade: B
  - note: >
      Peruvian youth, a population with low baseline financial exposure and thin
      savings capacity. A null on savings amounts in a population with little
      surplus is weaker evidence than the same null would be in a
      middle-income household. The null on savings PROBABILITY is less
      vulnerable to that objection than the null on amounts.
    grade: C
claim: >
  The nearest thing to a randomised test of "does a spending-recording app change
  financial behaviour" found that it moved knowledge and did not move saving.
  Frisancho, Herrera and Prina randomised access to a user-friendly budget
  recording tool, bundled with regular enumerator visits and SMS delivery over a
  27-week period, against a placebo app. Adopting the tool and recording
  transactions regularly had a positive and statistically significant effect on
  financial literacy scores and on awareness of market prices for goods and
  services. Effects were concentrated among youth with no previous exposure to
  financial education. On behaviour the results split: credit usage expanded at
  both the extensive and the intensive margin, while the probability of saving
  was unchanged and the amount saved was unchanged. The honest summary is that
  the intervention taught something real and did not produce the outcome the
  product category is sold on.
reasoning: >
  Graded at the strong empirical band -- randomised assignment, an active placebo
  control rather than a do-nothing control, a 27-week exposure, and pre-specified
  behavioural outcomes -- and held below the top band because it is one trial in
  one population. It is shipped precisely because it is a partial null, and
  because the alternative to shipping it is a lane in which the domain-general
  monitoring result (item 001) stands unopposed and gets read as evidence that
  expense tracking saves money. It is not. The one time somebody randomised an
  actual budget-recording tool and measured saving, saving did not move. Two
  cautions against over-reading in the other direction. The treatment is a bundle,
  so the null belongs to the bundle rather than to the app, and the population is
  youth with limited surplus, where an amount-saved null is expected to be weak
  evidence. But the probability-of-saving null survives that objection better,
  and the expansion of credit use is a result nobody designing such a product
  would have predicted or wanted. What this supports operationally: a ledger
  should be justified as a measurement and decision-support instrument, and the
  claim that keeping it will by itself increase saving is not evidenced.
---

# spending-saving/budget-app-rct-knowledge-not-saving-014

Somebody did the obvious experiment. Give people a budget-recording app, at
random, and see whether they save more.

The trial ran 27 weeks, with a placebo app as the control rather than nothing,
and bundled the recording tool with regular visits and text-message prompts. It
worked on knowledge: financial literacy scores rose, and so did awareness of what
things actually cost, with the largest gains among participants who had never
had any financial education before. Those are real effects with a real control
group.

On behaviour, it did not deliver what the product category promises. The
probability of saving was unchanged. The amount saved was unchanged. What did
change was credit use, which expanded on both margins -- more people using
credit, and more use among those already using it. That is not a result anyone
building a budgeting app would put on the box.

Set this against the general evidence that monitoring progress changes
behaviour, and the tension is the point. Monitoring works across 138 randomised
studies of goals in general. When the goal was money and the monitor was a
spending log, the behaviour did not move.

Two limits keep it from being a verdict. The treatment was a bundle, so the null
belongs to the whole package rather than to the app, and the enumerator visits
may be carrying the knowledge gain. And the participants were young people with
little spare money, where a null on the amount saved is not very informative --
though the null on whether they saved at all is harder to dismiss that way.

The conclusion to build on is narrower than the marketing and more defensible
than it: a spending log earns its place as an instrument for measuring and for
supporting specific decisions. The claim that keeping one will by itself make
someone save more does not have evidence behind it, and the one direct test
points the other way.
