---
# Collection sprint 2026-09-02. The deliberate counterweight to item 004. The
# popular claim "sleep more and you will lift more" is almost always sourced to
# ONE uncontrolled study of eleven basketball players, and the only systematic
# review of the sleep-extension literature found seven studies total, three
# randomized trials all at high risk of bias, and two outright nulls. Rubric:
# sleep-recovery @clinical (VC-A). Contested is set deliberately: the
# practitioner consensus is far stronger than the evidence base.
id: sleep-recovery/sleep-extension-weak-evidence-005
domain: sleep-recovery
grade: C (extension helps SOME performance measures); D (any specific magnitude)
lane: "@clinical"
locale: universal
as_of: 2011-2021
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/33352457/"  # Silva AC, Silva A, Edwards BJ, Tod D, Souza Amaral A, de Alcantara Borba D, Grade I, Tulio de Mello M. 2021, Sleep Med 77:128-135, doi 10.1016/j.sleep.2020.11.028 -- the only systematic review of sleep extension in athletes
  - "https://researchonline.ljmu.ac.uk/id/eprint/14111/3/Sleep%20extension%20in%20athletes%20What%20we%20know%20so%20far%20a%20systematic%20review.pdf"  # same paper, accepted manuscript, open access (LJMU repository) -- full text read for this item
  - "https://pubmed.ncbi.nlm.nih.gov/21731144/"  # Mah CD, Mah KE, Kezirian EJ, Dement WC. 2011, Sleep 34(7):943-950, doi 10.5665/SLEEP.1132, PMCID PMC3119836 -- n=11, the single most-cited source for the popular claim
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # the asymmetry partner: removal of sleep is well demonstrated, addition is not
  - "exercise/recovery-modality-soreness-vs-performance-024"  # same perceived-versus-measured structure, different domain
  - "sleep-recovery/short-sleep-appetite-weight-015"  # extension for ENERGY INTAKE has one good RCT (Tasali 2022); that is a different outcome and does not upgrade this performance claim (linked 2026-10-07)
  - "framework:GRADE -- the review's own GRADE ratings across fifteen outcomes were 1 very low, 5 low, 4 moderate, 5 high; all three randomized trials were rated HIGH risk of bias; no meta-analysis was possible. That combination caps this claim at the observational band regardless of how large the individual percentages look."
applicability:
  axes:
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The famous study is weaker than its reputation, and the systematic
      reviewers say so explicitly. Mah et al. 2011 followed ELEVEN Stanford
      varsity basketball players through a 2-4 week baseline and a 5-7 week
      extension. There was no control group. Subjects served as their own
      control in a pre-post design, and the reviewers name the resulting threat
      directly: serial order carryover, meaning the improvement may reflect
      dependence on the earlier testing, learning of the test, or training
      adjustments over the seven-week block. Free-throw and three-point accuracy
      rising 9 percent over seven weeks of a college basketball season, with no
      control arm, is not attributable to sleep by design.
    grade: C
  - note: >
      The size of the whole literature is the finding. The review screened 74
      articles and finished with SEVEN. Study samples ran 9 to 24 athletes. Of
      fifteen performance measures analysed, six showed a large effect and the
      rest ranged from trivial to medium. TWO studies found no performance
      improvement at all despite successfully increasing total sleep time, and a
      third reported no gain in shooting performance. Heterogeneity of protocols
      was severe enough that no meta-analysis could be run.
    grade: B
  - note: >
      The confound that has never been controlled: were the participants
      sleep-DEPRIVED to begin with. The reviewers raise this as the central
      unresolved design question -- extension studies may simply be restoring
      normal sleep to people who were short, not adding a benefit above adequate
      sleep. Only two of the seven studies monitored sleep for the seven days
      needed to characterise a habitual pattern. If that confound is real, the
      correct reading of the entire literature is "fix a deficit," not "bank
      extra."
    grade: C
  - note: >
      Direction check against the domain's other item. Sleep LOSS impairing
      performance is supported by 69 publications of controlled experiments.
      Sleep EXTENSION improving performance rests on seven small studies, three
      of them at high risk of bias. These are not symmetric claims and must never
      be spoken as if they were. Asymmetry of evidence is not a rhetorical point
      here; it is the reason one is graded at the trial band and the other is not.
    grade: B
