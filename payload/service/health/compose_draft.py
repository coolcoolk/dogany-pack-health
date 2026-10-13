"""Names-only deterministic composition; prescription stays in program-plan."""
import copy
import compose_rank
import fatigue_overlap



def cooldown_for_lifts(p, cx, items):
    """The cooldown stretches for one session's lifts (<= 3): a caution
    site's stretch first (caution_policy site_cooldown) for the sites a lift
    uses, then the stretches of the lifts' primary muscles. `p` is the
    program-plan module. ONE rule for the composed program and for a free
    session (free_session.prep_day), so the two cannot drift."""
    muscles = {m for ex in items for m, role in cx.muscle_map().get(ex['name'], [])
               if role == 'primary'}
    # a caution site's cooldown stretch first (caution_policy
    # site_cooldown), for the sites a lift of the session uses
    site_cool = compose_rank.shared_rules()['caution_policy'].get('site_cooldown', {})
    sites = {it.get('site') for it in cx.st.get('safety_items') or ()}
    first = [k for site, lift in p.caution_lifts(cx, [e['name'] for e in items])
             if lift for k in site_cool.get(site, ())] if sites & set(site_cool) else []
    # one entry per drill: two catalog keys of the same stretch
    # never fill two of the three places (movement_catalog
    # drill_identity)
    out = p.MC.distinct_drills(first + [
        k for k, d in p.PREP_DRILLS.items()
        if d['slot'] == 'cooldown' and muscles.intersection(d['sites'])])[:3]
    return out or ['stretch_quads']

def build(cx, ranked, api, preview=False, report=None):
    """The draft; `report` (a dict) receives the soft volume shortfall the
    accepted draft would carry (the session minutes hold no more sets).
    A coverage tier whose composition the search found but the volume
    floor repair then refuses (a dumbbell-only home: one row a session
    and no vertical pull cannot hold the back floor) hands over to the
    next tier -- the plain composition last, as the coverage rules say."""
    skip = 0
    while True:
        held = {}
        try:
            return _build(cx, ranked, api, preview, report, skip, held)
        except api['Refused']:
            if 'tier' not in held or held['tier'] + 1 >= held['count']:
                raise
            skip = held['tier'] + 1


