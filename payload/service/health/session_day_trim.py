"""Freeze a weekday's reduced lineup per session, leaving the queue intact."""
import copy
import datetime
import hashlib
import json
import math
import os
from pathlib import Path

WEEKDAYS = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')


def validate_time_plan(plan):
    if plan is None:
        return
    if not isinstance(plan, dict):
        raise ValueError('time_plan must be an object')
    caps = plan.get('lift_minutes', {})
    if not isinstance(caps, dict):
        raise ValueError('time_plan.lift_minutes must be a weekday map')
    for day, minutes in caps.items():
        if (day not in WEEKDAYS or isinstance(minutes, bool)
                or not isinstance(minutes, (int, float))
                or not math.isfinite(minutes) or minutes < 0):
            raise ValueError('time_plan.lift_minutes needs nonnegative finite minutes')


def path_for(db, sid):
    root = Path(os.environ.get('LIFEKIT_HEALTH_STATE_DIR') or
                Path(__file__).resolve().parents[2] / 'files/program')
    key = hashlib.sha256(os.path.realpath(db).encode()).hexdigest()[:16]
    return root / '.day-trim' / ('%s-%s.json' % (key, int(sid)))


def effective_path(program, db, sid):
    if sid is None:
        return program
    path = path_for(db, sid)
    return str(path) if path.is_file() else program


def source_path(program):
    """Ancillary prep/history files remain beside the original program."""
    if program and Path(program).parent.name == '.day-trim':
        data = json.loads(Path(program).read_text())
        return data['_day_trim']['source']
    return program


def trimmed_program(program, day, date, rx):
    """Return (copy, removed names, budget); None budget means no decision."""
    import compose_rank
    plan = program.get('time_plan') or {}
    validate_time_plan(plan)
    weekday = WEEKDAYS[datetime.date.fromisoformat(date).weekday()]
    cap = (plan.get('lift_minutes') or {}).get(weekday)
    if plan.get('status') != 'set' or plan.get('pick') != 'shrink' or cap is None:
        return program, [], None
    result = copy.deepcopy(program)
    slots = rx.order_day_exercises(
        ((result.get('days') or {}).get(day) or {}).get('exercises') or [])
    if not slots:
        return result, [], cap
    costs = []
    for slot in slots:
        candidate = compose_rank.enrich(slot)
        if slot['name'] not in compose_rank.CATALOG_FACTS:
            candidate['tags'] = [rx.movement_class(slot['name'])]
        costs.append(compose_rank.session_minutes([candidate]))
    removed = []
    while slots and sum(costs) > cap:
        removed.append(slots.pop()['name'])
        costs.pop()
    result['days'][day]['exercises'] = slots
    return result, removed, cap


def prepare(program_path, db, sid, date, verdict, rx, allow_new=True):
    """Snapshot once, including ample-time decisions, so reopen is stable."""
    path = path_for(db, sid)
    if path.exists():
        return str(path)
    if not allow_new:
        return program_path
    if verdict.get('provisional') or verdict.get('session_class') != 'regular':
        return program_path
    program = rx.load_yaml(program_path)
    result, removed, cap = trimmed_program(
        program, verdict.get('rotation_day'), date, rx)
    if cap is None and (program.get('time_plan') or {}).get('pick') != 'shrink':
        return program_path
    result['_day_trim'] = dict(source=os.path.abspath(program_path), date=date,
                               day=verdict['rotation_day'], budget=cap,
                               removed=removed)
    # Use the existing atomic prescription writer; no DB/schema mutation.
    from free_session import save
    save(path, result)
    return str(path)
