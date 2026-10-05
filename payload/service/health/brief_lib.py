"""brief_lib -- what the health agent's brief / daily retro / weekly retro say
(pack_health 0.30.0, the domain brief/retro standard; owner 2026-10-02).

The kit owns the three slots (kit_life 2.38.0: morning-brief.sh /
daily-retro.sh / weekly-review.sh domain path), the lanes, the title, the grid
drawing and the silence of a message with nothing in it. This pack owns the
lines. Three providers read this module and print through the kit's
retro-sections contract (database/retro_sections.py):

  health-brief   morning  today's diet target (carry folded in) and, on a
                          training day, "today's workout is pinned above"
                          with the split and minutes -- the lineup itself is
                          the workbench pin (owner 2026-10-02 11:53). Rest
                          day: the diet line only.
  session-retro  daily    today's session against its plan and today's
                          intake against its target; `--part next` is the
                          card's tail ("내일 운동: <day> · <time>").
  week-health    weekly   sessions done vs planned, body trend, goal check by
                          layer; `--mode grid` the Mon..Sun minutes for the
                          kit grid; `--part next` the next-week placement
                          proposal (the message's one decision, last).

RULES EVERY PROVIDER KEEPS (tests/test-brief-retro-providers.py):
  * READ ONLY. The database is opened `mode=ro`; nothing here writes. The
    kit's day-target helpers are handed that connection.
  * DETERMINISTIC. No model, no clock but the run date (KIT_RETRO_TODAY, the
    kit's pinned date, else --date, else today) -- same rows, same bytes.
  * SILENCE OVER ABSENCE (D4). A line whose facts are missing is dropped, it
    never says "no record". A provider with no line exits 3.
  * <= 3 lines, at most one decision, and that decision is the last line.
  * Every sentence is a key in brief_copy.json (health.brief.* /
    health.retro.*), AGENT_LANG first, then en.

WHERE THE FACTS COME FROM (no new store):
  plan       the active exercise routines on the calendar (routine_def, the
             same predicate program-plan's calendar_routines uses -- the
             program consult writes them); a day is planned when its weekday
             is in a routine's cadence inside the routine's start..end.
  done       workouts rows (one session per date that has one).
  session    rx-calc (the prescription engine, read-only) over the program
             card files/program/program.yaml: split code, lifts, sets; the
             minutes are the MINUTES RULE below.
  sets       workout_sets working/hold rows against the program day's sets.
  diet       diet-status/carryover.py (today's aim after a carried surplus),
             else the kit's targets_for_date -- never from a body stat the
             kit is serving from its code defaults.
  body       metric_log weight_kg / body_fat_pct.
  goal       ledger_goal (domain health, active), by layer (Q3 rule).
"""
import contextlib
import datetime
import importlib.machinery
import importlib.util
import io
import json
import os
import re
import sqlite3
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import ui_labels as UL                                          # noqa: E402

PROJECT_ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
EXIT_OK, EXIT_NOTHING = 0, 3
MAX_LINES = 3

WEEKDAYS = UL.WEEKDAY_ORDER
# Same predicate as program-plan calendar_routines (parity is tested): the
# routines the program consult registers are "헬스" / "운동" titled.
EXERCISE_WORDS = re.compile("헬스|운동|세션|웨이트|workout|gym|training", re.I)
MEASURE_WORDS = re.compile("체중|인바디|측정|weigh|inbody", re.I)
# rx-gen's trip suppression, carried: a trip-class all-day block today means
# no training brief.
TRIP_SQL = ("SELECT 1 FROM timeblock WHERE schedule_kind='all_day' "
            "AND status != 'cancelled' AND start_at < ? "
            "AND (end_at IS NULL OR end_at > ?) "
            "AND (LOWER(title) LIKE '%trip%' OR LOWER(title) LIKE '%travel%' "
            "OR title LIKE '%여행%' OR title LIKE '%출장%') LIMIT 1")
