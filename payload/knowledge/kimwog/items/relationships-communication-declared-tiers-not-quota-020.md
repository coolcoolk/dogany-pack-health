---
# @relational-craft (VC-E), opened 2026-09-02. The owner has DECLARED intimacy
# tiers with yearly contact bands. The evidence lane has shipped a deliberate
# absence row saying no primary source prescribes any contact cadence. Those two
# facts are about to meet inside one agent, and without this row the predictable
# collision is an agent that reads the absence row and downgrades the owner's own
# setting as unsupported -- which would be a misuse of the absence row, not an
# application of it. This row states the direction of authority in both
# directions, and records a live numeric mismatch found while writing it.
id: relationships-communication/declared-tiers-not-quota-020
domain: relationships-communication
grade: D (craft -- operating rules for a DECLARED preference; the tier bands themselves are not an evidence claim, carry no evidential grade, and are not graded here)
lane: "@relational-craft"
locale: universal
as_of: 2026-07-19 to 2026-09-02
contested: yes
sources:
  - "owner-directive:2026-07-19 (declared, recorded in the knowledge-warehouse-ownership worklog 2026-09-02) -- tier 5 = 10 or more contacts a year, tier 4 = 4 to 9, tier 3 = 1 to 3; gap alerts fire on the OVERRUN RATIO against the declared tier rather than on a fixed interval; and explicitly: this is the owner's declared preference, not an evidence claim, and the warehouse's cadence-absence item does not refute it"
  - "measured:kit_life intimacy_levels table, read 2026-09-02 -- seven tiers, each carrying a qualitative criterion plus a cycle_months value labelled 'recommended meeting cycle'. Tier 5 (comfortable friend) 2.0 months, tier 4 (close friend) 4.0 months, tier 3 (occasionally-seen friend) 12.0 months, tier 2 18.0, tier 1 24.0, tier 0 48.0, partner 0.25"
  - "practice:kit relationship module, relmod compute_stale_list() -- the overdue ratio is computed as elapsed gap over cycle_months multiplied by thirty, per person, with a let-fade exclusion and a per-person channel mode (meet / contact / mixed, default meet); the ranking is sorted by that ratio"
  - "relationships-communication/contact-cadence-no-evidence-014"  # the absence row this one keeps from being misapplied
  - "relationships-communication/tie-reciprocity-perception-gap-012"  # why a tier is a note about how the owner sees a person, not a property of the pair
  - "framework:GRADE -- bottom band, and the reason is categorical rather than evidential. A declared preference is not the kind of thing that has a confidence level: it is not more or less likely to be true, it is simply what the owner chose. What IS graded here is the craft around it -- how to operate a declared band without converting it into a quota, and which way authority runs when a declaration meets an evidence row. That is practice, at the same band as the exercise domain's practitioner-heuristic rows. Marked contested because two live numeric parameterisations of the SAME declared preference disagree on their face (see the mismatch note); the contest is internal to the owner's own system, not in any literature."
