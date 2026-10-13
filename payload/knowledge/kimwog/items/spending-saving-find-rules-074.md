---
# Shopping / decision sprint 2026-10-07 (dispatch task kw-sh-product-choice-overload).
# The engine-readable synthesis of 028 (when overload holds), 029 (small diverse
# aligned set), 030 (learning from picks) and 031 (ratings). It is a routing
# rule, not a primary finding: each rule names the graded row it rests on, and
# every product constant (set size, repetition threshold, review-count floor)
# is labelled as a constant. Same posture as exercise/caution-severity-ladder-056.
#
# find_rules is structured data for a find-things skill. Each rule: id, when
# (trigger), do (action), constant (the product number, or none), basis (item
# id), basis_grade. Values are DIRECTIONS and product constants, never measured
# thresholds.
id: spending-saving/find-rules-074
domain: spending-saving
grade: D (synthesis rule over 028-031; directions are B/C-backed, every number is product judgement)
lane: "@household-behavioral"
locale: universal
as_of: 2026
contested: no
sources:
  - "spending-saving/choice-overload-conditional-028"  # overload is conditional; four moderators
  - "spending-saving/small-diverse-candidate-set-029"  # small, diverse, aligned set
  - "spending-saving/picks-are-relative-taste-signal-030"  # picks are relative, position-biased
  - "spending-saving/star-rating-weak-quality-signal-031"  # ratings are weak, biased, gameable
  - "spending-saving/flat-rate-usage-overestimation-010"  # buying for a future self that does not show up
  - "dispatch task 2026-10-07 kw-sh-product-choice-overload: engine-readable rules for a find-things skill, grounded in graded knowledge"
  - "framework:GRADE -- the directions (fewer and more diverse beats many and similar; picks are pairwise; stars are a tie-breaker) carry the grades of 028-031; the set size 3-4, the repetition count 3, the review-count floor and the slot rotation are product constants with no direct evidence."
find_rules:
  - id: set-size
    when: presenting candidates for one request
    do: show 3 to 4 candidates; more only on explicit user request
    constant: 3-4
    basis: spending-saving/small-diverse-candidate-set-029
    basis_grade: D
  - id: set-diversity
    when: choosing which candidates fill the set
    do: each candidate represents a different trade-off on the user's axes; all plausible on the user's hard constraints; no two slots for the same model in another colour or size
    constant: none
    basis: spending-saving/small-diverse-candidate-set-029
    basis_grade: C
  - id: align-axes
    when: rendering the set
    do: show every candidate on the same 1-2 user-named axes (price plus the axis the user stated), and lead each card with its one distinguishing label
    constant: 1-2 axes
    basis: spending-saving/choice-overload-conditional-028
    basis_grade: C
  - id: uncertain-preference
    when: user has no stated ideal or criteria (preference uncertainty)
    do: show contrasting archetypes as the set, or ask one sharpening question first; never a long list
    constant: none
    basis: spending-saving/choice-overload-conditional-028
    basis_grade: B
  - id: effort-goal
    when: user signals they want it done (just pick, 아무거나, quick)
    do: lead with one default and its reason, keep the others as collapsed alternatives
    constant: none
    basis: spending-saving/choice-overload-conditional-028
    basis_grade: B
  - id: deferral-is-overload
    when: user defers ("later", "let me think") or asks to switch after picking
    do: treat as an overload signal; next time narrow the set or align harder; do not re-send the same set
    constant: none
    basis: spending-saving/choice-overload-conditional-028
    basis_grade: B
  - id: pick-is-pairwise
    when: user picks a candidate
    do: record chosen-over-each-shown-alternative on the axes where they differed; no record for unshown items
    constant: none
    basis: spending-saving/picks-are-relative-taste-signal-030
    basis_grade: C
  - id: no-dislike-from-non-pick
    when: a candidate was shown and not picked
    do: write no dislike for it, its brand, colour or price band
    constant: none
    basis: spending-saving/picks-are-relative-taste-signal-030
    basis_grade: C
  - id: rotate-slots
    when: ordering candidates in the set
    do: vary slot order across sessions (do not always put the top score first) and store slot position with each pick
    constant: none
    basis: spending-saving/picks-are-relative-taste-signal-030
    basis_grade: C
  - id: confirm-on-repeat
    when: the same trade-off has won in repeated picks
    do: state it back to the user as an observed tendency once it has won 3 times; until then do not act on it silently
    constant: 3 picks
    basis: spending-saving/picks-are-relative-taste-signal-030
    basis_grade: D
  - id: stated-vs-picked
    when: picks contradict a stated preference
    do: ask once which should lead; never overwrite either side silently
    constant: none
    basis: spending-saving/picks-are-relative-taste-signal-030
    basis_grade: D
  - id: stars-tie-break
    when: using ratings
    do: never rank the set by star average; use it only to break a near-tie between candidates
    constant: none
    basis: spending-saving/star-rating-weak-quality-signal-031
    basis_grade: C
  - id: thin-reviews
    when: a candidate's review count is below the floor, or the profile is young with mostly 5 and 1 scores
    do: label its rating as uncertain or low-confidence; do not show it as a score
    constant: review-count floor (product constant; no source sets it)
    basis: spending-saving/star-rating-weak-quality-signal-031
    basis_grade: D
  - id: read-the-middle
    when: judging fit for the user's axes
    do: summarise what 2-4 star reviews say about the user's axes rather than the average
    constant: none
    basis: spending-saving/star-rating-weak-quality-signal-031
    basis_grade: C
  - id: kr-sponsored
    when: a KR review is marked 협찬, 광고, 제공 or 소정의 원고료
    do: treat as advertising, exclude from any review summary
    constant: none
    basis: spending-saving/star-rating-weak-quality-signal-031
    basis_grade: D
  - id: recurring-per-use
    when: a candidate is a subscription or flat-rate plan
    do: show the per-use price at the user's realistic, not hoped-for, frequency next to the pay-per-use option
    constant: none
    basis: spending-saving/flat-rate-usage-overestimation-010
    basis_grade: B
