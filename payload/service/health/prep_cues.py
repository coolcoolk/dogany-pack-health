"""prep_cues.py -- how ONE prep drill is told to the owner, from data.

WHY (live 2026-10-08 06:19-06:27, session 1). prep.yaml carried a one-line
`howto` per drill, the live entry plan never printed it, and the owner asked
what a roll-down is -- the agent improvised a standing roll-down. Then "what
is one rep?" on the bear crawl: the agent defined one rep as a pair and, in
the same breath, offered "or count one step". A cue the model composes is a
cue that changes between two sentences. So the whole cue is data:

    <display> . <dose>                     the header (NEXT_HINT)
    1 rep = ...                            what ONE counted rep / side is
    1. ... 2. ... 3. ...                   ordered steps (one line if single)
    <warning sign> ...                     the one common mistake

SOURCES, strongest first (owner-authored data always wins):
  1. the prep.yaml drill's own `steps` / `fault` / `rep_unit`
  2. the pack's prep_cues.json entry for the drill code (ko + en)
  3. the drill's one-line `howto` as a single step (still readable when 1-2
     have nothing -- the old shape degrades, it does not disappear)
ABSENT STAYS ABSENT: no step, fault or count unit is ever generated from the
drill's name.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "prep_cues.json")
FAULT_MARK = "\u26a0\ufe0f"
CUE_FIELDS = ("rep_unit", "steps", "fault")

# The dose header per language lives in the data file (`format`); per_side
# states BOTH sides explicitly (owner 2026-10-08), never a bare total.
LANGS = ("ko", "en")

_CACHE = {}


def _lang(lang=None):
    if lang in LANGS:
        return lang
    try:
        import ui_labels
        got = ui_labels.lang()
    except Exception:  # noqa: BLE001 -- no label layer -> the pack default
        got = "ko"
    return got if got in LANGS else "ko"


def _data(path=DATA):
    if path not in _CACHE:
        try:
            with open(path, encoding="utf-8") as fh:
                _CACHE[path] = json.load(fh)
        except (OSError, ValueError):
            _CACHE[path] = {}
    return _CACHE[path]


def load(path=DATA):
    """{code: {lang: cue}} from the data file ({} when unreadable)."""
    return _data(path).get("drills") or {}


def _fmt(lang=None):
    fmts = _data().get("format") or {}
    return fmts.get(_lang(lang)) or fmts.get("ko") or {}


def pack_cue(code, lang=None):
    """The pack's {rep_unit, steps, fault} for `code` in `lang` ({} if none)."""
    entry = load().get(code or "") or {}
    if not entry:
        import movement_cues
        entry = movement_cues.load().get(code or "") or {}
    return dict(entry.get(_lang(lang)) or entry.get("ko") or {})


def resolve(drill, lang=None):
    """{rep_unit, steps, fault} for one drill: its own fields, else the pack's,
    else `howto` as the one step. A field nobody declares is absent."""
    d = drill if isinstance(drill, dict) else {}
    pack = pack_cue(d.get("code"), lang)
    out = {}
    for key in CUE_FIELDS:
        val = d.get(key)
        if val in (None, "", []):
            val = pack.get(key)
        if val not in (None, "", []):
            out[key] = val
    if isinstance(out.get("steps"), str):
        out["steps"] = [out["steps"]]
    if not out.get("steps"):
        howto = d.get("howto") or ((d.get("cue") or {}).get("setup")
                                   if isinstance(d.get("cue"), dict) else None)
        if howto:
            out["steps"] = [str(howto)]
    return out


def dose_text(spec, lang=None, code=None):
    """The header's dose ('6 reps' / '6 each side' / '20s' in the owner's
    language, from the data file's `format`; '' if none). A drill whose count
    word is its own (bear crawl: steps per side; halo / arm circles: per
    direction -- kimwog exercise 741) carries a `dose` map that overrides
    `format` for that drill only."""
    f = dict(_fmt(lang))
    if not f:
        return ""
    own = pack_cue(code, lang).get("dose") if code else None
    if isinstance(own, dict):
        f.update(own)
    spec = spec if isinstance(spec, dict) else {}
    value, unit, hold = spec.get("value"), spec.get("unit"), spec.get("hold_sec")
    if hold is not None:
        if value in (None, 1):
            return f["sec"] % int(hold)
        return f["sec_sets"] % (int(hold), int(value))
    if value is None:
        return ""
    if unit == "per_side":
        return f["per_side"] % int(value)
    return f["reps"] % int(value)


def header(drill, spec, lang=None):
    """'<display> . <dose>' -- the one-line NEXT_HINT for a drill."""
    d = drill if isinstance(drill, dict) else {}
    name = d.get("display") or d.get("code") or ""
    dose = dose_text(spec, lang, d.get("code"))
    return ("%s \u00b7 %s" % (name, dose)) if dose else name


def _count(spec):
    spec = spec if isinstance(spec, dict) else {}
    if spec.get("hold_sec") is not None:
        return spec["hold_sec"]
    return spec.get("value")


def _kg(v):
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return ("%d" % f) if f.is_integer() else ("%g" % f)


def tool_text(drill):
    """The owner's RECORDED implement (+ the load when known): '<implement> 8kg' /
    '<implement>', or None when no implement is recorded. Owner 2026-10-08: an
    implement drill names the implement they actually use and its weight,
    never the catalog's generic 'a light dumbbell (or kettlebell)'. No default
    implement and no default load (ui_labels H2 contract)."""
    d = drill if isinstance(drill, dict) else {}
    imp = d.get("implement")
    if not (isinstance(imp, str) and imp.strip()):
        return None
    kg = _kg(d.get("load_kg")) if d.get("load_kg") is not None else None
    return "%s %skg" % (imp.strip(), kg) if kg else imp.strip()


def block(drill, spec, lang=None, ordinal=None):
    """The whole cue as lines: header, count unit, steps, fault."""
    cue = resolve(drill, lang)
    n = _count(spec)
    n = str(n) if n is not None else "N"
    tool = tool_text(drill)
    pack = pack_cue((drill or {}).get("code") if isinstance(drill, dict)
                    else None, lang)
    named = []

    def fill(text):
        text = str(text).strip().replace("{n}", n)
        if "{tool}" in text:
            named.append(True)
            text = text.replace("{tool}", tool or pack.get("tool_default")
                                or "")
        return text
    title = header(drill, spec, lang)
    if ordinal is not None:
        title = _fmt(lang)["item"].format(n=ordinal, item=title)
    lines = [title]
    if cue.get("rep_unit"):
        lines.append(fill(cue["rep_unit"]))
    steps = [s for s in cue.get("steps") or [] if str(s).strip()]
    if len(steps) == 1:
        lines.append(fill(steps[0]))
    else:
        lines += ["%d. %s" % (i, fill(s)) for i, s in enumerate(steps, 1)]
    if cue.get("fault"):
        lines.append("%s %s" % (FAULT_MARK, fill(cue["fault"])))
    if tool and not named:
        # the steps do not place the implement: say it on its own line,
        # right under the header
        fmt = _fmt(lang).get("implement")
        if fmt:
            lines.insert(1, fmt % tool)
    return lines


def missing(drill, lang=None):
    """The cue fields this drill cannot resolve (the lint's question)."""
    cue = resolve(drill, lang)
    return [k for k in CUE_FIELDS if not cue.get(k)]
