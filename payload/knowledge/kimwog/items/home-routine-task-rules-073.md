---
# Home routines sprint 2026-10-06 (dispatch task kw-home-routines: "rules the
# lifekit routine/task modules can use"). The engine-readable synthesis of 070
# (cognitive labour), 071 (fairness, buying time) and 072 (cleaning cadence,
# targeted hygiene), plus the existing time-cost row (013) and the
# task-management rows on estimates and records. Same posture as
# exercise/caution-severity-ladder-056: a routing rule, not a primary finding;
# each rule names the graded row it rests on and every product constant is
# labelled as one.
#
# routine_rules is structured data for the lifekit routine / task modules.
# Fields per rule: rule (stable key), module (routine | task | both), when
# (the condition), action (what the module does), never (what it must not
# do), constant (true when the rule contains a chosen value with no evidence
# behind it), basis (within-warehouse row), basis_grade (how strongly that
# row backs THIS rule -- not the row's headline grade). The YAML-subset reader
# returns scalars as strings; booleans and flow lists parse natively.
id: home/routine-task-rules-073
domain: home
lane: "@household-labor"
grade: D (synthesis rule over 070, 071, 072, 013 and task-management 001, 002, 009; individual rules carry their own basis grade, from B down to D)
locale: universal
as_of: 2026
contested: no
sources:
  - "home/cognitive-labour-mental-load-070"  # four stages; whole-task ownership; no load score
  - "home/chore-fairness-and-buying-time-071"  # ask fairness, never compute; drop -> reassign -> buy off
  - "home/cleaning-frequency-targeted-hygiene-072"  # no health-based cadence; event-triggered hygiene
  - "home/kr-household-labour-time-013"  # household labour is an hours-per-day block in Korean dual-income homes
  - "home/dampness-mould-respiratory-001"  # damp is the one home exposure with strong harm evidence
  - "home/kr-mandated-ventilation-rate-004"  # ventilation is the lever for damp
  - "task-management/planning-fallacy-own-estimates-001"  # own duration estimates run short; pessimism prompts do not fix it
  - "task-management/reference-class-base-rate-002"  # use the record of past completions as the base rate
  - "task-management/record-is-not-behaviour-009"  # a checked box is a record, not the act
  - "relationships-communication/roster-without-chore-list-021"  # owner directive: no nagging, no streaks, no debt ledger; caps in code
  - "framework:GRADE -- synthesis rule. Where a rule restates a graded row it inherits that row's support for the specific point; the rule-set as a whole, its ordering of responses and every default value are product judgement."
