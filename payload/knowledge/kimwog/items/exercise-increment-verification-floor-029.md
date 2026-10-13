---
# Collection sprint 2026-08-23, third of four items closing the LOAD-INCREMENT
# SIZE / MICROLOADING gap. ROUTING NOTE: this one goes to @clinical-physio
# (VC-A), not @performance-lit, even though its sources are sports-science
# journals. The subject is CLINIMETRIC -- test-retest reliability, standard
# error of measurement, minimal detectable change -- and the verification culture
# that grades measurement-instrument limits is the clinical one. Direct
# precedent inside this warehouse: sleep-recovery/tracker-accuracy-003, an
# instrument-accuracy item that sits in that domain's @clinical lane rather than
# with the substantive claims. Rubric: exercise.rubric.md @clinical-physio.
id: exercise/increment-verification-floor-029
domain: exercise
grade: B (1RM test-retest reliability); C (the derived detectable-change floor and its transfer to working-set loads)
lane: "@clinical-physio"
locale: universal
as_of: 2020-2024
contested: yes
sources:
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7367986/"  # Grgic J et al. 2020, Sports Med Open 6:31 -- 1RM test-retest reliability, 32 studies / n=1595, median ICC 0.97, median CV 4.2%, ICC range 0.64-0.99, CV range 0.5-12.1%
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10933212/"  # Nuzzo JL et al. 2024, Sports Med -- 269 studies / 7,289 individuals; between-individual SD of achievable reps 2.51 at 80% 1RM, 4.36 at 60%; sex, age, training status do not clearly moderate
  - "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11167475/"  # Washif JA et al. 2024, Biol Sport 41(3) -- n=16 male national rugby sevens; published SEM/MDC values that do NOT reproduce from the paper's own ICC and SD (see refraction_notes)
  - "exercise/progression-modality-load-vs-reps-028"  # within-warehouse: the Lasevicius threshold-then-plateau dose-response, the counter that refutes the linear-extrapolation rescue
  - "exercise/load-increment-size-evidence-gap-027"  # within-warehouse: the increment-magnitude gap this floor bounds from the measurement side
  - "sleep-recovery/tracker-accuracy-003"  # within-warehouse, cross-domain: the same posture on a measurement instrument -- what the device can and cannot resolve, kept separate from what is physiologically true
  - "framework:GRADE -- the reliability inputs are a large pooled reliability review (32 studies, n=1595) and a very large rep-prediction synthesis (269 studies, 7,289 individuals), which sit high. The 8-12% floor is DERIVED, not measured: it is the standard MDC95 = 1.96 x sqrt(2) x SEM applied to those inputs by three independent routes that converge. It is graded one rung below its inputs because it is arithmetic on top of them, and because no study has ever reported MDC for a WORKING-SET load."
