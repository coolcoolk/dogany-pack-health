---
# Fatigue-management sprint 2026-10-06 (dispatch kw-deload), for the
# next-version adaptive daily program. First of two rows. This one answers
# WHEN a lifter should take a lighter week (planned vs reactive) and WHAT a
# deload changes. Its partner, exercise/rir-accuracy-readiness-signals-061,
# owns the day-to-day signals and the RIR instrument; the reactive triggers
# below point at its signals instead of restating them.
#
# Numbering: 057-059 were taken on sibling branches in parallel, so this row
# starts at 060 to stay collision-free; renumbered at merge if needed.
#
# deload_prescription and deload_triggers are structured data for the
# adaptive daily layer. Every numeric value is either copied from a source
# (and says so) or labelled a product constant. The YAML-subset reader
# returns numbers as strings; cast them.
id: exercise/deload-planned-vs-reactive-060
domain: exercise
grade: C (a short deload costs little or no hypertrophy, and no trial shows it adds any; a full week off may cost a little strength); D (deload frequency, length and recipe are practitioner practice and expert consensus)
lane: "@gym-craft"
locale: universal
as_of: 2013-2026
contested: no
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10809978/"  # Coleman M et al. 2024, PeerJ 12:e16777, doi 10.7717/peerj.16777 -- RCT, 39 trained completers (50 randomised): 1 week of complete cessation at week 5 of a 9-week high-volume to-failure program vs continuous; quad thickness no difference (mid +4.1 vs +4.6 mm), squat 1RM +12.9 vs +16.4 kg and isometric +3.0 vs +20.2 Nm favouring continuous (Bayesian credible intervals overlapping zero); DELOAD reported MORE soreness and LESS motivation afterwards
  - "https://pubmed.ncbi.nlm.nih.gov/23053130/"  # Ogasawara R, Yasuda T, Ishii N, Abe T 2013, Eur J Appl Physiol 113(4):975-985 -- RCT n=14 untrained men, bench press: three 6-week blocks separated by 3-week cessation vs 24 weeks continuous; similar overall CSA and 1RM gains; continuous group's rate of gain slowed after week 6
  - "https://doi.org/10.1038/s41598-026-40612-5"  # Pancar Z et al. 2026, Sci Rep 16:10299 -- within-subject RCT n=19 untrained men: reduced-volume deload weeks (2 sets, once a week) at weeks 4 and 8 vs continuous; no condition difference in muscle thickness or 10RM (all CIs include zero). Abstract read only
  - "https://shura.shu.ac.uk/33446/"  # Rogerson D, Nolan D, Korakakis PA, Immonen V, Wolf M, Bell L 2024, Sports Med Open 10:26, doi 10.1186/s40798-024-00691-y -- survey n=246 competitive strength/physique athletes; deload every 5.6 +/- 2.3 weeks, lasting 6.4 +/- 1.7 days; 47.2% pre-planned, 39.4% planned plus reactive, 13.4% reactive only; triggers: programme 65.4%, feeling beat up (soreness, joint aches, pain) 62.6%, performance stall or drop 54.1%; weekly sets down 78.9%, multi-joint effort down 84.9%, main-lift frequency unchanged 61.0%. Full text read
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10511399/"  # Bell L, Strafford BW, Coleman M, Androulakis Korakakis P, Nolan D 2023, Sports Med Open 9:87, doi 10.1186/s40798-023-00633-0 -- Delphi, 34 -> 21 expert coaches; definition "a period of reduced training stress designed to mitigate physiological and psychological fatigue, promote recovery, and enhance preparedness for subsequent training"; consensus that deloads may be pre-planned, autoregulatory or both, reduce volume and/or proximity to failure, keep frequency, and that intensity may stay high
  - "https://pubmed.ncbi.nlm.nih.gov/32602418/"  # Bell L, Ruddock A, Maden-Wilkinson T, Rogerson D 2020, J Sports Sci 38(16):1897-1912 -- scoping review, 47 articles: high-volume or high-intensity RT can produce functional overreaching, chronic overload can produce non-functional overreaching; minimal evidence of true overtraining syndrome in RT
  - "https://pubmed.ncbi.nlm.nih.gov/31820373/"  # Grandou C et al. 2020, Sports Med 50(4):815-828 -- systematic review, 22 overload studies in RT: 12 produced a performance drop (8 with follow-up), 10 none; no standard diagnostic criteria. Abstract read
  - "https://sportgeneeskunde.com/wp-content/uploads/Meeusen-et-al-2013-Overtraining-Consensus-ECSS-ACSM.pdf"  # Meeusen R et al. 2013, Eur J Sport Sci 13(1):1-24 -- ECSS/ACSM joint consensus: a performance decrement is what defines overreaching; no single marker (hormonal, biochemical, psychological) meets the criteria for general use. Cited from the record
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7552788/"  # Travis SK, Mujika I, Gentles JA, Stone MH, Bazyler CD 2020, Sports 8(9):125 -- peaking review: taper of 2 weeks or less, volume-load roughly halved, intensity kept or reduced; a different job from a mid-block deload. Abstract read
  - "exercise/rir-accuracy-readiness-signals-061"  # within-warehouse partner: the signals the reactive triggers read
  - "exercise/volume-landmarks-heuristic-015"  # within-warehouse: the ramp-then-deload scaffold this row grades
  - "exercise/recovery-kinetics-session-spacing-025"  # within-warehouse: proximity to failure drives recovery cost
  - "exercise/doms-timeline-mechanism-023"  # within-warehouse: why soreness alone is not a trigger
  - "exercise/caution-severity-ladder-056"  # within-warehouse: joint aches and pain go to the caution ladder, not to a deload
  - "framework:GRADE -- the outcome evidence is three small RCTs (n=39 trained, n=14 and n=19 untrained) with consistent direction for hypertrophy (no cost) and an imprecise small strength cost for a full week off. No trial tests a deload against no deload over a longer horizon, none tests planned against reactive timing, and none compares deload recipes. Frequency, length and recipe come from one survey of practice and one Delphi of coaches."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
