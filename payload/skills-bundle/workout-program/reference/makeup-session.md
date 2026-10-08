# 주말 보충세션 규칙 (owner 2026-08-01; purpose step 2026-08-22)

Read when: rx-calc `session_class == "makeup"` (workout-session session-start hands
off here), or the user asks for an extra / weekend session.

## entry + boundary

- enter ONLY on `session_class == "makeup"` (C1 deterministic gate: weekly regular
  quota met). never by weekday or ad-hoc call; never re-judge regular / makeup here
  (shared with workout-session SESSION_START).
- NOT a program.yaml structure change. regular rotation fixed; a makeup day builds the
  session on the spot, consumes no rotation counter; next regular session = next in
  queue.
- no program.yaml write (dynamic session). sets via workout-session `set-add`; the
  session record via kit workout-log.

## step 0 -- purpose first (owner 2026-08-22)

owner: looked machine-driven, not purpose-driven -- the fill ladder answered "with
what", never "why today"; same session every time. decide PURPOSE, purpose picks the
material rules.

| 목적 | 언제 | 세션 성격 |
|---|---|---|
| **회수** | 그 주에 실제로 못 채운 부위가 있다 | 부족 부위를 메운다 (= 종전 로직) |
| **공략** | 사용자가 의도적으로 특정 부위를 민다 | 지목 부위 집중. 볼륨 표엔 안 나타남 |
| **회복** | 몸이 무겁다 / 통증 / 누적피로 | **채우면 안 되고 풀어야 한다** |
| **순환** | 결핍은 없고 그냥 움직이고 싶다 | 저강도로 충분. 억지 볼륨 금지 |

ladder, first match only; estimate from evidence before asking (asking every session
is itself a cost):
- Each supplementary day, compare this week's unfinished main-session work,
  small-muscle gaps, and a cardio option. Recommend the best fit for the week's
  state and let the user choose. A supplementary day never defaults to cardio
  solely because it is supplementary, and never consumes the regular rotation.
- G0 user names the purpose ("오늘은 회수", "회복으로 가자", "등 좀 밀자") -> that purpose;
  user will beats estimate. guards still apply; if G1 is also true, follow the pick but
  leave out the pain site and say so in one line (notice, not refusal).
- G1 open pain -> 회복. `pain.py list --open` (`NO_EVENTS` = none). path
  activation-first: `.claude/skills/pain-triage/pain.py`, else
  `.claude/skills-bundle/pain-triage/pain.py`. neither -> G1 undecidable: say so in one
  line, go to G2 (never assume "none").
- G2 day 6+ this week, or weekly >= 400 min, or last session RIR median <= 1 -> 회복.
  user explicitly wants intensity -> G3 (fatigue cap still holds).
- G3 user names a body part / goal -> 공략.
- G4 clear volume deficit -> 회수. audit = one input, not the decider (below).
- G5 else -> 순환.

evidence (existing paths only): weekly days / minutes = `workouts` WHERE date >= this
Monday; last RIR = `workout_sets` of the previous session; open pain = pain.py above;
deficit = `rx-calc --volume-audit`.

## step 0-B -- opening briefing (mandatory)

never announce the verdict alone. owner rejected "이번 주 N일 M분이라 푸는 쪽으로 잡았어요":
total days / minutes are the gate's internal signal, not information.
brief in 4 parts, then offer purposes:
1. this week -- total volume (kg) + sets, per part pushed / empty. no weekday / minute
   lists; user units (part, sets, kg).
2. body now -- per-muscle residual fatigue = `service/health/fatigue-brief open --day
   <today code> --json` `lines` verbatim (photo incl., max 4 lines, numbers = kit).
   heavy week / falling logs = `--volume-audit` `signals` (perf_drop / stall /
   overreach), said separately (acute recovery vs weekly excess). never internal words
   (fresh / loaded / fatigued).
3. top pick + one-line reason. no pick without a reason.
4. 2-3 other options, each one line: character + cost (gain / defer). the pick = G0.
the ladder stays as the reason for the top pick; user chooses on top of it.
combos beat pure types: low-fatigue gaps (calves / abs / forearms) do not clash with
recovery ("회복 + 저피로 구멍 메우기").
one-line 3-way confirm only when unclear (G2 vs G3 clash, or fell to G5). leave an
exit on the verdict ("다르게 가고 싶으시면 말씀만 하세요" class); a named purpose = G0.

audit is NOT the sole decider -- known faults: warmup ramps counted as training volume;
no kg in the metric (heavy 3 sets = light 3 sets); ungraded bands (MAJOR GAP). shaky
number: G4 input only, never overriding the gates above.

## material by purpose

- 회복: rehab drills lead + mobility + low-intensity pump. NO heavy barbell compounds.
  30-40 min is enough; short is not failure.
- 공략: real volume on the named part, inside next-session protection.
- 회수: fill order 1-4 below.
- 순환: low-intensity full-body circuit + rehab drills. empty unrecovered pool -> never
  manufacture volume.

guards, every purpose (safety constraints, not material rules):
- next-session protection: next day is a regular session -> avoid heavy load on its
  target groups (e.g. Sunday before the front-A day: no heavy chest / quad / triceps;
  fill parts it does not hit). weekday bias: Sat = 회수 + arms free; Sun = non-overlap +
  low fatigue.
- fatigue cap: day 5-6 -> isolation / machine / cable / bodyweight only, no heavy
  barbell compounds; RIR >= 1-2, never to failure; empty pool -> finish with low-intensity
  pump / cardio / mobility (low-fatigue activity during a cut helps; recovery pits hurt).
- injury guard: follow the user ledger injury profile (injury_shoulder -> no heavy
  overhead that side; injury_knee -> recovery pool is low-risk, keep).

## 회수 fill order

1. deficit parts (C13, 2026-08-01): weekly sets vs target per group from
   `rx-calc --volume-audit`, not "was the lift done". log-note "이월/미실시/스킵" marks
   only explain why; a same-name lift logged != target met.
2. chronic low-volume parts (back; side / rear delt -- shoulder profile on ledger ->
   pain-signal-conditional, no heavy overhead). lowest weekly volume first.
3. arm block with recovery bias: skip the head trained in the last 24-48 h, train the
   rested one.
4. rehab drills, weekend default-include (C3): reuse drills already defined in
   stretch-matrix.md (knee / shoulder). default, not "if time"; makeup days repeat on
   day 5-6 -- design for repetition. trim only when short on time.

## build procedure (C13 / C2; step 0 first since 2026-08-22)

request -> step 0 purpose -> (회수 only) audit per group + last 24-48 h hit parts ->
apply order / guards -> slot list -> reorder: (i) station / muscle adjacency (zones +
hops from files/program/gym-layout.md, never by eye; absent -> route axis off), (ii)
posture adjacency (fewest stand <-> lie switches; floor / mat drills in the front
mat-prep block). priority = what goes in; reorder = in which order. weights: reuse
program.yaml slot values; new / unmeasured -> first-set calibration.

output: post the session in the workout-session session-start full-routine format (2
lines per lift in a code block; spec = workout-session reference/progress-tables.md
"(1) 세션 시작 전체 루틴 카드"). no wide aligned grid (Korean glyph width breaks mobile);
no forced rx-card image (user prefers code block, 2026-08-01).
