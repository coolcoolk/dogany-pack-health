"""Goal/resource/constraint evaluation of weekly split shapes.

A split is judged by its STRUCTURE, never by an exercise draft (owner
2026-10-06 06:22): each session code carries regions / muscles / movement
patterns from the rules data (split_model.structure), and the facts are
scored over the plausible weeks the owner may train (split_model.week_set:
the declared days, and a main day slipping to a supplementary day). Exercise
choice happens after the split is picked. A shape whose session cannot hold
its required lifts inside the lift minutes is a failed shape.
"""
from types import SimpleNamespace

import caution_care
import compose_rank


def rules():
    return compose_rank.load_rules()['split_model']


def phase_of(cx, api):
    """cut | grow | maintain. The active goals' direction decides
    (program-plan goal_phase: a fat-down goal is a cut even with skeletal
    muscle linked); without one, the goal mode / strand words."""
    p = SimpleNamespace(**api)
    phase, _metric = p.goal_phase(cx.db)
    if phase:
        return phase
    ranked_profile = compose_rank.profile_from_context(cx, p.config_value, p._q)
    return rules()['phase_aliases'].get(ranked_profile['goal_mode'],
                                        'grow' if ranked_profile['size'] else 'maintain')


def input_model(cx, api):
    p = SimpleNamespace(**api)
    cfg = rules()
    phase = phase_of(cx, api)
    exp = cx.st.get('experience')
    exp = {'beginner': 'novice', 'first': 'novice', 'returning': 'returner'}.get(exp, exp) or 'novice'
    days = [d for d in p.UL.WEEKDAY_ORDER if d in cx.st['daytime']['weekdays']]
    timing = compose_rank.time_budget(cx, p._minutes)
    # the side word the user used (owner 2026-10-06 16:21: right = their own word, not the display layer's)
    name = api.get('user_site_name')
    sites = {it['site']: (name(cx, it) if name else p.UL.site_ko(it['site'], it.get('side')))
             for it in cx.st.get('safety_items', []) if it.get('site')}
    # the comparison names a site without its side ("knee", not "right knee")
    site_short = {s: p.UL.site_ko(s) for s in sites}
    # each site's care mode (caution_care, owner 2026-10-05 10:41): what the
    # user said decides which split facts the site scores; never one fixed
    # care for every site
    modes = (api['care_modes'](cx) if 'care_modes' in api else {})
    care = {s: list(modes.get(s) or []) for s in sites}
    profiles = api['care_profiles'](cx) if 'care_profiles' in api else {}
    intensity = {s: caution_care.intensity(profiles.get(s, dict(care=care[s]))) for s in sites}
    tissue = {s: (profiles.get(s) or {}).get('tissue') for s in sites}
    scored = {s: caution_care.scored_facts(profiles.get(s, dict(care=care[s])), cfg['care_facts']) for s in sites}
    weights = dict(cfg['weights'], **cfg['phase_weights'][phase])
    weights.update(cfg['experience_weights'].get(exp, {}))
    for fact in ('caution', 'adjacency'):
        if not any(f.get(fact) for f in scored.values()):
            weights[fact] = 0
    body = body_state(cx, api, sites, intensity)
    consecutive = [(d, p.UL.WEEKDAY_ORDER[(i+1) % len(p.UL.WEEKDAY_ORDER)])
                   for i,d in enumerate(p.UL.WEEKDAY_ORDER) if d in days
                   and p.UL.WEEKDAY_ORDER[(i+1) % len(p.UL.WEEKDAY_ORDER)] in days]
    return dict(goal=dict(phase=phase, frequency_floor=cfg['frequency_floor'][phase]),
                resources=dict(n=len(days), weekdays=days, back_to_back=consecutive, minutes=timing['minutes'],
                               extra=[d for d in p.UL.WEEKDAY_ORDER if d in (cx.st['daytime'].get('extra') or ())],
                               lift_minutes=timing['lift_minutes'], reserved=timing['reserved'], experience=exp,
                               training=timing['training'], care=compose_rank.care_minutes(),
                               chosen=cx.st.get('day_minutes'), strength=timing['strength']),
                constraints=dict(sites=sites, site_short=site_short, care=care, scored=scored, intensity=intensity,
                                 tissue=tissue,
                                 place=cx.st.get('place', {}), body=body),
                weights=weights)


def body_state(cx, api, sites, intensity):
    """{site: {level, pain, active}} (owner 2026-10-06 17:04): a site is
    ACTIVE only from the user's own word -- their care answer says it hurts
    now (split_model.body.active_levels) -- or a pain signal they logged
    (an open pain_event for the site observed within pain_days). A safety
    row's write date is when an agent wrote it down, not when the condition
    began: it never makes a site active. Prep-managed sites stay inactive."""
    cfg = rules()['body']
    pained = _pain_sites(cx, api, cfg['pain_days'])
    out = {}
    for site in sites:
        level = (intensity.get(site) or {}).get('level', caution_care.UNKNOWN)
        pain = site in pained
        out[site] = dict(level=level, pain=pain,
                         active=level in cfg['active_levels'] or pain)
    return out


def _pain_sites(cx, api, days):
    """The sites with an open, logged pain event (sensation pain, pain > 0)
    observed within `days` of today; empty without a kit db or the table
    (_q reads a missing table as no rows)."""
    import datetime
    q = api.get('_q')
    today = getattr(cx, 'today', None)
    if not (q and today and getattr(cx, 'db', None)):
        return set()
    since = (today - datetime.timedelta(days=days)).isoformat()
    rows = q(cx.db, "SELECT site FROM pain_event WHERE status='open' AND sensation='pain' "
                    "AND pain > 0 AND site IS NOT NULL AND substr(observed_at, 1, 10) >= ?", (since,))
    return {str(r[0]) for r in rows or ()}


