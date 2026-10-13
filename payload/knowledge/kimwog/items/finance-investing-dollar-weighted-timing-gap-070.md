---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 by two parallel passes (dispatch
# kw-finance-newitems, the GAPS sprint, and kw-finance-reaudit, the source
# re-audit) that both closed the same v12 refusal; merged into this one row in
# the v37 consolidation. The other provisional id,
# "dollar-weighted-gap-hindsight" (also numbered 070), was never released and
# is folded in here.
#
# Closes the v12 GAPS.md "INVESTOR BEHAVIOUR GAP" refusal in bounded form: the
# Dalbar figure stays refused; the peer-reviewed dollar-weighted literature is
# carried WITH its strongest published objection (Hayley 2014), so no single
# gap number is exported as "the cost of bad timing".
# Read at source on 2026-10-06: the Friesen & Sapp univariate table as
# reproduced in the US DOL-commissioned replication (AACG 2017, Table 1);
# Hayley's accepted manuscript (City Research Online: abstract, section III,
# Table I restatement of Dichev and Friesen-Sapp, conclusion), including its
# summary of Dichev 2007 and Keswani & Stolin 2009; the Dichev 2007 AER record.
# Friesen & Sapp full text itself was NOT reachable (publisher 403); its
# numbers are carried through the replication that reproduces its tables. The
# Clare-Motson and Dichev-Yu figures are carried only as Hayley restates them.
#
# return_measures / timing_attribution_rule are structured data for a
# portfolio / statement module: which return figure to compute, what each one
# answers, and which comparison may be labelled "timing". speech_rules say
# what that module may and may not say when it compares an owner's
# money-weighted return with the fund's own return.
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/dollar-weighted-timing-gap-070.
id: finance-investing/dollar-weighted-timing-gap-070
domain: finance-investing
grade: C (contested -- aggregate dollar-weighted shortfall measured repeatedly; how much of it is investor timing is disputed, the one decomposition read at source puts most of the NYSE/AMEX gap in hindsight bias); A (definitions -- what each return measure answers); D (plan-counterfactual window, scheduled-contributor exemption and speech rules -- product conventions)
lane: "@quant-market"
locale: universal
as_of: 1926-2016 (measurement windows) / 2014 (decomposition) / read 2026-10-06
contested: yes
sources:
  - "Dichev, I. D. (2007). What Are Stock Investors' Actual Historical Returns? Evidence from Dollar-Weighted Returns. American Economic Review 97(1), 386-401. https://doi.org/10.1257/aer.97.1.386 (record: https://www.aeaweb.org/articles?id=10.1257/aer.97.1.386) -- NYSE/AMEX 1926-2002 dollar-weighted return about 1.3 pct a year below buy-and-hold, NASDAQ 1973-2002 5.3 pct; Dichev reports the NYSE/AMEX differential falls to 0.7 pct in the second half of the period. Figures as summarised in Hayley 2014 (p.4, Table I); not read at source."
  - "Friesen, G. C. and Sapp, T. R. A. (2007). Mutual fund flows and investor returns: An empirical examination of fund investor timing ability. Journal of Banking & Finance 31(9), 2796-2816. https://ideas.repec.org/a/eee/jbfina/v31y2007i9p2796-2816.html (pii S0378426607001422) -- 7,125 US equity funds 1991-2004: time-weighted 0.62 pct a month vs dollar-weighted 0.49 pct, gap 0.13 pct a month (about 1.6 pct a year); load funds 0.16 pct vs no-load 0.08 pct a month. Tables read as reproduced in the AACG replication below; full text not reachable."
  - "Padmanabhan, K., Panis, C. and Tardiff, T. J. (2017). The Ability of Investors to Time Purchases and Sales of Mutual Funds. Advanced Analytical Consulting Group for the US Department of Labor, EBSA, 2017-11-01. https://www.dol.gov/sites/dolgov/files/EBSA/researchers/analysis/retirement/mutual-fund-timing-ability.pdf -- replicates Friesen & Sapp; 2007-2016 overall gap 0.53 pct a year (narrower), excess gap for load funds 1.58 pct. Commissioned in the fiduciary-rule context; not peer reviewed."
  - "Hayley, S. (2014). Hindsight Effects in Dollar-Weighted Returns. Journal of Financial and Quantitative Analysis 49(1), 249-269. https://doi.org/10.1017/s0022109014000155 -- accepted version read: https://openaccess.city.ac.uk/id/eprint/6226/ -- the dollar-weighted vs buy-and-hold differential mixes correlation of flows with FUTURE returns (timing, affects wealth) and with PAST returns (hindsight bias, does not); on Dichev's NYSE/AMEX data (geometric 9.87 pct, dollar-weighted 8.61 pct) the 1.26 pct differential splits into about 0.21 pct timing and 0.95 pct hindsight bias. Also records Keswani and Stolin (2009): the NYSE/AMEX differential disappears at some split points; and is the source of the Clare-Motson (0.8 pct, UK funds) and Dichev-Yu (3.6 pct, hedge funds) figures, carried as Hayley restates them."
  - "finance-investing/curator-checklist-017"  # within-warehouse: trigger (8), the dollar-weighted downgrade this item operationalises
  - "finance-investing/panic-selling-freakout-008"  # within-warehouse: the behavioural mechanism a timing gap would come from; failure to return is the measured harm
  - "finance-investing/individual-trading-penalty-007"  # within-warehouse: turnover penalty, a different measurement of the same family
  - "finance-investing/lump-sum-vs-cost-averaging-010"  # within-warehouse: why steady contributions are not themselves a timing error
return_measures:
  - measure: time_weighted
    also_called: [TWR, buy-and-hold return, fund return]
    answers: how the holdings performed, independent of when money went in or out
    use_for: comparing a portfolio or fund to its benchmark or to another fund
    basis_grade: A
  - measure: money_weighted
    also_called: [MWR, dollar-weighted return, IRR, investor return]
    answers: what the investor's own cash flows actually earned
    use_for: telling the user what their own money did
    basis_grade: A
  - measure: gap
    definition: money_weighted minus time_weighted over the same window
    label_as_timing_cost: false
    why: "the gap moves with contribution schedule and with flows that follow past returns (hindsight effect), not only with discretionary timing"
    basis_grade: C
timing_attribution_rule:
  compute: actual ending wealth vs ending wealth if the SAME cash amounts had followed the user's stated plan (same total, planned dates, no discretionary sells)
  may_label_as_timing: only this plan-counterfactual difference, over a window that contains at least one full market decline and recovery AND is at least 5 years long
  window_constant: product convention, not evidence
  never: quote a population gap figure (Dalbar or literature) as the user's own timing cost
  basis_grade: D
speech_rules:
  - rule: gap_is_not_skill_loss
    when: an owner's money-weighted return (IRR) is below the fund's time-weighted return
    say: the gap mixes any genuine timing effect with a hindsight effect of flows that followed past returns; it is not by itself proof of bad timing
    do_not_say: you lost N percent a year by timing badly
    basis: finance-investing/dollar-weighted-timing-gap-070
    basis_grade: C
  - rule: steady_contributor_exemption
    when: the owner contributes on a fixed schedule (salary, automatic plan) rather than by choice
    say: a gap here largely reflects the contribution schedule against the market path, not a decision the owner made
    do_not_say: any behaviour-gap figure applied to scheduled contributions
    basis: finance-investing/curator-checklist-017
    basis_grade: D
  - rule: no_industry_gap_number
    when: asked how much the average investor loses to behaviour
    say: academic aggregate gaps of roughly 1-2 percent a year exist, but a published decomposition attributes most of the US-equity one to hindsight in the measure, not to timing
    do_not_say: a Dalbar QAIB figure
    basis: GAPS.md finance-investing v12 refusal
    basis_grade: D
  - rule: discretionary_moves_still_costly
    when: the owner proposes selling out after a fall and waiting to re-enter
    say: route to 008 (failure to return is the measured harm) and 009 (both halves of the best/worst-days table)
    do_not_say: use this item to argue the move is harmless
    basis: finance-investing/panic-selling-freakout-008
    basis_grade: C
refraction_notes:
  - note: >
      CONTRIBUTION PATTERN DECIDES WHAT THE GAP MEANS. For an investor who
      adds money on a fixed schedule, a money-weighted return below the
      fund's return is mostly the arithmetic of when the schedule met the
      market, not a choice. Only discretionary, return-chasing flows are what
      the timing literature is about. The engine should ask, once, whether
      contributions are scheduled or discretionary before characterising a
      gap.
    grade: D
  - note: >
      SIZE OF THE REAL TIMING SHARE IS UNSETTLED. In the one decomposition
      read at source, about a sixth of the NYSE/AMEX differential is timing
      and the rest is hindsight bias. That is one market, one method, one
      author; fund-level and NASDAQ decompositions were not read, and the
      NYSE/AMEX result itself moves with the chosen split point (Keswani and
      Stolin). Speak the direction (some cost from chasing past returns)
      without a number.
    grade: C
claim: >
  An investor's own return (money-weighted, the internal rate of return on
  their cash flows) and the return of what they hold (time-weighted) answer
  different questions, and the gap between them is a real, repeatedly
  measured quantity: about 1.3 percent a year for NYSE/AMEX stocks over
  1926-2002 and 5.3 percent for NASDAQ over 1973-2002 in aggregate (Dichev
  2007, as restated by Hayley 2014), and about 0.13 percent a month, roughly
  1.6 percent a year, for 7,125 US equity mutual funds over 1991-2004, twice
  as large in load funds as in no-load funds (Friesen and Sapp 2007); Hayley
  also restates 0.8 percent for UK funds (Clare and Motson) and 3.6 percent
  for hedge funds (Dichev and Yu). A government-commissioned replication
  found the overall fund gap narrowed to about 0.5 percent a year in
  2007-2016 while the load-fund excess persisted. What the gap MEANS is
  contested. Hayley (2014) shows the differential mixes two things -- flows
  that anticipate future returns badly (true timing error, which costs
  wealth) and flows that merely follow past returns (a hindsight effect that
  lowers the dollar-weighted figure without lowering expected wealth). On
  Dichev's own NYSE/AMEX data the 1.26 percent differential decomposes into
  about 0.21 percent from investor timing and 0.95 percent from hindsight
  bias, and the result is also sensitive to the chosen start and end dates.
  Operational rule: report both measures with their names, never label the
  raw gap "the cost of your timing" -- whether it comes from an academic
  dataset, an industry report or the owner's own brokerage statement -- and
  attribute timing only against a counterfactual that holds the user's own
  cash amounts fixed on their stated plan.
