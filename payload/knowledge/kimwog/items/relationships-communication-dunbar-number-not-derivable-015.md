---
# Collection sprint 2026-09-02, relationships-communication lane expansion.
# Included on scope grounds: the consumer of this lane holds a roster of well
# over a hundred people, so "is there a cognitive ceiling on how many
# relationships a person can maintain" is not an abstract question here -- an
# agent that believed the 150 figure could tell the owner his roster is over
# capacity. The refutation is a clean statistical one and follows the same shape
# as relationships-communication/positivity-ratio-invalid-001: a precise
# constant produced by a method that cannot produce a precise constant.
# Rubric: relationships-communication @dyadic (VC-C).
id: relationships-communication/dunbar-number-not-derivable-015
domain: relationships-communication
grade: B (the 150 figure cannot be derived by the method it comes from -- a direct statistical re-analysis); D (the nested-layer structure of 5/15/50/150 and any per-layer prescription)
lane: "@dyadic"
locale: universal
as_of: 2021
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/33947220/"  # Lindenfors P, Wartel A, Lind J. 2021, Biol Lett 17(5):20210158, doi 10.1098/rsbl.2021.0158, PMCID PMC8103230 -- Bayesian and generalized least-squares phylogenetic re-analysis; point estimates 69-109 and 16-42, 95 pct CIs 4-520 and 2-336
  - "relationships-communication/positivity-ratio-invalid-001"  # the same failure shape: a precise constant extrapolated from a model that cannot support precision
  - "relationships-communication/curator-checklist-007"  # auto-downgrade triggers this row instantiates: precise universal constants, and popularity outpacing verified evidence
  - "relationships-communication/contact-cadence-no-evidence-014"  # the cadence-side twin: layers that are not supportable cannot generate per-layer contact schedules
  - "framework:GRADE -- the refutation sits at the trial-adjacent band rather than the top, and the distinction from relationships-communication/positivity-ratio-invalid-001 is deliberate. That row is graded at the top because the constant was shown to be an arithmetic artefact AND was formally retracted by the journal. This one has neither a retraction nor a mathematical impossibility -- it is a re-analysis showing that the original extrapolation cannot support the precision claimed, which is a strong statistical argument but remains a live scientific dispute with the original author still defending the estimate. The layer structure is graded at the bottom band because no source located in this sprint validates it at all."
refraction_notes:
  - note: >
      What the re-analysis actually did and found. The 150 figure originates from
      an extrapolation of a regression line describing the relationship between
      relative neocortex size and group size in primates. Lindenfors, Wartel and
      Lind 2021 tested whether that extrapolation carries statistical support,
      using complementary datasets and different methods. Bayesian methods
      produced average group size approximations of 69-109; generalized
      least-squares phylogenetic methods produced 16-42. The 95 percent confidence
      intervals were 4-520 and 2-336 respectively. The authors' conclusion, in
      their own words: enormous confidence intervals imply that specifying any one
      number is futile, and a cognitive limit on human group size cannot be
      derived in this manner.
    grade: B
  - note: >
      The interval is the finding, not the point estimate. A confidence interval
      running from 4 to 520 does not mean the answer is somewhere in the middle;
      it means the method has essentially no resolving power for this question.
      Note also that the two methods disagree with EACH OTHER by a factor of four
      on the point estimate before the intervals are even considered. Reporting
      "the real number might be 69 to 109 instead of 150" would repeat the
      original error at a different value -- the result is that no number is
      derivable, not that a better number was found.
    grade: B
  - note: >
      CONTESTED, and honestly so. This is a live scientific dispute, not a closed
      case. Unlike the positivity ratio, there is no formal retraction here and no
      demonstrated arithmetic impossibility; the original proponent continues to
      defend the estimate, and separate lines of argument for it exist that do not
      rest on the neocortex regression. What the re-analysis establishes is
      narrower and still decisive for practical purposes: the specific derivation
      that gave the number its authority does not support it. Speak it as
      "the number cannot be derived the way it is usually justified", not as
      "the number has been disproved".
    grade: C
  - note: >
      The layer structure has less support than the headline number, which is the
      reverse of how it is usually presented. The nested set -- roughly 5
      intimates, 15 close friends, 50 friends, 150 acquaintances -- is quoted with
      more confidence than the 150 itself, and no source located in this sprint
      validates it. If the top-level figure cannot be derived from the regression,
      a scaled series of sub-layers derived from the same framework inherits that
      problem and adds its own. The per-layer contact schedules that circulate
      alongside it have no primary source at all; see
      relationships-communication/contact-cadence-no-evidence-014.
    grade: D
  - note: >
      Why this matters operationally rather than academically, for a consumer
      holding a large person roster. An agent that treated 150 as a real cognitive
      ceiling would draw a false conclusion from a real count -- that a roster
      approaching or exceeding it is over capacity, that relationships must be
      pruned, or that maintenance is being spread too thin. None of those follow.
      There is no established ceiling, the count in a stored roster is not the same
      construct as the group size in the primate regression anyway, and no source
      in this domain links roster size to any outcome. Count is a bookkeeping fact
      here, not a diagnostic.
    grade: D
