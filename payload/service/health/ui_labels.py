"""ui_labels -- THE single resolver for owner-facing display names.

WHY THIS FILE EXISTS AND WHY IT IS THE ONLY ONE
===============================================
The workspace keeps relapsing into the same pathology: a name that the owner
reads gets written down in two places, the two drift, and the second one is
found weeks later by the owner rather than by us. So there is exactly ONE
resolver home for owner-facing labels, and this is it. Anything that turns an
internal identifier into words the owner reads belongs here -- not in a private
dict next to its caller.

That home was chosen by a design ticket, not by this file:
    design notes 2026-08-24 (rir label knob and level gating)
which specifies `service/health/ui_labels.py` carrying label() / gloss() /
fmt_rir() / level() / gate(), backed by a DB-resident `ui_label` / `ui_gate`
pair so the display name becomes a KNOB the owner can turn with one UPDATE
instead of a code edit ("서브에이전트 동생 displayname 처럼 취급해줘").

The RIR half of that ticket landed HERE on 2026-08-24 (see "RIR -- THE TERM
STAYS" below): label() / gloss() / fmt_rir(), plus the optional `ui_label` DB
read. The LEVEL half landed here with kit_life 2.23.0: level() / gate() read
the seeded ui_gate contract. Missing rows fail open; an absent level preserves
the intermediate screen. This is also the home of any future folding of
DRILL_DISPLAY under the same `ui_label` table with label_key='drill.<code>'.
Do NOT create a second module for any of it. The whole value of this file is
that there is one of it.

The two halves present here answer two different questions about the same
drill and are kept apart on purpose:
    resolve_drill_display()  WHAT IS IT CALLED  -- a name the owner reads
    equipment_phrase()       WHAT DOES HE HOLD  -- implement + load, if known
The first substitutes one recorded string for another. The second renders
values that may legitimately not exist, and its whole job is to stay silent
when they don't (H2, below). Do not merge them: a name is always present, and
equipment usually is not.

H4 -- WHAT THE DRILL HALF FIXES
===============================
Ruling, 2026-08-24: a rendered drill name was not readable as human speech.

prep.yaml's `display` field is doing two incompatible jobs at once: it is the
designer's CLASSIFICATION name (what movement family, what slot position) and
it is simultaneously the string echoed verbatim to the owner. Classification
vocabulary therefore leaks: "패턴" is a family, "프리프레스" is a placement,
"프라이밍" is a purpose. None of the three tells the owner what to DO, which is
why every one of them needs a sentence of explanation trailing behind it. A
name that works needs no gloss.

The identifier is untouched. `code` (U1c, U3, U4) stays the stable key on both
sides -- prep.yaml, stretch-matrix.md, the glossary, every cross-reference.
Only the rendered label moves.

WHY THE OVERRIDE LIVES IN CODE RATHER THAN IN prep.yaml
-------------------------------------------------------
It shouldn't, long-term -- prep.yaml is the declared home of drill text and
that file's own header says so ("DISPLAY TEXT IS A CONTRACT ... Edit the string
here and nowhere else"). This module is a deliberate, TEMPORARY seam: the
landing that carries these names is not allowed to edit prep.yaml (concurrent
lanes own that file today), and the owner trains tomorrow. So the override sits
in the read path, guarded (see below), until it can be folded into the data.

FOLD-IN PATH (do this when prep.yaml is writable again): copy each `after`
string into the matching prep.yaml `display`, delete its row here. The guard
below makes that a no-op transition rather than a flag day -- once prep.yaml
carries the new string, the `before` match stops firing on its own.

THE GUARD
---------
Each override declares the EXACT string it replaces. If prep.yaml's text is
anything else -- the owner edited it, another lane rewrote it, the fold-in
above already happened -- the override does not fire and the data wins. An
override can therefore never silently overwrite a newer decision, and it can
never quietly outlive its own reason to exist.
"""

import os
import sys
from collections.abc import Mapping
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# code -> (before, after)
#
# `before` is the EXACT current prep.yaml display string (measured, not
# guessed). `after` is what the owner reads.
#
# SOURCING RULE: a display name is NOT invented when a human-readable one is
# already written down. Every `after` below is traced to recorded text, and
# the ones that are still a coinage are marked COINED so the owner can correct
# them -- they name their own drills; this module only stops the classification
# vocabulary from being the thing they read.
DRILL_DISPLAY = {
    # U1c -- the drill the owner actually complained about.
    # NOT coined. stretch-matrix.md:185-186 describes it as "맨몸 또는 경량밴드로
    # 양팔을 벌렸다 모으는 플라이 패턴 8-10회", and the pack's own H4 triage
    # (files/inbox/배치세션-2026-08-24.md:117) already proposed this exact
    # string as the display. The name now says the movement, which is the
    # property every drill name the owner DID understand shares (고관절
    # 스트레칭 / 덤벨 풀오버 / 어깨 밴드 외회전 웜업).
    # CORRECTED 2026-08-24 by the owner: this was a different point, and a
    # real exercise name must not be swapped for a made-up description.
    # H4 is about INVENTED words leaking, not about domain vocabulary being
    # hard. "플라이" is real exercise vocabulary and STAYS; "프리프레스" is the
    # coinage. Paraphrasing the movement away ("양팔 벌렸다 모으기") discarded a
    # term the owner already knows -- the same mistake as renaming a leg
    # extension into a description of the motion.
    # FOLDED IN 2026-09-02. This module's own header names the fold-in path:
    # "copy each `after` string into the matching prep.yaml `display`, delete
    # its row here", to be done "when prep.yaml is writable again". It is, and
    # the structure wave gave prep.yaml a `display` field distinct from `name`
    # -- which is the seam this override was standing in for.
    # prep.yaml now declares `U1c.display: "가벼운 플라이"`; the rep count moved
    # to `target_reps`, where a number belongs. The row is deleted rather than
    # left as a no-op, because the guard would keep it inert while its `before`
    # string quietly rotted into an un-diagnosable mismatch.
    # 「프라이머」 / 「프리프레스」 are gone from every owner-facing `display` in
    # prep.yaml, and `name` keeps the internal designer vocabulary. That is the
    # D12 fix: the model can obey the vocabulary rule because the data it reads
    # no longer contains the banned word. An instruction not to say 프라이머
    # while handing the model a string containing 프라이머 is not a rule, it is
    # a trap.

    # U3 -- "프라이밍" is a purpose word, and the qualifier already spelled the
    # movement out in parentheses ("랫풀다운 경량 10-12회"), which is the tell
    # that the name was not carrying it. Promote the movement to the name and
    # keep only the number, which is prescription and stays.
    # NOT coined: stretch-matrix.md:162 -- "경량(워킹세트 대비 40-50% 추정)
    # 랫풀다운, 10-12회 1세트".
    "U3": ("랫 프라이밍 (랫풀다운 경량 10-12회)", "가벼운 랫풀다운 (10-12회)"),

    # U4 -- COINED. ** THE OWNER SHOULD CHECK THIS ONE. **
    # "오버헤드 슈러그" is not gibberish the way U1c was, but it is the same
    # shape: a family word ("오버헤드") plus a jargon word ("슈러그"). Derived
    # from the recorded description, stretch-matrix.md:194-195 -- "가벼운 봉
    # (PVC/빈바) 또는 밴드를 머리 위로 완전히 뻗은 채 어깨를 으쓱(슈러그)
    # 10-12회". No pre-existing plain name was recorded anywhere, so this
    # phrasing is mine and is the one line in this table the owner has not
    # already effectively written themselves.
    # REVERTED 2026-08-24 by the owner. "슈러그" and "오버헤드" are both real
    # exercise vocabulary, not coinages -- this row never belonged in H4, and
    # "머리 위로 뻗고 어깨 으쓱" is exactly the over-translation they rejected.
    # Identity mapping: the name stays as written.
    "U4": ("오버헤드 슈러그", "오버헤드 슈러그"),

    # STILL DELIBERATELY ABSENT -- U1a "어깨 트리오", and now absent for a
    # second reason: as of 2026-08-24 there is no U1a to map.
    # It was the worst offender of the bundle-name class, and renaming it
    # here would have been the
    # WRONG fix -- any single string standing in for all three, however plain,
    # re-creates the bundle they rejected, while making H1 look done. H1 ruled
    # the bundle NAME must cease to exist rather than read better, and it has:
    # prep.yaml now declares 와이레이즈 / 시티드 어라운드 더 월드 / 헤일로 as
    # three peer drills (U1d / U1e / U1f) with no parent node.
    # Nothing belongs here for them. Their names ARE the movements, which is
    # the property every drill name the owner understood already had, so there
    # is no classification vocabulary left to override. Adding a row for any of
    # the three -- or, worse, re-adding one keyed to a bundle -- would be a
    # regression, not a fix.
}


