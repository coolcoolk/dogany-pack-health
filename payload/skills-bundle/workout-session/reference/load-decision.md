# load decision ownership (read when today's weight will differ from the engine's, or the user questions a load)

owner ruling (batch P2, 2026-08-24; distinct from the "no over-explaining" P2): the AGENT
owns today's weight. rx-calc's verdict (`up` / `hold` / `deload`) is INPUT, not decision.
the reason for the decision is also the agent's to give.
(what happened: engine `hold` @ X; model wrote a lower `--ov-weight`, stored with no
reason; when asked, cited the engine it had just overridden and threw the choice back:
"<낮은값> 유지냐 <엔진값> 복귀냐 사용자가 고르시면 돼요.")

## rules (all enforced by `set-arm gate_weight_override`)
1. differ from the engine -> `set-add --ov-reason "<한 줄>"`. reason = the agent's
   observation (logs, performance, condition). "엔진이 hold라서" is not a reason.
2. unsure -> lower side, decided by code: an unreasoned heavier override does not go out;
   the gate serves the engine weight and says so in a sentence. a decision, not an error.
   assist machines invert direction (code handles it).
3. user-named weight -> `--ov-by owner`. not gated; recorded as the owner's decision.

## banned (load up / down only)
- "<낮은값> 유지냐 <엔진값> 복귀냐 사용자가 고르시면 돼요" and every variant: `고르시면` /
  `선택해 주세요` / `A냐 B냐` / weight candidates as `[[OPTIONS]]` buttons. throwing the load
  decision back is dereliction, not friction.
- the engine as shield ("엔진 판정도 hold 였고요"). mention the engine only beside the
  agent's decision: "엔진 판정은 유지(<엔진값>)인데, 저는 ...라고 봅니다".

## say it -- code writes the sentence
weight differs -> set-add prints `LOAD_DECISION: <문장>`, set-table repeats it under the
table. relay verbatim. shape (set-arm `load_decision_say`): conclusion
(`오늘 <종목> <N>kg으로 갑니다`) -> the engine value it weighed + one-line reason ->
one-phrase undo.
the last clause is not a menu; never attach one.
code: `service/health/set-arm gate_weight_override` / `load_decision_say`.
grill: `service/health/tests/test-progression-ownership-p2.py`.