deload_prescription:
  - field: duration_days
    value: 7
    kind: practice
    note: survey mean 6.4 days (SD 1.7); one microcycle
    basis: Rogerson 2024
    basis_grade: D
  - field: planned_interval_weeks
    value: 6
    range: [4, 8]
    kind: product constant
    note: survey mean 5.6 weeks (SD 2.3); the 6 is the plan's default, not a measured optimum; skip the planned deload if a reactive one happened in the last 3 weeks (product constant)
    basis: Rogerson 2024; Bell 2023
    basis_grade: D
  - field: weekly_sets_multiplier
    value: 0.5
    kind: product constant
    note: direction (fewer sets) is consensus and majority practice; no source fixes the size; one half matches the peaking literature's halved volume-load
    basis: Bell 2023; Rogerson 2024; Travis 2020
    basis_grade: D
  - field: rir_floor
    value: 3
    kind: product constant
    note: direction (further from failure) is consensus and 84.9% practice on multi-joint lifts; no set taken to failure during the deload week
    basis: Bell 2023; Rogerson 2024
    basis_grade: D
  - field: load
    value: keep or trim
    kind: practice
    note: intensity may stay high (Delphi 81%); most athletes trim load somewhat; the engine keeps the working load and lets sets and RIR carry the reduction, trimming only where the RIR floor is otherwise unreachable
    basis: Bell 2023; Rogerson 2024
    basis_grade: D
  - field: frequency
    value: unchanged
    kind: practice
    note: training days and main-lift frequency stay; consensus 100%, practice 61.0%
    basis: Bell 2023; Rogerson 2024
    basis_grade: D
  - field: exercise_selection
    value: unchanged
    kind: practice
    note: same movements, same range of motion (practice 70.3% / 89.0%); keeps the next block's first week from being a novelty bout (023)
    basis: Rogerson 2024
    basis_grade: D
  - field: full_cessation
    value: not default
    kind: evidence
    note: a full week off did not cost hypertrophy but leaned toward smaller strength gains and left trainees more sore and less motivated on return; use only when the user asks for or needs time off
    basis: Coleman 2024
    basis_grade: C
deload_triggers:
  - trigger: planned
    condition: planned_interval_weeks of regular training reached without a deload
    action: deload week per deload_prescription
    basis_grade: D
  - trigger: performance-drop
    condition: the anchor lift misses its reps, or reported RIR on the first working set is 2 or more below target at the same load, in two consecutive exposures (thresholds are product constants; signal defined in 061)
    action: deload week now; the planned clock restarts
    basis_grade: C
  - trigger: performance-drop-plus-wellness
    condition: performance-drop on one exposure AND low self-reported fatigue / motivation / sleep quality on 3 or more of the last 5 days (product constants)
    action: deload week now
    basis_grade: C
  - trigger: wellness-only
    condition: low self-reported wellness with performance holding
    action: no deload; trim today's session per 061 and keep watching performance
    basis_grade: C
  - trigger: soreness-only
    condition: muscle soreness with performance holding
    action: no deload; soreness is not a load signal (023)
    basis_grade: B
  - trigger: joint-ache-or-pain
    condition: joint aches, tendon pain or any pain at a site
    action: route to the caution ladder (056), not to a whole-body deload
    basis_grade: D
  - trigger: life-stress-or-travel
    condition: user reports a hard week (exams, travel, illness recovery, high stress) ahead
    action: offer to move the planned deload into that week (practice; 30-31% of surveyed athletes deload for stress or travel)
    basis_grade: D
