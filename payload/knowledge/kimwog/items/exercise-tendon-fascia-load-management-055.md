---
# Injury-caution sprint 2026-10-06 (owner directive 17:50). The PRESENT-PAIN
# half for the tissues a lifter most often carries: tendon (patellar, Achilles,
# rotator cuff) and plantar fascia. Product code today treats "current pain"
# as avoid-all-site-loading. For these tissues the trial evidence says the
# opposite default: keep loading, under a pain-monitoring rule. This row does
# NOT cover acute trauma, joint locking/giving way, swelling, night pain or
# nerve symptoms -- those stay with the pain-triage skill (harm boundary 031).
id: exercise/tendon-fascia-load-management-055
domain: exercise
grade: B (continued, monitored loading is not worse than rest for tendinopathy; progressive loading helps plantar fasciopathy short-term); C (shoulder and patellofemoral exercise effects, low-certainty pooled evidence); D (loading-day spacing for a lifter)
lane: "@clinical-physio"
locale: universal
as_of: 2007-2023
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/17307888/"  # Silbernagel KG, Thomeé R, Eriksson BI, Karlsson J 2007, Am J Sports Med 35(6):897-906 -- RCT n=38 Achilles tendinopathy: continued running/jumping under a pain-monitoring model vs 6 weeks active rest; no negative effect of continued loading out to 12 months. Model: pain during activity allowed to 5/10, after activity may reach 5/10, must settle by the next morning, morning pain/stiffness must not rise week to week
  - "https://myorthoevidence.com/AceReport/Report/7998"  # Beyer R et al. 2015, Am J Sports Med 43(7):1704-1711 -- RCT n=58 chronic Achilles tendinopathy: heavy slow resistance (3 sessions/week) vs daily eccentric training, equal clinical and structural improvement to 52 weeks; HSR compliance 92% vs 78%
  - "https://blogs.bmj.com/bjsm/2014/09/15/plantar-fasciitis-important-new-research-by-michael-rathleff/"  # Rathleff MS et al. 2015, Scand J Med Sci Sports 25(3):e292-e300 -- RCT n=48 ultrasound-verified plantar fasciitis: high-load single-leg heel raise (towel under toes, 3 s up / 2 s hold / 3 s down, every second day, 12RM -> 8RM with backpack load) vs stretching; Foot Function Index 29 points better at 3 months, no difference at 6 and 12 months
  - "https://pubmed.ncbi.nlm.nih.gov/38037331/"  # Koc TA et al. 2023, J Orthop Sports Phys Ther 53(12):CPG1-CPG39 -- heel pain / plantar fasciitis clinical practice guideline revision (APTA Academy of Orthopaedic PT); cited from the record, no recommendation strength quoted
  - "https://bjsm.bmj.com/content/51/23/1679"  # Smith BE et al. 2017, Br J Sports Med 51(23):1679-1687 -- meta-analysis of RCTs, chronic musculoskeletal pain: exercise into pain vs pain-free exercise -- small short-term benefit for painful exercise (SMD -0.27, moderate quality), no difference medium/long term estate-scrub:allow(cited author surname)
  - "https://bjsm.bmj.com/content/51/18/1340"  # Steuri R et al. 2017, Br J Sports Med 51(18):1340-1347 -- shoulder impingement meta-analysis: exercise beats non-exercise for pain (SMD -0.94, 95% CI -1.69 to -0.19), specific beats generic exercise; overall quality low
  - "https://bjsm.bmj.com/content/52/18/1170"  # Collins NJ et al. 2018, Br J Sports Med 52(18):1170-1178 -- patellofemoral pain consensus: exercise therapy, especially hip plus knee exercise, recommended for pain and function
  - "https://research.regionh.dk/en/publications/the-pathogenesis-of-tendinopathy-balancing-the-response-to-loadin/"  # Magnusson SP, Langberg H, Kjaer M 2010, Nat Rev Rheumatol 6(5):262-268 -- after loading, tendon collagen degradation rises and peaks earlier than synthesis; synthesis peaks ~24 h and stays raised ~3 days (mechanism for spacing heavy tendon-loading days)
  - "https://pubmed.ncbi.nlm.nih.gov/26390269/"  # Malliaras P, Cook J, Purdam C, Rio E 2015, J Orthop Sports Phys Ther 45(11):887-898 -- patellar tendinopathy: clinical diagnosis and load management; cited from the record, not read at full text
  - "exercise/injury-history-reinjury-risk-054"  # within-warehouse: the history half
  - "exercise/caution-severity-ladder-056"  # within-warehouse: the ladder this row feeds
  - "exercise/harm-route-boundary-031"  # within-warehouse: what stays with pain-triage
  - "framework:GRADE -- tendon and plantar-fascia loading rest on small RCTs (n=38, 48, 58) with consistent direction plus a moderate-quality meta-analysis on painful exercise; shoulder and patellofemoral pooled effects are low-certainty. No trial compares spreading a symptomatic site's load across more days against concentrating it in fewer days in resistance trainees."