def resolve_drill_display(code, display):
    """Owner-facing name for one prep/cooldown drill.

    `code` is the stable identifier (U1c, K4, HP1 ...); `display` is the raw
    string prep.yaml declared. Returns the string the owner should read.

    Pass-through in every case except an exact, still-current override match:
    an unknown code, a missing code, a non-string display, or a display that
    has since been edited away from the recorded `before` all return `display`
    untouched. There is no partial or fuzzy matching, on purpose -- a rename
    that fires on a string nobody verified is how the owner ends up reading
    something no human approved.
    """
    if not isinstance(display, str):
        return display
    entry = DRILL_DISPLAY.get(code)
    if not entry:
        return display
    before, after = entry
    return after if display == before else display


# ===========================================================================
# H2 -- THE EQUIPMENT PHRASE. ABSENCE IS THE DEFAULT, AND ABSENCE IS SILENT.
# ===========================================================================
# Ruling, 2026-08-24: an implement and a load were both invented for a
# mobility drill that had neither on record.
#
# The agent had told them a 헤일로 set used a "원판(6kg)", and justified the
# number with "이전에 쓰시던 6kg 기준으로 갈게요" -- a provenance claim for a
# value no record anywhere contained. A full-text sweep found ZERO hits for the
# drill in current data. So the model invented the drill's implement, invented
# its load, and then invented a source for the load.
#
# The root was not the model being careless. There was NO FIELD to put a
# drill's implement or load in, anywhere, so the only place the information
# could exist was inside a generated sentence -- and a generated sentence will
# always be complete, because fluent prose has no way to render a blank. The
# fix is therefore a DATA HOME (prep.yaml `implement` / `load_kg`) plus this
# function, which is the one place those two values become words the owner
# reads.
#
# THE CONTRACT, and why it is written as code rather than as guidance:
#   implement absent  -> "" . The line says NOTHING about equipment.
#   implement present, load absent -> "(케틀벨)". Named, unweighted. This is
#       today's 헤일로: the owner has stated the implement and never the
#       weight, so the weight does not appear. It is not 0, not "가벼운", not
#       the last similar drill's number.
#   implement present, load present -> "(케틀벨 6kg)".
# There is deliberately no `default=` parameter and no fallback branch. A
# default is exactly the shape of the defect: a plausible value standing where
# a missing one should be visible. If this function ever grows an "if not
# implement: return <something>", H2 has regressed.
#
# NOT A PARAPHRASE. 케틀벨 / 덤벨 / 원판 / 밴드 are real equipment vocabulary
# the owner uses themselves, so they are rendered verbatim -- same standard they set
# tonight for exercise terms ("레그 익스텐션은 앉아서 다리 쭉뻡기로할래?").
# This function never translates an implement, only places it.

# ---------------------------------------------------------
# PREP ZONE -- the owner-facing name of WHERE a drill is performed
# ---------------------------------------------------------
# prep.yaml has carried `zone: mat | equipment` on every catalogued drill since
# 2026-09-02 (the axis is WHERE the drill is performed, not whether equipment is
# involved), and its header already declares the session-block display names
# 「0 매트 프렙」 / 「E 장비 프렙」 / 「C 쿨다운」 for the morning card.
#
# The LIVE session surface had no name for the axis at all, so three drills in a
# row read 준비운동 1 / 2 / 3 with no hint that drill 3 is at a machine on the
# other side of the gym. Owner, 2026-09-11: 「랫풀다운은 매트프렙이아닌데 구분이
# 전혀안돼있네」.
#
# These are the SAME two words the card already uses, resolved in the one place
# owner-facing labels live, so the card and the live plan cannot start calling
# the same zone two things. No new vocabulary is coined here.
ZONE_DISPLAY = {
    "mat": "매트",
    "equipment": "장비",
}


def zone_display(zone):
    """Owner-facing name for a prep zone, or None when undeclared.

    None is a real answer and is NOT defaulted to 매트: an undeclared zone means
    the drill was never catalogued, and defaulting is what let two uncatalogued
    drills sit in the wrong block for a week (prep.yaml D5). A caller with None
    says nothing about place, which is honest."""
    if not zone:
        return None
    return ZONE_DISPLAY.get(str(zone).strip())


def _fmt_load_kg(load_kg):
    """Owner-facing weight text for a recorded load, or None when there is no
    usable number. `None` in -> `None` out is the whole point: the caller must
    not be able to turn "no load recorded" into a printed value.

    Trailing ".0" is dropped (6.0 -> "6kg") because the owner reads kilos, not
    floats; a genuine half-plate (2.5) keeps its decimal."""
    if load_kg is None or isinstance(load_kg, bool):
        return None
    try:
        val = float(load_kg)
    except (TypeError, ValueError):
        return None
    if val != val or val in (float('inf'), float('-inf')) or val <= 0:
        return None
    txt = ('%g' % val)
    return txt + 'kg'


