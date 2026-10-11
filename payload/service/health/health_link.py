"""health_link -- the iPhone Health app link offer and its dev-channel gate
(pack_health 0.38.2; owner 2026-10-11 12:24 / 12:27).

The link is offered ONCE after the whole consult wraps (goal + calorie +
program: the setup tail's records step in program-plan). An install whose
calorie target was already settled before this release hears it once at a
natural moment instead -- under the session close-out card, never as a
conversation's first message (`closeout_offer`). Declined -> one more offer
at the first 2-3 week recalibration only (brief_lib.calorie_week_lines).

DEV CHANNEL ONLY. Both offers, and every Dogany app link, are gated by
`offer_gate()`: the install's framework update channel is a dev channel
(DOGANY_UPDATE_CHANNEL, the env first, else the nearest .instance.conf the
framework mint writes; dev | main) AND the Dogany app is connected (the
companion file carries an ack with read_at). A stable install (channel
release, staging, or none declared -- the framework reads none as release)
never sees an offer. The pack had no channel flag of its own; this reads the
framework's.

Answers: `program-plan answer --stage records` inside the tail,
`program-plan answer --stage health_link --json '{"pick":"yes|no"}'`
outside it. Both write config health_link=linked|declined (+ the day).
Watch active kcal is never imported for the target (WATCH_IMPORT_KINDS); a
workout row's watch kcal is shown as reference only.
"""
import json
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
DEV_CHANNELS = ("dev", "main")
INSTANCE_CONF = ".instance.conf"
APP_FILE = "com.moha.dogany.dogany.json"
# what the link brings in: the phone's steps, the watch's workouts / heart
# rate, sleep (hk-ingest KINDS; never active_energy_day)
LINK_KINDS = ("workout", "sleep", "steps", "heart_rate", "resting_heart_rate")
OFFER_MARKER = ".health-link-offer.json"
# config keys a settled calorie step leaves behind (any one is enough)
SETTLED_KEYS = ("calorie_target_kcal", "deficit_kcal", "surplus_kcal")


def _conf_value(key, start=None):
    """`key=value` from the nearest .instance.conf at or above `start`."""
    d = os.path.abspath(start or HERE)
    while True:
        p = os.path.join(d, INSTANCE_CONF)
        if os.path.isfile(p):
            try:
                with open(p, encoding="utf-8") as f:
                    for ln in f:
                        k, sep, v = ln.strip().partition("=")
                        if sep and k.strip() == key:
                            return v.strip().strip("\"'")
            except OSError:
                return None
            return None
        up = os.path.dirname(d)
        if up == d:
            return None
        d = up


def update_channel():
    env = os.environ.get("DOGANY_UPDATE_CHANNEL")
    if env:
        return env.strip()
    return _conf_value("DOGANY_UPDATE_CHANNEL") or "release"


def dev_channel():
    return update_channel() in DEV_CHANNELS


def app_connected():
    """True only when the Dogany app is connected to this install: the
    framework-written companion file (DGN-1825) carries an ack with
    read_at."""
    d = (os.environ.get("DOGANY_INTEGRATIONS_DIR")
         or os.path.join(os.path.expanduser("~"), ".dogany", "integrations"))
    try:
        with open(os.path.join(d, APP_FILE), encoding="utf-8") as f:
            ack = (json.load(f) or {}).get("ack") or {}
    except (OSError, ValueError, AttributeError):
        return False
    return bool(ack.get("read_at"))


def offer_gate():
    """Every Health-app / Dogany-app offer passes here: dev channel AND the
    app connected."""
    return dev_channel() and app_connected()


def _rows(db, sql, args=()):
    try:
        conn = sqlite3.connect("file:%s?mode=ro" % db, uri=True)
    except sqlite3.Error:
        return None
    try:
        return conn.execute(sql, args).fetchall()
    except sqlite3.Error:
        return None
    finally:
        conn.close()


def consented(db):
    """The healthkit kinds with an active consent, or None on a kit without
    the ingest ledger (nothing can be offered there)."""
    if not db or not _rows(db, "SELECT 1 FROM sqlite_master WHERE "
                               "type='table' AND name='ingest_consent'"):
        return None
    return {k for (k,) in _rows(db, "SELECT kind FROM ingest_consent WHERE "
                                    "source='healthkit' AND revoked_at IS "
                                    "NULL") or ()}


def config(db, key):
    r = _rows(db, "SELECT value FROM config WHERE key=?", (key,))
    return r[0][0] if r else None


def link_answer(db):
    """'linked' | 'declined' | None (never answered)."""
    v = config(db, "health_link")
    return v if v in ("linked", "declined") else None


def calorie_settled(db):
    for k in SETTLED_KEYS:
        v = config(db, k)
        if v not in (None, ""):
            return True
    return False


def _marker(state_dir):
    return os.path.join(state_dir, OFFER_MARKER)


def offered(state_dir):
    try:
        with open(_marker(state_dir), encoding="utf-8") as f:
            return bool((json.load(f) or {}).get("after_update"))
    except (OSError, ValueError, AttributeError):
        return False


def closeout_offer(db, state_dir, today):
    """The existing user's one offer after the update, for the close-out
    card's tail: [offer line, answer line] once, else []. Gate: dev channel
    + the app; the calorie already settled; the link never answered and its
    kinds not all consented; not offered before (marker in the state dir,
    written here so it is said once)."""
    if not offer_gate() or not calorie_settled(db) or link_answer(db):
        return []
    have = consented(db)
    if have is None or set(LINK_KINDS) <= have:
        return []
    if offered(state_dir):
        return []
    try:
        os.makedirs(state_dir, exist_ok=True)
        tmp = _marker(state_dir) + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({"after_update": str(today)}, f)
        os.replace(tmp, _marker(state_dir))
    except OSError:
        return []          # no marker -> no offer (it would repeat)
    import ui_labels
    return ["HEALTH_LINK_OFFER: " + ui_labels.i18n("health.link.offer"),
            "HEALTH_LINK_ANSWER cmd=service/health/program-plan answer "
            "--stage health_link --json {\"pick\":\"yes|no\"}"]
