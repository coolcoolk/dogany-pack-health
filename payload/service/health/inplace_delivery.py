#!/usr/bin/env python3
"""inplace_delivery.py -- deliver a live-session surface IN PLACE: the first
send is a new message, every later render of the same surface edits that
message instead of stacking another one.

WHY (session UX intent spec 2026-08-20 s.0-2; owner 2026-08-21 "같은 메시지
인플레이스 스왑, 새 메시지 0"). The set table (표2) is re-rendered at every set
boundary. Until now each render was a NEW message (CHANGELOG: "인플레이스가
아니라 새 메시지다") because routines/push.sh had no edit call and returned no
message_id. push.sh --strict now returns {"ok":true,"message_id":N,
"chat_id":C} (DGN-1683 WP3); the edit call is the bridge/template seam built
by the framework as DGN-1803 (see SEAM). This module is the pack half, ready for it:

  * it records (message_id, chat_id) per SURFACE KEY (e.g.
    "set-table:<session>:<exercise>") under STATE_DIR/.inplace/;
  * it edits only when push.sh DECLARES the capability
    (`push.sh --capabilities` prints a line containing the word `edit`);
    a push.sh without it (framework before v2.6.0-dev.68) gets exactly the
    old behavior -- a new message per render;
  * every edit outcome that leaves the owner without the table falls back to
    a new message, EXCEPT "uncertain" (the edit may have landed: a second
    message would be the duplicate the spec forbids -- see UNCERTAIN below;
    the caller says so instead of re-posting the body).

SEAM (framework push.sh, DGN-1803, v2.6.0-dev.68):
  push.sh --capabilities                 -> stdout lists `edit`, rc 0
  push.sh --strict --edit <message_id> --chat <chat_id> --text <body>
          [--buttons-json <rows>]
      rc 0  edited      stdout {"ok":true,"message_id":N,"chat_id":C,"edited":true}
      rc 7  not editable (deleted, too old, not this bot's) -> send new
      rc 8  not modified (same body)                        -> nothing to do
      rc 6  uncertain (transport error)                     -> no new send
      other = not edited (strict rc table)                  -> send new

KEYBOARD (framework 2026-09-30, DGN-1803 review): editMessageText without
reply_markup REMOVES the message's inline keyboard. So the keyboard is part
of the surface, exactly like the body:
  * `buttons` = rows of {"text", "callback_data"} (push.sh --buttons-json);
    None = keep the rows this surface already carries (from the record),
    [] = no keyboard. Every send AND every edit passes the effective rows,
    so an edit never strips a keyboard by omission.
  * the record's hash covers body + rows: a keyboard-only change is an edit,
    not "unchanged". With no rows the hash is the body hash alone, so a
    record written before this change still matches its body.

UNCERTAIN NEVER DUPLICATES. An edit that may have landed (rc 6, a timeout,
or rc 0 whose reply cannot be read) never falls through to a new send and
never drops the record. A fast rc 6 retries the SAME edit once -- an edit is
idempotent (a landed first attempt answers rc 8); a timeout is not retried.
After that the outcome is "edit_uncertain" and the next render edits the
same message.

Never raises. Model-free. stdlib only.
"""

import hashlib
import json
import os
import re
import subprocess
import time

RC_EDIT_OK = 0
RC_UNCERTAIN = 6
RC_NOT_EDITABLE = 7
RC_NOT_MODIFIED = 8

# Telegram lets a bot edit its own message for 48 h; a live session is hours.
# Past this the surface is treated as gone (new message), so a stale record
# from a previous day can never pull an old table back into view.
MAX_EDIT_AGE_SEC = 6 * 3600

# An uncertain edit is retried once, and only after a FAST failure (curl
# connect blips return in well under a second). A slow one is a timeout;
# retrying it would double a live beat's worst case.
EDIT_RETRY_FAST_FAIL_SEC = 5
EDIT_RETRY_TIMEOUT_SEC = 10

# push.sh's own --buttons-json gate (callback_data <= 64 bytes, Telegram).
CALLBACK_DATA_MAX_BYTES = 64

_KEY_SAFE = re.compile(r"[^A-Za-z0-9_.:-]")
_CAPS = {}


