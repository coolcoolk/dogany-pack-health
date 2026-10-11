---
# Collection sprint 2026-09-02. The "sleep under 8 hours means 1.7 times the
# injury risk" line is one of the most repeated claims in strength coaching. It
# comes from a specific study, that study is real, and it is a retrospective
# survey of ADOLESCENTS. The only systematic review restricted to adults and to
# prospective designs reached the opposite verdict. Rubric: sleep-recovery
# @clinical (VC-A). Contested set because two credible syntheses disagree once
# you notice they cover different populations.
id: sleep-recovery/adult-injury-risk-not-established-006
domain: sleep-recovery
grade: C (adolescent association); D (any causal or adult-transferable injury claim)
lane: "@clinical"
locale: universal
as_of: 2014-2021
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/25028798/"  # Milewski MD, Skaggs DL, Bishop GA, Pace JL, Ibrahim DA, Wren TA, Barzdukas A. 2014, J Pediatr Orthop 34(2):129-133, doi 10.1097/BPO.0000000000000151 -- n=112 adolescents, the origin of the 1.7x figure
  - "https://pubmed.ncbi.nlm.nih.gov/30888337/"  # Gao B, Dwivedi S, Milewski MD, Cruz AI Jr. 2019, J Pediatr Orthop 39(5):e324-e333, doi 10.1097/BPO.0000000000001306 -- meta-analysis, 7 studies, adolescents, OR 1.58
  - "https://pubmed.ncbi.nlm.nih.gov/33560506/"  # Dobrosielski DA, Sweeney L, Lisman PJ. 2021, Sports Med 51(4):777-793, doi 10.1007/s40279-020-01416-3 -- 12 PROSPECTIVE cohorts, ADULT athletes, evidence does NOT support sleep as an independent risk factor
  - "framework:GRADE -- every study on both sides is observational, so the ceiling is the observational band before any other consideration. The adolescent meta-analysis self-rates as Level IV (a systematic review of Level II studies and one Level IV study). The adult review used the Newcastle-Ottawa Scale and still concluded the evidence is insufficient. Nothing here reaches the trial band, and the popular version of the claim is stated causally, which no source supports."
applicability:
  axes:
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The origin study, examined directly. Milewski et al. 2014 surveyed
      student athletes at a single combined middle and high school, grades 7 to
      12. 160 consented; 112 completed the online survey, a 70 percent
      completion rate. Mean age 15 years, range 12 to 18. Sleep hours were
      SELF-REPORTED in an online questionnaire about training practices; injuries
      came from a RETROSPECTIVE review of the school athletic department's
      records. The reported figure is an odds ratio of 1.7 with a 95 percent
      confidence interval of 1.0 to 3.0 and p = 0.04 -- the interval's lower
      bound sits ON 1.0. In the same multivariate model, each additional grade in
      school carried an odds ratio of 1.4 with an interval of 1.2 to 1.6 and
      p < 0.001, which is the tighter and more significant of the two predictors.
      Presenting this as a clean causal 1.7-times-injury-risk finding
      misrepresents a borderline association in a retrospective adolescent survey.
    grade: C
  - note: >
      The adult literature is the one that matters for an adult lifter, and it
      does not agree. Dobrosielski et al. 2021 restricted inclusion to adult
      athletic populations, to studies that followed participants PROSPECTIVELY
      for injury, and graded each with the Newcastle-Ottawa Scale. Across 12
      prospective cohorts they found limited evidence overall: INSUFFICIENT
      evidence of an association in professional or elite athletes, collegiate
      athletes, dancers and endurance athletes, and only limited evidence for
      sport-related concussion in collegiate athletes. Their conclusion is
      explicit -- the current evidence does not support poor sleep as an
      independent risk factor for sport or training-related injury in adults.
    grade: B
  - note: >
      Population, not contradiction, is what separates the two verdicts. The
      adolescent meta-analysis (7 studies, odds ratio 1.58, 95 percent CI 1.05 to
      2.37) is not wrong; it is about adolescents, whose sleep need, school-driven
      schedules and growth-related injury profile all differ. Any transfer to an
      adult recreational lifter is an extrapolation across populations and should
      be spoken as one.
    grade: B
  - note: >
      No resistance-training-specific evidence was found. Every study on both
      sides concerns sport participation or team-sport training exposure. Nothing
      located in this sprint measures injury risk in a barbell-training
      population as a function of sleep. Treat any statement about lifting
      injuries and sleep as unevidenced rather than as covered by this item.
    grade: D
  - note: >
      Direction of causation is untested throughout. All designs are
      observational and several are retrospective. Injury and poor sleep plausibly
      run both ways -- pain and post-injury stress degrade sleep -- and the
      adolescent origin study's own strongest predictor was school grade, a
      proxy for age, competition level and training exposure. No source found
      isolates sleep from training load.
    grade: C
