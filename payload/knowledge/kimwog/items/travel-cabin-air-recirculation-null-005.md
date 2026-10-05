---
# Authored 2026-09-02 (travel-lane opening sprint). @travel-clinical (VC-A).
# A folklore refutation with an unusually good source, and a funding disclosure
# that has to be stated because the warehouse has a standing rule about it. The
# recirculated-air claim is refuted by a natural experiment that nobody funded
# from inside the industry; the proximity finding comes from a study part-funded
# by an aircraft manufacturer and with a manufacturer employee as a co-author,
# and that is carried on the face of the item rather than in a footnote.
id: travel/cabin-air-recirculation-null-005
domain: travel
lane: "@travel-clinical"
grade: B (recirculated cabin air was not associated with more post-flight colds); C (the proximity-limited transmission model)
locale: universal
as_of: 2002-2018
contested: yes
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/12132979/"  # Zitter JN, Mazonson PD, Miller DP, Hulley SB, Balmes JR. 2002, JAMA 288(4):483-486, doi 10.1001/jama.288.4.483 -- natural experiment, 1100 passengers, San Francisco Bay area to Denver, January-April 1999. Abstract read verbatim 2026-09-02
  - "https://pubmed.ncbi.nlm.nih.gov/29555754/"  # Hertzberg VS, Weiss H, Elon L, Si W, Norris SL; FlyHealthy Research Team. 2018, Proc Natl Acad Sci U S A 115(14):3623-3627, doi 10.1073/pnas.1711611115, PMCID PMC5889623 -- observational behaviour study plus simulation, 10 transcontinental US flights, 229 environmental samples. Abstract read verbatim 2026-09-02
  - "source:exercise/funding-coi-check-004 -- the warehouse's standing rule on industry funding, applied here to the PNAS study"
  - "source:relationships-communication/source-misattribution-rule-005 -- the folklore in this entry survives by being attributed to nothing in particular"
  - "framework:observational + simulation -- the 2002 study is a natural experiment on aircraft types, not a randomized trial, with self-reported symptoms by telephone follow-up. The 2018 study is a behavioural observation feeding a transmission SIMULATION; its transmission-probability output is modelled, not measured. Neither is a controlled infection experiment and neither should be quoted as one."
refraction_notes:
  - note: >
      THE RECIRCULATION CLAIM WAS TESTED DIRECTLY AND DID NOT SURVIVE. In 1999,
      some aircraft on the same route used 100 percent fresh air and others
      recirculated roughly half the cabin air, which made a natural experiment
      possible. Among 1100 passengers, 47 percent on fresh-air aircraft and 53
      percent on recirculating aircraft, the rates of reporting a cold were 19
      versus 21 percent (P = 0.34), runny nose plus cold 10 versus 11 percent
      (P = 0.70), and an aggregate of 8 upper-respiratory symptoms 3 percent in
      BOTH groups (P greater than 0.99). Results were similar after adjustment for
      confounders. The authors conclude they found no evidence that recirculation
      increases risk.
    grade: B
  - note: >
      THE STUDY DESIGN IS THE REASON THIS IS WORTH SHIPPING, AND ALSO ITS LIMIT.
      A natural experiment on aircraft type is a much stronger design for this
      question than a survey, because passengers did not choose their ventilation
      system. It is still observational, the outcome is self-reported symptoms at a
      5-to-7-day telephone follow-up rather than a confirmed infection, and it is a
      single route in a single season in 1999. Fleet ventilation has changed since.
      What it refutes is the specific mechanism claim; it does not certify that
      flying carries no respiratory risk at all.
    grade: C
  - note: >
      WHERE THE RISK ACTUALLY SITS, PER THE SECOND SOURCE. Chronicling passenger
      and crew movement on 10 transcontinental flights and simulating droplet
      transmission from those data, the study concludes there is low probability of
      direct transmission to passengers not seated in close proximity to an
      infectious passenger. Proximity, not ventilation. That reframes the practical
      question from what the aeroplane does to who is sitting next to you.
    grade: C
  - note: >
      THE PATHOGEN BURDEN MEASUREMENT IS THE UNDERRATED PART. The team collected
      229 environmental samples during the flights and ran qPCR for 18 common
      respiratory viruses. Every assay was negative, and eight of the flights were
      during influenza season. That is a direct measurement rather than a model
      output, and it sits badly with the idea of a cabin as a reservoir. It is also
      10 flights, so it is a small direct measurement.
    grade: C
  - note: >
      FUNDING DISCLOSED ON THE FACE OF THE ITEM. The 2018 paper's own conflict
      statement records that the authors received support from The Boeing Company
      by way of a subcontract to the Georgia Institute of Technology, and that one
      co-author is a Boeing employee. The finding is favourable to aircraft
      manufacturers. This warehouse has a standing rule that industry funding is
      checked and stated rather than discovered later, so it is stated: the
      proximity result is graded a band below the 2002 null partly for design and
      partly for this. Note the asymmetry that makes the pairing work -- the 2002
      natural experiment carries no such tie and is the one doing the refuting.
    grade: B
  - note: >
      NOT COVERED, AND ONE ERA CAVEAT THAT MATTERS. Neither source addresses
      airborne (as opposed to droplet) transmission, masking, HEPA filter
      performance as such, tuberculosis or measles on aircraft, or anything from
      the COVID-19 period. The 2018 study models DROPLET-mediated disease
      explicitly. Do not extend either paper to a pathogen or a transmission route
      it did not study, and in particular do not read the 2002 null as a general
      statement about respiratory infection on aircraft in 2026.
    grade: D
