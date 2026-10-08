"""Deterministic, history-free compose shortlists. No prescription ownership.

Rule conditions are ANDed; tags_any is an intersection. Constraint effects
are interpreted by validate(). Equipment diversity uses prior shortlist leaders,
not records or an assumed model selection. Only user config/axes are queried.
"""
import json
from pathlib import Path
from exercise_catalog import CATALOG, CLOSE_GAPS, EXISTING_STABILIZERS

CATALOG_FACTS = dict(CATALOG, **CLOSE_GAPS)


RULES_PATH = Path(__file__).with_name('compose_rank_rules.json')


def load_rules():
    """The rules, the caller's own copy to change (the file's text is read
    once per file version)."""
    stamp = RULES_PATH.stat().st_mtime_ns
    if _TEXT.get('stamp') != stamp:
        _TEXT.update(stamp=stamp, text=RULES_PATH.read_text())
    return json.loads(_TEXT['text'])


_TEXT = {}
_SHARED = {}


def shared_rules():
    """The rules parsed once per file version, for READ-ONLY use on the hot
    paths (enrich / validate / the draft search call them thousands of
    times); load_rules() still hands a caller its own copy to change."""
    stamp = RULES_PATH.stat().st_mtime_ns
    if _SHARED.get('stamp') != stamp:
        _SHARED.update(stamp=stamp, rules=json.loads(RULES_PATH.read_text()))
    return _SHARED['rules']


def history_extension_noop(profile, candidates):
    """Reserved extension point. Owner chose NO history; never reads a DB."""
    return candidates


def _values(value):
    if isinstance(value, dict):
        return [x for v in value.values() for x in _values(v)]
    if isinstance(value, (list, tuple)):
        return [x for v in value for x in _values(v)]
    return [str(value)] if value is not None else []


def goal_mode(cx, config_value, goal_phase=None):
    """The goal mode the program is built for: the stated one (kit config,
    the handoff, the state), else 'cut' when the active goals' direction is a
    cut (program-plan goal_phase). A goal set in the consult carries no mode
    key on the live kit -- only its fat-down goal says cut (replay of the real
    state, 2026-10-06) -- so without this fallback a program-only restart
    skipped the trainer-time sizing and kept the thin 85-minute sessions."""
    st = cx.st
    mode = (config_value(cx.db, 'goal_mode') or (st.get('handoff') or {}).get('goal_mode')
            or st.get('goal_mode'))
    if not mode and goal_phase is not None and goal_phase(cx.db)[0] == 'cut':
        mode = 'cut'
    return mode


def profile_from_context(cx, config_value, query, goal_phase=None):
    st = cx.st
    h = st.get('handoff') or {}
    # Deliberately never call experience_from_record / practiced_rotation.
    band = config_value(cx.db, 'training_years_band') or st.get('years_band') or h.get('training_band')
    exp = config_value(cx.db, 'training_experience') or st.get('experience')
    experience_kind = {'beginner': 'first', 'returner': 'returning'}.get(exp, exp)
    axes = query(cx.db, "SELECT axis_key, label FROM metric_axis "
                       "WHERE origin='user' AND role='picture'")
    strands = list(dict.fromkeys(label for _key, label in axes if label))
    practice = _values(h.get('practice'))
    care = [k.strip() for k in (config_value(cx.db, 'goal_care') or '').split(',') if k.strip()]
    mode = goal_mode(cx, config_value, goal_phase)
    words = ' '.join(strands).lower()
    functional = any(w in words for w in ('기능', 'function')) or 'unilateral' in practice
    return dict(training_years_band=band, training_experience=exp,
                strands=strands, practice=practice, care=care, goal_mode=mode,
                novice=band in ('under1', 'lt1') or experience_kind in ('first', 'returning'),
                advanced=band == '3plus' and exp == 'continuous',
                technical='technical' in practice,
                functional=functional, unilateral_required='unilateral' in practice,
                size=any(w in words for w in ('볼륨','size','근육')) or mode in ('bulk','lean_bulk'),
                performance=any(w in words for w in ('수행','3대','performance')),
                body_composition=any(w in words for w in ('이쁜','몸','body')) or mode in ('cut','recomp'),
                health=any(w in words for w in ('건강','health')) or bool(care),
                facilities=(st.get('place') or {}).get('facilities', []),
                safety_sites=[s.get('site') for s in st.get('safety_items') or []])


def enrich(candidate):
    c = dict(candidate)
    cat = CATALOG_FACTS.get(c['name'], {})
    pattern, eq = c.get('pattern'), c.get('equipment')
    name = c['name']
    unilateral = cat.get('unilateral', False) or any(
        word in name for word in ('single_leg','single_arm','one_arm','split_squat','lunge'))
    compound = (cat['rep_class'] == 'compound' if cat.get('rep_class')
                else pattern in ('squat', 'hinge', 'horizontal_push',
                                 'horizontal_pull', 'vertical_push', 'vertical_pull'))
    tags = set()
    if unilateral: tags.add('unilateral')
    if compound: tags.add('compound')
    if pattern == 'isolation': tags.update(('isolation','simple'))
    if eq in ('machine','smith','smith_machine','cable','bodyweight_assist'): tags.add('guided')
    if pattern in ('carry','anti_rotation'): tags.add(pattern)
    if compound and eq in ('barbell','dumbbell','kettlebell','ez_bar'): tags.add('free_compound')
    if compound and eq == 'barbell': tags.update(('barbell_main','complex'))
    if unilateral and pattern == 'hinge': tags.add('complex')
    for key in ('movement', 'grip', 'fatigue'):
        c.setdefault(key, cat.get(key))
    c['technical'] = cat.get('technical', any(t in name for t in shared_rules()['technical']['name_tokens']))
    c['tags'] = sorted(tags)
    return c


def matches(condition, facts):
    for key, value in condition.items():
        if key.endswith('_any'):
            ok = bool(set(value) & set(facts.get(key[:-4], [])))
        elif key.endswith('_in'):
            ok = facts.get(key[:-3]) in value
        else:
            ok = facts.get(key) == value
        if not ok:
            return False
    return True


def safety_load(candidate, sites, rules):
    muscles = set(candidate.get('primary', []) + candidate.get('secondary', [])
                  + list(candidate.get('stabilizers', [])))
    grades = []
    for site in sites:
        precedent = rules.get('knee_precedents', {}).get(candidate.get('name')) if site == 'knee' else None
        if precedent:
            grades.append(precedent['grade'])
            continue
        if not muscles.intersection(rules['site_muscles'].get(site, [])):
            continue
        for rule in rules['safety_load_rules']:
            if matches(rule['condition'], dict(candidate, site=site)):
                grades.append(rule['grade'])
                break
    return next((g for g in ('high', 'medium', 'low') if g in grades), 'none')


def caution_substitution(name, sites, rules=None, profiles=None):
    """The base or intensity-specific substitution, if listed. Destinations
    must independently pass every site's load filter in for_context."""
    import caution_care
    policy = (rules or shared_rules())['caution_policy']
    table = {s: dict(rows) for s, rows in policy['substitutions'].items()}
    for site, profile in (profiles or {}).items():
        kind = caution_care.intensity(profile)['substitutions']
        table.setdefault(site, {}).update(policy['intensity_substitutions'].get(kind, {}).get(site, {}))
    for site in sorted(s for s in sites if s):
        to = table.get(site, {}).get(name)
        if to:
            return site, to
    return None


def caution_unavailable(candidate, profiles, rules=None):
    import caution_care
    cfg = rules or shared_rules()
    if caution_substitution(candidate['name'], profiles, cfg, profiles):
        return True
    return any(safety_load(enrich(candidate), [site], cfg)
               in caution_care.intensity(profile)['blocked_grades']
               for site, profile in profiles.items())


def grip_variant(a, b):
    return (a.get('movement') and a.get('movement') == b.get('movement')
            and a.get('equipment') == b.get('equipment')
            and a.get('grip') and b.get('grip') and a['grip'] != b['grip'])


def practice_effects(rules, kind=None):
    """The goal practice picks the program acts on, as (pick, effect)."""
    return [(pick, e) for pick, e in rules.get('practice_effects', {}).items()
            if isinstance(e, dict) and e.get('kind')
            and (kind is None or e.get('kind') == kind)]


def practice_only_names(rules):
    """Practice rows reserved for preparation, never lifting fillers.
    Retain withheld rows too, so dropping a pick cannot leak them into
    another lifting slot or turn unloaded practice into muscle volume."""
    return {n for _pick, e in practice_effects(rules)
            for n in tuple(e.get('names', ())) + tuple(e.get('withheld_names') or ())}


def muscle_credit_table(rules):
    """{name: {'loaded': f, 'bodyweight': f}}: the muscle-set credit of the
    functional / practice rows (rules `muscle_credit`, owner 2026-10-04
    11:21). A practice-only row left unlisted counts 0 (the 10:05 ruling);
    an unlisted row is absent and counts 1.0 (muscle_credit())."""
    table = {n: {'loaded': 0.0, 'bodyweight': 0.0} for n in practice_only_names(rules)}
    for name, e in ((rules.get('muscle_credit') or {}).get('exercises') or {}).items():
        loaded = float(e['loaded'])
        table[name] = {'loaded': loaded, 'bodyweight': float(e.get('bodyweight', loaded))}
    return table


def slot_loaded(ex):
    """True when a program slot carries real load: weight_kg > 0, or a
    `load` that is not bodyweight (a number > 0 or a word like "light")."""
    try:
        if float(ex.get('weight_kg') or 0) > 0:
            return True
    except (TypeError, ValueError):
        pass
    load = ex.get('load')
    if isinstance(load, bool) or load is None:
        return False
    if isinstance(load, (int, float)):
        return load > 0
    return str(load).strip().lower() not in ('', '0', 'none', 'bodyweight', 'bw')


def muscle_credit(table, name, loaded):
    """The factor a set of `name` adds to its mapped muscles (1.0 unlisted)."""
    e = table.get(name)
    if e is None:
        return 1.0
    return e['loaded'] if loaded else e['bodyweight']


def core_expected(rules, code):
    """False for a session whose type excludes abs (back days): the core pick
    asks for loaded core work only where abs may land (owner rule F31)."""
    return 'abs' not in rules['session_excluded_muscles'].get(code.rstrip('AB'), [])


def mandatory_slots(rules=None):
    rules = rules or shared_rules()
    return ('main', 'unilateral_practice') + tuple(
        e['slot'] for _pick, e in practice_effects(rules, 'slot'))


def caution_fit(rules, profile):
    """(avoid, capped, cap, prefer) of the trainer-fit caution table for the
    profile's recorded sites; empty outside the trainer-fit planner."""
    table = rules.get('trainer_fit', {}).get('caution_fit', {}) if profile.get('trainer_fit') else {}
    sites = [s for s in profile.get('safety_sites', []) if isinstance(table.get(s), dict)]
    avoid = {n for s in sites for n in table[s].get('avoid', [])}
    caps = [table[s]['weekly_cap'] for s in sites if table[s].get('weekly_cap')]
    capped = {n for c in caps for n in c['names']}
    cap = min((c['maximum'] for c in caps), default=None)
    prefer = {}
    for s in sites:
        for muscle, names in table[s].get('prefer', {}).items():
            prefer.setdefault(muscle, []).extend(n for n in names if n not in prefer.get(muscle, []))
    return avoid, capped, cap, prefer


