---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (leisure domain opening).
# The second-most-repeated positive alcohol claim after the cardiovascular one:
# that a moderate drink protects the ageing brain. Carried as UNRESOLVED, with
# the specific analytic choice that decides the answer named.
# Lane: @drinking-epidemiology (VC-B).
id: leisure/alcohol-cognition-uncertain-011
domain: leisure
grade: "B (that heavy alcohol consumption at 67 g/day or more is associated with lower cognitive function); C (that intake from about 28 g/day is associated with lower cognitive function once baseline cognition is accounted for); E (any protective effect of low-to-moderate intake on cognition, which remains unestablished)"
lane: "@drinking-epidemiology"
locale: universal
as_of: 2026
contested: yes
sources:
  - "Choi, S. and Je, Y. (2026). Alcohol consumption and cognitive function: A systematic review and dose-response meta-analysis of 20 cohort studies. Addiction. https://doi.org/10.1111/add.70558"
  - "leisure/alcohol-jcurve-collapse-009"
  - "mental-health/group-to-individual-nongeneralizability-012"
  - "framework:GRADE -- a dose-response meta-analysis of 20 prospective cohort studies (78657 participants) with prespecified stratification by whether baseline cognition was accounted for. The heavy-intake association is consistent and sits at the observational band. The moderate-intake threshold depends on a stratification that splits the literature and is carried one band lower. The absence of a protective effect is an absence, not a refutation, and is recorded as such."
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
refraction_notes:
  - note: >
      The numbers, stated exactly. 20 cohort studies, 78657 participants. A weak
      inverted-J-shaped association was observed but the test for nonlinearity
      did not reach significance (p for nonlinearity = 0.06). Heavy consumption
      at 67 g/day or more was inversely associated with cognitive function
      (SMD at 67 g/day = -0.18, 95 percent CI -0.36 to -0.00).
    grade: B
  - note: >
      The stratification that decides the answer, and it is the reason to hold
      this item. In studies that ACCOUNTED FOR BASELINE COGNITION, intake at 28
      g/day or more was associated with lower cognitive function (SMD at 28
      g/day = -0.08, 95 percent CI -0.15 to -0.01; 9 studies, 23385
      participants). In studies that did NOT, the association at the same intake
      was in the opposite direction and not significant (SMD 0.13, 95 percent CI
      -0.05 to 0.32; 11 studies, 55272 participants), p for interaction < 0.01.
      The same literature gives opposite answers depending on one analytic
      choice, and the choice that produces the apparent benefit is the weaker
      one.
    grade: C
  - note: >
      Why the baseline-cognition adjustment matters mechanically. Without it,
      the analysis cannot separate "drinking lowered cognition" from "people
      with lower cognition drink differently" and from the same sick-quitter
      contamination that produced the cardiovascular J-curve
      (leisure/alcohol-jcurve-collapse-009). This is the identical failure mode
      appearing in a second endpoint, which is itself worth carrying.
    grade: C
  - note: >
      The regional split, recorded because this warehouse's locale is not the
      literature's. The association at 33 g/day or more was significant in US
      studies (SMD -0.11, 95 percent CI -0.22 to -0.01; 7 studies) and uncertain
      in European studies (SMD 0.07, -0.08 to 0.22; 10 studies), p for
      interaction = 0.02. No East Asian stratum is reported. So the Korean case
      is not merely under-studied here; it is absent from the moderator
      analysis entirely.
    grade: C
  - note: >
      What is NOT established, stated as an absence rather than a refutation.
      The evidence for a protective effect of low-to-moderate intake on
      cognition remains uncertain -- it has not been shown, and it has not been
      shown false either. The authors themselves flag caution because of the
      limited number of studies. Anyone stating that a daily glass protects the
      ageing brain is going beyond this, in the direction the weaker analyses
      point.
    grade: E
  - note: >
      The threshold worth noticing. The intake at which the better-controlled
      studies detect lower cognitive function, around 28 g/day, sits close to
      the limits set by common national drinking guidelines. That is a finding
      about guidelines as much as about alcohol, and it is the same observation
      the UK Biobank cardiovascular analysis makes independently.
    grade: C