refraction_notes:
  - note: >
      THE DECLARATION OF RECORD, quoted as a preference and not as a finding.
      Tier 5, ten or more contacts a year. Tier 4, four to nine. Tier 3, one to
      three. Gap alerts fire on how far past the declared band a gap has run --
      an overrun ratio -- rather than on a fixed universal interval. The owner
      set this on 2026-07-19 and it was re-affirmed in writing on 2026-09-02,
      specifically alongside the warehouse's cadence-absence row, with the note
      that the two do not conflict.
    grade: D
  - note: >
      DIRECTION OF AUTHORITY, FIRST DIRECTION. The absence row
      (relationships-communication/contact-cadence-no-evidence-014) refuses the
      claim that research prescribes a contact frequency. It says nothing about a
      frequency somebody chose for himself, and it cannot: a preference is not a
      hypothesis and does not compete with evidence for the same slot. An agent
      that reads 014 and then tells the owner his own tier setting is
      unsupported has inverted the row -- it exists to stop the agent inventing a
      number, not to stop the owner having one. 014 itself says this in as many
      words: a user-stated interval is a legitimate user preference and must be
      spoken as one.
    grade: D
  - note: >
      DIRECTION OF AUTHORITY, SECOND DIRECTION, and this one is the constraint.
      The band never leaves the owner's own configuration. It is not advice, it
      does not generalise to anyone else, it is never offered as what a
      relationship needs, and it is never justified by pointing at the warehouse.
      If asked why the number is what it is, the honest answer is that the owner
      chose it and it can be changed -- not that it is recommended. The moment a
      declared value is spoken with warehouse authority behind it, the absence row
      has been defeated from the inside.
    grade: D
  - note: >
      A BAND IS A CRITERION, NOT A TARGET -- the distinction the whole row turns
      on. Ten-plus a year is part of what makes somebody a tier 5 person, sitting
      alongside the qualitative criterion already stored against that tier
      ("someone you talk to about small everyday things"). Read the other way
      round -- as a number to hit -- it becomes a quota, and a quota is exactly
      the prescription the evidence lane refuses AND the obligation the owner's
      own no-guilt directive forbids. The same number is safe as a classifier and
      unsafe as a goal, and nothing in the data marks which way it is being used.
      That is why it has to be written down.
    grade: D
  - note: >
      A TIER IS A NOTE ABOUT THE OWNER'S VIEW, not a property of the pair. The
      level is set by one person about another, which is the exact instrument the
      evidence lane records as biased toward assuming mutuality in established
      ties (relationships-communication/tie-reciprocity-perception-gap-012). This
      does not make tiers useless -- as a sorting key for the owner's own
      attention they do not need to be mutual. It does mean a tier is never
      spoken as a fact about the relationship, never used to tell the owner where
      he stands with someone, and never turned into a claim about what the other
      person feels.
    grade: D
  - note: >
      LIVE MISMATCH, FOUND WHILE WRITING THIS ROW, FLAGGED AND NOT FIXED. The
      stored cycle values do not match the declared bands on their face. Declared
      tier 5 is ten-plus contacts a year, implying a cycle of about 1.2 months;
      the stored cycle for tier 5 is 2.0 months, roughly six a year. Declared tier
      4 is four to nine a year (about 1.3 to 3.0 months); stored is 4.0 months,
      roughly three a year -- outside the band. Declared tier 3 is one to three a
      year (4 to 12 months); stored is 12.0 months, at the loose edge but inside.
      The ranking engine computes its overrun ratio from the STORED value, so on
      its face the engine is running looser than the declaration it implements,
      and most so at the closest tier.
    grade: D
  - note: >
      THE BENIGN READING OF THAT MISMATCH, stated because asserting a defect
      without it would be exactly the over-read this lane refuses. The stored
      field is labelled a recommended MEETING cycle, while the declaration is
      phrased as contacts. A looser meeting cycle underneath a tighter contact
      band is perfectly coherent -- ten contacts a year with six meetings among
      them is an ordinary shape for a close friendship. The module's per-person
      channel mode makes this live rather than theoretical: the default channel is
      meetings, and remote friends can be switched to counting any contact. So
      there are two readings, one benign and one a real drift between declaration
      and implementation, and NOTHING IN THE STORE DISTINGUISHES THEM. The craft
      rule is therefore to flag it to the owner as a question about units, not to
      reconcile it by choosing a number. An agent that silently picked either
      value would be inventing the owner's preference on his behalf.
    grade: D
claim: >
  The owner's intimacy tiers are a DECLARED preference and must be operated as a
  classification, never as a quota, and never re-described as evidence. The
  declaration of record (2026-07-19): tier 5 is ten or more contacts a year, tier
  4 is four to nine, tier 3 is one to three, and gap alerts fire on the OVERRUN
  RATIO against the declared band rather than on a fixed interval. Four rules.
  (1) AUTHORITY RUNS ONE WAY IN: the cadence-absence row (item 014) refuses the
  claim that research prescribes a frequency; it does not touch a frequency the
  owner chose, and an agent that cites it to call the owner's own setting
  unsupported has inverted it -- 014 says in its own text that a user-stated
  interval is a legitimate preference. (2) AND ONE WAY OUT: the band never leaves
  the owner's configuration as advice, never generalises, and is never justified
  by pointing at the warehouse; asked why, the honest answer is that he chose it
  and can change it. (3) A BAND IS A CRITERION, NOT A TARGET: ten-plus a year is
  part of what makes someone tier 5, alongside the qualitative criterion already
  stored against that tier; read as a number to hit it becomes the quota the
  evidence lane refuses and the obligation the owner's own no-guilt directive
  forbids, and nothing in the data marks which way it is being used. (4) A TIER
  IS THE OWNER'S VIEW, not a property of the pair -- the same one-sided
  instrument item 012 records as biased toward assumed mutuality; usable as a
  sorting key for his own attention, never spoken as a fact about where he stands
  with someone. LIVE MISMATCH, flagged not fixed: the stored cycle values (tier 5
  = 2.0 months, tier 4 = 4.0, tier 3 = 12.0) imply roughly six, three and one
  contacts a year against declared bands of ten-plus, four-to-nine and
  one-to-three, and the ranking engine computes from the stored value. There is a
  benign reading -- the stored field is a MEETING cycle while the declaration
  counts contacts -- and a defect reading, and nothing in the store distinguishes
  them. Raise it with the owner as a question about units; never reconcile it by
  choosing a number for him.
