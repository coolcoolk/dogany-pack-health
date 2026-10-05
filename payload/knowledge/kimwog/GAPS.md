# Kimwog gap list -- what the next collection sprint should fetch

Output of DGN-173 (seed conversion). This lists claims dropped for quality,
coverage areas the rubrics name but the current raws do not cover, and rows that
need a re-run. It is NOT a to-do inside DGN-173 (no new research this ticket) --
it is the queue for a future collection sprint.

Author: seed-conversion pass, 2026-07-06. Scope: exercise / nutrition /
sleep-recovery only (the kimwog bundle). Sources: batch1, batch2 (sleep rows).

## exercise

Dropped for quality / not sourced:
- @gym-craft lane (exercise/dc-inversion-craft-007 in the rubric) is EMPTY of
  shippable items. The rubric's single @gym-craft row is a STRUCTURAL inversion
  RULE (D may outrank a confounded observational C for training-craft), explicitly
  marked "[unconfirmed -- no single primary claim row]" in the rubric. It has no
  sourced 3-vote survivor behind it, so it was NOT converted into an item. The
  gym-craft lane therefore ships with zero items in warehouse #1.
  -> A collection sprint should fetch real, sourced training-craft claims
     (split/tempo/volume/frequency programming consensus from coaching literature
     + hypertrophy meta-analyses) so the D/C-inversion lane has substantive items,
     not just a grading rule.
  PARTIALLY FILLED 2026-08-17 / 2026-08-21 (bookkeeping correction 2026-08-22 --
  the paragraph above still read "zero items" long after it stopped being true):
  @gym-craft now holds exercise/volume-landmarks-heuristic-015,
  exercise/deficit-volume-guidance-016, exercise/warmup-load-rampup-progression-018,
  exercise/serratus-anterior-integration-019 and
  exercise/female-training-considerations-020. STILL OPEN: all five are
  theory-only or single-source practitioner digests. The lane still has no item
  that demonstrates the D-over-confounded-C INVERSION doing actual work, which
  was the original point of the gap.

Coverage the rubric implies but batch1 does not supply:
- No substantive @clinical-physio items beyond creatine + protein-window + BCAA +
  the COI rule. Missing high-value ergogenics the AIS framework grades Group A:
  caffeine, beta-alanine, sodium bicarbonate, nitrate/beetroot. These are named
  by the anchored AIS framework but were not in the batch1 findings.
- No @performance-lit substantive training claims -- only the two field-methodology
  rules (replication crisis, small-n culture). The lane needs actual performance
  findings (e.g. training-volume/-frequency dose-response) graded THROUGH those
  rules to show the lane doing work, not just describing its own hazards.
- REP-RANGE vs TECHNICAL-STABILITY/INJURY-RISK for heavy multi-joint free-weight
  compounds (squat/deadlift/RDL-class hinge, barbell row/press) was an UNLOGGED
  coverage hole -- flagged 2026-08-07 mid-session (사용자 asked whether "heavy
  compound multi-joint lifts -> low reps because synergist/stabilizer fatigue +
  neural-control loss raises injury risk" is graded knowledge). No item or raw
  covers this; closest adjacent item is exercise/rest-interval-volume-load-017
  (rest, not rep-count), which itself flags compound extrapolation as unverified.
  Answer given in-session was own-rule/conventional-coaching-heuristic, explicitly
  NOT presented as warehouse-graded. -> A collection sprint should fetch sourced
  claims on rep-range selection, technical breakdown risk, and injury incidence
  by rep-range for trained lifters on heavy compound multi-joint lifts.

Rerun-needed: none in exercise (batch1 verified cleanly, 3-0 across the rows used).

Filled 2026-08-23 (load-increment size / microloading collection sprint, v9):
- LOAD-INCREMENT SIZE / MICROLOADING (2.5 vs 5 kg jumps, minimum effective load
  increment, absolute-vs-relative load jump) had NO item at any grade. Queued
  here 2026-08-23 by the weekly kimwog-gap cron after sitting instance-side for
  23 days; the BLOCKED-ON owner-go condition on that queued entry was satisfied
  by an explicit owner trigger (the cron notice alone was correctly not treated
  as one). Filled by a sprint of 2 research passes + 3 adversarial verification
  passes into four items. The headline is an ABSENCE: nobody has studied how big
  an increment should be.
  - exercise/load-increment-size-evidence-gap-027 (@performance-lit, B/D,
    contested) -- the documented absence and its provenance trace. ACSM 2009's
    2-10% rule carries exactly one citation and that citation is a narrative
    prescription review, not an experiment; ACSM 2026 is silent (recorded as an
    argument from silence, NOT a repudiation); Hostler 2001 (n=19, untrained,
    upper-body) is the only trial ever to manipulate increment magnitude, and
    it is an unrejected null, not demonstrated equivalence.
  - exercise/progression-modality-load-vs-reps-028 (@performance-lit, B/C,
    not contested) -- load-vs-rep progression equivalence (Plotkin 2022, Chaves
    2024) with its three bounds: the tested envelope is ~2x the rep target over
    8 weeks, the equivalence is HYPERTROPHY-only (strength favours high load),
    and the load dose-response is threshold-then-plateau, not linear.
  - exercise/increment-verification-floor-029 (@clinical-physio, B/C,
    contested) -- MDC95 ~8-12% of 1RM for a single test-retest pair, derived
    three ways and shown; plus the category distinction (undetectable is not
    inert) with the linear-extrapolation rescue stripped.
  - exercise/autoregulation-vs-percentage-prescription-030 (@performance-lit,
    B/C, contested) -- the standard escape from the increment question, which
    fails twice: no measured advantage over percentage-based prescription, and
    an instrument error (RIR ~0.65-1.0 reps, ~3-4% of 1RM near 85%) larger than
    the increments under dispute.
  ROUTING NOTE: all four to EXERCISE. Three to @performance-lit, whose two
  methodology rules (replication-power-crisis-005, small-n-culture-006) are
  exactly what position-stand prescription and small-pool meta-analysis need to
  be graded through. Item 029 is the non-obvious one: it went to
  @clinical-physio (VC-A) despite sports-science sources, because its subject is
  clinimetric (test-retest reliability, SEM, minimal detectable change) and
  measurement-instrument limits belong to the clinical verification culture --
  the same placement sleep-recovery/tracker-accuracy-003 already has in its own
  domain.
  WHAT THE FILL DOES NOT DO: the LIVE CONSEQUENCE recorded on the queued entry
  (the B7 plate policy picking micro-anchor lifts from an unsourced
  relative-load-jump heuristic) is NOT resolved by a graded number, because no
  evidence supports one. What the sprint supplies instead is the arithmetic
  justification for relative framing without the rejected physiological story,
  an explicit statement that no increment size is evidence-backed, removal of
  the injury-risk rail, and a measurement floor bounding what any retest can
  confirm. The policy remains a heuristic; it is now a heuristic that knows it
  is one.
  RESIDUAL SUB-GAPS carried out of this sprint -- all seven genuinely unfilled,
  and each recorded on the relevant item:
  1. No trial has manipulated increment magnitude in TRAINED lifters. Hostler
     2001 is untrained, upper-body only, n=19.
  2. Absolute (kg) versus relative (%) increment framing has NEVER been tested
     head-to-head. Both framings carry error (percentage framing is itself
     ~2.5 reps wide at 80% 1RM, Nuzzo 2024); neither is the demonstrated
     correct one.
  3. Increment SIZE and increment FREQUENCY have never been separated. Every
     protocol confounds them.
  4. MDC/SEM for WORKING-SET loads is thin to absent -- all reliability data is
     laboratory 1RM testing under standardized protocol. The transfer to the
     loads a lifter actually manipulates week to week is an extrapolation of
     unknown direction.
  5. Machine and cable FIXED-STACK progression has ZERO research literature --
     vendor and forum sources only. Treat as ABSENT, not weak. This is the case
     where the trainee cannot choose the increment at all, so it is the case
     where guidance would matter most.
  6. Failed-increment and reset protocols are untested. The nearest RCT
     (Coleman 2024, PMC10809978) tested complete CESSATION, not a load
     reduction and not a reset, and found it impaired lower-body strength.
  7. No study interacts increment size with training age, sex, or bodyweight.

Filled 2026-08-22 (stretching / DOMS / recovery collection sprint, v7):
- STRETCHING + RECOVERY was a total blind spot -- the warehouse held ZERO items,
  at any grade, on acute static stretching, dynamic warm-up / mobility effects,
  DOMS, active recovery, blood-flow recovery modalities, recovery timelines, or
  session spacing. Discovered when a live 사용자 question (prep work on a
  still-fatigued muscle) returned nothing; the miss was never logged at the time
  (see GAPS-instance.md, second unlogged-hole incident after rest-interval).
  Now covered by six items from a 19-source deep-research pass:
  - exercise/acute-static-stretch-force-deficit-021 (@performance-lit, B/C,
    contested) -- duration-dependent force deficit, ~60 s per muscle group
    threshold; deficit is specific to ISOLATED MAXIMAL STRENGTH and does not
    extend to jump/sprint/RFD; disappears inside a full warm-up.
  - exercise/dynamic-warmup-same-day-performance-022 (@performance-lit, B/C,
    contested) -- the warm-up carries the benefit; the stretching MODALITY
    inside it is a small and possibly null increment.
  - exercise/doms-timeline-mechanism-023 (@clinical-physio, B/C, contested) --
    onset/peak/resolution timeline + repeated-bout effect; soreness correlates
    POORLY with every objective damage marker, so it is not a training gauge;
    mechanism genuinely contested (classical damage-inflammation vs the
    bradykinin/NGF nociceptor-sensitization pathway).
  - exercise/recovery-modality-soreness-vs-performance-024 (@performance-lit,
    C/B, contested) -- the PERCEIVED-SORENESS vs MEASURED-PERFORMANCE split;
    massage tops the soreness meta and is null on every performance endpoint.
  - exercise/recovery-kinetics-session-spacing-025 (@performance-lit, C/D,
    contested) -- proximity to failure / volume / movement complexity, not a
    per-muscle-group clock.
  - exercise/prep-on-fatigued-muscle-two-effects-026 (@clinical-physio, C/C/D,
    contested) -- the originating question, answered as two separately graded
    effects.
  ROUTING NOTE: all six went to the EXERCISE domain, NOT sleep-recovery, even
  though "recovery" is in that domain's name. sleep-recovery's single lane
  (@clinical, VC-A) is anchored to the AASM/sleep-medicine authority hierarchy,
  the wrong verification culture for exercise-induced muscle physiology; the
  exercise domain's 3-lane structure maps the evidence cleanly (@clinical-physio
  for the nociception/physiotherapy RCT material, @performance-lit for the
  sports-science meta-analytic material). The sleep-recovery substantive-claim
  gap below is therefore STILL OPEN and was not touched by this sprint.
  RESIDUAL SUB-GAPS carried out of this sprint (each on the relevant item's
  refraction_notes, and each genuinely unfilled):
  - No trial exists on the DIRECT question -- prep performed on a muscle already
    carrying fatigue from a previous session. Item 026 is assembled inference
    from adjacent designs and says so.
  - No trial tests whether pre-session stretching changes reps-at-load across a
    multi-set heavy compound SESSION. All stretching outcomes are single efforts
    (one contraction, one jump, one sprint).
  - No systematic comparison of recovery kinetics ACROSS muscle groups under
    matched volume/intensity/proximity-to-failure exists anywhere. The
    per-muscle-group recovery tables in circulation are practitioner
    constructions. This is a real hole in the field, not just in this warehouse.
  - Cold-water immersion's alleged blunting of long-term hypertrophy/strength
    adaptation was NOT researched in this pass; flagged on item 024 so its
    absence is not read as an all-clear.
  - The stretching/warm-up evidence base is overwhelmingly young adult males;
    the 2024 meta states its results are not interpretable for women or children.
    Interacts with exercise/female-training-considerations-020's claim (6), which
    recommends stability work over static stretching for women -- that specific
    sex-conditioned claim remains D-tier practitioner material and was NOT
    upgraded by this sprint.
  - Whether performance-based readiness proxies (first-set rep performance, bar
    speed, jump height) are practical day-to-day autoregulation signals for a
    general trainee is untested; item 025 names them only as what the trials
    measured.

Filled 2026-07-31:
- Inter-set REST INTERVAL was an UNLOGGED coverage hole -- the warehouse held
  volume/dose-response and regional-hypertrophy items but nothing on rest, and
  this gap was never even recorded here. Now covered by
  exercise/rest-interval-volume-load-017 (@performance-lit, grade B/C) from a
  2026-07-31 deep-research run (11 sources, 25 claims verified 3-0). Residual
  sub-gaps carried on that item's refraction_notes: no direct compound-vs-
  isolation head-to-head rest trial; the volume-equated evidence is isolation/
  untrained/short-duration, so heavy-compound + trained-strength application is
  an extrapolation; RIR-by-rest quantitative thresholds are undetermined.

CLOSED 2026-08-23: the "Queued 2026-08-23" LOAD-INCREMENT SIZE / MICROLOADING
entry that stood here was filled by the v9 sprint and has been rewritten as the
"Filled 2026-08-23" block above, in newest-first order with the other fills. Its
original terms are preserved there (instance-side logging 2026-07-31, the
23-day human-carried-route delay, the cron promotion, the owner-go block, and
the B7 plate-policy live consequence), together with what the fill did NOT do
and the seven sub-gaps that remain open. The first cron-promoted gap on record
is therefore also the first cron-promoted gap closed.

Safety boundary -- drugs row (added 2026-09-25, pack_health 0.17.1):
- exercise/harm-route-boundary-031 lists "drugs" (PEDs / injections /
  non-prescribed drugs for body composition) as a caught route but NO graded
  item carries its reasons. The row tells the agent to invent nothing and point
  to a physician. A collection sprint should fetch sourced @clinical-physio
  items on anabolic-androgenic steroid harms and on non-prescribed diuretic /
  stimulant use for weight loss, then re-point the row at them.

Body-ideal archetype sprint (v33, 2026-09-30, owner ask 19:53) -- filled and open:
- FILLED: exercise/body-ideal-archetype-map-032 and one row per archetype,
  033-045 (classic X, men's V, open bodybuilding, CrossFit/functional,
  Pilates, calisthenics/gymnast, yoga/mobility, powerlifting,
  weightlifting/athletic power, endurance, swimmer, combat, healthy-lean).
  Machine index: payload/service/health/body_ideal_archetypes.json.
- OPEN, not sourced: no peer-reviewed quantification of the classic-physique
  proportions (shoulder-to-waist, thigh-to-waist). Federation judging is
  qualitative ("harmonious", "good proportion"); the only numbers are the
  height-indexed weight caps. Do not invent a target ratio.
- OPEN: segmental InBody (arms/legs/trunk lean) validity in resistance-trained
  adults. nutrition/body-composition-measurement-floor-011 covers whole-body
  bias; segment-level agreement with DXA was seen to vary by population
  (hundreds of grams per limb, kilograms in the trunk) in clinical samples
  only. A sprint should fetch a trained-population segmental validation before
  any item grades a segmental lean-mass CHANGE as real.
- OPEN: Pilates tempo is qualitative in every source found ("slow",
  "controlled", "flow"); no source gives seconds per repetition. The
  controlled_tempo marker proposed for the kit therefore needs a craft
  definition (e.g. a stated eccentric/concentric tempo, or a Pilates-type
  movement tag), not an evidence-derived threshold.
- OPEN: yoga fitness evidence located only in older adults (Shin 2021) and
  clinical groups; no pooled trial set in healthy young/middle-aged adults.
- OPEN: injury data for straight-arm calisthenics skills (planche, levers,
  muscle-ups) outside CrossFit samples; the gymnast review is competitive
  gymnastics only.
- OPEN: swimmer look -- selection (limb length) vs training contribution is
  unquantified; the item is contested on that point.
- OPEN: Hyrox / fitness-racing not itemised separately (one acute-response
  study found, Brandt 2025); currently read as CrossFit/functional + endurance.
- STILL OPEN from v32: the drugs row of exercise/harm-route-boundary-031 has
  no graded harm item. v33 added the prevalence side only (Sagoe 2014, cited in
  035), not harms.
- MEASUREMENT GAPS (not warehouse gaps, recorded here so they stay visible):
  no kit token for girths, range of motion, pace/distance, jump/sprint/bar
  speed, skill level, controlled-tempo share, benchmark times, or weekly
  cardio minutes; segmental lean mass is readable but not a strand token. The
  proposed names are in body_ideal_archetypes.json `missing_token_defs`.

Body-ideal archetype sprint pass 2 (v34, 2026-09-30, owner asks 19:57/20:02) -- filled and open:
- FILLED: 046 climber, 047 grappler / 씨름 / wrestler (split from the
  striking-leaning combat row 044), 048 sprinter/athletic, 049 rower, 050
  cyclist, 051 dancer, 052 ski/snowboard, 053 racket sports; map 032 and
  body_ideal_archetypes.json v2 updated.
- OPEN: 씨름 has almost no English-language sport science -- two small
  Korean studies (isokinetic asymmetry n=25; short-term weight loss n=6).
  The grappler row leans on wrestling/judo reviews. A sprint should fetch
  KCI (Korean) literature on 씨름 physiology and injury before any item
  claims something 씨름-specific beyond the rule and the classes.
- OPEN: 씨름 and lightweight-rowing class limits were read from press /
  broadcaster explainers; the 대한씨름협회 and World Rowing rulebooks were not
  fetched. The 'above-the-knee touches the ground' loss rule is widely
  repeated but was NOT found in the UNESCO or Korea.net text fetched, so no
  item relies on it.
- OPEN: no study links neck strength to neck-injury risk in wrestling (Lee
  2017 critically appraised topic); neck training in 047 is craft.
- OPEN: climbing injury risk factors are "inconclusive and contradictory"
  (Zielinski 2025); the leanness-pressure evidence is one recreational survey.
- OPEN: squash has no dedicated source; the racket row is tennis- and
  badminton-led. Table tennis only appears as a trigger word.
- OPEN: dancer evidence on supplementary strength training is two studies
  (Angioi 2009) plus one feasibility trial; energy-deficiency figures are
  small professional cohorts whose prevalence depends on method.
- OPEN: ski/snowboard physiology (eccentric demand, low-position endurance)
  is craft here; the sources found are injury-side only. Track-sprint
  cycling is named as a separate picture inside 050, not itemised.
- MEASUREMENT GAPS added: grip, finger hang, climbing grade, neck girth,
  loaded carries, rowing and riding distance, cycling power, single-leg
  balance, agility. Proposed names in body_ideal_archetypes.json
  `missing_token_defs`.

## nutrition

Dropped for quality: none dropped -- all five converted @obs-inferential rows are
verified 3-vote survivors. (The GRADE-inadequate position was CONTESTED, so it
shipped at C-equivalent with a contested flag rather than being dropped.)

Coverage the rubric names but batch1 does not supply:
- The nutrition lane is currently 4/5 field-METHODOLOGY items (observational
  dominance, eight fallacies, tool instability, GRADE-inadequate debate) + 1
  substantive claim (protein intake). It is heavy on "how to grade nutrition" and
  thin on graded substantive diet/supplement claims.
  -> Fetch substantive supplement/diet claims to grade through the lane: omega-3,
     vitamin D, creatine-for-nutrition-overlap, fiber, added-sugar, dietary-pattern
     (Mediterranean) outcomes. Encode tiny-effect (RR 0.95-1.05 -> C cap) and
     confounding downgrades per this lane's rules.
- MR ERRATA (inherited DGN-151): Mendelian randomization is retained as a
  method-valid path to the A ceiling in the rubric, but batch1 did NOT empirically
  confirm any MR-backed claim. No MR-backed A item was authored (correctly).
  -> A future sprint must RE-SOURCE an MR-backed A claim before any ships; MR stays
     in the ceiling as a method, not deleted.
- NutriGrade parallel-run: the tool-instability item establishes the rule, but no
  item yet demonstrates an actual GRADE-vs-NutriGrade disagreement forcing a
  CONTESTED flag on a substantive claim. Fetch one worked case.

Filled 2026-09-02 (nutrition-lane collection sprint, v13):
- The lane's headline structural complaint above -- 4/5 field-METHODOLOGY items
  and 1 substantive claim, "heavy on how to grade nutrition and thin on graded
  substantive claims" -- is now PARTIALLY CLOSED. The lane goes 5 -> 15 items.
  The balance is deliberately not all-substantive: a consumer that reads a real
  meal log every day needs the MEASUREMENT items as much as the diet items,
  because the log is the instrument.
  - nutrition/self-report-underreporting-007 (@obs-inferential, A/field-methodology,
    not contested) -- recovery-biomarker validation across 5 pooled US cohorts.
    FFQ understates energy ~28%, single 24-h recall ~15%, protein less. The
    load-bearing part is that under-reporting is DIFFERENTIAL (predicted by BMI,
    age, education), so a flat correction factor would swap a known bias for a
    hidden one. A logged intake is a floor and a trend line, not an estimate.
  - nutrition/protein-per-meal-ceiling-008 (B, contested) -- a live printed
    dispute held against an already-shipped top-band item. Trommelen 2023
    (quadruple tracer, n=36 recreationally active young men, 25 vs 100 g) reports
    no upper limit in magnitude or duration; Witard & Mettler 2024 dispute the
    practical reading and state it does not extend to resistance-trained young
    women; Trommelen replied in print. Deliberately UNRESOLVED. The only
    consumer-facing change is a de-escalation: there is no longer a defensible
    basis for warning a user that protein above ~40 g in one sitting is wasted.
  - nutrition/protein-distribution-thin-009 (C, contested) -- the even-distribution
    concept, traced. Positive result is an n=8 acute crossover; an 8-week RCT
    (n=14) and a further RCT (n=24) both returned null at real outcomes; the
    review-level positive association does not extend to strength or turnover.
  - nutrition/energy-availability-threshold-010 (C, contested) -- the 30 kcal/kg
    FFM cut-off, with the 2023 IOC consensus statement's own walk-back quoted
    verbatim, its n=29 / 5-day / sedentary-female origin named, and the
    male range (~9-25) recorded as lower and less understood.
  - nutrition/body-composition-measurement-floor-011 (B, not contested) --
    instrument-limit item bounding what any body-composition reading can confirm.
  - nutrition/weight-loss-rate-lean-mass-012 (C, contested) -- the 0.5-1 %/wk
    rule traced to one unblinded n=24 trial with a duration confound.
  - nutrition/fibre-doseresponse-013 (C, not contested) -- Lancet 2019 fibre
    series. Partially answers the "fetch substantive diet claims" request above:
    fibre was chosen over the other named candidates (omega-3, vitamin D, added
    sugar, Mediterranean pattern) because it is the one with BOTH a large
    prospective base and a randomised arm, so the lane's observational discount
    lands on something rather than on everything. The item records explicitly why
    the RR 0.95-1.05 cap does NOT apply to it.
  - nutrition/kr-reference-intakes-2025-014 (A/jurisdictional-standard, LOCALE KR).
  - nutrition/metabolizable-energy-atwater-015 (B, not contested) -- measured
    metabolisable energy vs Atwater prediction for tree nuts.
  - nutrition/kr-food-composition-accuracy-016 (C, contested, LOCALE KR).

- KR-LOCALE CHECK RUN, and it changed the answer. This is the first pass to
  check the Korean case for this lane, and two findings came out of it.
  1. STALENESS. Korea revised its national reference standard on 2025-12-31
     (2025 KDRIs, MOHW with the Korean Nutrition Society, statutory 5-year
     cycle). Protein AMDR moved 7-20% -> 10-20%; fibre was re-derived on a new
     12.5 g/1000 kcal basis. Every 2020-edition Korean figure in circulation,
     including ones a model would recite from memory, is a prior edition. Item
     014 carries this as its first refraction note.
  2. DATABASE ACCURACY. Exactly one chemical validation of the Korean food
     composition tables was located (n=66 women, Jeju, 2003): energy 98%,
     protein 101%, lipid +24%, carbohydrate -8%. Its answer is convenient for a
     protein-focused consumer, which is precisely why it ships at the
     observational band with a contested flag rather than as reassurance.

WHAT THE FILL DOES NOT DO: it does not give the consumer a trustworthy number
for what the user actually ate. Three INDEPENDENT error sources now sit on
record between a logged Korean meal and the truth -- self-report bias (007),
composition-table bias (016), and the composition-to-available-energy conversion
(015) -- and they do not cancel in any known ratio. Netting them off against each
other is explicitly forbidden on item 015. The lane can now say how the number is
wrong; it still cannot say what the right number is.

