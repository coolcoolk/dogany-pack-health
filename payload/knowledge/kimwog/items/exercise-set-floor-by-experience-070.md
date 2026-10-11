---
# Set-floor sprint 2026-10-07 (dispatch kw-ex-set-floor-experience). The
# composer fits sessions to the user's minutes and must decide what to cut
# when they do not fit: sets per lift, or lifts. This row carries the
# EVIDENCE half: how many weekly sets per muscle, how many sets per exercise,
# and where per-session sets stop paying, by training experience. Companion
# rows: 071 (maintenance vs growth during a cut), 072 (the set_floor rule
# the composer reads). Builds on 007 (weekly dose-response), 008 (fractional
# counting) and 015 (practitioner landmarks); does not restate them.
#
# Excluded on purpose: Barbalho et al. 2020 ("Evidence of a ceiling effect
# for training volume ... in trained men -- less is more?", IJSPP, PMID
# 31188644) is RETRACTED for data irregularities (notice PMID 32804467). Its
# "5-10 weekly sets are enough for trained men" is widely repeated and is NOT
# used here.
id: exercise/set-floor-by-experience-070
domain: exercise
grade: B (multiple sets per exercise beat one set; >=10 weekly sets per muscle enhances hypertrophy); C (the novice vs trained difference in the floor; the ~11 fractional-sets-per-session point, one preprint meta-regression); D (every product floor number below 10 weekly sets)
lane: "@performance-lit"
locale: universal
as_of: 2009-2026
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/41843416/"  # Currier BS ... Phillips SM 2026, ACSM Position Stand, Med Sci Sports Exerc 58(4):851-872 -- overview of 137 systematic reviews (>30,000 participants, novice or trained): hypertrophy enhanced by higher volumes (>=10 sets/wk); strength by >=80% 1RM, full ROM, 2-3 sets, early in the session, >=2 sessions/wk; failure, equipment, periodization not consistently influential
  - "https://pubmed.ncbi.nlm.nih.gov/37414459/"  # Currier BS, Mcleod JC et al. 2023, Br J Sports Med 57(18):1211-1220 -- Bayesian network meta-analysis, hypertrophy network 119 studies (n=3364): every prescription beat control and all promoted hypertrophy comparably; highest-ranked for hypertrophy was higher-load, multiset, twice-weekly
  - "https://pubmed.ncbi.nlm.nih.gov/20300012/"  # Krieger JW 2010, J Strength Cond Res 24(4):1150-1159 -- 8 studies, 55 ESs: multiple sets per exercise ~40% larger hypertrophy ES than 1 set, in both trained and untrained; ES 0.24 (1 set), 0.34 (2-3), 0.44 (4-6); 2-3 vs 4-6 not significantly different
  - "https://pubmed.ncbi.nlm.nih.gov/27433992/"  # Schoenfeld BJ, Ogborn D, Krieger JW 2017, J Sports Sci 35(11):1073-1082 -- 15 studies, 34 groups, mostly untrained: each weekly set +0.37% growth; <5 / 5-9 / 10+ weekly sets per muscle = 5.4% / 6.6% / 9.8% (trend p=0.074); after removing one influential study 5.5% / 7.2% / 8.6%; authors state only two volume studies in resistance-trained people
  - "https://link.springer.com/article/10.1007/s40279-025-02344-w"  # Pelland JC et al. 2025, Sports Med (PMID 41343037) -- 67 studies (28 untrained, 39 trained), training status entered as an adjustment covariate, not reported as a moderator of the volume slope; see 007
  - "https://sportrxiv.org/index.php/server/preprint/view/537"  # Remmert JF, Pelland JC, Robinson ZP, Hinson SR, Zourdos MC 2025, SportRxiv preprint (not peer reviewed) -- per-session meta-regression: point of undetectable outcome superiority ~11 fractional sets per muscle per session for hypertrophy (~8 direct, ~14 total) and ~2 direct sets for strength; authors: not an upper limit, too little data at very high per-session volumes, interpret cautiously
  - "https://pubmed.ncbi.nlm.nih.gov/30153194/"  # Schoenfeld BJ et al. 2019, Med Sci Sports Exerc 51(1):94-103 -- 34 trained men, 1 vs 3 vs 5 sets per exercise, 3x/week, 8 weeks: strength similar across groups; hypertrophy favoured higher volume at 3 of 4 sites
  - "https://pubmed.ncbi.nlm.nih.gov/30160627/"  # Heaselgrave SR et al. 2019, Int J Sports Physiol Perform 14(3):360-368 -- 49 trained men, 9 / 18 / 27 weekly biceps sets for 6 weeks: all grew, no significant between-group difference; 9 sets in one weekly session sufficient to increase muscle thickness
  - "https://pubmed.ncbi.nlm.nih.gov/32058362/"  # Aube D et al. 2022, J Strength Cond Res 36(3):600-607 -- 35 trained (squat ~2.1x body mass), 12 / 18 / 24 weekly lower-body sets, 8 weeks: no difference in thigh thickness or regional lean mass; 18 sets trended best for squat 1RM
  - "https://pubmed.ncbi.nlm.nih.gov/39665246/"  # Barsuhn A et al. 2025, J Appl Physiol 138(1):259-269 -- 29 trained men completed: keeping their previous weekly sets vs +30% vs +60% for 8 weeks; growth in all, no group difference in muscle size; maintenance group best 1RM
  - "https://pubmed.ncbi.nlm.nih.gov/19204579/"  # ACSM 2009 Position Stand, Progression models, Med Sci Sports Exerc 41(3):687-708 -- evidence category A: 1-3 sets per exercise for novices initially; category B: multiple sets with systematic variation to progress to intermediate/advanced; advanced hypertrophy 3-6 sets per exercise
  - "https://pubmed.ncbi.nlm.nih.gov/35438660/"  # Kassiano W et al. 2022, J Strength Cond Res 36(6):1753-1762 -- systematic review (8 studies, young men): systematic exercise variation can help regional growth; redundant exercises or excessive rotation may hinder gains
  - "https://pubmed.ncbi.nlm.nih.gov/31188644/"  # Barbalho M et al. 2020 IJSPP -- RETRACTED (notice PMID 32804467); listed so the exclusion is traceable, NOT used as evidence
  - "exercise/volume-doseresponse-007"  # within-warehouse: weekly dose-response, no plateau observed
  - "exercise/effective-sets-fractional-008"  # within-warehouse: direct 1.0 / indirect 0.5 counting
  - "exercise/set-counting-volume-unit-009"  # within-warehouse: the set as the volume unit
  - "exercise/volume-landmarks-heuristic-015"  # within-warehouse: MEV/MAV/MRV numbers are practitioner defaults
  - "framework:GRADE -- multiple-set superiority and the >=10 weekly-set hypertrophy direction rest on several meta-analyses and an umbrella review (B). No trial randomises novices and trained lifters to the same volume ladder, so the experience split of the floor is inferred from which populations the studies used (C). The per-session point is one preprint meta-regression (C). Every product number under 10 weekly sets is a constant (D)."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      NOVICES GROW ON LITTLE; THE 10-SET LINE IS WHERE MORE STARTS TO PAY.
      The pooled data that show growth at fewer than 5 weekly sets per muscle
      are mostly untrained people, and in them the step from no training to
      any training dwarfs every other choice (ACSM 2026). For a novice the
      floor can sit below 10 weekly sets without losing most of the early
      gain; the exact lower number is a product constant.
    grade: C
  - note: >
      TRAINED LIFTERS: AROUND 10 OR MORE WEEKLY SETS, AND THE TOP IS
      INDIVIDUAL. In trained men, 9 weekly biceps sets, 12 weekly thigh sets
      and "keep your current volume" all produced growth no different from
      much higher volumes in 6 to 8 week trials, while the pooled curve keeps
      rising slowly to about 30 weekly sets (007). Use 10 as the floor for a
      trained lifter, not as the target, and never tell a trained user that
      5 sets a week is enough: that claim came from a retracted paper.
    grade: C
  - note: >
      SETS PER EXERCISE: TWO OR MORE. One set per exercise grows muscle, but
      2-3 sets per exercise produced about 40% larger effects than one set in
      trained and untrained alike, and 2-3 vs 4-6 did not differ
      significantly (Krieger 2010). For strength, 2-3 sets of the lift itself
      is the ACSM 2026 line. One-set slots are the dose a maintenance phase
      tolerates (071), not the shape of a growth week.
    grade: B
  - note: >
      THE PER-SESSION POINT IS NOT A HARM LIMIT. About 11 fractional sets
      (about 8 direct sets) for one muscle in one session is where the
      preprint could no longer show that more sets beat fewer. Beyond it,
      growth still rose slightly with wide uncertainty. Use it to decide when
      a muscle's weekly sets should move to another day, not to say that
      the 12th set is wasted or harmful.
    grade: C
  - note: >
      FEWER, FULLER EXERCISES. Adding a second, redundant exercise for the
      same muscle and pattern adds no proven stimulus beyond its sets
      (Kassiano 2022), while each extra exercise costs a setup, warm-up and
      transition. When minutes are short, the evidence favours keeping sets
      on fewer exercises over spreading the same sets thinly across many.
      That trade-off is reasoning from the trials plus the composer's own
      time costs; no trial compares the two under a fixed time budget.
    grade: D
