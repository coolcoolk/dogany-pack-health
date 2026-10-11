#!/usr/bin/env python3
"""machine_contradiction.py -- the CONTRADICTION carrier (owner 2026-10-10:
the agent and the machine never reconcile on screen).

WHY
    12:50 and 12:51, free session: code posted a 40kg rung keyboard and a
    "next row 50kg x 10" table row from a stale target, and the agent's own reply
    told the owner to ignore that row, twice. The model
    and the machine contradicted each other on screen, and the wrong row
    stayed up because nothing changed the state that drew it.

RULE
    A code post the agent judges wrong is fixed by CHANGING THE STATE through
    a verb, so code re-posts the right thing:
      wrong target weight      set-arm <sid> <ex> <seq> --ov-weight <kg>
                               --ov-reason "..." (--ov-by owner when the
                               owner named it)
      set in the wrong lane    set-reclass <sid> <ex> <seq> --to ramp|working
      row that should not be   set-undo <sid> <ex> <seq>
    Telling the owner to ignore a machine post is never the fix.

WHAT (deterministic, string arithmetic only)
    At turn start, read the assistant reply to the owner's previous message
    (question_close.previous_exchange -- same transcript reader). When it
    tells the owner to ignore / disregard something on screen, inject the
    rule above with the offending excerpt, so THIS turn changes the state
    first. Live session only (the caller gates on the active marker);
    read-only; fail-open; capped at BUDGET_BYTES.

stdlib only. ASCII source: the Korean domain vocabulary is unicode-escaped.
"""
import importlib.util
import os
import re

BUDGET_BYTES = 700
EXCERPT_CHARS = 140

# "ignore it" addressed to the owner, about something on screen.
_IGNORE = re.compile(
    "(\ubb34\uc2dc(\ud558\uc138\uc694|\ud574\\s*\uc8fc\uc138\uc694|\ud558\uc154\ub3c4|\ud558\uc2dc\uba74|\ud574\ub3c4\\s*\ub3fc|\ud558\uace0)|"
    "\uc2e0\uacbd\\s*(\uc4f0\uc9c0\\s*\ub9c8|\uc548\\s*\uc4f0\uc154\ub3c4)|"
    "(\uce78|\ubc84\ud2bc|\uc54c\ub9bc|\ud0c0\uc774\uba38|\ud45c)[^\\n.]{0,20}(\ud2c0\ub838|\uc798\ubabb\\s*(\ub5b4|\ub098\uc654|\ub410))|"
    "\\bignore (it|that|the)\\b)")


def _qc():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "question_close.py")
    spec = importlib.util.spec_from_file_location("question_close_mc", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def offending(reply):
    """The clause of `reply` that tells the owner to ignore a machine post,
    or None."""
    for clause in re.split(r"[\n]+|(?<=[.!?])\s+", reply or ""):
        if _IGNORE.search(clause):
            one = " ".join(clause.split())
            return one if len(one) <= EXCERPT_CHARS else one[:EXCERPT_CHARS] + "..."
    return None


def build_context(excerpt):
    text = ("[MACHINE-CONTRADICTION] Your last reply told the owner to ignore "
            "something code put on screen: \"%s\". Before anything else this "
            "turn, CHANGE THE STATE so code re-posts the right thing: wrong "
            "target -> set-arm <sid> <ex> <seq> --ov-weight <kg> --ov-reason "
            "\"...\"; set in the wrong lane -> set-reclass <sid> <ex> <seq> "
            "--to ramp|working; a row that should not exist -> set-undo. "
            "Then say what changed in one line. Never tell the owner to ignore "
            "a machine post." % excerpt)
    raw = text.encode("utf-8")
    if len(raw) > BUDGET_BYTES:
        text = raw[:BUDGET_BYTES - 3].decode("utf-8", "ignore") + "..."
    return text


def compute(hook_input):
    """hook stdin dict -> context string or None. Never raises."""
    try:
        path = (hook_input or {}).get("transcript_path")
        if not path or not os.path.isfile(path):
            return None
        ex = _qc().previous_exchange(path, (hook_input or {}).get("prompt"))
        if not ex:
            return None
        hit = offending(ex[1])
        return build_context(hit) if hit else None
    except Exception:  # noqa: BLE001 -- fail-open
        return None
