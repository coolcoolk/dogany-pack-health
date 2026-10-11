---
# Cardio-in-a-cut sprint 2026-10-06 (dispatch task kw-cardio-cut). The
# EVIDENCE row for concurrent aerobic + resistance training when the goal is
# losing fat while keeping strength and muscle. 063 is the engine-readable
# placement rule built on it. Headline: on average the interference effect on
# whole-muscle size and maximal strength is about zero; what remains is a small
# set of modifiers (lower-body strength in trained lifters, same-session
# stacking, running at the fibre level, dose) and one deficit fact that is
# bigger than all of them -- cardio's energy cost is part of the deficit.
#
# v38 MERGE (2026-10-07, dispatch kw-consolidate-2): a parallel sprint
# (kw-ex-cardio-interference-cut) wrote the same row from the same sources
# as provisional "concurrent-cardio-interference-fat-loss" (070). It was
# never released and is folded in here, not shipped as a second row. What it
# added that this row lacked: Gergley 2009, the only located trial with
# incline treadmill walking as the concurrent arm (it found incline walking
# WORSE than cycling for leg-press gains). Its placement rules went to 063.
id: exercise/concurrent-cardio-interference-cut-062
domain: exercise
grade: B (on average concurrent training does not blunt whole-muscle hypertrophy or maximal strength; RT-first sequencing helps lower-body dynamic strength); C (modifiers -- trained lifters and same-session stacking, running vs cycling, frequency and duration, the ~500 kcal/day deficit ceiling for lean-mass gain); C contested (incline walking: one small untrained RCT found it costs more leg strength than cycling); D (anything about stepmill, and every transfer of these modifiers into a deficit in trained lifters)
lane: "@performance-lit"
locale: universal
as_of: 2009-2022
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/34757594/"  # Schumann M, Feuerbacher JF, Sünkeler M, Freitag N, Rønnestad BR, Doma K, Lundberg TR 2022, Sports Med 52(3):601-612, PMC8891239 -- 43 studies, concurrent vs identical RT alone, >=4 weeks supervised: maximal strength SMD -0.06 (95% CI -0.20 to 0.09), hypertrophy -0.01 (-0.16 to 0.18), explosive strength -0.28 (-0.48 to -0.08); explosive-strength loss only when same session, not when separated by >=3 h; no moderator effect of cycling vs running, frequency (>5 vs <5 sessions/week), training status or age
  - "https://pubmed.ncbi.nlm.nih.gov/35476184/"  # Lundberg TR, Feuerbacher JF, Sünkeler M, Schumann M 2022, Sports Med 52(10):2391-2403, PMC9474354 -- 15 studies, muscle FIBRE hypertrophy: overall SMD -0.23 (95% CI -0.46 to -0.00); type I fibres with running SMD -0.81 (-1.26 to -0.36), not with cycling; no effect of order, frequency or training status
  - "https://pubmed.ncbi.nlm.nih.gov/33751469/"  # Petré H, Hemmingsson E, Rosdahl H, Psilander N 2021, Sports Med 51(5):991-1010, PMC8053170 -- 27 studies, lower-body 1RM: trained ES -0.35, moderately trained -0.20 (ns), untrained 0.03; in trained, same session ES -0.66 vs different sessions -0.10 (ns)
  - "https://pubmed.ncbi.nlm.nih.gov/22002517/"  # Wilson JM, Marin PJ, Rhea MR, Wilson SM, Loenneke JP, Anderson JC 2012, J Strength Cond Res 26(8):2293-2307 -- 21 studies, 422 ESs: hypertrophy ES RT 1.23 vs concurrent 0.85; running but not cycling decremented hypertrophy and strength; endurance frequency (r -0.26 to -0.35) and duration (r -0.29 to -0.75) negatively related to hypertrophy, strength and power
  - "https://pubmed.ncbi.nlm.nih.gov/28783467/"  # Murlasits Z, Kneffel Z, Thalib L 2018, J Sports Sci 36(11):1212-1219 -- same-session order: lower-body 1RM +3.96 kg (95% CI 0.81 to 7.10) when strength precedes endurance; VO2max unaffected by order
  - "https://pubmed.ncbi.nlm.nih.gov/28917030/"  # Eddens L, van Someren K, Howatson G 2018, Sports Med 48(1):177-188 -- 10 studies: RT-then-endurance +6.91% lower-body dynamic strength (95% CI 1.96 to 11.87); no order effect on lower-body hypertrophy, static strength, VO2max or body-fat percentage
  - "https://pubmed.ncbi.nlm.nih.gov/29658408/"  # Sabag A, Najafi A, Michael S, Esgin T, Halaki M, Hackett D 2018, J Sports Sci 36(21):2472-2483 -- HIIT + RT vs RT: hypertrophy and upper-body strength unaffected; lower-body strength ES -0.248 (p=0.049); cycling HIIT trend ES -0.377 (p=0.074), running HIIT -0.176 (ns) -- the modality direction is the OPPOSITE of Wilson 2012 for HIIT
  - "https://pubmed.ncbi.nlm.nih.gov/25546450/"  # Robineau J, Babault N, Piscione J, Lacome M, Bigard AX 2016, J Strength Cond Res 30(3):672-683 -- n=58 amateur rugby players, 7 weeks, strength always first: bench and half-squat 1RM gains lower with 0 h between sessions than with 6 h or 24 h; VO2peak gain largest at 24 h; authors advise >=6 h between the two
  - "https://pubmed.ncbi.nlm.nih.gov/19387377/"  # Gergley JC 2009, J Strength Cond Res 23(3):979-987 -- RCT n=30 untrained, 2x/week for 9 weeks: leg-press gains resistance-only > resistance + cycling > resistance + INCLINE TREADMILL WALKING (men); the only located trial with incline walking as the cardio arm (abstract read; folded in at v38 from the kw-ex-cardio-interference-cut sprint)
  - "https://pubmed.ncbi.nlm.nih.gov/34623696/"  # Murphy C, Koehler K 2022, Scand J Med Sci Sports 32(1):125-137 -- RCTs, RT in an energy deficit >=3 weeks: lean-mass gain impaired (ES -0.57, p=0.02), strength gain not (ES -0.31, p=0.28); meta-regression: a deficit of ~500 kcal/day prevented lean-mass gain
  - "https://pubmed.ncbi.nlm.nih.gov/28514618/"  # Villareal DT et al. 2017, N Engl J Med 376(20):1943-1955, PMC5552187 -- n=160 obese older adults, diet + aerobic / resistance / combined, 6 months, ~9% weight loss in every exercise arm: lean mass fell 5% with aerobic only, 3% combined, 2% resistance only; strength +18% combined, +19% resistance, +4% aerobic
  - "https://pubmed.ncbi.nlm.nih.gov/23019316/"  # Willis LH et al. 2012, J Appl Physiol 113(12):1831-1837, PMC3544497 -- STRRIDE AT/RT, n=119 overweight adults, 8 months: aerobic and combined lost more body and fat mass than resistance only; resistance and combined gained more lean mass than aerobic only
  - "https://pubmed.ncbi.nlm.nih.gov/19127177/"  # Donnelly JE et al. 2009, ACSM Position Stand, Med Sci Sports Exerc 41(2):459-471 -- 150-250 min/week moderate activity gives modest weight loss; >250 min/week associated with clinically significant loss; resistance training does not enhance weight loss but may increase fat-free mass
  - "https://pubmed.ncbi.nlm.nih.gov/24998610/"  # Helms ER, Fitschen PJ, Aragon AA, Cronin J, Schoenfeld BJ 2015, J Sports Med Phys Fitness 55(3):164-178 -- narrative recommendations for natural bodybuilding prep: lowest cardio frequency and duration that achieves the fat loss; full-body modes or cycling may reduce interference; high intensity needs more recovery
  - "nutrition/weight-loss-rate-lean-mass-012"  # within-warehouse: rate of loss and lean mass; the deficit this item's cardio feeds into
  - "nutrition/energy-availability-threshold-010"  # within-warehouse: cardio energy cost lowers energy availability
  - "exercise/deficit-volume-guidance-016"  # within-warehouse: lifting volume in a deficit (theory-only); this item does not change it
  - "exercise/recovery-kinetics-session-spacing-025"  # within-warehouse: session spacing; same caution about tables
  - "exercise/ideal-endurance-runner-triathlete-042"  # within-warehouse: the archetype-level summary of the same interference evidence
  - "framework:GRADE -- the null average effect rests on a 43-study meta-analysis with tight intervals. The modifiers come from subgroup analyses that are underpowered and partly contradict each other (running worse in Wilson 2012 and at type I fibres in Lundberg 2022; cycling HIIT trend worse in Sabag 2018; no modality effect in Schumann 2022). Nearly every trial was run at energy balance in untrained or moderately trained people; the only diet-plus-modality trials located are in obese middle-aged or older adults. One small RCT (Gergley 2009, n=30 untrained) used incline treadmill walking as the concurrent arm and found it cost MORE leg-press gain than cycling; no trial uses a stepmill or stair climber."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      TRAINING STATUS DECIDES WHETHER PLACEMENT MATTERS. In untrained and
      moderately trained people adding cardio did not measurably cost
      lower-body 1RM; in trained lifters it did, and only when the cardio sat
      in the same session (separate sessions: no clear loss). For a beginner
      the placement rules in 063 are cheap tidiness, not a protected outcome;
      for a trained lifter on a cut they are the main lever.
    grade: C
  - note: >
      MODE IS CONTESTED -- DO NOT SPEAK "RUNNING KILLS GAINS". Running looked
      worse than cycling in an older pooled analysis and at the type I fibre
      level, but the largest and newest whole-muscle analysis found no mode
      effect, and for HIIT the trend pointed the other way (cycling HIIT
      slightly worse for leg strength). Carry it as a mild preference for
      lower-impact, concentric-dominant cardio when leg training matters,
      nothing stronger.
    grade: C
  - note: >
      STEPMILL HAS NO INTERFERENCE DATA. It is low impact and
      concentric-dominant like cycling, which is the proposed reason cycling
      interferes less (less eccentric damage, closer movement pattern to hip
      and knee extension work). That is mechanism by analogy. A hard stepmill
      session is still leg work and should be counted as leg fatigue by the
      scheduler.
    grade: D
  - note: >
      INCLINE WALKING HAS ONE TRIAL, AND IT CUTS AGAINST THE GYM HABIT. In 30
      untrained people training twice a week for 9 weeks, adding incline
      treadmill walking cost more leg-press gain than adding cycling (Gergley
      2009). One small trial, untrained, men driving the effect: it does not
      rank incline walking below running, but it does mean incline walking
      is never spoken as "interference-free" or ranked level with cycling.
    grade: C
  - note: >
      THE DEFICIT IS THE BIGGER INTERFERENCE. In the pooled deficit trials,
      strength gains survived a deficit but lean-mass gains did not, and a
      deficit of about 500 kcal a day was where lean-mass gain stopped.
      Cardio burns energy that comes out of that same deficit. Adding 300 kcal
      of cardio on top of an unchanged 500 kcal diet deficit is an 800 kcal
      deficit. The ceiling is a meta-regression estimate from mixed
      populations, not a measured threshold for this user.
    grade: C
  - note: >
      CARDIO DOES NOT REPLACE LIFTING IN A CUT. When dieting adults lost the
      same weight, aerobic-only training lost the most lean mass and strength
      barely moved; adding resistance training kept lean mass and strength
      close to resistance-only. The cut keeps the lifting; cardio is added
      around it, never swapped in for it.
    grade: B