def equipment_phrase(implement, load_kg=None):
    """The parenthetical an owner-facing drill line carries, or '' when the
    data does not say.

    Returns '' for: implement None, implement not a string, implement blank
    after stripping. Those are all the same case -- nobody wrote down what they
    picks up -- and they all render as silence.

    A load with no implement is ALSO '': a bare weight with no object attached
    ("(6kg)") is not something the owner can act on, and printing it would be
    half-inventing the equipment by implication."""
    if not isinstance(implement, str):
        return ''
    name = implement.strip()
    if not name:
        return ''
    load = _fmt_load_kg(load_kg)
    return '(%s %s)' % (name, load) if load else '(%s)' % name


def with_equipment(display, implement, load_kg=None):
    """`display` with its equipment parenthetical appended, or `display`
    unchanged when there is no equipment to name.

    Unchanged is the common case and must stay cheap and total: a non-string
    display, an absent implement, or an unusable load all return the input
    object itself, so a drill whose equipment nobody recorded is byte-identical
    to what it rendered before this function existed."""
    if not isinstance(display, str):
        return display
    phrase = equipment_phrase(implement, load_kg)
    if not phrase:
        return display
    return '%s %s' % (display.rstrip(), phrase)


# ===========================================================================
# RIR -- THE TERM STAYS. ONLY ITS DISPLAY NAME IS A KNOB.
# ===========================================================================
# Owner, twice on 2026-08-24:
#   morning -- "Rir 원래대로. 이건 서브에이전트 동생 displayname 처럼 취급해줘"
#   night   -- "Rir 제발 살려줘... 디스플레이네임으로 투트랙으로가자니까 전문용어는.."
#
# WHAT WENT WRONG. They said the acronym was hard. That was read as "replace the
# word", and a Korean substitution was rolled out across the whole set surface
# (instance commit b9d0080). It was the wrong reading twice over: they already knew the
# concept and used it correctly in the very next sentence, and "this is hard"
# asks for an EXPLANATION, not a rename. Substitution deletes information;
# explanation adds it. Substitution also has to be hunted back out of the code
# one literal at a time, which is what this module now ends.
#
# THE TWO TRACKS, which is exactly the frame they handed over:
#   TERM      the domain word, RIR. Stable, never translated, never
#             paraphrased. It is the field name, the DB column, the --rir flag,
#             the arm-file JSON key, the step_validate regex -- and it is also
#             the DEFAULT thing they read.
#   DISPLAY   what that term is CALLED on screen. A knob. Default "RIR".
# A subagent has an internal id and a displayname; changing the displayname
# never touches the id. Same shape here, and the same consequence: if they ever
# says "call it 여유", that is ONE row of data, not ten code edits.
#
# WHERE THE KNOB LIVES, AND WHY IT IS NOT A MIGRATION TODAY
# ---------------------------------------------------------
# The design ticket puts the knob in a DB table (`ui_label`, migration 031).
# That table is not created here: this landing is explicitly barred from
# migrations and from moving user_version, and the owner trains tomorrow
# morning. So the resolution order is:
#
#     1. `ui_label` row for the key, IF that table exists       <- the knob
#     2. DEFAULT_LABELS below                                   <- today
#
# Step 1 is written and live already, it simply finds no table yet. When
# migration 031 lands, the knob starts working with ZERO code change -- and if
# it never lands, every surface still reads "RIR", which is what they asked for.
# Fail-open in both directions, and no surface is left holding a literal.
#
# THE ONE RULE THIS MODULE EXISTS TO ENFORCE: no caller writes the display name
# down. set-arm / set-table / set-add hold no label literal; they call label()
# or fmt_rir(). The single mirror that remains is each script's degrade
# fallback for a sandbox tree with no ui_labels.py in it, and that fallback is
# the TERM itself ("RIR"), pinned equal to DEFAULT_LABELS by test.

