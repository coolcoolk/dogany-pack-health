---
# Authored 2026-10-06 (cooking craft/holding re-audit sprint). @food-safety, KR.
# The engine-readable rule set for the cooking-session flow, built the way
# exercise/caution-severity-ladder-056 was: a SYNTHESIS over already-graded
# items, written as structured frontmatter so a module can read fields rather
# than parse prose. It adds no new evidence. Every row names the item that
# carries the evidence and that item's grade; the D on this item is for the
# assembly (state names, which rule wins on conflict, what the flow says),
# not for any number, every one of which is copied from a source item.
# Lane is @food-safety, not @test-kitchen, because where the timeline and the
# safety rules collide the safety row wins, and this item is where that
# precedence is written down.
id: cooking/session-holding-timeline-rules-072
domain: cooking
lane: "@food-safety"
grade: D (synthesis rule over 005, 007, 014, 015, 016, 017, 070, 071; every number is copied from a cited item, the state model and precedence are product judgement)
locale: KR
as_of: 2026-10-06
contested: no
sources:
  - "cooking/session-holding-fence-014"  # 60C / 5C / 2시간 from end of cooking / 75C reheat; household-facing ministry advice (A)
  - "cooking/kr-food-code-cooked-food-holding-070"  # legal text: 60C hot, 10C cold for businesses; 2h from 조리 후 when untempered (A)
  - "cooking/batch-cooling-depth-071"  # split to ~5 cm, active cooling, no stockpot in the fridge (C)
  - "cooking/kr-core-temperatures-005"  # household core temperatures (A)
  - "cooking/kr-cold-chain-band-006"  # Korean legal cold band 0~10C; why a household is told 5C (A)
  - "cooking/reheating-not-a-reset-007"  # reheating is not a reset (B)
  - "cooking/session-slack-classes-015"  # pinned / decaying classification (C)
  - "cooking/timeline-backward-pass-016"  # durations in, float out; negative float = infeasible (B)
  - "cooking/parallelism-resource-claim-017"  # resource-blind timeline is a lower bound; barriers (C)
holding_states:
  - state: cooking
    meaning: on heat, inside a stated cooking step
    clock: none
    flow_says: nothing about safety; the step's stated duration is never shortened
    basis: cooking/timeline-backward-pass-016
    basis_grade: A
  - state: hot-held
    meaning: kept on heat or in a warmer at 60C or above
    clock: none from the regulator (no hold limit stated above 60C); texture still decays per item 015
    flow_says: this is the ONLY state in which a finished dish absorbs schedule slack
    basis: cooking/session-holding-fence-014
    basis_grade: A
  - state: ambient
    meaning: cooking finished, heat off, not refrigerated -- includes a pot left on a switched-off stove
    clock: 2 h counted from end of cooking (가급적 2시간 이내 섭취); the clock does not wait for the pot to drop below 60C
    flow_says: serve and eat inside the window, or start cooling (state cooling) inside it
    basis: cooking/session-holding-fence-014, cooking/kr-food-code-cooked-food-holding-070
    basis_grade: A
  - state: cooling
    meaning: being brought down for storage
    clock: no Korean cooling rate exists; do not quote one as Korean
    flow_says: split into containers about 5 cm deep or less, cold-water or iced sink and stir, then coldest fridge shelf or freezer, uncrowded; never a full pot straight into the fridge
    basis: cooking/batch-cooling-depth-071, cooking/session-holding-fence-014
    basis_grade: C
  - state: cold-held
    meaning: refrigerated at 5C or below (household advice); 10C is the business legal line and is NOT spoken to a household
    clock: storage-duration questions go to the storage items, not to this ladder
    flow_says: set the fridge colder rather than trusting the legal band
    basis: cooking/session-holding-fence-014, cooking/kr-cold-chain-band-006
    basis_grade: A
  - state: reheated
    meaning: stored food brought back for eating
    clock: none new
    flow_says: reheat to 75C or above; say plainly this kills vegetative bacteria and does not undo spores or toxin formed while it sat
    basis: cooking/session-holding-fence-014, cooking/reheating-not-a-reset-007
    basis_grade: A
timeline_constraints:
  - rule: park-only-hot
    text: a dish the backward pass finishes early may wait only in hot-held; if it cannot be kept at 60C or above, its finish-to-serve gap counts against the 2 h ambient window, and the gap is capped there
    basis_grade: A
  - rule: ambient-gap-cap
    text: for any dish that will sit ambient, (serve time - its cooking end) must be at most 2 h; the flow should keep this gap as small as the network allows, since the 2 h is a ceiling, not a target
    basis_grade: A
  - rule: no-duration-trim
    text: never shorten a stated cooking step to make a target fit; negative float means the target is infeasible, so move the target, drop work or add a real resource
    basis: cooking/timeline-backward-pass-016
    basis_grade: A
  - rule: cooling-is-a-step
    text: for a batch cooked to store, cooling (split, ice bath, stir) is a timed step on the network with its own attention claim, not an afterthought after serving
    basis: cooking/batch-cooling-depth-071, cooking/parallelism-resource-claim-017
    basis_grade: C
  - rule: bulk-temperature-scope
    text: when the session cooks in bulk to hold or store, use the bulk targets (meat 75C core, fish/shellfish 85C, 1 min or more) and not the household table; never average the two
    basis: cooking/session-holding-fence-014, cooking/kr-core-temperatures-005
    basis_grade: B
