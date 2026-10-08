#!/bin/bash
# hk-ingest.sh -- HealthKit ingest entry point (pack-owned routine).
#
# Three callers, one engine (service/health/hk-ingest):
#   scheduled pass 04:50  routine-ctl.sh enable hk-ingest-early   routines/bundle/hk-ingest.sh 04:50
#   scheduled pass 09:00  routine-ctl.sh enable hk-ingest-morning routines/bundle/hk-ingest.sh 09:00
#   workout callback      transporter config.json "callback":
#                         "<root>/routines/bundle/hk-ingest.sh --callback"
#                         (the receiver pipes {"source","kind","id"} on stdin
#                         once per NEW id; the engine filters at entry and
#                         only healthkit/workout goes further)
# 04:50 closes yesterday (steps, heart rate, active energy closed:true);
# 09:00 lands last night's sleep on today's wake day. Updates to an id never
# call back, so every pass re-reads its date window.
#
# Root: probe for database/ + service/ one or two levels up
# (session-ensure.sh idiom); HK_ROOT overrides. Output appends to .telegram_bot/logs/hk-ingest.log.
set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -z "${HK_ROOT:-}" ]; then
    for _up in ".." "../.."; do
        _cand="$(cd "$SCRIPT_DIR/$_up" && pwd)"
        if [ -d "$_cand/database" ] && [ -d "$_cand/service" ]; then HK_ROOT="$_cand"; break; fi
    done
    [ -n "${HK_ROOT:-}" ] || HK_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
fi
export HK_ROOT

MODE="pass"
if [ "${1:-}" = "--callback" ]; then MODE="callback"; shift; fi

PY="${HK_PYTHON:-/usr/bin/python3}"
[ -x "$PY" ] || PY="python3"
LOG_DIR="${HK_LOG_DIR:-$HK_ROOT/.telegram_bot/logs}"
mkdir -p "$LOG_DIR"
{
    echo "--- $(date '+%Y-%m-%d %H:%M:%S') hk-ingest $MODE"
} >>"$LOG_DIR/hk-ingest.log"
"$PY" "$HK_ROOT/service/health/hk-ingest" "$MODE" "$@" >>"$LOG_DIR/hk-ingest.log" 2>&1
rc=$?
echo "--- exit $rc" >>"$LOG_DIR/hk-ingest.log"
exit "$rc"
