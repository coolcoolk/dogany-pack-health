---
# First item of the @relational-craft lane (VC-E), opened 2026-09-02 because
# the relationships-communication domain held 17 evidence items and zero craft
# items while its consumer runs a live roster of 115 people and 293 recorded
# relations. Modelled on the exercise domain's @gym-craft rows: the basis is
# practice rather than a trial, and the basis is STATED rather than implied.
# This row exists because the single most consequential thing a contact log can
# do is accuse the owner of something he did not do, and that failure has
# already happened once in a sibling surface of the same product.
id: relationships-communication/record-absence-not-neglect-018
domain: relationships-communication
grade: D (craft operating rule -- distilled from one dated local failure, one owner directive and code currently in force; no trial and no literature behind it, and none claimed)
lane: "@relational-craft"
locale: universal
as_of: 2026-08-28 to 2026-09-02
contested: no
sources:
  - "incident:2026-08-28 roller-anomaly-on-retired-routine (pack worklog ticket, P0, opened 2026-08-28, closed 2026-09-02 11:35) -- an anomaly detector emitted consec_miss=4 for a routine that had been retired four months earlier; the agent relayed it to the owner three times as four consecutive missed training sessions; the owner replied that he had trained the day before; the domain table held real entries on exactly the dates counted as missed"
  - "owner-directive:2026-09-02 10:59 -- for any resource the kit can actually see, settle the schedule against the domain record FIRST, judge 'not done' only when evidence was looked for and not found, and stay SILENT for resources the kit does not see at all. The alert condition becomes 'evidence was checked and is absent', not 'no record exists'"
  - "design:2026-08-28 area-metric-axis DESIGN, sections 8.22.3 and 8.23.4 -- the three-state model (value present / verified absent / unknown) and the rule that unknown is never promoted into neglect; carried forward into the kit-life v3 skeleton"
  - "practice:kit relationship module, relmod compute_stale_list() -- in force today: a person with zero recorded contact is excluded from stale ranking entirely, on the stated ground that zero record means an UNKNOWN gap rather than an overdue one; the separate check-in path surfaces at most one such person as a curiosity question with a 60-day per-person window"
  - "relationships-communication/contact-cadence-no-evidence-014"  # the evidence-side pairing: there is no cadence to be behind on in the first place
  - "relationships-communication/tie-reciprocity-perception-gap-012"  # the same instrument problem stated from the evidence side: this store is one person's report
  - "framework:GRADE -- bottom band by construction, and the band is honest rather than modest. This is an operating rule with three kinds of basis, all of them local: a dated incident whose ground truth was checked against the owner's own records, an owner directive issued in response to it, and code currently running that already implements the rule for this surface. There is no experiment, no external source, and no generalisation to anyone else's system claimed anywhere in it."
