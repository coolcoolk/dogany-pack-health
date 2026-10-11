---
# Injury-caution sprint follow-up 2026-10-06 (dispatch kw-knee-joint).
# Companion to 057: once the knee is on the knee variant of current-load-pain,
# WHICH depth, range and variant should the plan swap to. Also answers the
# healthy-knee question "is a deep squat bad for my knees". Evidence base is
# mostly biomechanical modelling in small samples of healthy people plus two
# small training trials, so this row is held at C / D. Machine / cable /
# dumbbell as categories have no knee-load comparison at all (GAPS.md).
#
# variant_swaps is structured data for the caution / exercise-selection code:
# ORDERINGS of patellofemoral load, never kilograms or risk figures.
id: exercise/knee-friendly-squat-depth-variants-058
domain: exercise
grade: C (patellofemoral stress by knee angle and exercise type, from biomechanical models; deep squats not shown harmful to healthy knees; half squats grow the quadriceps as much as full squats in one small trial); D (the variant swap order, the progression ladder, and machine / cable / dumbbell choices)
lane: "@clinical-physio"
locale: universal
as_of: 1998-2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/23821469/"  # Hartmann H, Wirth K, Klusemann M 2013, Sports Med 43(10):993-1008 -- literature review (>164 articles): highest retropatellar compressive force and stress at about 90 deg knee flexion in models and cadavers; deeper, the wrapping effect and larger contact area LOWER retropatellar stress; no realistic knee-force estimates beyond about 50 deg in the deep squat; concerns that deep squats cause chondromalacia or OA "unfounded"; authors argue half/quarter squats with supra-maximal loads favour degenerative change (argument, not data). Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/24673446/"  # Powers CM et al. 2014, J Orthop Sports Phys Ther 44(5):320-327 -- n=10 healthy, modelled PFJ stress: squat higher than knee extension at 60-90 deg; knee extension higher at 0-30 deg; variable-resistance knee extension lower than constant-resistance at 60-90 deg. Authors' conclusion: squat 45 -> 0 deg, variable-resistance knee extension 90 -> 45 deg to minimise PFJ stress. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/9565938/"  # Escamilla RF et al. 1998, Med Sci Sports Exerc 30(4):556-569 -- n=10 men at 12RM: squat and leg press (closed chain) PF and tibiofemoral compression greatest near full flexion; knee extension (open chain) PF force greatest mid-range, ACL tension only in open chain near full extension; squat about twice the hamstring activity of leg press and knee extension. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/14636100/"  # Fry AC, Smith JC, Schilling BK 2003, J Strength Cond Res 17(4):629-633 -- n=7 trained men, parallel squat at body-weight load: blocking the knees from passing the toes cut knee torque 150 -> 117 N.m but raised hip torque 28 -> 303 N.m with more trunk lean; "forces are inappropriately transferred to the hips and low-back region". Abstract read estate-scrub:allow(cited author surname)
  - "https://pubmed.ncbi.nlm.nih.gov/31230110/"  # Kubo K, Ikebukuro T, Yata H 2019, Eur J Appl Physiol 119(9):1933-1942 -- RCT n=17 men, 10 weeks, 2 days/week: full vs half squat -- knee extensor volume +4.9% vs +4.6% (no difference); gluteus maximus +6.7% vs +2.2% and adductors +6.2% vs +2.7% (full > half); full-squat 1RM +31.8% vs +11.3%. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/18978453/"  # Escamilla RF et al. 2008, J Orthop Sports Phys Ther 38(11):681-690 -- n=18 at 12RM: forward lunge PF force and stress rise with knee flexion; at 70-90 deg a SHORT step loads the PF joint more than a long step; with a stride more than without at 10-40 deg. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/35697336/"  # Escamilla RF et al. 2022, J Appl Biomech 38(4):210-220 -- n=16 forward lunge: PF load lower stepping up to a 10-cm platform than at ground level in deep flexion; authors' progression: 0-30 deg -> 0-60 deg -> long step deep to a 10-cm platform -> long step deep at ground level. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/29925502/"  # Collins NJ et al. 2018, Br J Sports Med 52(18):1170-1178 -- patellofemoral pain consensus: exercise therapy, especially hip plus knee, recommended (why hip work is part of every swap set)
  - "exercise/knee-pain-symptom-guided-loading-057"  # within-warehouse: the knee ceiling and ladder placement this row serves
  - "exercise/caution-severity-ladder-056"  # within-warehouse: exclude_grades and rung semantics
  - "exercise/quad-subregion-low-independence-014"  # within-warehouse: quad regions grow together, so range swaps cost little quad stimulus
  - "framework:GRADE -- PF stress curves are model outputs from 7-18 healthy participants (indirect for a painful knee, imprecise); the healthy-knee deep-squat conclusion is a narrative review; the hypertrophy cost of a shallower squat rests on one 17-person trial. No trial compares knee pain outcomes between squat depths, between machine, cable, dumbbell and barbell variants, or between knee-forward and knee-back squat styles in lifters."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
