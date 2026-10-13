---
# Collection sprint 2026-09-02 (mental-health lane expansion). The self-help
# item. Gratitude journals and positive-psychology exercises are the single most
# likely thing a well-meaning life agent would suggest, and they are the clearest
# case in this lane of an effect that exists against doing nothing and vanishes
# against doing something else. This is the domain's existing comparator-
# dependence rule (item 004) with a second, cleaner worked example. It also
# carries a live MISATTRIBUTION catch: the d = 0.31 versus d = -0.03 pair that
# circulates as "the gratitude meta-analysis" belongs to Davis et al. 2016 and is
# QUOTED inside Cregg and Cheavens, not produced by it.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/wellbeing-exercise-comparator-collapse-017
domain: mental-health
grade: "A (that positive-psychology and gratitude interventions show small effects against passive controls and trivial-to-null effects against active controls); D (any claim that a specific wellbeing exercise produces a specific benefit)"
lane: "@clinical"
locale: universal
as_of: 2019-2021
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/31141537/"  # White CA, Uttl B, Holder MD. 2019, PLoS One 14(5):e0216588, doi 10.1371/journal.pone.0216588, PMCID PMC6541265 -- reanalysis and replication of the two most-cited positive-psychology-intervention meta-analyses, correcting for small sample size bias
  - "https://doi.org/10.1007/s10902-020-00236-6"  # Cregg DR, Cheavens JS. 2021, J Happiness Stud 22(1):413-445 -- meta-analysis of gratitude interventions, k=27, N=3675, read at publisher full text
  - "https://doi.org/10.1037/cou0000107"  # Davis DE et al. 2016, J Couns Psychol 63(1):20-31 -- the ORIGINAL source of the d = 0.31 (measurement-only control) versus d = -0.03 (psychologically active comparison) figures that are widely misattributed to later reviews
  - "mental-health/cbt-gad-comparator-004"  # the domain's existing comparator-dependence worked example; this is the second one
  - "relationships-communication/source-misattribution-rule-005"  # the rule this item's misattribution catch instantiates
  - "framework:GRADE -- two independent lines converge here: a reanalysis showing the field's headline effects shrink to about r = 0.10 once small-sample bias is accounted for, and a focused meta-analysis showing the residual effect is comparator-dependent. Convergence across independent reanalyses is what the domain's no-single-hierarchy rule asks for."
