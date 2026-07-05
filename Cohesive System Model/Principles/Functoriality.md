---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-07-01
---

# Functoriality

Functoriality is the principle that a mapping between domains should preserve the structure that matters: identities, relationships, composition, and change.

Informally, it lets the model relate distinct semantic domains without collapsing them. The cave-shadow analogy is useful only if changes in the source are also related to changes in the shadows. A functorial view does not merely map things to things; it maps transformations to transformations in a way that preserves how they compose.

In categorical terms, a functor maps:

```txt
objects -> objects
morphisms -> morphisms
identity morphisms -> identity morphisms
compositions -> compositions
```

In modeling terms, functoriality asks:

- What is the source domain?
- What is the target domain?
- What are the objects being related?
- What are the changes, dependencies, transitions, observations, or interactions being preserved?
- What information is forgotten, collapsed, aggregated, or made explicit?
- Which diagrams are expected to commute?

Examples in the Cohesive System Model:

- [[Realization]] relates semantic roles and operational concerns to substrate mechanisms while preserving the meanings that matter for correctness.
- [[Projections]] map one semantic view into another while preserving selected identity, version, dependency, or derivation structure.
- [[Reconstitution]] maps persisted material back into usable observations of state.
- Folding an event schedule into [[Behavior|behavior]] maps event occurrences and ordering into state samples and time-varying values through an interpretation function.
- A protocol mapping should preserve the intended [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], acknowledgment meaning, and failure boundary rather than merely transmit bytes.

Functoriality is violated when two layers are related only by names. For example, saying that an actor realizes an entity is not enough; routing, ordering, state access, persistence, recovery, and concurrency control must preserve the entity transition semantics.

Functoriality also clarifies partial or lossy mappings. A projection may forget fields. A state sample may forget event causality. A serialization may forget object identity. A realization may preserve command interpretation while not preserving locality or timing. These are acceptable only when the forgotten structure is outside the relevant boundary or explicitly accounted for.

Related concepts: [[Realization|realization]], [[Projections|projections]], [[Reconstitution|reconstitution]], [[Behavior|behavior]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Boundaries|boundaries]].
