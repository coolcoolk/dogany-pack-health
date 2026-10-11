#!/usr/bin/env python3
"""Alias-resolution utility for a Kimwog warehouse.

Alias resolution ALWAYS precedes item-status lookup (v3 section 5.3 / DGN-118
F2 MAJOR-2). A resolved-but-tombstoned target renders as "retracted", never
"missing". Consumed by the answer path (DGN-175) and the retraction fan-out
(DGN-171).

Usage:
  resolve.py [--root DIR] <slug-or-id> [<slug-or-id> ...]

Accepts a bare domain slug (exercise, skill-learning), a full item ID
(exercise/creatine-ergogenic-001), or an E-record ID (e/nutrition/003). Prints
the canonical domain, its status, and the render verdict.
"""

import argparse
import sys

import kimwog


def resolve_one(token, domains):
    parsed = kimwog.parse_item_id(token)
    if parsed:
        _kind, domain, _tail = parsed
        res = kimwog.resolve_domain(domain, domains)
        item_render = "missing" if res.render == "missing" else res.render
        return domain, res, item_render
    res = kimwog.resolve_domain(token, domains)
    return token, res, res.render


def main(argv):
    ap = argparse.ArgumentParser(description="Kimwog alias resolver")
    ap.add_argument("--root", default=kimwog.default_root(),
                    help="warehouse root (default: this warehouse)")
    ap.add_argument("tokens", nargs="+", help="domain slug or item ID")
    args = ap.parse_args(argv)

    domains = kimwog.load_registry(args.root)
    rc = 0
    for tok in args.tokens:
        domain, res, render = resolve_one(tok, domains)
        chain = " -> ".join(res.chain)
        canon = res.canonical if res.canonical else "(none)"
        print("%s : domain=%s canonical=%s status=%s render=%s [chain: %s]" % (
            tok, domain, canon, res.status, render, chain))
        if render == "missing":
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
