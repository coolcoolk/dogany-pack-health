---
# Leisure-recovery sprint 2026-10-06 (dispatch kw-leisure-recovery). Closes
# GAPS.md leisure want 8 (screen and consumption time) PARTLY. The question a
# brief / retro module asks -- is screen time restorative or not -- has no
# adult experimental answer located this pass. What is located: screen-time
# totals are a weak, contested correlate of wellbeing (adolescent and mixed
# samples); one adult survey on how the appraisal of entertainment (guilt)
# relates to its recovery value; and the rule from 070 that an activity label
# does not identify the recovery experience. Work-related screen use is the
# exception: it is a work object (026). All read at the abstract or the
# issuing university's release on 2026-10-06. Lane: @hobby-practice (VC-C).
id: leisure/screen-time-appraisal-not-category-072
domain: leisure
grade: "B (that total digital-technology use explains at most a fraction of a percent of adolescent wellbeing variance in large datasets); C (that pooled screen-media studies show little to no relation with mental-health outcomes -- contested); D (that guilt about entertainment use lowers its recovery value in depleted adults -- one cross-sectional survey); D (the engine rules, which are routing over these rows); E (any claim that a screen activity is or is not restorative for adults as a category)"
lane: "@hobby-practice"
locale: universal
as_of: 2014-2022
contested: yes
sources:
  - "Orben, A. and Przybylski, A. K. (2019). The association between adolescent well-being and digital technology use. Nature Human Behaviour 3, 173-182. https://doi.org/10.1038/s41562-018-0506-1"
  - "Ferguson, C. J., Kaye, L. K., Branley-Bell, D., Markey, P., Ivory, J. D., Klisanin, D., Elson, M., Smyth, M., Hogg, J. L., McDonnell, D., Nichols, D., Siddiqui, S., Gregerson, M. and Wilson, J. (2022). Like this meta-analysis: Screen media and mental health. Professional Psychology: Research and Practice 53(2), 205-214. https://doi.org/10.1037/pro0000426"
  - "Reinecke, L., Hartmann, T. and Eden, A. (2014). The Guilty Couch Potato: The Role of Ego Depletion in Reducing Recovery Through Media Use. Journal of Communication 64(4), 569-589. https://doi.org/10.1111/jcom.12107 (design and findings read at the Mainz University press release, press.uni-mainz.de/?p=17542; abstract not reached)"
  - "Steed, L. B., Swider, B. W., Keem, S. and Liu, J. T. (2021). Leaving Work at Work: A Meta-Analysis on Employee Recovery From Work. Journal of Management 47(4), 867-897. https://doi.org/10.1177/0149206319864153"
  - "leisure/recovery-experiences-four-dimensions-070"  # experience-not-activity
  - "leisure/discretionary-time-dose-and-use-071"  # 'productive' is felt worth, not a class
  - "leisure/flow-effortful-leisure-thin-base-008"  # reading is not ranked above television
  - "leisure/self-report-measurement-005"  # screen time self-report is worse than most: the person must decide what counts
  - "mental-health/detachment-is-a-schedule-property-026"  # work messages on a screen end an off-interval
  - "mental-health/phone-app-intervention-evidence-018"  # neighbouring row on phone-based interventions
  - "framework:GRADE -- the adolescent specification-curve analysis is large (n = 355,358) and methodologically strong for what it is: correlational, adolescents, total use. The 2022 meta-analysis (37 effect sizes, 33 studies, 2015-2019) reports little role and sits in an openly contested literature (the 2024 follow-up by the same group drew published methodological rebuttals). The adult recovery-specific evidence is one cross-sectional survey (N = 471). Nothing located tests screen versus non-screen leisure for adult recovery experimentally."
