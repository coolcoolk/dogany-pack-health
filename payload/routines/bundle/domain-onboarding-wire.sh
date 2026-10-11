#!/bin/bash
# domain-onboarding-wire.sh -- register this pack's onboarding hooks in THIS
# instance's .claude/settings.local.json.
#
#   SessionStart -> routines/bundle/domain-onboarding-check.py
#   Stop         -> routines/bundle/domain-onboarding-stop.py   (0.16.1; log-only 0.17.1)
#   UserPromptSubmit -> routines/bundle/domain-onboarding-prompt.py (0.17.2)
#   UserPromptSubmit -> routines/bundle/session-progress-inject.py (live-session
#                       progress injection; no-op outside a session)
#
# BOTH legs matter and they are not interchangeable: on a FRESH MINT the
# SessionStart leg structurally cannot fire the offer (the identity marker is
# still present at that instant, so the gate answers NO-OFFER), and the Stop
# leg is the one that catches the moment identity onboarding completes. Wiring
# only the SessionStart leg here would preserve, across updates, exactly the
# half that cannot work on a newborn.
#
# WHY settings.local.json AND NOT settings.json:
#   update.sh regenerates .claude/settings.json wholesale from the framework
#   hook manifest and has dropped instance-local hook wiring four times
#   (DGN-1250). settings.local.json is instance-only and untracked by the
#   framework, so wiring placed here survives framework updates. Claude Code
#   merges both files.
#
#   MEASURED 2026-09-23: pack_install.sh's own declared-hook lane (_hooks_wire)
#   writes manifest hooks[] into settings.json -- the very file DGN-1250
#   declared unsafe. So a pack that declares hooks gets wiring that dies at the
#   next update. The framework fix is taken (DGN-1250 reopened, 2.7); until it
#   lands, running this script is what keeps a live instance's hooks alive.
#   Until then both files may carry the same hook: Claude Code merges them, so
#   the hook can run twice in one Stop event. Both runs emit the same block
#   reason and the framework copy disappears at the first update, so the
#   duplicate is cosmetic -- stated here so nobody reads it as a defect.
#
# WHY A SCRIPT AND NOT A MANUAL EDIT:
#   the pack install profile returns before the framework's hook-wiring lane,
#   so a pack cannot register a hook at install time (measured -- see
#   health-install-ensure.sh). This script is run ONCE per instance after mint
#   by whoever operates that instance. Idempotent: re-running is a no-op.
#
# Usage:  domain-onboarding-wire.sh [<instance-root>]
#         default root = two levels up from this file
set -euo pipefail

ROOT="${1:-}"
if [[ -z "$ROOT" ]]; then
  ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
fi

SETTINGS="$ROOT/.claude/settings.local.json"
# event:script-relative-path pairs -- add a line to extend.
HOOK_SPECS=(
  "SessionStart:routines/bundle/domain-onboarding-check.py"
  "Stop:routines/bundle/domain-onboarding-stop.py"
  "UserPromptSubmit:routines/bundle/domain-onboarding-prompt.py"
  "UserPromptSubmit:routines/bundle/session-progress-inject.py"
)
PY="${LIFEKIT_PYTHON:-}"
# Apple's /usr/bin/python3 is fine for THIS script (no long-line tokenizing),
# but prefer homebrew when present for consistency with the rest of the bundle.
if [[ -z "$PY" ]]; then
  if [[ -x /opt/homebrew/bin/python3 ]]; then PY=/opt/homebrew/bin/python3
  else PY="$(command -v python3 || echo /usr/bin/python3)"; fi
fi

mkdir -p "$ROOT/.claude"
[[ -f "$SETTINGS" ]] || printf '{}\n' > "$SETTINGS"

for _spec in "${HOOK_SPECS[@]}"; do
  _event="${_spec%%:*}"
  _rel="${_spec#*:}"
  _hook="$ROOT/$_rel"
  if [[ ! -f "$_hook" ]]; then
    # A missing leg is skipped, never fatal: an older payload may not carry it.
    echo "WIRE: skipped $_event -- hook script absent at $_hook" >&2
    continue
  fi
  chmod +x "$_hook" 2>/dev/null || true

  "$PY" - "$SETTINGS" "$_hook" "$_event" <<'PYEOF'
import json, sys, os

settings_path, hook_path, event = sys.argv[1], sys.argv[2], sys.argv[3]
cmd = "/usr/bin/python3 " + hook_path

try:
    with open(settings_path) as f:
        data = json.load(f)
except Exception:
    data = {}
if not isinstance(data, dict):
    data = {}

hooks = data.setdefault("hooks", {})
if not isinstance(hooks, dict):
    hooks = {}
    data["hooks"] = hooks
sessions = hooks.setdefault(event, [])
if not isinstance(sessions, list):
    sessions = []
    hooks[event] = sessions

# idempotence: match on the hook script path, not the exact command string,
# so a python-interpreter change does not create a duplicate entry.
for group in sessions:
    for h in (group or {}).get("hooks", []) or []:
        if hook_path in (h or {}).get("command", ""):
            print("WIRE: %s already registered -- no change" % event)
            sys.exit(0)

sessions.append({"hooks": [{"type": "command", "command": cmd, "timeout": 30}]})

tmp = settings_path + ".tmp"
with open(tmp, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    f.write("\n")
os.replace(tmp, settings_path)
print("WIRE: registered %s -> %s" % (event, os.path.basename(hook_path)))
PYEOF

done

# verify the file still parses after the writes
"$PY" -c "import json,sys; json.load(open('$SETTINGS')); print('WIRE: settings.local.json parses OK')"
