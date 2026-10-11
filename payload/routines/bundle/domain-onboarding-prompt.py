#!/usr/bin/env python3
"""domain-onboarding-prompt.py -- UserPromptSubmit fallback for the pack_health
domain gate. The "never silently dies" leg, with no Stop-block.

WHY THIS EXISTS (measured 2026-09-25, retired instance 946a82d5):
  The identity close is supposed to carry the owner straight into goal
  onboarding (framework POST-IDENTITY CONTINUATION CHECK, DGN-1632). On the
  live run it did not: the close ended on a settings recap and the domain step
  only started because the pack Stop hook blocked the turn -- and a Stop-block
  arrives AFTER the text already reached the owner, so the regeneration opened
  cold on a records dump with a start-now consent button. 0.17.1 made the Stop hook
  LOG-ONLY to stop the duplicate question. That left nothing at all to carry
  the owner forward when the inline continuation is skipped: the 2026-09-15
  "why does it stop here" hole (DGN-1487) was open again.

  This hook closes it BEFORE generation instead of after: on the owner's NEXT
  message, if the gate still says OFFER for a card that was never offered,
  the model is told to open goal onboarding in that reply, using the opening
  shape the health-onboarding skill owns (step 1, CONTINUATION OPENING).
  Nothing is shown twice, because nothing was shown yet.

SINGLE SOURCE: service/health/onboarding-gate. This file decides nothing on
its own. It reads `onboarding-gate state` (the same inputs the verdict is
built on) and fires only when ALL of these hold:
  - verdict == OFFER and reason == absent (no card at all; registry-drift and
    invalid are resumes, not openings, and the SessionStart leg names them)
  - offers == 0 and declines == 0 (never offered, never declined)
  - identity marker absent (the framework identity gate owns the turn
    otherwise -- checked here as well as by the gate, belt and braces)
  - owner-facing bridge session (same predicate as the framework gates)

NEVER TWICE: before printing, it records the offer through the gate itself
(`onboarding-gate offered --by domain-onboarding-prompt`). The next prompt
then reads offers >= 1 and stays silent. If that write fails, it prints
nothing -- an offer it cannot record is an offer it could repeat.

CONTRACT (fail-open, always): any error, timeout, missing gate, malformed
state, or unexpected shape -> no output, exit 0. Never blocks a prompt,
never prints a traceback.

SECOND LEG, THE LIVE CONSULT (journey 2026-09-26, DELTA 2 "emoji / praise /
escape" row, the 2-tier carrier). While the onboarding consult is live --
service/health/program-plan has a plan state that is not written yet and not
paused -- every owner prompt gets CONSULT_RULES: speak the tool's lines
verbatim, no persona emoji or praise in the consult, the side-question rule,
restart = `program-plan restart` only, corrections ride the answer. It
decides nothing and records nothing; the plan state is only read.

THIRD LEG, THE SETUP TAIL (owner 2026-10-06 21:46). After the program is
written, program-plan keeps `tail: open` until the "all set" wrap (diet,
first session, brief / retro times). Every owner prompt meanwhile gets
TAIL_RULES: serve an unrelated request first, then send the open step's
move -- a user who left mid-way is resumed there, never dropped.

WIRING: declared in pack-manifest.json hooks[] (event UserPromptSubmit);
pack_install.sh (_hooks_wire) writes it into .claude/settings.local.json.
routines/bundle/domain-onboarding-wire.sh carries the same leg for instances
installed before 0.17.2.
"""

import json
import os
import subprocess
import sys

GATE_REL = os.path.join("service", "health", "onboarding-gate")
IDENTITY_REL = os.path.join("identity", "hot.custom.agent.md")
MARKER = "<!-- ONBOARDING_PENDING -->"
TIMEOUT_S = 15
OFFERED_BY = "domain-onboarding-prompt"

