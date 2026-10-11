---
# Authored 2026-10-06 (travel source re-audit, dispatch kw-reaudit-travel-2).
# KR-LOCALE item, @travel-advisory (VC-F). Closes the GAPS entry "검역감염병
# 오염지역 -- the designation mechanism, not the list" and corrects item 009,
# which used a pre-2020 term. 오염지역 and 오염인근지역 were replaced by 검역관리지역
# and 중점검역관리지역 in 2020; the duty a returning traveller actually has depends
# on WHICH of the two tiers they were in and on whether they have symptoms, which
# the KDCA consumer page words more broadly than the statute does. Read from the
# statute and its enforcement rule on the national legal service (machine-readable
# records), plus the KDCA quarantine portal's own system page. No applicability
# .axes block: a statutory rule, not a personalised estimate. The list of areas
# currently designated is NOT carried in any form: it moves with events and is
# the KDCA's to publish. The structured blocks below (declaration_rules,
# max_incubation_days, designation, penalties) are for a trip-return reminder:
# they take a live tier, a departure date and a symptom answer, never a country.
id: travel/kr-quarantine-area-declaration-duty-070
domain: travel
lane: "@travel-advisory"
grade: A (jurisdictional-statute)
locale: KR
as_of: 2026-10-01
contested: no
sources:
  - "https://www.law.go.kr/DRF/lawService.do?OC=test&target=law&type=XML&LM=%EA%B2%80%EC%97%AD%EB%B2%95"  # 법제처 국가법령정보센터 machine-readable text of 검역법, 법령ID 001790; current version 법률 제21255호, 공포 2025-12-30, 시행 2026-07-01. Retrieved and read verbatim 2026-10-06 (제2조, 제5조, 제12조, 제12조의2, 제17조, 제39조, 제41조, 부칙)
  - "https://www.law.go.kr/DRF/lawService.do?OC=test&target=law&type=XML&LM=%EA%B2%80%EC%97%AD%EB%B2%95%20%EC%8B%9C%ED%96%89%EA%B7%9C%EC%B9%99"  # 법제처 machine-readable text of 검역법 시행규칙 (보건복지부령), 법령ID 006197; current version 제1195호, 공포 2026-08-31, 시행 2026-10-01. Retrieved and read verbatim 2026-10-06 (제2조, 제6조의2, 제6조의3, 제6조의4, 제14조의3, 별지 제7호서식, 제개정이유)
  - "https://travelhealth.kdca.go.kr/travel/www/QRNTN_MNG_AREA/QRNTN_MNG_AREA_SYS.jsp"  # 질병관리청 검역정보 포털 (formerly the nqs.kdca.go.kr pages), 중점검역관리지역 > 제도 소개. Retrieved and read 2026-10-06; the consumer wording of the two tiers, of the designation process and of who declares, with the 제12조의2 text quoted underneath
  - "https://www.kdca.go.kr/kdca/4915/subview.do"  # 질병관리청 해외감염병예방수칙 consumer page. Retrieved and read 2026-10-06 for the broader wording of the Q-CODE duty, quoted below
  - "source:travel/kr-pretravel-decision-structure-009 -- the pre-travel route this duty completes; that item used the pre-2020 term 오염지역 and stated the Q-CODE duty without its condition, both now corrected there"
  - "source:travel/kr-travel-ban-legal-gate-008 -- the other Korean statute gate; same rule: the tier or colour is not the legal object, the current designation is, and nothing here answers from memory"
  - "source:finance-investing/kr-tax-regime-staleness-gate-016 -- the warehouse's staleness-gate pattern; this item carries a live example (the plague figure below)"
  - "framework:jurisdictional-statute -- a statute and its enforcement rule are definitive about their own contents. They are definitive about NOTHING ELSE: whether a given country is a 검역관리지역 today, which disease it is designated for, and how a quarantine officer applies the rule to one traveller are questions for the current KDCA designation and for the 검역소장."
declaration_rules:
  - tier: 중점검역관리지역
    stayed_or_transited: true
    needs_suspect_symptoms: false
    duty: declare the stay or transit and health status to the 검역소장
    window: from leaving the area until the disease's maximum incubation period has elapsed
    basis: 검역법 제12조의2제1항제2호
  - tier: 검역관리지역
    stayed_or_transited: true
    needs_suspect_symptoms: true
    duty: declare the stay or transit and health status to the 검역소장
    window: from leaving the area until the disease's maximum incubation period has elapsed
    basis: 검역법 제12조의2제1항제1호
