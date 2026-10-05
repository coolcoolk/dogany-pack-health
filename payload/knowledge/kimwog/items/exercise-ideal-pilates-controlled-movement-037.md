---
# Body-ideal archetype sprint 2026-09-30. The owner's third named ideal
# ("필라테스의 연결"). The agent treated Pilates as isometric holds; the owner
# corrected it: Pilates is slow, controlled, full-range movement with precise
# alignment and breath. The pack's current measure for this side
# (zero_load_control_share_sets, classified by rx-calc._is_isometric_hold)
# counts HOLDS, which is the same error in code -- recorded in the sprint
# report and in exercise/body-ideal-archetype-map-032.
id: exercise/ideal-pilates-controlled-movement-037
domain: exercise
grade: B (definition -- systematic review + clinician Delphi); B (low back pain effect, low-certainty evidence); B (no body-composition or strength advantage)
lane: "@performance-lit"
locale: universal
as_of: 2012-2026
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/22579438/"  # Wells C, Kolt GS, Bialocerkowski A. Complement Ther Med 2012;20:253-62 -- 119 papers: Pilates is a mind-body exercise focusing on strength, core stability, flexibility, muscle control, posture and breathing; mat or apparatus; traditional principles centering, concentration, control, precision, flow, breathing
  - "https://pubmed.ncbi.nlm.nih.gov/24179139/"  # Wells C et al. Phys Ther 2014 -- Delphi of 30 physiotherapists: Pilates requires body awareness, breathing, movement control, posture, education; 30-60 min, 2x/week, 3-6 months
  - "https://thecore.pilates.com/flow-where-the-magic-happens/"  # Balanced Body (Pilates education body) on the flow principle: continuity and fluidity of movement, control and precision over speed or force
  - "https://pubmed.ncbi.nlm.nih.gov/34538747/"  # Hayden JA et al. J Physiother 2021 -- 217 RCTs, chronic LBP network meta-analysis: Pilates, McKenzie, functional restoration most effective for pain/function
  - "https://pubmed.ncbi.nlm.nih.gov/31666220/"  # Owen PJ et al. Br J Sports Med 2020 -- LBP NMA, Pilates ranked best for pain; low GRADE certainty; an expression of concern is attached to this paper
  - "https://pubmed.ncbi.nlm.nih.gov/32396869/"  # Cavina APS et al. J Phys Act Health 2020 -- mat Pilates not more effective than other exercise or control for BMI, lean mass, body fat %, abdominal circumference
  - "https://pubmed.ncbi.nlm.nih.gov/42784403/"  # Bajcetic C et al. Sports 2026 -- adult women, 12 studies: significant BMI, body weight, sit-and-reach gains; no pooled effect on body fat %, waist, lean mass, handgrip, vertical jump
  - "https://pubmed.ncbi.nlm.nih.gov/38876695/"  # Oliveira LS et al. J Bodyw Mov Ther 2024 -- older adults, 24 RCTs: no strength advantage vs other exercise (SMD 0.01)
  - "https://pubmed.ncbi.nlm.nih.gov/25601394/"  # Schoenfeld BJ et al. Sports Med 2015 -- repetition durations 0.5-8 s give similar hypertrophy; >10 s per rep likely inferior
  - "https://pubmed.ncbi.nlm.nih.gov/36622555/"  # Alizadeh S et al. Sports Med 2023 -- full-range resistance training improves ROM as much as stretching
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      PILATES IS MOVEMENT, NOT A HOLD. Its principles are control, precision,
      flow, breathing, centering and concentration: slow, continuous,
      full-range movement with exact alignment, the breath paired to the phase
      of the movement, the trunk organised first. A plank or hollow HOLD is at
      most an element; a measure that counts only timed holds (the pack's
      zero_load_control_share_sets via _is_isometric_hold) does not see Pilates
      at all. The right marker is a controlled-tempo, full-range set (for
      example a roll-down, roll-up, bridge articulation, leg circles, or a
      loaded lift done at a slow stated tempo), not seconds held.
    grade: B
  - note: >
      DO NOT MEASURE PILATES WITH INBODY. Pooled trials find no advantage over
      other exercise or control for body fat, lean mass or waist; strength gains
      in older adults do not exceed other exercise. A Pilates strand linked to
      body_fat_pct or skeletal_muscle_kg will read "no progress" while the thing
      the user wanted (control, range, a pain-free back) improves.
    grade: B
  - note: >
      THE LOW-BACK-PAIN RESULT IS REAL BUT SOFT. Two network meta-analyses rank
      Pilates among the most effective exercise types for chronic low back
      pain, but certainty is low and one of them carries a journal expression
      of concern. Speak it as "one of the better-supported options", never as
      a cure, and never as a substitute for pain triage.
    grade: B
  - note: >
      SLOW IS NOT A HYPERTROPHY DISCOUNT until it is very slow. Repetition
      durations of 0.5 to 8 seconds produce similar growth; above about 10
      seconds per rep, growth appears worse. So controlled Pilates-style tempo
      on ordinary lifts does not cost the physique strands, while super-slow
      work might.
    grade: B
