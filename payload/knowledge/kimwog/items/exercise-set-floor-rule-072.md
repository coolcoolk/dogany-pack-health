---
# Set-floor sprint 2026-10-07 (dispatch kw-ex-set-floor-experience). The
# engine-readable synthesis of 070 (growth floors, sets per exercise,
# per-session point) and 071 (maintenance floor, cut). It is a routing rule,
# not a primary finding: each row names the graded item it rests on, and
# every number below 10 weekly sets, every age boundary and the trim order
# are labelled product constants. Same posture as 056.
#
# set_floor, age_modifiers and trim_order are structured data for the
# composer (see docs/kimwog-set-floor-fields.md). Vocabulary matches
# compose_rank_rules.json: experience keys novice / returner / continuous
# (split.experience_weights), goal keys grow / cut / maintain
# (phase_aliases), set levels 3 and 2 (budget.set_levels), primary_min_sets
# (trainer_fit), cut_keep, optional_accessory_muscles, weekly_muscles. Weekly sets are FRACTIONAL (direct 1.0, indirect 0.5, 008).
id: exercise/set-floor-rule-072
domain: exercise
grade: D (synthesis rule over 070 and 071; the >=2 sets per exercise and the 10-set trained floor are B-backed, the novice / returner numbers, the age boundary and the trim order are product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "exercise/set-floor-by-experience-070"  # growth floors by experience, >=2 sets per exercise, ~11 fractional sets per muscle per session
  - "exercise/maintenance-vs-growth-volume-cut-071"  # maintenance floor (load kept), older adults need more, deficit moves the goal to keep
  - "exercise/effective-sets-fractional-008"  # fractional counting of weekly sets
  - "exercise/deficit-volume-guidance-016"  # the high-volume-protects-muscle-in-a-cut claim stays refuted
  - "exercise/volume-landmarks-heuristic-015"  # MV / MEV are practitioner defaults; these floors play the same role, labelled the same way
  - "dispatch task kw-ex-set-floor-experience 2026-10-07: engine-readable set_floor rules for a composer that must trim exercises, not sets"
  - "framework:GRADE -- multiple sets per exercise and >=10 weekly sets for growth are meta-analytic (B, 070). The maintenance fraction is one RCT plus a review (C, 071). The novice and returner floors, the maintenance numbers per experience, the age-60 boundary and the trim order are product constants with no direct evidence (D)."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
set_floor:
  - experience: novice
    words: no regular resistance training, or under about six months of it
    per_exercise_min: 2
    primary_min: 2
    weekly_growth_floor: 6
    weekly_maintenance_floor: 3
    maintenance_per_exercise_min: 1
    session_muscle_point: 11
    basis: exercise/set-floor-by-experience-070
    basis_grade: D
  - experience: returner
    words: trained regularly before, now back after a long break
    per_exercise_min: 2
    primary_min: 3
    weekly_growth_floor: 8
    weekly_maintenance_floor: 3
    maintenance_per_exercise_min: 1
    session_muscle_point: 11
    basis: exercise/set-floor-by-experience-070
    basis_grade: D
  - experience: continuous
    words: training regularly for a year or more without a long break
    per_exercise_min: 2
    primary_min: 3
    weekly_growth_floor: 10
    weekly_maintenance_floor: 4
    maintenance_per_exercise_min: 1
    session_muscle_point: 11
    basis: exercise/set-floor-by-experience-070
    basis_grade: B
set_style:
  - style: volume
    default: true
    words: three or more working sets on every lift, mains three to four (the 0.33.0 composer rule)
    per_exercise_min: 3
    primary_min: 3
    primary_max: 4
    applies_to: continuous training for a year or more (compose_rank_rules experience_set_floor)
    weekly_floor: unchanged
    basis: product rule above the two-set evidence floor (owner 2026-10-06)
    basis_grade: D
  - style: intensity
    default: false
    words: warm-up sets with fewer reps as the weight climbs, then two hard working sets per lift
    per_exercise_min: 2
    working_sets: 2
    compound_max: 3
    accessory_max: 2
    rir_target: 0-1
    rir_exception: compound free-weight lifts keep their own band (G19, rir-floor)
    ramp_counts_as_volume: false
    weekly_floor: unchanged
    floor_lever: more exercises, never more sets per exercise
    basis: exercise/set-floor-by-experience-070
    basis_grade: B
age_modifiers:
  - when: age_years 60 or more
    maintenance_per_exercise_min: 2
    weekly_maintenance_floor: 6
    maintenance_min_days: 2
    basis: exercise/maintenance-vs-growth-volume-cut-071
    basis_grade: C
goal_floor:
  - goal: grow
    priority_muscles: growth
    other_muscles: growth
    basis_grade: B
  - goal: cut
    priority_muscles: growth
    other_muscles: maintenance
    priority_source: trainer_fit.cut_keep
    basis_grade: D
  - goal: maintain
    priority_muscles: maintenance
    other_muscles: maintenance
    basis_grade: C
trim_order:
  - step: 1
    action: drop an unfocused isolation exercise for an optional accessory muscle whose weekly floor is already met by fractional sets from compounds
    keeps_sets_per_exercise: true
    basis_grade: D
  - step: 2
    action: drop a second exercise for the same muscle and the same pattern in one session
    keeps_sets_per_exercise: true
    basis_grade: D
  - step: 3
    action: on a cut, lower muscles outside cut_keep from the growth floor to the maintenance floor by removing exercises
    keeps_sets_per_exercise: true
    basis_grade: D
  - step: 4
    action: lower accessory exercises from set level 3 to 2, never below per_exercise_min
    keeps_sets_per_exercise: false
    basis_grade: B
  - step: 5
    action: if a weekly_muscles muscle still misses its floor, keep the shortfall and name the muscle to the user; do not create one-set slots and do not lighten the load
    keeps_sets_per_exercise: true
    basis_grade: D
never:
  - an exercise below per_exercise_min sets in a growth or cut week
  - the primary lift below primary_min sets
  - reducing load or effort per set to fit the minutes
  - dropping the last exercise that gives a weekly_muscles muscle its direct sets while that muscle is below its floor
refraction_notes:
  - note: >
      THE PER-EXERCISE FLOOR IS THE USER'S STYLE, THE WEEKLY FLOOR IS NOT.
      Two or three hard sets per exercise grow about as well as four to six
      when the weekly sets per muscle and the closeness to failure match
      (070, B). So the per-exercise floor is a setting (set_style): volume
      keeps three or more per exercise, intensity takes two working sets at
      RIR 0-1 after warm-up sets that are never counted as weekly sets. The
      weekly per-muscle floor does not move with the style; under intensity
      it is reached with more exercises. The volume floor of three is a
      product rule, the two-set floor is the evidence line.
    grade: B
  - note: >
      TRIM EXERCISES BEFORE SETS. With a fixed number of minutes, sets
      concentrated on fewer exercises buy more weekly sets than the same
      minutes spread over many short slots, because every exercise carries a
      setup and transition. Two or more sets per exercise is where the
      per-exercise evidence sits (070). The ordering itself is product
      judgement; no trial compares the two under a time budget.
    grade: D
  - note: >
      THE TRAINED FLOOR IS 10, THE NOVICE AND RETURNER FLOORS ARE OURS.
      Ten weekly fractional sets per muscle is the umbrella-review line for
      growth (070). Six for a novice and eight for a returner rest on
      novices growing well at low volume, not on a trial of those numbers.
      Nothing in this sprint measured how fast a returner regains muscle.
      Speak the lower floors as the plan's rule, never as a measured
      threshold.
    grade: D
  - note: >
      MAINTENANCE IS ABOUT A THIRD OF GROWTH, WITH THE LOAD KEPT. The
      maintenance floors (3 or 4 weekly sets, one set per exercise allowed)
      follow the one-third / one-ninth arms that kept young adults' muscle
      for 32 weeks. From age 60 the floor rises to about two days and two
      sets per exercise, because the older arm lost size at the lower doses.
      The 60 boundary is a product constant.
    grade: C
  - note: >
      THE SESSION POINT MOVES SETS, IT DOES NOT CUT THEM. When one muscle
      would get more than about 11 fractional sets in one session, move the
      excess to another session that trains it; if none does, the sets may
      stay. It is a point of no detectable extra benefit, not a harm limit.
    grade: C
  - note: >
      A CUT DOES NOT RAISE THE FLOOR. Raising sets in a deficit to protect
      muscle was tested and refuted (016); the cut rule only lets
      non-priority muscles fall to maintenance so the priority muscles keep
      their growth floor inside the same minutes.
    grade: B
claim: >
  The composer should hold a per-exercise floor of two working sets (one in a
  maintenance week), a primary-lift floor of two sets for novices and three
  otherwise, and a weekly fractional-set floor per muscle of 6 (novice), 8
  (returner) or 10 (continuous) for growth and 3-4 for maintenance, raised to
  about 6 over two days from age 60. A cut keeps cut_keep muscles at the
  growth floor and lets the rest fall to maintenance. When the minutes do
  not fit, it trims whole exercises first (optional accessories already
  covered, redundant same-pattern exercises, then non-priority muscles on a
  cut), then accessory set level 3 to 2, and never goes below a floor or
  lightens the load; a muscle that still falls short is reported, not padded
  with one-set slots. Only the two-set exercise floor and the 10-set trained
  floor are evidence-backed numbers; the rest are product constants.
reasoning: >
  070 gives the B-backed anchors (2-3 sets per exercise beats one; >=10
  weekly sets enhances growth) and the C-level per-session point; 071 gives
  the maintenance fraction with the load kept, the age difference and the
  deficit effect on gain. The experience rows copy those anchors and fill
  the gaps with labelled constants. The trim order follows from the
  composer's own costs (each lift adds a transition) and from the absence of
  any benefit for redundant same-pattern exercises, and it keeps the
  existing composer guarantees (primary_min_sets, every weekly muscle
  trained). It reverses the order the current set_levels_doc states
  ("fewer sets per lift before fewer lifts"): here covered and redundant
  exercises go first and set level 2 comes after. That change belongs to
  the build and is not made here.
---

# exercise/set-floor-rule-072 -- 시간이 모자랄 때 세트 말고 종목을 줄이는 규칙

**한 줄 그림:** 종목당 2세트, 근육당 주간 최소선은 지킨다. 시간이 모자라면 종목을 먼저 빼고,
그래도 모자라면 그 근육이 부족하다고 말한다.

## The floors (weekly sets are fractional: direct 1, indirect 0.5)

| Experience | Sets / exercise | Primary lift | Weekly growth floor | Weekly maintenance floor |
|---|---:|---:|---:|---:|
| novice | 2 | 2 | 6 (product) | 3 (product), 1 set / exercise allowed |
| returner | 2 | 3 | 8 (product) | 3 (product), 1 set / exercise allowed |
| continuous | 2 | 3 | 10 | 4 (product), 1 set / exercise allowed |
| age 60+ (any) | -- | -- | -- | 6 over 2 days, 2 sets / exercise |

Session point: about 11 fractional sets for one muscle in one session; above
it, move sets to another day that trains the muscle.

## Trim order when the minutes do not fit

1. Drop an unfocused isolation exercise for an optional accessory muscle
   already at its floor from compound work.
2. Drop a second same-muscle, same-pattern exercise in one session.
3. On a cut, take muscles outside `cut_keep` down to the maintenance floor by
   removing exercises.
4. Lower accessories from 3 sets to 2 (never below 2).
5. Still short: keep the shortfall and name the muscle. No one-set slots, no
   lighter load.

Example with the composer's own costs (isolation 8 minutes at 3 sets, 2
minutes transition): two accessories at 3 sets take about 20 minutes for 6
sets; three at 2 sets take about 22 minutes for the same 6 sets.

