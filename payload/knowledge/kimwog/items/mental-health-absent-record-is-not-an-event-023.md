---
# CRAFT LANE OPENING 2026-09-02 (marker: mh-craft-lane-021-028). The item with a
# live incident behind it. On 2026-08-28 an automated routine check in this
# estate computed a completion rate over a table it shares with another agent,
# produced a figure that was the near-opposite of the truth, and the number was
# relayed to the owner three times without a check. The owner corrected it from
# memory. The engineering defect is being fixed in its own ticket; what is
# recorded HERE is the conduct half, which no code fix removes: an absence in a
# record was spoken as a fact about a person, in the second person.
# Rubric: mental-health @assistant-craft (VC-E).
id: mental-health/absent-record-is-not-an-event-023
domain: mental-health
grade: "D (the craft rules, which rest on operational practice and one documented incident in one estate); C (the general fact that gaps in behavioural records arise for behavioural and mechanical reasons and are therefore not random, which is established on item 013)"
lane: "@assistant-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "incident:2026-08-28 03:40, this estate. An automated routine-completion check emitted rate=0.0 and consec_miss=4 for a training block series that was in fact 8 done and 1 abandoned across 9 scheduled instances over 11 days (true completion 0.89, true consecutive misses 0, most recent instance completed the previous day). The figure was relayed to the owner three times without being checked against the underlying rows. The owner rejected it from memory and was right. Root cause established 2026-09-02: the completion query ran over a store shared with a second agent and carried no owner condition, so it aggregated another agent's rows; the final step from 0.89 to 0.0 remains unexplained. Ticket held separately."
  - "mental-health/passive-sensing-hypothesis-generating-013"  # missing data in behavioural streams goes missing for behavioural reasons; the gaps are not random
  - "mental-health/screening-score-is-not-a-diagnosis-011"  # a derived number about a person is a measurement with error, never a statement about them
  - "mental-health/craft-verification-ceiling-021"  # the lane's ceiling and admission test
  - "framework:VC-E. One estate, one incident, no controlled comparison. The incident establishes that this failure mode occurs and what it cost; it does not establish that the rules below prevent it. They are the corrections adopted afterwards, not a tested intervention."
refraction_notes:
  - note: >
      THE THREE STATES. A record about a person's behaviour has three states, not
      two: recorded-and-happened, recorded-and-did-not-happen, and NO RECORD.
      Systems collapse the third into the second because a boolean field has only
      two slots and a null has to go somewhere. The collapse is silent, it happens
      at the storage layer rather than at the reasoning layer, and by the time a
      sentence is being written the third state has already been destroyed. This
      is a structural defect, not an occasional bug, and it must be assumed
      present in any completion field that was not explicitly designed against it.
    grade: D
  - note: >
      ABSENCE HAS ITS OWN CAUSES AND THEY ARE NOT RANDOM. Item 013's reviewers
      establish this for sensor data specifically: a stream goes missing because
      the device was off, flat, left at home, or no longer carried, and each of
      those is itself a behaviour possibly related to the thing being measured.
      The mechanical causes are worse still because they are invisible from
      inside: a sync that failed, an agent that was not running, a routine that
      was retired, a schema that changed, or -- as in the incident behind this
      item -- rows that belong to a different owner in a shared store. None of
      these produce a marker saying "this gap is mine".
    grade: C
  - note: >
      THE ACCUSATION ASYMMETRY, which is the rule that actually governs the
      threshold. A false positive here is not a wrong number. It is an accusation,
      made by a system, to a person who cannot cross-examine it, about their own
      conduct in an area where they are already likely to take it personally. A
      missed true positive costs a delayed mention. These are not comparable
      costs, and the threshold must be set as if they are not. Silence is cheap
      here in a way it is not in most of engineering.
    grade: D
  - note: >
      WHEN CORRECTED, THE CORRECTION IS THE FINDING. The failure in the incident
      was not that a query was wrong; queries are wrong all the time. It was that
      a number about a person was passed to that person three times without once
      being checked against the rows beneath it, and it took the person's own
      memory to stop it. The move after a correction is to check and report what
      was actually there, not to explain how the metric works. Explaining the
      metric to someone you have just accused wrongly is defending the instrument
      at their expense.
    grade: D
claim: >
  A missing record is a fact about the record, never a fact about the person. Any
  store of human behaviour has three states -- recorded-and-happened,
  recorded-and-did-not-happen, and no record -- and systems collapse the third
  into the second because a boolean has two slots. Absence has its own causes and
  they are not random: item 013 establishes for sensor streams that data goes
  missing for reasons that are themselves behavioural, and the mechanical causes
  are worse because they are invisible from inside the system (failed sync, agent
  not running, retired routine, schema change, rows owned by a different agent in
  a shared store). Five operative rules. (1) An absence is reported as a property
  of the record: "I have no record of X", never "you did not do X". (2) The
  recording path is verified before an absence is spoken at all; an absence whose
  path cannot be verified is not speakable. (3) A derived number about a person's
  behaviour is never relayed on first sight -- it is checked against the
  underlying rows first. (4) The threshold is set on the accusation asymmetry: a
  false positive is an accusation levelled by a system the person cannot
  cross-examine, a missed true positive is a delayed mention, and these costs are
  not comparable. (5) When corrected, the correction is the finding; report what
  was actually there rather than explaining how the metric works.
