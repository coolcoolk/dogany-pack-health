---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The "3x risk" number is the most repeated fact in this domain and it is
# repeated without a denominator, which is what makes it frightening rather than
# informative. This item ships the relative risk and the ABSOLUTE risk together
# and refuses to ship either alone. Same handling this warehouse gives the
# social-connection mortality magnitude in relationships-communication: direction
# robust, magnitude quoted only with its base rate attached.
id: travel/flight-vte-absolute-vs-relative-003
domain: travel
lane: "@travel-clinical"
grade: B (the association and its dose-response); B (the absolute incidence in the cohort studied); D (any personal risk estimate for an individual traveller)
locale: universal
as_of: 2007-2009
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/19581633/"  # Chandra D, Parisini E, Mozaffarian D. 2009, Ann Intern Med 151(3):180-190, doi 10.7326/0003-4819-151-3-200908040-00129 -- meta-analysis, 14 studies, 4055 VTE cases. Abstract read verbatim 2026-09-02
  - "https://pubmed.ncbi.nlm.nih.gov/17896862/"  # Kuipers S, Cannegieter SC, Middeldorp S, Robyn L, Buller HR, Rosendaal FR. 2007, PLoS Med 4(9):e290, doi 10.1371/journal.pmed.0040290, PMCID PMC1989755 -- prospective cohort, 8755 employees, 38910 person-years. Abstract read verbatim 2026-09-02
  - "source:travel/compression-stockings-endpoint-gap-004 -- the intervention side, and why its high-certainty result does not attach to the outcome this item is about"
  - "source:relationships-communication/social-connection-mortality-magnitude-008 -- the same discipline applied to a different hazard ratio: a multiplier without a base rate is not information"
  - "framework:observational-only -- every study in both sources is observational. The meta-analysis pools 11 case-control studies, 2 cohorts and 1 case-crossover; the cohort is a prospective occupational cohort. No randomized evidence on travel as an exposure exists or could exist, so nothing here is a causal effect size, and the meta-analysis's own headline limitation is that all available studies were from Western countries."
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: medication_list
      type: categorical
      role: soft
      unknown_policy: block_specifics
refraction_notes:
  - note: >
      THE TWO NUMBERS MUST TRAVEL TOGETHER. Relative: pooled relative risk 2.0
      (95 percent CI 1.5 to 2.7) across all 14 studies, rising to 2.8 (95 percent
      CI 2.2 to 3.7) with no significant heterogeneity once studies using
      referred control participants were excluded. Absolute: one symptomatic event
      per 4656 long-haul flights, from a prospective cohort of 8755 employees
      followed over 38910 person-years, in which 53 thromboses occurred and 22 of
      them within 8 weeks of a long-haul flight. Speaking the first without the
      second is the standard failure of this claim.
    grade: B
  - note: >
      THERE IS A REAL DOSE-RESPONSE AND IT IS THE ACTIONABLE PART. The
      meta-analysis reports an 18 percent higher risk for each 2-hour increase in
      travel duration by any mode, and 26 percent for every 2 hours of AIR travel
      specifically. So duration is the variable, and note what else that implies:
      the exposure is not aeroplanes as such. Travel by any mode carries the
      dose-response, which points at immobility rather than at anything peculiar
      to a cabin.
    grade: B
  - note: >
      THE RISK WINDOW IS WEEKS, NOT HOURS. The cohort found incidence highest in
      the first 2 weeks after travel, decreasing gradually to baseline by 8 weeks.
      A traveller who lands fine has not cleared the exposure, which matters for
      how a post-trip symptom is interpreted. This is the least-known part of the
      finding and arguably the most useful.
    grade: B
  - note: >
      WHO IT CONCENTRATES IN, AS REPORTED. The cohort states the risk was
      particularly high in employees under age 30, in women who used oral
      contraceptives, and in individuals who were particularly short, particularly
      tall, or overweight. The under-30 finding is counterintuitive and is
      reported here as the cohort reported it, without a mechanism attached and
      without being turned into a screening rule. This is an occupational cohort
      of international-organisation employees, not a general population, so the
      subgroup pattern is a description of that cohort.
    grade: C
  - note: >
      NO PERSONAL NUMBER COMES OUT OF THIS ITEM. A ratio from case-control studies
      and an incidence from one occupational cohort cannot be composed into an
      individual's risk, and doing so would require a personal baseline this
      warehouse does not have. If a traveller has a thrombosis history, a known
      clotting disorder, recent surgery, active cancer, pregnancy or is on
      hormonal therapy, the correct output is not an adjusted number, it is that
      this is a question for their doctor before the flight. That is the boundary
      and it is not negotiable.
    grade: A
  - note: >
      GENERALISABILITY IS FLAGGED BY THE SOURCE ITSELF. The meta-analysis states
      that all available studies were from Western countries and that
      generalizability to non-Western populations is expected but needs
      confirmation. For a Korean traveller that is an untested transfer, not a
      demonstrated one -- the same posture the relationships domain records for
      Western-sampled couples research.
    grade: C
  - note: >
      NOT COVERED. Nothing here supports any specific preventive behaviour. Aisle
      seats, calf exercises, walking every N hours, hydration, aspirin and
      anticoagulants were NOT assessed by either source. The one preventive
      measure with a randomized evidence base in this domain has its own item and
      the news there is more complicated than it looks.
    grade: D
