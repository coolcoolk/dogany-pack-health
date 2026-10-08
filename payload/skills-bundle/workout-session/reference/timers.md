# timers -- rest, hold, start gate, water (read when arming a hold / press-start timer or diagnosing a missing push)

## rest timer (live set-by-set only, DGN-303 path; never for bulk logging)
arming, two channels, fire condition, rest formula = code (service/health/set-arm,
set-add, rx-calc). the main path `set-arm <sid> <ex> <seq>` runs only after a real, newest
set write (`rest_bound` / `set_write_bound`, enforced since C12-B 2026-08-24), and refuses
after the last prescribed set (F14). countdown is placed LAST by code (`emit_countdown`
defer, F11), so table -> cue -> timer holds on screen.
channel-2 milestone pushes log attempt + result to `files/program/.ch2-push.log`
(`CH2_INTENT` / `CH2_OUT=SENT|FAILED|SUPPRESSED-gen`, #42). INTENT without OUT = dropped by a
connection blip. retry / queueing is the bridge transport layer (framework), not here.
rest-over push starts with "✅ {sec}초 휴식 완료" (not on hold sets).

## start gate (#22)
"~하자 / ~할게 / ~도 하자 / 마무리하자" = plan statements, not execution. never start a
timer on them. timers (incl. press-start hold countdowns) fire only on a real trigger:
explicit "시작" / "준비됐어" / [시작] button (start / ready) or a set / rep completion
(set_done). mechanism: `set-arm countdown <sec> --trigger <start|ready|set_done>`;
`--trigger` required, no valid trigger -> code refuses (`GUARD_BLOCKED`). pass the real
trigger. the bridge renderer countdown.py is the framework's; the gate lives in the arming decision.

## hold timer affordance (no dead air, 2026-08-17)
a message that arms a hold / isometric countdown (`set-arm countdown ... --label ...`)
carries its done / next affordance in the same message, unless code already delivered
one (`HOLD_SET_BTN` / `HOLD_CHAIN_BTN` / `KEYBOARD_DELIVERED` / `AFFORDANCE`).
- no code affordance -> end the message with an authored `[[OPTIONS]]` done / next button.
- scope: hold / isometric working sets, cooldown stretch holds, mat-prep hold drills, every
  set-arm countdown hold. not rest timers between rep sets (set logging advances those).
- rep-based working sets never get timer buttons; only timed holds (isometric hold / dead
  hang / stretch / cooldown) get countdown + done seconds + next / done branch.
- after the hold: `HOLD_NEXT: <label>` names the next action (다음 세트 / 다음(진행) / 완료),
  never a fixed "다음". `AUTO_ADVANCE` with it -> do it now; the label only names it.
  `[[OPTIONS]]` only for 2+ real candidates; `NEXT_ACTION_MISSING` -> no auto-advance,
  relay and confirm (D3, 2026-08-24).
- left / right unilateral holds: `set-arm hold-chain` (owner 2026-08-20/21) emits timer +
  buttons itself; never add buttons. left done fires the right timer at once, no "start"
  step between. right done = record + advance.
- detail (branch rules, self-advance wording, 3-way label SoT, unilateral chain):
  reference/hold-unilateral.md.

## water (15-minute cadence)
each turn read the injected clock. >15 min since the last water line -> one water line
rides the next outgoing message (T-60 early push or chat reply). not a separate alert, not
per set. code also fires its own water line (set-arm WATER_LINES) on channel 2.
wording (#35, owner 2026-08-19): a natural full sentence with light reason, varied each
time, never a telegraphic fragment, never preachy, no over-explaining to a user who knows:
"물 한 모금 하고 가시죠. 세트 사이 수분 채우면 다음 세트 힘 잘 붙습니다." /
"목 마르기 전에 미리 한 모금. 탈수되면 근력·집중 다 떨어집니다." /
"잠깐 물 한 모금, 페이스 유지하기 좋습니다."