applicability:
  axes:
    - key: injury_history
      type: categorical
      role: hard
      unknown_policy: block_specifics
refraction_notes:
  - note: >
      REST IS NOT THE DEFAULT FOR A FAMILIAR TENDON OR FASCIA ACHE. In
      Achilles tendinopathy, continuing loading under a pain-monitoring rule
      did no harm against six weeks of rest. Heavy slow loading three times a
      week matched daily eccentrics. For plantar fasciopathy, progressive
      high-load heel raises every second day beat stretching at three months.
      So "current pain" at a tendon or the plantar fascia, once triage has
      ruled out the red-flag pictures, maps to keep-loading-with-a-ceiling,
      not avoid.
    grade: B
  - note: >
      THE CEILING THE ENGINE CAN STATE. During the session pain may reach
      about 5 out of 10 and no more; after the session it may reach about 5;
      it must be back to the usual level by the next morning; and morning
      pain and stiffness must not climb from one week to the next. Breach any
      of the four -> step load back (fewer sets at the site, lower load,
      slower tempo, or swap to an isometric or less provocative variant) for
      the next exposure. This is the Silbernagel model; it was tested on the
      Achilles and is applied to other tendons by analogy.
    grade: B
  - note: >
      SOME PAIN DURING EXERCISE IS NOT A STOP SIGN. In chronic musculoskeletal
      pain, exercise that was allowed to hurt did slightly better short term
      than pain-free exercise and no worse later. The ceiling above, not
      zero pain, is the rule.
    grade: B
  - note: >
      SPACING HEAVY TENDON DAYS. Tendon collagen synthesis peaks around a day
      after loading and stays raised about three days, while breakdown peaks
      earlier; the trial protocols that worked loaded the site every second
      day or three times a week. This supports putting at least one day
      between the heaviest loading of a symptomatic tendon or fascia, and
      spreading that site's work across the week rather than stacking it
      into back-to-back days. Mechanism plus protocol design, not a
      head-to-head trial in lifters.
    grade: D
  - note: >
      SHOULDER AND KNEE-FRONT SPECIFICS. Shoulder pain of the impingement /
      rotator-cuff type improves with exercise (specific better than
      generic), low certainty. Patellofemoral pain is managed with hip plus
      knee exercise, consensus-backed. For both, the evidence is for doing
      targeted work, not for removing pressing or squatting days; whether a
      lifter flares less when pressing or squatting is spread across more,
      lighter days has not been tested.
    grade: C
  - note: >
      WHAT THIS ROW DOES NOT LICENSE. Sharp or catching pain, swelling,
      locking, giving way, night pain, numbness or weakness, pain after a
      new trauma, or pain that keeps rising -- these are not a tendon ache
      to train through. They go to the pain-triage skill first (031).
    grade: D
claim: >
  For tendon pain (patellar, Achilles, rotator cuff type) and plantar
  fasciopathy, continued, progressive loading is the treatment, not the risk.
  Continuing Achilles-loading activity under a pain-monitoring model did no
  harm compared with rest; heavy slow resistance three times a week matched
  daily eccentric training; progressive heavy heel raises every second day
  beat stretching for plantar fasciitis at three months. The monitoring rule
  the engine can state: pain up to about 5/10 during and after loading, back
  to baseline by the next morning, and morning pain and stiffness not rising
  week to week; breaching it steps the site's load back for the next
  exposure. Exercise into some pain is not worse than pain-free exercise.
  Spacing heavy loading of a symptomatic tendon or fascia by at least a day
  is supported by collagen-turnover timing and by the protocols that worked,
  but no trial in lifters compares spreading against concentrating the
  site's load. None of this covers trauma, swelling, locking, instability,
  night pain or nerve signs, which go to triage.