claim: >
  Weekly sets per muscle drive hypertrophy with diminishing returns; ten or
  more weekly sets per muscle is the umbrella-review line where more volume
  enhances growth, and multiple sets per exercise (2-3) beat one set in both
  novices and trained lifters. Novices grow substantially on fewer than ten
  weekly sets, so their floor can sit lower; trained lifters show growth
  across roughly 9-24 weekly sets in short trials with no proven advantage
  above about a dozen, while the pooled curve keeps rising slowly. One muscle
  stops showing a detectable benefit from extra sets in a single session at
  about 11 fractional sets (one preprint). The specific floor numbers below
  ten weekly sets are product constants, not findings.
reasoning: >
  ACSM 2026 (137 reviews) names >=10 sets per week as the hypertrophy lever
  and 2-3 sets per exercise as the strength lever, and says the largest gain
  is going from no training to any. Krieger 2010 gives the per-exercise
  comparison: multiple sets ~40% larger hypertrophy effect than one set,
  trained and untrained, with no significant gap between 2-3 and 4-6 sets.
  Schoenfeld 2017 shows growth at every volume band in mostly untrained
  samples (5.4 / 6.6 / 9.8% for <5 / 5-9 / 10+ weekly sets), which supports
  a lower novice floor; it also says trained data were scarce. In trained
  lifters, Heaselgrave 2019, Aube 2022 and Barsuhn 2025 found growth at the
  lower volumes they tested and no significant gain from more, while
  Schoenfeld 2019 found more growth at 5 sets per exercise than 1; the
  pooled Pelland 2025 curve (007) has no plateau. The per-session point is
  Remmert 2025, a preprint by the same group as 007, flagged as cautious by
  its own authors. The retracted Barbalho paper is excluded. Training status
  was an adjustment covariate in Pelland 2025, not a reported moderator, so
  no source gives an experience-specific floor directly.
