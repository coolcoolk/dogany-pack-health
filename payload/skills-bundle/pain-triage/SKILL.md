---
name: pain-triage
display_name: 통증·자세 진단
description: >
  Handles in-session pain / form-fault triage AND its follow-up + records + program review.
  (1) In-session log+triage: fires when 사용자 reports pain or discomfort DURING a set --
  "아파", "여기 아파", "무릎 아파", "시큰해", "어깨 결려", "따끔", "아까 그 무게에서 아팠어",
  "hurts here", "knee tweaked", "shoulder pinch". Do a FAST triage (minimal questions,
  immediate action: drop load / substitute / stop), log the event, keep the session moving.
  (2) Post-session follow-up: after the workout, raise any pain events from that day and
  discuss them properly (mechanism, fault pattern, guardrail: cue/tempo/load-cap/substitute/
  primer isometric), then close each event. (3) Query / status: "요즘 어디 자주 아파",
  "무릎 통증 기록", "통증 패턴 봐줘", "자세 진단 기록", "이 종목 아팠던 적", "프로그램 점검해줘",
  "pain history", "where do I keep hurting" -- read the time-series and report patterns.
  (4) Program review: when the same movement keeps hurting the same way, flag the actual
  workout program for a change (substitute / load cap / tempo) via the safety ledger.
  Records each event into an independent local store (pain_events.db). NOT medical
  diagnosis -- form/mechanics triage + coaching guardrails only; escalate to a doctor
  if pain persists or worsens.
---

# pain-triage

coaching triage for pain + bad-form events. fast fix in-session, deep talk after,
time-series so repeats get seen, program review when a movement keeps hurting.
NOT medical diagnosis.

## paths
resolve once from PROJECT_ROOT (never cd into skill dir):
```bash
for c in .claude/skills/pain-triage/pain.py .claude/skills-bundle/pain-triage/pain.py; do
  [ -f "$c" ] && PAIN="$c" && break
done
```
`pain.py <verb>` below = `python3 "$PAIN" <verb>`. all writes via pain.py verbs, never raw SQL.
verb args, store layout, audit flag lines -> read reference/pain-cli.md when composing a
pain.py call beyond `add --exercise --pain` or reading audit output.

## hard safety line
- no medical verdict. never name tear / tendinopathy / any diagnosis.
- speak mechanics + coaching only: cue / tempo / load-cap / substitute / primer.
- sharp, swelling, persists across sessions, or rising trend -> say so plainly,
  recommend doctor / physio, stop coaching that movement. never push through.
- injury ledger (per-joint ROM caps, pain swap threshold, per-side bans) = INSTANCE
  DATA. read it, never assume entries, never advise past its limits.
- never auto-change program or safety ledger. propose -> explicit approval -> main
  session applies (one-writer rule).

## when + tier
- pain mid-set -> phase 1. BEST-EFFORT (description auto-fire).
- session end AND open events -> phase 2. MUST-HAPPEN: carrier = workout-session
  session-end step (runs `pain.py recent` before the wrap). prose-only, no hook yet.
  never defer to another day.
- history / pattern / program-review ask -> phase 3.
- audit FLAG -> phase 4.

## body signals (stiff / tight / sore, NOT pain)
"햄스 뻣뻣", "허벅지 당겨", "어깨 뻐근해" -> one call records + renders:
```bash
service/health/fatigue-brief signal --site <muscle node> --sensation stiff|tight|sore \
    [--side L|R|both] [--exercise <slot name, mid-session only>]
```
- site = muscle node token (hamstrings, quads, glutes, back_lats ...). no muscle named
  ("다리가 뻐근") -> group token (legs). joint word (knee) ok, kept as user's word.
- say stdout verbatim. ask nothing.
- exit 4 + `ROUTE pain-triage` = it was pain -> phase 1.

## phase 1 -- in-session (FAST)
1. ask only what is missing, 1-2 questions max: exercise? where + side? pain 0-10?
2. act now:
   - pain >= ledger swap threshold for that joint, or form broke -> drop load, or
     ledger's declared substitute, or stop the movement. ONE form cue.
   - ledger has no threshold -> any reported pain = stop-and-ask. never invent one.
   - low + clean -> one cue, continue, watch next set.
3. log now: `pain.py add --exercise <slot> --pain <0-10> [...]`.
   `--exercise` = program.yaml slot name (English snake_case), never Korean display
   name. audit groups by exact string; mixed names split one lift into two groups (F34).
   non-slot report -> stable English key (e.g. `pre-session-checkin_<area>`).
4. keep session moving. diagnosis waits for phase 2.

## phase 2 -- post-session (DEEP)
1. `pain.py recent` -> open events (all days; `--days 1` = today only).
2. per event, talk it through: movement, position that broke, how joint loaded wrong
   (cave / forward / shift / twist), side.
3. set guardrail grounded in ledger: entry cue + tempo (slow eccentric) + load cap +
   substitute if needed + primer isometric.
4. close: `pain.py resolve --id <n> --guardrail "<>" --note "<>" [--program-change "<>"]`.
5. `pain.py audit`. any FLAG -> phase 4.

## phase 3 -- query
`pain.py list [--exercise <slot>] [--days n] [--open]` / `recent` / `show --id n` /
`audit [--window-days 30] [--threshold 3]`. speak in own voice: what keeps hurting,
where, trend. `NO_EVENTS` on fresh instance = correct empty state, not a fault.

## phase 4 -- program review
audit flag = coaching signal, not auto-change. pain-triage owns detect / judge /
propose (both directions); workout-program owns the adaptation catalog + program.yaml
write ("injury-driven program adaptation 라이프사이클").
- escalation (recurring-fault / recurring-side / rising-pain): propose change + why ->
  on approval route via safety ledger + workout-program -> `resolve --program-change`.
- recovery (roll-back): audit emits NO recovery flag. judge from `pain.py list`.
  one-axis one-step probe, post-session only.
read reference/program-review.md when an audit FLAG prints or a recovery roll-back
is on the table.

## integration
session lifecycle + set logging = workout-session; program.yaml = workout-program;
session row = kit workout-log; injury ledger = kit_life SoT (main-session write).
loose join to workouts = by date.

## model routing
phase 1 + 2 talk = main agent (hard cases opus); keep phase 1 terse. pain.py = plain python.
