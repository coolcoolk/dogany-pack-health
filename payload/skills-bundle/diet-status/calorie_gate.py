#!/usr/bin/env python3
"""
The COUNTABLE half of the G6 safety gate: does this calorie plan clear the
inviolable rows, and if it does not, what does it clear at?

WHY THIS FILE EXISTS.  Until 0.11.0 the gate was a sentence and nothing else.
The two thresholds it needs were alive -- `ledger_constraint` rows
`max_deficit_cap` and `calorie_floor`, both `inviolable=1`, both carried into
the consult frame by the kit's `sot_registry` -- and the kit's own comment says
of them "nothing inspects the value".  The PROCEDURE that was supposed to
inspect them lived in an AGENT.md section this pack never delivered, so a
consult reaching G6 was told to run a section that does not exist, and the
card's daily target was computed with no floor under it at all.  Measured
before the change: `grep -rE 'max_deficit_cap|calorie_floor' payload/` -> 0.

  Prose is the last resort, not the mechanism (owner-agreed with the framework
  owner, 2026-09-12).  Everything on this page is a comparison a machine can
  do; the conversational half of G6 -- asking about injuries, hearing a refusal,
  choosing words -- stays in AGENT-CONSULT.md because it is not a comparison.

NO THRESHOLD IS WRITTEN HERE.  The numbers stay in the kit and arrive by KEY.
This module knows the key names (`max_deficit_cap`, `calorie_floor`) and the
field names inside the floor's JSON policy object; it knows none of the values.
A threshold copied into pack code is a threshold that drifts from the row the
consult frame shows the owner in the same turn -- which is the two-homes defect
that put the gate in this state to begin with, one layer down.

ABSENT IS NOT CLEAR.  The rows are `source='seed'` and NOTHING in the kit plants
them: they are not in `schema.sql` and not in any migration (measured against
kit_life 2.19.0, migrations 028-047).  They exist on the owner's database
because someone inserted them by hand on 2026-07-13 and 2026-07-15.  So a
freshly minted instance has NO safety floor, and the honest verdict for that
state is `unverifiable`, never `pass`.  A gate that reports "clear" when it
could not read its own limits is worse than no gate: it manufactures a
clearance nobody granted.  Seeding those rows is the KIT's to do
(`ledger_constraint` is the kit's table and this pack declares
`capabilities.db_lane=false`); this file's job is to refuse to paper over it.

THE THREE LIMBS, and where each one's text comes from.  Reconstructed from the
framework-side legacy fragment `packs/health-trainer/<instance>/AGENT.md.add`
(DGN-287-CONSULT-FRAGMENT v2.4) and the instance copy in force until retirement
(`identity/hot.custom.agent.md`, 2026-09-11).  The two agree on all three.

  cap        deficit <= max_deficit_cap.  Over cap -> refuse/refract, no
             override.  Refraction here = the deficit is CLAMPED to the cap and
             the clamp is named; a refusal the owner cannot see is a refusal
             that did not happen.

  bmr_floor  base_target >= bmr_base_factor x BMR.  Both terms are computed by
             the kit's own calculator, so this limb is always decidable when a
             plan exists.

  sex_floor  weekly_avg_effective >= the floor for the declared sex, where
             weekly_avg_effective = base_target + (weekly_freq x
             per_session_burn) / 7.  `per_session_burn` is history average or
             kit-computed; NO HISTORY -> 0, which is the conservative branch the
             source names explicitly and is this module's default.  With burn 0
             the limb reduces to base_target >= floor.  Sex undeclared has its
             own floor field -- it is not an error and not a skip.

WHAT IS DELIBERATELY NOT DECIDED HERE.  Whether `weekly_freq`/`per_session_burn`
should be MINED from workout history rather than passed in.  The source says
"history average or kit_life", and this pack cannot query the kit's history
without growing a second reader of a table it does not own; the caller that
already holds those numbers passes them.  Absent them the module runs the
conservative branch and SAYS which branch it ran (`assumed` in the output),
instead of quietly picking one.

Usage:
  calorie_gate.py --deficit N --base-target N --bmr N [--sex male|female]
                  [--weekly-freq N] [--per-session-burn N] [--json]
Exit: 0 pass · 1 refuse · 2 unverifiable (limits unreadable/absent).
The three codes are distinct so a caller can branch without parsing prose.
"""
import argparse
import json
import os
import sqlite3
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
KIT_DB = os.path.join(_PROJECT_ROOT, "database", "kit_life.db")

