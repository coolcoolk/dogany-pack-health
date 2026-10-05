---
# Collection sprint 2026-09-02 (mental-health lane expansion). The workload item.
# A life agent sees hours and blocks, so the two questions it can actually reach
# are (a) does the amount of work relate to mood, and (b) does what happens
# AFTER work relate to mood. Both are answered here from large primary
# syntheses, and both come out weaker and more conditional than the popular
# version. The long-hours effect is also the lane's clearest WEIRD-sampling
# warning: it is region-dependent, and the Asian estimate is several times the
# European one and the opposite sign of the North American one.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/workload-detachment-recovery-016
domain: mental-health
grade: "B (that psychological detachment from work correlates moderately with lower exhaustion and fatigue and better wellbeing, cross-sectionally); C (that long working hours are associated with onset of depressive symptoms, at a small overall magnitude with strong regional variation); D (any causal or directional reading of either)"
lane: "@clinical"
locale: universal
as_of: 2017-2018
contested: yes
sources:
  - "https://doi.org/10.3389/fpsyg.2016.02072"  # Wendsche J, Lohmann-Haislah A. 2017, Front Psychol 7:2072 -- meta-analysis on antecedents and outcomes of detachment from work, 86 publications, k=91 independent study samples, N=38124 employees
  - "https://pubmed.ncbi.nlm.nih.gov/29423526/"  # Virtanen M, Jokela M, Madsen IE, Magnusson Hanson LL, Lallukka T, Nyberg ST, Alfredsson L, Batty GD, et al. 2018, Scand J Work Environ Health 44(3):239-250, doi 10.5271/sjweh.3712 -- systematic review and meta-analysis combining 10 published cohort studies with unpublished individual-participant data from 18 cohorts, 189729 participants from 35 countries, 21747 new-onset cases
  - "mental-health/burnout-definition-bound-015"  # why the outcome in this area must be described in observable terms rather than labelled
  - "mental-health/kr-help-seeking-service-use-020"  # the locale item this one's regional finding points at
  - "framework:GRADE -- both sources are large and well conducted and both are OBSERVATIONAL. The detachment meta-analysis pools correlations, most of them cross-sectional, so direction of effect is not identified. The working-hours meta-analysis is prospective and pools onset, which is stronger, but remains observational with significant heterogeneity."
