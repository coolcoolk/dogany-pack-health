---
# Injury-caution follow-up 2026-10-07 (dispatch task kw-ex-shoulder-prehab-dose).
# The shoulder half of "add, don't only subtract" (056 note 4): once a shoulder
# caution is recorded, HOW MUCH external-rotation / lower-trapezius / scapular
# work goes into the plan, how often, how heavy, and where in the session. The
# prevention trials are in handball (overhead throwers), the treatment trials
# in subacromial / rotator-cuff-related pain; no trial was found in lifters, so
# every number here is a transported protocol, labelled as such.
#
# shoulder_prehab is structured data for the composer (field guide:
# docs/kimwog-shoulder-prehab-fields.md). Each row keys to 056 rungs; numbers
# are copied from the protocol named in `basis`, never derived. Rows marked
# basis_grade D are product judgement on top of those protocols.
id: exercise/shoulder-prehab-dose-074
domain: exercise
grade: B (exercise-based shoulder programmes reduce shoulder problems in overhead athletes; specific cuff plus scapular exercise helps persistent subacromial pain); C (transport to lifters; resisted and progressive beats non-resisted; scapula-only focus no better beyond 6 weeks); D (set, frequency and placement numbers for lifters; keeping fatiguing cuff work after pressing)
lane: "@clinical-physio"
locale: universal
as_of: 2010-2022
contested: no
sources:
  - "https://bjsm.bmj.com/content/51/14/1073"  # Andersson SH, Bahr R, Clarsen B, Myklebust G 2017, Br J Sports Med 51(14):1073-1080 -- cluster RCT, 45 elite handball teams, 660 players, one 7-month season: OSTRC Shoulder Injury Prevention Programme 3x/week in the warm-up; shoulder-problem prevalence 17% vs 23%, OR 0.72 (95% CI 0.52 to 0.98); substantial problems OR 0.78 (0.53 to 1.16, not significant)
  - "https://bjsm.bmj.com/content/bjsports/51/14/1073/DC1/embed/inline-supplementary-material-1.pdf"  # the programme sheet itself (read in full 2026-10-07): five exercises, 3 x 8-16 reps (external rotation / drop-and-catch / backwards throw 3 x 10-20; sleeper or cross-body stretch 3 x 30 s), exercises change every six weeks; progress by more reps, then a stiffer band, then a small weight or weighted ball; "reduce load and seek medical attention if you experience shoulder pain during the exercises"
  - "https://search.pedro.org.au/search-results/record-detail/70387"  # Asker M, Hägglund M, Waldén M, Källberg H, Skillgate E 2022, Sports Med Open -- three-armed cluster RCT, 18 schools, 627 adolescent elite handball players: Shoulder Control programme 3x/week for a year; shoulder injury rate HRR 0.44 (95% CI 0.29 to 0.68). Read at abstract (PEDro record); programme sets/reps not read
  - "https://www.bmj.com/content/bmj/344/bmj.e787.full.pdf"  # Holmgren T et al. 2012, BMJ 344:e787 -- RCT n=102, persistent (>6 months) subacromial impingement after failed conservative care: 2 eccentric cuff + 3 concentric/eccentric scapular-stabiliser exercises + posterior shoulder stretch, each strengthening exercise 3 x 15 twice daily for 8 weeks, once daily weeks 8-12; load set by the pain-monitoring model (no more than 5/10 during, pain back to pre-exercise level before the next session, else load down). Successful outcome 69% vs 24%; chose surgery 20% vs 63%. Read at full text
  - "https://e-space.mmu.ac.uk/626200/3/Malliaras%20et%20al%202020_%20high%20vs%20low%20dose%20systematic%20review.pdf"  # Malliaras P et al. 2020, Arch Phys Med Rehabil 101(10):1822-1834 -- systematic review, 3 RCTs, n=283: higher vs lower exercise dose in rotator cuff tendinopathy -- low to very low certainty and conflicting; no dose shown to be needed. Read at abstract
  - "https://pedro.org.au/english/systematic-review-found-that-resisted-and-progressive-exercise-reduces-pain-and-dysfunction-but-non-resisted-or-non-progressive-exercise-does-not-in-people-with-rotator-cuff-related-shoulder-pain/"  # Naunton J, Littlewood C, Street G, Haines T, Malliaras P 2020, Clin Rehabil 34(9):1198-1216 -- 7 RCTs, n=468: progressive and resisted exercise vs no treatment/placebo, composite pain/dysfunction MD 15 points (95% CI 9 to 21), clinical importance uncertain; non-progressive or non-resisted MD 4 (-2 to 9), not significant, and more short-term pain flares (RR 3.77, 1.49 to 9.54); all low certainty. Read via PEDro evidence summary
  - "https://keele-repository.worktribe.com/output/406161/effectiveness-of-scapula-focused-approaches-in-patients-with-rotator-cuff-related-shoulder-pain-a-systematic-review-and-meta-analysis"  # Bury J et al. 2016, Man Ther -- scapula-focused vs generalised approaches, 4 RCTs (n=190 pain): benefit up to 6 weeks (pain change not clinically significant), not apparent by 3 months. Read at abstract
  - "https://bjsm.bmj.com/content/52/2/102"  # Hickey D et al. 2018, Br J Sports Med 52(2):102-110 -- 5 prospective studies, 419 athletes: scapular dyskinesis at baseline, RR 1.43 (95% CI 1.05 to 1.93) for shoulder pain over 9-24 months
  - "https://bjsm.bmj.com/content/48/17/1327"  # Clarsen B et al. 2014, Br J Sports Med 48(17):1327-1333 -- prospective cohort, 206 elite male handball players: external rotation strength OR 0.71 per 10 Nm, total rotational motion OR 0.77 per 5 degrees, obvious scapular dyskinesis OR 8.41 (1.47 to 48.1)
  - "https://search.pedro.org.au/search-results/record-detail/60634"  # Fredriksen H, Cools A, Bahr R, Myklebust G 2020, Scand J Med Sci Sports -- RCT in young handball players: the OSTRC programme changed NEITHER external rotation strength NOR internal rotation range of motion. Read at abstract
  - "https://scholars.nova.edu/en/publications/shoulder-joint-and-muscle-characteristics-among-weight-training-p/"  # Kolber MJ et al. 2017, J Strength Cond Res 31(4):1024-1032 -- cross-sectional, 55 recreational weight-training men (24 with subacromial impingement): impingement group had lower bodyweight-adjusted external-rotator and lower-trapezius strength and less IR/ER range. Association only, direction unknown
  - "https://experts.mcmaster.ca/scholarly-works/1774717"  # Chopp JN, O'Neill JM, Hurley K, Dickerson CR 2010, J Shoulder Elbow Surg 19(8):1137-1144 -- lab study: after a protocol designed to fatigue the whole rotator cuff, the humeral head migrated superiorly on radiographs. Mechanism only; read at record
  - "https://research.bond.edu.au/en/publications/the-epidemiology-of-injuries-across-the-weight-training-sports/"  # Keogh JWL, Winwood PW 2017, Sports Med -- weight-training sports: shoulder among the most commonly injured sites (with lower back, knee, elbow, wrist/hand); mostly retrospective designs
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the rungs every shoulder_prehab row keys to
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: the pain ceiling; Steuri 2017 (specific shoulder exercise beats generic, low certainty) is cited there and not repeated
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: why a recovered shoulder keeps prep
  - "exercise/serratus-anterior-integration-019"  # within-warehouse: the serratus drills (practitioner source) that fill the scapular family
  - "exercise/emg-not-hypertrophy-proxy-013"  # within-warehouse: why EMG rankings do not pick the "best" lower-trap or cuff drill
  - "exercise/prep-on-fatigued-muscle-two-effects-026"  # within-warehouse: warm-up effects in general
  - "exercise/harm-route-boundary-031"  # within-warehouse: red flags stay with pain-triage
  - "framework:GRADE -- prevention effect rests on two cluster RCTs in handball (n=660, 627) with consistent direction; treatment effect on one RCT with a blinded assessor (n=102) plus low-certainty reviews. No RCT of shoulder prehab in lifters, none comparing sets, frequency or within-session placement for prevention, and the dose review found no dose shown to be needed. Lifter transport is indirect (different sport demands) -> downgraded."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
