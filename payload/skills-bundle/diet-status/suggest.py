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

Usage:
  suggest.py [--date YYYY-MM-DD] [--carry-kcal N] [--limit 5] [--window 60]
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


def shortlist(day, limit=LIMIT, window=WINDOW_DAYS, today=None, card=None):
    """The whole answer. `day` is card.py's input dict (date / carry_kcal /
    optional explicit numbers), loaded exactly as the card loads it."""
    card = card or _card()
    life = card.life
    day, iso = card.load_day(day)
    state = card.day_state(day)
    today = today or datetime.date.fromisoformat(iso)
    foods = history(life, today, window)
    out = {'date': iso, 'window_days': window, 'state': state,
           'excluded_over': 0, 'items': []}
    if state['remaining_kcal'] <= 0:
        out['status'] = 'no_room'
        return out
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
    a = ap.parse_args(argv)
    day = {}
    if a.date:
        day['date'] = a.date
    if a.carry_kcal:
        day['carry_kcal'] = a.carry_kcal
    print(json.dumps(shortlist(day, limit=a.limit, window=a.window),
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
