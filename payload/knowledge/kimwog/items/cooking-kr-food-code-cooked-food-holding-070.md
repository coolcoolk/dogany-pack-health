---
# Authored 2026-10-06 (cooking craft/holding re-audit sprint). KR-LOCALE item, @food-safety.
# Filed because the lane's holding fence (014) rested on ministry ADVICE
# pages, and on 2026-10-01 -- five days before this pass -- an amendment to the
# Food Code itself came into force that writes a holding rule and a 2-hour
# serving rule into the legal standard for restaurants and mass catering. The
# legal text was read from the ministry's own notice attachment, not from the
# trade press that first surfaced it.
# Scope fence stated up front: this is a BUSINESS standard (식품접객업소,
# 집단급식소). It binds no household. It is filed because its numbers are the
# legal floor the household advice in 014 sits beside, and because one of
# them (10C) differs from that advice (5C).
id: cooking/kr-food-code-cooked-food-holding-070
domain: cooking
lane: "@food-safety"
grade: A (jurisdictional-standard)
locale: KR
as_of: 2026-10-01
contested: no
sources:
  - "https://www.mfds.go.kr/brd/m_207/view.do?seq=15182"  # 식품의약품안전처 고시 제2026-55호, 식품의 기준 및 규격 일부개정고시, 2026-07-31, 시행 2026-10-01. The attached 개정고시 .hwpx was downloaded and its 신구조문 text for 제6. 4. 조리 및 관리 기준 read directly 2026-10-06; quotations below are from that text
  - "https://www.mfds.go.kr/brd/m_207/down.do?brd_id=data0008&seq=15182&data_tp=A&file_seq=5"  # same notice, attachment 식품접객업소 집단급식소 조리식품 등의 기준 개정 관련 Q&A (식품기준과, 2026-07-31, PDF), read in full 2026-10-06. Source for the scope definition of 조리식품, the statement that the thawing list is illustrative not mandatory (A4), and the effective date (A15)
  - "https://www.fsnews.co.kr/news/articleView.html?idxno=61845"  # 대한급식신문 trade report of the same amendment. Cited ONLY as the lead that surfaced the notice; no figure is taken from it
  - "source:cooking/session-holding-fence-014 -- the household-facing ministry advice (60C / 5C / 2시간 섭취) this legal text sits beside"
  - "source:cooking/kr-cold-chain-band-006 -- the general Food Code storage band (0~10C), consistent with this item's 10C cold-holding line"
  - "source:cooking/reheating-not-a-reset-007 -- why a held dish is not reset by bringing it back up to temperature"
holding_rules:
  - rule: hot-hold
    text_kr: 따뜻한 음식은 60℃ 이상에서 보관·운반
    value_c_min: 60
    binding_on: 식품접객업소, 집단급식소
    strength: 가능한 한 (best-effort wording in the legal text)
    clause: 제6. 4. 1) (5)
  - rule: cold-hold
    text_kr: 냉면육수 등 찬 음식은 10℃ 이하에서 보관·운반
    value_c_max: 10
    binding_on: 식품접객업소, 집단급식소
    strength: 가능한 한
    clause: 제6. 4. 1) (5)
    household_advice_differs: "ministry consumer advice is 5℃ 이하 (items 005, 014); speak 5C to a household"
  - rule: untempered-serving-window
    text_kr: 조리한 식품의 온도관리를 하지 아니하는 경우에는 조리 후 가능한 한 2시간 이내에 배식을 마쳐야 한다
    clock_starts: end of cooking
    clock_hours: 2
    applies_when: food is neither hot-held nor cold-held
    binding_on: 집단급식소 only
    strength: 가능한 한
    clause: 제6. 4. 2) (1)
  - rule: cool-in-clean-place
    text_kr: 가열조리한 식품은 위해미생물에 의하여 오염되지 않도록 청결한 장소에서 식히거나 보관해야 한다
    cooling_rate_specified: false
    clause: 제6. 4. 1) (4)
  - rule: thawing-methods
    text_kr: 냉장온도에서 해동하거나, 21℃ 이하의 흐르는 물로 해동할 수 있으며, 필요한 경우 실온에서 해동하거나 전자레인지 등을 이용하여 급속해동할 수 있다
    running_water_c_max: 21
    mandatory: false
    clause: 제6. 3. 2) 가) (6) ④
