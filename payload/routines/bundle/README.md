# payload/routines/bundle -- pack-owned routine surface

Installs to `<instance>/routines/bundle/`. Anything here is PACK-OWNED and is
replaced on reinstall.

`<instance>/routines/` (the level above) is INSTANCE-OWNED and is never written
by the installer. A routine that lives there is not shipped, and copying it here
without moving its call sites produces a second copy nobody invokes.

## what belongs here

A routine belongs here when it is true for any user who installs this pack --
the routine's DEFINITION. What that user then configures about it (time,
on/off, target) stays instance-side.

## what is here

- `tool-output-filter-gate.py` (PreToolUse, 0.36.0) -- refuses a Bash call that
  pipes a pack in-session CLI (set-add, set-arm, exercise-enter, ...) through
  grep/head/sed/... or sends its stdout to /dev/null: that stdout is the reply
  contract (review of a live session, 2026-10-08). Fail-open.

- `session-ensure.sh` -- idempotent "today's health-session task exists" gate.
  Drives `service/health/session-open` first, then the kit_life task gate.
  Its only caller is this pack's own `workout-session/SKILL.md`
  (`bash routines/bundle/session-ensure.sh`), which moved in the same commit --
  that is what makes it shippable rather than a second copy nobody invokes.
  It was carried out of the retired instance-local tree on 2026-09-12 and
  REPATHED on the way in. It used to resolve the root one level up; from
  `bundle/` that is `<instance>/routines`, so it now probes for `database/` +
  `service/` instead of counting levels.

- `health-install-ensure.sh` -- the install-completion lane. Three steps: it
  SEEDS the taxonomy (pack content), REPORTS the program card + syncs only its
  derived registry (owner content -- D1), and REPORTS the domain-onboarding
  verdict (`service/health/onboarding-gate`). Its caller is `session-ensure.sh`,
  so it runs on every session birth. That is also why the onboarding verdict
  lives here: the `health-onboarding` skill FIRES on a description match (this
  pack cannot register a hook), and this lane is the only code that runs
  unconditionally, so an offer that was never made still leaves a line
  (`ONBOARDING outstanding <reason>`) instead of leaving a silence.

- `domain-onboarding-check.py` (SessionStart), `domain-onboarding-prompt.py`
  (UserPromptSubmit, 0.17.2) and `domain-onboarding-stop.py` (Stop, LOG-ONLY
  since 0.17.1) -- the three callers of `service/health/onboarding-gate`,
  declared in the manifest `hooks[]` and wired by pack_install into
  `.claude/settings.local.json`. The prompt leg fires once, on the owner's
  next message, when identity is done and goal onboarding was never offered.
  `domain-onboarding-check.py` is also the wrapper the manifest
  `post_mint_next` slot names for the framework's inline continuation check.

- `session-progress-inject.py` (UserPromptSubmit, 2026-09-30) -- the declared
  entry point for the live-session progress injection. It runs
  `service/health/session_harness/hooks/turn_pre.py` in place (C-HOOKS only
  admits `routines/bundle/` paths). While `.active-session` names a session,
  every owner message gets the `session-cursor resolve` block (current slot,
  done/next set, whole-day `day_progress`) plus the owner's 2026-09-30 ruling
  (loads on judgment, reorder asks first). In the same envelope, the
  question-close carrier (`session_harness/hooks/question_close.py`) carries the
  owner's previous question when the reply did not visibly address it. No
  session = zero bytes. Declared in the manifest `hooks[]` and in
  `domain-onboarding-wire.sh`.

