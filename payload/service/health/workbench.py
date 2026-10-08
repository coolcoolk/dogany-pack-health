#!/usr/bin/env python3
"""Health pack's ONE daily pin card (owner 2026-10-02 12:41-13:00).

    <title: date + weekday>

    [diet]   eaten / target kcal, the macro line, one line per EATEN meal
    [week]   <YYYY> <ISO week> . M/D - M/D, the 3-row week calendar
             (ui_labels.week_calendar), no rule lines
    [today]  training day before its session: header + the static lineup
             ([ ] rows, exercise-enter.render_lineup_preview); after the
             session: the closeout card's rows ([v] / [>] / [ ]); rest day:
             one line
    Each section is one quote block ("> " rows); the title stays plain.

Every word is copy (ui_labels.i18n, health.pin.* / health.weekday.*); this
file stays ASCII. The diet numbers come from kit verbs only: load_card_data
(the meal list the diet-status card reads) and brief_lib.diet_target (the
morning message's target: carryover, else targets_for_date). A live session
card holds the pin instead (pin() returns 'session'); the goal and weekly
progress lines of the old board are gone (the weekly retro carries the goal
check).

pin() is the one writer of this section; it runs from the morning brief
(health-brief), the session close-out and the diet-status card after a meal
log (card.py).

A diet read that FAILS while the kit is installed (live 2026-10-08 14:56: a
pin with no [diet] block although two meals were logged; a re-run minutes
later was fine) keeps the [diet] lines this owner published earlier the same
day, read back from the section store, and says so once on stderr. Only a
missing kit drops the section.

Concurrency: pin() may run twice at once (the kit spawns this file after
every meal / workout write). status-footer --pin-set already serialises the
store's read-modify-write under its own flock and writes tmp + os.replace, so
two publishes never corrupt dashboard-sections.json; but it is last-writer-
wins, so pin() also holds its own lock (PIN_LOCK) across read + render +
publish -- the later run renders after the earlier one published, and a pin
rendered from an older database read never lands last.
"""
import argparse
from contextlib import closing
import datetime as dt
import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

try:
    import fcntl
except ImportError:  # pragma: no cover - non-POSIX: lock-free best effort
    fcntl = None

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
PIN_OWNER = "health-workbench"
FOOTER = ROOT / "routines" / "status-footer.py"
BOT_DIR = Path(os.environ.get("WARG_DASHBOARD_FILE", ROOT / ".telegram_bot" / "dashboard.md")).parent
DB = ROOT / "database" / "kit_life.db"
STATE = ROOT / "files" / "program" / ".program-plan.json"
SECTIONS = "dashboard-sections.json"   # status-footer's section store
PIN_LOCK = ".health-workbench.lock"    # serialises pin() runs (bot dir)
PIN_LOCK_SECS = 30.0
sys.path.insert(0, str(HERE))
import ui_labels as UL  # noqa: E402

# Weekday labels are copy (owner 2026-10-02): health.weekday.short.*.
WEEKDAYS = [UL.weekday_short(d) for d in UL.WEEKDAY_ORDER]
CARDIO = "\uc720\uc0b0\uc18c"     # workout_types.category of a cardio log
PLANNED_SUFFIX = " (\uc608\uc815)"  # the kit's not-yet-eaten meal marker


def rows(db, sql, args=()):
    try:
        return db.execute(sql, args).fetchall()
    except sqlite3.Error:
        return []


def number(value):
    return format(int(round(float(value or 0))), ",")


def md(day):
    if isinstance(day, str):
        day = dt.date.fromisoformat(day[:10])
    return f"{day.month}/{day.day}"


def week_workouts(db, start, end):
    return rows(db, "SELECT w.id,w.date,s.code,wc.category,wc.subtype,w.note,w.minutes "
                "FROM workouts w LEFT JOIN session_type s ON s.id=w.session_type_id "
                "LEFT JOIN (SELECT c.workout_id,group_concat(DISTINCT t.category) category, "
                "group_concat(t.subtype, ', ') subtype FROM workout_classifications c "
                "JOIN workout_types t ON t.id=c.type_id GROUP BY c.workout_id) wc "
                "ON wc.workout_id=w.id WHERE w.date BETWEEN ? AND ? ORDER BY w.id", (start, end))


def is_cardio(category):
    return bool(category) and CARDIO in category


