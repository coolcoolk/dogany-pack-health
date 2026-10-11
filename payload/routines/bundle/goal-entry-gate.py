#!/usr/bin/env python3
"""goal-entry-gate.py -- UserPromptSubmit hook: a bare goal-setting request
reaches the kit's goal interview, never an improvised scope menu.

WHY (carried in from the retired health agent, inherited-items 2026-09-15 #325)
  2026-08-23: the owner typed "목표설정다시하자" and the agent answered with a
  scope menu it wrote itself; the axis that was missing could not be on a menu
  built from what existed, so the session never reached it. 2026-08-24: a
  blank-recall "새 목표, 어떤 것부터 잡고 싶으세요?" and a goal interview run
  without --domain health (uncovered axes leaked across every domain). The
  procedure lived in a cold doc (consult-goal-part.md) the model opens only
  once it already knows it is in a consult -- and a bare goal request did not
  read as one. The retired agent's instance-level hook closed that; it died
  with the agent (no pack or kit shipped it). This is the same leg, shipped by
  the pack through the manifest hooks lane.

GUARANTEE BOUNDARY (stated honestly): the hook guarantees the INSTRUCTION IS
PRESENT in context on a matching turn, not that the model obeys it.

WHEN IT IS SILENT
  - not an owner-facing session, or identity onboarding still pending
  - the onboarding/program consult is live (program-plan state not written):
    domain-onboarding-prompt.py's CONSULT_RULES already own that turn, and
    restart there is `program-plan restart`, not the kit's --start
  - no goal-setting phrase in the first 400 chars of the prompt (a pasted blob
    that happens to contain the words is not a request)
  The predicates are domain-onboarding-prompt.py's own (loaded by path), so
  "interactive" / "identity pending" / "consult live" mean one thing.

THE SEAM (owner 2026-10-06 21:46, "the consult just stops"): the kit's
wrap says the next consult follows; the context makes the same reply continue
with `program-plan handoff` instead of a dead stop.

THE OWNER'S WORDS (2026-10-10): the instruction carries the prompt itself
as `goal-interview --start --said "<words>"`; the kit decides fork vs fresh
start. The installed kit's usage line picks the older-kit form (see OLDER
KIT RULE below).

CONTRACT: fail-open. Any error, missing sibling, unreadable input -> no
output, exit 0. Never blocks a prompt.

WIRING: pack-manifest.json hooks[] (event UserPromptSubmit); pack_install.sh
_hooks_wire writes it into .claude/settings.local.json.
"""

import sys
sys.dont_write_bytecode = True     # the sibling is loaded by path; no cache
                                   # beside it (C4b residue on a pack tree)

import importlib.machinery         # noqa: E402
import importlib.util              # noqa: E402
import json                        # noqa: E402
import os                          # noqa: E402
import re                          # noqa: E402
import shlex                       # noqa: E402
import subprocess                  # noqa: E402

HEAD_CHARS = 400

# Goal-setting entry phrasings (retired gate, measured misses included).
# Anchored on the NOUN 목표 so a lookup ("목표 칼로리 얼마야") does not trip it;
# broad on the verb side. English for mixed-language turns.
PATTERNS = (
    r"목표\s*\S{0,6}(설정|재설정|세팅)",
    r"목표\s*\S{0,6}(다시|새로|처음부터|리셋)",
    r"목표\s*\S{0,6}(잡|짜|세우|정하|바꾸|수정|변경|손보|손 보|고치|추가|올리|내리)",
    # 2026-09-11: "목표상담하고싶다" matched nothing -- the owner named the
    # ACTIVITY, not an edit verb.
    r"목표\s*\S{0,6}(상담|인터뷰|컨설팅|코칭|점검|리뷰|얘기|이야기|봐줘)",
    r"(상담|인터뷰)\s*\S{0,6}목표",
    r"(다시|새로|처음부터)\s*\S{0,6}목표",
    r"목표\s*(리셋|재정비|재조정)",
    r"\b(re-?do|reset|rebuild|redefine|change|update|set)\b[^.\n]{0,20}\bgoals?\b",
    r"\bgoals?\b[^.\n]{0,20}\b(again|from scratch|over)\b",
    r"\bnew goal\b",
    r"\bset (a|my|new) target\b",
)
RX = [re.compile(p, re.I) for p in PATTERNS]

# THE OWNER'S WORDS GO TO THE KIT (lifekit agent-rehearsal S1, a goal
# consult asked "from the start", 2026-10-10: 2 of 5 runs failed because this hook named the
# retired `goal-setting` skill, ran --start without the owner's words, and
# told the agent to speak the rebuild / adjust / add fork). The kit's
# `goal-interview --start --said "<words>"` decides fork vs fresh start in
# code; the agent asks the fork only when the tool returns it.
#
# OLDER KIT RULE (stated once): the installed kit's goal-interview usage line
# is read at runtime (`goal-interview --help`, read-only, short timeout).
#   usage has --said        -> --start --said "<words>"
#   usage known, no --said  -> fresh-start words (FRESH below) run
#                              --start --intent rebuild (when the usage has
#                              --intent), anything else --start alone
#   usage unreadable        -> --said, plus the same old-kit rule as the
#                              retry if the kit rejects --said
# In every case: never ask the fork unless the tool returned it.
SAID_CHARS = 1000
PROBE_TIMEOUT = 5

