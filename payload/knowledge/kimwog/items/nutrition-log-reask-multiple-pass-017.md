---
# Authored 2026-09-02 (nutrition craft-lane opening, @meal-craft). FIRST ITEM IN
# THE LANE. Modelled on the @gym-craft pattern: a published practitioner
# protocol whose SHAPE is usable and whose transfer to this consumer is
# explicitly untested, stated as such rather than smoothed over.
# The evidence lane already established that a meal log understates intake
# (item 007). It says nothing about what to DO when a logged meal looks thin.
# This is that half.
id: nutrition/log-reask-multiple-pass-017
domain: nutrition
lane: "@meal-craft"
grade: D (published-protocol, transfer untested)
locale: universal
as_of: 2008-2026
contested: no
sources:
  - "https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/ampm-usda-automated-multiple-pass-method/"  # USDA ARS Food Surveys Research Group -- AMPM described as "a research-based, multiple-pass approach employing 5 steps designed to enhance complete and accurate food recall and reduce respondent burden"
  - "https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/ampm-features/"  # the five passes, verbatim: Quick List / Forgotten Foods / Time and Occasion / Detail Cycle / Final Probe
  - "https://doi.org/10.1093/ajcn/88.2.324"  # Moshfegh AJ, Rhodes DG, Baer DJ, Murayi T, Clemens JC, Rumpler WV, Paul DR, Sebastian RS, Kuczynski KJ, Ingwersen LA, Staples RC, Cleveland LE. Am J Clin Nutr 2008;88(2):324-332. PMID 18689367 -- n=524 aged 30-69, three 24-h recalls over two weeks, validated against total energy expenditure by doubly labelled water
  - "source:nutrition/self-report-underreporting-007 -- the measurement finding this protocol is the operational response to"
  - "source:nutrition/unlogged-day-not-zero-019 -- what to do when the re-ask is not possible at all"
  - "framework:VC-E craft -- the instrument is published and its ACCURACY is validated, but nothing has tested it as a chat-based self-report with no interviewer, no food model booklet and no fixed session. The transfer is the untested part and is graded as craft, not as evidence"
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
claim: >
  The re-ask of a thin-looking meal record has a published shape, and it is not
  the intuitive one. The USDA Automated Multiple-Pass Method runs five named
  passes in a fixed order: Quick List (collect a list of foods and beverages
  consumed the previous day), Forgotten Foods (probe for foods forgotten during
  the Quick List), Time and Occasion (collect time and eating occasion for each
  food), Detail Cycle (for each food collect detailed description, amount and
  additions, then review the 24-hour day), and Final Probe (final probe for
  anything else consumed). Two structural features carry the craft content:
  omission is chased in its own dedicated pass BEFORE any question of quantity
  is asked, and amount is asked LAST, after description and after the occasion
  is fixed. Validated against doubly labelled water in 524 adults with three
  recalls over two weeks, the method underestimated energy intake by 11 percent
  on average, by under 3 percent in normal-weight subjects, with the largest
  shortfall and the largest share of low reporters among obese subjects.
reasoning: >
  This is a federal survey instrument with a published step structure and a
  doubly-labelled-water validation, so the protocol itself is not folklore.
  What makes it a craft item rather than an evidence item is the transfer: AMPM
  is interviewer-administered, uses a physical Food Model Booklet at the Detail
  Cycle, and runs as a scheduled session. A conversational agent reading a
  self-kept log has none of those. No study was located testing the five-pass
  shape in that setting, so the ORDER is carried as a defensible default and the
  ACCURACY figures are carried as properties of the original instrument, not as
  properties of the transfer. The residual bias number also matters in its own
  right: even a well-run, interviewer-administered, multiple-pass recall still
  came in 11 percent short, so re-asking narrows the gap and never closes it.
  Note the direction of agreement with the evidence lane: the AMPM validation
  found the shortfall concentrated by body mass, independently reproducing the
  differential-bias finding in nutrition/self-report-underreporting-007. That
  convergence is the single strongest argument against the widespread coaching
  habit of applying one flat upward correction to a client's log.
  WHAT WAS NOT RETRIEVED: the actual probe list used inside the Forgotten Foods
  pass lives in the instrument, not on the published description pages, and was
  not obtained. This item therefore carries the EXISTENCE and POSITION of that
  pass and deliberately does not invent its contents.
---

# nutrition/log-reask-multiple-pass-017

When a logged meal looks too thin to be true, the instinct is to ask whether the
amount is right. The published instrument does the opposite, and the order is the
part worth stealing.

The USDA's multiple-pass recall runs five passes. First a quick list of what was
eaten. Then a separate pass whose only job is to chase things the person forgot
in the first pass. Only then does it fix the time and the eating occasion for
each item. Only after that does it ask for the description, the amount and the
additions, and re-walk the whole day. Then a final sweep for anything else.

Two things in that sequence are the craft. Omission gets its own dedicated step,
run before any question of quantity, because the dominant error in a food record
is a missing item rather than a wrong number. And quantity is asked last, once
the food is described and the occasion is pinned, because an amount asked in the
abstract is an amount invented.

The instrument is not magic. Checked against biological energy expenditure in
524 adults over three recalls, it still came in 11 percent short. In
normal-weight subjects the gap was under 3 percent; in obese subjects it was
largest, and so was the share of implausibly low reporters. Re-asking narrows the
gap. It does not close it, and how much it narrows depends on who is answering --
which is the same body-mass-dependent pattern the measurement item in this
domain's evidence lane reports from a completely different pool of studies. Two
independent lines therefore say the same thing: the shortfall is a property of
the person as well as of the method, so one flat correction applied to everyone
is the wrong repair.

Two honest limits. The method was built for an interviewer with a set of physical
food models in front of a respondent in a scheduled session; nothing has tested
the same five-pass shape in a chat with an assistant, so the ordering travels as
a sensible default and the accuracy numbers stay attached to the original
setting. And the actual list of prompts inside the forgotten-foods pass sits
inside the instrument rather than in its published description, and was not
obtained here, so this item carries the existence and the position of that pass
and does not invent its contents.

One consequence for when to re-ask at all. Because the shortfall is
person-dependent, a day that merely looks numerically low is not by itself a
signal -- for one person that is the normal reading of their own instrument.
What is a signal is a structural hole: an eating occasion the person normally
records and did not, a day with fewer occasions than their own established
pattern, a meal recorded with no additions when their meals normally carry them.
Chase the missing slot, not the small number.
