"""Session-local prescriptions for off-plan workouts; never edits consult data."""
import hashlib
import importlib.machinery
import importlib.util
import json
import os
from pathlib import Path
import sqlite3

CODE = "자유"
# rx-calc defaults: three working sets, 6-10 reps, factored rest (no override).
# G19's compound-freeweight safety floor is 2 even without an owner card.
DEFAULT_SETS = 3
DEFAULT_REPS = [6, 10]
DEFAULT_RIR_FLOOR = 2
HERE = Path(__file__).resolve().parent


def module(filename):
    loader = importlib.machinery.SourceFileLoader('free_' + filename.replace('-', '_'), str(HERE / filename))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


def is_free(db, sid):
    if sid is None:
        return False
    try:
        with sqlite3.connect('file:%s?mode=ro' % os.path.abspath(db), uri=True) as cx:
            row = cx.execute('SELECT st.code FROM workouts w JOIN session_type st '
                             'ON st.id=w.session_type_id WHERE w.id=?', (sid,)).fetchone()
        return bool(row and row[0] == CODE)
    except sqlite3.Error:
        return False


def path_for(db, sid):
    root = Path(os.environ.get('LIFEKIT_HEALTH_STATE_DIR') or HERE.parent.parent / 'files/program')
    key = hashlib.sha256(os.path.realpath(db).encode()).hexdigest()[:16]
    return root / '.free-sessions' / ('%s-%s.json' % (key, int(sid)))


def effective_path(program, db, sid):
    if not is_free(db, sid):
        from session_day_trim import effective_path as planned_path
        return planned_path(program, db, sid)
    path = path_for(db, sid)
    if not path.exists():
        raise ValueError('Free session prescription missing: %s' % path)
    return str(path)


def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    os.replace(tmp, path)


def context(db, venue=None):
    plan = module('program-plan')
    # A fresh in-memory context: no load/save of the paused consult state.
    cx = plan.Ctx.__new__(plan.Ctx)
    cx.db = db
    cx._facts = cx._mmap = cx._holds = None
    venue = venue or plan.venue_record(db)[0]
    if not venue:
        raise ValueError('운동할 장소와 쓸 수 있는 기구를 알려 주세요.')
    cx.st = {'place': {'venue': venue}, 'structure': {'rotation': [CODE]},
             'safety_items': [{'site': site, 'side': side} for site, side, _ in plan.safety_rows(db)]}
    return plan, cx


def _norm(text):
    return ''.join(str(text or '').split()).lower()


# A bare gym lift name (the clean) whose only catalog rows are implement-
# qualified siblings (the one-arm kettlebell clean): in a gym the bare name is
# the barbell lift. Rehearsal S2 (2026-10-11): the near-miss branch answered
# "ask the owner which one" with the kettlebell clean as the only candidate, so
# a bare clean was never registered (all 3 runs). Words / id prefixes that only name the implement:
IMPLEMENT_WORDS_KO = ('\ubc14\ubca8', '\ucf00\ud2c0\ubca8', '\ub364\ubca8',
                      '\uc6d0\uc554', '\uc2f1\uae00\uc554', '\ud55c\ud314')
IMPLEMENT_PREFIXES = ('barbell_', 'kettlebell_', 'dumbbell_', 'one_arm_',
                      'single_arm_')
BARBELL_KO = '\ubc14\ubca8'


class NeedsRegister(ValueError):
    """An owner-named bare lift with no barbell row: register `spec`."""

    def __init__(self, raw, spec):
        self.raw, self.spec = raw, spec
        super().__init__(
            'NOT_IN_CATALOG %s -- the bare gym lift is the barbell one and is not '
            'catalogued yet. Run EXACTLY: session-open --free --register "%s" '
            '(or exercise-enter <sid> %s mid-session: it registers it). Never '
            'tell the owner it cannot be recorded.' % (raw, spec, raw))


def _base_id(name):
    changed = True
    while changed:
        changed = False
        for pre in IMPLEMENT_PREFIXES:
            if name.startswith(pre):
                name, changed = name[len(pre):], True
    return name