# MINUTES RULE: one working set = 40 s under the bar and setup, plus that
# slot's prescribed rest (rx-calc rest_sec; 120 s when it has none); rounded
# to the nearest 5 minutes. Stated, not tuned -- "~minutes" is a planning
# figure, not a promise.
SET_SECONDS = 40
DEFAULT_REST_SEC = 120
# A body reading older than this at the week's end is not a "trend" line.
BODY_FRESH_DAYS = 28
# Body stats the day target is computed from: a target built on one of these
# served from the kit's code defaults is a stranger's number (kit 2.20.0).
KCAL_STATS = ("weight_kg", "height_cm", "deficit_kcal")
LAYER_ORDER = {"short": 0, "event_overlay": 1, "mid": 2, "long": 3}


# ---------------------------------------------------------------------------
# environment
# ---------------------------------------------------------------------------
def db_path():
    return (os.environ.get("HEALTH_BRIEF_DB")
            or os.path.join(PROJECT_ROOT, "database", "kit_life.db"))


def program_path():
    data = (os.environ.get("WARG_DATA_DIR")
            or os.path.join(PROJECT_ROOT, "files", "program"))
    return os.path.join(data, "program.yaml")


def run_date(arg=None):
    """--date, else the kit's pinned run date, else today."""
    raw = arg or os.environ.get("KIT_RETRO_TODAY") or ""
    if raw:
        return datetime.date.fromisoformat(raw)
    return datetime.date.today()


def connect(path=None):
    """Read-only connection (URI mode=ro): a provider never writes."""
    p = os.path.abspath(path or db_path())
    if not os.path.isfile(p):
        raise FileNotFoundError(p)
    return sqlite3.connect("file:%s?mode=ro" % urllib.parse.quote(p), uri=True)