def _record_path(state_dir, key):
    return os.path.join(state_dir, ".inplace",
                        _KEY_SAFE.sub("_", key) + ".json")


def read_record(state_dir, key):
    try:
        with open(_record_path(state_dir, key), encoding="utf-8") as fh:
            rec = json.load(fh)
    except (OSError, ValueError):
        return None
    if not isinstance(rec, dict) or not isinstance(rec.get("message_id"), int):
        return None
    return rec


def write_record(state_dir, key, message_id, chat_id, body, now=None,
                 buttons=None):
    path = _record_path(state_dir, key)
    rec = {"message_id": message_id, "chat_id": chat_id,
           "sha": _sha(body, buttons), "sent_at": now or time.time()}
    if buttons:
        rec["buttons"] = buttons
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as fh:
            json.dump(rec, fh, ensure_ascii=False)
        os.replace(tmp, path)
        return True
    except OSError:
        return False


def drop_record(state_dir, key):
    try:
        os.unlink(_record_path(state_dir, key))
    except OSError:
        pass


def _sha(body, buttons=None):
    """Hash of what the surface shows: body, plus the keyboard rows when it
    has any. No rows -> the body hash alone (pre-keyboard records match)."""
    text = body or ""
    if buttons:
        text += "\n\0" + _buttons_json(buttons)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def _buttons_json(rows):
    return json.dumps(rows, ensure_ascii=False, separators=(",", ":"))


def valid_buttons(rows):
    """True for [] or rows push.sh --buttons-json accepts: a list of non-empty
    lists of {"text", "callback_data"} (non-empty strings, callback_data at
    most 64 UTF-8 bytes). Checked here so a bad keyboard is refused before
    any call instead of failing the strict gate after a record decision."""
    if not isinstance(rows, list):
        return False
    for row in rows:
        if not isinstance(row, list) or not row:
            return False
        for b in row:
            if not isinstance(b, dict) or set(b) != {"text", "callback_data"}:
                return False
            text, data = b["text"], b["callback_data"]
            if not isinstance(text, str) or not text.strip():
                return False
            if not isinstance(data, str) or not data or \
                    len(data.encode("utf-8")) > CALLBACK_DATA_MAX_BYTES:
                return False
    return True


def _record_buttons(rec):
    rows = (rec or {}).get("buttons")
    return rows if rows and valid_buttons(rows) else []


def _with_buttons(argv, rows):
    if rows:
        argv += ["--buttons-json", _buttons_json(rows)]
    return argv


def can_edit(push_bin, timeout=5):
    """True when push.sh declares the edit call. Cached per binary."""
    if push_bin in _CAPS:
        return _CAPS[push_bin]
    ok = False
    try:
        p = subprocess.run([push_bin, "--capabilities"], capture_output=True,
                           text=True, timeout=timeout)
        ok = p.returncode == 0 and bool(re.search(r"\bedit\b", p.stdout or ""))
    except Exception:  # noqa: BLE001 -- no capability, never a crash
        ok = False
    _CAPS[push_bin] = ok
    return ok


def _strict_json(stdout):
    for line in reversed((stdout or "").strip().splitlines()):
        try:
            res = json.loads(line)
        except ValueError:
            continue
        if isinstance(res, dict) and res.get("ok") is True and \
                isinstance(res.get("message_id"), int) and \
                not isinstance(res.get("message_id"), bool):
            return res
    return None


def _run(argv, timeout):
    try:
        p = subprocess.run(argv, capture_output=True, text=True,
                           timeout=timeout)
        return p.returncode, p.stdout
    except Exception:  # noqa: BLE001
        return None, ""


def send_new(push_bin, body, state_dir, key, timeout=25, now=None,
             buttons=None):
    """(ok, detail, message_id): one strict send; records the id."""
    rows = buttons or []
    rc, out = _run(_with_buttons([push_bin, "--strict", "--text", body],
                                 rows), timeout)
    res = _strict_json(out) if rc == 0 else None
    if res is None:
        return False, "send_rc=%s" % rc, None
    write_record(state_dir, key, res["message_id"], res.get("chat_id"), body,
                 now=now, buttons=rows)
    return True, "sent", res["message_id"]