routine_rules:
  - rule: whole-task-owner
    module: both
    when: a recurring household task is created or reassigned
    action: assign one owner for the whole task (notice, options, decision, follow-up) as well as the execution; the module itself holds the anticipation (the reminder) and the monitoring (the done-check)
    never: split a recurring task into "who decides" and "who does" by default; compute or display a mental-load score
    constant: false
    basis: home/cognitive-labour-mental-load-070
    basis_grade: D
  - rule: task-kind
    module: routine
    when: a household task is defined
    action: tag it event-hygiene (fires on a risk moment) or calendar-comfort (fires on a household-set interval); event-hygiene triggers are food handling, eating with fingers, toilet and nappy, coughing and sneezing, frequently touched surfaces, dirty laundry and linen, pets, refuse, an ill household member
    never: present any calendar interval as medically or hygienically required
    constant: false
    basis: home/cleaning-frequency-targeted-hygiene-072
    basis_grade: D
  - rule: cadence-source
    module: routine
    when: a calendar-comfort task has no interval set
    action: ask the household once for its own interval; if unanswered, use a starter interval labelled "a starting point, change it freely"
    never: cite a health reason for the starter interval; re-ask after a refusal
    constant: true
    basis: home/cleaning-frequency-targeted-hygiene-072
    basis_grade: D
  - rule: duration-from-record
    module: task
    when: a chore needs a time estimate for scheduling
    action: use the household's own logged durations for that chore as the base rate once at least a few completions exist; before that, use the stated estimate and label it likely short
    never: fix a short estimate by asking the person to be more pessimistic; use a national average as a personal duration
    constant: true
    basis: task-management/planning-fallacy-own-estimates-001
    basis_grade: B
  - rule: household-block-is-real-time
    module: both
    when: a day or week plan is built for someone in a household
    action: reserve household labour as its own block in hours, sized from the household's own record or statement
    never: treat housework as slack between scheduled items; size the block from the national mean for a specific person
    constant: false
    basis: home/kr-household-labour-time-013
    basis_grade: B
  - rule: over-capacity-order
    module: both
    when: the scheduled household load exceeds the capacity the household has stated
    action: offer, in this order -- drop or lower the standard of a calendar-comfort task; reassign a whole task; buy the task off (outsourcing) as one option
    never: frame outsourcing as advice to spend; drop or delay an event-hygiene task to make room
    constant: true
    basis: home/chore-fairness-and-buying-time-071
    basis_grade: D
  - rule: fairness-is-asked
    module: both
    when: the split between household members comes up, or the household asks for a split
    action: treat the household's own stated agreement as the target; if fairness is in question, ask the people, do not infer it
    never: score the split against 50/50; show a running tally or leaderboard of who did more; name who is behind
    constant: false
    basis: home/chore-fairness-and-buying-time-071
    basis_grade: C
  - rule: record-not-act
    module: task
    when: a chore is checked off or left unchecked
    action: treat the check as a record; an unchecked item is unknown, not missed
    never: infer neglect from a missing check; use streak or shortfall language
    constant: false
    basis: task-management/record-is-not-behaviour-009
    basis_grade: B
  - rule: damp-routes-to-moisture
    module: routine
    when: a task or note mentions damp, condensation, mould or a musty smell
    action: route to moisture and ventilation (airing, drying, ventilation system use) rather than adding a more frequent wiping task
    never: treat mould as solved by a cleaning cadence; recommend mould air testing
    constant: false
    basis: home/dampness-mould-respiratory-001
    basis_grade: B
refraction_notes:
  - note: >
      THE RULES ARE ROUTING, THE CONSTANTS ARE CHOICES. Three rules carry a
      chosen value or ordering with no evidence behind it (starter cadence,
      "a few completions" before switching to the record, the
      drop-reassign-outsource order). Speak them as the module's rule, never
      as a finding, and expose them as settings.
    grade: D
  - note: >
      HYGIENE AND COMFORT ARE DIFFERENT TASK KINDS. Event-hygiene tasks are
      the only ones with an infection rationale, and that rationale is an
      expert consensus rather than a trial result. Calendar tasks express the
      household's standard of tidiness, which is legitimate and is the
      household's own choice. The module never lets an over-capacity cut
      remove an event-hygiene task.
    grade: D
  - note: >
      ESTIMATES RUN SHORT, RECORDS DO NOT. People underestimate their own
      task durations, and prompting pessimism does not correct it; the
      household's own past completions are the better base rate. The
      threshold for switching from stated to recorded is a constant.
    grade: B
  - note: >
      NO LEDGER, NO STREAK, NO NAMING. Every rule above that touches who did
      what is constrained by the owner's standing no-nag directive and by
      the fairness finding: what tracked relationship satisfaction was a
      perception, which a tally cannot measure and can inflame.
    grade: D
  - note: >
      NOT COVERED. Childcare scheduling, eldercare, and any Korean-specific
      split norms are outside these rules; no Korean measurement of cognitive
      labour or perceived fairness was located (GAPS.md).
    grade: D
claim: >
  Nine routing rules for household routine and task modules. Assign recurring
  tasks whole (one owner from noticing to follow-up) and let the module hold
  the reminder and the done-check. Tag each task as event-hygiene (fires on a
  risk moment such as food handling, toilet use or illness in the home) or
  calendar-comfort (fires on an interval the household sets), and never call
  an interval medically required. Ask for intervals rather than assert them.
  Size chore durations from the household's own record once one exists,
  because stated estimates run short. Reserve household labour as real hours
  in any plan. When load exceeds stated capacity, offer lowering a comfort
  standard, then reassigning a whole task, then outsourcing, and never cut a
  hygiene task. Fairness is asked, never computed or tallied. A check is a
  record, not proof of the act. Damp routes to moisture and ventilation, not
  to more wiping. The rules restate graded rows; the ordering and every
  default value are product constants.
