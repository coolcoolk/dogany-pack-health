---
# Source re-audit 2026-10-06: Neale 2019 abstract re-read (all numbers hold).
# The boundary this item named -- no trial at high SPF -- was closed by the
# Sun-D randomised trial (Tran 2025, BJD, PMID 40927943): SPF 50+ for a year
# lowered 25(OH)D by 5.2 nmol/L vs discretionary use and raised deficiency
# prevalence. Claim, one note and the closing prose updated; the unsourced
# 'SPF 50-plus dominates the Korean market' line removed. engine_rules added.
id: skincare-hygiene/sunscreen-vitamin-d-004
domain: skincare-hygiene
lane: "@clinical-derm"
grade: B
locale: universal
as_of: 2025-11
contested: yes
sources:
  - "Neale RE, Khan SR, Lucas RM, Waterhouse M, Whiteman DC, Olsen CM. The effect of sunscreen on vitamin D: a review. Br J Dermatol 2019 Nov;181(5):907-915. DOI 10.1111/bjd.17980. PMID 30945275. Systematic review following MOOSE guidelines, English-language literature 1970 to 21 November 2017; 4 experimental studies, 3 field trials (2 randomised), 69 observational studies."
  - "Tran V, Duarte Romero BL, Andersen H, Clarke M, Collins LG, Dawson T, Hartel G, Lefevre JG, Lucas RM, McLeod DSA, Milne RL, Sinclair C, Whiteman DC, Waterhouse M, Neale RE. Effect of daily sunscreen application on vitamin D: findings from the open-label randomized controlled Sun-D Trial. Br J Dermatol 2025 Nov 18;193(6):1128-1137. DOI 10.1093/bjd/ljaf310. PMID 40927943. ACTRN12621001752853. 639 Australian adults aged 18-70 not routinely using sunscreen or vitamin D supplements, SPF 50+ on forecast UV index 3+ days vs discretionary use, about one year; NHMRC-funded."
  - "source:skincare-hygiene/sunscreen-rct-what-was-shown-001 -- the same Queensland research group and the benefit side of the trade-off"
refraction_notes:
  - note: >
      THE EXPERIMENTAL AND THE REAL-WORLD EVIDENCE POINT DIFFERENT WAYS, AND
      THAT DISCORDANCE IS THE FINDING. Under artificial ultraviolet sources,
      sunscreen considerably abrogated vitamin D3 production -- with sources
      whose spectral output, the review notes, is unlike terrestrial sunlight.
      In field trials at about SPF 16 and in observational studies, no such
      effect appeared. Both halves must be
      spoken; picking one produces a confident wrong answer in either direction.
    grade: A
  - note: >
      THE FIELD TRIALS USED MODERATE SPF AND THE REVIEW SAYS SO. The randomised
      field evidence rests on sunscreens of approximately SPF 16. The review
      states explicitly that there have been NO trials of the high-SPF products
      now widely recommended and used. Any reassurance derived from this
      literature does not automatically extend to an SPF 50-plus product.
    grade: B
  - note: >
      AT SPF 50-PLUS THE FIELD RESULT IS NO LONGER NULL. The Sun-D trial
      randomised 639 adults to routine SPF 50-plus on days the UV index was
      forecast to reach 3 or more, against discretionary use, for about a
      year. The between-group effect on 25-hydroxyvitamin D was -5.2 nmol per L
      (95 percent CI -7.2 to -3.2), consistent across almost all subgroups, and
      deficiency below 50 nmol per L at the end was 45.7 versus 36.9 percent
      (prevalence ratio 1.33, 95 percent CI 1.14 to 1.55). Open-label, one
      country, people who did not already use sunscreen routinely. The
      authors keep recommending regular sunscreen and say users may need
      vitamin D testing or supplementation -- not less sunscreen.
    grade: B
  - note: >
      THE OBSERVATIONAL FINDING RUNS THE WRONG WAY FOR A NAIVE READING. Most
      observational studies found no association, or found self-reported
      sunscreen use associated with HIGHER 25-hydroxyvitamin D. That is almost
      certainly confounding by outdoor behaviour -- people who use sunscreen are
      people who go outside -- and must not be spoken as sunscreen raising
      vitamin D.
    grade: B
  - note: >
      A REVIEW OF OBSERVATIONAL STUDIES IS NOT AN INTERVENTION TRIAL. Of 76
      included studies, 69 are observational. The review followed a stated
      methodology and applied purpose-built quality criteria, which is why it is
      usable at all, but its evidentiary ceiling is set by what it pooled.
    grade: B
engine_rules:
  - when: user uses SPF 50-plus routinely and asks about vitamin D
    say: keep the sunscreen; a vitamin D test or supplement is a reasonable thing to raise with a clinician
    never: advise less sunscreen or deliberate unprotected sun to make vitamin D
    basis: Tran 2025 Sun-D trial
    basis_grade: B
  - when: user uses moderate SPF or occasional sunscreen
    say: field trials and population data show no meaningful effect on vitamin D
    never: describe sunscreen users' higher observational vitamin D as caused by sunscreen
    basis: Neale 2019 review
    basis_grade: B
