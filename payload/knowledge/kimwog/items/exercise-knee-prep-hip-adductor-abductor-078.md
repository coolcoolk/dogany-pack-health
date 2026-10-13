---
# Knee-prep sprint 2026-10-07 (dispatch task kw-ex-knee-adductor-prep). The
# question: does hip adductor / abductor / glute "activation" work before
# squatting help a lifter with anterior knee discomfort, at what dose and
# where in the session? Product code today (compose_rank_rules.json
# caution_policy.site_prep.knee) prepares a knee caution site with
# hip_adduction_machine + ankle_mobility. This row grades the pieces
# separately: the multi-week programme evidence (strong, posterolateral hip),
# the adductor-specific evidence (a null RCT), and the in-session placement
# (no trial at all). It feeds the 056 ladder; it does not change it.
#
# knee_prep is structured data for the split / caution code (see
# docs/kimwog-caution-ladder-fields.md, "knee_prep" section). Drill families
# are ORDERINGS; every set/rep/minute figure is either copied from a named
# trial protocol or labelled a product constant.
#
# v38 MERGE (2026-10-07, dispatch kw-consolidate-2): this row was written on
# the v36 base, before the v37 knee rows. Aligned to them: at
# current-load-pain the knee ceiling of exercise/knee-pain-symptom-guided-
# loading-057 (2/10) governs patellofemoral lines (055 only for a
# patellar-tendon ache), and the patellofemoral-to-current-load-pain move
# this row proposed was already made in v37 (056 joint-cartilage modifier
# -> 057). Range and variant choice stay with 058's variant_swaps.
id: exercise/knee-prep-hip-adductor-abductor-078
domain: exercise
grade: A (hip- plus knee-targeted exercise as a multi-week programme for patellofemoral pain); B (the hip increment over knee-only work -- favoured in meta-analyses, volume-confounded, one null trial); B (adding hip adduction to leg-press adds nothing); C (hip weakness follows the pain rather than predicting it); D (in-session placement before squats and the prep dose -- no trial)
lane: "@clinical-physio"
locale: universal
as_of: 2009-2023
contested: yes
sources:
  - "https://www.jospt.org/doi/10.2519/jospt.2019.0302"  # Willy RW, Hoglund LT, Barton CJ, Bolgla LA, Scalzitti DA, Logerstedt DS, Lynch AD, Snyder-Mackler L, McDonough CM 2019, J Orthop Sports Phys Ther 49(9):CPG1-CPG95 -- APTA patellofemoral pain CPG, read at full text (orthodiv.org PDF) 2026-10-07. Strongest recommendation level: combined hip- and knee-targeted exercise, hip work aimed at the POSTEROLATERAL hip; hip-targeted work may be preferred early. Gaps text: optimal dosage unclear; most combined-vs-knee trials did not match exercise volume. Protocol figures quoted: 3 x 10 at 60% of 10RM (Ahmed Hamada 2017, hip-first carryover trial); high-volume knee work 3 x 30+ 3x/week 12 weeks vs 3 x 10, pain-avoiding, single moderate-quality RCT
  - "https://bjsm.bmj.com/content/49/21/1365"  # Lack S, Barton C, Sohan O, Crossley K, Morrissey D 2015, Br J Sports Med 49(21):1365-1376 -- systematic review + meta-analysis, 14 studies (7 high quality): proximal (hip) plus quadriceps rehab beats quadriceps alone short term (strong evidence), medium term (moderate) and at 1 year (limited); abstract read
  - "https://bjsm.bmj.com/content/52/18/1170"  # Collins NJ et al. 2018, Br J Sports Med 52(18):1170-1178 -- patellofemoral pain consensus: exercise therapy, especially hip plus knee, recommended (already carried in 055)
  - "https://search.pedro.org.au/search-results/record-detail/23210"  # Song C-Y, Lin Y-F, Wei T-C, Lin D-H, Yen T-Y, Jan M-H 2009, Phys Ther 89(5):409-418 -- RCT n=89 PFP: leg press + hip adduction vs leg press alone vs no exercise, 3x/week for 8 weeks; both exercise groups improved pain, function and VMO size equally -- hip adduction added nothing
  - "https://pubmed.ncbi.nlm.nih.gov/19212898/"  # Smith TO, Bowyer D, Dixon J, Stephenson R, Chester R, Donell ST 2009, Physiother Theory Pract 25(2):69-98 -- systematic review of 20 EMG studies (387 participants): changing joint position or adding a co-contraction (incl. hip adduction) does not preferentially activate VMO over VL; methodologically weak base estate-scrub:allow(cited author surname)
  - "https://pubmed.ncbi.nlm.nih.gov/24687010/"  # Rathleff MS, Rathleff CR, Crossley KM, Barton CJ 2014, Br J Sports Med 48(14):1088 -- systematic review + meta-analysis: moderate-to-strong prospective evidence of NO association between isometric hip strength and developing PFP; cross-sectional evidence that people with PFP are weaker -- weakness looks like a consequence, not a cause (abstract via search record; PubMed page did not render)
  - "https://www.healio.com/news/orthopedics/20190604/kneefocused-exercise-with-patient-education-did-not-show-significant-benefit-vs-other-exercises-for"  # Hott A, Brox JI, Pripp AH, Juel NG, Paulsen G, Liavaag S 2019, Am J Sports Med 47(6):1312-1322 (doi 10.1177/0363546519830644) -- RCT n=112, ages 16-40, PFP > 3 months: 6 weeks education + hip-focused vs + knee-focused exercise vs + free physical activity; AKPS at 3 months not different (hip vs control 1.0 points, knee vs control 0.2); read via a news report of the paper, not the full text
  - "https://search.pedro.org.au/search-results/record-detail/30031"  # Dolak KL, Silkman C, Medina McKeon J, Hosey RG, Lattermann C, Uhl TL 2011, J Orthop Sports Phys Ther 41(8):560-570 -- RCT n=33 women: 4 weeks hip-first vs quad-first, then the same functional programme; hip-first had less pain at 4 weeks, groups equal at 8 weeks (cited in the CPG; abstract-level read)
  - "https://ijspt.scholasticahq.com/article/87764-the-use-of-elastic-resistance-bands-to-reduce-dynamic-knee-valgus-in-squat-based-movements-a-narrative-review"  # Forman DA, Alizadeh S, Button DC, Holmes MWR 2023, Int J Sports Phys Ther 18(5) -- narrative review: a band around the distal thighs during squats raises gluteal EMG but does not reduce, and sometimes increases, dynamic knee valgus; single-session studies only
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC4519208/"  # Comyns TM, Kenny IC, Scales G 2015, J Hum Kinet 46:177-187 -- n=11 athletes, 7-exercise low-load gluteal warm-up (1 x 10 each, ~7 min): jump height FELL from 30 s to 6 min after, some rate-of-force variables improved at 8 min; small, no control arm
  - "https://vbn.aau.dk/en/publications/exercise-induced-hypoalgesia-in-young-adult-females-with-long-sta"  # Straszek CL, Rathleff MS, Graven-Nielsen T, Petersen KK, Roos EM, Holden S 2019, Eur J Pain 23(10):1780-1789 -- crossover n=29 women with long-standing PFP: one bout of hip exercise and one of knee exercise both raised pressure-pain thresholds; knee exercise raised tolerance more; clinical knee pain during activity not reported
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: patellar-tendon ache and the pain-monitoring ceiling; PFP exercise direction (Collins 2018)
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the rung decides whether knee_prep runs at all
  - "exercise/knee-pain-symptom-guided-loading-057"  # within-warehouse (v37): patellofemoral pain and knee OA on the ladder; the 2/10 knee ceiling at current-load-pain
  - "exercise/knee-friendly-squat-depth-variants-058"  # within-warehouse (v37): depth and variant swaps for the squat pattern this prep precedes; hip-dominant work as a swap family
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: history weight for a recovered knee
  - "exercise/dynamic-warmup-same-day-performance-022"  # within-warehouse: general warm-up raises same-day performance
  - "exercise/prep-on-fatigued-muscle-two-effects-026"  # within-warehouse: what prep can and cannot do
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: EMG "activation" is not an outcome
  - "exercise/harm-route-boundary-031"  # within-warehouse: red-flag knee pictures go to triage
  - "framework:GRADE -- the programme direction (hip plus knee exercise over weeks reduces patellofemoral pain) rests on a CPG at its strongest level, a consensus statement and several meta-analyses; the hip-over-knee increment is downgraded for unmatched exercise volume and a null 112-person RCT. The adductor null is one moderate RCT plus a weak EMG review. NO trial compares hip work placed immediately before squats against the same work elsewhere in the session or week, and no trial is in barbell lifters; placement and prep dose are product constants."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
