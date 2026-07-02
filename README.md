# Cohesive Knowledge

This repository is the public conceptual source for the Cohesive system model.
The canonical authored form is Markdown intended for graph navigation in
Obsidian.

The graph describes concepts such as domain semantics, operational concerns,
system graph, realization substrate, architecture practices, and the
relations among them. Curated publication belongs in the broader Cohesive
website; this repository remains the source graph that those editorial surfaces
can consume.

## Repository Shape

- `Cohesive System Model.md` is the top-level model overview.
- `Cohesive System Model/` contains graph notes organized by realm.
- `GRAPH.md` defines the graph contract used by contributors and tooling.
- `schema/` contains machine-readable schema definitions for generated exports.
- `scripts/` contains validation and export tooling.

## Using the Graph

Open this repository as an Obsidian vault to navigate the graph with wikilinks
and backlinks. Local Obsidian settings under `.obsidian/` are intentionally not
tracked. The Markdown files are the source of truth.

To validate the graph:

```sh
python3 scripts/validate_graph.py
```

To export a structured graph projection:

```sh
python3 scripts/export_graph.py --out dist/graph.json
```

Generated exports are projections. They are not the canonical authored source.

## Public Boundary

This repository is for public conceptual material. Do not add private product
plans, unreleased implementation details, credentials, customer details,
commercial terms, paid-feed content, or private realization mappings from code.

Private implementation mappings and code reconciliation belong in private
system graph or realization graph repositories unless they are intentionally
published.

## License

Markdown content is licensed under CC BY 4.0. Code, scripts, and schemas are
licensed under Apache-2.0. See LICENSE, LICENSE-CONTENT, and LICENSE-CODE.
