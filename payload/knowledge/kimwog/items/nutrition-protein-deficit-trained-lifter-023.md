---
# Authored 2026-10-07 (dispatch kw-nu-cut-protein-lifter). Protein for a
# trained lifter in a calorie deficit -- the case the diet card meets on every
# cut day. Owned elsewhere and NOT restated here: the general daily range
# (002), the per-meal ceiling dispute (008), the distribution question (009),
# the rate of loss (012), Korean exchange arithmetic (021), the training-timing
# window (exercise/protein-anabolic-window-002). This item owns only what
# changes when the lifter is in a deficit, and the reading of the two numbers
# the diet engine already uses (Morton 2018's 2.2 and Schoenfeld & Aragon
# 2018's 0.4 / 0.55), each re-read at the primary on 2026-10-07.
#
# protein_rules is structured data for diet-status (protein.py day target and
# nudge caps). Values are per kg of BODY WEIGHT unless the unit field says
# otherwise. No program code was changed by this item.
# Renumbered at the v37 merge (provisional 070 -> 023). Written in parallel
# with nutrition/protein-deficit-lean-mass-target-062, which OWNS the deficit
# target band (same 1.6-2.4 g/kg, same core trials); this row carries the
# trained-lifter reading of the engine's numbers and the protein_rules the
# diet-status code reads (pack 0.33.0 applies them).
id: nutrition/protein-deficit-trained-lifter-023
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2010-2022
contested: yes
sources:
  - "https://doi.org/10.1136/bjsports-2017-097608"  # Morton RW, Murphy KT, McKellar SR, Schoenfeld BJ, Henselmans M, Helms E, Aragon AA, Devries MC, Banfield L, Krieger JW, Phillips SM. Br J Sports Med 2018;52(6):376-384. PMID 28698222, PMC5867436 -- 49 RCTs, 1863 participants; break point 1.62 g/kg/day, 95% CI 1.03-2.20, p=0.079 (not significant), 42 arms, intakes 0.9-2.4 g/kg/day; full text read
  - "https://doi.org/10.1186/s12970-018-0215-1"  # Schoenfeld BJ, Aragon AA. J Int Soc Sports Nutr 2018;15:10. PMID 29497353, PMC5828430 -- 0.4 g/kg/meal is a TARGET across at least four meals to reach a minimum of 1.6 g/kg/day; 0.55 g/kg/meal is 2.2 g/kg/day spread over the same four meals
  - "https://doi.org/10.1123/ijsnem.2013-0054"  # Helms ER, Zinn C, Rowlands DS, Brown SR. Int J Sport Nutr Exerc Metab 2014;24(2):127-138. PMID 24092765 -- systematic review, 6 studies, energy-restricted resistance-trained lean athletes; 2.3-3.1 g/kg of FAT-FREE MASS, scaled up with deficit severity and leanness
  - "https://doi.org/10.1249/mss.0b013e3181b2ef8e"  # Mettler S, Mitchell N, Tipton KD. Med Sci Sports Exerc 2010;42(2):326-337. PMID 19927027 -- n=20 resistance-trained athletes, 2 weeks at 60% energy; ~2.3 vs ~1.0 g/kg: lean mass -0.3 vs -1.6 kg
  - "https://doi.org/10.3945/ajcn.115.119339"  # Longland TM, Oikawa SY, Mitchell CJ, Devries MC, Phillips SM. Am J Clin Nutr 2016;103(3):738-746. PMID 26817506, NCT01776359 -- n=40 young men, 4 weeks at ~40% deficit, RT + HIIT 6 d/wk; 2.4 vs 1.2 g/kg: LBM +1.2 vs +0.1 kg, fat -4.8 vs -3.5 kg; registry does not record resistance-training history
  - "https://doi.org/10.1096/fj.13-230227"  # Pasiakos SM, Cao JJ, Margolis LM, et al. FASEB J 2013;27(9):3837-3847. PMID 23739654 -- n=39 adults, 21 d at 40% deficit; 1.6 and 2.4 g/kg both spared fat-free mass vs 0.8, and were not separated from each other
  - "https://doi.org/10.1123/ijsnem.2017-0273"  # Hector AJ, Phillips SM. Int J Sport Nutr Exerc Metab 2018;28(2):170-177. PMID 29182451 -- review: current recommendation for athletes losing weight 1.6-2.4 g/kg/day, end of range set by deficit severity and training
  - "https://doi.org/10.1002/jcsm.12922"  # Nunes EA, Colenso-Semple L, McKellar SR, et al. J Cachexia Sarcopenia Muscle 2022;13(2):795-810. PMID 35187864, PMC8978023 -- 74 RCTs; in resistance-exercising adults under 65 the lean-mass effect appeared at >=1.6 g/kg/day; small effect (SMD 0.22)
  - "https://doi.org/10.1093/nutrit/nuaa104"  # Tagawa R, Watanabe D, Ito K, et al. Nutr Rev 2020. PMID 33300582, PMC7727026 -- 105 articles, 5402 participants; dose-response flattens above 1.3 g/kg/day but does not reach zero
  - "KDIGO 2024 Clinical Practice Guideline for the Evaluation and Management of Chronic Kidney Disease, Kidney Int 2024;105(4S) -- Rec 3.3.1 0.8 g/kg/day in CKD G3-G5 (2C); Practice Point 3.3.2 avoid >1.3 g/kg/day in adults with CKD at risk of progression (ungraded); read via the NephJC guideline summary https://www.nephjc.com/news/kdigo-ckd-part2"
  - "source:nutrition/protein-deficit-lean-mass-target-062 -- owns the deficit target band; this item does not restate a different one"
  - "source:nutrition/protein-intake-002 -- owns the general 1.4-2.0 g/kg range; its deficit carve-out note quotes the Helms band, which is per kg FAT-FREE MASS (see refraction note 2)"
  - "source:nutrition/protein-per-meal-ceiling-008 -- the per-meal ceiling is contested; this item does not reinstate it"
  - "source:nutrition/protein-distribution-thin-009 -- the even split is not an established lever"
  - "source:nutrition/weight-loss-rate-lean-mass-012 -- deficit size is the other half of lean-mass retention"
  - "source:nutrition/kr-reference-intakes-2025-014 -- the Korean population standard is a different construct"
  - "source:nutrition/kr-protein-exchange-counting-021 -- how the target is counted on a Korean plate"
  - "source:exercise/deficit-volume-guidance-016 -- the training side of a cut"
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: ask
      rescale:
        per_unit_low: 1.6     # g protein per kg body weight per day, cut floor
        per_unit_high: 2.4    # upper end of the deficit band (Hector & Phillips 2018; Longland 2016 arm)
    - key: body_fat_pct
      type: numeric
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: renal_condition    # hedge, not block: unknown speaks the ledger baseline (no known renal impairment); a KNOWN condition outside the gate EXCLUDE_SWAPs the band
      type: categorical
      role: hard
      unknown_policy: hedge
      gate:
        allowed: [none, healthy]
