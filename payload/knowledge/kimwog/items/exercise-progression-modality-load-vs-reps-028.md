---
# Collection sprint 2026-08-23, second of four items closing the LOAD-INCREMENT
# SIZE / MICROLOADING gap. Separated from exercise/load-increment-size-evidence-
# gap-027 on purpose: the two trials most often recruited to answer "how big a
# jump" actually answer a DIFFERENT question (which VARIABLE to progress), and
# collapsing them into the increment item would let the answer path speak them
# as increment evidence. Rubric: exercise.rubric.md @performance-lit.
id: exercise/progression-modality-load-vs-reps-028
domain: exercise
grade: B (hypertrophy equivalence inside the tested envelope); C (strength transfer and any extension beyond it)
lane: "@performance-lit"
locale: universal
as_of: 2017-2024
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/36199287/"  # Plotkin DL et al. 2022, PeerJ 10:e14142, doi 10.7717/peerj.14142 -- 43 randomized / 38 analyzed, trained 1yr+, 8 wk, load vs rep progression
  - "https://www.thieme-connect.de/products/ejournals/abstract/10.1055/a-2256-5857"  # Chaves TS et al. 2024, Int J Sports Med 45:504-510, doi 10.1055/a-2256-5857 -- n=39 untrained, 10 wk, within-subject contralateral-leg design
  - "https://pubmed.ncbi.nlm.nih.gov/28834797/"  # Schoenfeld BJ et al., low- vs high-load meta-analysis -- hypertrophy similar across the loading spectrum, 1RM strength significantly favours high load
  - "https://pubmed.ncbi.nlm.nih.gov/29564973/"  # Lasevicius T et al. 2018, Eur J Sport Sci 18(6) -- volume-equated within-subject n=30 at 20/40/60/80% 1RM; the threshold-then-plateau dose-response
  - "exercise/load-increment-size-evidence-gap-027"  # within-warehouse: neither trial here specifies an increment size, so neither can answer the magnitude question
  - "exercise/volume-doseresponse-007"  # within-warehouse: the volume dose-response this sits alongside
  - "framework:GRADE -- two randomized trials in different populations (trained and untrained) with a within-subject contralateral replication converge on no modality difference, which supports the equivalence direction at RCT level for HYPERTROPHY. Everything beyond that is downgraded: the trials are 8-10 weeks, the strength half is contradicted by a larger loading-spectrum meta-analysis, and the tested rep envelope is bounded by what the participants happened to drift to."
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
      The tested envelope is narrow and is defined by drift, not by design. In
      Plotkin 2022 the repetition-progression group held its LOAD CONSTANT for
      the full eight weeks and, starting from an 8-12 rep target, drifted up to
      24.1 plus or minus 7.3 reps by the end -- roughly twice the target. That
      is the envelope in which equivalence was observed: adding reps works up
      to about double the rep target, over about two months, with load frozen.
      It is not evidence that reps can be added indefinitely, and it is not
      evidence about a lifter who adds reps for a year. Read the result as
      bounded by that drift.
    grade: B
  - note: >
      A null with a null-biasing confound is weaker than a clean null. The
      Plotkin authors themselves flag it: 1RM was tested on a SMITH MACHINE
      while training used the free-weight back squat. A test that is mechanically
      unlike the trained movement compresses the differences it can detect, which
      biases the comparison toward finding nothing. The direction of the bias is
      the direction of the reported result, so the equivalence finding should not
      be treated as though the design were neutral. Chaves 2024 partially
      compensates -- different population, within-subject contralateral-leg
      design, leg extension tested as trained -- which is why the two together
      support more than either alone.
    grade: C
  - note: >
      The equivalence is a HYPERTROPHY equivalence. It survives into maximal
      strength only inside the moderate-load zone. Schoenfeld's low- vs
      high-load meta-analysis (PMID 28834797) finds hypertrophy similar across
      the loading spectrum but 1RM strength gains significantly favouring high
      load. So "swap the progression variable freely" is defensible for growth
      and is NOT defensible as a general statement for a lifter chasing a
      one-rep max: past a point, adding reps at a fixed load moves the training
      away from the loads that build maximal strength. Plotkin's and Chaves'
      rep groups stayed inside moderate loads, which is why their strength
      results do not contradict the meta.
    grade: B
  - note: >
      The load dose-response is threshold-then-plateau, not linear -- and this
      is the counter that kills the "1% more load is 1% more stimulus" rescue.
      Lasevicius 2018 (volume-equated, within-subject, n=30) measured vastus
      lateralis CSA at 20/40/60/80% of 1RM: plus 8.9, 20.5, 20.4 and 19.5%
      respectively, and elbow flexors plus 11.4, 25.3, 25.1 and 25.0%. DOUBLING
      the relative load from 40% to 80% changed hypertrophy by roughly one
      percentage point. Above a threshold the curve is flat for growth. Strength
      is more load-sensitive than cross-sectional area (60 and 80% beat 20 and
      40%), so the plateau is flatter for hypertrophy than for strength.
      Anything that assumes proportionality between a small load increase and a
      proportional increase in stimulus is extrapolating along a curve that has
      been measured and is not a straight line.
    grade: B
  - note: >
      Neither trial specifies the INCREMENT it used. Plotkin's load-progression
      group progressed load; the paper never states by how much. Chaves is the
      same. That is exactly why these trials are separated from
      exercise/load-increment-size-evidence-gap-027 -- they are frequently cited
      into increment arguments where they carry no information at all. Citing
      them for a jump size is a source-substitution error.
    grade: C
  - note: >
      Duration and population bounds. Plotkin is 8 weeks in trained lifters
      (1 year or more), 43 randomized and 38 analyzed; Chaves is 10 weeks in 39
      untrained participants. Both are short relative to how long anyone
      actually trains, and neither followed participants long enough to observe
      whether a rep-only progression eventually stalls where a load progression
      would not. The authors of Plotkin describe the between-group differences
      as "of questionable practical significance", which is the correct register
      to speak this in -- similar outcomes over a short block, not proven
      interchangeability over a training career.
    grade: C
