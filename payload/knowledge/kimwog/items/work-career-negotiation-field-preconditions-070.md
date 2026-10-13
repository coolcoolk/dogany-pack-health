---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (work-career GAPS sprint, dispatch
# kw-work-newitems). Closes part of the v20 negotiation gap: item 007 is
# laboratory-dominated; this row carries the FIELD evidence on when salary
# bargaining happens at all, what makes people ask, and how wrong people are
# about their outside option. It does NOT supply a figure for what a
# negotiation is worth -- that refusal (v20 ledger) stands.
# Read at source 2026-10-06: Leibbrandt and List abstract (IDEAS/RePEc
# record); Jaeger et al. abstract (EconPapers record); Hall and Krueger
# NBER w14329 full text (survey section and summary), published version
# cited. No applicability.axes block: none of the moderators is on the axes
# ledger.
# decision_rules is structured data for an answer path or a future career
# module; each rule names the graded row it rests on. No program code reads
# it yet.
# Rubric: work-career.rubric.md @behavioral-career row
# work-career/negotiation-field-preconditions-070.
id: work-career/negotiation-field-preconditions-070
domain: work-career
grade: B (natural field experiment + representative survey + survey linked to administrative wage data; US and Germany)
lane: "@behavioral-career"
locale: universal
as_of: 2008 US survey / 2015 field experiment / 2024 German beliefs study
contested: no
sources:
  - "Leibbrandt, A. and List, J. A. (2015). Do Women Avoid Salary Negotiations? Evidence from a Large-Scale Natural Field Experiment. Management Science 61(9), 2016-2024. https://doi.org/10.1287/mnsc.2014.1994"
  - "Hall, R. E. and Krueger, A. B. (2012). Evidence on the Incidence of Wage Posting, Wage Bargaining, and On-the-Job Search. American Economic Journal: Macroeconomics 4(4), 56-67. https://doi.org/10.1257/mac.4.4.56 -- figures read in the working-paper version, NBER w14329 (2008), https://www.nber.org/papers/w14329"
  - "Jaeger, S., Roth, C., Roussille, N. and Schoefer, B. (2024). Worker Beliefs About Outside Options. The Quarterly Journal of Economics 139(3), 1505-1556. https://doi.org/10.1093/qje/qjae001"
  - "work-career/negotiation-context-bound-007"  # the laboratory and meta-analytic half; this row is the field half
  - "work-career/kr-seniority-wage-and-main-job-exit-014"  # why the US bargaining incidence does not transfer to Korean seniority-pay employers
decision_rules:
  - rule: establish-negotiability
    when: an offer or a pay conversation is coming and the owner has not said whether pay is negotiable
    do: treat whether pay is negotiable as a fact to find out, not a personality question; suggest asking directly whether the figure is open to discussion
    never: tell the owner they are or are not a negotiating type
    basis: Leibbrandt and List 2015 (explicit statement of negotiability removed the gender difference in negotiating)
    basis_grade: B
  - rule: outside-option-before-number
    when: the owner names a target or a walk-away figure for a raise or an offer
    do: ask what similar roles pay elsewhere before endorsing the figure; a figure anchored on the current wage is the documented error
    never: endorse a target derived only from the current salary
    basis: Jaeger et al. 2024 (beliefs about outside options anchored on the current wage; information about similar workers changed negotiation intentions)
    basis_grade: B
  - rule: low-pay-underestimates-more
    when: the owner is in a low-paying firm or role and reports little expected gain from moving
    do: flag that this group underestimates wages elsewhere most; suggest checking market data before concluding
    never: state a specific market wage the warehouse has not read
    basis: Jaeger et al. 2024
    basis_grade: B
  - rule: employed-search-leverage
    when: the owner is weighing whether to quit before searching
    do: note that a job the owner could keep is the bargaining position about 40 percent of US hires had; leaving first removes it
    never: present this as a measured pay premium; the survey measures incidence, not the gain
    basis: Hall and Krueger 2012 (about 39-40 percent of workers could have stayed in their earlier job)
    basis_grade: B
  - rule: posted-wage-sectors
    when: the job is unionised, public-sector, or a pay-scale (호봉) post
    do: say individual bargaining is rare in these settings and the lever is grade, step or role, not the starting number
    never: coach a counter-offer on a fixed scale as if it were a bargained wage
    basis: Hall and Krueger 2012 (individual bargaining rare for union and government workers); kr-seniority-wage-and-main-job-exit-014
    basis_grade: C
refraction_notes:
  - note: >
      INCIDENCE IS NOT VALUE. A third of US hires bargained, and bargaining
      rose with education from 26 to 75 percent. Neither number says what
      bargaining gained. Never convert these into "negotiating is worth X";
      the v20 refusal of any per-negotiation value figure stands.
    grade: B
  - note: >
      KOREA IS NOT MEASURED. No Korean incidence-of-bargaining survey was
      read. Large Korean employers commonly set entry pay by grade and step
      (item 014: seniority pay in 60.3 percent of establishments with 100+
      staff in 2017), so the US incidence is likely too high for a Korean
      공채 entry offer and unknown for 경력직 hires. Say so rather than
      transplanting the US share.
    grade: C
claim: >
  Field evidence on salary negotiation is about preconditions, and three
  preconditions are measured. (1) Bargaining is common but not universal,
  and it is structured by the job: in a representative 2008 US survey
  (Hall and Krueger; 2,513 interviewed, about 1,400 hired in the previous
  ten years), about a third of workers bargained before accepting their job;
  bargaining rose steeply with education, from 26 percent of those without a
  high-school diploma to 75 percent of those with professional degrees; it
  was rare for union and government workers; and about 39 to 40 percent of
  hires could have stayed in their earlier job, a stronger position than an
  unemployed searcher holds. (2) Whether people ask depends on whether the
  rules are stated: in a natural field experiment randomising nearly 2,500
  US job seekers across job ads, when there was no explicit statement that
  wages were negotiable men negotiated more and women more often signalled
  willingness to work for less; when the ad said wages were negotiable, the
  difference disappeared completely (Leibbrandt and List 2015). (3) People
  misjudge their outside option in a known direction: German workers
  anchored beliefs about pay elsewhere on their current wage -- workers who
  would see a 10 percent change by moving expected about 1 percent -- and
  workers in low-paying firms underestimated wages elsewhere; information on
  similar workers' pay corrected beliefs and changed stated job-search and
  negotiation intentions (Jaeger et al. 2024). Practical shape: find out
  whether pay is negotiable, check the market before naming a figure, and do
  not give up a job you could keep before you have an offer. None of these
  sources says how much a negotiation is worth.
reasoning: >
  Graded at the strong empirical band because each leg is either a
  randomised field design (Leibbrandt and List), a representative survey
  measuring incidence (Hall and Krueger), or survey beliefs compared against
  linked administrative wage data (Jaeger et al.), and each is reported at
  source with no live rebuttal located. Not higher: two countries, none of
  them Korea, and the intention changes in Jaeger et al. are stated
  intentions, not observed negotiations. This is the field companion to
  item 007, not a replacement: 007 says the gender gap in outcomes is small
  and moderated by information and experience in mostly laboratory data;
  this row shows the same information moderator operating on whether people
  ask at all, in the field. The decision_rules are routing rules over these
  rows and carry the grade of the row they cite; the posted-wage rule is C
  because it combines a US incidence finding with the Korean institutional
  row by inference.
---

# work-career/negotiation-field-preconditions-070 -- 연봉 협상, 현장 증거가 말하는 전제 조건

**한 줄 그림:** 협상은 성격 문제가 아니다. 협상이 되는 자리인지 먼저 확인하고, 다른 곳 시세를 확인한
다음 숫자를 말하고, 다닐 수 있는 직장을 먼저 버리지 않는다.

## What the field evidence shows

- **About a third bargain, and it depends on the job.** In a representative
  US survey (2008), about one hire in three bargained over pay. Bargaining
  rose from 26 percent (no high-school diploma) to 75 percent (professional
  degree) and was rare in union and government jobs.
- **People ask when they are told they may.** In a field experiment with
  nearly 2,500 real job seekers, the gender difference in negotiating
  appeared only when the job ad was silent about negotiability. Saying
  "wages are negotiable" made it disappear.
- **People underrate their outside option.** German workers who would gain
  about 10 percent by moving expected about 1 percent. Low-paid workers in
  low-paying firms underrated outside pay most. Showing them what similar
  workers earn changed their beliefs and their stated plans to search and
  negotiate.
- **A job you can keep is leverage.** About 40 percent of US hires could
  have stayed in their previous job when they accepted the new one.

What none of this says: how much negotiating is worth. That number is still
refused (v20 ledger).

## Rules for the answer path

| Rule | When | Do | Grade |
|---|---|---|---|
| establish-negotiability | offer or pay talk coming, negotiability unknown | ask whether the figure is open; it is a fact to find, not a trait | B |
| outside-option-before-number | owner names a target from the current salary | check what similar roles pay elsewhere first | B |
| low-pay-underestimates-more | low-paying firm, "moving won't help" | flag the documented underestimate; check data | B |
| employed-search-leverage | thinking of quitting before searching | a keepable job is the stronger position; not a measured premium | B |
| posted-wage-sectors | union, public, 호봉 post | the lever is grade/step/role, not the starting number | C |

## 한국어 요약 (답변용)

- 협상을 할지 말지는 성격이 아니라 그 자리의 규칙 문제다. 연봉이 조정 가능한지 먼저 직접 물어보라고
  권한다. 미국 현장 실험에서 공고에 "협상 가능"이라고 적혀 있으면 남녀 간 협상 시도 차이가 사라졌다.
- 목표 연봉을 지금 연봉에서만 끌어오면 안 된다. 독일 연구에서 사람들은 다른 곳 임금을 지금 임금에
  맞춰 짐작했고, 옮기면 10% 오를 사람이 1% 정도만 기대했다. 저임금 회사에 있을수록 더 낮게 짐작했다.
  숫자를 말하기 전에 비슷한 자리의 시세를 먼저 확인한다.
- 다니면서 구직하는 쪽이 협상 위치가 낫다. 미국 조사에서 입사자의 약 40%는 이전 직장에 남을 수 있는
  상태였다. 다만 이것이 연봉을 얼마 더 올려 준다는 측정치는 아니다.
- 공무원·노조·호봉제 자리는 개인 협상이 드물다. 이런 곳에서는 첫 연봉 숫자보다 직급·호봉·직무 배정이
  실제 지렛대다.
- 한국의 협상 빈도는 측정된 자료를 읽지 못했다. 대기업 공채 신입은 호봉·직급으로 정해지는 경우가 많아
  미국의 "3명 중 1명" 수치를 그대로 옮기지 않는다. 경력직은 모른다고 말한다.
- 협상 한 번이 평생 얼마의 가치라는 숫자는 근거가 없어 쓰지 않는다.