refraction_notes:
  - note: >
      THE DELOAD IS CHEAP, NOT PROVEN. In three small trials, a lighter or
      missed week did not cost muscle: a full week off midway through nine
      weeks in trained lifters (Coleman 2024), two reduced-volume weeks in
      untrained men (Pancar 2026), and 3-week breaks between 6-week blocks in
      untrained men (Ogasawara 2013). No trial shows that a deload produces
      MORE muscle or strength than training straight through. Speak it as
      fatigue management that costs little, never as a growth booster or
      "resensitisation".
    grade: C
  - note: >
      A FULL WEEK OFF IS NOT THE SAME AS A DELOAD. In the one trained RCT,
      the week-off group gained less squat and isometric strength (credible
      intervals still crossed zero), came back MORE sore and LESS motivated,
      and almost none of the participants felt they had needed the break.
      The engine's default deload therefore keeps training days and
      movements and cuts sets and effort; complete rest is a user choice.
    grade: C
  - note: >
      PLANNED OR REACTIVE IS PRACTICE, NOT EVIDENCE. Most competitive lifters
      pre-plan (47.2%) or combine planning with reacting (39.4%); 13.4% only
      react. Coaches agree both are legitimate. Nothing compares them. The
      engine therefore runs a planned default (every 6 training weeks,
      product constant) with reactive triggers that can pull it earlier.
    grade: D
  - note: >
      THE TRIGGER IS PERFORMANCE. Overreaching is defined by a drop in
      performance; no hormone, blood or questionnaire marker is accepted on
      its own (Meeusen 2013). In resistance training, overload studies
      produce a performance drop only about half the time (Grandou 2020),
      and true overtraining syndrome is barely documented (Bell 2020). So a
      single bad day is noise, a repeated drop on the same lift is the
      signal, and "overtraining" is not a word the engine should use for a
      recreational lifter's tired week.
    grade: C
  - note: >
      FOR NOVICES THE CASE IS WEAKER STILL. Two of the three trials were in
      untrained men and found no cost, but beginners progress fast on low
      volumes and rarely accumulate the fatigue a deload manages. With
      training_status untrained or unknown, the planned deload is optional
      and the performance trigger does most of the work.
    grade: D
  - note: >
      A TAPER IS A DIFFERENT TOOL. Peaking for a test or meet (2 weeks or
      less, volume-load roughly halved, intensity held) is not the routine
      deload and should not be scheduled every block.
    grade: C
claim: >
  A deload -- a planned or triggered week of reduced training stress -- is
  cheap but not proven to help. Three small randomised trials found no
  hypertrophy cost from a lighter or missed week (a full week off midway
  through nine weeks in 39 trained lifters; reduced-volume weeks in 19
  untrained men; 3-week breaks every 6 weeks in 14 untrained men), and none
  shows a deload adds muscle or strength. A full week of complete rest leaned
  toward smaller strength gains and left trainees more sore and less
  motivated on return. Practice and expert consensus agree on the recipe:
  about a week, roughly every 4 to 8 weeks (survey mean 5.6), fewer sets,
  further from failure, same training days and movements, load kept or only
  trimmed; planned, reactive or both. Overreaching is defined by a repeated
  performance drop, not by soreness or any single marker, and true
  overtraining is barely documented in resistance training. Engine default:
  a planned deload every 6 training weeks (product constant), pulled earlier
  by a repeated performance drop on the anchor lift, never triggered by
  soreness alone, with pain routed to the caution ladder.
