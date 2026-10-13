---
# Finance GAPS sprint 2026-10-06 (dispatch kw-finance-newitems). Answers the
# v12 coverage gap "OPTIMAL REBALANCING FREQUENCY" as far as the evidence
# goes, which is: there is no optimal frequency, the risk differences between
# sane schedules are small, and the cost differences are large. Item 011 keeps
# the WHY (rebalancing is risk control with a concave payoff); this row is the
# HOW OFTEN. Read at source on 2026-10-06: the Vanguard 2010 paper in full
# text (executive summary, Figure 7 table, Figure 8 discussion); the
# Daryanani 2008 abstract page at the FPA. The Daryanani result is carried
# only as a refused rule, for the reason given in reasoning.
#
# rebalancing_policy is structured data for a portfolio module. Every
# threshold and interval below is a DEFAULT labelled as a product convention;
# the evidence supports the range, not the specific value.
id: finance-investing/rebalancing-cadence-072
domain: finance-investing
grade: C (no schedule dominates on risk-adjusted return; event count and cost rise steeply with frequency -- one long historical simulation, vendor research); D (the specific default interval and band)
lane: "@quant-market"
locale: universal
as_of: 1926-2009 (simulation window) / read 2026-10-06
contested: no
sources:
  - "Jaconetti, C. M., Kinniry, F. M. Jr. and Zilbering, Y. (2010). Best practices for portfolio rebalancing. Vanguard research, July 2010. Copy read: https://indexacapital.com/bundles/unaiadvisor/docs/papers/2010-Vanguard-Best-practices-for-portfolio-rebalancing.pdf -- 60/40 US stock/bond, 1926-2009, no taxes, no contributions. Figure 7: monthly with no threshold 8.5 pct return / 12.1 pct volatility / 1,008 rebalancing events; monthly 5 pct band 8.6 / 12.2 / 58; quarterly 5 pct 8.8 / 12.1 / 50; annual 5 pct 8.6 / 11.8 / 28; annual 10 pct 8.7 / 12.1 / 15; never rebalanced 9.1 / 14.4 / 0, drifting to about 99 pct stocks. Conclusion: no optimal frequency or threshold; annual or semiannual monitoring with 5 pct thresholds a reasonable balance; annual preferred when taxes or substantial time/costs are involved."
  - "Daryanani, G. (2008). Opportunistic Rebalancing: A New Paradigm for Wealth Managers. Journal of Financial Planning, January 2008. https://www.financialplanningassociation.org/article/journal/JAN08-opportunistic-rebalancing-new-paradigm-wealth-managers -- look often (biweekly), trade rarely (wide bands), rebalance only the classes out of band; claims benefits more than double annual rebalancing. Abstract page read; the band width and period are from secondary summaries and are not carried."
  - "finance-investing/rebalancing-risk-not-return-011"  # within-warehouse: why to rebalance at all; this row is how often
  - "finance-investing/backtest-overfitting-floor-006"  # within-warehouse: why a parameter tuned on one sample is not a rule
  - "finance-investing/kr-foreign-stock-cgt-015"  # within-warehouse: a sell inside a taxable foreign-share account realises a gain
  - "finance-investing/kr-domestic-stock-cgt-exemption-014"  # within-warehouse: domestic sells still pay transaction tax on every sale
  - "finance-investing/kr-pension-isa-wrapper-structure-073"  # within-warehouse: trades inside a pension or ISA account do not realise tax at the trade
rebalancing_policy:
  objective: hold the risk level of the target mix; not a return source (011)
  check_interval_default: 12 months
  check_interval_range: 6 to 12 months
  band_default_pp: 5
  band_range_pp: 5 to 10
  band_meaning: absolute percentage-point drift of the largest asset-class weight from target
  trigger: rebalance at a scheduled check only if drift is at or beyond the band
  first_lever: direct new contributions, withdrawals and income to the underweight class before selling anything
  rebalance_to: target when the cost is mainly fixed per trade (time, flat fees); the nearest band edge when the cost is mainly proportional to trade size (commissions, taxes); in between when both
  tax_rule: prefer moves inside tax-deferred wrappers or via new cash over sells that realise taxable gains
  never: claim a schedule raises expected return; recommend checking or trading more often than monthly for a long-term mix
  defaults_are: product convention, inside the range the evidence finds indistinguishable
  basis: Jaconetti et al. 2010
  basis_grade: C
refused_rules:
  - rule: opportunistic rebalancing with biweekly looks and wide bands beats annual rebalancing by a stated margin
    source: Daryanani 2008
    why_refused: parameters selected on one historical sample by the same study that reports the gain; no out-of-sample test read; see 006
claim: >
  No rebalancing schedule has been shown to be best, and the choices that
  matter most are cheap ones. In a 1926-2009 US simulation of a 60/40
  stock/bond mix, rebalancing monthly, quarterly or annually, with or
  without 1, 5 or 10 percentage-point bands, gave average returns between
  8.5 and 8.9 percent and volatility between 11.8 and 12.3 percent, while
  the number of rebalancing events ranged from 1,008 down to 15. Never
  rebalancing is the one choice that is clearly different: it drifted to
  about 99 percent stocks, with volatility of 14.4 percent. Because risk
  control is close to flat across sensible schedules and cost is not, the
  practical rule is to check once or twice a year, act only when a weight
  has drifted by about 5 percentage points or more, use new money,
  withdrawals and income to rebalance first, and in taxable accounts prefer
  the least-taxed route. The specific interval and band are defaults inside
  a range the evidence cannot tell apart, not findings. Claims that a
  particular look-often, trade-rarely rule adds a stated return margin come
  from parameters tuned on one historical sample and are not adopted.