claim: >
  Extending sleep beyond habitual duration MAY improve some sports-performance
  measures, but the evidence base is far smaller and weaker than its reputation
  and cannot support a specific promised gain. The only systematic review of
  sleep extension in athletes screened 74 articles and retained SEVEN, with
  samples of 9 to 24 participants; no meta-analysis was possible; all three
  randomized controlled trials were rated at HIGH risk of bias; and of fifteen
  performance measures, six showed a large effect while the remainder ranged from
  trivial to medium. Two included studies found NO performance improvement at all
  despite successfully increasing total sleep time. The single study that
  generated the popular version of this claim -- 11 collegiate basketball players
  whose sprint time improved from 16.2 s to 15.5 s and whose free-throw and
  three-point accuracy each rose about 9 percent -- had NO control group; it was a
  non-randomized pre-post design in which the athletes were their own control
  across a 5-7 week block of their competitive season, and the reviewers flag
  serial-order carryover as an unexcluded explanation. A further unresolved
  confound runs through the whole literature: it is not established whether the
  participants were sleep-deprived at baseline, meaning extension studies may be
  restoring adequate sleep rather than adding benefit above it. The operative
  rule: the claim that losing sleep costs performance is well supported; the
  claim that adding sleep buys performance is not, and the two must not be spoken
  in the same voice.
reasoning: >
  This item exists because the asymmetry is invisible in popular retellings.
  Craven et al. 2022, the basis of item 004, pools 227 outcome measures from 69
  publications of controlled sleep-loss experiments; Silva et al. 2021 (Sleep Med
  77:128-135), the basis of this one, is the only systematic review of the
  extension side and found seven eligible studies in the entire literature. The
  reviewers rated risk of bias with Cochrane RoB 2.0 and ROBINS-I and reported
  that all three randomized trials were at high risk; among the four
  non-randomized studies, two were low risk, one moderate and one serious, with
  ALL non-randomized studies showing selection bias. They applied GRADE across
  fifteen outcomes and obtained one very-low, five low, four moderate and five
  high ratings -- a split, not a verdict. They could not pool, citing variation in
  intervention programmes and measurement tools. Their own conclusion is that
  conclusions are tentative because of evidence quality and risk of bias. On the
  Mah 2011 study specifically: the abstract itself describes eleven healthy
  students, a habitual-sleep baseline followed by an extension period, and no
  control arm; the reviewers classify it as a non-randomized quasi-experimental
  trial with subjects as their own control and explicitly raise serial-order
  carryover and test learning as unexcluded alternatives. Note also that two
  papers in the review reported nulls: one found no change in countermovement jump
  or yo-yo test after a sleep-hygiene protocol that did increase total sleep time,
  and another found percentage changes of +0.6 and +0.9 percent on the Wingate
  test with effect sizes of 0.05. Contested is set because practitioner and media
  consensus states this claim with a confidence the source literature does not
  license, and because the included studies genuinely disagree with each other.
  The confound the reviewers foreground -- unknown baseline sleep adequacy -- is
  the one that would, if resolved against the claim, convert the entire
  literature from "extra sleep is ergogenic" into "restoring a deficit is
  ergogenic," which is item 004 restated and not a new finding at all.
---

# sleep-recovery/sleep-extension-weak-evidence-005

Everyone has heard that the Stanford basketball players who slept ten hours a
night got faster and shot better. It is true that they did. It is not
established that sleep is why.

There were eleven of them. There was no control group. They were measured
through a baseline block and then through a five-to-seven week extension block
of their own competitive college season, serving as their own comparison. Over
seven weeks of a season, a college athlete's sprint time and shooting percentage
move for a great many reasons, and the systematic reviewers who later assessed
this literature name the specific problem: serial-order carryover, meaning the
later numbers may depend on the earlier testing, on learning the test, or on
training changes across the block. Nothing about the study design separates those
from the sleep.

The wider literature is smaller than most people would guess. A systematic review
searching for every controlled trial of sleep extension in athletes screened 74
articles and ended with seven. The samples ran from nine to twenty-four people.
Protocols varied so much that the reviewers could not pool the results at all.
All three of the randomized trials were rated at high risk of bias. Two of the
studies found no performance improvement whatsoever even though the athletes
demonstrably did sleep more.

Then there is the confound nobody has closed. It is not known whether the
participants were short on sleep to begin with. Only two of the seven studies
watched sleep for the week it takes to establish someone's habitual pattern. If
the participants were running a deficit, then these studies show that fixing a
deficit helps -- which is a different and much better-supported claim, and it
belongs to the sleep-loss item, not to this one.

So the honest shape is asymmetric, and the asymmetry is the whole point.

Taking sleep away demonstrably costs performance: sixty-nine papers, controlled
experiments, every exercise category, objective endpoints. Adding sleep on top of
what someone already gets may help some measures in some sports, on a base of
seven small studies with two nulls in it. Those two statements deserve very
different tones of voice, and collapsing them into one confident line about
sleeping more to lift more is how a thin literature gets laundered into a rule.

This is the same structure as the recovery-modality problem in the exercise
domain, where a thing that reliably changes how you feel turns out not to
reliably change what you can do. The difference is that sleep clears the bar in
one direction. It has not yet cleared it in the other.
