---
name: health-onboarding
display_name: 헬스 첫 설정
description: >
  DOMAIN ONBOARDING for this health-trainer agent -- the step that runs AFTER
  the framework's identity onboarding (dogany-user-onboarding) and BEFORE the
  agent is usable. It fires on STATE, not on a phrase the 사용자 has to know:
  (1) IMMEDIATELY after identity onboarding completes -- the moment the five
  identity answers (name / emoji / address term / tone / humor) are filled and
  the ONBOARDING_PENDING block is deleted, this skill runs in the SAME turn as
  the completion message. Do not close first contact with "아무거나 던져주세요"
  / "무엇이든 말씀해 주세요" / "ask me anything" and wait: an agent that just
  claimed 운동 기록·프로그램 설계·라이브 세션·식단 관리·체성분 추적 while
  holding no goal, no body state, no injury history and no split cannot serve
  any of them, and the 사용자's first "운동 시작" hits `session-open exit 1`.
  (2) At the START of any session on an instance that has finished identity
  onboarding and still has NO usable training card
  (files/program/program.yaml absent, or its session_type rotation rows
  missing) -- a first contact that was interrupted, crashed, or never happened
  is resumed, never restarted.
  (3) On a first-contact utterance that has no domain content yet -- "뭐부터
  하면 돼", "시작하자", "설정하자", "뭘 해줄 수 있어", "어떻게 쓰는 거야",
  "where do I start", "let's begin", "set me up".
  NOT on an explicit goal request -- "목표 상담 시작하자", "목표 설정하자",
  "목표 다시 잡자", "set my goals": that is the goal-setting skill's turn,
  even with the gate OPEN. This skill speaks no opener then and resumes only
  after the goal card is complete (the program consult hand-off).
  MANDATORY FIRST ACTION, ALWAYS: run `service/health/onboarding-gate verdict`.
  The gate -- not recall, not the transcript -- decides whether this runs.
  Gate exit 3 (NO-OFFER) means STOP and say nothing about setup: a 사용자 who
  already has a card must NEVER be re-interviewed, and identity onboarding must
  never be interleaved with. This skill OWNS NO INTERVIEW of its own: it routes
  to the consult spine (workout-program reference/AGENT-CONSULT.md), to
  goal-setting and inbody-capture (kit_life) and to pain-triage, and the
  program card is written ONLY by service/health/program-init. It designs no
  split, invents no goal and ships no default program.
---

# health-onboarding -- the continuity between the agent introducing itself and a real first session

Closes the 2026-09-15 hole: identity onboarding ended on "편하게 아무거나 던져주세요" with
zero domain state (owner ruling: agent onboarding must flow straight into the
workout-goal onboarding, never stop there). This skill walks the user from the identity close to the card. Audit + ledger:
docs/skill-compaction/health-onboarding.md (pack repo).

## firing + done signal

three legs (post-mint inline, next-message UserPromptSubmit, every SessionStart); read
reference/firing.md when debugging whether the entry fired.

DONE SIGNAL = THE ARTIFACT. `onboarding-gate` computes from `program.yaml` + the
`session_type` rows via `program-init check` (their only reader). no flag, no sentence
closes it. interview ends without a card -> gate stays OPEN, offered again next session;
never offered -> `session-open` still refuses and names `program-init`. a miss costs one
session, not the install. all files are pack payload, so this survives a framework
update; a local edit to `dogany-user-onboarding` would have been
reverted by the next framework update -- that is why this is not one.

## paths (resolve once; PROJECT_ROOT, never cd into a skill dir)

```bash
GATE="service/health/onboarding-gate"
INIT="service/health/program-init"
for c in .claude/skills/workout-program .claude/skills-bundle/workout-program; do
  [ -d "$c" ] && WP="$c" && break
done
CONSULT="$WP/reference/AGENT-CONSULT.md"
```

`goal-setting` + `inbody-capture` are KIT skills (`kit_life`, manifest `requires_kit`).
resolve activation-first: `.claude/skills/<name>/SKILL.md`, then
`.claude/skills-bundle/<name>/SKILL.md`. missing -> kit absent or older than the
manifest requires: say so, skip that step, never reimplement its interview.

## step 0 -- THE GATE. Always. Before any word to the 사용자.

```bash
service/health/onboarding-gate verdict
```

