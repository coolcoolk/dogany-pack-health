#!/usr/bin/env python3
"""
"뭐 먹지" SHORTLIST -- the engine half of "what should I eat".

WHY (2026-09-30 overnight-followups item 6, owner go 17:40). Asked for an
alternative, the model used to answer from nothing: a free-text food out of
its own head, with calorie arithmetic done in prose. Gate 4 (engine-first)
says the decision is the engine's and the model only SPEAKS it. So:

    remaining kcal / protein for the day    (card.py day_goals -- the SAME
                                             target the card draws: carry,
                                             burn, G6 floor included)
  x the foods the owner has actually logged (kit MEALS_V32 surface, last
                                             `window` days: how often, and
                                             the typical serving as eaten)
  -> ranked by fit, each with its own projection (kcal_after, protein_after).

WHAT IT NEVER DOES. It never proposes a food the owner has not eaten (no
catalog, no model knowledge), never writes anything (no meal-add, no cache
write), and never ranks an item that would cross the target: an item whose
typical serving is bigger than what is left is excluded and counted. No room
left at all -> status `no_room` and an empty list -- the card already says
"초과", and a suggestion list at that point is an unrequested nudge.

FIT (explainable on purpose -- `why` names the dominant term):
  protein still owed  : 0.5 x share of the owed protein this serving covers
                        + 0.2 x protein density (g per 100 kcal, capped at 10)
                        + 0.3 x how often it was logged (relative to the top)
  protein already met : 0.7 x frequency + 0.3 x how much room it leaves
Foods logged twice or more fill the list first; one-offs only top it up.

MEAL SPLIT + COMBOS (owner incident 2026-10-13 13:19). The shortlist alone
ranked single foods against the DAY's remainder, so nothing stopped "the day's
protein in one dinner": the model subtracted a planned 25 g shake from the
120 g left by hand and told the owner to eat 95 g at dinner. `plan` closes
both halves in code:
  * the remainder (minus anything the owner says is still coming, --planned)
    is split over the meal slots still ahead TODAY -- the owner's usual slots
    (logged on >= 30% of logged days in the window) that are not taken today
    and whose clock (+90 min grace) is not past;
  * every meal is capped at a per-meal protein CEILING from body weight (see
    PROTEIN_PER_MEAL_G_PER_KG); what cannot fit goes to ONE explicit
    SHORTFALL entry (a snack / shake slot up to the same ceiling, then the
    plain gap) -- never into one giant meal;
  * each slot carries 1-3 item COMBOS from the owner's own history with their
    totals already summed, so the model relays numbers and adds nothing.

Usage:
  suggest.py [--date YYYY-MM-DD] [--carry-kcal N] [--limit 5] [--window 60]
             [--now HH:MM] [--planned '{"name": ..., "protein": .., "kcal": ..}']...
Prints one JSON object. Exit 0 whenever the read itself succeeded; the
"nothing to suggest" cases are `status`, never an exit code.
"""
import argparse
import datetime
import importlib.util
import json
import os
import statistics
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.abspath(os.path.join(_HERE, "..", "..", ".."))
LIFEKIT_PATH = os.path.join(_PROJECT_ROOT, "database", "kit_life.py")

PLANNED_TAG = '(예정)'           # card.py's contract: not eaten yet
WINDOW_DAYS = 60
LIMIT = 5
DENSITY_CAP = 10.0               # g protein per 100 kcal that scores 1.0

