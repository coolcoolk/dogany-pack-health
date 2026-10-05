---
# Collection sprint 2026-08-23, fourth of four items closing the LOAD-INCREMENT
# SIZE / MICROLOADING gap. Included because "just autoregulate the load" is the
# standard escape from the increment question, and it turns out to be an escape
# into an instrument whose own error is larger than the increments under
# dispute. Rubric: exercise.rubric.md @performance-lit -- the material is
# sports-science meta-analysis plus a network meta-analysis with internal
# contradictions, which is precisely what
# exercise/replication-power-crisis-005 and exercise/small-n-culture-006 are for.
id: exercise/autoregulation-vs-percentage-prescription-030
domain: exercise
grade: B (autoregulated and percentage-based prescription produce similar strength gains); C (the RIR-error magnitude relative to a plate step)
lane: "@performance-lit"
locale: universal
as_of: 2021-2025
contested: yes
sources:
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8762534/"  # Hickmott LM et al. 2022, Sports Med Open 8:9 -- 6 studies, n=133 trained; MD 2.07 kg, 95% CI -0.32 to 4.46, p=0.09, SMD 0.21
  - "https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0259790"  # Liao 2021, PLOS ONE 16(10):e0259790 -- 6 studies, n=124; squat 1RM MD 3.03 kg, 95% CI -3.55 to 9.61, p=0.37; PARTIALLY OVERLAPPING with Hickmott (shares Banyard, Dorrell, Orange -- 3 of 6 each)
  - "https://pubmed.ncbi.nlm.nih.gov/40791980/"  # Huang et al. 2025, J Exerc Sci Fit 23(4):360-369 -- network meta-analysis claiming APRE/VBRT/RPE beat percentage-based; abstract internally contradictory, see refraction_notes
  - "https://pubmed.ncbi.nlm.nih.gov/37436724/"  # Remmert JF et al. 2023, Percept Mot Skills 130(5):2139-2160, doi 10.1177/00315125231189098 -- RIR prediction accuracy does not improve over 6 weeks of bench press training
  - "https://journals.lww.com/nsca-jscr/abstract/2024/03000/accuracy_of_intraset_repetitions_in_reserve.26.aspx"  # Refalo MC et al., J Strength Cond Res 38(3):e78-e85 (online 2023), doi 10.1519/JSC.0000000000004653 -- intraset RIR prediction accuracy in resistance-trained men and women
  - "exercise/increment-verification-floor-029"  # within-warehouse: the measurement-side bound, and the reps-per-percentage spread that limits the percentage framing too
  - "exercise/load-increment-size-evidence-gap-027"  # within-warehouse: the gap this item does NOT fill -- autoregulation is not an answer to increment size
  - "framework:GRADE -- the no-difference direction rests on two meta-analyses that are PARTIALLY DEPENDENT (3 of 6 studies shared), so it is one and a half replications, not two. Total pooled n is small (133 and 124 trained participants). The RIR-error figures come from small primary studies (single digit to low double digit n) and are graded lower accordingly. The dissenting network meta-analysis is not treated as a counterweight because its own abstract does not cohere."
