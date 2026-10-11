---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (cross-cutting re-audit pass:
# behaviour change, measurement, nudges). Every source below was read at the
# abstract or full text on 2026-10-06; no figure is reconstructed from memory.
# Fills a hole the re-audit found: the warehouse cited defaults (spending-saving
# 006) and implementation intentions (task-management 003) but had no general
# calibration for how big a "nudge" is.
#
# engine_rules is structured data for any Dogany module that picks between a
# default, a reminder and a message. Values are ORDERINGS and DISCOUNT
# DIRECTIONS; no field is an effect size to quote to the user.
id: learning-habits/nudge-effect-shrinks-at-scale-025
domain: learning-habits
grade: B (two large evidence bases agree on the direction -- 126 at-scale RCTs and a 200+ study meta-analysis with a bias-corrected reanalysis; magnitude unsettled)
lane: "@behavioral"
locale: universal
as_of: 2021-2022
contested: yes
sources:
  - "DellaVigna, S. and Linos, E. (2022). RCTs to Scale: Comprehensive Evidence From Two Nudge Units. Econometrica 90(1), 81-116. https://doi.org/10.3982/ECTA18709"
  - "Mertens, S., Herberz, M., Hahnel, U. J. J. and Brosch, T. (2022). The effectiveness of nudging: A meta-analysis of choice architecture interventions across behavioral domains. PNAS 119(1), e2107346118. https://doi.org/10.1073/pnas.2107346118"
  - "Maier, M., Bartos, F., Stanley, T. D., Shanks, D. R., Harris, A. J. L. and Wagenmakers, E.-J. (2022). No evidence for nudging after adjusting for publication bias. PNAS 119(31), e2200300119. https://doi.org/10.1073/pnas.2200300119 (PMC9351501, full text read)"
  - "learning-habits/small-trial-inflation-009"  # the same small-trial / selective-publication mechanism, measured in behavioural meta-analyses
  - "learning-habits/replication-calibration-001"  # the field-wide discount this item specialises
  - "spending-saving/automation-defaults-dominate-intention-006"  # the default evidence that does NOT rest on the nudge literature
  - "task-management/implementation-intentions-effect-shrinks-003"  # a planning prompt, same shrink-on-correction pattern
engine_rules:
  - rule: published-nudge-size-is-an-upper-bound
    applies_to: any effect size quoted from a single academic nudge paper or an uncorrected nudge meta-analysis
    action: speak as "smaller in practice"; never quote the published figure as what this user should expect
    basis: DellaVigna and Linos 2022 (8.7 pp in journals vs 1.4 pp at scale; selective publication with low power explains about 70 percent of the gap)
    basis_grade: B
  - rule: structure-over-information
    applies_to: choosing what a module does to change a behaviour
    order: [decision-structure (defaults, what happens if the user does nothing), decision-assistance (reminders, commitment prompts), decision-information (messages, framing, feedback)]
    action: prefer the earliest rung that the user has agreed to; do not escalate message volume when a structural option exists
    basis: Mertens 2022 ordering; Maier 2022 finds evidence AGAINST a mean effect for information and assistance after correction and undecided for structure
    basis_grade: C
  - rule: heterogeneity-means-test-not-assume
    applies_to: deciding whether a nudge is working for THIS user
    action: judge by the user's own before/after record over weeks, not by the literature's average; an absent record is not evidence of failure (see mental-health/absent-record-is-not-an-event-023)
    basis: Maier 2022 (evidence for heterogeneity in almost every category -- some nudges work even where the mean is null)
    basis_grade: C
  - rule: no-percentage-promises
    applies_to: any user-facing line about how much a reminder, streak, message or framing will help
    action: no number; say it may help a little and that the module will check
    basis: all three sources (magnitude unsettled)
    basis_grade: B
refraction_notes:
  - note: >
      THE DIRECTION IS SOLID, THE SIZE IS NOT. Every source agrees that the
      published nudge literature overstates the effect. They disagree on how
      much remains: DellaVigna and Linos still find a small, highly
      significant average at scale (1.4 percentage points, an 8 percent
      relative increase); Maier et al. find no evidence of an average effect
      after correction. Speak "small and variable", never "none" and never a
      published figure.
    grade: B
  - note: >
      DEFAULTS ARE THE PART LEAST TOUCHED BY THE CORRECTION. After bias
      correction the evidence for decision-structure interventions (defaults
      and the like) is undecided rather than against, and the strongest default
      evidence in this warehouse (Chetty et al. 2014, item
      spending-saving/automation-defaults-dominate-intention-006) is
      population administrative data, not the journal nudge literature. Do not
      let this item drag 006 down with it.
    grade: C
  - note: >
      NUDGE UNITS ARE A US GOVERNMENT SAMPLE. The at-scale trials are
      take-up outcomes (sign-ups, payments, enrolments) run by two US units on
      letters, emails and forms. Whether a personal assistant's in-app prompt
      to one user behaves like a mailed letter to millions is not tested.
    grade: C
claim: >
  A nudge works less well in the field than in the paper that reported it, and
  the gap is mostly a publication artefact. DellaVigna and Linos (2022)
  assembled all 126 randomised trials (23 million people) run by two of the
  largest US government nudge units and compared them with the academic trials
  in two recent meta-analyses: the journal papers average an 8.7 percentage
  point take-up effect (a 33.4 percent increase over control), the nudge units
  1.4 percentage points (8.0 percent) -- still sizable and highly significant,
  but about a sixth of the published size. Selective publication,
  exacerbated by low statistical power, explains about 70 percent of the
  difference. Mertens et al. (2022), pooling over 200 studies and 450 effect
  sizes, report an overall d of 0.45 with decision-structure interventions
  outperforming information and assistance, and also a moderate publication
  bias. Reanalysing those data with robust Bayesian bias correction, Maier et
  al. (2022) find no evidence for an overall effect, evidence against an effect
  for information and assistance interventions, undecided evidence for
  structure interventions, and evidence of heterogeneity almost everywhere --
  some nudges may work even where the average does not.
reasoning: >
  Graded at the strong empirical band on the DIRECTION only: two independent
  bases (a complete, unselected registry of at-scale RCTs, and a
  bias-corrected reanalysis of the largest meta-analysis) converge on "the
  published average is inflated". It is flagged contested because the
  remaining magnitude is genuinely disputed (small-but-real at scale versus no
  evidence after correction), and the two approaches answer slightly different
  questions (letters and forms at population scale versus a mixed lab and
  field literature). The operational consequence is the same either way, which
  is why the item ships: a module should prefer structure over messages,
  should never promise a size, and should judge a prompt by the user's own
  record. The ordering rule leans on the uncorrected Mertens ordering plus the
  corrected "undecided rather than against" for structure, which is weaker
  than the direction finding and is carried at the observational band.
---

# learning-habits/nudge-effect-shrinks-at-scale-025 -- 넛지는 논문보다 현장에서 작다

**한 줄 그림:** 넛지 논문의 효과는 상한선이다. 실제 현장에서는 훨씬 작고, 그 차이의 대부분은
출판 편향이다.

Two US government nudge units ran 126 randomised trials on 23 million people
and published every one of them, good result or bad. Their average effect was
1.4 percentage points. The academic papers on the same kind of intervention
averaged 8.7. Most of that gap is not that governments do it worse. It is that
journals mostly print the trials that worked, and small trials that happen to
work look enormous.

The biggest meta-analysis of nudging reported a respectable average and also
admitted to publication bias. When other researchers corrected for that bias,
the average effect lost its support. Reminders and information messages came
out with evidence against an effect. Changing the structure of the choice --
what happens if you do nothing -- came out undecided. In almost every category
the effects varied a lot, so some nudges do work. The average just does not
tell you which.

What this means for an assistant:

- Prefer structure over messages. If the user has agreed to an automatic
  default, that beats any number of prompts.
- Never promise a size. "This reminder will make you 30% more likely" is a
  published figure, and published figures are the upper end.
- Judge a prompt by this user's own record over weeks, not by the paper.

## 한국어 요약 (답변용)

- 넛지(알림, 메시지, 프레이밍)의 논문 속 효과는 상한선으로 본다. 미국 정부 넛지 조직의 시험
  126건 평균은 1.4%포인트로, 학술지 평균 8.7%포인트의 약 6분의 1이었다. 차이의 약 70%는
  성공한 연구만 실리는 출판 편향과 작은 표본 때문이다.
- 출판 편향을 보정한 재분석에서는 정보 제공형·도움형(알림 등) 넛지의 평균 효과가 뒷받침되지
  않았고, 기본값처럼 선택 구조를 바꾸는 방식은 판단 보류로 남았다.
- 그래서 메시지를 늘리기보다, 사용자가 동의한 경우 기본값·자동 설정을 먼저 쓴다.
- "이 알림으로 30% 더 잘하게 된다" 같은 숫자는 말하지 않는다. "조금 도움이 될 수 있고, 실제로
  도움이 되는지 기록으로 확인하겠다"고 말한다.
- 효과는 사람과 상황에 따라 크게 다르다. 판단은 논문 평균이 아니라 이 사용자의 몇 주 기록으로
  한다. 기록이 비어 있다고 실패로 치지 않는다.
- 근거가 일치하는 것은 "논문보다 작다"는 방향이고, 남은 크기는 아직 논쟁 중이다.
