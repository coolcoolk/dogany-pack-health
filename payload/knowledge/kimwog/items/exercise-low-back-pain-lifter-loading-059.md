---
# Injury-caution sprint follow-up 2026-10-06 (GAPS.md v36: "low-back pain has
# no loading row in this warehouse ... deserves its own row"). The low back /
# pelvis is the commonest injury site in powerlifting and among the top sites
# in weightlifting (Tung 2024), yet 056 has no tissue for it, so any present
# back pain falls to current-other (close the site, triage). For non-specific
# back pain the trial and guideline evidence says the opposite default: stay
# active, keep exercising, and keep loading the hinge at a dose the back
# tolerates. This row says where low-back pain sits on the 056 ladder, which
# lifts change first, and which cues are red flags. Population caveat up
# front: the treatment evidence is general-population (primary-care) back
# pain plus one small Swedish deadlift trial; no trial in competitive lifters.
#
# ladder_mapping, modify_order and red_flags are structured data for the
# split / caution code (site key lower_back; see
# docs/kimwog-caution-ladder-fields.md, Rule 7). Values are DIRECTIONS and
# ORDERINGS, never loads in kilograms and never risk figures.
id: exercise/low-back-pain-lifter-loading-059
domain: exercise
grade: B (stay active and exercise over rest; exercise plus education prevents new episodes); C (deadlift-based loading as treatment, flexion while lifting not a risk factor, recurrence base rate); D (the ladder mapping and the modify-first order for a lifter)
lane: "@clinical-physio"
locale: universal
as_of: 2010-2024
contested: no
sources:
  - "https://cochranelibrary.com/cdsr/doi/10.1002/14651858.CD007612.pub2/information"  # Dahm KT, Brurberg KG, Jamtvedt G, Hagen KB 2010, Cochrane CD007612 -- 10 RCTs, n=1923, acute LBP < 6 weeks: advice to stay active gives small improvements in pain and function over advice to rest in bed (moderate quality); for sciatica little or no difference between the two
  - "https://www.cochrane.org/CD009790/BACK_exercise-therapy-chronic-low-back-pain"  # Hayden JA et al. 2021, Cochrane CD009790 -- chronic non-specific LBP: exercise vs no treatment / usual care / placebo, pain MD -15.2 (95% CI -18.3 to -12.2) on 0-100 at earliest follow-up, moderate certainty, clinically important
  - "https://bjsm.bmj.com/content/54/21/1279.abstract"  # Owen PJ et al. 2020, Br J Sports Med 54(21):1279-1287 -- network meta-analysis, 89 RCTs, n=5578, chronic LBP: no single best mode; Pilates, resistance training and stabilisation / motor control best for pain; resistance and stabilisation best for function
  - "https://wrap.warwick.ac.uk/id/eprint/100520"  # Foster NE et al. 2018, Lancet 391(10137):2368-2383 -- Lancet LBP series: guidelines converge on education, self-management, resumption of normal activity and exercise first; prudent imaging; evidence-practice gap includes overuse of rest and imaging
  - "https://search.pedro.org.au/search-results/record-detail/41745"  # Aasa B, Berglund L, Michaelson P, Aasa U 2015, J Orthop Sports Phys Ther 45(2):77-85 -- RCT n=70 recurrent mechanical (nociceptive) LBP: high-load lifting (deadlift) + education vs individualised low-load motor control + education, 12 sessions / 8 weeks; both improved pain, strength and endurance; motor control group better on Patient-Specific Functional Scale and movement-control tests
  - "https://www.medicaljournals.se/jrm/content/abstract/10.2340/16501977-2091"  # Michaelson P, Holmberg D, Aasa B, Aasa U 2016, J Rehabil Med 48(5) -- same trial at 2, 12 and 24 months: no significant difference between high-load lifting and low-load motor control on any outcome; 50-80% in both arms reported less pain and disability
  - "https://pubmed.ncbi.nlm.nih.gov/25559899/"  # Berglund L, Aasa B, Hellqvist J, Michaelson P, Aasa U 2015, J Strength Cond Res 29(7):1803-1811 -- deadlift arm (n=35) secondary analysis: lower baseline pain, lower disability and better Biering-Sorensen back-extensor endurance predicted benefit; Sorensen in every model. The cut-offs that circulate (pain < 60/100, Sorensen > 60 s) were NOT in the abstract read and are not carried (GAPS.md)
  - "https://pubmed.ncbi.nlm.nih.gov/31775556/"  # Saraceni N, Kent P, Ng L, Campbell A, Straker L, O'Sullivan P 2020, J Orthop Sports Phys Ther 50(3):121-130 -- SR/MA, 13 studies: low-quality evidence that greater lumbar flexion during lifting is not a risk factor for LBP onset or persistence; 9/11 studies no group difference
  - "https://bjsm.bmj.com/content/51/23/1679"  # Smith BE et al. 2017, Br J Sports Med 51(23):1679-1687 -- chronic musculoskeletal pain (back pain trials included): exercise into pain vs pain-free, small short-term benefit for painful exercise (moderate quality), no difference later; the basis for a ceiling over zero pain estate-scrub:allow(cited author surname)
  - "https://pubmed.ncbi.nlm.nih.gov/31208917/"  # da Silva T et al. 2019, J Physiother 65(3):159-165 -- inception cohort n=250 recovered from LBP: 69% (95% CI 62-74) recur within 12 months, 40% activity-limiting; median 139 days; > 2 previous episodes predicts recurrence
  - "https://researchers.mq.edu.au/en/publications/prevention-of-lowback-pain-a-systematic-review-and-meta-analysis/"  # Steffens D et al. 2016, JAMA Intern Med 176(2):199-208 -- 23 RCTs, n=30,850: exercise + education RR 0.55 (0.41-0.74) for a new LBP episode (moderate quality), exercise alone RR 0.65 (0.50-0.86) (low to very low); education alone, back belts (RR 1.01) and insoles no effect. Belt trials are occupational, not lifting-performance belts
  - "https://pubmed.ncbi.nlm.nih.gov/32438853/"  # Finucane LM et al. 2020, J Orthop Sports Phys Ther 50(7):350-372 -- IFOMPT international framework for red flags for potential serious spinal pathology (cauda equina, fracture, malignancy, infection); most single red flags lack diagnostic-accuracy evidence, so they work as a clinical-reasoning cluster
  - "https://researchers.mq.edu.au/en/publications/red-flags-to-screen-for-malignancy-and-fracture-in-patients-with--2/"  # Downie A et al. 2013, BMJ 347:f7095 -- 14 studies: fracture more likely with older age, prolonged corticosteroid use, severe trauma, contusion / abrasion (several together raise it more); history of malignancy the most informative cancer flag (post-test 33%)
  - "https://pubmed.ncbi.nlm.nih.gov/39650568/"  # Tung MJ, Lantz GA, Lopes AD, Berglund L 2024, BMJ Open Sport Exerc Med -- updated SR, 17 reports: powerlifting 1.0-4.4 injuries / 1000 h, lower back / pelvis the commonest site; weightlifting knee, lower back, shoulder; point prevalence 70% when injury = pain that impairs training
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC5954586"  # Stromback E, Aasa U, Gilenstam K, Berglund L 2018, Orthop J Sports Med 6(5) -- 104 Swedish subelite powerlifters: 70% currently injured, lumbopelvic region among the commonest sites; 81% of the injured altered training, only 16% stopped completely; commonest alteration was less volume / intensity or omitting certain exercises (descriptive, cross-sectional)
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC6059276/"  # Bengtsson V, Berglund L, Aasa U 2018, BMJ Open Sport Exerc Med 4(1):e000382 -- narrative review: lifters attribute 22-32% of injuries to the squat, 18-46% to the bench and 12-31% to the deadlift; no article reported a documented thoracic / lumbar structural injury; bar-close and fatigue mechanisms are biomechanical, not injury-outcome, evidence
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the ladder this row places the low back on
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: the pain-monitoring ceiling borrowed by analogy
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: history weight; recurrence here is the back-specific case
  - "exercise/harm-route-boundary-031"  # within-warehouse: red flags are routed, not coached through
  - "framework:GRADE -- stay-active-over-rest and exercise-for-chronic-LBP rest on Cochrane reviews (moderate certainty) in general-population back pain; deadlift-as-treatment rests on one trial (n=70, mechanical LBP, physio-supervised), no difference from motor control at 24 months; flexion-while-lifting is low-quality observational; no trial in competitive lifters compares modifying vs pausing the hinge, or ranks which lift to change first. The ladder mapping and the modify-first order are practitioner synthesis."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
