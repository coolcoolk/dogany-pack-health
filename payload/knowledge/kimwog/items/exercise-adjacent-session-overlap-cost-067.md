---
# Adjacent-recovery sprint 2026-10-06 (dispatch kw-ex-adjacent-recovery). What
# overlap between BACK-TO-BACK sessions actually costs, split three ways:
# next-day performance (measured), long-term adaptation (measured, null when
# weekly volume is equated) and injury (not measured anywhere found). Extends
# exercise/recovery-kinetics-session-spacing-025 (which holds the
# per-muscle-group-clock rejection) from "what sets recovery" to "what a
# composer should charge for a consecutive-day overlap", by overlap TYPE:
# same primary pattern, secondary mover only, squat <-> hinge (axial / hip
# extensor), grip, and upper vs lower.
#
# adjacent_overlap is structured data for the split / program composer (field
# guide: docs/kimwog-adjacent-overlap-fields.md). Values are DIRECTIONS and
# ORDERINGS (cost_performance: high / moderate / low / none-measured /
# see-056; cost_when qualifies it). No penalty number
# here is a measurement; the composer's own weights stay product constants.
id: exercise/adjacent-session-overlap-cost-067
domain: exercise
grade: B (consecutive-day exposure costs no long-term strength or size when weekly volume is equated); C (a same-pattern session to failure leaves next-day performance down, work short of failure recovers within hours; no fixed upper-faster-than-lower or deadlift-slower-than-squat order); D (squat-hinge, grip and secondary-mover overlap rules; any injury cost of back-to-back overlap)
lane: "@performance-lit"
locale: universal
as_of: 2016-2026
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/32594858/"  # Goulart KNO et al. 2021, Eur J Sport Sci 21(7):935-943 -- 14 resistance-trained men, 5 x 8-10RM squat + leg press to concentric failure, the SAME session repeated after 24, 48 or 72 h (randomised): session volume load fell at 24 h (ES -0.90), first-set volume load still down at 48 h (ES -0.63), CMJ and MVIC up at 72 h; authors: at least 48 h after lower-limb work to failure
  - "https://link.springer.com/article/10.1007/s00421-017-3725-7"  # Morán-Navarro R et al. 2017, Eur J Appl Physiol 117(12):2387-2399 -- 10 resistance-trained men, bench press + full squat: 3x10(10) to failure vs volume-matched 6x5(10) vs 3x5(10); after the half-effort protocols V1-load velocity and CMJ were back by 6 h, after failure velocity not back until 48 h (V1 load, 72 h) and CMJ 72 h; bench velocity was still below basal at 48 h, squat at 24 h (read at full text)
  - "https://pubmed.ncbi.nlm.nih.gov/30036284/"  # Pareja-Blanco F et al. 2020 (epub 2018), J Strength Cond Res 34(10):2867-2876 -- 10 protocols bench + squat; to failure with many reps: mechanical function down to 48 h, greater CK and hormonal response
  - "https://pubmed.ncbi.nlm.nih.gov/30779596/"  # Belcher DJ et al. 2019, Appl Physiol Nutr Metab 44:1033-1042 -- 12 well-trained men, 4 sets to failure at 80% 1RM on squat, bench, deadlift in separate weeks; no between-lift differences in swelling, ROM, soreness, velocity, CK, LDH, cfDNA; squat velocity down to 72 h (-8.6%), deadlift velocity did not fall
  - "https://academic.oup.com/bmb/article/158/1/ldag013/8658890"  # Gervasi M et al. 2026, Br Med Bull 158(1) ldag013 -- 54 resistance-trained adults, 3 x 12 at 70% 1RM back squat vs deadlift vs control: squat larger, earlier CMJ impairment; deadlift smaller but more persistent braking-RFD / RSImod loss at 24 h; abstract read
  - "https://pubmed.ncbi.nlm.nih.gov/28447186/"  # Bartolomei S et al. 2017, Eur J Appl Physiol 117(7):1287-1298 -- 12 trained men, 8x10 vs 8x3 lower body: isometric leg extension still down at 72 h after the high-volume protocol, not after high intensity
  - "https://pubmed.ncbi.nlm.nih.gov/27093538/"  # Raeder C et al. 2016, J Strength Cond Res 30(12):3412-3427 -- 23 athletes, 6-day intensified (overreaching) strength microcycle: 1RM est -7.5%, CMJ -6.4%; 1RM and CMJ back after 3 rest days, RSI not
  - "https://paulogentil.com/pdf/Training%20Volume%2C%20Not%20Frequency%2C%20Indicative%20of%20Maximal%20Strength%20Adaptations%20to%20Resistance%20Training.pdf"  # Colquhoun RJ et al. 2018, J Strength Cond Res 32(5):1207-1213 -- 28 trained men, 3x vs 6x per week, volume and intensity equated (6x did half the per-session volume, squat and bench Mon-Sat): squat +16.8 vs +16.7 kg, bench +7.8 vs +8.8, deadlift +19 vs +21, no difference (read at full text)
  - "https://pubmed.ncbi.nlm.nih.gov/30363041/"  # Saric J et al. 2019, J Strength Cond Res 33(7S):S122-S129 -- 27 trained men, 3x vs 6x per week volume-equated, 6 weeks: similar strength and muscle thickness
  - "https://vuir.vu.edu.au/37695/"  # Grgic J et al. 2018, Sports Med -- frequency meta-analysis: under volume-equated conditions no significant effect of frequency on strength; abstract-level only
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC11057610/"  # Sousa CA, Zourdos MC, Storey AG, Helms ER 2024, J Hum Kinet -- narrative review of recovery in microcycle construction; asserts lower body 48-72 h vs upper body 24 h or less (the contested point below); its injury sentence cites general muscle-damage reviews, no lifter injury data
  - "https://rke.abertay.ac.uk/en/publications/ergogenic-effects-of-lifting-straps-on-movement-velocity-grip-str/"  # Jukic I et al. 2021, Physiol Behav -- 16 men, deadlifts with vs without straps: less grip fatigue and faster grip recovery with straps; within-session only, no next-day measure
  - "https://pubmed.ncbi.nlm.nih.gov/27328853/"  # Keogh JW, Winwood PW 2017, Sports Med 47(3):479-501 -- systematic review, weight-training sports: ~2-4 injuries per 1000 h in most, lower back / shoulder / knee commonest; no training-frequency or session-spacing risk factor analysed
  - "exercise/recovery-kinetics-session-spacing-025"  # within-warehouse: what sets recovery (failure, volume, complexity), the per-muscle-group-clock rejection
  - "exercise/volume-doseresponse-007"  # within-warehouse: weekly volume, the variable frequency studies hold constant
  - "exercise/doms-timeline-mechanism-023"  # within-warehouse: soreness is not the overlap signal
  - "exercise/autoregulation-vs-percentage-prescription-030"  # within-warehouse: first-set performance as the day's readiness read
  - "exercise/caution-severity-ladder-056"  # within-warehouse: site-level spacing for a caution site overrides this row
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: symptomatic tendon spacing (one day between heaviest site days)
  - "framework:GRADE -- frequency (B): two volume-equated RCTs in trained men (6 weeks each) plus a meta-analysis read at abstract level. Next-day performance (C): small within-subject trials (n=10-14, trained men), consistent direction on failure vs non-failure; only Goulart measured the repeated session itself. Overlap-type rules (D): no trial measures next-day cross-effects between squat and hinge, grip carry-over, or secondary-mover overlap; no study of any kind links back-to-back overlap to injury in lifters. Population: young trained men throughout."
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
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: hedge
adjacent_overlap:
  - overlap: same-primary-to-failure
    words: day 2 loads a muscle as PRIMARY mover that day 1 loaded as primary, and day 1's sets went to or within about 1 rep of failure, or many reps per set
    cost_performance: high
    cost_adaptation: none when weekly volume is equated
    cost_injury: not measured
    expect: next-day session volume down; first-set performance may stay down to 48 h
    composer: penalise; prefer >= 48 h before the same primary pattern
    basis: Goulart 2021; Morán-Navarro 2017; Pareja-Blanco 2020
    basis_grade: C
  - overlap: same-primary-short-of-failure
    words: same primary mover on consecutive days, sets stopped well short of failure (about half the possible reps, or 3+ in reserve)
    cost_performance: low
    cost_adaptation: none when weekly volume is equated
    cost_injury: not measured
    expect: velocity and jump back within about 6 h in the trial; daily squat and bench at half per-session volume matched 3x/week gains
    composer: allow; charge less than the to-failure case
    basis: Morán-Navarro 2017; Colquhoun 2018; Saric 2019
    basis_grade: C
  - overlap: secondary-only
    words: day 2 loads the muscle only as a secondary mover (triceps under presses after direct triceps; glutes under a squat after hinge day; biceps under pulls)
    cost_performance: none-measured
    cost_adaptation: none-measured
    cost_injury: not measured
    expect: no trial isolates it
    composer: record, do not score (matches current structure.pattern_roles rule)
    basis: absence of evidence
    basis_grade: D
  - overlap: squat-hinge
    words: a heavy squat day and a heavy hinge day (deadlift, RDL) on consecutive days, either order; both load hip extensors and the trunk extensors axially
    cost_performance: moderate
    cost_when: both days heavy or near failure; low when either day is light
    cost_adaptation: none-measured
    cost_injury: not measured
    expect: deadlift recovery is not slower than squat recovery (matched trial); squat hits jump output harder and sooner, deadlift leaves a smaller, longer braking-RFD dip
    composer: treat as a lower-body heavy adjacency even though pattern_roles names different primaries; no extra deadlift-needs-longer penalty
    basis: Belcher 2019; Gervasi 2026; no next-day cross-exercise trial read
    basis_grade: D
  - overlap: grip
    words: heavy pulling (deadlift, rows, pull-ups, carries) on consecutive days
    cost_performance: none-measured
    cost_when: grip limits pulling sets within a session; no next-day data
    cost_adaptation: none-measured
    cost_injury: not measured
    expect: straps reduce grip fatigue and speed grip recovery within the session
    composer: do not score; if grip limits day-2 pulling, the lever is straps, not a moved day
    basis: Jukic 2021
    basis_grade: D
  - overlap: upper-vs-lower
    words: any rule that a lower-body day needs longer than an upper-body day (or the reverse)
    cost_performance: none-measured
    cost_when: no fixed order between body halves
    cost_adaptation: none-measured
    cost_injury: not measured
    expect: matched squat / bench / deadlift showed no between-lift difference; after failure bench velocity recovered later than squat in one trial; a 2024 review states the opposite
    composer: do not use body half as a recovery clock; use effort and pattern
    basis: Belcher 2019; Morán-Navarro 2017; Sousa 2024 (contrary)
    basis_grade: C
  - overlap: caution-site
    words: a caution site (056 rung history-recent, history-unknown or current-load-pain) loaded on consecutive days
    cost_performance: see-056
    cost_adaptation: see-056
    cost_injury: not measured for lifters; site spacing comes from 055 / 056
    expect: the 056 spread rule applies first
    composer: 056 overrides this row for that site (no consecutive heavy days at the site)
    basis: exercise/caution-severity-ladder-056; exercise/tendon-fascia-load-management-055
    basis_grade: D
