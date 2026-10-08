---
# Leisure-recovery sprint 2026-10-06 (dispatch kw-leisure-recovery). The dose
# item: how much free time, and does how it is spent matter. Two primaries,
# both read 2026-10-06: Sharif et al. 2021 at the accepted-manuscript full text
# (UCLA Anderson-hosted PDF), Kuykendall et al. 2015 at the abstract. The
# two-to-five-hour band is the authors' own "rough approximation" from one
# binned US dataset and is carried as that, never as a target. Lane:
# @hobby-practice (VC-C).
id: leisure/discretionary-time-dose-and-use-071
domain: leisure
grade: "B (that leisure engagement correlates moderately with subjective wellbeing, r = .26, and that frequency and diversity of leisure track wellbeing more than time spent in it); C (that wellbeing rises with discretionary time up to roughly two hours a day and stops rising, with a decline at high amounts in one of two datasets, explaining well under one percent of variance); C (that the high-time decline is absent for social time and attenuated when time feels productive); D (the two-to-five-hour band as anything more than a descriptive approximation)"
lane: "@hobby-practice"
locale: universal
as_of: 2015-2021
contested: no
sources:
  - "Sharif, M. A., Mogilner, C. and Hershfield, H. E. (2021). Having too little or too much time is linked to lower subjective well-being. Journal of Personality and Social Psychology 121(4), 933-947. https://doi.org/10.1037/pspp0000391 (accepted manuscript read: https://anderson-review.ucla.edu/wp-content/uploads/2021/12/Discretionary-Time-and-Life-Satisfaction.pdf)"
  - "Kuykendall, L., Tay, L. and Ng, V. (2015). Leisure engagement and subjective well-being: A meta-analysis. Psychological Bulletin 141(2), 364-403. https://doi.org/10.1037/a0038508"
  - "leisure/recovery-experiences-four-dimensions-070"  # what about the time matters
  - "leisure/flow-effortful-leisure-thin-base-008"  # why 'productive' here does not rank activities
  - "leisure/self-report-measurement-005"  # time amounts are self-reported; ATUS is a diary, NSCW a stylized question
  - "mental-health/workload-detachment-recovery-016"  # the regional caveat for US-sample defaults
  - "framework:GRADE -- Kuykendall pools 37 effect sizes, 11,834 people, plus cross-lagged longitudinal and experimental legs; the cross-lagged effects run both ways at similar size. Sharif is two large US cross-sectional datasets (35,375 people) and two online imagination experiments; the quadratic terms are highly significant and tiny in variance explained (R-squared about .003 to .007 without covariates). Large n, small effect, US only."
leisure_time_rules:
  # Engine-readable for brief / retro. Values are DIRECTIONS; the hour band is
  # descriptive (Sharif Study 2 binned plot) and is never spoken as a target.
  - rule: scarcity-is-the-signal
    says: very little discretionary time on a day (roughly under 2 h, descriptive) is the end of the curve with a clear association (stress); brief may name a run of such days as a count
    basis_grade: C
  - rule: more-is-not-monotone
    says: never suggest more free time as if well-being keeps rising with it; beyond about 2 h the association flattens, and in one dataset declined above about 5 h
    basis_grade: C
  - rule: frequency-and-variety-over-hours
    says: when summarising leisure in a retro, report how often and how varied (count of distinct self-chosen activities in the week), not total hours
    basis_grade: B
  - rule: social-time-no-ceiling-seen
    says: the high-amount decline was not found for social discretionary time; do not apply a too-much framing to time with people
    basis_grade: C
  - rule: productive-means-felt-worthwhile
    says: the attenuating condition is time the person themselves experiences as worthwhile; it is not an activity class, and screen or rest time is not by default unproductive
    basis_grade: C
  - rule: no-hour-target
    says: never set or score a daily free-time target from this row
    basis_grade: D