claim: >
  Adding cardio to resistance training does not, on average, reduce gains in
  muscle size or maximal strength (43-study meta-analysis, effects about zero
  with tight intervals). The cost appears in narrower places: explosive
  strength when both are done in the same session; lower-body maximal
  strength in already-trained lifters, again mainly when both share a
  session; a small negative effect at the muscle-fibre level, larger with
  running than cycling in one analysis; and larger losses with more frequent
  and longer endurance work. When both share a session, lifting first gives
  slightly better lower-body strength gains with no cost to aerobic fitness.
  Separating the two by at least about 6 hours (one rugby trial: 0 h worse
  than 6 h or 24 h) avoids most of the same-session loss. In a fat-loss
  phase the larger threat to muscle is the size of the total energy deficit,
  to which cardio contributes: strength gains survive a deficit, lean-mass
  gains stop at roughly 500 kcal a day. Lifting stays in the plan; cardio is
  added to it, not substituted for it.
reasoning: >
  The modern pooled evidence (Schumann 2022, Lundberg 2022, Petré 2021)
  overturned the older blanket interference story (Hickson 1980, Wilson 2012)
  for whole-muscle outcomes but kept a residual effect for explosive
  strength, fibre-level growth and trained lifters' leg strength. The
  sequencing analyses agree with each other on direction and size (about
  4 kg or 7 percent of lower-body 1RM). The modality question is genuinely
  split across analyses, so it is carried as a weak preference and the item
  is flagged contested. None of the concurrent trials were run in a deficit
  in trained lifters; the deficit facts come from a separate meta-analysis
  (Murphy and Koehler 2022) and from diet-plus-modality trials in obese
  middle-aged and older adults (Willis 2012, Villareal 2017). The transfer of
  the modifiers into a cut is therefore an inference, which is why the
  practical rule built on this row (063) sits at the practitioner floor.
