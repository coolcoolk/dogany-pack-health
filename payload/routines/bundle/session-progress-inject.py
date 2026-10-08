#!/usr/bin/env python3
# session-progress-inject.py -- UserPromptSubmit entry point for the two
# live-session carriers.
#
#   1. progress (TurnPre)  service/health/session_harness/hooks/turn_pre.py
#      Tickets 2026-08-25-session-state-not-injected (P0) + the owner
#      ruling of 2026-09-30 in 2026-09-11-actor-architecture: progress is
#      injected on every turn, only during a live session.
#   2. question-close      service/health/session_harness/hooks/question_close.py
#      Ticket 2026-08-09-question-close-deterministic-carrier: the owner's
#      previous question, when the reply did not visibly address it.
#
# The carriers live beside the engine they read, but the pack contract
# (C-HOOKS) only lets a manifest hooks[] entry point under routines/bundle/, so
# this file is the declared entry point. It imports the carriers from their
# files and emits ONE envelope, so a live turn costs one hook process.
#
# Both carriers are gated on the same fact: the .active-session marker names a
# session. No live session -> zero bytes. Fail-open throughout: any error is a
# silent no-op, never a blocked turn.
import importlib.util
import json
import os
import sys

# The carriers are imported, not exec'd as scripts; keep the instance's
# service/health tree free of __pycache__ residue.
sys.dont_write_bytecode = True

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.abspath(os.path.join(HERE, "..", "..", "service", "health",
                                     "session_harness", "hooks"))


def _load(name, filename):
    path = os.path.join(HOOKS, filename)
    if not os.path.isfile(path):
        return None
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def compose(hook_input):
    """[context, ...] for this turn (possibly empty)."""
    tp = _load("turn_pre_carrier", "turn_pre.py")
    if tp is None:
        return []
    parts = []
    try:
        root = tp.resolve_project_root()
        tp.active_session_id(root)          # the live-session gate
    except Exception:                       # TurnPreSkip or anything else
        return []
    try:
        parts.append(tp.compute_injection())
    except Exception:
        pass
    qc = _load("question_close_carrier", "question_close.py")
    if qc is not None:
        try:
            q = qc.compute(hook_input)
            if q:
                parts.append(q)
        except Exception:
            pass
    return [p for p in parts if p]


def main():
    try:
        try:
            raw = sys.stdin.read()
            hook_input = json.loads(raw) if raw.strip() else {}
        except Exception:
            hook_input = {}
        parts = compose(hook_input if isinstance(hook_input, dict) else {})
        if parts:
            sys.stdout.write(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "UserPromptSubmit",
                    "additionalContext": "\n\n".join(parts),
                }
            }, ensure_ascii=False) + "\n")
            sys.stdout.flush()
    except BaseException:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
