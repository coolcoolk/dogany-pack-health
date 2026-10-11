# form-demo review loop -- independent QA gate

Builder NEVER passes own work. Every demo goes through this gate before catalog
or send. Numbers alone LIE (a pose can pass every distance/angle check and still
have a hand buried in the chest or a bar skewering the neck). Reviewer MUST OPEN
the actual QA still images and LOOK.

## who reviews
- reviewer = separate from the builder subagent (bias: builder wants to pass).
  use a FRESH review subagent (vision) OR the main coordinator. builder self-cert
  does NOT count as review.
- reviewer opens all 3 QA stills (top / mid / bottom) with the Read tool (vision)
  and judges each frame.

## checklist (open all 3 stills, check every item)
1. interpenetration / clipping (the #1 miss): NO mesh through mesh.
   - hands / forearms into TORSO (crossed-arms, hands-on-chest sink into pecs).
   - prop (bar / plate / dumbbell) through body, head, neck, or the other arm
     (bar must rest ON the part, e.g. traps behind neck -- not skewer through).
   - limb through limb; heel / toe through floor.
2. contact / grounding: feet planted correctly for the move (flat, or ball-planted
   for calf raise); no float, no sink.
3. form correct for THIS exercise: joint angles right, spine neutral (no rounding /
   butt-wink), gaze neutral (no chin tuck), knees track over toes (no valgus),
   balance / COM over the base (not tipping back).
4. prop placement: on the correct body part, seated not floating, not skewering.
5. render artifacts: no holes, inverted normals, candy-wrapper twist, detached
   chunks, weird bulges.
6. reads as a real human doing the real lift (sanity: "does a person look like
   this doing this?").

## zoom the extremities (MANDATORY -- full-body still is NOT enough)
- a full-body 720p still is too small to judge fingers / toes. hands and feet
  MUST be inspected as ZOOMED CROPS or the damage is invisible (this is how
  crushed hands + mangled toes slipped through repeatedly).
- for EACH keyframe: crop the hand region(s) and the foot region, enlarge ~3x,
  and LOOK. check for:
  - hand crushed / collapsed into a blob, mesh shards/spikes, wrist candy-wrapper
    (grouped-finger rig crushes when forced to wrap a bar -> watch this on any
    grip pose).
  - toes fused/mangled, foot edge clipping THROUGH the floor (dark z-fight sliver
    at the sole), ankle deformation creases.
- a demo does not PASS until the zoomed hand + foot crops are clean, not just the
  full-body silhouette.

## verdict
- reviewer returns PASS or FAIL.
- FAIL -> list each defect precisely: which still (top/mid/bottom), what is wrong,
  where on the body. vague "looks off" is not actionable -- name it.

## loop
- FAIL -> defect list goes back to the BUILDER -> builder fixes the named defects
  -> re-render -> reviewer re-checks (fresh look at new stills).
- cap: max 3 fix rounds. still failing after 3 -> STOP. report to owner exactly
  what is limiting it (rig can't do X, mesh can't do Y). do NOT ship a broken
  demo, and do NOT loop forever.
- only PASS -> finalize: update registry, then coordinator gives it a final look
  and presents / sends to owner.

## note
- this gate is why the skill exists as a pipeline, not a one-shot render. a demo
  is not "done" when it renders -- it is done when it PASSES review.
