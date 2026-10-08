---
# Injury-caution sprint follow-up 2026-10-06 (dispatch kw-knee-joint). Fills
# the joint-cartilage hole 056 left open ("no graded loading row for
# cartilage yet"). Topic: front-of-knee (patellofemoral) pain and knee
# osteoarthritis pain in someone who lifts. It answers three questions for
# the split / caution code: is loading a painful knee harmful, what pain
# ceiling governs it, and how many knee days a week to keep. Companion: 058
# (squat depth and knee-friendly variants). This row does NOT cover a new
# knee trauma, swelling, locking, giving way or a ligament / meniscus
# picture -- those stay red-flag / pain-triage under 031 and 056.
#
# ladder_placement and knee_pain_monitoring are structured data for the
# caution code, same style as 056's decision_ladder. Pain numbers are 0-10
# ratings copied from the protocols named in `basis`; they are not loads.
id: exercise/knee-pain-symptom-guided-loading-057
domain: exercise
grade: B (exercise therapy treats patellofemoral pain and knee osteoarthritis -- consensus and guideline; heavy strength training no better than light for knee osteoarthritis pain); C (loading exercise does not harm knee cartilage, low certainty; the 2/10 knee ceiling comes from one uncontrolled adolescent cohort; 3 sessions a week from between-trial meta-regression); D (ladder placement and the adult-lifter application)
lane: "@clinical-physio"
locale: universal
as_of: 1995-2021
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/29925502/"  # Collins NJ et al. 2018, Br J Sports Med 52(18):1170-1178 -- 5th International Patellofemoral Pain Research Retreat consensus (41-expert panel, AMSTAR / PEDro graded inputs): exercise therapy recommended, especially hip-focused plus knee-focused exercise; isolated mobilisation and electrophysical agents not recommended. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/31475628/"  # Willy RW et al. 2019, J Orthop Sports Phys Ther 49(9):CPG1-CPG95 -- patellofemoral pain clinical practice guideline: pain worse with squatting, stairs, prolonged sitting, jumping, running. Record read only (full text 403); no recommendation letter from it is quoted here
  - "https://pubmed.ncbi.nlm.nih.gov/31095417/"  # Rathleff MS et al. 2019, Am J Sports Med 47(7):1629-1637 -- prospective cohort, n=151 adolescents (10-14 y) with PFP, no control arm: activity modification + pain monitoring + hip/knee exercise + graded return; activity ladder progressed only at "maximum 2 on NRS scale during, after, or the day after a given activity" (accepted manuscript, Methods, read at full text); 86% successful at 12 weeks, 81% at 12 months; hip and knee torque +20-33%. Secondary summaries quote "<4/10" -- the primary says 2
  - "https://pubmed.ncbi.nlm.nih.gov/31278997/"  # Bannuru RR et al. 2019, Osteoarthritis Cartilage 27(11):1578-1589 -- OARSI guideline: structured land-based exercise (with or without weight management) plus education are CORE treatment for knee OA. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/29934429/"  # Bricca A et al. 2019, Br J Sports Med 53(15):940-947 -- systematic review of RCTs, 9 trials / 14 comparisons, people at risk of or with knee OA: knee-joint-loading exercise "seems to not be harmful for articular cartilage" (thickness, volume, defects, GAG, collagen); evidence quality LOW. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/24574223/"  # Juhl C et al. 2014, Arthritis Rheumatol 66(3):622-636 -- 48 RCTs, knee OA, meta-regression: aerobic, resistance and performance exercise similar for pain (SMD 0.67 / 0.62 / 0.48); quadriceps-specific > general lower-limb (SMD 0.85 vs 0.39); supervised at least 3x/week > fewer (SMD 0.68 vs 0.41); no effect of intensity or session duration; similar regardless of radiographic severity or baseline pain. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/33591346/"  # Messier SP et al. 2021, JAMA 325(7):646-657 -- START RCT, n=377 adults >=50 y with knee OA: high-intensity vs low-intensity strength training vs attention control, 18 months -- no difference in WOMAC pain (5.1 vs 4.4 vs 4.9) or tibiofemoral compressive force; nonserious adverse events 53 / 30 / 4. Abstract read; per-session %1RM not read (PMC blocked)
  - "https://pubmed.ncbi.nlm.nih.gov/26564575/"  # Sandal LF et al. 2016, Osteoarthritis Cartilage 24(4):589-592 -- 8 weeks of supervised neuromuscular exercise twice weekly, knee/hip pain: pain 3.6 -> 2.6/10; the acute pre-to-post-session pain flare shrank each session, approaching none in the last weeks. Single-arm. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/7718008/"  # Kujala UM et al. 1995, Arthritis Rheum 38(4):539-546 -- 117 former elite athletes aged 45-68: radiographic knee OA 31% in weight lifters vs 3% in shooters; patellofemoral OA highest in weight lifters (28%); lifters' excess partly explained by high BMI; previous knee injury OR 4.73. Small, retrospective, one era of Olympic lifting. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/27707741/"  # Aasa U et al. 2017, Br J Sports Med 51(4):211-219 -- weightlifting and powerlifting injuries, 9 mostly low-quality studies: spine, shoulder and knee the commonest sites; 1.0-4.4 injuries per 1000 h. Abstract read
  - "https://bjsm.bmj.com/content/51/23/1679"  # Smith BE et al. 2017, Br J Sports Med 51(23):1679-1687 -- painful vs pain-free exercise in chronic musculoskeletal pain: small short-term benefit for painful exercise, no difference later (already carried in 055) estate-scrub:allow(cited author surname)
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: the Achilles 5/10 model this row deliberately does NOT reuse for the knee
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the ladder this row places the knee on
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: past knee injury as history
  - "exercise/harm-route-boundary-031"  # within-warehouse: red flags are routed, not coached
  - "exercise/knee-friendly-squat-depth-variants-058"  # within-warehouse: which squat depth and variants to swap to
  - "framework:GRADE -- that exercise helps patellofemoral pain and knee OA is consensus- and guideline-level; that knee loading does not harm cartilage is low-certainty RCT evidence on structure; the 2/10 knee ceiling is from one uncontrolled cohort in 10-14-year-olds; the 3x/week signal is between-trial meta-regression (observational across trials). No study was located in adult resistance-trained lifters with knee pain that tests a pain ceiling, a weekly frequency, or a squat-specific progression."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
