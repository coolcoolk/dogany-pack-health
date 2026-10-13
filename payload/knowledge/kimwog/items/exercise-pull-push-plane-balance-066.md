---
# Pull-plane balance sprint 2026-10-06 (dispatch kw-ex-pull-plane-balance).
# The question the compose code asks: does a week need both a horizontal and
# a vertical pull, should pulling outnumber pushing, and what changes for a
# lifter with a shoulder caution. Primary abstracts read at PubMed on
# 2026-10-06 (Baker 2004, Kolber 2009/2010/2013/2017, Clarsen 2014, Andersson
# 2017, Lynch 2010, Hibberd 2012, Barrett 2016, Cools 2007, Kassiano 2022,
# Keogh 2017); Appleby & Hori 2011 read at its SPONET record (conference
# abstract). The common 2:1 and 3:1 pull:push program ratios were searched
# for a primary source and none was found: they are refused, not carried.
#
# plane_coverage is structured data for compose (pattern names match
# compose_rank_rules.json: horizontal_push, vertical_push, horizontal_pull,
# vertical_pull). Every count in it is a product floor, labelled as such;
# none is a measured threshold.
id: exercise/pull-push-plane-balance-066
domain: exercise
grade: C (lifters carry rotator-cuff and lower-trapezius imbalances, cross-sectional; external-rotation strength and scapular work protect overhead athletes, prospective cohort plus one cluster RCT, transported by analogy); D (both pull planes every week and pulls at least matching pushes are program-design floors with no outcome trial)
lane: "@clinical-physio"
locale: universal
as_of: 2004-2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/19077737/"  # Kolber MJ, Beekhuizen KS, Cheng MS, Hellman MA 2009, J Strength Cond Res 23(1):148-157 -- 60 recreational upper-body weight trainers vs 30 controls (men): less active ROM in every direction except external rotation; agonist/antagonist strength ratios greater in trainers (p<=0.001). Authors: training is biased to pectorals and deltoids and neglects external rotators and lower trapezius. Cross-sectional; no injury outcome
  - "https://pubmed.ncbi.nlm.nih.gov/27390859/"  # Kolber MJ et al. 2017, J Strength Cond Res 31(4):1024-1032 -- 55 male weight trainers (24 with subacromial impingement by clinical cluster, 31 without): impingement group had less internal and external rotation ROM, weaker bodyweight-adjusted external rotators and lower trapezius (p<=0.02), and greater select strength ratios. Case-control; direction of cause not shown
  - "https://pubmed.ncbi.nlm.nih.gov/22836608/"  # Kolber MJ, Corrao M, Hanney WJ 2013, J Strength Cond Res 27(5):1333-1339 -- 123 weight trainers vs 36 controls: more anterior hyperlaxity, positive apprehension and relocation tests in trainers; association between 'high-five' position exercises (behind-the-neck lat pulldown and military press) and anterior-instability signs; inverse association with external-rotator strengthening. Cross-sectional, questionnaire exposure
  - "https://pubmed.ncbi.nlm.nih.gov/20508476/"  # Kolber MJ et al. 2010, J Strength Cond Res 24(6):1696-1704 -- review: up to 36% of documented resistance-training injuries are at the shoulder; mostly retrospective surveys; few predictive data
  - "https://pubmed.ncbi.nlm.nih.gov/27328853/"  # Keogh JW, Winwood PW 2017, Sports Med 47(3):479-501 -- systematic review of weight-training sports: shoulder, lower back, knee, elbow, wrist/hand most commonly injured; only 4 of 20 studies prospective
  - "https://pubmed.ncbi.nlm.nih.gov/24948083/"  # Clarsen B et al. 2014, Br J Sports Med 48(17):1327-1333 -- prospective cohort, 206 elite male handball players: obvious scapular dyskinesis OR 8.41 (95% CI 1.47-48.1), total rotation ROM OR 0.77 per 5 deg, external-rotation strength OR 0.71 per 10 Nm, for shoulder problems over a season. Throwing athletes, not lifters
  - "https://bjsm.bmj.com/content/51/14/1073"  # Andersson SH, Bahr R, Clarsen B, Myklebust G 2017, Br J Sports Med 51(14):1073-1080 -- cluster RCT, 660 elite handball players: OSTRC shoulder programme (internal-rotation ROM, external-rotation and scapular strength, kinetic chain, thoracic mobility) 3x/week in warm-up; shoulder-problem prevalence 17% vs 23%, 28% lower risk (OR 0.72, 95% CI 0.52-0.98)
  - "https://pubmed.ncbi.nlm.nih.gov/15320678/"  # Baker DG, Newton RU 2004, J Strength Cond Res 18(3):594-598 -- 42 rugby league players training both lifts: 1RM bench press / 1RM pull-up (bodyweight plus load) = 97.7% (SD 9.0), r = 0.81; individuals differ by up to 15%. Descriptive; no injury outcome
  - "https://sponet.de/sponet/Record/4024315?lng=en"  # Appleby B, Hori N 2011, J Sci Med Sport 14(7S):96 (conference abstract) -- bench press : bench pull 1RM 132% in 6 elite rugby union, 112% in 7 water polo players. Descriptive, tiny n
  - "https://pubmed.ncbi.nlm.nih.gov/27475532/"  # Barrett E, O'Keeffe M, O'Sullivan K, Lewis J, McCreesh K 2016, Man Ther 26:38-46 -- systematic review, 10 studies: moderate evidence of NO difference in thoracic kyphosis between people with and without shoulder pain
  - "https://pubmed.ncbi.nlm.nih.gov/20371564/"  # Lynch SS et al. 2010, Br J Sports Med 44(5):376-381 -- RCT, 28 collegiate swimmers, 8 weeks: posture programme reduced forward-head angle and forward-shoulder translation
  - "https://pubmed.ncbi.nlm.nih.gov/22387875/"  # Hibberd EE et al. 2012, J Sport Rehabil 21(3):253-265 -- RCT, 44 collegiate swimmers, 6 weeks of rows, Ts/Ys/Ws, external rotation and stretching: no between-group change in strength or scapular kinematics
  - "https://pubmed.ncbi.nlm.nih.gov/17606671/"  # Cools AM et al. 2007, Am J Sports Med 35(10):1744-1751 -- EMG, 45 healthy subjects: side-lying external rotation, side-lying forward flexion, prone horizontal abduction with external rotation and prone extension give the lowest upper/lower and upper/middle trapezius ratios. Activation only
  - "https://pubmed.ncbi.nlm.nih.gov/35438660/"  # Kassiano W et al. 2022, J Strength Cond Res 36(6):1753-1762 -- systematic review, 8 studies, 241 young men: systematic exercise variation can enhance regional hypertrophy and strength; redundant or random variation may hinder it. No back-muscle plane comparison among them
  - "exercise/regional-hypertrophy-exists-010"  # within-warehouse: regional growth follows regional loading
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: why pull-variant EMG rankings are not used here
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: present rotator-cuff-type pain loading rule
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the shoulder caution rung this row plugs into
  - "framework:GRADE -- no trial randomises lifters to different pull:push set ratios or to one vs both pull planes with a shoulder-injury or shoulder-pain outcome; no training study compares vertical against horizontal pulling for back-muscle growth. What exists is cross-sectional lifter data (Kolber), a prospective cohort and a cluster RCT in throwing athletes (Clarsen, Andersson), and descriptive strength ratios in rugby players (Baker, Appleby)."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
