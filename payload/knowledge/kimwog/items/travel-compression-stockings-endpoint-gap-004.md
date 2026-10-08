---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# The lane's cleanest example of a high-certainty result attached to the wrong
# endpoint. Cochrane says high certainty; what it says it about is SYMPTOMLESS
# DVT, and zero events occurred for death, pulmonary embolism or symptomatic DVT
# across every included trial. Contested is set not because the evidence is
# disputed but because the popular claim and the demonstrated claim are different
# claims, which is what the flag is for in this warehouse.
# Source re-audit 2026-10-06: Cochrane CD004002.pub4 abstract re-read; every
# figure and certainty label confirmed. One overreach narrowed: 'a trial of a few
# thousand passengers has essentially no chance of observing any' -- at one
# symptomatic event per 4,656 long-haul flights (003) 2,918 passengers expect
# about 0.6 events with no stockings at all, so zero is likelier, not
# impossible (curator arithmetic; the review only says very large numbers are
# needed). No newer review or trial located (PubMed, 2026-10-06).
id: travel/compression-stockings-endpoint-gap-004
domain: travel
lane: "@travel-clinical"
grade: A (the symptomless-DVT reduction, high-certainty Cochrane); D (any effect on death, pulmonary embolism or symptomatic DVT)
locale: universal
as_of: 2021
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/33878207/"  # Clarke MJ, Broderick C, Hopewell S, Juszczak E, Eisinga A. 2021, Cochrane Database Syst Rev 4(4):CD004002, doi 10.1002/14651858.CD004002.pub4, PMCID PMC8092568 -- 12 randomized trials, n=2918, searched to 1 April 2020. Abstract read verbatim 2026-09-02
  - "source:travel/flight-vte-absolute-vs-relative-003 -- the risk this intervention is bought against, with the base rate attached"
  - "source:sleep-recovery/evening-light-mechanism-vs-intervention-012 -- the same structural lesson from a different product: what a trial measured is not what the product is sold on"
  - "source:exercise/recovery-modality-soreness-vs-performance-024 -- the warehouse's other perceived-versus-measured endpoint split"
  - "framework:GRADE -- the review grades its own outcomes separately and the spread is the finding: HIGH certainty for symptomless DVT, MODERATE for superficial vein thrombosis, LOW for oedema (limited by how oedema was measured), and NO estimate at all for death, pulmonary embolism or symptomatic DVT because no such events occurred in any trial. An absent event count is not a null result."
applicability:
  axes:
    - key: cardiovascular_condition
      type: categorical
      role: hard
      unknown_policy: block_specifics
    - key: pregnancy_status
      type: categorical
      role: hard
      unknown_policy: block_specifics
refraction_notes:
  - note: >
      THE HIGH-CERTAINTY RESULT IS REAL AND IT IS ABOUT AN ASYMPTOMATIC FINDING.
      Across the trials of stockings on both legs, 50 of 2637 participants with
      follow-up data had a SYMPTOMLESS deep vein thrombosis: 3 wore stockings, 47
      did not, odds ratio 0.10 (95 percent CI 0.04 to 0.25, P less than 0.001),
      rated high certainty. Three trials had no symptomless events at all. This is
      a large, consistent and well-graded effect, and it is on a screening finding
      rather than on an illness anyone noticed.
    grade: A
  - note: >
      THE ENDPOINTS PEOPLE ACTUALLY CARE ABOUT HAVE NO DATA, NOT A NULL. The
      review states that no deaths, pulmonary emboli or symptomatic DVTs were
      reported across the included trials, and concludes it therefore cannot
      assess the effect of stockings on those outcomes. That is a very different
      statement from "stockings do not prevent them." It also tells you why:
      randomized trials powered for those outcomes "would need to include a very
      large number of people," which follows directly from the base rate recorded
      in this lane's absolute-risk item.
    grade: A
  - note: >
      THE OTHER OUTCOMES, GRADED HONESTLY. Superficial vein thrombosis: 16 of 1804
      people, 4 in stockings and 12 not, odds ratio 0.45 (95 percent CI 0.18 to
      1.13, P = 0.09), moderate certainty -- the interval crosses 1. Oedema:
      reduced, mean difference -4.72 (95 percent CI -4.91 to -4.52) from six
      trials, but only LOW certainty, and the review says explicitly that the
      certainty was limited by the way oedema was measured, with three further
      trials unpoolable because they measured it differently. No significant
      adverse effects were reported.
    grade: B
  - note: >
      WHO WAS IN THE TRIALS. Twelve randomized trials, 2918 participants, all
      flights longer than five hours. Eight trials enrolled people judged at low or
      medium risk of developing DVT (n=1598) and two enrolled high-risk
      participants (n=1273). Ten trials compared graduated compression stockings on
      both legs against none; one used compression tights; one put a stocking on
      one leg outbound and the other leg on the return. So the evidence is not
      exclusively about healthy travellers, and the high-risk trials are a
      substantial share of it -- which matters, because whether a benefit on
      asymptomatic clot means anything is likeliest to differ between those groups.
    grade: B
  - note: >
      WHY CONTESTED IS SET. There is no scientific dispute inside this review; the
      dispute is between what it found and what the product is sold on. "Compression
      socks prevent DVT on flights" is a claim about symptomatic disease, and the
      only outcome with high-certainty evidence is a symptomless one. This is the
      same shape as the sleep domain's blue-light entry, where a well-run study and
      a consumer product get spoken as one sentence. The flag exists for that gap,
      not for uncertainty in the evidence.
    grade: A
  - note: >
      NOT COVERED, AND ONE THING TO BE CAREFUL ABOUT. The review says nothing about
      correct sizing, fitting or compression class, nothing about who should avoid
      them, and nothing about wearing them outside flights. There is a real clinical
      contraindication space around compression garments -- peripheral arterial
      disease being the usual example -- that this source does not address at all,
      and its absence here is not a clearance. Route anyone with a circulatory or
      diabetic condition to a clinician rather than to a shopping recommendation.
    grade: D