reasoning: >
  The outcome rows are Coleman 2024 (the only trial in trained lifters; full
  week off; Bayesian estimates favour continuous training for strength but
  with credible intervals crossing zero), Pancar 2026 (within-subject,
  untrained, reduced-volume weeks; abstract only) and Ogasawara 2013 (small,
  untrained, longer breaks). They agree on hypertrophy and are imprecise on
  strength, which supports C for "costs little" and nothing for "helps".
  The recipe rests on Rogerson 2024 (practice, n=246, full text) and Bell
  2023 (Delphi), so it is held at D and every number the engine uses is
  either the survey's own figure or labelled a product constant. The trigger
  logic takes Meeusen 2013's definition (performance decrement) and the RT
  reviews' finding that overload does not reliably produce a measurable drop,
  which is why the trigger requires a repeat. Soreness is excluded by 023
  and pain is routed by 056. training_status is a soft hedge: the data are
  mixed across trained and untrained samples and nothing tests deload need
  by training age.
---

# exercise/deload-planned-vs-reactive-060 -- 디로드: 언제, 어떻게

**한 줄 그림:** 디로드는 손해가 거의 없는 피로 관리일 뿐, 근육을 더 키워 주는 장치는 아니다. 6주쯤
훈련했거나 같은 운동에서 기록이 두 번 연달아 떨어지면 일주일 동안 세트와 강도를 줄인다. 근육통만으로는
디로드하지 않는다.

## Deload week (engine-readable)

| Field | Value | Kind |
|---|---|---|
| length | 7 days | practice (survey mean 6.4) |
| planned interval | every 6 training weeks (range 4-8) | product constant (survey mean 5.6) |
| weekly sets | x 0.5 | product constant (direction is consensus) |
| effort | RIR at least 3, nothing to failure | product constant (direction is consensus) |
| load | keep, trim only if the RIR floor needs it | practice |
| training days, movements | unchanged | practice / consensus |
| full week off | not the default | trial (Coleman 2024) |

## Triggers

| Trigger | Action |
|---|---|
| planned clock reached | deload week |
| anchor lift misses reps, or first-set RIR 2+ below target, two exposures in a row | deload now, clock restarts |
| one such drop plus low wellness on 3 of the last 5 days | deload now |
| low wellness, performance holding | no deload; trim today (061) |
| soreness only | no deload (023) |
| joint ache or pain | caution ladder (056), not a deload |
| hard week ahead (exams, travel, stress) | offer to move the planned deload there |

Thresholds (2 RIR, two exposures, 3 of 5 days, 6 weeks, x 0.5, RIR 3) are the
plan's rules, not measured cut-offs.

## 한국어 요약 (답변용)

- 디로드(가볍게 가는 주)는 손해가 거의 없다. 훈련 경력자가 9주 중 한 주를 완전히 쉬어도 근육 증가는
  같았고, 초보자가 가볍게 간 주를 넣어도 차이가 없었다. 하지만 디로드가 근육이나 근력을 더 늘려 준다는
  연구는 없다. "몸이 리셋돼서 더 큰다"는 식으로 말하지 않는다.
- 한 주를 통째로 쉬는 건 기본값이 아니다. 완전히 쉰 쪽은 스쿼트 근력이 조금 덜 늘었고(통계적으로
  확실하진 않음), 복귀 후 오히려 더 쑤시고 의욕도 떨어졌다. 그래서 운동하는 날과 동작은 그대로 두고
  세트 수와 강도만 줄인다.
- 기본 방식: 약 일주일, 세트는 절반, 실패 3회 전(RIR 3)에서 멈추기, 무게는 되도록 유지. 숫자는
  제품이 정한 규칙이고, "세트 줄이기·실패에서 멀어지기·빈도 유지"라는 방향은 코치 합의와 선수 대다수의
  관행이다.
- 언제: 기본은 훈련 6주마다(선수 평균 5.6주). 그 전이라도 같은 주 운동에서 목표 반복을 못 채우거나
  첫 세트가 목표보다 2회 이상 힘든 일이 두 번 연달아 나오면 바로 디로드한다. 하루 컨디션이 나쁜
  건 잡음이고, 같은 운동에서 반복되는 하락이 신호다.
- 근육통만으로는 디로드하지 않는다. 관절이 시큰하거나 어딘가 아프면 전신 디로드가 아니라 부상 주의
  단계(056)로 보낸다.
- 시험·출장·여행처럼 힘든 주가 예정돼 있으면 계획된 디로드를 그 주로 옮기자고 제안할 수 있다.
- 일반 헬스 이용자의 지친 한 주를 "오버트레이닝"이라 부르지 않는다. 근력운동에서 진짜 과훈련
  증후군은 거의 보고된 적이 없다.
- 초보자는 디로드가 꼭 필요하다는 근거가 더 약하다. 계획된 디로드는 선택으로 두고, 기록 하락
  신호를 주로 본다.
