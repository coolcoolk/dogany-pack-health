#!/bin/bash
# session-ensure.sh -- idempotent "ensure today's health-session task exists".
#
# Called when the owner commits to / starts a workout session (S2). Guarantees
# exactly one OPEN session task for the day, titled "헬스 - <split>" (or plain
# "헬스" when no split is known). Reconcile-before-write: never creates a dup.
#
# Usage:
#   session-ensure.sh [YYYY-MM-DD] [split_code]
#     date defaults to today (KST); split_code optional (else planned next split).
#
# SESSION BIRTH (2026-08-26). This script is also the CODE CARRIER for
# `files/program/session-open`. Until now session-open had ZERO code callers:
# the instruction to run it lived only in workout-session/SKILL.md prose
# (~L91, L816-822, L1309-1316, L1664), and prose is not a caller. The measured
# cost is on disk -- sessions 10090 (08-22), 10091 (08-24) and 10092 (08-25)
# have NO "헬스" timeblock at all, because neither this gate nor session-open
# was ever actually run on those days. `routines/session-gate.py` is a test
# harness, not a caller.
#
# Same discipline session-closeout already applies with close_day_timeblock:
# "CODE decides, not the model". The session task and the session ROW are one
# event, so they get one carrier. session-open is idempotent (re-running it on
# the same day returns the existing session, never duplicates or clobbers a
# tag) and best-effort, so driving it here cannot make this gate worse.
#
# ORDERING: session-open runs FIRST, before the kit_life task gate. A missing
# task CLI must not be able to suppress the session ROW -- the row is the thing
# every set-add later hangs off, the task is calendar bookkeeping.
#
# RE-ENTRANCY: WARG_SESSION_OPEN_CHAIN is the chain flag for this pair, read by
# the same `set means someone else owns this edge` rule as
# LIFEKIT_SESSION_CLOSE_CHAIN. Set it before calling this script from anything
# that session-open itself drives. Asserted in
# tests/test-session-lifecycle-wiring.py (the close-chain flag went unasserted
# for a day and that is how this class of defect survives).
#
# INSTALL COMPLETION RUNS FIRST (2026-09-14). Before session birth, this gate
# drives routines/bundle/health-install-ensure.sh -- the pack's install-
# completion lane, which seeds the health taxonomy if it has not been seeded.
# It is here because a kind=pack install has no post-install execution hook at
# all (measured; see that script's header), so the earliest code this pack owns
# on a fresh instance is the gate the owner's first "운동 시작" already reaches.
# Ordering is load-bearing: session-open READS the taxonomy to decide whether to
# print its install-incomplete banner, so seeding after it would leave the first
# session of an instance's life reporting a gap that had just been closed.
# The banner is NOT replaced -- it is the backstop for every path that does not
# come through here.
#
# stdout:
#   FREE<TAB><session_id>          a free session is open: the ONLY line, nothing
#                                  else ran (no session-open, no task, no sweep)
#   TAXONOMY<TAB>...               install-completion lane (first line; see
#                                  health-install-ensure.sh for the shapes)
#   OPENED<TAB><session_id>        session row opened/confirmed (first line,
#                                  omitted when session-open is unavailable,
#                                  skipped by the chain flag, or fails)
#   EXISTS<TAB><id><TAB><title>    an open session task already exists for DAY
#   CREATED<TAB><id><TAB><title>   a new session task was created
#   NONE                           CLI unavailable / could not proceed (graceful)
#
# Exit codes: 0 always on the happy/graceful paths.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Resolve kit_life.sh: prefer $PROJECT_ROOT, else walk up from this script.
# PACKED 2026-09-12: this file used to live at <instance>/routines/ (one level
# below the root). As a pack-owned bundle routine it installs to
# <instance>/routines/bundle/, i.e. TWO levels down -- the old single `..`
# would resolve ROOT to <instance>/routines and every path below would miss.
# Probe instead of counting levels, so the script survives either home.
if [[ -n "${PROJECT_ROOT:-}" && -x "$PROJECT_ROOT/database/kit_life.sh" ]]; then
  ROOT="$PROJECT_ROOT"
else
  ROOT=""
  for _up in ".." "../.."; do
    _cand="$(cd "$SCRIPT_DIR/$_up" && pwd)"
    if [[ -d "$_cand/database" && -d "$_cand/service" ]]; then ROOT="$_cand"; break; fi
  done
  [[ -n "$ROOT" ]] || ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
fi
LIFEKIT="$ROOT/database/kit_life.sh"

DAY="${1:-$(TZ=Asia/Seoul date +%F)}"
SPLIT="${2:-}"

