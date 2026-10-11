---
# Collection sprint 2026-09-02, relationships-communication lane expansion.
# This row CLOSES the open question flagged on
# relationships-communication/gottman-prediction-artifact-003, which recorded
# that "the exact 21-43 pct PPV range is NOT verified (see open question)". It
# is now verified, from the primary methodological paper, at 28.81 pct on
# crossvalidation and 20.99 pct when reweighted to the true divorce prevalence.
# The second source adds the other half nobody had: an INDEPENDENT sample in
# which the affective-process models did not replicate at all.
# Rubric: relationships-communication @dyadic (VC-C) -- methodology/negative.
id: relationships-communication/divorce-prediction-crossvalidation-011
domain: relationships-communication
grade: A (methodology/negative -- divorce-prediction accuracy collapses on crossvalidation and the affective-process models failed independent replication)
lane: "@dyadic"
locale: universal
as_of: 2001-2007
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/17066126/"  # Heyman RE, Smith Slep AM. 2001, J Marriage Fam 63(2):473-479, doi 10.1111/j.1741-3737.2001.00473.x, PMCID PMC1622921 -- 1985 National Family Violence Survey archival data, n=6,002 total, analysis retained 176+176+176 <!-- estate-scrub:allow(author surname Smith, not an instance) -->
  - "https://pubmed.ncbi.nlm.nih.gov/17372624/"  # Kim HK, Capaldi DM, Crosby L. 2007, J Marriage Fam 69(1):55-72, doi 10.1111/j.1741-3737.2006.00343.x, PMCID PMC1828692 -- independent test of Gottman et al 1998 affective process models, 85 couples, Oregon Youth Study, 2.5-year interval
  - "https://pubmed.ncbi.nlm.nih.gov/1403613/"  # Gottman JM, Levenson RW. 1992, J Pers Soc Psychol 63(2):221-233, doi 10.1037/0022-3514.63.2.221 -- 73 couples, the original balance-theory regulated/nonregulated split
  - "https://pubmed.ncbi.nlm.nih.gov/8450108/"  # Gottman JM. 1993, J Consult Clin Psychol 61(1):6-15, doi 10.1037/0022-006X.61.1.6 -- same 73 couples, the five-type typology
  - "relationships-communication/gottman-prediction-artifact-003"  # the row this one closes the open question on
  - "relationships-communication/curator-checklist-007"  # the auto-downgrade trigger this is the worked example for: accuracy without base rate, PPV, or crossvalidation
  - "framework:GRADE -- top band, on the same terms this warehouse grants it elsewhere for refutations. Both sources are direct methodological tests rather than opinion: one recomputes prediction statistics on a nationally representative archival dataset with an explicit holdout, the other applies the published models to an independent community sample and reports the result. Neither depends on effect-size pooling, so heterogeneity and publication bias do not apply. The one limit worth stating is that the replication sample is 85 at-risk couples, which bounds how far its null can be generalised -- but a failed replication in ANY independent sample is decisive against a model that was never crossvalidated in the first place."
refraction_notes:
  - note: >
      The exact collapse, from the primary paper. Heyman and Smith Slep 2001 took
      the 1985 National Family Violence Survey, a nationally representative
      dataset of 6,002 participants, and built a divorce-prediction equation the
      way the published studies did. In the DEVELOPMENT sample the equation
      achieved 89.71 percent correct, 91.89 percent sensitivity, 89.22 percent
      specificity and a positive predictive value of 65.38 percent. On
      CROSSVALIDATION in the holdout the same equation achieved 69.31 percent
      correct, 45.95 percent sensitivity, 74.55 percent specificity and a
      positive predictive value of 28.81 percent. Reweighted to the true
      population prevalence -- approximately 16 percent divorce among couples
      married three to six years -- the positive predictive value falls to 20.99
      percent. This closes the open question left on
      relationships-communication/gottman-prediction-artifact-003.
    grade: A
  - note: >
      Read the positive predictive value, not the accuracy. Twenty-one percent
      positive predictive value at true prevalence means that when the model
      flags a couple as heading for divorce, it is wrong about four times out of
      five. The accuracy figure stays superficially respectable at 69 percent
      only because most couples do not divorce and the model gets those right by
      default. This is the same arithmetic that
      relationships-communication/gottman-prediction-artifact-003 identifies in
      the 94.3 percent headline, now demonstrated end to end on a nationally
      representative dataset. The authors' own conclusion: results of studies
      without crossvalidation analyses should be interpreted with extreme
      caution, no matter how impressive the initial results appear.
    grade: A
  - note: >
      The independent replication failed, and this is a separate and additional
      strike. Kim, Capaldi and Crosby 2007 applied the Gottman et al. 1998
      affective process models to 85 married or cohabiting couples from a
      community-based sample, assessed at about age 21 and followed up 2.5 years
      later. Their stated conclusion is that the major findings of Gottman et al.
      failed to replicate. Specifically, men's rejection of their partners'
      influence, men's failure to deescalate partners' negative affect, and
      women's negative start-up were NOT predictive of relationship status. Only
      2 of 22 affective processes predicted relationship status at all. So the
      problem is not merely that the original accuracy was inflated by in-sample
      fitting -- the underlying behavioural predictors did not carry over.
    grade: A
  - note: >
      What is NOT being claimed, stated explicitly so this row is not
      over-read. This does not establish that the observed behaviours are
      irrelevant to relationships, that couples therapy does not work -- see
      relationships-communication/couples-therapy-rct-006, which has genuine
      randomised support -- or that the original studies were fraudulent. They
      were small (73 couples), longitudinal, and honestly reported; what was
      never done was out-of-sample validation, and the popular retelling then
      converted an in-sample classification statistic into a predictive
      capability. The failure is one of inference and of retelling, not of
      integrity.
    grade: A
  - note: >
      The replication sample's own limit. Kim, Capaldi and Crosby used 85 couples
      from a community sample of young men at RISK for delinquency, assessed at
      about age 21 with a 2.5-year interval. That is a specific and young
      population and a short window, and a null in it does not by itself prove
      the models fail everywhere. It is decisive in combination with the
      crossvalidation result rather than alone: a model that was never
      crossvalidated, whose crossvalidated positive predictive value collapses to
      roughly a fifth, and which then fails in the first independent sample to
      test it, has no surviving claim to predictive validity.
    grade: B