---

# exercise/concurrent-cardio-interference-cut-062 -- 감량기에 유산소가 근력·근육을 깎는가

**한 줄 그림:** 평균적으로 유산소를 더해도 근육 크기와 최대 근력은 줄지 않는다. 손해는 같은 세션에 붙일 때,
이미 훈련된 사람의 하체 근력, 그리고 유산소 소모가 키운 적자에서 나온다.

## What moves the effect

| Modifier | Direction | Strength of evidence |
|---|---|---|
| Average concurrent vs lifting only | about zero for size and max strength | 43-study meta-analysis |
| Same session vs separated (>=3-6 h) | same session costs explosive strength; trained lifters' leg 1RM | subgroup analyses + one RCT |
| Lift first vs cardio first (same session) | lift first: about +4 kg / +7% leg 1RM | two meta-analyses, consistent |
| Running vs cycling | split: running worse (older pool, type I fibres); cycling HIIT trend worse; newest pool no difference | contested |
| Stepmill | no data; analogy to cycling | mechanism only |
| Incline walk | one trial: worse than cycling for leg-press gains | one small RCT, untrained |
| More minutes, more sessions | more interference (correlational) | one older meta-analysis |
| Training status | untrained ~none; trained lifters lose leg 1RM in same-session stacking | one meta-analysis |
| Deficit size (diet + cardio cost) | lean-mass gain stops near 500 kcal/day; strength kept | one meta-analysis + meta-regression |

