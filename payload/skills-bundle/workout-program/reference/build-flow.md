# build flow -- program-plan move contract, message shapes, stage map

Read when: running a program BUILD (first program or redesign) through
`service/health/program-plan`, or a move's shape looks off. Every sentence and number
is the tool's; this file says what the tool renders so you can recognise it and not
redraw it. The compose step (model lane) is reference/compose.md.

## entry (service-hijack guard)

- direct open = program-BUILD requests only (design / redesign program, routine,
  split). today's-workout / rx requests are NOT this lane.
- program-need offer (never hijack), when workout:pending and: (a) today's-workout /
  rx request or workout log with no program.yaml -> reference/one-off-serving.md, then
  ONE trailing offer line; (b) consult spine just completed (G7 trailing offer); (c) a
  short-habit revision changes frequency with no program to reconcile.

inputs READ, never re-asked: current phase from the kit (user strands,
`metric_axis.phase_order`, active goal rows), standing safety rows, stored place
(`ledger_resource kind='env'`, `ax_machine`), workout history (frequency, weekdays,
gaps), active `weekly_sessions` goal, practiced rotation (`session_type`), profile /
body stats (config). no long-goal row, no mandatory habit, no tradeoff answer (round-2
goal interview) -- the tool does not read them.

## move contract (2026-09-26 owner rehearsal, gaps E1-E14)

the W1-W5 prose ledger collapsed five decisions into one confirm, invented sets / reps,
opened questions it should have proposed, leaked internal terms -> program-plan now
decides the next move and renders it.

- speak `readback` lines, then `say`, verbatim, as ONE message; `choices` = that
  message's buttons (recommended one marked); user's pick (+ own words where the
  payload asks) -> `answer`.
