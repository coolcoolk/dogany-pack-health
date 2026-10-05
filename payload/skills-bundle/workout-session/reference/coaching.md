# coaching judgement -- intensity, performance, reorder, variant switch, cardio
read when judging intensity / a performance drop, reordering lifts, switching a variant,
or starting a cardio block.

## intensity scale = RIR (defaults; a slot's rep_range wins)
- compound working sets: RIR 1-2 · isolation: RIR 0-1 · ramp-up sets: RIR 4+.
- floor override (2026-08-23): the 10 compound free-weight lifts take RIR floor 2-3 over
  these defaults. list, criteria, reasons: workout-program "복합 프리웨이트 RIR 하한 정책".
  never prescribe RIR 1-2 on them from this scale.
- next-set target RIR comes from the slot (via NEXT_HINT, code-derived, F11), never copied
  from the RIR just reported.

## floor breach -- `RIR_FLOOR_BREACH` / `RIR_FLOOR_NOTE` (D5, 2026-08-24)
code enforces the floor twice: rx-calc clamps the band (`_apply_rir_floor`), set-add
detects a breach at record time (owner 2026-08-01: safety caps in the tool layer).
```
RIR_FLOOR_BREACH <session> <exercise> set_seq=<n> rir=<r> floor=<f>
RIR_FLOOR_NOTE: [RIR 하한] <종목> <n>세트 RIR <r> ... 이 종목 하한은 RIR <f> ...
```
- first line A (suppressed). second line B: drop the prefix, relay the WHOLE sentence. do
  not summarise, soften or skip; it is a safety notice.
- the set is recorded as reported (code never raises it); never imply the record changed.
- "RIR" inside it is the tool string; relay as printed (vocabulary.md "RIR display").
- tone: not a scolding. room above the floor = a signal to add weight next time; the
  sentence already says so; add nothing.
code: service/health/set-add (`_rir_floor` + breach branch), service/health/rx-calc
(`_apply_rir_floor` / `resolve_rir_floor`). suite: service/health/tests/test-rir-floor.py.

## performance drop -- 3 steps (G6)
never jump to one cause ("과음 피로 탓").
1. compare logs: last session of the same lift (weight / sets / RIR) vs today.
2. fold in self-report (sleep / fatigue / pain).
3. judge from 1 + 2, keep several candidates open: "X 가능성이 높으나 Y도 배제하기 어렵다".

## change framing = delta by default (G9)
say direction + size vs before, not a lone absolute: "지난 세션 대비 2kg 증가" / "3회
줄었지만 RIR은 동일".

## live reorder (G13)
before confirming a mid-session order change, check: shared muscle overlap before / after
(e.g. hammer curl right before chin-up -> forearm / grip stacking) and back-to-back
grip-heavy lifts. impact -> one line + confirmation; none -> confirm at once. never reorder
without the check.

## live variant switch (G14)
bilateral -> single-leg (or similar) switched live: first one bilateral set at the plan
weight for feel, confirm, then single-leg working sets. the bilateral set is its own
guided step with its own confirmation, never merged. not for slots planned single-leg.

## cardio target heart-rate zone (Karvonen, lazy)
only when a live cardio segment (stepper / treadmill / bike) needs a zone. max_hr derives
from birth_year (never asked). resting_hr = 60-day valid series; missing / expired -> ask
once in session, Apple Watch "휴식기 심박수" widget value only (not the "심박수 범위" low).
freshness check / ask script / formula / write path: read reference/cardio-hr-zone.md.