def eligible(n):
    result = []
    for shape in rules()['catalog']:
        rotations = [r for r in shape['rotations'] if n % len(r) == 0]
        if rotations:
            result.append((shape['family'] + str(n), max(rotations, key=len)))
    return result


def week_set(model):
    """[(weekdays, weight, slip)] the plausible weeks (split_model.week_set,
    owner 2026-10-06 06:25): the declared main days first, then every week
    where one main day slips to one declared supplementary day. slip = the
    supplementary day trained instead (None for the declared week)."""
    res = model['resources']
    main = list(res['weekdays'])
    extra = [d for d in res.get('extra') or () if d not in main]
    slips = []
    for d in main:
        for e in extra:
            days = sorted(set(main) - {d} | {e}, key=WEEK.index)
            if all(days != w for w, _e in slips):
                slips.append((days, e))
    head = rules()['week_set']['declared_weight'] if slips else 1.0
    return ([(main, head, None)]
            + [(days, (1.0 - head) / len(slips), e) for days, e in slips])


def session_shape(code, model, api):
    """What session `code` carries, from rules data only (split_model
    structure): its major-region muscles, major regions, movement patterns,
    caution sites loaded and the prep drills the structure asks for."""
    p = SimpleNamespace(**api)
    cfg = rules()
    st = cfg['structure']
    rank_rules = compose_rank.load_rules()
    rule = lambda key, default=None: compose_rank.session_rule(rank_rules, key, code, default)  # noqa: E731
    patterns = list(st['session_patterns'].get(code, st['session_patterns'].get(day_type(code), [])))
    regions = set(rule('session_regions', []))
    muscles = {m for m, r in p.MUSCLE_REGION if r in regions} - set(rule('session_excluded_muscles', []))
    for pattern in patterns:
        muscles |= set((rule('session_pattern_muscle_exceptions', {}) or {}).get(pattern, []))
    major = {m for m, r in p.MUSCLE_REGION if r in cfg['major_regions']}
    roles = [st['pattern_roles'].get(x) or {} for x in patterns]
    # recovery also reads the muscles pattern_roles names outside the major
    # regions (the arms): they never add a region, only an overlap
    tracked = major | set().union(*(set(r.get('primary', ())) | set(r.get('secondary', ()))
                                    for r in st['pattern_roles'].values() if isinstance(r, dict)))
    base = muscles & major
    muscles &= tracked
    # a pattern loads its secondary movers whatever the session's direct
    # work excludes (owner 2026-10-06 10:16, Awesome Bliss arms: the front
    # day trains the biceps directly and the triceps under the presses; the
    # back day the reverse)
    muscles |= set().union(*(set(r.get('secondary', ())) for r in roles)) & tracked
    # the muscles the session moves as a PRIMARY mover (structure.
    # pattern_roles, owner 2026-10-06 09:06): only these make a recovery
    # overlap; a muscle its patterns load only as a secondary mover (the
    # glutes under a front-day squat) does not. A muscle none of its
    # patterns names is direct work: primary.
    named = set().union(*(set(r.get('primary', ())) | set(r.get('secondary', ())) for r in roles))
    primary = {m for m in muscles if m not in named or any(m in r.get('primary', ()) for r in roles)}
    halves = [st['stack_groups'][x] for x in patterns if x in st['stack_groups']]
    sites = {s for s in model['constraints']['sites']
             if set(st['site_patterns'].get(s, ())) & set(patterns)}
    lower = [x for x in patterns if x in st['lower_patterns']][:1]
    upper = [x for x in patterns if x not in st['lower_patterns']][:1]
    drills = []
    for x in lower + upper:
        drills += [k for k in rank_rules['prep_by_pattern'].get(x, []) if k not in drills]
    intensity = model['constraints'].get('intensity') or {}
    for s in model['constraints']['sites']:
        if s in sites and (intensity.get(s) or {}).get('prep', True):
            drills += [k for k in rank_rules['caution_policy']['site_prep'].get(s, []) if k not in drills]
    budget = rank_rules['budget']
    lift = (budget['compound_minutes'] * min(budget['set_levels']) / float(budget['base_sets'])
            + budget['transition_minutes'])
    return dict(code=code, patterns=patterns, muscles=muscles, primary=primary,
                stack=max([halves.count(h) for h in halves] or [0]),
                regions={r for m, r in p.MUSCLE_REGION if m in base} | (regions & set(cfg['major_regions'])),
                big=len({r for m, r in p.MUSCLE_REGION if m in base}), sites=sites, drills=drills,
                prep=len(drills) * budget['prep_minutes'] / float(budget['max_prep']),
                need=lift * len(rule('required_regions', [])),
                main=bool(rule('main_patterns', [])))


def week_facts(days, shapes, rotation, model):
    """The week-varying facts of one week: the i-th training day carries the
    rotation's i-th session (sessions rotate, whatever the weekday)."""
    week = [None] * len(WEEK)
    for i, d in enumerate(days):
        week[WEEK.index(d)] = shapes[rotation[i % len(rotation)]]
    n = len(WEEK)
    nxt = lambda i: (i + 1) % n  # noqa: E731
    # recovery reads the primary movers only (structure.pattern_roles)
    pairs = [i for i in range(n) if week[i] and week[nxt(i)] and week[i]['primary'] & week[nxt(i)]['primary']]
    gaps = []
    for m in set().union(*(s['primary'] for s in week if s)):
        on = [i for i in range(n) if week[i] and m in week[i]['primary']]
        gaps += [((on[(k + 1) % len(on)] - i - 1) % n) if len(on) > 1 else n - 1 for k, i in enumerate(on)]
    site_on = {s: [bool(x and s in x['sites']) for x in week] for s in model['constraints']['sites']}
    shared = sorted(set().union(*(week[i]['primary'] & week[nxt(i)]['primary'] for i in pairs)))
    # consecutive days sharing a muscle only through a secondary mover:
    # recorded, not scored
    secondary = sorted(set().union(*((week[i]['muscles'] & week[nxt(i)]['muscles'])
                                     - (week[i]['primary'] & week[nxt(i)]['primary'])
                                     for i in range(n) if week[i] and week[nxt(i)])))
    return dict(back_to_back=len(pairs), rest_gap=min(gaps, default=n - 1), shared=shared,
                shared_secondary=secondary,
                site_days={s: sum(v) for s, v in site_on.items()},
                site_adjacency={s: sum(v[i] and v[nxt(i)] for i in range(n)) for s, v in site_on.items()},
                site_week=site_on)


