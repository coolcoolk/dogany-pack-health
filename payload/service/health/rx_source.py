#!/usr/bin/env python3
# rx_source.py -- THE PRESCRIPTION OF RECORD: every set-start number, with the
# name of the code path that produced it.
#
# ---------------------------------------------------------------------------
# WHY THIS FILE EXISTS (2026-09-11, two incidents, one exercise, three minutes)
# ---------------------------------------------------------------------------
# A. standing_calf_raise, session 10103. `program.yaml` carries
#    `weight_kg: null` (a deliberate calibration sentinel), so rx-calc
#    prescribed nothing and the 세트표 WT column rendered `? / ? / ?`. The turn
#    then said "지난 세션(08/25) 105kg ... 증량으로 갈게요: 115kg" and warmed the
#    owner up AT 115kg. The engine, handed 115, produces 세팅 55 / 웜업 75 /
#    웜업 95 -- so 115 was never a warm-up any code path had computed. It was
#    minted in prose and then written to the DB as set_seq -1, weight 115.0.
#
# B. The same exercise, two minutes later: a switch to single-leg execution was
#    announced. `program.yaml` declares `unilateral` on exactly one slot in the
#    file and this is not it; ax_exercise says isolation / reps / machine. At
#    115kg, 양발 -> 한발 doubles the load per leg. The owner: 「스탠딩은 양발이야」.
#
# ONE ROOT. Both numbers were minted in the gap where code emitted NOTHING. The
# weight axis was silent because it was unresolved; the side axis was silent
# because nothing was declared. Silence is not a null value to a language model
# -- it is an invitation, and it was accepted twice in three minutes.
#
# ---------------------------------------------------------------------------
# THE RULE THIS FILE MAKES MECHANICAL (owner ruling, 2026-09-11)
# ---------------------------------------------------------------------------
#   세트 시작 발화의 처방값(무게 / 편측 / 반복수 / RIR)은 코드가 낸 값만 쓴다.
#   모델은 그 값을 설명할 수는 있어도 새 값을 만들 수 없다.
#
# THE DESIGN CHOICE, and why it is not the other one. Two candidates were on the
# table: (1) ship a deterministic payload and let the utterance fill declared
# tokens, or (2) let the utterance be composed and verify it afterwards against
# the code values.
#
# (2) CANNOT BE BUILT FROM HERE, and saying so is part of the design. This pack
# ships CLI tools; nothing in it can read, edit or refuse the turn's outgoing
# chat text. events.py rosters a TurnPost carrier for exactly that job and it
# has never had one. A "verifier" the turn is asked to call on itself is prose
# discipline wearing a costume -- and prose discipline is the surface that
# failed five times today.
#
# So the mechanism is (1), plus the one enforcement point that is genuinely in
# reach: THE WRITE PATH. Three moves, and the third is what makes the first two
# bind:
#
#   1. NO SILENT AXIS. Every prescription axis is emitted on every arm, with a
#      value AND a source -- including when the value is UNKNOWN. There is no
#      state in which the wire says nothing about the weight, so there is no
#      vacuum left to fill. This is the same move set-table made for the ramp
#      ("the decision is now a VALUE, not an absence") applied to all four axes.
#
#   2. UNKNOWN IS A SENTENCE, NOT A BLANK. An unresolved axis emits the Korean
#      ask that says so. The relay reads "몇 kg으로 가실지 알려주세요", which is
#      a thing to SAY -- it competes with inventing a number instead of leaving
#      the field open.
#
#   3. THE WRITE IS VERIFIED. verify() compares what a caller is about to record
#      against what was issued. A minted number can still be SPOKEN -- no code
#      here can stop that -- but it cannot be made TRUE: it does not reach the
#      DB, it does not reach 표2, it does not reach the keyboard, and the
#      refusal names it. A number that is contradicted on screen inside the same
#      message is a number the owner can catch in one look, which is exactly
#      what the "?  /  ?  /  ?" WT column could not do for them this morning.
#
# i18n: English module, English tokens. The ONLY Korean is the owner-facing
# sentences, which are authored here on purpose -- a consumer that composes its
# own is a second author, and two authors eventually say two things.
#
# stdlib only. No I/O, no clock, no DB: a pure record + two pure functions over
# it, so every caller on the arming critical path can afford it.

