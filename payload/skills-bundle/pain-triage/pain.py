#!/usr/bin/env python3
"""pain.py -- pain / form-fault time-series store (self-contained, B-plan).

Independent SQLite store for in-session pain + form-fault events. Kept OUT of the
shared kit_life DB on purpose (owner choice: start independent, migrate to kit_life
later if join-with-sets analysis is needed). Loose join to workouts = by date.

Verbs:
  add      insert one event (in-session fast log). only --exercise + --pain need.
  list     show events (filter --exercise / --days / --open).
  recent   unresolved events (for the post-session raise). alias: list --open.
  resolve  close an event: attach --guardrail / --note / --program-change.
  audit    pattern scan -> recurring (exercise x fault / exercise x side) over
           threshold, or rising pain trend -> flag for program review.
  show     one event detail by --id.

All output = plain text lines the agent reads then speaks in own voice.
NOT a medical tool: stores form/mechanics triage + coaching, not diagnosis.
"""
import argparse, os, sqlite3, sys
from datetime import datetime, timedelta

DB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "pain_events.db")

# reference vocab (free text still allowed; these just guide the agent)
ROM_PHASES = ["setup", "descent", "bottom", "ascent", "lockout", "other"]
FAULTS = ["valgus", "knee_forward", "shift", "twist", "round", "buttwink",
          "impingement", "unknown"]
ACTIONS = ["load_drop", "substitute", "stop", "continue", "form_cue"]


def conn():
    os.makedirs(os.path.dirname(DB), exist_ok=True)
    c = sqlite3.connect(DB)
    c.execute("""CREATE TABLE IF NOT EXISTS pain_events(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ts TEXT NOT NULL,
        session TEXT,
        exercise TEXT NOT NULL,
        load_kg REAL,
        set_no INTEGER,
        rir INTEGER,
        side TEXT,
        pain INTEGER NOT NULL,
        rom_phase TEXT,
        fault TEXT,
        action TEXT,
        note TEXT,
        guardrail TEXT,
        program_change TEXT,
        status TEXT NOT NULL DEFAULT 'open'
    )""")
    c.commit()
    return c


def _now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def _row(r):
    # compact one-line view of an event row
    (i, ts, ses, ex, load, setno, rir, side, pain, rom, fault,
     action, note, guard, prog, status) = r
    bits = ["#%d" % i, ts, "[%s]" % status]
    if ses:
        bits.append(ses)
    bits.append(ex)
    if load is not None:
        bits.append("%gkg" % load)
    if setno is not None:
        bits.append("set%d" % setno)
    if rir is not None:
        bits.append("RIR%d" % rir)
    if side:
        bits.append(side)
    bits.append("pain=%d" % pain)
    if rom:
        bits.append(rom)
    if fault:
        bits.append("fault=%s" % fault)
    if action:
        bits.append("->%s" % action)
    line = " | ".join(bits)
    tail = []
    if guard:
        tail.append("guardrail: %s" % guard)
    if prog:
        tail.append("program: %s" % prog)
    if note:
        tail.append("note: %s" % note)
    if tail:
        line += "\n    " + " ; ".join(tail)
    return line


def cmd_add(a):
    c = conn()
    ts = a.ts or _now()
    cur = c.execute(
        """INSERT INTO pain_events
        (ts,session,exercise,load_kg,set_no,rir,side,pain,rom_phase,fault,action,note,status)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?, 'open')""",
        (ts, a.session, a.exercise, a.load, a.set_no, a.rir, a.side, a.pain,
         a.rom, a.fault, a.action, a.note))
    c.commit()
    eid = cur.lastrowid
    print("ADDED #%d  %s  %s  pain=%d  side=%s  fault=%s"
          % (eid, ts, a.exercise, a.pain, a.side or "NA", a.fault or "NA"))
    # nudge the post-session raise if this is a real hit
    print("OPEN_EVENT logged. raise at POST_SESSION (pain.py recent).")


def cmd_list(a):
    c = conn()
    q = "SELECT * FROM pain_events"
    conds, args = [], []
    if a.exercise:
        conds.append("exercise LIKE ?"); args.append("%%%s%%" % a.exercise)
    if a.open:
        conds.append("status='open'")
    if a.days:
        cutoff = (datetime.now() - timedelta(days=a.days)).strftime("%Y-%m-%d %H:%M")
        conds.append("ts >= ?"); args.append(cutoff)
    if conds:
        q += " WHERE " + " AND ".join(conds)
    q += " ORDER BY ts DESC, id DESC"
    rows = c.execute(q, args).fetchall()
    if not rows:
        print("NO_EVENTS")
        return
    for r in rows:
        print(_row(r))


def cmd_recent(a):
    a.exercise = None; a.open = True; a.days = a.days or None
    cmd_list(a)


def cmd_resolve(a):
    c = conn()
    r = c.execute("SELECT id FROM pain_events WHERE id=?", (a.id,)).fetchone()
    if not r:
        print("NO_SUCH_EVENT #%d" % a.id); sys.exit(1)
    sets, args = [], []
    if a.guardrail is not None:
        sets.append("guardrail=?"); args.append(a.guardrail)
    if a.note is not None:
        sets.append("note=?"); args.append(a.note)
    if a.program_change is not None:
        sets.append("program_change=?"); args.append(a.program_change)
    sets.append("status=?"); args.append("open" if a.reopen else "resolved")
    args.append(a.id)
    c.execute("UPDATE pain_events SET %s WHERE id=?" % ",".join(sets), args)
    c.commit()
    print("RESOLVED #%d" % a.id if not a.reopen else "REOPENED #%d" % a.id)
    print(_row(c.execute("SELECT * FROM pain_events WHERE id=?", (a.id,)).fetchone()))