# key -> (display, gloss). The gloss slot is the EXPLANATION path; it carried
# the RIR explanation from 2026-08-24 until the removal below on 2026-09-11,
# and is now empty for "rir" by owner ruling, not merely unused.
#
# RIR GLOSS REMOVED, 2026-09-11 (owner ruling): an explanation shown after the
# RIR input is too late and only reaches people who already understood it. Two defects,
# the second fatal: (1) TIMING -- the explanation rendered in the confirm fold
# AFTER the value was already logged, answering a question after the test was
# graded; (2) TARGET INVERSION -- that fold only ever reached someone who had
# already PASSED the RIR keyboard, i.e. someone who already understood it. The
# person stuck at the keyboard not knowing what RIR means never saw it, because
# there was no confirm to fold it under yet. A gate that only opens for people
# who already know the answer is not a gate, it is noise. This is a REMOVAL,
# not a relocation -- do not re-attach an explanation to the RIR keyboard step
# or any other point in the session flow; the owner's instruction was "빼버려"
# (take it out), not "옮겨" (move it). The TERM itself is unaffected: "RIR"
# stays exactly as the section below already required. The caller that built
# the fold from this gloss (set-arm's confirm_fold, DGN-939 sec.5.11/5.12) was
# retired in the same landing -- see set-arm's build_rest_grounds_fold.
#
# The `layer.*` rows are the H7 DOMAIN LAYER VOCABULARY, an unrelated asset
# (owner ruling 2026-08-24, still live). Read the section under this dict
# before adding, removing or renaming one of them -- do not fold this removal
# into that one. One of those rows, 「layer.round」, is itself already retired
# by a SEPARATE ruling (2026-09-02); its absence is documented in place below.
DEFAULT_LABELS = {
    "rir": (
        "RIR",
        "",
    ),

    # ---- H7 domain layers. Display names, not new concepts. --------------
    # Each gloss is the BOUNDARY -- what the layer IS, and what it is NOT.
    # The "is not" half is the load-bearing half: every collision measured in
    # design notes 2026-08-24 (h7 domain vocabulary) is one word sliding into
    # the neighbouring layer, never a layer that had no name at all.
    "layer.session": (
        "세션",
        "세션 = 헬스장에 들어가서 나올 때까지 한 번의 운동. "
        "하루 단위가 아니고(하루 두 번이면 두 세션), 앞A/뒷A 같은 '무슨 날'도 아니다.",
    ),
    "layer.phase": ("구간", "세션의 준비운동, 본운동, 쿨다운 중 한 부분."),
    "layer.prep": ("준비운동", "모빌리티와 활성화로 시작하는 구간."),
    "layer.work": ("본운동", "종목의 세팅, 웜업, 본 세트와 끝의 유산소."),
    "layer.mobility": ("모빌리티", "준비운동에서 움직이며 관절을 푸는 동작."),
    "layer.activation": ("활성화", "준비운동에서 근육에 힘을 넣어 깨우는 동작."),
    "layer.cooldown": ("쿨다운", "본운동 뒤 정적인 스트레칭을 하는 구간."),
    "layer.stretch": ("스트레칭", "쿨다운에서 멈춰서 늘리는 동작."),
    "layer.slot": (
        "종목",
        "종목 = 오늘 플랜에서 차례가 정해진 한 자리. "
        "동작 이름 자체가 아니라 '오늘 몇 번째로 하는 무엇'이고, "
        "대체 종목으로 바꿔도 그 자리는 그대로다.",
    ),
    # OWNER RULINGS 2026-08-25 09:30, applied to the words below:
    #   warmup -> 「웜업」   (워밍업 retired -- 웜업 is what they say)
    #   ramp   -> not a word they are shown at all; a loaded rung reads 웜업 too,
    #             and 램프 stays an internal key (set_seq band / step_type)
    #   prep   -> 「준비운동」 (프렙 and 준비 드릴 both retired). They said "나도
    #             여기에 익숙해질게", so 프렙 does not survive on the grounds
    #             that they use it in chat.
    # This table is the display-name resolver's home, so a retired word left
    # HERE is worse than one left at a call site: it would be the registered
    # answer every future call site fetches.
    "layer.set": (
        "세트",
        "세트 = 쉬지 않고 이어서 한 반복 묶음 하나. "
        "본 세트만 세트로 센다 -- 웜업은 세트 수에 들어가지 않는다.",
    ),
    "layer.rung": (
        "웜업",
        "웜업 = 본 세트 전에 무게를 올려가며 밟는 준비 단계. "
        "빈 봉도 램프도 전부 웜업이고, 오늘 세트 수에는 포함되지 않는다.",
    ),
    # 「layer.round」 IS DELETED -- owner ruling 2026-09-02 06:12, verbatim:
    #     "라운드라는 말을 만든 게 이상해. 세트가 있는데."
    #
    # This row is the sharpest possible case of the thing this module exists to
    # prevent, and it was sitting in the module itself: a REGISTERED display
    # name for a layer that did not need one. Registered here, it was the
    # answer every future call site would fetch -- so the word could not simply
    # fall out of use.
    #
    # Its gloss argued its own case ("세트가 아니다 -- 라운드는 준비운동에만
    # 쓰고") and the case does not hold. The one property the distinction
    # protected is "웜업이 세트 수에 안 들어간다", and that is enforced by
    # set_kind='prep' and the PREP_SEQ_BASE band -- a column, not a word.
    # Measured on a real session: prep rows land at seq -107..-100 and are
    # excluded from every working aggregate. A vocabulary that defends nothing
    # costs the owner a word to learn and buys them nothing.
    #
    # A prep drill performed N times is now `sets: N` and is 「세트」, which
    # layer.set above already defines. Deleting the row rather than remapping
    # it is deliberate: a 폐기어 kept as a synonym is how the pair comes back.
    # rx-calc validate_prep refuses `target_unit: rounds` so the DATA cannot
    # reintroduce it either.
}

# ===========================================================================
# H7 -- DOMAIN LAYER VOCABULARY. THE LAYERS WERE NAMED, JUST NOT ONCE.
# ===========================================================================
# Ruling, 2026-08-24: the 세션 / 종목 layers were being confused on both sides,
# so the layer vocabulary needs a taxonomy and a fixed display name.
#
# This is a measured condition, not an impression. The same morning the phrases
# 세션 중 and 종목 진입 named two different layers in one
# conversation, and neither reading was wrong -- both are written down
# somewhere in this workspace.
#
# WHAT WAS ACTUALLY BROKEN. Not a missing name: every layer here already had
# one, usually two. The defect is that no file declared WHICH name belongs to
# WHICH layer, so each surface picked locally and the picks disagreed. The
# sharpest single instance is in the engine itself --
#     database/ax_engine.py:835
#         return row.get("label") == "bw" or row.get("rung") == "empty_bar"
# -- one row, one concept, two names, joined by `or` because neither could be
# retired without knowing which was canonical. That `or` IS the taxonomy gap.
#
# THE CONTAINMENT ORDER, declared once so nothing has to infer it:
#     프로그램 > 로테이션 데이(앞A/뒷A/앞B/뒷B) > 세션 > 페이즈(프렙/본운동/쿨다운)
#             > 슬롯 > 스텝 > 세트 · 렁
# 「라운드」 was the last term on that line until 2026-09-02 and is RETIRED --
# owner ruling 06:12: inventing the word "round" was wrong when "set" exists. Left in a
# taxonomy comment it would be exactly what the layer.round row below was: the
# answer a future reader fetches. A 폐기어 kept as a footnote is how the word
# comes back.
#
# Internal keys per layer -- UNCHANGED, and deliberately NOT renamed here:
#     session   workouts.id / workout_sets.session_id / SESSION_OPEN
#     slot      program.yaml `slot` / workout_sets.slot_num
#               / prep.yaml card_slot · live_slot / rx-calc focus_slot
#     exercise  exercise_name / ax_exercise -- the MOVEMENT, distinct from the
#               slot that holds it, even though both read as "종목" to the owner
#     step      us_step (step_type = prep|warmup|ramp|working|hold)
#     set       workout_sets row, set_seq >= 1
#     rung      set_seq <= 0, labelled 'bw' (0) / 'rN' (-N)
# NOTE `ax_projection_slot` is NOT this taxonomy's slot: it is keyed on
# step_ref, i.e. one row per STEP. Its name is a 폐기어 the schema is stuck
# with; do not read it as an exercise position.
#
# WHY ONLY FIVE ROWS ARE REGISTERED ABOVE. A display name is registered here
# only when the evidence already settles it -- the owner says the word themselves,
# or a surface already prints it. `layer.exercise`, `layer.step`, `layer.drill`
# are deliberately ABSENT: their owner-facing wording is a
# decision the owner has not made yet (open questions in the worklog ticket).
# Registering a guess here would put the guess on their screen, which is exactly
# what the RIR substitution above was reverted for.
#
# THESE ROWS ARE INERT TODAY, ON PURPOSE. Nothing calls label("layer.set") yet.
# The owner-facing literals for these layers are still hardcoded at their call
# sites -- measured, not assumed:
#     set-arm:594   HOLD_NEXT_LABEL_SET    = "다음 세트"
#     set-arm:612   GENERIC_NEXT_SPEC      = "다음 세트 준비"
#     set-arm:828   CONFIRM_FMT_RUNG       = "✅ 웜업 {1}회 기록"
#     set-arm:829   RUNG_PROMPT_BW_BAR     = "세팅 빈 봉"
#     set-arm:830   RUNG_PROMPT_BW_STACK   = "세팅"
#     set-arm:831   RUNG_PROMPT_RAMP       = "웜업"
#     set-arm:832   RUNG_PROMPT_BODYWEIGHT = "웜업 (맨몸)"
#     set-table:447 SET_COL_LABEL_BW       = "세팅"   (표2 SET 칼럼)
# (Re-measured 2026-08-25 09:30: those four had drifted to 804-807, and the word
# in them is now 웜업 per the 09:30 ruling. Re-measured AGAIN 2026-08-25 12:04:
# the set_seq==0 rung is now 「세팅」 (프라이머 retired), and the single
# RUNG_PROMPT_BW split into a BAR form and a STACK form because stacks got a
# 세팅 rung of their own at 12:07 -- one name, the equipment decides the
# trailing description. Quoting a literal in a comment means the comment has to
# be re-measured with it, or it becomes a second, older copy of the string it is
# describing -- which is the exact failure this ticket is about one layer up.)
# Rewiring those six to label() is a code change with live blast radius and is
# NOT authorised by this ticket, which establishes vocabulary only. Registering
# the keys first is the cheap half: the knob exists, the fold-in target is
# named, and every string above stays byte-identical until a ticket that is
# allowed to move them does so. When that happens each literal becomes
# label("layer.set") / label("layer.rung") and this paragraph is deleted.
#
# THE RULE THIS SECTION EXISTS TO ENFORCE: a layer noun the OWNER reads is
# resolved here. A layer noun only the CODE reads stays an internal key and is
# never translated. If a new word for an existing layer shows up anywhere, it
# is a 폐기어, not a synonym.

