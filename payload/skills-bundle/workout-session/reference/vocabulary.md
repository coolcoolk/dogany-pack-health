# user-facing vocabulary (read at session start; canonical for every word the user sees)

## never shown to the user
- component / script / file / function names: `rx-calc`, `set-table`, `program.yaml`,
  `service/health/...`. say the result, never the mechanism. program.yaml -> "운동 프로그램".
- internal state keys / flags / English tokens (2026-08-20 leak recurrence): "water due"
  (set-arm now prints `water=1/0`; code writes the water line itself), "(top)" / "상단(top)"
  -> "목표 횟수" or "상단", ROM words bottom / mid / peak / lockout -> Korean only.
- ticket IDs and parenthesised English expansions; code removed both.
- skill delegation / routing / hand-off (owner 2026-09-11: 「지 담당이아니라고? 이소리왜함」).
  one agent to the user. banned in any form: 「제 담당이 아니라」 「전용 스킬로 넘겨서」
  「스킬을 호출해서」 「~ 스킬이 처리합니다」 「핸드오프」 「라우팅」. say what you do:
  「세션 시작할게요」.

## "처방" banned (#38, owner 2026-08-19; medical nuance)
- whole session's weights / sets -> **"오늘 플랜"** (or "오늘의 운동 루틴").
- one lift / set's numbers -> **"오늘 무게/세트"**.
- "처방 무게" -> "오늘 무게", "처방 큐" -> "오늘 큐" / "시작 큐", "처방한 대로" -> "플랜대로".
internal code / keys / DB (rx, rx-calc, calc_rx) stay English; rule prose may say 처방
internally, never to the user.

## 사용자 대면 어휘 (owner ruling 2026-08-25 09:30) -- internal keys unchanged
| internal key (English, fixed) | user reads |
|---|---|
| `prep` | **준비운동** |
| `warmup` | **웜업** |
| `ramp` | **웜업** (no separate category) |
| `bw` (`set_seq == 0`) | **세팅** |
- user says "프렙" in chat -> output still 준비운동 (user chose to follow product wording).
- **웜업이지 워밍업이 아니다.** 웜업 is the word the user actually uses.
- ruling 1 (2026-08-25 12:04): 「프라이머」 retired, 「세팅」 replaces it (names what the user
  does: sit, pin, move once). direction is 프라이머 -> 세팅, never the reverse.
- ruling 2 (2026-08-25 12:04): the 2026-08-14 rule "스택류(케이블·핀) -> 프라이머 생략" is
  REVERSED. stack machines get a 세팅 set too (07:07 lat_pulldown had none; face_pull same).
  one name, equipment-specific description:
  ```
  바벨·스미스        빈 봉 (20kg)
  플레이트로디드     원판 없이 (무부하)
  스택(케이블·핀)    낮은 무게 한 세트
  ```
- real exercise terms (슈러그 / 플라이 / 랫풀다운) untouched; only coined compounds
  (프리프레스 / 프라이밍 / 프렙) are replaced.
- speech DEPTH (RIR in plain words, sub-muscle names, tempo talk) is a separate axis:
  workout-program "도메인 화법 레지스터" (config `vocab_register`). tool strings verbatim
  outrank the register: table / NEXT_HINT RIR text goes out as printed.
- 구간은 **준비운동 / 본운동 / 쿨다운**이다. 준비운동 안의 움직이는 동작은
  **모빌리티**, 근육에 힘을 넣는 동작은 **활성화**다. 쿨다운의 멈춰서 늘리는
  동작은 **스트레칭**이다. 본운동은 종목의 세팅 → 웜업1.. → 본 세트 1..,
  그리고 끝의 유산소로 이뤄진다. 준비운동 동작은 종목 세트표에 넣지 않는다.
- 세트표 열은 **세트 · 무게 · 횟수 · RIR · 표시**이며 표시 열 제목은 비운다.
  부위 줄은 **주동근 X · 보조근 Y**, 기록은 **볼륨 / 예상 1RM /
  최근 N세션 추세**, 휴식은 분·초로 적는다. 종료는 **🏁 세션 종료**와
  **합계: N종목 · 본 세트 N · 볼륨 N,NNNkg**으로 적는다.
- reference prose is not output vocabulary: progress-tables.md / warmup-stretch.md /
  stretch-matrix.md / gym-layout.md still say "매트 프렙", "기구프렙", "워밍업". never carry
  those words to the user. card headers (`0 매트 준비운동` / `E 장비 준비운동`) are owned by
  `rx-card.py`.