ladder_placement:
  - picture: knee stiffness or occasional ache that does not limit training, no named diagnosis
    rung: mild
    knee_rule: prep only; no site weight
    basis: exercise/caution-severity-ladder-056
    basis_grade: D
  - picture: named past knee injury or surgery, now training without pain
    rung: history-old or history-recent by date (054)
    knee_rule: prep plus quadriceps and hip strengthening kept in the plan; ligament or meniscus history follows the ligament modifier in 056
    basis: exercise/injury-history-reinjury-risk-054
    basis_grade: C
  - picture: familiar front-of-knee pain, gradual onset, brought on by squatting, stairs, sitting, jumping or running, no trauma, no swelling, no locking, no giving way (patellofemoral picture), or knee osteoarthritis already diagnosed by a clinician
    rung: current-load-pain (knee variant)
    knee_rule: keep the knee loaded under the knee ceiling; swap to lower-patellofemoral-stress ranges and variants (058); keep knee exposure days; drop only the highest-load variants
    basis: exercise/knee-pain-symptom-guided-loading-057
    basis_grade: B
  - picture: present knee pain whose type the user cannot describe, pain at the side or back of the knee after a twist, or pain that does not fit the picture above
    rung: current-other
    knee_rule: close heavy knee loading at the site and route to pain-triage before choosing a split
    basis: exercise/harm-route-boundary-031
    basis_grade: D
  - picture: new trauma, swelling, locking or catching, giving way, night pain, numbness, sharp or rising pain, a hot or red knee
    rung: red-flag
    knee_rule: pain-triage; refer
    basis: exercise/harm-route-boundary-031
    basis_grade: D
knee_pain_monitoring:
  during_max: 2
  after_max: 2
  next_day_max: 2
  scale: 0-10 numeric rating
  weekly_trend: knee pain and stiffness not rising week to week
  breach_action: next knee exposure steps back one notch (shallower range, lower load, or a lower-stress variant from 058); do not drop the knee day
  progress_rule: progress one notch (range, load or variant) only after a week inside the ceiling
  basis: Rathleff 2019 (patellofemoral, adolescents, uncontrolled cohort)
  basis_grade: C
knee_exposure:
  knee_days_per_week: 2-3
  heavy_back_to_back: false
  basis: Juhl 2014 (knee OA, supervised at least 3x/week did better, between-trial); 055 spacing note
  basis_grade: C
