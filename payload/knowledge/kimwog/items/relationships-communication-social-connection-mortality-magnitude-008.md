---
# Collection sprint 2026-09-02, relationships-communication lane expansion. The
# domain's first SUBSTANTIVE claim -- the seven prior rows are all refutations,
# curator rules and one therapy-efficacy row. This is the health-side finding a
# life agent is most likely to be asked about, and it is also the domain's
# clearest case of a real result whose popular retelling is one full generation
# of evidence out of date. Rubric: relationships-communication @dyadic (VC-C),
# but note the evidence is epidemiological rather than social-psychological, so
# the grading anchor used here is the cohort/meta-analysis ladder, not the
# lab-experiment one.
id: relationships-communication/social-connection-mortality-magnitude-008
domain: relationships-communication
grade: B (the direction: weaker social connection is prospectively associated with higher all-cause mortality); C (any specific effect magnitude); D (any causal or dose reading)
lane: "@dyadic"
locale: universal
as_of: 2010-2025
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/20668659/"  # Holt-Lunstad J, Smith TB, Layton JB. 2010, PLoS Med 7(7):e1000316, doi 10.1371/journal.pmed.1000316, PMCID PMC2910600 -- 148 studies, 308,849 participants, random-effects OR 1.50 (95% CI 1.42-1.59) <!-- estate-scrub:allow(author surname Smith, not an instance) -->
  - "https://pubmed.ncbi.nlm.nih.gov/25910392/"  # Holt-Lunstad J, Smith TB, Baker M, Harris T, Stephenson D. 2015, Perspect Psychol Sci 10(2):227-237, doi 10.1177/1745691614568352 -- confound-adjusted ORs: social isolation 1.29, loneliness 1.26, living alone 1.32 <!-- estate-scrub:allow(author surname Smith, not an instance) -->
  - "https://pubmed.ncbi.nlm.nih.gov/37337095/"  # Wang F, Gao Y, Han Z et al. 2023, Nat Hum Behav 7(8):1307-1319, doi 10.1038/s41562-023-01617-6, PROSPERO CRD42022299959 -- 90 prospective cohorts, 2,205,199 individuals; social isolation 1.32 (1.26-1.39), loneliness 1.14 (1.08-1.20)
  - "https://pubmed.ncbi.nlm.nih.gov/39836319/"  # Nakou A, Dragioti E, Bastas NS et al. 2025, Aging Clin Exp Res 37(1):29, doi 10.1007/s40520-024-02925-1, PMCID PMC11750934 -- 86 studies in older adults; loneliness HR 1.14 (1.10-1.18), I2 84.0 pct; social isolation HR 1.35 (1.27-1.43); living alone HR 1.21 (1.13-1.30)
  - "relationships-communication/curator-checklist-007"  # the domain rule this item obeys: report observational associations at their real effect sizes, never as headline percentages
  - "framework:GRADE -- every input here is observational. Not one participant was randomised to be connected or isolated, and the 2010 meta-analysis says so in its own discussion. The direction sits at the trial-adjacent band because it is now supported by 90 prospective cohorts and 2.2 million people with prospective design and confounder adjustment, which is about as strong as a non-randomisable exposure can get. The magnitude sits a band lower because the three largest syntheses disagree with each other by a factor of roughly three on the loneliness estimate, and heterogeneity in the newest one is I2 84 pct. Any causal or dose statement sits at the bottom, unsupported."
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The number that everyone quotes is the OLDEST and LARGEST estimate, and it
      has been superseded. Holt-Lunstad 2010 pooled 148 studies and 308,849
      participants to an odds ratio of 1.50, which is where the popular "50
      percent better survival odds" line comes from. The same first author's own
      2015 meta-analysis, restricted to studies that statistically controlled for
      confounds, reported much smaller figures: social isolation 1.29, loneliness
      1.26, living alone 1.32. The largest synthesis to date, Wang 2023 in Nature
      Human Behaviour, covers 90 prospective cohorts and 2,205,199 individuals and
      lands at 1.32 for social isolation and 1.14 for loneliness. Nakou 2025 in
      older adults independently reproduces almost exactly those two figures. So
      the correct summary is not one number but a shape: the direction has
      survived scaling up by a factor of seven in sample size, and the magnitude
      has roughly halved on the isolation side and dropped by more than half on
      the loneliness side. Speak the 2023 and 2025 figures, not the 2010 one.
    grade: B
  - note: >
      Objective isolation and subjective loneliness are NOT the same exposure and
      the newer data separates them. In Wang 2023 the pooled effect for measured
      social isolation is 1.32 while the effect for felt loneliness is 1.14, and
      Nakou 2025 reproduces the same ordering (1.35 versus 1.14). This matters
      operationally for an agent that holds contact records: what it can measure
      is the isolation side, which happens to carry the larger association, but a
      person with a full calendar and a low measured isolation score can still be
      lonely, and the two are separately predictive. Note that Holt-Lunstad 2015
      reported finding NO difference between objective and subjective measures --
      the later and much larger work does find one. Report this split as an open
      disagreement, not a settled fact.
    grade: C
  - note: >
      CONTESTED, and specifically on the point where the popular version does the
      most damage. The "as bad as smoking" comparison originates in the 2010
      paper's own discussion, which states that the magnitude of the effect is
      comparable with quitting smoking and exceeds obesity and physical
      inactivity, and in its Figure 6 comparing log odds across risk factors. What
      the article's TEXT does NOT contain, in the full text checked for this
      sprint, is the specific "equivalent to smoking 15 cigarettes a day" phrasing
      that circulates everywhere. That figure is a secondary retelling of a
      comparison condition in a figure, attached to the 2010 effect size that has
      since been revised downward by the larger syntheses. Treat the cigarette
      equivalence as an unverified popularisation, and note that it is being
      quoted against an estimate its own literature no longer supports. Same
      failure mode as relationships-communication/source-misattribution-rule-005.
    grade: D
  - note: >
      Causality is not available here and the primary authors say so. The 2010
      paper states plainly that one cannot randomly assign human participants to
      be socially isolated, married, or in a poor-quality relationship. Reverse
      causation is the live confound: illness reduces social contact, and social
      contact is measured before death but often after disease onset. Nakou 2025
      finds mortality risk estimates that vary systematically with follow-up
      length, sex, region, chronic disease and study quality, which is what a
      confounded exposure looks like. This does not make the association fake. It
      makes "get more social contact and you will live longer" an unsupported
      inference from data that only supports "people with less social connection
      die sooner, for reasons this design cannot separate."
    grade: D
  - note: >
      NOT established by any source in this item: any dose. There is no threshold
      of contacts per month, no target number of close friends, and no minimum
      contact frequency anywhere in these four syntheses. The exposure variables
      are composite social-integration indices, single-item loneliness scales, and
      living-alone flags. An agent holding a contact log must not convert this
      literature into a numeric cadence target -- see
      relationships-communication/contact-cadence-no-evidence-014, which exists to
      block exactly that move.
    grade: D
