---
# Collection sprint 2026-09-02 (mental-health lane expansion). The item that
# governs SCHEDULING. Willpower-as-a-depleting-resource is the folk model behind
# every "do the hard thing first" and "decision fatigue" heuristic a life agent
# might build into a day plan, and it is the single most prominent replication
# failure in this literature. Two independent multi-laboratory preregistered
# replications, ten thousand participants between the original meta-analytic
# claim and them, and an effect indistinguishable from zero. Flagged contested
# because the theory retains defenders and because the exploratory analyses are
# not uniformly null.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/ego-depletion-replication-failure-019
domain: mental-health
grade: "A (that the sequential-task ego-depletion effect failed to replicate in two independent preregistered multi-laboratory studies); D (any scheduling heuristic built on a depleting willpower resource)"
lane: "@clinical"
locale: universal
as_of: 2016-2021
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/27474142/"  # Hagger MS, Chatzisarantis NLD, Alberts H, Anggono CO, Batailler C, Birt AR, Brand R, Brandt MJ, et al. 2016, Perspect Psychol Sci 11(4):546-573, doi 10.1177/1745691616652873 -- Registered Replication Report, k=23 laboratories, total N=2141
  - "https://pubmed.ncbi.nlm.nih.gov/34520296/"  # Vohs KD, Schmeichel BJ, Lohmann S, Gronau QF, Finley AJ, Ainsworth SE, Alquist JL, Baker MD, et al. 2021, Psychol Sci 32(10):1566-1581, doi 10.1177/0956797621989733, PMCID PMC12422598 -- preregistered multisite paradigmatic replication, k=36 laboratories, N=3531. Note the author list includes the effect's original proponents
  - "exercise/replication-power-crisis-005"  # the warehouse's existing anchor on what replication failure does to a published effect size
  - "learning-habits/replication-calibration-001"  # the behavioural-domain companion rule
  - "framework:GRADE -- two independent preregistered multi-laboratory replications, one of them designed and co-authored by the effect's own original proponents, is the strongest disconfirmatory design available in psychology. Graded at the top band for the replication failure itself."
refraction_notes:
  - note: >
      The two replications, stated exactly. Hagger et al. 2016 (Registered
      Replication Report, 23 laboratories, N=2141) using a standardised
      sequential-task protocol found the ego-depletion effect SMALL WITH A
      CONFIDENCE INTERVAL ENCOMPASSING ZERO: d = 0.04, 95 percent CI -0.07 to
      0.15. Vohs et al. 2021 (36 laboratories, N=3531) found confirmatory tests
      NON-SIGNIFICANT at d = 0.06, with Bayesian meta-analysis under an informed
      prior showing the data about 4 times more likely under the null than under
      the alternative.
    grade: A
  - note: >
      What makes the 2021 replication unusually strong is who ran it. The author
      list includes the original proponents of the effect, and the design was
      built as a paradigmatic rather than a direct replication -- each laboratory
      implemented one of two procedures intended to manipulate self-control,
      chosen to give the theory its best shot rather than to reproduce one study
      verbatim. A null obtained under a design its own advocates helped specify is
      much harder to dismiss as a failed methodological copy.
    grade: A
  - note: >
      Where it is NOT clean, kept because omitting it would be laundering the
      result in the sceptical direction. Vohs et al.'s exploratory analyses on
      the full sample, ignoring exclusion criteria, found a STATISTICALLY
      SIGNIFICANT effect of d = 0.08, with the Bayesian analysis showing the data
      about equally likely under the null and the informed-prior hypothesis. So
      the honest statement is that the preregistered analyses found no effect and
      an exploratory analysis found a trivially small one, not that the effect is
      proven to be exactly zero.
    grade: A
  - note: >
      The one moderator that emerged, and it points somewhere more useful than
      the original theory. Vohs et al.'s exploratory moderator tests suggested the
      depletion effect was LARGER FOR PARTICIPANTS WHO REPORTED MORE FATIGUE, and
      was NOT moderated by trait self-control, willpower beliefs, or action
      orientation. That is a hint that whatever small effect exists tracks actual
      tiredness rather than a spent psychological resource -- which points back at
      the sleep and workload items in this lane, where the evidence is
      experimental and considerably better.
    grade: C
  - note: >
      The scheduling consequence, which is the reason this item is in a
      mental-health lane rather than a learning one. Do NOT build day plans on a
      willpower budget: front-loading hard tasks because self-control is depleting,
      protecting a decision quota, or explaining an evening lapse by "you used it
      all up in the morning". Those are all inferences from an effect that failed
      to replicate twice. Scheduling around observed tiredness, observed sleep and
      observed load is a different and better-supported thing, and this item does
      not touch it.
    grade: D
  - note: >
      Contested, honestly. The effect has published defenders and the theoretical
      literature is not settled; the 2016 replication itself drew published
      commentary. What is not seriously in dispute is the replication record: two
      large preregistered multi-laboratory attempts, one of them co-designed by
      the theory's proponents, produced effects indistinguishable from zero. Carry
      the replication record as established and the theory's status as disputed.
    grade: A