def bare_lift(raw, shown, catalog):
    """('name', catalog id) | ('register', spec) | None for an owner's bare
    lift name: every catalog row whose display is <implement words> + the
    name shares ONE base id -> its barbell row when catalogued, else the
    spec registering barbell_<base> modelled on the sibling."""
    words = str(raw or '').split()
    if not words or any(w in IMPLEMENT_WORDS_KO for w in words):
        return None
    want = _norm(raw)
    if not want or want.isascii():
        return None
    hits = {}
    for name, disp in shown.items():
        d = _norm(disp)
        if not d.endswith(want) or d == want:
            continue
        prefix = str(disp).split()
        tail = len(words)
        if len(prefix) <= tail or [_norm(w) for w in prefix[-tail:]] != [_norm(w) for w in words]:
            continue
        if all(w in IMPLEMENT_WORDS_KO for w in prefix[:-tail]):
            hits[name] = _base_id(name)
    if len(set(hits.values())) != 1:
        return None
    base = next(iter(hits.values()))
    target = 'barbell_' + base
    if target in catalog:
        return ('name', target)
    like = sorted(hits)[0]
    return ('register', '%s=%s@barbell:%s %s' % (target, like, BARBELL_KO,
                                                 ' '.join(words)))


def ensure_names(db, kit_life, names, dry_run=False):
    """Owner-named lifts -> catalog ids, registering a bare gym lift's
    barbell row (bare_lift) through the kit's exercise-add in this same call.
    Prints the REGISTERED line; any other name passes through unchanged
    (choices() resolves / refuses it)."""
    try:
        with sqlite3.connect('file:%s?mode=ro' % os.path.abspath(db), uri=True) as c:
            catalog = {r[0] for r in c.execute('SELECT exercise_name FROM ax_exercise')}
    except sqlite3.Error:
        return list(names)
    out = []
    for raw in names:
        try:
            out.append(resolve_name(raw, catalog))
        except NeedsRegister as need:
            name = parse_register(need.spec)[0]
            if dry_run or not kit_life:
                print('DRYRUN register=%s' % need.spec)
            else:
                print(register_lift(db, kit_life, need.spec))
                print('REGISTERED_FROM owner_word=%s as=%s -- the owner\'s bare "%s" '
                      'is the barbell lift; if they meant another implement, '
                      'exercise-enter that one instead' % (raw, name, raw))
            out.append(name)
        except ValueError:
            out.append(raw)
    return out


def resolve_name(raw, catalog):
    """An owner/agent-given lift name -> its catalog name.

    Rehearsal S2 (2026-10-10): `--exercises <Korean deadlift name>` failed on the
    display name, and a run then GUESSED a catalog id (registering a duplicate
    barbell_deadlift aliased to sumo). A catalog name passes through; a display
    name (the registered display, else the Korean name) resolves when exactly
    one catalog lift carries it; more than one is an error that lists the
    candidates; a near miss lists the close ones. Never a guess."""
    if raw in catalog:
        return raw
    from ui_labels import exercise_ko
    want = _norm(raw)
    shown = {}
    for name in catalog:
        disp = registered_display(name) or exercise_ko(name)
        if disp and disp != exercise_ko(None):
            shown[name] = disp
    exact = sorted(n for n, d in shown.items() if _norm(d) == want or _norm(n) == want)
    if len(exact) == 1:
        return exact[0]
    if len(exact) > 1:
        raise ValueError('AMBIGUOUS_NAME %s -- several catalog lifts carry this name: %s. '
                         'Ask the owner which one; never pick a catalog id yourself.'
                         % (raw, ', '.join('%s(%s)' % (n, shown[n]) for n in exact)))
    bare = bare_lift(raw, shown, catalog)
    if bare is not None and bare[0] == 'name':
        return bare[1]
    if bare is not None:
        raise NeedsRegister(raw, bare[1])
    near = sorted(n for n, d in shown.items()
                  if want and (want in _norm(d) or _norm(d) in want))
    if near:
        raise ValueError('NOT_IN_CATALOG %s -- no lift is named exactly that. Close catalog '
                         'lifts: %s. Ask the owner which one they mean (pass its catalog name); '
                         'never guess a catalog id or register a duplicate.'
                         % (raw, ', '.join('%s(%s)' % (n, shown[n]) for n in near[:8])))
    return raw