---

# exercise/set-floor-by-experience-070 -- 경력별로 주당·종목당 최소 몇 세트인가

**한 줄 그림:** 근육 하나에 주 10세트 이상이면 성장이 더 붙고, 종목 하나는 2세트 이상이 1세트보다
낫다. 초보는 그보다 적어도 자라지만, 숫자 자체는 제품 기준이다.

## What the engine reads from this row

| Quantity | Evidence says | Strength of support |
|---|---|---|
| Weekly sets per muscle, growth | more is better, diminishing; >=10/wk enhances growth | umbrella review + meta-regressions |
| Novice weekly floor | growth at <5 and 5-9 weekly sets in mostly untrained samples | inferred from study populations |
| Trained weekly floor | growth at 9-12 weekly sets in short trials; no proven gain above ~12-18, pooled curve still rising | small RCTs + meta-regression |
| Sets per exercise | 2-3 beat 1 (~40% larger effect); 2-3 vs 4-6 not different | meta-analysis |
| Sets per muscle per session | detectable benefit ends near ~11 fractional (~8 direct) | one preprint |
| Strength lift sets per session | ~2 direct sets of the lift; ACSM 2-3 | preprint + umbrella review |

The composer's numbers (6 / 8 / 10 weekly sets, 2 or 3 sets per exercise)
live in 072 as product constants.

## 한국어 요약 (답변용)

- 근육 하나를 키우려면 주당 세트 수가 핵심이다. 많을수록 더 자라지만 갈수록 덜 붙는다. 미국스포츠의학회
  2026 지침은 근성장에 주 10세트 이상을 권한다.
- 종목 하나는 2~3세트가 1세트보다 근성장 효과가 40%쯤 컸다. 초보든 경력자든 같았다. 2~3세트와
  4~6세트는 뚜렷한 차이가 없었다. 힘을 키우는 데는 그 동작을 2~3세트 하는 것이 기준이다.
- 초보는 주 5세트가 안 되는 양에서도 꽤 자란다. 운동을 안 하다가 시작하는 것 자체가 가장 큰
  변화다. 그래서 초보의 최소선은 10세트보다 낮게 잡아도 된다. 다만 그 숫자는 제품 기준이다.
- 경력자는 짧은 연구에서 주 9~12세트로도 자랐고, 그보다 많이 해도 더 자란다는 차이가 뚜렷하지
  않았다. 다만 여러 연구를 합친 곡선은 주 30세트 근처까지 천천히 오른다. 경력자에게 주 10세트는
  출발선이지 목표가 아니다.
- "경력자는 주 5~10세트면 충분하다"는 말은 철회된 논문에서 나왔다. 근거로 쓰지 않는다.
- 한 번 운동에서 한 근육에 약 11세트(보조 동작은 반 세트로 셈)를 넘기면 더 하는 쪽이 낫다는
  게 더는 보이지 않았다. 해롭다는 뜻은 아니고, 그 이상이면 다른 날로 나누는 게 낫다는 신호다.
  이 수치는 아직 동료 심사 전인 연구 하나에서 나왔다.
- 같은 근육, 같은 패턴의 비슷한 종목을 하나 더 넣는다고 자극이 더 생긴다는 근거는 없다. 시간이
  모자라면 종목을 줄이고 남은 종목의 세트를 지키는 편이 근거에 더 맞는다.
