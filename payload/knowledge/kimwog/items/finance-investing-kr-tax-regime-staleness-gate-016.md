---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-09-02 (finance-investing lane opening).
# Jurisdiction-bound rule -- locale KR. The worked example is verified against
# the Korean National Assembly Budget Office primary publication.
# Rubric: finance-investing.rubric.md @quant-market row
# finance-investing/kr-tax-regime-staleness-gate-016.
id: finance-investing/kr-tax-regime-staleness-gate-016
domain: finance-investing
grade: B (jurisdiction rule)
lane: "@quant-market"
locale: KR
as_of: 2024-12-10 (National Assembly plenary) / rule written 2026-09-02
contested: no
sources:
  - "National Assembly Budget Office (Korea), 나보포커스 제82호 (2024.12.18), 2024년 개정세법 심의 결과 및 주요 내용, 추계세제분석실 세제분석1과. https://www.nabo.go.kr/board/file/down.do?fid=33318358 -- states that at the 418th National Assembly plenary session on 2024.12.10, 소득세법 was passed as submitted, with 금융투자소득세 폐지 and 가상자산소득 과세 유예 from 2025 to 2027."
  - "National Tax Service (Korea), 주식등 양도소득세 과세대상. https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800 -- the current regime that remains in force after the repeal."
claim: >
  Korean investment tax parameters change on a legislative cycle fast enough
  that any stored NUMBER must be treated as expiring, while the STRUCTURE is
  what is safe to store. Worked example, verified at the primary source: the
  financial investment income tax (금융투자소득세), which was legislated in
  2020 and scheduled to take effect on 2025-01-01, was REPEALED -- the
  National Assembly Budget Office records that the 소득세법 amendment
  containing 금융투자소득세 폐지 passed the plenary session on 2024-12-10,
  and that the existing capital gains tax regime for shares remains in force.
  Any Korean investing guidance written before 2025 that assumes 금투세 takes
  effect is therefore WRONG, and that includes a large volume of material
  still in circulation. Operating rule for this lane: a Korean tax RATE or
  THRESHOLD is never asserted from stored knowledge alone; it is asserted
  only with its verification date attached, and re-checked against the
  National Tax Service or 국가법령정보센터 before it drives a decision. The
  securities transaction tax rate is the standing example: it is set by
  증권거래세법 제8조 and its 시행령 제5조, has been amended repeatedly in
  recent years, and is therefore stored in NO item in this lane -- it is
  looked up, never recalled.
reasoning: >
  This is a jurisdiction-staleness GATE rather than a fact about investing,
  which is why it is written as a rule with one verified worked example
  rather than as a table of current rates. A table would be the exact failure
  mode it exists to prevent. It sits at the strong band because the worked
  example is confirmed at a government primary source, while the general
  proposition (Korean investment tax changes fast) is a structural
  observation about the legislative cycle rather than a measured claim.
---

# finance-investing/kr-tax-regime-staleness-gate-016

Korean investment tax parameters move fast enough that storing them is a
liability. Store the structure, verify the numbers.

The clearest worked example is the financial investment income tax. It was
legislated in 2020, repeatedly delayed, and scheduled to take effect on 1
January 2025 -- and then repealed outright: the National Assembly passed the
income tax amendment containing the repeal at its plenary session on 10
December 2024, leaving the existing share capital gains regime in place.
Anything written before 2025 that plans around that tax arriving is simply
wrong, and a great deal of such material is still in circulation and still
reads as authoritative.

The securities transaction tax is the standing example of the same problem.
Its rate lives in the securities transaction tax act and its enforcement
decree, has been amended repeatedly in recent years, and is deliberately not
stored anywhere in this lane. It is looked up, never recalled.

The rule this produces: never state a Korean tax rate or threshold from
memory. State it with the date it was verified, and re-verify it against the
National Tax Service or the national law information service before it is
allowed to change a decision. Structure -- who is taxed, on what event,
whether losses are recognised, whether a deduction resets annually -- is
durable and can be reasoned about. Numbers are not.
