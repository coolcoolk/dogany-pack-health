---
# RIR-accuracy sprint 2026-10-07 (dispatch kw-ex-rir-accuracy). Owns the SET
# LOG: how much a logged repetitions-in-reserve number can carry once it is
# stored on a set row -- by set position, rep count / load, distance from
# failure and exercise type -- and what the logger may compute from it (e1RM
# input, floor-breach reading, increase trigger). NOT restated here:
# the method comparison and RIR-vs-plate-step resolution (030), and the
# day-level readiness read and load-step sizes
# (exercise/rir-accuracy-readiness-signals-061, released v37 from the
# kw-deload sprint; both rows kept their numbers at the v38 merge, and 061
# links back here). Where this row refines a 061 rule it says so by rule
# name. Both rows carry a block named rir_rules: 061's is the DAY read,
# this row's is the SET log; read each from its own item.
#
# rir_rules is structured data for the set logger / rx code. Values are
# directions plus product constants; each entry carries its own basis_grade.
# The YAML-subset reader returns numbers as strings. No program code changed.
#
# Excluded on purpose: Hughes LJ, Peiffer JJ, Scott B 2020, J Strength Cond
# Res, doi 10.1519/JSC.0000000000003865 ("Estimating RIR in four commonly
# used resistance exercises", the free-weight vs Smith and 65/75/85% 1RM estate-scrub:allow(Smith machine, gym equipment)
# study). It is RETRACTED (J Strength Cond Res 2021;35(3):585). Its
# "accurate at 85%, not at 65-75%" finding circulates widely; do not cite it.
id: exercise/rir-set-log-accuracy-077
domain: exercise
grade: B (logged RIR runs low -- lifters under-predict reps left -- and the error grows far from failure, in long sets and in the first set of an exercise; training years do not predict accuracy); C (squat-pattern reads less accurate than bench; practice with feedback improving accuracy; the error-band widths); D (every rir_rules threshold and the post-set logging transfer)
lane: "@performance-lit"
locale: universal
as_of: 2017-2026
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/34542869/"  # Halperin I et al. 2022, Sports Med 52(2):377-390, doi 10.1007/s40279-021-01559-x -- scoping review + exploratory meta-analysis, 12 studies, n=414: under-prediction 0.95 reps (95% CI 0.17-1.73), I2 97.9%; more accurate nearer failure (beta -0.025, CI -0.05 to 0.0014), in sets of 12 reps or fewer (beta 0.06 vs 0.47 over 12), in later sets (beta -0.07, trivial); training status no effect (beta -0.006); upper minus lower body -0.58 reps (CI -2.32 to 1.16). Abstract read 2026-10-07
  - "https://pubmed.ncbi.nlm.nih.gov/30747900/"  # Zourdos MC et al. 2021, J Strength Cond Res 35(2S):S158-S165, doi 10.1519/JSC.0000000000002995 -- n=25 trained men (training age 4.7 y), one squat set to failure at 70% 1RM (16 +/- 4 reps): error at called RIR 1 = 2.05 +/- 1.73, RIR 3 = 3.65 +/- 2.46, RIR 5 = 5.15 +/- 2.92 reps; more reps per set predicted error at RIR 5 and 3; training age did not. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/37967832/"  # Refalo MC et al. 2024, J Strength Cond Res 38(3):e78-e85, doi 10.1519/JSC.0000000000004653 -- n=24 trained (12 M, 12 F), bench 75% 1RM, calls at 1 and 3 RIR: raw -0.17 +/- 1.00, absolute 0.65 +/- 0.78 reps; equivalent (+/-1 rep) between 1 and 3 RIR, set 1 and 2, session 1 and 2; no relation to sex, years trained or relative strength. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/32881842/"  # Mansfield SK et al. 2020, J Strength Cond Res (online ahead of print), doi 10.1519/JSC.0000000000003779 -- n=20 trained men, bench and prone row, 3 sets at 60% and 80% 1RM: RIR under-estimated on SET 1 at both loads (ES 1.30-2.89) and set 2 of 80% bench (ES 0.39); accuracy improved sets 1-3; knowing the load or the %1RM did not change estimates. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/37036795/"  # Remmert JF, Laurson KR, Zourdos MC 2023, Percept Mot Skills 130(3):1239-1254, doi 10.1177/00315125231169868 -- n=58 (27 M, 31 F), biceps curl, triceps pushdown, seated row (machine/cable, single- and multi-joint) at 72.5% 1RM, 4 sets to failure: more accurate nearer failure and in later sets; NO exercise effect (p=0.688); sex, experience and RIR-rating experience did not matter. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/40249908/"  # Hermann T et al. 2025, Med Sci Sports Exerc 57(9):2021-2031, doi 10.1249/MSS.0000000000003728 -- RCT n=42 trained, 8 weeks single-set failure vs 2-RIR: RIR estimation more accurate for bench than squat; accuracy improved over the intervention, particularly for bench. Abstract read; magnitudes not in abstract
  - "https://pubmed.ncbi.nlm.nih.gov/28933716/"  # Helms ER et al. 2017, J Strength Cond Res 31(10):2938-2943, doi 10.1519/JSC.0000000000002097 -- n=12 powerlifters, 3 weeks, self-selected loads for target RPE on squat/bench/deadlift: mean absolute miss 0.33 +/- 0.28 RPE; bench closer than squat for 8 reps at RPE 8; squat power sets took 3 weeks to peak accuracy. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/37436724/"  # Remmert JF et al. 2023, Percept Mot Skills 130(5):2139-2160, doi 10.1177/00315125231189098 -- n=9 trained men, bench 3x/week for 6 weeks, last set to failure with calls at 4 and 1 RIR: no significant change in ABSOLUTE error; raw error drifted toward more under-estimation over time and in higher-rep sets. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/42632893/"  # Wiedenmann T et al. 2026, BMC Sports Sci Med Rehabil 18(1):375, doi 10.1186/s13102-026-01997-y -- n=26 (13 younger, 13 older), bench and leg press at 75-85% 1RM, calls at 4 and 2 RIR then to failure, 6 sessions: mean absolute error fell by up to 2.3 reps; no age effect. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/29204323/"  # Steele J et al. 2017, PeerJ 5:e4105, doi 10.7717/peerj.4105 -- n=141, pre-set prediction of reps to failure, full-body single sets: under-prediction about 2.6-3.4 reps; tendency to improve with experience. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/33424678/"  # Armes C et al. 2020, Front Psychol 11:565416, doi 10.3389/fpsyg.2020.565416 -- trained at least 1 year, knee extension at 70% 1RM / 70% MVC, self-determined RM vs actual failure: under-prediction 2.0 reps (95% CI 0.0-4.0). Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/38595310/"  # Hickmott LM, Butcher SJ, Chilibeck PD 2024, J Strength Cond Res 38(7):1206-1212, doi 10.1519/JSC.0000000000004784 -- n=36 (18 M, 18 F) bench, calls at 4 and 2 RIR: an individual velocity-RIR profile beat subjective calls on sets 1-2 and at 75-80% 1RM. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/42328880/"  # Chen W et al. 2026, J Strength Cond Res (online ahead of print), doi 10.1519/JSC.0000000000005549 -- n=19 well-trained men, hexagonal-bar deadlift 65% and 85%: velocity-based RIR estimation failed every accuracy criterion. Abstract read; recorded so velocity is not assumed to rescue deadlift reads
  - "https://pubmed.ncbi.nlm.nih.gov/38662926/"  # Ruiz-Alias SA et al. 2024, J Strength Cond Res 38(8):1379-1385, doi 10.1519/JSC.0000000000004805 -- n=19 men, squat and bench at 65/75/85% 1RM, calls at RIR 5 and 2: under-estimation in about 15% of RIR-5 sets and 4-8% of RIR-2 sets. Abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/40902458/"  # Gomez-Redondo P et al. 2025, Exp Gerontol 210:112884, doi 10.1016/j.exger.2025.112884 -- n=25 older adults, chest press 65%: predicted RIR 2 was -2.1 reps, RIR 4 -1.6 reps vs actual. Abstract read; population note only
  - "https://pubmed.ncbi.nlm.nih.gov/38970765/"  # Robinson ZP et al. 2024, Sports Med 54(9):2209-2231, doi 10.1007/s40279-024-02069-2 -- meta-regressions on estimated RIR: strength flat across a wide RIR range; hypertrophy rises nearer failure. Abstract read; used for what a 1-rep log error costs
  - "https://pubmed.ncbi.nlm.nih.gov/38393985/"  # Refalo MC et al. 2024, J Sports Sci 42(1):85-101, doi 10.1080/02640414.2024.2321021 -- n=18 trained, within-participant 8 weeks: leg press / leg extension at perceived 2 / 1 RIR gave quadriceps growth similar to failure. Abstract read
  - "exercise/autoregulation-vs-percentage-prescription-030"  # within-warehouse: method comparison and the resolution argument (1 rep ~3-4% of 1RM near 85%); its "no improvement over six weeks" line is the Remmert 2023 result, now one of three practice studies (note 5)
  - "exercise/rir-accuracy-readiness-signals-061"  # within-warehouse (v37, kw-deload sprint): day-level readiness read, 2-rep action threshold, load-step size; this row refines its experience-does-not-calibrate and read-near-the-target rules for the set log
  - "exercise/progression-modality-load-vs-reps-028"  # within-warehouse: progressing by reps at a fixed load is an equivalent route for hypertrophy
  - "exercise/increment-verification-floor-029"  # within-warehouse: the measurement floor on retests; e1RM drift below it is not a verified change
  - "framework:GRADE -- direction rests on one exploratory meta-analysis with I2 97.9% plus a consistent run of small primary studies (n 9-141, mostly trained young men, mostly bench and squat, all INTRASET calls followed by a set to failure). Magnitudes vary several-fold by protocol (0.65 reps on a 75% bench vs 2-5 reps on a 16-rep 70% squat), so widths are C. Practice effects split 2-1 across three small studies. No study validates the post-set RIR a logger stores, which is a retrospective estimate with no failure test behind it."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
