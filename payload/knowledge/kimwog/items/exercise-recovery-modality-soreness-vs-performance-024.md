---
# Collection sprint 2026-08-22. Fills GAPS gap-areas 4 and 5 (active recovery /
# light-load movement between sessions; blood-flow and circulation-based
# recovery modalities). The organising axis of this item is the PERCEIVED
# SORENESS vs MEASURED PERFORMANCE split, because that is precisely where the
# popular versions of these claims fail. Rubric: exercise.rubric.md
# @performance-lit.
id: exercise/recovery-modality-soreness-vs-performance-024
domain: exercise
grade: C (modality -> performance recovery); B (stretching does not reduce soreness)
lane: "@performance-lit"
locale: universal
as_of: 2011-2026
contested: yes
sources:
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC5932411/"  # Dupuy/Douzi/Theurot/Bosquet/Dugue 2018, Front Physiol 9:403, meta-analysis of 99 studies, soreness/fatigue/CK/IL-6/CRP
  - "https://pubmed.ncbi.nlm.nih.gov/32426160/"  # Davis/Alabed/Chico 2020, BMJ Open Sport Exerc Med 6(1):e000614, meta-analysis 29 RCTs / 1012 participants, PERFORMANCE endpoints
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC6465761/"  # Wiewelhove et al. 2019, Front Physiol 10:376, foam-rolling meta 21 studies / 454 subjects
  - "https://pubmed.ncbi.nlm.nih.gov/29663142/"  # Van Hooren & Peake 2018, Sports Med 48(7):1575-1595, active cool-down narrative review
  - "https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.CD004577.pub3/abstract"  # Herbert/de Noronha/Kamper 2011, Cochrane Database Syst Rev CD004577, 12 studies / 2597 participants
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC8133317/"  # Afonso et al. 2021, Front Physiol 12:677581, post-exercise stretching meta of RCTs
  - "https://link.springer.com/article/10.1007/s40279-017-0728-9"  # Brown et al. 2017, Sports Med 47(11):2245-2267, compression-garment meta, 23 studies
  - "https://www.mdpi.com/2227-9032/14/10/1321"  # Healthcare 2026;14(10):1321, PMID 42194413, network meta-analysis ranking strategies on CMJ/DOMS/CK -- ABSTRACT-LEVEL VERIFICATION ONLY, full text returned 403 in this sprint
  - "framework:GRADE -- soreness and perceived-fatigue outcomes in this literature are (a) subjective and (b) collected in trials where blinding is practically impossible, so placebo cannot be excluded; the meta-analysts say so themselves. Objective performance outcomes are the harder test, and modality effects there are consistently smaller, shorter-lived, or absent. Where a modality moves soreness but not performance, this item reports BOTH and does not let the soreness result stand in for a recovery result."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      The blinding problem is not a footnote, it is the main threat to this
      whole literature. Dupuy 2018 states directly that the practical
      difficulty of blinding meant placebo effects could not be eliminated,
      and that it did NOT evaluate performance capacity at all, warning of a
      mismatch between blood or soreness measures and recovery of short-term
      muscular performance. Wiewelhove 2019 lists high placebo bias as a
      primary limitation for the same reason. A hands-on modality with a large
      soreness effect and a null performance effect is the exact signature of
      an expectation effect, and massage is that pattern.
    grade: C
  - note: >
      Massage is the sharpest worked example of the split. Dupuy 2018 gives
      massage the largest soreness effect of any modality (Hedges g -2.26,
      95% CI -3.05 to -1.47) and the largest perceived-fatigue effect
      (g -2.55). Davis 2020, restricted to 29 RCTs and 1012 participants and
      measuring PERFORMANCE, found no evidence that massage improves strength,
      jump, sprint, endurance or fatigue -- only small improvements in
      flexibility and soreness. Same intervention, two outcome families, two
      opposite verdicts. This does not make massage worthless; it makes it a
      comfort intervention with no demonstrated performance-restoration effect.
    grade: B
  - note: >
      Foam rolling is small and mostly negligible by its own meta-analysts'
      description. Wiewelhove 2019 (21 studies, 454 subjects): as a RECOVERY
      tool, post-rolling gives +2.0% overall performance (g 0.19), +3.1%
      sprint (g 0.34), +3.9% strength (g 0.21), -0.2% jump (g 0.06), and a
      6.0% reduction in muscle pain (g 0.47). As a WARM-UP tool, pre-rolling
      gives +1.5% overall (g 0.20) and +4.0% flexibility (g 0.34). The authors
      conclude the evidence justifies foam rolling more as a warm-up activity
      than as a recovery tool. The soreness effect is again the largest one.
    grade: C
  - note: >
      Timing window. The 2026 network meta-analysis reports that recovery
      effects after damaging exercise are time-dependent and concentrate in
      the FIRST 24 HOURS rather than at 48-72 h, with active recovery ranking
      best for short-term jump recovery, massage best for early soreness, and
      cold-water immersion most consistent across soreness and creatine
      kinase. Treat modality choice as goal-specific and short-window. NOTE:
      this source was verified at ABSTRACT level only in this sprint (full
      text returned HTTP 403); its specific rankings are carried as reported,
      not independently checked against the forest plots.
    grade: C
  - note: >
      Cold-water immersion carries a separate, orthogonal cost not covered by
      any source in this item: regular post-session cold exposure has been
      argued to blunt long-term hypertrophy and strength adaptation. That
      literature was NOT researched in this sprint and no claim is made about
      it here. It is an open sub-gap, flagged so the absence is not read as
      an all-clear.
    grade: D
