---
# Collection sprint 2026-09-02, cat-domain opening. The domain's largest-sample
# claim, and the one whose result most sharply contradicts the framing an agent
# would arrive with. Everyone expects "overweight cat, shorter life". The primary
# study's own numbers put the biggest hazard at the THIN end by a wide margin,
# and put the lowest hazard at a score most charts label above ideal. Shipped
# because it is the domain's best-powered evidence AND because getting this one
# backwards would produce actively harmful household advice about a live animal.
# Rubric: cat @clinical-vet (VC-A, borrowed anchor -- read one band down).
# Source re-audit 2026-10-06: Teng 2018 abstract also reports an age-banded
# lifespan analysis (max BCS 4/5 reached at age 1-3; 3/9 at age 3-11) that the
# item omitted; added to the reverse-causation note, which now says the max-BCS
# exposure blunts but does not remove that confound. Abstract CI '11.5-1.76' is a
# typo for 1.15. Teng 2024 figures re-read, unchanged. Grades unchanged.
id: cat/body-condition-lifespan-004
domain: cat
grade: B (that body condition at both extremes is associated with shorter survival in large veterinary datasets); C (the direction and relative ordering of the individual score bands); D (any causal reading, and any target score for a specific household cat)
lane: "@clinical-vet"
locale: universal
as_of: 2018-2024
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/29393723/"  # Teng KT, McGreevy PD, Toribio JLML, Raubenheimer D, Kendall K, Dhand NK. 2018, J Feline Med Surg 20(12):1110-1118, doi 10.1177/1098612X17752198 -- 2,609 cats from 4,020 screened, one cat-dominant primary practice in metropolitan Sydney; median max BCS 6 (IQR 5-7), median lifespan 15.8 years (IQR 13.5-17.6)
  - "https://pubmed.ncbi.nlm.nih.gov/38714312/"  # Teng KT, Brodbelt DC, Church DB, O'Neill DG. 2024, J Feline Med Surg 26(5), doi 10.1177/1098612X241234556 -- UK VetCompass life tables, 7,936 confirmed deaths; life expectancy at age 0 of 11.74 years (95 pct CI 11.61-11.87)
  - "cat/curator-checklist-001"  # domain rule: a large observational veterinary dataset supports direction, and reverse causation is the standing confound