claim: >
  The widely repeated claim that sleeping under 8 hours multiplies injury risk
  by 1.7 is traceable to one specific study, and that study is a RETROSPECTIVE
  survey of 112 adolescent athletes aged 12 to 18 at a single school, using
  self-reported sleep and a retrospective review of school injury records; its
  odds ratio of 1.7 carries a 95 percent confidence interval of 1.0 to 3.0, with
  the lower bound resting on 1.0, and in the same model school grade was the
  stronger predictor (OR 1.4, CI 1.2 to 1.6). A later meta-analysis of 7 studies
  supports the association IN ADOLESCENTS (OR 1.58, 95 percent CI 1.05 to 2.37).
  The picture inverts for adults: the systematic review restricted to adult
  athletic populations and to studies following participants PROSPECTIVELY for
  injury examined 12 prospective cohorts and concluded that the current evidence
  does NOT support poor sleep as an independent risk factor for sport or physical
  training-related injury, finding the evidence insufficient in professional,
  elite, collegiate, dance and endurance populations. No study located in this
  sprint measures injury risk against sleep in a resistance-training population at
  all. The operative rule: the injury-risk number circulating in strength
  coaching is adolescent, retrospective, borderline-significant and confounded
  with age and training exposure, and the adult prospective literature does not
  reproduce it. Sleep may still be worth protecting for the performance reasons
  in item 004; it should not be sold as adult injury insurance.
reasoning: >
  Three sources, read in their own terms, produce a clean population split.
  Milewski et al. 2014 (J Pediatr Orthop 34(2):129-133) is the origin of the
  circulating figure and is transparent about its own design: an online survey of
  training practices completed by 112 of 160 consenting students at a combined
  middle and high school, correlated against a retrospective review of the
  school's injury records. That is a cross-sectional self-report exposure against
  a retrospective outcome, which cannot establish direction, and the effect is
  borderline (95 percent CI 1.0 to 3.0, p = 0.04). The authors themselves report
  school grade as the more robust predictor in the same multivariate model, which
  is a strong hint that training exposure and age are doing work the sleep
  variable is being credited with. Gao et al. 2019 (J Pediatr Orthop
  39(5):e324-e333) pooled 7 studies and found OR 1.58 (95 percent CI 1.05 to 2.37)
  for chronically poor sleepers among adolescents, while explicitly stating that
  current evidence cannot determine the effect of ACUTE sleep loss on injury
  rates, and self-classifying as Level IV evidence. Dobrosielski et al. 2021
  (Sports Med 51(4):777-793) is the decisive one for an adult consumer: by
  requiring adult populations AND prospective injury follow-up, it removes both
  the age transfer and the retrospective-recall problem, and across 12 cohorts it
  reports limited evidence overall, insufficient evidence for every specific adult
  athletic subgroup examined, and a conclusion that the evidence does not support
  poor sleep as an independent risk factor. Contested is set because two
  competent syntheses reach opposite-sounding verdicts, and a reader who does not
  notice the population and design difference will treat one of them as simply
  wrong. Neither is wrong. The adolescent finding is real and the adult finding is
  real, and the popular claim survives only by quoting the first and applying it
  to the second.
---

# sleep-recovery/adult-injury-risk-not-established-006

The number is real. The study exists. It is about teenagers.

"Sleeping under eight hours makes you 1.7 times more likely to get injured" comes
from a 2014 paper on 112 student athletes at a single middle-and-high school,
aged twelve to eighteen. The athletes filled in an online questionnaire about
their training habits, including how much they slept, and the researchers matched
that against a retrospective look through the school athletic department's injury
records. The 1.7 figure carries a confidence interval running from 1.0 to 3.0 --
the bottom edge is sitting exactly on "no effect." And in the very same
statistical model, the athlete's school grade was the stronger and far more
significant predictor, with a much tighter interval. Grade in school is a stand-in
for age, competition level and how much training someone is doing. A good part of
what gets called the sleep effect may be that.

A later pooled analysis of seven studies does back the association up in
adolescents, at odds ratio 1.58. That is a genuine finding and it is worth
knowing if the person in front of you is fifteen.

For adults the picture reverses, and this is the part that almost never gets
quoted. A systematic review deliberately restricted to adult athletes and to
studies that followed people FORWARD in time to see who got hurt -- twelve
prospective cohorts, each quality-scored -- concluded that the current evidence
does not support poor sleep as an independent risk factor for sport or
training-related injury in adults. Not "the effect is smaller." Insufficient
evidence, in professional athletes, collegiate athletes, dancers and endurance
athletes alike.

The two reviews are not fighting. They cover different people using different
designs, and the popular claim survives only by taking the adolescent,
retrospective, self-reported one and quietly applying it to a thirty-something
who lifts four times a week.

One more absence worth stating plainly: nothing found in this sprint studies
injury risk against sleep in a barbell-training population specifically. Every
study on either side is about sport participation and team training exposure. So
if the question is "will short sleep hurt my back under a squat bar," the honest
answer is that nobody has measured it.

None of this argues for sleeping badly. Short sleep has a measured, replicated
cost in performance, and that case is made elsewhere in this domain on much
stronger evidence. It just should not be sold as insurance against getting hurt,
because for adults that part has not been shown.
