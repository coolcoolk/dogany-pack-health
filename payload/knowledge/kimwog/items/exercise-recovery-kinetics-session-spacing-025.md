---
# Collection sprint 2026-08-22. Fills GAPS gap-areas 6 and 7 (recovery timelines
# per muscle group + recovery-rate modifiers; session sequencing / muscle
# recovery between training days). This is the WEAKEST of the six items authored
# in this sprint and is graded accordingly -- the headline finding is largely
# NEGATIVE: the per-muscle-group recovery tables in circulation have no
# controlled evidence base. Rubric: exercise.rubric.md @performance-lit.
id: exercise/recovery-kinetics-session-spacing-025
domain: exercise
grade: C (proximity-to-failure / volume / movement-complexity as the real drivers); D (anything stated per muscle group)
lane: "@performance-lit"
locale: universal
as_of: 2017-2023
contested: yes
sources:
  - "https://link.springer.com/article/10.1007/s00421-017-3725-7"  # Pareja-Blanco et al. 2017, Eur J Appl Physiol 117(12):2387-2399, recovery following training leading or not to failure
  - "https://pubmed.ncbi.nlm.nih.gov/30036284/"  # Pareja-Blanco et al. 2018, J Strength Cond Res, time course of recovery with different set configurations
  - "https://pmc.ncbi.nlm.nih.gov/articles/PMC10286608/"  # Dourado/Vieira/Boullosa/Bottaro 2023, Biol Sport 40(3):767-774, single- vs multi-joint recovery, n=14 untrained males
  - "exercise/rest-interval-volume-load-017"  # within-warehouse cross-ref: same volume-load-is-the-mechanism logic one timescale down (between sets rather than between sessions), and the same isolation/untrained generalizability limit
  - "exercise/doms-timeline-mechanism-023"  # within-warehouse cross-ref: why soreness must NOT be used as the spacing signal
  - "framework:GRADE -- there is NO systematic review or meta-analysis of recovery kinetics COMPARED ACROSS MUSCLE GROUPS under matched conditions. The direct measurements available are single small trials in untrained or moderately trained men, on the quadriceps and on elbow flexors. The failure/volume direction has RCT-level support; every per-muscle-group statement is coaching convention with no controlled backing and is graded as such."
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
      The "each muscle group needs 48-72 hours" rule has NO controlled evidence
      base. It is a coaching convention. No study located in this sprint
      systematically compares recovery kinetics ACROSS muscle groups under
      matched volume, intensity and proximity to failure. Published
      per-muscle-group recovery tables (chest 48 h, back 72 h, arms 24 h, and
      similar) are practitioner constructions, not measurements. Treat any
      such number as a scheduling convenience, never as a physiological fact.
    grade: D
  - note: >
      REJECTED during verification and recorded so it is not re-adopted:
      "large muscle groups recover more slowly than small ones." The one
      direct measurement available contrasts single-joint versus multi-JOINT
      work within the SAME muscle group (quadriceps), and the structure that
      recovered slowest was the bi-articular rectus femoris -- a
      joint-involvement and muscle-lengthening story, not a muscle-size story.
      Size-based recovery ordering was not supported by anything found and is
      not carried in the claim.
    grade: D
  - note: >
      REJECTED during verification: "upper body recovers faster than lower
      body." Widely repeated, and no matched head-to-head comparison was
      located to support it. Secondary sources asserting it also concede that
      upper-body muscles are trained indirectly far more often, which is a
      confound large enough to explain the belief on its own. Not carried.
    grade: D
  - note: >
      Generalizability limit on the one direct measurement. Dourado 2023 is
      n=14 UNTRAINED young males, quadriceps only, one session, with the
      authors themselves noting they collected no soreness and no EMG data to
      explain why functional recovery and swelling recovery dissociated.
      Reading its 24 h versus 48 h split across to a trained lifter doing
      heavy multi-set barbell work is an extrapolation, not a finding. This is
      the same shape of limit already carried on
      exercise/rest-interval-volume-load-017.
    grade: C
  - note: >
      What to steer off instead. Because soreness does not track recovery
      state (see exercise/doms-timeline-mechanism-023), the usable proxies are
      performance-based: load and rep performance on the first working set,
      bar speed, and jump height are what the recovery trials actually
      measured and found depressed. Whether these are practical as day-to-day
      autoregulation signals for a general trainee was not evaluated in this
      sprint.
    grade: D
