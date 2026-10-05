"""Goal/resource/constraint evaluation of composed weekly shapes.

Preview uses the production names-only draft search, before prescription and
volume fitting, composed TO the time budget (the user's session minutes,
owner 2026-10-01): fewer sets per lift, then fewer lifts, never a longer day.
A shape that cannot be composed inside the budget is a failed composition.
"""
import copy
from types import SimpleNamespace

import compose_draft
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
    sites = {it['site']: p.UL.site_ko(it['site'], it.get('side'))
             for it in cx.st.get('safety_items', []) if it.get('site')}
    # the comparison names a site without its side ("knee", not "right knee")
    site_short = {s: p.UL.site_ko(s) for s in sites}
    weights = dict(cfg['weights'], **cfg['phase_weights'][phase])
    weights.update(cfg['experience_weights'].get(exp, {}))
    if not sites:
        weights.update(caution=0, adjacency=0)
    consecutive = [(d, p.UL.WEEKDAY_ORDER[(i+1) % len(p.UL.WEEKDAY_ORDER)])
                   for i,d in enumerate(p.UL.WEEKDAY_ORDER) if d in days
                   and p.UL.WEEKDAY_ORDER[(i+1) % len(p.UL.WEEKDAY_ORDER)] in days]
    return dict(goal=dict(phase=phase, frequency_floor=cfg['frequency_floor'][phase]),
                resources=dict(n=len(days), weekdays=days, back_to_back=consecutive, minutes=timing['minutes'],
                               lift_minutes=timing['lift_minutes'], reserved=timing['reserved'], experience=exp,
                               training=timing['training'], care=compose_rank.care_minutes(),
                               chosen=cx.st.get('day_minutes'), strength=timing['strength']),
                constraints=dict(sites=sites, site_short=site_short, place=cx.st.get('place', {})),
                weights=weights)


def eligible(n):
    result = []
    for shape in rules()['catalog']:
        rotations = [r for r in shape['rotations'] if n % len(r) == 0]
        if rotations:
            result.append((shape['family'] + str(n), max(rotations, key=len)))
    return result


