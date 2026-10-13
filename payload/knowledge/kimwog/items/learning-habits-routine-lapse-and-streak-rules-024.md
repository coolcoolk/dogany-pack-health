---
# Habit-formation sprint 2026-10-06 (dispatch kw-habit-formation-2). The
# engine-readable rule set for the lifekit routine module: how to display
# progress, what to do on a missed day, a longer lapse, and the end of a
# programme. A routing rule over graded rows, same posture as
# exercise/caution-severity-ladder-056: each rule names the row it rests on,
# and every constant (the 7-day window, the 3-miss replan trigger) is
# labelled a product constant. The study-practice version of the lapse rule
# is learning-habits/lapse-is-not-a-reset-015 and is not restated.
#
# routine_rules is structured data (see docs/kimwog-routine-habit-fields.md).
id: learning-habits/routine-lapse-and-streak-rules-024
domain: learning-habits
grade: D (synthesis rule over 015, 022, 023 and four primaries; the directions are C-backed, every window and count is product judgement)
lane: "@behavioral"
locale: universal
as_of: 2010-2026
contested: yes
sources:
  - "https://doi.org/10.1002/ejsp.674"  # Lally et al. (2010): missing one opportunity did not materially affect habit formation (abstract)
  - "https://doi.org/10.1093/jcr/ucac029"  # Silverman & Barasch (2023), JCR 49(6):1095-1117: logs that highlight an intact streak raise later engagement vs a broken one; amplified by self-blame, attenuated by repair (seven studies, abstract)
  - "https://doi.org/10.1038/s41586-021-04128-4"  # Milkman, K. L., et al. (2021). Megastudies improve the impact of applied behavioural science. Nature, 600, 478-483 -- 61,293 gym members, 54 four-week programmes; top performer rewarded returning after a missed workout; 8% of programmes showed change measurable after four weeks (abstract via the Wharton lab page; publisher page paywalled)
  - "https://doi.org/10.1073/pnas.2216115120"  # Buyalskaya et al. (2023): days since last visit the strongest negative predictor of gym attendance
  - "https://doi.org/10.1287/mnsc.2020.3706"  # Beshears et al. (2021): post-programme drop, larger for rigid-window incentives
  - "learning-habits/lapse-is-not-a-reset-015"  # the study-craft lapse rule and the streak refusal
  - "learning-habits/habit-time-is-a-distribution-022"  # no completion day
  - "learning-habits/cue-design-repetition-over-rigidity-023"  # cue, flexibility, repetition
  - "framework:GRADE -- no trial compares a streak display against a rate display in a habit app, or tests a replan trigger. The directions come from one diary study (Lally), seven consumer experiments (Silverman & Barasch), two field datasets and one megastudy; the thresholds are product constants."
routine_rules:
  - rule: progress-display
    trigger: any routine progress view
    action: show done-count over a rolling window (e.g. 5 of last 7) and the cumulative total; do not make a consecutive-day counter the primary number
    constant: rolling window 7 days (product)
    basis: Silverman & Barasch 2023; learning-habits/lapse-is-not-a-reset-015
    basis_grade: C
  - rule: streak-if-shown
    trigger: a streak counter exists (user asked for it)
    action: a single miss never shows as zero; offer a repair (do it today, the streak continues) and frame the break as circumstance, not character
    constant: one repair per window (product)
    basis: Silverman & Barasch 2023 (repair attenuates; self-attribution amplifies)
    basis_grade: C
  - rule: single-miss
    trigger: one planned day not done
    action: no reset language, no reproach; the next planned occurrence is the only ask
    constant: none
    basis: Lally 2010
    basis_grade: C
  - rule: return-prompt
    trigger: the day after a missed planned occurrence
    action: one short, warm prompt to return at the next cue; acknowledge the return when it happens
    constant: one prompt per miss (product)
    basis: Milkman 2021; Buyalskaya 2023
    basis_grade: C
  - rule: replan-on-repeated-miss
    trigger: three or more misses in the rolling window, or no completion for 7 days
    action: ask once whether the cue or the size should change (smaller version, different anchor or time); keep the history; never restart the count at day one
    constant: 3 misses / 7 days (product)
    basis: learning-habits/cue-design-repetition-over-rigidity-023; learning-habits/lapse-is-not-a-reset-015
    basis_grade: D
  - rule: no-graduation
    trigger: any day count reached (21, 30, 66 or other)
    action: never announce the habit as formed or retire the reminder on a day count; reduce support only when the user asks
    constant: none
    basis: learning-habits/habit-time-is-a-distribution-022; Milkman 2021 (8% persistence); Beshears 2021
    basis_grade: C
  - rule: lapse-off-timeline
    trigger: a long lapse (user absent, travel, illness)
    action: resume at the current plan or a smaller version; the time-to-habit estimate is not restarted in copy
    constant: none
    basis: learning-habits/lapse-is-not-a-reset-015; Lally 2010
    basis_grade: D
