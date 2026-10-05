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

## G3 -- the phase's nutrition numbers

- migration: migrated config values (e.g. goal_mode=cut, deficit 650, protein 160) enter
  HERE and only here, as carried-over starting values to confirm / adjust.
- fresh: height / weight / composition came through the move loop. at THIS doorstep
  collect only what the calculator still lacks, one topic per message: (a) sex + birth
  year (one profile ask), (b) average daily steps (approximate fine). skip what is on
  record.
- WRITE BEFORE SPEAK (A9): on receipt, before any assessment or number:
    database/kit_life.sh config-set sex=<male|female> birth_year=<YYYY> \
      height_cm=<N> weight_kg=<N> avg_steps=<N> [fat_mass_kg=<weight*pct/100>]
  (skeletal_muscle_kg / lean_mass_kg too if known.)
- activity provisional: steps unknown / skipped -> config-set avg_steps=0
  other_neat_kcal=0 as DECLARED PROVISIONAL, said with every number built on them ("걸음 수
  반영 전 기준이라 실제 여유는 이보다 높을 수 있어요"); replace at the first weekly review.
  never let the tool's silent 8,000-step default speak as canonical. [SAFETY:
  provisional-declaration.]
- then run A8 (above).
- numeric path (all calculator inputs: weight, height, composition; activity real or
  declared-provisional): phase proposal via the owner calculator (Katch-McArdle, kit_life
  `body-state`); run the G6 gate command on the derived numbers BEFORE presenting; a
  proposal that has not cleared the gate is not a proposal. present as proposed starting
  values.
- measure-first (composition or weight / height unobtainable): confirm the phase KIND only
  (numbers 미정), pull the start-point measurement proposal FORWARD as its own
  single-topic message (conditional slot 0-1; OQ-28); finalize numbers when the
  measurement lands (derive -> gate -> ordered writes). does NOT mark the diet module
  done; DOES pre-satisfy its measurement item (idempotency reconciles). user insists on
  numbers now -> decline per A9, one line: one measurement unlocks accurate targets.
- both: 확정 the layer; nutrition numbers are STAGED until the goal part wraps; G6 must
  pass first. deficit_kcal / protein_g = ledger_constraint rows (constraints on the phase,
  not its metric), written right after the move that confirmed them, then the config
  mirror (reference/AGENT-CONSULT.md "Ledger one-writer + SoT").
- choreography: [missing calculator input, one topic] -> (writes) -> [phase numbers
  proposal + ONE 확정 question]. venue is NOT asked here (program-plan `place`).
- measure-first at the wrap: constraint rows + config mirror for 미정 numbers are written
  when the measurement lands, same ordered discipline; everything else proceeds now.
