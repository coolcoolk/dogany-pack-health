---
# Collection sprint 2026-09-02. Closes the melatonin half of the GAPS.md
# sleep-supplement routing gap ("Fetch melatonin (jet-lag / circadian) and
# magnesium sleep claims; route efficacy to sleep-recovery"). Magnesium was NOT
# closed -- see GAPS.md. The organising axis is the split between what melatonin
# is endorsed FOR (circadian timing) and what it is recommended AGAINST (chronic
# insomnia), by the same authority, using the same framework, six months apart
# in publication terms. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/melatonin-chronobiotic-not-hypnotic-008
domain: sleep-recovery
grade: B (the circadian endorsement and the insomnia non-endorsement); C (the pooled 7-minute effect size)
lane: "@clinical"
locale: universal
as_of: 2013-2017
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/27998379/"  # Sateia MJ, Buysse DJ, Krystal AD, Neubauer DN, Heald JL. 2017, J Clin Sleep Med 13(2):307-349, doi 10.5664/jcsm.6470, PMCID PMC5263087 -- AASM guideline, suggests clinicians NOT use melatonin for chronic insomnia (WEAK)
  - "https://pubmed.ncbi.nlm.nih.gov/26414986/"  # Auger RR, Burgess HJ, Emens JS, Deriy LV, Thomas SM, Sharkey KM. 2015, J Clin Sleep Med 11(10):1199-1236, doi 10.5664/jcsm.5100, PMCID PMC4582061 -- AASM guideline, positive endorsement of strategically timed melatonin for circadian rhythm sleep-wake disorders
  - "https://pubmed.ncbi.nlm.nih.gov/23691095/"  # Ferracioli-Oda E, Qawasmi A, Bloch MH. 2013, PLoS One 8(5):e63773, doi 10.1371/journal.pone.0063773, PMCID PMC3656905 -- meta-analysis, 19 studies, 1683 subjects
  - "sleep-recovery/grade-aasm-anchor-002"  # certainty versus strength: a WEAK recommendation against is not a demonstration of no effect
  - "framework:GRADE -- both AASM documents are GRADE-based systematic-review guidelines, which is why they anchor this item; the meta-analysis is a pooled RCT synthesis and sits below them. Note the AASM's own stated downgrade reasons in the 2017 guideline: funding source and attendant publication-bias risk, small numbers of eligible trials per agent, and observed heterogeneity. Those apply to the melatonin evidence too."
applicability:
  axes:
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: medication_list
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The effect size is the part that never survives retelling. The pooled
      meta-analysis of 19 randomized placebo-controlled trials in 1683 subjects
      found melatonin reduced time to fall asleep by 7.06 minutes (95 percent CI
      4.37 to 9.75) and increased total sleep time by 8.25 minutes (95 percent CI
      1.74 to 14.75), with a sleep-quality standardized mean difference of 0.22
      (95 percent CI 0.12 to 0.32). Statistically real, and about seven minutes.
      The meta-analysts themselves describe the absolute benefit as smaller than
      other pharmacological insomnia treatments, and argue melatonin's case on its
      benign side-effect profile rather than on its efficacy.
    grade: B
  - note: >
      The apparent contradiction is a routing question, not a conflict. The 2015
      circadian guideline endorses STRATEGICALLY TIMED melatonin for delayed
      sleep-wake phase disorder, for blind adults with non-24-hour sleep-wake
      rhythm disorder, and for children and adolescents with irregular sleep-wake
      rhythm disorder and comorbid neurological disorders -- at a second-tier
      degree of confidence. The 2017 insomnia guideline suggests clinicians not
      use melatonin for sleep-onset or sleep-maintenance insomnia. Same body,
      same framework, different question: melatonin is being used as a clock
      signal in one and as a sedative in the other. TIMING is the active
      ingredient in the endorsed use.
    grade: A
  - note: >
      Note what the 2015 guideline also says: it recommends AGAINST melatonin in
      demented elderly patients, at a second-tier degree of confidence. Melatonin
      is not uniformly benign-and-optional across populations, and this is a real
      negative recommendation from the same document that carries the positive
      ones.
    grade: A
  - note: >
      Read the negative recommendation with the domain's grading discipline in
      hand. The AASM statement on melatonin for insomnia is WEAK, which per the
      GRADE separation means low certainty about the balance of outcomes -- not a
      demonstration that melatonin does nothing. The 2017 guideline lists its own
      generic downgrade reasons: industry funding across the field with attendant
      publication-bias risk, few eligible trials per individual agent, and
      heterogeneity. A weak recommendation against and a small positive pooled
      effect are compatible, and the honest reading holds both.
    grade: A
  - note: >
      NOT covered by any source in this item: melatonin dose, formulation,
      long-term safety, product-label accuracy for over-the-counter supplements,
      or any interaction with resistance training, recovery or performance. No
      performance-endpoint melatonin evidence was located in this sprint. Do not
      infer an ergogenic or recovery claim from anything here.
    grade: D
