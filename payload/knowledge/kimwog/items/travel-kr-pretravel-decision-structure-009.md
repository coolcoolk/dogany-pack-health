---
# Authored 2026-09-02 (travel-lane opening sprint). KR-LOCALE item,
# @travel-advisory (VC-F). Vaccination and prophylaxis as a DECISION STRUCTURE,
# which is the only form in which a warehouse for an assistant may carry them.
# Everything here is lead time, route and who decides. There is no schedule, no
# drug selection and no dose in this item, and that boundary is the item's
# design rather than an omission. Sourced entirely to Korea's own disease-control
# authority, because a US recommendation is not a Korean one -- the mistake this
# warehouse's cooking lane was corrected for earlier the same day.
id: travel/kr-pretravel-decision-structure-009
domain: travel
lane: "@travel-advisory"
grade: A (jurisdictional-guidance)
locale: KR
as_of: 2026-09-02
contested: no
sources:
  - "https://www.kdca.go.kr/kdca/4915/subview.do"  # 질병관리청 (Korea Disease Control and Prevention Agency), 해외감염병예방수칙 consumer page. Retrieved and read 2026-09-02; the 2-week minimum, the 해외감염병NOW / 1339 route and the Q-CODE entry requirement are quoted from it
  - "https://www.kdca.go.kr/kdca/4916/subview.do"  # 질병관리청, 해외여행전 consumer page. Retrieved and read 2026-09-02; the 2-month preparation lead time, the yellow fever and Japanese encephalitis lead times, and the prescription-gated status of malaria prophylaxis are quoted from it
  - "https://nqs.kdca.go.kr/nqs/vaccination.do?gubun=yellowFever&subGubun=2"  # 질병관리청 국립검역소 (National Quarantine Stations), 황열 예방접종 page. Retrieved and read 2026-09-02; the 10-day minimum, the exemption certificate and the designated-facility restriction are quoted from it
  - "source:travel/td-severity-decision-structure-007 -- the international expert-panel guideline this item deliberately does NOT substitute for Korean guidance"
  - "source:travel/kr-travel-ban-legal-gate-008 -- the other Korean gate, and the reason a session should check a current designation rather than recall one"
  - "framework:jurisdictional-guidance -- these are consumer-facing instructions published by the Korean disease-control authority on its own portals. They are definitive about what Korea instructs its travellers to do. They are NOT a clinical schedule, they are not binding, and they are not a substitute for a travel clinic's assessment of an individual."
applicability:
  axes:
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: medication_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: allergen_list
      type: categorical
      role: hard
      unknown_policy: block_specifics
