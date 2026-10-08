---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (schedule/task-time sprint, dispatch
# kw-schedule-time). Reminder timing for a calendar/task module. What was
# read: Einstein et al. 2003 in full text (PDF); Gurol-Urganci et al. 2013
# Cochrane abstract (Europe PMC); Steiner et al. 2018 abstract plus the
# results/discussion pages (AJMC); Lee et al. 2014 (Korea) abstract (OpenAlex).
# The Cochrane full text was NOT read: no subgroup or timing figure is taken
# from it. A 2026 target-trial emulation preprint on 24 h vs 72 h reminders
# surfaced in search and was NOT used (preprint, not read).
id: task-management/reminder-lead-time-prospective-memory-072
domain: task-management
grade: B (reminder-versus-none from a Cochrane meta-analysis of RCTs and a 54,066-patient RCT; the lead-time rules below it are C or product constants)
lane: "@behavioral-productivity"
locale: universal
as_of: 2003-2018
contested: no
sources:
  - "https://doi.org/10.1002/14651858.CD007458.pub3"  # Gurol-Urganci I, de Jongh T, Vodopivec-Jamsek V, Atun R, Car J. Mobile phone messaging reminders for attendance at healthcare appointments. Cochrane Database Syst Rev 2013;(12):CD007458. PMID 24310741. Abstract read 2026-10-06: 8 RCTs, 6,615 participants; text reminder vs none RR 1.14 (95% CI 1.03-1.26; 7 studies, 5,841; moderate quality); text vs phone call RR 0.99 (0.95-1.02); attendance 67.8% no reminder, 78.6% text, 80.3% phone. Authors: studies should report message timing in relation to the appointment
  - "https://www.ajmc.com/view/optimizing-number-and-timing-of-appointment-reminders-a-randomized-trial"  # Steiner JF, Shainline MR, Dahlgren JZ, Kroll A, Xu S. Optimizing number and timing of appointment reminders: a randomized trial. American Journal of Managed Care 2018;24(8):377-384. Read 2026-10-06: 54,066 patients, 25 US primary-care clinics; missed visits 4.4% with reminders 3 days AND 1 day before, 5.8% with 3-day only, 5.3% with 1-day only (P<.001 across arms); high-risk patients 20.5% vs 25.0% vs 24.2%; no effect on cancellations (P=.53); satisfaction unchanged. No pairwise 3-day vs 1-day test is reported
  - "https://doi.org/10.1037/1076-898X.9.3.147"  # Einstein GO, McDaniel MA, Williford CL, Pagan JL, Dismukes RK. Forgetting of intentions in demanding situations is rapid. Journal of Experimental Psychology: Applied 2003;9(3):147-162. Full text read 2026-10-06. Exp 1 (n=40): an intention held for 5, 15 or 40 s before it could be carried out was executed 92% of the time under standard load and 76% under divided attention; delay length had no effect; a 40 s delay with an interruption dropped it to .55 vs .80. Rehearsal and implementation-intention instructions did not help (power for a medium effect was not large)
  - "https://doi.org/10.15384/kjhp.2014.14.1.1"  # Lee JA, Kim WS, Bae MJ, et al. The effectiveness of short term mobile phone text reminders in improving compliance among hypertensive patients. Korean Journal of Health Promotion 2014;14(1):1 (end page not confirmed). Abstract read 2026-10-06: 15 Korean hospitals, 1,449 patients; advice texts every 2 weeks; control also received the next-visit date at week 10; attendance 92.8% vs 94.7% (P=.14), no difference on adherence or blood pressure
  - "task-management/implementation-intentions-effect-shrinks-003"  # if-then plans: smaller effect than famous, and Einstein 2003 found none under load
  - "task-management/interruption-resumption-measured-004"  # interruptions are frequent in real work; the condition under which held intentions fail
  - "task-management/momentary-interruption-error-cost-005"  # seconds-long interruptions cost place-keeping
  - "task-management/alert-fatigue-notification-budget-074"  # (v38) the COST side: repeats and co-timed alerts lower uptake; batch the non-urgent, never the time-critical final cue set here
  - "task-management/travel-prep-departure-cue-075"  # (v38) how to size the travel and prep terms of this row's departure-time formula, and why the cue must be external
reminder_rules:
  - rule: remind-at-all
    value: a dated commitment with another party gets a reminder by default
    basis: Gurol-Urganci 2013 (RR 1.14 vs none); Steiner 2018
    basis_grade: B
  - rule: two-stage-for-appointments
    value: appointments get a planning reminder days ahead (time to reschedule or prepare) AND a day-of or day-before reminder
    basis: Steiner 2018 (two reminders beat either single one)
    basis_grade: B
  - rule: last-reminder-at-actionable-moment
    value: the final reminder fires when the owner can act on it -- departure time (start minus travel minus prep), not a fixed number of minutes before the start
    basis: Einstein 2003 (an intention that cannot be acted on yet is fragile under load and interruption)
    basis_grade: C
  - rule: re-fire-after-interruption
    value: an unacknowledged final reminder repeats once at the next actionable moment; an acknowledged one does not
    basis: Einstein 2003 (interruption between cue and execution drops execution); product cadence
    basis_grade: D
  - rule: cue-not-advice
    value: reminder text names the action, place and time; it does not carry general advice
    basis: Lee 2014 (advice texts did not move attendance); Steiner/Gurol-Urganci messages were appointment cues
    basis_grade: C
  - rule: no-evidence-lead-minutes
    value: the exact lead in minutes, and 3 days vs 1 day as a single reminder, are product settings; speak them as settings
    basis: no head-to-head test located (Gurol-Urganci asks for timing to be reported; Steiner reports no pairwise test)
    basis_grade: D
refraction_notes:
  - note: >
      THE EFFECT IS REAL AND MODEST, AND IT SHRINKS WHEN BASELINE IS HIGH.
      Reminders lifted attendance from 67.8% to 78.6% in the Cochrane pool.
      In the Kaiser trial, where only about 5% missed, the second reminder
      cut misses by about a quarter in relative terms but around one
      percentage point absolute. In the Korean trial attendance was about 93%
      in both arms. An owner who rarely misses things gains little; the
      reminder earns its interruption cost on items the owner has missed
      before.
    grade: B
  - note: >
      HOLDING AN INTENTION IS FRAGILE EVEN OVER SECONDS. In Einstein et al.
      the length of the wait (5 to 40 s) did not matter; what mattered was
      load and an interruption between the cue and the chance to act. The
      transfer to a phone reminder is an argument: a reminder that fires
      while the owner cannot act asks them to hold the intention across
      whatever comes next. Hence the last reminder at the actionable moment.
    grade: C
  - note: >
      IF-THEN PLANS ARE NOT A SUBSTITUTE. Einstein et al. found no benefit of
      implementation-intention or rehearsal instructions under load, and
      task-management/implementation-intentions-effect-shrinks-003 records
      the effect as smaller than its famous size. An external cue does the
      job the plan is supposed to do.
    grade: C
  - note: >
      KOREAN DATA POINTS THE OTHER WAY ON CONTENT, NOT ON CUES. Lee et al.
      tested biweekly ADVICE texts, and the control arm also got a
      next-visit-date message, so it does not test reminder against none.
      What it shows is that health advice by text did not move attendance or
      blood pressure in Korean outpatients with a high baseline.
    grade: C
claim: >
  Reminders improve keeping appointments, two well-timed reminders beat one,
  and the last one should land when the person can act. A Cochrane review of
  eight RCTs (Gurol-Urganci et al. 2013) found text reminders raised
  attendance against no reminder (RR 1.14, 95% CI 1.03-1.26; 67.8% vs 78.6%),
  with phone calls no better than texts; the authors note that timing was
  not reported well enough to analyse. Steiner et al. (2018) randomised
  54,066 primary-care patients: reminders both 3 days and 1 day before cut
  missed visits to 4.4%, against 5.8% for a 3-day reminder alone and 5.3%
  for a 1-day reminder alone. No pairwise test separates the two single
  timings. Einstein et al. (2003) showed that an intention that must wait
  even 5 to 40 seconds before it can be carried out is lost more often under
  divided attention (76% vs 92% carried out) and after an interruption (.55
  vs .80). The wait length itself did not matter, and rehearsal and if-then
  instructions did not help. A Korean trial of biweekly advice texts (Lee
  et al. 2014) found no change in attendance against a 93-95% baseline. No
  located study sets the right lead time in minutes.
reasoning: >
  The reminder-versus-none and two-versus-one findings are randomised and
  large, which earns the second band under
  task-management/curator-checklist-016. They are about healthcare
  appointments with another party, which is the closest located analogue to
  a personal calendar commitment, and the transfer to self-set tasks is not
  tested. The actionable-moment rule rests on a laboratory paradigm with
  second-long delays and an argument about phones, so it is carried in the
  third band. Lead time in minutes and the single-reminder 3-day vs 1-day
  question are open, and the rules mark them as product settings. The
  structured reminder_rules are for the lifekit schedule/task module.
---

# task-management/reminder-lead-time-prospective-memory-072

Reminders help people keep appointments. The effect is real and modest, and
the evidence says more about how many reminders and when than about exact
minutes.

- **Reminders beat no reminders.** Eight randomised trials pooled by Cochrane:
  attendance 67.8% without a reminder, 78.6% with a text. A phone call did no
  better than a text.
- **Two beat one.** In a trial of 54,066 US primary-care patients, reminders
  3 days and 1 day before left 4.4% missing, against 5.8% and 5.3% for either
  one alone. The trial authors suggest the early one gives time to cancel or
  rearrange and the late one prompts the day itself; they did not test which.
- **The last reminder should land when the person can act.** In laboratory
  work by Einstein and colleagues, people asked to hold an intention for
  only 5 to 40 seconds dropped it more often when they were busy, and much
  more often when something interrupted them in between. How long they had
  to wait did not matter. Telling them to rehearse or to form an if-then plan
  did not help.

What is not known: the right number of minutes. No located trial compares lead
times in minutes, and the big trial did not test 3 days against 1 day for a
single reminder. A Korean trial sending biweekly health advice by text found
no change in attendance, which already sat at about 93%. Advice is not a cue,
and a high baseline leaves little to gain.

## Rules for the schedule/task module (frontmatter `reminder_rules`)

| Rule | What the module does | Basis |
|---|---|---|
| remind-at-all | dated commitments with another party get a reminder | Cochrane 2013 |
| two-stage-for-appointments | days-ahead planning reminder + day-of/day-before reminder | Steiner 2018 |
| last-reminder-at-actionable-moment | final reminder at departure time (start - travel - prep) | Einstein 2003 |
| re-fire-after-interruption | unacknowledged final reminder repeats once | Einstein 2003 + product |
| cue-not-advice | text names action, place, time; no advice | Lee 2014 |
| no-evidence-lead-minutes | exact minutes are settings, not findings | searched absence |

## 한국어 요약 (답변용)

- 알림은 약속을 지키는 데 도움이 된다. 무작위 연구 8개를 모은 결과 알림이 없을 때 참석률 67.8%,
  문자 알림 78.6%였다. 전화와 문자는 효과가 같았다.
- 한 번보다 두 번이 낫다. 미국 5만 4천여 명 연구에서 3일 전과 1일 전 두 번 알렸을 때 불참이
  4.4%로, 한 번만 알렸을 때(5.8%, 5.3%)보다 적었다.
- 마지막 알림은 바로 움직일 수 있는 때 울려야 한다. 몇십 초만 미뤄도, 특히 중간에 다른 일이
  끼어들면 하려던 일을 잘 잊는다. 그래서 고정된 "10분 전"이 아니라 출발 시각(시작 − 이동 −
  준비)에 맞춘다.
- 확인하지 않은 마지막 알림은 다음 움직일 수 있는 때 한 번 더 울린다.
- 알림 문구에는 할 일·장소·시간만 넣는다. 건강 조언을 문자로 보낸 한국 연구에서는 참석률이
  달라지지 않았다(원래 93% 수준).
- 몇 분 전이 최적인지는 연구된 바 없다. 그 숫자는 제품 설정이라고 말한다.
- 거의 빠뜨리지 않는 사람에게는 이득이 작다. 전에 놓친 적 있는 종류의 일정에 알림이 더 값어치가
  있다.
