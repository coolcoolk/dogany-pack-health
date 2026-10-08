---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# Split out from item 002 on purpose: this is the single most operationally
# relevant measurement fact for an agent reading a real daily log.
id: spending-saving/diary-attrition-zero-reporting-003
domain: spending-saving
grade: B (benchmark comparison against national accounts, single national instrument)
lane: "@household-behavioral"
locale: US
as_of: 2012 (analysis window ending 2010)
contested: no
sources:
  - "Bee, A., Meyer, B. D. and Sullivan, J. X. (2015). The Validity of Consumption Data: Are the Consumer Expenditure Interview and Diary Surveys Informative? In Improving the Measurement of Consumer Expenditures, University of Chicago Press, 204-240. https://doi.org/10.7208/chicago/9780226194714.003.0008 (working-paper text read at NBER WP 18308, https://doi.org/10.3386/w18308)"
  - "source:spending-saving/self-report-spending-error-not-uniform-002 -- the general measurement item this one specialises"
refraction_notes:
  - note: >
      This is a US instrument (the Consumer Expenditure Diary Survey) with a
      fixed two-week recording window and a paid, recruited respondent panel. A
      voluntarily kept personal ledger differs on motivation, duration and
      granularity, so the MECHANISM (recording effort decays into omission, and
      omission looks like a zero) transfers while the rates do not.
    grade: C
claim: >
  When a diary-style spending record degrades, it degrades by producing ZEROS,
  not by producing smaller numbers. Bee, Meyer and Sullivan compared the US
  Consumer Expenditure Interview and Diary surveys separately against national
  income account data and report that the results are markedly less encouraging
  for the Diary component: there is no large Diary category that is both
  measured well AND reported at a higher rate than in the Interview survey.
  They further report much greater dispersion in Diary spending than Interview
  spending, that Diary respondents are much more likely to report ZERO spending
  for a given consumption category, and that a high and INCREASING fraction of
  Diary respondents report zero for ALL categories. Their conclusion is that
  using Diary data to assess inequality trends and other distributional
  outcomes is likely to lead to biased and misleading results. Separately, the
  Consumer Expenditure Survey is broadly representative on observable
  characteristics but shows strong under-representation at the top of the income
  distribution and under-reporting of income and expenditures at the top.
reasoning: >
  This is graded at the strong empirical band rather than the top because it is
  one national instrument benchmarked against one set of national accounts,
  where item 002's top-band status rests on convergence across three
  independent benchmark comparisons. It is broken out as its own item because
  its operational consequence is different from, and sharper than, the general
  measurement claim. For an agent reading a ledger of daily entries, the failure
  mode to watch for is not "the amounts look low." It is "a category went
  quiet," and then "a day went quiet," and then "a week went quiet" -- and each
  of those renders in a naive analysis as a genuine reduction in spending. A
  zero produced by not logging is indistinguishable from a zero produced by not
  spending unless the agent explicitly models logging effort as a separate
  variable. Any month-over-month comparison that does not first check entry
  COUNT and coverage alongside entry AMOUNT is measuring diary fatigue and
  calling it progress.
---

# spending-saving/diary-attrition-zero-reporting-003

The way a spending diary fails is worth knowing precisely, because the failure
mimics success.

When the US national spending diary was benchmarked category by category
against national accounts, it came out worse than the interview-based survey on
essentially every front: no large category in the diary was both well measured
and better captured than in the interview. But the specific defect is the
interesting one. Diary responses show far more spread than interview responses,
diary respondents are much more likely to report zero spending in a given
category, and the share of respondents reporting zero across ALL categories is
both high and rising. The authors' own conclusion is blunt -- diary data used
for distributional questions will mislead.

The reason this matters for a personal ledger is that a diary's error is not a
shrunken number, it is an absent one. Somebody who stops logging their coffee
does not log smaller coffees. They log nothing, and the category reads zero. To
anything computing a trend, that is a spending reduction. It looks exactly like
the outcome the person was hoping for, which is the worst possible property for
a measurement error to have.

The practical rule is to treat coverage as a first-class number. Before saying
a category fell, check whether entries fell. Before saying a month improved,
check how many days in it have any entry at all. A quiet category is a hypothesis
about recording before it is a conclusion about behaviour.

Two limits: this is a US instrument with a short fixed recording window and
recruited respondents, so the mechanism travels and the rates do not; and the
same survey under-represents and under-reports at the top of the income
distribution, which is a separate bias from the diary problem and not fixed by
watching coverage.
