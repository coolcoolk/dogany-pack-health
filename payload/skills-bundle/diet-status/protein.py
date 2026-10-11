#!/usr/bin/env python3
"""
PROTEIN NUDGE -- the engine half of the retro's protein line.

WHY (worklog 2026-08-15-protein-coaching-dynamic, owner 2026-08-15:
"수면 패턴 고려 마지막 단백질 채우는 시간 / 부족 큰 날 프로틴 한 스쿱 (자원
있으면)"). The retro used to say a static "단백질 목표 160g". The instance-local
rebuild of this nudge was never carried into the pack, so it is rebuilt here,
engine-first: every number and the one sentence come out of this file; the
retro provider (service/health/protein-retro) and the model only carry `line`.

NOTHING HARDCODED AS A GRAM THRESHOLD (owner rule). "Short enough to nudge"
is derived from three inputs, each from its own source:

  weight     kit body stats (weight_kg). Not stored -> silent: a threshold
             built on the code default 70 kg would be a guess.
  program    the kit's balance (deficit_kcal - surplus_kcal): cut / maintain /
             bulk. Also already inside the day's protein target and eff_goal.
  kcal left  card.py day_state(): the SAME target the card draws (carry, burn,
             G6 floor included).

  shortfall     = protein target - protein eaten
  natural_fill  = what the calories still left would bring if eaten at the
                  day's own planned protein share (target*4 / eff_goal)
  gap           = shortfall - natural_fill   (what ordinary eating will NOT
                  close tonight)
  tolerance     = weight x TOLERANCE_G_PER_KG

  shortfall <= 0          met       one light line (달성)
  gap <= tolerance        on_track  one light line: the meals left cover it
  otherwise               short     the nudge (scoop if owned, else food)
  short, past last call   late      no cramming; a small capped carry

PER-MEAL SPLIT / PER-DAY CAP. The day's TOTAL is what counts; timing and
splitting fade once it is matched (kimwog nutrition/protein-timing-total-
matched). 0.4 g/kg a meal is a SPLIT TARGET -- four meals of it make 1.6
g/kg a day -- and 0.55 g/kg is 2.2 g/kg over the same four meals (Schoenfeld
& Aragon 2018, J Int Soc Sports Nutr 15:10). Neither is an absorption limit:
a bigger meal is not wasted, and no sentence here may say it is. A nudge asks
for at most one meal's share only because one meal is what a person can act
on tonight (a tractability convention).
The day cap is a product choice, not a measured ceiling. Outside a cut it is
2.2 g/kg, the upper CI of Morton et al. 2018's non-significant plateau (Br J
Sports Med 52:376). In a cut the evidence band for a trained lifter is
1.6-2.4 g/kg (kimwog nutrition/protein-deficit-trained-lifter: Hector &
Phillips 2018; Longland 2016's 2.4 arm), so a cut day's goal is honoured up
to 2.4 g/kg and a goal under the 1.6 floor is flagged (`below_cut_floor`),
never silently raised -- the goal stays the one the card draws. A missed
amount carries to tomorrow only as a SMALL capped top-up (CARRY_G_PER_KG,
never past the day cap), never as the whole debt.

FAT-FREE MASS. The 2.3-3.1 figure (Helms 2014) is per kg of FAT-FREE mass;
it is reported (`ffm_band_g`) only when the owner's body fat is on record
(kit fat_mass_kg stored, not the code default). Unknown body fat -> the
body-weight band alone.

KIDNEYS. A known kidney condition (kit config `renal_condition` set to
anything but none / healthy) withdraws the cut band: no 2.4 allowance, no
band or FFM figure (KDIGO 2024 PP 3.3.2 -- avoid > 1.3 g/kg/day in CKD at
risk of progression; that number is the clinician's to set). Unknown is the
baseline (no known condition), not a block.

LAST CALL. Back-computed from the owner's bedtime (kit life skeleton,
`life_skeleton_weekday_bed` / `_weekend_bed`; which one = whether TOMORROW is
a work day, `life_skeleton_work_days`, default Mon-Fri). Minus a digestion
margin: a shake 60 min, solid food 120 min (late meals within ~3 h of lying
down raise reflux risk -- Fujiwara et al. 2005, Am J Gastroenterol
100:2633). Bedtime not captured -> no time is spoken, never a guessed one.

PROTEIN RESOURCE (owner ruling: never push a resource the owner does not have). A scoop is proposed
only when the owner has one: an active kit ledger_resource kind='supplement'
row that is a protein (detail.protein_g, or a protein name), or a protein
shake logged at least twice in the window (consult-conduct's supplement
stack: supplement-classified meals + ledger_resource). Grams per scoop from
the row's detail, else the owner's own typical logged serving; unknown ->
the scoop is named without a number. No resource -> the food fallback is the
top protein item of suggest.py's shortlist (foods the owner actually eats).

Read-only: never writes a meal, a config key or a resource row.

Usage:
  protein.py [--date YYYY-MM-DD] [--at HH:MM] [--carry-kcal N]
Prints one JSON object (`status`, numbers, `line`). Exit 0 whenever the read
succeeded; "nothing to say" is a status (silent_*), never an exit code.
"""
import argparse
import datetime
import importlib.util
import json
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))

