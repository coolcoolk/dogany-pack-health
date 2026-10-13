"""Adjacent-session fatigue overlap (owner 2026-10-06 21:50: neighbouring
sessions need their shared fatigue counted, and an RDL after the deadlift in
one session is too much).

The rotation is a queue over flexible training days, so any two neighbouring
sessions of the queue (the last wraps to the first) may land on back-to-back
days: the tightest plausible gap is rules fatigue_overlap.gap_days_tightest.
Two neighbours OVERLAP on a stressor (spinal/axial load, hinge/hamstrings,
grip, one primary muscle) when both carry a lift of that stressor's carrier
class -- a high-fatigue lift by the per-lift fatigue grade (rx-calc
exercise_fatigue_cost / its heuristic). Same-session stacking (a second heavy
hinge after the deadlift) is compose_rank.stack_errors.

Pure: the caller hands the lift facts ({pattern, fatigue, primary}); the
composer (compose_draft) lightens the non-anchor lift of an overlap, the
volume audit (rx-calc volume_audit 'session_overlap') reports the numbers.

Evidence (kimwog exercise/adjacent-session-overlap-cost-067): at equal weekly
volume back-to-back days cost no strength or size (B); the next-day cost
scales with effort -- sets to failure cost the next session, sets well short
of it recover within hours (C); no lifter study links an overlap to injury.
So every overlap here is a SOFT preference: the draft lightens a lift only
when the whole draft still validates, nothing is ever refused on an overlap.
The spinal stressor is a practitioner rule (D: no spine recovery clock was
found). Grip is reported, never swapped (a stressor with "swap": false): it
limits pulling sets within a session and has no next-day data (D; the lever
is straps). A squat day next to a hinge day is a light lower-body
back-to-back fact (rules lower_adjacency): reported, never a swap.
"""
import json
from pathlib import Path

RULES_PATH = Path(__file__).with_name('compose_rank_rules.json')
GRADE_RANK = {'low': 0, 'med': 1, 'medium': 1, 'high': 2}


def rules_spec(rules=None):
    if rules is None:
        rules = json.loads(RULES_PATH.read_text())
    return rules.get('fatigue_overlap') or {}


def _match(cond, fact):
    """compose_rank-style condition: key_in (value in list), key_any
    (list intersection), key (equality)."""
    for key, value in cond.items():
        if key.endswith('_any'):
            ok = bool(set(value) & set(fact.get(key[:-4]) or ()))
        elif key.endswith('_in'):
            ok = fact.get(key[:-3]) in value
        else:
            ok = fact.get(key) == value
        if not ok:
            return False
    return True


def carries(stressor, fact):
    return any(_match(c, fact) for c in stressor.get('carriers', ()))


def swaps(stressor):
    """True when the draft may lighten a lift over this stressor (rules
    `swap`, default true); a report-only stressor (grip) is false."""
    return stressor.get('swap', True) is not False


def is_anchor(stressor, fact):
    """An anchor carries the stressor by the session's purpose (the lower
    day's squat / hinge): an overlap is resolved on the OTHER lift; two
    anchors are the heavy-lift spacing's to space (program-plan
    apply_spacing), here only reported."""
    anchor = stressor.get('anchors')
    return bool(anchor) and _match(anchor, fact)


def stressor_keys(fact, spec):
    """[(key, stressor)] the lift carries: a per_primary stressor yields one
    key per primary muscle ('muscle:quads')."""
    out = []
    for s in spec.get('stressors', ()):
        if not carries(s, fact):
            continue
        if s.get('per_primary'):
            out.extend(('%s:%s' % (s['id'], m), s) for m in fact.get('primary') or ())
        else:
            out.append((s['id'], s))
    return out


def neighbours(rotation):
    """Consecutive pairs of the queue, the last wrapping to the first."""
    n = len(rotation)
    if n < 2:
        return []
    return [(rotation[i], rotation[(i + 1) % n]) for i in range(n if n > 2 else 1)]


