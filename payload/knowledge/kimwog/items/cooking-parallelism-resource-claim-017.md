---
# Authored 2026-09-02 (cooking-session craft sprint). @test-kitchen, universal.
# The companion to item 016. A timeline builder that treats a recipe's step
# ordering as the whole constraint will produce a schedule that is arithmetically
# correct and physically impossible. This item states what else is a constraint,
# proves the direction of the resulting error, and REFUSES to ship durations for
# the barriers because none were measured.
id: cooking/parallelism-resource-claim-017
domain: cooking
lane: "@test-kitchen"
grade: C (deterministic bound, practitioner-enumerated inputs)
locale: universal
as_of: 2025-2026
contested: no
sources:
  - "https://biz.libretexts.org/Bookshelves/Management/Project_Management_from_Simple_to_Complex/08:_Project_Time_Management/8.03:_Critical_Path_and_Float"  # LibreTexts Business, Project Management from Simple to Complex, 8.3 Critical Path and Float. CC BY-NC-SA, page last modified 2025-05-26, retrieved 2026-09-02. Source for the precedence-network vocabulary this item extends
  - "source:cooking/timeline-backward-pass-016 -- the computation this item supplies the missing constraint to"
  - "source:cooking/browning-water-activity-013 -- the measured reason a wet surface stalls near 100C, which is what makes surface drying a real barrier rather than a fussy habit"
  - "source:cooking/session-holding-fence-014 -- what governs a dish that finishes early because a barrier upstream cleared sooner than planned"
refraction_notes:
  - note: >
      THE BOUND IS A ONE-LINE PROOF AND IT IS WRITTEN OUT. Any schedule that
      satisfies both the ordering constraints and the equipment constraints also
      satisfies the ordering constraints on their own. So the set of
      resource-feasible schedules is a subset of the set of order-feasible ones,
      and the shortest achievable finish once equipment is accounted for cannot be
      earlier than the shortest achievable finish when it is ignored. A timeline
      built from recipe ordering alone is therefore a LOWER BOUND on elapsed time,
      never an estimate. The direction of the error is certain even though its
      size is not.
    grade: A
  - note: >
      THE LIST OF BARRIERS IS PRACTITIONER-ENUMERATED AND CARRIES NO STUDY. No
      controlled work was located enumerating or timing the non-overlappable steps
      of home cooking. The list below is a category argument -- these are the
      steps that gate everything downstream and cannot be worked through -- not a
      measured inventory, and a session that meets a barrier not on it should
      treat the list as incomplete rather than treat the step as absent.
    grade: D
  - note: >
      NO BARRIER DURATIONS ARE SHIPPED, DELIBERATELY. How long a given oven takes
      to preheat, or a given pot of water to boil on a given hob, is an appliance
      and quantity question, and nothing here measured any of it. Publishing a
      generic figure would be exactly the precise-sounding number with nothing
      behind it that this lane refuses elsewhere. A module that needs these
      numbers should measure them once per kitchen and store them, which is cheap
      and gives a real answer instead of a plausible one.
    grade: B
  - note: >
      ATTENTION IS THE RESOURCE WITH CAPACITY ONE, AND IT IS THE ONE RECIPES NEVER
      DECLARE. A step that requires continuous stirring, continuous turning, or
      standing at the pan occupies the cook and not merely the burner, so nothing
      that also needs the cook can overlap it. Equipment conflicts announce
      themselves physically; attention conflicts do not, and they are where a
      plausible-looking parallel plan usually fails.
    grade: C
  - note: >
      A BARRIER CLEARING EARLY IS NOT FREE EITHER. Overlapping work around a
      barrier can leave a dish finished well before service, which moves the
      question out of this item and into item 014: a finished dish waiting is
      being held, and holding is free only at or above 60C. Parallelising toward
      an earlier finish is not automatically a gain.
    grade: A