refraction_notes:
  - note: >
      Detachment, stated exactly. Across 86 publications, 91 independent samples
      and 38124 employees, psychological detachment from work correlated
      NEGATIVELY with job demands (r = -0.25, k=60, N=28507; quantitative demands
      specifically r = -0.28) and with exhaustion (r = -0.36, k=23, N=7007) and
      fatigue (r = -0.42, k=17, N=12510), and POSITIVELY with general wellbeing
      (r = 0.32, k=16, N=11133), life satisfaction (r = 0.32) and sleep quality
      (r = 0.30, k=18, N=12028). These are moderate correlations by the standards
      of this literature and they are consistent in sign across outcomes.
    grade: B
  - note: >
      The direction problem, which is the whole reason this is not graded higher.
      This pools correlations from a largely cross-sectional literature. People
      who are exhausted find it harder to stop thinking about work; people who
      cannot stop thinking about work get more exhausted; and a demanding job
      produces both. The correlation between detachment and exhaustion of -0.36 is
      equally consistent with all three stories, and nothing in the pooled estimate
      distinguishes them. Anyone stating this as "switching off reduces exhaustion"
      has added a causal arrow the data does not contain.
    grade: D
  - note: >
      Long working hours, stated exactly. Pooling 10 published cohort studies with
      unpublished individual-participant data from 18 cohorts -- 189729
      participants from 35 countries, 21747 new-onset cases, follow-up 1 to 5 years
      -- the multivariable-adjusted association between long working hours (defined
      as 55 or more hours per week in most cohorts) and onset of depressive
      symptoms was 1.14 (95 percent CI 1.03 to 1.25), with significant
      heterogeneity (I-squared 45.1 percent, p=0.004). A 14 percent relative
      increase, with a confidence interval whose lower bound sits at 1.03, is a
      small association.
    grade: C
  - note: >
      The regional split is the load-bearing part and it is why this item is
      flagged contested. The same analysis found a MODERATE association in Asian
      countries (1.50, 95 percent CI 1.13 to 2.01), a WEAKER one in Europe (1.11,
      1.00 to 1.22, lower bound exactly on the null), and NO association in North
      America (0.97, 0.70 to 1.34) or Australia (0.95, 0.70 to 1.29). Differences
      by other characteristics were small. So the single most-cited fact about
      overwork and mood does not hold uniformly across the world, and the
      direction of the divergence runs against the WEIRD-sampled default: the
      effect is largest in the region this warehouse's owner lives in and absent
      in the region most of the literature comes from.
    grade: C
  - note: >
      Do not read the regional split as established mechanism. The authors report
      it as an observed difference by region; they do not identify what produces
      it, and candidate explanations -- different hour distributions, different
      job control, different reporting norms for depressive symptoms, different
      cohort composition -- are not separated by these data. The useful conclusion
      is the negative one: an overwork-and-mood estimate imported from a North
      American or Australian sample cannot be assumed to describe a Korean
      working week, and vice versa.
    grade: D
  - note: >
      What survives as operationally usable, and it is modest. Two things are
      observable to an assistant that sees a calendar: total load, and whether
      there is any interval in which work is genuinely off. Both correlate with
      how people report feeling, in the expected directions, at moderate strength.
      Neither has been shown to cause anything. Naming the pattern out loud --
      "this is the third week with nothing off in it" -- is supported. Promising
      that clearing an evening will fix how someone feels is not.
    grade: C
claim: >
  Two workload facts are available and both are weaker than their popular
  versions. First, psychological detachment from work -- being genuinely off, not
  merely not-at-work -- correlates with better outcomes across a large pooled
  literature: Wendsche and Lohmann-Haislah 2017 (Frontiers in Psychology, 86
  publications, 91 independent samples, N=38124 employees) report detachment
  correlating negatively with job demands (r = -0.25), exhaustion (r = -0.36) and
  fatigue (r = -0.42), and positively with general wellbeing (r = 0.32), life
  satisfaction (r = 0.32) and sleep quality (r = 0.30). That literature is largely
  cross-sectional, so the direction is not identified: exhaustion impairing
  detachment, poor detachment producing exhaustion, and a demanding job causing
  both are all equally consistent with r = -0.36. Second, long working hours are
  associated with onset of depressive symptoms, but only slightly and only in some
  places: Virtanen et al. 2018 (Scandinavian Journal of Work, Environment and
  Health), pooling 10 published cohorts with unpublished individual-participant
  data from 18 more (189729 participants, 35 countries, 21747 new-onset cases),
  found an overall association of 1.14 (95 percent CI 1.03 to 1.25) for working 55
  or more hours per week, with significant heterogeneity. The regional breakdown is
  the important part: 1.50 (1.13 to 2.01) in Asian countries, 1.11 (1.00 to 1.22)
  in Europe, 0.97 (0.70 to 1.34) in North America and 0.95 (0.70 to 1.29) in
  Australia. The authors report the divergence without identifying its mechanism.
  The operative consequences: the overwork-and-mood association cannot be imported
  across regions, both findings are observational and neither licenses a causal
  claim, and what an assistant may legitimately do is name an observable pattern
  in load and recovery rather than promise an outcome from changing it.