def rotation_offset(db, rotation, before):
    """The next session follows recorded training order across week boundaries."""
    if not rotation:
        return 0
    history = rows(db, "SELECT s.code FROM workouts w JOIN session_type s "
                   "ON s.id=w.session_type_id WHERE w.date<? ORDER BY w.date,w.id", (before,))
    cursor = 0
    for (code,) in history:
        if code in rotation:
            cursor = (rotation.index(code) + 1) % len(rotation)
    return cursor


def _db_file(db):
    try:
        return db.execute("PRAGMA database_list").fetchone()[2] or None
    except (sqlite3.Error, TypeError, IndexError):
        return None


def _load(name, path):
    import importlib.machinery
    import importlib.util
    prev = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        loader = importlib.machinery.SourceFileLoader(name, str(path))
        spec = importlib.util.spec_from_loader(name, loader)
        mod = importlib.util.module_from_spec(spec)
        loader.exec_module(mod)
        return mod
    finally:
        sys.dont_write_bytecode = prev


# ---------------------------------------------------------------------------
# [diet]
# ---------------------------------------------------------------------------
PORTION = re.compile(r"\s+\d+(?:\.\d+)?\s*(?:g|kg|ml|l)$", re.I)


def short_name(name):
    """A meal's name for one pin line: the planned marker, every
    parenthesised note and a trailing portion dropped ('A (B) 230g' -> 'A')."""
    n = str(name or "").strip()
    if n.endswith(PLANNED_SUFFIX.strip()):
        n = n[:-len(PLANNED_SUFFIX.strip())]
    got = re.sub(r"\s+", " ", re.sub(r"\s*\([^)]*\)", "", n)).strip()
    got = PORTION.sub("", got).strip()
    return got or n.strip()


DIET_ERROR = []    # the swallowed kit_diet exception(s) of this process
_DIET_LOGGED = []  # set once the failure went to stderr


def kit_present():
    """The kit SDK file brief_lib.kit_life loads is installed."""
    try:
        import brief_lib as BL
        path = (os.environ.get("KIT_LIFE_PY")
                or os.path.join(BL.PROJECT_ROOT, "database", "kit_life.py"))
        return os.path.isfile(path)
    except BaseException:  # noqa: BLE001
        return False


def kit_diet(db, day):
    """(meal dicts, target dict | None) from kit verbs, or None when the kit
    is not reachable or the read failed (the exception lands in DIET_ERROR).
    Meals: life.load_card_data (type, name, kcal, carbs, protein, fat) minus
    the planned rows; target: brief_lib.diet_target (kcal / protein, each
    None when not the owner's own)."""
    try:
        import brief_lib as BL
        with BL.quiet():
            life = BL.kit_life()
            db_file = _db_file(db)
            if db_file:
                life.DB_PATH = db_file
            card = life.load_card_data(day.isoformat(), conn=db)
            # the morning message's number, all day (burn-free base)
            target = BL.diet_target(db, day, before_training=True)
        rank = getattr(life, "_MEAL_SLOT_RANK", {}) or {}
        suffix = getattr(life, "PLANNED_SUFFIX", PLANNED_SUFFIX).strip()
    except BaseException as e:  # noqa: BLE001 -- no diet data this run
        DIET_ERROR.append(e)
        return None
    meals = [m for m in (card or {}).get("meals") or ()
             if not str(m.get("name") or "").rstrip().endswith(suffix)]
    order = {id(m): i for i, m in enumerate(meals)}
    meals.sort(key=lambda m: (rank.get(m.get("type") or "", 9), order[id(m)]))
    return meals, target


def published_text(bot_dir):
    """This owner's last published pin text from the section store, or None."""
    try:
        store = json.loads((Path(bot_dir) / SECTIONS).read_text(encoding="utf-8"))
        text = (store.get("sections") or {}).get(PIN_OWNER, {}).get("text")
    except (OSError, ValueError, AttributeError, TypeError):
        return None
    return text if isinstance(text, str) else None


def kept_diet(previous, day, lang=None):
    """The [diet] lines of `previous` (a published pin text) when its title
    is today's title, else []: a failed read keeps the same day's lines and
    never carries yesterday's meals into today."""
    if not previous:
        return []
    title = UL.i18n("health.pin.title", lang, date=md(day),
                    weekday=UL.i18n("health.weekday.abbr."
                                    + UL.WEEKDAY_ORDER[day.weekday()], lang))
    rows = previous.split("\n")
    if rows[0].strip() != title.strip():
        return []
    label = UL.i18n("health.pin.diet_eaten", lang, eaten="").split("]")[0] + "]"
    block = []
    for r in rows[1:]:
        if r.startswith(">"):
            block.append(r[2:] if r.startswith("> ") else r[1:])
        elif block:
            break
        elif r.strip():
            return []      # the first block is not a quote block
    return block if block and block[0].startswith(label) else []


