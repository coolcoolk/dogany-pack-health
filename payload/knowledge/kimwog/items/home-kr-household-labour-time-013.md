---
# Kimwog warehouse #1. HOME-DOMAIN OPENING SPRINT 2026-09-02
# (marker: home-lane-opening-001-013). KR-LOCALE. The only MEASUREMENT item in
# the 가사노동 lane: how much household labour actually costs, from the national
# statistical office rather than from a productivity blog.
id: home/kr-household-labour-time-013
domain: home
lane: "@household-labor"
grade: B
locale: KR
as_of: 2024
contested: no
sources:
  - "https://www.korea.kr/briefing/policyBriefingView.do?newsId=156700368"  # Statistics Korea (통계청), 2024 생활시간조사 결과 (2024 Time Use Survey), official government release carried on the government policy-briefing portal. Read at source 2026-09-02
  - "source:home/cleaning-agents-lung-function-009"  # within-warehouse cross-ref: who does the work is directly relevant to a finding that appeared only in the group doing it
claim: >
  Household labour in Korean dual-income households is measured, large and
  unequally split. Statistics Korea's 2024 Time Use Survey reports that in
  dual-income (맞벌이) households the husband spent 1 hour 24 minutes a day on
  household labour and the wife 3 hours 32 minutes. Compared with five years
  earlier the husband's figure rose by 13 minutes and the wife's fell by 17, so
  the gap narrowed from 2 hours 38 minutes to 2 hours 8 minutes -- a change of
  roughly 30 minutes over five years. Two readings follow and both matter. As a
  PLANNING input: household labour in a dual-income Korean home is a multi-hour
  daily block, not a residual, and any schedule or routine that treats it as
  slack time is mis-costed by hours. As a TREND: the gap is closing at
  approximately six minutes per year, and closing partly because the wife's
  hours fell rather than only because the husband's rose. Do not narrate the
  narrowing as redistribution without saying which side moved.
reasoning: >
  This is a national statistical product, not a study, and it is graded for what
  that is worth. Strengths: the sampling frame and instrument are serious --
  roughly 12,750 sample households and about 25,000 residents aged 10 and over,
  recording activity in 10-minute intervals across two days, with the 2024 round
  covering all four seasons including spring for the first time. That is a time
  DIARY, which is the measurement method that does not suffer the recall bias
  that ruins survey questions of the form how many hours do you spend on
  housework. It sits one rung below the top of the ladder because it is a
  descriptive population measurement rather than an established causal or
  converged-consensus claim, and because a single national round is a snapshot
  whose category boundaries are the statistical office's own. Read at the
  official government release rather than at any of the newspaper write-ups,
  which quote several different and non-interchangeable figures from the same
  publication.
refraction_notes:
  - note: >
      CATEGORY BOUNDARY NOT VERIFIED AT DEFINITION LEVEL, and this is why
      conflicting numbers circulate from the same release. Korean coverage of
      this survey quotes both a 가사노동 (household labour) figure and a smaller
      가정관리 (household management) figure for the same population, and the two
      are not interchangeable. The figures carried here are the 가사노동 ones
      from the official release. The precise statistical composition of that
      category was not read at source in this pass, so do not convert between
      the two, and do not compare this figure to a foreign statistic without
      checking that the categories match.
    grade: C
  - note: >
      A POPULATION AVERAGE IS NOT A PERSONAL BUDGET. These are means over a
      national sample. Household size, children, housing type and outsourcing
      all move an individual figure enormously. Use this to establish that the
      cost is measured in hours per day, not to tell any specific household what
      its own number is.
    grade: B
  - note: >
      READ THE DIRECTION OF THE NARROWING HONESTLY. The gap fell by about 30
      minutes over five years, but the wife's hours fell by 17 minutes while the
      husband's rose by 13. Roughly half the convergence came from less work
      being done on one side rather than more being taken up on the other.
      Stating only the narrowing is technically true and materially misleading.
    grade: B
  - note: >
      NOT COVERED: what any of this does to anybody. This is a time
      measurement. It carries no health, satisfaction, or relationship outcome,
      and none should be inferred from it. The one place it connects to an
      outcome in this warehouse is item 009, where an exposure effect appeared
      in the group doing the cleaning -- and that connection is a reason to be
      careful, not a finding.
    grade: D
---

# home/kr-household-labour-time-013

Household labour is the largest un-costed line item in most people's week, and
Korea happens to measure it properly.

Statistics Korea's 2024 Time Use Survey puts household labour in dual-income
households at 1 hour 24 minutes a day for the husband and 3 hours 32 minutes for
the wife. Five years earlier the husband's figure was 13 minutes lower and the
wife's was 17 minutes higher, so the gap has come down from 2 hours 38 minutes
to 2 hours 8 minutes.

The method is worth knowing, because it is the reason to trust these numbers
more than any survey answer on the same topic. This is a time diary: about
12,750 sample households, roughly 25,000 people aged ten and over, recording
what they were doing in ten-minute intervals across two days, with the 2024
round covering all four seasons. Nobody was asked to estimate how many hours a
week they spend on housework, which is a question humans answer badly. They
wrote down what they were doing.

Two things to take from it.

As a planning input: in a dual-income Korean household, this is a multi-hour
daily block. Any routine, schedule or plan that treats housework as the slack
between real activities is mis-costed by hours per day, and mis-costed
asymmetrically between the two people in it.

As a trend, read carefully. The gap narrowed by about half an hour over five
years, which sounds like redistribution. Roughly half of that came from the
wife's hours falling, not from the husband's rising. Reporting only the
narrowing is true and misleading at the same time.

Three limits.

Korean coverage of this same release quotes more than one number, because the
survey has both a household-labour category and a narrower household-management
category, and they are not interchangeable. The figures here are the
household-labour ones from the official release. The exact statistical
composition of that category was not read at definition level in this pass, so
do not convert between them and do not compare against a foreign statistic
without checking the categories line up.

These are population means. Children, housing type, household size and paid help
move an individual number enormously. This establishes the order of magnitude,
not anybody's personal budget.

And it is a time measurement and nothing else. It carries no health,
satisfaction or relationship outcome, and none should be read into it. The one
adjacent finding in this warehouse is item 009, where a respiratory exposure
effect showed up in the group actually doing the cleaning. That is a reason for
care, not a conclusion.
