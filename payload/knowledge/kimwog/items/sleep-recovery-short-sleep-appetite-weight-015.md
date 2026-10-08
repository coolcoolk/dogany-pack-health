---
# Sleep-regularity sprint 2026-10-07. The energy-balance half: what short
# sleep does to intake, expenditure, body weight and -- for a user in a cut --
# the split between fat and lean mass lost. Sits in sleep-recovery because the
# EXPOSURE is sleep; the cut-phase consequence links to nutrition 012 and
# exercise 016. Every number was read from the PubMed record (abstract) of the
# primary; full texts were not read. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/short-sleep-appetite-weight-015
domain: sleep-recovery
grade: B (short sleep raises energy intake without a matching rise in expenditure; extending habitually short sleep lowers intake); C (short sleep during a calorie deficit shifts loss from fat toward lean mass); D (any personal kcal or kg figure)
lane: "@clinical"
locale: universal
as_of: 2004-2022
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/27804960/"  # Al Khatib HK, Harding SV, Darzi J, Pot GK. 2017, Eur J Clin Nutr 71(5):614-624, doi 10.1038/ejcn.2016.201 -- systematic review 17 studies (n=496), meta-analysis 11 studies (n=172): partial sleep deprivation raised energy intake by 385 kcal/day (95% CI 252-517), no significant change in total EE or RMR; higher fat, lower protein intake. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/35129580/"  # Tasali E, Wroblewski K, Kahn E, Kilkus J, Schoeller DA. 2022, JAMA Intern Med 182(4):365-374, doi 10.1001/jamainternmed.2021.8098, PMCID PMC8822469 -- RCT n=80, BMI 25-29.9, habitual sleep <6.5 h; one sleep-hygiene counselling session aiming at 8.5 h in bed; +1.2 h/night sleep (actigraphy), energy intake -270 kcal/day vs control (doubly labelled water), no EE change, weight fell. Two weeks of intervention. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/23479616/"  # Markwald RR, Melanson EL, Smith MR, Higgins J, Perreault L, Eckel RH, Wright KP Jr. 2013, PNAS 110(14):5695-5700, doi 10.1073/pnas.1216951110, PMCID PMC3619301 -- inpatient n=16, 5 days of insufficient sleep: EE up ~5% but after-dinner intake exceeded it, +0.82 kg; recovery sleep reduced intake. Abstract read. estate-scrub:allow(cited author surname)
  - "https://pubmed.ncbi.nlm.nih.gov/15583226/"  # Spiegel K, Tasali E, Penev P, Van Cauter E. 2004, Ann Intern Med 141(11):846-850, doi 10.7326/0003-4819-141-11-200412070-00008 -- crossover n=12 young men, 2 nights restriction vs extension: leptin -18%, ghrelin +28%, hunger +24%, appetite for calorie-dense high-carbohydrate foods +33-45%. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/20921542/"  # Nedeltcheva AV, Kilkus JM, Imperial J, Schoeller DA, Penev PD. 2010, Ann Intern Med 153(7):435-441, doi 10.7326/0003-4819-153-7-201010050-00006, PMCID PMC2951287 -- crossover n=10 overweight adults, 14 days moderate calorie restriction with 8.5 vs 5.5 h sleep opportunity: fat lost 1.4 vs 0.6 kg, fat-free mass lost 1.5 vs 2.4 kg, more hunger. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/29438540/"  # Wang X, Sparks JR, Bowyer KP, Youngstedt SD. 2018, Sleep 41(5):zsy027, doi 10.1093/sleep/zsy027, PMCID PMC8591680 -- RCT n=36, 8 weeks calorie restriction alone vs plus ~1 h less sleep on five nights (ad lib two nights): same total weight, lean and fat lost, but smaller PROPORTION of loss as fat with sleep restriction; weekend catch-up did not reverse it. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/34059916/"  # Depner CM et al. 2021, Sleep 44(11):zsab136, doi 10.1093/sleep/zsab136, PMCID PMC8598190 -- between-group, ad libitum intake: 24 h energy balance rose ~800 kcal in ALL arms including 9 h control, with no group difference. The null that keeps this item contested. Abstract read.
  - "sleep-recovery/regularity-vs-duration-014"  # timing half; social jetlag and BMI
  - "sleep-recovery/regularity-appetite-brief-rules-016"  # the engine-readable brief rules that use this item (evening-appetite, cut-phase-sleep)
  - "sleep-recovery/sleep-extension-weak-evidence-005"  # extension for PERFORMANCE is weak; extension for INTAKE has one good RCT -- do not conflate
  - "nutrition/weight-loss-rate-lean-mass-012"  # the cut-rate rule this item modifies
  - "nutrition/self-report-underreporting-007"  # logged intake under-reports; the 385 kcal is measured, a user's log is not
  - "exercise/deficit-volume-guidance-016"  # training during a deficit
  - "framework:GRADE -- intake and expenditure rest on controlled laboratory crossovers pooled in one meta-analysis plus one free-living RCT with doubly labelled water; the lean-mass shift rests on two small trials (n=10 crossover, n=36 parallel) that agree in direction and differ in size. One between-group trial (Depner 2021) found no energy-balance difference by sleep condition. Laboratory food access is ad libitum and not a free-living diet."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      SHORT SLEEP RAISES INTAKE, NOT BURN. Pooled across controlled studies,
      restricted sleep raised energy intake by roughly 385 kcal a day with
      no significant change in energy expenditure, and the extra came more
      from fat and less from protein. In the inpatient study the extra
      eating happened after dinner, and it outran the small extra cost of
      being awake longer. The brief consequence: after short nights, expect
      evening hunger and plan for it, rather than read it as a lack of
      willpower.
    grade: B
  - note: >
      EXTENDING SHORT SLEEP LOWERED INTAKE IN REAL LIFE. In adults with
      overweight who habitually slept under 6.5 hours, one counselling
      session aimed at 8.5 hours in bed added about 1.2 hours of measured
      sleep and cut intake by about 270 kcal a day against control, without
      any diet instruction, measured by doubly labelled water, over two
      weeks. This is the intake outcome; it is a different question from
      item 005's weak performance-extension literature.
    grade: B
  - note: >
      IN A CUT, SHORT SLEEP CHANGES WHAT IS LOST. In a 14-day crossover
      (n = 10), the same moderate calorie deficit with 5.5 instead of 8.5
      hours in bed lost 0.6 instead of 1.4 kg of fat and 2.4 instead of
      1.5 kg of fat-free mass. An 8-week trial (n = 36) with only about one
      hour less on five nights a week found the same direction -- equal
      weight lost, smaller share of it fat -- and two nights of catch-up per
      week did not undo it. For a user on a fat-loss phase, protecting sleep
      is part of protecting muscle. The magnitude is not transportable: the
      trials are small, and fat-free mass includes water and glycogen.
    grade: C
  - note: >
      THE SCALE CAN MISLEAD BOTH WAYS. Markwald's participants gained about
      0.8 kg in five short nights, and part of any short-term change is
      water and gut content. A brief must not attribute a one-week weight
      change to sleep, and must not tell a user that a good week of sleep
      will show on the scale.
    grade: D
  - note: >
      CONTESTED. Depner 2021 found energy balance rose by about 800 kcal a
      day in every arm of an ad libitum laboratory protocol, including the
      9-hour control, with no difference between sleep conditions. The
      authors call for within-subject and free-living designs. The direction
      in the pooled crossovers and the Tasali RCT is still carried; the
      magnitude is not.
    grade: C
  - note: >
      POPULATION. The hormone study is 12 young men; the cut trials are
      overweight adults, not lean trained lifters; sex differences appear
      (Markwald: women held weight under adequate sleep, men did not).
      Nothing here is resolved for women or for lean athletes.
    grade: C
