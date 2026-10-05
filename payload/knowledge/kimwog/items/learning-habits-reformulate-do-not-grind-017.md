---
# STUDY-CRAFT LANE (VC-E). The setup half of the craft: what a well-formed
# study item looks like, and what to do with one that keeps failing. This is the
# study analogue of "the machine is set up wrong" rather than "push harder".
#
# Both sources are practitioner primaries read at source: the Anki manual's
# leeches page for the documented failure threshold and its stated remedy
# ordering, and Wozniak's 1999 rule set for the formulation principle. Neither
# has been tested as a package and this item says so.
id: learning-habits/reformulate-do-not-grind-017
domain: learning-habits
grade: D (practitioner-heuristic)
lane: "@study-craft"
locale: universal
as_of: 1999-2026
contested: yes
sources:
  - "https://docs.ankiweb.net/leeches.html"  # the 8-lapse default, the auto-suspend, and the manual's own remedy ordering
  - "https://www.supermemo.com/en/blog/twenty-rules-of-formulating-knowledge"  # Wozniak, P. (1999). Effective learning: Twenty rules of formulating knowledge.
  - "https://supermemo.guru/wiki/Minimum_information_principle"
  - "learning-habits/rep-is-attempt-then-check-016"  # within-warehouse cross-ref: same lane, defines the rep whose repeated failure this item diagnoses
  - "framework:GRADE -- one practitioner's 1999 rule compilation plus one application's shipped default. The twenty rules have never been tested as a package, no experiment supports the specific 8-lapse threshold, and no study compares reformulating a failing item against continuing to drill it."
claim: >
  An item that keeps failing is a badly formed item, and the correct response is
  to REBUILD IT, not to drill it harder. The practice is documented rather than
  measured. Anki ships an automatic detector: a review card that has lapsed
  eight times is tagged a leech and SUSPENDED, on the stated grounds that
  "leeches are cards that you keep forgetting. Because they require so many
  reviews, they take up a lot more of your time, compared to other cards" --
  and the manual's first remedy is not more effort but reformulation, "the most
  efficient method to deal with leeches is to change how the information is
  presented", with deletion offered as an acceptable second option when the
  material is not worth the time. The formulation principle underneath is
  Wozniak's minimum information principle (1999): split material until each
  item asks for ONE retrieval, because a compound item cannot report which part
  failed and cannot be scheduled at the pace its hardest part needs. This is a
  single practitioner's rule set, never validated as a whole, and the specific
  threshold of eight is a shipped default with no derivation.
reasoning: >
  This is the highest-folklore-risk area in the domain and the item is
  deliberately narrow because of it. Two things make the shipped claim
  defensible rather than repeated. First, it is falsifiable and mechanical: an
  item that bundles three facts produces one pass/fail signal for three
  retrievals, so a failure cannot be attributed and the scheduler is forced to
  treat the easy parts at the hard part's interval. That is an argument from
  the structure of the instrument, not an appeal to consensus. Second, the
  remedy ORDERING is documented in a shipped product used at scale, and it puts
  reformulation ahead of repetition -- which is the non-obvious part, and the
  part most study advice gets backwards.
  .
  What is not established, and must be said whenever this is used. Nobody has
  compared reformulating a failing item against continuing to drill it. The
  eight-lapse threshold is a default chosen by developers, not an estimate; it
  is useful as a tripwire and meaningless as a number. Wozniak's twenty rules
  are one person's compilation from 1999 and have never been tested as a set,
  which is the same evidential position as this warehouse's single-coach
  practitioner items -- credible, internally coherent, uncorroborated. Marked
  contested because the surrounding advice literature is enormous, confident
  and almost entirely unsourced, and because a reader who meets this claim
  elsewhere will meet it stated as established fact.
---

# learning-habits/reformulate-do-not-grind-017

Some material will not stick. The universal instinct is to conclude something
about yourself and then hit it harder. The craft answer is the opposite one,
and it is the same answer a coach gives when a lift keeps failing at a weight
that should be easy: stop adding effort and look at the setup.

The practice here is documented rather than proven, and the documentation is
worth taking seriously precisely because it is a shipped mechanism rather than
an essay. Spaced-repetition software counts how many times each item has been
forgotten. When the count reaches eight, the item is automatically tagged and
taken out of circulation, on the explicit reasoning that items you keep
forgetting consume far more of your time than the rest. The remedy the manual
reaches for first is not more repetitions. It is to change how the information
is presented -- rebuild the item, split it, add a hook. Deletion is offered as
a legitimate second option: if the material is not worth what it is costing,
drop it. Working harder on the existing item is not on the list.

The formulation principle underneath comes from the oldest practitioner canon
in this field, a 1999 rule set from the author of the first widely used spaced
repetition system. Its central rule is to keep each item as small as possible:
one item, one retrieval. The reason is structural rather than mystical. An item
that asks for three things at once returns a single pass or fail for three
separate memories, so when it fails you cannot tell which part failed, and the
scheduler must treat the two parts you know well at the interval demanded by
the part you do not. Splitting it restores both the diagnosis and the pacing.
That is also what makes the failure signal in this lane's companion item
readable at all: a failing item only tells you something if it is small enough
to point at one thing.

Practically, when something keeps failing: split it into single retrievals;
make the prompt unambiguous enough that only one answer is correct; separate
items that are so similar they interfere with each other, and consider parking
one of them until the other is solid; and if none of that is worth doing, delete
it and let it go.

Honest limit, and it is a large one. No study compares rebuilding a failing item
against drilling it. The threshold of eight failures is a developer's default,
not a measured cut point -- treat it as a tripwire, never as a number that means
something. The twenty rules are one person's compilation and have never been
tested as a set. This is genuine craft knowledge from people who have run the
practice for decades, and it is exactly the kind of confident, well-written,
never-verified advice that this lane exists to handle carefully. Present it as
what it is: the practice of experienced practitioners, with the structural
argument for the minimum-information rule given openly so the reader can judge
it, and no pretence that a trial stands behind any of it.
