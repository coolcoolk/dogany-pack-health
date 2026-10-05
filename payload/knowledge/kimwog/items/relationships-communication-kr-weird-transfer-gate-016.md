---
# Collection sprint 2026-09-02, relationships-communication lane expansion.
# The mandated locale check for this sprint. The instruction was to check the
# Korean / East Asian case wherever a claim might be culture-specific, and to
# mark or omit anything whose transfer could not be verified. The result splits
# cleanly in two and the split is the finding: the HEALTH side has direct
# Korean cohort evidence, the COUPLES/COMMUNICATION side has none at all. This
# row records that split so the domain's other rows can be spoken with the right
# hedge instead of a blanket one.
# Rubric: relationships-communication @dyadic (VC-C), locale row.
id: relationships-communication/kr-weird-transfer-gate-016
domain: relationships-communication
grade: C (that the social-isolation and mortality association is reproduced in Korean cohorts); D (any transfer of the couples/communication findings to a Korean population, which has no supporting sample)
lane: "@dyadic"
locale: KR
as_of: 2007-2025
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/40274055/"  # Yang JM, Hwang J, Boo Y. 2025, Ann Epidemiol 106:55-66, doi 10.1016/j.annepidem.2025.04.014 -- Korean Longitudinal Study of Aging, 6,284 participants, isolation trajectories 2006-2012, mortality 2013-2022
  - "https://pubmed.ncbi.nlm.nih.gov/35008145/"  # Jeong H, Yim HW, Nam BW. 2022, Epidemiol Health 44:e2022012, doi 10.4178/epih.e2022012, PMCID PMC9117106 -- Korean population-based cohort, 1,033 participants over 60, 2-year all-cause mortality
  - "https://pubmed.ncbi.nlm.nih.gov/32719123/"  # Joel S et al. 2020, PNAS 117(32):19061-19071, doi 10.1073/pnas.1917036117 -- the source of the explicit all-Western sampling statement
  - "https://pubmed.ncbi.nlm.nih.gov/33536694/"  # Barreto M, Victor C, Hammond C, Eccles A, Richins MT, Qualter P. 2021, Pers Individ Dif 169:110066, doi 10.1016/j.paid.2020.110066, PMCID PMC7768187 -- BBC Loneliness Experiment, 46,054 participants across 237 countries and territories, self-selected online sample
  - "relationships-communication/relationship-quality-predictors-joel-009"  # the row whose stated Western-only limit this one carries forward
  - "relationships-communication/social-connection-mortality-magnitude-008"  # the row this one supplies Korean corroboration for
  - "framework:GRADE -- the Korean corroboration is graded at the observational band and no higher. The two Korean cohorts are real prospective population data, but one is 1,033 people over a 2-year window with a sex-split result and a very wide interval, and the other is a trajectory analysis with propensity-score matching whose exposure classification is model-derived. Together they establish direction in Korean data, not magnitude. The couples/communication transfer is graded at the bottom band because it rests on nothing: no East Asian sample was located in ANY of the couples sources used in this sprint. That is an absence, not a demonstrated failure to transfer."
