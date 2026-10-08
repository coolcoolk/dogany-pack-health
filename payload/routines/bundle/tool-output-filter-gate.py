#!/usr/bin/env python3
"""tool-output-filter-gate.py -- PreToolUse hook: a pack in-session CLI runs
BARE, never with its output piped through a filter.

WHY (review of a live session, 2026-10-08). The agent ran set-add /
set-arm / exercise-enter piped through `grep` / `head` all session. Their
stdout is the reply contract: the record line, the load decision, the
next-set lines, the keyboard receipts, the machine ask. A filter keeps what
the agent guessed it needed and silently drops the rest, so lines the owner
was owed never reached the chat (the owner was told the warm-up buttons were missing when
they existed, a next-set line never shown). The reference text already said
"never pipe" (set-recording.md, hotfix 0.34.x) and was not followed; this is
the mechanical leg.

WHAT IT REFUSES: a Bash call that invokes one of IN_SESSION_CLIS (by path or
bare name) AND either pipes that output into a filter (grep, head, tail, sed,
awk, cut, sort, uniq, wc, tr, jq, less, more) or discards stdout
(`>/dev/null`, `1>/dev/null`, `&>/dev/null`). `2>/dev/null` and `2>&1` are
fine: stderr is audit only. The deny reason names the fix (run it bare).

WHAT IT DOES NOT TOUCH: every other tool and command; suite files whose name
merely contains a CLI name (tests/test-set-add.py is not set-add).

CONTRACT: fail-open. Any error, unreadable input, unknown shape -> no output,
exit 0. PACK_HEALTH_FILTER_GATE=off disables it (debugging only).

WIRING: pack-manifest.json hooks[] (event PreToolUse); pack_install.sh
_hooks_wire writes it into .claude/settings.local.json.
"""

import sys
sys.dont_write_bytecode = True

import json  # noqa: E402
import os    # noqa: E402
import re    # noqa: E402

IN_SESSION_CLIS = (
    "set-add", "set-arm", "set-table", "set-undo", "exercise-enter",
    "exercise-variant", "exercise-drop", "machine-pick", "session-open",
    "session-post", "session-closeout", "session-cursor", "session-block",
    "session-abort", "session-retro", "fatigue-brief", "cardio-record",
    "lattice-set", "workout-parts",
)
FILTERS = ("grep", "egrep", "fgrep", "rg", "head", "tail", "sed", "awk",
           "cut", "sort", "uniq", "wc", "tr", "jq", "less", "more")

_CLI_RE = re.compile(r"(?:^|[\s/;&|(`'\"])(%s)(?=$|[\s;&|)`'\"])"
                     % "|".join(re.escape(c) for c in IN_SESSION_CLIS))
_DEVNULL_RE = re.compile(r"(?:^|[\s;])(?:1|&)?>{1,2}\s*/dev/null")


def _segments(cmd):
    """Split on a single `|` (a pipe), keeping `||` inside a segment."""
    return re.split(r"(?<!\|)\|(?!\|)", cmd)


def verdict(cmd):
    """None (allowed) or the reason string (refused)."""
    if not isinstance(cmd, str) or not cmd.strip():
        return None
    segs = _segments(cmd)
    for i, seg in enumerate(segs):
        m = _CLI_RE.search(seg)
        if not m:
            continue
        cli = m.group(1)
        for nxt in segs[i + 1:]:
            words = nxt.strip().split()
            head = os.path.basename(words[0]) if words else ""
            if head in FILTERS:
                return ("`%s` output piped through `%s`" % (cli, head))
        if _DEVNULL_RE.search(seg):
            return "`%s` stdout discarded (>/dev/null)" % cli
    return None


def main():
    if os.environ.get("PACK_HEALTH_FILTER_GATE", "").lower() == "off":
        return 0
    try:
        data = json.load(sys.stdin)
    except Exception:  # noqa: BLE001 -- fail-open
        return 0
    if not isinstance(data, dict) or data.get("tool_name") != "Bash":
        return 0
    cmd = (data.get("tool_input") or {}).get("command")
    why = verdict(cmd)
    if not why:
        return 0
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": (
            "%s. This tool's stdout IS the reply contract (record line, load "
            "decision, next-set lines, keyboard receipts) -- a filter drops "
            "lines the owner is owed. Run the same command BARE (no pipe, no "
            ">/dev/null; 2>/dev/null is fine) and read the whole output."
            % why)}}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:  # noqa: BLE001 -- fail-open, never block on a bug here
        sys.exit(0)
