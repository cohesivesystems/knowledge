---
realm: Operational Semantics
kind: operational-semantics
---

# Concurrency Control

Concurrency Control answers: how are conflicting attempts to change the same semantic subject constrained?

In the model, commands may carry an expected version or etag: the [[Version]] of [[Entity]] state the [[Observer]] believed was current when it formulated the [[Command]].

Concurrency-control mechanisms include:

- Optimistic concurrency using expected-version checks.
- Pessimistic locking.
- Fencing tokens.
- Actor identity serialization.
- Per-key ordering.
- Transactional [[Isolation|isolation]].
- [[CRDTs|CRDT]] merge or commutative-update semantics for compatible replicated state.

If an expected-version check fails, the attempted transition is rejected, no accepted state change occurs for the target entity, and the entity version remains unchanged.

Entity transitions require the [[Observer]] that interprets the attempted transition to remain coherently aligned with the realization context that commits it. There are two common patterns:

- A serialized observer owns the transition boundary, such as an actor that hosts an entity and processes commands for that entity one at a time.
- A temporary observer performs the operation, such as an HTTP request handler that loads entity state, interprets a command, and commits only if the expected version still matches.

Session affinity may help keep related requests near the same cache or host, but it is not a concurrency-control guarantee unless it also enforces exclusive transition ownership.

## Event Schedules And State Histories

Concurrency control depends on the [[Version Histories|version-history]] shape of the state machine being modeled.

A sequential entity behaves like a linear state machine: its endogenous events form a single ordered schedule and its state history is indexed by monotonically advancing versions. Expected-version checks, actor serialization, per-key ordering, and compare-and-swap operations all enforce the rule that only one successor state may be committed from a given current version.

Not all useful state machines are sequential. Git, for example, allows non-sequential state histories: commits form a directed acyclic graph, branches name different heads, and merges explicitly combine histories. In that model, concurrency control is not merely "is the current version still V?" It asks whether the proposed successor is based on acceptable parent states, whether a reference may advance, and whether concurrent heads must be rejected, merged, or preserved.

Event schedules and state histories are therefore related by [[Event-State Duality]], but not interchangeable. A linear entity history can be represented as alternating events and state versions. A non-sequential history may require partial orders, parent links, branch heads, merge events, patch residuals, or conflict records. The concurrency mechanism must match the history shape the system intends to preserve.

Related concepts: [[Command]], [[Transition]], [[Version]], [[Version Histories]], [[Consistency Models]], [[Isolation]], [[ACID]], [[Weak Isolation Patterns]], [[Entity]], [[Event]], [[State]], [[Event-State Duality]], [[Event Sourcing]], [[CRDTs]], [[Behavior]], [[Realization]], [[Ordering]], [[Actor Systems]], [[Storage Systems]].
