---
# Diet-adherence sprint 2026-10-07 (dispatch kw-nu-diet-adherence-structure).
# MATADOR is quoted as "diet breaks make you lose 50 percent more fat". Read
# at the full text: obese men, ALL main meals provided, per-protocol
# completers, and the break arm took 30 weeks to do 16 weeks of restriction.
# The trained-adult replication (ICECAP, intention-to-treat) found no extra
# fat loss but lower hunger. Both are carried; the superiority claim is held
# contested.
id: nutrition/diet-breaks-refeeds-026
domain: nutrition
lane: "@obs-inferential"
grade: B (no-worse per restriction week; the superiority claim is contested)
locale: universal
as_of: 2018-2021
contested: yes
sources:
  - "https://doi.org/10.1038/ijo.2017.206"  # Byrne NM, Sainsbury A, King NA, Hills AP, Wood RE. Intermittent energy restriction improves weight loss efficiency in obese men: the MATADOR study. Int J Obes 2018;42(2):129-138. PMID 28925405, PMC5803575 (full text read 2026-10-07) -- n=51 randomised, 47 started; 16 wk restriction at 67 pct of maintenance, continuous vs 8 x 2-wk restriction alternating with 7 x 2-wk energy balance (30 wk total); all main meals and snacks provided; per-protocol (19 vs 17) weight loss 14.1 vs 9.1 kg, fat 12.3 vs 8.0 kg; break blocks 0.0 +/- 0.3 kg; 6-month follow-up subset (13 vs 15) loss about 8 kg greater in the break arm
  - "https://doi.org/10.1249/MSS.0000000000002636"  # Peos JJ, Helms ER, Fournier PA, Ong J, Hall C, Krieger J, Sainsbury A. Continuous versus intermittent dieting for fat loss and fat-free mass retention in resistance-trained adults: the ICECAP trial. Med Sci Sports Exerc 2021;53(8):1685-1698. PMID 33587549 -- n=61 (32 women), intention-to-treat; 4 x 3 wk moderate restriction with 3 x 1 wk energy balance (15 wk) vs 12 wk continuous; no difference in fat mass, fat-free mass, weight, strength, REE or hormones; lower hunger and desire to eat, higher satisfaction in the break arm
  - "https://doi.org/10.1371/journal.pone.0247292"  # Peos JJ, Helms ER, Fournier PA, Krieger J, Sainsbury A. PLoS One 2021;16(2):e0247292. PMID 33630880 -- pre-specified ICECAP secondary analysis, n=26: across a 1-week break fat mass did not change, body weight +0.6 kg and fat-free mass +0.7 kg, hunger and irritability down, satisfaction up
  - "https://doi.org/10.3390/jfmk5010019"  # Campbell BI et al. J Funct Morphol Kinesiol 2020;5(1):19. PMID 33467235 -- refeed trial: n=27 resistance-trained, 7 wk, ~25 pct deficit continuous vs 5 days ~35 pct deficit + 2 high-carbohydrate maintenance days; weight and fat loss not different; authors report better fat-free mass and RMR retention
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7739336/"  # Peos JJ et al. comment on Campbell 2020, J Funct Morphol Kinesiol 2020 -- on reanalysis only dry fat-free mass differed between groups; Campbell et al. replied (PMC7739255). Held as an open printed dispute
  - "source:nutrition/weight-loss-rate-lean-mass-012 -- the rate and lean-mass question a break is often sold as solving"
  - "source:nutrition/body-composition-measurement-floor-011 -- why a 0.4 vs 1.3 kg fat-free-mass difference over 7 weeks is at the edge of what the instruments resolve"
  - "source:nutrition/adherence-rules-074 -- the diet-card rule that consumes this item"
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
      A BREAK IS MAINTENANCE, NOT A FREE-FOR-ALL. In both break trials the
      break was calibrated energy balance (MATADOR supplied the food and
      reported 0.0 kg change across break blocks; ICECAP set intake to
      predicted maintenance, mostly from extra carbohydrate). Neither trial
      tested an unstructured "cheat week", and neither result transfers to one.
    grade: B
  - note: >
      THE CALENDAR COST IS REAL. Breaks do not shorten a diet; they lengthen
      it. MATADOR needed 30 weeks for 16 weeks of restriction, ICECAP 15 for
      12. Any plan with breaks must show the longer end date.
    grade: A (rule)
  - note: >
      THE "MORE FAT LOSS" CLAIM IS CONTESTED. MATADOR's advantage is in obese
      men eating provided food, reported per protocol; the intention-to-treat
      replication in trained adults found none. For a trained, free-living
      user the defensible expectation is equal fat loss per restriction week,
      with less hunger. Do not quote the 14.1 vs 9.1 kg figure as what a user
      can expect.
    grade: C
  - note: >
      REFEEDS (1-2 DAYS) AND FAT-FREE MASS: one 27-person trial, effect only
      robust for dry fat-free mass on reanalysis, disputed in print. Equal
      fat loss with a weekly 2-day maintenance block is the safe reading; the
      muscle-sparing claim is not.
    grade: D
  - note: >
      WHY OFFER ONE AT ALL: ICECAP is the cleanest evidence and its signal is
      appetite and satisfaction, which are adherence variables. A break is an
      adherence tool with no measured fat-loss cost, not a metabolic trick.
    grade: B
  - note: >
      EXPECT THE SCALE TO RISE DURING A BREAK. In the ICECAP secondary analysis
      a 1-week break raised body weight 0.6 kg with no change in fat mass. The
      weekly retro must not read a break-week rise as regain or as a missed
      target.
    grade: B
