---
realm: System Structure
---

# Projections

Realm: System Structure

Projections describe how derived observations or derived state views are arranged in the system graph.

At the structure level, projections organize how one semantic view is shaped from another. They may support [[Query|queries]], read models, indexes, materialized views, UI models, analytics, routing views, or process state. This describes derivation and dependency structure, not the concrete database, cache, index, or compute substrate that realizes it.

Projection state is usually not the primary semantic history. It is a derived observation that must be related back to its source, update protocol, and recovery strategy.

In [[CQRS]], projections commonly realize the query side: read-oriented observations derived from authoritative write-side persistence and selected by [[Query|queries]].

[[CRDTs]] may realize projections or replicated read models when their update algebra can tolerate asynchronous, concurrent updates and converge without central serialization.

Projection should be understood functorially where possible: it maps source structure into a derived view while preserving the identities, versions, dependencies, or ordering needed for the projection's purpose.

Projection concerns include:

- Source events or state.
- [[Shape]] of the derived observation.
- Update ordering.
- Lag and consistency expectations.
- Rebuild and recovery.
- Idempotent update handling.

Related concepts: [[Functoriality]], [[Observation]], [[Observable]], [[Shape]], [[Query]], [[State]], [[Event]], [[Persistence]], [[Reconstitution]], [[CRDTs]], [[CQRS]], [[Ordering]], [[Recovery]].