claim: >
  Weaker social connection is prospectively associated with higher all-cause
  mortality. The direction is one of the better-replicated findings in this
  domain and now rests on 90 prospective cohorts covering 2,205,199 individuals
  (Wang 2023, Nature Human Behaviour), independently reproduced in 86 studies of
  older adults (Nakou 2025). The MAGNITUDE, however, is much smaller than the
  version in circulation. The famous figure -- odds ratio 1.50, "50 percent
  greater likelihood of survival" -- is Holt-Lunstad 2010, the oldest and least
  confounder-adjusted synthesis. The same author's confound-adjusted 2015 update
  reports 1.29 for social isolation, 1.26 for loneliness and 1.32 for living
  alone; Wang 2023 reports 1.32 for social isolation and 1.14 for loneliness;
  Nakou 2025 reports 1.35, 1.14 and 1.21. Measured isolation and felt loneliness
  are separable exposures with different effect sizes in the newer work, though
  Holt-Lunstad 2015 reported no such difference -- an open disagreement. Every
  input is observational, none randomised, and the original authors state that
  causality cannot be established for this exposure. The "equivalent to smoking
  15 cigarettes a day" phrasing could NOT be located in the 2010 article's text,
  which claims comparability with quitting smoking; treat the cigarette figure as
  an unverified popularisation attached to a superseded effect size. No source
  here supports any dose, threshold, or contact-frequency target.