shoulder_prehab:
  - context: baseline
    rungs: [no-caution, mild, history-old]
    trigger: the session holds a lift that uses the shoulder
    slot: prep
    families: [external_rotation, scapular]
    exercises_min: 1
    exercises_max: 2
    sets_min: 2
    sets_max: 3
    reps_min: 8
    reps_max: 16
    per_week_target: 3
    load: light band or cable; stop well short of failure
    progression: reps first, then a stiffer band or the next cable plate, then a small weight
    rotate_weeks: 6
    pain_rule: pain during the drill -> lower the load; if it persists, route to pain-triage
    basis: Andersson 2017 OSTRC programme sheet; Asker 2022
    basis_grade: B
    transport_grade: C
  - context: history
    rungs: [history-recent, history-unknown]
    trigger: the session holds a lift that uses the shoulder
    slot: prep
    families: [external_rotation, scapular]
    exercises_min: 2
    exercises_max: 2
    sets_min: 2
    sets_max: 3
    reps_min: 8
    reps_max: 16
    per_week_target: 3
    load: light band or cable; stop well short of failure
    progression: reps first, then a stiffer band or the next cable plate, then a small weight
    rotate_weeks: 6
    pain_rule: pain during the drill -> lower the load; if it persists, route to pain-triage
    accessory: one resisted external-rotation or lower-trapezius exercise after the main lifts, 2-3 sets of 10-15, on 2 of the week's shoulder days, loaded and progressed like any accessory
    basis: OSTRC dose for the prep; Naunton 2020 (resisted and progressive) for the accessory
    basis_grade: D
    transport_grade: D
  - context: current-load-pain
    rungs: [current-load-pain]
    trigger: rotator-cuff-type shoulder pain in the user's words, no red flag, pain-triage has not flagged it
    slot: prep plus accessory
    families: [external_rotation, scapular]
    exercises_min: 2
    exercises_max: 3
    sets_min: 3
    sets_max: 3
    reps_min: 10
    reps_max: 15
    per_week_target: 3
    load: set by the 055 pain ceiling -- up to about 5/10 during, back to the usual level before the next session; some pain is allowed
    progression: add external load whenever a session stays inside the ceiling; non-progressed, unresisted drills are not the treatment
    rotate_weeks: 0
    pain_rule: 055 ceiling; breach -> lower the load next session; red-flag words -> pain-triage
    review_weeks: 12
    home_option: the tested rehab dose was 3 x 15 twice daily for 8 weeks then daily to week 12; offer as optional home work, never required
    basis: Holmgren 2012 (protocol); Naunton 2020; Malliaras 2020 (no dose shown to be needed)
    basis_grade: B
    transport_grade: C
  - context: closed
    rungs: [current-other, red-flag]
    trigger: present shoulder joint, ligament, instability or unknown-tissue pain, or any red flag
    slot: none
    families: []
    exercises_min: 0
    exercises_max: 0
    sets_min: 0
    sets_max: 0
    reps_min: 0
    reps_max: 0
    per_week_target: 0
    load: none prescribed
    progression: none
    rotate_weeks: 0
    pain_rule: pain-triage before any shoulder prescription
    basis: exercise/harm-route-boundary-031; exercise/caution-severity-ladder-056
    basis_grade: D
    transport_grade: D