# Resolved rows, keyed by db path. The design ticket's rule 2 is "one lookup
# per process, at the render entry point, never inside a loop"; memoising here
# enforces that property no matter where a caller happens to call from, which
# is strictly safer than asking six call sites to remember it.
_LABEL_CACHE = {}


def _lookup(db_path, key):
    """(display, gloss) for `key`, preferring a `ui_label` row when one exists.

    TOTAL, and silent on every failure: no db path, no file, no table, no row,
    a locked db, a db that is not a db -- all of them fall through to
    DEFAULT_LABELS. A label resolver must never be able to break arming or a
    render, and an instance that has not run the migration must behave exactly
    like one that never will."""
    default = DEFAULT_LABELS.get(key)
    if default is None:
        return None
    ck = (db_path, key)
    if ck in _LABEL_CACHE:
        return _LABEL_CACHE[ck]
    out = default
    if db_path:
        try:
            import os
            import sqlite3
            if os.path.exists(db_path):
                conn = sqlite3.connect(db_path)
                try:
                    row = conn.execute(
                        "SELECT display, gloss FROM ui_label "
                        "WHERE label_key = ?", (key,)).fetchone()
                finally:
                    conn.close()
                if row and isinstance(row[0], str) and row[0].strip():
                    out = (row[0].strip(),
                           row[1] if isinstance(row[1], str) and row[1].strip()
                           else default[1])
        except Exception:  # noqa: BLE001 -- absent table/row is the normal case
            out = default
    _LABEL_CACHE[ck] = out
    return out


def label(key="rir", db_path=None):
    """The name the owner reads for `key`. "RIR" unless the knob says otherwise.

    An unknown key returns the key itself rather than raising or returning '':
    a caller that asks for a name always gets a printable one, and a typo shows
    up on screen as the typo instead of as a blank cell."""
    got = _lookup(db_path, key)
    return got[0] if got else str(key)


def gloss(key="rir", db_path=None):
    """One-line explanation of `key` -- the EXPLAIN path, and the single home
    for that sentence. '' for an unknown key (a surface with nothing to say
    says nothing; see equipment_phrase above for the same principle)."""
    got = _lookup(db_path, key)
    return got[1] if got else ''


# Korean particles agree with the SOUND of the word in front of them, so the
# moment the display name becomes a knob, every sentence that carries one has
# a second thing that must move with it. Turning the knob to 여유 and leaving
# "RIR이" behind would produce "여유이 무슨 뜻?" -- the same class of defect as
# the substitution's own "여유 4+개", which is what made this a knob in the
# first place. Selected here rather than at the call sites, for the same reason
# the name itself is: one place.
_LATIN_HAS_FINAL = set("flmnrsxz")     # 에프 엘 엠 엔 아르 에스 엑스 제트
_DIGIT_HAS_FINAL = set("013678")       # 영 일 삼 육 칠 팔


def _has_final(word):
    """Does the Korean READING of `word` end in a final consonant?

    Hangul is decided arithmetically (the jongseong index of the last syllable).
    A Latin letter or digit is decided by how it is READ aloud in Korean, which
    is why 'RIR' takes the final-consonant particle: it ends in R, read 아르.
    Anything else (punctuation, an emoji, an empty string) reports False, which
    picks the vowel-form particle -- the gentler wrong answer of the two, and
    unreachable from any name a person would actually choose."""
    w = (word or '').strip()
    if not w:
        return False
    ch = w[-1]
    if '가' <= ch <= '힣':
        return (ord(ch) - 0xAC00) % 28 != 0
    ch = ch.lower()
    if ch.isdigit():
        return ch in _DIGIT_HAS_FINAL
    if 'a' <= ch <= 'z':
        return ch in _LATIN_HAS_FINAL
    return False


def josa(word, with_final, without_final):
    """`word` plus the particle that agrees with it -- josa('RIR','이','가')
    -> 'RIR이', josa('여유','이','가') -> '여유가'.

    Particle-invariant ones (도, 로 after a vowel-ish name, ...) simply do not
    call this."""
    return '%s%s' % (word, with_final if _has_final(word) else without_final)


