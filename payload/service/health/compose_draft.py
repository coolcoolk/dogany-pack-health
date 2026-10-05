"""Names-only deterministic composition; prescription stays in program-plan."""
import copy
import compose_rank


def build(cx, ranked, api, preview=False, report=None):
    """The draft; `report` (a dict) receives the soft volume shortfall the
    accepted draft would carry (the session minutes hold no more sets)."""
    from types import SimpleNamespace
    p = SimpleNamespace(**api)
    if ranked['blocked']:
        raise p.Refused('\n'.join(ranked['blocked']))
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
        spent = compose_rank.session_minutes([allowed.get(n, {}) for n in names], rules, profile.get('sets'))
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

    def partial_ok(code):
        return (not compose_rank.validate(ranked, days, complete=False, check_order=False)
                and room(code))

    # a session whose owed lifts alone overrun the budget fails at once
    for code in codes:
        days[code] = []
        fits = room(code)
        days.pop(code)
        if not fits:
            raise p.Refused('E-DRAFT-INFEASIBLE\tdays\tno safe shortlist composition')

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
            for c in s['shortlist']:
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

    if not session(0):
        raise p.Refused('E-DRAFT-INFEASIBLE\tdays\tno safe shortlist composition')

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
            muscles = {m for ex in items for m, role in cx.muscle_map().get(ex['name'], [])
                       if role == 'primary'}
            cooldown[code] = [k for k, d in p.PREP_DRILLS.items()
                              if d['slot'] == 'cooldown' and muscles.intersection(d['sites'])][:3]
            if not cooldown[code]:
                cooldown[code] = ['stretch_quads']
        return dict(days={c: [dict(e) for e in ordered(c, days[c])] for c in ranked['sessions']},
                    prep=prep, cooldown=cooldown)

    if preview:
        return payload()

    # Probe the existing spacing and volume fitter on detached state. A missing
    # audit must not masquerade as a verified draft.
    visited = set()
    def signature():
        return tuple((code, tuple(e['name'] for e in items)) for code, items in days.items())

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
                        for c in sorted(options.values(), key=lambda c: (-c['score'], c['name'])):
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
            for muscle in floors:
                for code in sorted(ranked['sessions'], key=lambda c: len(days[c])):
                    options = {c['name']: c for s in ranked['sessions'][code]
                               for c in s['shortlist'] if muscle in c['primary']}
                    for c in sorted(options.values(), key=lambda c: (-c['score'], c['name'])):
                        if (c['name'] in {e['name'] for e in days[code]}
                                or p.loads_caution_area(cx, c['name'])):
                            continue
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
            if max(counts.values()) - min(counts.values()) > compose_rank.load_rules()['balance_max_difference']:
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
                    for c in sorted(options.values(), key=lambda c: (-c['score'], c['name'])):
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
                    if check.st.get('volume_error'):
                        days[code] = old
                        continue
                    balanced = True
                    break
                if balanced:
                    continue
            return result
    raise p.Refused('E-DRAFT-INFEASIBLE\tdays\tvolume floor could not be met')


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
    if 'core' in profile.get('practice', []) and compose_rank.core_expected(rules, code):
        sets_.append({n for n, c in usable.items() if c.get('region') == 'core' and n not in only})
    for pick, effect in compose_rank.practice_effects(rules, 'slot'):
        if pick in profile.get('practice', []):
            sets_.append(set(effect['names']))
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
