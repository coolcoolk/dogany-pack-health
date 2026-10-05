#!/bin/bash
# health-install-ensure.sh -- pack_health's INSTALL-COMPLETION LANE.
#
# Runs the post-install steps this pack ships but that nothing was calling, and
# runs them from code rather than from a sentence in a README. Idempotent,
# cheap when already done, and it NEVER fails its caller.
#
# It carries THREE steps today:
#   1. the taxonomy seed (service/health/health_taxonomy_seed.py) -- DOES the
#      work, because the rows are the pack's own product knowledge;
#   2. the program card + its rotation registry (service/health/program-init)
#      -- REPORTS, because the content is the owner's and no lane may invent
#      it. See "TWO KINDS OF STEP" below: the difference is not an oversight.
#   3. the DOMAIN ONBOARDING verdict (service/health/onboarding-gate) --
#      REPORTS, for the same reason step 2 does and one rung earlier: step 2
#      says the card is missing, step 3 says whether the owner was ever ASKED.
#      Added 2026-09-15, because on a fresh mint an absent card is not an
#      install defect -- it is a question nobody put to him. This is also the
#      one place in this pack where the onboarding verdict is computed by CODE
#      THAT ACTUALLY RUNS on every session birth (session-ensure.sh calls this
#      lane), so an offer that never happened leaves a line in the log instead
#      of leaving nothing at all.
#
# WHY THIS FILE EXISTS (2026-09-14)
#   The pack shipped health_taxonomy_seed.{py,sql} -- 386 rows of taxonomy that
#   every weight the engine prints depends on -- and NOTHING RAN IT. Measured
#   on the 2026-09-13 fresh-mint simulation: `grep -rn health_taxonomy_seed`
#   across the framework's scripts/ returned nothing, and the only in-instance
#   mentions were two SKILL.md sentences calling it "설치 직후 한 번 수동으로
#   돌리는 시드". A fresh DB held 0 rows in all eleven seeded tables. That is
#   the same defect class the whole 2026-09-12 audit was written about --
#   shipping a thing and calling it delivered -- applied to the seed itself.
#
# WHY IT IS A ROUTINE AND NOT A pack_install.sh STEP -- MEASURED, NOT ASSUMED
#   The framework's kind=pack install pipeline has NO post-install execution
#   hook of any kind. Measured 2026-09-14 against dogany-agent @ 34d78c92:
#   pack_install.sh's behavior-pack profile runs service_facade / skills-bundle
#   / routines-bundle / config-merge / knowledge-warehouse / deps-provision /
#   agent_md_fragment / DOGANY_PACKS upsert -- all file-copy lanes. The one
#   step that looks like a hook, `domain_seed` (step 8), is not one: it is a
#   hardcoded write of config.consult_state into database/lifekit.db. And
#   `capabilities.schedules` (the plist lane) is BLOCKED for kind=pack by
#   DGN-1402, so a launchd unit is not available either.
#   Adding a real hook is framework machinery and is the framework's call, not this
#   pack's. It is escalated separately. What this pack CAN own is the earliest
#   code that runs inside its own installed tree -- which is this lane, called
#   from session-ensure.sh, the gate every session birth already goes through.
#
# THE BACKSTOP STAYS. session-open still probes the taxonomy itself and prints
# its `install incomplete:` banner when the seed has not run. This lane is not
# allowed to become the only guard: if it is skipped, misconfigured, or the DB
# is replaced underneath it, the owner still gets told at the moment it matters.
# Two independent guards, one of them loud.
#
# TWO KINDS OF STEP, AND WHY STEP 2 DOES NOT WRITE (2026-09-14, D1)
#   The taxonomy seed is PACK CONTENT: 386 rows of movement/muscle/grip facts
#   the pack authored and ships. A lane may apply it unattended because nothing
#   in it is a statement about this owner.
#   files/program/program.yaml is the opposite: it is the owner's split, his
#   lifts, his weights. A lane that generated one would be the pack deciding
#   his training -- and a plausible generated program is WORSE than no program,
#   because session-open would open it and rx-calc would prescribe from it and
#   nothing anywhere would say the numbers were invented. So step 2 runs the
#   verdict (`program-init check`) and names the command that builds the card
#   WITH him. It reports; it never authors.
#   The one thing it DOES write is the derived half: when a card exists but the
#   session_type registry has drifted from its `rotation:` list, the lane runs
#   `program-init sync`. That is not owner content -- it is the same list,
#   re-expressed as rows, and the file is its only source.
#
# Usage:
#   health-install-ensure.sh [--dry-run] [--quiet]
#     --dry-run  report what is unmet; write nothing
#     --quiet    suppress the "already complete" line (still reports work/fail)
#
# stdout: one line per step.
#   TAXONOMY<TAB>ok<TAB><n> rows seeded       the seed ran here, now
#   TAXONOMY<TAB>present                      already seeded; nothing to do
#   TAXONOMY<TAB>unmet<TAB><reason>           --dry-run, or the seed refused
#   TAXONOMY<TAB>skipped<TAB><reason>         no DB / no runner: not this
#                                             lane's failure to report
#   PROGRAM<TAB>present                       card + registry both complete
#   PROGRAM<TAB>unmet<TAB>absent               no card: the owner has not been
#                                             asked yet. Names the command.
#   PROGRAM<TAB>unmet<TAB>invalid              a card exists and does not pass
#                                             its own contract
#   PROGRAM<TAB>synced<TAB><detail>            card fine, registry had drifted
#                                             and was re-derived here
#   PROGRAM<TAB>unmet<TAB>sync-failed<TAB>...  the re-derivation did not take
#   PROGRAM<TAB>skipped<TAB><reason>           no runner / no DB
#   ONBOARDING<TAB>outstanding<TAB><reason>   identity onboarding is finished
#                                             and the owner has NOT been walked
#                                             through the domain interview yet
#   ONBOARDING<TAB>held<TAB><reason>          identity onboarding has not
#                                             finished; the domain must wait
#   ONBOARDING<TAB>complete                   he answered; nothing to offer
#   ONBOARDING<TAB>passive<TAB>declined-exhausted  he declined twice; passive
#   ONBOARDING<TAB>skipped<TAB><reason>       no runner: not this lane's
#                                             failure to report
# Exit: 0 ALWAYS. This lane reports; it never gates. A caller that wants a
#       verdict runs `health_taxonomy_seed.py --check` or
#       `program-init check` (both exit 0 ok / 3 unmet) directly.
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