refraction_notes:
  - note: >
      A PAINFUL KNEE IS TREATED BY LOADING IT. For front-of-knee
      (patellofemoral) pain, an expert consensus recommends exercise therapy,
      especially hip plus knee strengthening. For knee osteoarthritis, the
      international guideline makes structured land-based exercise a core
      treatment. So a familiar, non-traumatic knee ache without red flags
      maps to keep-loading-with-a-ceiling, the same direction as tendons in
      055, not to avoid-the-knee.
    grade: B
  - note: >
      LOADING DOES NOT WEAR OUT THE CARTILAGE. In trials of people at risk of
      or with knee osteoarthritis, knee-loading exercise did not harm
      cartilage thickness, defects or composition. Certainty is low (nine
      trials, imaging outcomes), but there is no trial signal of harm.
    grade: C
  - note: >
      THE KNEE CEILING IS STRICTER THAN THE TENDON ONE. The only tested knee
      pain-monitoring protocol (adolescent patellofemoral pain, 151 children,
      no control arm) let activity progress only at pain of at most 2 out of
      10 during, after and the day after. The Achilles model in 055 allows
      about 5. Until a knee trial tests the higher number, the engine uses 2
      for the knee and the 055 rule of "settled by next morning, not rising
      week to week". Applying this to adult lifters is by analogy.
    grade: C
  - note: >
      HEAVIER IS NOT BETTER FOR A PAINFUL ARTHRITIC KNEE. In an 18-month
      trial of 377 adults over 50 with knee osteoarthritis, high-intensity
      strength training reduced pain no more than low-intensity training,
      did not lower knee compressive force, and came with more minor adverse
      events. For knee osteoarthritis pain the plan starts at moderate loads;
      the highest-load knee variants are the first thing dropped.
    grade: B
  - note: >
      KEEP THE KNEE DAYS. In knee osteoarthritis trials, supervised exercise
      at least three times a week reduced pain more than fewer sessions
      (comparison across trials, not within one). The knee rung therefore
      keeps 2-3 knee exposure days a week, without heavy back-to-back days,
      and steps back range, load or variant on a breach rather than removing
      the day.
    grade: C
  - note: >
      EXPECT THE FLARE TO SHRINK. When people with knee pain start a
      supervised programme, the small rise in pain right after each session
      gets smaller session by session and was close to none by week eight.
      A mild flare in the first weeks that settles by next day is the
      expected course, not a breach.
    grade: C
  - note: >
      HEAVY LIFTING IS NOT KNEE-NEUTRAL OVER A CAREER. Former elite Olympic
      weight lifters had more knee osteoarthritis than shooters (31% vs 3%),
      mostly at the kneecap joint, partly explained by body mass. Small,
      retrospective, one era. It supports keeping quadriceps strength and
      technique work and not chasing maximal knee loads on a symptomatic
      knee; it does not show that recreational lifting causes arthritis.
    grade: C
  - note: >
      THE PICTURE COMES FROM THE USER'S WORDS. The knee variant of
      current-load-pain applies only when the user's words fit the
      patellofemoral picture (front of the knee, gradual, worse with squats,
      stairs or sitting, no trauma, swelling, locking or giving way) or
      a clinician has named knee osteoarthritis. Anything else, or any red
      flag word, stays current-other or red-flag under 056.
    grade: D
claim: >
  Front-of-knee (patellofemoral) pain and knee osteoarthritis pain are treated
  with exercise, not rest: an expert consensus recommends hip plus knee
  strengthening for patellofemoral pain and the international osteoarthritis
  guideline makes structured exercise a core treatment. Knee-loading exercise
  has not been shown to harm cartilage (low certainty). The only tested knee
  pain-monitoring protocol progressed activity at pain of at most 2/10
  during, after and the next day, stricter than the 5/10 Achilles model, and
  the engine uses 2 for the knee by analogy. For knee osteoarthritis,
  high-intensity strength training gave no more pain relief than
  low-intensity, with more minor adverse events, so a painful arthritic knee
  starts at moderate loads. Programmes run at least three times a week did
  better across trials, so the caution rung keeps 2-3 knee days a week
  without heavy back-to-back days and steps back range, load or variant on a
  breach instead of dropping days. On the 056 ladder this is a knee variant
  of current-load-pain, used only when the user's words fit the
  patellofemoral picture or a clinician has diagnosed osteoarthritis. Trauma,
  swelling, locking, giving way and other red flags stay with triage.
reasoning: >
  Collins 2018 and OARSI 2019 establish direction for the two commonest
  non-traumatic knee pains in adults, so the keep-loading default carries
  moderate confidence. Bricca 2019 answers the "am I wearing my cartilage
  down" fear with low-certainty imaging evidence and no harm signal. The
  ceiling is the weakest link: Rathleff 2019 is an uncontrolled adolescent
  cohort, but it is the one knee protocol whose number was read at the
  primary, and it is lower than 055's Achilles number; borrowing 5/10 for
  the knee would be an untested extrapolation in the less cautious
  direction, so 2 is used and the gap is logged. START (Messier 2021) is a
  large, long RCT and is the reason heavy loading is not the starting point
  for an arthritic knee; it was run in over-50s, not in trained lifters.
  Juhl 2014 provides the frequency signal, but as a between-trial
  meta-regression it shows association, not a tested dose. Kujala 1995 is
  the only located data on lifting and long-run knee osteoarthritis and is
  confounded by body mass. The injury_history axis is hard with
  block_specifics: without the user's words on what the knee pain is like,
  the knee ceiling and placement are withheld and the 056 triage route
  applies; age is a soft modifier because the osteoarthritis rows were
  tested in older adults.
