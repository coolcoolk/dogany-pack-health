---
# Alcohol-and-training sprint 2026-10-07 (dispatch kw-nu-alcohol-training-cut).
# What a realistic social dose does to the things a lifter on a cut tracks:
# post-exercise muscle protein synthesis, strength recovery, sleep, and fat
# loss. Filed under nutrition because the questions are diet and training
# questions; the health-outcome rows stay in leisure (@drinking-epidemiology,
# 009-011) and are linked, not repeated. Every effect is stated per gram of
# ethanol per kg of body weight, because that is how the trials dosed it; the
# Korean glass/bottle conversion lives in the sibling KR row (032).
#
# alcohol_rules is structured data for retro / diet copy (no module reads it
# yet). Each rule names a dose band, the direction to speak, the framing to
# avoid, and the graded basis. Bands are g ethanol per kg body weight; the
# band edges 0.25 / 0.75 are Pietila 2018's categories, the 0.5 / 1.0 / 1.5
# anchors are the trial doses. They are evidence anchors, not safe limits.
id: nutrition/alcohol-training-recovery-dose-031
domain: nutrition
lane: "@obs-inferential"
grade: "B (that REM sleep falls with dose and is already reduced near 0.5 g/kg; that drinking adds energy without compensation at the next meal); B (direction only: about 1 g/kg or more after hard training impairs strength recovery and post-exercise protein synthesis); C (every magnitude from the n=8-10 muscle trials, the null at 0.5 g/kg, and the 10-week training trial); A (the energy arithmetic, 7 kcal per gram)"
locale: universal
as_of: 1999-2026
contested: no
sources:
  - "https://doi.org/10.1371/journal.pone.0088384"  # Parr EB, Camera DM, Areta JL, Burke LM, Phillips SM, Hawley JA, Coffey VG. PLoS One 2014;9(2):e88384. PMID 24533082 -- randomised crossover, 8 active men, resistance + cycling session, 1.5 g/kg alcohol (12 +/- 2 standard drinks) over the recovery period: myofibrillar protein synthesis 24% lower than protein alone when alcohol was taken WITH 25 g whey x2, 37% lower with carbohydrate instead of protein; MPS still rose above rest in every arm (~29-109%)
  - "https://doi.org/10.1007/s00421-009-1311-3"  # Barnes MJ, Mundel T, Stannard SR. Eur J Appl Physiol 2010;108(5). -- 10 men, 300 maximal eccentric quadriceps contractions then 1 g/kg alcohol vs orange juice: at 36 h isometric torque down 40.9% vs 28.7%, concentric 42.8% vs 31.9%, eccentric 44.8% vs 25.9%
  - "https://doi.org/10.1007/s00421-010-1655-8"  # Barnes MJ, Mundel T, Stannard SR. Eur J Appl Physiol 2011;111(4):725-729. PMID 20878178 -- same model, 0.5 g/kg: no difference from control at 36 or 60 h (n=10, null, not powered for small effects)
  - "https://doi.org/10.1519/JSC.0000000000001468"  # Duplanty AA, Budnar RG, Luk HY, Levitt DE, Hill DW, McFarlin BK, Huggett DB, Vingren JL. J Strength Cond Res 2017;31(1):54-61. PMID 27135475 -- 10 trained men, 9 trained women, heavy squats then alcohol vs placebo: mTOR/S6K1 phosphorylation lower at +3 h in men only; signalling, not measured synthesis. Dose not re-read from the full text
  - "https://doi.org/10.3390/biom13010002"  # Levitt DE, Luk HY, Vingren JL. Biomolecules 2022;13(1):2. PMID 36671386 -- narrative review: alcohol impairs and resistance exercise activates mTORC1; feeding, sex, training status and quantity modify it; many questions open
  - "https://doi.org/10.1016/j.smrv.2024.102030"  # Gardiner C, Weakley J, Burke LM, Roach GD, Sargent C, Maniar N, Huynh M, Miller DJ, Townshend A, Halson SL. Sleep Med Rev 2025;80:102030 -- systematic review + meta-analysis, 27 controlled studies, healthy adults: REM duration -11.3 min overall, significant from ~0.50 g/kg and worse with dose; REM onset +18.0 min (+30.1 min per 1 g/kg); sleep onset faster only at >=0.85 g/kg; total sleep time, efficiency and WASO not determinable (wide intervals); timing of intake did not moderate effects; no sex moderation overall
  - "https://doi.org/10.2196/mental.9519"  # Pietila J, Helander E, Korhonen I, Myllymaki T, Kujala UM, Lindholm H. JMIR Ment Health 2018;5(1):e23. PMC5878366 -- observational, 4098 Finnish employees, HRV-based recovery in the first 3 h of sleep: -9.3 percentage units at <=0.25 g/kg, -24.0 at >0.25-0.75, -39.2 at >0.75; similar in active and sedentary people
  - "https://doi.org/10.1017/S0007114518003677"  # Kwok A, Dordevic AL, Paton G, Page MJ, Truby H. Br J Nutr 2019;121(5):481-495. PMID 30630543 -- systematic review, 22 crossover/RCTs, 701 adults aged 18-37: no compensation for alcohol energy; alcohol raised food energy intake by 343 kJ (95% CI 161-525) and total intake by 1072 kJ (820-1323); heterogeneity and small-study effects noted
  - "https://doi.org/10.1093/ajcn/70.5.928"  # Siler SQ, Neese RA, Hellerstein MK. Am J Clin Nutr 1999;70(5):928-936. PMID 10539756 -- 8 healthy men, 24 g alcohol, isotope methods: de novo lipogenesis 0.8 g over 6 h (<5% of the dose); 77% of cleared alcohol went to plasma acetate; adipose fatty-acid release -53%, whole-body lipid oxidation -73%
  - "https://doi.org/10.3390/nu11040909"  # Molina-Hidalgo C, De-la-O A, Jurado-Fasoli L, Amaro-Gahete FJ, Castillo MJ. Nutrients 2019;11(4):909. PMID 31018614 -- BEER-HIIT, 72 young adults, 10 weeks HIIT 2x/week; men 2 x 330 mL and women 1 x 330 mL of 5.4% beer or vodka-equivalent Mon-Fri (computed ~28 g and ~14 g ethanol/day): DXA fat mass fell and lean mass rose in all training arms, not influenced by alcohol. Alcohol vs no-alcohol was SELF-CHOSEN; only beer vs ethanol and 0.0 beer vs water were randomised
  - "https://doi.org/10.1186/s12970-020-00356-7"  # Molina-Hidalgo C, De-la-O A, Dote-Montero M, Amaro-Gahete FJ, Castillo MJ. J Int Soc Sports Nutr 2020;17(1):29. PMID 32460793 -- same trial: VO2max and test duration improved in all training arms regardless of beverage
  - "source:nutrition/metabolizable-energy-atwater-015 -- the energy-factor row; ethanol is counted at 7 kcal/g"
  - "source:nutrition/kr-alcohol-units-drinking-pattern-032 -- converts g/kg into 잔 and bottles for Korean drinks"
  - "source:leisure/alcohol-jcurve-collapse-009 -- why no rule here may say a drink is good for health"
  - "source:leisure/kr-aldh2-flushing-010 -- flushing is a metabolic signal; this row does not lower its bands for flushers on muscle grounds (no data)"
  - "source:exercise/protein-anabolic-window-002 -- the protein-timing context the MPS rule sits in"
  - "source:exercise/autoregulation-vs-percentage-prescription-030 -- next-day load is set by readiness, not by a drinking penalty"
  - "source:sleep-recovery/sleep-loss-performance-decrement-004 -- what a short or broken night does to the next session"
  - "source:nutrition/weekend-drift-073 -- (parallel v38 sprint) weekend intake drift, of which drinking is one part"
  - "framework:GRADE -- sleep: a meta-analysis of 27 controlled crossover studies with a dose-response, kept at RCT level with wide prediction intervals noted. Muscle: three small randomised crossovers (n=8, 10, 10) and one signalling study, consistent in direction at about 1 g/kg and above, imprecise in size, so direction B and magnitude C; the 0.5 g/kg null is one underpowered trial (C). Energy intake: meta-analysis of 22 trials with heterogeneity (B). Lipid-oxidation mechanism: n=8 isotope study (C as a magnitude, carried as mechanism). The 10-week training trial had self-selected alcohol exposure and about 14 people per arm (C). No trial tested a lifter's hypertrophy over months against social drinking."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: hedge
      rescale:
        per_unit_low: 0.5    # g ethanol per kg body weight where trial harms begin to show (REM reduction, Gardiner 2025)
        per_unit_high: 1.0   # g/kg where strength recovery was measurably worse (Barnes 2010); a range, not a safe limit
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
      gate:
        allowed: [not_pregnant, none]
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
dose_bands:
  - band: light
    g_per_kg: "< 0.25"
    example_70kg_g: "< 17.5"
    what_is_measured: HRV-based recovery in the first 3 h of sleep about 9 points lower (observational); no muscle trial at this dose
    basis_grade: C
  - band: moderate
    g_per_kg: "0.25 - 0.75"
    example_70kg_g: "17.5 - 52.5"
    what_is_measured: REM sleep reduced from about 0.5 g/kg; strength recovery after damaging exercise not different at 0.5 g/kg (one null trial)
    basis_grade: B
  - band: heavy
    g_per_kg: "0.75 - 1.5"
    example_70kg_g: "52.5 - 105"
    what_is_measured: at 1 g/kg strength loss 36 h after eccentric damage about 11-19 points larger; REM loss larger; HRV recovery about 39 points lower above 0.75
    basis_grade: B
  - band: very-heavy
    g_per_kg: ">= 1.5"
    example_70kg_g: ">= 105"
    what_is_measured: post-exercise myofibrillar protein synthesis 24% lower even with 2 x 25 g whey, 37% lower without protein (n=8)
    basis_grade: C
