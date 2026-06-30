---
realm: Operational Semantics
kind: operational-semantics
---

# Concurrency Control

Concurrency Control answers: How can multiple concurrent histories be reconciled into a single valid history?

In the model, commands may carry an expected version or etag: the [[Version|version]] of [[Entity|entity]] state the [[Observer|observer]] believed was current when it formulated the [[Command|command]].

Concurrency-control mechanisms include:

- Optimistic concurrency using [[Version|expected-version]] checks.
- Pessimistic locking.
- Fencing tokens.
- Actor identity serialization.
- Per-key ordering.
- Transactional [[Isolation|isolation]].
- [[CRDTs|CRDT]] merge or commutative-update semantics for compatible replicated state.

These mechanisms have different [[Progress Conditions|progress conditions]]. A lock can be blocking if progress depends on the lock holder. Optimistic retry loops may be obstruction-free, lock-free, or wait-free only under additional assumptions about contention, scheduling, bounded retries, helping, or backoff. Actor serialization gives clear per-entity ordering, but progress still depends on mailbox delivery, scheduler fairness, and actor recovery. If an expected-version check fails, the attempted transition is rejected, no accepted state change occurs for the target entity, and the entity version remains unchanged.

Entity transitions require the [[Observer|observer]] that interprets the attempted transition to remain coherently aligned with the realization context that commits it. There are two common patterns:

- A serialized observer owns the transition boundary, such as an actor that hosts an entity and processes commands for that entity one at a time.
- A temporary observer performs the operation, such as an HTTP request handler that loads entity state, interprets a command, and commits only if the expected version still matches.

Session affinity may help keep related requests near the same cache or host, but it is not a concurrency-control guarantee unless it also enforces exclusive transition ownership.

## Event Schedules and State Histories

Concurrency control depends on the [[Version Histories|version-history]] shape of the state machine being modeled.

A sequential entity behaves like a linear state machine: its endogenous events form a single ordered schedule and its state history is indexed by monotonically advancing versions. Expected-version checks, actor serialization, per-key ordering, and compare-and-swap operations all enforce the rule that only one successor state may be committed from a given current version.

Not all useful state machines are sequential. Git, for example, allows non-sequential state histories: commits form a directed acyclic graph, branches name different heads, and merges explicitly combine histories. In that model, concurrency control is not merely "is the current version still V?" It asks whether the proposed successor is based on acceptable parent states, whether a reference may advance, and whether concurrent heads must be rejected, merged, or preserved.

Event schedules and state histories are therefore related by [[Event-State Duality|event-state duality]], but not interchangeable. A linear entity history can be represented as alternating events and state versions. A non-sequential history may require partial orders, parent links, branch heads, merge events, patch residuals, or conflict records. The concurrency mechanism must match the history shape the system intends to preserve.

Related concepts: [[Command|command]], [[Transition|transition]], [[Version|version]], [[Version Histories|version histories]], [[Consistency Models|consistency models]], [[Progress Conditions|progress conditions]], [[Isolation|isolation]], [[ACID]], [[Weak Isolation Patterns|weak isolation patterns]], [[Entity|entity]], [[Event|event]], [[State|state]], [[Event-State Duality|event-state duality]], [[Event Sourcing|event sourcing]], [[CRDTs]], [[Behavior|behavior]], [[Realization|realization]], [[Ordering|ordering]], [[Actor Systems|actor systems]], [[Storage Systems|storage systems]].