SPREAD = ('back_to_back', 'rest_gap')


def measure(rotation, model, api):
    """The split's facts from its STRUCTURE (owner 2026-10-06 06:22): each
    session code's regions / muscles / patterns (rules data), scored over
    the plausible weeks (week_set). No exercise draft is composed. Raises
    Refused when a session cannot hold its required lifts inside the lift
    minutes (a failed shape, as before)."""
    cfg = rules()
    shapes = {c: session_shape(c, model, api) for c in rotation}
    lift_minutes = model['resources']['lift_minutes']
    short = [c for c, s in shapes.items() if s['need'] > lift_minutes]
    if short:
        raise api['Refused']('E-COMPOSE\tsplit\t%s needs %d lift minutes, %d available'
                             % (short[0], shapes[short[0]]['need'], lift_minutes))
    n = model['resources']['n']
    sessions = [shapes[rotation[i % len(rotation)]] for i in range(n)]
    frequency = {r: sum(r in s['regions'] for s in sessions) for r in cfg['major_regions']}
    weeks = [(days, w, slip, week_facts(days, shapes, rotation, model)) for days, w, slip in week_set(model)]
    cap = cfg['rest_gap_cap']
    mean = lambda f: round(sum(w * f(x) for _d, w, _s, x in weeks), 3)  # noqa: E731
    declared = weeks[0][3]

    def spread(get, better):
        """{typical, worst, slip}: the declared week's value, the worst
        week's, and the supplementary days the worst weeks slip to."""
        worst = (min if better == 'high' else max)(get(x) for _d, _w, _s, x in weeks)
        return dict(typical=get(declared), worst=worst,
                    slip=sorted({s for _d, _w, s, x in weeks if s and get(x) == worst and worst != get(declared)},
                                key=WEEK.index))
    sites = model['constraints']['sites']
    misfit = sorted({s for _d, _w, s, x in weeks if s and x['back_to_back'] > declared['back_to_back']},
                    key=WEEK.index)
    scored = model['constraints'].get('scored') or {}
    unknown = caution_care.facts_for([], cfg['care_facts'])
    factor = lambda s, fact: (scored.get(s, unknown)).get(fact, 0)  # noqa: E731
    site_days = {s: mean(lambda x, s=s: x['site_days'][s]) for s in sites}
    site_adjacency = {s: mean(lambda x, s=s: x['site_adjacency'][s]) for s in sites}
    prep = [s['prep'] for s in sessions]
    work = rules()['structure'].get('site_work') or {}
    site_work = {}
    for site in sites:
        pats = set((work.get(site) or {}).get('patterns', ()))
        per_day = [len(pats & set(x['patterns'])) for x in sessions]
        site_work[site] = dict(days=sum(1 for c in per_day if c), stack=max(per_day or [0]),
                               measure=(work.get(site) or {}).get('measure', 'days'))
    facts = dict(site_work=site_work, frequency=min(frequency.values()), per_region=frequency,
                 back_to_back=mean(lambda x: x['back_to_back']),
                 rest_gap=mean(lambda x: min(x['rest_gap'], cap)),
                 prep_minutes=round(sum(prep) / len(prep), 2),
                 session_prep=[round(x, 2) for x in prep],
                 stacking=round(sum(s['stack'] for s in sessions) / float(len(sessions)), 2),
                 big_regions=round(sum(s['big'] for s in sessions) / float(len(sessions)), 2),
                 supp_misfit=len(misfit), supp_misfit_days=misfit,
                 skill=sum(shapes[c]['main'] for c in rotation),
                 site_days=site_days, site_adjacency=site_adjacency,
                 caution=sum(v * factor(s, 'caution') for s, v in site_days.items()),
                 adjacency=sum(v * factor(s, 'adjacency') for s, v in site_adjacency.items()),
                 declared_adjacency=sum(v * factor(s, 'adjacency') for s, v in declared['site_adjacency'].items()),
                 site_week={s: v for s, v in declared['site_week'].items()},
                 session_minutes=[model['resources']['minutes']] * n,
                 training_minutes=[model['resources']['training']] * n,
                 weeks=[dict(weekdays=d, weight=round(w, 4), slip=s,
                             **{k: x[k] for k in SPREAD + ('shared', 'shared_secondary', 'site_days', 'site_adjacency')})
                        for d, w, s, x in weeks])
    facts['spread'] = dict({k: spread(lambda x, k=k: x[k], 'high' if k == 'rest_gap' else 'low') for k in SPREAD},
                           **{'%s:%s' % (k, s): spread(lambda x, k=k, s=s: x[k][s], 'low')
                              for k in ('site_days', 'site_adjacency') for s in sites})
    return facts