claim: >
  Recovery of neuromuscular performance after resistance training is driven
  mainly by PROXIMITY TO FAILURE, by the number of repetitions accumulated in
  the fatiguing sets, and by the movement's complexity -- NOT by a fixed
  per-muscle-group clock. Sets carried to failure, especially with a high
  repetition count, leave mechanical muscle function depressed as far out as
  48 h, while volume-matched work stopped short of failure recovers markedly
  faster. Movement complexity matters independently: in a direct within-subject
  comparison, single-joint knee extension recovered peak torque by 24 h while
  multi-joint leg press took 48 h, and the bi-articular rectus femoris showed
  the longest swelling resolution of all. Everything commonly asserted at the
  PER-MUSCLE-GROUP level -- "48-72 h per muscle group," per-muscle recovery
  tables, "big muscles need longer," "upper body recovers faster than lower" --
  is coaching convention with no controlled comparison behind it, and this item
  explicitly declines to endorse it. Practical direction for spacing sessions:
  spacing is set by how close to failure the work was, how much of it there was,
  and whether the same movement pattern recurs -- not by which muscle was
  trained. Do not use soreness as the spacing signal (see item 023); the
  measured recovery variable in these trials is performance, not sensation.
reasoning: >
  Pareja-Blanco et al. 2017 (Eur J Appl Physiol 117(12):2387-2399) tracked
  countermovement jump height, velocity against a fixed load, and a hormonal and
  creatine-kinase panel from 24 h pre-exercise to 48 h post across protocols that
  did or did not reach failure. Protocols to failure -- particularly those with a
  high number of repetitions performed -- produced the largest reductions in
  mechanical muscle function and remained depressed at 48 h, with greater
  hormonal response and greater muscle damage; non-failure work recovered
  substantially faster. The companion 2018 set-configuration study (J Strength
  Cond Res, PMID 30036284) reproduces the same dependence on how the sets are
  arranged rather than on which muscle was worked. Dourado et al. 2023 (Biol
  Sport 40(3):767-774) supplies the movement-complexity dimension in a
  within-participant unilateral and contralateral design (n=14 untrained young
  males): knee-extension peak torque and jump height were back to baseline by
  24 h, leg press took 48 h for both, and while vastus lateralis swelling
  resolved by 24 h after leg press, rectus femoris swelling was still elevated
  out to 96 h -- attributed to its bi-articular nature and to lengthening during
  the hip-extension phase. Note carefully what that study does NOT show: it
  compares exercises within one muscle group, so it cannot support any claim
  about one muscle group recovering faster than another. That absence is the
  central honest finding of this item. No systematic review or meta-analysis
  comparing recovery kinetics across muscle groups under matched conditions was
  located in this sprint, and the per-muscle-group tables in wide circulation
  trace to practitioner sources, not measurements. The mechanism logic parallels
  exercise/rest-interval-volume-load-017 one timescale up: as with inter-set
  rest, the apparent variable (time, muscle group) is not the operative one --
  the operative one is how much fatiguing work was accumulated and how it was
  arranged. Contested flag is set because the per-muscle-group recovery model is
  near-universal in coaching practice and is not supported here.
---

# exercise/recovery-kinetics-session-spacing-025

The common mental model is that each muscle group has a recovery clock -- chest
so many hours, back so many more -- and you space sessions by reading that
clock. There is no controlled evidence for that model, and the evidence that
does exist points somewhere else entirely.

