# phase 4 -- program review detail (read when audit FLAGs or a roll-back is considered)

## escalation flags (from `pain.py audit`)
- recurring-fault -> propose program change (substitute / load cap / tempo).
- recurring-side -> check L/R imbalance, unilateral fix.
- rising-pain -> propose load cap / substitute / deload.

steps:
1. propose change to 사용자, explain why.
2. ON APPROVAL only: route via safety ledger + workout-program (owns program.yaml).
   ledger write = main session + explicit approval (one-writer rule). never auto-edit.
3. link it: `pain.py resolve --id <n> --program-change "<what changed>"`.
4. several proposals at once -> one decision per message (workout-session pacing rule).

## recovery candidate (de-escalation, ACTIVE roll-back)
audit does NOT compute this. agent judges from `pain.py list --exercise <slot>`
(rule-lane candidate: see docs/skill-compaction/pain-triage.md).
- primary trigger: pain <= 2 on that part / exercise for K sessions (default 3) OR
  N weeks straight, AND no load_drop / substitute / stop action in that window.
- strengtheners: (a) load-tolerance rise -- conditional-progression lift took normal
  progression with no pain hold in window; (b) primer-dependence drop -- cutting a
  primer cue left no pain.

steps:
1. POST_SESSION only (phase 2 flow). never a separate push, never morning brief.
   ONE proposal line: one-axis one-step re-exposure probe, exactly one of
   {load up one step | ROM cap up one step | primer reduce one step}. never stack axes.
2. ON APPROVAL only: workout-program applies probe to program.yaml; workout-session
   shows an in-session verify cue on that slot ("오늘 회복 테스트: <축> <새 값>, 아프면
   바로 말해 주세요").
3. verify in session:
   - pain-free -> settle the step (cap raised / substitute reverted / primer trimmed);
     update safety ledger + mirror safety_note.
   - pain recurs -> revert to prior value same session, log pain event, tell 사용자:
     "아직 이르네요, 되돌렸습니다".
4. rejected -> cooldown, do not re-offer for N sessions.

## evidence grade (recovery)
self-reported pain + training-log PROXIES, not tissue-recovery measurement. mechanical
pain: "pain 0" may only mean trigger load / posture was never re-touched. recovery is
gradual + conditional, verified by the probe. never say "healed" / "다 나았다".
