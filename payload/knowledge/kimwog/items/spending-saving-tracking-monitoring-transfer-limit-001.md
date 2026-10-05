---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# Foundational item: the strongest evidence that tracking anything works, and
# the honest statement of what that evidence is NOT.
id: spending-saving/tracking-monitoring-transfer-limit-001
domain: spending-saving
grade: B (meta-analysis of randomised experiments, domain-general)
lane: "@household-behavioral"
locale: universal
as_of: 2016
contested: no
sources:
  - "Harkin, B., Webb, T. L., Chang, B. P. I., Prestwich, A., Conner, M., Kellar, I., Benn, Y. and Sheeran, P. (2016). Does monitoring goal progress promote goal attainment? A meta-analysis of the experimental evidence. Psychological Bulletin 142(2), 198-229. https://doi.org/10.1037/bul0000025 (PMID 26479070, record read at PubMed)"
  - "source:spending-saving/budget-app-rct-knowledge-not-saving-014 -- the money-specific randomised trial that does NOT reproduce a behaviour effect, and the reason this item is capped below the top band"
refraction_notes:
  - note: >
      The 138 pooled trials are self-regulation studies across many behavioural
      domains, overwhelmingly health and performance. Money is not the tested
      domain. Quoting the pooled figure as if it were an effect of expense
      tracking on spending is a domain-transfer error, and the one randomised
      trial of an actual budget-recording tool did not move saving at all.
    grade: B
claim: >
  The general premise a tracking agent rests on -- that recording progress
  changes behaviour -- has real experimental support, and the support is
  domain-general rather than financial. Harkin et al. (2016) pooled 138 studies
  (N = 19,951) that randomly assigned participants to an intervention designed
  to promote monitoring of goal progress versus a control condition. A
  random-effects model found interventions increased monitoring frequency with
  d+ = 1.98, 95 percent CI [1.71, 2.24], and promoted goal attainment with
  d+ = 0.40, 95 percent CI [0.32, 0.48]. The effect on attainment was MEDIATED
  by the change in monitoring frequency, which is what makes this a claim about
  monitoring rather than about attention generally. Two moderators are directly
  actionable for a logging product: effects on attainment were larger when
  outcomes were reported or made public, and larger when the information was
  PHYSICALLY RECORDED rather than merely noticed. The boundary that must travel
  with the number: the pooled evidence is not about money. The nearest
  randomised test of a budget-recording tool moved knowledge and did not move
  saving (item 014).
reasoning: >
  This is graded at the strong empirical band and deliberately not at the top,
  and the reason is transfer rather than quality. The meta-analysis itself is
  strong -- randomised allocation as an inclusion criterion, a large pooled
  sample, a mediation result rather than a bare association -- but the domain it
  measures is not the domain it is being used in. This lane's ceiling is
  reserved for measurements taken against an external benchmark in the
  measured domain (item 002), and an effect imported from health and
  performance self-regulation does not qualify however good it is at home. The
  item is placed first in the lane on purpose: it is the assumption every other
  item is built on top of, and it is better to state its limit at the top than
  to let it be assumed everywhere silently. Practical consequences: an agent
  should keep the record explicit and written rather than inferred, and should
  surface it, because both of those are the moderators that carried the effect.
---

# spending-saving/tracking-monitoring-transfer-limit-001

Does keeping a record actually change what someone does? The strongest answer
available is yes, with a moderate effect, from 138 randomised studies covering
almost 20,000 people. Interventions that got people monitoring their progress
raised how often they monitored by a large margin, and raised the rate at
which they reached their goal by a moderate one. Importantly, the goal effect
ran THROUGH the monitoring: the studies that increased monitoring most were the
ones that moved attainment most. That is what turns this from "engaged people
do better" into a claim about the act of recording.

Two details from the moderator analysis are worth designing around. Monitoring
worked better when the result was reported or made visible to someone else, and
it worked better when the information was physically written down rather than
just observed. Both point the same way for a ledger: an explicit, durable,
surfaced record beats a passive one.

Now the limit, which is large enough that it belongs in the same breath as the
finding. These are not studies about money. They are self-regulation studies,
mostly about health and performance behaviours. The number says that monitoring
is an effective self-regulation strategy in general; it does not say that
tracking your spending reduces your spending by any particular amount, and it
was never measured that way. The closest thing to a direct financial test --
a randomised trial of a budget-recording app -- improved what people knew and
left their saving unchanged.

So the defensible position is narrow and still useful: a written, visible
record is a well-supported way to change behaviour, and anyone quoting a
specific percentage of money saved from tracking is quoting a number that does
not exist in this literature.
