---
realm: Architecture Practices
kind: pattern
---

# Transactional Outbox

The transactional outbox addresses the problem of committing local state change and publishing a message without relying on a distributed transaction between the database and broker.

The concrete substrate pattern is [[Outbox|outbox]]. The architecture practice is deciding where that outbox belongs, which transition or process creates the obligation, which relay publishes it, and what downstream delivery, idempotency, and recovery semantics are required.

## Cohesive Formulation

The practice separates domain commitment from publication:

```txt
entity transition + outbox record commit in one persistence boundary
outbox relay -> broker interaction boundary
```

The outbox record is durable operational material that represents responsibility to publish after the domain transition commits.

## In the Model

The outbox makes [[Commit Boundaries|commit boundaries]] and [[Acknowledgments|acknowledgment]] spaces explicit. A database transaction can commit the entity transition and outbox record. Broker publication and downstream observation happen later, with their own delivery, ordering, retry, and idempotency semantics.

Outbox is therefore not "exactly-once messaging." It is local atomicity plus asynchronous publication responsibility. It prevents the local [[Dual-Write Problem|dual-write problem]] between state persistence and outbound publication responsibility, but it does not prove that another observer received, processed, or committed follow-up work.

## Relationship to Event Sourcing

[[Event Sourcing]] and transactional outbox both use durable committed material to tie persistence to coordination.

In event sourcing, the committed endogenous event history can be the atomic source of both entity reconstitution and downstream orchestration. Projections, process managers, subscribers, and publications can follow the same committed history that defines the entity state.

In transactional outbox, the domain state change and an outbound obligation are committed together in one local transaction. This gives a similar consistency shape even when the authoritative state is a current-state record rather than an event stream.

The shared principle is:

```txt
do not commit authoritative state and coordination trigger as independent writes
```

If the trigger that tells the rest of the system to act is not committed atomically with the authoritative transition, or reliably derived from the committed history, the system can diverge.

## Consumer Side

Outbox solves the producer-side handoff. Consumers still need a receiving mechanism.

When the delivery substrate can redeliver, consumers usually need [[Idempotency|idempotency]], expected-version checks, deduplication records, or a [[Transactional Inbox|transactional inbox]]. Without that consumer-side mechanism, outbox retry can produce duplicate downstream effects.

## Failure Modes

The pattern fails when downstream consumers assume broker delivery means immediate domain consistency, when the relay lacks idempotency, ordering scope, recovery, and duplicate-publication handling, or when consumer-side processing lacks an inbox or equivalent idempotent receiver.

Related concepts: [[Outbox|outbox]], [[Persistence|persistence]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Acknowledgments|acknowledgments]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Transactional Inbox|transactional inbox]], [[Dual-Write Problem|dual-write problem]], [[Event Sourcing|event sourcing]], [[Brokers|brokers]], [[Boundaries|boundaries]], [[Event-Driven Architecture|event-driven architecture]].
