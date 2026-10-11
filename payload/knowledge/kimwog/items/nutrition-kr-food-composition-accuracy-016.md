---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). KR-LOCALE item.
# The KR check asked for in the sprint brief: when a Korean meal is logged, is the
# nutrient database behind it accurate for Korean food. Exactly one validation
# against chemical analysis was located, and it is old and narrow, so it ships at
# the observational band with a contested flag rather than being either quoted as
# settled or dropped. Filing it as a bounded finding is what stops a later pass
# from assuming the question was never asked.
id: nutrition/kr-food-composition-accuracy-016
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: KR
as_of: 2003
contested: yes
sources:
  - "https://doi.org/10.1620/tjem.200.7"  # Kim ES, Ko YS, Kim J, Matsuda-Inoguchi N, Nakatsuka H, Watanabe T, Shimbo S, Ikeda M. Tohoku J Exp Med 2003;200(1):7-15. PMID 12862306 -- 24-hour duplicate diet samples from 66 women in three Jeju Island locations, chemical analysis vs Korean Food Composition Tables
  - "source:nutrition/self-report-underreporting-007 -- the INDEPENDENT error source; that item covers what the user fails to report, this one covers what the table gets wrong about correctly reported food"
  - "source:nutrition/metabolizable-energy-atwater-015 -- the third independent error source, in the conversion from composition to available energy"
refraction_notes:
  - note: >
      THE POPULATION AND THE VINTAGE BOTH BOUND THIS HARD. 66 women aged 29-54 on
      Jeju Island, sampled for a 2003 publication, half homemakers and half
      farmers or fishers. That is a specific regional diet from over two decades
      ago, and the composition tables themselves have been revised since. The
      direction of each finding is usable as a caution; the percentages should not
      be quoted as current accuracy figures for a present-day Korean food database.
    grade: D
  - note: >
      THIS MEASURES THE TABLE, NOT THE LOG. The design fed correctly identified
      duplicate portions through the tables, so it isolates database error with
      portion estimation and food identification removed. A real consumer log adds
      both of those on top. This is therefore a FLOOR on the error of a Korean
      meal log, not an estimate of it.
    grade: B
  - note: >
      NO MODERN REPLICATION WAS LOCATED, and no validation at all was located for
      Korean mixed dishes as logged by a consumer application (jjigae, guk,
      bibimbap and similar composite servings), which is precisely where portion
      and composition ambiguity is worst. Recorded as an open gap. Do not fill it
      by inference from this study.
    grade: D
claim: >
  Korean food composition tables were accurate for energy and protein but biased
  for the other macronutrients when validated against chemical analysis of
  duplicate diets. In 66 Korean women providing 24-hour duplicate food samples,
  table-based estimates matched measured values closely for energy (estimated at
  over 98 percent of measured) and protein (101 percent), while overestimating
  lipid by about 24 percent and underestimating carbohydrate by about 8 percent.
  The authors concluded the tables are sufficiently accurate for total energy and
  protein but that care is required for fat and carbohydrate.
reasoning: >
  This is the only direct chemical validation of the Korean composition tables
  located in this pass, and its result is genuinely useful in shape: the two
  numbers a training consumer leans on hardest, energy and protein, are the two
  that validated cleanly, while the macronutrient split did not. That is a
  favourable finding, which is exactly why it needs the discipline applied rather
  than relaxed. One study, 66 women, one island, one regional diet, published in
  2003, against table editions that have since been revised. Under this lane's
  rules a single unreplicated study in a narrow population cannot carry a strong
  grade regardless of how convenient its answer is, so it sits at the
  observational band with a contested flag, meaning under-evidenced rather than
  disputed. The operational reading is deliberately asymmetric: the fat and
  carbohydrate cautions are safe to carry as cautions, while the reassurance about
  energy and protein must not be spoken as a current guarantee. It also bounds
  only the table, since correctly identified duplicate portions remove the
  portion-estimation and food-identification errors a real log contains.
---

# nutrition/kr-food-composition-accuracy-016

When a Korean meal is logged, the nutrient numbers come from Korean food
composition tables, and the obvious question is whether those tables match what
is actually in the food. One study has asked it directly: sixty-six women on Jeju
Island collected duplicate portions of everything they ate for twenty-four hours,
the samples went to chemical analysis, and the analysed values were compared
against what the tables predicted.

Energy came out within two percent and protein within one. Fat was overestimated
by roughly a quarter and carbohydrate underestimated by roughly eight percent. So
the two quantities a training consumer relies on most are the two that held up,
and the macronutrient split is where the tables drift.

That is a comfortable answer, which is the reason to be careful with it. It is
one study, on one island, in sixty-six women, published in 2003, against table
editions that have since been revised. The reassuring half of the result is the
half that should be trusted least, because a single unreplicated finding cannot
license a present-day guarantee. The cautionary half is safe to carry forward as
a caution.

One structural point is worth keeping separate. Because the study fed correctly
identified duplicate portions through the tables, it measures the database alone,
with portion guessing and food misidentification removed. A real meal log carries
those on top, and on top of that the systematic under-reporting that affects every
self-recorded diet. Three independent errors sit between a logged Korean meal and
the truth, and this study bounds only the smallest of them. No validation was
found at all for the case that matters most in a Korean log, the composite dishes
where one serving mixes many foods.
