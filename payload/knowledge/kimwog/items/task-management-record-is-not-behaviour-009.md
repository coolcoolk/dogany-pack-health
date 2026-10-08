---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# Read in full text at PMC. The 32%-of-days figure and the 92% reported
# compliance for those same days are quoted from the paper's own results and
# are the pair that makes this item load-bearing.
id: task-management/record-is-not-behaviour-009
domain: task-management
grade: B (randomised comparison with a covert objective validator; clinical diary protocol, n = 80)
lane: "@behavioral-productivity"
locale: universal
as_of: 2002
contested: no
sources:
  - "https://doi.org/10.1136/bmj.324.7347.1193"
  - "Stone, A. A., Shiffman, S., Schwartz, J. E., Broderick, J. E., & Hufford, M. R. (2002). Patient non-compliance with paper diaries. BMJ, 324(7347), 1193-1194."
refraction_notes:
  - note: >
      This is a clinical protocol with externally imposed entry times (10am,
      4pm, 8pm within a 15-minute window) and n = 80 chronic-pain patients. A
      person keeping their own task system has different motivation and no
      external schedule. What transfers is the STRUCTURE of the failure -- the
      record and the behaviour diverge, in both directions, and the record's
      own account of itself is the least reliable part. The rates do not
      transfer.
    grade: C
claim: >
  A record of an action is a separate thing from the action, and the two come
  apart in both directions. In a randomised comparison, 80 patients kept either
  a paper diary or an electronic one; unknown to them, the paper binder
  contained a photosensor logging every time it was opened. Reported compliance
  with the paper diary was 90%; actual compliance was 11% (within a 30-minute
  window; 20% within 90 minutes). On 32% of days the binder was never opened at
  all -- and reported compliance for those same days was 92%. Roughly 75% of
  paper-diary participants filled entries in retrospectively at least once
  ("hoarding"). The electronic diary, which timestamped entries as they were
  made, achieved 94% actual compliance, which the authors note rules out the
  sample and the burden of the protocol as explanations for the paper result.
reasoning: >
  Graded high because of the design rather than the size: a covert objective
  validator running underneath a self-maintained record is the only way this
  question can be answered, and this study has one. Held one band below the top
  for n = 80 in a single clinical protocol. This is the item that a task or
  calendar agent must have before it interprets any completion field, and it is
  placed in this lane specifically because of a live incident in the system
  this warehouse serves -- an anomaly detector read "not yet marked done" as
  "did not do it" and pushed a false accusation at the owner. The paper shows
  the same gap opening in BOTH directions at once: work recorded as done that
  was not done, and, in the electronic arm, that the gap closes when the
  timestamp is produced by the instrument rather than by the person.
---

# task-management/record-is-not-behaviour-009

The cleanest measurement of the gap between a record and the behaviour it
claims to describe comes from a study where patients kept a paper diary that,
without their knowledge, logged every time it was opened.

They reported completing 90% of the required entries. The sensor showed 11%
were actually made in the required window. On nearly a third of days the diary
was never opened at all -- and for those same days, reported compliance was
92%. Three-quarters of participants filled in entries after the fact at least
once.

The control arm is what makes this decisive rather than merely embarrassing.
The same protocol, with an electronic diary that timestamped entries as they
were made, produced 94% real compliance. So the failure was not the people and
not the burden of the protocol. It was that a self-maintained record has no
mechanism forcing it to correspond to what happened.

For any system reading a task store, this is the governing distinction, and it
cuts both ways:

- A completed marker is a claim that something was done. It is not evidence
  that it was done, and it is not evidence of WHEN it was done.
- An absent marker is not evidence that something was not done. Absence in a
  self-maintained record is produced by the recording process failing, at least
  as often as by the behaviour failing.

The second half of that is the one that causes harm. In this very system, an
anomaly detector read "not yet marked done" as "did not do it" and pushed a
false accusation at the owner. That is exactly the inference this study
forbids: on 32% of days the record showed nothing and the person's own account
was that everything had been done. An unmarked item licenses a QUESTION, never
a conclusion, and never an accusation.

The design consequence is that state changes an instrument can produce itself
-- a timestamp written when the work actually starts or ends -- are a different
and better class of evidence than a status field a person updates later. Where
only the person's field exists, the honest reading of a gap is "unknown", not
"not done".