def uses_site(c, site, rank_rules):
    """True when lift c (a preview row) uses the safety site's joint: it
    works the site's muscles (primary or secondary; a stabilizer role is not
    using the joint) and either loads it (a loaded grade), is the rules'
    safer variant for the site (knee_precedents), or was put in place of a
    lift that loads it (for_site). A lateral raise or rear-delt row graded
    low for the shoulder, or a crunch swapped for a leg raise, does not."""
    # a standing lift loads the planted foot by its pattern (caution_policy
    # pattern_sites: plantar / calf / hamstring)
    if c.get('pattern') in rank_rules['caution_policy'].get('pattern_sites', {}).get(site, ()):
        return True
    worked = set(c.get('primary', [])) | set(c.get('secondary', []))
    if not worked & set(rank_rules['site_muscles'].get(site, [])):
        return False
    if compose_rank.safety_load(c, [site], rank_rules) in rules()['loaded_grades']:
        return True
    if site == 'knee' and c.get('name') in rank_rules.get('knee_precedents', {}):
        return True
    return c.get('for_site') == site


def fact_value(d, facts, model):
    """Comparable (scored) value of one dimension: the weighted mean over
    the week set for a week-varying fact; frequency saturates at the goal
    floor."""
    if d == 'frequency':
        return min(facts['frequency'],
                   model['goal']['frequency_floor'] * rules()['frequency_reward_cap_multiplier'])
    return facts.get(d, 0)


def evaluate(facts, model):
    floor = model['goal']['frequency_floor']
    violations = []
    if facts['frequency'] < floor:
        violations.append('frequency')
    # a care site's back-to-back loaded days in the DECLARED week are a
    # violation; a slip week's are scored, not forbidden
    if facts.get('declared_adjacency', facts.get('adjacency')):
        violations.append('adjacency')
    # the bigger the better: frequency (to the floor) and the rest gap;
    # every other fact is a cost
    utilities = {k: fact_value(k, facts, model) * (1 if k in ('frequency', 'rest_gap') else -1)
                 for k in model['weights']}
    score = sum(model['weights'][k] * v for k, v in utilities.items())
    return dict(violations=violations, score=score, utilities=utilities)


def options(cx, api):
    model = input_model(cx, api)
    options = []
    signatures = set()
    full_body_ok = model['resources']['experience'] in rules()['full_body_experience']
    for key, rot in eligible(model['resources']['n']):
        # Full-body is not a way of DIVIDING the week; it is offered only to
        # novices / returners (owner 2026-09-28 07:57).
        if key.startswith('fb') and not full_body_ok:
            continue
        signature = tuple(tuple(compose_rank.session_rule(compose_rank.load_rules(), 'session_regions', rot[i % len(rot)], []))
                          for i in range(model['resources']['n']))
        if signature in signatures:
            continue
        signatures.add(signature)
        option = dict(rotation=rot, n=model['resources']['n'], weekdays=model['resources']['weekdays'], model=model)
        try:
            facts = measure(rot, model, api)
            option.update(facts=facts, **evaluate(facts, model))
        except api['Refused'] as exc:
            # A session that cannot hold its required lifts inside the lift
            # minutes is a failed shape: a visible conflict, never
            # fabricated facts.
            option.update(facts=None, violations=['composition'], score=0, utilities={}, error=str(exc))
        options.append((key, option))
    options.sort(key=lambda pair: (bool(pair[1]['violations']), pair[1]['facts'] is None,
                                   -pair[1]['score'], (pair[1]['facts'] or {}).get('caution', 0), pair[0]))
    # Every buildable shape is offered (owner 2026-10-01): a shape scored
    # below another still divides the week differently. Only a failed
    # shape is dropped.
    shown = drop_failed(options)
    model['dropped'] = len(options) - len(shown)
    options = shown
    model['current'] = current_family(cx, api)
    cx.st['split_model'] = model
    menu = shown_order(options[:rules()['menu_size']], model)
    menu = body_first(menu, model)
    return menu, 'model' if menu and not menu[0][1]['violations'] else 'conflict'


def drop_failed(options):
    """An option whose composition failed is not offered while at least two
    composable options remain; with one left, only it is offered (the menu
    says so plainly); with none, the shapes stay so the owner still sees the
    days."""
    return [pair for pair in options if pair[1]['facts']] or options


# -- the split screen (owner 2026-10-06 17:02, approved by sample) ----------
# Each option is ONE blockquote: "**N. name**" (+ the rec mark), the
# "[day] session" line, bullets carrying only the items that differ across
# the options (the caution-site groups first, then the other measured
# items; an item where one option alone differs goes only in its block),
# then the bundle sentence. No folded stats block, no separate caution
# section: the recommendation footer and the question follow the blocks
# (split_model.compare). A week-varying item says the declared week's value
# and, only when a slip week is worse, the bad case with the day it slips
# to (owner 2026-10-06 06:25).
WEEK = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')


def family(key):
    return str(key or '').rstrip('0123456789')


def day_type(code):
    """The session name without its A/B variant letter."""
    code = str(code)
    return code[:-1] if len(code) > 1 and code[-1] in 'ABCD' else code


def _days(option):
    """[(weekday, day type)] in week order."""
    rot = option['rotation']
    return [(d, day_type(rot[i % len(rot)])) for i, d in enumerate(option['weekdays'])]


def title(key, api):
    """The menu title, no count: the card's count line carries it."""
    k = 'sm_t_' + family(key)
    return api['T'](k) if k in api['COPY'] else api['T']('sm_t_record')


def _sites(model):
    return model['constraints'].get('site_short') or model['constraints']['sites']


def _built(options):
    return [o for _k, o in options if o['facts']]


