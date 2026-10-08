---
# Authored 2026-09-02 (cooking-lane collection sprint). @food-safety, universal.
# The highest-value correction available for a Korean kitchen: the habit of
# re-boiling a pot of 국/찌개 across days, and of leaving cooked rice out, both
# rest on the assumption that heat resets a food's safety state. Two primary
# sources say it does not. Shipped as the mechanism item that the KR
# core-temperature item's 74C reheat figure must be read against.
id: cooking/reheating-not-a-reset-007
domain: cooking
lane: "@food-safety"
grade: B
locale: universal
as_of: 2023
contested: no
sources:
  - "https://doi.org/10.3390/foods12030626"  # Navaneethan Y, Effarizah ME. Post-Cooking Growth and Survival of Bacillus cereus Spores in Rice and Their Enzymatic Activities Leading to Food Spoilage Potential. Foods 2023;12(3):626. PMC9914848. Eight B. cereus strains, spore survival through boiling rice 15 min, then storage at 4C / 25C / 30C
  - "https://doi.org/10.1111/j.1472-765X.2008.02350.x"  # Rajkovic A, Uyttendaele M, Vermeulen A, et al. Heat resistance of Bacillus cereus emetic toxin, cereulide. Letters in Applied Microbiology 2008;46(5):536-541. Cereulide heated at 100C, 121C and 150C across alkaline pH 8.6-10.6
  - "source:cooking/kr-core-temperatures-005 -- the Korean regulator's 74C reheat figure, which this item bounds: 74C is a vegetative-cell rule, not a spore or toxin rule"
  - "source:cooking/kr-cold-chain-band-006 -- the control that actually works here is the cold side, and Korea's legal cold band is warmer than the 4C at which the rice study saw zero growth"
refraction_notes:
  - note: >
      THE 74C REHEAT FIGURE IS NOT WRONG, IT IS NARROW. Reaching 74C in reheated
      food kills vegetative pathogens and is the right instruction. It does not
      inactivate bacterial spores, and it does not touch a preformed heat-stable
      toxin at all. So "I boiled it again" is a valid answer to one hazard and no
      answer to another. Never let a reheating instruction be spoken as if it
      restored a food to its post-cooking state.
    grade: A
  - note: >
      WHAT THE COLD RESULT DOES AND DOES NOT LICENSE. In the rice study, no
      viable B. cereus was detected at 4C at any sampling point out to seven
      days, while four of eight strains grew at 30C and three at 25C. That is a
      strong practical signal that prompt refrigeration is the control. It is
      also ONE study, EIGHT strains, in ONE matrix (cooked rice), and it must not
      be generalised into "refrigeration makes food safe" or extended to stews,
      banchan or any other matrix without its own evidence.
    grade: C
  - note: >
      THE TOXIN RESULT WAS TESTED UNDER ALKALINE CONDITIONS AND SOME ACTIVITY
      LOSS WAS REVERSIBLE. Rajkovic tested cereulide at 100C, 121C and 150C
      across pH 8.6-10.6, and reported that removing the alkaline buffer after
      heating recovered toxic activity. Read the finding as "no heat treatment
      used in the food industry inactivates it", which is what the authors
      concluded, and do NOT quote a specific time-at-temperature destruction
      figure from it, because none was established.
    grade: B
  - note: >
      NO KOREAN-DISH EVIDENCE WAS LOCATED. The mechanism is general, but nothing
      in this pass measured spore survival or toxin formation in 국, 찌개,
      볶음밥, 김밥 or banchan specifically, and no Korean outbreak dataset was
      read. The reasoning below extends a rice-and-model-system finding to a
      Korean reheating habit by MECHANISM, and says so. It is not a measured
      Korean result and must not be spoken as one.
    grade: D
claim: >
  Reheating does not return a food to its post-cooking safety state, because two
  of the three things that can go wrong are not heat-reversible. Bacillus cereus
  spores survive normal cooking: four of eight strains remained viable in rice
  after boiling for 15 minutes, and on subsequent storage four strains grew at
  30C (reaching 3.78-5.44 log CFU/g within 24 h, with growth detectable as early
  as 6 h) and three grew at 25C (3.32-4.92 log CFU/g by 48 h), while at 4C no
  viable B. cereus was detected at any point up to seven days. The emetic toxin
  those organisms produce, cereulide, is heat-stable: tested at 100C, 121C and
  150C across alkaline pH 8.6-10.6, its heat stability was described as
  remarkable at all temperatures tested, with the authors concluding that no heat
  treatment used in the food industry can inactivate it and that safety must rest
  on prevention and cold-chain maintenance. The operative control is therefore
  the speed with which cooked food gets cold, not the temperature it is brought
  back to.
reasoning: >
  Both halves rest on directly retrieved primary publications rather than on
  secondary write-ups, and both report their numbers plainly, which is why the
  item ships in the solid band rather than lower. It does not reach the top band
  because the substantive half of the practical advice rests on a single
  eight-strain study in a single food matrix, and because the leap from that
  study to a pot of stew reheated across three days is a mechanistic inference
  rather than a measured result. The item earns its slot on consequence: a live
  cooking consumer will be asked "is this still fine, I boiled it again" more
  often than almost any other safety question, and the intuition behind the
  question is wrong in a way that the regulator's own 74C reheating figure can
  accidentally reinforce. Stating the bound on that figure is most of the value
  here. The asymmetry to preserve when speaking it: the cold finding is the part
  that is actionable and the part that is thinnest, so it should be spoken as
  "get it cold fast" rather than as a guarantee that cold food is safe food.
---

# cooking/reheating-not-a-reset-007

The most common safety question in a real kitchen is some version of "it has
been sitting out, but I am going to heat it again, so it is fine". The
assumption underneath is that heat resets the food. For one hazard it does. For
two others it does not, and those two are exactly the ones a Korean kitchen
runs into: cooked rice left out, and a pot of soup or stew reheated across
several days.

Bacillus cereus forms spores, and spores survive cooking. In a study of eight
strains, four still had viable spore counts in rice after fifteen minutes of
boiling. What happened next depended entirely on storage temperature. Held at
30C, four strains grew, reaching 3.78 to 5.44 log CFU per gram within 24 hours,
with the fastest showing growth after as little as six. At 25C, three strains
grew, reaching 3.32 to 4.92 log by 48 hours. At 4C, no viable Bacillus cereus
was detected at any sampling point out to seven days.

The toxin is the harder half. Cereulide, the emetic toxin these organisms
produce, was heated at 100C, 121C and 150C across a range of alkaline pH values.
Its heat stability was remarkable at every temperature tested, and where activity
appeared to be lost, removing the alkaline buffer brought it back. The authors'
conclusion is the sentence that matters: no heat treatment used in the food
industry inactivates it, so safety has to rely on prevention and on maintaining
the cold chain.

Put those together and the reheating instruction gets a boundary. Bringing
leftovers to 74C, which is what the Korean regulator advises, kills vegetative
pathogens and is worth doing. It does not kill spores. It does nothing at all to
a toxin that was already made while the food sat warm. So the boiling is not the
control. The control is how fast the food got cold in the first place.

Two limits are worth carrying honestly. The reassuring result -- nothing grew at
4C for a week -- is the thinnest part of the evidence: one study, eight strains,
rice only. It should be spoken as a reason to refrigerate promptly, not as a
promise that a cold fridge makes food safe. And nothing here was measured in a
Korean dish. The habit this item is aimed at, the pot of 찌개 that lives on the
stove between meals, is reached by mechanism, not by data.
