<!-- AGENT-CONSULT.md -- consult spine (cold: read when a consult / re-consult runs;
never hot-injected). no mint placeholders. ships at
.claude/skills-bundle/workout-program/reference/AGENT-CONSULT.md (activation copy under
.claude/skills/); a bare `AGENT-CONSULT.md` at instance root does not resolve (installer
writes no root slot, 2026-09-12). entry = health-onboarding (post-onboarding state,
2026-09-15) or a goal-shaped ask; no persona line routes here. interview machinery
(how to ask, ladder fill / promotion) = kit since kit_life 2.22.0 / pack 0.12.0; this
file keeps domain content. history + coverage ledger:
docs/skill-compaction/AGENT-CONSULT.md. -->

# AGENT-CONSULT -- goal interview + re-consult procedure

DGN-317 v2.4 consult spine: always-needed consult rules + section index. topic bodies =
sibling reference files; read each when its condition holds.

SAFETY -- ONE HOME, AND IT IS THIS FILE (0.11.0): the G6 gate ("G6 -- Safety gate") and
the write discipline ("Ledger one-writer + SoT") below. nothing else in the pack restates
them. calorie cap / floor numbers = kit rows, never text. history: reference/consult-g6-notes.md.

## section index

| topic | read | when |
|---|---|---|
| restart / resume batch confirm, question budget, record-first field list, consume-ahead classes, planning inputs (A1), resource wall (A6) | reference/consult-conduct.md | restart / redo / resume / full re-consult; before mining a field; budget audit; any plan / design branch |
| goal-setting entry, move loop + measurables walk, G0 consent slot, G1 follow-up, G2 strands + lift linking, G4, G5, staging + cascade | reference/consult-goal-part.md | goal part runs and a move looks off; bare goal-setting ask; legacy / adjust field; linking a lift |
| A8 profile assessment, G3 nutrition numbers, measure-first | reference/consult-phase-numbers.md | strand goal implies an energy phase; A8 inputs landed; calculator input missing |
| migration: digest, pre-ready, mis-seed, G0 lead, G1-pre | reference/consult-migration.md | `entry_path = migration` |
| modules: consult_modules states, offer bounds, 30-day workout cooldown, contract, idempotency + titles | reference/consult-modules.md | module trigger; before any module offer; consult_modules missing; creating a routine / measurement artifact |
| goal revision R1-R6, full re-consult, weekly-loop proposals | reference/consult-revision.md | consult_state=done and the user changes / redoes a goal |
| G6 open gaps + provenance | reference/consult-g6-notes.md | changing the gate; asked why it behaves so |

## Entry paths + state machine

`consult_state`: `pending_data -> digesting -> ready -> done` (migration) or
`ready -> done` (fresh, seeded at ready).
`entry_path = migration` iff ANY (priority order): (1) consult_state pending_data or
digesting; (2) `files/consult/digest-*.md` exists; (3) migration traces: migrated rows
predating this conversation OR config goal_mode / deficit_kcal / protein_g seeded without a
prior consult. else `fresh`. checked at pre-flight. migration -> reference/consult-migration.md.

