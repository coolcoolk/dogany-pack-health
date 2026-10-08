---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (task-management lane opening).
# Both Mark papers were downloaded and read in full text for this item. The
# 2008 CHI paper was read SPECIFICALLY to check whether it contains the
# "23 minutes 15 seconds" figure attributed to it. It does not; it contains no
# refocus-time figure at all. See GAPS.md, rejected-claim ledger.
id: task-management/interruption-resumption-measured-004
domain: task-management
grade: C (small ethnographic field observation, single industry, 2005 office conditions)
lane: "@behavioral-productivity"
locale: universal
as_of: 2005
contested: no
sources:
  - "https://doi.org/10.1145/1054972.1055017"
  - "Mark, G., Gonzalez, V. M., & Harris, J. (2005). No task left behind? Examining the nature of fragmented work. Proceedings of CHI 2005, 321-330."
  - "https://doi.org/10.1145/1357054.1357072"
  - "Mark, G., Gudith, D., & Klocke, U. (2008). The cost of interrupted work: More speed and stress. Proceedings of CHI 2008, 107-110. (read to verify the absence of the '23 minutes' figure, and for the direction of its own result)"
refraction_notes:
  - note: >
      n = 24 information workers at one company, observed three days each,
      about 25 hours 42 minutes of observation per informant, in 2005. Read
      these as ORDERS OF MAGNITUDE from one office, not as constants. The
      standard deviation on the resumption figure (54 min 48 s) is more than
      twice its mean, so the mean is a poor summary of the distribution.
    grade: D
claim: >
  The measured cost of an interruption is a gap and a queue, not a fixed
  refocus tax. Mark, Gonzalez and Harris (2005) observed 24 information workers
  and recorded: average 11 min 4 s spent in a working sphere before switching or
  being interrupted (SD 18 min 9 s); 57% of working spheres interrupted;
  interrupted segments lasted LONGER (12 min 40 s) than uninterrupted ones
  (8 min 58 s). When interrupted work was resumed on the same day, the mean
  elapsed time before resumption was 25 min 26 s (SD 54 min 48 s), and an
  average of 2.26 other working spheres were entered in between. Central work
  was resumed the same day 82.0% of the time; peripheral work only 43.8%.
  Separately, Mark, Gudith and Klocke (2008) found in a controlled experiment
  that people completed interrupted tasks in LESS time with no difference in
  quality, at the cost of higher reported stress, frustration, time pressure and
  effort.
reasoning: >
  Graded at the observational floor on purpose. It is 24 people in one industry
  over three days, coded by hand without video, in 2005 -- the authors list
  those limitations themselves. It is carried anyway because it is the primary
  measurement that the domain's single most-quoted number is falsely attributed
  to, and because it measures the right thing for a system holding real time
  blocks: how much elapsed time and how many intervening activities separate an
  interruption from a resumption. The 2008 paper is included because its actual
  result runs OPPOSITE to the popular framing -- interrupted tasks were finished
  faster, not slower -- which is a fact that cannot be recovered from any
  retelling of this literature.
---

# task-management/interruption-resumption-measured-004

What was actually measured about interrupted work, by direct observation of
information workers:

- People spent about eleven minutes in a unit of work before switching away
  from it or being interrupted, and 57% of those units were interrupted.
- When interrupted work was picked up again the same day, about twenty-five
  minutes had elapsed, and on average more than two other activities had
  happened in between.
- Not everything comes back. Work central to the person's own role was resumed
  the same day 82% of the time; peripheral work only 44%.
- Counter-intuitively, segments that got interrupted lasted longer overall than
  segments that did not, and a separate controlled experiment by the same lead
  author found people finished interrupted tasks FASTER with no loss of
  quality -- while reporting more stress, frustration, time pressure and
  effort.

So the honest shape of the interruption cost is: elapsed time before you come
back, a queue of other things in between, a real chance the work never comes
back at all, and a subjective cost paid in stress rather than in output. It is
not a fixed number of minutes of "refocusing".

Two cautions on the numbers themselves. The spread is enormous -- the standard
deviation on that twenty-five-minute figure is nearly fifty-five minutes, more
than double the mean -- so it describes a long-tailed distribution badly. And
it is twenty-four people in one office in 2005.

The operational reading for a system holding real time blocks: the signal worth
tracking is not "how long to refocus". It is whether an interrupted item was
ever resumed, and how much unrelated work landed in between. Those are both
directly observable in a log. And note which class of work went unresumed more
than half the time -- the peripheral kind, which in a personal system is
usually the maintenance work nobody is waiting for.

The very widely repeated claim that it takes 23 minutes 15 seconds to refocus
after an interruption is NOT from this study or from the 2008 one; both were
read for this item and neither contains it. See GAPS.md for the trace.