# -- per-meal split ------------------------------------------------------------
# Per-meal protein CEILING. Source: Schoenfeld BJ & Aragon AA, "How much
# protein can the body use in a single meal for muscle-building? Implications
# for daily protein distribution", J Int Soc Sports Nutr 2018;15:10
# (doi:10.1186/s12970-018-0215-1): 0.4 g/kg/meal over >= 4 meals, and
# 0.55 g/kg/meal as the upper end (2.2 g/kg/day over the same four meals).
# We take that upper end as the ceiling, held inside 40-60 g: 40 g is the dose
# Macnaughton et al. 2016 (Physiol Rep 4:e12893) found beat 20 g after
# whole-body training, and above ~60 g a single sitting stops being a
# realistic meal for this owner (the 2026-10-13 95 g dinner was the failure).
PROTEIN_PER_MEAL_G_PER_KG = 0.55
PROTEIN_MEAL_FLOOR_G = 40
PROTEIN_MEAL_CAP_G = 60
# Wall-clock anchor (minutes after local midnight) per kit meal_slot label.
# A slot is still "ahead" until its anchor + SLOT_GRACE_MIN has passed.
# Labels: breakfast, lunch, snack, dinner, late-night -- \u-escaped, as are
# the spoken lines below (test-ascii-ratchet: no file's non-ASCII count rises).
SLOT_CLOCK = (('\uc544\uce68', 8 * 60), ('\uc810\uc2ec', 12 * 60 + 30), ('\uac04\uc2dd', 16 * 60),
              ('\uc800\ub141', 19 * 60), ('\uc57c\uc2dd', 22 * 60))
SLOT_GRACE_MIN = 90
USUAL_SHARE = 0.3                # slot logged on >= 30% of logged days
DEFAULT_SLOTS = ('\uc544\uce68', '\uc810\uc2ec', '\uc800\ub141')
SNACK_SLOT = '\uac04\uc2dd\u00b7\uc250\uc774\ud06c'
SNACK_KCAL_WEIGHT = 0.4          # a snack slot's kcal share vs a full meal
COMBO_POOL = 12                  # most-logged foods considered for combos
COMBO_MAX_ITEMS = 3
COMBO_LIMIT = 3
COMBO_MIN_SHARE = 0.5            # a combo covers >= half the slot's protein


