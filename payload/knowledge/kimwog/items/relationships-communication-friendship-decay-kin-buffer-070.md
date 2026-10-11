---
# Relationship-contact sprint 2026-10-06 (dispatch task kw-relationship-contact).
# The DECAY half of "maintaining ties": what longitudinal data says happens to
# closeness when contact falls, who is buffered, and whether a lapsed tie can
# be picked up again. It narrows -- does NOT close -- the cadence gap recorded
# at relationships-communication/contact-cadence-no-evidence-014: every source
# here gives a DIRECTION (less contact, less closeness, for friends) and none
# gives an interval. Read 014 first; this row must never be used to back a
# schedule.
#
# decay_signals is structured data for the lifekit person module. Values are
# DIRECTIONS and FLAGS, not intervals; no field here carries a day count.
id: relationships-communication/friendship-decay-kin-buffer-070
domain: relationships-communication
grade: C (friend closeness declines without maintenance while kin closeness holds; closeness tracks logged call volume; dormant strong ties reconnect with most of their strength); D (any conversion into a per-person interval, and the life-transition timing rule)
lane: "@dyadic"
locale: universal
as_of: 2011-2015
contested: no
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC4626528/"  # Roberts SGB, Dunbar RIM 2015, Hum Nat 26(4):426-450, doi 10.1007/s12110-015-9242-7, PMID 26489745 -- READ AT FULL TEXT 2026-10-06. 30 English school-leavers recruited, 25 completed all three waves (T1 month 1, T2 month 9, T3 month 18), 1291 network members rated for emotional closeness on a 1-10 scale. Friends' closeness fell (b=-0.62 per wave) while kin closeness rose (b=0.27); of inner-layer kin at T1 70.3% were still inner at T3 against 48.6% of inner-layer friends; long-known and inner-layer friends were NOT more resistant to decay (H3 not supported); adding more new friends at T2 predicted a larger closeness drop to old friends and kin between T2 and T3; increased contact or joint activity mitigated the friend decline. Authors' own limits: modest sample, all about 18 years old, recalled contact data
  - "https://doi.org/10.1016/j.evolhumbehav.2010.08.005"  # Roberts SGB, Dunbar RIM 2011, Evol Hum Behav 32(3):186-197 -- earlier paper on the same cohort ("The costs of family and friends"); cited from the bibliographic record and the shared abstract only, not read at full text
  - "https://arxiv.org/abs/1204.5602"  # Saramaki J, Leicht EA, Lopez E, Roberts SGB, Reed-Tsochas F, Dunbar RIM 2014, PNAS 111(3):942-947, doi 10.1073/pnas.1308540110, PMID 24395777 -- READ AT the arXiv full text 2026-10-06. 24 of the same students, 18 months of OBJECTIVELY LOGGED mobile calls plus surveys at 0, 9 and 18 months; multilevel models show (log) call count predicts rated emotional closeness and fewer days since face-to-face contact; each person keeps a stable call-distribution 'signature' (top alter about 0.20-0.25 of calls, top three about 0.40-0.48) despite heavy turnover of who fills it (Jaccard overlap of the top-20 alters between 6-month windows 0.36-0.44)
  - "https://ideas.repec.org/a/inm/ororsc/v22y2011i4p923-939.html"  # Levin DZ, Walter J, Murnighan JK 2011, Organ Sci 22(4):923-939, doi 10.1287/orsc.1100.0566 -- READ AT an author-hosted full text 2026-10-06. 224 Executive MBA students asked to consult dormant contacts (no communication for at least 3 years) on a work project, 129 completed both surveys; a robustness sample of 116 (95 completed). Reconnected formerly strong ties gave value comparable to or better than current ties; 'dormant strong ties did decay somewhat' but 'retained most of their strength'; the executives were 'initially reluctant to reconnect'. Not randomised in which ties were chosen (authors' own limitation)
  - "relationships-communication/contact-cadence-no-evidence-014"  # the interval stays absent; this row adds direction only
  - "relationships-communication/reach-out-appreciation-gap-013"  # the act of reaching out is under-valued, most of all toward distant ties
  - "relationships-communication/record-absence-not-neglect-018"  # an empty log is unknown, not a lapse -- decay_signals only reads RECORDED contact
  - "relationships-communication/dunbar-number-not-derivable-015"  # same research group; the layer counts are not derivable, the decay direction is a separate, observational finding
  - "framework:GRADE -- observational band. Roberts and Dunbar is prospective (closeness measured before the transition) with low attrition, but 25 eighteen-year-olds in one English city, recalled contact, one life transition. Saramaki adds objective call logs but the closeness link is an association at survey points, not a manipulation. Levin is a field assignment to reconnect, but participants chose which ties, in a work context, and it measures usefulness, not closeness. Direction consistent across all three; no trial manipulates contact. The gender split reported by Roberts and Dunbar (talking for women, activities for men) rests on 12 and 13 people and is NOT carried."