def _log_diet_failure():
    if _DIET_LOGGED:
        return
    _DIET_LOGGED.append(True)
    e = DIET_ERROR[-1] if DIET_ERROR else None
    sys.stderr.write("workbench: diet read failed (%s: %s); keeping today's "
                     "published [diet] lines if any\n"
                     % (type(e).__name__ if e else "?", e if e else "no detail"))


def diet_section(db, day, lang=None, data=None, previous=None):
    """The [diet] lines: eaten / target kcal (eaten alone without a target),
    the macro line (protein against its target when there is one), one line
    per eaten meal. [] when the kit is not installed. A failed read with the
    kit installed keeps today's published lines (kept_diet over `previous`,
    the store's pin text) and logs the failure once to stderr."""
    got = data if data is not None else kit_diet(db, day)
    if got is None and data is None and kit_present():
        _log_diet_failure()
        return kept_diet(previous, day, lang)
    if not got:
        return []
    meals, target = got
    target = target or {}
    tot = {k: sum(float(m.get(k) or 0) for m in meals)
           for k in ("kcal", "carbs", "protein", "fat")}
    if target.get("kcal"):
        out = [UL.i18n("health.pin.diet", lang, eaten=number(tot["kcal"]),
                       target=number(target["kcal"]))]
    else:
        out = [UL.i18n("health.pin.diet_eaten", lang, eaten=number(tot["kcal"]))]
    if target.get("protein"):
        out.append(UL.i18n("health.pin.macros", lang, carb=number(tot["carbs"]),
                           protein=number(tot["protein"]),
                           protein_target=number(target["protein"]),
                           fat=number(tot["fat"])))
    else:
        out.append(UL.i18n("health.pin.macros_eaten", lang,
                           carb=number(tot["carbs"]),
                           protein=number(tot["protein"]), fat=number(tot["fat"])))
    for m in meals:
        out.append(UL.i18n("health.pin.meal", lang, slot=m.get("type") or "?",
                           name=short_name(m.get("name")), kcal=number(m.get("kcal"))))
    return out


# ---------------------------------------------------------------------------
# [week]
# ---------------------------------------------------------------------------
def week_cells(db, state, day, done):
    """({MON..SUN: split code}, {MON..SUN: 'done'|'today'}) of day's week
    for the calendar. A day with a session shows the split it trained (a
    session off the rotation, the rest glyph) and is done once closed or
    past; a planned day still ahead takes the next split in the rotation; a
    missed planned day is rest (the queue shifts). Cardio logs are not
    sessions here."""
    rotation = (state.get("structure") or {}).get("rotation") or []
    planned = (state.get("days") or {}).get("weekdays") or []
    week = day - dt.timedelta(days=day.weekday())
    cursor = rotation_offset(db, rotation, week.isoformat())
    days, status = {}, {}
    for i, key in enumerate(UL.WEEKDAY_ORDER):
        date = week + dt.timedelta(days=i)
        if date == day:
            status[key] = "today"
        sessions = [x for x in done.get(date.isoformat(), [])
                    if not is_cardio(x[1])]
        if sessions and date <= day:
            code = next((x[0] for x in sessions if x[0] in rotation), None)
            if code:
                cursor = (rotation.index(code) + 1) % len(rotation)
            days[key] = code
            if date < day or all(x[3] is not None for x in sessions):
                status[key] = "done"
        elif date >= day and key in planned and rotation:
            days[key] = rotation[cursor]
            cursor = (cursor + 1) % len(rotation)
    return days, status


def week_section(days, status, day, lang=None):
    """'<header>' + the kit's calendar rows. No rule lines: the section is
    a quote block (quote()), which already sets it apart (owner 2026-10-06
    21:04: the pin's quote blocks back, no dash lines)."""
    year, week, _ = day.isocalendar()
    start = day - dt.timedelta(days=day.weekday())
    calendar = UL.week_calendar(days, status, lang)
    head = UL.i18n("health.pin.week", lang, year=year, week=week, start=md(start),
                   end=md(start + dt.timedelta(days=6)))
    return [head] + calendar


# ---------------------------------------------------------------------------
# [today]
# ---------------------------------------------------------------------------
def plan_minutes(state, split):
    """The day length the program consult said for `split`, or None
    (brief_lib.plan_minutes -- the one reader)."""
    import brief_lib as BL
    return BL.plan_minutes(state, split)