reasoning: >
  The definitions are textbook and uncontested, so the return_measures rows
  that say what each figure answers sit at the top of the ladder. The size
  and meaning of the gap is where the evidence splits: two peer-reviewed
  primaries in different datasets agree the dollar-weighted figure is lower,
  and a third peer-reviewed paper in a top methods journal shows the standard
  interpretation of that shortfall overstates timing harm, with a published
  robustness challenge on the date split. Measured repeatedly but with its
  causal reading contested puts it in the observational band with the
  contested flag set; the timing share rests on a single decomposition paper
  on one market, read directly, with no independent replication on fund flows
  located. Honesty notes: the Dichev and Clare-Motson / Dichev-Yu figures are
  carried at one remove (as restated by Hayley); the Friesen and Sapp numbers
  were read from the DOL-commissioned replication's reproduction of their
  table, not from the paper itself, and the replication is a consultancy
  report in a regulatory context. The fund-level load/no-load difference
  survives Hayley's objection better than the aggregate-market figure does,
  because it compares two investor populations under the same market path,
  but no paper read here formally decomposes the fund gap, so that is stated
  as reasoning, not as a finding. The plan-counterfactual rule and the
  scheduled-contributor exemption are method choices (practitioner floor)
  that follow from the decomposition: holding the cash amounts fixed removes
  the contribution-schedule effect, which is the part that is not a decision,
  and so a portfolio-review module never tells an owner who contributes from
  salary that a money-weighted shortfall is their fault. The Dalbar QAIB
  figure remains refused (GAPS.md v12 ledger) and is not reintroduced here.
