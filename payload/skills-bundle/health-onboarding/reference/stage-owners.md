# consult stages -- what each collects and who owns it

Read when: the user asks what is left or who handles a part, a stage misbehaves, or
you need to know which tool owns an answer. Routing only; the rules bind in the tools
(program-plan stages, the kit move loop) and in workout-program reference/build-flow.md.

| step | what it collects | who owns it | lane |
|---|---|---|---|
| G0-G7 | 지향 (direction FIRST -- it decides 종목/분할/순서), the user's own strands, and ONE current-phase goal (a multi-week phase or a first habit -- the kit move loop picks). Later phases are named, not numbered; promotion is the weekly review's. The kit's wrap ends it: no second summary, no second approval | the kit move loop (`goal-interview --next --domain health`, read through program-plan) + `$CONSULT` for the pack's domain content (G3 calculator numbers, G6 safety gate) | kit renders the words and writes; LLM carries them |
| G1-pre / O3 | body state -- weight, 체성분, 인바디 | asked by the move loop (`ask_baseline`: photo or height + weight) only when the record lacks it; a photo goes to `inbody-capture` (kit). | LLM extracts, kit CLI writes |
| G6 (journey G4) | injuries and pain history -- UNSKIPPABLE, asked BEFORE the order decision and any number, and "없어요" is a complete answer; rows on record -> one-tap re-check | the kit move loop's `ask_safety` (program-plan reads the answer at the wrap; its own `safety` stage only when no kit asked); `pain-triage` owns events from here on | tool renders, LLM carries the answer |
| G3 calorie step (2026-10-08) | 목표 상담 안, 프로그램 상담 전: 하루 보내는 방식(근무 패턴) → 최근 하루 평균 걸음 수, 각 한 번씩 (워치 연동은 다음 버전, 2026-10-08 13:56) → 유지 칼로리 범위(시작 추정)와 가운데 기준 목표, 확정 한 번. 워치 칼로리는 목표에 넣지 않음 | `service/health/program-plan` `calorie` stage (`answer --stage calorie:job|steps|result`), G6 gate = diet-status `calorie_gate.py` | tool renders and gates, LLM carries the answer |
| W1-W5 (now program-plan stages) | 운동 장소 (기록에서 읽음; 없거나 이름이 없을 때만 질문), 운동일시 (기본과 보충 요일·시간), 인바디 요일, 분할/전신, 부위 목표, 세션별 종목, 유산소 종목·시간 | `service/health/program-plan` (its `JOURNEY` order); stage map in workout-program reference/build-flow.md | tool proposes and renders; LLM names lifts only |
| setup tail | 프로그램을 쓴 뒤 한 대화로 이어서: 식단 목표 (목표 상담 안의 칼로리 단계가 확정했으면 다시 묻지 않음) → 첫 세션 날 → 아침 브리핑 시간 → 일간회고 시간 → 주간회고 요일·시간 → "설정이 모두 끝났어요" 요약 (owner 2026-10-06 21:46; the 10-03 "turn on without asking" is retired) | `service/health/program-plan` (`then` of `done`, then `next` / `answer --stage diet|first|brief|retro|weekly`); times switched through the kit's `brief-standard.sh` at the weekly answer | tool renders, LLM carries the answer; a user who leaves is resumed at the open step (hook TAIL_RULES) |
| goal -> program | 목표 상담이 따로 끝난 경우(명시적 목표 요청) 같은 답장에서 `program-plan handoff`: 프로그램이 없으면 첫 질문, 있으면 다시 짜기 / 유지 | `program-plan handoff` / `answer --stage reprogram` | never a dead stop between consults |
| final consent | 프로그램 마무리 뒤 운동·걸음·심박·수면·활동 칼로리 자동 기록 승인 또는 건너뛰기 | `program-plan automation` → `service/health/hk-ingest consent` | user chooses once; kit owns the consent ledger |
| restart | "다시 하자" / "처음부터" / "프로그램만 다시" | `service/health/program-plan restart [--from goal|program]` -- the ONE path (kit `goal-interview --restart` behind it); nothing deleted, finished goals stay until the new wrap | tool archives and renders; LLM speaks the returned move |
| side question | a question instead of an answer, mid-consult | the agent: own words, at most 3 sentences, grounded in the move's own facts (split: read `program-plan next` silently, never paste it); then the ONE line `program-plan reask` returns, the SAME choices re-armed as an `[[OPTIONS]]` marker (never re-send the card, the readback, the session lists, the lead or the option bodies); a biomechanics claim is looked up in `knowledge/kimwog/items` first; a shape named outside the offered menu is still pickable (nothing recorded) | LLM |

owner rulings 2026-09-18 bound in program-plan, not here (this table only routes):
- 장소/장비 (F7): a place on record (kit place registry, mined history) is a READ, never a
  question; only its ABSENCE is asked (ideal place + reason, then "can you?"); no lift
  named before the answer (lift step after place, candidates filtered by place). a gym
  is never assumed (owner ruling: the place was never said, so a gym must not
  be assumed).
- 경력·연속성 + 구조 (F4): options hold the RETURNER ("2년 했는데 1년 쉼"); beginners and
  returners get FULL-BODY, split revisited at 4-6 weeks. binds in `experience` / `split`.