ladder_mapping:
  - picture: familiar non-specific low-back ache or stiffness, no leg symptoms below the knee, no red flag, can hinge with at most moderate pain
    site: lower_back
    maps_to: current-load-pain
    lumbar_override: keep training; modify the heaviest hinge and squat first (modify_order); the 055 ceiling applies by analogy; walking and other activity encouraged
    basis: Dahm 2010, Hayden 2021, Aasa 2015 / Michaelson 2016
    basis_grade: D
  - picture: new acute episode, pain sharp on bending or lifting, cannot hinge an empty bar without sharp pain, no red flag
    site: lower_back
    maps_to: current-other
    lumbar_override: stay active (walking, unloaded movement, upper body and machine work that does not provoke); no heavy hinge or loaded squat at the site until bending is tolerable; re-check each session, not a fixed rest period; not bed rest
    basis: Dahm 2010, Foster 2018
    basis_grade: D
  - picture: back pain with pain, tingling or numbness spreading below the knee (sciatica-type), no motor or bladder signs
    site: lower_back
    maps_to: current-other
    lumbar_override: pain-triage before heavy axial loading; staying active is still advised; this row does not license training through leg symptoms
    basis: Dahm 2010 (little difference rest vs active in sciatica), Finucane 2020
    basis_grade: D
  - picture: any red_flags cue
    site: lower_back
    maps_to: red-flag
    lumbar_override: stop the site; refer; cauda-equina cues are same-day urgent
    basis: Finucane 2020, Downie 2013
    basis_grade: D
  - picture: recovered episode, back pain-free now, last episode within the product window
    site: lower_back
    maps_to: history-recent
    lumbar_override: keep all lifts; prep plus back-extensor and trunk endurance work; recurrence is the base rate, not the exception
    basis: da Silva 2019, Steffens 2016
    basis_grade: C
  - picture: recovered episode longer ago, or recurrent episodes but none current
    site: lower_back
    maps_to: history-old
    lumbar_override: more than two previous episodes is a recurrence predictor -- treat as history-recent instead
    basis: da Silva 2019
    basis_grade: C
