---
# Authored 2026-09-02 (cooking-session craft sprint). @test-kitchen, universal.
# The 유지형 / 즉시형 discriminator. Written for a live cooking-session module
# that has to decide, per dish, how much schedule slack it may spend. The item
# refuses to ship a slack NUMBER because none was measured, and it hands the
# safety half of the question to item 014 by ID rather than absorbing it.
id: cooking/session-slack-classes-015
domain: cooking
lane: "@test-kitchen"
grade: C (deterministic mechanism, practitioner-judged assignment)
locale: universal
as_of: 2021-2026
contested: no
sources:
  - "https://chem.libretexts.org/Courses/Modesto_Junior_College/Chemistry_143_-_Bunag/Chemistry_143_-_Introductory_Chemistry_(Bunag)/16:_Solutions/16.15:_Boiling_Point_Elevation"  # LibreTexts Chemistry, boiling-point elevation. Used here for one thing only: the magnitude of the elevation a culinary salt or seasoning load produces, which is what licenses treating a seasoned broth as pinned at essentially the boiling point of water. Same page item 011 already ships against
  - "source:cooking/pasta-water-salinity-011 -- the arithmetic already done in this warehouse: about 0.18C at conventional salinity, about 0.61C at aggressive salinity"
  - "source:cooking/browning-water-activity-013 -- evaporative pinning of a wet surface near 100C, the same mechanism seen from the surface rather than from the pot"
  - "source:cooking/session-holding-fence-014 -- the safety fence this item is conditional on. Holding is free only at or above 60C"
  - "source:cooking/craft-testing-ceiling-001 -- the lane rule invoked for the deterministic half"
refraction_notes:
  - note: >
      SAFETY OVERRIDE, AND IT IS THE POINT OF THE ITEM RATHER THAN A CAVEAT ON
      IT. Phase-change pinning is a fact about the POT. It says nothing whatever
      about whether the FOOD is safe to leave. The moment a pinned dish comes off
      the heat it descends through the 5~60C zone, and item 014 records the
      Korean regulator's stated growth optimum for Clostridium perfringens as
      43~47C, inside that descent. So the class label must never be spoken as
      "holdable". It is holdable AT OR ABOVE 60C. A module that renders 유지형 as
      permission to leave a pot sitting has taken a craft observation and used it
      to overrule a published safety rule.
    grade: A
  - note: >
      THE PINNING HALF IS DETERMINISTIC, THE ASSIGNMENT HALF IS JUDGEMENT, AND
      THEY MUST NOT INHERIT EACH OTHER'S CONFIDENCE. That a mixture containing
      free boiling water cannot exceed its boiling point while liquid remains is
      textbook physics, and the warehouse has already done the arithmetic showing
      that culinary salting moves that point by a fraction of a degree. That a
      particular dish belongs in one class rather than the other is a judgement
      about that dish, with no controlled test behind it in this pass.
    grade: C
  - note: >
      NO SLACK NUMBER IS SHIPPED, DELIBERATELY. It would be easy and wrong to
      publish something like "유지형 tolerates 30 minutes". Nothing measured that.
      What the mechanism licenses is a DIRECTION and a BOUND: a pinned dish's
      tolerance is limited by texture and by the hold-temperature rule rather
      than by the temperature running away, and an unpinned dish's tolerance is
      limited by the rate at which its surface keeps cooking, which is fast and
      unquantified here. A module that needs a number must get it from the user
      or from measurement, not from this item.
    grade: B
  - note: >
      THE SECOND CRITERION IS ONE-WAY AND THAT IS WHY IT COUNTS. Loss of crispness
      as interior moisture migrates outward through a fried crust, and loss of
      turgor in a dressed salad as salt and acid draw water out, do not reverse
      when the dish is served. A dish can therefore be perfectly pinned and still
      be 즉시형, because the clock that is running is a texture clock and not a
      temperature clock. 튀김 is the clean case: the oil is far above any pinning
      temperature AND the crust decays, so it fails both tests at once.
    grade: C
  - note: >
      RICE IS PINNED ONLY DURING THE ABSORPTION PHASE. While free water remains,
      cooking rice is pinned like any other boiling preparation. Once the water is
      absorbed, the pinning is gone and whatever holds the rice afterwards is the
      appliance, whose actual hold temperature this warehouse does not know. See
      item 020, which refuses to assume it.
    grade: B