DRY=0
QUIET=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY=1 ;;
    --quiet)   QUIET=1 ;;
    *) echo "health-install-ensure: unknown argument: $arg" >&2 ;;
  esac
done

# Root probe: identical to session-ensure.sh's (this file installs beside it, at
# routines/bundle/, i.e. TWO levels below the instance root -- do not count
# levels, probe).
if [[ -n "${PROJECT_ROOT:-}" && -d "$PROJECT_ROOT/database" && -d "$PROJECT_ROOT/service" ]]; then
  ROOT="$PROJECT_ROOT"
else
  ROOT=""
  for _up in ".." "../.."; do
    _cand="$(cd "$SCRIPT_DIR/$_up" && pwd)"
    if [[ -d "$_cand/database" && -d "$_cand/service" ]]; then ROOT="$_cand"; break; fi
  done
  [[ -n "$ROOT" ]] || ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
fi

SEED_PY="$ROOT/service/health/health_taxonomy_seed.py"
PROGRAM_INIT="$ROOT/service/health/program-init"
ONBOARDING_GATE="$ROOT/service/health/onboarding-gate"
DB="$ROOT/database/kit_life.db"

# PYTHON: the same resolution kit_life.sh uses, with one correction measured on
# 2026-09-13 -- Apple's /usr/bin/python3 (3.9.6) cannot tokenize kit_life.py's
# long history lines and dies with a bogus "Non-UTF-8 code" SyntaxError. Prefer
# an explicit LIFEKIT_PYTHON, then homebrew, then PATH.
PY="${LIFEKIT_PYTHON:-}"
if [[ -z "$PY" ]]; then
  if [[ -x /opt/homebrew/bin/python3 ]]; then PY=/opt/homebrew/bin/python3
  else PY="$(command -v python3 || true)"; fi