What has actually been measured is that recovery tracks how the work was done.
Sets taken to failure, especially sets where a lot of reps were accumulated
before failure, leave measurable performance depressed as far out as 48 hours,
along with larger hormonal and muscle-damage responses. Volume-matched work
stopped short of failure comes back much faster. That difference is large and
it is the reliable one.

Movement complexity is the second lever. In a within-subject comparison, single
joint knee extension had recovered its peak torque and jump height by 24 hours;
multi-joint leg press needed 48 for both. Interestingly, swelling in the
vastus lateralis had cleared 24 hours after the leg press, while the rectus
femoris -- which crosses two joints and gets lengthened during hip extension --
was still swollen at 96 hours. So even within one muscle group, different
structures ran on different clocks depending on how the movement loaded them.

That last detail is exactly why the muscle-group model fails. The study
compares exercises inside a single muscle group. It cannot tell you anything
about chest versus back. And no study was found that does -- no systematic
comparison of recovery kinetics across muscle groups under matched volume,
intensity and proximity to failure exists. The recovery tables that circulate,
and the "48 to 72 hours per muscle group" rule, are scheduling conventions
someone wrote down. They may be perfectly serviceable as conventions. They are
not measurements, and they should not be quoted as if they were.

Two beliefs specifically did not survive checking and are recorded here so they
do not creep back in: that bigger muscles need longer (the slowest-recovering
structure in the one direct measurement was a small bi-articular muscle, and
the pattern was about joint involvement, not size), and that upper body recovers
faster than lower body (no matched comparison found; upper-body muscles also
get far more indirect work, which would produce the same impression without any
underlying difference in recovery rate).

Honest limits. The direct recovery-timing measurement is 14 untrained young men,
quadriceps only, one session, with the authors noting they collected neither
soreness nor EMG data to explain why functional recovery and swelling recovery
came apart. Reading it across to a trained lifter under heavy multi-set barbell
work is an extrapolation. And whatever you space sessions by, it should not be
soreness -- soreness has been directly measured not to track the state you are
trying to manage.

## Applicability check (2026-08-22) -- NOT adopted, implication only

Checked against `files/program/program.yaml`. **Nothing changed, nothing
proposed.**

Current state: `rotation: [앞A, 뒷A, 앞B, 뒷B]`. 앞A is chest plus quad
(incline dumbbell press, V-squat), 뒷A is back plus deadlift, 앞B is shoulder
plus quad (overhead press, back squat, incline barbell press), 뒷B is back
thickness plus hamstring and glute (pendlay row, RDL, Bulgarian split squat).
So quad-dominant work recurs on 앞A and 앞B with one session between them, and
back work recurs on 뒷A and 뒷B the same way.

What this item would imply:

1. The rotation should be defended -- or revised -- on movement-pattern and
   proximity-to-failure grounds, not on a muscle-group recovery clock. The
   relevant question is not "have his quads had 48 hours" but "how close to
   failure was the squat work, how many reps were accumulated, and does the
   next session repeat the same movement pattern."
2. The specific spacing risk the evidence identifies is the multi-joint,
   through-a-lengthened-range case: leg press took 48 hours where knee extension
   took 24, and the bi-articular rectus femoris was still swollen at 96. In his
   rotation the analogue is RDL on 뒷B into squat work on 앞A -- hinge loading of
   the hamstrings and hip extensors landing ahead of knee-dominant work. Whether
   that ordering matters at his volumes is not answerable from this evidence; it
   is the thing to watch, not a defect to fix.
3. What the item explicitly does NOT license: reshuffling the split on the
   grounds that some muscle group "needs longer." There is no controlled
   evidence for per-muscle-group recovery ordering at all.
4. If a readiness signal is ever wanted, the trials measured first-set load and
   rep performance, bar speed, and jump height. Whether any of those is workable
   as day-to-day autoregulation for him is untested and would be a design
   decision, not a finding.
