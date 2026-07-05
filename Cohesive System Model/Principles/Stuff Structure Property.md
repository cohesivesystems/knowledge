---
realm: Principles
kind: principle
created: 2026-06-24
updated: 2026-06-29
---

# Stuff Structure Property

Stuff, structure, and property are a modeling distinction for separating what a model contains, how it is organized, and what constraints it satisfies.

In the Cohesive System Model, this provides a useful lens:

- **Stuff**: the subjects, values, observations, events, entities, observers, identities, and other things the model talks about.
- **Structure**: the operations, relations, transitions, projections, flows, ordering, and composition rules that organize or transform the stuff.
- **Property**: the invariants, policies, laws, constraints, guarantees, and predicates that the stuff and structure must satisfy.

This aligns roughly with:

```txt
entities -> stuff
operations and relations -> structure
invariants and laws -> property
```

The distinction is relative to a model boundary. A transition may be structure in a domain model, but become stuff in a meta-model that classifies transition rules. An invariant may be a property of entity transitions, but become structure when the system represents policies or validation rules as first-class objects.

This lens helps ask:

- Are we adding new things to the model, or only new structure on existing things?
- Is this constraint a property, or is it represented as first-class structure?
- Which parts should be preserved by a [[Functoriality|functorial]] mapping?
- Which parts can be forgotten without changing the intended meaning?
- Are two models equivalent because they preserve the same structure and properties, even if they present different stuff?

Examples:

- An [[Entity|entity]] is stuff, while its [[Transition|transitions]], state history, and emitted events give it structure.
- A [[Transition|transition]] is structure on entity state, observations, commands, authority, and versions.
- An [[Invariant|invariant]] is a property constraining which transitions may commit.
- A [[Projection Models|projection]] adds structure that relates a derived view back to source state or events.
- A [[Realization|realization]] maps semantic stuff, structure, and properties into substrate stuff, structure, and properties.

This distinction also clarifies forgetting. A mapping may forget properties, such as validation constraints; forget structure, such as ordering or causality; or forget stuff, such as collapsing several entities into one aggregate view. These are different losses and should not be treated as the same.

Related concepts: [[Entity|entity]], [[Transition|transition]], [[Invariant|invariants]], [[Policy|policies]], [[Relation|relations]], [[Projection Models|projection models]], [[Realization|realization]], [[Functoriality|functoriality]], [[Equivalence vs Equality|equivalence vs equality]], [[Universal Constructions|universal constructions]].
