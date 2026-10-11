---
# Relationship-contact sprint 2026-10-06 (dispatch task kw-relationship-contact).
# The RECIPROCITY half of "maintaining ties". 012 records that perceived ties
# are over-assumed mutual and that nothing links tie asymmetry to any outcome;
# 021 forbids a "who does not reciprocate" feature on that basis. This row adds
# the POSITIVE reason from experimental work: in relationships people want to
# be communal, prompt tit-for-tat repayment and requests for repayment LOWER
# liking, and people track the other's NEEDS rather than a balance of inputs.
# A give/receive ledger is the exchange-relationship instrument, applied to
# the relationships where it backfires.
#
# reciprocity_rules is structured data for the lifekit person module.
id: relationships-communication/communal-no-scorekeeping-072
domain: relationships-communication
grade: C (where a communal relationship is wanted, prompt repayment or a request for repayment lowers attraction, and people track the other's needs rather than inputs -- small single-lab experiments with strangers, 1979-1986); D (the module rule that no give/receive balance or "your turn" prompt is shown)
lane: "@dyadic"
locale: universal
as_of: 1979-2018
contested: no
sources:
  - "https://clarkrelationshiplab.yale.edu/sites/default/files/files/Interpersonal%20attraction%20in%20exchance%20and%20commual%20relationships.pdf"  # Clark MS, Mills J 1979, J Pers Soc Psychol 37(1):12-24, doi 10.1037/0022-3514.37.1.12 -- READ AT the lab-hosted full text 2026-10-06. Experiment 1: 96 unmarried male students; desire for a communal relationship manipulated by whether the other person (a woman) was presented as available and new on campus or as married; a benefit given back right after the subject helped her LOWERED liking when a communal relationship was desired and RAISED it when an exchange relationship was expected. Experiment 2: 80 female introductory psychology students, a different manipulation; a request for a benefit right after being helped raised liking under exchange and lowered it under communal expectations
  - "https://doi.org/10.1037/0022-3514.51.2.333"  # Clark MS, Mills J, Powell MC 1986, J Pers Soc Psychol 51(2):333-338 -- two experiments: with no opportunity to reciprocate, people in communal conditions kept track of the other's NEEDS more than in exchange conditions, and did so even when nothing could be done to help; in exchange conditions tracking rose only with a chance of reciprocation. Cited from the record and secondary summaries; not read at full text
  - "https://perfilesycapacidades.javeriana.edu.co/en/publications/reciprocity-in-a-social-network-evidence-from-a-natural-field-exp/"  # Reyes LC 2018, Econ Bull 38(2):672-680 -- reciprocation of a birthday greeting happens without any prompt and fades over months; used here only to show the module need not engineer it
  - "relationships-communication/tie-reciprocity-perception-gap-012"  # perceived mutuality is biased; no source links asymmetry to an outcome
  - "relationships-communication/roster-without-chore-list-021"  # the craft rule this row gives an evidence reason for: no reciprocity feature, fade only on the owner's own declared gap
  - "relationships-communication/remembered-detail-follow-up-071"  # birthdays as an occasion, not a ledger entry
  - "relationships-communication/zombie-stat-retraction-rule-002"  # check before carrying a 1970s lab finding as settled
  - "framework:GRADE -- observational-band ceiling despite experimental design. Both papers randomise, but each experiment has 80-96 students, the 'relationship' is a manipulated expectation about a stranger, the work comes from one research programme, and no independent modern replication was located in this pass. The direction fits later communal-strength work by the same group, which was not re-read here. The product rule (no balance, no 'your turn') is design built on the direction and on 012, and sits at the bottom band."
reciprocity_rules:
  - rule: no-balance-display
    effect: never show or speak a count or ratio of who contacted whom, who gave what, or whose turn it is
    basis: Clark and Mills 1979; relationships-communication/tie-reciprocity-perception-gap-012
    basis_grade: C
  - rule: no-your-turn-prompt
    effect: an unanswered or unreturned contact is never a trigger and never appears in a nudge's reason
    basis: Clark and Mills 1979; relationships-communication/roster-without-chore-list-021
    basis_grade: D
  - rule: needs-not-inputs
    effect: what the module may carry forward is the person's situation (what they are going through, what they shared), not what the owner has given them
    basis: Clark, Mills and Powell 1986
    basis_grade: C
  - rule: owner-asks-reciprocity
    effect: if the owner asks "do they ever reach out to me?", answer from records only, with the 018 unknown caveat and the 012 bias note, and without a verdict on the relationship
    basis: relationships-communication/record-absence-not-neglect-018; relationships-communication/tie-reciprocity-perception-gap-012
    basis_grade: D
refraction_notes:
  - note: >
      REPAYING TOO PROMPTLY READS AS "WE ARE NOT CLOSE". In two experiments,
      when people wanted a communal relationship with someone, getting a
      benefit straight back after helping them -- or being asked for one --
      made them like that person less. When they expected an exchange
      relationship, the same repayment made them like the person more. Tit for
      tat is the grammar of exchange relationships, and in close ones it
      signals distance.
    grade: C
  - note: >
      IN COMMUNAL RELATIONSHIPS PEOPLE TRACK NEEDS, NOT SCORE. Where a
      communal relationship was wanted, people kept track of what the other
      person needed even when they could do nothing about it, and that
      tracking did not depend on any chance of being repaid. So the useful
      memory for a close tie is what the person is going through, which is
      exactly what 071's remembered detail is.
    grade: C
  - note: >
      HOW FAR TO TRUST IT. Students, strangers, a relationship that existed
      only as an expectation in a lab, 80-96 people per experiment, one
      research group, 1979 and 1986. No independent modern replication was
      located in this pass. The direction is plausible and consistent with the
      same group's later work; the size of the effect in real friendships is
      unknown.
    grade: C
  - note: >
      WHAT THE MODULE DOES WITH THIS. A contact module holding who-messaged-whom
      can compute a balance trivially, and that balance is the
      exchange-relationship instrument. It is not shown, not used as a
      trigger, and not used to rank. 012 already says nothing links asymmetry
      to any outcome; this row adds that keeping the score is itself the thing
      close relationships are defined against. If the owner asks directly, the
      records are given plainly, with the unknown caveat (018) and without a
      verdict.
    grade: D
claim: >
  In relationships people want to be close, keeping score backfires. In two
  randomised experiments (Clark and Mills 1979, JPSP; 96 male and 80 female
  students), when a communal relationship was desired, being repaid right after
  helping someone -- or being asked for a repayment -- LOWERED liking for them,
  while under an exchange expectation the same repayment raised it. People in
  communal conditions tracked the other person's NEEDS, even when they could not
  help, and not a balance of what had been given (Clark, Mills and Powell 1986).
  These are small, old, single-programme lab studies with strangers, so the
  direction is carried and the size is not. Combined with
  relationships-communication/tie-reciprocity-perception-gap-012 (perceived
  mutuality is biased; nothing links asymmetry to an outcome), the rule for a
  nudge module is: never display who contacted whom more, never fire or justify
  a nudge with "they reached out last" or "it is your turn", and carry forward
  the person's situation rather than the owner's contributions. Reciprocation
  of small rituals happens on its own -- a birthday greeting raises the chance
  of one back by about half (Reyes 2018) -- so the module need not engineer it.
reasoning: >
  021 already refuses a reciprocity feature, but on an absence (012: no source
  links asymmetry to harm). An absence is a weak defence against a feature that
  looks obviously useful, and a contact log makes the balance free to compute.
  The communal/exchange experiments supply a positive reason: the score is not
  neutral information in a close relationship, it is the marker of the other
  relationship type, and in the lab its prompt use lowered liking. The grade is
  held at the observational band on purpose even though the design is
  experimental, because the samples are small, the relationships were
  manipulated expectations about strangers, all the work is from one programme
  over forty years ago, and this pass did not locate an independent
  replication -- the kind of finding 002 says to check before treating as
  settled. The rules block is written so the module can enforce the ban
  mechanically (no balance field reaches a renderer) rather than relying on
  tone. Not marked contested: no published dispute was located; the risk is
  over-extension, not contradiction.
---

# relationships-communication/communal-no-scorekeeping-072 -- 누가 더 연락했는지 세면 안 되는 이유

**한 줄 그림:** 가까워지고 싶은 사이에서 주고받기를 바로바로 맞추면 오히려 덜 좋아한다. 셈은 보여 주지 않고,
그 사람이 요즘 겪는 일을 기억한다.

## What the engine reads from this row

| rule | effect | basis strength |
|---|---|---|
| no balance display | no who-contacted-whom count, ratio or "your turn" anywhere | small old experiments + 012 |
| no your-turn prompt | an unreturned contact is never a trigger or a stated reason | design |
| needs, not inputs | carry the person's situation forward, not the owner's contributions | small old experiments |
| owner asks directly | records only, with the unknown caveat (018) and the bias note (012), no verdict | design |

## 한국어 요약 (답변용)

- 1979년 실험에서 상대와 가까운 관계를 원하는 조건의 사람들은, 자기가 도와준 직후 상대가 곧바로
  갚거나 갚으라고 요청하면 상대를 덜 좋아했다. 거래 관계를 예상한 조건에서는 같은 행동이 호감을
  올렸다. 바로바로 주고받는 셈은 거래 관계의 문법이고, 가까운 사이에서는 거리감의 신호가 된다.
- 1986년 실험에서는 가까운 관계를 원하는 사람들이 주고받은 양이 아니라 상대에게 필요한 것을
  챙겨 봤다. 도와줄 방법이 없을 때도 그랬다.
- 믿을 수 있는 정도: 대학생, 처음 보는 상대, 실험실에서 만든 기대, 실험당 80-96명, 한 연구팀,
  40년 넘은 연구다. 독립적인 최근 재현은 이번에 찾지 못했다. 방향은 쓰되 크기는 말하지 않는다.
- 그래서 사람 모듈은 누가 더 많이 연락했는지, 누구 차례인지를 보여 주지도, 알림 이유로 쓰지도,
  순위에 넣지도 않는다. 대신 그 사람이 요즘 겪는 일(이사, 시험, 가족 일)을 기억해 둔다.
- 사용자가 "그 사람은 나한테 연락 안 하지?"라고 직접 물으면 기록만 그대로 말한다. 기록이 빠졌을
  수 있다는 점, 서로 가깝다는 느낌은 실제보다 부풀려지기 쉽다는 점을 함께 말하고, 관계가
  어떻다는 판정은 하지 않는다.
- 작은 답례는 저절로 돌아온다. 생일 축하를 보내면 나중에 돌려받을 확률이 약 50% 오른다는 실험이
  있다. 모듈이 억지로 맞출 필요가 없다.
