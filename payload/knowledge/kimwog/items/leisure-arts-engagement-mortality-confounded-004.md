---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (leisure domain opening).
# The arts-and-wellbeing headline a life agent is most likely to meet. Carried
# CONTESTED rather than shipped as a benefit, and carried with its published
# critique attached. Lane: @cultural-life (VC-C).
id: leisure/arts-engagement-mortality-confounded-004
domain: leisure
grade: "B (that frequent receptive arts engagement is ASSOCIATED with lower all-cause mortality in this cohort at the stated magnitude); D (any causal reading, i.e. that going to more exhibitions extends life)"
lane: "@cultural-life"
locale: universal
as_of: 2019-2020
contested: yes
sources:
  - "Fancourt, D. and Steptoe, A. (2019). The art of life and death: 14 year follow-up analyses of associations between arts engagement and mortality in the English Longitudinal Study of Ageing. BMJ 367, l6377. https://doi.org/10.1136/bmj.l6377"
  - "Wright, L. (2020). Arts engagement, mortality and dementia: what can the data say? Journal of Epidemiology and Community Health 74(9), 764. https://doi.org/10.1136/jech-2020-214227"
  - "mental-health/group-to-individual-nongeneralizability-012"
  - "framework:GRADE -- a large well-conducted prospective cohort (n = 6710, 14-year follow-up, register-linked mortality) with extensive covariate adjustment. Observational design caps the association at the observational band and any causal reading at the practitioner floor. A published critique in a peer-reviewed epidemiology journal is what moves the contested flag, not this curator's discomfort with the effect size."
applicability:
  axes:
    # The cohort is 50+. Below that age the estimate is out of sample entirely,
    # which is a hedge, not a safety gate -- nothing here can hurt anyone.
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The numbers, stated exactly. English Longitudinal Study of Ageing, 6710
      community-dwelling adults aged 50 and over (53.6 percent women, mean age
      65.9, SD 9.4), baseline 2004-05, mortality by linkage to the NHS central
      register over 14 years. Infrequent receptive arts engagement (once or
      twice a year) versus never: hazard ratio 0.86 (95 percent CI 0.77 to
      0.96). Frequent engagement (every few months or more) versus never: 0.69
      (0.59 to 0.80), after adjustment for demographic, socioeconomic,
      health-related, behavioural and social factors.
    grade: B
  - note: >
      Read the exposure literally before reading the effect. "Receptive arts
      engagement" here means going to museums, art galleries, exhibitions, the
      theatre, concerts or the opera, self-reported. It is a going-out variable
      in over-50s. Whatever else it measures, it measures being well enough,
      mobile enough, moneyed enough and socially connected enough to leave the
      house for a discretionary reason.
    grade: B
  - note: >
      Why this cannot be spoken as a benefit. A 31 percent reduction in
      all-cause mortality is a very large effect for a discretionary leisure
      behaviour -- of an order normally reserved for major clinical exposures --
      which is itself evidence that the estimate is carrying confounding the
      adjustments did not remove. Reverse causation is the obvious mechanism:
      undiagnosed or early-stage illness stops people going out years before it
      kills them. The paper's own results section states that the study was
      observational and so causality cannot be assumed.
    grade: D
  - note: >
      The contested flag is anchored in the literature, not in taste. A
      commentary in the Journal of Epidemiology and Community Health (Wright
      2020) responded specifically to this paper on what the data can and cannot
      support. Carry the finding WITH the objection attached; a curator who
      cites the hazard ratio without it is quoting half a conversation.
    grade: B
  - note: >
      PUBLICATION CONTEXT, disclosed because it changes how the paper should be
      read. This article appeared in the BMJ's Christmas issue, under the
      heading "Christmas 2019: For Art's Sake". The Christmas issue publishes
      genuine peer-reviewed research with a deliberately light editorial framing
      and is not the venue the same authors would use for a definitive causal
      claim. This is not a reason to dismiss the analysis; it IS a reason not to
      treat its headline as a public-health conclusion.
    grade: B
