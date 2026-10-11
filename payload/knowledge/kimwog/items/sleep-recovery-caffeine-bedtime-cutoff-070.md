---
# Sleep-training sprint 2026-10-06 (dispatch kw-sleep-training-2). Closes the
# "CAFFEINE TIMING VERSUS SLEEP" gap GAPS.md has carried since v14. Every
# source was read at PubMed (abstract) or PMC (full text) on 2026-10-06; no
# number is reconstructed from memory. The item is built around DOSE x HOURS
# BEFORE BED, because the single "no coffee after 2 pm" rule hides the fact
# that dose moves the cutoff by more than half a day.
#
# caffeine_cutoff is structured data for a health / brief module: one row per
# dose band; product_hours = minimum gap from the LAST caffeine to bedtime
# that the brief uses, conservative_hours = the cautious alternative. The hours
# are the source's numbers where a source gives one and are labelled product
# rules where they are not. Rubric: sleep-recovery @clinical (VC-A).
id: sleep-recovery/caffeine-bedtime-cutoff-070
domain: sleep-recovery
grade: B (caffeine shortens and fragments sleep; 400 mg disrupts sleep onset even 12 h before bed; 100 mg 4 h before bed did not); C (the 8.8 h and 13.2 h regression cutoffs); D (the product cutoff table)
lane: "@clinical"
locale: universal
as_of: 2013-2025
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/36870101/"  # Gardiner C, Weakley J, Burke LM, Roach GD, Sargent C, Maniar N, Townshend A, Halson SL. 2023, Sleep Med Rev 69:101764, doi 10.1016/j.smrv.2023.101764 -- systematic review and meta-analysis, 24 studies
  - "https://pubmed.ncbi.nlm.nih.gov/39377163/"  # Gardiner CL, Weakley J, Burke LM, Fernandez F, Johnston RD, Leota J, Russell S, Munteanu G, Townshend A, Halson SL. 2025, Sleep 48(4):zsae230, doi 10.1093/sleep/zsae230, ACTRN12621001625864 -- double-blind randomised crossover, 23 males, 100 or 400 mg at 12, 8 or 4 h before bed, in-home partial polysomnography
  - "https://pubmed.ncbi.nlm.nih.gov/24235903/"  # Drake C, Roehrs T, Shambroom J, Roth T. 2013, J Clin Sleep Med 9(11):1195-1200, doi 10.5664/jcsm.3170, PMCID PMC3805807 -- 12 participants (6 F, 6 M), 400 mg at 0, 3 or 6 h before habitual bedtime vs placebo, home monitor
  - "https://pubmed.ncbi.nlm.nih.gov/33388079/"  # Guest NS et al. 2021, J Int Soc Sports Nutr 18(1):1, doi 10.1186/s12970-020-00383-4 -- ISSN position stand; dose 3-6 mg/kg, usually 60 min pre-exercise; names sleep as an individual adverse effect. COI disclosed in the stand: several authors advise supplement companies and the ISSN receives grants from caffeine-product sellers
  - "sleep-recovery/sleep-loss-performance-decrement-004"  # why the sleep that caffeine costs matters for the next session
  - "sleep-recovery/early-morning-session-071"  # the morning side: caffeine before a 05:00-06:00 session
  - "exercise/funding-coi-check-004"  # how the ISSN stand's disclosures are weighed
  - "framework:GRADE -- the direction (caffeine reduces total sleep time and efficiency, more so with dose and proximity to bed) rests on placebo-controlled experiments with objective sleep measures, hence B. The 8.8 h / 13.2 h figures are a meta-regression across 24 heterogeneous studies and are downgraded for imprecision and because the 2025 trial found 100 mg harmless at 4 h, which the regression would not predict. Downgraded for indirectness on sex: the 2025 trial is all male; the 2013 trial has 12 people."
applicability:
  axes:
    - key: caffeine_sensitivity
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: sleep_baseline_hours
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: body_weight_kg
      type: numeric
      role: soft
      unknown_policy: hedge
