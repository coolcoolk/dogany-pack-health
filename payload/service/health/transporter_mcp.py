#!/usr/bin/env python3
"""transporter_mcp.py -- minimal stdio MCP client for the Transporter receiver.

The Transporter (iPhone/Watch -> Mac receiver) exposes its store through a
stdio MCP server (`transporter-mcp`, tools list_events / get_event /
refresh_events). A scheduled routine has no MCP host around it, so this module
IS the host: it spawns the server, runs the JSON-RPC 2.0 handshake
(initialize -> notifications/initialized) and calls tools. stdlib only.

Server command, first hit wins:
  1. the `command` argument (callers pass HK_TRANSPORTER_MCP from pack config)
  2. $HK_TRANSPORTER_MCP
  3. ~/.transporter/venv/bin/transporter-mcp   (the receiver's own install)
The value is split with shlex, so a test stub can be `python3 stub.py`.

Result decoding: a tool result carries `structuredContent` (newer servers,
{"result": <value>} for non-object returns) and/or `content` text items. The
structured form wins; text items are JSON-decoded, and several items are read
as one list (older servers emit one item per list element).
"""

import json
import os
import shlex
import subprocess

PROTOCOL_VERSION = "2025-06-18"
DEFAULT_COMMAND = os.path.join(os.path.expanduser("~"), ".transporter",
                               "venv", "bin", "transporter-mcp")


class TransporterError(Exception):
    """The server could not be reached, or a tool call failed."""


class ToolFailed(TransporterError):
    """The tool ran and reported an error (e.g. get_event: not found)."""


def resolve_command(command=None):
    cmd = command or os.environ.get("HK_TRANSPORTER_MCP") or DEFAULT_COMMAND
    return shlex.split(cmd)


class Client(object):
    def __init__(self, command=None, timeout=60):
        self.argv = resolve_command(command)
        self.timeout = timeout
        self.proc = None
        self._next = 0

    # -- lifecycle -----------------------------------------------------------
    def __enter__(self):
        self.open()
        return self

    def __exit__(self, *exc):
        self.close()

    def open(self):
        try:
            self.proc = subprocess.Popen(
                self.argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL, text=True, encoding="utf-8",
                bufsize=1)
        except OSError as exc:
            raise TransporterError("cannot start %s: %s"
                                   % (" ".join(self.argv), exc))
        self._request("initialize", {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {},
            "clientInfo": {"name": "pack_health-hk-ingest", "version": "1"},
        })
        self._send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def close(self):
        p, self.proc = self.proc, None
        if p is None:
            return
        try:
            p.stdin.close()
        except OSError:
            pass
        try:
            p.wait(timeout=5)
        except subprocess.TimeoutExpired:
            p.kill()
            p.wait()

    # -- wire ----------------------------------------------------------------
    def _send(self, msg):
        try:
            self.proc.stdin.write(json.dumps(msg) + "\n")
            self.proc.stdin.flush()
        except (OSError, ValueError) as exc:
            raise TransporterError("transporter server closed: %s" % exc)

    def _request(self, method, params):
        self._next += 1
        rid = self._next
        self._send({"jsonrpc": "2.0", "id": rid, "method": method,
                    "params": params})
        while True:
            line = self.proc.stdout.readline()
            if not line:
                raise TransporterError("transporter server exited during %s"
                                       % method)
            line = line.strip()
            if not line:
                continue
            try:
                msg = json.loads(line)
            except ValueError:
                continue          # a stray log line on stdout; not ours
            if msg.get("id") != rid:
                continue          # notification / progress / other id
            if "error" in msg:
                raise TransporterError("%s: %s" % (method, msg["error"]))
            return msg.get("result") or {}

    # -- tools ---------------------------------------------------------------
    def call(self, name, **arguments):
        args = dict((k, v) for k, v in arguments.items() if v is not None)
        res = self._request("tools/call", {"name": name, "arguments": args})
        if res.get("isError"):
            texts = [c.get("text", "") for c in res.get("content") or []]
            raise ToolFailed("%s: %s" % (name, " ".join(texts).strip()))
        return decode_result(res)

    def list_events(self, source=None, kind=None, since=None, limit=500):
        out = self.call("list_events", source=source, kind=kind,
                        since=since, limit=limit)
        if isinstance(out, dict):
            out = [out]
        return list(out or [])

    def get_event(self, source, kind, id):
        """The event, or None when the store has no such id."""
        try:
            return self.call("get_event", source=source, kind=kind, id=id)
        except ToolFailed as exc:
            if "not found" in str(exc):
                return None
            raise

    def refresh_events(self, kinds=None, wait_s=20):
        return self.call("refresh_events", kinds=kinds, wait_s=wait_s)


def decode_result(res):
    sc = res.get("structuredContent")
    if isinstance(sc, dict):
        if set(sc.keys()) == {"result"}:
            return sc["result"]
        return sc
    items = []
    for c in res.get("content") or []:
        if c.get("type") != "text":
            continue
        try:
            items.append(json.loads(c.get("text", "")))
        except ValueError:
            items.append(c.get("text", ""))
    if len(items) == 1:
        return items[0]
    return items
