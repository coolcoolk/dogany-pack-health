---
# Collection sprint 2026-09-02 (mental-health lane expansion). The second thing
# a well-meaning life agent would suggest, after a gratitude exercise: an app.
# An umbrella review applying explicit evidence-strength criteria across 14
# meta-analyses found NO effect size in the entire literature meeting its
# convincing-evidence bar. Records the positive findings that do exist at their
# actual strength rather than dismissing the field, and records the specific
# pattern -- effects shrink as comparators get more rigorous -- that connects it
# to items 004 and 017.
# Rubric: mental-health @clinical (VC-A).
id: mental-health/phone-app-intervention-evidence-018
domain: mental-health
grade: "B (that no phone-based mental-health intervention effect reaches convincing-evidence criteria under umbrella-review methodology, and that effects shrink as comparators become more rigorous); C (the eight highly-suggestive effects, which are the field's real positive findings)"
lane: "@clinical"
locale: universal
as_of: 2022
contested: no
sources:
  - "https://pubmed.ncbi.nlm.nih.gov/35224559/"  # Goldberg SB, Lam SU, Simonsson O, Torous J, Sun S. 2022, PLOS Digit Health 1(1):e0000002, doi 10.1371/journal.pdig.0000002, PMCID PMC8881800 -- systematic meta-review of 14 meta-analyses representing 145 randomized controlled trials and 47940 participants, 34 unique PICO effect sizes graded by umbrella review methodology
  - "mental-health/mindfulness-pitfalls-006"  # the domain's existing item on the same field's positive-result saturation; many of these apps are mindfulness apps
  - "mental-health/wellbeing-exercise-comparator-collapse-017"  # the same comparator-collapse pattern in the self-help exercise literature
  - "mental-health/cbt-gad-comparator-004"  # the domain's original comparator-dependence rule
  - "framework:GRADE -- umbrella review methodology with prespecified evidence-strength criteria (convincing requires n greater than 1000, p less than 10 to the minus 6, I-squared under 50 percent, and absence of publication bias). A meta-review that grades its own field against a fixed bar and reports that nothing clears it is a stronger statement than any single pooled estimate."
refraction_notes:
  - note: >
      The headline, stated exactly and in the authors' own terms. Across 34 unique
      PICO effect sizes drawn from 14 meta-analyses (145 randomized controlled
      trials, 47940 participants), the reviewers "failed to find convincing
      evidence of efficacy", where convincing was prespecified as n greater than
      1000, p less than 10 to the minus 6, I-squared under 50 percent, and absence
      of publication bias. They also note that publication bias was RARELY
      ASSESSED for the representative effect sizes, which is itself part of why
      nothing cleared the bar.
    grade: B
  - note: >
      What DID clear the lower bars, because the field is not empty and reporting
      it as empty would be its own distortion. Eight effect sizes reached
      HIGHLY SUGGESTIVE evidence (n greater than 1000, p less than 10 to the minus
      6), including smartphone interventions outperforming INACTIVE controls on
      psychological symptoms and quality of life (d = 0.32 to 0.47), and
      text-message-based interventions outperforming non-specific controls
      (d = 0.31) and active controls (d = 0.19) for smoking cessation. Four
      effect sizes were suggestive, 14 weak, and 8 non-significant.
    grade: C
  - note: >
      The pattern that connects this to the rest of the lane, in the reviewers'
      own words: the magnitude of effects and the strength of evidence "tended to
      diminish as comparison conditions became more rigorous", moving from
      inactive to active and from non-specific to specific. This is the third
      independent appearance of comparator collapse in this domain, after the
      CBT-for-anxiety item and the wellbeing-exercise item, and it is now the
      lane's most reliably recurring structural finding rather than a
      one-intervention quirk.
    grade: A
  - note: >
      Notice which comparison the strongest surviving numbers come from. The
      smartphone effects that reached highly-suggestive status were against
      INACTIVE controls. The one active-control comparison that survived is
      text-message support for SMOKING CESSATION at d = 0.19 -- a behavioural
      outcome, not a mood outcome, and a small effect at that. So the best
      evidence in the field for phone-delivered help is not evidence about mood.
    grade: C
  - note: >
      Two further weaknesses reported by the reviewers. Despite substantial
      heterogeneity, NO moderators were identified -- so there is no
      evidence-based basis for saying which app, which population, or which
      format works better. And ADVERSE EFFECTS WERE NOT REPORTED anywhere in the
      literature reviewed, which means the safety of these interventions is
      unstudied rather than established.
    grade: A
  - note: >
      Operational consequence. Recommending an app is not forbidden by this
      evidence and the reviewers themselves conclude that the results support the
      POTENTIAL of these interventions. What is forbidden is the framing: an app
      may not be described as evidence-backed for improving mood, because no
      effect in the field meets the convincing bar, the surviving mood effects are
      against doing nothing, and nobody has published on harms.
    grade: B