# ---------------------------------------------------------------------------
# THE FOUR AXES. Named once, in the owner's own enumeration order
# (무게 / 편측 / 반복수 / RIR), because a fifth axis added without a source is
# the next incident and the roster is where that gets noticed.
# ---------------------------------------------------------------------------
F_WEIGHT = "weight"
F_EXEC = "exec"          # execution mode (양측 / 편측) -- set-table.resolve_unilateral
F_REPS = "reps"
F_RIR = "rir"

FIELDS = (F_WEIGHT, F_EXEC, F_REPS, F_RIR)

# The owner-facing name of each axis, for the refusal sentence. Never the raw
# key: an English field name inside a Korean sentence is a code regression
# (SKILL D4), so the mapping lives beside the sentences that use it.
FIELD_KO = {
    F_WEIGHT: "무게",
    F_EXEC: "수행 방식",
    F_REPS: "반복수",
    F_RIR: "RIR",
}

# ---------------------------------------------------------------------------
# SOURCES -- the closed vocabulary of "which code path produced this value".
#
# A value with no source cannot be constructed (see issue()), and that is the
# whole point: `{"weight_kg": 25.0}` with no author is the artifact shape P2 was
# written about, and it recurred today one axis over.
# ---------------------------------------------------------------------------
S_RX = "rx"                    # rx-calc's prescription for today
S_SLOT = "slot"                # program.yaml's own declared value
S_LAST_LOGGED = "last_logged"  # DERIVED from history (dated, auditable)
S_OVERRIDE = "override"        # the F19/F21 mid-session artifact
S_OWNER = "owner"              # the owner named it themselves
S_LADDER = "ladder"            # set-table.ramp_decision (a rung's own numbers)
S_DEFAULT = "default"          # a DECLARED default, not a guess (exec: bilateral)
S_NONE = "none"                # nothing resolves it -> value is UNKNOWN

SOURCES = (S_RX, S_SLOT, S_LAST_LOGGED, S_OVERRIDE, S_OWNER, S_LADDER,
           S_DEFAULT, S_NONE)

# The one source that is NOT a source: a value the model composed. It exists as
# a token so a violation can be NAMED rather than merely detected.
S_MODEL = "model"


class _Unknown(object):
    """The unresolved value. NOT None.

    None already means three different things across this codebase -- "no rir
    was reported", "this is a genuine bodyweight set", "the resolver failed" --
    and collapsing "we do not know today's load" into that pile is how a blank
    WT cell stopped being an alarm. UNKNOWN is loud, prints as a word, and is
    never equal to a number."""

    __slots__ = ()

    def __repr__(self):
        return "UNKNOWN"

    def __bool__(self):
        return False

    __nonzero__ = __bool__


UNKNOWN = _Unknown()


class RxSourceError(ValueError):
    """A value was offered without a source, or with a source outside SOURCES.

    Raised, not degraded: the degrade path for a sourceless number is exactly
    the defect. A caller that cannot name where a number came from does not get
    to publish it."""


def _norm(value, source):
    """One (value, source) pair, validated. UNKNOWN forces source S_NONE and
    S_NONE forces UNKNOWN -- the two are the same statement and are never
    allowed to disagree, so no consumer has to check both."""
    if source not in SOURCES:
        raise RxSourceError("unknown source %r (must be one of %s)"
                            % (source, ", ".join(SOURCES)))
    if value is UNKNOWN or value is None or source == S_NONE:
        return (UNKNOWN, S_NONE)
    # An EMPTY range is a resolver that answered with nothing, not a resolver
    # that answered. rx-calc emits `target_rir: []` on that path, and keeping
    # the source would render `rir=unknown:rx` -- a token that claims rx-calc
    # produced an unknown, which is precisely the value/source disagreement this
    # function exists to make impossible. (`0` and `0.0` are NOT empty: a RIR of
    # 0 is a real, and hard, prescription.)
    if isinstance(value, (list, tuple, str)) and len(value) == 0:
        return (UNKNOWN, S_NONE)
    return (value, source)