reasoning: >
  This item exists because the failure happened, in this estate, to this owner,
  and it is the clearest available demonstration that the conduct problem is not
  downstream of the engineering problem. The query defect has an owner and a
  ticket. The conduct defect does not disappear when the query is fixed, because
  the conduct defect was relaying a number about a person to that person, three
  times, without looking underneath it. Placed in the mental-health craft lane
  rather than filed only as an engineering ticket for a specific reason: the
  content of the false statement was about the person's own follow-through, which
  is precisely the class of statement item 011 refuses to let a tracked signal
  make, and the harm was of the kind that lane exists to prevent rather than the
  kind a bug tracker measures. Graded at the practitioner floor for the rules,
  which are corrections adopted after one incident and have not been tested
  against any alternative, and at the observational band for the underlying fact
  that gaps in behavioural records are non-random, which item 013's reviewers
  establish for sensor data and which generalises straightforwardly to any
  self-maintained or agent-maintained stream. Not flagged contested. The incident
  is recorded with its numbers and its unresolved residue rather than tidied,
  because a craft item whose basis is a failure should carry the failure at full
  size, including the part that is still not explained.
---

# mental-health/absent-record-is-not-an-event-023

At 03:40 on a Friday in August, an automated check in this estate reported that
a training commitment had been missed four times in a row and that its
completion rate was zero.

The truth was nine scheduled sessions over eleven days, of which eight were
completed and one was abandoned. Completion was eighty-nine per cent.
Consecutive misses were zero. The most recent session had been completed the
previous day, and the training log confirmed it independently: two hours and
twelve minutes.

The number was relayed to the owner three times before anyone checked. It
stopped because the owner said, from memory, that he had trained the day before.
He was right.

The cause turned out to be mundane and is being fixed elsewhere: the completion
query ran against a store shared with a second agent and carried no condition
restricting it to its own rows, so it counted somebody else's schedule. The last
step of the arithmetic, from eighty-nine per cent to zero, is still not fully
explained.

None of that is the reason this is in a knowledge warehouse.

The reason is that a system told a person, in the second person, that they had
missed something four times, on the basis of an absence in a record it had not
looked at. Fixing the query removes this particular wrong number. It does not
remove the move that made it harmful.

**A record about behaviour has three states, not two.** Recorded and happened.
Recorded and did not happen. And no record. The third collapses into the second
almost everywhere, because a completion field is a boolean and a null has to go
somewhere, and the collapse happens down at the storage layer where nobody is
thinking about what a sentence will later assert. By the time the sentence is
written, the distinction is already gone.

**Absence has its own causes, and they are not random.** The evidence lane
establishes this for sensor streams: data goes missing because a device was off,
or flat, or left at home, or no longer being carried -- and every one of those is
itself a behaviour that may be connected to whatever was being measured. So
dropping the gaps is never a neutral choice.

The mechanical causes are worse, because they are invisible from inside. A sync
that failed. A process that was not running that night. A routine that was
retired months ago and still has rows. A schema that changed. Rows belonging to
somebody else entirely in a store that two systems share. Not one of these
leaves a marker saying "this gap is mine, not the person's."

Five rules follow, and they are cheap.

**An absence is a property of the record.** "I don't have a record of Tuesday" is
true and checkable. "You skipped Tuesday" is a claim about a person built from
the absence of a row. The first invites a correction. The second requires one.

**Verify the recording path before speaking the absence at all.** Did the thing
that writes these rows run? Is it writing to the place being read? Is the read
scoped to the right owner? If those cannot be answered, the absence is not
speakable yet. This is a small amount of work and it is the entire fix for the
incident above.

**Never relay a derived number about a person on first sight.** A rate, a
streak, a count of misses -- these are all computed, and computed things about
people get checked against the rows before they get spoken. The failure in
August was not that the query was wrong. Queries are wrong routinely. It was
that the number went to the person it was about, three times, without anyone
looking underneath it.

**Set the threshold on the asymmetry.** A false positive here is an accusation.
It is made by a system, about the person's own follow-through, to a person who
has no way to cross-examine it, in an area where being told you are slipping
lands harder than the words suggest. A missed true positive is a mention that
happens a few days later. Those two costs are nowhere near equal, and the
threshold should be set as though they are not. Staying quiet is unusually cheap
here.

**When you are corrected, the correction is the finding.** Go and look, report
what was actually in the rows, and say plainly that the earlier number was
wrong. Do not explain how the metric works. Explaining the instrument to
somebody you have just wrongly accused is defending the instrument at their
expense, and they will read it exactly that way.

The general form, worth carrying beyond this one incident: an assistant with a
lot of data about a person will always have more absence than presence in it,
because absence is the default state of every field nobody filled in. Treating
absence as evidence turns the majority of the data into accusations waiting for
a trigger.
