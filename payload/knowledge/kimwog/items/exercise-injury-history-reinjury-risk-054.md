---
# Injury-caution sprint (directive: caution depends on the injury's severity,
# site and type, read from the warehouse). The split
# recommendation must decide how much a caution site weighs. This row carries
# the HISTORY half: does an old injury still count, does a recent one count
# more, and does it depend on the tissue. Companion rows: 055 (what to do with a
# tendon / fascia site that hurts now), 056 (the ladder the engine reads).
# Population caveat stated up front: almost every cohort here is team sport
# (football, Australian football) or post-surgical; no prospective re-injury
# cohort in recreational lifters was located.
id: exercise/injury-history-reinjury-risk-054
domain: exercise
grade: C (prior injury raises same-site risk; recent more than remote); D (any specific time boundary such as 12 months)
lane: "@clinical-physio"
locale: universal
as_of: 2006-2020
contested: no
sources:
  - "https://bjsm.bmj.com/content/40/9/767"  # Hägglund M, Waldén M, Ekstrand J 2006, Br J Sports Med 40(9):767-772 -- 12 elite Swedish men's football teams, two seasons; injured in season 1 -> HR 2.7 (95% CI 1.7-4.3) for any injury in season 2; previous hamstring, groin and knee-joint injury 2-3x more likely to recur identically; NO such relation for ankle sprain
  - "https://bjsm.bmj.com/content/54/18/1081"  # Green B, Bourne MN, van Dyk N, Pizzari T 2020, Br J Sports Med 54(18):1081-1088 -- 78 studies, 8,319 hamstring injuries; any previous HSI RR 2.7, RECENT (same-season) HSI RR 4.8; previous ACL injury RR 1.7; previous calf strain RR 1.5; older age
  - "https://bjsm.bmj.com/content/51/23/1670"  # Toohey LA et al. 2017, Br J Sports Med 51(23):1670-1678 -- 12 studies; previous injury of one kind raises risk of a DIFFERENT lower-limb injury (ACL history -> hamstring RR 2.25, 95% CI 1.34-3.76; muscle injury -> muscle injury elsewhere)
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC4196323/"  # Fulton J et al. 2014, Int J Sports Phys Ther 9(5):583-595 -- narrative-systematic review by tissue: hamstring, ACL, Achilles, ankle; neuromuscular deficits (strength, proprioception, kinematics) as the proposed mechanism
  - "https://pubmed.ncbi.nlm.nih.gov/26772611/"  # Wiggins AJ et al. 2016, Am J Sports Med 44(7):1861-1876 -- after ACL reconstruction, second ACL injury 15% overall, 23% in under-25s returning to sport, and early in the return period
  - "https://bjsm.bmj.com/content/46/2/124"  # de Visser HM et al. 2012, Br J Sports Med 46(2):124-130 -- recurrent hamstring injury, 5 prospective studies: recurrence 13.9-63.3% in the same season up to 2 years after the first injury; evidence for individual risk factors limited. The often-repeated "over half of recurrences in the first month after return" figure was NOT confirmed at a primary in this sprint and is not carried (GAPS.md)
  - "https://pubmed.ncbi.nlm.nih.gov/30131332/"  # Lauersen JB et al. 2018, Br J Sports Med 52:1557-1563 -- strength training reduces acute and overuse sports injury (RR 0.338), dose-dependent
  - "https://research.bond.edu.au/en/publications/the-epidemiology-of-injuries-across-the-weight-training-sports/"  # Keogh JWL, Winwood PW 2017, Sports Med 47(3):479-501 -- weight-training sports ~2-4 injuries per 1000 h; shoulder, lower back, knee, elbow, wrist/hand most common; strains, tendinitis, sprains most common types
  - "exercise/ideal-healthy-lean-injury-free-045"  # within-warehouse: strength training as the trainable injury lever
  - "exercise/tendon-fascia-load-management-055"  # within-warehouse: what to do when the site hurts now
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the engine-readable ladder this row feeds
  - "framework:GRADE -- prospective cohorts (observational) consistently show the direction; the magnitudes come from team-sport and post-surgical populations and are not transportable as numbers to a recreational lifter. No study located sets a time boundary after which a past injury stops mattering; the 12-month cut used by product code is a convention."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: soft
      unknown_policy: ask
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      A PAST INJURY NEVER DROPS TO ZERO WEIGHT. Across cohorts, any previous
      injury at a site raises the chance of a new one there, and also of a
      different injury nearby (ACL history -> hamstring). Elapsed time
      weakens the signal but no study located shows it disappearing. An old,
      well-healed injury therefore earns a small, non-zero weight (prep and
      site-specific strengthening), never exclusion.
    grade: C
  - note: >
      RECENT COUNTS ROUGHLY DOUBLE. For hamstring strain the same-season
      (recent) history ratio was 4.8 against 2.7 for any history, and
      second ACL injuries cluster early in the return period. (The popular
      "most hamstring recurrences come in the first month" figure was not
      confirmed at a primary and is not carried.) Direction
      is solid; the exact window is not. Treat "recent" as heavier than
      "old" without claiming the boundary is a measured one.
    grade: C
  - note: >
      THE 12-MONTH BOUNDARY IS A CONVENTION. "Same season" in football is a
      window of a few months to a year, which is where a 12-month product cut
      comes from. No study compares 11 against 13 months. Keep the boundary
      as a product constant, labelled as such, and never quote it as a
      finding.
    grade: D
  - note: >
      TISSUE CHANGES THE SHAPE, NOT THE DIRECTION. Muscle strain: recurrence
      concentrated in the same season after return. Ligament after
      reconstruction: high second-injury rate in young athletes returning to
      cutting sport, early. Ankle sprain: mixed (no recurrence relation in
      one elite cohort, raised risk in others; exercise therapy and bracing
      cut recurrence). Tendon: long, slow course -- the Achilles contralateral
      rupture signal sat years out. These are pivoting / sprinting sports;
      none is a lifting cohort.
    grade: C
  - note: >
      HISTORY IS MODIFIABLE. The proposed mechanism for elevated risk is
      residual deficit (strength, control, range), and strength training
      reduces injury dose-dependently. So the engine's response to history
      is to ADD work at the site (prep, targeted strengthening, controlled
      tempo) more than to remove it.
    grade: C
  - note: >
      LIFTING-SPECIFIC CONTEXT. Weight-training sports run at roughly 2-4
      injuries per 1000 hours, lower than common team sports, and the usual
      sites are shoulder, lower back, knee, elbow and wrist/hand -- mostly
      strains, tendon pain and sprains. No prospective study of re-injury by
      history in recreational lifters was located (GAPS.md).
    grade: C