---

# finance-investing/dollar-weighted-timing-gap-070 -- 내 수익률과 펀드 수익률은 왜 다른가

**한 줄 그림:** 내 돈의 수익률(금액가중)과 상품의 수익률(시간가중)은 다른 질문의 답이다.
둘의 차이를 곧바로 "타이밍 손실"이라고 부르면 안 된다.

## Which number answers which question (engine-readable)

| Measure | Answers | Use for |
|---|---|---|
| time-weighted (TWR) | how the holdings did, ignoring when money moved | fund vs benchmark, fund vs fund |
| money-weighted (MWR / IRR) | what the user's own cash flows earned | "how did my money do" |
| gap (MWR minus TWR) | a mix of contribution schedule, flows that follow past returns, and real timing | never labelled as timing cost on its own |

Timing attribution, when the user asks "did my timing cost me": compare the
actual ending balance with the balance the same cash amounts would have
reached on the user's stated plan (same total, planned dates, no
discretionary sells). Only that difference is called timing, and only over a
window that contains at least one full decline and recovery and is at least five years long. The
window is a product convention.

## What the measurements say, and the objection

- Aggregate US stocks, 1926-2002: dollar-weighted about 1.3 percent a year
  below buy-and-hold; about 0.7 percent in the second half of the period.
  NASDAQ, 1973-2002: about 5.3 percent.