max_incubation_days:
  - disease: 콜레라
    days: 5
    basis: 검역법 시행규칙 제14조의3제1호
  - disease: 페스트
    days: 7
    basis: 제14조의3제2호; was 6 until 보건복지부령 제1195호 took effect on 2026-10-01
  - disease: 황열
    days: 6
    basis: 제14조의3제3호
  - disease: 중증 급성호흡기 증후군(SARS)
    days: 10
    basis: 제14조의3제4호
  - disease: 동물인플루엔자 인체감염증
    days: 10
    basis: 제14조의3제5호
  - disease: 중동 호흡기 증후군(MERS)
    days: 14
    basis: 제14조의3제6호
  - disease: 에볼라바이러스병
    days: 21
    basis: 제14조의3제7호
  - disease: 신종인플루엔자 and any disease the 질병관리청장 notifies under 검역법 제2조제1호자목
    days: set by the 검역전문위원회, not carried
    basis: 제14조의3제8호
designation:
  decides: 질병관리청장
  after: deliberation by the 검역전문위원회
  criteria: WHO IHR information on a quarantine disease; a risk of importing or spreading one; a lethal and highly infectious one needing intensive quarantine
  lifted: must be lifted when the reason for it ends
  published: each designation or lifting is posted on the 질병관리청 website
  basis: 검역법 제5조; 검역법 시행규칙 제2조
penalties:
  - act: failing to declare, or declaring falsely, under 검역법 제12조의2제1항
    sanction: 과태료 of up to 10 million won
    basis: 검역법 제41조제1항제1호
  - act: not complying with a 제12조의2제3항 measure after declaring
    sanction: 과태료 of up to 5 million won
    basis: 검역법 제41조제2항제2호의2
  - act: refusing, obstructing or evading a document request, or submitting false documents
    sanction: up to 1 year in prison or a fine of up to 10 million won
    basis: 검역법 제12조제3항 and 제39조제1항제2호; the 건강상태 질문서 form itself carries this warning
