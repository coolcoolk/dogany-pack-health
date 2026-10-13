"""Site-scoped care mode, severity and recency from recorded words.

The ko/en cue and intensity tables live in compose_rank_rules.json.
Missing severity opens one merged ask; history missing time gets one narrow
follow-up. The table documents inferred care policies separately from the
user's explicit modes and clinical sources separately from product choices.
"""
import os
import re

import compose_rank

UNKNOWN = 'unknown'

# The warehouse sits beside the service in both layouts: the pack repo
# (payload/service/health -> payload/knowledge/kimwog) and the installed
# instance (<root>/service/health -> <root>/knowledge/kimwog, pack_install.sh).
KIMWOG = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                      '..', '..', 'knowledge', 'kimwog')
_LADDER = {}


def rules():
    return compose_rank.shared_rules()['caution_care']


def ladder_path():
    return os.path.join(os.environ.get('DOGANY_KIMWOG_DIR') or KIMWOG, 'items',
                        rules()['ladder_item'] + '.md')


def _kimwog():
    import importlib.util
    path = os.path.join(os.path.dirname(os.path.dirname(ladder_path())), 'tools', 'kimwog.py')
    spec = importlib.util.spec_from_file_location('kimwog_reader', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ladder():
    """{level: rung} from the installed caution ladder (kimwog 056
    decision_ladder), read once per file version. The reader returns
    site_weight as a string; it is cast here. A missing item raises: the
    split never runs on a guessed ladder."""
    path = ladder_path()
    stamp = (path, os.stat(path).st_mtime_ns)
    if _LADDER.get('stamp') != stamp:
        fm, _body = _kimwog().read_frontmatter(path)
        rungs = {}
        for n, r in enumerate(fm['decision_ladder']):
            rungs[r['level']] = dict(r, order=n, site_weight=int(r['site_weight']),
                                     exclude_grades=list(r.get('exclude_grades') or []))
        _LADDER.update(stamp=stamp, rungs=rungs,
                       tissues=[t['tissue'] for t in fm.get('tissue_modifiers') or ()])
    return _LADDER


def modes():
    return list(rules()['modes'])


def _site_spans(text, words_of):
    """[(start, end, site)] for every mention of a known site in `text`, in
    text order; a mention inside a longer one is kept once, by the longer
    word."""
    hits = []
    low = text.lower()
    for site, words in words_of.items():
        for w in words:
            pat = re.escape(w.lower())
            if w.isascii():
                pat = r'\b%s\b' % pat     # 'hip' never inside 'ship'
            for m in re.finditer(pat, low):
                hits.append((m.start(), m.end(), site))
    hits.sort(key=lambda h: (h[0], -(h[1] - h[0])))
    out, end = [], -1
    for s, e, site in hits:
        if s < end:
            continue
        out.append((s, e, site))
        end = e
    return out


def _same(a, b, words_of):
    """One site, or two sites sharing a word (back / lower_back)."""
    return a == b or bool(set(words_of.get(a, ())) & set(words_of.get(b, ())))


def segments(words, site):
    """The stretches of `words` about `site`. When the words name another
    site too, only the stretches that start at this site's name (up to the
    next site's name) count -- one sentence often says one thing per site
    ("the knee before squats, the shoulder with a warm-up"). Sites named in
    a row ("knee and shoulder ...", caution_care.list_glue between them)
    share the stretch after the last of them. Words naming no other site
    are all about this one."""
    text = str(words or '')
    words_of = rules()['site_words']
    spans = _site_spans(text, words_of)
    if all(_same(s, site, words_of) for _a, _b, s in spans):
        return [text]
    glue = re.compile(rules()['list_glue'], re.IGNORECASE)
    own = [text[a:spans[n + 1][0] if n + 1 < len(spans) else len(text)]
           for n, (a, _b, _s) in enumerate(spans)]
    # back to front: a mention followed only by list glue reads on into the
    # next mention's stretch
    reach = [None] * len(spans)
    for n in range(len(spans) - 1, -1, -1):
        a, b, _s = spans[n]
        rest = own[n][b - a:]
        reach[n] = own[n] + (reach[n + 1] if n + 1 < len(spans)
                             and glue.fullmatch(rest) else '')
    return [reach[n] for n, (_a, _b, s) in enumerate(spans)
            if _same(s, site, words_of)]


def modes_from_words(words, site):
    """The modes the words state for the site, in the table's order; [] when
    they state none (unknown)."""
    text = ' '.join(segments(words, site))
    cues = rules()['cues']
    return [m for m in rules()['modes']
            if any(re.search(c, text, re.IGNORECASE) for c in cues.get(m, ()))]


def facts_for(site_modes, care_facts):
    """{fact: factor} a site's modes score in the split (split_model
    care_facts): the largest factor any of its modes gives; an empty or
    unknown mode list scores as `unknown`."""
    out = {}
    for m in (site_modes or [UNKNOWN]):
        for fact, f in (care_facts.get(m) or {}).items():
            out[fact] = max(out.get(fact, 0), f)
    return out


def _cue(text, patterns):
    return any(re.search(c, text, re.IGNORECASE) for c in patterns)


def profile_from_words(words, site):
    """Site-scoped severity and elapsed-time cues; no date is invented."""
    cfg = rules()
    text = ' '.join(segments(words, site))
    pain = text
    for pattern in cfg['pain_negations']:
        pain = re.sub(pattern, '', pain, flags=re.IGNORECASE)
    severity = next((s for s in cfg['severity_order']
                     if _cue(pain if s == 'current' else text,
                             cfg['severity_cues'][s])), None)
    recency = next((r for r in ('old', 'recent')
                    if _cue(text, cfg['recency_cues'][r])), None)
    for row in cfg['elapsed_cues']:
        hit = re.search(row['pattern'], text, re.IGNORECASE)
        if hit:
            months = float(hit[1]) * row['months']
            recency = 'recent' if months < cfg['recency_boundary_months'] else 'old'
            break
    for field in ('severity', 'recency'):
        if _cue(text, cfg['unknown_cues'][field]):
            if field == 'severity' and severity is None:
                severity = UNKNOWN
            elif field == 'recency' and recency is None:
                recency = UNKNOWN
    tissue = next((t for t, pats in cfg['tissue_cues'].items() if _cue(text, pats)), None)
    # a site-scoped load-pain picture (rules load_pain_site_tissues: the
    # knee's patellofemoral / named-OA joint pain, 056 + 057) names its
    # tissue only at its own sites; a tissue word alone (meniscus) is not it
    picture = None
    for name, spec in (cfg.get('load_pain_site_tissues') or {}).items():
        if site in spec['sites'] and tissue in (None, name) and _cue(text, spec['cues']):
            tissue = picture = name
    flags = text
    for pattern in cfg['red_flag_negations']:
        flags = re.sub(pattern, '', flags, flags=re.IGNORECASE)
    # a red flag counts with present pain (or words that name no level and
    # no time); a swelling in an old injury's story is history, not a flag
    red = ((severity == 'current' or severity in (None, UNKNOWN) and recency is None)
           and _cue(flags, cfg['red_flag_cues']))
    if red and severity in (None, UNKNOWN):
        severity = 'current'
    return dict(care=modes_from_words(words, site), severity=severity,
                recency=recency if severity == 'history' else None,
                tissue=tissue, red_flag=bool(red), load_pain_picture=picture)


def level_of(profile):
    """The ladder rung (kimwog 056) the profile stands on. Present pain is
    two rungs: a familiar ache at a tendon or the plantar fascia (tissue from
    the user's words, never from the site), or the knee's patellofemoral /
    named-OA joint pain (load_pain_site_tissues), stays loadable; any other or
    unnamed tissue, or a red flag, closes the site pending triage."""
    severity = profile.get('severity') or UNKNOWN
    if severity == 'history':
        return 'history-' + (profile.get('recency') or UNKNOWN)
    if severity == 'current':
        if profile.get('red_flag'):
            return 'red-flag'
        if profile.get('tissue') in rules()['load_pain_tissues']:
            return 'current-load-pain'
        if profile.get('tissue') and profile.get('load_pain_picture') == profile['tissue']:
            return 'current-load-pain'
        return 'current-other'
    return severity


def intensity(profile):
    """The rung's row: factor / prep / blocked grades / spread / route from
    the installed ladder item; substitutions and the care override from the
    rules table (product rows). Factors are score weights, never kilograms.
    `strengthen`: a rung that weighs the site and keeps prep adds the site's
    targeted strengthening (056 note 'add, don't only subtract'); mild stays
    prep only."""
    key = level_of(profile)
    product = rules()['intensity'][key]
    rung = ladder()['rungs'].get(key)
    row = dict(product, level=key)
    if rung:
        row.update(factor=rung['site_weight'], prep=bool(rung['prep']),
                   blocked_grades=rung['exclude_grades'],
                   spread=bool(rung['spread_load']), exposure=rung['exposure_days'],
                   triage=str(rung['route']).startswith('pain-triage'),
                   pain_limit=str(rung['route']).startswith('pain-monitoring'),
                   basis_grade=rung['basis_grade'])
    row.setdefault('spread', False)
    row.setdefault('pain_limit', False)
    row['strengthen'] = bool(row['prep'] and row['factor'] and not row['triage'])
    severity = profile.get('severity') or UNKNOWN
    suggested = rules()['suggested_modes']
    care = list(profile.get('care') or suggested.get(key) or suggested[severity])
    # spread before cut (056 note 3): the site's heavy days are kept apart
    # (fatigue scores back-to-back days); its exposure days are not cut
    if row['spread'] and 'fatigue' not in care:
        care = [m for m in care if m != UNKNOWN] + ['fatigue']
    row['care'] = list(row.get('care_override', care))
    return row


def scored_facts(profile, care_facts):
    row = intensity(profile)
    return {k: v * row['factor'] for k, v in facts_for(row['care'], care_facts).items()
            if row['factor']}
