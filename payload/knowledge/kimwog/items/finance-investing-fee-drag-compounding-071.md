---
# Finance GAPS sprint 2026-10-06 (dispatch kw-finance-newitems). The
# PER-INVESTOR fee arithmetic. Item 001 carries the market-wide identity
# (after costs, the average active dollar trails the average passive dollar)
# and French's aggregate bill; this row carries what a single holding's
# recurring fee does to a single user's ending balance over their horizon,
# which is the number a Dogany module can actually compute. Read at source on
# 2026-10-06: the SEC investor bulletin (text; its chart values are an image
# and were NOT read -- the worked figures below are recomputed from the
# bulletin's stated setup); the Carhart 1997 abstract record (full text not
# reachable, publisher 403).
#
# fee_drag is structured data: a pure formula plus the input rules. It
# produces a number only from the user's own fee and horizon (RESCALE-style
# arithmetic on item data); it never estimates a return.
id: finance-investing/fee-drag-compounding-071
domain: finance-investing
grade: A (field-methodology -- compounding arithmetic); B (higher expenses go with persistently worse fund results)
lane: "@quant-market"
locale: universal
as_of: 1997 / 2014 / formula timeless
contested: no
sources:
  - "US Securities and Exchange Commission, Office of Investor Education and Advocacy (2014). Investor Bulletin: How Fees and Expenses Affect Your Investment Portfolio. https://www.sec.gov/investor/alerts/ib_fees_expenses.pdf -- setup: 100,000 USD, 4 pct annual return, 20 years, ongoing fees of 0.25, 0.50 and 1 pct; mechanism stated in text: 'not only is your investment balance reduced by the fee, but you also lose any return you would have earned on that fee'. Fees come as transaction fees and ongoing fees."
  - "Carhart, M. M. (1997). On Persistence in Mutual Fund Performance. Journal of Finance 52(1), 57-82. https://ideas.repec.org/a/bla/jfinan/v52y1997i1p57-82.html -- common factors in stock returns and investment expenses almost completely explain persistence in equity fund returns; the only significant persistence is in the underperformance of the worst funds. Abstract record read; full text not reachable."
  - "finance-investing/active-arithmetic-cost-floor-001"  # within-warehouse: the market-wide identity this row localises to one holding
  - "finance-investing/fund-alpha-luck-vs-skill-002"  # within-warehouse: why a fee is rarely bought back by skill
  - "finance-investing/individual-trading-penalty-007"  # within-warehouse: transaction costs from the user's own turnover
fee_drag:
  formula_exact: "share_of_ending_balance_lost = 1 - ((1 + r - f) / (1 + r)) ^ T"
  formula_engine: "share_of_ending_balance_lost = 1 - (1 - f) ^ T"
  formula_note: "the engine form needs no return assumption and always slightly OVERSTATES the loss (conservative); over r 0 to 0.08, f up to 0.015, T up to 30 the overstatement is at most about 0.022 of the ending balance, at most about 0.011 for r up to 0.04"
  inputs:
    - name: f
      meaning: total recurring annual cost as a decimal (fund expense ratio plus any account, wrap or advice fee charged as a percent of assets)
      source: user statement or product document; never assumed
    - name: T
      meaning: years the money is expected to stay invested
      source: user statement; if unknown, show 10, 20 and 30 side by side
    - name: r
      meaning: gross annual return, exact form only
      source: not estimated by the engine; the engine form is used so no return forecast is needed
  worked_table:
    - f: 0.0025
      lost_10y: 0.024
      lost_20y: 0.047
      lost_30y: 0.070
    - f: 0.005
      lost_10y: 0.047
      lost_20y: 0.092
      lost_30y: 0.135
    - f: 0.01
      lost_10y: 0.092
      lost_20y: 0.176
      lost_30y: 0.252
    - f: 0.015
      lost_10y: 0.135
      lost_20y: 0.252
      lost_30y: 0.353
  worked_table_note: exact form at r = 0.04; values at r = 0.06 differ by at most 0.005
  comparison_rule: when two products track the same exposure, the fee difference is the only part of the outcome known in advance; state it as share of ending balance over the user's horizon
  never: present a lower fee as a guarantee of higher return between products with DIFFERENT exposures
  basis_grade: A
claim: >
  A recurring fee does not cost its headline percentage once; it compounds.
  Because each year's fee also removes the return that money would have
  earned (the mechanism the SEC states), the share of the ending balance lost
  to an annual cost f over T years is 1 - ((1+r-f)/(1+r))^T, which for any
  plausible return is close to 1 - (1-f)^T. A 1 percent annual cost
  therefore takes about 9 percent of the ending balance over 10 years, about
  18 percent over 20 and about 25 percent over 30; a 0.25 percent cost takes
  about 2, 5 and 7 percent. In the SEC's own setup (100,000 USD, 4 percent a
  year, 20 years) that is roughly 219,000 with no fee against about 181,000
  at 1 percent. The arithmetic is exact; the empirical companion is
  directional: in US equity funds, investment expenses are one of the two
  things that almost completely explain why some funds keep doing better or
  worse than others, and the only persistence that holds up is the
  continued underperformance of the worst funds (Carhart 1997). Operational
  rule: when two products give the same exposure, compute the fee
  difference as a share of the user's ending balance over their horizon;
  never sell a lower fee as a higher expected return between products that
  hold different things.