claim: >
  Over a training block of roughly two months, progressing by ADDING LOAD and
  progressing by ADDING REPS at a fixed load produce similar muscle growth and
  similar strength gains. Plotkin 2022 (43 randomized, 38 analyzed, trained at
  least one year, 8 weeks) found squat 1RM up 21.8 kg with load progression
  versus 19.3 kg with rep progression, a difference the authors called "of
  questionable practical significance"; Chaves 2024 (n=39 untrained, 10 weeks,
  within-subject contralateral-leg design) found no difference between the two
  in either 1RM or vastus lateralis cross-sectional area. Three bounds are part
  of the claim, not caveats to it. First, the tested envelope: the rep group in
  Plotkin held load constant for eight weeks and drifted from an 8-12 rep target
  up to 24.1 plus or minus 7.3 reps, so equivalence is demonstrated to about
  twice the rep target and no further. Second, the equivalence is a HYPERTROPHY
  equivalence; a low- versus high-load meta-analysis finds growth similar across
  the loading spectrum but 1RM strength significantly favouring high load, so
  the swap is safe for growth and only holds for maximal strength while the
  loads stay moderate. Third, the underlying load dose-response is
  threshold-then-plateau rather than linear: doubling relative load from 40% to
  80% of 1RM changed hypertrophy by about one percentage point. Neither trial
  states the size of the increment it used, so neither answers how big a jump
  should be.
