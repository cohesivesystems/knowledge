---
realm: Domain Semantics
kind: semantic-construct
created: 2026-06-24
updated: 2026-07-01
---

# Shape

A shape is the logical structure expected of a [[Value|value]], [[Observation|observation]], state view, event payload, command input, query result, or projection result within a model [[Boundaries|boundary]].

Shape answers: what structure must a value have in order to be interpreted, validated, compared, transformed, observed, or transmitted for a declared purpose?

A shape may specify:

- Fields, paths, names, and positions.
- Scalar kinds and composite kinds.
- Required, optional, absent, or null components.
- Cardinality, ordering, and containment.
- Constraints needed for validation or interpretation.
- Projection, selection, masking, or redaction rules.
- Compatibility with schemas, layouts, buffers, serialization formats, or storage records.

Shape is not the same as [[Value|value]]. A value is the concrete structured data. Shape is the declared structure under which that value is understood.

Shape is not the same as [[State|state]]. State is condition or configuration. Shape determines which dimensions of state are made visible, writable, comparable, or required for a particular [[Observation|observation]], [[Query|query]], [[Command|command]], [[Projections|projection]], or [[Transition|transition]].

Shape is not the same as representation. A shape may be represented by a record schema, map, array, ordinal layout, sparse buffer, packed presence bits, columnar layout, or protocol schema. The representation is the physical or substrate form; the shape is the logical structure the model relies on.

Shape is boundary-relative. The same underlying state may be observed through several shapes: a full entity state view, a partial transition input view, a redacted API resource, a search document, a projection row, or a compact protocol payload.

Completeness is therefore shape-relative. A value or observation can be complete for one declared shape and partial for another. "Full state" only means full with respect to the state dimensions included by the chosen boundary and shape.

The word shape is also used informally for graph shape, process shape, interaction shape, or system topology. This entry refers specifically to semantic shape: the logical structure of values and observations used to make state visible and actionable.

Related concepts: [[Value|value]], [[Observation|observation]], [[State|state]], [[Observable|observable]], [[Query|query]], [[Command|command]], [[Transition|transition]], [[Projections|projections]], [[Boundaries|boundaries]], [[Naturality|naturality]], [[Equivalence vs Equality|equivalence vs equality]].