refraction_notes:
  - note: >
      LEAD TIME IS THE WHOLE DECISION, AND THERE ARE THREE DIFFERENT ONES. The
      authority's 해외여행전 page says 예방접종이 필요한 경우 최소 2개월 전부터
      준비해야 합니다 -- two months to PREPARE. Its 해외감염병예방수칙 page says
      해외여행 국가별 예방접종이 필요한 백신은 출국 최소 2주 전에 접종해야 합니다 --
      two weeks minimum to ADMINISTER. The 국립검역소 yellow fever page says
      예방접종은 최소 출국 10일 전에 접종하여야 -- ten days for that specific
      vaccine. These are not in conflict; they answer different questions, and a
      session that collapses them into a single number will give bad advice in
      one direction or the other. The operationally useful one is the first: this
      is a two-month-out decision, and by the time someone has booked flights for
      next week the menu has already shrunk.
    grade: A
  - note: >
      YELLOW FEVER IS THE ONE WITH A HARD ADMINISTRATIVE GATE. The authority
      states that vaccination must be given at least ten days before departure, and
      that where a person medically cannot be vaccinated they must obtain a
      황열예방접종면제증명서 -- an exemption certificate -- BEFORE leaving. Vaccination
      is available at 국립검역소 and at 국제공인예방접종 지정 의료기관, not at any
      clinic. The page also records that since 2016-07-11 immunity is treated as
      lifelong. The structural point for an assistant: this is a documentation
      problem as much as a medical one, and the document has to exist before
      departure, not after.
    grade: A
  - note: >
      MALARIA PROPHYLAXIS IS PRESCRIPTION-GATED AND THE PAGE SAYS SO. The
      authority describes it as 전문 의약품으로 반드시 의사의 처방을 받아 최소 일주일
      전부터 복용해야 하며, with a stated start of 여행 출발 1~2주 전. That is the
      complete content this warehouse carries. WHICH agent, for WHICH destination,
      at WHAT dose, for how long after return -- none of that is here, and none of
      it should be generated. Regional resistance patterns make agent selection a
      genuinely destination-specific clinical decision, and the authority itself
      routes it to a doctor.
    grade: A
  - note: >
      THE ROUTE, WHICH IS THE MOST REUSABLE PART. Before travelling: 해외감염병NOW,
      or the authority's call centre on 1339, for country-by-country outbreak
      information. On entry back into Korea: 입국 할 때 검역관에게 Q-CODE (또는
      건강상태질문서)를 제출해야 합니다. If symptoms appear after returning: 1339,
      which the page says will connect the caller to a 보건소 and give 행동요령. A
      session that remembers nothing else from this item should remember that
      there is one number and one portal.
    grade: A
  - note: >
      A US RECOMMENDATION IS NOT A KOREAN ONE, AND THIS IS WHERE THE TEMPTATION IS
      STRONGEST. English-language travel-health material is abundant, well written
      and mostly American, and it differs from Korean guidance in ways that matter:
      which facilities may issue an international certificate, which products are
      available and prescription-gated in Korea, and where the traveller is meant
      to go. This warehouse dropped a US-only cooking rule earlier on 2026-09-02
      for exactly this substitution. Nothing in this item comes from a non-Korean
      source, deliberately.
    grade: A
  - note: >
      NOT COVERED, AND SOME OF IT IS ABSENT ON PURPOSE. No vaccine schedule, no
      destination-to-vaccine mapping, no age or pregnancy variation, no cost or
      coverage detail beyond what the pages state, no 검역감염병 오염지역 list, and
      nothing about the routine childhood schedule. The designated-area list in
      particular moves and is the authority's to publish; a session must look it
      up rather than recall it, exactly as with the travel-ban designations. What
      WOULD be worth adding later is the 오염지역 designation mechanism itself,
      which was not read in this pass.
    grade: D
claim: >
  Korea's disease-control authority publishes a pre-travel structure whose active
  ingredient is lead time. Its 해외여행전 page states 예방접종이 필요한 경우 최소
  2개월 전부터 준비해야 합니다. Its 해외감염병예방수칙 page states 해외여행 국가별
  예방접종이 필요한 백신은 출국 최소 2주 전에 접종해야 합니다. For yellow fever
  specifically, the National Quarantine Stations state 예방접종은 최소 출국 10일
  전에 접종하여야, that vaccination is available at 국립검역소 and at 국제공인예방접종
  지정 의료기관, that a person who medically cannot be vaccinated must obtain a
  황열예방접종면제증명서 before departure, and that since 2016-07-11 immunity is
  treated as lifelong. Japanese encephalitis vaccination is stated as needing to be
  completed 여행 10일 전. Malaria prophylaxis is described as 전문 의약품으로 반드시
  의사의 처방을 받아 최소 일주일 전부터 복용해야, with a stated start of 여행 출발
  1~2주 전 -- that is, it is prescription-gated and the decision belongs to a
  doctor. The route is: 해외감염병NOW or the 1339 call centre for country-by-country
  information before departure; submission of a Q-CODE or 건강상태질문서 to a
  quarantine officer on entry; and 1339 again if symptoms appear after returning,
  which connects the caller to a 보건소. This item carries lead times, routes and
  who-decides. It carries no schedule, no product selection and no dose.