refraction_notes:
  - note: >
      THREE COSTS, NOT ONE. A back-to-back overlap has a next-day performance
      cost (measured: real after work to failure, small after work stopped
      short), a long-term adaptation cost (measured: none when weekly volume
      is the same -- six sessions a week matched three in trained men), and
      an injury cost (not measured in any lifter study found). Speak each
      separately; never let the measured performance cost stand in for an
      injury warning.
    grade: B
  - note: >
      EFFORT DECIDES THE PRICE. In the one trial that repeated the session
      itself, squat plus leg press to failure lost volume load when repeated
      24 h later and first-set load was still down at 48 h. Volume-matched
      work at about half the possible reps per set had velocity and jump
      back within about 6 h. So the same day-1 / day-2 muscle overlap is
      expensive after failure training and cheap after submaximal training.
    grade: C
  - note: >
      DEADLIFT DOES NOT NEED LONGER. The common belief that the deadlift
      needs more recovery than the squat failed a matched test in
      well-trained men (four sets to failure at 80%): no between-lift
      differences, and deadlift bar speed did not drop. Squat and deadlift
      fatigue do differ in shape (squat: larger, sooner; deadlift: smaller,
      longer-lasting braking-RFD loss), so a heavy squat day next to a heavy
      hinge day is a real lower-body adjacency, but not a special axial
      penalty.
    grade: C
  - note: >
      NO AXIAL-LOAD OR SPINE RECOVERY CLOCK WAS FOUND. No study located
      measures trunk-extensor or spinal recovery across 24-48 h after squats
      or deadlifts, or next-day hinge performance after a squat day (one
      university thesis appears to, and was not readable). The squat-hinge
      rule is a practitioner rule built from shared hip-extensor work.
    grade: D
  - note: >
      UPPER VERSUS LOWER IS CONTESTED. A 2024 review states the lower body
      needs 48-72 h and the upper body 24 h or less. The matched comparison
      found no between-lift difference, and after failure training bench
      velocity was still down at 48 h while squat velocity was back at 48 h
      in another trial. Do not schedule from body half.
    grade: C
  - note: >
      GRIP IS A SESSION LIMITER, NOT A SCHEDULE RULE. Grip fatigue limits
      pulling sets within a session, and straps reduce it. No next-day grip
      carry-over data were found, so the composer should not move days for
      grip.
    grade: D
  - note: >
      POPULATION. Every trial is young trained (mostly male) lifters over
      days to six weeks. Novices, older adults and women are extrapolation.
      Over a week of daily overreaching, 1RM and jump came back after three
      rest days, but jump reactivity did not. Whole-week fatigue is a
      different question from day-to-day overlap and is not settled here.
    grade: C
