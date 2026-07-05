---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-05
aliases:
  - Relation Graph
  - Relation Graphs
  - Relational Model
  - Relational Models
---

# Relation Models

Relation models describe how semantic [[Relation|relations]] are represented in the system graph.

At the structure level, relation models connect identities, states, observations, observer models, entity models, process graphs, events, boundaries, policy scopes, and invariant scopes by dependency, reference, observation, constraint, causation, derivation, or inclusion. This describes graph shape and semantic dependency, not a specific join mechanism, network link, storage relation, or runtime call.

Examples of modeled relations include:

- Entity-to-entity references.
- Observer-to-entity hosting.
- Observer-to-observer interaction edges.
- Event-to-state causation.
- Projection derivation.
- Policy or invariant scope.
- Boundary inclusion.

Relation models make the system graph navigable and explain how changes in one part of the model may be observed, derived, constrained, or interpreted elsewhere.

Related concepts: [[Relation|relation]], [[Entity Models|entity models]], [[Observer Models|observer models]], [[Process Graphs|process graphs]], [[Projection Models|projection models]], [[Entity|entity]], [[Observer|observer]], [[Identity|identity]], [[State|state]], [[Observation|observation]], [[Event|event]], [[Boundaries|boundaries]], [[Realization|realization]].
