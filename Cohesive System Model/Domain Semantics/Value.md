---
realm: Domain Semantics
kind: semantic-construct
---

# Value

A **value** is pure structured data. It is the concrete information used to read, write, transmit, compare, validate, transform, or carry state.

Values are identity-free, version-free, lineage-free, and timeless. They do not carry subject, observer, source, occurrence, or provenance. Those belong to contextual concepts such as [[Observation|observation]], [[Event|event]], entity state, state records, histories, and lineage metadata.

A value may be:

- Empty or absent, such as null or undefined.
- Scalar, such as boolean, integer, decimal, string, temporal value, or bytes.
- Composite, such as array, vector, map, dictionary, record, object, or another structured aggregate.

A value may have a [[Shape|shape]] or representation. The shape describes the logical structure expected by a model or operation. The representation describes how the value is physically stored or accessed, such as dictionary-backed fields, ordinal record layouts, sparse buffers, packed presence bits, columnar storage, or struct-of-arrays storage.

Representation is not part of semantic identity. Two values with the same logical content are the same value even if one is dictionary-backed and another is layout-buffer-backed. Optimized representations must preserve logical equality, validation, serialization, and transformation behavior.

Values relate to the other semantic concepts as follows:

- [[State]] is condition; value is the concrete information used to read or write that condition.
- [[Observation]] is a value with context: subject, [[Shape|shape]], source, version, observer, or lineage.
- [[Event]] is a value with occurrence.
- [[Command]] is an input [[Event|event]] interpreted as an attempted [[Transition|transition]].
- [[Query]] is an input [[Event|event]] interpreted as a request to observe, compute, or return information.
- Entity state is an entity-scoped observation: a value attributed to an entity identity at a version.
- A [[Transition|transition]] consumes values and observations in a transition context and may produce an accepted endogenous event or state change.

Values may be complete, partial, or projected only relative to a declared [[Shape|shape]], model [[Boundaries|boundary]], or operation. Completeness is not intrinsic to the value itself.

Related concepts: [[Shape|shape]], [[State|state]], [[Observation|observation]], [[Event|event]], [[Command|command]], [[Query|query]], [[Transition|transition]], [[Entity|entity]], [[Observable|observable]], [[Boundaries|boundaries]], [[Equivalence vs Equality|equivalence vs equality]], [[Naturality|naturality]].
