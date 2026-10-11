---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (schedule/task-time sprint, dispatch
# kw-schedule-time). The engine-readable synthesis for the lifekit
# schedule/task module, same posture as exercise/caution-severity-ladder-056:
# a routing rule, not a primary finding. Every rule names the row it rests on;
# every number is labelled a product constant. Reminder rules live in 072,
# estimate rules in 070, breakdown rules in 071; this row holds BUFFERS
# between appointments and OVERDUE handling, which no located primary study
# prescribes for an individual calendar.
#
# What was read for the buffer half: Kuiper, Mandjes, de Mast & Brokkelkamp
# (Decision Sciences) in full text, 2026-10-06; Robinson & Chen 2003 abstract
# (OpenAlex). Both are clinic-scheduling operations research. The step from a
# clinic session to one person's day is an argument, stated as such.
id: task-management/schedule-buffer-overdue-rules-073
domain: task-management
grade: D (synthesis rule; the buffer mechanism is operations-research math, its transfer to a personal calendar and every constant are product judgement)
lane: "@behavioral-productivity"
locale: universal
as_of: 2026
contested: no
sources:
  - "https://doi.org/10.1111/deci.12517"  # Kuiper A, Mandjes M, de Mast J, Brokkelkamp R. A flexible and optimal approach for appointment scheduling in healthcare. Decision Sciences 2023;54(1):85-100 (online 2021). Full text read 2026-10-06: remaining variability is absorbed by waiting or by idle capacity, which 'act as communicating vessels' (variability buffering law, Hopp & Spearman); optimal slots are not equidistant; larger variability in service time makes the optimal slot profile more pronounced
  - "https://doi.org/10.1080/07408170304367"  # Robinson LW, Chen RR. Scheduling doctors' appointments: optimal and empirically-based heuristic policies. IIE Transactions 2003;35(3):295-307. Abstract read: spacing appointments trades waiting time (too close) against idle time (too far)
  - "source:cooking/duration-estimate-asymmetry-018 -- a timeline summed from stated durations omits transitions, so it is a lower bound; buffer is added, never subtracted"
  - "task-management/duration-from-logged-actuals-070"  # logged actuals supply the overrun spread a buffer is sized from
  - "task-management/planning-fallacy-own-estimates-001"  # 70.3% missed their own best estimate: an overdue own estimate is the expected case
  - "task-management/interruption-resumption-measured-004"  # peripheral work resumed same day only 43.8%
  - "task-management/record-is-not-behaviour-009"  # an unchecked box is not an undone task
  - "task-management/target-corruption-completion-metrics-010"  # do not turn overdue counts into a score
  - "task-management/no-block-length-or-task-count-evidence-015"  # no evidenced number for any interval
  - "task-management/reminder-lead-time-prospective-memory-072"  # where reminder timing lives
  - "source:learning-habits/lapse-is-not-a-reset-015 -- a missed stretch is a delay, not a deletion"
  - "framework:GRADE -- the buffer DIRECTION (variable events need more slack; slack costs idle time) is model-derived; the overdue rules are the lane's measurement fences applied to a task store; all minutes, counts and day thresholds are product constants with no direct evidence"
buffer_rules:
  - rule: travel-is-not-buffer
    value: travel and setup between two events are computed as their own block from location and stated prep; buffer sits on top of them and never absorbs them
    basis: cooking 018 (stated durations omit transitions; lower bound)
    basis_grade: D
  - rule: buffer-has-a-price
    value: slack is idle time when things run on time; no slack is lateness that carries into every later event; present the choice, do not hide it
    basis: Kuiper 2023; Robinson & Chen 2003 (waiting vs idle trade-off)
    basis_grade: C
  - rule: size-from-overrun-spread
    value: buffer after an event grows with how much that kind of event has overrun in the owner's log (070 actuals vs scheduled end); low-spread events get less
    basis: Kuiper 2023 (larger service-time variability -> longer optimal slot); 070
    basis_grade: D
  - rule: protect-hard-starts
    value: put slack before events with a fixed start and another party (appointment, meeting, transport departure); events the owner can start late take less or none
    basis: product rule; lateness cost falls on the hard-start event
    basis_grade: D
  - rule: default-without-history
    value: with no logged overruns for the event class, use a product default (15 minutes, a convention) and label it a setting
    basis: no evidenced interval (015); no peer-reviewed source for a personal between-meeting buffer located
    basis_grade: D
  - rule: never-negative
    value: a conflict is never resolved by shrinking travel, prep or a logged duration; move or drop an event instead
    basis: cooking 018; cooking/timeline-backward-pass-016 invariant
    basis_grade: D
overdue_rules:
  - rule: overdue-is-a-re-estimate-event
    value: when an own-estimated due date passes, ask for a new date and show the logged actuals for that class (070); do not frame it as a failure
    basis: 001 (most own estimates are missed); 070
    basis_grade: B
  - rule: unchecked-is-not-undone
    value: an open item past its date is unknown state; ask "done, moved, or dropped?" before treating it as not done
    basis: 009 (record and action come apart)
    basis_grade: B
  - rule: hard-vs-soft-due
    value: items with an external consequence (bill, filing, another person waiting) keep their date and escalate; self-set target dates roll on re-estimate
    basis: product rule
    basis_grade: D
  - rule: carry-forward-not-pile-up
    value: one overdue prompt per item per day at most; batch the rest into one review line; never re-list every overdue item on every view
    basis: product constant; 010 (counts become targets); learning-habits 015 (backlog is a delay)
    basis_grade: D
  - rule: stalled-item-surface
    value: an item with no activity past a product threshold (14 days, a convention) is surfaced once for keep / reschedule / drop; there is no evidenced threshold
    basis: GAPS.md task-management (no source prescribes when to surface a stalled item); 004 (peripheral work often not resumed same day)
    basis_grade: D
  - rule: no-overdue-score
    value: overdue counts are not shown as a streak, ratio or grade of the owner
    basis: 010
    basis_grade: D
refraction_notes:
  - note: >
      THE DIRECTION IS THE EVIDENCE, THE MINUTES ARE NOT. That slack trades
      against idle time and that more variable events deserve more of it is
      the structure of the optimal clinic schedule (Kuiper et al.; Robinson &
      Chen). The 15-minute default, the one-prompt-per-day cap and the 14-day
      stall threshold are product constants. Speak them as the plan's
      settings, never as research.
    grade: D
  - note: >
      CLINIC MATH, PERSONAL DAY. The operations-research results optimise a
      provider's session of many patients with known duration distributions.
      An individual's day has fewer events and a different cost of lateness.
      What carries is the qualitative structure, not any slot length.
    grade: C
  - note: >
      AN OVERDUE OWN ESTIMATE IS THE EXPECTED CASE. In the study behind
      task-management/planning-fallacy-own-estimates-001, fewer than a third
      finished inside their own best estimate. A module that treats every
      missed self-set date as a lapse misreads the base rate. The useful act
      is a better second estimate, from logged actuals.
    grade: B
  - note: >
      AN OPEN BOX IS UNKNOWN, NOT UNDONE. Following
      task-management/record-is-not-behaviour-009, an unchecked item past its
      date may be done and unrecorded. Ask once; do not infer.
    grade: B
claim: >
  Buffers and overdue handling for a personal schedule/task module follow a
  small rule set. Buffers: travel and setup are computed as their own block,
  and buffer sits on top; slack always costs idle time when things run on
  time and its absence costs lateness that carries forward, so the trade is
  shown, not hidden; buffer after an event grows with that kind of event's
  logged overrun spread; slack protects events with a fixed start and another
  party; with no history a product default applies; and a conflict is never
  solved by shrinking travel, prep or a logged duration. Overdue: a passed
  self-estimated date is a re-estimate event shown against logged actuals,
  not a failure; an unchecked item is unknown until asked; external-
  consequence dates escalate while self-set dates roll; prompts are capped
  and batched; a stalled item is surfaced once after a product threshold;
  overdue counts are never scored. The directions rest on graded rows and on
  clinic-scheduling mathematics; every number is a product constant.
reasoning: >
  No located primary study prescribes a buffer between one person's
  appointments or a rule for handling their overdue tasks, and the lane's
  standing failure mode (task-management/no-block-length-or-task-count-
  evidence-015) is a fluent invented interval next to sourced material. So
  this row does what 056 does for the caution ladder: it routes. The buffer
  directions come from the waiting-versus-idle structure that clinic
  scheduling research proves for sessions with variable service times, plus
  the lower-bound arithmetic in cooking 018. The overdue directions are the
  lane's own measurement fences (001 base rate, 009 record-not-behaviour, 010
  target corruption) applied to a task store. Two overdue rules inherit their
  basis rows' grade; everything else is D. Structured buffer_rules and
  overdue_rules are for the lifekit schedule/task module.