refraction_notes:
  - note: >
      THE SPLIT, which is the actual finding of this row. The health-side claim --
      weaker social connection associated with higher mortality -- HAS Korean
      primary evidence behind it. The couples-and-communication claims do NOT have
      any East Asian evidence behind them, from any source used in this sprint.
      These two halves of the domain therefore deserve different hedges, and
      applying one blanket "this may not transfer" caveat to both understates the
      first and overstates the second.
    grade: C
  - note: >
      What the Korean cohorts actually show. Yang, Hwang and Boo 2025 used the
      Korean Longitudinal Study of Aging (6,284 participants), classified social-
      isolation trajectories from 2006 to 2012 with propensity-score matching
      between urban and rural participants, and followed mortality from 2013 to
      2022. In urban areas, ascending (HR 1.89), mild (HR 1.86) and severe (HR
      2.58) isolation trajectories were significantly associated with all-cause
      mortality; in rural areas, ascending (HR 1.42), moderate (HR 1.59) and
      severe (HR 1.67). Descending isolation was not associated in urban areas --
      that is, isolation that RESOLVED did not carry the risk, which is a
      direction-of-effect signal worth noting even though the design cannot
      establish causation.
    grade: C
  - note: >
      The second Korean cohort, and its important asymmetry. Jeong, Yim and Nam
      2022 followed 1,033 Korean participants over 60 (320 men, 713 women) for
      2-year all-cause mortality. Social isolation was an independent predictor of
      mortality in elderly MEN (adjusted relative risk 4.6, 95 percent CI 2.0 to
      10.2) but NOT in women; depressive symptoms were an independent predictor in
      women (aRR 2.0, CI 1.2 to 3.6) but not in men. The point estimate for men is
      much larger than anything in the international meta-analyses, and the
      interval is correspondingly wide -- read this as directional corroboration
      in Korean data, never as a Korea-specific effect size. A 2-year window and
      102 deaths cannot support a magnitude claim.
    grade: C
  - note: >
      CONTESTED, on the cross-cultural loneliness result, which points the
      opposite way to the intuitive expectation. Barreto et al. 2021 analysed
      46,054 participants aged 16-99 across 237 countries, islands and
      territories, and found loneliness INCREASED with individualism, decreased
      with age, and was greater in men than in women -- the most vulnerable group
      being younger men in individualistic cultures. On Hofstede's dimension Korea
      is collectivistic, so the naive transfer of Western loneliness prevalence
      figures to a Korean population would OVERSTATE it. But the sample is the BBC
      Loneliness Experiment: a self-selected online media audience, not a
      probability sample of any country, and country-level individualism is a crude
      proxy for an individual's cultural context. Carry the direction as a caution
      against importing Western prevalence figures, not as a measured Korean rate.
    grade: D
  - note: >
      The couples-side gap, stated at its source rather than inferred. Joel et al.
      2020 -- 43 datasets, 29 laboratories, the best-powered study in this domain
      -- states that all of the current datasets were sampled from Western
      countries: the United States, Canada, Switzerland, New Zealand, the
      Netherlands and Israel, and that future work should examine whether the
      effects generalise beyond the Western context. There is no East Asian sample
      in it. The couples-therapy meta-analytic evidence carried at
      relationships-communication/couples-therapy-rct-006 already flags its own
      sample-composition limit. So every substantive couples finding in this domain
      is Western-sampled, and the honest statement is that transfer is UNTESTED --
      not that it fails.
    grade: D
  - note: >
      The one partial counterweight, handled carefully. The relationship-
      satisfaction trajectory meta-analysis carried at
      relationships-communication/satisfaction-trajectory-duration-010 reports that
      its pattern held across country and ethnicity as moderators. That is the only
      cross-cultural robustness signal this sprint located anywhere in the couples
      literature, and it is a moderator null inside a sample whose regional
      composition is not broken down. It means no difference was DETECTED. It does
      not mean the curve was verified in Korea, and it must not be upgraded into
      that.
    grade: D
  - note: >
      EXPLICITLY REFUSED, and recorded so a later sprint does not adopt it. The
      cultural-psychology finding that Asians and Asian Americans benefit more from
      IMPLICIT social support (focusing on valued social groups) than from EXPLICIT
      support (seeking advice and emotional solace), with the reverse for European
      Americans, comes from Taylor, Welch, Kim and Sherman 2007 (Psychol Sci
      18(9):831-837, doi 10.1111/j.1467-9280.2007.01987.x). It is an appealing and
      frequently cited result, and it was NOT shipped as an actionable claim in
      this sprint for three reasons: it is a small single-laboratory study from the
      pre-replication-crisis era with biological stress-response endpoints of the
      kind that replicated poorly; no independent replication or meta-analysis was
      located; and "Asian American university students" is not the same population
      as an adult living in Korea. Recorded here as an untested hypothesis worth
      knowing about, never as a basis for changing how support is offered.
    grade: D
claim: >
  This domain's evidence splits by half on Korean transferability, and the two
  halves need different hedges. HEALTH SIDE, corroborated: the social-isolation
  and mortality association is reproduced in Korean primary data. Yang, Hwang and
  Boo (2025, Annals of Epidemiology) followed 6,284 Korean Longitudinal Study of
  Aging participants and found severe social-isolation trajectories associated
  with all-cause mortality in both urban (HR 2.58) and rural (HR 1.67) areas,
  with resolving isolation NOT associated in urban areas. Jeong, Yim and Nam
  (2022, Epidemiology and Health) followed 1,033 Koreans over 60 and found social
  isolation an independent predictor of 2-year mortality in men (aRR 4.6, CI
  2.0-10.2) but not women, with depressive symptoms predicting in women but not
  men. Read these as directional corroboration in Korean data, never as
  Korea-specific effect sizes. COUPLES AND COMMUNICATION SIDE, untested: the
  best-powered study in the domain states that all 43 of its datasets came from
  Western countries with no East Asian sample, and every substantive couples
  finding carried here is Western-sampled. Transfer is UNTESTED, not shown to
  fail. Separately, loneliness INCREASES with cultural individualism across
  46,054 people in 237 territories (Barreto et al. 2021), so importing Western
  loneliness prevalence into a Korean context would likely overstate it -- but
  that sample is a self-selected online media audience, so carry the direction
  only. The Taylor et al. 2007 implicit-versus-explicit social support finding was
  searched and REFUSED as an actionable claim: single small pre-replication-era
  laboratory study, no located replication, and Asian-American students are not
  Koreans in Korea.
