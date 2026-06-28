---
realm: Principles
kind: principle
---

# Naturality

Naturality is the principle that a transformation should be independent of arbitrary representation choices. It should commute with the structure-preserving maps between representations.

Informally, naturality asks whether the same conceptual operation behaves consistently across equivalent presentations of the same idea.

In categorical terms, a natural transformation relates functors in a way that makes the relevant diagrams commute:

```txt
F(A) -> G(A)
 |       |
 v       v
F(B) -> G(B)
```

In modeling terms, naturality asks:

- Does this transformation depend on accidental representation details?
- If a value, observation, event, or entity is represented differently, does the transformation still mean the same thing?
- Does serialization, projection, reconstitution, validation, or realization commute with the relevant mappings?
- Are special cases breaking a claimed abstraction?

Examples:

- A [[Value]] transform should not depend on whether the value is dictionary-backed, layout-buffer-backed, or columnar, unless representation is explicitly part of the boundary.
- [[Reconstitution]] should produce semantically equivalent observations from different persisted representations when those representations are intended to be equivalent.
- A [[Projections|Projection]] should preserve its declared meaning across schema, storage, or transport changes.
- [[Realization]] should preserve observer, entity, transition, and boundary meaning across runtime choices.

Naturality is useful for detecting hidden coupling. If a model says two representations are equivalent but an operation behaves differently for one of them, the operation is not natural with respect to that equivalence.

Related concepts: [[Functoriality]], [[Value]], [[Observation]], [[Reconstitution]], [[Projections]], [[Realization]], [[Equivalence vs Equality]].