def session_rule(rules, key, code, default=None):
    """Prefer a full session variant, then the shared family rule."""
    table = rules.get(key, {})
    return table.get(code, table.get(code.rstrip('AB'), default))


def ranking_order(rotation, rules):
    """Stable shortlist history even after recovery spacing rotates the week."""
    canonical = next((r for shape in rules['split_model']['catalog']
                      for r in shape['rotations'] if set(r) == set(rotation)),
                     sorted(rotation))
    return sorted(canonical, key=lambda c: c.endswith('B'))


def coverage_requirement(rules, rid):
    return next(r for r in (rules.get('coverage') or {}).get('requirements', ()) if r['id'] == rid)


def coverage_match(cond, c):
    """True when candidate `c` meets a coverage condition: matches() keys
    plus any_of (one sub-condition holds) and name_tokens_any /
    name_tokens_none (a token in / no token in the name)."""
    cond = dict(cond)
    alternatives = cond.pop('any_of', None)
    if alternatives is not None and not any(coverage_match(a, c) for a in alternatives):
        return False
    tokens = cond.pop('name_tokens_any', None)
    if tokens is not None and not any(t in c['name'] for t in tokens):
        return False
    tokens = cond.pop('name_tokens_none', None)
    if tokens is not None and any(t in c['name'] for t in tokens):
        return False
    return matches(cond, c)


def coverage_offer(c):
    """A pool candidate the shortlists can actually hold: not excluded by
    equipment / the caution intensity table (the `unavailable` fact) and
    not a caution substitution row."""
    return not c.get('unavailable') and not c.get('substitute')


def coverage_owed(pools, profile, rules):
    """{code: [requirement id, ...]}: each active weekly coverage
    requirement (rules `coverage`) dealt to one session that can meet it.
    Active: a session of its families is in the rotation, its muscle is not
    narrowed away (time_plan keep), and the family's pool offers a matching
    lift (a caution-blocked class is not offered, so it is not owed). Dealt
    in list order to the feasible session holding the fewest so far,
    ranking order breaking ties -- an A/B pair splits the planes."""
    owed = {code: [] for code in pools}
    keep = set(profile.get('keep') or ())
    for req in (rules.get('coverage') or {}).get('requirements', ()):
        if keep and req.get('muscle') not in keep:
            continue
        feasible = [code for code in pools
                    if code.rstrip('AB') in req['families'] or code in req['families']
                    if any(coverage_offer(c) and coverage_match(req['match'], c)
                           for c in pools[code][2])]
        if feasible:
            code = min(feasible, key=lambda c: (len(owed[c]), list(pools).index(c)))
            owed[code].append(req['id'])
    return owed


def coverage_errors(plan, days, complete=True):
    """Draft-only coverage errors (compose_draft.build marks its plan with
    `draft_rules`; a recorded or edited compose is never refused on them):
    a session repeating a session_unique pattern; complete, an owed
    requirement its session does not hold (strict) or the week does not hold;
    a pair whose kinds the week's lifts of that muscle do not both hold."""
    cov = plan.get('coverage') or {}
    rules = shared_rules()
    spec = rules.get('coverage') or {}
    unique = set(spec.get('session_unique_patterns', ()))
    errors = []
    held = {}
    for code, slots in plan['sessions'].items():
        items = days.get(code)
        if not isinstance(items, list):
            continue
        allowed = slot_facts(slots)[0]
        lifts = [allowed[e['name']] for e in items
                 if isinstance(e, dict) and e.get('name') in allowed]
        held[code] = lifts
        patterns = [c.get('pattern') for c in lifts if c.get('pattern') in unique]
        if len(patterns) != len(set(patterns)):
            errors.append('E-PLANE-REPEAT\tdays.%s\tone lift per movement plane' % code)
        errors.extend(stack_errors(code, lifts, rules))
    if not complete:
        return errors
    owed = cov.get('owed') or {}
    whole = (len(plan['sessions']) == plan.get('rotation_length', len(plan['sessions']))
             and set(plan['sessions']) <= set(days))
    for code, ids in owed.items():
        for rid in ids:
            match = coverage_requirement(rules, rid)['match']
            if cov.get('strict') and code in held:
                if not any(coverage_match(match, c) for c in held[code]):
                    errors.append('E-COVERAGE\tdays.%s\t%s' % (code, rid))
            elif whole and not any(coverage_match(match, c) for lifts in held.values() for c in lifts):
                errors.append('E-COVERAGE\tdays\t%s' % rid)
    if whole and len(held) == 4:
        # every region twice a week (program-plan lone_regions, the
        # self-check's rule): a four-session draft never leaves one region
        # to a single session (the floor repair stacking both calf lifts on
        # one back day)
        weekly = plan.get('profile', {}).get('weekly_frequency', len(held))
        hits = {}
        for lifts in held.values():
            for region in {c.get('region') for c in lifts} - {None, 'core'}:
                hits[region] = hits.get(region, 0) + 1
        for region, n in sorted(hits.items()):
            if n * weekly < 2 * len(held):
                errors.append('E-REGION-LONE\tdays\t%s' % region)
    if whole:
        for pair in spec.get('pairs', ()):
            # a slot pair: the lifts its slot shortlists; a scoped pair
            # (press_angle): the lifts its scope matches, any slot
            lifts = [c for code, ls in held.items() for c in ls
                     if any(pair_holds(pair, s['slot'], c) and c in s['shortlist']
                            for s in plan['sessions'][code])]
            sessions = {code for code, ls in held.items()
                        if any(c in lifts for c in ls)}
            offered = [k['id'] for k in pair['kinds']
                       if any(coverage_match(k['match'], c) for code in held
                              for s in plan['sessions'][code]
                              for c in s['shortlist'] if pair_holds(pair, s['slot'], c))]
            if len(sessions) >= 2 and len(offered) == len(pair['kinds']):
                for k in pair['kinds']:
                    if not any(coverage_match(k['match'], c) for c in lifts):
                        errors.append('E-COVERAGE-PAIR\tdays\t%s: %s' % (pair['id'], k['id']))
    return errors


def isolation_key(rules, c):
    """The identity a session holds one of (rules coverage
    session_unique_isolation), or None: an isolation lift's movement plus
    its coverage pair kind when a pair names a muscle it trains as a
    primary (a straight-knee and a seated calf raise differ)."""
    cov = rules.get('coverage') or {}
    spec = cov.get('session_unique_isolation')
    if not spec or c.get('pattern') != spec['pattern'] or not c.get(spec['key']):
        return None
    kinds = tuple(pair_kind(rules, pair['slot'], c) for pair in cov.get('pairs', ())
                  if pair.get('slot') in c.get('primary', ()))
    return (c[spec['key']],) + kinds


def isolation_errors(code, lifts, rules, exempt=None):
    """A session holding two isolation lifts of one identity (isolation_key)
    unless every lift of the repeat is a focused one (the user's focus).
    `exempt` {identity: lifts allowed}: the floor repair's last resort, a
    repeat that is the only lift bringing a muscle to its weekly floor
    (compose_draft, plan `isolation_floor`)."""
    spec = (rules.get('coverage') or {}).get('session_unique_isolation')
    if not spec:
        return []
    seen = {}
    for c in lifts:
        key = isolation_key(rules, c)
        if key is not None:
            seen.setdefault(key, []).append(c)
    return ['%s\tdays.%s\t%s: one lift per isolation movement' % (spec['error'], code, key[0])
            for key, held in sorted(seen.items(), key=lambda kv: str(kv[0]))
            if len(held) > (exempt or {}).get(key, 1)
            and not all(c.get('focused') for c in held)]


def stack_errors(code, lifts, rules):
    """Same-session fatigue stacking (rules fatigue_overlap.stacking): a
    session holding a lift of a rule's `heavy` class holds no other lift of
    its `also` class (no RDL after the deadlift)."""
    out = []
    for rule in (rules.get('fatigue_overlap') or {}).get('stacking', ()):
        heavy = [c for c in lifts if coverage_match(rule['heavy'], c)]
        if heavy and any(c is not heavy[0] and coverage_match(rule['also'], c) for c in lifts):
            out.append('E-FATIGUE-STACK\tdays.%s\t%s' % (code, rule['id']))
    return out


def shoulder_caution(rules, profile):
    """The rules shoulder_caution block when the profile records one of its
    sites (kimwog exercise/pull-push-plane-balance-066), else None."""
    spec = rules.get('shoulder_caution') or {}
    if spec and set(profile.get('safety_sites') or ()) & set(spec.get('sites', ())):
        return spec
    return None


def high_five(spec, c):
    """True for a behind-the-neck variant of the spec's excluded patterns
    (a lift with no pattern fact is judged by its name alone)."""
    return (any(t in c['name'] for t in spec.get('excluded_name_tokens', ()))
            and c.get('pattern') in set(spec.get('excluded_patterns', ())) | {None})


def shoulder_errors(plan, days, complete=True):
    """A shoulder caution's hard rules on an engine plan (plan['shoulder'],
    set by rank): no behind-the-neck press / pulldown; complete and the
    whole week, a horizontal pull kept (its variant may change, it never
    disappears to protect the shoulder)."""
    spec = plan.get('shoulder')
    if not spec:
        return []
    errors = []
    rules = shared_rules()
    caution = rules.get('shoulder_caution') or {}
    held = []
    for code, items in days.items():
        if not isinstance(items, list) or code not in plan['sessions']:
            continue
        allowed = slot_facts(plan['sessions'][code])[0]
        for ex in items:
            name = ex.get('name') if isinstance(ex, dict) else None
            if not isinstance(name, str):
                continue
            fact = allowed.get(name) or {'name': name}
            if high_five(caution, fact):
                errors.append('E-SHOULDER-HIGH-FIVE\tdays.%s\t%s: no behind-the-neck '
                              'variant under a shoulder caution' % (code, name))
            held.append(fact)
    whole = (len(plan['sessions']) == plan.get('rotation_length', len(plan['sessions']))
             and set(plan['sessions']) <= set(days))
    if complete and whole:
        for pattern in spec.get('keep', ()):
            if not any(c.get('pattern') == pattern for c in held):
                errors.append('E-SHOULDER-PULL\tdays\tkeep a %s under a shoulder '
                              'caution (the variant may change)' % pattern)
    return errors