refraction_notes:
  - note: >
      The whole-field reanalysis, stated exactly. The two most-cited
      positive-psychology-intervention meta-analyses disagreed with each other
      before anyone reanalysed them: Sin and Lyubomirsky 2009 reported r = 0.29 for
      wellbeing and r = 0.31 for depression, Bolier et al. 2013 reported r = 0.17
      for subjective wellbeing, r = 0.10 for psychological wellbeing and r = 0.11
      for depression. White, Uttl and Holder 2019 reanalysed both, found many
      primary studies used small samples and that small sample size bias was
      pronounced, and reported that once it was accounted for the effect on
      wellbeing was SMALL BUT SIGNIFICANT at approximately r = 0.10, while the
      effect on depression was VARIABLE, DEPENDENT ON OUTLIERS, and GENERALLY NOT
      STATISTICALLY SIGNIFICANT.
    grade: A
  - note: >
      The gratitude case, stated exactly, because it is the specific exercise most
      likely to be suggested. Cregg and Cheavens 2021 (k=27, N=3675) found a small
      overall effect on depression and anxiety symptoms at post-test (g = -0.29,
      SE 0.06) and follow-up (g = -0.23, SE 0.06). Moderation by control type is
      the finding: at post-test the pooled effect was g = -0.51 (SE 0.15) against
      WAITLIST controls (k=9) but only g = -0.18 (SE 0.06) against ACTIVE controls
      (k=18); at follow-up, g = -0.63 (SE 0.13) waitlist (k=3) versus g = -0.16 (SE
      0.05) active (k=10). No other moderator was consistently significant --
      including risk of bias, symptom severity, and type of intervention.
    grade: A
  - note: >
      MISATTRIBUTION CATCH, and it is a live one. The figures "d = 0.31 for a
      measurement-only control down to d = -0.03 for a psychologically active
      comparison" circulate as the result of the gratitude meta-analysis. They are
      not. They are Davis et al. 2016 (J Couns Psychol 63:20-31), quoted inside
      Cregg and Cheavens' introduction as prior work. Anyone citing the 2021 paper
      for those numbers has attributed a result to the wrong study. Same failure
      mode the relationships-communication domain keeps a standing rule for.
    grade: A
  - note: >
      The authors' own conclusion, which is stronger than the numbers alone and
      should be quoted rather than softened. Cregg and Cheavens write that they
      agree with Davis et al. that "a parsimonious explanation of gratitude
      interventions may be that they operate primarily through placebo effects, at
      least for depression and anxiety symptoms", and recommend that people
      seeking to reduce those symptoms engage instead in interventions with
      stronger evidence of efficacy.
    grade: A
  - note: >
      One internal check worth carrying, because it cuts the other way and should
      not be hidden. Cregg and Cheavens computed fail-safe N values well above the
      standard guideline, concluding the pooled effects are unlikely to be an
      artefact of unpublished null studies. Their cumulative meta-analyses did show
      a trend toward larger effects in smaller samples at post-test. So the
      residual effect is probably not purely a file-drawer artefact -- it is just
      small, and it mostly disappears when the comparison group also does
      something.
    grade: A
  - note: >
      Operational consequence, stated as a constraint rather than a prohibition.
      Nothing here says a gratitude exercise is harmful or that someone who finds
      it useful should stop. What it forbids is the claim: an assistant may not
      present a wellbeing exercise as evidence-backed for reducing depressive or
      anxiety symptoms, because against any comparison activity the measured
      effect is close to zero, and the field's own reviewers describe the
      parsimonious explanation as placebo.
    grade: A
claim: >
  Positive-psychology wellbeing exercises show small effects against doing
  nothing and trivial-to-null effects against doing something else, and the
  field's headline figures shrink substantially under reanalysis. White, Uttl and
  Holder 2019 (PLOS ONE) reanalysed the two most-cited meta-analyses in the area
  -- which already disagreed with each other, at r = 0.29 and r = 0.31 (Sin and
  Lyubomirsky 2009) versus r = 0.17, r = 0.10 and r = 0.11 (Bolier et al. 2013) --
  found small sample size bias pronounced across many analyses, and reported that
  once it was accounted for the effect on wellbeing was approximately r = 0.10
  while the effect on depression was variable, outlier-dependent and generally not
  statistically significant. On gratitude specifically, Cregg and Cheavens 2021
  (Journal of Happiness Studies, k=27, N=3675) found small overall effects on
  depression and anxiety symptoms (g = -0.29 post-test, -0.23 at follow-up) that
  were strongly moderated by control type: g = -0.51 against waitlist controls
  versus g = -0.18 against active controls at post-test, and -0.63 versus -0.16 at
  follow-up. No other moderator was consistently significant. The authors conclude
  that a parsimonious explanation is that these interventions operate primarily
  through placebo effects for depression and anxiety symptoms, and recommend
  interventions with stronger evidence instead. MISATTRIBUTION CATCH: the
  widely-quoted "d = 0.31 down to d = -0.03" pair is Davis et al. 2016 (Journal of
  Counseling Psychology 63:20-31), quoted inside the 2021 paper's introduction,
  and is routinely credited to the wrong study. Operative rule: an assistant may
  not present a wellbeing exercise as evidence-backed for reducing symptoms; that
  it is harmless and that someone may enjoy it are separate and unaffected claims.