refraction_notes:
  - note: >
      The meta-analysis, stated exactly. Kuykendall, Tay and Ng (2015), 37
      effect sizes, 11,834 individuals: leisure engagement and subjective
      wellbeing are moderately associated (inverse-variance weighted r = .26),
      mediated by leisure satisfaction. Cross-lagged longitudinal analyses
      controlling for prior wellbeing show leisure satisfaction predicting
      later wellbeing (beta = .15) and wellbeing predicting later leisure
      satisfaction (beta = .16) -- both directions, same size. Retired samples
      show stronger relations than working samples.
    grade: B
  - note: >
      THE OPERATIVE FINDING for a summary module: measures of the FREQUENCY and
      DIVERSITY of leisure engagement were more strongly associated with
      wellbeing than measures of time spent in leisure. A retro that totals
      hours is reporting the weaker correlate; one that says "three different
      things you chose this week" is reporting the stronger one.
    grade: B
  - note: >
      The experimental leg is reported and discounted. Kuykendall et al. report
      that experimental leisure interventions enhanced wellbeing at d = 1.02.
      A d of one for leisure programmes is far above anything else in this
      domain, the experimental k and designs were not read this pass, and gate
      1 of leisure/curator-checklist-012 treats an effect too large for the
      activity as evidence about the design. Not carried as a usable size.
    grade: D
  - note: >
      The dose curve, stated exactly. Sharif, Mogilner and Hershfield (2021):
      two large US datasets, 35,375 people. National Study of the Changing
      Workforce (stylized question, working-day free time, mean 1.80 h):
      wellbeing rises to a break point at about 2 h and then flattens -- the
      high-end slope was negative but NOT significant. American Time Use Survey
      (diary of the previous 24 h, mean 5.48 h): rise, then a significant
      decline above a break point of about 3.4 h. From a 30-minute binned plot
      the authors give a "rough approximation": rising from zero to two hours,
      peaking between two and five, declining above five. Variance explained by
      the quadratic is tiny (R-squared about .003 to .007 without covariates).
    grade: C
  - note: >
      What moderates the high end. In the ATUS data the decline appeared for
      solo discretionary time (break point about 2.5 h) and NOT for social
      discretionary time, which showed only a positive linear relation. In two
      preregistered online experiments, people imagining a lot of free time
      reported lower wellbeing than those imagining a moderate amount, and the
      gap shrank when the time was imagined as productive -- defined to
      participants as feeling useful, accomplished, fulfilling or worthwhile.
      In the first experiment the high-versus-moderate difference was itself
      small (d = .10, p = .066). In the second (N about 4,000), imagining 7
      versus 3.5 hours a day lowered wellbeing when the time was imagined as
      not worthwhile (d = .23) and marginally raised it when imagined as
      worthwhile (d = .11, p = .068). Imagined time, online samples.
    grade: C
  - note: >
      WHAT "PRODUCTIVE" DOES NOT MEAN HERE. In the ATUS coding, "productive"
      was a list (working out, hobbies, sports); TV, games and relaxing sat in
      the other bucket. In the experiments it was the person's own sense that
      the time was not wasted. The defensible reading is the second one, and
      it is the reading item 070's experience-not-activity rule requires. This
      row does not license calling anyone's evening of television
      unproductive (item 008 stands).
    grade: C
claim: >
  Free time helps up to a point, and how varied and how often matters more than
  how many hours. Kuykendall, Tay and Ng (2015; 37 effect sizes, N = 11,834)
  found leisure engagement moderately associated with subjective wellbeing (r =
  .26) via leisure satisfaction, with longitudinal effects running in both
  directions (beta .15 and .16), and found the frequency and diversity of
  leisure more strongly associated with wellbeing than the time spent; their
  experimental d = 1.02 is too large to carry. Sharif, Mogilner and Hershfield
  (2021; 35,375 US adults in two datasets, plus two online experiments) found
  wellbeing rising with discretionary time up to about two hours a day and then
  not rising further; one dataset showed a decline at high amounts (the authors'
  rough band: peak between two and five hours, decline above five), absent for
  social time and attenuated when the time felt worthwhile. The variance
  explained is well under one percent and the samples are American. Operative
  consequences for brief and retro: scarcity of free time is the end worth
  naming as a count; more free time is not promised to help; leisure is
  summarised by frequency and variety, not hours; no hour target is set; and
  "productive" is the person's own sense of worth, not an activity class.