def choices(db, regions=(), names=(), venue=None):
    import compose_rank
    plan, cx = context(db, venue)
    pool = plan.candidates(cx)
    # Both the explicit lift lane and proposals use compose's caution filter.
    allowed = {c['name']: c for c in pool if not plan.loads_caution_area(cx, c['name'])}
    if names:
        known = {c['name'] for c in pool}
        names = [resolve_name(n, known | set(cx.facts())) for n in names]
        for name in names:
            if name not in known and name not in cx.facts():
                raise ValueError(
                    'NOT_IN_CATALOG %s -- register it in this same call: '
                    'session-open --free --register %s=<catalogued sibling>@<implement>:<display> '
                    '(e.g. barbell_clean=kettlebell_clean@barbell:<owner-facing name>). Never tell the '
                    'owner it cannot be recorded.' % (name, name))
            if name not in allowed:
                raise ValueError('Unavailable or caution-loaded exercise: ' + name)
        return [compose_rank.enrich(allowed[n]) for n in dict.fromkeys(names)]
    aliases = {'shoulder': 'shoulders', '어깨': 'shoulders', '가슴': 'chest',
               '삼두': 'triceps', 'arms': 'arms'}
    wanted = {aliases.get(r, r) for r in regions}
    if not wanted:
        return []
    ranked = compose_rank.for_context(cx, list(allowed.values()), vars(plan))
    selected = {}
    mapping = dict(plan.MUSCLE_REGION)
    for slot in ranked['sessions'][CODE]:
        for c in slot['shortlist']:
            muscles = set(c['primary'])
            if wanted & (muscles | {mapping.get(m) for m in muscles}):
                selected[c['name']] = c
    return sorted(selected.values(), key=lambda c: (-c['score'], c['name']))[:5]


# ---------------------------------------------------------------------------
# an owner-named lift that is not in the catalog (owner 2026-10-10 12:19:
# The agent answered that the barbell clean "is not in the list, so it cannot be
# recorded or prescribed"). Never refused:
# it is registered in the same turn through the kit's own exercise-add verb
# (movement / load_type / measure / pattern + muscle map, so fatigue and
# volume accounting work), modelled on a catalogued sibling, with the
# implement the owner named. Spec: NAME=LIKE[@EQUIPMENT][:DISPLAY], e.g.
# barbell_clean=kettlebell_clean@barbell:<owner-facing name>.
# ---------------------------------------------------------------------------
FREEWEIGHT_EQUIPMENT = ('barbell', 'dumbbell', 'kettlebell', 'ez_bar', 'trap_bar',
                        'smith_machine')


def names_path():
    root = Path(os.environ.get('LIFEKIT_HEALTH_STATE_DIR') or HERE.parent.parent / 'files/program')
    return root / '.registered-exercises.json'


def registered_display(name):
    try:
        return (json.loads(names_path().read_text()).get(name) or {}).get('display')
    except (OSError, ValueError, AttributeError):
        return None


def parse_register(spec):
    import re
    m = re.match(r'^([a-z0-9_]+)=([a-z0-9_]+)(?:@([a-z_]+))?(?::(.+))?$', spec.strip())
    if not m:
        raise ValueError('register spec is NAME=LIKE[@EQUIPMENT][:DISPLAY]: %r' % spec)
    return m.group(1), m.group(2), m.group(3), (m.group(4) or '').strip() or None