knee_prep:
  scope: anterior knee discomfort of the patellofemoral type (front of the knee, around or behind the kneecap, worse with squatting, stairs, sitting long) in a lifter; a localised patellar-tendon ache goes to 055 instead
  drill_families:
    - family: posterolateral_hip
      examples: [banded or cable hip abduction, side-lying hip abduction, clamshell, glute bridge or hip thrust, hip external rotation]
      priority: 1
      role: prep and strengthening
      basis: Willy 2019 CPG; Lack 2015
      basis_grade: A
    - family: knee_quadriceps
      examples: [leg extension in a tolerated range, partial-range or box squat, leg press to a tolerated depth, step-down]
      priority: 2
      role: strengthening; the main squat already counts as knee-targeted work
      basis: Willy 2019 CPG (weight-bearing and non-weight-bearing equal)
      basis_grade: A
    - family: hip_adductor
      examples: [hip adduction machine, adductor isometric squeeze, Copenhagen-type adduction]
      priority: 3
      role: allowed; no added effect on patellofemoral pain; never the only hip drill for a knee site
      basis: Song 2009; Smith 2009  # estate-scrub:allow(cited author surname)
      basis_grade: B
  prep_dose:
    sets: 1-2 per drill, 1-2 drills
    reps: 10-15, stopping well short of fatigue
    minutes: 5 or less
    when: after the general warm-up, before the first squat-pattern lift
    basis_grade: D
    constant: product constant; no trial sets a pre-squat activation dose
  strengthening_dose:
    sessions_per_week: 2-3
    sets_reps: about 3 x 10 at a moderate load (trial protocol 3 x 10 at 60% of 10RM), progressed; high-volume pain-avoiding knee work up to 3 x 30 is the other tested pattern
    weeks: 6-12 before judging it
    placement: after the main lifts of a lower day, or on a non-squat day
    basis_grade: C
    constant: protocol figures copied from trials; the CPG says the optimal dose is unknown
  ladder_alignment:
    - level: mild
      knee_prep: prep_dose
    - level: history-old
      knee_prep: prep_dose
    - level: history-recent
      knee_prep: prep_dose plus strengthening_dose
    - level: history-unknown
      knee_prep: prep_dose plus strengthening_dose
    - level: current-load-pain
      knee_prep: prep_dose plus strengthening_dose; the knee ceiling of 057 governs patellofemoral / knee-OA lines, the 055 ceiling a patellar-tendon ache
    - level: current-other
      knee_prep: none until pain-triage; once triage or the user's words name a familiar patellofemoral ache or diagnosed knee OA, the case is current-load-pain (056 joint-cartilage modifier, 057) and the row above applies (see refraction note 6)
    - level: red-flag
      knee_prep: none; refer
