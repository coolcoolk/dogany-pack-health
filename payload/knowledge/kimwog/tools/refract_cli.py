#!/usr/bin/env python3
"""Thin production CLI entry point for the kimwog refraction engine (DGN-398 Phase 2).

WHAT THIS IS
------------
A deterministic entry point over the existing refract() function. The caller
(a skill) fetches measured axis values from its own record store and passes
them in as arguments. This file does NOT read kit_life.db or any live user
data store -- it is 100% data-in-from-args, deterministic.

USAGE
-----
  refract_cli.py [--root DIR] <item> \\
      [--measured KEY=VALUE[@DATE]] ... \\
      [--profile-json '<json>'] \\
      [--profile-file <path>] \\
      [--now YYYY-MM-DD] \\
      [--demo]

  <item>              item ID (nutrition/protein-intake-002), alias, or file path.
  --measured          KEY=VALUE or KEY=VALUE@DATE; repeatable. Numbers parsed
                      as float, else kept as string. VALUE after the first @
                      is the measured_at date; if omitted, defaults to --now.
  --profile-json      JSON object of stated axis rows (same shape profile_axes
                      dict refract() expects: {key: {value, as_of, status}}).
  --profile-file      path to a JSON file with the same shape as --profile-json.
  --now               reference date YYYY-MM-DD (default: today from
                      datetime.date.today().isoformat()). Passed in explicitly
                      to keep the contract fully deterministic: the value is
                      visible in the output so callers can pin it.
  --demo              run the built-in self-test demo instead of processing
                      a user-supplied item (reproduces the _demo() behaviour).

Output: refraction result as JSON on stdout. Exit 0 on success, nonzero on
usage or validation errors (message on stderr).

Python 3 stdlib only. No new dependencies introduced.
"""

import argparse
import datetime
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import kimwog   # noqa: E402
import refract  # noqa: E402


# --------------------------------------------------------------------------
# Item resolution: ID / alias / file path -> frontmatter dict
# --------------------------------------------------------------------------

def _resolve_item(token, root):
    """Resolve a token to a frontmatter dict.

    Resolution order:
      1. Item ID (domain/slug-NNN or e/domain/NNN) -- tried first; parse_item_id
         validates the grammar so a well-formed ID never falls through to the file
         path branch accidentally.
      2. Exact file path (.md suffix or absolute path) -- for callers that pass
         a literal file path.
      3. Alias resolution via registry domain aliases on the domain component of
         an ID-shaped token.

    Returns (frontmatter_dict, resolved_path_for_error_messages).
    Raises ValueError on not-found or parse failure.
    """
    domains = kimwog.load_registry(root)

    # 1. file path: explicit .md suffix or absolute path that exists.
    # We check this ONLY when the token cannot be an item ID, to avoid treating
    # "nutrition/protein-intake-002" (a valid ID grammar) as a relative path.
    is_item_id_shape = kimwog.parse_item_id(token) is not None
    if not is_item_id_shape and (token.endswith(".md") or os.path.isabs(token)):
        path = token if os.path.isabs(token) else os.path.join(os.getcwd(), token)
        if not os.path.isfile(path):
            raise ValueError("item file not found: %s" % path)
        fm, _ = kimwog.read_frontmatter(path)
        return fm, path

    # 2. Treat as item ID or possibly a domain-alias-prefixed ID.
    # Normalize: resolve the domain component through registry aliases.
    resolved_id = _normalize_item_id(token, domains)

    # Walk all item files comparing their `id` field.
    for path in kimwog.iter_item_files(root):
        try:
            fm, _ = kimwog.read_frontmatter(path)
        except Exception:
            continue
        if fm.get("id") == resolved_id or fm.get("id") == token:
            return fm, path

    raise ValueError(
        "item %r not found in warehouse %s (tried id lookup and alias resolution)"
        % (token, root))


def _normalize_item_id(token, domains):
    """Attempt to alias-resolve the domain component of a token that looks like
    an item ID. Returns the potentially redirected ID string, or token unchanged
    if it does not look like an item ID."""
    parsed = kimwog.parse_item_id(token)
    if not parsed:
        return token
    _kind, domain, _tail = parsed
    res = kimwog.resolve_domain(domain, domains)
    if res.canonical and res.canonical != domain:
        # replace the domain prefix in the raw token
        return res.canonical + token[len(domain):]
    return token


# --------------------------------------------------------------------------
# --measured argument parsing: KEY=VALUE[@DATE]
# --------------------------------------------------------------------------

def _parse_measured_arg(raw, default_date):
    """Parse a single --measured argument: KEY=VALUE or KEY=VALUE@DATE.

    VALUE is parsed as float if possible, kept as string otherwise.
    DATE defaults to default_date (the --now value) when not supplied.

    Returns (axis_name, {"value": v, "measured_at": date}).
    Raises ValueError on bad syntax.
    """
    if "=" not in raw:
        raise ValueError(
            "--measured argument must be KEY=VALUE or KEY=VALUE@DATE, got: %r"
            % raw)
    key, rest = raw.split("=", 1)
    key = key.strip()
    if not key:
        raise ValueError("--measured KEY is empty in: %r" % raw)

    # split on last '@' to allow values that contain '@' in theory, though
    # in practice axis values are plain numbers or short strings. Using the
    # FIRST '@' that appears after the '=' is the convention documented in
    # the usage string (VALUE@DATE), and is the conservative choice.
    if "@" in rest:
        at_idx = rest.index("@")
        value_str = rest[:at_idx]
        date_str = rest[at_idx + 1:]
        if not date_str:
            raise ValueError(
                "--measured date part is empty in: %r (use KEY=VALUE@YYYY-MM-DD)"
                % raw)
    else:
        value_str = rest
        date_str = default_date

    # parse value: float if possible, else string
    try:
        value = float(value_str)
    except ValueError:
        value = value_str

    return key, {"value": value, "measured_at": date_str}


