"""Deterministic, history-free compose shortlists. No prescription ownership.

Rule conditions are ANDed; tags_any is an intersection. Constraint effects
are interpreted by validate(). Equipment diversity uses prior shortlist leaders,
not records or an assumed model selection. Only user config/axes are queried.
"""
import json
from pathlib import Path
from exercise_catalog import CATALOG, CLOSE_GAPS, EXISTING_STABILIZERS

CATALOG_FACTS = dict(CATALOG, **CLOSE_GAPS)


def load_rules():
    return json.loads(Path(__file__).with_name('compose_rank_rules.json').read_text())


_SHARED = {}


def shared_rules():
    """The rules parsed once per file version, for READ-ONLY use on the hot
    paths (enrich / validate / the draft search call them thousands of
    times); load_rules() still hands a caller its own copy to change."""
    path = Path(__file__).with_name('compose_rank_rules.json')
    stamp = path.stat().st_mtime_ns
    if _SHARED.get('stamp') != stamp:
        _SHARED.update(stamp=stamp, rules=json.loads(path.read_text()))
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


def profile_from_context(cx, config_value, query):
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
    mode = config_value(cx.db, 'goal_mode') or h.get('goal_mode') or st.get('goal_mode')
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


def caution_substitution(name, sites, rules=None):
    """(site, substitute) when a recorded caution site's owner-approved
    substitution table (caution_policy.substitutions) takes `name` out of
    the plan, else None. The only lifts a caution swaps (owner 2026-09-27,
    restated 2026-10-04 11:44): anything not in the table keeps the lift."""
    table = (rules or shared_rules())['caution_policy']['substitutions']
    for site in sorted(s for s in sites if s):
        to = table.get(site, {}).get(name)
        if to:
            return site, to
    return None


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
    """Rows only a chosen practice slot may offer: never another slot.
    `withheld_names` are rows a practice slot no longer offers (hollow_hold
    left breath_trunk 2026-09-30: a hold is not Pilates); they stay out of
    every other slot too, so dropping a pick never leaks it elsewhere."""
    return {n for _pick, e in practice_effects(rules, 'slot')
            for n in tuple(e['names']) + tuple(e.get('withheld_names') or ())}


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


def session_rule(rules, key, code, default=None):
    """Prefer a full session variant, then the shared family rule."""
    table = rules.get(key, {})
    return table.get(code, table.get(code.rstrip('AB'), default))


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
    # Rank A first even when spacing rotates B ahead of its partner.
    for code in sorted(rotation, key=lambda c: c.endswith('B')):
        base = code.rstrip('AB')
        regions = session_rule(rules, 'session_regions', code, list(dict(muscle_region).values()))
        excluded = rules['session_excluded_muscles'].get(base, [])
        session_pool = [c for c in pool if c['region'] in regions
                        and all(region in regions for m, region in muscle_region if m in c.get('primary', []))
                        and not set(c.get('primary', [])) & (set(excluded) - set(rules.get('session_pattern_muscle_exceptions', {}).get(base, {}).get(c.get('pattern'), [])))
                        and not any(t in c['name'] for t in rules['session_excluded_name_tokens'].get(base, []))
                        and all(m not in c.get('primary', []) or any(t in c['name'] for t in tokens)
                                for m, tokens in rules['session_slot_name_tokens'].get(base, {}).items())
                        and not (rules['fillers']['forearms_focus_only'] and 'forearms' in c.get('primary', []) and not c.get('focused')
                                 and not any(t in ' '.join(profile.get('strands', [])).lower() for t in rules['fillers']['forearms_goal_tokens']))
                        and c.get('pattern') not in
                        session_rule(rules, 'session_excluded_patterns', code, [])]
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
        priority = rules['slot_priority']
        slots.sort(key=lambda s: priority.index(s[0]) if s[0] in priority else len(priority))
        sessions[code] = []
        for slot, region, eligible in slots:
            scored, subs = [], []
            for c in eligible:
                facts = dict(profile, **c)
                facts.update(slot=slot, practice_slot=slot == 'unilateral_practice')
                facts['equipment_repeated'] = c.get('equipment') in previous_eq.get(slot, set())
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
            shortlist = scored[:rules['shortlist_k']]
            if code.endswith('B') and shortlist:
                partner = leaders.get((code[:-1] + 'A', slot), {})
                variant = next((c for c in scored if grip_variant(partner, c)), None)
                if variant and variant not in shortlist:
                    shortlist[-1] = variant
            counterfactual = sorted(scored, key=lambda c: (-c['unpenalized_score'], c['name']))
            sessions[code].append(dict(slot=slot, region=region, shortlist=shortlist,
                                       unpenalized=counterfactual[0] if counterfactual else None))
            if shortlist:
                leaders[code, slot] = shortlist[0]
                previous_eq.setdefault(slot, set()).add(shortlist[0].get('equipment'))
            elif slot in mandatory_slots(rules):
                blocked.append('E-SHORTLIST-INFEASIBLE\t%s\tno available %s lift' % (code, slot))
    return dict(profile=profile, sessions={code: sessions[code] for code in rotation},
                constraints=constraints, blocked=blocked, order=rules['order'], caps=rules['unilateral_cap'],
                rotation_length=len(rotation))


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
    off = set(plan.get('cardio_off') or ())
    caps = per_day_strength(cx, minutes_between, care, cardio, off)
    total = cx.st.get('day_minutes')
    if total and plan.get('pick') == 'shrink':
        strength = int(total) - care - cardio
    elif total:
        strength = min([int(total) - care - cardio] + list(caps.values()))
    elif caps:
        strength = min(caps.values())
    else:
        strength = budget['default_minutes'] - care - cardio
    practice = set(_values((cx.st.get('handoff') or {}).get('practice')))
    blocks = block_minutes(practice, rules)
    return dict(minutes=strength + care + cardio, reserved=care + cardio + blocks,
                lift_minutes=strength - blocks, training=strength + cardio,
                strength=strength, cardio=cardio, per_day=caps)


