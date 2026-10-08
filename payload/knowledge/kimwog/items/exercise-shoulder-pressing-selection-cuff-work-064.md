---
# Shoulder sprint 2026-10-06 (dispatch kw-shoulder-warmup), on top of the
# injury-caution rows 054 / 055 / 056. The shoulder is among the commonest
# injury sites in weight-training sports (Keogh & Winwood 2017, cited in 054),
# and 055 / 056 already say a familiar rotator-cuff-type ache keeps loading
# under a pain ceiling. This row answers the next question the split / caution
# code has to decide for a PRESSING lifter with subacromial / rotator-cuff
# related shoulder pain (RCRSP) or history at the shoulder: which variants to
# keep, which to drop, and what cuff / scapular work to add. The prep half
# (specific drills vs general warm-up) is the companion row 065.
#
# selection_rules is structured data for the split / caution code, same posture
# as 056's decision_ladder: DIRECTIONS and ORDERINGS, each rule naming its
# basis and its own grade. No load in kilograms, no risk figure.
id: exercise/shoulder-pressing-selection-cuff-work-064
domain: exercise
grade: B (exercise therapy is first-line for subacromial / rotator-cuff related shoulder pain; progressive resisted loading is what carries the effect); C (cuff-plus-scapular "specific" programmes over generic exercise -- contested; lifter-specific variant associations are cross-sectional); D (grip-width and scapular-position limits for pressing -- modelling and clinical opinion only)
lane: "@clinical-physio"
locale: universal
as_of: 1998-2024
contested: yes
sources:
  - "https://search.pedro.org.au/search-results/record-detail/60958"  # Pieters L, Lewis J, Kuppens K et al. 2020, J Orthop Sports Phys Ther 50(3):131-141 -- umbrella review of 16 systematic reviews (AMSTAR): strong recommendation for exercise therapy as first-line for subacromial shoulder pain; manual therapy as an add-on; moderate evidence of no effect for laser, shockwave, pulsed electromagnetic energy, ultrasound
  - "https://e-space.mmu.ac.uk/625819"  # Naunton J, Street G, Littlewood C et al. 2020, Clin Rehabil 34(9) -- 7 RCTs, n=468: progressive and resisted exercise vs no treatment / placebo reduced composite pain-and-dysfunction by 15 points (95% CI 9 to 21), pain with activity by 25 (14 to 36); non-progressive or non-resisted exercise 4 points (-2 to 9), no effect; low certainty
  - "https://www.bmj.com/content/344/bmj.e787"  # Holmgren T et al. 2012, BMJ 344:e787 -- RCT n=102, long-standing subacromial impingement after failed conservative care: eccentric cuff + concentric/eccentric scapular-stabiliser exercise vs unspecific neck/shoulder movement; successful outcome 69% vs 24%, chose surgery 20% vs 63% (NNT 3) at 3 months
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5393017/"  # Shire AR et al. 2017, BMC Musculoskelet Disord 18 -- 6 RCTs, n=231: specific vs general exercise strategy, no significant difference in short-term pain during activity or function
  - "https://bjsm.bmj.com/content/51/18/1340"  # Steuri R et al. 2017, Br J Sports Med 51(18):1340-1347 -- impingement meta-analysis: exercise beats non-exercise for pain; specific beat generic exercise; overall quality low (already carried in 055)
  - "https://eprints.whiterose.ac.uk/101408"  # Bury J, West M, Chamorro-Moriana G, Littlewood C 2016, Man Ther 25 -- 4 RCTs (n=190) pain, 3 (n=122) disability: scapula-focused beat generalised exercise up to 6 weeks (pain change not clinically significant), no difference by 3 months
  - "https://pubmed.ncbi.nlm.nih.gov/24077379/"  # Kolber MJ, Cheatham SW, Salamh PA, Hanney WJ 2014, J Strength Cond Res 28(4):1081-1089 -- cross-sectional, 77 men (46 recreational weight trainers, 31 controls): combined positive painful arc + Hawkins-Kennedy more frequent in trainers; associated with lateral raises and upright rows above 90 degrees (p<=0.004); inverse association with external-rotator strengthening. Read at abstract
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC11224528/"  # Noteboom L et al. 2024, Front Physiol 15:1393235 -- OpenSim musculoskeletal model, 10 experienced strength athletes, 21 bench techniques at 16 kg: grip <1.5 bi-acromial width lowered modelled acromioclavicular compression and glenohumeral posterior shear and cuff activity; scapular retraction lowered glenohumeral compression, posterior shear and cuff activity; 45-degree abduction raised superior shear. Model, light load, no injury outcome
  - "https://lida.sport-iat.de/ta/Record/4013441"  # Green CM, Comfort P 2007, Strength Cond J 29(5):10-14 -- narrative review: grip wider than 1.5 bi-acromial width linked to anterior instability, distal clavicle osteolysis, pectoralis major rupture; narrowing changes 1RM by about 5%. Cited from the record
  - "https://pubmed.ncbi.nlm.nih.gov/9784824/"  # Fees M, Decker T, Snyder-Mackler L, Axe MJ 1998, Am J Sports Med 26(5):732-742 -- clinical perspective: modifying grip, hand spacing, bar path, start/finish position of bench, shoulder press and others for the injured shoulder. Cited from the record, opinion level
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10426227/"  # Haugen ME et al. 2023, BMC Sports Sci Med Rehabil 15:103 -- 13 studies, n=1016: free-weight vs machine training, no difference in strength or hypertrophy in direct comparison; each modality gains more on its own test (specificity)
  - "https://pubmed.ncbi.nlm.nih.gov/15296366/"  # Reinold MM et al. 2004, J Orthop Sports Phys Ther 34(7):385-394 -- EMG of infraspinatus, teres minor, supraspinatus, deltoid across common external-rotation exercises; side-lying ER recorded the highest infraspinatus / teres minor activity. Cited from the record; EMG is a recruitment measure, not an outcome (013)
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: the pain ceiling this row's loading runs under
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the rung decides how many of these rules fire
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: history weight, never zero
  - "exercise/shoulder-prep-specific-vs-general-065"  # within-warehouse: the prep half
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: why EMG ranking only picks drills, never predicts outcome
  - "exercise/serratus-anterior-integration-019"  # within-warehouse: scapular upward-rotation / protraction drills (practitioner)
  - "exercise/harm-route-boundary-031"  # within-warehouse: red-flag shoulder pain is routed
  - "exercise/machine-free-weight-equivalence-075"  # within-warehouse (v38): the general machine vs free-weight row behind machine-substitution-costs-little (Haugen 2023 plus the direct trials); exercise/machine-first-selection-rules-076 carries the general equipment_rules, this row governs at a shoulder site
  - "framework:GRADE -- exercise as first-line rests on an umbrella of systematic reviews (strong recommendation); the progressive-resisted vs non-resisted contrast is low certainty (7 trials). Specific-vs-general is split: one well-run RCT (Holmgren) and one low-quality meta-analysis (Steuri) favour specific, one meta-analysis (Shire) finds no difference, scapula-focused gains fade by 3 months (Bury). No prospective study in lifters tests any variant restriction; the lifter data are one cross-sectional sample (Kolber) and one light-load model (Noteboom)."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
