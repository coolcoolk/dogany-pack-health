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
- exception: `done` states the next session and asks nothing. never add a question
  ("첫 세션 지금 열까요?" retired, owner 2026-09-26 17:48).
- Before the session preview, ask once for cardio modality and duration. Every
  goal direction gets at least 10 minutes after strength work; a cut can get a
  longer default. The user picks from stepmill, running, incline walking,
  cycling and rowing. Caution sites explain a recommendation, never remove a
  choice. The program card carries the chosen modality and duration.
- The program wrap precedes the final automation consent question. One answer
  approves all, approves chosen categories, or skips. Approval calls
  `service/health/hk-ingest consent`; a skip writes no consent.
- `decide` move (split, owner rehearsal 2026-10-01) = up to three options, every one
  on the SAME lines so they compare: bold `**N. name**` heading (no count; `(추천)` in
  the body only, never in a button label), the schedule line (`월 앞 · 화 뒤 · ...`,
  full session names), a day-name gloss only for 앞/뒤 shapes, then `• 부위마다: 주 N번`
  / `• <sites> 부담: ...` (the last only with a safety site: per site the day types whose
  sessions USE that joint -- safer swapped variants count, they still load it -- and on
  how many days a week, e.g. "무릎은 하체 날(주 2일), 어깨는 상체 날(주 2일)", read the
  same way on every option). no minutes line (owner 2026-10-01): every option is
  composed to the user's session minutes. then ONE paragraph comparing every shown
  option from those facts only (no minutes talk): 부위마다 frequency first (up to the
  goal floor), then how the site days spread (sites on different days, then a site over
  more days = less load per day); the menu is ordered the same way, and options equal
  on all of it keep the model's order with the tie-break said plainly. ends on the pick,
  and "어떻게 나눌까요?". every composable option is shown; only an option that could
  not be built is dropped (never printed as a con); no header line. send as is.
- never compose a sentence around a move, never announce a step, never preview the
  next one (no step counter to narrate).
