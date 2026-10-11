#!/usr/bin/env python3
"""Lint a Kimwog warehouse against the frozen F2 contract (DGN-118) + v3 map
+ DGN-119 applicability schema. Python 3 stdlib only.

Validates:
  - ID grammar (domain/slug-NNN for RAG, e/<domain>/NNN for E-records; lane
    never in ID; domain field == ID prefix).
  - lane names against lanes.yaml (12 active lanes); multi-lane domains
    (exercise=3, cooking=2) REQUIRE lane:, single-lane domains MAY omit.
  - locale values (ISO-ish code or "universal").
  - axis names against the axes ledger (core / pack-namespaced / alias).
  - grade values (A..E letter ladder), contested boolean, sources present,
    applicability.axes role/unknown_policy enums.
  - registry consistency (no prefix reuse, alias targets exist, merge targets
    exist, no self-merge).
  - changelog well-formedness (known event classes, referenced IDs exist or are
    retracted, domain-transition events reference known slugs).
  - alias resolution sanity (every item's domain resolves; no alias loops).

Usage: lint.py [--root DIR]
Exit 0 = clean, 1 = errors found.
"""

import argparse
import os
import re
import sys

import kimwog

GRADES = set("ABCDE")
ROLES = {"hard", "soft", "scale"}
UNKNOWN_POLICIES = {"hedge", "ask", "block_specifics"}
AXIS_TYPES = {"numeric", "categorical", "boolean"}
LOCALE_RE = re.compile(r"^[A-Z]{2}(-[A-Z0-9]{1,3})?$")   # ISO-ish, e.g. KR, en-US
CHANGE_EVENTS = {"merge", "deprecate", "alias-add", "rename"}
AXIS_SOURCES = {"kit_life", "profile"}
# core axis names are bare slugs; pack axis names are namespace/name (one slash).
CORE_AXIS_RE = re.compile(r"^[a-z][a-z0-9_]*$")
PACK_AXIS_RE = re.compile(r"^[a-z][a-z0-9_-]*/[a-z][a-z0-9_]*$")


