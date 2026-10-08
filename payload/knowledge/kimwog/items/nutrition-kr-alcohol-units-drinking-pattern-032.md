---
# Alcohol-and-training sprint 2026-10-07 (dispatch kw-nu-alcohol-training-cut).
# KR-LOCALE companion to 031. Closes two open wants from the leisure section
# of GAPS.md: (1) every alcohol threshold in this warehouse was in grams,
# which is not how anyone in Korea counts, and (2) no Korean base rate for
# ordinary or high-risk drinking was carried. This row converts grams to
# 잔 / 병 / 캔 and states what the official survey measures, so a retro line
# can say "소주 1병쯤" instead of "47 g".
#
# drink_units and kr_thresholds are structured data. ethanol_g is arithmetic
# (volume x ABV x 0.789, the density of ethanol); the label ABV of the actual
# product overrides abv_default. kr_thresholds are a survey definition and a
# practitioner guideline, NOT personal limits the engine may prescribe.
id: nutrition/kr-alcohol-units-drinking-pattern-032
domain: nutrition
lane: "@obs-inferential"
grade: "A (jurisdictional-standard: the KDCA survey definitions and 2025 rates as published); A (unit arithmetic, mL x ABV x 0.789); D (the Korean low-risk-drinking thresholds, a Korean family-medicine guideline read in its 2024 restatement, original not read); D (the ~50 mL soju glass and 7-glasses-per-bottle convention)"
locale: KR
as_of: 2019-2026
contested: no
sources:
  - "https://kdca.go.kr/bbs/kdca/42/308588/download.do"  # 질병관리청 보도자료 2026-07-27, '최근 10년간 고위험음주 남성 전 연령에서 감소, 여성은 30대 이상 모든 연령에서 증가' -- 2025 지역사회건강조사, ~230,000 adults 19+, face-to-face interview. Definitions: 고위험음주율 = men 7잔+ (or beer 5 cans) / women 5잔+ (or beer 3 cans) per occasion, 2+ times a week, past year; 월간폭음률 = same amount 1+ times a month; 월간음주율 = drank 1+ times a month. 2025: 57.1% / 33.7% / 12.0%; 59% of monthly drinkers binge and 35.6% of those binge 2+/week; men 30s-50s about 1 in 2 binge, men 40s-50s more than 1 in 5 high-risk; women 20s-40s highest among women; over 2016-2025 high-risk drinking fell in men of every age and rose in women 30+. Korea 5th of 27 comparable OECD countries for monthly binge (Health at a Glance 2025; definitions differ by country)
  - "https://doi.org/10.5124/jkma.2024.67.4.256"  # Jung JG, Kim JS, Yoon SJ, Hong JH, Sunwoo J. 일차의료기관에서의 알코올 클리닉 지침. J Korean Med Assoc 2024;67(4):256-264 -- 1 standard drink = 14 g; 16.9% soju 1 standard drink = 1/3.5 bottle (105 mL); Korean moderate drinking <=8 drinks/week men <=65 (soju 2 bottles), <=4 women and men 65+, <=2 women 65+; Korean binge >3 drinks men, >2 women and men 65+; flushers (inactive ALDH2) half of each. Table adapted from Lee S et al. Korean J Fam Med 2019;40:204-211 (not read here). Note: the table footnote prints '1 drink=4 g', an evident typo for the 14 g stated in the text
  - "source:nutrition/alcohol-training-recovery-dose-031 -- the g/kg dose bands this row converts into glasses"
  - "source:leisure/kr-aldh2-flushing-010 -- the flushing genotype the guideline halves its thresholds for"
  - "source:leisure/alcohol-jcurve-collapse-009 -- why 'moderate' here is a lower-risk ceiling, not a recommended amount"
  - "source:nutrition/kr-mixed-dish-logging-unit-020 -- same principle: log in the unit people use, convert in data"
  - "framework:GRADE -- the survey rates are official national statistics from the issuing body (jurisdictional-standard A for what they define and count; self-report interview, so true intake is likely under-counted, see nutrition/self-report-underreporting-007). The unit conversion is arithmetic. The low-risk thresholds are a Korean professional guideline derived from Korean cohort studies on biomarkers, blood pressure, insulin resistance and cardiovascular risk, read only in a 2024 restatement, so practitioner-consensus band."
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: hedge
      rescale:
        per_unit_low: 0.077   # soju glasses (~6.5 g each) per kg body weight at 0.5 g/kg (031's REM anchor)
        per_unit_high: 0.154  # soju glasses per kg at 1.0 g/kg (031's strength-recovery anchor)
    - key: sex
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
drink_units:
  formula: ethanol_g = volume_ml x abv x 0.789
  units:
    - unit: 소주 1병
      volume_ml: 360
      abv_default: 0.165
      ethanol_g: 46.9
      note: label ABV overrides; at 16.9% (the JKMA example) 48.0 g
    - unit: 소주 1잔
      volume_ml: 50
      abv_default: 0.165
      ethanol_g: 6.5
      note: glass size is a convention (~7 glasses per bottle), not a measured standard
    - unit: 맥주 1캔 (355 mL)
      volume_ml: 355
      abv_default: 0.045
      ethanol_g: 12.6
      note: KDCA counts beer in cans without stating size
    - unit: 맥주 500 mL (생맥주 1잔, 큰 캔)
      volume_ml: 500
      abv_default: 0.045
      ethanol_g: 17.8
      note: one 500 mL beer is about 1.3 standard drinks
    - unit: 막걸리 1병
      volume_ml: 750
      abv_default: 0.06
      ethanol_g: 35.5
      note: one bowl (~300 mL) is about one 14 g standard drink
    - unit: 와인 1잔
      volume_ml: 150
      abv_default: 0.12
      ethanol_g: 14.2
      note: about one 14 g standard drink
    - unit: 위스키 1샷
      volume_ml: 45
      abv_default: 0.40
      ethanol_g: 14.2
      note: about one 14 g standard drink
    - unit: 소맥 1잔
      volume_ml: null
      abv_default: null
      ethanol_g: null
      note: no standard ratio; count the soju and beer poured separately, or ask
