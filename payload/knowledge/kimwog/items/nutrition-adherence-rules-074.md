---
# Diet-adherence sprint 2026-10-07 (dispatch kw-nu-diet-adherence-structure).
# The engine-readable synthesis of 025 (restraint style), 026 (diet breaks,
# refeeds), 027 (self-monitoring frequency) and 073 (weekend drift), for the
# diet card (skills-bundle/diet-status) and the weekly retro (week-health).
# It is a routing rule, not a primary finding: each rule names the graded
# row it rests on, and every product constant is labelled as one. Same
# posture as exercise/caution-severity-ladder-056.
#
# adherence_rules is structured data (see docs/kimwog-adherence-rules-fields.md).
# The YAML-subset reader returns every scalar as a string; flow lists parse
# natively. No program code was changed.
id: nutrition/adherence-rules-074
domain: nutrition
lane: "@meal-craft"
grade: D (synthesis rule over 025-027 and 073; each rule carries its own basis grade; every constant is product judgement)
locale: universal
as_of: 2026
contested: no
sources:
  - "nutrition/flexible-vs-rigid-restraint-025"  # all-or-nothing phrasing travels with disinhibition and binge episodes; flexibility does not cause more loss
  - "nutrition/diet-breaks-refeeds-026"  # breaks at maintenance cost no fat loss per restriction week, cut hunger, lengthen the calendar
  - "nutrition/self-monitoring-frequency-027"  # frequency is a signal; entries not minutes; daily weighing as a trend, with an exit
  - "nutrition/weekend-drift-073"  # compare like days; the weekend eating gap is the lever, the Monday bump is noise
  - "nutrition/unlogged-day-not-zero-019"  # an unlogged day is unknown, never zero
  - "https://doi.org/10.1038/ijo.2008.8"  # Alhassan S, Kim S, Bersamin A, King AC, Gardner CD. Dietary adherence and weight loss success among overweight women: results from the A TO Z weight loss study. Int J Obes 2008;32(6):985-991. PMID 18268511 -- secondary analysis, n=181: within each of Atkins, Zone and Ornish, adherence correlated with 12-month weight change (rs 0.34-0.42); most vs least adherent tertile -8.3 vs -1.9 kg (Atkins); authors conclude adherence may deserve more emphasis than macronutrient composition
  - "nutrition/body-measure-reading-rules-029"  # (parallel v38 sprint) measure_rules: speak bands and the confirmed-trend rule that any weight line in the retro also respects; weigh-as-trend and like-day-comparison here agree with its weekday-not-diet
  - "framework:GRADE -- each rule's basis_grade is the grade of the row it routes from; the thresholds (3:1 break block, 2 prior weeks, minimum logged days) are product constants with no direct evidence."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
