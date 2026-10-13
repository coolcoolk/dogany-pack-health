---
# Finance GAPS sprint 2026-10-06 (dispatch kw-finance-newitems). Closes the
# v12 refusal "KR PENSION-ACCOUNT TAX CREDIT" by doing what that entry asked:
# the article text was read at 국가법령정보센터 (law.go.kr) on 2026-10-06 and
# every parameter below carries that verification date and its article.
# Jurisdiction-bound item -- locale KR. Staleness-gated by
# finance-investing/kr-tax-regime-staleness-gate-016: these are exactly the
# parameters the annual tax-revision cycle moves.
# Read at source: 소득세법 제59조의3 (text in force 2026-01-01, unchanged in the
# 2026-07-01 version; 법률 제21221호, 2025-12-23 개정), 제14조 제3항 제9호,
# 제21조 제1항 제21호, 제64조의4, 제129조 제1항 제5호의2 and 제6호;
# 조세특례제한법 제91조의18 (version in force 2026-09-18, 법률 제21467호).
# NOT read: the age-banded pension withholding rate table inside 제129조
# 제1항 제5호의2 가목 (rendered as a table image), the ISA annual contribution
# formula in 제91조의18 제3항 제5호 (rendered as a formula image), the
# 지방세법 local-income-tax surtax, and every 시행령 detail. Those numbers are
# NOT stored.
#
# wrapper_parameters is structured data for a tax / account module. Each row:
# the value, the article it was read from, and verified_on. A row past its
# reverify_by date must be re-read before it drives a decision (016).
id: finance-investing/kr-pension-isa-wrapper-structure-073
domain: finance-investing
grade: B (codified regulatory fact, staleness-gated)
lane: "@quant-market"
locale: KR
as_of: statute text in force 2026-01-01 / 2026-09-18, verified 2026-10-06
contested: no
sources:
  - "소득세법 제59조의3 (연금계좌세액공제), 국가법령정보센터. https://www.law.go.kr/lsLawLinkInfo.do?lsJoLnkSeq=1001059881&chrClsCd=010202 -- read 2026-10-06."
  - "소득세법 제14조 제3항 제9호 (분리과세연금소득), 제21조 제1항 제21호 (연금외수령 기타소득), 제64조의4 (연금소득 세액 계산 특례), 제129조 제1항 제5호의2 및 제6호 나목 (원천징수세율), 국가법령정보센터. https://www.law.go.kr/법령/소득세법 -- read 2026-10-06."
  - "조세특례제한법 제91조의18 (개인종합자산관리계좌에 대한 과세특례), 국가법령정보센터. https://www.law.go.kr/법령/조세특례제한법/제91조의18 -- read 2026-10-06."
  - "finance-investing/kr-tax-regime-staleness-gate-016"  # within-warehouse: the gate that governs every number below
  - "finance-investing/kr-foreign-stock-cgt-015"  # within-warehouse: the taxable-account regime these wrappers sit beside
  - "finance-investing/kr-domestic-stock-cgt-exemption-014"  # within-warehouse: domestic listed shares outside a wrapper
  - "finance-investing/fee-drag-compounding-071"  # within-warehouse: a wrapper's tax saving is weighed against its product fees
