---
# Relationship-contact sprint 2026-10-06 (dispatch task kw-relationship-contact).
# The CONTENT half of a reach-out: what a remembered detail (an event the
# person mentioned, their news, a birthday) is good for. 013 says the act is
# under-valued; 019 says hand over the last shared occasion as the opener.
# This row adds what the evidence says about the shape of the message itself
# -- a question that follows up on what they told you, and an engaged response
# to their good news -- and records honestly that remembering a BIRTHDAY has
# almost no evidence behind it beyond a reciprocity effect.
#
# message_rules is structured data for the lifekit person module.
id: relationships-communication/remembered-detail-follow-up-071
domain: relationships-communication
grade: B (asking more questions, especially follow-up questions, raises the partner's liking via perceived responsiveness -- randomised, live conversations); C (engaged, enthusiastic responses to a partner's good news go with better relationship well-being and fewer break-ups two months later; a birthday greeting raises the chance of one back); D (that remembering birthdays or dates builds closeness, and the module's message-shape rules)
lane: "@dyadic"
locale: universal
as_of: 2004-2018
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/28447835/"  # Huang K, Yeomans M, Brooks AW, Minson J, Gino F 2017, J Pers Soc Psychol 113(3):430-452, doi 10.1037/pspi0000097 -- READ AT the author manuscript (Harvard DASH) 2026-10-06. Pilot 67 dyads; Study 1 random assignment of one partner to ask many (at least 9) or few questions in a 15-minute online chat, 398 analysed; follow-up questions identified as the active ingredient via perceived responsiveness; speed-dating field data: more follow-up questions, more second-date agreement. Strangers in first conversations, US university samples
  - "https://pubmed.ncbi.nlm.nih.gov/15301629/"  # Gable SL, Reis HT, Impett EA, Asher ER 2004, J Pers Soc Psychol 87(2):228-245, doi 10.1037/0022-3514.87.2.228 -- four studies: telling others about good events was linked with more daily positive affect beyond the event itself; perceived active-constructive responses further enhanced it and went with higher relationship well-being. Diary and correlational; read at the PubMed abstract
  - "https://pubmed.ncbi.nlm.nih.gov/17059309/"  # Gable SL, Gonzaga GC, Strachman A 2006, J Pers Soc Psychol 91(5):904-917, doi 10.1037/0022-3514.91.5.904 -- 79 dating couples, videotaped turns on recent positive and negative events, observer coding; responses to POSITIVE event disclosures predicted relationship well-being and break-up two months later more closely than responses to negative events. Prospective but observational; read at the PubMed abstract
  - "https://perfilesycapacidades.javeriana.edu.co/en/publications/reciprocity-in-a-social-network-evidence-from-a-natural-field-exp/"  # Reyes LC 2018, Econ Bull 38(2):672-680 -- natural field experiment: one Facebook user's friends randomly sent birthday greetings over a year; a greeting raised the probability of a greeting back on the sender's birthday by about 50%, and the effect faded with time (about three times larger when the sender's birthday was one month away than six). One account; outcome is a returned greeting, not closeness; sample size not verified from the record
  - "relationships-communication/reach-out-appreciation-gap-013"  # the act of reaching out is under-valued; this row is about its content
  - "relationships-communication/reconnect-after-gap-craft-019"  # the last shared occasion is the opener; this row gives the evidence for turning it into a question
  - "relationships-communication/communal-no-scorekeeping-072"  # why the birthday reciprocity effect must not become a ledger
  - "relationships-communication/record-absence-not-neglect-018"  # an un-logged birthday message is unknown, not a missed one
  - "framework:GRADE -- question-asking reaches the trial-adjacent band on design: random assignment of question volume in live conversations, a replicated pattern across studies, and a behavioural field indicator (second-date agreement). It is held there and not higher because all partners were strangers in first meetings, samples were US, and liking is self-report. Capitalization is observational (diary, cross-sectional, one prospective couples study of 79). The birthday evidence is a single-account randomised greeting study whose endpoint is reciprocation, so it says nothing about closeness. Searched: birthday remembering and relationship quality, anniversary or date recall and closeness, gift timing -- no primary source located that links remembering a birthday or date to closeness."
message_rules:
  - rule: carry-the-detail-as-a-question
    payload: the remembered detail the person shared (an exam, a move, a sick parent, a project) offered as a follow-up question, not a statement of what the module knows
    basis: Huang et al. 2017
    basis_grade: B
  - rule: good-news-gets-engagement
    payload: when the stored detail is the person's good news, suggest an engaged, curious reply (ask about it, reflect it) rather than a brief acknowledgement
    basis: Gable et al. 2004, 2006
    basis_grade: C
  - rule: birthday-is-an-occasion
    payload: a birthday or anniversary is offered as an easy opener on the day, once; skipping it is not recorded as a miss and never resurfaces
    basis: no closeness evidence located; Reyes 2018 shows only that greetings tend to be returned
    basis_grade: D
  - rule: owner-words-not-template
    payload: the module offers the detail and at most a question stem; it never sends or drafts a finished message on its own initiative (019)
    basis: relationships-communication/reconnect-after-gap-craft-019
    basis_grade: D
refraction_notes:
  - note: >
      FOLLOW-UP QUESTIONS ARE THE ACTIVE INGREDIENT. When one partner in a
      live chat was randomly told to ask more questions, the other partner
      liked them more, and the effect ran through feeling listened to and
      understood. Follow-up questions -- ones that build on what the other
      person just said -- carried it. In speed dating, more follow-up questions
      went with more agreement to a second date. So a remembered detail is
      most useful turned into a question about it ("how did the move go?"),
      not as proof the sender remembered.
    grade: B
  - note: >
      THE LIMIT ON THAT RESULT. Every pair was meeting for the first time.
      Whether follow-up questions raise liking between old friends has not
      been tested in this design; it is carried by mechanism (responsiveness
      is also what close-relationship research names as central), not by a
      trial on established ties.
    grade: C
  - note: >
      GOOD NEWS IS WHERE THE RESPONSE COUNTS MOST. Sharing a good event was
      linked with more positive feeling than the event alone, more so when
      the listener responded actively and with interest. In dating couples
      observed on video, how partners responded to each other's GOOD news
      predicted relationship well-being and break-up two months later more
      closely than how they responded to bad news. Observational, couples,
      self-report plus coding. Practical reading: when the stored detail is
      something good that happened to them, the reach-out is worth more, and
      a curious, engaged reply is the form to suggest.
    grade: C
  - note: >
      BIRTHDAYS: THE EVIDENCE IS ABOUT RETURNED GREETINGS, NOT CLOSENESS. In a
      randomised field test on one person's Facebook friends, sending a
      birthday greeting raised the chance of getting one back by about half,
      and the effect faded over the months. That is reciprocity of a ritual.
      No source was located that links remembering a birthday or anniversary
      to how close a relationship is or stays. A birthday is therefore an
      easy, low-cost occasion to offer -- and nothing more. A skipped
      birthday carries no evidence of harm and must never be surfaced as a
      lapse.
    grade: D
  - note: >
      WHAT THIS ROW DOES NOT LICENSE. A birthday streak, a "you missed N
      birthdays" count, a reminder chain before a date, or a rule that close
      people "should" get a message on the day. Also not licensed: drafting a
      finished message that performs remembering. The evidence is about the
      question and the engagement, which have to be the owner's.
    grade: D
claim: >
  The shape of a reach-out matters more than proof of remembering. In randomised
  live conversations, people told to ask more questions -- especially FOLLOW-UP
  questions that build on what the other person said -- were liked more, via
  being seen as responsive (Huang et al. 2017, JPSP; first conversations between
  strangers). When someone shares GOOD news, an active, engaged response is
  linked with more positive feeling and better relationship well-being, and in
  79 dating couples responses to good news predicted well-being and break-up two
  months later more closely than responses to bad news (Gable et al. 2004, 2006;
  observational). For a nudge module: a remembered detail the person shared is
  best offered back as a follow-up question, and stored good news is the
  strongest occasion. BIRTHDAYS: the only primary evidence located is that a
  birthday greeting raises the chance of one coming back by about half, fading
  over months (Reyes 2018, one account's Facebook friends). No source links
  remembering a birthday or anniversary to closeness. A birthday is an easy
  opener offered once on the day; a skipped one is not a lapse, is never
  counted, and never resurfaces.
reasoning: >
  The craft lane (019) already hands over the last shared occasion as the
  opener but explicitly has no evidence for how that occasion should be used.
  Question-asking is the best-designed source located for it: question volume
  was randomly assigned in live exchanges, and the effect was traced to
  follow-up questions specifically, which is precisely what a stored detail
  makes easy. The transport problem is stated rather than hidden -- strangers,
  not old friends -- and the second note carries that limit at a lower band.
  Capitalization research adds that good news is a high-value moment and that
  engagement is the form; it is diary and observational couples data and is
  graded there. The birthday part is deliberately thin. The one randomised
  birthday study located measures a returned greeting, which is a reciprocity
  ritual, and pairing it with 072 keeps that from turning into a give-and-take
  tally. Birthday reminders are a feature a contact module grows by default;
  recording that the closeness benefit is unevidenced keeps the feature as an
  occasion and stops it becoming a duty. Not marked contested: no dispute was
  located, only absence on the birthday question.
---

# relationships-communication/remembered-detail-follow-up-071 -- 기억해 둔 일, 생일은 어떻게 쓰나

**한 줄 그림:** 기억해 둔 일은 "그거 어떻게 됐어?" 같은 후속 질문으로 건넨다. 생일은 연락하기 쉬운 계기일 뿐이고,
놓쳐도 빚이 아니다.

## What the engine reads from this row

| message rule | what the module offers | basis strength |
|---|---|---|
| carry the detail as a question | the shared detail + a question stem about it | randomised (strangers) |
| good news gets engagement | stored good news flagged as the best occasion; suggest a curious reply | observational |
| birthday is an occasion | one offer on the day; skip is not logged as a miss, never resurfaces | no closeness evidence |
| owner's words, not a template | detail + at most a question stem; never a finished message | design |

## 한국어 요약 (답변용)

- 처음 만난 사람끼리 채팅하는 실험에서 한쪽에 질문을 많이 하라고 무작위로 지시했더니 상대가
  그 사람을 더 좋아했다. 특히 상대가 방금 한 말을 이어받는 후속 질문이 효과를 냈다. 상대가 "내
  말을 들어 준다"고 느꼈기 때문이다. 스피드 데이트에서도 후속 질문이 많을수록 다음 만남에 응한
  경우가 많았다.
- 그래서 기억해 둔 일(이사, 시험, 가족 병환, 프로젝트)은 "내가 이걸 기억해"가 아니라 "그거
  어떻게 됐어?"라는 질문으로 건네는 게 맞다. 다만 이 실험은 모두 처음 만난 사이였다. 오래된
  친구 사이에서 같은 실험을 한 연구는 없다.
- 좋은 소식에는 관심 있게 반응하는 게 중요하다. 좋은 일을 나누고 상대가 적극적으로 반응해 준
  경우 기분과 관계 만족이 더 좋았다. 연애 중인 커플 79쌍을 본 연구에서는 나쁜 소식보다 좋은
  소식에 어떻게 반응했는지가 두 달 뒤 관계 만족·이별을 더 잘 예측했다. 관찰 연구다.
- 생일: 페이스북 친구에게 생일 축하를 무작위로 보낸 실험에서, 축하를 받은 사람이 나중에 보낸
  사람 생일에 축하를 돌려줄 확률이 약 50% 올랐고 시간이 지나면 약해졌다. 이건 '돌려주기'에
  대한 결과다. 생일을 기억하는 게 관계를 가깝게 한다는 연구는 찾지 못했다.
- 그래서 생일은 그날 한 번, 연락하기 쉬운 계기로만 알려 준다. 놓쳐도 기록하지 않고 다시
  꺼내지 않는다. "생일 N번 놓침", 연속 기록, 미리 여러 번 알림은 하지 않는다. 완성된 축하
  문구를 대신 써 주지도 않는다. 기억한 내용과 질문 하나까지만 건넨다.