refraction_notes:
  - note: >
      THE DOCUMENTED FAILURE, with its ground truth, because a craft rule with no
      failure case behind it is just an opinion. On 2026-08-28 an anomaly detector
      in the training surface of the same product reported four consecutive missed
      sessions. The agent relayed that number to the owner three times without
      checking it. The owner said he had trained the day before. He was right: the
      domain table held real entries on the very dates that had been counted as
      missed. The detector had been reading unfilled calendar instances of a
      routine that was retired four months earlier, and it translated "the
      instance ledger has no stamp" into "the person did not do it". Those are not
      the same sentence, and the second one is a judgement about the owner's own
      behaviour, which is where being wrong costs the most.
    grade: D
  - note: >
      THE PREDICATE, which is the transferable part. The defect was not a bad
      threshold or a noisy signal. It was a silent substitution of one predicate
      for another: absence-of-record was read as absence-of-event. The owner's own
      correction fixed it at that level rather than by tuning the number -- settle
      against the domain record first; judge only after evidence was looked for
      and not found; and where the system cannot see the resource at all, do not
      judge and do not notify. The last clause is the one that is easy to skip and
      is the most important: silence is a legitimate output.
    grade: D
  - note: >
      WHY THE RELATIONSHIP SURFACE IS THE MORE EXPOSED ONE, not the safer one.
      The training surface at least had a second table to settle against. This
      surface has no automatic evidence source whatsoever: every meeting and every
      touch exists only because the owner or the agent typed it in. A quiet phone
      call leaves no trace at all. So the proportion of the log that is real
      absence, as opposed to unrecorded presence, is not merely unknown here --
      it is unknowable from inside the system. Any confident statement about a
      gap is therefore a statement about the log, not about the owner's life.
    grade: D
  - note: >
      WHAT IS ALREADY IN FORCE, recorded because a craft lane should describe
      practice rather than propose it. The stale-list computation excludes any
      person with zero recorded contact from ranking entirely, with the reason
      written into the code: zero record means an unknown gap, not an overdue one.
      Separately, at most one zero-record person per surfacing is raised through a
      distinct path, phrased as curiosity about how that person is doing, capped
      at one per surfacing and one per person per 60 days, and explicitly
      forbidden from being framed as something the owner should do. That pairing
      -- exclude from the accusation path, admit to the question path -- is the
      concrete shape of the rule, and it is the thing that does not exist in any
      paper.
    grade: D
  - note: >
      WHAT THIS DOES NOT LICENSE, in both directions. It does not license the
      inverse claim that the owner's relationships are fine; the log cannot
      support that either, and an agent that answered "you are all caught up" from
      an empty table would be making the same error with the sign flipped. And it
      does not license silence as a general posture: the third state is UNKNOWN,
      and the correct output for unknown is a question, not a finding and not
      nothing. The failure mode this row blocks is specifically the promotion of
      unknown into neglect.
    grade: D
  - note: >
      THE HONEST LIMIT ON THE BASIS. The documented incident is from the training
      surface, not this one. A targeted search of the owner's worklogs, tickets
      and memories found NO case of the relationship module falsely accusing him
      of neglecting a person. So this row is carried forward by structural
      analogy -- same product, same predicate, a surface with strictly weaker
      evidence -- and not by a relationship incident. That distinction is stated
      here rather than smoothed over, because a craft lane that inflates its own
      basis is exactly the folklore door this lane was built to keep shut.
    grade: D
claim: >
  A contact log is a partial instrument, and in this store it is a hand-fed one:
  a row exists only because someone wrote it. An empty stretch therefore carries
  two readings that the data cannot separate -- no contact HAPPENED, or no
  contact was RECORDED -- and an agent must never promote the second into the
  first. The failure is documented and dated rather than hypothetical: on
  2026-08-28 an anomaly detector in the training surface of the same product
  reported four consecutive missed sessions from unfilled instances of a routine
  retired four months earlier, the agent relayed it to the owner three times, and
  the owner was right that he had trained -- the domain table held entries on the
  exact dates counted as missed. The owner's correction (2026-09-02) changed the
  predicate rather than the threshold: settle against the domain record first,
  judge only when evidence was sought and not found, and stay silent where the
  system cannot see the resource at all. The relationship surface is MORE
  exposed, not less, because it has no automatic evidence source -- a phone call
  that nobody logs leaves no trace anywhere. OPERATING RULE: three states, not
  two. Recorded contact; verified absence; UNKNOWN. Unknown is never rendered as
  neglect, is never counted into a gap statistic spoken as fact, and is answered
  with a question rather than a finding. This is already how the surface behaves:
  a person with zero recorded contact is excluded from stale ranking outright,
  and is instead admitted to a separate, capped, curiosity-framed check-in path.
  The rule cuts both ways -- an empty log also cannot support "you are all caught
  up".
