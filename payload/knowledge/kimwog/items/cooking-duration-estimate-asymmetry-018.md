---
# Authored 2026-09-02 (cooking-session craft sprint). @test-kitchen, universal.
# The item that says WHERE buffer goes and, more importantly, refuses the
# fashionable justification for putting it everywhere. The planning-fallacy
# literature is real, was read in the primary, and does NOT license inflating a
# user's stated cooking times -- a distinction the 2012 review makes explicitly
# and that popular repetitions of the finding erase.
id: cooking/duration-estimate-asymmetry-018
domain: cooking
lane: "@test-kitchen"
grade: B (deterministic bound; the behavioural half is contested and fenced)
locale: universal
as_of: 1994-2012
contested: yes
sources:
  - "https://web.mit.edu/curhan/www/docs/Articles/biases/67_J_Personality_and_Social_Psychology_366,_1994.pdf"  # Buehler R, Griffin D, Ross M. Exploring the "Planning Fallacy": Why People Underestimate Their Task Completion Times. Journal of Personality and Social Psychology 1994;67(3):366-381. PDF retrieved and the Study 1 method and results read directly 2026-09-02; the numbers below are read out of Table 1 and the Results section, not from a secondary write-up
  - "https://doi.org/10.1037/a0025996"  # Halkjelsvik T, Jorgensen M. From origami to software development: a review of studies on judgment-based predictions of performance time. Psychological Bulletin 2012;138(2):238-271. PMID 22061688. Abstract retrieved verbatim via Europe PMC 2026-09-02; the full text was NOT read in this pass (see refraction note). Source for the performance-time versus completion-time distinction, the field asymmetry, and the artefact caution
  - "source:cooking/timeline-backward-pass-016 -- the computation these estimates feed, and the invariant that forbids repairing a shortfall by trimming them"
  - "source:cooking/parallelism-resource-claim-017 -- the barriers, which is where the omitted time actually lives"
refraction_notes:
  - note: >
      THE DETERMINISTIC HALF IS THE ONLY PART THAT NEEDS NO EVIDENCE. A sum over
      a subset of a set of non-negative quantities is at most the sum over the
      whole set. Stated cooking and prep times omit steps -- coming to
      temperature, fetching, washing, the transitions between steps -- and every
      omitted step has a duration of zero or more. Therefore a timeline summed
      from stated times is a lower bound on elapsed time and the error is
      one-signed. Buffer is ADDED, never subtracted. That conclusion does not
      depend on any psychology at all, and it should be spoken without borrowing
      any.
    grade: A
  - note: >
      THE FAMOUS RESULT IS A COMPLETION-TIME RESULT AND A COOKING STEP IS A
      PERFORMANCE-TIME ESTIMATE. The 2012 Psychological Bulletin review states
      that many studies fail to distinguish performance-time predictions, such as
      how many hours of work a task takes, from completion-time predictions, such
      as a delivery date, and it summarises them separately. "How long does this
      braise take" is the first kind. "When will dinner be on the table" is the
      second. Transferring the thesis-deadline finding onto a braise duration is
      exactly the conflation the review names. Do not do it, and do not let a
      module apply a blanket multiplier to the user's stated cooking times on the
      strength of it.
    grade: B
  - note: >
      THE UNIVERSAL VERSION OF THE FINDING IS NOT SUPPORTED. The same review
      reports that underestimation was more frequently reported than
      overestimation in the engineering and management literature but that this
      was NOT the case in the psychology literature, and it questions the
      recurrent claim that small tasks are overestimated and large tasks
      underestimated, noting this can to some extent be a statistical artefact
      caused by random error. So "people always underestimate how long things
      take" is a popular compression of a field-dependent and partly artefactual
      picture. This item is flagged contested for that reason and not because
      Buehler is doubted.
    grade: B
  - note: >
      THE SECOND HALF OF STUDY 1 IS THE DESIGN-RELEVANT HALF. Respondents were
      also asked to predict when they would finish if everything went as poorly as
      it possibly could. That pessimistic estimate averaged 48.6 days against an
      actual 55.5 -- still short. A module therefore cannot repair an optimistic
      estimate by asking the user for a worst case, because in the one study read
      here the worst case was also optimistic. Buffer has to come from structure,
      not from a second question.
    grade: B
  - note: >
      PROVENANCE LIMITS ON BOTH SOURCES, STATED RATHER THAN SMOOTHED. Buehler
      Study 1 is 37 Canadian undergraduates on one task type in 1994, with 33
      retained in the analysis, and no replication check was performed in this
      pass. For the 2012 review only the abstract was retrievable; the full text
      was not read, so nothing is quoted from it beyond what the abstract itself
      states, and no effect size is taken from it. Neither source is about
      cooking, and the extension to a kitchen is by argument rather than by
      measurement.
    grade: C