claim: >
  Blood-flow and circulation-based recovery modalities (massage, foam rolling,
  compression garments, cold or contrast water immersion, active recovery) move
  PERCEIVED soreness and PERCEIVED fatigue reliably and often substantially, but
  the evidence that they restore measured PERFORMANCE is much weaker,
  shorter-lived, and in the case of massage absent. Worked contrast: the largest
  soreness meta-analysis (99 studies) ranks massage first for reducing soreness
  (Hedges g -2.26) and perceived fatigue (g -2.55), yet explicitly did not
  measure performance; a separate meta-analysis restricted to performance
  endpoints (29 RCTs, 1012 participants) found NO evidence that massage improves
  strength, jump, sprint, endurance or fatigue. Foam rolling's own meta-analysts
  describe its effects as minor and partly negligible (post-rolling +2.0%
  overall performance, g 0.19) and recommend it more as a warm-up than as a
  recovery tool. An active cool-down is largely ineffective for enhancing
  same-day or next-day performance. Stretching, before or after exercise, does
  NOT reduce soreness: a Cochrane review of 12 studies and 2597 participants
  found the differences small, PRECISE, and not clinically worthwhile, and a
  later meta of post-exercise stretching found no effect on strength recovery or
  on soreness at 24, 48 or 72 h. Compression garments are the modest exception
  with an objective signal, showing benefit for strength recovery beyond 24 h.
  These trials are unblindable by construction, so the soreness effects cannot
  be separated from expectation. The operative rule: a modality that reduces how
  sore something FEELS has not thereby been shown to restore what the muscle can
  DO, and the two must be reported separately.
reasoning: >
  Two meta-analyses of the same intervention with different outcome families
  produce opposite verdicts, and that dissociation is the finding. Dupuy et al.
  2018 (Front Physiol 9:403), pooling 99 studies, reports meaningful soreness
  reductions for massage (g -2.26, 95% CI -3.05 to -1.47), active recovery
  (g -0.94), compression garments (g -0.92), cryotherapy (g -0.53), immersion
  (g -0.47) and contrast water therapy (g -0.40), with stretching (g +0.15) and
  electrostimulation (g -0.28) showing nothing. It also finds active recovery
  has NO effect on perceived fatigue (g +0.64, CI crossing zero) even though it
  reduces soreness. The authors state plainly that they did not evaluate
  performance capacity and warn of a mismatch between blood or soreness measures
  and recovery of short-term muscular performance. Davis, Alabed & Chico 2020
  (BMJ Open Sport Exerc Med 6(1):e000614), running the performance test that
  Dupuy did not, found across 29 RCTs and 1012 participants no evidence massage
  improves strength, jump, sprint, endurance or fatigue -- only flexibility and
  soreness. Wiewelhove et al. 2019 (Front Physiol 10:376, 21 studies) reach the
  same shape for foam rolling: the largest post-rolling effect is on muscle pain
  (6.0%, g 0.47) while performance effects sit at or under g 0.34 and the
  authors call them minor and partly negligible. Van Hooren & Peake 2018 (Sports
  Med 48(7):1575-1595) conclude an active cool-down is largely ineffective for
  psychophysiological recovery markers and specifically for same-day and
  next-day performance, does not prevent injury, and does not appear to blunt
  long-term adaptation. The stretching result is the strongest single negative
  in the set: Herbert, de Noronha & Kamper 2011 (Cochrane CD004577) pooled 12
  randomized studies and 2597 participants and found the difference between
  stretching and not stretching small, PRECISE (tight confidence intervals) and not
  clinically worthwhile -- precision is what makes this a genuine null rather
  than an underpowered one, which is why it grades higher than the rest of the
  item. Afonso et al. 2021 (Front Physiol 12:677581) independently found no
  effect of post-exercise stretching on strength recovery or on soreness at 24,
  48 or 72 h, while honestly rating their own cumulative confidence as very low.
  Brown et al. 2017 (Sports Med 47(11):2245-2267, 23 studies) is the main
  counterweight: compression garments show benefit for strength recovery in the
  2-8 h window and beyond 24 h, most effectively after resistance exercise --
  an objective outcome, though from a modality that is also unblindable.
  Contested flag is set because the practitioner and consumer consensus around
  these modalities is stated far more strongly than the performance evidence
  supports, and because the two meta-analyses above genuinely disagree once you
  fail to notice they measured different things.