def kit_life():
    """The kit facade: the one already imported (card.py / a test put it in
    sys.modules) or the sibling database/kit_life.py (carryover.py's idiom)."""
    mod = sys.modules.get("kit_life")
    if mod is not None:
        return mod
    spec = importlib.util.spec_from_file_location("kit_life", LIFEKIT_PATH)
    if spec is None or spec.loader is None:
        raise ImportError("kit_life SDK not found: %s" % LIFEKIT_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules.setdefault("kit_life", mod)
    spec.loader.exec_module(mod)
    return mod


def _card():
    """card.py beside this file, by path, without bytecode (same residue rule
    as card.py's _sibling). Imported for day_goals/day_state/projection only;
    it no longer needs matplotlib for those."""
    path = os.path.join(_HERE, "card.py")
    prev = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec = importlib.util.spec_from_file_location("dietstatus_card", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        sys.dont_write_bytecode = prev


def _strip_planned(name):
    n = str(name or '').rstrip()
    if n.endswith(PLANNED_TAG):
        return None
    return n


def history(life=None, today=None, window=WINDOW_DAYS):
    """The owner's logged foods over [today - window, today], grouped by the
    kit's own food key. One entry per food: times logged, the typical serving
    (median of what was actually logged), last date, display name (latest).
    Planned rows (`(예정)`) are not food that was eaten and are skipped."""
    life = life or kit_life()
    today = today or datetime.date.today()
    lo = (today - datetime.timedelta(days=window)).isoformat()
    conn = life.get_conn()
    try:
        rows = conn.execute(
            "SELECT date, name, kcal, protein, fat, carb FROM " + life.MEALS_V32
            + " WHERE date >= ? AND date <= ? ORDER BY date, id;",
            (lo, today.isoformat())).fetchall()
    finally:
        conn.close()
    groups = {}
    for date, name, kcal, protein, fat, carb in rows:
        name = _strip_planned(name)
        if not name or not kcal or float(kcal) <= 0:
            continue
        key = life.normalize_food_key(name) or name
        g = groups.setdefault(key, {'key': key, 'rows': []})
        g['rows'].append((date, name, float(kcal), float(protein or 0),
                          float(fat or 0), float(carb or 0)))
    out = []
    for key, g in groups.items():
        rs = g['rows']
        med = lambda i: statistics.median(r[i] for r in rs)   # noqa: E731
        out.append({'key': key, 'name': rs[-1][1], 'times': len(rs),
                    'last_date': rs[-1][0],
                    'kcal': round(med(2)), 'protein': round(med(3), 1),
                    'fat': round(med(4), 1), 'carbs': round(med(5), 1)})
    return out


def history_item(name, life=None, today=None, window=WINDOW_DAYS):
    """The owner's typical logged serving of `name`, or None."""
    life = life or kit_life()
    key = life.normalize_food_key(name)
    for h in history(life, today, window):
        if h['key'] == key:
            return h
    return None


def _portion_g(life, name):
    try:
        p = life.portion_lookup(name)
    except Exception:            # noqa: BLE001 -- display nicety only
        return None
    return p.get('grams') if p.get('found') else None


def rank(state, foods, limit=LIMIT):
    """Pure: day_state x history -> (ranked items, excluded_over count)."""
    r_k = state['remaining_kcal']
    r_p = state['remaining_protein_g']
    fits = [f for f in foods if f['kcal'] <= r_k]
    excluded = len(foods) - len(fits)
    top = max([f['times'] for f in fits] or [1])
    scored = []
    for f in fits:
        freq = f['times'] / float(top)
        if r_p > 0:
            cover = min(f['protein'], r_p) / float(r_p)
            dens = min(f['protein'] * 100.0 / f['kcal'] / DENSITY_CAP, 1.0)
            terms = {'protein': 0.5 * cover + 0.2 * dens, 'frequent': 0.3 * freq}
        else:
            terms = {'frequent': 0.7 * freq,
                     'light': 0.3 * (1.0 - f['kcal'] / float(r_k))}
        fit = sum(terms.values())
        scored.append((f['times'] >= 2, round(fit, 3), f['times'], f,
                       max(terms, key=terms.get)))
    scored.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    return [dict(f, fit=fit, why=why) for _, fit, _, f, why in scored[:limit]], excluded


def _line(item, window):
    portion = ' (보통 %gg)' % item['portion_g'] if item.get('portion_g') else ''
    return ('%s%s: %skcal, 단백질 %gg (최근 %d일 %d번 기록), 먹고 나면 남는 칼로리 %skcal'
            % (item['name'], portion, format(item['kcal'], ','),
               round(item['protein']), window, item['times'],
               format(item['remaining_kcal_after'], ',')))


# -- per-meal split + combos (2026-10-13) -------------------------------------

def protein_ceiling(stats, defaults_used=()):
    """{g, weight_kg, basis}: the per-meal protein ceiling from the body
    weight in the kit's body state (load_body_stats -- the same stats the
    card's target uses). No weight -> the floor, said so in `basis`."""
    w = (stats or {}).get('weight_kg')
    try:
        w = float(w) if w not in (None, '') else None
    except (TypeError, ValueError):
        w = None
    if not w or w <= 0:
        return {'g': PROTEIN_MEAL_FLOOR_G, 'weight_kg': None, 'basis': 'floor'}
    g = round(PROTEIN_PER_MEAL_G_PER_KG * w)
    g = max(PROTEIN_MEAL_FLOOR_G, min(PROTEIN_MEAL_CAP_G, g))
    basis = 'default_weight' if 'weight_kg' in tuple(defaults_used or ()) else 'weight'
    return {'g': g, 'weight_kg': w, 'basis': basis}


def slot_days(life=None, today=None, window=WINDOW_DAYS):
    """({slot: days logged}, days with any meal, slots taken TODAY). Planned
    rows count as taken today (that slot already has its food), never as
    history."""
    life = life or kit_life()
    today = today or datetime.date.today()
    lo = (today - datetime.timedelta(days=window)).isoformat()
    conn = life.get_conn()
    try:
        rows = conn.execute(
            "SELECT date, meal, name FROM " + life.MEALS_V32
            + " WHERE date >= ? AND date <= ?;",
            (lo, today.isoformat())).fetchall()
    finally:
        conn.close()
    iso = today.isoformat()
    per, days, taken = {}, set(), set()
    for date, meal, name in rows:
        meal = str(meal or '').strip()
        if date == iso:
            if meal:
                taken.add(meal)
            continue
        if _strip_planned(name) is None:
            continue
        days.add(date)
        if meal:
            per.setdefault(meal, set()).add(date)
    return {k: len(v) for k, v in per.items()}, len(days), taken


def usual_slots(per, n_days):
    """The owner's usual slots in clock order; no history -> DEFAULT_SLOTS."""
    known = [n for n, _ in SLOT_CLOCK]
    if n_days <= 0:
        return list(DEFAULT_SLOTS)
    out = [n for n in known if per.get(n, 0) / float(n_days) >= USUAL_SHARE]
    return out or list(DEFAULT_SLOTS)


def local_now(life=None):
    """Local wall clock: the declared AGENT_TZ_OFFSET_HOURS (env, then the
    kit's agent.conf reader) over UTC; undeclared -> the host clock."""
    raw = os.environ.get('AGENT_TZ_OFFSET_HOURS')
    if raw in (None, '') and life is not None:
        try:
            raw = life._card_tz_offset()
        except Exception:        # noqa: BLE001 -- host clock below
            raw = None
    try:
        off = float(raw) if raw not in (None, '') else None
    except (TypeError, ValueError):
        off = None
    if off is None:
        return datetime.datetime.now()
    return (datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(hours=off)).replace(tzinfo=None)


def _minutes(now, iso):
    """Minutes after local midnight of `iso` (past date -> after the last
    slot, future date -> 0)."""
    d = datetime.date.fromisoformat(iso)
    if now.date() > d:
        return 24 * 60
    if now.date() < d:
        return 0
    return now.hour * 60 + now.minute


def slots_ahead(usual, taken, minute):
    clock = dict(SLOT_CLOCK)
    return [s for s in usual
            if s not in taken and clock[s] + SLOT_GRACE_MIN > minute]


def _resolve_extra(card, planned):
    """--planned entries -> resolved numbers (card.resolve_candidate: given
    numbers > food cache > owner history). Unknown -> available False."""
    out = []
    for p in planned or ():
        p = p if isinstance(p, dict) else {'name': str(p)}
        rc = card.resolve_candidate(p)
        if rc.get('found'):
            out.append({'name': rc['name'], 'available': True,
                        'kcal': round(rc.get('kcal') or 0),
                        'protein': round(rc.get('protein') or 0)})
        else:
            out.append({'name': rc.get('name'), 'available': False})
    return out


def _split(total, n):
    """`total` over n parts, integers that sum back to round(total)."""
    total = int(round(total))
    if n <= 0:
        return []
    base, rem = divmod(total, n)
    return [base + (1 if i < rem else 0) for i in range(n)]


def combos(foods, protein_target, kcal_budget, ceiling,
           max_items=COMBO_MAX_ITEMS, limit=COMBO_LIMIT, pool=COMBO_POOL):
    """1..max_items-item combos of the owner's logged foods whose SUMMED
    protein stays <= ceiling and summed kcal <= kcal_budget and covers at
    least COMBO_MIN_SHARE of protein_target, closest to
    protein_target first (then the more often eaten). Totals are computed
    here so nobody adds them up in prose."""
    import itertools
    cand = sorted((f for f in foods if f['kcal'] > 0),
                  key=lambda f: (f['times'] >= 2, f['times']), reverse=True)[:pool]
    found = []
    for k in range(1, max_items + 1):
        for combo in itertools.combinations(cand, k):
            kcal = sum(f['kcal'] for f in combo)
            prot = sum(f['protein'] for f in combo)
            if kcal > kcal_budget or prot > ceiling:
                continue
            if prot < COMBO_MIN_SHARE * protein_target:
                continue         # a 5 g rice bowl is not a 41 g slot's answer
            found.append((abs(protein_target - prot),
                          -sum(f['times'] for f in combo), k, combo,
                          round(kcal), round(prot)))
    found.sort(key=lambda x: (x[0], x[1], x[2]))
    out = []
    for _, _, _, combo, kcal, prot in found[:limit]:
        names = [f['name'] for f in combo]
        out.append({'items': names, 'kcal': kcal, 'protein': prot,
                    'line': '%s: %skcal, \ub2e8\ubc31\uc9c8 %dg'
                            % (' + '.join(names), format(kcal, ','), prot)})
    return out


def meal_plan(state, foods, stats, defaults_used, per, n_days, taken, minute,
              extra=()):
    """Pure: the day's remainder split over the slots still ahead, each under
    the per-meal ceiling, plus one SHORTFALL entry for what cannot fit."""
    ceil = protein_ceiling(stats, defaults_used)
    C = ceil['g']
    usual = usual_slots(per, n_days)
    ahead = slots_ahead(usual, taken, minute)
    known = [e for e in extra if e.get('available')]
    rp = max(0, state['remaining_protein_g'] - sum(e['protein'] for e in known))
    rk = max(0, state['remaining_kcal'] - sum(e['kcal'] for e in known))
    n = len(ahead)
    if n and rp <= n * C:
        meal_p, over = _split(rp, n), 0
    else:
        meal_p, over = [C] * n, rp - n * C
    snack_p = min(over, C)
    gap = over - snack_p
    weights = [1.0] * n + ([SNACK_KCAL_WEIGHT] if snack_p else [])
    wsum = sum(weights) or 1.0
    kcal_parts = [int(rk * w / wsum) for w in weights]
    if kcal_parts:
        kcal_parts[0] += int(rk) - sum(kcal_parts)
    plan = {'now': '%02d:%02d' % divmod(min(minute, 24 * 60 - 1), 60),
            'ceiling_g': C, 'ceiling_basis': ceil['basis'],
            'weight_kg': ceil['weight_kg'], 'usual_slots': usual,
            'taken_today': sorted(taken),
            'remaining_protein_g': rp, 'remaining_kcal': int(rk),
            'planned': list(extra), 'meals': [], 'shortfall': None,
            'lines': []}
    for e in extra:
        plan['lines'].append(
            '\uc608\uc815 %s: %skcal, \ub2e8\ubc31\uc9c8 %dg (\ub0a8\uc740 \uc591\uc5d0\uc11c \ube90\uc5b4\uc694)'
            % (e['name'], format(e['kcal'], ','), e['protein'])
            if e.get('available') else
            '\uc608\uc815 %s: \uc218\uce58\ub97c \ubab0\ub77c\uc11c \ub0a8\uc740 \uc591\uc5d0\uc11c \ube7c\uc9c0 \ubabb\ud588\uc5b4\uc694' % e['name'])
    for i, slot in enumerate(ahead):
        m = {'slot': slot, 'protein_g': meal_p[i], 'kcal': kcal_parts[i],
             'combos': combos(foods, meal_p[i], kcal_parts[i], C)}
        m['line'] = '%s: \ub2e8\ubc31\uc9c8 %dg, \uce7c\ub85c\ub9ac %skcal' % (
            slot, m['protein_g'], format(m['kcal'], ','))
        plan['meals'].append(m)
        plan['lines'].append(m['line'])
        plan['lines'].extend('  - ' + c['line'] for c in m['combos'])
    if over > 0:
        sf = {'kind': 'SHORTFALL', 'protein_g': over, 'ceiling_g': C,
              'snack_slot': SNACK_SLOT if snack_p else None,
              'snack_protein_g': snack_p,
              'snack_kcal': kcal_parts[-1] if snack_p else 0,
              'unfilled_protein_g': gap,
              'combos': combos(foods, snack_p, kcal_parts[-1], C, max_items=2)
              if snack_p else []}
        if n:
            head = '\ub07c\ub2c8\ub2f9 \ub2e8\ubc31\uc9c8\uc740 %dg\uae4c\uc9c0\ub77c %dg\uc740 \ub07c\ub2c8\uc5d0 \ubabb \ub2f4\uc544\uc694.' % (C, over)
        else:
            head = '\uc624\ub298 \ub0a8\uc740 \ub07c\ub2c8\uac00 \uc5c6\uc5b4\uc11c \ub2e8\ubc31\uc9c8 %dg\uc774 \ub0a8\uc544\uc694.' % over
        tail = ' %s \ud55c \ubc88\uc73c\ub85c %dg (\uce7c\ub85c\ub9ac %skcal)' % (
            SNACK_SLOT, snack_p, format(sf['snack_kcal'], ','))
        tail += (', \uadf8\ub798\ub3c4 %dg\uc740 \uc624\ub298 \ubabb \ucc44\uc6cc\uc694.' % gap) if gap else ' \ucc44\uc6b0\uba74 \ub3fc\uc694.'
        sf['line'] = head + tail
        plan['shortfall'] = sf
        plan['lines'].append(sf['line'])
        plan['lines'].extend('  - ' + c['line'] for c in sf['combos'])
    plan['status'] = ('protein_met' if rp == 0 else
                      'shortfall' if over > 0 else 'ok')
    return plan


def plan_for(card, state, foods, iso, window=WINDOW_DAYS, now=None,
             planned=()):
    """meal_plan() fed from the kit: body stats, slot history, the clock."""
    life = card.life
    stats = card.load_body_stats()
    try:
        used = life.body_stats_defaults_used(stats)
    except Exception:            # noqa: BLE001 -- older kit: treat as measured
        used = ()
    today = datetime.date.fromisoformat(iso)
    per, n_days, taken = slot_days(life, today, window)
    now = now or local_now(life)
    return meal_plan(state, foods, stats, used, per, n_days, taken,
                     _minutes(now, iso), _resolve_extra(card, planned))


def shortlist(day, limit=LIMIT, window=WINDOW_DAYS, today=None, card=None,
              now=None, planned=()):
    """The whole answer. `day` is card.py's input dict (date / carry_kcal /
    optional explicit numbers), loaded exactly as the card loads it. `plan`
    is the per-meal split (None when there is no room left at all)."""
    card = card or _card()
    life = card.life
    day, iso = card.load_day(day)
    state = card.day_state(day)
    today = today or datetime.date.fromisoformat(iso)
    foods = history(life, today, window)
    out = {'date': iso, 'window_days': window, 'state': state,
           'excluded_over': 0, 'items': [], 'plan': None}
    if state['remaining_kcal'] <= 0:
        out['status'] = 'no_room'
        return out
    out['plan'] = plan_for(card, state, foods, iso, window, now, planned)
    if not foods:
        out['status'] = 'no_history'
        return out
    items, excluded = rank(state, foods, limit)
    out['excluded_over'] = excluded
    for it in items:
        pj = card.projection(state, dict(it, found=True, basis='history',
                                         grams=None))
        it['portion_g'] = _portion_g(life, it['name'])
        for k in ('kcal_after', 'protein_after', 'over_kcal',
                  'remaining_kcal_after', 'remaining_protein_after'):
            it[k] = pj[k]
        it['line'] = _line(it, window)
        out['items'].append(it)
    out['status'] = 'ok' if out['items'] else 'nothing_fits'
    return out


def main(argv):
    ap = argparse.ArgumentParser(prog="suggest.py")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default: today)")
    ap.add_argument("--carry-kcal", type=int, default=0,
                    help="carryover.py's carry, exactly as passed to the card")
    ap.add_argument("--limit", type=int, default=LIMIT)
    ap.add_argument("--window", type=int, default=WINDOW_DAYS)
    ap.add_argument("--now", default=None,
                    help="HH:MM local clock (default: declared tz offset)")
    ap.add_argument("--planned", action="append", default=[],
                    help='food still coming today, not logged: JSON '
                         '{"name": .., "protein": .., "kcal": ..} or a name')
    a = ap.parse_args(argv)
    now = None
    if a.now:
        hh, mm = (int(x) for x in a.now.split(':'))
        base = (datetime.date.fromisoformat(a.date) if a.date
                else local_now().date())
        now = datetime.datetime.combine(base, datetime.time(hh, mm))
    planned = []
    for p in a.planned:
        try:
            planned.append(json.loads(p))
        except ValueError:
            planned.append({'name': p})
    day = {}
    if a.date:
        day['date'] = a.date
    if a.carry_kcal:
        day['carry_kcal'] = a.carry_kcal
    print(json.dumps(shortlist(day, limit=a.limit, window=a.window, now=now,
                               planned=planned),
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