---

# exercise/knee-pain-symptom-guided-loading-057 -- 무릎 앞쪽 통증·관절염이 있을 때 하체 운동

**한 줄 그림:** 무릎 앞쪽이 익숙하게 아프거나 관절염 진단을 받은 무릎은 쉬기보다 계속 쓰는 게 치료다.
통증은 10점 중 2점 안에서, 다음 날에도 2점 안에서 유지한다. 무릎 운동하는 날은 줄이지 않고 범위와
무게를 조절한다.

## Where the knee sits on the 056 ladder

| User's picture | Rung | What the plan does |
|---|---|---|
| stiffness or occasional ache, not limiting | mild | prep only |
| past knee injury or surgery, now pain-free | history-old / history-recent (054) | prep + quad and hip strengthening kept |
| familiar front-of-knee pain, gradual, worse with squats / stairs / sitting, no trauma, swelling, locking or giving way; or clinician-diagnosed knee OA | current-load-pain (knee variant) | keep loading under the knee ceiling, swap variants (058), keep knee days, drop highest-load variants |
| knee pain the user cannot describe, or side / back of knee after a twist | current-other | close heavy knee loading, pain-triage first |
| new trauma, swelling, locking, giving way, night pain, numbness, sharp or rising pain, hot or red knee | red-flag | pain-triage; refer |

## The knee ceiling (engine-readable)

| Check | Pass | Breach -> next knee exposure |
|---|---|---|
| pain during the session | at most 2/10 | one notch back: shallower range, lower load, or a lower-stress variant (058) |
| pain after the session | at most 2/10 | same |
| the next day | at most 2/10 | same |
| week to week | knee pain and stiffness not rising | same, and hold progression |
| progression | a full week inside the ceiling | then one notch forward (range, load or variant) |

Exposure: 2-3 knee days a week, no heavy back-to-back knee days. A breach
changes the content of the next knee day, not the number of knee days.

## 한국어 요약 (답변용)

- 무릎 앞쪽(슬개골 주변) 통증이나 무릎 관절염은 운동이 치료다. 슬개대퇴 통증에는 엉덩이와 무릎을 함께
  강화하는 운동을 권하는 전문가 합의가 있고, 관절염에는 국제 지침이 운동을 기본 치료로 둔다.
- 무릎에 부하를 주는 운동이 연골을 상하게 한다는 근거는 없다. 다만 연구 수가 적고 확실성은 낮다.
- 무릎 통증 기준은 힘줄보다 엄격하다. 운동 중·운동 후·다음 날 모두 10점 중 2점까지다. 아킬레스 힘줄에서
  쓰는 5점 기준을 무릎에 시험한 연구는 아직 없다. 2점 기준도 청소년 대상 연구에서 나온 숫자라 성인
  운동하는 사람에게는 유추해서 쓰는 것이다.
- 기준을 넘으면 다음 무릎 운동에서 한 단계 낮춘다. 범위를 얕게 하거나, 무게를 줄이거나, 무릎에 덜
  부담 가는 동작(058)으로 바꾼다. 무릎 운동하는 날을 빼는 게 아니다. 일주일 동안 기준 안에 있으면 한
  단계 올린다.
- 관절염 무릎은 무겁게 할수록 좋은 게 아니다. 50세 이상 377명을 18개월 본 연구에서 고강도 근력운동이
  저강도보다 통증을 더 줄이지 못했고, 가벼운 부작용은 더 많았다. 중간 무게로 시작한다.
- 무릎 운동은 주 2-3일 유지하고 무거운 날을 연달아 붙이지 않는다. 관절염 연구들에서 주 3회 이상 한
  프로그램이 더 효과가 좋았지만, 연구끼리 비교한 결과라서 이 횟수를 직접 시험한 건 아니다.
- 처음 몇 주는 운동 직후 살짝 더 아플 수 있다. 회차가 쌓일수록 줄어들고 8주쯤엔 거의 없어졌다.
  다음 날 가라앉으면 정상 경과다.
- 다쳐서 생긴 통증, 붓기, 무릎이 걸리거나 잠김, 빠지는 느낌, 밤에 아픈 통증, 저림, 날카롭거나 점점
  심해지는 통증, 열감·발적은 여기 해당하지 않는다. 먼저 통증 확인으로 보내고 진료를 권한다.