- US equity funds, 1991-2004: a gap of about 0.13 percent a month (about 1.6
  percent a year), and in load funds twice the no-load gap. A later
  replication found the overall gap narrower in 2007-2016 (about 0.5 percent
  a year) but the load-fund excess still there. UK funds about 0.8 percent.
- The objection: money tends to flow in after prices have risen. That alone
  lowers the dollar-weighted figure even when it does not lower anyone's
  expected wealth. When this is separated out on the NYSE/AMEX data, about
  0.21 points of the 1.26-point gap are timing and about 0.95 are hindsight
  bias in the measure, and the result moves with the chosen start and end
  dates.

Two consequences. First, a statement that "the average investor loses N
percent a year to behaviour" overstates what is known, and the commercial
version of that figure is refused in this lane for separate reasons. Second,
an owner who adds money every month from salary will see a money-weighted
return below the fund's return in many years, and that is the schedule
meeting the market, not a mistake.

What is NOT dismissed: chasing past returns can still cost something, and
the measured harm of selling in a fall is not returning (008). This row is
about reading the gap number, not about licensing timing.

## What the engine reads from this row

| Input | Direction | Strength of the evidence |
|---|---|---|
| owner's IRR below fund return, scheduled contributions | describe as schedule effect, no blame | measurement logic, decomposition paper |
| owner's IRR below fund return, discretionary flows | possible timing cost, size not stated; plan-counterfactual only | contested, one decomposition |
| "how much do investors lose to behaviour" | aggregate gaps 1-2 pct a year exist, mostly hindsight on US equities | observational, contested |
| industry behaviour-gap figure | do not quote | refused (GAPS.md v12) |
| sell-after-fall proposal | route to 008 / 009 | 008 observational |

## 한국어 요약 (답변용)

- "펀드는 10% 올랐는데 내 계좌는 왜 6%냐"는 질문은 숫자 두 개를 섞어서 생긴다. 펀드 수익률은
  시간가중 수익률로, 언제 돈을 넣고 뺐는지와 상관없이 상품 자체의 성과다. 내 계좌 수익률은
  금액가중 수익률(IRR)로, 내가 넣고 뺀 돈이 실제로 번 수익률이다. 펀드끼리 비교하거나 지수와
  비교할 때는 앞의 것을, "내 돈이 어떻게 됐나"를 말할 때는 뒤의 것을 쓴다.
- 미국 연구에서는 투자자 돈의 수익률이 상품 수익률보다 대체로 낮게 나왔다. 미국 주식 전체는
  1926-2002년에 연 1.3% 정도, 미국 주식형 펀드는 1991-2004년에 연 1.6% 정도 낮았고, 판매보수·
  수수료가 붙는 판매사 경유 펀드에서 그 차이가 두 배쯤 컸다.
- 다만 이 차이를 전부 "투자자가 타이밍을 못 맞춰서 잃은 돈"으로 읽으면 과장이다. 돈은 주로 값이
  오른 뒤에 들어오는데, 이것만으로도 금액가중 수익률이 낮게 찍힌다. NYSE/AMEX 자료를 나눠 보면
  1.26%p 차이 중 타이밍 몫은 0.21%p 정도고 나머지 0.95%p는 측정상의 편향이었다. 한 연구자, 한
  시장의 분석이고 기간을 어디서 자르느냐에 따라 결과가 흔들린다는 반론도 있어 숫자는 확정이 아니다.
- 월급에서 정기적으로 적립하는 사람의 계좌 수익률이 펀드 수익률보다 낮게 나와도, 그건 적립 일정과
  시장 흐름이 만난 결과다. 본인 잘못으로 말하지 않는다.
- 그래서 사용자의 계좌에서 두 수익률의 차이가 보여도 "타이밍 손실"이라고 말하지 않는다. 타이밍
  손실을 따지려면 같은 금액을 원래 계획대로(같은 날짜에, 중간에 팔지 않고) 넣었을 때의 잔고와
  실제 잔고를 비교하고, 그 비교는 하락과 회복을 한 번 이상 포함하면서 5년 이상인 기간에서만 한다.
  이 기간 기준은 제품 쪽에서 정한 규칙이다.
- 흔히 돌아다니는 "평균 투자자는 매년 몇 퍼센트씩 손해 본다"는 수치(Dalbar 계열)는 계산 방법 자체에
  문제가 있어서 쓰지 않는다. 남의 평균 숫자를 사용자 본인의 손실처럼 말하지 않는다.
- 그렇다고 사고팔기가 무해하다는 뜻은 아니다. 하락장에서 판 뒤 돌아오지 못하는 게 측정된 손해다(008).
