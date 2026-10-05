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


def choices(db, regions=(), names=(), venue=None):
    import compose_rank
    plan, cx = context(db, venue)
    pool = plan.candidates(cx)
    # Both the explicit lift lane and proposals use compose's caution filter.
    allowed = {c['name']: c for c in pool if not plan.loads_caution_area(cx, c['name'])}
    if names:
        for name in names:
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
    out = dict(slot=number, name=name, display=exercise_ko(name),
               sets=DEFAULT_SETS, rep_range=list(DEFAULT_REPS),
               weight_kg=row[0] if row else None, progression='double')
    if 'free_compound' in c['tags']:
        out['rir_floor'] = DEFAULT_RIR_FLOOR
    return out


def enter(program, db, sid, name):
    path = effective_path(program, db, sid)
    if not is_free(db, sid):
        return path
    data = json.loads(Path(path).read_text())
    # Recheck active safety on every entry, including a previously chosen lift.
    candidate = choices(db, names=[name], venue=data.get('free_venue'))[0]
    slots = data['days'][CODE]['exercises']
    if not any(s['name'] == name for s in slots):
        slots.append(slot(db, candidate, len(slots) + 1, sid))
        save(path, data)
    return path


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


def open_free(opener, args, db, program, date):
    regions = [r.strip() for r in (args.regions or '').split(',') if r.strip()]
    names = [n.strip() for n in (args.exercises or '').split(',') if n.strip()]
    picked = choices(db, regions, names, args.venue) if regions or names else []
    if regions and not picked:
        raise ValueError('No safe catalog proposals for these regions')
    data = {'session_mode': 'free', 'rotation': [CODE], 'free_venue': args.venue,
            'days': {CODE: {'exercises': [slot(db, c, i + 1) for i, c in enumerate(picked)]}}}
    if args.dry_run:
        print('DRYRUN session_class=free rotation_day=NONE')
        print(json.dumps(data, ensure_ascii=False))
        return 0
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
    save(path_for(db, sid), data)
    opener.set_marker(args.marker, sid, args.tombstone)
    opener.clear_pending_markers(sid)
    print('OPENED session_id=%s created=%s session_class=free rotation_day=NONE tag=applied' % (sid, created))
    print(json.dumps(data, ensure_ascii=False))
    return 0


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