claim: >
  No phone-delivered mental-health intervention has evidence of efficacy that
  meets convincing-evidence criteria. Goldberg et al. 2022 (PLOS Digital Health)
  synthesised 14 meta-analyses representing 145 randomized controlled trials and
  47940 participants, extracted 34 unique PICO effect sizes and graded them by
  umbrella review methodology, and report that they "failed to find convincing
  evidence of efficacy" -- convincing being prespecified as n greater than 1000, p
  less than 10 to the minus 6, I-squared under 50 percent and absence of
  publication bias -- while noting publication bias was rarely assessed for the
  representative effect sizes. Eight effect sizes reached highly suggestive
  evidence, including smartphone interventions beating INACTIVE controls on
  psychological symptoms and quality of life (d = 0.32 to 0.47) and
  text-message interventions beating non-specific (d = 0.31) and active (d = 0.19)
  controls for smoking cessation; four were suggestive, 14 weak, and 8
  non-significant. The reviewers report that effect magnitude and evidence
  strength tended to diminish as comparison conditions became more rigorous, that
  despite substantial heterogeneity no moderators were identified, and that
  adverse effects were not reported anywhere in the reviewed literature. Three
  consequences: the strongest surviving active-control finding is a smoking-
  cessation behaviour outcome rather than a mood outcome; there is no
  evidence-based basis for preferring one app, format or population over another;
  and safety is unstudied rather than established. An app may therefore be
  offered but may not be described as evidence-backed for improving mood.
reasoning: >
  After a wellbeing exercise, an app is the second thing a generalist assistant
  would reach for, and the field's marketing runs far ahead of its evidence. This
  meta-review was selected because of its METHOD rather than its result: instead
  of pooling one more estimate into a crowded literature, it applies a fixed,
  prespecified evidence-strength ladder to every effect size in 14 existing
  meta-analyses and reports where each one lands. That produces a claim of a
  different kind -- not "the effect is X" but "nothing in this field clears this
  bar" -- which is far more durable, since it will not be overturned by one more
  trial. The item deliberately records the eight highly-suggestive findings at
  their real strength rather than collapsing the field to nothing, because
  overstating a negative is the same error as overstating a positive and this
  warehouse's discipline applies in both directions; the reviewers themselves
  conclude the results support the potential of these interventions. The pattern
  worth promoting out of this item is comparator collapse: this is now its third
  independent appearance in the domain, after item 004 (CBT for anxiety loses
  significance against supportive therapy) and item 017 (gratitude effects fall
  from -0.51 to -0.18 against active controls), and three independent
  literatures showing the same structure make it a lane-level regularity rather
  than an intervention-specific quirk. The unreported-adverse-effects finding is
  carried at the top band because absence of harm reporting is routinely read as
  evidence of safety, and it is not. Graded at the trial band for the umbrella
  finding and at the observational band for the surviving positive effects. Not
  flagged contested: no source located disputes the meta-review, and its negative
  conclusion is a grading result rather than a contested estimate.
---

# mental-health/phone-app-intervention-evidence-018

The obvious suggestion, after a journalling exercise, is an app. Here is what
the evidence for those looks like when someone grades it against a fixed bar
instead of pooling one more estimate.

A team took 14 existing meta-analyses covering 145 randomised trials and nearly
forty-eight thousand participants, pulled out every distinct
participants-intervention-comparison-outcome combination, and graded each one
against prespecified criteria for how strong the evidence was. The top rung
required a large sample, a very small p-value, low heterogeneity, and no
publication bias.

Nothing reached it. Across 34 effect sizes covering the whole field, they failed
to find convincing evidence of efficacy for any of them. Part of the reason is
mundane and damning at once: publication bias was rarely even assessed for the
effect sizes they examined, so one of the four criteria usually could not be
checked.

The field is not empty, though, and saying it is would be its own kind of
overstatement. Eight effect sizes reached the next rung down. Smartphone
interventions beat inactive controls on psychological symptoms and quality of
life at around a third to a half of a standard deviation. Text-message support
beat both non-specific and active controls for quitting smoking.

Look carefully at which comparison each of those came from, because it matters.
The mood-related wins are against doing nothing. The one that survived a genuine
active comparison is a smoking-cessation outcome at about a fifth of a standard
deviation -- a behaviour, not a feeling, and a small effect.

Which is the third time this exact pattern has shown up in this domain. Anxiety
therapy holds up against a waitlist and loses significance against supportive
therapy. Gratitude exercises drop from half a standard deviation against a
waitlist to a sixth against any matched activity. And here the reviewers state it
outright as a property of their whole field: magnitude and evidence strength both
diminished as the comparison conditions got more rigorous. At three independent
literatures, that stops being a quirk and becomes something to expect by default.

Two more findings that constrain what can be said.

Despite a lot of variation between studies, no moderators were identified. So
there is no evidence-based way to say this app rather than that one, this format,
this kind of user. Any such recommendation is preference dressed as evidence.

And adverse effects were not reported anywhere in the reviewed literature. That is
not a clean safety record. It is an absence of data, and absence of data about
harm is not evidence of its absence -- a distinction this warehouse insists on
elsewhere and insists on here.

So: an app is not forbidden and the reviewers themselves think the field has
potential. What cannot be said is that it is evidence-backed for feeling better.
The strongest mood findings are against doing nothing at all, nothing in the
literature clears the convincing bar, nobody knows which one to pick, and nobody
has published on what happens when they go wrong.
