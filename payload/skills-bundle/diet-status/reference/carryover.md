# calorie carry-over v0.2 (read when a carry value is present or the user asks why the target moved)

user's gap statement (2026-09-10): "오늘 칼로리 초과면 내일 덜먹는다거나 이런 기전이 없어".
narrowed 2026-10-11 21:03: "많이 먹으면 그걸 감수해야지, 건강이 제일 우선" -- overeating is
absorbed, not paid back across the week.

```bash
python3 .claude/skills/diet-status/carryover.py --json     # machine
python3 .claude/skills/diet-status/carryover.py            # KEY=VALUE
```
derived, never stored: inputs = `measure` rows the weekly criterion reads + goal detail
fields + the settled target (config `calorie_target_kcal`) when one is set.

## the rule (v0.2)
- window = YESTERDAY only. no week boundary, no spread over the days left.
- yesterday must be complete (>= 3 meal slots). partial / unlogged -> no carry,
  `dropped_days` 1, `dropped_dates` = yesterday.
- `surplus_kcal` = yesterday intake - yesterday's effective target (settled target, else
  the rule's rest / training day target).
- `carry_kcal` = min(surplus, cap). `absorbed_kcal` = the rest: dropped, never carried
  to any later day.
- cap = `CARRY_CAP_KCAL` 300, a product constant (no per-day reduction bound in the
  knowledge warehouse; the ~500 kcal/day lean-mass figure in nutrition 062 bounds a
  standing deficit, not one day's cut). override: kit config `carry_cap_kcal`.
  `carry_cap_source` says which applied.
- safety gate (G6) still applied LAST on the aim; `cut_kcal` = what actually came off.

## two touchpoints, both existing. do not build a third.
- morning brief = WHY. kit `morning-brief.sh` probes carryover.py, renders `why_line`
  verbatim, only when the number moved. probe = quiet degrade when pack absent.
  e.g. "어제 400kcal 더 드셔서 오늘 목표를 300kcal 낮췄어요. 오늘 목표는 1,450kcal예요."
- status card = RESULT. pass `carry_kcal` top-level (card-render.md).

## how to speak it
- ate MORE yesterday -> today's target comes down by at most the cap. the rest is
  absorbed: never say it will be made up later, never a "debt".
- ate LESS -> ERASED. target does NOT go up. undershoot is not credit; fat loss follows
  cumulative deficit. carry floored at 0: carry only lowers a target (the safety
  floor may then lift it, safety-gate.md).
- large deficit -> `floor_pressure`. REPORT, never assert: state projected week vs
  declared floor and let it stand. never say they ARE under-eating, no health
  consequence, no nudge. (EA threshold graded C / contested; IOC consensus calls itself
  guidance, not diagnosis.)
- `dropped_days` > 0 = yesterday unlogged / under-logged, so nothing carried. if it
  comes up: "어제는 기록이 비어서 뺐습니다". never read a missing record as not eating.
- `applicable: false` or `cut_kcal` 0 -> say nothing. no filler encouragement.
- protein NOT carried (day-to-day make-up graded C; the daily total graded A,
  a per-meal saturation ceiling graded B and disputed, kimwog nutrition 008). calories
  only until that changes.
