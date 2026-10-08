# consult goal part -- G0 consent, G1 follow-up, G2 strands, G4, G5, measurables walk

read when: the goal part (G0-G5) runs and a move looks off, a bare goal-setting ask
arrives, a legacy / adjust row returns a field, or a lift must be linked to a strand.
the kit move loop renders every user-facing line of G1-G5; this file adds no wording
for it. ladder mechanics (fill order, rung count, promotion) = kit (life-onboarding /
goal-interview), never restated here; any older fill-order line loses to the kit.

## goal-setting entry (bare "목표설정 다시 하자" outside a consult)

- not routed through the G-spine. entry = kit `goal-setting` SKILL (kit_life,
  `requires_kit`; pack stopped shipping it at 0.10.0). resolve activation-first:
  `.claude/skills/goal-setting/SKILL.md`, then `.claude/skills-bundle/goal-setting/SKILL.md`.
  neither -> kit absent or older than the manifest requires / skill not installed: say
  so, stop. never improvise a scope menu, never reimplement the interview.
- reinforcement: this pack's UserPromptSubmit hook `routines/bundle/goal-entry-gate.py`
  (manifest hooks[]) puts this entry rule in context on a goal-setting phrase outside a
  live consult. it guarantees the instruction is present, not that it is obeyed.
- scars 2026-08-23 / 2026-08-24 (improvised scope menu; blank-recall "새 목표,
  어떤 것부터 잡고 싶으세요?"): the SKILL decides WHICH structural operation (rebuild /
  adjust / add); G1 decides HOW to ask for content once "add" or a fresh consult needs it.
  neither substitutes for the other; neither is replaced by an improvised open ask.
- `--domain health` ALWAYS explicit (omitted -> `uncovered_axes` across ALL domains;
  2026-08-24 spending axis leak).

      database/kit_life.sh goal-interview --start --domain health
      database/kit_life.sh goal-interview --start --scope rebuild|adjust|add

  `--start` asks ONE question first: rebuild / adjust / add a missing axis. never a
  self-written scope menu (built from what exists, cannot contain what is missing; tool
  computes `uncovered_axes`). `--revise <field>` re-opens one filled field (adjust
  branch), one question per turn.

## move loop + measurables walk (kit_life >= 2.28.0)

    database/kit_life.sh goal-interview --next --domain health --json   # --stage in a rebuild