variant_swaps:
  - pattern: barbell back squat to depth
    pf_load_peak: high near 90 deg and in deep flexion under load
    knee_friendly_swap: same squat to about 45 deg (box or pin set at that height), then lower the box one notch at a time under the 057 ceiling
    keeps: quadriceps stimulus (Kubo 2019); loses some glute and adductor stimulus
    basis_grade: C
  - pattern: leg press, hack squat, pendulum squat (closed chain machines)
    pf_load_peak: highest near full flexion
    knee_friendly_swap: limit the bottom to about 45-60 deg with the machine stop or a shorter range; keep the load stable and controllable
    keeps: quadriceps stimulus with no balance demand
    basis_grade: D
  - pattern: leg extension (open chain)
    pf_load_peak: highest from mid-range to full extension (0-45 deg)
    knee_friendly_swap: work the 90 -> 45 deg range; a variable-resistance (cam) machine is lower stress than constant resistance in deep flexion
    keeps: isolated quadriceps loading in the range where the squat is hardest on the PF joint
    basis_grade: C
  - pattern: forward lunge, split squat, step-up with dumbbells
    pf_load_peak: rises with knee flexion; short step higher in deep flexion
    knee_friendly_swap: long step, no stride, shallow range first; step up to a low (about 10 cm) platform before going deep at ground level
    keeps: single-leg quadriceps and glute work
    basis_grade: C
  - pattern: hip-dominant work (Romanian deadlift, hip thrust, cable pull-through, hip abduction machine or cable)
    pf_load_peak: low at the PF joint
    knee_friendly_swap: kept or added in every knee swap set; hip plus knee is the consensus treatment for front-of-knee pain
    keeps: glute and hamstring stimulus lost from shallower squats
    basis_grade: B
  - pattern: blocking the knees behind the toes in a squat
    pf_load_peak: lower knee torque
    knee_friendly_swap: not a default cue; it moves load to the hips and lower back (hip torque about tenfold in Fry 2003); use only as a short-term knee swap for someone with no back caution
    keeps: squat pattern with a hip bias
    basis_grade: C
refraction_notes:
  - note: >
      A DEEP SQUAT IS NOT BAD FOR A HEALTHY KNEE. In models and cadaver
      data, pressure behind the kneecap peaks around 90 degrees and falls
      again deeper, as the tendon wraps and the contact area grows. A review
      of more than 160 articles found the fear that deep squats cause
      cartilage damage or arthritis unfounded. For a knee without pain,
      depth is a training choice, not a caution.
    grade: C
  - note: >
      FOR A PAINFUL KNEE, CHANGE THE RANGE BEFORE CHANGING THE DAY. In a
      modelling study, squatting from standing to about 45 degrees and
      doing leg extensions from 90 to 45 degrees kept kneecap stress lowest;
      the squat is hardest on the kneecap deep, the leg extension near
      straight. So a knee on the knee variant of current-load-pain swaps to
      those ranges and works back toward full range one notch at a time
      under the 057 ceiling.
    grade: C
  - note: >
      THE SHALLOW SQUAT KEEPS THE QUADRICEPS GAIN. In a 10-week trial, half
      squats grew the thigh-front muscles as much as full squats; full squats
      grew the glutes and inner thigh more. A knee-friendly range costs
      little quadriceps stimulus; add hip work to cover the rest.
    grade: C
  - note: >
      "KNEES BEHIND THE TOES" MOVES THE LOAD, IT DOES NOT REMOVE IT. Blocking
      the knees from travelling forward cut knee torque by about a fifth but
      multiplied hip torque roughly tenfold, with more trunk lean. It is not
      a default squat cue, and it is a poor swap for anyone who also has a
      low-back caution.
    grade: C
  - note: >
      LUNGES AND STEP-UPS: LONG STEP, LOW STEP FIRST. A longer forward step
      puts less load behind the kneecap in deep flexion than a short one,
      and stepping up to a low platform less than lunging at ground level.
      The progression is shallow range, then moderate range, then deep to a
      low platform, then deep at ground level.
    grade: C
  - note: >
      MACHINE, CABLE OR DUMBBELL IS NOT ITSELF THE KNEE LEVER. No study
      compares knee pain or kneecap load between the same movement done with
      a machine, a cable, dumbbells or a barbell. What the evidence speaks to
      is knee angle, step length and hip-versus-knee bias. Machines are
      useful because a stop can fix the range and the load is easy to dial;
      that is a practical choice, not a measured knee benefit.
    grade: D
claim: >
  For a healthy knee, a deep squat has not been shown to harm cartilage:
  modelled pressure behind the kneecap peaks near 90 degrees and falls deeper.
  For a painful front of the knee, kneecap stress depends on knee angle and
  exercise type: squats and leg presses are hardest on the kneecap deep in
  flexion, leg extensions near straight, so the lowest-stress ranges are a
  squat from standing to about 45 degrees and a leg extension from 90 to 45
  degrees (variable-resistance machine lower than constant). A half squat
  grew the quadriceps as much as a full squat in a small trial, so a shallower
  range costs little quadriceps stimulus; hip-dominant work covers the glute
  and adductor gain and is part of the consensus treatment. Lunges load the
  kneecap less with a long step and when stepping to a low platform. Blocking
  the knees behind the toes shifts load to the hips and lower back rather than
  removing it. Machine, cable and dumbbell versions have not been compared for
  knee load; their value is that range and load are easy to control.