claim: >
  What overlap between back-to-back sessions costs depends on how hard the
  first session was, not on which muscle or body half was trained. Repeating
  a lower-body session to failure 24 h later lowers that session's volume, and
  first-set performance can stay down to 48 h. Work stopped well short of
  failure recovers within hours. Over six weeks, spreading the same weekly
  volume across six sessions, including the same lifts on consecutive days,
  gave the same strength and size gains as three sessions. Matched testing
  does not support the beliefs that the deadlift needs longer than the squat or
  that the upper body recovers faster than the lower body; one 2024 review
  states the second, so it is marked contested. A heavy squat day next to a
  heavy hinge day is still a lower-body adjacency, because both load the hip
  extensors, though no next-day cross-exercise trial was read. Grip and
  secondary-mover overlap have no measured next-day cost. No lifter study
  links back-to-back overlap to injury. For a composer, overlap should be
  charged by effort (to failure versus short of failure) and by pattern (same
  primary pattern, squat to hinge), with a caution site's spacing (056) taking
  precedence.
reasoning: >
  Goulart 2021 is the only design found that measures the second session
  itself at 24, 48 and 72 h. Its protocol was taken to failure, so it shows the
  high end of the cost. Morán-Navarro 2017 adds the effort contrast at matched
  volume in trained men. Pareja-Blanco 2020 repeats that contrast across ten
  set configurations. Item 025 attributed both to one paper; the re-audit of 025
  corrects this. Belcher 2019 is the only matched comparison of lifts. Gervasi
  2026 shows that squat and deadlift fatigue differ in shape. Colquhoun 2018 and
  Saric 2019 isolate frequency at equal weekly volume, and Colquhoun's 6x group
  squatted and benched on consecutive days. They are the strongest evidence that
  adjacency itself carries no adaptation cost; both ran six weeks in trained
  men. Keogh & Winwood 2017 gives low injury rates in weight-training sports and
  no spacing or frequency risk factor. Sousa 2024 states injury risk only
  through general muscle-damage reviews. The injury column is therefore "not
  measured" throughout, and the caution-site row defers to 056. Contested flag:
  the upper-versus-lower and deadlift-needs-longer conventions are widespread in
  coaching and in one 2024 review, and the matched data do not support them.