# ===========================================================================
# THE FORM OF ADDRESS. READ FROM THE ENVIRONMENT, WRITTEN DOWN NOWHERE.
# ===========================================================================
# A pack is distributed; an instance is one person's. So the word this software
# CALLS that person cannot be a literal in either direction, and the pack has
# been wrong in both directions at once:
#
#   live  '무게 0에서도 통제가 최대일 수 있다 (<호칭> 필라테스 반례)'
#   pack  '무게 0에서도 통제가 최대일 수 있다 (필라테스 반례)'
#   live  '[COORDINATION] %s 축 -- 두 갈래, 하중과 독립 (<호칭> 룰링 2026-08-24)'
#   pack  '[COORDINATION] %s 축 -- 두 갈래, 하중과 독립 (오너 룰링)'
#   live  'kit_life.db에 추가로 쓸 종목이 없음 -- <호칭> 결정 필요'
#   pack  'kit_life.db에 추가로 쓸 종목이 없음 -- 사용자 결정 필요'
#
# These are not comments. They are stdout, read by the person being named. The
# pack's depersonalisation swept them along with the comments, so the pack->live
# direction has no way back: every apply silently downgrades the register, and
# the only repair anyone could make was to hand-edit the literals back -- which
# is how they got wrong the first time.
#
# THE SEAM IS THE ENVIRONMENT, and it already exists: this instance sets
# DOGANY_USER_LABEL. Reading it at RENDER time is what makes both literals go
# away -- the depersonalised one AND the personal one. Nothing here needs the
# installer, a mint token or a substitution pass; a string this module builds
# is correct on whatever instance is running it.
#
# WHY NOT A MINT TOKEN (the other candidate, measured and rejected 2026-09-11 --
# docs/reports/2026-09-11-skillmd-3way-and-user-label.md). Install-side token
# substitution is a literal sed with no Korean particle agreement, compat-lint
# C5 gate(b) ABORTS on any pack file carrying a persona token, and the
# class=pack skills-bundle lane does not run the substitution pipeline at all.
# Three independent blocks. An env read has none of them: the variable name is
# not a persona token (C5 matches the double-underscore token forms), nothing
# is rewritten at install, and `josa` below settles the particle from the value
# that is actually in play.
#
# CLASSIFIER NOUNS ARE NOT ADDRESS, and are deliberately left alone: 「사용자
# 데이터」 / 「사용자 ledger」 / 「사용자 정의」 name a CATEGORY (whose data is
# this) rather than call anybody anything. Substituting them would produce
# 「회원님 데이터」, which is a different and wrong sentence. When in doubt, do
# not substitute.
USER_LABEL_ENV = 'DOGANY_USER_LABEL'
DEFAULT_USER_LABEL = '사용자'


def user_label(with_final=None, without_final=None):
    """How this instance ADDRESSES its owner, from DOGANY_USER_LABEL.

        user_label()             -> '회원님'    (or '사용자' when unset)
        user_label('이', '가')   -> '회원님이'  / '사용자가'
        user_label('은', '는')   -> '회원님은'  / '사용자는'

    The particle pair is optional and goes through `josa`, so the caller never
    has to know whether the configured label ends in a consonant -- which is
    the whole reason a plain substitution cannot do this job: 「회원님」 takes
    이/은/을 and 「사용자」 takes 가/는/를, and a sed that does not know the
    difference emits 「회원님가」.

    Fallback is DEFAULT_USER_LABEL for unset, empty and whitespace-only alike;
    all three mean the same thing -- nobody said. Neutral on purpose: a pack
    that guessed a warmer word would be putting a form of address on a
    stranger's screen, which is the same defect as guessing a display name
    (see WHY ONLY FIVE ROWS ARE REGISTERED above).

    Read on EVERY call, not cached: this costs an os.environ lookup and buys
    the property that a label change takes effect without a restart, the same
    way the DB-backed label() knob does."""
    name = (os.environ.get(USER_LABEL_ENV) or '').strip() or DEFAULT_USER_LABEL
    if with_final is None and without_final is None:
        return name
    return josa(name, with_final or '', without_final or '')


def fmt_rir(rir_str, db_path=None):
    """One already-formatted rir value -> the owner-facing clause.

        '2'   -> 'RIR 2'
        '1-2' -> 'RIR 1-2'
        '4+'  -> 'RIR 4+'
        ''    -> ''          (and None -> '')

    Input is _fmt_rir's output, i.e. a value that has ALREADY been rendered as
    a number, a range, or the open anchor. This function only puts the name in
    front of it, which is why it is the same function for the set-table cell,
    the NEXT_HINT spec and the override path.

    Empty in -> empty out is load-bearing: a spec with no target rir must lose
    the whole clause, not print a bare name (`_spec_line` relies on '' here).

    '4+' KEEPS ITS '+' -- deliberate, and a documented departure from §2-3 of
    the design ticket, which proposed 'RIR 4 이상'. That form existed to escape
    a Korean grammar problem the substitution had created ("여유 4+개" is not
    grammatical); with the term restored the problem is gone, and '+' is the
    standard notation for an open-ended RIR anchor. It also keeps ONE string on
    screen: set-table renders the cell value '4+' verbatim in the RIR column,
    so a spec line reading 'RIR 4 이상' next to a table cell reading '4+' would
    re-create the two-names-one-screen defect this whole landing exists to
    remove. If the owner prefers the spelled-out form, it is this one return
    statement."""
    if not rir_str:
        return ''
    return '%s %s' % (label("rir", db_path), rir_str)


# Level and gate snapshots are process-local, like _LABEL_CACHE. Render entry
# points resolve before loops; separate tools see a changed config next run.
CARD_LEVEL_KEYS = ("workout_level", "user_level", "training_level")
CARD_LEVEL_DEFAULT = "intermediate"
CARD_LEVEL_BEGINNER = ("초급", "beginner", "novice")
_LEVEL_CACHE = {}
_GATE_CACHE = {}


def _normalize_level(value):
    return ("beginner" if str(value).strip().lower() in CARD_LEVEL_BEGINNER
            else CARD_LEVEL_DEFAULT)


def level(db_path=None):
    """Resolve the first nonempty config key; never create or write a DB."""
    if db_path not in _LEVEL_CACHE:
        resolved = CARD_LEVEL_DEFAULT
        try:
            import sqlite3
            if db_path and os.path.exists(db_path):
                conn = sqlite3.connect(db_path)
                try:
                    for key in CARD_LEVEL_KEYS:
                        row = conn.execute(
                            "SELECT value FROM config WHERE key = ?", (key,)).fetchone()
                        if row and row[0]:
                            resolved = _normalize_level(row[0])
                            break
                finally:
                    conn.close()
        except Exception:  # same fail-open discipline as _lookup
            pass
        _LEVEL_CACHE[db_path] = resolved
    return _LEVEL_CACHE[db_path]


def gate(surface, db_path=None, *, level_override=None):
    """The only visibility verdict. Unknown surface/table/DB -> visible.

    level_override preserves the incumbent card renderer's explicit-level API;
    normalization and the verdict still live here and still read ui_gate.
    explain is returned as metadata only; there is no explanation renderer.
    """
    resolved = (level(db_path) if level_override is None
                else _normalize_level(level_override))
    key = (db_path, resolved)
    if key not in _GATE_CACHE:
        rows = {}
        try:
            import sqlite3
            if db_path and os.path.exists(db_path):
                conn = sqlite3.connect(db_path)
                try:
                    rows = {r[0]: {"visible": bool(r[1]), "label_key": r[2],
                                   "explain": r[3]}
                            for r in conn.execute(
                                "SELECT surface, visible, label_key, explain "
                                "FROM ui_gate WHERE level = ?", (resolved,))}
                finally:
                    conn.close()
        except Exception:  # missing table, locked or unreadable DB -> visible
            pass
        _GATE_CACHE[key] = rows
    return dict(_GATE_CACHE[key].get(surface,
                {"visible": True, "label_key": None, "explain": None}))