applicability:
  axes:
    - key: fitness/one_rep_max_kg
      type: numeric
      role: scale
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE CATEGORY DISTINCTION, and it is the conceptual core of this item.
      Measurement error governs whether a change can be VERIFIED from a noisy
      test. It does not govern whether a stimulus was biologically real. "The
      change is smaller than the measurement error, therefore nothing happened"
      is a category error, and it is the most common misuse of an MDC figure.
      A 1 kg increase on a 100 kg lift is unverifiable from a single retest and
      may still be a real change in what the muscle was asked to do. BUT the
      naive rescue in the other direction is equally wrong and is STRIPPED here
      rather than kept as a hedge: "1 kg on 100 kg is a genuine 1% stimulus"
      assumes the stimulus scales linearly with load, and the volume-equated
      dose-response has been measured and is not linear -- doubling relative
      load from 40% to 80% of 1RM changed hypertrophy by about one percentage
      point (Lasevicius 2018, carried on
      exercise/progression-modality-load-vs-reps-028). So the correct position
      is narrow: undetectable does not mean inert, AND no one is entitled to
      claim a proportional stimulus from a proportional load increase.
    grade: C
  - note: >
      BOUNDARY CONDITIONS on the floor. These must travel with the number or it
      will be misapplied. (1) It governs SINGLE-PAIR inference only: one test
      versus one retest. The standard error of a TREND estimated over k sessions
      shrinks roughly as 1 over the square root of k, so a lifter who logs many
      sessions can detect a slope far smaller than any single pair could
      resolve. (2) It applies to change ACCUMULATED BETWEEN TESTS, never to one
      session's increment. Adding 2.5 kg this week is not a claim that needs to
      clear MDC95; the claim that needs to clear it is "my max is higher than it
      was at the last test". (3) It is a floor for VERIFICATION, not a
      recommendation for increment size -- nothing here says jumps should be
      8-12%.
    grade: B
  - note: >
      Washif 2024 is flagged NOT REPRODUCIBLE. The paper (Biol Sport 41(3),
      n=16 male national rugby sevens) publishes bench SEM 1.0 kg / MDC 2.9 kg
      (2.6%) and squat SEM 1.7 kg / MDC 4.8 kg (3.5%) against bench 92 plus or
      minus 14 kg (ICC 0.960, CV 3.2%) and squat 136 plus or minus 21 kg (ICC
      0.957, CV 3.6%). Three arithmetic problems. First, its SEM does not
      reproduce from its own ICC and SD: the textbook SEM = SD x sqrt(1 - ICC)
      gives 2.80 kg for the bench and 4.35 kg for the squat, about 2.7 times
      larger than printed. Second, its SEM as a percentage (about 1.1%) is
      roughly three times SMALLER than its own reported CV of 3.2%, which is
      internally inconsistent. Third, its printed bench MDC percentage is
      arithmetically wrong: 2.9 divided by 92 is 3.2%, not the 2.6% printed.
      The paper's own recomputed values are used in the derivation below; its
      published SEM and MDC are not. This is why the item carries the contested
      flag.
    grade: C
  - note: >
      Percentage-of-1RM framing is NOT automatically the correct framing. Nuzzo
      et al. 2024 (269 studies, 7,289 individuals) reports the between-individual
      standard deviation of achievable repetitions as 2.51 reps at 80% of 1RM
      and 4.36 reps at 60%, and finds that sex, age and training status do not
      clearly moderate the reps-versus-percentage relationship. So prescribing
      by percentage is itself an instrument with a spread of roughly plus or
      minus 2.5 reps at heavy loads. The common assumption that absolute
      kilograms are crude while percentages are principled does not survive
      that: both framings carry error, in different currencies. There is also
      no head-to-head trial of absolute versus relative increment framing -- the
      comparison has never been run.
    grade: B
  - note: >
      All the reliability evidence is LABORATORY 1RM testing. MDC and SEM for
      WORKING-SET loads -- the loads a lifter actually manipulates week to week
      -- are thin to absent. Treat any transfer of these figures from a formal
      1RM test to a working set as an extrapolation, and note that the direction
      of the transfer error is unknown: a working set is submaximal and more
      repeatable in some respects, but is performed fatigued, unstandardized and
      without the test-day protocol control the reliability studies imposed.
    grade: D
  - note: >
      Spread matters more than the median here. Grgic's median ICC of 0.97 and
      median CV of 4.2% sit inside an ICC range of 0.64 to 0.99 and a CV range
      of 0.5 to 12.1%. The floor derived below uses the median; a lifter, lift,
      or testing protocol from the bad end of that range has a substantially
      worse floor, and an untrained or novel lift is exactly where the bad end
      lives. Do not speak the 8-12% band as though it were tight.
    grade: B
claim: >
  For ONE trained lifter, a single 1RM test compared against a single retest
  under a standardized protocol, the minimal detectable change at 95%
  confidence is roughly 8-12% of the 1RM (roughly 7-10% at 90% confidence).
  Three independent routes converge on that band. Route one: applying
  MDC95 = 1.96 x sqrt(2) x SEM = 2.772 x SEM to the pooled median coefficient
  of variation from Grgic 2020 (4.2%, from 32 studies and 1,595 participants,
  median ICC 0.97) gives 2.772 x 4.2% = 11.6%. Route two: recomputing a
  published cohort the textbook way -- Washif 2024, bench 92 plus or minus
  14 kg with ICC 0.960, squat 136 plus or minus 21 kg with ICC 0.957 -- gives
  SEM = SD x sqrt(1 - ICC) of 14 x sqrt(0.040) = 2.80 kg for the bench, hence
  MDC95 = 7.8 kg = 8.4% of 92 kg, and 21 x sqrt(0.043) = 4.35 kg for the squat,
  hence 12.1 kg = 8.9% of 136 kg. Route three: 2.772 x that same paper's
  reported CV of 3.2% = 8.9%. The practical consequence: a 2.5 kg step on a
  60 kg bench press is 4.17%, which sits BELOW this floor -- it cannot be
  confirmed from a single retest. The consequence that does NOT follow, and
  which the item exists to block, is that such a step is therefore
  physiologically inert. Measurement error governs verifiability, not biology.
  Equally, the reflexive rescue -- "1 kg on 100 kg is a real 1% stimulus" -- is
  unsupported linear extrapolation and is refuted by the measured
  threshold-then-plateau load dose-response.