# Fresh-start wording (old-kit fallback only; a current kit decides itself).
FRESH = re.compile(
    "\uCC98\uC74C\uBD80\uD130|\uC0C8\uB85C|\uB9AC\uC14B|"    # cheoeumbuteo|saero|riset
    "\uC7AC\uC124\uC815|\uC7AC\uC815\uBE44|"                  # jaeseoljeong|jaejeongbi
    r"from scratch|\bre-?build\b|\breset\b|"
    r"\bnew goal\b|\bstart over\b", re.I)

# Model-facing (English, like the sibling hooks); every owner-facing line
# comes from the kit's moves.
HEAD = (
    "[goal-entry / pack_health] This message asks to set, redo or change "
    "goals. The kit's goal interview owns it: load the goal-session skill "
    "(.claude/skills/goal-session/SKILL.md, else "
    ".claude/skills-bundle/goal-session/SKILL.md%s) and run "
)
# A kit without --said predates goal-session and ships the skill under its
# older name; only that branch names it.
OLD_SKILL = ("; this older kit may ship it as .claude/skills/goal-setting/"
             "SKILL.md or .claude/skills-bundle/goal-setting/SKILL.md")
TAIL = (
    " (--domain health ALWAYS explicit). The tool decides between a fresh "
    "start, the card's wrap and its fork choice (the kit owns the list); ask the fork ONLY when "
    "the tool returned it (then verbatim), never on your own. Do NOT write a "
    "scope menu or an open 'which goal first?' question of your own -- a menu "
    "built from what exists cannot contain the axis that is missing. After "
    "that, one kit question per turn; numbers the records hold are "
    "confirmed, not asked; unknown values stay empty, never guessed. Neither "
    "skill file present -> say the goal interview is not installed and stop. "
    "WHEN THE KIT RETURNS ITS WRAP MOVE (the goal card complete) the consult "
    "does not stop there: in the SAME reply, right after the wrap, run "
    "`service/health/program-plan handoff` and send its move as the next "
    "message (no program yet -> the program consult's first question; a "
    "program in place -> one question, redo it for the new goal or keep it; "
    "answer with `program-plan answer --stage <answer.stage>`). Never wait "
    "for the owner to ask for the program."
)
KIT = "database/kit_life.sh goal-interview"


def owner_words(prompt):
    return (prompt or "").strip()[:SAID_CHARS]


def old_kit_cmd(words, has_intent=True):
    if has_intent and FRESH.search(words):
        return "`%s --start --intent rebuild --domain health --json`" % KIT
    return "`%s --start --domain health --json`" % KIT


def said_cmd(words):
    return "`%s --start --said %s --domain health --json`" % (
        KIT, shlex.quote(words))


def kit_usage(root):
    """The goal-interview usage text, or None when it cannot be read."""
    path = (os.environ.get("KIT_LIFE_SH")
            or os.path.join(root, "database", "kit_life.sh"))
    if not os.path.isfile(path):
        return None
    try:
        p = subprocess.run([path, "goal-interview", "--help"],
                           capture_output=True, text=True,
                           timeout=PROBE_TIMEOUT, stdin=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError):
        return None
    text = "%s\n%s" % (p.stdout or "", p.stderr or "")
    if "goal-interview" not in text or "--start" not in text:
        return None
    return text


def context(prompt, usage):
    words = owner_words(prompt)
    if usage is not None and "--said" not in usage:
        cmd = old_kit_cmd(words, "--intent" in usage)
        return (HEAD % OLD_SKILL) + cmd + " -- this kit has no --said" + TAIL
    cmd = said_cmd(words)
    if usage is None:
        note = (" -- --said carries the owner's words verbatim; if the kit "
                "rejects --said (older kit), run " + old_kit_cmd(words) +
                " instead")
    else:
        note = " -- --said carries the owner's words verbatim"
    return (HEAD % "") + cmd + note + TAIL


def matches(prompt):
    if not isinstance(prompt, str):
        return False
    head = prompt.strip()[:HEAD_CHARS]
    return bool(head) and any(rx.search(head) for rx in RX)


def sibling():
    """domain-onboarding-prompt.py as a module (its predicates), or None."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "domain-onboarding-prompt.py")
    if not os.path.isfile(path):
        return None
    loader = importlib.machinery.SourceFileLoader("_dop_for_goal_gate", path)
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def main():
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except Exception:
        return 0
    if not isinstance(data, dict) or not matches(data.get("prompt")):
        return 0
    dop = sibling()
    if dop is None or not dop.session_is_interactive():
        return 0
    root = dop.instance_root(data)
    if dop.identity_pending(root) or dop.consult_live(root):
        return 0
    dop.emit(context(data.get("prompt"), kit_usage(root)))
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