def option_lines(options, model, api):
    """{key: [line, ...]}: the schedule line, the option's bullets (only
    what differs), then the bundle sentence last. Unquoted: the caller
    quotes the block under the title."""
    t = api['T']
    bullets = option_bullets(options, model, api)
    out = {}
    for key, option in options:
        lines = [t('sm_schedule_sep').join(t('sm_schedule_day', day=api['UL'].WEEKDAY_KO[d], name=n)
                                            for d, n in _days(option))]
        lines += bullets.get(key, [])
        lines.append(bundle_line(option, api))
        out[key] = lines
    return out


def _differ(values):
    """{key} the options whose value is said: none when all are equal; the
    odd one alone when every other option shares one value (three or more
    options); else every option."""
    keys = list(values)
    if len(set(values.values())) < 2:
        return set()
    if len(keys) >= 3:
        for k in keys:
            rest = {values[o] for o in keys if o != k}
            if len(rest) == 1 and values[k] not in rest:
                return {k}
    return set(keys)


def _meets(option, model):
    return option['facts']['frequency'] >= model['goal']['frequency_floor']


def option_bullets(options, model, api):
    """{key: [bullet, ...]} (owner 2026-10-06 17:02): the caution-site
    groups over every built option (loaded days a week; for a stacked site
    also the big lifts on one day), then -- among the options meeting the
    goal floor as the first does -- the other measured items that differ;
    an option short of the floor says so in its own block instead."""
    t = api['T']
    names = _sites(model)
    built = [(k, o) for k, o in options if o['facts']]
    out = {k: [] for k, _o in options}
    if len(built) < 2:
        return out
    for measure, sites in site_groups(options, model):
        label = t('sm_site_sep').join(names[s] for s in sites)
        site = sites[0]
        vals = {k: _site_value(o, site) for k, o in built}
        said = _differ(vals)
        stacks = [_work(o, site)['stack'] for _k, o in built]
        for k, o in built:
            if k not in said:
                continue
            w = _work(o, site)
            if measure == 'days':
                text = t('sm_cv_site_days', n=w['days'])
            else:
                how = ('more' if w['stack'] == max(stacks) else 'less')
                text = t('sm_site_stack', n=w['days'], k=w['stack'], how=t('sm_stack_' + how))
            out[k].append(t('sm_line', label=label, text=text))
    first = built[0][1]
    peers = [(k, o) for k, o in built if _meets(o, model) == _meets(first, model)]
    items = [(it, s) for it, s in _items(model)
             if it['fact'] not in ('frequency', 'site_days') and not it.get('bundle') and not it.get('neutral')]
    # a site item (adjacency) reads with the caution bullets, ahead of the rest
    items.sort(key=lambda pair: pair[1] is None)
    if len(peers) >= 2:
        for item, site in items:
            vals = {k: _shown(item, site, model, api, o) for k, o in peers}
            for k in _differ(vals):
                out[k].append(t('sm_line', label=_label(item, site, model, api), text=vals[k]))
    if _meets(first, model):
        goal = t('sm_short_' + model['goal']['phase'])
        for k, o in built:
            if not _meets(o, model):
                out[k].append(t('sm_bullet', text=t('sm_rec_short', n=o['facts']['frequency'], goal=goal)))
    return out


# -- what a day bundles and what rests (owner 2026-10-06 16:05) ------------
def _day_patterns(option):
    """[(day type, [pattern, ...])] in rotation order, from the structure."""
    st = rules()['structure']['session_patterns']
    out = {}
    for code in option['rotation']:
        kind = day_type(code)
        pats = out.setdefault(kind, [])
        for x in st.get(code, st.get(kind, [])):
            if x not in pats:
                pats.append(x)
    return list(out.items())


def _pattern_words(patterns, api):
    words = rules()['structure']['pattern_words']
    groups = list(dict.fromkeys(words[x] for x in patterns if x in words))
    for pair, whole in ((('push', 'pull'), 'upper_all'), (('squat', 'hinge'), 'lower_all')):
        if set(pair) <= set(groups):
            groups = [whole if g == pair[0] else g for g in groups if g != pair[1]]
    return api['T']('sm_pat_sep').join(api['T']('sm_pat_' + g) for g in groups) or api['T']('sm_pat_none')


def bundle_line(option, api):
    """ONE line: what each day bundles and what rests, from the structure
    (session_patterns, stack_groups): one half a day -> the other half rests
    a whole day; both halves every day -> nothing rests whole, the load is
    spread; more than two single-half days -> one part a day, the parts
    wait their turn."""
    t = api['T']
    halves = rules()['structure']['stack_groups']
    days = _day_patterns(option)
    sides = [{halves[x] for x in pats if x in halves} for _k, pats in days]
    if all(len(h) == 2 for h in sides):
        rest = 'spread'
    elif len(days) <= 2:
        rest = 'half'
    else:
        rest = 'parts'
    what = (t('sm_bundle_parts') if rest == 'parts' else
            t('sm_bundle_sep').join(t('sm_bundle_day', name=k, what=_pattern_words(pats, api))
                                    for k, pats in days))
    return t('sm_bundle', days=what, rest=t('sm_rest_' + rest))


# -- what each split means for THIS user's caution sites ----------------------
def _work(option, site):
    return ((option.get('facts') or {}).get('site_work') or {}).get(site)


def _site_value(option, site):
    w = _work(option, site)
    if not w:
        return None
    return w['days'] if w['measure'] == 'days' else (w['stack'], w['days'])


def site_groups(options, model):
    """[(measure, [site, ...])]: the user's caution sites, those the options
    load the same way said together (knee and plantar: the same days)."""
    built = _built(options)
    out = []
    for site in _sites(model):
        if not built or any(_work(o, site) is None for o in built):
            continue
        sig = (_work(built[0], site)['measure'], tuple(_site_value(o, site) for o in built))
        for g in out:
            if g[0] == sig:
                g[1].append(site)
                break
        else:
            out.append((sig, [site]))
    return [(sig[0], sites) for sig, sites in out]