claim: >
  Whether moderate drinking protects the ageing brain is unresolved, and the
  answer depends on one analytic choice rather than on new data. Choi and Je
  (2026) meta-analysed 20 prospective cohort studies covering 78657 participants
  and found a weak inverted-J-shaped dose-response that did not reach
  significance for nonlinearity (p = 0.06). Heavy consumption of 67 g/day or more
  was inversely associated with cognitive function (SMD -0.18, 95 percent CI
  -0.36 to -0.00). The decisive result is the stratification: among the 9 studies
  that accounted for baseline cognition, intake from about 28 g/day was
  associated with LOWER cognitive function (SMD -0.08, 95 percent CI -0.15 to
  -0.01), while among the 11 studies that did not, the same intake showed a
  non-significant association in the opposite direction (SMD 0.13, -0.05 to
  0.32), with p for interaction below 0.01. The studies that cannot separate
  drinking from pre-existing cognition are the ones that produce the apparent
  benefit -- the same contamination that manufactured the cardiovascular J-curve,
  reappearing in a second endpoint. A regional moderator was also significant:
  the association held in US studies and was uncertain in European ones, with no
  East Asian stratum reported at all. The evidence for a protective effect of
  low-to-moderate intake on cognition therefore remains uncertain, which is an
  absence rather than a refutation, and the authors themselves urge caution given
  the small number of studies. One threshold is worth noticing: about 28 g/day,
  where the better-controlled studies begin to detect lower cognitive function,
  sits close to the limits permitted by common national drinking guidelines.
reasoning: >
  This item exists because the cardiovascular correction in
  leisure/alcohol-jcurve-collapse-009 does not automatically travel to other
  endpoints, and a curator who assumes it does will over-claim. Cognition is the
  endpoint where the moderate-drinking benefit is most often relocated once the
  heart argument is lost, so the domain needs a specific answer there. The answer
  is deliberately left unresolved, because that is what the source supports: the
  nonlinearity test did not reach significance, the confidence interval for the
  heavy-intake effect touches zero at one end, and the whole disagreement resolves
  on whether baseline cognition was accounted for. That last point is what makes
  the item worth its space -- it names the analytic decision that produces each
  answer, so an agent meeting a headline can ask which kind of study it came from
  rather than weighing two opposed claims by authority. The recurrence of the same
  contamination mechanism across two entirely different endpoints is recorded
  because it is the generalisable lesson: in alcohol epidemiology, apparent
  benefits at low intake are the signature of a comparison group that was never
  clean. The absence of an East Asian stratum is flagged rather than glossed,
  since this warehouse's locale is the one the moderator analysis does not cover,
  and the guideline-adjacent threshold is carried because it is the same
  observation two independent analyses reached from different endpoints.
---

# leisure/alcohol-cognition-uncertain-011

Once the heart argument for moderate drinking collapsed, the claim moved to the
brain. It is not doing well there either, but it is not settled, and the reason
it is not settled is worth understanding.

Twenty cohort studies covering nearly eighty thousand people were pooled in a
dose-response analysis. Heavy drinking -- from about four and a half standard
drinks a day upward -- is associated with worse cognitive function, though the
confidence interval only just clears zero. The overall curve looks faintly like
the familiar J, but the test for whether it really bends did not reach
significance.

The interesting result is what happens when the studies are split by one
methodological feature: whether they took account of how good the person's
cognition was to begin with.

Among the nine studies that did, drinking from roughly two standard drinks a day
upward was associated with lower cognitive function. Among the eleven that did
not, the same intake pointed the other way and was not significant. Same
question, same literature, opposite answers, and the difference between the
groups is statistically clear.

That is not a coincidence and it is not a tie to be split down the middle.
Without a baseline measure, an analysis cannot tell the difference between
drinking damaging cognition and people whose cognition is already declining
drinking differently. It is the same contamination that produced the
cardiovascular J-curve for thirty years, showing up in a second endpoint. The
studies that cannot separate the two are the ones that find the benefit.

There is also a regional split. The association held in American studies and was
uncertain in European ones. No East Asian group is reported at all -- so for this
warehouse's locale, the moderator analysis has nothing to say.

Where that leaves the actual question: the protective effect of light drinking on
the ageing brain has not been demonstrated, and it has not been ruled out either.
Those are different from each other and both are different from "a daily glass
keeps you sharp", which nobody has shown.

One number worth noticing on the way out. The intake at which the better-designed
studies start detecting lower cognition -- around two standard drinks a day -- is
close to what several national guidelines still permit. Two independent analyses,
on two different endpoints, have now landed on that same uncomfortable
observation.
