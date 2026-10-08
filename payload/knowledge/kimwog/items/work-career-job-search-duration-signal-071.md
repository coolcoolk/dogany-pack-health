---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (work-career GAPS sprint, dispatch
# kw-work-newitems). Job-search DURATION: how a gap reads to employers, how
# job seekers misjudge their own odds, and the Korean time-to-first-job base
# rate. Links 018 (entry overconfidence) and task-management 001 (planning
# fallacy) -- the self-prediction error is the same family.
# Read at source 2026-10-06: Kroft et al. abstract (IDEAS/RePEc record);
# Eriksson and Rooth abstract (IDEAS/RePEc and IZA DP 6235 records); Mueller
# et al. AER abstract (aeaweb.org) and NBER w25294 full text (introduction and
# data section); 국가데이터처 2026-07-23 release text as mirrored by the KDI
# 경제정책정보센터 record (attachment D26070130.pdf named, not opened).
# CONTESTED on mechanism, not on direction: the audit studies attribute the
# callback decline to employer screening; Mueller et al. attribute most of
# the decline in job FINDING to who is left in the pool (dynamic selection).
# Rubric: work-career.rubric.md @behavioral-career row
# work-career/job-search-duration-signal-071.
id: work-career/job-search-duration-signal-071
domain: work-career
grade: B (two resume audit field experiments + survey beliefs matched to outcomes; KR base rate is national statistics)
lane: "@behavioral-career"
locale: universal
as_of: 2013-2014 audits (US, Sweden) / 2021 beliefs study (US) / KR May 2026 survey
contested: yes
sources:
  - "Kroft, K., Lange, F. and Notowidigdo, M. J. (2013). Duration Dependence and Labor Market Conditions: Evidence from a Field Experiment. The Quarterly Journal of Economics 128(3), 1123-1167. https://doi.org/10.1093/qje/qjt015"
  - "Eriksson, S. and Rooth, D.-O. (2014). Do Employers Use Unemployment as a Sorting Criterion When Hiring? Evidence from a Field Experiment. American Economic Review 104(3), 1014-1039. https://doi.org/10.1257/aer.104.3.1014"
  - "Mueller, A. I., Spinnewijn, J. and Topa, G. (2021). Job Seekers' Perceptions and Employment Prospects: Heterogeneity, Duration Dependence, and Bias. American Economic Review 111(1), 324-363. https://doi.org/10.1257/aer.20190808 -- figures read in NBER w25294"
  - "국가데이터처 사회통계국 고용통계과 (2026-07-23). 2026년 5월 경제활동인구조사 청년층 부가조사 결과. read at the KDI 경제정책정보센터 record https://eiec.kdi.re.kr/policy/materialView.do?num=284575"
  - "work-career/entry-overconfidence-018"  # same self-prediction error, founders
  - "task-management/planning-fallacy-own-estimates-001"  # own-duration estimates run short
decision_rules:
  - rule: gap-clock
    when: the owner is out of work and searching
    do: treat roughly the first 8-9 months as the window where a current gap starts to count against callbacks; front-load applications and keep some dated activity on the record
    never: state a month on which the owner becomes unemployable; the thresholds come from two audits in US and Swedish markets
    basis: Kroft et al. 2013 (most of the callback decline in the first eight months); Eriksson and Rooth 2014 (contemporary spells of at least nine months penalised, short spells not)
    basis_grade: B
  - rule: past-gap-fades
    when: the owner worries about an old gap on the CV that was followed by work
    do: say that in the Swedish audit a past long spell followed by work did not affect hiring decisions
    never: claim no employer ever asks about it
    basis: Eriksson and Rooth 2014
    basis_grade: B
  - rule: own-odds-optimistic
    when: the owner estimates how long the search will take or how likely an offer is soon
    do: accept the estimate as informative but expect it to be too optimistic the longer the search has run; plan money and fallback on a longer horizon than stated
    never: tell the owner their estimate is worthless; elicited beliefs did predict job finding
    basis: Mueller et al. 2021 (beliefs predictive, unbiased at the start, not revised down, over-optimistic for the long-term unemployed)
    basis_grade: B
  - rule: kr-first-job-baseline
    when: a Korean graduate asks how long getting a first job normally takes
    do: give 11.2 months as the national average for those whose first job was a wage job (May 2026 survey), as an average, not a deadline
    never: present it as a typical or expected individual duration, or for career changers
    basis: 국가데이터처 2026-07-23
    basis_grade: A
  - rule: slack-market-softer
    when: the owner's field or region is visibly in a downturn
    do: say a gap is a weaker negative signal when many people are out of work
    never: quantify the softening
    basis: Kroft et al. 2013 (duration dependence stronger in tighter local markets)
    basis_grade: B
refraction_notes:
  - note: >
      MECHANISM IS CONTESTED, DIRECTION IS NOT. Audit studies show employers
      call back fewer applicants with longer current gaps (screening).
      Mueller et al. find that most of the observed decline in job finding
      can be explained by which seekers remain in the pool. Both can be true;
      the owner-facing advice (search early, keep the record active, do not
      assume your own odds are unchanged) holds under either.
    grade: B
  - note: >
      THE 11.2 MONTHS IS NARROW. It covers 15-29-year-old graduates whose first
      job after their final schooling was a wage job, averaged over the
      whole group. It is not a career-changer figure and not a forecast for
      one person. The Korean audit equivalent (does a gap reduce callbacks
      here) was not found; the 8-9 month thresholds are US and Swedish.
    grade: C
claim: >
  Three measured facts about the length of a job search. (1) A CURRENT gap
  costs callbacks, early: in a resume audit sending fictitious CVs to real
  postings in 100 US cities, the chance of an interview callback fell
  significantly with the length of the current unemployment spell, with most
  of the decline in the first eight months, and the penalty was stronger in
  tighter local labour markets (Kroft et al. 2013). In a Swedish audit,
  employers did not treat short current spells differently but penalised
  current spells of at least nine months (Eriksson and Rooth 2014). (2) A
  PAST gap that was followed by work did not matter for hiring decisions in
  the Swedish audit -- subsequent experience erased the signal. (3) Job
  seekers' own odds drift optimistic: in two US surveys (the New York Fed
  Survey of Consumer Expectations and the Krueger-Mueller survey), elicited
  job-finding beliefs strongly predicted actual job finding and were roughly
  unbiased at the start of a spell, but were not revised down while the
  search continued, so the long-term unemployed substantially over-estimated
  their chances (Mueller et al. 2021). The same paper attributes most of the
  fall in job finding over a spell to dynamic selection rather than to the
  spell itself, which is why the mechanism is contested. Korean base rate,
  national statistics: among young graduates whose first job was a wage job,
  the average time from graduation to that job was 11.2 months in the May
  2026 youth supplementary survey (국가데이터처, 2026-07-23).