---

# task-management/schedule-buffer-overdue-rules-073 -- 일정 사이 여유와 기한 지난 일 처리 규칙

**한 줄 그림:** 여유 시간은 공짜가 아니고, 기한이 지난 일은 실패가 아니라 다시 추정할 때다.

## Buffers between appointments (frontmatter `buffer_rules`)

| Rule | What the module does | Basis |
|---|---|---|
| travel-is-not-buffer | travel and setup are their own block; buffer on top | cooking 018 |
| buffer-has-a-price | show the trade: slack = idle when on time; none = carried lateness | clinic scheduling math |
| size-from-overrun-spread | more buffer after event kinds that overrun more in the log | Kuiper et al.; 070 |
| protect-hard-starts | slack before fixed-start events with another party | product rule |
| default-without-history | 15 min (setting) when no log exists | none evidenced (015) |
| never-negative | never shrink travel, prep or a logged duration to fit | cooking 016/018 |

## Overdue handling (frontmatter `overdue_rules`)

| Rule | What the module does | Basis |
|---|---|---|
| overdue-is-a-re-estimate-event | ask for a new date, show logged actuals | 001, 070 |
| unchecked-is-not-undone | ask "done, moved, or dropped?" first | 009 |
| hard-vs-soft-due | external-consequence dates escalate; self-set dates roll | product rule |
| carry-forward-not-pile-up | at most one prompt per item per day; batch the rest | product constant |
| stalled-item-surface | no activity for 14 days (setting): surface once | no evidenced threshold |
| no-overdue-score | no streaks, ratios or grades from overdue counts | 010 |

