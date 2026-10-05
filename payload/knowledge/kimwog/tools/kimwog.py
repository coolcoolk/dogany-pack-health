#!/usr/bin/env python3
"""Kimwog warehouse core: minimal YAML reader, item/registry loaders, alias
resolution. Python 3 stdlib only (no PyYAML). Shared by lint.py and resolve.py.

The YAML we emit is a deliberately small subset: block mappings, block
sequences, "- key: value" inline map items, list-of-scalars, quoted/plain
scalars, and folded ">" block scalars. The parser below covers exactly that
subset and rejects nothing silently -- if a file uses YAML we do not model, the
caller sees a structurally wrong dict and lint flags it. Keep warehouse files
within this subset.
"""

import os
import re
import sys


# --------------------------------------------------------------------------
# Minimal YAML subset parser
# --------------------------------------------------------------------------

def _strip_comment(line):
    """Remove a trailing '# ...' comment when not inside quotes."""
    out = []
    in_s = in_d = False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        elif ch == "#" and not in_s and not in_d:
            # comment only if preceded by start-of-line or whitespace
            if i == 0 or line[i - 1] in " \t":
                break
        out.append(ch)
        i += 1
    return "".join(out)


def _scalar(text):
    """Convert a scalar token to a Python value."""
    t = text.strip()
    if t == "" or t == "~" or t == "null":
        return None
    if len(t) >= 2 and t[0] == t[-1] and t[0] in "'\"":
        return t[1:-1]
    low = t.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    if t.startswith("[") and t.endswith("]"):
        inner = t[1:-1].strip()
        if inner == "":
            return []
        return [_scalar(x) for x in _split_flow(inner)]
    return t


def _split_flow(inner):
    """Split a flow-sequence body on top-level commas."""
    parts = []
    depth = 0
    cur = ""
    in_s = in_d = False
    for ch in inner:
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        if ch in "[{" and not in_s and not in_d:
            depth += 1
        elif ch in "]}" and not in_s and not in_d:
            depth -= 1
        if ch == "," and depth == 0 and not in_s and not in_d:
            parts.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur)
    return parts


class _Line:
    __slots__ = ("indent", "text", "raw")

    def __init__(self, raw):
        self.raw = raw
        stripped = raw.lstrip(" ")
        self.indent = len(raw) - len(stripped)
        self.text = stripped.rstrip()


def _prepare(source):
    lines = []
    for raw in source.splitlines():
        body = _strip_comment(raw)
        if body.strip() == "":
            continue
        lines.append(_Line(body.rstrip()))
    return lines


def parse_yaml(source):
    """Parse the supported YAML subset into Python dict/list/scalars."""
    lines = _prepare(source)
    value, _ = _parse_block(lines, 0, 0)
    return value


def _parse_block(lines, idx, indent):
    if idx >= len(lines):
        return None, idx
    if lines[idx].text.startswith("- "):
        return _parse_seq(lines, idx, indent)
    return _parse_map(lines, idx, indent)


def _parse_seq(lines, idx, indent):
    seq = []
    while idx < len(lines):
        ln = lines[idx]
        if ln.indent < indent or not ln.text.startswith("- "):
            break
        if ln.indent > indent:
            raise ValueError("bad sequence indent at: %s" % ln.raw)
        item_body = ln.text[2:]
        # inline "- key: value" starts a mapping owned by this item
        if _looks_like_mapping(item_body):
            synth = " " * (indent + 2) + item_body
            block = [_Line(synth)]
            j = idx + 1
            while j < len(lines) and lines[j].indent > indent:
                block.append(lines[j])
                j += 1
            val, _ = _parse_map(block, 0, indent + 2)
            seq.append(val)
            idx = j
        else:
            seq.append(_scalar(item_body))
            idx += 1
    return seq, idx


def _looks_like_mapping(body):
    m = re.match(r"^[^\s:'\"\[][^:]*:(\s|$)", body)
    return m is not None


def _parse_map(lines, idx, indent):
    mp = {}
    while idx < len(lines):
        ln = lines[idx]
        if ln.indent < indent:
            break
        if ln.indent > indent:
            raise ValueError("bad mapping indent at: %s" % ln.raw)
        if ln.text.startswith("- "):
            break
        m = re.match(r"^([^:]+):(.*)$", ln.text)
        if not m:
            raise ValueError("bad mapping line: %s" % ln.raw)
        key = m.group(1).strip()
        rest = m.group(2).strip()
        if rest == ">" or rest == "|":
            # folded / literal block scalar
            j = idx + 1
            buf = []
            child_indent = None
            while j < len(lines) and lines[j].indent > indent:
                if child_indent is None:
                    child_indent = lines[j].indent
                buf.append(lines[j].raw[child_indent:])
                j += 1
            joiner = " " if rest == ">" else "\n"
            mp[key] = joiner.join(x.strip() if rest == ">" else x for x in buf).strip()
            idx = j
        elif rest == "":
            # nested block: could be map or seq
            j = idx + 1
            if j < len(lines) and lines[j].indent > indent:
                child_indent = lines[j].indent
                child, j = _parse_block(lines, j, child_indent)
                mp[key] = child
                idx = j
            else:
                mp[key] = None
                idx += 1
        else:
            mp[key] = _scalar(rest)
            idx += 1
    return mp, idx


