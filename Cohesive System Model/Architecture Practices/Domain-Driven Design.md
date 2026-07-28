---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-27
aliases:
  - DDD
---

# Domain-Driven Design

Domain-Driven Design, or DDD, addresses the problem of preserving domain meaning in software as systems grow in complexity.

## Cohesive Formulation

DDD can be expressed as a discipline for making domain semantics explicit:

- [[Entity|Entities]] identify enduring domain subjects.
- [[Value|Values]] represent identity-free domain information.
- [[Transition|Transitions]] encode valid domain change.
- [[Invariant|Invariants]] and [[Policy|policies]] constrain change.
- [[Event|Events]] record or publish committed domain occurrences.
- [[Boundaries]] define where terms, rules, authority, and consistency apply.

## In the Model

Bounded contexts are semantic and structural boundaries. Aggregates are entity models that scope transitions and invariant scopes. Domain events are endogenous events relative to the boundary in which they are committed. Repositories and application services are realization and interaction choices, not the domain model itself.

## Failure Modes

DDD fails when names are preserved but semantics are not: entities become database rows, value objects become DTOs, domain events become arbitrary messages, and aggregate boundaries are chosen for storage convenience rather than invariant scope.

## External References

- Eric Evans, [*Domain-Driven Design: Tackling Complexity in the Heart of Software*](https://www.informit.com/store/domain-driven-design-tackling-complexity-in-the-heart-9780321125217), Addison-Wesley Professional, 2003.
- Vaughn Vernon, [*Implementing Domain-Driven Design*](https://www.informit.com/store/implementing-domain-driven-design-9780321834577), Addison-Wesley Professional, 2013.
- Vaughn Vernon, [*Domain-Driven Design Distilled*](https://www.informit.com/store/domain-driven-design-distilled-9780134434988), Addison-Wesley Professional, 2016.

Related concepts: [[Entity|entity]], [[Value|value]], [[Transition|transition]], [[Invariant|invariants]], [[Policy|policies]], [[Event|event]], [[Boundaries|boundaries]], [[Entity Models|entity models]].
