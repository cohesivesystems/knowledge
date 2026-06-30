---
realm: System Structure
kind: structural-construct
---

# Entity Models

Entity models describe how the semantic [[Entity|entity]] role is arranged in the system graph.

At the structure level, entity models organize placement, ownership, and composition around stable [[Identity|identities]], versioned state histories, transitions, invariants, policies, and effects. This page describes structural use of the entity role, not the primitive definition of entity and not a specific runtime or storage implementation.

An entity collection, aggregate, actor, record, workflow subject, or domain object may all occupy the entity role when the model treats it as an identifiable subject whose [[State|state]] evolves over time. Concrete mechanisms such as actor placement, database rows, documents, tables, or storage records belong to substrate concerns such as [[Actor Systems|actor systems]] and [[Storage Systems|storage systems]].

This structural concept may also be called an entity model: a model-specific arrangement of the semantic entity role.

## Semantic and Structural Multiplicity

A single semantic entity can have multiple structural entity models. Each model realizes the same semantic subject under a different boundary, purpose, or operational role.

For example, a semantic Shipment entity may appear structurally as:

- Shipment aggregate: owns core lifecycle transitions and invariants.
- Shipment process subject: tracks long-running workflow state.
- Shipment read model: supports [[Query|queries]] or UI.
- Shipment search document: supports search.
- Shipment API resource: exposes a boundary-specific shape.
- Shipment actor: serializes command handling in a runtime.

These are not necessarily the same structural entity, even when they correspond to the same semantic subject. Some may be canonical state, some may be projections, some may be process subjects, and some may be boundary-specific resources.

The relation is many-to-many. One semantic entity may have several structural entity models, and one structural entity model may combine aspects of several semantic entities, such as a dashboard row that joins shipment, carrier, customer, and exception state.

Entity models provide structure for:

- Addressing current and historical state.
- Scoping transitions and invariants.
- Deciding which observer, if any, hosts the entity transition boundary.
- Emitting endogenous events.
- Relating observations across time as versions of the same subject.

Related concepts: [[Entity|entity]], [[Observer|observer]], [[State|state]], [[Identity|identity]], [[Version|version]], [[Transition|transition]], [[Query|query]], [[Invariants|invariants]], [[Policies|policies]], [[Boundaries|boundaries]], [[Relations|relations]], [[Projections|projections]], [[Realization|realization]], [[Concurrency Control|concurrency control]].