protein_rules:
  - rule: cut-floor
    when: program is cut (deficit_kcal > surplus_kcal)
    value: 1.6
    unit: g per kg body weight per day
    effect: the day target in a cut should not sit below this
    basis: Morton 2018 break point; Nunes 2022 >=1.6 subgroup; Mettler 2010 and Longland 2016 lower arms (~1.0-1.2) lost or failed to gain lean mass
    basis_grade: B
  - rule: cut-band-high
    when: program is cut and the user is lean or the deficit is steep
    value: 2.4
    unit: g per kg body weight per day
    effect: upper end of the band; move toward it as leanness and deficit size rise
    basis: Hector & Phillips 2018 range 1.6-2.4; Longland 2016 2.4 arm; Helms 2014 direction (scaled with leanness and deficit)
    basis_grade: C
  - rule: no-evidence-ceiling-at-2.2
    when: program is cut
    value: 2.2
    unit: g per kg body weight per day
    effect: 2.2 is the upper 95% CI of a non-significant break point from mostly energy-balance trials; it is not a ceiling in a cut and a cut target up to 2.4 is not clamped on evidence grounds
    basis: Morton 2018 full text (break point p=0.079, CI 1.03-2.20, arms 0.9-2.4 g/kg); deficit RCTs used 2.3-2.4
    basis_grade: B
  - rule: ffm-unit-guard
    when: any figure quoted from Helms 2014 (2.3-3.1)
    value: 2.3-3.1
    unit: g per kg FAT-FREE MASS per day
    effect: multiply by fat-free mass, never by body weight; fat-free mass = body_weight_kg x (1 - body_fat_pct/100); body fat unknown -> do not use this band, use the body-weight band above
    basis: Helms 2014 abstract
    basis_grade: A (definitional)
  - rule: per-meal-is-a-target
    when: sizing one meal's or one nudge's protein
    value: 0.4-0.55
    unit: g per kg body weight per meal
    effect: a distribution target (0.4 x 4 meals = 1.6; 2.2 / 4 = 0.55), not a usable-absorption cap; capping a nudge at one sitting is a tractability convention, never spoken as "the rest is wasted"
    basis: Schoenfeld & Aragon 2018 conclusion; nutrition/protein-per-meal-ceiling-008
    basis_grade: B
  - rule: renal-gate
    when: renal_condition known CKD or reduced kidney function
    value: 1.3
    unit: g per kg body weight per day
    effect: do not show the cut band; KDIGO advises avoiding intakes above 1.3 in CKD at risk of progression; route to the treating clinician; unknown is the baseline (no known renal impairment), not a block
    basis: KDIGO 2024 practice point 3.3.2 (ungraded)
    basis_grade: D (guideline practice point)