def per_day_strength(cx, minutes_between, care, cardio, off=()):
    """{weekday: the strength minutes its window holds} for the timed
    training days (care and, unless moved off that day, cardio out)."""
    out = {}
    for w in (cx.st.get('daytime') or {}).get('windows', []):
        if not (w.get('start') and w.get('end')):
            continue
        m = minutes_between(w['start'], w['end'])
        for d in w['weekdays']:
            out[d] = m - care - (0 if d in off else cardio)
    return out


def care_minutes(rules=None):
    """Prep and cooldown care around every session (outside the training
    time the user chooses)."""
    budget = (rules or load_rules())['budget']
    return budget['prep_minutes'] + budget['cooldown_minutes']


def block_minutes(chosen, rules=None):
    """Minutes one session's practice blocks take at most: every start block
    (flow, power) plus the longest end block once -- a conditioning finisher
    and a circuit never stack on one session (practice_effects.end_blocks)."""
    rules = rules or load_rules()
    picked = [e for pick, e in practice_effects(rules, 'block') if pick in chosen]
    ends = [e['minutes'] for e in picked if e.get('when') == 'end']
    return sum(e['minutes'] for e in picked if e.get('when') != 'end') + max(ends, default=0)


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
    budget = (rules or shared_rules())['budget']
    base = budget['base_sets']
    return sum((budget['compound_minutes'] if 'compound' in c.get('tags', [])
                else budget['isolation_minutes']) * (c.get('sets') or sets or base) / float(base)
               + budget['transition_minutes']
               for c in candidates)


def set_levels(rules=None):
    return list((rules or shared_rules())['budget']['set_levels'])


def build_to_budget(cx, candidates, module, build, **kw):
    """(ranked, draft, sets): compose to the time budget -- fewer sets per
    lift BEFORE fewer lifts (owner 2026-10-01): each set level in turn, the
    first whose draft still trains every major region its sessions offer;
    when none does, the first level that built at all. Never past the
    budget. The level kept is stored on cx.st ('session_sets'); a `report`
    dict gets the kept draft's report. Raises the last refusal when no
    level builds, the state as it was."""
    refused, first = None, None
    had, before = 'session_sets' in cx.st, cx.st.get('session_sets')
    report = kw.pop('report', None)
    for level in set_levels():
        cx.st['session_sets'] = level
        ranked = for_context(cx, candidates, module)
        got = {} if report is not None else None
        try:
            draft = build(cx, ranked, module, report=got, **kw) if got is not None \
                else build(cx, ranked, module, **kw)
        except module['Refused'] as exc:
            refused = exc
            continue
        if first is None:
            first = (ranked, draft, level, got)
        if covers(ranked, draft, module):
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