- `compose` has no `say`: the one model-lane step (reference/compose.md).
- `source: kit` move = the kit move loop's own: run the command it names (goal-setting
  table), then `program-plan next` again. its `choices[].cmd` argv are kit verbs: run
  them as `database/kit_life.sh <argv...>` (the move's `cmd_runner`), never under
  `service/health/`.

## stage map

| stage | old slot | what the tool does | the one decision |
|---|---|---|---|
| goal | G1-G8 | runs the kit move loop (`goal-interview --next --domain health`) and passes its move through untouched (the kit's own order is its GOAL_JOURNEY: direction, activity, training, safety, order, pace, practice, wrap); an older kit's `ask_safety` without commands and `ask_experience` are answered by the pack's own question and written back through kit verbs | the kit's |
| safety | G4 | the kit asks the ONE safety check inside the goal part (records re-check, narrowed); program-plan READS the answer at the wrap (`ledger_constraint`, the kit's card phrase). the pack's own question runs only when no kit asked it | still the same / anything painful |
| (wrap) | G8 | ONE message (A2): the kit's readback (the filled goal card), its `say` (wrap line + "다음은 운동 프로그램 상담으로 넘어갈게요. ..." transition line), a blank line, then the program's FIRST question -- the weekly count (횟수), or the place when none is on record. no program card on it -- except when the goal part recorded a gym: the card (장소: 헬스장, bold) opens the gym-name question --, no offer question, no second approval, no care block | -- |
| place | W2 | reads a stored place, gym name included (the kit `place` row the machine registry points at) -- its card line is the statement; a gym the goal part recorded (the kit handoff's `activity` words name 헬스장) -> 장소: 헬스장 on the card, never "can you?", only which gym (owner rehearsal 2026-10-01); else the ideal place + its reason, then "can you?"; a gym with no name on record -> ONE follow-up: which gym (a fact ask), registered as the place (`resource-add --kind env`); home -> one equipment check | gym / home / other; then the gym's name |
| frequency | W3 count + minutes | the weekly session count AND the minutes a day ("주 몇 회, 하루 몇 분"), BEFORE the days (owner 2026-10-01): the why line (the user's current frequency when the kit handed it over, the goal phase's region floor), three numbered options (rec-1 / rec / rec+1, clamped to 2..6) each on `• 좋은 점:` / `• 아쉬운 점:` (templates by place on the menu: fewest / middle / most days; the 덜 먹는 lines only in a cut, the site phrase only with a site), the recommended one marked in the body (never in a button label); then the minutes paragraph: the range for the training history (program-plan `SESSION_MINUTES`: under a year / beginner 45~60, 1~3 years / returner 60~75, 3+ years 75~90) and, with calendar windows, whether the recommended minutes + prep / cooldown fit the SHORTEST window ("2시간") -- when not, said, and the largest that fits is recommended; a closing that names both ("주 4회, 하루 70분") and one example line. rec count = the kit handoff's `activity` frequency (upper bound of a range), else 3 for a beginner, 4 otherwise; rec minutes = the range's midpoint rounded to 5. buttons "주 N회 · M분" (recommended minutes on each). any count 1..7 and 20..180 minutes are accepted; a count alone keeps the recommended minutes; minutes alone -> the count is asked by itself. the card reads "주 4회 · 하루 70분". the program is then composed TO the minutes (fewer sets per lift, then fewer lifts; never a longer day). days already answered with no count stored -> the count is the regular days, never asked | 3 / 4 / 5 / other + count [+ minutes, or the user's words] |
| daytime | W3 days + time | A4, an OPEN ask naming the count: "주 4회로 정했으니, 운동하는 4일의 요일과 시간을 알려 주세요." + the calendar sentence from the kit handoff's calendar windows ("캘린더에는 월요일 6~8시, 화~금요일 5~7시로 운동이 잡혀 있어요.") and, when the calendar has more days than the count, the fixed / 보충 sentence (both omitted with no calendar) + the 보충 line + examples; it may end on "알려 주세요." (a fact ask). ONE answer carries the regular days with their windows AND the extra (보충) days with theirs (`extra_windows`); never asked twice. regular days that differ from the count are accepted: the count follows the days and the next message says so once | windows [+ extra_windows] |
| measure | P7 | right after the schedule, tied to a training day: the agent's own measure routine on a new training day -> that day, before the session, fasted, STATED on the next message; else the second training day after the weekend -> ONE narrowed proposal, opened by the weekly cadence the goal part declared ("<요일>로" / 다른 요일로); monthly cadence -> the month's first training day, stated. an answer before the daytime is refused (E-STAGE) | ok / other weekday |
| experience | W3b | ONE question records BOTH answers -- the history kind (drives full-body vs split) and the years band the kit's rate model reads (`training_experience`, `training_years_band`, `training_years_band_as_of`, via `config-set`); seven one-tap picks (처음 / 지금 하는 중 x 1년 미만·1~3년·3년 이상 / 쉬었다 다시 x the same bands); records settle what they can (steady run -> band only; 3+ years -> no question; a gap -> one returner confirm). The kit's goal interview asks the training age inside its 운동 slot (`ask_training`) and stores the band + history; a stored band is READ here and never asked again | one pick |
| split | W4 split | ONE decision, three STRUCTURALLY different options sized to the regular day count (one per family, never two of a family: 앞·뒤 / 상체·하체 / 밀기·당기기·하체, full-body families for the full-body norm), ranked by the split model (the phase from the active goals' DIRECTION: a fat-down goal is a cut even with skeletal muscle linked), every composable shape offered (owner 2026-10-01; only a failed composition is dropped), each composed to the chosen session minutes; "하시던 대로 주 N회" leads ONLY on evidence (6+ logged sessions with a session code in 6 weeks) and drops the family of the same shape; a written plan (session_type rows) is only the reason's source ("전에 적어 두신 ...와도 같은 모양이라"). each option carries its schedule line and the same comparison lines; the recommendation paragraph compares every shown option. The queue explanation (sessions are a queue over the training days; an extra day is a 보충 session that does not consume it) rides the next decision message | option 1-3 / other |
| focus | W1 | a cut phase STATES it (고르게, the date of the phase check) on the sessions message -- no turn; otherwise PROPOSES first: evenly, or the areas already on the card | even / keep / other areas |
| emphasis | W4 focus-vs-injury | only when a focus area overlaps a safety site, BEFORE compose; recommends protecting, with the reason (a protected area gets no focus lift) | protect / grow carefully |
| compose | W4 lifts | model lane, no user message (THE COMPOSE STEP below): the tool builds a deterministic draft from the data rulebook; default answer accepts it in one step, an edit picks only from the move's shortlists with a Korean `why` per changed lift; the tool doses, holds the weekly volume floor, and refuses what breaks a rule. a floor the session minutes cannot hold (no set fits past them) is NOT a refusal: the draft stands and the move carries `volume_shortfall` ([{muscle, weekly_sets, floor}]) for the consult to mention | -- |
| field | -- | never asked (owner 2026-09-27: the pack decides doses). kept only as a user-initiated override: the user names an amount for one lift -> `answer --stage field` | the user's amount |
| swaps | -- | never asked (owner 2026-10-04 11:44, restating 2026-09-27): a caution site adds its prep drills before the first lift using it and keeps the lift; the only swaps are the data table's (`caution_policy.substitutions`), applied by the compose. The sessions message states each site in ONE line ("우측 무릎 주의: 백 스쿼트 앞에 볼 스퀴즈·무릎 벽 터치를 넣었어요."). The stage stays in the journey so a consult parked here moves on; an answer to it is refused (`E-SWAPS`) | -- |
| cardio | cardio choice | Before cards, choose modality and duration so each card includes it before cooldown. | modality |
| sessions | W4 confirm | ALL sessions in ONE message, plain blockquotes: `> **앞A · 대퇴사두·가슴·어깨**`. One names-only prep line, lifts as `N. name S set × lo~hi reps (primary muscles)`, cardio, one names-only cooldown line. No kind or sub-lines. Titles sum primary-muscle working sets, exclude core, top three with ties by first appearance. Detailed heads roll up through muscle_node parents; back subdivisions retain their named muscles. | 이대로 / 종목 바꾸기 (changed sessions are re-checked) |
| done | W5 | an existing program is copied to `files/_archive/program-<ts>/` first (no replace question: on onboarding and restart a new plan IS the intent), then writes through program-init, writes `prep.yaml` when there is none, sets consult_modules, and reconciles the calendar BEFORE writing it (D3/P8): the agent's active workout routines on a new training / extra day and its measure routines get an end date and are retired through the kit (`routine update <id> end=<today>`, `routine retire <id>`: rows kept, only future instances cancelled), then one routine per time window ("운동", all-day when no time was said -- a time is never picked) + the measure day ("인바디"). the closing message is the full card + "프로그램 다 짰어요." + what went on the calendar and what it replaced ("7월부터 있던 '헬스'·'체중측정' 일정은 이걸로 바꿨어요. 지난 기록은 그대로예요.") + the next session + the cues sentence, and NO question; carries `care` and `next_session` as data | -- |
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

## journey rules around the moves

- restart ("다시 하자", "처음부터", "목표부터 다시"): `service/health/program-plan
  restart` -- the ONE path. the plan state goes to `files/_archive/restart-<ts>/`, the
  kit's `goal-interview --restart` archives the unfinished interview and keeps finished
  goals active until the new wrap; the returned move (restart line + the direction
  question) is spoken as is. "프로그램만 다시": `restart --from program` (goal kept,
  the 운동일시 asked again). never reset state or re-interview by hand.
- side question (the user asks instead of answering): answer in your own words, at
  most 3 sentences, grounded in the move's own facts (split stage: read the option
  facts off `program-plan next` silently -- never paste its output). then ONE short
  return line naming what is still open, and re-arm the SAME choices as an
  `[[OPTIONS]]` marker with the move's own labels. never re-send the program card, the
  lead or the option bodies -- already on screen. nothing is recorded, no new question.
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
