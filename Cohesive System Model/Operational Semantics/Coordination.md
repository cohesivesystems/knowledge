---
realm: Operational Semantics
---

# Coordination

Realm: Operational Semantics

Coordination answers: how is multi-step or multi-participant work made coherent across [[Observer|Observers]]?

Coordination defines how multiple transitions, observers, stores, processes, projections, or external systems are made to move together without losing the semantic meaning of the work.

[[Interaction]] provides the edges through which participants affect, observe, or signal one another. Coordination asks whether the resulting multi-participant behavior is coherent with the intended invariants, ordering, failure handling, and commitment boundaries.

[[Business Transactions]] are a common reason coordination is needed: business-level work often composes several local transitions, interactions, persistence boundaries, retries, and recovery paths into one domain outcome.

Coordination mechanisms include:

- Local transactions.
- Distributed transactions.
- Transactional outbox.
- [[CRDTs]].
- Sagas with compensation.
- Durable workflows with resume.
- Choreography through events.
- Process managers.
- Projection update protocols.

[[CRDTs]] coordinate replicated state by making the merge or operation algebra converge under concurrent updates. This reduces the need for synchronous coordination for each update, but only for data types and invariants compatible with the CRDT's convergence semantics.

In [[CQRS]], coordination often centers on consistency under asynchrony: propagating write-side commits to read-side projections while preserving the required ordering, idempotency, freshness, and recovery semantics.

The right mechanism depends on the failure boundaries, persistence choices, delivery semantics, and invariants involved.

Related concepts: [[Interaction]], [[Delivery Semantics]], [[Recovery]], [[Business Transactions]], [[Processes]], [[CRDTs]], [[CQRS]], [[Workflow Engines]], [[Brokers]], [[Invariants]].