def _build(cx, ranked, api, preview, report, skip, held):
    """build() from coverage tier `skip` on; `held` gets the tier index
    the search found a composition in and the tier count."""
    from types import SimpleNamespace
    p = SimpleNamespace(**api)
    # The search asks the caution check per candidate per branch (~150k
    # calls a compose, a fifth of its time); within one build the answer
    # per lift cannot change (the safety items and the kit DB are not
    # written mid-search), so it is asked once per lift.
    caution = {}
    loads = p.loads_caution_area

    def loads_once(cx_, name):
        key = (id(cx_), name)
        if key not in caution:
            caution[key] = loads(cx_, name)
        return caution[key]
    p.loads_caution_area = loads_once
    if ranked['blocked']:
        raise p.Refused('\n'.join(ranked['blocked']))
    tiers = coverage_tiers(ranked)
    if ranked.get('cover_only') and len(tiers) > 1:
        tiers = tiers[:-1]      # the caller tries the plain draft later
    held['count'] = len(tiers)
    tiers = tiers[skip:]
    if not tiers:
        raise p.Refused('E-DRAFT-INFEASIBLE\tdays\tno safe shortlist composition')
    ranked = tiers[0]
    search_limit = compose_rank.load_rules()['split_model']['preview_search_visits'] if preview else 10000
    codes = sorted(ranked['sessions'], key=lambda c: c.endswith('B'))
    mandatory = compose_rank.mandatory_slots()
    days = {}
    visits = 0
    def ordered(code, items):
        return compose_rank.ordered(ranked, code, items)

    needs = {code: requirements(cx, ranked, code, p) for code in codes}
    profile = ranked['profile']
    rules = compose_rank.shared_rules()

    def room(code):
        """False when the lifts still owed to `code` cannot fit the lift
        minutes / count left (an admissible bound: only a branch that could
        never complete is cut, so the first draft found is unchanged)."""
        names = {e['name'] for e in days.get(code, [])}
        allowed = {c['name']: c for s in ranked['sessions'][code] for c in s['shortlist']}
        lifts = [allowed.get(n, {}) for n in names]
        spent = (compose_rank.session_minutes(lifts, rules, profile.get('sets'))
                 + compose_rank.main_reserve(profile, lifts, rules))
        owed, count = 0, 0
        taken = set()
        for cost, names_ok in needs[code]:
            if names_ok & names or names_ok & taken:
                continue
            # an unmet requirement no lift can meet, or the cheapest lift
            # for each requirement no other one shares
            owed += cost
            count += 1
            taken |= names_ok
        return (spent + owed <= profile.get('lift_minutes', float('inf')) + 1e-9
                and len(names) + count <= profile.get('lift_cap', len(names) + count))

    # the regions each session's shortlists can hold (lone-region lookahead)
    can_hold = {code: {c.get('region') for s in ranked['sessions'][code] for c in s['shortlist']
                       if not p.loads_caution_area(cx, c['name'])} for code in codes}

    def lone_dead(i):
        """True when the sessions through codes[i] leave a region to fewer
        sessions than the lone-region rule (compose_rank coverage_errors,
        E-REGION-LONE) needs and the sessions still to compose cannot all
        add it -- the branch can never validate, so it is cut here instead
        of after every composition of the later sessions (an admissible
        cut: the first draft found is unchanged)."""
        if not ranked.get('draft_rules') or len(codes) != 4 or \
                ranked.get('rotation_length', len(codes)) != len(codes):
            return False
        weekly = profile.get('weekly_frequency', len(codes))
        hits = {}
        for code in codes[:i+1]:
            allowed = compose_rank.slot_facts(ranked['sessions'][code])[0]
            for region in {allowed.get(e['name'], {}).get('region') for e in days.get(code, [])} - {None, 'core'}:
                hits[region] = hits.get(region, 0) + 1
        later = codes[i+1:]
        for region, n in hits.items():
            reach = n + sum(1 for code in later if region in can_hold[code])
            if reach * weekly < 2 * len(codes):
                return True
        return False

    def partial_ok(code):
        return (not compose_rank.validate(ranked, days, complete=False, check_order=False)
                and room(code))

    def fits_all():
        # a session whose owed lifts alone overrun the budget fails at once
        for code in codes:
            days[code] = []
            fits = room(code)
            days.pop(code)
            if not fits:
                return False
        return True

    def session(i):
        if i == len(codes):
            return not compose_rank.validate(ranked, days)
        code = codes[i]
        days[code] = []
        slots = ranked['sessions'][code]

        def slot(j):
            nonlocal visits
            visits += 1
            if visits > search_limit:
                raise p.Refused('E-DRAFT-SEARCH\tdays\tbounded search exhausted; edit shortlists')
            if j == len(slots):
                days[code] = ordered(code, days[code])
                if compose_rank.validate(dict(ranked, sessions={
                        c: ranked['sessions'][c] for c in codes[:i+1]}), days):
                    return False
                days[code] = ordered(code, days[code])
                if lone_dead(i):
                    return False
                if session(i+1):
                    return True
                for later in codes[i+1:]:
                    days.pop(later, None)
                return False
            s = slots[j]
            if not s['shortlist'] and s['slot'] not in mandatory:
                return slot(j+1)
            selected = {ex['name'] for ex in days[code]}
            if any(c['name'] in selected for c in s['shortlist']):
                if slot(j+1):
                    return True
                # Coverage can still need a bilateral companion for A/B
                # variety; retry this slot instead of making coverage final.
            for c in pair_order(code, s):
                if c['name'] in selected:
                    continue
                if p.loads_caution_area(cx, c['name']):
                    continue
                before = list(days[code])
                if c['name'] not in {x['name'] for x in before}:
                    days[code].append(dict(name=c['name'], display=p.UL.exercise_ko(c['name'])))
                if partial_ok(code) and slot(j+1):
                    return True
                days[code] = before
            # Only main and explicit practice slots are mandatory. Muscle
            # floors are audited across the week, not forced on every day.
            return slot(j+1) if s['slot'] not in mandatory else False
        return slot(0)

    def pair_order(code, s):
        """The slot's shortlist, a coverage pair kind the week's other
        sessions do not hold yet first (the second calf day seated, the
        second chest-press day the low incline)."""
        tags = lambda c: compose_rank.pair_tags(rules, s['slot'], c)   # noqa: E731
        if not ranked.get('draft_rules') or not any(tags(c) for c in s['shortlist']):
            return s['shortlist']
        held = set()
        for other, items in days.items():
            if other == code:
                continue
            allowed = compose_rank.slot_facts(ranked['sessions'][other])[0]
            for e in items:
                fact = allowed.get(e['name'])
                if fact is None:
                    continue
                # a scoped pair (press_angle) counts its lift in any slot; a
                # slot pair (calves) only a lift its own slot shortlisted
                held |= compose_rank.pair_tags(rules, None, fact, scoped_only=True)
                if any(sl['slot'] == s['slot'] and fact in sl['shortlist']
                       for sl in ranked['sessions'][other]):
                    held |= tags(fact)
        return sorted(s['shortlist'], key=lambda c: bool(tags(c) & held))

    # The coverage tiers (compose_rank coverage_tiers): every owed session
    # holds its requirement, else the week holds each, else the old search.
    found = False
    for index, tier in enumerate(tiers, skip):
        ranked = tier
        needs = {code: requirements(cx, ranked, code, p) for code in codes}
        days.clear()
        visits = 0
        if not fits_all():
            continue
        try:
            found = session(0)
        except p.Refused:
            found = False
        if found:
            held['tier'] = index
            break
    if not found:
        raise p.Refused('E-DRAFT-INFEASIBLE\tdays\tno safe shortlist composition')

    def overlap_count():
        facts = {}
        for code in days:
            facts.update(compose_rank.slot_facts(ranked['sessions'][code])[0])
        return fatigue_overlap.overlaps(list(ranked['sessions']), days, facts.get, rules)

    def lighten():
        """Adjacent-session overlap (fatigue_overlap), a SOFT preference: on
        an overlap a non-anchor lift carries over a swapping stressor (never
        grip, never the lower-body back-to-back fact), swap it for the
        lowest-fatigue lift of the same pattern and a shared primary muscle
        its session's shortlists hold that does not carry the stressor --
        only when the whole draft still validates and the week's overlaps
        fall; otherwise the lift stays. Bounded."""
        if not ranked.get('draft_rules'):
            return
        spec = fatigue_overlap.rules_spec(rules)
        by_id = {s['id']: s for s in spec['stressors']}
        for _round in range(8):
            report = overlap_count()
            if not report['resolvable']:
                return
            done = False
            for code, name, key in fatigue_overlap.swap_lifts(report):
                stressor = by_id[key.split(':')[0]]
                allowed = compose_rank.slot_facts(ranked['sessions'][code])[0]
                fact = allowed[name]
                held = {e['name'] for e in days[code]}
                options = sorted(
                    (c for c in allowed.values()
                     if c['name'] not in held
                     and c.get('pattern') == fact.get('pattern')
                     and set(c.get('primary', ())) & set(fact.get('primary', ()))
                     and not fatigue_overlap.carries(stressor, c)
                     and fatigue_overlap.lighter_key(c) < fatigue_overlap.lighter_key(fact)
                     and not p.loads_caution_area(cx, c['name'])),
                    key=lambda c: (fatigue_overlap.lighter_key(c), -c.get('score', 0), c['name']))
                old = days[code]
                for c in options:
                    days[code] = ordered(code, [
                        dict(name=c['name'], display=p.UL.exercise_ko(c['name']))
                        if e['name'] == name else e for e in old])
                    if (not compose_rank.validate(ranked, days)
                            and overlap_count()['resolvable'] < report['resolvable']):
                        done = True
                        break
                    days[code] = old
                if done:
                    break
            if not done:
                return

    lighten()

    def payload():
        prep, cooldown = {}, {}
        for code, items in days.items():
            for ex in items:
                for key in ('for_site', 'why', 'replaces', 'replaces_display'):
                    ex.pop(key, None)
            # The only safety swap is a caution table row (compose_rank
            # caution_policy.substitutions): the substitute the rank put in
            # its place records what it stands in for. Nothing else is
            # marked -- a caution prepares, it does not swap.
            names = {e['name'] for e in items}
            pool = {c['name']: c for s in ranked['sessions'][code] for c in s['shortlist']}
            for ex in items:
                c = pool.get(ex['name']) or {}
                if c.get('substitutes') and c['substitutes'] not in names:
                    ex.update(for_site=c['for_site'], replaces=c['substitutes'],
                              replaces_display=p.UL.exercise_ko(c['substitutes']),
                              why=p.caution_why(cx, c['for_site']))
        for code, items in days.items():
            prep[code] = p.prep_for_lifts(cx, items)
            if not prep[code]:
                prep[code] = ['dead_bug']
            cooldown[code] = cooldown_for_lifts(p, cx, items)
        return dict(days={c: [dict(e) for e in ordered(c, days[c])] for c in ranked['sessions']},
                    prep=prep, cooldown=cooldown)

    if preview:
        return payload()

    # Probe the existing spacing and volume fitter on detached state. A missing
    # audit must not masquerade as a verified draft.
    visited = set()
    def signature():
        return tuple((code, tuple(e['name'] for e in items)) for code, items in days.items())

    def repair_shortfall(probe):
        """Spend the existing day better before exposing a time decision.

        Each trial runs the real set fitter, spacing and volume audit. Keep
        only a strict reduction of the weekly deficit, with no new deficit
        in another trained muscle. This bounds repairs without cycling.
        """
        if profile.get('trainer_fit', {}).get('complete'):
            return False
        short = probe.st.get('volume_shortfall') or []
        if not short:
            return False
        floors = {s['muscle'] for s in short}
        before = {s['muscle']: s['floor'] - s['weekly_sets'] for s in short}
        mmap = cx.muscle_map()
        # Optional accessory groups must be reconsidered across the week:
        # removing only one occurrence can create a temporary deficit and
        # prevent reallocation. Explicit focus and chosen core work stay.
        optional = set(rules.get('optional_accessory_muscles', []))
        if 'core' in profile.get('practice', []):
            optional.discard('abs')
        original = {code: list(items) for code, items in days.items()}
        for code, items in original.items():
            pool = {c['name']: c for slot in ranked['sessions'][code]
                    for c in slot['shortlist']}
            days[code] = [ex for ex in items if not (
                set(pool[ex['name']]['primary']) <= optional
                and not pool[ex['name']].get('focused')
                and 'compound' not in pool[ex['name']]['tags'])]
        if signature() not in visited and not compose_rank.validate(ranked, days):
            check = copy.copy(cx)
            check.st = copy.deepcopy(cx.st)
            try:
                p.accept_compose(check, payload(), defer_floors=True)
            except p.Refused:
                pass
            else:
                after = {s['muscle']: s['floor'] - s['weekly_sets']
                         for s in check.st.get('volume_shortfall') or []}
                if (not check.st.get('volume_error')
                        and sum(after.values()) < sum(before.values())
                        and all(gap <= before.get(m, 0) for m, gap in after.items())):
                    return True
        days.update(original)
        for code in sorted(days, key=lambda c: len(days[c])):
            old = days[code]
            options = {c['name']: c for slot in ranked['sessions'][code]
                       for c in slot['shortlist'] if floors & set(c['primary'])}
            additions = [dict(name=c['name'], display=p.UL.exercise_ko(c['name']))
                         for c in sorted(options.values(), key=repair_priority)
                         if c['name'] not in {e['name'] for e in old}
                         and not p.loads_caution_area(cx, c['name'])]
            removable = []
            for ex in reversed(old):
                primary = {m for m, role in mmap.get(ex['name'], []) if role == 'primary'}
                remaining = {m for other, items in days.items() for e in items
                             if other != code or e is not ex
                             for m, role in mmap.get(e['name'], []) if role == 'primary'}
                if not primary & floors and (primary <= remaining or
                                               p.lift_region(cx, ex['name']) == 'core'):
                    removable.append(ex)
            # First recover minutes for sets on existing lifts; then add or
            # replace accessories using the same visible, safe shortlist.
            trials = [[e for e in old if e is not ex] for ex in removable]
            for addition in additions:
                trials.append(old + [addition])
                trials.extend([e for e in old if e is not ex] + [addition]
                              for ex in removable)
            for trial in trials:
                days[code] = ordered(code, trial)
                if signature() in visited or compose_rank.validate(ranked, days):
                    days[code] = old
                    continue
                check = copy.copy(cx)
                check.st = copy.deepcopy(cx.st)
                try:
                    p.accept_compose(check, payload(), defer_floors=True)
                except p.Refused:
                    days[code] = old
                    continue
                after = {s['muscle']: s['floor'] - s['weekly_sets']
                         for s in check.st.get('volume_shortfall') or []}
                if (not check.st.get('volume_error')
                        and sum(after.values()) < sum(before.values())
                        and all(gap <= before.get(m, 0) for m, gap in after.items())
                        and not compose_rank.validate(ranked, check.st['compose'])):
                    return True
                days[code] = old
        return False

    def add_margin(probe):
        """One more lift for a region-margin muscle no slot can raise
        further (program-plan fit_margin left it short): from the session
        shortlists, kept only when the whole draft validates, the accepted
        program leaves strictly fewer margin muscles short and no band
        shortfall grows."""
        short = probe.st.get('margin_short') or []
        if not short or probe.st.get('volume_shortfall'):
            return False
        for muscle in short:
            for code in sorted(days, key=lambda c: len(days[c])):
                old = days[code]
                held = {e['name'] for e in old}
                options = {c['name']: c for slot in ranked['sessions'][code]
                           for c in slot['shortlist'] if muscle in c.get('primary', ())}
                for c in sorted(options.values(), key=repair_priority):
                    if c['name'] in held or p.loads_caution_area(cx, c['name']):
                        continue
                    days[code] = ordered(code, old + [dict(
                        name=c['name'], display=p.UL.exercise_ko(c['name']))])
                    if signature() in visited or compose_rank.validate(ranked, days):
                        days[code] = old
                        continue
                    check = copy.copy(cx)
                    check.st = copy.deepcopy(cx.st)
                    try:
                        p.accept_compose(check, payload())
                    except p.Refused:
                        days[code] = old
                        continue
                    if (not check.st.get('volume_error') and not check.st.get('volume_shortfall')
                            and set(check.st.get('margin_short') or []) < set(short)):
                        return True
                    days[code] = old
        return False

    def repair_priority(candidate):
        preferences = rules.get('floor_repair_preferences', {})
        preferred = [n for site in profile.get('safety_sites', [])
                     for n in preferences.get(site, [])]
        name = candidate['name']
        return (preferred.index(name) if name in preferred else len(preferred),
                -candidate['score'], name)


    for _ in range(64):
        visited.add(signature())
        result = payload()
        errors = p.validate_compose(cx, result)
        if errors:
            raise p.Refused('\n'.join(errors))
        probe = copy.copy(cx)
        probe.st = copy.deepcopy(cx.st)
        try:
            p.accept_compose(probe, result)
        except p.Refused as exc:
            lines = str(exc).splitlines()
            floors = [line.split('\t')[2].split(':')[0] for line in lines
                      if line.startswith('E-VOLUME-FLOOR\t')]
            ceilings = [line.split('\t')[2].split(':')[0] for line in lines
                        if line.startswith('E-VOLUME-CEILING\t')]
            removed = False
            # Practice rows keep their practice dose and a zero-credit row is
            # not band volume (rx-calc muscle_credit): neither is a lever on
            # a muscle's ceiling. A loaded functional move counts in part and
            # may be dropped or swapped like any lift.
            shared = compose_rank.shared_rules()
            practice_only = compose_rank.practice_only_names(shared) | {
                n for n, e in compose_rank.muscle_credit_table(shared).items()
                if not e['loaded']}
            for muscle in ceilings:
                for code in reversed(list(days)):
                    for ex in reversed(days[code]):
                        if (muscle, 'primary') not in cx.muscle_map().get(ex['name'], []):
                            continue
                        if ex['name'] in practice_only:
                            continue    # not a band lever (see above)
                        trial = [e for e in days[code] if e is not ex]
                        # A redundant isolation slot may be dropped when its
                        # region remains covered here and its muscle elsewhere.
                        before_regions = {p.lift_region(cx, e['name']) for e in days[code]}
                        after_regions = {p.lift_region(cx, e['name']) for e in trial}
                        elsewhere = {m for other, es in days.items() for e in es
                                     if other != code or e in trial
                                     for m, r in cx.muscle_map().get(e['name'], []) if r == 'primary'}
                        primaries = {m for m, r in cx.muscle_map().get(ex['name'], []) if r == 'primary'}
                        if before_regions != after_regions or not primaries <= elsewhere:
                            continue
                        old = days[code]
                        days[code] = trial
                        if signature() not in visited and not compose_rank.validate(ranked, days):
                            removed = True
                            break
                        days[code] = old
                    if removed:
                        break
                if removed:
                    break
            if removed:
                continue
            # A required unilateral or main lift cannot simply be dropped.
            # Replace it from the same visible pool when another muscle can
            # take the practice slot without increasing the overfull muscle.
            replaced = False
            for muscle in ceilings:
                for code in reversed(list(days)):
                    options = {c['name']: c for slot in ranked['sessions'][code] for c in slot['shortlist']}
                    for ex in reversed(days[code]):
                        if (muscle, 'primary') not in cx.muscle_map().get(ex['name'], []):
                            continue
                        if ex['name'] in practice_only:
                            continue    # not a band lever (see above)
                        for c in sorted(options.values(), key=repair_priority):
                            if (muscle in c['primary'] or muscle in c.get('secondary', [])
                                    or c['name'] in {e['name'] for e in days[code]}
                                    or p.loads_caution_area(cx, c['name'])):
                                continue
                            old = days[code]
                            days[code] = ordered(code, [dict(name=c['name'], display=p.UL.exercise_ko(c['name']))
                                                       if e is ex else e for e in old])
                            if signature() not in visited and not compose_rank.validate(ranked, days):
                                replaced = True
                                break
                            days[code] = old
                        if replaced:
                            break
                    if replaced:
                        break
                if replaced:
                    break
            if replaced:
                continue
            if not floors:
                raise
            added = False
            # The weekly floor is hard over one-lift-per-isolation-movement
            # (rules coverage session_unique_isolation): only when no other
            # lift brings the muscle to its floor does the repair take a
            # repeat (a once-a-week arm day whose biceps lifts are all
            # curls), exempting that identity on that day in this tier only.
            for repeat in (False, True):
                for muscle in floors:
                    for code in sorted(ranked['sessions'], key=lambda c: len(days[c])):
                        facts = {c['name']: c for s in ranked['sessions'][code]
                                 for c in s['shortlist']}
                        options = {n: c for n, c in facts.items() if muscle in c['primary']}
                        held_keys = {compose_rank.isolation_key(rules, facts[e['name']])
                                     for e in days[code] if e['name'] in facts}
                        # a lift the week does not hold yet first (lat
                        # pulldown on the row day, not the B day's chin-up twice)
                        week = {e['name'] for items in days.values() for e in items}
                        for c in sorted(options.values(),
                                        key=lambda c: (c['name'] in week, repair_priority(c))):
                            if (c['name'] in {e['name'] for e in days[code]}
                                    or p.loads_caution_area(cx, c['name'])):
                                continue
                            key = compose_rank.isolation_key(rules, c)
                            if repeat and (key is None or key not in held_keys):
                                continue    # tried in the first pass
                            exempt = ranked.setdefault('isolation_floor', {}).setdefault(code, {})
                            fresh = repeat and key not in exempt
                            if fresh:
                                exempt[key] = 2
                            ex = dict(name=c['name'], display=p.UL.exercise_ko(c['name']))
                            old = days[code]
                            trials = [old + [ex]]
                            # At the time cap, replace a redundant accessory rather
                            # than breaking the cap to repair a weekly floor.
                            trials += [[e for e in old if e is not removed] + [ex]
                                       for removed in reversed(old)
                                       if not any(m in floors for m, role in cx.muscle_map().get(removed['name'], []) if role == 'primary')]
                            for trial in trials:
                                days[code] = ordered(code, trial)
                                if signature() not in visited and not compose_rank.validate(ranked, days):
                                    added = True
                                    break
                                days[code] = old
                            if added:
                                break
                            if fresh:
                                del exempt[key]
                        if added:
                            break
                    if added:
                        break
                if added:
                    break
            if not added:
                raise
        else:
            if probe.st.get('volume_error'):
                raise p.Refused('E-DRAFT-AUDIT\tdays\t' + probe.st['volume_error'])
            # The accepted result must still satisfy membership and A/B rules.
            errors = compose_rank.validate(ranked, probe.st['compose'])
            if errors:
                raise p.Refused('\n'.join(errors))
            if repair_shortfall(probe):
                continue
            if add_margin(probe):
                continue
            if report is not None:
                report['volume_shortfall'] = probe.st.get('volume_shortfall')
            # A region one session of four visits fails the self-check's
            # "every region twice a week": drop that lone lift and re-probe
            # (a tighter lift budget, e.g. practice blocks, can leave one).
            repaired = False
            for region in p.lone_regions(probe, probe.st['compose']):
                for code in days:
                    trial = [e for e in days[code] if p.lift_region(cx, e['name']) != region]
                    if len(trial) == len(days[code]):
                        continue
                    old = days[code]
                    days[code] = ordered(code, trial)
                    if signature() not in visited and not compose_rank.validate(ranked, days):
                        repaired = True
                        break
                    days[code] = old
                if repaired:
                    break
            if repaired:
                continue
            # Balance only with arrangements that pass the same full audits.
            # Prefer dropping a redundant accessory; otherwise add a useful
            # visible lift to a shorter session within its time budget.
            counts = {code: len(items) for code, items in days.items()}
            balance = compose_rank.load_rules()
            if profile.get('trainer_fit', {}).get('complete') and not balance['trainer_fit']['count_balance']:
                counts = {}
            if counts and max(counts.values()) - min(counts.values()) > balance['balance_max_difference']:
                trials = []
                for code in sorted(days, key=lambda c: -counts[c]):
                    if counts[code] != max(counts.values()):
                        continue
                    trials.extend((code, [e for e in days[code] if e is not ex])
                                  for ex in reversed(days[code]))
                for code in sorted(days, key=lambda c: counts[c]):
                    if counts[code] != min(counts.values()):
                        continue
                    options = {c['name']: c for slot in ranked['sessions'][code] for c in slot['shortlist']}
                    for c in sorted(options.values(), key=repair_priority):
                        if (c['name'] not in {e['name'] for e in days[code]}
                                and not p.loads_caution_area(cx, c['name'])):
                            trials.append((code, days[code] + [dict(name=c['name'], display=p.UL.exercise_ko(c['name']))]))
                balanced = False
                for code, trial in trials:
                    old = days[code]
                    days[code] = ordered(code, trial)
                    if signature() in visited or compose_rank.validate(ranked, days):
                        days[code] = old
                        continue
                    candidate = payload()
                    check = copy.copy(cx)
                    check.st = copy.deepcopy(cx.st)
                    try:
                        p.accept_compose(check, candidate)
                    except p.Refused:
                        days[code] = old
                        continue
                    if (check.st.get('volume_error') or
                            sum(s['floor'] - s['weekly_sets'] for s in
                                check.st.get('volume_shortfall') or []) >
                            sum(s['floor'] - s['weekly_sets'] for s in
                                probe.st.get('volume_shortfall') or [])):
                        days[code] = old
                        continue
                    balanced = True
                    break
                if balanced:
                    continue
            return result
    raise p.Refused('E-DRAFT-INFEASIBLE\tdays\tvolume floor could not be met')


