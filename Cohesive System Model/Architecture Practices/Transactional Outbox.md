---
realm: Architecture Practices
kind: architecture-practice
created: 2026-06-24
updated: 2026-07-05
---

# Transactional Outbox

Transactional outbox is the architecture practice of using an [[Outbox|outbox]] to tie an accepted local state change to downstream publication responsibility without a distributed transaction between storage and consumer.

## Architectural Context

Use transactional outbox when an accepted [[Transition|transition]] or semantic [[Process|process]] step must cause follow-up work outside the local commit boundary, but the system should not rely on [[Two-Phase Commit|two-phase commit]] across all participants.

The architecture decision considers:

- Which observer, entity, service, stream, or process boundary owns the local commit.
- What semantic obligation the outbox record represents: event publication, command dispatch, projection update, notification, or another effect.
- Which relay, projector, process manager, or runtime component reads the obligation.
- What ordering scope, retry policy, recovery path, acknowledgment timing, and duplicate-publication behavior apply.
- What downstream [[Idempotency|idempotency]], deduplication, or [[Transactional Inbox|transactional inbox]] mechanism protects consumers.

These choices determine the actual consistency claim. The outbox prevents a local [[Dual-Write Problem|dual-write problem]] between authoritative persistence and publication responsibility; it does not make downstream processing immediate, globally atomic, or exactly once.

## Relation to Adjacent Practices

In [[Event-Driven Architecture|event-driven architecture]], transactional outbox is a producer-side handoff mechanism. It helps publish facts or commands after local commitment, but the architecture still needs explicit event meanings, subscription boundaries, ordering scopes, and consumer guarantees.

In [[Event Sourcing|event sourcing]], the committed event history can already be the durable source for projections, subscriptions, process managers, and publications. A separate outbox is useful only when it is committed atomically with that history or derived reliably from it.

In designs built around [[Sagas|sagas]], [[Process Managers|process managers]], or [[Durable Execution|durable execution]], an outbox may be one material used to preserve pending effects. It is not the saga, process manager, workflow, or durable execution itself; those practices define broader process identity, progress, recovery, compensation, and coordination meanings.

## Failure Modes

Transactional outbox is being overclaimed when broker delivery is treated as proof of domain consistency, when consumers lack idempotent receiving behavior, when the relay has no durable progress or recovery model, or when the outbox record is written outside the same commit boundary as the state change that requires publication.

Related concepts: [[Outbox|outbox]], [[Cohesive System Model/Architecture Practices/Weak Isolation Patterns|weak isolation patterns as architecture practice]], [[Persistence|persistence]], [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Acknowledgments|acknowledgments]], [[Interaction|interaction]], [[Delivery Semantics|delivery semantics]], [[Idempotency|idempotency]], [[Retry|retry]], [[Recovery|recovery]], [[Transactional Inbox|transactional inbox]], [[Dual-Write Problem|dual-write problem]], [[Event Sourcing|event sourcing]], [[Process Managers|process managers]], [[Sagas|sagas]], [[Durable Execution|durable execution]], [[Brokers|brokers]], [[Boundaries|boundaries]], [[Event-Driven Architecture|event-driven architecture]].
