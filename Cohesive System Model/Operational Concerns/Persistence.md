---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-24
updated: 2026-07-04
---

# Persistence

Persistence answers: what is recorded as authoritative material?

In the cohesive system model, persistence chooses which view of the system is recorded as the authoritative basis for future execution, reconstitution, coordination, recovery, or audit. [[Durability]] then states which failures that material is expected to survive.


Persistent material may include:

- Current-state records as [[Observation|observations]].
- [[Event Sourcing|Event-sourced]] histories of committed endogenous [[Event|events]].
- Transaction logs, [[Write-Ahead Logging|write-ahead logs]], checkpoints, and recovery records.
- [[Outbox]] records.
- [[Transactional Inbox|Inbox]] and deduplication records.
- Actor state providers.
- Workflow histories.
- Process execution histories, checkpoints, timers, signals, and pending work.
- Process state.
- [[Projection Models|Projection]] state as derived observations.
- [[CRDTs|CRDT]] replica state, deltas, operations, and causal metadata.

Persistence is not a single technology choice. It is a semantic decision about what the system treats as recoverable truth inside a boundary. Durability is the separate claim that this material survives declared failures and remains usable after them.

For [[CRDTs]], persistence must preserve enough replica state, operation history, delta history, and causal metadata for merge and convergence semantics to remain valid after restart, compaction, replication, or recovery.

In [[CQRS]], persistence usually names the authoritative write-side material from which read-side observations are reconstituted or projected.

In database transaction systems, the transaction log may be the authoritative recovery material even when the application primarily sees tables, rows, and indexes. ARIES-style [[Write-Ahead Logging|write-ahead logging]] is an example where redo and undo records make committed state recoverable after crash, partial rollback, and restart.

Persistence and [[Reconstitution|reconstitution]] form a useful [[Duality and Symmetry|duality]]: persistence makes selected material durable, while reconstitution turns durable material back into usable observations. The duality is not perfect because persistence choices determine what can later be reconstituted.

Related concepts: [[Durability|durability]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[ACID]], [[Write-Ahead Logging|write-ahead logging]], [[Durable Execution|durable execution]], [[Duality and Symmetry|duality and symmetry]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[State|state]], [[Observation|observation]], [[Event|event]], [[Event Sourcing|event sourcing]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[CRDTs]], [[CQRS]], [[Storage Systems|storage systems]], [[Workflow Engines|workflow engines]], [[Durable Execution Engines|durable execution engines]], [[Actor Systems|actor systems]].
