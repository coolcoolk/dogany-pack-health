---
# Kimwog warehouse #1. Frozen F2 contract (DGN-118) + v3 map + DGN-119
# applicability.axes. Authored 2026-10-06 (schedule/task-time sprint, dispatch
# kw-schedule-time). Task breakdown as an ESTIMATION aid. What was read:
# Wiese, Buehler & Griffin 2016 in full text (open access, JDM); Forsyth &
# Burt 2008 abstract (Europe PMC). Kruger & Evans 2004 was NOT retrievable
# (publisher 403, abstract elided in every index tried); its finding and
# position is carried only as Wiese et al. report it, and no number is taken
# from it. Wiese et al. call the unpacking evidence 'somewhat mixed' and
# attribute the three moderators to three different papers (Kruger & Evans
# 2004; Hadjichristidis, Summers & Thomas 2014; Moher 2012), none read here. Ariely & Wertenbroch 2002 (spaced deadlines) was checked and
# REFUSED: a failed replication (Hyndman & Bisin, Psychological Science,
# July 2026) and a retraction notice indexed September 2026 (PMID 42684323;
# the notice text was not retrievable, so no reason is asserted).
id: task-management/task-breakdown-unpacking-071
domain: task-management
grade: C (laboratory and student-project experiments; mixed results by the field's own account; the main unpacking paper read only through a secondary account)
lane: "@behavioral-productivity"
locale: universal
as_of: 2004-2026
contested: yes
sources:
  - "https://doi.org/10.1017/S1930297500007269"  # Wiese J, Buehler R, Griffin D. Backward planning: Effects of planning direction on predictions of task completion time. Judgment and Decision Making 2016;11(2):147-167. Full text read 2026-10-06. Study 4 (n=125 completed projects): backward planners predicted 2.82 days before deadline and finished 2.64 days before (bias .18 days, t(43)=.46, p=.65); forward planners predicted 3.91 and finished 1.98 (bias 1.93 days); unspecified 3.00 vs 1.79 (bias 1.21). Actual completion was SELF-REPORTED at follow-up. Also the source for the unpacking literature: 'somewhat mixed results' (Kruger & Evans effective; Byram 1997 and Connolly & Dean 1997 not), and the three moderators with their separate sources
  - "Kruger J, Evans M. If you don't want to be late, enumerate: Unpacking reduces the planning fallacy. Journal of Experimental Social Psychology 2004;40(5):586-598. doi:10.1016/j.jesp.2003.11.001. NOT READ (publisher refused retrieval; abstract elided). Carried only as reported by Wiese et al. 2016: unpacking reduced prediction bias; less effective with few components (Kruger & Evans), easy components (Hadjichristidis et al. 2014) or distant tasks (Moher 2012) -- the last two not read"
  - "https://doi.org/10.3758/MC.36.4.791"  # Forsyth DK, Burt CDB. Allocating time to future tasks: the effect of task segmentation on planning fallacy bias. Memory & Cognition 2008;36(4):791-798. Abstract read 2026-10-06: in three experiments the time allocated to a single task was significantly smaller than the summed allocations for its subtasks (the segmentation effect); rounding does not account for it. The abstract does not report actual completion times, so it shows estimates go UP, not that they become accurate
  - "https://doi.org/10.1037/a0025996"  # Halkjelsvik & Jorgensen 2012, abstract: task decomposition listed among the influences on performance-time predictions
  - "https://doi.org/10.1177/09567976261460772"  # Hyndman K, Bisin A. Replication of 'Procrastination, deadlines, and performance: Self-control by precommitment'. Psychological Science 2026;37:557-571. Abstract read: changes in deadlines had a negligible effect on performance; evenly spaced external deadlines did not stand out. REFUSAL source -- see refraction note 4
  - "https://doi.org/10.1177/09567976261488042"  # Retraction: Procrastination, deadlines, and performance: Self-control by precommitment. Psychological Science, September 2026 (PMID 42684323). Index record read; notice text not retrieved
  - "task-management/duration-from-logged-actuals-070"  # the per-subtask figure should come from logged actuals where they exist
  - "source:cooking/timeline-backward-pass-016 -- the same backward pass from a fixed end time, in the kitchen"
breakdown_rules:
  - rule: unpack-before-estimate
    value: for a multi-step task, ask for or draft the steps BEFORE asking for a total duration; total = sum of step estimates
    basis: Kruger & Evans 2004 as reported by Wiese 2016; Forsyth & Burt 2008 (sum of parts > whole); mixed results elsewhere (Byram 1997, Connolly & Dean 1997, via Wiese)
    basis_grade: C
  - rule: unpack-when
    value: worth the friction when the task has several components, some non-trivial, and starts soon; skip for one-step or easy tasks and for far-off tasks
    basis: moderators as reported by Wiese 2016 (Kruger & Evans 2004; Hadjichristidis et al. 2014; Moher 2012)
    basis_grade: C
  - rule: plan-backward-from-deadline
    value: for a task with a fixed due date, lay steps out from the due date backward and show the latest start for each step
    basis: Wiese 2016 Study 4 (only the backward group's prediction did not differ from its self-reported actual, in a real project)
    basis_grade: C
  - rule: step-is-a-scheduling-unit
    value: each step carries its own estimate, logged actual and done state; the parent is done when its steps are done
    basis: product rule; makes 070's capture-actual possible per step
    basis_grade: D
  - rule: no-step-count-target
    value: never prescribe a number of steps or a maximum step length
    basis: task-management/no-block-length-or-task-count-evidence-015
    basis_grade: D
  - rule: no-imposed-deadline-ladder
    value: do not generate evenly spaced intermediate deadlines as a procrastination cure; offer step due dates only when the owner asks
    basis: Ariely & Wertenbroch 2002 retracted 2026; failed replication 2026
    basis_grade: B
refraction_notes:
  - note: >
      BREAKDOWN RAISES THE ESTIMATE; WHETHER IT MAKES IT RIGHT IS LESS
      CERTAIN. The segmentation effect (Forsyth & Burt 2008) is that the sum
      of subtask allocations exceeds the allocation for the whole. Given the
      direction of the planning fallacy that is usually a move toward the
      truth, but this abstract does not measure actual times, and Kruger &
      Evans' accuracy finding is held here only through a secondary account.
    grade: C
  - note: >
      THE MODERATORS ARE THE USEFUL PART. As reported by Wiese et al.,
      unpacking helped less when a task had few components (Kruger & Evans),
      when the components were easy (Hadjichristidis et al. 2014), and when
      the task lay in the distant future (Moher 2012). Wiese et al. also call
      the unpacking evidence somewhat mixed: two earlier studies found
      similar strategies ineffective. Hence contested.
      So a module should not force breakdown on every item; it pays on
      near-term, many-part tasks.
    grade: C
  - note: >
      BACKWARD PLANNING IS ONE STUDY DEEP IN THE FIELD. Study 4 of Wiese et
      al. is a real project with recorded completion, and only the backward
      group's prediction did not differ from its actual. The actual
      completion times were self-reported at follow-up, not recorded by a
      third party. Studies 1-3 moved predictions without measuring
      accuracy. One research group, student samples, Canada.
    grade: C
  - note: >
      SPACED DEADLINES ARE REFUSED, NOT DOWNGRADED. The study usually cited
      for "set evenly spaced deadlines" (Ariely & Wertenbroch 2002) failed a
      2026 replication and carries a retraction notice dated September 2026.
      The reason for the retraction was not read; the item asserts only the
      fact of both events. No module rule may cite it.
    grade: B
claim: >
  Breaking a multi-step task into steps before estimating its duration raises
  the estimate, and with the right task it reduces the planning fallacy.
  Forsyth and Burt (2008) found in three experiments that people allocate
  less time to a task as a whole than the sum of what they allocate to its
  subtasks. Kruger and Evans (2004), as reported by Wiese, Buehler and Griffin
  (2016), found that unpacking reduced prediction bias, but less so when the
  task had few components, and other work places the same limit on easy
  components and on tasks far in the future; Wiese et al. call the
  unpacking evidence somewhat mixed. Wiese et al. (2016) found that planning steps
  backward from the deadline gave predictions that matched actual completion
  self-reported completion in a real student project (bias .18 days, not
  significant), while forward
  and unspecified planning stayed optimistic (1.93 and 1.21 days). The study
  usually cited for imposing evenly spaced deadlines (Ariely and Wertenbroch
  2002) failed a 2026 replication and was retracted in September 2026, and is
  not used.
reasoning: >
  Third band under task-management/curator-checklist-016. The experiments are
  real manipulations with measured outcomes, but the central unpacking paper
  could not be read, the segmentation abstract measures allocations only, the
  field's own summary calls the unpacking results mixed, and the
  backward-planning accuracy result rests on one study in one group with
  self-reported completion.
  The direction is consistent across all three and with items 001 and 070,
  which is what keeps it in C rather than D. The retraction refusal is
  carried at B because the replication abstract and the retraction index
  record were both read at source; it is a fact about the literature, not a
  behavioural claim. Rules are structured for the lifekit schedule/task
  module; the step-as-unit rule is product design and labelled D.
---

# task-management/task-breakdown-unpacking-071

Breaking a task into steps is mainly a way to estimate it better. It is not a
cure for procrastination.

- People give a whole task less time than the sum they give its parts. Forsyth
  and Burt (2008) found this in three experiments and called it the
  segmentation effect.
- Kruger and Evans (2004) found that listing the steps reduced the planning
  fallacy, though two earlier studies found similar strategies did not
  work. Later studies report it helps less for tasks with few parts, easy
  parts, or a start far in the future. None of these papers could be
  retrieved, so all of this is carried as Wiese, Buehler and Griffin (2016)
  report it.
- Wiese et al. (2016) had students plan a real project either backward from
  the deadline or forward from today. Backward planners predicted finishing
  2.82 days early and finished 2.64 days early. Forward planners predicted
  3.91 days and managed 1.98. Finish dates were reported by the students
  themselves.

What is refused: the popular advice to set evenly spaced intermediate
deadlines usually cites Ariely and Wertenbroch (2002). A 2026 replication found
deadlines had a negligible effect, and a retraction notice was indexed in
September 2026. This item does not give a reason for the retraction because
the notice was not read.

## Rules for the schedule/task module (frontmatter `breakdown_rules`)

| Rule | What the module does | Basis |
|---|---|---|
| unpack-before-estimate | get the steps first, total = sum of steps | Kruger & Evans via Wiese; Forsyth & Burt |
| unpack-when | many parts, non-trivial, starting soon; skip otherwise | moderators via Wiese |
| plan-backward-from-deadline | fixed due date: lay steps backward, show latest start per step | Wiese 2016 Study 4 |
| step-is-a-scheduling-unit | each step has estimate, actual, done; parent done when steps done | product rule |
| no-step-count-target | no prescribed number or size of steps | 015 |
| no-imposed-deadline-ladder | no auto-generated spaced deadlines as a cure | retraction 2026 |

## 한국어 요약 (답변용)

- 할 일을 단계로 나누는 건 주로 시간을 더 정확히 잡기 위한 것이다. 통째로 잡은 시간보다 단계별
  시간의 합이 더 크게 나오고, 보통 그쪽이 실제에 가깝다.
- 단계가 여러 개이고 쉽지 않으며 곧 시작할 일에 효과가 있다. 한 단계짜리이거나 쉬운 일, 먼 미래의
  일은 굳이 나누지 않는다.
- 마감이 정해진 일은 마감일부터 거꾸로 단계를 배치하고, 단계마다 늦어도 언제 시작해야 하는지
  보여 준다. 실제 과제에서 이렇게 했을 때 예측과 실제가 맞았다(한 연구, 캐나다 학생, 완료일은
  학생 본인 보고).
- 나누기의 효과는 연구마다 엇갈린다. 효과가 없었다는 연구도 있다.
- 단계 수나 단계 길이의 정답은 없다.
- "중간 마감을 고르게 잘게 정하라"는 조언의 근거 논문은 2026년 재현에 실패했고 철회됐다. 이걸
  근거로 중간 마감을 자동으로 만들지 않는다. 사용자가 원할 때만 단계별 기한을 둔다.