claim: >
  The concern that sunscreen use causes vitamin D deficiency was not supported in
  real-world settings at moderate SPF, but that reassurance had a stated
  boundary, and the one trial that has since tested past it found a small real
  effect. A systematic
  review following MOOSE guidelines identified 4 experimental studies, 3 field
  trials (2 of them randomised) and 69 observational studies. In the experimental
  studies, using artificially generated ultraviolet radiation, sunscreen
  considerably abrogated vitamin D3 and 25-hydroxyvitamin D production. The
  randomised field trials found NO effect of daily sunscreen application on
  25-hydroxyvitamin D concentration -- but the sunscreens used provided only
  moderate protection, approximately SPF 16. The observational studies mostly
  found no association, or found self-reported sunscreen use associated with
  HIGHER 25-hydroxyvitamin D concentration. The reviewers conclude that there is
  little evidence sunscreen decreases 25-hydroxyvitamin D in real life and that
  vitamin D concerns should not negate skin-cancer prevention advice, while
  stating that no trials of the high-SPF sunscreens now widely recommended had
  been conducted. That trial now exists: in the Sun-D open-label randomised
  trial (639 Australian adults, about one year), routine SPF 50-plus on days
  with a forecast UV index of 3 or more lowered 25-hydroxyvitamin D by 5.2 nmol
  per L relative to discretionary use (95 percent CI -7.2 to -3.2) and raised the
  end-of-trial prevalence of concentrations below 50 nmol per L from 36.9 to
  45.7 percent (prevalence ratio 1.33). Its authors conclude that regular
  sunscreen users may need vitamin D supplementation, while still recommending
  regular sunscreen use.
reasoning: >
  This is a question a consumer will actually ask, and the honest answer has two
  parts that pull against each other. Mechanistically the worry is real and was
  demonstrated under artificial ultraviolet sources. Practically it does not show
  up in field trials or in population data. The review is marked contested for
  exactly that reason: the discordance between the experimental and the
  real-world evidence is unresolved, not settled. It sits in the solid band
  rather than the top band because sixty-nine of its seventy-six included studies
  are observational and its randomised evidence is two field trials at moderate
  SPF. The boundary the reviewers themselves drew is the most useful line in the
  item and is carried verbatim into the claim: the reassurance was earned at
  approximately SPF 16. The 2025 Sun-D trial tested past that boundary and found
  a small reduction, so the answer at SPF 50-plus is now "slightly lower vitamin
  D, keep the sunscreen, consider testing or supplementation", not "no effect".
  It remains one open-label trial in one country, which is why the grade does not
  move and the item stays contested. The observational finding that sunscreen users have
  higher vitamin D is kept in the item and flagged as confounded, because it
  would otherwise be the most quotable and most misleading sentence in the
  literature.
---

# skincare-hygiene/sunscreen-vitamin-d-004

Does sunscreen cause vitamin D deficiency. The honest answer has two halves that
disagree with each other, and both belong in the reply.

A systematic review following a stated methodology pulled 4 experimental studies,
3 field trials of which 2 were randomised, and 69 observational studies.

Under artificial ultraviolet sources, in the laboratory, sunscreen considerably
suppressed vitamin D3 production. The mechanism is real. It was demonstrated.

Out in the world, it does not show up. The randomised field trials found no
effect of daily sunscreen application on 25-hydroxyvitamin D. The observational
studies mostly found no association, and where they found one it usually ran the
other way -- self-reported sunscreen users had HIGHER vitamin D. That last result
is almost certainly confounding rather than a benefit: people who apply sunscreen
are people who go outdoors. It should never be spoken as sunscreen raising
vitamin D.

The reviewers' own conclusion is that there is little evidence sunscreen lowers
vitamin D in real-life use, and that vitamin D worries should not be allowed to
override skin-cancer prevention advice.

And then the line that most summaries of this literature drop. The randomised
field evidence was obtained with sunscreens of about SPF 16. The reviewers state
plainly that no trials have been done on the high-SPF products now widely
recommended and widely bought. The reassurance was earned at SPF 16.

That gap has since been tested. The Sun-D trial in Australia randomised 639
adults who did not already use sunscreen routinely to SPF 50-plus on every day
the UV index was forecast to reach 3, or to their own discretion, for about a
year. The sunscreen group ended 5.2 nmol per L lower on 25-hydroxyvitamin D, and
more of them were below 50 nmol per L at the end, 45.7 against 36.9 percent. A
small effect, measured blind to group, in an open-label trial. The authors did
not conclude "use less sunscreen". They concluded that regular users may need
vitamin D testing or supplementation, and that is the line to carry.
