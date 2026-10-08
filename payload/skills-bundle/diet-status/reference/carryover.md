# calorie carry-over v0.1 (read when a carry value is present or the user asks why the target moved)

user's gap statement (2026-09-10): "오늘 칼로리 초과면 내일 덜먹는다거나 이런 기전이 없어".
weekly criterion judges after the fact; carry gives a number to steer by before the next meal.

```bash
python3 .claude/skills/diet-status/carryover.py --json     # machine
python3 .claude/skills/diet-status/carryover.py            # KEY=VALUE
```
derived, never stored: inputs = `measure` rows the weekly criterion reads + goal detail
fields. no table, no constant.

## two touchpoints, both existing. do not build a third.
- morning brief = WHY. kit `morning-brief.sh` probes carryover.py, renders `why_line`
  verbatim, only when the number moved. probe = quiet degrade when pack absent.
- status card = RESULT. pass `carry_kcal` top-level (card-render.md).

## how to speak it
- ate MORE than the days allowed -> CARRIED, today's target comes down.
- ate LESS -> ERASED. target does NOT go up. undershoot is not credit; fat loss follows
  cumulative deficit. `carry_kcal` floored at 0: carry only lowers a target (the safety
  floor may then lift it, safety-gate.md).
- large deficit -> `floor_pressure`. REPORT, never assert: state projected week vs
  declared floor and let it stand. never say they ARE under-eating, no health
  consequence, no nudge. (EA threshold graded C / contested; IOC consensus calls itself
  guidance, not diagnosis.)
- `dropped_days` > 0 = some day unlogged / under-logged, left out of both sides. if it
  comes up: "그 날은 기록이 비어서 뺐습니다". never read a missing record as not eating.
- `applicable: false` or `cut_kcal` 0 -> say nothing. no filler encouragement.
- protein NOT carried in v0.1 (day-to-day make-up graded C; the daily total graded A,
  a per-meal saturation ceiling graded B and disputed, kimwog nutrition 008). calories
  only until that changes.