precedence: safety rows (states hot-held / ambient / reheated, constraints park-only-hot, ambient-gap-cap, no-duration-trim) override any craft slack class from item 015
refraction_notes:
  - note: >
      THE STATE NAMES ARE OURS; THE NUMBERS ARE THE REGULATOR'S. 60C, 5C, 10C,
      2 hours from end of cooking, 75C, 85C are copied from items 014 and 070.
      Splitting a session into six named states is a product decision, and a
      module may rename or merge them so long as no number moves and the
      precedence line holds.
    grade: D
  - note: >
      "FREE ABOVE 60C" MEANS FREE OF THE SAFETY CLOCK, NOT FREE OF DECAY. The
      regulator states no hold limit above 60C. A fried or dressed dish still
      degrades while it waits (item 015), so hot-held is where slack is
      ALLOWED, not where it is costless.
    grade: C
  - note: >
      THE 2 HOURS IS A CEILING, NOT A BUDGET. The ministry's wording is 가급적 2
      시간 이내, as soon as possible within two hours. A timeline that parks every
      ambient dish for 1 h 59 min is compliant on paper and is not what the advice
      asks. Minimise the ambient gap; never plan to it.
    grade: B
  - note: >
      THERMOMETER UNKNOWN, SAY THE SAFE THING. A household often cannot tell 60C
      from 50C. When the flow does not know the dish is being kept at 60C or
      above (a warmer, a pot visibly at a simmer), it treats the dish as ambient
      and runs the 2-hour clock from end of cooking. There is still no axis for
      thermometer availability on the ledger (GAPS, v15 and v31); this note is
      the default until one exists.
    grade: D
claim: >
  A cooking-session flow can run its food-safety logic as a small state model
  over each finished dish, with every number taken from Korean regulator text
  already in this warehouse. A dish is cooking, hot-held (60C or above, the only
  state that absorbs schedule slack), ambient (heat off and not chilled, on a
  2-hour clock counted from the end of cooking), cooling (split to shallow
  containers about 5 cm deep, actively cooled; Korea sets no cooling rate),
  cold-held (5C or below for a household), or reheated (75C or above, which is
  not a reset). The timeline builder obeys three hard constraints on top of its
  backward pass: a dish finished early may only be parked hot; any ambient gap
  between a dish's cooking end and the serve time is capped at 2 hours and kept
  as small as the network allows; and no stated cooking time is ever shortened.
  For batches cooked to store, cooling is a scheduled step, and bulk cooking
  uses the bulk core temperatures (75C meat, 85C fish and shellfish, 1 minute or
  more) rather than the household table.
reasoning: >
  The cooking-session items each answer one question -- how hot, how long to
  hold, how to cool, how to schedule -- and a module that has to combine them
  at run time needs the combination written down once, with the conflict rule
  stated. That is all this item is. It ships at D because the assembly is
  judgement: the state names, the decision to treat an unknown temperature as
  ambient, and the precedence of safety rows over craft slack are product
  choices, even though each number underneath is A-graded regulator text or a
  B/C-graded item. Two points are worth the structure. The 2-hour clock is
  anchored at the end of cooking, which the 2026-10-06 re-audit of item 014 and
  the new Food Code text both support, and which a household can actually
  observe. And the timeline constraints turn "a stew tolerates waiting" into a
  checkable rule: it tolerates waiting only while it is kept hot, and otherwise
  it costs minutes from a fixed window.
---

# cooking/session-holding-timeline-rules-072

This item adds no new evidence. It writes down, in a form a program can read,
how the cooking-session flow should combine the safety items it already has.

Every finished dish is in one of six states:

- **cooking** -- on the heat inside a stated step. Never shortened.
- **hot-held** -- kept at 60 degrees or more. The only place a dish can wait
  for the rest of the meal without a safety clock. It still loses texture.
- **ambient** -- heat off, not in the fridge. Two hours, counted from when the
  cooking finished, to eat it or start cooling it. A pot left on a switched-off
  stove is here.
- **cooling** -- split into shallow containers (about 5 cm of food), cold water
  or ice and stir, then the coldest shelf. Never a full pot straight into the
  fridge. Korea sets no cooling time; foreign codes do.
- **cold-held** -- 5 degrees or below at home. (The 10 degree figure in the
  law is for businesses.)
- **reheated** -- back up to 75 or more. Kills what grew; does not undo spores
  or toxin.

And the timeline builder gets three rules on top of its backward pass:

1. A dish that finishes early may wait only if it is kept hot.
2. Otherwise the time from its cooking end to serving is capped at two hours --
   and should be as short as the plan allows, because two hours is a ceiling,
   not a target.
3. No cooking time is ever shortened to make a target fit.

When the flow cannot tell whether a dish is really being kept at 60 or more --
most kitchens have no thermometer -- it assumes it is not, and runs the clock.

The numbers all come from Korea's food-safety ministry and the Food Code, via the
items listed in the sources. The state names and which rule wins when craft and
safety disagree are product judgement, which is why this item is graded D.