claim: >
  Travel is associated with a higher risk of venous thromboembolism, and the honest
  statement of that risk needs both a ratio and a base rate. The meta-analysis of
  14 studies covering 4055 VTE cases found a pooled relative risk of 2.0 (95
  percent CI 1.5 to 2.7) overall, and 2.8 (95 percent CI 2.2 to 3.7) after
  excluding studies whose controls had themselves been referred for VTE
  evaluation, a selection bias the authors identify as the reason earlier studies
  disagreed. The relationship is dose-dependent: 18 percent higher risk per
  additional 2 hours of travel by any mode, and 26 percent per 2 hours of air
  travel. The absolute risk comes from a prospective cohort of 8755 employees of
  international organisations followed for 38910 person-years, in which 53
  thromboses occurred, 22 of them within 8 weeks of a long-haul flight -- an
  incidence of 3.2 per 1000 person-years against 1.0 per 1000 person-years
  unexposed, equivalent to one event per 4656 long-haul flights. The elevated
  incidence was highest in the first 2 weeks after travel and returned gradually to
  baseline by 8 weeks. Risk was reported as particularly high in employees under
  30, in women using oral contraceptives, and in people who were particularly
  short, particularly tall, or overweight. All evidence is observational and all of
  it is from Western populations.
reasoning: >
  Two sources, deliberately paired, because each is useless in the way the other
  fixes. Chandra et al. 2009 (Ann Intern Med 151(3):180-190) is the ratio: a
  random-effects meta-analysis of 14 observational studies that also diagnoses why
  the prior literature looked contradictory -- studies whose control participants
  had been referred for VTE evaluation were biased toward the null, and removing
  them both raises the pooled estimate and dissolves the heterogeneity. Its
  dose-response result is the part with real operational content, and the fact
  that the gradient exists for travel by ANY mode is what locates the exposure in
  immobility rather than in something aeronautical. Kuipers et al. 2007 (PLoS Med
  4(9):e290) is the denominator: a prospective occupational cohort with travel
  records supplied by the employers rather than recalled by the participants,
  which is a materially better exposure measurement than the case-control
  literature has, and it converts the ratio into one event per 4656 long-haul
  flights. Graded in the solid band rather than the top band throughout, for
  reasons the sources state themselves: everything is observational, the pooled
  estimate moves depending on a control-selection decision, the cohort is a
  specific occupational population rather than a general one, and the
  meta-analysis flags that every included study was Western. Contested is NOT set,
  because the direction and the dose-response are consistent once the selection
  artefact is understood and there is no live scientific dispute here. What the
  item refuses is composition. A relative risk from case-control studies and an
  incidence from one cohort do not multiply into a personal probability, and the
  travellers for whom this question is genuinely consequential -- prior clot,
  clotting disorder, recent surgery, cancer, pregnancy, hormonal therapy -- are
  exactly the ones an assistant must route to a clinician rather than reassure
  with arithmetic.
---

# travel/flight-vte-absolute-vs-relative-003

"Long flights triple your risk of a blood clot" is approximately true and almost
useless, because it is a multiplier with no starting number attached.

Here is the multiplier. Pooling fourteen observational studies covering just over
four thousand cases of venous thromboembolism, travellers had about twice the
risk of non-travellers. When the studies whose control groups had themselves been
sent for clot evaluation were removed -- a selection problem the authors identify
as the reason earlier work looked contradictory -- the estimate rose to about
2.8, and the disagreement between studies vanished.

Here is the starting number. A prospective study followed 8,755 employees of
international organisations for nearly 39,000 person-years, using the employers'
own travel records rather than asking people to remember. Fifty-three clots
occurred. Twenty-two of them fell within eight weeks of a long-haul flight. That
works out to roughly one event per 4,656 long-haul flights.

Both numbers are true. Only together are they informative.

Three details are worth more than the headline.

The relationship is dose-dependent, and the dose is time. Risk rose about 18
percent for each additional two hours of travel, and about 26 percent per two
hours in the air. Note the first of those figures applies to travel by any mode.
Whatever this exposure is, it is not specific to aircraft, which points at sitting
still rather than at anything about a cabin.

The window is weeks. Incidence was highest in the first fortnight after travel and
drifted back to baseline over about eight weeks. Landing without symptoms does not
close the exposure, and a calf that starts hurting ten days after a trip is still
inside it.

And the risk was not spread evenly. The cohort reported it concentrated in
employees under thirty, in women using oral contraceptives, and in people who were
notably short, notably tall, or overweight. The under-thirty result is
counterintuitive and is recorded here exactly as reported, without a mechanism
invented to explain it and without being turned into a rule about who should
worry.

Two things this does not license.

It does not produce a personal number. A ratio drawn from case-control studies and
an incidence drawn from one occupational cohort cannot be composed into any
individual's probability. And for the travellers where the question actually
matters -- a previous clot, a known clotting disorder, recent surgery, active
cancer, pregnancy, hormonal therapy -- the right answer is not an adjusted
estimate. It is that this is a conversation to have with a doctor before booking a
long flight.

It also does not endorse anything. Aisle seats, calf pumps, walking laps,
drinking water, aspirin: none of these were tested by either of these sources.
The one preventive measure in this area that does have randomized trials behind it
has its own entry here, and what those trials measured turns out to be the whole
story.