def _edit_once(argv, timeout):
    """One edit call -> (outcome, retryable): outcome is "edited" |
    "unchanged" | "uncertain" | "gone". rc 0 with an unreadable reply is
    uncertain: Telegram took the edit, so a new send would be the duplicate.
    Only push.sh's own fast rc 6 is retryable -- never a timeout."""
    t0 = time.time()
    rc, out = _run(argv, timeout)
    elapsed = time.time() - t0
    if rc == RC_EDIT_OK:
        return ("edited" if _strict_json(out) is not None
                else "uncertain"), False
    if rc == RC_NOT_MODIFIED:
        return "unchanged", False
    if rc == RC_UNCERTAIN:
        return "uncertain", elapsed < EDIT_RETRY_FAST_FAIL_SEC
    if rc is None:
        return "uncertain", False
    return "gone", False


def deliver(key, body, push_bin, state_dir, timeout=25, now=None,
            buttons=None):
    """Deliver `body` (+ keyboard) for surface `key`. Returns
    (ok, detail, message_id):

        (True,  "edited",    mid)  the recorded message now shows `body`
        (True,  "unchanged", mid)  it already did (same body+rows / rc 8)
        (True,  "sent",      mid)  a new message (first render, no edit
                                   capability, or the old one is gone)
        (False, "edit_uncertain", mid)  edit may have landed; NO new send,
                                   record kept -- the caller must not
                                   re-post the body either
        (False, "<reason>",  None)  nothing delivered -- caller falls back

    `buttons`: None = keep this surface's recorded rows, [] = no keyboard,
    rows = that keyboard (see KEYBOARD above).
    """
    body = (body or "").strip()
    if not body:
        return False, "empty", None
    if buttons is not None and not valid_buttons(buttons):
        return False, "bad_buttons", None
    if not push_bin or not os.path.exists(push_bin):
        return False, "no_push_binary", None
    now = now or time.time()
    rec = read_record(state_dir, key)
    if rec and now - float(rec.get("sent_at") or 0) > MAX_EDIT_AGE_SEC:
        drop_record(state_dir, key)
        rec = None
    rows = _record_buttons(rec) if buttons is None else buttons
    if rec and can_edit(push_bin):
        mid = rec["message_id"]
        if rec.get("sha") == _sha(body, rows):
            return True, "unchanged", mid
        argv = [push_bin, "--strict", "--edit", str(mid), "--text", body]
        if rec.get("chat_id") is not None:
            argv[4:4] = ["--chat", str(rec["chat_id"])]
        argv = _with_buttons(argv, rows)
        outcome, retryable = _edit_once(argv, timeout)
        if retryable:
            outcome, _ = _edit_once(argv, min(timeout,
                                              EDIT_RETRY_TIMEOUT_SEC))
        if outcome in ("edited", "unchanged"):
            write_record(state_dir, key, mid, rec.get("chat_id"), body,
                         now=rec.get("sent_at"), buttons=rows)
            return True, outcome, mid
        if outcome == "uncertain":
            return False, "edit_uncertain", mid
        drop_record(state_dir, key)          # rc 7 / any other: gone
    return send_new(push_bin, body, state_dir, key, timeout, now,
                    buttons=rows)


def shows(state_dir, key, body, buttons=None, now=None):
    """Does the recorded message for `key` show exactly `body` (+ rows)?
    True / False, or None when there is no live record (nothing in place).
    For content ledgers that predate in-place: a table delivered once may
    since have been edited away (undo, re-log), so "delivered before" is no
    longer "on the screen now"."""
    rec = read_record(state_dir, key)
    if rec is None or \
            (now or time.time()) - float(rec.get("sent_at") or 0) > \
            MAX_EDIT_AGE_SEC:
        return None
    rows = _record_buttons(rec) if buttons is None else buttons
    return rec.get("sha") == _sha((body or "").strip(), rows)


def surface_key(kind, session_id, exercise_name=None):
    """Canonical key: one in-place surface per (kind, session[, exercise])."""
    parts = [kind, str(session_id)]
    if exercise_name:
        parts.append(exercise_name)
    return ":".join(parts)
