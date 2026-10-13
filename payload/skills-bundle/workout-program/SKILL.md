---
name: workout-program
display_name: 운동 프로그램 설계
description: >
  Handles weight-training PROGRAM DESIGN, revision, and update -- building or
  changing the workout program card (files/program/program.yaml), NOT logging a
  workout and NOT running a live set.
  (1) Build/redesign: fires when 사용자 asks to make/design/redesign a program,
  routine, or split -- "운동 프로그램 짜줘", "루틴 만들어줘", "분할 다시 짜줘",
  "make me a program/routine/split", "redesign my routine". Runs
  service/health/program-plan -- ONE move per turn, every sentence and every
  number rendered by the tool -- and program-init writes
  files/program/program.yaml.
  (2) Update/revise: "프로그램 수정", "슬롯 바꿔줘", "세트 늘려줘",
  "종목 추가/교체", "add/drop/resize a slot" -- runs the volume-audit +
  set-increase suppression before any program.yaml change.
  (3) Deload/periodization: "디로드", "이번 주 좀 빼자", "주기화", "deload",
  "time for a lighter week" -- hybrid deload (planned N-week baseline + fatigue
  self-report early summon).
  (4) Placement/ordering consult: "종목 순서", "슬롯 배치", "동선", "순서 바꾸면
  어때", "프렙을 어디에 넣지", "왜 이 종목이 여기 있어", "why is this exercise
  here", "reorder the slots", "what order should I run these in" -- answered
  from the design-data files below (gym-layout.md 동선/홉 행렬 +
  program-history.json 근거), never improvised from prose.
  Owns ALL program.yaml STRUCTURE writes; when no program card exists, proposes
  lifts and hands off to a real free session (workout-session, session-open
  --free). Does NOT log workouts
  (session record = the kit's workout-log; sets = workout-session) or drive
  the live per-set session (workout-session).
---

# workout-program

Program DESIGN skill: program.yaml STRUCTURE writes (build / revise / volume audit /
deload), prep design, placement. Split from workout-log (2026-07-28, N1). NOT: session
record (kit workout-log, kit_life >=2.27.0), live drive + set logging (workout-session),
progression writes at set log (`set-add`, workout-session lane). Safety invariants of
this skill (F1 gate, focus-vs-injury, set-increase suppression) are delivered in the
files that execute them; the pack ships no AGENT.md to defer to (0.11.0).
Audit + coverage ledger: docs/skill-compaction/workout-program.md (pack repo).

## paths (cwd = PROJECT_ROOT, never cd into the skill dir)

- helper `database/kit_life.sh`; rx `service/health/rx-calc`; card
  `service/health/rx-card.py`; build `service/health/program-plan`; writer
  `service/health/program-init`.
- user data `files/program/`: `program.yaml` (slots), `prep.yaml` (prep SoT),
  `program-history.json` (why + changelog), `gym-layout.md` (zones), `stretch-matrix.md`
  (prep prose). templates `service/health/sot/` (pack-owned, read-only).
- consult spine = `reference/AGENT-CONSULT.md` (bare `AGENT-CONSULT.md` at instance root
  does not resolve: installer writes nothing there). G6 safety gate, calorie floor /
  ceiling and ledger one-writer live there ("G6 -- Safety gate", "Ledger one-writer +
  SoT"); counting = `.claude/skills/diet-status/calorie_gate.py`.

## hard rules

- YOU NEVER WRITE program.yaml. build = program-plan (moves) + program-init (write);
  revision = program-init `write --force` after the audit. no Write, no heredoc (D1/D2).
- `files/program/` file missing = not built yet, never "error". no install lane writes
  there; never copy a template as data. read reference/design-data.md when a file is
  missing or session-open printed `INSTALL-GAP` / `install=incomplete:N`.
- rotation position / next split / done this week: answer ONLY from
  `database/kit_life.sh rotation-current [monday]` (KEY=VALUE: week_monday /
  completed_this_week / cardio_this_week / last_split / next_split / remaining_this_week).
  no hook injects it (none ships in pack, kit or framework template) -- this rule is
  the only guard. never from memory.
- numbers never from the model: doses = program-plan RX_RULES, weights measured by the
  ramp-up, audit sentences = `program-plan volume-say` verbatim.
- every program.yaml / prep.yaml change is owner-approved; one decision question per
  message.
- practitioner heuristics (volume bands, rest model, micro-anchor, knee model) are
  ungraded: never "과학이 그렇다" / "연구가 이렇다".
- activation primers default OFF; ramp stays the warmup. Explicit preference = program.yaml `activation_primers`, optional
  `activation_drills` (global: pattern -> drill-list map; slot: 1-2 drills); slot overrides program. Keep user's recorded
  drills; caution prep replaces, not adds to, default menu. One light set before ramp, never between top rung and working
  set. Load alone never turns primers on. Never say drills prevent injury or wake an inactive muscle.
- never name internal machinery to the user (file names, stage ids, config keys,
  verdict tokens). before plainifying a word, tier it: read reference/speech-register.md
  when glossing, raising or lowering domain vocabulary.
- before asking the user about gear / venue / anything they own: read
  reference/resource-ask-gate.md (look up first; re-asking a known value is a defect).

## (1) build / redesign

1. goal consult (G0-G7), re-consult, module offer / cooldown, staging: read
   reference/AGENT-CONSULT.md before answering.
2. loop `service/health/program-plan next` -> speak -> `program-plan answer --stage <s>
   --json '<payload>'`. speak `readback` then `say` verbatim as one message; `choices` =
   buttons. never add a sentence, a confirmation, a closing question or a step preview;
   `done` asks nothing. read reference/build-flow.md for the move contract, card /
   split-option shapes and the stage map (first build turn, or when a move looks off).
3. `compose` move (no user message): read reference/compose.md. answer =
   accept the engine draft (`{"accept": true}`) or edit only within the
   move's shortlists, with a short Korean `why` per changed lift; no
   `candidates` / flat list, no titles.
4. `done` writes card + session_type rows + prep.yaml (when none) + calendar routines
   and renders the closing message. nothing else to save. program-init details: read
   reference/program-init.md when repairing, revising or reading an `E-*` / `W-*` line.

Compose is followed by swaps (confirm caution-site like-for-like changes),
then cardio, then sessions (all four session cards in one message), then
self-check and the closing message (asks nothing). The setup tail follows, never a dead
stop: diet target -> first session -> morning brief time -> daily retro time -> weekly
retro day/time -> short wrap. `done`'s `then` = the first tail question, sent as its own
message; one decision per message; resumable (`tail: open`). Detail: reference/build-flow.md.
The final app consent is available only with explicit pack config; it is off by default.

## (2) update / revise, (3) deload

read reference/program-edit.md BEFORE confirming any slot change or deload week: draft
in files/tmp, two-run audit (set-increase suppression), focus-vs-injury re-run, trim
priority, then `program-init write --force`. dose / set floor / rest / lattice / grip /
swap rules: read reference/program-rules.md when setting any slot field. compound
freeweight added or `W-G19-UNSET` printed: read reference/rir-floor.md.

## (4) placement / ordering consult

read reference/placement.md + `files/program/gym-layout.md` before any order answer;
"why is this here / why this weight / when changed": read `files/program/program-history.json`
first (reference/design-data.md). never improvise from prose or memory.

## other lanes

- no program.yaml + today's-workout / rx request: read reference/one-off-serving.md
  (proposal -> real free session via workout-session, session-open --free; per-set
  storage and progression stay on; one trailing offer).
- `session_class == "makeup"` / weekend extra session: read reference/makeup-session.md.
- pain-triage flag, recovery candidate, single pain event on a loaded joint, injury
  re-diagnosis: read reference/injury-adaptation.md (proposal only, POST_SESSION only).

## 분할 전환 (시작/복귀 4~6주) -- revisit point + the pack's declared offer moment (F12)

- full-body users (STRUCTURE NORM) revisit the split 4-6 weeks after start / return,
  via the weekly review's offer lane (offer bounds unchanged), never forced.
- same point = this pack's declared self-offer moment (owner 2026-09-18): install state
  is a READ, never a question. installed -> the pack says nothing about itself (incl.
  onboarding, see health-onboarding). not installed -> kit runs conservative generic
  programming; the honest moment to mention the pack is this split transition, never
  onboarding (month one is full-body, kit default loses little; the wall = split + set /
  weight lattice).
- single declaration home = this section; kit docs point here, never redefine.

## section index (names other docs cite -> file)

- 설치 완결, design-data ownership (프렙 / gym-layout / program-history) -> reference/design-data.md
- Question ledger / program-plan stage map, consult workout module setup detail -> reference/build-flow.md
- THE COMPOSE STEP -> reference/compose.md
- program.yaml generation, W5 calendar registration -> reference/program-init.md
- NO-CARD FREE SESSION (proposal -> real free session), decline / degradation -> reference/one-off-serving.md
- Volume-audit run procedure, Program-edit lane, 디로드 / 주기화 -> reference/program-edit.md
- 워킹 무게를 정하는 방식, 최소 세트 하한 정책, rest_sec, 바벨 마이크로-앵커, 템포/TUT, 셋업 참고자료, 그립, 기구 대체 시 슬롯 식별자 유지, rx-calc progression (F30), 과거 최고 기록 "예전에 데드 182까지" (`lift-peak`) -> reference/program-rules.md
- 복합 프리웨이트 RIR 하한 정책 (G19) -> reference/rir-floor.md
- 슬롯 우선순위, 분할 배치 원칙 (F31), 세션 페이즈 모델 -> reference/placement.md
- injury-driven program adaptation 라이프사이클, injury_knee 원칙, 부상 부위 x 워밍업 매트릭스 -> reference/injury-adaptation.md
- 도메인 화법 레지스터, 어휘 3층 -> reference/speech-register.md
- 자원 ASK-GATE -> reference/resource-ask-gate.md
- 주말 보충세션 규칙 -> reference/makeup-session.md