reasoning: >
  The two audits are randomised field designs in which only the gap varies,
  so the direction "a long current gap costs callbacks" sits at the strong
  band. The beliefs result is observational but compares stated beliefs with
  realised outcomes in the same people, and it is published in the AER with
  no rebuttal located. The item ships contested because the two literatures
  disagree on how much of the observed duration effect is employer behaviour
  versus selection -- the advice does not depend on settling it, the size
  of any causal penalty does. The Korean figure is official statistics and
  would be top-band on its own; it is narrow in scope (young graduates, first
  wage job) and the warehouse found no Korean audit of gap penalties, which
  is recorded in GAPS.md. Callbacks are not offers and not pay: none of these
  audits measures the wage consequence of a gap.
---

# work-career/job-search-duration-signal-071 -- 구직 기간이 길어질 때 일어나는 일

**한 줄 그림:** 지금 쉬는 기간이 길어지면 서류 회신이 줄고, 그 감소는 앞쪽 몇 달에 몰린다. 본인의
취업 전망은 시간이 갈수록 실제보다 낙관적으로 남는다. 과거의 공백은 그 뒤 경력이 있으면 지워진다.

## What is measured

- **Current gap, early cost.** US audit (100 cities): callbacks fall with
  the current spell, most of the fall within the first eight months;
  stronger when the local market is tight. Swedish audit: short current
  spells not penalised, spells of nine months or more penalised.
- **Past gap, erased by later work.** Swedish audit: a long past spell
  followed by work did not change hiring decisions.
- **Own odds drift optimistic.** US surveys: beliefs predict job finding and
  start out unbiased, but do not come down as the search runs on, so
  long-term searchers over-estimate their chances.
- **Korea, first job.** Young graduates whose first job was a wage job took
  11.2 months on average (May 2026).

Contested: how much of the duration effect is employers screening on the
gap and how much is who is left in the pool. The advice below holds either
way; any number for the causal penalty does not.

## Rules for the answer path

| Rule | When | Do | Grade |
|---|---|---|---|
| gap-clock | out of work, searching | first ~8-9 months matter most; front-load, keep dated activity | B |
| past-gap-fades | worried about an old gap followed by work | in the audit it did not matter | B |
| own-odds-optimistic | owner estimates search length | plan cash and fallback on a longer horizon | B |
| kr-first-job-baseline | Korean graduate, first job | 11.2 months average, not a deadline | A |
| slack-market-softer | field or region in a downturn | gap is a weaker signal; do not quantify | B |

## 한국어 요약 (답변용)

- 지금 쉬고 있는 기간이 길어질수록 서류 회신이 줄어든다. 미국 실험에서는 감소의 대부분이 처음 8개월
  안에 일어났고, 스웨덴 실험에서는 9개월 이상 쉰 경우부터 불이익이 보였다. 그래서 구직 초반에 지원을
  몰아서 하고, 이력에 날짜가 찍히는 활동(단기 일, 교육, 프로젝트)을 이어 두라고 권한다. 다만 "몇 개월이
  지나면 끝"이라는 식으로 말하지 않는다. 한국에서 같은 실험은 찾지 못했다.
- 예전에 오래 쉬었어도 그 뒤에 일한 경력이 있으면, 스웨덴 실험에서는 채용 판단에 영향이 없었다.
- 본인이 예상하는 취업 시기는 쓸모 있는 정보지만, 구직이 길어질수록 실제보다 낙관적으로 남는다.
  생활비와 대안은 본인이 말한 기간보다 길게 잡고 계획하도록 돕는다.
- 한국 기준값: 2026년 5월 청년층 부가조사에서 졸업 후 첫 일자리가 임금근로자인 청년은 첫 취업까지 평균
  11.2개월 걸렸다. 평균이지 개인 기한이 아니고, 이직·경력 전환에는 쓰지 않는다.
- 업계나 지역 전체가 어려울 때는 공백이 덜 불리한 신호가 된다. 얼마나 덜한지는 숫자로 말하지 않는다.
- 공백이 회신을 줄이는 이유가 회사의 판단인지, 남아 있는 사람들의 구성 때문인지는 연구끼리 다툼이
  있다. 조언은 어느 쪽이든 같다.
