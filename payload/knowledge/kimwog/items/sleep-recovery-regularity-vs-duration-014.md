---
# Sleep-regularity sprint 2026-10-07. Closes the regularity half of the
# "duration is not the whole story" question that items 004 and 013 left
# open. Every number below was read from the PubMed record (abstract) of the
# primary; none was taken from a secondary retelling. Full texts were NOT
# read for Windred 2024, Sletten 2023 or Chaput 2020 -- the panel's voting
# detail and the per-outcome GRADE tables are cited from the abstracts only.
# Rubric: sleep-recovery @clinical (VC-A). Regularity here means day-to-day
# consistency of sleep ONSET and OFFSET timing (Sleep Regularity Index, SD of
# onset / duration, social jetlag), not total hours.
id: sleep-recovery/regularity-vs-duration-014
domain: sleep-recovery
grade: C (irregular sleep timing is associated with worse health outcomes independent of duration); B (that the NSF consensus states regularity matters, and what it says); D (any personal threshold in minutes, and any effect on training adaptation)
lane: "@clinical"
locale: universal
as_of: 2012-2024
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/37738616/"  # Windred DP, Burns AC, Lane JM, Saxena R, Rutter MK, Cain SW, Phillips AJK. 2024, Sleep 47(1):zsad253, doi 10.1093/sleep/zsad253, PMCID PMC10782501 -- UK Biobank, 60,977 participants with accelerometry, mean age 62.8; top four SRI quintiles vs least regular: 20-48% lower all-cause mortality; SRI a stronger predictor than duration in nested models. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/37684151/"  # Sletten TL, Weaver MD, Foster RG, Gozal D, Klerman EB, Rajaratnam SMW, Roenneberg T, Takahashi JS, Turek FW, Vitiello MV, Young MW, Czeisler CA. 2023, Sleep Health 9(6):801-820, doi 10.1016/j.sleh.2023.07.016 -- National Sleep Foundation consensus, modified Delphi RAND/UCLA, 63 publications, two voting rounds: regularity important for health and performance; weekend catch-up "may be beneficial" when weekday sleep is insufficient. Panel COI disclosures extensive (device and pharma). Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/33054339/"  # Chaput JP et al. 2020, Appl Physiol Nutr Metab 45(10 Suppl 2):S232-S247, doi 10.1139/apnm-2020-0032 -- systematic review, 41 articles, 92,340 participants, 63% subjective sleep; later timing and greater variability associated with adverse outcomes; linear associations, NO threshold identifiable; GRADE very low to moderate. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/32138974/"  # Huang T, Mariani S, Redline S. 2020, J Am Coll Cardiol 75(9):991-999, doi 10.1016/j.jacc.2019.12.054, PMCID PMC7237955 -- MESA, 1,992 adults, 7-day actigraphy, median 4.9 y follow-up, 111 CVD events; duration SD >120 min HR 2.14 (1.24-3.68) and onset-timing SD >90 min HR 2.11 (1.13-3.91), adjusted for mean duration. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/28607474/"  # Phillips AJK et al. 2017, Sci Rep 7(1):3216, doi 10.1038/s41598-017-03171-4, PMCID PMC5468315 -- origin of the Sleep Regularity Index; 61 undergraduates, 30 days; irregular sleepers had DLMO ~2.5 h later and lower light-rhythm amplitude. Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/22578422/"  # Roenneberg T, Allebrandt KV, Merrow M, Vetter C. 2012, Curr Biol 22(10):939-943, doi 10.1016/j.cub.2012.03.038 -- large epidemiological sample, social jetlag associated with higher BMI beyond sleep duration (cross-sectional). Abstract read.
  - "https://pubmed.ncbi.nlm.nih.gov/30827911/"  # Depner CM et al. 2019, Curr Biol 29(6):957-967.e4, doi 10.1016/j.cub.2019.01.069 -- weekend recovery sleep did not prevent insulin-sensitivity loss; circadian phase delayed after the weekend (n=8/14/14). Abstract read.
  - "sleep-recovery/hour-target-is-a-threshold-consensus-013"  # the duration floor this item sits beside, and a second consensus product from the same NSF lineage
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # what is experimentally shown about short sleep and performance
  - "sleep-recovery/tracker-accuracy-003"  # onset/offset from a wrist device is an estimate; regularity inherits that error
  - "sleep-recovery/short-sleep-appetite-weight-015"  # the energy-balance half
  - "sleep-recovery/regularity-appetite-brief-rules-016"  # the engine-readable rules that use this item
  - "framework:GRADE -- the regularity evidence is observational cohorts and cross-sections (one large objective-accelerometry cohort, one actigraphy cohort, a review rated very low to moderate). The NSF statement is an expert consensus over that literature, the same instrument class item 013 warns about. No randomized trial that manipulates regularity while holding duration constant and measures a clinical or training outcome was located."
