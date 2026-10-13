---
# Collection sprint 2026-09-02, relationships-communication lane expansion. This
# is the best-powered thing this field has ever produced on "what makes a
# relationship good", and its most important result is a NEGATIVE one that the
# popular coverage almost entirely dropped. It is included partly as the
# positive counterweight to the domain's five refutation rows -- the domain
# needed at least one row that says what IS known -- and partly because its
# negative half is the strongest available argument against every
# relationship-forecasting product on the market.
# Rubric: relationships-communication @dyadic (VC-C).
id: relationships-communication/relationship-quality-predictors-joel-009
domain: relationships-communication
grade: B (which self-report variables rank highest as concurrent predictors, and the actor-over-partner asymmetry); A (the negative finding that CHANGE in relationship quality is not predictable from baseline self-report)
lane: "@dyadic"
locale: universal
as_of: 2020
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/32719123/"  # Joel S, Eastwick PW, Allison CJ et al (86 authors). 2020, Proc Natl Acad Sci USA 117(32):19061-19071, doi 10.1073/pnas.1917036117, PMCID PMC7431040 -- 43 dyadic longitudinal datasets, 29 laboratories, Random Forests
  - "relationships-communication/gottman-prediction-artifact-003"  # the prior domain row on why relationship-outcome prediction claims need out-of-sample discipline
  - "relationships-communication/divorce-prediction-crossvalidation-011"  # the crossvalidation collapse this study's design avoids by construction
  - "framework:GRADE -- the predictor RANKINGS are graded at the trial-adjacent band rather than the top: they are machine-learning variable-importance orderings from pooled observational self-report, not experimental manipulations, and importance rankings are known to be unstable under collinearity, which is severe among relationship-satisfaction items. The NEGATIVE finding is graded at the top band because it is the rare case where scale, design and pre-registration-grade transparency all point the same way -- 43 independent datasets from 29 labs, out-of-sample machine-learning evaluation, and a ceiling below 5 pct of variance. A null this well powered is stronger evidence than most positive findings in this domain."
refraction_notes:
  - note: >
      The headline the coverage ran with, stated correctly. Across 43 dyadic
      longitudinal datasets from 29 laboratories, the top relationship-specific
      predictors of relationship quality were perceived-partner commitment,
      appreciation, sexual satisfaction, perceived-partner satisfaction, and
      conflict. The top individual-difference predictors were life satisfaction,
      negative affect, depression, attachment avoidance, and attachment anxiety.
      Note what is at the top of the first list: FOUR of the five are perceptions
      of the relationship or the partner, not traits of either person. This is the
      study's substantive contribution and it is worth stating in that form.
    grade: B
  - note: >
      The finding almost nobody repeats, and the reason this item exists. Change
      in relationship quality over the course of a study was LARGELY
      UNPREDICTABLE from any combination of self-report variables. The paper
      reports that no analysis accounted for more than 5 percent of the variance
      in change. Baseline self-report told the models a great deal about where a
      couple currently stood and almost nothing about where they were going. Any
      product, questionnaire or agent feature that claims to forecast whether a
      relationship will improve or deteriorate from self-report inputs is
      claiming to do something that 43 datasets and 29 laboratories could not do.
    grade: A
  - note: >
      The asymmetry that constrains what a one-sided data source can know.
      Actor-reported variables -- a person's own ratings -- predicted two to four
      times more variance than partner-reported variables. More strikingly,
      individual differences and partner reports had NO predictive effect beyond
      actor-reported relationship-specific variables alone. The authors read this
      as the sum of individual differences and partner experiences exerting their
      influence THROUGH a person's own relationship-specific experience. The
      operational consequence is favourable for a single-user agent: holding only
      one partner's perceptions is much less of a handicap than it looks, because
      the second partner's ratings add essentially nothing on top.
    grade: B
  - note: >
      The variance figures must be quoted with their anchor or they mislead.
      Relationship-specific variables predicted UP TO 45 percent of variance at
      baseline and UP TO 18 percent at the end of each study; individual
      differences managed 21 percent and 12 percent. The 45 percent figure is
      concurrent -- self-reported satisfaction predicted by self-reported
      relationship perceptions measured at the same time, which is partly the
      same construct measured twice. The honest reading is that the impressive
      number is near-tautological and the prospective number is much smaller, and
      that the gap between the two is the whole story. Reporting 45 percent
      without that anchor repeats exactly the error that
      relationships-communication/gottman-prediction-artifact-003 documents.
    grade: B
  - note: >
      GENERALISABILITY LIMIT, stated by the authors and load-bearing for this
      warehouse's owner. The paper states that all of the current datasets were
      sampled from Western countries -- the United States, Canada, Switzerland,
      New Zealand, the Netherlands and Israel -- and that future work should
      examine whether the effects generalise beyond the Western context. There is
      no East Asian sample in the set. On the affluence axis the study is better
      than most, because more than half of the couples came from a project that
      deliberately oversampled low-income couples, but on the cultural axis it is
      fully WEIRD. See relationships-communication/kr-weird-transfer-gate-016.
    grade: B