# ===========================================================================
# PLAN COPY LABELS -- body areas, muscles, sites, weekdays, clock times
# ===========================================================================
# service/health/program-plan renders every sentence of the program-building
# hand-off. The names inside those sentences are owner-facing labels, so they
# resolve here and nowhere else. Muscles and areas read the pack's own seeded
# `muscle_label` rows (lang='ko', form='long') first; the fallback below is the
# same seed text, kept so a DB without the taxonomy still renders a Korean
# word instead of an English key.
_AREA_KO_FALLBACK = {
    'shoulders': '어깨', 'chest': '가슴', 'back': '등', 'arms': '팔',
    'legs': '다리', 'calves': '종아리', 'abs': '복근', 'glutes': '둔근',
    'quads': '대퇴사두', 'hamstrings': '햄스트링', 'biceps': '이두',
    'triceps': '삼두', 'forearms': '전완', 'core': '코어',
}

# Body sites for the safety check. The kit stores a standing safety row as
# `injury_<site>[_l|_r]` (047_pain_event names the family); these are the
# sites the plan knows how to read back and relate to a focus area.
SITE_KO = {
    'knee': '무릎', 'shoulder': '어깨', 'hip': '고관절', 'back': '허리',
    'lower_back': '허리', 'neck': '목', 'elbow': '팔꿈치', 'wrist': '손목',
    'ankle': '발목', 'foot': '발',
}
SIDE_KO = {'l': '왼쪽', 'r': '오른쪽'}

WEEKDAY_ORDER = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')


# ===========================================================================
# LOCALE + PACK COPY (owner 2026-10-02 11:40-11:53)
# ===========================================================================
# Weekday names (and the week calendar's glyphs, card_lib.week_calendar) are
# COPY, not code: they live in this pack's i18n bundle under the pack-owned
# `health.` prefix -- service/health/i18n/<lang>.json, byte-identical to
# payload/config/i18n/<lang>.bundle.json (test-i18n-bundle-layer B3), which
# pack_install.sh writes to config/packs/pack_health.i18n.<lang>.json. The
# kit's pack-copy seam filters by its own prefixes, so it never sees these.
#
# lang(): HEALTH_LANG, else AGENT_LANG (env, then config/agent.conf), else
# 'ko' -- the language every other surface of this pack is written in.
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, '..', '..'))
_I18N = {}


def _agent_conf(key):
    try:
        with open(os.path.join(_ROOT, 'config', 'agent.conf'),
                  encoding='utf-8', errors='replace') as fh:
            for line in fh:
                line = line.strip()
                if line.startswith(key + '='):
                    v = line.split('=', 1)[1].strip()
                    if len(v) >= 2 and v[0] == v[-1] and v[0] in '\'"':
                        v = v[1:-1]
                    return v.strip()
    except OSError:
        pass
    return ''


def lang():
    return (os.environ.get('HEALTH_LANG') or os.environ.get('AGENT_LANG')
            or _agent_conf('AGENT_LANG') or 'ko')


def _bundle(code):
    """{key: copy} for one language: the first bundle file found among the
    service copy, the installed pack layer, the payload bundle."""
    if code not in _I18N:
        data = {}
        for path in (os.path.join(_HERE, 'i18n', '%s.json' % code),
                     os.path.join(_ROOT, 'config', 'packs',
                                  'pack_health.i18n.%s.json' % code),
                     os.path.join(_ROOT, 'config', 'i18n',
                                  '%s.bundle.json' % code)):
            try:
                import json
                with open(path, encoding='utf-8') as fh:
                    got = json.load(fh)
            except (OSError, ValueError):
                continue
            if isinstance(got, dict):
                data = got
                break
        _I18N[code] = data
    return _I18N[code]


def i18n(key, code=None, **kw):
    """The copy for `key` in `code` (default lang()), then en; '' when
    neither bundle has it."""
    for c in (code or lang(), 'en'):
        v = _bundle(c).get(key)
        if isinstance(v, str) and v:
            return v.format(**kw) if kw else v
    return ''


def weekday_short(day, code=None):
    """'MON' -> the one-cell weekday label of the language."""
    return i18n('health.weekday.short.' + day, code)


def weekday_full(day, code=None):
    return i18n('health.weekday.full.' + day, code)


class _WeekdayNames(Mapping):
    """Compatibility accessor: the old WEEKDAY_KO / WEEKDAY_FULL_KO dicts,
    now read from the ko bundle (owner 2026-10-02: no weekday literal in
    code). Behaves as the read-only dict it replaces."""

    def __init__(self, form):
        self._form = form

    def __getitem__(self, day):
        if day not in WEEKDAY_ORDER:
            raise KeyError(day)
        return i18n('health.weekday.%s.%s' % (self._form, day), 'ko')

    def __iter__(self):
        return iter(WEEKDAY_ORDER)

    def __len__(self):
        return len(WEEKDAY_ORDER)


WEEKDAY_KO = _WeekdayNames('short')


# ===========================================================================
# week calendar (owner ruling 2026-10-02 13:27: ONE standard for the main and health agents)
# ===========================================================================
# The kit draws it (`kit_life.sh week-calendar`; today is "[<day>]" in the
# weekday row, rows indented one space, row three = 'done' marks only, rule
# lines via --rule). This file only maps the pack's split codes to the kit's
# cell codes and calls the verb. No glyph, layout or fallback renderer here.
_FULLBODY = u"\uc804\uc2e0"          # the full-body split code (data)


def kit_cell(code):
    """The kit's cell code for a rotation day code: a full-body A/B day is
    its tail letter (full-body A -> 'A'), a bare full-body day keeps its first syllable; every
    other code goes through unchanged (the kit takes its first Hangul syllable
    or first letter)."""
    c = str(code or "").strip()
    if c.startswith(_FULLBODY):
        tail = c[len(_FULLBODY):].strip()
        if tail and tail[0].isascii() and tail[0].isalnum():
            return tail[0].upper()
        return _FULLBODY[0]
    return c.replace(",", " ")


def _kit_sh():
    return (os.environ.get("KIT_LIFE_SH")
            or os.path.join(os.path.abspath(os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "..", "..")),
                "database", "kit_life.sh"))


