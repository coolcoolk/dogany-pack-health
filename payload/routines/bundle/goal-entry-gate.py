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

# Model-facing (English, like the sibling hooks); every owner-facing line
# comes from the kit's moves.
CONTEXT = (
    "[goal-entry / pack_health] This message asks to set, redo or change "
    "goals. The kit's goal interview owns it: load the goal-setting skill "
    "(.claude/skills/goal-setting/SKILL.md, else "
    ".claude/skills-bundle/goal-setting/SKILL.md) and run "
    "`database/kit_life.sh goal-interview --start --domain health --json` "
    "(--domain health ALWAYS explicit). Its first question is the kit's own "
    "rebuild / adjust / add choice; speak it verbatim. Do NOT write a scope "
    "menu or an open 'which goal first?' question of your own -- a menu built "
    "from what exists cannot contain the axis that is missing. After that, one "
    "kit question per turn; numbers the records hold are confirmed, not asked; "
    "unknown values stay empty, never guessed. Neither skill file present -> "
    "say the goal interview is not installed and stop."
)


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
    dop.emit(CONTEXT)
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