claim: >
  Melatonin is a circadian timing signal, not a sleeping pill, and the evidence
  splits cleanly along that line. The AASM's GRADE-based guideline on intrinsic
  circadian rhythm sleep-wake disorders gives a POSITIVE endorsement, at a
  second-tier degree of confidence, to STRATEGICALLY TIMED melatonin for delayed
  sleep-wake phase disorder, for blind adults with non-24-hour sleep-wake rhythm
  disorder, and for children and adolescents with irregular sleep-wake rhythm
  disorder plus comorbid neurological disorders -- while recommending AGAINST it
  in demented elderly patients. The AASM's GRADE-based guideline on pharmacologic
  treatment of chronic insomnia in adults suggests clinicians NOT use melatonin
  for sleep-onset or sleep-maintenance insomnia (WEAK). These are not in conflict:
  in the endorsed uses the timing IS the intervention. On raw magnitude, the
  pooled meta-analysis of 19 randomized placebo-controlled trials in 1683 subjects
  found a reduction in sleep-onset latency of 7.06 minutes (95 percent CI 4.37 to
  9.75), an increase in total sleep time of 8.25 minutes (95 percent CI 1.74 to
  14.75), and a sleep-quality standardized mean difference of 0.22 -- real,
  consistent, and about seven minutes, with the meta-analysts themselves noting
  the absolute benefit is smaller than for other pharmacological options. The
  operative rule: melatonin used to shift a clock has a guideline behind it;
  melatonin used to knock someone out has a guideline against it and a
  seven-minute effect size.
reasoning: >
  Two AASM systematic-review guidelines and one pooled RCT meta-analysis produce
  a coherent picture that looks contradictory only if the use case is ignored.
  Auger et al. 2015 (J Clin Sleep Med 11(10):1199-1236) ran a systematic review
  with meta-analyses where appropriate and used GRADE to update the prior AASM
  practice parameters on circadian rhythm sleep-wake disorders; its positive
  endorsements are explicitly for STRATEGICALLY TIMED melatonin in named
  circadian conditions, and it also issues negative recommendations for melatonin
  and for discrete sleep-promoting medications in demented elderly patients.
  Sateia et al. 2017 (J Clin Sleep Med 13(2):307-349) applied the same machinery
  to individual drugs for chronic insomnia and placed melatonin among the agents
  it suggests clinicians not use, alongside trazodone, tiagabine, diphenhydramine,
  tryptophan and valerian -- all WEAK. Ferracioli-Oda et al. 2013 (PLoS One
  8(5):e63773) supplies the magnitude the guidelines do not foreground: 19 trials,
  1683 subjects, statistically significant but numerically small effects on
  latency, total sleep time and quality, with the authors resting melatonin's case
  on tolerability rather than efficacy. Contested is set for two reasons. First,
  there is a genuine surface tension between a same-body endorsement and
  non-endorsement that a reader will encounter as a contradiction unless the
  circadian-versus-hypnotic routing is made explicit. Second, and more importantly
  for a consumer-facing agent, melatonin's popular reputation as a general sleep
  aid is not what either guideline supports, and the gap between reputation and
  evidence is exactly what a contested flag is for in this warehouse. Graded at
  the trial band rather than the top band because the endorsement itself is
  reported at a second-tier degree of confidence and the negative recommendation
  is weak; the pooled effect size is graded lower still, since the AASM's own
  listed downgrade reasons for this literature -- industry funding, few trials per
  agent, heterogeneity -- apply directly to it.
---

# sleep-recovery/melatonin-chronobiotic-not-hypnotic-008

Melatonin is a clock signal. It tells the body what time it is. It is not a
sedative, and almost every disappointment people have with it comes from using it
as one.

The sleep field's authoritative body has published guidelines on both uses, and
they point in opposite directions on purpose.

For circadian problems -- a sleep phase shifted too late, a blind adult whose
rhythm has come free of the 24-hour day, certain paediatric neurological cases --
strategically timed melatonin gets a positive endorsement. The word doing the work
in that sentence is "timed." In these uses the timing is the treatment; the
molecule is just the messenger.

For chronic insomnia in adults, the same body reviewed melatonin and suggested
clinicians not use it, putting it in the same bucket as trazodone,
diphenhydramine, tryptophan and valerian.

Those two are not a contradiction. They are two different questions, and the
answer differs because the mechanism being invoked differs.

Then there is the size of the thing, which is where popular retellings quietly
fail. The pooled analysis of nineteen randomized placebo-controlled trials across
1,683 people found melatonin cut the time to fall asleep by about seven minutes
and added about eight minutes of total sleep. Those results are statistically
solid; the intervals do not cross zero. They are also seven and eight minutes. The
researchers who ran that analysis said plainly that the absolute benefit is
smaller than other pharmacological options and argued for melatonin mainly on the
grounds that it is mild, not on the grounds that it works well.

A discipline note that this domain insists on. The recommendation against
melatonin for insomnia is a WEAK one, and weak in this framework means low
certainty about the balance of benefits and harms -- it is not a finding that
melatonin does nothing. A weak recommendation against and a small real effect are
perfectly compatible, and the honest answer holds both rather than picking the
more quotable one.

Two things nothing here covers. It is not uniformly benign: the circadian
guideline recommends against melatonin in elderly patients with dementia. And
there is no evidence in any of these sources touching dose, formulation, long-term
use, over-the-counter product accuracy, or any effect on training, recovery or
performance. Nothing in this item licenses a claim that melatonin helps anyone
recover from a workout.
