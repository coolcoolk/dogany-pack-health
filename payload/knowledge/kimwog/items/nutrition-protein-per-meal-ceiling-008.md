---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). This item exists
# to hold a LIVE DISPUTE against an already-shipped item: the per-meal ceiling
# in nutrition/protein-intake-002 was directly challenged by a 2023 tracer trial
# and the challenge is itself disputed in print. Neither side is laundered.
# Item 002 keeps ownership of the daily-intake range; this item owns the ceiling
# dispute only.
id: nutrition/protein-per-meal-ceiling-008
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2023-2024
contested: yes
sources:
  - "https://doi.org/10.1016/j.xcrm.2023.101324"  # Trommelen J, van Lieshout GAA, Nyakayiru J, Holwerda AM, Smeets JSJ, Hendriks FK, van Kranenburg JMX, Zorenc AH, Senden JM, Goessens JPB, Gijsen AP, van Loon LJC. Cell Rep Med 2023;4(12):101324. PMID 38118410, PMC10772463
  - "https://doi.org/10.1123/ijsnem.2024-0041"  # Witard OC, Mettler S. Int J Sport Nutr Exerc Metab 2024;34(5):322-324. PMID 38991545 -- the published caution against the practical reading
  - "https://doi.org/10.1123/ijsnem.2024-0107"  # Trommelen J, Holwerda AM, van Loon LJC. Response to Witard and Mettler. Int J Sport Nutr Exerc Metab 2024. PMID 38986499
  - "source:nutrition/protein-intake-002 -- the shipped item carrying the 0.25 g/kg or 20-40 g per-meal figure this dispute is about"
  - "source:nutrition/observational-dominance-003 -- lane rule: a single trial does not close a question"
applicability:
  axes:
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      POPULATION BOUND, and it is narrow. The trial enrolled 36 healthy,
      recreationally active young men aged 18-40. The published counter-comment
      states explicitly that these participants were recreationally active but
      NOT resistance-trained, and that the no-upper-limit reading does not appear
      to translate to resistance-trained young women. Do not speak this finding
      to a trained user, or to a woman, as if it were established for them.
    grade: C
  - note: >
      DO NOT INVERT THIS INTO ADVICE. That a 100 g bolus produces a larger and
      longer anabolic response than 25 g is a mechanistic measurement over 12
      hours. No trial has shown that eating protein in large infrequent boluses
      produces more muscle over a training block than the same daily total spread
      out. The measured endpoint is protein synthesis, not accrued muscle.
    grade: B
claim: >
  The long-standing per-meal anabolic ceiling (about 0.25 g/kg body weight, or
  20-40 g absolute) is contested rather than settled. A quadruple-tracer
  feeding-infusion trial in 36 healthy recreationally active young men found that
  100 g of protein after resistance exercise produced a greater and longer
  (beyond 12 hours) anabolic response than 25 g, with a dose-response rise in
  amino acid availability and incorporation into muscle protein and negligible
  change in breakdown or oxidation rates. The authors conclude the response has
  no upper limit in magnitude or duration. A published counter-comment accepts
  the measurement but disputes the practical reading and states the result does
  not appear to extend to resistance-trained young women.
reasoning: >
  This is a single, methodologically strong, mechanistically deep trial that
  contradicts a figure this warehouse already ships at the top confidence band.
  The lane's own rules forbid both available shortcuts: it cannot be dismissed
  (the tracer methodology is stronger than what established the ceiling) and it
  cannot promote itself over a converged position (one trial, n=36, one narrow
  population, and a live printed dispute between the authors and independent
  commentators). It therefore sits at the RCT-level pre-consensus band with a
  contested flag, and the resolution is deliberately withheld rather than guessed.
  What survives for a consumer is narrow and it is a DE-ESCALATION, not a new
  target: there is no evidential basis for warning a user that protein above
  roughly 40 g in one sitting is wasted. That warning was never well founded and
  is now directly contradicted. It does not follow that large boluses are better,
  because no study has taken this to a muscle-mass endpoint over a training block.
---

# nutrition/protein-per-meal-ceiling-008

The familiar rule that a single meal can only use twenty to forty grams of
protein for muscle-building is under real challenge. A tracer study using four
simultaneous isotope labels followed thirty-six young men for over twelve hours
after they ate either twenty-five or one hundred grams of protein following
resistance exercise, and found the larger dose produced a bigger and much longer
anabolic response with essentially no increase in oxidation or breakdown. The
authors state flatly that the response has no upper limit.

That is not the end of the argument, and this item deliberately does not end it.
An independent published comment accepts the measurement while objecting to how
it has been read, and adds that the participants were recreationally active
rather than resistance-trained and that the finding does not appear to hold for
resistance-trained young women. The original authors replied in print. The
dispute is live, so the claim is held one step below the top of the confidence
ladder and carries a contested flag.

What actually changes for someone logging meals is smaller than the headline
suggests, and it points toward relaxing a rule rather than adopting a new one.
There is no longer a defensible basis for telling a user that protein beyond a
per-meal threshold is wasted. There is equally no basis for telling them to eat
in large infrequent boluses, because the studied endpoint is protein synthesis
measured over hours, not muscle measured over months. The daily-total claim is
owned by a separate item and is not disturbed here.
