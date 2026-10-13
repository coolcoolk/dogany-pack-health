---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02, HOME-DOMAIN OPENING SPRINT
# (marker: home-lane-opening-001-013). This is the anchor item of the
# @home-environment lane: the one part of the household-knowledge area with a
# genuinely strong evidence base. No applicability.axes -- the axes ledger
# carries no housing/dwelling axis and this sprint does not invent one.
id: home/dampness-mould-respiratory-001
domain: home
lane: "@home-environment"
grade: B
locale: universal
as_of: 2007-2009
contested: no
sources:
  - "https://www.ncbi.nlm.nih.gov/books/NBK143943/"  # WHO Guidelines for Indoor Air Quality: Dampness and Mould (2009), Executive summary, read at source 2026-09-02
  - "https://doi.org/10.1111/j.1600-0668.2007.00475.x"  # Fisk WJ, Lei-Gomez Q, Mendell MJ. Meta-analyses of the associations of respiratory health effects with dampness and mold in homes. Indoor Air 2007;17(4):284-296. PMID 17661925
  - "source:home/mould-no-exposure-threshold-002"  # within-warehouse cross-ref: the same WHO document is ALSO the reason no measurable mould threshold exists, which is what makes visible dampness the operative signal
claim: >
  Persistent dampness and visible mould growth in a dwelling is one of the few
  household-environment exposures with a converged evidence base. WHO (2009)
  states that sufficient epidemiological evidence is available, from studies in
  different countries and different climates, that occupants of damp or mouldy
  buildings are at increased risk of respiratory symptoms, respiratory
  infections and exacerbation of asthma. The quantitative size of that
  association, pooled by Fisk 2007 across the studies the US Institute of
  Medicine had reviewed plus related work, is central odds-ratio estimates of
  1.34 to 1.75 across ten respiratory and asthma-related outcomes, with the 95
  percent interval excluding 1.0 in nine of ten and the lower bound above 1.2 in
  most -- summarised by the authors as roughly 30 to 50 percent increases. The
  actionable form is WHO's own: persistent dampness and microbial growth on
  interior surfaces and in building structures should be avoided or minimised,
  and where they occur they should be remediated. Direction of effect and rough
  magnitude are solid. Everything downstream of that -- which mould, how much
  mould, what number counts as safe -- is not, and is handled by item 002.
reasoning: >
  Two mutually reinforcing sources at different tiers. The WHO 2009 guideline is
  a formal evidence-review-and-recommendation document from an international
  health authority, and its language is deliberately graded: sufficient
  epidemiological evidence for respiratory symptoms, respiratory infections and
  asthma exacerbation; only some evidence for allergic rhinitis and asthma
  onset; clinical evidence for rarer conditions such as hypersensitivity
  pneumonitis and allergic fungal sinusitis. Fisk 2007 supplies the pooled
  numbers under random-effects models on log odds ratios, accounting for
  correlation between multiple results within a study. Both are read at the
  primary document, not through a secondary write-up. The grade is set one step
  below the top because the underlying epidemiology is dominated by
  cross-sectional and cohort designs with self-reported or inspector-assessed
  dampness, not randomised remediation trials -- WHO itself notes that few
  intervention studies were available, though those that exist show remediation
  reduces adverse outcomes. That is a real limit on causal strength, and it is
  why this ships as a strong association with a plausible and endorsed
  intervention rather than as an established causal dose-response.
---

# home/dampness-mould-respiratory-001

If there is one thing in the whole household-environment area that is worth
acting on without hedging, it is persistent damp.

WHO's 2009 indoor air quality guideline concluded that the epidemiological
evidence is sufficient -- across different countries and different climates --
that people living or working in damp or mouldy buildings have more respiratory
symptoms, more respiratory infections, and more asthma exacerbations. That is a
strong statement by the standards of an organisation that is normally very
careful about causal language, and it was made about buildings generally, not
about one climate or one construction type.

Fisk and colleagues put numbers on it two years earlier, pooling the studies the
US Institute of Medicine had reviewed plus related work. Across ten different
respiratory and asthma-related outcomes, the central odds ratios landed between
1.34 and 1.75. Nine of the ten confidence intervals excluded 1.0, and in most
cases the lower bound sat above 1.2. The authors' own summary sentence is the
one worth carrying: building dampness and mould are associated with roughly 30
to 50 percent increases in a variety of respiratory and asthma-related health
outcomes.

The practical instruction follows directly, and again it is WHO's own wording:
persistent dampness and microbial growth on interior surfaces and inside
building structures should be avoided or minimised, and where they occur they
should be remediated.

Two honest limits.

First, this is association, not a randomised demonstration. The evidence base is
cross-sectional and cohort work where dampness was self-reported or assessed by
inspection. WHO notes that few intervention studies were available. The ones
that existed pointed the right way -- remediating dampness reduced adverse
outcomes -- but there is no large trial of "fix the damp, measure the asthma."
So the direction is trustworthy and the magnitude is roughly right; a precise
causal effect size is not on offer.

Second, and this is the part that gets abused commercially: none of this
licenses a number. There is no measured level of mould that separates a safe
home from an unsafe one. That is not an oversight in this item; it is WHO's
explicit position, and it is important enough to carry its own entry -- see item
002.
