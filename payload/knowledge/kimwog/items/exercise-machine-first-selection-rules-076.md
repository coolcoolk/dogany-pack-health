---
# Equipment sprint 2026-10-07 (dispatch task kw-ex-machine-vs-free). The
# engine-readable SELECTION half: when the composer should rank a machine (or
# cable / supported) variant first for a working-set slot, and when a
# free-weight lift must be kept. A routing rule over 075 (evidence), 056
# (caution ladder) and the ED surveillance row cited below; same posture as
# 031, 032 and 056 -- each rule names the graded row it rests on and its own
# basis_grade, and product constants are labelled as constants.
#
# equipment_rules is structured data for the composer
# (payload/service/health/compose_rank_rules.json, which today has only an
# `equipment` availability exclude and an `equipment_variety` repeat penalty;
# prep/cooldown drills are already machine-first by owner rule 2026-10-06).
# Values are PREFERENCES and KEEP-constraints, not scores; no number here is
# a load or a risk figure.
id: exercise/machine-first-selection-rules-076
domain: exercise
grade: D (selection rule over 075, 056 and injury surveillance; the hypertrophy swap is C-backed, the strength-keep is B-backed, the caution / fatigue / cut preferences are product judgement)
lane: "@gym-craft"
locale: universal
as_of: 2010-2025
contested: no
sources:
  - "exercise/machine-free-weight-equivalence-075"  # growth: no modality difference found (C); strength test-specific (B); squat > leg press for jump (C)
  - "exercise/caution-severity-ladder-056"  # which rungs spread load and drop high-load variants at a caution site
  - "exercise/tendon-fascia-load-management-055"  # pain ceiling and step-back options at a loaded tendon / fascia
  - "exercise/knee-pain-symptom-guided-loading-057"  # the knee pain ceiling (2/10) that replaces the 055 ceiling at a knee site (v37; linked at the v38 merge)
  - "exercise/knee-friendly-squat-depth-variants-058"  # at a knee site the lever is range and hip-vs-knee bias, not the equipment class; the machine stop is how range gets limited (v37; linked at the v38 merge)
  - "exercise/shoulder-pressing-selection-cuff-work-064"  # at a shoulder site its selection_rules pick the variant; machine-substitution-costs-little is the same Haugen 2023 finding as 075 (v37; linked at the v38 merge)
  - "exercise/shoulder-prep-specific-vs-general-065"  # machine-first PREP policy (ramp sets on the first machine); this row is machine-first SELECTION (v37; linked at the v38 merge)
  - "exercise/deficit-volume-guidance-016"  # deficit volume guidance is theory-only and contested -- the cut rule inherits that floor
  - "exercise/load-increment-size-evidence-gap-027"  # fixed-stack machine increments have no research literature
  - "exercise/female-training-considerations-020"  # machine-fit mismatch claim (practitioner, contested) -- the fit rule
  - "exercise/harm-route-boundary-031"  # pain that triage owns is not solved by a machine swap
  - "https://pubmed.ncbi.nlm.nih.gov/20139328/"  # Kerr ZY, Collins CL, Comstock RD 2010, Am J Sports Med 38(4):765-771 -- NEISS, US emergency departments 1990-2007, 25,335 cases (~970,801 national estimate): 90.4% involved free weights; weights dropping on the person was the commonest mechanism (65.5%); free-weight injuries had a larger share of fractures/dislocations (23.6% vs 9.7%, IPR 2.44); people 55+ had a larger share of machine injuries (18.2% vs 9.3%). Descriptive, NO exposure denominator -- shows how free-weight injuries happen, not that machines have a lower injury rate per hour. Abstract read from the article PDF 2026-10-07
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10426227/"  # Haugen ME et al. 2023, BMC Sports Sci Med Rehabil 15:103 -- discussion speculates machines may suit beginners (fewer degrees of freedom, possible lower injury risk at free weights) and that combining modalities may give more complete hypertrophy; both labelled speculation by the authors. Full text read 2026-10-07
  - "owner rule 2026-10-06 16:11/16:21 (compose_rank_rules.json drill_equipment_doc): prep and cooldown drills are machine-first; this row extends the reasoning to working sets with graded limits"
  - "framework:GRADE -- the swap is licensed by a C-level hypertrophy null and limited by a B-level strength-specificity finding (075). No trial tests machine-first selection for injured sites, under fatigue, in a caloric deficit, or for training without a spotter; those rules rest on mechanism (dropped-load injuries, fixed path, pin stop) and practitioner judgement and are held at D."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
