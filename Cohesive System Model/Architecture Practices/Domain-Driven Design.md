---
realm: Architecture Practices
kind: architecture-practice
---

# Domain-Driven Design

Domain-Driven Design, or DDD, addresses the problem of preserving domain meaning in software as systems grow in complexity.

## Cohesive Formulation

DDD can be expressed as a discipline for making semantic dynamics explicit:

- [[Entity|Entities]] identify enduring domain subjects.
- [[Value|Values]] represent identity-free domain information.
- [[Transition|Transitions]] encode valid domain change.
- [[Invariants]] and [[Policies]] constrain change.
- [[Event|Events]] record or publish committed domain occurrences.
- [[Boundaries]] define where terms, rules, authority, and consistency apply.

## Practice Interpretation

Bounded contexts are semantic and structural boundaries. Aggregates are entity models that scope transitions and invariants. Domain events are endogenous events relative to the boundary in which they are committed. Repositories and application services are realization and interaction choices, not the domain model itself.

## Failure Modes

DDD fails when names are preserved but semantics are not: entities become database rows, value objects become DTOs, domain events become arbitrary messages, and aggregate boundaries are chosen for storage convenience rather than invariant scope.

Related concepts: [[Entity]], [[Value]], [[Transition]], [[Invariants]], [[Policies]], [[Event]], [[Boundaries]], [[Entity Models]].