refraction_notes:
  - note: >
      THE FLOOR IS THE SUPPORTED PART. Every deficit trial located that compared
      roughly 1.0-1.2 g/kg against roughly 2.3-2.4 g/kg favoured the higher arm
      for lean mass (Mettler 2010, Longland 2016), and Pasiakos 2013 found both
      1.6 and 2.4 better than 0.8. No trial in trained lifters in a deficit
      separated 1.6 from 2.4. So "at least 1.6 in a cut" carries the evidence;
      the choice inside 1.6-2.4 is a judgement on leanness and deficit size.
    grade: B
  - note: >
      UNIT TRAP. The often-quoted 2.3-3.1 g/kg deficit band (Helms 2014) is per
      kilogram of FAT-FREE MASS, not body weight. For an 80 kg lifter at 15
      percent body fat it is about 156-211 g a day, not 184-248 g. Item 002's
      carve-out note quotes the band without the unit; read it through this
      note. Without a body-fat value, quote the body-weight band only.
    grade: A
  - note: >
      2.2 IS NOT A CEILING. Morton 2018's plateau at 1.62 g/kg is an unadjusted,
      non-significant break point (p=0.079) whose 95 percent interval runs to
      2.20, built from trials that were mostly at energy balance and that
      topped out at 2.4 g/kg. The authors suggest about 2.2 as a prudent target
      for someone maximising gains; that is a recommendation, not a measured
      upper limit, and it says nothing about a deficit, where the trials that
      exist used 2.3-2.4.
    grade: B
  - note: >
      SMALL, SHORT TRIALS. The deficit RCTs ran two to four weeks with 20-40
      people; Longland's subjects were young men whose resistance-training
      history the registry does not record, and Pasiakos's were not lifters.
      The direction is consistent; effect sizes are not transportable to a
      12-week cut.
    grade: C
  - note: >
      KIDNEYS ARE THE ONE HARD GATE. Known chronic kidney disease withdraws the
      cut band (KDIGO 2024 advises avoiding more than 1.3 g/kg/day when CKD is
      at risk of progressing). No evidence located shows harm from 1.6-2.4 g/kg
      in people with normal kidney function, and none is claimed here.
    grade: D
claim: >
  For a resistance-trained adult in a calorie deficit, daily protein of at least
  about 1.6 g per kg of body weight is supported, and the working band is
  1.6-2.4 g/kg, moving toward the top as the person gets leaner and the deficit
  gets steeper. Short randomised deficit trials consistently favoured about
  2.3-2.4 g/kg over 1.0-1.2 g/kg for lean mass (Mettler 2010, n=20 trained
  athletes, -0.3 vs -1.6 kg; Longland 2016, n=40, +1.2 vs +0.1 kg), while 1.6
  and 2.4 g/kg were not separated in the one trial that tested both (Pasiakos
  2013, non-lifters). The 2.3-3.1 figure from Helms 2014 is per kg of fat-free
  mass. The 2.2 g/kg figure from Morton 2018 is the upper end of a confidence
  interval around a non-significant break point from mostly energy-balance
  trials, not a ceiling for a cut. The 0.4 and 0.55 g/kg per-meal figures from
  Schoenfeld & Aragon 2018 are distribution targets across at least four meals,
  not limits on what one meal can use.
