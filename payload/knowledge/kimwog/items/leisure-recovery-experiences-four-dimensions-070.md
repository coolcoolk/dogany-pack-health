---
# Leisure-recovery sprint 2026-10-06 (dispatch kw-leisure-recovery). The
# construct item: WHAT about off-job time tracks recovery. Deliberately LINKED
# to, not duplicated from, mental-health/workload-detachment-recovery-016 (owns
# the detachment correlations and their unidentified direction) and
# mental-health/detachment-is-a-schedule-property-026 (owns the calendar-gap
# craft). This item owns the four-dimension model, the activity-is-not-the-
# experience finding, and the intervention effect size. Lane: @hobby-practice
# (VC-C). All sources read at the abstract on 2026-10-06; no full text, so no
# per-dimension r values are carried (GAPS.md).
id: leisure/recovery-experiences-four-dimensions-070
domain: leisure
grade: "B (that the four recovery experiences -- detachment, relaxation, mastery, control -- are separable and each correlates with better wellbeing, with detachment tracking fatigue most and control tracking vigour most, cross-sectionally); B (that structured detachment interventions raise reported detachment, d = 0.36 pooled); C (that an activity label predicts the recovery experience -- it only modestly does); D (any causal reading from experience to outcome)"
lane: "@hobby-practice"
locale: universal
as_of: 2007-2021
contested: no
sources:
  - "Sonnentag, S. and Fritz, C. (2007). The Recovery Experience Questionnaire: Development and validation of a measure for assessing recuperation and unwinding from work. Journal of Occupational Health Psychology 12(3), 204-221. https://doi.org/10.1037/1076-8998.12.3.204"
  - "Bennett, A. A., Bakker, A. B. and Field, J. G. (2018). Recovery from work-related effort: A meta-analysis. Journal of Organizational Behavior 39(3), 262-275. https://doi.org/10.1002/job.2217"
  - "Steed, L. B., Swider, B. W., Keem, S. and Liu, J. T. (2021). Leaving Work at Work: A Meta-Analysis on Employee Recovery From Work. Journal of Management 47(4), 867-897. https://doi.org/10.1177/0149206319864153"
  - "Karabinski, T., Haun, V. C., Nuebold, A., Wendsche, J. and Wegge, J. (2021). Interventions for improving psychological detachment from work: A meta-analysis. Journal of Occupational Health Psychology 26(3), 224-242. https://doi.org/10.1037/ocp0000280"
  - "Park, H. I., Park, Y. A., Kim, J. I. and Hur, T. K. (2011). 한국판 직무스트레스 회복경험 척도(Recovery Experience Questionnaire)의 타당화 연구. 한국심리학회지: 산업 및 조직 (Korean Journal of Industrial and Organizational Psychology) 24(3), 523-552. https://accesson.kr/ksiop/assets/pdf/19740/journal-24-3-523.pdf -- 286 pharmaceutical-company employees, Seoul metropolitan area; abstract and title page read"
  - "mental-health/workload-detachment-recovery-016"  # detachment correlations and the three causal stories
  - "mental-health/detachment-is-a-schedule-property-026"  # the calendar-observable half of detachment
  - "leisure/vacation-recovery-fadeout-007"  # vacation is a dose, not one of these experiences
  - "leisure/flow-effortful-leisure-thin-base-008"  # why mastery does not rank activities
  - "leisure/self-report-measurement-005"  # every number here is a self-report
  - "framework:GRADE -- the four-factor structure is a confirmatory factor analysis across two samples (N = 930) and has been reproduced in other languages including Korean. The outcome links are meta-analytic (54 samples, N = 26,592; 198 samples) but pool mostly cross-sectional self-reports, so direction is not identified. The intervention meta-analysis (30 studies, 34 interventions, N = 3,725) is the only experimental leg and its outcome is reported detachment itself, not wellbeing."
recovery_experiences:
  # Engine-readable map for brief / retro modules. 'observable' is what a
  # Dogany module can see WITHOUT asking; 'ask' is the one-line retro probe
  # in the person's own words; 'tracks' is the outcome the meta-analysis
  # links it to most strongly (correlational). Nothing here is a target.
  - dimension: detachment
    definition: not thinking about work during off-job time
    observable: interval with no work item and no assistant work message (026)
    ask: 일 생각이 났어요, 안 났어요?
    tracks: lower fatigue (strongest of the four)
    basis_grade: B
  - dimension: relaxation
    definition: low activation, low effort, pleasant calm
    observable: none reliable; activity label is a weak proxy
    ask: 좀 쉬어지는 느낌이었어요?
    tracks: lower fatigue, wellbeing
    basis_grade: B
  - dimension: mastery
    definition: challenge or learning in a non-work domain
    observable: self-chosen practice entry (instrument, sport, class) -- presence only
    ask: 뭔가 해낸 느낌이 있었어요?
    tracks: vigour, wellbeing
    basis_grade: B
  - dimension: control
    definition: deciding for oneself what to do and when
    observable: off-time block the person scheduled themselves vs. one imposed
    ask: 그 시간은 내가 정해서 쓴 시간이었어요?
    tracks: vigour (strongest of the four)
    basis_grade: B
