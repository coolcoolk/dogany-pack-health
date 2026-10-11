---
# Shopping / decision sprint 2026-10-07 (dispatch task kw-sh-product-choice-overload).
# Joachims et al. 2005 read in full (SIGIR test-of-time reprint PDF); Hu, Koren
# and Volinsky 2008 read at secondary summaries of the paper's stated problem
# framing only -- carried for the framing, not for any number.
id: spending-saving/picks-are-relative-taste-signal-030
domain: spending-saving
grade: C (one eyetracking user study plus a methods paper; transfer from web search and media consumption to shopping picks is inferred)
lane: "@household-behavioral"
locale: universal
as_of: 2005-2008
contested: no
sources:
  - "Joachims, T., Granka, L., Pan, B., Hembrooke, H. and Gay, G. (2005). Accurately Interpreting Clickthrough Data as Implicit Feedback. Proceedings of the 28th ACM SIGIR Conference, 154-161. https://doi.org/10.1145/1076034.1076063 -- eyetracking user study (Phase I 34 Cornell undergraduates, normal Google ranking; Phase II 22 participants under normal, swapped-top-two or reversed rankings). Clicks are informative but biased: a trust bias toward higher-ranked links even when their abstracts are less relevant, and a quality bias from the overall result set; interpreted as absolute judgements clicks are unreliable, as RELATIVE preferences (clicked over skipped-above) they are reasonably accurate on average (full text read)."
  - "Hu, Y., Koren, Y. and Volinsky, C. (2008). Collaborative Filtering for Implicit Feedback Datasets. Proceedings of the 8th IEEE International Conference on Data Mining (ICDM), 263-272. https://doi.org/10.1109/ICDM.2008.22 -- implicit data carry no direct negative signal (an unchosen item may be unseen, not disliked) and a single action is low-confidence; repeated actions raise confidence (problem framing read via secondary summaries; full text not read)."
  - "spending-saving/small-diverse-candidate-set-029 -- the set the pick is made from; a diverse set makes a pick more informative because the rejected candidates differ on a known trade-off"
  - "spending-saving/spending-self-prediction-bias-005 -- stated intention is a weak guide to behaviour, which is why a pick outranks a stated preference when they disagree"
refraction_notes:
  - note: >
      A PICK IS A COMPARISON, NOT A RATING. The tested object is clicks on a
      ranked search page, not purchases from a 3-4 card set. The transfer --
      chosen over shown-and-not-chosen is the reliable part, the absolute
      "she likes X" is not -- is an inference from the same structure.
    grade: C
  - note: >
      POSITION LEAKS INTO THE PICK. Users clicked higher-ranked results more
      even when the order had been swapped. A skill that always puts its own
      favourite first will learn its own ordering back. Rotate or randomise
      slot order across sessions before learning from picks.
    grade: C
  - note: >
      THE UPDATE SIZES ARE THE SKILL'S. How much one pick moves a taste
      estimate, and how fast an old pick decays, are product constants. No
      source here supplies them.
    grade: D
claim: >
  What a person picks from a shown set is reliable evidence of a RELATIVE
  preference -- the chosen candidate over the ones they saw and passed over --
  and weak evidence of an absolute one. In an eyetracking study of search
  result clicks, clicks were informative but biased: people favoured whatever
  the system put on top even when it was less relevant, and the quality of the
  whole set shifted what they clicked. Read as "this is good", clicks were
  unreliable; read as "this beat those", they were reasonably accurate. Two
  further limits come from the implicit-feedback literature: nothing
  unchosen counts as disliked (it may simply not have been noticed), and one
  action is a low-confidence signal while repeated choices in the same
  direction are a stronger one. For a find-things skill that means: learn
  pairwise (chosen over the shown alternatives, on the axes where they
  differed), discount by slot position, never write a dislike from a non-pick,
  and raise confidence only on repetition.
reasoning: >
  This is the evidence for the "taste learning from picks" half of the skill.
  It sits in the observational band because the core study is one eyetracking
  experiment on web search with a few dozen undergraduates, and the second
  source is a modelling paper whose contribution is a framing, not a measured
  effect in shoppers. It ships because the structural point transfers cleanly
  and the failure it prevents is concrete: an agent that writes "user likes
  black / dislikes brand Y" from a single pick, or that learns from picks made
  under its own fixed ordering, will build a confident profile out of its own
  presentation choices. The diverse set of 029 makes each pick more useful,
  because the passed-over candidates differ on named trade-offs and the pick
  says which trade-off won.
---

# spending-saving/picks-are-relative-taste-signal-030 -- 고른 것은 "이게 저것보다 낫다"는 신호

**한 줄 그림:** 사용자가 3~4개 중 하나를 골랐다는 건 "보여 준 다른 것들보다 이게 낫다"는 뜻이지,
"이걸 좋아한다"나 "안 고른 걸 싫어한다"는 뜻이 아니다.

Researchers tracked people's eyes while they searched with Google, and
secretly swapped or reversed the result order for some of them. Clicks did
follow relevance, but people also clicked whatever sat on top more often, even
when the swap had put a worse result there, and the overall quality of the page
changed what they clicked. The conclusion: as "this one is good" a click is
shaky; as "this one beat the ones I looked at above it" it is reasonably
accurate.

The same structure applies to a person picking from a small set of
candidates. What the pick tells you is which trade-off won among the ones
shown. It does not tell you the unchosen ones are disliked -- they may not even
have been looked at properly -- and a single pick is one weak data point.
Consistent picks in the same direction are what earn confidence.

## Learning rule

| Signal | Read as | Do not read as |
|---|---|---|
| picked A from {A, B, C} | A over B and A over C, on the axes where they differ | "likes A" with high confidence |
| did not pick B | nothing about B on its own | dislike of B, its brand or its colour |
| same trade-off won 3+ times | a stable preference worth stating back | a rule to enforce silently |
| picked slot 1 again | partly position | pure taste, unless slot order was varied |
| user stated a preference that picks contradict | ask once; picks are what they did | overwrite either side silently |

## 한국어 요약 (답변용)

- 여러 후보 중 하나를 고른 건 "보여 준 나머지보다 이게 낫다"는 비교 신호다. "이걸 좋아한다"는 절대
  평가로 읽으면 부정확하다.
- 안 고른 후보를 싫어한다고 기록하지 않는다. 제대로 안 봤을 수도 있다.
- 사람은 맨 위·첫 번째에 놓인 것을 더 고른다. 순서를 늘 같게 두면 우리가 정한 순서를 다시 배우게
  된다. 순서를 돌려 가며 보여 준다.
- 한 번 고른 건 약한 신호다. 같은 방향의 선택이 여러 번 쌓일 때 "가벼운 쪽을 고르시는 편이네요"처럼
  되짚어 말한다.
- 한 번의 선택이 취향 추정을 얼마나 움직이는지, 예전 선택이 얼마나 빨리 잊히는지는 제품이 정하는
  값이다.