class Linter:
    def __init__(self, root):
        self.root = root
        self.errors = []
        self.warnings = []
        self.domains = kimwog.load_registry(root)
        self.lanes = kimwog.load_lanes(root)
        self.axes = kimwog.load_axes(root)
        self._index()

    def err(self, where, msg):
        self.errors.append("%s: %s" % (where, msg))

    def warn(self, where, msg):
        self.warnings.append("%s: %s" % (where, msg))

    def _index(self):
        # lane names per domain, and multiplicity
        self.lanes_by_domain = {}
        self.valid_lane_names = set()
        for ln in self.lanes:
            self.valid_lane_names.add(ln.get("name"))
            self.lanes_by_domain.setdefault(ln.get("domain"), []).append(ln.get("name"))
        # axis names
        self.axis_names = set()
        self.axis_aliases = {}
        for a in (self.axes.get("core") or []):
            self.axis_names.add(a.get("name"))
        for a in (self.axes.get("pack") or []):
            self.axis_names.add(a.get("name"))
        for k, v in (self.axes.get("aliases") or {}).items():
            self.axis_aliases[k] = v
        # registry slugs
        self.reg_slugs = {r.get("slug") for r in self.domains}

    # ---- registry ------------------------------------------------------
    def check_registry(self):
        seen = set()
        for row in self.domains:
            slug = row.get("slug")
            where = "registry[%s]" % slug
            if slug in seen:
                self.err(where, "duplicate/reused prefix '%s' (no-reuse rule)" % slug)
            seen.add(slug)
            status = row.get("status", "active")
            if isinstance(status, str) and status.startswith("merged-into:"):
                target = status.split(":", 1)[1]
                if target == slug:
                    self.err(where, "self-merge")
                elif target not in self.reg_slugs:
                    self.err(where, "merge target '%s' does not exist" % target)
            elif status not in ("active", "deprecated"):
                self.err(where, "bad status '%s'" % status)
            for al in (row.get("aliases") or []):
                if al in self.reg_slugs and al != slug:
                    # an alias that is itself a live slug is a modelling smell
                    row2 = next(r for r in self.domains if r.get("slug") == al)
                    st2 = row2.get("status", "active")
                    if not (isinstance(st2, str) and st2.startswith("merged-into:")):
                        self.warn(where, "alias '%s' shadows an active slug" % al)

    # ---- axes ledger discipline (DGN-172 M-3 tiering + name grammar) ---
    def check_axes_ledger(self):
        where = "axes.yaml"
        seen = set()

        def _check_axis(row, tier):
            name = row.get("name")
            if not name:
                self.err(where, "%s axis with no name" % tier)
                return
            if name in seen:
                self.err(where, "duplicate axis name '%s' (append-only, no reuse)"
                         % name)
            seen.add(name)
            # name grammar: core = bare slug, pack = namespace/name.
            if tier == "core" and not CORE_AXIS_RE.match(name):
                self.err(where, "core axis '%s' must be a bare slug (pack axes "
                         "use namespace/name)" % name)
            if tier == "pack" and not PACK_AXIS_RE.match(name):
                self.err(where, "pack axis '%s' must be namespace/name" % name)
            # required tiering fields (M-3: axes required full-spec on source,
            # type, volatility, safety; SAFETY axes additionally require
            # baseline_text).
            src = row.get("source")
            if src not in AXIS_SOURCES:
                self.err(where, "axis '%s' bad source '%s' (kit_life|profile)"
                         % (name, src))
            if row.get("type") not in AXIS_TYPES:
                self.err(where, "axis '%s' bad type '%s'" % (name, row.get("type")))
            vol = row.get("volatility")
            if vol != "stable":
                try:
                    int(vol)
                except (TypeError, ValueError):
                    self.err(where, "axis '%s' volatility must be 'stable' or an "
                             "integer max_age_days, got %r" % (name, vol))
            safety = row.get("safety")
            if not isinstance(safety, bool):
                self.err(where, "axis '%s' safety must be a boolean" % name)
            elif safety and not row.get("baseline_text"):
                # SAFETY axes are FULL-SPEC (M-3): baseline_text is mandatory so
                # the answer-first fallback has a data-sourced stated baseline.
                self.err(where, "SAFETY axis '%s' missing baseline_text "
                         "(safety axes are full-spec)" % name)

        for row in (self.axes.get("core") or []):
            _check_axis(row, "core")
        for row in (self.axes.get("pack") or []):
            _check_axis(row, "pack")
        # alias table: every alias target must be a known canonical name.
        for alias, target in (self.axes.get("aliases") or {}).items():
            if target not in seen:
                self.err(where, "alias '%s' -> unknown canonical axis '%s'"
                         % (alias, target))
            if alias in seen:
                self.err(where, "alias '%s' shadows a live axis name" % alias)

    # ---- items ---------------------------------------------------------
    def check_item(self, path):
        where = os.path.relpath(path, self.root)
        try:
            fm, _body = kimwog.read_frontmatter(path)
        except Exception as exc:  # noqa: BLE001
            self.err(where, "frontmatter parse failed: %s" % exc)
            return
        item_id = fm.get("id")
        if not item_id:
            self.err(where, "missing id")
            return
        parsed = kimwog.parse_item_id(item_id)
        if not parsed:
            self.err(where, "malformed id '%s'" % item_id)
            return
        kind, domain, _tail = parsed
        # lane must never appear in the ID
        if "@" in item_id:
            self.err(where, "lane token in ID '%s' (lane never in ID)" % item_id)
        # domain field must equal ID prefix
        if fm.get("domain") != domain:
            self.err(where, "domain field '%s' != ID prefix '%s'" % (fm.get("domain"), domain))
        # domain must resolve
        res = kimwog.resolve_domain(domain, self.domains)
        if res.render == "missing":
            self.err(where, "domain '%s' not in registry (%s)" % (domain, res.status))
        if kind == "e":
            self.check_e_item(where, fm, domain)
        else:
            self.check_rag_item(where, fm, domain)

    def check_rag_item(self, where, fm, domain):
        grade = fm.get("grade")
        # grade may be "A" or "A (rule)" etc. -- first token must be a letter grade
        gletter = str(grade).strip()[:1] if grade else ""
        if gletter not in GRADES:
            self.err(where, "bad grade '%s' (must start A..E)" % grade)
        # locale
        loc = fm.get("locale")
        if loc is None:
            self.err(where, "missing locale")
        elif loc != "universal" and not LOCALE_RE.match(str(loc)):
            self.err(where, "bad locale '%s' (ISO code or 'universal')" % loc)
        # as-of present
        if not fm.get("as_of"):
            self.err(where, "missing as_of")
        # contested boolean
        if not isinstance(fm.get("contested"), bool):
            self.err(where, "contested must be a boolean")
        # sources present + non-empty
        sources = fm.get("sources")
        if not sources or not isinstance(sources, list):
            self.err(where, "sources must be a non-empty list")
        # lane requirement
        self.check_lane(where, fm, domain)
        # applicability axes
        self.check_axes(where, fm)

    def check_e_item(self, where, fm, domain):
        status = fm.get("status")
        if status not in ("active", "revised", "retracted"):
            self.err(where, "E-record status '%s' invalid (active|revised|retracted)" % status)
        if not fm.get("date"):
            self.err(where, "E-record missing date")
        if not fm.get("claim"):
            self.err(where, "E-record missing claim")
        links = fm.get("evidence_links")
        if not links or not isinstance(links, list):
            self.err(where, "E-record evidence_links must be a non-empty list")
        # E-records must NOT carry a grade ladder (F2: E has no letter grade)
        if fm.get("grade") is not None:
            self.err(where, "E-record must not carry a letter grade")

    def check_lane(self, where, fm, domain):
        lane = fm.get("lane")
        lane_names = self.lanes_by_domain.get(domain, [])
        multi = len(lane_names) > 1
        if lane is None:
            if multi:
                self.err(where, "lane: required on multi-lane domain '%s' (%d lanes)"
                         % (domain, len(lane_names)))
            return
        if lane not in self.valid_lane_names:
            self.err(where, "unknown lane '%s' (not in lanes.yaml)" % lane)
        elif lane not in lane_names:
            self.err(where, "lane '%s' not valid for domain '%s'" % (lane, domain))

    def check_axes(self, where, fm):
        app = fm.get("applicability")
        if not app:
            return  # applicability is optional (M-3 tiering: axes required only when personalizing)
        axes = app.get("axes") if isinstance(app, dict) else None
        if axes is None:
            return
        if not isinstance(axes, list):
            self.err(where, "applicability.axes must be a list")
            return
        for ax in axes:
            key = ax.get("key")
            if key not in self.axis_names:
                if key in self.axis_aliases:
                    self.warn(where, "axis '%s' is an alias -> '%s' (prefer canonical)"
                              % (key, self.axis_aliases[key]))
                else:
                    self.err(where, "off-ledger axis '%s'" % key)
            if ax.get("type") not in AXIS_TYPES:
                self.err(where, "axis '%s' bad type '%s'" % (key, ax.get("type")))
            if ax.get("role") not in ROLES:
                self.err(where, "axis '%s' bad role '%s'" % (key, ax.get("role")))
            if ax.get("unknown_policy") not in UNKNOWN_POLICIES:
                self.err(where, "axis '%s' bad unknown_policy '%s'"
                         % (key, ax.get("unknown_policy")))

    # ---- changelog -----------------------------------------------------
    def check_changelog(self, item_ids):
        path = os.path.join(self.root, "CHANGELOG.yaml")
        if not os.path.exists(path):
            self.warn("CHANGELOG.yaml", "absent")
            return
        try:
            data = kimwog.load_yaml_file(path)
        except Exception as exc:  # noqa: BLE001
            self.err("CHANGELOG.yaml", "parse failed: %s" % exc)
            return
        releases = (data or {}).get("releases")
        if not isinstance(releases, list):
            self.err("CHANGELOG.yaml", "releases must be a list")
            return
        for rel in releases:
            ver = rel.get("version", "?")
            where = "CHANGELOG[%s]" % ver
            if not rel.get("version") or not rel.get("date"):
                self.err(where, "release needs version + date")
            for cls in ("added", "changed"):
                for iid in (rel.get(cls) or []):
                    if iid not in item_ids:
                        self.err(where, "%s ID '%s' has no item file" % (cls, iid))
            # retracted IDs may legitimately have no file (item pulled)
            for gt in (rel.get("grade_transitions") or []):
                if not gt.get("id") or gt.get("from") is None or gt.get("to") is None:
                    self.err(where, "grade_transition needs id/from/to")
            for dt in (rel.get("domain_transitions") or []):
                ev = dt.get("event")
                if ev not in CHANGE_EVENTS:
                    self.err(where, "unknown domain_transition event '%s'" % ev)
                    continue
                for fld in ("from", "into", "domain", "alias", "to"):
                    val = dt.get(fld)
                    if fld in ("from", "into", "domain") and val and val not in self.reg_slugs:
                        self.err(where, "domain_transition %s '%s' not in registry" % (fld, val))
            for lt in (rel.get("lane_transitions") or []):
                if not lt.get("id") or not lt.get("to"):
                    self.err(where, "lane_transition needs id + to")

    # ---- M-2 protocol: grades speak ONLY via the skill path ------------
    # Grades/personalized numbers must be spoken only through the answer-path
    # skill (F3 extension). The frontmatter `grade:` field is the machine record
    # the skill reads; a letter grade baked into the human PROSE body would leak
    # a grade outside the skill path (the "parametric bypass" M-2 warns about).
    # We flag a bare letter-grade token in the body as an error.
    # Matches 'grade A', 'A-grade', and the Korean 'A<geup>' form (U+AE09,
    # escaped to keep this source ASCII-only per the code style rule).
    GRADE_LEAK_RE = re.compile(
        "\\b(grade\\s+[A-E]\\b|[A-E]-grade\\b)|[A-E]\uae09")

    def check_m2_grade_leak(self, path, body):
        where = os.path.relpath(path, self.root)
        for m in self.GRADE_LEAK_RE.finditer(body or ""):
            self.err(where, "M-2: letter grade '%s' in prose body (grades speak "
                     "ONLY via the skill path -- keep grades in frontmatter)"
                     % m.group(0).strip())

    # ---- driver --------------------------------------------------------
    def run(self):
        self.check_registry()
        self.check_axes_ledger()
        item_ids = set()
        item_files = list(kimwog.iter_item_files(self.root))
        for path in item_files:
            self.check_item(path)
            try:
                fm, body = kimwog.read_frontmatter(path)
                if fm.get("id"):
                    item_ids.add(fm["id"])
                # M-2 applies to RAG items (E-records carry no grade at all).
                if kimwog.parse_item_id(fm.get("id") or "") \
                        and kimwog.parse_item_id(fm["id"])[0] == "rag":
                    self.check_m2_grade_leak(path, body)
            except Exception:  # noqa: BLE001
                pass
        self.check_changelog(item_ids)
        return self.errors, self.warnings


def main(argv):
    ap = argparse.ArgumentParser(description="Kimwog warehouse lint")
    ap.add_argument("--root", default=kimwog.default_root(),
                    help="warehouse root (default: this warehouse)")
    args = ap.parse_args(argv)
    linter = Linter(args.root)
    errors, warnings = linter.run()
    for w in warnings:
        print("WARN  " + w)
    for e in errors:
        print("ERROR " + e)
    n = len(errors)
    print("\n%d error(s), %d warning(s) in %s" % (n, len(warnings), args.root))
    return 1 if n else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