modify_order:
  - step: 1
    action: lower load and effort on the heaviest axial hinge and squat (conventional deadlift from the floor, good morning, heavy back squat) -- fewer top sets, more reps in reserve, slower controlled tempo; keep the movement
    basis_grade: D
  - step: 2
    action: shorten or change the range or the lever (block or rack pull, trap-bar deadlift, Romanian deadlift to tolerance, box squat or front squat) when step 1 still breaches the ceiling
    basis_grade: D
  - step: 3
    action: swap to a lower-axial-load variant for the pattern (hip thrust or glute bridge, back extension at tolerance, split squat, machine-supported leg work) while keeping the hinge pattern itself at an unloaded or light dose
    basis_grade: D
  - step: 4
    action: spread the remaining hinge and squat work across the week rather than stacking heavy hinge and heavy squat on consecutive days; cut exposure days only at current-other or red-flag
    basis_grade: D
  - step: always
    action: keep upper-body, non-provoking lower-body work and walking or other aerobic activity; add back-extensor and trunk endurance work; progress back toward the original lift as the ceiling holds
    basis_grade: C
red_flags:
  - cue_en: numbness or altered feeling in the saddle area (groin, buttocks, inner thighs)
    cue_ko: 사타구니·엉덩이 안쪽 감각이 둔하거나 이상함
    suspect: cauda equina
    action: same-day urgent care
  - cue_en: new difficulty passing urine, loss of bladder or bowel control, new sexual dysfunction
    cue_ko: 소변이 잘 안 나오거나 대소변을 참기 어려움, 새로 생긴 성기능 이상
    suspect: cauda equina
    action: same-day urgent care
  - cue_en: weakness in one or both legs, foot drop, or numbness in both legs, especially if getting worse
    cue_ko: 한쪽 또는 양쪽 다리 힘 빠짐, 발목이 들리지 않음, 양쪽 다리 저림이 심해짐
    suspect: progressive neurological deficit
    action: urgent referral
  - cue_en: back pain after a fall, crash or heavy impact, or with osteoporosis, long-term steroid use or older age
    cue_ko: 넘어지거나 부딪힌 뒤 생긴 허리 통증, 골다공증·장기 스테로이드 복용·고령
    suspect: fracture
    action: refer before loading
  - cue_en: history of cancer, unexplained weight loss, or constant pain at night not eased by rest or position
    cue_ko: 암 병력, 이유 없는 체중 감소, 자세를 바꿔도 가라앉지 않는 밤 통증
    suspect: malignancy
    action: refer
  - cue_en: fever, feeling unwell, recent infection or injecting drug use with back pain
    cue_ko: 열·몸살 기운, 최근 감염, 주사 약물 사용과 함께 오는 허리 통증
    suspect: infection
    action: refer