def coverage_tiers(ranked):
    """The draft's plans, strictest first: every session holds the coverage
    it owes (compose_rank coverage_owed), then the week holds each owed
    requirement somewhere, then the composition without the coverage
    layer (its cover slots and draft rules off) -- so the minutes that
    cannot hold the coverage still build what they held before."""
    if not compose_rank.shared_rules().get('coverage'):
        return [ranked]
    owed = (ranked.get('coverage') or {}).get('owed') or {}
    plain = dict(ranked, draft_rules=False, coverage=None, sessions={
        code: [s for s in slots if not s['slot'].startswith('cover:')]
        for code, slots in ranked['sessions'].items()})
    return [dict(ranked, draft_rules=True, coverage=dict(owed=owed, strict=True)),
            dict(ranked, draft_rules=True, coverage=dict(owed=owed, strict=False)),
            plain]


def requirements(cx, ranked, code, p):
    """[(cheapest minutes, names that meet it)] for each lift session `code`
    must hold to validate (compose_rank.validate, complete): the main, each
    required region, the unilateral practice, the core practice, each
    chosen practice slot. Sorted dearest first; an empty name set (nothing
    can meet it) costs infinity. Only lifts the search may add count."""
    rules = compose_rank.shared_rules()
    profile = ranked['profile']
    slots = ranked['sessions'][code]
    usable = {}
    for s in slots:
        for c in s['shortlist']:
            if c['name'] not in usable:
                usable[c['name']] = (None if p.loads_caution_area(cx, c['name']) else c)
    usable = {n: c for n, c in usable.items() if c is not None}
    sets_ = []
    main = next((s for s in slots if s['slot'] == 'main'), None)
    if main:
        sets_.append({c['name'] for c in main['shortlist']})
    for region in compose_rank.session_rule(rules, 'required_regions', code, []):
        sets_.append({n for n, c in usable.items() if c.get('region') == region})
    constraints = {c['constraint']: c for c in ranked['constraints']}
    if constraints.get('unilateral_per_session', {}).get('minimum', 0):
        sets_.append({c['name'] for s in slots if s['slot'] == 'unilateral_practice'
                      for c in s['shortlist']})
    only = compose_rank.practice_only_names(rules)
    if (profile.get('trainer_fit', {}).get('complete') or
            'core' in profile.get('practice', []) and compose_rank.core_expected(rules, code)):
        sets_.append({n for n, c in usable.items() if c.get('region') == 'core' and n not in only})
    for pick, effect in compose_rank.practice_effects(rules, 'slot'):
        if pick in profile.get('practice', []):
            sets_.append(set(effect['names']))
    if ranked.get('draft_rules') and (ranked.get('coverage') or {}).get('strict'):
        # each coverage requirement the session owes (cover slot)
        for s in slots:
            if s['slot'].startswith('cover:'):
                sets_.append({c['name'] for c in s['shortlist']})
    out = []
    for names in sets_:
        names = frozenset(n for n in names if n in usable)
        cost = min((compose_rank.session_minutes([usable[n]], rules, profile.get('sets'))
                    for n in names), default=float('inf'))
        out.append((cost, names))
    return sorted(out, key=lambda r: -r[0])