def _build_adapter(measured_args, default_date):
    """Build a DictLifekitAdapter from a list of raw --measured strings."""
    table = {}
    for raw in (measured_args or []):
        try:
            key, row = _parse_measured_arg(raw, default_date)
        except ValueError as exc:
            _die(str(exc))
        if key in table:
            _die("--measured axis %r specified more than once" % key)
        table[key] = row
    return refract.DictLifekitAdapter(table)


# --------------------------------------------------------------------------
# --profile-json / --profile-file loading
# --------------------------------------------------------------------------

def _load_profile(profile_json, profile_file):
    """Load profile_axes from --profile-json or --profile-file (or return {})."""
    if profile_json and profile_file:
        _die("specify only one of --profile-json or --profile-file, not both")
    if profile_json:
        try:
            data = json.loads(profile_json)
        except json.JSONDecodeError as exc:
            _die("--profile-json parse error: %s" % exc)
        if not isinstance(data, dict):
            _die("--profile-json must be a JSON object, got %s" % type(data).__name__)
        return data
    if profile_file:
        if not os.path.isfile(profile_file):
            _die("--profile-file not found: %s" % profile_file)
        try:
            with open(profile_file, "r", encoding="utf-8") as fh:
                data = json.load(fh)
        except (json.JSONDecodeError, OSError) as exc:
            _die("--profile-file read error: %s" % exc)
        if not isinstance(data, dict):
            _die("--profile-file must contain a JSON object")
        return data
    return {}


# --------------------------------------------------------------------------
# Error helper
# --------------------------------------------------------------------------

def _die(msg):
    print("error: " + msg, file=sys.stderr)
    sys.exit(1)


# --------------------------------------------------------------------------
# main()
# --------------------------------------------------------------------------

def main(argv):
    ap = argparse.ArgumentParser(
        prog="refract_cli.py",
        description="Deterministic refraction CLI for a kimwog warehouse (DGN-398).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  refract_cli.py nutrition/protein-intake-002 \\\n"
            "      --measured body_weight_kg=80@2026-07-05 --now 2026-07-06\n"
            "\n"
            "  refract_cli.py exercise/creatine-ergogenic-001 \\\n"
            "      --measured age_years=28 \\\n"
            "      --profile-json '{\"renal_condition\": "
            "{\"value\": \"healthy\", \"as_of\": \"2026-07-01\", \"status\": \"set\"}}'\n"
        ),
    )
    ap.add_argument(
        "--root", default=kimwog.default_root(),
        help="warehouse root directory (default: this warehouse)")
    ap.add_argument(
        "item", nargs="?",
        help="item ID (domain/slug-NNN), alias, or file path")
    ap.add_argument(
        "--measured", metavar="KEY=VALUE[@DATE]", action="append", default=[],
        help="measured axis value; repeatable. Number parsed as float, else string. "
             "DATE defaults to --now when omitted.")
    ap.add_argument(
        "--profile-json", metavar="JSON",
        help="stated axis rows as a JSON object "
             "({key: {value, as_of, status}})")
    ap.add_argument(
        "--profile-file", metavar="PATH",
        help="path to a JSON file with the same shape as --profile-json")
    ap.add_argument(
        "--now", metavar="YYYY-MM-DD", default=None,
        help="reference date for determinism (default: today, "
             "datetime.date.today().isoformat()). Always echoed in output.")
    ap.add_argument(
        "--demo", action="store_true",
        help="run the built-in self-test demo (ignores other arguments)")

    args = ap.parse_args(argv)

    # --demo: delegate to the existing _demo() self-test and exit.
    if args.demo:
        refract._demo()
        return 0

    # item is required outside of --demo
    if not args.item:
        ap.print_usage(sys.stderr)
        print("error: item argument is required (or use --demo)", file=sys.stderr)
        return 2

    # --now: default to today, explicit and documented in output for
    # determinism traceability. The calling skill should pass this explicitly
    # when pinning results; the default is a pragmatic convenience for
    # interactive use and does not violate the engine contract (refract()
    # only uses `now` for volatile-axis age checks, not for clock-dependent
    # output -- the same item+axes+now always yields the same result).
    now = args.now or datetime.date.today().isoformat()

    # resolve item -> frontmatter
    root = args.root
    try:
        fm, item_path = _resolve_item(args.item, root)
    except ValueError as exc:
        _die(str(exc))

    # build adapter from --measured args
    adapter = _build_adapter(args.measured, now)

    # load profile_axes from --profile-json / --profile-file
    profile_axes = _load_profile(args.profile_json, args.profile_file)

    # load ledger
    ledger = refract.Ledger.from_root(root)

    # run the deterministic engine
    result = refract.refract(fm, ledger, adapter, profile_axes, now)

    # emit JSON to stdout; include now in output for traceability
    out = result.to_dict()
    out["_now"] = now  # injected for traceability (not part of engine schema)
    print(json.dumps(out, indent=2, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