reasoning: >
  Workload and recovery is the area where a life agent has the most data and the
  least licence, so this item was built to state exactly how much each of the two
  available findings supports. The detachment meta-analysis was chosen because it
  is by far the largest synthesis of the construct and because its outcome set --
  exhaustion, fatigue, wellbeing, sleep quality -- maps onto what an assistant can
  actually observe. Its weakness is structural and is graded accordingly: pooling
  correlations from a cross-sectional literature produces a reliable association
  and no direction at all, and the reverse causal story here is not a technicality
  but the more intuitive reading. The working-hours meta-analysis was chosen over
  the larger published-studies-only literature specifically because it incorporates
  unpublished individual-participant data from 18 cohorts, which is the strongest
  available guard against the publication-bias inflation this domain already
  documents at roughly 37 percent for its own psychotherapy literature. Its
  headline result is small -- a 14 percent relative increase with the interval's
  lower bound at 1.03 -- and its regional breakdown is the reason this item exists
  in this form. The task of checking the Korean case usually means looking for a
  Korean study; here the check is stronger than that, because a single pooled
  analysis of 35 countries reports the association at 1.50 in Asia and at 0.97 in
  North America, which is direct within-study evidence that the WEIRD-sampled
  default estimate does not describe this warehouse's own locale. Flagged
  contested on that divergence: the estimates are inconsistent across regions and
  no mechanism has been established, so any single global figure is disputed by
  the data that produced it. Graded at the trial band for the detachment
  correlations, at the observational band for the working-hours association and
  its regional split, and at the practitioner floor for any causal reading of
  either.
---

# mental-health/workload-detachment-recovery-016

A system watching a calendar can see two things that bear on how someone is
doing: how much work there is, and whether there is any point at which it stops.
Here is what each of those is actually worth.

Start with stopping. Pooled across 86 publications and more than thirty-eight
thousand employees, being psychologically detached from work -- genuinely off,
not just physically elsewhere -- correlates with lower exhaustion, much lower
fatigue, better general wellbeing, better life satisfaction and better sleep
quality. Correlations in the low-to-mid thirties, consistent in sign across every
outcome measured. As correlational findings in this field go, that is a solid
result.

And then the catch, which is not a technicality. Almost all of it is
cross-sectional -- measured at one moment, not followed over time. So the
correlation of about minus a third between detachment and exhaustion is equally
compatible with three different stories. Switching off protects you from
exhaustion. Being exhausted makes it impossible to switch off. A brutal job
produces both. Nothing in the pooled number picks between them, and the second
story is at least as intuitive as the first.

Anyone who says "switching off reduces exhaustion" has quietly added an arrow
that the data does not contain.

Now hours. A very large analysis combined ten published cohort studies with
unpublished individual-level data from eighteen more: nearly a hundred and ninety
thousand people across thirty-five countries, more than twenty-one thousand new
cases of depressive symptoms. Working fifty-five hours a week or more was
associated with a 14 percent higher chance of developing depressive symptoms.
The confidence interval's lower edge sits at 1.03. That is a small effect.

But the breakdown is where this gets interesting, and it is the reason this item
matters more than its headline number.

In Asian countries the association was 1.50. In Europe, 1.11 -- with the lower
bound sitting exactly on no effect. In North America, 0.97. In Australia, 0.95.

So the relationship between long hours and mood is not one fact. It is a strong
one in some places, a marginal one in others, and absent in the two regions that
supply most of the psychological literature the world reads. The authors report
the divergence and do not explain it, and the plausible explanations -- different
hour distributions, different control over the work, different willingness to
report feeling low, different cohorts -- are not separable from these data.

The lesson generalises past this one finding. The default estimate for almost
anything in this lane comes from Western samples, and here is a single pooled
analysis showing that the default estimate for overwork and mood is the wrong
one for Asia, in the direction of understating it by a factor of about three
relative to Europe and by an unbounded amount relative to a North American null.

What is left that can be said honestly is small and worth saying anyway. Load and
recovery both track how people report feeling, in the expected directions, at
moderate strength, in observational data. Nothing here shows that changing either
one changes the other. Pointing at a pattern -- three weeks running with nothing
genuinely off in them -- is supported by this evidence. Promising that clearing
an evening will fix anything is not.
