---
# Equipment sprint 2026-10-07 (dispatch task kw-ex-machine-vs-free). The
# EVIDENCE half: does the tool (machine vs free weight) change muscle growth
# or strength? The selection rules that act on this row live in
# exercise/machine-first-selection-rules-076. Product code already ranks drills
# machine-first for prep/cooldown (compose_rank_rules.json drill_equipment_doc,
# owner 2026-10-06); this row says how far that preference is backed for
# working sets.
id: exercise/machine-free-weight-equivalence-075
domain: exercise
grade: B (strength gains are test-specific; no modality difference in strength measured on neutral tests); C (no hypertrophy difference -- few trials, crude measures); C (free-weight squat transfers better to jumping than leg press)
lane: "@performance-lit"
locale: universal
as_of: 2010-2025
contested: no
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10426227/"  # Haugen ME, Vårvik FT, Larsen S, Haugen AS, van den Tillaar R, Bjørnsen T 2023, BMC Sports Sci Med Rehabil 15:103 -- systematic review + meta-analysis, 13 studies, n=1016 (789 men), 6-12 weeks, 6 trained / 7 untrained samples. Free-weight tests favour free-weight training (SMD -0.21, 95% CI -0.39 to -0.03); machine tests lean to machine training (SMD 0.29, -0.02 to 0.60, p=0.064); direct comparison dynamic strength SMD 0.08 (-0.11 to 0.27), isometric -0.08 (-0.43 to 0.27), CMJ -0.21 (-0.60 to 0.18), hypertrophy -0.06 (-0.40 to 0.29). Hypertrophy rows: 6 studies, measured by ultrasound (2), circumference, skinfold (2), Bod Pod -- authors flag measures 'not always gold standard'. Full text read 2026-10-07
  - "https://pubmed.ncbi.nlm.nih.gov/32358310/"  # Schwanbeck SR, Cornish SM, Barss T, Chilibeck PD 2020, J Strength Cond Res 34(7):1851-1859 -- RCT n=46 (26 women), 8 weeks: biceps and quadriceps muscle thickness (ultrasound) rose similarly; machine bench press rose more with machines (+13.9% vs +8.6%, p=0.05); free-weight and Smith squat rose 11-19% in both groups, no difference. Abstract read estate-scrub:allow(cited author surname)
  - "https://pubmed.ncbi.nlm.nih.gov/41316621/"  # Amanuma MT, ... de Salles Painelli V 2025, J Bodyw Mov Ther -- within-subject RCT, n=8 untrained women, 9 weeks, one leg lunge vs other leg incline leg press: rectus femoris and vastus lateralis thickness up ~9-28% in both, no between-condition difference at proximal or distal sites. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/26439782/"  # Wirth K, Hartmann H, Sander A, Mickel C, Szilvas E, Keiner M 2016, J Strength Cond Res 30(5):1205-1212 -- RCT n=78, 8 weeks back squat vs 45-degree leg press: squat jump +12.4% and CMJ +12.0% with squat, +3.5% and +0.5% with leg press. Abstract read
  - "https://bretcontreras.com/wp-content/uploads/Strength-body-composition-and-functional-outcomes-in-the-squat-versus-leg-press-exercises.pdf"  # Rossi FE, Schoenfeld BJ, Ocetnik S et al. 2018, J Sports Med Phys Fitness 58(3):263-270 -- 10 weeks, squat-only vs leg-press-only vs both, 8-12RM: squat strength rose more with squats; CMJ effect sizes favoured squat groups, balance effect sizes favoured leg-press groups, no statistically significant between-group differences. Abstract read (repository record)
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: EMG comparisons of Smith vs free squat (and similar) cannot decide hypertrophy estate-scrub:allow(Smith machine, gym equipment)
  - "exercise/progression-modality-load-vs-reps-028"  # within-warehouse: Smith-vs-free test mismatch as a known confound -- the same specificity this row reports estate-scrub:allow(Smith machine, gym equipment)
  - "exercise/machine-first-selection-rules-076"  # within-warehouse: the selection rules that act on this row
  - "framework:GRADE -- strength specificity and null direct comparisons come from one 2023 meta-analysis of 13 short RCTs (fair-to-good TESTEX, low heterogeneity except direct strength I2=60%), so B. The hypertrophy null rests on 6 small trials, most with skinfold / circumference / whole-body measures, so it is an absence of a detected difference, held at C. Jump transfer rests on two squat-vs-leg-press trials in untrained students, C. No trial runs longer than 12 weeks and none uses advanced lifters."
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      FOR MUSCLE GROWTH THE TOOL IS NOT THE LEVER. No trial or pooled
      analysis found more growth with free weights than with machines (or
      the reverse) over 6-12 weeks when sets, rep range and effort were
      similar. A machine set taken close to failure counts like a free-weight
      set for the muscle it trains. The evidence is thin (six small trials,
      mostly crude body-composition measures), so say "no difference was
      found", not "proven identical".
    grade: C
  - note: >
      STRENGTH IS SPECIFIC TO THE TEST. People get stronger mostly at the
      thing they practise: free-weight training raised free-weight 1RM more,
      machine training leaned toward raising machine 1RM more, and on neutral
      tests (isometric, cross-modality) the groups did not differ. So a
      machine-built strength number is real but transfers only partly to the
      barbell, and vice versa. If the user's goal names a barbell lift (a
      powerlifting total, a squat target, a test), that lift must stay in the
      plan.
    grade: B
  - note: >
      JUMP AND SPORT TRANSFER FAVOUR THE FREE-STANDING PATTERN. Back squat
      training raised jump height about 12% in eight weeks; leg press barely
      moved it, although both raised maximal strength. For a user whose goal
      is jumping, sprinting or a field sport, keep at least one free-standing
      lower-body lift. Two trials, untrained students.
    grade: C
  - note: >
      HORMONE RESPONSES ARE NOT A REASON TO PICK. Schwanbeck 2020 saw a
      larger acute free-testosterone rise after free-weight sessions in men,
      with no difference in muscle or strength gained. Acute hormone spikes
      do not decide hypertrophy; do not speak this as a free-weight advantage.
    grade: C
  - note: >
      EMG AND "STABILISER" ARGUMENTS DO NOT SETTLE IT. Higher stabiliser EMG
      during free-weight lifts is often cited as proof they build more; 013
      bars EMG as a hypertrophy proxy, and the longitudinal trials above did
      not show the predicted difference.
    grade: B