claim: >
  The ego-depletion effect -- that exerting self-control on one task leaves less
  available for the next, as if from a limited resource -- failed to replicate in
  two independent preregistered multi-laboratory studies. Hagger et al. 2016
  (Registered Replication Report, 23 laboratories, N=2141) using a standardised
  sequential-task protocol found d = 0.04 with a 95 percent confidence interval of
  -0.07 to 0.15, encompassing zero. Vohs et al. 2021 (36 laboratories, N=3531),
  whose author list includes the effect's original proponents and whose
  paradigmatic design let each laboratory implement one of two procedures intended
  to give the manipulation its best chance, found confirmatory tests
  non-significant at d = 0.06, with Bayesian meta-analysis showing the data about
  four times more likely under the null. Two honest qualifications: an exploratory
  analysis on the full sample ignoring exclusion criteria did find a statistically
  significant d = 0.08, so the claim is "no effect in preregistered analyses" and
  not "proven zero"; and exploratory moderator tests suggested any residual effect
  was larger for participants reporting more fatigue while NOT being moderated by
  trait self-control, willpower beliefs or action orientation. The scheduling
  consequence is the operative one: no day plan may be built on a willpower
  budget -- no front-loading hard tasks because self-control depletes, no decision
  quota, no explaining an evening lapse by morning expenditure. Scheduling around
  observed tiredness, sleep and load is a separate and better-evidenced thing and
  is untouched by this.
reasoning: >
  This item is in a mental-health lane rather than a learning-habits one because
  its live consequence is scheduling: a generalist agent that arranges someone's
  day is exactly the system most likely to encode a willpower-budget model, and
  the folk version of that model is directly downstream of the ego-depletion
  literature. Two replications were used rather than one because they are
  independent in design as well as in personnel: the 2016 Registered Replication
  Report standardised a single protocol across 23 laboratories, while the 2021
  study deliberately used a paradigmatic approach across 36 laboratories with the
  effect's original proponents co-authoring, which closes the two most common
  escapes -- that the protocol was wrong, and that the replicators were hostile. A
  null obtained under a design the theory's advocates helped specify is the
  strongest disconfirmation available in this field, which is why the replication
  record is graded at the top band. The item is flagged contested and the
  exploratory results are carried explicitly because the sceptical direction
  deserves the same discipline as the credulous one: the preregistered analyses
  found nothing, an exploratory analysis ignoring exclusions found a trivially
  small significant effect, and stating only the first would be laundering.
  The fatigue moderator is carried because it redirects to better evidence rather
  than merely qualifying the null -- if anything real is happening it appears to
  track actual tiredness, which this lane covers experimentally in item 014 and
  observationally in item 016. Graded at the practitioner floor for any scheduling
  heuristic built on the resource model, which is the concrete thing this item
  exists to forbid.
---

# mental-health/ego-depletion-replication-failure-019

The idea that willpower is a tank that empties is one of the most successful
ideas psychology ever exported. It is also one of the most thoroughly failed
replications in the discipline, and it matters here because anything that plans
someone's day is likely to have built it in without noticing.

The claim was specific: exert self-control on one task, and you have less
available for the next one. Hundreds of studies, a meta-analysis reporting a
medium-sized effect, and a folk vocabulary -- decision fatigue, willpower
depletion, do the hard thing while you still have it -- that outlived the
evidence by a decade.

Two large replication efforts have now tested it.

The first pooled 23 laboratories and over two thousand participants using a
single standardised protocol agreed in advance. The effect came out at 0.04 with
a confidence interval running from below zero to just above it.

The second was bigger and, more importantly, friendlier. Thirty-six laboratories,
three and a half thousand participants, and an author list that includes the
people who proposed the effect in the first place. Rather than copying one study
exactly, each laboratory ran one of two procedures chosen to give the
manipulation its best chance. The preregistered tests came out non-significant at
0.06, and a Bayesian analysis found the data roughly four times more likely if
there were no effect at all.

That second design closes the usual escape hatches. It was not a hostile
replication and it was not a botched copy of a protocol; the theory's own
advocates helped specify what a fair test would look like, and the fair test came
back empty.

Two things should be said against the tidy version of this story, because the
sceptical direction gets the same discipline as the credulous one.

An exploratory analysis on the full sample, ignoring the preregistered
exclusions, did find a statistically significant effect -- of 0.08, which is
trivially small, and with the Bayesian evidence then sitting about evenly between
the two hypotheses. So the accurate claim is that the preregistered analyses
found nothing, not that the effect has been proven to be exactly zero.

And one moderator turned up that is more interesting than the original theory.
Whatever small effect there was, was larger in participants who reported being
more tired. It was not moderated by trait self-control, by beliefs about
willpower, or by action orientation. If something real is in there, it looks like
plain fatigue rather than a spent psychological resource -- and fatigue is a
thing this lane can speak about from experimental evidence rather than from a
metaphor.

The practical consequence is a prohibition on a family of scheduling moves. Do
not front-load hard tasks on the theory that self-control is being spent. Do not
budget decisions. Do not explain someone's evening lapse by what they did that
morning. Every one of those is an inference from an effect that failed to
replicate twice, at scale, including once under conditions its own proponents
helped design.

Scheduling around tiredness that has actually been observed, around a short night
that actually happened, around a week that is actually heavy -- that is a
different thing entirely, it rests on better evidence, and none of it is affected
by any of this.
