"""Explicit bilingual movement instructions shared by lift and drill prompts.

The string-only i18n bundle remains compatible with kit lookup. Ordered cue
arrays live here as JSON data, beside prep_cues.json, rather than being coerced
into strings by that lookup. A missing translation never falls back silently.
"""
import json
import os
from functools import lru_cache

HERE = os.path.dirname(os.path.abspath(__file__))


@lru_cache(maxsize=1)
def load():
    with open(os.path.join(HERE, "movement_cues.json"), encoding="utf-8") as f:
        return json.load(f)["movements"]


def cue(code, lang="ko"):
    import prep_cues
    entry = load().get(code) or prep_cues.load().get(code) or {}
    return dict(entry.get(lang) or {})


def lines(code, lang="ko", recorded=None):
    data = cue(code, lang)
    for key in ("steps", "fault"):
        if (recorded or {}).get(key):
            data[key] = recorded[key]
    steps = data.get("steps") or []
    if isinstance(steps, str):
        steps = [steps]
    result = ["%d. %s" % (i, s) for i, s in enumerate(steps, 1)]
    if data.get("fault"):
        result.append("\u26a0\ufe0f " + data["fault"])
    return result


def attach(payload):
    """Put the cue INSIDE the keyboard prompt, including marker-only delivery.

    Machine-selection arms also carry exercise_name and step text. Only attach
    to set-add callbacks; preserve command and button data and stay idempotent.
    """
    if payload.get("movement_cue_attached") or not payload.get("step_text"):
        return payload
    cmd = payload.get("cmd") or []
    if not cmd or os.path.basename(str(cmd[0])) != "set-add":
        return payload
    import ui_labels
    lang = ui_labels.lang()
    code = payload.get("exercise_name")
    # ONE cadence owner (cue.py): the full cue once per lift per session, then
    # one rotating tip per set. Never the full block on every set (owner 07:52).
    import cue
    shown = cue.card(payload.get("session_id"), code, payload.get("set_seq"),
                     lang)
    body = shown["lines"]
    if not body:
        return payload
    name = ui_labels.i18n("movement." + code)
    dose = []
    if payload.get("weight") is not None:
        dose.append("%gkg" % float(payload["weight"]))
    if payload.get("target_reps") is not None:
        dose.append(ui_labels.i18n("health.undo.reps", n=payload["target_reps"]))
    if dose:
        name += " \u00b7 " + " \u00d7 ".join(dose)
    text = payload["step_text"].get("1")
    if not text:
        return payload
    payload["step_text"] = dict(payload["step_text"])
    payload["step_text"]["1"] = "\n".join([name] + body + [text])
    payload["movement_cue_attached"] = True
    return payload