`consult_offered` (decline latch, both paths): unset/0 = never declined; 1 = declined once,
one re-offer allowed; 2 = exhausted, fully passive. first decline -> config-set
consult_offered=1. re-offer at most once at a later natural opening (1/day, decision-free
reply, trailing line), and config-set consult_offered=2 in the same turn. at 2 the consult
opens only on a goal-shaped ask or menu pick. consult_state stays ready throughout.
(health-onboarding's `onboarding-gate declined` latch uses the same 0/1/2 ladder.)

## Global conduct rules

Pacing (A3, every consult + re-consult turn):
- one step per message. never preview future steps; the goal part is driven by the kit
  move loop, whose payload has no step counter or roadmap to speak (kit_life >= 2.28.0).
- shape: 1-2 lines context, this step's proposal, ONE question. cap ~4 short lines outside
  the proposal. max 1 decision ask per message.
- never re-explain a layer the user already confirmed.
- ONE TOPIC PER QUESTION: one interrogative elicits one topic; never fuse two (e.g.
  injuries + weak points). exemption (OQ-29, owner 2026-07-15): a multi-topic line that
  CONFIRMS already-captured data (the restart batch confirm). ELICITATION of an unknown
  stays single-topic, always.
- consume-ahead: pre-answered later step -> record per class (reference/consult-conduct.md),
  then fast-confirm in one line when its step arrives ("말씀하신 주5회로 갈게요. 맞죠?"),
  never re-ask. step ORDER unchanged.
- record-first fast-confirm (NORMATIVE, DGN-317 section 5): before ANY elicitation, mine
  own stores (records, ledger rows, config, files, prior confirmed answers). candidate found
  -> ONE-LINE fast-confirm, never an open ask; nothing found -> open ask as specced. field
  list: reference/consult-conduct.md.
  **CARVE-OUT -- INTENT IS NEVER MINED (owner 2026-08-27).** record-first = FACTS the owner
  would hate to repeat (venue, window, frequency, body stats, supplements, meals). NOT
  intent: direction (G2), thesis, any goal target -- a re-consult exists to change them;
  a mined fast-confirm hands back the answer the owner came to replace. intent ask is
  OPEN even with a prior value; prior value may be MENTIONED after the open answer lands
  ("직전에는 X 였습니다"), never before, never as a proposal.
- restart / resume / full re-consult: ONE batch fast-confirm of all captured answers
  first, never a full re-interview (reference/consult-conduct.md restart rule).
- question budget: typical <= ~7 / HARD CAP 11 decision questions; measurables walk is
  its own band (reference/consult-conduct.md).

Wording (A5): verb for closing a goal layer, ledger draft or revision = "확정"
("확정할게요", "확정됐습니다"). never say "잠금", "잠근다" or "lock" to the user; accept
"잠금" from the user as approval.

Vocabulary: never say "라더" / "ladder", stage ids, file names or config keys to the
user; speak plainly ("목표", "지금 단계", "다음 단계"). the ban reaches INTERNAL MACHINERY
words only (F1, owner 2026-09-18): domain words the user owns stay (분할 / 전신 /
후면사슬 / 데드리프트; "분할" -> "쪼갠다/갈래" was the over-application). tier any word
before plainifying: reference/speech-register.md.

Planning inputs (A1): plan = goal ladder + measured current state + resources /
constraints (the four ledger quadrants). plans cite the numbers and constraints they rest
on. "자원·취향은 안 물어요" holds for the GOAL INTERVIEW ONLY; any meal / workout PLAN or
DESIGN branch runs the resource pre-check (A6). detail: reference/consult-conduct.md.

Prohibitions:
- no as-is exit: never offer "keep everything and end the consult" before the walk is
  done; a no-change user gets the walk in fast-confirm mode. 지향 (direction) may not stay
  uncollected (program design consumes it); an unset long LAYER is normal (kit ladder).
- no teaser debt: findings promised by an offer or G0 are delivered, never a generic menu.
- migrated config numbers = mid-layer evidence only, never the purpose or opening agenda,
  never presented as current commitments without confirmation.

## Pre-flight (mandatory before first response)

READ config keys consult_state, consult_modules, goal_mode, deficit_kcal, protein_g, sex,
birth_year, height_cm, weight_kg, fat_mass_kg, lean_mass_kg, skeletal_muscle_kg,
avg_steps, other_neat_kcal (no body_fat_pct key; fat_ratio is a dietary macro ratio,
never body fat; user-stated body-fat % -> fat_mass_kg = weight_kg * pct/100).
There is NO `config-get` verb: `kit_life.sh config-get` fails with "알 수 없는 명령" (measured 2026-09-25).
read the set in ONE SELECT (no `-readonly`: on WAL it cannot open without a -shm file):

    sqlite3 database/kit_life.db "SELECT key, value FROM config WHERE key IN ('consult_state','consult_modules','consult_offered','goal_mode','deficit_kcal','protein_g','sex','birth_year','height_cm','weight_kg','fat_mass_kg','lean_mass_kg','skeletal_muscle_kg','avg_steps','other_neat_kcal');"

no row = unset. computed body / target state (goal_mode, weight, bmr / neat / deficit /
eff_goal, macros) = `database/kit_life.sh body-state` (KEY=VALUE); never recompute.
determine entry_path (above).

QUERY own stores for grounding (queries, not the path flag, decide what exists): recent
meals / workouts / metric_log + calendar / routine entries. verb shapes (kit_life 2.27.x):
`workout-find <YYYY-MM-DD>` and `meal-day <YYYY-MM-DD>` take ONE date (no range);
`agg-week <monday YYYY-MM-DD>` = a week; `trend <metric> [--window <N>] [--json]` takes a
BARE INTEGER: `--window 90`, never `--window 90일` (usage prints `<N일>`, parser is int()).
grounding feeds later confirms; it is NOT the opening line.

- self-heal (crash window, 2026-09-26): consult_state not done but the kit move loop
  already answers `wrap` -> do NOT re-enter the interview; run
  `service/health/program-plan next` (reads the wrap, writes consult_state=done, seeds
  consult_modules if absent, says nothing about the goals again).
- resume: proposed ledger_goal rows with source='interview' exist -> interrupted
  interview. ONE restart-rule batch fast-confirm, then re-enter at the first step whose
  output is missing. goal part needs no re-entry map: `goal-interview --next` recomputes
  from stored state. G6 re-runs on any resume (an injuries-none answer from the dead
  session left no row -> simply re-asked). newest staged row older than 7 days -> re-run
  the G1-pre snapshot confirm first (migration). batch-rejected item -> that step in full
  + reversal cascade.
- fresh: config health keys EMPTY is correct (the interview fills them). no digest; never
  mention one.

## Interview procedure -- spine steps G0-G7

the kit move loop runs G1-G5 and renders their words; inside a consult program-plan drives
it (`program-plan next` -> speak `readback` then `say` verbatim -> `program-plan answer
--stage <s>`; workout-program reference/build-flow.md). this file keeps domain content:
direction always collected (decides 종목/분할/순서), the G3 calculator numbers, the G6 gate,
the modules. body: reference/consult-goal-part.md.

G0 -- Opening (consent conditional; slot rules: reference/consult-goal-part.md).
- fresh: the move loop's first move is the opening -- the kit's intro + empty goal card +
  the G1 copy (no intent statement or roadmap line of your own).
- migration: lead with at most 2 staleness-verified digest findings
  (reference/consult-migration.md).
- Continuation entry (pack 0.17.2, owner 2026-09-25): consult opens from
  `health-onboarding` right after identity onboarding (inline in the identity close, or
  the next owner message via the fallback hook). consent slot = 0; G0 collapses to the
  goal consult's own first message (owner 2026-09-27) -- no transition line, no intent
  statement, no roadmap, no digest / records lead, no "지금 시작할까요?" gate. an
  explicit goal request ("목표 상담 시작하자") opens it the same way through goal-setting.
  shape owned by `health-onboarding` step 1 (CONTINUATION OPENING):
    [intro, i18n goal.opening.intro.health] + [empty goal card]
    then the G1 question + examples below, verbatim
  no easy-out line either (journey K8): "later" is never offered; a user who says it
  first is heard (`onboarding-gate declined`), never pushed.

G1 -- First goal question (ONE open question + 3 examples; owner ruling 2026-09-11).

  「목표하는 모습이나 운동 목표가 있으신가요?」

  예)
  • 보디빌더 같은 몸
  • 10km 마라톤 대회 완주하기
  • 주 4회 운동하기

  (examples BELOW the question: a `예)` line, then one `• ` line each, owner
  2026-09-26 18:58)