def plane_variety(rules, slot, shortlist, scored):
    """The muscle slot's shortlist with plane variety (rules coverage
    slot_plane_variety): a shortlist holding one session_unique_patterns
    plane alone also offers the best `slot_plane_variety` lifts of each
    other such plane (`scored` = the slot's ranked candidates), so the
    floor repair can add a second lift of the muscle to a session that
    already holds the first plane. The main, a cover slot and the
    unilateral practice keep their list."""
    cov = rules.get('coverage') or {}
    unique, k = cov.get('session_unique_patterns', ()), cov.get('slot_plane_variety')
    if (not unique or not k or not shortlist or slot in ('main', 'unilateral_practice')
            or slot.startswith('cover:')):
        return shortlist
    held = {c.get('pattern') for c in shortlist}
    if len(held & set(unique)) != 1:
        return shortlist
    out = list(shortlist)
    for pattern in unique:
        if pattern not in held:
            out.extend([c for c in scored if c.get('pattern') == pattern][:k])
    return out


def pair_holds(pair, slot, c):
    """True when candidate `c` in slot `slot` is one of `pair`'s lifts: a
    slot pair (calves) by its slot, a scoped pair (press_angle) by its
    `scope` match in any slot."""
    if pair.get('scope') is not None:
        return coverage_match(pair['scope'], c)
    return pair.get('slot') == slot


def pair_kind(rules, slot, c):
    """The coverage pair kind id of candidate `c` in muscle slot `slot`, or None."""
    for pair in (rules.get('coverage') or {}).get('pairs', ()):
        if pair_holds(pair, slot, c):
            return next((k['id'] for k in pair['kinds'] if coverage_match(k['match'], c)), None)
    return None


def pair_tags(rules, slot, c, scoped_only=False):
    """{(pair id, kind id)} of every coverage pair holding candidate `c` in
    slot `slot` (`scoped_only`: the scoped pairs alone, whatever the slot)."""
    out = set()
    for pair in (rules.get('coverage') or {}).get('pairs', ()):
        if scoped_only and pair.get('scope') is None:
            continue
        if pair_holds(pair, slot, c):
            kind = next((k['id'] for k in pair['kinds'] if coverage_match(k['match'], c)), None)
            if kind:
                out.add((pair['id'], kind))
    return out


def pair_variety(rules, profile, slot, shortlist, scored):
    """A slot's shortlist with both kinds of every scoped coverage pair
    (rules coverage pairs `scope`, press_angle): a shortlist holding the
    pair's lifts of one kind only also offers the best-ranked lift of each
    missing kind (`scored` = the slot's ranked candidates), so the draft
    can take a low-incline press on the second chest day. With a caution
    at a `prefer_equipment` site, that kind's lifts in the preferred
    equipment come first (the incline dumbbell before the incline barbell
    at a shoulder caution)."""
    if not shortlist:
        return shortlist
    sites = set(profile.get('safety_sites') or ())
    out = list(shortlist)
    for pair in (rules.get('coverage') or {}).get('pairs', ()):
        if pair.get('scope') is None:
            continue
        kind = lambda c: next((k['id'] for k in pair['kinds']  # noqa: E731
                               if coverage_match(k['match'], c)), None)
        mine = [c for c in out if pair_holds(pair, slot, c)]
        if not mine:
            continue
        pref = pair.get('prefer_equipment') or {}
        preferred = bool(sites & set(pref.get('sites', ())))

        def rank_key(c):
            return 0 if (preferred and kind(c) == pref.get('kind')
                         and c.get('equipment') in pref.get('equipment', ())) else 1
        held = {kind(c) for c in mine}
        for k in pair['kinds']:
            if k['id'] in held:
                continue
            extra = sorted((c for c in scored if pair_holds(pair, slot, c)
                            and kind(c) == k['id'] and c not in out),
                           key=rank_key)
            if extra:
                out.append(extra[0])
        if preferred:
            # within the preferred kind, the preferred equipment first,
            # every other lift keeping its place
            spots = [i for i, c in enumerate(out) if pair_holds(pair, slot, c)
                     and kind(c) == pref.get('kind')]
            for i, c in zip(spots, sorted((out[i] for i in spots), key=rank_key)):
                out[i] = c
    return out


def _session_pool(code, pool, profile, muscle_region, rules):
    """(regions, excluded muscles, the session's candidate pool) of one
    rotation code: the family's regions, primary-muscle exclusions, name
    tokens, slot patterns and excluded patterns applied."""
    base = code.rstrip('AB')
    regions = session_rule(rules, 'session_regions', code, list(dict(muscle_region).values()))
    excluded = list(rules['session_excluded_muscles'].get(base, []))
    # a muscle's slot takes only the movement patterns the rules allow
    # it in this family (front/back arms: elbow work, never a press/row)
    slot_patterns = {m: v for m, v in rules.get('session_slot_patterns', {}).get(base, {}).items()
                     if isinstance(v, list)}
    if profile.get('trainer_fit') and 'abs' in excluded:
        excluded.remove('abs')
    session_pool = [c for c in pool if c['region'] in regions
                    and all(region in regions for m, region in muscle_region if m in c.get('primary', []))
                    and not set(c.get('primary', [])) & (set(excluded) - set(rules.get('session_pattern_muscle_exceptions', {}).get(base, {}).get(c.get('pattern'), [])))
                    and not any(t in c['name'] for t in rules['session_excluded_name_tokens'].get(base, []))
                    and all(m not in c.get('primary', []) or any(t in c['name'] for t in tokens)
                            for m, tokens in rules['session_slot_name_tokens'].get(base, {}).items())
                    and all(m not in c.get('primary', []) or c.get('pattern') in patterns
                            for m, patterns in slot_patterns.items())
                    and not (rules['fillers']['forearms_focus_only'] and 'forearms' in c.get('primary', []) and not c.get('focused')
                             and not any(t in ' '.join(profile.get('strands', [])).lower() for t in rules['fillers']['forearms_goal_tokens']))
                    and c.get('pattern') not in
                    session_rule(rules, 'session_excluded_patterns', code, [])]
    return regions, excluded, session_pool