claim: >
  Short sleep pushes energy balance positive mainly through intake. A
  meta-analysis of controlled partial sleep deprivation studies (11 studies,
  n=172) found energy intake rose by about 385 kcal a day with no
  significant change in energy expenditure, with more fat and less protein
  eaten. In an inpatient study, five short nights added about 0.8 kg as
  after-dinner eating outran the ~5 percent extra cost of staying awake; in a
  crossover, two short nights lowered leptin, raised ghrelin and raised
  hunger and appetite for calorie-dense foods. In the reverse direction, a
  free-living RCT in adults with overweight who habitually slept under 6.5
  hours found that sleep counselling added about 1.2 hours a night and cut
  measured intake by about 270 kcal a day against control. During a calorie
  deficit, short sleep changed the composition of what was lost: with the
  same diet, 5.5 hours in bed lost less fat and more fat-free mass than 8.5
  hours (n=10), and about one hour less on five nights a week lowered the
  share of loss that was fat over 8 weeks even with weekend catch-up (n=36).
  One laboratory trial found no energy-balance difference between sleep
  conditions. The operative rule: after short nights, expect higher evening
  appetite; in a fat-loss phase, treat sleep as part of lean-mass
  protection; never convert these figures into a personal calorie or kilogram
  prediction.
reasoning: >
  The intake finding reaches the trial band because it rests on controlled
  crossovers pooled in a meta-analysis and is replicated in a free-living RCT
  with objective intake (doubly labelled water plus body-energy change) and
  objective sleep (actigraphy). The lean-mass finding stays at the
  observational band despite randomization because both trials are small,
  short, in overweight rather than trained populations, and measure
  fat-free mass, which moves with water and glycogen; their agreement in
  direction is what keeps the note at all. Contested because Depner 2021, a
  randomized between-group study from the group that produced Markwald 2013,
  found no difference in energy balance between sleep conditions under ad
  libitum feeding. The item links to nutrition 012 rather than amending it:
  012 owns the rate-of-loss rule and its evidence; this item adds sleep as a
  modifier and should be read alongside it in a cut phase. The figures are
  pooled or group means and are never spoken as a user's expected kcal.