def measure(cx, rotation, model, api, candidates):
    p = SimpleNamespace(**api)
    probe = copy.copy(cx)
    probe.st = copy.deepcopy(cx.st)
    probe.st['structure'] = dict(rotation=rotation)
    probe.st['days'] = dict(weekdays=model['resources']['weekdays'])
    # Composed to the budget: each set level in turn, never past the minutes.
    ranked, draft, sets = compose_rank.build_to_budget(
        probe, candidates, api, compose_draft.build, preview=True)
    cfg = rules()
    rank_rules = compose_rank.load_rules()
    week = [[] for _ in p.UL.WEEKDAY_ORDER]
    mains = set()
    costs = []
    for i, day in enumerate(model['resources']['weekdays']):
        code = rotation[i % len(rotation)]
        pool = {c['name']: c for slot in ranked['sessions'][code] for c in slot['shortlist']}
        main_names = {c['name'] for slot in ranked['sessions'][code] if slot['slot'] == 'main' for c in slot['shortlist']}
        main_name = next((e['name'] for e in draft['days'][code] if e['name'] in main_names), None)
        lifts = [dict(pool[e['name']], main=e['name'] == main_name, for_site=e.get('for_site'))
                 for e in draft['days'][code]]
        week[p.UL.WEEKDAY_ORDER.index(day)] = lifts
        mains.update(c['name'] for c in lifts if c['main'])
        costs.append(compose_rank.session_minutes(lifts, rank_rules, sets) + model['resources']['reserved'])
    frequency = {region: sum(any(region in {r for m, r in p.MUSCLE_REGION if m in c['primary']} for c in lifts) for lifts in week)
                 for region in cfg['major_regions']}
    heavy = [{c['pattern'] for c in lifts if c['fatigue'] in cfg['heavy_fatigue']} for lifts in week]
    # Recovery: major regions trained on two back-to-back calendar days.
    # Counted per PRIMARY MUSCLE, not per region: front/back splits exist to
    # put front delts / quads and rear delts / hamstrings on different days,
    # and a region-level count ("shoulders", "legs") erased exactly that.
    major = {m for m, r in p.MUSCLE_REGION if r in cfg['major_regions']}
    day_muscles = [{m for c in lifts for m in c['primary'] if m in major} for lifts in week]
    overlap = sum(len(day_muscles[i] & day_muscles[(i+1) % len(week)]) for i in range(len(week)))
    loaded = {site: [any((c['main'] or c['fatigue'] in cfg['heavy_fatigue']) and
                         compose_rank.safety_load(c, [site], rank_rules) in cfg['loaded_grades'] for c in lifts) for lifts in week]
              for site in model['constraints']['sites']}
    site_days = {s: sum(v) for s, v in loaded.items()}
    # What the split screen SHOWS (owner 2026-10-01): the days whose session
    # USES the joint -- a lift loading it, or a safer variant standing in for
    # one (it still loads the joint), so a safety swap never hides the day.
    # `loaded` above stays the scored burden (main / heavy lifts after the
    # swaps).
    use = {site: [any(uses_site(c, site, rank_rules) for c in lifts) for lifts in week]
           for site in model['constraints']['sites']}
    # What the split screen compares (owner 2026-10-01 20:08): per joint,
    # the days carrying loaded work and the days carrying only low-load
    # work, graded by the SAME safety_load table the safety swaps use
    # (joint_load).
    high = {site: [any(joint_load(c, site, rank_rules) == 'high' for c in lifts) for lifts in week]
            for site in model['constraints']['sites']}
    low = {site: [any(joint_load(c, site, rank_rules) == 'low' for c in lifts) for lifts in week]
           for site in model['constraints']['sites']}
    adjacent = {s: sum(v[i] and v[(i+1) % len(week)] for i in range(len(week))) for s, v in loaded.items()}
    facts = dict(frequency=min(frequency.values()), per_region=frequency,
                 session=max(costs), fits_window=max(costs) <= model['resources']['minutes'], session_minutes=costs, evenness=max(costs)-min(costs),
                 sets=sets, training_minutes=[c - model['resources']['care'] for c in costs],
                 caution=sum(site_days.values()), site_days=site_days, adjacency=sum(adjacent.values()), site_adjacency=adjacent,
                 heavy_lower=sum(bool(v & {'squat', 'hinge'}) for v in heavy),
                 leg_rest=sum(not any(set(c['primary']) & {m for m,r in p.MUSCLE_REGION if r == 'legs'} for c in lifts) for lifts in week),
                 squat=sum('squat' in v for v in heavy), hinge=sum('hinge' in v for v in heavy),
                 squat_hinge=sum('squat' in heavy[i] and 'hinge' in heavy[(i+1) % len(week)] for i in range(len(week))),
                 overlap=overlap, skill=len(mains), main_lifts=sorted(mains),
                 site_week={s: [bool(x) for x in v] for s, v in loaded.items()},
                 site_use={s: [bool(x) for x in v] for s, v in use.items()},
                 site_high=high, site_low=low)
    return facts, draft


def joint_load(c, site, rank_rules):
    """'high' | 'low' | None: how lift c (a preview row) loads the safety
    site's joint, read from compose_rank.safety_load -- the one grading the
    safety swaps use (owner 2026-10-01 20:08: one load source). A loaded
    grade (split_model.loaded_grades) is high, 'low' is low, 'none' is no
    work for the joint."""
    grade = compose_rank.safety_load(c, [site], rank_rules)
    if grade in rules()['loaded_grades']:
        return 'high'
    return 'low' if grade == 'low' else None


def uses_site(c, site, rank_rules):
    """True when lift c (a preview row) uses the safety site's joint: it
    works the site's muscles (primary or secondary; a stabilizer role is not
    using the joint) and either loads it (a loaded grade), is the rules'
    safer variant for the site (knee_precedents), or was put in place of a
    lift that loads it (for_site). A lateral raise or rear-delt row graded
    low for the shoulder, or a crunch swapped for a leg raise, does not."""
    worked = set(c.get('primary', [])) | set(c.get('secondary', []))
    if not worked & set(rank_rules['site_muscles'].get(site, [])):
        return False
    if compose_rank.safety_load(c, [site], rank_rules) in rules()['loaded_grades']:
        return True
    if site == 'knee' and c.get('name') in rank_rules.get('knee_precedents', {}):
        return True
    return c.get('for_site') == site


def fact_value(d, facts, model):
    """Comparable value of one dimension. Session minutes only count above
    the comfort line of the owner's window (session_comfort_ratio): two
    sessions that both sit well inside the window are not a real difference."""
    if d == 'session':
        line = rules().get('session_comfort_ratio', 1) * model['resources']['minutes']
        return max(0, facts['session'] - line)
    return facts[d]