def _conf(key):
    try:
        with open(os.path.join(PROJECT_ROOT, "config", "agent.conf"),
                  encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if line.startswith(key + "="):
                    v = line.split("=", 1)[1].strip()
                    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
                        v = v[1:-1]
                    return v.strip()
    except OSError:
        pass
    return ""


def lang():
    return (os.environ.get("HEALTH_BRIEF_LANG") or _conf("AGENT_LANG")
            or "en")


_COPY = None


def t(key, **kw):
    """The copy for `key` in AGENT_LANG, then en; '' when neither has it."""
    global _COPY
    if _COPY is None:
        with open(os.path.join(HERE, "brief_copy.json"), encoding="utf-8") as fh:
            _COPY = json.load(fh)
    for lg in (lang(), "en"):
        v = (_COPY.get(lg) or {}).get(key)
        if isinstance(v, str) and v:
            return v.format(**kw) if kw else v
    return ""


def num(x):
    """1234.4 -> '1,234' (kcal and grams are shown whole)."""
    return format(int(round(x)), ",")


def dec(x):
    """82.95 -> '83', 21.64 -> '21.6': one decimal, trailing zero dropped."""
    return ("%.1f" % x).rstrip("0").rstrip(".") if x is not None else ""


def md(day):
    return t("health.date.md", m=day.month, d=day.day)


def wd_short(day):
    """The weekday's short name in the brief's language (i18n
    health.weekday.abbr.*)."""
    return UL.i18n("health.weekday.abbr." + WEEKDAYS[day.weekday()], lang())


def wd_full(day):
    return UL.weekday_full(WEEKDAYS[day.weekday()], lang())


def clock(hhmm):
    if lang() == "ko":
        return UL.clock_ko(hhmm)
    h, m = (int(x) for x in hhmm.split(":"))
    return "%d:%02d %s" % (h % 12 or 12, m, "AM" if h < 12 else "PM")


def diet_text(d):
    """The morning's diet line from diet_target(); '' when it has nothing."""
    if not d:
        return ""
    if d["kcal"] is not None and d["protein"] is not None:
        line = t("health.brief.diet", kcal=num(d["kcal"]), protein=num(d["protein"]))
    elif d["kcal"] is not None:
        line = t("health.brief.diet_kcal", kcal=num(d["kcal"]))
    elif d["protein"] is not None:
        line = t("health.brief.diet_protein", protein=num(d["protein"]))
    else:
        return ""
    if d["kcal"] is not None and d.get("cut", 0) > 0:
        line = t("health.brief.diet_carry", line=line, cut=num(d["cut"]))
    return line


def capped(lines):
    """The provider contract: <= 3 nonempty lines."""
    out = [ln for ln in lines if ln and ln.strip()]
    return out[:MAX_LINES]


def emit(lines, mode="section"):
    lines = capped(lines)
    if not lines:
        return EXIT_NOTHING
    print(lines[0] if mode == "line" else "\n".join(lines))
    return EXIT_OK


@contextlib.contextmanager
def quiet():
    """Engines print diagnostics; a provider's stdout is its lines only."""
    with contextlib.redirect_stdout(io.StringIO()), \
            contextlib.redirect_stderr(io.StringIO()):
        yield


def _load(name, path):
    prev = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        loader = importlib.machinery.SourceFileLoader(name, path)
        spec = importlib.util.spec_from_loader(name, loader)
        mod = importlib.util.module_from_spec(spec)
        loader.exec_module(mod)
        return mod
    finally:
        sys.dont_write_bytecode = prev


_MODS = {}


def rx_calc():
    if "rx" not in _MODS:
        _MODS["rx"] = _load("brief_rx_calc", os.path.join(HERE, "rx-calc"))
    return _MODS["rx"]


def kit_life():
    """The kit SDK, bound to the database this module reads."""
    if "kit" not in _MODS:
        path = (os.environ.get("KIT_LIFE_PY")
                or os.path.join(PROJECT_ROOT, "database", "kit_life.py"))
        mod = _load("brief_kit_life", path)
        mod.DB_PATH = os.path.abspath(db_path())
        _MODS["kit"] = mod
    return _MODS["kit"]


def carryover():
    """diet-status/carryover.py: the installed skill, then this repo."""
    if "carry" not in _MODS:
        env = os.environ.get("DIET_STATUS_DIR")
        cands = ([env] if env else []) + [
            os.path.join(PROJECT_ROOT, ".claude", "skills", "diet-status"),
            os.path.join(PROJECT_ROOT, ".claude", "skills-bundle", "diet-status"),
            os.path.join(PROJECT_ROOT, "skills-bundle", "diet-status")]
        _MODS["carry"] = None
        for d in cands:
            p = os.path.join(d, "carryover.py")
            if os.path.isfile(p):
                _MODS["carry"] = _load("brief_carryover", p)
                break
    return _MODS["carry"]


# ---------------------------------------------------------------------------
# plan (the calendar the program consult wrote)
# ---------------------------------------------------------------------------
def _weekdays(cadence):
    c = (cadence or "").strip().split("!", 1)[0]     # W:MON,FRI!hol -> W:MON,FRI
    if not c.upper().startswith("W:"):
        return []
    days = {x.strip().upper() for x in c[2:].split(",")}
    return [d for d in WEEKDAYS if d in days]


def schedule(conn):
    """Active exercise routines: [{id, weekdays, start, minutes, since,
    until}] in id order (program-plan calendar_routines' predicate)."""
    out = []
    try:
        rows = conn.execute(
            "SELECT id, title, COALESCE(purpose,''), cadence, time_of_day, "
            "duration_min, start_date, end_date FROM routine_def "
            "WHERE status='active' ORDER BY id").fetchall()
    except sqlite3.Error:
        return out
    for rid, title, purpose, cad, tod, dur, since, until in rows:
        if MEASURE_WORDS.search(title or ""):
            continue
        if not EXERCISE_WORDS.search("%s %s" % (title or "", purpose)):
            continue
        days = _weekdays(cad)
        if not days:
            continue
        start = None
        m = re.match(r"^(\d{1,2}):(\d{2})", str(tod or ""))
        if m:
            start = "%02d:%02d" % (int(m.group(1)), int(m.group(2)))
        out.append({"id": rid, "weekdays": days, "start": start,
                    "minutes": int(dur or 0),
                    "since": str(since or "")[:10],
                    "until": str(until or "")[:10]})
    return out


def planned(sched, day):
    """(is a training day, earliest start or None)."""
    iso, code = day.isoformat(), WEEKDAYS[day.weekday()]
    starts, hit = [], False
    for w in sched:
        if code not in w["weekdays"]:
            continue
        if w["since"] and iso < w["since"]:
            continue
        if w["until"] and iso > w["until"]:
            continue
        hit = True
        if w["start"]:
            starts.append(w["start"])
    return hit, (min(starts) if starts else None)


def week_of(day):
    mon = day - datetime.timedelta(days=day.weekday())
    return [mon + datetime.timedelta(days=i) for i in range(7)]


def next_training(sched, day, horizon=14):
    """(date, start) of the first planned day after `day`, else None."""
    for k in range(1, horizon + 1):
        d = day + datetime.timedelta(days=k)
        hit, start = planned(sched, d)
        if hit:
            return d, start
    return None


def earliest_start(windows):
    """The earliest HH:MM among windows' `start` (program-plan's daytime
    windows); None when none carries a time."""
    starts = sorted(w["start"] for w in windows or () if w.get("start"))
    return starts[0] if starts else None


def minus_minutes(hhmm, minutes):
    h, m = (int(x) for x in hhmm.split(":"))
    x = (h * 60 + m - minutes) % (24 * 60)
    return "%02d:%02d" % (x // 60, x % 60)


# ---------------------------------------------------------------------------
# done (workouts / workout_sets)
# ---------------------------------------------------------------------------
def workouts(conn, first, last):
    """[{id, date, minutes, code, label}] for first..last, date then id."""
    rows = conn.execute(
        "SELECT w.id, w.date, COALESCE(w.minutes, 0), st.code "
        "FROM workouts w LEFT JOIN session_type st ON st.id = w.session_type_id "
        "WHERE w.date >= ? AND w.date <= ? ORDER BY w.date, w.id",
        (first.isoformat(), last.isoformat())).fetchall()
    out = []
    for wid, date, minutes, code in rows:
        subs = [r[0] for r in conn.execute(
            "SELECT wt.subtype FROM workout_classifications wc "
            "JOIN workout_types wt ON wt.id = wc.type_id "
            "WHERE wc.workout_id = ? ORDER BY wt.sort, wt.id", (wid,))]
        label = code or "·".join(dict.fromkeys(subs)) or ""
        out.append({"id": wid, "date": date, "minutes": float(minutes or 0),
                    "code": code, "label": label})
    return out


def sets_done(conn, workout_id):
    """{exercise_name: working/hold sets logged}."""
    return {name: n for name, n in conn.execute(
        "SELECT exercise_name, COUNT(*) FROM workout_sets WHERE session_id = ? "
        "AND set_kind IN ('working','hold') GROUP BY exercise_name",
        (workout_id,))}


def week_counts(conn, sched, day, through):
    """(planned days in day's week, distinct workout dates Mon..through,
    minutes Mon..through)."""
    week = week_of(day)
    n_planned = sum(1 for d in week if planned(sched, d)[0])
    if through < week[0]:
        return n_planned, 0, 0.0
    rows = workouts(conn, week[0], min(through, week[-1]))
    return (n_planned, len({r["date"] for r in rows}),
            sum(r["minutes"] for r in rows))


# ---------------------------------------------------------------------------
# program (rx-calc, read-only)
# ---------------------------------------------------------------------------
def load_program():
    p = program_path()
    if not os.path.isfile(p):
        return None
    try:
        with quiet():
            return rx_calc().load_yaml(p)
    except BaseException:                        # noqa: BLE001 -- SystemExit too
        return None


def session_rx(day, db=None):
    """rx-calc's prescription for `day`, or None."""
    p = program_path()
    if not os.path.isfile(p):
        return None
    try:
        with quiet():
            return rx_calc().calc_rx(p, day.isoformat(), db or db_path())
    except BaseException:                        # noqa: BLE001
        return None


def session_minutes(exercises):
    sec = sum(int(e.get("sets") or 0) *
              (SET_SECONDS + int(e.get("rest_sec") or DEFAULT_REST_SEC))
              for e in exercises)
    return max(5, int(5 * round(sec / 300.0)))


def lifts_text(exercises, shown=3):
    names = [e.get("display") or e.get("name") or "" for e in exercises]
    names = [n for n in names if n]
    head = "·".join(names[:shown])
    if len(names) > shown:
        return t("health.brief.lifts_more", lifts=head, n=len(names) - shown)
    return head


# ---------------------------------------------------------------------------
# diet (carryover, else the kit's day target)
# ---------------------------------------------------------------------------
def diet_target(conn, day, before_training=False):
    """{kcal, protein, cut} or None. kcal = carryover's aim when it applies,
    else the kit's targets_for_date; each number only when its body stats
    are the owner's own (not the kit's code defaults). before_training (the
    morning): the day's burn is not in yet, so the kit target is the
    burn-free base (burn_override=0) -- the same number at 04:30 and on a
    re-render after the session."""
    try:
        life = kit_life()
        with quiet():
            stats = life.load_body_stats()
            used = set(life.body_stats_defaults_used(stats))
    except BaseException:                        # noqa: BLE001
        return None
    protein = None if "protein_g" in used else stats.get("protein_g")
    kcal, cut = None, 0
    mod = carryover()
    if mod is not None:
        try:
            with quiet():
                r = mod.compute(conn, life, day)
            if r.get("applicable"):
                kcal, cut = r["aim_kcal"], int(r.get("cut_kcal") or 0)
        except BaseException:                    # noqa: BLE001
            kcal, cut = None, 0
    body_known = not (used & set(KCAL_STATS)) and not (
        {"lean_mass_kg", "fat_mass_kg"} <= used)
    if kcal is None and body_known:
        try:
            with quiet():
                tg = life.targets_for_date(
                    day.isoformat(), stats=stats, conn=conn,
                    burn_override=0 if before_training else None)
            kcal = tg.get("eff_goal")
        except BaseException:                    # noqa: BLE001
            kcal = None
    if kcal is None and protein is None:
        return None
    return {"kcal": kcal, "protein": protein, "cut": cut}


def intake(conn, day):
    """{meals, kcal, protein} for the day, or None."""
    try:
        life = kit_life()
        with quiet():
            a = life.agg_day(day.isoformat(), conn=conn)
    except BaseException:                        # noqa: BLE001
        return None
    return {"meals": int(a.get("meal_cnt") or 0),
            "kcal": float(a.get("intake_kcal") or 0),
            "protein": float(a.get("protein_g") or 0)}


def trip_today(conn, day):
    try:
        local = datetime.datetime.combine(day, datetime.time()).astimezone()
        ws = local.astimezone(datetime.timezone.utc)
        we = ws + datetime.timedelta(days=1)
        f = "%Y-%m-%dT%H:%M:%SZ"
        return conn.execute(TRIP_SQL, (we.strftime(f), ws.strftime(f))
                            ).fetchone() is not None
    except sqlite3.Error:
        return False


# ---------------------------------------------------------------------------
# body + goal (metric_log, ledger_goal)
# ---------------------------------------------------------------------------
def readings(conn, metric, last):
    return conn.execute(
        "SELECT date, value FROM metric_log WHERE metric = ? AND date <= ? "
        "ORDER BY date DESC LIMIT 2", (metric, last.isoformat())).fetchall()


def goals(conn):
    try:
        rows = conn.execute(
            "SELECT id, layer, title, metric, target_value, target_dir, "
            "COALESCE(detail,'') FROM ledger_goal WHERE status='active' "
            "AND domain='health' ORDER BY id").fetchall()
    except sqlite3.Error:
        return []
    out = []
    for gid, layer, title, metric, target, tdir, detail in rows:
        try:
            d = json.loads(detail) if detail else {}
        except ValueError:
            d = {}
        out.append({"id": gid, "layer": layer or "", "title": title or "",
                    "metric": metric, "target": target, "dir": tdir,
                    "detail": d if isinstance(d, dict) else {}})
    out.sort(key=lambda g: (LAYER_ORDER.get(g["layer"], 9), g["id"]))
    return out


def goal_cadence(layer, sunday):
    """The kit weekly's Q3 rule: short / event_overlay judged weekly; mid
    shown, judged on the month's last Sunday; long not touched, judged on a
    quarter's last Sunday. -> 'judge' | 'show' | None."""
    month_end = (sunday + datetime.timedelta(days=7)).month != sunday.month
    if layer in ("short", "event_overlay"):
        return "judge"
    if layer == "mid":
        return "judge" if month_end else "show"
    if layer == "long":
        return "judge" if month_end and sunday.month in (3, 6, 9, 12) else None
    return None


def _unit(metric):
    m = metric or ""
    if m.endswith("_pct"):
        return "%", "%p"
    if m.endswith("_kg"):
        return "kg", "kg"
    return "", ""


def goal_verdict(g, value):
    unit, gap_unit = _unit(g["metric"])
    lo, hi = g["detail"].get("range_lo"), g["detail"].get("range_hi")
    if isinstance(lo, (int, float)) and isinstance(hi, (int, float)):
        if lo <= value <= hi:
            return t("health.retro.verdict_in_range")
        gap = (value - hi) if value > hi else (lo - value)
        return t("health.retro.verdict_gap", gap=dec(gap) + gap_unit)
    target = g["target"]
    if target is None:
        return ""
    if g["dir"] == "hold":
        noise = g["detail"].get("noise_sd") or 0
        if abs(value - target) <= noise:
            return t("health.retro.verdict_hold")
        return t("health.retro.verdict_drift", gap=dec(abs(value - target)) + gap_unit)
    if (g["dir"] == "down" and value <= target) or (g["dir"] == "up" and value >= target):
        return t("health.retro.verdict_reached")
    return t("health.retro.verdict_gap", gap=dec(abs(value - target)) + gap_unit)


def goal_line(conn, sunday):
    for g in goals(conn):
        how = goal_cadence(g["layer"], sunday)
        if how is None:
            continue
        value = None
        if g["metric"]:
            r = readings(conn, g["metric"], sunday)
            value = r[0][1] if r else None
        if value is None:
            return t("health.retro.goal_show_bare", title=g["title"])
        shown = dec(value) + _unit(g["metric"])[0]
        verdict = goal_verdict(g, value) if how == "judge" else ""
        if verdict:
            return t("health.retro.goal_judge", title=g["title"], value=shown,
                     verdict=verdict)
        return t("health.retro.goal_show", title=g["title"], value=shown)
    return ""


def body_line(conn, sunday):
    w = readings(conn, "weight_kg", sunday)
    if not w:
        return ""
    last_date = datetime.date.fromisoformat(w[0][0][:10])
    if (sunday - last_date).days > BODY_FRESH_DAYS:
        return ""
    bf = conn.execute("SELECT value FROM metric_log WHERE metric='body_fat_pct' "
                      "AND date = ?", (w[0][0],)).fetchone()
    bf_txt = t("health.retro.body_bf", bf=dec(bf[0])) if bf else ""
    if len(w) > 1:
        return t("health.retro.body", prev=dec(w[1][1]), last=dec(w[0][1]),
                 bf=bf_txt, md=md(last_date))
    return t("health.retro.body_one", last=dec(w[0][1]), bf=bf_txt,
             md=md(last_date))
