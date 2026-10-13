---
# Collection sprint 2026-09-02, relationships-communication lane expansion.
# Scope-driven: the consumer of this lane holds a person roster with recorded
# relations, which makes "is the stored closeness the real closeness" a live
# operational question rather than a curiosity. This row is deliberately graded
# LOW despite how well-known the finding is, because the primary study is 84
# students -- the honest position is that the direction is credible and the
# magnitude is not warehouse-grade. Included with that flag rather than
# excluded, because the alternative is an agent that silently treats a stored
# relation as symmetric.
# Rubric: relationships-communication @dyadic (VC-C).
id: relationships-communication/tie-reciprocity-perception-gap-012
domain: relationships-communication
grade: C (that self-perceived friendship ties are systematically over-assumed to be reciprocal); D (the specific 53 pct reciprocity figure as a population estimate)
lane: "@dyadic"
locale: universal
as_of: 2016
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/27002530/"  # Almaatouq A, Radaelli L, Pentland A, Shmueli E. 2016, PLoS ONE 11(3):e0151588, doi 10.1371/journal.pone.0151588, PMCID PMC4803335 -- 84 participants, reciprocity survey; 413/775 nominated edges reciprocal (53 pct); 1273/1353 nominations expected to be reciprocated (94 pct)
  - "https://pubmed.ncbi.nlm.nih.gov/30183512/"  # Boothby EJ, Cooney G, Sandstrom GM, Clark MS. 2018, Psychol Sci 29(11):1742-1756, doi 10.1177/0956797618783714 -- the liking gap, five studies including a months-long dorm-mate cohort
  - "relationships-communication/curator-checklist-007"  # the domain rule applied here: small-n social-psychology findings get the observational band and an explicit sample annotation, never a headline percentage
  - "framework:GRADE -- the direction is graded at the observational band and the magnitude one lower, for a reason that should not be smoothed over. The primary source is a single study of 84 people in one university course. Its internal numbers are exact and checkable (413 of 775 edges; 1273 of 1353 nominations; r=0.95 expected versus r=0.36 actual), which is why it is usable at all, but n=84 in one classroom is not a basis for a population reciprocity rate. The paired source (Boothby 2018) is much stronger -- five studies including a months-long cohort -- but measures a DIFFERENT bias, so it corroborates the general theme rather than this specific number."
refraction_notes:
  - note: >
      The exact figures and the exact sample, together, because either without
      the other misleads. In a reciprocity survey of 84 participants -- early
      career adults aged 23 to 38 taking a single university course in applied
      management, 40 percent male -- only 53 percent of nominated friendship
      edges were reciprocal (413 of 775). Meanwhile, in 94 percent of cases
      (1,273 of 1,353) where a subject nominated someone as a friend, they also
      expected to be nominated back. The correlation between how a person rated
      someone and how they PREDICTED that person would rate them was r=0.95; the
      correlation between the two people's ACTUAL ratings was r=0.36. That is the
      whole finding: expectation of symmetry is near-perfect, actual symmetry is
      moderate at best.
    grade: C
  - note: >
      CONTESTED as a number, not as a direction. "Only half your friendships are
      mutual" circulates as a fact about human relationships; what exists behind
      it, in the source located this sprint, is one classroom. A reciprocity rate
      is a property of a particular network and a particular nomination
      threshold, and it will differ between a university cohort, a workplace, and
      a long-standing personal roster. Cite the direction. Do not cite 53 percent
      as a rate that applies to anyone's own contact list.
    grade: D
  - note: >
      The perception error is DIRECTIONAL, which is the part with operational
      consequences. People are not randomly wrong about their ties; they are
      systematically biased toward assuming symmetry. For anything holding stored
      relations, the implication is concrete: a stored relation is one person's
      report, and treating it as a mutual fact imports a known bias. This is the
      social-graph twin of nutrition/self-report-underreporting-007 -- the
      instrument is a person reporting on themselves, and it errs in a consistent
      direction rather than noisily.
    grade: C
  - note: >
      The paired bias runs the OTHER WAY for new acquaintances, and confusing the
      two produces the wrong advice. Boothby et al. 2018 documents the liking gap:
      after conversations, people systematically UNDERESTIMATE how much their
      partner liked them and enjoyed their company. This was observed as strangers
      got acquainted in the laboratory, as first-year students got to know dorm
      mates, and among previously unacquainted adults in a workshop, and it
      persisted for several months in the dorm-mate cohort. So the two errors do
      not cancel into a single "people misjudge relationships" rule: in
      ESTABLISHED nominations people over-assume reciprocity, and in NEW
      interactions they under-assume being liked. Which correction applies depends
      on the stage of the tie.
    grade: B
  - note: >
      NOT established here: that unreciprocated ties are harmful, that
      reciprocity should be measured, or that anyone should be told their
      friendships are one-sided. The source is about the limits of using perceived
      networks to propagate influence, not about wellbeing, and no source in this
      row links tie asymmetry to any outcome. An agent that used this to inform a
      user which of their relationships are not mutual would be inventing both the
      measurement and the harm.
    grade: D
