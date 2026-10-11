---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (work-career GAPS sprint, dispatch
# kw-work-newitems). Skill SIGNALLING: what makes a skill visible to an
# employer, separated from whether the skill exists. Three randomised field
# designs where only the signal varies. Sits next to 001 (what predicts
# performance once hired) -- this row is about getting seen at all.
# Read at source 2026-10-06: Pallais NBER w18917 full text (abstract and
# results section; AER version cited); Athey and Palikot arXiv 2405.00247v2
# html (abstract, funding and collaboration note, data section); Deming et al.
# NBER w20528 rev1 full text (abstract and introduction; AER version cited).
# COI note: Athey and Palikot ran the experiment WITH Coursera staff on
# Coursera's platform; funding was a Stanford GSB lab, and the outcome is read
# from LinkedIn profiles, not from Coursera. Kept as a source, labelled as a
# working paper with platform collaboration, and not load-bearing alone.
# Rubric: work-career.rubric.md @behavioral-career row
# work-career/skill-signal-verified-record-072.
id: work-career/skill-signal-verified-record-072
domain: work-career
grade: B (randomised field experiments, online platforms and US resume audit; one leg is an unrefereed working paper)
lane: "@behavioral-career"
locale: universal
as_of: 2013-2014 platform experiment / 2016 resume audit / 2022-2023 credential-sharing experiment
contested: no
sources:
  - "Pallais, A. (2014). Inefficient Hiring in Entry-Level Labor Markets. American Economic Review 104(11), 3565-3599. https://doi.org/10.1257/aer.104.11.3565 -- figures read in NBER w18917 (2013), https://www.nber.org/papers/w18917"
  - "Athey, S. and Palikot, E. The Value of Non-Traditional Credentials in the Labor Market. Working paper, arXiv 2405.00247 v2. https://arxiv.org/abs/2405.00247 -- run in collaboration with Coursera staff; AEA RCT registry AEARCTR-0009438"
  - "Deming, D. J., Yuchtman, N., Abulafi, A., Goldin, C. and Katz, L. F. (2016). The Value of Postsecondary Credentials in the Labor Market: An Experimental Study. American Economic Review 106(3), 778-806. https://doi.org/10.1257/aer.20141757 -- read in NBER w20528 rev1"
  - "work-career/selection-validity-recalibrated-001"  # what predicts performance once hired; work samples and job knowledge
  - "work-career/job-search-duration-signal-071"  # a dated record also blunts the gap signal
decision_rules:
  - rule: third-party-record-first
    when: the owner asks how to show a skill they have no job title for
    do: steer toward a record someone else issues or can check (a paid project with a rating or reference, a public work sample, a completed and listed credential) over a self-description of the skill
    never: promise a callback or pay effect; the measured gains are platform- and market-specific
    basis: Pallais 2014 (a hired job plus a public evaluation raised later employment and earnings for inexperienced workers)
    basis_grade: B
  - rule: weak-signal-gains-most
    when: deciding whether a certificate or small project is worth doing
    do: say the signal adds most where the CV has least else to show (no degree, no related experience) and little where strong signals already exist
    never: tell an experienced candidate a certificate will move them
    basis: Pallais 2014 (no effect for experienced workers); Athey and Palikot (bottom-tercile gains ~12 percent, top tercile negligible)
    basis_grade: B
  - rule: make-it-visible
    when: the owner has finished a course or credential
    do: suggest listing it where employers look (profile, CV) promptly; in one trial merely prompting people to post it raised new employment
    never: quote the 6 percent as a general effect of certificates
    basis: Athey and Palikot (working paper, platform collaboration)
    basis_grade: C
  - rule: issuer-matters-unless-licensed
    when: choosing where to get a credential for a job that does not require a licence
    do: note the issuer's reputation changes how the same credential reads; where a licence is required the licence is what counts
    never: name specific institutions as good or bad on this evidence
    basis: Deming et al. 2016 (for-profit online BA 22 percent fewer callbacks; for-profit health certificate 57 percent fewer where no certificate required; no difference where certificate plus licence required)
    basis_grade: B
  - rule: detail-cuts-both-ways
    when: the owner can choose a detailed versus a bare reference or rating
    do: a detailed public evaluation helps strong performers and hurts weak ones; advise detail only where the work was good
    never: advise hiding or misrepresenting an evaluation
    basis: Pallais 2014
    basis_grade: B
refraction_notes:
  - note: >
      SIGNAL, NOT SKILL. Each design holds the worker or the CV fixed and
      varies only what an employer can see. They show visibility changes
      hiring; they do not show that courses or certificates build skill.
      Speak them as "shows it", never as "teaches it".
    grade: B
  - note: >
      KOREA IS NOT MEASURED. No Korean experiment on 자격증, 포트폴리오 or
      online certificates was read; Korean 공채 screening can run on
      formal 자격증 lists, which is a different mechanism from these
      platform and audit settings. The direction (verified beats claimed,
      weak CVs gain most) is the transferable part; no number transfers.
    grade: C
claim: >
  What makes a skill visible to employers has been randomised, and three
  results hold. (1) A first verified record is worth more than the skill
  unseen: on an online labour platform, Pallais hired 952 randomly selected
  workers for a short job and gave them public evaluations; among workers
  with no prior platform experience, the job plus a coarse public rating
  raised the share with any work in the next two months from 12 to 30
  percent and average earnings from about 10 to 27 dollars, and raised their
  posted wage by about 10 percent, with no effect for already-experienced
  workers. A more detailed evaluation helped good performers and hurt poor
  ones. (2) Making a credential visible helps most those with the weakest
  other signal: in a randomised trial with over 800,000 online-certificate
  earners, mostly from developing countries and without degrees, a prompt
  and a one-click path to post the certificate on LinkedIn raised new
  employment by about 6 percent (1.0 percentage point) in a tracked subsample
  of about 40,000, concentrated in the bottom tercile of baseline
  employability (about 12 percent) and negligible in the top tercile (Athey
  and Palikot, working paper run with Coursera staff). (3) The issuer of a
  credential changes how it reads where no licence is required: in a US
  resume audit, a business BA from a for-profit online institution got 22
  percent fewer callbacks than the same degree from a non-selective public
  institution, and a for-profit health certificate got 57 percent fewer for
  health jobs that did not require a certificate; there was no difference
  for health jobs requiring both a certificate and a licence (Deming et al.
  2016). Shape for advice: a checkable third-party record beats a
  self-claim, it matters most when the CV is thin, and where a licence
  governs entry the licence is the signal.
reasoning: >
  Graded at the strong empirical band because each leg randomises the signal
  in a real hiring market: Pallais by hiring and rating workers, Athey and
  Palikot by randomising the posting prompt, Deming et al. by randomising
  the credential on otherwise identical CVs. Not higher: two of the three
  are online-platform settings, the audit measures callbacks rather than
  offers or pay, the credential-sharing trial is an unrefereed working
  paper run with the platform whose product it studies, and none is Korean.
  The make-it-visible rule rests on that working paper alone and is
  therefore C. Checked against item 001 so the two do not blur: 001 is about
  which predictors forecast performance after hire; this row is about which
  signals get a candidate considered, a different question with a
  different evidence base. Self-presentation advice that circulates without
  a randomised test (resume formats, keyword tricks, personal branding) was
  not shipped.
---

# work-career/skill-signal-verified-record-072 -- 실력을 보이게 만드는 것

**한 줄 그림:** 실력이 있다는 말보다 남이 확인해 줄 수 있는 기록이 낫다. 그 효과는 이력서가 빈약할수록
크고, 면허가 필요한 일에서는 면허가 곧 신호다.

## What was randomised

- **First verified record.** Online platform, 952 workers hired at random
  for a short job and publicly rated. For newcomers, any work in the next
  two months rose from 12 to 30 percent and earnings roughly tripled;
  experienced workers saw no effect. Detailed ratings helped good
  performers and hurt poor ones.
- **Posting the credential.** 800,000+ online-certificate earners, mostly
  without degrees: a prompt to post the certificate on LinkedIn raised new
  employment about 6 percent, mostly for those with the weakest CVs.
  Working paper, run with the platform.
- **Who issued it.** US resume audit: the same degree or certificate from a
  for-profit online institution drew 22 to 57 percent fewer callbacks --
  except for jobs needing a licence, where there was no difference.

These show that being SEEN changes hiring. They do not show that a course
builds the skill.

## Rules for the answer path

| Rule | When | Do | Grade |
|---|---|---|---|
| third-party-record-first | skill without a job title | a rated project, reference or public work sample over a self-description | B |
| weak-signal-gains-most | is a certificate worth it | most for thin CVs, little for strong ones | B |
| make-it-visible | finished a credential | list it where employers look | C |
| issuer-matters-unless-licensed | choosing a credential source | issuer reputation matters unless a licence governs entry | B |
| detail-cuts-both-ways | detailed vs bare reference | detail helps only if the work was good | B |

## 한국어 요약 (답변용)

- 실력을 "할 줄 안다"고 쓰는 것보다, 남이 확인할 수 있는 기록(평가가 붙은 실제 작업, 추천인, 공개된
  작업물, 이수한 자격)을 만드는 쪽을 권한다. 온라인 플랫폼 실험에서 경력 없는 사람을 무작위로 한 번
  고용해 공개 평가를 남겨 주자, 이후 두 달 안에 일을 구한 비율이 12%에서 30%로 올랐다.
- 이 효과는 이력서에 내세울 게 적은 사람에게 크고, 이미 경력이 탄탄한 사람에게는 거의 없다. 경력자에게
  "자격증 하나 따면 달라진다"고 말하지 않는다.
- 딴 자격은 고용주가 보는 곳(이력서, 프로필)에 바로 올리라고 권한다. 한 실험에서 올리도록 알림만 줘도
  새 취업이 약 6% 늘었다. 다만 플랫폼과 함께 한 미발표 연구라 일반적인 자격증 효과로 인용하지 않는다.
- 같은 학위·수료증이라도 어디서 받았는지에 따라 서류 회신이 달랐다. 단, 면허가 필요한 직무에서는
  차이가 없었다. 면허가 진입 조건인 일이라면 면허가 곧 신호다. 특정 기관을 좋다·나쁘다로 평가하지 않는다.
- 상세한 평가나 추천서는 일을 잘했을 때만 도움이 된다. 못한 일에 대해서는 오히려 손해다.
- 이 연구들은 "보이게 하면 채용이 달라진다"는 것이지 "강의가 실력을 키운다"는 것이 아니다. 한국의
  자격증·포트폴리오 실험은 찾지 못했으므로 방향만 옮기고 숫자는 옮기지 않는다.