| exit | line | do |
|---|---|---|
| 0 | `VERDICT OFFER <reason> <tier>` | run this skill from step 1 |
| 3 | `VERDICT NO-OFFER identity-pending` | STOP. `dogany-user-onboarding` owns this turn; never interleave two interviews |
| 3 | `VERDICT NO-OFFER identity-absent` | STOP. identity onboarding not started |
| 3 | `VERDICT NO-OFFER complete` | STOP, say NOTHING about setup. never re-interview a user who answered (D3/D6) |
| 3 | `VERDICT NO-OFFER declined-exhausted` | STOP. declined twice; passive. serve what they asked |
| 1 | `VERDICT ERROR <why>` | STOP, report the environment fault. never proceed on a guess |

OFFER `reason` = where to RESUME:
- `absent` -- no card. full run from step 1.
- `registry-drift` -- card exists, `session_type` rows do not. they already answered: no
  re-interview. `service/health/program-init sync`, re-run the gate
  (`routines/bundle/health-install-ensure.sh` may already have fixed it -> `complete`).
- `invalid` -- card fails its own contract. never overwrite: `service/health/program-init
  validate` names every error; `workout-program` owns structure repairs. bring the errors.
- `unknown` -- program-init check gave an unexpected exit; treat like ERROR: report its
  detail, no interview.

record the offer in the same turn (skip when the UserPromptSubmit leg already did -- its
context says so): `service/health/onboarding-gate offered --by health-onboarding`.
"not now" -> `service/health/onboarding-gate declined`. ladder = the consult spine's
`consult_offered` ladder: never declined -> declined once (one re-offer) -> exhausted
(passive). it only WITHHOLDS; only the card says complete (D2). never touch the latch
file by hand.

## step 1 -- CONTINUATION OPENING = goal-setting's first message, nothing added

the domain opening IS the goal consult's own first message (owner 2026-09-27: goal
consult is its own skill and starts as itself -- entered directly, later for revision,
or after identity onboarding). same shape on every leg (inline, UserPromptSubmit,
SessionStart): NO transition line of this skill's, NO settings recap, NO quote or
records lead, NO second message.

- run `service/health/program-plan next`; with zero goals its move is the kit's
  goal opening. speak `readback` then `say` VERBATIM: intro (i18n
  `goal.opening.intro.health`, 3 lines), the empty goal card, the G1 question +
  its three examples.
- inline: that move is the TAIL of the identity close message (after the framework's
  role recap + capability list), never a second message.
- no move (kit absent / older) -> the G1 question + examples verbatim from `$CONSULT` G1,
  nothing before them.
- EXPLICIT GOAL REQUEST ("목표 상담 시작하자", "목표 설정하자", "목표 다시 잡자") ->
  goal-setting owns the turn, even with the gate OPEN; this skill adds nothing. it
  resumes after the goal card is complete: the kit wrap's 「다음은 운동 프로그램 상담으로
  넘어갈게요」, then `program-plan next` (step 2).

The shipped first message (kit-rendered, ko):

```
운동 목표랑 지향을 잡아볼게요.
지향은 어떤 몸, 어떤 운동을 원하는지 정하는 큰 방향이에요. 목표는 그 방향으로 가면서 언제까지 무엇을 얼마나 할지 정한 숫자예요.
이야기하면서 아래 표를 같이 채워나갈게요.

<empty goal card>

목표하는 모습이나 운동 목표가 있으신가요?

버튼을 선택하거나 직접 말씀해 주세요.
```