- `hk-ingest.sh` -- the HealthKit ingest routine (engine:
  `service/health/hk-ingest`, transporter client:
  `service/health/transporter_mcp.py`, mapping data:
  `service/health/hk_activity_map.tsv`). Three callers, one engine:
  two scheduled passes, activated through routine-ctl, never auto-scheduled --
  `routine-ctl.sh enable hk-ingest-early routines/bundle/hk-ingest.sh 04:50`
  and `routine-ctl.sh enable hk-ingest-morning routines/bundle/hk-ingest.sh 09:00`
  -- plus the Transporter receiver's `callback` (`config.json`, instance-side:
  `<root>/routines/bundle/hk-ingest.sh --callback`), which pipes
  `{"source","kind","id"}` once per NEW id; the engine filters at entry and
  only healthkit/workout goes further. Updates to an id never call back, so
  every pass re-reads a date window (`HK_INGEST_WINDOW_DAYS`, default 3).
  Writes go through the kit facade only (`workout-add --new`, `workout-upd`,
  `log-metric`, `ingest-check`, `ingest-put`, `metric-register`); kit tables are READ
  read-only in-process (the fatigue-brief idiom). Dedupe is the kit ingest
  ledger (`ingest_ref`): on a kit without `ingest-get` the pass exits 2 and
  writes nothing. Health onboarding calls `hk-ingest consent KIND [KIND ...]`
  only for kinds the user approved. That invokes `kit_life.sh ingest-consent
  healthkit KIND --module health` for each kind and starts ingestion at the
  kit's `floor=` approval time. `hk-ingest revoke KIND [KIND ...]` invokes
  `ingest-consent healthkit KIND --off --module health`. Kinds are `workout`,
  `steps`, `heart_rate`, `resting_heart_rate`, `sleep`, and
  `active_energy_day`. The onboarding question itself is pending owner review.
  An unapproved or revoked kind is skipped; pre-approval events are never
  imported. The first active energy day is the day after approval. Optional
  `HK_INGEST_REFRESH=on` wakes the phone before a pass (off by default: it
  is a push to the owner's phone). `HK_TRANSPORTER_MCP` overrides the server
  command (default `~/.transporter/venv/bin/transporter-mcp`).
  Requires kit migration 057 for consent, ingest ledger, and module metric
  registration. `resting_hr_bpm` and `hr_avg_bpm` register with unit `bpm`.

## retired: the standalone 05:00 prescription push (0.30.0)

The old rx-gen routine (DGN-301) pushed the day's prescription on its own at
05:00. It is gone, folded into the health agent's morning brief: the session
is the `오늘 운동` line of the kit's domain morning card
(`service/health/health-brief`, retro-sections lane `morning`), sent 30
minutes before the earliest weekly training start, so the morning has one
health contact, not two. Verified before deleting (2026-10-02): the live
health instance carried the file in `routines/bundle/` but had no launchd unit
for it, and its gated push path (a framework gate script, its library and a
trigger registry) was never installed -- on this instance it could only have
exited 127. Nothing was lost in delivery.

What it also carried, and what still has no scheduled carrier: its close-out
gate ran `session-closeout --check` (the "close the last session first" nag)
and then `session-closeout --sweep` (the cron's one full-mode reach). Neither
fit a provider -- providers are read-only. Both modes stay in
`service/health/session-closeout` and are tested there; a scheduled caller is
an open follow-up (it was not running on the live instance either).

The health-retro the kit's daily retro used to carry is the domain daily
glance card now (`service/health/session-retro`, lane `daily`).

## what has NO slot (do not force it here)

`card-followup.py` is health-domain but is wired as a Claude Code hook by
absolute path in `<instance>/.claude/settings.json` (the framework template
ships and registers it). `goal-entry-gate.py` used to sit here too; since the
manifest `hooks[]` lane exists (pack_install.sh _hooks_wire), it ships in this
directory and is registered from the manifest like the domain-onboarding legs
(2026-09-30). The health libraries under `<instance>/routines/lib/`
(`health_metrics.py`, `health_dashboard.py`, `muscle_taxonomy.py`,
`purpose_gate.py`) still have no slot: their importers resolve
`routines/lib/`, not `routines/bundle/lib/`.