reasoning: >
  The central finding rests on a single long historical simulation by an
  index-fund provider. That is observational-tier evidence, and the
  provider's commercial interest leans toward low-turnover, low-cost advice,
  which is the direction of the conclusion, so the row is held below the
  strong band. Two things keep it from the practitioner floor: the result is
  a flat-maximum finding (many schedules land within a few tenths of a
  percent of each other), which is the kind of conclusion least sensitive to
  the exact sample, and it agrees with item 011's theory, under which no
  schedule should be a return source. The specific 12-month / 5-point
  defaults are product conventions within that flat region and are graded
  at the floor. The simulation has no taxes and no contributions; the
  cash-flow-first and tax-route rules come from the same paper's
  discussion and from the Korean wrapper structure in items 014, 015 and
  073, not from a measured Korean comparison. Daryanani's opportunistic
  rule is refused as a rule, not dismissed as an idea: looking more often
  while trading rarely is consistent with the Vanguard result, but the
  claimed margin over annual rebalancing comes from bands and look
  intervals chosen on the same sample that produced the margin, the exact
  failure item 006 exists to catch.
---

# finance-investing/rebalancing-cadence-072 -- 리밸런싱은 얼마나 자주 해야 하나

**한 줄 그림:** 정답 주기는 없다. 1년에 한두 번 확인하고, 5%p 이상 벗어났을 때만 맞춘다.
새로 넣는 돈으로 먼저 맞추고, 세금이 나는 매도는 마지막이다.

## The policy (engine-readable)

| Field | Default | Range the evidence cannot tell apart |
|---|---|---|
| check interval | 12 months | 6-12 months |
| band (drift from target weight) | 5 percentage points | 5-10 points |
| trigger | act at a check only if drift is at or beyond the band | |
| first lever | new contributions, withdrawals and income go to the underweight class | |
| rebalance to | target if cost is mostly fixed per trade; band edge if cost is mostly proportional; in between if both | |
| taxable account | prefer moves inside tax-deferred accounts or via new cash | |

The defaults are product conventions. Never claim a schedule raises return.
Never recommend checking or trading a long-term mix more often than monthly.

## What the simulation showed (60/40, US, 1926-2009, no taxes)

| Schedule | Return | Volatility | Rebalancing events |
|---|---|---|---|
| monthly, no band | 8.5% | 12.1% | 1,008 |
| monthly, 5-point band | 8.6% | 12.2% | 58 |
| quarterly, 5-point band | 8.8% | 12.1% | 50 |
| annual, 5-point band | 8.6% | 11.8% | 28 |
| annual, 10-point band | 8.7% | 12.1% | 15 |
| never | 9.1% | 14.4% | 0 |

The sensible schedules are within a few tenths of each other on both return
and risk; the number of trades differs about seventy-fold. Never rebalancing
is the outlier: higher return because it drifted toward nearly all stocks,
and correspondingly higher risk.

## 한국어 요약 (답변용)

- 리밸런싱을 몇 달마다 하는 게 가장 좋은지에 대한 정답은 없다. 미국 주식 60%·채권 40% 포트폴리오를
  1926-2009년으로 돌려 본 연구에서 매월·분기·매년, 허용폭 1·5·10%p 조합들의 수익률은 8.5-8.9%,
  변동성은 11.8-12.3%로 거의 같았다. 반면 매매 횟수는 1,008번에서 15번까지 차이가 컸다.
- 확실히 다른 건 "아예 안 하기" 하나다. 이 경우 주식 비중이 99% 가까이까지 불어나서 변동성이
  14.4%로 커졌다. 수익률이 높았던 건 더 위험한 포트폴리오가 됐기 때문이다.
- 그래서 기본 규칙은 이렇다. 1년에 한두 번 비중을 확인하고, 목표에서 5%p 이상 벗어났을 때만
  맞춘다. 새로 넣는 돈, 빼는 돈, 배당·이자를 먼저 모자란 쪽으로 보내고, 파는 건 그다음이다.
  12개월·5%p라는 값은 제품 쪽 기본값이고, 근거가 말해 주는 건 6-12개월, 5-10%p 범위 안에서는
  차이를 가릴 수 없다는 것까지다.
- 한국에서는 어디서 파느냐가 비용을 바꾼다. 해외주식을 일반 계좌에서 팔면 양도차익이 실현되고,
  국내 상장주식은 손익과 상관없이 팔 때마다 거래세가 붙는다. 연금저축·IRP·ISA 안에서 바꾸는 매매는
  그 시점에 소득세가 확정되지 않는다(국내 상장주식을 팔 때 붙는 거래세는 별개다). 그래서 가능하면 이런 계좌 안이나 새 돈으로 맞춘다.
- "2주마다 확인하고 넓은 폭을 벗어날 때만 매매하면 연간 리밸런싱보다 수익이 두 배"라는 식의 주장은
  같은 과거 데이터로 규칙을 고르고 성과도 잰 결과라서 규칙으로 쓰지 않는다. 리밸런싱은 수익을 올리는
  방법이 아니라 정한 위험 수준을 지키는 방법이다.
