# consult modules -- completeness ledger, offer bounds, cooldown, contract, idempotency

read when: a module trigger fires (workout / diet / supp); before any module offer; when
consult_modules is missing or must be edited; before creating a routine / calendar /
measurement artifact. per-module execution: last section.

## Completeness ledger (consult_modules) + offer bounds

config key `consult_modules` (OQ-20): comma list of `<module>:<state>`; modules =
workout | diet | supp (fixed vocabulary; new modules at spec level only).
states:
- `pending` -- never completed; offerable when a trigger fires.
- `offered~k` -- offered k times without uptake (k = 1..2).
- `done@YYYY-MM-DD` -- completed.
- `declined@YYYY-MM-DD` -- explicitly declined, or auto from offered~2 (soft no).
- `declined@YYYY-MM-DD~r` -- WORKOUT ONLY (OQ-23 pin (b), dec-023 2026-07-15; spec v1.3
  4.2): the single 30-day cooldown re-offer has been MADE; terminal silence after (user
  request always opens). date stays the ORIGINAL decline date; ~r written ONLY when the
  offer actually goes out (a skipped offer does not burn it).

updates MERGE-only (item-level replace, never blind overwrite). seeded by `program-plan
next` on reading the wrap (and set workout -> done@ by program-plan `done`).
missing-key belt: consult_state=done but consult_modules absent -> reconstruct from
ARTIFACTS ONLY, config-set before acting:
- workout done iff program.yaml exists AND `program-init check` exits 0 (focus areas are
  on the card; a training time is optional -- all-day routine is a complete answer).
- diet done iff diet-guideline.md exists AND (a metric_log measurement OR a weigh-in
  cadence artifact; artifact lookup under the TITLE-DRIFT PIN below).
- supp done iff diet-guideline.md carries the MODULE STAMP MARKER
  `<!-- supp-module: done YYYY-MM-DD -->`. marker, not section-5 presence: section 5
  filled by the accrual lane must NOT reconstruct done (resource rows look the same as
  on-utterance accrual). honest residual: a pre-marker supp completion maps PENDING on key
  loss (bounded by re-offers; no supp module has ever run).
accepted residual: declined is NOT artifact-reconstructible; on key loss it revives as
PENDING (worst: two bounded offers, then auto re-decline). legacy consult_ops =
corroborating evidence only, never the sole predicate.

rules:
- DONE: never re-asked, never re-offered. re-entry on explicit request OR the revision
  R6 lane, as an EDIT (program-edit / guideline refresh), not a setup re-run; captured
  answers fast-confirm (record-first + restart rule).
- PENDING: offered only when an entry trigger fires. bounds (OQ-24, one pool with the
  1/day unsolicited-decision budget): max 1 module offer per day across ALL modules; only
  as a trailing single line in an otherwise decision-free reply at a user-initiated
  opening; NEVER a push. unanswered -> ~k+1; at ~2 auto-decline. budget-collision offers
  SKIPPED, not queued.
- DECLINED base (diet, supp): silent. reopened ONLY by (a) explicit request (opens
  directly) or (b) a program-need trigger of a DIFFERENT class than those declined -> ONE
  new offer, then back to declined. same-class re-fires never re-offer. no timers, no
  weekly-review re-offers (nagging is the failure mode).
- DECLINED WORKOUT -- cooldown (OQ-23 pin (b), dec-023; spec v1.3 4.3; REPLACES base for
  workout): after declined@D no offers of ANY kind until D+30 (different-class lane
  subsumed). from D+30 the FIRST qualifying program-need trigger of any class may carry ONE
  cooldown re-offer line (trailing, 1/day pool; a skipped one WAITS for the next trigger).
  making it rewrites declined@D -> declined@D~r same turn. at ~r: terminal silence; opens
  only on explicit request. why (owner): workout is the CORE domain; a silent two-strike
  decline would park the program / rx / progression / DGN-316 stack behind the F1 gate.
  today's-workout serving unaffected (reference/one-off-serving.md); inside the window or
  after ~r, NO trailing offer rides it.
- consult_ops: v2.4 natives never write it. instances mid-flight under v2.3.1 finish
  in-flight O-steps under the old grammar, then backfill (files/consult/retrofit-log.md);
  then frozen (legacy read only).

## common module contract

- precondition consult_state=done. trigger before the spine ran -> consult offer
  machinery instead; modules never run before ladder + safety rows exist.
- entry: (a) USER REQUEST opens directly, no offer, regardless of declined state;
  (b) PROGRAM-NEED -- a per-module detection rule fires while pending -> OFFER (one
  trailing line, bounds above). never forced, never a push.
- module questions: one topic, record-first, the module's own budget band. statements +
  mining reads cost 0.
- writes only through existing machinery: ledger verbs, config-set, main-session file
  writes, idempotency rule + title convention. one-writer invariant unchanged.
- partial run (session death): state stays pending / offered; next entry reconciles by
  artifact query + batch fast-confirm (reference/consult-conduct.md restart rule). no
  sub-state machinery.
- A4: plan is operationalizable on demand, complete PER MODULE at module completion; the
  completeness ledger carries the follow-through consult_ops used to.

## Idempotency rule (all modules)

before any artifact step, QUERY existing artifacts first (routines / appointments by title
convention, calendar blocks, recent metric_log rows). match -> reconcile (skip or update);
never blind-add.
title convention (creation key): training blocks = "운동 -- <split day>" (e.g. "운동 -- 앞A"),
weekly weigh-in = "측정 -- 주간 체중", start-point measurement = "측정 -- 시작점 (체중/인바디)".
new artifacts ALWAYS under this convention.
TITLE-DRIFT PIN (spec v1.3 3.0; read side only): every title lookup matches BOTH the
convention prefixes ("측정 -- " / "운동 -- ") AND the live legacy titles "체중측정" (weekly
weigh-in) and "헬스" (training). why: routine rows have no consult-ownership field, title is
the match key (verified 2026-07-15: convention "운동 -- ..." rows retired, active ones carry
legacy titles). NO retitling of live artifacts; a retitle is a separate owner ask.

## per-module execution

- workout (`workout`): workout-program SKILL.md routes each part -- reference/build-flow.md
  (stage map), reference/program-init.md, reference/one-off-serving.md,
  reference/program-edit.md. F1 gate, focus-vs-injury check (program-plan `emphasis`),
  volume-audit binding live where they execute.
- diet (`diet`) and supp (`supp`): NO execution home ships in this pack. the "consult diet
  module" (D1-D2 ledger, weigh-in scheduling, guideline sections, InBody intake O3) and
  "consult supp module" (P1-P3, stack capture, section 5 + stamp marker) sections this
  file used to point at were never carried into diet-status (0.8.0 carry-in; measured
  2026-09-26). on a diet / supp module trigger: do not improvise a D / P question ledger.
  what exists: body intake = kit `inbody-capture`; measurement cadence =
  diet-status reference/cadence-ask.md; daily target / card = diet-status SKILL.md. say plainly that
  the guided setup is not available yet.