alcohol_rules:
  - rule: energy-counts
    trigger: any logged drink on a diet day
    say: count the ethanol at 7 kcal per gram plus the drink's carbohydrate; it is energy like any other, not a separate penalty
    avoid: calling it empty calories that wreck the cut, or treating it as uncountable
    basis: nutrition/metabolizable-energy-atwater-015
    basis_grade: A
  - rule: food-follows-drink
    trigger: drinking occasion on a cut
    say: drinking usually adds food rather than replacing it (trials show no compensation and roughly 80 kcal more food); planning the 안주 helps more than trimming the next day
    avoid: advising skipped meals before or after drinking to make room
    basis: Kwok 2019
    basis_grade: B
  - rule: fat-burning-pauses
    trigger: user asks whether alcohol turns into fat
    say: very little alcohol becomes fat directly; the body burns it first and burns less fat for some hours, so it is the total energy for the day that decides fat change
    avoid: saying alcohol is stored as fat, or that one night undoes a week
    basis: Siler 1999
    basis_grade: C
  - rule: protein-window-blunted
    trigger: heavy or very-heavy band within the evening after a training session
    say: a big night after training blunts that session's protein-synthesis response (about a quarter even with protein in the one trial); eating a protein meal before and keeping protein in the plan is the lever that helped
    avoid: saying the session was wasted or muscle was lost; MPS still rose above rest
    basis: Parr 2014
    basis_grade: C
  - rule: low-dose-no-measured-muscle-cost
    trigger: light or moderate band up to about 0.5 g/kg after training
    say: at this amount no muscle-recovery cost has been measured; the clearer cost is sleep quality
    avoid: claiming it is proven harmless, or that a drink helps recovery
    basis: Barnes 2011
    basis_grade: C
  - rule: strength-recovery-heavy
    trigger: heavy band or above within a day of hard or new eccentric-heavy training
    say: expect slower strength recovery for a couple of days; set the next session by readiness and RPE instead of forcing planned loads
    avoid: prescribing punishment cardio or a skipped session as a penalty
    basis: Barnes 2010
    basis_grade: C
  - rule: sleep-not-a-sleep-aid
    trigger: drinking within about 3 h of bedtime, any band; user mentions drinking to sleep
    say: alcohol may make falling asleep faster only at large amounts, while REM sleep is cut from about 0.5 g/kg (about 35 g for a 70 kg person) and more with each drink; a nightcap is not a sleep aid
    avoid: recommending a nightcap; stating total sleep time is reduced as fact (not determinable in the meta-analysis)
    basis: Gardiner 2025
    basis_grade: B
  - rule: habitual-moderate-not-blocking
    trigger: user worries a regular beer with dinner cancels training
    say: in a 10-week trial, a daily beer or two on weekdays did not stop fat loss, lean gain or fitness gains from training; amount and the rest of the day's food matter more than the habit itself
    avoid: overstating this as permission or as a health benefit (009); the trial was small and not randomised for drinking
    basis: Molina-Hidalgo 2019, 2020
    basis_grade: C
  - rule: no-moralizing
    trigger: every alcohol mention in retro or diet copy
    say: report dose, timing and the measured effect in plain terms, then one practical lever; same tone as a late-night meal
    avoid: guilt, cheat-day language, 반성, counting drinks back at the user unasked, health-benefit claims, medical or addiction language from intake data alone
    basis: nutrition/alcohol-training-recovery-dose-031 note 6
    basis_grade: D
