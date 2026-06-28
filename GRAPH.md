# Graph Contract

The Cohesive knowledge graph is the public conceptual source of truth for the
Cohesive system model. Markdown notes are the authored source. Generated JSON,
web pages, search indexes, and other derived artifacts are projections.

## Source Layers

- Conceptual graph: public concepts, definitions, distinctions, and relations.
- System graph: authored system structure and correspondence across concepts.
- Realization graph: mappings from system graph nodes to code, runtime,
  infrastructure, or content artifacts.

This repository contains the public conceptual graph. Private system graph or
realization graph data should live elsewhere unless explicitly published.

## Realms

Allowed public realms:

- `Principles`
- `Semantic Dynamics`
- `Operational Semantics`
- `System Structure`
- `Realization Substrate`
- `Architecture Practices`

The top-level `Cohesive System Model.md` file acts as the overview.

## Nodes

A graph node is a Markdown note that defines or organizes a concept.

Required for notes inside `Cohesive System Model/`:

- A frontmatter `realm` matching one of the allowed realms.
- A first-level heading naming the concept.

Recommended:

- `kind`: `concept`, `overview`, `practice`, `principle`, or `index`.
- `status`: `draft`, `stable`, or `deprecated`.
- `aliases`: alternate titles or search names.

## Relations

The primary authored relation format is an Obsidian wikilink:

```md
[[Process]]
[[Process|processes]]
```

Tooling exports wikilinks as typed edges with relation type `mentions`. Future
typed relations may include:

- `defines`
- `refines`
- `depends_on`
- `constrains`
- `observes`
- `realizes`
- `documents`

Use typed relations only when the relation is intentional and reviewable. A
plain wikilink is acceptable for ordinary conceptual adjacency.

## Public Boundary

Do not include:

- Private implementation mappings from code.
- Customer-specific details.
- Secrets or credentials.
- Paid-feed block content.
- Closed-source Ari module details.
- Commercial terms or support commitments not already public.

## Downstream Use

`cohesive-website` may consume selected graph notes or generated graph exports
to render public library content. That website is an editorial projection. This
repository remains the canonical graph source.