applicability:
  axes:
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      Two meta-analyses, not two independent replications. Hickmott 2022
      (6 studies, n=133 trained) and Liao 2021 (6 studies, n=124) share three
      of their six included studies each -- Banyard, Dorrell and Orange. They
      are PARTIALLY DEPENDENT and must be spoken as such. Reporting them as two
      separate confirmations inflates the apparent evidence base by roughly
      double. What actually exists is a small, largely shared pool of trained
      participants studied over short blocks.
    grade: C
  - note: >
      "Similar improvements" is not "equivalent", and the same non-inferiority
      discipline applied to Hostler 2001 on
      exercise/load-increment-size-evidence-gap-027 applies here. Hickmott's
      pooled mean difference is 2.07 kg with a 95% confidence interval of -0.32
      to 4.46 kg and p=0.09; Liao's squat estimate is 3.03 kg with an interval
      of -3.55 to 9.61 and p=0.37. Neither declares an equivalence margin and
      neither runs an equivalence test, so both intervals remain compatible with
      a difference of several kilograms in either direction. The correct reading
      is that no difference was DETECTED in a small pool, which is why the
      practical instruction ("do not switch methods expecting a strength
      dividend") is safe while the theoretical claim ("the methods are
      equivalent") is not established.
    grade: B
  - note: >
      CONTESTED, with the counter recorded in full. Huang et al. 2025 (J Exerc
      Sci Fit 23(4):360-369) is a network meta-analysis claiming that APRE,
      velocity-based and RPE-based prescription significantly outperform
      percentage-based, with APRE ranked at SUCRA 93.0% for the squat and 97.1%
      for the bench. Its own abstract does not cohere. It states that no
      moderate or large effect sizes were observed between interventions for
      squat 1RM while simultaneously ranking APRE at 93.0%. It describes an
      RPE-versus-APRE standardized mean difference of -0.76 with an interval of
      -1.70 to 0.19 -- an interval that crosses zero -- as "a moderate effect".
      It asserts that velocity-based and RPE-based prescription beat
      percentage-based significantly, while no such estimate appears anywhere in
      the abstract. Exactly ONE comparison in that abstract has an interval
      excluding zero: bench press, percentage-based versus APRE, SMD -0.83
      (-1.22 to -0.44). SUCRA produces a complete ranking even when every
      pairwise interval overlaps zero, and it is unstable when a network has few
      studies per node -- so a high SUCRA percentage is not evidence of
      superiority. Study count, total N and population could not be verified
      (the retrieval returned 403 twice). Stored as contested and disfavoured,
      not as a competing finding.
    grade: D
  - note: >
      The autoregulation instrument's own error is LARGER than the increments
      being argued about. Trained lifters carry roughly 0.65 to 1.0 repetitions
      of absolute error in their repetitions-in-reserve estimates near failure,
      and that accuracy does NOT improve over six weeks of deliberate practice
      (Refalo; Remmert 2023). At about 85% of 1RM, one repetition is worth
      roughly 3-4% of 1RM. So the RIR reading a lifter uses to decide today's
      load carries an error of about 3-4% of the max, while a 2.5 kg jump on a
      100 kg squat is 2.5%. The instrument cannot resolve the decision it is
      being asked to make. This does not make autoregulation useless -- it makes
      it useless as a PRECISION tool for increment sizing, which is exactly what
      it gets recruited for.
    grade: C
  - note: >
      What this item does not do: it does not answer the increment-size
      question. "Autoregulate instead" is the most common way that question gets
      deflected, and the deflection fails twice over -- autoregulated
      prescription shows no measured strength advantage over a percentage
      scheme, and its own resolution is coarser than the steps under discussion.
      The increment-magnitude gap on
      exercise/load-increment-size-evidence-gap-027 stays open.
    grade: C
claim: >
  Autoregulated load prescription -- adjusting today's load by velocity, by RPE,
  by repetitions in reserve, or by an autoregulatory progressive resistance
  scheme -- does not produce better strength gains than a fixed percentage-based
  scheme. Hickmott et al. 2022 (6 studies, n=133 trained) reports a pooled mean
  difference of 2.07 kg, 95% CI -0.32 to 4.46, p=0.09, SMD 0.21, and states
  verbatim that "Autoregulated and standardized load prescription produced
  similar improvements in strength." Liao 2021 (6 studies, n=124) reports squat
  1RM MD 3.03 kg, 95% CI -3.55 to 9.61, p=0.37 -- but shares three of its six
  studies with Hickmott, so the two are partially dependent and amount to less
  than two independent replications. Neither declares an equivalence margin, so
  the finding is an undetected difference in a small pool rather than a
  demonstrated equality. A dissenting 2025 network meta-analysis claiming
  autoregulation is superior is stored as contested: its abstract contradicts
  itself, its rankings come from a SUCRA procedure that orders interventions
  even when every pairwise interval crosses zero, and its study count and sample
  size could not be verified. Separately and more usefully, the autoregulation
  instrument has a resolution limit of its own: trained lifters carry about
  0.65 to 1.0 repetitions of absolute RIR error near failure and do not get
  better at it over six weeks of practice, and at roughly 85% of 1RM one
  repetition is worth about 3-4% of the max -- which is LARGER than the 2.5%
  represented by a 2.5 kg jump on a 100 kg squat. Autoregulation is therefore
  not an answer to the increment-size question; it is a coarser instrument being
  offered in place of one.
reasoning: >
  This item was authored because "just autoregulate" is the standard escape from
  the increment-size gap, and the escape does not hold. Hickmott et al. 2022
  (Sports Med Open 8:9, PMC8762534) pooled six studies of 133 resistance-trained
  participants and found no significant difference between autoregulated and
  standardized prescription; Liao 2021 (PLOS ONE 16(10):e0259790) reached the
  same conclusion in six studies of 124. The temptation is to read that as
  independent replication. It is not: the two reviews share Banyard, Dorrell and
  Orange, three of six studies each, so the second review largely re-analyses
  the first review's participants. The correct summary is one modest,
  partially-replicated null in a small trained pool over short blocks. Neither
  review set an equivalence margin, so, exactly as with Hostler 2001 on the
  increment question, the honest description is an undetected difference rather
  than an established equality -- the confidence intervals still admit several
  kilograms in either direction. The single dissenting synthesis, Huang et al.
  2025 (J Exerc Sci Fit 23(4):360-369, PMID 40791980), is not treated as a
  counterweight because its abstract is internally inconsistent: it denies
  moderate or large effects between interventions while ranking APRE at SUCRA
  93.0%, calls a confidence interval that crosses zero "a moderate effect", and
  asserts significant superiority for comparisons it never reports. Only one
  comparison in that abstract has an interval excluding zero. SUCRA yields a
  full ordering regardless of overlap and is unstable with few studies per node,
  so a 93.0% ranking is a rank statistic, not a demonstrated advantage. The
  second half of the item is the part that actually bears on increments. RIR
  accuracy near failure sits at roughly 0.65-1.0 reps of absolute error in
  trained lifters and does not improve across six weeks of training with
  feedback (Remmert 2023, Percept Mot Skills 130(5):2139-2160; Refalo, J
  Strength Cond Res 38(3):e78-e85). Converting that into load at about 85% of
  1RM, where one rep is worth roughly 3-4% of the max, the instrument's error
  exceeds a 2.5 kg step on a 100 kg squat. That is a resolution argument, not a
  dismissal: autoregulation remains a reasonable way to handle day-to-day
  readiness, but it cannot adjudicate a question finer than its own error bar.
  This mirrors the measurement-side bound on
  exercise/increment-verification-floor-029 from the prescription side.
---

# exercise/autoregulation-vs-percentage-prescription-030

If nobody knows how big a weight jump should be, the natural next thought is to
stop choosing one -- let the day's readiness decide the load. Autoregulation, in
other words: pick the weight by bar speed, by how hard the set felt, by how many
reps you think you had left, or by an autoregulatory progression scheme. It is a
reasonable thought, and it does not survive contact with either the outcome data
or the arithmetic of its own precision.

On outcomes, pooling six studies of 133 trained lifters found autoregulated and
standard percentage-based prescription produced similar strength improvements --
a difference of about two kilos, with a confidence interval that includes zero
and a p-value of 0.09. A second review of six studies and 124 participants found
the same for the squat, a three-kilo difference with a wide interval and no
significance. That looks like two independent confirmations, and it is not: the
two reviews share half their studies with each other. What exists is one modest
null in a small, largely shared pool of trained lifters over short training
blocks. And neither review defined in advance how small a difference would count
as "no difference", so the correct statement is that nobody has detected an
advantage, not that the two methods have been shown to be equal.

There is one prominent dissent, a 2025 network meta-analysis reporting that
autoregulatory, velocity-based and RPE-based methods significantly beat
percentage-based prescription, with the autoregulatory method ranked at 93
percent for the squat and 97 percent for the bench. It is recorded here as
disputed rather than as a counterweight, because its own summary does not hold
together: it says no moderate or large differences were observed between methods
while simultaneously publishing those rankings, it describes a comparison whose
interval crosses zero as showing a moderate effect, and it claims significance
for comparisons it never reports. Only one of its comparisons has an interval
that excludes zero. The ranking statistic it leans on will produce a confident-
looking ordering even when every single comparison is inconclusive, and it is
especially unstable when a network is thin. The study count and total sample
size could not be checked at all.

The more useful finding is about resolution. Ask a trained lifter how many reps
they had left in the tank and they will be off by roughly two-thirds of a rep to
a full rep, and six weeks of doing it every session does not make them better at
it. Near a heavy working load -- around 85 percent of maximum -- one repetition
is worth about three to four percent of that maximum. So the reading being used
to set the load carries an error of three to four percent, while the increment
under debate, two and a half kilos on a hundred-kilo squat, is two and a half
percent. The instrument is coarser than the decision.

None of that makes autoregulation a bad practice. Adjusting load for how the day
is going is sensible, and there is no evidence it costs anything. What it cannot
do is settle how big a jump should be, which is what it is usually recruited to
do. The question the previous item leaves open stays open.