refraction_notes:
  - note: >
      DOSE IS PER KILOGRAM, AND THE MUSCLE TRIALS USED LARGE DOSES. The only
      measured cut to post-exercise protein synthesis came at 1.5 g/kg, which
      the authors put at about twelve standard drinks. Strength recovery was
      measurably worse at 1 g/kg and not at 0.5 g/kg. So "alcohol kills
      gains" is true of a very heavy night after training and is not shown
      for one or two drinks. The same grams are a bigger dose for a lighter
      person; the body_weight_kg rescale exists for that.
    grade: C
  - note: >
      THE DIRECTION ABOVE ABOUT 1 g/kg IS CONSISTENT. Two independent small
      randomised crossovers (protein synthesis, strength) and a signalling
      study point the same way, and a review agrees. What is not known is how
      big the effect is for a trained lifter over months, because no trial ran
      that long with drinking as the exposure.
    grade: B
  - note: >
      SLEEP IS THE COST THAT SHOWS AT SOCIAL DOSES. Across 27 controlled
      studies, REM sleep fell by about 11 minutes on average, was already
      significantly lower near 0.5 g/kg, and fell further with each extra
      drink; REM started later. Faster sleep onset appeared only at about
      0.85 g/kg and above. In a real-world sample of 4098 employees, heart
      rate variability recovery early in the night dropped even at the
      lightest dose band, in active and sedentary people alike. The
      meta-analysis could not determine total sleep time, so copy must not
      claim it shrinks.
    grade: B
  - note: >
      FAT LOSS RUNS THROUGH ENERGY, NOT MAGIC. Ethanol is 7 kcal per gram.
      After 24 g, the body burned about three quarters less fat for some
      hours while it cleared the alcohol, and turned less than 5 percent of
      the alcohol into fat. In trials, people did not eat less to make room
      for drinks and ate somewhat more. So the advice is to count it and
      plan the food around it, not to treat it as uniquely fattening.
    grade: B
  - note: >
      SEX DIFFERENCES ARE NOT SETTLED. In one study the signalling drop
      after squats appeared in men and not women; the sleep meta-analysis
      found no sex moderation overall, but in one large trial women showed
      sleep losses at the doses given while men did not. Do not speak a
      sex-specific rule; use g/kg, which already scales for size.
    grade: C
  - note: >
      HOW TO SAY IT. This row exists so retro and diet copy can mention a
      drinking night the way it mentions a late meal: what was measured at
      that dose, and one lever (protein before, food planned, next session
      by readiness, no nightcap for sleep). No guilt, no "cheat", no
      health-benefit claims (009), no addiction or medical language from a
      log entry (that is a clinician's frame), and no lower personal limit
      invented from a muscle study. Pregnancy and medication unknown ->
      withhold numbers (block_specifics).
    grade: D
claim: >
  At social doses the measurable cost of drinking for a lifter on a cut is
  mostly sleep and energy, and the muscle cost shows up at heavy doses. A
  2025 meta-analysis of 27 controlled studies found REM sleep reduced by
  about 11 minutes on average, significantly from about 0.5 g ethanol per kg
  (roughly 35 g for a 70 kg person) and more with each drink, with faster
  sleep onset only at about 0.85 g/kg and above; total sleep time could not
  be determined. Post-exercise myofibrillar protein synthesis was 24 percent
  lower at 1.5 g/kg even with 2 x 25 g whey (37 percent lower without
  protein) in eight men, and strength loss 36 h after eccentric damage was
  larger at 1 g/kg but not different at 0.5 g/kg in two ten-person trials.
  For fat loss, ethanol counts at 7 kcal/g; after 24 g, fat oxidation fell
  about 73 percent while very little alcohol became fat, and across 22
  trials people did not eat less to compensate and ate about 343 kJ more
  food. In a 10-week training trial, a weekday beer or two did not stop
  fat loss or lean gain. Magnitudes from the muscle trials are imprecise
  and none tested months of lifting. The rules attached here state dose,
  timing and one practical lever, without moralising and without any
  health-benefit claim.
reasoning: >
  The questions a training-and-diet agent gets about drinking are practical:
  did last night undo the workout, will it stall the cut, does a beer help me
  sleep. The literature answers them unevenly. Sleep has a proper
  meta-analysis with a dose-response, so it carries the most confident rule,
  and it is also the effect that appears at ordinary amounts. The muscle
  literature is three small crossovers whose direction agrees above about
  1 g/kg; that supports saying a very heavy night after training costs
  something and does not support a percentage for two drinks, so magnitudes
  are held at the observational band and the low-dose null is carried as an
  underpowered null rather than proof of safety. Fat loss is mostly
  arithmetic plus a trial-level finding that people do not compensate, with
  the lipid-oxidation study kept as mechanism. BEER-HIIT is the only
  training-length trial; its alcohol exposure was self-chosen and arms were
  small, so it is used only to stop copy from catastrophising a habit. The
  dose bands use Pietila's 0.25 / 0.75 g/kg categories as edges because they
  are the only published bands, with trial doses as anchors; they are not
  limits. The no-moralising rule is product judgement and graded as such.
  Health effects of drinking are deliberately left to the leisure rows.
---

# nutrition/alcohol-training-recovery-dose-031 -- 술 마신 다음 날, 운동과 다이어트는 어떻게 되나

**한 줄 그림:** 한두 잔의 대가는 주로 잠(렘수면)과 칼로리다. 근육 회복을 늦춘다는 결과는 운동한 날 밤 크게 마셨을 때(체중 1kg당 1g 이상) 나왔다.

## Dose bands (engine-readable)

Grams of ethanol per kg body weight. The 70 kg column is arithmetic only;
the Korean glass and bottle conversion is in
`nutrition/kr-alcohol-units-drinking-pattern-032`.

| Band | g/kg | 70 kg person | What was measured |
|---|---|---|---|
| light | under 0.25 | under ~17 g | early-night HRV recovery about 9 points lower (observational) |
| moderate | 0.25-0.75 | ~17-52 g | REM sleep down from ~0.5 g/kg; strength recovery unchanged at 0.5 (one null trial) |
| heavy | 0.75-1.5 | ~52-105 g | strength loss after eccentric damage larger at 1.0; more REM loss |
| very heavy | 1.5 and up | ~105 g and up | post-exercise protein synthesis 24% lower even with whey (n=8) |

## The copy rules (engine-readable)

| Rule | When | Say | Do not say |
|---|---|---|---|
| energy-counts | any drink on a diet day | count 7 kcal/g plus the drink's carbs | "empty calories wreck the cut" |
| food-follows-drink | a drinking night on a cut | plan the 안주; drinking adds food, it does not replace it | skip meals to make room |
| fat-burning-pauses | "does alcohol become fat?" | burned first, fat burning pauses; the day's total decides | "stored as fat", "one night undoes a week" |
| protein-window-blunted | heavy+ after training | protein meal first; the session still counted | "workout wasted", "muscle lost" |
| low-dose-no-measured-muscle-cost | up to ~0.5 g/kg | no muscle cost measured; sleep is the cost | "proven harmless", "helps recovery" |
| strength-recovery-heavy | heavy+ within a day of hard training | next session by readiness/RPE | punishment cardio, skip as penalty |
| sleep-not-a-sleep-aid | drinking near bedtime | REM drops from ~0.5 g/kg; nightcap is not a sleep aid | "helps you sleep", "less total sleep" as fact |
| habitual-moderate-not-blocking | "a beer with dinner cancels training?" | a 10-week trial saw gains anyway; amount and food matter | permission or health benefit |
| no-moralizing | every mention | dose, timing, measured effect, one lever | guilt, 반성, cheat-day, addiction language |

## 한국어 요약 (답변용)

- 근육 단백질 합성이 줄었다는 연구는 운동 직후 체중 1kg당 알코올 1.5g, 표준잔으로 열두 잔 정도를 마신
  경우다. 단백질(유청 25g 두 번)을 같이 먹었어도 24%, 단백질 없이 마시면 37% 낮았다. 그래도 합성은 쉬는
  상태보다는 올라갔다. 운동이 헛수고가 된 건 아니다.
- 근력 회복은 1kg당 1g을 마셨을 때 36시간 뒤 근력 손실이 더 컸고, 0.5g에서는 차이가 없었다. 둘 다
  10명짜리 연구라 정확한 크기는 모른다. 크게 마신 다음 날은 계획한 무게를 고집하지 말고 컨디션과 RPE로
  정한다.
- 적게 마셔도 드러나는 대가는 잠이다. 27개 실험을 모은 분석에서 렘수면이 평균 11분쯤 줄었고, 1kg당
  0.5g 근처부터 확실히 줄어 잔이 늘수록 더 줄었다. 빨리 잠드는 효과는 많이 마셨을 때만 나타났다. 자기
  전에 마시는 술은 수면제가 아니다. 다만 총 수면시간이 준다고는 말하지 않는다. 그건 분석에서 결론이
  안 났다.
- 다이어트에서는 알코올 1g이 7kcal다. 몸은 알코올을 먼저 태우느라 몇 시간 동안 지방을 덜 태우지만,
  알코올이 직접 지방으로 바뀌는 양은 아주 적다. 결국 하루 전체 칼로리가 결정한다. 실험에서 사람들은 술을
  마신 만큼 덜 먹지 않았고 오히려 조금 더 먹었다. 그래서 다음 날 굶기보다 안주를 미리 정하는 편이 낫다.
- 평일 저녁에 맥주 한두 캔을 마신 사람도 10주 운동 효과(체지방 감소, 근육량 증가)가 그대로 나왔다. 작고
  음주 여부를 무작위로 정하지 않은 연구라 "마셔도 된다"는 근거로는 쓰지 않는다.
- 말투: 야식 먹은 날처럼 말한다. 마신 양과 시간, 그 양에서 확인된 영향, 실천할 것 하나. 죄책감, 반성,
  치팅데이 같은 표현, 술이 건강에 좋다는 말, 기록만 보고 중독이나 질환을 말하는 건 하지 않는다. 임신
  여부나 복용 약을 모르면 숫자는 말하지 않는다.
