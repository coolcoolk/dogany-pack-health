---
# Collection sprint 2026-09-02, relationships-communication lane expansion.
# Methodology row, included on scope grounds: the consumer of this lane holds a
# person roster with recorded relations and logs who the owner spends time with,
# which is exactly the data shape from which "your friends are influencing you"
# conclusions get drawn. The refutation is unusually clean because it is a
# positive-control demonstration -- the same standard method finds a social
# contagion effect for HEIGHT, which nobody believes is contagious.
# Rubric: relationships-communication @dyadic (VC-C) -- methodology/negative.
id: relationships-communication/network-effect-inference-floor-017
domain: relationships-communication
grade: B (methodology/negative -- standard social-network regression detects effects for outcomes that cannot plausibly be transmitted, and those effects vanish on environmental-confounder adjustment)
lane: "@dyadic"
locale: universal
as_of: 2008
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/19056789/"  # Cohen-Cole E, Fletcher JM. 2008, BMJ 337:a2533, doi 10.1136/bmj.a2533, PMCID PMC2600605 -- Add Health subsamples, 4,300-5,400 adolescents; acne OR 1.62 (0.91-2.89), headaches 1.47 (0.93-2.33), height 0.18 (0.15-0.26)
  - "relationships-communication/curator-checklist-007"  # the auto-downgrade trigger instantiated here: an association reported without the confound structure that would make it interpretable
  - "relationships-communication/social-connection-mortality-magnitude-008"  # the neighbouring observational literature this row constrains the reading of
  - "framework:GRADE -- trial-adjacent band rather than top. The demonstration is methodologically decisive within its own frame: it is a positive-control design, it uses a large nationally-representative adolescent dataset, and it was published in a general medical journal with a reply from the authors it critiques. It is held one band below the top because it is a single paper on a single dataset in a single age group, and because it establishes that a METHOD can produce spurious results rather than that any particular published network finding IS spurious. The distinction matters and is preserved in the claim."
refraction_notes:
  - note: >
      The design is a positive control, which is what makes it decisive rather
      than merely sceptical. Cohen-Cole and Fletcher took outcomes that cannot
      plausibly spread through a friendship network -- acne, headaches, and HEIGHT
      -- and analysed them with the standard methods used in published social-
      network health studies: logistic regression controlling for own and
      friend's lagged health status, on subsamples of 4,300 to 5,400 adolescents
      from the National Longitudinal Study of Adolescent Health. Significant
      network effects appeared for all three. A friend's acne raised the odds of
      acne (OR 1.62), a friend's headaches raised the odds of headaches (1.47),
      and an individual's height rose by 20 percent of their friend's height
      (0.18, CI 0.15 to 0.26).
    grade: B
  - note: >
      The second half is what turns the demonstration into a diagnosis. After
      adjustment for environmental confounders, the results became uniformly
      smaller and insignificant. So the spurious effects were not produced by
      randomness or by a coding error; they were produced by shared environment
      being mistaken for transmission between people. Friends share schools,
      neighbourhoods, seasons, diets and exposures, and any of those will generate
      correlated outcomes with no influence passing between the individuals at
      all. The authors' conclusion: researchers should be cautious in attributing
      correlations in health outcomes of close friends to social network effects,
      especially when environmental confounders are not adequately controlled.
    grade: B
  - note: >
      What this row does and does NOT establish, stated carefully because the
      overshoot is easy and would itself be an error. It establishes that the
      METHOD can produce confident-looking effects for outcomes known to be
      untransmittable, and that environmental adjustment removes them. It does NOT
      establish that any specific published social-contagion finding is false, and
      it does not show that social influence is absent. It is a floor on
      inference, not a verdict on a literature. Homophily -- people befriending
      others already similar to them -- is a further and separate confound in the
      same direction that this design does not isolate.
    grade: B
  - note: >
      Why this belongs in a lane whose consumer holds a social graph. Any store
      that records who a person spends time with, plus outcomes about that person,
      contains exactly the raw material for the inference this paper shows to be
      unsafe: "the people you see most have property X, and so do you, therefore
      they are influencing you." The correlation may be perfectly real and still
      carry no transmission, because the store also contains the confound -- people
      seen frequently are typically colleagues, neighbours, family and people in
      the same life stage, which is shared environment by construction. The
      operative rule: a co-occurrence pattern in a personal social graph is a
      description, never a mechanism, and must never be surfaced as one.
    grade: B
  - note: >
      A note on the sample's limits, so the row is not over-extended either. The
      subsamples are adolescents in a school-based study, an age group and a
      setting where shared environment is unusually concentrated -- everyone in the
      same building on the same schedule. That arguably makes the confounding
      easier to produce here than in an adult network, so the demonstration should
      be read as establishing that the failure mode is REAL and easy to fall into,
      not as quantifying how often it occurs in adult data. The height result is
      the load-bearing one regardless of setting: no amount of shared schooling
      makes height contagious.
    grade: C
