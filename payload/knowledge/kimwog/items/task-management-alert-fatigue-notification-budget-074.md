---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-07 (reminder-lead-time sprint, dispatch
# kw-sc-reminder-lead-time). The COST side of reminders: 072 (released v37,
# from the kw-schedule-time sprint) says a reminder helps; this row says what each extra one
# costs and what the evidence says about volume, repeats and batching.
# What was read: Ancker et al. 2017 in full text (PMC open-access copy,
# 2026-10-07); Stothart et al. 2015 abstract (OpenAlex); Fitz et al. 2019
# abstract (Semantic Scholar); Pielot & Rello 2017 abstract (Semantic
# Scholar). Kushlev, Proulx & Dunn 2016 (CHI, "Silence your phones") was seen
# only through press coverage and is NOT cited. No effect size beyond the
# abstracts is quoted for the three abstract-only sources.
# CROSS-BRANCH LINKS: task-management/*-070, -072 and -073 shipped in v37 with
# those numbers (no renumber); this row kept 074 at the v38 merge.
id: task-management/alert-fatigue-notification-budget-074
domain: task-management
grade: C (direction from a 112-clinician EHR cohort, one lab experiment and one randomised field experiment on self-report outcomes; no trial of a personal reminder budget)
lane: "@behavioral-productivity"
locale: universal
as_of: 2015-2019
contested: no
sources:
  - "https://doi.org/10.1186/s12911-017-0430-8"  # Ancker JS, Edwards A, Nosal S, Hauser D, Mauer E, Kaushal R. Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical decision support system. BMC Medical Informatics and Decision Making 2017;17(1):36. Full text read 2026-10-07: retrospective cohort, 112 primary-care clinicians, 2010-2013, 1,266,325 reminders (BPAs) and 326,203 drug alerts over 430,803 encounters; median acceptance ~22% for reminders, <1% for drug alerts; each additional reminder per encounter IRR 0.70 for acceptance; each 5-point rise in the share of within-patient repeats IRR 0.90; no association with workload (patients, encounters); newly deployed reminders showed no decline over time (no desensitisation signal)
  - "https://doi.org/10.1037/xhp0000100"  # Stothart C, Mitchum A, Yehnert C. The attentional cost of receiving a cell phone notification. Journal of Experimental Psychology: Human Perception and Performance 2015;41(4):893-897. PMID 26121498. Abstract read 2026-10-07: notifications alone, not answered, significantly disrupted an attention-demanding task, comparable in magnitude to active phone use. The "three times the error probability" figure in press coverage was NOT found in the abstract and is not used
  - "https://doi.org/10.1016/j.chb.2019.07.016"  # Fitz N, Kushlev K, Jagannathan R, Lewis T, Paliwal D, Ariely D. Batching smartphone notifications can improve well-being. Computers in Human Behavior 2019;101:84-94. Abstract read 2026-10-07: randomised field experiment, n=237, arms as-usual / batched three times a day / none; batched arm reported more attention, productivity, mood and control, less stress, fewer interruptions; the no-notification arm gained little and reported more anxiety and fear of missing out. Outcomes are daily-diary self-report. The abstract also says "lower productivity" for the batched group, contradicting its own preceding sentence; the full text was not read to settle it
  - "https://doi.org/10.1145/3098279.3098526"  # Pielot M, Rello L. Productive, anxious, lonely: 24 hours without push notifications. MobileHCI 2017. Abstract read 2026-10-07: 30 volunteers, one day with all notification alerts off vs a baseline day; less distracted and more productive by self-report, but some anxious about responsiveness and less connected
  - "task-management/momentary-interruption-error-cost-005"  # Altmann 2014: seconds-long interruptions cost place-keeping -- the per-alert cost mechanism
  - "task-management/interruption-resumption-measured-004"  # interrupted work is often not resumed the same day
  - "task-management/self-report-vs-log-divergence-008"  # why Fitz/Pielot self-report outcomes are discounted
  - "task-management/reminder-lead-time-prospective-memory-072"  # the benefit side: remind-at-all, two-stage, re-fire once (v37)
  - "task-management/schedule-buffer-overdue-rules-073"  # carry-forward-not-pile-up: one overdue prompt per item per day (v37)
  - "task-management/curator-checklist-016"  # self-report standing in for behaviour is an auto-downgrade trigger
alert_rules:
  - rule: every-alert-has-a-cost
    value: an alert is not free even when ignored; the module counts alerts it sends and treats each one as spending attention
    basis: Stothart 2015 (unanswered notifications disrupted a task); 005 (seconds-long interruptions cost place)
    basis_grade: C
  - rule: no-repeat-of-same-item
    value: the same item does not alert again unless its state changed (new time, new travel estimate, unacknowledged final cue per 072); a repeat that carries nothing new is dropped
    basis: Ancker 2017 (a higher share of within-patient repeats lowered acceptance, IRR 0.90 per 5 points)
    basis_grade: C
  - rule: fewer-per-moment
    value: when several alerts fall in the same window, send one message that lists them, highest consequence first, not one alert each
    basis: Ancker 2017 (each extra reminder in the same encounter lowered acceptance, IRR 0.70)
    basis_grade: C
  - rule: batch-the-non-urgent
    value: alerts with no time-critical action (reviews, stalled items, summaries) go into fixed digest slots; the number and times of slots are product settings
    basis: Fitz 2019 (three-a-day batching beat as-usual on self-report); slot count is a setting
    basis_grade: C
  - rule: do-not-go-silent
    value: time-critical cues (prep start, departure, a hard-start appointment) are never batched or suppressed by the budget; the budget cuts the rest first
    basis: Fitz 2019 and Pielot 2017 (no notifications at all brought anxiety, not benefit); 072 remind-at-all
    basis_grade: C
  - rule: budget-is-a-setting
    value: the daily alert cap, the digest times and the quiet hours are product settings and are spoken as such; no study gives a per-day number for a personal assistant
    basis: searched absence (GAPS.md, task-management)
    basis_grade: D
refraction_notes:
  - note: >
      THE STRONGEST NUMBER IS CLINICAL, NOT PERSONAL. Ancker et al. measured
      what clinicians did with more than a million alerts: acceptance fell
      by about 30% for each extra reminder in the same encounter and by
      about 10% for each 5-point rise in the share of repeats. The volume
      and repetition dose is real behaviour, not self-report. But the
      population is doctors and nurse practitioners at work, and the alerts
      were often uninformative. The direction carries to a personal
      assistant; the size does not.
    grade: C
  - note: >
      OVERLOAD, NOT WEAR-OUT. In the same study newly deployed reminders did
      not lose acceptance over time, and workload did not matter; what
      mattered was how many alerts arrived together and how many were
      repeats. For a module that means the fix is fewer and less repetitive
      alerts at each moment, not rotating the wording to keep it fresh.
    grade: C
  - note: >
      BATCHING HELPED, SILENCE DID NOT. Fitz et al. randomised 237 people:
      three digests a day beat normal delivery, while no notifications at
      all brought anxiety and fear of missing out. Pielot and Rello saw the
      same split in a one-day study of 30. Both rest on self-report, which
      this lane discounts (008, 016), and other papers co-authored by one
      Fitz author have been retracted (Shu et al. 2012, PNAS, retracted 2021;
      the v37 GAPS.md note on Ariely and Wertenbroch 2002). Nothing is
      alleged about this paper. Carried at C: the shape is
      plausible and consistent, the magnitude is not shipped.
    grade: C
  - note: >
      NO KOREAN DATA. No Korean study of notification volume, batching or
      alert fatigue in personal reminders was located. Transfer is untested,
      not shown to fail.
    grade: D
claim: >
  Every alert costs attention, and more alerts at once or repeats of the
  same alert get acted on less. In a retrospective cohort of 112 primary-care
  clinicians and over 1.2 million reminders (Ancker et al. 2017), the
  likelihood of accepting a reminder fell by about 30% for each additional
  reminder in the same encounter (IRR 0.70) and by about 10% for each
  5-percentage-point rise in the share of repeated reminders (IRR 0.90).
  Workload did not matter, and newly deployed reminders did not lose
  acceptance over time. In the laboratory, phone notifications that were not
  answered still disrupted an attention-demanding task (Stothart et al.
  2015). In a randomised field experiment (n=237; Fitz et al. 2019),
  notifications batched three times a day beat normal delivery on
  self-reported attention, mood, stress and sense of control, while no
  notifications at all brought more anxiety and fear of missing out. A
  one-day study of 30 people found the same split (Pielot & Rello 2017).
  No study gives a daily alert budget for a personal assistant.
reasoning: >
  The volume and repetition result is behavioural and large-sample but
  comes from clinicians receiving decision-support alerts. The batching
  result is randomised but self-reported. The notification-cost result is a
  single laboratory study read at abstract level. Under
  task-management/curator-checklist-016 that is a third-band row: the
  direction is consistent across three designs; the magnitudes belong to
  their settings. The rules turn the direction into module behaviour (drop
  repeats, merge co-timed alerts, batch the non-urgent, never batch the
  time-critical) and label every number a setting. Structured alert_rules
  are for the lifekit schedule/task module, alongside the reminder_rules in
  072 and the travel/prep reminder_rules in 075.
---

# task-management/alert-fatigue-notification-budget-074

A reminder helps (see task-management/reminder-lead-time-prospective-memory-072).
But each alert costs attention, and too many get ignored.

- **More at once, less acted on.** In a study of 112 primary-care clinicians
  and more than a million reminders, each extra reminder in the same visit
  cut the chance of acting on reminders by about 30%. Each 5-point rise in
  the share of repeats cut it by about 10%. How busy the clinician was did
  not matter, and new reminders did not wear out over months. The problem
  was overload at the moment, not boredom over time.
- **Ignored still costs.** In a laboratory task, phone notifications that
  were never answered still hurt performance.
- **Batching beat both extremes.** In a randomised trial of 237 phone users,
  getting notifications in three digests a day beat normal delivery on
  attention, mood and stress (self-reported). Getting none at all did not
  help much and made people anxious about missing things.

What this means for a reminder module: drop repeats that carry nothing new,
merge alerts that land together, put non-urgent ones in digests, and never
hold back the time-critical cue (prep start, departure, hard-start
appointment). No study gives the right number of alerts per day for a
personal assistant; the cap and the digest times are settings.

## Rules for the schedule/task module (frontmatter `alert_rules`)

| Rule | What the module does | Basis |
|---|---|---|
| every-alert-has-a-cost | count alerts sent; each spends attention | Stothart 2015; 005 |
| no-repeat-of-same-item | re-alert only on changed state (or 072's one re-fire) | Ancker 2017 |
| fewer-per-moment | co-timed alerts merge into one message, highest consequence first | Ancker 2017 |
| batch-the-non-urgent | reviews, stalled items, summaries go to digest slots | Fitz 2019 |
| do-not-go-silent | prep, departure, hard-start cues are never batched | Fitz 2019; Pielot 2017; 072 |
| budget-is-a-setting | daily cap, digest times, quiet hours are settings | searched absence |

## 한국어 요약 (답변용)

- 알림은 도움이 되지만 공짜가 아니다. 무시한 알림도 집중을 깬다는 실험 결과가 있다.
- 한꺼번에 많이 오거나 같은 알림이 반복되면 덜 따른다. 의사 112명이 받은 알림 120여만 건을 본
  연구에서, 같은 진료 중 알림이 하나 늘 때마다 따를 확률이 약 30% 줄었고, 반복 알림 비율이 5%p
  늘 때마다 약 10% 줄었다. 바쁜 정도와는 관계없었고, 새 알림이 시간이 지나며 무뎌지지도 않았다.
- 그래서 바뀐 것이 없는 같은 일정은 다시 알리지 않고, 같은 때 겹치는 알림은 하나로 묶어 중요한
  것부터 보여 준다.
- 급하지 않은 알림(검토, 오래 멈춘 일, 요약)은 정해진 시간에 모아서 보낸다. 237명 무작위 연구에서
  하루 세 번 모아 받은 쪽이 평소대로 받은 쪽보다 집중·기분·스트레스가 나았다(자기 보고).
- 알림을 아예 끄면 오히려 불안해졌다. 준비 시작, 출발, 시작 시각이 정해진 약속 알림은 묶거나
  줄이지 않는다.
- 하루 몇 개가 적당한지는 연구된 바 없다. 하루 상한, 모아 보내는 시각, 방해 금지 시간은 제품
  설정이라고 말한다.
