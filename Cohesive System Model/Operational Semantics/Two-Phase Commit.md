---
realm: Operational Semantics
kind: operational-semantics
---

# Two-Phase Commit

Two-Phase Commit is a coordination protocol for atomic commit across multiple participants.

It attempts to make several resource managers act like one commitment boundary. A coordinator first asks participants to prepare. If every participant votes to commit, the coordinator records and sends the commit decision. If any participant votes to abort or fails before prepare succeeds, the coordinator aborts.

## Semantics

Two-phase commit provides atomic agreement about commit or abort for the participants covered by the protocol. It is a realization mechanism for a distributed transaction boundary, not a business guarantee by itself.

The protocol does not eliminate the need to define [[Isolation]], [[Persistence|durability]], recovery behavior, participant membership, timeout meaning, idempotency, or what external observers may see while the protocol is in progress.

## Costs And Failure Modes

Two-phase commit is coordination-heavy. It adds synchronous dependency between participants, increases latency, and can reduce availability when participants or the coordinator are unreachable.

Classic two-phase commit can block: a prepared participant may be unable to unilaterally decide commit or abort if it loses contact with the coordinator. Recovery requires durable logs and careful replay of coordinator and participant decisions.

## Alternatives

When a single distributed transaction boundary is unavailable or too costly, systems often use [[Weak Isolation Patterns|weak isolation patterns]] such as transactional outbox, sagas, compensation, idempotent retry, escrow, reservations, reconciliation, or [[CRDTs|CRDT]]-compatible updates.

These alternatives do not provide the same semantics as two-phase commit. They replace one atomic boundary with explicit process, recovery, and invariant-preservation rules.

## External References

- Jim Gray and Andreas Reuter, [Transaction Processing: Concepts and Techniques](https://www.microsoft.com/en-us/research/publication/transaction-processing-concepts-and-techniques/), Morgan Kaufmann, 1993.

Related concepts: [[ACID]], [[Isolation]], [[Coordination]], [[Concurrency Control]], [[Persistence]], [[Recovery]], [[Durable Execution]], [[Business Transactions]], [[Weak Isolation Patterns]].