refraction_notes:
  - note: >
      REST IS NOT THE TREATMENT. For acute back pain, advice to stay active
      gave small gains in pain and function over advice to rest in bed; for
      chronic non-specific back pain, exercise cut pain by about 15 points
      out of 100 against no treatment. Guidelines put activity and exercise
      first. So a familiar back ache without red flags changes how the lifter
      trains, not whether they train. For sciatica-type leg pain, the review
      found little difference either way; that picture goes to triage first.
    grade: B
  - note: >
      THE DEADLIFT IS A TREATMENT OPTION, NOT A BANNED LIFT. In recurrent
      mechanical back pain, a supervised deadlift programme improved pain,
      strength and endurance and matched individualised low-load motor
      control at 2, 12 and 24 months (motor control did better on the
      patients' own activity goals at 2 months). Who did best on the
      deadlift: lower pain, lower disability, better back-extensor
      endurance. So with higher pain or poor back endurance, start the hinge
      lighter, or from low-load control work, and build up. One trial of 70,
      with physio supervision.
    grade: C
  - note: >
      DO NOT SELL "NEVER ROUND YOUR BACK" AS INJURY PREVENTION. Low-quality
      evidence finds that more lumbar flexion while lifting is not a risk
      factor for back pain starting or persisting. Technique cues are fine as
      performance and load-control cues; they are not the claim that a
      rounded rep caused or will cause the pain. Modify by load, range and
      variant (modify_order), not by chasing a posture.
    grade: C
  - note: >
      CHANGE THE HEAVIEST AXIAL LIFT FIRST, THEN THE RANGE, THEN THE VARIANT.
      Lifters attribute back-and-other injuries to the squat about as often
      as to the deadlift, and most injured powerlifters keep training by
      cutting volume or intensity or dropping certain exercises; few stop
      completely. That is the order modify_order encodes: load and effort,
      then range or lever, then a lower-axial swap, then spread across the
      week, with exposure cut only at the triage rungs. This is practitioner
      synthesis plus descriptive survey data, not a trial that ranks options.
    grade: D
  - note: >
      THE PAIN CEILING IS BORROWED. The 055 rule (about 5/10 during and after,
      back to usual by next morning, not rising week to week) was tested on
      the Achilles; using it for the low back is by analogy. Exercise into
      some pain was not worse than pain-free exercise in a meta-analysis that
      included chronic back pain, which supports a ceiling over zero pain,
      but no back trial tested this exact rule.
    grade: D
  - note: >
      AFTER AN EPISODE, EXPECT IT BACK. About two thirds of people recovered
      from back pain had another episode within 12 months (40% activity-
      limiting); more than two previous episodes predicted recurrence.
      Exercise with education cut the risk of a new episode by about 45%;
      back belts did not prevent back pain in the (occupational) trials.
      So a recovered back stays history-recent for the product window, keeps
      its prep and trunk endurance work, and repeated episodes do not decay
      to history-old. Whether a lifting belt changes back-pain risk in
      lifters was not studied.
    grade: B
  - note: >
      RED FLAGS ARE A CLUSTER, NOT A CHECKLIST SCORE. Most single red flags
      have weak diagnostic accuracy; older age, steroids, trauma and bruising
      raise fracture likelihood, and a cancer history is the strongest
      malignancy flag. Cauda-equina cues (saddle numbness, bladder or bowel
      change, both legs weak or numb) override everything and are same-day.
      The engine names the cue and routes; it never rules a red flag out.
    grade: D
claim: >
  Low-back pain in a lifter is placed on the 056 ladder by its picture, not
  by the site alone. A familiar, non-specific back ache or stiffness without
  leg symptoms or red flags maps to current-load-pain: keep training, keep
  hinging at a tolerated dose under the borrowed 055 pain ceiling, and change
  the heaviest axial lifts first (load and effort, then range or lever, then a
  lower-axial swap, then spread the remaining hinge and squat work across the
  week). A new sharp episode that stops the lifter hinging an empty bar, or
  pain spreading below the knee, maps to current-other: stay active, no heavy
  hinge or loaded squat, triage the leg symptoms, no bed rest. Saddle
  numbness, bladder or bowel change, progressive leg weakness, trauma or
  osteoporosis, cancer history, night pain or fever are red flags and are
  referred; cauda-equina cues the same day. Staying active beats bed rest,
  exercise treats chronic back pain, a supervised deadlift programme worked
  as well as low-load motor control, flexion while lifting has not been
  shown to cause back pain, about two thirds of recovered backs flare again
  within a year, and exercise with education lowers that risk. The ladder
  mapping and the modify-first order are practitioner synthesis; no trial in
  lifters ranks them.
reasoning: >
  Without this row, 056 has no tissue for the lower back and every present
  back pain falls to current-other, which closes the site. That is the
  bed-rest default the back-pain evidence argues against. Dahm 2010 and
  Hayden 2021 carry the stay-active and exercise direction at moderate
  certainty in general populations, and Foster 2018 shows guidelines agree.
  The lifter-specific piece is thin: Aasa 2015 / Michaelson 2016 is one
  70-person trial showing a deadlift programme is a legitimate treatment, and
  Berglund 2015 says who is more likely to benefit (lower pain, better back
  endurance), which is why the high-pain picture starts lighter instead of
  being barred. Saraceni 2020 removes the flexion-causes-pain premise behind
  many technique-based bans, at low quality. Tung 2024, Stromback 2018 and
  Bengtsson 2018 are descriptive: the low back is the commonest powerlifting
  site, lifters mostly modify rather than stop, and the squat is implicated
  as often as the deadlift, so the modify order targets heavy axial loading
  in general, not the deadlift alone. da Silva 2019 and Steffens 2016 justify
  keeping a recovered back on history-recent with endurance work. The red
  flags follow the IFOMPT framework (Finucane 2020) with Downie 2013's
  accuracy caveat. The axis is hard with block_specifics: until the user's
  words place the back pain in one picture, the specific modify steps and the
  ceiling are withheld and the triage route applies.
---

# exercise/low-back-pain-lifter-loading-059 -- 허리가 아픈데 운동해도 되나, 데드리프트는

**한 줄 그림:** 익숙한 허리 통증이고 위험 신호가 없으면 쉬지 말고 계속 운동한다. 가장 무거운
데드리프트·스쿼트부터 무게, 범위, 동작 순서로 바꾼다. 다리로 뻗치는 통증이나 위험 신호가 있으면
먼저 확인부터 한다.

## Where the low back sits on the 056 ladder

| Picture (user's words) | 056 rung | What changes |
|---|---|---|
| familiar ache / stiffness, no leg symptoms, no red flag | current-load-pain | keep training; modify_order steps 1-4; 055 ceiling by analogy |
| new sharp episode, cannot hinge an empty bar | current-other | stay active; no heavy hinge / loaded squat until bending is tolerable; no bed rest |
| pain or tingling below the knee | current-other | pain-triage before heavy axial loading |
| any red-flag cue | red-flag | stop the site, refer; cauda-equina cues same day |
| recovered, last episode inside the product window | history-recent | keep the lifts, add back-extensor / trunk endurance |
| recovered longer ago | history-old | history-recent instead if more than two past episodes |

## Modify first (in this order)

1. Load and effort on the heaviest axial hinge and squat (fewer top sets, more reps in reserve, controlled tempo).
2. Range or lever (block / rack pull, trap bar, Romanian deadlift to tolerance, box or front squat).
3. Lower-axial swap (hip thrust, back extension at tolerance, split squat, machine-supported leg work), hinge pattern kept light.
4. Spread the remaining hinge and squat work across the week; cut exposure days only at current-other or red-flag.

Always: keep upper body, walking and non-provoking work; add trunk and back-extensor endurance; step back up as the ceiling holds.

## 한국어 요약 (답변용)

- 허리가 아프다고 쉬는 게 치료는 아니다. 급성 허리 통증에서 침대에서 쉬라는 조언보다 평소처럼
  움직이라는 조언이 통증과 일상 기능에서 조금 나았다. 만성 허리 통증에는 운동이 통증을 100점 중
  15점쯤 줄였다.
- 익숙한 허리 통증이고, 무릎 아래로 뻗치는 증상이나 위험 신호가 없으면 계속 운동한다. 대신 가장
  무거운 데드리프트·스쿼트부터 바꾼다. 먼저 무게와 강도를 낮추고, 그래도 아프면 범위나 동작
  (블록 풀, 트랩바, 루마니안 데드리프트, 박스·프론트 스쿼트)을 바꾸고, 그다음 허리에 덜 실리는
  동작(힙 쓰러스트, 백 익스텐션, 스플릿 스쿼트, 머신)으로 바꾼다. 남은 힌지·스쿼트는 주 안에 나눈다.
- 통증 기준은 힘줄 규칙(055)을 빌려 쓴다. 운동 중·후 10점 중 5점까지, 다음 날 아침엔 평소대로,
  주마다 늘지 않을 것. 다만 허리에서 직접 시험된 기준은 아니다.
- 데드리프트는 금지 동작이 아니라 치료로도 쓰인다. 허리가 반복해서 아픈 사람에게 감독하에 데드리프트를
  시킨 연구에서 통증·근력·지구력이 좋아졌고, 2년 뒤까지 저부하 조절 운동과 차이가 없었다. 통증이
  낮고 허리 버티는 힘이 좋은 사람이 더 잘 맞았다. 통증이 크면 가볍게 시작해서 올린다.
- 들 때 허리가 조금 굽는 것이 허리 통증의 원인이라는 근거는 없다(질 낮은 근거). 자세 교정은
  수행·부하 조절용 큐로 쓰고, "허리를 굽히면 다친다"고 말하지 않는다.
- 갑자기 날카롭게 아파서 빈 봉도 못 들 정도면 무거운 힌지와 스쿼트는 잠시 빼고, 걷기와 상체 운동
  같은 다른 움직임은 이어간다. 침대에 눕는 게 아니다. 무릎 아래로 저리거나 뻗치면 먼저 확인한다.
- 위험 신호: 사타구니·엉덩이 감각 이상, 소변·대변 조절 이상, 다리 힘 빠짐이나 양쪽 저림이
  심해짐(이 셋은 당일 진료), 넘어지거나 부딪힌 뒤 통증, 골다공증·장기 스테로이드·고령, 암 병력,
  이유 없는 체중 감소, 쉬어도 안 가라앉는 밤 통증, 열·감염. 이런 경우 운동이 아니라 진료로 보낸다.
- 나은 뒤에도 1년 안에 셋 중 둘은 다시 아프다. 운동과 교육을 같이 하면 재발 위험이 절반 가까이
  준다. 그래서 회복 후에도 허리 지구력 운동을 유지하고, 여러 번 반복된 허리는 오래된 이력으로
  내리지 않는다.
- 단계 배치와 바꾸는 순서는 실무 판단이다. 역도·파워리프팅 선수를 대상으로 순서를 비교한 연구는 없다.