rir_rules:
  - rule: logged-rir-runs-low
    applies_when: any working set with a logged RIR
    value: lifters on average have more reps left than they report; a logged RIR is closer to a lower bound than a centre
    engine: read the true RIR as at or above the logged value; do not subtract a safety buffer; do not add a correction either (the size varies too much between people and protocols)
    basis: Halperin 2022; Refalo 2024; Zourdos 2021; Mansfield 2020; Steele 2017
    basis_grade: B
  - rule: precise-zone
    applies_when: reps 12 or fewer AND logged RIR 0-3
    value: the reading is good to about one rep (absolute error 0.65 +/- 0.78 reps on a 75% bench, equivalent at 1 and 3 RIR)
    engine: usable as a number -- e1RM input, floor check, increase trigger
    basis: Refalo 2024; Halperin 2022
    basis_grade: C
  - rule: coarse-zone
    applies_when: reps over 12, OR logged RIR 4 or more (the "4+" key)
    value: error of 2 to 5 reps (at RIR 3 and 5 on a 16-rep squat set, 3.65 and 5.15 reps)
    engine: ordinal only ("far from failure"); exclude from e1RM; never fires a load change; for these sets progress by reps at a fixed load (028)
    basis: Zourdos 2021; Halperin 2022
    basis_grade: B
  - rule: first-set-reads-low
    applies_when: the first working set of an exercise in a session
    value: the first set is the least accurate and is under-estimated most (large effect sizes at 60% and 80%); later sets read better
    engine: a first-set RIR alone does not fire a step-down; confirm with reps achieved or a later set. Refines 061 read-near-the-target -- 061 reads the anchor set first, this row says that read leans "harder than it was"
    basis: Mansfield 2020; Remmert 2023 (single-joint); Halperin 2022
    basis_grade: C
  - rule: e1rm-input-choice
    applies_when: estimating e1RM from logged sets of one exercise in one session
    value: e1RM = load x (1 + (reps + RIR) / 30) moves about 1/30 of the load per rep; an under-reported RIR of 1 lowers e1RM by about 2.5-3%
    engine: feed only precise-zone sets; among sets at the same load prefer the one with the lowest logged RIR (nearest failure, most accurate); the resulting e1RM is conservative, so do not discount it further; an e1RM change below the 029 floor is not a verified change
    basis: rule over Halperin 2022, Zourdos 2021 and 029
    basis_grade: D
  - rule: increase-trigger
    applies_when: a slot with target RIR t (for a floor slot, t = rir_floor)
    value: because logged RIR runs low, a reading above target is credible -- the bias works against false increase signals
    engine: propose a load increase when the LAST working set at the same load logs RIR of t+1 or more with reps at or above target, on 2 consecutive exposures; one exposure is a prompt to watch, not a trigger (2 exposures is a product constant)
    basis: rule over Halperin 2022; Refalo 2024
    basis_grade: D
  - rule: floor-breach-reading
    applies_when: logged RIR below rir_floor on a floor slot
    value: a logged 0-1 may truly be 1-2; the reading still means the set ended close to failure
    engine: keep the breach flag as is (the cap is on the prescription, and a conservative over-flag costs little); say "close to failure", not "you went to failure"; never edit the logged value
    basis: rule over Halperin 2022
    basis_grade: D
  - rule: exercise-type
    applies_when: squat-pattern free-weight lifts vs bench / machine / isolation
    value: squat reads were less accurate than bench in two studies; among machine and cable single- and multi-joint lifts no exercise difference was found; upper vs lower body was not clearly different in the pooled data
    engine: no separate error numbers per exercise; squat-pattern slots keep the 2-exposure rule strictly and do not use a single-session exception
    basis: Hermann 2025; Helms 2017; Remmert 2023 (single-joint); Halperin 2022
    basis_grade: C
  - rule: experience-is-not-accuracy
    applies_when: choosing error assumptions by user
    value: years of training did not predict accuracy in the pooled data or in four primary studies
    engine: same rules for every training_status; never widen or narrow bands by experience
    basis: Halperin 2022; Zourdos 2021; Refalo 2024; Remmert 2023 (single-joint)
    basis_grade: B
  - rule: practice-with-feedback
    applies_when: deciding whether to calibrate a user
    value: CONTESTED -- accuracy improved over sessions that ended in failure in two studies (Hermann 2025, mostly bench; Wiedenmann 2026, up to 2.3 reps over 6 sessions) and did not in one (Remmert 2023, n=9, 6 weeks)
    engine: optional calibration only on non-floor slots (machine, cable, isolation) where a set taken to failure is acceptable; never on rir_floor slots; show the gap between called and actual reps; promise nothing about improvement
    basis: Hermann 2025; Wiedenmann 2026; Remmert 2023 (6 weeks)
    basis_grade: C
  - rule: counted-beats-estimated
    applies_when: reps at a fixed load and the logged RIR disagree across sessions
    value: reps are counted, RIR is estimated
    engine: rep gains at the same load are the progression evidence; RIR breaks ties and sets the speech, never overrides the rep count
    basis: rule over the whole set
    basis_grade: D
  - rule: post-set-log-unvalidated
    applies_when: always (the logger stores RIR after a set the user chose to end)
    value: every accuracy study used calls made DURING a set that then went to failure; a post-set RIR with no failure test behind it has not been validated
    engine: treat the above as the best available transfer; do not present logged RIR as measured
    basis: absence across all sources
    basis_grade: D