# The model reads this, not the owner. English on purpose (internal prompt
# text); the owner-facing wording lives in the skill, in one place.
CONTEXT = (
    "[domain-onboarding / pack_health] Identity setup finished in an earlier "
    "turn, but goal onboarding never started: this instance has no training "
    "card and the owner has not been offered it yet (measured by "
    "service/health/onboarding-gate, not self-reported). In THIS reply, open "
    "goal onboarding as the continuation of the setup that just finished. "
    "Load the health-onboarding skill and use its step 1 CONTINUATION OPENING "
    "(the later-turn leg opens the same way as every leg): run "
    "`service/health/program-plan next` and speak the move's readback then say "
    "(the goal consult's own first message: intro, empty goal card, the G1 "
    "open question with its three examples) "
    "verbatim, with nothing of your own before it: no transition line, no "
    "settings recap, no quote or stats dump. No easy-out line (no 'later' sentence, journey K8). No "
    "consent question before G1, no buttons. The offer is already "
    "recorded -- do not run `onboarding-gate "
    "offered` again. If the owner's message is a concrete request, serve it "
    "first in a line or two, then append that move. If the owner's message "
    "postpones or declines setup, run `service/health/onboarding-gate "
    "declined` and do not ask. If the owner's message explicitly asks for the "
    "goal consult, the goal-session skill owns the turn: its first message IS "
    "this opening, add nothing. One setup offer per reply: if a SessionStart "
    "[domain-onboarding] line is also in context, it is this same offer."
)


PLAN_STATE_REL = os.path.join("files", "program", ".program-plan.json")

# The live consult, every turn (model-facing, English on purpose). The words
# the owner reads are the tool's (program-plan / the kit's moves); this only
# keeps the model from writing around them.
CONSULT_RULES = (
    "[health consult / pack_health] The onboarding consult is live "
    "(service/health/program-plan holds its state; measured, not recalled). "
    "This turn: (1) speak the move's `readback` lines then `say` VERBATIM as "
    "ONE message and offer its `choices` as the buttons; write no sentence of "
    "your own around a move -- no praise or cheering, no emoji (persona "
    "emoji are off while the consult runs), no 'later' escape line, "
    "no step preview or step count. (2) A side question (the owner asks "
    "something instead of answering): answer it in your own words in at most "
    "3 sentences (1-2 is the aim); a claim about how a lift loads a joint or "
    "a muscle (angle, grip, range, which version of the lift is easier on a site) is "
    "looked up first in knowledge/kimwog (`grep -ril <term> "
    "knowledge/kimwog/items`; shoulder pressing: "
    "exercise/shoulder-pressing-selection-cuff-work-064; bench angle: the "
    "item carrying `press_angle_rules`, `grep -rl press_angle_rules "
    "knowledge/kimwog/items`) and said only as "
    "far as the item grades it. Then run `service/health/program-plan "
    "reask` and send its ONE `say` line with its `choices` as the SAME "
    "buttons -- never re-send the program card, the readback, the session "
    "lists or the option bodies (already on screen) and never ask the owner "
    "to type an answer again; nothing was answered, nothing moved. (3) "
    "'start over' / 'from the goal again', in the owner's own words -> "
    "`service/health/program-plan restart` (`--from program` when only the "
    "program is to be redone): the ONLY restart path; never reset the state "
    "or re-run the interview by hand. (4) A correction riding an answer "
    "(e.g. 'option 1, but Friday is 6-8') goes into that answer's payload "
    "(`patch`), never a question back. (5) If the owner says 'later' first, "
    "answer with `pick: later` and stop; never offer it."
)


# The setup tail, every turn until its wrap (owner 2026-10-06 21:46: the
# first run is ONE conversation; a user who leaves mid-way is resumed at the
# open step). Model-facing, English on purpose.
TAIL_RULES = (
    "[health setup / pack_health] The program is written and the first-run "
    "setup still has open steps (diet target, first session, brief / retro "
    "times -- measured from program-plan's state, not recalled). This turn: "
    "if the owner asked for something else (starting a session, logging a "
    "meal), serve it first. Then -- or when the message answers the open "
    "step -- run `service/health/program-plan next` (or `program-plan answer "
    "--stage <its answer.stage> --json '<payload>'` with the owner's answer) "
    "and send the move as ONE message: `say` verbatim, `choices` as the "
    "buttons, no sentence of your own around it, no 'later' line, no step "
    "preview. A skip in the owner's own words is an answer (diet: pick skip; "
    "a brief / retro time: pick off). 'later' first -> `pick: later`, stop."
)