---

# exercise/recovery-modality-soreness-vs-performance-024

There are two different questions hiding inside "does this help me recover," and
almost every popular claim about recovery tools answers only the easy one.

Question one: does it make you feel less sore and less beaten up? For the
blood-flow family -- massage, foam rolling, compression, cold or contrast water,
light active recovery -- the answer is yes, and for massage the effect is large.
The biggest pooled analysis, covering 99 studies, puts massage at the top for
both soreness and perceived fatigue by a wide margin.

Question two: does it restore what the muscle can actually do? Here the same
tools mostly stop working. A separate analysis of 29 randomized trials and over
a thousand participants, this time measuring strength, jump, sprint, endurance
and fatigue, found no evidence massage improves any of them -- only flexibility
and soreness. Foam rolling's own meta-analysts describe its effects as minor and
partly negligible, and recommend it more as a warm-up than as a recovery tool.
An active cool-down turns out to be largely ineffective for same-day and
next-day performance. Compression garments are the one modality with a
reasonably clean objective signal, showing benefit for strength recovery beyond
24 hours after resistance work.

Stretching gets its own line because it is the most confidently held belief in
the set and the most cleanly refuted. A Cochrane review of 12 randomized studies
and 2,597 participants found that stretching -- before exercise, after exercise,
or both -- produces differences in soreness that are small, tightly bounded, and
not clinically worthwhile. Tightly bounded is the important word: this is a
demonstrated absence of effect, not a failure to find one. A later analysis of
post-exercise stretching specifically found no effect on strength recovery or on
soreness at 24, 48 or 72 hours.

The structural problem underneath all of it: you cannot blind someone to a
massage or a foam roller. The researchers say this themselves. So a modality
that produces a huge subjective effect and a null objective one is showing you
the exact fingerprint of an expectation effect, and it should be reported that
way rather than rounded up into "it aids recovery."

Which does not make these tools pointless. Feeling less sore is worth something
on its own terms, and if it keeps someone training consistently it is worth a
lot. It is just not the same claim as "this restores my strength faster," and
the two should never be spoken as one.

Open sub-gap, flagged rather than papered over: the argument that regular
post-session cold exposure blunts long-term muscle and strength adaptation was
not researched in this pass. Nothing here should be read as clearing it.

## Applicability check (2026-08-22) -- NOT adopted, implication only

Checked against `files/program/prep.yaml`. **Nothing changed, nothing proposed.**

Current state: the `cooldown` block was seeded on 2026-08-22 with exactly one
item, HP1 고관절 스트레칭, carrying no duration and no parenthetical because none
was ever specified by the owner. Its provenance is owner decision F20, recorded
in `workout-session/SKILL.md` prose as a session-closeout cooldown item. There is
no massage, foam-rolling, compression or immersion entry anywhere in the program.

What this item would imply:

1. HP1's RATIONALE, not its existence, is what the evidence touches. If the
   cooldown block is justified as recovery -- reducing soreness or speeding
   readiness for the next session -- that justification is not supported:
   post-exercise stretching has been measured to have no effect on soreness at
   24, 48 or 72 hours and no effect on strength recovery, and the null is a
   precise one, not an underpowered one. If it is justified as hip range-of-
   motion maintenance, it stands on its own footing and this item says nothing
   against it. Restating the rationale would be a prose change in
   `stretch-matrix.md`, which is reference material, not data -- and it is the
   owner's call, not this sprint's.
2. Nothing here argues for REMOVING HP1. A cooldown stretch that the owner
   values is a legitimate mobility and wind-down item. The correction is to what
   it is claimed to do, not to whether it is done.
3. If a recovery modality is ever added to the program, the item that has the
   cleanest objective signal is compression garments (strength recovery beyond
   24 h after resistance work) -- not massage or foam rolling, which are the two
   with the biggest reputations and the weakest performance evidence.
4. Any modality added should be evaluated against a performance readout, not
   against how sore he reports feeling, for the reason the whole item exists.