refraction_notes:
  - note: >
      THE DIRECTIONS ARE THE EVIDENCE, THE NUMBERS ARE NOT. That a small
      diverse aligned set beats a long similar one, that a pick is a
      comparison and that stars are a weak signal carry the grades of 028-031.
      The 3-4 set size, the 3-pick repetition rule and any review-count floor
      are product constants; speak them as the skill's rule.
    grade: D
  - note: >
      OVERLOAD IS CONDITIONAL, SO THE NARROWING IS TOO. The rules that narrow
      hardest (uncertain-preference, effort-goal) fire on the moderators, not
      on every request. A user who asks for "all the options" or is clearly
      comparing on one axis they understand can get a longer aligned list;
      the evidence does not say a long list always hurts.
    grade: B
  - note: >
      THE SKILL NEVER INVENTS AN AXIS OR A PREFERENCE. Axes come from the
      user's words or a confirmed repeated tendency. A taste the user never
      stated and the picks have not yet shown three times is not used to
      filter.
    grade: D
claim: >
  A find-things skill follows sixteen rules in four groups. SET: show 3 to 4
  candidates, each a different plausible trade-off, all on the same 1-2
  user-named axes, each led by its one distinguishing label. MODERATORS: when
  the user has no stated ideal, show contrasting archetypes or ask one
  sharpening question; when they want it done, lead with one default; treat
  deferral or post-pick switching as an overload signal and narrow next time.
  PICKS: record a pick as chosen-over-each-shown-alternative, never as a
  dislike of the rest, rotate slot order and store position, confirm a
  tendency back to the user only after it has won 3 times, and ask once when
  picks and stated preference disagree. RATINGS: never rank by star average,
  use it only as a tie-breaker, mark thin or young-and-extreme review profiles
  as uncertain, summarise mid-range reviews on the user's axes, and treat
  Korean reviews marked as sponsored as advertising. For subscriptions, show
  the per-use price at realistic frequency. Directions are evidence-backed;
  counts and floors are product constants.