kr_thresholds:
  - label: KDCA binge occasion (월간폭음 / 고위험음주 amount)
    men: 7잔 (or 5 beer cans) per occasion
    women: 5잔 (or 3 beer cans) per occasion
    approx_g_men: 45
    approx_g_women: 32
    frequency_rule: binge = 1+/month; high-risk = 2+/week over the past year
    use: population survey category; never label a user from one night or one week of logs
    basis_grade: A
  - label: Korean guideline weekly lower-risk ceiling
    men_to_65: 8 standard drinks (112 g, about soju 2 bottles) per week
    women_and_men_over_65: 4 standard drinks (56 g, about soju 1 bottle) per week
    women_over_65: 2 standard drinks (28 g) per week
    flushers: half of the above
    use: may be quoted as the Korean guideline's figure if the user asks; not a target, not proof of benefit (009)
    basis_grade: D
  - label: Korean guideline binge occasion
    men: more than 3 standard drinks (over 42 g)
    women_and_men_over_65: more than 2 standard drinks (over 28 g)
    flushers: half of the above
    use: same as above
    basis_grade: D
refraction_notes:
  - note: >
      HOW KOREANS COUNT, CONVERTED. A 360 mL bottle of soju at a label
      16.5 percent holds about 47 g of ethanol; a ~50 mL glass about 6.5 g;
      a 355 mL can of 4.5 percent beer about 12.6 g; a 500 mL draft about
      17.8 g; a 750 mL bottle of 6 percent makgeolli about 35.5 g. These are
      arithmetic from volume and label strength; the product's own label
      overrides the default. 소맥 has no standard ratio and must be counted
      by its parts.
    grade: A
  - note: >
      WHAT THE 031 DOSES LOOK LIKE HERE. For a 70 kg person, 0.5 g/kg is
      35 g, about five to six glasses of soju (roughly three quarters of a
      bottle); 1.0 g/kg is about a bottle and a half; 1.5 g/kg, the dose that
      cut protein synthesis, is a little over two bottles. For a 55 kg person
      0.5 g/kg is about four glasses. The KDCA binge amount for men (7 glasses,
      about one bottle) sits between the REM anchor and the strength anchor
      for an average-weight man.
    grade: A
  - note: >
      WHAT ORDINARY KOREAN DRINKING LOOKS LIKE. In the 2025 Community Health
      Survey, 57.1 percent of adults drank at least monthly, 33.7 percent
      binged (men 7+ glasses, women 5+ in one sitting) at least monthly, and
      12.0 percent did so twice a week or more. Among monthly drinkers,
      59 percent binged. About half of men in their 30s to 50s binge monthly.
      So a user reporting a one-bottle 회식 night is describing the common
      Korean pattern, not an outlier. Over 2016-2025 high-risk drinking fell
      in men of every age and rose in women 30 and over. Self-reported, so if
      anything an under-count.
    grade: A
  - note: >
      THE KOREAN GUIDELINE IS LOWER THAN THE US ONE, ON PURPOSE. Korean
      family-medicine guidance sets the weekly lower-risk ceiling at 8
      standard drinks of 14 g for men up to 65 (about two bottles of soju)
      and 4 for women and older men, with binge at more than 3 and more than
      2 drinks per occasion, and halves everything for people who flush. Its
      reasoning is Korean cohort data and smaller average body weight
      (US adults weighed 1.24-1.34 times more than Korean adults in the cited
      comparison). It is a professional guideline, read in its 2024
      restatement; the 2019 original was not read.
    grade: D
  - note: >
      LABELS ARE FOR POPULATIONS. 고위험음주 is a survey category that needs
      binge-level drinking twice a week across a year. The engine must not
      call a user 고위험음주자, 폭음자 or anything clinical from a log, and must
      not volunteer the weekly ceiling as a scolding. When the user asks "how
      much is a lot", the survey amounts and the guideline figures can be
      quoted with their source, flatly. Flushing users get the half figures
      only if they bring up flushing.
    grade: D
