---
realm: Semantic Dynamics
kind: semantic-construct
---

# Observation

An **observation** is a contextualized [[Value|value]] produced by an [[Observable|observable]] acting on [[State|state]]. It is the form in which state becomes usable by an [[Observer|observer]] relative to a [[Boundaries|boundary]].

An observation has:

- A [[Value|value]], such as a scalar, array, vector, map, record, bytes, null, or another composite.
- A [[Shape|shape]] or representation, such as a schema, projection, record layout, or optimized internal buffer.
- A subject, source, or address that says what state the value was read from or derived from.
- Optional context such as version, observer, source, and field-level lineage.

The value inside an observation is identity-free, version-free, lineage-free, and timeless. Observation metadata supplies attribution and provenance when correctness requires it.

Observations do not carry intrinsic occurrence time. Time and occurrence belong to [[Event|events]]. An observation may carry a source version or observed-at metadata, but that is provenance or addressing, not the event occurrence itself.

When an [[Entity|entity]] is reconstituted, its current state is delivered as an entity-scoped observation. When an exogenous event arrives, its value can be observed and interpreted by an observer relative to a [[Boundaries|boundary]]. [[Command|Commands]] are validated against observations of current entity state, related state, policy state, and environmental state. [[Query|Queries]] request observations or values from state, projections, read models, or computations.

Entity state is a specialized observation whose subject is an entity. Non-entity observations may describe relations, projections, processes, policies, query results, aggregates, or runtime environment.

An event can be understood structurally as a time-bearing value. When the event is interpreted by an observer relative to a [[Boundaries|boundary]], it may become an input event, command, endogenous event, output event, or ignored/rejected input.

Related concepts: [[Value|value]], [[Shape|shape]], [[State|state]], [[Observable|observable]], [[Observer|observer]], [[Boundaries|boundaries]], [[Event|event]], [[Command|command]], [[Query|query]], [[Reconstitution|reconstitution]], [[Optics and Lenses|optics and lenses]], [[Fibrations and Indexed Structure|fibrations and indexed structure]].
