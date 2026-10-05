---
# Authored 2026-09-02 (travel-lane opening sprint). KR-LOCALE item,
# @travel-advisory (VC-F). The only item in this lane where getting it wrong is
# a criminal matter rather than a health matter, and it carries a live staleness
# trap: the penalty for visiting a banned country CHANGED five days before this
# item was written. Every widely circulating summary, and any model answering
# from memory, still has the old numbers. The statute was read directly from the
# national legal information service rather than from any secondary page.
id: travel/kr-travel-ban-legal-gate-008
domain: travel
lane: "@travel-advisory"
grade: A (jurisdictional-statute)
locale: KR
as_of: 2026-08-28
contested: no
sources:
  - "https://www.law.go.kr/DRF/lawService.do?OC=test&target=law&type=XML&LM=%EC%97%AC%EA%B6%8C%EB%B2%95"  # 법제처 국가법령정보센터 (Korea Ministry of Government Legislation, national statute service) machine-readable text of 여권법 (Passport Act), 법령ID 000006. Retrieved and read verbatim 2026-09-02; current text as promulgated 2026-02-27 by 법률 제21383호, in force from 2026-08-28. All article text below is quoted from this record
  - "https://0404.go.kr/"  # 외교부 해외안전여행 (Ministry of Foreign Affairs official travel-safety portal). Retrieved 2026-09-02 for the four-tier 여행경보 table and the 특별여행주의보 definition, quoted verbatim below
  - "source:finance-investing/kr-tax-regime-staleness-gate-016 -- the warehouse's existing Korean-regime staleness gate. This item is the second member of that family and the reason the family needed to exist"
  - "source:cooking/kr-histamine-blue-fish-008 -- the edition-check failure this warehouse has already paid for once"
  - "framework:jurisdictional-statute -- a statute is definitive about its own contents, which is why the confidence band is the top one. It is definitive about NOTHING ELSE: whether a given country is currently designated, and whether an individual's circumstances qualify for an exception, are questions for the current 고시 and for the ministry, not for this item."
