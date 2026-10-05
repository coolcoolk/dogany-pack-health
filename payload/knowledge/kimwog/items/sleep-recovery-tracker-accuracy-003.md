---
# Converted from batch2-sleep-productivity.raw.json finding [11] (consumer
# sleep-tracker accuracy, vote 3-0). Rubric: sleep-recovery.rubric.md @clinical
# row sleep-recovery/tracker-accuracy-003. Red-flag override WITHIN the lane
# (not a separate lane) per v3.
id: sleep-recovery/tracker-accuracy-003
domain: sleep-recovery
grade: A (tracker-limitation finding)
lane: "@clinical"
locale: universal
as_of: 2023
contested: no
sources:
  - "https://mhealth.jmir.org/2023/1/e50983"  # JMIR mHealth multicenter PSG validation, 11 devices (batch2 3-0)
  - "2024 JCSM meta-analysis (reinforcing)"
  - "2024 JMIR systematic review (reinforcing)"
  - "framework:GRADE -- red-flag override: tracker-derived numbers are NOT high-certainty"
refraction_notes:
  - note: >
      Red-flag override WITHIN the clinical lane: do NOT treat any consumer
      sleep-tracker-derived number as high-certainty. Device accuracy varies
      widely vs polysomnography (macro F1 0.26-0.69). This is a within-lane
      override, not a separate lane.
    grade: A
claim: >
  Consumer sleep-tracker accuracy cannot be assumed uniform or high: across 11
  consumer trackers validated against polysomnography, macro F1 ranged from 0.69
  (best) down to 0.26 (worst). Tracker-derived sleep numbers must not be treated
  as high-certainty measurements.
reasoning: >
  From the JMIR mHealth prospective multicenter validation (349,114 epochs, 11
  devices) against gold-standard polysomnography, reinforced by a 2024 JCSM
  meta-analysis and a 2024 JMIR systematic review. The FINDING itself (accuracy
  varies widely) is high-certainty and graded A; its function is a red-flag
  override on tracker-derived claims. Per v3 this is a within-lane override, not a
  separate lane -- the clinical lane simply refuses to treat tracker numbers as
  high-certainty.
---

# sleep-recovery/tracker-accuracy-003

Consumer sleep trackers vary enormously in accuracy against clinical
polysomnography -- from decent to poor -- so a number off a wearable is not a
high-certainty measurement. The finding that accuracy is non-uniform is itself
well-established; the takeaway is caution about the numbers, not distrust of the
finding.

This is a red-flag override that lives inside the clinical lane rather than
forming its own lane: when a claim rests on tracker-derived data, the answer path
hedges the specific numbers even though the domain otherwise reaches a real top
tier.