- every program move's LAST readback line = the program card (`card` carries it too):
  quote block `> **[프로그램]**`, then one `> • 칸: 값` line per slot in the order they
  fill (목표 / 장소 / 횟수 / 운동일시 / 보충 / 측정 / 분할 / 집중 부위 / 주의 / 종목 / 유산소; 목표 = the
  goal card's order + deadline, shown when the kit handed it over; 주의 only when a
  safety site exists, in the kit's card words). an empty slot is its label alone
  (`> • 분할:`, no placeholder glyph -- A6); the slot asked now in bold (`emphasis`
  bolds 집중 부위, `field` bolds 종목, `measure` bolds 측정). speak as is; a filled line
  IS the confirmation. the `experience` move carries the card too (no bold slot) --
  speak it as is, never add or strip one.
- EXCEPT the program's FIRST question (journey A2): it rides the goal wrap as ONE
  message -- the goal card (`readback`), the wrap line + transition line, a blank
  line, the question (`say`) -- and carries NO program card (`card: null`). the
  program card opens from the next message. `restart --from program` renders the same
  way (its one line, then the question).
- every `say` ends on the next decision (last line = the question). example answers sit
  BELOW the question: a `예)` line, then one `• ` line per example (as the daytime and
  gym-name moves render, owner 2026-09-26 18:58). confirmations already ride
  `readback`: never add a closing line, never send a confirmation alone, no
  hand-gesture emoji, no backslash escape.
- exception: `done` asks nothing (the card, "프로그램 다 짰어요.", the self-check in ONE
  line). never add a question ("첫 세션 지금 열까요?" retired, owner 2026-09-26 17:48).
  it is never the end either (owner 2026-10-06 21:46): its `then` is the setup tail's
  first question -- send it as a SECOND message in the same reply.
- SETUP TAIL (owner 2026-10-06 21:46 / 21:09; supersedes the 2026-10-03 "switch the
  brief / retros on without asking"): after `done`, `next` walks diet -> first session
  -> morning brief -> daily retro -> weekly retro -> wrap. one message, one decision
  each; the recommended value is marked "(추천)" in the body line only, buttons are
  neutral (그 날로 / 내일 먼저 / 다른 날; <time> / 다른 시간 / 안 받기; 일요일 밤 10시 /
  다른 때 / 안 받기), never a "나중에" button -- a skip in the user's own words is an
  answer (diet `skip`, a time `off`). the open step is the first one unanswered on the
  plan state (`tail: open`), so a user who leaves is resumed there; "later" first ->
  `pick: later` (paused at that step). nothing is switched before the weekly answer:
  then `brief-standard.sh activate` takes the agreed times, an "안 받기" slot is turned
  off (`bundle-routine-ctl.sh off <id>`, `BUNDLE_<ID>=off`), all three off ->
  `deactivate`. the time steps are skipped where the kit verb is absent. a first
  session off the regular days goes on the calendar once (`appt-add`). the wrap is one
  short message: first session, brief, retros, diet target, the calendar line; it asks
  nothing (`stage: wrap`).
- GOAL -> PROGRAM SEAM: inside program-plan the goal wrap folds into the program's first
  question (above). a goal consult run on its own (an explicit goal request, the kit's
  goal-session skill) ends on the kit's wrap: in the SAME reply run `program-plan
  handoff` -- no program yet -> the program's first question; a program in place ->
  one question (`reprogram`: 다시 짜기 / 지금 프로그램 유지; `answer --stage reprogram`,
  redo = `restart --from program`). never wait for the user to ask for the program.
- Before the session preview, ask once for cardio modality and duration. Every
  goal direction gets at least 10 minutes after strength work; a cut can get a
  longer default. The user picks from stepmill, running, incline walking,
  cycling and rowing. Caution sites explain a recommendation, never remove a
  choice. The program card carries the chosen modality and duration.
- The setup tail precedes the final automation consent question (when the pack
  config enables it); the wrap comes after it. One answer
  approves all, approves chosen categories, or skips. Approval calls
  `service/health/hk-ingest consent`; a skip writes no consent.
- `decide` move (split, owner rehearsal 2026-10-01; table form owner 2026-10-05
  10:41) = up to three options: bold `**N. name**` heading (no count; `(추천)` in the
  body only, never in a button label), the week calendar as two `> ` rows, the
  schedule line (`월 앞 · 화 뒤 · ...`, full session names), a day-name gloss only for
  앞/뒤 shapes. no item lines under an option. then ONE comparison block in the
  Telegram Tier-2 form (a blockquote list, never a code block or a markdown table):
  `> 세 안 비교`, the items equal on every option said once (`> 세 안 모두 같아요:
  ...`, only the goal floor and the items a care mode makes relevant), then per option
  `> N. name` with the items that DIFFER stacked as `> • label: value` (split_model
  `compare`: 부위 반복수, the caution sites by their care mode -- `<site> 무겁게 쓰는
  날` for frequency / avoid, `<site> 연달아 쓰는 날` for fatigue, nothing for prep --
  무거운 하체 날, 다리 쉬는 날, 같은 근육 이틀 연속, 스쿼트 다음 날 힙힌지, 익힐 메인
  동작), and a `> 추천: N번. ...` footer naming the measured items that separated the
  pick from the next option by their weighted share of the score ("2번보다 같은 근육을
  이틀 연속 쓰는 일이 3번 적고, 다리 쉬는 날이 2일 많아요."), never the listing order;
  only one option meets the floor -> said so; a recorded current split -> that is the
  reason, plus what the other does better; options short of the floor named after it.
  no minutes anywhere (owner 2026-10-01): every option is composed to the user's
  session minutes. no option holding every limit -> no footer, the no-pick line. prep
  sites are said once in the lead ("무릎·어깨는 운동 전에 풀어 주면 괜찮다고 하셔서,
  어떻게 나누든 준비 동작으로 챙겨요."). ends on "어떻게 나눌까요?". every composable
  option is shown; only an option that could not be built is dropped (never printed as
  a con); no header line. send as is.
- never compose a sentence around a move, never announce a step, never preview the
  next one (no step counter to narrate).
- `compose` has no `say`: the one model-lane step (reference/compose.md).
- `source: kit` move = the kit move loop's own: run the command it names (goal-session
  table), then `program-plan next` again. its `choices[].cmd` argv are kit verbs: run
  them as `database/kit_life.sh <argv...>` (the move's `cmd_runner`), never under
  `service/health/`.

## stage map

| stage | old slot | what the tool does | the one decision |
|---|---|---|---|
| goal | G1-G8 | runs the kit move loop (`goal-interview --next --domain health`) and passes its move through untouched (the kit's own order is its GOAL_JOURNEY: direction, activity, training, safety, order, pace, practice, wrap); an older kit's `ask_safety` without commands and `ask_experience` are answered by the pack's own question and written back through kit verbs | the kit's |
| safety | G4 | the kit asks the ONE safety check inside the goal part (records re-check, narrowed); program-plan READS the answer at the wrap (`ledger_constraint`, the kit's card phrase). the pack's own question runs only when no kit asked it | still the same / anything painful |
| (wrap) | G8 | ONE message (A2): the kit's readback (the filled goal card), its `say` (wrap line; its program transition line is swapped for the calorie step's lead), a blank line, then the calorie step's first question (2026-10-08). when the calorie step closes: its receipt + "다음은 운동 프로그램 상담으로 넘어갈게요. ..." transition line, a blank line, then the program's FIRST question -- the weekly count (횟수), or the place when none is on record. no program card on it -- except when the goal part recorded a gym: the card (장소: 헬스장, bold) opens the gym-name question --, no offer question, no second approval, no care block | -- |
| calorie | G3 | owner 2026-10-08: the calorie step inside the goal part, BEFORE the program. the wrap folds into its first question; one question per message: work pattern (주로 앉아서 / 주로 서서 움직이며 / 몸 쓰는 일 / own words), recent daily steps (5천 미만 / 5천~1만 / 1만 이상 / 잘 모르겠어요 / own number); no watch ask this release (owner 13:56: needs the Dogany app, next version; CAL_WATCH_ASK off); then three blockquote blocks from the record (0.38.2): 기초대사량 (value; sex · age · height · weight · body fat · its source, InBody date or the formula; one-line meaning), 유지 칼로리 (the range + the activity basis), 목표 (target = band middle -/+ the shift, G6-gated (calorie_gate.py); protein g with g/kg; the weekly pace; "2~3주 체중 추이를 보고 다시 맞춰요"), ONE 확정 question. an existing setting with no answered activity (activity_job) asks job + steps first, then the same blocks on its keep / change ask. settled -> the meal-logging guide (photo or product / brand name, rough amounts marked as estimates) + a sample diet card image (diet-status card.py, the settled target, two sample meals) ride the receipt; the settled target is written once (config calorie_target_kcal + maintenance_mid) and the card, the pin and the briefs read it. the Health app link is NOT asked here (the tail's records step). watch kcal never enters the target. its receipt + the program transition ride the program's first question. no body stats or gate unverifiable -> no number, the receipt says why. rules: service/health/calorie_band.py | 이대로 확정 / 숫자 바꿀게요 |
| place | W2 | reads a stored place, gym name included (the kit `place` row the machine registry points at) -- its card line is the statement; a gym the goal part recorded (the kit handoff's `activity` words name 헬스장) -> 장소: 헬스장 on the card, never "can you?", only which gym (owner rehearsal 2026-10-01); else "다니는 헬스장 있으세요?" [네, 다녀요 / 아직 없어요 / 집에서 할래요] (owner 2026-10-08 13:56); 아직 없어요 -> the ideal place + its reason, then "can you?"; a gym with no name on record -> ONE follow-up: which gym (a fact ask), registered as the place (`resource-add --kind env`); home -> one equipment check | gym / none / home (+ other in words); none -> gym / home / other; then the gym's name |
| frequency | W3 count + minutes | the weekly session count AND the minutes a day ("주 몇 회, 하루 몇 분"), BEFORE the days (owner 2026-10-01): the why line (the user's current frequency when the kit handed it over, the goal phase's region floor), three numbered options (rec-1 / rec / rec+1, clamped to 2..6) each on `• 좋은 점:` / `• 아쉬운 점:` (templates by place on the menu: fewest / middle / most days; the 덜 먹는 lines only in a cut, the site phrase only with a site), the recommended one marked in the body (never in a button label); then the minutes paragraph: the range for the training history (program-plan `SESSION_MINUTES`: under a year / beginner 45~60, 1~3 years / returner 60~75, 3+ years 75~90) and, with calendar windows, whether the recommended minutes + prep / cooldown fit the SHORTEST window ("2시간") -- when not, said, and the largest that fits is recommended; a closing that names both ("주 4회, 하루 70분") and one example line. rec count = the kit handoff's `activity` frequency (upper bound of a range), else 3 for a beginner, 4 otherwise; rec minutes = the range's midpoint rounded to 5. buttons "주 N회 · M분" (recommended minutes on each). any count 1..7 and 20..180 minutes are accepted; a count alone keeps the recommended minutes; minutes alone -> the count is asked by itself. the card reads "주 4회 · 하루 70분". the minutes are an initial estimate; goal-complete work determines the duration inside the stated availability. days already answered with no count stored -> the count is the regular days, never asked | 3 / 4 / 5 / other + count [+ minutes, or the user's words] |
| daytime | W3 days + time | A4, an OPEN ask for WHEN, as a time range per day (owner 2026-10-04 19:05): "주 4회 언제 운동하실 수 있어요? 요일마다 몇 시부터 몇 시까지 되는지 알려 주세요." + the calendar sentence from the kit handoff's calendar windows (omitted with no calendar) + the 보충 line + range examples; no dose hint, no minutes question; it may end on "알려 주세요." (a fact ask). ONE answer carries the regular days with their windows AND the extra (보충) days with theirs (`extra_windows`); never asked twice. the window IS the time a day. every answer shape has its handler (see "daytime answer patterns" below): at most ONE narrow follow-up per answer (`daytime:end` / `daytime:range` / `daytime:start` / `daytime:when` / `daytime:confirm`), never a re-ask of the whole question. regular days that differ from the count are accepted: the count follows the days and the next message says so once | windows [+ extra_windows] [+ minutes / unknown / question] |
| measure | P7 | right after the schedule, tied to a training day: the agent's own measure routine on a new training day -> that day, before the session, fasted, STATED on the next message; else the second training day after the weekend -> ONE narrowed proposal, opened by the weekly cadence the goal part declared ("<요일>로" / 다른 요일로); monthly cadence -> the month's first training day, stated. an answer before the daytime is refused (E-STAGE) | ok / other weekday |
| experience | W3b | ONE question records BOTH answers -- the history kind (drives full-body vs split) and the years band the kit's rate model reads (`training_experience`, `training_years_band`, `training_years_band_as_of`, via `config-set`); seven one-tap picks (처음 / 지금 하는 중 x 1년 미만·1~3년·3년 이상 / 쉬었다 다시 x the same bands); records settle what they can (steady run -> band only; 3+ years -> no question; a gap -> one returner confirm). The kit's goal interview asks the training age inside its 운동 slot (`ask_training`) and stores the band + history; a stored band is READ here and never asked again | one pick |
| split | W4 split | ONE decision, three STRUCTURALLY different options sized to the regular day count (one per family, never two of a family: 앞·뒤 / 상체·하체 / 밀기·당기기·하체, full-body families for the full-body norm), ranked by the split model (the phase from the active goals' DIRECTION: a fat-down goal is a cut even with skeletal muscle linked), every composable shape offered (owner 2026-10-01; only a failed composition is dropped), each composed to the chosen session minutes; "하시던 대로 주 N회" leads ONLY on evidence (6+ logged sessions with a session code in 6 weeks) and drops the family of the same shape; a written plan (session_type rows) is only the reason's source ("전에 적어 두신 ...와도 같은 모양이라"). each option carries its calendar and schedule line; ONE comparison block (Tier-2 blockquote) under them carries the differing items and the measured 추천 reason (the `decide` move above). CAUTION CARE (r8): each site carries the user's care mode plus severity (`mild`, `history`, `current`) and, for history, recency (`recent`, `old`). The ko/en cue tables in `compose_rank_rules.caution_care` read these from the site's constraint words. The intensity table controls scoring and composition. Mild means prep only, no load score; old history uses the mode's normal score; recent history doubles that score and excludes the highest loading; current pain excludes all graded loading and returns `handoff_skill: pain-triage`. Split copy states the level once per group and the pain handoff once overall. Silent severity opens ONE merged ask per site (`split:care`, three severity buttons plus `T("free_input")`); history without timing opens one narrow timing follow-up. Known modes are retained; severity-only answers use the table's disclosed product care policy (prep / fatigue / avoid), without another mode question. Answers remain on the safety item and are written through `constraint-add` to the same kit key, preserving the original words. Unknown free text is recorded as unknown and never loops; unknown history timing takes recent precautions without inventing a date. The queue explanation (sessions are a queue over the training days; an extra day is a 보충 session that does not consume it) rides the next decision message | option 1-3 / other |
| focus | W1 | a cut phase STATES it (고르게, the date of the phase check) on the sessions message -- no turn; otherwise PROPOSES first: evenly, or the areas already on the card | even / keep / other areas |
| emphasis | W4 focus-vs-injury | only when a focus area overlaps a safety site, BEFORE compose; recommends protecting, with the reason (a protected area gets no focus lift) | protect / grow carefully |
| compose | W4 lifts | model lane, no user message (THE COMPOSE STEP below): the tool builds a deterministic draft from the data rulebook; default answer accepts it in one step, an edit picks only from the move's shortlists with a Korean `why` per changed lift; the tool doses, holds the weekly volume floor, and refuses what breaks a rule. a floor the session minutes cannot hold (no set fits past them) is NOT a refusal: the draft stands and the move carries `volume_shortfall` ([{muscle, weekly_sets, floor}]) for the consult to mention | -- |
| field | -- | never asked (owner 2026-09-27: the pack decides doses). kept only as a user-initiated override: the user names an amount for one lift -> `answer --stage field` | the user's amount |
| swaps | -- | never asked (owner 2026-10-04 11:44, restating 2026-09-27): a caution site adds its prep drills before the first lift using it and keeps the lift; the only swaps are the data table's (`caution_policy.substitutions`), applied by the compose. The sessions message states each site in ONE line ("우측 무릎 주의: 백 스쿼트 앞에 볼 스퀴즈·무릎 벽 터치를 넣었어요."). The stage stays in the journey so a consult parked here moves on; an answer to it is refused (`E-SWAPS`) | -- |
| cardio | cardio choice | Before cards, choose modality and duration so each card includes it before cooldown. | modality |
| sessions | W4 confirm | Show the finished program card and 2-3 plain lines "왜 이렇게 짰는지": actual minutes per session, priority, and any adjusted lower-priority goal. Use stated training days/windows, recovery and equipment as resources; caution prep and hard floors/caps as constraints. During a cut keep chosen cardio and muscle retention first. Fit balanced weekly muscle volume (including arms, calves, glutes), exactly one core lift per session and functional practice before settling the day length. The history recommendation is a starting estimate, not a cap: use ~100-110 minutes if needed inside 120, never pad to 120. Merge overlapping prep/mobility before trimming lifts and preserve caution care. If the full window cannot hold the complete scope, narrow the lower-priority muscle-size goal and name that adjustment plainly; proceed with the finished program. Never offer resource-fitting menus (85 vs 105 minutes, shorter cardio, fewer lifts) or ask "할까요" about these engine decisions. Only an extra resource beyond stated availability may require one concrete proposal with its reason. The user edits what they dislike. Order: program card, rationale lines, caution/prep notes, then the accept/edit question ("이 네 세션으로 갈까요? ...") LAST -- the message never ends on a declarative line (owner 2026-10-05). | 이대로 / 종목 바꾸기 |
| done | W5 | an existing program is copied to `files/_archive/program-<ts>/` first (no replace question: on onboarding and restart a new plan IS the intent), then writes through program-init, writes `prep.yaml` when there is none, sets consult_modules, and reconciles the calendar BEFORE writing it (D3/P8): the agent's active workout routines on a new training / extra day and its measure routines get an end date and are retired through the kit (`routine update <id> end=<today>`, `routine retire <id>`: rows kept, only future instances cancelled), then one routine per time window ("운동", all-day when no time was said -- a time is never picked) + the measure day ("인바디"). the closing message is the full card + "프로그램 다 짰어요." + the self-check in one line; it asks nothing and carries the setup tail's first question in `then` (its own message). the calendar line ("7월부터 있던 '헬스'·'체중측정' 일정은 이걸로 바꿨어요. 지난 기록은 그대로예요."), the first session and the brief / retro times are said by the tail's wrap, never here; carries `care` and `next_session` as data | -- |
| diet | tail 1 | while the diet module is pending / offered~1: the kit's daily target (kcal · protein) | 이 숫자로 시작 / 숫자 바꾸기 (no numbers: 지금 계산하기 / 숫자 직접 정하기); skip from the user's words |
| first | tail 2 | the next regular day + time + the queue's first session; tomorrow's supplementary slot when there is one | 그 날로 / 내일 먼저 / 다른 날 |
| brief | tail 3 | the morning brief, 30 min before the earliest training start | <time> / 다른 시간 / 안 받기 |
| retro | tail 4 | the daily retro, the kit's resolved time | <time> / 다른 시간 / 안 받기 |
| weekly | tail 5 | the weekly retro day + time; the answer switches the three slots through the kit | <day time> / 다른 때 / 안 받기 |
| records | tail 6 | the iPhone Health app link, the ONE link offer after the whole consult (0.38.2): steps come from the phone (watch optional), workout time / heart rate / watch kcal and sleep come in automatically; watch kcal is reference only, the food target follows steps and the weight trend. DEV CHANNEL ONLY (`health_link.offer_gate`: framework DOGANY_UPDATE_CHANNEL dev/main AND the Dogany app connected); never asked once `health_link` is answered. yes -> hk-ingest passes + consent + config `health_link=linked`; no -> `health_link=declined`. outside the consult (close-out `HEALTH_LINK_OFFER:`, the weekly recalibration's "건강 앱 연동") answer with `program-plan answer --stage health_link --json '{"pick":"yes"}'` (or no) | 연동하기 / 안 할게요 |
| wrap | tail end | one short "all set" message: first session, brief, retros, diet target, calendar line | -- |
| automation | after done | one final question for workout, steps, heart rate, sleep and active calories; calls `hk-ingest consent` only for approved kinds | approve all / select kinds / skip |
| blocked | -- | no lift fits the place: asks to pick the place again | place |

Current closing behavior: before the four-session preview, `program-plan` records
the goal, caution, spacing, practice, health and cardio checks. The cardio
pick precedes this preview; caution prep and table swaps are stated in it, never asked. A failed preview check returns
to the silent compose step with the failing plan. The closing move includes
only checks that passed, the dated first session, and the 21:00 reminder
promise. Workout calendar routines keep the owner's title `헬스`, end at the
goal horizon, and use a lead alert for the prior night at 21:00 plus a start
alert. When the start alert arrives, open the next session through
`session-open` for that date and deliver its mat-prep opening.

The order above is program-plan's `JOURNEY` tuple; an answer for a stage while an
earlier one is open is refused (E-STAGE, nothing recorded). tests/test-journey-order.py
pins it end to end with the real kit.

No move offers "later" (no button, no sentence -- journey K8). If the user says it
first, answer the stage with `pick: later`: the build pauses (`paused`, exit 3) and the
next `next` resumes where it stopped.

## daytime answer patterns (D12 point 3, owner review 2026-10-04)

the days ask is designed for its answers: every shape below has ONE handler in
program-plan (`apply_daytime`, `daytime_followup`, `apply_daytime_followup`). put
the user's words into the payload shape in the middle column; the tool decides the
follow-up. never more than one follow-up per answer: what that follow-up still
leaves open is planned on the recommendation and SAID (a default used is a default
stated).

| the user says | payload | what happens |
|---|---|---|
| full ranges: "월·금 6시~8시" | `windows: [{weekdays, start, end}]` | recorded, no follow-up |
| a start only: "평일 7시부터" | `windows: [{weekdays, start, end: null}]` | ONE follow-up `daytime:end`: "몇 시까지 운동하실 수 있어요?" (one start per group when they differ); answer `ranges: [{weekdays, end}]` |
| a length only: "2시간", "90분" | `minutes: 120` (no windows) | minutes recorded; ONE follow-up `daytime:when` (which days, what time); answer with `windows`. days said but no time ("월수금 90분") -> `daytime:start` ("... 몇 시에 시작하세요?") |
| days only: "월·수·금", "평일" | `windows: [{weekdays, start: null, end: null}]` | ONE follow-up `daytime:range`: "월·수·금요일 몇 시부터 몇 시까지 되세요?"; answer `ranges: [{weekdays, start, end}]` |
| a vague time: "퇴근 후", "새벽", "점심시간", "저녁", "아침", "밤" | `windows: [{weekdays, vague: after_work / dawn / lunch / evening / morning / night}]` | never refused: the tool guesses a concrete range (퇴근 후 / 저녁 19:00~21:00, 새벽 06:00~07:30, 아침 07:00~08:30, 점심시간 12:00~13:00, 밤 21:00~22:30) and asks to confirm in ONE line (`daytime:confirm`) with a one-tap button "네, 그렇게 해요" -> `pick: ok`; a correction in free text -> `ranges` |
| per-day mixed: "평일 6~8시, 주말은 아무 때나" | one window per distinct time; the "아무 때나 / 시간 되면" days: `anytime: true` on a regular day, or in `extra_windows` when they are 보충 days | per-day windows; an anytime regular day has no time limit and is planned on the recommended day, said in one line ("토요일은 시간 제한 없이 권하는 하루 85분으로 잡을게요.") |
| undecidable: "그때그때 달라요", "모르겠어요" | `unknown: true` (+ the days in `windows` when said) | planned on the recommendation, said: "운동 시간이 정해지지 않아서 우선 권하는 하루 85분으로 잡을게요. 시간이 정해지면 언제든 말씀해 주세요."; no days either -> the count spread over the week (주 4회: 월·화·목·금), said too |
| an answer plus a question: "6~8시요. 근데 주말에도 해도 돼요?" | the answer as above + `question: "<the question, verbatim>"` | the answer is recorded FIRST; the next move carries `aside` -> answer the question in one or two lines from the plan's own facts, then speak the move's `say` as is |
| out of range: an end before the start, a window under 20 minutes, minutes outside 20..180 | as said | refused, nothing recorded (`E-TIME` / `E-DAYTIME`); stderr carries a `SAY` line: the reason and ONE narrow re-ask ("끝나는 시간이 시작보다 앞이에요. 저녁 8시부터 몇 시까지 되세요?") -- speak it as is, once |

a window shorter than the recommended day (60 against 85, even 30) is NOT refused and
does not stall the build: fit inside it, narrow the lower-priority scope if needed,
and state that decision with the finished sessions (the sessions row above).

## Legacy time answers

Previously saved explicit time answers remain parseable for compatibility. New
resource fitting follows the trainer judgment rule above and does not emit a
tradeoff menu. A user-requested change to days, minutes, cardio or exercise choice
still updates those facts and triggers a fresh fit.

## the care ask's answers (split stage, `split:care`, r8)

Cognitive budget: zero questions when severity and needed timing are stated;
one merged level/care question otherwise; only a history answer missing time
allows one timing follow-up. No separate mode question, no repeat after an
answer. Every ask carries buttons and exactly the shared free-input line.

| the user says | payload | what happens |
|---|---|---|
| occasional stiffness | `pick: mild` | prep, zero split load score; next site or split |
| a significant past injury | `pick: history` | retain known mode; ask timing only if missing |
| pain now | `pick: current` | avoid loading; `pain-triage` skill handoff, no triage implemented here |
| less than a year / at least a year | `pick: recent` / `old` | timing recorded; next site or split |
| own words, possibly with mode and time | `pick: other`, `words` | the same cue tables read all three fields at once |
| explicitly names care modes too | optional `modes: [prep, fatigue]` | preserve these modes alongside severity and timing |
| vague / unknown | `pick: other`, `words` | persist unknown; never repeat the same question |
| side question | no answer write | answer briefly, `program-plan reask` (one line, the existing buttons) |
| invalid pick / empty other | invalid payload | refuse without recording an answer |

Timing is elapsed time, not a claim of continuous recovery: 12 months is old;
`작년` / last year is conservatively recent because the date is ambiguous.
School days / athlete days indicate old history. Current pain overrides a
past injury cue; negated pain does not. The live knee/shoulder warm-up words
resolve to mild + prep for both, with no question and unchanged split scores.

## journey rules around the moves

- restart ("다시 하자", "처음부터", "목표부터 다시"): `service/health/program-plan
  restart` -- the ONE path. the plan state goes to `files/_archive/restart-<ts>/`, the
  kit's `goal-interview --restart` archives the unfinished interview and keeps finished
  goals active until the new wrap; the returned move (restart line + the direction
  question) is spoken as is. "프로그램만 다시": `restart --from program` (goal kept,
  the 운동일시 asked again). never reset state or re-interview by hand.
- side question (the user asks instead of answering): answer in your own words, at
  most 3 sentences, grounded in the move's own facts (split stage: read the option
  facts off `program-plan next` silently -- never paste its output). a claim about how
  a lift loads a joint or muscle (angle, grip, range) is looked up in
  `knowledge/kimwog/items` first and said only as far as the item grades it. then
  `program-plan reask`: its ONE `say` line (the open move's own question) and its
  `choices` re-armed as an `[[OPTIONS]]` marker. never re-send the program card, the
  readback, the session lists, the lead or the option bodies -- already on screen.
  nothing is recorded, no new question (owner 2026-10-05; live 2026-10-07 15:52).
- a shape the user names outside the offered menu is still pickable: the split answer
  takes any eligible family key for his day count (e.g. `{"pick": "ab4"}`) or
  `{"pick": "other", "rotation": [...]}`; never tell him it is unavailable.
- a correction riding an answer ("1번, 근데 금요일은 6~8시"): put it in that answer's
  payload as `patch: {daytime: {windows, extra_windows}}`; applied at once, never a
  question back.

## care beyond the lifts (owner rehearsal 2026-09-26, functional direction)

a user strand on a program-computed measure -> program-plan adds `CARE_ITEMS`: 5-min
joint prep + core activation before (with prep for each safety site), 5-min cooldown
stretch after, breathing / bracing cue on heavy lifts, the body-signal line. data
(`care` in plan state, on the card and the `done` move); in the consult they ARE the
sessions' `매트 준비` / `마무리 스트레칭` slots and the closing cues sentence (round 3),
not a block of their own. never compose them as prose.

## where the numbers come from (E7)

compose payload REFUSES any number (`E-NUMBER-FROM-MODEL`). doses = program-plan
`RX_RULES`, transcribing reference/program-rules.md 「워킹 무게를 정하는 방식」 (compound
5-8 / isolation 12-15) + 「최소 세트 하한 정책」 (3 working sets). weights start `null`
(ramp-up measures, owner 2026-07-19). core drill -> 12-15, unregistered hold -> 3 x 20 s,
unclassified lift -> the isolation scheme; no dose is ever asked (owner 2026-09-27).
a hold is picked by PURPOSE (`builds_size: false`), see program-rules.md. first program: every slot at the set floor; compose holds the
WEEKLY VOLUME FLOOR itself (owner 17:38): sets raised / trimmed silently in [3, 5] per
slot; a program no set change fits is refused (`E-VOLUME-FLOOR` / `E-VOLUME-CEILING`,
nothing recorded) -> add or drop a lift. no volume question; sessions message states it
in one sentence.
practice rows (a goal-strand practice slot: roll-down, bear crawl, get-up --
`compose_rank.practice_only_names`) are NOT band volume (owner 2026-10-04): rx-calc
leaves them out of the weekly-set band (proposed and actual) and reports them apart
(`--volume-audit` `practice`); the sessions message and volume-say say them on their
own line ("연결 연습은 근육 세트와 따로 세요: ...").
loaded functional moves count HALF (owner 2026-10-04 11:21): the factor is data,
`compose_rank_rules.json` `muscle_credit` (loaded / bodyweight per row). kettlebell
swing, a loaded get-up / bear crawl -> 0.5 x sets toward their mapped muscles;
roll-down, a bodyweight bear crawl / get-up -> 0. loaded = the slot's load (weight_kg
> 0 or a non-bodyweight `load`; a logged set: weight_kg > 0), not the name. they are
also said on their own line ("부하를 건 기능성 동작은 근육 세트에 일부만 세요: 케틀벨
스윙 주 3세트 = 근육 1.5세트로 계산."). conditioning blocks stay cardio, never sets.

## domain rules the stages carry

- spillover valence (old W1): a pain word in the focus answer = SAFETY fact -> `answer
  --stage safety` with `changed` / `some`, never a focus area. aspiration without pain
  words ("어깨가 약해요") = focus area.
- focus vocabulary: shoulders, chest, back, arms, legs, calves, abs, glutes. written to
  `program.yaml focus_areas`; rx-calc reads there first, legacy long row only fallback.
- F7 HARD ORDER (owner ruling 2026-09-18: a gym was assumed though no place
  was said): no lift named before the place is known. structural: `compose` after
  `place`, `candidates` filtered by the place's equipment. a gym is never assumed.
- STRUCTURE NORM (owner 2026-09-18, F4): beginners AND returners get FULL-BODY (a split
  hits each part once a week, slowest way back). only continuous training opens a split
  at week 0. revisit at 4-6 weeks (SKILL.md 분할 전환).
- training experience (beginner | returner | continuous) feeds STRUCTURE only, never
  speech depth (reference/speech-register.md). "2년+" earns ONE register offer, handled
  there.

Current pain returns a `handoff` move at the split screen, with
`handoff_skill: pain-triage`, one pain sentence and no split choices. A
split answer is refused while current pain is recorded. The existing
pain-triage skill owns assessment; this flow only resumes after the safety
record reflects the outcome. No unavailable split is offered as a remedy
for pain, and extra time or different equipment is not proposed as one.
