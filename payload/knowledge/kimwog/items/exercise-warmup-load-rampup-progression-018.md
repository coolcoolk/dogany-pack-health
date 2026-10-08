---
# Triggered by a live overhead-press session (2026-08-13): a single ramp-up
# jump of 20kg -> 42.5kg (~53% of the working weight) felt too large to the
# owner. Researched how established loading schemes size warm-up/ramp-up
# jumps, to ground a "max single jump = X% of working weight, else insert an
# intermediate step" heuristic. Rubric: exercise.rubric.md @gym-craft, same
# lane/grade family as exercise/volume-landmarks-heuristic-015.
id: exercise/warmup-load-rampup-progression-018
domain: exercise
grade: D (practitioner-heuristic)
lane: "@gym-craft"
locale: universal
as_of: 2009-2026
contested: yes
sources:
  - "https://support.stronglifts.com/article/87-warmup"  # StrongLifts warmup calculator: hard rule, no single warmup jump > 45 lb; worked example 45/45/95/135/185 -> 225 lb
  - "https://www.baystrength.com/calculating-warmup-sets/"  # Bay Strength coaching blog: 45/65/85% of work weight for loaded warmup sets (advanced novice+)
  - "https://www.typeatraining.com/blog/5-3-1-program-guide-jim-wendlers-proven-strength-system/"  # secondary summary of Jim Wendler's 5/3/1: warmups 40/50/60% of training max, work-set ramp 65/75/85% (week 1), all ~10pp steps
  - "exercise/volume-landmarks-heuristic-015"  # within-warehouse cross-ref: same D/practitioner-heuristic/@gym-craft family, same caveat pattern (usable scaffold, contested specific numbers)
  - "framework:GRADE -- no RCT evidence exists on optimal warm-up jump size; this is triangulated from three independently-published coaching/programming schemes (a novice barbell program, a coaching blog, and an intermediate/advanced powerlifting-style program) that converge on a similar band, not from controlled trials"
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
claim: >
  There is no controlled-trial evidence on optimal warm-up/ramp-up jump size;
  it is pure coaching practice. Three independently-published loading schemes
  converge on capping any single ramp-up jump at roughly 15-25% of the
  eventual working-set weight, with the jump into the FINAL working set kept
  at the tighter end of that band (or tighter still, ~10%, for advanced
  lifters / near-maximal loads / technically demanding or injury-sensitive
  lifts). A default working threshold of 20% of working-set weight is a
  reasonable single number: if a planned jump between successive ramp-up
  sets (or into the first working set) would exceed it, insert one or more
  intermediate steps that split the remaining gap into roughly equal jumps
  at or under the cap, rounded to plate-loadable values.
reasoning: >
  StrongLifts' warmup calculator enforces a hard rule that no single warmup
  jump exceeds 45 lb, and its worked example for a 225 lb squat (45/45/95/135/
  185 -> 225 lb) never exceeds a ~20% jump of the 225 lb target. Bay Strength's
  coaching guidance for advanced novices makes the same shape explicit as
  percentages: 45/65/85% of work weight for three loaded warmup sets, i.e. flat
  20-percentage-point jumps between warmup sets and a smaller 15-point jump
  into the working set. Jim Wendler's 5/3/1 (intermediate/advanced,
  near-maximal programming) uses tighter ~10-percentage-point spacing
  throughout -- both in its warmups (40/50/60% of training max) and in its own
  work-set ramp (65/75/85% in week 1) -- consistent with the pattern that jumps
  should tighten as the load gets heavier / closer to true limit or the lift
  is more technical. All three sources are practitioner/coaching programming,
  not experimental data -- there is no RCT comparing injury rate, bar-speed
  readiness, or performance across different ramp-jump sizes. The 15-25% band
  and the recommendation to tighten near the top set is therefore a reasoned
  synthesis across converging practice, not a measured finding; treat the
  specific number as adjustable, not as an established safety limit.
---

# exercise/warmup-load-rampup-progression-018

How big a jump between one ramp-up set and the next should be, and when to add
an extra step, is not something anyone has run a controlled trial on -- it is
coaching practice, refined by feel and iteration. But when several independent,
long-used loading schemes are lined up, they land in roughly the same place.

StrongLifts' warmup calculator hard-caps every jump at 45 lb regardless of the
target weight, and its published example for a 225 lb squat (45, 45, 95, 135,
185, then 225 lb) never actually needs a jump bigger than about 20% of the
225 lb target. Bay Strength's coaching write-up makes that percentage explicit:
three loaded warmup sets at 45%, 65%, and 85% of the work weight -- flat
20-point jumps, tightening to a 15-point jump for the last step into the
working set. Jim Wendler's 5/3/1, built for heavier, more advanced,
closer-to-limit lifting, runs noticeably tighter: warmups at 40/50/60% of
training max, and even its own top-set ramp (65/75/85% in week one) advances
in ~10-point steps.

Put together, that is a workable heuristic: cap any single ramp-up jump at
about 20% of the eventual working-set weight as a default, and tighten toward
10-15% for the jump into the top set itself, especially on heavier, more
technical, or injury-sensitive lifts (overhead pressing -- shoulder-loaded,
technical, easy to feel a jump as "too much" -- is exactly that case). When a
planned jump would exceed the cap, do not take it in one step: split the
remaining distance into roughly equal jumps that each stay at or under the
cap, and round each step to a plate-loadable weight.

Worked check against the case that prompted this: overhead press, ramp-up set
at 20 kg (empty bar), working set at 42.5 kg. The raw jump is 22.5 kg, about
53% of the working weight -- more than double even the loosest end of the
15-25% band, regardless of which exact number in that band is used (even a
25% cap still forces at least two intermediate steps here, since a single
11.25 kg jump exceeds it). Applying the 20% default (max single jump =
8.5 kg) means the 22.5 kg gap needs at least 3 roughly-equal jumps, i.e. 2
intermediate steps:

  20 kg (bar) -> 27.5 kg -> 35 kg -> 42.5 kg (working set)

Each jump is 7.5 kg, about 17.6% of the 42.5 kg working weight -- under the
cap -- and every step is plate-loadable with standard fractional plates
(27.5 kg = bar + 2.5+1.25 kg per side; 35 kg = bar + 5+2.5 kg per side; 42.5 kg
= bar + 10+1.25 kg per side, matching the owner's existing 42.5 kg notation).

Honest limit: the 15-25% band and the "tighten near the top" direction are
triangulated from three published coaching/programming schemes that happen to
converge, not from any experimental comparison -- there is no evidence this
specific number reduces injury or improves performance versus, say, 15% or
30%. Treat 20% as a sensible, adjustable default, not a validated safety
threshold.