refraction_notes:
  - note: >
      THE HIP WORK THAT HAS EVIDENCE IS POSTEROLATERAL. The patellofemoral
      guideline recommends, at its strongest level, combining hip- and
      knee-targeted exercise, and names the posterolateral hip (abductors,
      external rotators, extensors) as the hip target. Pooled trials favour
      hip plus quadriceps work over quadriceps alone for pain and function,
      short and medium term, with limited one-year data. This is a multi-week
      programme effect, not a warm-up effect.
    grade: A
  - note: >
      THE HIP INCREMENT IS REAL BUT SMALLER THAN IT LOOKS. Most trials that
      found hip plus knee better than knee alone gave the hip group more total
      exercise; the guideline itself says the difference may be volume. One
      112-person RCT found six weeks of hip-focused or knee-focused exercise no
      better than free physical activity at three months. Speak of hip work as
      a useful part of the plan, not as the fix.
    grade: B
  - note: >
      THE ADDUCTOR IS NOT THE KNEE LEVER. In an 89-person RCT, adding hip
      adduction to leg-press training changed nothing in pain, function or
      VMO size compared with leg press alone. Squeezing or adducting does not
      preferentially switch on the VMO either (20 EMG studies). An adductor
      drill is fine to keep for the hip or groin, but for a knee caution site
      it should sit behind, never instead of, a posterolateral hip drill.
    grade: B
  - note: >
      WEAKNESS IS MOSTLY THE RESULT, NOT THE CAUSE. Prospective studies do not
      find that weaker hips predict who develops patellofemoral pain; people
      who already have it are weaker. So hip work is justified as treatment
      and capacity, not as fixing a cause, and a strong-hipped lifter with
      knee pain still gets it.
    grade: C
  - note: >
      PLACEMENT AND PREP DOSE ARE THE PLAN'S RULE. No trial compares hip work
      done right before squats against the same work after them or on another
      day, and none is in barbell lifters. One bout of hip or knee exercise
      raised pain thresholds in women with patellofemoral pain, and a general
      warm-up helps same-day output (022), which supports a short prep. A
      seven-drill glute warm-up briefly lowered jump height, and a band round
      the knees during squats raised glute EMG without reducing knee cave-in.
      So the prep is kept short and well short of fatigue, and the real
      strengthening sets go after the main lifts or on another day. Say this
      as the plan's rule, not a measured finding.
    grade: D
  - note: >
      FRONT-OF-KNEE PAIN AND THE LADDER. Under 056, present joint pain with
      an unnamed tissue is current-other (triage first). Once triage or the
      user's words name a familiar patellofemoral ache with no red flag
      (no swelling, locking, giving way, new trauma, night pain), exercise is
      the treatment, the same logic 055 applies to tendons. v37 made that
      move on the ladder itself: 056's joint-cartilage modifier sends the
      patellofemoral / diagnosed knee-OA picture to the knee variant of
      current-load-pain (057), with the 2/10 knee ceiling. Unnamed present
      joint pain still triages first.
    grade: D
  - note: >
      DO NOT SELL ACTIVATION AS ALIGNMENT. "Activate the glutes so the knee
      tracks" and "fire the VMO" are not supported claims: bands did not reduce
      valgus, adduction did not target VMO, and EMG is not an outcome (013).
      The honest copy is: this is part of the hip and thigh strengthening that
      helps front-of-knee pain over weeks.
    grade: C