claim: >
  The Cochrane review of compression stockings for airline passengers included 12
  randomized trials with 2918 participants on flights longer than five hours. Its
  headline result is high-certainty and narrow: among participants wearing
  graduated compression stockings on both legs, 50 of 2637 with follow-up data had
  a SYMPTOMLESS deep vein thrombosis -- 3 in stockings, 47 not -- an odds ratio of
  0.10 (95 percent CI 0.04 to 0.25). Superficial vein thrombosis may be reduced
  (16 of 1804; OR 0.45, 95 percent CI 0.18 to 1.13, moderate certainty), and leg
  oedema is reduced (mean difference -4.72, low certainty, limited by how oedema
  was measured). No significant adverse effects were reported. Decisively, NO
  deaths, pulmonary emboli or symptomatic DVTs occurred in ANY included trial, so
  the review states it cannot assess the effect on those outcomes and that trials
  powered for them would need very large numbers of people. Eight of the twelve
  trials enrolled low- or medium-risk passengers and two enrolled high-risk
  passengers. The operative reading: stockings have a strong, well-graded effect on
  a finding that is detected rather than felt, and the evidence base is silent --
  not negative, silent -- on the outcomes that motivate wearing them.
reasoning: >
  Clarke et al. 2021 (Cochrane CD004002.pub4) is among the higher-quality documents
  this warehouse cites, and the interesting thing about it is not its effect size
  but its endpoint structure. It grades four outcomes at four different certainty
  levels and reports zero events for a fifth group of outcomes, and reading it
  correctly means holding all of that rather than lifting the headline odds ratio.
  The odds ratio of 0.10 on symptomless DVT is graded at the top band here without
  hesitation: it is a Cochrane high-certainty rating on 2637 participants with a
  tight interval and a consistent direction. What it is not is evidence about
  illness. A symptomless deep vein thrombosis is a finding on a scan, and whether
  reducing those reduces anything a traveller would ever experience is precisely
  the question the review says it cannot answer, because the events needed to
  answer it did not occur. Recording that as "no effect demonstrated on
  symptomatic outcomes" would be a misreading in the opposite direction -- an
  absence of events is not a null result, and this warehouse has a standing rule
  against converting one into the other. The reason it plays out this way is
  quantitative and it links straight to the absolute-risk item in this lane: at
  roughly one symptomatic event per several thousand long-haul flights, a trial of
  a few thousand passengers expects fewer than one such event even if nobody wore
  stockings (2,918 passengers at one per 4,656 flights is about 0.6, so zero events
  is the likelier outcome; that arithmetic is the curator's, composed from this
  review and item 003). The review says only that trials powered for these
  outcomes would need a very large number of people. Contested is set deliberately. Not because
  reviewers disagree -- they do not -- but because the sentence people say about
  this product and the sentence the evidence supports are about different
  endpoints, and this warehouse flags exactly that gap. The oedema finding is
  worth keeping in view as the honest small benefit: it is the outcome a healthy
  traveller might actually notice, it is real, and it is only low certainty.
---

# travel/compression-stockings-endpoint-gap-004

Compression socks for flights have unusually good evidence behind them. The
question is what the evidence is about.

Twelve randomized trials, 2,918 passengers, all flights over five hours. Among
those wearing graduated compression stockings on both legs, three people had a
deep vein thrombosis; among those not wearing them, forty-seven did. That is an
odds ratio of about 0.10, and Cochrane rates it high certainty. As effect sizes
in preventive medicine go, that is enormous.

Every one of those clots was symptomless.

That word is doing all the work. A symptomless deep vein thrombosis is something
a study found by scanning people who felt fine. It is not the thing anyone buys
compression socks to avoid.

What about the things people do buy them to avoid? The review is explicit: no
deaths, no pulmonary emboli and no symptomatic clots occurred in any of the
twelve trials, and it therefore cannot assess whether stockings affect them. It
adds that a trial capable of answering the question would need a very large
number of people.

Read that carefully, because it can be misread in both directions.

It is not evidence that stockings fail to prevent serious clots. Zero events in
both arms is not a null result; it is no result. And the reason there were none is
mostly arithmetic: the other item in this lane puts the symptomatic event rate
at roughly one per several thousand long-haul flights, so a study of a few
thousand passengers should expect fewer than one even with no stockings at all.

But it is also not permission to say stockings prevent DVT and let the listener
supply the meaning of the word.

The rest of the review is the honest middle. Superficial vein thrombosis may be
reduced, at moderate certainty, with an interval that still crosses no effect. Leg
swelling is reduced, at low certainty, and the reviewers say plainly the certainty
was limited by how swelling was measured. No significant harms were reported. The
swelling result is the one a healthy traveller is most likely to actually notice,
and it is the weakest-graded of the lot -- which is a fair summary of the whole
product.

One thing the review does not cover at all, and its silence should not be read as
clearance: sizing, compression class, and who should not wear compression
garments. There is a real clinical contraindication space here that this evidence
never touches. Anyone with a circulatory condition or diabetes is a question for a
clinician, not for a shopping list.