equipment_rules:
  - id: hypertrophy-swap-free
    when: primary_goal is muscle size or general fitness
    prefer: none -- machine and free-weight variants rank equal for the muscle; pick by availability, fit, and weekly variety
    keep: []
    scope: working sets
    basis: exercise/machine-free-weight-equivalence-075
    basis_grade: C
  - id: strength-keep-named-lift
    when: primary_goal names a barbell or free-weight lift (powerlifting total, squat / bench / deadlift target, a test)
    prefer: the named lift stays as the primary slot; machines fill accessory slots
    keep: [named-lift]
    scope: primary slot of the session that trains that pattern
    basis: exercise/machine-free-weight-equivalence-075
    basis_grade: B
  - id: performance-keep-free-standing
    when: primary_goal is jumping, sprinting or a field / court sport
    prefer: at least one free-standing lower-body lift per week (squat, lunge or hinge class); leg press may add volume, not replace it
    keep: [free-standing-lower]
    scope: weekly
    basis: exercise/machine-free-weight-equivalence-075
    basis_grade: C
  - id: caution-site-machine-first
    when: the slot loads a site at 056 rung history-recent, history-unknown or current-load-pain
    prefer: machine, cable or supported variant first for that site's slot (fixed path, pin or stack stop, no load to drop), unless keep from a goal rule applies; still obey 056 exclude_grades and the site's pain ceiling (055; 057 at the knee); at a knee site range and hip-vs-knee bias are the lever (058 variant_swaps) and the machine is picked for its stop and fixed path, not as the knee fix; at a shoulder site 064 selection_rules pick the variant
    keep: []
    scope: the caution site's slots only
    basis: exercise/caution-severity-ladder-056
    basis_grade: D
  - id: caution-triage-no-swap
    when: the site is at 056 rung current-other or red-flag
    prefer: no swap -- a machine does not reopen a site that is closed pending triage
    keep: []
    scope: the caution site
    basis: exercise/harm-route-boundary-031
    basis_grade: D
  - id: near-failure-unspotted
    when: a set is planned to or near failure and no spotter or safety rack is known
    prefer: machine or cable variant for that set, or keep the free-weight set at a few reps in reserve
    keep: []
    scope: per set
    basis: Kerr 2010 (dropped weights were 65.5% of ED weight-training injuries)
    basis_grade: D
  - id: fatigue-or-cut-accessories
    when: primary_goal is fat loss / cut, or the user reports high fatigue or poor sleep
    prefer: machine-first for accessory slots; keep the primary free-weight lift if a keep rule applies
    keep: []
    scope: accessory slots
    basis: exercise/deficit-volume-guidance-016
    basis_grade: D
  - id: fit-mismatch-swap
    when: the user says a machine does not fit (seat, pivot, handle width, pain only on that machine)
    prefer: dumbbell or cable variant of the same pattern; never insist on the machine
    keep: []
    scope: that machine
    basis: exercise/female-training-considerations-020
    basis_grade: D
  - id: older-adult-not-risk-free
    when: age_years 55 or older
    prefer: machine-first stays allowed, but machine setup and path cues are still given; machines are not injury-free
    keep: []
    scope: all slots
    basis: Kerr 2010 (55+ had a larger share of machine injuries, 18.2% vs 9.3%)
    basis_grade: D
refraction_notes:
  - note: >
      THE SWAP IS FREE FOR MUSCLE, NOT FOR A NAMED LIFT. Because no growth
      difference was found between modalities (075), a machine can replace a
      free-weight lift for hypertrophy without a stated penalty. Because
      strength is test-specific, it cannot replace a lift the user wants to
      get stronger at; that lift stays.
    grade: C
  - note: >
      MACHINE-FIRST AT A CAUTION SITE IS A JUDGEMENT, NOT A FINDING. The
      reasoning is mechanism: a fixed path, a stack that stops, and no bar to
      drop or bail from, while most emergency-department weight-room injuries
      involve free weights and dropped loads (Kerr 2010). That survey has no
      exposure denominator, so it does NOT show machines have a lower injury
      rate. No trial tests machine-first loading after injury. Speak it as the
      plan's rule.
    grade: D
  - note: >
      A MACHINE DOES NOT CLEAR A SITE. For pain that the 056 ladder routes to
      triage (joint, ligament, muscle, unknown tissue, red flags), swapping to
      a machine is not a way around the triage step.
    grade: D
  - note: >
      FATIGUE AND CUT: LEAST EVIDENCE. Moving accessories to machines during a
      cut or a high-fatigue week is coaching practice built on lower setup and
      stabilising demand. No trial measures fatigue, recovery or lean-mass
      retention by modality in a deficit, and the deficit-volume guidance it
      sits beside is itself theory-only (016).
    grade: D
  - note: >
      MACHINES HAVE THEIR OWN LIMITS. Fixed stacks can make progression jumps
      large (no research on stack increments, 027); a machine that does not
      fit the body should be swapped, not forced (020); and older adults are
      injured on machines too (Kerr 2010).
    grade: D