---

# exercise/adjacent-session-overlap-cost-067 -- 연달아 하는 날, 겹치면 무엇을 잃나

**한 줄 그림:** 이틀 연속 같은 근육을 쓰는 비용은 전날 얼마나 한계까지 갔느냐로 정해진다. 근육 부위나
상체·하체로 정해지지 않는다. 장기 성장 손해는 측정되지 않았고, 부상과의 관련은 연구된 적이 없다.

## The overlap table (engine-readable: `adjacent_overlap`)

| Overlap on consecutive days | Next-day performance | Long-term gains | Injury | Composer |
|---|---|---|---|---|
| same primary mover, day 1 to failure | high (volume down at 24 h, first set to 48 h) | none if weekly volume equal | not measured | penalise; prefer 48 h |
| same primary mover, day 1 well short of failure | low (back within ~6 h in trial) | none if weekly volume equal | not measured | allow, charge less |
| secondary mover only | none measured | none measured | not measured | record, don't score |
| heavy squat day next to heavy hinge day | moderate if both heavy / near failure | none measured | not measured | lower-body adjacency; no extra deadlift penalty |
| heavy pulling (grip) | none measured next day | none measured | not measured | don't move days; straps |
| upper vs lower body | not a fixed order (contested) | -- | -- | don't use body half as a clock |
| caution site (056) | -- | -- | from 055/056 | 056 overrides |