claim: >
  The widely repeated claim that humans can maintain roughly 150 stable
  relationships cannot be derived by the method it comes from. The figure
  originates as an extrapolation of a regression line relating relative neocortex
  size to group size in primates. Lindenfors, Wartel and Lind (2021, Biology
  Letters) re-tested that extrapolation on complementary datasets: Bayesian
  methods gave average group-size approximations of 69-109, generalized
  least-squares phylogenetic methods gave 16-42, and the 95 percent confidence
  intervals were 4-520 and 2-336. The authors conclude that such enormous
  intervals imply specifying any one number is futile and that a cognitive limit
  on human group size cannot be derived in this manner. The interval, not the
  point estimate, is the finding -- the correct reading is that NO number is
  derivable, not that a better number was found. This remains a live dispute
  rather than a closed refutation: there is no retraction and no demonstrated
  arithmetic impossibility, and the original proponent still defends the estimate
  on other grounds. Speak it as "cannot be derived the way it is usually
  justified", not "disproved". The nested layer structure (roughly 5/15/50/150)
  has LESS support than the headline number and was validated by no source
  located here; the per-layer contact schedules quoted alongside it have no
  primary source at all. Operationally: there is no established ceiling on how
  many people a person can keep track of, and roster size is a bookkeeping fact,
  not a diagnostic.
reasoning: >
  Included on scope grounds rather than as a general-interest debunking. This
  lane's consumer holds a roster of well over a hundred people, which means the
  150 figure is not abstract here: an agent that believed it would draw a
  concrete and wrong conclusion from a real number in its own store -- that the
  roster is at or past capacity, that relationships need pruning, that attention
  is spread too thin. None of that follows from anything, and blocking it needs an
  item rather than a ledger note. The failure shape is the same one
  relationships-communication/positivity-ratio-invalid-001 documents: a precise
  constant produced by a method that cannot produce precision, then carried by
  popularity rather than by evidence, which is two of the auto-downgrade triggers
  in relationships-communication/curator-checklist-007 firing at once. The grading
  is deliberately one band below that row, and the difference is worth stating
  because it is the kind of distinction this warehouse exists to preserve: the
  positivity ratio was shown to be an arithmetic artefact and was formally
  corrected by the journal, whereas this is a re-analysis showing insufficient
  statistical support, with no retraction, no impossibility proof, and an original
  author still defending the estimate. Those deserve different confidence and
  different language, and collapsing them would be exactly the kind of
  over-claiming the domain's checklist warns against. The layer structure gets the
  bottom band because nothing located in this sprint supports it -- and it is
  worth noting that it is quoted with MORE confidence than the number it is
  derived from, which is a reliable marker of folklore. Marked contested for the
  honest reason: the underlying scientific question is genuinely open, and this
  row refutes a derivation, not a hypothesis.
---

# relationships-communication/dunbar-number-not-derivable-015

The claim that a person can maintain about a hundred and fifty relationships
comes from extrapolating a regression line -- one relating brain size to group
size across primate species -- out to humans.

A 2021 re-analysis asked whether that extrapolation actually supports a number.
Using complementary datasets and two different statistical approaches, it got
point estimates of roughly sixty-nine to a hundred and nine by one method, and
sixteen to forty-two by the other. The two methods disagree with each other by
about a factor of four. And the confidence intervals were four to five hundred
and twenty, and two to three hundred and thirty-six.

The intervals are the finding. A range from four to five hundred and twenty does
not mean the true answer sits somewhere in the middle; it means the method cannot
resolve this question at all. The authors put it directly: specifying any one
number is futile, and a cognitive limit on human group size cannot be derived
this way.

So the right correction is not "the real number is seventy, not a hundred and
fifty". That would be making the same mistake at a different value. The
correction is that no number comes out of this.

Be honest about the status, though. This is a live dispute, not a closed case.
There has been no retraction, nobody has shown the arithmetic to be impossible,
and the original proponent still defends the estimate on grounds that do not rest
only on the brain-size regression. What the re-analysis settles is narrower and
still enough for practical purposes: the derivation that gave the number its
authority does not support it. Say it cannot be derived the usual way. Do not say
it has been disproved.

The nested layers -- five intimates, fifteen close friends, fifty friends, a
hundred and fifty acquaintances -- are quoted with even more confidence than the
headline figure, and have even less behind them. Nothing found in this pass
validates them. If the top number does not come out of the regression, a scaled
series of sub-layers from the same framework inherits the problem. The contact
rhythms often attached to each layer have no source whatsoever.

And the practical point, for anything holding a large list of people: there is no
established ceiling. A roster of a hundred and fifteen people is not near
capacity, because no capacity has been established, and the count in a contact
list is not even the same construct as the group size in a primate regression.
The number of people on file is bookkeeping. It is not a diagnosis.
