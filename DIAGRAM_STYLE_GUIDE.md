# Cohesive Diagram Style Guide

This guide defines the visual and semantic conventions for authored diagrams in
the public Cohesive knowledge graph. The reference example is the
[cross-realm projection](assets/diagrams/cross-realm-projection.svg).

Diagrams are explanatory projections of the Markdown graph. They are not a
second source of conceptual truth. Every important claim in a diagram must be
supported by the surrounding note or linked graph concepts.

## Visual Character

Aim for a restrained, publication-quality, TikZ-inspired aesthetic:

- Crisp vector geometry rather than presentation-slide ornament.
- Thin strokes, quiet fills, generous spacing, and modest corner radii.
- A subtle construction grid or paper-like field when it improves orientation.
- A system sans-serif for headings, blocks, and annotations.
- A mathematical serif only for judgments, variables, and formal notation.
- Color used to identify realms, paired with shape, labels, and line styles.
- No gradients, heavy shadows, glossy effects, or decorative icon collections.

## Semantic Discipline

Preserve the distinction among
[[Cohesive System Model#1. Domain Semantics|domain semantics]], the
[[Cohesive System Model#3. System Graph|system graph]],
[[Cohesive System Model#2. Operational Concerns|operational concerns]], and the
[[Cohesive System Model#4. Realization Substrate|realization substrate]]. Do not
use visual adjacency to imply that concepts from different realms are
identical.

Cross-realm arrows are typed correspondences. Label them with the relation they
assert, such as `allocated to`, `arranged as`, `requires`, `realizes`,
`preserves`, `approximates`, or `forgets`. A dashed projection arrow does not
mean inheritance or containment.

When a diagram includes services and interactions:

- Draw a logical [[Service|service]] as a boundary containing its allocated
  responsibilities.
- Draw a required or provided [[Interfaces|interface]] as an explicit block at
  the service boundary, not as unattached text.
- Draw an [[Interaction Channels|interaction channel]] separately from the
  interface and from the semantic [[Interaction|interaction]] it carries.
- Allow a semantic [[Process|process]] to span services when that is the model;
  do not imply that every process belongs to one runtime or workflow engine.
- Present operational concerns as qualifications on nodes, edges, and mappings,
  rather than as another semantic participant.

Keep private implementation mappings, customer-specific topology, credentials,
and unreleased realization details out of public diagrams.

## Shape Vocabulary

| Meaning | Preferred mark |
| --- | --- |
| entity or enduring semantic subject | oval |
| semantic process or decision structure | restrained hexagon |
| semantic or system-graph node | rounded rectangle |
| service or deployment boundary | unfilled rounded container |
| required or provided interface | compact, emphasized boundary block |
| interaction channel, broker, or transport locus | capsule with sparse internal rules |
| state or storage | cylinder |
| semantic interaction | solid, realm-colored directed edge |
| structural channel flow | solid, system-graph-colored directed edge |
| cross-realm projection or realization | neutral dashed directed edge |
| relation without control or movement meaning | neutral dotted edge |
| cross-cutting operational requirements | neutral dashed band |
| formal realization judgment | quiet mathematical label plate |

Use a new shape only when it encodes a distinction that the legend, labels, and
surrounding text can explain.

## Realm Composition

For cross-realm diagrams, prefer horizontal bands in this order:

1. Domain semantics: meaning-bearing entities, processes, relations, and
   interactions.
2. System graph: service boundaries, models, interfaces, channels, and flows.
3. Operational concerns: a narrow cross-cutting qualification band, when
   relevant.
4. Realization substrate: modules, deployments, runtimes, storage, network, and
   other concrete mechanism families.

Align corresponding nodes across bands when that keeps mappings legible. Break
alignment deliberately when it would incorrectly suggest a one-to-one mapping.

## Typography and Labels

- Use a system sans-serif for every block title. Do not use Times New Roman for
  block titles.
- Reserve mathematical serif type for notation such as
  `G; P @ B ⊢ ρ : G → R`.
- Use weight, not large size changes, to distinguish titles from details.
- Keep graph-entry names lowercase unless they begin a sentence.
- Prefer one short title and at most two short detail lines inside a node.
- Wrap or shorten text before reducing its size. At the intended display size,
  essential labels should not render below 11 px.
- Keep clear internal padding on every side of an oval, hexagon, capsule, or
  rectangle. Text must not touch the outline.
- Use concise noun phrases inside nodes and put explanation in the surrounding
  Markdown.

## Edges and Collision Avoidance

Edges must remain subordinate to meaning and labels:

- Route arrows around realm headings, block titles, detail text, and edge
  labels.
- Terminate projection arrows at node or boundary edges, not inside labeled
  blocks.
- Give an edge label a quiet opaque plate when the edge must pass behind it.
- Place `required interface` and `provided interface` inside their interface
  blocks.
- Use orthogonal bends for allocation and realization mappings when direct
  diagonals create ambiguity.
- Keep return flows visually distinct and provide enough curvature that their
  direction is obvious.
- Split a cross-cutting mapping around an operational-concern band instead of
  drawing through its text.
- Never let an arrowhead cover a character or block title.

## Color and Theme

Use the following stable category mapping:

- Domain semantics: blue.
- System graph: amber or orange.
- Realization substrate: green.
- Operational concerns and cross-realm projections: neutral gray.

Use low-chroma field fills and stronger strokes. Preserve sufficient contrast
in both light and dark themes. Color must not be the only carrier of meaning:
retain labels, shape differences, and line-style differences.

For standalone SVGs, define light colors as the default and provide a
`prefers-color-scheme: dark` override. Avoid external fonts and runtime
dependencies.

## Asset and Embedding Rules

- Store published diagrams under `assets/diagrams/` with lowercase,
  hyphen-separated names.
- Prefer SVG for conceptual diagrams. Keep text as text when practical.
- If a diagram has editable TikZ or other source, place it under
  `assets/diagrams/source/` with the same basename.
- Do not commit generated website output.
- Give every SVG a concise `<title>` and meaningful `<desc>`.
- Use descriptive Markdown alt text; do not repeat the entire surrounding
  paragraph.
- Keep a diagram close to the section whose claims it illustrates. Link to that
  canonical section from related notes rather than duplicating the image.
- When a dense landscape diagram becomes illegible on a narrow viewport,
  provide a compact companion or a documented zoomable presentation.

Example embedding from a note two directories below the repository root:

```md
![Cross-realm projection from domain semantics through the system graph to the realization substrate](../../assets/diagrams/cross-realm-projection.svg)
```

## Agent Workflow

Before drawing:

1. Read the defining graph notes and identify the realm of every depicted
   concept.
2. Write down the meaning of every node, edge, boundary, and cross-realm
   mapping.
3. Decide which information the diagram preserves and which it intentionally
   omits.

Before finishing:

1. Check that no implementation mechanism has replaced a semantic concept.
2. Check every label for graph vocabulary, capitalization, and boundary scope.
3. Inspect text fit in every shape.
4. Inspect all arrow routes for collisions with labels and headings.
5. Render the SVG in light and dark themes at its expected publication width.
6. Check a narrow viewport or provide a compact alternative.
7. Confirm that the surrounding Markdown states the diagram's substantive
   claims.
8. Run the repository graph validation and export commands.