refraction_notes:
  - note: >
      THE NUMBERS, because the shape of them is the finding. Teng 2018 analysed
      2,609 cats from a single cat-dominant primary practice in Sydney, using each
      cat's MAXIMUM nine-point body condition score as the exposure. Median
      maximum score was 6 with an interquartile range of 5 to 7, and median
      lifespan was 15.8 years. Taking score 6 as the reference, the hazard of
      death was raised at score 3 (HR 4.67, 95 percent CI 3.00-7.27), at score 4
      (HR 2.61, CI 1.95-3.49), at score 5 (HR 1.43, CI 1.15-1.76) and at score 9
      (HR 1.80, CI 1.11-2.93). The largest hazard in the whole analysis is at the
      THIN end and it is more than twice the hazard at the fattest score.
    grade: C
  - note: >
      SCORE 5 IS THE ONE THAT BREAKS THE EXPECTED STORY. On a nine-point scale,
      5 is conventionally the ideal. In this dataset a maximum score of 5 carried
      a raised hazard relative to 6, with a confidence interval excluding 1. An
      agent that has internalised "5 out of 9 is the target" will read that as an
      error. It is not an error; it is what maximum-BCS-as-exposure produces in a
      clinic population, and the most likely explanation is the one the design
      cannot exclude -- see the reverse-causation note below.
    grade: C
  - note: >
      REVERSE CAUSATION IS THE STANDING CONFOUND AND IT PLAUSIBLY DRIVES THE THIN
      END. Cats lose condition because they are ill: kidney disease,
      hyperthyroidism and neoplasia all take weight off before they take life.
      Using the MAXIMUM score a cat ever recorded blunts this -- a peak tends to
      predate terminal weight loss -- but a cat whose disease began before it ever
      reached a higher score is still counted thin, so the design cannot fully
      separate "thin therefore dies" from "dying therefore thin". The abstract's
      age-banded lifespan analysis points the same way without settling it: a
      maximum of 4 (HR 4.15, CI 1.26-13.67) or 5 (HR 1.75, CI 1.07-2.85) reached
      between ages 1 and 3, and of 3 (HR 6.09, CI 1.47-25.25) or 9 (HR 2.27, CI
      1.27-4.04) reached between 3 and 11, went with shorter lifespans. Thinness
      in young adults is harder to blame on the old-cat diseases above, which
      makes reverse causation a less complete explanation; the intervals are
      wide and condition before disease onset was still not measured. This does
      NOT make the association fake. It makes "feed the cat up to score
      6" an unsupported inference from data that only supports "cats whose
      recorded condition was low died sooner, for reasons this design cannot
      separate". The same handling this warehouse gives the social-connection
      mortality literature at relationships-communication/
      social-connection-mortality-magnitude-008.
    grade: D
  - note: >
      THE SECOND SOURCE IS LARGER, INDEPENDENT AND MUCH BLUNTER. Teng 2024 built
      UK life tables from 7,936 confirmed feline deaths in primary-care records
      and reports overall life expectancy at age 0 of 11.74 years (CI
      11.61-11.87), 12.51 years for females against 11.18 for males, 14.42 for
      Burmese and 14.39 for Birman at the top and 6.68 years for Sphynx at the
      bottom. On body condition it says only that being entire, purebred, and of
      NON-IDEAL BODY WEIGHT were significantly linked to decreased lifespan. That
      is a both-ends statement without a per-band breakdown, so it corroborates
      the shape and adds nothing to the ordering.
    grade: B
  - note: >
      NOTE THE LIFESPAN GAP BETWEEN THE TWO SOURCES, which is a sampling artefact
      and not a finding. The Sydney clinic population had a median lifespan of
      15.8 years; the UK life tables put life expectancy at birth at 11.74 years.
      Those are different quantities measured on different populations by
      different methods -- a median among cats with clinic records that reached
      an endpoint, versus a life table over all recorded deaths including early
      ones. Neither number is "how long a cat lives", and quoting either as such
      is a mistake.
    grade: C
  - note: >
      CONTESTED, and specifically on the direction the popular version gets
      backwards. The circulating claim is that feline obesity shortens life. What
      the best-powered per-band analysis available shows is a raised hazard at
      BOTH extremes with the larger hazard at the thin end, and a nadir at a score
      most owner-facing charts describe as above ideal. Obesity is not being
      exonerated here -- score 9 carried a clearly raised hazard, and the UK life
      tables independently flag non-ideal weight -- but the confident one-sided
      story is not what these data say.
    grade: C
  - note: >
      NOT ESTABLISHED BY EITHER SOURCE: a target score for any individual cat.
      Teng 2018 is one clinic in one city with one scoring practice, and body
      condition scoring is itself an observer-dependent measurement whose
      inter-rater reliability was not assessed in either study. An agent must not
      convert "the nadir in this dataset was 6" into "your cat should be a 6".
      Body condition targets for a specific animal are a veterinary judgement and
      sit outside this warehouse's scope.
    grade: D
claim: >
  Body condition at BOTH extremes is associated with shorter survival in cats,
  and the larger hazard sits at the thin end -- which is the opposite emphasis to
  the popular version. Teng et al. (2018, JFMS) analysed 2,609 cats from a
  cat-dominant Sydney primary practice using maximum nine-point body condition
  score as the exposure. Median maximum score was 6 (IQR 5-7) and median lifespan
  15.8 years (IQR 13.5-17.6). Against score 6 as reference, death hazard was
  raised at score 3 (HR 4.67, CI 3.00-7.27), score 4 (HR 2.61, CI 1.95-3.49),
  score 5 (HR 1.43, CI 1.15-1.76) and score 9 (HR 1.80, CI 1.11-2.93). The
  thin-end hazard is more than double the fat-end hazard, and score 5 -- the
  conventional "ideal" -- carried a raised hazard relative to 6. Teng et al.
  (2024, JFMS) built UK life tables from 7,936 deaths, reporting life expectancy
  at age 0 of 11.74 years (CI 11.61-11.87), 12.51 for females against 11.18 for
  males, and 6.68 for Sphynx against 14.42 for Burmese; on condition it states
  only that being entire, purebred and of non-ideal body weight were linked to
  decreased lifespan. Reverse causation is unresolved and plausibly drives the
  thin end: cats lose condition because of illness. NOT established: any causal
  reading, and any target score for an individual cat, which is a veterinary
  judgement outside this warehouse's scope.
