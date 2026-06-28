# Contributing

Contributions are welcome when they improve the clarity, consistency, or
navigability of the public Cohesive system model.

## Scope

Good contributions include:

- Concept corrections or clarifications.
- Missing links between existing concepts.
- New public concepts that fit the graph contract.
- Improvements to validation, export, or schema tooling.
- Editorial fixes that preserve meaning.

Out of scope:

- Private code mappings or implementation details.
- Customer, partner, or commercial engagement details.
- Credentials, secrets, internal URLs, or paid-feed content.
- Claims that a private module or commercial offering is available unless it is
  already intentionally public.

## Graph Style

- One primary concept per note.
- The first heading should match the concept title.
- Use Obsidian wikilinks for concept references.
- Prefer explicit related-concept lists when a note introduces several important
  adjacent concepts.
- Keep realization claims separate from conceptual definitions. Public
  realization mappings should be intentional and reviewable.

Recommended note frontmatter:

```yaml
---
realm: Semantic Dynamics
status: draft
kind: concept
aliases: []
---
```

Only `realm` is currently required for notes inside a realm folder.

## Review Checklist

Before opening a pull request, run:

```sh
python3 scripts/validate_graph.py
python3 scripts/export_graph.py --out dist/graph.json
```

Pull requests should explain the conceptual change, not only the text change.

## Licensing

By contributing, you agree that your contribution is licensed under this
repository's licenses:

- Content contributions: CC BY 4.0.
- Code, scripts, schemas, and configuration contributions: Apache-2.0.
