---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-28
updated: 2026-07-01
---

# ACID

ACID is a transaction contract: atomicity, consistency, isolation, and durability.

In the Cohesive model, ACID describes a realization contract. It says what a transaction manager, database, or storage substrate guarantees for a bounded set of operations. It does not automatically describe a full [[Business Transactions|business transaction]], process, workflow, message publication, downstream observer, or external system.

## Properties

- **Atomicity**: the transaction's covered effects commit as a unit or abort as a unit.
- **Consistency**: the transaction preserves declared validity constraints and invariants within its boundary.
- **Isolation**: concurrent transactions are separated according to the chosen [[Isolation|isolation]] level.
- **Durability**: committed effects survive the failures covered by the persistence mechanism.

The "C" in ACID is not the same as distributed [[Consistency Models|consistency models]]. ACID consistency means preserving invariants across a transaction boundary. On the other hand, distributed consistency models describe which histories, reads, and observations are valid across observers, replicas, sessions, and ordering spaces.

Serializable isolation inside an ACID transaction boundary gives a legal serial transaction order, but it does not by itself imply [[Consistency Models|linearizability]]. Linearizability also requires real-time order. For transactions, that stronger property is usually called strict serializability or external consistency.

## Boundary Limits

ACID is powerful because it composes several guarantees inside one commitment boundary. The limit is that the boundary is rarely identical to the business outcome.

A local ACID transaction may commit entity state and an outbox record. It does not prove that a broker delivered the output event, that another observer processed it, that a read model caught up, or that the broader business transaction completed.

When the work crosses multiple ACID boundaries, the model must choose a coordination strategy. [[Two-Phase Commit]] can try to create one atomic commit across participants. If that is unavailable, too expensive, or undesirable, the system must use explicit [[Weak Isolation Patterns|weak isolation patterns]].

## Transaction Logs and Recovery

Database transactions rely on recovery semantics, not only isolation semantics. ARIES is the classic reference point: a transaction manager uses [[Write-Ahead Logging|write-ahead logging]], log sequence numbers, redo, undo, checkpoints, and Compensation Log Records to preserve atomicity and durability through crash recovery and partial rollback.

This matters for the Cohesive model because a transaction's visible state is backed by an ordered durable history inside the storage substrate. The log may be internal to the database rather than part of the domain model, but it still realizes [[Persistence|persistence]], [[Reconstitution|reconstitution]], and [[Recovery|recovery]] for the transaction boundary.

## External References

- Jim Gray and Andreas Reuter, [Transaction Processing: Concepts and Techniques](https://www.microsoft.com/en-us/research/publication/transaction-processing-concepts-and-techniques/), Morgan Kaufmann, 1993.
- C. Mohan, Don Haderle, Bruce Lindsay, Hamid Pirahesh, and Peter Schwarz, [ARIES: A Transaction Recovery Method Supporting Fine-Granularity Locking and Partial Rollbacks Using Write-Ahead Logging](https://web.stanford.edu/class/cs345d-01/rl/aries.pdf), ACM Transactions on Database Systems, 17(1):94-162, March 1992. [IBM Research](https://research.ibm.com/publications/aries-a-transaction-recovery-method-supporting-fine-granularity-locking-and-partial-rollbacks-using-write-ahead-logging)

Related concepts: [[Isolation|isolation]], [[Two-Phase Commit|two-phase commit]], [[Weak Isolation Patterns|weak isolation patterns]], [[Consistency Models|consistency models]], [[Concurrency Control|concurrency control]], [[Coordination|coordination]], [[Persistence|persistence]], [[Reconstitution|reconstitution]], [[Recovery|recovery]], [[Write-Ahead Logging|write-ahead logging]], [[Durable Execution|durable execution]], [[Business Transactions|business transactions]], [[Transactional Outbox|transactional outbox]].
