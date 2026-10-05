---
# Collection sprint 2026-09-02 (mental-health lane expansion). The locale item.
# Everything else in this lane is WEIRD-sampled, and the single most
# consequential thing that does NOT transfer is the assumption that talking to
# someone is a normal, low-friction default. Korean nationwide survey data says
# prevalence is broadly comparable to other countries while service use is
# markedly low, and the 2011-to-2021 comparison shows stigma RISING and service
# use FALLING. The one Korea-specific item in this domain, and the one the rest
# of the lane must be read through when the user is Korean.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/kr-help-seeking-service-use-020
domain: mental-health
grade: "B (that Korean mental health service utilisation is low relative to prevalence, and that stigma rose while service use fell between the 2011 and 2021 national surveys); D (any use of a prevalence figure as an individual-level inference)"
lane: "@clinical"
locale: KR
as_of: 2021-2026
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/36990670/"  # Rim SJ, Hahm BJ, Seong SJ, Park JE, Chang SM, Kim BS, An H, Jeon HJ, Hong JP, Park S. 2023, Psychiatry Investig 20(3):262-272, doi 10.30773/pi.2022.0307, PMCID PMC10064208 -- National Mental Health Survey of Korea 2021, 13530 households approached, 5511 completed interviews, response rate 40.7 percent, Korean version of the Composite International Diagnostic Interview 2.1
  - "https://pubmed.ncbi.nlm.nih.gov/42155352/"  # Kang B, Hahm BJ, Seong SJ, Seo HY, Kim BS, Chang SM, Hong JP, Kim HJ, Park D, Lee H, Kwak JH, Ryu H, Kim J, Park JE. 2026, Psychiatry Res 363:117226, doi 10.1016/j.psychres.2026.117226 -- comparison of the Korean Epidemiologic Catchment Area study 2011 (n=6022) with the National Mental Health Survey of Korea 2021 (n=5511), stigma measured with the Perceived Devaluation-Discrimination scale
  - "mental-health/workload-detachment-recovery-016"  # the within-study regional divergence on long working hours and depressive symptoms, which is the other Korea-relevant finding in this lane
  - "mental-health/screening-score-is-not-a-diagnosis-011"  # why these interview-based figures are NOT interchangeable with questionnaire-based prevalence estimates, and are lower for exactly that reason
  - "finance-investing/kr-tax-regime-staleness-gate-016"  # the warehouse's existing pattern for a jurisdiction-bound item that needs an edition check, not just a source check