def rank(candidates, profile, rotation, muscle_region, rules=None):
    rules = rules or load_rules()
    pool = [enrich(c) for c in history_extension_noop(profile, candidates)]
    chosen = set(profile.get('practice', []))
    # A whole-body pick is itself the opt-in for its light loaded get-up.
    opted = {n for pick, e in practice_effects(rules, 'slot')
             if pick in chosen and e.get('technical_opt_in') for n in e['names']}
    pool = [c for c in pool if not c['technical'] or profile.get('technical', False)
            or c['name'] in opted]
    for c in pool:
        requirements = {v for token, values in rules['availability']['requirements'].items()
                        if token in c['name'] for v in values}
        c['availability'] = 'limited' if requirements else 'common'
        c['region'] = next((region for m, region in muscle_region if m in c.get('primary', [])), 'core')
    pool = [c for c in pool if c['availability'] == 'common' or
            all(v in profile.get('facilities', []) for token, values in
                rules['availability']['requirements'].items() if token in c['name'] for v in values)]
    practice_only = practice_only_names(rules)
    practice_pool = [c for c in pool if c['name'] in practice_only]
    pool = [c for c in pool if c['name'] not in practice_only]
    constraints = [dict(r['effect'], id=r['id'], reason=r['reason'])
                   for r in rules['rules'] if 'constraint' in r['effect']
                   and matches(r['condition'], profile)]
    sessions, previous_eq, blocked = {}, {}, []
    leaders = {}
    avoid, capped, _cap, prefer = caution_fit(rules, profile)
    pool = [c for c in pool if c['name'] not in avoid]
    shoulder = shoulder_caution(rules, profile)
    if shoulder:
        # a shoulder caution: no behind-the-neck press / pulldown (rules
        # shoulder_caution, the high-five position)
        pool = [c for c in pool if not high_five(shoulder, c)]
    # Keep the catalog's ranking history when spacing reorders the calendar;
    # otherwise a valid selected lift can leave its own shortlist on rerank.
    pools = {code: _session_pool(code, pool, profile, muscle_region, rules)
             for code in ranking_order(rotation, rules)}
    owed = coverage_owed(pools, profile, rules)
    # a shoulder caution keeps its horizontal pull whenever a session of
    # the rotation can hold one (rules shoulder_caution keep_patterns)
    keep_pulls = [pat for pat in (shoulder or {}).get('keep_patterns', ())
                  if any(coverage_offer(c) and c.get('pattern') == pat
                         for _r, _x, session_pool in pools.values() for c in session_pool)]
    for code in ranking_order(rotation, rules):
        base = code.rstrip('AB')
        regions, excluded, session_pool = pools[code]
        slots = []
        main_patterns = session_rule(rules, 'main_patterns', code, [])
        if main_patterns:
            eligible = [c for c in session_pool if c['pattern'] in main_patterns
                        and 'compound' in c['tags'] and c['region'] != 'core'
                        and not any(t in c['name'] for t in rules['main_excluded_name_tokens'])]
            if (base in rules['performance_hinge']['sessions'] and matches(rules['performance_hinge']['condition'], profile)
                    and not set(profile.get('safety_sites', [])) & set(rules['performance_hinge']['except_sites'])):
                family = rules['performance_hinge']['B' if code.endswith('B') else 'A']
                preferred = [c for c in eligible if c['name'] in family]
                eligible = preferred or [c for c in eligible if c['name'] in rules['performance_hinge']['fallback']]
            slots.append(('main', 'main', eligible))
        for muscle, region in muscle_region:
            if region not in regions or muscle in excluded: continue
            eligible = [c for c in session_pool if muscle in c.get('primary', [])]
            tokens = rules.get('session_slot_name_tokens', {}).get(base, {}).get(muscle)
            if tokens:
                eligible = [c for c in eligible if any(t in c['name'] for t in tokens)]
            if eligible: slots.append((muscle, region, eligible))
        # Practice uses the same region-filtered pool as every other slot.
        if profile.get('unilateral_required'):
            practice_tags = set(session_rule(rules, 'practice_required_tags', code, ['unilateral', 'compound']))
            eligible = [c for c in session_pool if practice_tags <= set(c['tags'])
                        and not c['technical'] and c['pattern'] in session_rule(rules, 'practice_patterns', code, rules['practice_patterns']['전신'])
                        and c['equipment'] in rules['practice_equipment_by_pattern'].get(c['pattern'], [c['equipment']])]
            slots.append(('unilateral_practice', 'practice', eligible))
        # Breath/trunk and whole-body picks: one per session in any split,
        # so their rows ignore the session region filter.
        for pick, effect in practice_effects(rules, 'slot'):
            if pick in chosen:
                slots.append((effect['slot'], 'practice',
                              [c for c in practice_pool if c['name'] in effect['names']]))
        # the weekly coverage this session owes (rules `coverage`): a slot
        # shortlisting only the lifts that meet it, ranked right after the
        # main, so the draft fills it before any filler
        for rid in owed.get(code, ()):
            req = coverage_requirement(rules, rid)
            slots.append(('cover:' + rid, req['region'],
                          [c for c in session_pool if coverage_match(req['match'], c)]))
        priority = rules['slot_priority']
        # the goal's keep order (time_plan keep, owner 2026-10-05): when the
        # time is cut, the muscles the surviving goals need most take the
        # minutes first -- right after the main and the unilateral practice,
        # ahead of every other slot. No keep: the rules' order alone.
        keep = list(profile.get('keep') or ())
        # a kept muscle the session's main lift already loads (glutes under
        # the squat) ranks below a kept muscle no lift covers yet (the
        # hamstrings): when the cut drops lifts, every kept muscle still
        # keeps one lift (rehearsal GA(b), r5). Filled as the main is picked.
        loaded = set()

        def slot_key(s):
            base = priority.index(s[0]) if s[0] in priority else len(priority)
            if s[0] in ('main', 'unilateral_practice'):
                return (0, 0, base)
            if s[0].startswith('cover:'):
                return (0, 1, base)
            if s[0] in keep:
                return (1, s[0] in loaded, keep.index(s[0]))
            return (2, 0, base)
        slots.sort(key=slot_key)
        if keep:
            # a muscle no surviving goal keeps takes no minutes the kept
            # ones need: its filler slot goes (the main, the practice
            # slots, a region the session requires and a chosen core
            # practice stay -- validate still holds)
            required = session_rule(rules, 'required_regions', code, [])
            core = 'core' in profile.get('practice', [])
            slots = [s for s in slots if s[0] in mandatory_slots(rules)
                     or s[0].startswith('cover:') or s[0] in keep or s[1] in required or s[1] == 'practice'
                     or (core and s[1] == 'core')]
        sessions[code] = []
        while slots:
            slots.sort(key=slot_key)
            slot, region, eligible = slots.pop(0)
            # "main" spans unrelated movements (upper pull, squat, hinge).
            # Equipment variety belongs within that movement family: an
            # upper barbell row must not demote the lower day's squat, nor
            # a squat demote its hinge. Muscle slots already have this scope.
            equipment_slot = (slot, tuple(sorted(main_patterns))) if slot == 'main' else slot
            scored, subs = [], []
            for c in eligible:
                facts = dict(profile, **c)
                facts.update(slot=slot, practice_slot=slot == 'unilateral_practice')
                facts['equipment_repeated'] = c.get('equipment') in previous_eq.get(equipment_slot, set())
                partner = leaders.get((code[:-1] + 'A', slot), {}) if code.endswith('B') else {}
                facts['grip_alternative'] = bool(grip_variant(partner, c))
                score, reasons, excluded_candidate = 0, [], False
                penalty = 0
                for r in rules['rules']:
                    if not matches(r['condition'], facts): continue
                    effect = r['effect']
                    if effect.get('exclude'): excluded_candidate = True
                    if 'score' in effect:
                        score += effect['score']; reasons.append(r['reason'])
                        if r['id'].startswith('safety_'): penalty += effect['score']
                if not excluded_candidate:
                    scored.append(dict(c, score=score, unpenalized_score=score-penalty, reasons=reasons))
                elif c.get('substitute'):
                    subs.append((score, c))
            # A caution table row (caution_policy.substitutions) leaves the
            # pool; its substitute takes the row's rank when that is higher,
            # and carries what it stands in for (the plan's replaces/for_site).
            for row_score, row in sorted(subs, key=lambda r: (-r[0], r[1]['name'])):
                site, to = row['substitute']
                hit = next((i for i, x in enumerate(scored) if x['name'] == to), None)
                if hit is not None and row_score > scored[hit].get('rank_score', scored[hit]['score']):
                    scored[hit] = dict(scored[hit], rank_score=row_score,
                                       substitutes=row['name'], for_site=site)
            scored.sort(key=lambda c: (-c.get('rank_score', c['score']), c['name']))
            if capped:
                # trainer-fit caution: weekly-capped patterns rank last
                scored.sort(key=lambda c: c['name'] in capped)
            shortlist = scored[:rules['shortlist_k']]
            friendly = [c for n in prefer.get(slot, []) for c in scored if c['name'] == n]
            if friendly and not any(c in shortlist for c in friendly) and shortlist:
                # and a friendlier option is always on the list
                shortlist[-1] = friendly[0]
            if code.endswith('B') and shortlist:
                partner = leaders.get((code[:-1] + 'A', slot), {})
                variant = next((c for c in scored if grip_variant(partner, c)), None)
                if variant and variant not in shortlist:
                    shortlist[-1] = variant
            if ((rules.get('fatigue_overlap') or {}).get('lighter_option') and shortlist
                    and slot not in ('main', 'unilateral_practice') and not slot.startswith('cover:')
                    and all(c.get('fatigue') in ('high', 'med') for c in shortlist)):
                # the slot's lighter option (fatigue_overlap.lighter_option)
                lighter = next((c for c in scored if c.get('fatigue') == 'low'), None)
                if lighter:
                    shortlist.append(lighter)
            shortlist = plane_variety(rules, slot, shortlist, scored)
            shortlist = pair_variety(rules, profile, slot, shortlist, scored)
            counterfactual = sorted(scored, key=lambda c: (-c['unpenalized_score'], c['name']))
            sessions[code].append(dict(slot=slot, region=region, shortlist=shortlist,
                                       unpenalized=counterfactual[0] if counterfactual else None))
            if shortlist:
                leaders[code, slot] = shortlist[0]
                if slot == 'main' and keep:
                    loaded.update(shortlist[0].get('primary', []) + shortlist[0].get('secondary', []))
                previous_eq.setdefault(equipment_slot, set()).add(shortlist[0].get('equipment'))
            elif slot in mandatory_slots(rules):
                blocked.append('E-SHORTLIST-INFEASIBLE\t%s\tno available %s lift' % (code, slot))
    return dict(profile=profile, sessions={code: sessions[code] for code in rotation},
                constraints=constraints, blocked=blocked, order=rules['order'], caps=rules['unilateral_cap'],
                rotation_length=len(rotation), coverage=dict(owed=owed, strict=True),
                shoulder=dict(keep=keep_pulls) if shoulder else None)


def time_budget(cx, minutes_between):
    """One time model for split evaluation and final composition.

    The day-total is the user's own (owner 2026-10-02): st['day_minutes'] is
    the whole gym day -- prep + strength + cardio + cooldown. The strength
    part is what is left; practice blocks come out of it before the lifts.
    Each training day's window caps that day's strength, a day whose cardio
    moved to the supplementary day (time_plan cardio_off, the reconcile)
    holding no cardio. With a session-local shrink decision, compose the
    full queue to the agreed total; session-open applies the weekday cap.
    Otherwise the lift budget is the tightest day's. Without a total the shortest
    window is the day, as before. minutes = the planned day on the
    calendar; training = strength + cardio (the day without care)."""
    rules = load_rules()
    budget = rules['budget']
    care = care_minutes(rules)
    plan = cx.st.get('time_plan') or {}
    cardio = ((cx.st.get('cardio') or {}).get('minutes') or plan.get('cardio')
              or budget['default_cardio_minutes'])
    if plan.get('cardio_keep'):
        # a lower-priority fat goal's cardio shortened (the goal adjustment,
        # owner 2026-10-05): its minutes go to strength
        cardio = int(plan['cardio_keep'])
    off = set(plan.get('cardio_off') or ())
    caps = per_day_strength(cx, minutes_between, care, cardio, off)
    total = cx.st.get('day_minutes')
    # the cardio moved off EVERY regular day (the time decision, owner
    # 2026-10-04 19:05): the day-total holds no cardio, its minutes go to
    # strength
    days = (cx.st.get('daytime') or {}).get('weekdays') or ()
    in_day = 0 if days and set(days) <= off else cardio
    if total and plan.get('pick') == 'shrink':
        strength = int(total) - care - in_day
    elif total:
        strength = min([int(total) - care - in_day] + list(caps.values()))
    elif caps:
        strength = min(caps.values())
    else:
        strength = budget['default_minutes'] - care - cardio
    practice = set(_values((cx.st.get('handoff') or {}).get('practice')))
    blocks = block_minutes(practice, rules)
    if cx.st.get('trainer_fit'):
        blocks -= prep_overlap(practice, rules)
    return dict(minutes=strength + care + in_day, reserved=care + in_day + blocks,
                lift_minutes=strength - blocks, training=strength + in_day,
                strength=strength, cardio=cardio, per_day=caps)


def per_day_strength(cx, minutes_between, care, cardio, off=()):
    """{weekday: the strength minutes its window holds} for the timed
    training days (care and, unless moved off that day, cardio out). The
    user's own minutes a day (st['available_minutes'], owner 2026-10-04)
    cap every regular day as a window does."""
    avail = cx.st.get('available_minutes')
    out = {}
    for w in (cx.st.get('daytime') or {}).get('windows', []):
        m = (minutes_between(w['start'], w['end'])
             if w.get('start') and w.get('end') else None)
        if avail:
            m = min(m, avail) if m is not None else avail
        if m is None:
            continue
        for d in w['weekdays']:
            out[d] = m - care - (0 if d in off else cardio)
    return out


def care_minutes(rules=None):
    """Prep and cooldown care around every session (outside the training
    time the user chooses)."""
    budget = (rules or load_rules())['budget']
    return budget['prep_minutes'] + budget['cooldown_minutes']


def prep_overlap(chosen, rules=None):
    """Shared mobility time; caution preparation remains in the combined block."""
    rules = rules or load_rules()
    flow = max((e['minutes'] for pick, e in practice_effects(rules, 'block')
                if pick in chosen and e['block'] == 'flow'), default=0)
    return min(flow, rules['trainer_fit']['prep_overlap_minutes'])


def block_minutes(chosen, rules=None):
    """Reserve one combined preparation flow, power, and the longest end
    block. Trunk drills share the mobility flow; they do not add another
    lifting block. A circuit and finisher never stack."""
    rules = rules or load_rules()
    picked = [e for pick, e in practice_effects(rules, 'block') if pick in chosen]
    ends = [e['minutes'] for e in picked if e.get('when') == 'end']
    flow = max((e['minutes'] for e in picked if e['block'] == 'flow'), default=0)
    return (flow + sum(e['minutes'] for e in picked
                       if e.get('when') != 'end' and e['block'] != 'flow')
            + max(ends, default=0))


