# consult phase numbers -- A8 profile assessment, G3 nutrition numbers, measure-first

read when: the confirmed strand goal implies an energy phase (deficit first = cut,
surplus first = lean bulk, together = recomp); the A8 assessment's inputs just landed;
a calculator input is missing. the strand goal itself (target + deadline + basis) is the
kit move loop's `propose`; this file = what the pack's calculator owns.
every number here clears reference/AGENT-CONSULT.md "G6 -- Safety gate" BEFORE it is
spoken.

## A8 profile-informed assessment (once, at the earliest step its inputs exist)

migration = before G2; fresh = once the move loop has the body reading.
- FFMI = lean_mass_kg / height_m^2 (skeletal_muscle_kg if available; else lean =
  weight_kg - fat_mass_kg when fat mass known; composition unknown -> say assessment is
  weight-only). FFMI = backbone of the as-is line; segmental refines, never replaces.
- segmental refinement: segmental InBody on file (metric_log segmental keys, migrated
  records, a report consumed this conversation) -> at most ONE line from the report's
  PRINTED %-of-standard flags, never recomputed (A9): e.g. "부위별로는 하체가
  표준 대비 낮은 편이에요". none on file -> no mention, NO ask; only invitations: the
  optional line in the fresh G3 ask ("체지방률이나 인바디 결과지(사진)가 있으면 더
  정확해요") and the start-point measurement proposal.
- physique assessment in ONE friendly line (e.g. "골격 대비
  근육량이 상당한 편"); segmental = the one allowed second line.
- steer, don't dictate: high FFMI + high BF -> cut bias; low FFMI -> lean-bulk / strength.
- calibrate norms by sex / age: protein g/kg, healthy-BF% reading, recovery / progression
  expectations, calorie-floor safety. sex / age declined -> QUALITATIVE guidance on
  general-adult framing (said so); NUMERIC targets never from invented person constants
  -> numeric path requires measurement first. [SAFETY: A9 no-invention.]
- fresh late-assessment: assessment contradicts the chosen direction -> ONE line naming
  the tension + OFFER a revisit; never force.

## G3 -- the phase's nutrition numbers (the calorie step)

WHERE IT RUNS (owner 2026-10-08 06:34): INSIDE the goal consult, right after the kit wrap
(and the G6-a safety check), BEFORE the program consult. It is program-plan's `calorie`
stage (`JOURNEY`: goal -> safety -> calorie -> place ...); E-STAGE refuses a program
answer while it is open. The goal wrap folds into its first question; its receipt + the
program transition line fold into the program's first question (A2, one message each).
Do not run G3 by hand from this file: speak the tool's moves verbatim, answer with
`program-plan answer --stage calorie:<job|steps|result>`.
(Root cause of the live order, 2026-10-08: G3 had no move of its own -- the wrap folded
straight into the program, and the only coded calorie step was the setup tail's `diet`,
after `done`, with no activity question.)

The rules (owner 2026-10-08 07:09; supersedes 2026-09-27 "watch linked -> NEAT from watch
kcal" and 2026-09-28 "7,000 steps, no watch mention"; rule table:
service/health/calorie_band.py):
- ONE question per message, each asked exactly once, in this order:
  (a) work pattern -- how the working / studying day is spent: 주로 앉아서 / 주로 서서
      움직이며 / 몸 쓰는 일, or the user's own words mapped to the closest;
  (b) recent daily mean steps (phone health app or a rough number): 5천 미만 / 5천~1만 /
      1만 이상 / 잘 모르겠어요, or the user's own number.
  Owner 2026-10-08 13:56: the smartwatch link ask is OUT of this release (it needs the
  Dogany app; next version) -- the band is the estimate from (a) + (b). The code path
  stays behind program-plan's CAL_WATCH_ASK (off): no watch question, no watch line.
  Shift / rest-day pattern is NOT asked: the band table (calorie_band.py) has no shift
  input -- the day's tier and the steps decide it -- so a second question would not move
  the number.
- activity band = the job tier's PAL range on the kit calculator's BMR (Katch-McArdle,
  `kit_life.sh body-state`); steps in another tier -> the range runs between the two
  tiers' middles. lifting 3-6x/week sits INSIDE the band: no exercise add-on.
- maintenance is shown as a RANGE ("시작 추정"); the target comes from its MIDDLE
  (cut -20%, lean bulk +10%, maintain 0, in 50s); the weight trend narrows it at the
  weekly reviews.
- (next version, CAL_WATCH_ASK) watch linked -> config `watch_link=linked`, `watch_import=steps,heart_rate,
  resting_heart_rate`; the automation consent step then recommends "워치 걸음·심박만"
  (steps + heart rate). watch kcal NEVER sets or tops up the food target; workout kcal:
  cardio -> watch kcal is a reference on the record, lifting -> recorded only. the watch
  transport itself is not this step's.
- no step count is ever assumed: unknown -> the job band alone. never speak a default
  step figure (the old 7,000 / 8,000 defaults are gone). the kit gets avg_steps=0 and
  the band's activity as other_neat_kcal, so its base = middle - deficit with nothing
  added on top.
- G6 gate: the tool runs calorie_gate.py on the derived numbers BEFORE the result is
  spoken; refuse -> the refracted number is the proposal with the ONE bound line; a
  user number is gated the same way; unverifiable -> no target is 확정 (the receipt
  says so). sex / birth year / body stats come through the move loop; none on record
  -> measure-first (below), no number.
- writes (tool, through kit verbs): activity_job / steps_weekly_mean on the steps answer
  (write before speak); on 확정 the ledger row first (`constraint-add --class nutrition
  --key deficit_kcal|surplus_kcal`), then the config mirror (deficit_kcal, surplus_kcal,
  avg_steps, other_neat_kcal, maintenance_low/high, maintenance_basis), then
  consult_modules diet:done -- the setup tail's diet step is then not asked again.
- migration: migrated config values (e.g. goal_mode=cut, deficit 650, protein 160) are
  mid-layer evidence only; the step's own range replaces them on 확정.
- then run A8 (above) where its inputs exist.
- measure-first (composition or weight / height unobtainable): the work pattern / steps
  are still asked (activity facts), no number is spoken; the receipt line says numbers
  follow the measurement; pull the start-point measurement proposal FORWARD (OQ-28).
  user insists on numbers now -> decline per A9, one line: one measurement unlocks
  accurate targets. does NOT mark the diet module done.