def issue(weight=(UNKNOWN, S_NONE), exec_mode=(UNKNOWN, S_NONE),
          reps=(UNKNOWN, S_NONE), rir=(UNKNOWN, S_NONE)):
    """Build the prescription of record for ONE set.

    Every argument is a (value, source) PAIR and there is no single-value form.
    That is not ceremony: the call site physically cannot pass a number without
    also naming the code path it came from, which is the one property the P2
    override artifact lacked and the one this file exists to make unskippable.

    Returns {field: (value, source)} for all four axes, always -- an axis that
    resolves to nothing is present as (UNKNOWN, S_NONE), never absent. Callers
    read it with value_of() / source_of() and never by .get() with a default,
    because a default IS a mint."""
    return {
        F_WEIGHT: _norm(*weight),
        F_EXEC: _norm(*exec_mode),
        F_REPS: _norm(*reps),
        F_RIR: _norm(*rir),
    }


def value_of(rec, field):
    return (rec or {}).get(field, (UNKNOWN, S_NONE))[0]


def source_of(rec, field):
    return (rec or {}).get(field, (UNKNOWN, S_NONE))[1]


def resolved(rec, field):
    """Did code produce a value for this axis? UNKNOWN -> False."""
    return value_of(rec, field) is not UNKNOWN


def unresolved_fields(rec):
    """The axes no code path could answer, in FIELDS order."""
    return [f for f in FIELDS if not resolved(rec, f)]


# ---------------------------------------------------------------------------
# THE WIRE FORMAT -- the D4 split this codebase already runs on: a machine line
# carrying raw tokens (A-class, never relayed) and a colon line carrying a
# finished Korean sentence (B-class, relayed verbatim).
# ---------------------------------------------------------------------------
# Korean particle selection. The sentences below are read by the owner, so
# "무게을(를)" is a defect like any other -- the bracketed both-forms hedge is the
# tell that a machine wrote the line. Same rule and same Hangul-block walk as
# set-arm._ko_topic, kept here rather than imported because this module is on
# the arming critical path and must stay import-free.
#
# Trailing Latin letters are read aloud in Korean, so the particle follows the
# SPOKEN syllable: RIR -> "알" (final ㄹ) -> 을/이. The map covers only the
# letters that actually end a field name in FIELD_KO; anything unmapped falls to
# the no-final form, which is the safer read for a bare number.
_LATIN_HAS_FINAL = {"l": True, "m": True, "n": True, "r": True,
                    "g": True, "k": False}


def _has_final(word):
    """Does `word` end in a consonant (받침)? Unknown -> False."""
    for ch in reversed(str(word or "")):
        code = ord(ch)
        if 0xAC00 <= code <= 0xD7A3:              # Hangul syllable block
            return bool((code - 0xAC00) % 28)
        if ch.isdigit():
            # A digit is read as its Korean numeral: 0 영, 1 일, 3 삼, 6 육,
            # 7 칠, 8 팔 carry a final; 2 이, 4 사, 5 오, 9 구 do not.
            return ch in "01368"
        if ch.isalpha():
            return _LATIN_HAS_FINAL.get(ch.lower(), False)
    return False


def _josa(word, with_final, without_final):
    """`word` + the correct particle: 을/를, 이/가, 은/는, 으로/로."""
    return "%s%s" % (word, with_final if _has_final(word) else without_final)


