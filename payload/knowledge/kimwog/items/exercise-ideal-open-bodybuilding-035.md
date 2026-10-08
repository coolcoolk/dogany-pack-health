---
# Body-ideal archetype sprint 2026-09-30. Open bodybuilding is the reference
# point the other physique divisions are defined against, and the one whose
# culture most often carries the drugs and extreme-cut routes; this row states
# both so the agent can keep the goal and refuse the route
# (exercise/harm-route-boundary-031).
id: exercise/ideal-open-bodybuilding-035
domain: exercise
grade: A (rule -- federation judging criteria); B (contest-prep and injury evidence)
lane: "@gym-craft"
locale: universal
as_of: 2014-2026
contested: no
sources:
  - "https://www.ifbbpro.com/rules/"  # IFBB Pro League Men's Open: eight mandatory poses incl. front/back lat spread, side triceps, most muscular; no weight cap
  - "https://ifbb.com/wp-content/uploads/2023/02/Mens-Classic-Physique-2023.pdf"  # IFBB Art. 10.1 shared assessment language: muscular bulk, balanced development, muscular density and definition
  - "https://pubmed.ncbi.nlm.nih.gov/24864135/"  # Helms ER, Aragon AA, Fitschen PJ. J Int Soc Sports Nutr 2014;11:20 -- natural contest prep: ~0.5-1%/wk loss, protein 2.3-3.1 g/kg LBM; dehydration/electrolyte manipulation 'can be dangerous, and may not improve appearance'; eating/body-image disorder risk
  - "https://pubmed.ncbi.nlm.nih.gov/27328853/"  # Keogh JW, Winwood PW. Sports Med 2017;47:479-501 -- bodybuilding had the lowest injury rates of the weight-training sports (0.24-1 per 1000 h)
  - "https://pubmed.ncbi.nlm.nih.gov/24582699/"  # Sagoe D et al. Ann Epidemiol 2014 -- global lifetime AAS prevalence 3.3%, males 6.4%; athlete samples a significant predictor
  - "exercise/harm-route-boundary-031"
  - "exercise/volume-doseresponse-007"
applicability:
  axes:
    - key: primary_goal
      type: categorical
      role: soft
      unknown_policy: hedge
    - key: training_status
      type: categorical
      role: soft
      unknown_policy: hedge
refraction_notes:
  - note: >
      THE STAGE LOOK OF THE OPEN CLASS IS NOT A NATURAL-TRAINING TARGET, and the
      agent should not pretend otherwise. Non-medical anabolic steroid use is
      common enough in athlete samples that sample type predicts prevalence
      (Sagoe 2014). The route is caught by harm-route-boundary-031; the goal
      "as much muscle as I can carry" is not, and is served by natural-contest
      methods (Helms 2014).
    grade: B
  - note: >
      PEAK-WEEK DEHYDRATION IS A CAUGHT ROUTE with its own evidence: the
      natural-contest review calls it potentially dangerous and possibly
      useless for appearance.
    grade: B
claim: >
  Open bodybuilding judges maximal muscular size together with balance,
  density and definition at extreme leanness, across eight mandatory poses
  (including lat spreads, side triceps and most muscular), with no body-weight
  cap. It is the size end of the physique continuum: classic physique caps mass
  to keep proportion first; men's physique marks extreme muscularity down.
  Injury rates are the lowest of the weight-training sports; the health risks
  that define the culture are drug use and extreme contest preparation, not
  training injury.
reasoning: >
  Pose list and absence of a cap are the federation's rule text. Keogh and
  Winwood's systematic review places bodybuilding's injury incidence at 0.24-1
  per 1000 h, lowest of the weight-training sports. Helms 2014 is the standard
  evidence-based review for natural contest preparation and supplies both the
  safe-rate figure and the dehydration warning. Sagoe 2014 establishes that
  non-medical steroid use is a real population phenomenon concentrated in
  athlete samples, which is why the harm boundary matters most for this
  archetype.
---

# exercise/ideal-open-bodybuilding-035 -- 오픈 보디빌딩

**한 줄 그림:** 체급 상한 없이 가능한 한 큰 근육을, 좌우·상하 균형과 선명도를 갖춰 극도로 낮은
체지방에서 보여주는 몸.

## Distinguishing features

Mass first (with balance and density), no weight cap, "most muscular" allowed.
Everything classic caps and men's physique marks down is rewarded here.

## Measurable here

- `skeletal_muscle_kg` -- the central strand.
- Segmental lean mass (all five segments) -- balance and lagging parts.
- `body_fat_pct` -- conditioning phase only.
- `body_weight` -- phase direction (surplus/deficit).
- Workout logs: weekly sets per muscle (the volume dose-response, item 007),
  e1RM on lead compounds as a proxy that load is still progressing.

## Not measurable here

Muscle density/separation/striation, symmetry by eye, girths (no tokens).

## Training emphasis and practice

High-volume hypertrophy per muscle with long building phases, periodic lean
phases. The program objective is `band_center` while building. Practice picks
are optional extras.

## Failure modes and risks

Drugs, extreme cuts, peak-week dehydration (caught routes); eating and body-image
disorder risk in aesthetic sport (Helms 2014); low joint-injury rates otherwise.

## Combines / conflicts

Conflicts with endurance volume (interference, energy), with the weight cap of
classic, and with the "less muscular" ceiling of men's physique. Compatible with
mobility and Pilates as supplementary work.