fi

# EACH STEP IS A FUNCTION THAT RETURNS (2026-09-14). It used to be one straight
# run of `exit 0`s, which was correct while there was one step and becomes a
# silent truncation the moment there are two: step 1 taking its "nothing to do"
# exit would have skipped step 2 entirely and printed nothing about it. A lane
# that reports on some of its steps depending on how the earlier ones went is
# the reporting defect this lane exists to close, one level up.

taxonomy_step() {
  if [[ ! -f "$SEED_PY" ]]; then
    printf 'TAXONOMY\tskipped\tseed runner absent at %s\n' "$SEED_PY"
    return 0
  fi
  # -e, not -f: database/kit_life.db is a SYMLINK into the crew-shared DB on a
  # normal mint (DGN-1436), and -f follows it only when the target exists.
  if [[ ! -e "$DB" ]]; then
    printf 'TAXONOMY\tskipped\tno kit_life.db at %s (kit not installed yet)\n' "$DB"
    return 0
  fi

  # --check: exit 0 complete / 3 missing seed rows / 1 error. Its stdout is
  # the per-table report, which belongs in a diagnostic run, not in a session-birth log -- so it
  # is captured and only re-emitted when it is the thing that went wrong.
  local CHECK_OUT CHECK_RC APPLY_OUT APPLY_RC INSERTED
  CHECK_OUT="$("$PY" "$SEED_PY" --db "$DB" --check 2>&1)"
  CHECK_RC=$?

  if [[ "$CHECK_RC" -eq 0 ]]; then
    [[ "$QUIET" -eq 1 ]] || printf 'TAXONOMY\tpresent\n'
    return 0
  fi
  if [[ "$CHECK_RC" -ne 3 ]]; then
    printf 'TAXONOMY\tskipped\t--check errored (rc=%s)\n' "$CHECK_RC"
    printf '%s\n' "$CHECK_OUT" >&2
    return 0
  fi

  if [[ "$DRY" -eq 1 ]]; then
    printf 'TAXONOMY\tunmet\tseed rows missing on %s\n' "$DB"
    printf '%s\n' "$CHECK_OUT" >&2
    return 0
  fi

  # The write. --apply is transactional in the runner: a FK violation or a refused
  # statement rolls the whole thing back and exits non-zero, so a partial seed is
  # not a state this can produce.
  APPLY_OUT="$("$PY" "$SEED_PY" --db "$DB" --apply 2>&1)"
  APPLY_RC=$?
  if [[ "$APPLY_RC" -ne 0 ]]; then
    printf 'TAXONOMY\tunmet\tseed --apply failed (rc=%s) -- session-open will name it again\n' "$APPLY_RC"
    printf '%s\n' "$APPLY_OUT" >&2
    return 0
  fi
  INSERTED="$(printf '%s\n' "$APPLY_OUT" | awk '$1=="TOTAL" {print $2; exit}')"

  # RE-CHECK AFTER THE WRITE -- the verdict is MEASURED, never inferred from
  # "--apply exited 0". Found by the probe-honesty run on 2026-09-14: against a
  # tree whose seed file was missing its ax_exercise block, --apply legitimately
  # succeeded (+370 of the 370 statements it had) and this lane reported
  # `TAXONOMY ok` over a DB that --check calls PARTIAL. A lane that says "done"
  # while the install is incomplete is the exact defect class this lane exists to
  # close, so it asks the same question again and answers with what it gets back.
  if "$PY" "$SEED_PY" --db "$DB" --check >/dev/null 2>&1; then
    printf 'TAXONOMY\tok\t%s\n' "${INSERTED:-applied}"
  else
    printf 'TAXONOMY\tunmet\tseed ran (%s) but the DB is STILL not fully seeded -- the seed file itself is incomplete. session-open will name it again\n' "${INSERTED:-applied}"
    "$PY" "$SEED_PY" --db "$DB" --check >&2 2>&1 || true
  fi
  # The seed's own stderr (the pre-049 owning_agent warning, if any) has already
  # been merged into APPLY_OUT; re-emit it so the operator sees it rather than
  # only the row count.
  printf '%s\n' "$APPLY_OUT" >&2
  return 0
}