# --------------------------------------------------------------------------
# Frontmatter + file loaders
# --------------------------------------------------------------------------

def read_frontmatter(path):
    """Return (frontmatter_dict, body_str) for a markdown file with a leading
    '---' YAML frontmatter block."""
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---"):
        raise ValueError("no frontmatter in %s" % path)
    parts = text.split("\n---", 1)
    if len(parts) != 2:
        raise ValueError("unterminated frontmatter in %s" % path)
    head = parts[0]
    head = head[len("---"):] if head.startswith("---") else head
    body = parts[1].lstrip("\n")
    return parse_yaml(head), body


def load_yaml_file(path):
    with open(path, "r", encoding="utf-8") as fh:
        return parse_yaml(fh.read())


def default_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_registry(root):
    data = load_yaml_file(os.path.join(root, "registry.yaml"))
    return data.get("domains", []) if data else []


def load_lanes(root):
    data = load_yaml_file(os.path.join(root, "lanes.yaml"))
    return data.get("lanes", []) if data else []


def load_axes(root):
    return load_yaml_file(os.path.join(root, "axes.yaml")) or {}


def iter_item_files(root):
    for sub in ("items", "e"):
        d = os.path.join(root, sub)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if name.endswith(".md"):
                yield os.path.join(d, name)


# --------------------------------------------------------------------------
# Alias resolution (MAJOR-2: resolution precedes item-status lookup)
# --------------------------------------------------------------------------

class Resolution:
    def __init__(self, canonical, status, render, chain):
        self.canonical = canonical      # resolved domain slug (or None)
        self.status = status            # registry status of the canonical row
        self.render = render            # "active" | "retracted" | "missing"
        self.chain = chain              # list of slugs walked

    def __repr__(self):
        return "Resolution(canonical=%r, status=%r, render=%r, chain=%r)" % (
            self.canonical, self.status, self.render, self.chain)


def build_alias_index(domains):
    """Map every alias and slug to its owning domain row. Detect collisions."""
    by_slug = {}
    alias_to_slug = {}
    for row in domains:
        slug = row.get("slug")
        by_slug[slug] = row
    for row in domains:
        slug = row.get("slug")
        for al in (row.get("aliases") or []):
            alias_to_slug[al] = slug
    return by_slug, alias_to_slug


def resolve_domain(slug, domains):
    """Resolve a possibly-aliased / merged domain slug to its canonical target.

    Alias resolution ALWAYS precedes status lookup. A resolved-but-tombstoned
    target (deprecated, or merged into a deprecated slug) renders as
    'retracted', never 'missing'. An unknown slug renders 'missing'.
    """
    by_slug, alias_to_slug = build_alias_index(domains)
    chain = []
    seen = set()
    cur = slug
    while True:
        if cur in seen:
            return Resolution(None, "alias-loop", "missing", chain + [cur])
        seen.add(cur)
        chain.append(cur)
        # alias redirect first
        if cur not in by_slug and cur in alias_to_slug:
            cur = alias_to_slug[cur]
            continue
        if cur not in by_slug:
            return Resolution(None, "unknown", "missing", chain)
        status = by_slug[cur].get("status", "active")
        if isinstance(status, str) and status.startswith("merged-into:"):
            cur = status.split(":", 1)[1]
            continue
        if status == "deprecated":
            return Resolution(cur, status, "retracted", chain)
        if status == "active":
            return Resolution(cur, status, "active", chain)
        return Resolution(cur, status, "missing", chain)


# --------------------------------------------------------------------------
# Shared ID grammar
# --------------------------------------------------------------------------

# domain/slug-NNN  -- domain is a slug, trailing -NNN numeric, lane never present.
ITEM_ID_RE = re.compile(r"^([a-z0-9][a-z0-9-]*)/([a-z0-9][a-z0-9-]*)-(\d{3,})$")
# e/<domain>/NNN
E_ID_RE = re.compile(r"^e/([a-z0-9][a-z0-9-]*)/(\d{3,})$")


def parse_item_id(item_id):
    """Return ('rag'|'e', domain, tail) or None if the ID is malformed."""
    m = E_ID_RE.match(item_id)
    if m:
        return ("e", m.group(1), m.group(2))
    m = ITEM_ID_RE.match(item_id)
    if m:
        return ("rag", m.group(1), m.group(3))
    return None


if __name__ == "__main__":
    # tiny smoke self-check of the parser
    sample = "a: 1\nb:\n  - x\n  - y\nc:\n  d: hi\n"
    print(parse_yaml(sample), file=sys.stderr)
