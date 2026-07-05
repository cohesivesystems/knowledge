---
realm: System Graph
kind: structural-construct
created: 2026-06-24
updated: 2026-07-05
aliases:
  - Invariant Scope
  - Invariant Scopes
---

# Invariant Scopes

Invariant scopes describe where semantic [[Invariant|invariants]] are attached in the system graph.

At the structure level, an invariant scope identifies which entity model, process graph, transition, relation model, projection model, observer model, or boundary the invariant constrains. This describes the constraint's modeled scope and dependency surface, not a specific validation mechanism or runtime enforcement substrate.

Under the [[Stuff Structure Property|stuff structure property]] lens, an invariant is primarily property: a constraint or predicate that valid stuff and structure must satisfy. An invariant scope becomes structure when the model represents the constraint as an explicit attachment, dependency, validation rule, or first-class graph element.

Invariant scopes may require observations of:

- Current state observations.
- Expected versions.
- Related entities, relation models, or projection models.
- Process state.
- Policy and authority context.
- External facts observed through an observer boundary.

When an invariant fails, the command is rejected for the target entity and no accepted state change occurs for that entity.

With [[CRDTs]], invariants must be checked for compatibility with monotonic merge or commutative updates. Non-monotonic invariants may still require coordination, escrow, reservations, or a different data model.

Related concepts: [[Invariant|invariant]], [[Entity Models|entity models]], [[Process Graphs|process graphs]], [[Relation Models|relation models]], [[Projection Models|projection models]], [[Observer Models|observer models]], [[Entity|entity]], [[State|state]], [[Observation|observation]], [[Command|command]], [[Transition|transition]], [[Version|version]], [[Stuff Structure Property|stuff structure property]], [[Concurrency Control|concurrency control]], [[CRDTs]].