PER_MEAL_G_PER_KG = 0.4          # one meal's share: 1.6 g/kg over 4 meals (a split target)
PER_MEAL_G_PER_KG_CUT = 0.55     # one meal's share in a deficit: 2.2 g/kg over 4 meals
DAY_CAP_G_PER_KG = 2.2           # product day cap outside a cut (Morton 2018 upper CI)
CUT_DAY_CAP_G_PER_KG = 2.4       # cut band top (deficit-trained-lifter; Hector & Phillips 2018)
CUT_FLOOR_G_PER_KG = 1.6         # cut band floor: a lower goal is flagged, not raised
FFM_BAND_G_PER_KG = (2.3, 3.1)   # Helms 2014, per kg FAT-FREE mass, cut only
RENAL_CLEAR = ('', 'none', 'healthy', 'unknown')   # renal_condition values that keep the cut band
CARRY_G_PER_KG = 0.2             # the most a missed amount moves to tomorrow
TOLERANCE_G_PER_KG = 0.1         # below this the gap is noise, not a nudge
SHAKE_MARGIN_MIN = 60            # last shake before bed
FOOD_MARGIN_MIN = 120            # last solid meal before bed
HISTORY_MIN_TIMES = 2            # a shake logged this often = owned
PROTEIN_NAME = re.compile(r'프로틴|단백질\s*(파우더|쉐이크|셰이크)|웨이|카제인|'
                          r'쉐이크|셰이크|protein|whey|casein|shake', re.I)
WEEK = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
DEFAULT_WORK_DAYS = WEEK[:5]


def _sibling(name):
    """card.py / suggest.py beside this file, by path, no bytecode (the
    residue rule card.py's own _sibling follows)."""
    mod = sys.modules.get('dietstatus_' + name)
    if mod is not None:
        return mod
    prev = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        spec = importlib.util.spec_from_file_location(
            'dietstatus_' + name, os.path.join(_HERE, name + '.py'))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod
    finally:
        sys.dont_write_bytecode = prev


# -- pure pieces (unit-tested directly) ---------------------------------------
def program_of(stats):
    bal = float(stats.get('deficit_kcal') or 0) - float(stats.get('surplus_kcal') or 0)
    return 'cut' if bal > 0 else 'bulk' if bal < 0 else 'maintain'


def renal_known(stats):
    """True when the kit records a kidney condition (anything but none /
    healthy / unknown in `renal_condition`): the cut band is withdrawn."""
    return str((stats or {}).get('renal_condition') or '').strip().lower() \
        not in RENAL_CLEAR


def ffm_kg(stats, weight_kg):
    """Fat-free mass from the owner's own body-fat record, else None. The
    kit's code-default fat_mass_kg (`_defaults_used`) is not a record."""
    stats = stats or {}
    used = stats.get('_defaults_used') or ()
    fat = stats.get('fat_mass_kg')
    if fat is None or 'fat_mass_kg' in used:
        return None
    ffm = float(weight_kg) - float(fat)
    return ffm if 0 < ffm < float(weight_kg) else None


def caps(weight_kg, program, renal=False):
    cut = program == 'cut' and not renal
    per_meal = weight_kg * (PER_MEAL_G_PER_KG_CUT if program == 'cut'
                            else PER_MEAL_G_PER_KG)
    return {'per_meal_g': round(per_meal),
            'day_cap_g': round(weight_kg * (CUT_DAY_CAP_G_PER_KG if cut
                                            else DAY_CAP_G_PER_KG)),
            'carry_cap_g': round(weight_kg * CARRY_G_PER_KG),
            'tolerance_g': round(weight_kg * TOLERANCE_G_PER_KG)}


def cut_band(weight_kg, program, renal=False, ffm=None):
    """The cut-day band figures, or {} (not a cut / kidney condition known).
    The fat-free-mass band only with a body-fat record."""
    if program != 'cut' or renal:
        return {}
    out = {'cut_band_g': [round(weight_kg * CUT_FLOOR_G_PER_KG),
                          round(weight_kg * CUT_DAY_CAP_G_PER_KG)]}
    if ffm:
        out['ffm_band_g'] = [round(ffm * FFM_BAND_G_PER_KG[0]),
                             round(ffm * FFM_BAND_G_PER_KG[1])]
    return out