def compact(ranked, display, draft, safe=lambda c: True):
    """One shared entry per lift/score; slots reference entries by index."""
    entries, indices, sessions = [], {}, {}
    constraints = {c['constraint'] for c in ranked['constraints']}
    for code, slots in ranked['sessions'].items():
        sessions[code] = {}
        selected = ({e['name'] for e in draft['days'][code]} if draft else
                    {c['name'] for s in slots for c in s['shortlist'][:2]})
        extra = False
        for slot in slots:
            if (slot['slot'] == 'unilateral_practice'
                    and selected <= {c['name'] for other in slots if other is not slot
                                     for c in other['shortlist']}):
                continue
            refs = []
            visible = [c for c in slot['shortlist'] if c['name'] in selected]
            if not extra and not code.endswith('B'):
                original = next((e for e in draft['days'][code]
                                 if e['name'] in {c['name'] for c in slot['shortlist']}), None) if draft else None
                for c in slot['shortlist']:
                    if c['name'] in selected or not safe(c):
                        continue
                    if original:
                        trial = copy.deepcopy(draft['days'])
                        trial[code] = [dict(e, name=c['name']) if e['name'] == original['name'] else e
                                       for e in trial[code]]
                        if compose_rank.validate(ranked, trial):
                            continue
                    visible.append(c)
                    extra = True
                    break
            for c in visible:
                entry = [c['name'], display(c['name']), c['score']]
                # Short tokens, not the repeated rule explanations.
                tokens = {'기능성 연습': '기능', '근육 볼륨': '근육',
                          '수행 능력': '수행', '안정적인 동작': '안정',
                          '주의 부위 부담 낮음': '부담낮음'}
                reasons = [tokens.get(r, r.replace(' ', '')[:8]) for r in c['reasons'][:1]]
                entry.append(reasons)
                flags = {}
                if 'unilateral_per_session' in constraints and 'unilateral' in c['tags']:
                    flags['unilateral'] = True
                if 'different_ab_grip' in constraints and c.get('grip'):
                    flags['grip'] = c['grip']
                if flags:
                    entry.append(flags)
                key = repr(entry)
                if key not in indices:
                    indices[key] = len(entries)
                    entries.append(entry)
                refs.append(indices[key])
            sessions[code][slot['slot']] = refs
    return dict(entries=entries, sessions=sessions)