reasoning: >
  The inputs are strong and the derivation is deliberately shown so it can be
  audited rather than trusted. Grgic et al. 2020 (Sports Med Open 6:31,
  PMC7367986) pooled 32 studies and 1,595 participants and reported a median
  1RM test-retest ICC of 0.97 and a median CV of 4.2%, with ranges of 0.64-0.99
  and 0.5-12.1% respectively. Minimal detectable change at 95% confidence is
  the standard clinimetric quantity MDC95 = 1.96 x sqrt(2) x SEM, the sqrt(2)
  arising because two independent measurements each carry the error. Treating
  the CV as a proportional SEM gives 11.6% of 1RM. An independent route uses a
  published cohort: Washif et al. 2024 reports bench 92 plus or minus 14 kg
  (ICC 0.960) and squat 136 plus or minus 21 kg (ICC 0.957), and the textbook
  SEM = SD x sqrt(1 - ICC) yields 2.80 kg and 4.35 kg, hence MDC95 of 7.8 kg
  (8.4%) and 12.1 kg (8.9%). A third route applies the 2.772 multiplier to that
  paper's own CV of 3.2% and lands at 8.9%. Three routes, two datasets, one
  band: about 8-12%. Note that the same paper's PUBLISHED SEM and MDC values
  are roughly 2.7 times smaller than its own ICC and SD imply and are
  internally inconsistent with its own CV, which is recorded as a defect on the
  paper rather than as a competing estimate (see refraction_notes) and is the
  reason for the contested flag. The interpretive half of the item matters more
  than the number. An MDC is a statement about what a noisy instrument can
  resolve from two readings; it says nothing about whether a stimulus occurred.
  Sliding from "undetectable" to "inert" is a category error. But the usual
  counter-move -- rescuing small increments by asserting that a 1% load increase
  is a 1% stimulus increase -- assumes a linear dose-response that has been
  measured and is not linear (Lasevicius 2018: doubling relative load from 40%
  to 80% of 1RM moved hypertrophy by about one percentage point). Both moves
  are blocked, and what is left is a narrow, defensible position. Finally,
  Nuzzo et al. 2024 (269 studies, 7,289 individuals, PMC10933212) shows that
  the percentage framing people reach for as the "correct" alternative to
  kilograms is itself an instrument with a spread of about plus or minus 2.5
  reps at 80% of 1RM, unmoderated by sex, age or training status. Neither
  framing is precise; they are imprecise in different units, and no trial has
  ever compared them head to head.
---

# exercise/increment-verification-floor-029

There is a hard limit on what a strength test can tell you, and most training
increments sit under it.

Pooled across 32 reliability studies and about 1,600 participants, a one-rep max
test repeated under standardized conditions has a typical variation of around
4.2 percent, with excellent agreement overall (a median reliability coefficient
of 0.97) but a wide spread across studies. To turn that into a threshold for
"did this person actually get stronger", the standard measurement-science step
is to multiply the measurement error by 1.96 and by the square root of two --
the square root of two because you are comparing two measurements, each carrying
its own error. That multiplier is about 2.77, and 2.77 times 4.2 percent is
11.6 percent.

A second route, using a published cohort of sixteen national rugby sevens
players, gets to the same place. Their bench press averaged 92 kg with a
standard deviation of 14 kg and a reliability coefficient of 0.960. The textbook
standard error of measurement is the standard deviation times the square root of
one minus the reliability: 14 times the square root of 0.040, which is 2.80 kg.
Multiply by 2.77 and the detectable change is 7.8 kg, which is 8.4 percent of
92 kg. The squat in the same group: 21 times the square root of 0.043 is 4.35 kg,
so 12.1 kg, which is 8.9 percent of 136 kg. A third route, applying the same
multiplier to that group's own 3.2 percent variation, gives 8.9 percent.

Three routes, two datasets, one answer: for a single lifter, comparing one test
to one retest, you need something like 8 to 12 percent before you can say the
number moved rather than wobbled. At the more forgiving 90 percent confidence
level it is roughly 7 to 10 percent.

Now the arithmetic that makes this concrete. Two and a half kilos on a 60 kg
bench press is 4.17 percent. That is comfortably below the floor. If you test,
add 2.5 kg over some weeks, and test again, the second number cannot tell you
whether you improved.

That is where almost everyone draws the wrong conclusion, in one of two
directions.

The wrong conclusion in the first direction is that a change too small to detect
is therefore a change that did not happen. That is a confusion between an
instrument and a body. The measurement floor describes what a noisy test can
resolve from two readings. It has nothing to say about whether the muscle
experienced anything. A jump that is invisible to a retest can still be a real
change in what was demanded.

The wrong conclusion in the second direction is the reflexive rescue: "fine, but
one kilo on a hundred is still one percent more stimulus." That assumes stimulus
tracks load proportionally, and that assumption has been tested. With total
volume held equal, quadriceps growth was essentially flat from 40 to 80 percent
of maximum -- doubling the relative load moved growth by about a percentage
point. The dose-response has a threshold and then a plateau. Nobody is entitled
to convert a one percent load increase into a one percent anything.

Three boundary conditions keep the floor from being misused. It applies to a
single test-retest pair; a trend estimated across many logged sessions has a
much smaller standard error, shrinking roughly with the square root of the
number of sessions, so a well-kept training log can see things a pair of tests
cannot. It applies to change accumulated between tests, never to a single
session's increment -- adding weight this week is not a claim that has to clear
a statistical threshold. And it is a floor for verification, not advice about
increment size; nothing here suggests jumps ought to be 8 to 12 percent.

Two further honesty notes. First, the percentage-of-maximum framing that people
reach for as the more principled alternative to kilograms is itself blunt: across
269 studies and over seven thousand people, how many reps someone can do at
80 percent of their maximum varies with a standard deviation of about two and a
half reps, and at 60 percent about four and a third, with sex, age and training
status failing to explain it. Percentages are not the correct framing; they are
a different imprecise framing, and no study has ever put the two head to head.
Second, every reliability figure quoted here comes from formal laboratory max
testing. What the error looks like on an ordinary working set, performed tired
and unstandardized, has not been measured at all.
