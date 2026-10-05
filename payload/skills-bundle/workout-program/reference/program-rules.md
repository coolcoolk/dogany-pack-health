# program rules -- dose, set floor, slot fields

Read when: designing or revising slot sets / reps / weight / rest / lattice / setup
fields, a grip or equipment swap goes permanent, or asked why a dose is what it is.
program-plan `RX_RULES` transcribes 「워킹 무게를 정하는 방식」 + 「최소 세트 하한 정책」
below -- change them here and there in the same commit.

## 워킹 무게를 정하는 방식 (owner 2026-07-19)

verbatim: 「워킹 무게 결정 방식: 램프업 + RIR 오토레귤레이션 계측식 (감 기반 지양)」
- weight is MEASURED: ramp up, read the day via RIR, fix the working weight. never
  declared from last log or feel. survives any program change (program = what, this =
  how much).
- 강도 기본 스킴: 복합 RIR 1-2 · 5-8회 / 고립 RIR 0-1 · 12-15회 / 램프업 RIR 4+. slot
  `rep_range` is final authority; this is the start. compound freeweights: G19 floor
  (RIR 2-3) overrides -> reference/rir-floor.md.
- 코어·버티기 (owner 2026-09-27 「이런거 나한테 왜물어봐 지가 정해줘야지」 + 「임의로
  적지말고 지식창고 뒤져봐」): core drill 12-15회 = isolation scheme (kimwog
  exercise/set-counting-volume-unit-009 B: near-failure sets count in ~6-20+ reps;
  exercise/progression-modality-load-vs-reps-028 B: growth similar across loads). a
  lift no class covers -> isolation scheme. hold without registered `hold_sec`: 3 x
  20초 (short repeated holds over one long grind -- McGill torso-endurance practice;
  3 x 20 s front-plank trial protocol; Behm & Colado 2012: diminishing transfer past
  60-90 s). the pack decides; a dose is never asked.
- 버티기 선택 = 목적 판단 (owner 2026-09-27 11:35 「근육 크기에 영향이 없으면 목적에 안
  맞으니 빼는게 맞고」): a hold trains trunk endurance, not size. size / body-comp goal
  -> loaded core lift for abs (cable crunch); hold only for function / health goals or
  when no loaded core lift is available. candidates carry `builds_size`.
- first program: every `weight_kg` starts null; the ramp-up measures it.
- 무거운 하체 간격 (owner 2026-09-27 13:16):
  heavy = high axial spinal load only: back-squat and conventional-deadlift families.
  Romanian deadlifts, back-targeted hinges, and V squat are not heavy. Qualifying
  lifts sharing a
  muscle node never start inside the kit's recovery window (056 half-life x
  log2(hard / recovering) = 36 h for glutes / erectors). program-plan `apply_spacing`
  reorders the rotation (split kept) first, else pairs the heavy lift with a light one
  of the same pattern; the week keeps a heavy squat and hinge. one card line, never asked.
  A light replacement must not load a recorded caution area: one-leg balance is
  excluded when the standing foot or ankle is cautioned.

## 최소 세트 하한 정책 (C16/C19, owner 2026-08-01)

- WORKING slot (not warmup) never designed / kept below 3 sets. never trim to 2.
- need less weekly volume -> drop a slot, lower load / intensity, lower frequency, or
  reallocate. (reverses the old 3->2 redistribution trims of 2026-07-17 / 07-26.)
- EXCEPTION: time-hold slots (rep_range in SECONDS, e.g. wall sit) = not volume sets;
  floor does not apply, keep designed count.
- floor = LOWER bound only. never forces an increase that set-increase suppression /
  audit ceiling blocks; adding sets still needs ceiling headroom.
- 2026-08-01 adoption restored the 2-set slots to 3 after audit headroom check (hold
  slot stayed 2); all affected groups ended in_band.

## muscle fatigue in rx (F30; code = rx-calc DGN-316 6.3)

code: a PRIMARY muscle in state `fatigued` trims that lift's SETS by one step (floor
kept; hold / rehab slots never trimmed); `weight_kg` is never touched; `muscle_state`
is exposed in rx JSON. a `loaded` accessory muscle changes nothing in code. old prose
("loaded -> hold / relax weight progression") has no carrier -> rule-lane candidate,
not a rule the model applies silently.

