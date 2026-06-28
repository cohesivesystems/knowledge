# Agent Instructions

This repository is the conceptual source of truth for the public Cohesive system
model. Treat the Markdown graph as the canonical artifact.

## Working Rules

- Preserve Obsidian wikilinks such as `[[Process]]` and
  `[[Process|processes]]`.
- Keep graph notes under `Cohesive System Model.md` or
  `Cohesive System Model/`.
- Use frontmatter `realm` values that match the model realms in GRAPH.md.
- Use frontmatter `kind` values from the controlled vocabulary in GRAPH.md.
- Keep private implementation details, customer specifics, credentials,
  unreleased Ari modules, paid-feed block content, and private realization
  mappings out of this repository.
- Do not commit generated website output. Generated graph exports may be
  produced for downstream consumers but are projections, not source.
- Do not commit `.obsidian/` local settings or workspace state.
- Prefer small, conceptually coherent edits over broad rewrites.

## Before Finishing Changes

Run:

```sh
python3 scripts/validate_graph.py
python3 scripts/export_graph.py --out dist/graph.json
```

If validation fails, fix the graph issue rather than weakening the script unless
the graph contract itself is intentionally changing.