reasoning: >
  This is the strongest health-side claim available in this domain and it is
  worth having precisely because its popular form is wrong in a specific,
  correctable way rather than wholesale. The pattern -- a real effect, an
  original estimate that becomes the culturally fixed number, and a decade of
  larger and better-adjusted work quietly halving it -- is the same shape as the
  zombie-statistic problem that relationships-communication/
  zombie-stat-retraction-rule-002 was written for, except that nothing here was
  retracted. Nothing is wrong with the 2010 paper. What is wrong is quoting a
  2010 unadjusted pooled odds ratio in 2026 when a 2.2-million-person prospective
  synthesis exists and puts the loneliness figure at 1.14. Graded at the
  trial-adjacent band for direction because a non-randomisable exposure studied
  prospectively across 90 cohorts with confounder adjustment is at the ceiling of
  what this design can deliver, and because two independent 2023 and 2025
  syntheses agree with each other to two decimal places on the loneliness
  estimate. Graded a band lower for magnitude because the three main syntheses
  disagree by roughly a factor of three on that same estimate depending on
  adjustment and sample, and because heterogeneity in the most recent one is 84
  percent. Graded at the bottom for causal and dose readings because the primary
  authors explicitly disclaim the first and no source in the set even attempts
  the second. Contested is set for two reasons: the objective-versus-subjective
  question is answered one way by Holt-Lunstad 2015 and the opposite way by the
  two newer and larger syntheses, and the cigarette-equivalence framing that
  carries this finding in public could not be verified against the article text
  it is attributed to.
---

# relationships-communication/social-connection-mortality-magnitude-008

If someone asks whether loneliness really shortens life, the honest answer has
two halves that point in different directions.

The first half: yes, the direction is real and it has held up under scaling. A
2023 synthesis in Nature Human Behaviour pooled ninety prospective cohorts
covering more than two million people, with a registered protocol, and found
weaker social connection associated with higher all-cause mortality. A 2025
review of eighty-six studies in older adults reproduced it almost exactly. This
is not a fragile finding.

The second half: the number in everyone's head is the wrong one. The famous
"fifty percent better survival odds" comes from a 2010 meta-analysis, the
earliest and least adjusted of the set. Once studies that control for confounds
are the ones being pooled, the association shrinks a lot. Measured social
isolation lands around a third higher risk rather than a half. Felt loneliness
lands around fourteen percent higher. That is still a real signal, and it is not
the signal the popular version describes.

Two other things are worth separating out.

Being isolated and feeling lonely are different exposures. In the newer and
larger work they carry noticeably different effect sizes, with measured
isolation the stronger of the two. The 2015 review reported no such difference,
so this is a live disagreement rather than a settled point -- but it matters for
anything that tracks contact records, because contact records measure the
isolation side and say nothing about the loneliness side.

And the causal reading is not available. The original authors say it themselves:
you cannot randomly assign a person to be isolated. Illness reduces social
contact, which means some of this association runs backwards. "People with less
social connection die sooner" is what the data supports. "Add more social
contact and you will live longer" is an inference the design cannot carry.

One popular detail did not survive checking. The line that loneliness is as bad
as smoking fifteen cigarettes a day could not be found in the text of the paper
it is attributed to. That paper claims comparability with quitting smoking, and
puts a smoking condition in a comparison figure. The specific cigarette count is
a secondary retelling, and it is being attached to an effect size the field has
since revised downward.

Finally, and most practically: nothing in this literature specifies a dose. No
number of friends, no contact frequency, no threshold. The exposures are
composite integration indices and single-item loneliness scales. Anyone
converting this into "call someone every N days" has left the evidence behind.