reasoning: >
  The sprint instruction was to check the Korean and East Asian case wherever a
  claim might be culture-specific, and to mark or leave out anything whose
  transfer could not be verified. Doing that produced a cleaner answer than
  expected, and the answer is a split rather than a verdict, which is why it
  earns its own row instead of a caveat sentence on each of the others: the
  health-side finding has direct Korean cohort evidence and the couples-side
  findings have none whatsoever. Attaching one uniform "may not transfer" hedge to
  both would be wrong in both directions -- too weak for the mortality row, which
  has been reproduced in Korean data twice, and too strong for the couples rows,
  where nothing has been tested at all and the honest word is untested rather than
  doubtful. The Korean corroboration is deliberately held at the observational
  band. Both cohorts are genuine prospective population data, but one runs 2 years
  with 102 deaths and reports a point estimate for men several times larger than
  any international meta-analysis with an interval to match, and the other derives
  its exposure from trajectory modelling with propensity-score matching. Together
  they establish that the direction holds in Korea; neither can establish a
  magnitude, and quoting an adjusted relative risk of 4.6 as a Korean effect size
  would be exactly the kind of small-sample precision this domain's checklist
  flags. The Barreto result is carried at the bottom band and marked contested on
  purpose: it is the largest cross-cultural loneliness dataset located and it
  points against the intuitive expectation, which makes it worth recording, but a
  self-selected BBC audience is not a probability sample of any nation and
  country-level individualism is a crude individual-level proxy. The Taylor 2007
  refusal is recorded inside the item rather than only in the ledger because it is
  the single most likely thing to be reached for when an East Asian support
  question arises, and a refusal that only lives in a gap file will not be present
  at the moment it is needed. Marked contested because the cross-cultural
  loneliness direction is genuinely disputed territory and because the domain's
  central couples claims rest on samples that exclude the owner's population
  entirely.
---

# relationships-communication/kr-weird-transfer-gate-016

Almost all of this domain was measured on Western samples. Checking what
survives the trip to Korea produced a split, and the split is worth more than a
blanket warning.

The health half transfers, and there is Korean data behind that statement rather
than an assumption. A study following more than six thousand participants in the
Korean Longitudinal Study of Aging classified social isolation over six years and
tracked mortality for nine more. Severe isolation was associated with higher
all-cause mortality in both urban and rural areas. Notably, isolation that
resolved was not associated with it in urban areas. A second Korean cohort, over a
thousand people aged over sixty, found social isolation independently predicting
two-year mortality in men -- though not in women, where depressive symptoms
predicted instead.

Those numbers should be read as direction, not magnitude. The men's estimate in
the second study is far larger than anything in the international meta-analyses
and its confidence interval is correspondingly wide, which is what happens with a
two-year window and around a hundred deaths. What the Korean cohorts establish is
that the association exists here too. They cannot establish how big it is.

The couples and communication half is a different situation entirely. The
best-powered study in the field -- forty-three datasets, twenty-nine laboratories
-- says outright that every one of its samples came from a Western country, and
names them: the United States, Canada, Switzerland, New Zealand, the Netherlands,
Israel. No East Asian sample anywhere. The couples-therapy evidence carries its
own sample-composition warning. So the correct word for everything on that side is
untested, not doubtful. Nobody has looked.

There is one partial counterweight. The relationship-satisfaction trajectory
synthesis reports that its pattern held across country and ethnicity as
moderators. That is the only cross-cultural robustness signal found anywhere in
this literature, and it means no difference was detected -- not that the curve was
checked in Korea.

One cross-cultural result points against intuition and is worth knowing. Across
forty-six thousand people in more than two hundred territories, loneliness
increased with cultural individualism, and the most vulnerable group was younger
men in individualistic cultures. Korea sits on the collectivistic side of that
dimension, which implies that importing Western loneliness prevalence figures here
would overstate the picture. But the sample was a self-selected online audience
recruited through a broadcaster, not a probability sample of any country, so this
is a caution against importing numbers rather than a Korean number of its own.

Finally, something searched and deliberately not shipped. There is a well-known
finding that people of East Asian background benefit more from implicit support --
drawing comfort from belonging to valued groups -- than from explicitly asking for
advice or emotional solace, with the pattern reversed for European Americans. It
is appealing, it is frequently cited, and it was refused here as a basis for
action: one small single-laboratory study, from the era whose stress-response
results replicated badly, with no replication located, and studying Asian-American
students rather than adults living in Korea. Worth knowing it exists. Not worth
changing how support is offered.