---

# sleep-recovery/short-sleep-appetite-weight-015

Short sleep makes people eat more. It barely changes how much they burn.

Across controlled studies where people's sleep was cut, intake went up by
roughly 385 calories a day on average, and expenditure did not move in any
measurable way. The extra food leaned toward fat and away from protein. In one
inpatient study, most of it was eaten after dinner. Staying up longer does
cost a little energy, about five percent, but the late eating more than
covered that, and people put on close to a kilogram in five days.

The reverse also held in everyday life. In adults with overweight who were
sleeping under six and a half hours, one counselling session about getting to
bed earlier added just over an hour of measured sleep a night. Over two weeks,
with no diet advice, they ate about 270 calories a day less than the control
group.

For someone trying to lose fat, the more important result is about what gets
lost. In a two-week crossover, the same diet with five and a half hours in bed
instead of eight and a half lost less than half as much fat and more lean mass.
An eight-week trial with only about an hour less on weeknights found the same
direction: the same weight came off, but less of it was fat, and weekend
lie-ins did not fix it. Both trials are small and in people with overweight,
so the size of the effect does not carry over to a lean lifter. The direction
is the part to keep.

One trial did not fit. In a ten-day laboratory study where people could eat as
much as they liked, everyone ate more than they needed, including the group
that slept nine hours, with no difference between groups. That is why the
item keeps the direction and drops the exact numbers.

Two things a brief should not do. It should not blame a week's change on the
scale on sleep, because water and food in the gut move faster than fat. And it
should not turn 385 or 270 into a personal calorie estimate.

## 한국어 요약 (답변용)

- 잠이 짧으면 소모 칼로리는 거의 그대로인데 먹는 양이 늘어난다. 통제 실험을 모은 분석에서
  하루 평균 약 385kcal 더 먹었고, 늘어난 건 주로 지방이었고 단백질은 줄었다. 특히 저녁 식사
  후에 많이 먹었다.
- 반대로 평소 6.5시간 미만 자던 과체중 성인이 수면을 하루 약 1.2시간 늘리자, 식단 지도 없이도
  하루 약 270kcal 덜 먹었다(2주, 무작위 배정 실험).
- 감량 중에 잠을 줄이면 같은 체중이 빠져도 지방은 덜 빠지고 근육 등 제지방이 더 빠졌다.
  주말에 몰아 자도 되돌려지지 않았다. 감량기에는 수면이 근육 지키기의 일부다. 다만 소규모·
  과체중 대상 연구라서 크기는 그대로 옮기지 않는다.
- 다른 실험 하나는 수면 조건 사이에 차이를 못 찾았다. 방향은 유지하되 숫자는 개인 예측으로
  말하지 않는다.
- 짧게 잔 다음 날 저녁 배고픔은 의지 부족이 아니라 예상되는 반응이라고 안내한다. 한 주
  체중 변화를 수면 탓으로 돌리지 않는다.
