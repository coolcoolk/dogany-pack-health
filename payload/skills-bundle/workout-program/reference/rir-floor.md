# 복합 프리웨이트 RIR 하한 정책 (G19, owner 2026-08-23)

Read when: program-init prints `W-G19-UNSET`, a compound freeweight slot is added or
changed, or the floor / roster is questioned. SINGLE HOME of the roster + floor value
(program-init schema, test-rir-floor.py and slot notes point here; no copy in code).

## rule

- floor RIR 2-3: target lifts end working sets at RIR 2-3, never pushed to <=1. owner:
  heavy progression stays possible inside 2-3 -- goal is keep control while adding
  weight, not cap volume. actual RIR staying >= 3 = increase signal.
- mechanism: near failure on heavy compound freeweights the STABILISERS fail first,
  prime-mover control collapses, load leaks into joints before muscle failure. stack
  machines / cables fix the path -> no such route, not targets.

## target test (all three)

1. `exercise_pattern` multi-joint (squat / hinge / horizontal_push / vertical_push /
   horizontal_pull / vertical_pull), not isolation / core.
2. freeweight (barbell / dumbbell / bodyweight): lifter stabilises the path. stack
   machine / cable excluded.
3. trunk not supported by the machine (chest pad / backrest removes the stabiliser
   demand -> mechanism absent).

## roster (2026-08-23 judgement over every program.yaml slot) -- 10

- back_squat, overhead_press, incline_barbell_press -- earlier 3, floor 2 -> 2-3.
- deadlift, barbell_row, pendlay_row, rdl -- new, barbell, fatigue high. rdl = one of
  the two lifts the user named after trying it.
- bulgarian_split_squat -- new, dumbbell squat; the other user-named lift; also carries
  knee rehab.
- incline_dumbbell_press -- new; dumbbell press = classic shoulder-first failure path.
- chinup -- new, BORDERLINE: hanging bodyweight keeps the stabiliser demand; assist
  stack adds force, not a fixed path -> in. the 2026-08-14 "pull family out (no injury
  note)" exclusion used the injury-flag test; the test is now compound freeweight, so
  that exclusion lapsed (same logic brought the rows in).

explicit exclusions (reason kept so it is not re-argued):
- v_squat: plate-loaded machine, fixed path (test 2). also the SAFE SUBSTITUTE back_squat
  moves to when knee pain > 3/10 -- a floor on the escape hatch voids the swap rule.
- chest_supported_t_bar_row: chest pad removes trunk demand (test 3);
  `exercise_fatigue_cost` also low / explicit.
- wall_sit: seconds-based hold, no RIR (`resolve_target_rir` returns None).
- every machine / cable stack + single-joint isolation lift in the program.

## carriers (promoted to tool layer 2026-08-23; owner rule 2026-08-01 "안전 캡은
tool-layer에서 강제 (prompt-only 금지)")

1. program.yaml target slots declare `rir_floor: 2`.
2. rx-calc `resolve_target_rir()` clamps the rep-range band UP to the floor, width kept
   ([0,1] -> [2,3], [1,2] -> [2,3]).
3. set-add prints `RIR_FLOOR_BREACH` + Korean WARN when logged RIR < floor.
   regression: service/health/tests/test-rir-floor.py.
- RIR keyboard stays 0-4 by design: cap the PRESCRIPTION, never the RECORD (capping
  input = falsified log, blinds autoregulation + breach detection).
- program-init never derives `rir_floor`; it checks coverage and names each G19-class
  slot missing one as `W-G19-UNSET` -> answer the floor or record the exclusion reason.

## still model-owned

1. roster judgement: stamp `rir_floor` on new / changed slots by the 3 tests (engine
   honours the field, never derives the roster; a missed stamp = no floor).
2. speech: relay the breach, propose next-session increase. code signals, never talks.
3. increase-signal read: no automation detects RIR >= 3 streaks; target_rir is display
   only, not in progression math.
- behaviour change is felt, not a no-op, for a user whose logs end at RIR 0-1: flag a
  target-lift RIR <= 1 on the spot, propose an increase next session.