plane_coverage:
  - rule: both-pull-planes-weekly
    applies: any plan with upper-body training on 2 or more days a week
    requirement: at least one horizontal_pull and at least one vertical_pull exposure in the rotation week
    patterns: [horizontal_pull, vertical_pull]
    on_violation: soft penalty in the split scorer, never a hard block
    product_constant: true
    basis: exercise/regional-hypertrophy-exists-010
    basis_grade: D
  - rule: pull-sets-not-below-push-sets
    applies: weekly hard sets, healthy shoulder or any shoulder caution
    requirement: weekly sets of horizontal_pull plus vertical_pull at least equal to weekly sets of horizontal_push plus vertical_push
    ratio_floor: 1.0
    ratio_ceiling: none stated
    refused_ratios: [2:1, 3:1]
    on_violation: soft penalty; fill with a pull or an external-rotation / lower-trapezius accessory before cutting a press
    product_constant: true
    basis: exercise/pull-push-plane-balance-066
    basis_grade: D
  - rule: shoulder-caution-keep-pulls
    applies: shoulder site at any caution rung below current-other (056)
    requirement: keep horizontal_pull in the plan; never remove pulling to protect the shoulder
    patterns: [horizontal_pull]
    on_violation: hard rule for compose; pulls may change variant, not disappear
    product_constant: false
    basis: exercise/pull-push-plane-balance-066
    basis_grade: C
  - rule: shoulder-caution-add-cuff-and-lower-trap
    applies: shoulder site at any caution rung below current-other (056)
    requirement: add one external-rotation or lower-trapezius movement to the week
    movements: [side_lying_external_rotation, prone_horizontal_abduction_external_rotation, prone_extension, side_lying_forward_flexion]
    catalog_today: [band_external_rotation, cable_external_rotation]
    movements_note: the four named movements are the low upper-trapezius-ratio picks of Cools 2007 (EMG, not outcome); the catalog today carries only the two external-rotation entries
    on_violation: soft penalty
    product_constant: false
    basis: exercise/pull-push-plane-balance-066
    basis_grade: C
  - rule: shoulder-caution-no-high-five
    applies: shoulder site at any caution rung, or any reported shoulder instability
    requirement: exclude behind-the-neck variants of vertical_push and vertical_pull; front-of-head pressing and pulldowns are not excluded by this rule
    excluded_name_tokens: [behind_neck, behind_the_neck]
    catalog_note: no behind-the-neck variant is in the catalog today; the rule guards future entries and user-named lifts
    on_violation: exclude the variant
    product_constant: false
    basis: exercise/pull-push-plane-balance-066
    basis_grade: C