selection_rules:
  - rule: keep-pressing-loaded
    applies_at: [history-old, history-recent, history-unknown, current-load-pain]
    action: keep horizontal pressing in the split; do not remove the pattern, change the variant
    basis: Pieters 2020; Naunton 2020; exercise/tendon-fascia-load-management-055
    basis_grade: B
  - rule: add-progressive-cuff-work
    applies_at: [history-old, history-recent, history-unknown, current-load-pain]
    action: add external-rotation strengthening that progresses in load (cable, machine or band ER; side-lying ER), counted in the work block, not only as prep
    basis: Naunton 2020; Holmgren 2012; Kolber 2014
    basis_grade: B
  - rule: add-scapular-work
    applies_at: [history-recent, history-unknown, current-load-pain]
    action: pair cuff work with scapular-stabiliser work (rows, serratus / upward-rotation drills); expect early benefit, not a lasting edge over general loading
    basis: Holmgren 2012; Bury 2016; Shire 2017
    basis_grade: C
  - rule: lateral-raise-upright-row-below-90
    applies_at: [history-old, history-recent, history-unknown, current-load-pain]
    action: cap lateral raises and upright rows at about shoulder height; prefer cable or machine lateral raise to the same range
    basis: Kolber 2014
    basis_grade: C
  - rule: bench-grip-max-1.5-biacromial
    applies_at: [history-recent, history-unknown, current-load-pain]
    action: grip no wider than about 1.5x shoulder (bi-acromial) width; cue scapular retraction; let elbow angle follow comfort (a very tucked ~45-degree elbow raised modelled superior shear)
    basis: Noteboom 2024; Green & Comfort 2007
    basis_grade: D
  - rule: drop-highest-load-variants
    applies_at: [history-recent, history-unknown, current-load-pain]
    action: exclude the high-load / end-range variants first (behind-the-neck press or pulldown, wide-grip barbell bench, deep dips); machine chest press and machine shoulder press at a pain-free range are the default substitutes
    basis: Fees 1998; exercise/caution-severity-ladder-056
    basis_grade: D
  - rule: machine-substitution-costs-little
    applies_at: [history-old, history-recent, history-unknown, current-load-pain]
    action: swapping a free-weight press for a machine press keeps hypertrophy and general strength; it only costs strength specific to the free-weight lift
    basis: Haugen 2023
    basis_grade: B
  - rule: progress-under-the-ceiling
    applies_at: [current-load-pain]
    action: progress load at the shoulder under the 055 pain-monitoring rule (about 5/10 during and after, settled next morning, not rising week to week)
    basis: exercise/tendon-fascia-load-management-055
    basis_grade: B
  - rule: route-not-coach
    applies_at: [current-other, red-flag]
    action: no shoulder selection rule applies; pain-triage first (night pain, weakness, instability, trauma, numbness, rising pain)
    basis: exercise/harm-route-boundary-031
    basis_grade: D