engine_rules:
  - rule: experience-not-activity
    says: never infer a recovery experience from an activity label; the same activity yields different experiences for different people and days
    basis_grade: C
  - rule: no-single-best-dimension
    says: no dimension is ranked above the others overall; detachment maps to fatigue, control to vigour; report the one that matches the person's own complaint
    basis_grade: B
  - rule: count-not-consequence
    says: brief may state an observable (e.g. no work-free evening this week); never promise that adding one will restore anything
    basis_grade: D
  - rule: ask-at-most-one
    says: retro asks at most one recovery question per day, in the person's words, and records the answer as that day's report, not as a trait
    basis_grade: D
refraction_notes:
  - note: >
      The construct, stated exactly. Sonnentag and Fritz (2007) built the
      Recovery Experience Questionnaire from the mood-regulation and job-stress
      recovery literatures; confirmatory factor analyses in a calibration and a
      cross-validation sample (total N = 930) separated FOUR recovery
      experiences: psychological detachment from work, relaxation, mastery and
      control. The final instrument has 16 items. Relations with job stressors
      and wellbeing were moderate; relations with coping and personality were
      generally low, which is the evidence that these are experiences rather
      than traits.
    grade: B
  - note: >
      Each dimension maps to a different outcome. Bennett, Bakker and Field
      (2018) pooled 299 effect sizes from 54 independent samples (N = 26,592).
      Detachment after work had a stronger negative relationship with fatigue
      than relaxation or control did; control had a stronger positive
      relationship with vigour than detachment or relaxation did. A model with
      recovery experiences as a partial mediator added up to 62 percent more
      explained variance in outcomes (delta R-squared = .12) beyond work
      characteristics alone. The per-dimension correlations were not read this
      pass (abstract only) and are not carried.
    grade: B
  - note: >
      THE ACTIVITY IS NOT THE EXPERIENCE, and this is the rule a scheduling
      assistant most needs. Steed et al. (2021), 198 samples, compared recovery
      conceptualised as activities, as experiences and as states: the three
      were only modestly related to one another, and the size and consistency
      of effects differed markedly by which one was measured. Experiences and
      the recovered state were temporally consistent; activities were not the
      same thing. So "watched TV", "went for a run", "played in the band" do not
      tell an assistant which recovery experience occurred.
    grade: C
  - note: >
      Detachment can be raised on purpose, modestly. Karabinski et al. (2021):
      30 studies, 34 interventions, N = 3,725, systematic search of published
      and unpublished work 1998-2020. Pooled effect on reported detachment d =
      0.36. Longer and higher-dose interventions did better, and effects were
      larger for older participants and for people starting with health or
      recovery impairment. Interventions targeting primary appraisal (how
      threatening work demands seem) were the only subgroup that beat the
      others. The outcome is detachment itself; that downstream wellbeing
      follows is item 016's correlational inference, not shown here.
    grade: B
  - note: >
      The direction caveat is inherited from item 016 and not re-argued:
      exhausted people find it harder to detach, and a demanding job lowers
      both. Bennett et al. also report that challenge demands relate MORE
      negatively to detachment, relaxation and control than hindrance demands
      do -- interesting, demanding work is the kind that follows people home.
      An assistant must not read low recovery as a personal failing.
    grade: C
  - note: >
      Korean locale. Park, Park, Kim and Hur (2011) translated the REQ (286
      pharmaceutical-company employees, Seoul metropolitan area) and reproduced
      the four factors (named 심리적 분리, 휴식, 자기성취, 통제), with job-related
      mobile ICT use after hours among the antecedents tested. Relations
      broadly matched prior work, but some factors differed slightly from
      Western results and the authors discuss what recovery means in Korean
      culture. The structure transfers; the magnitudes are not assumed to.
      Read at the abstract and title page only.
    grade: C
