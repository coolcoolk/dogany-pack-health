---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Jurisdiction-bound item -- locale KR. Verified against the Korean National
# Tax Service on 2026-09-02.
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/kr-foreign-stock-cgt-015.
# Source re-audit 2026-10-06: NTS pages re-read (5-year residency, 2020
# netting, 2.5m KRW deduction unchanged); added that 2026 carries TEMPORARY
# foreign-share deductions (조특법 제91조의26 domestic-return account and
# 제91조의27 FX-hedge product, 법률 제21549호, 2026-04-21). Their rates and
# windows were seen only in the press and are deliberately not stored.
id: finance-investing/kr-foreign-stock-cgt-015
domain: finance-investing
grade: B (codified regulatory fact, staleness-gated)
lane: "@quant-market"
locale: KR
as_of: 2020-01-01 netting rule, verified 2026-09-02; 2026 temporary overlay verified 2026-10-06
contested: no
sources:
  - "National Tax Service (Korea), 주식등 양도소득세 과세대상. https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800"
  - "국가법령정보센터, 조세특례제한법 제정·개정이유, 법률 제21549호 (2026-04-21): 국내시장복귀계좌를 통한 국외상장주식 양도 시 한시적 소득공제 (제91조의26), 환율변동위험회피상품 투자액 5 pct 국외상장주식 양도소득금액 공제 (제91조의27). https://www.law.go.kr/LSW/lsRvsRsnListP.do?lsId=001584&chrClsCd=010102 (read 2026-10-06)"
  - "National Tax Service (Korea), 양도소득세 기본정보 (세액계산 흐름도 / 주식등 신고납부). https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2310&cntntsId=7709"
claim: >
  Foreign shares are taxed on a completely different basis from domestic
  shares for a Korean resident, and the difference drives behaviour more than
  the rate does. Per the National Tax Service: a resident who has maintained
  a domicile or place of residence in Korea continuously for 5 years or more
  up to the disposal date is taxable on gains from foreign shares; since
  2020-01-01 domestic and foreign share gains and losses may be NETTED
  against each other, with a single annual basic deduction of 2.5 million KRW
  applied to the combined amount. The headline rate quoted in practice is 22
  percent (20 percent national plus 10 percent local surtax on the tax), and
  the final return is filed in May of the following year for the prior
  calendar year, with local income tax self-reported separately since
  2020-01-01. Three structural consequences that matter more than the rate:
  losses are usable (unlike the domestic minority-shareholder case where
  neither gains nor losses are recognised), the deduction is annual and does
  not carry forward, and realisation timing is therefore a live decision each
  December. TEMPORARY OVERLAY for 2026 (verified 2026-10-06 at the
  국가법령정보센터 revision record, law no. 21549 of 2026-04-21): 조세특례제한법
  제91조의26 gives a time-limited deduction on foreign listed shares sold
  through a 국내시장복귀계좌 and reinvested domestically, and 제91조의27
  deducts 5 percent of an FX-hedge product investment from foreign-share
  gains. The 26 deduction's sale-date ladder and cap are NOT stored here
  (press-only at this audit); look them up before a 2026 sale.
reasoning: >
  Same treatment as finance-investing/kr-domestic-stock-cgt-exemption-014:
  codified and authoritative, but revocable by legislation, so it sits at the
  strong band with a mandatory staleness gate rather than at the top band.
  The 22 percent figure is stated as the composite rate as commonly applied
  (20 percent plus local surtax) and is the one number in this item most
  exposed to legislative change. The netting rule, the 5-year residency
  condition, the 2.5 million KRW annual deduction and the May filing window
  were each read off the NTS pages directly, not from brokerage summaries.
---

# finance-investing/kr-foreign-stock-cgt-015

For a Korean resident, foreign shares work in the opposite way to domestic
listed shares. Gains are taxable, at a headline 22 percent once the local
surtax is included, and the return is filed in May for the previous calendar
year. The taxable person is a resident who has kept a domicile or residence
in Korea continuously for at least 5 years up to the disposal date.

Three structural points do more work than the rate.

First, since 2020 domestic and foreign share gains and losses can be netted
against each other, and one annual basic deduction of 2.5 million KRW applies
to the combined figure. Losses are therefore useful in a way they simply are
not for an ordinary minority shareholder in Korean listed stock, where
neither the gain nor the loss is recognised at all.

Second, the deduction is annual and does not carry forward. An investor who
realises nothing in a given year has thrown that allowance away.

Third, because of the first two, the timing of realisation is a genuine
December decision each year rather than an afterthought.

The rate is the part most likely to change by legislation, so it should be
re-checked rather than assumed. 2026 shows the other way it moves: a
temporary special-taxation deduction for foreign shares sold through a
domestic-return account and reinvested in Korean shares, plus a small
deduction for FX-hedge products, both enacted in April 2026. Their windows
and caps are deliberately not stored here -- check them before a 2026 sale.
