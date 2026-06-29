---
realm: Operational Semantics
kind: operational-semantics
---

# Coordination

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
- [[Durable Execution|Durable execution]] with resume.
- Choreography through events.
- Process managers.
- Projection update protocols.

## Ordering, Intent, And Avoidance

[[Ordering]] preserves distinctions that may matter semantically. If `A then B` and `B then A` collapse into the same result, the model may lose intent, causality, auditability, or invariant context. Ordered, non-commutative histories are therefore valuable when the domain needs to preserve what happened before what.

Preserving order across distributed boundaries usually requires coordination. Coordination may add latency, reduce availability under partitions, constrain throughput, or create operational coupling. The design question is whether the domain invariant really requires the order being preserved.

Coordination avoidance designs move work into structures where concurrent updates can be accepted without synchronously agreeing on one global order. [[CRDTs]] do this with monotonic merge or commutative operations when the domain can tolerate temporary divergence and the invariants are compatible with the data type. Probabilistic data structures can play a similar role when approximate answers are acceptable and their update or merge operations compose without central serialization.

The tradeoff is not "ordered" versus "unordered" in general. It is choosing which distinctions must be preserved and which can be safely forgotten, merged, approximated, or made commutative. Those choices determine the [[Consistency Models|consistency model]] the system can honestly claim.

[[CRDTs]] coordinate replicated state by making the merge or operation algebra converge under concurrent updates. This reduces the need for synchronous coordination for each update, but only for data types and invariants compatible with the CRDT's convergence semantics.

In [[CQRS]], coordination often centers on consistency under asynchrony: propagating write-side commits to read-side projections while preserving the required ordering, idempotency, freshness, and recovery semantics.

The right mechanism depends on the failure boundaries, persistence choices, delivery semantics, and invariants involved.

## External References

- Peter Bailis, Alan Fekete, Ali Ghodsi, Joseph M. Hellerstein, and Ion Stoica, [Coordination Avoidance in Database Systems](https://www.vldb.org/pvldb/vol8/p185-bailis.pdf), PVLDB 8(3):185-196, 2014.

Related concepts: [[Interaction]], [[Ordering]], [[Version Histories]], [[Consistency Models]], [[Delivery Semantics]], [[Durable Execution]], [[Recovery]], [[Business Transactions]], [[Processes]], [[CRDTs]], [[CQRS]], [[Workflow Engines]], [[Durable Execution Engines]], [[Brokers]], [[Invariants]].
