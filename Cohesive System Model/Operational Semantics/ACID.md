---
realm: Operational Semantics
kind: operational-semantics
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

## External References

- Jim Gray and Andreas Reuter, [Transaction Processing: Concepts and Techniques](https://www.microsoft.com/en-us/research/publication/transaction-processing-concepts-and-techniques/), Morgan Kaufmann, 1993.

Related concepts: [[Isolation]], [[Two-Phase Commit]], [[Weak Isolation Patterns]], [[Consistency Models]], [[Concurrency Control]], [[Coordination]], [[Persistence]], [[Durable Execution]], [[Business Transactions]], [[Transactional Outbox]].
