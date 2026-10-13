---
# STUDY-CRAFT LANE (VC-E). The load-planning item -- the study analogue of
# exercise/volume-landmarks-heuristic-015, and graded in exactly the same way:
# the SHAPE of the relationship is sound and mechanically derivable, the
# specific multiplier is a practitioner number with no trial behind it.
#
# The ratio is quoted verbatim from the Anki manual's deck-options page, read at
# source.
id: learning-habits/review-load-follows-intake-018
domain: learning-habits
grade: D (practitioner-heuristic)
lane: "@study-craft"
locale: universal
as_of: 2026
contested: yes
sources:
  - "https://docs.ankiweb.net/deck-options.html"  # "If you are consistently learning 20 new cards a day, you can expect your daily reviews to be roughly about 200 cards/day." -- read at source
  - "learning-habits/interval-from-retention-target-014"  # within-warehouse cross-ref: the schedule this load is the arithmetic consequence of
  - "learning-habits/lapse-is-not-a-reset-015"  # within-warehouse cross-ref: an unsustainable intake rate is the usual upstream cause of the lapse that item handles
  - "framework:GRADE -- a single application's published rule of thumb. No study derives the multiplier, no study validates it, and it is a property of one scheduler's parameters rather than of memory. Same evidential position as the per-muscle numbers in exercise/volume-landmarks-heuristic-015: usable scaffold, unverified number."
claim: >
  Daily study load is not chosen on the day; it is set weeks earlier by the
  intake rate, and the multiplier is large. The Anki manual states it directly:
  "If you are consistently learning 20 new cards a day, you can expect your
  daily reviews to be roughly about 200 cards/day", with the mechanism given as
  "studying new cards will temporarily increase the number of reviews you need
  to do a day, as newly-learned material needs to be repeated a number of times
  before the delay between repetitions can increase appreciably", and the lever
  named as "you can decrease the reviews required by introducing fewer new
  cards each day until your review burden decreases". Practical consequence: an
  intake decision is a standing daily-time commitment at roughly an order of
  magnitude, it arrives with a lag of weeks, and the only durable way to fix an
  unsustainable load is to cut intake -- not to work faster or raise the daily
  cap. The specific ten-to-one figure is a practitioner number tied to one
  scheduler's defaults and must never be presented as a measured constant.
reasoning: >
  The SHAPE of this relationship is not in doubt and does not need a study: any
  scheduler that repeats new material several times before intervals lengthen
  will accumulate a steady-state review queue that is a multiple of the intake
  rate, and the multiple falls out of the interval sequence and the retention
  target. It is arithmetic, and it is the reason the load lags the decision --
  material introduced today mostly comes due over the following weeks.
  .
  The MULTIPLIER is a different matter and is the reason this item sits at the
  practitioner band. Ten-to-one is a published rule of thumb from one
  application's documentation. It depends on that application's default
  intervals, on the target retention setting, and on the user's actual failure
  rate, none of which are held constant across users -- a person who fails more
  reps generates more repetitions and a higher multiple. No study derives it,
  validates it, or compares intake policies against each other on any outcome.
  It is directly analogous to the per-muscle weekly-set numbers in
  exercise/volume-landmarks-heuristic-015: the taxonomy and the direction are
  sound, the number is coaching experience, and the honest use is as a
  transparent default the individual then adjusts against their own observed
  load.
  .
  Marked contested because a large body of study advice recommends daily intake
  figures with no reference to the review load they commit the person to, which
  is the same error as prescribing training volume without reference to
  recovery.
---

# learning-habits/review-load-follows-intake-018

The most common way a study practice dies is not boredom. It is that the daily
load quietly grew past what the person's day can hold, and every attempt to fix
it was aimed at the wrong end.

The relationship is arithmetic. New material has to come back several times
before its intervals stretch out, so every item taken in today generates a
string of reviews over the following weeks. In steady state that produces a
daily queue that is a multiple of the daily intake, and the multiple is large:
the widely used spaced-repetition application states in its own documentation
that consistently taking in twenty new items a day should be expected to settle
at roughly two hundred reviews a day. Ten to one.

Three things follow, and all three are the opposite of what people do.

First, the intake decision is the load decision. Choosing how much new material
to take in each day is choosing a standing daily time commitment about ten
times that size. It is not a decision about ambition; it is a decision about
the calendar.

Second, the bill arrives late. Material taken in this week mostly comes due over
the following weeks, so the load a person is experiencing today was set by a
decision they made a while ago and have stopped thinking about. A practice that
feels comfortable in its first fortnight can be unmanageable in its second
month without anything having gone wrong.

Third, when the load is too high, the fix is upstream. Reduce intake and let the
queue drain. Raising the daily review cap does not reduce the work, it only
reveals more of it; working faster degrades the reps into the exposure-without-
attempt failure this lane's rep item describes; and abandoning the practice
discards material that was already paid for. The tooling's own instruction is
the correct one -- introduce fewer new items until the burden comes down.

This also names the usual upstream cause of a lapse. Most collapses are not a
motivation failure at all. They are an intake rate that committed the person to
a daily load they never agreed to, followed by a few missed days, followed by a
backlog that now looks like a punishment.

Honest limit. The ten-to-one figure is one application's published rule of
thumb, not a measured constant. It moves with the scheduler's settings, with
the retention target, and with how often the person actually fails a rep --
someone failing more reps generates more repetitions and a bigger multiple.
Nobody has studied intake policies against any outcome. Use it the way a
sensible coach uses a starting set count: a transparent default, stated as a
default, adjusted against what the person's own load actually does.