reasoning: >
  Each rule cites the row it rests on and that row's support for the specific
  point. Two rules inherit trial-level support (duration-from-record from the
  planning-fallacy row; record-not-act from the photosensor diary trial), two
  inherit measurement or strong observational support (the household block
  from the national time-use diary; damp from the WHO-level dampness row),
  one inherits cross-sectional support (fairness-is-asked), and the rest are
  design reasoning from definitions or expert consensus. The headline grade is
  the bottom band because the set, its order and its constants are judgement,
  matching the posture of exercise/caution-severity-ladder-056.
---

# home/routine-task-rules-073 -- 집안일 루틴·할 일 모듈이 읽는 규칙

**한 줄 그림:** 반복되는 집안일은 통째로 한 사람에게 맡기고, 알림과 확인은 시스템이 든다. 위생은
위험한 순간에, 나머지 주기는 그 집이 정한다. 공평함은 묻지 계산하지 않는다.

## The rules

| Rule | Module | Does | Never | Constant | Basis (grade for this rule) |
|---|---|---|---|---|---|
| whole-task-owner | both | one owner, notice to follow-up; module holds reminder and check | mental-load score | no | 070 (D) |
| task-kind | routine | event-hygiene vs calendar-comfort | interval as health requirement | no | 072 (D) |
| cadence-source | routine | ask once; labelled starter interval | health reason for it | yes | 072 (D) |
| duration-from-record | task | own logged durations as base rate | pessimism prompt as fix | yes | task-management 001 (B) |
| household-block-is-real-time | both | housework as hours in the plan | housework as slack | no | 013 (B) |
| over-capacity-order | both | lower standard -> reassign -> outsource | cut a hygiene task | yes | 071 (D) |
| fairness-is-asked | both | household's own agreement is the target | 50/50 score, tally, naming | no | 071 (C) |
| record-not-act | task | unchecked = unknown | streaks, inferred neglect | no | task-management 009 (B) |
| damp-routes-to-moisture | routine | moisture and ventilation | more wiping, mould testing | no | 001 (B) |

## 한국어 요약 (답변용)

- 반복되는 집안일은 "누가 정하고 누가 한다"로 쪼개지 않고, 알아채기부터 챙기기까지 한 사람이 통째로
  맡는다. 미리 알려 주기와 끝났는지 확인하기는 시스템이 맡는다.
- 집안일은 두 종류로 나눈다. 위험한 순간에 하는 위생 일(음식 손질, 화장실, 아픈 가족, 자주 만지는
  곳 등)과 그 집이 정한 주기로 하는 깔끔함 일. 어떤 주기도 "건강상 꼭 필요하다"고 말하지 않는다.
- 주기는 한 번 묻는다. 답이 없으면 "시작용 주기, 마음대로 바꾸세요"라고 붙여서 쓴다. 거절하면 다시
  묻지 않는다.
- 걸리는 시간은 본인 추정보다 실제 기록을 쓴다. 사람은 자기 일 시간을 짧게 잡고, "비관적으로
  생각해 보라"고 해도 잘 고쳐지지 않는다.
- 하루·한 주 계획에서 집안일은 빈 시간이 아니라 몇 시간짜리 실제 블록이다. 크기는 그 집의 기록이나
  말로 정하고, 전국 평균을 한 사람에게 대지 않는다.
- 감당할 양을 넘으면 깔끔함 기준 낮추기 → 일 통째로 넘기기 → 돈 주고 맡기기 순으로 제안한다. 위생
  일은 줄이지 않는다.
- 공평함은 묻는다. 반반 점수, 누가 더 했는지 집계, 누가 밀렸는지 이름 부르기는 하지 않는다.
- 체크는 기록일 뿐이다. 체크가 없으면 "안 했다"가 아니라 "모른다"이다. 연속 기록 같은 말은 쓰지
  않는다.
- 습기·결로·곰팡이 얘기가 나오면 더 자주 닦기가 아니라 습기 관리와 환기로 보낸다.
- 순서와 기본값(시작용 주기, 기록으로 바꾸는 기준, 제안 순서)은 제품이 정한 규칙이다. 그렇게 말한다.