claim: >
  Recovery from work during leisure is best described by four separable
  experiences, not by the activities that fill the time: psychological
  detachment (not thinking about work), relaxation (low activation), mastery
  (challenge or learning outside work) and control (deciding for oneself what to
  do). Sonnentag and Fritz (2007) established the four-factor structure (16
  items, N = 930 across two samples), and a Korean translation reproduced it.
  Meta-analytically (Bennett, Bakker and Field 2018: 54 samples, N = 26,592),
  each relates to better wellbeing, with detachment most strongly tied to lower
  fatigue and control most strongly tied to vigour; recovery experiences add
  explained variance beyond work characteristics (delta R-squared = .12). Steed
  et al. (2021, 198 samples) found recovery activities, experiences and states
  only modestly related to each other, so an activity label does not identify
  the experience. Structured interventions raise reported detachment by d = 0.36
  (Karabinski et al. 2021, 30 studies, N = 3,725), more with higher dose. The
  outcome links are cross-sectional self-report and carry item 016's
  unidentified direction. Operative consequences for brief and retro modules:
  report observables (work-free intervals, self-scheduled blocks), ask about the
  experience in the person's words at most once a day, never infer an experience
  from an activity, never rank dimensions or activities, and never promise an
  outcome.
reasoning: >
  The leisure domain held a dose item (007) and an absence row (008), and the
  mental-health lane held detachment alone (016, 026). What was missing is the
  model the recovery literature actually uses, which has four dimensions rather
  than one, and the one finding that most constrains an assistant that sees a
  calendar: activities and experiences are only modestly related. That finding
  is what keeps this item from becoming the active-versus-passive ranking that
  008 refuses -- mastery is an experience a person reports, not a property of
  guitar practice, so it cannot rank guitar above television. The grades split
  by leg: the factor structure and the meta-analytic correlations sit at the
  trial band because they are large, reproduced and consistent in sign; the
  activity-to-experience mapping sits lower because it is a modest relation;
  any causal arrow sits at the practitioner floor on 016's reasoning. The
  intervention meta-analysis is the only experimental evidence and is graded
  for what it measured -- reported detachment -- not for the wellbeing it is
  usually quoted as improving. The recovery_experiences and engine_rules
  blocks are structured so a brief or retro module can read observables and
  the single permitted ask without parsing prose; the Korean ask wordings are
  product phrasing, not validated scale items.
---

# leisure/recovery-experiences-four-dimensions-070 -- 회복 경험 네 가지

What recovers a person after work is not which activity they did but what the
time felt like, along four separate lines: being off work in their head,
being calm, getting a sense of having done something of their own, and having
chosen it themselves.

## What the evidence says

- The four are measurably distinct (two samples, 930 people; reproduced in a
  Korean sample of 286 employees).
- All four go with feeling better. Being mentally off work goes with less
  fatigue more than the others do; choosing your own time goes with more
  energy more than the others do.
- The same activity does different things for different people. Recovery as
  activity, as experience and as state were only modestly related across 198
  samples. A run can be mastery for one person and a chore for another.
- Detachment can be helped on purpose, modestly (pooled d = 0.36 across 30
  studies), more with longer programmes. That measured detachment, not
  wellbeing.
- Almost all of it is people answering questionnaires at one moment. Which way
  the arrow points is not known (see mental-health 016).

## What the engine reads from this row

| Dimension | Observable without asking | One retro ask | Tracks most |
|---|---|---|---|
| detachment | interval with no work item and no assistant work message | 일 생각이 났어요, 안 났어요? | fatigue |
| relaxation | none reliable | 좀 쉬어지는 느낌이었어요? | fatigue, wellbeing |
| mastery | a self-chosen practice entry (presence only) | 뭔가 해낸 느낌이 있었어요? | vigour |
| control | the block was scheduled by the person | 그 시간은 내가 정해서 쓴 시간이었어요? | vigour |

Rules: experience-not-activity, no-single-best-dimension, count-not-consequence,
ask-at-most-one (frontmatter `engine_rules`).

## 한국어 요약 (답변용)

- 퇴근 후 회복은 "무엇을 했나"보다 "그 시간이 어땠나"로 본다. 네 가지다: 일 생각에서 벗어남(분리),
  편하게 늘어짐(이완), 일 밖에서 뭔가 배우거나 해냄(숙달), 내가 정해서 씀(통제).
- 네 가지 모두 컨디션이 좋은 것과 함께 간다. 일 생각에서 벗어난 날은 덜 피곤하고, 스스로 정한
  시간은 활력과 더 가깝다. 다만 대부분 한 시점 설문이라, 회복 경험이 좋아서 컨디션이 좋은지 그
  반대인지는 모른다.
- 같은 활동이 사람마다, 날마다 다른 경험이 된다. 그래서 "TV 봤다", "운동했다"만 보고 회복이 됐다
  안 됐다 말하지 않는다.
- 브리프는 보이는 사실만 말한다(예: "이번 주는 일 없는 저녁이 없었어요"). "쉬면 나아질 거예요"
  같은 약속은 하지 않는다.
- 회고에서는 하루에 한 번까지만, 본인 말로 묻는다. 대답은 그날의 기록이지 그 사람의 성향이 아니다.
- 어떤 경험이나 활동이 더 낫다고 순위를 매기지 않는다.