## domain layers -- one name per layer (H7, 2026-08-24)
```
프로그램 > 로테이션 데이(앞A/뒷A/앞B/뒷B) > 세션 > 구간(준비운동/본운동/쿨다운)
        > 종목 > 세팅·웜업·본 세트
```
| internal key | user hears | is | is not |
|---|---|---|---|
| `session` (`workouts.id`) | 세션 | one workout, in to out | a day (2 a day = 2 sessions); not 앞A |
| `session_type.code` | 앞A / 뒷A / 앞B / 뒷B / 보충 | rotation position | muscle names ("가슴+쿼드") |
| `slot` (`slot_num`, `card_slot`, `live_slot`) | 종목 | an ordered place in today's plan | the movement; a substitute keeps the slot |
| `exercise_name` / `ax_exercise` | 종목 | the movement itself | today's order |
| `step` (`us_step.step_type`) | (not shown) | prep / warmup / ramp / working / hold unit | chat "STEP 1·2" |
| `set` (`set_seq >= 1`) | 세트 | one unbroken rep bundle | warmups do not count |
| `rung` (`set_seq <= 0`, `bw` / `rN`) | 웜업 (`bw` = **세팅**) | loading steps before working | a set; never say "렁" / "램프" |
| `drill` (prep.yaml `code`) | 준비운동 | one prep / cooldown move | a lift; no sets / weight |
| `round` | 라운드 | one pass through drills | a set; not used in main work |
display names rendered by code live in `service/health/ui_labels.py` `layer.*` (knob, like
RIR). never re-type them as literals. unregistered layers (exercise / step) keep their internal keys
by the user, not missing; do not fill them.

폐기어 (second names for a layer; never write new):
- "슬롯" to the user -> 종목. internal only.
- `empty_bar` / `ramp_1` -> canonical rung labels are `bw` / `rN` (`ax_engine.py` still
  accepts both).
- "정리세션" / "마감세션" -> the closing phase of a session, not a separate session.
- "워밍업" -> 웜업 (ruling 2026-08-25 09:30; the line once said the opposite).
- "프라이머" -> 세팅 (never reverse it).
- "램프" to the user -> 웜업. `ramp` stays an internal key.
- "프렙" / "준비 드릴" -> 준비운동.
- "slot" in `ax_projection_slot` = step layer (one row per `step_ref`), not exercise order.

## RIR display (2026-08-24 correction, reverses the 2026-08-23 "여유 N개" substitution)
the term is RIR. only the display name can change, owned in ONE place:
`service/health/ui_labels.py` resolver (DB `ui_label` row, else `RIR`).
- never compose a display name; echo tool strings. no invented aliases ("여유", "몇 개
  더 할 수 있는 여유"): a second name made `여유` and `RIR` appear on one screen.
- user asks what it means -> one line, the same words as the ask's explainer
  ("자세 안 무너지고 몇 개 더 할 수 있었는지예요."); never rename.
- `rir`, DB column, JSON key, `--rir` flag unchanged. no exception list remains: every
  surface goes through the resolver.
- THE RIR ask (owner 2026-10-10 18:49), code copy on every RIR keyboard (working set,
  warm-up `RIR_ASK`, text ask): "이번 세트 RIR은요?", buttons `0 · 1 · 2 · 3 · 4+`. for
  the owner's first 3 workout sessions with an RIR ask the explainer line sits directly
  under the question (`RIR_EXPLAINER:` on stdout), then code drops it. the explainer
  lives ONLY at the ask: never in a confirm, a fold, a cue or a recap (2026-09-14).
- cue `데드리프트 50kg × 10 (RIR 2~3)`, record `✅ 1세트 · 50kg × 10 · RIR 2`, 세트표
  column `RIR` -- echoed from code, never re-typed.
- typed results: "10-2", "10회 RIR 2", "10 2" = 10 reps, RIR 2 (`ui_labels.parse_reps_rir`).
- wording preference, ONLY when the owner asks for it: `kit_life.sh config-set
  rir_wording=yeoyu|rpe|rir` (default rir). 여유: "여유 2개", buttons "여유 없음 · 1개 ·
  2개 · 3개 · 4개+", ask "이번 세트 얼마나 여유 있었어요?". RPE: "RPE 8" = 10 - RIR. the
  stored value is RIR in every mode; the 세트표 column stays `RIR`.

## rep range in chat (owner 2026-08-25; supersedes 2026-07-22 "top rep only")
announce a working-set rep target as the narrow range that set will actually produce,
not the slot's whole rep_range and not the top number: "워킹세트 1/3: 60kg, 목표 7-8회
(RIR 1~2)". RIR stays a range. prose-only (no code narrows the range yet).