refraction_notes:
  - note: >
      The prevalence figures, stated exactly and with their instrument. In the
      National Mental Health Survey of Korea 2021 (5511 completed interviews from
      13530 households, response rate 40.7 percent, diagnoses made with the Korean
      version of the Composite International Diagnostic Interview 2.1), the
      LIFETIME prevalence of mental disorders was 27.8 percent. The 12-month
      prevalence rates were 2.6 percent for alcohol use disorder, 2.7 percent for
      nicotine use disorder, 1.7 percent for depressive disorder and 3.1 percent
      for anxiety disorder.
    grade: B
  - note: >
      Note WHY those 12-month figures look low next to numbers commonly quoted
      elsewhere: they come from a structured DIAGNOSTIC INTERVIEW, not from a
      questionnaire cut-off. This domain's item 011 records that pooled prevalence
      runs at about 31 percent from screening tools versus about 17 percent from
      diagnostic interviews. Comparing an interview-based Korean figure against a
      questionnaire-based figure from anywhere else is not a cross-country
      comparison; it is an instrument comparison wearing a flag.
    grade: A
  - note: >
      The utilisation figures, which are the point of the item. Among those with a
      12-month diagnosis, 12-month treatment and service utilisation rates were
      2.6 percent for alcohol use disorder, 1.1 percent for nicotine use disorder,
      28.2 percent for depressive disorder and 9.1 percent for anxiety disorder.
      The authors' own conclusion is that the treatment rates were substantially
      low.
    grade: B
  - note: >
      The decade comparison, and it moves the wrong way. Comparing the Korean
      Epidemiologic Catchment Area study 2011 (n=6022) with the 2021 survey
      (n=5511) using the Perceived Devaluation-Discrimination scale, stigma was
      higher among older individuals and INCREASED ACROSS ALL AGE GROUPS between
      2011 and 2021, while mental health service use DECLINED OVERALL except among
      younger adults. The stigma-to-service-use association differed by age: it
      was present among middle-aged and older adults in 2011 and persisted only
      among middle-aged adults in 2021, with no significant association among
      younger adults in either year.
    grade: B
  - note: >
      The framing that must NOT be adopted. The 2026 comparison paper's own
      premise is that the prevalence of mental disorders in Korea is COMPARABLE to
      that in other countries while service use remains markedly low. So the
      Korean difference this item records is a HELP-SEEKING difference, not a
      prevalence difference. Any framing that treats Korea as unusually afflicted
      is not what these sources say and must not be constructed from them.
    grade: A
  - note: >
      Two sampling caveats. The 2021 survey's response rate was 40.7 percent,
      which is low enough that non-response bias in either direction cannot be
      excluded. And these are nationally representative population figures, so they
      say nothing whatsoever about any individual -- a base rate is not a personal
      probability, and this domain's own group-to-individual item (012) is the
      reason.
    grade: A
  - note: >
      The operative consequence, and it is about tone rather than content. Most of
      what this lane holds is WEIRD-sampled, including the unstated background
      assumption that suggesting someone talk to a professional is a light,
      ordinary, low-cost suggestion. In this locale that assumption is measurably
      wrong: the great majority of people with a diagnosable condition did not use
      any service, stigma rose over the last decade rather than falling, and it
      bears hardest on working-age adults. Reading a person's non-use of services
      as evidence that nothing is wrong is a straightforward misreading of the base
      rate; treating a suggestion to seek help as costless is a second one.
    grade: B
  - note: >
      STALENESS GATE, on the same discipline the warehouse applies to
      jurisdiction-bound figures elsewhere. These are the 2021 survey's numbers,
      published 2023, with the decade comparison published 2026. The Korean
      national survey runs on a multi-year cycle, so any figure here must be
      re-checked against the most recent edition before it is quoted, and a
      pre-2021 Korean figure recited from memory is a prior edition rather than a
      current one.
    grade: A
claim: >
  In Korea, mental health service use is low relative to prevalence, and the gap
  widened over the last decade. The National Mental Health Survey of Korea 2021
  (Rim et al. 2023, Psychiatry Investigation; 5511 completed interviews from 13530
  households, response rate 40.7 percent, diagnoses via the Korean Composite
  International Diagnostic Interview 2.1) found lifetime prevalence of mental
  disorders at 27.8 percent, and 12-month prevalence of 2.6 percent for alcohol
  use disorder, 2.7 percent nicotine use disorder, 1.7 percent depressive disorder
  and 3.1 percent anxiety disorder. Among those with a 12-month diagnosis, 12-month
  treatment and service utilisation was 2.6 percent (alcohol use disorder), 1.1
  percent (nicotine use disorder), 28.2 percent (depressive disorder) and 9.1
  percent (anxiety disorder); the authors conclude treatment rates were
  substantially low. Comparing the 2011 Korean Epidemiologic Catchment Area study
  (n=6022) with the 2021 survey, Kang et al. 2026 (Psychiatry Research) found
  stigma measured on the Perceived Devaluation-Discrimination scale INCREASED
  across all age groups while service use DECLINED overall except among younger
  adults, with the stigma-to-service-use association persisting in 2021 only among
  middle-aged adults. Their stated premise is that Korean prevalence is COMPARABLE
  to other countries while service use is markedly low -- so this is a help-seeking
  difference, not a prevalence difference, and no framing of Korea as unusually
  afflicted may be built from these sources. Two caveats: the 40.7 percent
  response rate leaves non-response bias open, and these are population base rates
  that say nothing about any individual. The operative consequence is about tone:
  the WEIRD-sampled background assumption that suggesting professional help is a
  light, ordinary suggestion is measurably wrong in this locale, non-use of
  services cannot be read as evidence that nothing is wrong, and these figures
  carry a staleness gate against the next survey edition.