def _vote_value(option, site, spread):
    """What an active site wants less of: on a spread rung (kimwog 056
    spread_load) its back-to-back loaded days in the declared week, then
    the most of its work one day stacks -- exposure days are not cut; on
    any other rung its site_work measure (fewer loaded days, or less
    stacked on one day)."""
    if not spread:
        return _site_value(option, site)
    w = _work(option, site)
    sp = ((option.get('facts') or {}).get('spread') or {}).get('site_adjacency:' + site)
    if not w or sp is None:
        return None
    return (sp['typical'], w['stack'])


def body_pick(options, model):
    """The option the user's ACTIVE caution sites favour (owner 2026-10-06
    16:05), or None: each active site votes by its site_work measure (fewer
    loaded days, or less stacked on one day); a site that does not separate
    the candidates abstains; disagreeing votes decide nothing. Candidates:
    the built options meeting the goal floor as the first option meets it;
    the pick itself must hold every limit (no violation)."""
    body = model['constraints'].get('body') or {}
    active = [s for s in model['constraints']['sites'] if (body.get(s) or {}).get('active')]
    built = [(k, o) for k, o in options if o['facts']]
    if not active or len(built) < 2 or built[0][1]['violations']:
        return None
    floor = model['goal']['frequency_floor']
    meets = lambda o: o['facts']['frequency'] >= floor  # noqa: E731
    first = built[0][1]
    cands = [(k, o) for k, o in built if meets(o) == meets(first)]
    if len(cands) < 2:
        return None

    rows = model['constraints'].get('intensity') or {}

    def best(site):
        vals = [(_vote_value(o, site, (rows.get(site) or {}).get('spread')), k) for k, o in cands]
        if any(v is None for v, _k in vals):
            return None
        low = min(v for v, _k in vals)
        keys = [k for v, k in vals if v == low]
        return keys[0] if len(keys) == 1 else None
    votes = {s: best(s) for s in active}
    picks = {k for k in votes.values() if k}
    if len(picks) != 1:
        return None
    key = picks.pop()
    if dict(cands)[key]['violations']:
        return None
    deciding = [s for s in active if votes[s] == key]
    over = [s for s in model['constraints']['sites'] if s not in active and best(s) not in (None, key)]
    return dict(key=key, sites=deciding, over=over)


def body_first(menu, model):
    """The body-state pick leads the menu (it carries the rec mark)."""
    pick = body_pick(menu, model)
    model['body_pick'] = pick
    if not pick:
        return menu
    return ([pair for pair in menu if pair[0] == pick['key']]
            + [pair for pair in menu if pair[0] != pick['key']])


def _body_reason(i, key, option, model, api):
    """'Pick: N. <site> hurts now, so the split that uses <sites> only two
    days a week is better' -- the body reason in plain speech (owner
    2026-10-06 17:04), never a score."""
    t = api['T']
    pick = model['body_pick']
    names = _sites(model)
    body = model['constraints'].get('body') or {}
    site = pick['sites'][0]
    active = t('sm_site_sep').join(names[s] for s in pick['sites'])
    levels = [(body.get(s) or {}).get('level') for s in pick['sites']]
    rows = model['constraints'].get('intensity') or {}
    spread = bool((rows.get(site) or {}).get('spread'))
    # the rung in plain speech (kimwog 056): a loadable tendon / fascia ache,
    # a site closed for triage, else what the user logged
    level = next((lv for lv in levels if lv and _has(api, 'sm_body_why_' + lv.replace('-', '_'))), None)
    if spread:
        # the rung speaks of the tissue the user named (the plantar fascia)
        active = t('sm_site_sep').join(_tissue_name(model, s, api) for s in pick['sites'])
    why = t('sm_body_why_' + level.replace('-', '_') if level else 'sm_body_why_pain',
            site=active, i=api['josa'](active, 'i'), eun=api['josa'](active, 'eun'))
    group = next((g for _m, g in site_groups([(key, option)] + [
        (k, o) for k, o in model.get('_shown', [])], model) if site in g), [site])
    sites = t('sm_site_sep').join(names[s] for s in sorted(group, key=list(names).index))
    w = _work(option, site)
    tt = title(key, api)
    apart = spread and not ((option['facts'].get('spread') or {}).get('site_adjacency:' + site) or {}).get('typical')
    out = t('sm_body_rec_spread' if apart else 'sm_body_rec_' + w['measure'],
            i=i, why=why, sites=sites, k=w['stack'],
            days=t('sm_days_word_%d' % w['days']), reul=api['josa'](sites, 'reul'),
            title=tt, title_i=api['josa'](tt, 'i'))
    if pick['over']:
        over = t('sm_site_sep').join(names[s] for s in pick['over'])
        out += t('sm_body_over', sites=over, eun=api['josa'](over, 'eun'))
    return out


def _tissue_name(model, site, api):
    """The site said as the tissue the user named when the copy has a word
    for it (plantar + fascia: the plantar fascia); else the short site."""
    key = 'sm_tissue_' + str(model['constraints'].get('tissue', {}).get(site)) + '_' + site
    return api['T'](key) if _has(api, key) else _sites(model)[site]


def _has(api, key):
    return key in api['COPY'] or key in api.get('I18N_KEYS', ())


def prep_sites(model):
    """The sites whose care is only prep: the split does not touch them
    (compose's caution prep drills carry it)."""
    care = model['constraints'].get('care') or {}
    return [s for s in _sites(model) if care.get(s) and set(care[s]) == {'prep'}]


