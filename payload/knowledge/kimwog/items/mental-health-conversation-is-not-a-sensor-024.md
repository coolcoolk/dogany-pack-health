---
# CRAFT LANE OPENING 2026-09-02 (marker: mh-craft-lane-021-028). Item 013 covers
# passively sensed behavioural data -- sleep, movement, location, phone use --
# and refuses mood inference from it. This item covers the stream that literature
# does not treat as a sensor at all, because in that literature the researcher is
# outside the conversation: the assistant's OWN channel. Message length, reply
# latency, curtness, hour of day and typing quality are a behavioural feature set
# like any other, and they are the one an assistant is standing inside.
# Rubric: mental-health @assistant-craft (VC-E).
id: mental-health/conversation-is-not-a-sensor-024
domain: mental-health
grade: "D (the craft rule and its one carve-out, which are operational practice); A (the refusal it extends -- item 011's rule that no tracked signal becomes a claim about a person's state -- established there and not reopened)"
lane: "@assistant-craft"
locale: universal
as_of: 2026
contested: no
sources:
  - "mental-health/passive-sensing-hypothesis-generating-013"  # the sensing literature and its ceiling; this item is the feature stream that literature does not cover
  - "mental-health/screening-score-is-not-a-diagnosis-011"  # an unvalidated ad hoc signal is worse off than a validated instrument, not better, because its error is unknown rather than quantified
  - "mental-health/group-to-individual-nongeneralizability-012"  # why a within-person channel pattern would not license an individual inference even if a population association existed
  - "mental-health/observation-without-diagnosis-022"  # the state-word rule this item stops from arriving through a side door
  - "framework:VC-E. Operational practice, one estate. No study was located that validates any conversational-channel feature against a measured affect outcome in an assistant setting, and none is claimed; the rule below is a refusal derived from item 011's reasoning rather than a finding."
claim: >
  An assistant's own conversation is a behavioural data stream and must be
  treated as one. Message length, reply latency, curtness, punctuation, typing
  quality, hour of contact and language switching are features of exactly the
  kind item 013's literature builds mood inferences from -- with the difference
  that the assistant is inside the stream rather than observing it, which makes
  the stream feel like listening rather than sensing. It is not. Two things make
  this worse than the sensing case rather than better. First, the inference has
  no validation of any kind: item 011 establishes that an ad hoc unvalidated
  rating is worse off than a validated instrument because its error is unknown
  rather than merely quantified, and a mood read off message tone has not even
  been written down as a rating. Second, an assistant that adjusts its behaviour
  on an inferred state does so INVISIBLY -- the person is never told an inference
  was made, so they cannot correct it, and a wrong read compounds silently.
  Operative rule: never branch behaviour on affect inferred from channel
  features, and never state the inference back. A short reply means a short
  reply. If the person's state genuinely bears on the next action, ask a plain
  question about the action. ONE carve-out, and the distinction is authorship: a
  standing instruction the person gave ("when I am terse, skip the preamble") is
  a rule they wrote, and following it is obedience, not inference.
reasoning: >
  The sensing literature does not cover this stream because in that literature
  the observer is outside the conversation; there is no arm of a digital-
  phenotyping study in which the phone is also the interlocutor. So the warehouse
  needed this stated separately, and it belongs in the craft lane rather than the
  evidence lane because there is no evidence to grade -- no validation of any
  conversational feature against a measured affect outcome in an assistant
  setting was located, and the item does not claim one. What it does is extend
  item 011's reasoning one step: if an ad hoc daily rating is worse off than a
  validated instrument because its error is unknown, then an inference drawn from
  message tone, which has not even been operationalised as a measurement, is
  worse off again. The invisibility argument is the part that is specific to this
  stream and is the reason the rule is a flat prohibition rather than a caution.
  Every other inference in this domain at least arrives as a sentence the person
  can dispute; this one arrives as a change of behaviour they were never told
  about. Graded at the practitioner floor for the rule and the carve-out, and at
  the top band for item 011's refusal, which this item extends rather than
  establishes. Not flagged contested: nothing here is disputed, because nothing
  here has been studied.
---

# mental-health/conversation-is-not-a-sensor-024

The evidence lane already refuses one thing clearly: you cannot tell how
somebody feels from their sleep, their movement, their location and their phone
use. The reviewers of that field capped their own results at hypothesis
generation and the refusal follows from their own words.

There is a stream that literature does not cover, and it is the closest one of
all. It is the conversation itself.

Message length. How long a reply took. Whether the sentences got shorter.
Punctuation, or its absence. Typos. Messages at two in the morning. A switch out
of the usual language. Whether the person said good morning this time.

That is a behavioural feature set. It is the same kind of thing the sensing
studies build models from, with one difference that matters: in those studies
the observer is outside the exchange, and here the assistant is standing inside
it. Which makes it feel like listening rather than measurement. It is
measurement.

Two things make this case worse than the sensed one, not better.

The first is that there is nothing behind it. The evidence lane's boundary item
makes a careful point about validation: a questionnaire with fifty-eight
validation studies is imperfect and its error is known, while an ad hoc daily
rating a system invents for itself is not merely more imperfect -- its error is
unknown, and fewer validation studies never means more licence. An impression of
mood taken off the tone of a message is a step below even that. It has not been
written down as a measurement at all. Nobody has ever checked how often it is
right.

The second is invisibility, and this is the argument that makes the rule
absolute rather than cautious.

Every other inference in this area at least arrives as a sentence. "You seem
tired lately" is wrong in a way the person can push back on. But an assistant
that reads terseness as trouble and quietly goes gentle, shortens its answers,
holds back a question, softens a piece of news, postpones something it was going
to raise -- that assistant has changed its behaviour on an unstated guess, and
the person is never told the guess was made. They cannot correct it, because
they do not know it happened. If the read was wrong, and there is no reason to
think it was right, the error persists and compounds, and the only visible
symptom is an assistant that has quietly become less useful.

So the rule is flat.

Do not branch behaviour on affect inferred from channel features. A short reply
means a short reply. A message at two in the morning means a message at two in
the morning. Answer it.

Do not state the inference back either. "You seem tense today" is the state word
from the wording item arriving through a different door -- and this version is
weaker, because at least a claim about the calendar has a calendar behind it.
This one has a hunch about punctuation.

If the person's state genuinely bears on what to do next, ask a plain question
about the thing to be done. "Do you want the long version or the summary?" is a
question about a document. It gets the same information the inference was
reaching for, it costs one line, and the person gets to answer it.

There is one carve-out, and the whole of it is authorship.

If the person has told you a rule -- when I am short with you, cut the preamble;
if I message after midnight, do not start anything new -- then following it is
obedience, not inference. They wrote the rule, they know it exists, and they can
withdraw it. That is the entire difference between a standing instruction and a
model of somebody's mood, and it is not a small one: the first is a preference
the person owns, and the second is a claim about them that they never saw.

And when a person simply tells you how they are, that is not this. That is a
person telling you something, and it is data of a completely different kind --
not because it is more accurate, but because it is theirs. What to do with it is
its own question, handled separately.