refraction_notes:
  - note: >
      THE PENALTY CHANGED ON 2026-08-28 AND THE OLD NUMBER IS EVERYWHERE. Under
      법률 제21383호, promulgated 2026-02-27 and in force six months later, the
      offence of visiting or staying in a 방문ㆍ체류 금지 country without permission
      was moved OUT of 여권법 제26조 (제26조제3호 삭제 <2026.2.27>) and INTO 제24조
      as a new 제2호. 제24조's penalty band is 3년 이하의 징역 또는 3천만원 이하의
      벌금. The legislature's own stated reason, in the 제개정이유 attached to the
      amendment, is that the penalty was raised 1년 이하의 징역 또는 1천만원 이하의
      벌금에서 3년 이하의 징역 또는 3천만원 이하의 벌금으로. Anything -- a blog, a
      summary, a model answering from memory -- that says one year or ten million
      won is quoting the law as it stood until five days before this item was
      written.
    grade: A
  - note: >
      THE OPERATIVE LEGAL TRIGGER IS THE 고시, NOT THE COLOUR OF THE ADVISORY.
      제17조제1항 lets the Minister of Foreign Affairs, on a 국외 위난상황 of the
      kind prescribed by Presidential Decree, restrict passport use or prohibit
      visiting and staying in a named country or region for a set period; 제17조제2항
      requires that this be published as a 고시. 제24조제2호 then penalises a person
      who, KNOWING that the country or region has been so published, visits or
      stays without the 제17조제1항 단서 permission. So the criminal exposure
      attaches to the published prohibition. The four-tier advisory system is the
      ministry's presentation layer over it, and the authoritative check before a
      trip is the current designation, not a remembered colour.
    grade: A
  - note: >
      THE EXCEPTION ROUTE EXISTS AND IS NAMED IN THE STATUTE. 제17조제1항 단서
      allows the Minister to permit passport use and visiting or staying for
      travel of a purpose prescribed by Presidential Decree -- 영주(永住),
      취재ㆍ보도, 긴급한 인도적 사유, 공무 등 -- where the Minister considers it
      necessary. The correct output for a user with a real reason to go somewhere
      banned is therefore not "you cannot," it is that a permission process exists,
      it is discretionary, it must be obtained BEFORE travelling, and it goes to
      the ministry. Note also 제17조제4항: the Minister must first submit the matter
      to the 여권정책협의회, renamed from the previous body by the 2023-03-28
      amendment.
    grade: A
  - note: >
      THE FOUR ADVISORY TIERS, QUOTED FROM THE MINISTRY'S OWN PORTAL. 1단계 여행유의
      (남색경보), described as 국내 대도시보다 상당히 높은 수준의 위험, with the
      action 신변안전 위험 요인 숙지ㆍ대비. 2단계 여행자제 (황색경보), 국내 대도시보다
      매우 높은 수준의 위험, with 불필요한 여행 자제 for the intending traveller and
      신변안전 특별유의 for someone already there. 3단계 출국권고 (적색경보), 국민의
      생명과 안전을 위협하는 심각한 수준의 위험, with 여행 취소ㆍ연기 and 긴요한
      용무가 아닌 한 출국. 4단계 여행금지 (흑색경보), 매우 심각한 수준의 위험, with
      여행금지 준수 and 즉시 대피ㆍ철수. Separately, 특별여행주의보 covers 단기적으로
      긴급한 위험 and its action level is stated as 2단계 이상 3단계 이하에 준함.
    grade: A
  - note: >
      TIERS ONE TO THREE ARE ADVICE. Read against 제24조제2호, which penalises only
      travel to a country published as prohibited under 제17조, the first three
      tiers carry no criminal penalty of their own. That distinction is worth
      stating because the tiers are frequently spoken as if they were a graduated
      legal scale. They are graduated ADVICE, and the legal cliff is at the fourth
      tier. What this item did NOT separately verify is whether every 4단계
      designation is invariably accompanied by a 제17조 고시; the statute is clear
      that the 고시 is what the offence attaches to, so the 고시 is what to check.
    grade: B
  - note: >
      OUT OF SCOPE HERE, AND IT IS THE PART THAT GOES STALE FASTEST. Which
      countries and regions are currently designated, at any tier. That list moves
      with events, it is published by the ministry, and NOTHING in this warehouse
      should ever answer it from memory. This item exists to make a session go and
      look, and to make sure that when it does look it knows what the tiers mean
      and what the penalty now is. Travel insurance consequences of a designation
      are also out of scope: no source for them was located in this pass.
    grade: A
claim: >
  Korea's travel advisory system has four tiers, and only the fourth has criminal
  force. The Ministry of Foreign Affairs publishes 1단계 여행유의 (남색경보), 2단계
  여행자제 (황색경보), 3단계 출국권고 (적색경보) and 4단계 여행금지 (흑색경보), plus a
  특별여행주의보 for 단기적으로 긴급한 위험 whose action level is stated as 2단계 이상
  3단계 이하에 준함. The legal instrument behind the fourth tier is 여권법 제17조:
  the Minister may, on a prescribed 국외 위난상황, restrict passport use or prohibit
  visiting and staying in a named country or region for a fixed period, and must
  publish this as a 고시, having first put it to the 여권정책협의회. 제17조제1항 단서
  provides a discretionary permission route for travel of prescribed purposes --
  영주, 취재ㆍ보도, 긴급한 인도적 사유, 공무 등. A person who knowingly visits or
  stays in a published prohibited country or region without that permission commits
  an offence. AS OF 2026-08-28 that offence sits in 여권법 제24조제2호 and carries
  3년 이하의 징역 또는 3천만원 이하의 벌금. It previously sat in 제26조제3호 and
  carried 1년 이하의 징역 또는 1천만원 이하의 벌금; 법률 제21383호, promulgated
  2026-02-27 and in force from 2026-08-28, deleted 제26조제3호, added the offence to
  제24조, and states in its 제개정이유 that the penalty was raised from the former
  band to the latter. The criminal exposure attaches to the published prohibition,
  not to the advisory colour, so the current 고시 is the thing to check.
