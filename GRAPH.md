# Graph Contract

The Cohesive knowledge graph is the public conceptual source of truth for the
Cohesive system model. Markdown notes are the authored source. Generated JSON,
web pages, search indexes, and other derived artifacts are projections.

## Source Layers

- Conceptual graph: public concepts, definitions, distinctions, and relations.
- System graph: authored composition of semantic constructs into modeled systems,
  including public graph projections such as entity models, relation models,
  process graphs, and infrastructure graphs.
- Realization graph: mappings from system graph nodes to code, runtime,
  infrastructure, or content artifacts.

This repository contains the public conceptual graph. Private system graph or
realization graph data should live elsewhere unless explicitly published.

## Realms

Allowed public realms:

- `Principles`
- `Domain Semantics`
- `Operational Concerns`
- `System Graph`
- `Realization Substrate`
- `Architecture Practices`

The top-level `Cohesive System Model.md` file acts as the overview.

## Nodes

A graph node is a Markdown note that defines or organizes a concept.

Required for graph nodes:

- A frontmatter `realm` matching one of the allowed realms, except for the
  top-level overview.
- A frontmatter `kind` matching one of the allowed kinds.
- A frontmatter `created` date in `YYYY-MM-DD` format.
- A frontmatter `updated` date in `YYYY-MM-DD` format.
- A first-level heading naming the concept.

Allowed kinds:

- `discipline`: source discipline or body of theory, such as category theory.
- `principle`: modeling discipline used to keep distinctions precise.
- `semantic-construct`: meaning-bearing construct in domain semantics.
- `structural-construct`: system-graph arrangement or composition construct.
- `operational-concern`: correctness, execution behavior, reliability, or control concern.
- `realization-substrate`: concrete mechanism family or substrate category.
- `architecture-practice`: named architecture practice or methodology.
- `pattern`: reusable narrower technique that can appear inside practices or substrates.
- `example`: concrete domain, system, or scenario example.
- `reference`: organizing note, index-like reference, or explanatory guide.
- `glossary`: term list or vocabulary note.
- `overview`: reserved for the top-level `Cohesive System Model.md` overview.

Use `kind` by the primary role of the note, not by the concepts it references.
A `semantic-construct` is a meaning-bearing modeling primitive in domain
semantics. A `principle` is a modeling discipline, distinction, or relationship
that constrains how primitives are interpreted. If a note primarily relates,
compares, or disciplines constructs such as `Event` and `State`, classify it as
`principle` even when it is heavily referenced from domain semantics.

Recommended:

- `status`: `draft`, `stable`, or `deprecated`.
- `aliases`: alternate titles or search names.

Date metadata is authored graph metadata, not filesystem metadata:

- `created` is the date the note was first authored as a public graph node.
- `updated` is the date of the last substantive conceptual edit.

Use ISO calendar dates. `updated` must be equal to or later than `created`.
Mechanical metadata changes, export regeneration, or website projection changes
should not by themselves advance `updated`.

## Relations

The primary authored relation format is an Obsidian wikilink:

```md
[[Process]]
[[Process|processes]]
```

Tooling exports ordinary wikilinks as edges with relation type `mentions`. Use
a formal relation when the source note makes a stable, intentional, and
reviewable assertion about another graph node.

### Authored Format

Formal relations appear in an exact `## Formal relations` section:

```md
## Formal relations

- `bundles`: [[Service]] — Aligns semantic responsibility with ownership, deployment, and runtime boundaries.
```

Each entry must be written on one physical line using the form
``- `type`: [[Target]] — rationale``. The rationale states why the relation
holds and, for a cross-realm correspondence, should identify the relevant
boundary, preserved structure, qualification, or limitation. Use a fuller
correspondence profile in the note when that explanation does not fit in one
line.

The source note owns the assertion. Do not author the inverse relation in the
target merely to obtain a backlink; tooling derives inverse labels for
navigation. Whether an edge crosses realms is derived from the source and
target node metadata. The `realm_peer_of` type does not replace that derived
property: it makes the narrower assertion that two entries are realm-specific
treatments of the same nominal notion.

The target wikilink in a formal relation is exported under the asserted type
instead of `mentions`. Other wikilinks in the note, including links used in the
rationale, remain ordinary `mentions` edges.

### Controlled Vocabulary

Relation names are directed predicates from the source note to the target note:

| Relation | Derived inverse | Meaning |
| --- | --- | --- |
| `mentions` | `mentioned_by` | Untyped conceptual adjacency expressed by an ordinary wikilink. Do not author this type in a formal-relations section. |
| `refines` | `refined_by` | Gives a narrower or more precise account without asserting identity. |
| `arranges` | `arranged_by` | A system-graph construct places, connects, scopes, or composes the target role in a modeled system. |
| `qualifies` | `qualified_by` | An operational concern states scoped properties, guarantees, or execution behavior for the target. |
| `constrains` | `constrained_by` | Restricts the valid forms, choices, or realizations of the target. |
| `requires` | `required_by` | The source cannot satisfy its stated claims without the target concern or capability. |
| `bundles` | `bundled_by` | An architecture practice deliberately adopts the target as part of a named cross-realm choice. |
| `documents` | `documented_by` | A reference, catalog, glossary, or overview explains or organizes the target. |
| `may_realize` | `may_be_realized_by` | A public substrate family is a candidate mechanism for the target when its requirements are met. |
| `realizes` | `realized_by` | A selected concrete artifact or mechanism actually realizes the target at a declared boundary. |
| `realm_peer_of` | `realm_peer_of` | Relates distinct entries in different realms that deliberately treat the same nominal notion from realm-specific perspectives. |
| `corresponds_to` | `corresponds_to` | Records a symmetric structural correspondence when no stronger predicate is justified. |

`arranges`, `qualifies`, `bundles`, and `may_realize` originate in the System
Graph, Operational Concerns, Architecture Practices, and Realization Substrate
realms respectively. `documents` originates from a reference-like node.
`realizes` is stronger than `may_realize`: the former asserts an actual selected
mapping, while the latter records only a possible public realization family.

`realm_peer_of` is symmetric and must cross realms. It asserts that the entries
treat the same named notion, not graph-node identity, equality of claims,
interchangeable meanings, bundle membership, or a realization mapping. Use it
when one established term or named pattern is deliberately split into separate
entries because its realm-specific claims need different kinds or boundaries.
Do not use it merely because two entries are related and happen to be in
different realms; use the stronger directed predicate or `corresponds_to`
instead. Author the relation once, preferably from the more explicitly
realm-qualified entry, and state each peer's scope in the rationale.

The generated node projection includes `realm_peers`, a sorted array of peer
node IDs derived from `realm_peer_of` edges. The exporter populates this array
symmetrically on both endpoints even though the relation is authored once. An
empty array means that no realm peer has been declared. The typed edge remains
in the edge collection with its authored rationale; `realm_peers` is navigation
metadata for consumers, not a second source of truth.

A plain wikilink remains appropriate for ordinary conceptual adjacency. Formal
relations are a reviewed semantic layer over the Markdown graph, not a
replacement for explanatory prose.

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