claim: >
  Pilates (mat or apparatus such as the reformer) is a mind-body exercise
  method whose defining features are movement control, precision of alignment,
  breathing coordinated with movement, trunk centering and flowing continuity:
  slow, controlled, full-range movements, typically articulating the spine
  segment by segment and moving the limbs around a stable, organised trunk.
  "Connection" in the owner's sense is this: the breath, the trunk and the
  limbs moving as one controlled sequence. It is not a program of isometric
  holds. Its best evidence is for chronic low back pain (low certainty); pooled
  trials show no body-composition or strength advantage over other exercise,
  with modest flexibility gains, so its progress is not visible on InBody.
reasoning: >
  Wells 2012's systematic review of 119 papers is the standard definition and
  names the six traditional principles; the 2014 Delphi of Pilates-trained
  physiotherapists adds movement control, body awareness and breathing as
  consensus requirements. Balanced Body's educational text supplies the
  practitioner meaning of flow (continuity, control over speed or force). The
  effect evidence is mixed in a specific way: favourable and repeated for low
  back pain (Hayden 2021, 217 RCTs; Owen 2020, low certainty and an expression
  of concern), null for body composition (Cavina 2020; Bajcetic 2026 except
  BMI/weight in women) and for strength relative to other exercise (Oliveira
  2024). The item is marked contested because the LBP ranking is disputed in
  certainty, not because the definition is.
---

# exercise/ideal-pilates-controlled-movement-037 -- 필라테스 (연결 / 통제된 움직임)

**한 줄 그림:** 호흡에 맞춰 척추를 한 마디씩 굴리고 팔다리를 몸통 중심에서 정확하게 움직이는,
느리고 끊김 없는 전 가동범위 움직임 -- 숨·몸통·팔다리가 한 동작으로 이어지는 몸. 버티기(홀드)가 아니다.

## Distinguishing features

- Six principles: centering, concentration, control, precision, flow, breathing.
- Slow, continuous, full-range, precisely aligned movement; spinal articulation
  (roll-down / roll-up, bridge peel), limb movement around an organised trunk,
  breath timed to the movement.
- Load is usually light or spring-assisted/resisted (reformer); the difficulty
  is control, not load.
- Neighbours: yoga/mobility = range and positions held/flowed, less emphasis on
  precise trunk-limb control; calisthenics = bodyweight strength and skill,
  output-driven; "core training" = often isometric holds -- the thing Pilates is
  NOT reducible to.

## Measurable here

- Controlled-tempo share: sets logged with a slow stated tempo or as a
  Pilates-type controlled movement. The pack has `tempo` in the exercise
  record but NO strand token for it (proposed `controlled_tempo_share_sets`).
- `zero_load_control_share_sets` exists but counts timed holds only -- wrong
  proxy for Pilates (see note 1).
- `unilateral_share_sets` -- partial (single-leg circles, side-lying series are
  unilateral), not the definition.
- `weekly_sessions` (a Pilates class logged as a workout), workouts `minutes`.

## Not measurable here

Movement quality, alignment, breath coordination, segmental spinal control,
range of motion (no ROM test token), low-back pain trajectory beyond the
pain-event log. InBody numbers will not show Pilates progress (note 2).

## Training emphasis and practice

A controlled-movement slot each session (roll-down, bridge articulation, leg
circles, a dead-bug with slow breath-paced reps), a mobility flow, and slow
tempo on ordinary lifts. Program-engine fit: the kit's connection set
(`breath_trunk`, `mobility_flow`, `whole_body`); within `breath_trunk` the
roll-down is the Pilates-faithful pick, the hollow HOLD is not.

## Failure modes

- Reducing it to holds (the error this row exists to fix).
- Chasing difficult flexion-heavy mat moves with an irritable back -- route to
  pain triage first.
- Expecting it to change body composition or build size.

## Combines / conflicts

- With classic physique: complementary; it does not compete for growth volume,
  and controlled tempo within 0.5-8 s per rep does not reduce hypertrophy.
- With CrossFit-type work: complementary -- it rebuilds control and range that
  fatigued high-intensity work erodes.
- All three together (the owner's picture): hypertrophy volume for the X,
  a conditioning/power dose for work capacity, and controlled full-range
  movement for connection -- three different measures, never one number.
