---
# STUDY-CRAFT LANE (VC-E). The gap this item closes was named explicitly when
# the lane was commissioned: the training lane has an answer for a missed
# session and the study lane has none. This is that answer. It is assembled
# from two measured findings and one documented practitioner procedure, and the
# joins between them are labelled as joins.
id: learning-habits/lapse-is-not-a-reset-015
domain: learning-habits
grade: D (practitioner-heuristic)
lane: "@study-craft"
locale: universal
as_of: 2008-2026
contested: yes
sources:
  - "https://doi.org/10.1111/j.1467-9280.2008.02209.x"  # Cepeda et al. 2008: the overshoot asymmetry, read at source
  - "https://doi.org/10.1371/journal.pone.0120644"  # Murre, J. M. J., & Dros, J. (2015). Replication and Analysis of Ebbinghaus' Forgetting Curve. PLoS ONE, 10(7), e0120644 -- savings on relearning
  - "https://docs.ankiweb.net/deck-options.html"  # the documented backlog procedure, read at the application's own manual
  - "learning-habits/interval-from-retention-target-014"  # within-warehouse cross-ref: same lane, supplies the asymmetry this item leans on
  - "learning-habits/21-day-myth-refuted-003"  # within-warehouse cross-ref: the evidence lane on how long habits take, against which streak folklore is measured
  - "framework:GRADE -- NO study of any kind compares backlog-recovery strategies against each other. The two empirical legs bound the COST of a lapse; the recovery procedure itself is one application's documented practice, and is graded accordingly."
claim: >
  A missed stretch of study is a delay, not a deletion, and the standard
  reactions to it -- restart the deck, reset the schedule, abandon the material
  -- are all more expensive than doing nothing special. Two measurements bound
  the cost. Cepeda et al. (2008) found the penalty curve asymmetric: "while
  there are costs to using a gap that is longer than the optimal value, these
  costs are much smaller than the costs of using too small a gap value", so an
  overdue review is on the CHEAP side of the error. Murre & Dros (2015), a
  close replication of Ebbinghaus, measured savings on relearning still
  positive at every interval tested, 0.421 at 20 minutes down to 0.090 at 31
  days -- material that tests as forgotten is still cheaper to relearn than
  material never learned. The recovery procedure that follows is practitioner
  practice, not a tested protocol: STOP INTRODUCING NEW MATERIAL until the
  backlog clears (the Anki manual's own instruction: "If you have a backlog of
  overdue review cards, it is recommended that you stop introducing new cards
  until you catch up with that backlog"), work the backlog most-likely-forgotten
  first rather than oldest-first, and do not bulk-reschedule or reset. Refuse
  streak metrics: they price a lapse as a catastrophe when the measured cost is
  small, and nothing was located that measures a streak device in a study
  context at all.
reasoning: >
  The two empirical legs are real and are doing limited, specific work. The
  Cepeda asymmetry is a direct read of a large experiment and is the strongest
  single fact available for lapse policy: it says overshooting an interval is
  the forgiving direction. The Murre & Dros savings figures are a faithful
  replication of Ebbinghaus and establish that relearning is not relearning
  from zero -- but that study is ONE subject relearning nonsense syllables, and
  its authors say so, noting it remains unclear what the shape of forgetting
  would be with other subjects and whether their subject's memory was
  exceptional. It is cited here only for the direction of the savings effect,
  never for a magnitude that anyone should plan against.
  .
  The procedure itself is graded at the practitioner band because that is
  honestly what it is. The Anki manual's backlog guidance is a documented,
  long-used, widely-followed practice with a stated rationale ("continuing to
  introduce new cards when you're already behind can make the backlog worse"),
  and its ordering advice is specific -- relative overdueness "is generally
  recommended if you have a large backlog that may take some time to get
  through, and you want to reduce the chances of forgetting more cards",
  against due-date order which is "the recommended order when you are up to
  date, or when you only have a small backlog". That is a documented scheme
  with an internal logic, not folklore. It is still not evidence: no study
  compares catching up against restarting, or most-overdue-first against
  oldest-first, and this item does not pretend one exists.
  .
  Marked contested because the recovery half is disputed practitioner territory
  with active disagreement about postponing, rescheduling and bulk-deferring
  tools, and because the refusal of streak devices runs directly against the
  most popular consumer study products.
---

# learning-habits/lapse-is-not-a-reset-015

Training has a settled answer for a missed session: you missed a session, the
next one is not a restart, and nothing about the plan changes except the date.
Study advice has no equivalent, so people invent one, and the invented answers
are uniformly bad -- delete the deck, start the book again, reset every
interval to day one, or quietly abandon the whole project because the streak
counter went to zero.

Two things are actually measured about this, and both say the missed days cost
less than they feel like they cost.

The first is the shape of the penalty. In the large spacing experiment behind
this lane's scheduling item, being LATE for a review is much cheaper than being
early: accuracy rises steeply as the gap widens toward its optimum and then
falls away only gradually. An overdue review sits on the gentle side of the
curve. This is the single most useful fact in the whole lane, because it means
an imperfectly kept schedule is not a broken one.

The second is that forgetting is not erasure. The careful modern replication of
Ebbinghaus measured how much time is saved on relearning material you can no
longer recall, and the saving is still there at every interval tested -- large
after twenty minutes, small but present after a month. Material that tests as
gone is still cheaper the second time. Restarting from zero prices your past
work at zero, and that price is wrong.

So the recovery procedure. It comes from the practice of the applications
people actually use, not from a trial, and it is short:

- Stop taking in new material until the backlog is gone. This is the one
  instruction the tooling states outright, on the grounds that adding intake
  while behind makes the backlog worse. It is also the point where most people
  do the opposite, because new material feels like progress and a backlog feels
  like punishment.
- Work the backlog in most-likely-forgotten-first order, not oldest-first, when
  the backlog is large enough to take a while. Oldest-first is the right order
  when you are current or barely behind.
- Do not reset, do not bulk-reschedule, and do not "clean up" by deleting.
  Those actions discard the savings you already paid for.
- Expect the catch-up to take days, and let it.

And the refusal, which matters more than the procedure. Streak counters, chains
of unbroken days, and every device whose core mechanic is that a missed day
destroys something you accumulated: this lane will not carry them as study
technique. Nothing was located that measures a streak device in a learning
context. What exists is one qualitative study of recreational runners, a
preprint on streak-breaking backfire, and retention numbers published by an app
vendor about its own product. Against that, the two measured facts above both
say a missed day is cheap. A device that tells the user a missed day was
expensive is not merely unsupported, it is pointed the wrong way, and the
person most likely to be harmed by it is the one who already missed the day and
is deciding whether to come back.

Honest limit, stated plainly: nobody has run the experiment. There is no trial
comparing catching up against restarting, no trial on backlog ordering, and no
measurement of how a real person's completion rate decays across a lapse. The
cost bounds are measured; the procedure is borrowed practice with a coherent
rationale. Say it that way when using it.