reasoning: >
  This item earns the domain's highest confidence band for its direction and
  still needs three separate hedges, which is a fair picture of how good feline
  evidence gets. The direction -- condition at both extremes tracks shorter
  survival -- rests on two independent datasets, one of 2,609 cats with per-band
  hazard ratios and one of 7,936 deaths with a blunt both-ends statement, and
  that is about as strong as a non-randomisable exposure in this species can get.
  It ships primarily because the emphasis everyone carries is wrong in a specific
  and correctable way. The circulating story is that fat cats die younger. The
  per-band numbers put the biggest hazard at the thin end by more than a factor
  of two, and put the nadir at a score that owner-facing charts routinely call
  above ideal. Shipping the popular version would leave an agent nudging a
  household in a direction the data does not support, about a living animal. The
  three hedges are all load-bearing. Reverse causation is not a technicality
  here: weight loss precedes death in the commonest feline diseases, and a design
  using maximum recorded score cannot separate cause from consequence, which is
  why the causal reading is graded at the floor. The two headline lifespan
  numbers -- 15.8 years and 11.74 years -- are different quantities on different
  populations and neither answers "how long does a cat live", so the item says so
  rather than letting one of them travel. And a target score for a specific
  animal is refused outright, not because the data is weak but because it is a
  clinical judgement and the domain's boundary rule puts it out of scope. Marked
  contested on the direction-of-emphasis dispute rather than on any disagreement
  between the sources, which agree.
---

# cat/body-condition-lifespan-004

Everyone knows that a fat cat lives less long. The best-powered analysis of this
question says something more complicated, and the part it gets loudest about is
the other end.

A study of just over twenty-six hundred cats from a cat-focused primary practice
took each cat's highest recorded nine-point body condition score and measured
survival against it. Median lifespan in that population was around fifteen and a
half years. Taking a score of six as the reference point, the hazard of death was
raised at three, at four, at five, and at nine.

Read that list again. The largest hazard in the whole analysis is at score three
-- the thin end -- and it is more than twice the hazard at score nine. And score
five, which is what most nine-point charts label as ideal, carried a raised
hazard relative to six.

That last part is going to look like a mistake to anyone who has absorbed the
usual advice. It is not a mistake, but it probably is not what it looks like
either. The most likely explanation is one the study design cannot rule out:
cats lose condition because they are getting sick. Kidney disease, thyroid
disease and cancer all take weight off a cat before they take its life. A design
that measures the highest condition score a cat ever reached and then watches for
death cannot separate "thin, therefore died" from "dying, therefore thin." Taking each
cat's highest score softens that problem without removing it, and the study's
own breakdown by age -- thinness in cats aged one to three also went with
shorter lives -- makes illness a less complete explanation without ruling it
out. So the association is real and the causal reading is not available. Feeding a cat up to
a target number is not what this evidence supports.

A second and larger dataset -- life tables built from nearly eight thousand
recorded deaths in UK primary care -- corroborates the shape without adding
detail. It reports that non-ideal body weight was linked to a shorter lifespan,
along with being unneutered and being purebred. Both ends, no breakdown.

One thing worth separating out because it invites confusion. The Sydney study
reports a median lifespan around fifteen and a half years; the UK life tables put
life expectancy at birth at just under twelve. Those are different quantities,
measured on different populations, by different methods. Neither of them is the
answer to "how long does a cat live," and quoting either as if it were is an
error.

None of this yields a target for a particular cat. Body condition scoring is an
observer-dependent judgement whose reliability neither study assessed, the
per-band result comes from one clinic in one city, and what condition a specific
animal should be in is a veterinary decision. That sits outside what this
warehouse will say.
