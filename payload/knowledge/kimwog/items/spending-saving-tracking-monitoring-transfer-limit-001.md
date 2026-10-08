---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# Foundational item: the strongest evidence that tracking anything works, and
# the honest statement of what that evidence is NOT.
# Source re-audit 2026-10-07: Harkin et al. 2016 accepted manuscript (White Rose
# copy) read in full. 'Overwhelmingly health and performance' -> almost all
# health goals (1 of 138 studies monitored a non-health domain, time use; none
# money). Mediation was study-level on 21 studies, a limit the authors flag;
# the unadjusted d+=0.40 now carries trim-and-fill (0.19) and the adequately
# powered subset (0.33); 'moderate' -> the authors' 'small-to-medium'.
id: spending-saving/tracking-monitoring-transfer-limit-001
domain: spending-saving
grade: B (meta-analysis of randomised experiments with bias diagnostics reported, almost all health goals)
lane: "@household-behavioral"
locale: universal
as_of: 2016
contested: no
sources:
  - "Harkin, B., Webb, T. L., Chang, B. P. I., Prestwich, A., Conner, M., Kellar, I., Benn, Y. and Sheeran, P. (2016). Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. Psychological Bulletin 142(2), 198-229. https://doi.org/10.1037/bul0000025 (PMID 26479070, record read at PubMed; full text read in the accepted manuscript, https://eprints.whiterose.ac.uk/id/eprint/91437/)"
  - "source:spending-saving/budget-app-rct-knowledge-not-saving-014 -- the money-specific randomised trial that does NOT reproduce a behaviour effect, and the reason this item is capped below the top band"
refraction_notes:
  - note: >
      The 138 pooled trials are self-regulation studies almost all about health
      goals (the authors report one study outside health, on time use). Money
      is not the tested domain. Quoting the pooled figure as if it were an
      effect of expense tracking on spending is a domain-transfer error, and
      the one randomised trial of an actual budget-recording tool did not move
      saving at all.
    grade: B
claim: >
  The general premise a tracking agent rests on -- that recording progress
  changes behaviour -- has real experimental support, and the support is
  domain-general in design but almost entirely about health goals, not
  financial ones. Harkin et al. (2016) pooled 138 studies (N = 19,951) that
  randomly assigned participants to an intervention designed to promote
  monitoring of goal progress versus a control condition. A random-effects
  model found interventions increased monitoring frequency with d+ = 1.98,
  95 percent CI [1.71, 2.24], and promoted goal attainment with d+ = 0.40,
  95 percent CI [0.32, 0.48], which the authors call small-to-medium. That 0.40
  is unadjusted: Egger's test showed small-study asymmetry (p < .01 for
  attainment), trim-and-fill imputed 31 effects and gave d+ = 0.19 (95 percent
  CI [0.10, 0.28]), and the adequately powered half of the studies (at least 35
  per condition) gave d+ = 0.33; the authors judge publication bias modest
  rather than severe, because trim-and-fill can understate a real effect when
  heterogeneity is large. A mediation analysis on the 21 studies that reported
  both measures (N = 1,995) found the effect on attainment ran through the
  change in monitoring frequency, which points to monitoring rather than
  attention generally; it is a study-level analysis, not participant-level, and
  the authors list that as a limitation. Two moderators are directly actionable
  for a logging product: effects on attainment were larger when outcomes were
  reported or made public, and larger when the information was PHYSICALLY
  RECORDED rather than merely noticed -- between-study comparisons, for which
  the authors offer several explanations (for public reporting, among them
  accountability and experimenter demand). The boundary that must travel with
  the number: the pooled evidence is not about money. The nearest randomised
  test of a budget-recording tool moved knowledge and did not move saving
  (item 014).
reasoning: >
  This is graded at the strong empirical band and deliberately not at the top,
  and the reason is transfer rather than quality. The meta-analysis itself is
  strong -- randomised allocation as an inclusion criterion, a large pooled
  sample, publication-bias diagnostics reported, a study-level mediation result
  rather than a bare association -- but the headline effect roughly halves under
  trim-and-fill and the domain it measures is not the domain it is being used
  in. This lane's ceiling is reserved for measurements taken against an
  external benchmark in the measured domain (item 002), and an effect imported
  from health self-regulation does not qualify however good it is at home. The
  item is placed first in the lane on purpose: it is the assumption every other
  item is built on top of, and it is better to state its limit at the top than
  to let it be assumed everywhere silently. Practical consequences: an agent
  should keep the record explicit and written rather than inferred, and should
  surface it, because both of those are the between-study moderators that went
  with larger effects.
---

# spending-saving/tracking-monitoring-transfer-limit-001

Does keeping a record actually change what someone does? The strongest answer
available is yes, with a small-to-medium effect that shrinks under the authors'
own bias adjustment (0.40 raw, about 0.2 after trim-and-fill), from 138
randomised studies covering almost 20,000 people. Interventions that got people
monitoring their progress raised how often they monitored by a large margin,
and raised the rate at which they reached their goal by a smaller one. The goal
effect appears to run THROUGH the monitoring: across the 21 studies that
reported both, the ones that increased monitoring most were the ones that
moved attainment most. That is a pattern across studies, which the authors flag
as a limit, but it is what moves this from "engaged people do better" toward a
claim about the act of recording.

Two details from the moderator analysis are worth designing around. Monitoring
worked better when the result was reported or made visible to someone else, and
it worked better when the information was physically written down rather than
just observed. Both point the same way for a ledger: an explicit, durable,
surfaced record beats a passive one -- with the caveat that these are
comparisons between studies, and that being visible to someone may partly be
accountability.

Now the limit, which is large enough that it belongs in the same breath as the
finding. These are not studies about money. They are self-regulation studies,
almost all about health goals; the authors found one study outside health, on
time use, and none on money. The number says that monitoring
is an effective self-regulation strategy in general; it does not say that
tracking your spending reduces your spending by any particular amount, and it
was never measured that way. The closest thing to a direct financial test --
a randomised trial of a budget-recording app -- improved what people knew and
left their saving unchanged.

So the defensible position is narrow and still useful: a written, visible
record is a well-supported way to change behaviour, and anyone quoting a
specific percentage of money saved from tracking is quoting a number that does
not exist in this literature.