claim: >
  For a lifter with front-of-the-knee (patellofemoral-type) discomfort, the
  supported lever is a multi-week programme that combines posterolateral hip
  strengthening (abduction, external rotation, extension) with quadriceps
  work; the patellofemoral guideline recommends this at its strongest level,
  though part of the hip advantage may be extra exercise volume and one large
  trial found no gain over free activity at three months. Hip adductor work is
  not the knee lever: adding hip adduction to leg press added nothing in a
  randomised trial, and adduction does not preferentially activate the VMO.
  Hip weakness tends to follow the pain rather than cause it. Whether hip work
  helps more when placed immediately before squats has never been tested, so
  the plan uses a short, non-fatiguing posterolateral hip prep before the
  first squat-pattern lift (1-2 drills, 1-2 sets of 10-15, about 5 minutes,
  product constants) and puts the strengthening dose (about 3 x 10, 2-3 times
  a week, judged over 6-12 weeks, from trial protocols) after the main lifts
  or on another day. Present unnamed joint pain still goes to triage first
  under 056.
reasoning: >
  Willy 2019 was read at full text: its recommendation text, the
  posterolateral target, the hip-first-early allowance, the unmatched-volume
  caveat and the unknown-dose gap are all quoted from it. Lack 2015 supplies
  the pooled direction over time. Song 2009 is the only trial found that
  isolates the adductor and it is null; the 2009 EMG review removes the usual VMO
  rationale. Rathleff 2014 explains why the work is treatment, not cause
  correction. Hott 2019 and the volume caveat keep the hip increment at the
  RCT band and set contested. The placement and prep dose have no direct
  trial; the D rule is built from 022 (warm-up helps same-day output),
  Straszek 2019 (one bout is hypoalgesic), Comyns 2015 (a long glute warm-up
  briefly dulls jumping) and Forman 2023 (bands do not fix valgus). The axis
  is hard with block_specifics: without the user's words on what and where
  the knee pain is, the rung -- and so the dose -- is not asserted.