reasoning: >
  The rules come straight from the four graded rows and one existing lane
  item. 028 supplies the conditional framing and the moderator triggers, which
  is why the narrowest rules fire on preference uncertainty and an effort goal
  rather than always. 029 supplies set size and diversity, with the count
  labelled as a constant. 030 supplies the learning rules. 031 supplies the
  rating discounts. 010 already shipped the per-use arithmetic for flat-rate
  plans and is linked rather than duplicated. Graded at the practitioner
  band because it is a synthesis whose numbers no study sets; each rule's own
  basis_grade tells the consuming code how hard it may speak.
---

# spending-saving/find-rules-074 -- 찾아 주기 규칙

**한 줄 그림:** 후보는 3~4개, 서로 다른 장단점, 같은 기준 위에. 고른 건 비교로 기록하고, 별점은 동점
정리에만 쓴다.

## Rules

| Group | Rule | Constant | Basis | Band |
|---|---|---|---|---|
| set | show 3-4 candidates | 3-4 | 029 | constant |
| set | each a different plausible trade-off; no colour/size duplicates | -- | 029 | C |
| set | same 1-2 user-named axes, one distinguishing label per card | 1-2 axes | 028 | C |
| moderators | no stated ideal -> contrasting archetypes or one question | -- | 028 | B |
| moderators | "just pick" -> one default plus reason | -- | 028 | B |
| moderators | deferral / switching -> narrow next time | -- | 028 | B |
| picks | chosen over each shown alternative | -- | 030 | C |
| picks | no dislike from a non-pick | -- | 030 | C |
| picks | rotate slot order, store position | -- | 030 | C |
| picks | state a tendency back after 3 wins | 3 | 030 | constant |
| picks | stated vs picked disagree -> ask once | -- | 030 | D |
| ratings | never rank by stars; tie-break only | -- | 031 | C |
| ratings | thin or young-extreme reviews -> uncertain | floor | 031 | constant |
| ratings | summarise 2-4 star text on user's axes | -- | 031 | C |
| ratings | KR 협찬/광고/제공 -> advertising | -- | 031 | D |
| plans | per-use price at realistic frequency | -- | 010 | B |

## 한국어 요약 (답변용)

- 후보는 3~4개만 보여 준다. 각각 다른 장단점을 대표하고, 모두 사용자 조건은 만족해야 한다. 같은 제품의
  색·사이즈 차이는 별도 후보로 세지 않는다.
- 모든 후보를 사용자가 말한 기준 한두 개(가격 + 말한 기준) 위에 나란히 놓고, 카드마다 차이 하나를 앞에
  쓴다.
- 원하는 게 아직 흐리면 성격이 확실히 다른 후보를 보여 주거나 질문 하나를 먼저 한다. "그냥 골라 줘"면
  하나를 추천하고 이유를 말한다. 결정을 미루거나 고른 뒤 바꾸면 다음엔 더 좁힌다.
- 고른 건 "보여 준 나머지보다 이게 낫다"로 기록한다. 안 고른 걸 싫어한다고 적지 않는다. 순서는 돌려 가며
  보여 주고, 같은 방향 선택이 세 번 쌓이면 "가벼운 쪽을 고르시는 편이네요"처럼 말해 본다.
- 별점 평균으로 순위를 매기지 않는다. 비슷한 후보끼리 동점 정리에만 쓴다. 후기가 적거나 새 상품에 5점·1점만
  많으면 "아직 믿기 어렵다"고 말한다. 맞는지는 2~4점 후기 내용으로 본다. 협찬·광고·제공 표시 후기는 광고로
  보고 요약에서 뺀다.
- 구독·정액 상품은 실제로 쓸 횟수 기준의 1회당 가격을 건별 가격과 나란히 보여 준다.
- 방향은 연구로 뒷받침되지만, 3~4개·세 번·후기 수 기준은 제품이 정한 규칙이다. 답할 때도 그렇게 말한다.