def care_text(model, api):
    """One plain-language level sentence per group; one pain handoff."""
    rows = model['constraints'].get('intensity')
    if rows is None:
        sites = prep_sites(model)
        if not sites:
            return ''
        names = api['T']('sm_site_sep').join(_sites(model)[s] for s in sites)
        return api['T']('sm_care_prep', sites=names, eun=api['josa'](names, 'eun'))
    groups = {}
    for site, row in rows.items():
        groups.setdefault((row['level'], tuple(row['care'])), []).append(site)
    out = ''
    for (level, care), sites in groups.items():
        # a spread rung speaks of the tissue the user named (the plantar fascia)
        spread = rows[sites[0]].get('spread') and level.startswith('current')
        names = api['T']('sm_site_sep').join(_tissue_name(model, s, api) if spread else _sites(model)[s]
                                             for s in sites)
        # each method is its own short sentence (one idea per sentence)
        method = '. '.join(api['T']('care_method_' + m) for m in care)
        out += api['T']('sm_care_' + level.replace('-', '_'), sites=names,
                        eun=api['josa'](names, 'eun'), method=method)
    if any(row['triage'] for row in rows.values()):
        out += api['T']('care_pain_triage')
    return out


def _items(model):
    """[(item, site)] the comparison can show, in the rules' order: a site
    item only for the sites whose care mode scores that fact; a
    scored_only item only while it carries weight (main lifts to learn:
    novices / returners, owner 2026-10-06)."""
    scored = model['constraints'].get('scored') or {}
    out = []
    for item in rules()['compare']['items']:
        if item.get('scored_only') and not model['weights'].get(item['fact']):
            continue
        per = item.get('per_site')
        if not per:
            out.append((item, None))
            continue
        out += [(item, s) for s in _sites(model) if (scored.get(s) or {}).get(per)]
    return out


def _value(option, item, site):
    """The scored value (a week-varying fact: its weighted mean)."""
    v = option['facts'].get(item['fact'])
    if site is not None:
        v = (v or {}).get(site, 0)
    return v or 0


def _spread(option, item, site):
    """{typical, worst, slip} of a week-varying item; None for a fixed one
    (or for facts measured without a week set)."""
    if not item.get('spread'):
        return None
    key = item['fact'] if site is None else '%s:%s' % (item['fact'], site)
    return (option['facts'].get('spread') or {}).get(key)


def _typical(option, item, site):
    """The value the screen says: the declared week's for a week-varying
    item; prep minutes in whole minutes."""
    sp = _spread(option, item, site)
    v = sp['typical'] if sp else _value(option, item, site)
    return int(v + 0.5) if item['fact'] == 'prep_minutes' else v


def _weight(model, item, site):
    """The score weight one unit of the item carries (split_model weights,
    times the site's care factor for a site item)."""
    if site is not None:
        per = item['per_site']
        return model['weights'].get(per, 0) * (model['constraints']['scored'][site].get(per, 0))
    return model['weights'].get(item['fact'], 0)


def _utility(model, item, site, option):
    v = _value(option, item, site)
    if item['fact'] == 'frequency':
        v = min(v, model['goal']['frequency_floor'])
    return v if item['better'] == 'high' else -v


def _label(item, site, model, api):
    k = item['fact']
    return api['T']('sm_cl_' + k, site=_sites(model).get(site, '') if site else '')


def _cv(api, fact, n):
    key = 'sm_cv_%s_%s' % (fact, n)
    return api['T'](key if fact == 'rest_gap' and n == 0 else 'sm_cv_' + fact, n=_fmt(n))


def _slip_days(api, days):
    return api['T']('sm_site_sep').join(api['UL'].WEEKDAY_KO[d] for d in days)


def _shown(item, site, model, api, option):
    """The value line: the declared week's value, plus the bad case and
    the supplementary day it slips to only when a slip week is worse
    (owner 2026-10-06 06:25)."""
    fact = item['fact']
    if fact == 'supp_misfit':
        days = option['facts'].get('supp_misfit_days') or []
        return (api['T']('sm_cv_supp_misfit', days=_slip_days(api, days)) if days
                else api['T']('sm_cv_supp_misfit_0'))
    text = _cv(api, fact, _typical(option, item, site))
    sp = _spread(option, item, site)
    if sp and sp['worst'] != sp['typical'] and sp['slip']:
        text = api['T']('sm_cv_slip', typical=text, days=_slip_days(api, sp['slip']),
                        worst=_cv(api, fact, sp['worst']))
    return text


def _fmt(v):
    return int(v) if float(v).is_integer() else round(v, 1)


def comparison(options, source, api):
    """The lines after the option blocks: the recommendation footer, or the
    plain no-pick line when no option holds every limit. With fewer than two
    built options: the plain recommendation sentence only. What the options
    measure lives in their own blocks (option_bullets)."""
    t = api['T']
    built = [(i, k, o) for i, (k, o) in enumerate(options, 1) if o['facts']]
    if len(built) < 2:
        return [recommendation(options, source, api)]
    if source != 'model':
        return [t('sm_no_rec')]
    return [_footer(built, options[0][1]['model'], api)]


def _contrib(model, a, b):
    """[(share, item, site, diff)] how much each shown item moves the score
    from option b to option a (positive = a wins it), largest first. A
    neutral item (descriptive only) moves nothing."""
    out = []
    for item, site in _items(model) + [(x, None) for x in rules()['compare'].get('hidden', [])]:
        if item.get('fact') not in a['facts'] or item.get('per_site') and site is None or item.get('neutral'):
            continue
        ua, ub = _utility(model, item, site, a), _utility(model, item, site, b)
        share = _weight(model, item, site) * (ua - ub)
        if share:
            out.append((share, item, site, abs(_typical(a, item, site) - _typical(b, item, site))))
    out.sort(key=lambda x: -x[0])
    return out