claim: >
  A cooking timeline summed from the durations a recipe or a user states is a
  LOWER BOUND on elapsed time, not an estimate, because the steps such times omit
  -- coming to temperature, fetching and washing, the transitions between steps --
  all have non-negative duration. The error is therefore one-signed, and buffer
  must be added rather than subtracted. That much is arithmetic and needs no
  evidence. What must NOT be added on top of it is a blanket padding factor
  justified by the planning fallacy. Buehler, Griffin and Ross (1994) is real and
  its Study 1 is striking: 37 Honors Thesis students predicted, on average, that
  they would finish in 33.9 days and actually took 55.5; fewer than a third
  (29.7 percent) finished within their own best prediction; and even their
  explicitly pessimistic estimate, 48.6 days, fell short of the actual. But
  Halkjelsvik and Jorgensen's 2012 Psychological Bulletin review reports that
  underestimation was more frequently reported than overestimation in the
  engineering and management literature and that this was not the case in the
  psychology literature, questions the recurrent small-task-overestimated /
  large-task-underestimated pattern as partly a statistical artefact of random
  error, and states that many studies fail to distinguish performance-time
  predictions from completion-time predictions. A cooking step duration is a
  performance-time prediction; the famous result is a completion-time result. The
  operational consequence: put buffer at the points where the arithmetic says
  something is missing, which is the barriers, and do not apply a multiplier to
  the user's stated cooking times.
reasoning: >
  A timeline builder needs to know where slack should be inserted, and there are
  two candidate justifications with very different standing. The first is
  arithmetic: stated times omit steps, omitted steps take a non-negative amount of
  time, so the sum is a lower bound and the error can only run one way. That is
  airtight, needs no citation, and is enough on its own to establish that buffer
  is added and never subtracted. The second is the planning fallacy, which is the
  justification a designer will reach for, and which does not support what it is
  usually used to support. The 1994 primary was read directly and its numbers are
  not in doubt. The 2012 review is the reason the finding cannot be lifted onto
  cooking steps: it separates predictions of how long work takes from predictions
  of when work will be delivered, reports the underestimation pattern as
  field-dependent rather than universal, and warns that part of the familiar
  small-versus-large pattern may be a regression artefact. A cooking step is the
  first kind of prediction and the famous study measured the second. The item is
  flagged contested to mark that the behavioural half is genuinely disputed
  territory, not to cast doubt on the arithmetic. The most useful thing in the
  1994 study for a module is the part nobody quotes: asking for a worst case did
  not fix the bias, so a module cannot buy safety by asking the user a second,
  more pessimistic question.
---

# cooking/duration-estimate-asymmetry-018

Buffer belongs in a cooking timeline. The interesting question is why, because
the two available reasons are not equally good and only one of them survives
contact with the literature.

The good reason is arithmetic. A recipe states cooking times and prep times. It
does not state the time to bring the oven up, or to find the colander, or to wash
the board between two things, or the seconds that leak away at every transition.
Each of those takes zero or more minutes. Add up only the steps that were stated
and you have added up a subset of a set of non-negative numbers, so what you have
is a lower bound on the elapsed time, and the error can only run one way. Buffer
is added. Never subtracted. Nothing psychological is needed to reach that, and it
tells you where the buffer goes as well: at the barriers, which is where the
omitted time actually lives.

The tempting reason is the planning fallacy, and this is where care is required.

The original finding is real and was read in the primary. Buehler, Griffin and
Ross asked 37 students near the end of an Honors Thesis course to predict as
accurately as they could when they would hand in. They predicted 33.9 days on
average. They took 55.5. Fewer than a third finished within their own best
prediction. And the detail most worth having: the researchers also asked what
would happen if everything went as poorly as it possibly could, and that
pessimistic estimate averaged 48.6 days -- still short of the real 55.5.

But the 2012 review of this literature is the reason that finding cannot simply
be dropped onto a braise. It reports three things that a popular retelling
flattens. Underestimation showed up more often than overestimation in the
engineering and management studies, and that was not the case in the psychology
studies -- the pattern is field-dependent, not a law. The familiar claim that
small tasks get overestimated and large tasks underestimated may be, in part, a
statistical artefact of random error. And many studies fail to distinguish
predictions of how long the work itself takes from predictions of when it will be
delivered.

That last one is decisive here. "How long does this braise need" is a prediction
about the work. "When will dinner be on the table" is a prediction about delivery.
The thesis study measured the second. A module that pads every stated cooking
time by a fixed factor because of it has moved a finding across the exact seam
the reviewers say people keep crossing without noticing.

So: buffer where the arithmetic says something is missing. Do not multiply the
user's cooking times. And take the pessimism result seriously in the other
direction too, because it constrains the design -- asking the user for a worst
case does not fix an optimistic estimate. In the one study read here, the worst
case was optimistic too. Buffer has to come from the structure of the plan, not
from a second question.

Both sources are held at arm's length where they should be. The 1994 study is 37
Canadian undergraduates on one task in one year, 33 of them retained in the
analysis, and no replication check was run in this pass. For the 2012 review only
the abstract could be retrieved, so nothing is claimed from it beyond what the
abstract says and no effect size is taken from it. Neither one is about cooking.
The step from them to a kitchen is an argument, and it is the argument for
refusing a transfer rather than for making one.