claim: >
  Korean drinking is counted in glasses, bottles and cans, so this row
  carries the conversion as data: ethanol in grams is volume x label ABV x
  0.789, giving about 47 g for a 360 mL bottle of 16.5 percent soju, 6.5 g
  for a ~50 mL glass, 12.6 g for a 355 mL can of 4.5 percent beer and 35.5 g
  for a 750 mL bottle of 6 percent makgeolli. On that scale the dose bands
  in nutrition/alcohol-training-recovery-dose-031 read as roughly three
  quarters of a bottle of soju (0.5 g/kg, the REM-reduction anchor), a
  bottle and a half (1.0 g/kg, slower strength recovery) and a little over
  two bottles (1.5 g/kg, blunted protein synthesis) for a 70 kg person. The
  KDCA 2025 Community Health Survey (about 230,000 adults) found 57.1
  percent drinking monthly, 33.7 percent binge drinking monthly (men 7+
  glasses or 5 cans, women 5+ or 3 cans per sitting) and 12.0 percent
  binge drinking twice a week or more; 59 percent of monthly drinkers binge,
  and about half of men in their 30s-50s do. A Korean family-medicine
  guideline sets lower-risk ceilings at 8 standard drinks (112 g) a week for
  men up to 65 and 4 for women and older men, with binge above 3 and 2
  drinks per sitting and half of each for people who flush. These are
  population categories and a professional guideline, quoted when asked,
  never applied as a label to one user's log.
reasoning: >
  The leisure section of GAPS.md named the missing Korean unit convention as
  the domain's clearest failure: thresholds in grams cannot be spoken to
  someone who counts in 잔. Two primary documents close most of it. The KDCA
  press release is the issuing body's own publication of its survey
  definitions and 2025 rates, which is the strongest form a jurisdictional
  statistic takes here, so it is carried at the top band for what it
  defines and counts while noting that interview self-report under-counts
  intake. The JKMA 2024 guideline gives the Korean standard-drink anchor
  (14 g, 1/3.5 bottle of 16.9 percent soju) and the Korean thresholds,
  derived from Korean cohort studies and adjusted for body size and
  flushing; because it is a professional guideline read in restatement,
  its thresholds stay in the practitioner band. The conversion is plain
  arithmetic and graded as such; the one convention that is not measured,
  the ~50 mL soju glass, is labelled. Survey categories are kept away from
  individual labelling deliberately: a population definition built on a
  year of frequency cannot be applied to a single night, and doing so would
  be the moralising 031 forbids.
---

# nutrition/kr-alcohol-units-drinking-pattern-032 -- 소주 몇 잔이 몇 그램인가, 한국인은 얼마나 마시나