def evaluate(facts, model):
    floor = model['goal']['frequency_floor']
    violations = []
    if facts['frequency'] < floor:
        violations.append('frequency')
    if facts['session'] > model['resources']['minutes']:
        violations.append('session')
    if facts['adjacency']:
        violations.append('adjacency')
    # Saturate frequency reward at the goal floor; extra visits alone must
    # not dominate time, learning, load and evenness in their measured units.
    utilities = {k: fact_value(k, facts, model) * (1 if k in ('frequency', 'leg_rest') else -1)
                 for k in model['weights']}
    utilities['frequency'] = min(facts['frequency'], floor * rules()['frequency_reward_cap_multiplier'])
    score = sum(model['weights'][k] * v for k, v in utilities.items())
    return dict(violations=violations, score=score, utilities=utilities)


def options(cx, api):
    model = input_model(cx, api)
    pool = api['candidates'](cx)
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
            facts, draft = measure(cx, rot, model, api, pool)
            option.update(facts=facts, preview=draft, **evaluate(facts, model))
        except api['Refused'] as exc:
            # Keep structural eligibility separate from composability. Failed
            # searches are visible conflicts, never fabricated load facts.
            option.update(facts=None, preview=None, violations=['composition'], score=0, utilities={}, error=str(exc))
        options.append((key, option))
    options.sort(key=lambda pair: (bool(pair[1]['violations']), pair[1]['facts'] is None,
                                   -pair[1]['score'], (pair[1]['facts'] or {}).get('caution', 0), pair[0]))
    # Every composable shape is offered (owner 2026-10-01): a shape scored
    # below another still divides the week differently. Only a failed
    # composition is dropped.
    shown = drop_failed(options)
    model['dropped'] = len(options) - len(shown)
    options = shown
    model['current'] = current_family(cx, api)
    cx.st['split_model'] = model
    menu = shown_order(options[:rules()['menu_size']], model)
    return menu, 'model' if menu and not menu[0][1]['violations'] else 'conflict'


def drop_failed(options):
    """An option whose composition failed is not offered while at least two
    composable options remain; with one left, only it is offered (the menu
    says so plainly); with none, the shapes stay so the owner still sees the
    days."""
    return [pair for pair in options if pair[1]['facts']] or options


# -- the comparison the owner reads (owner rehearsal 2026-10-01) ------------
# Every option is shown on the SAME lines so they compare: how often each
# region comes back and on which days each safety joint carries loaded or
# only low-load work (joint_load). No minutes line:
# every option is composed to the user's session minutes (owner 2026-10-01).
# Shared synergist muscles are not "the same region": overlap is scored,
# never shown.
# day names that need a gloss (the front / back days)
NAMED_DAYS = {'ab': 'sm_names_ab', 'supp': 'sm_names_ab'}


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


def _site_key(option, site):
    """What a site's load looks like on one option: the weekdays with
    loaded work, and whether it has low-load work at all."""
    n = len(WEEK)
    week = _week(option, site)
    return (tuple(bool(i < len(week) and week[i]) for i in range(n)),
            bool(site_days(option, site, 'low')))


def shared_sites(options, model):
    """{site: option} for the sites whose high-load days (and low-load
    presence) are identical on every built option, only when two or more
    options are compared: they are said once in the lead, not per option."""
    built = _built(options)
    if len(built) < 2:
        return {}
    return {s: built[0] for s in _sites(model)
            if len({_site_key(o, s) for o in built}) == 1}


def shown_sites(options, model):
    """The sites that differ across the built options (one fact line each)."""
    shared = shared_sites(options, model)
    return {s: n for s, n in _sites(model).items() if s not in shared}


def line_count(options, model):
    """How many comparison lines each option carries."""
    return 1 + len(shown_sites(options, model))


def shared_text(options, model, api):
    """The lead sentences for the sites that are the same on every option."""
    t = api['T']
    names = _sites(model)
    out = []
    for s, o in shared_sites(options, model).items():
        name = names[s]
        days = sum(site_days(o, s).values())
        if not days and site_days(o, s, 'low'):
            out.append(t('sm_shared_swap', site=name, eun=api['josa'](name, 'eun')))
        else:
            out.append(t('sm_shared_days', site=name, days=days))
    return ''.join(out)


