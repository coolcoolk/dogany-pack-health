---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Every source below was resolved and read during authoring; no citation is
# reconstructed from memory.
# Lane-anchor item: the measurement half of the lane, and the direct twin of
# nutrition/self-report-underreporting-007.
id: spending-saving/self-report-spending-error-not-uniform-002
domain: spending-saving
grade: A (field-methodology)
lane: "@household-behavioral"
locale: universal
as_of: 2009-2014 (US and Tanzania validation windows)
contested: no
sources:
  - "Bee, A., Meyer, B. D. and Sullivan, J. X. (2015). The Validity of Consumption Data: Are the Consumer Expenditure Interview and Diary Surveys Informative? In Improving the Measurement of Consumer Expenditures, University of Chicago Press, 204-240. https://doi.org/10.7208/chicago/9780226194714.003.0008 (working-paper text read at NBER WP 18308, https://doi.org/10.3386/w18308)"
  - "Zinman, J. (2009). Where Is the Missing Credit Card Debt? Clues and Implications. Review of Income and Wealth 55(2), 249-265. https://doi.org/10.1111/j.1475-4991.2009.00321.x"
  - "Beegle, K., De Weerdt, J., Friedman, J. and Gibson, J. (2012). Methods of household consumption measurement through surveys: Experimental results from Tanzania. Journal of Development Economics 98(1), 3-18. https://doi.org/10.1016/j.jdeveco.2011.11.001"
  - "Browning, M., Crossley, T. F. and Winter, J. (2014). The Measurement of Household Consumption Expenditures. Annual Review of Economics 6, 475-501. https://doi.org/10.1146/annurev-economics-080213-041247"
refraction_notes:
  - note: >
      The validation evidence is US survey instruments benchmarked against US
      national accounts, plus one randomised survey-design experiment in
      Tanzania. The DIRECTION and the MECHANISM travel. The specific ratios do
      not transfer to a Korean-language personal ledger, and no Korean
      validation of a consumer spending log against an external benchmark was
      located in this pass.
    grade: C
  - note: >
      A personal ledger is a DIARY instrument, not a recall survey. That is the
      relevant comparison class, and it is the one the evidence treats least
      kindly on completeness even while treating it kindly on recency. Do not
      import recall-survey error rates onto a daily log, and do not import diary
      completeness findings onto a monthly self-estimate.
    grade: B
claim: >
  Self-reported household spending is mis-measured, but NOT by a uniform
  downward shift, and the popular "people underestimate everything they spend"
  framing is wrong in a way that matters operationally. Three separable
  findings. (1) INSTRUMENT DEPENDENCE: Beegle et al. (2012) randomised eight
  alternative consumption-measurement methods in Tanzania and found significant
  differences between the benchmark personal diary and every other diary and
  recall format; recall modules measured LOWER consumption than a personal
  diary, with larger gaps among poorer households and among households with
  more adult members, and under-reporting was particularly apparent for
  illiterate households and for urban respondents completing a HOUSEHOLD
  (rather than personal) diary. The measured error is therefore a property of
  the instrument and the respondent, not a constant. (2) CATEGORY DEPENDENCE:
  Bee, Meyer and Sullivan report that most of the LARGEST consumption
  categories are measured well in the US Consumer Expenditure Interview Survey,
  with the ratio to national-account data close to one and not declining
  appreciably over time, while several other large categories are reported at a
  low rate or have seen that ratio decline. So a total can be accurate while
  specific categories are badly off. (3) FLOW VERSUS STOCK: Zinman (2009) finds
  that Survey of Consumer Finances and industry data match up well on credit
  card CHARGES and fairly well on account totals, but that the survey always
  yields much lower estimates of revolving DEBT, with an estimated lower bound
  for the 2004 discrepancy of half the industry-implied total and some evidence
  the gap has grown. People report what they SPENT far better than what they
  OWE. Both Bee et al. and Zinman additionally report that under-reporting is
  concentrated at the top of the income distribution.
reasoning: >
  This sits at the top of the lane because the error is measured against an
  EXTERNAL benchmark rather than inferred from one self-report against another:
  national income accounts, credit-card industry aggregates, and a randomised
  experiment in survey design. That is the same evidentiary move that puts
  nutrition/self-report-underreporting-007 at the top of its lane -- recovery
  biomarkers there, administrative and industry aggregates here -- and it is
  why this item, not any behavioural finding, is the lane anchor. The
  operational consequence for an agent reading a real spending log is precise
  and is the reason the item refuses the simpler story: the correct default is
  NOT to inflate the user's totals by a correction factor. The correct default
  is to trust the grand total more than any single category, to trust logged
  outflow more than any stated balance or debt, and to treat a suspiciously
  clean category as an instrument failure before treating it as a behaviour
  change.
---

# spending-saving/self-report-spending-error-not-uniform-002

Everything a person writes down about money is measured with error, but the
error is not the simple one that gets repeated. It is not "people undercount
their spending by roughly a third." The error is structured, and the structure
is what an agent reading a real ledger has to work with.

The first structure is the instrument. A randomised experiment that gave
households eight different ways of recording the same consumption found real
differences between all of them, and found that asking people to recall
spending produced lower totals than having them keep a personal diary. The gap
was larger for poorer households and for households with more adults in them,
and the household-level diary broke down for respondents who could not read
easily and for urban respondents. None of this is a fixed bias that could be
corrected with a multiplier; it is the recording method interacting with the
person.

The second structure is the category. Benchmarked against national accounts,
the largest categories of US household spending come through survey reporting
roughly intact, and have not degraded much over decades. Several other large
categories come through badly, or have degraded. So a total can be close to
right while the breakdown underneath it is wrong -- which is the opposite of
the intuition that the details are solid and only the sum drifts.

The third structure is the difference between what you spend and what you owe.
Compared against credit-card industry data, household surveys get charges
roughly right and account counts roughly right, and then miss about half of
revolving debt. People are decent reporters of outflow and poor reporters of
their own liabilities.

What follows for reading a log. Trust the total more than the category split.
Trust the logged outflow more than any figure the person states about a balance
or a debt. And when a category suddenly looks clean, suspect the recording
before you congratulate the behaviour. Two limits are worth carrying openly:
the validation work is US and Tanzanian, so the direction transfers and the
magnitudes do not, and no Korean study benchmarking a consumer spending log
against an external source was found.