reasoning: >
  If a generalist assistant ever volunteers a mental-health intervention
  unprompted, this is the one it will volunteer -- a gratitude list, a
  three-good-things exercise, a wellbeing prompt -- because they are free,
  harmless-seeming and culturally ubiquitous. So the lane needs a sourced answer
  about what they do. Two independent lines were used deliberately rather than
  one. The White et al. reanalysis addresses the WHOLE field and shows that its
  two flagship meta-analyses disagreed with each other and both shrank once
  small-sample bias was handled, which is a methodological finding about the
  literature. Cregg and Cheavens addresses one intervention in depth and shows
  the residual effect is almost entirely comparator-driven, which is a finding
  about the effect. Convergence between an independent reanalysis and a focused
  meta-analysis is exactly what the domain's no-single-hierarchy rule asks for
  before a top band is used, which is why this is graded above the domain's
  mindfulness item despite being the same kind of claim. The misattribution catch
  was found by reading the 2021 paper's full text rather than its abstract: the
  d = 0.31 versus -0.03 pair that circulates as its result sits in its
  introduction as a citation of Davis et al. 2016. That is precisely the failure
  mode the relationships-communication domain maintains a standing rule for, and
  recording it here means a later sprint meeting those numbers can attribute them
  correctly. The fail-safe N note is carried because it cuts against the item's
  own direction and omitting it would be selective: the residual small effect
  survives a publication-bias check, so the honest statement is that the effect
  is small and comparator-dependent, not that it is fabricated. Not flagged
  contested: the two sources agree with each other and with the earlier reviews
  they reanalyse, and the authors of the focused meta-analysis reach the
  sceptical conclusion themselves.
---

# mental-health/wellbeing-exercise-comparator-collapse-017

If something like this ever suggests a mental-health intervention on its own
initiative, it will suggest a gratitude list. So it is worth knowing what those
do.

Two separate lines of evidence, and they point the same way.

The first is about the whole field. The two most-cited meta-analyses of
positive-psychology interventions did not agree with each other in the first
place -- one reported correlations around 0.29 and 0.31 for wellbeing and
depression, the other around 0.17, 0.10 and 0.11. A later team reanalysed both,
found that many of the underlying studies had small samples and that small-sample
bias was pronounced, and reported that once that was handled, the effect on
wellbeing came out at about 0.10 -- small but real -- while the effect on
depression was variable, driven by outliers, and generally not statistically
significant at all.

The second is about gratitude specifically. Twenty-seven studies, over three and
a half thousand participants. The overall effect on depression and anxiety
symptoms was small: about a third of a standard deviation at post-test, a bit
less at follow-up.

And then the moderation, which is the actual finding. Against a waitlist -- people
who did nothing and just filled in the questionnaires -- the effect was about half
a standard deviation. Against an active control -- people who did some other
matched activity for the same amount of time -- it was about a sixth. At follow-up
the split was starker still: roughly two thirds of a standard deviation against
waitlist, roughly a sixth against activity.

Nothing else moderated it. Not risk of bias, not how depressed people were at
baseline, not which kind of gratitude exercise was used.

The authors' own reading, which is more direct than most: the parsimonious
explanation is that these interventions work primarily through placebo, at least
for depression and anxiety symptoms, and people trying to reduce those symptoms
should use something with better evidence behind it.

One correction that has to travel with this, because it is currently circulating
wrong. The figures that get quoted as the punchline of the gratitude
meta-analysis -- an effect of 0.31 against a measurement-only control falling to
minus 0.03 against a psychologically active one -- are not from that paper. They
are from an earlier 2016 review, quoted in the 2021 paper's introduction. The
numbers are real and the attribution is wrong, and this warehouse keeps a
standing rule about exactly that mistake.

One thing that cuts the other way, kept because leaving it out would be
selective. The gratitude reviewers ran publication-bias checks and concluded the
small residual effect is probably not just a file-drawer artefact. So the honest
verdict is not that nothing happens. It is that something small happens, and
almost all of it also happens if you do some other structured activity for the
same twenty minutes.

Which sets the constraint precisely. Nobody should stop keeping a gratitude
journal because of this, and there is no evidence it does harm. What cannot be
said is that it is evidence-backed for feeling better -- because against any
comparison that involves doing something, the measured difference is close to
nothing, and the people who ran the numbers say the simplest explanation is
placebo.
