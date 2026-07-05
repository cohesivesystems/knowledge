# Cohesive Knowledge

This repository is the public conceptual source for the Cohesive system model.
The canonical authored form is Markdown intended for graph navigation in
Obsidian.

The graph describes concepts such as domain semantics, operational concerns,
system graph, realization substrate, architecture practices, and the
relations among them. Curated publication belongs in the broader Cohesive
website; this repository remains the source graph that those editorial surfaces
can consume.

## Vision

Cohesive has two linked goals:

- Establish a standard language for describing systems.
- Build compiler-like realizations that lower that language into working
  infrastructure while preserving meaning.

The graph is therefore more than documentation. It is the public conceptual
contract for Cohesive building blocks. Concepts should be precise enough to
guide realization into actors, storage systems, brokers, workflows, protocols,
runtimes, and other infrastructure without collapsing semantic roles into the
mechanisms that host them.

Category theory is an important source of modeling discipline for this work:
compositionality, functoriality, naturality, duality, universal constructions,
local-to-global consistency, and feedback all help expose hidden assumptions.
The practical test is whether the language can be realized in systems that
run.

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
