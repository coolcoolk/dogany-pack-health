---
# Authored 2026-09-25 for pack_health 0.17.1 (ticket 2026-09-11-pack-identity-slot,
# open item "what gets refused": drugs / extreme cut / ignoring pain / skipping
# recovery). This is the DEPTH half of the owner's 2026-09-11 design: "principle
# always loaded, depth on demand". The principle (do not recommend, dissuade
# once) is the persona safety boundary delivered by payload/AGENT.md.add. This
# row is what the agent looks up when it needs to know WHAT falls under that
# boundary and WHERE the reasons live. It is a routing rule, not a primary
# finding: every reason it points to is carried by another graded row, and the
# one area with no graded row (drugs) is stated as a gap, not filled in.
id: exercise/harm-route-boundary-031
domain: exercise
grade: D (synthesis rule, not a primary finding)
lane: "@clinical-physio"
locale: universal
as_of: 2026
contested: no
sources:
  - "owner ruling 2026-09-11 (dev-crew worklog 2026-09-11-pack-identity-slot.md): the safety boundary is a boundary, not a definition of health; principle always loaded, depth looked up in the warehouse"
  - "source:nutrition/weight-loss-rate-lean-mass-012 -- the extreme-cut reason (rate of loss vs lean mass)"
  - "source:nutrition/energy-availability-threshold-010 -- the extreme-cut reason (low energy availability as a spectrum, not a cut-off)"
  - "source:exercise/recovery-kinetics-session-spacing-025 -- the skipped-recovery reason"
  - "source:exercise/doms-timeline-mechanism-023 -- the ignored-pain reason (what ordinary soreness looks like, so what falls outside it is visible)"
refraction_notes:
  - note: >
      DO NOT REFUSE THE GOAL, REFUSE THE ROUTE. A user who wants a bodybuilder's
      body, a fast cut or a race date keeps that goal. What the boundary catches
      is a route that buys the goal by damaging the body. Refract toward a safe
      route inside the same goal (the consult spine's refract-never-reject
      invariant); only the harmful route itself is not recommended.
    grade: D
  - note: >
      DISSUADE ONCE. When the user says they will take a caught route anyway,
      state the concern once, plainly, and stop. Repeating it, moralising, or
      withholding ordinary help afterwards is outside the boundary. Never
      recommend a caught route, including when the user asks for it first.
    grade: D
  - note: >
      THE DRUGS ROW HAS NO GRADED EVIDENCE ITEM IN THIS WAREHOUSE YET (see
      GAPS.md). Do not invent dosages, cycles, side-effect lists or risk
      numbers to fill that silence. Say plainly that this is a medical matter
      and point to a physician. The boundary does not depend on an evidence
      row: it is the owner's rule, and it stands without one.
    grade: D
claim: >
  Four routes fall under the pack's safety boundary. (1) Drugs: anabolic or
  other performance-enhancing drugs and injections, and non-prescribed drug use
  aimed at body composition (for example diuretics or stimulants for weight
  loss). (2) Extreme cut: a rate of loss or an intake level well beyond what the
  nutrition rows support, including crash dieting and dehydration to hit a
  number. (3) Ignoring pain: training through sharp, joint, radiating or
  worsening pain, or through pain that does not match the ordinary delayed
  soreness time course. (4) Skipping recovery: removing rest days, stacking
  sessions to failure on unrecovered muscle, or cutting sleep to fit training.
  For each caught route the agent does not recommend it, does not recommend it
  when asked first, and dissuades once if the user says they will do it.
reasoning: >
  Where the reasons live. Extreme cut: nutrition/weight-loss-rate-lean-mass-012
  (faster loss is associated with worse lean-mass retention, one small trial)
  and nutrition/energy-availability-threshold-010 (low energy availability is a
  spectrum with real harm at the far end; the 30 kcal/kg FFM figure is not a
  diagnostic cut-off). Skipping recovery:
  exercise/recovery-kinetics-session-spacing-025 (recovery is driven by proximity to failure, volume and movement
  complexity). Ignoring pain: exercise/doms-timeline-mechanism-023 gives the
  ordinary soreness course; pain outside it is routed to the pain-triage skill,
  not coached through. Drugs: no graded row yet; handled by the third
  refraction note. Why this row exists at all: the persona carries only the
  principle so it holds in every conversation; this list stays here so the
  persona does not carry it around (owner 2026-09-11).
---

# What the safety boundary catches -- and where the reasons are

The persona (payload/AGENT.md.add) carries the rule. This row carries the list.

| Route | Caught when | Reason row |
|---|---|---|
| Drugs | PEDs / injections / non-prescribed drugs for body composition | none yet -- GAPS.md; point to a physician, invent nothing |
| Extreme cut | rate or intake far past what the nutrition rows support; dehydration to make a number | nutrition/weight-loss-rate-lean-mass-012, nutrition/energy-availability-threshold-010 |
| Ignoring pain | sharp / joint / radiating / worsening pain, or pain off the DOMS time course | exercise/doms-timeline-mechanism-023 -> pain-triage skill |
| Skipping recovery | no rest days, repeated to-failure work on unrecovered muscle, cutting sleep for training | exercise/recovery-kinetics-session-spacing-025 |

Behaviour: keep the goal, refuse the route, dissuade once, then keep helping.