decay_signals:
  - signal: friend-contact-falling
    tie_type: friend
    reading: closeness is likely to drift down unless contact or shared activity is kept up; long-known or very close friends are not exempt
    nudge_ok: true
    basis: Roberts and Dunbar 2015 (H1, H3, H5)
    basis_grade: C
  - signal: kin-contact-falling
    tie_type: kin
    reading: closeness held or rose in the same window; a quiet stretch with family is weak evidence of drift
    nudge_ok: false
    basis: Roberts and Dunbar 2015 (H1)
    basis_grade: C
  - signal: life-transition
    tie_type: friend
    reading: a move, new school or job, or a burst of new people is when old friendships lost the most closeness; the transition, not distance itself, carried the effect for friends
    nudge_ok: true
    basis: Roberts and Dunbar 2015 (H2, H4); extrapolated beyond 18-year-old school-leavers
    basis_grade: D
  - signal: dormant-strong-tie
    tie_type: any
    reading: a formerly close tie that went quiet for years is not lost; reconnection restored most of its value, and people are reluctant beforehand
    nudge_ok: true
    basis: Levin, Walter and Murnighan 2011
    basis_grade: C
  - signal: own-pattern-shift
    tie_type: any
    reading: compare a person's recorded contact against the owner's own past pattern with that person, never against a population interval; each person's distribution of contact is stable while who fills it turns over
    nudge_ok: true
    basis: Saramaki et al. 2014 (signature persistence) plus design inference
    basis_grade: D
refraction_notes:
  - note: >
      FRIENDS DRIFT, FAMILY HOLDS -- in the one prospective whole-network study
      located. Over 18 months across the move from school to university or work,
      emotional closeness to friends fell while closeness to kin rose. Of the
      people in the inner circle at the start, about seven in ten relatives were
      still there at the end against about half of friends. Friends who stayed
      in the inner circle kept their closeness; those who slipped out lost it.
    grade: C
  - note: >
      CLOSENESS IS NOT SELF-SUSTAINING. Friendships that were older or already
      in the inner circle were no more resistant to the decline than newer or
      outer ones. What mitigated the decline was more contact or more shared
      activity after the separation. So the direction "contact keeps a
      friendship close" is supported; any interval at which that happens is
      not (014).
    grade: C
  - note: >
      THE BUDGET IS FINITE. People who added more new friends lost more
      closeness to old friends and to kin in the following months. Logged call
      data from the same cohort show each person keeps a stable shape of how
      contact is spread -- a few people take most of it -- while the people
      filling that shape change. Practical reading: a drop in contact with one
      person often means someone else took the slot, not neglect. Do not frame
      it as a failure.
    grade: C
  - note: >
      LOGGED CONTACT TRACKS CLOSENESS. In call records (not recall), more calls
      went with higher rated closeness and with shorter gaps since meeting face
      to face. This is an association across people and alters at three survey
      points; it does not show that adding calls raises closeness. It supports
      using recorded contact as a soft signal, never as a closeness score
      spoken back to the owner.
    grade: C
  - note: >
      A LAPSED TIE IS NOT A LOST TIE. Executives asked to reconnect with
      contacts they had not spoken to in three or more years found the
      formerly close ones had kept most of their strength and were as useful as
      current ties; they had been reluctant beforehand. Work setting, ties
      chosen by the participants, value measured as usefulness. Carried as
      permission to reconnect without apology (019), not as a promise about how
      the other person feels.
    grade: C
  - note: >
      WHAT THIS ROW DOES NOT LICENSE. No day count, no per-tier interval, no
      decay curve with a half-life, no "you are losing this friendship"
      statement. The kin result is a reason to stay quieter about family gaps,
      not a claim that family never needs contact. The gender split in the
      source is not used: twelve women and thirteen men cannot carry it.
    grade: D
claim: >
  In the one prospective whole-network study located (Roberts and Dunbar 2015,
  Human Nature; 25 English school-leavers, 1291 network members rated at 1, 9
  and 18 months), emotional closeness to FRIENDS fell over the transition from
  school to university or work while closeness to KIN rose; 70.3% of inner-layer
  kin stayed in the inner layer against 48.6% of inner-layer friends. Long-known
  and very close friends were not more resistant. More contact or shared activity
  after separation mitigated the decline, and adding many new friends predicted
  a larger drop toward old friends and family -- contact time is a finite budget.
  In the same cohort's objectively logged phone calls (Saramaki et al. 2014,
  PNAS; 24 people, 18 months), call volume tracked rated closeness, and each
  person kept a stable shape of how contact was spread across people while the
  people filling it turned over. A lapsed tie is not a lost one: executives who
  reconnected with contacts dormant for three or more years found formerly close
  ties kept most of their strength and value (Levin, Walter and Murnighan 2011,
  Organization Science), after being reluctant beforehand. All of this is
  DIRECTION. None of it gives an interval, and it narrows rather than closes the
  cadence gap at relationships-communication/contact-cadence-no-evidence-014.
  For a nudge module: a falling recorded contact pattern with a FRIEND, especially
  around a life transition, is a reasonable soft cue for an optional reach-out;
  the same pattern with family is a weak cue; a long-dormant close tie is worth
  offering, framed without apology; and every comparison is against the owner's
  own past pattern with that person, never a population interval.
