# card render + delivery (read before rendering the card; diet-plan uses this too)

## the snippet
```bash
RENDER_PY="${RENDER_PYTHON:-}"
[ -z "$RENDER_PY" ] && [ -x "$HOME/dogany/.venvs/render/bin/python" ] && RENDER_PY="$HOME/dogany/.venvs/render/bin/python"
[ -z "$RENDER_PY" ] && command -v python3 >/dev/null && python3 -c 'import matplotlib' 2>/dev/null && RENDER_PY="$(command -v python3)"
[ -z "$RENDER_PY" ] && RENDER_PY="python3"   # last fallback; card.py exits 3 if no matplotlib

# activation path first, bundle path second (installer always lands the bundle)
CARD=""
for c in .claude/skills/diet-status/card.py .claude/skills-bundle/diet-status/card.py; do
  [ -f "$c" ] && CARD="$c" && break
done
[ -z "$CARD" ] && { echo "diet-status card.py not found -- pack_health is half-installed"; exit 3; }

# live turn (direct reply)
OUT=$("$RENDER_PY" "$CARD" '{"output":"files/outbox/diet_card.png"}')   # then send_file:: "$OUT"
# cron / routine (bot direct-send)
OUT=$("$RENDER_PY" "$CARD" '{}'); routines/push.sh --photo "$OUT"
```
- default output `/tmp/diet_card.png` is outside PROJECT_ROOT, so `send_file::` cannot
  send it on a live turn. live turn -> `files/outbox/`. push.sh can send /tmp.
- exit 3 = matplotlib missing (graceful skip). answer text-only; tell the user plainly
  the card image could not be drawn this time, e.g. "카드 이미지는 지금 못 그려서 글로
  알려드릴게요." no library / file names in that line.
- fonts: bundled `fonts/ASDGN_*.ttf` first, then system TTC (`DIET_CARD_TTC` env or
  defaults), then matplotlib default (CJK may break, warning only).

## JSON input (all keys optional; passed keys override the kit_life.db auto-aggregate)
```json
{"date": "2026-06-25", "output": "files/outbox/diet_card.png"}
```
- `date`: YYYY-MM-DD (omit = today KST). header shows "YYYY.MM.DD 요일".
- card auto-loads that date's meals + workouts from kit_life.db ONLY when both `meals`
  and `intake_kcal` are absent.
- `meals[].kcal/carbs/sugar/protein/fat` optional -> the row's table cells (메뉴 | kcal |
  탄수 | 당류 | 단백 | 지방); long names are cut with … before the kcal column. a workout
  row shows its burn as a minus, dashes elsewhere.
- `meals[].sugar` / `carbs.sugar` optional; auto-aggregate fills from meals.sugar.
- net carb: OPT-IN, default total carbs. owner turns it on with `kit_life.sh config-set
  diet_net_carb=1`; the card then shows 순탄수 (carb - fiber) in the header, the column
  and the macro bar. kcal NEVER changes with it: the kit's kcal is already net of fiber
  (generated). on but fiber unreadable -> total, never a half-net column. `net_carb`
  in the JSON overrides the config for one render.
- colours: framework >= 2.6.0 -> `card_palette()` (light, agent accent from
  config/agent.conf AGENT_ACCENT); older framework -> the legacy dark card. both are
  normal; never mention the palette to the owner.
- `burn_kcal` omitted -> no burn label, no exercise segment. present -> intake bar
  splits [base + activity - deficit] + [exercise bonus].
- `carry_kcal`: TOP-LEVEL, from `carryover.py`, never typed. omit / 0 -> card unchanged.
  present -> target drops, formula line gains `- 이월 N`, bar + macro goals follow.
  nesting it under `intake_kcal` suppresses the meal auto-load -> empty card.
- rows whose name ends ` (예정)` (diet-plan) render dimmed in row text, intake bar,
  macro bars.

manual check: `kit_life.sh agg-day <date>` (intake / macros / burn / balance),
`meal-day <date>`, `workout-find <date>`.

## NOTICE band (card foot, warn colour, grows downward only)
| notice starts with | producer | means |
|---|---|---|
| `안전 게이트: ...` | calorie_gate refused | target shown was hoisted to what the inviolable rows permit |
| `안전 하한/상한을 확인 못 했습니다 (...)` | gate `unverifiable` | rows unreadable; target UNCHECKED, not safe |
| `안전 게이트 미탑재` / `안전 게이트 실행 실패` | carrier missing / raised | same as unverifiable |
| `킷 모양 불일치: 선언 N != 설치 M` | kitmode mismatch | card tables are a shape the pack has not verified |
| `킷 모양 미선언` | kitmode undeclared | `mimics_kit` missing from product.yaml |
| `킷 모양 확인 실패` | kitmode raised | shape check produced no verdict |
no notices = every check ran and cleared. never restate a notice in chat.

## trade-off line + "뭐 먹지" (engine numbers; the model does no arithmetic)
both run on any python3 (no matplotlib), on the card's own target (carry, burn, G6 floor).
```bash
# trade-off for a food the owner is weighing -> projections[0].line, spoken verbatim
python3 "$CARD" '{"candidate": {"name": "목살", "grams": 220}}'
# "뭐 먹을까" -> items[].line, the only foods that may be named
python3 "$(dirname "$CARD")/suggest.py" [--carry-kcal N]
```
- candidate: `{name, grams}` or numbers already looked up this turn (`kcal`, `protein`,
  `fat`, `carbs`). resolved: given > kit food cache (scaled to grams) > owner's own logged
  serving. `available: false` -> no trade-off number; never estimate one.
- projection = `kcal_after`, `protein_after`, `over_kcal` (+ fat/carbs_after). `line` =
  kcal then protein, "참고로 ... 넘어요" only when `over_kcal` > 0.
- shortlist = owner's logged foods (last 60 days), typical serving must fit what is left,
  ranked by fit (protein owed first, then how often logged). speak `items[].line`, at
  most the list; no food outside it. `status`: `no_room` (nothing left -> say so, no
  list), `no_history`, `nothing_fits` (`excluded_over` = how many were too big).
- only when asked ("뭐 먹지", "대신 뭐 먹을까"); never an unrequested alternative.
- pass the same `carry_kcal` the card got (`--carry-kcal`), or the numbers disagree.
