---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). The consumer asks
# this question daily ("should the log be evened out across meals?"), so the
# absence of a good answer has to be stored as a first-class item rather than
# left for the model to fill in. The positive finding here is exactly the design
# class this lane exists to discount: an n=8 acute crossover.
id: nutrition/protein-distribution-thin-009
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 2014-2022
contested: yes
sources:
  - "https://doi.org/10.3945/jn.113.185280"  # Mamerow MM, Mettler JA, English KL, Casperson SL, Arentson-Lantz E, et al. J Nutr 2014;144(6):876-880. PMID 24477298 -- n=8, 7-day crossover, EVEN vs SKEW, the positive acute result
  - "https://doi.org/10.1016/j.clnu.2017.02.020"  # Kim IY, Schutzler S, Schrader AM, Spencer HJ, Azhar G, Wolfe RR, et al. Clin Nutr 2018;37(2):488-493. PMID 28318687 -- 8-week RCT, n=14 older adults, NULL on lean body mass, strength, function
  - "https://doi.org/10.3390/nu14214442"  # Justesen TEH, Jespersen SE, Tagmose Thomsen T, Holm L, van Hall G, et al. Nutrients 2022;14(21):4442. PMID 36364705 -- RCT, n=24 older adults, no difference in muscle protein synthesis
  - "https://doi.org/10.3390/nu12051441"  # Hudson JL, Bergia RE III, Campbell WW. Nutrients 2020;12(5):1441. PMID 32429355 -- review: does the evidence support the concept
  - "https://doi.org/10.1007/s00394-021-02487-2"  # Jespersen SE, Agergaard J. Eur J Nutr 2021. PMID 33550490 -- systematic review: evenness associated with higher muscle mass but NOT strength or turnover
  - "source:nutrition/protein-intake-002 -- daily total, the claim that does have converged support"
  - "source:exercise/small-n-culture-006 -- the lane rule that forces the discount applied here"
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE EVIDENCE BASE IS THE WRONG POPULATION for a training consumer. The two
      controlled trials that took distribution to a real outcome (lean mass,
      strength, function) were both run in OLDER adults, where the research
      motivation is sarcopenia, not hypertrophy. No adequately powered trial has
      tested even versus skewed distribution to a hypertrophy endpoint in young
      resistance-trained adults. Applying either the positive or the null result
      to such a user is an extrapolation across populations.
    grade: D
  - note: >
      The systematic-review signal that evenness associates with higher muscle
      mass is OBSERVATIONAL and carries this lane's standard confounding
      objection with unusual force: people who eat protein at breakfast differ
      systematically from people who do not. It did not extend to strength or to
      protein turnover, which is what a causal effect would be expected to move.
    grade: C
claim: >
  Whether daily protein should be spread evenly across meals is not established.
  The often-cited positive result is an n=8 seven-day crossover measuring 24-hour
  muscle protein synthesis. When the question was taken to controlled trials with
  real outcomes it did not replicate: an 8-week randomised trial (n=14, older
  adults) found no effect of distribution pattern on lean body mass, strength,
  function or synthesis rate, and a further randomised trial (n=24, older adults)
  found no difference in synthesis or amino acid utilisation. A systematic review
  found evenness associated with higher muscle mass but not with strength or
  protein turnover, and that association is observational. Total daily protein
  remains the supported lever.
reasoning: >
  This is a case where the field's structure, not any single result, decides the
  grade. The concept is mechanistically attractive and heavily promoted, the
  supporting trial is an eight-person acute crossover, and both attempts to
  confirm it at an outcome that matters returned null. Under this lane's rules
  and exercise/small-n-culture-006, an acute crossover of that size is precisely
  what must be discounted, and two nulls at the outcome level are the more
  informative signal. It is held at the observational band with a contested flag
  rather than being reported as either established or refuted, because the trials
  that exist are small, in the wrong age group, and none tested hypertrophy in
  trained young adults. The honest operational answer for a consumer reading a
  daily log is that skew toward dinner is not a defect to correct, and that
  chasing an even split at the cost of hitting the daily total inverts the
  evidence.
---

# nutrition/protein-distribution-thin-009

Spreading protein evenly across the day is one of the most confidently repeated
pieces of nutrition advice for anyone training, and its evidence base does not
support that confidence. The study everyone cites fed eight people for a week and
measured protein synthesis over twenty-four hours. When later investigators asked
whether the pattern actually changes anything a person can feel, over eight weeks
and with lean mass, strength and function as endpoints, it did not. A second
randomised trial found no difference in synthesis either.

The one supportive signal at scale is a review-level association between an even
intake pattern and higher muscle mass, and it fails the obvious test: it does not
extend to strength or to protein turnover, which is what a real causal effect
should also move. Association without the mechanistic corroborates is exactly the
pattern this lane treats as confounded.

There is a further limitation that is easy to miss and changes the reading
entirely. Both controlled trials were run in older adults, because the question
is funded as a sarcopenia question. Nobody has tested even versus skewed
distribution against muscle growth in young trained people. So the claim is held
at the observational band with the dispute flagged, and the practical stance is
deliberately permissive: a log that puts most protein at dinner is not a problem
to be fixed, and sacrificing the daily total to even out the split would trade a
supported lever for an unsupported one.
