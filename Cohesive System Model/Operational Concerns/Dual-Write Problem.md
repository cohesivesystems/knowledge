---
realm: Operational Concerns
kind: operational-concern
aliases:
  - Dual Write
  - Dual-Write
  - Dual Write Problem
---

# Dual-Write Problem

The dual-write problem is the failure mode that appears when one operation tries to commit two or more effects across independent commit boundaries without one atomic commit protocol or durable recovery protocol connecting them.

The common example is:

```txt
update database
publish message
```

but the problem is broader. A dual write may involve a database and broker, two databases, a broker acknowledgment and local state update, a workflow checkpoint and external API call, an entity transition and search-index update, or any pair of effects whose failure, retry, visibility, and recovery are not governed by the same [[Commit Boundaries|commit boundary]].

## Failure Shape

If the first effect commits and the second does not, the system may have durable state with no corresponding notification, projection update, or downstream process.

If the second effect commits and the first does not, downstream observers may react to a fact that is not actually committed in the authoritative state.

If the outcome is ambiguous, retries can create duplicate effects unless the receiver or target boundary has [[Idempotency|idempotency]], expected-version checks, deduplication records, or compensating recovery.

## Resolutions

The dual-write problem is resolved by changing the commit structure, not by hoping operations happen close together in time.

Common resolutions include:

- Put all required effects inside one local [[ACID]] transaction when one boundary is sufficient.
- Use [[Two-Phase Commit|two-phase commit]] or another distributed atomic commit protocol when the covered participants support it and the cost is acceptable.
- Use an [[Outbox|outbox]] so local state and publication responsibility commit atomically, then publish asynchronously with retry and recovery.
- Use a [[Transactional Inbox|transactional inbox]] or idempotent receiver so redelivered inputs do not duplicate local effects.
- Use [[Sagas|sagas]], [[Process Managers|process managers]], [[Durable Execution|durable execution]], compensation, reservations, or reconciliation when one atomic boundary is unavailable or misaligned with the business process.
- Use [[Event Sourcing|event sourcing]] so committed endogenous events are the authoritative durable basis for state reconstitution and downstream orchestration, when that history is the intended source of coordination.

Each option must state which stronger guarantee it replaces and what guarantees remain at each boundary.

Related concepts: [[Commit Boundaries|commit boundaries]], [[Effects|effects]], [[Persistence|persistence]], [[Coordination|coordination]], [[Recovery|recovery]], [[Delivery Semantics|delivery semantics]], [[Acknowledgments|acknowledgments]], [[Idempotency|idempotency]], [[Weak Isolation Patterns|weak isolation patterns]], [[Outbox|outbox]], [[Transactional Inbox|transactional inbox]], [[Event Sourcing|event sourcing]], [[ACID]], [[Two-Phase Commit|two-phase commit]], [[Business Transactions|business transactions]].