def _fmt_value(v):
    """A value as a wire token. UNKNOWN prints as a WORD, never as an empty
    field: `weight=` with nothing after it is indistinguishable from a parse
    failure, and the whole point of this line is that absence is legible.

    NEVER contains whitespace. The machine line is space-separated
    `key=value:source` tokens, so a value that renders with a space splits one
    token into two and every parser downstream reads garbage. rx-calc's
    `target_rir` is a RANGE ([0, 1]) and rendered it as `rir=[0,` + ` 1]:rx`
    -- measured while wiring this in. A range collapses to `lo-hi` (the same
    shape set-table._fmt_rir and set-arm._fmt_rir already print), a single-value
    range to the bare value, and anything else has its whitespace squeezed."""
    if v is UNKNOWN:
        return "unknown"
    if isinstance(v, (list, tuple)):
        if not v:
            return "unknown"
        if len(v) >= 2 and v[0] != v[1]:
            return "%s-%s" % (_fmt_value(v[0]), _fmt_value(v[1]))
        return _fmt_value(v[0])
    if isinstance(v, float) and v.is_integer():
        return "%d" % int(v)
    return "_".join(str(v).split())


def emit_line(rec, exercise_name, set_seq):
    """The machine line. One token per axis, `<value>:<source>`, always all four.

        RX_ISSUED exercise=<name> seq=<n> weight=115:override exec=bilateral:default reps=20:rx rir=1:rx

    A reader can tell at a glance which numbers were READ and which were
    DERIVED, and `unknown:none` is a visible state rather than a missing key."""
    parts = ["RX_ISSUED exercise=%s seq=%s" % (exercise_name, set_seq)]
    for f in FIELDS:
        v, s = (rec or {}).get(f, (UNKNOWN, S_NONE))
        parts.append("%s=%s:%s" % (f, _fmt_value(v), s))
    return " ".join(parts)


def ask_say(rec, display):
    """The ONE owner-facing sentence for the axes nothing resolved, or None when
    all four are answered.

    This is move (2) of the design: an unresolved axis must arrive as something
    to SAY. "무게를 모르겠습니다" competes with inventing 115; a blank does not
    compete with anything."""
    missing = [f for f in unresolved_fields(rec) if f != F_RIR]
    if not missing:
        return None
    names = " / ".join(FIELD_KO[f] for f in missing)
    if F_WEIGHT in missing:
        return ("%s 첫 무게를 맞춰볼게요. 가장 가벼운 설정으로 5회 해보고, "
                "자세가 편하고 2회 정도 더 할 수 있으면 조금씩 올리세요. "
                "편하게 마친 무게를 알려주시면 그 무게로 첫 작업 세트를 시작해요."
                % (display or "이 종목"))
    return "%s %s 알려주세요." % (display or "이 종목", names)


def emit_lines(rec, exercise_name, display, set_seq):
    """Both lines, in D4 order (machine first, Korean second). The Korean line
    is omitted when there is nothing to ask -- an ordinary, fully-resolved set
    says nothing extra, exactly like load_decision_say()'s None branch."""
    out = [emit_line(rec, exercise_name, set_seq)]
    say = ask_say(rec, display)
    if say is not None:
        out.append("RX_ASK: %s" % say)
    return out


# ---------------------------------------------------------------------------
# THE VERIFY GATE -- move (3).
# ---------------------------------------------------------------------------
# A claim is what a caller is about to WRITE or PUBLISH. It is checked against
# what was ISSUED, per axis, with three outcomes:
#
#   agree     the claim IS the issued value                     -> pass
#   authored  the issued value came from the owner themselves    -> pass
#   minted    the claim differs from a code-issued value, or the
#             axis was never resolved at all                     -> VIOLATION
#
# The second is why `by` exists. The owner naming a weight is not a mint: it is
# them training, and gate_weight_override has ruled since P2 that their word is
# never clamped. This gate inherits that ruling rather than re-deciding it.
# ---------------------------------------------------------------------------
V_MINTED = "minted_value"        # a number no code path produced
V_DIVERGED = "diverged_value"    # code produced one; the claim is a different one

