---
# Authored 2026-09-02 (cooking-session craft sprint). @test-kitchen, universal.
# The item that grounds the module's hard invariant -- the timeline builder never
# shortens a stated cooking time. The invariant is not a policy preference here;
# it falls out of the definition of the computation, and in this domain the
# minutes are a safety specification rather than a schedule variable.
id: cooking/timeline-backward-pass-016
domain: cooking
lane: "@test-kitchen"
grade: B (deterministic scheduling identities on a defined network)
locale: universal
as_of: 2025
contested: no
sources:
  - "https://biz.libretexts.org/Bookshelves/Management/Project_Management_from_Simple_to_Complex/08:_Project_Time_Management/8.03:_Critical_Path_and_Float"  # LibreTexts Business, Project Management from Simple to Complex, section 8.3 Critical Path and Float. CC BY-NC-SA open textbook, page last modified 2025-05-26, retrieved 2026-09-02. Source for the forward-pass / backward-pass / float definitions quoted below. Cited as a DEFINITION source, not as an empirical result
  - "source:cooking/craft-testing-ceiling-001 -- the lane rule invoked: a deterministic pocket may outrank taste-panel craft evidence, which is why definitional scheduling identities are allowed to speak firmly in a craft lane"
  - "source:cooking/kr-core-temperatures-005 -- 닭고기 74C 1분 이상, the first reason a duration is not a free variable"
  - "source:cooking/kr-norovirus-oyster-010 -- 중심 온도 85C 1분 이상, the second"
  - "source:cooking/session-holding-fence-014 -- 중심온도 75C 1분 이상 for bulk cooking, the third, plus the rule that governs a dish parked by the schedule"
refraction_notes:
  - note: >
      THE ARITHMETIC IS DEFINITIONAL; THE NETWORK IS NOT. Float equals latest
      start minus earliest start. That is a definition and it cannot come out
      wrong. Whether the recipe was correctly turned into a precedence network --
      which step really must follow which, what the durations really are, what was
      left out -- carries no such guarantee at all. A confidently computed
      negative float over a wrong network is a confidently wrong answer, and the
      confidence belongs to the arithmetic rather than to the conclusion.
    grade: B
  - note: >
      WHY THE NO-SHORTENING RULE IS A SAFETY RULE HERE AND NOT A STYLE RULE.
      Korean guidance does not specify temperatures alone; it specifies time AT a
      temperature. 닭고기 74C 1분 이상 (item 005). Oysters marked for cooking, 중심
      온도 85C 1분 이상 (item 010). Bulk-cooked meat, 중심온도 75C 1분 이상 (item
      014). Those minutes are part of the specification. Trimming a cooking time
      to make a schedule fit is therefore not schedule compression, it is
      reducing a stated safety parameter, and it is the single thing a timeline
      builder must never do silently.
    grade: A
  - note: >
      SOURCE TIER, STATED PLAINLY. The scheduling definitions come from an open
      project-management textbook, not from a research finding. That is adequate
      precisely because they are definitions rather than results, and it is the
      same handling item 011 gave a chemistry teaching text. Nothing empirical is
      claimed from this source, and the identities are written out below so a
      reader can check them instead of trusting them.
    grade: C
  - note: >
      NO CLAIM THAT A BACK-CALCULATED TIMELINE PRODUCES BETTER MEALS. No study
      was located comparing home cooks working from a back-calculated schedule
      against home cooks working without one, and none is asserted. The item
      claims only that IF a timeline is computed this way, THEN these properties
      follow. The value proposition of doing it at all is a product judgement, and
      this warehouse is not the place it gets settled.
    grade: D
  - note: >
      NEGATIVE FLOAT IS A FACT, NOT A WARNING LEVEL. When the backward pass drives
      a latest start earlier than the earliest possible start, no valid schedule
      exists at the stated durations and target. That is different in kind from
      "tight". A module that renders infeasibility as a caution and then proceeds
      is misreporting a proof as an opinion. Say the target is gone, say by how
      much, and offer the repairs that keep the durations intact.
    grade: A