claim: >
  Perceived social ties are systematically over-assumed to be mutual, and the
  error is directional rather than random. In the primary study located (Almaatouq
  et al. 2016, PLoS ONE; 84 participants in a single university course, aged
  23-38), only 53 percent of nominated friendship edges were reciprocal (413 of
  775), while in 94 percent of nominations (1,273 of 1,353) the nominator
  expected to be nominated back. The correlation between a person's rating of
  another and their PREDICTION of that person's rating was r=0.95; the
  correlation between the two ACTUAL ratings was r=0.36. Treat the DIRECTION as
  usable and the 53 percent as a property of that one classroom network, not a
  population reciprocity rate. The complementary bias runs the opposite way at
  the start of a tie: Boothby et al. (2018, Psychological Science; five studies
  including a months-long dorm-mate cohort) find people systematically
  UNDERESTIMATE how much new conversation partners liked them, an effect that
  persisted for months. So which correction applies depends on tie stage --
  over-assumed symmetry in established nominations, under-assumed liking in new
  ones. Nothing here establishes that asymmetric ties are harmful or that anyone
  should be told a relationship is one-sided.
reasoning: >
  This row is included because of what its consumer holds, and graded down
  because of what its source is. A life agent that stores people and recorded
  relations is, whether or not it says so, maintaining a perceived network -- and
  the perceived network is exactly the object this literature says is biased. The
  question "is the stored closeness the real closeness" therefore has operational
  stakes, and leaving the domain silent on it means the agent defaults to
  treating one person's report as a mutual fact. That is the failure this row
  exists to block. Against that, the primary source is a single study of 84 people
  in one classroom, and the warehouse's own curator checklist calls for
  observational-band grading with an explicit sample annotation rather than a
  headline percentage. Both grades follow from that: the direction is credible
  because the internal numbers are exact, checkable, and mutually consistent (the
  r=0.95 versus r=0.36 contrast is not the kind of pattern that emerges from
  noise), while the 53 percent figure is a property of one network at one
  nomination threshold and is graded at the bottom band precisely to stop it being
  quoted as a rate. Marked contested for that reason alone -- the direction is not
  disputed, the number is over-circulated relative to what supports it. The
  Boothby pairing is deliberate and is the more useful half operationally: without
  it, this row would read as a general "people are wrong about relationships"
  claim, when in fact the error reverses sign depending on whether the tie is new
  or established, and an agent applying the wrong correction to the wrong stage
  would give exactly backwards advice.
---

# relationships-communication/tie-reciprocity-perception-gap-012

A stored relationship is one person's report. The literature on perceived social
networks says that report is biased in a specific direction, and the direction
flips depending on how old the tie is.

For established ties, people over-assume that the feeling is mutual. In the study
this rests on, participants nominated people as friends, and only about half of
those nominations were returned. Meanwhile, in ninety-four percent of cases the
nominator expected the nomination to be returned. The tell is in the two
correlations: how a person rated someone tracked their prediction of the other
person's rating almost perfectly, while the two people's actual ratings tracked
each other only moderately. People are confident about symmetry that is not
there.

The sample matters and should be stated whenever this is used. It is eighty-four
people in one university course. The exact reciprocity figure is a property of
that classroom, not a fact about anybody's contact list, and the widely repeated
version -- "only half your friendships are mutual" -- is quoting a number with
one small network behind it. The direction is worth carrying. The percentage is
not.

For new ties, the error runs the other way. After conversations with people they
had just met, participants systematically underestimated how much the other
person liked them and enjoyed their company. This showed up with strangers in the
lab, with first-year students meeting dorm mates, and with adults at a workshop,
and among the dorm mates it lasted for months. That evidence base is considerably
stronger than the reciprocity one.

So there is no single "people misjudge their relationships" rule. In established
nominations, the bias is toward assuming more mutuality than exists. In new
interactions, the bias is toward assuming less warmth than exists. Applying the
wrong correction to the wrong stage produces advice that is exactly backwards.

One thing this must not become. Nothing here shows that one-sided ties are
harmful, that reciprocity is worth measuring, or that anyone should be told which
of their friendships are not returned. The source is about the limits of
propagating influence through perceived networks. The harm would have to be
invented, and so would the measurement.