def today_lineup(db, program, day, lang=None, state=None):
    """Training day before its session: (header, lineup rows) from rx-calc
    (the prescription the session opens with), or None when there is no
    program / no prescription / no lineup. The header's minutes are the
    plan's whole-day figure (plan_minutes: the number the consult said),
    else rx-calc's lifting estimate."""
    if not program or not Path(program).is_file():
        return None
    try:
        import brief_lib as BL
        db_file = _db_file(db)
        with BL.quiet():
            rx = BL.rx_calc().calc_rx(str(program), day.isoformat(), db_file)
        ex = [e for e in (rx or {}).get("exercises") or () if e.get("sets")]
        split = (rx or {}).get("rotation_day")
        if not ex or not split:
            return None
        ee = _load("workbench_exercise_enter", HERE / "exercise-enter")
        with BL.quiet():
            lineup = ee.render_lineup_preview(ex, db_file)
        if not lineup:
            return None
        head = UL.i18n("health.pin.today", lang, split=split, lifts=len(ex),
                       minutes=BL.session_estimate_minutes(
                           split, ex, str(program), state=state))
        return head, lineup
    except BaseException:  # noqa: BLE001 -- the split line is the fallback
        return None


def session_lines(db, program, wid, code, minutes, lang=None):
    """A session today: (header, rows) -- the closeout card's rows
    (session-closeout.close_rows over exercise-enter.gather_card_state:
    [v] done, [>] ended short, [ ] not started), or None."""
    if not program or not Path(program).is_file() or not code:
        return None
    try:
        import brief_lib as BL
        db_file = _db_file(db)
        with BL.quiet():
            sc = _load("workbench_closeout", HERE / "session-closeout")
            slots = sc._close_slots(sc.include_unstarted([], str(program), code))
            if not slots:
                return None
            ee = sc._sibling("closeout_exercise_enter", "exercise-enter")
            cs = ee.gather_card_state(db_file, str(program), wid, slots,
                                      rotation_day=code)
            got = sc.close_rows(slots, cs)
        out = []
        for mark, name, value in got:
            out.append("%s %s" % (mark, name))
            if value:
                out.append("    " + value)
        if minutes:
            head = UL.i18n("health.pin.today_done", lang, split=code,
                           lifts=len(slots), minutes=number(minutes))
        else:
            head = UL.i18n("health.pin.today_split", lang, split=code)
        return head, out
    except BaseException:  # noqa: BLE001 -- the split line is the fallback
        return None


# ---------------------------------------------------------------------------
# the pin
# ---------------------------------------------------------------------------
def quote(rows):
    """One section as one quote block: every row '> '-led (the bridge renders
    the run as a single blockquote). Only trailing blanks go, so the
    calendar's columns stay aligned."""
    return ["> " + r.rstrip() if r.strip() else ">" for r in rows]


def render(db, state, today=None, program=None, lang=None, previous=None):
    """The pin text."""
    return render_pin(db, state, today, program, lang, previous=previous)[1]


def render_pin(db, state, today=None, program=None, lang=None, diet=None,
               previous=None):
    """(kind, text): kind 'lineup' (a training day before its session: the
    pin carries today's lineup) or 'pin'. `diet` = (meals, target) injects
    the diet data (tests); default: the kit verbs. `previous` = the pin text
    published before (the store's), the source of a failed read's diet."""
    now = (today if isinstance(today, dt.datetime) else
           dt.datetime.combine(today, dt.time(12, 30)) if today else
           dt.datetime.now(ZoneInfo("Asia/Seoul")))
    day = now.date()
    key = UL.WEEKDAY_ORDER[day.weekday()]
    week = day - dt.timedelta(days=day.weekday())
    done = {}
    for wid, date, code, category, sub, _note, minutes in week_workouts(
            db, week.isoformat(), (week + dt.timedelta(days=6)).isoformat()):
        done.setdefault(date, []).append((code, category, wid, minutes, sub))
    days, status = week_cells(db, state, day, done)
    rotation = (state.get("structure") or {}).get("rotation") or []
    planned = (state.get("days") or {}).get("weekdays") or []

    lines = [UL.i18n("health.pin.title", lang, date=md(day),
                     weekday=UL.i18n("health.weekday.abbr." + key, lang)), ""]
    food = diet_section(db, day, lang, diet, previous)
    if food:
        lines += quote(food) + [""]
    lines += quote(week_section(days, status, day, lang)) + [""]
    section = []

    kind = "pin"
    trained = [x for x in done.get(day.isoformat(), []) if not is_cardio(x[1])]
    if trained:
        code, cat, wid, minutes, sub = next(
            (x for x in reversed(trained) if x[0]), trained[-1])
        got = session_lines(db, program, wid, code, minutes, lang)
        if got:
            section += [got[0]] + got[1]
        else:
            section.append(UL.i18n("health.pin.today_split", lang,
                                 split=code or sub or cat or days.get(key) or ""))
    elif key in planned and rotation:
        got = today_lineup(db, program, day, lang, state)
        if got:
            kind = "lineup"
            section += [got[0]] + got[1]
        else:
            section.append(UL.i18n("health.pin.today_split", lang,
                                 split=days.get(key) or rotation[0]))
    else:
        section.append(UL.i18n("health.pin.rest", lang))
    lines += quote(section)
    return kind, "\n".join(lines)


