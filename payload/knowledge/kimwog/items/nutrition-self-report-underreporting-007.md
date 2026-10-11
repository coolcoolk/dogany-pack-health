---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). Closes the
# highest-value hole for a consumer that reads a daily meal log: the log itself
# is a biased instrument. Primary source fetched directly (EuropePMC metadata +
# abstract), not via any secondary write-up.
id: nutrition/self-report-underreporting-007
domain: nutrition
lane: "@obs-inferential"
grade: A (field-methodology)
locale: universal
as_of: 1999-2009
contested: no
sources:
  - "https://doi.org/10.1093/aje/kwu116"  # Freedman LS, Commins JM, Moler JE, Arab L, Baer DJ, Kipnis V, Midthune D, Moshfegh AJ, Neuhouser ML, Prentice RL, Schatzkin A, Spiegelman D, Subar AF, Tinker LF, Willett W. Am J Epidemiol 2014;180(2):172-188. PMID 24918187
  - "framework:recovery-biomarker validation (doubly-labelled water for energy, urinary nitrogen for protein) -- the reference method that makes this a measured error, not an opinion"
  - "source:nutrition/observational-dominance-003 -- the lane rule this item supplies the measurement half of"
refraction_notes:
  - note: >
      The five pooled cohorts are US adult populations sampled 1999-2009 with US
      instruments. The DIRECTION (self-report understates intake, and understates
      it more as body mass rises) is a measurement-psychology finding and travels;
      the SPECIFIC percentages do not transfer to a Korean-language log of Korean
      dishes and must not be quoted as if they did. No Korean recovery-biomarker
      validation of a consumer meal log was located in this pass.
    grade: C
  - note: >
      Underreporting is DIFFERENTIAL, not a constant offset. Body mass index,
      education and age predict it. A fixed correction factor is therefore the
      wrong fix, and applying one silently would replace a known bias with a
      hidden one.
    grade: A
claim: >
  Self-reported dietary intake systematically understates true intake when
  measured against recovery biomarkers. Pooled across five large US validation
  studies, mean under-reporting of energy was about 28 percent with a food
  frequency questionnaire and about 15 percent with a single 24-hour recall;
  under-reporting was smaller for protein than for energy. Correlations between
  reported and true intake were weak for absolute energy (about 0.21 by FFQ,
  0.26 by a single recall, rising to 0.31 across three averaged recalls).
  Under-reporting is predicted by body mass index, education level and age, so
  it is differential rather than a uniform offset.
reasoning: >
  Freedman et al. 2014 pooled five validation studies that used recovery
  biomarkers (doubly-labelled water, urinary nitrogen) as the reference, which
  makes the error a measured quantity against an objective standard rather than
  an inference from one instrument to another. Independent populations,
  independent instruments and a converged direction put this at the top
  confidence band as a field-methodology finding. It is the measurement
  companion to nutrition/observational-dominance-003: that item explains why
  observational nutrition inference is weak at the design level, this one
  explains why the exposure variable itself is mis-measured before any design
  question is reached. Operational consequence for a consumer that reads a
  daily meal log: a logged intake is a floor, not an estimate, and the gap
  widens with body mass. Averaging more days raises the correlation with truth
  but does not remove the bias.
---

# nutrition/self-report-underreporting-007

Anything a person writes down about what they ate understates what they actually
ate, and the size of the understatement is itself a variable rather than a
constant. Measured against biological reference methods, food frequency
questionnaires miss roughly a quarter of energy intake and single-day recalls
roughly a sixth. Protein fares better than energy, which matters because protein
is usually the number a training consumer cares most about.

The finding that changes behaviour is not the headline percentage, it is that
the error is differential. Heavier people under-report more. That means a flat
correction factor is the wrong repair, because it would leave the person-to-person
pattern of the bias intact while hiding it behind a plausible-looking number. The
defensible use of a logged intake is as a lower bound and, above all, as a
within-person trend line, where a stable personal bias mostly cancels.

Two limits are worth carrying explicitly. The pooled studies are US adults using
US instruments across 1999 to 2009, so the direction transfers but the specific
percentages do not, and no Korean-language equivalent validation of a consumer
meal log was found. And averaging more recall days improves how well the log
tracks truth without correcting the systematic shortfall.