wrapper_parameters:
  verified_on: 2026-10-06
  reverify_by: 2027-01-31
  reverify_rule: re-read after each December tax-law plenary and before any January-onward decision; a row past reverify_by is spoken only as structure, without its number
  rows:
    - key: pension_credit_rate_base
      value: 0.12
      meaning: national income-tax credit on eligible pension-account contributions
      article: 소득세법 59조의3 1항
    - key: pension_credit_rate_low_income
      value: 0.15
      applies_if: 종합소득금액 4,500만원 이하, or 총급여 5,500만원 이하 when wage income is the only income
      article: 소득세법 59조의3 1항
    - key: pension_savings_cap_krw
      value: 6000000
      meaning: 연금저축계좌 contributions above this in a year are ignored for the credit
      article: 소득세법 59조의3 1항 단서
    - key: pension_combined_cap_krw
      value: 9000000
      meaning: 연금저축 (up to its own cap) plus 퇴직연금계좌 (IRP and similar) contributions above this are ignored
      article: 소득세법 59조의3 1항 단서
    - key: isa_conversion_extra
      value: "min(0.10 x converted amount, 3,000,000 KRW)"
      meaning: extra credit base when a matured ISA balance is moved into a pension account, on top of the 9m cap; split across two years if paid in across two years
      article: 소득세법 59조의3 3항-4항; 조특법 91조의18 11항
    - key: private_pension_separate_tax_threshold_krw
      value: 15000000
      meaning: annual private-pension income (excluding pensioned retirement income and hardship withdrawals) at or below this may stay out of global income
      article: 소득세법 14조 3항 9호 다목
    - key: private_pension_above_threshold
      value: "choose: global taxation, or 15 pct on that pension income"
      article: 소득세법 64조의4
    - key: pension_non_annuity_withdrawal_rate
      value: 0.15
      meaning: credited contributions and their earnings taken out other than as pension (연금외수령) are other income withheld at 15 pct
      article: 소득세법 21조 1항 21호; 129조 1항 6호 나목
    - key: pension_annuity_withholding
      value: age-banded low rate; 3 pct for a qualifying lifetime contract
      note: the age table is not stored (not read as text)
      article: 소득세법 129조 1항 5호의2
    - key: isa_eligibility
      value: resident aged 19 or over, or 15 or over with wage income in the prior tax year
      article: 조특법 91조의18 1항
    - key: isa_tax_free_krw_general
      value: 2000000
      article: 조특법 91조의18 2항 2호
    - key: isa_tax_free_krw_low_income
      value: 4000000
      applies_if: prior-year 총급여 5,000만원 이하, or 종합소득금액 3,800만원 이하 with 총급여 not over 5,000만원, or qualifying farmers/fishers
      article: 조특법 91조의18 2항 1호
    - key: isa_excess_rate
      value: 0.09
      meaning: interest and dividend income above the tax-free amount, taxed separately at 9 pct and kept out of global income
      article: 조특법 91조의18 1항
    - key: isa_loss_netting
      value: true
      meaning: income is computed at termination after netting losses inside the account
      article: 조특법 91조의18 5항
    - key: isa_min_term_years
      value: 3
      meaning: terminating before 3 years (or withdrawing more than total contributions before 3 years) claws back the relief, except death, emigration and other listed hardship
      article: 조특법 91조의18 3항 4호, 7항, 8항
    - key: isa_total_cap_krw
      value: 100000000
      article: 조특법 91조의18 3항 5호
    - key: isa_one_account
      value: true
      article: 조특법 91조의18 3항 1호
    - key: isa_foreign_funds_excluded
      value: true
      meaning: foreign collective investment securities cannot be held; domestic-listed funds and listed shares can
      article: 조특법 91조의18 3항 3호
not_stored:
  - local income tax surtax (the commonly quoted 13.2 / 16.5 pct credit rates assume a 10 pct local surtax on the national figure; 지방세법 not read)
  - ISA annual contribution limit (formula image not read)
  - age-banded pension withholding rates
  - whether a credit larger than the computed tax has any value (general credit-limit rule not read in this pass)
claim: >
  Korea's two tax wrappers for an individual investor work on different
  mechanisms, and the mechanism matters more than the rate. Pension accounts
  (연금저축 and 퇴직연금계좌 such as IRP) give a credit at contribution time:
  12 percent of eligible contributions against national income tax, or 15
  percent for a taxpayer with global income of 45 million KRW or less (total
  salary of 55 million KRW or less when wages are the only income); 연금저축
  counts up to 6 million KRW a year and 연금저축 plus 퇴직연금 together up to 9
  million KRW. The price is a lock-up: credited money and its earnings taken
  out other than as a pension are taxed as other income at 15 percent, while
  money taken as a pension is taxed at a low age-banded rate, and private
  pension income above 15 million KRW a year must either join global income
  or be taxed at 15 percent. The ISA gives no upfront credit; it shelters
  interest and dividend income inside the account at termination, after
  netting losses, with 2 million KRW tax-free (4 million for the
  lower-income band) and the excess taxed separately at 9 percent, on a
  3-year minimum term with clawback for earlier termination, one account per
  person, 100 million KRW lifetime contributions, and no foreign-domiciled
  funds. A matured ISA moved into a pension account adds a credit base of 10
  percent of the moved amount, capped at 3 million KRW, on top of the 9
  million cap. Every number here was read from the statute on 2026-10-06 and
  expires on the tax-revision cycle (016).
reasoning: >
  Same treatment and same band as items 014 and 015: codified and read at
  the authoritative primary (the statute text itself, which is stronger than
  the NTS guidance pages those items used), but revocable by legislation
  every December, so it sits at the strong band with a hard staleness gate
  instead of the top band. Parameters that rendered as images (the age
  withholding table, the ISA annual limit formula) and anything that lives
  in 지방세법 or a 시행령 were not read and are listed under not_stored
  rather than filled from brokerage material, which is the failure the v12
  refusal named. The item states structure and verified parameters only; it
  deliberately does not say which wrapper a user should use, because that
  depends on income band, liquidity needs and horizon, and no evidence read
  here ranks them for an individual. What the engine can do with it is
  arithmetic: the eligible credit base and the national credit rate for a
  stated income band, the ISA tax-free band, and the lock-up terms to show
  next to them.