# ---- a FREE session is open: no-op (rehearsal S2, 2026-10-11) -------------
# The free open (`session-open --free`) is the whole open. With the marker on
# its free row, the session-open below would refuse to reconcile into it
# (force_new) and birth a SECOND, planned session plus a planned day block.
# Open = the marker names a free row the .session-closed tombstone does not.
STATE_DIR="${LIFEKIT_HEALTH_STATE_DIR:-$ROOT/files/program}"
FREE_SID=""
if [[ -f "$STATE_DIR/.active-session" && -f "$ROOT/database/kit_life.db" \
      && -f "$ROOT/service/health/free_session.py" ]]; then
  FREE_SID="$(PYTHONDONTWRITEBYTECODE=1 python3 - "$ROOT/service/health" \
      "$ROOT/database/kit_life.db" "$STATE_DIR" <<'PY' 2>/dev/null || true
import os, sys
sys.path.insert(0, sys.argv[1])
from free_session import is_free
def _id(name):
    try:
        with open(os.path.join(sys.argv[3], name)) as fh:
            txt = fh.read().strip()
        return int(txt) if txt else None
    except (OSError, ValueError):
        return None
sid = _id(".active-session")
if sid is not None and sid != _id(".session-closed") and is_free(sys.argv[2], sid):
    print(sid)
PY
)"
fi
if [[ -n "$FREE_SID" ]]; then
  printf 'FREE\t%s\n' "$FREE_SID"
  exit 0
fi

# ---- install completion: seed the taxonomy if it has not been seeded -------
# Never gates. The lane exits 0 on every path including its own failures, and
# `|| true` covers the one case it cannot (the file not being executable at all,
# e.g. a partial copy). A missing seed must not be able to suppress session
# birth -- session-open names the gap loudly and the session still opens.
INSTALL_ENSURE="$SCRIPT_DIR/health-install-ensure.sh"
if [[ -n "${WARG_HEALTH_INSTALL_CHAIN:-}" ]]; then
  : # re-entrancy: something upstream already ran this lane in this chain
elif [[ -x "$INSTALL_ENSURE" ]]; then
  WARG_HEALTH_INSTALL_CHAIN=1 "$INSTALL_ENSURE" --quiet || true
else
  echo "session-ensure: health-install-ensure.sh not executable at $INSTALL_ENSURE" >&2
fi

# ---- session birth: drive session-open (idempotent, best-effort) ----------
# Never `set -e`-aborts this gate: a failed birth still leaves the task gate
# below to run, and the operator line goes to stderr where cron-guard sees it.
# PACKED 2026-09-12: was files/program/session-open -- a pre-pack location.
# The engine ships from this pack's payload/service/health/, so a freshly
# minted instance has it at service/health/session-open and nowhere else.
SESSION_OPEN="$ROOT/service/health/session-open"
if [[ -n "${WARG_SESSION_OPEN_CHAIN:-}" ]]; then
  echo "session-ensure: session-open skipped -- WARG_SESSION_OPEN_CHAIN set" >&2
elif [[ -x "$SESSION_OPEN" ]]; then
  # STDERR IS NOT NOISE (2026-09-12). This used to carry `2>/dev/null`, which
  # discarded every operator diagnostic session-open emits on the headless
  # path -- including the taxonomy announcement it now makes at session birth
  # ("the pack_health seed never ran on this DB"). A gate whose whole job is to
  # be the CODE CARRIER for session-open must not be the thing that silences
  # it. Command substitution captures fd 1 only, so dropping the redirect is
  # all it takes: session-open's stderr flows to THIS script's stderr, where
  # cron-guard already looks, while stdout stays captured for session_id.
  SO_OUT=""
  SO_RC=0
  SO_OUT="$(WARG_SESSION_OPEN_CHAIN=1 "$SESSION_OPEN")" || SO_RC=$?
  if [[ "$SO_RC" -eq 0 ]]; then
    # session-open stdout: "OPENED session_id=<id> ..." -- re-emit the id in
    # this script's own TAB shape so one call carries both halves.
    # ONE awk, not `sed | head -1`: under `set -o pipefail` an early-closing
    # `head` can make the upstream stage exit 141 (SIGPIPE) and take the whole
    # assignment -- and with `set -e`, the script -- down. awk's own `exit`
    # after the first match has no second stage to race.
    SO_SID="$(printf '%s\n' "$SO_OUT" | awk '
      match($0, /session_id=[0-9]+/) {
        print substr($0, RSTART + 11, RLENGTH - 11); exit
      }')"
    if [[ -n "$SO_SID" ]]; then
      printf 'OPENED\t%s\n' "$SO_SID"
    else
      echo "session-ensure: session-open gave no session_id -- $SO_OUT" >&2
    fi
  else
    echo "session-ensure: session-open exit=$SO_RC (task gate continues)" >&2
  fi