reasoning: >
  The Achilles trial (Silbernagel 2007) is small but randomised and is the
  origin of the pain-monitoring model in common clinical use. Beyer 2015 shows
  that a thrice-weekly heavy slow protocol is as effective as twice-daily
  eccentrics, which matters for a lifter: tendon rehab fits a normal training
  week. Rathleff 2015 is the plantar-fascia analogue, with a heavy, slow,
  every-second-day protocol and a short-term advantage that converges by six
  months. The 2017 pain-exercise meta-analysis supplies the general permission to work into some pain.
  Steuri 2017 and Collins 2018 extend the direction to the shoulder and the
  front of the knee at lower certainty. The spacing note rests on Magnusson
  2010's collagen-turnover timing plus protocol design, so it is held at the
  practitioner floor. The axis is marked hard with block_specifics: without
  knowing whether the site is a tendon/fascia ache or a red-flag picture, the
  specific loading ceiling is withheld and the triage route applies.
---

# exercise/tendon-fascia-load-management-055 -- 힘줄·족저근막이 아플 때 쉬어야 하나

**한 줄 그림:** 익숙한 힘줄·족저근막 통증이면 쉬지 말고, 아픔 상한을 지키며 계속 부하를 준다.
다음 날 아침에 돌아오지 않으면 그 부위만 한 단계 줄인다.

## The monitoring rule (engine-readable)

| Check | Pass | Breach -> next exposure at this site |
|---|---|---|
| pain during the session | at most about 5/10 | fewer sets, lower load, slower tempo, or a less provocative variant |
| pain after the session | at most about 5/10 | same |
| next morning | back to the usual level | same |
| week to week | morning pain/stiffness not rising | same, and hold progression |
| any red-flag picture | none | stop the site, route to pain-triage |

Spacing: at least one day between the heaviest loading days of a symptomatic
tendon or fascia; spread the site's work across the week rather than stacking
it on consecutive days.

## 한국어 요약 (답변용)

- 무릎 앞·아킬레스·어깨 회전근개 쪽 힘줄 통증, 족저근막 통증은 쉬는 것보다 부하를 계속 주는 게
  치료다. 아킬레스 힘줄 연구에서 통증 기준을 지키며 달리기·점프를 계속한 쪽이 6주 쉰 쪽보다
  나쁘지 않았다. 족저근막은 무겁고 천천히 하는 한발 카프레이즈를 이틀에 한 번 한 쪽이 3개월에
  스트레칭보다 좋았다.
- 기준은 이렇다. 운동 중 통증 10점 중 5점까지, 운동 후 5점까지. 다음 날 아침에는 평소 수준으로
  돌아와야 하고, 아침 통증·뻣뻣함이 주마다 늘면 안 된다. 하나라도 어기면 다음 번에 그 부위만
  세트·무게를 줄이거나 템포를 늦추거나 덜 자극하는 동작으로 바꾼다.
- 운동 중 약간 아픈 건 멈출 신호가 아니다. 통증을 어느 정도 허용한 운동이 통증 없는 운동보다
  나쁘지 않았다.
- 아픈 힘줄·근막에 가장 무거운 부하를 주는 날은 하루 이상 띄우고, 그 부위 운동은 연달아 몰지 말고
  주 안에 나눈다. 다만 이건 콜라겐 회복 시간과 효과 있던 프로그램 구성에서 나온 추론이고, 헬스
  하는 사람을 대상으로 나눠 하기와 몰아 하기를 비교한 연구는 없다.
- 날카롭거나 걸리는 통증, 붓기, 무릎이 잠기거나 빠지는 느낌, 밤에 아픈 통증, 저림·힘 빠짐,
  새로 다친 뒤의 통증, 계속 심해지는 통증은 여기 해당하지 않는다. 먼저 통증 확인(pain-triage)으로
  보낸다.
