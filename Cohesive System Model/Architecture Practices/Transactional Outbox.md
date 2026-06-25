---
realm: Architecture Practices
---

# Transactional Outbox

Realm: Architecture Practices

The Transactional Outbox addresses the problem of committing local state change and publishing a message without relying on a distributed transaction between the database and broker.

## Cohesive Formulation

The practice separates domain commitment from publication:

```txt
entity transition + outbox record commit in one persistence boundary
outbox relay -> broker interaction boundary
```

The outbox record is durable operational material that represents responsibility to publish after the domain transition commits.

## Practice Interpretation

The outbox makes acknowledgment spaces explicit. A database transaction can commit the entity transition and outbox record. Broker publication and downstream observation happen later, with their own delivery, ordering, retry, and idempotency semantics.

## Failure Modes

The pattern fails when downstream consumers assume broker delivery means immediate domain consistency, or when the relay lacks idempotency, ordering scope, recovery, and duplicate-publication handling.

Related concepts: [[Persistence]], [[Interaction]], [[Delivery Semantics]], [[Idempotency]], [[Retry]], [[Recovery]], [[Brokers]], [[Boundaries]], [[Event-Driven Architecture]].