# The keys, and only the keys. Every value behind them is the kit's.
CAP_KEY = "max_deficit_cap"
FLOOR_KEY = "calorie_floor"
FLOOR_BY_SEX = {"male": "floor_male", "female": "floor_female"}
FLOOR_UNDECLARED = "floor_undeclared"
BMR_FACTOR_FIELD = "bmr_base_factor"


def _ro_conn(path):
    """Read-only connection, or None.

    Same reason kitmode.py opens `mode=ro`: a safety check must never be the
    thing that writes to, creates, or checkpoints the owner's database. Unlike
    kitmode there is no header fallback -- a row read needs a real connection,
    and failing to get one is a reportable state (`unverifiable`), not a state
    to paper over with a stale guess."""
    if not os.path.isfile(path):
        return None
    try:
        return sqlite3.connect("file:%s?mode=ro" % path, uri=True)
    except sqlite3.Error:
        return None


def load_limits(db_path=None):
    """The two inviolable rows, by key, from the kit.

    Returns {'cap': float|None, 'floor': dict|None, 'missing': [key...],
             'error': str|None}. A row that is present but unparseable counts
    as missing and says so -- a malformed floor is not a floor."""
    path = db_path or KIT_DB
    out = {"cap": None, "floor": None, "missing": [], "error": None,
           "db": path}
    conn = _ro_conn(path)
    if conn is None:
        out["error"] = ("kit database not readable read-only: %s" % path)
        out["missing"] = [CAP_KEY, FLOOR_KEY]
        return out
    try:
        rows = dict(conn.execute(
            "SELECT key, value FROM ledger_constraint "
            "WHERE key IN (?,?) AND status='active' AND inviolable=1;",
            (CAP_KEY, FLOOR_KEY)).fetchall())
    except sqlite3.Error as e:
        out["error"] = "ledger_constraint unreadable: %s" % e
        out["missing"] = [CAP_KEY, FLOOR_KEY]
        return out
    finally:
        conn.close()

    raw_cap = rows.get(CAP_KEY)
    if raw_cap is None:
        out["missing"].append(CAP_KEY)
    else:
        try:
            out["cap"] = float(raw_cap)
        except (TypeError, ValueError):
            out["missing"].append(CAP_KEY)
            out["error"] = "%s is not a number: %r" % (CAP_KEY, raw_cap)

    raw_floor = rows.get(FLOOR_KEY)
    if raw_floor is None:
        out["missing"].append(FLOOR_KEY)
    else:
        try:
            parsed = json.loads(raw_floor)
        except (TypeError, ValueError):
            parsed = None
        if isinstance(parsed, dict):
            out["floor"] = parsed
        else:
            out["missing"].append(FLOOR_KEY)
            out["error"] = "%s is not a JSON policy object" % FLOOR_KEY
    return out


def sex_floor(limits, sex):
    """The floor value for a declared sex, or None when the row cannot say.

    Undeclared is a DECLARED case in the policy object, not a missing one."""
    floor = (limits or {}).get("floor")
    if not isinstance(floor, dict):
        return None
    field = FLOOR_BY_SEX.get((sex or "").strip().lower(), FLOOR_UNDECLARED)
    v = floor.get(field)
    if v is None and field != FLOOR_UNDECLARED:
        v = floor.get(FLOOR_UNDECLARED)
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _limb(name, verdict, **kw):
    d = {"limb": name, "verdict": verdict}
    d.update(kw)
    return d


