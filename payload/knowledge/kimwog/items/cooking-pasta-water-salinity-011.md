---
# Authored 2026-09-02 (cooking-lane collection sprint). @test-kitchen, universal.
# A named folklore correction. Shipped as a DETERMINISTIC-CHEMISTRY item, which
# cooking/craft-testing-ceiling-001 already carves out as a legitimate pocket in
# this lane, with the arithmetic written out in full so the reader can check it
# rather than trust it.
id: cooking/pasta-water-salinity-011
domain: cooking
lane: "@test-kitchen"
grade: B (deterministic arithmetic on a textbook constant)
locale: universal
as_of: 2021
contested: no
sources:
  - "https://chem.libretexts.org/Courses/Modesto_Junior_College/Chemistry_143_-_Bunag/Chemistry_143_-_Introductory_Chemistry_(Bunag)/16:_Solutions/16.15:_Boiling_Point_Elevation"  # LibreTexts Chemistry (open chemistry teaching text, CK-12 licensed content curated onto LibreTexts; page last modified 2021-06-14). Source for the ebullioscopic constant of water, Kb = 0.512 C/m, and for the statement that over 100 g of NaCl per litre would be needed to raise the boiling point by a couple of degrees
  - "source:cooking/craft-testing-ceiling-001 -- the lane rule this item invokes: food chemistry is a deterministic pocket that can outrank taste-panel craft evidence"
refraction_notes:
  - note: >
      THE SOURCE IS A TEACHING TEXT, NOT A MEASUREMENT. What is cited is a
      standard physical constant and a standard equation, not an experiment
      someone ran on pasta. The claim is therefore only as good as the arithmetic,
      which is written out in the body so it can be checked. This is why the item
      does not sit at the top band despite the underlying physics being settled.
    grade: B
  - note: >
      THE ERROR DIRECTION IS SAFE. Real sodium chloride solutions do not fully
      dissociate at culinary concentrations, so the effective van 't Hoff factor
      is slightly below 2 and the true elevation is slightly SMALLER than the
      figures here. Every correction to this arithmetic makes the effect more
      negligible, never less. That one-sidedness is what licenses stating the
      conclusion confidently from a calculation.
    grade: A
  - note: >
      THE FOLKLORE IS WRONG ABOUT THE SIGN, NOT ONLY THE SIZE. The common form is
      that salt makes water boil faster. Dissolved salt RAISES the boiling point,
      so it can only make the water take marginally longer to reach a boil. Both
      effects are far below what anyone could perceive, but a correction that
      only says "the effect is small" leaves the direction error in place.
    grade: A
  - note: >
      SCOPE. This item is about temperature only. It makes no claim about pasta
      texture, starch gelatinisation, sauce adhesion, or how much salt actually
      ends up in the pasta -- none of which were researched. The seasoning
      rationale for salting is stated as the surviving purpose, not as a measured
      result.
    grade: D
claim: >
  Salting pasta water does not meaningfully raise its boiling point, and cannot
  make it boil sooner. Boiling-point elevation is a colligative property:
  delta-Tb = i x Kb x m, with Kb for water = 0.512 C per molal. At the
  conventional culinary salinity of roughly 10 g NaCl per litre, m = 10 / 58.44 =
  0.171 mol/kg, and with full dissociation (i = 2) delta-Tb = 0.512 x 2 x 0.171 =
  about 0.18 C. Even aggressive salting at 35 g per litre gives m = 0.599 and
  delta-Tb = about 0.61 C. The cited chemistry text notes that raising the boiling
  point by a couple of degrees would take over 100 g of NaCl per litre. Since
  dissolved salt raises rather than lowers the boiling point, salt can only make
  water take marginally longer to boil, never less. The surviving reason to salt
  pasta water is seasoning.
reasoning: >
  This is one of the most confidently repeated claims in home cooking and it is
  wrong twice over -- about the magnitude and about the direction -- so a lane
  that is read during actual cooking should carry the corrected version rather
  than stay silent and let the folklore fill the space. The evidence is a standard
  physical constant plus arithmetic rather than a cooking experiment, which is
  exactly why the item ships in the solid band rather than the top one, and why
  the calculation is written out instead of summarised. Two features make the
  calculation safe to act on. Its only significant assumption, complete
  dissociation of sodium chloride, errs in the conservative direction: real
  solutions dissociate less, so the true elevation is even smaller than stated.
  And the conclusion does not depend on precision at all, since a fifth of a
  degree is not a quantity any cook can act on regardless of how it is refined.
  The correction is stated with the direction included, because a correction that
  only shrinks the number leaves the "boils faster" error standing.
---

# cooking/pasta-water-salinity-011

The claim that salting pasta water changes how it boils is repeated constantly
and is worth doing the arithmetic on, because the arithmetic is short.

Boiling-point elevation is a colligative property. The elevation equals the van 't
Hoff factor times the ebullioscopic constant times the molality:

    delta-Tb = i x Kb x m,    Kb (water) = 0.512 C per molal

Take the conventional salting level, about 10 g of salt per litre of water.
Sodium chloride has a molar mass of 58.44 g/mol, so that is 0.171 mol per
kilogram of water. Sodium chloride dissociates into two ions, so i = 2:

    delta-Tb = 0.512 x 2 x 0.171 = about 0.18 C

Roughly a fifth of a degree. Salt heavily -- 35 g per litre, which is more than
most people use -- and it becomes about 0.61 C. The chemistry text this constant
comes from makes the same point from the other end: to move the boiling point by
a couple of degrees you would need to dissolve more than 100 g of salt in every
litre.

There is a second error in the popular version, and it is the more interesting
one. The folklore usually says salt makes water boil faster. Dissolved salt
raises the boiling point. Whatever it does, it cannot make water reach a boil
sooner -- it can only, imperceptibly, delay it. A correction that only shrinks
the number leaves that backwards belief intact.

Two honesty notes. The one assumption in the calculation, that the salt fully
dissociates, errs in the safe direction: real solutions at these concentrations
dissociate somewhat less, which makes the real effect smaller still. And this
item is about temperature and nothing else. It says nothing about texture, starch,
or how sauce clings, none of which were researched here. The reason to salt the
water is that it seasons the pasta.