reasoning: >
  The headline claim is compounding arithmetic, true by construction, which
  is why it sits at the top band with the methodology qualifier, matching
  how item 001 is graded. The engine form deliberately drops the return term
  so the module never has to forecast a return to state a fee cost: the
  dependence on r is second order, and the stated tolerance was checked
  numerically over the grid in formula_note (the engine form errs only toward overstating the cost). The SEC bulletin is a
  regulator's investor-education page rather than research, and it is cited
  for the setup and the mechanism only; its chart values sit in an image and
  were not read, so the dollar figures in the claim are recomputed from its
  setup (fee subtracted from the 4 percent return each year), not quoted.
  Carhart is a peer-reviewed primary in a top journal and is carried only to
  the strength of its abstract (expenses help explain persistent
  underperformance); the commonly quoted "one-for-one or worse" coefficient
  was not read at source and is NOT stated. What this row does not cover:
  Korean fund cost disclosure (total expense ratio versus separately
  disclosed trading-commission ratio) was not read at a primary in this pass
  and is logged in GAPS.md rather than asserted.
---

# finance-investing/fee-drag-compounding-071 -- 보수 1%는 정말 1%만 가져가나

**한 줄 그림:** 매년 떼는 비용은 복리로 커진다. 연 1%는 20년이면 최종 잔고의 약 18%,
30년이면 약 25%다.

## The fee-drag rule (engine-readable)

Share of the ending balance lost to a recurring annual cost `f` over `T` years:

- exact: `1 - ((1 + r - f) / (1 + r)) ^ T`
- engine form (no return forecast needed): `1 - (1 - f) ^ T`

| Annual cost | 10 years | 20 years | 30 years |
|---|---|---|---|
| 0.25% | about 2% | about 5% | about 7% |
| 0.50% | about 5% | about 9% | about 13% |
| 1.00% | about 9% | about 18% | about 25% |
| 1.50% | about 13% | about 25% | about 35% |

`f` is every recurring percent-of-assets charge stacked together: the fund's
expense ratio plus any account, wrap or advice fee. Take it from the user or
the product document; never assume it. If the horizon is unknown, show the
three columns side by side.

Comparison rule: for two products with the same exposure, the fee difference
is the one part of the result known in advance; state it as a share of the
ending balance over the user's horizon. For products with different
exposures, the fee is one input among several and is never presented as a
return guarantee.

## 한국어 요약 (답변용)

- 연 보수는 한 번 떼고 끝나는 돈이 아니다. 매년 떼인 돈이 그 뒤로 벌었을 수익까지 같이 사라진다.
  그래서 연 비용 f를 T년 동안 내면 최종 잔고에서 대략 1-(1-f)^T 만큼이 빠진다. 기대수익률을
  몰라도 비슷한 값이 나오고, 비용을 약간 크게 잡는 쪽으로만 틀린다.
- 숫자로 보면 연 1%는 10년에 최종 잔고의 약 9%, 20년에 약 18%, 30년에 약 25%다. 연 0.25%면 같은
  기간에 약 2%, 5%, 7%다. 미국 증권거래위원회(SEC) 예시 조건(10만 달러, 연 4%, 20년)으로 계산하면
  보수가 없을 때 약 21만 9천 달러, 연 1%일 때 약 18만 1천 달러다.
- 비용에는 펀드·ETF 보수뿐 아니라 계좌 수수료, 일임·자문 수수료처럼 자산의 몇 %로 매년 떼는 돈을
  전부 더한다. 비용 값은 사용자나 상품 설명서에서 받고, 짐작해서 넣지 않는다.
- 같은 지수를 따라가는 두 상품이라면 보수 차이는 미리 알 수 있는 유일한 차이이므로, 사용자의 투자
  기간 동안 최종 잔고의 몇 %인지로 말해 준다. 담고 있는 자산이 다른 상품끼리는 "보수가 싸니까 수익이
  더 높다"고 말하지 않는다.
- 미국 주식형 펀드 연구에서는 비용이 높은 펀드일수록 성과가 계속 나쁜 쪽에 남는 경향이 확인됐다.
  다만 "보수 1%p가 수익 1%p 이상을 깎는다"는 식의 계수는 원문에서 확인하지 못해 말하지 않는다.
- 한국 펀드의 비용 공시(총보수, 총비용비율, 매매·중개수수료율의 구분)는 이번에 1차 출처로 확인하지
  못했다. 상품별 비용은 공시 자료로 직접 확인한다.
