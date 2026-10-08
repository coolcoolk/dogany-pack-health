---
# Shopping / decision sprint 2026-10-07 (dispatch task kw-sh-product-choice-overload:
# evidence base for a find-things skill). Filed under spending-saving because no
# shopping domain exists and opening one is a registry act for the merge, not
# for a parallel worker (GAPS.md spending-saving, v38 note). Every source below
# was read at the primary or its publisher abstract on 2026-10-07; what could
# not be read is named in the note on it.
id: spending-saving/choice-overload-conditional-028
domain: spending-saving
grade: B (two meta-analyses of experiments; the average effect is near zero, the moderators are the finding)
lane: "@household-behavioral"
locale: universal
as_of: 2000-2015
contested: yes
sources:
  - "Iyengar, S. S. and Lepper, M. R. (2000). When Choice is Demotivating: Can One Desire Too Much of a Good Thing? Journal of Personality and Social Psychology 79(6), 995-1006. Read in full: Study 1, 60% (145 of 242) stopped at the 24-jam display vs 40% (104 of 260) at the 6-jam display; nearly 30% (31) of limited-choice vs 3% (4) of extensive-choice consumers purchased, chi2(1, N = 249) = 32.34."
  - "Scheibehenne, B., Greifeneder, R. and Todd, P. M. (2010). Can There Ever Be Too Many Options? A Meta-Analytic Review of Choice Overload. Journal of Consumer Research 37(3), 409-425. https://doi.org/10.1086/651235 -- 63 conditions from 50 experiments, N = 5,036; mean effect virtually zero with considerable between-study variance; no sufficient conditions identified (publisher abstract read)."
  - "Chernev, A., Boeckenholt, U. and Goodman, J. (2015). Choice overload: A conceptual review and meta-analysis (working-paper title: When Product Assortment Leads to Choice Overload). Journal of Consumer Psychology 25(2), 333-358. https://doi.org/10.1016/j.jcps.2014.08.002 -- 99 observations, N = 7,202; four moderators (choice set complexity, decision task difficulty, preference uncertainty, effort-minimising decision goal); with moderators modelled the assortment-size effect is significant; satisfaction/confidence, regret, deferral and switching are interchangeable measures (abstract read at the Kellogg faculty page)."
  - "Gourville, J. T. and Soman, D. (2005). Overchoice and Assortment Type: When and Why Variety Backfires. Marketing Science 24(3), 382-395. https://doi.org/10.1287/mksc.1040.0109 -- alignable assortments (one compensating dimension) raise brand share; non-alignable assortments (many non-compensating dimensions) raise effort and anticipated regret and lower it (abstract read)."
  - "source:spending-saving/spending-self-prediction-bias-005 -- the same lane's evidence that intention is a weak guide to what a person will actually do; the jam study's outcome is a purchase, not a stated preference"
refraction_notes:
  - note: >
      THE JAM NUMBERS ARE ONE STORE ON TWO SATURDAYS. The 30 percent vs 3
      percent contrast is real and correctly reported, but it is a single field
      study of gourmet jam tasting, and the meta-analytic average across 50
      experiments sits near zero. Quote it as the study that started the
      literature, never as the size of the effect.
    grade: B
  - note: >
      THE MODERATORS ARE ONE META-ANALYSIS'S CODING. Chernev et al. found
      the effect once four moderators were modelled; Scheibehenne et al. coded
      their own moderators and found no sufficient condition. The two do not
      contradict on the average (near zero unconditionally) and disagree on how
      predictable the exceptions are. Treat the four moderators as the best
      available map, not a validated predictor.
    grade: C
claim: >
  "More options make people choose worse or not at all" is not a general law.
  Across 50 experiments (N = 5,036) the average effect of a larger assortment
  is virtually zero, with large spread between studies. The effect does appear,
  reliably enough to design around, under four conditions identified in a
  second meta-analysis (99 observations, N = 7,202): the options are hard to
  compare (complex, many attributes, no common dimension), the task is hard
  (time pressure, many attributes to weigh), the person does not yet know what
  they want (no articulated ideal), and the person wants to minimise effort
  rather than find the best. When it does appear it shows as lower satisfaction
  or confidence, more regret, deferral (not choosing at all), and switching.
  Non-alignable sets -- options that differ on different dimensions rather than
  along one shared one -- are the clearest trigger.
reasoning: >
  Graded at the strong band because both meta-analyses pool randomised
  experiments with behavioural or choice outcomes, and contested because the
  two disagree about whether the exceptions can be predicted. What carries for
  a find-things skill is the conditional, not the slogan: an agent cannot
  assume a long list will paralyse, and it cannot assume a long list is
  harmless when the user is unsure what they want, in a hurry, or looking at
  options that cannot be lined up on one axis. Those are exactly the states in
  which a user asks an agent to find something, which is why the item matters
  more than its zero average suggests. The jam study is kept in the sources as
  the origin and with its real numbers so a later retelling cannot inflate it.
---

# spending-saving/choice-overload-conditional-028 -- 선택 과부하는 조건부다

**한 줄 그림:** 선택지가 많다고 늘 망하지는 않는다. 비교하기 어렵고, 원하는 게 아직 흐리고,
빨리 끝내고 싶을 때만 확실히 문제가 된다.

The famous jam study is real: at an upscale grocery store, 24 flavours drew
more shoppers to the table than 6 (60 vs 40 percent stopped), but nearly 30
percent of those who saw 6 bought a jar against 3 percent of those who saw 24.

What the popular version leaves out is the next fifteen years. Pooling 50
experiments and over five thousand participants, the average effect of a
bigger assortment came out at roughly nothing, with studies scattered on both
sides. A second pooling of 99 observations found the effect is there once you
ask WHEN: the options are hard to compare, the decision itself is hard, the
person does not yet know what they want, or they just want to be done. Under
those conditions a bigger set means less satisfaction, more regret, more
"I'll decide later", and more switching.

The sharpest trigger is a set whose members differ on different things -- one
is cheaper, one is lighter, one has a better warranty -- rather than along one
shared scale. Lining options up on a common dimension takes much of the sting
out.

## Moderators (Chernev et al. 2015)

| Moderator | Raises overload when | A find-things skill can act by |
|---|---|---|
| Choice set complexity | options are non-alignable, many attributes, no dominant one | aligning candidates on 1-2 shared axes the user named |
| Decision task difficulty | time pressure, many attributes to trade | presenting fewer attributes per candidate |
| Preference uncertainty | user has no articulated ideal | asking one sharpening question or showing contrasting archetypes |
| Decision goal | user wants to minimise effort | leading with one default and the reason |

## 한국어 요약 (답변용)

- "선택지가 많으면 못 고른다"는 일반 법칙이 아니다. 실험 50개를 모으면 평균 효과는 거의 0이다.
- 다만 네 가지 조건에서는 실제로 나타난다: 선택지끼리 비교하기 어려울 때, 결정 자체가 어려울 때(시간
  압박·따질 항목이 많음), 본인이 뭘 원하는지 아직 모를 때, 그냥 빨리 끝내고 싶을 때.
- 나타나면 만족·확신이 떨어지고, 후회가 늘고, 결정을 미루고, 나중에 바꾼다.
- 가장 큰 유발 요인은 서로 다른 축에서 다른 후보들(하나는 싸고, 하나는 가볍고, 하나는 보증이 김)이다.
  같은 기준 한두 개로 나란히 놓아 주면 부담이 줄어든다.
- 잼 연구(6종 30% 구매 vs 24종 3%)는 한 매장 한 번의 결과다. 효과 크기로 인용하지 않는다.