## 한국어 요약 (답변용)

- 유산소를 같이 한다고 근육이 줄거나 최대 근력이 덜 오르는 건 평균적으로 아니다. 큰 메타분석에서
  차이가 거의 0이었다.
- 손해가 나는 자리는 좁다. 같은 날 같은 세션에 붙이면 순발력이 덜 오르고, 이미 운동을 오래 한 사람은
  하체 1RM이 덜 오른다. 따로 떼면(최소 몇 시간, 가능하면 6시간 이상이나 다른 날) 대부분 사라진다.
- 같은 세션에 해야 하면 웨이트 먼저, 유산소 나중. 하체 근력에 조금 유리하고 심폐 쪽 손해는 없다.
- 달리기가 자전거보다 나쁘다는 말은 연구마다 엇갈린다. "달리면 근손실"이라고 말하지 않는다. 다리 운동이
  중요할 때 충격이 적은 종목을 조금 더 권하는 정도다. 스텝밀은 직접 연구가 없고, 경사 걷기는
  작은 연구 하나(30명)에서 오히려 자전거보다 다리 근력 손해가 컸다. 둘 다 "간섭이 없다"고 말하지 않는다.
- 감량기에 더 큰 문제는 적자 크기다. 유산소로 태운 열량도 적자에 들어간다. 연구를 모아 보면 하루 약
  500kcal 적자 즈음에서 근육 증가가 멈췄다(근력은 유지). 이 숫자는 혼합 집단의 추정치다.
- 감량기에도 웨이트는 빼지 않는다. 유산소만 한 집단이 근육을 가장 많이 잃었다. 유산소는 웨이트에
  더하는 것이지 바꾸는 것이 아니다.
