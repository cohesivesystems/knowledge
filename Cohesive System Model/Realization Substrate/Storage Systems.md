---
realm: Realization Substrate
kind: realization-substrate
created: 2026-06-24
updated: 2026-07-29
---

# Storage Systems

Storage Systems are concrete mechanisms for durable or semi-durable data: databases, event stores, object stores, key-value stores, logs, file systems, caches, and actor state providers.

Storage systems [[Realization|realize]] [[Persistence|persistence]], support [[Reconstitution|reconstitution]], and participate in coordination and concurrency control.

For [[Event Sourcing|event sourcing]], an event store is not merely a log of received messages. It stores committed persistence events interpreted as state actions that define an entity's versioned state history. Those records are domain events only when the domain independently assigns them that meaning.

For [[CQRS]], write-side storage and read-side storage may have different shapes, consistency guarantees, and recovery strategies. The write side commits authoritative transition effects; the read side realizes reconstituted observations for [[Query|queries]]. A transition decision is not committed state merely because it was evaluated successfully.

For [[CRDTs]], storage must preserve the data type's convergence requirements, including replica identifiers, causal metadata, tombstones, deltas, or operation history when those are part of the merge semantics.

Some replicated storage systems realize [[Replica Models|replica models]] with [[Consensus Protocols|consensus protocols]] to elect leaders, replicate logs, commit writes, and expose stronger consistency guarantees at a [[Partition Models|partition]] or key range. Those guarantees depend on the exact read and write path, not merely on the presence of a consensus implementation inside the storage system.

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

## Execution Definitions and Commit Plans

Storage systems may persist canonical [[Transition Models|transition models]], [[Process Graphs|process graphs]], their accepted revisions and normalized content identities, and the source or compiler provenance needed to interpret them independently of one application binary.

A transition decision describes a sparse patch, outcome, emissions, movements, and guarantee demands. Storage interprets the commit plan. It must preserve the validity of every observation that influenced the decision through the required commit boundary, apply the entity's concurrency and version rule, and make required local obligations durable atomically when the modeled scope demands it.

Storage must not silently turn an unavailable atomic scope into a sequence of weaker writes. It may realize a requirement natively, compose several mechanisms, or report constraints and unavailable capabilities. Multi-entity atomicity requires evidence at the actual participating authority and storage boundaries; otherwise compensation or reconciliation must be authored explicitly in the process graph.

## Durable Process Material

Durable process execution may require storage for:

- Definition identity, semantic revision, normalized content identity, and checkpoint schema version.
- Process instance, process attempt, activation sequence, and token identities.
- Complete token state, fork and join membership, typed bindings, and terminal outcomes.
- Wait registrations, timers, early or buffered inputs, and claimed or consumed signal identities.
- Inbox admission and deduplication records.
- Outbound emission intent, pending replies, and operation-attempt ledgers.
- Retry, acknowledgment, ambiguous-outcome, reconciliation, compensation, and control state.
- Ownership, leases, claims, revisions, and fences.

A physical checkpoint need not use one prescribed schema, but it must preserve the canonical continuation state and its declared guarantees. One current-node cursor is insufficient when a process supports parallel tokens, fork and join recovery, or more than one armed wait.

When an activation reaches a durable cut, the required atomic commit may include continuation state, eligible local entity mutations, wait registration, inbox or outbox intent, and staged replies. The exact physical transaction is substrate-specific; the semantic scope and lost-wakeup, duplicate, and crash-boundary obligations are not.

A storage system stores records, logs, snapshots, projections, or histories. The model defines what those stored values mean.

Shared-database integration and message stores are specialized uses of storage as a mediating interaction locus. Sharing physical storage does not erase semantic ownership, transaction, isolation, compatibility, authority, retention, or recovery boundaries. A diagnostic message store is not automatically authoritative domain history.

## External References

- Enterprise Integration Patterns, [Shared Database, Message Store, and integration patterns](https://www.enterpriseintegrationpatterns.com/patterns/messaging/toc.html).

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Execution Kernel|execution kernel]], [[Realization|realization]], [[Transition Models|transition models]], [[Process Graphs|process graphs]], [[Replica Models|replica models]], [[Partition Models|partition models]], [[Messages and Envelopes|messages and envelopes]], [[Batch and File Exchange|batch and file exchange]], [[Observability and Provenance|observability and provenance]], [[Retention Expiration and Quarantine|retention, expiration, and quarantine]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Concurrency Control|concurrency control]], [[Consensus Protocols|consensus protocols]], [[ACID]], [[Write-Ahead Logging|write-ahead logging]], [[Commit Boundaries|commit boundaries]], [[Effect|effect]], [[Effects]], [[State|state]], [[Event|event]], [[Query|query]], [[Event Sourcing|event sourcing]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[CRDTs]], [[CQRS]], [[Projection Models|projection models]], [[Durable Execution Engines|durable execution engines]], [[Recovery|recovery]].