buttons attached to that message (the kit move's `choices`, one per axis): 보디빌더 같은 몸 / 10km 마라톤 대회 완주하기 / 주 4회 운동하기 (owner 2026-10-05 10:45: answer examples are buttons, free input still taken).

NO CONSENT GATE, NO EASY OUT (journey K8): no "지금 시작할까요?" / start-now-or-later
question or button before G1, and no "later" line (consult spine G0 consent slot = 0,
`$CONSULT` G0 continuation entry). the user postpones first ("나중에", "다음에", "지금은
됐어") -> `onboarding-gate declined`, stop, no re-ask in that reply.
forbidden: numbered capability menu, settings recap, records / stats dump, process
preview (Pacing A3), how-long copy, two questions in one message, urgency framing (D5b).

## step 2 -- hand off to the consult spine. No second interview.

- READ `$CONSULT` BEFORE THE FIRST QUESTION (cold by design; carries choreography,
  pacing, question budget, G6 safety gate). this skill is its missing ENTRY, not a
  replacement. run it FRESH-path (`entry_path = fresh`); the `$CONSULT` pre-flight decides,
  and on the migration path it defers instead of interviewing.
- ONE DRIVER, ONE MOVE PER TURN (2026-09-26): from the G1 answer on -- goal part, safety
  check, program (kit wrap folds into the program's first question; no offer question) --
  loop `service/health/program-plan next` / `program-plan answer --stage <stage> --json
  '<payload>'`. speak `readback` then `say` verbatim, offer `choices`. `source: kit` move ->
  run the command it names (the `goal-setting` skill's table), then `next` again. never
  write a sentence of your own around a move, announce a step or preview the next one.
  move contract: workout-program reference/build-flow.md.
- RESTART = ONE PATH: "다시 하자" / "처음부터" / "목표상담부터 다시" -> `service/health/
  program-plan restart` ("프로그램만 다시" -> `--from program`); speak the move it returns.
  never reset state, delete rows or re-run the interview by hand (nothing is deleted;
  finished goals stay active until the new wrap).
- SIDE QUESTION (asked instead of an answer): answer it in your own words, at most 3
  sentences, grounded in the move's own facts (split stage: read the option facts off
  `program-plan next` silently -- never paste its output). then ONE short return line
  naming what is still open, and re-arm the SAME choices as an `[[OPTIONS]]` marker with
  the move's own labels. NEVER re-send the program card, the lead or the option bodies --
  already on screen. nothing recorded, no new question.
- a shape the user names outside the offered menu is still pickable (e.g. split: any
  eligible family for his day count, or a named custom rotation) -- never call it
  unavailable.
- no persona emoji, praise or cheering around a move while the consult runs.
- stages: goal G0-G7 (kit), body state (`inbody-capture` for a photo), G6 injuries
  (unskippable, before any number; `pain-triage` owns events after), W1-W5 program-plan
  stages. read reference/stage-owners.md when asked what is left or who owns a part.
- pre-answered later step -> consume-ahead: record, FAST-CONFIRM in one line when its
  step arrives. never re-ask an answered question (D6: repeat target 0).

## step 3 -- the last answer WRITES. No "and then save it" step.

sessions confirm ("이대로") leads to the cardio choice, self-check, and wrap.
The optional app consent appears only when the explicit pack config flag enables it;
it is off by default. Program-plan `done` hands the answers to
`program-init write`, which writes `files/program/program.yaml` AND the `session_type`
rows in the SAME call (same `rotation:` list), retires the agent's old workout / measure
routines (end date, rows kept) and registers one routine per time window + the measure
day, writes `prep.yaml` when none, renders the closing message (asks nothing itself).
The flow does not end there: the move's `then` is the setup tail's first question, sent
as a SECOND message in the same reply. Tail = diet target -> first session -> morning
brief time -> daily retro time -> weekly retro day/time -> short wrap. One decision per
message, with buttons; resumable (plan state `tail: open`). Nothing is switched on
unasked: brief / retros are activated from the agreed times after the weekly answer.
Detail: workout-program reference/build-flow.md.
(`program-init next / answer` = lower-level contract; `program-init schema` = data.)

**YOU NEVER WRITE `program.yaml`.** not Write, not heredoc, not "just this once": a file
you author is a program the 사용자 never chose, and session-open / rx-calc would run it
with nothing saying the numbers were invented (D1).

close the loop; report what you measured:

```bash
service/health/onboarding-gate verdict      # expect: NO-OFFER  complete
```

- `complete` -> one line: set up, "운동 시작" now opens a real session. no capability list.
- anything else -> say so plainly, name what is outstanding. "설정 끝났습니다" over an
  open gate is the defect this skill closes.

## what this skill must never do

- Invent a split, goal, target weight, deficit or rep scheme. The interview COLLECTS;
  no default program ships anywhere in this pack (D1).
- Run when the gate says NO-OFFER. Not "briefly", not "to confirm".
- Ask more than one question per message, or preview the remaining steps.
- Push. One offer, one bounded re-offer, then passive (D5b).
- Mention this pack -- name, install state, what installing it unlocked (F12, owner
  2026-09-18). install status is a READ, never a question. the pack's declared
  self-offer moment (NOT-installed case, spoken by the kit) is the split transition at
  4-6 weeks, never onboarding; single home = workout-program SKILL.md "분할 전환".
- Edit the framework's identity onboarding, `identity/hot.custom.agent.md`, or anything
  outside this pack's payload. the handoff INTO the domain is a framework-lane change,
  reported upstream separately.