def register_lift(db, kit_life, spec):
    """Register one uncatalogued lift through `kit_life.sh exercise-add`.
    Returns the machine line; an already-catalogued name is a no-op."""
    import subprocess
    name, like, equipment, display = parse_register(spec)
    with sqlite3.connect('file:%s?mode=ro' % os.path.abspath(db), uri=True) as c:
        if c.execute('SELECT 1 FROM ax_exercise WHERE exercise_name=?', (name,)).fetchone():
            return 'REGISTERED %s existing=yes' % name
        base = c.execute('SELECT movement, measure, load_type FROM ax_exercise '
                         'WHERE exercise_name=?', (like,)).fetchone()
        if base is None:
            raise ValueError('register: the model lift %s is not in the catalog' % like)
        pattern = c.execute('SELECT pattern FROM exercise_pattern WHERE exercise_name=?',
                            (like,)).fetchone()
        muscles = c.execute('SELECT muscle, role FROM exercise_muscle_map '
                            'WHERE exercise_name=?', (like,)).fetchall()
        grip = c.execute('SELECT movement, equipment, grip FROM exercise_movement_grip '
                         'WHERE exercise_name=?', (like,)).fetchone()
        cost = c.execute('SELECT cost FROM exercise_fatigue_cost WHERE exercise_name=?',
                         (like,)).fetchone()
    movement, measure, load_type = base
    if equipment in FREEWEIGHT_EQUIPMENT:
        load_type = 'freeweight'
    if load_type in ('machine', 'cable'):
        raise ValueError('register: a machine/cable lift names its machine '
                         '(machine-register first)')
    if not muscles or not pattern:
        raise ValueError('register: %s has no muscle map / pattern to model on' % like)
    argv = [kit_life, 'exercise-add', '--name', name, '--movement', movement,
            '--measure', measure or 'reps', '--load-type', load_type,
            '--pattern', pattern[0], '--new-confirmed']
    for muscle, role in muscles:
        argv += ['--muscle', '%s:%s' % (muscle, role)]
    if cost:
        argv += ['--cost', cost[0]]
    r = subprocess.run(argv, capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        raise ValueError('register: exercise-add refused %s: %s'
                         % (name, (r.stderr or r.stdout).strip()[-300:]))
    # The pack-owned facts row: which implement (candidates() filters the
    # venue's equipment on it) and the movement key the e1RM ratios read.
    with sqlite3.connect(db) as c:
        c.execute('INSERT OR REPLACE INTO exercise_movement_grip(exercise_name, movement, '
                  'equipment, grip) VALUES(?,?,?,?)',
                  (name, grip[0] if grip else movement, equipment or (grip[1] if grip else None),
                   grip[2] if grip else None))
    try:
        data = json.loads(names_path().read_text())
    except (OSError, ValueError):
        data = {}
    data[name] = {'like': like, 'equipment': equipment, 'display': display}
    save(names_path(), data)
    return ('REGISTERED %s like=%s equipment=%s map=%s -- confirm in ONE line that '
            'the lift (%s) is now on record and is prescribed and recorded as usual, '
            'then prescribe and record it normally'
            % (name, like, equipment or '-', ','.join('%s:%s' % m for m in muscles),
               display or name))


def slot(db, candidate, number, sid=None):
    import compose_rank
    c = compose_rank.enrich(candidate)
    name = c['name']
    with sqlite3.connect(db) as cx:
        row = cx.execute('SELECT ws.weight_kg FROM workout_sets ws JOIN workouts w '
                         'ON w.id=ws.session_id WHERE ws.exercise_name=? AND ws.set_seq>0 '
                         'AND ws.weight_kg IS NOT NULL AND (? IS NULL OR w.id!=?) '
                         'ORDER BY w.date DESC,w.id DESC,ws.set_seq DESC LIMIT 1',
                         (name, sid, sid)).fetchone()
    from ui_labels import exercise_ko
    out = dict(slot=number, name=name, display=registered_display(name) or exercise_ko(name),
               sets=DEFAULT_SETS, rep_range=list(DEFAULT_REPS),
               weight_kg=row[0] if row else None, progression='double')
    if 'free_compound' in c['tags']:
        out['rir_floor'] = DEFAULT_RIR_FLOOR
    if fixed_implement(name):
        # owner 2026-10-10 13:58: kettlebell swing 12kg x 40 x 3. The bell is
        # the load and the reps are the dose: a high band, no calibration
        # ramp (a 40-rep set is not a "too light" warm-up rung).
        out['rep_range'] = list(FIXED_IMPLEMENT_REPS)
        out['fixed_implement'] = True
        out.pop('rir_floor', None)
    return out


# Reps band of a lift whose implement IS the load (compose_rank_rules
# muscle_credit: loaded == bodyweight > 0 -- swing, kettlebell clean, slams):
# owner-named in a free session it is dosed by reps, not by load.
FIXED_IMPLEMENT_REPS = (10, 40)


def fixed_implement(name):
    try:
        import compose_rank
        ex = (compose_rank.shared_rules().get('muscle_credit') or {}).get('exercises') or {}
        row = ex.get(name) or {}
        return bool(row) and row.get('loaded') == row.get('bodyweight') and (row.get('loaded') or 0) > 0
    except Exception:  # noqa: BLE001
        return False


def enter(program, db, sid, name):
    return enter_named(program, db, sid, name)[0]


def enter_named(program, db, sid, name, kit_life=None):
    """(effective program path, catalog name). A free session appends an
    owner-named lift (display name resolved; a bare gym lift's barbell row
    registered when kit_life is given)."""
    path = effective_path(program, db, sid)
    if not is_free(db, sid):
        return path, name
    data = json.loads(Path(path).read_text())
    if kit_life:
        name = ensure_names(db, kit_life, [name])[0]
    # Recheck active safety on every entry, including a previously chosen lift.
    candidate = choices(db, names=[name], venue=data.get('free_venue'))[0]
    name = candidate['name']
    slots = data['days'][CODE]['exercises']
    if not any(s['name'] == name for s in slots):
        slots.append(slot(db, candidate, len(slots) + 1, sid))
        refresh_prep(data, db, data.get('_source') or program)
        save(path, data)
    return path, name


GYM_STANDARD_LOADED = ('machine', 'cable', 'dumbbell', 'barbell',
                       'kettlebell_or_dumbbell')


def owner_prep(program, load_yaml=None):
    """The owner's prep.yaml beside the program card ({} when absent)."""
    path = Path(program).parent / 'prep.yaml'
    if not path.is_file():
        return {}
    try:
        data = (load_yaml or module('rx-calc').load_yaml)(str(path))
    except Exception:  # noqa: BLE001 -- a bad edit degrades to the pack doses
        return {}
    return data if isinstance(data, dict) else {}


def _dose(plan, code, owned):
    """The day-item dose: the owner's own (first prep.yaml day that lists
    the drill), else the pack's first-plan dose -- prep_file_text's rule."""
    for day in (owned.get('days') or {}).values():
        for block in ('prep', 'cooldown'):
            for it in ((day or {}).get(block) or []) if isinstance(day, dict) else []:
                if isinstance(it, dict) and it.get('code') == code:
                    return {k: it[k] for k in ('target_reps', 'target_unit', 'hold_sec')
                            if it.get(k) is not None}
    import re
    dose = plan.MC.MOVEMENTS[code]['dose']
    number = int(re.search(r'\d+', dose).group())
    if '\ucd08' in dose:            # seconds
        return {'target_reps': 1, 'target_unit': 'hold_sets', 'hold_sec': number}
    return {'target_reps': number,
            'target_unit': 'per_side' if '\uc88c\uc6b0' in dose else 'reps'}  # per side


def prep_day(db, slots, venue=None, program=None):
    """{'prep': [...], 'cooldown': [...], 'drills': {...}} for a free session:
    the SAME composer the planned program's prep.yaml was written by
    (program-plan prep_for_lifts + compose_draft.cooldown_for_lifts), on
    today's lifts. Owner 2026-10-10: a free session gets the mat prep and the
    cooldown stretch a planned session gets.

      * mat drills are session prep (phase mat_prep, no live_slot);
      * a drill that needs a gym tool (machine / cable / dumbbell / barbell /
        kettlebell) is EQUIPMENT prep (zone equipment), hosted on a lift
        (live_slot) so it runs after the mat drills, right before that lift
        -- it is never labelled mat;
      * caution_policy.lift_triggers: a drill tied to a lift pattern (the
        adduction machine before a squat) is served only with such a lift,
        on the first one; none in the session -> not served;
      * `drills` = catalog rows for codes the owner's prep.yaml lacks (the
        owner's own rows always win)."""
    names = [s['name'] for s in slots]
    if not names:
        return {'prep': [], 'cooldown': [], 'drills': {}}
    plan, cx = context(db, venue)
    import compose_draft
    import compose_rank
    pol = compose_rank.shared_rules()['caution_policy']
    triggers = pol.get('lift_triggers') or {}
    owned = owner_prep(program) if program else {}
    gloss = owned.get('drills') if isinstance(owned.get('drills'), dict) else {}
    with sqlite3.connect('file:%s?mode=ro' % os.path.abspath(db), uri=True) as c:
        marks = ','.join('?' for _ in names)
        pattern = dict(c.execute('SELECT exercise_name, pattern FROM exercise_pattern '
                                 'WHERE exercise_name IN (%s)' % marks, names))
    lifts = [{'name': n} for n in names]
    prep, drills = [], {}
    for code in plan.prep_for_lifts(cx, lifts):
        item = {'code': code}
        trig = triggers.get(code)
        if trig:
            host = next((s for s in slots if pattern.get(s['name']) in trig['patterns']), None)
            if host is None:
                continue
            item['live_slot'] = host['slot']
        if plan.drill_class(code) in GYM_STANDARD_LOADED:
            item['zone'] = 'equipment'
            item.setdefault('live_slot', slots[0]['slot'])
        item.update(_dose(plan, code, owned))
        prep.append(item)
        drills[code] = code
    cooldown = []
    for code in compose_draft.cooldown_for_lifts(plan, cx, lifts):
        item = {'code': code}
        item.update(_dose(plan, code, owned))
        cooldown.append(item)
        drills[code] = code
    extra = {}
    for code in drills:
        if code in gloss or code not in plan.MC.MOVEMENTS:
            continue
        mv = plan.MC.MOVEMENTS[code]
        extra[code] = {'name': code, 'display': mv['ko'], 'zone': plan.drill_zone(code),
                       'howto': mv['how']}
        if mv['category'] == 'stretch':
            extra[code]['timing'] = 'cooldown'
    return {'prep': prep, 'cooldown': cooldown, 'drills': extra}


def refresh_prep(data, db, program):
    """Recompose the free day's prep for its current lineup (best-effort:
    a prep miss never blocks the session)."""
    try:
        data['prep_day'] = prep_day(db, data['days'][CODE]['exercises'],
                                    data.get('free_venue'), program)
    except Exception as exc:  # noqa: BLE001
        print('WARN free prep unavailable (session unaffected): %s' % exc)
    data['_source'] = str(program)
    return data


def free_prep(program_path, load_yaml=None):
    """load_prep's view of a free-session file: the owner's prep.yaml with
    the free day composed in, or None when `program_path` is not one."""
    p = Path(program_path)
    if p.parent.name != '.free-sessions' or not p.is_file():
        return None
    try:
        data = json.loads(p.read_text())
    except (OSError, ValueError):
        return None
    pd = data.get('prep_day')
    if not isinstance(pd, dict):
        return None
    src = data.get('_source')
    owned = owner_prep(src, load_yaml) if src else {}
    out = dict(owned)
    drills = dict(pd.get('drills') or {})
    drills.update(owned.get('drills') or {})
    out['drills'] = drills
    days = dict(owned.get('days') or {})
    days[CODE] = {'prep': pd.get('prep') or [], 'cooldown': pd.get('cooldown') or []}
    out['days'] = days
    return out


def register(db):
    """Insert registry DATA only; existing kit schema, no migration/retirement."""
    with sqlite3.connect(db) as cx:
        row = cx.execute('SELECT id FROM routine WHERE name=? AND status=?',
                         ('free-session', 'off-plan')).fetchone()
        rid = row[0] if row else cx.execute(
            'INSERT INTO routine(name,style,status,note) VALUES(?,?,?,?)',
            ('free-session', 'free', 'off-plan', 'Off-plan sessions; excluded from rotation')).lastrowid
        cx.execute('INSERT OR IGNORE INTO session_type(routine_id,code,display_name,sort,note) '
                   'VALUES(?,?,?,?,?)', (rid, CODE, CODE, 99, 'Off-plan session'))
        cx.execute('INSERT OR IGNORE INTO workout_types(category,subtype,sort) VALUES(?,?,?)',
                   ('근력', CODE, 99))
        return cx.execute('SELECT id FROM session_type WHERE routine_id=? AND code=?', (rid, CODE)).fetchone()[0]


def ensure_install():
    """The install-completion lane the planned path reaches through
    session-ensure.sh (taxonomy, program registry, set-keyboard flag). The
    free path never ran it, so a fresh state dir opened with keyboards OFF
    (2026-10-08, 2026-10-10). Best-effort: it never gates the open."""
    if os.environ.get('WARG_HEALTH_INSTALL_CHAIN'):
        return 'chained'
    script = HERE.parent.parent / 'routines' / 'bundle' / 'health-install-ensure.sh'
    if not os.access(str(script), os.X_OK):
        return 'absent'
    import subprocess
    env = dict(os.environ, WARG_HEALTH_INSTALL_CHAIN='1')
    try:
        r = subprocess.run([str(script), '--quiet'], capture_output=True,
                           text=True, timeout=60, env=env)
    except (OSError, subprocess.SubprocessError):
        return 'error'
    for line in r.stdout.splitlines():
        if (line.startswith(('KEYBOARD\t', 'TAXONOMY\t'))
                and '\tskipped' not in line):
            print('INSTALL_ENSURE ' + line.replace('\t', ' '))
    return 'ran'


def open_free(opener, args, db, program, date):
    for spec in getattr(args, 'register', None) or ():
        if args.dry_run:
            print('DRYRUN register=%s' % spec)
            continue
        print(register_lift(db, args.kit_life, spec))
    regions = [r.strip() for r in (args.regions or '').split(',') if r.strip()]
    names = [n.strip() for n in (args.exercises or '').split(',') if n.strip()]
    names = ensure_names(db, args.kit_life, names, dry_run=args.dry_run)
    picked = choices(db, regions, names, args.venue) if regions or names else []
    if regions and not picked:
        raise ValueError('No safe catalog proposals for these regions')
    data = {'session_mode': 'free', 'rotation': [CODE], 'free_venue': args.venue,
            'days': {CODE: {'exercises': [slot(db, c, i + 1) for i, c in enumerate(picked)]}}}
    refresh_prep(data, db, program)
    care = _program_care(program)
    if care:
        data['care'] = care
    if args.dry_run:
        print('DRYRUN session_class=free rotation_day=NONE')
        print(json.dumps(data, ensure_ascii=False))
        return 0
    ensure_install()
    # Idempotent while active. Never reconcile a free open into a planned row.
    cursor = module('session-cursor')
    active = cursor.marker_read(args.marker)
    if active and is_free(db, active):
        with sqlite3.connect(db) as cx:
            same_date = cx.execute('SELECT date FROM workouts WHERE id=?', (active,)).fetchone()[0] == date
        if same_date and module('session-closeout').read_closed_tombstone(args.tombstone) != active:
            print('OPENED session_id=%s created=existing session_class=free rotation_day=NONE' % active)
            return 0
    type_id = register(db)
    sid, created, err = opener.open_workout_row(args.kit_life, date, CODE, args.minutes,
                                               args.kcal, args.note, force_new=True)
    if sid is None:
        raise ValueError(err)
    # The tag is mandatory: an untagged free row would contaminate rotation.
    with sqlite3.connect(db) as cx:
        cx.execute('UPDATE workouts SET session_type_id=? WHERE id=?', (type_id, sid))
    path = path_for(db, sid)
    save(path, data)
    # The open moment, as the planned open stamps it: without it the
    # close-out's minutes ran from the FIRST RECORDED SET (owner 2026-10-10:
    # 22 minutes for a ~100-minute session).
    try:
        import session_clock
        session_clock.stamp_open(sid, sd=opener.STATE_DIR)
    except Exception:  # noqa: BLE001 -- the first row stands in for it
        pass
    opener.set_marker(args.marker, sid, args.tombstone)
    opener.clear_pending_markers(sid)
    # The planned open's steps 6-7, through the SAME functions: the table-3 pin
    # switches from the workbench to the session card and the lineup card
    # lands in chat before the first question (owner 2026-10-10: the free
    # session left the workbench pinned and rendered no exercise card).
    verdict = {'session_class': 'free', 'rotation_day': CODE}
    card = []
    pin = opener.write_start_pin(str(path), verdict, db_path=db, session_id=sid,
                                 card_out=card)
    card_result = opener.deliver_start_card(card, sid)
    opener.start_flow_ledger(sid, db, program, free=True)
    print('OPENED session_id=%s created=%s session_class=free rotation_day=NONE tag=applied '
          'start_pin=%s start_card=%s' % (sid, created, pin, card_result))
    print(json.dumps(data, ensure_ascii=False))
    print(lineup_line(sid, data))
    opener.emit_start_lines(opener.care_lines(str(path), CODE), card_result)
    return 0


def lineup_line(sid, data):
    """Rehearsal S2 (2026-10-11): the owner named a deadlift and a clean; the
    open carried the deadlift only and the clean was promised "later" and
    never registered (3/3). The open names its lineup and the exact verb for
    an owner-named lift that is not in it."""
    lifts = ['%s(%s)' % (s['name'], s.get('display') or s['name'])
             for s in data['days'][CODE]['exercises']]
    return ('LINEUP %s -- today\'s lifts. EVERY lift the owner named must be '
            'here: one missing (any name, catalogued or not) -> run '
            '`service/health/exercise-enter %s <owner\'s word>` THIS turn, before '
            'the reply (it resolves the name or registers the lift). Never a '
            'memo, never "later".' % (', '.join(lifts) or 'none', sid))


def _program_care(program):
    """The program card's `care:` lines (what every session carries beyond
    the lifts), or None. A free session serves them too."""
    try:
        if not program or not Path(program).is_file():
            return None
        card = module('rx-calc').load_yaml(str(program))
        return (card or {}).get('care') if isinstance(card, dict) else None
    except Exception:  # noqa: BLE001
        return None


def history_result(db, name, sid):
    """Prior working history across plans; calibration stays unknown otherwise."""
    with sqlite3.connect(db) as cx:
        row = cx.execute('SELECT ws.reps,ws.weight_kg FROM workout_sets ws JOIN workouts w '
                         'ON w.id=ws.session_id WHERE ws.exercise_name=? AND ws.set_seq>0 '
                         'AND ws.weight_kg IS NOT NULL AND (? IS NULL OR w.id!=?) '
                         'ORDER BY w.date DESC,w.id DESC,ws.set_seq DESC LIMIT 1',
                         (name, sid, sid)).fetchone()
        if row:
            return tuple(row)
        # The owner-reported calibration seeds this session, without progression.
        row = cx.execute('SELECT weight_kg FROM workout_sets WHERE session_id=? '
                         'AND exercise_name=? AND set_seq>0 AND weight_kg IS NOT NULL '
                         'ORDER BY set_seq LIMIT 1', (sid, name)).fetchone()
        return None, row[0] if row else None