## 한국어 요약 (답변용)

- 종목 하나는 최소 2세트로 한다. 첫 번째 큰 운동은 초보 2세트, 그 외 3세트를 지킨다. 2세트 이상이
  1세트보다 낫다는 건 연구로 뒷받침된다.
- 근육 하나의 주간 최소선(보조로 쓰인 세트는 반 세트로 셈)은 근성장 기준으로 초보 6, 복귀자 8,
  꾸준히 해 온 사람 10세트다. 10은 지침에 근거가 있고, 6과 8은 제품이 정한 숫자다.
- 유지가 목표일 때는 주 3~4세트, 종목당 1세트도 된다. 대신 무게는 그대로 지킨다. 60세 이상은
  주 2회, 종목당 2세트, 주 6세트 정도로 올린다. 60이라는 경계는 제품 기준이다.
- 감량기에는 하체·등·가슴 같은 우선 근육은 성장 최소선을 지키고, 나머지는 유지선까지 내린다.
  감량 중이라고 세트를 늘리지는 않는다.
- 시간이 모자라면 이 순서로 줄인다. 이미 충분히 쓰인 근육의 고립 운동 빼기, 같은 근육·같은 패턴의
  중복 종목 빼기, 감량기면 우선 아닌 근육을 유지선까지 내리기, 보조 종목을 3세트에서 2세트로.
  그래도 모자라면 1세트짜리 종목을 끼우거나 무게를 낮추지 말고, 어느 근육이 부족한지 그대로 알린다.
- 한 번 운동에서 한 근육이 11세트를 넘으면 넘는 만큼 다른 날로 옮긴다. 해롭다는 기준은 아니다.
- 종목당 세트 방식은 사용자가 고른다(set_style). 기본은 종목마다 3세트 이상(volume), 원하면 몸풀기
  세트 뒤 본 세트 2세트를 실패 직전(RIR 0~1)까지 하는 방식(intensity)으로 바꾼다. 몸풀기 세트는 주간
  세트에 세지 않고, 근육별 주간 최소선은 어느 방식이든 그대로다. 2세트 방식에서는 종목을 늘려 채운다.
- 이 순서와 대부분의 숫자는 제품 규칙이다. 답할 때도 연구로 정해진 값처럼 말하지 않는다.