screen_time_rules:
  # Engine-readable for brief / retro modules. Directions only; no thresholds.
  - rule: no-screen-hours-score
    says: do not compute, display or score leisure screen hours as a wellbeing or recovery signal
    basis_grade: B
  - rule: work-screen-is-work
    says: work email, work chat and assistant work messages during an off-interval count as a work object (ends the interval per 026); this is the one screen distinction the engine applies
    basis_grade: D
  - rule: no-category-ranking
    says: never label TV, games, video or scrolling as non-restorative, or reading, walking or practice as restorative, by category
    basis_grade: E
  - rule: no-guilt-framing
    says: brief and retro wording never frames leisure media use as wasted, lazy or procrastination; that appraisal is the variable associated with lower recovery
    basis_grade: D
  - rule: ask-the-experience
    says: if recovery matters for the retro, ask the 070 experience question (detached? rested?) about the evening, not what was watched or for how long
    basis_grade: D
  - rule: owner-goal-overrides
    says: if the person has declared their own screen goal, track it as their goal in their words; the engine does not supply the goal
    basis_grade: D
refraction_notes:
  - note: >
      The large-data result, stated exactly and in scope. Orben and Przybylski
      (2019) ran specification-curve analysis over three large social datasets
      (total n = 355,358 adolescents): the association between digital
      technology use and adolescent wellbeing is negative but small,
      explaining at most 0.4 percent of the variation in wellbeing; they judge
      it too small to warrant policy change. Adolescents, total use,
      correlational. Not an adult recovery finding.
    grade: B
  - note: >
      The pooled result, and the dispute. Ferguson et al. (2022), 37 effect
      sizes from 33 studies published 2015-2019: screen media plays little
      role in mental-health concerns, including for smartphones and social
      media specifically. This is one side of an active dispute; the same
      group's 2024 meta-analysis of social-media experiments drew published
      rebuttals over inclusion and effect-size coding. Carried as "no
      consistent large effect", not as "proven harmless".
    grade: C
  - note: >
      The adult recovery leg is one survey. Reinecke, Hartmann and Eden (2014):
      N = 471 adults and students in Germany and the Netherlands, asked about
      the previous day. People more depleted after work or school were more
      likely to appraise their TV or game use as procrastination, and that
      guilt was negatively related to the recovery experience from the same
      entertainment. Those who needed recovery most got least from it -- via
      the appraisal, not the medium. Cross-sectional, one sample; the
      direction of the guilt link is not identified.
    grade: D
  - note: >
      Why no category ranking. Item 070 records (Steed et al. 2021, 198
      samples) that recovery activities and recovery experiences are only
      modestly related; item 008 records that effortful-over-passive leisure
      is unestablished; item 071 records that the "productive" moderator is
      the person's own sense of worth. Together they leave no basis for
      calling a screen activity non-restorative as a class. The absence is
      deliberate and graded at the bottom of the ladder.
    grade: E
  - note: >
      The one screen distinction that IS supported is content, not medium:
      work on a screen during off-time is work. Detachment (016, 070) is
      defined as not engaging with work, the Korean REQ validation tested
      job-related mobile ICT use after hours as an antecedent of recovery
      experiences, and item 026 makes the assistant's own messages part of
      the count. So the engine separates work-screen from leisure-screen and
      nothing else.
    grade: D
  - note: >
      Measurement warning carried from 005: self-reported screen time is the
      worst case of the stylized-recall problem, because the person must
      first decide what counts (background TV, phone while cooking, video at
      work). Device-logged totals avoid recall but not that boundary problem,
      and neither tells the engine the experience.
    grade: C
claim: >
  Screen time is not a usable recovery signal, and screen versus non-screen is
  not a usable restorative-versus-not split. In the largest correlational work,
  digital technology use explains at most 0.4 percent of adolescent wellbeing
  variance (Orben and Przybylski 2019, n = 355,358), and a 2022 meta-analysis of
  37 effect sizes found little role for screen media in mental health (Ferguson
  et al.), in a literature that remains openly contested. No adult experiment
  comparing screen and non-screen leisure for recovery was located. What adult
  evidence exists points at appraisal rather than medium: in one survey of 471
  adults and students, people depleted after work tended to see their
  entertainment as procrastination, and that guilt went with less recovery
  from it (Reinecke, Hartmann and Eden 2014). Combined with item 070 (activities
  only modestly predict recovery experiences) and item 008 (effortful-over-
  passive unestablished), the operative rules for brief and retro are: no
  screen-hours score; work content on a screen during off-time counts as work
  (026); no category ranking of leisure media; no wording that frames leisure
  media as wasted; ask about the experience, not the content or duration; and
  a person's own declared screen goal is tracked in their words.