refraction_notes:
  - note: >
      THE TERM IS 검역관리지역 / 중점검역관리지역, AND 오염지역 IS THE PRE-2020 WORD.
      검역법 제2조제7호: 검역관리지역 is 검역감염병이 유행하거나 유행할 우려가
      있어 국내로 유입될 가능성이 있는 지역으로서 제5조에 따라 지정된 지역.
      제2조제8호: 중점검역관리지역 is 검역관리지역 중 유행하거나 유행할 우려가
      있는 검역감염병이 치명적이고 감염력이 높아 집중적인 검역이 필요한 지역으로서
      제5조에 따라 지정된 지역. 부칙 제2조 deems areas designated under the old rules
      as 오염지역 or 오염인근지역 to be the new designations. So a source, a blog or a
      model that says 오염지역 is using the old vocabulary, and item 009 had done so
      until this re-audit. The KDCA's own current pages say 검역관리지역.
    grade: A
  - note: >
      HOW AN AREA GETS DESIGNATED. 검역법 제5조제1항: 질병관리청장 designates or
      lifts 검역관리지역 and 중점검역관리지역 after deliberation by the
      검역전문위원회; 제5조제2항 sends the criteria and procedure to a 보건복지부령.
      시행규칙 제2조제1항 lists three grounds: a country or region for which the WHO
      has given quarantine-disease information under the IHR; one where a
      quarantine disease is or may be epidemic and could be imported or spread; one
      where a lethal, highly infectious one has occurred or may occur and intensive
      quarantine is needed. 제2조제2항: when the reason ends the 질병관리청장
      must lift it. 제2조제3항: each designation or lifting must be posted on the
      질병관리청 website. The KDCA portal words the process as reflecting 검역감염병의
      국외 발생 동향과 위험도 평가 등. The list itself is not here, and no session
      should answer it from memory: look at the portal's 중점 및 검역관리지역 안내
      page or call 1339.
    grade: A
  - note: >
      THE DUTY HAS TWO TIERS AND A CLOCK. 검역법 제12조의2제1항, quoted: 다음 각
      호의 어느 하나에 해당하는 사람은 해당 검역관리지역 또는 중점검역관리지역을
      출발한 후 제17조제3항에 따른 검역감염병의 최대 잠복기간이 경과하지 아니한
      경우 그 사실을 보건복지부령으로 정하는 바에 따라 검역소장에게 건강 상태 등을
      신고하여야 한다. 1호: 검역관리지역에 체류하거나 그 지역을 경유하여 국내에
      입국하는 사람 중 검역감염병을 의심할 수 있는 증상이 있는 사람. 2호:
      중점검역관리지역에 체류하거나 그 지역을 경유하여 국내에 입국하는 사람. So
      from a 중점검역관리지역 everyone who stayed or transited declares; from a
      검역관리지역 only someone with symptoms suggesting a quarantine disease does.
      The clock is the maximum incubation period counted from leaving the area. 제2항
      puts 해외감염병신고센터 at airport, port and land-border arrival (and
      departure) halls (시행규칙 제6조의3).
    grade: A
  - note: >
      THE MAXIMUM INCUBATION TABLE, AND A LIVE CHANGE IN IT. 시행규칙 제14조의3,
      as amended by 보건복지부령 제1195호 (공포 2026-08-31, 시행 2026-10-01):
      콜레라 5일, 페스트 7일, 황열 6일, SARS 10일, 동물인플루엔자 인체감염증 10일,
      MERS 14일, 에볼라바이러스병 21일; 신종인플루엔자 and the notified 자목
      diseases take whatever the 검역전문위원회 sets. The plague figure was 6 until
      2026-09-30: the amendment's own 개정이유 says it was moved from 6 to 7 days
      to unify the plague management standard. Any summary written before
      2026-10-01 has the old number. This is the same kind of trap as the passport
      penalty in item 008, and the rule is the same: state the figure with its date.
    grade: A
  - note: >
      THE CONSUMER PAGE IS LOOSER THAN THE LAW, AND THE STATUTE IS WHAT TO SPEAK.
      The 질병관리청 해외감염병예방수칙 page says: 검역관리지역을 방문 또는 경유한
      경우, 입국 할 때 검역관에게 Q-CODE(또는 건강상태질문서)를 제출해야 합니다.
      발열, 기침, 발진 등 감염병 증상이 있는 경우, 검역관에게 상담받으시기
      바랍니다. That reads as if every traveller from a 검역관리지역 submits. The
      statute, and the KDCA portal's own 제도 소개 page (대상: 중점검역관리지역
      입국자, 발열 등 증상이 있는 검역관리지역 입국자), carry the symptom condition
      for that tier. Speak the statutory version and say the consumer page words it
      more broadly; a traveller who is unsure whether they are covered should ask
      the 해외감염병신고센터 or the 검역관 on arrival, or call 1339. This is a
      reading of two official texts against each other, not a ruling.
    grade: B
  - note: >
      WHAT THE DECLARATION IS. 시행규칙 제6조의2제1항: the declaration is a
      검역관리지역등 체류ㆍ경유 신고서 (별지 제4호의2서식) to the 검역소장; 제2항
      treats a 건강상태 질문서 (별지 제7호서식) submitted for aircraft or ship
      quarantine inspection as having filed it. The string Q-CODE occurs in neither
      the statute nor the rule; it is the KDCA's electronic route named on its
      consumer pages as Q-CODE(또는 건강상태질문서). That the Q-CODE entry stands in
      for the form is read from those pages, not stated in the legal text.
    grade: B
  - note: >
      WHAT FOLLOWS A DECLARATION, AND WHAT FAILING COSTS. 검역법 제12조의2제3항
      lets the 검역소장, where spread is a concern, ask the declarant for
      information on the travel area and timing, on health status, and for
      vaccination proof, and carry out tests or examinations; 시행규칙
      제6조의3제4항 adds a request for information on people, animals and plants
      met in the area. 제41조제1항제1호: failing to declare or declaring falsely is
      a 과태료 of up to 1천만원; 제41조제2항제2호의2: not complying with a 제3항
      measure, up to 5백만원. Separately the 건강상태 질문서 form states: 작성을
      기피하거나 거짓으로 작성하여 제출하는 경우 「검역법」 제12조 및 제39조에 따라
      1년 이하의 징역 또는 1천만원 이하의 벌금에 처해질 수 있습니다.
    grade: A
  - note: >
      NOT COVERED. Which countries and regions are designated today, at either
      tier, and for which disease: that list is the KDCA's and moves with events.
      The compulsory isolation and contact-monitoring provisions (제16조, 제17조)
      beyond the pointer above, which are medical-legal and belong to the 검역소.
      The list of diseases notified under 제2조제1호자목. Pet, plant and goods
      quarantine. Whether a specific traveller is covered, which is for the
      검역소장. No source was found for any travel-insurance consequence of a
      designation, which stays out of scope as in item 008.
    grade: D
