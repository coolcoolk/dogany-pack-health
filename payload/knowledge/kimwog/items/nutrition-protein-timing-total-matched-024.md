---
# Authored 2026-10-07 (dispatch kw-nu-cut-protein-lifter). The timing claims a
# lifter meets around a training day -- pre vs post, "around the session",
# casein before bed -- read for one question: once the DAILY TOTAL is matched,
# is anything left? The window WIDTH claim stays with
# exercise/protein-anabolic-window-002 (single ownership); this item owns the
# total-matched reading and the Korean day shape the diet card actually sees
# (breakfast skipped, protein loaded at dinner or late). Primaries read
# 2026-10-07.
#
# timing_rules is structured data for diet-status (protein.py nudge, last-call
# line, card copy). No program code was changed by this item.
# Renumbered at the v37 merge (provisional 071 -> 024).
id: nutrition/protein-timing-total-matched-024
domain: nutrition
lane: "@obs-inferential"
grade: B
locale: universal
as_of: 2013-2026
contested: no
sources:
  - "https://doi.org/10.1186/1550-2783-10-53"  # Schoenfeld BJ, Aragon AA, Krieger JW. J Int Soc Sports Nutr 2013;10(1):53. PMID 24299050, PMC3879660 -- meta-regression, 23 hypertrophy studies (525 subjects) and 20 strength studies (478); a small pooled timing effect on hypertrophy vanished once covariates were controlled; total protein was the strongest predictor
  - "https://doi.org/10.7717/peerj.2825"  # Schoenfeld BJ, Aragon AA, Wilborn C, Urbina SL, Hayward SE, Krieger J. PeerJ 2017;5:e2825. PMID 28070459, PMC5214805 -- n=21 resistance-trained men, 10 weeks, 25 g protein immediately pre vs immediately post: no difference on any measure
  - "https://doi.org/10.3945/jn.114.208371"  # Snijders T, Res PT, Smeets JS, et al. J Nutr 2015;145(6):1178-1184. PMID 25926415, NCT02222415 -- n=44 young men, 12 weeks; 27.5 g protein before sleep vs NON-CALORIC placebo: more strength and quadriceps CSA; daily totals NOT matched
  - "https://doi.org/10.1186/s12970-018-0228-9"  # Joy JM, Vogel RM, Shane Broughton K, et al. J Int Soc Sports Nutr 2018;15(1):24. PMID 29764464, PMC5952515 -- n=13, 10 weeks, 35 g casein daytime vs before bed on isocaloric 1.8 g/kg diets: no between-group difference (preliminary, small)
  - "https://doi.org/10.1016/j.jsams.2020.07.016"  # Reis CEG, Loureiro LMR, Roschel H, da Costa THM. J Sci Med Sport 2021;24(2):177-182. PMID 32811763 -- systematic review, 9 studies: possible benefit in young men, conclusions limited by uneven protein intakes between groups
  - "https://www.segye.com/newsView/20260609500948"  # Segye Ilbo 2026-06-09 reporting KDCA KNHANES 2024: breakfast skipping 35.3% (age 1+), 62.1% at age 19-29. SECONDARY report of the national statistic; the KDCA table itself was not retrieved
  - "https://doi.org/10.4082/kjfm.2018.39.2.130"  # Park HA. Korean J Fam Med 2018;39(2):130-134. PMID 29629047, PMC5876049 -- KNHANES 2013-2014, adults 60+: protein spread fairly evenly across meals but low in absolute amount per meal; only older adults
  - "source:exercise/protein-anabolic-window-002 -- owns the claim that the post-exercise window is wide (hours, not minutes)"
  - "source:nutrition/protein-distribution-thin-009 -- the even split is not an established lever"
  - "source:nutrition/protein-per-meal-ceiling-008 -- a large late meal is not wasted protein"
  - "source:nutrition/protein-deficit-trained-lifter-023 -- the daily target this item says to prioritise"
  - "source:nutrition/kr-protein-exchange-counting-021 -- per-meal splitting kept on a logging-tractability ground only"
  - "source:nutrition/unlogged-day-not-zero-019 -- a blank breakfast row is unknown until the user says it was skipped"
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
    - key: chronotype
      type: categorical
      role: soft
      unknown_policy: hedge
timing_rules:
  - rule: total-first
    when: the day's protein is short and a timing question comes up
    effect: speak the remaining daily total first; timing is never the reason a day is short or met
    basis: Schoenfeld 2013 meta-regression (timing effect gone once total protein is in the model)
    basis_grade: B
  - rule: pre-or-post-equal
    when: user asks whether protein goes before or after training
    effect: either; whichever meal is convenient; no minute window is enforced or spoken
    basis: Schoenfeld 2017 (n=21 trained, matched dose); exercise/protein-anabolic-window-002
    basis_grade: B
  - rule: bedtime-slot-is-a-fill-slot
    when: the last-call line proposes protein before bed
    effect: justify it as a convenient slot to reach the daily total, never as an overnight-synthesis bonus on top of a met day
    basis: Snijders 2015 positive but totals unmatched; Joy 2018 matched and null; Reis 2021 caveat
    basis_grade: C
  - rule: skipped-breakfast-not-a-defect
    when: no breakfast protein, or the user says they skip breakfast
    effect: do not flag the skip or push a breakfast; plan the total across the meals the user actually eats
    basis: nutrition/protein-distribution-thin-009; KNHANES 2024 skip rate 62.1% at age 19-29 (secondary report)
    basis_grade: C
  - rule: blank-is-unknown
    when: a breakfast row is empty and the user has not said they skipped it
    effect: unknown, not zero; skipped only after the user says so
    basis: nutrition/unlogged-day-not-zero-019
    basis_grade: C
  - rule: late-heavy-protein-allowed
    when: most of the day's protein lands at dinner or a late meal (회식, 야식)
    effect: count it in full toward the total; no "too much in one meal" warning; any timing margin before bed stays a comfort and reflux rule, not a protein rule
    basis: nutrition/protein-per-meal-ceiling-008; nutrition/protein-distribution-thin-009
    basis_grade: B