claim: >
  A previous injury is one of the most consistent predictors of a new one at
  the same site, and it also raises the risk of a different injury nearby. In
  elite football, players injured in one season were 2.7 times as likely to be
  injured the next, and hamstring, groin and knee injuries recurred two to
  three times as often (ankle sprain did not, in that cohort). Recency
  strengthens the signal: a hamstring strain in the same season carried a risk
  ratio of 4.8 against 2.7 for any history, and hamstring recurrence runs
  at roughly 14-63% within the same season to two years. Elapsed time weakens but
  does not erase the signal, and no study sets the point at which a past
  injury stops counting. Tissue changes the time course (muscle within the same season,
  reconstructed ligament early and high in young returners, tendon slow), not
  the direction. The elevated risk is attributed to residual deficits, which
  strength training reduces. For a program engine: history earns non-zero
  weight that scales with recency, and the response is added preparation and
  targeted strengthening, not exclusion.
reasoning: >
  Hägglund 2006 is a prospective two-season cohort with individual exposure
  and a multivariate model -- the strongest design for "does history predict".
  Green 2020 is a meta-analysis of 78 studies and supplies the recent-versus-any
  contrast directly. Toohey 2017 extends the signal across injury types. Wiggins
  2016 adds the post-surgical ligament case. All are observational and from
  sport populations with sprinting, cutting and contact, so the letter is
  capped at the observational band and no number is transported to a lifter as
  a risk figure; only the direction and the relative ordering (recent > old >
  none) are carried. A first-month recurrence share circulates widely but
  was not confirmed at a primary here, so it is left out. The specific product boundary
  (12 months) has no direct evidence and is graded as a convention.
---

# exercise/injury-history-reinjury-risk-054 -- 예전 부상은 얼마나 오래 신경 써야 하나

**한 줄 그림:** 다쳤던 자리는 다시 다치기 쉽다. 최근일수록 더 그렇고, 오래돼도 0이 되지는 않는다.
대응은 빼기보다 그 자리를 준비시키고 강하게 만드는 쪽이다.

## What the engine reads from this row

| Input | Direction | Strength of the evidence |
|---|---|---|
| any history at the site | weight > 0 (never zero) | observational, consistent |
| recent history (within the product window) | weight about double the old-history weight | observational, consistent direction |
| exact window length (12 months) | product convention | no direct evidence |
| tissue = muscle | recurrence concentrated in the same season after return | observational |
| tissue = reconstructed ligament | high, early second injury in young returners to cutting sport | observational, post-surgical |
| tissue = tendon | slow course; see 055 for loading | mechanism + small trials |
| response to history | add prep and targeted strengthening; do not exclude | trial evidence for strength training |

## 한국어 요약 (답변용)

- 예전에 다친 부위는 같은 부위를 다시 다칠 위험이 높다. 축구 선수 코호트에서는 같은 부상이 다음
  시즌에 2-3배 많이 재발했다. 다만 이건 축구 같은 종목 데이터라, 헬스 하는 사람에게 숫자를 그대로
  옮기지 않는다. 방향만 가져온다.
- 최근 부상일수록 위험이 크다. 햄스트링은 같은 시즌 안의 부상이 예전 부상보다 위험을 더 크게
  올렸다. "재발 대부분이 복귀 첫 달"이라는 말은 원문에서 확인하지 못해 쓰지 않는다.
- 오래된 부상도 0으로 치지 않는다. 시간이 지나면 약해지지만, 언제부터 완전히 괜찮다고 볼 수
  있는지 정한 연구는 없다. 제품의 "12개월" 경계는 연구 결과가 아니라 정해 둔 규칙이다.
- 조직마다 시간표가 다르다. 근육은 복귀한 그 시즌 안이 위험하고, 수술한 인대는 젊은 선수가 방향 전환
  운동에 복귀할 때 이른 시기에 위험이 높다. 힘줄은 느리게 간다(055 참고).
- 대응은 빼는 쪽이 아니라 더하는 쪽이다. 남은 근력·조절 부족이 원인으로 꼽히고, 근력 운동은 부상을
  줄인다. 그래서 예전 부상 부위에는 준비 운동과 그 부위 강화를 더한다.