else
  echo "session-ensure: session-open not executable at $SESSION_OPEN" >&2
fi

# ---- ghost-block sweep (2026-09-30) -----------------------------------------
# A block this gate opened for a session that then ended with NO sets (mock,
# diagnosis, walked away) is never settled by anything: a ghost in
# task-overdue. session-block archives exactly those -- blocks whose note links
# a session (`session-ensure sid=<id>`, written below) that has no sets and is
# from an earlier day or no longer exists. Today's and the active session's
# blocks are never touched. Best-effort, never gates.
SESSION_BLOCK="$ROOT/service/health/session-block"
if [[ -x "$SESSION_BLOCK" && -f "$ROOT/database/kit_life.db" ]]; then
  "$SESSION_BLOCK" sweep --db "$ROOT/database/kit_life.db" --today "$DAY" >&2 || true
fi

# CLI not available / task verbs missing -> graceful no-op.
if [[ ! -x "$LIFEKIT" ]] || ! "$LIFEKIT" task-find "헬스" >/dev/null 2>&1; then
  echo "NONE"
  exit 0
fi

# Reconcile-before-write: an OPEN "헬스" / "헬스 - ..." task for DAY already? ->
# EXISTS, no dup. Same date/status/title filter as close_task.sh.
EXISTING="$("$LIFEKIT" task-find "헬스" 2>/dev/null \
  | awk -F'\t' -v d="$DAY" '
      $3==d && $4=="todo" && ($2=="헬스" || $2 ~ /^헬스 -/) {print $1"\t"$2; exit}')"

if [[ -n "$EXISTING" ]]; then
  EID="$(printf '%s' "$EXISTING" | cut -f1)"
  ETITLE="$(printf '%s' "$EXISTING" | cut -f2)"
  printf 'EXISTS\t%s\t%s\n' "$EID" "$ETITLE"
  exit 0
fi

# Resolve the planned split: explicit arg wins, else rotation-current -> next_split.
# rotation-current emits deterministic "key=value / key=value ..." on one line.
# Trim whitespace from an explicit split arg so a blank/whitespace arg falls
# back to rotation rather than producing a "헬스 - " (empty-code) title.
SPLIT="$(printf '%s' "$SPLIT" | awk '{gsub(/^[[:space:]]+|[[:space:]]+$/,""); print}')"

if [[ -z "$SPLIT" ]]; then
  ROT="$("$LIFEKIT" rotation-current 2>/dev/null || true)"
  # Extract next_split=<value> from the KEY=VALUE block.
  SPLIT="$(printf '%s\n' "$ROT" | tr '/' '\n' \
    | awk -F'=' '/^[[:space:]]*next_split[[:space:]]*=/ {gsub(/^[[:space:]]+|[[:space:]]+$/,"",$2); print $2; exit}')"
fi

# Compose the title. Unknown/empty split -> plain "헬스".
if [[ -n "$SPLIT" ]]; then
  TITLE="헬스 - ${SPLIT}"
else
  TITLE="헬스"
fi

# The note LINKS the block to the session opened above, so a session that ends
# with no sets can take its block with it (session-block). Unlinked when
# session-open gave no id -- such a block is never reclaimed automatically.
NOTE="session-ensure"
if [[ -n "${SO_SID:-}" ]]; then
  NOTE="session-ensure sid=${SO_SID}"
fi

# Create. task-add <title> [due_date] [note] -> id<TAB>title<TAB>due<TAB>state[<TAB>place].
# --new: we already ran our own same-day dup reconcile above; bypass kit_life's
# cross-date title-dedup gate (which would EXISTS-refuse just because a "헬스 - X"
# title exists on ANOTHER day). Our EXISTS check is day-scoped and authoritative.
ROW="$("$LIFEKIT" task-add "$TITLE" "$DAY" "$NOTE" --new 2>/dev/null || true)"
if [[ -z "$ROW" ]]; then
  echo "NONE"
  exit 0
fi
# Guard: a well-formed created row starts with a numeric id. If the CLI still
# returned an EXISTS/error shape, degrade to NONE rather than mis-report.
FIRST="$(printf '%s\n' "$ROW" | head -1)"
case "$FIRST" in
  [0-9]*) : ;;                 # numeric id -> real created row
  *) echo "NONE"; exit 0 ;;
esac
NID="$(printf '%s\n' "$ROW" | head -1 | cut -f1)"
NTITLE="$(printf '%s\n' "$ROW" | head -1 | cut -f2)"
printf 'CREATED\t%s\t%s\n' "$NID" "$NTITLE"
