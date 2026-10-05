# placement / order -- slot priority, route, pre-fatigue, session phases

Read when: slot order, drill order, lift placement, route, zone change, "순서 바꾸면
어때", makeup-slot reorder, or any program.yaml order edit. Read
`files/program/gym-layout.md` too (hop matrix exists; never improvise route from prose).

## order rules (gym-layout.md "사용" section is canonical)

1. 슬롯 우선순위 = top constraint (below). route and kinematic order sit under it.
2. kinematic order next (prep -> slot, injury priming order). inside it, minimise hops.
   conflict -> route loses.
3. pre-fatigue interference = kinematic constraint (owner 2026-08-17; second case
   owner 2026-08-08), applies to accessory lifts only: never put a lift that burns
   grip / forearm or the same muscle head BEFORE a lift that head bottlenecks. owner
   cases: 「해머컬 → 친업 순서 배치 금지 (그립/이두 선피로)」, 「인클라인 덤벨 컬을 해머
   컬보다 먼저 배치」. forearm burners (hammer curl, farmer carry) never before a grip-
   or biceps-bound accessory lift.
   the main slot is exempt and engine-owned: compose_rank.ordered() places the main
   lift first always, and E-MAIN-SPINAL forces the heaviest spinal-loading lift (e.g.
   deadlift) into the main slot on a hinge day -- deadlift-first on back days is
   correct, never move it behind an accessory. `order_day_exercises` (program.yaml
   `priority`) carries the same-slot accessory order; the pre-fatigue call above is
   the designer's prose rule for that layer only.
4. same-zone items adjacent (fewer zone revisits).
5. prep right before a slot ends in the slot's zone or an adjacent one.
6. source grade: zones A-G + 4 mappings (월싯->A, 스탠딩 카프레이즈->C, 친업바->C,
   행잉 레그레이즈->E) are owner-confirmed; every other lift->zone map is agent
   inference. looks wrong -> suspect the inference first, never "user decided so".

## 슬롯 우선순위 (2026-08-24, user rule -- data is canonical)

owner: design with priority from the start -- the tail may get cut, so what comes
first matters more; rehab first is correct, bake it into program setup.

field, not prose -- code enforces:
- SoT = program.yaml per-slot `priority` (int, lower first) + `role`
  (warmup|main|focus|rehab|prehab|accessory). band contract in that file's header.
- applied in `rx-calc.load_yaml` -> `order_day_exercises`. set-table / set-arm /
  exercise-enter / session-open / session-cursor all go through it: one order only.
- guard `service/health/tests/test-slot-priority.py` (rehab / prehab / focus behind
  accessory -> red). run it after any program.yaml order change.

design rules:
- sessions end when they end; the tail gets cut. protect a slot by placing it ahead
  of the cut line AT DESIGN TIME.
- injury flag != rehab slot. a main lift carrying a safe-execution condition is
  already in front; do not move it. move only slots that exist FOR rehab / prehab and
  sat at the back.
- classify from `program-history.json` safety_notes + ledger_constraint
  injury_knee / injury_shoulder (user ledger keys), not by feel.
- reorder renumbers `slot`. prep.yaml `card_slot` / `live_slot` and
  program-history.json safety_notes keys are keyed (day, slot): remap them by LIFT in
  the SAME commit. follow the lift, not the number.
- order rule only: never touches slot count / sets / reps / weight.
- layout edits (zones / adjacency / map) = this skill; owner-confirmed items change
  only with owner ok.

## 분할 배치 원칙 -- 복근/종아리 (F31)

placement/order is engine-owned: core and calves may appear on both halves of a
split (compose_rank_rules.json `session_regions` lists both for every split code);
the only cap is calves at most twice a week unless focused (`E-CALVES-CAP`). never
state a fixed half (e.g. "abs on front days only, calves on back days only") --
follow the engine's session assignment, not a half-based rule.

## 세션 페이즈 모델 (owner 2026-08-14)

verbatim: 「세션 페이즈 모델 확정: 매트프렙 / 기구프렙 / 운동(종목직전 프렙 interleaved) / 유산소 / 쿨다운」

    매트프렙 -> 기구프렙 -> 운동(종목 직전 프렙은 그 종목에 붙여 interleave)
             -> 유산소 -> 쿨다운

rx-calc already knows mat / equipment prep + cooldown in code. cardio position and
"pre-lift prep attaches to its lift, not a block" are prose only -> a new program off
this order makes the owner re-place every time.
