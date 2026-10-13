---
# Collection sprint 2026-09-02, cat-domain opening. KR-LOCALE item, and the only
# item in the @vet-regulatory lane. The mandated jurisdiction check for this
# sprint. The result is genuinely Korean rather than an import, and it is a
# distinction that no English-language source would ever surface: in Korean law
# dogs and cats are NOT in the same registration category, and an assistant that
# assumes "pet registration" applies to a cat would be wrong about a statutory
# obligation. Two adjacent questions were checked and came back unresolved; they
# are recorded rather than guessed.
# Rubric: cat @vet-regulatory (VC-F).
# Source re-audit 2026-10-06: easylaw page re-read -- 등록대상동물 still dogs only
# (제2조 제8호, 시행령 제4조), fines at 제101조 unchanged; no source found moving
# cats into the mandatory class. Staleness date moved; nothing else changed.
id: cat/kr-registration-gate-013
domain: cat
grade: A (jurisdictional-legal, read from the statute and the government portals); D (anything about vaccination obligation for cats in Korea, and anything about the current count of participating local governments)
lane: "@vet-regulatory"
locale: KR
as_of: 2022-2026
contested: no
sources:
  - "https://easylaw.go.kr/CSP/CnpClsMain.laf?csmSeq=1809&ccfNo=1&cciNo=1&cnpClsNo=2"  # 찾기쉬운 생활법령정보 (Ministry of Government Legislation, official). Cites 동물보호법 제2조 제8호 and 동물보호법 시행령 제4조: 등록대상동물 is a dog aged 2 months or older. Cats are not in the category. Fines: registration failure up to 1,000,000 KRW; late change notification up to 500,000 KRW. Retrieved and read 2026-09-02; re-read 2026-10-06, unchanged (fines cited at 동물보호법 제101조 제3항제4호 and 제4항)
  - "https://www.animal.go.kr/front/community/show.do?boardId=contents&seq=66&menuNo=2000000016"  # 국가동물보호정보시스템 (official national animal protection information system): 등록대상동물 stated as "주택.준주택에서 기르거나 그 외의 장소에서 반려 목적으로 기르는 월령 2개월 이상인 개". Dogs only. Retrieved 2026-09-02
  - "https://korea.kr/news/visualNewsView.do?newsId=148898741"  # 대한민국 정책브리핑 (korea.kr, official government policy portal), published 2022-02-08: the cat registration pilot went nationwide on 2022-02-01, by 내장형 (implanted microchip) method. Retrieved 2026-09-02
  - "https://www.qia.go.kr/animal/prevent/ani_rabies_prev.jsp"  # 농림축산검역본부 rabies prevention page. Read 2026-09-02 for a legal obligation on cat vaccination; the page describes a vaccination protocol and states no obligation. See the refusal note
  - "cat/curator-checklist-001"  # domain rule: a jurisdictional legal fact read off the statute is the domain's most certain band, because it is verified by reading rather than by trial
refraction_notes:
  - note: >
      DOGS AND CATS ARE NOT THE SAME CATEGORY IN KOREAN LAW, and this is the whole
      item. 등록대상동물 -- the class of animal that MUST be registered -- is
      defined under 동물보호법 제2조 제8호 and 동물보호법 시행령 제4조 as a dog
      aged two months or older, kept in a dwelling or quasi-dwelling or kept for
      companionship elsewhere. Cats are not in that class. An assistant that
      treats "반려동물 등록" as a single obligation covering both species is
      wrong about a statutory duty, and would generate a non-existent deadline
      for a cat household.
    grade: A
  - note: >
      THE CAT PILOT IS VOLUNTARY, NATIONWIDE, AND MICROCHIP-ONLY. The government
      policy portal published on 2022-02-08 that the cat registration pilot ran
      nationwide from 2022-02-01, and that registration is by 내장형 -- an
      implanted microchip. Dog registration allows a choice of 내장형 or 외장형
      (an external tag); the cat pilot does not. So a cat owner who wants to
      register faces a different and narrower procedure than a dog owner, and it
      involves an implant.
    grade: A
  - note: >
      THE PENALTIES ATTACH TO THE DOG OBLIGATION, NOT TO THE CAT PILOT. The
      Ministry of Government Legislation portal states a fine of up to 1,000,000
      KRW for failing to register a 등록대상동물 and up to 500,000 KRW for late
      notification of a change. Since a cat is not a 등록대상동물, there is no
      corresponding penalty for not registering a cat. An agent must not warn a
      cat household about a fine.
    grade: A
  - note: >
      NOT ESTABLISHED, AND SEARCHED FOR: whether rabies vaccination is legally
      required for cats in Korea. The 농림축산검역본부 rabies prevention page was
      read for this in this sprint. It describes a vaccination protocol for cats
      including annual boosters, and it does not state an obligation; the word
      의무 does not appear in relation to cats there. Whether a local ordinance or
      a 가축전염병예방법 vaccination order can bring cats in was NOT resolved from
      the sources read. An agent must not tell a Korean cat household that rabies
      vaccination is legally mandatory, and must not tell it that it is not. This
      needs its own legal source.
    grade: D
  - note: >
      NOT SHIPPED: the current number of participating local governments. Figures
      circulate for how many 시.군.구 take part in the cat pilot. The only
      government source read here is the 2022 nationwide-expansion announcement,
      and the participation count appeared only in pet media. Consistent with the
      warehouse's treatment of figures that exist only in retellings, the
      nationwide status is carried and the count is not.
    grade: D
  - note: >
      STALENESS. This is a jurisdictional fact with a live legislative surface --
      the cat pilot has been described as a pilot since 2018 and expanded since,
      and the obvious future move is bringing cats into the mandatory category.
      Treat this row as verified AS OF the 2026-10-06 re-read and re-check before
      relying on it for a deadline or an obligation. Same discipline as
      finance-investing/kr-tax-regime-staleness-gate-016.
    grade: A
