"""Adaptive daily session engine (day-plan), pure.

Spec: dynamic daily program design (2026-10-06) (owner decisions D1-D5
confirmed 2026-10-06 13:53). The base program is the vocabulary and the queue
is the default order (D1 a); the engine swaps or edits ONLY with a stated
reason token and inside the bounds of D2 a (swap the day type, drop / trim,
sets toward the allotment, +1 slot at most). With perfect attendance and no
fatigue signal the plan is the queue's session, byte for byte (neutral
invariant).

This module does no I/O and owns no fatigue arithmetic: readiness arrives as
per-muscle residual/dose ratios from the kit's muscle-state, done-so-far from
the kit's muscle-week `sets_effective`, thresholds from the kit's
STATE_RECOVERING / STATE_HARD, minutes and caps from compose_rank_rules.json
(`budget`, `set_caps`, `trainer_fit`). day_plan_rules.json holds only the rows
this layer adds. The `day-plan` CLI gathers the inputs; day_plan_sim.py feeds
the same function a synthetic world.

Shapes
  spec   {code: {'slots': [slot...]}}      slot = {name, sets, main, priority,
                                                    mw: {muscle: weight*credit}}
  state  {'done': {m: sets}, 'ratio': {m: residual/dose}, 'blocked': {m},
          'performed': {names done this week}, 'future_days': float,
          'unavailable': {names}}
  band   {m: {'floor','target','ceiling'}}
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# refusal / error codes (spec decision-point table)
E_BLOCKED = 'E-DAYPLAN-BLOCKED'
E_CEILING = 'E-DAYPLAN-CEILING'
E_MINUTES = 'E-DAYPLAN-MINUTES'
E_REGION = 'E-DAYPLAN-REGION'
E_OUTSET = 'E-DAYPLAN-OUTSET'

ENERGY = ('low',)


def load_rules():
    with open(os.path.join(HERE, 'day_plan_rules.json'), encoding='utf-8') as fh:
        mine = json.load(fh)
    import compose_rank
    cr = compose_rank.load_rules()
    b = cr['budget']
    mine['budget'] = {k: b[k] for k in ('compound_minutes', 'isolation_minutes',
                                        'transition_minutes', 'base_sets',
                                        'max_lifts', 'set_levels')}
    mine['set_caps'] = dict(cr['set_caps'])
    mine['primary_min_sets'] = cr['trainer_fit']['primary_min_sets']
    return mine


# -- spec from a program ----------------------------------------------------
def build_spec(program, muscle_map, credit=None, work_items=None):
    """{code: {'slots': [...]}} from program.yaml days. `muscle_map` =
    {exercise: [(muscle, role)]}; `credit(ex_dict)` -> muscle_credit factor
    (rx-calc slot_credit); `work_items(program, day)` -> the day's work slots
    (rx-calc day_work_items). Unmapped exercises carry no muscle (never
    guessed). A MAIN slot is a block main lift: priority < 400 (the product's
    band contract), else the first slot of the day."""
    spec = {}
    for code in program.get('rotation') or []:
        items = (work_items(program, code) if work_items else
                 ((program.get('days') or {}).get(code) or {}).get('exercises')
                 or [])
        slots = []
        for i, ex in enumerate(items):
            f = credit(ex) if credit else 1.0
            if f <= 0:
                continue
            pr = ex.get('priority')
            main = (pr < 400) if isinstance(pr, (int, float)) else i == 0
            slots.append({
                'name': ex.get('name', ''), 'sets': int(ex.get('sets', 3)),
                'main': bool(main),
                'priority': pr if isinstance(pr, (int, float)) else 1000 + i,
                'mw': {m: (1.0 if role == 'primary' else 0.5) * f
                       for m, role in muscle_map.get(ex.get('name', ''), [])}})
        slots.sort(key=lambda s: s['priority'])
        spec[code] = {'slots': slots}
    return spec


def primary_of(slot):
    return {m for m, w in slot['mw'].items() if w >= 1.0}


def deliver(slots):
    out = {}
    for s in slots:
        for m, w in s['mw'].items():
            out[m] = out.get(m, 0.0) + s['sets'] * w
    return out


def base_dose(spec, rotation, freq):
    """Weekly dose the program promises per muscle (rx-calc proposed_sets
    arithmetic: slot sets x weight x freq / len(rotation))."""
    f = freq / float(len(rotation)) if rotation else 1.0
    out = {}
    for code in rotation:
        for m, v in deliver(spec[code]['slots']).items():
            out[m] = out.get(m, 0.0) + v * f
    return out


# -- attendance (D4: blend observed attendance in early) -------------------
def attendance_weight(weeks_observed, rules):
    """0 below `start_weeks` of history, rising linearly to 1 at `full_weeks`
    (owner 2026-10-06 D4: start blending at 3 weeks, full by ~6)."""
    a = rules['attendance']
    lo, hi = a['start_weeks'], a['full_weeks']
    return min(1.0, max(0.0, (weeks_observed - lo) / float(hi - lo)))


def expected_days(rest_of_week, declared, observed, weeks_observed, rules):
    """Expected training days left this week after today. rest_of_week =
    weekday tokens after today; declared = set of declared main days;
    observed = {weekday: attended / weeks seen} (any day, supplementary
    included). Per day: (1-w) x declared(1|0) + w x observed rate -- the
    shrink-toward-declared blend; a non-declared day only counts through its
    observed rate x w, so catch-up days are never planned on from declaration
    alone (D4 a)."""
    w = attendance_weight(weeks_observed, rules)
    total = 0.0
    for d in rest_of_week:
        prior = 1.0 if d in declared else 0.0
        total += (1 - w) * prior + w * observed.get(d, prior)
    return total


# -- readiness -------------------------------------------------------------
def readiness(state, th, rules):
    """{muscle: 'ready'|'partial'|'blocked'}; th = (recovering, hard) from
    the kit. 'partial' acts from rules `act_ratio` (>= the kit's recovering
    cut): the kit's 0.5 is a display cut, and a muscle in the lower half of
    recovering is the ordinary two-day frequency, not a reason to edit.
    Pain-blocked muscles are blocked whatever the ratio."""
    act = max(th[0], rules['act_ratio'])
    out = {}
    for m, r in state['ratio'].items():
        out[m] = 'blocked' if r >= th[1] else 'partial' if r >= act else 'ready'
    for m in state.get('blocked', ()):
        out[m] = 'blocked'
    return out


def _slot_copy(s):
    c = dict(s)
    c['mw'] = dict(s['mw'])
    c['reasons'] = []
    return c


def _main_primaries(slots):
    return set().union(*(primary_of(s) for s in slots if s['main'])) if slots else set()


def _ahead(rotation, code, future_days):
    """[(code, weight)] the sessions the queue serves on the expected days
    left after `code` today: the rotation continues from `code`, a fractional
    day counts fractionally."""
    out, i, left = [], rotation.index(code), future_days
    while left > 1e-9 and len(out) < 4 * len(rotation):
        i = (i + 1) % len(rotation)
        out.append((rotation[i], min(1.0, left)))
        left -= 1.0
    return out


def _future(spec, rotation, code, future_days):
    """({muscle: expected future sessions loading it},
        {muscle: expected future effective sets})."""
    opp, sets = {}, {}
    for c, w in _ahead(rotation, code, future_days):
        for m, v in deliver(spec[c]['slots']).items():
            opp[m] = opp.get(m, 0.0) + w
            sets[m] = sets.get(m, 0.0) + w * v
    return opp, sets


def _score(code_slots, need, opp, floor_gap, warm, rules):
    sc = rules['score']
    total = 0.0
    dl = deliver(code_slots)
    for m, v in dl.items():
        allot = math.ceil(need.get(m, 0.0) / (1 + opp.get(m, 0.0)))
        w = 1.0 + (sc['floor_gap_bonus'] if floor_gap.get(m, 0) > 0 else 0.0)
        total += min(v, allot) * w
    for s in code_slots:
        for m in primary_of(s):
            if m in warm:
                total -= sc['partial_penalty'] * s['sets']
    return total


def _minutes(slot, rules):
    b = rules['budget']
    kind = b['compound_minutes'] if (slot['main'] or slot['priority'] < 400) \
        else b['isolation_minutes']
    return kind * slot['sets'] / float(b['base_sets']) + b['transition_minutes']


def plan(spec, rotation, head, band, base, state, th, rules,
         minutes=None, avoid=None, want=None, energy=None,
         supplementary=False, drills=None, open_codes=None):
    """One day's plan. head = the queue's next code (kit pass rule). Returns
    a dict: code, base_code, swapped, slots (final, each with reasons),
    prep, refusals, shortfall, reasons (day level). Deterministic."""
    if minutes is not None and minutes < rules['minutes_min']:
        return {'error': E_MINUTES, 'code': None}
    ready = readiness(state, th, rules)
    warm = {m for m, r in state['ratio'].items() if r >= th[0]} | {
        m for m, v in ready.items() if v != 'ready'}   # the kit's recovering cut: soft preference only
    done = state.get('done', {})
    need = {m: max(0.0, b['target'] - done.get(m, 0.0)) for m, b in band.items()}
    gap = {m: max(0.0, b['floor'] - done.get(m, 0.0)) for m, b in band.items()
           if base.get(m, 0.0) >= b['floor']}        # catch-up only where the program promised >= floor
    # future_days None = the training days are not declared: no catch-up or
    # exposure edits (nothing to plan against), swaps / trims still apply
    known = state.get('future_days') is not None
    fd = state.get('future_days') or 0.0
    day_reasons = []
    refusals = []

    def feasible(code):
        return not any(ready.get(m) == 'blocked'
                       for m in _main_primaries(spec[code]['slots']))

    def partial_main(code):
        return any(ready.get(m) == 'partial'
                   for m in _main_primaries(spec[code]['slots']))

    # the kit's pass rule: only the splits still open in the pass are
    # candidates ("defer A, do B first"); a pass with none feasible falls
    # back to the whole rotation
    pool = [c for c in (open_codes or rotation) if c in rotation]
    cands = [c for c in pool if feasible(c)] or [c for c in rotation if feasible(c)]
    if avoid:
        keep = [c for c in cands
                if avoid not in _main_primaries(spec[c]['slots'])
                and avoid not in {m for s in spec[c]['slots'] if s['main']
                                  for m in s['mw']}]
        if keep:
            cands = keep
            if head not in cands:
                day_reasons.append('wish_avoid')
    if not cands:
        return {'error': E_BLOCKED, 'code': None, 'refusals': [E_BLOCKED]}

    def best(pool):
        sc = {c: _score(spec[c]['slots'], need, _future(spec, rotation, c, fd)[0],
                        gap, warm, rules) for c in pool}
        # queue order breaks ties: head first, then rotation order
        order = sorted(pool, key=lambda c: (c != head, rotation.index(c)))
        return max(order, key=lambda c: sc[c])

    code = head if head in rotation else rotation[0]
    if supplementary:
        code = best(cands)
        day_reasons.append('supplementary')
    elif code not in cands:
        code = best(cands)
        day_reasons.append('swap_blocked')
    elif partial_main(code):
        calm = [c for c in cands if not partial_main(c)]
        if calm:
            code = best(calm)
            day_reasons.append('swap_recovery')
    if want and not supplementary:
        wanted = [c for c in cands
                  if want in deliver(spec[c]['slots']) and not any(
                      ready.get(m) == 'partial' for m in _main_primaries(spec[c]['slots']))]
        if wanted and code not in wanted:
            code = max(wanted, key=lambda c: deliver(spec[c]['slots']).get(want, 0))
            day_reasons.append('wish_want')

    slots = [_slot_copy(s) for s in spec[code]['slots']]
    caps = rules['set_caps']
    lo = rules['edits']['min_sets']
    pmin = rules['primary_min_sets']

    # a. drop a non-main slot whose primary muscle is blocked
    kept = []
    for s in slots:
        if not s['main'] and any(ready.get(m) == 'blocked' for m in primary_of(s)):
            day_reasons.append('drop_blocked')
            continue
        kept.append(s)
    slots = kept
    # b. trim sets on partial primaries (main keeps primary_min_sets)
    for s in slots:
        if any(ready.get(m) == 'partial' for m in primary_of(s)):
            floor = pmin if s['main'] else lo
            if s['sets'] > floor:
                s['sets'] -= rules['edits']['trim']
                s['reasons'].append('trim_partial')
    # energy low: one set off every non-main slot
    if energy == 'low':
        for s in slots:
            if not s['main'] and s['sets'] > lo:
                s['sets'] -= 1
                s['reasons'].append('energy_low')

    opp, fsets = _future(spec, rotation, code, fd)
    # tomorrow's session (the queue's next) when tomorrow is likely a training
    # day: an ADDED slot never stacks a muscle the next session works first
    tomorrow = set()
    if state.get('next_day_p', 0.0) >= 0.5 and _ahead(rotation, code, fd):
        nxt = _ahead(rotation, code, fd)[0][0]
        tomorrow = {m for s in spec[nxt]['slots'] for m in primary_of(s)}

    def capacity(m):
        """What this session plus the queue's expected future days add."""
        return deliver(slots).get(m, 0.0) + fsets.get(m, 0.0)

    # c. sets toward the allotment where the floor cannot close otherwise
    for s in (slots if known else ()):
        prim = [m for m in primary_of(s) if gap.get(m, 0) > 0]
        for m in prim:
            while (done.get(m, 0.0) + capacity(m) < band[m]['floor']
                   and s['sets'] < caps['compound' if s['main'] else 'isolation']):
                if done.get(m, 0.0) + deliver(slots).get(m, 0.0) + s['mw'][m] > band[m]['ceiling']:
                    refusals.append(E_CEILING)
                    break
                if deliver(slots).get(m, 0.0) + s['mw'][m] > rules['session_muscle_cap']:
                    refusals.append(E_CEILING)
                    break
                s['sets'] += 1
                if 'sets_catchup' not in s['reasons']:
                    s['reasons'].append('sets_catchup')
    # d/e. +1 slot at most: main exposure first, then the floor accessory
    add_max = rules['edits']['add_max']
    added = 0
    performed = state.get('performed', set())
    if (known and not supplementary and added < add_max and fd < 1.0
            and len(slots) < rules['budget']['max_lifts']):
        have = {s['name'] for s in slots}
        for c in rotation:
            if c == code:
                continue
            for s in spec[c]['slots']:
                if (s['main'] and s['name'] not in performed and s['name'] not in have
                        and s['name'] not in state.get('unavailable', ())
                        and not any(m in warm or m in tomorrow for m in primary_of(s))):
                    n = _slot_copy(s)
                    n['reasons'].append('main_exposure')
                    n['from'] = c
                    slots.append(n)
                    added += 1
                    break
            if added:
                break
    if known and added < add_max and len(slots) < rules['budget']['max_lifts']:
        have = {s['name'] for s in slots}
        for m in sorted(gap, key=lambda x: -gap[x]):
            if gap[m] <= 0 or done.get(m, 0.0) + capacity(m) >= band[m]['floor']:
                continue
            if m in warm or m in tomorrow:
                continue
            pool = [s for c in rotation for s in spec[c]['slots']
                    if not s['main'] and m in primary_of(s)
                    and s['name'] not in have
                    and s['name'] not in state.get('unavailable', ())]
            if not pool:
                continue
            s = min(pool, key=lambda x: x['priority'])
            n = _slot_copy(s)
            if done.get(m, 0.0) + deliver(slots).get(m, 0.0) + n['sets'] * n['mw'][m] > band[m]['ceiling']:
                refusals.append(E_CEILING)
                continue
            n['reasons'].append('floor_catchup')
            slots.append(n)
            added += 1
            break

    # fit the minutes: lowest-weight accessory out, then 3 -> 2 sets on
    # accessories; a main never goes below primary_min_sets
    if minutes is not None:
        def total():
            return sum(_minutes(s, rules) for s in slots)
        while total() > minutes:
            acc = [s for s in slots if not s['main']]
            if acc:
                worst = max(acc, key=lambda s: s['priority'])
                if worst['sets'] > lo and any(a['sets'] > lo for a in acc):
                    # set level first on the heaviest accessory, then drop
                    cut = max((a for a in acc if a['sets'] > lo),
                              key=lambda a: a['priority'])
                    cut['sets'] -= 1
                    cut['reasons'].append('fit_minutes')
                    continue
                slots.remove(worst)
                day_reasons.append('fit_minutes')
                continue
            mains = [s for s in slots if s['main'] and s['sets'] > pmin]
            if not mains:
                break
            mains[-1]['sets'] -= 1
            mains[-1]['reasons'].append('fit_minutes')
    # prep follows the muscles actually loaded today
    prep = []
    loaded = set().union(*(set(s['mw']) for s in slots)) if slots else set()
    for d in drills or ():
        if set(d['needs']) & loaded or not d['needs']:
            prep.append(d['name'])
    after = dict(done)
    for m, v in deliver(slots).items():
        after[m] = after.get(m, 0.0) + v
    shortfall = {} if not known else {m: round(band[m]['floor'] - after.get(m, 0.0) - fsets.get(m, 0.0), 2)
                 for m in gap
                 if band[m]['floor'] - after.get(m, 0.0) - fsets.get(m, 0.0) > 0.5}
    return {'code': code, 'base_code': head, 'swapped': code != head,
            'slots': [{k: s[k] for k in ('name', 'sets', 'main', 'reasons')
                       } | ({'from': s['from']} if 'from' in s else {})
                      for s in slots],
            'prep': prep, 'reasons': sorted(set(day_reasons)),
            'refusals': sorted(set(refusals)), 'shortfall': shortfall,
            'supplementary': supplementary}


def base_slots(spec, code):
    """The rotation session as the plan renders it (neutral reference)."""
    return [{'name': s['name'], 'sets': s['sets'], 'main': s['main'],
             'reasons': []} for s in spec[code]['slots']]


def ratios_from_nodes(nodes, lift):
    """{muscle: ratio} from the kit's muscle-state rows (kind == 'muscle').
    A node carrying an active body signal reads as at least
    `lift` (rules act_ratio): a stiff/tight/sore signal makes the muscle
    partial (spec readiness), never blocked."""
    out = {}
    for n, r in nodes.items():
        if r.get('kind') != 'muscle':
            continue
        ratio = r['ratio']
        if r.get('signals'):
            ratio = max(ratio, lift)
        out[n] = ratio
    return out
