# Changelog: Dogany Health Trainer

## 0.37.0

- Every exercise and warm-up drill now comes with numbered form cues and the
  one common mistake to avoid.
- Activation primers are off by default: the warm-up ramp does that job. A
  program preference or a joint that needs care turns them back on.
- Weight row: when the agent's chat bridge supports it, the reps keyboard
  can show a row of nearby weights, so you can log the weight you actually
  lifted with one tap. Older bridges keep the single prescribed weight.
- The weekly review lists the facts and ends with a single question.
- Undo no longer shows raw values in its messages.

## 0.36.0

- Goal consult: a calorie step before the program. It estimates your
  maintenance range from your work pattern and recent steps and proposes a
  daily target for you to confirm.
- After the last working set, the session runs the finisher, cardio and
  cooldown one block at a time. Cooldown holds have a start button and a
  countdown. A session closes only when every block is done or skipped.
- The completion card is posted automatically.
- Set buttons for each set are posted automatically, one keyboard per set,
  and undo clears them.
- Mat warm-up drills come with step-by-step instructions, and the next
  drill is cued as you finish each one.
- Plate cues on every warm-up rung, including the empty bar.
- Session minutes are taken from your logged times. The only thing it asks
  at the end is the calories from your watch.
- The pinned board keeps today's diet lines when a read fails.
- Internal kit-version notices no longer appear on the diet card.

## 0.35.1

- Warm-up rows are planned from the working weight you state, from the
  first set table on.
- Shorter pauses between warm-up sets.
- A set logged with the wrong set number is refused instead of closing the
  exercise early.

## 0.35.0

- Program consult: a side question gets a short answer and a one-line
  return to the open question, not the whole card again.
- Claims about how a lift loads a joint or muscle are checked against the
  bundled knowledge base first.
- Weeks that press on two or more days pair a flat press with a low-incline
  press.
- Running the program consult again with the same training windows keeps
  your workout calendar as it is. Only the routines that changed are
  replaced.

## 0.34.0

- New set style setting: `volume` (the default) or `intensity`, which uses
  fewer, harder working sets after untimed warm-up sets. Ask the trainer to
  switch at any time.
- Weekly set minimums for each muscle are now always met inside your
  training window.
- One lift per isolation movement in a session (for example, no two curls
  on one day), unless a weekly minimum can't be met any other way.

## 0.33.0

Includes the 0.31 and 0.32 preview builds.

- After the program is written, a short setup follows, one step per
  message: daily diet target, first session, and the times for the morning
  brief and the daily and weekly reviews (each can be turned off).
- A fuller training week: both pull planes, overhead pressing, side and
  rear delts, direct arm work, calves on two days, and at least 3 sets a
  lift for lifters with a year or more of training.
- Back-to-back sessions avoid stacking the same heavy fatigue (for example,
  a lighter row next to a deadlift day).
- Shoulder care keeps a horizontal pull in the week, adds a rotator-cuff
  drill, and removes behind-the-neck variants.
- Front/back splits put biceps work on the front days and triceps work on
  the back days.
- Diet card: during a cut the protein goal can go up to 2.4 g/kg. A
  recorded kidney condition removes the higher cut range.
- Knee pain that fits a kneecap or arthritis picture is treated as
  trainable at a low pain level.
- Program building is several times faster.
- Knowledge base update.

## 0.30.2

First public release.

- Program: a guided consult that builds a weight-training program card, and
  program review and rebalancing when things change.
- Live workout session: set-by-set guidance, set tables, rest and hold
  timers, and load progression from your own history.
- Pain and form notes during a session, with follow-up.
- Diet: a daily calorie and macro card, planned meals and protein coaching.
- 3D exercise form demos.
- Requires Dogany LifeKit 2.38.0 or later.