claim: >
  Over 6-12 weeks, training with machines and training with free weights
  produce similar muscle growth and similar strength when strength is
  measured on a neutral test; each modality improves its own test more
  (free-weight training raises free-weight 1RM more, machine training
  tends to raise machine 1RM more). The hypertrophy equivalence rests on few,
  small trials with mostly indirect measures, so it is "no difference found"
  rather than proven identity. Free-standing lower-body lifts (back squat)
  transfer better to jump performance than leg press in untrained people.
  Acute hormone or EMG differences do not translate into different growth.
  No trial covers advanced lifters or runs past 12 weeks.
reasoning: >
  Haugen 2023 is the only meta-analysis that pools direct free-weight vs
  machine comparisons (13 studies, n=1016). Its direction is clean: specific
  tests favour the trained modality, direct comparisons are null for dynamic
  strength, isometric strength, CMJ and hypertrophy, with no publication bias
  signal. The strength specificity is the firmest part (consistent with the
  general specificity principle and with Schwanbeck's machine-bench result),
  so it carries B. The hypertrophy null is supported by Schwanbeck's
  ultrasound result and by Amanuma 2025's within-subject ultrasound trial, but
  both are small and short, and half the pooled hypertrophy studies used
  skinfold or circumference -- a null from coarse instruments, held at C. Wirth
  2016 and Rossi 2018 show that the leg press builds leg strength but transfers
  less to jumping than the squat; that is the case where the tool matters,
  and it matters for performance goals, not for muscle size. The row is the
  evidence base for 076's machine-first rules: equivalence for hypertrophy is
  what licenses a machine swap without a growth penalty, and specificity is
  what limits it.
---

# exercise/machine-free-weight-equivalence-075 -- 머신 vs 프리웨이트, 근육과 근력에 차이가 있나

**한 줄 그림:** 근육 크기에는 머신이냐 프리웨이트냐가 차이를 만들지 않았다. 근력은 연습한 도구로
잴 때 더 오른다. 점프 같은 운동 능력은 서서 하는 프리웨이트 하체 운동이 더 잘 옮겨 간다.

## What the trials show

| Outcome | Result | How firm |
|---|---|---|
| Strength on a free-weight test | free-weight training better (SMD -0.21) | meta-analysis, 13 trials |
| Strength on a machine test | machine training tends better (SMD 0.29, p=0.06) | meta-analysis |
| Strength on a neutral / isometric test | no difference | meta-analysis |
| Muscle growth | no difference (SMD -0.06) | 6 small trials, mostly crude measures |
| Jump height | squat +12%, leg press ~0-4% (Wirth 2016) | 2 trials, untrained |
| Acute testosterone | larger after free weights in men, no effect on gains | 1 trial |

No trial is longer than 12 weeks; none uses advanced lifters.

## 한국어 요약 (답변용)

- 근육을 키우는 데는 머신과 프리웨이트 사이에 차이가 발견되지 않았다. 세트 수, 반복 범위, 실패에
  가까운 정도가 비슷하면 머신 한 세트도 프리웨이트 한 세트와 똑같이 센다. 다만 연구가 적고
  측정이 거친 편이라 "똑같다고 증명됐다"가 아니라 "차이를 찾지 못했다"고 말한다.
- 근력은 연습한 도구에서 더 오른다. 프리웨이트로 훈련하면 바벨 1RM이, 머신으로 훈련하면 머신
  1RM이 더 오르는 경향이 있고, 중립적인 테스트에서는 차이가 없었다. 목표가 바벨 기록(파워리프팅,
  스쿼트 목표치)이면 그 종목은 계획에 남겨야 한다.
- 점프·달리기·구기 같은 운동 능력이 목표면 서서 하는 하체 프리웨이트를 하나는 둔다. 8주 스쿼트는
  점프를 약 12% 올렸지만 레그프레스는 거의 올리지 못했다(두 연구, 초보자).
- 프리웨이트 뒤에 테스토스테론이 더 오른다거나 안정근 근전도가 더 높다는 건 근육 성장 차이로
  이어지지 않았다. 고르는 이유로 쓰지 않는다.