refraction_notes:
  - note: >
      LOADING IS THE TREATMENT, AND IT HAS TO PROGRESS. For subacromial /
      rotator-cuff related shoulder pain, exercise therapy is the first-line
      recommendation across systematic reviews. The pooled trials suggest the
      effect sits with exercise that is resisted and progressed in load;
      range-of-motion or unloaded exercise showed no effect against no
      treatment. For the engine: cuff work at the shoulder site is a
      progressing working-set exercise, not a token warm-up drill.
    grade: B
  - note: >
      SPECIFIC VS GENERAL IS NOT SETTLED. One good trial in people who had
      failed earlier care found cuff-plus-scapular exercise produced far more
      recoveries and far fewer surgeries than unspecific movement, and one
      low-quality meta-analysis agrees; another meta-analysis found no
      difference, and scapula-focused programmes lose their edge by three
      months. Speak it as "targeted cuff and scapular work is a reasonable
      default", never as "targeted beats general".
    grade: C
  - note: >
      THE LIFTER-SPECIFIC SIGNALS ARE THIN. In one cross-sectional sample of
      recreational weight trainers, impingement signs were associated with
      lateral raises and upright rows taken above shoulder height and were
      less common in those who trained the external rotators. Association,
      not cause, one sample of men. It justifies capping those two lifts at
      shoulder height for a caution site and adding external-rotator work,
      not banning them for everyone.
    grade: C
  - note: >
      BENCH GRIP AND SCAPULA. A musculoskeletal model of experienced lifters
      at a light load found that a grip under about 1.5 times shoulder width
      and a retracted scapula lowered the modelled joint and cuff loads, and
      older clinical reviews give the same advice. No injury outcome was
      measured. Use it for a caution site; do not present it as a proven
      injury-prevention rule.
    grade: D
  - note: >
      MACHINES ARE A CHEAP SUBSTITUTION. Free-weight and machine training
      produced the same strength and hypertrophy in direct comparison; each
      wins only on its own test. So moving a caution-site lifter from a
      barbell to a machine press for a block costs muscle and general
      strength nothing measurable. Whether machines lower shoulder injury
      risk has not been tested (GAPS.md).
    grade: B
claim: >
  For a pressing lifter with subacromial or rotator-cuff related shoulder
  pain, or a history of it, the evidence-backed default is to keep pressing
  and change the variant, while adding progressive external-rotation and
  scapular work. Exercise is the first-line treatment for this pain, and the
  effect is carried by exercise that is resisted and progressed; unloaded
  range-of-motion work showed none. Cuff-plus-scapular programmes beat
  unspecific movement in one good trial (69% vs 24% recovered, 20% vs 63% went
  to surgery), but meta-analyses disagree on whether targeted beats general,
  and scapula-focused gains fade by three months, so targeted work is a
  default, not a proven superiority. In recreational lifters, impingement signs
  were associated with lateral raises and upright rows above shoulder height
  and were less common in those who trained the external rotators
  (cross-sectional). A light-load model and clinical reviews favour a bench grip
  no wider than about 1.5 times shoulder width with the scapula retracted.
  Swapping free weights for machines keeps hypertrophy and general strength, so
  machine pressing is a low-cost substitute for the highest-load variants.
  Present pain progresses under the 055 ceiling; red-flag shoulder pain is
  routed, not coached.