claim: >
  Whether a dish tolerates schedule slack is decided by two physical questions,
  not by the dish's name. FIRST, is the food's temperature pinned by a boiling
  liquid? While free water is boiling at ordinary pressure, the mixture cannot
  exceed its boiling point while liquid remains, and at culinary seasoning levels
  that point is within a fraction of a degree of the boiling point of pure water
  (about 0.18C of elevation at conventional salinity, about 0.61C at aggressive
  salinity, per the arithmetic already shipped in this warehouse). So extra
  minutes in a simmering pot add cooking but cannot raise the temperature.
  국, 찌개, 조림 and the absorption phase of 밥 are pinned; 볶음 and 튀김 are not,
  because their surfaces sit at pan or oil temperature well above 100C and every
  additional minute moves the food monotonically further along. SECOND, does the
  finished state decay irreversibly while it waits? A fried crust softens as
  interior moisture migrates outward; a dressed salad loses turgor as salt and
  acid draw water out. Neither reverses. A dish is the tolerant class (유지형)
  when it is pinned AND slow-decaying, and the urgent class (즉시형) when it is
  unpinned OR fast-decaying. The classification is about the pot and the texture
  only: holding remains free ONLY at or above the 60C floor in item 014, below
  which the tolerance is a two-hour clock rather than slack.
reasoning: >
  A live cooking-session module has to decide, dish by dish, whether it may spend
  schedule slack, and the folk version of that decision is a list of dish names.
  A list of names does not generalise and cannot be checked. The mechanism can:
  the reason a stew forgives a late cook is that a boiling pot is temperature-
  regulated by a phase change, and the reason a stir-fry does not is that nothing
  regulates a hot dry pan. That half of the item is deterministic, rests on
  textbook physics plus arithmetic this warehouse has already published, and is
  the same deterministic pocket item 001 carves out for this lane. The item still
  ships in the middle band rather than higher, because the classification of any
  particular dish is judgement and because no controlled test of dish tolerance
  was located in this pass. The most important line in it is not the physics; it
  is the fence. Pinning is a property of the pot, safety is a property of the
  food, and the two are being answered by different lanes. Craft may say a stew
  tolerates delay. Only the food-safety lane may say a stew is safe to leave, and
  its answer is a temperature.
---

# cooking/session-slack-classes-015

Every cooking session that runs on a clock needs to know which dishes will
forgive it. The useful answer is not a list of dish names. It is two questions
about the physics of the pot.

The first question: is the food's temperature pinned by boiling liquid? A
mixture with free water boiling in it cannot get hotter than its boiling point
while liquid remains, and the seasoning a cook adds does not move that point in
any way a cook could act on -- this warehouse has already done the arithmetic and
got about a fifth of a degree at conventional salting. So a simmering pot is
temperature-regulated. Five more minutes cooks the food more; it does not make
the pot hotter.

A hot dry pan or a pot of frying oil has no such regulator. Those surfaces sit
far above the boiling point of water and keep climbing, and every extra minute
carries the food monotonically further along toward the state you did not want.

The second question: does the finished dish decay in a way that does not reverse
while it waits? A fried crust softens as moisture from inside migrates out
through it. A dressed salad slumps as salt and acid pull water from the cells.
Neither of those un-happens when the plate reaches the table.

Put the two together. A dish is the tolerant kind when it is pinned and slow to
decay -- 국, 찌개, 조림, and rice while it is still absorbing water. A dish is the
urgent kind when either test fails. 볶음 fails the first. A salad fails the
second. 튀김 fails both at once, which is why it is the least forgiving thing in
a home kitchen and why it belongs at the very end of a timeline.

Now the part that matters more than any of the above.

Pinning is a fact about the pot. It is not a fact about the food. The instant a
tolerant dish comes off the heat it begins descending through the range where
things grow, and Korea's regulator puts the growth optimum for the organism that
lives in boiled food at 43 to 47 degrees -- inside that descent. So the tolerant
class does not mean holdable. It means holdable at or above 60 degrees. Below
that line there is no slack, there is a two-hour clock, and the rule that governs
is the food-safety one, not this one.

Two things are deliberately absent. There is no number here for how long a
tolerant dish tolerates, because nothing measured it; what the mechanism gives is
the shape of the limit, not its size. And nothing here has been through a
controlled test -- the physics is textbook, the texture argument is
uncontroversial and unmeasured, and sorting any particular dish into a class is a
judgement that should be spoken as one.