claim: >
  The composer may rank a machine, cable or supported variant first for a
  working-set slot in four cases: the goal is muscle size (no growth
  difference between modalities, so the swap costs nothing measurable); the
  slot loads a caution site at the recent / undated history or loaded-tendon
  rung of the 056 ladder; a set is planned near failure without a known
  spotter or safety stop; or the user is in a cut or a high-fatigue week
  (accessory slots only). It must keep a free-weight lift when the user's
  goal names that lift (strength is test-specific) and keep one free-standing
  lower-body lift weekly when the goal is jumping, sprinting or a field
  sport. A machine never reopens a site closed for triage, a machine that
  does not fit is swapped for a dumbbell or cable variant, and machines are
  not presented as injury-free. Only the hypertrophy swap and the strength
  keep rest on trial evidence; the caution, unspotted-failure and cut
  preferences are product judgement on mechanism.
reasoning: >
  075 supplies the two evidence-backed edges: the hypertrophy null that
  licenses the swap and the strength specificity that limits it, plus the
  squat-vs-leg-press jump result behind the performance keep. The caution
  rule plugs into 056's rungs rather than inventing new ones: the rungs that
  already spread load and drop high-load variants are the ones where a
  fixed-path variant is preferred, while the rungs that go to triage keep 031's
  behaviour. Kerr 2010 gives the mechanism picture (free weights, dropped
  loads, more fractures) and also its limit (no exposure denominator, and a
  larger share of machine injuries in people 55 and over), so it backs a
  preference, not a safety claim. The fatigue / cut rule inherits 016's
  theory-only floor. The injury_history axis is hard with block_specifics as
  in 056: without the user's words on the site's rung, the caution rule is
  not applied to a specific site.
---

# exercise/machine-first-selection-rules-076 -- 언제 머신을 먼저 고르나

**한 줄 그림:** 근육이 목표면 머신으로 바꿔도 손해가 확인되지 않았다. 다만 키우고 싶은 바벨
종목은 남기고, 주의 부위·보조자 없는 실패 세트·감량기에는 머신을 먼저 고른다(이건 제품 판단).

## The rules (engine-readable: `equipment_rules`)

| Rule | When | Prefer / keep | Basis |
|---|---|---|---|
| hypertrophy-swap-free | goal = muscle size | machine = free weight; pick by availability, fit, variety | 075 |
| strength-keep-named-lift | goal names a barbell lift | keep that lift as the primary slot | 075 |
| performance-keep-free-standing | goal = jump / sprint / sport | keep one free-standing lower lift weekly | 075 |
| caution-site-machine-first | site at history-recent / unknown / current-load-pain | machine or supported variant first at that site | 056 + mechanism |
| caution-triage-no-swap | site at current-other / red-flag | no swap; triage first | 031 |
| near-failure-unspotted | near-failure set, no spotter or safety stop | machine, or leave reps in reserve | Kerr 2010 mechanism |
| fatigue-or-cut-accessories | cut or high fatigue | machine-first for accessories | 016, practice |
| fit-mismatch-swap | machine does not fit | dumbbell / cable instead | 020 |
| older-adult-not-risk-free | 55+ | machines allowed, cues still given | Kerr 2010 |

## 한국어 요약 (답변용)

- 근육을 키우는 게 목표면 머신과 프리웨이트를 같은 선택지로 본다. 근육 성장 차이가 발견되지 않았으니,
  있는 장비·몸에 맞는지·주간 장비 반복 여부로 고른다.
- 스쿼트·벤치·데드리프트처럼 사용자가 목표로 이름 붙인 종목이 있으면 그 종목은 주 운동으로 남긴다.
  근력은 연습한 도구에서 더 오르기 때문이다. 머신은 보조 운동 자리를 채운다.
- 점프·달리기·구기 종목이 목표면 서서 하는 하체 프리웨이트(스쿼트·런지·힙힌지)를 주에 하나는 남긴다.
  레그프레스는 양을 더할 뿐 대신하지 않는다.
- 최근 다쳤거나 언제 다쳤는지 모르는 부위, 또는 익숙한 힘줄·족저근막 통증이 있는 부위는 머신·케이블·
  지지되는 동작을 먼저 고른다. 궤도가 정해져 있고, 떨어뜨릴 바가 없어서다. 다만 머신이 부상을
  줄인다는 연구는 없다. 응급실 통계에서 웨이트 부상 대부분이 프리웨이트와 떨어진 무게였지만,
  사용 시간을 감안한 비교가 아니다. "계획의 규칙"으로 말한다.
- 관절·인대·근육 통증, 어디가 아픈지 모르는 통증, 위험 신호가 있는 부위는 머신으로 바꿔도 다시
  열지 않는다. 통증 확인이 먼저다.
- 보조자나 안전바 없이 실패 직전까지 하는 세트는 머신으로 하거나, 프리웨이트면 몇 회 남기고 멈춘다.
- 감량기나 피로가 큰 주에는 보조 운동을 머신 위주로 한다. 근거가 가장 약한 규칙이다.
- 머신이 몸에 안 맞는다고 하면(좌석, 회전축, 손잡이 폭, 그 기계에서만 아픔) 덤벨·케이블로 바꾼다.
  55세 이상도 머신을 먼저 써도 되지만, 응급실에 온 이 나이대 부상 중 머신 비중이 더 컸던 만큼
  자세·세팅 안내는 빼지 않는다.