refraction_notes:
  - note: >
      THE BEDTIME RESULT IS AN EXTRA-PROTEIN RESULT. Snijders 2015 compared a
      27.5 g pre-sleep drink with a non-caloric placebo, so the protein group
      simply ate more protein each day. When Joy 2018 moved the same 35 g of
      casein between day and bedtime on matched 1.8 g/kg diets, nothing
      separated (n=13, preliminary). Read pre-sleep protein as one more slot
      in which to reach the total.
    grade: C
  - note: >
      NO TIMING TRIAL IN A DEFICIT. None of the timing trials located ran in a
      calorie deficit in trained lifters. That timing matters more in a cut
      is a plausible theory and is not tested; it is not spoken as a finding.
    grade: D
  - note: >
      KOREAN DAY SHAPE. In the 2024 national survey as reported, about six in
      ten Koreans aged 19-29 skip breakfast. The one KNHANES study of protein
      across meals located covers only adults over 60 and found an even but
      low spread; no per-meal protein profile of young Korean lifters was
      found. A dinner-heavy day is treated as normal, not as an error.
    grade: C
claim: >
  When the daily protein total is matched, the timing of protein around
  training does not measurably change strength or muscle gain. A
  meta-regression of 23 hypertrophy and 20 strength studies found the small
  pooled timing effect disappeared once total protein intake was accounted for,
  and total intake was the strongest predictor. In resistance-trained men, 25 g
  immediately before training and 25 g immediately after gave the same 10-week
  results. Protein before sleep improved gains against a non-caloric placebo,
  but in that trial the protein group also ate more protein per day; when the
  same casein dose was moved between daytime and bedtime with totals matched,
  no difference appeared. For the diet card this means: the remaining daily
  total comes first, the session and bedtime are convenient slots to reach it,
  and a skipped breakfast or a dinner-heavy Korean day is not a defect.
reasoning: >
  The direction is supported by a meta-regression and by an RCT in the target
  population with matched doses, which puts the core claim at the RCT-level
  band; it is not contested in print in its total-matched form. The pre-sleep
  part is held lower because its positive trial did not match totals and its
  matched trial has 13 people. The Korean breakfast figure is a secondary press
  report of the KDCA survey, and the only Korean per-meal protein study located
  is in older adults, so the Korean rule rests on the distribution evidence
  (009, 008) rather than on a Korean outcome study. Nothing here sets a
  minute window; the width of the window belongs to the exercise-owned item.
---

# nutrition/protein-timing-total-matched-024

Once the day's protein total is the same, when it is eaten around training
makes no measurable difference to strength or muscle over weeks. The pooled
timing studies show a small effect only until total protein is accounted for,
and then it disappears. Trained men who took the same 25 g just before or
just after lifting ended ten weeks in the same place.

The bedtime-protein finding is the one people cite as a timing effect, and it
is really a quantity effect. The trial that found bigger gains gave the
protein group an extra drink and the control group a calorie-free placebo. The
small trial that moved the same casein between daytime and bedtime, with daily
protein held equal, found no difference.

Applied to a Korean day: most people in their twenties skip breakfast, and
protein tends to arrive at lunch, dinner or a late meal. None of that needs
correcting. The diet card's job is to keep the daily total in view and to use
whatever meals are left, including a shake before bed, as places to reach it.

## Engine rules (diet card)

| Rule | When | Effect | Basis band |
|---|---|---|---|
| total-first | day short, timing asked | speak remaining total first | RCT-level |
| pre-or-post-equal | before vs after training | either; no minute window | RCT-level |
| bedtime-slot-is-a-fill-slot | last-call protein line | a slot to reach the total, not a bonus | observational |
| skipped-breakfast-not-a-defect | no breakfast | no flag, plan across eaten meals | observational |
| blank-is-unknown | empty breakfast row | unknown until the user says skipped | operating rule |
| late-heavy-protein-allowed | dinner / 회식 / 야식 heavy | count in full, no per-meal warning | RCT-level reading |

## 한국어 요약 (답변용)

- 하루 단백질 총량이 같다면, 운동 전후 언제 먹느냐로 근육·근력 결과가 달라진다는 근거는 없다.
  부족한 날에는 남은 총량부터 말한다.
- 운동 직전 25 g과 직후 25 g은 훈련자 10주 시험에서 결과가 같았다. "운동 후 30분 안에"는
  지키라고 말하지 않는다.
- 자기 전 단백질이 효과가 있었다는 연구는 대조군이 열량 없는 위약이라 사실상 "더 먹은" 효과다.
  총량을 맞추고 시간만 바꾼 작은 시험에서는 차이가 없었다. 자기 전은 총량을 채우는 편한 자리일 뿐이다.
- 20대의 약 60%가 아침을 거른다(2024 국민건강영양조사 보도). 아침을 안 먹은 것을 문제로 짚지 않고,
  실제로 먹는 끼니로 총량을 나눈다. 아침 칸이 비어 있으면 사용자가 거른 것이라고 말하기 전까지는
  '모름'이다.
- 저녁·회식·야식에 단백질이 몰려도 전부 총량에 넣는다. "한 끼에 너무 많다"는 경고는 하지 않는다.
- 감량 중에 타이밍이 더 중요하다는 말은 시험된 적이 없다. 사실처럼 말하지 않는다.
