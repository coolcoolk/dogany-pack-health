#!/usr/bin/env python3
"""domain-onboarding-stop.py -- Stop-hook caller for the pack_health domain gate.

WHY THIS EXISTS (measured 2026-09-23, from the deleted 09-22 instance's own
transcript):
  domain-onboarding-check.py is the SessionStart caller for the same gate, and
  on a FRESH MINT it can never fire the offer that matters. Sequence measured
  on the instance the owner deleted the same day:

    11:57:55  pack install wires the SessionStart hook (confirmed in the mint
              log -- wiring was never the defect)
    13:29:15  first owner turn. At SessionStart the identity file still carries
              ONBOARDING_PENDING, so the gate answers NO-OFFER (identity
              pending) and the caller correctly prints nothing.
    13:29-13:34  identity onboarding runs INSIDE that same session: name,
              emoji, address term, tone, humor. Marker cleared 13:34:37.
    13:34:58  the instance closes with a capability list -- no goal, no body
              state, no injuries, no split, and one single tool call that
              touched the shared records it was minted to own.
    (no further owner turn ever arrives; the instance is deleted that day)

  The domain offer could only have fired at the NEXT SessionStart, i.e. only if
  the user came back and spoke again. They did not -- they had just been handed
  a brochure. Measured cost of this one-session-late gate: the user asked for a
  health agent fifteen times between 2026-09-14 and 2026-09-23, deleting each
  newborn in between. Every one of those mints succeeded. Every one of them
  died in the same minute.

  SessionStart is the one moment on a fresh mint where the answer is GUARANTEED
  to be "not yet". This hook asks the same gate at the moment the answer can
  finally be yes: when the model tries to END a turn and the identity marker is
  already gone.

RELATIONSHIP TO THE TWO EXISTING GATES (no overlap, by construction):
  - routines/onboarding-gate-stop.py (framework, DGN-1543 R7) owns the turn
    WHILE the marker is present. This hook abstains for exactly that case, so
    the two can never both block the same turn.
  - routines/bundle/domain-onboarding-check.py (this pack, SessionStart) stays
    as-is: it is still the right caller for every session AFTER the first.
    This file is the first-session leg it structurally cannot serve.

CONTRACT (fail-open, always):
  - stop_hook_active set                         -> exit 0 (one re-prompt per
                                                    turn, never a loop --
                                                    output-gate-stop precedent)
  - identity marker still present                -> exit 0 (identity gate's turn)
  - not an owner-facing bridge session           -> exit 0
  - gate missing / errors / times out            -> exit 0
  - gate says NO-OFFER                           -> exit 0
  - gate says OFFER                              -> LOG ONLY (0.17.1; no block)
  Never blocks on anything but a measured OFFER, never prints a traceback.

LANE: pack_health asset (same lane note as domain-onboarding-check.py). The
gate decides; this file only asks it at the right instant and carries its
verdict to the model.
"""

import json
import os
import subprocess
import sys
import time

GATE_REL = os.path.join("service", "health", "onboarding-gate")
IDENTITY_REL = os.path.join("identity", "hot.custom.agent.md")
MARKER = "<!-- ONBOARDING_PENDING -->"
TIMEOUT_S = 20
GATE_OFFER_RC = 0

# The model reads this, not the user. English on purpose (backend/internal
# prompt text), and the user is named generically -- this ships to instances
# whose user is addressed differently.
BLOCK_REASON_TMPL = (
    "Domain onboarding gate (pack_health): identity onboarding is complete, "
    "but this instance still has NO usable training card -- no goal, no body "
    "state, no injury history, no split. The gate measured that from the "
    "artifact, not from anyone's self-report, so you cannot settle it by "
    "saying it is settled.\n"
    "\n"
    "Do NOT end this turn on a capability list. Ending on 'here is what I can "
    "do for you' is the measured shape that got every previous instance of "
    "this agent deleted the same day.\n"
    "\n"
    "Before you speak again: START THE DOMAIN INTERVIEW NOW, in this turn. "
    "Entry point: %s. Open with its step 1 CONTINUATION OPENING "
    "(goal-session's first message, verbatim, nothing added: "
    "no transition line, never a stats dump). One question at a time, in "
    "the user's language.\n"
    "\n"
    "The gate closes when the card artifact exists, never when you announce "
    "that onboarding is done."
)
ENTRY_FALLBACK = "the health-onboarding entry skill"


def instance_root(data):
    env = os.environ.get("DOGANY_INSTANCE_ROOT")
    if env and os.path.isdir(env):
        return env
    cwd = data.get("cwd") if isinstance(data, dict) else None
    if cwd and os.path.isdir(cwd):
        return cwd
    here = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(os.path.dirname(here)))


def identity_pending(root):
    """True when the framework identity gate still owns this turn.

    Unreadable / missing identity file -> True (abstain). Abstaining is always
    safe here: the worst case is the offer waits one more turn, and the
    alternative is two hooks blocking the same turn.
    """
    path = os.path.join(root, IDENTITY_REL)
    try:
        with open(path, encoding="utf-8") as f:
            return MARKER in f.read()
    except Exception:
        return True


def gate_offer_entry(root):
    """Return the gate's ENTRY string when it OFFERs, else None.

    Same invocation shape as domain-onboarding-check.py (the SessionStart leg)
    on purpose: one pack, one way of asking its own gate. The ENTRY line is
    read rather than restated -- if the pack renames its entry skill, only the
    gate changes.
    """
    gate = os.path.join(root, GATE_REL)
    if not os.path.isfile(gate):
        return None
    try:
        proc = subprocess.run(
            [sys.executable, gate, "verdict", "--root", root],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_S,
        )
    except Exception:
        return None
    # exit 0 is the ONLY offer signal. 3 = no-offer, 1 = env error.
    if proc.returncode != GATE_OFFER_RC:
        return None
    for line in (proc.stdout or "").splitlines():
        parts = line.split("\t")
        if parts and parts[0].strip() == "ENTRY":
            entry = parts[-1].strip()
            if entry:
                return entry
    return ENTRY_FALLBACK


def main():
    try:
        raw = sys.stdin.read()
    except Exception:
        return 0
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}

    # One re-prompt per turn. A forcing point that can fire twice is a wedge.
    if data.get("stop_hook_active"):
        return 0

    # Owner-facing bridge session only: same predicate the framework Stop gate
    # uses. A cron/session-inbox turn has no user in it to interview.
    if not os.environ.get("PROJECT_ROOT"):
        return 0

    root = instance_root(data)

    # While the marker stands, the framework gate owns the turn. Never two.
    if identity_pending(root):
        return 0

    entry = gate_offer_entry(root)
    if not entry:
        return 0

    # LOG-ONLY (pack_health 0.17.1): a Stop-block fires AFTER the text already
    # reached the owner, so the bridge regeneration shows the owner the same
    # question twice (live 2026-09-25, DGN-1703 class). Record the would-block
    # and let the SessionStart offer carry the nudge. Re-enable blocking only
    # once the framework hook contract forbids Stop-block on owner-visible
    # turns and the bridge stops appending regenerations.
    try:
        log_dir = os.path.join(root, ".telegram_bot", "logs")
        with open(os.path.join(log_dir, "onboarding-gate.log"), "a") as fh:
            fh.write("%s domain-onboarding-stop would-block (log-only) entry=%s\n"
                     % (time.strftime("%Y-%m-%dT%H:%M:%S"), entry))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException:
        # Catch-all fail-open: never wedge a turn.
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