caffeine_cutoff:
  - dose_band: up to about 100 mg (one small coffee, one 250 ml energy drink)
    product_hours: 4
    source_hours: "4 (no objective or subjective effect at 4 h, 2025 trial)"
    conservative_hours: 9
    basis: Gardiner 2025 RCT; Gardiner 2023 regression (8.8 h for 107 mg)
    basis_grade: B
  - dose_band: about 200 mg (a large coffee, one standard pre-workout serve)
    product_hours: 13
    source_hours: "13.2 (2023 regression for 217.5 mg)"
    conservative_hours: 13
    basis: Gardiner 2023 regression
    basis_grade: C
  - dose_band: about 400 mg or more (double pre-workout, several coffees)
    product_hours: 14
    source_hours: "more than 12 (sleep onset delayed at 12, 8 and 4 h; fragmentation within 8 h; 2025 trial). 6 h cost more than 1 h of sleep (2013 trial)"
    conservative_hours: 14
    basis: Gardiner 2025 RCT; Drake 2013
    basis_grade: B
caffeine_rules:
  - rule: last caffeine of the day is timed against BEDTIME, not against the clock
    product_constant: false
    basis_grade: B
  - rule: when the dose is unknown, use the about-200 mg row (13 h)
    product_constant: true
    basis_grade: D
  - rule: the user's own feeling of having slept fine does not clear a dose -- the 6 h effect was seen only by the monitor, and 400 mg at 8-12 h was not felt
    product_constant: false
    basis_grade: B
  - rule: caffeine taken for a session that starts 05:00-06:00 is outside every cutoff in this table for any normal bedtime
    product_constant: false
    basis_grade: B
  - rule: never set a cutoff shorter than the table on the user's say-so of high tolerance; caffeine_sensitivity can lengthen it, not shorten it
    product_constant: true
    basis_grade: D
refraction_notes:
  - note: >
      Dose moves the cutoff more than anything else. In the 2025 crossover
      trial (23 men, habitual intake under 300 mg a day), 100 mg had no
      significant effect on objective or subjective sleep even 4 hours before
      bed, while 400 mg delayed sleep onset and changed sleep architecture when
      taken 12, 8 or 4 hours before bed, and fragmented sleep when taken
      within 8 hours. A single clock-time rule cannot be right for both doses.
    grade: B
  - note: >
      The pooled picture. Across 24 studies, caffeine reduced total sleep time
      by 45 minutes and sleep efficiency by 7 percent, lengthened time to fall
      asleep by 9 minutes and wake after sleep onset by 12 minutes, increased
      light sleep and reduced deep sleep (by 11.4 minutes). The review's
      regression puts the gap needed to avoid lost sleep at 8.8 hours for a
      107 mg coffee and 13.2 hours for a 217.5 mg pre-workout serve. These two
      cutoffs are model outputs across mixed studies, and the 2025 trial (from
      the same group) found 100 mg harmless at 4 hours, so the 8.8 hours is a
      cautious bound, not a measured threshold.
    grade: C
  - note: >
      People do not feel it. In the 2013 trial (12 people, 400 mg), caffeine
      taken 6 hours before bed cut measured sleep by more than an hour, yet
      only the monitor detected it -- the sleep diary did not. The 2025 trial
      found the same gap: perceived sleep quality fell only at 4 hours, while
      objective changes appeared out to 12. So "coffee doesn't affect me" is
      not evidence about the dose; it is evidence about the perception.
    grade: B
  - note: >
      The ergogenic dose is the problem dose. The ISSN stand puts the
      performance dose at 3-6 mg per kg, usually 60 minutes before exercise --
      roughly 210-420 mg for a 70 kg lifter, i.e. the 200-400 mg rows of the
      table. Pre-workout caffeine before an EVENING session therefore sits
      inside the disruptive window almost by definition. Before a MORNING
      session it does not. The stand also names sleep disruption as an
      individual adverse effect and attributes response differences partly to
      caffeine-metabolism genetics and habitual intake; several of its authors
      disclose supplement-industry ties, so it is used here for the dose and
      timing convention, not as independent evidence.
    grade: B
  - note: >
      Population. The 2025 trial is 23 young men; the 2013 trial is 12 people.
      Pregnancy, oral contraceptives, liver function and some medications
      slow caffeine clearance and are not covered by any row here. Where any
      of those apply, speak only the direction and the conservative column.
    grade: C