REFUSED THIS SPRINT (recorded rather than dropped, v7/v9 rejected-claim
discipline). Each of these was searched, not assumed:
- RATE-OF-MUSCLE-GAIN TABLES ("a beginner can gain 1-1.5% of body weight per
  month", and the tiered ladders by training age). A targeted search for any
  primary study measuring a maximum or typical rate of lean-mass gain returned
  ZERO results. These numbers are practitioner-authored and have no trial behind
  them anywhere. REFUSED OUTRIGHT -- must never be spoken as research. This is
  the nutrition-side twin of the v9 load-increment finding: the field's most
  confidently quoted number is one nobody has measured.
- CONSUMER FOOD-TRACKING-APP DATABASE ACCURACY. Located studies are n=37
  Filipino adults with obesity and an Australian app-store quality survey.
  Nothing KR-applicable, nothing adequately powered. REFUSED.
- KOREAN MIXED-DISH LOGGING ERROR (jjigae, guk, bibimbap and other composite
  servings). No primary source quantifies portion or nutrient error for Korean
  composite dishes as logged by a consumer. This is the single sub-topic where
  the consumer most needs a number and where there is none. REFUSED, and NOT
  inferred from item 016, which measured correctly identified duplicate portions
  and therefore removes exactly the error this question is about.
- SODIUM AND THE KOREAN DIET. The most obviously Korea-specific nutrition
  question. Outcome evidence is genuinely disputed and needs its own adversarial
  pass. NOT RESEARCHED; its absence is flagged on item 014 so it cannot be read
  as an all-clear.
- MEAL FREQUENCY and INTERMITTENT FASTING. Out of this sprint's brief. Recorded
  as UNTOUCHED, not as absent.

RESIDUAL SUB-GAPS carried out of this sprint, each recorded on the relevant item
and each genuinely unfilled:
1. No Korean-language validation of a consumer meal log against recovery
   biomarkers exists. The direction of self-report bias transfers; the
   percentages do not, and item 007 says so rather than importing them.
2. No adequately powered trial has tested even-vs-skewed protein distribution to
   a HYPERTROPHY endpoint in young resistance-trained adults. Both controlled
   trials are in older adults, because the question is funded as a sarcopenia
   question. Item 009.
3. The per-meal protein ceiling dispute has no trial in resistance-TRAINED
   people, and the published counter-comment asserts the finding does not extend
   to resistance-trained young women. Item 008.
4. No least-significant-change figure exists for consumer bioimpedance under
   uncontrolled home or gym conditions. All precision data are standardised
   laboratory protocols. Item 011 states the direction and DECLINES to publish a
   threshold rather than importing a laboratory one.
5. Rate of weight loss has never been tested with equal-duration arms, so rate
   and training exposure remain confounded in the only trial that exists. No
   data at all outside the two rates tested. Item 012.
6. The Korean composition-table validation has no modern replication and covers
   one regional diet in 66 women from a 2003 publication, against table editions
   since revised. Item 016.
7. No safety-axis review was done for the deficit and energy-availability items.
   A hard gate on pregnancy_status for deficit advice is arguably correct but
   would have been authored from judgment rather than from a source, so it was
   deliberately NOT added. Flagged for a designed decision rather than left as a
   silent omission.

STILL OPEN after this sprint, unchanged: the MR ERRATA below (no
Mendelian-randomization-backed claim was sourced this pass, so the top band still
has no MR-backed item and MR remains a method in the ceiling rather than a
demonstrated path) and the NutriGrade parallel-run worked case below (no item yet
demonstrates an actual GRADE-vs-NutriGrade disagreement forcing a contested flag
on a substantive claim; the five contested items shipped here are contested on
evidence grounds, not on tool-disagreement grounds).


Rerun-needed: none (batch1 nutrition rows verified 3-0).

## sleep-recovery

Dropped for quality: none -- all three of the original @clinical rows are 3-vote
survivors.

CLOSED 2026-09-02 (v14 collection sprint, ten items 004-013): the coverage gap
that had stood open since v2 -- "There are ZERO substantive sleep/recovery
claims" -- is now closed. The v14 sprint authored the domain's first substantive
claims, all sourced to primary publications verified through PubMed rather than
to secondary write-ups. What landed:
- sleep-recovery/sleep-loss-performance-decrement-004 (B/D) -- Craven 2022
  meta-analysis, 69 publications / 227 outcomes. Sleep loss degrades measured
  performance in every exercise category INCLUDING strength. The pooled -7.56%
  is deliberately graded down (I2 = 98.1%); what survives is the pattern split
  (deprivation and LATE restriction harmful, early restriction not consistently
  so) and the AM/PM asymmetry with ~0.4% decrement per hour awake.
- sleep-recovery/sleep-extension-weak-evidence-005 (C/D, contested) -- Silva 2021,
  the only systematic review of sleep extension in athletes: 74 screened, SEVEN
  included, all three RCTs at high risk of bias, two outright nulls, no
  meta-analysis possible. Mah 2011 (n=11, no control arm) named as the origin of
  the popular claim.
- sleep-recovery/adult-injury-risk-not-established-006 (C/D, contested) --
  the "<8h = 1.7x injury" figure traced to Milewski 2014 (n=112 ADOLESCENTS,
  retrospective, 95% CI 1.0-3.0) and Gao 2019 (adolescent meta, OR 1.58); the
  adult prospective review (Dobrosielski 2021, 12 cohorts) concludes the evidence
  does NOT support poor sleep as an independent adult injury risk factor.
- sleep-recovery/cbti-strong-sleep-hygiene-weak-007 (A) -- Edinger 2021 AASM
  guideline + its companion systematic review. STRONG for multicomponent CBT-I;
  CONDITIONAL AGAINST sleep hygiene as a single-component therapy. The first
  item to actually use the aasm-hierarchy-001 / grade-aasm-anchor-002 anchors
  for a top-tier substantive claim, which is what those two items were for.
- sleep-recovery/melatonin-chronobiotic-not-hypnotic-008 (B/C, contested) --
  closes the MELATONIN half of the supplement-routing gap below. Auger 2015
  endorses strategically timed melatonin for circadian disorders; Sateia 2017
  suggests clinicians NOT use it for chronic insomnia; Ferracioli-Oda 2013 puts
  the pooled effect at ~7 minutes of sleep-onset latency.
- sleep-recovery/nap-force-null-shuttle-signal-009 (C/B/D, contested) -- closes
  the nap-protocol gap. Mesas 2023 (22 RCTs, 291 male participants) vs Boukhris
  2024: the pooled "large effect" resolves into a strong signal on one
  intermittent-running test and a NULL on muscle force (ES 0.175, p = 0.267).
- sleep-recovery/evening-training-sleep-effect-010 (B/C/D) -- Stutz 2019 PSG
  meta-analysis: evening exercise does not harm sleep. Carries the source's own
  fragility disclosure (all moderator effects vanished on removal of one study).
- sleep-recovery/subjective-monitoring-vs-objective-markers-011 (B/C/D) --
  Saw 2016 (56 studies): subjective and objective measures generally do NOT
  correlate and subjective ones track load better. Manresa-Rocamora 2021:
  HRV-guided training improves HRV and produces only small non-significant
  performance differences, in endurance training only.
- sleep-recovery/evening-light-mechanism-vs-intervention-012 (C/D/B, contested)
  -- Chang 2015 (n=12, four-hour inpatient exposure) establishes the mechanism;
  the Cochrane review of blue-light filtering lenses (17 RCTs, no pooling
  possible, very low certainty on sleep) shows the consumer product does not
  deliver. No included trial measured serum melatonin.
- sleep-recovery/hour-target-is-a-threshold-consensus-013 (B/D, contested) --
  the AASM/SRS "7 or more hours" is a modified-RAND expert CONSENSUS with a
  THRESHOLD shape and no upper bound, on a predominantly cross-sectional
  self-report base; the familiar "7-9" RANGE is the National Sleep Foundation's
  separate product. Built on the consensus panel's own limitations section.

ROUTING NOTE (unchanged from v7 and still correct): recovery-from-TRAINING
physiology continues to live under the exercise domain (items 021-026), not
here. This lane's verification culture (@clinical, VC-A, AASM-anchored) is the
right grader for sleep medicine and the wrong grader for exercise-induced muscle
physiology. What v14 added is the SLEEP side of the domain's name, which was the
genuinely missing half.

OPEN -- not closed by v14, each searched and deliberately refused rather than
filled with plausible material:
- SLEEP DEBT AND ITS REPAYMENT. Searched. The best-controlled source located
  (Depner 2019, Curr Biol, n=36 across three arms) found ad libitum weekend
  recovery sleep failed to prevent metabolic dysregulation -- but its endpoints
  are insulin sensitivity and energy intake, NOT performance, and n=36 with
  three arms cannot carry a general claim. NO performance-endpoint evidence on
  accumulated deficit or its repayment was located. Refused rather than shipped.
  -> Fetch performance-endpoint evidence on cumulative sleep restriction across a
     training week and on whether recovery sleep restores it.
- MAGNESIUM (the other half of the v3 5a supplement-routing tie-break). NOT
  researched in this sprint at all. Melatonin is closed; magnesium is untouched.
  -> Fetch magnesium sleep claims; route efficacy here, safety cross-reference to
     nutrition.
- PROPRIETARY READINESS / RECOVERY SCORES. Searched, not found. No peer-reviewed
  validation of a consumer device's composite readiness or recovery score against
  measured next-day physical performance was located. What exists is
  observational work correlating such scores with training load and sleep
  duration, which shows the score responds to its inputs, not that it predicts
  capability. Recorded on item 011 as a searched-and-unfound gap, NOT as a
  finding against the devices.
  -> Fetch any validation study with a performance endpoint. If none exists, that
     absence is itself worth stating as a durable finding.
- SLEEP AND HYPERTROPHY / ANABOLIC ENDPOINTS. Searched, refused. The two
  candidate primaries are small and mechanistic: Leproult & Van Cauter 2011
  (JAMA research letter, n=10, one week of 5 h sleep, testosterone) and Saner
  2020 (J Physiol, n=24 across three arms, myofibrillar protein synthesis lower
  under five nights of 4 h time-in-bed, maintained by high-intensity interval
  exercise). Both are interesting; neither supports a hypertrophy or strength
  OUTCOME claim, and shipping them would have meant laundering mechanism into
  outcome. Refused.
  -> Fetch a training-outcome study (lean mass or strength) under controlled
     sleep restriction before authoring anything here.
- CAFFEINE TIMING VERSUS SLEEP. Named in the original gap list, still NOT
  researched. Untouched by v14.
- CREATINE KINASE AND OTHER BIOCHEMICAL RECOVERY MARKERS as predictors. Searched
  without locating a clean systematic-review anchor. Item 011 covers the general
  subjective-versus-objective finding; a CK-specific item was not authored.
- Behavioral sleep-hygiene HABIT claims still straddle learning-habits (VC-C) and
  this lane. Item 007 now carries the clinical half (the AASM guideline's
  conditional recommendation against sleep hygiene as a standalone therapy); the
  behaviour-change half remains learning-habits territory.
- SEX-CONDITIONED EFFECTS. Every substantive source in this sprint is
  overwhelmingly or exclusively male: Craven 2022 was 89% male, the nap
  meta-analyses are 100% male. This is the same population skew flagged for the
  exercise stretching literature and it is now flagged here too.

Rerun-needed: none. All v14 sources were verified against PubMed primary records
(or, for the two AASM guidelines and the consensus statement, against the
publisher full text) rather than against secondary write-ups.

## cooking

Added 2026-09-02 (v15 cooking-lane collection sprint). The domain had no
GAPS section at all before this, which was itself a gap: it shipped three items
in the 2026-09-02 rubric-conversion pass with nothing recording what the lane was
missing.

Two lanes, two evidence standards, and they must not be blended:
- @food-safety (VC-F) takes the regulator of the jurisdiction the user cooks in
  (Ministry of Food and Drug Safety / 식약처, foodsafetykorea.go.kr) or
  peer-reviewed microbiology. A US regulatory fact is NOT a Korean regulatory
  fact.
- @test-kitchen (VC-E) takes published food science. Not a recipe blog, not a
  cooking-show assertion, not a content-farm repost of an unnamed study.

CLOSED by v15 (nine items, 005-013): the domain's first substantive
cooking content. Before this sprint the three existing items were 001 (how craft
testing is graded), 004 (how contested toxicity scares are defaulted) and 002
(poultry temperature) -- two of the three were about the FIELD rather than about
cooking. The lane now carries a Korean core-temperature table (005), the Korean
legal cold-chain band (006), the reheating-is-not-a-reset mechanism (007),
histamine in blue-backed fish (008), cutting-board cross-contamination (009), the
winter oyster rule (010), and three folklore corrections (011-013).

Jurisdiction rule, established the hard way and now the lane's standing
discipline: on 2026-09-02 a claim was DROPPED from this lane after a Korean
check. The US codifies a lower-temperature-plus-holding-time safety equivalence
for whole cuts; Korea codifies nothing of the kind, its official guidance gives
plain core temperatures, and 레스팅 appears in Korean sources only as a juiciness
technique and never as a safety equivalence. Item 005 now fences that exact edge:
it publishes the Korean beef range 63~77C verbatim and records in the same breath
that no holding-time equivalence attaches to its lower end. Any future pass that
meets the US construct in a source should read that note before acting.

OPEN -- searched in this sprint and deliberately refused rather than shipped:

- MEAT RESTING as a juice-retention rule. Every quantified measurement located is
  blog-tier (a test-kitchen write-up reporting tablespoons of purge; a secondhand
  attribution to a culinary-science journal that could not be resolved to a
  citation). The one controlled attempt located, which held serving temperature
  constant at slicing, reported NO difference. Refused in both directions: the
  lane ships neither "resting keeps the juices in" nor "resting does nothing".
  What would close it: a primary publication measuring purge loss against a
  controlled internal temperature at slicing.

- MARINADE PENETRATION DEPTH. The circulating millimetre figures (wet marinade
  1-3 mm, dry brine up to 5 mm, "salt takes 24 hours to reach an inch") are
  blog-sourced. The peer-reviewed literature located measures something else:
  phosphate marinade penetration in tumbled poultry, ultrasound-assisted salt
  diffusion in sauced duck, NaCl diffusion simulation in multi-tissue beef. None
  of those is a household marinade. Refused. What would close it: a primary study
  measuring flavour-compound or salt penetration under domestic marination.

- "NEVER WASH RAW CHICKEN". Real public-health advice from named regulators, and
  the mechanism (splash dispersal of a low-infectious-dose organism) is
  plausible, but in this pass it could be traced only to regulator communications
  and press coverage, not to a retrievable primary measurement. Refused. Note the
  complication that makes this worth doing properly rather than assuming: a
  US-funded consumer observational study exists in this area and was NOT read,
  and its reported direction is that not-washing did not eliminate sink
  contamination. Item 009 ships the cutting-board evidence that does have a
  primary behind it, deliberately in place of this claim.

- COOKING TIME AS A FUNCTION OF THICKNESS (Fourier scaling: conduction time goes
  with the square of the distance, so a "minutes per kilogram" rule is the wrong
  shape). The physics is not in doubt and this would be genuinely useful to a live
  session, but the peer-reviewed food-engineering sources located were paywalled
  (Journal of Food Engineering) or scanned-image-only (a 1975 Reciprocal Meat
  Conference paper). Nothing was quoted from either. Refused pending a readable
  primary.

- KOREAN FERMENTATION SAFETY (kimchi, jang, 장아찌) and BANCHAN STORAGE LIMITS.
  The highest-value Korean-specific gap in the lane and NOT researched in this
  pass. Its absence here is a not-yet-asked, not an all-clear. What would close
  it: MFDS guidance or Korean food-microbiology literature on fermentation
  temperature/time and on refrigerated shelf life of prepared side dishes.

- KOREAN-DISH EVIDENCE FOR ITEM 007. The reheating-is-not-a-reset mechanism is
  established in rice and in model systems; nothing was located measuring spore
  survival or toxin formation in 국, 찌개, 볶음밥, 김밥 or banchan specifically,
  and no Korean outbreak dataset was read. Item 007 carries the extension as an
  explicit mechanistic inference. This is the single most valuable thing a next
  sprint could close, because the reheated-stew habit is where the mechanism
  actually bites.

- SHELLFISH-WIDE HEATING RULE. Korean media generalise the 85C-for-one-minute
  oyster instruction to shellfish at large. The government source read for item
  010 stated it for oysters. The generalisation is not shipped and needs its own
  source.

- INDEPENDENT CORROBORATION FOR ITEM 008. The US fishery-hazards guidance chapter
  on scombrotoxin is the standard second source for histamine heat-stability and
  would also cover the histidine-decarboxylase enzyme surviving freezing. Both the
  official copy and a university mirror refused retrieval (404 and 403) in this
  pass. Nothing was quoted from them; the enzyme detail is therefore absent from
  the item rather than asserted.

Edition-check debt (the v13 staleness lesson applied to this domain): item 006's
Food Code temperature bands were read from the ministry's own presentation of its
standard rather than from the legal annex, and item 008's 200 mg/kg histamine
specification comes from a 2012 announcement. Neither was checked against the
edition in force in 2026. A jurisdiction-bound item needs an EDITION check, not
just a source check. Both are recorded as current-as-presented, not as certified.

Structural gap, axes: none of the nine items carries applicability.axes. The axes
ledger is fitness-shaped -- training status, one-rep max, body composition,
sleep baseline -- and nothing in it conditions a cooking-safety claim. The axes a
cooking session would actually refract on (allergen exposure in the dish being
cooked, who is at the table, appliance capability, whether a thermometer is even
available) either do not exist in the ledger or exist in a form aimed at a
different question. Adding them is an append-only ledger change and was
deliberately NOT attempted in a content-only release. Flagged for whoever owns
the cooking-session module design.

Rerun-needed: none. Every source in v15 was retrieved directly -- the
Korean items from the ministry's own portal or the government policy portal, the
microbiology and Maillard items from the publishers' records with resolvable
DOIs, and the alcohol figures extracted from the USDA primary PDF itself rather
than from any secondary write-up.

## relationships-communication

Section opened 2026-09-02 (v16 collection sprint, ten items 008-017). This
domain had no GAPS section at all before this sprint -- it was activated in the
26-row rubric-conversion pass with 7 items and no gap accounting, the same class
of omission that finance-investing and mental-health carried. The section is
written from the state AFTER the expansion, not before it.

CLOSED BY v16: the domain's structural imbalance. The seven pre-existing rows
were five refutations, one curator checklist and one therapy-efficacy row -- a
domain that could say what is false and almost nothing about what is true. That
is now closed on the substantive side. What landed:
- relationships-communication/social-connection-mortality-magnitude-008 (B/C/D,
  contested) -- the direction survives scaling to 90 prospective cohorts and
  2,205,199 individuals (Wang 2023, Nat Hum Behav); the magnitude is roughly half
  the 2010 figure everyone quotes. Isolation 1.32, loneliness 1.14. Independently
  reproduced by Nakou 2025 (86 studies) to two decimal places on loneliness.
- relationships-communication/relationship-quality-predictors-joel-009 (B/A) --
  Joel 2020 PNAS, 43 dyadic longitudinal datasets from 29 laboratories. The
  top-band grade is on the NEGATIVE half: change in relationship quality was
  unpredictable from any combination of self-report, under 5% of variance.
- relationships-communication/satisfaction-trajectory-duration-010 (B/D) --
  Buhler 2021 Psychol Bull, 165 samples / 165,039 participants. Two distinct
  curves (age and relationship duration); within-relationship mean change is
  downward, steepest early.
- relationships-communication/divorce-prediction-crossvalidation-011 (A) --
  CLOSES the open question recorded on item 003. Heyman and Smith Slep 2001: <!-- estate-scrub:allow(author surname Smith, not an instance) -->
  positive predictive value 65.38% in development, 28.81% on crossvalidation,
  20.99% reweighted to true prevalence. Kim, Capaldi and Crosby 2007: independent
  replication failure, only 2 of 22 affective processes predictive.
- relationships-communication/tie-reciprocity-perception-gap-012 (C/D, contested)
  -- 53% of nominations reciprocal against 94% expected, r=0.95 expected vs
  r=0.36 actual. Graded down on purpose: n=84 in one classroom.
- relationships-communication/reach-out-appreciation-gap-013 (B/D) -- the only
  experimentally supported actionable finding in the sprint. Licenses the ACT of
  reaching out, explicitly NOT a frequency.
- relationships-communication/contact-cadence-no-evidence-014 (D/C) -- deliberate
  absence row, built like the exercise domain's load-increment-size gap row.
- relationships-communication/dunbar-number-not-derivable-015 (B/D, contested) --
  Lindenfors 2021, confidence intervals 4-520 and 2-336.
- relationships-communication/kr-weird-transfer-gate-016 (C/D, contested, KR) --
  the mandated locale check.
- relationships-communication/network-effect-inference-floor-017 (B) --
  Cohen-Cole and Fletcher 2008: the same standard method finds social contagion
  for HEIGHT.

STILL OPEN -- each searched this sprint and deliberately left unfilled rather
than filled with something plausible:
- CONTACT CADENCE, the domain's largest hole and the one its consumer most needs.
  No primary study prescribing a contact frequency, interval, or minimum contact
  count exists. Shipped as an explicit absence row (014) rather than left silent,
  because a gap-file entry does not fire at answer time and an item does. WHAT
  WOULD CLOSE IT: a randomised or quasi-experimental study manipulating contact
  frequency against a relationship-quality or wellbeing endpoint; or a
  within-person longitudinal dataset with OBJECTIVELY LOGGED contact (call or
  message records, not recall) related to closeness change. The objective-log
  requirement is not fussiness -- item 012 records that self-reported social data
  is biased in a consistent direction.
- LONELINESS INTERVENTIONS. Searched; NOT shipped. The best source located (Masi
  et al. 2011, Pers Soc Psychol Rev 15(3):219-266, PMCID PMC3865701) reports that
  single-group pre-post and non-randomized comparison studies yielded LARGER mean
  effects than randomized comparison studies, and that among randomized designs
  the most successful interventions addressed maladaptive social cognition. That
  is a design-quality finding, not an effect size a life agent can act on, and it
  is fifteen years old. A current randomized-only synthesis would close this.
- MEASURED VERSUS SELF-REPORTED SOCIAL CONTACT. The domain now records that
  perceived ties are biased (012), but no source was located that quantifies the
  error between self-reported and objectively logged social contact for adults.
  Searched via smartphone-sensing and communication-record framings; nothing
  usable found. This is the measurement floor the whole lane rests on and it is
  currently unquantified.
- KOREAN COUPLES AND COMMUNICATION DATA. Zero. Item 016 documents that every
  couples finding in this domain is Western-sampled and that the best-powered
  study says so explicitly. The health side has Korean cohorts; the relationship
  side has nothing. A Korean or East Asian longitudinal couples dataset would be
  the single highest-value acquisition for this domain.
- THE 5:1 RATIO. Distinct from the 2.9013 constant already refuted at item 001,
  and NOT closed by this sprint. Its primary sources were located and verified as
  citations (Gottman and Levenson 1992, JPSP 63(2):221-233; Gottman 1993, JCCP
  61(1):6-15 -- the same 73 couples in both), but no source was located that
  tests the 5:1 figure prospectively or out of sample. Given that item 011 now
  shows the divorce-prediction models from these same 73 couples collapse on
  crossvalidation and failed independent replication, the ratio should be
  presumed to inherit that problem -- but presumption is not verification, and it
  is recorded here as open rather than shipped as refuted.
- ATTACHMENT STYLE. Named as a top-five individual-difference predictor by Joel
  2020 (avoidance and anxiety) and otherwise untouched by this sprint. The
  popular typology version of attachment is a forced-choice categorical framing
  of what the research treats as continuous dimensions -- the same structural
  defect item 004 documents for love languages -- but no source was researched
  for it this pass. Flagged as a likely future refusal, not as one.
- SEX AND GENDER CLAIMS. Refused rather than shipped (see the ledger below). The
  gender-similarities evidence is strong (Hyde 2005; Zell, Krizan and Teeter 2015,
  106 meta-analyses, 386 effects, mean absolute d = 0.21) but no substantive claim
  in this domain currently needs it, and shipping a refutation with no target
  would be padding. Ship it when a domain claim requires the correction.

Rerun-needed: none. All v16 sources were verified against PubMed primary
records or the publisher DOI. Four were additionally read at PMC full text to
extract exact figures rather than trust an abstract: Heyman and Smith Slep 2001 <!-- estate-scrub:allow(author surname Smith, not an instance) -->
(the crossvalidation table), Almaatouq 2016 (the reciprocity counts), Joel 2020
(the sampling-limitation statement), and Holt-Lunstad 2010 (the smoking-comparison
wording, which is how the cigarette refusal below was established).

## mental-health

Added v17 2026-09-02 (mental-health lane collection sprint, thirteen
items 008-020). The domain had no GAPS section before this sprint, which was
itself a signal: it held 7 items and ALL SEVEN were methodology -- two grading
anchors (001, 002), a no-single-hierarchy rule (003), a publication-bias rule
(005), one comparator worked example (004), one contested-intervention worked
example (006), and a synthesised curator checklist (007). Excellent scaffolding
and almost nothing a generalist life agent could act on. The consumer here sees
the owner's daily blocks, energy, sleep and workload, so the sprint targeted what
is inferable from what is OBSERVED, not what a clinician would want.

What landed:
- mental-health/exercise-depression-trial-certainty-008 (B/D, contested) --
  Noetel 2024 BMJ network meta-analysis, 218 studies / 495 arms / 14170
  participants. Moderate effects vs active controls (walking or jogging g -0.62,
  yoga -0.55, strength training -0.49) and ONE study out of 218 meeting Cochrane
  low-risk-of-bias criteria, with CINeMA confidence LOW to VERY LOW. Authored as
  a CERTAINTY item, not an effect-size item: direction usable, magnitude not.
  Published correction (BMJ 2024;385:q1024) resolved separately.
- mental-health/activity-incident-depression-observational-009 (B/D) -- Pearce
  2022 JAMA Psychiatry, 15 prospective cohorts / 191130 participants / 2110588
  person-years. Curvilinear dose-response with the steepest gradient at the LOW
  end (18% lower risk at half the recommended volume, 25% at full). Kept SEPARATE
  from 008 on purpose: prevention-association and treatment-trials are constantly
  fused and have opposite weaknesses. The 11.5% preventable-fraction figure is
  explicitly refused for individual-level use.
- mental-health/behavioural-activation-noninferiority-010 (B/D) -- COBRA
  (Richards 2016, Lancet, n=440). BA non-inferior to CBT at 12 months (0.1 PHQ-9
  points, margin 1.9), delivered by junior mental health workers. Its HARD
  BOUNDARY note is graded at the top band and placed above the result, because
  this is the item whose mechanism most resembles something an assistant could
  improvise, and must not be.
- mental-health/screening-score-is-not-a-diagnosis-011 (A) -- Levis 2019 BMJ
  (PHQ-9 IPD meta-analysis, 58 studies, n=17357: sensitivity 0.88, specificity
  0.85 at cutoff 10+ vs semistructured interview) plus Levis 2019 BMC Medicine
  (69 meta-analyses: 31% pooled prevalence from screening tools vs 17% from
  diagnostic interviews). The lane's BOUNDARY item, authored deliberately as a
  measurement-limitation finding whose operative content is entirely negative.
- mental-health/group-to-individual-nongeneralizability-012 (B/C, contested) --
  Fisher 2018 PNAS. Variance 2-4x larger WITHIN individuals than within groups.
  The governor on every other item in the lane when applied to one person. Split
  grade because the empirical variance finding and the strong ergodicity
  conclusion have very different standing; the latter drew four published PNAS
  commentaries in 2019.
- mental-health/passive-sensing-hypothesis-generating-013 (C/D) -- De Angel 2022
  npj Digital Medicine, 51 studies. Consistent bivariate associations between
  depression and sleep / activity / location / phone-use features, and the
  reviewers' own ceiling adopted verbatim: "purely as a starting point for
  hypothesis generation". Operative rule: observed behavioural data may be used to
  ASK, never to CONCLUDE.
- mental-health/sleep-loss-affect-asymmetry-014 (A/C) -- Palmer 2024
  Psychological Bulletin, preregistered, 1338 effect sizes / 154 studies /
  N=5717. The lane's only EXPERIMENTAL evidence, hence its only clean top band.
  The finding is an asymmetry: sleep loss reliably removes positive affect
  (SMD -0.27 to -1.14) and raises anxiety (0.57-0.63), while negative affect and
  depressive symptoms are MIXED. Short sleep subtracts enjoyment more reliably
  than it adds misery, which is the opposite of the popular framing.
- mental-health/burnout-definition-bound-015 (A/E) -- Rotenstein 2018 JAMA, 182
  studies / 109628 individuals / 45 countries: at least 142 unique definitions,
  prevalence 0% to 80.5%, planned meta-analysis ABANDONED, correlates
  undeterminable. Plus the WHO ICD-11 entry, which scopes burn-out to the
  occupational context and does not classify it as a medical condition. Any
  specific prevalence figure is refused outright rather than graded.
- mental-health/workload-detachment-recovery-016 (B/C/D, contested) -- Wendsche
  and Lohmann-Haislah 2017 (86 publications, N=38124: detachment correlates
  -0.36 with exhaustion, -0.42 with fatigue, +0.32 with wellbeing, all
  cross-sectional so direction unidentified) plus Virtanen 2018 (189729
  participants, 35 countries, published plus unpublished IPD). The regional split
  is the point: 1.50 in Asia, 1.11 in Europe, 0.97 in North America, 0.95 in
  Australia. Direct within-study evidence that the WEIRD default estimate does not
  describe this warehouse's own locale.
- mental-health/wellbeing-exercise-comparator-collapse-017 (A/D) -- White, Uttl
  and Holder 2019 PLOS ONE (positive-psychology effects fall to about r = 0.10
  once small-sample bias is handled; depression effects outlier-dependent and
  generally non-significant) plus Cregg and Cheavens 2021 (gratitude, k=27,
  N=3675: g -0.51 vs waitlist but -0.18 vs active control at post-test). Carries
  a live MISATTRIBUTION catch, see the ledger.
- mental-health/phone-app-intervention-evidence-018 (B/C) -- Goldberg 2022 PLOS
  Digital Health, umbrella meta-review of 14 meta-analyses / 145 RCTs / 47940
  participants. NO effect size in the entire field met the prespecified
  convincing-evidence bar. Also: no moderators identified, and adverse effects not
  reported anywhere -- unstudied, not established.
- mental-health/ego-depletion-replication-failure-019 (A/D, contested) -- Hagger
  2016 RRR (23 labs, N=2141, d = 0.04, CI encompassing zero) and Vohs 2021 (36
  labs, N=3531, d = 0.06 non-significant, Bayes factor 4:1 favouring the null,
  co-authored by the effect's original proponents). Placed in this lane rather
  than learning-habits because its live consequence is SCHEDULING: no day plan
  may be built on a willpower budget.
- mental-health/kr-help-seeking-service-use-020 (B/D, locale KR) -- Rim 2023
  Psychiatry Investigation (National Mental Health Survey of Korea 2021, n=5511,
  response rate 40.7%, lifetime prevalence 27.8%, 12-month service utilisation
  28.2% for depressive disorder and 9.1% for anxiety disorder) plus Kang 2026
  Psychiatry Research (2011 vs 2021: stigma UP across all age groups, service use
  DOWN overall). The locale item, and the one the rest of the lane must be read
  through.

BOUNDARY NOTE, and it is the defining constraint on this domain. This is a
knowledge warehouse for an assistant, not a clinical tool. Nothing in this lane
is written as diagnosis, screening, risk assessment or crisis handling. Where a
topic could only be stated usefully in clinical-advice form it was refused and
recorded in the ledger rather than written in a softened version. The two items
closest to the line carry their boundary at the top band and ABOVE the result
rather than below it (010 and 011), because a boundary printed after the
interesting part is a boundary that will be skipped.

STRUCTURAL FINDING TO CARRY FORWARD: comparator collapse now appears in FOUR
independent literatures in this domain -- CBT for anxiety (004), mindfulness
(006), gratitude and positive-psychology exercises (017), and phone-delivered
interventions (018), whose reviewers state it as a property of their whole field.
At four independent appearances this is a lane-level regularity to expect by
default. A future sprint meeting a new intervention in this domain should ask
what the control group DID before it asks how big the effect was.

OPEN -- not closed by this sprint, each either searched and refused or explicitly
excluded on the clinical boundary:
- ANTIDEPRESSANT EFFICACY VERSUS PLACEBO. EXCLUDED ON THE BOUNDARY, not for want
  of sources. The literature is large, genuinely contested, and squarely about
  medication. A generalist life agent has no action to take on it, and any
  surfacing of it reads as guidance about someone's prescription. This is an
  out-of-scope-by-design exclusion and should stay one; it is recorded here so a
  later sprint does not read the absence as an oversight and fill it.
- DIAGNOSTIC CRITERIA, SCREENING PROTOCOLS, RISK ASSESSMENT, CRISIS HANDLING.
  EXCLUDED OUTRIGHT, out-of-scope-by-design. No item in this lane may state or
  imply a threshold at which someone should be considered to have a condition, be
  screened, or be treated as at risk. Item 011 is the closest this domain comes,
  and it is authored so that its entire operative content is a refusal.
- TREATMENT SELECTION. Excluded. Which therapy, which medication, which clinician
  -- none of it is answerable by this consumer and all of it reads as advice.
  Item 010 records a non-inferiority finding as a fact about the evidence base
  and explicitly refuses any operational use.
- KOREAN VALIDATION OF SELF-REPORT INSTRUMENTS. Not researched, and deliberately
  left open rather than filled, because researching it would mean assembling
  exactly the screening material the boundary above excludes. If a future sprint
  wants it, the question to ask is narrowly about MEASUREMENT INVARIANCE across
  languages, not about cut-offs.
- CONSUMER "STRESS" OR "MOOD" SCORES FROM WEARABLES. Searched, not closed. What
  the search returned is algorithm-development-and-validation work on bespoke
  physiological signals, not peer-reviewed validation of any shipped consumer
  stress or mood score against a measured affect outcome. Exactly parallel to the
  sleep domain's proprietary readiness-score gap, and recorded the same way: a
  hole in the evidence, NOT a finding against the devices.
  -> Fetch any validation of a shipped consumer composite against an affect
     endpoint. If none exists, the absence is itself worth stating durably.
- ECOLOGICAL MOMENTARY ASSESSMENT REACTIVITY. Searched without locating a clean
  meta-analytic anchor on whether repeatedly asking someone to rate their mood
  changes the mood being rated. Directly relevant to a system that would collect
  daily check-ins, and currently unanswered here.
- KOREAN WORKPLACE RECOVERY DATA. Item 016 carries the Asia-versus-West
  divergence on long working hours from a 35-country pooled analysis, which is
  strong. No Korea-specific study of psychological detachment or off-work
  recovery was located, so the detachment correlations in 016 remain
  WEIRD-sampled and are flagged as such.
- LONELINESS AND SOCIAL CONTACT. Not researched. A generalist life agent can
  observe social contact in a calendar, so this is a real coverage hole rather
  than an out-of-scope one, and it is the most obvious candidate for the next
  sprint in this domain.
- SEX-CONDITIONED AND AGE-CONDITIONED EFFECTS. Not examined in any item here.
  The same population-skew flag the exercise and sleep lanes already carry
  applies to this domain and has not yet been quantified for it.

Rerun-needed: none. Every source in this sprint was verified against the PubMed
E-utilities primary record or the Crossref work record; Cregg and Cheavens 2021,
Wendsche and Lohmann-Haislah 2017 and Rim et al. 2023 were additionally read at
publisher full text, and the correction to Noetel 2024 was resolved separately.

## home

Opened v19 (2026-09-02), 13 items across two lanes (@home-environment 7,
@household-labor 6). The domain is the owner's own taxonomy unit for the
household area and the lanes are his own two areas; he directed the warehouse to
be filled along his shape and said reorganising later is fine.

The structural fact about this domain, stated up front so later sprints do not
mistake the small item count for a thin sprint: **this area is almost entirely
folklore with a thin scientific core.** The candidate list going in was roughly
twice what shipped. Most household "life hack" claims, most antibacterial and
cleaning-product efficacy claims, most decluttering effect sizes and essentially
all air-purifier performance marketing do not survive contact with primary
literature. Four of the thirteen shipped items exist mainly to refuse a claim;
nine further claims were researched and shipped in no form at all (ledger at the
end of this file). A later sprint that finds this domain small should check the
rejected-claim ledger before assuming there is easy material here.

What is genuinely well evidenced, and is now covered:

- Dampness and mould as a respiratory exposure (item 001). WHO-level "sufficient
  evidence" plus pooled odds ratios. This is the strongest thing in the domain
  and everything else is weaker than it.
- The absence of any mould threshold (item 002) -- WHO's own explicit refusal to
  set one, which is what makes commercial spore-count testing unfalsifiable.
- Korean radon and ventilation regulation (items 003, 004), both read at Korean
  primary sources.
- Chloramine formation from mixing bleach with ammonia (item 008), the one
  hard-safety claim in the domain.
- The measured time cost of household labour in Korea (item 013).

What is NOT covered and should be the next sprint's target list:

1. **Korean high-PM2.5 ventilation guidance.** The genuinely practical Korean
   question -- whether to ventilate on a 고농도 미세먼지 day, and what the
   indoor/outdoor ratio does in a Korean apartment -- was searched and NOT
   verified at a regulator source in this pass. Nothing was shipped. Closing it
   means reading the Ministry of Environment's own response guidance and any
   Korean I/O-ratio measurement study directly. This is probably the single
   highest-value open item in the domain for a Korean user.
2. **Condensation (결로) in Korean apartments.** Korea has a mandatory
   condensation-prevention design standard for apartments (국토교통부고시
   제2016-835호, 공동주택 결로 방지를 위한 설계기준), whose existence was
   confirmed at law.go.kr but whose design conditions, TDR performance metric and
   unit-count threshold could not be read at source in this pass. This is the
   direct Korean bridge between item 001 (damp harms) and item 004 (ventilation
   is the lever), and it is a document-reading job rather than a research job.
3. **Bedroom CO2 and sleep quality.** Item 005 covers the office-derived
   cognition literature. The residential sleep case draws on a different
   evidence base and was not searched. Note the routing: if it lands, it may
   belong in sleep-recovery rather than here.
4. **Gas cooking, NO2 and respiratory outcomes.** Contested and politically
   loaded, with a well-known attributable-fraction estimate that has drawn
   substantive methodological criticism. Deliberately not attempted in a first
   sprint. Needs the primary estimate AND its published critiques read together,
   or it will ship as advocacy.
5. **Carbon monoxide alarms in Korean housing.** A hard-safety topic with a
   clear regulatory answer somewhere; not searched at all this pass.
6. **What actually works against household pests.** Item 007 establishes that
   one product class fails against bed bugs. No verified alternative protocol is
   carried, and nothing at all is carried for cockroaches or ants.
7. **Laundry temperature and textile hygiene.** Researched and REFUSED this pass
   for source-access reasons -- see the ledger. The candidate sources are
   narrative reviews rather than systematic ones, and full text could not be
   read at source. A later sprint should either read them properly or find a
   pooled analysis.
8. **Humidity targets.** The familiar 40-60% relative humidity range was
   researched and refused as unsourceable to any primary study (ledger). If a
   defensible target exists it is likely to be surface-condensation-based rather
   than a room-air range, which routes it into gap 2 above.
9. **Korean mould and damp prevalence.** No Korean measurement of dampness or
   mould prevalence in housing was located. Item 001 is universal; the Korean
   base rate is unknown here.

Boundary note for future sprints: food handling, cutting-board material,
refrigerator temperature and cross-contamination to food are **cooking**
domain questions and were deliberately left alone in this sprint, which ran
concurrently with a cooking expansion. Do not duplicate them here.

## work-career

Added 2026-09-02 by the work-career lane opening (v20). The domain
shipped in lanes.yaml from the v3 map with a registered @behavioral-career lane
and ZERO items; this release lands 20 and appends a second lane
(@venture-obs, VC-B) so the owner's own area split -- 회사/커리어 versus
사업/부업 -- is carried structurally rather than by convention.

This is the worst domain in the warehouse for survivorship bias and commercial
packaging, and the sprint was run on that assumption. Careers advice is
overwhelmingly produced by people it worked for, resold by consultancies with
a product attached, and quoted at a distance from whatever study it started
from. A large fraction of this sprint's work was refusal, and the refusals are
listed in the cross-cutting section below as the v20 rejected-claim
ledger. What follows here is what a NEXT sprint should fetch, with what was
searched and what would close each gap.

### Searched and not closed -- employment lane (@behavioral-career)

- US establishment survival rates. The primary is the Bureau of Labor
  Statistics Business Employment Dynamics programme. Every bls.gov URL tried
  (the age/survival tables, the entrepreneurship pages, the 20th-anniversary
  spotlight) returned HTTP 403 to automated retrieval. The figure is widely
  repeated at roughly 20 percent closing in year one and about half gone by
  year five, and it was NOT taken from any of the secondary write-ups that
  quote it. Closing this needs the BLS table read by a human or through an
  access path that is not blocked. Until then the domain carries only the
  Korean base rate (item 015).
  CLOSED 2026-10-03 (v35): read at the BLS Economics Daily BED table --
  private-sector establishments born March 2013, 79.6 percent alive in 2014,
  50.6 percent in 2018. Stored in item 015 with cohort and unit attached.
- Korean early-career wage-growth decomposition. Item 005 carries the US
  Topel and Ward estimate that job changes supply at least a third of
  early-career wage growth. No Korean equivalent -- a within-job versus
  between-job decomposition on 한국노동패널 or equivalent -- was located at a
  readable primary. This gap matters more than most because item 014 shows
  Korean pay is far more tenure-indexed, so the US magnitude is very likely
  wrong here in a knowable direction.
- Korean hiring norms and selection practice. Nothing was shipped about
  공채 versus 수시채용, 자소서 screening, or how Korean employers actually
  select, because no primary measurement was found. Item 001's validity table
  is international and its transfer to Korean practice is UNVERIFIED.
- Burn-out outside medicine. Items 009 and 010 both rest on physician
  populations, which is where the literature is. Whether the 142-definition
  spread and the organisation-versus-individual intervention gap hold in
  non-clinical occupations was not established.
- Salary-history bans and pay-range posting. Located as an active literature
  but no primary was read at source in this pass. Item 006 covers
  coworker-communication transparency only, which is a different intervention.
- Transfer of training to the job (Blume et al. 2010, Journal of Management
  36(4), 1065-1105, https://doi.org/10.1177/0149206309352880). Verified and
  deliberately NOT shipped here: it is a learning-and-transfer finding and
  belongs in learning-habits, not work-career. Routing decision, not an
  absence. Its most useful result for a future curator is that transfer
  relationships are inflated when the outcome is reported by the same source
  in the same context as the predictor.
- Open-plan offices (Bernstein and Turban 2018, Phil. Trans. R. Soc. B
  373(1753), 20170239, https://doi.org/10.1098/rstb.2017.0239). Citation
  resolved; not shipped because the study is two field cases and the effect
  size could not be verified at source in this pass.

### Searched and not closed -- independent-work lane (@venture-obs)

- Korean self-employment EARNINGS versus paid employment. Item 016 carries two
  US results that disagree. No Korean comparison was verified at a primary.
  This is the single most consequential hole in the venture lane, because item
  014 establishes that a large share of Korean self-employment is entered
  after displacement from a main job rather than chosen against a paid
  alternative -- which means neither US result is likely to transfer.
- Side-project and gig earnings distributions. Nothing shipped. The
  administrative-data reports that exist in this area are largely published by
  firms with a commercial interest in the answer, and the academic
  alternatives located either had author funding from the platform studied or
  could not be read at source. Recorded rather than filled.
- Korean 4대보험 obligations for the self-employed and for freelancers, the
  사업장현황신고 deadline for 면세사업자, and 홈택스 filing procedure. Item
  019 covers registration, withholding and VAT status only. The rest was NOT
  inferred.
- Serial entrepreneurship and performance persistence (Gompers, Kovner, Lerner
  and Scharfstein 2010, Journal of Financial Economics 96(1), 18-32,
  https://doi.org/10.1016/j.jfineco.2009.11.001). Citation resolved; the
  persistence magnitudes were not read at source, so nothing was shipped.
- Failure taxonomy. Item 015 counts administrative firm deaths, which merge
  failure, voluntary closure and restructuring into one number. No source was
  found that separates them for Korea. Until one is, the survival rate bounds
  optimism but cannot be spoken as a failure rate.

### Structural note for the next sprint

The employment lane has 15 items and the independent-work lane has 5. That
imbalance is real and it is honest: the employment side has meta-analyses and
randomised trials, and the independent side has administrative counts and two
econometric papers that disagree. Growing the venture lane means finding
better primary data, not writing more items from the same four sources.

## finance-investing

Added 2026-09-02 by the finance-investing lane opening (v12). The @quant-market
lane went from 0 to 17 items in that pass. This section records what was
researched and REFUSED, so a later sprint cannot quietly re-adopt a claim that
already failed verification here. Refusals are as load-bearing as the shipments:
finance is adversarial territory and most of what circulates as investing wisdom
is survivorship bias, backtest overfitting, or product marketing.

Rejected-claim ledger, v12 (a popular claim that failed verification is recorded
here, not silently dropped):

- INVESTOR BEHAVIOUR GAP ("the average investor underperforms the funds they own
  by several percent a year"). REFUSED. The circulating figure traces to the
  Dalbar QAIB series, whose method is disputed in a way that goes to the number
  itself, not to its interpretation: the published critique (Pfau, later
  corroborated by Edesess, both in trade publications) is that the calculation
  does not compute a proper internal rate of return over an ongoing series of
  cash flows and effectively treats deposits and withdrawals as occurring at the
  start of the study period, which penalises anyone contributing steadily.
  Dalbar's own rebuttal is a rejection of the premise rather than a correction.
  A cleaner peer-reviewed primary DOES exist and was located -- Friesen & Sapp
  (2007), "Mutual fund flows and investor returns: An empirical examination of
  fund investor timing ability", Journal of Banking & Finance 31(9), 2796-2816 --
  but the paper's own effect size was NOT read at source during this pass, only
  its citation, so no number from it is carried. -> A collection sprint should
  read Friesen & Sapp directly (and any newer dollar-weighted-return literature)
  and ship a properly bounded timing-cost item. Until then this lane has NO
  behaviour-gap number, and item 017 carries an explicit downgrade trigger for
  dollar-weighted-vs-time-weighted comparisons that ignore contribution timing.

- KR ETF WRAPPER COMPARISON (domestic-listed foreign-index ETF taxed as dividend
  income and swept into the 20m KRW financial-income aggregation threshold, with
  no loss offsetting, versus overseas-listed ETF taxed as capital gains with
  netting and the 2.5m KRW annual deduction). REFUSED for now, and this is the
  single highest-value hole in the lane for the Korean owner, because it is a
  live wrapper-choice decision rather than a background fact. It is stated
  consistently across brokerage and Big-4 tax publications, but no PRIMARY
  anchor was obtained in this pass: the statutory hook is 소득세법 시행령
  제26조의2 (집합투자기구로부터의 이익) read together with the dividend-income
  articles, and law.go.kr could not be fetched into a readable form here.
  -> A sprint should pull the article text from 국가법령정보센터 or an NTS
  guidance page and ship it with a verification date.

- KR PENSION-ACCOUNT TAX CREDIT (연금저축 600m KRW / combined IRP 900m KRW cap,
  16.5 pct credit at or below 55m KRW total salary and 13.2 pct above). REFUSED.
  Only brokerage and news sources were located; the statutory anchor is
  소득세법 제59조의3 and it was not read at source. These are exactly the
  parameters that move on the annual tax-revision cycle, so shipping them from
  secondary sources would bake in a number that rots silently. -> Same fix as
  above: read the article, ship with a verification date.

- KR SECURITIES TRANSACTION TAX RATE. DELIBERATELY NOT STORED, and this is a
  design decision rather than a gap to fill. The rate sits in 증권거래세법 제8조
  and 시행령 제5조 and has been amended repeatedly in recent years. Item 014
  carries the STRUCTURE that actually changes decisions (the tax is levied on
  the sale whether it is a profit or a loss, so turnover in Korean listed stock
  is taxed even when it loses money) and refuses the number. A future sprint
  should NOT "fix" this by adding the rate.

- SPIVA-STYLE ACTIVE-VS-PASSIVE BASE RATES ("N pct of active funds lag their
  benchmark over M years"). NOT SHIPPED. The scorecards are published by an
  index provider whose commercial interest is in the passive conclusion, which
  under this lane's own conflict-of-interest rule forces a downgrade, and the
  underlying primary was not independently obtained in this pass. The
  substantive conclusion a personal investing agent needs is already carried,
  and carried better, by finance-investing/active-arithmetic-cost-floor-001,
  which is an identity and cannot decay. -> If a sprint wants a persistence base
  rate specifically, it should go to the peer-reviewed persistence literature,
  not to a provider scorecard.

- MISSING-THE-BEST-DAYS, ONE-SIDED FORM. REJECTED as stated and shipped only in
  corrected form (item 009). The underlying measurement is real (Estrada 2008,
  15 markets, ~160,000 daily returns) but the circulating version quotes only
  the 50.8 pct downside from missing the best 10 days and suppresses the 150.4
  pct upside from avoiding the worst 10 days, which is the LARGER number in the
  same table. Any future item quoting this statistic in one direction is a
  regression.

- ADVISER MISCONDUCT, KR EQUIVALENT. NOT FOUND. Item 013 is a US measurement
  under a US disclosure regime (FINRA BrokerCheck) and is explicitly not
  generalised. No Korean equivalent dataset or regulator publication was
  located. -> Open jurisdiction hole; the practitioner-tier discount in item 017
  currently rests on US evidence only.

Coverage the lane implies but this pass does not supply:

- EMERGENCY-FUND SIZING. No item at any grade. The one lead carried over from
  the earlier finance research raw (a CFPB evidence review on savings-behaviour
  interventions) is about intervention effectiveness, not about how large a
  buffer should be, and its own claims failed the adversarial vote in that run.
  No defensible evidence base for a specific number of months was located.
  Recording the absence rather than filling it: there is no verified answer to
  "how many months of expenses", and the lane should say so.
- OPTIMAL REBALANCING FREQUENCY. Item 011 establishes what rebalancing IS (a
  risk-control policy with a concave payoff) and explicitly refuses to name a
  best schedule, because no primary establishing one was located. A sprint
  should look for controlled comparisons of calendar vs threshold rules before
  any frequency guidance is shipped.
- POSITION SIZING for an individual (as distinct from the diversification
  argument in item 003). Nothing verified; the popular material here is
  overwhelmingly practitioner heuristic and backtest.
- KR-SPECIFIC RETURN OR BEHAVIOUR EVIDENCE. Every behavioural item in the lane
  (007, 008) is a US brokerage dataset. Whether Korean retail investors show the
  same turnover penalty and panic-selling pattern is unmeasured here.
- TAX-LOSS HARVESTING under the Korean foreign-share regime. Item 015 carries
  the ingredients (losses are recognised, netting exists, the annual deduction
  does not carry forward) but no verified evidence on whether systematic
  harvesting adds value net of costs.

## task-management

Section opened 2026-09-02 (v22 lane opening, sixteen items 001-016). A NEW
domain: registry row, lanes.yaml row and all sixteen items land together, from
zero. The consumer is the agent that manages the owner's tasks and calendar
against real logged data, so this section is written from the position of
someone who has to answer a question against a real log tonight, not from the
position of a literature reviewer.

THE STRUCTURAL FACT ABOUT THIS DOMAIN, stated first because it governs
everything below: this is the warehouse's widest gap between popular authority
and evidential strength -- wider than relationships-communication, which
previously held that title. The reason is the transmission channel. In the
clinical domains the famous claims come from guideline bodies and can be checked
against a guideline. In the market domain they come from papers and can be
checked against a paper. Here they come from books that sell, and a book has no
obligation to carry a citation. Three of the most-repeated numbers in this
domain were traced during this sprint and turned out to have no primary source
at all. The refusal ledger below is longer than several domains' entire item
lists, and that is the sprint's main output, not a side effect of it.

WHAT LANDED, and what each row rests on:
- task-management/planning-fallacy-own-estimates-001 (B) -- Buehler, Griffin and
  Ross 1994, read in full text. Predicted 33.9 days against an objectively
  recorded 55.5; only 29.7% finished inside their own estimate. The half that
  does not survive retelling: instructing people to predict PESSIMISTICALLY
  moved the number without improving absolute accuracy (23.2 vs 22.6 days of
  error), and fewer than half finished even by their own worst case.
- task-management/reference-class-base-rate-002 (B) -- Flyvbjerg, Holm and Buhl
  2002, 258 projects, per-type figures read from the paper's own table. The
  operationally important half is the one that gets dropped: underestimation has
  not decreased over the seventy years the data covers.
- task-management/implementation-intentions-effect-shrinks-003 (B, contested) --
  Sheeran, Listrom and Gollwitzer 2024/2025, 642 tests. d = .36 raw, Egger's
  b = 1.06 meeting the published threshold for "substantial" publication bias,
  Robust Bayesian model-averaged d = .15. The famous d = .65 is superseded by
  the same authors who produced it.
- task-management/interruption-resumption-measured-004 (C) -- Mark, Gonzalez and
  Harris 2005, n = 24. 11 min 4 s per working sphere, 57% interrupted, 25 min
  26 s elapsed before same-day resumption with 2.26 intervening activities, and
  peripheral work resumed only 43.8% of the time against 82.0% for central work.
- task-management/momentary-interruption-error-cost-005 (B) -- Altmann, Trafton
  and Hambrick 2014. 4.4 s triples and 2.8 s doubles sequence errors, with
  non-sequence errors unaffected. The cost is a lost place, at a dose no time
  log can register.
- task-management/switch-cost-not-a-productivity-percentage-006 (B) -- the
  verified negative on the 40% claim.
- task-management/time-management-effect-modest-007 (B) -- Aeon, Faber and
  Panaccio 2021, 158 studies / 490 effects / 53,957 participants, figures read
  from Tables 4-7. Work performance r = .259 falling to .188 on trim-and-fill;
  wellbeing r = .313; life satisfaction r = .426 against job satisfaction .248.
- task-management/self-report-vs-log-divergence-008 (B) -- Parry et al. 2021.
  r = 0.38, and the figure that settles it: only 3 of 49 comparisons (6.12%)
  landed within 5% of the logged mean. Errors run both ways in equal proportion.
- task-management/record-is-not-behaviour-009 (B) -- Stone et al. 2002. The
  fence against reading an empty field as a fact.
- task-management/target-corruption-completion-metrics-010 (D) -- carried as a
  named hazard with no effect size, and with its own sourcing limit stated in
  the item.
- task-management/zeigarnik-recall-refuted-011 (B) -- Ghibellini and Meier 2025,
  1,455 publications screened to 59.
- task-management/breaks-wellbeing-not-performance-012 (B) -- Albulescu et al.
  2022 plus Biwer et al. 2023.
- task-management/procrastination-predictors-013 (C) -- Steel 2007, 691
  correlations.
- task-management/goal-setting-side-effects-contested-014 (D, contested) -- a
  live published dispute, recorded rather than adjudicated.
- task-management/no-block-length-or-task-count-evidence-015 (D) -- deliberate
  absence row.
- task-management/curator-checklist-016 (D) -- the lane's grading rule.

STILL OPEN -- each searched this sprint and deliberately left unfilled rather
than filled with something plausible:
- KOREAN DATA. Zero. This is the lane's largest structural hole and the mandated
  locale check came back empty. A targeted search located exactly one
  Korean-primary source in this domain -- a translation and validation of
  procrastination scales in a student and community sample -- and it is a
  measurement instrument rather than a finding, and it could not be retrieved in
  this pass (the publisher refused automated retrieval), so nothing from it is
  asserted anywhere. No Korean behavioural or intervention study on task
  management, estimation, interruption or work scheduling was located at all.
  Every substantive row in this lane is therefore Western-sampled and its
  transfer to a Korean adult is UNTESTED, not shown to fail. WHAT WOULD CLOSE
  IT: any Korean or East Asian primary study with a behavioural outcome in this
  domain; failing that, a retrieval of the scale-validation paper would at least
  establish that the constructs measure the same thing in Korean, which is the
  minimum precondition for transferring anything else.
- THE MEASUREMENT FLOOR FOR TASK TIME SPECIFICALLY. Item 008 is the best
  available estimate of how far a person's estimate of their own time use sits
  from a machine record, and it measures DIGITAL MEDIA USE. No equivalent
  paired self-report-versus-log study for WORK time was located. This is the
  floor the whole lane rests on and it is currently borrowed from an adjacent
  behaviour. WHAT WOULD CLOSE IT: a study pairing self-reported task duration
  against an objective work log (calendar telemetry, IDE or document
  timestamps, or an instrumented time tracker) in adults.
- WHETHER ANY TASK-MANAGEMENT SYSTEM WORKS. There is no trial of a named
  method. Item 007 is a correlational synthesis of "time management" as an
  unspecified family of self-reported habits -- its authors note explicitly that
  studies often do not say what was taught. So the domain can say that people
  who report managing their time are modestly better off, and cannot say that
  adopting any particular system causes that. WHAT WOULD CLOSE IT: a randomised
  trial of a defined system against an active control with a behavioural
  outcome. None was located for GTD, for any matrix method, or for any
  commercial task system.
- LONG-HORIZON PROJECT ESTIMATION FOR INDIVIDUALS. Item 001's horizon is a few
  weeks and item 002's subject is public infrastructure. Nothing was located
  measuring an individual's estimation error on multi-month personal projects,
  which is the horizon a project store actually holds. Not inferred across.
- WHAT AN UNRESUMED ITEM MEANS. Item 011 establishes that interrupted tasks are
  resumed about 67% of the time in laboratory conditions and item 004 that
  peripheral work is resumed the same day only 43.8% of the time in the field.
  Neither licenses a threshold for when a stalled item in a real store should be
  surfaced. No source prescribing such a threshold was located, and none was
  invented.
- ATTENTION RESIDUE. Named in passing in the interruption literature and
  untouched by this sprint. Flagged as a likely future refusal rather than as
  one -- no source was researched for it this pass.

Rerun-needed: two, both recorded rather than papered over. Bevan and Hood 2006
and Campbell 1979 were resolved to publisher records and their positions
verified, but their full texts were NOT retrieved; item 010 states this in its
own frontmatter and quotes no figure from either. The three papers in the
goal-setting exchange (item 014) were likewise verified as citations and
positions only. Every other source in this lane was read in full text.

## learning-habits

Section opened 2026-09-02 by the study-craft lane opening (v23). The domain
had shipped 13 items since the seed conversion and had never had a GAPS section
of its own -- itself a gap, since it is one of the older domains in the
warehouse. This release adds a SECOND lane, @study-craft (VC-E), and 8 items.
No registry change: learning-habits keeps its prefix and its two aliases
(skill-learning, habits-behavior-change), and none of the 13 existing items was
edited.

WHY A CRAFT LANE HERE. Before this release, exercise was the only domain in the
warehouse with a practitioner-craft lane sitting beside its evidence lanes.
Every other domain except cooking had exactly one lane, and that lane was the
evidence lane. For learning-habits the consequence was concrete: the domain
could say that spacing and retrieval practice work, and could say that rereading
and highlighting do not, and could say nothing at all about how to run a
practice. What schedule to keep, what to do about the fortnight you missed, what
a wasted rep looks like, how much material you can take in without burying
yourself, when a session is over. None of that is in a paper. The training
domain had answers for all of it and this one had none.

WHAT THIS LANE LOOKS LIKE, AND WHY IT IS NOT A LICENCE. VC-E is a different
standard, not a lower one, and this is the hardest domain in the warehouse in
which to hold that line -- study advice is an ocean of confident unsourced
assertion, and unlike the clinical lanes the folklore here is usually not even a
distorted version of a real finding. The lane was run on three rules. Every item
names its basis and marks its epistemic status. Where a claim is an inference
from a study's design rather than a measurement, it is labelled as an inference
in the item itself. And nothing ships because it is widely repeated: the
rejected-claim ledger for v23 in the cross-cutting section below is
longer than the shipment, which is the honest ratio for this subject matter.

One methodological note worth carrying forward. An automated summary of one
primary in this sprint (Cepeda et al. 2008) came back describing it as a
meta-analysis when it is a single 1354-subject experiment. Every figure in this
release was consequently taken from a direct read of the source document. The
lesson generalises: in a domain this heavily summarised, a summary of a primary
is not a primary.

WHERE THIS LANE CONTRADICTS THE DOMAIN'S OWN EVIDENCE LANE. Recorded here
because a later sprint must not quietly pick a side.

- Grading by feel. The evidence lane rates rereading and highlighting LOW
  utility precisely because they produce a sense of fluency without durable
  learning (item 011). The dominant craft grading habit reaches for that same
  signal -- work it until it feels smooth; mark it "hard" rather than failed
  when recall was slow but arrived. Item 016 refuses felt-smoothness as a
  session signal and says outright that the craft habit is reaching for a signal
  the evidence lane has already discredited.
- Vocabulary systems and fluency. Language craft routinely promises that a
  spaced vocabulary system produces the ability to speak. Item 013 establishes
  that the technique literature is dominated by surface outcomes (d=0.60) with a
  far weaker and far thinner deep-learning estimate (d=0.26, N=109). The craft
  over-claim is contradicted by this warehouse's own evidence, not merely
  unsupported by it. Item 019 therefore ships the boundary as its main product
  and the finding as secondary.
- Daily writing. Items 005 and 006 cap what accumulated practice explains at
  about 12 percent of performance variance overall and about 1 percent
  (non-significant, p=.377) in professional skill -- which is exactly the
  population the "write every day" rule is sold to. Item 020 names the conflict
  and shows that the rule's own evidence base does not survive a reading of the
  papers.
- The cost of a missed day. Craft devices built on streaks price a lapse as a
  catastrophe. The two measurements in item 015 -- the overshoot asymmetry and
  savings on relearning -- both price it cheap. This is a case where the
  folklore is not merely unsupported but pointed in the wrong direction, and the
  person it misdirects is the one deciding whether to come back.

### Searched and not closed -- @study-craft

- ANY TRIAL OF ANY PRACTICE PROTOCOL. This is the lane's defining hole and it
  should be stated first. No study was located comparing backlog-recovery
  strategies, item-reformulation against continued drilling, intake policies,
  session lengths, or stop conditions -- on any outcome, at any tier. The
  spacing and retrieval literature tests INGREDIENTS under experimenter control;
  nobody has tested the assembled practice a person actually runs. Every
  procedural item in this lane is consequently at the practitioner band, and
  that is a property of the field, not of the sprint.
- KOREAN ANYTHING. Every source in this lane is anglophone. No Korean study of
  study practice, no Korean-language-learner spacing measurement, and nothing on
  whether Korean study culture's characteristic patterns change any of it. Same
  structural hole the spending-saving and relationships lanes record.
- LOG COMPLETENESS AND ADHERENCE DECAY. Nothing was located measuring how a real
  person's study schedule adherence decays over weeks and months, which is the
  number an agent needs to tell a genuine drop in practice from a drop in
  logging. -> This may be measurable from the instance's own data rather than
  from literature, exactly as the spending lane records for its ledger.
- OPTIMAL SCHEDULES, AS OPPOSED TO OPTIMAL GAPS. Item 014 rests on a two-session
  gap experiment. Nothing was located that tests a multi-month, many-item
  schedule of the kind a scheduler actually runs. -> A sprint could look for
  classroom-scale distributed-practice trials and ship a properly bounded item,
  or record why not.
- PRODUCTION AND FLUENCY IN LANGUAGE. Item 019 deliberately stops at the lexical
  layer. Nothing is shipped on comprehensible input, output practice, shadowing,
  or conversation frequency, because no primary was read at source in this pass.
  This is the largest content hole in the lane relative to the owner's actual
  area. -> A sprint should read the applied-linguistics primaries directly;
  there IS a real literature here and this pass simply did not reach it.
- VOCABULARY SIZE AND FREQUENCY COVERAGE. The applied-linguistics work on how
  much of a text a given vocabulary size covers is a real and directly relevant
  body of research, and would sit in the @behavioral lane rather than this one.
  Not researched this pass. Recorded so the absence is not mistaken for a
  judgment.
- LEARNING STYLES / MODALITY MATCHING. Not researched this pass and not shipped
  in either lane. It is a famous refutation and it belongs in the @behavioral
  evidence lane, not here. Recorded so a later sprint does not assume the
  warehouse has already covered it. It has not.
- INTERLEAVING. Not shipped. It sits next to spacing in the same literature, has
  its own trials, and is arguably the third technique a practice item would want
  after spacing and retrieval. No primary was read at source in this pass. ->
  Evidence-lane work, for @behavioral.

Rerun-needed: none. Every source used in this release was read at source
(publisher DOI, an author copy, an institutional repository copy, or the
application's own manual), and where a mirror was read rather than the
publisher, the mirror URL is listed on the item alongside the DOI.

## leisure

Section opened 2026-09-02 (v24 collection sprint, twelve items 001-012).
New domain -- the owner's own taxonomy unit 여가, opened at his direction so the
modules are designed from his view of his life. Both of his areas under it were
at zero items: 문화생활 (id 8, "문화적 인풋과 아웃풋") and 취미 (id 19, "밴드, 술, ...").
Three lanes, one more than he has areas, because his 취미 contains two evidence
bases with different verification cultures (see lanes.yaml).

READ THIS SECTION AS THE SPRINT'S PRIMARY OUTPUT ALONGSIDE THE ITEMS. This is
one of the worst domains in the warehouse for replication failure, and the
sprint ran on the stated rule that refusing a famous claim with a reason beats
shipping it. The rejected-claim ledger for this sprint, in the cross-cutting
section below, is longer than the item list. Of twelve items, two are outright
refutations of famous claims (001, 002), SIX carry `contested` (003, 004, 008,
009, 010, 011), one is a deliberate absence row (008), one is a measurement rule
(005), one is the domain checklist (012), and exactly ONE states a clean positive
actionable finding (006). That is the correct shape for this domain rather than a
shortfall in it.

WHAT LANDED, by lane:

@cultural-life (VC-C) -- 문화생활, input and output together:
- leisure/mozart-effect-refuted-001 (A/B) -- Pietschnig 2010 (~40 studies,
  >3000 subjects, d=0.37 on one spatial task, publication bias, effects several
  times larger in the originating lab) plus Oberleiter 2023 on the epilepsy
  spin-off (k=8, N=207). The lab-affiliation result is the generalisable part.
- leisure/music-training-transfer-null-002 (A) -- Sala & Gobet 2020, 254 effects
  / 54 studies / N=6984. Null once design quality is controlled; the positive
  effect exists ONLY without randomisation and without active controls. The
  strongest single item in the domain, and it is a refutation.
- leisure/fiction-social-cognition-small-003 (A/B/D, contested) -- the famous
  single-passage result failed a 792-participant three-group replication; the
  pooled experimental effect survives at g=0.15-0.16 on a photographs-of-eyes
  test; the real-life empathy claim is unmeasured by anyone.
- leisure/arts-engagement-mortality-confounded-004 (B/D, contested) -- Fancourt
  & Steptoe 2019, n=6710, 14 years, HR 0.69. Carried with its published JECH
  commentary and with the BMJ Christmas-issue placement disclosed.
- leisure/self-report-measurement-005 (B/C) -- Kan & Pudney 2008 within-
  respondent stylized-versus-diary comparison; non-classical error; DRM as the
  remedy. Upstream of everything else in the domain.
- leisure/curator-checklist-012 (A, synthesis) -- six gates, a disposition rule,
  and a tone rule.

@hobby-practice (VC-C) -- 취미 as skill, time and recovery:
- leisure/skill-decay-nonuse-006 (B/C) -- Arthur 1998, 189 data points from 53
  articles, d=-0.01 immediately to d=-1.4 after 365+ days; physical and
  speed-based tasks decay less than cognitive and accuracy-based ones. The
  domain's one clean actionable positive.
- leisure/vacation-recovery-fadeout-007 (C) -- de Bloom 2009, k=7. Small
  benefit, quick fade-out, and the moderator everyone cares about unstudied.
- leisure/flow-effortful-leisure-thin-base-008 (D/E, contested) -- deliberate
  absence row.

@drinking-epidemiology (VC-B) -- 술:
- leisure/alcohol-jcurve-collapse-009 (B/B/C, contested) -- the current state,
  not the 2015 consensus.
- leisure/kr-aldh2-flushing-010 (B/C/E, KR, contested) -- the locale row.
- leisure/alcohol-cognition-uncertain-011 (B/C/E, contested) -- unresolved, and
  the analytic choice that decides it is named.

OPEN WANTS, in rough order of how much a live session would feel their absence:

1. KOREAN DRINKING GUIDELINES AND UNITS. The highest-value missing item in the
   domain and the sprint's clearest failure. Korean drinking norms, the local
   standard-drink convention, and 음주 문화 differ from the Western literature's
   assumptions, and a Korean official low-risk-drinking guideline could not be
   sourced this pass to a document with a resolvable citation. Every gram-per-day
   threshold currently in this domain is therefore stated in grams of ethanol
   rather than in 잔, which is not how anyone actually counts. What would close
   it: the Ministry of Health and Welfare / KDCA 절주 guideline read at the issuing
   body's own site, or a peer-reviewed Korean paper stating the national unit
   convention. Same discipline the cooking lane adopted after a US-only rule was
   dropped from it: a Western regulatory fact is not a Korean regulatory fact.
2. KOREAN DRINKING PREVALENCE AND HIGH-RISK-DRINKING BASE RATES. KNHANES
   publishes 월간음주율 and 고위험음주율 annually. Nothing in this domain currently
   states what ordinary Korean drinking looks like, so an agent has no base rate
   to place a user against. Searched this pass and not resolved to a citable
   primary; recorded rather than guessed.
3. ALCOHOL AND SLEEP. The single most practically useful drinking question for a
   life agent, and entirely absent. The sleep-recovery lane exists and is mature;
   this is a cross-lane item that should be authored once and linked, not
   duplicated. Not researched this pass.
4. ACTIVE VERSUS PASSIVE LEISURE, PROPERLY. Item 008 records that the evidence is
   one 1989 study of 78 people. If a modern experience-sampling or ecological
   momentary assessment literature with adequate n exists, it would convert the
   domain's biggest absence into its most useful item. This is the highest-value
   research target here.
5. A POST-1998 SKILL-RETENTION SYNTHESIS. Item 006 rests on a meta-analysis that
   is 27 years old. Nothing newer was located. The direction is not in doubt; a
   modern pooling would let the moderator pattern be stated with more confidence
   for recreational rather than occupational samples.
6. GROUP AND ENSEMBLE PARTICIPATION. The owner's 취미 explicitly includes playing
   in a band, which is a social activity as much as a musical one. Whether the
   ensemble part carries anything the solo part does not is unexamined here, and
   the relationships-communication lane's social-connection items are the obvious
   neighbours. Not researched this pass.
7. HOBBY ENGAGEMENT AND COGNITIVE AGEING. A large observational literature exists
   and was deliberately not opened, because on gate 1 of this domain's checklist
   it is the exposure-is-a-proxy-for-being-well problem in its purest form and
   would need careful handling rather than a quick pass.
8. SCREEN AND CONSUMPTION TIME. Not researched. Note that item 005 predicts the
   self-report problem will be worse here than anywhere else in the domain,
   because the respondent must first decide what counts.

## skincare-hygiene

Added 2026-09-02 (v25 skincare-hygiene domain opening). The domain did not
exist before this release: area 16 under the owner's 건강 domain, 스킨케어/위생,
held zero items while its sibling areas were covered. Fifteen items opened it.

Two lanes, two evidence standards, and they must not be blended:
- @clinical-derm (VC-A) takes randomised controlled trials, Cochrane and other
  systematic reviews with named methodology, GRADE-style certainty ratings, and
  blinded outcome assessment. A cosmetic-journal single-product trial is not this
  standard. A brand's own data on its own product is never this standard.
- @cosmetic-regulatory (VC-F) takes the national instrument itself -- 화장품법,
  its 시행규칙 and annexes, and the 식약처 고시 governing functional-cosmetic
  review, labelling and advertising substantiation -- quoted with its instrument
  number and effective date. A VC-F item is definitive about what a rule SAYS and
  silent about whether the regulated thing WORKS.

THE DOMAIN'S GOVERNING HAZARD, stated once so every later pass inherits it. This
is the most commercially captured subject matter in the warehouse. Nearly every
claim in circulation originates with a party selling the thing, the endpoints are
unusually soft, and there is a whole second class of statements -- regulatory
permissions -- that read like efficacy findings and are not. The operating rule
adopted here, and inherited from the v16 relationships sprint, is that refusing a
famous claim with a stated reason beats shipping it.

CLOSED by v25 (fifteen items, 001-015): the domain's first content. The
clinical lane now carries what the only randomised sunscreen trial actually
showed including its nulls (001), the gap between labelled and applied sunscreen
quantity (002), the FDA systemic-absorption trials and what they do and do not
establish (003), the sunscreen-and-vitamin-D discordance (004), the Cochrane
individual-participant-data failure of prophylactic emollients (005), the
hand-washing effect size (006), what the retinoid evidence covers and where it
stops (007), the placebo-response measurement floor (008), oral collagen as a
contested claim (009), an explicit cleansing-frequency absence row (010) and the
domain's curator checklist (015). The regulatory lane carries the 기능성화장품
category and its pre-market gate (011), Korean SPF/PA labelling conventions (012),
the closed waived-dossier active list (013) and the prohibition on advertising a
cosmetic through a doctor (014).

OPEN -- searched in this sprint and deliberately refused rather than shipped:

- COLLAGEN SUPPLEMENT EFFECT SIZE. A real systematic review and meta-analysis
  exists with a resolvable DOI (19 randomised double-blind trials, 1,125
  participants, 95 percent women) and reports favourable pooled results, so the
  claim ships as item 009 marked contested. What was NOT obtained is the full
  text, and therefore the funding sources of the 19 pooled trials, their
  individual risk-of-bias ratings, and whether any publication-bias analysis was
  performed. No claim about industry sponsorship of those trials is made here,
  because asserting one unread would be the same offence as the marketing it
  guards against. No pooled effect magnitude is carried anywhere. What would close
  it: the full text of that review, read for funding and risk of bias, or an
  independent synthesis with a stated conflict-of-interest analysis.

- THE 10-STEP ROUTINE, and every claim about routine LENGTH or step ORDER.
  Searched; zero primary sources exist for a comparison of routine lengths or
  layering orders against any endpoint. Refused outright. This is not shipped even
  as an absence row because, unlike cleansing frequency, no specific number is at
  risk of being generated -- but any future pass meeting a step-count claim should
  read this line before treating it as established.

- CLEANSING AND SHOWERING FREQUENCY. Searched 2026-09-02 for randomised evidence
  on face-washing frequency (including twice-daily cleansing against acne
  outcomes) and on bathing or showering frequency against skin-barrier outcomes in
  healthy adults. Zero eligible primaries. SHIPPED AS AN EXPLICIT ABSENCE ROW
  (010) rather than left silent, on the model of
  relationships-communication/contact-cadence-no-evidence-014, because the
  question is asked constantly and a plausible number is available in unlimited
  supply from unsourced internet text. What would close it: a randomised or
  crossover trial comparing defined washing frequencies against an objective
  barrier or lesion endpoint.

- SKIN-MICROBIOME COSMETIC CLAIMS. Searched. Every result located was a branded
  single-product trial in a cosmetic-dermatology journal or a study of a medical
  intervention in atopic dermatitis, neither of which supports a general
  microbiome-balancing claim for a consumer product. Refused. What would close it:
  a systematic review of microbiome-directed cosmetic interventions against a
  clinical endpoint, with a stated funding analysis.

- TOPICAL VITAMIN C AT CONSUMER CONCENTRATIONS as an anti-aging claim. No
  independent RCT-grade source was located. Note the regulatory asymmetry that
  makes this easy to misread: several ascorbyl derivatives DO appear on the
  Korean waived-dossier list (item 013), but they are registered there for the
  MELANIN claim, at fixed concentrations, and a dossier waiver is not an efficacy
  finding in any case. Refused.

- "DERMATOLOGIST TESTED" AS A QUALITY SIGNAL. No regulation read in this pass
  defines the phrase, and no standard specifying what such a test must consist of
  was located. Refused as an efficacy signal. Item 014 ships the regulatory fact
  that IS retrievable and is more useful: under 화장품법 시행규칙 별표 5 제2호 다목
  it is prohibited in Korea to advertise a cosmetic on a medical professional's
  endorsement, recommendation, designation, guidance, research, development or
  use, with one narrow literature-citation exception.

- PEPTIDES, GROWTH FACTORS, EXOSOMES and the aesthetic-active category generally.
  Searches returned narrative reviews, small split-face trials paired with
  procedures, and aesthetic-practice literature. No independent synthesis with a
  stated methodology was located. Refused.

- THE "REAPPLY SUNSCREEN EVERY TWO HOURS" INTERVAL. A labelling and regulatory
  convention; no primary measurement supporting that specific interval was located
  in this pass. It is not asserted anywhere in this release. Note that the one
  reviewed source that does make a reapplication recommendation proposes a
  DIFFERENT shape -- apply before exposure and reapply once within the first hour
  -- and states it as the authors' own suggestion rather than as a measured
  result. Item 002 carries it that way.

- THE US REGULATORY COMPARISON. The obvious follow-on to items 011 to 014 is how
  the Korean 기능성화장품 structure differs from the US arrangement, where
  sunscreens are handled as over-the-counter drugs and most other cosmetic claims
  are not pre-cleared. DIRECT RETRIEVAL OF THE RELEVANT fda.gov PAGES FAILED in
  this pass -- repeated HTTP 404 on the cosmetics-authority and cosmetic-versus-drug
  pages. Nothing was quoted from them and no US regulatory fact is asserted
  anywhere in this release. This is the same discipline the cooking lane adopted
  in v15 after a US-only cooking rule was dropped from it, applied in the opposite
  direction. What would close it: a directly retrieved fda.gov or eCFR primary.

- KOREAN CLINICAL AND EPIDEMIOLOGICAL EVIDENCE FOR THIS DOMAIN. All four KR items
  in this release are REGULATORY. No Korean dermatology cohort, no Korean
  photoprotection behaviour survey and no Korean skin-cancer incidence data were
  researched. The entire clinical half of this domain rests on Australian,
  European, UK, US and multi-national samples, and whether any of it transfers to
  Korean skin phototypes and Korean sun-exposure patterns is UNTESTED, not shown
  to fail. This is the single most valuable thing a next sprint could close.

- FITZPATRICK PHOTOTYPE AS A CONDITIONING VARIABLE. The Korean SPF test protocol
  itself selects subjects of Fitzpatrick types I, II and III (item 012's source
  annex), while the Korean population is predominantly type III to IV. Whether the
  labelled protection transfers across that gap was not researched. Flagged
  because it is a question the regulatory text itself raises.

- HAND HYGIENE AND RESPIRATORY INFECTION. Item 006 covers diarrhoeal illness only.
  The respiratory hand-hygiene literature is separate, considerably more
  contested, and was NOT researched in this pass. Its absence is a not-yet-asked.

Edition-check debt, inherited from the v13 staleness lesson and the v15 cooking
application of it: every regulatory instrument cited in this release was retrieved
from the national law database with its instrument number and effective date
attached, and all four were revised within the last year (시행규칙 총리령 제2109호
시행 2026-04-02; 고시 제2025-88호 and 제2025-89호 both 2025-12-16; 별표 5 개정
2025-08-01). That currency is recorded as verified-at-retrieval on 2026-09-02, not
as permanent. Korean cosmetic regulation moves on a fast cycle and a
jurisdiction-bound item needs an EDITION check before every reuse, exactly as the
finance lane's Korean tax items do.

Structural gap, axes: only two of the fifteen items carry applicability.axes.
Item 007 attaches pregnancy_status as a hard SAFETY axis with block_specifics,
which is a genuine and correct use of the ledger -- a retinoid question with
unknown pregnancy status should withhold specifics. Everything else in the ledger
is fitness-shaped (training status, one-rep max, body composition, sleep
baseline) and nothing in it conditions a photoprotection or cosmetic-regulation
claim. The axes this domain would actually refract on -- Fitzpatrick phototype,
typical daily ultraviolet exposure, whether the user has a diagnosed skin
condition, current topical or systemic medication as it bears on photosensitivity
-- either do not exist in the ledger or exist aimed at a different question.
Adding them is an append-only ledger change and was deliberately NOT attempted in
a content-only release. Flagged for whoever owns the skincare module design.

Rerun-needed: none. Every clinical source in v25 was retrieved through the
PubMed E-utilities record with a resolvable DOI, and every Korean regulatory
source was retrieved directly from the 국가법령정보센터 open interface at law.go.kr
as XML or as the ministry's own PDF annex, and quoted verbatim. One retrieval
FAILED and is recorded above rather than worked around: the US regulator's pages.


## travel

Opened v26 (2026-09-02) with 10 items across two new lanes,
@travel-clinical (VC-A) and @travel-advisory (VC-F), both appended to lanes.yaml
in the same pass because travel had no row in either ledger beforehand. The
structurally notable part is not that it is new but that it is SPLIT: travel is a
two-lane, two-verification-culture domain, which in this warehouse only cooking
and exercise otherwise are. The clinical half and the jurisdictional half are
answerable by different kinds of source and fail in different ways, and grading a
statute on a clinical-trial ladder would be a category error.

What the opening sprint covers: the standing jet-lag guideline and its grading
ladder, light timing including the wrong-direction risk, flight-associated venous
thromboembolism in relative AND absolute terms, compression stockings and their
endpoint gap, the cabin-air folklore, travellers' diarrhoea prevention and
severity structure, the Korean travel-ban legal gate, the Korean pre-travel
route, and an explicit altitude gate row carrying no numbers.

DOMAIN BOUNDARY, checked at authoring time rather than assumed. The owner's life
taxonomy places 여행 as an area under 여가, and a `leisure` domain was opened in
this warehouse concurrently with this sprint. The two were compared: leisure's
lanes are @cultural-life, @hobby-practice and @drinking-epidemiology, and its
items are about arts engagement, music, flow, skill decay and alcohol. There is
NO content overlap and no lane collision. The one adjacent row is
leisure/vacation-recovery-fadeout-007, which is a well-being finding about
holidays rather than a travel-health one. Whether travel should eventually be a
sub-area of leisure in the registry is a modelling question for the warehouse
owner; it was NOT decided here, and the registry's merge machinery
(merged-into + alias redirect) exists precisely so that decision can be taken
later without a prefix ever being reused. Do not silently fold one into the
other.

WANTED NEXT, in rough order of how often a live session would hit it:

- THE ALTITUDE GUIDELINE, READ PROPERLY. Item 010 is a deliberate gate row and
  says so. What closes it: the WMS 2024 update (Wilderness Environ Med
  35(1_suppl):2S-19S, doi 10.1016/j.wem.2023.05.013) read at full text for two
  things -- the risk-stratification categories, and the graded ascent
  recommendation with its ACCP strength and evidence-quality labels carried as
  issued. The publisher page and the society's own summary both refused
  retrieval in this pass (403 on both). Secondary summaries of the ascent rate
  were seen and NOT taken. This is the lane's highest-value missing item.
- MOTION SICKNESS. Not researched at all in this pass, and it is a high-frequency
  practical question. There is a real Cochrane-tier literature here and none of
  it was read. Nothing should be said about it from memory until it is.
- 검역감염병 오염지역 -- THE DESIGNATION MECHANISM, NOT THE LIST. Item 009 covers
  the pre-travel route but not how Korea designates contaminated areas, what
  designation obliges a returning traveller to do beyond the Q-CODE, or how the
  list is revised. The LIST itself must never be carried; the mechanism should
  be.
- A KOREAN AUTHORITY WORDING FOR FOOD AND WATER PRECAUTIONS. Item 006 refutes the
  incidence claim and deliberately quotes NO Korean regulator wording, because
  none was captured verbatim in this pass. The two-level handling this warehouse
  uses -- report the instruction as the instruction, report the evidence
  separately -- needs the instruction actually quoted to be complete.
- INSECT-BORNE DISEASE AS A DECISION STRUCTURE. Dengue, malaria and Japanese
  encephalitis risk by destination, and repellent/net evidence. Only touched
  here through the KDCA lead-time item. The repellent literature in particular
  looks like it has real trials behind it and none were read.
- SLEEP ON THE AIRCRAFT, as distinct from circadian adjustment. Whether anything
  done in the seat affects arrival state, and specifically whether the
  sleep-loss-performance literature the sleep domain already carries transfers to
  a travel day. Not researched.
- LONG-HAUL FLIGHT AND EXISTING CONDITIONS. Cabin pressure altitude and its
  implications for people with respiratory or cardiac conditions; fitness-to-fly
  frameworks. Genuinely important, entirely absent, and the one area of this
  domain most likely to need a hard route-to-a-clinician rather than an item.
- TRAVEL INSURANCE. The task that opened this lane flagged travel-insurance risk
  framings as suspect folklore. A search for a usable source returned only a
  large undifferentiated literature with nothing addressing the framings
  themselves. Nothing was shipped in either direction. Recorded as a likely
  future refusal rather than as one.

OPEN -- searched in this sprint and deliberately refused rather than shipped:

- HYDRATION AND JET LAG. A targeted search for any primary study measuring a
  hydration intervention against a jet-lag endpoint returned nothing usable; the
  handful of hits were a case report and an athlete review. The claim that
  drinking water reduces jet lag has no primary source located here, and no
  magnitude was shipped in either direction. This is an ABSENCE, not a
  demonstrated null.
- THE ANTI-JET-LAG DIET. A search for a randomized or controlled trial of a
  jet-lag diet or feeding-schedule protocol returned exactly one paper, and it
  was a bright-light study. Refused outright. The feeding-as-zeitgeber
  literature in animals is real and is NOT the same claim.
- ASPIRIN OR ANTICOAGULANTS FOR FLIGHT VTE. The only randomized evidence located
  is from a single research group publishing a series in one journal, which is
  not a base this warehouse builds on. It is also outside the medical-advice
  boundary this lane holds. Refused on both counts.
- CABIN HUMIDITY AS A HEALTH EFFECT. Searched; the hits were about cabin
  environment generally and none measured a health endpoint attributable to
  humidity. Nothing shipped.
- ANY 여행경보 COUNTRY LIST. Deliberately not carried in any form. It changes with
  events and is the ministry's to publish. Item 008 exists to make a session go
  and look rather than recall.

AXES LEDGER GAP (the same complaint the cooking and relationships sprints
recorded, now with travel-specific instances). The core axes ledger is
fitness-shaped. The axes this lane actually wants do not exist: destination
time-zone offset and direction, flight duration, itinerary maximum altitude, and
a prior-VTE flag distinct from the generic cardiovascular_condition safety axis.
Items here therefore lean on cardiovascular_condition, pregnancy_status,
medication_list, allergen_list, chronotype and sleep_baseline_hours, which is a
workable but coarse fit. Adding travel axes is an append-only ledger change and
was NOT made in this pass.

Rerun-needed: item 010, and only item 010. Every other source in this sprint was
read either at its PubMed record or at full text, and the Korean statute was read
from the national legal information service's own machine-readable record rather
than from any explanatory page. Item 008 additionally needs a scheduled re-check
rather than a rerun: it quotes a penalty that changed on 2026-08-28, and any
future amendment to 여권법 제17조 or 제24조 invalidates it.

## cat

Section opened 2026-09-02 (v27 collection sprint, thirteen items 001-013).
NEW DOMAIN: new registry prefix `cat`, three new lanes (@clinical-vet VC-A,
@companion-ethology VC-C, @vet-regulatory VC-F). The domain went 0 -> 13.

WHY THE DOMAIN IS SHAPED THIS WAY. The owner filed this area under his
RELATIONSHIPS domain, not under pets or household upkeep -- his cat is a member
of the household he has a relationship with, not an object of maintenance. That
filing drove three content decisions worth recording so a later sprint does not
undo them: the slug is `cat` rather than `cat-care`, because a stable ID prefix
named after the maintenance activity would bake the rejected framing in
permanently; the cat-human attachment question gets its own row even though it
settles nothing, because it is the direct evidential test of the filing; and
"cats are low maintenance" is refuted head-on rather than left alone.

THE STRUCTURAL FACT ABOUT THIS DOMAIN, which every gap below inherits:
veterinary evidence is materially thinner than human medicine. The intervention
studies used in this sprint run 6, 9, 16, 28, 46 and 54 animals. There is no
formal evidence-grading body for feline practice comparable to the anchors the
sleep-recovery and mental-health lanes use, and the professional guidelines
state in their own text that parts of them are clinical experience. This is why
cat/curator-checklist-001 was shipped FIRST and why the domain's ladder puts a
jurisdictional legal fact ABOVE any clinical one. That inversion is not a
stylistic choice; it is where the certainty actually is.

WHAT LANDED:
- cat/curator-checklist-001 (D) -- the grading rule. Lower ceiling, the ladder,
  the auto-refusal triggers, the manufacturer-funding carry, and the absolute
  scope boundary (no diagnosis, no dosing, no treatment protocols, at any
  confidence level).
- cat/dietary-water-urinary-dilution-002 (C/D, contested) -- the domain's most
  actionable claim. Food moisture, urine dilution and calcium oxalate
  supersaturation, across Buckley 2011 (n=6), Markwell 1999 (n=54, 18 vs 28
  arms) and Segev 2011 (82 vs 82 case-control). Contested on FUNDING: both
  controlled studies come from a pet-food manufacturer's research centre and
  support a conclusion about a category that manufacturer sells.
- cat/water-bowl-type-null-003 (C/D) -- the fountain. Robbins 2019 (16 cats,
  randomised crossover, three bowl types, nothing significant on intake, urine
  volume, USG or RSS; osmolality significantly HIGHER on the circulating bowl)
  and Pachel and Neilson 2010 (9 cats, not significant). Individual preference
  appears in both and is the actionable half.
- cat/body-condition-lifespan-004 (B/C/D, contested) -- Teng 2018, 2,609 cats,
  per-band hazard ratios against BCS 6: score 3 HR 4.67, score 4 HR 2.61, score
  5 HR 1.43, score 9 HR 1.80. The THIN end carries more than double the fat-end
  hazard and the conventional "ideal" of 5 is raised. Corroborated in shape by
  Teng 2024 UK life tables (7,936 deaths).
- cat/urinary-obstruction-same-day-005 (C/D) -- severity profile only. Segev
  2011: 8.5% mortality, 22% recurrence at 6 months, 24% at 2 years.
  Duperrier-Simond 2024: cardiovascular events in 61.9% of 168 cats.
- cat/pain-observable-grimace-scale-006 (B/D) -- Evangelista 2019, five facial
  action units, inter-rater ICC 0.89 (CI 0.85-0.92), rho 0.86 against an
  established instrument. Kills "cats hide pain, you can't tell" for acute pain.
- cat/lily-nephrotoxicity-007 (B/D) -- Rumbeiha 2004, experimental rather than
  case-report-derived; acute necrosis of proximal convoluted tubules.
- cat/milk-lactase-decline-008 (C/D, contested) -- Kienzle 1993: lactase 96+/-66
  U/g protein in newborns to 13+/-9 at six weeks, and diet had NO effect on
  enzyme activity, which is the direct answer to "the cat has had milk for years".
- cat/declawing-associated-harm-009 (C/D, contested) -- Martell-Moran 2018, 137
  pairs. The retained-bone-fragment subgroup (63% of declawed cats) is what
  defeats the confounding-by-indication objection.
- cat/attachment-contested-010 (C/D, contested) -- Vitale 2019 against Potter
  and Mills 2015. Opposite conclusions, both small, both using methodology
  borrowed from human infant research.
- cat/five-pillars-framework-011 (C/D) -- the AAFP/ISFM environmental needs
  framework, real and published, consensus and not trial-tested. Buffington 2006
  (46 cats, NO control group) is the closest thing to intervention evidence.
- cat/litter-provisioning-evidence-012 (C/D) -- n+1 provenance. Its own
  peer-reviewed source attributes it to 20 years of referral practice. Grigg
  2013 (28 cats) found no covered-versus-uncovered preference at group level.
- cat/kr-registration-gate-013 (A/D, locale KR) -- the mandated locale check,
  and a genuinely Korean finding.

STILL OPEN -- each searched this sprint and deliberately left unfilled rather
than filled with something plausible:
- THE ATTACHMENT PERCENTAGE. The proportion of cats classified as securely
  attached in Vitale et al. 2019 is quoted everywhere and was NOT obtainable in
  this pass: the Current Biology full text returned access errors from the
  publisher and from the open-access mirrors, and the abstract record carries
  neither a sample size nor a percentage. WHAT WOULD CLOSE IT: full-text access
  to the article, or a replication reporting its own classification
  distribution. Until then the number is not laundered into the warehouse.
- OBESITY AND THE THIN-END CONFOUND. Item 004's headline result -- larger hazard
  at the thin end than the fat end -- cannot be separated from reverse causation
  by its own design, because the commonest feline diseases take weight off before
  they take life. WHAT WOULD CLOSE IT: a cohort with body condition measured
  BEFORE disease onset and analysed with time-varying exposure, or any analysis
  excluding cats with a subsequent weight-losing diagnosis. Neither was located.
- HOME-BASED HYDRATION EVIDENCE. Both water-presentation studies (items 003)
  used individually housed cats under controlled conditions. Nothing tests bowl
  type, placement or number in a household where cats compete for resources.
  This is a real limitation and it cuts BOTH ways -- the laboratory result could
  be the clean truth or could be hiding a home-only effect.
- LITTER BOX EVERYTHING EXCEPT COVERED-VERSUS-UNCOVERED. Box size, substrate,
  depth, liners, cleaning frequency, placement relative to food and water, and
  whether boxes on different floors count toward n+1. All circulate confidently.
  A targeted search located no controlled feline test of any of them. The one
  variable anyone tested found nothing at group level.
- KOREAN DECLAWING LEGALITY. Searched against primary legal sources and NOT
  resolved. 동물보호법's prohibited-injury article carries exceptions for disease
  prevention and treatment, and nothing located settles whether an elective claw
  removal falls inside them. Recorded inside item 009 as well as here, because a
  gap-file entry does not fire at answer time.
- KOREAN CAT VACCINATION OBLIGATION. Also searched and NOT resolved. The
  농림축산검역본부 rabies page sets out a vaccination protocol for cats including
  annual boosters and states no obligation; whether a local ordinance or a
  가축전염병예방법 vaccination order can bring cats in was not established.
  Recorded inside item 013.
- KOREAN FELINE EPIDEMIOLOGY generally. Every clinical figure in this domain
  comes from Australian, UK, US, Israeli, French or German-language work. No
  Korean feline cohort, life table or primary-practice dataset was located in
  this sprint. The Korean content that exists here is legal, not clinical.
- WSAVA AND AAFP VACCINATION GUIDELINES. Located as citable documents
  (Stone et al. 2020 AAHA/AAFP feline vaccination guidelines, JFMS 22(9):813-830,
  doi 10.1177/1098612X20941784) and NOT converted into an item this sprint,
  because a vaccination schedule sits uncomfortably close to the domain's scope
  boundary and the Korean jurisdictional overlay could not be established. A
  later sprint should decide whether "which vaccines are considered core" is a
  fact about evidence (in scope) or a protocol (out of scope). Flagged rather
  than guessed.
- INDOOR VERSUS OUTDOOR LIFESTYLE. Tan, Stellato and Niel 2020 (Animals
  10(2):258) was located and read as a review of risks and benefits, and was NOT
  shipped: it is a narrative review rather than a primary study, and the
  quantified life-expectancy comparison an agent would actually want is not in
  it. Teng 2024's UK life tables do not break out lifestyle. WHAT WOULD CLOSE
  IT: a cohort or life-table analysis with outdoor access as an exposure.
- AGE-RELATED AND CHRONIC CONDITIONS. Chronic kidney disease, hyperthyroidism
  and degenerative joint disease are the conditions an older cat actually gets,
  and this sprint shipped nothing on any of them. They were out of budget rather
  than out of scope, and the observable-signs framing (item 005's pattern) is the
  right shape for all three. Highest-value target for the next sprint.
- ENRICHMENT AND FEEDING STRUCTURE. Dantas et al. 2016 (JFMS 18(9):723-732, doi
  10.1177/1098612X16643753) on food puzzles was located and not converted: it is
  a clinical-practice review rather than a controlled trial, and the domain
  already carries one consensus-framework row (011). Ship it when there is a
  controlled outcome to attach it to.
- AXES. This domain personalises on facts about the CAT -- age, sex, neuter
  status, indoor or outdoor, single or multi-cat household -- and the axes ledger
  contains only human-subject axes. No item in this sprint carries an
  `applicability` block for that reason. Adding pack-namespaced feline axes is a
  SCHEMA change and was deliberately kept out of a content-only sprint. Flagged
  as the domain's main structural gap.

Rerun-needed: none. Every source was verified against the PubMed primary record,
the publisher DOI record, or an official Korean government portal read directly.
Two sources sit outside PubMed and were verified through Crossref DOI records
instead (Kienzle 1993; Pachel and Neilson 2010). Two PubMed records carry no DOI
and are cited by PMID with that stated on the row (Markwell 1999, pre-DOI JAVMA;
Duperrier-Simond 2024, Can Vet J). One full text was sought and NOT obtained
(Vitale 2019), which is why the attachment percentage is refused rather than
shipped.

## cross-cutting

- Zombie-stat ledger: one zombie stat was caught and recorded as a refraction_note
  on exercise/replication-power-crisis-005 (the "~50% mean shrinkage" figure was
  REFUTED 1-2 in batch1; the confirmed figure is 88%-shrink / median -75%). Future
  sprints should keep flagging refuted-but-circulating pop-stats the same way.
- Warehouse size after this pass: exercise 6, nutrition 6, sleep-recovery 3 =
  15 RAG items, within the M3 solo-curator small+deep cap. Growth should stay
  quality-gated, not volume-driven.
- Size update 2026-08-22 (after v7): exercise 26, nutrition 5, sleep-recovery 3
  = 34 RAG items + 2 E-records. Exercise now carries 76% of the warehouse and is
  approaching the point where the small+deep cap should be re-argued rather than
  assumed; the other two domains have not grown since v2 and the imbalance is
  now the warehouse's most visible structural problem.
- Size update 2026-08-23 (after v9): exercise 30, nutrition 5, sleep-recovery 3
  = 38 RAG items + 2 E-records. Exercise is now 79% of the warehouse. The
  imbalance flagged after v7 has widened, not narrowed, and every sprint since
  v4 has landed in the same domain. The small+deep cap now needs re-arguing on
  purpose rather than by default: either the other two domains get a sprint, or
  the warehouse should be described as an exercise warehouse with two
  vestigial domains attached.
- Size update 2026-09-02 (after v13): exercise 30, finance-investing 17,
  nutrition 15, learning-habits 13, mental-health 7,
  relationships-communication 7, cooking 3, sleep-recovery 3
  = 95 RAG items + 2 E-records. Exercise moves from 35% to 32% of the
  warehouse. The v7/v9 complaint that "every sprint since v4 has landed in the
  same domain" is broken: v13 is the first NUTRITION sprint since v2, and the
  lane it lands in goes from 5 items to 15. The remaining structural imbalance
  is sleep-recovery, still at 3 items and still holding ZERO substantive
  claims of its own since v2. It is now the warehouse's most visible hole, and
  its trap is unchanged: the domain named "recovery" does not contain the
  training-recovery items, which live under exercise (021-026).
- Rejected-claim ledger, v13 (nutrition-lane sprint):
  - "A beginner can gain roughly 1-1.5% of body weight in muscle per month",
    and the whole family of tiered rate-of-gain-by-training-age tables. REFUSED
    OUTRIGHT. A targeted search for any primary study measuring a maximum or
    typical rate of lean-mass gain returned ZERO results. These are
    practitioner-authored figures with no trial behind them at any tier. This is
    the nutrition-side twin of the v9 load-increment finding: the most
    confidently quoted number in the area is one nobody has ever measured.
    Recorded so a later sprint that meets these tables in a coaching source
    cannot mistake their ubiquity for evidence.
  - "Protein above ~20-40 g in a single meal is wasted / oxidised." REFUSED AS
    STATED, and the refusal is now sourced rather than merely cautious. A 2023
    quadruple-tracer trial reports a greater and more prolonged response to 100 g
    than to 25 g with negligible change in oxidation. The ceiling claim is
    contested, not established. Note the direction carefully: this does NOT
    license advising large boluses, because the measured endpoint is protein
    synthesis over hours, not muscle over a training block. Item 008.
  - "Protein must be spread evenly across meals to maximise muscle." REFUSED as
    evidence-backed. The supporting study is an n=8 acute crossover; two RCTs at
    real outcomes returned null; the review-level association fails to extend to
    strength or turnover. Item 009.
  - "Energy availability below 30 kcal/kg FFM/day indicates a problem." REFUSED
    as a diagnostic reading, on the authority of the body that popularised it:
    the 2023 IOC consensus statement states the concept was intended as a guide
    rather than a diagnostic end-point and warns of the risks of a definitive
    clinical threshold. Compounding this, all three inputs to the equation are
    unmeasurable to laboratory standard in a consumer setting. Item 010.
  - "An energy surplus is required to maximise hypertrophy." NOT SHIPPED as the
    symmetric partner of the deficit guidance; the review evidence for the
    requirement is weak. Recorded on item 012 so the deficit rule does not drag
    a surplus rule along behind it.
  - Consumer food-tracking-app accuracy figures. REFUSED for lack of any
    KR-applicable or adequately powered primary source (located: n=37 Filipino
    adults; an Australian app-store quality survey).
  - Korean mixed-dish logging error. REFUSED as unsourceable in this pass. No
    primary source quantifies portion or nutrient error for Korean composite
    dishes. Explicitly NOT inferred from nutrition/kr-food-composition-accuracy-016,
    whose duplicate-portion design removes precisely that error.
  - STALENESS CATCH, a ledger category this sprint adds: the 2020 Korean Dietary
    Reference Intakes. Not wrong when issued, but SUPERSEDED on 2025-12-31 by the
    2025 edition, which raised the protein energy-percentage floor and re-derived
    dietary fibre. Any Korean reference figure recited from memory or from a
    pre-2026 source is a prior edition. Handled like a zombie stat: recorded here
    so it cannot be re-adopted, and carried as the first refraction note on item
    014. Generalisable lesson for the warehouse: jurisdiction-bound items need an
    edition check, not just a source check, because the source can be correct and
    obsolete at the same time.
- Rejected-claim ledger, v9 (load-increment sprint):
  - "A JSCR study showed smaller weight increments produce more consistent
    strength gains" (reposted by content-farm sites, no author/year/DOI).
    REJECTED -- with a nuance that changes the correct response. Two research
    passes called it a pure phantom; the third, adversarial pass found that a
    real, on-point JSCR paper DOES exist (Hostler 2001, PMID 11708713) and that
    it points the OTHER WAY: micro-loading merely not-worse, with the authors
    noting traditional loading might be more effective over an extended period.
    So the rejection is "a real study exists and the repost misrepresents its
    direction", NOT "no such study exists". Item 027. Recorded this way so a
    later sprint that rediscovers Hostler cannot mistake it for confirmation.
  - "Microplates beat stalling." REJECTED as evidence-backed. No trial compares
    micro-loading against stall-and-reset; the arithmetic shows only that large
    increments become unsustainable, which is not evidence that small ones
    work. Never "research shows". Item 027.
  - "Upper body adapts slower and therefore needs smaller jumps." PHYSIOLOGY
    REJECTED, ARITHMETIC KEPT. Jung 2023 (PLOS ONE 18(4):e0284216) has
    label-swap typos in its published abstract (correct reading: 7.2%/wk LOWER,
    5.2%/wk UPPER), a primary pooled effect of 0.47 [-0.13, 1.08] that is NOT
    significant and becomes so only after post-hoc outlier removal, no
    upper/lower difference at all in beginners, and a young-women-only
    population. 7.2%/wk must never be stored as a sustainable rate (compounded
    it implies over 100% in ten weeks). The surviving argument is arithmetic
    only: 2.5 kg is 4.17% of a 60 kg bench and 1.8% of a 140 kg squat. Item 027.
  - "Deload restores progression." REJECTED as stated. Coleman 2024 (PeerJ,
    PMC10809978, RCT n=39 trained): a one-week complete-cessation deload at the
    midpoint of a 9-week program IMPAIRED lower-body strength gains and did
    nothing for hypertrophy. It tested cessation, not a load reduction, so a
    volume/load deload remains untested. Item 027.
  - "Load progression above 15%/week raises injury risk 21-49%." DROPPED
    OUTRIGHT and flagged must-not-ship-as-a-safety-rail. Traces to the
    acute:chronic workload ratio literature, whose central injury sweet-spot
    figure carries a retraction request (Impellizzeri et al.), is statistically
    unstable at low chronic load, has no causal estimation, and describes weekly
    aggregate team-sport load rather than per-session barbell increments. The
    accompanying absence is the real finding: NO evidence links per-session
    increment SIZE to injury incidence in either direction. Item 027.
  - Two papers flagged DEFECTIVE rather than used as evidence, a new ledger
    category this sprint: Huang 2025 (PMID 40791980) -- abstract contradicts
    itself, SUCRA ordering with only one interval excluding zero, study
    count/N unverifiable (item 030); and Washif 2024 (PMC11167475) -- published
    SEM/MDC do not reproduce from its own ICC and SD, SEM% is 3x smaller than
    its own CV, printed bench MDC% is arithmetically wrong (item 029; its
    recomputed values are used, its printed ones are not).
  - NOT rejected but stored at the practitioner floor with an explicit
    unverified locator: the NSCA increment table (less-trained upper 2.5-5 lb /
    lower 5-10 lb; more-trained upper 5-10+ lb / lower 10-15+ lb). Its direction
    -- more-trained lifters get LARGER absolute increments -- is real and opposes
    the popular microplate framing, but the Baechle & Earle attribution could
    not be verified; the only trail that checked out is NSCA's Essentials of
    Tactical Strength and Conditioning (Alvar, Sell & Deuster, Eds., Human
    Kinetics, 2017). No table number was fabricated. Item 027.
- Rejected-claim ledger, v7 (same discipline as the zombie-stat entry above --
  a popular claim that failed adversarial verification is recorded here, not
  quietly dropped, so it cannot be re-adopted by a later sprint):
  - "Static stretching before lifting blunts power/explosiveness." REJECTED as
    stated. Outcome-stratified meta (Warneke & Lohmann 2024, 83 studies): jump
    ES +0.15 (p=0.006, trivially POSITIVE), sprint/throwing null, rate of force
    development ES -0.03 (p=0.86). Only isolated maximal strength shows the
    deficit. Carried on item 021 in the narrowed form.
  - "Massage speeds recovery." REJECTED at the performance level (Davis 2020,
    29 RCTs / 1012 participants: null for strength, jump, sprint, endurance,
    fatigue). Survives only as a soreness/flexibility claim. Item 024.
  - "Stretching before or after training reduces soreness." REJECTED (Cochrane
    2011, 12 studies / 2597 participants -- small, PRECISE, not clinically
    worthwhile; Afonso 2021 null at 24/48/72 h). Item 024.
  - "Each muscle group needs 48-72 h" + published per-muscle-group recovery
    tables. REJECTED as evidence-based; no controlled cross-muscle comparison
    exists. Item 025.
  - "Bigger muscles recover slower" / "upper body recovers faster than lower."
    REJECTED, no matched comparison located; the one direct measurement is
    about JOINT involvement within a single muscle group, not size. Item 025.
  - Repeated-bout-effect precision figures ("60-80% soreness reduction for
    6-8 weeks, protection lasting 6-9 months"). REJECTED as unsourceable --
    present only in fitness media, absent from every peer-reviewed source
    checked. The repeated-bout effect itself is retained qualitatively.
    New zombie-stat entry, same handling as the "~50% mean shrinkage" figure.
  - "Lactic acid causes DOMS." Refuted and still circulating. Item 023.

- Size update 2026-09-02 (after v14): exercise 30, finance-investing 17, nutrition 15, learning-habits 13, sleep-recovery 13, mental-health 7, relationships-communication 7, cooking 3
  = 105 RAG items + 2 E-records. Exercise is now 29% of the warehouse.
  sleep-recovery went from 3 methodology-only items to 13: the domain's
  first substantive claims, and the close of the coverage gap that had
  stood open since v2. Counts computed at apply time, not asserted.
- Rejected-claim ledger, v14 (sleep-recovery collection sprint). Each entry is a
  widely circulating claim that was researched and NOT shipped as stated, so it
  cannot be quietly re-adopted by a later sprint:
  - "Sleeping more improves athletic performance" (as an unqualified claim).
    REJECTED AS STATED. The entire controlled literature is seven studies
    (Silva 2021 systematic review), all three RCTs at high risk of bias, two
    reporting no improvement despite successfully increasing total sleep time,
    and no meta-analysis possible. Survives only in the hedged form on item 005.
    Note the asymmetry that makes this a rejection rather than a null: sleep
    LOSS impairing performance rests on 69 publications of controlled
    experiments (item 004). The two directions are not symmetric and were
    routinely spoken as if they were.
  - "The Stanford basketball study proved extra sleep makes athletes faster and
    more accurate." REJECTED as a causal claim. Mah 2011 is real and correctly
    reported, but it has ELEVEN participants and NO control group -- a
    non-randomized pre-post design across 5-7 weeks of a competitive season,
    with serial-order carryover named by the systematic reviewers as an
    unexcluded explanation. Same handling as the exercise domain's Hostler 2001
    entry: the study exists and the popular retelling misrepresents what it can
    support.
  - "Sleeping under 8 hours makes you 1.7x more likely to get injured" applied
    to ADULTS. REJECTED as transferred. The figure is real and comes from
    Milewski 2014 -- 112 ADOLESCENTS aged 12-18, self-reported sleep against a
    retrospective review of school injury records, 95% CI 1.0-3.0 with the lower
    bound ON 1.0, and school grade the stronger predictor in the same model. The
    adult prospective systematic review (Dobrosielski 2021, 12 cohorts)
    concludes the evidence does not support poor sleep as an independent adult
    injury risk factor. Item 006.
  - "Blue-light blocking glasses improve sleep." REJECTED. Cochrane 2023
    (Singh, 17 RCTs): no meta-analysis possible for any outcome, sleep-quality
    evidence at VERY LOW certainty with six trials splitting three positive and
    three null, and no included trial measured serum melatonin at all. The
    underlying mechanism (Chang 2015) is real but was demonstrated at n=12 with
    a four-hour inpatient exposure under dim background lighting. Item 012.
  - "Adults need 7-9 hours" quoted as the AASM position. REJECTED as
    misattributed. The AASM/SRS joint consensus is a THRESHOLD -- "7 or more
    hours" -- with NO upper bound, and the panel recorded that the
    appropriateness of 9 or more hours could not be ascertained with certainty.
    The 7-9 RANGE is the National Sleep Foundation's separate product from a
    separate panel. Same source-misattribution failure mode that
    relationships-communication/source-misattribution-rule-005 exists to catch.
  - "Naps improve athletic performance." REJECTED as stated, in the endpoint
    that matters for a lifter. The pooled large effect (Mesas 2023, SMD 0.99)
    resolves task-by-task (Boukhris 2024) into a strong signal on one
    intermittent-running test and a NULL on muscle force (ES 0.175, p = 0.267),
    with nulls on sprint and on the 30-s Wingate. Perceived fatigue improves
    (SMD -0.76). Same perceived-versus-measured split as item 024 in exercise.
  - "Do not exercise in the evening, it ruins your sleep." REJECTED. Stutz 2019
    (23 PSG studies) does not support it and points mildly the other way. Only
    the narrow caveat survives: vigorous exercise ending one hour or less before
    bedtime MIGHT impair onset latency, total sleep time and efficiency.
    Item 010.
  - "Melatonin is a sleep aid." REJECTED as framed. AASM 2017 suggests
    clinicians NOT use it for chronic insomnia; the endorsed use (AASM 2015) is
    STRATEGICALLY TIMED melatonin for circadian disorders, where the timing is
    the intervention. Pooled effect where it does act: about 7 minutes of
    sleep-onset latency. Item 008.
  - "Follow good sleep hygiene" as a standalone remedy. REJECTED at the clinical
    level -- the AASM behavioural guideline (Edinger 2021) issues a conditional
    recommendation AGAINST sleep hygiene as a single-component therapy for
    chronic insomnia, while giving multicomponent CBT-I the guideline's only
    STRONG recommendation. Item 007. Note the scope: this is about hygiene used
    ALONE for a clinical diagnosis, not about hygiene elements inside a larger
    programme.
  - NOT rejected, NOT shipped, explicitly refused for insufficient evidence:
    sleep-debt repayment, magnesium, proprietary readiness scores, sleep-and-
    hypertrophy outcomes, caffeine timing. See the sleep-recovery section above
    for what was searched in each case and what would close it.

- Size update 2026-09-02 (after v15): exercise 30, finance-investing 17,
  nutrition 15, learning-habits 13, sleep-recovery 13, cooking 12,
  mental-health 7, relationships-communication 7
  = 114 RAG items + 2 E-records. Exercise moves from 29% to 26% of the
  warehouse. cooking goes from 3 items to 12, and for the first time the
  domain holds substantive cookable content rather than field methodology:
  before this sprint two of its three items were about how the FIELD is graded
  and only one was a cooking claim. Five of the nine new items are KR-locale
  and sourced to Korea's own food-safety regulator, which is the discipline
  this lane adopted after a US-only rule was dropped from it the same day.
  Counts computed at apply time, not asserted.
- Rejected-claim ledger, v15 (cooking-lane collection sprint). Cooking is
  unusually dense with confidently repeated folklore, so this ledger is as much
  the output of the sprint as the nine items are. Each entry is a claim that was
  researched and NOT shipped as stated, recorded so it cannot be quietly
  re-adopted:
  - CARRIED FORWARD, not re-litigated: "63C plus a 3-minute rest is a safety
    equivalence for whole cuts." The US codifies this. KOREA DOES NOT. Korean
    official guidance gives plain core temperatures with no holding-time
    equivalence attached, and 레스팅 appears in Korean sources only as a juiciness
    technique. The claim was dropped from this lane earlier on 2026-09-02 and is
    recorded here so the drop survives as warehouse memory rather than as one
    agent's decision. v15 hardens it structurally: item 005 publishes the
    Korean beef range 63~77C verbatim AND states in the same item that Korea
    attaches no holding-time rule to its lower end, so the next pass meeting the
    US construct in a source hits the fence before the claim. Generalisable rule,
    and the governing rule of this sprint: A US REGULATORY FACT IS NOT A KOREAN
    REGULATORY FACT, and shipping it as one misrepresents the law the consumer
    actually cooks under.
  - "Salting pasta water raises the boiling point enough to matter" / "salt makes
    water boil faster." REJECTED, AND WRONG IN TWO DIFFERENT WAYS. Magnitude:
    delta-Tb = i x Kb x m with Kb = 0.512 C/m gives about 0.18 C at the
    conventional 10 g/L, and about 0.61 C even at an aggressive 35 g/L; a couple
    of degrees would take over 100 g per litre. Direction: dissolved salt RAISES
    the boiling point, so it can only delay the boil, never hasten it. The popular
    version has the sign backwards, and a correction that only shrinks the number
    leaves that standing. Item 011. Same handling as the exercise lane's
    "physiology rejected, arithmetic kept" entries: the conclusion rests on
    arithmetic over a textbook constant, and the one assumption in it (complete
    dissociation) errs conservatively -- every refinement makes the effect
    smaller, never larger.
  - "The alcohol cooks off." REJECTED at every ordinary duration, with numbers.
    USDA retention factors for ethyl alcohol: 85 percent retained when stirred
    into hot liquid, 75 percent flamed, 40 percent after a 15-minute simmer, 25
    percent after an hour, 10 percent after two, 5 percent after two and a half.
    Note the inversion that makes this worth recording rather than merely
    correcting: FLAMBEING RETAINS MORE THAN A SHORT SIMMER DOES, so the most
    visually convincing way of burning off alcohol is among the least effective.
    Item 012. Kept honest in the other direction too: these are retention factors
    from a compiled reference table rounded to 5 percent, they are retention of
    what was added rather than a concentration, and they must not be converted
    into a drink equivalent.
  - "The Maillard reaction starts at 140C" (also circulated as 154C). REJECTED as
    a threshold. The kinetic literature describes a continuous Arrhenius
    dependence, with model-system studies reporting maximum rates near 120C and
    the rate falling off both above 120C and below 100C. There is no switch to
    cross. A precise-sounding onset figure that nothing measured is exactly the
    kind of number this warehouse treats as a zombie stat. Item 013 ships the
    dependency that IS measured -- water activity peaking at 0.6-0.7, with excess
    free water diluting the reactants -- and the technique consequence that
    follows from it.
  - "Rest meat and it keeps its juices." REFUSED IN BOTH DIRECTIONS, which is the
    unusual part. Every quantified measurement located is blog-tier, including a
    secondhand attribution to a culinary-science journal that could not be
    resolved to a citation; and the one controlled attempt located, which held
    internal temperature constant at the moment of slicing, reported no
    difference. So the lane ships neither the folklore nor its refutation. Recorded
    because refusing the REBUTTAL as well as the claim is the honest position when
    both sides are unsourced, and a later pass will otherwise be tempted to ship
    the debunk on the strength of the debunk being fashionable.
  - Marinade penetration depth in millimetres (wet 1-3 mm, dry brine up to 5 mm,
    "salt takes 24 hours to reach an inch"). REFUSED. Blog-sourced. The
    peer-reviewed literature located measures phosphate-tumbled poultry,
    ultrasound-assisted salt diffusion in sauced duck, and NaCl diffusion
    simulation in multi-tissue beef -- industrial and instrumented processes, not
    a household marinade. Not inferred across.
  - "Never wash raw chicken." REFUSED as an evidence-backed claim, NOT as advice.
    It is real public-health guidance from named regulators and the splash
    mechanism is plausible, but in this pass it traced only to regulator
    communications and press coverage, never to a retrievable primary
    measurement. Item 009 ships the cutting-board evidence that does have a
    primary behind it, deliberately in place of this. The complication worth
    recording: a US-funded consumer observational study exists in this area, was
    not read, and its reported direction is that not-washing did not eliminate
    sink contamination -- so this is a "verify before adopting", not a
    "obviously true, just find the paper".
  - Cooking time as a function of thickness rather than weight (conduction time
    scaling with the square of the distance). NOT REJECTED -- the physics is not
    in doubt -- but NOT SHIPPED, because the peer-reviewed food-engineering
    sources located were paywalled or scanned-image-only and nothing was quoted
    from them. Recorded as a live want: this is the highest-value @test-kitchen
    item still missing for a live session.
  - Seasonal-incidence multiplier for winter oyster food poisoning (a roughly
    eight-fold year-on-year rise). EXCLUDED. It appeared in secondary coverage of
    the ministry advisory and was absent from the government text actually read.
    Same handling as any figure that lives only in retellings: the seasonality is
    carried on item 010, the multiplier is not.
  - NOT rejected, NOT shipped, explicitly not researched: Korean fermentation
    safety (kimchi, jang), banchan storage limits, and Korean-dish evidence for
    the reheating mechanism in 국/찌개/볶음밥. These are the lane's most
    consumer-relevant Korean questions and this sprint did not ask them. See the
    cooking section above for what would close each.
- Size update 2026-09-02 (after v16): exercise 30, finance-investing 17, relationships-communication 17, nutrition 15, learning-habits 13, sleep-recovery 13, cooking 12, mental-health 7
  = 124 RAG items + 2 E-records. Exercise is now 24% of the warehouse.
  relationships-communication went from 7 items to 17. The 7 it had were
  five refutations, a curator checklist and one therapy-efficacy row -- a
  domain that could say what is false and almost nothing about what is
  true. That asymmetry is what this sprint closed. Note the shape of the
  result rather than the count: 5 of the 10 new rows are flagged
  contested, one is a deliberate ABSENCE row, and the sprint's refusal
  ledger is longer than several domains' entire item lists. Counts
  computed at apply time, not asserted.
- Rejected-claim ledger, v16 (relationships-communication lane sprint). This
  domain has the largest gap in the warehouse between popular authority and
  evidential strength, so the sprint's operating rule was that refusing a famous
  claim with a stated reason beats shipping it. Each entry below was researched
  and NOT shipped as stated, so it cannot be quietly re-adopted later:
  - "Loneliness is as bad as smoking 15 cigarettes a day." REFUSED, and the
    refusal has two independent parts. First, SOURCE: the phrasing could not be
    located anywhere in the text of Holt-Lunstad 2010 (PLoS Med 7(7):e1000316),
    which was read at PMC full text for this purpose. What the article's text
    actually says is that the magnitude "is comparable with quitting smoking" and
    that it exceeds obesity and physical inactivity; the cigarette count appears
    to come from a comparison condition in its Figure 6, whose per-condition
    labels are in the figure image and were NOT verifiable in this pass. Second,
    and worse, MAGNITUDE: the phrase is attached to the 2010 odds ratio of 1.50,
    which the field has since revised down -- Wang 2023 (Nat Hum Behav, 90
    prospective cohorts, 2,205,199 individuals) puts social isolation at 1.32 and
    loneliness at 1.14. So a popular equivalence of unverified provenance is being
    quoted against an effect size its own literature no longer supports. Same
    failure mode as relationships-communication/source-misattribution-rule-005.
    Item 008.
  - "It takes 50 hours to make a casual friend and 200 hours to make a good
    friend." REFUSED AS A RULE, study confirmed as real. Hall 2019 (J Soc Pers
    Relat 36(4):1278-1296, doi 10.1177/0265407518761225) exists and the figures
    are its own. What it did was ask participants to RETROSPECTIVELY ESTIMATE
    hours: Study 1 is N=355 MTurk adults who had recently relocated, estimating
    time spent with a new acquaintance. No hours were measured, none were
    assigned, and no threshold was tested against an alternative. These are
    recalled estimates producing descriptive averages, converted into a
    prescription by retelling. Study 2's sample was NOT verified in this pass and
    no figure from it is asserted. Same handling as the exercise domain's Hostler
    2001 entry: the study exists and the popular version misrepresents what it can
    support. Item 014.
  - ANY contact cadence or frequency rule ("call a close friend weekly", "check in
    every N weeks", per-layer contact schedules). REFUSED OUTRIGHT. A targeted
    search returned ZERO primary sources prescribing a contact frequency,
    interval, or minimum contact count. The health literature such rules are
    attributed to measures composite social-integration indices, single-item
    loneliness scales and living-alone flags -- never contact counts. Note the
    scope carefully, because the opposite over-read would be a worse error: this
    is a SEARCHED ABSENCE, not a demonstrated null. Nobody has shown that contact
    frequency does not matter. Shipped as an explicit absence item (014) rather
    than left in this ledger alone, because a gap-file entry does not fire at
    answer time and the predictable failure is a fluent invented interval
    delivered beside sourced material and inheriting its authority.
  - "Humans can maintain about 150 relationships", and the nested 5/15/50/150
    layers. REFUSED AS DERIVABLE. Lindenfors, Wartel and Lind 2021 (Biol Lett
    17(5):20210158) re-tested the neocortex-to-group-size extrapolation: Bayesian
    methods gave 69-109, generalized least-squares phylogenetic methods gave
    16-42, and the 95% confidence intervals were 4-520 and 2-336. The authors'
    conclusion is that specifying any one number is futile. Note what the refusal
    is NOT: there is no retraction and no arithmetic impossibility here, and the
    original proponent still defends the estimate on other grounds -- so this is
    "cannot be derived the way it is usually justified", not "disproved". Graded
    one band below the positivity-ratio refutation for exactly that reason. The
    layer structure has LESS support than the headline number and is quoted with
    MORE confidence, which is a reliable folklore marker. Item 015.
  - "Asians and Asian Americans benefit more from implicit than explicit social
    support." REFUSED AS ACTIONABLE, recorded because it is the first thing anyone
    will reach for on an East Asian support question. Taylor, Welch, Kim and
    Sherman 2007 (Psychol Sci 18(9):831-837, doi 10.1111/j.1467-9280.2007.01987.x)
    is a real and frequently cited paper. Three reasons it was not shipped: it is
    a small single-laboratory study from the pre-replication-crisis era with
    biological stress-response endpoints of the class that replicated poorly; no
    independent replication or meta-analysis was located in a targeted search; and
    "Asian American university students" is not the same population as an adult
    living in Korea. Carried inside item 016 as an untested hypothesis worth
    knowing about, never as a basis for changing how support is offered.
  - "Men and women communicate differently." REFUSED, and NOT shipped as an item
    either. The refutation evidence is genuinely strong -- Hyde 2005 (Am Psychol
    60(6):581-592, 46 meta-analyses) and Zell, Krizan and Teeter 2015 (Am Psychol
    70(1):10-20, 106 meta-analyses and 386 meta-analytic effects, mean absolute
    difference d = 0.21, with 46% of effects small and 39% very small, holding
    across age, culture and generation). It was not made an item because no
    substantive claim currently in this domain requires the correction, and a
    refutation with no target is padding. Recorded here so the evidence is on file
    the moment a domain claim needs it.
  - Loneliness-intervention effect sizes. REFUSED as actionable. The best source
    located (Masi et al. 2011, Pers Soc Psychol Rev 15(3):219-266) reports that
    single-group pre-post and non-randomized designs yielded LARGER mean effects
    than randomized comparison studies, and that among randomized designs the
    interventions addressing maladaptive social cognition performed best. That is
    a design-quality finding rather than a usable effect size, and it is fifteen
    years old. Refused rather than shipped at a low grade, because a weak
    intervention recommendation in this area invites action.
  - NOT rejected, NOT shipped, explicitly left open: the Gottman 5:1 positivity
    ratio (distinct from the 2.9013 constant already refuted at item 001). Its
    primary sources were located and verified as citations -- Gottman and Levenson
    1992 (JPSP 63(2):221-233) and Gottman 1993 (JCCP 61(1):6-15), the same 73
    couples in both -- but no source testing the 5:1 figure prospectively or out
    of sample was found. Item 011 now shows that the divorce-prediction models
    built on those same 73 couples collapse on crossvalidation and failed
    independent replication, which makes it likely the ratio inherits the problem.
    Likely is not verified. Recorded as open in the section above rather than
    shipped as refuted, because inferring a refutation from a neighbouring one is
    the same shortcut this domain exists to prevent.
  - VERIFICATION-CLOSED, a ledger category this sprint adds as the mirror image of
    a rejection: relationships-communication/gottman-prediction-artifact-003
    recorded against itself that "the exact 21-43% PPV range is NOT verified (see
    open question)". It is now verified from the primary methodological paper
    (Heyman and Smith Slep 2001, J Marriage Fam 63(2):473-479): positive <!-- estate-scrub:allow(author surname Smith, not an instance) -->
    predictive value 65.38% in the development sample, 28.81% on crossvalidation,
    and 20.99% reweighted to the true divorce prevalence of approximately 16%.
    The low end of the circulating range was approximately right; the high end was
    not supported by this paper. Worth recording as a category because it is the
    behaviour the domain's curator checklist is meant to produce: a prior sprint
    flagged an unverified figure instead of shipping it, and a later sprint
    verified it instead of quietly adopting it.

- Size update 2026-09-02 (after v17): exercise 30, mental-health 20, finance-investing 17, relationships-communication 17, nutrition 15, learning-habits 13, sleep-recovery 13, cooking 12
  = 137 RAG items + 2 E-records. Exercise is now 22% of the warehouse.
  mental-health went from 7 methodology-only items to 20: the domain's
  first substantive claims. Every remaining domain now holds substantive
  content, so the structural complaint that has run through this file
  since v7 -- one domain carrying the warehouse while others stay
  vestigial -- is closed. Counts computed at apply time, not asserted.
- Rejected-claim ledger, v17 (mental-health lane collection sprint). Each
  entry is a claim that was researched and NOT shipped as stated, or was excluded
  on the domain's clinical boundary, so it cannot be quietly re-adopted by a later
  sprint. The exclusions are listed first and deliberately: in this domain the
  refusals are the more important half of the output.
  - EXCLUDED ON THE CLINICAL BOUNDARY, not for want of evidence. The following
    were considered and deliberately not authored, because this is a knowledge
    warehouse for a generalist life agent and each of them can only be stated
    usefully in clinical-advice form:
      (a) ANTIDEPRESSANT EFFICACY VERSUS PLACEBO. Named explicitly as a candidate
          area. The literature is large and genuinely contested -- that is not
          why it was dropped. It was dropped because the consumer has no action
          to take on it and any surfacing reads as guidance about somebody's
          prescription. Recorded so a later sprint does not mistake the gap for
          an oversight.
      (b) DIAGNOSTIC CRITERIA AND DIAGNOSIS. No item may state or imply a
          threshold at which someone should be considered to have a condition.
      (c) SCREENING. No cut-off in this domain is to be applied to anyone. Item
          011 handles the closest adjacent topic and is authored so that its
          entire operative content is the refusal: a self-reported score,
          threshold or tracked signal may not be converted into a claim about a
          person's state.
      (d) RISK ASSESSMENT AND CRISIS HANDLING. Excluded outright. Nothing in this
          lane estimates, ranks or flags risk for an individual.
      (e) TREATMENT SELECTION. Which therapy, which medication, which clinician.
          Item 010 records a non-inferiority result as a fact about an evidence
          base and explicitly refuses any operational use of it.
  - "Exercise is an effective treatment for depression", quoted with the
    confidence the sentence implies. REJECTED AS STATED. The direction is
    supported and the confidence is not: Noetel 2024 (BMJ, 218 studies, 495 arms,
    14170 participants) reports moderate effects AND reports that exactly ONE of
    its 218 studies met the Cochrane low-risk-of-bias criteria, with CINeMA
    confidence LOW for walking or jogging and VERY LOW for every other modality.
    Participants cannot be blinded and the outcome is self-reported, so an
    expectancy component cannot be excluded; the authors themselves recommend
    future blinding. Item 008. Survives only as a direction, never as a number.
  - Any HEAD-TO-HEAD RANKING out of that same network -- "exercise is as effective
    as therapy or medication". REJECTED. At low-to-very-low confidence across a
    network containing one low-risk-of-bias trial, no comparative statement is
    supported at usable certainty. It is also treatment-selection content, which
    is excluded above on the boundary. Two independent reasons, either sufficient.
  - "Exercise prevents depression" and "exercise treats depression" used
    interchangeably. REJECTED as a conflation, and the reason two items were
    authored instead of one. The prevention claim is observational (Pearce 2022,
    15 cohorts, no randomisation, self-reported exposure, reverse causation
    unresolved because reduced activity is itself an early feature of the
    condition); the treatment claim is randomised but almost entirely at high risk
    of bias. Neither weakness fixes the other, and a reader who merges them ends
    up with a claim that appears to have both randomisation and population reach
    when no single body of evidence has both. Items 008 and 009.
  - "11.5% of depression cases could be prevented by meeting activity
    guidelines." DROPPED for individual-level use. It is a real published
    population-attributable estimate (Pearce 2022) stacked on the causal
    assumption its own design cannot supply. Legitimate as public-health
    modelling; a fabrication when said to one person about their own odds.
  - "X% of people are burned out", in any form. REFUSED OUTRIGHT rather than
    ranged. Rotenstein 2018 (JAMA, 182 studies, 109628 individuals, 45 countries)
    found at least 142 unique definitions of burnout and a reported prevalence
    range of 0% to 80.5%, and the reviewers ABANDONED their planned meta-analysis
    as inappropriate. A 0-to-80.5% range is not an imprecise estimate awaiting a
    bigger study; it is what happens when the threshold choice determines the
    answer. The same review reports that burnout's associations with sex, age,
    geography, time, specialty and depressive symptoms could not be reliably
    determined either -- so the correlates fail with the prevalence. Item 015.
    New ledger category, same handling as a zombie stat: not corrected, refused.
  - "Burnout" applied outside work. REJECTED against the definition. The WHO
    ICD-11 entry states that burn-out "refers specifically to phenomena in the
    occupational context and should not be applied to describe experiences in
    other areas of life", and that it is NOT classified as a medical condition.
    Parenting, caregiving, study and general life exhaustion are not burnout
    under the definition, and neither is a tired week. Item 015.
  - "Gratitude journalling improves mood / reduces depression and anxiety."
    REJECTED as evidence-backed. Cregg and Cheavens 2021 (k=27, N=3675): pooled
    g -0.29 at post-test, but -0.51 against WAITLIST controls versus -0.18 against
    ACTIVE controls, and -0.63 versus -0.16 at follow-up. No other moderator was
    consistently significant. The authors' own conclusion is that a parsimonious
    explanation is placebo, and they recommend interventions with stronger
    evidence. Note the direction of the refusal carefully: nothing here says the
    practice is harmful or that someone who enjoys it should stop. What is refused
    is the CLAIM. Item 017.
  - MISATTRIBUTION CATCH, a live one. The figures "d = 0.31 for a measurement-only
    control down to d = -0.03 for a psychologically active comparison" circulate as
    the result of the Cregg and Cheavens gratitude meta-analysis. They are NOT.
    They belong to Davis et al. 2016 (J Couns Psychol 63:20-31, doi
    10.1037/cou0000107) and appear inside the 2021 paper's INTRODUCTION as a
    citation of prior work. Found by reading the full text rather than the
    abstract. Recorded here so a later sprint meeting those numbers attributes
    them correctly. Same failure mode
    relationships-communication/source-misattribution-rule-005 exists to catch.
  - "Positive psychology interventions improve wellbeing", quoted at the effect
    size of the field's two most-cited meta-analyses. REJECTED. Those two
    meta-analyses disagreed with each other before anyone reanalysed them (Sin and
    Lyubomirsky 2009: r = .29 wellbeing, r = .31 depression; Bolier 2013: r = .17,
    .10, .11). White, Uttl and Holder 2019 reanalysed both, found small sample
    size bias pronounced, and reported the corrected wellbeing effect at
    approximately r = .10 with the DEPRESSION effect variable, outlier-dependent
    and generally NOT statistically significant. Item 017.
  - "Mental health apps work" / "there's an app with evidence behind it."
    REJECTED. Goldberg 2022 (PLOS Digital Health) applied prespecified
    evidence-strength criteria to 34 unique effect sizes drawn from 14
    meta-analyses (145 RCTs, 47940 participants) and "failed to find convincing
    evidence of efficacy" for any of them; publication bias was rarely even
    assessed. Eight effect sizes reached highly-suggestive -- but the mood-related
    ones are against INACTIVE controls, and the one that survived an active
    comparison is text-message support for SMOKING CESSATION at d = 0.19, a
    behavioural rather than an affective outcome. No moderators were identified,
    so there is no evidence-based basis for preferring any particular app. Item 018.
  - "Adverse effects of mental health apps are minimal." REJECTED as an inference
    from silence. Goldberg 2022 reports that adverse effects were NOT REPORTED
    anywhere in the reviewed literature. Unstudied is not the same as safe, and
    this warehouse keeps that distinction everywhere else.
  - "Willpower is a limited resource that depletes" / decision fatigue as a
    scheduling model. REJECTED, with the nuance kept. Two independent preregistered
    multi-laboratory replications: Hagger 2016 (23 labs, N=2141, d = 0.04, 95% CI
    -0.07 to 0.15) and Vohs 2021 (36 labs, N=3531, confirmatory d = 0.06
    non-significant, Bayes factor about 4:1 favouring the null) -- the second
    co-authored by the effect's ORIGINAL PROPONENTS using a paradigmatic design
    chosen to give the manipulation its best chance, which closes both the
    hostile-replicator and the botched-protocol escapes. The nuance that must
    travel with it: an exploratory analysis on the full sample ignoring exclusions
    DID find a significant d = 0.08, so the honest claim is "no effect in
    preregistered analyses", not "proven zero". Item 019. What is forbidden is the
    scheduling heuristic: no willpower budget, no decision quota, no explaining an
    evening lapse by morning expenditure.
  - "Bad sleep makes you irritable and low." REJECTED AS FRAMED, and the correct
    direction is the more useful finding. Palmer 2024 (Psychological Bulletin,
    preregistered, 1338 effect sizes across 154 studies, N=5717): all forms of
    experimentally imposed sleep loss reduced POSITIVE affect (SMD -0.27 to -1.14),
    increased anxiety symptoms (0.57-0.63) and blunted emotional arousal
    (-0.20 to -0.53), while findings for NEGATIVE affect, emotional valence and
    depressive symptoms were MIXED and depended on the type of sleep loss. Short
    sleep reliably SUBTRACTS enjoyment and responsiveness; it does not reliably ADD
    misery. Effects were also nonlinear in the amount lost and differed by sleep
    stage, so no per-hour conversion may be built. Item 014.
  - "Your tracker can tell how you're feeling." REJECTED. De Angel 2022 (npj
    Digital Medicine, 51 studies) found consistent bivariate associations between
    depression and sleep, activity, location and phone-use features, and then
    stated that the results "should be taken purely as a starting point for
    hypothesis generation", citing small samples, short follow-up, unreported
    feature construction and unreported missing-data handling. Two structural
    problems compound it: sensor data goes missing for behavioural reasons, so the
    gaps are not random, and studies construct and test many features per study
    without correction. Note also the DIRECTION: that sleep and movement change
    during a depressive episode is near-definitional and does not license the
    converse inference. Item 013.
  - "Sleep and mood are correlated, so this person's short night explains their
    flat afternoon." REJECTED as an inference type, not as a specific claim.
    Fisher 2018 (PNAS) found variance 2-4x larger WITHIN individuals than within
    groups across six repeated-measures samples, meaning a group-level correlation
    systematically understates individual variability and does not transfer to a
    person. Item 012 carries this at the trial band; the stronger ergodicity
    conclusion built on it drew FOUR published PNAS commentaries in 2019 and is
    carried lower and flagged contested, because laundering the disputed half into
    the measured half would be the exact failure this warehouse exists to prevent.
  - "Long working hours cause depression", quoted at a single global figure.
    REJECTED as region-invariant. Virtanen 2018 (SJWEH, 10 published cohorts plus
    unpublished individual-participant data from 18 more, 189729 participants, 35
    countries, 21747 new-onset cases) reports an overall association of 1.14 (95%
    CI 1.03-1.25) for 55+ hours per week -- small, with the lower bound at 1.03 --
    and a regional split of 1.50 (1.13-2.01) in ASIA, 1.11 (1.00-1.22) in Europe,
    0.97 (0.70-1.34) in North America and 0.95 (0.70-1.29) in Australia. The
    authors report the divergence without identifying a mechanism. This is direct
    within-study evidence that the WEIRD-sampled default estimate does not
    describe this warehouse's own locale, and it points the opposite way from the
    usual assumption. Item 016.
  - "Switching off from work reduces exhaustion." REJECTED as causal. Wendsche and
    Lohmann-Haislah 2017 (86 publications, 91 samples, N=38124) reports detachment
    correlating -0.36 with exhaustion, -0.42 with fatigue and +0.32 with general
    wellbeing -- from a largely CROSS-SECTIONAL literature, in which "exhaustion
    prevents switching off" and "a demanding job causes both" fit the same numbers
    equally well. The correlations are real; the arrow is added by the reader.
    Item 016.
  - "Korea has unusually high rates of mental illness." NOT SHIPPED, and refused
    in the direction people expect it to go. Kang et al. 2026 (Psychiatry
    Research) open by stating that the prevalence of mental disorders in Korea is
    COMPARABLE to that in other countries while service use remains markedly low.
    The Korean difference this warehouse records is a HELP-SEEKING difference, not
    a prevalence difference. Item 020.
  - INSTRUMENT-COMPARISON TRAP, a ledger category worth naming. Korean 12-month
    prevalence figures from the National Mental Health Survey (1.7% depressive
    disorder, 3.1% anxiety disorder) come from a structured DIAGNOSTIC INTERVIEW.
    Levis 2019 (BMC Medicine, 69 meta-analyses) shows pooled prevalence runs at
    about 31% from screening tools versus about 17% from diagnostic interviews.
    Setting an interview-based Korean figure against a questionnaire-based figure
    from elsewhere is not a cross-country comparison; it is an instrument
    comparison wearing a flag. Items 011 and 020.
  - STALENESS CATCH, on the discipline the warehouse established for Korean
    reference intakes and the Korean tax regime: the National Mental Health Survey
    of Korea figures in item 020 are the 2021 edition, published 2023, with the
    decade comparison published 2026. The survey runs on a cycle, so any figure
    must be re-checked against the most recent edition before it is quoted, and
    any Korean figure recalled from memory is almost certainly a prior edition.
  - SEARCHED AND NOT FOUND, recorded so the absence is not read as an all-clear:
    no peer-reviewed validation of a shipped CONSUMER STRESS OR MOOD SCORE against
    a measured affect outcome was located in this sprint. What the search returned
    is algorithm-development-and-validation work on bespoke physiological signals.
    Exactly parallel to the sleep domain's proprietary readiness-score gap, and
    handled the same way: a hole in the evidence, NOT a finding against the
    devices.
  - NOT REJECTED, NOT SHIPPED, left open for the next sprint: loneliness and
    social contact (a genuine coverage hole, and the most obvious next candidate
    since a life agent can observe social contact in a calendar); ecological
    momentary assessment reactivity, searched without a clean meta-analytic
    anchor; Korea-specific workplace detachment and recovery data, not located, so
    the detachment correlations in item 016 remain WEIRD-sampled; and
    sex-conditioned and age-conditioned effects, which are unexamined across this
    entire domain. See the mental-health section above for what would close each.

## spending-saving

Added 2026-09-02 by the spending-saving lane opening (v18). The
@household-behavioral lane went from 0 to 16 items in that pass. This is the
first domain in the warehouse that did NOT already exist in the v3 lane map --
it was created because the owner's own area taxonomy holds 소비/저축 and 투자 as
two separate areas, and the warehouse had covered only the second.

WHY A SEPARATE DOMAIN, NOT AN EXTENSION OF finance-investing. Three reasons, in
order of weight. The domain slug is the stable ID prefix and is never reused or
renamed, so filing household spending under a prefix that says "investing" would
mislabel it permanently. The verification cultures genuinely differ: the
@quant-market lane grades against arithmetic identities, cross-sectional return
distributions and post-publication alpha decay, none of which have any analogue
here, while this lane grades against measurement validation, randomised field
experiments and behavioural replication risk. And the modules are being designed
from the owner's area view, so merging the two would put the knowledge model out
of step with the product model. The two curator checklists
(finance-investing/curator-checklist-017 and spending-saving/curator-checklist-016)
state the grading differences explicitly rather than leaving them implied.

WHAT THIS LANE LOOKS LIKE. It is measurement-first by construction. The top-band
item is not a behavioural finding but a measurement one -- self-reported spending
is mis-measured, and NOT uniformly (item 002) -- because in this domain the
recording instrument is the primary source of error and the agent's whole input
is a self-report. That mirrors the nutrition lane's structure, where
nutrition/self-report-underreporting-007 plays the same role for a meal log, and
the two items were written to be read together. The finding does NOT reproduce
the nutrition pattern exactly, and the difference is the point: dietary
self-report understates fairly systematically, while spending self-report is
accurate on some categories, poor on others, good on outflow and bad on
liabilities, and fails by producing ZEROS rather than smaller numbers (item 003).

Rejected-claim ledger, v18 (a popular rule that failed verification is
recorded here, not silently dropped, so a later sprint cannot re-adopt it):

- THE 50/30/20 RULE (50 percent needs, 30 percent wants, 20 percent savings).
  REFUSED OUTRIGHT, no item at any band. It originates in a 2005 trade book and
  no study deriving, testing or validating the split against outcomes was
  located. It is not a distorted version of a real finding, which is the usual
  case in the clinical lanes; there is nothing underneath it. Recorded so that
  its ubiquity is never mistaken for evidence. The same refusal covers every
  competing fixed-ratio budget (70/20/10, 80/20 and the rest) for the same
  reason: a ratio with no measurement behind it.

- THE LATTE FACTOR. REFUSED OUTRIGHT. Two separate defects. There is no study
  establishing that eliminating small recurring discretionary purchases produces
  the claimed wealth outcome, and the arithmetic version of the claim is a
  compounding assumption dressed as a finding -- it asserts a return, a horizon
  and perfect redirection of the saved money, none of which are measured. Note
  the direction this cuts for a Korean ledger with 카페/간식 as a live category:
  refusing the rule does NOT mean small recurring costs are unimportant, it means
  the specific claim has no evidence. What IS evidenced about recurring costs is
  in items 009 and 010, and both are about inattention and contract choice, not
  about the size of the individual purchase.

- "PAY YOURSELF FIRST" AS A QUANTIFIED EFFECT. REFUSED as stated, and SHIPPED
  ONLY IN CORRECTED FORM. No measurement of the slogan itself was located. What
  is measured, and is now item 006, is a sharper and different claim: saving that
  happens WITHOUT A DECISION dominates saving that requires one, with roughly 85
  percent of the Danish population behaving as passive savers and each dollar of
  savings subsidy raising total saving by about a cent. The operative variable is
  the absence of a required action, not the ordering of the transfer, and an
  agent that tells someone to "save first" has not implemented the finding.

- ENVELOPE BUDGETING EFFECT SIZES. REFUSED. No effect size for envelope
  budgeting as a general practice was located at any tier. One real field
  experiment survives and is shipped as item 011, and its scope is far narrower
  than the advice it is used to support: 146 rural Indian day labourers paid in
  weekly cash with no bank accounts, physical sealed envelopes, 14 weeks. Its
  transferable content is that PARTITIONING beats labelling and that raising a
  savings target without a partition BACKFIRED. A labelled digital sub-account
  is not the tested object and no evidence was found that it reproduces the
  effect.

- EMERGENCY-FUND MONTH COUNTS (three months, six months, twelve months).
  REFUSED, holding the line already taken by the investing lane. That lane's v12
  ledger records that no defensible evidence base for any specific number of
  months was located; this pass searched again from the spending side and found
  nothing further. The absence is now recorded in BOTH lanes so neither can be
  used to imply the other has an answer.

- "YOU SPEND N PERCENT MORE WITH A CARD THAN WITH CASH." REJECTED as stated,
  SHIPPED IN CORRECTED FORM as item 012. The effect is real and the circulating
  magnitude is not: the meta-analysis over 392 effect sizes from 71 papers puts
  the grand mean at g = 0.135 with very high heterogeneity, finds that the
  payment-method features the mechanism story rests on do NOT independently
  moderate it, and finds the effect has declined linearly over time. In a market
  as far into cashless payment as Korea the current effect should be expected at
  the low end. Same failure mode as the warehouse's other zombie statistics: an
  early, small, striking experiment outliving the synthesis that superseded it.

- "TRACKING YOUR SPENDING SAVES YOU N PERCENT." REFUSED. No money-specific
  measurement supporting any such figure was located. The evidence that
  monitoring works is domain-general (item 001: 138 randomised studies,
  d+ = 0.40 on goal attainment, overwhelmingly health and performance), and the
  single located randomised trial of an actual budget-recording tool moved
  knowledge and left saving unchanged while INCREASING credit use (item 014).
  Quoting the general monitoring effect as an expense-tracking effect is a
  domain-transfer error and is trigger (3) on the lane checklist.

- "FINANCIAL EDUCATION DOESN'T WORK" (and its mirror, "financial education
  works"). REFUSED AS SETTLED IN EITHER DIRECTION, shipped as contested (item
  013). Two flagship-journal meta-analyses disagree, and they disagree because
  the randomised evidence base grew from 13 trials to 76 between them. Both
  agree on the ceiling -- effects in fractions of a standard deviation, decaying
  with time since delivery, best delivered just-in-time against a live decision
  -- and that agreement, not either headline, is what an advising product should
  calibrate to.

- "체크카드가 무조건 유리하다" (the debit-card-is-always-better reading of the
  Korean card deduction). REFUSED as a blanket rule. The higher rate is real, but
  the statute puts a 25 percent-of-gross-salary floor in front of it, caps the
  annual total by income tier, and excludes large parts of household outflow from
  the base entirely. Below the floor the payment mix is irrelevant; above it the
  answer depends on total spend against salary. Item 015 carries the structure
  and the exclusions and explicitly refuses to be recited as a rate table.

- KR YOUTH SAVINGS PRODUCTS (청년도약계좌 and successors). REFUSED for this
  pass, and the reason is itself the lesson. The product most likely to be
  recommended by an agent working from general knowledge appears to have stopped
  accepting new enrolment at the end of 2025, with a differently-named successor
  in 2026, and NEITHER the closure nor the successor's terms could be confirmed
  at a government primary source in this pass -- only at secondary write-ups,
  which this lane does not accept. Shipping any parameter here would have baked
  in a number that was already wrong. -> A sprint should read the 금융위원회 and
  서민금융진흥원 primary pages directly and ship with a verification date, or
  keep refusing.

- KR HOUSEHOLD SPENDING UNDER-REPORTING MAGNITUDE. REFUSED as unsourceable in
  this pass. There is a Korean literature comparing 가계동향조사 consumption
  against 국민계정 private consumption and reporting a substantial gap, but the
  primary sits behind a Korean journal paywall and was not read at source, so no
  figure is carried. Item 002 therefore states plainly that no Korean validation
  of a consumer spending log against an external benchmark was located.
  Explicitly NOT inferred from the US benchmark ratios, which are a different
  instrument against a different national accounts system.

Coverage this lane implies but this pass does not supply:

- ANY KOREAN BEHAVIOURAL MEASUREMENT. Every behavioural item here (004, 005,
  006, 007, 008, 009, 010, 011, 012, 014) is US, Philippine, Indian, Peruvian or
  pooled-international. The only Korean item in the lane is a statute (015).
  Whether Korean households show the same self-prediction bias, the same category
  malleability or the same subscription inertia is unmeasured here. This is the
  lane's largest structural hole and it is the same hole the investing lane
  records for KR-specific return and behaviour evidence.

- INCOME-ARRIVAL AND PAY-CYCLE EFFECTS. Not shipped. The literature exists
  (consumption spikes at benefit and payday arrival, and drops at benefit
  exhaustion) and is directly relevant to a ledger of date-stamped entries, but
  the primaries located are US transfer-recipient and unemployment-insurance
  populations and none were read at source in this pass. -> A sprint should read
  them and ship a properly bounded timing item, or record why not.

- THE EFFECT OF CATEGORISATION SCHEME ON BEHAVIOUR. Item 004 establishes that
  people move expenses between ambiguous categories to justify spending. Whether
  a FIXED, agent-assigned category scheme changes behaviour relative to a
  user-chosen one is the obvious product question and no evidence on it was
  located at any tier.

- ANY MEASURED CONSEQUENCE OF LOG COMPLETENESS. Item 003 establishes that diary
  instruments fail by producing zeros. No study was located that measures how a
  personal ledger's coverage decays over time, which is the number an agent would
  need to distinguish a real spending drop from a logging drop. -> This may be
  measurable from the instance's own data rather than from literature.

- OPTIMAL REVIEW CADENCE. Nothing at any tier on how often a spending review
  should happen. The monitoring meta-analysis (item 001) reports that physically
  recorded and publicly reported monitoring works better, but says nothing about
  frequency, and no frequency comparison was located.

Size update 2026-09-02 (after v18). Counts computed at apply time from
disk, not asserted:

  exercise 30
  mental-health 20
  finance-investing 17
  relationships-communication 17
  spending-saving 16
  nutrition 15
  learning-habits 13
  sleep-recovery 13
  cooking 12

  = 153 RAG items + 2 E-records. exercise is 20% of the warehouse.
  spending-saving enters at 16 items.
- Size update 2026-09-02 (after v19): exercise 30, mental-health 20, finance-investing 17, relationships-communication 17, spending-saving 16, nutrition 15, home 13, learning-habits 13, sleep-recovery 13, cooking 12
  = 166 RAG items + 2 E-records. Exercise is now 18% of the warehouse.
  The `home` domain opens at 13 items across two lanes, filled along the
  owner's own taxonomy rather than the warehouse's. Note what the number
  means before reading it as thin coverage: this domain is almost entirely
  folklore with a thin scientific core, and the rejected-claim ledger below
  is longer than the shipment. Counts computed at apply time, not asserted.
- Rejected-claim ledger, v19 (home-domain opening sprint). This domain is
  almost entirely folklore with a thin scientific core, so this ledger is the
  larger and more informative half of the release. Each entry is a claim that
  was researched and NOT shipped as stated, recorded so it cannot be quietly
  re-adopted by a later sprint:
  - "Microwaving or boiling your kitchen sponge sanitises it." REFUSED. And the
    viral OVER-CORRECTION -- "sanitising your sponge selects for pathogens and
    makes it worse" -- is refused too, in the same item. The 2017 observational
    finding behind the over-correction is confounded by indication: users chose
    whether to clean, so the sponges being cleaned may be the sponges that
    provoked cleaning. The controlled follow-up (20 participants, 4 weeks, 10
    assigned to a standardised microwave protocol) found altered composition and
    metabolic properties, and its own authors write that follow-up studies will
    have to show whether the changes are more positive or negative. A
    metagenomic shift with no health endpoint is not a hygiene result in either
    direction. Item 011. Refusing BOTH directions is the finding.
  - "Antibacterial soap kills more germs than plain soap." REFUSED on the
    regulator's own adjudication, not on scepticism. FDA 2016 final rule (81 FR
    61106): 19 active ingredients including triclosan and triclocarban found not
    generally recognised as safe and effective for consumer antiseptic washes,
    because the submitted data were insufficient to demonstrate ANY additional
    benefit compared to non-antibacterial soap and water, and the available
    information was insufficient to establish the safety of long-term daily
    repeated exposure. Note the burden direction: the industry held it, had an
    open docket, and did not meet it. Item 010. Scope caveat carried with the
    refusal -- this rule does NOT cover alcohol hand sanitisers, health-care
    antiseptics, first-aid antiseptics or food-industry antiseptics, and citing
    it against hand sanitiser is citing the wrong document.
  - "Vinegar and baking soda are effective disinfectants." REFUSED as a
    disinfection claim. Quantitative suspension test: vinegar under 3 log10
    against S. aureus and E. coli, baking soda under 3 log10 against ALL test
    pathogens, while the commercial comparators completely inactivated both
    resistant and susceptible bacteria at both exposure times. Note the
    precision that keeps this honest: nothing here is a claim against vinegar or
    baking soda as CLEANING agents, and physical soil removal is a separate and
    real mechanism. Item 012.
  - "Vinegar plus baking soda" as a cleaning hack. REFUSED FOR TOTAL ABSENCE OF
    A SOURCE, in either direction. No primary measurement of the mixture's
    cleaning or antimicrobial performance was located at all. Not endorsed, not
    debunked -- there is nothing to cite. Recorded because the acid-base
    chemistry is trivial enough that it is tempting to reason from mechanism to
    a performance claim, which is exactly the move this warehouse refuses.
  - "Cleaning products damage your lungs as much as smoking 20 cigarettes a
    day." ZOMBIE STAT, REJECTED. The underlying study (Svanes 2018, ECRHS, 6235
    participants, 20-year follow-up) is real and its finding survives in hedged
    form on item 009: FEV1 decline of -22.1 vs -18.5 ml/yr in women who clean at
    home, -22.4 in occupational cleaners, and NOT significant in men. The paper
    contains no smoking comparison arm and no cigarette-equivalence
    calculation. The comparison entered circulation through the publishing
    institution's own news page, not through the peer-reviewed text. Same
    failure mode the warehouse already catches with
    relationships-communication/source-misattribution-rule-005: the study is
    real, the number attached to it in public was manufactured around it.
  - "CO2 above about 1000 ppm measurably impairs your thinking." REFUSED AS
    STATED, corrected version shipped. Zhang 2017 separated the marker from the
    mixture: adding PURE CO2 produced no significant effect on perceived air
    quality, symptoms or cognition, while human bioeffluents at a CO2 level of
    3000 ppm degraded all three. Same meter reading, opposite result. The
    office study that put this claim into circulation varied ventilation,
    volatile organic compounds and CO2 together and therefore cannot adjudicate
    it; it is not cited in the shipped item. The 2023 meta-analysis (15 studies)
    finding complex-task decrements below 5000 ppm IS carried as the contrary
    evidence, along with its authors' own description of the field's consistency
    as disappointing. Item 005 ships CO2 as a ventilation proxy only.
  - Air-purifier performance and health marketing. REFUSED WHOLESALE, and no
    manufacturer document was consulted as a source at any point -- a device
    maker is not a source for its own device's efficacy. What shipped instead
    (item 006) is a 2024 review's ordering: policy and SOURCE CONTROL are the
    most effective approaches while engineering interventions such as air
    cleaners have attracted the most research attention. Two claims that get
    merged are separated in the item: that a portable cleaner lowers particle
    concentration in its room is a physical measurement and is not disputed;
    that this produces a measured health improvement is a separate and weaker
    question. NO effect size is carried, because the source is a review with
    recommendations and contains none. Population limit recorded: the evidence
    base is people with chronic respiratory disease, not the healthy adults most
    devices are sold to.
  - Mould air sampling, spore counts and species identification as a way to
    judge a home. REFUSED on WHO's own words, quoted in item 002: "as the
    relations between dampness, microbial exposure and health effects cannot be
    quantified precisely, no quantitative health-based guideline values or
    thresholds can be recommended for acceptable levels of contamination with
    microorganisms." There is no number to compare a measurement against. Any
    pass/fail verdict sold against a measured mould level is selling a threshold
    the responsible authority explicitly declined to set. Note the direction:
    this does NOT weaken item 001, it weakens only the measurement layer sold on
    top of it.
  - "40-60% is the ideal indoor relative humidity." REFUSED AS UNSOURCEABLE in
    this pass. No primary study establishing that range as a health target was
    located; the range traces to a mid-1980s narrative chart in a
    building-engineering proceedings, not to a trial. WHO's refusal to set any
    microbial threshold (item 002) points the same way. If a defensible humidity
    target exists it is likely to be surface-condensation-based rather than a
    room-air range, which routes it to the Korean 결로 design standard -- see
    the home section's gap 2. Not shipped in any form.
  - Decluttering and tidying method effect sizes (KonMari and the wider genre).
    REFUSED. A targeted search for controlled evidence returned trials and
    protocols for HOARDING DISORDER -- a clinical population, with decluttering
    as an augmentation to group CBT -- and an educational-programme trial for
    people with difficulty decluttering. Nothing was located that measures an
    effect of a tidying method on wellbeing or productivity in a general
    population. The genre's confident before/after claims have no
    general-population trial behind them. Same shape as the v13 rate-of-gain
    finding and the v9 load-increment finding: the most confidently quoted
    numbers in an area are the ones nobody has measured.
  - "Bug bombs will handle a bed bug problem." REJECTED, and shipped as item
    007: three consumer total-release foggers against five bed bug populations,
    little if any adverse effect, because foggers deposit on exposed surfaces
    and bed bugs live in harbourages. SCOPE HELD DELIBERATELY NARROW and
    recorded here as a limit, not a finding: no evidence was located for foggers
    against cockroaches, ants or any other household pest, and the null does not
    transfer.
  - Laundry temperature and textile hygiene. RESEARCHED AND REFUSED THIS PASS,
    for source-access reasons rather than for a negative finding, and recorded
    so the absence is not read as an all-clear. The candidate sources located
    (Bockmuhl 2017 J Appl Microbiol; Bockmuhl, Schages, Rehberg 2019 Microbial
    Cell) are NARRATIVE reviews with no pooling and no risk-of-bias assessment,
    and neither could be read at full text at source in this pass -- only
    abstract and search-snippet level. Shipping a washing-temperature threshold
    from snippets would have been exactly the laundering-of-a-secondary-source
    failure this sprint was built to avoid. Nothing shipped. Funding and
    conflict-of-interest status of the candidate sources was also NOT checked,
    which matters in a field adjacent to detergent manufacture; check it before
    adopting them.
  - Korean high-PM2.5 (고농도 미세먼지) ventilation guidance. SEARCHED, NOT
    VERIFIED AT A REGULATOR SOURCE, NOT SHIPPED. This is the most practically
    valuable open question in the domain for a Korean user and it is honestly
    unanswered here rather than answered from a US/EU analogue.
  - Korean new-apartment radon EXCEEDANCE RATE. NOT CARRIED. Figures for the
    share of new Korean apartments exceeding the 148 Bq/m3 recommended standard
    circulate through news coverage of parliamentary audits; no ministry-issued
    dataset was located and read at source. Item 003 carries the standard and
    the disclosure duty, and deliberately carries no percentage.
  - STALE-FIGURE CATCH, the same category v13 opened for the Korean dietary
    reference intakes: the 100-unit applicability threshold for Korea's
    apartment ventilation requirement. Korean secondary summaries, including
    high-ranking search results, still state that 건축물의 설비기준 등에 관한
    규칙 제11조 applies to apartment complexes of 100 or more units. The current
    rule text (국토교통부령 제1614호, in force 2026-08-24) says 30. Carried as a
    refraction note on item 004. Generalisable lesson, restated: a
    jurisdiction-bound item needs an EDITION check, not merely a source check.
  - DELIBERATE NON-OVERLAP, recorded so it is not mistaken for a gap: food
    handling, cutting-board material, refrigerator temperature and
    cross-contamination to food were left entirely alone. They are cooking
    domain @food-safety questions, that domain was being expanded concurrently
    with this sprint, and duplicating them here would have created two homes for
    one claim. Item 011 (kitchen sponges) is filed under household labour
    because its claim is about a cleaning ritual, and it carries an explicit
    note handing the food-contact questions to cooking.
  - NOT RESEARCHED AT ALL, listed so later sprints know these are absences and
    not negative findings: gas cooking and NO2; carbon monoxide alarms in Korean
    housing; bedroom CO2 and sleep; ondol floor heating and indoor air; Korean
    housing dampness prevalence; what actually works against household pests.

- Size update 2026-09-02 (after v20): exercise 30, mental-health 20, work-career 20, finance-investing 17, relationships-communication 17, spending-saving 16, nutrition 15, home 13, learning-habits 13, sleep-recovery 13, cooking 12
  = 186 RAG items + 2 E-records. Exercise is now 16% of the warehouse.
  work-career opens at 20 items, split 15 @behavioral-career
  (employment / career development) and 5 @venture-obs (independent and
  side work). Lanes registered in lanes.yaml still holding zero items
  after this release: 0. The employment/independent imbalance is real
  and is argued in the work-career section above, not smoothed over.
  Every count on this line was computed at apply time from disk, not
  asserted.
- CONCURRENT-WRITE INCIDENT observed while preparing v20, recorded here
  because it is a warehouse-integrity fact and not a content one. The
  finance-investing lane opening (v12, applied 2026-09-02 10:59) shipped a
  `## finance-investing` GAPS.md section containing its own rejected-claim
  ledger. That section is NOT present in the live GAPS.md, although the v12
  CHANGELOG release and all 17 items are. The v12 package used a WHOLE-FILE
  preimage-and-replace strategy for GAPS.md; a later package that same hour
  replaced the file from a snapshot that did not contain it. The lesson is
  mechanical: in a warehouse with concurrent writers, a package must only
  INSERT and APPEND at unique anchors, never rewrite a whole shared file.
  v20 was built that way -- registry.yaml, lanes.yaml and this file are
  appended to or inserted into, never replaced. Recovering the lost v12 GAPS
  section is possible from the v12 package's own payload and is left as a
  separate action, deliberately not bundled into this release.
- Rejected-claim ledger, v20 (work-career lane opening). Each entry is
  a widely circulating career claim that was researched and NOT shipped as
  stated, so it cannot be quietly re-adopted by a later sprint. This is the
  longest such ledger in the warehouse so far, which is the correct shape for
  this domain rather than a sign the sprint went badly:
  - "General mental ability is the single best predictor of job performance."
    REFUSED AS STATED, and this is the domain's largest single correction. The
    figure behind it (.51) comes from Schmidt and Hunter 1998 and was revised
    to .31 by Sackett et al. 2022, who show the field's range-restriction
    corrections systematically overcorrected. In the revised table the
    structured interview (.42) and the job knowledge test (.40) both outrank
    it. Note carefully what kind of rejection this is: the original number was
    not fabricated and the predictor is not useless -- the correction method
    was wrong, and the ORDERING changed. Also note the correction is itself
    disputed (Oh, Le and Roth 2023 in the same journal, with a reply from
    Sackett et al. in the same issue), which is why item 001 ships contested.
  - The whole pre-2022 personnel-selection validity table, quoted as current.
    REFUSED. Work samples .54, integrity tests .41, conscientiousness .31,
    unstructured interviews .38, experience .18 -- every one of these is a
    superseded estimate and every one is still in circulation in careers and
    HR writing. Item 001 stores the revised values WITH the prior value
    attached specifically so a later reader who meets the old figure
    recognises it as the old figure rather than as corroboration.
  - "Grit predicts success." REFUSED as stated, with source. Crede, Tynan and
    Harms 2017 (584 effect sizes, 88 samples, 66,807 individuals) report that
    the higher-order structure of grit is not confirmed, that grit is only
    moderately correlated with performance and retention, that it is very
    strongly correlated with conscientiousness, and that interventions to
    enhance grit may have only weak effects. The perseverance-of-effort facet
    survives with incremental validity for academic performance; the popular
    construct does not. Item 004.
  - "10,000 hours" / deliberate practice as the lever for career success. NOT
    re-shipped into this domain. It is already carried at
    learning-habits/deliberate-practice-ceiling-005 (Macnamara 2014: practice
    explains about 12 percent of performance variance). This is a routing
    decision, recorded so a later sprint does not read its absence from
    work-career as an oversight and ship a duplicate.
  - "Emotional intelligence accounts for the large majority of career
    success." REFUSED OUTRIGHT. The percentage figures attached to this claim
    in popular management writing have no traceable primary study. A real
    meta-analytic literature on emotional intelligence and job performance
    exists and reports modest incremental validity; the popular number is not
    from it. Nothing was shipped, because verifying the real literature at
    source was out of scope for this pass -- recorded as a gap, not as a
    finding.
  - MBTI / personality-type job fit. REFUSED. No defensible primary evidence
    that type assignment predicts job performance or job fit was located, and
    the instrument's own psychometric criticism literature is the more
    commonly cited body of work. Not shipped in either direction.
  - "People leave managers, not companies." REFUSED as evidence-backed. This
    is a consultancy assertion with no primary study behind it. Note the
    contrast with item 010, where the organisation-versus-individual
    distinction IS supported by a controlled meta-analysis -- the shape of the
    claim is plausible, its usual citation is not a source.
  - "Companies with more diverse executives outperform financially", as
    supported by the McKinsey Diversity Matters / Delivers / Wins series.
    REFUSED, with a named failed replication: Green and Hand 2024 (Econ
    Journal Watch 21(1), 5-34) revisited McKinsey's tests on S&P 500 firms as
    of 2019-12-31 and found no statistically significant relation between
    McKinsey's diversity measure and industry-adjusted EBIT margin, sales
    growth, gross margin, return on assets, return on equity or total
    shareholder return. This is the domain's canonical consultancy-white-paper
    case and is why trigger (5) exists on item 020. Nothing is asserted here
    about the underlying question, only about that evidence.
  - "Working from home makes you 13 percent more productive." REFUSED AS
    TRANSPLANTED. The figure is real and correctly reported in Bloom et al.
    2015, but it describes call-centre employees who VOLUNTEERED, at one
    Chinese firm, over nine months, and 9 of the 13 points came from working
    MORE MINUTES rather than working better. The same paper reports that their
    promotion rate conditional on performance FELL, which is almost never
    quoted alongside it. Same handling as the exercise domain's Hostler 2001
    entry and the sleep domain's Mah 2011 entry: the study exists, the popular
    retelling misrepresents what it supports. Item 011.
  - "Remote work is less productive", as a general claim. ALSO REFUSED, in the
    other direction. The strongest negative evidence (Gibbs et al. 2023,
    productivity down about 20 percent) measures FORCED full-time remote work
    during a pandemic, and the strongest recent trial (Bloom, Han and Liang
    2024, Nature) finds hybrid working cut attrition 33 percent without
    damaging performance. Neither side supports a general claim. Item 011
    ships contested for exactly this reason.
  - "90 percent of startups fail" / "9 out of 10 businesses fail in the first
    year". REFUSED. No primary source produces these numbers. The Korean
    administrative measurement is shipped instead: 64.4 percent survive one
    year and 36.4 percent survive five (통계청 기업생멸행정통계, 2024
    provisional). Item 015. The failure of the folk figure is not that it is
    pessimistic but that it is unsourced and one-year-anchored.
  - "Successful founders are young." REFUSED, with a full-population
    counter-measurement: the mean age at founding for the fastest-growing 1 in
    1,000 US new ventures is 45.0 (Azoulay et al. 2020), and this holds in
    high-technology sectors and entrepreneurial hubs. The youth belief is a
    textbook survivorship artefact -- it is produced by looking only at the
    famous young founders and never at the denominator. Item 017.
  - US establishment survival rates. NOT SHIPPED, for a mechanical reason
    worth recording: bls.gov returned HTTP 403 to every automated retrieval
    attempted, and the widely quoted figures were NOT taken from any of the
    secondary sites that repeat them. An unverifiable primary is an absence,
    not a licence to quote a blog. See the work-career section above.
  - Camerer and Lovallo (1999), American Economic Review 89(1), 306-318,
    https://doi.org/10.1257/aer.89.1.306. Citation fully resolved; no
    accessible full text or abstract could be read at source in this pass, so
    it was NOT used as evidence on item 018, which ships on Cooper et al. 1988
    alone. Same ledger category as the v9 "unverified locator" entries.
  - Salary negotiation VALUE claims -- any figure for what a single salary
    negotiation is worth over a career. REFUSED as unsourceable in this pass.
    Item 007 ships only what the meta-analytic moderator evidence supports.
  - First-offer anchoring in real salary negotiations. NOT REFUSED but
    DOWNGRADED and labelled: the effect is well replicated in laboratory
    studies with student participants (Galinsky and Mussweiler 2001) and has
    not been established at the same strength in field salary negotiations. It
    is carried on item 007 as the second and weaker half, never as a measured
    workplace result.

## nutrition -- craft lane (@meal-craft)

Added v21 (2026-09-02, nutrition craft-lane opening). This is a SECOND
section for the nutrition domain; the evidence-lane section above (`## nutrition`)
stays authoritative for @obs-inferential and is not superseded. Five items
(017-021) open @meal-craft, VC-E.

WHY THE LANE EXISTS. Before this release, exercise had three lanes, cooking had
two, and every other domain in the warehouse had exactly one -- the evidence
lane. What @gym-craft carries is the reason the exercise domain is usable: how
big a warm-up jump may be, how to cue a muscle that will not fire, what to do
when the plan does not survive contact with the gym floor. None of that is in a
paper. nutrition shipped 15 evidence items in v13 and zero craft items, while the
consumer reads the owner's meal log every single day. The evidence lane can now
say precisely how the logged number is wrong; it had nothing at all on what to do
about it.

THE STANDARD APPLIED. VC-E is a different standard, not a lower one. Each item
names its basis and marks the untested part as untested:
- nutrition/log-reask-multiple-pass-017 (@meal-craft, practitioner-protocol band,
  not contested) -- the USDA Automated Multiple-Pass Method's five passes, quoted
  verbatim from the publisher's own description: Quick List, Forgotten Foods, Time
  and Occasion, Detail Cycle, Final Probe. The craft content is the ORDER --
  omission is chased in a dedicated pass before any question of quantity, and
  amount is asked last. Validated against doubly labelled water in 524 adults
  (Moshfegh 2008): still 11 percent short overall, under 3 percent in
  normal-weight subjects, worst in obese subjects. The transfer to a chat-based
  self-log with no interviewer and no food model booklet is UNTESTED and the item
  says so. Also refuses to publish a numeric re-ask trigger, and routes instead
  to structural absence (a missing eating occasion) because the shortfall is
  person-dependent.
- nutrition/portion-estimation-shape-ceiling-018 (observational band, CONTESTED as
  under-evidenced) -- Gibson 2016, n=67, 42 pre-weighed foods. The best unaided
  technique put 80 percent of GEOMETRIC foods within 25 percent of true weight and
  only 13 percent within 10 percent; household cups and spoons managed 29 percent
  within 25 percent. For amorphous foods (cereal, mashed potato, muffin, RICE) not
  one estimate was within 10 percent and exactly one was within 25. For irregular
  protein pieces (fish fillet, chicken breast, beef steak) both methods were off by
  more than half. So portion estimation is a plus-or-minus-25-percent instrument at
  its ceiling, and it fails on exactly the two things a Korean training plate is
  made of.
- nutrition/unlogged-day-not-zero-019 (operating rule, empirically anchored, not
  contested) -- Fraser 2009: 2091 participants re-contacted, 92 percent of missing
  items recovered, and for frequently consumed foods most blanks were NOT zeros,
  with missingness non-random; the authors' stated conclusion is that automatic
  zero imputation will usually be incorrect. Rule: mark unknown, never write zero,
  never let an unknown day into an average or a streak or a trend, reconstruct only
  inside the previous-day window the recall instrument was actually validated for.
  Cross-domain corroboration of the MECHANISM ONLY from
  spending-saving/diary-attrition-zero-reporting-003: a decaying self-kept diary
  fails by emitting zeros, not smaller numbers. No rate imported.
- nutrition/kr-mixed-dish-logging-unit-020 (professional-tool convention, LOCALE
  KR, not contested) -- the item this lane was opened for. Two published Korean
  units coarser than grams: the clinical exchange system (식품교환표, per-exchange
  content quoted exactly from the Korean Diabetes Association) and the Ministry of
  Food and Drug Safety's measured restaurant-dish dataset (외식 영양성분 자료집,
  108 dishes in volume 2 alone). Rule: log a composite dish by NAME against a
  measured whole-dish entry or in exchange units; never itemise a 찌개 into grams.
- nutrition/kr-protein-exchange-counting-021 (professional-tool convention, LOCALE
  KR, not contested) -- protein against real Korean food. A meat-and-fish exchange
  is 8 g of protein at any fat tier, milk 6 g, grain 2 g, vegetable 2 g, fruit and
  fat none. A 밥 + 국 + 나물 meal of two grain and two vegetable exchanges is about
  8 g of protein in total, so a training target is met almost entirely on the 반찬
  side and essentially not at all by the 주식. Count exchanges, not grams.

WHERE CRAFT AND EVIDENCE DISAGREE. Recorded in the open rather than resolved by
quietly picking a side.
1. THE FLAT CORRECTION FACTOR. Adding a fixed percentage to a client's food log
   ("assume they ate 15-20 percent more than they wrote") is ordinary coaching
   practice. This warehouse's evidence lane forbids it:
   nutrition/self-report-underreporting-007 shows the bias is DIFFERENTIAL, and
   the AMPM validation independently reproduces that by body-mass group (under 3
   percent in normal-weight subjects, worst in obese subjects, from a completely
   separate pool of studies). A flat factor would replace a known bias with a
   hidden one. REFUSED. Evidence wins; the craft practice does not ship.
2. THE PER-MEAL EVEN-DISTRIBUTION PRESCRIPTION. Practitioners near-universally
   teach roughly four meals of 30-40 g. The evidence lane does not support it:
   nutrition/protein-distribution-thin-009 traces the concept to an n=8 acute
   crossover with two later randomised trials null at real outcomes, and
   nutrition/protein-per-meal-ceiling-008 removed the basis for the
   above-40-g-is-wasted warning. NEITHER SIDE IS SUPPRESSED: item 021 keeps a
   per-meal split, re-bases it explicitly on logging tractability and adherence,
   and forbids the physiological justification. Anyone stating the split must say
   which justification they are using.
3. A MAGNITUDE ORDERING THAT READS AS A DISAGREEMENT AND SHOULD BE SAID OUT LOUD.
   nutrition/kr-food-composition-accuracy-016 reports that the Korean tables
   validated cleanly for energy and protein. That is true and it is nearly
   irrelevant to a real Korean log, because item 018 shows the dominant error sits
   UPSTREAM of the table, in the portion, on exactly the amorphous staples the
   plate is built from. The convenient half of 016 invites precisely the wrong
   conclusion, and craft's job here is to say the table is not the problem.
4. A NUMERIC TENSION, not a contradiction. The AMPM's own validation reports an 11
   percent energy shortfall; item 007's pooled figure is about 15 percent for a
   single 24-hour recall and about 28 percent by food frequency questionnaire.
   Same direction, different pools, different instruments. Neither number may be
   quoted as "the" under-reporting figure.

REFUSED THIS SPRINT (recorded rather than dropped, v7/v9/v13/v18 rejected-claim
discipline). Each was searched, not assumed. THE REFUSALS ARE THE POINT OF A
CRAFT LANE: a craft lane is not a licence to ship folklore because no study
exists.
- KOREAN MIXED-DISH LOGGING ERROR, any figure. The evidence lane already refused
  this in v13 and the refusal STANDS. Craft does not fill an evidence hole by
  being confident. Item 020 ships the handling instead of the number, and states
  in its own body that item 016 cannot be extrapolated into one because that
  study's design removed exactly the portion and identification error in question.
- SHARED-DISH APPORTIONMENT. No published method was located for apportioning a
  shared Korean serving (공유 찌개, 공유 반찬). Item 020 ships a bounded-omission
  convention -- count what you can name, mark the shared broth present-but-uncounted
  -- and explicitly labels it the weakest thing in the item. It is chosen because
  its error has a KNOWN SIGN (undercount, same direction as every other error in a
  food record), NOT because it is accurate. An invented apportionment fraction
  would have an unknown sign and would destroy that property.
- KOREAN 눈대중량 / 손대중 PORTION TABLES. Searched directly. Everything located
  was blog posts and community-cafe reposts with no traceable origin. REFUSED
  OUTRIGHT. The only fetched primary on hand-based estimation is Gibson 2016,
  which is Australian, uses investigator-chosen foods, and reports outright
  failure on rice. What would close it: a Korean validation of visual or
  hand-based portion estimation against weighed reference portions of Korean
  foods.
- THE FLAT LOG-CORRECTION FACTOR. See disagreement 1 above. Refused.
- "ADJUST FROM THE OBSERVED WEIGHT TREND, NOT FROM THE LOGGED NUMBER." This is
  the single most useful craft rule a coach would state, and it was hunted for.
  The obvious citable source, Helms ER, Aragon AA, Fitschen PJ, J Int Soc Sports
  Nutr 2014;11:20, was READ DIRECTLY and does NOT contain the recommendation --
  it says only that intake will need adjusting over time as metabolic adaptation
  occurs. REFUSED rather than attributed to a paper that does not say it. Recorded
  here so a later pass does not re-attribute it. What would close it: a peer-
  reviewed practitioner recommendation or position stand that actually states
  outcome-driven adjustment. Note that the rate-of-loss figure often bundled with
  this rule is already owned, and already discounted, by
  nutrition/weight-loss-rate-lean-mass-012.
- RESTAURANT PORTION MULTIPLIERS ("a restaurant serving is N times a standard
  serving"). Not sourced. Item 020 routes 외식 to the ministry's measured
  named-dish values instead, which is a real number rather than a ratio.
- RECONSTRUCTION BEYOND THE PREVIOUS DAY. No instrument with any validation
  reaches further back than the previous day. Item 019 caps reconstruction there
  and deliberately publishes NO accuracy expectation for older reconstruction
  rather than offering a softened one.
- CONSUMER FOOD-TRACKING-APP DATABASE ACCURACY. Already refused in v13 (nothing
  KR-applicable, nothing adequately powered). NOT re-attempted this pass;
  recorded as untouched, not as absent.

RESIDUAL SUB-GAPS carried out of this sprint, each recorded on the relevant item:
1. The probe list inside the AMPM Forgotten Foods pass lives in the instrument,
   not in its published description, and was not retrieved. Item 017 carries the
   EXISTENCE and POSITION of that pass and deliberately does not invent its
   contents. What would close it: the AMPM instrument documentation itself.
2. No study compares itemised against whole-dish logging of a composite dish, in
   any population, for accuracy or for adherence. Item 020's central rule is
   argued from the measurement position, not measured. This is the highest-value
   thing a next pass could close.
3. No study compares exchange-unit counting against gram estimation. Item 021's
   counting convention has the same status.
4. Gibson 2016 is unreplicated, Australian, and its food set contains no Korean
   composite dish. Item 018 ships the shape-dependence and refuses the
   percentages as transferable.
5. The 외식 영양성분 자료집 itself was located but NOT read: retrieval exceeded
   the fetch size limit, so item 020 quotes no figure from the dataset and cites
   only the ministry notice describing it. The notice was additionally read from a
   MUNICIPAL REPOST rather than the ministry's own copy, which is recorded on the
   source line. An edition check (which volumes are current in 2026, and whether
   the 2010 consumption basis has been re-surveyed) is owed, per the v15 lesson
   that a jurisdiction-bound item needs an edition check and not just a source
   check.
6. Structural gap, axes: only items 017 and 021 carry applicability.axes, and the
   axes available are fitness-shaped. The axis a logging item would actually
   refract on -- whether the user has a kitchen scale at all, whether the meal was
   eaten alone or shared, whether the day was 외식 -- does not exist in the ledger.
   Adding axes is an append-only ledger change and was deliberately NOT attempted
   in a content-only release. This is the same finding the v15 cooking sprint
   recorded from a different direction, which makes it a warehouse-level signal
   rather than a per-domain one. Flagged for whoever owns the meal-logging module
   design.

Rerun-needed: none. Every source shipped in this release was retrieved directly
in this pass -- the AMPM five passes from the publisher's own description pages,
the AMPM validation and the two journal articles resolved to full bibliographic
records with DOIs, and the exchange table read from the issuing professional
society's own page. The two sources that could NOT be fully retrieved (the
external dataset PDF and the ministry's own copy of its notice) are named as
such on the item and nothing is quoted from them.

Warehouse size at the moment this section was appended (counted from disk by
apply.sh, not hardcoded at build time -- v11 to v18 all landed on 2026-09-02 and
several agents were writing concurrently):

  exercise 30
  mental-health 20
  nutrition 20
  work-career 20
  finance-investing 17
  relationships-communication 17
  spending-saving 16
  home 13
  learning-habits 13
  sleep-recovery 13
  cooking 12

  = 191 RAG items + 2 E-records across 11 domains.
  nutrition now splits 20 items across 2 lanes: @meal-craft 5, @obs-inferential 15

- Size update 2026-09-02 (after v22): exercise 30, mental-health 20, nutrition 20, work-career 20, finance-investing 17, relationships-communication 17, spending-saving 16, task-management 16, home 13, learning-habits 13, sleep-recovery 13, cooking 12
  = 207 RAG items + 2 E-records. Exercise is now 14% of the warehouse.
  task-management opens at 16 items -- a NEW domain, registry row and
  lane row included, built from zero rather than expanded from an
  existing stub. Note the shape rather than the count: two rows are
  verified negatives established by reading the primary source cover to
  cover (006, 011), one is a deliberate ABSENCE row (015), two ship with
  an explicitly stated retrieval limit rather than silently (010, 014),
  and the sprint's refusal ledger names eleven claims plus one new
  ledger category -- it is longer than several domains' entire item
  lists. The lane also carries ZERO
  Korean-primary sources, which is recorded as a searched absence rather
  than an unexamined one. Counts computed at apply time, not asserted.
- Rejected-claim ledger, v22 (task-management lane opening). This domain has
  the widest gap in the warehouse between popular authority and evidential
  strength, and the reason is structural: its famous claims are transmitted
  commercially, in books that sell, rather than through guideline bodies or
  papers. The sprint's operating rule was the relationships lane's -- refusing a
  famous claim with a stated reason beats shipping it. Each entry below was
  researched and NOT shipped as stated, so it cannot be quietly re-adopted:
  - "It takes 23 minutes 15 seconds to refocus after an interruption."
    REFUSED, and the refusal is established by direct reading rather than by
    failure to find. Both papers the figure is attributed to were downloaded and
    read in full: Mark, Gudith and Klocke 2008 (CHI '08, doi
    10.1145/1357054.1357072) and Mark, Gonzalez and Harris 2005 (CHI '05, doi
    10.1145/1054972.1055017). Neither contains the figure, and neither contains
    ANY time-to-refocus measurement. What the 2005 paper does measure is 25 min
    26 s of ELAPSED time before an interrupted working sphere was resumed on the
    same day -- a different quantity, describing a queue of other work rather
    than a cognitive recovery period -- with a standard deviation of 54 min 48 s,
    more than twice the mean. Worse for the popular version: the 2008 paper's
    actual result is that people completed interrupted tasks in LESS time with no
    difference in quality, paying instead in stress, frustration, time pressure
    and effort. So the study most often cited for "interruptions cost you time"
    found the opposite and the number attached to it is not in it. Item 004.
  - "Multitasking costs up to 40 percent of your productive time." REFUSED. The
    35-page primary (Rubinstein, Meyer and Evans 2001, JEP:HPP 27(4):763-797,
    doi 10.1037/0096-1523.27.4.763) was downloaded and read cover to cover for
    this purpose. It contains no percentage of productive time, no workday, and
    no measurement outside the laboratory; its four experiments had people
    alternate between classifying shapes and solving arithmetic, and its
    switching costs run from about 63 ms to roughly 1,100 ms. There is no
    quantity in the paper that a percentage of a working day could be computed
    from. The phrasing traces to a statement attributed to one of the authors in
    press material summarising the study; that page could not be retrieved in
    this pass (the publisher's site refused automated retrieval), so the ledger
    asserts only the verified half -- the number is not in the research. Item
    006. Same failure mode as
    relationships-communication/source-misattribution-rule-005.
  - THE 25-MINUTE POMODORO INTERVAL, and the 5-minute break attached to it.
    REFUSED as evidence-backed. No primary study establishing 25 minutes, or any
    other specific interval, was located. The nearest thing to a test is Biwer
    et al. 2023 (Br J Educ Psychol 93(S2):353-367, doi 10.1111/bjep.12593), and
    three details of it matter: its own "Pomodoro" condition ran 24 minutes of
    work and 6 of break rather than 25 and 5; it compared fixed schedules against
    SELF-CHOSEN breaks, not against another interval; and it found no difference
    between groups in invested mental effort or in task completion. What it did
    find is a mood and drift result -- students on a fixed schedule reported more
    concentration and motivation and less fatigue and distractedness. Pointing
    the other way entirely, the micro-break meta-analysis (Albulescu et al. 2022,
    PLOS ONE 17(8):e0272460) states there is no established standard for break
    length and reports that its only significant duration moderator favoured
    LONGER breaks (b = .07, p = .006). Note the direction carefully, because the
    over-read would be a worse error: structure is not being refused, the NUMBER
    is. Items 012 and 015.
  - "Implementation intentions have a medium-to-large effect (d = .65)." REFUSED
    AS CURRENT, and this is the cleanest zombie-stat catch in the warehouse
    because the correction was published by the same authors. Sheeran, Listrom
    and Gollwitzer (Eur Rev Soc Psychol 36(1):162-194, doi
    10.1080/10463283.2024.2334563) pooled 642 tests including unpublished ones
    and report d = .36 raw, Egger's b = 1.06 -- meeting the published threshold
    for "substantial" publication bias -- and a Robust Bayesian model-averaged
    estimate of d = .15 (95% CI .08-.22). Their own limitations section reads
    "publication bias was substantial" and "caution is warranted in interpreting
    findings from the present review". The effect EXISTS (BF_10 = 319.3); what is
    refused is the magnitude and the confidence with which it is spoken. Item
    003.
  - THE ZEIGARNIK EFFECT ("unfinished tasks stay in your mind"). REFUSED on its
    memory claim, which is the half every productivity argument uses. Ghibellini
    and Meier 2025 (Humanit Soc Sci Commun 12:962, doi
    10.1057/s41599-025-05000-w) screened 1,455 publications to 59 and found that
    excluding Zeigarnik's own 1927 data the recall ratio is 0.99, interrupted
    tasks account for 49.16% of what is recalled against a 50% null, and the
    averaged effect size is dz = 0.15. Her own study measurably moves the pooled
    estimate. The SEPARATE Ovsiankina resumption effect survives at 67.00%
    (66.79% excluding Ovsiankina's own data) against a 50% chance rate, so the
    correct handling is to split the pair rather than refute both: people do
    return to unfinished work, they just do not remember it better. Item 011.
  - "Procrastination is really perfectionism." REFUSED, and well powered enough
    to be called refuted rather than unsupported. Steel 2007 (Psychol Bull
    133(1):65-94, doi 10.1037/0033-2909.133.1.65) reports perfectionism at
    r = -.03 across K = 24, N = 3,884. Also refused from the same table:
    neuroticism (r = .24), rebelliousness and sensation seeking (r = .17) as
    explanations. Recorded because the folk account of a delayed task -- high
    standards, fear of imperfection -- is the first thing an agent will reach for
    and it is the one the data does not support. The same table carries the
    finding that makes this actionable: INTENTION correlates r = -.03 with
    procrastination (K = 8) while the intention-action gap correlates r = .29
    (K = 6), so strengthening someone's commitment is aimed at the wrong
    variable. Item 013.
  - GETTING THINGS DONE (GTD). REFUSED OUTRIGHT, not shipped at a low grade. A
    targeted search for any controlled test returned nothing. The one academic
    treatment located (Heylighen and Vidal 2008, Long Range Plann
    41(6):585-605) is by its own framing an argument that cognitive-science
    findings SUPPORT the method's recommendations -- a theoretical
    rationalisation, not a test -- and its authors note it would be interesting
    to test GTD empirically by comparing users against control groups, which is
    a statement that this had not been done. Recorded so a later sprint meeting
    that paper in a citation list cannot mistake it for evidence that the method
    works. Note the shape: this is not "GTD is wrong", it is "there is no trial",
    and the honest position is that the method's individual components are
    testable and untested.
  - THE EISENHOWER MATRIX / urgent-versus-important quadrants. REFUSED as
    evidence-backed. No primary study testing quadrant prioritisation against any
    alternative was located. Its provenance is also not what the name implies:
    the urgent/important distinction appears in a 1954 Eisenhower speech in which
    he attributes it to an unnamed former college president, and the 2x2 grid
    itself is a later popularisation. A named historical anecdote plus a grid is
    the entire evidential base. Recorded rather than dropped because its
    ubiquity makes it feel evidenced.
  - "A JOB / PROJECT SHOULD BE BROKEN INTO N ITEMS" and every daily task-count
    rule ("three most important tasks", a maximum open-item count, a
    focused-to-unfocused time ratio). REFUSED OUTRIGHT. A targeted search
    returned ZERO primary sources prescribing any of these. Shipped as an
    explicit absence item (015) rather than left in this ledger alone, for the
    reason the relationships lane established: a gap-file entry does not fire at
    answer time, and the predictable failure is a fluent invented number
    delivered beside sourced material and inheriting its authority. Note the
    scope: this is a SEARCHED ABSENCE, not a demonstrated null.
  - "Goal setting has systematic harmful side effects" AND "goal-setting theory
    is settled". BOTH REFUSED AS SETTLED, which is the unusual part -- the lane
    refuses the critique and the defence equally. Ordonez, Schweitzer, Galinsky
    and Bazerman 2009 (Acad Manag Perspect 23(1):6-16) and the same-issue reply
    by Locke and Latham (23(1):17-23) plus a further rejoinder (23(3):82-87) are
    a live, unresolved, published dispute between named principals, in which the
    theory's own authors accuse the critics of misreporting results. Shipped at
    the bottom band and flagged contested (item 014) with NO effect size quoted,
    because the full texts were not retrieved in this pass. Recorded because a
    task agent will otherwise import "set specific, difficult goals" as
    uncontested background.
  - KOREAN EVIDENCE OF ANY KIND IN THIS DOMAIN. REFUSED as unsourceable in this
    pass. One Korean-primary source was located -- a translation and validation
    of procrastination scales in a student and community sample -- and it is a
    measurement instrument rather than a behavioural finding, and the publisher
    refused automated retrieval, so nothing from it is asserted and no KR row was
    shipped. Explicitly NOT inferred from anything else: every substantive row in
    this lane is Western-sampled, and per the discipline in
    relationships-communication/kr-weird-transfer-gate-016 that makes transfer
    UNTESTED rather than shown to fail. Recorded so the absence is on file as
    searched rather than as unexamined.
  - SOURCING-LIMIT CATCH, a ledger category this sprint adds as the mirror image
    of a refusal: two rows in this lane are shipped with an explicitly stated
    retrieval limit rather than silently. Item 010 (target corruption of
    completion metrics) cites Bevan and Hood 2006 and Campbell 1979 whose
    abstracts, citations and positions were verified but whose FULL TEXTS were
    not retrieved; the item says so in its own frontmatter and quotes no figure
    from either. Item 014 does the same for the three goal-setting exchange
    papers. Worth recording as a category because the alternative -- shipping the
    row while quietly implying the paper was read -- is the failure this
    warehouse's whole grading apparatus exists to prevent, and it is a much
    easier failure to commit than fabricating a source.

- Size update 2026-09-02 (after v23): exercise 30, learning-habits 21, mental-health 20, nutrition 20, work-career 20, finance-investing 17, relationships-communication 17, spending-saving 16, task-management 16, home 13, sleep-recovery 13, cooking 12
  = 215 RAG items + 2 E-records. learning-habits goes to 21 across TWO
  lanes: @behavioral (13, evidence) and @study-craft (8, execution).
  Read the 8 against the refusal ledger below, not on its own -- this
  lane refused more claims than it shipped, which is the honest ratio
  for a subject whose folklore usually has nothing underneath it at
  all. Counts computed at apply time from disk, not asserted.
- Rejected-claim ledger, v23 (study-craft lane opening). This lane
  refused MORE than it shipped, and that ratio is the honest one for this
  subject matter. Study advice differs from the clinical lanes in a specific
  way worth recording: there, a folk claim is usually a distorted version of a
  real finding, and the repair is to ship the corrected form. Here, several of
  the most repeated rules have nothing underneath them at all -- no
  misinterpreted study, no superseded synthesis, nothing. Each entry below is
  recorded so a later sprint cannot re-adopt it by mistaking its ubiquity for
  evidence.

  - THE BOICE "NINE TIMES AS MANY PAGES" STATISTIC (variously quoted as 157
    pages versus 17 pages per year for daily writers versus binge writers).
    REFUSED OUTRIGHT as a zombie statistic. Sword (2016), who went back to the
    original article, reports that these figures "appear nowhere in the original
    article, except obliquely in a rather hard-to-interpret diagram." Same
    category as the exercise domain's Hostler entry and the sleep domain's Mah
    entry: a real study exists, and the number everyone quotes is not in it.
    Item 020 carries the refusal.

  - "WRITE EVERY DAY" AS AN EVIDENCE-BACKED RULE. REFUSED as stated, SHIPPED
    ONLY IN CORRECTED FORM (item 020). The evidence base is two small studies by
    one author, never replicated: ten hand-picked chronic procrastinators
    personally mentored and monitored twice weekly by the researcher, and a
    27-completer study (nine per group, 15 of 42 dropped out) whose CONTROL
    GROUP WAS INSTRUCTED TO ABSTAIN from all non-essential academic writing for
    ten weeks -- a baseline manufactured by instruction, not observed. Reported
    outputs were page counts that may have been longhand drafts. Against 1323
    academics surveyed in 15 countries, roughly seven in eight do not write
    daily, including the peer-nominated exemplary writers. What survives is a
    negative claim only; this lane does NOT ship a replacement cadence, because
    none is supported.

  - TWENTY-FIVE MINUTES (the Pomodoro session length). REFUSED as a number, at
    any band. Its author reports having experimented across roughly a five-to-
    thirty-minute range and settled on what suited him personally; no comparison
    of session lengths against any learning outcome was located. The practice of
    scheduling a bounded block is not refused -- it is a reasonable calendar
    habit -- but it ships with no learning claim attached. Item 021.

  - THE NINETY-MINUTE "ULTRADIAN" STUDY BLOCK. REFUSED AS UNSOURCEABLE, and the
    manner of the failure is the point. Every retrievable source applying the
    basic rest-activity cycle to study-session length was a productivity blog or
    a timer product's own marketing. Not one primary testing it as a
    study-session length was located. The underlying construct belongs to sleep
    research; its transfer to how long a person should study is an unsupported
    leap that has been repeated until it sounds established. Item 021.

  - STREAK AND "DON'T BREAK THE CHAIN" DEVICES, as study technique. REFUSED.
    Nothing was located that measures a streak device in a learning context at
    any tier. What exists is one qualitative study of recreational runners, a
    preprint on streak-breaking backfire, and retention figures published by an
    app vendor about its own product -- a conflict of interest identical to the
    one exercise/funding-coi-check-004 exists to flag. The refusal is not merely
    on absence: item 015's two measurements (the overshoot asymmetry, and
    savings on relearning still positive at 31 days) both price a missed day
    CHEAP, so a device whose mechanic is that a missed day destroys something
    accumulated is pointed the wrong way. Note also that this domain's own item
    003 already refuses the 21-day habit figure the chain metaphor is usually
    sold alongside.

  - A SPECIFIC IMPROVEMENT PERCENTAGE FOR ANY SCHEDULING ALGORITHM (e.g. "the
    modern scheduler beats SM-2 by N percent"). REFUSED as a shipped number. The
    peer-reviewed result (Ye, Su & Cao, KDD 2022, ~12.6 percent) was produced by
    researchers using the review data of the commercial vendor whose product it
    is -- the funding/COI structure this warehouse flags elsewhere -- and the
    community benchmark that gets quoted alongside it is self-published by the
    algorithm's own authors and not peer-reviewed. Item 014 ships only the
    qualitative claim that survives: interval arithmetic across hundreds of
    items is bookkeeping, and a scheduler is the thing that exists to replace
    it. Which scheduler is a product question this warehouse does not answer.

  - THE FIXED "SPACE AT 10-20 PERCENT OF YOUR RETENTION INTERVAL" RULE. REJECTED
    AS STATED, SHIPPED CORRECTED (item 014). It is a misstatement of the very
    paper it is attributed to: measured optimal gaps were 1, 11, 21 and 21 days
    for retention intervals of 7, 35, 70 and 350 days, and the fitted surface
    puts the one-year optimum at 23 days, "which is just 7% of the RI". The
    ratio DECLINES as the horizon lengthens, and the paper says explicitly that
    its estimates depart from fixed-ratio advice derived from shorter-term
    studies. A fixed percentage cannot describe a relationship that is not
    fixed.

  - THE TWENTY RULES OF FORMULATING KNOWLEDGE, AS A VALIDATED METHOD. REJECTED
    as stated, SHIPPED AS ATTRIBUTED PRACTITIONER CANON (item 017). It is one
    person's 1999 compilation and has never been tested as a set. The single
    rule carried forward -- keep each item to one retrieval -- is shipped with
    its STRUCTURAL argument stated openly (a compound item returns one pass/fail
    for several memories, so failure cannot be attributed and the easy parts get
    scheduled at the hard part's pace), so the reader can judge the reasoning
    rather than take the authority. The rest of the rule set is not carried.

  - THE EIGHT-LAPSE LEECH THRESHOLD AS A MEANINGFUL NUMBER. DOWNGRADED AND
    LABELLED rather than refused. It is a shipped software default with no
    derivation and no study behind it. Item 017 carries it as a tripwire that
    makes repeated failure legible at all, and says plainly that the number
    itself means nothing.

  - THE TEN-TO-ONE INTAKE-TO-REVIEW MULTIPLIER. DOWNGRADED AND LABELLED, not
    refused. The SHAPE is arithmetic and not in doubt; the multiplier is one
    application's published rule of thumb, tied to that application's default
    intervals, its retention target, and the individual's own failure rate.
    Item 018 carries it in exactly the position
    exercise/volume-landmarks-heuristic-015 carries per-muscle set counts:
    transparent default, adjustable, never a measured constant.
- Size update 2026-09-02 (after v24): exercise 30, learning-habits 21, mental-health 20, nutrition 20, work-career 20, finance-investing 17, relationships-communication 17, spending-saving 16, task-management 16, home 13, sleep-recovery 13, cooking 12, leisure 12
  = 227 RAG items + 2 E-records across 13 domains. leisure opens at 12
  items across three lanes, 6 of them flagged contested. Read the SHAPE
  rather than the count: two are outright refutations of famous claims
  (001 Mozart, 002 music-training transfer), one is a deliberate ABSENCE
  row (008 active-versus-passive leisure), one is a measurement rule
  (005 self-reported time use), one is the domain checklist (012), and
  exactly ONE states a clean positive actionable finding (006 skill
  decay with non-use). The sprint's rejected-claim ledger below is longer
  than its item list, which is the correct shape for the worst
  replication domain opened so far rather than a shortfall in it. Counts
  computed at apply time from disk, not asserted.
- Rejected-claim ledger, v24 (leisure-domain opening sprint). This domain
  is one of the worst in the warehouse for replication failure -- the arts,
  music, reading and drinking literatures between them contain more famous
  claims that did not survive than any other area opened so far -- so the
  sprint's operating rule was that REFUSING A FAMOUS CLAIM WITH A STATED REASON
  IS A BETTER OUTCOME THAN SHIPPING IT. This ledger is longer than the sprint's
  item list, and that is the result, not a side effect of it. Each entry was
  researched and NOT shipped as stated, recorded so it cannot be quietly
  re-adopted:
  - "Listening to Mozart makes you smarter." REFUTED, and shipped as a refutation
    (item 001). The pooled effect across close to 40 studies and more than 3000
    subjects is d=0.37 (95 percent CI 0.23-0.52) on ONE narrow spatial task, with
    formal evidence of publication bias requiring downward correction. The
    decisive result is not the size: effects were several times larger in studies
    run by the originating laboratory than in studies run by anyone else, which
    is a finding about the laboratory. The medical spin-off -- that the same
    sonata helps epilepsy -- was refused separately: the 2023 multiverse
    meta-analysis found eight usable studies totalling 207 participants, with
    further eligible studies omitted because authors would not release data.
  - "Music training raises IQ / helps children with maths and literacy." REFUTED,
    and shipped as a refutation (item 002). Sala and Gobet 2020, 254 effect sizes
    from 54 studies, N=6984: once study design quality is controlled the overall
    effect is null and highly consistent in being null. The positive effect
    (approximately 0.200) appears ONLY in studies that neither randomised
    participants nor used an active control. Note WHY this is stronger than an
    ordinary meta-analytic null: it does not average the positives away, it
    locates them in a design flaw. The three standard rescues -- start younger,
    train longer, different outcome type -- were tested in the same paper and all
    three failed.
  - "Reading fiction makes you more empathic." REFUSED IN THE FORM IT CIRCULATES,
    in two separable parts (item 003). The specific famous experiment -- a single
    short passage of literary fiction immediately improving theory of mind --
    failed a replication by three independent research groups with 792
    participants and four conditions, showing no advantage for literary fiction
    over popular fiction, non-fiction or no reading at all. The wider
    experimental literature does retain a small effect (g=0.15-0.16 across 53
    effects from 14 studies) and that half is shipped rather than refused. What
    is refused outright is the real-world claim: every outcome in this literature
    is a score on a test of reading emotion from photographs of eyes, nobody
    measured behaviour toward an actual person, and the meta-analysts themselves
    recommend that someone check whether it transfers.
  - "Going to museums and concerts cuts your risk of dying by a third." REFUSED
    AS A CAUSAL CLAIM, shipped as an association only (item 004). The hazard
    ratio of 0.69 is real in a 6710-person 14-year register-linked cohort. It is
    also an implausible causal magnitude for a discretionary leisure behaviour,
    the exposure is self-reported going-out behaviour in over-50s and therefore
    encodes health, money, mobility and company, reverse causation through
    undiagnosed illness has an obvious unmeasured path, and the paper states in
    its own results that causality cannot be assumed. A commentary in the Journal
    of Epidemiology and Community Health challenged what the data can say. The
    publication context was disclosed on the item rather than suppressed: this
    appeared in the BMJ's Christmas issue, confirmed by reading the article's own
    section heading "Christmas 2019: For Art's Sake". GENERALISABLE RULE, now
    gate 1 of this domain's checklist: in leisure epidemiology the exposure is
    almost always a proxy for being well enough to do the thing, so an effect
    size too large for the activity is evidence about the design.
  - Specific percentages for how often people reach flow at work versus at
    leisure. EXCLUDED, and this is a sourcing refusal rather than an evidential
    one. Figures of this kind circulate widely in secondary retellings of
    Csikszentmihalyi and LeFevre 1989 and none could be verified against the
    article itself. Handled the way this warehouse handles any figure that lives
    only in retellings -- the same disposition as the winter-oyster seasonal
    multiplier in the cooking lane and the smoking comparison in the
    relationships lane: the qualitative finding is carried, the number is not.
  - "Active, effortful leisure is better for you than passive consumption."
    REFUSED, and this is the sprint's most consequential refusal because it is
    the claim a life agent would most want (item 008, shipped as a deliberate
    ABSENCE row). Its empirical root is a single experience-sampling study from
    1989 in which 78 adults carried pagers for one week. No replication and no
    pooled effect size for flow was located. The design problem also survives
    scaling: challenge, skill and experience quality are all self-rated by the
    same person in the same instant, so part of the relationship is the
    instrument talking to itself, and people are at work during the hours they
    are most alert. NOTHING IN THIS WAREHOUSE LICENSES TELLING SOMEONE THEIR
    READING IS WORTH MORE THAN THEIR TELEVISION. It might be. Nobody has shown it.
  - "You will feel better after the holiday." REFUSED AS A PROMISE (item 007).
    The entire evidence base after methodological exclusion is seven studies, the
    benefit is small (d=+0.43), and it fades after work resumption (d=-0.38). The
    authors additionally report that vacation activities and experiences have
    hardly been studied, so whether what you DO on a break matters is unknown --
    which is precisely the input an assistant would use. Reframed rather than
    dropped: a break is recurring maintenance with a short half-life, not repair.
  - "Moderate drinking is good for your heart" / the J-curve. REFUSED AS THE
    CURRENT STATE OF THE EVIDENCE, and the item shipped in its place reflects
    2019-2023 rather than 2015 (item 009). Zhao 2023, 107 cohort studies,
    4838825 participants, 425564 deaths: after adjusting for former-drinker bias
    and study quality, occasional drinking RR 0.96 (0.86-1.06, p=.41) and
    low-volume drinking RR 0.93 (p=.07) versus lifetime nondrinkers -- neither
    significant -- with risk significantly raised at 45-64 g/day (1.19) and 65+
    g/day (1.35), and female drinkers at 1.22 versus female lifetime nondrinkers.
    THE MECHANISM IS NAMED, because that is what makes the correction stick: the
    "non-drinker" reference group in the classic studies mixed lifetime
    abstainers with people who had stopped, often because they were already ill,
    which raises the reference group's mortality and manufactures a benefit for
    everyone else. Two Mendelian randomisation analyses remove the U-shape
    entirely -- 512715 adults in China (genotype-predicted intake gives a
    log-linear stroke association, RR per 280 g/week 1.58 for intracerebral
    haemorrhage and 1.27 for ischaemic stroke, and no significant myocardial
    infarction effect) and 371463 in UK Biobank (exponential increases inside
    currently permitted guideline amounts). Genotype is fixed at conception and
    cannot be caused by illness or lifestyle, which is why it answers the
    objection cohort data cannot.
  - The industry-funded defence of moderate drinking. NOT SUPPRESSED, CARRIED
    WITH ITS PROVENANCE. A reply defending moderate alcohol's health benefits was
    published in the Journal of Studies on Alcohol and Drugs in 2024, and it is a
    genuine peer-reviewed comment on the 2023 meta-analysis. Its authors'
    published conflict-of-interest statement discloses extensive past funding and
    consultancy from wine, brewing and spirits interests. Both facts are recorded
    together, per exercise/funding-coi-check-004. Recording this is the point:
    suppressing a peer-reviewed objection is how a warehouse becomes propaganda,
    and quoting it without its funding history is how a reader gets misled.
  - "A daily glass protects the ageing brain." REFUSED AS UNESTABLISHED, not as
    false (item 011). Choi and Je 2026, 20 cohorts, N=78657: the answer flips on
    one analytic choice. Among the 9 studies that accounted for baseline
    cognition, 28+ g/day was associated with LOWER cognitive function (SMD -0.08,
    -0.15 to -0.01); among the 11 that did not, the same intake pointed the other
    way and was not significant (SMD 0.13, -0.05 to 0.32), p for interaction
    <0.01. The studies that cannot separate drinking from pre-existing cognition
    are the ones that find the benefit -- the same contamination that produced
    the cardiovascular J-curve, appearing in a second endpoint. No East Asian
    stratum is reported in the regional moderator analysis.
  - A numeric cancer-risk multiplier for flushing drinkers. REFUSED ON SOURCING,
    and the refusal is carried on the item rather than hidden (item 010). The
    claim is probably directionally right and could not be shipped. The
    best-indexed recent pooling (Zhang 2023, 23 publications) reports ALDH2 rs671
    as apparently PROTECTIVE against oesophageal squamous cell carcinoma, OR 0.60
    (0.50-0.73), and its own Mendelian randomisation found no causal effect of
    alcohol on that cancer. Drinker-stratified figures showing sharply elevated
    risk in heterozygous drinkers trace to a pooling published WITHOUT A DOI in a
    low-tier journal, which this warehouse does not cite. The contradiction is
    explicable -- the variant raises harm per drink and cuts drinks per person,
    so unstratified pooling lets the second effect dominate and the gene looks
    like a shield when it is a deterrent -- but explicable is not quantified. The
    magnitude stays unstated until a stratified primary with a resolvable
    citation is read. What IS shipped is the Korean genotype distribution from a
    17707-person Korean sample: 2.51 percent AA, 26.66 percent GA, 70.83 percent
    GG, so roughly 29 percent carry an inactive allele.
  - CARRIED FORWARD, not re-litigated: the deliberate-practice ceiling and the
    10000-hours framing. learning-habits/deliberate-practice-ceiling-005 already
    owns this and it was not re-opened for hobbies. Linked from item 006 rather
    than duplicated, per the same no-double-counting rule applied between item
    007 and mental-health/workload-detachment-recovery-016.
  - NOT rejected, NOT shipped, EXPLICITLY NOT RESEARCHED, listed so the next pass
    knows what this one did not ask: Korean official 절주 guidelines and the local
    standard-drink convention (the domain's biggest gap -- every threshold here is
    in grams of ethanol, which is not how anyone counts); Korean drinking
    prevalence and high-risk-drinking base rates from KNHANES; alcohol and sleep,
    which is the most practically useful drinking question a life agent has and is
    entirely absent; resveratrol and the red-wine-specific literature; ensemble
    and group music-making as distinct from solo practice, which matters because
    the owner's 취미 includes playing in a band; hobby engagement and cognitive
    ageing, deliberately left closed because it is gate 1 of this domain's
    checklist in its purest form; and screen and consumption time, where item 005
    predicts the self-report problem is worse than anywhere else in the domain
    because the respondent must decide what counts before answering. See the
    leisure section above for what would close each.
- Warehouse size at the moment this section was appended (counted from disk by
  apply.sh, not hardcoded at build time -- this warehouse took concurrent writes
  from several agents on 2026-09-02):

  exercise 30
  learning-habits 21
  mental-health 20
  nutrition 20
  work-career 20
  finance-investing 17
  relationships-communication 17
  spending-saving 16
  task-management 16
  skincare-hygiene 15
  home 13
  sleep-recovery 13
  cooking 12
  leisure 12

  = 242 RAG items + 2 E-records across 14 domains.
  skincare-hygiene opens at 15 items and is the 14th domain in the registry. It is the
  owner's own area 16 under 건강 (스킨케어/위생), which held zero items before
  this release. Its 2 lanes split @clinical-derm 11, @cosmetic-regulatory 4.
  Warehouse RAG-item total moves from 227 to 242.
- Rejected-claim ledger, v25 (skincare-hygiene domain opening). This is
  the most commercially captured subject matter in the warehouse: nearly every
  claim in circulation originates with a party selling the thing. The ledger is
  therefore at least as much the output of the sprint as the fifteen items are.
  Each entry is a claim that was researched and NOT shipped as stated, recorded so
  it cannot be quietly re-adopted:
  - COLLAGEN SUPPLEMENTS as an actionable efficacy claim. NOT REFUSED OUTRIGHT
    AND NOT ENDORSED -- shipped as item 009 with contested: yes, and this entry
    records exactly why the middle position is the honest one. The literature is
    not empty: a systematic review and meta-analysis in a dermatology society
    journal, with a resolvable DOI, searched five databases including a
    negative-results database, pooled 19 randomised double-blind controlled trials
    across 1,125 participants (95 percent women), and reported favourable results
    for hydration, elasticity and wrinkles. Pretending that does not exist would
    be caught and would rightly cost trust. But the full text was NOT retrievable
    in this pass, so the funding sources of the 19 pooled trials, their individual
    risk-of-bias ratings and any publication-bias analysis are UNREAD. This
    release makes NO claim about industry sponsorship of those trials, because
    asserting one unread is the same offence as the marketing it guards against.
    No pooled effect magnitude is carried anywhere. The endpoints are the
    instrument and appearance measures most exposed to the placebo floor that item
    008 documents. And the same searches returned, alongside the review, narrative
    reviews and trials named after the branded ingredient under test -- the
    signature of a literature grown out of a market. Generalisable rule: WHEN A
    POSITIVE SYNTHESIS EXISTS BUT ITS FUNDING AND BIAS STRUCTURE COULD NOT BE
    READ, SHIP IT AS CONTESTED WITH THE GAP NAMED AS A GAP. Do not fill the gap
    with a plausible assumption in either direction.
  - THE 10-STEP ROUTINE, and every claim about routine LENGTH or STEP ORDER.
    REJECTED OUTRIGHT. Zero primary sources exist comparing routine lengths or
    layering orders against any endpoint. This is a purely commercial construct
    with no measurement behind it anywhere in the searched literature.
  - CLEANSING AND SHOWERING FREQUENCY. REFUSED AS A NUMBER, SHIPPED AS AN
    ABSENCE. Searches for randomised evidence on face-washing frequency and on
    bathing frequency against skin-barrier outcomes returned no eligible
    primaries. Item 010 exists as the forcing point, on the model of
    relationships-communication/contact-cadence-no-evidence-014: without an
    explicit row, an assistant asked how often to wash will generate a number
    from parametric memory and speak it as knowledge, because the internet
    contains unlimited unsourced text on exactly this. Explicitly NOT a
    demonstrated null.
  - SKIN-MICROBIOME BALANCING as a cosmetic claim. REJECTED. Every located result
    was a branded single-product trial in a cosmetic-dermatology journal, or a
    study of a medical intervention in atopic dermatitis, neither of which
    supports a general microbiome claim for a consumer product.
  - TOPICAL VITAMIN C at consumer concentrations as an anti-aging claim.
    REJECTED. No independent RCT-grade source located. Note the regulatory trap
    that makes this easy to mis-ship: several ascorbyl derivatives DO appear on
    the Korean waived-dossier list at fixed concentrations, but registered for the
    MELANIN claim, and a dossier waiver is not an efficacy finding in any case
    (item 013).
  - "DERMATOLOGIST TESTED" and "DERMATOLOGIST RECOMMENDED" as quality signals.
    REJECTED AS EFFICACY SIGNALS, and replaced with the regulatory fact that IS
    retrievable and is sharper. No regulation read in this pass defines
    "dermatologist tested" or specifies what such a test must consist of -- it is
    an undefined marketing phrase. And the endorsement form is not merely weak in
    Korea, it is PROHIBITED: 화장품법 시행규칙 별표 5 제2호 다목 bars any claim, or
    implication, that a physician, dentist, doctor of Korean medicine, pharmacist,
    medical institution or other medical or pharmaceutical expert designates,
    endorses, recommends, guides, researches, develops or uses the cosmetic, with
    one narrow exception requiring the researcher's name, the publication name and
    the date. Item 014.
  - PEPTIDES, GROWTH FACTORS, EXOSOMES and the aesthetic-active category.
    REJECTED. The located literature is narrative reviews, procedure-paired
    split-face trials and aesthetic-practice writing. No independent synthesis
    with a stated methodology was found.
  - "REAPPLY SUNSCREEN EVERY TWO HOURS." REJECTED AS A FINDING. It is a labelling
    and regulatory convention; no primary measurement of that interval was
    located. Recorded with its inversion, because the one reviewed source that
    does make a reapplication recommendation proposes a DIFFERENT shape -- apply
    before exposure, reapply once within the FIRST HOUR -- and states it as the
    authors' own suggestion rather than as a measured result. Item 002 carries it
    that way and asserts no two-hour figure.
  - "SPF 50 IS BARELY BETTER THAN SPF 30" and its mirror "SPF 50+ IS TWICE THE
    PROTECTION." BOTH REFUSED as label comparisons, on a regulatory rather than a
    biological ground. Under 기능성화장품 심사에 관한 규정 제13조제2항, everything
    measuring 50 or above prints as "SPF50+", and the printed integer may sit
    anywhere from the truncated measured mean down to 20 percent below it. Two
    products showing the same string are not necessarily the same product, and two
    SPF50+ products cannot be ranked by their labels at all. Item 012.
  - THE US REGULATORY COMPARISON, in either direction. REFUSED FOR A RETRIEVAL
    FAILURE, not for a judgement. Direct retrieval of the relevant fda.gov pages
    returned HTTP 404 on repeated attempts, so nothing was quoted from them and no
    US regulatory fact is stated anywhere in this release -- even though the
    Korea-versus-US structural contrast was an explicit target of the sprint. This
    is the v15 cooking jurisdiction rule applied in the opposite direction: a
    KOREAN REGULATORY FACT IS NOT A US REGULATORY FACT EITHER, and a
    jurisdiction's rules are never stated from memory while another's are cited
    from the statute.
  - CARRIED FORWARD AS A DOMAIN-LEVEL RULE, and the reason this ledger is longer
    than the item list is short: A BRAND IS NEVER A SOURCE FOR ITS OWN PRODUCT'S
    EFFICACY, AND BEAUTY MEDIA IS NOT A SOURCE AT ALL. No brand page, no beauty
    publication and no content-farm repost is cited anywhere in v25. Where
    the only trace of a claim ran through those channels, the claim was refused
    rather than substituted with adjacent evidence that belongs to a different
    question.
- Cross-domain note, v25: the hand-hygiene item (006) is deliberately
  scoped to hand hygiene AS A HEALTH BEHAVIOUR and its measured effect on
  diarrhoeal illness. Food handling, kitchen-surface contamination and Korean
  food-safety instruction remain owned by the cooking domain and are LINKED from
  006 rather than restated inside it. This is the v3 section 5 single-ownership
  rule applied across a domain boundary that a naive reading would have
  duplicated: both domains have a legitimate claim on "washing", and the split is
  by what is being prevented, not by the verb.
- Warehouse-level signal, v25: this is now the THIRD consecutive domain
  opening to record the same structural gap from a different direction -- the axes
  ledger is fitness-shaped and does not contain the axes a non-fitness domain
  would refract on. The cooking sprint recorded it for cooking-session axes, the
  nutrition sprint for meal-logging axes, and this one for phototype, daily
  ultraviolet exposure and photosensitising medication. One item in this release
  (007) does make a genuine use of the existing ledger, attaching pregnancy_status
  as a hard SAFETY axis with block_specifics for a retinoid question. That it is
  one item out of fifteen is the finding. Three independent domains reaching the
  same conclusion is a warehouse-level input for whoever owns axes.yaml, not a
  per-domain complaint.


- Size update 2026-09-02 (after v26): exercise 30, learning-habits 21, mental-health 20, nutrition 20, work-career 20, finance-investing 17, relationships-communication 17, spending-saving 16, task-management 16, skincare-hygiene 15, home 13, sleep-recovery 13, cooking 12, leisure 12, travel 10
  = 252 RAG items + 2 E-records across 15 domains. Exercise is now 12%
  of the warehouse. travel opens at 10 items and had a row in NEITHER
  registry.yaml nor lanes.yaml beforehand, so both were appended in the same
  pass. The structurally notable part is the SPLIT: travel ships two lanes
  across two verification cultures -- @travel-clinical (VC-A) and
  @travel-advisory (VC-F) -- which in this warehouse only cooking and
  exercise otherwise do, because grading a statute on a clinical-trial
  ladder is a category error. Note the shape rather than the count: 3 of the
  10 rows are flagged contested, one is a deliberate GATE row that ships no
  numbers at all, and the sprint's refusal ledger is longer than the item
  list. Counts computed at apply time, not asserted.
- Rejected-claim ledger, v26 (travel-lane opening sprint). Travel is the
  densest folklore field this warehouse has opened -- denser than cooking,
  because almost every claim in it is repeated by an industry that benefits from
  it. The sprint's operating rule was that a refusal with a stated reason beats a
  plausible shipment, and this ledger is as much the output of the sprint as the
  ten items are. Each entry was researched and NOT shipped as stated, recorded so
  it cannot be quietly re-adopted:
  - "Recirculated cabin air spreads infection / planes make you sick because of
    the air." REJECTED, and unusually cleanly, because it was tested by a natural
    experiment rather than argued about. In 1999 some aircraft on one route used
    100 percent fresh air and others recirculated about half; passengers did not
    choose. Among 1100 of them: colds 19 vs 21 percent (P = 0.34), runny nose
    with cold 10 vs 11 percent (P = 0.70), an aggregate of 8 upper-respiratory
    symptoms 3 percent in BOTH groups (P greater than 0.99), unchanged after
    adjustment. Item 005 ships the replacement model (proximity) and discloses on
    its face that the proximity paper was part-funded by an aircraft manufacturer
    with a manufacturer employee as co-author -- the refutation deliberately
    rests on the independently funded 2002 study, not on the industry-linked one.
    Scope held: neither source covers airborne transmission or anything after
    2018, so this is NOT a clearance for respiratory risk on aircraft in 2026.
  - "Compression socks prevent DVT on flights." CORRECTED RATHER THAN REJECTED,
    and the correction is entirely about which endpoint. The Cochrane review (12
    RCTs, n=2918) reports HIGH-certainty evidence of a large reduction in
    SYMPTOMLESS DVT: 3 of the stocking group vs 47 of the no-stocking group among
    2637 with follow-up, OR 0.10 (95 percent CI 0.04 to 0.25). But NO deaths, NO
    pulmonary emboli and NO symptomatic DVTs occurred in ANY included trial, so
    the review states it cannot assess those outcomes and that trials powered for
    them would need very large numbers. Both misreadings are refused here: the
    product claim (they prevent clots that matter) is unsupported, AND the
    fashionable debunk (they have been shown not to) is a conversion of absent
    events into a null, which this warehouse does not permit. Item 004. Note the
    arithmetic tie to item 003: at roughly one symptomatic event per 4,656
    long-haul flights, a few thousand passengers should be expected to yield none.
  - "Boil it, cook it, peel it, or forget it." REJECTED AS AN INCIDENCE CLAIM. Of
    8 studies that specifically addressed whether personal hygiene precautions
    prevent travellers' diarrhoea, 7 showed no correlation between the types of
    food selected and risk; the eighth found a few dietary mistakes associated
    with DECREASED risk and further mistakes not raising it, which is a shape
    incompatible with a simple exposure-response story. Structurally corroborated
    by an absence: the 2017 graded expert panel issued 20 graded recommendations
    plus 3 consensus statements and NO graded recommendation on food and water
    precautions, which was checked at full text specifically for this item. The
    INVERSION is refused just as firmly -- water source and hand hygiene were not
    the variable, the review's own explanation is that precautions work where you
    control the kitchen and fail at someone else's restaurant, and nothing here
    licenses telling a user to disregard public-health advice. Item 006.
  - "Drink plenty of water to beat jet lag." REFUSED. A targeted search for any
    primary study measuring a hydration intervention against a jet-lag endpoint
    returned nothing usable. No magnitude was shipped in either direction, and
    this is recorded as an ABSENCE rather than as a demonstrated null -- the same
    handling as the relationships domain's contact-cadence row.
  - The Argonne-style ANTI-JET-LAG DIET (feast/fast cycling before departure).
    REFUSED OUTRIGHT. A search for a randomized or controlled trial of a jet-lag
    diet returned exactly one paper and it was a bright-light study. The
    feeding-as-zeitgeber literature in animals is real and is a different claim;
    do not let a later pass import it as support for the human protocol.
  - "One day per time zone to recover." REFUSED AS SYMMETRIC, which is the part
    that makes it wrong rather than merely rough. The travel review reports
    unaided re-entrainment of about 92 minutes per day of DELAY after westward
    flights against about 57 minutes per day of ADVANCE after eastward flights,
    and the mechanism is not folklore: the human free-running period is slightly
    longer than 24 hours, so advancing the clock is intrinsically harder than
    delaying it. A single symmetric rule cannot describe an asymmetric process.
    Item 002. Same family as the cooking lane's "wrong in two different ways"
    entries -- a correction that only adjusts the number leaves the shape wrong.
  - "Get morning light when you land." REFUSED AS STATED, and this is the
    sprint's most operationally important refusal. The direction of a light-induced
    phase shift depends on when the light falls relative to the CORE BODY
    TEMPERATURE MINIMUM, which sits late in the sleep episode, not on the
    destination's wall clock. Advice that omits the reference point is a coin
    flip. And mistimed light does not do nothing: the travel review names
    antidromic re-entrainment -- the clock shifting the OPPOSITE way to the one
    needed -- and reports it as common after eastward travel, especially across
    8 or more time zones. Item 002 ships the direction rule with its reference
    point attached and ships NO schedule.
  - ASPIRIN OR ANTICOAGULANTS FOR FLIGHT VTE PREVENTION. REFUSED on two
    independent grounds. The only randomized evidence located is a series from a
    single research group in a single journal, which is not a base this warehouse
    builds on. And it is a prescribing question, which is outside this lane's
    stated boundary regardless of evidence quality. Nothing was shipped, in
    either direction, and a later pass meeting a confident recommendation in a
    travel-media source should treat that confidence as unearned.
  - "Visiting a 여행금지 country is 1년 이하의 징역 또는 1천만원 이하의 벌금."
    STALE SINCE 2026-08-28, and this is the sprint's most consequential single
    correction because it is a criminal-liability fact. 법률 제21383호,
    promulgated 2026-02-27 and in force six months later, DELETED 여권법 제26조제3호
    and moved the offence into 제24조 as a new 제2호, whose band is 3년 이하의 징역
    또는 3천만원 이하의 벌금. The legislature's own 제개정이유 states the penalty was
    raised from the former band to the latter. The old figure is in essentially
    every secondary summary and in any model whose training predates the
    amendment. Verified by reading 여권법 directly from 법제처's machine-readable
    record, NOT from an explanatory page -- and note that one ministry page
    checked during this sprint was already correct while a search-engine summary
    of the same question was not, which is a good illustration of where to look.
    Item 008. Same staleness family as finance-investing's Korean tax-regime gate
    and the cooking lane's edition-check catch.
  - ANY US TRAVEL-HEALTH RECOMMENDATION PRESENTED AS KOREAN GUIDANCE. REFUSED
    STRUCTURALLY rather than case by case: both Korean rows in this sprint are
    sourced ONLY to Korean authorities, and no non-Korean source appears in
    either. This is the governing rule the cooking lane adopted earlier the same
    day after a US-only rest-time equivalence was dropped from it, and it bites
    hardest in this domain because English-language travel-health material is
    abundant, well-written and almost entirely American, and it differs from
    Korean guidance on exactly the things a traveller must act on -- which
    facilities may issue an international certificate, what is prescription-gated
    in Korea, and where to actually go.
  - ALTITUDE ASCENT RATES AND RISK CATEGORIES. NOT REJECTED -- the WMS 2024
    guideline is the right authority and its recommendations are presumably fine
    -- but NOT SHIPPED, because the full text would not load (publisher page and
    the society's own summary both 403) and the figures were available only in
    secondary summaries. Nothing was taken from those. Item 010 ships a
    deliberate GATE ROW instead: it names the current edition, records that 2019
    is superseded, notes that the guideline grades on ACCP criteria (a THIRD
    grading ladder in this warehouse, alongside GRADE and the older AASM
    Standard/Guideline/Option scheme), and states in terms that this warehouse
    holds none of its numbers. Rationale for shipping a refusal as a row rather
    than leaving the gap: altitude figures are memorable, precise-sounding, have
    moved across four editions, and are exactly what an answer path will supply
    from parametric memory if nothing stops it. An empty domain invites that; a
    row that says "go and read the 2024 update" is a forcing point.
  - NOT rejected, NOT shipped, explicitly not researched: motion sickness,
    insect-borne disease and repellent evidence, cabin pressure and
    fitness-to-fly for existing conditions, sleep obtained on the aircraft as
    distinct from circadian adjustment, and the 검역감염병 오염지역 designation
    mechanism. Travel insurance was searched and returned nothing addressing the
    risk framings the lane was asked to check, so it is recorded as a LIKELY
    future refusal rather than as one. See the travel section above for what
    would close each.
  - MEDICAL-ADVICE BOUNDARY, held throughout and recorded here so a later pass
    inherits it rather than rediscovering it. This lane carries decision
    structure and what authorities instruct. It carries no prescriptions, no
    dosages and no individualised advice. Melatonin appears only as "the standing
    guideline endorses TIMED administration for jet lag disorder" with no dose,
    no schedule and no product; malaria prophylaxis appears only as
    "prescription-gated, and the Korean authority routes the decision to a
    doctor"; travellers' diarrhoea treatment appears only at the level of which
    severity band calls for which class of response. Three items additionally
    carry an explicit route-to-a-clinician for the cases where the question stops
    being a travel question -- prior thrombosis and clotting risk on item 003,
    circulatory and diabetic contraindications for compression garments on item
    004, and pregnancy, medication and allergy gating on items 007 and 009.
- Size update 2026-09-02 (after v27): exercise 30, learning-habits 21, mental-health 20, nutrition 20, work-career 20, finance-investing 17, relationships-communication 17, spending-saving 16, task-management 16, skincare-hygiene 15, cat 13, home 13, sleep-recovery 13, cooking 12, leisure 12, travel 10
  = 265 RAG items + 2 E-records across 16 domains with items. Exercise is
  now 11% of the warehouse. This release OPENS a domain rather than
  expanding one: `cat` goes 0 -> 13 with three new lanes (@clinical-vet
  VC-A, @companion-ethology VC-C, @vet-regulatory VC-F). Note the shape
  rather than the count. 5 of the 13 rows are flagged contested, the
  domain's FIRST shipped item is its grading rule because the veterinary
  evidence ceiling is lower than the human-medicine lanes next to it, and
  the most certain band in the domain is a jurisdictional legal fact
  rather than a clinical one. The refusal ledger for this sprint is
  longer than the item list. Counts computed at apply time, not asserted.
- Rejected-claim ledger, v27 (cat-domain opening sprint). This domain runs on
  confidently-repeated folklore to a degree the warehouse has not met before --
  the advice corpus is enormous, the research corpus is small, and the two are
  not connected. The sprint's operating rule was the one the
  relationships-communication lane established: refusing a famous claim with a
  stated reason beats shipping it. Every entry below was researched and NOT
  shipped as stated, so it cannot be quietly re-adopted by a later sprint:
  - "Cats are low maintenance / self-sufficient." REFUTED, not merely omitted,
    and it is the domain's largest piece of folklore. The AAFP and ISFM
    environmental needs guidelines (Ellis et al. 2013, J Feline Med Surg
    15(3):219-230, doi 10.1177/1098612X13477537) state that addressing
    environmental needs is essential and NOT optional for the cat's wellbeing,
    and the guidelines exist because unmet needs present as medical and
    behavioural disease. The correction has a specific shape worth keeping: the
    claim is not that cats need more than people think, it is that a cat's needs
    are quieter, and a species whose distress is hard to read gets mistaken for a
    species without any. Item 011.
  - "Cats are aloof / do not form real bonds." REFUSED IN BOTH DIRECTIONS, which
    is the unusual part. Neither of the two studies in this literature supports
    the aloofness claim: Vitale, Behnke and Udell 2019 (Curr Biol 29(18):R864-
    R865, doi 10.1016/j.cub.2019.08.036) report distinct attachment styles, and
    Potter and Mills 2015 (PLoS One 10(9):e0135109, doi
    10.1371/journal.pone.0135109) -- the study usually cited AGAINST cat
    attachment -- found cats vocalising more when the OWNER rather than a
    stranger left, while declining to call the pattern secure attachment. The
    disagreement is about what kind of bond and whether the infant framework
    describes it, not about whether there is one. Citing the 2015 null as
    evidence of indifference inverts it. Item 010.
  - THE SECURELY-ATTACHED PERCENTAGE. REFUSED ON PROVENANCE, and this is the
    sprint's hardest refusal because it is the number this domain would most like
    to have. A specific percentage of cats classified as securely attached
    circulates everywhere the 2019 study is discussed. The Current Biology full
    text was NOT retrievable in this pass -- the publisher returned an access
    error and the open-access mirrors carried only the abstract, which contains
    neither a sample size nor a percentage. The figure may well be correct. It
    was not verified, and a percentage that travels only through retellings is
    not laundered into this warehouse because the conclusion is congenial. Same
    handling as the cigarette-equivalence refusal at relationships-communication/
    social-connection-mortality-magnitude-008. Item 010; recorded as open in the
    cat section above.
  - "A water fountain makes a cat drink more." REJECTED, with two independent
    controlled nulls behind it, which is rare in this domain. Robbins et al. 2019
    (J Feline Med Surg 21(8):682-690, doi 10.1177/1098612X18803753) randomised 16
    healthy cats through still, circulating and free-falling bowls in crossover,
    two weeks each, and reports that average daily water intake, urine volume,
    urine specific gravity and relative supersaturation for struvite and calcium
    oxalate were all not significantly different between bowl types -- while urine
    osmolality was significantly HIGHER on the circulating bowl (P = 0.009), which
    runs against the fountain. Pachel and Neilson 2010 (J Vet Behav 5(3):130-133,
    doi 10.1016/j.jveb.2010.01.001) found the same shape in 9 cats. NOTE THE
    CAREFUL FORM: 16 and 9 animals cannot rule out a small effect, so this is an
    undetected effect and not a demonstrated absence, and BOTH studies
    independently report real individual preference. Item 003.
  - "Cats are lactose intolerant" as a blanket claim about any individual cat.
    REFUSED AS STATED, corrected version shipped. Kienzle 1993 (J Anim Physiol
    Anim Nutr 70:89-96, doi 10.1111/j.1439-0396.1993.tb00310.x) measured lactase
    falling from 96 +/- 66 U/g protein in newborns to 13 +/- 9 at six weeks, with
    maltase, isomaltase and sucrase stable across ages, and -- the useful part --
    diet had NO effect on enzyme activity across carbohydrate-free, starch-rich,
    sucrose-rich and lactose-rich feeding, which is the direct answer to "the cat
    has had milk for years and is fine". TWO THINGS THE STANDARD CORRECTION
    DROPS: the same paper records SOME ADULT CATS with unusually high jejunal
    lactase, so the blanket individual claim is not what was measured; and no
    clinical endpoint was measured at all -- nobody gave a cat milk and recorded
    what happened. The step from low lactase to digestive upset is an inference.
    Item 008.
  - "Fat cats die younger" as the whole story. REFUSED AS FRAMED, and the
    correction reverses the emphasis rather than the direction. Teng et al. 2018
    (J Feline Med Surg 20(12):1110-1118, doi 10.1177/1098612X17752198), 2,609
    cats, hazard ratios against a maximum body condition score of 6: score 3
    HR 4.67 (CI 3.00-7.27), score 4 HR 2.61 (CI 1.95-3.49), score 5 HR 1.43
    (CI 1.15-1.76), score 9 HR 1.80 (CI 1.11-2.93). The thin end carries more
    than DOUBLE the fat-end hazard, and score 5 -- the conventional "ideal" on a
    nine-point scale -- is raised relative to 6. Obesity is not exonerated (score
    9 is clearly raised, and Teng 2024's UK life tables independently flag
    non-ideal weight), but the confident one-sided version is not what the data
    says. Reverse causation is unresolved and plausibly drives the thin end.
    Item 004.
  - "Grain-free food is better for cats." REFUSED OUTRIGHT, and the refusal is an
    absence rather than a contrary finding. A targeted PubMed search for evidence
    of a health benefit from grain-free diets in cats returned ZERO results. This
    is the feline twin of the v13 nutrition-lane rate-of-gain finding: the most
    confidently marketed claim in the area is one nobody has tested. Note also
    that the well-known dilated-cardiomyopathy regulatory investigation concerned
    DOGS, and importing it as a cat finding would be exactly the human-to-feline
    transplant error this domain's checklist flags -- in the wrong species.
    Recorded here rather than shipped, because a refusal with nothing to attach
    it to would be padding.
  - "One litter box per cat plus one" quoted as a research finding. REFUSED AS
    RESEARCH, KEPT AS PRACTICE. The formula appears in a peer-reviewed JFMS
    behaviour review (Halls 2018, 20(11):1005-1014, doi 10.1177/1098612X18806757)
    which attributes its consistently good outcomes to the author's twenty years
    of referral practice; no study is cited for it and none is claimed. The
    AAFP/ISFM house-soiling guidelines (Carney et al. 2014, 16(7):579-598, doi
    10.1177/1098612X14539092) describe their own basis the same way. This is not
    an argument against the advice -- experienced clinicians converging on a
    heuristic is worth something -- but it is a different kind of claim from a
    result. Item 012.
  - A PRESENTING-SIGN CHECKLIST FOR URINARY OBSTRUCTION. REFUSED FOR ABSENCE OF A
    SOURCE, which was the sprint's most tempting shortcut. The list everyone
    knows -- repeated unproductive trips to the box, straining, vocalising --
    appears in every clinic handout and no source read in this sprint stated it
    in quotable form. Attaching three genuine citations to a list assembled from
    memory is the precise failure this warehouse exists to prevent, so the item
    ships the SEVERITY PROFILE (8.5% mortality, 22-24% recurrence, 61.9%
    cardiovascular events) and the routing consequence instead. Item 005.
  - THE SEX RATIO FOR URETHRAL OBSTRUCTION. REFUSED ON A METHODOLOGICAL POINT
    rather than on doubt. It is universally stated that this is overwhelmingly a
    male cat's problem, and the anatomy is not disputed -- but Segev et al. 2011
    (J Feline Med Surg 13(2):101-108, doi 10.1016/j.jfms.2010.10.006) used
    SEX-MATCHED controls, which means the design deliberately removed sex as a
    variable and the paper cannot be cited about it, and nothing else read here
    quantified it. Item 005.
  - A TOXIC AMOUNT AND AN ONSET WINDOW FOR LILY EXPOSURE, and the genus-wide
    version of the rule. REFUSED, three separate refusals on one item. Rumbeiha
    et al. 2004 (J Vet Diagn Invest 16(6):527-541, doi
    10.1177/104063870401600607) demonstrated that only the AQUEOUS extracts of
    Easter lily leaves and flowers were nephrotoxic and pancreotoxic, with acute
    necrosis of the proximal convoluted tubules -- and that finding is a
    RESTRICTION, not a licence to generalise to all Lilium and Hemerocallis. The
    circulating quantities (a petal, pollen groomed off the coat, vase water) and
    the circulating timelines were not in the record read. Same handling the
    cooking lane gave the shellfish-wide version of the oyster rule at
    cooking/kr-norovirus-oyster-010. Item 007.
  - THE KOREAN LEGAL STATUS OF DECLAWING. SEARCHED AND UNRESOLVED, recorded
    rather than guessed. 동물보호법's prohibited-injury article carries exceptions
    for disease prevention and treatment, and nothing located in primary legal
    sources settles whether an elective claw removal falls inside them. It must
    not be stated as banned and must not be stated as permitted. Item 009.
  - WHETHER RABIES VACCINATION IS LEGALLY REQUIRED FOR CATS IN KOREA. ALSO
    SEARCHED AND UNRESOLVED. The 농림축산검역본부 rabies prevention page describes a
    vaccination protocol for cats including annual boosters and states no
    obligation; whether a local ordinance or a 가축전염병예방법 vaccination order
    can bring cats in was not established from the sources read. Recorded inside
    item 013 as well as here, because this is the first question anyone asks
    after registration and getting it wrong in either direction has consequences.
  - "반려동물 등록" AS A SINGLE OBLIGATION COVERING BOTH SPECIES. REJECTED, and this
    is the sprint's most consequential locale finding because the error it
    prevents is a confident false statement rather than a vague one. 등록대상동물
    is defined under 동물보호법 제2조 제8호 and 시행령 제4조 as a DOG aged two months
    or older; cats are outside the class, so there is no registration obligation
    for a cat and no penalty. The fines that circulate -- up to 1,000,000 KRW for
    failure to register, up to 500,000 KRW for late change notification -- attach
    to the dog duty. Cat registration is a VOLUNTARY nationwide pilot (from
    2022-02-01 per the government policy portal) and is microchip-only, where a
    dog owner may choose an external tag. An assistant assuming one duty would
    invent both a deadline and a million-won fine. Item 013, staleness-gated.
  - NOT rejected, NOT shipped, explicitly deferred for a scope decision: WSAVA
    and AAFP vaccination guidance. Stone et al. 2020 (2020 AAHA/AAFP Feline
    Vaccination Guidelines, J Feline Med Surg 22(9):813-830, doi
    10.1177/1098612X20941784) was located and verified as a citable
    professional-body document, and no item was built from it. A vaccination
    schedule sits uncomfortably close to this domain's absolute scope boundary,
    and the Korean jurisdictional overlay could not be established. A later
    sprint has to decide whether "which vaccines are considered core" is a fact
    about evidence (in scope) or a protocol (out of scope). Flagged rather than
    guessed, because guessing the boundary is worse than leaving a hole.
  - NOT rejected, NOT shipped, insufficient design: indoor-versus-outdoor
    lifestyle. Tan, Stellato and Niel 2020 (Animals 10(2):258) was located and
    read as a narrative review of risks and benefits. It is not a primary study
    and does not contain the quantified life-expectancy comparison an agent would
    actually want, and Teng 2024's UK life tables do not break out lifestyle.
    Refused rather than shipped at a low band, because a weak claim here would be
    read as licence for a decision about where an animal lives.
  - NOT rejected, NOT shipped, no controlled outcome to attach: food puzzles and
    feeding structure. Dantas et al. 2016 (J Feline Med Surg 18(9):723-732, doi
    10.1177/1098612X16643753) is a real, citable clinical-practice review rather
    than a controlled trial, and the domain already carries one
    consensus-framework row. Ship it when there is a measured outcome for it.

### spending-saving / @ledger-craft (appended by v28, 2026-09-02)

Appended at end-of-file rather than merged into the `## spending-saving`
section above, because GAPS.md takes concurrent appends from several agents and
an in-place edit could clobber one. A later curator should refile this block
under that section. It belongs to spending-saving, second lane.

WHAT OPENED AND WHY. @ledger-craft (VC-E) is a SECOND lane on the existing
spending-saving domain -- no new domain, no registry change. Before this
release, exercise was the only domain in the warehouse with a craft lane
alongside its evidence lanes, and cooking the only other domain with more than
one lane at all; every remaining domain had exactly one, the evidence lane. The
v18 pass landed 16 evidence items here and zero craft items, while the owner's
live ledger holds 1603 real entries across 11 categories. The evidence lane
carries what is KNOWN about household spending. It cannot carry how to RUN a
ledger -- what to do about a payee string that names only a payment gateway, a
category that has gone quiet, a day with no rows, a duplicate that may be real.
That is the same gap @gym-craft exists to fill for form, setup and what a failed
rep looks like. 11 items shipped (017-027).

THE BASIS IS THE INSTRUMENT, NOT PRACTITIONER CONSENSUS. This lane deliberately
does NOT inherit @gym-craft's method. That lane triangulates independently
published coaching schemes and treats their convergence as weak evidence, which
is legitimate there because strength coaching is adjudicated by a body that
pushes back: a bad loading scheme produces missed lifts and injuries, so a
practice that survived has survived something. A badly kept ledger pushes back
on nobody -- it produces a report that looks exactly like a good one, which is
this lane's founding observation. So convergence of practitioners is refused as
a basis here. What the lane rests on instead, in descending order and stated in
ceiling item 027: a deterministic query-checkable property of the recording
instrument; then a census of one instance ledger, mechanism transferring and
proportions not; then a procedure proposed on top of a measured fact with no
outcome claimed. Nothing ships on "it is generally recommended".

WHAT THE REAL LEDGER CHANGED. Three claims that would have been written from
intuition were falsified by the data and shipped in corrected form.
(a) The catch-all is NOT growing. Its share ranged 4.0 to 13.7 percent of rows
across thirteen months with no trend, so the premise that a catch-all
accumulates was wrong about the first real one examined (item 020). What it
holds instead is 63 income rows, 33 balance-sheet transfers and 28 rows whose
payee names only a payment intermediary -- and approximately zero genuine
miscellaneous consumption.
(b) The near-empty learning category is NOT a behaviour. 15 rows for one
vendor's assistant subscription sit under hobby content while the same
database's own declared-commitment table assigns that subscription to LEARNING,
and a competing vendor's subscription is one of the only two rows that reached
learning at all (item 021). The declared-versus-applied comparison falsifies the
category without asking the user anything.
(c) The v18 diary-attrition diagnostic returns a CLEAN result on this ledger and
is blind anyway. Coverage is 353 of 366 days with no downward trend, and the
ledger still cannot see a single cash purchase, because every row arrived from a
card or bank feed and the instrument vocabulary contains no cash instrument at
all (item 017). A diary loses rows, which coverage statistics detect. A feed
loses whole payment channels, which they cannot.

Rejected-claim ledger, v28 (@ledger-craft opening). This lane's whole
hazard is that a craft door lets refused folklore back in, so this half is the
one that defines the release:

- EVERY CLAIM THE v18 EVIDENCE LANE REFUSED, CHECKED FOR RE-ENTRY IN CRAFT
  CLOTHING AND REFUSED AGAIN. The fixed-ratio budgets restated as an envelope
  DISCIPLINE, the latte factor restated as a small-purchase AWARENESS PRACTICE,
  the emergency-fund month counts restated as a buffer RULE. Same claims, new
  labels, same absence of anything measured underneath. Refused, and made
  structural rather than a one-time decision: ceiling item 027 exclusion (3)
  states the refusal as a standing lane rule so a later sprint has to argue with
  it rather than route around it. This is recorded first because it is the exact
  way this lane would fail -- not by inventing new folklore, but by relabelling
  the folklore next door.

- A RECOMMENDED NUMBER OF SPENDING CATEGORIES. Refused. It is the most obvious
  craft question in the domain and nothing measured was located at any tier. The
  one piece of instance data that looked like it bore on the question -- two
  categories holding 2 rows each, which reads as a scheme that is too fine --
  turned out to be a routing defect rather than evidence about granularity (item
  021), so it does not adjudicate the question in either direction. Not shipped
  at any band.

- A THRESHOLD FOR THE PAYEE-CONCENTRATION CHECK. The diagnostic ships (item 018:
  compute what share of a category is carried by its single largest payee string,
  and whether that string names a merchant or a channel). The THRESHOLD at which
  concentration disqualifies a category total does NOT ship, because no basis for
  any number exists. The check's output is a reason to hedge a figure, not a
  correction to apply to it.

- A RATE FOR HOW MUCH HOUSEHOLD OUTFLOW ESCAPES A PAYMENT FEED. Refused, and
  recorded as a PERMANENT limit rather than a gap instance data can close. A
  feed-derived ledger cannot bound its own blind spot: the rows that would
  measure the missing channels are the rows that are missing. Closing this needs
  an external benchmark, which is exactly the ceiling condition the v18 curator
  checklist sets for the top band. The nearest candidate remains the Korean
  literature comparing household survey consumption against national accounts,
  which the v18 pass could not read at source.

- CASH ESTIMATION FROM WITHDRAWALS. Considered as the obvious workaround to the
  previous entry and refused. The instance ledger contains no cash-withdrawal
  rows at all to work from, and no method for inferring cash spending from
  withdrawal timing was located at any tier. An estimate built that way would be
  a model presented as a record, which is precisely the instrument-mixing failure
  item 023 exists to prevent.

- THE DIRECTION OF RECONSTRUCTION ERROR. Refused and explicitly not asserted in
  item 023. It is very tempting to state that a person reconstructing a missed
  day omits the small purchases. It is plausible, it was not measured, and the
  evidence lane establishes only that self-report error is instrument-dependent
  and non-uniform, not what a reconstructed personal day omits. The refusal makes
  the item's rule stronger rather than weaker: an error of unknown direction
  cannot be corrected for afterwards, so the only available control is knowing
  which rows carry it.

- ROUND AMOUNTS AS A SIGNAL OF AN ESTIMATED FIGURE. RESEARCHED ON THE LEDGER AND
  REFUSED WITH A MEASUREMENT, not on scepticism. 89 percent of the 1540 expense
  rows are multiples of ten and 46 percent are multiples of a hundred, because
  retail prices in this market are usually round. There is no discriminating
  signal in roundness here. Recorded both here and inside item 025, because it is
  the obvious next trigger to reach for after the duplicate check.

- AUTOMATIC DE-DUPLICATION AS A DEFAULT. Refused, and the reason is a
  measurement that inverts the assumption behind the practice. 52 exact
  duplicate groups cover 112 rows, 7.0 percent of the ledger, and 17 of the 52
  are transit-operator rows -- the payee class where two identical same-day
  transactions are entirely ordinary. The detector fires hardest where it is most
  likely to be wrong, and no duplicate group in the ledger exceeds the middle
  amount band, so even a genuinely spurious duplicate changes no figure anyone
  would act on. Shipped as item 025 with the opposite default.

- A REVIEW CADENCE NUMBER. Refused, holding the line the v18 pass already took
  when it recorded that nothing exists at any tier on review frequency. This pass
  did not re-run that search; item 026 records what FOLLOWS from the absence,
  which is more useful than a number would have been: every dominant error
  measured in this ledger is cadence-insensitive, and a shorter window is MORE
  exposed to feed incompleteness at the newest end, not less.

- ANY CLAIM ABOUT WHAT THE OWNER DOES WITH MONEY. Refused as out of lane, and
  recorded because the temptation was concrete: a 1603-row census invites
  observations about the household's habits. Ceiling item 027 exclusion (2)
  routes every claim about people to the evidence lane and its checklist,
  whatever the subject. This lane's subject is the instrument and the operator.
  The census also shows why the temptation is a trap -- items 018, 019 and 024
  each demonstrate that the row counts do not mean what a habit claim would need
  them to mean.

- SCHEMA AND CATEGORY-SCHEME REDESIGN PROPOSALS. Considered and deliberately not
  shipped. Items 020, 022 and 024 each imply an instrument change -- a
  consumption-versus-transfer axis, a usable unknown state, a participant field.
  Those are product decisions and belong on the ticket surface, not in the
  warehouse. The warehouse records what is true about the instrument; it does not
  carry the roadmap. Recorded so a later sprint does not start filing design
  proposals here.

Coverage this lane implies but this pass does not supply:

- A SECOND LEDGER. Everything in this lane is n=1. Every proportion is a
  property of one feed-derived Korean personal ledger with no cash rows and a
  coarse importer. The single highest-value next step is the same census against
  a ledger with a DIFFERENT provenance -- hand-entered, or mixed feed and
  hand-entered -- which is the case items 017 and 023 identify as the one where
  both failure modes operate at once and the coverage statistics are dominated
  by the feed half.

- ANY MEASURED OUTCOME OF ANY PRACTICE IN THIS LANE. Not one item measures an
  effect. Whether marking uncertainty instead of guessing, refusing to
  de-duplicate, or reporting outflow instead of consumption leaves a user better
  informed or better off is unmeasured, and the three contested items say so
  individually. This is the lane's largest structural hole and it is the same
  shape as the evidence lane's: the thing a product most wants to know is the
  thing nobody has measured.

- LONGITUDINAL COVERAGE DECAY, WHICH THE v18 GAP ASKED FOR FROM INSTANCE DATA.
  Not supplied, and the v18 gap should NOT be read as closed. That gap asked how
  a personal ledger's coverage decays over time, noting it might be measurable
  from instance data rather than from literature. It is not measurable from THIS
  instance's data, because the ledger is feed-derived with near-total coverage
  and no attrition to observe -- there is no decay curve in it. Measuring it
  needs a hand-kept ledger over a long window.

- KR-SPECIFIC ANYTHING. Same hole the evidence lane records for itself. The
  instance ledger is Korean, but a census of one Korean ledger is not Korean
  evidence; it is one ledger. Whether Korean feed-derived ledgers systematically
  differ in payee opacity, aggregator concentration or stored-value share is
  unmeasured.

- WHAT AN AGENT SHOULD DO WHEN THE INSTRUMENT CANNOT BE CHANGED. Every item here
  ends up pointing at an instrument fix, and items 022, 023 and 024 assume the
  schema can eventually carry a marker. Nothing in this pass addresses the case
  where it cannot and the agent must operate on a fixed, lossy instrument
  indefinitely. That is the realistic case for any third-party data source.

Size update 2026-09-02 (after v28). Counts computed at apply time from
disk, not asserted:

  exercise 30
  spending-saving 27
  learning-habits 21
  mental-health 20
  nutrition 20
  work-career 20
  finance-investing 17
  relationships-communication 17
  task-management 16
  skincare-hygiene 15
  cat 13
  home 13
  sleep-recovery 13
  cooking 12
  leisure 12
  travel 10

  = 276 RAG items + 2 E-records.
  spending-saving now spans 2 lanes: @household-behavioral 16, @ledger-craft 11
  Multi-lane domains at this release, read from lanes.yaml: cat, cooking, exercise, home, learning-habits, leisure, nutrition, skincare-hygiene, spending-saving, travel, work-career

### relationships-communication / @relational-craft (appended by v29, 2026-09-02)

Appended at end-of-file rather than merged into the `## relationships-communication`
section above, because GAPS.md takes concurrent appends from several agents and
an in-place edit could clobber one. A later curator should refile this block
under that section. It belongs to relationships-communication, second lane.

WHAT OPENED AND WHY. @relational-craft (VC-E) is a SECOND lane on the existing
relationships-communication domain -- no new domain, no registry change. The
v16 evidence lane (17 items) established what predicts relationship
satisfaction and, more usefully, what does not, but none of it tells an agent
holding a live roster of 115 people and 293 recorded relations what to do on a
Tuesday when a name has gone quiet, or how to hand over the domain's one
experimentally supported actionable finding without quietly turning it into a
rota. That is the same gap @gym-craft, @test-kitchen and @ledger-craft each
close for their own domain. 4 items shipped (018-021).

THE BASIS IS PER-ITEM AND STATED, NOT PRACTITIONER CONSENSUS. This lane does
not use blog or coaching convergence anywhere. Item 018 rests on a dated,
CLOSED incident (pack worklog, P0, opened 2026-08-28, closed 2026-09-02) on a
sibling surface of the same product, plus the owner's own corrective directive
issued in response, plus code already running that implements the corrected
rule. Item 019's evidenced content is entirely borrowed from
relationships-communication/reach-out-appreciation-gap-013 and is explicitly
NOT re-graded here; what is native to the item is the delivery, and the
delivery is untested. Item 020's subject is a declared owner preference dated
2026-07-19, which is not the kind of thing that carries evidential confidence.
Item 021 rests on an owner directive (P6, no nagging/no guilt framing) plus
the concrete cap values currently enforced in code.

THE DOOR RULE, stated because a craft lane opened next to an evidence lane
that just refused a cadence and flagged biased self-report is a re-entry door
for exactly that material. Closed by name inside the items themselves:
- Item 020 states in both directions that a declared preference and an
  absence-of-evidence finding (014) do not compete for the same slot. Neither
  may be used to defeat the other outside its own scope -- an agent may not
  call the owner's own tier setting "unsupported" by citing 014, and the
  owner's tier setting may never be spoken outward as advice by citing the
  warehouse behind it.
- Item 021's hard bound: `fade` may be offered ONLY on the owner's own
  declared gap overrun, and NEVER on a reciprocity or tie-asymmetry reading,
  because relationships-communication/tie-reciprocity-perception-gap-012 is
  explicit that no source links tie asymmetry to any outcome. With 293 stored
  relations sitting right there, a reciprocity feature is the most tempting
  thing this surface could grow, and it is the one the evidence forbids
  outright.
- Item 019's trigger rule: what fires a suggestion is the owner's own
  declared tier overrun, never the appreciation-gap finding itself, because
  citing the finding as the reason a surfacing rhythm exists would launder an
  unsourced schedule into a sourced one.

A LIVE MISMATCH SURFACED AND DELIBERATELY NOT RESOLVED. Item 020 found, while
being written, that the module's stored per-tier "recommended meeting cycle"
values (tier 5 = 2.0 months, tier 4 = 4.0, tier 3 = 12.0) imply roughly six,
three and one contacts a year against the owner's declared bands of ten-plus,
four-to-nine and one-to-three. There is a benign reading (the stored field
counts MEETINGS, the declaration counts CONTACTS, and the module already
tracks both with a per-person channel switch) and a defect reading (the
engine drifted from the declaration), and nothing in the store distinguishes
them. The item's own rule is to raise it with the owner as a units question,
never to reconcile it by picking a value -- doing so would mean deciding the
owner's preference on his behalf, which is what item 020 exists to forbid.
This is recorded here as a LIVE, UNRESOLVED item for whoever next touches the
intimacy-tier configuration, not as a defect ticket in its own right.

REFUSED THIS SPRINT (recorded rather than dropped, following the v15/v18/v28
rejected-claim discipline). THE REFUSALS ARE THE POINT OF A CRAFT LANE OPENED
NEXT TO AN EVIDENCE LANE THAT JUST REFUSED THINGS:
- A CONTACT CADENCE OR SCHEDULE OF ANY KIND. The evidence lane already
  refused this outright (item 014) and the refusal stands unchanged. No item
  in this lane ships an interval, a rota, a per-tier schedule, or a count of
  people "owed" a message. Item 021 states explicitly that a backlog must
  never be allowed to accumulate, for the same reason.
- A RECIPROCITY OR "WHO DOES NOT RECIPROCATE" FEATURE. Refused on the
  evidence lane's own item 012 (no source links tie asymmetry to any
  outcome), and named explicitly in item 021 as the sharpest place a
  plausible product feature is forbidden by the evidence rather than merely
  unsupported by it.
- A SLACK NUMBER OR TIME BOUND ON HOW LONG A SUGGESTION IS DELAYED, OFFERED,
  OR HELD. Considered nowhere in this lane. The domain's craft content is
  about WHAT is shown and WHEN a correction may be spoken, never about
  fixed durations.
- RECONCILING THE TIER-VERSUS-CYCLE MISMATCH BY PICKING A NUMBER. Refused by
  item 020's own rule (see above); flagged as a question for the owner
  instead of an editorial decision made on his behalf.
- AN OPENER-STYLE RECOMMENDATION PRESENTED AS RESEARCH. Item 019's
  lead-with-context-not-apology rule is stated explicitly as REASONED DESIGN
  WITH NOTHING BEHIND IT. No study comparing reconnection-opener types was
  located, and none is claimed.
- FRAMING A DECLARED PREFERENCE AS EVIDENCE-BACKED, OR AN EVIDENCE FINDING AS
  A CRITIQUE OF A PREFERENCE. Both directions refused in item 020; this is
  the door rule stated as a pair rather than a single direction.

RESIDUAL SUB-GAPS carried out of this sprint:
1. No relationship-side false-accusation incident is on record; item 018's
   basis is a documented incident on the training surface of the SAME
   product, carried across by structural argument (same predicate error, a
   surface with strictly weaker evidence) rather than by an incident of its
   own. If a relationship-side false accusation ever happens, it belongs on
   this item.
2. No test of opener style (context-first versus apology-first) after a long
   contact gap was located in any source. Item 019 names this as reasoned
   design rather than evidence and it remains open.
3. The tier/cycle mismatch above is unresolved and needs an owner
   conversation, not a warehouse edit, to close.
4. The three cap values in item 021 (2/day, 2-3/week, 60 days) are chosen,
   not measured, exactly like the exercise domain's ramp-up-jump cap and the
   ledger-craft lane's own unmeasured defaults. No comparison against an
   alternative budget was run or is claimed.

Rerun-needed: none. This lane cites no external primary literature to
re-verify -- its sources are a closed incident ticket, a dated owner
directive, code read at source in the live relationship module, and
cross-references to existing warehouse items, all current as of 2026-09-02.

Size update after v29. Counts computed at apply time from disk, not
asserted:

  exercise 30
  spending-saving 27
  learning-habits 21
  relationships-communication 21
  mental-health 20
  nutrition 20
  work-career 20
  finance-investing 17
  task-management 16
  skincare-hygiene 15
  cat 13
  home 13
  sleep-recovery 13
  cooking 12
  leisure 12
  travel 10

  = 280 RAG items + 2 E-records.
  relationships-communication now spans 2 lanes: @dyadic 17, @relational-craft 4
  Multi-lane domains at this release, read from lanes.yaml: cat, cooking, exercise, home, learning-habits, leisure, nutrition, relationships-communication, skincare-hygiene, spending-saving, travel, work-career

### mental-health / @assistant-craft (appended by v30, 2026-09-02)

Appended at end-of-file rather than merged into the `## mental-health` section
above, because GAPS.md takes concurrent appends from several agents and an
in-place edit could clobber one. A later curator should refile this block
under that section. It belongs to mental-health, second lane.

WHY IT WAS OPENED. After the preceding sprint the domain held 20 items and all
20 were @clinical (VC-A) -- what is ESTABLISHED about people. Excellent
evidence and nothing about conduct. The consumer is a generalist life agent
that sees the owner's daily blocks, sleep, energy and workload, and the
question it faces several times a day is not what is established but how to
BEHAVE in the presence of what is established: how to name an observed
pattern without asserting a state, what to do with an absence in a record,
what is in scope at all when the person says they feel bad, what may be kept
and for how long. None of that is in a paper and none of it can be graded
against one. This is the same structural gap the exercise domain closed with
@gym-craft, whose items carry setup, form and what-to-do-when knowledge that
no trial produces and that is what makes the training agent usable. 8 items
shipped (021-028).

THE CEILING, stated first because it governs everything below. The
verification basis of this lane is operational practice inside ONE estate:
unblinded, uncontrolled, n of one, no counterfactual, no measured outcome.
Item 021 is authored as the lane's anchor and states that ceiling as a
convention that does not move. VC-E was chosen to match @gym-craft,
@test-kitchen and @ledger-craft. VC-C was considered and rejected: nothing in
this lane is a finding about people, so filing it under an evidence culture
would imply a study that does not exist.

THE DOOR RULE, and it is the defining constraint on this lane exactly as the
clinical boundary is on the one above. A craft lane opened next to an
evidence lane that has just refused a large body of popular material is a
re-entry door for that material. It is closed, and the four candidates are
named in item 021 so the re-admission cannot happen by drift: gratitude
journalling as evidence-backed (refused on item 017), positive-psychology
effect sizes at their published values (017), willpower or self-control
budgeting as a scheduling input (019), and any inference of how somebody
feels from tracked behavioural data (013). "It is only craft advice" is not a
lower bar for the same claim; it is the same claim with its source removed.
The clinical boundary is inherited unchanged -- no diagnosis, no screening, no
risk assessment, no crisis handling, no treatment selection -- as is item
011's operative rule that no score, threshold or tracked signal may be
converted into a claim about a person's state. Three of the eight items exist
mainly to enforce that rule rather than to add anything to it.

What landed:
- mental-health/craft-verification-ceiling-021 (D/A) -- the anchor, authored
  first and deliberately. The ceiling, the three-condition admission test
  (about the assistant's conduct, falsifiable by an assistant failure, not
  something the evidence lane refused), the door rule, and the inherited
  clinical boundary.
- mental-health/observation-without-diagnosis-022 (D/A) -- the sentence-level
  mechanics of item 013's "ask, never conclude". Four failure shapes that
  each survive a naive self-check -- the smuggled state word, the causal
  arrow, the invented threshold, the concerned register -- each with a
  rewrite. Plus the when-to-say-nothing test: a decision the person can
  actually take must sit downstream, or the sentence is narration of
  surveillance.
- mental-health/absent-record-is-not-an-event-023 (D/C) -- three record
  states rather than two, absence having its own non-random causes, and the
  accusation asymmetry that sets the threshold. Basis is a documented
  incident in this estate on 2026-08-28: an automated routine check reported
  a zero completion rate and four consecutive misses for a series that was in
  fact eight of nine done, and the figure was relayed to the owner three
  times before he rejected it from memory and turned out to be right. Root
  cause established 2026-09-02 (a completion query over a shared store with
  no owner condition); the final step of the arithmetic is still unexplained
  and is recorded as unexplained. The engineering defect has its own ticket.
  What is recorded here is the conduct half, which no code fix removes: a
  number about a person was spoken to that person, in the second person,
  without anyone looking at the rows beneath it.
- mental-health/conversation-is-not-a-sensor-024 (D/A) -- the assistant's own
  channel is a behavioural feature stream, and it is the one the sensing
  literature does not cover, because in that literature the observer is
  outside the exchange and here it is inside. Two reasons this is worse than
  the sensed case rather than better: the inference has no validation at all
  (item 011's reasoning about unvalidated ad hoc ratings, one step further
  down), and the adjustment is invisible, so a wrong read cannot be corrected
  and compounds silently. One carve-out, and its whole content is
  authorship: a standing instruction the person wrote is obedience, not
  inference.
- mental-health/activity-support-without-coercion-025 (D) -- the calendar
  work an assistant actually owns, and the three prohibitions that carry
  equal weight with it. Item 010's hard boundary is restated at the top band
  and none of its standing is borrowed: this is not behavioural activation
  and may never be named as it. The anti-nag rule is carried with its
  mechanism rather than as an owner preference, because the mechanism is what
  makes it a craft rule -- guilt pressure fails by destroying the channel it
  operates through, leaving an assistant the person no longer looks at.
- mental-health/detachment-is-a-schedule-property-026 (D/B/D) -- the
  decomposition that makes this the one workable topic in the domain:
  detachment as studied is a psychological state and is off limits, but
  whether an interval contains no work object is a property of a calendar
  and asserts nothing about anyone. Adds two things practice produced and no
  paper contains -- an empty slot is not an off-interval (an unowned gap is
  reclaimed by a working week, so the act that does anything is giving the
  interval an owner), and the assistant is itself a work object, so its own
  delivery schedule is part of the quantity it is measuring and the only
  part it can change unilaterally.
- mental-health/scope-when-the-owner-reports-feeling-bad-027 (D/A) -- mostly
  a list of what is NOT in scope, authored that way deliberately because the
  refusals are the content. The first rule is the mirror image of item 011:
  that item refuses to let a rating become a claim about a state, and this
  one refuses the same conversion run forwards -- a person's own account of
  how they are must not be turned into a score, a metric or a trend, which is
  what a system with a database does by reflex. Referral carve-out worded
  narrowly: a factual lookup somebody asked for is a lookup, an unrequested
  routing decision is an assessment, and item 020's measurement of rising
  stigma and falling service use is why the latter is not a harmless default
  in this locale.
- mental-health/long-run-observation-without-surveillance-028 (D/B) -- the
  retention rules, which outlive every conversation and are therefore the
  part nobody reviews. The strongest is the second: surface on a cadence the
  person set, never on a threshold the assistant chose, because a
  threshold-triggered surfacing is a state claim delivered by TIMING and no
  amount of careful wording undoes it -- something appearing precisely when a
  number got bad says what the number means. Item 012 supplies why length is
  not strength: within-person variance runs two to four times the
  between-person variance, so a long private record is epistemically weaker
  than it feels, not stronger.

STRUCTURAL FINDING TO CARRY FORWARD. Three of the eight items converge on the
same failure without being designed to: item 022's invented threshold, item
023's absence-read-as-event, and item 028's threshold-triggered surfacing are
all the same move -- a machine picking a number, applying it to a person, and
delivering the resulting claim through a channel the wording rules do not
cover. A future craft item in this domain should ask FIRST what number is
being applied to the person and who chose it, before it asks how the sentence
is worded.

Rejected-claim ledger, v30 (mental-health craft lane opening). This
lane's whole hazard is that a craft door lets refused folklore back in, so
this half is the one that defines the release:
- REFUSED AT THE DOOR, all four named in item 021 as well as here so neither
  location alone can be missed, and all remain refused at full strength:
  (a) GRATITUDE JOURNALLING as evidence-backed, and any agent-initiated
      gratitude or journalling prompt. Refused on item 017 (Cregg and
      Cheavens 2021: g -0.51 against waitlist but -0.18 against an active
      control, the authors' own parsimonious explanation being placebo). The
      re-admission argument met and rejected here was that OFFERING it is
      not a claim, merely a helpful thing an assistant could do. Dropping the
      citation from a claim does not soften the claim; it makes it
      unsourced. Direction of the refusal, stated precisely as item 017 also
      did: nothing says the practice is harmful, and a person who asks for
      it is not refused. What is refused is the assistant initiating it and
      any framing of it as beneficial.
  (b) POSITIVE-PSYCHOLOGY EFFECT SIZES at their published values. Refused on
      item 017. A craft item may not quote a number the evidence lane found
      collapses under correction for small-sample bias.
  (c) WILLPOWER OR SELF-CONTROL BUDGETING as a scheduling input -- "do the
      hard thing while there is still some left", "you have spent your
      discipline", any day plan ordered by a depletable reserve. Refused on
      item 019 (Hagger 2016, 23 laboratories, N=2141, d=0.04 with a CI
      encompassing zero; Vohs 2021, 36 laboratories, N=3531). Item 025 states
      the prohibition operationally: if an ordering has a reason, the reason
      must be a real constraint -- a deadline, a booking, another person's
      time -- never an inferred internal quantity.
  (d) MOOD INFERENCE FROM TRACKED BEHAVIOURAL DATA. Refused on item 013,
      whose own reviewers cap their field at hypothesis generation. Item 024
      extends the refusal to the stream that literature does not cover,
      because there the observer sits outside the exchange: the assistant's
      OWN conversational channel.
- EXCLUDED ON THE CLINICAL BOUNDARY, inherited unchanged from the @clinical
  lane and reconsidered at the craft level before being refused again:
  (e) CRISIS HANDLING AND RISK-ESCALATION CONDUCT. The craft-level argument
      for admitting it was that "what should an agent do when it sees X" is
      a conduct question rather than a clinical one. Refused: every version
      of it requires a risk assessment to fire, and risk assessment is the
      excluded act. Item 027 states the exclusion inside the item that would
      otherwise be its natural home, so the silence reads as a decision
      rather than as a hole an assistant may fill by reasoning from the
      surrounding items.
  (f) SUPPORTIVE-COMMUNICATION TECHNIQUE -- reflective listening, validation
      moves, the counselling micro-skill repertoire. REFUSED as treatment
      content in conversational costume. It also fails the lane's own second
      admission condition: checking whether it works would require measuring
      a human outcome, which makes it an evidence claim, and that evidence
      is not in this warehouse.
  (g) EARLY BURNOUT DETECTION, in any form. REFUSED twice over, either
      reason sufficient. Item 015 records at least 142 incompatible
      definitions and a prevalence range of 0% to 80.5%, so there is no
      coherent thing to detect; and detecting a state in a person is risk
      assessment.
  (h) MOOD CHECK-IN AND DAILY AFFECT LOGGING DESIGN. REFUSED, and note that
      this converts a previously recorded research gap into a live blocker:
      this domain already records that no meta-analytic anchor was located
      on whether repeatedly asking someone to rate their mood changes the
      mood being rated. Designing a check-in means building the instrument
      item 011 refuses to let anyone interpret, on top of a reactivity
      question nobody has answered.
- "AN ASSISTANT CAN TELL WHEN SOMETHING IS OFF, SO IT SHOULD SAY SO." REFUSED
  as stated, and this is the claim the whole lane is arranged against. Three
  separate items were needed to hold it, which is itself the finding: item
  022 refuses the four sentence shapes that assert a state while appearing
  not to, item 024 refuses the inference drawn from the assistant's own
  channel, and item 028 refuses the surfacing rule that makes the claim
  through TIMING while the words stay clean. What survives is item 013's rule
  unchanged -- observed data may be used to ask, never to conclude -- plus
  the mechanics of complying with it.
- "A SELF-CHOSEN THRESHOLD IS NOT A CLINICAL CUT-OFF, SO ITEM 011 DOES NOT
  APPLY." REFUSED, and recorded because it is the most plausible-sounding way
  this lane could have gone wrong. A rule that fires when a count crosses a
  number is a cut-off applied to a person, and the fact that the assistant
  picked the number rather than a validation study does not exempt it -- on
  item 011's own reasoning it makes the position worse, because a validated
  instrument at least has a measured error rate while a self-authored line
  has none. This is a NEW ledger category for this warehouse: a refusal of
  an EXEMPTION ARGUMENT rather than of a factual claim.
- STORING A SENTIMENT OR TONE SCORE OVER THE OWNER'S MESSAGES. REFUSED, and
  item 024 carries the prohibition as its own content rather than as a
  caveat. The decisive argument is not accuracy but invisibility: every
  other inference in this domain arrives as a sentence the person can
  dispute, while a behaviour adjustment made on an inferred mood is never
  disclosed, so a wrong read cannot be corrected and compounds silently.
- BEHAVIOUR-CHANGE-TECHNIQUE TAXONOMIES AND NUDGE DESIGN. NOT SHIPPED, and
  the reason is worth recording as a mechanical one rather than a judgement:
  the readily available material for this lives in practitioner blogs and
  consultancy write-ups, and learning-habits already records the weak base
  of the underlying habit literature (item 004). A craft item assembled from
  secondary sources would be folklore wearing a lane label. Left open.
- NO EXTERNAL CRAFT LITERATURE FOR ASSISTANT CONDUCT IN THIS AREA was
  located, and none is claimed. This is the lane's structural weakness stated
  plainly: @gym-craft could triangulate a heuristic across three
  independently published loading schemes that happened to converge, and
  this lane had no published practice to converge on. Highest-value fetch
  for a next sprint: any professional body's guidance on what
  NON-CLINICIANS may say, or any published design standard for non-clinical
  digital-wellbeing conduct. Same handling as the "searched and not closed"
  entries elsewhere in this file -- an absence in the literature, not a
  finding against the rules.
- AND THE HONEST LIMIT ON THE WHOLE LANE: no outcome is measured anywhere in
  it. Nothing here has been compared against an alternative wording, an
  alternative threshold or an alternative retention policy, and no claim is
  made that following these rules improves anything for anybody. A later
  curator should not read a growing item count in this lane as growing
  confidence. The ceiling is item 021's and it does not move.

RESIDUAL SUB-GAPS carried out of this sprint:
1. CRISIS HANDLING AND RISK ESCALATION CONDUCT remains out-of-scope-by-design,
   inherited unchanged from @clinical.
2. SUPPORTIVE-COMMUNICATION TECHNIQUE remains refused as treatment content in
   conversational costume.
3. MOOD CHECK-IN / DAILY AFFECT LOGGING DESIGN remains blocked on the
   unanswered reactivity question this domain already recorded.
4. EARLY BURNOUT DETECTION remains refused twice over (definitional chaos
   plus the risk-assessment exclusion).
5. BEHAVIOUR-CHANGE-TECHNIQUE TAXONOMIES AND NUDGE DESIGN remain unresearched;
   the most obvious candidate for a next sprint IF a primary base can be
   found.
6. NO EXTERNAL CRAFT LITERATURE FOR ASSISTANT CONDUCT was located; the single
   highest-value fetch for this lane if it exists at all.
7. NO MEASUREMENT OF WHETHER ANY OF THESE RULES IMPROVES ANYTHING. The lane
   cannot fix this by adding items.
8. COORDINATION NOTE: the measurement side of item 023's subject -- how far
   a self-maintained record diverges from the behaviour it claims to
   describe -- has a genuine primary literature and is being staged for a
   different domain (task-management) in a separate package that may or may
   not land. Item 023 deliberately covers only the SPEECH side and cites no
   item outside this warehouse. If that package lands, the two are
   complements and neither needs rewriting.

Rerun-needed: not applicable in the sense the @clinical sections use it. This
lane cites no external primary sources to re-verify. Its within-warehouse
cross-references were checked against the live items on 2026-09-02, and its one
`incident:` source is a documented event in this estate with its root-cause
ticket held separately.

Size update after v30. Counts computed at apply time from disk, not
asserted:

  exercise 30
  mental-health 28
  spending-saving 27
  learning-habits 21
  relationships-communication 21
  nutrition 20
  work-career 20
  finance-investing 17
  task-management 16
  skincare-hygiene 15
  cat 13
  home 13
  sleep-recovery 13
  cooking 12
  leisure 12
  travel 10

  = 288 RAG items + 2 E-records.
  mental-health now spans 2 lanes: @clinical 20, @assistant-craft 8
  Multi-lane domains at this release, read from lanes.yaml: cat, cooking, exercise, home, learning-habits, leisure, mental-health, nutrition, relationships-communication, skincare-hygiene, spending-saving, travel, work-career

### cooking / cooking-session craft sprint (appended by v31, 2026-09-02)

Appended at end-of-file rather than merged into the `## cooking` section
above, because GAPS.md takes concurrent appends from several agents and an
in-place edit could clobber one. A later curator should refile this block
under that section. It belongs to cooking, both existing lanes -- no new lane
opened.

WHAT LANDED AND WHY. Five items (014-018) for a live cooking-session module
that back-calculates a timeline from a target serving time. Item 014 is
@food-safety (VC-F, KR); items 015-018 are @test-kitchen (VC-E, universal).
No new lane: this sprint uses the two lanes item 001 and item 002 already
established, and item 014 is filed first so every craft item that follows
defers to its fence by ID.

THE FENCE (014). Korea's Ministry of Food and Drug Safety publishes the
holding rule that governs a session's every waiting dish: hot food at or
above 60C is free to hold, cold food at or below 5C is free to hold, anything
in between is on a two-hour clock rather than earning schedule slack. The
Clostridium perfringens mechanism -- 43-47C growth optimum, a heat-resistant
spore that lets it grow again in food that has already been boiled -- is why
the DESCENT through the danger zone is the hazard, not the cooking. This
page's bulk-cooking temperatures (75C meat, 85C fish/shellfish) are a
DIFFERENT SCOPE from the household table already shipped as item 005, not a
correction to it, and the two must never be averaged.

THE CRAFT CONTENT (015-018). 015 gives the pinned/unpinned x
slow-decay/fast-decay test for whether a dish tolerates delay, and states as
its central point that pinning is a fact about the POT and never licenses
treating a dish as safely holdable below item 014's 60C floor. 016 grounds
the timeline builder's hard invariant -- never shorten a stated cooking
time -- in the definitional properties of a backward-pass schedule (float is
an output, never a chosen quantity; negative float is a proof of
infeasibility, not a tight schedule), and shows the invariant is a SAFETY
rule in this domain because Korean guidance specifies time AT a temperature.
017 proves without measurement that an ordering-only timeline is a LOWER
BOUND once equipment and attention capacity are considered, enumerates the
recurring hard barriers, and ships no barrier durations because none were
measured. 018 separates the arithmetic case for buffer (needs no evidence)
from the popularly over-applied planning-fallacy case, and shows via the
primary 2012 review that the famous 1994 finding is a COMPLETION-TIME result
being misapplied to cooking's PERFORMANCE-TIME durations.

OPEN -- searched or considered this sprint and deliberately refused rather
than shipped:
- A SLACK DURATION NUMBER for the tolerant (유지형) class. Item 015 gives the
  shape of the limit, not its size, because nothing measured how long a
  pinned, slow-decaying dish actually tolerates before texture loss becomes
  unacceptable. What would close it: a controlled holding-time-versus-texture
  study on a representative pinned dish.
- BARRIER DURATIONS (preheat time, come-to-boil time) for any specific
  appliance or quantity. Item 017 refuses to publish a generic figure because
  none was measured and a generic number would be exactly the
  precise-sounding-but-groundless figure this lane refuses elsewhere. What
  would close it: measuring once per kitchen and storing the result, which is
  cheap and gives a real answer.
- WHETHER A BACK-CALCULATED TIMELINE PRODUCES BETTER MEALS, OR IS USED AT
  ALL BY REAL COOKS. Not researched and not claimed. Item 016 states plainly
  that its claims are conditional (IF a timeline is computed this way, THEN
  these properties follow), not comparative.
- A GENERIC PADDING FACTOR FOR COOKING TIMES. REFUSED, and this is the
  headline refusal of the sprint. The planning-fallacy literature is real and
  was read in the primary (Buehler 1994) and the review (Halkjelsvik and
  Jorgensen 2012), and the review's own distinction between performance-time
  and completion-time predictions is the reason a blanket multiplier on a
  user's stated cooking time is not supported by it. Item 018 also records
  that in the one study read here, asking for a PESSIMISTIC estimate did not
  fix the bias either, so a module cannot buy safety with a second question.
- KOREAN-DISH-SPECIFIC BARRIER OR HOLDING DATA. None of the five items
  measures a barrier or a holding tolerance in a specific Korean dish (국,
  찌개, 볶음밥). Item 014 is a Korean AUTHORITY statement about boiled food in
  general, which is a real step up from the mechanistic inference item 007
  already carries, but it is still not a measurement taken in a specific pot.
  This remains, as recorded under item 007's own gap, the single most
  valuable thing a future sprint could close.
- APPLICABILITY.AXES on any of the five items. Same structural gap the v15
  cooking sprint recorded from a different angle: the axes ledger is
  fitness-shaped, and a cooking-session module's real axes (allergen
  exposure in the dish, who is at the table, appliance capability, whether a
  thermometer is even available) do not exist in it. Deliberately not
  attempted in a content-only release; flagged again for whoever owns the
  cooking-session module design.

RESIDUAL SUB-GAPS carried out of this sprint:
1. No controlled measurement of holding tolerance by dish class exists in
   this warehouse; item 015's classification remains a mechanism-derived
   judgement without a duration attached.
2. No per-appliance barrier-duration dataset exists; item 017's barrier list
   is a category argument, not a measured inventory, and a session that
   meets an unlisted barrier should treat the list as incomplete.
3. The 1994 Buehler primary is 37 Canadian undergraduates on one task type in
   one year (33 retained in analysis), and the 2012 review was read at
   abstract only, not full text; item 018 states both limits openly and
   claims nothing beyond what each source actually supports.
4. Item 014's bulk-cooking temperatures and item 006's Food Code bands carry
   the same edition-check debt the v15 section already recorded: read from
   the ministry's own presentation of its guidance rather than certified
   against the 2026-current legal text.

Rerun-needed: none. Item 014 was retrieved directly from the Ministry of Food
and Drug Safety's own government policy portal (korea.kr) on 2026-09-02.
Items 016 and 017 cite an open, CC-licensed project-management textbook as a
definitional source, not an empirical one. Item 018's two sources were read
directly -- the 1994 study in full, the 2012 review at abstract only, with
that limit stated on the item rather than smoothed over.

Size update after v31. Counts computed at apply time from disk, not
asserted:

  exercise 30
  mental-health 28
  spending-saving 27
  learning-habits 21
  relationships-communication 21
  nutrition 20
  work-career 20
  cooking 17
  finance-investing 17
  task-management 16
  skincare-hygiene 15
  cat 13
  home 13
  sleep-recovery 13
  leisure 12
  travel 10

  = 293 RAG items + 2 E-records.