claim: >
  Two cooking steps are parallel only if, at every minute they overlap, the
  equipment and the attention they require are simultaneously available.
  Precedence (this must follow that) and resource capacity (there is one large
  burner, one oven, one cook) are different constraints, and only the first is
  visible in a recipe. The direction of the resulting error is provable: any
  schedule that is feasible under both precedence and resources is also feasible
  under precedence alone, so the shortest resource-feasible finish is greater than
  or equal to the shortest precedence-only finish. A timeline built from recipe
  ordering alone is a LOWER BOUND on elapsed time, never an estimate. Separately,
  some steps are hard barriers: they gate everything downstream, they cannot be
  overlapped with the step they gate, and they are routinely absent from stated
  times. The recurring ones are bringing liquid to a boil, bringing oil or an oven
  to temperature, thawing, soaking and steeping, rice absorbing and then resting,
  drying a surface before it will brown, and any instruction whose duration is
  written as "until" rather than as a number. A barrier's defining property for a
  timeline is that work can be moved AROUND it but not THROUGH it.
reasoning: >
  A timeline builder that reads a recipe's step order as the complete constraint
  set will emit schedules that are arithmetically correct and physically
  impossible, because the recipe never declares that there is one large burner or
  one pair of hands. The correction has an unusual property worth relying on: even
  though the size of the error cannot be computed without knowing the kitchen, its
  DIRECTION is certain, because adding constraints to a minimisation can only
  raise the minimum. That is why the ordering-only timeline should be labelled a
  lower bound rather than an estimate -- a claim that is safe to make with no
  measurement at all. Beyond that bound the item is deliberately thin. The
  enumeration of barriers is a category argument with no study behind it, and no
  barrier duration is published, because preheat and come-to-boil times are
  properties of a specific appliance and quantity and nothing here measured them.
  Publishing a generic figure would manufacture exactly the kind of
  precise-sounding number this lane refuses elsewhere. The one constraint singled
  out for emphasis is attention, because equipment conflicts are self-announcing
  and attention conflicts are not, and a plan that overlaps two steps each
  requiring the cook's hands looks fine on paper right up to the minute it runs.
---

# cooking/parallelism-resource-claim-017

A recipe tells you that the sauce must be made before it goes on the pasta. It
does not tell you that you own one large burner.

Those are two different kinds of constraint. Ordering is what a recipe declares.
Capacity -- one oven, one big pan, one cook -- is what the kitchen imposes and
what nothing in the text mentions. A timeline built from the first alone will be
arithmetically correct and physically impossible.

The direction of that error can be settled without measuring anything. Any
schedule that respects both the ordering and the equipment also respects the
ordering by itself. So the schedules that are actually achievable are a subset of
the schedules the ordering allows, and the earliest achievable finish once
equipment is counted cannot be earlier than the earliest finish when it is
ignored. A plan built from recipe ordering alone is a lower bound on how long
the cooking takes. Never an estimate. The size of the gap depends on the kitchen;
the sign of it does not.

Then there are the steps that cannot be overlapped with what they gate at all.
Work can be moved around them, never through them:

- bringing liquid to a boil
- bringing oil, a pan, or an oven up to temperature
- thawing
- soaking and steeping
- rice absorbing its water, and then resting
- drying a surface enough that it will brown, which is a real barrier rather
  than a fussy habit, because a wet surface is held near the boiling point by
  evaporation and browning does not get going until the water is gone
- anything whose length the recipe writes as "until" instead of as a number

None of those has a duration in this item, and that absence is deliberate. How
long a particular oven takes to preheat, or a particular pot to boil on a
particular hob, depends on the appliance and the quantity, and nothing here
measured any of it. A generic figure would be a precise-sounding number with
nothing behind it. These are cheap to measure once per kitchen and worth storing,
which gives a real answer rather than a plausible one.

The constraint most likely to break a plan is the one with capacity one: the
cook. A step that needs continuous stirring or continuous turning occupies the
person, not just the burner, so nothing else that needs the person can share the
minute. Equipment conflicts announce themselves -- two pans and one hob is
obvious the moment it happens. Attention conflicts do not announce themselves
until the plan is already running.

One last thing that is easy to get backwards. Successfully overlapping work
around a barrier can land a dish well before service, and a dish finished early
is a dish being held, which is a food-safety question with a published number
attached rather than a scheduling win. Parallelising toward an earlier finish is
not automatically a gain.
