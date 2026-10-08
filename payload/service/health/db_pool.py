#!/usr/bin/env python3
"""db_pool.py -- per-process reuse of one sqlite connection per DB file.

WHY (2026-10-06, measured). Opening a connection to the kit DB and running its
first statement costs ~4.7 ms: sqlite parses the whole schema (~370 objects) on
every new connection. A statement on an already-open connection costs ~0.09 ms.
rx-calc / set-table / set-arm / session-cursor open a fresh connection for
almost every lookup -- one set-arm ran ~1,600 of them, 6-7 s of CPU that was
nearly all schema parsing. `connect()` below hands every caller in the process
the SAME underlying connection (per DB file, per thread), so the schema is
parsed once.

WHAT IT KEEPS EXACT. Each `connect()` returns a fresh handle object with the
semantics a caller of `sqlite3.connect()` relied on:
  * reads see the latest committed data -- the shared connection never holds a
    read transaction open between statements (no snapshot is kept, so a write
    by another process is seen exactly as it was with a new connection);
  * `close()` finalizes the cursors this handle made and rolls back anything
    it left uncommitted -- what closing a real connection does -- and the
    handle is unusable afterwards;
  * `with conn:` commits / rolls back as before; `row_factory` is per handle.
Nothing is cached but the connection itself: there is no result cache, so no
write (in this process or any other) can ever be served stale.

NOT POOLED (falls through to sqlite3.connect): ':memory:', `uri=True` opens,
and a path that does not exist yet (sqlite would create it). A pooled
connection whose file was replaced (different inode) is dropped and reopened.
"""

import os
import sqlite3
import threading
import weakref

_POOL = {}         # key -> [(connection, file id, weakref to owning handle)]
_MAX_PER_KEY = 8


def _file_id(path):
    try:
        st = os.stat(path)
    except OSError:
        return None
    return (st.st_dev, st.st_ino)


class _Cursor(sqlite3.Cursor):
    """A cursor that keeps its handle alive, as a real cursor keeps its
    connection alive (a function may return conn.execute(...) and drop conn)."""
    _handle = None


class PooledConnection(object):
    """One caller's view of the shared connection (see module docstring).
    While this handle is open it owns the connection exclusively: a second
    connect() in the meantime gets a separate connection, exactly as before."""

    def __init__(self, real):
        object.__setattr__(self, "_real", real)
        object.__setattr__(self, "_cursors", [])
        object.__setattr__(self, "_closed", False)
        object.__setattr__(self, "row_factory", None)

    def _check(self):
        if self._closed:
            raise sqlite3.ProgrammingError(
                "Cannot operate on a closed database.")

    def cursor(self, factory=None):
        self._check()
        if factory is not None:
            return self._real.cursor(factory)
        cur = self._real.cursor(_Cursor)
        cur._handle = self
        cur.row_factory = self.row_factory
        self._cursors.append(weakref.ref(cur))
        if len(self._cursors) > 64:
            self._cursors[:] = [r for r in self._cursors if r() is not None]
        return cur

    def execute(self, sql, parameters=()):
        return self.cursor().execute(sql, parameters)

    def executemany(self, sql, seq):
        return self.cursor().executemany(sql, seq)

    def executescript(self, script):
        return self.cursor().executescript(script)

    def commit(self):
        self._check()
        self._real.commit()

    def rollback(self):
        self._check()
        self._real.rollback()

    def close(self):
        """What closing a real connection does: finalize this handle's
        statements and discard anything it left uncommitted."""
        if self._closed:
            return
        for ref in self._cursors:
            cur = ref()
            if cur is not None:
                try:
                    cur.close()
                except sqlite3.Error:
                    pass
        del self._cursors[:]
        try:
            if self._real.in_transaction:
                self._real.rollback()
        except sqlite3.Error:
            pass
        object.__setattr__(self, "_closed", True)

    def __del__(self):
        # A dropped real connection rolls back when collected; so does this.
        try:
            self.close()
        except Exception:  # noqa: BLE001 -- interpreter teardown
            pass

    def __enter__(self):
        self._check()
        return self

    def __exit__(self, exc_type, exc, tb):
        return self._real.__exit__(exc_type, exc, tb)

    def __getattr__(self, name):
        self._check()
        return getattr(self._real, name)

    def __setattr__(self, name, value):
        if name == "row_factory":
            object.__setattr__(self, name, value)
        else:
            # Connection-level state would leak to the next handle: this
            # connection stops being shared.
            for slots in _POOL.values():
                slots[:] = [x for x in slots if x[0] is not self._real]
            setattr(self._real, name, value)


def connect(database, *args, **kwargs):
    """Drop-in for sqlite3.connect(database, ...) -- see module docstring."""
    if kwargs.get("uri") or not isinstance(database, (str, bytes, os.PathLike)):
        return sqlite3.connect(database, *args, **kwargs)
    path = os.fspath(database)
    if isinstance(path, bytes):
        path = os.fsdecode(path)
    if path in ("", ":memory:"):
        return sqlite3.connect(database, *args, **kwargs)
    fid = _file_id(path)
    if fid is None:
        return sqlite3.connect(database, *args, **kwargs)
    key = (os.getpid(), threading.get_ident(), os.path.abspath(path),
           args, tuple(sorted(kwargs.items())))
    slots = _POOL.setdefault(key, [])
    real = None
    for i, (cand, cfid, owner_ref) in enumerate(slots):
        owner = owner_ref()
        if owner is not None and not owner._closed:
            continue                      # busy: an open handle owns it
        if cfid != fid or cand.in_transaction:
            # The file was replaced (or state was left behind): drop it.
            try:
                cand.close()
            except sqlite3.Error:
                pass
            slots[i] = None
            continue
        real = cand
        slots[i] = None
        break
    slots[:] = [x for x in slots if x is not None]
    if real is None:
        # Every pooled connection is held by an open handle (a nested open):
        # a new one, exactly as before -- and it joins the pool.
        real = sqlite3.connect(database, *args, **kwargs)
    handle = PooledConnection(real)
    if len(slots) < _MAX_PER_KEY:
        slots.append((real, fid, weakref.ref(handle)))
    return handle
