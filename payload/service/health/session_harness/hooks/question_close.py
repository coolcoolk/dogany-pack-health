#!/usr/bin/env python3
"""question_close.py -- QUESTION-CLOSE carrier: the owner's unanswered question
is carried into the next turn (ticket 2026-08-09-question-close-
deterministic-carrier, RC8 answer-and-advance, D2 rung 1).

WHY
    workout-session's turn contract is answer-and-advance: every turn logs /
    arms / cues AND closes any question the owner asked. The only guard was the
    skill text itself ("no code gate exists", F16) and a live turn is exactly
    where it slips: the model advances the set and the owner's "왜 70이야?"
    goes unanswered, then the next message has moved on and the question is
    lost. The retired instance-local question-close-check.py looked the other way (the
    ASSISTANT's own trailing question) and was never wired.

WHAT (deterministic, no model, no NLP library)
    At turn start, read the transcript the harness hands every
    UserPromptSubmit hook (`transcript_path`). Take the owner's PREVIOUS
    message and the assistant text that answered it. Inject a reminder iff
      Q  that message is a question -- '?' or a Korean interrogative
         (왜/뭐/어떻게/언제/몇/얼마/... or a sentence ending -냐/-니/-나요/
         -까요/-ㄹ까/-는지/-인가 ...), AND
      U  the reply did not visibly address it -- no reply text at all (only
         tool calls / buttons), or no content bigram in common with the
         question once the interrogative words are removed.
    Both tests are string arithmetic; the same transcript always gives the
    same answer. The carrier does not decide the answer, it makes the open
    question impossible to lose: the model reads it on the next turn.

SCOPE
    Live session only, the same gate as turn_pre (the active marker): the
    answer-and-advance contract is the workout-session skill's, and the owner
    ruling of 2026-09-30 puts per-turn injection inside a live session only.

RULES (same shape as turn_pre)
    read-only; fail-open (any error -> no injection); a no-op emits nothing;
    capped at BUDGET_BYTES.

stdlib only. ASCII source except the Korean interrogative literals, which ARE
the domain vocabulary being matched.
"""
import json
import os
import re

BUDGET_BYTES = 600
EXCERPT_CHARS = 160
MIN_REPLY_CHARS = 12

# Interrogative words (anywhere) and sentence endings (end of a clause).
_WH = re.compile(
    "(왜|뭐|뭘|무슨|어떻게|어떡|"
    "언제|어디|얼마|몇|누가|어느|"
    "어때)")
_END = re.compile(
    "(냐|니|나요|까요|을까|를까|"
    "는지|은지|인지|인가|는가|아냐|어냐|"
    "죠)\\s*[.!~]*\\s*$")
# bare -나 is left out on purpose: "하나 더 했어" / "이따 하나" are statements.
_TOKEN = re.compile("[0-9A-Za-z가-힣]+")


def is_question(text):
    if not text:
        return False
    if "?" in text or "？" in text:
        return True
    if _WH.search(text):
        return True
    for clause in re.split(r"[\n.!]+", text):
        if _END.search(clause.strip()):
            return True
    return False


def _bigrams(text):
    out = set()
    for tok in _TOKEN.findall(_WH.sub(" ", text or "")):
        tok = tok.lower()
        if len(tok) == 1:
            continue
        for i in range(len(tok) - 1):
            out.add(tok[i:i + 2])
    return out


def unanswered_reason(question, reply):
    """None when the reply visibly addresses the question, else a reason."""
    body = "".join(_TOKEN.findall(reply or ""))
    if len(body) < MIN_REPLY_CHARS:
        return "no_reply_text"
    q = _bigrams(question)
    if not q:
        return None          # nothing to compare on: do not guess
    if not (q & _bigrams(reply)):
        return "reply_shares_nothing_with_the_question"
    return None


# ---------------------------------------------------------------------------
# transcript
# ---------------------------------------------------------------------------
def _text_of(content):
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for b in content:
            if isinstance(b, dict) and b.get("type") == "text" and b.get("text"):
                parts.append(b["text"].strip())
        return "\n".join(p for p in parts if p).strip()
    return ""


def _is_tool_result(content):
    return isinstance(content, list) and any(
        isinstance(b, dict) and b.get("type") == "tool_result"
        for b in content)


def turns(transcript_path):
    """[(role, text)] in order: owner messages and assistant TEXT, with tool
    traffic dropped and consecutive assistant texts merged."""
    out = []
    with open(transcript_path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except ValueError:
                continue
            kind = o.get("type")
            msg = o.get("message") or {}
            content = msg.get("content")
            if kind == "user":
                if o.get("isMeta") or _is_tool_result(content):
                    continue
                t = _text_of(content)
                if t:
                    out.append(["user", t])
            elif kind == "assistant":
                t = _text_of(content)
                if out and out[-1][0] == "assistant":
                    if t:
                        out[-1][1] = (out[-1][1] + "\n" + t).strip()
                else:
                    out.append(["assistant", t])
    return [tuple(x) for x in out]


def previous_exchange(transcript_path, current_prompt=None):
    """(owner_question_text, assistant_reply_text) for the exchange BEFORE the
    current prompt, or None."""
    seq = turns(transcript_path)
    if seq and seq[-1][0] == "user" and (
            current_prompt is None or seq[-1][1] == (current_prompt or "").strip()):
        seq = seq[:-1]           # the prompt of THIS turn, if already logged
    for i in range(len(seq) - 1, -1, -1):
        if seq[i][0] == "user":
            reply = " ".join(t for r, t in seq[i + 1:] if r == "assistant")
            if i + 1 >= len(seq):
                return None      # never replied to: not an exchange yet
            return seq[i][1], reply
    return None


def _excerpt(text):
    one = " ".join(text.split())
    return one if len(one) <= EXCERPT_CHARS else one[:EXCERPT_CHARS] + "..."


def build_context(question, reason):
    text = ("[QUESTION-CLOSE] The owner's previous message asked a question "
            "your reply did not visibly address (%s). Answer it in THIS turn, "
            "alongside advancing the session -- or say plainly why it cannot "
            "be answered. Never drop it silently.\nOwner asked: %s"
            % (reason, _excerpt(question)))
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
        ex = previous_exchange(path, (hook_input or {}).get("prompt"))
        if not ex:
            return None
        question, reply = ex
        if not is_question(question):
            return None
        reason = unanswered_reason(question, reply)
        if reason is None:
            return None
        return build_context(question, reason)
    except Exception:            # noqa: BLE001 -- fail-open
        return None