def assess(state, weight_kg, program, renal=False, ffm=None):
    """day_state x weight x program -> the tier and its numbers. Pure.
    `renal`: a known kidney condition (no cut band); `ffm`: fat-free mass kg
    from a body-fat record, else None."""
    c = caps(weight_kg, program, renal)
    goal = min(float(state['protein_goal_g']), c['day_cap_g'])
    eaten = float(state['protein_g'])
    short = goal - eaten
    eff = float(state['eff_goal'] or 0)
    share = (goal * 4.0 / eff) if eff > 0 else 0.0
    natural = max(0.0, float(state['remaining_kcal'])) * share / 4.0
    gap = short - natural
    if short <= 0:
        tier = 'met'
    elif gap <= c['tolerance_g']:
        tier = 'on_track'
    else:
        tier = 'short'
    fill = min(max(gap, 0.0), c['per_meal_g'])
    carry = min(max(short, 0.0), c['carry_cap_g'], max(0.0, c['day_cap_g'] - goal))
    band = cut_band(weight_kg, program, renal, ffm)
    if band:
        band['below_cut_floor'] = goal < band['cut_band_g'][0]
    return dict(c, tier=tier, program=program, goal_g=round(goal),
                eaten_g=round(eaten), shortfall_g=round(max(short, 0.0)),
                natural_fill_g=round(natural), gap_g=round(max(gap, 0.0)),
                fill_g=round(fill), carry_g=round(carry),
                renal_gate=bool(renal), **band)


def _hm(s):
    m = re.match(r'^\s*(\d{1,2}):(\d{2})\s*$', str(s or ''))
    if not m or int(m.group(1)) > 23 or int(m.group(2)) > 59:
        return None
    return int(m.group(1)), int(m.group(2))


def bedtime(skeleton, day):
    """The night of `day`: weekday bedtime when TOMORROW is a work day, else
    weekend; either missing -> the other; both -> None. A bedtime before noon
    (01:00) is after midnight: it lands on the next calendar day."""
    wd = [d.strip() for d in (skeleton.get('life_skeleton_work_days') or '').split(',')
          if d.strip() in WEEK] or list(DEFAULT_WORK_DAYS)
    tomorrow = WEEK[(day.weekday() + 1) % 7]
    first, second = (('life_skeleton_weekday_bed', 'life_skeleton_weekend_bed')
                     if tomorrow in wd else
                     ('life_skeleton_weekend_bed', 'life_skeleton_weekday_bed'))
    hm = _hm(skeleton.get(first)) or _hm(skeleton.get(second))
    if hm is None:
        return None
    at = datetime.datetime.combine(day, datetime.time(*hm))
    if hm[0] < 12:
        at += datetime.timedelta(days=1)
    return at


def clock_ko(t):
    h, m = t.hour, t.minute
    part = '오전' if h < 12 else '오후' if h < 18 else '밤'
    h12 = h % 12 or 12
    return '%s %d시%s' % (part, h12, ' %d분' % m if m else '')


# -- reads ---------------------------------------------------------------------
def skeleton_of(life):
    keys = getattr(life, '_LIFE_SKELETON_KEYS', None) or (
        'life_skeleton_weekday_bed', 'life_skeleton_weekend_bed',
        'life_skeleton_work_days')
    return {k: life.get_config(k, '') for k in keys}


def protein_resource(life, today, suggest=None):
    """{'name', 'protein_g'|None, 'kcal'|None, 'basis'} or None (not owned)."""
    rows = []
    try:
        conn = life.get_conn()
        try:
            rows = life.resource_list(conn, kind='supplement')
        finally:
            conn.close()
    except Exception:            # noqa: BLE001 -- pre-018 kit / no table = not owned
        rows = []
    sg = suggest or _sibling('suggest')
    hist = sg.history(life, today)
    for r in rows:
        d = r.get('detail') if isinstance(r.get('detail'), dict) else {}
        g = d.get('protein_g', d.get('scoop_protein_g'))
        if g is None and not PROTEIN_NAME.search(r['name'] or ''):
            continue
        out = {'name': r['name'], 'protein_g': None, 'kcal': None,
               'basis': 'resource'}
        if g is not None:
            out['protein_g'] = float(g)
            out['kcal'] = float(d['kcal']) if d.get('kcal') is not None else None
        else:
            key = life.normalize_food_key(r['name'])
            h = next((x for x in hist if x['key'] == key), None)
            if h:
                out.update(protein_g=float(h['protein']), kcal=float(h['kcal']),
                           basis='resource+history')
        return out
    shakes = sorted((h for h in hist if PROTEIN_NAME.search(h['name'])
                     and h['times'] >= HISTORY_MIN_TIMES and h['protein'] > 0),
                    key=lambda h: h['times'], reverse=True)
    if shakes:
        h = shakes[0]
        return {'name': h['name'], 'protein_g': float(h['protein']),
                'kcal': float(h['kcal']), 'basis': 'history'}
    return None