def covers(ranked, draft, module):
    """True when every session's draft trains each major region (split
    model rules) that one of its slots offers a lift for."""
    major = set(shared_rules()['split_model']['major_regions'])
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
        # safety_load is a fact (the split screen grades the joint with it);
        # it no longer ranks or removes a lift (caution_policy).
        pool.append(dict(c, safety_load=safety_load(c, sites, rules),
                         substitute=caution_substitution(c['name'], sites, rules),
                         unavailable=module.loads_caution_area(cx, c['name']),
                         focused=bool(focus & (muscles | regions))))
    profile = profile_from_context(cx, module.config_value, module._q)
    budget = rules['budget']
    timing = time_budget(cx, module._minutes)
    profile['weekly_frequency'] = len((cx.st.get('days') or {}).get('weekdays') or cx.st['structure']['rotation'])
    profile['lift_minutes'] = timing['lift_minutes']
    profile['sets'] = cx.st.get('session_sets') or budget['base_sets']
    compound = budget['compound_minutes'] * profile['sets'] / float(budget['base_sets'])
    profile['lift_cap'] = min(budget['max_lifts'], max(0, int(profile['lift_minutes'] // compound)))
    return rank(pool, profile, cx.st['structure']['rotation'], module.MUSCLE_REGION, rules)


def ordered(plan, code, items):
    """Main, compounds, isolations, core; validation also enforces region continuity."""
    slots = plan['sessions'][code]
    allowed = {c['name']: c for s in slots for c in s['shortlist']}
    mains = [c['name'] for s in slots if s['slot'] == 'main' for c in s['shortlist']]
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
    for code, slots in plan['sessions'].items():
        items = days.get(code)
        if not isinstance(items, list): continue
        names = [ex.get('name') for ex in items if isinstance(ex, dict) and isinstance(ex.get('name'), str)]
        allowed = {c['name']: c for s in slots for c in s['shortlist']}
        for name in names:
            if name not in allowed:
                errors.append('E-SHORTLIST\tdays.%s\t%s is outside this session shortlist' % (code, name))
        required = session_rule(rules, 'required_regions', code, [])
        if complete and not set(required) <= {allowed.get(n, {}).get('region') for n in names}:
            errors.append('E-REGION-COVERAGE\tdays.%s\tinclude each major session region' % code)
        budget = rules['budget']
        profile = plan.get('profile', {})
        cost = session_minutes([allowed.get(n, {}) for n in names], rules, profile.get('sets'))
        if len(names) > profile.get('lift_cap', budget['max_lifts']) or cost > profile.get('lift_minutes', float('inf')):
            errors.append('E-SESSION-BUDGET\tdays.%s\tlifts exceed available time' % code)
        # A breath/trunk or whole-body row is not the loaded core the core pick asks for.
        if complete and 'core' in profile.get('practice', []) and core_expected(rules, code) and not any(
                allowed.get(n, {}).get('region') == 'core' and n not in practice_only_names(rules) for n in names):
            errors.append('E-CORE-PRACTICE\tdays.%s\tinclude core work' % code)
        for pick, effect in practice_effects(rules, 'slot'):
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
        if len(names) == len(items) and all(n in allowed for n in names):
            sequence = ordered(plan, code, items)
            seen_regions, previous = set(), None
            for ex in sequence:
                region = allowed[ex['name']].get('region')
                if region != previous:
                    if region in seen_regions:
                        errors.append('E-ORDER-REGION\tdays.%s\tcompound/isolation phases must not revisit a region' % code)
                        break
                    seen_regions.add(region)
                    previous = region
        if check_order and len(names) == len(items) and all(n in allowed for n in names) and items != ordered(plan, code, items):
            errors.append('E-ORDER\tdays.%s\tmain first, region blocks, compounds before isolation, core last' % code)
        cap = constraints.get('complexity_cap', {}).get('maximum')
        if cap is not None and sum('complex' in allowed.get(n, {}).get('tags', []) for n in names) > cap:
            errors.append('E-COMPLEXITY\tdays.%s\tat most %d complex free-weight lifts' % (code, cap))
        ordered_names = [e['name'] for e in ordered(plan, code, items)] if len(names) == len(items) and all(n in allowed for n in names) else names
        for slot in slots:
            muscle = slot['slot']
            # The first selected compound for each primary muscle is its main.
            picks = [n for n in ordered_names if muscle in allowed.get(n, {}).get('primary', [])
                     and 'compound' in allowed.get(n, {}).get('tags', [])]
            if picks: main[code, muscle] = picks[0]
    calf_days = [code for code, items in days.items() if isinstance(items, list) and any(
        'calves' in c.get('primary', []) and not c.get('focused')
        for slot in plan['sessions'].get(code, []) for c in slot['shortlist']
        if c['name'] in {e.get('name') for e in items if isinstance(e, dict)})]
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


def practice_blocks(practice, prep, caution, equipment, rules=None,
                    facilities=(), lifts=(), circuit=True):
    """Timed blocks for the chosen practice picks: {block: {...}} for one session.

    `prep` is the session's mat prep (a flow never repeats it), `caution` the
    recorded safety sites, `equipment` the usable classes (None = a gym),
    `facilities` the named spaces/equipment (a med-ball slam needs its own),
    `lifts` the session's lift names (a circuit station never repeats one),
    `circuit` whether this session is one of circuit_sessions().
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
            # reach a caution site go first; catalog order otherwise.
            pool = [k for k in effect['drills'] if k not in prep]
            pool.sort(key=lambda k: not caution & set(MOVEMENTS[k]['areas']))
            drills = pool[:effect['count']]
            out['flow'] = dict(pick=pick, minutes=effect['minutes'], drills=drills)
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
                ok = block.get('minutes') == effect['minutes'] and len(block.get('drills') or []) == effect['count']
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
