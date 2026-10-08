---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (work-career lane opening).
# Jurisdiction-bound item -- locale KR. Every figure below was read at the
# Korean National Tax Service on 2026-09-02. Structure is stored; rates and
# thresholds are staleness-gated and must be re-checked before use.
# Rubric: work-career.rubric.md @venture-obs row
# work-career/kr-freelance-tax-structure-019.
# Source re-audit 2026-10-03: NTS simplified-VAT page -- the KRW 104m
# threshold applies only outside the excluded industries, and listed personal
# services (VAT decree art. 42) supplied without employees or facilities are
# VAT-exempt. NTS notice 2026-10-01: the 3 -> 2 percent withholding cut is a government proposal awaiting the
# National Assembly, not enacted; effective date not confirmed at primary.
id: work-career/kr-freelance-tax-structure-019
domain: work-career
grade: B (codified regulatory fact, staleness-gated)
lane: "@venture-obs"
locale: KR
as_of: verified 2026-09-02 against the National Tax Service
contested: no
sources:
  - "National Tax Service (Korea), 사업자등록 신청. https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2444&cntntsId=7777 -- '사업개시 전 또는 사업을 시작한 날로부터 20일 이내에 구비서류를 갖추어 관할세무서 또는 가까운 세무서 민원봉사실에 신청하여야 함', legal basis 부가가치세법 제8조."
  - "National Tax Service (Korea), 사업소득 원천징수방법. https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=6622&cntntsId=7902 -- '원천징수의무자가 원천징수대상 사업소득금액의 3%을 원천징수'; remittance by the 10th of the following month."
  - "National Tax Service (Korea), 일반과세자와 간이과세자 비교. https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?mi=2480&cntntsId=7802 -- 간이과세자 threshold 연 매출 1억 4백만원 미만; 납부의무 면제 where 해당 과세기간 공급대가 합계액 4천8백만원 미만."
  - "National Tax Service (Korea), N잡러·프리랜서 세금 고민, 국세청과 국회가 직접 듣고 답합니다, 2026-10-01. https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?mi=2201&nttSn=1355351 -- '정부 세제개편안에는 인적용역소득자의 원천징수 세율이 3%에서 2%로 낮추는 내용이 포함'; NTS asks the National Assembly to finalise it."
  - "finance-investing/kr-tax-regime-staleness-gate-016 -- the standing rule that a Korean tax rate or threshold is asserted only with its verification date attached, and re-checked before it drives a decision."
claim: >
  The structural facts a Korean freelancer or side-business owner has to
  operate inside, each read at the National Tax Service and each carrying a
  verification date. (1) REGISTRATION: 사업자등록 must be applied for before
  starting the business or WITHIN 20 DAYS of the day the business starts, at
  the competent or nearest tax office, under 부가가치세법 제8조. (2)
  WITHHOLDING IS A PREPAYMENT, NOT A TAX BILL: the payer withholds 3 PERCENT
  of withholding-eligible 사업소득 and remits it by the 10th of the following
  month. The familiar '3.3 percent' is that 3 percent plus the local income
  tax special collection levied on it; the composite is the figure in
  practice, and the national 3 percent component is the part read at the NTS
  page. This is an ADVANCE PAYMENT settled at the following May's 종합소득세
  filing -- the final liability can be higher or lower, and over-withheld
  amounts come back as a refund. Treating 3.3 percent as the tax paid is the
  single most common error in this area. (3) VAT STATUS: 간이과세자 applies
  below 연 매출 1억 4백만원 for businesses outside the 간이과세 배제 업종 --
  and a freelancer supplying one of the personal services listed in
  부가가치세법 시행령 제42조 (writing, design, performance and similar) without
  employees or physical facilities is a 면세사업자, outside VAT altogether and
  filing a 사업장현황신고 instead -- with tax computed as 공급대가 x 업종별
  부가가치율 x 10 percent instead of the standard 공급가액 x 10 percent, and
  input credit limited to 공급대가 x 0.5 percent; where the period's 공급대가
  total is under 4천8백만원 the VAT payment obligation is EXEMPT. STALENESS
  GATE, live and specific: the 2026 government tax reform package proposes
  cutting the personal-services withholding rate from 3 percent to 2 percent
  (3.3 to 2.2 percent composite), reported in the press as taking effect
  from 2027. The NTS confirmed on 2026-10-01 that this is a government
  PROPOSAL awaiting the National Assembly; enactment and effective date were
  not verified at a primary source, and it is recorded here only as a reason
  to re-check the rate rather than recall it.
reasoning: >
  Written as a STRUCTURE item with numbers attached rather than as a rate
  table, for the same reason the finance lane's Korean gate is written that
  way: the structure is stable and the numbers are legislated. Sits at the
  strong band rather than the top because every figure is revocable by statute
  or 시행령 -- the 간이과세 threshold itself moved from 8천만원 to 1억 4백만원
  on 2024-07-01, within the memory of most material still in circulation. The
  single most decision-relevant fact here is not a rate at all: it is that the
  3.3 percent is a prepayment, which means a freelancer who does not file in
  May may simply be leaving a refund uncollected. Deliberately NOT stored: any
  4대보험 obligation, the 사업장현황신고 deadline for 면세사업자, and the
  홈택스 filing procedure -- none was read at a primary source in this pass,
  and each is recorded in GAPS.md instead of being inferred.
---

# work-career/kr-freelance-tax-structure-019

The structural facts a Korean freelancer or side-business owner works inside,
each checked at the tax authority rather than recalled.

Registration. 사업자등록 has to be applied for either before the business
starts or within 20 days of the day it starts.

The 3.3 percent is not your tax bill. When a client pays you, they withhold 3
percent of the eligible business income and remit it by the 10th of the
following month; the familiar 3.3 percent is that plus the local income tax
levied on it. This is a PREPAYMENT. It gets settled at the following May's
종합소득세 filing against your actual income and deductions. Your real
liability can be higher, and it can be much lower -- in which case the
difference is refunded.

That last point is the one that costs people money. Someone who has had 3.3
percent taken all year and never files in May has not paid their taxes and
moved on; they have quite possibly left a refund sitting there.

VAT status. First check whether you are in VAT at all: many personal services
(writing, design, performance and similar, as listed in the VAT decree)
supplied without employees or physical facilities are VAT-exempt
(면세사업자), which means no VAT but a 사업장현황신고. If you are in VAT, below
연 매출 1억 4백만원 you fall under 간이과세, unless your business is in an
excluded industry (간이과세 배제 업종), and there the tax
is computed on 공급대가 times an industry value-added rate times 10 percent
rather than the standard 10 percent of 공급가액, and input credits are limited
to 0.5 percent of 공급대가. Below 4천8백만원 of 공급대가 in the period, the
VAT payment obligation is waived entirely.

Now the part that matters most for storing any of this. These numbers are
legislated and they move. The 간이과세 threshold itself went from 8천만원 to
1억 4백만원 on 1 July 2024, which means a great deal of guidance still online
is simply wrong. And the 2026 tax reform package proposes cutting the
personal-services withholding rate from 3 percent to 2 percent -- the NTS
confirmed the proposal on 1 October 2026, but it still needed the National
Assembly, and the 2027 start date is from press reports, not confirmed here.

So the operating rule is the same one this warehouse already applies to
Korean investment tax: store the structure, re-check the number before it
drives a decision.
