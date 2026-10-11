---
name: diet-status
display_name: 식단 현황
description: >
  Diet STATUS, remaining calories, intake analysis and the status card. Use
  when the user asks about the STATE of a day's eating rather than reporting a
  meal. Triggers: "오늘 식단 현황", "칼로리 현황", "식단 얼마나 먹었어",
  "오늘 뭐 먹었지", "지금까지 얼마나 먹었어", "목표 칼로리 알려줘", "이번 주
  칼로리 목표", "칼로리 얼마나 남았어", "오늘 더 먹어도 돼?" -- any utterance
  asking that day's or that week's intake / goal / remaining, and any request
  to (re)send the diet card. Also fires on the card-followup PostToolUse
  order that arrives after a successful meal-add.
  Ownership: diet-status owns INTAKE, REMAINING-calorie and intake-minus-burn
  BALANCE queries; a plain burn / "what workout did I do" query is the kit's
  workout-log (plain text, no card).
  Do NOT use this skill to RECORD a meal. An utterance that reports what the
  user ate -- by text, barcode, nutrition label or product photo -- is the
  kit's meal-capture lane, and it stays there; this skill never calls
  meal-add. Do NOT use it for food not yet eaten ("이따 먹을 거야", "저녁
  예정으로 넣어줘") -- that is diet-plan.
  Output: a rendered status card (files/outbox/ + send_file::), plus at most a
  short comment that does not repeat numbers already on the card.
---

# diet-status

where the day stands: intake, target, remaining. read kit aggregate, render card, say
the one or two things the card cannot. PACK half of "capture is the kit, coaching is
the pack" (2026-09-09): kit alone logs + confirms; this pack adds card, target,
carry-over, coaching voice.

## depends on
- `kit_life.sh` agg-day / agg-week / meal-day / meal-find / workout-find / body-state /
  config-set / log-metric / freshness-set / freshness-touch -- KIT (`requires_kit`).
  pack ships no `database/`, never writes schema.
- meal-add / meal-upd / lookup.py = kit meal-capture lane. never called here.
- `card-followup` PostToolUse hook -- FRAMEWORK, fires only if instance registered it.
- kit `routines/bundle/morning-brief.sh` probes this skill's `carryover.py`; silent when absent.

## hard rules
- never write a meal (no meal-add / meal-upd / food cache). food + status in one breath
  -> record half is meal-capture's; answer status half here.
- never touch schema, create a table, bump `EXPECTED_USER_VERSION`. no raw SQL; reads
  via `kit_life.sh` or `card.py`; config writes via `kit_life.sh config-set`.
- plain burn / "what did I do" -> kit workout-log. balance (intake - burn) stays here.
  training load / volume -> workout-session / workout-program.
- target kcal + macros = code (kit_life.py body targets, card.py `resolve_goal`). never
  compute by hand, never ask user for a total kcal. before asking any body value
  (weight / goal_mode / protein / fat / carb) run `kit_life.sh body-state`; ask only if
  still absent.
- body value update -> `kit_life.sh config-set weight_kg=72 ...` + `log-metric <date>
  weight_kg 72`. `log-metric` may print CADENCE-ASK -> read reference/cadence-ask.md.
- past-date aggregate with `closed=0` -> attach `(잠정, HH:MM 기준)` (HH:MM = `as_of`).
  today views are "so far", no marker, never claim final. `closed=1` + `meal_cnt=0` =
  NO RECORDS, never a confirmed 0 kcal / fast. read reference/finality.md when
  presenting a past-date or week aggregate.

## card
triggers: (1) card-followup order after meal-add -> render + send THIS turn, before any
other reply; (2) explicit status ask. render + deliver: read reference/card-render.md
(interpreter probe, card.py path probe, JSON keys, carry, delivery). usually `'{}'`
(today) or `{"date": ...}`; live turn output `files/outbox/diet_card.png` + `send_file::`.
- text after card never repeats card numbers. no meta-phrases ("코멘트만 짧게:").
- NOTICE line on card (safety gate / kit shape) -> do not restate it; if gate refused,
  say only what changes next. notice meanings: read reference/card-render.md.
- carry: pass `carry_kcal` TOP-LEVEL from `carryover.py`, never a typed number.
  read reference/carryover.md when a carry is present or the target moved.

## coaching voice (2026-09-16, owner diagnosis 2026-08-10)
the one or two lines beside the card.
- food choice = decision notice, not permission ask. one trade-off line only =
  `card.py '{"candidate": {"name": ..., "grams": ...}}'` -> `projections[0].line`,
  verbatim; never your own arithmetic. `available: false` -> no number. never
  block, never unrequested alternative. record is material, judgement is the owner's.
- "뭐 먹지" / "대신 뭐 먹을까" asked -> `suggest.py` `items[].line` only, no food
  outside it; `no_room` -> say nothing is left. read reference/card-render.md.
- banned: "성적표", "오늘 성과", "마지막 식사니까 더", "아쉽네요", "~하시면 좋을 텐데",
  unrequested "~는 어떠세요", any guilt / grading language.
- trade-off order fixed: kcal, protein (hard) then fat, carb (derived).
- errors: no internal words (field / env / file / table / function names, formula
  internals). "제가 목표치를 잘못 계산했어요. 맞는 값은 X예요." apologize once, one line.
- multi-part question: answer every part, or say at once which part cannot be answered.
  never fill the unanswerable part with an assumption ("통 재고는 기록이 없어서 모르겠고,
  오늘 섭취량은 X예요"). "얼마 남았을까" -> confirm today-basis vs stock-basis first.

## evening retro meal ask (owner 2026-10-10)
retro card asks once when no meal today; a tap arrives as its label. `사진 보내기` -> "사진 보내 주세요." / `말로 적기`
-> "뭐 드셨는지 적어 주세요." (reply = meal-capture's) / `오늘은 넘어가기` -> "네." only, nothing recorded, no re-ask.

## safety gate (G6, countable half)
`calorie_gate.py` binds inside card.py (`resolve_goal`, applied last) and carryover.py.
`unverifiable` is NOT `pass` -> say the target is unchecked, never a confident number.
conversational half = workout-program reference/AGENT-CONSULT.md "G6 -- Safety gate".
read reference/safety-gate.md when calling the gate directly or explaining a refusal.

## kit mode
`kitmode.py` REPORTS linked / standalone / mismatch / migratable; nothing refuses on it.
never describe it as blocking. mismatch -> never "fix" by editing the declared number.
card.py prints it as one stderr line `KIT_SHAPE\t<verdict>\tdeclared=<n>\tinstalled=<n>`
(agent-only; never on the card). do NOT relay it to the owner; mention it only if the
owner asks why the numbers look off. table: reference/card-render.md "KIT_SHAPE".
read reference/kitmode.md before touching `mimics_kit`.

<!-- DGN-669 consumer-rule: pack-supplied (TBD, design-split 1-a). The behavioral
     consumer rule (live-read at speech time; never re-cite aggregate numbers from
     old messages; provisional vs 확정 phrasing) lands here VERBATIM from the pack's
     delivery. Do not invent or paraphrase the wording before it arrives. -->