reasoning: >
  The domain had refused a cadence (014) and recorded that self-reported ties
  are biased (012), but held nothing on what happens to closeness when contact
  falls -- the question a contact log raises most directly. The Roberts and
  Dunbar cohort is the best-fitting source located: closeness was measured
  BEFORE the transition, attrition was low (25 of 30), and the analysis is at
  the level of 1291 alters. Its weaknesses are stated by the authors themselves
  and are serious for transport: one age, one city, one transition, recalled
  contact. Saramaki et al. supply the objective-log piece that 014 named as the
  missing measurement, but only as a cross-sectional association with closeness,
  so 014's closing criterion (logged contact related to closeness CHANGE, or a
  manipulation) is still unmet. Levin et al. add the reconnection half, from a
  different population and a work purpose, which is why it is used only for the
  narrow claim that dormancy does not erase a strong tie. The structured
  decay_signals block exists so the module reads directions and flags rather
  than inventing a number; the own-pattern rule and the transition rule are
  design inferences and are graded at the bottom band accordingly. Not marked
  contested: nothing located disputes the direction; the dispute would be about
  magnitude and transport, which this row does not claim.
---

# relationships-communication/friendship-decay-kin-buffer-070 -- 연락이 줄면 가까움도 줄어드나

**한 줄 그림:** 친구는 연락이 줄면 멀어지는 쪽으로 가고, 가족은 그대로 간다. 오래 끊긴 가까운 사이는 다시 이어진다.
간격 숫자는 여전히 없다.

## What the engine reads from this row

| decay signal | tie | nudge ok | basis strength |
|---|---|---|---|
| contact with a friend falling (vs the owner's own past pattern with them) | friend | yes, optional and gentle | observational |
| contact with family falling | kin | no (weak cue) | observational |
| life transition: move, new job, many new people | friend | yes, a good moment | inference |
| formerly close, quiet for years | any | yes, no apology | observational (field) |
| comparison basis | any | owner's own pattern only, never a population interval | inference |

No field carries a day count. The interval stays absent (014).

## 한국어 요약 (답변용)

- 학교를 마치고 대학·직장으로 옮겨 간 영국 청소년 25명의 인맥 전체(1,291명)를 18개월 동안 따라간
  연구가 있다. 친구와의 가까움은 줄었고 가족과의 가까움은 오히려 늘었다. 처음에 가장 가까운
  원 안에 있던 사람 중 가족은 약 70%가 끝까지 남았고, 친구는 절반 정도만 남았다.
- 오래 알았거나 아주 가까운 친구라고 해서 덜 멀어지지 않았다. 연락이나 함께 하는 활동을 늘린
  경우에 덜 멀어졌다. 가까움은 저절로 유지되지 않는다는 뜻이다. 다만 며칠에 한 번 연락하라는
  간격은 어떤 연구에도 없다.
- 새 친구를 많이 사귄 사람일수록 옛 친구·가족과 더 멀어졌다. 연락에 쓰는 시간은 한정돼 있다.
  한 사람과 연락이 줄었다면 다른 사람이 그 자리를 채운 경우가 많다. 소홀함으로 몰지 않는다.
- 같은 학생들의 실제 통화 기록을 보면 통화가 많을수록 가깝다고 답했다. 사람마다 연락이 퍼지는
  모양은 오래 유지되고, 그 자리를 채우는 사람만 바뀌었다. 그래서 비교는 늘 '그 사람과 나의
  예전 연락 패턴'에 대고 하고, 일반적인 기준 간격에 대지 않는다.
- 몇 년 연락이 끊긴 옛 가까운 사이도 다시 연락하면 힘이 대부분 남아 있었다. 사람들은 미리
  망설였지만 결과는 좋았다. 다시 연락할 때 사과부터 할 필요는 없다.
- 하지 않는 것: "이 친구와 멀어지고 있어요" 같은 판정, 날짜 간격 제시, 가족과의 공백을 문제로
  삼기. 연구에 나온 남녀 차이(여자는 대화, 남자는 활동)는 각각 12-13명 자료라 쓰지 않는다.