claim: >
  Korea's quarantine law designates two kinds of area, 검역관리지역 and the
  stricter 중점검역관리지역, which replaced the pre-2020 오염지역 and
  오염인근지역. The 질병관리청장 designates and lifts them after deliberation by
  the 검역전문위원회 (검역법 제5조) on the grounds in 시행규칙 제2조: WHO IHR
  information on a quarantine disease, a risk of importing or spreading one, or a
  lethal and highly infectious one needing intensive quarantine; a designation
  must be lifted when its reason ends, and each change is posted on the
  질병관리청 website. The traveller's duty is 검역법 제12조의2제1항: anyone who
  stayed in or transited a 중점검역관리지역 and entered Korea, and anyone who did
  so from a 검역관리지역 and has symptoms suggesting a quarantine disease, must
  declare their health status to the 검역소장 until the disease's maximum
  incubation period since leaving the area has elapsed. Those periods are in 시행규칙
  제14조의3: 콜레라 5, 페스트 7 (it was 6 until 보건복지부령 제1195호 took effect
  on 2026-10-01), 황열 6, SARS 10, 동물인플루엔자 인체감염증 10, MERS 14,
  에볼라바이러스병 21 days; 신종인플루엔자 and the notified diseases take the
  period the 검역전문위원회 sets. Failing to declare or declaring falsely is a
  과태료 of up to 1천만원 (제41조제1항제1호); not complying with a follow-up
  measure, up to 5백만원; refusing the document request or submitting false
  documents is punishable by up to 1 year or a fine of up to 1천만원 (제12조제3항,
  제39조제1항제2호), a warning printed on the 건강상태 질문서 itself. The KDCA's
  consumer page tells every traveller who visited or transited a 검역관리지역 to
  submit a Q-CODE or questionnaire, which is broader than the statute; the KDCA
  portal's own system page matches the statute. This item carries the rule and
  the clocks, never the list of designated areas.
reasoning: >
  This item exists because item 009 stated the Q-CODE duty as if it applied to
  every returning traveller and used a term the law dropped in 2020, and because
  the GAPS list had asked for the designation mechanism rather than the list.
  Both are fixed from the primary text: the statute and its enforcement rule
  were read in full from the national legal service's machine-readable records,
  so confidence about what they say is at the top band with a jurisdictional
  qualifier, the same treatment item 008 gives the Passport Act. Three things are
  worth keeping in view. First, the duty is conditional twice over: on the tier
  (everyone from the stricter one, only the symptomatic from the other) and on a
  clock (the maximum incubation period since leaving), so a session that says
  "you must submit a Q-CODE when you come home" is wrong in both directions, too
  broad for most trips and silent about the window. Second, the consumer page and
  the statute disagree in wording, and this warehouse's rule in that case is to
  speak the statute, say that the page is broader, and route doubt to the people
  who decide at arrival; the item grades that reading below the statute because
  it is a comparison of two official texts. Third, the table of maximum
  incubation periods changed on 2026-10-01 (five days before this item was
  written on 2026-10-06), with the plague figure moving from 6 to 7 days, so it
  is a staleness gate in the family of item 008 and the finance tax-regime row:
  carry the figure with its date, not from memory. What the item refuses to carry is the list of designated areas and
  any claim about a particular traveller. The list moves with events and is the
  KDCA's to publish; whether a given person is covered is for the 검역소장. The
  Q-CODE equivalence is recorded as read from the KDCA's pages, not from the
  legal text, because the legal text never uses the word.
---

# travel/kr-quarantine-area-declaration-duty-070 -- 어느 나라에서 왔을 때 입국 신고를 해야 하나

**한 줄 그림:** 입국 신고 의무는 "검역관리지역에 다녀왔다"로 끝나지 않는다. 지역 등급, 증상 유무,
떠난 뒤 며칠이 지났는지 세 가지가 함께 정한다.

## What the engine reads from this row

| Input | What it decides | Where it comes from |
|---|---|---|
| area tier at the time of the trip (read live from the KDCA, never carried here) | 중점검역관리지역: declare regardless of symptoms. 검역관리지역: declare only with symptoms suggesting a quarantine disease | statute 제12조의2 |
| days since leaving the area | duty runs until the disease's maximum incubation period has elapsed | statute 제12조의2 + rule 제14조의3 table |
| the disease the area is designated for (live) | picks the number of days from the table; 신종인플루엔자 and notified diseases have no number here | rule 제14조의3 |
| symptoms the user reports | the only trigger for the 검역관리지역 tier | statute 제12조의2제1항제1호 |
| consequence | 과태료 up to 1천만원 for not declaring or declaring falsely; criminal warning on the 건강상태 질문서 for refusing or falsifying it | statute 제41조, 제39조 |

A trip-return reminder should hold the area tier as a live lookup and the table as data, and
should say the plague figure with its effective date (2026-10-01, was 6 days).

## What this is