shoulder_prehab_placement:
  - rule: low-dose prep before the first pressing or overhead lift
    basis_grade: B
    note: the prevention programmes were run inside the warm-up, before throwing
  - rule: work taken near failure or at high volume on the cuff goes after the main pressing / overhead lifts or on a day without them
    basis_grade: D
    note: cuff fatigue raised the humeral head in a lab study (Chopp 2010); no trial of placement in lifters
  - rule: both families every time, not scapular-only
    basis_grade: C
    note: the effective programmes combined cuff and scapular work; a scapula-only focus was no better than general exercise after 6 weeks (Bury 2016)
refraction_notes:
  - note: >
      THE PREVENTION DOSE IS SMALL AND IT IS IN THE WARM-UP. The two trials
      that cut shoulder problems in overhead athletes ran a short band and
      bodyweight programme three times a week as part of the warm-up, about
      3 sets of 8-16 per exercise, changing exercises every six weeks and
      progressing by reps, then band stiffness, then a small weight.
      Shoulder-problem prevalence fell from 23% to 17% in one; the injury
      rate fell by about half in the other. These were handball players, not
      lifters; the direction is carried, the size is not.
    grade: B
  - note: >
      FOR A PAINFUL CUFF, RESISTED AND PROGRESSED IS WHAT WORKED. In
      persistent subacromial pain, cuff plus scapular strengthening (3 x 15,
      load set so pain stayed at or under 5/10 and settled before the next
      session) beat unspecific exercise and cut the share choosing surgery
      from 63% to 20%. Across trials, progressive resisted exercise helped and
      unresisted, non-progressed drills did not, and caused more flares.
      "Only ever a pink dumbbell" is folklore; the load is set by the pain
      ceiling, not by a weight cap.
    grade: B
  - note: >
      MORE IS NOT SHOWN TO BE BETTER. The only review of higher vs lower
      dose in rotator-cuff tendinopathy found three small trials with
      conflicting, low to very low certainty results. The twice-daily rehab
      dose is the dose that was TESTED, not the dose shown to be NEEDED. The
      composer may offer it as optional home work but should not make daily
      cuff work a requirement of the plan.
    grade: C
  - note: >
      THE MECHANISM IS UNPROVEN, THE OUTCOME IS NOT. Weaker external
      rotation and scapular dyskinesis predict later shoulder problems in
      athletes (dyskinesis RR 1.43), and lifters with impingement have
      weaker external rotators and lower trapezius. But the programme that
      cut shoulder problems did not change external-rotation strength or
      internal-rotation range. Say "this routine lowered shoulder problems",
      never "this fixes your imbalance" or "your ratio is now safe".
    grade: C
  - note: >
      PLACEMENT. Light, sub-failure prep before pressing is the tested form.
      Anything taken close to failure on the cuff belongs after the main
      pressing and overhead lifts (or on a day without them): a fatigued
      cuff let the humeral head ride up in a lab study. No trial tests
      placement in lifters; this is a cautious default, not a finding.
    grade: D
  - note: >
      FOLKLORE WITH NO TRIAL BEHIND IT. A fixed pull-to-push set ratio
      (2:1, 3:1); "face pulls prevent shoulder injury" (no trial of face
      pulls as prevention); "the best lower-trap exercise" picked from EMG
      rankings (EMG amplitude is not an outcome, see 013); "fix the scapula
      first" (scapula-only focus was not better beyond 6 weeks). The composer
      should not justify any choice with these.
    grade: C