claim: >
  Planned diet breaks (one to two weeks at energy balance between blocks of
  restriction) and weekly refeeds (two maintenance days inside the week) do
  not reduce fat loss per week of restriction compared with continuous
  dieting in the trials located, and in the best-controlled trial (ICECAP,
  61 resistance-trained adults, intention-to-treat) they reduced hunger and
  desire to eat and raised satisfaction while fat mass, fat-free mass,
  strength and resting energy expenditure did not differ. Whether breaks
  produce MORE fat loss is contested: MATADOR (obese men, all food provided,
  per-protocol) reported 14.1 versus 9.1 kg, the trained-adult replication
  found no difference. Breaks always lengthen the calendar time of a diet,
  and the break itself was calibrated maintenance, not unrestricted eating.
reasoning: >
  Three randomised trials point the same way on the no-harm question, which
  is why that part is graded at the trial band; they disagree on benefit,
  which is why the item is contested and the superiority sentence is held at
  the observational band. The disagreement is explicable rather than random:
  MATADOR's population had obesity, ate supplied food and is reported per
  protocol (the intention-to-treat analysis is in the full text and the
  advantage is smaller there), while ICECAP recruited trained, leaner adults
  and analysed everyone randomised. The 6-month follow-up advantage in
  MATADOR rests on a 28-person subset and is not carried as a figure. The
  refeed trial is small and short, and its fat-free-mass claim was
  reanalysed in print by the ICECAP authors to a dry-fat-free-mass-only
  difference; that is an open dispute, carried as such. The practical value
  the evidence does support is appetite: lower hunger with no measured cost
  is an adherence lever, and the engine should treat it as one.
---

# nutrition/diet-breaks-refeeds-026 -- 다이어트 브레이크와 리피드

다이어트 중간에 1~2주 유지 칼로리로 먹는 '다이어트 브레이크'는 MATADOR 연구
덕분에 "지방이 50% 더 빠진다"는 말로 퍼졌다. 원문을 읽으면 조건이 붙는다. 대상은
비만 남성이었고, 주요 끼니와 간식은 모두 연구진이 제공했으며, 큰 숫자(14.1 대
9.1 kg)는 끝까지 지킨 사람만 따로 본 분석이다. 그리고 브레이크 쪽은 16주 감량을
하는 데 30주가 걸렸다.

근력 운동을 하는 성인 61명을 대상으로 한 재현 연구(ICECAP)는 무작위 배정된 사람
전원을 분석했다. 3주 감량과 1주 유지를 번갈아 하는 쪽과 12주 연속 감량을 비교했을 때
지방, 제지방, 체중, 근력, 기초대사량 모두 차이가 없었다. 달랐던 것은 배고픔이다.
브레이크 쪽이 덜 배고팠고, 먹고 싶은 마음도 덜했고, 만족도는 높았다.

주말 이틀을 유지 칼로리로 먹는 '리피드'는 27명을 7주 본 연구 하나다. 지방 감량은
같았다. 근육 보존 효과는 재분석에서 수분을 뺀 제지방에서만 남았고, 지금도 지면에서
논쟁 중이다.

그러니 브레이크는 지방을 더 태우는 장치가 아니라, 손해 없이 배고픔을 줄이는 지속
장치로 쓴다. 브레이크는 유지 칼로리로 먹는 기간이지 마음대로 먹는 기간이 아니다.
그리고 끝나는 날짜는 반드시 뒤로 밀린다.

## 한국어 요약 (답변용)

- 브레이크·리피드를 제안할 수 있는 근거는 "감량 주당 지방 손실은 같고 배고픔은 줄었다"는
  것이다. "더 빠진다"고 약속하지 않는다.
- 브레이크는 유지 칼로리로 먹는 기간이다. 치팅 주간이 아니다. 기록과 체중 측정은 계속한다.
- 브레이크를 넣으면 목표 날짜가 그만큼 늦어진다. 식단 카드에 늦어진 날짜를 함께 보여 준다.
- 브레이크 주에 체중이 조금 오르는 건 예상 범위다. ICECAP 1주 브레이크에서 체중은 평균
  0.6 kg 올랐지만 지방량은 변하지 않았다(늘어난 몫은 제지방으로 측정됨). 지방이 다시
  붙었다고 해석하지 않는다.
- 리피드가 근육을 지켜 준다는 말은 하지 않는다. 근거가 작은 연구 하나이고 논쟁 중이다.