claim: >
  A cook-by-a-time plan is a backward pass over a precedence network, and the
  reason a target can be impossible is a property of that computation rather than
  a judgement call. The forward pass runs from the start and gives each step its
  earliest start and earliest finish. The backward pass runs from the required
  completion time and gives each step its latest start and latest finish -- the
  latest it can begin and still meet the completion time. Float, also called
  slack, is the amount a step can be delayed from its earliest start without
  moving the completion time, and it is computed as latest start minus earliest
  start. Two consequences decide the design of a timeline builder. FIRST,
  durations are INPUTS and float is an OUTPUT: slack is derived from the durations
  and the target, never chosen, and never taken out of a duration. SECOND, if the
  backward pass drives a latest start earlier than the earliest possible start,
  float is negative and the schedule is INFEASIBLE -- no valid schedule exists at
  those durations and that target. The only repairs that leave the durations
  intact are to move the target later by at least the shortfall, to remove work
  from the network, or to add a genuine resource so that steps previously forced
  into sequence can actually overlap. Shortening a duration is not a fourth
  repair; it changes the problem, and in cooking it changes a safety input,
  because Korean guidance specifies time at temperature.
reasoning: >
  A module that back-calculates a cooking timeline needs a defensible answer to
  one question: when the target cannot be met, what is the correct behaviour? The
  tempting answer is to shave a few minutes off something, and it is wrong for a
  reason stronger than taste. Under the standard definitions, durations are the
  inputs of the computation and float is what the computation returns; the
  quantity a planner is entitled to spend is the derived one, and taking time out
  of an activity is editing the input while pretending to spend the output. When
  the derived quantity goes negative, that is not a tight schedule, it is a proof
  that none exists at those numbers. This ships in the solid band rather than the
  top one for a stated reason: the identities are definitional and cannot be
  wrong, but they are only as useful as the network someone built, and building
  the network correctly from a recipe has no such guarantee. What lifts the
  no-shortening rule from a scheduling convention to a hard invariant is
  jurisdiction-specific and already in this warehouse: Korea's regulator publishes
  cooking rules as time AT a temperature, so a minute removed from a cooking step
  is a minute removed from a safety specification. The honest limit is stated too
  -- nothing here shows that cooks who plan this way eat better, and no such study
  was located.
---

# cooking/timeline-backward-pass-016

Planning backwards from "dinner at seven" is a specific computation with known
properties, and those properties settle the hardest design question a cooking
timeline has: what to do when the target cannot be met.

Two passes. The forward pass starts at the beginning and asks, for each step, the
earliest it could possibly start and finish given what has to come before it. The
backward pass starts at the required finishing time and works back, asking for
each step the latest it could start and still land the meal on time. Float, or
slack, is the gap: how long a step can be delayed from its earliest start without
moving the finish. It is the latest start minus the earliest start.

Notice what is an input and what is an output. The durations go in. The float
comes out. Slack is a derived quantity -- it is what the schedule has left over
after the durations and the target have had their say. It is not something a
planner picks, and it is emphatically not something that can be found by
shortening a step. Taking three minutes out of a braise to buy three minutes of
slack is editing the input while claiming to spend the output.

Now the case that matters. Run the backward pass and you may find a step whose
latest start is earlier than its earliest possible start. That means negative
float, and negative float is not a tight schedule. It is a proof that no valid
schedule exists at those durations and that target. There is nothing to try
harder at.

Three repairs keep the durations intact:

- move the finish later, by at least the size of the shortfall
- take work out of the plan -- one fewer dish, one simpler dish
- add a real resource, so that two things previously forced into sequence can
  genuinely happen at once (which is a stronger claim than it sounds, and has
  its own item)

Shortening a cooking time is not on that list, and in this domain the reason is
not aesthetic. Korean food-safety guidance does not publish temperatures alone;
it publishes time at a temperature. Chicken at 74 degrees for a minute or more.
Oysters sold for cooking at 85 degrees at the centre for a minute or more. Meat
cooked in bulk at 75 degrees for a minute or more. Those minutes are part of the
specification. A timeline that trims them has not compressed a schedule, it has
lowered a safety parameter, and it has done so in the one place a cook is least
likely to notice.

Two honest limits. The identities above are definitions, taken from an open
project-management textbook and written out here so they can be checked rather
than trusted; nothing empirical is claimed from that source. And they are only as
good as the network someone built out of the recipe. Whether each step really
must follow the one before it, and whether any step was left out, has no
guarantee attached to it at all -- which means a confidently computed
impossibility can still be a confidently wrong one, and the confidence belongs to
the arithmetic rather than to the conclusion.

Nothing here shows that cooks who plan this way produce better food. No such
comparison was located. The claim is conditional: if the timeline is computed
this way, these things follow from it.
