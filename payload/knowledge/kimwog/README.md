# Kimwog Warehouse #1 -- knowledge storage vessel

This directory is a knowledge warehouse: the working storage that implements the
frozen F2 knowledge-schema contract. It is the dev sandbox for warehouse #1 and
is built to move, unchanged, into a future `pak-*` pack directory. No absolute
paths are baked into any data file; every tool takes a `--root` flag defaulting
to this warehouse root.

A warehouse holds curated, graded knowledge items for one or more domains, the
user's own experience records (E-records), the domain registry, the axes
ledger, a lane reference, and a per-release changelog. The lint tool enforces
the schema so a solo curator cannot drift.

## Layout

```
kimwog/
  README.md            this file
  registry.yaml        per-warehouse domain registry (slug/status/aliases)
  lanes.yaml           the 12 active lanes (verification cultures) reference
  axes.yaml            axes ledger: core + pack-namespaced + aliases
  CHANGELOG.yaml       per-release changelog (added/changed/retracted/transitions)
  items/               A..D knowledge items (curated, graded)
    <domain>-<slug>-NNN.md
  e/                   E-records (user-local digested conclusions)
    <domain>-NNN.md
  tools/
    kimwog.py          core: YAML-subset reader, loaders, alias resolver
    lint.py            schema validator (run me before shipping)
    resolve.py         alias-resolution CLI
```

Tools are Python 3, standard library only (`/usr/bin/python3`). They read a
small YAML subset (no PyYAML dependency); keep data files within that subset
(block maps/sequences, `- key: value` list items, `[a, b]` flow sequences, and
`>` folded block scalars for multi-line prose -- do NOT use multi-line quoted
strings).

## Item format (F2 contract)

Each `items/*.md` file is markdown with a leading `---` YAML frontmatter block.
The frontmatter is the machine record; the prose below it is the curator's
human-readable layer.

Required and optional fields:

- `id` -- stable ID, grammar `domain/slug-NNN`. Domain-scoped, numeric tail.
  The lane NEVER appears in the ID. The ID is unique WITHIN this warehouse only.
- `domain` -- the cross-domain field (M5). MUST equal the ID prefix.
- `grade` -- letter grade on the confidence ladder A..E (A converged consensus,
  B RCT-level pre-consensus, C observational, D practitioner consensus, E
  experience-adjusted). A trailing qualifier is allowed (`A (rule)`); the first
  character must be a valid grade. Grade is CONFIDENCE; evidence type is a
  separate concern. `contested` is orthogonal to the letter.
- `lane` -- non-ID field, written with the leading `@` (e.g. `@clinical-physio`).
  REQUIRED on multi-lane domains (exercise = 3 lanes, cooking = 2). MAY be
  omitted on single-lane domains (defaults to the domain's only lane). Selects
  the speech-strength + red-flag profile at answer time.
- `locale` -- non-ID field. An ISO-ish code (`KR`, `en-US`) or `universal`.
  Never an ID segment (avoids prefix-fork explosion for jurisdiction-bound
  knowledge).
- `as_of` -- the as-of date or range of the underlying evidence.
- `contested` -- boolean, orthogonal to the letter grade.
- `sources` -- non-empty list. A within-warehouse cross-reference may omit the
  `source:` prefix; a cross-WAREHOUSE reference MUST be fully qualified as
  `source:domain/slug`.
- `applicability.axes` -- optional list (M-3 tiering: axes are required only
  when the item personalizes). Each axis: `key` (must be on the axes ledger),
  `type` (numeric|categorical|boolean), `role` (hard gate | soft modifier |
  scale math-input), `unknown_policy` (hedge | ask | block_specifics). A safety
  axis with `role: hard` and `unknown_policy: block_specifics` withholds
  specific numbers when the axis is unknown or refused (it does not go silent).
- `refraction_notes` -- optional list of curated direction adjustments; each
  note carries its OWN grade. With no note, the answer path hedges but does not
  change the number.
- `claim`, `reasoning` -- prose payload.

## E-record format (F2 amendment 1)

Each `e/*.md` file is a user-local "digested conclusion" -- the user's own
resolved position, tracked alongside A..D knowledge but graded by lived
experience, not by a letter ladder.

- `id` -- `e/<domain>/NNN`. The `e/` namespace blocks any collision with RAG
  IDs by construction; the same domain-scoped grammar applies under it.
- `domain` -- must be a registered domain (alias-resolved).
- `status` -- `active | revised | retracted`.
- `date` -- when the conclusion was recorded or last updated.
- `evidence_links` -- non-empty list; each link is a memory ref and/or a
  RAG-ID the conclusion engages.
- `claim` -- the conclusion prose.
- NO letter grade and NO changelog on E-records (the validator is the user's
  own life). Lint rejects an E-record that carries a `grade`.

## Domain registry (F2 / v3 section 4)

`registry.yaml` holds ONE entry per domain in this warehouse (the registry is
per-warehouse, not global). Each entry: `slug`, `status`, `aliases`.

Curator rules (lint-enforced):

- A shipped prefix is NEVER reused and NEVER hard-deleted.
- Merge = set `status: merged-into:<slug>` on the old domain AND add the old
  slug to the target's `aliases`. Alias resolution redirects reads forward.
- Deprecate = `status: deprecated` (a frozen tombstone). Not reused.
- Every merge/alias target must exist; no self-merge.

## Alias resolution (v3 section 5.3 / F2 MAJOR-2)

Alias resolution ALWAYS runs BEFORE item-status lookup. A resolved-but-
tombstoned target (deprecated, or merged into a deprecated slug) renders as
`retracted`, never `missing`. An unknown slug renders `missing`. Run:

```
python3 tools/resolve.py exercise skill-learning daily-life-ops
```

## Changelog (F2)

`CHANGELOG.yaml`, newest release first. Per release: `added`, `changed`,
`retracted` (stable-ID lists), `grade_transitions` ({id, from, to}),
`domain_transitions` ({event: merge|deprecate|alias-add|rename, ...}), and
`lane_transitions` ({id, from, to, note} -- lane-field rewrites, which are a
rubric-structure change, NOT an ID event). The touched-set consumer diffs these
ID lists against the user's local cache and re-queries only overlapping IDs.

## Lint

Run before shipping any change:

```
python3 tools/lint.py            # this warehouse
python3 tools/lint.py --root DIR # any warehouse
```

Exit 0 = clean. It validates ID grammar, lane names, locale values, axis names,
grade/contested/sources, applicability enums, registry consistency, and
changelog well-formedness. Warnings (non-fatal) flag off-canonical axis aliases.

## Portability note

Everything here is relative to the warehouse root. To promote this warehouse
into a pack, move the directory under the pack's namespace and register it; the
tools and data need no path edits. Items marked `SAMPLE` in their frontmatter
are schema fixtures, not shippable knowledge -- replace them with curated
content before release.
