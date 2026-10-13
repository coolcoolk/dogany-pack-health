---
# Authored 2026-09-02 (cooking-lane collection sprint). @test-kitchen, universal.
# A technique-decision item: which lever actually controls browning. Ships the
# CORRECTED version of two pieces of kitchen lore -- the fixed "browning starts
# at 140C" threshold, and the idea that browning is primarily a heat-level
# problem -- against a 2025 peer-reviewed review read directly.
id: cooking/browning-water-activity-013
domain: cooking
lane: "@test-kitchen"
grade: B
locale: universal
as_of: 2025
contested: no
sources:
  - "https://doi.org/10.3390/foods14111881"  # El Hosry L, Elias V, Chamoun V, Halawi M, Cayot P, Nehme A, Bou-Maroun E. Maillard Reaction: Mechanism, Influencing Parameters, Advantages, Disadvantages, and Food Industrial Applications: A Review. Foods 2025;14(11):1881. PMC12154226. Source for the activation energies, the reported temperature optima and the water-activity dependence
  - "source:cooking/craft-testing-ceiling-001 -- the same lane rule this item relies on, and the item that already carries the searing-seals-in-juices correction"
refraction_notes:
  - note: >
      THE KINETICS ARE FROM MODEL SYSTEMS, NOT FROM A PAN. The activation
      energies and temperature optima in the review come from sugar-plus-amino-
      acid systems: aqueous glucose-glycine, glucose-phenylalanine, milk powders.
      They establish that the reaction is strongly temperature-dependent and
      strongly water-activity-dependent. They do NOT establish a browning
      temperature for a steak, and no such figure should be quoted from them.
    grade: B
  - note: >
      THE FIXED THRESHOLD IS THE FOLKLORE BEING CORRECTED. Kitchen writing
      commonly states that the Maillard reaction "starts" at a specific
      temperature, usually given as about 140C or 154C. The review reports
      something different in shape: a continuous, Arrhenius-type temperature
      dependence, with model-system studies finding maximum rates near 120C and
      the rate falling off both above 120C and below 100C. There is no switch.
      Do not ship a threshold number.
    grade: B
  - note: >
      THE SURFACE-TEMPERATURE STEP IS AN INFERENCE, LABELLED AS ONE. That a wet
      surface is pinned near 100C by evaporation is standard physics, not
      something this review measured. The chain -- wet surface stays near 100C,
      near-100C plus high water activity is a slow region for the reaction,
      therefore drying the surface is the effective lever -- is a mechanistic
      argument built on the review's two measured dependencies. It is stated as
      reasoning, not reported as a result.
    grade: C
  - note: >
      THIS ITEM IS ABOUT BROWNING, NOT ABOUT MOISTURE IN THE FINISHED FOOD. It
      makes no claim about juiciness, yield, or interior texture, and it must not
      be read as endorsing drying food out. The claim is confined to the surface
      condition at the moment browning is wanted.
    grade: A
claim: >
  Browning is controlled by surface water at least as much as by burner setting.
  A 2025 review of Maillard reaction kinetics reports two dependencies. On
  temperature, the reaction follows Arrhenius behaviour -- reported activation
  energies of 109 kJ/mol for aqueous glucose-glycine and 145 kJ/mol for
  glucose-phenylalanine -- with model-system work finding maximum rate near 120C
  and the rate decreasing both above 120C and below 100C. On moisture, the rate
  peaks around a water activity of 0.6-0.7, and beyond that point the reaction
  slows because excess free water dilutes the reactants. Because evaporation pins
  a wet surface near 100C, a wet surface is held in a region that is unfavourable
  on both axes at once. The commonly quoted fixed onset temperature for browning
  (usually stated as about 140C) is not what the kinetic literature describes; the
  dependence is continuous, not a threshold.
reasoning: >
  For a live cooking session the useful question is not what browning is but which
  lever to pull when food is not browning, and the default answer in kitchen lore
  -- more heat -- is at best half right. The review supplies two measured
  dependencies from directly retrieved peer-reviewed work, and they point at the
  same neglected variable: surface water suppresses the reaction both by holding
  the temperature down through evaporation and by sitting above the water-activity
  band where the reaction is fastest. That makes drying the surface a real
  technique decision rather than a fussy habit. The item stays in the solid band
  rather than the top one for an honest reason: everything measured here was
  measured in model systems, and the step from those kinetics to a piece of meat
  in a pan is an inference. It is written as an inference. The threshold
  correction is included because a fixed onset number is exactly the kind of
  precise-sounding figure that gets repeated until it is treated as measured, and
  the kinetic literature does not contain it.
---

# cooking/browning-water-activity-013

When food is not browning, the reflex is to turn the heat up. The kinetics
suggest the more effective move is usually to dry the surface.

A 2025 review of the Maillard reaction reports two dependencies. The first is
temperature, and it behaves the way a chemical reaction behaves: Arrhenius, with
activation energies around 109 kJ/mol for glucose with glycine in water and 145
kJ/mol for glucose with phenylalanine. Model-system studies in the review found
maximum rates near 120C, with the rate falling off both above 120C and below
100C.

The second is water. The reaction peaks at a water activity of roughly 0.6 to
0.7. Above that, more free water slows it down, because the reactants are simply
diluted.

Now put those together with something the review did not measure but that is not
in dispute: while a surface is wet, evaporation holds it near 100C no matter how
hot the pan is. So a wet surface is unfavourable on both axes at the same time --
too cool, and too wet. Nothing much happens until the surface water is gone, and
only then does pan temperature start to matter. Patting meat dry, not crowding
the pan, letting a surface air-dry before it goes in: those are not fussiness,
they are the rate-limiting step. This chain is a mechanistic argument, not a
measured cooking result, and is offered as such.

One number that circulates should not be repeated. Kitchen writing routinely says
browning "starts" at some specific temperature, usually around 140C. The kinetic
literature does not describe a threshold; it describes a continuous temperature
dependence whose model-system optima sit closer to 120C. There is no switch to
cross, and quoting one gives a precise-sounding figure that nothing measured.

Two boundaries. Everything measured in the review was measured in sugar-and-amino-
acid systems and powders, not on meat, so no browning temperature for a steak
follows from it. And this item is strictly about the surface at the moment
browning is wanted -- it says nothing about juiciness or yield, and is not an
argument for drying food out.