## rest_sec -- rx-calc factor model (C18, owner 2026-07-31)

- `rest = clamp(base + intensity_adj + fatigue_adj, 60, 210)`, rounded to 15 s. base
  compound 150 / isolation 90. intensity_adj from rep_range top (<=6 +30, 7-12 0, >12
  -30). fatigue_adj from lift fatigue_cost (high +15, med 0, low -15). hold slots: base
  only. code owns it; do not hand-compute.
- slot `rest_sec` override still wins; model only fills slots without one.
- basis: warehouse rest-interval-volume-load-017 (grade B/C) -- own-rule, no "과학이
  그렇다". RIR not a rest input yet.

## 바벨 마이크로-앵커 / 2단 증량 (B7, owner 2026-07-31)

increment-unit values, not volume -> set fields directly, no volume audit.
- gym min plate 2.5 kg / side -> barbell loads in 5 kg totals. user owns micro plates
  (1.25 + 0.75 pairs), brings them for 1-2 main heavy lifts per session.
- micro-anchor slots = lifts where a 5 kg jump is a large % of load (upper-body barbell
  presses / rows): lattice {standard, step 2.5} + inc_override 2.5.
- 5 kg grid slots = big lower-body barbell lifts (jump <=5 %): lattice {standard, step
  5.0} + inc_override 5.0.
- selection = relative jump heuristic, no graded evidence (refract, no "연구가 이렇다").
- stall fallback (5 kg grid only): miss_streak >= 2 -> propose 2.5 kg micro for that
  session. live proposal, not an automatic lattice switch; rx-calc never flips lattice.
- plate notation: total = 20 kg bar + 2 x per side; convert to per-side when needed.
- low-load barbell isolation (curl) out of scope until measured.

## 단관절 고립 진행 축 -- 템포/TUT (owner 2026-08-08, NOT wired)

owner: 「단관절 고립운동 부하 증가 방향: 무게 증량 대신 수행시간(템포/TUT) 늘리는
방식으로 설계 전환」. rx-calc progression is still weight-axis; program.yaml has no
tempo / TUT field. next build / revise: propose this as default for isolation slots,
get owner ok. never fall back silently to weight-increase.

## 슬롯 셋업 참고자료 (C21, owner 2026-07-31)

- `setup_cue` (text) = PRIMARY, rendered on card / session: posture / feel,
  machine-agnostic (no raw dial numbers).
- `ref_photo` = OPTIONAL anchor only when text cannot hold gym-specific geometry; not
  parsed / rendered. not either-or: text always, photo only where needed.

## 그립 / 어태치먼트 (C19 owner 2026-07-31; F29; 2026-08-04)

- grip / variant auto-inherits last session's pick (F29); reconfirm once only on change.
  structured grip storage (grip_vocab migration) not wired -- prose rule.
- per-grip weight kept apart (2026-08-04): never mix a changed-grip session's weight
  into the original grip's line. storage split not wired -- judgment rule.
- grip_vocab (overhand / underhand / neutral / wide / close) has muscle deltas
  (grip_muscle_delta). attachment kind (rope / strap / bar) is a DIFFERENT axis
  (wrist freedom / ROM / comfort) -- never promote it to a muscle-delta axis (would
  invent ungraded deltas). record in `exercise_movement_grip.equipment`
  (documentation-only) and in setup_cue if useful.

## 기구 대체 시 슬롯 식별자 유지 (owner 2026-08-04)

owner: 「기구 대체 시 내부 슬롯명은 원래 종목명 유지, 표시명만 대체 기구로 변경 --
e1RM·볼륨 추세 이력 끊기지 않게 하는 방식으로 합의」
- slot key (English id) = history axis; display name (Korean) = render axis. a swap
  changes only render. new slot key breaks e1RM / volume trends at that point.
- live one-off swap: code carries it (workout-session set-add `--ov-display`, F19/F21).
- permanent swap in program.yaml: prose, editor keeps it. non-convertible weight system
  -> keep slot key, re-calibrate the weight line only.