reasoning: >
  This row was written because a collision was scheduled and nobody had put
  anything between the two sides of it. The evidence lane landed a deliberate
  absence row saying no primary source prescribes a contact cadence, and it landed
  it on the same day, in the same agent, that already carries the owner's declared
  per-tier yearly bands. The owner's own worklog flagged the risk in writing: an
  agent could read the absence row and start treating his configuration as
  unsupported folklore. That would be a misuse rather than an application, and the
  distinction is not subtle -- a preference and a hypothesis do not occupy the same
  slot, so they cannot contradict each other. Saying so in the ledger would not
  help, for the same reason the absence row was made an item instead of a gap
  entry: a note somewhere else does not fire at the moment the decision is made.
  The second direction is the harder half and is the one that keeps this from
  being a door for folklore. A declared preference is legitimate INSIDE the
  owner's configuration and nowhere else; the instant it is spoken outward as
  advice, or justified by the presence of a warehouse behind it, the absence row
  has been defeated by the very item that was supposed to protect it. The
  criterion-versus-target rule is the mechanism by which that leak actually
  happens in practice, which is why it is stated as a rule rather than as a
  caution: the same number is safe as a classifier and unsafe as a goal, and the
  data does not record which way it is being read. Marked contested for a specific
  and unusual reason -- not a dispute in any literature, but two live
  parameterisations of one declared preference that disagree on their face, with a
  benign explanation available and no way to tell from inside the store. That is
  reported at its full strength and then explicitly not resolved, because
  resolving it would mean picking a number on the owner's behalf, which is the
  same act this row exists to forbid.
---

# relationships-communication/declared-tiers-not-quota-020

The owner set his own tiers. Tier 5 is ten or more contacts a year, tier 4 is
four to nine, tier 3 is one to three, and a gap gets flagged by how far past the
band it has run rather than by any fixed interval.

The warehouse also says, in an item shipped the same day, that no primary source
anywhere prescribes a contact frequency.

Those two things are about to sit inside the same agent, and the obvious mistake
is to think one of them beats the other.

Neither does, because they are not the same kind of statement. The absence row
refuses a claim about the world -- that research recommends some rhythm. The
tiers are not a claim about the world at all. They are what the owner picked.
A preference cannot be unsupported, because it was never claiming support. The
absence row says this itself, in its own text: an interval the user sets is a
legitimate user preference and should be spoken as one.

So the first rule is that an agent reading the absence row must not turn around
and tell the owner his settings are folklore. That is the row inverted. It exists
to stop the agent from inventing a number, not to stop the owner from having one.

The second rule is the one that costs something, and it is the reason this row is
safe to write at all. The band stays inside the owner's own configuration. It is
not advice. It does not travel. It is never offered as what a friendship needs,
and it is never propped up by the fact that a knowledge warehouse is sitting
behind the agent saying it. If the owner asks why the number is ten, the true
answer is that he chose ten and can choose something else. Any answer that sounds
more authoritative than that has smuggled the invented cadence back in through
the one door built to keep it out.

Third, and this is where it actually goes wrong in daily use: a band is a
criterion, not a target.

Ten-plus a year is part of what makes somebody a tier 5 person. It sits next to
the qualitative criterion already stored against that tier -- someone you talk to
about small everyday things. Together they describe a kind of relationship. Read
backwards, as a number to hit, the same figure becomes a quota: nine contacts and
you are behind. That is the prescription the evidence refuses and the obligation
the owner has forbidden on every surface he owns, arrived at without anybody
deciding to add either. And nothing in the stored data marks which way the number
is being read, which is exactly why it has to be written down somewhere that
fires when it is used.

Fourth: a tier is one person's note about another. The owner sets it. That is the
same one-sided instrument the evidence lane records as reliably biased toward
assuming the feeling is mutual. This does not make tiers useless -- as a way of
sorting his own attention they never needed to be mutual. It means a tier is
never spoken as a fact about the relationship, and never used to tell him where
he stands with someone.

## One mismatch, flagged and left alone

Writing this row turned up something worth reporting rather than smoothing over.

The stored per-tier cycle values do not match the declared bands on their face.
Tier 5 is stored at a two-month cycle, about six a year, against a declared band
of ten or more. Tier 4 is stored at four months, about three a year, against a
declared four-to-nine -- outside the band. Tier 3 is stored at twelve months,
about one a year, which sits at the loose edge of its declared one-to-three but
inside it. The ranking that decides who gets surfaced is computed from the stored
value, so on its face it is running looser than the declaration it implements,
and the divergence is largest at the closest tier.

There is a perfectly innocent explanation. The stored field is labelled a
recommended MEETING cycle, and the declaration counts contacts. Ten contacts a
year with six actual meetings among them is an entirely normal shape for a close
friendship, and the module already tracks meetings and other contact separately,
with a per-person switch for people who are only ever reachable remotely.

And there is the other explanation, which is that the engine drifted from the
declaration.

Nothing in the store tells the two apart. So the rule is: raise it with the owner
as a question about which unit each number is in. Do not reconcile it by
picking one. Choosing a value here would mean deciding the owner's preference on
his behalf, which is the single thing this entire row exists to forbid.