# -- the sentence -----------------------------------------------------------------
def _line(a, when, res, food, late):
    short = a['shortfall_g']
    if a['tier'] == 'met':
        return '단백질 목표 채웠어요 (%dg / %dg).' % (a['eaten_g'], a['goal_g'])
    if a['tier'] == 'on_track':
        return '단백질 %dg 남았어요. 남은 식사로 채워지는 양이에요.' % short
    if late:
        if a['carry_g'] > 0:
            return ('단백질 %dg 부족해요. 자기 전에 몰아 먹기보다 '
                    '내일 한 끼에 %dg만 더 얹어요.' % (short, a['carry_g']))
        return '단백질 %dg 부족해요. 내일은 평소대로 채우면 돼요.' % short
    by = '%s까지 ' % clock_ko(when) if when else ''
    if res is not None:
        g = res.get('protein_g')
        if g:
            after = a['eaten_g'] + round(g)
            tail = '채워져요' if after >= a['goal_g'] else '%dg까지 올라가요' % after
            return '단백질 %dg 부족해요. %s프로틴 한 스쿱(~%dg)이면 %s.' % (
                short, by, round(g), tail)
        return '단백질 %dg 부족해요. %s프로틴 한 스쿱이면 도움이 돼요.' % (short, by)
    if food is not None:
        after = a['eaten_g'] + round(food['protein'])
        tail = '채워져요' if after >= a['goal_g'] else '%dg까지 올라가요' % after
        return '단백질 %dg 부족해요. %s%s 한 번이면 %s.' % (short, by, food['name'], tail)
    return '단백질 %dg 부족해요. %s한 끼에 %dg 정도까지 채울 수 있어요.' % (
        short, by, a['fill_g'])


def nudge(day=None, now=None, card=None, suggest=None):
    """The whole answer. `day` is card.py's input dict (date / carry_kcal),
    loaded exactly as the card loads it; `now` a datetime (default: now)."""
    card = card or _sibling('card')
    life = card.life
    day, iso = card.load_day(day or {})
    d = datetime.date.fromisoformat(iso)
    now = now or datetime.datetime.now()
    out = {'date': iso, 'line': None}
    if not day.get('meals'):
        out['status'] = 'silent_no_records'      # no rows is not 0 g eaten
        return out
    stats = card.load_body_stats()
    if 'weight_kg' in (stats.get(getattr(life, 'BODY_STATS_FALLBACK_KEY',
                                         '_defaults_used')) or ()):
        out['status'] = 'silent_no_weight'       # a threshold on a default is a guess
        return out
    state = card.day_state(day)
    w = float(stats['weight_kg'])
    a = assess(state, w, program_of(stats), renal_known(stats), ffm_kg(stats, w))
    out.update(a)
    out['status'] = a['tier']
    if a['tier'] != 'short':
        out['line'] = _line(a, None, None, None, False)
        return out
    sg = suggest or _sibling('suggest')
    res = protein_resource(life, d, sg)
    food = None
    if res is None:
        sl = sg.shortlist({'date': iso, 'carry_kcal': day.get('carry_kcal', 0)},
                          card=card, today=d)
        food = next((i for i in sl.get('items') or [] if i.get('why') == 'protein'), None)
    bed = bedtime(skeleton_of(life), d)
    margin = SHAKE_MARGIN_MIN if res is not None else FOOD_MARGIN_MIN
    when = bed - datetime.timedelta(minutes=margin) if bed else None
    late = bool(when and now >= when)
    out.update(status='late' if late else 'short', resource=res,
               food=food and {k: food[k] for k in ('name', 'kcal', 'protein')},
               bedtime=bed and bed.strftime('%Y-%m-%d %H:%M'),
               last_call=when and when.strftime('%Y-%m-%d %H:%M'),
               margin_min=margin if bed else None)
    out['line'] = _line(a, when, res, food, late)
    return out


def main(argv):
    ap = argparse.ArgumentParser(prog='protein.py')
    ap.add_argument('--date', default=None, help='YYYY-MM-DD (default: today)')
    ap.add_argument('--at', default=None, help='HH:MM on --date (default: now)')
    ap.add_argument('--carry-kcal', type=int, default=0)
    a = ap.parse_args(argv)
    day = {}
    if a.date:
        day['date'] = a.date
    if a.carry_kcal:
        day['carry_kcal'] = a.carry_kcal
    now = None
    if a.at:
        hm = _hm(a.at)
        if hm is None:
            ap.error('--at must be HH:MM')
        base = datetime.date.fromisoformat(a.date) if a.date else datetime.date.today()
        now = datetime.datetime.combine(base, datetime.time(*hm))
    print(json.dumps(nudge(day, now), ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