refraction_notes:
  - note: >
      THE LOG LEANS LOW. In the pooled data lifters said they had about one
      rep fewer left than they did, and the first set of an exercise leaned
      lowest. For a logger that is a useful asymmetry: e1RM computed from
      logged RIR comes out conservative, and a logged RIR above target is
      believable. It also means a logged 0-1 may really have been 1-2.
    grade: B
  - note: >
      TWO ZONES, NOT ONE NUMBER. Near failure in a set of 12 or fewer reps,
      trained lifters were within about two-thirds of a rep on the bench.
      Far from failure or in long sets the same people missed by 2 to 5
      reps (16-rep squat sets at 70%). The "4+" key is therefore a category,
      and long sets are progressed by counted reps, not by RIR.
    grade: B
  - note: >
      SQUAT IS HARDER TO READ THAN BENCH. Two trials (an 8-week RCT and a
      3-week powerlifter study) found squat reads less accurate than bench;
      the pooled upper-vs-lower comparison was inconclusive and machine
      lifts showed no exercise effect. Held at C and used only to keep the
      2-exposure rule strict on squat-pattern slots.
    grade: C
  - note: >
      EXPERIENCE NO, PRACTICE MAYBE. Training years did not predict accuracy
      anywhere it was tested. Practice with feedback from sets taken to
      failure improved accuracy in two studies and not in a third. The
      warehouse line "does not improve over six weeks" (030, 061; both
      scoped to it at v38) is the
      third study and should be spoken as one result of three, not as
      settled.
    grade: C
  - note: >
      WHAT A ONE-REP ERROR COSTS. Strength gains were flat across a wide RIR
      range, and stopping at a perceived 1-2 RIR gave similar quadriceps
      growth to failure over eight weeks. A one-rep logging error is
      therefore small for outcomes; it matters for the arithmetic the
      logger does with it (e1RM, triggers), which is why the rules above
      gate that arithmetic rather than the training.
    grade: C
  - note: >
      RETRACTED STUDY EXCLUDED. The widely quoted "RIR is accurate at 85%
      but not at 65-75% of 1RM" comes from a 2020 four-exercise study that
      was retracted in 2021. What survives is weaker: the pooled data tie
      better accuracy to heavier loads through fewer reps per set, and one
      non-retracted study found that knowing the load or its %1RM did not
      change estimates. The logger therefore gates on rep count, not on a
      %1RM cut-off.
    grade: B
