#!/usr/bin/env python3
# session_harness.hooks -- executable hook carriers for the event roster.
#
# events.py enumerates the 11 events; this package holds the concrete scripts
# that the harness runtime (Claude Code settings.json) actually invokes. Each
# module here is BOTH an importable module and a standalone script, so it must
# stay stdlib-only and must not depend on a package-relative import at runtime.
#
# Present carriers:
#   turn_pre.py   Event.TurnPre -- UserPromptSubmit cursor-state injection
#
# Wiring is a separate, gated landing step: nothing in this package registers
# itself in any settings.json on import.