- no branch pick first: no why / how / what menu, no door list (owner 2026-09-11: 갈래를
  먼저 고르게 하지 않고 한 질문으로). three-door branch retired.
- NOT a button: plain text, no inline keyboard (버튼 아님, 답이 열린 자리).
- all three examples, this order, none added. a bare question without them ("어떤 목표
  잡고 싶으세요" class, or "pick a number of goals") stays banned (measure-first,
  owner 2026-08-18).
- counts 1 (G1 slot). no config numbers, no config card here. follow-up reading:
  reference/consult-goal-part.md.

G2 direction + strands, G4 habit, G5 order: kit move loop (reference/consult-goal-part.md).
G3 phase nutrition numbers: reference/consult-phase-numbers.md; every number clears G6
first.

Activation rule: every proposed ledger row needs explicit user approval; proposed rows
never activate automatically. [SAFETY: activation invariant, restated in "Ledger
one-writer + SoT".]

G7 -- the kit wrap IS the end of the goal part (2026-09-26, gap E11 / H4). no second
summary, no second approval ("네/확인" again was the rehearsal's double confirm).
- measurables gate: kit `goal-interview <goal_id>` stays the gate the wrap and
  `goal-rebuild-commit` read. activation = the kit's.
- nutrition constraint rows + config mirror: written right after the move that confirmed
  them (measure-first: when the measurement lands), not re-approved here.
- consult_state=done + consult_modules seeding: `program-plan next` on reading the wrap
  (idempotent; existing consult_modules never overwritten).
- ONE message (journey A2): the kit's readback (filled goal card) + its `say` (wrap line
  + the transition line "다음은 운동 프로그램 상담으로 넘어갈게요. ..."), a blank line, then
  program-plan's FIRST program question -- the weekly count and the minutes a day (횟수: three count options, one
  recommended, and the recommended minutes; the 운동일시 follows it, naming the count), or the place when none is on
  record, or -- when the goal part recorded a gym -- the gym's name with 장소: 헬스장
  on the program card (shape: reference/build-flow.md). otherwise no program card on
  it (it opens from the next message), no offer question; never announce what will
  not be asked.

### G6 -- Safety gate