Korea's quarantine law has two designated-area tiers. 검역관리지역 is an area where a
quarantine disease is epidemic or may become so and could reach Korea. 중점검역관리지역 is
one of those where the disease is lethal and highly infectious and intensive quarantine is
needed. Before 2020 the words were 오염지역 and 오염인근지역. If a source still says
오염지역, it is using the old vocabulary.

The 질병관리청장 designates and lifts them after the 검역전문위원회 has deliberated. The
enforcement rule gives three grounds: WHO information under the International Health
Regulations, a risk of importing or spreading a quarantine disease, or a lethal and highly
infectious disease needing intensive quarantine. A designation has to be lifted when its
reason ends, and each change is posted on the KDCA's website.

## The duty

Someone who stayed in, or passed through, a 중점검역관리지역 and then entered Korea has to
declare their health status to the quarantine officer. Someone who did the same from a
검역관리지역 has to declare only if they have symptoms that suggest a quarantine disease.
The duty runs from leaving the area until the disease's maximum incubation period has
passed:

| Disease | Days |
|---|---|
| 콜레라 | 5 |
| 페스트 | 7 (was 6 until 2026-10-01) |
| 황열 | 6 |
| SARS | 10 |
| 동물인플루엔자 인체감염증 | 10 |
| MERS | 14 |
| 에볼라바이러스병 | 21 |
| 신종인플루엔자 and notified diseases | set by the 검역전문위원회 |

The plague number is the live example. The enforcement rule was amended on 2026-08-31 and
took effect on 2026-10-01; its stated reason for that line is to unify the plague management
standard by moving the period from 6 to 7 days. Anything written earlier has the old number.

## Where the pages and the law differ

The KDCA's consumer page says that anyone who visited or transited a 검역관리지역 should
hand a quarantine officer a Q-CODE or a 건강상태질문서, and that anyone with fever, cough or
rash should talk to the officer. The statute, and the KDCA's own system page, put the symptom
condition on the 검역관리지역 tier. Speak the statute, say that the consumer page words it
more broadly, and send anyone unsure to the 해외감염병신고센터, the officer on arrival, or 1339.

The declaration itself is a form: the 체류ㆍ경유 신고서, or a 건강상태 질문서 submitted
for the flight's quarantine inspection, which counts as having filed it. The word Q-CODE does
not appear in the statute or the rule. It is the KDCA's electronic route, and the pages
present it as interchangeable with the questionnaire.

## What failing costs

Not declaring, or declaring falsely, is a 과태료 of up to ten million won. Not following a
follow-up measure after declaring (information requests, tests, proof of vaccination, and
the people, animals and plants met in the area) is up to five million. Refusing the document
request or submitting a false one can be punished by up to a year in prison or a ten million
won fine, and the 건강상태 질문서 says so on its face.

## What this entry does not hold

Which countries are designated today, at which tier and for which disease. That list is the
KDCA's, it moves with events, and no session should recite it from memory. Look at the
portal's 중점 및 검역관리지역 안내 page or call 1339. It also does not decide whether a
particular traveller is covered; that is for the quarantine officer.

## 한국어 요약 (답변용)

- 지금 쓰는 말은 검역관리지역과 중점검역관리지역이다. 오염지역은 2020년 이전 용어다.
- 중점검역관리지역에 머물렀거나 거쳐서 입국했다면 증상이 없어도 검역소장에게 건강 상태를
  신고해야 한다. 검역관리지역에서 왔다면 감염병이 의심되는 증상이 있을 때 신고한다. 질병관리청
  해외감염병예방수칙 페이지는 "방문 또는 경유하면 제출"로 더 넓게 적어 두었으니, 헷갈리면
  신고센터나 검역관, 1339에 물어본다.
- 신고 의무는 그 지역을 떠난 날부터 해당 감염병의 최대 잠복기간이 끝날 때까지다. 콜레라 5일,
  페스트 7일, 황열 6일, 사스 10일, 동물인플루엔자 인체감염증 10일, 메르스 14일, 에볼라 21일.
  페스트는 2026-10-01부터 6일에서 7일로 바뀌었다.
- 지금 어느 나라가 지정돼 있는지는 여기 없다. 질병관리청 검역 포털의 "중점 및 검역관리지역
  안내"에서 확인한다.
- 신고를 안 하거나 거짓으로 하면 1천만원 이하 과태료다. 건강상태 질문서를 기피하거나 거짓으로
  쓰면 1년 이하 징역 또는 1천만원 이하 벌금에 처해질 수 있다고 질문서에 적혀 있다.
- Q-CODE는 법 조문에 나오는 말이 아니라 질병관리청의 전자 신고 경로 이름이다. 법에는 신고서와
  건강상태 질문서로 적혀 있다.
