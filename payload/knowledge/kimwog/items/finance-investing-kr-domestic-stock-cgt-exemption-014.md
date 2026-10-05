---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Jurisdiction-bound item -- locale KR. Verified against Korean government
# primary sources (National Tax Service; Ministry of Government Legislation
# easylaw service) on 2026-09-02.
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/kr-domestic-stock-cgt-exemption-014.
id: finance-investing/kr-domestic-stock-cgt-exemption-014
domain: finance-investing
grade: B (codified regulatory fact, staleness-gated)
lane: "@quant-market"
locale: KR
as_of: 2024-01-01 shareholder thresholds, verified 2026-09-02
contested: no
sources:
  - "National Tax Service (Korea), 주식등 양도소득세 과세대상. https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800"
  - "Ministry of Government Legislation (Korea), 찾기쉬운 생활법령정보: 주식투자자 > 주식의 거래 > 주식거래에 따른 세금. https://easylaw.go.kr/CSP/CnpClsMain.laf?popMenu=ov&csmSeq=1701&ccfNo=2&cciNo=3&cnpClsNo=1 (citing 증권거래세법 제7조/제8조 and 소득세법 제92조-제104조)"
claim: >
  For a Korean resident, gains on KRX-listed Korean shares sold on-exchange
  are NOT subject to capital gains tax unless the seller is a 대주주 (large
  shareholder). Per the National Tax Service, a 대주주 is taxable on the sale
  of even a single share, while a 소액주주 selling through the securities
  market is outside the scope; a 소액주주 selling OFF-exchange is inside the
  scope. Thresholds for disposals on or after 2024-01-01, as published by the
  NTS: KOSPI 1 percent or 5.0 billion KRW; KOSDAQ 2 percent or 5.0 billion
  KRW; KONEX 4 percent or 5.0 billion KRW; unlisted 4 percent or 1.0 billion
  KRW. Dividend income is separately withheld at 14 percent under 소득세법
  (before local surtax). STRUCTURAL ASYMMETRY that matters more than any
  rate: 증권거래세 (securities transaction tax) is levied on the SALE
  regardless of whether the sale is at a profit or a loss, so the transaction
  cost of a Korean domestic equity trade is incurred on losing trades too.
  The transaction-tax RATE is deliberately not stated in this item -- see
  finance-investing/kr-tax-regime-staleness-gate-016.
reasoning: >
  Codified regulatory facts are authoritative for their jurisdiction but are
  revocable by legislation, so this lane grades them at the strong band with
  a mandatory staleness gate rather than at the top band reserved for results
  that cannot change. The item carries STRUCTURE (who is taxed, on what
  event, and the profit-independence of the transaction tax) and refuses to
  carry the transaction-tax rate, which has moved repeatedly in recent years
  and would rot in place. Verified directly against two Korean government
  sources rather than brokerage or news summaries.
---

# finance-investing/kr-domestic-stock-cgt-exemption-014

A Korean resident who is an ordinary minority shareholder pays no capital
gains tax on Korean listed shares sold through the exchange. Capital gains
tax applies to a 대주주, and a 대주주 is taxable on the disposal of even one
share. It also applies to a minority shareholder who sells off-exchange.

The large-shareholder thresholds published by the National Tax Service for
disposals from 1 January 2024 are: KOSPI 1 percent of the company or 5.0
billion KRW held; KOSDAQ 2 percent or 5.0 billion KRW; KONEX 4 percent or 5.0
billion KRW; unlisted 4 percent or 1.0 billion KRW. Dividends are a separate
matter and are withheld at 14 percent before local surtax.

The part most likely to be reasoned about incorrectly is not the exemption,
it is what replaces it. Korea charges a securities transaction tax on the
sale itself, and that tax is owed whether the trade made money or lost money.
So a loss-making round trip in Korean shares still costs tax, which makes
turnover more expensive here than a naive "no capital gains tax" reading
suggests.

The rate of that transaction tax is intentionally not stated here. It is set
by enforcement decree and has been amended repeatedly in recent years, so a
number written into this item would go stale silently.
