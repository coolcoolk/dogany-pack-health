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
- An owner-named lift that is not in the catalog is never refused ("목록에 없어서
  안 돼요" is banned). `session-open --free` exits `NOT_IN_CATALOG <name>`; re-run it
  with `--register <name>=<catalogued sibling>@<implement>:<표시 이름>` (e.g.
  `barbell_clean=kettlebell_clean@barbell:바벨 클린`) -- kit `exercise-add` with the
  sibling's muscle map -- confirm in one line, then prescribe and record normally.
- The open serves the planned session's surfaces through the same code: the 표3 pin
  and lineup card (`START_CARD`), `CARE` lines, and a composed mat prep + cooldown
  stretch for today's lifts (`PREP_ENTRY` at the first lift). Equipment drills
  (machine / kettlebell) are equipment prep on their lift, never "매트"; the
  adduction machine is served only with a squat. A loaded drill states its recorded
  weight (`PREP_LOAD`) or, with no record, a first-time estimate (`PREP_LOAD ... load_source=estimate`) -- never an ask.
- All working sets are stored normally. Prior logged working loads seed the
  prescription. Without history the code prescribes the climb: `CALIBRATION_RAMP` /
  `LOAD_ESTIMATE_SAY` (empty bar or lightest weight first, a transferred ramp target
  when a related lift is on record) -- relay it; never say "편한 무게로 해 보세요".
  Owner-reported sets below the band are warm-up rungs (`RIR_ASK`: ask the RIR);
  a set in the wrong lane is `set-reclass <sid> <ex> <seq> --to ramp|working`, not
  undo + re-add.
- Code posts and your prose never contradict: a code value you judge wrong is
  changed through a verb (`set-arm --ov-weight`, `set-reclass`, `set-undo`); never
  tell the owner to ignore a machine post. A step-down the code posted after a set
  below the rep floor ("150kg × 3회 -- 다음 세트는 120kg") stands; "표의 ×10은 현실과 안
  맞아요" is the banned shape. Record the owner's report as reported: never pass the
  weight they just lifted back as `--ov-weight` (set-add drops it, `OV_ECHO_DROPPED`).
- The session's lift list is not the session (owner 2026-10-10 13:09 / 13:58): a lift
  the owner names mid-session -- a catalog lift (`kettlebell_swing`) or a registered one
  (`barbell_clean`) -- is appended with `exercise-enter <sid> <name>` and every set is
  recorded with `set-add` (volume, fatigue, the card). Never "이 설치본에서 세트 기록이 안
  되는 종목이라 메모로 남길게요". A lift whose implement is the load (swing, kettlebell
  clean, slams) is dosed by reps (10-40), never calibrated as a warm-up. After the last
  listed lift the code posts "✅ <종목> 끝 ... 다른 종목도 하시면 이름만 말해 주세요" -- the
  session stays open until the owner ends it.
- Interval rounds the owner asks for (e.g. swing 30s/30s × 3): `session-post interval
  <sid> --name <종목> --work 30 --rest 30 --rounds 3`. One countdown runs the whole
  block; say in one line that it does not cue each round (`INTERVAL_GAP`). Never send
  the owner to a phone timer without saying why.
- "집갈래" / "끝" -> `session-closeout <sid>`: the free day's cooldown is offered once
  (`CLOSEOUT_REFUSED post_blocks` -> `session-post next`), a skip is `session-post
  skip`, then close-out. Minutes are open -> close (the first close-out request), or the
  watch workout when the watch is onboarded (`WATCH state=onboarded`); kcal is asked by
  hand only when `WATCH` says consent_only / none. Never `workout-upd` the minutes after
  the card posted.
- Default prescription: 3 working sets, 6–10 reps, existing factored rest;
  compound freeweights retain the G19 RIR floor of 2. Explain briefly when needed:
  "오늘은 기본 3세트로 시작해요."
- Opening copy: "좋아요. 오늘은 자유 운동으로 하고, 세트마다 기록할게요."
- Free prescriptions live in session-local runtime files, not the owner's
  program card. They never advance rx-calc's planned rotation. A paused consult
  stays untouched and can resume later.

## planned owner wants another body part today (2026-10-12)
With a program, "오늘 상체해야겠는데" on a 하체 queue day is a fork between two RUNNABLE
paths, never "순번 변경": `[[OPTIONS: <swap> 정규로 | 자유 세션]]` from rx-calc
`split_choice.fork` (`<swap> 정규로` = `session-open --split <swap>`; `자유 세션` =
`session-open --free`). A free session in the last 72 h is said as its `recent_load` line
and steers `swap` away from its regions. Full rule:
workout-session reference/session-start.md "another body part today". Unsure a path runs -> dry-run first.

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