reasoning: >
  This is the one item in the lane where a wrong answer is a criminal-liability
  answer rather than a health answer, and it is also the item with the shortest
  half-life, which is why it was sourced from the statute itself rather than from
  any explanatory page. The text was pulled from the national legal information
  service's machine-readable record of 여권법, so confidence about what the law says
  is at the top band with a jurisdictional qualifier -- the same treatment this
  warehouse gives a regulator describing its own guidance, for the same reason: a
  statute is definitive about its own contents. It earns a slot on three grounds.
  It is genuinely Korean rather than an import, so no foreign source could stand in
  for it. It is the kind of fact a life agent might be asked about casually and
  could answer confidently and wrongly. And it contains a live staleness trap of
  precisely the sort this warehouse has already been caught by twice. The trap is
  worth spelling out: until 2026-08-28 the penalty was one year and ten million
  won, and that is the figure in essentially every secondary summary, every blog,
  and any model whose training predates the amendment. Since 2026-08-28 it is three
  years and thirty million won, the offence has moved to a different article, and
  the legislature's own 제개정이유 says the change was made to raise the penalty. The
  amendment is five days old at the time of writing. The second thing the item does
  deliberately is separate the advisory system from the legal one. The four tiers
  read like a legal escalation and they are not; 제24조제2호 attaches the offence to
  a published prohibition under 제17조, which means the legally operative object is
  the 고시. Stating that keeps a session from treating a remembered colour as a
  legal fact. What the item refuses to carry is the country list, in any form. That
  list changes with events, it is the ministry's to publish, and the entire purpose
  of this entry is to make a session go and look it up rather than recall it.
---

# travel/kr-travel-ban-legal-gate-008

Korea's travel advisories look like a four-step warning scale. Three of the steps
are advice. The fourth is a criminal statute.

The ministry's own tiers, in its own words:

- **1단계 여행유의 (남색경보)** -- 국내 대도시보다 상당히 높은 수준의 위험. Action:
  신변안전 위험 요인 숙지ㆍ대비.
- **2단계 여행자제 (황색경보)** -- 국내 대도시보다 매우 높은 수준의 위험. Intending
  travellers: 불필요한 여행 자제. Those already there: 신변안전 특별유의.
- **3단계 출국권고 (적색경보)** -- 국민의 생명과 안전을 위협하는 심각한 수준의 위험.
  여행 취소ㆍ연기, and 긴요한 용무가 아닌 한 출국.
- **4단계 여행금지 (흑색경보)** -- 매우 심각한 수준의 위험. 여행금지 준수, 즉시
  대피ㆍ철수.

There is also a 특별여행주의보 for 단기적으로 긴급한 위험, whose action level the
ministry states as 2단계 이상 3단계 이하에 준함.

Underneath the fourth tier is 여권법 제17조. It lets the Minister of Foreign
Affairs, faced with a prescribed 국외 위난상황 -- 천재지변ㆍ전쟁ㆍ내란ㆍ폭동ㆍ테러 and
the like -- restrict passport use or prohibit visiting and staying in a named
country or region for a set period. That decision has to be published as a 고시,
and it has to go through the 여권정책협의회 first.

Going anyway is an offence. Knowing that a country has been published as
prohibited, and visiting or staying there without permission, is punishable.

And here is the part that matters right now.

**The penalty changed on 28 August 2026.** Until then the offence sat in 여권법
제26조제3호 and carried 1년 이하의 징역 또는 1천만원 이하의 벌금. 법률 제21383호,
promulgated on 27 February 2026 and in force six months later, deleted that
provision and moved the offence into 제24조 as a new second item -- where the
penalty band is 3년 이하의 징역 또는 3천만원 이하의 벌금. The amendment's own stated
reason says exactly that: the sentence was raised from the first band to the
second.

That amendment is five days old. Every summary written before it, and any answer
produced from memory rather than from the statute, will give the old figure. If
this warehouse is asked, the answer is three years and thirty million won, and the
answer should carry the date it became true.

Two more things worth holding.

The exception route is real and it is in the statute. 제17조제1항's proviso lets
the Minister permit passport use and travel for prescribed purposes -- 영주,
취재ㆍ보도, 긴급한 인도적 사유, 공무 and others set by decree -- where he considers
it necessary. So someone with a genuine reason to go somewhere banned is not
simply told no. They are told there is a permission process, it is discretionary,
and it happens before departure, not after.

And the legally operative object is the 고시, not the colour. The offence is
defined against a country published as prohibited under 제17조. Which countries
those currently are changes with events, this warehouse does not carry the list,
and no session should ever recite one from memory. Go and look.