claim: >
  In Korean law dogs and cats are NOT in the same pet-registration category, and
  an assistant that assumes otherwise will assert a statutory duty that does not
  exist. 등록대상동물 -- the class that must be registered -- is defined under
  동물보호법 제2조 제8호 and 동물보호법 시행령 제4조 as a DOG aged two months or
  older kept in a dwelling or quasi-dwelling or kept for companionship elsewhere.
  Cats are not in that class, so there is no registration obligation for a cat and
  no corresponding penalty; the fines that circulate (up to 1,000,000 KRW for
  failure to register, up to 500,000 KRW for late change notification) attach to
  the dog obligation. Cat registration exists as a VOLUNTARY pilot which the
  government policy portal announced as going nationwide on 2022-02-01, and it is
  available only by 내장형 -- an implanted microchip -- whereas dog registration
  allows either an implant or an external tag. TWO ADJACENT QUESTIONS CAME BACK
  UNRESOLVED and are not asserted in either direction: whether rabies vaccination
  is legally required for cats in Korea (the 농림축산검역본부 rabies page describes
  a protocol and states no obligation; whether a local ordinance or a
  가축전염병예방법 order can bring cats in was not resolved), and the current count
  of participating local governments (present only in pet media, not in a
  government source). Verified as of 2026-09-02; re-check before relying on it.
reasoning: >
  The sprint instruction was to check the Korean case wherever guidance might be
  jurisdiction-specific, and this is the one that mattered, because the error it
  prevents is a confident assertion rather than a vague one. An assistant reading
  English-language material about pet registration, or reading Korean material
  about 반려동물 등록 without noticing the statutory definition, will conclude
  that a cat must be registered within a deadline or a fine follows. The statute
  says the registrable class is dogs. That is not a nuance; it is the difference
  between a real obligation and an invented one, and the invented version comes
  with a million-won number attached. Graded at the top band because a legal fact
  read off the statute and confirmed on two government portals is verified by
  reading rather than by inference -- which is exactly why the domain checklist
  puts jurisdictional facts above clinical ones here, in a domain where the
  clinical evidence is thin. The microchip-only detail is carried because it is a
  real asymmetry with a practical consequence: a cat owner choosing to register is
  consenting to an implant, where a dog owner can choose a tag. Two refusals are
  recorded inside the item rather than only in the gap file, on the same reasoning
  the relationships lane used: a refusal that lives only in a gap file is not
  present at the moment it is needed. The vaccination question is the more
  dangerous of the two, because it is the next thing anyone asks after
  registration and because getting it wrong in either direction has consequences
  -- so the item states plainly that neither answer is available. And the staleness
  gate is set because the cat pilot has been a pilot since 2018 and the obvious
  legislative direction is to end it, which would invert this row's headline.
---

# cat/kr-registration-gate-013

In Korean law, dogs and cats are not the same thing for registration purposes,
and getting that wrong produces a confident statement about an obligation that
does not exist.

The class of animal that must be registered -- 등록대상동물 -- is defined in the
Animal Protection Act and its enforcement decree as a dog aged two months or
older, kept in a home or kept for companionship elsewhere. A cat is not in that
class. There is no registration deadline for a cat and no penalty for not
registering one. The fines that circulate alongside this subject -- up to a
million won for failing to register, up to half a million for a late change
notification -- attach to the dog obligation.

Cat registration does exist, as a voluntary pilot. The government policy portal
announced it going nationwide from the first of February 2022. One detail is
worth carrying because it is a real asymmetry: cat registration is available only
by implanted microchip, whereas a dog owner can choose between an implant and an
external tag. A cat owner who decides to register is agreeing to an implant.

Two neighbouring questions were checked in this pass and neither could be
answered, so neither is answered here.

Whether rabies vaccination is legally required for cats in Korea is the obvious
next question and the answer was not obtainable. The quarantine agency's rabies
page sets out a vaccination protocol for cats, including annual boosters, and
states no obligation; whether a local ordinance or a livestock-disease
vaccination order can bring cats in was not resolved from what was read. It
should not be stated as mandatory and it should not be stated as optional.

And the number of local governments currently participating in the cat pilot
appears in pet media but not in any government source that was read, so the
nationwide status is carried and the count is not.

Finally, this is a fact with a live legislative surface. The cat pilot has been a
pilot since 2018 and has been expanded more than once, and the obvious direction
of travel is to fold cats into the mandatory category -- which would reverse the
headline of this row. It is verified as of the second of September 2026 and
should be re-checked before anyone relies on it for a deadline.