claim: >
  For a lifter with a shoulder caution, add a small amount of
  external-rotation plus scapular (lower-trapezius, serratus) work, sized by
  the 056 rung. No caution, mild, or old history: 1-2 light band or cable
  drills, 2-3 sets of 8-16, in the warm-up of sessions that load the
  shoulder, aiming at about three times a week, progressed by reps then
  resistance and rotated about every six weeks -- the shape of the handball
  programmes that cut shoulder problems (OR 0.72; HRR 0.44). Recent or
  undated history: both families in prep every shoulder session, plus one
  resisted external-rotation or lower-trap accessory after the main lifts
  twice a week. Present rotator-cuff-type pain without red flags: 2-3
  resisted cuff and scapular exercises of 3 x 10-15, load set by the 055
  pain ceiling and progressed, reviewed at 12 weeks, after the protocol
  that beat unspecific exercise and reduced surgery; the tested twice-daily
  home dose is optional because no dose has been shown to be needed.
  Present joint, instability or unknown pain, or red flags: no prehab
  prescription until triage. Keep fatiguing cuff work after pressing.
  Pull-push ratios, face-pull-as-prevention and EMG-ranked "best" drills
  have no outcome trial.
reasoning: >
  Prevention numbers come from the OSTRC programme sheet itself (read in
  full) and the Andersson 2017 cluster RCT, backed by Asker 2022's larger
  effect in adolescents; both are overhead-throwing populations, so the
  letter for lifters is dropped to C and the specific numbers are labelled
  as transported. Treatment numbers come from Holmgren 2012 at full text,
  whose load rule is the same pain-monitoring model 055 carries -- the
  shoulder trial used it as the load-setting method, it did not test it.
  Naunton 2020 supplies resisted-and-progressed over unresisted; Malliaras
  2020 supplies the absence of any shown dose-response, which is why the
  twice-daily rehab dose is optional and the in-gym dose is three times a
  week. Bury 2016 and Fredriksen 2020 keep the copy honest about mechanism.
  The placement rule rests on a lab mechanism (Chopp 2010) and stays at the
  practitioner floor. The history row is product judgement joining the
  prevention dose to a resisted accessory. The axis is hard with
  block_specifics because the rung (in particular whether present pain is
  cuff-type or a red flag) decides whether any dose is given at all.
---

# exercise/shoulder-prehab-dose-074 -- 어깨 주의가 있는 사람의 외회전·하부승모근·견갑 운동 양

**한 줄 그림:** 어깨 보강 운동은 많이 할수록 좋은 게 아니다. 워밍업에 가볍게 몇 세트, 주 3회 정도가
연구로 확인된 모양이다. 지금 회전근개 쪽이 아프면 통증 기준 안에서 무게를 올려 가며 한다.

## Dose by rung (engine-readable copy of `shoulder_prehab`)