claim: >
  Standard social-network regression can produce confident-looking contagion
  effects for outcomes that cannot possibly be contagious, and this is the
  cleanest demonstration of it. Cohen-Cole and Fletcher (2008, BMJ) applied the
  methods used in published social-network health studies -- logistic regression
  controlling for own and friend's lagged health status -- to acne, headaches and
  HEIGHT, in subsamples of 4,300 to 5,400 adolescents from the National
  Longitudinal Study of Adolescent Health. All three showed significant network
  effects: a friend's acne raised the odds of acne (OR 1.62), a friend's
  headaches raised the odds of headaches (1.47), and an individual's height rose
  by 20 percent of their friend's height (0.18, CI 0.15-0.26). After adjustment
  for environmental confounders, all results became uniformly smaller and
  insignificant. The mechanism generating the spurious effects is shared
  environment being read as transmission between people. This does NOT show that
  any particular published contagion finding is false, and it does not show
  social influence is absent -- it is a floor on inference, not a verdict on a
  literature; homophily is a further confound in the same direction that this
  design does not isolate. OPERATIVE RULE for any store that records who a person
  spends time with: a co-occurrence pattern between the people in a personal
  social graph and that person's outcomes is a DESCRIPTION, never a mechanism,
  and must never be surfaced as influence.
reasoning: >
  Included for what the consumer of this lane holds rather than for general
  methodological interest. A store that records a person's contacts and who they
  spend time with, alongside outcomes about that person, is precisely the data
  shape from which the inference "the people around you are shaping you" gets
  drawn -- and it is a store in which the confound is not merely possible but
  structural, because the people someone sees most often are colleagues,
  neighbours, family and peers in the same life stage, which is shared environment
  by construction. Without this row the failure is not hypothetical; it is the
  default reading of the data the agent already has. The paper earns the
  trial-adjacent band because of its design rather than its size: a positive
  control using outcomes known to be untransmittable is a much stronger instrument
  than a critique arguing that confounding might exist, and the height result in
  particular admits no alternative explanation -- nobody catches height from a
  friend. It is held one band below the top for two honest reasons. It is a single
  paper on a single dataset, and it demonstrates that a METHOD can generate
  spurious findings rather than that any specific published finding is spurious;
  collapsing that distinction would make this row commit the same over-reach it
  exists to prevent. The adolescent school-based setting is flagged a band lower
  still, because concentrated shared environment is exactly the condition that
  makes the artefact easy to produce, so the study shows the failure mode is real
  and easy to fall into without quantifying its frequency in adult networks. Not
  marked contested: the finding itself is not disputed, and the authors it
  critiques replied in the same issue without overturning the demonstration.
---

# relationships-communication/network-effect-inference-floor-017

There is a class of finding that says your friends make you heavier, happier, or
lonelier. Here is what happened when someone ran the same analysis on outcomes
that cannot spread.

Researchers took a large adolescent health dataset and applied the standard
method from published social-network studies -- regression controlling for your
own and your friend's earlier health status -- to acne, headaches, and height.
All three came back significant. A friend's acne raised your odds of acne. A
friend's headaches raised your odds of headaches. And your height went up by about
a fifth of your friend's height.

Nobody catches height from a friend. That is the point of the design.

Then they adjusted for environmental confounders, and all three effects shrank
and lost significance. So the spurious results were not noise or a coding
mistake. They were shared environment being read as transmission. Friends occupy
the same school, the same neighbourhood, the same season, the same diet, the same
exposures -- and any of that produces correlated outcomes with nothing at all
passing between the people involved.

Be careful about what this licenses. It shows that the method can manufacture
confident-looking contagion for things known to be untransmittable, and that
environmental adjustment removes it. It does not show that any particular
published social-contagion result is wrong, and it does not show that people fail
to influence each other. It is a floor on what can be inferred, not a verdict on a
field. There is also a further confound running the same way that this design does
not separate out: people tend to befriend others who were already similar to them.

The reason this belongs in a domain about a person's relationships is that any
store recording who someone spends time with, next to outcomes about that person,
already contains the ingredients for exactly this inference. Worse, it contains
the confound by construction -- the people you see most are your colleagues, your
neighbours, your family, and people at the same stage of life as you. That is
shared environment, not influence.

So the working rule is narrow and firm. A pattern between the people in someone's
social graph and that person's outcomes is a description of a co-occurrence. It
is not a mechanism, and it must never be presented as one.

One limit on the demonstration itself: it was done on adolescents in a
school-based study, where shared environment is unusually concentrated. That
probably makes the artefact easier to produce there than in an adult network. It
establishes that the failure mode is real and easy to fall into. It does not tell
you how often it happens in adult data.