**한 줄 그림:** 소주 1병은 알코올 약 47g, 1잔은 약 6.5g이다. 70kg이면 0.5g/kg은 소주 3/4병, 1g/kg은 1병 반쯤이다.

## Unit table (engine-readable)

`ethanol_g = volume_ml x ABV x 0.789`. The label ABV overrides the default.

| Drink | mL | Default ABV | Ethanol | 14 g standard drinks |
|---|---|---|---|---|
| 소주 1병 | 360 | 16.5% | ~47 g | ~3.4 |
| 소주 1잔 | ~50 | 16.5% | ~6.5 g | ~0.5 |
| 맥주 1캔 | 355 | 4.5% | ~12.6 g | ~0.9 |
| 맥주 500 mL | 500 | 4.5% | ~17.8 g | ~1.3 |
| 막걸리 1병 | 750 | 6% | ~35.5 g | ~2.5 |
| 와인 1잔 | 150 | 12% | ~14.2 g | ~1 |
| 위스키 1샷 | 45 | 40% | ~14.2 g | ~1 |
| 소맥 | -- | -- | count each part | -- |

## The 031 bands in Korean units (70 kg / 55 kg)

| 031 anchor | 70 kg | 55 kg |
|---|---|---|
| 0.5 g/kg (REM reduced) | 35 g, soju 5-6 glasses | 27.5 g, soju ~4 glasses |
| 1.0 g/kg (slower strength recovery) | 70 g, soju ~1.5 bottles | 55 g, soju ~8 glasses |
| 1.5 g/kg (protein synthesis blunted) | 105 g, soju ~2.2 bottles | 82.5 g, soju ~1.75 bottles |

## 한국어 요약 (답변용)

- 알코올 양은 "용량(mL) × 도수 × 0.789"로 계산한다. 소주 1병(360mL, 16.5%)은 약 47g, 소주 1잔(약
  50mL)은 약 6.5g, 맥주 355mL 1캔(4.5%)은 약 12.6g, 500mL는 약 17.8g, 막걸리 1병(750mL, 6%)은 약
  35.5g이다. 제품 라벨 도수가 다르면 라벨 도수로 계산한다. 소맥은 정해진 비율이 없으니 소주와 맥주를
  따로 센다.
- 70kg인 사람에게 소주 3/4병쯤이면 렘수면이 줄기 시작하는 양(0.5g/kg)이고, 1병 반이면 근력 회복이
  늦어진 양(1g/kg), 2병 남짓이면 근육 단백질 합성이 줄었던 양(1.5g/kg)이다.
- 2025 지역사회건강조사에서 성인 57.1%가 한 달에 한 번 이상 마셨고, 33.7%가 한 달에 한 번 이상
  폭음(남자 7잔 이상 또는 맥주 5캔, 여자 5잔 이상 또는 맥주 3캔)을 했다. 이런 폭음을 주 2회 이상 하는
  고위험음주는 12.0%였다. 30~50대 남성은 둘 중 한 명이 폭음을 한다. 회식에서 소주 1병쯤 마신 건 한국에서
  흔한 일이다. 최근 10년 동안 고위험음주는 남성은 모든 연령에서 줄었고, 여성은 30대 이상에서 늘었다.
- 국내 가정의학 진료지침은 한국인 남성(65세 이하)의 저위험 음주를 주 8잔 이하(1잔 = 알코올 14g, 소주
  약 2병), 여성과 65세 이상 남성은 주 4잔 이하로 본다. 한 번에 남성 3잔, 여성 2잔을 넘기면 폭음으로
  보고, 마시면 얼굴이 빨개지는 사람은 모두 절반이다. 미국 기준보다 낮은데, 한국인 자료와 체중 차이를
  반영했기 때문이다.
- 이 숫자들은 집단 통계이고 전문가 지침이다. 기록 한두 번으로 사용자를 "고위험음주자"나 "폭음자"로 부르지
  않는다. 기준을 먼저 꺼내 훈계하지도 않는다. 사용자가 "얼마면 많은 거냐"고 물으면 출처와 함께 담담하게
  알려준다. 얼굴이 빨개지는 사람 기준(절반)은 사용자가 홍조를 말했을 때만 쓴다.