claim: >
  The largest well-powered attempt to answer "what predicts relationship
  quality" pooled 43 dyadic longitudinal datasets from 29 laboratories and used
  Random Forests to rank self-report predictors (Joel et al. 2020, PNAS). Its
  two results point in opposite directions and only the first is widely
  repeated. POSITIVE: the top relationship-specific predictors were
  perceived-partner commitment, appreciation, sexual satisfaction,
  perceived-partner satisfaction and conflict; the top individual-difference
  predictors were life satisfaction, negative affect, depression, attachment
  avoidance and attachment anxiety. Actor-reported variables predicted two to
  four times more variance than partner-reported ones, and individual differences
  and partner reports added NOTHING beyond a person's own relationship-specific
  reports. NEGATIVE, and the more important half: CHANGE in relationship quality
  over time was largely unpredictable from any combination of self-report
  variables, with no analysis accounting for more than 5 percent of the variance
  in change. Relationship-specific variables predicted up to 45 percent of
  variance at baseline but only up to 18 percent at study end, and the 45 percent
  figure is concurrent -- near-tautological rather than prospective. The authors
  state that all 43 datasets came from Western countries (United States, Canada,
  Switzerland, New Zealand, Netherlands, Israel), with no East Asian sample.
reasoning: >
  Two separate grades because the two halves rest on different evidential
  footing. The predictor rankings are variable-importance orderings out of a
  Random Forest over pooled observational self-report. That is a strong design
  for this question but importance rankings are unstable when predictors are
  heavily collinear, and relationship-satisfaction items are about as collinear
  as psychological measurement gets; so the rankings sit at the trial-adjacent
  band and should be spoken as "these were the ones that kept coming up", not as
  a causal recipe. The negative finding is graded at the top band, which this
  warehouse otherwise reserves for refutations and multi-lab consensus, and it
  earns that placement on exactly those terms: 43 independent datasets, 29
  laboratories, out-of-sample machine-learning evaluation, and a variance ceiling
  under 5 percent. A null that well powered is a genuine refutation of the
  prediction claim, not an absence of evidence, and it is the single most useful
  thing this domain can tell a product that wants to forecast relationship
  trajectories. The item deliberately foregrounds the concurrent-versus-
  prospective gap in the variance figures, because quoting 45 percent without its
  anchor reproduces the base-rate-free percentage error that
  relationships-communication/gottman-prediction-artifact-003 exists to catch --
  and doing that with this study, of all studies, would be an unusually bad
  failure. Not marked contested: nothing here is disputed in the literature. The
  Western-only sampling is a stated limit, not a controversy, and it is carried
  forward to the locale row rather than treated as a defect of this study.
---

# relationships-communication/relationship-quality-predictors-joel-009

This is the study to reach for when someone asks what actually makes a
relationship good, and it has two answers that get very unequal airtime.

The answer that travelled: across forty-three longitudinal couple datasets from
twenty-nine different laboratories, the things that ranked highest were
perceived partner commitment, appreciation, sexual satisfaction, perceived
partner satisfaction, and conflict. Notice that four of those five are
perceptions of the relationship rather than traits of either person. The
strongest individual-level predictors were life satisfaction, negative affect,
depression, and the two attachment insecurity dimensions.

The answer that did not travel, and which matters more: change was
unpredictable. Whether a couple got better or worse over the course of a study
could not be predicted from any combination of self-report variables the
researchers threw at it. Nothing accounted for more than five percent of the
variance in change. Baseline questionnaires told the models a great deal about
where a couple stood right now and essentially nothing about where they were
heading.

That is a null with real teeth. It comes from forty-three independent datasets
with out-of-sample evaluation, which is the opposite of the small-sample
in-sample fitting that this domain's prediction claims usually rest on. Anything
that offers to forecast a relationship's trajectory from questionnaire answers
is offering something a twenty-nine-laboratory collaboration could not do.

There is a third result worth knowing for anything that only ever hears one side
of a couple. A person's own ratings predicted two to four times more variance
than their partner's ratings did, and once you had the person's own
relationship-specific reports, the partner's reports and both people's
personality traits added nothing at all. The authors read that as everything
else flowing through a person's own experience of the relationship. Practically:
having only one person's view is far less of a handicap than it sounds.

One number needs an asterisk. The often-quoted "forty-five percent of variance"
is concurrent -- self-reported satisfaction predicted by self-reported
perceptions collected at the same moment, which is close to measuring the same
thing twice. The prospective figure, at the end of each study, is eighteen
percent. Quote the second one, or quote both.

And one limit the authors state themselves: every one of the forty-three
datasets came from a Western country. There is no East Asian sample anywhere in
it.