# ---- step 2: the program card + the rotation registry it implies ------------
# REPORTS the card, DERIVES the registry. See "TWO KINDS OF STEP" in the header
# for why those are different verbs and why the difference is deliberate.
#
# `program-init check` exit codes: 0 card valid AND registry complete /
# 2 card present but INVALID / 3 unmet (absent card, or a registry that does not
# carry every code the card declares) / 1 environment error. This lane maps them
# and, for the one case it is allowed to fix, fixes it.
program_step() {
  if [[ ! -x "$PROGRAM_INIT" ]]; then
    printf 'PROGRAM\tskipped\tprogram-init absent or not executable at %s\n' "$PROGRAM_INIT"
    return 0
  fi
  if [[ ! -e "$DB" ]]; then
    printf 'PROGRAM\tskipped\tno kit_life.db at %s (kit not installed yet)\n' "$DB"
    return 0
  fi
  local OUT RC SYNC_OUT SYNC_RC
  OUT="$("$PY" "$PROGRAM_INIT" check --db "$DB" 2>&1)"
  RC=$?
  case "$RC" in
    0)
      [[ "$QUIET" -eq 1 ]] || printf 'PROGRAM\tpresent\n'
      return 0
      ;;
    2)
      # A card exists and does not pass its own contract. NOT this lane's to
      # repair: rewriting it would overwrite training the owner may be running
      # on. Name it and hand it to the skill that owns program.yaml structure.
      printf 'PROGRAM\tunmet\tinvalid\n'
      printf '%s\n' "$OUT" >&2
      printf 'health-install-ensure: files/program/program.yaml exists but fails its own contract. Fix with the owner (workout-program owns structure writes); `service/health/program-init validate` names every error.\n' >&2
      return 0
      ;;
    3) : ;;
    *)
      printf 'PROGRAM\tskipped\tcheck errored (rc=%s)\n' "$RC"
      printf '%s\n' "$OUT" >&2
      return 0
      ;;
  esac
  # rc=3. Two different unmet states and they need different verbs.
  if printf '%s\n' "$OUT" | grep -q '^PROGRAM	unmet	absent'; then
    printf 'PROGRAM\tunmet\tabsent\n'
    printf 'health-install-ensure: files/program/program.yaml does not exist, so NO SESSION CAN OPEN (session-open exits 1). It is the owner'"'"'s own training card and nothing ships one -- it is built WITH him:\n  service/health/program-init next\nThe last answer writes the card and derives the session_type rotation rows in the same call. Do NOT author one for him.\n' >&2
    return 0
  fi
  # The card is valid and the registry has drifted from its `rotation:` list.
  # Deriving the same list again is not owner content, so this one the lane does.
  if [[ "$DRY" -eq 1 ]]; then
    printf 'PROGRAM\tunmet\tregistry-drift (dry-run: not synced)\n'
    printf '%s\n' "$OUT" >&2
    return 0
  fi
  SYNC_OUT="$("$PY" "$PROGRAM_INIT" sync --db "$DB" 2>&1)"
  SYNC_RC=$?
  if [[ "$SYNC_RC" -ne 0 ]]; then
    printf 'PROGRAM\tunmet\tsync-failed\trc=%s -- session-open will name it again\n' "$SYNC_RC"
    printf '%s\n' "$SYNC_OUT" >&2
    return 0
  fi
  # RE-CHECK, for the same reason the taxonomy step re-checks: a verdict is
  # measured, not inferred from the writer's exit code.
  if "$PY" "$PROGRAM_INIT" check --db "$DB" >/dev/null 2>&1; then
    printf 'PROGRAM\tsynced\t%s\n' "$(printf '%s\n' "$SYNC_OUT" | awk -F'\t' '$1=="SYNC"{print $3"/"$4; exit}')"
  else
    printf 'PROGRAM\tunmet\tsync ran but the registry is STILL incomplete -- session-open will name it again\n'
    "$PY" "$PROGRAM_INIT" check --db "$DB" >&2 2>&1 || true
  fi
  return 0
}