reasoning: >
  A brief or retro module will be tempted to treat free hours as a score that
  should go up. The two best primaries both cut against that. Kuykendall's
  meta-analysis supplies the most usable single fact in this item -- frequency
  and diversity beat hours -- which directly changes what a weekly summary
  should count, and its cross-lagged result keeps the direction honest: people
  who are doing well also engage more. Sharif et al. was read at the full
  manuscript because its popular retelling ("more than five hours of free time
  makes you unhappy") overstates it: the first dataset shows only a plateau, the
  decline is significant in the second, the variance explained is a fraction of
  a percent, and the experimental high-time effect is d = .10 at p = .066. What
  survives is directional and is graded at the observational band. The
  productive-time moderator is the part most likely to be misused as licence to
  rank hobbies over television; the ATUS coding does exactly that, the
  experimental definition does not, and this row adopts the experimental
  definition to stay consistent with 070 and 008. The meta-analytic
  experimental d = 1.02 is recorded and refused on the domain checklist's
  implausible-magnitude gate rather than silently dropped. US-only samples are
  a standing caution under item 016's regional finding.
---

# leisure/discretionary-time-dose-and-use-071 -- 여가 시간의 양과 쓰임

Having almost no free time goes with feeling worse. Having more and more free
time does not keep making things better. And how often and how varied the free
time is tracks wellbeing better than the number of hours.

## What the evidence says

- Across 37 effect sizes and about 12,000 people, doing leisure things goes
  with higher wellbeing (r = .26), and it runs both ways over time.
- How often and how many different things predicted wellbeing better than
  total leisure hours.
- In 35,375 Americans, wellbeing rose up to about two hours of free time a day
  and then stopped rising. In one dataset it went down at large amounts (the
  authors' rough band: best between two and five hours, lower above five).
  The effect is very small.
- That drop showed up for time alone, not time with people, and was smaller
  when people saw the time as worthwhile.

## What the engine reads from this row

`leisure_time_rules`: scarcity-is-the-signal, more-is-not-monotone,
frequency-and-variety-over-hours, social-time-no-ceiling-seen,
productive-means-felt-worthwhile, no-hour-target.

| Module | Do | Don't |
|---|---|---|
| brief | name a run of days with almost no free time, as a count | suggest more free time will help |
| retro | count how often and how many different self-chosen things | total the hours or score them against a target |
| both | treat "worthwhile" as the person's own word | label TV or rest as unproductive |

## 한국어 요약 (답변용)

- 자유 시간이 거의 없는 날이 이어지면 그 사실을 횟수로 짚을 수 있다. 이 구간은 스트레스와 함께 가는
  것이 비교적 분명하다.
- 하지만 자유 시간이 많을수록 계속 좋아지는 건 아니다. 하루 두 시간쯤까지는 올라가다가 그 뒤로는
  더 오르지 않았고, 한 자료에서는 아주 많으면 오히려 낮았다. 효과 자체가 아주 작고, 미국 자료다.
  "두~다섯 시간"은 연구자가 그림을 보고 잡은 대략의 범위라서 목표로 쓰지 않는다.
- 회고에서는 "몇 시간 놀았나"보다 "얼마나 자주, 몇 가지를 했나"를 센다. 그쪽이 만족과 더 잘 맞는다.
- 사람들과 보낸 시간에는 "너무 많다"는 패턴이 보이지 않았다.
- "보람 있는 시간"은 본인이 그렇게 느끼는지로 본다. TV나 쉬는 시간을 비생산적이라고 부르지 않는다.