## 한국어 요약 (답변용)

- 이동 시간과 준비 시간은 따로 계산하고, 여유 시간은 그 위에 더한다. 이동 시간을 여유로 치지 않는다.
- 여유 시간은 공짜가 아니다. 일정이 제때 끝나면 빈 시간이 되고, 여유가 없으면 늦어진 게 뒤 일정에
  계속 밀린다. 이 맞바꿈을 사용자에게 보여 준다.
- 기록상 자주 늦게 끝나는 종류의 일정 뒤에는 여유를 더 두고, 거의 제때 끝나는 일정 뒤에는 덜 둔다.
- 다른 사람과 시작 시각이 정해진 일정(약속, 회의, 출발 시각) 앞을 먼저 지킨다.
- 기록이 없으면 15분을 쓰되, 연구로 정해진 값이 아니라 설정이라고 말한다.
- 일정이 겹치면 이동·준비·기록된 소요 시간을 줄여서 맞추지 않는다. 일정을 옮기거나 뺀다.
- 스스로 정한 기한이 지난 건 흔한 일이다(자기 예측 안에 끝낸 사람이 3분의 1도 안 됐다). 실패로
  다루지 말고, 기록된 실제 시간을 보여 주며 새 날짜를 묻는다.
- 체크 안 된 일이 안 한 일이라는 뜻은 아니다. "했어요, 미뤘어요, 뺐어요?"를 먼저 묻는다.
- 공과금·서류 제출·남이 기다리는 일처럼 밖에서 정한 기한은 유지하고 강조한다. 스스로 정한 날짜는
  다시 잡는다.
- 지난 일은 하루에 한 항목당 한 번까지만 묻고, 나머지는 한 줄로 묶는다. 14일(설정) 동안 손대지 않은
  일은 한 번 꺼내서 유지·변경·삭제를 묻는다.
- 기한 넘긴 개수를 연속 기록이나 점수로 만들지 않는다.
