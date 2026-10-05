---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (leisure domain opening).
# The measurement item. Every other item in this domain rests on somebody
# answering a question about their own time, so this one governs how much any
# of those answers is worth. Lane: @cultural-life (VC-C).
id: leisure/self-report-measurement-005
domain: leisure
grade: "B (that stylized recall estimates of time use are systematically biased relative to same-respondent diaries, at the magnitudes stated, for the activity measured); C (extending that conclusion from housework to leisure and hobby time, which is an inference from the instrument rather than a measurement)"
lane: "@cultural-life"
locale: universal
as_of: 2004-2008
contested: no
sources:
  - "Kan, M. Y. and Pudney, S. (2008). Measurement Error in Stylized and Diary Data on Time Use. Sociological Methodology 38(1), 101-132. https://doi.org/10.1111/j.1467-9531.2008.00197.x"
  - "Kahneman, D., Krueger, A. B., Schkade, D. A., Schwarz, N. and Stone, A. A. (2004). A Survey Method for Characterizing Daily Life Experience: The Day Reconstruction Method. Science 306(5702), 1776-1780. https://doi.org/10.1126/science.1103572"
  - "nutrition/self-report-underreporting-007"
  - "framework:GRADE -- a within-respondent comparison of two instruments applied to the same people is the correct design for this question and is what Kan and Pudney ran. It establishes the bias for the activity it measured. Carrying it across to leisure is an argument about the instrument, not a second measurement, and is graded one band lower on that basis."
refraction_notes:
  - note: >
      The demonstrated finding, stated exactly and in its own scope. Comparing
      stylized recall-questionnaire estimates against diary estimates from the
      SAME respondents in a British survey, Kan and Pudney found systematic bias
      in the stylized estimates and large random error in BOTH. For hours spent
      on household chores, stylized estimates exceeded diary estimates by about
      0.79 hours for women and 1.96 hours for men. The activity measured was
      housework, not leisure.
    grade: B
  - note: >
      Why this is worse than ordinary noise. The error is not classical. It is
      systematic, it differs by sex, and it therefore does not merely widen a
      confidence interval -- it biases coefficients when the time variable is
      used as an outcome, as a predictor, or in a cross-tabulation, which are
      the three uses Kan and Pudney work through. An assistant that treats a
      stated hours-per-week figure as a noisy but unbiased measurement of the
      real number is making the specific error this paper documents.
    grade: B
  - note: >
      The transfer to leisure is an inference and is labelled as one. Nobody in
      these sources measured hobby hours. The reason to expect the same failure
      is that the instrument is identical -- a global recall question about a
      recurring activity with fuzzy boundaries -- and leisure has an additional
      hazard housework does not: the boundary of the activity is itself
      contested by the respondent. Whether scrolling counts as reading, whether
      band practice counts as playing, whether drinking with friends is a hobby
      or a social obligation are all category decisions the respondent makes
      before answering.
    grade: C
  - note: >
      The remedy that exists, and its cost. The Day Reconstruction Method
      (Kahneman et al., 2004) reconstructs the previous day as a sequence of
      episodes and asks about each one, which recovers much of what a diary
      gives without the burden of keeping a diary. That is the design an agent
      should imitate when accuracy matters: ask about yesterday episode by
      episode, not about a typical week in the abstract.
    grade: B
  - note: >
      OPERATIVE RULE for anything downstream. Self-reported leisure hours are
      usable for direction and for change within one person over time, and are
      not usable as levels, as between-person comparisons, or as inputs to
      arithmetic that is then reported back as fact. "You have said this three
      weeks running" is supported. "You spend 6.5 hours a week on this" is not.
    grade: B
claim: >
  Self-reported time-use figures are systematically wrong, not merely noisy, and
  every claim in this domain that rests on one inherits the problem. Kan and
  Pudney (2008) compared stylized recall-questionnaire estimates with diary
  estimates collected from the SAME respondents in a British survey and found
  systematic bias in the stylized estimates plus large random error in both: for
  household chores, stylized estimates exceeded diary estimates by roughly 0.79
  hours for women and 1.96 hours for men. Because the error is systematic and
  differs by respondent characteristics rather than being classical noise, it
  biases analyses in which the time variable is a dependent variable, an
  explanatory variable, or the basis of a cross-tabulation. The measured
  activity was housework; extending the conclusion to leisure and hobby time is
  an inference from the shared instrument, strengthened by the fact that leisure
  has an extra source of error housework lacks -- the respondent must first
  decide what counts as the activity. The available remedy is the Day
  Reconstruction Method (Kahneman et al., 2004), which reconstructs the previous
  day episode by episode instead of asking for a typical-week total. The
  operative rule: treat self-reported leisure hours as usable for direction and
  for within-person change, and never as levels, between-person comparisons, or
  arithmetic inputs to be reported back as fact.
reasoning: >
  This item is placed early in the domain on purpose, because it is upstream of
  almost everything else here. Leisure, hobby and drinking research is dominated
  by asking people how much of something they do, and if that question does not
  return the number it appears to return then a great many downstream findings
  are measuring an instrument. The design that settles it is the within-
  respondent one -- same people, both instruments -- and that is what is cited,
  rather than a study comparing survey populations, which could not separate
  instrument from sample. The honest weak point of the item is that the
  demonstrated activity is housework, and it is graded and labelled accordingly
  instead of being quietly generalised: the extension to leisure is argued from
  the shared instrument, and the argument is shown so a reader can reject it.
  The Day Reconstruction Method is included not as a finding but as the
  actionable half -- it tells an agent what to ask instead. And the operative
  rule is written as a permission plus a prohibition rather than as a caution,
  because a caution would be ignored: direction and within-person change stay
  available, levels and cross-person comparisons do not.
---

# leisure/self-report-measurement-005

Ask someone how many hours a week they spend on something and the number you get
back is not a measurement of that. It is a different quantity with a bias in it.

The cleanest demonstration puts both instruments on the same people. In a British
survey, respondents were asked the usual recall question -- roughly how many hours
do you spend on housework -- and also kept a diary. The recall answers came in
high: by about three quarters of an hour a week for women, and by nearly two
hours for men. Both instruments also carried large random error, but the recall
one carried something worse: a bias that differs by who is answering.

That distinction is the whole point. Random noise widens your uncertainty. A
bias that varies by respondent bends your conclusions. When the time figure is
used as an outcome, as a predictor, or simply cross-tabulated against something
else, the answer moves in a direction determined by the error rather than by the
world.

The study measured housework, not hobbies. Carrying it across is an argument
rather than a second measurement, and it should be visible as one. The argument
is that the instrument is the same -- one global question about a recurring
activity with soft edges -- and that leisure has an extra problem housework does
not. Before a person can answer how much they read, they have to decide whether
scrolling counts. Before they can answer how much they play, they have to decide
whether band practice counts. Before they can answer how much they drink, they
have to decide whether the work dinner counts. The category call happens first,
silently, and it is not stable across people or across weeks.

There is a better instrument and it is worth knowing. Reconstructing yesterday as
a sequence of episodes, and asking about each episode, recovers most of what a
diary gives without asking anyone to keep one. That is the shape to imitate: ask
about yesterday, in pieces, not about a typical week in the abstract.

What this permits and forbids, concretely. Direction is fine. Change within one
person over time is fine. Saying "that is the third week you have told me this"
is fine. Saying "you spend six and a half hours a week on this", comparing that
figure to someone else's, or feeding it into a calculation and reporting the
result as a fact, is not.