applicability:
  axes:
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      REGULARITY IS A SECOND AXIS, NOT A REPLACEMENT FOR HOURS. In the
      largest objective cohort (UK Biobank, about 61,000 people with
      wrist accelerometry), the most irregular fifth had the highest
      mortality, and regularity predicted mortality better than duration
      did. In MESA, a week-to-week spread of sleep duration over two hours,
      or of sleep-onset time over 90 minutes, carried roughly double the
      cardiovascular event rate, after adjusting for mean duration. So a
      brief should look at how much the timing moves, not only at the
      nightly total. These are associations; the item does not claim that
      fixing the schedule removes the risk.
    grade: C
  - note: >
      THERE IS NO MEASURED CUT-OFF. The systematic review found the
      associations mostly linear and could not identify a threshold for
      "large variability" or "late timing". The MESA bands (60 / 90 / 120
      minutes of duration SD, 30 / 60 / 90 of onset SD) are the study's
      reporting categories, not a clinical boundary. Any minute value an
      engine uses to flag irregularity is a product constant and must be
      spoken as one.
    grade: D
  - note: >
      THE WAKE TIME IS THE ANCHOR THAT CAN BE HELD. The regularity
      literature measures both onset and offset; the circadian mechanism in
      Phillips 2017 runs through light exposure, and morning light is
      delivered by getting up. A fixed wake time (including on days off) is
      the conventional behavioural lever and the one under the user's
      control on an early-start schedule. This is mechanism plus clinical
      convention, not a trial result on wake-time anchoring alone.
    grade: D
  - note: >
      WEEKEND CATCH-UP IS CONTESTED, NOT FORBIDDEN. The NSF panel voted that
      catch-up sleep "may be beneficial" when weekday sleep is short, and
      the systematic review found catch-up associated with BETTER outcomes,
      while social jetlag was associated with worse ones. In the one
      controlled test (Depner 2019), two days of ad libitum recovery sleep
      did not prevent the loss of insulin sensitivity and delayed circadian
      phase into the next week. The coherent reading: sleeping longer on a
      day off repays some deficit, sleeping LATER on a day off shifts the
      clock. Prefer an earlier bedtime or a nap to a late lie-in.
    grade: C
  - note: >
      TRAINING ADAPTATION IS NOT COVERED. No source located measures
      strength, hypertrophy or endurance adaptation against sleep
      regularity with duration held equal. The consensus "performance"
      vote rests mostly on cognitive and academic performance (Phillips
      2017: SRI and grades, r = 0.37). Do not tell a lifter that irregular
      sleep is costing them muscle. See GAPS.md.
    grade: D
  - note: >
      POPULATION AND MEASUREMENT LIMITS. UK Biobank participants were mean
      age about 63; MESA is older adults; the SRI origin cohort is 61
      students. The irregular group differs in many ways (shift work,
      illness, unemployment) that adjustment only partly removes. And
      onset/offset times from a consumer wearable carry the error item 003
      documents, so a computed regularity score is an estimate of an
      estimate.
    grade: C
claim: >
  How consistently someone sleeps -- the night-to-night stability of sleep
  onset and wake time -- is associated with health outcomes independently of
  how long they sleep, and in the largest objective cohort it was the
  stronger predictor of the two. In 60,977 UK Biobank participants with
  wrist accelerometry, the top four Sleep Regularity Index quintiles had
  20-48 percent lower all-cause mortality than the least regular quintile,
  and regularity out-predicted duration. In MESA (1,992 adults, 7-day
  actigraphy), a duration SD over 120 minutes or an onset-time SD over 90
  minutes was associated with roughly double the cardiovascular event rate
  after adjusting for mean duration. A 2020 systematic review (41 studies,
  92,340 participants) found later timing and greater variability associated
  with adverse outcomes but could not identify any threshold, and rated the
  evidence very low to moderate; social jetlag was also associated with
  higher BMI. The National Sleep Foundation's 2023 consensus panel voted that
  regularity matters for health and performance and that weekend catch-up
  sleep may help when weekday sleep is short; a controlled trial found that
  weekend catch-up did not prevent metabolic harm and delayed the clock. The
  operative rule: track timing consistency alongside hours, anchor the wake
  time, prefer extra sleep earlier rather than later, never speak a minute
  cut-off as measured, and make no claim about training adaptation.