reasoning: >
  The floor rests on randomised trials with a consistent direction and on two
  meta-analyses that place the lean-mass benefit at or above about 1.6 g/kg, so
  it sits at the RCT-level band. The upper end is held lower and flagged
  contested: the reviews that argue for higher intakes in lean dieters (Helms
  2014, 6 small studies) and the one trial that tested 1.6 against 2.4 and found
  no separation (Pasiakos 2013) point in different directions, and none of it is
  in trained lifters over a full cut. Two readings of shipped numbers were
  corrected at the primary. Morton's 2.2 was never a measured limit; the
  full text gives p=0.079 for the break point and an interval of 1.03-2.20, and
  the trials in it reached only 2.4 g/kg. Schoenfeld & Aragon state 0.4 g/kg/meal
  as a target intake and 0.55 as the arithmetic of 2.2 over four meals, in a
  paper whose own conclusion is that protein above 20 g is not all oxidised;
  using either as an absorption cap inverts the paper. The renal gate is the one
  safety axis with a guideline behind it, and it is a practice point, so it is
  carried as a gate with its weak basis named.
---

# nutrition/protein-deficit-trained-lifter-023

In a cut, protein is the lever that most clearly protects muscle, and the
supported part is a floor: about 1.6 grams per kilogram of body weight per day
or more. Short deficit trials that put trained or hard-training people on
roughly 2.3-2.4 g/kg against roughly 1.0-1.2 g/kg kept or gained more lean mass
in the higher group. Inside 1.6-2.4 the evidence does not pick a number, and the
usual coaching move (lean and dieting hard -> nearer the top) is a judgement the
reviews support in direction only.

Three numbers in circulation are routinely misread. The 2.3-3.1 band from Helms
is per kilogram of fat-free mass, so it is smaller than it looks when multiplied
by body weight. Morton's 2.2 is the edge of a confidence interval around a
plateau that did not reach statistical significance, from trials mostly at
energy balance; it is not a wall, least of all in a deficit. And the 0.4 and
0.55 g/kg per meal figures are a way to spread a daily target across four
meals, not a statement that a bigger meal is wasted.

Kidney disease is the one case that changes the answer: there the cut band is
withdrawn and the question goes to the treating clinician.

## Engine rules (diet card)

| Rule | Value | Unit | Effect | Basis band |
|---|---:|---|---|---|
| cut-floor | 1.6 | g/kg BW/day | cut-day target not below this | RCT-level |
| cut-band-high | 2.4 | g/kg BW/day | top of band; lean or steep deficit moves toward it | observational/review |
| no-evidence-ceiling-at-2.2 | 2.2 | g/kg BW/day | not a clamp in a cut | RCT-level reading |
| ffm-unit-guard | 2.3-3.1 | g/kg FFM/day | multiply by fat-free mass only | definitional |
| per-meal-is-a-target | 0.4-0.55 | g/kg BW/meal | distribution target, not an absorption cap | RCT-level reading |
| renal-gate | 1.3 | g/kg BW/day | known CKD -> no cut band, route | practice point |

## 한국어 요약 (답변용)

- 감량 중인 근력운동인은 하루 단백질을 체중 1 kg당 최소 1.6 g 정도로 잡는다. 이 하한이 근거가
  가장 단단한 부분이다.
- 1.6-2.4 g/kg 사이에서는 연구가 숫자를 하나로 정해주지 않는다. 몸이 마를수록, 적자가 클수록
  위쪽으로 잡는 것은 방향만 뒷받침되는 판단이다.
- 흔히 보는 "2.3-3.1 g/kg"는 체중이 아니라 제지방량 기준이다. 체지방률을 모르면 이 숫자는 쓰지 않는다.
- "2.2 g/kg가 상한"은 연구가 말한 것이 아니다. 유의하지 않은 꺾임점의 신뢰구간 끝값이고, 감량
  시험들은 2.3-2.4 g/kg를 썼다.
- 끼니당 0.4-0.55 g/kg는 하루 목표를 네 끼에 나누는 계산이지, 그 이상 먹으면 버려진다는 뜻이 아니다.
- 신장 질환이 있으면 감량용 고단백 범위를 보여주지 않고 담당 의료진에게 넘긴다. 신장 기능이 정상인
  사람에게 1.6-2.4 g/kg가 해롭다는 근거는 찾지 못했고, 그렇다고 말하지도 않는다.
- 한국인 영양소 섭취기준의 단백질 권장량은 인구집단 적정 섭취 기준이다. 감량 중 훈련 목표를 대신하거나
  고쳐 주는 값으로 쓰지 않는다.