claim: >
  Caffeine costs sleep, and how much depends on dose and on hours before bed,
  not on a fixed clock time. Across 24 studies caffeine reduced total sleep
  time by 45 minutes and sleep efficiency by 7 percent and reduced deep sleep;
  the review's regression says a 107 mg coffee needs at least 8.8 hours before
  bed and a 217.5 mg pre-workout serve at least 13.2 hours to avoid lost sleep.
  A 2025 double-blind crossover trial (23 men) sharpened this: 100 mg 4 hours
  before bed had no significant effect, while 400 mg delayed sleep onset even
  12 hours before bed and fragmented sleep within 8 hours. A 2013 trial found
  400 mg 6 hours before bed cut measured sleep by more than an hour without
  the sleepers noticing. The operative rules: time the last caffeine against
  bedtime -- about 4 hours for up to 100 mg (9 if cautious), about 13 hours
  for a 200 mg pre-workout serve, more than 12 for 400 mg (14 in the product
  table); treat an unknown dose
  as 200 mg; do not let "I sleep fine on coffee" override the table; and note
  that pre-workout caffeine before a 05:00-06:00 session is outside every
  cutoff, while the same dose before an evening session is inside it.
reasoning: >
  Three primaries at three levels. The 2023 meta-analysis (24 studies)
  establishes the direction and gives the only published dose-specific cutoff
  regression; the 2025 crossover trial from the same group tests dose and
  timing directly with in-home polysomnography and placebo, which is the
  strongest design available and the reason the direction and the 400 mg row
  are B; the 2013 trial is small but is the source of the widely repeated
  6-hour rule and of the perception gap. They are consistent on direction and
  on proximity, and they disagree on the low-dose cutoff -- the regression
  says 8.8 hours for 107 mg, the trial saw nothing at 4 hours for 100 mg. The
  item keeps both: the trial number as the source row, the regression as the
  conservative column, and says which is which. The ISSN stand is used only
  for the conventional ergogenic dose and timing, with its disclosures noted
  per exercise/funding-coi-check-004. Not contested: no source located argues
  that caffeine near bedtime is harmless at ergogenic doses. The product rows
  (unknown dose -> 200 mg, sensitivity only lengthens) are D and labelled.
---

# sleep-recovery/caffeine-bedtime-cutoff-070 -- 카페인은 시계가 아니라 잠자리 시간과 양으로 끊는다

**한 줄 그림:** "오후 2시 이후 커피 금지" 같은 고정 시각 규칙보다, 마지막 카페인이 잠들기 몇 시간
전이었는지와 몇 mg이었는지가 중요하다.

## The cutoff table

| Dose (last intake) | Source says | Brief uses (product) | Cautious (product) |
|---|---|---:|---:|
| up to about 100 mg | 4 h before bed was fine (2025 trial) | 4 h | 9 h (2023 regression: 8.8 h for 107 mg) |
| about 200 mg (pre-workout serve) | 13.2 h (2023 regression) | 13 h | 13 h |
| about 400 mg | sleep onset delayed even at 12 h (2025 trial) | 14 h | 14 h |
| unknown | -- | as 200 mg (13 h) | 13 h |

A 05:00 session with caffeine at about 04:00 leaves 17 or more hours before a
21:00-22:00 bedtime: outside every row. An 18:00 session with a pre-workout at
17:00 and a 23:00 bedtime leaves 6 hours: inside the 200 mg and 400 mg rows.

## 한국어 요약 (답변용)

- 카페인 컷오프는 "몇 시 이후 금지"가 아니라 "잠들기 몇 시간 전, 몇 mg"으로 정한다.
- 연구 종합(24편)에서 카페인은 총 수면을 평균 45분, 수면 효율을 7% 줄였고 깊은 잠도 줄였다.
- 100mg 정도(작은 커피 한 잔)는 2025년 무작위 시험에서 잠자기 4시간 전에 먹어도 차이가 없었다.
  보수적으로 잡으면 9시간 전까지다.
- 프리워크아웃 한 스쿱(약 200mg)은 잠자기 약 13시간 전까지, 400mg 이상은 12시간 전에 먹어도 잠드는
  시간이 늦어졌다. 양을 모르면 200mg으로 본다.
- "커피 마셔도 잘 자요"는 근거가 되지 않는다. 6시간 전 400mg이 실제 수면을 1시간 넘게 줄였는데,
  본인은 수면일지에서 알아채지 못했다.
- 새벽 5~6시 운동 전 카페인은 어느 기준으로도 밤 수면 범위 밖이다. 같은 양을 저녁 운동 전에 먹으면
  범위 안이다.
- 시험 대상은 젊은 남성 위주이고 인원이 적다. 임신, 경구피임약, 간 질환, 일부 약물은 카페인 분해를
  늦추므로 이 표의 숫자를 그대로 쓰지 않는다.