def overlaps(rotation, days, facts, rules=None, gaps=None, units=None):
    """The overlap report of a composed week.

    rotation: [code, ...]; days: {code: [{'name', 'sets'?}, ...]};
    facts(name) -> {'pattern', 'fatigue', 'primary'} or None;
    gaps: {(first, then): {'days', 'source'}} (optional: the measured or
    planned calendar gap of that seam, said beside the tightest);
    units: {code: axial units} (optional, rx-calc axial_layer per_day).
    Returns {'gap_days_tightest', 'pairs': [...], 'clashes', 'resolvable'}
    -- each pair entry names both sessions, the gap (tightest and, when
    known, planned), and per shared stressor the lifts on each side with
    their fatigue grade and sets (and, given, both days' axial units);
    'resolvable' counts the non-anchor lifts inside an overlap (a row next
    to the deadlift day still counts when the deadlift keeps the overlap)."""
    spec = rules_spec(rules)
    by_id = {s['id']: s for s in spec.get('stressors', ())}
    pairs, clashes, resolvable = [], 0, 0
    for first, then in neighbours(list(rotation)):
        sides = {}
        for code in (first, then):
            carried = {}
            for ex in days.get(code) or ():
                f = facts(ex['name'])
                if not f:
                    continue
                for key, s in stressor_keys(f, spec):
                    carried.setdefault(key, []).append(dict(
                        name=ex['name'], fatigue=f.get('fatigue'),
                        sets=ex.get('sets'), anchor=is_anchor(s, f)))
            sides[code] = carried
        shared = []
        for key in sorted(set(sides[first]) & set(sides[then])):
            a, b = sides[first][key], sides[then][key]
            s = by_id[key.split(':')[0]]
            swap = swaps(s)
            loose = sum(not x['anchor'] for x in a + b) if swap else 0
            shared.append(dict(stressor=key, first_lifts=a, then_lifts=b,
                               fixable=bool(loose), swap=swap,
                               grade=s.get('grade')))
            clashes += 1
            resolvable += loose
        entry = dict(first=first, then=then,
                     gap_days_tightest=spec.get('gap_days_tightest', 1),
                     shared=shared)
        lower = lower_adjacency(days.get(first), days.get(then), facts, spec)
        if lower:
            entry['lower_back_to_back'] = lower
        if gaps and (first, then) in gaps:
            entry['gap'] = dict(gaps[(first, then)])
        if units:
            entry['axial_units'] = {first: units.get(first), then: units.get(then)}
        pairs.append(entry)
    return dict(gap_days_tightest=spec.get('gap_days_tightest', 1),
                pairs=pairs, clashes=clashes, resolvable=resolvable,
                evidence=dict(spec.get('evidence') or {}))


def lower_adjacency(first_items, then_items, facts, spec):
    """The light lower-body back-to-back fact (rules lower_adjacency): one
    side holds a lift of one lower pattern (squat), the other a lift of
    the other (hinge), either order -- both load the hip extensors and the
    trunk. Reported at its level ('light'), never a swap; None when the
    pair holds no such cross."""
    rule = spec.get('lower_adjacency')
    if not rule:
        return None
    grades = set(rule.get('fatigue_in') or ('high', 'med'))

    def held(items):
        out = {}
        for ex in items or ():
            f = facts(ex['name'])
            if f and f.get('pattern') in rule['patterns'] and f.get('fatigue') in grades:
                out.setdefault(f['pattern'], []).append(dict(
                    name=ex['name'], fatigue=f.get('fatigue'), sets=ex.get('sets')))
        return out
    a, b = held(first_items), held(then_items)
    x, y = rule['patterns'][:2]
    if not ((x in a and y in b) or (y in a and x in b)):
        return None
    return dict(id=rule['id'], level=rule['level'], swap=False,
                grade=rule.get('grade'),
                first_lifts=[l for p in rule['patterns'] for l in a.get(p, ())],
                then_lifts=[l for p in rule['patterns'] for l in b.get(p, ())])


def swap_lifts(report):
    """[(code, lift name, stressor key)] the draft may lighten: the
    non-anchor lifts of the overlaps on a swapping stressor. Grip and the
    lower-body back-to-back fact are never listed."""
    out = []
    for pair in report['pairs']:
        for shared in pair['shared']:
            if not shared.get('swap', True):
                continue
            for code, lifts in ((pair['first'], shared['first_lifts']),
                                (pair['then'], shared['then_lifts'])):
                out.extend((code, lift['name'], shared['stressor'])
                           for lift in lifts if not lift['anchor'])
    return out


def stacking(days, facts, rules=None):
    """[{session, rule, lifts}] same-session stacks (rules
    fatigue_overlap.stacking): a heavy-class lift with another also-class
    lift in one session."""
    spec = rules_spec(rules)
    out = []
    for code, items in days.items():
        fs = [(ex['name'], facts(ex['name']) or {}) for ex in items or ()]
        for rule in spec.get('stacking', ()):
            heavy = [n for n, f in fs if _match(rule['heavy'], f)]
            if not heavy:
                continue
            also = [n for n, f in fs if n != heavy[0] and _match(rule['also'], f)]
            if also:
                out.append(dict(session=code, rule=rule['id'], lifts=[heavy[0]] + also))
    return out


def lighter_key(fact):
    """Sort key of a replacement: lower fatigue first."""
    return GRADE_RANK.get(fact.get('fatigue'), 1)