| Context (056 rungs) | Slot | Drills | Sets x reps | Per week | Load | Basis |
|---|---|---|---|---|---|---|
| baseline (no caution, mild, history-old) | prep | 1-2 (ER + scapular) | 2-3 x 8-16 | ~3 | light band/cable, sub-failure, rotate every 6 wk | OSTRC programme (handball) |
| history (recent, unknown) | prep + 1 accessory | 2 in prep; 1 after main lifts | prep 2-3 x 8-16; accessory 2-3 x 10-15 | prep ~3; accessory 2 | accessory loaded and progressed | OSTRC + Naunton 2020; product judgement |
| current-load-pain (cuff-type, no red flag) | prep + accessory | 2-3 (ER + scapular) | 3 x 10-15 | ~3 (home daily optional) | 055 pain ceiling, progress load | Holmgren 2012 protocol |
| closed (current-other, red-flag) | none | -- | -- | -- | -- | pain-triage (031) |

Placement: light prep before the first pressing or overhead lift; anything near
failure on the cuff after the main pressing lifts or on another day; always cuff
plus scapular, never scapular-only.

## Evidence vs folklore

| Claim | State |
|---|---|
| A short shoulder programme in the warm-up, 3x/week, lowers shoulder problems | Two cluster RCTs, overhead athletes |
| Resisted, progressed cuff work helps cuff-type pain; unresisted does not | RCT + low-certainty review |
| Twice-daily cuff work is needed | Tested in one rehab trial; no dose shown to be needed |
| Cuff work must stay very light forever | Not supported; load is set by the pain ceiling |
| The routine works by fixing ER strength or IR range | Not shown; the programme changed neither |
| A fixed pull:push ratio protects the shoulder | No trial |
| Face pulls prevent shoulder injury | No trial of face pulls as prevention |
| EMG ranking picks the best drill | EMG amplitude is not an outcome (013) |

## 한국어 요약 (답변용)

- 어깨에 주의가 없거나, 가끔 뻣뻣한 정도거나, 예전에 다쳤다가 나은 경우: 어깨를 쓰는 날 워밍업에
  밴드·케이블 외회전과 견갑(하부승모근·전거근) 운동을 1~2개, 2~3세트 8~16회 가볍게 넣는다. 주 3회
  정도면 된다. 횟수부터 늘리고, 그다음 밴드를 더 센 걸로, 그다음 작은 무게로 올린다. 6주마다 동작을
  바꿔 준다. 핸드볼 선수 연구에서 이런 루틴이 어깨 문제를 줄였다. 헬스 하는 사람 대상 연구는 아니라서
  방향만 가져오고 효과 크기는 그대로 옮기지 않는다.
- 최근(12개월 안) 다쳤거나 언제 다쳤는지 모르면: 워밍업에 외회전과 견갑 운동을 둘 다 넣고, 메인
  운동이 끝난 뒤 저항을 건 외회전이나 하부승모근 운동 하나를 2~3세트 10~15회, 주 2회 더한다. 이 조합은
  연구 결과를 이어 붙인 제품 규칙이다.
- 지금 회전근개 쪽이 아프고 위험 신호가 없으면: 외회전과 견갑 운동 2~3개를 3세트 10~15회 한다.
  무게는 통증 기준(운동 중 10점 중 5점까지, 다음 운동 전에 평소 수준으로 돌아옴)으로 정하고, 기준 안에
  있으면 조금씩 올린다. 저항 없이 같은 동작만 반복하는 건 효과가 없었고 오히려 더 자주 아팠다. 12주쯤
  지나면 다시 본다. 연구에서는 하루 두 번 했지만, 더 많이 한다고 낫다는 근거는 없으니 집에서 하는 건
  선택으로 둔다.
- 지금 아픈 곳이 관절이거나, 빠지는 느낌이 있거나, 어디가 아픈지 모르거나, 위험 신호가 있으면: 보강
  운동을 처방하지 않고 먼저 통증 확인으로 보낸다.
- 순서: 가벼운 준비 운동은 프레스·머리 위 운동 전에 한다. 실패 지점까지 가는 회전근개 운동은 메인
  프레스가 끝난 뒤나 다른 날에 한다. 회전근개가 지치면 위팔뼈 머리가 위로 뜬다는 실험 결과에서 나온
  조심스러운 기본값이고, 헬스 하는 사람으로 확인된 건 아니다.
- 이렇게 말하지 않는다: "당기기:밀기 2:1이어야 안전하다", "페이스 풀이 부상을 막는다", "근전도로 보면
  이 동작이 최고다", "불균형을 고쳤으니 이제 안전하다". 모두 결과로 확인된 적이 없다. 예방 루틴은
  외회전 근력이나 가동범위를 바꾸지 않았는데도 어깨 문제를 줄였다.