def program_of(state_path):
    """program.yaml beside the plan state (files/program/)."""
    return Path(state_path).parent / "program.yaml"


def refresh(db_path=DB, state_path=STATE, today=None, bot_dir=BOT_DIR):
    return pin(db_path, state_path, today, bot_dir) is not None


def _pin_lock(bot_dir):
    """An open, flock'd PIN_LOCK file (close it to release), or None: no
    fcntl, or still held after PIN_LOCK_SECS (then run unlocked -- the
    footer's own flock still keeps the store whole)."""
    if fcntl is None:
        return None
    try:
        fh = open(Path(bot_dir) / PIN_LOCK, "a+")
    except OSError:
        return None
    deadline = time.monotonic() + PIN_LOCK_SECS
    while True:
        try:
            fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return fh
        except OSError:
            if time.monotonic() >= deadline:
                fh.close()
                return None
            time.sleep(0.05)


def pin(db_path=DB, state_path=STATE, today=None, bot_dir=BOT_DIR):
    """Publish the pin section (the ONE writer of this section). Returns
    the kind published -- 'lineup' | 'pin' | 'cleared' | 'session' (a live
    session card holds the pin) -- or None when nothing was applied."""
    if not Path(bot_dir).is_dir() or not FOOTER.is_file():
        return None
    lock = _pin_lock(bot_dir)
    try:
        return _pin(db_path, state_path, today, bot_dir)
    finally:
        if lock is not None:
            lock.close()


def _pin(db_path, state_path, today, bot_dir):
    try:
        kind = "cleared"
        with closing(sqlite3.connect("file:%s?mode=ro" % db_path, uri=True)) as db:
            state = json.loads(Path(state_path).read_text()) if Path(state_path).exists() else {}
            body = ""
            if state.get("written"):
                kind, body = render_pin(db, state, today, program_of(state_path),
                                        previous=published_text(bot_dir))
        env = dict(os.environ, DOGANY_BOT_DATA_DIR=str(bot_dir))
        if not body:
            # owner 2026-09-27 16:44: no pin until onboarding has written a
            # program -- mid-consult the workbench would show placeholders.
            ok = subprocess.run([sys.executable, str(FOOTER), "--pin-clear", PIN_OWNER],
                                text=True, capture_output=True, env=env,
                                timeout=15).returncode == 0
            return kind if ok else None
        store = Path(bot_dir) / SECTIONS
        try:
            sections = json.loads(store.read_text()).get("sections", {})
        except (OSError, ValueError):
            sections = {}
        if "workout" in sections:
            return "session"
        ok = subprocess.run([sys.executable, str(FOOTER), "--pin-set", PIN_OWNER],
                            input=body, text=True, capture_output=True, env=env,
                            timeout=15).returncode == 0
        return kind if ok else None
    except (OSError, sqlite3.Error, ValueError, subprocess.TimeoutExpired):
        return None


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default=str(DB))
    ap.add_argument("--state", default=str(STATE))
    ap.add_argument("--today")
    ap.add_argument("--render", action="store_true")
    args = ap.parse_args()
    day = dt.date.fromisoformat(args.today) if args.today else None
    if args.render:
        with closing(sqlite3.connect("file:%s?mode=ro" % args.db, uri=True)) as conn:
            state = json.loads(Path(args.state).read_text()) if Path(args.state).exists() else {}
            print(render(conn, state, day, program_of(args.state),
                         previous=published_text(BOT_DIR)))
    else:
        sys.exit(0 if refresh(args.db, args.state, day) else 1)