claim: >
  Going to museums, galleries, theatre, concerts or the opera is associated with
  lower mortality in older adults, and the association is almost certainly not a
  benefit of the activity. Fancourt and Steptoe (2019), following 6710
  community-dwelling English adults aged 50 and over for 14 years with
  register-linked mortality, report a hazard ratio of 0.86 (95 percent CI 0.77 to
  0.96) for engaging once or twice a year and 0.69 (0.59 to 0.80) for engaging
  every few months or more, compared with never, after adjustment for
  demographic, socioeconomic, health-related, behavioural and social factors, and
  robust to a range of sensitivity analyses. Three things must be carried with
  that number. The exposure is self-reported going-out behaviour in over-50s, so
  it necessarily encodes health, mobility, money and social connection. A 31
  percent reduction in all-cause mortality is implausibly large for a
  discretionary leisure behaviour and is the size one expects when residual
  confounding and reverse causation -- early illness suppressing outings years
  before death -- remain in the estimate. And the paper says in its own results
  that causality cannot be assumed. A commentary in the Journal of Epidemiology
  and Community Health (Wright 2020) engaged the paper directly on what the data
  can support. The article was published in the BMJ Christmas issue.
reasoning: >
  This item exists because a life agent working in the leisure domain will meet
  this headline, in the form "going to the theatre cuts your risk of dying by a
  third", and needs something better than either repeating it or waving it away.
  The association is carried at the observational band because it is a large,
  well-conducted, register-linked cohort and the association is real in the data.
  The causal reading is pushed all the way to the practitioner floor and the item
  is flagged contested, for reasons that are specific rather than reflexive: the
  exposure is a proxy for general capacity to leave the house, the effect size is
  out of scale with the exposure, reverse causation has an obvious and unmeasured
  path, and a peer-reviewed commentary has already challenged what the data can
  say. The Christmas-issue placement is disclosed because it is a fact about the
  publication that a reader is entitled to and would not otherwise learn from the
  citation, and because it explains the gap between the paper's headline framing
  and its own causal caveat. The generalisable rule this item anchors for the
  whole domain: in leisure epidemiology the exposure is almost always a proxy for
  being well, so an effect size that looks too good for the activity is evidence
  about the study design, not about the activity.
---

# leisure/arts-engagement-mortality-confounded-004

Older adults who go to exhibitions, concerts and the theatre die at lower rates
than those who never do. That much is in the data. Almost everything people do
with the finding afterwards is wrong.

The study followed six thousand seven hundred and ten English adults aged fifty
and over for fourteen years, with deaths taken from the national register rather
than from self-report. Going once or twice a year was associated with a 14
percent lower risk of dying during follow-up. Going every few months or more was
associated with a 31 percent lower risk. Both survived adjustment for income,
education, health, health behaviours and social contact, and both survived a
range of sensitivity checks.

Now look at what the exposure actually is. It is a self-reported answer to how
often you leave the house to go somewhere cultural. In people over fifty, that
answer is downstream of whether you can walk comfortably, whether you can afford
a ticket, whether anyone will come with you, and whether you feel well enough to
plan an evening out three weeks ahead.

And look at the size. A third off all-cause mortality is the kind of number
attached to major clinical exposures. For an optional evening at the opera, it is
not a plausible causal magnitude. When an effect is too large for its cause, the
right inference is usually about the study, not the world. The most likely
mechanism here is the ordinary one: illness that has not yet been diagnosed stops
people going out years before it kills them, and no amount of baseline adjustment
catches an illness nobody has noticed.

The paper says as much itself -- it states in its own results that this was
observational and causality cannot be assumed -- and a commentary in an
epidemiology journal took the question up directly afterwards. It is also worth
knowing where it appeared: the BMJ's Christmas issue, which carries real
peer-reviewed research in a deliberately lighter frame.

The rule to take away from this one and apply to the rest of the domain: in
leisure research the exposure is nearly always a proxy for being well enough to
do the thing. So an effect size that looks too good for the activity is telling
you about the design.