refraction_notes:
  - note: >
      THIS IS LAW FOR BUSINESSES, NOT FOR HOUSEHOLDS. 고시 제2026-55호 sets these
      lines inside 제6 (식품접객업소(집단급식소 포함)의 조리식품 등의 기준), and the
      Q&A defines 조리식품 by reference to 식품접객업소 and 집단급식소. A home cook
      is not bound by it. Speak it to a household as "this is what Korea
      requires of restaurants and canteens", never as "the law says you must".
    grade: A
  - note: >
      THE LEGAL COLD LINE IS 10C AND THE HOUSEHOLD ADVICE IS 5C. DO NOT MERGE THEM.
      The Food Code says 찬 음식은 10℃ 이하 for holding and transport; the
      ministry's own consumer pages (items 005 and 014) say 5℃ 이하. Both are
      real, at different scopes. A cooking-session flow speaking to a household
      uses 5C. The 10C line is the business floor and is the warmer of the two,
      which is exactly the gap item 006 already warns about.
    grade: A
  - note: >
      THE 2-HOUR CLOCK IS NOW IN THE LEGAL TEXT, AND IT STARTS AT THE END OF
      COOKING. 조리 후 가능한 한 2시간 이내에 배식을 마쳐야 한다, for food under no
      temperature control, in 집단급식소. That anchors the clock where item 014's
      re-audit put it: at the end of cooking, not at the moment a pot drops below
      60C. It also states the exemption the warehouse had only inferred: the
      clock is for food that is NOT being held hot or cold.
    grade: A
  - note: >
      "가능한 한" IS IN EVERY ONE OF THESE LINES. The holding temperatures and the
      2-hour window are written as best-effort (가능한 한), not as absolute limits.
      That is a statement about enforcement wording, not permission: it does not
      make 3 hours safe, and nothing on this page says what happens at 3 hours.
      Do not soften the 2-hour rule to a household on the strength of that phrase.
    grade: B
  - note: >
      NO COOLING RATE IS SPECIFIED, AND THIS WAS CHECKED. The amended text says
      only that cooked food is cooled or stored in a clean place (청결한 장소에서
      식히거나 보관). There is no time-to-temperature cooling standard of the kind
      some foreign codes carry. The batch-cooling numbers this warehouse carries
      (item 071) are therefore foreign-jurisdiction references and a single
      foodservice study, and must be labelled as such to a Korean user.
    grade: A
  - note: >
      EDITION CHECK DONE FOR THESE CLAUSES ONLY. This pass read the 2026-07-31
      notice text itself, so the clauses quoted here are certified current as of
      2026-10-01. It did NOT re-read the 보존 및 유통기준 annex that item 006
      relies on; that item's edition-check debt is unchanged.
    grade: B
claim: >
  An amendment to Korea's Food Code (식품의 기준 및 규격, 식품의약품안전처 고시
  제2026-55호, published 2026-07-31, in force 2026-10-01) writes cooked-food
  holding into the legal standard for restaurants and mass catering. For
  식품접객업소 including 집단급식소: 가능한 한 조리한 식품 중 냉면육수 등 찬 음식은
  10℃ 이하에서, 따뜻한 음식은 60℃ 이상에서 보관·운반해야 한다, and 가열조리한
  식품은 위해미생물에 의하여 오염되지 않도록 청결한 장소에서 식히거나 보관해야 한다.
  For 집단급식소 specifically: 조리한 식품의 온도관리를 하지 아니하는 경우에는 조리 후
  가능한 한 2시간 이내에 배식을 마쳐야 한다. Frozen food may be thawed 냉장온도에서,
  21℃ 이하의 흐르는 물로, or if needed at room temperature or by microwave; the
  ministry's Q&A states this list is illustrative, not a mandated method. No
  cooling rate (time to reach a temperature) is set anywhere in the amended text.
reasoning: >
  Confidence is about what the Korean legal standard says, and the ministry's
  own notice with the amending text attached is the definitive record of that,
  so the item sits at the top band with a jurisdictional qualifier. It earns its
  place for three reasons a cooking-session flow can use. It moves the 2-hour
  rule from advice to law (for catering) and fixes where the clock starts -- at
  the end of cooking -- which the household-facing pages implied but never said
  in those words. It confirms in legal text that the clock applies to food NOT
  held at temperature, which is the exemption the timeline items assumed. And
  it exposes a scope split the flow must not paper over: the business cold line
  is 10C, the household advice is 5C. Two limits are carried openly. Every line
  is softened by 가능한 한, which is enforcement wording and licenses nothing
  beyond it. And the amended text sets no cooling rate, which was checked rather
  than assumed, so any cooling-time figure spoken to a Korean user comes from
  outside Korean law.
---

# cooking/kr-food-code-cooked-food-holding-070

On 1 October 2026 a change to Korea's Food Code came into force that puts
cooked-food holding into the legal standard for restaurants and canteens. Until
then the warehouse's holding rule came from the ministry's advice pages. Now
the same lines are in the law -- for businesses.

What the amended text says, for restaurants and mass catering alike: as far as
possible, cold cooked food such as 냉면 broth is held and transported at 10
degrees or below, and hot food at 60 or above. Cooked food is cooled or stored
somewhere clean.

What it adds for mass catering (school, workplace, hospital kitchens): if cooked
food is not being kept hot or cold, serving should be finished within two hours
of cooking, as far as possible.

Three things follow for a home cooking session, even though none of this binds
a home cook.

First, the two-hour clock starts when the cooking ends. Not when the pot drops
below 60, which a home cook cannot see. The ministry's consumer pages said
"eat within two hours"; the legal text now says it for catering in so many
words.

Second, the clock is for food that is not being held. A pot kept hot on the
stove is outside it. A pot switched off and left on the stove is inside it.

Third, the cold line in the law is 10 degrees. The ministry's own advice to
households is 5. Those are different scopes, not a contradiction, and a home
session should say 5.

Two honest limits. Every one of these lines carries "as far as possible" (가능한
한) in the legal wording. That is how the rule is enforced, not a licence to
stretch it, and nothing here says what happens at three hours. And the amended
text sets no cooling rate at all -- no "down to this temperature within that
many hours". That was checked. Any cooling-time number a Korean user hears comes
from another country's rules, and the next item says so.