reasoning: >
  This is the first row of a craft lane, and the choice of what to put first is
  itself a statement about what the lane is for. The evidence lane established
  what predicts relationship satisfaction and, more usefully, what does not. None
  of that tells an agent holding 115 people and a partial contact log what to do
  on a Tuesday when a name has been quiet for three months. The single highest-
  stakes thing that surface can do is tell the owner he neglected somebody, and
  the single most likely way for it to be wrong is that the contact happened and
  nobody typed it. That is not speculation: the identical predicate error has
  already fired once in this product, in a surface with BETTER evidence available
  than this one has, and it reached the owner three times before he corrected it
  in conversation. A rule with that provenance is exactly what a VC-E row is for
  -- its basis is practice, the practice is dated and checkable, and the finding
  exists in no publication. The grade sits at the bottom band and stays there:
  nothing here is generalised beyond this product, no effect is claimed, and the
  incident is a single event rather than a study. Two things are stated in the
  row rather than left implied, both to stop a later reader over-reading it. The
  first is that the rule is symmetric -- the same empty table that cannot prove
  neglect also cannot prove that all is well, and an agent that reassures from
  absence has made the same mistake in the other direction. The second is that
  the incident that grounds the rule is from the training surface, and that no
  relationship-side false accusation is on record; the transfer is by structural
  analogy and is argued, not assumed. Not marked contested: there is no dispute
  here, and the owner has already ruled on the predicate.
---

# relationships-communication/record-absence-not-neglect-018

The log does not know what happened. It knows what got typed.

Every meeting and every message in this store exists because the owner or the
agent wrote it down. There is no sensor, no import, no second table to check
against. So when a name goes quiet in the record, the record is holding two
different situations that look identical from the inside: the contact did not
happen, or the contact happened and nobody wrote it down.

Treating the second as the first has already gone wrong once, in the same
product, on a surface that had better evidence available than this one does.

On the twenty-eighth of August an anomaly detector reported four consecutive
missed training sessions. The number came from a routine that had been retired
four months earlier: its calendar instances were still being generated and were
sitting unstamped, and the detector read unstamped as undone. That number went
to the owner three times, unchecked. He said he had trained the day before. He
was right -- the training table held real entries on the very dates that had
been counted as missed.

The important part is not the bug. It is which sentence got substituted for
which. "The instance ledger has no stamp" became "you did not do it." Those are
different claims, and the second one is a verdict on the owner's own behaviour,
which is where being wrong is most expensive. Trust does not degrade gracefully
here. One confident false accusation costs more than a hundred quiet correct
observations earn.

The owner's own fix, issued a few days later, changed the predicate rather than
the sensitivity. Where the system can actually see the resource, settle the
schedule against the real record first, and only call something undone once the
evidence has been looked for and is genuinely not there. Where the system cannot
see the resource at all, do not judge it, and do not send anything. Silence is
an allowed answer.

Now apply that here, and notice that this surface is the weaker one. The
training surface at least had a second table. This one has nothing behind the
log. A phone call on a walk, a message in an app the system never sees, a chance
meeting -- none of it leaves any trace unless someone types it later. The share
of the log that represents real absence rather than unrecorded presence is not
just unknown; from inside the system it is unknowable. So any confident claim
about a gap is a claim about the log, and it should be spoken as one.

The working shape is three states rather than two.

There is recorded contact. There is verified absence -- which on this surface
barely exists, because verifying it would require asking. And there is UNKNOWN,
which is most of the empty space. Unknown never becomes neglect. It does not get
counted into a gap statistic that then gets spoken as a fact. And its correct
output is a question, not a finding.

This is already how the surface behaves, and the shape is worth stating because
it is not obvious. A person with no recorded contact at all is thrown out of the
overdue ranking entirely -- an unknown gap cannot be ranked against a known one,
so it is not ranked. That same person is then admitted through a completely
different door: at most one per surfacing, at most once every sixty days,
phrased as curiosity about how they are doing rather than as something the owner
ought to be doing. Excluded from the accusation path; admitted to the question
path. That pairing is the whole rule in one mechanism, and it appears in no
paper anywhere.

One last thing, because the rule is symmetric and only one half of it is
intuitive. The same empty table that cannot prove the owner neglected someone
also cannot prove that he did not. An agent that looks at a quiet log and says
"you are all caught up" has made exactly the same error with the sign reversed.
Unknown means unknown.

And the honest limit on all of this: the incident that grounds it is from the
training surface. A search of the owner's tickets and records turned up no case
of the relationship module falsely accusing him about a person. The rule is
carried across by argument -- same product, same substituted predicate, a
surface with strictly less evidence to work from -- not by an incident of its
own. If one ever happens here, it belongs in this row.