def circuit_sessions(rotation, weekly_days, rules=None):
    """The rotation codes that carry the mixed-circuit finisher.

    Codes rotate over the training days, so a code visited once per rotation
    comes round weekly_days / len(rotation) times a week. Take
    floor(high x rotation / weekly_days) codes (at least one), spread evenly
    from the first: 1-2 circuits a week unless the week holds more than two
    full rotations (then one code, the fewest the rotation model allows)."""
    rules = rules or load_rules()
    low, high = rules['practice_effects']['mixed_circuit']['per_week']
    n = len(rotation)
    if not n:
        return []
    days = weekly_days or n
    k = max(low, min(n, (high * n) // days))
    return [rotation[(i * n) // k] for i in range(k)]


def session_minutes(candidates, rules=None, sets=None):
    """Minutes the lifts take: per lift its class minutes scaled to its sets
    (c['sets'], else `sets`, else base_sets), plus the transition."""
    rules = rules or shared_rules()
    budget = rules['budget']
    base = budget['base_sets']
    practice = rules.get('practice_dose', {})
    return sum((budget['compound_minutes'] if 'compound' in c.get('tags', [])
                else budget['isolation_minutes']) * (c.get('sets') or practice.get(c.get('name'), {}).get('sets')
                    or sets or base) / float(base)
               + budget['transition_minutes']
               for c in candidates)


def set_levels(rules=None):
    return list((rules or shared_rules())['budget']['set_levels'])


def experience_facts(cx, config_value):
    """{training_experience, training_years_band, set_style} as the profile
    reads them (kit config first, then the plan state, then the handoff;
    the set style is the plan state's, rules set_style)."""
    st = cx.st
    h = st.get('handoff') or {}
    return dict(training_experience=config_value(cx.db, 'training_experience') or st.get('experience'),
                training_years_band=(config_value(cx.db, 'training_years_band') or st.get('years_band')
                                     or h.get('training_band')),
                set_style=set_style_of(st))


def set_style_of(st, rules=None):
    """The user's set style (rules set_style): the plan state's when it
    names a known style, else the default."""
    spec = (rules or shared_rules())['set_style']
    style = (st or {}).get('set_style')
    return style if style in spec['styles'] else spec['default']


def set_floor(facts, rules=None):
    """The per-slot set floor the profile facts match, or None: the set
    style's (rules set_style) -- `volume` names experience_set_floor, which
    applies to a trained lifter only; a style with its own fields applies
    to anyone who chose it (the dict carries `style`)."""
    rules = rules or shared_rules()
    style = facts.get('set_style') or rules['set_style']['default']
    spec = rules['set_style']['styles'].get(style) or {}
    if spec.get('floor'):
        floor = rules.get(spec['floor'])
        if floor and matches(floor['condition'], facts):
            return dict(floor, style=style)
        return None
    return dict(spec, style=style)


def trained_lifter(facts, rules=None):
    """The profile meets the experience_set_floor condition (training now,
    1+ years), whatever the set style."""
    floor = (rules or shared_rules()).get('experience_set_floor')
    return bool(floor and matches(floor['condition'], facts))


def slot_set_cap(floor, compound):
    """The most working sets a slot may reach under `floor` (set_floor),
    or None (no style cap): compound_max_sets for a loaded compound (a
    session's main or assisting compound), accessory_max_sets for an
    isolation or core slot."""
    if not floor:
        return None
    return floor.get('compound_max_sets' if compound else 'accessory_max_sets')


def primary_min_sets(facts, rules=None):
    """The main-lift working floor: the set style's primary_min_sets when it
    names one, else trainer_fit.primary_min_sets."""
    rules = rules or shared_rules()
    floor = set_floor(facts, rules) or {}
    return floor.get('primary_min_sets', rules['trainer_fit']['primary_min_sets'])


def region_margin(facts, rules=None):
    """(muscles, sets) of rules region_margin for a trained lifter, else
    None. Under a set style that caps the slots the margin is reached by
    one more lift (compose_draft add_margin), not by sets past the cap."""
    rules = rules or shared_rules()
    margin = rules.get('region_margin')
    if margin and trained_lifter(facts, rules) and set_floor(facts, rules):
        return list(margin['muscles']), int(margin['sets'])
    return None


def floor_levels(cx, module, rules=None):
    """(levels at or above the set floor, levels below it): every set level
    is 'at the floor' for a profile with no floor; a style that names its
    own set_levels composes at those alone (nothing below them)."""
    levels = set_levels(rules)
    floor = set_floor(experience_facts(cx, module['config_value']), rules)
    if not floor:
        return levels, []
    if floor.get('set_levels'):
        return list(floor['set_levels']), []
    return ([l for l in levels if l >= floor['accessory_min_sets']],
            [l for l in levels if l < floor['accessory_min_sets']])


def program_minutes(cx, candidates, module):
    """Cost the prescribed sets and the blocks each session actually contains."""
    import math
    catalog = {c['name']: enrich(c) for c in candidates}
    timing = time_budget(cx, module['_minutes'])
    fixed = timing['minutes'] - timing['strength']
    overlap = prep_overlap(module['chosen_practices'](cx)) if cx.st.get('trainer_fit') else 0
    minutes = {}
    for code, items in cx.st['compose'].items():
        lifts = [dict(catalog[e['name']], sets=module['sets_for'](
            cx, code, e['name'], module['dose'](cx, e['name'])[0]['sets'])) for e in items]
        blocks = (cx.st.get('practice_blocks') or {}).get(code) or {}
        extra = sum(b.get('minutes', 0) for b in blocks.values()) - overlap
        minutes[code] = math.ceil(fixed + extra + session_minutes(lifts))
    return minutes


def primary_reserve(profile, rules=None):
    """Minutes the trainer-fit primary lift needs above the uniform set
    level (trainer_fit.primary_min_sets): the draft costs every lift at
    profile['sets'], so the primary's working dose is reserved up front."""
    if not profile.get('trainer_fit', {}).get('primary'):
        return 0
    rules = rules or shared_rules()
    budget = rules['budget']
    floor = profile.get('primary_min_sets', rules['trainer_fit']['primary_min_sets'])
    extra = max(0, floor - profile.get('sets', budget['base_sets']))
    return budget['compound_minutes'] * extra / float(budget['base_sets'])


def main_reserve(profile, lifts, rules=None):
    """Minutes every MAIN lift of a session needs above the uniform set
    level: the first loaded compound of each region (core aside) keeps
    trainer_fit.primary_min_sets (owner 2026-10-06 21:04: upper-A day had its
    bench and shoulder press at 2 sets while the screen said 3~4). `lifts`
    = the session's candidate dicts, in order. 0 off the trainer fit."""
    if not profile.get('trainer_fit', {}).get('primary'):
        return 0
    regions = {c.get('region') for c in lifts
               if 'compound' in (c.get('tags') or ()) and c.get('region')
               and c.get('region') != 'core'}
    return primary_reserve(profile, rules) * max(1, len(regions))


def short_day_week(caps, rec, stated=True):
    """A short day (owner rule): it gets the shortfall decision at the
    sessions step, resource first, never a silent fit -- the trainer-time
    search would size every day down to that window. Such a week is
    composed on the plain path to the recommended day and the reconcile
    decides. A stated cut (kit config, handoff, state) keeps the trainer
    judgment in a window that is short every day (compose-fit tight
    window); only a regular day shorter than the day the longer days hold
    (never past the recommended day) is short (rehearsal RC(b)). A cut read
    from the goals' direction (goal_mode's fallback) sizes the day only into
    windows that hold it (the real state's 2h days): any window under the
    recommended day is short (rehearsal RA(iii), RS, GA). caps: day_windows."""
    timed = [m for m in caps.values() if m is not None]
    if not timed:
        return False
    return min(timed) < (min(max(timed), rec) if stated else rec)


def stated_cut(cx, module):
    """The cut is stated (kit config, handoff, state), not only read from
    the active goals' direction."""
    return goal_mode(cx, module['config_value']) == 'cut'


def build_to_budget(cx, candidates, module, build, **kw):
    """Use the available resource to complete the goals, then report the dose."""
    import copy
    caps = module['day_windows'](cx.st.get('daytime'), cx.st.get('available_minutes'))
    limits = [m for m in caps.values() if m is not None]
    if cx.st.get('available_minutes'):
        limits.append(cx.st['available_minutes'])
    mode = goal_mode(cx, module['config_value'], module.get('goal_phase'))
    if kw.get('preview'):
        return _build_at_budget(cx, candidates, module, build, **kw)
    if (not limits or mode != 'cut'
            or short_day_week(caps, module['day_minutes_rec'](cx)['rec'],
                              stated_cut(cx, module))
            or (cx.st.get('time_plan') or {}).get('status') != 'set'):
        previous = cx.st.pop('trainer_fit', None)
        if previous and previous.get('adjusted'):
            (cx.st.get('time_plan') or {}).pop('keep', None)
        return _build_at_budget(cx, candidates, module, build, **kw)
    limit = min(limits)
    key = _search_key(cx, candidates, module, mode, limit, kw)
    hit = _search_recall(cx, key)
    if hit is not None:
        return _search_replay(cx, candidates, module, hit, kw)
    entered = copy.deepcopy(cx.st)
    original = copy.deepcopy(cx.st)
    if (original.get('trainer_fit') or {}).get('adjusted'):
        (original.get('time_plan') or {}).pop('keep', None)
    policy = load_rules()['trainer_fit']
    start = min(limit, module['day_minutes_rec'](cx)['rec'])
    refused = None
    report = kw.pop('report', None)
    held = None
    short_cover = None

    def finish(draft, level, got):
        if report is not None:
            report.update(got)
        _search_keep(cx, key, dict(
            draft=draft, level=level, report=got,
            st=_state_delta(entered, cx.st)))
        return for_context(cx, candidates, module), draft, level
    # Complete scope first. Only after trying the full resource may scope shrink.
    # The primary lift's working dose goes only in the narrowed scope, last.
    # The weekly coverage (rules coverage) and a trained lifter's set floor
    # (rules experience_set_floor) hold over every day length and scope
    # first; the plain composition, then a level below the floor, only when
    # nothing with them builds at all.
    # The order (merge 0.33.0): the complete scope tries every at-floor pass
    # -- the coverage tiers, then the plain composition -- before the scope
    # narrows ("only after trying the full resource may scope shrink"; the
    # owner path with a practice block lost its arms and calves to a
    # narrowed coverage draft while the plain complete draft fit the
    # window); a level below the experience floor comes after every scope
    # at the floor.
    at_floor = [(True, True), (True, False)]
    below = [(False, False)] if floor_levels(cx, module)[1] else []
    scopes = ((True, True), (False, True), (False, False))
    order = [(scope, group) for group in (at_floor, below) if group for scope in scopes]
    for (complete, primary), group in order:
        for floor_only, cover_only in group:
            totals = list(range(start, limit, policy['minute_step'])) + [limit] if complete else [limit]
            for total in totals:
                cx.st.clear()
                cx.st.update(copy.deepcopy(original))
                cx.st['trainer_fit'] = dict(complete=complete, window=limit, primary=primary)
                cx.st['day_minutes'] = total
                cx.st.setdefault('time_plan', {}).update(status='set', pick='fits', total=total)
                if not complete:
                    cx.st['time_plan']['keep'] = list(policy['cut_keep'])
                got = {}
                try:
                    result = _build_at_budget(cx, candidates, module, build, report=got,
                                              floor_only=floor_only,
                                              cover_only=cover_only, **kw)
                    ranked, draft, level = result
                    probe = copy.copy(cx)
                    probe.st = copy.deepcopy(cx.st)
                    module['accept_compose'](probe, draft)
                    if complete and probe.st.get('volume_shortfall'):
                        # a coverage draft whose minutes hold fewer weekly
                        # sets than the floor (a soft shortfall, said
                        # plainly): kept as this pass's fallback -- the
                        # coverage holds before the plain composition
                        if cover_only and short_cover is None:
                            minutes = program_minutes(probe, candidates, module)
                            if max(minutes.values()) <= limit:
                                st = copy.deepcopy(cx.st)
                                st['day_minutes'] = max(minutes.values())
                                st['time_plan'].update(total=st['day_minutes'])
                                st['trainer_fit'].update(minutes=minutes, adjusted=None)
                                st.pop('time_decision', None)
                                short_cover = (st, draft, level, dict(
                                    got, volume_shortfall=probe.st['volume_shortfall']))
                        continue
                    minutes = program_minutes(probe, candidates, module)
                    if max(minutes.values()) > limit:
                        continue
                    cx.st['day_minutes'] = max(minutes.values())
                    cx.st['time_plan'].update(total=cx.st['day_minutes'])
                    cx.st['trainer_fit'].update(minutes=minutes,
                        adjusted=None if complete else 'hypertrophy_scope')
                    cx.st.pop('time_decision', None)
                    short = set(probe.st.get('margin_short') or ())
                    if complete and short:
                        # the region margin is short (rules region_margin): a
                        # longer day inside the window may hold it; the first
                        # complete program stays the fallback unless a longer
                        # one holds strictly more of the margin
                        if held is None:
                            held = (copy.deepcopy(cx.st), draft, level, got, short)
                        elif short < held[4]:
                            held = (copy.deepcopy(cx.st), draft, level, got, short)
                        if total < limit:
                            continue
                        break
                    return finish(draft, level, got)
                except module['Refused'] as exc:
                    refused = exc
            if complete and held is not None:
                st, draft, level, got, _short = held
                cx.st.clear()
                cx.st.update(st)
                return finish(draft, level, got)
            if complete and short_cover is not None:
                # no day length held the coverage AND the floor: the
                # coverage draft with its soft shortfall beats the plain
                # composition (rules coverage: the plain one only when
                # nothing with the coverage builds)
                st, draft, level, got = short_cover
                cx.st.clear()
                cx.st.update(st)
                return finish(draft, level, got)
    cx.st.clear()
    cx.st.update(original)
    if refused is None or (type(refused) is module['Refused'] and not vars(refused)):
        _search_keep(cx, key, dict(
            refused=str(refused) if refused is not None else None))
    raise refused or module['Refused']('E-DRAFT-INFEASIBLE\tdays\tno safe program fits the available resource')


# -- the draft search, computed once per input set ---------------------------
# The trainer-fit search (build_to_budget's minute-total loop) is the slow
# step of a consult, and split -> compose -> accept would otherwise rerun it
# on identical inputs three times (owner replay 2026-10-06: ~280 s each).
# Its result is kept beside the plan state (<state>.compose-search), keyed by
# everything the search reads: the plan state minus the fields every
# iteration overwrites, the candidates, the day, the kit DB's content stamp,
# this directory's code and rules, and the env. Any change is a new key.
SEARCH_KEEP = 8
# fields each minute-total iteration sets before it builds (time_plan
# status / pick / total and, under a prior adjusted fit, keep): their entry
# value never reaches the result
SEARCH_OVERWRITTEN = ('trainer_fit', 'day_minutes', 'session_sets')
SEARCH_CACHE_KEY = '_compose_search'
_SEARCH_MEMO = {}
SEARCH_STATS = {'runs': 0, 'hits': 0}


def _file_stamp(path):
    import os
    try:
        st = os.stat(path)
    except OSError:
        return None
    return [st.st_size, st.st_mtime_ns]


def _db_stamp(db):
    """The kit DB's content stamp: the main file's size and mtime, and the
    WAL's bytes (every reader touches the WAL's mtime, a write changes its
    bytes or, checkpointed, the main file)."""
    import hashlib
    import os
    if not db:
        return None
    wal = str(db) + '-wal'
    digest = None
    try:
        if os.path.getsize(wal):
            with open(wal, 'rb') as f:
                digest = hashlib.sha1(f.read()).hexdigest()
    except OSError:
        pass
    return [os.path.abspath(str(db)), _file_stamp(db), digest]


def _code_stamp():
    import os
    here = Path(__file__).parent
    out = []
    for d in (here, here / 'i18n'):
        try:
            names = sorted(os.listdir(d))
        except OSError:
            continue
        for n in names:
            f = d / n
            if f.is_file():
                out.append([str(f.relative_to(here)), _file_stamp(f)])
    return out


def _search_key(cx, candidates, module, mode, limit, kw):
    import hashlib
    import os
    st = json.loads(json.dumps(cx.st, sort_keys=True, default=repr))
    st.pop(SEARCH_CACHE_KEY, None)
    if (st.get('trainer_fit') or {}).get('adjusted'):
        (st.get('time_plan') or {}).pop('keep', None)
    for k in SEARCH_OVERWRITTEN:
        st.pop(k, None)
    if isinstance(st.get('time_plan'), dict):
        for k in ('status', 'pick', 'total'):
            st['time_plan'].pop(k, None)
    today = getattr(cx, 'today', None)
    program = getattr(cx, 'program', None)
    raw = json.dumps(dict(
        st=st, candidates=candidates, mode=mode, limit=limit,
        kw=sorted(k for k in kw if k != 'report'), today=str(today) if today else None,
        db=_db_stamp(getattr(cx, 'db', None)),
        program=[program, _file_stamp(program)] if program else None,
        code=_code_stamp(), rules=load_rules(),
        # the plan's reader, by name (a test may stand in its own)
        reader=getattr(module.get('_q'), '__qualname__', None),
        env=[os.environ.get(k) for k in ('AGENT_LANG', 'DOGANY_LIFEKIT_DIR',
                                         'KIT_LIFE_SH', 'WARG_DATA_DIR')],
    ), sort_keys=True, default=repr)
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()


def _search_path(cx):
    path = getattr(cx, 'state_path', None)
    return str(path) + '.compose-search' if path else None


def _search_recall(cx, key):
    import copy
    if key in _SEARCH_MEMO:
        SEARCH_STATS['hits'] += 1
        return copy.deepcopy(_SEARCH_MEMO[key])
    path = _search_path(cx)
    if path:
        try:
            with open(path, encoding='utf-8') as f:
                kept = json.load(f)
        except (OSError, ValueError):
            kept = {}
        for entry in kept.get('entries', []) if isinstance(kept, dict) else []:
            if isinstance(entry, dict) and entry.get('key') == key:
                _SEARCH_MEMO[key] = entry['result']
                SEARCH_STATS['hits'] += 1
                return copy.deepcopy(entry['result'])
    return None


def _search_keep(cx, key, result):
    """Remember a finished search; the file write is best-effort (a
    read-only state dir only costs the next call its search)."""
    import os
    import tempfile
    SEARCH_STATS['runs'] += 1
    # through JSON, so a recalled result is the one a later process reads
    result = json.loads(json.dumps(result, default=repr))
    _SEARCH_MEMO[key] = result
    path = _search_path(cx)
    if not path:
        return
    try:
        with open(path, encoding='utf-8') as f:
            kept = json.load(f)
        entries = [e for e in kept.get('entries', [])
                   if isinstance(e, dict) and e.get('key') != key]
    except (OSError, ValueError, AttributeError):
        entries = []
    entries = (entries + [dict(key=key, result=result)])[-SEARCH_KEEP:]
    try:
        d = os.path.dirname(os.path.abspath(path))
        fd, tmp = tempfile.mkstemp(dir=d, prefix='.compose-search.')
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            json.dump(dict(entries=entries), f, ensure_ascii=False)
        os.replace(tmp, path)
    except OSError:
        pass


def _state_delta(entered, final):
    """What the search changed in the plan state: the top-level fields it
    set (every overwritten field always) and the ones it dropped."""
    put = {k: v for k, v in final.items()
           if k in SEARCH_OVERWRITTEN or k == 'time_plan'
           or k not in entered or entered[k] != v}
    return dict(put=put, drop=[k for k in entered if k not in final])


def _search_replay(cx, candidates, module, hit, kw):
    import copy
    if 'refused' in hit:
        # the state as the search leaves it on a refusal: as it entered,
        # less a prior adjusted fit's keep
        if (cx.st.get('trainer_fit') or {}).get('adjusted'):
            (cx.st.get('time_plan') or {}).pop('keep', None)
        raise module['Refused'](
            hit['refused'] or 'E-DRAFT-INFEASIBLE\tdays\tno safe program fits the available resource')
    delta = hit['st']
    for k in delta['drop']:
        cx.st.pop(k, None)
    for k in SEARCH_OVERWRITTEN:
        if k not in delta['put']:
            cx.st.pop(k, None)
    cx.st.update(copy.deepcopy(delta['put']))
    report = kw.get('report')
    if report is not None:
        report.update(hit['report'] or {})
    return for_context(cx, candidates, module), hit['draft'], hit['level']


def _build_at_budget(cx, candidates, module, build, floor_only=False,
                     cover_only=False, **kw):
    """(ranked, draft, sets): compose to the time budget -- fewer lifts
    BEFORE fewer sets (rules budget.set_levels_doc trim order: an
    overlapping isolation, then a second lift of the same muscle / pattern,
    then the non-priority muscles to maintenance, only then 3 -> 2 sets,
    never below the experience floor while a level at it builds): each set
    level in turn, the first whose repaired draft meets its floors, else one
    that trains every major region its sessions offer. Preview uses region coverage;
    when none qualifies, keep the first level that built at all. Never past the
    budget. The level kept is stored on cx.st ('session_sets'); a `report`
    dict gets the kept draft's report. Raises the last refusal when no
    level builds, the state as it was. `floor_only`: the levels at the
    experience set floor alone (the trainer-fit search tries every day
    length at the floor before any level below it); `cover_only`: the draft
    keeps its coverage tiers (ranked['cover_only'], compose_draft
    coverage_tiers) -- no fallback to the plain composition."""
    refused, first = None, None
    had, before = 'session_sets' in cx.st, cx.st.get('session_sets')
    report = kw.pop('report', None)
    at_floor, below = floor_levels(cx, module)
    if floor_only:
        below = []
    for level in at_floor + below:
        if level in below and first is not None:
            break       # below the experience floor only when none at it builds
        cx.st['session_sets'] = level
        ranked = for_context(cx, candidates, module)
        if cover_only:
            ranked['cover_only'] = True
        got = {}
        try:
            draft = build(cx, ranked, module, report=got, **kw)
        except module['Refused'] as exc:
            refused = exc
            continue
        if first is None:
            first = (ranked, draft, level, got)
        if ((not kw.get('preview') and not got.get('volume_shortfall'))
                or covers(ranked, draft, module, keep_regions(cx, module))):
            first = (ranked, draft, level, got)
            break
    if first is None:
        if had:
            cx.st['session_sets'] = before
        else:
            cx.st.pop('session_sets', None)
        raise refused
    ranked, draft, level, got = first
    cx.st['session_sets'] = level
    if report is not None:
        report.update(got or {})
    return ranked, draft, level


def keep_regions(cx, module):
    """The regions of the goal's keep order (time_plan keep), or None: under
    a goal adjustment the regions no surviving goal needs may go (owner
    2026-10-05), so a set level is judged on the kept regions alone."""
    keep = (cx.st.get('time_plan') or {}).get('keep')
    if not keep:
        return None
    return {r for m, r in module['MUSCLE_REGION'] if m in keep}


def covers(ranked, draft, module, only=None):
    """True when every session's draft trains each major region (split
    model rules) that one of its slots offers a lift for (`only`: of those
    regions alone)."""
    major = set(shared_rules()['split_model']['major_regions'])
    if only is not None:
        major &= set(only)
    region_of = module['MUSCLE_REGION']
    for code, slots in ranked['sessions'].items():
        offered = {r for s in slots if s['shortlist']
                   for c in s['shortlist'] for m, r in region_of if m in c.get('primary', [])} & major
        pool = {c['name']: c for s in slots for c in s['shortlist']}
        trained = {r for e in draft['days'].get(code, [])
                   for m, r in region_of if m in pool.get(e['name'], {}).get('primary', [])}
        if offered - trained:
            return False
    return True


def for_context(cx, candidates, module):
    from types import SimpleNamespace
    module = SimpleNamespace(**module)
    pool = []
    sites = {s.get('site') for s in cx.st.get('safety_items') or []}
    profiles = module.care_profiles(cx)
    focus = set(module.compose_focus(cx))
    rules = load_rules()
    grips = {n: (movement, grip) for n, movement, grip in module._q(
        cx.db, 'SELECT exercise_name, movement, grip FROM exercise_movement_grip')}
    fatigue = dict(module._q(cx.db, 'SELECT exercise_name, cost FROM exercise_fatigue_cost'))
    for c in candidates:
        c = enrich(c)
        if c['name'] in grips:
            c['movement'], c['grip'] = grips[c['name']]
        c['fatigue'] = fatigue.get(c['name'], c.get('fatigue'))
        muscles = set(c['primary'] + c.get('secondary', []))
        c['stabilizers'] = list(CATALOG_FACTS.get(c['name'], {}).get(
            'stabilizers', EXISTING_STABILIZERS.get(c['name'], ())))
        regions = {region for m, region in module.MUSCLE_REGION if m in muscles}
        # One load grade feeds both split facts and intensity exclusions.
        # Mild / old history keep r7's load-neutral ranking.
        pool.append(dict(c, safety_load=safety_load(c, sites, rules),
                         substitute=caution_substitution(c['name'], sites, rules, profiles),
                         unavailable=caution_unavailable(c, profiles, rules),
                         focused=bool(focus & (muscles | regions))))
    profile = profile_from_context(cx, module.config_value, module._q,
                                   getattr(module, 'goal_phase', None))
    budget = rules['budget']
    timing = time_budget(cx, module._minutes)
    profile['weekly_frequency'] = len((cx.st.get('days') or {}).get('weekdays') or cx.st['structure']['rotation'])
    profile['lift_minutes'] = timing['lift_minutes']
    profile['sets'] = cx.st.get('session_sets') or budget['base_sets']
    profile['trainer_fit'] = cx.st.get('trainer_fit') or {}
    profile['primary_min_sets'] = primary_min_sets(
        experience_facts(cx, module.config_value), rules)
    profile['primary_reserve'] = primary_reserve(profile, rules)
    profile['keep'] = list((cx.st.get('time_plan') or {}).get('keep') or ())
    compound = budget['compound_minutes'] * profile['sets'] / float(budget['base_sets'])
    profile['lift_cap'] = min(budget['max_lifts'], max(0, int(profile['lift_minutes'] // compound)))
    return rank(pool, profile, cx.st['structure']['rotation'], module.MUSCLE_REGION, rules)


_SLOT_FACTS = {}


def slot_facts(slots):
    """(allowed {name: candidate}, main names in order) of one session's
    slots. A ranked session's slots are not changed once rank() returns,
    and the draft search reads them hundreds of thousands of times: kept
    per slots list (held, so its id is not reused)."""
    hit = _SLOT_FACTS.get(id(slots))
    if hit is not None and hit[0] is slots:
        return hit[1], hit[2]
    if len(_SLOT_FACTS) > 4096:
        _SLOT_FACTS.clear()
    allowed = {c['name']: c for s in slots for c in s['shortlist']}
    mains = [c['name'] for s in slots if s['slot'] == 'main' for c in s['shortlist']]
    _SLOT_FACTS[id(slots)] = (slots, allowed, mains)
    return allowed, mains


def ordered(plan, code, items):
    """Main, compounds, isolations, core; validation also enforces region continuity."""
    slots = plan['sessions'][code]
    allowed, mains = slot_facts(slots)
    names = {e['name'] for e in items}
    selected = next((n for n in mains if n in names), None)
    regions = list((plan.get('order') or shared_rules()['order'])['regions'])
    if selected:
        region = allowed[selected]['region']
        regions.remove(region)
        regions.insert(0, region)
    def key(ex):
        c = allowed.get(ex['name'], {})
        return (0 if ex['name'] == selected else 1,
                2 if c.get('region') == 'core' else 0 if 'compound' in c.get('tags', []) else 1,
                regions.index(c.get('region', 'core')),
                c.get('pattern') != 'hinge',
                'unilateral' in c.get('tags', []),
                -c.get('score', 0), ex['name'])
    return sorted(items, key=key)


def validate(plan, days, complete=True, check_order=True):
    rules = shared_rules()
    errors = list(plan['blocked'])
    constraints = {c['constraint']: c for c in plan['constraints']}
    main = {}
    practice_only = practice_only_names(rules)
    slot_effects = practice_effects(rules, 'slot')
    for code, slots in plan['sessions'].items():
        items = days.get(code)
        if not isinstance(items, list): continue
        names = [ex.get('name') for ex in items if isinstance(ex, dict) and isinstance(ex.get('name'), str)]
        allowed = slot_facts(slots)[0]
        for name in names:
            if name not in allowed:
                errors.append('E-SHORTLIST\tdays.%s\t%s is outside this session shortlist' % (code, name))
        required = session_rule(rules, 'required_regions', code, [])
        if complete and not set(required) <= {allowed.get(n, {}).get('region') for n in names}:
            errors.append('E-REGION-COVERAGE\tdays.%s\tinclude each major session region' % code)
        budget = rules['budget']
        profile = plan.get('profile', {})
        lifts = [allowed.get(n, {}) for n in names]
        cost = (session_minutes(lifts, rules, profile.get('sets'))
                + main_reserve(profile, lifts, rules))
        if len(names) > profile.get('lift_cap', budget['max_lifts']) or cost > profile.get('lift_minutes', float('inf')):
            errors.append('E-SESSION-BUDGET\tdays.%s\tlifts exceed available time' % code)
        if sum(allowed.get(n, {}).get('region') == 'core' for n in names) > rules['core_cap']:
            errors.append('E-CORE-CAP\tdays.%s\tat most one core lift per session' % code)
        # Preparation practice does not require another loaded core lift.
        if complete and (profile.get('trainer_fit', {}).get('complete') or
                         'core' in profile.get('practice', []) and core_expected(rules, code)) and not any(
                allowed.get(n, {}).get('region') == 'core' and n not in practice_only for n in names):
            errors.append('E-CORE-PRACTICE\tdays.%s\tinclude core work' % code)
        for pick, effect in slot_effects:
            hits = [n for n in names if n in effect['names']]
            if pick in profile.get('practice', []) and (
                    len(hits) > effect['per_session'] or complete and not hits):
                errors.append('%s\tdays.%s\t%s' % (effect['error'], code, effect['message']))
        minimum = constraints.get('unilateral_per_session', {}).get('minimum', 0)
        practice_names = {c['name'] for slot in slots if slot['slot'] == 'unilateral_practice' for c in slot['shortlist']}
        if complete and minimum and not set(names) & practice_names:
            errors.append('E-UNILATERAL\tdays.%s\tchoose at least %d unilateral lift(s)' % (code, minimum))
        main_slot = next((s for s in slots if s['slot'] == 'main'), None)
        main_names = {c['name'] for c in main_slot['shortlist']} if main_slot else set()
        selected_main = next((n for n in names if n in main_names), None)
        if complete and main_slot and not selected_main:
            errors.append('E-MAIN-SLOT\tdays.%s\tchoose a main compound' % code)
        spinal = rules['spinal_load']
        if selected_main and code.rstrip('AB') in rules['performance_hinge']['sessions']:
            if any(spinal.get(n, 0) > spinal.get(selected_main, 0) for n in names):
                errors.append('E-MAIN-SPINAL\tdays.%s\theaviest spinal-loading lift must be main first' % code)
        cap_uni = (plan.get('caps') or rules['unilateral_cap'])['default']
        if sum('unilateral' in allowed.get(n, {}).get('tags', []) for n in set(names)) > cap_uni:
            errors.append('E-UNILATERAL-CAP\tdays.%s\tat most %d unilateral lifts' % (code, cap_uni))
        complete_names = len(names) == len(items) and all(n in allowed for n in names)
        sequence = ordered(plan, code, items) if complete_names else None
        if complete_names:
            seen_regions, previous = set(), None
            for ex in sequence:
                region = allowed[ex['name']].get('region')
                if region != previous:
                    if region in seen_regions:
                        errors.append('E-ORDER-REGION\tdays.%s\tcompound/isolation phases must not revisit a region' % code)
                        break
                    seen_regions.add(region)
                    previous = region
        if check_order and complete_names and items != sequence:
            errors.append('E-ORDER\tdays.%s\tmain first, region blocks, compounds before isolation, core last' % code)
        cap = constraints.get('complexity_cap', {}).get('maximum')
        if cap is not None and sum('complex' in allowed.get(n, {}).get('tags', []) for n in names) > cap:
            errors.append('E-COMPLEXITY\tdays.%s\tat most %d complex free-weight lifts' % (code, cap))
        ordered_names = [e['name'] for e in sequence] if complete_names else names
        for slot in slots:
            muscle = slot['slot']
            # The first selected compound for each primary muscle is its main.
            picks = [n for n in ordered_names if muscle in allowed.get(n, {}).get('primary', [])
                     and 'compound' in allowed.get(n, {}).get('tags', [])]
            if picks: main[code, muscle] = picks[0]
    if 'draft_rules' in plan:
        # every engine draft tier (compose_draft coverage_tiers, the plain
        # one too): one lift per isolation movement a session
        for code, slots in plan['sessions'].items():
            items = days.get(code)
            if isinstance(items, list):
                allowed = slot_facts(slots)[0]
                errors.extend(isolation_errors(code, [
                    allowed[e['name']] for e in items
                    if isinstance(e, dict) and e.get('name') in allowed], rules,
                    (plan.get('isolation_floor') or {}).get(code)))
    if plan.get('draft_rules'):
        errors.extend(coverage_errors(plan, days, complete))
    errors.extend(shoulder_errors(plan, days, complete))
    if complete and plan.get('profile', {}).get('trainer_fit', {}).get('complete'):
        if any(len(items) < rules['trainer_fit']['min_lifts'] for items in days.values()):
            errors.append('E-GOAL-COVERAGE\tdays\tinclude at least four lifts per session')
        if (len(plan['sessions']) == plan.get('rotation_length', len(plan['sessions']))
                and set(plan['sessions']) <= set(days)):
            trained = {m for code, items in days.items()
                       for slot in plan['sessions'].get(code, []) for c in slot['shortlist']
                       if c['name'] in {e['name'] for e in items} for m in c['primary']}
            missing = set(rules['trainer_fit']['weekly_muscles']) - trained
            if missing:
                errors.append('E-GOAL-COVERAGE\tdays\tweekly muscles missing: ' + ', '.join(sorted(missing)))
    _avoid, capped, cap, _prefer = caution_fit(rules, plan.get('profile', {}))
    if cap is not None:
        held = [e.get('name') for items in days.values() if isinstance(items, list)
                for e in items if isinstance(e, dict) and e.get('name') in capped]
        if len(held) > cap:
            errors.append('E-CAUTION-FIT\tdays\tat most %d of %s per week' % (cap, ', '.join(sorted(set(held)))))
    calf_days = []
    for code, items in days.items():
        if not isinstance(items, list):
            continue
        held = {e.get('name') for e in items if isinstance(e, dict)}
        if any('calves' in c.get('primary', []) and not c.get('focused')
               for slot in plan['sessions'].get(code, []) for c in slot['shortlist']
               if c['name'] in held):
            calf_days.append(code)
    cycle_length = plan.get('rotation_length', len(plan['sessions']))
    weekly = plan.get('profile', {}).get('weekly_frequency', cycle_length)
    if len(calf_days) * weekly > rules['fillers']['calves_sessions'] * cycle_length:
        errors.append('E-CALVES-CAP\tdays\tcalves at most two sessions unless focused')
    if 'different_ab_main' in constraints:
        for code, slots in plan['sessions'].items():
            if not code.endswith('B'): continue
            partner = code[:-1] + 'A'
            a_slots = {s['slot']: s for s in plan['sessions'].get(partner, [])}
            for slot in slots:
                muscle = slot['slot']
                a = main.get((partner, muscle)); b = main.get((code, muscle))
                options = {c['name'] for s in (slot, a_slots.get(muscle, {}))
                           for c in s.get('shortlist', []) if 'compound' in c['tags']}
                b_candidate = next((c for s in slots for c in s['shortlist'] if c['name'] == b), {})
                # A later bilateral companion can precede the reserved practice
                # lift. Do not reject that incomplete session prematurely.
                settled = complete or 'unilateral' not in b_candidate.get('tags', [])
                if settled and a and a == b and len(options) > 1:
                    errors.append('E-AB-VARIETY\tdays.%s.%s\tchoose a different main lift from %s' % (code, muscle, partner))
    if 'different_ab_grip' in constraints:
        for code, slots in plan['sessions'].items():
            if not code.endswith('B'):
                continue
            partner = code[:-1] + 'A'
            a_allowed = {c['name']: c for s in plan['sessions'].get(partner, []) for c in s['shortlist']}
            for slot in slots:
                muscle = slot['slot']
                a_picks = [a_allowed.get(ex.get('name'), {}) for ex in days.get(partner, [])
                           if isinstance(ex, dict)]
                b_names = {ex.get('name') for ex in days.get(code, []) if isinstance(ex, dict)}
                for a in a_picks:
                    if muscle not in a.get('primary', []):
                        continue
                    for b in slot['shortlist']:
                        if (b['name'] in b_names and a.get('movement')
                                and a.get('movement') == b.get('movement')
                                and a.get('grip') and a.get('grip') == b.get('grip')
                                and any(grip_variant(a, c) for c in slot['shortlist'])):
                            errors.append('E-AB-GRIP\tdays.%s.%s\tprefer a different available grip from %s' % (code, muscle, partner))
    return errors


def _allowed(option, caution, equipment, facilities=(), taken=()):
    return ((equipment is None or option['equipment'] is None
             or option['equipment'] in equipment)
            and not caution & set(option['caution'])
            and all(v in facilities for v in option.get('requires', ()))
            and option['key'] not in taken)


# drill areas that belong to the legs: a drill reaching only these is a
# leg drill, never on a day that trains no leg region unless a site this
# session loads asks for it (owner 2026-10-06 21:04: leg swing on upper-A)
LOWER_AREAS = frozenset(('hip', 'hamstrings', 'quads', 'glutes', 'knee',
                         'ankle', 'calves', 'foot', 'plantar', 'adductors'))


def practice_blocks(practice, prep, caution, equipment, rules=None,
                    facilities=(), lifts=(), circuit=True, loaded=None,
                    lower=None):
    """Timed blocks for the chosen practice picks: {block: {...}} for one session.

    `prep` is the session's mat prep (a flow never repeats it), `caution` the
    recorded safety sites, `equipment` the usable classes (None = a gym),
    `facilities` the named spaces/equipment (a med-ball slam needs its own),
    `lifts` the session's lift names (a circuit station never repeats one),
    `circuit` whether this session is one of circuit_sessions(), `loaded`
    the caution sites this session's lifts load (None = all of `caution`),
    `lower` whether the session trains a leg region (None = unknown).

    The flow and the mat prep are one warm-up: a mobility drill the prep
    already holds counts toward the flow's drills (listed in both; the
    sessions screen and prep.yaml show it once), so the block stays short.
    """
    rules = rules or load_rules()
    from movement_catalog import MOVEMENTS, CARDIO_CATALOG
    caution = set(caution) - {None}
    facilities = set(facilities or ())

    def display(key):
        return (CARDIO_CATALOG.get(key) or MOVEMENTS[key])['ko']
    out = {}
    for pick, effect in practice_effects(rules, 'block'):
        if pick not in practice:
            continue
        if effect['block'] == 'flow':
            # A warm-up drill is unloaded: a caution site is a reason to
            # move it, never to skip it (owner 2026-10-02). Drills that
            # reach a site this session loads go first, then general drills;
            # a drill for a site the session does not load goes last (an
            # upper day opens with no knee drill); catalog order otherwise.
            here = caution if loaded is None else caution & set(loaded)

            def rank(k):
                areas = set(MOVEMENTS[k]['areas'])
                if here & areas:
                    return 0
                if lower is False and areas <= LOWER_AREAS:
                    return 3
                return 2 if caution & areas else 1
            shared = [k for k in effect['drills'] if k in prep]
            pool = [k for k in effect['drills'] if k not in prep]
            pool.sort(key=rank)
            drills = shared[:effect['count']] + pool[:max(
                0, effect['count'] - len(shared))]
            flow = out.setdefault('flow', dict(pick=pick, minutes=0, drills=[]))
            flow['minutes'] = max(flow['minutes'], effect['minutes'])
            flow['drills'].extend(k for k in drills if k not in flow['drills'])
        elif effect['block'] == 'power':
            option = next((o for o in effect['options']
                           if _allowed(o, caution, equipment, facilities)
                           and (o.get('of') != 'first_lift' or lifts)), None)
            out['power'] = dict(pick=pick, minutes=0) if not option else dict(
                pick=pick, minutes=effect['minutes'], key=option['key'],
                display=None if option.get('of') else display(option['key']),
                sets=option['sets'], rep_range=list(option['rep_range']),
                rest_sec=option['rest_sec'])
            if option and option.get('of') == 'first_lift':
                out['power']['lift'] = lifts[0]
        elif effect['block'] == 'circuit':
            if not circuit:
                continue
            keys = []
            for station in effect['stations']:
                option = next((o for o in station['options']
                               if _allowed(o, caution, equipment, facilities,
                                           taken=set(keys) | set(lifts))), None)
                if option:
                    keys.append(option['key'])
            if len(keys) < effect['min_stations']:
                out['circuit'] = dict(pick=pick, minutes=0, keys=keys)
                continue
            rounds = effect['minutes'] * 60 // (effect['work_sec'] * len(keys))
            out['circuit'] = dict(pick=pick, minutes=effect['minutes'], keys=keys,
                                  display=[display(k) for k in keys],
                                  work_sec=effect['work_sec'], rest_sec=effect['rest_sec'],
                                  rounds=rounds)
        else:
            option = next((o for o in effect['options']
                           if _allowed(o, caution, equipment)), None)
            if option:
                out['finisher'] = dict(pick=pick, minutes=effect['minutes'], key=option['key'],
                                       display=display(option['key']), work_sec=effect['work_sec'],
                                       rest_sec=effect['rest_sec'], rounds=effect['rounds'])
            else:
                out['finisher'] = dict(pick=pick, minutes=0)
    # One end block per session: the circuit replaces the finisher.
    ends = [b for b in rules['practice_effects']['end_blocks']['precedence'] if b in out]
    for later in ends[1:]:
        out.pop(later)
    return out


def validate_blocks(practice, blocks, rules=None, weekly_days=None):
    """Error lines for chosen practice blocks: one per session missing a
    per-session block, one per bad circuit, E-MIXED-CIRCUIT when the week
    carries no circuit (or, with weekly_days, not circuit_sessions() many),
    E-END-STACK for a session with two end blocks."""
    rules = rules or load_rules()
    effects = rules['practice_effects']
    errors = []
    circuits = 0
    for code, found in blocks.items():
        found = found or {}
        ends = [b for b in effects['end_blocks']['precedence'] if found.get(b)]
        if len(ends) > 1:
            errors.append('%s\t%s\t%s' % (effects['end_blocks']['error'], code,
                                            effects['end_blocks']['message']))
        for pick, effect in practice_effects(rules, 'block'):
            if pick not in practice:
                continue
            block = found.get(effect['block']) or {}
            if effect['block'] == 'flow':
                flow_effects = [e for pk, e in practice_effects(rules, 'block')
                                if pk in practice and e['block'] == 'flow']
                drills = block.get('drills') or []
                ok = (block.get('minutes') == max(e['minutes'] for e in flow_effects)
                      and len(drills) == len(set(drills))
                      and len(set(drills) & set(effect['drills'])) >= effect['count'])
            elif effect['block'] == 'power':
                ok = (block.get('minutes') == effect['minutes'] and block.get('key')
                      and block.get('sets', 0) > 0
                      and (block['key'] != 'speed_sets' or block.get('lift')))
            elif effect['block'] == 'circuit':
                if not block:
                    continue
                circuits += 1
                keys = block.get('keys') or []
                ok = (block.get('minutes') == effect['minutes']
                      and len(set(keys)) == len(keys) >= effect['min_stations']
                      and 0 < block.get('rounds', 0) * block.get('work_sec', 0) * len(keys)
                      <= effect['minutes'] * 60)
            else:
                if 'mixed_circuit' in practice and found.get('circuit'):
                    continue       # the circuit replaces the finisher here
                low, high = effect['minutes_range']
                ok = (low <= block.get('minutes', 0) <= high and block.get('key')
                      and block.get('work_sec', 0) * block.get('rounds', 0) > 0)
            if not ok:
                errors.append('%s\t%s.%s\t%s' % (effect['error'], effect['block'], code, effect['message']))
    if 'mixed_circuit' in practice and blocks:
        effect = effects['mixed_circuit']
        want = len(circuit_sessions(list(blocks), weekly_days, rules)) if weekly_days else None
        if not circuits or want is not None and circuits != want:
            errors.append('%s\tcircuit\t%s' % (effect['error'], effect['message']))
    return errors