adherence_rules:
  - rule: no-all-or-nothing
    surface: diet_card
    trigger: any card or nudge text about an over-target meal or day
    action: name the next meal as the resume point; state the week total, not a verdict on the day
    never: [실패, 망쳤다, 치팅, 벌충, 보상 단식]
    constants: none
    basis: nutrition/flexible-vs-rigid-restraint-025
    basis_grade: C
  - rule: adherence-before-diet-switch
    surface: weekly_retro
    trigger: weight trend flat for the week and the user proposes changing diet type (low-carb, fasting, another plan)
    action: check logged adherence to the current plan first; a switch is offered only if adherence was high and the trend still flat
    never: [the new diet will work better]
    constants: none
    basis: Alhassan 2008 (A TO Z secondary analysis)
    basis_grade: C
  - rule: diet-break-offer
    surface: diet_card
    trigger: user on a deficit reports rising hunger or falling satisfaction, or asks about a break
    action: offer an optional planned break at maintenance calories; show the moved end date; logging and weighing continue
    never: [breaks burn more fat, cheat week]
    constants: block 3 weeks deficit to 1 week maintenance (ICECAP protocol, a tested pattern, not an optimum)
    basis: nutrition/diet-breaks-refeeds-026
    basis_grade: B
  - rule: break-week-weight
    surface: weekly_retro
    trigger: the week was a declared break or refeed week, or follows one
    action: do not judge the weight change against the loss target; expect a small rise without fat regain
    never: [regained, 다시 쪘다]
    constants: judged again from the second full deficit week
    basis: nutrition/diet-breaks-refeeds-026
    basis_grade: B
  - rule: log-at-the-meal
    surface: diet_card
    trigger: any logging prompt
    action: ask for one short entry at the meal; never a long end-of-day reconstruction beyond the previous day
    never: [log everything in detail]
    constants: none
    basis: nutrition/self-monitoring-frequency-027
    basis_grade: C
  - rule: logging-frequency-signal
    surface: weekly_retro
    trigger: logged complete days this week fewer than the mean of the user's 2 prior weeks
    action: mention the drop once as an early sign, in the user's own numbers; no prescribed minimum
    never: [log at least N days to lose weight]
    constants: comparison window 2 prior weeks; complete day uses the kit rule (3 or more meal slots)
    basis: nutrition/self-monitoring-frequency-027
    basis_grade: C
  - rule: weigh-as-trend
    surface: both
    trigger: any weight shown
    action: show the weekly mean or same-weekday comparison; a single daily reading is never judged
    never: [today you gained]
    constants: none
    basis: nutrition/self-monitoring-frequency-027
    basis_grade: C
  - rule: weighing-exit
    surface: both
    trigger: user words of distress at the scale, a disordered-eating history, or weighing many times a day
    action: turn off the daily-weighing default and do not offer it again; keep the plan otherwise
    never: [weighing daily is proven]
    constants: none
    basis: nutrition/self-monitoring-frequency-027
    basis_grade: C
  - rule: like-day-comparison
    surface: weekly_retro
    trigger: weekly body-trend line
    action: compare weekly means, or same weekday to same weekday; Monday alone never triggers feedback
    never: [Friday-to-Monday change read as gain]
    constants: none
    basis: nutrition/weekend-drift-073
    basis_grade: C
  - rule: weekend-gap
    surface: weekly_retro
    trigger: at least 2 complete weekend days and 3 complete weekdays logged, and mean weekend intake above mean weekday intake
    action: name the gap in the user's own kcal as the week's adjustable point; unlogged days stay out of both means
    never: [the US average weekend surplus, an unlogged weekend read as a light one]
    constants: minimum 2 weekend + 3 weekday complete days; weekend = Sat and Sun
    basis: nutrition/weekend-drift-073
    basis_grade: C
  - rule: holiday-preview
    surface: diet_card
    trigger: a multi-day holiday (명절, long weekend) in the next 7 days
    action: one forward-looking line; expect a larger rise than a normal weekend; plan, do not forbid
    never: [holiday ban, fasting before the holiday]
    constants: 7-day look-ahead
    basis: nutrition/weekend-drift-073
    basis_grade: D
refraction_notes:
  - note: >
      THE RULES ARE GRADED, THE NUMBERS ARE NOT. Every rule's direction rests
      on its basis row. The 3:1 block, the 2-week comparison window, the
      minimum logged days and the 7-day look-ahead are product constants.
      Speak them as the plan's rule, never as a tested threshold.
    grade: D
  - note: >
      CARRY-OVER IS ALREADY BOUNDED; KEEP IT THAT WAY. The diet-status
      carry-over spreads a surplus over the remaining days of the declared
      week under the calorie floor and never crosses a week boundary. That
      matches 073 (weekday compensation goes with success) and 025 (no
      punishment day). A Sunday surplus therefore surfaces in the weekly
      retro as the weekend-gap lever, not as debt into next week.
    grade: D
  - note: >
      ADHERENCE IS THE OUTCOME VARIABLE, DIET TYPE MOSTLY IS NOT. In a
      year-long trial of three very different diets, weight change tracked
      adherence within each diet. A stall is checked against adherence
      before a diet change is entertained. Secondary analysis, self-reported
      adherence: direction only.
    grade: C
  - note: >
      NO SAFETY AXIS GATES THESE RULES. An eating-disorder history would
      arguably gate weighing and break advice, but no such axis exists on
      the ledger (framework-owned); weighing-exit is a conversational
      trigger until one does (GAPS.md).
    grade: D
claim: >
  The diet card and the weekly retro apply eleven adherence rules: phrase
  plans without all-or-nothing language and resume at the next meal; check
  adherence before entertaining a diet switch; offer optional diet breaks at
  maintenance as an appetite tool, showing the later end date, and do not
  judge a break week's weight; ask for short entries at the meal; read a drop
  in logged days against the user's own prior weeks as an early sign without
  a prescribed minimum; show weight only as a weekly mean or same-weekday
  comparison and never judge a single reading; switch off daily weighing for
  users who report distress or disordered eating; never let a Monday reading
  trigger feedback; name a measured weekend-versus-weekday intake gap in the
  user's own numbers; and preview multi-day holidays. Directions are backed
  by 025-027 and 073 (B to C); thresholds are product constants.
