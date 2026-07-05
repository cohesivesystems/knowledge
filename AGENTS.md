# Agent Instructions

This repository is the conceptual source of truth for the public Cohesive system
model. Treat the Markdown graph as the canonical artifact.

## Modeling Vision

Cohesive has two linked goals:

- Establish a standard language for describing systems.
- Build compiler-like realizations that lower that language into working
  infrastructure while preserving meaning.

When adding or revising concepts, preserve the distinction between semantic
language, system graph structure, operational concern, and realization
substrate. Do not collapse a graph concept into one implementation mechanism
unless the note is explicitly about that mechanism.

For Cohesive building blocks, make the conceptual trace explicit: link to the
graph concepts that define the block's meaning, state the boundary of its
guarantees, and identify realization choices only at the public level suitable
for this repository.

For process-related language, consult [[Process Theories|process theories]] and
preserve distinctions among semantic processes, process structures, process
managers, sagas, durable execution, workflows, orchestration, choreography, and
runtime or physical processes.

## Working Rules

- Preserve Obsidian wikilinks such as `[[Process]]` and
  `[[Process|processes]]`.
- Keep graph notes under `Cohesive System Model.md` or
  `Cohesive System Model/`.
- Use frontmatter `realm` values that match the model realms in GRAPH.md.
- Use frontmatter `kind` values from the controlled vocabulary in GRAPH.md.
- When graph entries are referenced or mentioned, do not capitalize them unless
  they are the first word in a sentence.
- Use lowercase for connectives and prepositions in titles, such as `and`,
  `of`, `for`, `in`, and `by`.
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