The cost levels (high / moderate / low) are orderings. They are not
measurements, and the composer's weights stay product constants.

## 한국어 요약 (답변용)

- 이틀 연속 같은 근육을 주동근으로 쓸 때의 비용은 전날 강도에 달렸다. 실패 지점까지 간 하체 운동을
  24시간 뒤 똑같이 반복하면 그날 총 볼륨이 줄었다. 첫 세트 기록은 48시간까지 떨어져 있었다. 가능한 횟수의
  절반쯤에서 멈춘 운동은 몇 시간 만에 회복됐다.
- 주간 총량이 같으면 주 6회로 나눠 연달아 해도 주 3회와 근력·근육 증가가 같았다. 6주 동안 훈련된
  남성을 대상으로 한 연구들이고, 스쿼트와 벤치를 월요일부터 토요일까지 매일 한 그룹도 포함됐다.
- '데드리프트는 스쿼트보다 회복이 오래 걸린다'는 말은 같은 조건 비교에서 확인되지 않았다. 다만 스쿼트
  날과 힌지(데드리프트·RDL) 날을 붙이면 둘 다 엉덩이 신전근을 쓰므로 하체를 연달아 쓰는 날로 본다.
- '상체가 하체보다 빨리 회복된다'는 말은 근거가 엇갈린다. 2024년 리뷰는 그렇다고 하지만, 같은 조건
  비교에서는 차이가 없었다. 실패 지점까지 간 경우 벤치 속도가 스쿼트보다 늦게 돌아온 연구도 있다.
  상체·하체로 회복 시간을 정하지 않는다.
- 보조로만 쓰이는 근육(프레스할 때 삼두 등)과 악력이 겹치는 것은 다음 날 손해가 측정된 적이 없다.
  악력이 당기기 세트를 막으면 날짜를 옮기기보다 스트랩을 쓴다.
- 연달아 겹치는 날이 부상을 늘린다는 연구는 찾지 못했다. 부상 이력이 있거나 지금 아픈 부위는 주의
  단계(056)의 간격 규칙을 먼저 따른다.