reasoning: >
  The PF stress curves (Powers 2014, Escamilla 1998, 2008, 2022) are model
  estimates from small healthy samples, consistent with each other on
  direction (closed chain hardest deep, open chain hardest near extension;
  lunge load rises with flexion), so they hold at C for the ordering and are
  indirect for a painful knee. Hartmann 2013 is a narrative review and
  itself notes no realistic force estimates beyond about 50 degrees in the
  deep squat; its "deep squats are safe" conclusion is carried for healthy
  knees only, and its claim that heavy partial squats favour degeneration is
  not carried as a rule because it is argument rather than data. Kubo 2019
  is the one located trial measuring what a shallower squat costs in muscle,
  in 17 men (training status not read); 014 explains why the quadriceps grow
  as a unit. Fry 2003 (7 men) is the reason the knee-behind-toes cue is not
  a default. The swap table's order and the machine / cable / dumbbell
  remarks are practitioner judgement built on those curves (D). The
  injury_history axis is soft with hedge: the healthy-knee note needs no
  history, and the swap rules are triggered by 057's placement, which
  carries the hard gate.
---

# exercise/knee-friendly-squat-depth-variants-058 -- 깊은 스쿼트는 무릎에 나쁜가, 무릎이 아프면 무엇으로 바꾸나

**한 줄 그림:** 아프지 않은 무릎에는 깊은 스쿼트가 해롭다는 근거가 없다. 무릎 앞쪽이 아프면 날을 빼지 말고
범위를 바꾼다. 스쿼트는 0-45도, 레그 익스텐션은 90-45도로 하고, 엉덩이 운동을 더한다.

## Variant swap order (engine-readable)

| Pattern | Kneecap load is highest | Knee-friendly swap | Evidence |
|---|---|---|---|
| barbell back squat | near 90 deg / deep under load | squat to about 45 deg (box or pins), lower one notch at a time | model + small trial |
| leg press / hack / pendulum | near full flexion | machine stop at about 45-60 deg | practitioner |
| leg extension | 0-45 deg (near straight) | 90 -> 45 deg; cam (variable) machine over constant | model |
| lunge / split squat / step-up (dumbbells) | deep flexion, short step | long step, no stride; low platform before deep at ground | model |
| hip-dominant (RDL, hip thrust, cable pull-through, abduction) | low | keep or add in every swap set | consensus |
| knees blocked behind toes | -- | not a default; shifts load to hip and low back | small study |

Progression back to full range: one notch at a time, only after a week
inside the 057 knee ceiling.

## 한국어 요약 (답변용)

- 무릎이 아프지 않다면 깊은 스쿼트가 연골을 상하게 하거나 관절염을 만든다는 근거는 없다. 슬개골 뒤쪽
  압력은 90도 근처에서 가장 높고 그보다 깊이 앉으면 오히려 줄어든다는 계산 결과가 있다. 깊이는 훈련
  목적에 따라 고르면 된다.
- 무릎 앞쪽이 아프면 운동하는 날을 빼지 말고 범위를 바꾼다. 스쿼트는 서 있는 자세에서 45도 정도까지,
  레그 익스텐션은 90도에서 45도까지 하는 게 슬개골 부담이 가장 적었다. 스쿼트는 깊을수록, 레그
  익스텐션은 다리를 다 펼수록 부담이 커진다.
- 하프 스쿼트도 허벅지 앞 근육은 풀 스쿼트만큼 컸다(10주, 17명). 엉덩이와 안쪽 허벅지는 풀 스쿼트가 더
  컸으니 루마니안 데드리프트, 힙 쓰러스트, 케이블 풀스루, 힙 어브덕션 같은 엉덩이 운동을 더한다. 엉덩이와
  무릎을 같이 강화하는 게 무릎 앞쪽 통증의 권장 치료이기도 하다.
- 런지와 스플릿 스쿼트는 보폭을 길게 하고, 깊게 내려가기 전에 낮은 단(10cm 정도)에 올라서는 동작부터
  한다. 얕은 범위 → 중간 범위 → 낮은 단으로 깊게 → 바닥에서 깊게 순서로 올린다.
- "무릎이 발끝을 넘으면 안 된다"는 규칙은 부담을 없애는 게 아니라 엉덩이와 허리로 옮긴다. 한 연구에서
  무릎 부담은 5분의 1쯤 줄었지만 엉덩이 부담은 약 10배가 됐다. 기본 자세 지시로 쓰지 않고, 허리도 조심해야
  하는 사람에게는 쓰지 않는다.
- 머신, 케이블, 덤벨이라서 무릎에 더 좋다는 비교 연구는 없다. 머신은 멈춤 장치로 범위를 고정하고 무게를
  조절하기 쉬워서 쓰기 편할 뿐이다.
- 범위는 057의 무릎 통증 기준(운동 중·후·다음 날 10점 중 2점까지)을 일주일 지키면 한 단계씩 넓힌다.