# ---- step 3: has the owner been ASKED yet? ----------------------------------
# REPORTS ONLY, and it holds the same D1 line step 2 holds one rung lower: this
# lane may not interview him and may not treat an unasked question as answered.
# It runs the gate and prints what the gate says.
#
# `onboarding-gate verdict` exit codes: 0 OFFER (outstanding) / 3 NO-OFFER (the
# reason names which: identity-pending / identity-absent / complete /
# declined-exhausted) / 1 environment error.
#
# WHY IT IS HERE AND WHAT IT DOES NOT CLAIM. The health-onboarding skill FIRES
# on a description match, because this pack cannot register a Claude Code hook
# -- measured, not assumed: the behavior-pack install profile returns before the
# legacy hook-wiring lane (which is hardcoded to one filename anyway),
# compat-lint C4 refuses any routines/<non-bundle> path, and
# capabilities.schedules is blocked for kind=pack. So the OFFER cannot be made
# from code. What CAN be made from code is the RECORD that it was outstanding,
# on every session birth -- which turns a missed offer into a line a reader can
# find instead of a silence nobody can measure.
onboarding_step() {
  if [[ ! -f "$ONBOARDING_GATE" ]]; then
    printf 'ONBOARDING\tskipped\tonboarding-gate absent at %s\n' "$ONBOARDING_GATE"
    return 0
  fi
  local OUT RC REASON
  OUT="$("$PY" "$ONBOARDING_GATE" verdict --root "$ROOT" --db "$DB" 2>/dev/null)"
  RC=$?
  REASON="$(printf '%s\n' "$OUT" | awk -F'\t' '$1=="VERDICT"{print $3; exit}')"
  case "$RC" in
    0)
      printf 'ONBOARDING\toutstanding\t%s\n' "${REASON:-unknown}"
      printf 'health-install-ensure: identity onboarding is finished and the owner has never been walked through the DOMAIN interview (goal / body state / injuries / split). Nothing here may run it for him and nothing may author a program: the entry is the health-onboarding skill, which routes to the existing consult spine and lets service/health/program-init do the write.\n' >&2
      ;;
    3)
      case "$REASON" in
        complete)            [[ "$QUIET" -eq 1 ]] || printf 'ONBOARDING\tcomplete\n' ;;
        declined-exhausted)  printf 'ONBOARDING\tpassive\t%s\n' "$REASON" ;;
        *)                   printf 'ONBOARDING\theld\t%s\n' "${REASON:-unknown}" ;;
      esac
      ;;
    *)
      printf 'ONBOARDING\tskipped\tverdict errored (rc=%s)\n' "$RC"
      printf '%s\n' "$OUT" >&2
      ;;
  esac
  return 0
}

if [[ -z "$PY" || ! -x "$PY" ]]; then
  printf 'TAXONOMY\tskipped\tno python3 interpreter found\n'
  printf 'PROGRAM\tskipped\tno python3 interpreter found\n'
  printf 'ONBOARDING\tskipped\tno python3 interpreter found\n'
  exit 0
fi

taxonomy_step
program_step
onboarding_step
exit 0