def evaluate(deficit_kcal=None, base_target_kcal=None, bmr_kcal=None,
             sex=None, weekly_freq=None, per_session_burn=None, limits=None,
             db_path=None):
    """Run the three limbs. Never raises on a missing input -- an input this
    module does not have makes its limb `unverifiable`, which is a verdict.

    Overall verdict, in this order and for this reason:
      refuse        any limb refused -- a cleared limb cannot outvote a breach.
      unverifiable  no breach, but at least one limb could not be decided.
      pass          every limb decided and every limb cleared.
    `pass` is the only outcome that requires all three, which is what makes
    "the rows are missing" unable to read as "the plan is safe"."""
    lim = limits if limits is not None else load_limits(db_path)
    limbs = []

    # -- cap ---------------------------------------------------------------
    cap = lim.get("cap")
    if deficit_kcal is None:
        limbs.append(_limb("cap", "unverifiable", need="deficit_kcal"))
    elif cap is None:
        limbs.append(_limb("cap", "unverifiable",
                           need="ledger_constraint %s" % CAP_KEY))
    elif deficit_kcal > cap:
        limbs.append(_limb("cap", "refuse", value=float(deficit_kcal),
                           limit=cap, refract_to=cap,
                           why="deficit exceeds the inviolable cap"))
    else:
        limbs.append(_limb("cap", "pass", value=float(deficit_kcal),
                           limit=cap))

    # -- bmr floor ---------------------------------------------------------
    factor = None
    if isinstance(lim.get("floor"), dict):
        try:
            factor = float(lim["floor"].get(BMR_FACTOR_FIELD))
        except (TypeError, ValueError):
            factor = None
    if base_target_kcal is None or bmr_kcal is None:
        limbs.append(_limb("bmr_floor", "unverifiable",
                           need="base_target_kcal+bmr_kcal"))
    elif factor is None:
        limbs.append(_limb("bmr_floor", "unverifiable",
                           need="ledger_constraint %s.%s"
                                % (FLOOR_KEY, BMR_FACTOR_FIELD)))
    else:
        need = factor * float(bmr_kcal)
        if float(base_target_kcal) < need:
            limbs.append(_limb("bmr_floor", "refuse",
                               value=float(base_target_kcal), limit=need,
                               refract_to=need,
                               why="base target is under the BMR-relative "
                                   "floor"))
        else:
            limbs.append(_limb("bmr_floor", "pass",
                               value=float(base_target_kcal), limit=need))

    # -- sex floor on the weekly average -----------------------------------
    sf = sex_floor(lim, sex)
    assumed = []
    burn = per_session_burn
    if burn is None:
        burn = 0.0
        assumed.append("per_session_burn=0 (no history supplied -- the "
                       "conservative branch)")
    freq = weekly_freq
    if freq is None:
        freq = 0.0
        if burn:
            assumed.append("weekly_freq=0 (not supplied)")
    if base_target_kcal is None:
        limbs.append(_limb("sex_floor", "unverifiable", need="base_target_kcal",
                           assumed=assumed))
    elif sf is None:
        limbs.append(_limb("sex_floor", "unverifiable",
                           need="ledger_constraint %s (sex floor)" % FLOOR_KEY,
                           assumed=assumed))
    else:
        weekly_avg = float(base_target_kcal) + (float(freq) * float(burn)) / 7.0
        if weekly_avg < sf:
            # Refract on the term the caller controls: the base target has to
            # rise by the whole shortfall, because the burn term is measured,
            # not chosen.
            limbs.append(_limb(
                "sex_floor", "refuse", value=weekly_avg, limit=sf,
                refract_to=float(base_target_kcal) + (sf - weekly_avg),
                sex=(sex or "undeclared"), weekly_avg_effective=weekly_avg,
                assumed=assumed,
                why="weekly average effective intake is under the sex floor"))
        else:
            limbs.append(_limb("sex_floor", "pass", value=weekly_avg, limit=sf,
                               sex=(sex or "undeclared"),
                               weekly_avg_effective=weekly_avg,
                               assumed=assumed))

    verdicts = [l["verdict"] for l in limbs]
    if "refuse" in verdicts:
        overall = "refuse"
    elif "unverifiable" in verdicts:
        overall = "unverifiable"
    else:
        overall = "pass"

    refracted = {}
    for l in limbs:
        if l["verdict"] != "refuse":
            continue
        if l["limb"] == "cap":
            refracted["deficit_kcal"] = l["refract_to"]
        else:
            refracted["base_target_kcal"] = max(
                refracted.get("base_target_kcal", 0.0), l["refract_to"])

    return {
        "verdict": overall,
        "limbs": limbs,
        "refract": refracted,
        "limits_missing": lim.get("missing") or [],
        "limits_error": lim.get("error"),
        "db": lim.get("db"),
        # Said on every run, kitmode.py's claim discipline: this module decides
        # the countable limbs and nothing else. The injuries collection, the
        # wording of a refusal, and the medical-supervision referral are
        # AGENT-CONSULT.md G6 and are not represented in this verdict.
        "scope": "countable limbs only -- the injuries collection and the "
                 "refusal wording are AGENT-CONSULT.md G6",
    }


