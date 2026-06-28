---
realm: Architecture Practices
---

# CQRS As Architecture Practice

CQRS is often described as an architectural pattern or style. In the Cohesive System Model, the technical mechanics are captured by [[CQRS]] as a realization substrate pattern.

## Problem

CQRS addresses the problem that [[Command|command]] handling and [[Query|query]] answering often have different semantic, operational, and performance requirements.

## Cohesive Formulation

The command side protects transition correctness, authority, invariants, and versioned persistence. The query side answers [[Query|queries]] by reconstituting observations through projections, indexes, materialized views, or caches.

The central separation is:

```txt
write-side persistence -> read-side reconstitution
```

## Practice Interpretation

As an architecture practice, CQRS makes the read/write split a deliberate boundary. That boundary introduces consistency-under-asynchrony concerns: projection lag, read-your-writes, monotonic reads, ordering scope, idempotent updates, and recovery.

Related concepts: [[CQRS]], [[Command]], [[Query]], [[Transition]], [[Persistence]], [[Reconstitution]], [[Projections]], [[Observation]], [[Event Sourcing as Architecture Practice]].