---

# finance-investing/kr-pension-isa-wrapper-structure-073 -- 연금저축·IRP·ISA, 구조와 확인된 숫자

**한 줄 그림:** 연금계좌는 넣을 때 세금을 깎아 주고 대신 묶인다. ISA는 계좌 안의 이자·배당에 세금을
덜 매기고 3년을 묶는다. 숫자는 2026-10-06에 법조문으로 확인했고, 매년 다시 확인한다.

## Credit base (engine-readable)

```
eligible = min( min(연금저축, 6,000,000) + 퇴직연금계좌, 9,000,000 )
         + min( 0.10 x ISA_converted, 3,000,000 )      # only in the year(s) a matured ISA is moved in
national_credit = eligible x rate
rate = 0.15  if 종합소득금액 <= 45,000,000 (wages only: 총급여 <= 55,000,000)
       0.12  otherwise
```

The local income tax surtax is not in this formula; the commonly quoted
13.2 / 16.5 percent rates add it and were not read at source. Whether a
credit larger than the user's computed tax has any value was not checked;
the engine says so rather than assuming.

## The two wrappers side by side

| | Pension account (연금저축, IRP) | ISA |
|---|---|---|
| when the benefit lands | contribution year (tax credit) | termination (tax on account income) |
| benefit | 12% or 15% of eligible contributions | 2m KRW tax-free (4m low-income band), excess 9% separate |
| losses | n/a | netted inside the account |
| lock-up | non-pension withdrawal of credited money and earnings: 15% | under 3 years: relief clawed back |
| exit | pension income; over 15m KRW a year: global or 15% | may roll into a pension account for an extra credit base |
| holdings limit | (not read) | no foreign-domiciled funds |

## 한국어 요약 (답변용)

- 연금저축·IRP는 넣는 해에 세금을 돌려받는 계좌다. 공제율은 국세 기준 12%이고, 종합소득금액
  4,500만원 이하(근로소득만 있으면 총급여 5,500만원 이하)는 15%다. 연금저축은 연 600만원까지,
  연금저축과 퇴직연금계좌(IRP 등)를 합쳐 연 900만원까지만 공제 대상이 된다. 흔히 말하는 13.2%·
  16.5%는 여기에 지방소득세 10%를 더한 값인데, 지방세법 조문은 이번에 직접 확인하지 않았다.
- 대신 돈이 묶인다. 공제받은 돈과 그 수익을 연금이 아닌 방식으로 빼면 기타소득으로 15%가
  원천징수된다. 연금으로 받으면 나이에 따라 낮은 세율이 붙고, 사적연금 소득이 연 1,500만원을
  넘으면 종합과세와 15% 분리과세 중에서 고른다.
- ISA는 넣을 때 공제가 없다. 대신 계좌 안에서 생긴 이자·배당을 해지할 때 손실과 합쳐 계산하고,
  200만원(서민형 기준에 맞으면 400만원)까지 비과세, 넘는 부분은 9%로 따로 과세하고 종합소득에
  합치지 않는다. 3년 안에 해지하거나 낸 돈보다 많이 빼면 혜택을 토해 낸다(사망·해외이주 등 예외).
  1인 1계좌, 총 납입 1억원 한도, 해외에 설정된 펀드는 담을 수 없다.
- 만기된 ISA를 연금계좌로 옮기면 옮긴 금액의 10%, 최대 300만원이 900만원 한도 위에 공제 대상으로
  더해진다.
- 이 숫자들은 2026-10-06에 국가법령정보센터 조문으로 확인했다. 세법은 매년 12월에 바뀌므로
  확인일과 함께 말하고, 2027년 1월 말이 지나면 다시 확인하기 전에는 숫자 없이 구조만 말한다.
  ISA 연간 납입한도, 나이별 연금소득세율, 지방소득세는 이번에 확인하지 못해 말하지 않는다.
- 어느 계좌를 써야 하는지는 소득 구간, 중간에 돈이 필요할 가능성, 투자 기간에 따라 다르고, 이를 가려
  주는 연구는 찾지 못했다. 그래서 추천하지 않고, 사용자의 조건으로 공제 대상 금액과 묶이는 조건을
  나란히 계산해 보여 준다.