reasoning: >
  The first-line rule rests on Pieters 2020, an umbrella of sixteen systematic
  reviews, and Naunton 2020, which isolates progressive resisted exercise as
  the active ingredient at low certainty. Holmgren 2012 is the strongest single
  trial for cuff-plus-scapular work, but its control was deliberately
  unspecific and its population had failed prior care; Shire 2017 and Bury
  2016 temper the specific-over-general reading, hence contested and C for that
  half. Kolber 2014 is the only located study in recreational weight trainers;
  it is cross-sectional and read at abstract, so the variant caps are C and
  apply at caution rungs only. Noteboom 2024 is a model at 16 kg with no injury
  outcome, and Green & Comfort 2007 and Fees 1998 are opinion-level reviews
  cited from their records; the grip and end-range rules are held at D. Haugen
  2023 is a meta-analysis of direct comparisons and supports the substitution
  claim for hypertrophy and strength, not for injury. The injury_history axis
  is hard with block_specifics, matching 055 and 056: without the user's words
  on the shoulder's rung, specific variant limits are withheld and the one
  merged ask applies.
---

# exercise/shoulder-pressing-selection-cuff-work-064 -- 어깨가 걸리는 사람의 프레스 종목 고르기와 회전근개 운동

**한 줄 그림:** 어깨가 아프거나 다친 적이 있어도 미는 운동은 빼지 않는다. 종목을 바꾸고,
외회전·견갑 운동을 무게를 올려 가며 더한다.

## Selection rules (engine-readable)

| Rule | Fires at rung (056) | Action | Basis |
|---|---|---|---|
| keep-pressing-loaded | history-old .. current-load-pain | keep the pattern, change the variant | Pieters 2020, Naunton 2020 |
| add-progressive-cuff-work | history-old .. current-load-pain | ER work that progresses, in the work block | Naunton 2020, Holmgren 2012 |
| add-scapular-work | history-recent .. current-load-pain | rows, serratus / upward rotation | Holmgren 2012, Bury 2016 |
| lateral-raise-upright-row-below-90 | history-old .. current-load-pain | cap at shoulder height | Kolber 2014 |
| bench-grip-max-1.5-biacromial | history-recent .. current-load-pain | grip at most ~1.5x shoulder width, scapula retracted | Noteboom 2024 |
| drop-highest-load-variants | history-recent .. current-load-pain | behind-neck, wide-grip barbell, deep dips out; machine press in | Fees 1998, 056 |
| machine-substitution-costs-little | history-old .. current-load-pain | machine swap keeps size and general strength | Haugen 2023 |
| progress-under-the-ceiling | current-load-pain | 055 pain-monitoring rule | 055 |
| route-not-coach | current-other, red-flag | pain-triage first | 031 |

## 한국어 요약 (답변용)

- 어깨 앞·옆이 아픈 회전근개·견봉하 통증은 운동이 1순위 치료다. 그리고 효과는 무게를 올려 가는
  저항 운동에서 나왔다. 가동범위만 돌리는 운동은 아무것도 안 한 것과 차이가 없었다. 그러니
  외회전 운동은 몸풀기 한두 세트가 아니라 본운동 안에서 무게를 늘려 가는 종목으로 넣는다.
- 회전근개+견갑 운동이 일반 운동보다 낫다고 단정하지는 않는다. 다른 치료가 안 듣던 사람을 대상으로 한
  연구에서는 훨씬 많이 좋아지고 수술도 훨씬 덜 받았지만, 메타분석끼리 결론이 엇갈리고 견갑 위주
  운동의 우위는 3개월쯤이면 사라졌다. "기본으로 넣을 만하다" 정도로 말한다.
- 헬스 하는 사람들을 본 횡단 연구에서 사이드 레터럴 레이즈·업라이트 로우를 어깨 높이 위로
  올리는 사람에게 충돌 증후군 징후가 많았고, 외회전 근력을 따로 단련하는 사람에게는 적었다. 원인이라고
  확정된 건 아니다. 주의 부위가 있는 사람만 어깨 높이까지로 제한한다.
- 벤치 그립은 어깨너비의 약 1.5배 이내, 날개뼈를 모은 자세가 어깨에 걸리는 부하를 줄인다는
  모델 연구가 있다. 실제 부상을 추적한 연구는 아니다.
- 바벨 대신 머신 프레스로 바꿔도 근비대·근력은 손해가 없다. 프리웨이트 1RM처럼 그 동작 자체의
  힘만 덜 오른다. 머신이 부상을 줄이는지는 연구된 적이 없다.
- 지금 아픈 어깨는 통증 기준(운동 중·후 10점 중 5점까지, 다음 날 아침 회복, 주마다 늘지 않음)을
  지키며 무게를 올린다. 밤에 아프거나, 힘이 빠지거나, 빠질 것 같거나, 다친 직후이거나, 저리면
  여기서 처방하지 않고 통증 확인으로 보낸다.