def refract(deficit_kcal, base_target_kcal, bmr_kcal, sex=None,
            weekly_freq=None, per_session_burn=None, limits=None,
            db_path=None):
    """(deficit, base_target, verdict) with every breach brought back into
    range.  The caller gets numbers it may show; it does NOT get to see a
    breach as a pass, because `verdict` rides along and the card prints it."""
    v = evaluate(deficit_kcal, base_target_kcal, bmr_kcal, sex, weekly_freq,
                 per_session_burn, limits, db_path)
    d = v["refract"].get("deficit_kcal", deficit_kcal)
    b = v["refract"].get("base_target_kcal", base_target_kcal)
    return d, b, v


def permitted_base(verdict, base_target_kcal, deficit_kcal=None):
    """The lowest base daily target this verdict permits, as an int.

    ONE number, because a card and a consult proposal both have exactly one
    line to move.  The two floor limbs hoist the base target directly.  The CAP
    limb is a hoist too, and the conversion is arithmetic, not judgement: the
    kit computes `base_goal = BMR - deficit + NEAT`, so clamping the deficit to
    the cap raises the base target by exactly the overshoot.  Returns
    `base_target_kcal` unchanged on pass/unverifiable -- an unread limit must
    not move a number any more than it may clear one.
    """
    if not verdict or base_target_kcal is None:
        return base_target_kcal
    want = float(base_target_kcal)
    ref = verdict.get("refract") or {}
    if "base_target_kcal" in ref:
        want = max(want, float(ref["base_target_kcal"]))
    if "deficit_kcal" in ref and deficit_kcal is not None:
        want = max(want, float(base_target_kcal)
                   + (float(deficit_kcal) - float(ref["deficit_kcal"])))
    return int(round(want))


def why_line(v):
    """ONE line in the owner's language, or "" when there is nothing to say.

    The wording is the source's own pinned exemplar for the floor case ("이
    체구에서 이 밑으로는 권하지 않아요"); the cap case says which number moved
    and why.  A gate that acts without saying so is the defect this release is
    about, so every non-pass verdict has a line."""
    if not v or v.get("verdict") == "pass":
        return ""
    if v["verdict"] == "unverifiable":
        return ("안전 하한/상한 행을 읽지 못해서 이 숫자는 안전 확인이 "
                "안 된 상태입니다. 확정 전에 확인이 필요해요.")
    bits = []
    for l in v["limbs"]:
        if l["verdict"] == "refuse" and l["limb"] == "cap":
            bits.append("감량 폭이 상한을 넘어서 상한선(%d)으로 잡았습니다"
                        % round(l["limit"]))
    # The two floor limbs are ONE sentence, at the higher of the two hoists.
    # Saying "I will not go below X" twice with two different X reads as two
    # different floors, and there is only one floor being enforced.
    hoist = v["refract"].get("base_target_kcal")
    if hoist is not None:
        bits.append("이 체구에서 이 밑으로는 권하지 않아요. %d kcal로 "
                    "잡을게요" % round(hoist))
    return " / ".join(bits)


def main(argv):
    ap = argparse.ArgumentParser(prog="calorie_gate.py", add_help=True)
    ap.add_argument("--deficit", type=float, default=None)
    ap.add_argument("--base-target", type=float, default=None)
    ap.add_argument("--bmr", type=float, default=None)
    ap.add_argument("--sex", default=None)
    ap.add_argument("--weekly-freq", type=float, default=None)
    ap.add_argument("--per-session-burn", type=float, default=None)
    ap.add_argument("--db", default=None)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)

    v = evaluate(a.deficit, a.base_target, a.bmr, a.sex, a.weekly_freq,
                 a.per_session_burn, db_path=a.db)
    if a.json:
        print(json.dumps(v, ensure_ascii=False))
    else:
        print("verdict=%s" % v["verdict"])
        for l in v["limbs"]:
            extra = ""
            if l["verdict"] == "unverifiable":
                extra = " need=%s" % l.get("need")
            elif "limit" in l:
                extra = " value=%.1f limit=%.1f" % (l["value"], l["limit"])
                if l["verdict"] == "refuse":
                    extra += " refract_to=%.1f" % l["refract_to"]
            print("limb=%s %s%s" % (l["limb"], l["verdict"], extra))
            for note in l.get("assumed") or []:
                print("  assumed=%s" % note)
        if v["limits_missing"]:
            print("limits_missing=%s" % ",".join(v["limits_missing"]))
        if v["limits_error"]:
            print("limits_error=%s" % v["limits_error"])
        print("db=%s" % v["db"])
        print("scope=%s" % v["scope"])
        line = why_line(v)
        if line:
            print("why_line=%s" % line)
    return {"pass": 0, "refuse": 1, "unverifiable": 2}[v["verdict"]]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