def cmd_show(a):
    c = conn()
    r = c.execute("SELECT * FROM pain_events WHERE id=?", (a.id,)).fetchone()
    if not r:
        print("NO_SUCH_EVENT #%d" % a.id); sys.exit(1)
    print(_row(r))


def cmd_audit(a):
    """Pattern scan for program review. Flags when the SAME movement keeps
    hurting the same way, or pain is trending up. Coaching signal, not a verdict."""
    c = conn()
    cutoff = (datetime.now() - timedelta(days=a.window_days)).strftime("%Y-%m-%d %H:%M")
    rows = c.execute("SELECT * FROM pain_events WHERE ts >= ? ORDER BY ts ASC",
                     (cutoff,)).fetchall()
    if not rows:
        print("NO_EVENTS in window (%dd)" % a.window_days); return
    # group by exercise (+ fault) and exercise (+ side)
    by_ef, by_es, by_ex = {}, {}, {}
    for r in rows:
        ex, side, pain, fault = r[3], r[7], r[8], r[10]
        by_ef.setdefault((ex, fault or "unknown"), []).append(r)
        by_es.setdefault((ex, side or "NA"), []).append(r)
        by_ex.setdefault(ex, []).append((r[1], pain))
    flagged = False
    print("AUDIT window=%dd threshold=%d events=%d" % (a.window_days, a.threshold, len(rows)))
    for (ex, fault), rs in sorted(by_ef.items(), key=lambda kv: -len(kv[1])):
        if len(rs) >= a.threshold:
            flagged = True
            avg = sum(x[8] for x in rs) / len(rs)
            print("FLAG recurring-fault: %s x %s -> %d hits, avg pain %.1f  => PROGRAM REVIEW"
                  % (ex, fault, len(rs), avg))
    for (ex, side), rs in sorted(by_es.items(), key=lambda kv: -len(kv[1])):
        if side != "NA" and len(rs) >= a.threshold:
            flagged = True
            print("FLAG recurring-side: %s on %s -> %d hits  => check L/R imbalance"
                  % (ex, side, len(rs)))
    # rising trend: any exercise whose last pain > first pain and >=3 samples
    for ex, seq in by_ex.items():
        if len(seq) >= 3:
            seq = sorted(seq)
            if seq[-1][1] > seq[0][1]:
                flagged = True
                print("FLAG rising-pain: %s  %d -> %d over %d events  => PROGRAM REVIEW"
                      % (ex, seq[0][1], seq[-1][1], len(seq)))
    if not flagged:
        print("NO_FLAGS -- nothing crosses threshold yet")


def build_parser():
    p = argparse.ArgumentParser(prog="pain.py")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    # F34: --exercise MUST be the program.yaml slot name in English snake_case
    # (e.g. incline_dumbbell_press, v_squat), NOT a Korean display label. audit
    # groups by exact string match, so a Korean/English mix for the same
    # movement splits the group and hides recurring / rising patterns. For a
    # non-slot report (pre-session check-in, an ad-hoc primer) use a stable
    # English key such as pre-session-checkin_<area>.
    a.add_argument("--exercise", required=True,
                   help="program.yaml slot name, English snake_case (F34)")
    a.add_argument("--pain", type=int, required=True, help="0-10")
    a.add_argument("--side", choices=["L", "R", "both", "NA"])
    a.add_argument("--load", type=float)
    a.add_argument("--set-no", type=int)
    a.add_argument("--rir", type=int)
    a.add_argument("--rom", choices=ROM_PHASES)
    a.add_argument("--fault", help="one of: %s (free text ok)" % ",".join(FAULTS))
    a.add_argument("--action", choices=ACTIONS)
    a.add_argument("--session", help="split e.g. 앞A / 뒷B")
    a.add_argument("--note")
    a.add_argument("--ts", help="override YYYY-MM-DD HH:MM (default now)")
    a.set_defaults(fn=cmd_add)

    l = sub.add_parser("list")
    l.add_argument("--exercise")
    l.add_argument("--days", type=int)
    l.add_argument("--open", action="store_true")
    l.set_defaults(fn=cmd_list)

    r = sub.add_parser("recent")
    r.add_argument("--days", type=int)
    r.set_defaults(fn=cmd_recent)

    rs = sub.add_parser("resolve")
    rs.add_argument("--id", type=int, required=True)
    rs.add_argument("--guardrail")
    rs.add_argument("--note")
    rs.add_argument("--program-change", dest="program_change")
    rs.add_argument("--reopen", action="store_true")
    rs.set_defaults(fn=cmd_resolve)

    s = sub.add_parser("show")
    s.add_argument("--id", type=int, required=True)
    s.set_defaults(fn=cmd_show)

    au = sub.add_parser("audit")
    au.add_argument("--window-days", type=int, default=30)
    au.add_argument("--threshold", type=int, default=3)
    au.set_defaults(fn=cmd_audit)
    return p


if __name__ == "__main__":
    args = build_parser().parse_args()
    args.fn(args)
