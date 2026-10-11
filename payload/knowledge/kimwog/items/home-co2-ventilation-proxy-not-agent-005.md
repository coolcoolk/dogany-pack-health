---
# Kimwog warehouse #1. HOME-DOMAIN OPENING SPRINT 2026-09-02
# (marker: home-lane-opening-001-013). CONTESTED. Ships the CORRECTED version
# of a claim that is now sold on every consumer air-quality monitor.
id: home/co2-ventilation-proxy-not-agent-005
domain: home
lane: "@home-environment"
grade: C (the CO2 reading as a ventilation indicator); D (CO2 itself as the agent at residential levels)
locale: universal
as_of: 2016-2023
contested: yes
sources:
  - "https://doi.org/10.1111/ina.12284"  # Zhang X, Wargocki P, Lian Z, Thyregod C. Effects of exposure to carbon dioxide and bioeffluents on perceived air quality, self-assessed acute health symptoms, and cognitive performance. Indoor Air 2017;27(1):47-64
  - "https://doi.org/10.1016/j.buildenv.2023.110331"  # Fan Y, Cao X, Zhang J, Lai D, Pang L. Short-term exposure to indoor carbon dioxide and cognitive task performance: a systematic review and meta-analysis. Building and Environment 2023;237:110331
  - "source:home/kr-mandated-ventilation-rate-004"  # within-warehouse cross-ref: the thing a CO2 reading is actually a proxy FOR
claim: >
  A rising indoor CO2 reading is a usable indicator that a room is
  under-ventilated. It is NOT established that CO2 itself is what harms
  cognition at residential concentrations, and the two statements are routinely
  collapsed into one. The decisive experiment is Zhang 2017, which separated
  them: exposures where PURE CO2 was added produced no statistically significant
  effect on perceived air quality, on self-assessed acute symptoms, or on
  cognitive performance, while exposure to human BIOEFFLUENTS at a CO2 level of
  3000 ppm degraded perceived air quality, increased headache, fatigue,
  sleepiness and difficulty thinking clearly, and slowed several cognitive
  measures. Same CO2 number, opposite result, depending on whether the rest of
  what people emit was in the air. The 2023 meta-analysis over fifteen studies
  does find complex-task decrements below 5000 ppm and reports that complex
  tasks are affected more than simple ones -- but it also reports a persistent
  lack of consistency across the literature, which is why this ships contested.
  Practical form: treat the CO2 number as a ventilation gauge, act on it by
  ventilating, and do not tell anyone that a specific ppm figure is making them
  stupid.
reasoning: >
  Zhang 2017 is the load-bearing source because of its design, not its size: it
  is the study that dissociates the marker from the mixture by adding pure CO2
  in one condition and letting bioeffluents accumulate in another. That
  dissociation is what makes the popular claim a measurement error rather than a
  finding -- CO2 is easy and cheap to measure, everything else a human body
  emits is not, so CO2 became the number, and the number then got treated as the
  cause. Fan 2023 is included as the strongest contrary evidence rather than
  suppressed: a systematic review and meta-analysis of fifteen studies, finding
  effects on complex cognitive tasks in the 1000-1500 and 1500-3000 ppm bands,
  and reporting that occupationally exposed populations are less affected than
  general ones. Two things keep this off the higher rungs. The literature it
  pools is small-n laboratory work with heterogeneous cognitive batteries, and
  the reviewers themselves characterise the results as disappointingly
  inconsistent. And the well-known office-worker study that put this claim into
  general circulation is not cited here at all: it manipulated ventilation and
  volatile organic compounds together with CO2, which is precisely the confound
  Zhang 2017 was built to break, so it cannot adjudicate the question it is
  usually quoted for.
refraction_notes:
  - note: >
      WHAT THE NUMBER IS FOR. A CO2 reading in a home is a proxy for how much
      of the air is re-breathed, which is a proxy for ventilation. That makes it
      genuinely useful as a prompt to open a window or run the ventilation unit.
      It does not make it a toxicology reading, and a consumer monitor's
      colour-coded warning is a design choice by the manufacturer, not a
      health threshold from any authority.
    grade: C
  - note: >
      REFUSED AND RECORDED: the claim that CO2 above roughly 1000 ppm measurably
      impairs decision-making in a home. The best-known support for it comes
      from office studies that varied ventilation, volatile organic compounds
      and CO2 together, so they cannot separate CO2 from what ventilation also
      removes. When the separation was done directly, pure CO2 did nothing at
      3000 ppm. Not carried.
    grade: D
  - note: >
      NOT SEARCHED IN THIS SPRINT: bedroom CO2 and sleep quality, which is the
      residential setting where the claim is most often applied and where the
      evidence base is separate from the office literature pooled above. Open.
    grade: D
---

# home/co2-ventilation-proxy-not-agent-005

Cheap CO2 monitors created a claim. The claim is that when the number goes over
about a thousand, your thinking degrades. It is worth understanding exactly what
is wrong with it, because the underlying instinct is right and only the causal
story is broken.

The experiment that settles it added pure carbon dioxide to a room in one
condition, and in another let people sit in the room until their own emissions
brought the CO2 to the same level. Pure CO2 at 3000 ppm did nothing measurable:
no effect on how the air was perceived, no effect on reported symptoms, no
effect on cognitive performance. The bioeffluent condition, at the same CO2
reading, degraded perceived air quality, increased headache, fatigue,
sleepiness and difficulty thinking clearly, and slowed performance on several
tasks.

Same number on the meter. Opposite result. What differed was everything else
that comes off a human body, which nobody measures because measuring it is hard
and measuring CO2 is trivial.

So carbon dioxide is a marker for how much of the air you are re-breathing. It
is a decent one. It is not, at these concentrations, demonstrated to be the
thing doing the damage.

The contrary evidence is real and is carried here rather than buried. A 2023
systematic review and meta-analysis over fifteen studies does find that complex
cognitive tasks decline at added CO2 in the 1000 to 3000 ppm range, that complex
tasks suffer more than simple ones, and that people habituated by occupational
exposure are affected less. That is a genuine finding from a genuine pooling
effort. It is also a pooling of small laboratory studies with different
cognitive batteries, and the reviewers describe the field's consistency as
disappointing in their own words. Hence the contested flag: this is an open
question, not a settled refutation.

What is not carried at all is the famous office-worker study that launched the
claim into public circulation. It changed ventilation, volatile organic
compounds and CO2 at the same time. That is exactly the confound the
pure-versus-bioeffluent experiment was designed to break, so it cannot answer
the question people quote it for.

The practical version survives all of this intact and is almost boringly simple.
If the reading climbs, the room is under-ventilated. Ventilate it. In a Korean
apartment that usually means the equipment described in item 004, which is
already installed. Just do not tell anyone a particular ppm figure is making
them stupid.

One gap worth naming: bedroom CO2 and sleep quality is the residential case
where this claim gets applied most often, it draws on a different literature
from the office studies pooled above, and it was not searched in this pass.