reasoning: >
  Each rule is a routing of one graded row into a surface the product
  already has, so the item adds no new finding and is graded as a synthesis.
  The strongest rules are the two about breaks, which rest on randomised
  trials (026). The phrasing, monitoring and weekend rules rest on
  consistent observational evidence (025, 027, 073) and say only what that
  evidence allows: directions, not doses. Where the evidence is silent the
  rule says less, not more -- no minimum logging days, no weekend kcal
  figure imported from US data, no Korean holiday effect size. The weekend
  gap is computed only from complete logged days on both sides because an
  unlogged day is missing data (019) and the kit already defines a complete
  day; dropping a day from one side only would manufacture a gap. The
  adherence-before-switch rule borrows one secondary analysis from the
  diet-comparison literature, carried at its own observational grade.
---

# nutrition/adherence-rules-074 -- 식단 카드·주간 회고용 지속(adherence) 규칙

**한 줄 그림:** 식단은 종류보다 지키는 정도가 결과를 가른다. 그래서 카드와 회고는 '하루 판정'이
아니라 '다음 끼니와 이번 주'를 말한다.

## The rules

| Rule | Surface | Trigger | Action | Basis |
|---|---|---|---|---|
| no-all-or-nothing | diet card | over-target meal/day | resume at next meal; week total, no verdict | 025 |
| adherence-before-diet-switch | weekly retro | flat week + user wants new diet | check adherence first | A TO Z |
| diet-break-offer | diet card | hunger up / asks | optional maintenance break, later end date shown | 026 |
| break-week-weight | weekly retro | break/refeed week | not judged against loss target | 026 |
| log-at-the-meal | diet card | logging prompt | one short entry at the meal | 027 |
| logging-frequency-signal | weekly retro | fewer complete days than 2 prior weeks | mention once, own numbers | 027 |
| weigh-as-trend | both | any weight | weekly mean / same weekday | 027 |
| weighing-exit | both | distress / ED history / repeated checking | daily weighing off, not re-offered | 027 |
| like-day-comparison | weekly retro | body-trend line | Monday alone never triggers | 073 |
| weekend-gap | weekly retro | ≥2 weekend + ≥3 weekday complete days, weekend higher | name the gap in own kcal | 073 |
| holiday-preview | diet card | 명절 / long weekend within 7 days | one planning line | 073 |

Directions come from the basis rows. The 3:1 break block, the 2-week window,
the minimum logged days and the 7-day look-ahead are product constants.

## 한국어 요약 (답변용)

- 목표를 넘긴 끼니나 날에는 "실패", "망쳤다", "치팅" 같은 말을 쓰지 않는다. 다음 끼니에서
  이어 가면 되고, 판단은 하루가 아니라 주 단위로 한다.
- 정체된 주에 사용자가 식단 종류를 바꾸자고 하면, 먼저 지금 식단을 얼마나 지켰는지 기록으로
  확인한다. 잘 지켰는데도 정체일 때만 변경을 논의한다.
- 배고픔이 커지거나 지친다고 하면 유지 칼로리로 먹는 다이어트 브레이크를 선택지로 제안할 수
  있다. 이때 늦어지는 목표 날짜를 함께 보여 준다. 브레이크 주의 체중은 감량 목표로 평가하지 않는다.
- 기록은 끼니 직후 짧게. 기록한 날이 지난 2주보다 줄면 한 번만, 사용자 본인 숫자로 짚는다.
  "주 며칠은 기록해야 빠진다" 같은 기준은 말하지 않는다.
- 체중은 주 평균이나 같은 요일끼리 비교한다. 월요일 숫자 하나로 피드백하지 않는다.
- 체중계 때문에 괴롭다거나 섭식 문제 이력을 말하면 매일 측정 권유를 끄고 다시 꺼내지 않는다.
- 기록이 충분한 주에 주말 섭취가 평일보다 높으면, 그 차이를 사용자 본인 kcal로 이번 주 조정
  포인트로 짚는다. 기록 없는 날은 양쪽 평균에서 모두 뺀다.
- 명절이나 긴 연휴가 일주일 안에 있으면 미리 한 줄로 짚는다. 금지가 아니라 계획이다.
- 숫자 기준(3주 감량:1주 유지, 2주 비교 창, 최소 기록일, 7일 예고)은 제품이 정한 규칙이다.
  연구로 정해진 기준처럼 말하지 않는다.