refraction_notes:
  - note: >
      THERE IS NO SOURCED PULL:PUSH PROGRAM RATIO. The 2:1 and 3:1 "pull
      twice what you press" rules circulate in coaching media; no study that
      sets them, or that tests them against a shoulder outcome, was found.
      Do not present them as evidence. What can be said: rugby league players
      who trained both lifts pressed about as much as they pulled (bench
      press about 98 percent of the weighted pull-up), and a pull-up that
      falls far short of the bench is a sign the pulling side has been
      under-trained, not a diagnosis.
    grade: D
  - note: >
      THE LIFTER SHOULDER PATTERN IS REAL BUT CROSS-SECTIONAL. Recreational
      weight trainers had greater agonist/antagonist strength ratios and less
      range of motion than non-lifters; lifters with impingement had weaker
      external rotators and lower trapezius than lifters without. This
      supports adding rotator-cuff and lower-trapezius work. It does not show
      that pulling more prevents shoulder pain.
    grade: C
  - note: >
      THE PROTECTIVE LEVER IS CUFF AND SCAPULAR STRENGTH, NOT ROWS ALONE. In
      handball players, weak external rotation and obvious scapular
      dyskinesis predicted shoulder problems, and a three-times-a-week
      programme of external-rotation and scapular strength plus rotation
      range cut shoulder-problem prevalence (17 vs 23 percent). Lifters are
      not throwers, so this is carried by analogy. Rows and pulldowns train
      the scapular retractors and the lats; they are not an external-rotator
      exercise.
    grade: C
  - note: >
      DO NOT SELL PULLING AS POSTURE CORRECTION FOR PAIN. Rounded upper-back
      posture did not differ between people with and without shoulder pain
      (moderate evidence). One swimmer trial changed posture, another found
      no change in scapular movement. The engine may say pulling balances the
      training week; it should not promise that rows fix posture or prevent
      shoulder pain through posture.
    grade: C
  - note: >
      BOTH PULL PLANES FOR THE BACK, FROM ANATOMY NOT A TRIAL. No training
      study compares vertical with horizontal pulling for back-muscle growth.
      Regional growth follows where a muscle is loaded, and systematic (not
      random) exercise variation helped regional hypertrophy in a review of
      eight trials. That makes "at least one row and one pulldown or pull-up
      a week" a sensible floor, not a proven requirement. EMG rankings of
      pull variants are not used to rank them.
    grade: D
  - note: >
      SHOULDER CAUTION: KEEP THE ROW, CHANGE THE POSITION. Weight trainers
      who did behind-the-neck pulldowns or presses showed more signs of
      anterior instability; those who trained external rotators showed fewer.
      For a shoulder caution, drop behind-the-neck variants, keep pulling,
      and add a cuff or lower-trapezius movement. This association does not
      show that ordinary front overhead pressing is harmful; how much
      overhead pressing a painful shoulder tolerates is the loading rule of
      055, not a plane ban.
    grade: C
claim: >
  No study sets a pull:push ratio for program design or tests one against a
  shoulder outcome; the circulating 2:1 and 3:1 rules are unsourced. Lifters
  who trained both lifts pressed about as much as they pulled (bench press
  about 98 percent of the weighted pull-up in rugby league players), which
  supports pulls at least matching pushes as a planning floor. Recreational
  weight trainers show greater agonist/antagonist strength ratios and less
  shoulder range than non-lifters, and lifters with impingement have weaker
  external rotators and lower trapezius; in throwing athletes external-rotation
  weakness and scapular dyskinesis predict shoulder problems and a cuff and
  scapular programme lowered them. So the shoulder-health lever is
  external-rotator and lower-trapezius work plus keeping pulls in the week,
  not a large pull surplus or posture correction. Back development plausibly
  benefits from both a horizontal and a vertical pull each week (regional
  hypertrophy, systematic variation), but no trial compares the planes. For a
  shoulder caution: keep pulling, add cuff and lower-trapezius work, and drop
  behind-the-neck variants.
