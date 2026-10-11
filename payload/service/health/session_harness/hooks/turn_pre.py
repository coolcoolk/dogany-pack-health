#!/usr/bin/env python3
"""turn_pre.py -- Event.TurnPre carrier: live cursor injection (SPEC A2.1).

Ticket: 2026-08-25-session-state-not-injected (P0). This file and that
ticket are one deliverable.

WHY THIS EXISTS
    The write path is already deterministic and model-free: a button tap goes
    bridge -> set-add -> INSERT, "Behavior model turn 0, outbound 0". It is
    working as designed. (The text twin, session-fastpath, was removed
    2026-10-08: owner text is never parsed into a set row by code.)

    The RETURN wire is what is missing. Because a tap spends zero model
    turns, the sets it logs never appear anywhere in the SDK conversation
    history. On the next model turn those sets do not exist as far as the model
    is concerned, so it answers from its own last utterance -- which is how a
    correctly rendered table ("r2 100.0kg 2 [v]") and the prose in the SAME turn
    ("아직요 -- 램프 2 남았어요") ended up contradicting each other.

    Nothing needs to be computed. session-cursor already resolves the truth and
    set-table already renders from it. This hook only carries that truth back
    into the model's context, every turn.

    The prescription is deliberately NOT another SKILL.md sentence. That surface
    already carried a STATE RE-READ GATE and it was skipped; the same
    SKILL.md concedes that prompt discipline cannot reliably bind model
    behaviour (D2). Owner directive: if the button reliably prompts the next
    action, no such prose rule is needed in the first place.

PRECEDENT
    routines/rotation-gate.py (live instance, BUILT+WIRED) is the same machine one
    scope narrower: a UserPromptSubmit hook that injects authoritative state so
    the model cannot answer by guessing. Structure, I/O contract and fail-open
    behaviour are copied from it. The differences are deliberate and are the
    two places this hook is stricter:
      - it fires on EVERY turn (no intent keywords -- in-session state is never
        off-topic, and defect #4 happened on a prompt no keyword list catches)
      - a no-op emits NOTHING, not an empty additionalContext envelope

RULES ENFORCED AS CODE
    R-TURNPRE-READONLY  no writes, no DB access, no marker mutation. The only
                        subprocess is `session-cursor resolve <sid>`.
    R-TURNPRE-NOBLOCK   every failure path exits 0 with no injection. A turn is
                        never blocked, delayed past the timeout, or failed.
    R-TURNPRE-NOOP      no active session -> zero bytes on stdout, exit 0.
    R-TURNPRE-DEGRADED  session-cursor exit 2 (FALLBACK) -> inject the reason
                        VERBATIM. A degraded truth beats silent staleness: the
                        failure mode being fixed is the model confidently
                        reciting a stale set number, so "unknown, go read it"
                        is strictly better than nothing.
    R-TURNPRE-BUDGET    the injected payload is capped (see below) and any
                        overflow is truncated deterministically with a visible
                        marker. Never silently.

BYTE BUDGET -- 1536 bytes of UTF-8 for the whole additionalContext.
    (Raised from 1024 on 2026-09-30. Re-measured on a fixture session: the
    cursor block grew band/last_logged/read_cmd lines on 2026-09-11 and the
    day_progress line on 2026-09-30 -> 447 B for a 6-slot day; frame 483 B;
    owner-ruling line ~190 B. 1120 B realistic, so 1024 would have truncated
    the tail on every turn. Paid only while a session is live -- R-TURNPRE-NOOP
    keeps every other turn at zero bytes. The historical 1024 derivation
    follows.)
    This is the one hook that loads on EVERY model turn, so its cost is paid
    per turn for the entire session, not once. Measured, not guessed: the
    framing directive below is 483 B fixed, and a full emit_cursor() block --
    all 9 lines including the optional boundary line, with a Korean `display`
    value -- is 289 B. Realistic total: 774 B. 1024 B leaves 250 B of headroom
    for longer display names and future cursor lines while capping the per-turn
    tax at roughly 256 ASCII tokens. A FALLBACK injection is 338 B. The frame is
    emitted FIRST, so truncation can only ever eat state lines, never the
    directive that makes the state authoritative.

PATH RESOLUTION
    (2026-09-30) The deployed pack puts session-cursor at
    <root>/service/health/session-cursor, a sibling of this package; the only
    relpath this hook knew was the retired <root>/files/program/session-cursor.
    Measured on the live health instance: files/program/ holds no CLI, so the
    walk-up found no root and every turn was a silent no-op even with a live
    session. Both layouts are now probed, pack layout first.
    Same shape as rotation-gate.py: $PROJECT_ROOT first, else walk up from this
    file. The pack tree (service/health/session_harness/hooks/) and the deployed
    agent workspace do not have the same depth, so the walk-up is a bounded
    ancestor search for the `files/program/session-cursor` marker rather than a
    fixed number of `..` hops. Nothing is hardcoded to any agent workspace.
    LIFEKIT_HEALTH_STATE_DIR is honoured exactly as session-cursor honours it, so the
    hook and the CLI can never disagree about which marker is live.

Hook I/O contract (identical to rotation-gate.py):
    stdin  : JSON, {"prompt", "session_id", ...}. Contents are not required --
             this hook is state-driven, not prompt-driven.
    stdout : {"hookSpecificOutput": {"hookEventName": "UserPromptSubmit",
             "additionalContext": "..."}} -- or nothing at all on a no-op.
    exit   : always 0.

stdlib only (json / os / subprocess / sys). ASCII source except the framing
text, which is English by build directive (backend prompt, token economy, the
user referred to generically).
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Roster token. Kept as a literal rather than importing session_harness.events
# so this file runs as a bare script with no sys.path setup and no import-time
# failure surface. test_turn_pre.py asserts it equals Event.TurnPre.value, which
# binds the two without coupling them at runtime.
EVENT = "TurnPre"

# The Claude Code event this carrier is registered on (SPEC A2.1 mapping:
# UserPromptSubmit -> TurnPre). Wiring itself is a separate gated step.
HOOK_EVENT_NAME = "UserPromptSubmit"

# R-TURNPRE-BUDGET. See the module docstring for the derivation.
BUDGET_BYTES = 1536
TRUNCATION_MARKER = "\n[TRUNCATED: TurnPre budget %dB]" % BUDGET_BYTES

# R-TURNPRE-NOBLOCK. `session-cursor resolve` is a sqlite read plus a YAML
# parse; it has no business taking seconds. Bounded well under any sane
# settings.json hook timeout so the hook gives up before the harness does.
TIMEOUT_SEC = 8

# How far up from this file to look for the workspace root. Pack layout is
# service/health/session_harness/hooks -> 4; a couple of spare levels cost
# nothing and absorb a deploy-layout change.
MAX_WALK_UP = 6

# Pack layout first (service/health/, where the pack installs the engine),
# then the retired live layout (files/program/). First readable one wins.
CURSOR_CLI_RELPATHS = (
    ("service", "health", "session-cursor"),
    ("files", "program", "session-cursor"),
)
CURSOR_CLI_RELPATH = CURSOR_CLI_RELPATHS[-1]   # legacy name, retired layout

# session-cursor exit codes (its module header): 0 resolved, 2 FALLBACK, 1 bad
# args / missing files.
RC_RESOLVED = 0
RC_FALLBACK = 2

# A FALLBACK whose reason is this means the marker vanished between our read
# and the CLI's -- that is the no-op case (R-TURNPRE-NOOP), not a degraded one.
# Injecting "no active session" would be noise on every out-of-session turn.
FALLBACK_NOOP_REASONS = ("no_active_session",)


# ---------------------------------------------------------------------------
# Framing. The state block alone is not enough: the model has a plausible,
# self-consistent, WRONG account of the session in its own context window, and
# it has already been observed preferring it. The frame therefore has to say
# out loud that history is the untrustworthy source here, and why.
# ---------------------------------------------------------------------------
CURSOR_FRAME = (
    "AUTHORITATIVE LIVE SESSION CURSOR -- read from the workout store during "
    "THIS turn. It is the ONLY truth for the current exercise slot and set "
    "number, and it OVERRIDES the conversation history: sets logged by button "
    "tap spend zero model turns and never enter this transcript, "
    "so your recollection of this session is incomplete by construction. Never "
    "infer the current slot, next_set_seq, done_working or planned_sets from "
    "earlier turns -- state them from this block only."
)

# Owner ruling 2026-09-30 (actor ticket, "3. ㅇㅋ"): progress is injected on
# every turn of a live session only; the model may change a LOAD on its own
# judgment, but a change to the ORDER of the remaining lifts is asked first.
# Carried here because this is the one text the model reads on every live
# turn -- the same place the progress it acts on arrives.
RULING_LINE = (
    "Owner ruling: adjust a working LOAD on your own judgment when the "
    "session calls for it; ask the owner before changing the ORDER of the "
    "remaining exercises."
)

FALLBACK_FRAME = (
    "LIVE SESSION CURSOR UNRESOLVED (degraded) -- a session IS active but the "
    "cursor resolver declined to resolve it; its reason is reproduced verbatim "
    "below. Treat the current slot and set number as UNKNOWN. Do NOT "
    "reconstruct them from the conversation history -- read the store before "
    "stating any set number."
)


# ---------------------------------------------------------------------------
# Refusals. Every no-op reason is a named, declared skip rather than a bare
# `return None`, so the reason is inspectable in a test and greppable in a log.
# Mirrors the sibling modules' exception style (a `rule` id on the class).
# ---------------------------------------------------------------------------
class TurnPreSkip(Exception):
    """A declared reason to inject nothing. Always caught; always exit 0."""

    rule = "R-TURNPRE-NOOP"

    def __init__(self, reason):
        self.reason = reason
        super().__init__("%s: %s" % (self.rule, reason))


# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------
def _cli_under(path):
    for rel in CURSOR_CLI_RELPATHS:
        cand = os.path.join(path, *rel)
        if os.access(cand, os.R_OK):
            return cand
    return None


def _looks_like_root(path):
    return _cli_under(path) is not None


def resolve_project_root():
    """Workspace root: $PROJECT_ROOT, else the nearest ancestor of this file
    that carries files/program/session-cursor. Never hardcoded."""
    root = os.environ.get("PROJECT_ROOT")
    if root and _looks_like_root(root):
        return os.path.abspath(root)

    cand = HERE
    for _ in range(MAX_WALK_UP + 1):
        if _looks_like_root(cand):
            return cand
        parent = os.path.dirname(cand)
        if parent == cand:
            break
        cand = parent
    raise TurnPreSkip("no_project_root")


def resolve_cursor_cli(project_root):
    """Path to the session-cursor CLI, or skip."""
    cli = _cli_under(project_root)
    if cli is None:
        raise TurnPreSkip("no_cursor_cli")
    return cli


def marker_path(project_root):
    """Active-session marker. LIFEKIT_HEALTH_STATE_DIR is honoured exactly as
    session-cursor honours it (its STATE_DIR), so the hook and the CLI can never
    disagree about which marker surface is live."""
    state_dir = os.environ.get("LIFEKIT_HEALTH_STATE_DIR") or os.path.join(
        project_root, "files", "program")
    return os.path.join(state_dir, ".active-session")


def active_session_id(project_root):
    """Session id from the marker, or skip. Same parse as session-cursor's
    marker_read(): strip, int, anything else is 'no marker'."""
    try:
        with open(marker_path(project_root)) as fh:
            txt = fh.read().strip()
        sid = int(txt) if txt else None
    except (OSError, ValueError):
        sid = None
    if sid is None:
        raise TurnPreSkip("no_active_session")
    return sid


# ---------------------------------------------------------------------------
# The one subprocess
# ---------------------------------------------------------------------------
def run_cursor(cli, session_id, timeout=None):
    """`session-cursor resolve <sid>` -> (returncode, stdout). R-TURNPRE-NOBLOCK:
    a timeout or any spawn failure is a skip, never a raised turn failure."""
    argv = [cli, "resolve", str(session_id)]
    if not os.access(cli, os.X_OK):
        # Not marked executable (e.g. a checked-out copy losing its mode bit):
        # run it through this interpreter rather than giving up.
        argv = [sys.executable] + argv
    try:
        res = subprocess.run(
            argv,
            capture_output=True, text=True,
            timeout=TIMEOUT_SEC if timeout is None else timeout,
        )
    except subprocess.TimeoutExpired:
        raise TurnPreSkip("cursor_timeout") from None
    except Exception:
        raise TurnPreSkip("cursor_spawn_failed") from None
    return res.returncode, (res.stdout or "")


# ---------------------------------------------------------------------------
# Budget
# ---------------------------------------------------------------------------
def fit(text, budget=BUDGET_BYTES, marker=TRUNCATION_MARKER):
    """R-TURNPRE-BUDGET. Return `text` unchanged if it fits in `budget` UTF-8
    bytes; otherwise cut the TAIL deterministically and append `marker`.

    The frame is always the head of the payload, so the tail is state lines --
    losing a trailing key=value is survivable, losing the directive that makes
    the block authoritative is not. The cut lands on a UTF-8 character boundary
    (a partial character is dropped, never emitted half). The returned string is
    guaranteed to encode to <= budget bytes.
    """
    raw = text.encode("utf-8")
    if len(raw) <= budget:
        return text
    keep = budget - len(marker.encode("utf-8"))
    if keep <= 0:
        # Degenerate budget (build-time defect). Emit the marker alone, clipped.
        return marker.encode("utf-8")[:budget].decode("utf-8", "ignore")
    return raw[:keep].decode("utf-8", "ignore") + marker


# ---------------------------------------------------------------------------
# Context construction
# ---------------------------------------------------------------------------
def build_context(returncode, stdout):
    """(returncode, stdout) from session-cursor -> the additionalContext string.

    exit 0 -> the CURSOR block under the authoritative frame.
    exit 2 -> the FALLBACK reason verbatim under the degraded frame
              (R-TURNPRE-DEGRADED), except for the no-op reasons.
    anything else (1 = bad args / missing db, or a crash) -> skip.
    """
    body = (stdout or "").strip()

    if returncode == RC_RESOLVED:
        if not body:
            raise TurnPreSkip("cursor_empty_output")
        if not body.startswith("CURSOR"):
            # Exit 0 without the contract's first token: the CLI is not the one
            # we think it is. Do not dress up an unknown payload as truth.
            raise TurnPreSkip("cursor_malformed_output")
        return fit(CURSOR_FRAME + "\n" + RULING_LINE + "\n\n" + body)

    if returncode == RC_FALLBACK:
        if not body:
            raise TurnPreSkip("cursor_empty_output")
        # "FALLBACK <reason>" is the contract; keep the reason VERBATIM. If the
        # prefix is missing, pass the whole payload through rather than dropping
        # a degraded truth on a formatting technicality.
        parts = body.split(None, 1)
        if parts[0] == "FALLBACK" and len(parts) > 1:
            reason = parts[1].strip()
        else:
            reason = body
        if reason in FALLBACK_NOOP_REASONS:
            raise TurnPreSkip("no_active_session")
        return fit(FALLBACK_FRAME + "\n\nFALLBACK reason: " + reason)

    raise TurnPreSkip("cursor_exit_%s" % returncode)


def compute_injection():
    """Full read-only pipeline: root -> cli -> marker -> resolve -> context.
    Raises TurnPreSkip for every declared no-op."""
    root = resolve_project_root()
    cli = resolve_cursor_cli(root)
    sid = active_session_id(root)
    returncode, stdout = run_cursor(cli, sid)
    return build_context(returncode, stdout)


def emit(context):
    """Write the hook envelope. R-TURNPRE-NOOP means callers pass nothing here
    at all -- an empty envelope is still bytes on every out-of-session turn."""
    sys.stdout.write(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": HOOK_EVENT_NAME,
            "additionalContext": context,
        }
    }, ensure_ascii=False))
    sys.stdout.write("\n")
    sys.stdout.flush()


def main():
    try:
        try:
            # Drained but not required: this hook is state-driven, not
            # prompt-driven. Reading stdin keeps the harness from seeing a
            # broken pipe.
            sys.stdin.read()
        except Exception:
            pass

        try:
            context = compute_injection()
        except TurnPreSkip:
            sys.exit(0)
        except Exception:
            # R-TURNPRE-NOBLOCK: an undeclared internal error is still a clean
            # no-op. The turn proceeds without injection.
            sys.exit(0)

        try:
            emit(context)
        except Exception:
            pass
        sys.exit(0)
    except SystemExit:
        raise
    except BaseException:
        try:
            sys.exit(0)
        except SystemExit:
            raise


if __name__ == "__main__":
    main()