claim: >
  The belief that recirculated cabin air spreads infection was tested directly and
  was not supported. In 1999, when some aircraft on the San Francisco-to-Denver
  route used 100 percent fresh air and others recirculated about half the cabin
  air, a natural experiment among 1100 passengers found essentially identical
  post-flight upper-respiratory symptoms: colds reported by 19 versus 21 percent
  (P = 0.34), runny nose with cold 10 versus 11 percent (P = 0.70), and an
  aggregate of eight symptoms 3 percent in both groups (P greater than 0.99), with
  similar results after adjustment. Separately, a study that chronicled passenger
  and crew movement on 10 transcontinental flights and simulated droplet
  transmission from those observations concluded there is low probability of direct
  transmission to passengers not seated in close proximity to an infectious
  passenger; that team also collected 229 environmental samples during the flights
  and every qPCR assay for 18 common respiratory viruses was negative, on eight
  flights during influenza season. The second study was part-funded by an aircraft
  manufacturer and includes a manufacturer employee as a co-author. The operative
  reading: the ventilation system is the wrong thing to worry about, proximity is
  the plausible route, and neither source covers airborne transmission or anything
  after 2018.
reasoning: >
  This is the lane's clearest folklore entry, and it is unusual in that the
  folklore was tested against a genuine natural experiment rather than argued
  about. Zitter et al. 2002 (JAMA 288(4):483-486) exploited a fleet transition:
  on the same route, in the same season, some aircraft recirculated air and some
  did not, and passengers had no say in which they boarded. That removes the
  self-selection that ruins survey approaches to this question, and the result is a
  clean null across three different symptom definitions with a further adjustment
  producing nothing. It is graded in the solid band rather than the top band
  because the outcome is a self-reported symptom at telephone follow-up rather than
  a laboratory-confirmed infection, and because it is one route in one season a
  quarter of a century ago. Hertzberg et al. 2018 (PNAS 115(14):3623-3627) supplies
  the positive account that should replace the discarded one, and it is graded a
  band lower for two independent reasons that are both stated on the item rather
  than buried. Its transmission conclusion is a SIMULATION built on observed
  movement data, not a measurement of anyone catching anything. And its funding
  runs to an aircraft manufacturer, with a manufacturer employee among the
  authors, on a question where the manufacturer has an interest in the answer --
  the warehouse has a standing rule about checking this and it applies without
  exception, including when the finding is plausible. The environmental sampling is
  the sturdiest part of that paper because it is a direct measurement rather than a
  model, though 229 samples across 10 flights is a small direct measurement. The
  pairing is what makes the item work: the refutation rests on the independently
  funded natural experiment, and the industry-linked paper is used only for the
  replacement mental model, which is exactly the weight each deserves. Contested is
  set because a very widely held belief is being contradicted, not because the
  sources conflict. The era caveat is deliberate and load-bearing: neither paper
  speaks to airborne transmission or to anything learned since 2018, and it would
  be a serious misuse of this item to read it as a general clearance for
  respiratory risk on aircraft today.
---

# travel/cabin-air-recirculation-null-005

The idea that aeroplanes make you sick because they recirculate the air has been
tested about as well as such a thing can be, and it did not hold up.

In 1999 the fleet flying between the San Francisco Bay area and Denver was mixed:
some aircraft ventilated with entirely fresh air, others recirculated roughly half
the cabin air. Passengers did not choose which. Researchers surveyed 1,100 of
them at the gate and rang them back a week later.

Nineteen percent of the fresh-air passengers reported a cold. Twenty-one percent
of the recirculated-air passengers did. Runny nose with a cold: ten percent
against eleven. A stricter aggregate of eight upper-respiratory symptoms: three
percent in both groups, exactly. Adjusting for confounders changed nothing.

That is a real test of a specific mechanism, and the mechanism failed it.

So what does explain the occasional flight where someone clearly catches
something? The most careful work on that question watched how people actually
move in an economy cabin across ten transcontinental flights and simulated droplet
spread from those observations. Its conclusion was that transmission to passengers
not seated close to an infectious person is unlikely. The variable is proximity --
who is within a couple of rows of you -- not the ventilation architecture.

The same team also did something more direct and less quotable: they took 229
environmental samples during those flights and tested them for eighteen common
respiratory viruses. Every test was negative. Eight of the ten flights were during
influenza season.

Two honesty notes, because this item is being used to overturn a widespread
belief and it should be able to take scrutiny.

The proximity study was part-funded by an aircraft manufacturer, and one of its
authors works there. The finding is convenient for that manufacturer. That does
not make it wrong, and the environmental sampling in particular is a measurement
rather than an opinion, but it is why the refutation above leans on the 1999
natural experiment -- which has no such tie -- and uses the newer paper only for
the replacement picture.

And both papers have edges. The 1999 study measured self-reported symptoms on one
route in one season with a fleet that no longer exists. The 2018 study modelled
droplet transmission specifically. Neither speaks to airborne spread, to masking,
or to anything the world learned after 2018. Reading this entry as "flying is
respiratory-safe" would be a bigger error than the belief it replaces. What it
says is narrower and firmer: the recirculation story is wrong, and the thing worth
thinking about is who is sitting near you.