one home (0.11.0). the only step NEVER skipped: full run on every entry / resume /
restart. precedes the workout module; its injuries answer also feeds program design
(program-plan compose, marked in the sessions list).
NO THRESHOLD IS WRITTEN IN THIS FILE: the gate reads kit `ledger_constraint` rows
`max_deficit_cap` and `calorie_floor` (`inviolable=1`, `goal_id IS NULL`, delivered to the
consult frame unconditionally). read the row, never a typed number.

G6-a -- injuries / limitations (unskippable). carrier = the kit move loop's `ask_safety`
(journey G4: before the order decision and any number; program-plan passes it through
and reads the answer at the wrap). a kit without it: program-plan's own `safety` move
stands in, ahead of any kit number move. ONE question either way, before any number and
before the program's first dose. speak the tool's sentence verbatim:
  "목표 수치(체지방 몇 %까지 같은)를 제안드리기 전에 하나만 확인할게요. 상태에 따라 목표와 속도를 맞춰야 해서요. 아프거나 조심해야 하는 부위가 있으세요?"
- standing safety row -> tool reads it back, never an open re-ask; the gate still runs:
  ("조심할 부위로 ...이 적혀 있어요. 지금도 그대로인가요?")
- record: the kit move's choice `cmd` (+ `on_site` per new site), or `program-plan answer
  --stage safety` for the pack's own move (same kit verbs). never INSERT by hand.
- skipping is not available on any path (resume, restart, batch confirm that covered the
  safety set -> injuries SLOT counts 0, gate still runs in full).

G6-b -- the countable limbs. RUN THE GATE, DO NOT RECITE IT:

    python3 .claude/skills/diet-status/calorie_gate.py \
        --deficit <N> --base-target <N> --bmr <N> [--sex male|female] \
        [--weekly-freq <N>] [--per-session-burn <N>]

(skill not switched on -> `.claude/skills-bundle/diet-status/calorie_gate.py`.) exit 0 pass
· 1 refuse · 2 unverifiable. limbs cap / bmr_floor / sex_floor + no-history branch:
diet-status reference/safety-gate.md. obligations:
- pass -> proceed (stage the numbers).
- refuse (cap) -> the deficit is NOT confirmed at the asked value; no override, none
  offered. present the refracted number as the proposal, one line that the cap moved it.
- refuse (either floor) -> HOIST the target to what the gate permits, one line:
  "이 체구에서 이 밑으로는 권하지 않아요. X kcal로 잡을게요" (X = the tool's `refract_to`,
  never estimated; the tool's `why_line=` carries the same sentence). owner insists on a
  sub-floor number: REFUSE, recommend medically supervised care in one line, no guilt
  framing.
- unverifiable (row missing, DB unreadable, input never collected, or no
  `calorie_gate.py`) -> NOT a pass, never spoken as one: say the safety check could not
  run and what is missing; do not 확정 a calorie number that turn. reachable on a fresh
  instance (nothing in kit_life plants the two `source='seed'` rows).

G6-c -- not gate inputs / routed through it.
- segmental InBody + focus areas = DESIGN inputs; never enter or soften the cap / floor.
- calorie verdict = EFFECTIVE target, base + that day's burn (`kit_life.sh targets --burn
  <kcal>`); never present the base deficit alone as "the goal" (A9).
- overtraining frequency routes THROUGH this gate: cadence above 7 sessions/week or 2+ in
  a day does not pass on the short-layer backstop.

### Ledger one-writer + SoT

- ONE WRITER for ACTIVE rows: main session, on explicit user approval, nothing else.
  sanctioned exception: PROPOSED staging (migration-digest + interview rows); proposed
  rows never activate automatically.
- WRITE PATH: every write through the kit's ledger verbs. cap-exceeding value refused
  there, no `--override`; the floor is prompt-side (G6-b) -> G6-b runs BEFORE a number is
  confirmed.
- WRITE ORDER: ledger first, then the config mirror, immediately, no user-facing utterance
  between (a turn ending in between leaves the mirror stale).
- SoT on divergence: config vs active `ledger_constraint` rows disagree -> THE LEDGER WINS:
  config-set to match + one `ledger_audit` row recording the repair. measure-first window
  (zero active rows, numbers 미정) is NOT a divergence.

## Domain modules

workout / diet / supp modules, consult_modules states, offer bounds, 30-day workout
cooldown, idempotency + title convention: reference/consult-modules.md. modules run only
after consult_state=done. F1 gate, focus-vs-injury check and volume-audit binding live
where they execute (reference/one-off-serving.md, reference/program-edit.md).

## Goal revision (re-consult)

consult_state=done + a change / redo ask: reference/consult-revision.md. consult_state
never changes during a re-consult; G6 runs whenever the mid layer's numbers or phase
change.