one move per turn (journey G1-G8, the kit's GOAL_JOURNEY): direction -> user's own
strands (axis-add) -> what they do now (calendar + records lead) -> how long -> the
safety re-check -> ORDER for strands that pull apart (the held lines + the measuring
cadence are written by that answer and stated, never asked) -> pace, three options ->
practice, three options -> wrap. speak `readback` then `say` verbatim, run the command
the move names. per-kind table = the kit goal-setting skill's moves table.
every `choices[].cmd` (and any other argv a kit move carries) is a KIT verb: run it as
`database/kit_life.sh <argv...>` -- the move names its runner in `cmd_runner`
(`database/kit_life.sh`, kit_life with the per-strand practice menus). never
`service/health/<verb>`: the pack has no goal-move-note (live 2026-09-28).
practice picks the program acts on (compose.md "goal practice picks"): functional set
`power` / `mixed_circuit` / `conditioning` (legacy `unilateral` / `core` still compose),
connection set `breath_trunk` / `mobility_flow` / `whole_body` -- every pick recorded on
the card changes the sessions. silent `strand_picture` (kit >= f5af846): the strand's
first move waits for its picture -- write one in the owner's words (noun form, <= 30자)
via the move's `on_proceed` (`goal-move-note --picture`), never its `<...>` hint. inside a consult,
program-plan drives it (`program-plan next` passes kit moves through; the wrap ends on
the program's first question, workout-program reference/build-flow.md).

measurables per staged layer: domain, metric, baseline_value + baseline_as_of,
target_value + target_dir, horizon_date, owning_agent. title = human prose; columns =
machine version the weekly review compares against (prose title + NULL columns = the
defect this exists to prevent).
- per-goal walk `database/kit_life.sh goal-interview <goal_id>` = the GATE, not the
  script: `goal-rebuild-commit` and the G7 measurables gate read its `done`. a move-loop
  `on_yes` row is already complete. walk returns a field (legacy row, adjust) -> one field
  per turn; one confirmed proposal fills several fields in ONE `goal-set`.
- `ask_kind=confirm`: a record answers it (`inferred.value` + `inferred.as_of` + source
  table). put it as a correctable confirm; inferred baseline written only once accepted.
- NEVER INVENT A MEASURABLE. `ask_kind=open_nullable` = no record; "모름" is first-class:
  stores NULL, rung_state='baseline_declined', not re-asked. [SAFETY: A9 no-invention --
  consult safety invariant; fabricated baseline = weekly review reports progress against
  a number nobody measured.]
- unset fields VISIBLE: rung_state (target_proposed / baseline_pending /
  baseline_declined / tracking); weekly review 목표 진행 prints the gap ("목표 시점 미설정").
  NULL is acceptable; hiding NULL is not.

## G0 consent slot (DGN-317 2.3)

- user ASKED for the consult or ACCEPTED an explicit offer -> consent slot 0; G0 ends
  with G1 directly.
- slot 1 (ask consent) whenever the opening is NOT an explicit ask: agent-opened at a
  natural opening, decline-latch re-offer uptake ambiguity, menu-adjacent openings,
  fresh triggers that only IMPLY interest (self-intro, vague "what should I do first").
  standard MINT opening (agent self-intro -> user self-intro / vague help) = consent-firing.
- continuation entry (health-onboarding) = slot 0: reference/AGENT-CONSULT.md G0.
- migration lead: reference/consult-migration.md.

## G1 follow-up (why / how / what = how you READ the answer, not what you ask first)

place the answer on the layer it came in on; follow up from there, one question per turn:
  - what (form / look, e.g. "보디빌더 같은 몸") -> G2 strands from the user's own words.
  - how (activity / method, e.g. "10km 마라톤 대회 완주하기", "주 4회
    운동하기") -> take the activity or cadence as given; ask only what G2/G3 need next
    (event date, current level, available days).
  - why (purpose: health, rehab, a deadline) -> accept as anchor, continue to G2; never
    demand a form or number up front.
  - "모르겠어요" / no goal yet -> offer the examples once more in plain words, proceed from
    what the user reacts to; never re-ask the bare question.
- clear stated goal on arrival -> take it, skip the question, proceed within G2.
- harmful route (drugs / injections, extreme cut) -> persona safety boundary: do not
  recommend, dissuade once.
- why stays emergent: no immediate why-ask after any answer; later steps climb toward
  why from what the user volunteers (owner-confirmed 2026-08-21 bottom-up).
- record-first here too: a number history carries (lift weight, weekly count, lift
  names) -> confirm, never cold ask ("최근
  40일 기록 보니 데드리프트 <기록중량>kg, 백스쿼트 <기록중량>kg 찍으셨던데 이걸 기준으로
  잡을까요?" class).
- scope wall: WORKOUT-domain goal entry only; never enumerate / offer other-domain axes
  (spending, relationships) -- `--domain` scoping is the tool's concern.

## G2 -- direction + the user's own strands (owner rulings 2026-09-26)

- direction = the G1 answer verbatim + short name (`why-add`); no deadline, no number, no
  long-layer goal row.
- strands derived from THAT answer, user's words, by `axis-add` (one `--axis` per named
  strand; `=<metric>` only where a registered metric measures it). nothing pre-seeded;
  one named strand = one strand. readback comes from the verb.
- strand with no metric = carried as a direction; no proxy number.
- extreme / harmful route -> refract toward a safe range, never reject. [SAFETY:
  extreme-goal refraction -- consult safety invariant.]
- LINKING A LIFT: needs a `goal_metric_source` row (`source_table='workout_sets'`,
  `source_expr=<exercise_name>`) before `axis-add` can link it; no code edit. pack
  constraint: only a LEAD-COMPOUND lift (program slot 1) accumulates top-set history an
  e1RM reads off; an accessory lift's value stays thin.
- A8 profile assessment runs once its inputs exist: reference/consult-phase-numbers.md.

## G4 -- habit goal, when the direction names one

not mandatory: move loop picks the current phase from direction + records (returner
rebuilding consistency may start with a habit). habit = a strand linked to
`weekly_sessions`; move loop reads demonstrated cadence off `workouts` as readback and,
with no pace cargo, asks the number. cadence goal has no deadline by design ("주 N회 유지").

## G5 -- order before numbers (former tradeoff question)

strands that pull against each other (deficit vs surplus) get the move loop's
`order_choice` BEFORE any number: three options, a recommendation from the dated record,
one pick (`axis-order`) -> `metric_axis.phase_order`; the later strand is named in the
wrap as next phase. `program-rebalance` reads the order pick first
(`db:phase_order:<strands>`; no pull-apart pair -> strands with an active goal,
`db:active_goal:<strands>`); legacy `detail.tradeoff_priority` = fallback for old installs.

## interview staging + reversal cascade (A2)

layer confirmed -> ledger_goal row status='proposed', source='interview' (replaces an
earlier interview-proposed row for that layer; source='migration-digest' rows untouched
until G7). activation only on explicit approval. user revises a confirmed staged layer
mid-interview (incl. rejecting a batch-confirm item) -> replace that row AND
re-propose / re-confirm each dependent lower layer before advancing. move-loop rows are
written by the kit (a rebuild stages, `goal-rebuild-commit` activates).
