---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (spending-saving lane opening).
# Jurisdiction-bound item -- locale KR. Verified against Korean government
# primary sources on 2026-09-02: the statute text at 국가법령정보센터
# (law.go.kr) and the 법제처 찾기쉬운 생활법령정보 explainer (easylaw.go.kr).
# No brokerage, card-company, bank or news source was used.
id: spending-saving/kr-card-deduction-base-and-floor-015
domain: spending-saving
grade: B (codified regulatory fact, staleness-gated)
lane: "@household-behavioral"
locale: KR
as_of: law in force 2026-01-01 (조세특례제한법 법률 제21223호, 2025-12-23 일부개정), verified 2026-09-02
contested: no
sources:
  - "조세특례제한법 제126조의2 (신용카드 등 사용금액에 대한 소득공제). 국가법령정보센터 (Ministry of Government Legislation), 조문 인쇄본: https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1001060529&chrClsCd=010202&lsId=001584&print=print -- read at [시행 2026. 1. 1.] [법률 제21223호, 2025. 12. 23., 일부개정]"
  - "법제처 찾기쉬운 생활법령정보, 신용카드 이용자 > 신용카드등의 소득공제: https://www.easylaw.go.kr/CSP/CnpClsMainBtr.laf?csmSeq=585&ccfNo=3&cciNo=5&cnpClsNo=1 (citing 조세특례제한법 제126조의2 and 조세특례제한법 시행령 제121조의2)"
  - "source:finance-investing/kr-tax-regime-staleness-gate-016 -- the sibling lane's gate for jurisdiction-bound numbers, which this item follows"
refraction_notes:
  - note: >
      STALENESS GATE, and it is the most important line in this item. 제126조의2
      is amended on the annual tax-revision cycle, and the version read here took
      effect on 2026-01-01 under an amendment dated 2025-12-23. The STRUCTURE
      below (a threshold that must be crossed before anything is deductible, an
      ordering of rates by payment type, an income-tiered annual cap, and a base
      that excludes large parts of household spending) is durable. The
      PERCENTAGES and the CAP AMOUNTS are not, and must be re-verified against
      the statute for each 연말정산 season rather than recited from here.
    grade: B
  - note: >
      NOT VERIFIED in this pass: the culture and sports band. Both government
      sources show 30 percent for 도서/신문/공연/박물관/미술관/영화/체육시설,
      but this band has historically carried a 총급여 eligibility ceiling and
      the condition was not confirmed at source here. Treat the culture band as
      existing at 30 percent with an unverified income condition attached, and
      do not compute with it until the condition is read.
    grade: D
  - note: >
      Temporary 특례 provisions (for example additional deductions tied to
      year-on-year spending growth) have been enacted repeatedly for single tax
      years. None are carried in this item. Their absence here is not evidence
      that none is in force for a given year.
    grade: C
claim: >
  Korea's card-spending income deduction is not a rebate on spending; it is a
  deduction on the portion of spending ABOVE a threshold, computed over a base
  that excludes much of what a household actually spends. Four structural facts,
  read at the statute. (1) THRESHOLD: nothing is deductible until 신용카드등
  사용금액 exceeds 25 percent of 총급여액 (the 최저사용금액); 국외 사용분 is
  outside the base entirely. Below that line the deduction is zero regardless of
  payment method. (2) RATE ORDER: above the threshold the deduction rate depends
  on how the money was paid -- 신용카드 15 percent, 직불·선불카드 and
  현금영수증 30 percent, 전통시장 40 percent, 대중교통 40 percent (a culture and
  sports band at 30 percent also exists; see the refraction note). (3)
  INCOME-TIERED ANNUAL CAP: as published, 총급여 7천만원 이하 gives an annual
  cap of 300만원 and above 7천만원 gives 250만원, rising with dependent children
  to 350만원/275만원 with one and 400만원/300만원 with two or more. (4)
  EXCLUSIONS FROM THE BASE, which is the part most often reasoned about
  incorrectly: the statute excludes business or corporate costs, transactions
  that simulate a sale of goods or services, and vehicle purchases (with a
  partial exception for used vehicles), and delegates a further list to
  시행령 제121조의2 -- which per the 법제처 explainer removes insurance and
  pension premiums, tuition and childcare costs, utilities and taxes, gift
  certificates and securities, tolls, financial fees, political donations
  claimed as a credit, and 전월세 deposits.
reasoning: >
  Graded at the strong band with a mandatory staleness gate, which is the same
  treatment the sibling investing lane gives Korean tax facts: codified rules
  are authoritative for their jurisdiction but are revocable by legislation, so
  they never sit at the top band reserved for things that cannot change. The
  item is worth a slot because it is the one place in this lane where a
  Korean household's own spending log is directly decision-relevant to a
  computable outcome, and because the naive version of the rule is wrong in two
  expensive directions. It is wrong on the threshold: a household that does not
  cross 25 percent of gross salary gets nothing, so optimising the payment mix
  below that line is wasted effort. And it is wrong on the base: a large share of
  ordinary household outflow -- rent deposits, utilities, insurance, tuition,
  tolls -- is not in the deduction base at all, so a ledger's grand total is NOT
  the figure the rule operates on. An agent that maps a user's categories onto
  the statutory base before saying anything about the deduction is doing the only
  part of this that requires the ledger; an agent that repeats the rate table is
  doing the part that will be stale within a year.
---

# spending-saving/kr-card-deduction-base-and-floor-015

The Korean card deduction is widely described as "체크카드 rate is higher, so use
체크카드." That is a true sentence about one row of a table, and it is the least
useful thing to know about the rule.

Three structural facts matter more, and all three are read directly from the
statute rather than from any card company's explainer.

First, there is a floor. Nothing is deductible at all until card and cash-receipt
spending passes 25 percent of gross salary, and spending abroad does not count
toward it. A household under that line gets nothing no matter how it pays, which
makes payment-mix optimisation below the threshold pure wasted effort. A
household well above it is operating only on the margin above the line.

Second, the rate ordering is real but it is a second-order lever: credit card at
the bottom, debit and prepaid cards and cash receipts in the middle, traditional
markets and public transport at the top. There is a culture and sports band as
well, at the middle rate, but it has historically carried an income eligibility
condition that was not confirmed here, so it should not be computed with until
that condition is read.

Third, and this is the part a ledger actually changes: much of what a household
spends is not in the base. Vehicle purchases are out. Insurance and pension
premiums are out. Tuition and childcare are out. Utilities and taxes are out.
Gift certificates, tolls, financial fees and rental deposits are out. So the
bottom line of a spending log is not the number the rule operates on, and the
gap between the two can be large for a household whose spending is concentrated
in housing, health and education. Mapping logged categories onto the statutory
base is the work; quoting the rate table is not.

Finally, the shelf life. This article is amended on the annual tax-revision
cycle, and the version read here took effect on the first of January 2026 under
an amendment passed the previous December. The shape -- a floor, an ordering, a
capped total, and a base with holes in it -- is stable. The percentages and the
caps are not, and should be re-read against the statute each filing season
rather than recited. Temporary single-year provisions also appear regularly and
none are carried here, so their absence is not evidence that none is in force.
