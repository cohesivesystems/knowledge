---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-06-29
---

# Storage Systems

Storage Systems are concrete mechanisms for durable or semi-durable data: databases, event stores, object stores, key-value stores, logs, file systems, caches, and actor state providers.

Storage systems [[Realization|realize]] [[Persistence|persistence]], support [[Reconstitution|reconstitution]], and participate in coordination and concurrency control.

For [[Event Sourcing|event sourcing]], an event store is not merely a log of received messages. It stores the committed endogenous events that define an entity's versioned state history.

For [[CQRS]], write-side storage and read-side storage may have different shapes, consistency guarantees, and recovery strategies. The write side is authoritative for transitions; the read side realizes reconstituted observations for [[Query|queries]].

For [[CRDTs]], storage must preserve the data type's convergence requirements, including replica identifiers, causal metadata, tombstones, deltas, or operation history when those are part of the merge semantics.

Some replicated storage systems use [[Consensus Protocols|consensus protocols]] to elect leaders, replicate logs, commit writes, and expose stronger consistency guarantees at a partition or key range. Those guarantees depend on the exact read and write path, not merely on the presence of a consensus implementation inside the storage system.

Transaction-oriented storage systems may also maintain internal [[Write-Ahead Logging|write-ahead logs]] for recovery. ARIES is the classic example: the storage engine uses log sequence numbers, checkpoints, redo, undo, and Compensation Log Records to recover transaction state after failure.

Storage concerns include:

- Data model and shape.
- Transaction scope.
- Consistency guarantees.
- Version or etag support.
- Indexing and [[Query|query]] behavior.
- Retention and compaction.
- Backup and recovery.
- Change streams, [[Outbox|outbox]], or [[Transactional Inbox|inbox]] support.

A storage system stores records, logs, snapshots, projections, or histories. The model defines what those stored values mean.

Related concepts: [[Realization|realization]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Concurrency Control|concurrency control]], [[Consensus Protocols|consensus protocols]], [[ACID]], [[Write-Ahead Logging|write-ahead logging]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[State|state]], [[Event|event]], [[Query|query]], [[Event Sourcing|event sourcing]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[CRDTs]], [[CQRS]], [[Projections|projections]], [[Recovery|recovery]].