reasoning: >
  Vaccination and prophylaxis are exactly where a helpful assistant becomes a
  dangerous one, so this item is built around the question of what CAN be said
  rather than what is known. What can be said turns out to be substantial and
  genuinely useful: the whole thing is a lead-time problem, and lead time is
  information a life agent is uniquely well placed to act on, because it knows when
  the trip is. Two months out, everything is available. Two weeks out, most things
  still are. Three days out, the answer to several questions is simply no, and
  saying that early is worth more than any amount of detail said late. Confidence
  sits at the top band with a jurisdictional qualifier because these are the
  Korean authority's own instructions read from its own portals, and an authority
  is definitive about what it instructs -- the same basis on which the cooking lane
  carries Korea's core-temperature table. Confidence about whether each instruction
  is the clinically optimal one is a different and weaker question this item does
  not attempt. Three deliberate boundaries. The three lead-time figures are kept
  separate rather than reconciled, because they answer different questions --
  prepare, administer, and one specific vaccine -- and collapsing them is the
  obvious way to get this wrong. Malaria prophylaxis is recorded as
  prescription-gated and stops there, because agent selection turns on regional
  resistance and is a clinical decision the authority itself routes to a doctor.
  And every source is Korean, which is not a stylistic preference: English-language
  travel-health material is overwhelmingly American, it differs on facility
  designation and product availability, and this warehouse dropped a US-only rule
  from another lane earlier the same day for exactly that substitution. The
  strongest single takeaway is not any figure but the yellow fever structure, which
  shows the shape of the whole domain -- a ten-day biological minimum wrapped in an
  administrative requirement about a certificate that has to exist before someone
  gets on a plane.
---

# travel/kr-pretravel-decision-structure-009

Everything about pre-travel vaccination is a question about lead time, and the
Korean authority answers it three different ways for three different questions.

- **최소 2개월 전부터 준비해야 합니다** -- two months to *prepare*, if vaccination is
  needed at all.
- **출국 최소 2주 전에 접종해야 합니다** -- two weeks as the minimum before departure
  to actually *receive* a country-specific vaccine.
- **최소 출국 10일 전** -- ten days, for yellow fever specifically. Japanese
  encephalitis is stated as needing to be completed 여행 10일 전.

Those are not competing numbers and they should not be averaged. The first is a
planning horizon, the second an administration floor, the third a per-vaccine
rule. The one a life agent can act on is the first, because it is the only one
that is still actionable when it is heard.

Yellow fever is worth looking at closely, because it shows the shape of the whole
domain. Ten days before departure is the biological part. Everything else is
paperwork: the vaccination is only given at 국립검역소 or at 국제공인예방접종 지정
의료기관, not at a neighbourhood clinic; and someone who medically cannot be
vaccinated has to obtain a 황열예방접종면제증명서 *before* leaving. The authority
also records that since 11 July 2016 the immunity is treated as lifelong. So the
question "am I vaccinated" and the question "do I have the document" are different
questions, and only one of them can be fixed at the airport, which is neither.

Malaria prophylaxis gets one sentence here, on purpose. The authority describes it
as 전문 의약품 requiring a doctor's prescription, to be started at least a week and
typically one to two weeks before departure. Which drug, for which destination, at
what dose, and for how long after coming home are questions that turn on regional
resistance patterns and belong to a clinician. This warehouse carries the fact that
the decision is prescription-gated. It does not carry the decision.

The route is the part worth memorising, because it does not change:

- Before going: **해외감염병NOW**, or the authority's call centre on **1339**, for
  country-by-country outbreak information.
- Coming back: a **Q-CODE** or **건강상태질문서** submitted to a quarantine officer on
  entry.
- Symptoms after returning: **1339** again, which connects the caller to a 보건소
  and gives 행동요령.

One thing this entry will not do, and the reason is written into how it was built.
Every source here is Korean. Travel-health material in English is plentiful,
well-organised and almost entirely American, and it differs from Korean guidance
on things that matter -- which facilities can issue an international certificate,
what is available and prescription-only in Korea, and where a traveller is
actually meant to go. A recommendation from another country's health agency is
that country's recommendation. This warehouse has already had one foreign rule
pulled out of a different lane for being passed off as a Korean one.