# kg / rep comparison tolerance. Mirrors set-arm.LOAD_EPS: lattices step at
# 1.25kg, so anything under this is float noise and never a decision.
EPS = 0.001


def _same(a, b):
    """Value equality that does not trip on 115 vs 115.0 vs '115'."""
    if a is UNKNOWN or b is UNKNOWN:
        return False
    try:
        return abs(float(a) - float(b)) <= EPS
    except (TypeError, ValueError):
        return str(a).strip() == str(b).strip()


def verify(rec, claims, by=None):
    """Check a set of claimed prescription values against the record.

    `claims` is {field: value}; a field absent from it is not checked (a caller
    that says nothing about the RIR is not claiming one). A claim whose value is
    None is likewise not a claim -- None is set-add's legal "no value supplied".

    Returns a list of violation dicts, most-severe first is not a thing here --
    they are returned in FIELDS order so the sentence reads in the owner's own
    enumeration order:

        {"field", "claimed", "issued", "source", "code"}

    `by` == S_OWNER short-circuits to []: the owner's own instruction is never a
    mint. Every other caller is the agent, and the agent deciding IS its job -- but a
    decision it cannot source is the thing that put the owner under a 115kg
    warm-up, so it does not pass here."""
    if by == S_OWNER:
        return []
    out = []
    for f in FIELDS:
        if f not in (claims or {}):
            continue
        claimed = claims[f]
        if claimed is None or claimed is UNKNOWN:
            continue
        v, s = (rec or {}).get(f, (UNKNOWN, S_NONE))
        if v is UNKNOWN:
            out.append({"field": f, "claimed": claimed, "issued": UNKNOWN,
                        "source": S_MODEL, "code": V_MINTED})
        elif not _same(v, claimed):
            out.append({"field": f, "claimed": claimed, "issued": v,
                        "source": s, "code": V_DIVERGED})
    return out


def violation_say(violations, display):
    """The ONE owner-facing sentence for a refused claim, or None when clean.

    STATE what was refused -> name the code value and where it came from -> say
    the one input that resolves it. Deliberately NO branch that offers a choice
    between the two numbers: that shape is the banned utterance P2 removed
    ("25kg 유지냐 26.25kg 복귀냐 고르시면 돼요"), and the way to keep a shape out
    of the product is to own no code that can produce it."""
    if not violations:
        return None
    v = violations[0]
    name = FIELD_KO.get(v["field"], v["field"])
    claimed = _fmt_value(v["claimed"])
    if v["code"] == V_MINTED:
        return ("⚠️ %s -- %s 코드가 낸 적이 없습니다. 프로그램에도 기록에도 "
                "값이 없어서 %s 기록하지 않았습니다. 오늘 얼마로 가실지 "
                "말씀해 주시면 그 값으로 기록합니다."
                % (display or "이 종목", _josa(name, "을", "를"),
                   _josa(claimed, "으로", "로")))
    return ("⚠️ %s -- 코드가 낸 %s %s인데 %s 들어왔습니다. "
            "기록하지 않았습니다. %s 맞으면 그렇게 말씀해 주세요."
            % (display or "이 종목", _josa(name, "은", "는"),
               _fmt_value(v["issued"]), _josa(claimed, "으로", "로"),
               _josa(claimed, "이", "가")))


def violation_line(violations, exercise_name, set_seq):
    """The machine half of the D4 split for a refusal.

        RX_VIOLATION exercise=<name> seq=<n> field=weight claimed=115 issued=unknown source=model code=minted_value
    """
    if not violations:
        return None
    v = violations[0]
    return ("RX_VIOLATION exercise=%s seq=%s field=%s claimed=%s issued=%s "
            "source=%s code=%s"
            % (exercise_name, set_seq, v["field"], _fmt_value(v["claimed"]),
               _fmt_value(v["issued"]), v["source"], v["code"]))