refraction_notes:
  - note: >
      THE DIRECTIONS ARE EVIDENCE, THE NUMBERS ARE NOT. That one miss does
      not derail formation (Lally), that a log showing a broken streak
      lowers later engagement while repair softens it (Silverman & Barasch),
      and that the return after a miss is the high-leverage moment
      (megastudy top performer; days-since-last-visit as top predictor) are
      sourced. The 7-day window, the 3-miss trigger and the one-prompt cap
      are product constants. Say them as the plan's rule.
    grade: D
  - note: >
      THE STREAK CUTS BOTH WAYS. The same seven studies that warn about the
      broken streak find that an intact, highlighted streak raises
      engagement -- because people treat keeping it as a goal in itself.
      That is why the rule is not "never show streaks" but "never let one
      miss read as zero, and offer repair". The evidence is consumer
      experiments, not habit apps; transport is inference.
    grade: C
  - note: >
      PROGRAMMES END, HABITS DO NOT GRADUATE. In the megastudy only 8% of
      the 54 programmes left a change measurable after four weeks, and in
      the incentive experiment attendance fell once incentives stopped.
      Removing reminders on a day count is the most likely way for the
      module to undo its own work.
    grade: C
  - note: >
      CONTESTED: product streak mechanics are popular and vendor data claim
      retention gains; no independent habit-formation outcome was located.
      The rules here follow the independent evidence and may disagree with
      what users have learned to expect from other apps.
    grade: D
claim: >
  For a routine module: show progress as done-count over a rolling window plus
  the cumulative total, not a consecutive-day streak as the headline; if a
  streak is shown, one miss never displays as zero and a repair is offered;
  a single missed day gets no reset language and one warm prompt to return at
  the next cue; three misses in the window or a week without completion
  triggers one ask to resize or re-cue, keeping all history; and no day count
  ever declares a habit formed or retires a reminder. The directions rest on
  Lally (one miss did not materially affect formation), Silverman & Barasch
  2023 (broken-streak logs lower engagement, repair attenuates), Milkman 2021
  (rewarding the return after a miss was the top of 54 programmes; few
  effects outlasted four weeks) and Buyalskaya 2023 (days since last visit the
  strongest negative predictor); every window and count is a product constant.
reasoning: >
  A synthesis rule, graded at the practitioner band because the assembly is
  untested even though most parts are sourced, and marked contested because
  it runs against mainstream streak mechanics. Each rule names its basis
  and basis_grade so the module can speak its strength honestly. The
  lapse rules extend 015 from study practice to routines in general; the
  no-graduation rule turns 022's "no completion day" into a module action;
  the replan rule uses 023's cue levers instead of a restart.
---

# learning-habits/routine-lapse-and-streak-rules-024 -- 루틴 모듈: 빠진 날, 연속 기록, 끝나는 날

**한 줄 그림:** 하루 빠졌다고 0으로 돌리지 않는다. 빠진 다음 날 돌아오게 돕는 것이 가장 중요하고,
며칠째가 됐다고 "습관 완성"을 선언하지 않는다.

## The rules

| Rule | Trigger | Action | Constant | Basis strength |
|---|---|---|---|---|
| progress-display | any progress view | done over rolling window + total; streak not the headline | 7-day window | observational |
| streak-if-shown | user wants a streak | one miss never shows 0; repair offered; blame circumstance | 1 repair / window | observational |
| single-miss | one planned day missed | no reset, no reproach; next occurrence only | -- | observational |
| return-prompt | day after a miss | one warm prompt at the next cue | 1 per miss | observational |
| replan-on-repeated-miss | 3 misses in the window, or 7 days with none | ask once: smaller, new anchor or time; keep history | 3 / 7 | practitioner |
| no-graduation | any day count | never "formed"; never auto-retire reminders | -- | observational |
| lapse-off-timeline | long absence | resume current or smaller plan; no restart in copy | -- | practitioner |

Directions are sourced; windows and counts are product constants.

## 한국어 요약 (답변용)

- 진행 상황은 "최근 7일 중 5번", "지금까지 총 40번"처럼 보여 준다. 연속 일수를 대표 숫자로 쓰지
  않는다. 7일은 제품이 정한 기준이다.
- 사용자가 연속 기록을 원하면 보여 주되, 하루 빠졌다고 0으로 만들지 않고 "오늘 하면 이어진다"는
  만회 기회를 준다. 빠진 이유를 사람 탓이 아니라 상황 탓으로 말한다.
- 하루 빠지면 "처음부터"라는 말도, 나무라는 말도 하지 않는다. 다음 번 신호에 하자는 것 하나만
  말한다. 한 번 빠진 것은 습관 형성에 큰 영향이 없었다.
- 빠진 다음 날 짧고 따뜻하게 한 번 돌아오기를 권하고, 돌아오면 알아준다. 빠진 뒤 돌아오기를
  보상한 방법이 54개 중 가장 효과가 컸다.
- 일주일에 세 번 이상 빠지거나 일주일 동안 한 번도 못 했으면, 크기를 줄이거나 신호(일과·시간)를
  바꿀지 한 번 묻는다. 기록은 그대로 두고 1일차로 되돌리지 않는다.
- 21일·66일 같은 날짜에 "습관 완성"이라고 하거나 알림을 끄지 않는다. 프로그램이 끝나면 효과가
  대부분 사라졌다. 줄이는 건 사용자가 원할 때만.
- 오래 쉬었다 와도 지금 계획이나 더 작은 버전으로 다시 시작하고, "다시 66일"처럼 말하지 않는다.