reasoning: >
  The evidence is indirect at every step. Kolber's three lifter studies are
  cross-sectional or case-control, so they show the pattern a lifter's
  shoulder tends to carry, not that changing the push:pull mix prevents
  injury. The strongest causal evidence (Andersson 2017, cluster RCT; Clarsen
  2014, prospective) is in handball, and it points at external-rotation and
  scapular strength and rotation range, which rows and pulldowns only partly
  train. Baker 2004 and Appleby 2011 describe strength ratios in athletes
  without any injury outcome; they justify "pulls not below pushes" as a
  reasonable product floor and nothing stronger. The thoracic-posture review
  (Barrett 2016) and the mixed swimmer trials remove posture correction as a
  selling point. Plane coverage for the back rests on 010 and Kassiano 2022
  and is held at the practitioner floor because no plane comparison exists.
  The axis is soft with hedge: a shoulder caution changes the rules that
  apply, not whether general plane advice can be given.
---

# exercise/pull-push-plane-balance-066 -- 당기기·밀기, 수평·수직 균형

**한 줄 그림:** 당기기는 밀기보다 적지 않게, 노 젓기(수평)와 내려 당기기(수직)를 매주 하나씩.
어깨가 신경 쓰이면 당기기는 빼지 말고, 회전근개·하부승모근 운동을 더한다.

## plane_coverage (engine-readable)

| Rule | What compose checks | Violation | Basis strength |
|---|---|---|---|
| both-pull-planes-weekly | horizontal_pull 1회 이상 + vertical_pull 1회 이상 / 주 (상체 주 2일 이상) | soft penalty | practitioner floor |
| pull-sets-not-below-push-sets | 주간 pull 세트 ≥ push 세트 (floor 1.0, 상한 없음, 2:1·3:1 거부) | soft penalty, press 삭감보다 pull·보조 추가 먼저 | practitioner floor |
| shoulder-caution-keep-pulls | 어깨 caution(056 current-other 미만)에서 horizontal_pull 유지 | hard: 변형은 바꿔도 삭제 금지 | observational |
| shoulder-caution-add-cuff-and-lower-trap | 외회전 또는 하부승모근 동작 1개 / 주 | soft penalty | observational |
| shoulder-caution-no-high-five | behind-the-neck 프레스·풀다운 제외 (앞쪽 오버헤드는 이 규칙으로 제외 안 함) | 변형 제외 | observational |

Every count above is a product floor. None is a measured threshold.

## 한국어 요약 (답변용)

- "당기기를 밀기의 2배(또는 3배)" 같은 비율은 근거 논문을 찾지 못했다. 근거처럼 말하지 않는다.
  두 동작을 다 훈련한 럭비 선수들은 벤치프레스와 중량 턱걸이 1RM이 거의 같았다(벤치가 약 98%).
  그래서 계획 기준은 "당기기 세트가 밀기 세트보다 적지 않게" 정도다.
- 웨이트 하는 사람의 어깨는 운동 안 하는 사람보다 앞뒤 근력 비율이 한쪽으로 쏠리고 가동범위가
  줄어 있는 경향이 있었다. 어깨 충돌 증상이 있는 사람은 외회전근과 하부승모근이 더 약했다.
  다만 한 시점에 비교한 연구라 "당기기를 늘리면 어깨 통증이 예방된다"까지는 말할 수 없다.
- 어깨를 지키는 쪽으로 근거가 있는 건 외회전 근력과 날개뼈 조절이다. 핸드볼 선수에서 외회전이
  약하거나 날개뼈 움직임이 뚜렷이 흐트러진 사람이 어깨 문제가 더 많았다. 외회전·날개뼈 근력과
  회전 가동성을 주 3회 운동한 팀은 어깨 문제가 23%에서 17%로 줄었다. 던지는 종목이라
  웨이트에는 유추해서 적용한다. 로우와 풀다운은 외회전근 운동이 아니다.
- "등 운동으로 굽은 자세를 펴면 어깨가 안 아프다"는 말은 하지 않는다. 등 굽음 정도는 어깨가
  아픈 사람과 안 아픈 사람 사이에 차이가 없었다.
- 등 근육 발달을 위해 로우(수평)와 풀다운·턱걸이(수직)를 매주 하나씩 넣는 건 근육이 부하받는
  부위가 더 자란다는 연구에서 나온 추론이다. 두 방향을 직접 비교한 훈련 연구는 없다.
- 어깨가 신경 쓰이는 사람: 당기기는 빼지 않는다. 비하인드넥 풀다운·비하인드넥 프레스는 뺀다
  (이런 동작을 한 사람에게 어깨 앞쪽 불안정 징후가 더 많았다). 옆으로 누워 외회전, 엎드려
  팔 벌리기(엄지 위로), 엎드려 팔 뒤로 들기 같은 동작을 주 1회 이상 더한다. 앞쪽 오버헤드
  프레스 자체를 금지할 근거는 이 연구들에 없다. 지금 아픈 어깨에 얼마나 실을지는 055의 통증
  기준을 따른다.