def option_lines(options, model, api):
    """{key: [line, ...]}: the schedule line, the day-name gloss when the
    shape needs it, then the comparison lines (a site line only for a site
    that differs across the options; none for an option that could not be
    built)."""
    t = api['T']
    out = {}
    sites = shown_sites(options, model)
    for key, option in options:
        days = _days(option)
        lines = [t('sm_schedule_sep').join(t('sm_schedule_day', day=api['UL'].WEEKDAY_KO[d], name=n)
                                            for d, n in days)]
        if NAMED_DAYS.get(family(key)):
            lines.append(t(NAMED_DAYS[family(key)]))
        f = option['facts']
        if not f:
            out[key] = lines
            continue
        lines.append(t('sm_line', label=t('sm_l_frequency'),
                       text=t('sm_v_frequency', n=f['frequency'])))
        for site, name in sites.items():
            lines.append(t('sm_line', label=t('sm_l_site', site=name),
                           text=t('sm_v_days', days=sum(site_days(option, site).values()))))
        out[key] = lines
    return out


def _week(option, site, kind='high'):
    """The weekday flags (MON..SUN) of one site: 'high' = loaded work for
    the joint that day, 'low' = low-load work. A record
    without the load facts reads site_use / site_week as high."""
    facts = option['facts']
    week = (facts.get('site_' + kind) or {}).get(site)
    if week is None and kind == 'high':
        week = (facts.get('site_use') or facts.get('site_week') or {}).get(site)
    return week or []


WEEK = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')


def site_days(option, site, kind='high'):
    """{day type: days} with high- (or low-) load movements for the site's
    joint, in week order."""
    week = _week(option, site, kind)
    out = {}
    for d, name in _days(option):
        i = WEEK.index(d)
        if i < len(week) and week[i]:
            out[name] = out.get(name, 0) + 1
    return out


def _types(option):
    """The day types in week order, each once."""
    out = []
    for _d, name in _days(option):
        if name not in out:
            out.append(name)
    return out


def type_load(option, site):
    """{day type: 'high' | 'low' | None} for one site: 'high' when a day of
    the type carries loaded work for the joint, 'low' when its days carry
    only low-load work, None when no day of the type works the joint."""
    high, low = site_days(option, site), site_days(option, site, 'low')
    return {name: 'high' if name in high else 'low' if name in low else None
            for name in _types(option)}


def _split(option, site):
    """(loaded, light, rest) day types of one site, in week order."""
    load = type_load(option, site)
    return ([n for n, v in load.items() if v == 'high'],
            [n for n, v in load.items() if v == 'low'],
            [n for n, v in load.items() if v is None])


def light_types(option, model):
    """{site: [day types working the joint only with low-load movements]}."""
    return {s: _split(option, s)[1] for s in _sites(model)}


def resting_sites(option, model):
    """Sites whose days off the loaded ones carry NO work for the joint at
    all: loaded days, no light days, at least one day with nothing."""
    out = []
    for s in _sites(model):
        loaded, light, rest = _split(option, s)
        if loaded and not light and rest:
            out.append(s)
    return out


def rests_fully(option, model):
    """The gathering side of the trade-off: every joint has days with no
    work for it, and no joint is worked lightly on its days off the loaded
    ones -- the work is stacked and the other days are FULL rest."""
    sites = _sites(model)
    return bool(sites) and all(_split(option, s)[2] for s in sites) and not any(
        _split(option, s)[0] and _split(option, s)[1] for s in sites)


def spreads(option, model):
    """The spreading side of the trade-off: some joint carries loaded work
    on some days and only low-load work on others, and every training day
    works at least one joint -- the work runs through the week, lighter on
    some days."""
    if not any(_split(option, s)[0] and _split(option, s)[1] for s in _sites(model)):
        return False
    for d, _n in _days(option):
        i = WEEK.index(d)
        if not any(i < len(_week(option, s, k)) and _week(option, s, k)[i]
                   for s in _sites(model) for k in ('high', 'low')):
            return False
    return True