---

# exercise/knee-prep-hip-adductor-abductor-078 -- 무릎 앞이 불편할 때 스쿼트 전 엉덩이 운동

**한 줄 그림:** 무릎 앞 통증에 근거가 있는 건 엉덩이 바깥·뒤쪽 근육(벌림·바깥돌림·폄)과 허벅지 앞을 함께
몇 주 키우는 것이다. 모음근(내전근) 운동은 무릎에 더해 주는 게 없었다. 스쿼트 직전에 하는 게 더 낫다는 연구는 없다.

## Knee prep (engine-readable)

| Drill family | Priority | Role | Basis |
|---|---:|---|---|
| posterolateral hip (band/cable abduction, clamshell, bridge, hip ER) | 1 | prep + strengthening | CPG, meta-analysis |
| knee / quadriceps (leg extension, box squat, leg press, step-down) | 2 | strengthening | CPG |
| hip adductor (machine, squeeze) | 3 | allowed, never the only hip drill | null RCT |

| Dose | Figure | Status |
|---|---|---|
| prep, before the first squat-pattern lift | 1-2 drills x 1-2 sets x 10-15, short of fatigue, about 5 min | product constant |
| strengthening, after main lifts or another day | about 3 x 10, 2-3 days/week, judge at 6-12 weeks | copied from trial protocols |

Ladder: prep only at mild and history-old; prep plus strengthening at
history-recent, history-unknown and current-load-pain (knee ceiling from
057); nothing at current-other until triage names the ache, nothing at
red-flag.

## 한국어 요약 (답변용)

- 무릎 앞(슬개골 주변·뒤쪽)이 불편할 때 효과가 확인된 건 엉덩이 바깥·뒤쪽 근육 운동(밴드·케이블 힙
  어브덕션, 클램셸, 브리지·힙 스러스트)을 허벅지 앞 운동과 함께 몇 주 하는 프로그램이다. 미국
  물리치료학회 진료지침이 가장 강하게 권하는 항목이다.
- 다만 엉덩이 운동을 더한 쪽이 운동량 자체도 많았던 경우가 대부분이었고, 112명 연구에서는 6주
  엉덩이·무릎 운동이 자유 운동보다 3개월에 낫지 않았다. "도움이 되는 한 부분"으로 말하고 "이걸로
  고친다"고 하지 않는다.
- 모음근(내전근) 운동은 무릎 통증에 더해 주는 게 없었다. 레그프레스에 고관절 모음을 더해도
  레그프레스만 한 것과 같았고, 모음 동작이 내측광근(VMO)을 골라 쓰게 하지도 않았다. 내전근 머신은
  빼지 않아도 되지만 무릎 준비 운동에서 엉덩이 바깥쪽 운동을 대신하면 안 된다.
- 엉덩이가 약해서 무릎이 아파지는 게 아니라, 아프면서 약해지는 쪽에 가깝다. 그래서 원인 교정이
  아니라 치료와 체력으로 권한다.
- 스쿼트 바로 전에 하는 게 더 좋은지는 연구된 적이 없다. 계획은 짧게 간다. 스쿼트 전에 1~2가지
  동작, 1~2세트, 10~15회, 지치기 전에 끝내고 5분 안쪽. 근력용 세트(대략 3x10, 주 2~3회, 6~12주
  보고 판단)는 메인 운동 뒤나 다른 날에 한다. 이 숫자는 계획의 규칙이지 측정된 기준이 아니다.
- 무릎에 밴드를 걸고 스쿼트하면 엉덩이 근전도는 오르지만 무릎이 안으로 모이는 건 줄지 않았다.
  "엉덩이를 깨워서 무릎 정렬을 잡는다"고 말하지 않는다.
- 지금 무릎이 아픈데 어디가 문제인지 모르면 먼저 통증 확인으로 보낸다. 붓기, 잠김, 빠지는 느낌,
  새로 다침, 밤 통증이 있으면 진료를 권한다. 익숙한 무릎 앞 통증이나 진단된 무릎 관절염이면
  057의 무릎 통증 기준(운동 중·후·다음 날 2/10 이하)을 따르고, 무릎 아래 힘줄 통증이면 055의 통증 기준을 따른다.