reasoning: >
  Graded at the observational band because the evidence is cohorts: the two
  strongest are objectively measured (accelerometry, actigraphy) and
  prospective, which is why the association is carried at all, but no
  randomized trial varies regularity with duration held fixed. The NSF
  statement is graded at the trial band only for what it says, mirroring item
  013's treatment of the AASM/SRS duration statement: it is a modified RAND
  consensus over a literature the item itself grades lower, and the panel's
  conflict disclosures are long. Contested is set because the two most-cited
  readings of weekend catch-up point different ways (consensus "may be
  beneficial", review "associated with better outcomes", Depner's controlled
  test "fails to prevent metabolic dysregulation"), and because "regularity
  beats duration" is one cohort's nested-model result in an older population,
  routinely retold as a general law. The item fences off training adaptation
  explicitly: the performance half of the consensus vote rests on cognitive
  outcomes, and the only performance link with experimental support remains
  item 004's acute sleep-loss finding.
---

# sleep-recovery/regularity-vs-duration-014

Most sleep advice is about hours. The newer cohort data say the clock matters
too: people whose bed and wake times wander a lot from night to night do worse
on several health outcomes, even when their average hours are the same.

The largest look at this used wrist accelerometers on about 61,000 middle-aged
and older adults in the UK. The fifth of people with the most irregular sleep
had the highest death rate over about six years, and regularity predicted that
better than duration did. A US cohort of about 2,000 older adults found that
a week in which nightly sleep varied by more than two hours, or bedtime by
more than an hour and a half, went with roughly double the rate of heart
events, after allowing for how long people slept on average.

What those studies cannot say is where "too irregular" starts. The one
systematic review of the area found the relationships mostly linear, with no
visible threshold, and rated the evidence very low to moderate. So any number
of minutes a coach or app uses to flag an irregular week is a house rule.

A consensus panel of the National Sleep Foundation (2023) voted that
regularity matters for health and performance. The performance part leans on
studies of students' grades and alertness, not on strength or muscle. Nothing
located here shows irregular timing slowing training adaptation when hours are
held equal.

Weekend catch-up is where the sources disagree. The panel and the review lean
favourable: if the week was short, sleeping more on the weekend may help. The
one controlled experiment found two days of free recovery sleep did not stop
insulin sensitivity falling, and pushed the body clock later into the next
week. The workable reading is that extra hours help and later hours cost.
Going to bed earlier or napping is the cheaper repayment. A long lie-in is the
more expensive one.

The practical anchor is the wake time. It is the end of the night that light
and an alarm can hold steady, and it is the one an early-start schedule fixes
anyway. Keep it near the same on days off, and do the catching up at the
other end of the night.

## 한국어 요약 (답변용)

- 잠은 몇 시간 잤는지만 보면 부족하다. 매일 자고 일어나는 시각이 얼마나 들쭉날쭉한지가 따로
  건강 지표와 연결된다. 영국 약 6만 1천 명 손목 측정 연구에서는 가장 불규칙한 그룹의 사망률이
  가장 높았고, 규칙성이 수면 시간보다 더 잘 예측했다.
- 다만 이건 관찰 연구다. 시간을 맞추면 위험이 줄어든다는 실험 결과는 아직 없다.
- "몇 분 이상 차이 나면 불규칙"이라는 측정된 기준은 없다. 앱이나 브리핑이 쓰는 분 단위 기준은
  제품이 정한 규칙이라고 말한다.
- 주말 몰아 자기는 의견이 갈린다. 부족한 시간을 채우는 건 도움이 될 수 있지만, 늦게까지 자면
  체내 시계가 밀린다. 부족분은 일찍 자거나 낮잠으로 채우고, 일어나는 시각은 쉬는 날에도
  비슷하게 유지하는 쪽을 권한다.
- 불규칙한 수면이 근육이나 근력 향상을 방해한다는 근거는 찾지 못했다. 그렇게 말하지 않는다.
- 웨어러블이 잡은 잠든 시각·깬 시각은 추정치라서, 거기서 계산한 규칙성 점수도 추정치다.