def _reasons(parts, model, api):
    """'A and B' from [(item, site, diff)]: the item clauses joined."""
    t = api['T']
    out = []
    for n, (item, site, diff) in enumerate(parts):
        name = _sites(model).get(site, '') if site else ''
        end = 'end' if n == len(parts) - 1 else 'and'
        out.append(t('sm_cr_%s_%s' % (item['fact'], end), site=name, d=_fmt(diff),
                     reul=api['josa'](name, 'reul') if name else ''))
    return t('sm_clause_sep_and').join(out)


def _deciding(wins, lost, cap):
    """[(item, site, diff)] the winning items that carry the decision
    (owner: a near-tie names the one item that separated them, never an
    item that did not matter): each item whose share alone outweighs what
    the pick loses to the rival (`lost`); when none does, the largest
    shares until their sum does."""
    alone = [(item, site, diff) for share, item, site, diff in wins if share > lost]
    if alone:
        return alone[:cap]
    out, total = [], 0
    for share, item, site, diff in wins[:cap]:
        out.append((item, site, diff))
        total += share
        if total > lost:
            break
    return out


def _footer(built, model, api):
    """The "rec" footer line: the pick and the measured items that separated it
    from the next option (never the listing order), in plain speech; when
    the candidates train each region equally often that comes first (and,
    when only `minor` items separate them, that there is no big difference).
    A recorded current split is said as the reason it is. An option short of
    the floor says so in its own block, not here."""
    t = api['T']
    floor = model['goal']['frequency_floor']
    top_i, top_k, top = built[0]
    meets = lambda o: o['facts']['frequency'] >= floor  # noqa: E731
    rivals = [(i, o) for i, _k, o in built[1:] if meets(o) == meets(top)]
    cap = rules()['compare'].get('reason_max', 2)
    pick = model.get('body_pick')
    if pick and pick['key'] == top_k and rivals:
        model['_shown'] = [(k, o) for _i, k, o in built]
        out = _body_reason(top_i, top_k, top, model, api)
        model.pop('_shown', None)
        return out
    if not rivals:
        return t('sm_cr_rec_floor', i=top_i, floor=floor)
    j, rival = rivals[0]
    shares = _contrib(model, top, rival)
    wins = _deciding([x for x in shares if x[0] > 0], -sum(x[0] for x in shares if x[0] < 0), cap)
    loses = [(it, s, d) for sh, it, s, d in reversed(shares) if sh < 0][:cap]
    if _is_current(top_k, model):
        out = t('sm_cr_rec_current', i=top_i)
        if loses:
            out += ' ' + t('sm_cr_rival', j=j, reasons=_reasons(loses, model, api))
        return out
    if not wins:
        return t('sm_cr_rec_same', i=top_i, j=j)
    freq = {o['facts']['frequency'] for _i, o in rivals} | {top['facts']['frequency']}
    if len(freq) > 1:
        return t('sm_cr_rec', i=top_i, j=j, reasons=_reasons(wins, model, api))
    n = len(rivals) + 1
    count = t('count_%d' % n) if ('count_%d' % n) in api['COPY'] else str(n)
    every = t('sm_cr_all_2') if n == 2 else t('sm_cr_all', count=count)
    minor = set(rules()['compare'].get('minor', ()))
    tt = title(top_k, api)
    return t('sm_cr_rec_tie_minor' if all(it['fact'] in minor for it, _s, _d in wins) else 'sm_cr_rec_tie',
             i=top_i, every=every, n=_fmt(top['facts']['frequency']), title=tt,
             title_i=api['josa'](tt, 'i'), reasons=_reasons(wins, model, api))


# The order the menu shows, in order (owner 2026-10-01 20:08): (1) how often
# each region comes back, up to the goal floor (more is not better past it);
# (2) among options equal on (1) the user's current split when one is
# recorded; (3) the model's score.
def _shown_key(option, model):
    """Lower is better; None for an option that could not be built."""
    if not option['facts']:
        return None
    floor = model['goal']['frequency_floor']
    return (-min(option['facts']['frequency'], floor),)


def current_family(cx, api):
    """The family of the split the user runs now, read from the record
    (the in-cycle session_type rows, with sessions logged inside the record
    window); None without one."""
    p = SimpleNamespace(**api)
    codes = p.practiced_rotation(cx.db)
    if not codes or not p.logged_rotation_sessions(cx.db, cx.today):
        return None
    types = {day_type(c) for c in codes}
    for shape in rules()['catalog']:
        if any({day_type(c) for c in rot} == types for rot in shape['rotations']):
            return shape['family']
    return None


def _is_current(key, model):
    return bool(model.get('current')) and family(key) == model['current']


def shown_order(options, model):
    """The menu ordered by the shown comparison (frequency vs the floor);
    among options equal on it the user's current split comes first, then
    the model's order. Options with a violation or no composition stay
    behind."""
    def key(pair):
        i, (k, o) = pair
        shown = _shown_key(o, model)
        return (bool(o['violations']), shown is None, shown or (), not _is_current(k, model), i)
    return [pair for _i, pair in sorted(enumerate(options), key=key)]


def recommendation(options, source, api):
    """The plain sentence when there is nothing to compare: no option built,
    no option holding every limit, or one option left."""
    t = api['T']
    built = [(i, o) for i, (_k, o) in enumerate(options, 1) if o['facts']]
    if not built:
        return t('sm_none_built')
    if source != 'model':
        return t('sm_no_rec')
    model = options[0][1]['model']
    sentences = []
    if model.get('dropped'):
        sentences.append(t('sm_only_built'))
    sentences.append(t('sm_rec_pick_n', i=built[0][0]))
    return ' '.join(sentences)