_default_lang = lang


def week_calendar(days, status=None, lang=None, rule=False):
    """The calendar lines from the kit verb. `days` {MON..SUN: code};
    `status` {MON..SUN: 'done'|'today'}. Kit missing / too old -> [] and one
    stderr line (never a second renderer)."""
    import subprocess
    days, status = days or {}, status or {}
    cells = ",".join(kit_cell(days.get(d)) for d in WEEKDAY_ORDER)
    args = [_kit_sh(), "week-calendar", "--cells", cells]
    if any(status.get(d) for d in WEEKDAY_ORDER):
        args += ["--marks", ",".join(status.get(d) or "" for d in WEEKDAY_ORDER)]
    args += ["--lang", lang or _default_lang()]
    if rule:
        args.append("--rule")
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError) as e:
        r = None
        err = str(e)
    else:
        err = (r.stderr or "").strip()[-200:]
    if r is None or r.returncode != 0 or not r.stdout.strip():
        sys.stderr.write("week-calendar: kit verb unavailable (needs kit_life "
                         ">=2.38.0), calendar omitted: %s\n" % err)
        return []
    return r.stdout.rstrip("\n").split("\n")


def rotation_days(weekdays, rotation, start=0):
    """{MON..SUN: code} -- the rotation laid over the training days in week
    order from rotation[start] (week one of a split)."""
    days = [d for d in WEEKDAY_ORDER if d in set(weekdays or ())]
    rot = list(rotation or ())
    if not rot:
        return {}
    return {d: rot[(start + i) % len(rot)] for i, d in enumerate(days)}


def muscle_ko(node, db_path=None):
    """Korean name of a muscle or body area (closed vocabulary)."""
    if db_path:
        try:
            import sqlite3
            conn = sqlite3.connect('file:%s?mode=ro' % db_path, uri=True)
            try:
                row = conn.execute(
                    "SELECT text FROM muscle_label WHERE node=? AND lang='ko' "
                    "AND form='long'", (node,)).fetchone()
            finally:
                conn.close()
            if row and row[0]:
                return row[0]
        except Exception:  # missing table / unreadable DB -> fallback
            pass
    return _AREA_KO_FALLBACK.get(node, node)


def site_ko(site, side=None):
    """'knee','r' -> '오른쪽 무릎'. An unknown site is returned as given (it is
    the user's own word in that case)."""
    base = SITE_KO.get(site, site)
    return '%s %s' % (SIDE_KO[side], base) if side in SIDE_KO else base


def parse_site_key(key):
    """'injury_<site>_r' -> ('<site>', 'r'); 'injury_knee' -> ('knee',
    None); anything else -> (None, None)."""
    if not isinstance(key, str) or not key.startswith('injury_'):
        return None, None
    rest = key[len('injury_'):]
    side = None
    if rest[-2:] in ('_l', '_r'):
        rest, side = rest[:-2], rest[-1]
    return rest, side


def weekdays_ko(days):
    """['MON','WED','FRI'] -> '월·수·금' (week order, duplicates dropped)."""
    seen = [d for d in WEEKDAY_ORDER if d in set(days or ())]
    return '·'.join(WEEKDAY_KO[d] for d in seen)


def clock_ko(hhmm):
    """'19:00' -> '저녁 7시', '06:30' -> '아침 6시 30분'."""
    try:
        h, m = (int(x) for x in str(hhmm).split(':', 1))
    except (ValueError, TypeError):
        return str(hhmm)
    if h < 5:
        part = '새벽'
    elif h < 11:
        part = '아침'
    elif h < 13:
        part = '낮'
    elif h < 18:
        part = '오후'
    else:
        part = '저녁'
    h12 = h if h <= 12 else h - 12
    h12 = 12 if h12 == 0 else h12
    return '%s %d시%s' % (part, h12, (' %d분' % m) if m else '')


# ===========================================================================
# PROGRAM CARD LABELS (program-plan round 3, owner rehearsal 2026-09-26)
# ===========================================================================
# The names inside the all-sessions message come from the sourced movement
# catalog. A planning key never becomes an invented user-facing movement name.
try:
    from movement_catalog import MOVEMENTS as _MOVEMENTS
except ImportError:
    # A few standalone set-table sandboxes copy only the rendering modules.
    # Their set tables still need labels even without the planning catalog.
    _MOVEMENTS = {}
PLAN_DRILL_KO = {key: item['ko'] for key, item in _MOVEMENTS.items()}


# Plain body words for the "(kind / muscles)" tail of a lift line. The
# taxonomy's muscle_label rows are the anatomy register (대퇴사두, 둔근);
# this line is read by someone who may not have that vocabulary yet.
MUSCLE_PLAIN_KO = {
    'chest': '가슴', 'back': '등', 'shoulders': '어깨', 'quads': '허벅지 앞',
    'glutes': '엉덩이', 'hamstrings': '허벅지 뒤', 'adductors': '허벅지 안쪽',
    'calves': '종아리', 'biceps': '팔 앞쪽', 'triceps': '팔 뒤쪽',
    'forearms': '아래팔', 'abs': '복근',
}

LIFT_KIND_KO = {'main': '대근육', 'assist': '보조', 'small': '소근육',
                'core': '코어'}

WEEKDAY_FULL_KO = _WeekdayNames('full')


def plan_drill_ko(key):
    return PLAN_DRILL_KO.get(key, key)


def exercise_ko(key):
    """Owner-facing lift name when a historical row lacks program display."""
    try:
        import json
        import os
        path = os.path.join(os.path.dirname(__file__), 'fatigue_copy.json')
        with open(path, encoding='utf-8') as stream:
            found = json.load(stream).get('exercise', {}).get(key)
        if found:
            return found
    except (OSError, ValueError, TypeError):
        pass
    from movement_catalog import MOVEMENTS
    if key == 'reverse_pec_deck_fly':
        return '리버스 펙덱'
    return MOVEMENTS.get(key, {}).get('ko', '운동')


def muscle_plain_ko(node):
    return MUSCLE_PLAIN_KO.get(node) or _AREA_KO_FALLBACK.get(node, node)


def days_phrase_ko(days):
    """Extra-day phrase: ['WED','SAT','SUN'] -> '수요일·주말'; one day reads
    in full, a weekend pair folds to '주말'."""
    seen = [d for d in WEEKDAY_ORDER if d in set(days or ())]
    weekend = 'SAT' in seen and 'SUN' in seen
    others = [d for d in seen if not (weekend and d in ('SAT', 'SUN'))]
    names = ([WEEKDAY_FULL_KO[others[0]]] if len(others) == 1
             else [WEEKDAY_KO[d] for d in others])
    if weekend:
        names.append('주말')
    return '·'.join(names)
