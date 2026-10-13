---
# Authored 2026-09-02 (nutrition-lane collection sprint, v11). The "0.5 to 1
# percent of body weight per week" rule is quoted everywhere as though it were a
# settled dose-response. It is one small trial plus a review that cites it. Filed
# with the provenance visible so the rule cannot be re-inflated later.
id: nutrition/weight-loss-rate-lean-mass-012
domain: nutrition
lane: "@obs-inferential"
grade: C
locale: universal
as_of: 2011-2019
contested: yes
sources:
  - "https://doi.org/10.1123/ijsnem.21.2.97"  # Garthe I, Raastad T, Refsnes PE, Koivisto A, Sundgot-Borgen J. Int J Sport Nutr Exerc Metab 2011;21(2):97-104. PMID 21558571 -- n=24 elite athletes randomised to 0.7 vs 1.4 percent per week target
  - "https://doi.org/10.1186/1550-2783-11-20"  # Helms ER, Aragon AA, Fitschen PJ. J Int Soc Sports Nutr 2014;11:20. PMID 24864135 -- the review that carries the 0.5-1 percent per week recommendation and the 2.3-3.1 g/kg lean mass protein band
  - "https://doi.org/10.3389/fnut.2019.00131"  # Slater GJ, Dieter BP, Marsh DJ, Helms ER, Shaw G, Iraki J. Front Nutr 2019;6:131. PMID 31482093 -- the mirror-image question, energy surplus, and its weak evidence base
  - "source:nutrition/protein-intake-002 -- owns the hypocaloric lean-mass-retention protein band this item's context refers to"
  - "source:nutrition/body-composition-measurement-floor-011 -- the instrument limit that bounds any attempt to verify a rate week to week"
applicability:
  axes:
    - key: body_weight_kg
      type: numeric
      role: scale
      unknown_policy: ask
      rescale:
        per_unit_low: 0.005    # kg of body weight lost per week, per kg of measured body weight
        per_unit_high: 0.010
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE DURATION CONFOUND IS FATAL TO A CLEAN READING and is rarely repeated
      when this trial is cited. The two arms were not equal in length: the slow
      arm ran 8.5 weeks and the fast arm 5.3 weeks, because both were run to the
      same total weight loss. Any difference in lean-mass outcome is therefore
      confounded with 3 extra weeks of resistance training in the slow arm. The
      trial cannot separate rate of loss from duration of training.
    grade: C
  - note: >
      DIRECTION ONLY, NOT A DOSE-RESPONSE. One randomised trial with 24 elite
      athletes, unblinded, at two rates, does not establish a curve. There is no
      basis for treating 1.0 percent per week as safe and 1.2 percent as harmful,
      and no evidence at all about rates outside the tested pair.
    grade: D
  - note: >
      THE MIRROR CLAIM IS WEAKER STILL. The parallel belief that a deliberate
      energy surplus is required to maximise hypertrophy is reviewed as poorly
      supported. Do not present a surplus prescription as the symmetric partner of
      this deficit guidance.
    grade: D
  - note: >
      UNVERIFIABLE IN PRACTICE at the week scale. The rate this item describes is
      smaller than the noise on a consumer body-composition measurement, so a
      user cannot confirm they are hitting it from one week of readings. Pair with
      nutrition/body-composition-measurement-floor-011 before quoting a rate as a
      target to be checked.
    grade: B
claim: >
  Slower weight loss appears to preserve lean mass better than faster loss during
  resistance training, but the evidence is one small randomised trial. In 24
  elite athletes assigned to a 0.7 percent versus 1.4 percent body-weight-per-week
  target (achieved 0.7 versus 1.0 percent per week), both groups lost about 5.5
  percent of body weight and both lost fat mass, while lean body mass increased
  2.1 percent in the slow group and was unchanged in the fast group. The commonly
  quoted 0.5 to 1 percent per week guidance is a review-level derivation resting
  largely on this trial. The trial arms differed in duration (8.5 versus 5.3
  weeks), which confounds rate with training exposure.
reasoning: >
  The direction of this claim is plausible and is the field's working consensus,
  and the honest description of its base is one unblinded randomised trial with
  24 participants in an elite athletic population, plus a review that carries the
  figure forward. The duration imbalance between arms means the study cannot
  cleanly attribute the lean-mass difference to the rate of loss rather than to
  the additional three weeks of resistance training the slower group received.
  Under this lane's rules that is a forced downgrade to the observational band
  with a contested flag, not a dismissal: no contrary trial was located, and the
  direction is coherent with the protein and training literature. What must not
  happen is the rule being spoken as a calibrated dose-response with a safe
  boundary. The scaling here is genuinely per-kilogram, so the rate is refracted
  from measured body weight rather than quoted as fixed kilograms, and it must be
  paired with the measurement-floor item because the resulting weekly target is
  smaller than what any consumer device can verify in a week.
---

# nutrition/weight-loss-rate-lean-mass-012

Losing weight slowly is supposed to protect muscle better than losing it fast,
and the whole rule rests on a single study. Twenty-four elite athletes were
randomised to lose weight at roughly half a percent or one and a half percent of
body weight per week while resistance training four times a week. Both groups
lost a similar total and both lost fat. Lean mass rose about two percent in the
slow group and did not move in the fast group.

The detail that almost never travels with the citation is that the two arms were
not the same length. Because both were run to the same total weight loss, the
slow group trained for eight and a half weeks and the fast group for a little
over five. The slow group therefore got three extra weeks of lifting, and the
study cannot separate that from the rate of loss. The direction survives; the
causal attribution does not.

So the guidance is worth following and is not worth defending as precise. There
is no evidence distinguishing one percent per week from one and a bit, no data
outside the two rates tested, and the mirror belief that gaining requires a
deliberate energy surplus is on even thinner ground. There is also a practical
trap: the weekly change this rule describes is smaller than the measurement noise
on any consumer body-composition device, so a user cannot verify from one week's
readings whether they are hitting it. Rate targets belong on a multi-week trend
or nowhere.
