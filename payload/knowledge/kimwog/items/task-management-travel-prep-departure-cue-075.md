---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-07 (reminder-lead-time sprint, dispatch
# kw-sc-reminder-lead-time). How the module computes WHEN the prep and
# departure cues fire. 072 (v37, kw-schedule-time sprint) says the last
# reminder lands at departure time = start - travel - prep; 073 says travel
# is its own block, not buffer. This row says how to size travel and prep so
# that departure time is not a mean that is late half the time, and why the
# cue has to be external.
# What was read: FHWA 2005 reliability report (agency web page, 2026-10-07);
# Fosgerau & Karlstrom 2010 abstract (RePEc); Tenenboim & Shiftan 2018
# abstract (RePEc); Brunec et al. 2017 in full text (PMC); Roy & Christenfeld
# 2008 abstract (Europe PMC); Kvavilashvili et al. 2009 introduction (author
# repository PDF), used ONLY for the field's time-based vs event-based
# distinction, not for its age findings. Small 1982 (the scheduling model
# Fosgerau builds on) was not read and is not cited.
# CROSS-BRANCH LINKS: task-management/*-070, -072 and -073 shipped in v37 with
# those numbers (no renumber); this row kept 075 at the v38 merge.
id: task-management/travel-prep-departure-cue-075
domain: task-management
grade: C (the reliability-planning arithmetic is standard transport engineering; the estimation-bias evidence is mixed and small-sample; the cue argument is laboratory-derived; every percentile and minute is a product setting)
lane: "@behavioral-productivity"
locale: universal
as_of: 2005-2018
contested: no
sources:
  - "https://ops.fhwa.dot.gov/publications/tt_reliability/TTR_Report.htm"  # US Federal Highway Administration. Travel Time Reliability: Making It There On Time, All The Time. 2005 (December). Read 2026-10-07: commuters planning on average travel time "will be late half the time and early the other half"; buffer index = extra time travellers add to the average to arrive on time; planning time index = near-worst-case (95th percentile) time against free flow
  - "https://doi.org/10.1016/j.trb.2009.05.002"  # Fosgerau M, Karlstrom A. The value of reliability. Transportation Research Part B 2010;44(1):38-49. Abstract read 2026-10-07: in a scheduling model of an activity of random duration (e.g. congested travel), maximal expected utility is linear in the mean AND the standard deviation of trip duration, whatever the shape of the standardised distribution
  - "https://doi.org/10.1007/s11116-016-9757-8"  # Tenenboim E, Shiftan Y. Accuracy and bias of subjective travel time estimates. Transportation 2018;45(3):945-969. Abstract read 2026-10-07: 174 respondents, pre-trip estimates for car trips to local shopping areas vs Waze times; 48% accurate; over-estimates 2.5 times as frequent as under-estimates; return-trip effect only for unfamiliar destinations; familiarity, trip frequency, toll use and direction predicted error
  - "https://doi.org/10.1016/j.cognition.2017.06.004"  # Brunec IK, Javadi AH, Zisch FE, Spiers HJ. Contracted time and expanded space: the impact of circumnavigation on judgements of space and time. Cognition 2017;166:425-432. Full text read 2026-10-07: two virtual-navigation experiments (n=23, n=20); remembered travel time underestimated on all routes (about 0.78 of actual for near-straight, 0.73 for routes requiring a detour), more so when the route doubled back
  - "https://doi.org/10.3758/PBR.15.1.202"  # Roy MM, Christenfeld NJS. Effect of task length on remembered and predicted duration. Psychonomic Bulletin & Review 2008;15(1):202-207. PMID 18605504. Abstract read 2026-10-07: tasks of 1-15 min; tasks under about 2 min were overestimated and longer ones underestimated, in both remembered and predicted duration
  - "https://doi.org/10.1080/09658210802194366"  # Kvavilashvili L, Kornbrot DE, Mash V, Cockburn J, Milne A. Differential effects of age on prospective and retrospective memory tasks in young, young-old, and old-old adults. Memory 2009;17(2):180-196. Introduction read (author repository copy) 2026-10-07 for one statement of the field's position only: time-based tasks have no external event signalling the moment to act, need more self-initiated processing and are considered harder than event-based tasks (citing Einstein et al. 1995; Kvavilashvili & Fisher 2007; Sellen et al. 1997). Those primaries were not read
  - "task-management/duration-from-logged-actuals-070"  # logged actuals before stated estimates; no blanket multiplier (v37)
  - "task-management/reminder-lead-time-prospective-memory-072"  # last reminder at the actionable moment; two-stage (v37)
  - "task-management/schedule-buffer-overdue-rules-073"  # travel-is-not-buffer, never-negative, protect-hard-starts (v37)
  - "task-management/alert-fatigue-notification-budget-074"  # time-critical cues are exempt from batching
  - "task-management/planning-fallacy-own-estimates-001"  # own estimates of multi-step work run short
  - "task-management/implementation-intentions-effect-shrinks-003"  # an if-then plan helps a little; the alert supplies the "if"
  - "source:cooking/duration-estimate-asymmetry-018 -- stated durations omit transitions; a summed timeline is a lower bound"
  - "source:cooking/timeline-backward-pass-016 -- compute backward from the fixed start"
reminder_rules:
  - rule: departure-from-a-high-percentile
    value: departure time = hard start - travel at a high percentile of its spread (not the mean) - prep - exit transition; the percentile is a product setting (default 90th, labelled)
    basis: FHWA 2005 (planning on the average is late about half the time); Fosgerau & Karlstrom 2010 (optimal scheduling depends on the spread as well as the mean)
    basis_grade: C
  - rule: travel-from-a-routing-source
    value: travel time comes from a routing service for the actual mode and departure hour, or from the owner's logged trips on that route; an owner-stated travel time is a stated estimate, shown with the routed figure beside it
    basis: Tenenboim & Shiftan 2018 (stated car-trip times mostly accurate or over, not reliably short); Brunec 2017 (remembered navigation time compressed); 070 source-order
    basis_grade: C
  - rule: no-direction-correction-for-travel
    value: do not shrink or pad an owner-stated travel time by a fixed factor; the direction of the error differs by person, route and familiarity
    basis: Tenenboim & Shiftan 2018 vs Brunec 2017 (opposite directions in different designs); 070 no-blanket-multiplier
    basis_grade: C
  - rule: unfamiliar-route-wider
    value: a first trip to a destination (no logged trip, unfamiliar to the owner) uses the routed figure with the wider percentile; say that it is a first trip
    basis: Tenenboim & Shiftan 2018 (estimate error depended on destination familiarity); FHWA (variability is what the buffer covers)
    basis_grade: D
  - rule: prep-from-logged-actuals
    value: prep (getting ready, packing, gear) uses logged prep actuals for that event type (070); with none, use the owner's stated prep and say it is a stated figure; long multi-step prep is the case most likely to run over
    basis: Roy & Christenfeld 2008 (tasks over ~2 min underestimated, very short ones overestimated); 001; cooking 018
    basis_grade: C
  - rule: prep-cue-then-departure-cue
    value: an event with prep gets a prep-start cue (departure - prep) and a departure cue; each names the one action to do now
    basis: 072 last-reminder-at-actionable-moment; Kvavilashvili 2009 intro (time-based intentions lack an external cue)
    basis_grade: C
  - rule: the-cue-is-the-event
    value: a departure or prep intention is never left to the owner's clock-watching; the module fires an external cue at the moment, which turns a time-based intention into an event-based one; a stated if-then plan does not replace the cue
    basis: Kvavilashvili 2009 intro (field position, primaries not read); 072 (Einstein 2003: if-then instructions did not help under load); 003
    basis_grade: C
  - rule: recompute-before-firing
    value: the departure cue re-reads live travel time shortly before it fires; if departure has moved earlier, send one updated cue with the new time; if it has moved later, update without a new alert
    basis: FHWA (day-to-day variability); 074 no-repeat-of-same-item (a changed time is new state, an unchanged one is not)
    basis_grade: D
  - rule: infeasible-says-so
    value: if departure time is already past when computed, say the owner will be late by the computed amount and offer to notify the other party; never shrink travel or prep to make it fit
    basis: 073 never-negative; cooking 016
    basis_grade: D
refraction_notes:
  - note: >
      THE AVERAGE IS LATE HALF THE TIME. This is the one solid piece: if
      travel time varies, leaving at start minus the average gets there late
      on roughly the slow half of days. Transport engineering plans on a high
      percentile for that reason (FHWA), and scheduling theory shows the
      best departure depends on the spread, not only the mean (Fosgerau and
      Karlstrom). The 90th percentile default is a setting; the direction is
      not.
    grade: C
  - note: >
      PEOPLE DO NOT RELIABLY UNDERESTIMATE TRAVEL. Unlike own-task estimates
      (001), stated car-trip times in Tenenboim and Shiftan were accurate
      about half the time and erred long more often than short. Remembered
      navigation time in a virtual town ran short (Brunec et al.). The
      direction depends on route, familiarity and design, so the module
      prefers a routed or logged figure and applies no correction factor.
      Both studies are small; neither sampled Korean public transport.
    grade: C
  - note: >
      PREP IS WHERE THE PLANNING FALLACY LIVES. Getting ready is a
      multi-step own task, the kind that runs short in 001 and whose
      transitions drop out of a summed estimate (cooking 018). Roy and
      Christenfeld found tasks over about two minutes underestimated and
      very short ones overestimated. Logged prep actuals (070) are the fix,
      not a padding factor.
    grade: C
  - note: >
      THE ALERT SUPPLIES THE "IF". An if-then plan helps a little (003), but
      a time-based intention has no event to trigger it; the field's
      standing position is that such tasks are harder than event-based
      ones. A cue at the moment is the event. This is an argument from a
      laboratory literature read here only through a review introduction.
    grade: D
  - note: >
      NO KOREAN TRAVEL-ESTIMATE DATA. No Korean study of stated vs actual
      travel time, or of departure reminders, was located. Seoul transit
      variability differs from US highways; the percentile is computed from
      the routing source, not carried from FHWA.
    grade: D
claim: >
  A departure reminder computed from average travel time is late about half
  the time. Transport agencies plan trips on a near-worst-case (95th
  percentile) travel time for this reason (FHWA 2005), and scheduling theory
  shows the best departure depends on both the mean and the spread of trip
  duration (Fosgerau & Karlstrom 2010). People's stated travel times are not
  reliably short: in 174 respondents' car-trip estimates checked against Waze, 48% of
  estimates were accurate and over-estimates were 2.5 times as common as
  under-estimates, with familiarity changing the error (Tenenboim & Shiftan
  2018). Remembered travel time in virtual navigation was compressed to
  about three-quarters of actual (Brunec et al. 2017). Prep is different:
  multi-minute own tasks tend to be underestimated (Roy & Christenfeld 2008),
  as own-task estimates generally are (001). A time-based intention such as
  "leave at 6:40" has no external event to trigger it and is harder to
  carry out than an event-based one. So the module computes departure from a
  high percentile of routed or logged travel time, takes prep from logged
  actuals, and fires an external prep-start cue and departure cue.
reasoning: >
  The variability arithmetic is not in dispute and is the core of the row,
  but its source is transport planning for road networks, and its transfer
  to one person's mixed-mode trips is an argument. The estimation-bias
  evidence is two small studies pointing in opposite directions, which is
  itself the finding that licenses the no-correction rule. The prep rule
  rests on 001 and 070 plus one short-task study. The external-cue rule
  rests on a field position read through a review introduction, not on the
  primaries. Under task-management/curator-checklist-016 that is a
  third-band row overall, with the cue argument and every constant below
  it. Structured reminder_rules extend 072's set for prep and travel alerts
  in the lifekit schedule/task module.
---

# task-management/travel-prep-departure-cue-075

When should "start getting ready" and "leave now" fire? The schedule module
works backward from the fixed start: start, minus travel, minus prep, minus
the time it takes to get out the door (see
task-management/reminder-lead-time-prospective-memory-072 and
task-management/schedule-buffer-overdue-rules-073). This row is about sizing
those pieces.

- **Do not plan travel on the average.** If a trip varies, leaving at start
  minus the average gets you there late on about half of days. Transport
  agencies plan on a near-worst-case time instead. Scheduling theory agrees:
  the best departure time depends on how much the trip varies, not only on
  how long it usually takes.
- **People are not reliably optimistic about travel.** In one study of
  car trips checked against a navigation app, about half of guesses were
  right and too-long guesses were more common than too-short ones.
  Familiarity with the destination changed the error. In a virtual
  navigation study, remembered times ran short. Small studies, opposite
  directions: use the routed or logged figure, and do not apply a
  correction factor to the owner's guess.
- **Prep is where the planning fallacy lives.** Getting ready is a
  multi-step task of your own, the kind people underestimate. Use logged
  prep times, not a padding factor.
- **The alert is the trigger.** "Leave at 6:40" has nothing in the world to
  remind you. An external cue at the moment turns it into something that
  happens to you, which is easier to act on than watching the clock. An
  if-then plan helps a little but does not replace the cue.

What is not known: the right percentile, and anything about Korean transit
or Korean travellers' estimates. The 90th-percentile default is a setting.

## Rules for the schedule/task module (frontmatter `reminder_rules`)

| Rule | What the module does | Basis |
|---|---|---|
| departure-from-a-high-percentile | departure = start - travel (90th pct, setting) - prep - exit | FHWA 2005; Fosgerau 2010 |
| travel-from-a-routing-source | routed or logged travel time; owner's guess shown as stated | Tenenboim 2018; Brunec 2017; 070 |
| no-direction-correction-for-travel | no fixed pad or shrink on stated travel | Tenenboim vs Brunec |
| unfamiliar-route-wider | first trip: wider percentile, say so | Tenenboim 2018 |
| prep-from-logged-actuals | logged prep for the event type; else stated, labelled | Roy 2008; 001; 070 |
| prep-cue-then-departure-cue | prep-start cue + departure cue, one action each | 072 |
| the-cue-is-the-event | never leave departure to clock-watching | Kvavilashvili 2009; 003 |
| recompute-before-firing | re-read live travel; re-alert only if departure moved earlier | FHWA; 074 |
| infeasible-says-so | already late: say by how much, offer to notify; never shrink | 073; cooking 016 |

## 한국어 요약 (답변용)

- 출발 시각은 시작 시각에서 이동 시간, 준비 시간, 나서는 데 걸리는 시간을 거꾸로 빼서 정한다.
- 이동 시간을 평균으로 잡으면 절반쯤은 늦는다. 교통 계획에서는 거의 최악에 가까운 시간(95번째
  백분위)으로 잡는다. 여기서는 기본 90번째 백분위를 쓰되, 연구로 정해진 값이 아니라 설정이라고
  말한다.
- 사람들이 이동 시간을 늘 짧게 잡는 것은 아니다. 174명이 말한 자동차 이동 시간을 내비 시간과 비교한 연구에서
  절반가량은 맞았고, 길게 잡은 경우가 짧게 잡은 경우의 2.5배였다. 그래서 사용자가 말한 이동
  시간에 일정 비율을 더하거나 빼지 않고, 길찾기 결과나 기록된 실제 이동 시간을 쓴다.
- 처음 가는 곳이면 더 넉넉한 백분위를 쓰고, 처음 가는 길이라고 알려 준다.
- 준비 시간은 내 일이라 짧게 잡기 쉽다. 기록된 실제 준비 시간을 쓰고, 없으면 사용자가 말한 값을
  쓰되 말한 값이라고 밝힌다.
- 준비가 필요한 일정은 "준비 시작" 알림과 "출발" 알림 두 개를 보낸다. 각 알림에는 지금 할 일 하나만
  적는다.
- "6시 40분에 나가야지"는 시계를 보며 스스로 떠올려야 하는 일이라 잊기 쉽다. 그 순간 알림이 울리게
  한다. 만약-그러면 계획은 조금 도움이 되지만 알림을 대신하지 못한다.
- 출발 알림 직전에 실시간 이동 시간을 다시 확인한다. 더 일찍 나가야 하면 새 시각으로 한 번 다시
  알리고, 늦게 나가도 되면 알림 없이 시각만 고친다.
- 이미 출발 시각이 지났으면 몇 분 늦을지 말하고 상대에게 알릴지 묻는다. 이동이나 준비 시간을 줄여서
  맞추지 않는다.
- 한국 대중교통이나 한국 사람의 이동 시간 추정에 관한 연구는 찾지 못했다.