claim: >
  The divorce-prediction claims that made this field famous fail two independent
  methodological tests, and the exact figures are now on file. (1)
  CROSSVALIDATION COLLAPSE: Heyman and Smith Slep (2001, Journal of Marriage and
  Family) built a divorce-prediction equation on the nationally representative
  1985 National Family Violence Survey (n=6,002). In the development sample it
  achieved 89.71 percent correct with a positive predictive value of 65.38
  percent. On crossvalidation the same equation achieved 69.31 percent correct
  with a positive predictive value of 28.81 percent, and reweighted to the true
  divorce prevalence (about 16 percent for couples married three to six years)
  the positive predictive value falls to 20.99 percent -- wrong roughly four
  times in five when it flags a couple. (2) INDEPENDENT REPLICATION FAILURE: Kim,
  Capaldi and Crosby (2007, Journal of Marriage and Family) applied the Gottman
  et al. 1998 affective process models to 85 community couples over 2.5 years and
  state that the major findings failed to replicate; men's rejection of
  influence, men's failure to deescalate, and women's negative start-up did not
  predict relationship status, and only 2 of 22 affective processes predicted it
  at all. The original studies (73 couples, 1992 and 1993) were never
  crossvalidated. This does NOT show the behaviours are irrelevant, that couples
  therapy fails, or that anyone acted in bad faith -- it shows an in-sample
  classification statistic was retold as a predictive capability.
reasoning: >
  This row exists to close a specific open question the warehouse recorded
  against itself. relationships-communication/gottman-prediction-artifact-003
  states that "the exact 21-43 pct PPV range is NOT verified (see open
  question)". It is now verified from the primary source, and the verified
  numbers are 28.81 percent on crossvalidation and 20.99 percent at true
  prevalence -- which means the lower end of the range that had been circulating
  was approximately right and the upper end was not supported by this paper.
  Recording the resolution matters more than the digits: the warehouse flagged an
  unverified figure rather than shipping it, and a later sprint verified it
  rather than quietly adopting it, which is the behaviour the domain's curator
  checklist is meant to produce. Graded at the top band on the same terms this
  warehouse grants elsewhere for refutations: these are direct methodological
  tests, not effect-size pools, so heterogeneity and publication bias do not
  apply, and both are published in the field's own flagship journal rather than
  in outside commentary. The second source is what makes this decisive rather
  than merely cautionary. A crossvalidation collapse alone says the reported
  accuracy was inflated; an independent sample in which the behavioural
  predictors themselves did not carry says the model has no demonstrated
  predictive content to inflate. The item is deliberately fenced against
  over-reading, because the easy overshoot -- "so none of this couples research
  means anything" -- would contradict
  relationships-communication/couples-therapy-rct-006, which holds genuine
  randomised meta-analytic support in the same domain. Prediction claims and
  treatment claims rest on different evidence and fail or survive separately.
---

# relationships-communication/divorce-prediction-crossvalidation-011

The warehouse already recorded that the famous divorce-prediction accuracy was a
classification statistic on a low-base-rate sample rather than a validated
forecast, and it recorded that the precise predictive-value figures were
unverified. They are verified now, and there is a second finding nobody had
attached to them.

First, the collapse. Researchers took a nationally representative survey of six
thousand people and built a divorce-prediction equation the way the published
studies had. On the data it was built from, it looked excellent: about ninety
percent correct, and when it flagged a couple as heading for divorce it was
right about two-thirds of the time. Then they tested the same equation on data
it had never seen. Accuracy fell to sixty-nine percent, and when it flagged a
couple it was right under twenty-nine percent of the time. Reweighted to the
actual divorce rate for couples married three to six years, the flag is right
about twenty-one percent of the time -- wrong roughly four times in five.

Note which number stayed respectable. Accuracy held up at sixty-nine percent
because most couples do not divorce, so a model can score well simply by
predicting "stays together" and being right by default. The positive predictive
value is the number that tells you whether a flag means anything, and it is the
number the popular version never reports. The authors' own conclusion is that
results from studies without crossvalidation should be treated with extreme
caution however impressive they look.

Second, and separately: when an independent team applied the published
affective-process models to eighty-five community couples and followed them for
two and a half years, the major findings did not replicate. The specific
behaviours the models rest on -- a man rejecting his partner's influence, a man
failing to de-escalate her negative affect, a woman's harsh start-up -- did not
predict whether the couples were still together. Two of twenty-two affective
processes predicted anything at all.

So the two failures compound. The reported accuracy was inflated because the
model was scored on the data it was fitted to, and the behavioural content
underneath it did not carry to a new sample.

What this does not say is worth stating plainly, because the overshoot is
tempting. It does not say the behaviours are irrelevant. It does not say couples
therapy is ineffective -- this domain separately records genuine randomised
meta-analytic support for that. And it does not say anyone cheated. The original
work was small, longitudinal and honestly reported. What went wrong happened
afterwards, when an in-sample classification result was retold as an ability to
predict the future.
