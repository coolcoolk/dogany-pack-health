---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). KR-LOCALE item.
# Filed because the consumer eats and logs a Korean diet, and because the check
# turned up a live staleness trap: the Korean reference standard was REVISED on
# 2025-12-31 and any advice keyed to the 2020 edition is now out of date. Primary
# source is the issuing ministry's own release plus its official 2020-vs-2025
# comparison attachment, retrieved directly.
id: nutrition/kr-reference-intakes-2025-014
domain: nutrition
lane: "@obs-inferential"
grade: A (jurisdictional-standard)
locale: KR
as_of: 2025-12-31
contested: no
sources:
  - "https://mohw.go.kr/board.es?act=view&bid=0027&list_no=1488441&mid=a10503010100"  # Ministry of Health and Welfare, Republic of Korea. Press release, embargo 2025-12-31: 2025 Korean Dietary Reference Intakes (2025 한국인 영양소 섭취기준). Issued with the Korean Nutrition Society under the National Nutrition Management Act art. 14 (5-year revision cycle)
  - "MOHW attachment seq 2 to the above release -- the ministry explanatory document carrying the fibre derivation and the protein rationale"
  - "MOHW attachment seq 3 to the above release -- the official 2020-vs-2025 comparison table (대비표) carrying the per-age-band values"
  - "source:nutrition/fibre-doseresponse-013 -- the universal evidence base the Korean fibre figure happens to converge with"
  - "source:nutrition/protein-intake-002 -- the athletic per-kg protein range, which is a DIFFERENT construct from a national reference intake"
applicability:
  axes:
    - key: sex
      type: categorical
      role: hard
      unknown_policy: ask
    - key: age_years
      type: numeric
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      STALENESS TRAP. Korea revises this standard every five years by statute, and
      the 2025 edition superseded the 2020 edition on 2025-12-31. Any Korean
      nutrition guidance carried from before that date, including the widely
      circulated 2020 figures, is a prior edition. Re-check the edition before
      quoting any Korean reference number.
    grade: A
  - note: >
      PROVENANCE ASYMMETRY WITHIN THIS ITEM, stated so the weaker half is not read
      as the stronger. The adult male 30 g per day fibre figure is triply
      corroborated: it appears in the comparison table, it is consistent with the
      release prose keeping men aged 50 and over at 30 g or more, and it is what
      the stated 12.5 g per 1000 kcal basis yields against the male adult energy
      requirement after rounding. The female figures were read from the comparison
      table attachment only, whose column structure had to be reconstructed from
      the extracted layout; the release prose independently confirms 25 g for
      women aged 50 and over but not the under-50 value. Re-read the primary table
      before speaking a female under-50 figure.
    grade: C
  - note: >
      A NATIONAL REFERENCE INTAKE IS NOT AN ATHLETIC TARGET. The protein figures
      here are population adequacy standards, expressed as grams per day and as an
      energy-percentage range. They are not the per-kilogram training range owned
      by nutrition/protein-intake-002 and are not interchangeable with it. The
      two answer different questions and a consumer must not be shown one as a
      correction to the other.
    grade: A
  - note: >
      WHAT THIS ITEM DOES NOT COVER: sodium. The Korean diet's sodium load is the
      most obvious jurisdiction-specific nutrition question and its outcome
      evidence is genuinely disputed. It was not researched in this pass and its
      absence here must not be read as an all-clear.
    grade: D
claim: >
  Korea revised its national dietary reference standard effective 2025-12-31 (the
  2025 Korean Dietary Reference Intakes, issued by the Ministry of Health and
  Welfare with the Korean Nutrition Society on a statutory 5-year cycle covering
  41 nutrients). Changes relevant to a training consumer: the acceptable
  macronutrient distribution range for protein was RAISED from 7-20 percent to
  10-20 percent of energy, and for carbohydrate lowered from 55-65 percent to
  50-65 percent, with fat unchanged at 15-30 percent. Dietary fibre adequate
  intake was re-derived on a new basis of 12.5 g per 1000 kcal for adults with
  age adjustment; adults aged 50 and over are held at 30 g or more for men and
  25 g or more for women. The adult male figure is 30 g per day. Total-sugar
  wording became "within 20 percent" and added sugar "limited to within 10
  percent", with added advice to minimise sweetened beverages.
reasoning: >
  Confidence here is about WHAT THE STANDARD SAYS, not about whether the standard
  is the right target, and on that question a government-issued document
  describing its own contents is definitive, so it sits at the top band with a
  jurisdictional qualifier. The health rationale underneath it is a separate
  matter and inherits the observational band from nutrition/fibre-doseresponse-013
  and the general evidence base. The item earns its place through the staleness
  finding: the KR check was run precisely because a Korean-diet consumer needs
  Korean numbers, and it surfaced that the standard everyone would have quoted was
  superseded eight months before this item was written. Two limits are carried
  openly. The female under-50 fibre value rests on a reconstructed reading of a
  table attachment rather than on release prose, and is flagged for re-reading
  rather than quoted with false confidence. And sodium, the single most
  Korea-specific nutrition question, was not researched and is recorded as absent.
---

# nutrition/kr-reference-intakes-2025-014

한국인 영양소 섭취기준은 2025년 12월 31일자로 개정됐다. 국민영양관리법에 따라
5년 주기로 보건복지부와 한국영양학회가 함께 제·개정하며, 이번 판은 영양소 41종을
다룬다. 2020년판을 근거로 만들어진 한국 관련 영양 조언은 전부 이전 판 기준이라는
뜻이므로, 한국 수치를 인용하기 전에 판본부터 확인해야 한다.

운동하는 사용자에게 실제로 바뀌는 것:

- **단백질 에너지적정비율**이 7~20%에서 **10~20%**로 하한이 올라갔다. 탄수화물은
  55~65%에서 50~65%로 하향, 지방은 15~30% 유지.
- **식이섬유 충분섭취량**의 산출 기준이 성인 **12.5 g/1,000 kcal**로 새로 잡혔고
  연령별로 보정됐다. 50세 이상은 만성질환 예방 목적으로 남성 30 g, 여성 25 g
  이상을 유지한다. 성인 남성 기준값은 **30 g/일**이다.
- **총당류**는 "20% 이내", **첨가당**은 "10% 이내 제한"으로 문구가 강화됐고,
  가당음료 섭취를 가능한 줄이라는 문장이 추가됐다.

세 가지를 분명히 해둔다. 첫째, 성인 남성 30 g은 세 경로로 교차 확인된 값이지만,
50세 미만 여성 값은 대비표 첨부의 표 구조를 복원해 읽은 것이라 확신도가 낮다.
보도자료 본문이 직접 확인해 주는 것은 50세 이상 여성 25 g뿐이므로, 여성 수치를
말하기 전에 원표를 다시 확인해야 한다.

둘째, 이건 국가 인구집단 적정섭취 기준이지 훈련 목표치가 아니다. 체중당 g으로
표현되는 운동인 단백질 범위는 별도 항목이 소유하고 있고, 둘은 서로 다른 질문에
답한다. 하나를 다른 하나의 정정처럼 제시하면 안 된다.

셋째, 나트륨은 이번에 다루지 않았다. 한국 식단에서 가장 두드러지는 영양 이슈이고
건강 결과 근거 자체가 논쟁적이라 별도 검증 없이 넣지 않았다. 여기 없다는 게
괜찮다는 뜻은 아니다.