reasoning: >
  The modality question is far better evidenced than the magnitude question, and
  keeping them apart is the point of this item. Plotkin et al. 2022 (PeerJ
  10:e14142) randomized trained lifters to progress load within an 8-12 rep
  range or to hold load and add reps, over 8 weeks; hypertrophy and strength
  outcomes were similar, with the authors explicitly declining to call the
  differences practically meaningful. Chaves et al. 2024 (Int J Sports Med
  45:504-510) replicates the direction in a different population and a stronger
  design -- untrained participants, one leg per condition, 10 weeks -- with 1RM
  and vastus lateralis CSA both non-significant between conditions. Two trials
  in opposite training-status populations, one of them within-subject, is a
  reasonable basis for the direction. The bounds are where the honest work is.
  Plotkin's own flagged confound (1RM tested on a Smith machine while training
  used the free-weight back squat) pushes toward the null it reports, so the
  equivalence should not be read as a clean null. The rep group's drift to 24.1
  reps defines the envelope empirically rather than by protocol. And the
  strength half is bounded from outside by Schoenfeld's low- vs high-load
  meta-analysis (PMID 28834797), which finds hypertrophy similar across the
  loading spectrum but 1RM significantly better with high load -- so the
  equivalence must be spoken as hypertrophy-first. Lasevicius 2018 (Eur J Sport
  Sci 18(6), PMID 29564973, volume-equated, within-subject, n=30) supplies the
  shape of the underlying dose-response: 20% of 1RM is clearly inferior, but 40,
  60 and 80% are within about a percentage point of each other for CSA in both
  the vastus lateralis and the elbow flexors, while strength discriminates more
  sharply between them. That is a threshold with a plateau, which is why any
  reasoning that treats a small load increase as a proportionally small stimulus
  increase is unsupported (see the counter recorded on
  exercise/increment-verification-floor-029).
---

# exercise/progression-modality-load-vs-reps-028

Adding weight and adding reps are, over a couple of months, interchangeable ways
to make training harder. Two trials say so from opposite directions. In trained
lifters over eight weeks, a group that added load inside an eight-to-twelve rep
range gained 21.8 kg on their squat max while a group that kept the same weight
and added reps gained 19.3 kg -- a gap the authors themselves declined to call
practically meaningful. In untrained participants over ten weeks, with each
person running one protocol on each leg, leg-extension max and quadriceps
cross-sectional area came out statistically indistinguishable between the two.

Three limits belong to that result rather than sitting beside it.

The first is how far the rep side was actually tested. The rep-progression group
kept the same weight on the bar for eight full weeks and ended up doing 24 reps
per set, give or take seven, having started at a target of eight to twelve. So
what was demonstrated is that you can roughly double your rep target at a fixed
load and end up in about the same place. Nothing in the data speaks to adding
reps beyond that, and nothing speaks to doing it for a year.

The second is which outcome the equivalence belongs to. It is a muscle-growth
result. When the wider literature on light versus heavy loading is pooled, growth
comes out similar across a broad range of loads, but maximal strength clearly
favours heavier work. Both trials here kept their rep groups in moderate loads,
so their strength results are not in conflict with that -- but a lifter whose
goal is a one-rep max cannot extend "reps and load are interchangeable"
indefinitely, because far enough down the rep road the training is no longer
heavy.

The third is the shape of the curve underneath all of this, and it is the most
useful thing in the item. When load was varied deliberately with total volume
held equal, quadriceps growth ran plus 8.9 percent at 20 percent of maximum,
then 20.5, 20.4 and 19.5 percent at 40, 60 and 80 percent. The elbow flexors did
the same thing: 11.4, then 25.3, 25.1, 25.0. Doubling the relative load from 40
to 80 percent moved growth by about one percentage point. There is a threshold,
and above it the curve is flat. Strength discriminated more sharply than size
did, which is consistent with the second limit above.

One thing these trials cannot do, and are constantly asked to do: they do not
say how big a jump should be. Both of them progressed load without ever
reporting by how much. When someone cites them in an argument about two-and-a-
half versus five kilos, they are citing a study that did not measure the thing
being argued about.