reasoning: >
  Every other item in this lane was estimated on predominantly Western samples,
  and the thing that transfers worst is not an effect size but an unstated social
  assumption: that talking to someone about this is normal, cheap and easy. This
  item exists to make that assumption checkable in the locale that matters here.
  Two Korean nationwide sources were used together because they answer different
  halves. Rim et al. 2023 supplies the current levels, and crucially supplies them
  from a structured diagnostic interview rather than a questionnaire cut-off,
  which is what makes them comparable to the interview-based international figures
  and NOT comparable to the inflated questionnaire-based ones that this domain's
  item 011 already documents. Kang et al. 2026 supplies the direction of travel by
  putting the 2011 and 2021 surveys side by side on the same stigma instrument,
  and its finding is the uncomfortable one: stigma up across every age group,
  service use down overall. The item deliberately refuses the framing that a
  Korea-specific mental-health item most easily slides into. Neither source says
  Korea is unusually afflicted; the 2026 paper's own premise is the opposite, that
  prevalence is comparable and service use is not, and a warehouse that let a
  help-seeking finding become a prevalence claim would be committing the exact
  laundering it exists to prevent. Graded at the trial band for the survey
  findings, which are nationally representative interview-based data, and at the
  practitioner floor for any individual-level reading, since a base rate is not a
  personal probability. The staleness gate is carried because the warehouse
  already learned this lesson on Korean reference intakes: a jurisdiction-bound
  figure can be correct and obsolete at the same time, and needs an edition check
  rather than merely a source check. Not flagged contested: the two sources are
  consistent with each other and the second is by an overlapping author group
  working from the same national survey programme.
---

# mental-health/kr-help-seeking-service-use-020

Almost everything else in this lane was measured on Western samples, and the
thing that travels worst is not a number. It is an assumption nobody writes down:
that suggesting someone talk to a professional is a light, ordinary, low-cost
thing to say.

Here is what the Korean national survey data says about that.

In the 2021 national survey -- five and a half thousand completed interviews,
diagnoses made with a structured clinical interview rather than a questionnaire --
lifetime prevalence of mental disorders was 27.8 percent. Over the preceding
twelve months, 1.7 percent met criteria for a depressive disorder and 3.1 percent
for an anxiety disorder.

Those twelve-month figures look low compared with numbers people are used to
seeing, and there is a specific reason. They come from a diagnostic interview.
This warehouse separately documents that pooled prevalence runs at roughly 31
percent when it is built from screening questionnaires and roughly 17 percent
when it is built from interviews. Setting an interview-based Korean number
against a questionnaire-based number from somewhere else is not a comparison
between countries. It is a comparison between instruments with a flag attached.

Now the part that matters.

Among people who met criteria for a disorder in the past twelve months, the share
who used any mental health service in that period was 28.2 percent for depressive
disorder, 9.1 percent for anxiety disorder, 2.6 percent for alcohol use disorder
and 1.1 percent for nicotine use disorder. The survey's own authors describe the
treatment rates as substantially low.

And the trend goes the wrong way. Putting the 2011 and 2021 national surveys side
by side on the same stigma measure: perceived stigma increased across every age
group over that decade, and service use declined overall -- with younger adults
the one exception. The link between stigma and not using services was present in
middle-aged and older adults in 2011 and, by 2021, persisted specifically among
middle-aged adults. Working-age people carrying the most social role are where it
bites hardest.

One framing has to be refused explicitly, because it is the one this data most
easily slides into. Neither source says Korea is unusually afflicted. The 2026
comparison paper opens by stating the opposite: that prevalence in Korea is
comparable to other countries, and that what is unusual is how little of it
reaches a service. This is a help-seeking finding. Turning it into a prevalence
claim would be a fabrication.

Two limits. The 2021 survey had a response rate of about 41 percent, so who
declined and why is unknown, in either direction. And these are national base
rates. They describe a population and say nothing at all about any particular
person -- which is the whole content of this warehouse's item on group-to-
individual transfer, and it applies here as sharply as anywhere.

What actually changes, then, is tone rather than content. In this locale, most
people who meet criteria for something never use a service, the stigma behind
that got stronger over the last ten years, and it presses hardest on exactly the
working-age adults whose calendars a system like this one is looking at. Reading
somebody's non-use of services as evidence that nothing is going on is a
misreading of the base rate. Offering the suggestion as though it costs nothing
is a second one.

Finally, an expiry note. These are the 2021 survey's figures. The national survey
runs on a cycle, so any number here has to be re-checked against the most recent
edition before it is repeated, and any Korean figure recalled from memory is
almost certainly from a prior one. This warehouse has already been caught out
once by a jurisdiction-bound figure that was correct and obsolete at the same
time.
