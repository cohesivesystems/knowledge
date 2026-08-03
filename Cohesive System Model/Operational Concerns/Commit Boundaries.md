---
realm: Operational Concerns
kind: operational-concern
created: 2026-06-29
updated: 2026-08-02
aliases:
  - Commit Boundary
  - Commitment
---

# Commit Boundaries

Commit Boundaries answer: what becomes accepted as one unit, and within which boundary?

A commit boundary is the scope in which selected [[Effects|effects]] become accepted, durable, visible, or irreversible according to a declared rule. The rule may commit all covered effects as a unit, reject them as a unit, or record enough durable information for recovery to finish or compensate the work later.

Commitment is boundary-relative. A database transaction commit, event-store append, broker acknowledgment, consumer offset commit, workflow checkpoint, actor turn, outbox record, and business completion are different commitments unless a model explicitly coordinates them.

## Atomic Commit

Atomic commit means the covered effects commit or abort together within the same boundary.

Examples include:

- A local [[ACID]] transaction that commits entity state and an [[Outbox|outbox]] record together.
- An event-store append that commits the next event for an entity stream only if the expected version matches.
- A compare-and-set operation that commits one successor version for a register-like subject.
- A [[Two-Phase Commit|two-phase commit]] protocol that attempts to create one distributed commit boundary across resource managers.

Atomic commit does not automatically mean that downstream observers processed the work, read models caught up, or the [[Business Transactions|business transaction]] completed.

For channel consumption, the candidate operation set can include input consumption, authoritative state mutation, produced output, durable application-progress advancement, and provider settlement. A claim of atomicity should enumerate exactly which of these operations share one commit boundary. When provider settlement lies outside the application transaction, the safe causal order is to commit covered effects and exact progress before settlement, then use replay, redelivery, idempotency, or reconciliation across the remaining crash cut. See [[Delivery Progress and Settlement|delivery progress and settlement]].

## Boundary Questions

For any claimed commit, ask:

- Which effects are covered?
- Which observer, entity, transaction, stream, partition, process, or protocol boundary owns the commit?
- What durability and recovery assumptions preserve the commit?
- What acknowledgment, if any, reports it?
- What remains pending, retryable, compensating, or outside the boundary?

When required effects cross commit boundaries, the model needs a coordination mechanism, such as [[Two-Phase Commit|two-phase commit]], [[Consensus|consensus]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Sagas|sagas]], [[Process Managers|process managers]], [[Durable Execution|durable execution]], compensation, reconciliation, or another [[Weak Isolation Patterns|weak isolation pattern]].

Enterprise Integration Patterns describes a **Transactional Client** as an endpoint that coordinates its messaging actions with a transaction. The transaction's actual participants and boundary must still be named; transaction-aware messaging does not automatically include domain storage, external effects, or downstream processing.

## External References

- Gregor Hohpe and Bobby Woolf, [Transactional Client](https://www.enterpriseintegrationpatterns.com/patterns/messaging/TransactionalClient.html), *Enterprise Integration Patterns*, 2003.

Related concepts: [[Enterprise Integration Patterns|enterprise integration patterns]], [[Boundaries|boundaries]], [[Effects|effects]], [[Interaction Channels|interaction channels]], [[Delivery Progress and Settlement|delivery progress and settlement]], [[Acknowledgments|acknowledgments]], [[ACID]], [[Two-Phase Commit|two-phase commit]], [[Coordination|coordination]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Persistence|persistence]], [[Durability|durability]], [[Recovery|recovery]], [[Consistency Models|consistency models]], [[Isolation|isolation]], [[Dual-Write Problem|dual-write problem]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Business Transactions|business transactions]].