reasoning: >
  This is the domain's measurement and absence logic applied to the one leisure
  quantity a phone can log automatically, which is exactly why a module would
  reach for it. The strongest available evidence is about the wrong population
  and the wrong outcome -- adolescent total use and general wellbeing -- and
  says the association is tiny; it is graded at the trial band for that scope
  only. The pooled screen-media meta-analysis is carried at the observational
  band and flagged contested because the literature is in public dispute and
  this row should not pick a side beyond "no consistent large effect". The
  adult recovery-specific evidence is a single cross-sectional survey and is
  graded at the practitioner floor; it is used only for a wording rule
  (do not add guilt), which costs nothing if the finding fails to replicate.
  The category ranking is refused with an explicit bottom-of-ladder grade so
  that a later pass meets the fence before the folk claim. The one distinction
  kept -- work content is work -- rests on the definition of detachment
  rather than on any screen study, and is graded as routing. GAPS.md records
  the adult experience-sampling study that would replace most of this row.
---

# leisure/screen-time-appraisal-not-category-072 -- 화면 시간과 회복

Hours on a screen do not tell an assistant whether someone recovered, and
"screen" is not the line between restful and not restful. The one line that
holds is whether the screen had work on it.

## What the evidence says

- In 355,358 adolescents, all digital technology use together explained at
  most 0.4 percent of wellbeing differences. Teenagers, not adult recovery.
- A 2022 pooling of 37 effects found little role for screen media in mental
  health. The field argues about this loudly; read it as "no consistent big
  effect", not "harmless".
- For adults after work, one survey (471 people): the more drained people
  were, the more they saw their TV or games as procrastination, and that
  guilt went with getting less recovery out of them.
- No experiment located compares screen and non-screen leisure for adult
  recovery.

## What the engine reads from this row

`screen_time_rules`: no-screen-hours-score, work-screen-is-work,
no-category-ranking, no-guilt-framing, ask-the-experience,
owner-goal-overrides.

| Seen by the module | Treat as |
|---|---|
| leisure screen minutes (device log) | not a recovery signal; not shown as a score |
| work chat / mail / assistant work message in an off-interval | a work object; the interval is broken (026) |
| the person's own stated screen goal | tracked as their goal, their words |
| the person's own "I just wasted the evening" | reflected without agreeing or adding judgement |

## 한국어 요약 (답변용)

- 화면 본 시간은 회복 지표로 쓰지 않는다. 청소년 대규모 자료에서도 디지털 기기 사용 전체가 행복감
  차이의 0.4% 이하만 설명했고, 성인 회복에 대해 화면 여가와 다른 여가를 비교한 실험은 찾지 못했다.
- 그래서 "TV·게임·영상은 쉬는 게 아니다", "독서·산책은 진짜 휴식이다" 같은 구분을 하지 않는다.
- 지친 날 본 TV나 게임을 "시간 낭비"로 느낀 사람일수록 그걸로 덜 회복됐다는 조사가 하나 있다.
  그러니 브리프·회고에서 여가 화면 사용을 낭비나 미루기처럼 말하지 않는다.
- 예외 하나: 쉬는 시간에 화면으로 업무 메신저·메일을 봤다면 그건 일이다. 비서가 보내는 업무
  메시지도 마찬가지다.
- 회복이 궁금하면 무엇을 몇 분 봤는지 대신 "일 생각에서 좀 벗어났어요?", "좀 쉬어졌어요?"를 묻는다.
- 본인이 화면 시간 목표를 정했다면 그건 본인 목표로, 본인 말로 따라간다.