def _plan_state(root):
    base = os.environ.get("WARG_DATA_DIR")
    path = (os.path.join(base, ".program-plan.json") if base
            else os.path.join(root, PLAN_STATE_REL))
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def tail_live(root):
    """True while program-plan's setup tail is open (written, tail=open,
    not paused). Any error -> False (fail-open: say nothing)."""
    try:
        st = _plan_state(root)
    except Exception:
        return False
    return (isinstance(st, dict) and bool(st.get("written"))
            and st.get("tail") == "open" and st.get("offer") != "later")


def consult_live(root):
    """True while program-plan's state exists, is not written and is not
    paused. Any error -> False (fail-open: say nothing)."""
    base = os.environ.get("WARG_DATA_DIR")
    path = (os.path.join(base, ".program-plan.json") if base
            else os.path.join(root, PLAN_STATE_REL))
    try:
        with open(path, encoding="utf-8") as f:
            st = json.load(f)
    except Exception:
        return False
    return (isinstance(st, dict) and bool(st) and not st.get("written")
            and st.get("offer") != "later")


def emit(context):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": context,
    }}), flush=True)


def session_is_interactive():
    override = os.environ.get("DOGANY_SESSION", "").strip().lower()
    if override in ("interactive", "owner", "live"):
        return True
    if override in ("auto", "autonomous", "cron", "headless"):
        return False
    return bool(os.environ.get("PROJECT_ROOT"))


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
    """Marker present, or identity file unreadable/missing -> True (abstain)."""
    try:
        with open(os.path.join(root, IDENTITY_REL), encoding="utf-8") as f:
            return MARKER in f.read()
    except Exception:
        return True


def run_gate(root, *args):
    gate = os.path.join(root, GATE_REL)
    if not os.path.isfile(gate):
        return None
    try:
        return subprocess.run(
            [sys.executable, gate] + list(args) + ["--root", root],
            capture_output=True, text=True, timeout=TIMEOUT_S)
    except Exception:
        return None


def should_fire(state):
    if not isinstance(state, dict):
        return False
    return (state.get("verdict") == "OFFER"
            and state.get("reason") == "absent"
            and state.get("identity") == "set"
            and state.get("offers") == 0
            and state.get("declines") == 0)


def main():
    try:
        raw = sys.stdin.read()
    except Exception:
        raw = ""
    try:
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        data = {}
    if not isinstance(data, dict):
        data = {}

    if not session_is_interactive():
        return 0
    root = instance_root(data)
    if identity_pending(root):
        return 0
    # A newly logged weight or InBody reading reaches the pin on the next
    # owner turn, including days without a workout. The daily rx job also
    # refreshes the section at Monday rollover.
    workbench = os.path.join(root, "service", "health", "workbench.py")
    if os.path.isfile(workbench):
        try:
            subprocess.run([sys.executable, workbench], capture_output=True,
                           timeout=20, check=False)
        except (OSError, subprocess.TimeoutExpired):
            pass

    if consult_live(root):
        emit(CONSULT_RULES)
        return 0
    if tail_live(root):
        emit(TAIL_RULES)
        return 0

    proc = run_gate(root, "state")
    # state exits 0 on OFFER, 3 on NO-OFFER, 1 on env error.
    if proc is None or proc.returncode != 0:
        return 0
    try:
        state = json.loads(proc.stdout or "")
    except Exception:
        return 0
    if not should_fire(state):
        return 0

    rec = run_gate(root, "offered", "--by", OFFERED_BY)
    if rec is None or rec.returncode != 0 or not (rec.stdout or "").startswith("OFFERED"):
        return 0

    emit(CONTEXT)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except BaseException:
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