# The comparison the recommendation reads, in order (owner 2026-10-01
# 20:08): (1) how often each region comes back, up to the goal floor (more
# is not better past it). How the joint work is laid out is a trade-off,
# never a winner by itself: options equal on (1) are a tie, said with both
# sides; (2) a tie goes to the user's current split when one is recorded,
# else to the first listed option -- said plainly as such.
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
    """One plain paragraph comparing EVERY shown option from the shown
    facts only: the region frequency against the goal floor; for options
    equal on it, both sides of the joint-load trade-off and the honest
    tie-break; then the options short of the floor. No minutes talk (every
    option fits the chosen minutes). No pick when the best option still
    breaks a limit."""
    t = api['T']
    if not any(o['facts'] for _k, o in options):
        return t('sm_none_built')
    if source != 'model':
        return t('sm_no_rec')
    model = options[0][1]['model']
    floor = model['goal']['frequency_floor']
    built = [(i, k, o) for i, (k, o) in enumerate(options, 1) if o['facts']]
    sentences = []
    if model.get('dropped') and len(built) < 2:
        sentences.append(t('sm_only_built'))
    if len(built) == 1:
        sentences.append(t('sm_rec_pick_n', i=built[0][0]))
        return ' '.join(sentences)
    meets = [(i, o) for i, _k, o in built if o['facts']['frequency'] >= floor]
    short = [(i, o) for i, _k, o in built if o['facts']['frequency'] < floor]
    if len(meets) >= 2:
        freqs = {o['facts']['frequency'] for _i, o in meets}
        which = (t('sm_rec_all') if len(meets) == len(built) and len(built) > 2
                 else t('sm_rec_both', a=meets[0][0], b=meets[1][0]) if len(meets) == 2
                 else t('sm_rec_these', nums=_nums([i for i, _o in meets], t)))
        sentences.append(t('sm_rec_meet_same' if len(freqs) == 1 else 'sm_rec_meet_floor',
                           which=which, n=min(freqs), floor=floor))
    elif len(meets) == 1:
        sentences.append(t('sm_rec_meet_one', i=meets[0][0], n=meets[0][1]['facts']['frequency']))
    top_i, top_key, top = built[0]
    shown = _shown_key(top, model)
    rivals = [(i, o) for i, o in (meets if top in [x for _j, x in meets]
                                  else [(i, o) for i, _k, o in built])
              if o is not top]
    tied = [(i, o) for i, o in rivals if _shown_key(o, model) == shown]
    beaten = [i for i, o in rivals if _shown_key(o, model) > shown]
    if any(_shown_key(o, model) < shown for _i, o in rivals):
        # the model's order disagrees with the shown comparison
        sentences.append(t('sm_rec_score', i=top_i))
    elif beaten:
        sentences.append(t('sm_rec_top' if len(beaten) == len(rivals) else 'sm_rec_top_vs',
                           i=top_i, nums=_nums(beaten, t), text=t('sm_w_more_often')))
    if tied and not any(_shown_key(o, model) < shown for _i, o in rivals):
        trade = _trade_off([(top_i, top)] + tied, model, api)
        if trade:
            sentences.append(trade)
        if _is_current(top_key, model):
            sentences.append(t('sm_rec_pick_current', i=top_i))
        else:
            sentences.append(t('sm_rec_pick_first', i=top_i,
                               which=t('sm_rec_fit_two' if len(tied) == 1 else 'sm_rec_fit_all')))
        sentences += _short(short, model, t)
        return ' '.join(sentences)
    sentences += _short(short, model, t)
    sentences.append(t('sm_rec_pick_n', i=top_i))
    return ' '.join(sentences)


def _short(short, model, t):
    goal_short = t('sm_short_' + model['goal']['phase'])
    return [t('sm_rec_short', i=i, n=o['facts']['frequency'], goal=goal_short)
            for i, o in short]


def _nums(nums, t):
    return t('sm_num_sep').join(t('sm_num', i=i) for i in nums)


def _trade_off(tied, model, api):
    """Both sides of the joint-load trade-off among options equal on the
    frequency (sm_rec_trade_*): an option spreading the joint work over the
    week (spreads) vs one gathering it so the other days rest fully
    (rests_fully). Said only when the tied options really differ that way;
    an option that is neither is left out."""
    t = api['T']
    if not _sites(model):
        return None
    groups = []
    for i, o in tied:
        side = 'spread' if spreads(o, model) else 'rest' if rests_fully(o, model) else None
        if side is None:
            continue
        for g in groups:
            if g[0] == side:
                g[1].append(i)
                break
        else:
            groups.append((side, [i]))
    if len(groups) < 2:
        return None
    parts = [t('sm_rec_trade_%s_%s' % (side, 'end' if n == len(groups) - 1 else 'and'),
               nums=_nums(nums, t))
             for n, (side, nums) in enumerate(groups)]
    return t('sm_clause_sep_and').join(parts)
