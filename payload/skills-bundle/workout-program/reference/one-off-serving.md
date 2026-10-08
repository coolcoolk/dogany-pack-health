# Free-session serving + decline / degradation

Read when the owner asks for today's workout, names a region or lifts, or says
"어깨 하자", "오늘 가슴이랑 삼두", or "그냥 자유롭게 할게". This applies with
or without program.yaml, including a paused program consult.

## F1 FREE SESSION (owner override, 2026-09-28)

Offer a real free session. A missing program card never blocks per-set storage,
record-backed prescriptions, volume, or fatigue accounting. The spoken one-off
suggestion is the proposal step, not the whole service. Do not create or change
program.yaml, the planned calendar, or any paused consult state to start it.

- Read the exercise catalog and active safety rows. Use `session-open --free
  --regions shoulders --venue gym --dry-run` for proposals, or `--exercises
  dumbbell_lateral_raise,reverse_pec_deck_fly` for owner-named lifts. Region names
  are comma-separated; `shoulders`, `chest`, `arms`, and individual muscles work.
- F7 still applies: if neither records nor a registered place establish the venue
  and equipment, ask the place question before naming lifts. Pass `--venue` only
  after the owner supplies it; otherwise the recorded venue is used.
- The proposal reuses compose ranking and `loads_caution_area`. A shoulder caution
  excludes overhead main lifts; knee cautions use the same compose precedents.
  Do not replace those checks with a model-authored safety shortlist.
- On workout intent, run `session-open --free` with the chosen regions/lifts.
  Use the returned session id with ordinary `exercise-enter`, `set-add`,
  `set-arm`, `set-table`, and `session-cursor`. `exercise-enter` can append a
  catalog lift to an initially empty free session. `session-closeout <id>`
  preserves the free tag and writes the ordinary closeout/tombstone.
- All working sets are stored normally. Prior logged working loads seed the
  prescription. Without history, ask for the actual first calibration set;
  never invent a starting weight. Example: "먼저 편하게 할 수 있는 무게로 해 보고,
  무게랑 횟수를 알려 주세요."
- Default prescription: 3 working sets, 6–10 reps, existing factored rest;
  compound freeweights retain the G19 RIR floor of 2. Explain briefly when needed:
  "오늘은 기본 3세트로 시작해요."
- Opening copy: "좋아요. 오늘은 자유 운동으로 하고, 세트마다 기록할게요."
- Free prescriptions live in session-local runtime files, not the owner's
  program card. They never advance rx-calc's planned rotation. A paused consult
  stays untouched and can resume later.

## trailing offer

- workout:pending -> append the single module offer line:
  "원하시면 운동 계획도 같이 짜드릴게요. 말씀만 주세요."
- workout:declined -> NO trailing offer of ANY lane inside the 30-day cooldown.
  At >= 30 days with cooldown UNCONSUMED, the ONE cooldown re-offer rides the
  serving (state -> declined@D~r same turn). Consumed -> permanent offer silence.
  Ledger rules: reference/consult-modules.md "Completeness ledger".
- A paused consult is not permission to restart or overwrite that consult.

## decline / degradation

Declining a program does not decline workout logging or free sessions. Bulk
summary logging and generic advice remain available too. Later program acceptance
resumes from existing consult artifacts; a free session supplies real history.