claim: >
  A logged repetitions-in-reserve number is a useful but low-leaning
  estimate. Lifters under-predict the reps they have left by about one on
  average (12 studies, 414 people, very heterogeneous), most in the first
  set of an exercise, and far more when the set is long or ended far from
  failure: within about two-thirds of a rep for 1-3 RIR calls on a 75%
  bench, but 2 to 5 reps off on 16-rep squat sets at 70%. Squat reads were
  less accurate than bench in two studies; machine lifts showed no exercise
  effect. Years of training do not predict accuracy; practice with feedback
  from sets taken to failure helped in two studies of three. For a set
  logger this means: use RIR as a number only on sets of 12 reps or fewer
  logged at RIR 0-3; treat "4+" and long sets as ordinal; build e1RM only
  from those sets and accept that it comes out conservative; let a logged
  RIR above target on two consecutive exposures propose an increase; keep
  floor-breach flags but speak them as "close to failure"; and let counted
  reps outrank estimated RIR. All accuracy data are calls made during a set
  that then went to failure; the post-set RIR a logger stores has not been
  validated directly. Every threshold in the rules is a product constant.
reasoning: >
  Halperin 2022 supplies the direction and the moderators (nearer failure,
  12 reps or fewer, later sets, not training status); its I2 of 97.9% is
  why widths are taken from primary studies instead. The two anchor
  primaries bracket the range: Refalo 2024 (trained men and women, 75%
  bench, calls at 1 and 3 RIR, absolute error 0.65 reps, no difference by
  set, session, sex or experience) and Zourdos 2021 (trained men, 70%
  squat to failure at 16 reps, error 2.05 / 3.65 / 5.15 reps at called 1 /
  3 / 5 RIR, driven by reps per set). Mansfield 2020 and Remmert 2023 on
  single-joint machines give the first-set and later-set effect and show
  that knowing the load or its %1RM did not move estimates; the retracted
  Hughes 2020 is the usual source of a %1RM cut-off and is excluded, so the
  rules gate on rep count (Halperin's load effect runs through it).
  Exercise type rests on Hermann 2025 and Helms 2017 (bench better than
  squat) against a null pooled upper-lower contrast and a null exercise
  effect across machine lifts, hence C. Practice is split: Remmert 2023 (n=9,
  6 weeks bench) found no change in absolute error, while Hermann 2025 and
  Wiedenmann 2026 found improvement over sessions ending in failure; this is
  why the row is contested and why calibration is confined to slots where
  failure is permitted, leaving the compound floor policy intact. The
  engine rules translate the bias into arithmetic: e1RM = load x (1 +
  (reps + RIR) / 30) moves about 1/30 of the load per rep, so the bias makes
  e1RM conservative rather than inflated; a high reading is credible
  because the error runs the other way; a single first-set reading is the
  least trustworthy. Robinson 2024 and Refalo 2024 (J Sports Sci) bound the
  cost of a one-rep error on outcomes as small. The final rule records the
  absence: no study validates a post-set estimate without a failure test,
  which is exactly what a logger stores.
---

# exercise/rir-set-log-accuracy-077 -- 기록된 RIR은 얼마나 믿을 수 있나: 세트 기록기의 사용 규칙

**한 줄 그림:** 기록된 RIR은 대개 실제보다 낮게 적힌다. 12회 이하·RIR 0~3 세트에서는 한 개 안팎으로
맞지만, 긴 세트나 "4+"는 2~5개씩 틀린다. 숫자로 쓰는 곳과 범주로만 쓰는 곳을 나눈다.

## Accuracy by situation

| Situation | What the studies found | Logger use |
|---|---|---|
| 12 reps or fewer, RIR 0-3 | about 0.65 reps absolute error (75% bench) | number: e1RM, floor, trigger |
| over 12 reps, or RIR 4+ | 2-5 reps off (16-rep squat at 70%) | category only; progress by reps |
| first working set of an exercise | least accurate, leans low | no step-down from it alone |
| later sets | more accurate | prefer for e1RM |
| squat-pattern vs bench | squat less accurate (two studies) | keep the 2-exposure rule strict |
| machine / cable lifts | no exercise difference | same rules |
| years of training | no effect | same rules for everyone |
| practice with failure feedback | helped in two of three studies | calibrate only on non-floor slots |

Thresholds (12 reps, RIR 0-3, two exposures) are the plan's rules, not measured cut-offs.

## 한국어 요약 (답변용)

- 사람들은 "몇 개 더 할 수 있었나"를 평균 한 개쯤 적게 말한다. 그래서 기록된 RIR은 실제 여유의
  아래쪽 값에 가깝다. 여유분을 더 빼지도, 보정값을 더하지도 않고 그대로 읽는다.
- 12회 이하 세트에서 RIR 0~3으로 기록했다면 한 개 안팎으로 맞는다(벤치 75%에서 평균 0.65개 차이).
  이런 세트만 숫자로 써서 추정 1RM과 증량 판단에 쓴다.
- 12회가 넘는 세트나 "4+"는 2~5개씩 틀렸다(스쿼트 70%, 16회 세트). "아직 여유가 많다"는 뜻으로만
  읽고, 이런 세트는 같은 무게에서 반복 수를 늘려 진행한다.
- 운동의 첫 세트가 가장 부정확하고 실제보다 힘들게 느껴진다. 첫 세트 RIR 하나만 보고 무게를 내리지
  않는다. 실제로 몇 개를 했는지, 다음 세트가 어땠는지를 같이 본다.
- 추정 1RM은 RIR이 한 개 적게 적히면 2.5~3% 정도 낮게 나온다. 그래서 기록에서 나온 추정 1RM은
  보수적인 값이고, 더 깎을 필요가 없다.
- 목표보다 RIR이 1개 이상 높게, 같은 무게로 두 번 연속 기록되면 증량을 제안한다. 기록이 원래 낮게
  적히는 쪽이라 높게 적힌 값은 믿을 만하다. 한 번만이면 지켜보자고만 말한다.
- 하한(RIR 2)이 걸린 종목에서 0~1이 기록되면 경고는 그대로 내되, "실패했다"가 아니라 "실패에 꽤
  가까웠다"고 말한다. 기록된 숫자는 고치지 않는다.
- 스쿼트는 벤치보다 RIR 읽기가 부정확했다(두 연구). 머신·케이블 운동끼리는 차이가 없었다.
- 운동 경력이 길다고 더 정확하지 않았다. 실패까지 가 보고 차이를 확인하는 연습은 세 연구 중 두
  곳에서 정확도를 높였다. 그런 확인은 머신·케이블·고립 운동에서만 하고, 하한이 걸린 복합 프리웨이트
  종목에서는 하지 않는다.
- 같은 무게에서 반복 수가 늘었다면 그게 진행의 증거다. 셀 수 있는 반복 수가 추정인 RIR보다 앞선다.
- 이 연구들은 모두 세트 도중에 "이제 몇 개 남았다"고 말한 뒤 실패까지 해서 확인했다. 세트를 끝낸 뒤
  적는 RIR을 직접 검증한 연구는 없다. 기록된 RIR을 측정값처럼 말하지 않는다.
- "85%에서는 정확하고 65~75%에서는 부정확하다"는 널리 퍼진 결과는 철회된 논문에서 나왔다. 쓰지
  않는다.
