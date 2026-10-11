#!/usr/bin/env python3
"""domain-onboarding-check.py -- SessionStart signal for pack_health.

WHY THIS EXISTS (measured 2026-09-15):
  A freshly minted health agent finishes IDENTITY onboarding and then stops.
  The domain interview (goal / body state / injuries / split) never starts on
  its own, so the agent is born claiming capabilities it cannot serve and the
  owner's first "운동 시작" hits session-open exit 1.

  The verdict machinery already exists and is correct:
      service/health/onboarding-gate verdict
          exit 0 -> OFFER    (identity done, no usable card, owner not asked)
          exit 3 -> NO-OFFER (complete / identity pending / declined)
  What was missing is a CALLER. The gate shouted into a room with nobody in it.
  health-onboarding/SKILL.md declares it fires "immediately after identity
  onboarding", but a skill description is not a forcing point -- firing depended
  on best-effort description matching, and it did not fire. Measured: owner
  re-minted four times in one day chasing this.

  This script is that caller. It runs at SessionStart, asks the gate, and when
  the gate says OFFER it prints ONE line into the session context naming the
  entry skill. Code decides; the model is told, not trusted to remember.

CONTRACT (fail-open, always):
  - gate missing / not executable / errors / times out -> print nothing, exit 0
  - gate says NO-OFFER                                 -> print nothing, exit 0
  - anything unexpected                                -> print nothing, exit 0
  Never blocks a session, never prints a traceback, never errors out. A silent
  no-op is always a valid outcome; a broken session is not.

LANE: pack_health asset. It knows its own service path on purpose -- a pack
knowing its own layout is not a layer violation. The FRAMEWORK must not learn
domain conventions (that is the framework's slot contract, DGN-1487); this file is the
kit side of that same seam, usable today without waiting for the slot.

WIRING: registered in the instance's .claude/settings.local.json SessionStart
hooks -- NOT settings.json, which update.sh regenerates wholesale and has
dropped instance-local hook wiring four times (DGN-1250). settings.local.json is
instance-only and untracked by the framework, so this wiring survives updates.
"""

import os
import subprocess
import sys

GATE_REL = os.path.join("service", "health", "onboarding-gate")
TIMEOUT_S = 20


def instance_root():
    # env override first (matches how framework hooks are invoked), else derive
    # from this file's location: <root>/routines/bundle/this.py -> <root>
    env = os.environ.get("DOGANY_INSTANCE_ROOT") or os.environ.get("ONBOARDING_FILE")
    if env and os.path.isdir(env):
        return env
    here = os.path.abspath(__file__)
    return os.path.dirname(os.path.dirname(os.path.dirname(here)))


def main():
    root = instance_root()
    gate = os.path.join(root, GATE_REL)
    if not (os.path.isfile(gate) and os.access(gate, os.X_OK)):
        return 0

    try:
        proc = subprocess.run(
            [sys.executable, gate, "verdict", "--root", root],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_S,
        )
    except Exception:
        return 0

    # exit 0 is the ONLY offer signal. 3 = no-offer, 1 = env error, others unknown.
    if proc.returncode != 0:
        return 0

    entry = ""
    for line in (proc.stdout or "").splitlines():
        parts = line.split("\t")
        if parts and parts[0].strip() == "ENTRY":
            entry = parts[-1].strip()
            break

    # The gate's own ENTRY string names the skill. Do not restate it here --
    # if the pack renames the entry skill, this file must not have to change.
    if not entry:
        entry = "health-onboarding skill"

    # English on purpose (the model reads it). The owner-facing wording is the
    # skill's step 1 CONTINUATION OPENING, kept in one place (0.17.2).
    print(
        "[domain-onboarding] Identity onboarding is done; domain (goal) "
        "onboarding is not. Continue it in this session -- entry: " + entry + ". "
        "Recheck with service/health/onboarding-gate verdict first; on NO-OFFER "
        "say nothing about setup. Open with the skill's step 1 CONTINUATION "
        "OPENING: goal-session's first message (service/health/program-plan "
        "next), verbatim -- no transition line, no settings recap, no consent "
        "question, no records dump."
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
