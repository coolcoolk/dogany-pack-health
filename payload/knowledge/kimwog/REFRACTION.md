# Refraction engine (DGN-172) -- deterministic applicability refraction

This is the DGN-119 candidate-A engine: it turns a general knowledge item into a
statement about THIS user, deterministically. The spine is a hard split:

- DETERMINISM lives in code (`tools/refract.py`). Axis resolution, the three ops,
  the Need computation, budget gating -- all pure functions over data.
- JUDGEMENT lives in the model (the answer path, DGN-175): phrasing, whether to
  ask, tier selection. The model NEVER computes a number. Every number in a
  refraction result is copied from item data or produced by RESCALE (pure
  arithmetic on item data x a resolved axis value).

## Placement (framework side vs instance side)

| Component | File | Side | Why |
|---|---|---|---|
| Refraction engine + axes ledger view | `tools/refract.py` | framework/warehouse | deterministic logic + axis-name ledger are pack-shipped, user-independent |
| Axes ledger (canonical names + tiering) | `axes.yaml` | framework/warehouse | append-only, framework-owned (DGN-119 governance) |
| Lifekit adapter interface + fixtures | `tools/refract.py` (`LifekitAdapter`) | framework | the contract is framework; DGN-174 wires the real db |
| Stated axis store + Need dedup ledger | `instance/tools/profile_axes.py` | instance | user-owned conversational facts (DGN-120) |
| Question budget checker + daily state | `instance/tools/budget.py` | instance | per-user ask counts are user-owned state |
| refraction-log.jsonl writer | `instance/tools/refraction_log.py` | instance | user-owned interaction history (C-track material) |

The rule of thumb: NAMES and LOGIC are framework (shipped with the pack);
VALUES and COUNTS are instance (user-owned, survive pack removal, DGN-120).

## Axis resolution precedence

`measured (kit_life.db) > stated (profile_axes)`. For a ledger axis marked
`source: kit_life`, `refract.resolve_axis` asks the `LifekitAdapter` first and
only falls back to a stated `profile_axes` value if the adapter has none. Prose
memory is never machine-parsed here (if injected, the main agent confirms then
calls `profile_axes.set_axis`).

## The three ops (exactly three, DGN-119)

- RESCALE -- `role: scale` numeric axis carrying a `rescale: {per_unit_low,
  per_unit_high}` on its item entry. The ONLY op that produces a new number, by
  multiplying the per-unit range by the user's measured/stated value.
- REFRAME -- `role: soft` axis with a curated `refraction_notes` entry naming it
  (`axis:`). Keeps the number, attaches the graded hedge note. No note -> the
  present value simply stands.
- EXCLUDE_SWAP -- `role: hard` axis whose value is not in its `gate: {allowed}`
  set -> withdraw/route around the specific claim.

## block_specifics (safety gate)

A safety axis (ledger `safety: true`) with `unknown_policy: block_specifics`
that is unknown or refused sets `result.block_specifics = True` and lists the
axis in `blocked_axes`. The answer path then withholds specific numbers and any
green-light while still giving general info + mechanism -- NOT silence. The Need
is still recorded with the axis's data-sourced `baseline_text`.

## Need protocol (answer-first)

A missing axis never blocks the answer. `result.needed_missing` lists each
missing axis with its `baseline_text` (data, from the ledger -- e.g. a Korean
"trained young male baseline" lives there as data, never hardcoded in code) and
a `reask_ok` flag. The answer path speaks the stated-baseline answer FIRST, then
may ask per the budget. Dedup: a REFUSED axis is never re-asked; a stable axis
is asked at most once; a volatile axis is re-askable only after `max_age_days`.

## Lifekit adapter contract (DGN-174 wires the real db)

`refract.LifekitAdapter.get(axis_name, now) -> AxisValue | None`.

- Returns the most recent MEASURED value with `.measured_at` (ISO date), or None
  if the source has no measurement for that axis.
- `now` is passed IN for determinism; the adapter must not read an ambient clock
  and must never fabricate or DERIVE a value (scaling is refract's RESCALE).
- Answers ONLY `source: kit_life` axes; stated axes are never routed here.

Fixtures shipped for tests: `DictLifekitAdapter` (in-memory) and
`SqliteLifekitAdapter` (over a `metric_log`-shaped sqlite db -- used against the
sandbox FIXTURE db ONLY). DGN-174 replaces `SqliteLifekitAdapter` with an
adapter that goes through the official `database/kit_life.py` accessors (mapping
ledger axis names -> kit_life metrics/aggregates), never raw SQL, never a live db
from this sandbox.

## M-2 protocol line (parametric bypass guard)

Grades and personalized numbers speak ONLY via the skill path (F3 extension).
The frontmatter `grade:` field is the machine record the skill reads; a letter
grade baked into an item's human PROSE body would leak a grade outside the skill
path. The warehouse lint enforces this: `check_m2_grade_leak` errors on a bare
letter-grade token (`grade A`, `A-grade`, Korean `A<geup>`) in an item body.

## Question budget (three tiers)

`budget.decide(instance_root, tier, needed_missing, today, flow_ok, consent_given,
commit)` -> `BudgetDecision`.

- casual: answer first + at most 1 question; a DAILY BACKSTOP (1/day) applies
  here only (state in `ask-budget.yaml`, resets on a new day).
- engaged: 2-3, on user signal or accepted invitation (no daily backstop).
- assessment: `consent_required` until `consent_given=True`, then most of the
  Need set in one session (consent + disclosure IS the gate).
- flow-respect: `flow_ok=False` skips all asking, fall back to baseline answers.

This is a budget gate only -- it holds NO conversation logic. The answer path
(DGN-175) picks the tier from conversational signal and does the phrasing.

## refraction-log.jsonl seam (write-only)

`refraction_log.append(instance_root, result, budget_decision, ts, extra)`
appends one JSON line per refract call: `ts` (passed IN by the caller), item id,
ops (op + axis), block-specifics, axes used/missing, budget decision. NO
consumer is built (the DGN-119 C-track mirror reads it later).

## What the sibling tickets consume

- DGN-173 (seed conversion): authors real items with `applicability.axes`
  (+ `rescale`/`gate` where they personalize), against these canonical axis
  names. The lint keeps the ledger discipline green.
- DGN-174 (main-agent migration): implements the real `LifekitAdapter` over kit_life.db
  per the contract above; decides the kit_life read boundary (shared-read vs
  synced vs API-through-the-main-agent).
- DGN-175 (answer path): calls `refract.refract`, speaks the result (answer-first
  on Need), calls `budget.decide` for asking, calls `refraction_log.append` with
  the turn timestamp, and records the touched-set (DGN-171 `touched.record`).

## Tests

```
sh tests/run.sh     # refraction stack + lint-negative + both DGN-170/171 lints
```
