---
realm: Operational Semantics
kind: operational-semantics
---

# Recovery

Recovery defines how a system returns to coherent operation after failure, interruption, conflict, timeout, overload, or partial progress.

Recovery depends on the durable material provided by [[Persistence]] and the method used for [[Reconstitution]].

Retry is one recovery mechanism, but recovery is broader than retry. Some failures are recovered by re-driving incomplete work, while others require replay, reconstitution, compensation, rebuilding, or operator intervention.

Recovery may include:

- Replaying event history.
- Loading snapshots and subsequent events.
- Resuming workflow history.
- Rebuilding projections.
- Restoring CRDT replica state and causal metadata.
- Re-driving outbox records.
- Retrying incomplete work.
- Resuming durable execution state or replaying durable execution history.
- Compensating completed work.
- Activating an actor by identity.

Recovery must preserve the meaning of entity versions, committed events, idempotency records, CRDT causal metadata, and observer boundaries. Otherwise, the system may recover operationally while changing its semantic history or breaking convergence.

In [[Safety and Liveness]] terms, recovery is a liveness mechanism constrained by safety. It should restore progress without inventing histories, duplicating non-idempotent effects, losing committed facts, or weakening the boundary's consistency claim.

Related concepts: [[Persistence]], [[Reconstitution]], [[Durable Execution]], [[Retry]], [[Idempotency]], [[Safety and Liveness]], [[Coordination]], [[Event Sourcing]], [[CRDTs]], [[Workflow Engines]], [[Durable Execution Engines]], [[Actor Systems]].
